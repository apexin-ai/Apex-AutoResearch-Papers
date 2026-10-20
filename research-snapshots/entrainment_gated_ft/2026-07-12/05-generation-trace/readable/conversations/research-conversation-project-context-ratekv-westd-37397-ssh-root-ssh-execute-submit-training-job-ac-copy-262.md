# Research conversation: <project_context> # 项目: ratekv ## 运行环境 - 服务器名: westd-37397 - SSH 账户: root（调用 ssh_execute / submit_training_job 时传入 accou

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 55
- **Recorded user turns:** 1
- **Tool calls:** 15
- **Original source:** `logs/chats/exported-trajectories/account-3/0e163909-e397-4f29-9722-d542e29e1bd1.jsonl`
- **Structured JSON:** [`eecb7f075c2bb610cac2.json`](../../sessions/ee/eecb7f075c2bb610cac2.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-14T19:05:46.750Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-14T19:05:46.750Z",
  "sessionId": "0e163909-e397-4f29-9722-d542e29e1bd1",
  "content": "&lt;project_context>\n# 项目: ratekv\n\n## 运行环境\n- 服务器名: westd-37397\n- SSH 账户: root（调用 ssh_execute / submit_training_job 时传入 account=\"root\"）\n- SSH 连接命令: ssh westd-37397  # 必须用此命令，~/.ssh/config 自动应用密钥和跳板机，禁止用裸 IP\n- 项目代码根目录: /root/ratekv\n\n\n## 环境搭建\n连接服务器后先调 `detect_image` 检测是否为预置镜像。如果匹配，跳过基础环境搭建，只装项目特有依赖。已预装的包不要重复安装。\n\n## 输出风格\n回复简洁直接。只输出执行结果和必要信息，不要解释过程、不要客套、不要给未被要求的建议。\n&lt;/project_context>\n## 任务：更新 literature_map.yaml — 添加近期 KV cache 混合精度量化文献\n\n### 背景\n刚完成一轮文献调研 (artifacts/spike_vs_spread_literature.md)，发现多篇需要加入 literature_map.yaml 的论文。你的任务是读取当前 literature_map.yaml，然后根据调研报告添加缺失的论文条目。\n\n### 步骤\n1. 用 `read_project_file(project=\"ratekv\", file=\"literature_map.yaml\")` 读取当前 map\n2. 读取 `/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/artifacts/spike_vs_spread_literature.md` 获取新论文列表\n3. 对比，识别缺失的论文\n4. 用 `save_project_file` 更新 literature_map.yaml，添加缺失条目\n\n### 优先添加的论文（按重要性排序）\n1. **RateQuant** (arXiv:2605.06675, 2026-05) — role: direct-competitor — 最重要的竞争者，per-head bit allocation via rate-distortion theory\n2. **KVTuner** (ICML 2025) — role: direct-competitor — layer-level mixed-precision\n3. **KVmix** (AAAI 2026) — role: direct-competitor — gradient-based layer-level K/V allocation\n4. **HeadKV** (ICLR 2025) — role: background — head-level importance for eviction\n5. **AdaKV** (NeurIPS 2025) — role: background — adaptive per-head eviction budget\n6. **PM-KVQ** (2025) — role: method-component — progressive mixed-precision\n7. **MixKVQ** (2025) — role: method-component — query-aware mixed-precision\n8. **KITTY** (2025) — role: background — channel-wise precision for KV cache\n9. **MUXQ** (2026) — role: background — low-rank outlier decomposition\n\n### 格式要求\n- 匹配现有 literature_map.yaml 的 YAML 格式\n- 每个条目必须有: title, authors, venue, year, arxiv_id (如果有), role, relevance (一句话说明与我们的关系)\n- role 可选: direct-competitor, method-component, background, evaluation\n- 不要重复添加已有的条目"
}
```

---

### Runtime record

_source line 2 · 2026-05-14T19:05:46.754Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-14T19:05:46.754Z",
  "sessionId": "0e163909-e397-4f29-9722-d542e29e1bd1"
}
```

---

## Round 1

53 recorded events

### User

_source line 3 · 2026-05-14T19:05:46.788Z_

&lt;project_context>
# 项目: ratekv

## 运行环境
- 服务器名: westd-37397
- SSH 账户: root（调用 ssh_execute / submit_training_job 时传入 account="root"）
- SSH 连接命令: ssh westd-37397  # 必须用此命令，~/.ssh/config 自动应用密钥和跳板机，禁止用裸 IP
- 项目代码根目录: /root/ratekv


## 环境搭建
连接服务器后先调 `detect_image` 检测是否为预置镜像。如果匹配，跳过基础环境搭建，只装项目特有依赖。已预装的包不要重复安装。

## 输出风格
回复简洁直接。只输出执行结果和必要信息，不要解释过程、不要客套、不要给未被要求的建议。
&lt;/project_context>
## 任务：更新 literature_map.yaml — 添加近期 KV cache 混合精度量化文献

### 背景
刚完成一轮文献调研 (artifacts/spike_vs_spread_literature.md)，发现多篇需要加入 literature_map.yaml 的论文。你的任务是读取当前 literature_map.yaml，然后根据调研报告添加缺失的论文条目。

### 步骤
1. 用 `read_project_file(project="ratekv", file="literature_map.yaml")` 读取当前 map
2. 读取 `/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/artifacts/spike_vs_spread_literature.md` 获取新论文列表
3. 对比，识别缺失的论文
4. 用 `save_project_file` 更新 literature_map.yaml，添加缺失条目

### 优先添加的论文（按重要性排序）
1. **RateQuant** (arXiv:2605.06675, 2026-05) — role: direct-competitor — 最重要的竞争者，per-head bit allocation via rate-distortion theory
2. **KVTuner** (ICML 2025) — role: direct-competitor — layer-level mixed-precision
3. **KVmix** (AAAI 2026) — role: direct-competitor — gradient-based layer-level K/V allocation
4. **HeadKV** (ICLR 2025) — role: background — head-level importance for eviction
5. **AdaKV** (NeurIPS 2025) — role: background — adaptive per-head eviction budget
6. **PM-KVQ** (2025) — role: method-component — progressive mixed-precision
7. **MixKVQ** (2025) — role: method-component — query-aware mixed-precision
8. **KITTY** (2025) — role: background — channel-wise precision for KV cache
9. **MUXQ** (2026) — role: background — low-rank outlier decomposition

### 格式要求
- 匹配现有 literature_map.yaml 的 YAML 格式
- 每个条目必须有: title, authors, venue, year, arxiv_id (如果有), role, relevance (一句话说明与我们的关系)
- role 可选: direct-competitor, method-component, background, evaluation
- 不要重复添加已有的条目

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "964448b9-9407-4006-b5f8-3afa58950999",
  "type": "user",
  "uuid": "43cbe0c0-3f12-46b3-9cb7-f25542858a54",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "0e163909-e397-4f29-9722-d542e29e1bd1",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-14T19:05:46.787Z_

```json
{
  "parentUuid": "43cbe0c0-3f12-46b3-9cb7-f25542858a54",
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
  "uuid": "8bb347bf-8f7c-462c-8ecd-5b362de95dfa",
  "timestamp": "2026-05-14T19:05:46.787Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "0e163909-e397-4f29-9722-d542e29e1bd1",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Runtime record

_source line 5 · 2026-05-14T19:05:46.787Z_

```json
{
  "parentUuid": "8bb347bf-8f7c-462c-8ecd-5b362de95dfa",
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
  "uuid": "077c6df3-7557-4edd-a56f-a2fa3ea8a6a9",
  "timestamp": "2026-05-14T19:05:46.787Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "0e163909-e397-4f29-9722-d542e29e1bd1",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Runtime record

_source line 6 · 2026-05-14T19:05:46.787Z_

```json
{
  "parentUuid": "077c6df3-7557-4edd-a56f-a2fa3ea8a6a9",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "7433bbe5-77cc-4b9a-8560-43ae7fec73f4",
  "timestamp": "2026-05-14T19:05:46.787Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "0e163909-e397-4f29-9722-d542e29e1bd1",
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
  "aiTitle": "Update literature map with KV cache quantization papers",
  "sessionId": "0e163909-e397-4f29-9722-d542e29e1bd1"
}
```

---

### Assistant

_source line 8 · 2026-05-14T19:05:49.906Z_

I'll start by reading the current literature map and the survey report.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7433bbe5-77cc-4b9a-8560-43ae7fec73f4",
  "isSidechain": false,
  "requestId": "req_011Cb2z1ZUVzjNCwFknpMfNF",
  "type": "assistant",
  "uuid": "41c55c7f-eab4-43aa-bb02-819c20b1567f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "0e163909-e397-4f29-9722-d542e29e1bd1",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LBL9YgKduC9Y1qwM4YH9AX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11991,
      "cache_read_input_tokens": 11841,
      "output_tokens": 118,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11991,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 118,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11991,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11991
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

_source line 9 · 2026-05-14T19:05:50.681Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01DVF8W1Dba7rUqFHDBq8V21`</summary>

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
  "parentUuid": "41c55c7f-eab4-43aa-bb02-819c20b1567f",
  "isSidechain": false,
  "requestId": "req_011Cb2z1ZUVzjNCwFknpMfNF",
  "type": "assistant",
  "uuid": "744489f8-18e6-4df9-b0b3-fc4d625f4f7c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "0e163909-e397-4f29-9722-d542e29e1bd1",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LBL9YgKduC9Y1qwM4YH9AX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11991,
      "cache_read_input_tokens": 11841,
      "output_tokens": 118,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11991,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 118,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11991,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11991
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

_source line 10 · 2026-05-14T19:05:50.695Z_

<details><summary>↩ Tool result · `toolu_01DVF8W1Dba7rUqFHDBq8V21`</summary>

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
  "parentUuid": "744489f8-18e6-4df9-b0b3-fc4d625f4f7c",
  "isSidechain": false,
  "promptId": "964448b9-9407-4006-b5f8-3afa58950999",
  "type": "user",
  "uuid": "2ff0186c-d557-46c6-b8c8-318d647ffb90",
  "toolUseResult": {
    "matches": [
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__save_project_file"
    ],
    "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__save_project_file",
    "total_deferred_tools": 22
  },
  "sourceToolAssistantUUID": "744489f8-18e6-4df9-b0b3-fc4d625f4f7c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "0e163909-e397-4f29-9722-d542e29e1bd1",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 11 · 2026-05-14T19:05:53.956Z_

<details><summary>Logged reasoning block</summary>

```text
Let me read the current literature map and the survey report in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2ff0186c-d557-46c6-b8c8-318d647ffb90",
  "isSidechain": false,
  "requestId": "req_011Cb2z1rLm1qi1UH1BbKWfk",
  "type": "assistant",
  "uuid": "1e70cdc1-4d46-4a0e-93e4-c4d80b775e66",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "0e163909-e397-4f29-9722-d542e29e1bd1",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P5feUHLTE9ceaexEv4cCGM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 714,
      "cache_read_input_tokens": 23832,
      "output_tokens": 208,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 714,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 208,
          "cache_read_input_tokens": 23832,
          "cache_creation_input_tokens": 714,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 714
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

_source line 12 · 2026-05-14T19:05:54.897Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01PjBVGcFJbpRxb5SKiSVS2a`</summary>

```json
{
  "project": "ratekv",
  "file": "literature_map.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1e70cdc1-4d46-4a0e-93e4-c4d80b775e66",
  "isSidechain": false,
  "requestId": "req_011Cb2z1rLm1qi1UH1BbKWfk",
  "type": "assistant",
  "uuid": "540b7bd7-a7b9-49bb-b9c2-76f662a7a87b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "0e163909-e397-4f29-9722-d542e29e1bd1",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P5feUHLTE9ceaexEv4cCGM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 714,
      "cache_read_input_tokens": 23832,
      "output_tokens": 208,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 714,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 208,
          "cache_read_input_tokens": 23832,
          "cache_creation_input_tokens": 714,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 714
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

_source line 13 · 2026-05-14T19:05:54.931Z_

<details><summary>↩ Tool result · `toolu_01PjBVGcFJbpRxb5SKiSVS2a`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/literature_map.yaml\", \"content\": \"meta:\\n  last_updated: '2026-05-14T10:30:00.000Z'\\n  total_papers: 35\\ncategories:\\n  - Mixed-Precision Rate-Distortion\\n  - KV Cache Quantization\\n  - KV Cache Eviction\\n  - Model Compression\\n  - Attention Head Analysis\\n  - LLM Inference Efficiency\\n  - Evaluation Models\\n  - Theory\\npapers:\\n  # ============================================================\\n  # Cluster 1: Mixed-Precision R-D Allocation (5 papers)\\n  # ============================================================\\n  zuo2026ratequant:\\n    title: 'RateQuant: Optimal Mixed-Precision KV Cache Quantization via Rate-Distortion Theory'\\n    authors:\\n    - Fei Zuo\\n    - Zikang Zhou\\n    - Hao Cong\\n    - Xiaoyan Xi\\n    - Ho Fai Leung\\n    year: 2026\\n    venue: arXiv 2026\\n    url: ''\\n    doi: '2605.06675'\\n    bibtex_key: zuo2026ratequant\\n    category: Mixed-Precision Rate-Distortion\\n    role: direct-competitor\\n    relevance: 'Primary competitor: R-D optimal per-head KV cache bit allocation. Algorithm 1 (discrete greedy). Theorem 2 (continuous closed-form via reverse waterfilling). Proposition 6 (greedy optimality on consecutive integers). Key limitation: does not address hardware-aligned non-consecutive {2,4,8,16} where greedy may fail.'\\n    abstract: RateQuant fits a per-quantizer distortion model D(b)=alpha*beta^{-b} from a small calibration set, then solves the bit-allocation in closed form via reverse waterfilling from rate-distortion theory. On Qwen3-8B at 2.5 avg bits, calibrated RateQuant reduces KIVI perplexity from 49.3 to 14.9 (70% reduction). Calibration takes 1.6s on a single GPU with zero inference overhead.\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research\\n    added_at: '2026-05-14T08:42:26.710Z'\\n  lei2026arkv:\\n    title: 'ARKV: Adaptive and Resource-Efficient KV Cache Management under Limited Memory Budget for Long-Context Inference in LLMs'\\n    authors:\\n    - Jianlong Lei\\n    - Shashikant Ilager\\n    year: 2026\\n    venue: arXiv 2026\\n    url: ''\\n    doi: '2603.08727'\\n    bibtex_key: lei2026arkv\\n    category: Mixed-Precision Rate-Distortion\\n    role: direct-competitor\\n    relevance: Adaptive mixed-precision KV cache with tri-state token assignment (Original/Quantization/Eviction). Per-layer OQ ratio estimation via attention entropy, variance, kurtosis. Alternative adaptive allocation strategy to our R-D formulation.\\n    abstract: 'ARKV dynamically allocates precision levels to cached tokens based on per-layer attention dynamics and token-level importance. Three components: per-layer OQ ratio estimation, token importance scoring, and tri-state cache assignment. Preserves ~97% baseline accuracy with 4x KV memory reduction.'\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research\\n    added_at: '2026-05-14T08:42:26.710Z'\\n  li2025kvmix:\\n    title: 'KVmix: Gradient-Based Layer Importance-Aware Mixed-Precision Quantization for KV Cache'\\n    authors:\\n    - Fei Li\\n    - Song Liu\\n    - Weiguo Wu\\n    - Shiqiang Nie\\n    - Jinyu Wang\\n    year: 2025\\n    venue: arXiv 2025\\n    url: ''\\n    doi: '2506.08018'\\n    bibtex_key: li2025kvmix\\n    category: Mixed-Precision Rate-Distortion\\n    role: method-component\\n    relevance: Gradient-based importance for layer-wise KV cache bit-width allocation. Heuristic sensitivity-based approach vs our R-D optimal formulation. Achieves near-lossless at Key 2.19bit / Value 2.38bit.\\n    abstract: KVmix employs gradient-based importance analysis to evaluate how individual Key and Value projection matrices affect model loss, enabling layer-specific bit-width allocation. Includes dynamic long-context optimization preserving full-precision KV pairs for recent pivotal tokens.\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research\\n    added_at: '2026-05-14T08:42:26.710Z'\\n  zhang2025mixkvq:\\n    title: 'MixKVQ: Query-Aware Mixed-Precision KV Cache Quantization for Long-Context Reasoning'\\n    authors:\\n    - Tao Zhang\\n    - Ziqian Zeng\\n    - Hao Peng\\n    - Huiping Zhuang\\n    - Cen Chen\\n    year: 2025\\n    venue: arXiv 2025\\n    url: ''\\n    doi: '2512.19206'\\n    bibtex_key: zhang2025mixkvq\\n    category: Mixed-Precision Rate-Distortion\\n    role: method-component\\n    relevance: 'Query-aware channel-level mixed-precision for KV cache. Orthogonal to our per-head R-D allocation: operates at channel granularity rather than head granularity.'\\n    abstract: MixKVQ introduces a lightweight query-aware algorithm to identify and preserve critical key channels at higher precision while applying per-token quantization for value cache. Outperforms existing low-bit methods on complex reasoning datasets.\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research\\n    added_at: '2026-05-14T08:42:26.710Z'\\n  kim2024squeezellm:\\n    title: 'SqueezeLLM: Dense-and-Sparse Quantization'\\n    authors:\\n    - Sehoon Kim\\n    - Coleman Hooper\\n    - Amir Gholami\\n    - Zhen Dong\\n    - Xiuyu Li\\n    - Sheng Shen\\n    - Michael W. Mahoney\\n    - Kurt Keutzer\\n    year: 2024\\n    venue: ICML 2024\\n    url: ''\\n    doi: '2306.07629'\\n    bibtex_key: kim2024squeezellm\\n    category: Mixed-Precision Rate-Distortion\\n    role: foundation\\n    relevance: Foundational sensitivity-based non-uniform quantization using second-order information. Pioneered per-group precision assignment based on sensitivity—principle we extend to per-head KV cache R-D allocation.\\n    abstract: 'SqueezeLLM enables lossless compression to ultra-low 3-bit precision via two ideas: sensitivity-based non-uniform quantization searching for optimal bit precision assignment, and Dense-and-Sparse decomposition storing outliers in efficient sparse format.'\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research\\n    added_at: '2026-05-14T08:42:26.710Z'\\n\\n  # ============================================================\\n  # Cluster 2: KV Cache Quantization (6 papers)\\n  # ============================================================\\n  liu2024kivi:\\n    title: 'KIVI: A Tuning-Free Asymmetric 2bit Quantization for KV Cache'\\n    authors:\\n    - Zirui Liu\\n    - Jiayi Yuan\\n    - Hongye Jin\\n    - Shaochen Zhong\\n    - Zhaozhuo Xu\\n    - Vladimir Braverman\\n    - Beidi Chen\\n    - Xia Hu\\n    year: 2024\\n    venue: ICML 2024\\n    url: ''\\n    doi: '2402.02750'\\n    bibtex_key: liu2024kivi\\n    category: KV Cache Quantization\\n    role: direct-competitor\\n    relevance: Asymmetric per-channel key / per-token value 2-bit KV cache quantization; tuning-free baseline for mixed-precision KV cache methods\\n    abstract: We conduct a comprehensive study on the element distribution in KV cache of popular LLMs and find that the key cache should be quantized per-channel while the value cache should be quantized per-token. From this observation, we develop a tuning-free 2bit KV cache quantization algorithm named KIVI.\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research\\n    added_at: '2026-05-14T07:56:45.265Z'\\n  hooper2024kvquant:\\n    title: 'KVQuant: Towards 10 Million Context Length LLM Inference with KV Cache Quantization'\\n    authors:\\n    - Coleman Hooper\\n    - Sehoon Kim\\n    - Hiva Mohammadzadeh\\n    - Michael W. Mahoney\\n    - Yakun Sophia Shao\\n    - Kurt Keutzer\\n    - Amir Gholami\\n    year: 2024\\n    venue: NeurIPS 2024\\n    url: ''\\n    doi: '2401.18079'\\n    bibtex_key: hooper2024kvquant\\n    category: KV Cache Quantization\\n    role: direct-competitor\\n    relevance: Per-channel key quantization with pre-RoPE, non-uniform datatypes, and dense-and-sparse outlier handling; achieves sub-4-bit KV cache for 10M context\\n    abstract: KV cache activations are the dominant contributor to memory consumption during LLM inference for large context windows. We address this with per-channel key quantization, pre-RoPE key quantization, non-uniform KV cache quantization, and per-vector dense-and-sparse quantization to isolate outliers.\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research\\n    added_at: '2026-05-14T07:56:45.265Z'\\n  lin2024qserve:\\n    title: 'QServe: W4A8KV4 Quantization and System Co-design for Efficient LLM Serving'\\n    authors:\\n    - Yujun Lin\\n    - Haotian Tang\\n    - Shang Yang\\n    - Zhekai Zhang\\n    - Guangxuan Xiao\\n    - Chuang Gan\\n    - Song Han\\n    year: 2024\\n    venue: MLSys 2025\\n    url: ''\\n    doi: '2405.04532'\\n    bibtex_key: lin2024qserve\\n    category: KV Cache Quantization\\n    role: foundation\\n    relevance: W4A8KV4 co-design with SmoothAttention for KV4 quantization; demonstrates system-level gains from joint weight-activation-KV quantization\\n    abstract: QServe introduces QoQ (W4A8KV4), a quantization algorithm with 4-bit weight, 8-bit activation, and 4-bit KV cache. Progressive group quantization ensures all GEMMs run on INT8 tensor cores. SmoothAttention shifts quantization difficulty from keys to queries.\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research\\n    added_at: '2026-05-14T07:56:45.265Z'\\n  he2024zipcache:\\n    title: 'ZipCache: Accurate and Efficient KV Cache Quantization with Salient Token Identification'\\n    authors:\\n    - Yefei He\\n    - Luoming Zhang\\n    - Weijia Wu\\n    - Jing Liu\\n    - Hong Zhou\\n    - Bohan Zhuang\\n    year: 2024\\n    venue: NeurIPS 2024\\n    url: ''\\n    doi: '2405.14256'\\n    bibtex_key: he2024zipcache\\n    category: KV Cache Quantization\\n    role: direct-competitor\\n    relevance: Channel-separable tokenwise quantization with adaptive bit-width based on normalized attention score saliency; mixed-precision KV cache baseline\\n    abstract: ZipCache proposes channel-separable tokenwise quantization and uses normalized attention score for identifying salient tokens with adaptive bit-width assignment. Achieves 4.98x compression on Mistral-7B with 0.38% accuracy drop.\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research\\n    added_at: '2026-05-14T07:56:45.265Z'\\n  kang2024gear:\\n    title: 'GEAR: An Efficient KV Cache Compression Recipe for Near-Lossless Generative Inference of LLM'\\n    authors:\\n    - Hao Kang\\n    - Qingru Zhang\\n    - Souvik Kundu\\n    - Geonhwa Jeong\\n    - Zaoxing Liu\\n    - Tushar Krishna\\n    - Tuo Zhao\\n    year: 2024\\n    venue: arXiv 2024\\n    url: ''\\n    doi: '2403.05527'\\n    bibtex_key: kang2024gear\\n    category: KV Cache Quantization\\n    role: direct-competitor\\n    relevance: Hybrid quantization + low-rank + sparse error correction for KV cache; demonstrates that residual compensation improves ultra-low-bit quantization quality\\n    abstract: GEAR first applies quantization to majority of entries to ultra-low precision, then employs a low rank matrix to approximate the quantization error, and a sparse matrix to remedy individual errors from outlier entries. Achieves near-lossless 4-bit compression with 2.38x throughput improvement.\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research\\n    added_at: '2026-05-14T07:56:45.265Z'\\n  duanmu2024skvq:\\n    title: 'SKVQ: Sliding-window Key and Value Cache Quantization for Large Language Models'\\n    authors:\\n    - Haojie Duanmu\\n    - Zhihang Yuan\\n    - Xiuhong Li\\n    - Jiangfei Duan\\n    - Xingcheng Zhang\\n    - Dahua Lin\\n    year: 2024\\n    venue: arXiv 2024\\n    url: ''\\n    doi: '2405.06219'\\n    bibtex_key: duanmu2024skvq\\n    category: KV Cache Quantization\\n    role: direct-competitor\\n    relevance: Channel rearrangement + sliding-window high-precision recent tokens; achieves 2-bit key / 1.5-bit value with minimal accuracy loss\\n    abstract: SKVQ rearranges KV cache channels to improve similarity within quantization groups and applies clipped dynamic quantization at group level. Preserves recent window tokens at high precision. Enables 2-bit keys and 1.5-bit values with up to 1M context on 80GB GPU.\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research\\n    added_at: '2026-05-14T07:56:45.265Z'\\n\\n  # ============================================================\\n  # Cluster 3: KV Cache Eviction (6 papers)\\n  # ============================================================\\n  zhang2023h2o:\\n    title: 'H2O: Heavy-Hitter Oracle for Efficient Generative Inference of Large Language Models'\\n    authors:\\n    - Zhenyu Zhang\\n    - Ying Sheng\\n    - Tianyi Zhou\\n    - Tianlong Chen\\n    - Lianmin Zheng\\n    - Ruisi Cai\\n    - Zhao Song\\n    - Yuandong Tian\\n    - Christopher Re\\n    - Clark Barrett\\n    - Zhangyang Wang\\n    - Beidi Chen\\n    year: 2023\\n    venue: NeurIPS 2023\\n    url: ''\\n    doi: 10.48550/arXiv.2306.14048\\n    bibtex_key: zhang2023h2o\\n    category: KV Cache Eviction\\n    role: background\\n    relevance: Foundational KV cache eviction policy based on heavy-hitter tokens; orthogonal to our quantization approach\\n    abstract: H2O identifies Heavy Hitters — a small set of tokens contributing most to attention scores — and dynamically retains recent and H2 tokens. With 20% heavy hitters, H2O improves throughput by up to 29x and reduces KV cache memory by up to 5x.\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research\\n    added_at: '2026-05-14T08:10:15.562Z'\\n  li2024snapkv:\\n    title: 'SnapKV: LLM Knows What You are Looking for Before Generation'\\n    authors:\\n    - Yuhong Li\\n    - Yingbing Huang\\n    - Bowen Yang\\n    - Bharat Venkitesh\\n    - Acyr Locatelli\\n    - Hanchen Ye\\n    - Tianle Cai\\n    - Patrick Lewis\\n    - Deming Chen\\n    year: 2024\\n    venue: NeurIPS 2024\\n    url: ''\\n    doi: 10.48550/arXiv.2404.14469\\n    bibtex_key: li2024snapkv\\n    category: KV Cache Eviction\\n    role: background\\n    relevance: Observation-driven KV cache compression using attention pattern consistency; competes with eviction-based approaches our work compares against\\n    abstract: SnapKV efficiently minimizes KV cache size by selecting clustered important KV positions per attention head using an observation window at the end of the prompt. Achieves 3.6x speed increase and 8.2x memory efficiency at 16K tokens.\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research\\n    added_at: '2026-05-14T08:10:15.562Z'\\n  ge2024fastgen:\\n    title: 'Model Tells You What to Discard: Adaptive KV Cache Compression for LLMs'\\n    authors:\\n    - Suyu Ge\\n    - Yunan Zhang\\n    - Liyuan Liu\\n    - Minjia Zhang\\n    - Jiawei Han\\n    - Jianfeng Gao\\n    year: 2024\\n    venue: ICLR 2024\\n    url: ''\\n    doi: 10.48550/arXiv.2310.01801\\n    bibtex_key: ge2024fastgen\\n    category: KV Cache Eviction\\n    role: background\\n    relevance: Adaptive per-head eviction strategy (FastGen); demonstrates head-specific compression is beneficial, complementary to quantization\\n    abstract: 'FastGen constructs KV cache adaptively per attention head: evicting long-range contexts on local-attention heads, discarding non-special tokens on special-token-focused heads, and using standard KV cache for broad-attention heads. Reduces memory by 50% without sacrificing quality.'\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research\\n    added_at: '2026-05-14T08:10:15.562Z'\\n  xiao2024streamingllm:\\n    title: Efficient Streaming Language Models with Attention Sinks\\n    authors:\\n    - Guangxuan Xiao\\n    - Yuandong Tian\\n    - Beidi Chen\\n    - Song Han\\n    - Mike Lewis\\n    year: 2024\\n    venue: ICLR 2024\\n    url: ''\\n    doi: 10.48550/arXiv.2309.17453\\n    bibtex_key: xiao2024streamingllm\\n    category: KV Cache Eviction\\n    role: background\\n    relevance: Discovers attention sink phenomenon in initial tokens; motivates why naive eviction can fail and informs our quantization-first approach\\n    abstract: StreamingLLM enables LLMs to generalize to infinite sequence lengths without fine-tuning by retaining attention sink tokens alongside a sliding window of recent tokens. Achieves up to 22.2x speedup over sliding window recomputation.\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research\\n    added_at: '2026-05-14T08:10:15.562Z'\\n  liu2024scissorhands:\\n    title: 'Scissorhands: Exploiting the Persistence of Importance Hypothesis for LLM KV Cache Compression at Test Time'\\n    authors:\\n    - Zichang Liu\\n    - Aditya Desai\\n    - Fangshuo Liao\\n    - Weitao Wang\\n    - Victor Xie\\n    - Zhaozhuo Xu\\n    - Anastasios Kyrillidis\\n    - Anshumali Shrivastava\\n    year: 2024\\n    venue: NeurIPS 2023\\n    url: ''\\n    doi: 10.48550/arXiv.2305.17118\\n    bibtex_key: liu2024scissorhands\\n    category: KV Cache Eviction\\n    role: background\\n    relevance: Persistence-of-importance hypothesis for KV cache eviction; achieves 5x cache reduction, combinable with 4-bit quantization for 20x compression\\n    abstract: Scissorhands maintains KV cache at a fixed budget by storing pivotal tokens with higher probability, achieving up to 5x memory reduction without quality loss, and up to 20x when combined with 4-bit quantization.\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research\\n    added_at: '2026-05-14T08:10:15.562Z'\\n  yang2024pyramidinfer:\\n    title: 'PyramidInfer: Pyramid KV Cache Compression for High-throughput LLM Inference'\\n    authors:\\n    - Dongjie Yang\\n    - Xiaodong Han\\n    - Yan Gao\\n    - Yao Hu\\n    - Shilin Zhang\\n    - Hai Zhao\\n    year: 2024\\n    venue: Findings of ACL 2024\\n    url: ''\\n    doi: 10.48550/arXiv.2405.12532\\n    bibtex_key: yang2024pyramidinfer\\n    category: KV Cache Eviction\\n    role: background\\n    relevance: Layer-wise pyramid compression exploiting inter-layer dependency; crucial KV count decreases across layers, relevant to our per-layer rate allocation\\n    abstract: PyramidInfer compresses KV cache by layer-wise retaining crucial context, exploiting the finding that crucial keys and values decrease layer by layer. Achieves 2.2x throughput improvement with 54% GPU memory reduction.\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research\\n    added_at: '2026-05-14T08:10:15.562Z'\\n\\n  # ============================================================\\n  # Cluster 4: Model Compression (6 papers)\\n  # ============================================================\\n  frantar2023gptq:\\n    title: 'GPTQ: Accurate Post-Training Quantization for Generative Pre-trained Transformers'\\n    authors:\\n    - Elias Frantar\\n    - Saleh Ashkboos\\n    - Torsten Hoefler\\n    - Dan Alistarh\\n    year: 2023\\n    venue: ICLR 2023\\n    url: ''\\n    doi: '2210.17323'\\n    bibtex_key: frantar2023gptq\\n    category: Model Compression\\n    role: foundation\\n    relevance: Foundational one-shot weight quantization based on approximate second-order information (OBQ). Reduces bitwidth to 3-4 bits per weight with negligible accuracy degradation. Established post-training quantization paradigm for LLMs.\\n    abstract: GPTQ is a one-shot weight quantization method based on approximate second-order information that can quantize GPT models with 175 billion parameters in approximately four GPU hours, reducing bitwidth to 3 or 4 bits per weight with negligible accuracy degradation.\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: literature-survey\\n    added_at: '2026-05-14T10:30:00.000Z'\\n  lin2024awq:\\n    title: 'AWQ: Activation-aware Weight Quantization for LLM Compression and Acceleration'\\n    authors:\\n    - Ji Lin\\n    - Jiaming Tang\\n    - Haotian Tang\\n    - Shang Yang\\n    - Wei-Ming Chen\\n    - Wei-Chen Wang\\n    - Guangxuan Xiao\\n    - Xingyu Dang\\n    - Chuang Gan\\n    - Song Han\\n    year: 2024\\n    venue: MLSys 2024 (Best Paper)\\n    url: ''\\n    doi: '2306.00978'\\n    bibtex_key: lin2024awq\\n    category: Model Compression\\n    role: foundation\\n    relevance: Activation-aware salient weight protection via equivalent scaling transformation. Demonstrates that 1% salient weights dominate quantization quality—analogous to our finding that per-head sensitivity varies drastically.\\n    abstract: AWQ finds that protecting only 1% salient weights (identified by activation distribution, not weights) greatly reduces quantization error. Scales salient channels via mathematically equivalent transformation. No backpropagation or reconstruction needed. 3x speedup over FP16.\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: literature-survey\\n    added_at: '2026-05-14T10:30:00.000Z'\\n  xiao2023smoothquant:\\n    title: 'SmoothQuant: Accurate and Efficient Post-Training Quantization for Large Language Models'\\n    authors:\\n    - Guangxuan Xiao\\n    - Ji Lin\\n    - Mickael Seznec\\n    - Hao Wu\\n    - Julien Demouth\\n    - Song Han\\n    year: 2023\\n    venue: ICML 2023\\n    url: ''\\n    doi: '2211.10438'\\n    bibtex_key: xiao2023smoothquant\\n    category: Model Compression\\n    role: foundation\\n    relevance: Smooths activation outliers by migrating quantization difficulty from activations to weights. Enables W8A8 for all matmuls in LLMs. QServe's SmoothAttention extends this idea to KV cache.\\n    abstract: SmoothQuant enables INT8 quantization of both weights and activations for all matrix multiplications in LLMs by smoothing activation outliers via offline migration of quantization difficulty from activations to weights. Up to 1.56x speedup and 2x memory reduction with negligible accuracy loss.\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: literature-survey\\n    added_at: '2026-05-14T10:30:00.000Z'\\n  dettmers2022llmint8:\\n    title: 'LLM.int8(): 8-bit Matrix Multiplication for Transformers at Scale'\\n    authors:\\n    - Tim Dettmers\\n    - Mike Lewis\\n    - Younes Belkada\\n    - Luke Zettlemoyer\\n    year: 2022\\n    venue: NeurIPS 2022\\n    url: ''\\n    doi: '2208.07339'\\n    bibtex_key: dettmers2022llmint8\\n    category: Model Compression\\n    role: foundation\\n    relevance: First to identify emergent outlier features in transformers that dominate quantization quality. Mixed-precision decomposition (0.1% in FP16, 99.9% in INT8) is conceptually related to our per-head mixed-precision allocation.\\n    abstract: LLM.int8() develops Int8 matrix multiplication for feed-forward and attention projection layers via absmax vector-wise quantization and mixed precision decomposition. Cuts inference memory by half while retaining full precision performance for 175B-parameter models.\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: literature-survey\\n    added_at: '2026-05-14T10:30:00.000Z'\\n  tseng2024quipsharp:\\n    title: 'QuIP#: Even Better LLM Quantization with Hadamard Incoherence and Lattice Codebooks'\\n    authors:\\n    - Albert Tseng\\n    - Jerry Chee\\n    - Qingyao Sun\\n    - Volodymyr Kuleshov\\n    - Christopher De Sa\\n    year: 2024\\n    venue: ICML 2024\\n    url: ''\\n    doi: '2402.04396'\\n    bibtex_key: tseng2024quipsharp\\n    category: Model Compression\\n    role: foundation\\n    relevance: State-of-the-art extreme compression (2-bit weights) via Hadamard incoherence processing and E8 lattice codebooks. Theoretical grounding for why incoherent distributions quantize better—relevant to understanding per-head distortion variation.\\n    abstract: QuIP# achieves state-of-the-art in extreme weight compression using randomized Hadamard transform for incoherence processing, E8 lattice codebooks for vector quantization of sub-Gaussian incoherent weights, and fine-tuning for fidelity. Hardware-efficient implementation.\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: literature-survey\\n    added_at: '2026-05-14T10:30:00.000Z'\\n  zhao2024atom:\\n    title: 'Atom: Low-bit Quantization for Efficient and Accurate LLM Serving'\\n    authors:\\n    - Yilong Zhao\\n    - Chien-Yu Lin\\n    - Kan Zhu\\n    - Zihao Ye\\n    - Lequn Chen\\n    - Size Zheng\\n    - Luis Ceze\\n    - Arvind Krishnamurthy\\n    - Tianqi Chen\\n    - Baris Kasikci\\n    year: 2024\\n    venue: MLSys 2024\\n    url: ''\\n    doi: '2310.19102'\\n    bibtex_key: zhao2024atom\\n    category: Model Compression\\n    role: foundation\\n    relevance: End-to-end low-bit quantization for serving with mixed-precision, group quantization, and KV cache quantization. Demonstrates system-level throughput gains (3.5x over FP16) from co-designed quantization kernels.\\n    abstract: Atom combines mixed-precision quantization retaining salient activations/weights in high precision, fine-grained group quantization, dynamic activation quantization, KV-cache quantization, and efficient CUDA kernels. Achieves 7.73x throughput over FP16 baseline.\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: literature-survey\\n    added_at: '2026-05-14T10:30:00.000Z'\\n\\n  # ============================================================\\n  # Cluster 5: Attention Head Analysis (4 papers)\\n  # ============================================================\\n  voita2019heads:\\n    title: 'Analyzing Multi-Head Self-Attention: Specialized Heads Do the Heavy Lifting, the Rest Can Be Pruned'\\n    authors:\\n    - Elena Voita\\n    - David Talbot\\n    - Fedor Moiseev\\n    - Rico Sennrich\\n    - Ivan Titov\\n    year: 2019\\n    venue: ACL 2019\\n    url: ''\\n    doi: '1905.09418'\\n    bibtex_key: voita2019heads\\n    category: Attention Head Analysis\\n    role: foundation\\n    relevance: Foundational work on attention head specialization and pruning. Shows most heads can be pruned (38/48 with only 0.15 BLEU drop). Motivates our per-head heterogeneous quantization—heads have different importance and roles.\\n    abstract: Evaluates individual attention head contributions and identifies specialized heads playing consistent linguistically-interpretable roles. Using stochastic gates with L0 penalty, the vast majority of heads can be pruned without seriously affecting performance.\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: literature-survey\\n    added_at: '2026-05-14T10:30:00.000Z'\\n  michel2019sixteen:\\n    title: Are Sixteen Heads Really Better than One?\\n    authors:\\n    - Paul Michel\\n    - Omer Levy\\n    - Graham Neubig\\n    year: 2019\\n    venue: NeurIPS 2019\\n    url: ''\\n    doi: '1905.10650'\\n    bibtex_key: michel2019sixteen\\n    category: Attention Head Analysis\\n    role: foundation\\n    relevance: Shows large proportion of attention heads can be removed at test time. Greedy pruning analysis reveals varying head importance. Directly supports our premise that heads deserve different quantization precision.\\n    abstract: A large proportion of attention heads can be removed at test time without significantly impacting performance, and some layers can be reduced to a single head. Self-attention layers can be significantly pruned while encoder-decoder layers are more dependent on multi-headedness.\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: literature-survey\\n    added_at: '2026-05-14T10:30:00.000Z'\\n  clark2019bert:\\n    title: What Does BERT Look At? An Analysis of BERT's Attention\\n    authors:\\n    - Kevin Clark\\n    - Urvashi Khandelwal\\n    - Omer Levy\\n    - Christopher D. Manning\\n    year: 2019\\n    venue: ACL Workshop BlackboxNLP 2019\\n    url: ''\\n    doi: '1906.04341'\\n    bibtex_key: clark2019bert\\n    category: Attention Head Analysis\\n    role: background\\n    relevance: Characterizes attention head behavior patterns (delimiter tokens, positional offsets, broad attention). Shows heads in same layer often exhibit similar behaviors—relevant to understanding GQA group structure.\\n    abstract: Proposes methods for analyzing attention mechanisms of pre-trained models. Finds BERT heads exhibit patterns like attending to delimiter tokens, positional offsets, or broadly over sentences. Certain heads correspond to syntactic and coreference relations with high accuracy.\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: literature-survey\\n    added_at: '2026-05-14T10:30:00.000Z'\\n  ainslie2023gqa:\\n    title: 'GQA: Training Generalized Multi-Query Transformer Models from Multi-Head Checkpoints'\\n    authors:\\n    - Joshua Ainslie\\n    - James Lee-Thorp\\n    - Michiel de Jong\\n    - Yury Zemlyanskiy\\n    - Federico Lebron\\n    - Sumit Sanghai\\n    year: 2023\\n    venue: EMNLP 2023\\n    url: ''\\n    doi: '2305.13245'\\n    bibtex_key: ainslie2023gqa\\n    category: Attention Head Analysis\\n    role: foundation\\n    relevance: Defines grouped-query attention (GQA) which is the architecture used by all three models we evaluate (Qwen2.5 7:1, Llama-3.1 4:1, Mistral 4:1). GQA group ratio directly affects our per-head allocation granularity and results.\\n    abstract: Proposes grouped-query attention (GQA), a generalization of multi-query attention using an intermediate number of key-value heads. Uptrained GQA achieves quality close to multi-head attention with comparable speed to MQA. Provides recipe for uptraining existing MHA checkpoints.\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: literature-survey\\n    added_at: '2026-05-14T10:30:00.000Z'\\n\\n  # ============================================================\\n  # Cluster 6: LLM Inference Efficiency (4 papers)\\n  # ============================================================\\n  kwon2023vllm:\\n    title: Efficient Memory Management for Large Language Model Serving with PagedAttention\\n    authors:\\n    - Woosuk Kwon\\n    - Zhuohan Li\\n    - Siyuan Zhuang\\n    - Ying Sheng\\n    - Lianmin Zheng\\n    - Cody Hao Yu\\n    - Joseph E. Gonzalez\\n    - Hao Zhang\\n    - Ion Stoica\\n    year: 2023\\n    venue: SOSP 2023\\n    url: ''\\n    doi: '2309.06180'\\n    bibtex_key: kwon2023vllm\\n    category: LLM Inference Efficiency\\n    role: background\\n    relevance: PagedAttention enables non-contiguous KV cache storage, reducing memory waste. Our per-head mixed-precision allocation is complementary—can be applied within vLLM's paged memory management.\\n    abstract: vLLM proposes PagedAttention inspired by virtual memory paging, achieving near-zero waste in KV cache memory and flexible sharing within and across requests. 2-4x throughput improvement over state-of-the-art systems.\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: literature-survey\\n    added_at: '2026-05-14T10:30:00.000Z'\\n  dao2022flashattention:\\n    title: 'FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness'\\n    authors:\\n    - Tri Dao\\n    - Daniel Y. Fu\\n    - Stefano Ermon\\n    - Atri Rudra\\n    - Christopher Re\\n    year: 2022\\n    venue: NeurIPS 2022\\n    url: ''\\n    doi: '2205.14135'\\n    bibtex_key: dao2022flashattention\\n    category: LLM Inference Efficiency\\n    role: background\\n    relevance: IO-aware tiling for exact attention. Our quantized KV cache reduces HBM reads during attention, providing complementary gains to FlashAttention's tiling strategy.\\n    abstract: FlashAttention uses tiling to reduce memory reads/writes between GPU HBM and SRAM. 15% speedup on BERT-large, 3x on GPT-2, 2.4x on long-range arena, without approximation.\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: literature-survey\\n    added_at: '2026-05-14T10:30:00.000Z'\\n  shazeer2019mqa:\\n    title: 'Fast Transformer Decoding: One Write-Head is All You Need'\\n    authors:\\n    - Noam Shazeer\\n    year: 2019\\n    venue: arXiv 2019\\n    url: ''\\n    doi: '1911.02150'\\n    bibtex_key: shazeer2019mqa\\n    category: LLM Inference Efficiency\\n    role: foundation\\n    relevance: Introduces multi-query attention (MQA) sharing a single KV head across all query heads. GQA generalizes MQA. Our per-head allocation exploits the remaining KV head heterogeneity in GQA models.\\n    abstract: Proposes multi-query attention where keys and values are shared across all attention heads, greatly reducing KV cache size and memory bandwidth requirements of incremental decoding. Much faster decoding with minor quality degradation.\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: literature-survey\\n    added_at: '2026-05-14T10:30:00.000Z'\\n  deepseek2024v2:\\n    title: 'DeepSeek-V2: A Strong, Economical, and Efficient Mixture-of-Experts Language Model'\\n    authors:\\n    - DeepSeek-AI\\n    year: 2024\\n    venue: arXiv 2024\\n    url: ''\\n    doi: '2405.04434'\\n    bibtex_key: deepseek2024v2\\n    category: LLM Inference Efficiency\\n    role: background\\n    relevance: Introduces Multi-head Latent Attention (MLA) compressing KV cache into low-rank latent vectors (93.3% reduction). Alternative architectural approach to KV cache reduction vs our post-training quantization.\\n    abstract: DeepSeek-V2 uses Multi-head Latent Attention (MLA) compressing KV caches into latent vectors and DeepSeekMoE for sparse computation. 236B total parameters, 21B activated per token. 42.5% training cost reduction, 93.3% KV cache reduction, 5.76x throughput increase vs DeepSeek 67B.\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: literature-survey\\n    added_at: '2026-05-14T10:30:00.000Z'\\n\\n  # ============================================================\\n  # Cluster 7: Evaluation Models (3 papers)\\n  # ============================================================\\n  grattafiori2024llama3:\\n    title: The Llama 3 Herd of Models\\n    authors:\\n    - Aaron Grattafiori\\n    - et al.\\n    year: 2024\\n    venue: arXiv 2024\\n    url: ''\\n    doi: '2407.21783'\\n    bibtex_key: grattafiori2024llama3\\n    category: Evaluation Models\\n    role: evaluation\\n    relevance: Llama-3.1-8B is one of three evaluation models. GQA with 4:1 ratio (8 KV heads, 32 query heads). Marginal gains from per-head allocation in our experiments.\\n    abstract: Llama 3 is a herd of foundation models natively supporting multilinguality, coding, reasoning, and tool usage. Dense Transformer up to 405B parameters with 128K context. Comparable quality to GPT-4.\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: literature-survey\\n    added_at: '2026-05-14T10:30:00.000Z'\\n  yang2025qwen25:\\n    title: Qwen2.5 Technical Report\\n    authors:\\n    - An Yang\\n    - et al.\\n    year: 2025\\n    venue: arXiv 2024\\n    url: ''\\n    doi: '2412.15115'\\n    bibtex_key: yang2025qwen25\\n    category: Evaluation Models\\n    role: evaluation\\n    relevance: Qwen2.5-7B is our strongest-result model. GQA with 7:1 ratio (4 KV heads, 28 query heads)—highest heterogeneity among tested models, yielding 29.3% PPL improvement from per-head allocation.\\n    abstract: Qwen2.5 is a comprehensive LLM series with improvements in pre-training (18T tokens) and post-training. Qwen2.5-72B-Instruct outperforms many open and proprietary models, competitive with Llama-3-405B-Instruct at 5x smaller size.\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: literature-survey\\n    added_at: '2026-05-14T10:30:00.000Z'\\n  jiang2023mistral:\\n    title: Mistral 7B\\n    authors:\\n    - Albert Q. Jiang\\n    - Alexandre Sablayrolles\\n    - Arthur Mensch\\n    - Chris Bamford\\n    - Devendra Singh Chaplot\\n    - Diego de las Casas\\n    - Florian Bressand\\n    - Gianna Lengyel\\n    - Guillaume Lample\\n    - Lucile Saulnier\\n    - Lelio Renard Lavaud\\n    - Marie-Anne Lachaux\\n    - Pierre Stock\\n    - Teven Le Scao\\n    - Thibaut Lavril\\n    - Thomas Wang\\n    - Timothee Lacroix\\n    - William El Sayed\\n    year: 2023\\n    venue: arXiv 2023\\n    url: ''\\n    doi: '2310.06825'\\n    bibtex_key: jiang2023mistral\\n    category: Evaluation Models\\n    role: evaluation\\n    relevance: Mistral-7B-v0.3 is our third evaluation model. GQA with 4:1 ratio (8 KV heads, 32 query heads). Negative result from per-head allocation—demonstrates architecture-dependent effectiveness.\\n    abstract: Mistral 7B leverages grouped-query attention (GQA) for faster inference and sliding window attention (SWA) for handling arbitrary-length sequences with reduced cost. Outperforms Llama 2 13B on all benchmarks.\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: literature-survey\\n    added_at: '2026-05-14T10:30:00.000Z'\\n\\n  # ============================================================\\n  # Cluster 8: Theory (1 paper)\\n  # ============================================================\\n  kellerer2004knapsack:\\n    title: Knapsack Problems\\n    authors:\\n    - Hans Kellerer\\n    - Ulrich Pferschy\\n    - David Pisinger\\n    year: 2004\\n    venue: Springer\\n    url: ''\\n    doi: 10.1007/978-3-540-24777-7\\n    bibtex_key: kellerer2004knapsack\\n    category: Theory\\n    role: foundation\\n    relevance: Definitive reference for multiple-choice knapsack problem (MCKP, Chapter 11). Our per-head bit allocation with hardware-aligned {2,4,8,16} is formulated as MCKP. Greedy optimality conditions and dominance relations from this text underpin our theoretical analysis.\\n    abstract: Comprehensive monograph on knapsack problems covering 0-1, bounded, unbounded, subset-sum, change-making, multiple-choice, and multi-dimensional variants. Chapter 11 covers MCKP including dominance, branch-and-bound, dynamic programming, and approximation algorithms.\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: literature-survey\\n    added_at: '2026-05-14T10:30:00.000Z'\\n\", \"total_chars\": 36288, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "540b7bd7-a7b9-49bb-b9c2-76f662a7a87b",
  "isSidechain": false,
  "promptId": "964448b9-9407-4006-b5f8-3afa58950999",
  "type": "user",
  "uuid": "7228d464-278b-474c-9c4d-c3ff03df26df",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/literature_map.yaml\\\", \\\"content\\\": \\\"meta:\\\\n  last_updated: '2026-05-14T10:30:00.000Z'\\\\n  total_papers: 35\\\\ncategories:\\\\n  - Mixed-Precision Rate-Distortion\\\\n  - KV Cache Quantization\\\\n  - KV Cache Eviction\\\\n  - Model Compression\\\\n  - Attention Head Analysis\\\\n  - LLM Inference Efficiency\\\\n  - Evaluation Models\\\\n  - Theory\\\\npapers:\\\\n  # ============================================================\\\\n  # Cluster 1: Mixed-Precision R-D Allocation (5 papers)\\\\n  # ============================================================\\\\n  zuo2026ratequant:\\\\n    title: 'RateQuant: Optimal Mixed-Precision KV Cache Quantization via Rate-Distortion Theory'\\\\n    authors:\\\\n    - Fei Zuo\\\\n    - Zikang Zhou\\\\n    - Hao Cong\\\\n    - Xiaoyan Xi\\\\n    - Ho Fai Leung\\\\n    year: 2026\\\\n    venue: arXiv 2026\\\\n    url: ''\\\\n    doi: '2605.06675'\\\\n    bibtex_key: zuo2026ratequant\\\\n    category: Mixed-Precision Rate-Distortion\\\\n    role: direct-competitor\\\\n    relevance: 'Primary competitor: R-D optimal per-head KV cache bit allocation. Algorithm 1 (discrete greedy). Theorem 2 (continuous closed-form via reverse waterfilling). Proposition 6 (greedy optimality on consecutive integers). Key limitation: does not address hardware-aligned non-consecutive {2,4,8,16} where greedy may fail.'\\\\n    abstract: RateQuant fits a per-quantizer distortion model D(b)=alpha*beta^{-b} from a small calibration set, then solves the bit-allocation in closed form via reverse waterfilling from rate-distortion theory. On Qwen3-8B at 2.5 avg bits, calibrated RateQuant reduces KIVI perplexity from 49.3 to 14.9 (70% reduction). Calibration takes 1.6s on a single GPU with zero inference overhead.\\\\n    semantic_scholar_id: ''\\\\n    verified: true\\\\n    added_by: paper-research\\\\n    added_at: '2026-05-14T08:42:26.710Z'\\\\n  lei2026arkv:\\\\n    title: 'ARKV: Adaptive and Resource-Efficient KV Cache Management under Limited Memory Budget for Long-Context Inference in LLMs'\\\\n    authors:\\\\n    - Jianlong Lei\\\\n    - Shashikant Ilager\\\\n    year: 2026\\\\n    venue: arXiv 2026\\\\n    url: ''\\\\n    doi: '2603.08727'\\\\n    bibtex_key: lei2026arkv\\\\n    category: Mixed-Precision Rate-Distortion\\\\n    role: direct-competitor\\\\n    relevance: Adaptive mixed-precision KV cache with tri-state token assignment (Original/Quantization/Eviction). Per-layer OQ ratio estimation via attention entropy, variance, kurtosis. Alternative adaptive allocation strategy to our R-D formulation.\\\\n    abstract: 'ARKV dynamically allocates precision levels to cached tokens based on per-layer attention dynamics and token-level importance. Three components: per-layer OQ ratio estimation, token importance scoring, and tri-state cache assignment. Preserves ~97% baseline accuracy with 4x KV memory reduction.'\\\\n    semantic_scholar_id: ''\\\\n    verified: true\\\\n    added_by: paper-research\\\\n    added_at: '2026-05-14T08:42:26.710Z'\\\\n  li2025kvmix:\\\\n    title: 'KVmix: Gradient-Based Layer Importance-Aware Mixed-Precision Quantization for KV Cache'\\\\n    authors:\\\\n    - Fei Li\\\\n    - Song Liu\\\\n    - Weiguo Wu\\\\n    - Shiqiang Nie\\\\n    - Jinyu Wang\\\\n    year: 2025\\\\n    venue: arXiv 2025\\\\n    url: ''\\\\n    doi: '2506.08018'\\\\n    bibtex_key: li2025kvmix\\\\n    category: Mixed-Precision Rate-Distortion\\\\n    role: method-component\\\\n    relevance: Gradient-based importance for layer-wise KV cache bit-width allocation. Heuristic sensitivity-based approach vs our R-D optimal formulation. Achieves near-lossless at Key 2.19bit / Value 2.38bit.\\\\n    abstract: KVmix employs gradient-based importance analysis to evaluate how individual Key and Value projection matrices affect model loss, enabling layer-specific bit-width allocation. Includes dynamic long-context optimization preserving full-precision KV pairs for recent pivotal tokens.\\\\n    semantic_scholar_id: ''\\\\n    verified: true\\\\n    added_by: paper-research\\\\n    added_at: '2026-05-14T08:42:26.710Z'\\\\n  zhang2025mixkvq:\\\\n    title: 'MixKVQ: Query-Aware Mixed-Precision KV Cache Quantization for Long-Context Reasoning'\\\\n    authors:\\\\n    - Tao Zhang\\\\n    - Ziqian Zeng\\\\n    - Hao Peng\\\\n    - Huiping Zhuang\\\\n    - Cen Chen\\\\n    year: 2025\\\\n    venue: arXiv 2025\\\\n    url: ''\\\\n    doi: '2512.19206'\\\\n    bibtex_key: zhang2025mixkvq\\\\n    category: Mixed-Precision Rate-Distortion\\\\n    role: method-component\\\\n    relevance: 'Query-aware channel-level mixed-precision for KV cache. Orthogonal to our per-head R-D allocation: operates at channel granularity rather than head granularity.'\\\\n    abstract: MixKVQ introduces a lightweight query-aware algorithm to identify and preserve critical key channels at higher precision while applying per-token quantization for value cache. Outperforms existing low-bit methods on complex reasoning datasets.\\\\n    semantic_scholar_id: ''\\\\n    verified: true\\\\n    added_by: paper-research\\\\n    added_at: '2026-05-14T08:42:26.710Z'\\\\n  kim2024squeezellm:\\\\n    title: 'SqueezeLLM: Dense-and-Sparse Quantization'\\\\n    authors:\\\\n    - Sehoon Kim\\\\n    - Coleman Hooper\\\\n    - Amir Gholami\\\\n    - Zhen Dong\\\\n    - Xiuyu Li\\\\n    - Sheng Shen\\\\n    - Michael W. Mahoney\\\\n    - Kurt Keutzer\\\\n    year: 2024\\\\n    venue: ICML 2024\\\\n    url: ''\\\\n    doi: '2306.07629'\\\\n    bibtex_key: kim2024squeezellm\\\\n    category: Mixed-Precision Rate-Distortion\\\\n    role: foundation\\\\n    relevance: Foundational sensitivity-based non-uniform quantization using second-order information. Pioneered per-group precision assignment based on sensitivity—principle we extend to per-head KV cache R-D allocation.\\\\n    abstract: 'SqueezeLLM enables lossless compression to ultra-low 3-bit precision via two ideas: sensitivity-based non-uniform quantization searching for optimal bit precision assignment, and Dense-and-Sparse decomposition storing outliers in efficient sparse format.'\\\\n    semantic_scholar_id: ''\\\\n    verified: true\\\\n    added_by: paper-research\\\\n    added_at: '2026-05-14T08:42:26.710Z'\\\\n\\\\n  # ============================================================\\\\n  # Cluster 2: KV Cache Quantization (6 papers)\\\\n  # ============================================================\\\\n  liu2024kivi:\\\\n    title: 'KIVI: A Tuning-Free Asymmetric 2bit Quantization for KV Cache'\\\\n    authors:\\\\n    - Zirui Liu\\\\n    - Jiayi Yuan\\\\n    - Hongye Jin\\\\n    - Shaochen Zhong\\\\n    - Zhaozhuo Xu\\\\n    - Vladimir Braverman\\\\n    - Beidi Chen\\\\n    - Xia Hu\\\\n    year: 2024\\\\n    venue: ICML 2024\\\\n    url: ''\\\\n    doi: '2402.02750'\\\\n    bibtex_key: liu2024kivi\\\\n    category: KV Cache Quantization\\\\n    role: direct-competitor\\\\n    relevance: Asymmetric per-channel key / per-token value 2-bit KV cache quantization; tuning-free baseline for mixed-precision KV cache methods\\\\n    abstract: We conduct a comprehensive study on the element distribution in KV cache of popular LLMs and find that the key cache should be quantized per-channel while the value cache should be quantized per-token. From this observation, we develop a tuning-free 2bit KV cache quantization algorithm named KIVI.\\\\n    semantic_scholar_id: ''\\\\n    verified: true\\\\n    added_by: paper-research\\\\n    added_at: '2026-05-14T07:56:45.265Z'\\\\n  hooper2024kvquant:\\\\n    title: 'KVQuant: Towards 10 Million Context Length LLM Inference with KV Cache Quantization'\\\\n    authors:\\\\n    - Coleman Hooper\\\\n    - Sehoon Kim\\\\n    - Hiva Mohammadzadeh\\\\n    - Michael W. Mahoney\\\\n    - Yakun Sophia Shao\\\\n    - Kurt Keutzer\\\\n    - Amir Gholami\\\\n    year: 2024\\\\n    venue: NeurIPS 2024\\\\n    url: ''\\\\n    doi: '2401.18079'\\\\n    bibtex_key: hooper2024kvquant\\\\n    category: KV Cache Quantization\\\\n    role: direct-competitor\\\\n    relevance: Per-channel key quantization with pre-RoPE, non-uniform datatypes, and dense-and-sparse outlier handling; achieves sub-4-bit KV cache for 10M context\\\\n    abstract: KV cache activations are the dominant contributor to memory consumption during LLM inference for large context windows. We address this with per-channel key quantization, pre-RoPE key quantization, non-uniform KV cache quantization, and per-vector dense-and-sparse quantization to isolate outliers.\\\\n    semantic_scholar_id: ''\\\\n    verified: true\\\\n    added_by: paper-research\\\\n    added_at: '2026-05-14T07:56:45.265Z'\\\\n  lin2024qserve:\\\\n    title: 'QServe: W4A8KV4 Quantization and System Co-design for Efficient LLM Serving'\\\\n    authors:\\\\n    - Yujun Lin\\\\n    - Haotian Tang\\\\n    - Shang Yang\\\\n    - Zhekai Zhang\\\\n    - Guangxuan Xiao\\\\n    - Chuang Gan\\\\n    - Song Han\\\\n    year: 2024\\\\n    venue: MLSys 2025\\\\n    url: ''\\\\n    doi: '2405.04532'\\\\n    bibtex_key: lin2024qserve\\\\n    category: KV Cache Quantization\\\\n    role: foundation\\\\n    relevance: W4A8KV4 co-design with SmoothAttention for KV4 quantization; demonstrates system-level gains from joint weight-activation-KV quantization\\\\n    abstract: QServe introduces QoQ (W4A8KV4), a quantization algorithm with 4-bit weight, 8-bit activation, and 4-bit KV cache. Progressive group quantization ensures all GEMMs run on INT8 tensor cores. SmoothAttention shifts quantization difficulty from keys to queries.\\\\n    semantic_scholar_id: ''\\\\n    verified: true\\\\n    added_by: paper-research\\\\n    added_at: '2026-05-14T07:56:45.265Z'\\\\n  he2024zipcache:\\\\n    title: 'ZipCache: Accurate and Efficient KV Cache Quantization with Salient Token Identification'\\\\n    authors:\\\\n    - Yefei He\\\\n    - Luoming Zhang\\\\n    - Weijia Wu\\\\n    - Jing Liu\\\\n    - Hong Zhou\\\\n    - Bohan Zhuang\\\\n    year: 2024\\\\n    venue: NeurIPS 2024\\\\n    url: ''\\\\n    doi: '2405.14256'\\\\n    bibtex_key: he2024zipcache\\\\n    category: KV Cache Quantization\\\\n    role: direct-competitor\\\\n    relevance: Channel-separable tokenwise quantization with adaptive bit-width based on normalized attention score saliency; mixed-precision KV cache baseline\\\\n    abstract: ZipCache proposes channel-separable tokenwise quantization and uses normalized attention score for identifying salient tokens with adaptive bit-width assignment. Achieves 4.98x compression on Mistral-7B with 0.38% accuracy drop.\\\\n    semantic_scholar_id: ''\\\\n    verified: true\\\\n    added_by: paper-research\\\\n    added_at: '2026-05-14T07:56:45.265Z'\\\\n  kang2024gear:\\\\n    title: 'GEAR: An Efficient KV Cache Compression Recipe for Near-Lossless Generative Inference of LLM'\\\\n    authors:\\\\n    - Hao Kang\\\\n    - Qingru Zhang\\\\n    - Souvik Kundu\\\\n    - Geonhwa Jeong\\\\n    - Zaoxing Liu\\\\n    - Tushar Krishna\\\\n    - Tuo Zhao\\\\n    year: 2024\\\\n    venue: arXiv 2024\\\\n    url: ''\\\\n    doi: '2403.05527'\\\\n    bibtex_key: kang2024gear\\\\n    category: KV Cache Quantization\\\\n    role: direct-competitor\\\\n    relevance: Hybrid quantization + low-rank + sparse error correction for KV cache; demonstrates that residual compensation improves ultra-low-bit quantization quality\\\\n    abstract: GEAR first applies quantization to majority of entries to ultra-low precision, then employs a low rank matrix to approximate the quantization error, and a sparse matrix to remedy individual errors from outlier entries. Achieves near-lossless 4-bit compression with 2.38x throughput improvement.\\\\n    semantic_scholar_id: ''\\\\n    verified: true\\\\n    added_by: paper-research\\\\n    added_at: '2026-05-14T07:56:45.265Z'\\\\n  duanmu2024skvq:\\\\n    title: 'SKVQ: Sliding-window Key and Value Cache Quantization for Large Language Models'\\\\n    authors:\\\\n    - Haojie Duanmu\\\\n    - Zhihang Yuan\\\\n    - Xiuhong Li\\\\n    - Jiangfei Duan\\\\n    - Xingcheng Zhang\\\\n    - Dahua Lin\\\\n    year: 2024\\\\n    venue: arXiv 2024\\\\n    url: ''\\\\n    doi: '2405.06219'\\\\n    bibtex_key: duanmu2024skvq\\\\n    category: KV Cache Quantization\\\\n    role: direct-competitor\\\\n    relevance: Channel rearrangement + sliding-window high-precision recent tokens; achieves 2-bit key / 1.5-bit value with minimal accuracy loss\\\\n    abstract: SKVQ rearranges KV cache channels to improve similarity within quantization groups and applies clipped dynamic quantization at group level. Preserves recent window tokens at high precision. Enables 2-bit keys and 1.5-bit values with up to 1M context on 80GB GPU.\\\\n    semantic_scholar_id: ''\\\\n    verified: true\\\\n    added_by: paper-research\\\\n    added_at: '2026-05-14T07:56:45.265Z'\\\\n\\\\n  # ============================================================\\\\n  # Cluster 3: KV Cache Eviction (6 papers)\\\\n  # ============================================================\\\\n  zhang2023h2o:\\\\n    title: 'H2O: Heavy-Hitter Oracle for Efficient Generative Inference of Large Language Models'\\\\n    authors:\\\\n    - Zhenyu Zhang\\\\n    - Ying Sheng\\\\n    - Tianyi Zhou\\\\n    - Tianlong Chen\\\\n    - Lianmin Zheng\\\\n    - Ruisi Cai\\\\n    - Zhao Song\\\\n    - Yuandong Tian\\\\n    - Christopher Re\\\\n    - Clark Barrett\\\\n    - Zhangyang Wang\\\\n    - Beidi Chen\\\\n    year: 2023\\\\n    venue: NeurIPS 2023\\\\n    url: ''\\\\n    doi: 10.48550/arXiv.2306.14048\\\\n    bibtex_key: zhang2023h2o\\\\n    category: KV Cache Eviction\\\\n    role: background\\\\n    relevance: Foundational KV cache eviction policy based on heavy-hitter tokens; orthogonal to our quantization approach\\\\n    abstract: H2O identifies Heavy Hitters — a small set of tokens contributing most to attention scores — and dynamically retains recent and H2 tokens. With 20% heavy hitters, H2O improves throughput by up to 29x and reduces KV cache memory by up to 5x.\\\\n    semantic_scholar_id: ''\\\\n    verified: true\\\\n    added_by: paper-research\\\\n    added_at: '2026-05-14T08:10:15.562Z'\\\\n  li2024snapkv:\\\\n    title: 'SnapKV: LLM Knows What You are Looking for Before Generation'\\\\n    authors:\\\\n    - Yuhong Li\\\\n    - Yingbing Huang\\\\n    - Bowen Yang\\\\n    - Bharat Venkitesh\\\\n    - Acyr Locatelli\\\\n    - Hanchen Ye\\\\n    - Tianle Cai\\\\n    - Patrick Lewis\\\\n    - Deming Chen\\\\n    year: 2024\\\\n    venue: NeurIPS 2024\\\\n    url: ''\\\\n    doi: 10.48550/arXiv.2404.14469\\\\n    bibtex_key: li2024snapkv\\\\n    category: KV Cache Eviction\\\\n    role: background\\\\n    relevance: Observation-driven KV cache compression using attention pattern consistency; competes with eviction-based approaches our work compares against\\\\n    abstract: SnapKV efficiently minimizes KV cache size by selecting clustered important KV positions per attention head using an observation window at the end of the prompt. Achieves 3.6x speed increase and 8.2x memory efficiency at 16K tokens.\\\\n    semantic_scholar_id: ''\\\\n    verified: true\\\\n    added_by: paper-research\\\\n    added_at: '2026-05-14T08:10:15.562Z'\\\\n  ge2024fastgen:\\\\n    title: 'Model Tells You What to Discard: Adaptive KV Cache Compression for LLMs'\\\\n    authors:\\\\n    - Suyu Ge\\\\n    - Yunan Zhang\\\\n    - Liyuan Liu\\\\n    - Minjia Zhang\\\\n    - Jiawei Han\\\\n    - Jianfeng Gao\\\\n    year: 2024\\\\n    venue: ICLR 2024\\\\n    url: ''\\\\n    doi: 10.48550/arXiv.2310.01801\\\\n    bibtex_key: ge2024fastgen\\\\n    category: KV Cache Eviction\\\\n    role: background\\\\n    relevance: Adaptive per-head eviction strategy (FastGen); demonstrates head-specific compression is beneficial, complementary to quantization\\\\n    abstract: 'FastGen constructs KV cache adaptively per attention head: evicting long-range contexts on local-attention heads, discarding non-special tokens on special-token-focused heads, and using standard KV cache for broad-attention heads. Reduces memory by 50% without sacrificing quality.'\\\\n    semantic_scholar_id: ''\\\\n    verified: true\\\\n    added_by: paper-research\\\\n    added_at: '2026-05-14T08:10:15.562Z'\\\\n  xiao2024streamingllm:\\\\n    title: Efficient Streaming Language Models with Attention Sinks\\\\n    authors:\\\\n    - Guangxuan Xiao\\\\n    - Yuandong Tian\\\\n    - Beidi Chen\\\\n    - Song Han\\\\n    - Mike Lewis\\\\n    year: 2024\\\\n    venue: ICLR 2024\\\\n    url: ''\\\\n    doi: 10.48550/arXiv.2309.17453\\\\n    bibtex_key: xiao2024streamingllm\\\\n    category: KV Cache Eviction\\\\n    role: background\\\\n    relevance: Discovers attention sink phenomenon in initial tokens; motivates why naive eviction can fail and informs our quantization-first approach\\\\n    abstract: StreamingLLM enables LLMs to generalize to infinite sequence lengths without fine-tuning by retaining attention sink tokens alongside a sliding window of recent tokens. Achieves up to 22.2x speedup over sliding window recomputation.\\\\n    semantic_scholar_id: ''\\\\n    verified: true\\\\n    added_by: paper-research\\\\n    added_at: '2026-05-14T08:10:15.562Z'\\\\n  liu2024scissorhands:\\\\n    title: 'Scissorhands: Exploiting the Persistence of Importance Hypothesis for LLM KV Cache Compression at Test Time'\\\\n    authors:\\\\n    - Zichang Liu\\\\n    - Aditya Desai\\\\n    - Fangshuo Liao\\\\n    - Weitao Wang\\\\n    - Victor Xie\\\\n    - Zhaozhuo Xu\\\\n    - Anastasios Kyrillidis\\\\n    - Anshumali Shrivastava\\\\n    year: 2024\\\\n    venue: NeurIPS 2023\\\\n    url: ''\\\\n    doi: 10.48550/arXiv.2305.17118\\\\n    bibtex_key: liu2024scissorhands\\\\n    category: KV Cache Eviction\\\\n    role: background\\\\n    relevance: Persistence-of-importance hypothesis for KV cache eviction; achieves 5x cache reduction, combinable with 4-bit quantization for 20x compression\\\\n    abstract: Scissorhands maintains KV cache at a fixed budget by storing pivotal tokens with higher probability, achieving up to 5x memory reduction without quality loss, and up to 20x when combined with 4-bit quantization.\\\\n    semantic_scholar_id: ''\\\\n    verified: true\\\\n    added_by: paper-research\\\\n    added_at: '2026-05-14T08:10:15.562Z'\\\\n  yang2024pyramidinfer:\\\\n    title: 'PyramidInfer: Pyramid KV Cache Compression for High-throughput LLM Inference'\\\\n    authors:\\\\n    - Dongjie Yang\\\\n    - Xiaodong Han\\\\n    - Yan Gao\\\\n    - Yao Hu\\\\n    - Shilin Zhang\\\\n    - Hai Zhao\\\\n    year: 2024\\\\n    venue: Findings of ACL 2024\\\\n    url: ''\\\\n    doi: 10.48550/arXiv.2405.12532\\\\n    bibtex_key: yang2024pyramidinfer\\\\n    category: KV Cache Eviction\\\\n    role: background\\\\n    relevance: Layer-wise pyramid compression exploiting inter-layer dependency; crucial KV count decreases across layers, relevant to our per-layer rate allocation\\\\n    abstract: PyramidInfer compresses KV cache by layer-wise retaining crucial context, exploiting the finding that crucial keys and values decrease layer by layer. Achieves 2.2x throughput improvement with 54% GPU memory reduction.\\\\n    semantic_scholar_id: ''\\\\n    verified: true\\\\n    added_by: paper-research\\\\n    added_at: '2026-05-14T08:10:15.562Z'\\\\n\\\\n  # ============================================================\\\\n  # Cluster 4: Model Compression (6 papers)\\\\n  # ============================================================\\\\n  frantar2023gptq:\\\\n    title: 'GPTQ: Accurate Post-Training Quantization for Generative Pre-trained Transformers'\\\\n    authors:\\\\n    - Elias Frantar\\\\n    - Saleh Ashkboos\\\\n    - Torsten Hoefler\\\\n    - Dan Alistarh\\\\n    year: 2023\\\\n    venue: ICLR 2023\\\\n    url: ''\\\\n    doi: '2210.17323'\\\\n    bibtex_key: frantar2023gptq\\\\n    category: Model Compression\\\\n    role: foundation\\\\n    relevance: Foundational one-shot weight quantization based on approximate second-order information (OBQ). Reduces bitwidth to 3-4 bits per weight with negligible accuracy degradation. Established post-training quantization paradigm for LLMs.\\\\n    abstract: GPTQ is a one-shot weight quantization method based on approximate second-order information that can quantize GPT models with 175 billion parameters in approximately four GPU hours, reducing bitwidth to 3 or 4 bits per weight with negligible accuracy degradation.\\\\n    semantic_scholar_id: ''\\\\n    verified: true\\\\n    added_by: literature-survey\\\\n    added_at: '2026-05-14T10:30:00.000Z'\\\\n  lin2024awq:\\\\n    title: 'AWQ: Activation-aware Weight Quantization for LLM Compression and Acceleration'\\\\n    authors:\\\\n    - Ji Lin\\\\n    - Jiaming Tang\\\\n    - Haotian Tang\\\\n    - Shang Yang\\\\n    - Wei-Ming Chen\\\\n    - Wei-Chen Wang\\\\n    - Guangxuan Xiao\\\\n    - Xingyu Dang\\\\n    - Chuang Gan\\\\n    - Song Han\\\\n    year: 2024\\\\n    venue: MLSys 2024 (Best Paper)\\\\n    url: ''\\\\n    doi: '2306.00978'\\\\n    bibtex_key: lin2024awq\\\\n    category: Model Compression\\\\n    role: foundation\\\\n    relevance: Activation-aware salient weight protection via equivalent scaling transformation. Demonstrates that 1% salient weights dominate quantization quality—analogous to our finding that per-head sensitivity varies drastically.\\\\n    abstract: AWQ finds that protecting only 1% salient weights (identified by activation distribution, not weights) greatly reduces quantization error. Scales salient channels via mathematically equivalent transformation. No backpropagation or reconstruction needed. 3x speedup over FP16.\\\\n    semantic_scholar_id: ''\\\\n    verified: true\\\\n    added_by: literature-survey\\\\n    added_at: '2026-05-14T10:30:00.000Z'\\\\n  xiao2023smoothquant:\\\\n    title: 'SmoothQuant: Accurate and Efficient Post-Training Quantization for Large Language Models'\\\\n    authors:\\\\n    - Guangxuan Xiao\\\\n    - Ji Lin\\\\n    - Mickael Seznec\\\\n    - Hao Wu\\\\n    - Julien Demouth\\\\n    - Song Han\\\\n    year: 2023\\\\n    venue: ICML 2023\\\\n    url: ''\\\\n    doi: '2211.10438'\\\\n    bibtex_key: xiao2023smoothquant\\\\n    category: Model Compression\\\\n    role: foundation\\\\n    relevance: Smooths activation outliers by migrating quantization difficulty from activations to weights. Enables W8A8 for all matmuls in LLMs. QServe's SmoothAttention extends this idea to KV cache.\\\\n    abstract: SmoothQuant enables INT8 quantization of both weights and activations for all matrix multiplications in LLMs by smoothing activation outliers via offline migration of quantization difficulty from activations to weights. Up to 1.56x speedup and 2x memory reduction with negligible accuracy loss.\\\\n    semantic_scholar_id: ''\\\\n    verified: true\\\\n    added_by: literature-survey\\\\n    added_at: '2026-05-14T10:30:00.000Z'\\\\n  dettmers2022llmint8:\\\\n    title: 'LLM.int8(): 8-bit Matrix Multiplication for Transformers at Scale'\\\\n    authors:\\\\n    - Tim Dettmers\\\\n    - Mike Lewis\\\\n    - Younes Belkada\\\\n    - Luke Zettlemoyer\\\\n    year: 2022\\\\n    venue: NeurIPS 2022\\\\n    url: ''\\\\n    doi: '2208.07339'\\\\n    bibtex_key: dettmers2022llmint8\\\\n    category: Model Compression\\\\n    role: foundation\\\\n    relevance: First to identify emergent outlier features in transformers that dominate quantization quality. Mixed-precision decomposition (0.1% in FP16, 99.9% in INT8) is conceptually related to our per-head mixed-precision allocation.\\\\n    abstract: LLM.int8() develops Int8 matrix multiplication for feed-forward and attention projection layers via absmax vector-wise quantization and mixed precision decomposition. Cuts inference memory by half while retaining full precision performance for 175B-parameter models.\\\\n    semantic_scholar_id: ''\\\\n    verified: true\\\\n    added_by: literature-survey\\\\n    added_at: '2026-05-14T10:30:00.000Z'\\\\n  tseng2024quipsharp:\\\\n    title: 'QuIP#: Even Better LLM Quantization with Hadamard Incoherence and Lattice Codebooks'\\\\n    authors:\\\\n    - Albert Tseng\\\\n    - Jerry Chee\\\\n    - Qingyao Sun\\\\n    - Volodymyr Kuleshov\\\\n    - Christopher De Sa\\\\n    year: 2024\\\\n    venue: ICML 2024\\\\n    url: ''\\\\n    doi: '2402.04396'\\\\n    bibtex_key: tseng2024quipsharp\\\\n    category: Model Compression\\\\n    role: foundation\\\\n    relevance: State-of-the-art extreme compression (2-bit weights) via Hadamard incoherence processing and E8 lattice codebooks. Theoretical grounding for why incoherent distributions quantize better—relevant to understanding per-head distortion variation.\\\\n    abstract: QuIP# achieves state-of-the-art in extreme weight compression using randomized Hadamard transform for incoherence processing, E8 lattice codebooks for vector quantization of sub-Gaussian incoherent weights, and fine-tuning for fidelity. Hardware-efficient implementation.\\\\n    semantic_scholar_id: ''\\\\n    verified: true\\\\n    added_by: literature-survey\\\\n    added_at: '2026-05-14T10:30:00.000Z'\\\\n  zhao2024atom:\\\\n    title: 'Atom: Low-bit Quantization for Efficient and Accurate LLM Serving'\\\\n    authors:\\\\n    - Yilong Zhao\\\\n    - Chien-Yu Lin\\\\n    - Kan Zhu\\\\n    - Zihao Ye\\\\n    - Lequn Chen\\\\n    - Size Zheng\\\\n    - Luis Ceze\\\\n    - Arvind Krishnamurthy\\\\n    - Tianqi Chen\\\\n    - Baris Kasikci\\\\n    year: 2024\\\\n    venue: MLSys 2024\\\\n    url: ''\\\\n    doi: '2310.19102'\\\\n    bibtex_key: zhao2024atom\\\\n    category: Model Compression\\\\n    role: foundation\\\\n    relevance: End-to-end low-bit quantization for serving with mixed-precision, group quantization, and KV cache quantization. Demonstrates system-level throughput gains (3.5x over FP16) from co-designed quantization kernels.\\\\n    abstract: Atom combines mixed-precision quantization retaining salient activations/weights in high precision, fine-grained group quantization, dynamic activation quantization, KV-cache quantization, and efficient CUDA kernels. Achieves 7.73x throughput over FP16 baseline.\\\\n    semantic_scholar_id: ''\\\\n    verified: true\\\\n    added_by: literature-survey\\\\n    added_at: '2026-05-14T10:30:00.000Z'\\\\n\\\\n  # ============================================================\\\\n  # Cluster 5: Attention Head Analysis (4 papers)\\\\n  # ============================================================\\\\n  voita2019heads:\\\\n    title: 'Analyzing Multi-Head Self-Attention: Specialized Heads Do the Heavy Lifting, the Rest Can Be Pruned'\\\\n    authors:\\\\n    - Elena Voita\\\\n    - David Talbot\\\\n    - Fedor Moiseev\\\\n    - Rico Sennrich\\\\n    - Ivan Titov\\\\n    year: 2019\\\\n    venue: ACL 2019\\\\n    url: ''\\\\n    doi: '1905.09418'\\\\n    bibtex_key: voita2019heads\\\\n    category: Attention Head Analysis\\\\n    role: foundation\\\\n    relevance: Foundational work on attention head specialization and pruning. Shows most heads can be pruned (38/48 with only 0.15 BLEU drop). Motivates our per-head heterogeneous quantization—heads have different importance and roles.\\\\n    abstract: Evaluates individual attention head contributions and identifies specialized heads playing consistent linguistically-interpretable roles. Using stochastic gates with L0 penalty, the vast majority of heads can be pruned without seriously affecting performance.\\\\n    semantic_scholar_id: ''\\\\n    verified: true\\\\n    added_by: literature-survey\\\\n    added_at: '2026-05-14T10:30:00.000Z'\\\\n  michel2019sixteen:\\\\n    title: Are Sixteen Heads Really Better than One?\\\\n    authors:\\\\n    - Paul Michel\\\\n    - Omer Levy\\\\n    - Graham Neubig\\\\n    year: 2019\\\\n    venue: NeurIPS 2019\\\\n    url: ''\\\\n    doi: '1905.10650'\\\\n    bibtex_key: michel2019sixteen\\\\n    category: Attention Head Analysis\\\\n    role: foundation\\\\n    relevance: Shows large proportion of attention heads can be removed at test time. Greedy pruning analysis reveals varying head importance. Directly supports our premise that heads deserve different quantization precision.\\\\n    abstract: A large proportion of attention heads can be removed at test time without significantly impacting performance, and some layers can be reduced to a single head. Self-attention layers can be significantly pruned while encoder-decoder layers are more dependent on multi-headedness.\\\\n    semantic_scholar_id: ''\\\\n    verified: true\\\\n    added_by: literature-survey\\\\n    added_at: '2026-05-14T10:30:00.000Z'\\\\n  clark2019bert:\\\\n    title: What Does BERT Look At? An Analysis of BERT's Attention\\\\n    authors:\\\\n    - Kevin Clark\\\\n    - Urvashi Khandelwal\\\\n    - Omer Levy\\\\n    - Christopher D. Manning\\\\n    year: 2019\\\\n    venue: ACL Workshop BlackboxNLP 2019\\\\n    url: ''\\\\n    doi: '1906.04341'\\\\n    bibtex_key: clark2019bert\\\\n    category: Attention Head Analysis\\\\n    role: background\\\\n    relevance: Characterizes attention head behavior patterns (delimiter tokens, positional offsets, broad attention). Shows heads in same layer often exhibit similar behaviors—relevant to understanding GQA group structure.\\\\n    abstract: Proposes methods for analyzing attention mechanisms of pre-trained models. Finds BERT heads exhibit patterns like attending to delimiter tokens, positional offsets, or broadly over sentences. Certain heads correspond to syntactic and coreference relations with high accuracy.\\\\n    semantic_scholar_id: ''\\\\n    verified: true\\\\n    added_by: literature-survey\\\\n    added_at: '2026-05-14T10:30:00.000Z'\\\\n  ainslie2023gqa:\\\\n    title: 'GQA: Training Generalized Multi-Query Transformer Models from Multi-Head Checkpoints'\\\\n    authors:\\\\n    - Joshua Ainslie\\\\n    - James Lee-Thorp\\\\n    - Michiel de Jong\\\\n    - Yury Zemlyanskiy\\\\n    - Federico Lebron\\\\n    - Sumit Sanghai\\\\n    year: 2023\\\\n    venue: EMNLP 2023\\\\n    url: ''\\\\n    doi: '2305.13245'\\\\n    bibtex_key: ainslie2023gqa\\\\n    category: Attention Head Analysis\\\\n    role: foundation\\\\n    relevance: Defines grouped-query attention (GQA) which is the architecture used by all three models we evaluate (Qwen2.5 7:1, Llama-3.1 4:1, Mistral 4:1). GQA group ratio directly affects our per-head allocation granularity and results.\\\\n    abstract: Proposes grouped-query attention (GQA), a generalization of multi-query attention using an intermediate number of key-value heads. Uptrained GQA achieves quality close to multi-head attention with comparable speed to MQA. Provides recipe for uptraining existing MHA checkpoints.\\\\n    semantic_scholar_id: ''\\\\n    verified: true\\\\n    added_by: literature-survey\\\\n    added_at: '2026-05-14T10:30:00.000Z'\\\\n\\\\n  # ============================================================\\\\n  # Cluster 6: LLM Inference Efficiency (4 papers)\\\\n  # ============================================================\\\\n  kwon2023vllm:\\\\n    title: Efficient Memory Management for Large Language Model Serving with PagedAttention\\\\n    authors:\\\\n    - Woosuk Kwon\\\\n    - Zhuohan Li\\\\n    - Siyuan Zhuang\\\\n    - Ying Sheng\\\\n    - Lianmin Zheng\\\\n    - Cody Hao Yu\\\\n    - Joseph E. Gonzalez\\\\n    - Hao Zhang\\\\n    - Ion Stoica\\\\n    year: 2023\\\\n    venue: SOSP 2023\\\\n    url: ''\\\\n    doi: '2309.06180'\\\\n    bibtex_key: kwon2023vllm\\\\n    category: LLM Inference Efficiency\\\\n    role: background\\\\n    relevance: PagedAttention enables non-contiguous KV cache storage, reducing memory waste. Our per-head mixed-precision allocation is complementary—can be applied within vLLM's paged memory management.\\\\n    abstract: vLLM proposes PagedAttention inspired by virtual memory paging, achieving near-zero waste in KV cache memory and flexible sharing within and across requests. 2-4x throughput improvement over state-of-the-art systems.\\\\n    semantic_scholar_id: ''\\\\n    verified: true\\\\n    added_by: literature-survey\\\\n    added_at: '2026-05-14T10:30:00.000Z'\\\\n  dao2022flashattention:\\\\n    title: 'FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness'\\\\n    authors:\\\\n    - Tri Dao\\\\n    - Daniel Y. Fu\\\\n    - Stefano Ermon\\\\n    - Atri Rudra\\\\n    - Christopher Re\\\\n    year: 2022\\\\n    venue: NeurIPS 2022\\\\n    url: ''\\\\n    doi: '2205.14135'\\\\n    bibtex_key: dao2022flashattention\\\\n    category: LLM Inference Efficiency\\\\n    role: background\\\\n    relevance: IO-aware tiling for exact attention. Our quantized KV cache reduces HBM reads during attention, providing complementary gains to FlashAttention's tiling strategy.\\\\n    abstract: FlashAttention uses tiling to reduce memory reads/writes between GPU HBM and SRAM. 15% speedup on BERT-large, 3x on GPT-2, 2.4x on long-range arena, without approximation.\\\\n    semantic_scholar_id: ''\\\\n    verified: true\\\\n    added_by: literature-survey\\\\n    added_at: '2026-05-14T10:30:00.000Z'\\\\n  shazeer2019mqa:\\\\n    title: 'Fast Transformer Decoding: One Write-Head is All You Need'\\\\n    authors:\\\\n    - Noam Shazeer\\\\n    year: 2019\\\\n    venue: arXiv 2019\\\\n    url: ''\\\\n    doi: '1911.02150'\\\\n    bibtex_key: shazeer2019mqa\\\\n    category: LLM Inference Efficiency\\\\n    role: foundation\\\\n    relevance: Introduces multi-query attention (MQA) sharing a single KV head across all query heads. GQA generalizes MQA. Our per-head allocation exploits the remaining KV head heterogeneity in GQA models.\\\\n    abstract: Proposes multi-query attention where keys and values are shared across all attention heads, greatly reducing KV cache size and memory bandwidth requirements of incremental decoding. Much faster decoding with minor quality degradation.\\\\n    semantic_scholar_id: ''\\\\n    verified: true\\\\n    added_by: literature-survey\\\\n    added_at: '2026-05-14T10:30:00.000Z'\\\\n  deepseek2024v2:\\\\n    title: 'DeepSeek-V2: A Strong, Economical, and Efficient Mixture-of-Experts Language Model'\\\\n    authors:\\\\n    - DeepSeek-AI\\\\n    year: 2024\\\\n    venue: arXiv 2024\\\\n    url: ''\\\\n    doi: '2405.04434'\\\\n    bibtex_key: deepseek2024v2\\\\n    category: LLM Inference Efficiency\\\\n    role: background\\\\n    relevance: Introduces Multi-head Latent Attention (MLA) compressing KV cache into low-rank latent vectors (93.3% reduction). Alternative architectural approach to KV cache reduction vs our post-training quantization.\\\\n    abstract: DeepSeek-V2 uses Multi-head Latent Attention (MLA) compressing KV caches into latent vectors and DeepSeekMoE for sparse computation. 236B total parameters, 21B activated per token. 42.5% training cost reduction, 93.3% KV cache reduction, 5.76x throughput increase vs DeepSeek 67B.\\\\n    semantic_scholar_id: ''\\\\n    verified: true\\\\n    added_by: literature-survey\\\\n    added_at: '2026-05-14T10:30:00.000Z'\\\\n\\\\n  # ============================================================\\\\n  # Cluster 7: Evaluation Models (3 papers)\\\\n  # ============================================================\\\\n  grattafiori2024llama3:\\\\n    title: The Llama 3 Herd of Models\\\\n    authors:\\\\n    - Aaron Grattafiori\\\\n    - et al.\\\\n    year: 2024\\\\n    venue: arXiv 2024\\\\n    url: ''\\\\n    doi: '2407.21783'\\\\n    bibtex_key: grattafiori2024llama3\\\\n    category: Evaluation Models\\\\n    role: evaluation\\\\n    relevance: Llama-3.1-8B is one of three evaluation models. GQA with 4:1 ratio (8 KV heads, 32 query heads). Marginal gains from per-head allocation in our experiments.\\\\n    abstract: Llama 3 is a herd of foundation models natively supporting multilinguality, coding, reasoning, and tool usage. Dense Transformer up to 405B parameters with 128K context. Comparable quality to GPT-4.\\\\n    semantic_scholar_id: ''\\\\n    verified: true\\\\n    added_by: literature-survey\\\\n    added_at: '2026-05-14T10:30:00.000Z'\\\\n  yang2025qwen25:\\\\n    title: Qwen2.5 Technical Report\\\\n    authors:\\\\n    - An Yang\\\\n    - et al.\\\\n    year: 2025\\\\n    venue: arXiv 2024\\\\n    url: ''\\\\n    doi: '2412.15115'\\\\n    bibtex_key: yang2025qwen25\\\\n    category: Evaluation Models\\\\n    role: evaluation\\\\n    relevance: Qwen2.5-7B is our strongest-result model. GQA with 7:1 ratio (4 KV heads, 28 query heads)—highest heterogeneity among tested models, yielding 29.3% PPL improvement from per-head allocation.\\\\n    abstract: Qwen2.5 is a comprehensive LLM series with improvements in pre-training (18T tokens) and post-training. Qwen2.5-72B-Instruct outperforms many open and proprietary models, competitive with Llama-3-405B-Instruct at 5x smaller size.\\\\n    semantic_scholar_id: ''\\\\n    verified: true\\\\n    added_by: literature-survey\\\\n    added_at: '2026-05-14T10:30:00.000Z'\\\\n  jiang2023mistral:\\\\n    title: Mistral 7B\\\\n    authors:\\\\n    - Albert Q. Jiang\\\\n    - Alexandre Sablayrolles\\\\n    - Arthur Mensch\\\\n    - Chris Bamford\\\\n    - Devendra Singh Chaplot\\\\n    - Diego de las Casas\\\\n    - Florian Bressand\\\\n    - Gianna Lengyel\\\\n    - Guillaume Lample\\\\n    - Lucile Saulnier\\\\n    - Lelio Renard Lavaud\\\\n    - Marie-Anne Lachaux\\\\n    - Pierre Stock\\\\n    - Teven Le Scao\\\\n    - Thibaut Lavril\\\\n    - Thomas Wang\\\\n    - Timothee Lacroix\\\\n    - William El Sayed\\\\n    year: 2023\\\\n    venue: arXiv 2023\\\\n    url: ''\\\\n    doi: '2310.06825'\\\\n    bibtex_key: jiang2023mistral\\\\n    category: Evaluation Models\\\\n    role: evaluation\\\\n    relevance: Mistral-7B-v0.3 is our third evaluation model. GQA with 4:1 ratio (8 KV heads, 32 query heads). Negative result from per-head allocation—demonstrates architecture-dependent effectiveness.\\\\n    abstract: Mistral 7B leverages grouped-query attention (GQA) for faster inference and sliding window attention (SWA) for handling arbitrary-length sequences with reduced cost. Outperforms Llama 2 13B on all benchmarks.\\\\n    semantic_scholar_id: ''\\\\n    verified: true\\\\n    added_by: literature-survey\\\\n    added_at: '2026-05-14T10:30:00.000Z'\\\\n\\\\n  # ============================================================\\\\n  # Cluster 8: Theory (1 paper)\\\\n  # ============================================================\\\\n  kellerer2004knapsack:\\\\n    title: Knapsack Problems\\\\n    authors:\\\\n    - Hans Kellerer\\\\n    - Ulrich Pferschy\\\\n    - David Pisinger\\\\n    year: 2004\\\\n    venue: Springer\\\\n    url: ''\\\\n    doi: 10.1007/978-3-540-24777-7\\\\n    bibtex_key: kellerer2004knapsack\\\\n    category: Theory\\\\n    role: foundation\\\\n    relevance: Definitive reference for multiple-choice knapsack problem (MCKP, Chapter 11). Our per-head bit allocation with hardware-aligned {2,4,8,16} is formulated as MCKP. Greedy optimality conditions and dominance relations from this text underpin our theoretical analysis.\\\\n    abstract: Comprehensive monograph on knapsack problems covering 0-1, bounded, unbounded, subset-sum, change-making, multiple-choice, and multi-dimensional variants. Chapter 11 covers MCKP including dominance, branch-and-bound, dynamic programming, and approximation algorithms.\\\\n    semantic_scholar_id: ''\\\\n    verified: true\\\\n    added_by: literature-survey\\\\n    added_at: '2026-05-14T10:30:00.000Z'\\\\n\\\", \\\"total_chars\\\": 36288, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/literature_map.yaml\", \"content\": \"meta:\\n  last_updated: '2026-05-14T10:30:00.000Z'\\n  total_papers: 35\\ncategories:\\n  - Mixed-Precision Rate-Distortion\\n  - KV Cache Quantization\\n  - KV Cache Eviction\\n  - Model Compression\\n  - Attention Head Analysis\\n  - LLM Inference Efficiency\\n  - Evaluation Models\\n  - Theory\\npapers:\\n  # ============================================================\\n  # Cluster 1: Mixed-Precision R-D Allocation (5 papers)\\n  # ============================================================\\n  zuo2026ratequant:\\n    title: 'RateQuant: Optimal Mixed-Precision KV Cache Quantization via Rate-Distortion Theory'\\n    authors:\\n    - Fei Zuo\\n    - Zikang Zhou\\n    - Hao Cong\\n    - Xiaoyan Xi\\n    - Ho Fai Leung\\n    year: 2026\\n    venue: arXiv 2026\\n    url: ''\\n    doi: '2605.06675'\\n    bibtex_key: zuo2026ratequant\\n    category: Mixed-Precision Rate-Distortion\\n    role: direct-competitor\\n    relevance: 'Primary competitor: R-D optimal per-head KV cache bit allocation. Algorithm 1 (discrete greedy). Theorem 2 (continuous closed-form via reverse waterfilling). Proposition 6 (greedy optimality on consecutive integers). Key limitation: does not address hardware-aligned non-consecutive {2,4,8,16} where greedy may fail.'\\n    abstract: RateQuant fits a per-quantizer distortion model D(b)=alpha*beta^{-b} from a small calibration set, then solves the bit-allocation in closed form via reverse waterfilling from rate-distortion theory. On Qwen3-8B at 2.5 avg bits, calibrated RateQuant reduces KIVI perplexity from 49.3 to 14.9 (70% reduction). Calibration takes 1.6s on a single GPU with zero inference overhead.\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research\\n    added_at: '2026-05-14T08:42:26.710Z'\\n  lei2026arkv:\\n    title: 'ARKV: Adaptive and Resource-Efficient KV Cache Management under Limited Memory Budget for Long-Context Inference in LLMs'\\n    authors:\\n    - Jianlong Lei\\n    - Shashikant Ilager\\n    year: 2026\\n    venue: arXiv 2026\\n    url: ''\\n    doi: '2603.08727'\\n    bibtex_key: lei2026arkv\\n    category: Mixed-Precision Rate-Distortion\\n    role: direct-competitor\\n    relevance: Adaptive mixed-precision KV cache with tri-state token assignment (Original/Quantization/Eviction). Per-layer OQ ratio estimation via attention entropy, variance, kurtosis. Alternative adaptive allocation strategy to our R-D formulation.\\n    abstract: 'ARKV dynamically allocates precision levels to cached tokens based on per-layer attention dynamics and token-level importance. Three components: per-layer OQ ratio estimation, token importance scoring, and tri-state cache assignment. Preserves ~97% baseline accuracy with 4x KV memory reduction.'\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research\\n    added_at: '2026-05-14T08:42:26.710Z'\\n  li2025kvmix:\\n    title: 'KVmix: Gradient-Based Layer Importance-Aware Mixed-Precision Quantization for KV Cache'\\n    authors:\\n    - Fei Li\\n    - Song Liu\\n    - Weiguo Wu\\n    - Shiqiang Nie\\n    - Jinyu Wang\\n    year: 2025\\n    venue: arXiv 2025\\n    url: ''\\n    doi: '2506.08018'\\n    bibtex_key: li2025kvmix\\n    category: Mixed-Precision Rate-Distortion\\n    role: method-component\\n    relevance: Gradient-based importance for layer-wise KV cache bit-width allocation. Heuristic sensitivity-based approach vs our R-D optimal formulation. Achieves near-lossless at Key 2.19bit / Value 2.38bit.\\n    abstract: KVmix employs gradient-based importance analysis to evaluate how individual Key and Value projection matrices affect model loss, enabling layer-specific bit-width allocation. Includes dynamic long-context optimization preserving full-precision KV pairs for recent pivotal tokens.\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research\\n    added_at: '2026-05-14T08:42:26.710Z'\\n  zhang2025mixkvq:\\n    title: 'MixKVQ: Query-Aware Mixed-Precision KV Cache Quantization for Long-Context Reasoning'\\n    authors:\\n    - Tao Zhang\\n    - Ziqian Zeng\\n    - Hao Peng\\n    - Huiping Zhuang\\n    - Cen Chen\\n    year: 2025\\n    venue: arXiv 2025\\n    url: ''\\n    doi: '2512.19206'\\n    bibtex_key: zhang2025mixkvq\\n    category: Mixed-Precision Rate-Distortion\\n    role: method-component\\n    relevance: 'Query-aware channel-level mixed-precision for KV cache. Orthogonal to our per-head R-D allocation: operates at channel granularity rather than head granularity.'\\n    abstract: MixKVQ introduces a lightweight query-aware algorithm to identify and preserve critical key channels at higher precision while applying per-token quantization for value cache. Outperforms existing low-bit methods on complex reasoning datasets.\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research\\n    added_at: '2026-05-14T08:42:26.710Z'\\n  kim2024squeezellm:\\n    title: 'SqueezeLLM: Dense-and-Sparse Quantization'\\n    authors:\\n    - Sehoon Kim\\n    - Coleman Hooper\\n    - Amir Gholami\\n    - Zhen Dong\\n    - Xiuyu Li\\n    - Sheng Shen\\n    - Michael W. Mahoney\\n    - Kurt Keutzer\\n    year: 2024\\n    venue: ICML 2024\\n    url: ''\\n    doi: '2306.07629'\\n    bibtex_key: kim2024squeezellm\\n    category: Mixed-Precision Rate-Distortion\\n    role: foundation\\n    relevance: Foundational sensitivity-based non-uniform quantization using second-order information. Pioneered per-group precision assignment based on sensitivity—principle we extend to per-head KV cache R-D allocation.\\n    abstract: 'SqueezeLLM enables lossless compression to ultra-low 3-bit precision via two ideas: sensitivity-based non-uniform quantization searching for optimal bit precision assignment, and Dense-and-Sparse decomposition storing outliers in efficient sparse format.'\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research\\n    added_at: '2026-05-14T08:42:26.710Z'\\n\\n  # ============================================================\\n  # Cluster 2: KV Cache Quantization (6 papers)\\n  # ============================================================\\n  liu2024kivi:\\n    title: 'KIVI: A Tuning-Free Asymmetric 2bit Quantization for KV Cache'\\n    authors:\\n    - Zirui Liu\\n    - Jiayi Yuan\\n    - Hongye Jin\\n    - Shaochen Zhong\\n    - Zhaozhuo Xu\\n    - Vladimir Braverman\\n    - Beidi Chen\\n    - Xia Hu\\n    year: 2024\\n    venue: ICML 2024\\n    url: ''\\n    doi: '2402.02750'\\n    bibtex_key: liu2024kivi\\n    category: KV Cache Quantization\\n    role: direct-competitor\\n    relevance: Asymmetric per-channel key / per-token value 2-bit KV cache quantization; tuning-free baseline for mixed-precision KV cache methods\\n    abstract: We conduct a comprehensive study on the element distribution in KV cache of popular LLMs and find that the key cache should be quantized per-channel while the value cache should be quantized per-token. From this observation, we develop a tuning-free 2bit KV cache quantization algorithm named KIVI.\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research\\n    added_at: '2026-05-14T07:56:45.265Z'\\n  hooper2024kvquant:\\n    title: 'KVQuant: Towards 10 Million Context Length LLM Inference with KV Cache Quantization'\\n    authors:\\n    - Coleman Hooper\\n    - Sehoon Kim\\n    - Hiva Mohammadzadeh\\n    - Michael W. Mahoney\\n    - Yakun Sophia Shao\\n    - Kurt Keutzer\\n    - Amir Gholami\\n    year: 2024\\n    venue: NeurIPS 2024\\n    url: ''\\n    doi: '2401.18079'\\n    bibtex_key: hooper2024kvquant\\n    category: KV Cache Quantization\\n    role: direct-competitor\\n    relevance: Per-channel key quantization with pre-RoPE, non-uniform datatypes, and dense-and-sparse outlier handling; achieves sub-4-bit KV cache for 10M context\\n    abstract: KV cache activations are the dominant contributor to memory consumption during LLM inference for large context windows. We address this with per-channel key quantization, pre-RoPE key quantization, non-uniform KV cache quantization, and per-vector dense-and-sparse quantization to isolate outliers.\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research\\n    added_at: '2026-05-14T07:56:45.265Z'\\n  lin2024qserve:\\n    title: 'QServe: W4A8KV4 Quantization and System Co-design for Efficient LLM Serving'\\n    authors:\\n    - Yujun Lin\\n    - Haotian Tang\\n    - Shang Yang\\n    - Zhekai Zhang\\n    - Guangxuan Xiao\\n    - Chuang Gan\\n    - Song Han\\n    year: 2024\\n    venue: MLSys 2025\\n    url: ''\\n    doi: '2405.04532'\\n    bibtex_key: lin2024qserve\\n    category: KV Cache Quantization\\n    role: foundation\\n    relevance: W4A8KV4 co-design with SmoothAttention for KV4 quantization; demonstrates system-level gains from joint weight-activation-KV quantization\\n    abstract: QServe introduces QoQ (W4A8KV4), a quantization algorithm with 4-bit weight, 8-bit activation, and 4-bit KV cache. Progressive group quantization ensures all GEMMs run on INT8 tensor cores. SmoothAttention shifts quantization difficulty from keys to queries.\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research\\n    added_at: '2026-05-14T07:56:45.265Z'\\n  he2024zipcache:\\n    title: 'ZipCache: Accurate and Efficient KV Cache Quantization with Salient Token Identification'\\n    authors:\\n    - Yefei He\\n    - Luoming Zhang\\n    - Weijia Wu\\n    - Jing Liu\\n    - Hong Zhou\\n    - Bohan Zhuang\\n    year: 2024\\n    venue: NeurIPS 2024\\n    url: ''\\n    doi: '2405.14256'\\n    bibtex_key: he2024zipcache\\n    category: KV Cache Quantization\\n    role: direct-competitor\\n    relevance: Channel-separable tokenwise quantization with adaptive bit-width based on normalized attention score saliency; mixed-precision KV cache baseline\\n    abstract: ZipCache proposes channel-separable tokenwise quantization and uses normalized attention score for identifying salient tokens with adaptive bit-width assignment. Achieves 4.98x compression on Mistral-7B with 0.38% accuracy drop.\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research\\n    added_at: '2026-05-14T07:56:45.265Z'\\n  kang2024gear:\\n    title: 'GEAR: An Efficient KV Cache Compression Recipe for Near-Lossless Generative Inference of LLM'\\n    authors:\\n    - Hao Kang\\n    - Qingru Zhang\\n    - Souvik Kundu\\n    - Geonhwa Jeong\\n    - Zaoxing Liu\\n    - Tushar Krishna\\n    - Tuo Zhao\\n    year: 2024\\n    venue: arXiv 2024\\n    url: ''\\n    doi: '2403.05527'\\n    bibtex_key: kang2024gear\\n    category: KV Cache Quantization\\n    role: direct-competitor\\n    relevance: Hybrid quantization + low-rank + sparse error correction for KV cache; demonstrates that residual compensation improves ultra-low-bit quantization quality\\n    abstract: GEAR first applies quantization to majority of entries to ultra-low precision, then employs a low rank matrix to approximate the quantization error, and a sparse matrix to remedy individual errors from outlier entries. Achieves near-lossless 4-bit compression with 2.38x throughput improvement.\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research\\n    added_at: '2026-05-14T07:56:45.265Z'\\n  duanmu2024skvq:\\n    title: 'SKVQ: Sliding-window Key and Value Cache Quantization for Large Language Models'\\n    authors:\\n    - Haojie Duanmu\\n    - Zhihang Yuan\\n    - Xiuhong Li\\n    - Jiangfei Duan\\n    - Xingcheng Zhang\\n    - Dahua Lin\\n    year: 2024\\n    venue: arXiv 2024\\n    url: ''\\n    doi: '2405.06219'\\n    bibtex_key: duanmu2024skvq\\n    category: KV Cache Quantization\\n    role: direct-competitor\\n    relevance: Channel rearrangement + sliding-window high-precision recent tokens; achieves 2-bit key / 1.5-bit value with minimal accuracy loss\\n    abstract: SKVQ rearranges KV cache channels to improve similarity within quantization groups and applies clipped dynamic quantization at group level. Preserves recent window tokens at high precision. Enables 2-bit keys and 1.5-bit values with up to 1M context on 80GB GPU.\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research\\n    added_at: '2026-05-14T07:56:45.265Z'\\n\\n  # ============================================================\\n  # Cluster 3: KV Cache Eviction (6 papers)\\n  # ============================================================\\n  zhang2023h2o:\\n    title: 'H2O: Heavy-Hitter Oracle for Efficient Generative Inference of Large Language Models'\\n    authors:\\n    - Zhenyu Zhang\\n    - Ying Sheng\\n    - Tianyi Zhou\\n    - Tianlong Chen\\n    - Lianmin Zheng\\n    - Ruisi Cai\\n    - Zhao Song\\n    - Yuandong Tian\\n    - Christopher Re\\n    - Clark Barrett\\n    - Zhangyang Wang\\n    - Beidi Chen\\n    year: 2023\\n    venue: NeurIPS 2023\\n    url: ''\\n    doi: 10.48550/arXiv.2306.14048\\n    bibtex_key: zhang2023h2o\\n    category: KV Cache Eviction\\n    role: background\\n    relevance: Foundational KV cache eviction policy based on heavy-hitter tokens; orthogonal to our quantization approach\\n    abstract: H2O identifies Heavy Hitters — a small set of tokens contributing most to attention scores — and dynamically retains recent and H2 tokens. With 20% heavy hitters, H2O improves throughput by up to 29x and reduces KV cache memory by up to 5x.\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research\\n    added_at: '2026-05-14T08:10:15.562Z'\\n  li2024snapkv:\\n    title: 'SnapKV: LLM Knows What You are Looking for Before Generation'\\n    authors:\\n    - Yuhong Li\\n    - Yingbing Huang\\n    - Bowen Yang\\n    - Bharat Venkitesh\\n    - Acyr Locatelli\\n    - Hanchen Ye\\n    - Tianle Cai\\n    - Patrick Lewis\\n    - Deming Chen\\n    year: 2024\\n    venue: NeurIPS 2024\\n    url: ''\\n    doi: 10.48550/arXiv.2404.14469\\n    bibtex_key: li2024snapkv\\n    category: KV Cache Eviction\\n    role: background\\n    relevance: Observation-driven KV cache compression using attention pattern consistency; competes with eviction-based approaches our work compares against\\n    abstract: SnapKV efficiently minimizes KV cache size by selecting clustered important KV positions per attention head using an observation window at the end of the prompt. Achieves 3.6x speed increase and 8.2x memory efficiency at 16K tokens.\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research\\n    added_at: '2026-05-14T08:10:15.562Z'\\n  ge2024fastgen:\\n    title: 'Model Tells You What to Discard: Adaptive KV Cache Compression for LLMs'\\n    authors:\\n    - Suyu Ge\\n    - Yunan Zhang\\n    - Liyuan Liu\\n    - Minjia Zhang\\n    - Jiawei Han\\n    - Jianfeng Gao\\n    year: 2024\\n    venue: ICLR 2024\\n    url: ''\\n    doi: 10.48550/arXiv.2310.01801\\n    bibtex_key: ge2024fastgen\\n    category: KV Cache Eviction\\n    role: background\\n    relevance: Adaptive per-head eviction strategy (FastGen); demonstrates head-specific compression is beneficial, complementary to quantization\\n    abstract: 'FastGen constructs KV cache adaptively per attention head: evicting long-range contexts on local-attention heads, discarding non-special tokens on special-token-focused heads, and using standard KV cache for broad-attention heads. Reduces memory by 50% without sacrificing quality.'\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research\\n    added_at: '2026-05-14T08:10:15.562Z'\\n  xiao2024streamingllm:\\n    title: Efficient Streaming Language Models with Attention Sinks\\n    authors:\\n    - Guangxuan Xiao\\n    - Yuandong Tian\\n    - Beidi Chen\\n    - Song Han\\n    - Mike Lewis\\n    year: 2024\\n    venue: ICLR 2024\\n    url: ''\\n    doi: 10.48550/arXiv.2309.17453\\n    bibtex_key: xiao2024streamingllm\\n    category: KV Cache Eviction\\n    role: background\\n    relevance: Discovers attention sink phenomenon in initial tokens; motivates why naive eviction can fail and informs our quantization-first approach\\n    abstract: StreamingLLM enables LLMs to generalize to infinite sequence lengths without fine-tuning by retaining attention sink tokens alongside a sliding window of recent tokens. Achieves up to 22.2x speedup over sliding window recomputation.\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research\\n    added_at: '2026-05-14T08:10:15.562Z'\\n  liu2024scissorhands:\\n    title: 'Scissorhands: Exploiting the Persistence of Importance Hypothesis for LLM KV Cache Compression at Test Time'\\n    authors:\\n    - Zichang Liu\\n    - Aditya Desai\\n    - Fangshuo Liao\\n    - Weitao Wang\\n    - Victor Xie\\n    - Zhaozhuo Xu\\n    - Anastasios Kyrillidis\\n    - Anshumali Shrivastava\\n    year: 2024\\n    venue: NeurIPS 2023\\n    url: ''\\n    doi: 10.48550/arXiv.2305.17118\\n    bibtex_key: liu2024scissorhands\\n    category: KV Cache Eviction\\n    role: background\\n    relevance: Persistence-of-importance hypothesis for KV cache eviction; achieves 5x cache reduction, combinable with 4-bit quantization for 20x compression\\n    abstract: Scissorhands maintains KV cache at a fixed budget by storing pivotal tokens with higher probability, achieving up to 5x memory reduction without quality loss, and up to 20x when combined with 4-bit quantization.\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research\\n    added_at: '2026-05-14T08:10:15.562Z'\\n  yang2024pyramidinfer:\\n    title: 'PyramidInfer: Pyramid KV Cache Compression for High-throughput LLM Inference'\\n    authors:\\n    - Dongjie Yang\\n    - Xiaodong Han\\n    - Yan Gao\\n    - Yao Hu\\n    - Shilin Zhang\\n    - Hai Zhao\\n    year: 2024\\n    venue: Findings of ACL 2024\\n    url: ''\\n    doi: 10.48550/arXiv.2405.12532\\n    bibtex_key: yang2024pyramidinfer\\n    category: KV Cache Eviction\\n    role: background\\n    relevance: Layer-wise pyramid compression exploiting inter-layer dependency; crucial KV count decreases across layers, relevant to our per-layer rate allocation\\n    abstract: PyramidInfer compresses KV cache by layer-wise retaining crucial context, exploiting the finding that crucial keys and values decrease layer by layer. Achieves 2.2x throughput improvement with 54% GPU memory reduction.\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research\\n    added_at: '2026-05-14T08:10:15.562Z'\\n\\n  # ============================================================\\n  # Cluster 4: Model Compression (6 papers)\\n  # ============================================================\\n  frantar2023gptq:\\n    title: 'GPTQ: Accurate Post-Training Quantization for Generative Pre-trained Transformers'\\n    authors:\\n    - Elias Frantar\\n    - Saleh Ashkboos\\n    - Torsten Hoefler\\n    - Dan Alistarh\\n    year: 2023\\n    venue: ICLR 2023\\n    url: ''\\n    doi: '2210.17323'\\n    bibtex_key: frantar2023gptq\\n    category: Model Compression\\n    role: foundation\\n    relevance: Foundational one-shot weight quantization based on approximate second-order information (OBQ). Reduces bitwidth to 3-4 bits per weight with negligible accuracy degradation. Established post-training quantization paradigm for LLMs.\\n    abstract: GPTQ is a one-shot weight quantization method based on approximate second-order information that can quantize GPT models with 175 billion parameters in approximately four GPU hours, reducing bitwidth to 3 or 4 bits per weight with negligible accuracy degradation.\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: literature-survey\\n    added_at: '2026-05-14T10:30:00.000Z'\\n  lin2024awq:\\n    title: 'AWQ: Activation-aware Weight Quantization for LLM Compression and Acceleration'\\n    authors:\\n    - Ji Lin\\n    - Jiaming Tang\\n    - Haotian Tang\\n    - Shang Yang\\n    - Wei-Ming Chen\\n    - Wei-Chen Wang\\n    - Guangxuan Xiao\\n    - Xingyu Dang\\n    - Chuang Gan\\n    - Song Han\\n    year: 2024\\n    venue: MLSys 2024 (Best Paper)\\n    url: ''\\n    doi: '2306.00978'\\n    bibtex_key: lin2024awq\\n    category: Model Compression\\n    role: foundation\\n    relevance: Activation-aware salient weight protection via equivalent scaling transformation. Demonstrates that 1% salient weights dominate quantization quality—analogous to our finding that per-head sensitivity varies drastically.\\n    abstract: AWQ finds that protecting only 1% salient weights (identified by activation distribution, not weights) greatly reduces quantization error. Scales salient channels via mathematically equivalent transformation. No backpropagation or reconstruction needed. 3x speedup over FP16.\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: literature-survey\\n    added_at: '2026-05-14T10:30:00.000Z'\\n  xiao2023smoothquant:\\n    title: 'SmoothQuant: Accurate and Efficient Post-Training Quantization for Large Language Models'\\n    authors:\\n    - Guangxuan Xiao\\n    - Ji Lin\\n    - Mickael Seznec\\n    - Hao Wu\\n    - Julien Demouth\\n    - Song Han\\n    year: 2023\\n    venue: ICML 2023\\n    url: ''\\n    doi: '2211.10438'\\n    bibtex_key: xiao2023smoothquant\\n    category: Model Compression\\n    role: foundation\\n    relevance: Smooths activation outliers by migrating quantization difficulty from activations to weights. Enables W8A8 for all matmuls in LLMs. QServe's SmoothAttention extends this idea to KV cache.\\n    abstract: SmoothQuant enables INT8 quantization of both weights and activations for all matrix multiplications in LLMs by smoothing activation outliers via offline migration of quantization difficulty from activations to weights. Up to 1.56x speedup and 2x memory reduction with negligible accuracy loss.\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: literature-survey\\n    added_at: '2026-05-14T10:30:00.000Z'\\n  dettmers2022llmint8:\\n    title: 'LLM.int8(): 8-bit Matrix Multiplication for Transformers at Scale'\\n    authors:\\n    - Tim Dettmers\\n    - Mike Lewis\\n    - Younes Belkada\\n    - Luke Zettlemoyer\\n    year: 2022\\n    venue: NeurIPS 2022\\n    url: ''\\n    doi: '2208.07339'\\n    bibtex_key: dettmers2022llmint8\\n    category: Model Compression\\n    role: foundation\\n    relevance: First to identify emergent outlier features in transformers that dominate quantization quality. Mixed-precision decomposition (0.1% in FP16, 99.9% in INT8) is conceptually related to our per-head mixed-precision allocation.\\n    abstract: LLM.int8() develops Int8 matrix multiplication for feed-forward and attention projection layers via absmax vector-wise quantization and mixed precision decomposition. Cuts inference memory by half while retaining full precision performance for 175B-parameter models.\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: literature-survey\\n    added_at: '2026-05-14T10:30:00.000Z'\\n  tseng2024quipsharp:\\n    title: 'QuIP#: Even Better LLM Quantization with Hadamard Incoherence and Lattice Codebooks'\\n    authors:\\n    - Albert Tseng\\n    - Jerry Chee\\n    - Qingyao Sun\\n    - Volodymyr Kuleshov\\n    - Christopher De Sa\\n    year: 2024\\n    venue: ICML 2024\\n    url: ''\\n    doi: '2402.04396'\\n    bibtex_key: tseng2024quipsharp\\n    category: Model Compression\\n    role: foundation\\n    relevance: State-of-the-art extreme compression (2-bit weights) via Hadamard incoherence processing and E8 lattice codebooks. Theoretical grounding for why incoherent distributions quantize better—relevant to understanding per-head distortion variation.\\n    abstract: QuIP# achieves state-of-the-art in extreme weight compression using randomized Hadamard transform for incoherence processing, E8 lattice codebooks for vector quantization of sub-Gaussian incoherent weights, and fine-tuning for fidelity. Hardware-efficient implementation.\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: literature-survey\\n    added_at: '2026-05-14T10:30:00.000Z'\\n  zhao2024atom:\\n    title: 'Atom: Low-bit Quantization for Efficient and Accurate LLM Serving'\\n    authors:\\n    - Yilong Zhao\\n    - Chien-Yu Lin\\n    - Kan Zhu\\n    - Zihao Ye\\n    - Lequn Chen\\n    - Size Zheng\\n    - Luis Ceze\\n    - Arvind Krishnamurthy\\n    - Tianqi Chen\\n    - Baris Kasikci\\n    year: 2024\\n    venue: MLSys 2024\\n    url: ''\\n    doi: '2310.19102'\\n    bibtex_key: zhao2024atom\\n    category: Model Compression\\n    role: foundation\\n    relevance: End-to-end low-bit quantization for serving with mixed-precision, group quantization, and KV cache quantization. Demonstrates system-level throughput gains (3.5x over FP16) from co-designed quantization kernels.\\n    abstract: Atom combines mixed-precision quantization retaining salient activations/weights in high precision, fine-grained group quantization, dynamic activation quantization, KV-cache quantization, and efficient CUDA kernels. Achieves 7.73x throughput over FP16 baseline.\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: literature-survey\\n    added_at: '2026-05-14T10:30:00.000Z'\\n\\n  # ============================================================\\n  # Cluster 5: Attention Head Analysis (4 papers)\\n  # ============================================================\\n  voita2019heads:\\n    title: 'Analyzing Multi-Head Self-Attention: Specialized Heads Do the Heavy Lifting, the Rest Can Be Pruned'\\n    authors:\\n    - Elena Voita\\n    - David Talbot\\n    - Fedor Moiseev\\n    - Rico Sennrich\\n    - Ivan Titov\\n    year: 2019\\n    venue: ACL 2019\\n    url: ''\\n    doi: '1905.09418'\\n    bibtex_key: voita2019heads\\n    category: Attention Head Analysis\\n    role: foundation\\n    relevance: Foundational work on attention head specialization and pruning. Shows most heads can be pruned (38/48 with only 0.15 BLEU drop). Motivates our per-head heterogeneous quantization—heads have different importance and roles.\\n    abstract: Evaluates individual attention head contributions and identifies specialized heads playing consistent linguistically-interpretable roles. Using stochastic gates with L0 penalty, the vast majority of heads can be pruned without seriously affecting performance.\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: literature-survey\\n    added_at: '2026-05-14T10:30:00.000Z'\\n  michel2019sixteen:\\n    title: Are Sixteen Heads Really Better than One?\\n    authors:\\n    - Paul Michel\\n    - Omer Levy\\n    - Graham Neubig\\n    year: 2019\\n    venue: NeurIPS 2019\\n    url: ''\\n    doi: '1905.10650'\\n    bibtex_key: michel2019sixteen\\n    category: Attention Head Analysis\\n    role: foundation\\n    relevance: Shows large proportion of attention heads can be removed at test time. Greedy pruning analysis reveals varying head importance. Directly supports our premise that heads deserve different quantization precision.\\n    abstract: A large proportion of attention heads can be removed at test time without significantly impacting performance, and some layers can be reduced to a single head. Self-attention layers can be significantly pruned while encoder-decoder layers are more dependent on multi-headedness.\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: literature-survey\\n    added_at: '2026-05-14T10:30:00.000Z'\\n  clark2019bert:\\n    title: What Does BERT Look At? An Analysis of BERT's Attention\\n    authors:\\n    - Kevin Clark\\n    - Urvashi Khandelwal\\n    - Omer Levy\\n    - Christopher D. Manning\\n    year: 2019\\n    venue: ACL Workshop BlackboxNLP 2019\\n    url: ''\\n    doi: '1906.04341'\\n    bibtex_key: clark2019bert\\n    category: Attention Head Analysis\\n    role: background\\n    relevance: Characterizes attention head behavior patterns (delimiter tokens, positional offsets, broad attention). Shows heads in same layer often exhibit similar behaviors—relevant to understanding GQA group structure.\\n    abstract: Proposes methods for analyzing attention mechanisms of pre-trained models. Finds BERT heads exhibit patterns like attending to delimiter tokens, positional offsets, or broadly over sentences. Certain heads correspond to syntactic and coreference relations with high accuracy.\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: literature-survey\\n    added_at: '2026-05-14T10:30:00.000Z'\\n  ainslie2023gqa:\\n    title: 'GQA: Training Generalized Multi-Query Transformer Models from Multi-Head Checkpoints'\\n    authors:\\n    - Joshua Ainslie\\n    - James Lee-Thorp\\n    - Michiel de Jong\\n    - Yury Zemlyanskiy\\n    - Federico Lebron\\n    - Sumit Sanghai\\n    year: 2023\\n    venue: EMNLP 2023\\n    url: ''\\n    doi: '2305.13245'\\n    bibtex_key: ainslie2023gqa\\n    category: Attention Head Analysis\\n    role: foundation\\n    relevance: Defines grouped-query attention (GQA) which is the architecture used by all three models we evaluate (Qwen2.5 7:1, Llama-3.1 4:1, Mistral 4:1). GQA group ratio directly affects our per-head allocation granularity and results.\\n    abstract: Proposes grouped-query attention (GQA), a generalization of multi-query attention using an intermediate number of key-value heads. Uptrained GQA achieves quality close to multi-head attention with comparable speed to MQA. Provides recipe for uptraining existing MHA checkpoints.\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: literature-survey\\n    added_at: '2026-05-14T10:30:00.000Z'\\n\\n  # ============================================================\\n  # Cluster 6: LLM Inference Efficiency (4 papers)\\n  # ============================================================\\n  kwon2023vllm:\\n    title: Efficient Memory Management for Large Language Model Serving with PagedAttention\\n    authors:\\n    - Woosuk Kwon\\n    - Zhuohan Li\\n    - Siyuan Zhuang\\n    - Ying Sheng\\n    - Lianmin Zheng\\n    - Cody Hao Yu\\n    - Joseph E. Gonzalez\\n    - Hao Zhang\\n    - Ion Stoica\\n    year: 2023\\n    venue: SOSP 2023\\n    url: ''\\n    doi: '2309.06180'\\n    bibtex_key: kwon2023vllm\\n    category: LLM Inference Efficiency\\n    role: background\\n    relevance: PagedAttention enables non-contiguous KV cache storage, reducing memory waste. Our per-head mixed-precision allocation is complementary—can be applied within vLLM's paged memory management.\\n    abstract: vLLM proposes PagedAttention inspired by virtual memory paging, achieving near-zero waste in KV cache memory and flexible sharing within and across requests. 2-4x throughput improvement over state-of-the-art systems.\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: literature-survey\\n    added_at: '2026-05-14T10:30:00.000Z'\\n  dao2022flashattention:\\n    title: 'FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness'\\n    authors:\\n    - Tri Dao\\n    - Daniel Y. Fu\\n    - Stefano Ermon\\n    - Atri Rudra\\n    - Christopher Re\\n    year: 2022\\n    venue: NeurIPS 2022\\n    url: ''\\n    doi: '2205.14135'\\n    bibtex_key: dao2022flashattention\\n    category: LLM Inference Efficiency\\n    role: background\\n    relevance: IO-aware tiling for exact attention. Our quantized KV cache reduces HBM reads during attention, providing complementary gains to FlashAttention's tiling strategy.\\n    abstract: FlashAttention uses tiling to reduce memory reads/writes between GPU HBM and SRAM. 15% speedup on BERT-large, 3x on GPT-2, 2.4x on long-range arena, without approximation.\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: literature-survey\\n    added_at: '2026-05-14T10:30:00.000Z'\\n  shazeer2019mqa:\\n    title: 'Fast Transformer Decoding: One Write-Head is All You Need'\\n    authors:\\n    - Noam Shazeer\\n    year: 2019\\n    venue: arXiv 2019\\n    url: ''\\n    doi: '1911.02150'\\n    bibtex_key: shazeer2019mqa\\n    category: LLM Inference Efficiency\\n    role: foundation\\n    relevance: Introduces multi-query attention (MQA) sharing a single KV head across all query heads. GQA generalizes MQA. Our per-head allocation exploits the remaining KV head heterogeneity in GQA models.\\n    abstract: Proposes multi-query attention where keys and values are shared across all attention heads, greatly reducing KV cache size and memory bandwidth requirements of incremental decoding. Much faster decoding with minor quality degradation.\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: literature-survey\\n    added_at: '2026-05-14T10:30:00.000Z'\\n  deepseek2024v2:\\n    title: 'DeepSeek-V2: A Strong, Economical, and Efficient Mixture-of-Experts Language Model'\\n    authors:\\n    - DeepSeek-AI\\n    year: 2024\\n    venue: arXiv 2024\\n    url: ''\\n    doi: '2405.04434'\\n    bibtex_key: deepseek2024v2\\n    category: LLM Inference Efficiency\\n    role: background\\n    relevance: Introduces Multi-head Latent Attention (MLA) compressing KV cache into low-rank latent vectors (93.3% reduction). Alternative architectural approach to KV cache reduction vs our post-training quantization.\\n    abstract: DeepSeek-V2 uses Multi-head Latent Attention (MLA) compressing KV caches into latent vectors and DeepSeekMoE for sparse computation. 236B total parameters, 21B activated per token. 42.5% training cost reduction, 93.3% KV cache reduction, 5.76x throughput increase vs DeepSeek 67B.\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: literature-survey\\n    added_at: '2026-05-14T10:30:00.000Z'\\n\\n  # ============================================================\\n  # Cluster 7: Evaluation Models (3 papers)\\n  # ============================================================\\n  grattafiori2024llama3:\\n    title: The Llama 3 Herd of Models\\n    authors:\\n    - Aaron Grattafiori\\n    - et al.\\n    year: 2024\\n    venue: arXiv 2024\\n    url: ''\\n    doi: '2407.21783'\\n    bibtex_key: grattafiori2024llama3\\n    category: Evaluation Models\\n    role: evaluation\\n    relevance: Llama-3.1-8B is one of three evaluation models. GQA with 4:1 ratio (8 KV heads, 32 query heads). Marginal gains from per-head allocation in our experiments.\\n    abstract: Llama 3 is a herd of foundation models natively supporting multilinguality, coding, reasoning, and tool usage. Dense Transformer up to 405B parameters with 128K context. Comparable quality to GPT-4.\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: literature-survey\\n    added_at: '2026-05-14T10:30:00.000Z'\\n  yang2025qwen25:\\n    title: Qwen2.5 Technical Report\\n    authors:\\n    - An Yang\\n    - et al.\\n    year: 2025\\n    venue: arXiv 2024\\n    url: ''\\n    doi: '2412.15115'\\n    bibtex_key: yang2025qwen25\\n    category: Evaluation Models\\n    role: evaluation\\n    relevance: Qwen2.5-7B is our strongest-result model. GQA with 7:1 ratio (4 KV heads, 28 query heads)—highest heterogeneity among tested models, yielding 29.3% PPL improvement from per-head allocation.\\n    abstract: Qwen2.5 is a comprehensive LLM series with improvements in pre-training (18T tokens) and post-training. Qwen2.5-72B-Instruct outperforms many open and proprietary models, competitive with Llama-3-405B-Instruct at 5x smaller size.\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: literature-survey\\n    added_at: '2026-05-14T10:30:00.000Z'\\n  jiang2023mistral:\\n    title: Mistral 7B\\n    authors:\\n    - Albert Q. Jiang\\n    - Alexandre Sablayrolles\\n    - Arthur Mensch\\n    - Chris Bamford\\n    - Devendra Singh Chaplot\\n    - Diego de las Casas\\n    - Florian Bressand\\n    - Gianna Lengyel\\n    - Guillaume Lample\\n    - Lucile Saulnier\\n    - Lelio Renard Lavaud\\n    - Marie-Anne Lachaux\\n    - Pierre Stock\\n    - Teven Le Scao\\n    - Thibaut Lavril\\n    - Thomas Wang\\n    - Timothee Lacroix\\n    - William El Sayed\\n    year: 2023\\n    venue: arXiv 2023\\n    url: ''\\n    doi: '2310.06825'\\n    bibtex_key: jiang2023mistral\\n    category: Evaluation Models\\n    role: evaluation\\n    relevance: Mistral-7B-v0.3 is our third evaluation model. GQA with 4:1 ratio (8 KV heads, 32 query heads). Negative result from per-head allocation—demonstrates architecture-dependent effectiveness.\\n    abstract: Mistral 7B leverages grouped-query attention (GQA) for faster inference and sliding window attention (SWA) for handling arbitrary-length sequences with reduced cost. Outperforms Llama 2 13B on all benchmarks.\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: literature-survey\\n    added_at: '2026-05-14T10:30:00.000Z'\\n\\n  # ============================================================\\n  # Cluster 8: Theory (1 paper)\\n  # ============================================================\\n  kellerer2004knapsack:\\n    title: Knapsack Problems\\n    authors:\\n    - Hans Kellerer\\n    - Ulrich Pferschy\\n    - David Pisinger\\n    year: 2004\\n    venue: Springer\\n    url: ''\\n    doi: 10.1007/978-3-540-24777-7\\n    bibtex_key: kellerer2004knapsack\\n    category: Theory\\n    role: foundation\\n    relevance: Definitive reference for multiple-choice knapsack problem (MCKP, Chapter 11). Our per-head bit allocation with hardware-aligned {2,4,8,16} is formulated as MCKP. Greedy optimality conditions and dominance relations from this text underpin our theoretical analysis.\\n    abstract: Comprehensive monograph on knapsack problems covering 0-1, bounded, unbounded, subset-sum, change-making, multiple-choice, and multi-dimensional variants. Chapter 11 covers MCKP including dominance, branch-and-bound, dynamic programming, and approximation algorithms.\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: literature-survey\\n    added_at: '2026-05-14T10:30:00.000Z'\\n\", \"total_chars\": 36288, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "540b7bd7-a7b9-49bb-b9c2-76f662a7a87b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "0e163909-e397-4f29-9722-d542e29e1bd1",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-14T19:05:56.187Z_

<details><summary>↩ Tool result · `toolu_019z7MaVDJzR6vDUomMXx2Jt`</summary>

```text
1	# Literature Survey: KV Cache Heterogeneity Distribution Shape (Spike vs Spread)
2	
3	**Date**: 2026-05-14
4	**Context**: RateKV project — per-KV-head non-uniform bit-width allocation via constrained MCKP solver. Core finding: sensitivity heterogeneity distribution shape (spike vs spread) determines MCKP allocator effectiveness, not GQA ratio.
5	
6	---
7	
8	## 1. Direct Competitors (Per-Head Mixed-Precision KV Cache Quantization)
9	
10	### 1.1 RateQuant (2026)
11	- **Title**: RateQuant: Optimal Mixed-Precision KV Cache Quantization via Rate-Distortion Theory
12	- **Authors**: (arXiv:2605.06675)
13	- **Venue**: arXiv preprint, May 2026
14	- **Category**: **Direct competitor**
15	- **Summary**: First to apply rate-distortion theory to per-head KV cache bit allocation. Uses reverse waterfilling for closed-form allocation. Fits per-quantizer distortion model D(b)=α·β^{-b}, with β varying 3.6–5.3 across quantizers. Key metric: AM/GM ratio of head sensitivities predicts achievable distortion reduction without any quantization. Gradient-based importance yields 1.07 PPL improvement over activation-based at 3.5 bits.
16	- **Results**: On Qwen3-8B at 2.5 bits, reduces KIVI PPL from 49.3 to 14.9 (70% reduction). On TurboQuant at 4.0 bits, recovers 66% of quantization-induced degradation.
17	- **Relation to our work**: **Closest competitor**. RateQuant uses AM/GM ratio as a scalar heterogeneity metric but does NOT analyze the distribution *shape* (spike vs spread). Their AM/GM captures heterogeneity magnitude, not whether it comes from one extreme outlier (spike) or a distributed cluster (spread). Our contribution: explaining *why* some models benefit from non-uniform allocation and others don't, through distribution shape analysis. RateQuant would predict benefit whenever AM/GM > 1 but cannot explain the Yi-1.5 failure case (high AM/GM from spike pattern, yet negative returns).
18	
19	### 1.2 KVTuner (2025)
20	- **Title**: KVTuner: Sensitivity-Aware Layer-Wise Mixed-Precision KV Cache Quantization for Efficient and Nearly Lossless LLM Inference
21	- **Authors**: Li et al.
22	- **Venue**: ICML 2025
23	- **Category**: **Direct competitor** (layer-level, not head-level)
24	- **Summary**: Uses Pareto search over hardware-friendly layer-wise K/V precision pairs. Achieves nearly lossless 3.25-bit for Llama-3.1-8B, 4.0-bit for Qwen2.5-7B. Gradient-based sensitivity shows U-shaped pattern (early+late layers sensitive); activation-based is monotonically increasing.
25	- **Relation to our work**: Operates at layer granularity, not head granularity. Does not analyze within-layer head heterogeneity distribution shape. Notes that Qwen2.5-7B requires higher precision → consistent with our finding of Qwen's spread pattern requiring differentiated allocation.
26	
27	### 1.3 PM-KVQ (2025)
28	- **Title**: PM-KVQ: Progressive Mixed-Precision KV Cache Quantization for Long-CoT LLMs
29	- **Authors**: Chen et al.
30	- **Venue**: arXiv:2505.18610
31	- **Category**: **Method component**
32	- **Summary**: Progressive quantization strategy that gradually lowers bit-width over decoding steps. Block-wise memory allocation assigns higher bits to sensitive transformer blocks. Uses integer programming for allocation.
33	- **Relation to our work**: Temporal dimension (progressive) is orthogonal to our spatial (per-head) analysis. Does not analyze head-level heterogeneity distribution shapes.
34	
35	### 1.4 MixKVQ (2025)
36	- **Title**: MixKVQ: Query-Aware Mixed-Precision KV Cache Quantization for Long-Context Reasoning
37	- **Authors**: (arXiv:2512.19206)
38	- **Venue**: arXiv, Dec 2025
39	- **Category**: **Method component**
40	- **Summary**: Query-aware algorithm identifies critical key channels needing higher precision. Combines intrinsic quantization difficulty with query relevance. Per-channel mixed precision for keys, per-token for values.
41	- **Relation to our work**: Operates at channel granularity within heads, not across heads. The "intrinsic quantization difficulty" concept relates to sensitivity heterogeneity but is measured per-channel, not per-head.
42	
43	### 1.5 KVmix (2025)
44	- **Title**: KVmix: Gradient-Based Layer Importance-Aware Mixed-Precision Quantization for KV Cache
45	- **Authors**: (arXiv:2506.08018; AAAI 2026)
46	- **Venue**: AAAI 2026
47	- **Category**: **Direct competitor** (layer-level)
48	- **Summary**: Gradient-based importance analysis for layer-specific K/V bit-width allocation. Achieves K 2.19-bit / V 2.38-bit with 4.9× compression. Introduces dynamic long-context optimization for recent pivotal tokens.
49	- **Relation to our work**: Layer-level, not head-level. Confirms K/V asymmetric sensitivity (consistent with our K/V separation findings).
50	
51	---
52	
53	## 2. Spike vs Spread / Outlier Pattern Analysis
54	
55	### 2.1 "Precision Where It Matters" — Spike-Aware Quantization (2025)
56	- **Title**: Precision Where It Matters: A Novel Spike Aware Mixed-Precision Quantization Strategy for LLaMA-based Language Models
57	- **Authors**: (arXiv:2504.21553)
58	- **Venue**: Springer, April 2025
59	- **Category**: **Background — spike pattern in activations (not heads)**
60	- **Summary**: Identifies activation spikes concentrated in down projections of exactly 2 layers (one early, one late) in LLaMA. Spikes reach values up to 2500. Solution: FP8 for spiking layers, INT8 for rest. 30+ PPL reduction on LLaMA3-8B.
61	- **Relation to our work**: Uses "spike" terminology for activation outliers, not head sensitivity distribution. The spike/spread dichotomy is analogous but operates at a different level (activation magnitude within layers vs. sensitivity distribution across heads). Supports the broader idea that spike-like concentration has different optimization implications than spread-like distributions.
62	
63	### 2.2 CMPQ — Channel-Wise Mixed-Precision Quantization (2024)
64	- **Title**: Channel-Wise Mixed-Precision Quantization for Large Language Models
65	- **Authors**: Chen & Xie et al.
66	- **Venue**: arXiv:2410.13056, Oct 2024
67	- **Category**: **Background — channel-level outlier patterns**
68	- **Summary**: Allocates precision per-channel based on activation distribution. Distinguishes activation-based outliers (persistent in specific channels) from quantization-based outliers. ~0.5% of values are outliers. Uses L2-norm per channel for allocation.
69	- **Relation to our work**: Channel-level analogue of our head-level analysis. The observation that outlier concentration varies by channel parallels our head-level spike vs spread finding, but at finer granularity and for weight/activation quantization, not KV cache.
70	
71	### 2.3 KITTY — Dynamic Channel-wise Precision Boost (2025)
72	- **Title**: Kitty: Accurate and Efficient 2-bit KV Cache Quantization with Dynamic Channel-wise Precision Boost
73	- **Authors**: (arXiv:2511.18643)
74	- **Venue**: arXiv, Nov 2025
75	- **Category**: **Method component**
76	- **Summary**: Ranks Key-cache channels by sensitivity; keeps small fraction at higher precision. "Critical channels play a disproportionately important role." Decomposes mixed-precision Key pages into two uniform 2-bit tensors for hardware efficiency.
77	- **Relation to our work**: Channel-level analogue within keys. The finding that "critical channels play disproportionately important roles" is consistent with our heterogeneity thesis, but KITTY does not analyze whether the critical channel distribution is spike-like or spread-like.
78	
79	### 2.4 MUXQ — Low-Rank Outlier Decomposition (2026)
80	- **Title**: MUXQ: Mixed-to-Uniform Precision Matrix Quantization via Low-Rank Outlier Decomposition
81	- **Authors**: (arXiv:2604.04701)
82	- **Venue**: arXiv, April 2026
83	- **Category**: **Background**
84	- **Summary**: Decomposes outlier channels into a low-rank matrix to convert mixed-precision quantization into uniform precision. Applies rotation/permutation to redistribute outlier energy.
85	- **Relation to our work**: Addresses outliers via decomposition rather than differentiated allocation. Different philosophy: eliminate heterogeneity (smoothing) vs. exploit heterogeneity (our approach).
86	
87	---
88	
89	## 3. Head-Specific KV Cache Compression (Eviction-based, not Quantization)
90	
91	### 3.1 HeadKV / "Not All Heads Matter" (2024)
92	- **Title**: Not All Heads Matter: A Head-Level KV Cache Compression Method with Integrated Retrieval and Reasoning
93	- **Authors**: Fu et al.
94	- **Venue**: ICLR 2025 (arXiv:2410.19258)
95	- **Category**: **Background — head importance for eviction**
96	- **Summary**: Head-level KV cache budget allocation based on importance scores from Needle-in-a-Haystack probing. Retains 1.5% KV cache with 97% performance. Different heads serve retrieval vs reasoning roles.
97	- **Relation to our work**: Confirms head-level importance heterogeneity exists and is exploitable. Does not analyze the distribution shape of this heterogeneity. Eviction-based, not quantization-based.
98	
99	### 3.2 AdaKV (2024)
100	- **Title**: Ada-KV: Optimizing KV Cache Eviction by Adaptive Budget Allocation
101	- **Authors**: Feng et al.
102	- **Venue**: NeurIPS 2025 (arXiv:2407.11550)
103	- **Category**: **Background — adaptive head budget**
104	- **Summary**: Adaptive per-head budget allocation for KV eviction. Extends SnapKV/PyramidKV with head-wise adaptive allocation. Key insight: uniform compression rate across heads is a "rigidity" that hurts performance.
105	- **Relation to our work**: Directly supports our thesis that head-level heterogeneity matters. But AdaKV addresses eviction budgets (how many tokens to keep per head), not quantization bit-width. Does not analyze spike vs spread patterns.
106	
107	### 3.3 KV-Compress (2024)
108	- **Title**: KV-Compress: Paged KV-Cache Compression with Variable Compression Rates per Attention Head
109	- **Authors**: Rehg
110	- **Venue**: arXiv:2410.00161, Oct 2024
111	- **Category**: **Background — variable-rate per-head compression**
112	- **Summary**: Variable compression rates across attention heads within PagedAttention framework. Proposes query-group-compression for GQA models yielding additional 4× compression. 8× compression with negligible impact on Llama-3.1.
113	- **Relation to our work**: Confirms per-head heterogeneity is exploitable for compression. Addresses GQA grouping explicitly. Does not analyze why some heads/models benefit more (no spike vs spread analysis).
114	
115	### 3.4 PyramidKV (2024)
116	- **Title**: PyramidKV: Dynamic KV Cache Compression based on Pyramidal Information Funneling
117	- **Authors**: Cai et al.
118	- **Venue**: arXiv:2406.02069
119	- **Category**: **Background**
120	- **Summary**: Attention scatters widely in lower layers, consolidates in higher layers → pyramidal budget allocation (more cache for lower layers). Layer-level, not head-level.
121	- **Relation to our work**: Layer-level heterogeneity analysis. Complementary perspective but no head-level distribution shape analysis.
122	
123	---
124	
125	## 4. GQA Ratio and Quantization Sensitivity
126	
127	### 4.1 GQA Original Paper (2023)
128	- **Title**: GQA: Training Generalized Multi-Query Transformer Models from Multi-Head Checkpoints
129	- **Authors**: Ainslie et al.
130	- **Venue**: EMNLP 2023 (arXiv:2305.13245)
131	- **Category**: **Background**
132	- **Summary**: Proposes GQA as interpolation between MHA and MQA. Does not discuss quantization sensitivity implications of GQA ratio.
133	- **Relation to our work**: Foundational paper. Our finding that GQA ratio is NOT a reliable proxy for heterogeneity is novel — the original paper does not address this.
134	
135	### 4.2 QCQA — Quality-and-Capacity-Aware Grouping (2025)
136	- **Title**: Quality- and Capacity-Aware Grouped Query Attention
137	- **Venue**: 2025
138	- **Category**: **Background — GQA grouping optimization**
139	- **Summary**: Evolutionary algorithm to discover optimal query-head groupings that minimize accuracy loss under KV-cache constraints. Achieves 20% higher accuracy at equal cache size vs naive GQA, or 40% KV reduction at same accuracy.
140	- **Relation to our work**: Addresses the grouping structure of GQA but not quantization. Supports the idea that the default GQA grouping may not be optimal, which is related to our finding about GQA ratio being a poor proxy.
141	
142	---
143	
144	## 5. MCKP / Constrained Optimization for Bit Allocation
145	
146	### 5.1 MPQCO (2021)
147	- **Title**: Towards Mixed-Precision Quantization of Neural Networks via Constrained Optimization
148	- **Authors**: Chen, Wang, Cheng
149	- **Venue**: ICCV 2021
150	- **Category**: **Method component — MCKP formulation origin**
151	- **Summary**: Formulates mixed-precision quantization as MCKP. Uses second-order Taylor expansion + Hessian for sensitivity. Greedy solver. 5–10 min calibration. Principled and efficient.
152	- **Relation to our work**: We use the same MCKP formulation. MPQCO applies it to weight quantization layer-wise; we apply it to KV cache head-wise. MPQCO does not analyze when MCKP allocation fails (i.e., no spike vs spread analysis).
153	
154	### 5.2 JointSQ (2024)
155	- **Title**: JointSQ: Joint Sparsification-Quantization for Distributed Learning
156	- **Authors**: Xie et al.
157	- **Venue**: CVPR 2024
158	- **Category**: **Background**
159	- **Summary**: Joint sparsity-quantization optimization via MCKP where profit = -error, weight = storage.
160	- **Relation to our work**: Uses MCKP but for sparsity+quantization jointly, not for KV cache head-level allocation.
161	
162	---
163	
164	## 6. Foundational KV Cache Quantization Methods
165	
166	### 6.1 KIVI (2024)
167	- **Title**: KIVI: A Tuning-Free Asymmetric 2bit Quantization for KV Cache
168	- **Authors**: Liu & Yuan et al.
169	- **Venue**: ICML 2024 (arXiv:2402.02750)
170	- **Category**: **Evaluation baseline**
171	- **Summary**: Per-channel symmetric quantization for keys, per-token asymmetric for values. Tuning-free 2-bit. Establishes K/V asymmetry as important principle.
172	- **Relation to our work**: Baseline quantizer. Our MCKP allocator can sit on top of KIVI. KIVI applies uniform bit-width — our work addresses its limitation.
173	
174	### 6.2 KVQuant (2024)
175	- **Title**: KVQuant: Towards 10 Million Context Length LLM Inference with KV Cache Quantization
176	- **Authors**: (arXiv:2401.18079)
177	- **Venue**: NeurIPS 2024
178	- **Category**: **Evaluation baseline**
179	- **Summary**: Per-layer sensitivity-weighted non-uniform datatypes. Handles outlier channels. Extends to 3-bit and 2-bit from FlexGen's 4-bit.
180	- **Relation to our work**: Layer-level non-uniform datatype design, not head-level bit allocation. Pioneered per-layer sensitivity analysis for KV cache.
181	
182	### 6.3 RotateKV (2025)
183	- **Title**: RotateKV: Accurate and Robust 2-Bit KV Cache Quantization
184	- **Venue**: IJCAI 2025
185	- **Category**: **Evaluation baseline**
186	- **Summary**: Outlier-aware rotation to enhance quantization adaptability across diverse outlier distributions.
187	- **Relation to our work**: Smoothing-based approach (eliminate heterogeneity) vs our exploitation-based approach (allocate to heterogeneity).
188	
189	---
190	
191	## 7. Distribution Shape Metrics
192	
193	### 7.1 Mix-QViT — Layer Importance + Quantization Sensitivity (2025)
194	- **Title**: Mix-QViT: Mixed-Precision Vision Transformer Quantization Driven by Layer Importance and Quantization Sensitivity
195	- **Authors**: (arXiv:2501.06357)
196	- **Venue**: arXiv, Jan 2025
197	- **Category**: **Background — sensitivity metrics for ViTs**
198	- **Summary**: Dual scoring: explainability-based layer importance (via LRP) + quantization sensitivity per layer. Uses these scores for mixed-precision allocation in Vision Transformers.
199	- **Relation to our work**: Uses sensitivity metrics for allocation but does not analyze distribution shape. Applied to ViTs, not LLMs.
200	
201	### 7.2 Representational Compactness via Singular Values
202	- **Category**: **Background — concentration metric**
203	- **Summary**: Singular value distribution as a measure of information concentration: uniform SVs → high compactness (redundant); few dominant SVs → low compactness (concentrated/sensitive).
204	- **Relation to our work**: SVD-based concentration measurement is related to our Gini/CV analysis of head sensitivity distributions. The "few dominant SVs" scenario parallels our "spike" pattern.
205	
206	---
207	
208	## 8. Novelty Assessment
209	
210	### What already exists:
211	1. **Head-level heterogeneity is well-documented**: HeadKV, AdaKV, KV-Compress, RateQuant all confirm heads have varying importance
212	2. **MCKP for mixed-precision allocation**: MPQCO (2021) established the formulation; RateQuant (2026) applies rate-distortion allocation to KV cache per-head
213	3. **AM/GM ratio as heterogeneity scalar**: RateQuant proposes this as a predictor of allocation benefit
214	4. **Spike-aware quantization for activations**: "Precision Where It Matters" addresses spike patterns in activation magnitudes
215	
216	### What is NOVEL in our work:
217	1. **Distribution shape analysis (spike vs spread)**: No prior work explicitly analyzes how the *shape* of the head sensitivity distribution determines allocation effectiveness. RateQuant's AM/GM is a scalar that captures magnitude but not shape — two distributions with identical AM/GM can have very different shapes (one spike outlier vs distributed cluster)
218	2. **GQA ratio ≠ heterogeneity proxy**: No prior work has shown that GQA ratio fails to predict allocation benefit. Yi-1.5-9B (highest GQA 8:1) with spike pattern yields negative returns despite high heterogeneity magnitude — this finding is absent from all surveyed papers
219	3. **Failure mode characterization**: Prior work reports when mixed-precision helps; we characterize *when and why it fails* (spike pattern concentrates sensitivity in a single head that cannot be further differentiated by allocation)
220	4. **Cross-model shape taxonomy**: Systematic classification of 5 models into spike/spread patterns with predictive power for MCKP effectiveness
221	
222	### Positioning relative to RateQuant:
223	RateQuant is the closest competitor (same per-head granularity, similar MCKP-style allocation). Our contribution is **complementary and deeper**: RateQuant provides the allocation mechanism; we explain *when allocation mechanisms work*. RateQuant's AM/GM metric would incorrectly predict benefit for Yi-1.5-9B (high AM/GM from spike pattern). Our spike vs spread analysis provides a more informative predictor.
224	
225	---
226	
227	## 9. Papers to Cite (by section)
228	
229	### Related Work — KV Cache Quantization
230	- KIVI (Liu & Yuan et al., ICML 2024)
231	- KVQuant (NeurIPS 2024)
232	- RotateKV (IJCAI 2025)
233	- KITTY (arXiv 2511.18643, 2025)
234	
235	### Related Work — Mixed-Precision KV Cache
236	- KVTuner (Li et al., ICML 2025)
237	- KVmix (AAAI 2026)
238	- PM-KVQ (Chen et al., 2025)
239	- MixKVQ (arXiv 2512.19206, 2025)
240	- RateQuant (arXiv 2605.06675, 2026)
241	
242	### Related Work — Head Importance Heterogeneity
243	- HeadKV / "Not All Heads Matter" (Fu et al., ICLR 2025)
244	- AdaKV (Feng et al., NeurIPS 2025)
245	- KV-Compress (Rehg, 2024)
246	- PyramidKV (Cai et al., 2024)
247	
248	### Related Work — MCKP for Bit Allocation
249	- MPQCO (Chen et al., ICCV 2021)
250	
251	### Related Work — Outlier/Spike Patterns
252	- "Precision Where It Matters" (arXiv 2504.21553, 2025)
253	- CMPQ (Chen & Xie et al., 2024)
254	- MUXQ (arXiv 2604.04701, 2026)
255	
256	### Related Work — GQA
257	- GQA (Ainslie et al., EMNLP 2023)
258	- QCQA (2025)
259	
260	---
261	
262	## 10. Summary
263	
264	The spike vs spread distribution shape analysis is **novel**. While head-level heterogeneity is well-documented and exploited by multiple recent methods (RateQuant, HeadKV, AdaKV), no prior work has:
265	1. Analyzed the *shape* of sensitivity distributions (beyond scalar metrics like AM/GM)
266	2. Explained why MCKP/allocation-based methods fail for certain models
267	3. Shown that GQA ratio is a poor proxy for allocation benefit
268	4. Provided a predictive taxonomy (spike → negative returns, spread → positive returns)
269	
270	This positions our work as providing **diagnostic insight** that complements allocation methods like RateQuant, explaining their failure modes and suggesting when non-uniform allocation should (and should not) be applied.
271	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bcfa721e-f6b3-42c8-a564-5e72af107035",
  "isSidechain": false,
  "promptId": "964448b9-9407-4006-b5f8-3afa58950999",
  "type": "user",
  "uuid": "651f8c40-33cf-426a-9f8b-ec433c0e9050",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/artifacts/spike_vs_spread_literature.md",
      "content": "# Literature Survey: KV Cache Heterogeneity Distribution Shape (Spike vs Spread)\n\n**Date**: 2026-05-14\n**Context**: RateKV project — per-KV-head non-uniform bit-width allocation via constrained MCKP solver. Core finding: sensitivity heterogeneity distribution shape (spike vs spread) determines MCKP allocator effectiveness, not GQA ratio.\n\n---\n\n## 1. Direct Competitors (Per-Head Mixed-Precision KV Cache Quantization)\n\n### 1.1 RateQuant (2026)\n- **Title**: RateQuant: Optimal Mixed-Precision KV Cache Quantization via Rate-Distortion Theory\n- **Authors**: (arXiv:2605.06675)\n- **Venue**: arXiv preprint, May 2026\n- **Category**: **Direct competitor**\n- **Summary**: First to apply rate-distortion theory to per-head KV cache bit allocation. Uses reverse waterfilling for closed-form allocation. Fits per-quantizer distortion model D(b)=α·β^{-b}, with β varying 3.6–5.3 across quantizers. Key metric: AM/GM ratio of head sensitivities predicts achievable distortion reduction without any quantization. Gradient-based importance yields 1.07 PPL improvement over activation-based at 3.5 bits.\n- **Results**: On Qwen3-8B at 2.5 bits, reduces KIVI PPL from 49.3 to 14.9 (70% reduction). On TurboQuant at 4.0 bits, recovers 66% of quantization-induced degradation.\n- **Relation to our work**: **Closest competitor**. RateQuant uses AM/GM ratio as a scalar heterogeneity metric but does NOT analyze the distribution *shape* (spike vs spread). Their AM/GM captures heterogeneity magnitude, not whether it comes from one extreme outlier (spike) or a distributed cluster (spread). Our contribution: explaining *why* some models benefit from non-uniform allocation and others don't, through distribution shape analysis. RateQuant would predict benefit whenever AM/GM > 1 but cannot explain the Yi-1.5 failure case (high AM/GM from spike pattern, yet negative returns).\n\n### 1.2 KVTuner (2025)\n- **Title**: KVTuner: Sensitivity-Aware Layer-Wise Mixed-Precision KV Cache Quantization for Efficient and Nearly Lossless LLM Inference\n- **Authors**: Li et al.\n- **Venue**: ICML 2025\n- **Category**: **Direct competitor** (layer-level, not head-level)\n- **Summary**: Uses Pareto search over hardware-friendly layer-wise K/V precision pairs. Achieves nearly lossless 3.25-bit for Llama-3.1-8B, 4.0-bit for Qwen2.5-7B. Gradient-based sensitivity shows U-shaped pattern (early+late layers sensitive); activation-based is monotonically increasing.\n- **Relation to our work**: Operates at layer granularity, not head granularity. Does not analyze within-layer head heterogeneity distribution shape. Notes that Qwen2.5-7B requires higher precision → consistent with our finding of Qwen's spread pattern requiring differentiated allocation.\n\n### 1.3 PM-KVQ (2025)\n- **Title**: PM-KVQ: Progressive Mixed-Precision KV Cache Quantization for Long-CoT LLMs\n- **Authors**: Chen et al.\n- **Venue**: arXiv:2505.18610\n- **Category**: **Method component**\n- **Summary**: Progressive quantization strategy that gradually lowers bit-width over decoding steps. Block-wise memory allocation assigns higher bits to sensitive transformer blocks. Uses integer programming for allocation.\n- **Relation to our work**: Temporal dimension (progressive) is orthogonal to our spatial (per-head) analysis. Does not analyze head-level heterogeneity distribution shapes.\n\n### 1.4 MixKVQ (2025)\n- **Title**: MixKVQ: Query-Aware Mixed-Precision KV Cache Quantization for Long-Context Reasoning\n- **Authors**: (arXiv:2512.19206)\n- **Venue**: arXiv, Dec 2025\n- **Category**: **Method component**\n- **Summary**: Query-aware algorithm identifies critical key channels needing higher precision. Combines intrinsic quantization difficulty with query relevance. Per-channel mixed precision for keys, per-token for values.\n- **Relation to our work**: Operates at channel granularity within heads, not across heads. The \"intrinsic quantization difficulty\" concept relates to sensitivity heterogeneity but is measured per-channel, not per-head.\n\n### 1.5 KVmix (2025)\n- **Title**: KVmix: Gradient-Based Layer Importance-Aware Mixed-Precision Quantization for KV Cache\n- **Authors**: (arXiv:2506.08018; AAAI 2026)\n- **Venue**: AAAI 2026\n- **Category**: **Direct competitor** (layer-level)\n- **Summary**: Gradient-based importance analysis for layer-specific K/V bit-width allocation. Achieves K 2.19-bit / V 2.38-bit with 4.9× compression. Introduces dynamic long-context optimization for recent pivotal tokens.\n- **Relation to our work**: Layer-level, not head-level. Confirms K/V asymmetric sensitivity (consistent with our K/V separation findings).\n\n---\n\n## 2. Spike vs Spread / Outlier Pattern Analysis\n\n### 2.1 \"Precision Where It Matters\" — Spike-Aware Quantization (2025)\n- **Title**: Precision Where It Matters: A Novel Spike Aware Mixed-Precision Quantization Strategy for LLaMA-based Language Models\n- **Authors**: (arXiv:2504.21553)\n- **Venue**: Springer, April 2025\n- **Category**: **Background — spike pattern in activations (not heads)**\n- **Summary**: Identifies activation spikes concentrated in down projections of exactly 2 layers (one early, one late) in LLaMA. Spikes reach values up to 2500. Solution: FP8 for spiking layers, INT8 for rest. 30+ PPL reduction on LLaMA3-8B.\n- **Relation to our work**: Uses \"spike\" terminology for activation outliers, not head sensitivity distribution. The spike/spread dichotomy is analogous but operates at a different level (activation magnitude within layers vs. sensitivity distribution across heads). Supports the broader idea that spike-like concentration has different optimization implications than spread-like distributions.\n\n### 2.2 CMPQ — Channel-Wise Mixed-Precision Quantization (2024)\n- **Title**: Channel-Wise Mixed-Precision Quantization for Large Language Models\n- **Authors**: Chen & Xie et al.\n- **Venue**: arXiv:2410.13056, Oct 2024\n- **Category**: **Background — channel-level outlier patterns**\n- **Summary**: Allocates precision per-channel based on activation distribution. Distinguishes activation-based outliers (persistent in specific channels) from quantization-based outliers. ~0.5% of values are outliers. Uses L2-norm per channel for allocation.\n- **Relation to our work**: Channel-level analogue of our head-level analysis. The observation that outlier concentration varies by channel parallels our head-level spike vs spread finding, but at finer granularity and for weight/activation quantization, not KV cache.\n\n### 2.3 KITTY — Dynamic Channel-wise Precision Boost (2025)\n- **Title**: Kitty: Accurate and Efficient 2-bit KV Cache Quantization with Dynamic Channel-wise Precision Boost\n- **Authors**: (arXiv:2511.18643)\n- **Venue**: arXiv, Nov 2025\n- **Category**: **Method component**\n- **Summary**: Ranks Key-cache channels by sensitivity; keeps small fraction at higher precision. \"Critical channels play a disproportionately important role.\" Decomposes mixed-precision Key pages into two uniform 2-bit tensors for hardware efficiency.\n- **Relation to our work**: Channel-level analogue within keys. The finding that \"critical channels play disproportionately important roles\" is consistent with our heterogeneity thesis, but KITTY does not analyze whether the critical channel distribution is spike-like or spread-like.\n\n### 2.4 MUXQ — Low-Rank Outlier Decomposition (2026)\n- **Title**: MUXQ: Mixed-to-Uniform Precision Matrix Quantization via Low-Rank Outlier Decomposition\n- **Authors**: (arXiv:2604.04701)\n- **Venue**: arXiv, April 2026\n- **Category**: **Background**\n- **Summary**: Decomposes outlier channels into a low-rank matrix to convert mixed-precision quantization into uniform precision. Applies rotation/permutation to redistribute outlier energy.\n- **Relation to our work**: Addresses outliers via decomposition rather than differentiated allocation. Different philosophy: eliminate heterogeneity (smoothing) vs. exploit heterogeneity (our approach).\n\n---\n\n## 3. Head-Specific KV Cache Compression (Eviction-based, not Quantization)\n\n### 3.1 HeadKV / \"Not All Heads Matter\" (2024)\n- **Title**: Not All Heads Matter: A Head-Level KV Cache Compression Method with Integrated Retrieval and Reasoning\n- **Authors**: Fu et al.\n- **Venue**: ICLR 2025 (arXiv:2410.19258)\n- **Category**: **Background — head importance for eviction**\n- **Summary**: Head-level KV cache budget allocation based on importance scores from Needle-in-a-Haystack probing. Retains 1.5% KV cache with 97% performance. Different heads serve retrieval vs reasoning roles.\n- **Relation to our work**: Confirms head-level importance heterogeneity exists and is exploitable. Does not analyze the distribution shape of this heterogeneity. Eviction-based, not quantization-based.\n\n### 3.2 AdaKV (2024)\n- **Title**: Ada-KV: Optimizing KV Cache Eviction by Adaptive Budget Allocation\n- **Authors**: Feng et al.\n- **Venue**: NeurIPS 2025 (arXiv:2407.11550)\n- **Category**: **Background — adaptive head budget**\n- **Summary**: Adaptive per-head budget allocation for KV eviction. Extends SnapKV/PyramidKV with head-wise adaptive allocation. Key insight: uniform compression rate across heads is a \"rigidity\" that hurts performance.\n- **Relation to our work**: Directly supports our thesis that head-level heterogeneity matters. But AdaKV addresses eviction budgets (how many tokens to keep per head), not quantization bit-width. Does not analyze spike vs spread patterns.\n\n### 3.3 KV-Compress (2024)\n- **Title**: KV-Compress: Paged KV-Cache Compression with Variable Compression Rates per Attention Head\n- **Authors**: Rehg\n- **Venue**: arXiv:2410.00161, Oct 2024\n- **Category**: **Background — variable-rate per-head compression**\n- **Summary**: Variable compression rates across attention heads within PagedAttention framework. Proposes query-group-compression for GQA models yielding additional 4× compression. 8× compression with negligible impact on Llama-3.1.\n- **Relation to our work**: Confirms per-head heterogeneity is exploitable for compression. Addresses GQA grouping explicitly. Does not analyze why some heads/models benefit more (no spike vs spread analysis).\n\n### 3.4 PyramidKV (2024)\n- **Title**: PyramidKV: Dynamic KV Cache Compression based on Pyramidal Information Funneling\n- **Authors**: Cai et al.\n- **Venue**: arXiv:2406.02069\n- **Category**: **Background**\n- **Summary**: Attention scatters widely in lower layers, consolidates in higher layers → pyramidal budget allocation (more cache for lower layers). Layer-level, not head-level.\n- **Relation to our work**: Layer-level heterogeneity analysis. Complementary perspective but no head-level distribution shape analysis.\n\n---\n\n## 4. GQA Ratio and Quantization Sensitivity\n\n### 4.1 GQA Original Paper (2023)\n- **Title**: GQA: Training Generalized Multi-Query Transformer Models from Multi-Head Checkpoints\n- **Authors**: Ainslie et al.\n- **Venue**: EMNLP 2023 (arXiv:2305.13245)\n- **Category**: **Background**\n- **Summary**: Proposes GQA as interpolation between MHA and MQA. Does not discuss quantization sensitivity implications of GQA ratio.\n- **Relation to our work**: Foundational paper. Our finding that GQA ratio is NOT a reliable proxy for heterogeneity is novel — the original paper does not address this.\n\n### 4.2 QCQA — Quality-and-Capacity-Aware Grouping (2025)\n- **Title**: Quality- and Capacity-Aware Grouped Query Attention\n- **Venue**: 2025\n- **Category**: **Background — GQA grouping optimization**\n- **Summary**: Evolutionary algorithm to discover optimal query-head groupings that minimize accuracy loss under KV-cache constraints. Achieves 20% higher accuracy at equal cache size vs naive GQA, or 40% KV reduction at same accuracy.\n- **Relation to our work**: Addresses the grouping structure of GQA but not quantization. Supports the idea that the default GQA grouping may not be optimal, which is related to our finding about GQA ratio being a poor proxy.\n\n---\n\n## 5. MCKP / Constrained Optimization for Bit Allocation\n\n### 5.1 MPQCO (2021)\n- **Title**: Towards Mixed-Precision Quantization of Neural Networks via Constrained Optimization\n- **Authors**: Chen, Wang, Cheng\n- **Venue**: ICCV 2021\n- **Category**: **Method component — MCKP formulation origin**\n- **Summary**: Formulates mixed-precision quantization as MCKP. Uses second-order Taylor expansion + Hessian for sensitivity. Greedy solver. 5–10 min calibration. Principled and efficient.\n- **Relation to our work**: We use the same MCKP formulation. MPQCO applies it to weight quantization layer-wise; we apply it to KV cache head-wise. MPQCO does not analyze when MCKP allocation fails (i.e., no spike vs spread analysis).\n\n### 5.2 JointSQ (2024)\n- **Title**: JointSQ: Joint Sparsification-Quantization for Distributed Learning\n- **Authors**: Xie et al.\n- **Venue**: CVPR 2024\n- **Category**: **Background**\n- **Summary**: Joint sparsity-quantization optimization via MCKP where profit = -error, weight = storage.\n- **Relation to our work**: Uses MCKP but for sparsity+quantization jointly, not for KV cache head-level allocation.\n\n---\n\n## 6. Foundational KV Cache Quantization Methods\n\n### 6.1 KIVI (2024)\n- **Title**: KIVI: A Tuning-Free Asymmetric 2bit Quantization for KV Cache\n- **Authors**: Liu & Yuan et al.\n- **Venue**: ICML 2024 (arXiv:2402.02750)\n- **Category**: **Evaluation baseline**\n- **Summary**: Per-channel symmetric quantization for keys, per-token asymmetric for values. Tuning-free 2-bit. Establishes K/V asymmetry as important principle.\n- **Relation to our work**: Baseline quantizer. Our MCKP allocator can sit on top of KIVI. KIVI applies uniform bit-width — our work addresses its limitation.\n\n### 6.2 KVQuant (2024)\n- **Title**: KVQuant: Towards 10 Million Context Length LLM Inference with KV Cache Quantization\n- **Authors**: (arXiv:2401.18079)\n- **Venue**: NeurIPS 2024\n- **Category**: **Evaluation baseline**\n- **Summary**: Per-layer sensitivity-weighted non-uniform datatypes. Handles outlier channels. Extends to 3-bit and 2-bit from FlexGen's 4-bit.\n- **Relation to our work**: Layer-level non-uniform datatype design, not head-level bit allocation. Pioneered per-layer sensitivity analysis for KV cache.\n\n### 6.3 RotateKV (2025)\n- **Title**: RotateKV: Accurate and Robust 2-Bit KV Cache Quantization\n- **Venue**: IJCAI 2025\n- **Category**: **Evaluation baseline**\n- **Summary**: Outlier-aware rotation to enhance quantization adaptability across diverse outlier distributions.\n- **Relation to our work**: Smoothing-based approach (eliminate heterogeneity) vs our exploitation-based approach (allocate to heterogeneity).\n\n---\n\n## 7. Distribution Shape Metrics\n\n### 7.1 Mix-QViT — Layer Importance + Quantization Sensitivity (2025)\n- **Title**: Mix-QViT: Mixed-Precision Vision Transformer Quantization Driven by Layer Importance and Quantization Sensitivity\n- **Authors**: (arXiv:2501.06357)\n- **Venue**: arXiv, Jan 2025\n- **Category**: **Background — sensitivity metrics for ViTs**\n- **Summary**: Dual scoring: explainability-based layer importance (via LRP) + quantization sensitivity per layer. Uses these scores for mixed-precision allocation in Vision Transformers.\n- **Relation to our work**: Uses sensitivity metrics for allocation but does not analyze distribution shape. Applied to ViTs, not LLMs.\n\n### 7.2 Representational Compactness via Singular Values\n- **Category**: **Background — concentration metric**\n- **Summary**: Singular value distribution as a measure of information concentration: uniform SVs → high compactness (redundant); few dominant SVs → low compactness (concentrated/sensitive).\n- **Relation to our work**: SVD-based concentration measurement is related to our Gini/CV analysis of head sensitivity distributions. The \"few dominant SVs\" scenario parallels our \"spike\" pattern.\n\n---\n\n## 8. Novelty Assessment\n\n### What already exists:\n1. **Head-level heterogeneity is well-documented**: HeadKV, AdaKV, KV-Compress, RateQuant all confirm heads have varying importance\n2. **MCKP for mixed-precision allocation**: MPQCO (2021) established the formulation; RateQuant (2026) applies rate-distortion allocation to KV cache per-head\n3. **AM/GM ratio as heterogeneity scalar**: RateQuant proposes this as a predictor of allocation benefit\n4. **Spike-aware quantization for activations**: \"Precision Where It Matters\" addresses spike patterns in activation magnitudes\n\n### What is NOVEL in our work:\n1. **Distribution shape analysis (spike vs spread)**: No prior work explicitly analyzes how the *shape* of the head sensitivity distribution determines allocation effectiveness. RateQuant's AM/GM is a scalar that captures magnitude but not shape — two distributions with identical AM/GM can have very different shapes (one spike outlier vs distributed cluster)\n2. **GQA ratio ≠ heterogeneity proxy**: No prior work has shown that GQA ratio fails to predict allocation benefit. Yi-1.5-9B (highest GQA 8:1) with spike pattern yields negative returns despite high heterogeneity magnitude — this finding is absent from all surveyed papers\n3. **Failure mode characterization**: Prior work reports when mixed-precision helps; we characterize *when and why it fails* (spike pattern concentrates sensitivity in a single head that cannot be further differentiated by allocation)\n4. **Cross-model shape taxonomy**: Systematic classification of 5 models into spike/spread patterns with predictive power for MCKP effectiveness\n\n### Positioning relative to RateQuant:\nRateQuant is the closest competitor (same per-head granularity, similar MCKP-style allocation). Our contribution is **complementary and deeper**: RateQuant provides the allocation mechanism; we explain *when allocation mechanisms work*. RateQuant's AM/GM metric would incorrectly predict benefit for Yi-1.5-9B (high AM/GM from spike pattern). Our spike vs spread analysis provides a more informative predictor.\n\n---\n\n## 9. Papers to Cite (by section)\n\n### Related Work — KV Cache Quantization\n- KIVI (Liu & Yuan et al., ICML 2024)\n- KVQuant (NeurIPS 2024)\n- RotateKV (IJCAI 2025)\n- KITTY (arXiv 2511.18643, 2025)\n\n### Related Work — Mixed-Precision KV Cache\n- KVTuner (Li et al., ICML 2025)\n- KVmix (AAAI 2026)\n- PM-KVQ (Chen et al., 2025)\n- MixKVQ (arXiv 2512.19206, 2025)\n- RateQuant (arXiv 2605.06675, 2026)\n\n### Related Work — Head Importance Heterogeneity\n- HeadKV / \"Not All Heads Matter\" (Fu et al., ICLR 2025)\n- AdaKV (Feng et al., NeurIPS 2025)\n- KV-Compress (Rehg, 2024)\n- PyramidKV (Cai et al., 2024)\n\n### Related Work — MCKP for Bit Allocation\n- MPQCO (Chen et al., ICCV 2021)\n\n### Related Work — Outlier/Spike Patterns\n- \"Precision Where It Matters\" (arXiv 2504.21553, 2025)\n- CMPQ (Chen & Xie et al., 2024)\n- MUXQ (arXiv 2604.04701, 2026)\n\n### Related Work — GQA\n- GQA (Ainslie et al., EMNLP 2023)\n- QCQA (2025)\n\n---\n\n## 10. Summary\n\nThe spike vs spread distribution shape analysis is **novel**. While head-level heterogeneity is well-documented and exploited by multiple recent methods (RateQuant, HeadKV, AdaKV), no prior work has:\n1. Analyzed the *shape* of sensitivity distributions (beyond scalar metrics like AM/GM)\n2. Explained why MCKP/allocation-based methods fail for certain models\n3. Shown that GQA ratio is a poor proxy for allocation benefit\n4. Provided a predictive taxonomy (spike → negative returns, spread → positive returns)\n\nThis positions our work as providing **diagnostic insight** that complements allocation methods like RateQuant, explaining their failure modes and suggesting when non-uniform allocation should (and should not) be applied.\n",
      "numLines": 271,
      "startLine": 1,
      "totalLines": 271
    }
  },
  "sourceToolAssistantUUID": "bcfa721e-f6b3-42c8-a564-5e72af107035",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "0e163909-e397-4f29-9722-d542e29e1bd1",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-14T19:05:56.177Z_

<details open><summary>🔧 Tool call — Read · `toolu_019z7MaVDJzR6vDUomMXx2Jt`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/artifacts/spike_vs_spread_literature.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7228d464-278b-474c-9c4d-c3ff03df26df",
  "isSidechain": false,
  "requestId": "req_011Cb2z1rLm1qi1UH1BbKWfk",
  "type": "assistant",
  "uuid": "bcfa721e-f6b3-42c8-a564-5e72af107035",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "0e163909-e397-4f29-9722-d542e29e1bd1",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P5feUHLTE9ceaexEv4cCGM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 714,
      "cache_read_input_tokens": 23832,
      "output_tokens": 208,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 714,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 208,
          "cache_read_input_tokens": 23832,
          "cache_creation_input_tokens": 714,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 714
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
  "leafUuid": "651f8c40-33cf-426a-9f8b-ec433c0e9050",
  "sessionId": "0e163909-e397-4f29-9722-d542e29e1bd1"
}
```

---

### Runtime record

_source line 17_

```json
{
  "type": "ai-title",
  "aiTitle": "Update literature map with KV cache quantization papers",
  "sessionId": "0e163909-e397-4f29-9722-d542e29e1bd1"
}
```

---

### Assistant

_source line 18 · 2026-05-14T19:06:28.293Z_

<details><summary>Logged reasoning block</summary>

```text
Now I need to compare the existing literature_map.yaml with the papers mentioned in the survey report and the user's priority list. Let me identify what's already in the map and what needs to be added.

Already in literature_map.yaml:
1. **RateQuant** (zuo2026ratequant) ✓
2. **KVmix** (li2025kvmix) ✓
3. **MixKVQ** (zhang2025mixkvq) ✓


4. **KVTuner** (ICML 2025) — role: direct-competitor
5. **HeadKV** (ICLR 2025) — role: background
6. **AdaKV** (NeurIPS 2025) — role: background
7. **PM-KVQ** (2025) — role: method-component
8. **KITTY** (2025) — role: background
9. **MUXQ** (2026) — role: background

So it looks like all the papers from the survey are already in the map, including the ones from the user's priority list. I'm checking which of the nine papers the user requested are already in the map and which ones I need to add. Looking at the list, I see that RateQuant, KVmix, and MixKVQ are already present, so I need to add the remaining six: KVTuner, HeadKV, AdaKV, PM-KVQ, KITTY, and MUXQ. I'm also noting JointSQ as another paper to potentially include.

Now I'm organizing these six new papers into the appropriate clusters based on their focus areas—some fit into mixed-precision quantization, others into KV cache eviction or quantization strategies—and preparing to construct the YAML entries for each.

I notice the save_project_file tool has restrictions on which files it can write to, and literature_map.yaml isn't on the whitelist. Let me try using it anyway since that's what was requested, but I'm prepared to use the Write tool directly if needed.

Now I'm organizing the six new papers into their respective clusters—KVTuner and PM-KVQ go into the mixed-precision cluster, KITTY into KV cache quantization, HeadKV and AdaKV into the eviction cluster, and MUXQ into model compression—while updating the paper count from 35 to 41 and refreshing the timestamp. Rather than regenerating the entire file, I'll use targeted edits to add these entries safely.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "651f8c40-33cf-426a-9f8b-ec433c0e9050",
  "isSidechain": false,
  "requestId": "req_011Cb2z2GY3vWjsDvH597wJB",
  "type": "assistant",
  "uuid": "8028de55-26b1-439c-8e7d-42c0df8298fa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "0e163909-e397-4f29-9722-d542e29e1bd1",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011X9LQ4L1vYtDcnRxQTaoD2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18832,
      "cache_read_input_tokens": 24546,
      "output_tokens": 1600,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 18832,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1600,
          "cache_read_input_tokens": 24546,
          "cache_creation_input_tokens": 18832,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 18832
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

_source line 19 · 2026-05-14T19:06:28.376Z_

Already in the map: RateQuant, KVmix, MixKVQ. Need to add 6 papers: KVTuner, HeadKV, AdaKV, PM-KVQ, KITTY, MUXQ.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8028de55-26b1-439c-8e7d-42c0df8298fa",
  "isSidechain": false,
  "requestId": "req_011Cb2z2GY3vWjsDvH597wJB",
  "type": "assistant",
  "uuid": "a09a4596-7473-4236-a9e8-db33df48c7cb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "0e163909-e397-4f29-9722-d542e29e1bd1",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011X9LQ4L1vYtDcnRxQTaoD2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18832,
      "cache_read_input_tokens": 24546,
      "output_tokens": 1600,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 18832,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1600,
          "cache_read_input_tokens": 24546,
          "cache_creation_input_tokens": 18832,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 18832
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

_source line 20 · 2026-05-14T19:06:28.392Z_

<details open><summary>🔧 Tool call — Read · `toolu_012R7R7CEvkFeaMFiu9K3bHQ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/literature_map.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a09a4596-7473-4236-a9e8-db33df48c7cb",
  "isSidechain": false,
  "requestId": "req_011Cb2z2GY3vWjsDvH597wJB",
  "type": "assistant",
  "uuid": "c020d4be-267f-49cc-b475-b717f4100f40",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "0e163909-e397-4f29-9722-d542e29e1bd1",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011X9LQ4L1vYtDcnRxQTaoD2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18832,
      "cache_read_input_tokens": 24546,
      "output_tokens": 1600,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 18832,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1600,
          "cache_read_input_tokens": 24546,
          "cache_creation_input_tokens": 18832,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 18832
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

_source line 21 · 2026-05-14T19:06:28.785Z_

<details><summary>↩ Tool result · `toolu_012R7R7CEvkFeaMFiu9K3bHQ`</summary>

```text
1	meta:
2	  last_updated: '2026-05-14T10:30:00.000Z'
3	  total_papers: 35
4	categories:
5	  - Mixed-Precision Rate-Distortion
6	  - KV Cache Quantization
7	  - KV Cache Eviction
8	  - Model Compression
9	  - Attention Head Analysis
10	  - LLM Inference Efficiency
11	  - Evaluation Models
12	  - Theory
13	papers:
14	  # ============================================================
15	  # Cluster 1: Mixed-Precision R-D Allocation (5 papers)
16	  # ============================================================
17	  zuo2026ratequant:
18	    title: 'RateQuant: Optimal Mixed-Precision KV Cache Quantization via Rate-Distortion Theory'
19	    authors:
20	    - Fei Zuo
21	    - Zikang Zhou
22	    - Hao Cong
23	    - Xiaoyan Xi
24	    - Ho Fai Leung
25	    year: 2026
26	    venue: arXiv 2026
27	    url: ''
28	    doi: '2605.06675'
29	    bibtex_key: zuo2026ratequant
30	    category: Mixed-Precision Rate-Distortion
31	    role: direct-competitor
32	    relevance: 'Primary competitor: R-D optimal per-head KV cache bit allocation. Algorithm 1 (discrete greedy). Theorem 2 (continuous closed-form via reverse waterfilling). Proposition 6 (greedy optimality on consecutive integers). Key limitation: does not address hardware-aligned non-consecutive {2,4,8,16} where greedy may fail.'
33	    abstract: RateQuant fits a per-quantizer distortion model D(b)=alpha*beta^{-b} from a small calibration set, then solves the bit-allocation in closed form via reverse waterfilling from rate-distortion theory. On Qwen3-8B at 2.5 avg bits, calibrated RateQuant reduces KIVI perplexity from 49.3 to 14.9 (70% reduction). Calibration takes 1.6s on a single GPU with zero inference overhead.
34	    semantic_scholar_id: ''
35	    verified: true
36	    added_by: paper-research
37	    added_at: '2026-05-14T08:42:26.710Z'
38	  lei2026arkv:
39	    title: 'ARKV: Adaptive and Resource-Efficient KV Cache Management under Limited Memory Budget for Long-Context Inference in LLMs'
40	    authors:
41	    - Jianlong Lei
42	    - Shashikant Ilager
43	    year: 2026
44	    venue: arXiv 2026
45	    url: ''
46	    doi: '2603.08727'
47	    bibtex_key: lei2026arkv
48	    category: Mixed-Precision Rate-Distortion
49	    role: direct-competitor
50	    relevance: Adaptive mixed-precision KV cache with tri-state token assignment (Original/Quantization/Eviction). Per-layer OQ ratio estimation via attention entropy, variance, kurtosis. Alternative adaptive allocation strategy to our R-D formulation.
51	    abstract: 'ARKV dynamically allocates precision levels to cached tokens based on per-layer attention dynamics and token-level importance. Three components: per-layer OQ ratio estimation, token importance scoring, and tri-state cache assignment. Preserves ~97% baseline accuracy with 4x KV memory reduction.'
52	    semantic_scholar_id: ''
53	    verified: true
54	    added_by: paper-research
55	    added_at: '2026-05-14T08:42:26.710Z'
56	  li2025kvmix:
57	    title: 'KVmix: Gradient-Based Layer Importance-Aware Mixed-Precision Quantization for KV Cache'
58	    authors:
59	    - Fei Li
60	    - Song Liu
61	    - Weiguo Wu
62	    - Shiqiang Nie
63	    - Jinyu Wang
64	    year: 2025
65	    venue: arXiv 2025
66	    url: ''
67	    doi: '2506.08018'
68	    bibtex_key: li2025kvmix
69	    category: Mixed-Precision Rate-Distortion
70	    role: method-component
71	    relevance: Gradient-based importance for layer-wise KV cache bit-width allocation. Heuristic sensitivity-based approach vs our R-D optimal formulation. Achieves near-lossless at Key 2.19bit / Value 2.38bit.
72	    abstract: KVmix employs gradient-based importance analysis to evaluate how individual Key and Value projection matrices affect model loss, enabling layer-specific bit-width allocation. Includes dynamic long-context optimization preserving full-precision KV pairs for recent pivotal tokens.
73	    semantic_scholar_id: ''
74	    verified: true
75	    added_by: paper-research
76	    added_at: '2026-05-14T08:42:26.710Z'
77	  zhang2025mixkvq:
78	    title: 'MixKVQ: Query-Aware Mixed-Precision KV Cache Quantization for Long-Context Reasoning'
79	    authors:
80	    - Tao Zhang
81	    - Ziqian Zeng
82	    - Hao Peng
83	    - Huiping Zhuang
84	    - Cen Chen
85	    year: 2025
86	    venue: arXiv 2025
87	    url: ''
88	    doi: '2512.19206'
89	    bibtex_key: zhang2025mixkvq
90	    category: Mixed-Precision Rate-Distortion
91	    role: method-component
92	    relevance: 'Query-aware channel-level mixed-precision for KV cache. Orthogonal to our per-head R-D allocation: operates at channel granularity rather than head granularity.'
93	    abstract: MixKVQ introduces a lightweight query-aware algorithm to identify and preserve critical key channels at higher precision while applying per-token quantization for value cache. Outperforms existing low-bit methods on complex reasoning datasets.
94	    semantic_scholar_id: ''
95	    verified: true
96	    added_by: paper-research
97	    added_at: '2026-05-14T08:42:26.710Z'
98	  kim2024squeezellm:
99	    title: 'SqueezeLLM: Dense-and-Sparse Quantization'
100	    authors:
101	    - Sehoon Kim
102	    - Coleman Hooper
103	    - Amir Gholami
104	    - Zhen Dong
105	    - Xiuyu Li
106	    - Sheng Shen
107	    - Michael W. Mahoney
108	    - Kurt Keutzer
109	    year: 2024
110	    venue: ICML 2024
111	    url: ''
112	    doi: '2306.07629'
113	    bibtex_key: kim2024squeezellm
114	    category: Mixed-Precision Rate-Distortion
115	    role: foundation
116	    relevance: Foundational sensitivity-based non-uniform quantization using second-order information. Pioneered per-group precision assignment based on sensitivity—principle we extend to per-head KV cache R-D allocation.
117	    abstract: 'SqueezeLLM enables lossless compression to ultra-low 3-bit precision via two ideas: sensitivity-based non-uniform quantization searching for optimal bit precision assignment, and Dense-and-Sparse decomposition storing outliers in efficient sparse format.'
118	    semantic_scholar_id: ''
119	    verified: true
120	    added_by: paper-research
121	    added_at: '2026-05-14T08:42:26.710Z'
122	
123	  # ============================================================
124	  # Cluster 2: KV Cache Quantization (6 papers)
125	  # ============================================================
126	  liu2024kivi:
127	    title: 'KIVI: A Tuning-Free Asymmetric 2bit Quantization for KV Cache'
128	    authors:
129	    - Zirui Liu
130	    - Jiayi Yuan
131	    - Hongye Jin
132	    - Shaochen Zhong
133	    - Zhaozhuo Xu
134	    - Vladimir Braverman
135	    - Beidi Chen
136	    - Xia Hu
137	    year: 2024
138	    venue: ICML 2024
139	    url: ''
140	    doi: '2402.02750'
141	    bibtex_key: liu2024kivi
142	    category: KV Cache Quantization
143	    role: direct-competitor
144	    relevance: Asymmetric per-channel key / per-token value 2-bit KV cache quantization; tuning-free baseline for mixed-precision KV cache methods
145	    abstract: We conduct a comprehensive study on the element distribution in KV cache of popular LLMs and find that the key cache should be quantized per-channel while the value cache should be quantized per-token. From this observation, we develop a tuning-free 2bit KV cache quantization algorithm named KIVI.
146	    semantic_scholar_id: ''
147	    verified: true
148	    added_by: paper-research
149	    added_at: '2026-05-14T07:56:45.265Z'
150	  hooper2024kvquant:
151	    title: 'KVQuant: Towards 10 Million Context Length LLM Inference with KV Cache Quantization'
152	    authors:
153	    - Coleman Hooper
154	    - Sehoon Kim
155	    - Hiva Mohammadzadeh
156	    - Michael W. Mahoney
157	    - Yakun Sophia Shao
158	    - Kurt Keutzer
159	    - Amir Gholami
160	    year: 2024
161	    venue: NeurIPS 2024
162	    url: ''
163	    doi: '2401.18079'
164	    bibtex_key: hooper2024kvquant
165	    category: KV Cache Quantization
166	    role: direct-competitor
167	    relevance: Per-channel key quantization with pre-RoPE, non-uniform datatypes, and dense-and-sparse outlier handling; achieves sub-4-bit KV cache for 10M context
168	    abstract: KV cache activations are the dominant contributor to memory consumption during LLM inference for large context windows. We address this with per-channel key quantization, pre-RoPE key quantization, non-uniform KV cache quantization, and per-vector dense-and-sparse quantization to isolate outliers.
169	    semantic_scholar_id: ''
170	    verified: true
171	    added_by: paper-research
172	    added_at: '2026-05-14T07:56:45.265Z'
173	  lin2024qserve:
174	    title: 'QServe: W4A8KV4 Quantization and System Co-design for Efficient LLM Serving'
175	    authors:
176	    - Yujun Lin
177	    - Haotian Tang
178	    - Shang Yang
179	    - Zhekai Zhang
180	    - Guangxuan Xiao
181	    - Chuang Gan
182	    - Song Han
183	    year: 2024
184	    venue: MLSys 2025
185	    url: ''
186	    doi: '2405.04532'
187	    bibtex_key: lin2024qserve
188	    category: KV Cache Quantization
189	    role: foundation
190	    relevance: W4A8KV4 co-design with SmoothAttention for KV4 quantization; demonstrates system-level gains from joint weight-activation-KV quantization
191	    abstract: QServe introduces QoQ (W4A8KV4), a quantization algorithm with 4-bit weight, 8-bit activation, and 4-bit KV cache. Progressive group quantization ensures all GEMMs run on INT8 tensor cores. SmoothAttention shifts quantization difficulty from keys to queries.
192	    semantic_scholar_id: ''
193	    verified: true
194	    added_by: paper-research
195	    added_at: '2026-05-14T07:56:45.265Z'
196	  he2024zipcache:
197	    title: 'ZipCache: Accurate and Efficient KV Cache Quantization with Salient Token Identification'
198	    authors:
199	    - Yefei He
200	    - Luoming Zhang
201	    - Weijia Wu
202	    - Jing Liu
203	    - Hong Zhou
204	    - Bohan Zhuang
205	    year: 2024
206	    venue: NeurIPS 2024
207	    url: ''
208	    doi: '2405.14256'
209	    bibtex_key: he2024zipcache
210	    category: KV Cache Quantization
211	    role: direct-competitor
212	    relevance: Channel-separable tokenwise quantization with adaptive bit-width based on normalized attention score saliency; mixed-precision KV cache baseline
213	    abstract: ZipCache proposes channel-separable tokenwise quantization and uses normalized attention score for identifying salient tokens with adaptive bit-width assignment. Achieves 4.98x compression on Mistral-7B with 0.38% accuracy drop.
214	    semantic_scholar_id: ''
215	    verified: true
216	    added_by: paper-research
217	    added_at: '2026-05-14T07:56:45.265Z'
218	  kang2024gear:
219	    title: 'GEAR: An Efficient KV Cache Compression Recipe for Near-Lossless Generative Inference of LLM'
220	    authors:
221	    - Hao Kang
222	    - Qingru Zhang
223	    - Souvik Kundu
224	    - Geonhwa Jeong
225	    - Zaoxing Liu
226	    - Tushar Krishna
227	    - Tuo Zhao
228	    year: 2024
229	    venue: arXiv 2024
230	    url: ''
231	    doi: '2403.05527'
232	    bibtex_key: kang2024gear
233	    category: KV Cache Quantization
234	    role: direct-competitor
235	    relevance: Hybrid quantization + low-rank + sparse error correction for KV cache; demonstrates that residual compensation improves ultra-low-bit quantization quality
236	    abstract: GEAR first applies quantization to majority of entries to ultra-low precision, then employs a low rank matrix to approximate the quantization error, and a sparse matrix to remedy individual errors from outlier entries. Achieves near-lossless 4-bit compression with 2.38x throughput improvement.
237	    semantic_scholar_id: ''
238	    verified: true
239	    added_by: paper-research
240	    added_at: '2026-05-14T07:56:45.265Z'
241	  duanmu2024skvq:
242	    title: 'SKVQ: Sliding-window Key and Value Cache Quantization for Large Language Models'
243	    authors:
244	    - Haojie Duanmu
245	    - Zhihang Yuan
246	    - Xiuhong Li
247	    - Jiangfei Duan
248	    - Xingcheng Zhang
249	    - Dahua Lin
250	    year: 2024
251	    venue: arXiv 2024
252	    url: ''
253	    doi: '2405.06219'
254	    bibtex_key: duanmu2024skvq
255	    category: KV Cache Quantization
256	    role: direct-competitor
257	    relevance: Channel rearrangement + sliding-window high-precision recent tokens; achieves 2-bit key / 1.5-bit value with minimal accuracy loss
258	    abstract: SKVQ rearranges KV cache channels to improve similarity within quantization groups and applies clipped dynamic quantization at group level. Preserves recent window tokens at high precision. Enables 2-bit keys and 1.5-bit values with up to 1M context on 80GB GPU.
259	    semantic_scholar_id: ''
260	    verified: true
261	    added_by: paper-research
262	    added_at: '2026-05-14T07:56:45.265Z'
263	
264	  # ============================================================
265	  # Cluster 3: KV Cache Eviction (6 papers)
266	  # ============================================================
267	  zhang2023h2o:
268	    title: 'H2O: Heavy-Hitter Oracle for Efficient Generative Inference of Large Language Models'
269	    authors:
270	    - Zhenyu Zhang
271	    - Ying Sheng
272	    - Tianyi Zhou
273	    - Tianlong Chen
274	    - Lianmin Zheng
275	    - Ruisi Cai
276	    - Zhao Song
277	    - Yuandong Tian
278	    - Christopher Re
279	    - Clark Barrett
280	    - Zhangyang Wang
281	    - Beidi Chen
282	    year: 2023
283	    venue: NeurIPS 2023
284	    url: ''
285	    doi: 10.48550/arXiv.2306.14048
286	    bibtex_key: zhang2023h2o
287	    category: KV Cache Eviction
288	    role: background
289	    relevance: Foundational KV cache eviction policy based on heavy-hitter tokens; orthogonal to our quantization approach
290	    abstract: H2O identifies Heavy Hitters — a small set of tokens contributing most to attention scores — and dynamically retains recent and H2 tokens. With 20% heavy hitters, H2O improves throughput by up to 29x and reduces KV cache memory by up to 5x.
291	    semantic_scholar_id: ''
292	    verified: true
293	    added_by: paper-research
294	    added_at: '2026-05-14T08:10:15.562Z'
295	  li2024snapkv:
296	    title: 'SnapKV: LLM Knows What You are Looking for Before Generation'
297	    authors:
298	    - Yuhong Li
299	    - Yingbing Huang
300	    - Bowen Yang
301	    - Bharat Venkitesh
302	    - Acyr Locatelli
303	    - Hanchen Ye
304	    - Tianle Cai
305	    - Patrick Lewis
306	    - Deming Chen
307	    year: 2024
308	    venue: NeurIPS 2024
309	    url: ''
310	    doi: 10.48550/arXiv.2404.14469
311	    bibtex_key: li2024snapkv
312	    category: KV Cache Eviction
313	    role: background
314	    relevance: Observation-driven KV cache compression using attention pattern consistency; competes with eviction-based approaches our work compares against
315	    abstract: SnapKV efficiently minimizes KV cache size by selecting clustered important KV positions per attention head using an observation window at the end of the prompt. Achieves 3.6x speed increase and 8.2x memory efficiency at 16K tokens.
316	    semantic_scholar_id: ''
317	    verified: true
318	    added_by: paper-research
319	    added_at: '2026-05-14T08:10:15.562Z'
320	  ge2024fastgen:
321	    title: 'Model Tells You What to Discard: Adaptive KV Cache Compression for LLMs'
322	    authors:
323	    - Suyu Ge
324	    - Yunan Zhang
325	    - Liyuan Liu
326	    - Minjia Zhang
327	    - Jiawei Han
328	    - Jianfeng Gao
329	    year: 2024
330	    venue: ICLR 2024
331	    url: ''
332	    doi: 10.48550/arXiv.2310.01801
333	    bibtex_key: ge2024fastgen
334	    category: KV Cache Eviction
335	    role: background
336	    relevance: Adaptive per-head eviction strategy (FastGen); demonstrates head-specific compression is beneficial, complementary to quantization
337	    abstract: 'FastGen constructs KV cache adaptively per attention head: evicting long-range contexts on local-attention heads, discarding non-special tokens on special-token-focused heads, and using standard KV cache for broad-attention heads. Reduces memory by 50% without sacrificing quality.'
338	    semantic_scholar_id: ''
339	    verified: true
340	    added_by: paper-research
341	    added_at: '2026-05-14T08:10:15.562Z'
342	  xiao2024streamingllm:
343	    title: Efficient Streaming Language Models with Attention Sinks
344	    authors:
345	    - Guangxuan Xiao
346	    - Yuandong Tian
347	    - Beidi Chen
348	    - Song Han
349	    - Mike Lewis
350	    year: 2024
351	    venue: ICLR 2024
352	    url: ''
353	    doi: 10.48550/arXiv.2309.17453
354	    bibtex_key: xiao2024streamingllm
355	    category: KV Cache Eviction
356	    role: background
357	    relevance: Discovers attention sink phenomenon in initial tokens; motivates why naive eviction can fail and informs our quantization-first approach
358	    abstract: StreamingLLM enables LLMs to generalize to infinite sequence lengths without fine-tuning by retaining attention sink tokens alongside a sliding window of recent tokens. Achieves up to 22.2x speedup over sliding window recomputation.
359	    semantic_scholar_id: ''
360	    verified: true
361	    added_by: paper-research
362	    added_at: '2026-05-14T08:10:15.562Z'
363	  liu2024scissorhands:
364	    title: 'Scissorhands: Exploiting the Persistence of Importance Hypothesis for LLM KV Cache Compression at Test Time'
365	    authors:
366	    - Zichang Liu
367	    - Aditya Desai
368	    - Fangshuo Liao
369	    - Weitao Wang
370	    - Victor Xie
371	    - Zhaozhuo Xu
372	    - Anastasios Kyrillidis
373	    - Anshumali Shrivastava
374	    year: 2024
375	    venue: NeurIPS 2023
376	    url: ''
377	    doi: 10.48550/arXiv.2305.17118
378	    bibtex_key: liu2024scissorhands
379	    category: KV Cache Eviction
380	    role: background
381	    relevance: Persistence-of-importance hypothesis for KV cache eviction; achieves 5x cache reduction, combinable with 4-bit quantization for 20x compression
382	    abstract: Scissorhands maintains KV cache at a fixed budget by storing pivotal tokens with higher probability, achieving up to 5x memory reduction without quality loss, and up to 20x when combined with 4-bit quantization.
383	    semantic_scholar_id: ''
384	    verified: true
385	    added_by: paper-research
386	    added_at: '2026-05-14T08:10:15.562Z'
387	  yang2024pyramidinfer:
388	    title: 'PyramidInfer: Pyramid KV Cache Compression for High-throughput LLM Inference'
389	    authors:
390	    - Dongjie Yang
391	    - Xiaodong Han
392	    - Yan Gao
393	    - Yao Hu
394	    - Shilin Zhang
395	    - Hai Zhao
396	    year: 2024
397	    venue: Findings of ACL 2024
398	    url: ''
399	    doi: 10.48550/arXiv.2405.12532
400	    bibtex_key: yang2024pyramidinfer
401	    category: KV Cache Eviction
402	    role: background
403	    relevance: Layer-wise pyramid compression exploiting inter-layer dependency; crucial KV count decreases across layers, relevant to our per-layer rate allocation
404	    abstract: PyramidInfer compresses KV cache by layer-wise retaining crucial context, exploiting the finding that crucial keys and values decrease layer by layer. Achieves 2.2x throughput improvement with 54% GPU memory reduction.
405	    semantic_scholar_id: ''
406	    verified: true
407	    added_by: paper-research
408	    added_at: '2026-05-14T08:10:15.562Z'
409	
410	  # ============================================================
411	  # Cluster 4: Model Compression (6 papers)
412	  # ============================================================
413	  frantar2023gptq:
414	    title: 'GPTQ: Accurate Post-Training Quantization for Generative Pre-trained Transformers'
415	    authors:
416	    - Elias Frantar
417	    - Saleh Ashkboos
418	    - Torsten Hoefler
419	    - Dan Alistarh
420	    year: 2023
421	    venue: ICLR 2023
422	    url: ''
423	    doi: '2210.17323'
424	    bibtex_key: frantar2023gptq
425	    category: Model Compression
426	    role: foundation
427	    relevance: Foundational one-shot weight quantization based on approximate second-order information (OBQ). Reduces bitwidth to 3-4 bits per weight with negligible accuracy degradation. Established post-training quantization paradigm for LLMs.
428	    abstract: GPTQ is a one-shot weight quantization method based on approximate second-order information that can quantize GPT models with 175 billion parameters in approximately four GPU hours, reducing bitwidth to 3 or 4 bits per weight with negligible accuracy degradation.
429	    semantic_scholar_id: ''
430	    verified: true
431	    added_by: literature-survey
432	    added_at: '2026-05-14T10:30:00.000Z'
433	  lin2024awq:
434	    title: 'AWQ: Activation-aware Weight Quantization for LLM Compression and Acceleration'
435	    authors:
436	    - Ji Lin
437	    - Jiaming Tang
438	    - Haotian Tang
439	    - Shang Yang
440	    - Wei-Ming Chen
441	    - Wei-Chen Wang
442	    - Guangxuan Xiao
443	    - Xingyu Dang
444	    - Chuang Gan
445	    - Song Han
446	    year: 2024
447	    venue: MLSys 2024 (Best Paper)
448	    url: ''
449	    doi: '2306.00978'
450	    bibtex_key: lin2024awq
451	    category: Model Compression
452	    role: foundation
453	    relevance: Activation-aware salient weight protection via equivalent scaling transformation. Demonstrates that 1% salient weights dominate quantization quality—analogous to our finding that per-head sensitivity varies drastically.
454	    abstract: AWQ finds that protecting only 1% salient weights (identified by activation distribution, not weights) greatly reduces quantization error. Scales salient channels via mathematically equivalent transformation. No backpropagation or reconstruction needed. 3x speedup over FP16.
455	    semantic_scholar_id: ''
456	    verified: true
457	    added_by: literature-survey
458	    added_at: '2026-05-14T10:30:00.000Z'
459	  xiao2023smoothquant:
460	    title: 'SmoothQuant: Accurate and Efficient Post-Training Quantization for Large Language Models'
461	    authors:
462	    - Guangxuan Xiao
463	    - Ji Lin
464	    - Mickael Seznec
465	    - Hao Wu
466	    - Julien Demouth
467	    - Song Han
468	    year: 2023
469	    venue: ICML 2023
470	    url: ''
471	    doi: '2211.10438'
472	    bibtex_key: xiao2023smoothquant
473	    category: Model Compression
474	    role: foundation
475	    relevance: Smooths activation outliers by migrating quantization difficulty from activations to weights. Enables W8A8 for all matmuls in LLMs. QServe's SmoothAttention extends this idea to KV cache.
476	    abstract: SmoothQuant enables INT8 quantization of both weights and activations for all matrix multiplications in LLMs by smoothing activation outliers via offline migration of quantization difficulty from activations to weights. Up to 1.56x speedup and 2x memory reduction with negligible accuracy loss.
477	    semantic_scholar_id: ''
478	    verified: true
479	    added_by: literature-survey
480	    added_at: '2026-05-14T10:30:00.000Z'
481	  dettmers2022llmint8:
482	    title: 'LLM.int8(): 8-bit Matrix Multiplication for Transformers at Scale'
483	    authors:
484	    - Tim Dettmers
485	    - Mike Lewis
486	    - Younes Belkada
487	    - Luke Zettlemoyer
488	    year: 2022
489	    venue: NeurIPS 2022
490	    url: ''
491	    doi: '2208.07339'
492	    bibtex_key: dettmers2022llmint8
493	    category: Model Compression
494	    role: foundation
495	    relevance: First to identify emergent outlier features in transformers that dominate quantization quality. Mixed-precision decomposition (0.1% in FP16, 99.9% in INT8) is conceptually related to our per-head mixed-precision allocation.
496	    abstract: LLM.int8() develops Int8 matrix multiplication for feed-forward and attention projection layers via absmax vector-wise quantization and mixed precision decomposition. Cuts inference memory by half while retaining full precision performance for 175B-parameter models.
497	    semantic_scholar_id: ''
498	    verified: true
499	    added_by: literature-survey
500	    added_at: '2026-05-14T10:30:00.000Z'
501	  tseng2024quipsharp:
502	    title: 'QuIP#: Even Better LLM Quantization with Hadamard Incoherence and Lattice Codebooks'
503	    authors:
504	    - Albert Tseng
505	    - Jerry Chee
506	    - Qingyao Sun
507	    - Volodymyr Kuleshov
508	    - Christopher De Sa
509	    year: 2024
510	    venue: ICML 2024
511	    url: ''
512	    doi: '2402.04396'
513	    bibtex_key: tseng2024quipsharp
514	    category: Model Compression
515	    role: foundation
516	    relevance: State-of-the-art extreme compression (2-bit weights) via Hadamard incoherence processing and E8 lattice codebooks. Theoretical grounding for why incoherent distributions quantize better—relevant to understanding per-head distortion variation.
517	    abstract: QuIP# achieves state-of-the-art in extreme weight compression using randomized Hadamard transform for incoherence processing, E8 lattice codebooks for vector quantization of sub-Gaussian incoherent weights, and fine-tuning for fidelity. Hardware-efficient implementation.
518	    semantic_scholar_id: ''
519	    verified: true
520	    added_by: literature-survey
521	    added_at: '2026-05-14T10:30:00.000Z'
522	  zhao2024atom:
523	    title: 'Atom: Low-bit Quantization for Efficient and Accurate LLM Serving'
524	    authors:
525	    - Yilong Zhao
526	    - Chien-Yu Lin
527	    - Kan Zhu
528	    - Zihao Ye
529	    - Lequn Chen
530	    - Size Zheng
531	    - Luis Ceze
532	    - Arvind Krishnamurthy
533	    - Tianqi Chen
534	    - Baris Kasikci
535	    year: 2024
536	    venue: MLSys 2024
537	    url: ''
538	    doi: '2310.19102'
539	    bibtex_key: zhao2024atom
540	    category: Model Compression
541	    role: foundation
542	    relevance: End-to-end low-bit quantization for serving with mixed-precision, group quantization, and KV cache quantization. Demonstrates system-level throughput gains (3.5x over FP16) from co-designed quantization kernels.
543	    abstract: Atom combines mixed-precision quantization retaining salient activations/weights in high precision, fine-grained group quantization, dynamic activation quantization, KV-cache quantization, and efficient CUDA kernels. Achieves 7.73x throughput over FP16 baseline.
544	    semantic_scholar_id: ''
545	    verified: true
546	    added_by: literature-survey
547	    added_at: '2026-05-14T10:30:00.000Z'
548	
549	  # ============================================================
550	  # Cluster 5: Attention Head Analysis (4 papers)
551	  # ============================================================
552	  voita2019heads:
553	    title: 'Analyzing Multi-Head Self-Attention: Specialized Heads Do the Heavy Lifting, the Rest Can Be Pruned'
554	    authors:
555	    - Elena Voita
556	    - David Talbot
557	    - Fedor Moiseev
558	    - Rico Sennrich
559	    - Ivan Titov
560	    year: 2019
561	    venue: ACL 2019
562	    url: ''
563	    doi: '1905.09418'
564	    bibtex_key: voita2019heads
565	    category: Attention Head Analysis
566	    role: foundation
567	    relevance: Foundational work on attention head specialization and pruning. Shows most heads can be pruned (38/48 with only 0.15 BLEU drop). Motivates our per-head heterogeneous quantization—heads have different importance and roles.
568	    abstract: Evaluates individual attention head contributions and identifies specialized heads playing consistent linguistically-interpretable roles. Using stochastic gates with L0 penalty, the vast majority of heads can be pruned without seriously affecting performance.
569	    semantic_scholar_id: ''
570	    verified: true
571	    added_by: literature-survey
572	    added_at: '2026-05-14T10:30:00.000Z'
573	  michel2019sixteen:
574	    title: Are Sixteen Heads Really Better than One?
575	    authors:
576	    - Paul Michel
577	    - Omer Levy
578	    - Graham Neubig
579	    year: 2019
580	    venue: NeurIPS 2019
581	    url: ''
582	    doi: '1905.10650'
583	    bibtex_key: michel2019sixteen
584	    category: Attention Head Analysis
585	    role: foundation
586	    relevance: Shows large proportion of attention heads can be removed at test time. Greedy pruning analysis reveals varying head importance. Directly supports our premise that heads deserve different quantization precision.
587	    abstract: A large proportion of attention heads can be removed at test time without significantly impacting performance, and some layers can be reduced to a single head. Self-attention layers can be significantly pruned while encoder-decoder layers are more dependent on multi-headedness.
588	    semantic_scholar_id: ''
589	    verified: true
590	    added_by: literature-survey
591	    added_at: '2026-05-14T10:30:00.000Z'
592	  clark2019bert:
593	    title: What Does BERT Look At? An Analysis of BERT's Attention
594	    authors:
595	    - Kevin Clark
596	    - Urvashi Khandelwal
597	    - Omer Levy
598	    - Christopher D. Manning
599	    year: 2019
600	    venue: ACL Workshop BlackboxNLP 2019
601	    url: ''
602	    doi: '1906.04341'
603	    bibtex_key: clark2019bert
604	    category: Attention Head Analysis
605	    role: background
606	    relevance: Characterizes attention head behavior patterns (delimiter tokens, positional offsets, broad attention). Shows heads in same layer often exhibit similar behaviors—relevant to understanding GQA group structure.
607	    abstract: Proposes methods for analyzing attention mechanisms of pre-trained models. Finds BERT heads exhibit patterns like attending to delimiter tokens, positional offsets, or broadly over sentences. Certain heads correspond to syntactic and coreference relations with high accuracy.
608	    semantic_scholar_id: ''
609	    verified: true
610	    added_by: literature-survey
611	    added_at: '2026-05-14T10:30:00.000Z'
612	  ainslie2023gqa:
613	    title: 'GQA: Training Generalized Multi-Query Transformer Models from Multi-Head Checkpoints'
614	    authors:
615	    - Joshua Ainslie
616	    - James Lee-Thorp
617	    - Michiel de Jong
618	    - Yury Zemlyanskiy
619	    - Federico Lebron
620	    - Sumit Sanghai
621	    year: 2023
622	    venue: EMNLP 2023
623	    url: ''
624	    doi: '2305.13245'
625	    bibtex_key: ainslie2023gqa
626	    category: Attention Head Analysis
627	    role: foundation
628	    relevance: Defines grouped-query attention (GQA) which is the architecture used by all three models we evaluate (Qwen2.5 7:1, Llama-3.1 4:1, Mistral 4:1). GQA group ratio directly affects our per-head allocation granularity and results.
629	    abstract: Proposes grouped-query attention (GQA), a generalization of multi-query attention using an intermediate number of key-value heads. Uptrained GQA achieves quality close to multi-head attention with comparable speed to MQA. Provides recipe for uptraining existing MHA checkpoints.
630	    semantic_scholar_id: ''
631	    verified: true
632	    added_by: literature-survey
633	    added_at: '2026-05-14T10:30:00.000Z'
634	
635	  # ============================================================
636	  # Cluster 6: LLM Inference Efficiency (4 papers)
637	  # ============================================================
638	  kwon2023vllm:
639	    title: Efficient Memory Management for Large Language Model Serving with PagedAttention
640	    authors:
641	    - Woosuk Kwon
642	    - Zhuohan Li
643	    - Siyuan Zhuang
644	    - Ying Sheng
645	    - Lianmin Zheng
646	    - Cody Hao Yu
647	    - Joseph E. Gonzalez
648	    - Hao Zhang
649	    - Ion Stoica
650	    year: 2023
651	    venue: SOSP 2023
652	    url: ''
653	    doi: '2309.06180'
654	    bibtex_key: kwon2023vllm
655	    category: LLM Inference Efficiency
656	    role: background
657	    relevance: PagedAttention enables non-contiguous KV cache storage, reducing memory waste. Our per-head mixed-precision allocation is complementary—can be applied within vLLM's paged memory management.
658	    abstract: vLLM proposes PagedAttention inspired by virtual memory paging, achieving near-zero waste in KV cache memory and flexible sharing within and across requests. 2-4x throughput improvement over state-of-the-art systems.
659	    semantic_scholar_id: ''
660	    verified: true
661	    added_by: literature-survey
662	    added_at: '2026-05-14T10:30:00.000Z'
663	  dao2022flashattention:
664	    title: 'FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness'
665	    authors:
666	    - Tri Dao
667	    - Daniel Y. Fu
668	    - Stefano Ermon
669	    - Atri Rudra
670	    - Christopher Re
671	    year: 2022
672	    venue: NeurIPS 2022
673	    url: ''
674	    doi: '2205.14135'
675	    bibtex_key: dao2022flashattention
676	    category: LLM Inference Efficiency
677	    role: background
678	    relevance: IO-aware tiling for exact attention. Our quantized KV cache reduces HBM reads during attention, providing complementary gains to FlashAttention's tiling strategy.
679	    abstract: FlashAttention uses tiling to reduce memory reads/writes between GPU HBM and SRAM. 15% speedup on BERT-large, 3x on GPT-2, 2.4x on long-range arena, without approximation.
680	    semantic_scholar_id: ''
681	    verified: true
682	    added_by: literature-survey
683	    added_at: '2026-05-14T10:30:00.000Z'
684	  shazeer2019mqa:
685	    title: 'Fast Transformer Decoding: One Write-Head is All You Need'
686	    authors:
687	    - Noam Shazeer
688	    year: 2019
689	    venue: arXiv 2019
690	    url: ''
691	    doi: '1911.02150'
692	    bibtex_key: shazeer2019mqa
693	    category: LLM Inference Efficiency
694	    role: foundation
695	    relevance: Introduces multi-query attention (MQA) sharing a single KV head across all query heads. GQA generalizes MQA. Our per-head allocation exploits the remaining KV head heterogeneity in GQA models.
696	    abstract: Proposes multi-query attention where keys and values are shared across all attention heads, greatly reducing KV cache size and memory bandwidth requirements of incremental decoding. Much faster decoding with minor quality degradation.
697	    semantic_scholar_id: ''
698	    verified: true
699	    added_by: literature-survey
700	    added_at: '2026-05-14T10:30:00.000Z'
701	  deepseek2024v2:
702	    title: 'DeepSeek-V2: A Strong, Economical, and Efficient Mixture-of-Experts Language Model'
703	    authors:
704	    - DeepSeek-AI
705	    year: 2024
706	    venue: arXiv 2024
707	    url: ''
708	    doi: '2405.04434'
709	    bibtex_key: deepseek2024v2
710	    category: LLM Inference Efficiency
711	    role: background
712	    relevance: Introduces Multi-head Latent Attention (MLA) compressing KV cache into low-rank latent vectors (93.3% reduction). Alternative architectural approach to KV cache reduction vs our post-training quantization.
713	    abstract: DeepSeek-V2 uses Multi-head Latent Attention (MLA) compressing KV caches into latent vectors and DeepSeekMoE for sparse computation. 236B total parameters, 21B activated per token. 42.5% training cost reduction, 93.3% KV cache reduction, 5.76x throughput increase vs DeepSeek 67B.
714	    semantic_scholar_id: ''
715	    verified: true
716	    added_by: literature-survey
717	    added_at: '2026-05-14T10:30:00.000Z'
718	
719	  # ============================================================
720	  # Cluster 7: Evaluation Models (3 papers)
721	  # ============================================================
722	  grattafiori2024llama3:
723	    title: The Llama 3 Herd of Models
724	    authors:
725	    - Aaron Grattafiori
726	    - et al.
727	    year: 2024
728	    venue: arXiv 2024
729	    url: ''
730	    doi: '2407.21783'
731	    bibtex_key: grattafiori2024llama3
732	    category: Evaluation Models
733	    role: evaluation
734	    relevance: Llama-3.1-8B is one of three evaluation models. GQA with 4:1 ratio (8 KV heads, 32 query heads). Marginal gains from per-head allocation in our experiments.
735	    abstract: Llama 3 is a herd of foundation models natively supporting multilinguality, coding, reasoning, and tool usage. Dense Transformer up to 405B parameters with 128K context. Comparable quality to GPT-4.
736	    semantic_scholar_id: ''
737	    verified: true
738	    added_by: literature-survey
739	    added_at: '2026-05-14T10:30:00.000Z'
740	  yang2025qwen25:
741	    title: Qwen2.5 Technical Report
742	    authors:
743	    - An Yang
744	    - et al.
745	    year: 2025
746	    venue: arXiv 2024
747	    url: ''
748	    doi: '2412.15115'
749	    bibtex_key: yang2025qwen25
750	    category: Evaluation Models
751	    role: evaluation
752	    relevance: Qwen2.5-7B is our strongest-result model. GQA with 7:1 ratio (4 KV heads, 28 query heads)—highest heterogeneity among tested models, yielding 29.3% PPL improvement from per-head allocation.
753	    abstract: Qwen2.5 is a comprehensive LLM series with improvements in pre-training (18T tokens) and post-training. Qwen2.5-72B-Instruct outperforms many open and proprietary models, competitive with Llama-3-405B-Instruct at 5x smaller size.
754	    semantic_scholar_id: ''
755	    verified: true
756	    added_by: literature-survey
757	    added_at: '2026-05-14T10:30:00.000Z'
758	  jiang2023mistral:
759	    title: Mistral 7B
760	    authors:
761	    - Albert Q. Jiang
762	    - Alexandre Sablayrolles
763	    - Arthur Mensch
764	    - Chris Bamford
765	    - Devendra Singh Chaplot
766	    - Diego de las Casas
767	    - Florian Bressand
768	    - Gianna Lengyel
769	    - Guillaume Lample
770	    - Lucile Saulnier
771	    - Lelio Renard Lavaud
772	    - Marie-Anne Lachaux
773	    - Pierre Stock
774	    - Teven Le Scao
775	    - Thibaut Lavril
776	    - Thomas Wang
777	    - Timothee Lacroix
778	    - William El Sayed
779	    year: 2023
780	    venue: arXiv 2023
781	    url: ''
782	    doi: '2310.06825'
783	    bibtex_key: jiang2023mistral
784	    category: Evaluation Models
785	    role: evaluation
786	    relevance: Mistral-7B-v0.3 is our third evaluation model. GQA with 4:1 ratio (8 KV heads, 32 query heads). Negative result from per-head allocation—demonstrates architecture-dependent effectiveness.
787	    abstract: Mistral 7B leverages grouped-query attention (GQA) for faster inference and sliding window attention (SWA) for handling arbitrary-length sequences with reduced cost. Outperforms Llama 2 13B on all benchmarks.
788	    semantic_scholar_id: ''
789	    verified: true
790	    added_by: literature-survey
791	    added_at: '2026-05-14T10:30:00.000Z'
792	
793	  # ============================================================
794	  # Cluster 8: Theory (1 paper)
795	  # ============================================================
796	  kellerer2004knapsack:
797	    title: Knapsack Problems
798	    authors:
799	    - Hans Kellerer
800	    - Ulrich Pferschy
801	    - David Pisinger
802	    year: 2004
803	    venue: Springer
804	    url: ''
805	    doi: 10.1007/978-3-540-24777-7
806	    bibtex_key: kellerer2004knapsack
807	    category: Theory
808	    role: foundation
809	    relevance: Definitive reference for multiple-choice knapsack problem (MCKP, Chapter 11). Our per-head bit allocation with hardware-aligned {2,4,8,16} is formulated as MCKP. Greedy optimality conditions and dominance relations from this text underpin our theoretical analysis.
810	    abstract: Comprehensive monograph on knapsack problems covering 0-1, bounded, unbounded, subset-sum, change-making, multiple-choice, and multi-dimensional variants. Chapter 11 covers MCKP including dominance, branch-and-bound, dynamic programming, and approximation algorithms.
811	    semantic_scholar_id: ''
812	    verified: true
813	    added_by: literature-survey
814	    added_at: '2026-05-14T10:30:00.000Z'
815	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c020d4be-267f-49cc-b475-b717f4100f40",
  "isSidechain": false,
  "promptId": "964448b9-9407-4006-b5f8-3afa58950999",
  "type": "user",
  "uuid": "26aa19ef-cd1f-4b82-9b52-294f286f7e1a",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/literature_map.yaml",
      "content": "meta:\n  last_updated: '2026-05-14T10:30:00.000Z'\n  total_papers: 35\ncategories:\n  - Mixed-Precision Rate-Distortion\n  - KV Cache Quantization\n  - KV Cache Eviction\n  - Model Compression\n  - Attention Head Analysis\n  - LLM Inference Efficiency\n  - Evaluation Models\n  - Theory\npapers:\n  # ============================================================\n  # Cluster 1: Mixed-Precision R-D Allocation (5 papers)\n  # ============================================================\n  zuo2026ratequant:\n    title: 'RateQuant: Optimal Mixed-Precision KV Cache Quantization via Rate-Distortion Theory'\n    authors:\n    - Fei Zuo\n    - Zikang Zhou\n    - Hao Cong\n    - Xiaoyan Xi\n    - Ho Fai Leung\n    year: 2026\n    venue: arXiv 2026\n    url: ''\n    doi: '2605.06675'\n    bibtex_key: zuo2026ratequant\n    category: Mixed-Precision Rate-Distortion\n    role: direct-competitor\n    relevance: 'Primary competitor: R-D optimal per-head KV cache bit allocation. Algorithm 1 (discrete greedy). Theorem 2 (continuous closed-form via reverse waterfilling). Proposition 6 (greedy optimality on consecutive integers). Key limitation: does not address hardware-aligned non-consecutive {2,4,8,16} where greedy may fail.'\n    abstract: RateQuant fits a per-quantizer distortion model D(b)=alpha*beta^{-b} from a small calibration set, then solves the bit-allocation in closed form via reverse waterfilling from rate-distortion theory. On Qwen3-8B at 2.5 avg bits, calibrated RateQuant reduces KIVI perplexity from 49.3 to 14.9 (70% reduction). Calibration takes 1.6s on a single GPU with zero inference overhead.\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research\n    added_at: '2026-05-14T08:42:26.710Z'\n  lei2026arkv:\n    title: 'ARKV: Adaptive and Resource-Efficient KV Cache Management under Limited Memory Budget for Long-Context Inference in LLMs'\n    authors:\n    - Jianlong Lei\n    - Shashikant Ilager\n    year: 2026\n    venue: arXiv 2026\n    url: ''\n    doi: '2603.08727'\n    bibtex_key: lei2026arkv\n    category: Mixed-Precision Rate-Distortion\n    role: direct-competitor\n    relevance: Adaptive mixed-precision KV cache with tri-state token assignment (Original/Quantization/Eviction). Per-layer OQ ratio estimation via attention entropy, variance, kurtosis. Alternative adaptive allocation strategy to our R-D formulation.\n    abstract: 'ARKV dynamically allocates precision levels to cached tokens based on per-layer attention dynamics and token-level importance. Three components: per-layer OQ ratio estimation, token importance scoring, and tri-state cache assignment. Preserves ~97% baseline accuracy with 4x KV memory reduction.'\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research\n    added_at: '2026-05-14T08:42:26.710Z'\n  li2025kvmix:\n    title: 'KVmix: Gradient-Based Layer Importance-Aware Mixed-Precision Quantization for KV Cache'\n    authors:\n    - Fei Li\n    - Song Liu\n    - Weiguo Wu\n    - Shiqiang Nie\n    - Jinyu Wang\n    year: 2025\n    venue: arXiv 2025\n    url: ''\n    doi: '2506.08018'\n    bibtex_key: li2025kvmix\n    category: Mixed-Precision Rate-Distortion\n    role: method-component\n    relevance: Gradient-based importance for layer-wise KV cache bit-width allocation. Heuristic sensitivity-based approach vs our R-D optimal formulation. Achieves near-lossless at Key 2.19bit / Value 2.38bit.\n    abstract: KVmix employs gradient-based importance analysis to evaluate how individual Key and Value projection matrices affect model loss, enabling layer-specific bit-width allocation. Includes dynamic long-context optimization preserving full-precision KV pairs for recent pivotal tokens.\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research\n    added_at: '2026-05-14T08:42:26.710Z'\n  zhang2025mixkvq:\n    title: 'MixKVQ: Query-Aware Mixed-Precision KV Cache Quantization for Long-Context Reasoning'\n    authors:\n    - Tao Zhang\n    - Ziqian Zeng\n    - Hao Peng\n    - Huiping Zhuang\n    - Cen Chen\n    year: 2025\n    venue: arXiv 2025\n    url: ''\n    doi: '2512.19206'\n    bibtex_key: zhang2025mixkvq\n    category: Mixed-Precision Rate-Distortion\n    role: method-component\n    relevance: 'Query-aware channel-level mixed-precision for KV cache. Orthogonal to our per-head R-D allocation: operates at channel granularity rather than head granularity.'\n    abstract: MixKVQ introduces a lightweight query-aware algorithm to identify and preserve critical key channels at higher precision while applying per-token quantization for value cache. Outperforms existing low-bit methods on complex reasoning datasets.\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research\n    added_at: '2026-05-14T08:42:26.710Z'\n  kim2024squeezellm:\n    title: 'SqueezeLLM: Dense-and-Sparse Quantization'\n    authors:\n    - Sehoon Kim\n    - Coleman Hooper\n    - Amir Gholami\n    - Zhen Dong\n    - Xiuyu Li\n    - Sheng Shen\n    - Michael W. Mahoney\n    - Kurt Keutzer\n    year: 2024\n    venue: ICML 2024\n    url: ''\n    doi: '2306.07629'\n    bibtex_key: kim2024squeezellm\n    category: Mixed-Precision Rate-Distortion\n    role: foundation\n    relevance: Foundational sensitivity-based non-uniform quantization using second-order information. Pioneered per-group precision assignment based on sensitivity—principle we extend to per-head KV cache R-D allocation.\n    abstract: 'SqueezeLLM enables lossless compression to ultra-low 3-bit precision via two ideas: sensitivity-based non-uniform quantization searching for optimal bit precision assignment, and Dense-and-Sparse decomposition storing outliers in efficient sparse format.'\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research\n    added_at: '2026-05-14T08:42:26.710Z'\n\n  # ============================================================\n  # Cluster 2: KV Cache Quantization (6 papers)\n  # ============================================================\n  liu2024kivi:\n    title: 'KIVI: A Tuning-Free Asymmetric 2bit Quantization for KV Cache'\n    authors:\n    - Zirui Liu\n    - Jiayi Yuan\n    - Hongye Jin\n    - Shaochen Zhong\n    - Zhaozhuo Xu\n    - Vladimir Braverman\n    - Beidi Chen\n    - Xia Hu\n    year: 2024\n    venue: ICML 2024\n    url: ''\n    doi: '2402.02750'\n    bibtex_key: liu2024kivi\n    category: KV Cache Quantization\n    role: direct-competitor\n    relevance: Asymmetric per-channel key / per-token value 2-bit KV cache quantization; tuning-free baseline for mixed-precision KV cache methods\n    abstract: We conduct a comprehensive study on the element distribution in KV cache of popular LLMs and find that the key cache should be quantized per-channel while the value cache should be quantized per-token. From this observation, we develop a tuning-free 2bit KV cache quantization algorithm named KIVI.\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research\n    added_at: '2026-05-14T07:56:45.265Z'\n  hooper2024kvquant:\n    title: 'KVQuant: Towards 10 Million Context Length LLM Inference with KV Cache Quantization'\n    authors:\n    - Coleman Hooper\n    - Sehoon Kim\n    - Hiva Mohammadzadeh\n    - Michael W. Mahoney\n    - Yakun Sophia Shao\n    - Kurt Keutzer\n    - Amir Gholami\n    year: 2024\n    venue: NeurIPS 2024\n    url: ''\n    doi: '2401.18079'\n    bibtex_key: hooper2024kvquant\n    category: KV Cache Quantization\n    role: direct-competitor\n    relevance: Per-channel key quantization with pre-RoPE, non-uniform datatypes, and dense-and-sparse outlier handling; achieves sub-4-bit KV cache for 10M context\n    abstract: KV cache activations are the dominant contributor to memory consumption during LLM inference for large context windows. We address this with per-channel key quantization, pre-RoPE key quantization, non-uniform KV cache quantization, and per-vector dense-and-sparse quantization to isolate outliers.\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research\n    added_at: '2026-05-14T07:56:45.265Z'\n  lin2024qserve:\n    title: 'QServe: W4A8KV4 Quantization and System Co-design for Efficient LLM Serving'\n    authors:\n    - Yujun Lin\n    - Haotian Tang\n    - Shang Yang\n    - Zhekai Zhang\n    - Guangxuan Xiao\n    - Chuang Gan\n    - Song Han\n    year: 2024\n    venue: MLSys 2025\n    url: ''\n    doi: '2405.04532'\n    bibtex_key: lin2024qserve\n    category: KV Cache Quantization\n    role: foundation\n    relevance: W4A8KV4 co-design with SmoothAttention for KV4 quantization; demonstrates system-level gains from joint weight-activation-KV quantization\n    abstract: QServe introduces QoQ (W4A8KV4), a quantization algorithm with 4-bit weight, 8-bit activation, and 4-bit KV cache. Progressive group quantization ensures all GEMMs run on INT8 tensor cores. SmoothAttention shifts quantization difficulty from keys to queries.\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research\n    added_at: '2026-05-14T07:56:45.265Z'\n  he2024zipcache:\n    title: 'ZipCache: Accurate and Efficient KV Cache Quantization with Salient Token Identification'\n    authors:\n    - Yefei He\n    - Luoming Zhang\n    - Weijia Wu\n    - Jing Liu\n    - Hong Zhou\n    - Bohan Zhuang\n    year: 2024\n    venue: NeurIPS 2024\n    url: ''\n    doi: '2405.14256'\n    bibtex_key: he2024zipcache\n    category: KV Cache Quantization\n    role: direct-competitor\n    relevance: Channel-separable tokenwise quantization with adaptive bit-width based on normalized attention score saliency; mixed-precision KV cache baseline\n    abstract: ZipCache proposes channel-separable tokenwise quantization and uses normalized attention score for identifying salient tokens with adaptive bit-width assignment. Achieves 4.98x compression on Mistral-7B with 0.38% accuracy drop.\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research\n    added_at: '2026-05-14T07:56:45.265Z'\n  kang2024gear:\n    title: 'GEAR: An Efficient KV Cache Compression Recipe for Near-Lossless Generative Inference of LLM'\n    authors:\n    - Hao Kang\n    - Qingru Zhang\n    - Souvik Kundu\n    - Geonhwa Jeong\n    - Zaoxing Liu\n    - Tushar Krishna\n    - Tuo Zhao\n    year: 2024\n    venue: arXiv 2024\n    url: ''\n    doi: '2403.05527'\n    bibtex_key: kang2024gear\n    category: KV Cache Quantization\n    role: direct-competitor\n    relevance: Hybrid quantization + low-rank + sparse error correction for KV cache; demonstrates that residual compensation improves ultra-low-bit quantization quality\n    abstract: GEAR first applies quantization to majority of entries to ultra-low precision, then employs a low rank matrix to approximate the quantization error, and a sparse matrix to remedy individual errors from outlier entries. Achieves near-lossless 4-bit compression with 2.38x throughput improvement.\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research\n    added_at: '2026-05-14T07:56:45.265Z'\n  duanmu2024skvq:\n    title: 'SKVQ: Sliding-window Key and Value Cache Quantization for Large Language Models'\n    authors:\n    - Haojie Duanmu\n    - Zhihang Yuan\n    - Xiuhong Li\n    - Jiangfei Duan\n    - Xingcheng Zhang\n    - Dahua Lin\n    year: 2024\n    venue: arXiv 2024\n    url: ''\n    doi: '2405.06219'\n    bibtex_key: duanmu2024skvq\n    category: KV Cache Quantization\n    role: direct-competitor\n    relevance: Channel rearrangement + sliding-window high-precision recent tokens; achieves 2-bit key / 1.5-bit value with minimal accuracy loss\n    abstract: SKVQ rearranges KV cache channels to improve similarity within quantization groups and applies clipped dynamic quantization at group level. Preserves recent window tokens at high precision. Enables 2-bit keys and 1.5-bit values with up to 1M context on 80GB GPU.\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research\n    added_at: '2026-05-14T07:56:45.265Z'\n\n  # ============================================================\n  # Cluster 3: KV Cache Eviction (6 papers)\n  # ============================================================\n  zhang2023h2o:\n    title: 'H2O: Heavy-Hitter Oracle for Efficient Generative Inference of Large Language Models'\n    authors:\n    - Zhenyu Zhang\n    - Ying Sheng\n    - Tianyi Zhou\n    - Tianlong Chen\n    - Lianmin Zheng\n    - Ruisi Cai\n    - Zhao Song\n    - Yuandong Tian\n    - Christopher Re\n    - Clark Barrett\n    - Zhangyang Wang\n    - Beidi Chen\n    year: 2023\n    venue: NeurIPS 2023\n    url: ''\n    doi: 10.48550/arXiv.2306.14048\n    bibtex_key: zhang2023h2o\n    category: KV Cache Eviction\n    role: background\n    relevance: Foundational KV cache eviction policy based on heavy-hitter tokens; orthogonal to our quantization approach\n    abstract: H2O identifies Heavy Hitters — a small set of tokens contributing most to attention scores — and dynamically retains recent and H2 tokens. With 20% heavy hitters, H2O improves throughput by up to 29x and reduces KV cache memory by up to 5x.\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research\n    added_at: '2026-05-14T08:10:15.562Z'\n  li2024snapkv:\n    title: 'SnapKV: LLM Knows What You are Looking for Before Generation'\n    authors:\n    - Yuhong Li\n    - Yingbing Huang\n    - Bowen Yang\n    - Bharat Venkitesh\n    - Acyr Locatelli\n    - Hanchen Ye\n    - Tianle Cai\n    - Patrick Lewis\n    - Deming Chen\n    year: 2024\n    venue: NeurIPS 2024\n    url: ''\n    doi: 10.48550/arXiv.2404.14469\n    bibtex_key: li2024snapkv\n    category: KV Cache Eviction\n    role: background\n    relevance: Observation-driven KV cache compression using attention pattern consistency; competes with eviction-based approaches our work compares against\n    abstract: SnapKV efficiently minimizes KV cache size by selecting clustered important KV positions per attention head using an observation window at the end of the prompt. Achieves 3.6x speed increase and 8.2x memory efficiency at 16K tokens.\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research\n    added_at: '2026-05-14T08:10:15.562Z'\n  ge2024fastgen:\n    title: 'Model Tells You What to Discard: Adaptive KV Cache Compression for LLMs'\n    authors:\n    - Suyu Ge\n    - Yunan Zhang\n    - Liyuan Liu\n    - Minjia Zhang\n    - Jiawei Han\n    - Jianfeng Gao\n    year: 2024\n    venue: ICLR 2024\n    url: ''\n    doi: 10.48550/arXiv.2310.01801\n    bibtex_key: ge2024fastgen\n    category: KV Cache Eviction\n    role: background\n    relevance: Adaptive per-head eviction strategy (FastGen); demonstrates head-specific compression is beneficial, complementary to quantization\n    abstract: 'FastGen constructs KV cache adaptively per attention head: evicting long-range contexts on local-attention heads, discarding non-special tokens on special-token-focused heads, and using standard KV cache for broad-attention heads. Reduces memory by 50% without sacrificing quality.'\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research\n    added_at: '2026-05-14T08:10:15.562Z'\n  xiao2024streamingllm:\n    title: Efficient Streaming Language Models with Attention Sinks\n    authors:\n    - Guangxuan Xiao\n    - Yuandong Tian\n    - Beidi Chen\n    - Song Han\n    - Mike Lewis\n    year: 2024\n    venue: ICLR 2024\n    url: ''\n    doi: 10.48550/arXiv.2309.17453\n    bibtex_key: xiao2024streamingllm\n    category: KV Cache Eviction\n    role: background\n    relevance: Discovers attention sink phenomenon in initial tokens; motivates why naive eviction can fail and informs our quantization-first approach\n    abstract: StreamingLLM enables LLMs to generalize to infinite sequence lengths without fine-tuning by retaining attention sink tokens alongside a sliding window of recent tokens. Achieves up to 22.2x speedup over sliding window recomputation.\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research\n    added_at: '2026-05-14T08:10:15.562Z'\n  liu2024scissorhands:\n    title: 'Scissorhands: Exploiting the Persistence of Importance Hypothesis for LLM KV Cache Compression at Test Time'\n    authors:\n    - Zichang Liu\n    - Aditya Desai\n    - Fangshuo Liao\n    - Weitao Wang\n    - Victor Xie\n    - Zhaozhuo Xu\n    - Anastasios Kyrillidis\n    - Anshumali Shrivastava\n    year: 2024\n    venue: NeurIPS 2023\n    url: ''\n    doi: 10.48550/arXiv.2305.17118\n    bibtex_key: liu2024scissorhands\n    category: KV Cache Eviction\n    role: background\n    relevance: Persistence-of-importance hypothesis for KV cache eviction; achieves 5x cache reduction, combinable with 4-bit quantization for 20x compression\n    abstract: Scissorhands maintains KV cache at a fixed budget by storing pivotal tokens with higher probability, achieving up to 5x memory reduction without quality loss, and up to 20x when combined with 4-bit quantization.\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research\n    added_at: '2026-05-14T08:10:15.562Z'\n  yang2024pyramidinfer:\n    title: 'PyramidInfer: Pyramid KV Cache Compression for High-throughput LLM Inference'\n    authors:\n    - Dongjie Yang\n    - Xiaodong Han\n    - Yan Gao\n    - Yao Hu\n    - Shilin Zhang\n    - Hai Zhao\n    year: 2024\n    venue: Findings of ACL 2024\n    url: ''\n    doi: 10.48550/arXiv.2405.12532\n    bibtex_key: yang2024pyramidinfer\n    category: KV Cache Eviction\n    role: background\n    relevance: Layer-wise pyramid compression exploiting inter-layer dependency; crucial KV count decreases across layers, relevant to our per-layer rate allocation\n    abstract: PyramidInfer compresses KV cache by layer-wise retaining crucial context, exploiting the finding that crucial keys and values decrease layer by layer. Achieves 2.2x throughput improvement with 54% GPU memory reduction.\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research\n    added_at: '2026-05-14T08:10:15.562Z'\n\n  # ============================================================\n  # Cluster 4: Model Compression (6 papers)\n  # ============================================================\n  frantar2023gptq:\n    title: 'GPTQ: Accurate Post-Training Quantization for Generative Pre-trained Transformers'\n    authors:\n    - Elias Frantar\n    - Saleh Ashkboos\n    - Torsten Hoefler\n    - Dan Alistarh\n    year: 2023\n    venue: ICLR 2023\n    url: ''\n    doi: '2210.17323'\n    bibtex_key: frantar2023gptq\n    category: Model Compression\n    role: foundation\n    relevance: Foundational one-shot weight quantization based on approximate second-order information (OBQ). Reduces bitwidth to 3-4 bits per weight with negligible accuracy degradation. Established post-training quantization paradigm for LLMs.\n    abstract: GPTQ is a one-shot weight quantization method based on approximate second-order information that can quantize GPT models with 175 billion parameters in approximately four GPU hours, reducing bitwidth to 3 or 4 bits per weight with negligible accuracy degradation.\n    semantic_scholar_id: ''\n    verified: true\n    added_by: literature-survey\n    added_at: '2026-05-14T10:30:00.000Z'\n  lin2024awq:\n    title: 'AWQ: Activation-aware Weight Quantization for LLM Compression and Acceleration'\n    authors:\n    - Ji Lin\n    - Jiaming Tang\n    - Haotian Tang\n    - Shang Yang\n    - Wei-Ming Chen\n    - Wei-Chen Wang\n    - Guangxuan Xiao\n    - Xingyu Dang\n    - Chuang Gan\n    - Song Han\n    year: 2024\n    venue: MLSys 2024 (Best Paper)\n    url: ''\n    doi: '2306.00978'\n    bibtex_key: lin2024awq\n    category: Model Compression\n    role: foundation\n    relevance: Activation-aware salient weight protection via equivalent scaling transformation. Demonstrates that 1% salient weights dominate quantization quality—analogous to our finding that per-head sensitivity varies drastically.\n    abstract: AWQ finds that protecting only 1% salient weights (identified by activation distribution, not weights) greatly reduces quantization error. Scales salient channels via mathematically equivalent transformation. No backpropagation or reconstruction needed. 3x speedup over FP16.\n    semantic_scholar_id: ''\n    verified: true\n    added_by: literature-survey\n    added_at: '2026-05-14T10:30:00.000Z'\n  xiao2023smoothquant:\n    title: 'SmoothQuant: Accurate and Efficient Post-Training Quantization for Large Language Models'\n    authors:\n    - Guangxuan Xiao\n    - Ji Lin\n    - Mickael Seznec\n    - Hao Wu\n    - Julien Demouth\n    - Song Han\n    year: 2023\n    venue: ICML 2023\n    url: ''\n    doi: '2211.10438'\n    bibtex_key: xiao2023smoothquant\n    category: Model Compression\n    role: foundation\n    relevance: Smooths activation outliers by migrating quantization difficulty from activations to weights. Enables W8A8 for all matmuls in LLMs. QServe's SmoothAttention extends this idea to KV cache.\n    abstract: SmoothQuant enables INT8 quantization of both weights and activations for all matrix multiplications in LLMs by smoothing activation outliers via offline migration of quantization difficulty from activations to weights. Up to 1.56x speedup and 2x memory reduction with negligible accuracy loss.\n    semantic_scholar_id: ''\n    verified: true\n    added_by: literature-survey\n    added_at: '2026-05-14T10:30:00.000Z'\n  dettmers2022llmint8:\n    title: 'LLM.int8(): 8-bit Matrix Multiplication for Transformers at Scale'\n    authors:\n    - Tim Dettmers\n    - Mike Lewis\n    - Younes Belkada\n    - Luke Zettlemoyer\n    year: 2022\n    venue: NeurIPS 2022\n    url: ''\n    doi: '2208.07339'\n    bibtex_key: dettmers2022llmint8\n    category: Model Compression\n    role: foundation\n    relevance: First to identify emergent outlier features in transformers that dominate quantization quality. Mixed-precision decomposition (0.1% in FP16, 99.9% in INT8) is conceptually related to our per-head mixed-precision allocation.\n    abstract: LLM.int8() develops Int8 matrix multiplication for feed-forward and attention projection layers via absmax vector-wise quantization and mixed precision decomposition. Cuts inference memory by half while retaining full precision performance for 175B-parameter models.\n    semantic_scholar_id: ''\n    verified: true\n    added_by: literature-survey\n    added_at: '2026-05-14T10:30:00.000Z'\n  tseng2024quipsharp:\n    title: 'QuIP#: Even Better LLM Quantization with Hadamard Incoherence and Lattice Codebooks'\n    authors:\n    - Albert Tseng\n    - Jerry Chee\n    - Qingyao Sun\n    - Volodymyr Kuleshov\n    - Christopher De Sa\n    year: 2024\n    venue: ICML 2024\n    url: ''\n    doi: '2402.04396'\n    bibtex_key: tseng2024quipsharp\n    category: Model Compression\n    role: foundation\n    relevance: State-of-the-art extreme compression (2-bit weights) via Hadamard incoherence processing and E8 lattice codebooks. Theoretical grounding for why incoherent distributions quantize better—relevant to understanding per-head distortion variation.\n    abstract: QuIP# achieves state-of-the-art in extreme weight compression using randomized Hadamard transform for incoherence processing, E8 lattice codebooks for vector quantization of sub-Gaussian incoherent weights, and fine-tuning for fidelity. Hardware-efficient implementation.\n    semantic_scholar_id: ''\n    verified: true\n    added_by: literature-survey\n    added_at: '2026-05-14T10:30:00.000Z'\n  zhao2024atom:\n    title: 'Atom: Low-bit Quantization for Efficient and Accurate LLM Serving'\n    authors:\n    - Yilong Zhao\n    - Chien-Yu Lin\n    - Kan Zhu\n    - Zihao Ye\n    - Lequn Chen\n    - Size Zheng\n    - Luis Ceze\n    - Arvind Krishnamurthy\n    - Tianqi Chen\n    - Baris Kasikci\n    year: 2024\n    venue: MLSys 2024\n    url: ''\n    doi: '2310.19102'\n    bibtex_key: zhao2024atom\n    category: Model Compression\n    role: foundation\n    relevance: End-to-end low-bit quantization for serving with mixed-precision, group quantization, and KV cache quantization. Demonstrates system-level throughput gains (3.5x over FP16) from co-designed quantization kernels.\n    abstract: Atom combines mixed-precision quantization retaining salient activations/weights in high precision, fine-grained group quantization, dynamic activation quantization, KV-cache quantization, and efficient CUDA kernels. Achieves 7.73x throughput over FP16 baseline.\n    semantic_scholar_id: ''\n    verified: true\n    added_by: literature-survey\n    added_at: '2026-05-14T10:30:00.000Z'\n\n  # ============================================================\n  # Cluster 5: Attention Head Analysis (4 papers)\n  # ============================================================\n  voita2019heads:\n    title: 'Analyzing Multi-Head Self-Attention: Specialized Heads Do the Heavy Lifting, the Rest Can Be Pruned'\n    authors:\n    - Elena Voita\n    - David Talbot\n    - Fedor Moiseev\n    - Rico Sennrich\n    - Ivan Titov\n    year: 2019\n    venue: ACL 2019\n    url: ''\n    doi: '1905.09418'\n    bibtex_key: voita2019heads\n    category: Attention Head Analysis\n    role: foundation\n    relevance: Foundational work on attention head specialization and pruning. Shows most heads can be pruned (38/48 with only 0.15 BLEU drop). Motivates our per-head heterogeneous quantization—heads have different importance and roles.\n    abstract: Evaluates individual attention head contributions and identifies specialized heads playing consistent linguistically-interpretable roles. Using stochastic gates with L0 penalty, the vast majority of heads can be pruned without seriously affecting performance.\n    semantic_scholar_id: ''\n    verified: true\n    added_by: literature-survey\n    added_at: '2026-05-14T10:30:00.000Z'\n  michel2019sixteen:\n    title: Are Sixteen Heads Really Better than One?\n    authors:\n    - Paul Michel\n    - Omer Levy\n    - Graham Neubig\n    year: 2019\n    venue: NeurIPS 2019\n    url: ''\n    doi: '1905.10650'\n    bibtex_key: michel2019sixteen\n    category: Attention Head Analysis\n    role: foundation\n    relevance: Shows large proportion of attention heads can be removed at test time. Greedy pruning analysis reveals varying head importance. Directly supports our premise that heads deserve different quantization precision.\n    abstract: A large proportion of attention heads can be removed at test time without significantly impacting performance, and some layers can be reduced to a single head. Self-attention layers can be significantly pruned while encoder-decoder layers are more dependent on multi-headedness.\n    semantic_scholar_id: ''\n    verified: true\n    added_by: literature-survey\n    added_at: '2026-05-14T10:30:00.000Z'\n  clark2019bert:\n    title: What Does BERT Look At? An Analysis of BERT's Attention\n    authors:\n    - Kevin Clark\n    - Urvashi Khandelwal\n    - Omer Levy\n    - Christopher D. Manning\n    year: 2019\n    venue: ACL Workshop BlackboxNLP 2019\n    url: ''\n    doi: '1906.04341'\n    bibtex_key: clark2019bert\n    category: Attention Head Analysis\n    role: background\n    relevance: Characterizes attention head behavior patterns (delimiter tokens, positional offsets, broad attention). Shows heads in same layer often exhibit similar behaviors—relevant to understanding GQA group structure.\n    abstract: Proposes methods for analyzing attention mechanisms of pre-trained models. Finds BERT heads exhibit patterns like attending to delimiter tokens, positional offsets, or broadly over sentences. Certain heads correspond to syntactic and coreference relations with high accuracy.\n    semantic_scholar_id: ''\n    verified: true\n    added_by: literature-survey\n    added_at: '2026-05-14T10:30:00.000Z'\n  ainslie2023gqa:\n    title: 'GQA: Training Generalized Multi-Query Transformer Models from Multi-Head Checkpoints'\n    authors:\n    - Joshua Ainslie\n    - James Lee-Thorp\n    - Michiel de Jong\n    - Yury Zemlyanskiy\n    - Federico Lebron\n    - Sumit Sanghai\n    year: 2023\n    venue: EMNLP 2023\n    url: ''\n    doi: '2305.13245'\n    bibtex_key: ainslie2023gqa\n    category: Attention Head Analysis\n    role: foundation\n    relevance: Defines grouped-query attention (GQA) which is the architecture used by all three models we evaluate (Qwen2.5 7:1, Llama-3.1 4:1, Mistral 4:1). GQA group ratio directly affects our per-head allocation granularity and results.\n    abstract: Proposes grouped-query attention (GQA), a generalization of multi-query attention using an intermediate number of key-value heads. Uptrained GQA achieves quality close to multi-head attention with comparable speed to MQA. Provides recipe for uptraining existing MHA checkpoints.\n    semantic_scholar_id: ''\n    verified: true\n    added_by: literature-survey\n    added_at: '2026-05-14T10:30:00.000Z'\n\n  # ============================================================\n  # Cluster 6: LLM Inference Efficiency (4 papers)\n  # ============================================================\n  kwon2023vllm:\n    title: Efficient Memory Management for Large Language Model Serving with PagedAttention\n    authors:\n    - Woosuk Kwon\n    - Zhuohan Li\n    - Siyuan Zhuang\n    - Ying Sheng\n    - Lianmin Zheng\n    - Cody Hao Yu\n    - Joseph E. Gonzalez\n    - Hao Zhang\n    - Ion Stoica\n    year: 2023\n    venue: SOSP 2023\n    url: ''\n    doi: '2309.06180'\n    bibtex_key: kwon2023vllm\n    category: LLM Inference Efficiency\n    role: background\n    relevance: PagedAttention enables non-contiguous KV cache storage, reducing memory waste. Our per-head mixed-precision allocation is complementary—can be applied within vLLM's paged memory management.\n    abstract: vLLM proposes PagedAttention inspired by virtual memory paging, achieving near-zero waste in KV cache memory and flexible sharing within and across requests. 2-4x throughput improvement over state-of-the-art systems.\n    semantic_scholar_id: ''\n    verified: true\n    added_by: literature-survey\n    added_at: '2026-05-14T10:30:00.000Z'\n  dao2022flashattention:\n    title: 'FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness'\n    authors:\n    - Tri Dao\n    - Daniel Y. Fu\n    - Stefano Ermon\n    - Atri Rudra\n    - Christopher Re\n    year: 2022\n    venue: NeurIPS 2022\n    url: ''\n    doi: '2205.14135'\n    bibtex_key: dao2022flashattention\n    category: LLM Inference Efficiency\n    role: background\n    relevance: IO-aware tiling for exact attention. Our quantized KV cache reduces HBM reads during attention, providing complementary gains to FlashAttention's tiling strategy.\n    abstract: FlashAttention uses tiling to reduce memory reads/writes between GPU HBM and SRAM. 15% speedup on BERT-large, 3x on GPT-2, 2.4x on long-range arena, without approximation.\n    semantic_scholar_id: ''\n    verified: true\n    added_by: literature-survey\n    added_at: '2026-05-14T10:30:00.000Z'\n  shazeer2019mqa:\n    title: 'Fast Transformer Decoding: One Write-Head is All You Need'\n    authors:\n    - Noam Shazeer\n    year: 2019\n    venue: arXiv 2019\n    url: ''\n    doi: '1911.02150'\n    bibtex_key: shazeer2019mqa\n    category: LLM Inference Efficiency\n    role: foundation\n    relevance: Introduces multi-query attention (MQA) sharing a single KV head across all query heads. GQA generalizes MQA. Our per-head allocation exploits the remaining KV head heterogeneity in GQA models.\n    abstract: Proposes multi-query attention where keys and values are shared across all attention heads, greatly reducing KV cache size and memory bandwidth requirements of incremental decoding. Much faster decoding with minor quality degradation.\n    semantic_scholar_id: ''\n    verified: true\n    added_by: literature-survey\n    added_at: '2026-05-14T10:30:00.000Z'\n  deepseek2024v2:\n    title: 'DeepSeek-V2: A Strong, Economical, and Efficient Mixture-of-Experts Language Model'\n    authors:\n    - DeepSeek-AI\n    year: 2024\n    venue: arXiv 2024\n    url: ''\n    doi: '2405.04434'\n    bibtex_key: deepseek2024v2\n    category: LLM Inference Efficiency\n    role: background\n    relevance: Introduces Multi-head Latent Attention (MLA) compressing KV cache into low-rank latent vectors (93.3% reduction). Alternative architectural approach to KV cache reduction vs our post-training quantization.\n    abstract: DeepSeek-V2 uses Multi-head Latent Attention (MLA) compressing KV caches into latent vectors and DeepSeekMoE for sparse computation. 236B total parameters, 21B activated per token. 42.5% training cost reduction, 93.3% KV cache reduction, 5.76x throughput increase vs DeepSeek 67B.\n    semantic_scholar_id: ''\n    verified: true\n    added_by: literature-survey\n    added_at: '2026-05-14T10:30:00.000Z'\n\n  # ============================================================\n  # Cluster 7: Evaluation Models (3 papers)\n  # ============================================================\n  grattafiori2024llama3:\n    title: The Llama 3 Herd of Models\n    authors:\n    - Aaron Grattafiori\n    - et al.\n    year: 2024\n    venue: arXiv 2024\n    url: ''\n    doi: '2407.21783'\n    bibtex_key: grattafiori2024llama3\n    category: Evaluation Models\n    role: evaluation\n    relevance: Llama-3.1-8B is one of three evaluation models. GQA with 4:1 ratio (8 KV heads, 32 query heads). Marginal gains from per-head allocation in our experiments.\n    abstract: Llama 3 is a herd of foundation models natively supporting multilinguality, coding, reasoning, and tool usage. Dense Transformer up to 405B parameters with 128K context. Comparable quality to GPT-4.\n    semantic_scholar_id: ''\n    verified: true\n    added_by: literature-survey\n    added_at: '2026-05-14T10:30:00.000Z'\n  yang2025qwen25:\n    title: Qwen2.5 Technical Report\n    authors:\n    - An Yang\n    - et al.\n    year: 2025\n    venue: arXiv 2024\n    url: ''\n    doi: '2412.15115'\n    bibtex_key: yang2025qwen25\n    category: Evaluation Models\n    role: evaluation\n    relevance: Qwen2.5-7B is our strongest-result model. GQA with 7:1 ratio (4 KV heads, 28 query heads)—highest heterogeneity among tested models, yielding 29.3% PPL improvement from per-head allocation.\n    abstract: Qwen2.5 is a comprehensive LLM series with improvements in pre-training (18T tokens) and post-training. Qwen2.5-72B-Instruct outperforms many open and proprietary models, competitive with Llama-3-405B-Instruct at 5x smaller size.\n    semantic_scholar_id: ''\n    verified: true\n    added_by: literature-survey\n    added_at: '2026-05-14T10:30:00.000Z'\n  jiang2023mistral:\n    title: Mistral 7B\n    authors:\n    - Albert Q. Jiang\n    - Alexandre Sablayrolles\n    - Arthur Mensch\n    - Chris Bamford\n    - Devendra Singh Chaplot\n    - Diego de las Casas\n    - Florian Bressand\n    - Gianna Lengyel\n    - Guillaume Lample\n    - Lucile Saulnier\n    - Lelio Renard Lavaud\n    - Marie-Anne Lachaux\n    - Pierre Stock\n    - Teven Le Scao\n    - Thibaut Lavril\n    - Thomas Wang\n    - Timothee Lacroix\n    - William El Sayed\n    year: 2023\n    venue: arXiv 2023\n    url: ''\n    doi: '2310.06825'\n    bibtex_key: jiang2023mistral\n    category: Evaluation Models\n    role: evaluation\n    relevance: Mistral-7B-v0.3 is our third evaluation model. GQA with 4:1 ratio (8 KV heads, 32 query heads). Negative result from per-head allocation—demonstrates architecture-dependent effectiveness.\n    abstract: Mistral 7B leverages grouped-query attention (GQA) for faster inference and sliding window attention (SWA) for handling arbitrary-length sequences with reduced cost. Outperforms Llama 2 13B on all benchmarks.\n    semantic_scholar_id: ''\n    verified: true\n    added_by: literature-survey\n    added_at: '2026-05-14T10:30:00.000Z'\n\n  # ============================================================\n  # Cluster 8: Theory (1 paper)\n  # ============================================================\n  kellerer2004knapsack:\n    title: Knapsack Problems\n    authors:\n    - Hans Kellerer\n    - Ulrich Pferschy\n    - David Pisinger\n    year: 2004\n    venue: Springer\n    url: ''\n    doi: 10.1007/978-3-540-24777-7\n    bibtex_key: kellerer2004knapsack\n    category: Theory\n    role: foundation\n    relevance: Definitive reference for multiple-choice knapsack problem (MCKP, Chapter 11). Our per-head bit allocation with hardware-aligned {2,4,8,16} is formulated as MCKP. Greedy optimality conditions and dominance relations from this text underpin our theoretical analysis.\n    abstract: Comprehensive monograph on knapsack problems covering 0-1, bounded, unbounded, subset-sum, change-making, multiple-choice, and multi-dimensional variants. Chapter 11 covers MCKP including dominance, branch-and-bound, dynamic programming, and approximation algorithms.\n    semantic_scholar_id: ''\n    verified: true\n    added_by: literature-survey\n    added_at: '2026-05-14T10:30:00.000Z'\n",
      "numLines": 815,
      "startLine": 1,
      "totalLines": 815
    }
  },
  "sourceToolAssistantUUID": "c020d4be-267f-49cc-b475-b717f4100f40",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "0e163909-e397-4f29-9722-d542e29e1bd1",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 22_

```json
{
  "type": "last-prompt",
  "leafUuid": "26aa19ef-cd1f-4b82-9b52-294f286f7e1a",
  "sessionId": "0e163909-e397-4f29-9722-d542e29e1bd1"
}
```

---

### Runtime record

_source line 23_

```json
{
  "type": "ai-title",
  "aiTitle": "Update literature map with KV cache quantization papers",
  "sessionId": "0e163909-e397-4f29-9722-d542e29e1bd1"
}
```

---

### Assistant

_source line 24 · 2026-05-14T19:06:51.058Z_

<details><summary>Logged reasoning block</summary>

```text
Now I'll apply the edits. I need to:

1. Update meta: total_papers from 35 to 41, last_updated
2. Add KVTuner to Cluster 1 (after kim2024squeezellm, before Cluster 2 comment)
3. Add PM-KVQ to Cluster 1 as well
4. Add KITTY to Cluster 2 (after duanmu2024skvq, before Cluster 3 comment)
5. Add HeadKV to Cluster 3 (after yang2024pyramidinfer, before Cluster 4 comment)


6. Add AdaKV to Cluster 3 as well
7. Add MUXQ to Cluster 4 (after zhao2024atom, before Cluster 5 comment)

Let me double-check the cluster assignments for these papers—KVTuner and PM-KVQ both fit mixed-precision approaches in Cluster 1, KITTY belongs with the quantization methods in Cluster 2, and I'm reconsidering whether HeadKV should go in Cluster 3 with eviction strategies or if it belongs in Cluster 5 with attention head analysis.

Looking at the survey details, HeadKV's focus on head-level importance for eviction decisions places it squarely in Cluster 3. That settles it—AdaKV and HeadKV both go there, and MUXQ fits with model compression in Cluster 4.

Now I need to update the paper counts for each cluster: Cluster 1 grows from 5 to 7, Cluster 2 from 6 to 7, Cluster 3 from 6 to 8, and Cluster 4 from 6 to 7. Since these edits are spread throughout the file and many are sequential, I should plan my edit strategy carefully to ensure each old_string is unique and avoid conflicts.

I can batch the independent changes together—updating the meta information at the top, then refreshing each cluster's comment and adding the new papers right after their respective anchor points. That way I'm working on different sections in parallel without overlap.

I also need to fix KVmix's metadata: change the venue from "arXiv 2025" to "AAAI 2026" and update its role from "method-component" to "direct-competitor" as the user specified.

So my full edit plan is: bump the paper count to 41 and update the timestamp, adjust all four cluster comments to reflect their new sizes, update KVmix's venue and role, then insert the five new papers (KVTuner and PM-KVQ after kim2024squeezellm, KITTY after duanmu2024skvq, HeadKV and AdaKV after yang2024pyramidinfer, and MUXQ after zhao2024atom).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "26aa19ef-cd1f-4b82-9b52-294f286f7e1a",
  "isSidechain": false,
  "requestId": "req_011Cb2z4f4SK9QP27zXBmS8o",
  "type": "assistant",
  "uuid": "8f8aefad-54e7-4b5f-9a7d-4ade42fc072c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "0e163909-e397-4f29-9722-d542e29e1bd1",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AE6EJLgm3YXaeiAeYHPZx1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14690,
      "cache_read_input_tokens": 43378,
      "output_tokens": 1190,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14690,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1190,
          "cache_read_input_tokens": 43378,
          "cache_creation_input_tokens": 14690,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14690
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

_source line 25 · 2026-05-14T19:06:51.059Z_

Now I'll apply all edits. Updating meta, cluster headers, adding 6 new papers, and fixing KVmix metadata.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8f8aefad-54e7-4b5f-9a7d-4ade42fc072c",
  "isSidechain": false,
  "requestId": "req_011Cb2z4f4SK9QP27zXBmS8o",
  "type": "assistant",
  "uuid": "a74d2bfb-ca90-446d-bcd8-c1ead7383272",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "0e163909-e397-4f29-9722-d542e29e1bd1",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AE6EJLgm3YXaeiAeYHPZx1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14690,
      "cache_read_input_tokens": 43378,
      "output_tokens": 1190,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14690,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1190,
          "cache_read_input_tokens": 43378,
          "cache_creation_input_tokens": 14690,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14690
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

_source line 26 · 2026-05-14T19:06:53.117Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01Lp9MbBet4iAbDtqdyjfWjN`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/literature_map.yaml",
  "old_string": "  last_updated: '2026-05-14T10:30:00.000Z'\n  total_papers: 35",
  "new_string": "  last_updated: '2026-05-14T18:00:00.000Z'\n  total_papers: 41"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a74d2bfb-ca90-446d-bcd8-c1ead7383272",
  "isSidechain": false,
  "requestId": "req_011Cb2z4f4SK9QP27zXBmS8o",
  "type": "assistant",
  "uuid": "2d91a4c0-d30f-4557-b20c-a343ff0700da",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "0e163909-e397-4f29-9722-d542e29e1bd1",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AE6EJLgm3YXaeiAeYHPZx1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14690,
      "cache_read_input_tokens": 43378,
      "output_tokens": 1190,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14690,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1190,
          "cache_read_input_tokens": 43378,
          "cache_creation_input_tokens": 14690,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14690
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

_source line 27 · 2026-05-14T19:06:53.145Z_

<details><summary>↩ Tool result · `toolu_01Lp9MbBet4iAbDtqdyjfWjN`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/literature_map.yaml has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2d91a4c0-d30f-4557-b20c-a343ff0700da",
  "isSidechain": false,
  "promptId": "964448b9-9407-4006-b5f8-3afa58950999",
  "type": "user",
  "uuid": "c410605b-55d2-4f1f-bd6e-46c829522459",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/literature_map.yaml",
    "oldString": "  last_updated: '2026-05-14T10:30:00.000Z'\n  total_papers: 35",
    "newString": "  last_updated: '2026-05-14T18:00:00.000Z'\n  total_papers: 41",
    "originalFile": null,
    "structuredPatch": [
      {
        "oldStart": 1,
        "oldLines": 6,
        "newStart": 1,
        "newLines": 6,
        "lines": [
          " meta:",
          "-  last_updated: '2026-05-14T10:30:00.000Z'",
          "-  total_papers: 35",
          "+  last_updated: '2026-05-14T18:00:00.000Z'",
          "+  total_papers: 41",
          " categories:",
          "   - Mixed-Precision Rate-Distortion",
          "   - KV Cache Quantization"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "2d91a4c0-d30f-4557-b20c-a343ff0700da",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "0e163909-e397-4f29-9722-d542e29e1bd1",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-14T19:06:56.726Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01YZcc3SqiQXHQzj1MrHCvoz`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/literature_map.yaml",
  "old_string": "  # Cluster 1: Mixed-Precision R-D Allocation (5 papers)",
  "new_string": "  # Cluster 1: Mixed-Precision R-D Allocation (7 papers)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c410605b-55d2-4f1f-bd6e-46c829522459",
  "isSidechain": false,
  "requestId": "req_011Cb2z6TkbpjSPt6dttLyrJ",
  "type": "assistant",
  "uuid": "9bc04ee8-d226-469a-9eae-81e0a8cd5a83",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "0e163909-e397-4f29-9722-d542e29e1bd1",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JjhExUddExx4mzpX8wA1gG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1257,
      "cache_read_input_tokens": 58068,
      "output_tokens": 782,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1257,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 782,
          "cache_read_input_tokens": 58068,
          "cache_creation_input_tokens": 1257,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1257
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

_source line 29 · 2026-05-14T19:06:56.736Z_

<details><summary>↩ Tool result · `toolu_01YZcc3SqiQXHQzj1MrHCvoz`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/literature_map.yaml has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9bc04ee8-d226-469a-9eae-81e0a8cd5a83",
  "isSidechain": false,
  "promptId": "964448b9-9407-4006-b5f8-3afa58950999",
  "type": "user",
  "uuid": "9848baab-eed1-48c8-bd0e-8e21a5b211d4",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/literature_map.yaml",
    "oldString": "  # Cluster 1: Mixed-Precision R-D Allocation (5 papers)",
    "newString": "  # Cluster 1: Mixed-Precision R-D Allocation (7 papers)",
    "originalFile": null,
    "structuredPatch": [
      {
        "oldStart": 12,
        "oldLines": 7,
        "newStart": 12,
        "newLines": 7,
        "lines": [
          "   - Theory",
          " papers:",
          "   # ============================================================",
          "-  # Cluster 1: Mixed-Precision R-D Allocation (5 papers)",
          "+  # Cluster 1: Mixed-Precision R-D Allocation (7 papers)",
          "   # ============================================================",
          "   zuo2026ratequant:",
          "     title: 'RateQuant: Optimal Mixed-Precision KV Cache Quantization via Rate-Distortion Theory'"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "9bc04ee8-d226-469a-9eae-81e0a8cd5a83",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "0e163909-e397-4f29-9722-d542e29e1bd1",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-14T19:06:58.607Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01YGQvj7RqwRGcek6MyiAbdr`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/literature_map.yaml",
  "old_string": "    venue: arXiv 2025\n    url: ''\n    doi: '2506.08018'\n    bibtex_key: li2025kvmix\n    category: Mixed-Precision Rate-Distortion\n    role: method-component",
  "new_string": "    venue: AAAI 2026\n    url: ''\n    doi: '2506.08018'\n    bibtex_key: li2025kvmix\n    category: Mixed-Precision Rate-Distortion\n    role: direct-competitor"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9848baab-eed1-48c8-bd0e-8e21a5b211d4",
  "isSidechain": false,
  "requestId": "req_011Cb2z6TkbpjSPt6dttLyrJ",
  "type": "assistant",
  "uuid": "3cb230a6-ad0f-44f9-83ab-6c2bc2334c5a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "0e163909-e397-4f29-9722-d542e29e1bd1",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JjhExUddExx4mzpX8wA1gG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1257,
      "cache_read_input_tokens": 58068,
      "output_tokens": 782,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1257,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 782,
          "cache_read_input_tokens": 58068,
          "cache_creation_input_tokens": 1257,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1257
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

_source line 31 · 2026-05-14T19:07:01.735Z_

<details><summary>↩ Tool result · `toolu_015NTZaUQfaVEGXcZpoA2kMB`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/literature_map.yaml has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f215e660-5e90-4289-a09c-63ed1bb5a47f",
  "isSidechain": false,
  "promptId": "964448b9-9407-4006-b5f8-3afa58950999",
  "type": "user",
  "uuid": "180b5f23-94e5-42a1-b079-83ce5ccd0e71",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/literature_map.yaml",
    "oldString": "  # Cluster 4: Model Compression (6 papers)",
    "newString": "  # Cluster 4: Model Compression (7 papers)",
    "originalFile": null,
    "structuredPatch": [
      {
        "oldStart": 408,
        "oldLines": 7,
        "newStart": 408,
        "newLines": 7,
        "lines": [
          "     added_at: '2026-05-14T08:10:15.562Z'",
          " ",
          "   # ============================================================",
          "-  # Cluster 4: Model Compression (6 papers)",
          "+  # Cluster 4: Model Compression (7 papers)",
          "   # ============================================================",
          "   frantar2023gptq:",
          "     title: 'GPTQ: Accurate Post-Training Quantization for Generative Pre-trained Transformers'"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "f215e660-5e90-4289-a09c-63ed1bb5a47f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "0e163909-e397-4f29-9722-d542e29e1bd1",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-14T19:06:58.617Z_

<details><summary>↩ Tool result · `toolu_01YGQvj7RqwRGcek6MyiAbdr`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/literature_map.yaml has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3cb230a6-ad0f-44f9-83ab-6c2bc2334c5a",
  "isSidechain": false,
  "promptId": "964448b9-9407-4006-b5f8-3afa58950999",
  "type": "user",
  "uuid": "1470db3c-7791-419b-995c-5a48c3d1f9db",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/literature_map.yaml",
    "oldString": "    venue: arXiv 2025\n    url: ''\n    doi: '2506.08018'\n    bibtex_key: li2025kvmix\n    category: Mixed-Precision Rate-Distortion\n    role: method-component",
    "newString": "    venue: AAAI 2026\n    url: ''\n    doi: '2506.08018'\n    bibtex_key: li2025kvmix\n    category: Mixed-Precision Rate-Distortion\n    role: direct-competitor",
    "originalFile": null,
    "structuredPatch": [
      {
        "oldStart": 62,
        "oldLines": 12,
        "newStart": 62,
        "newLines": 12,
        "lines": [
          "     - Shiqiang Nie",
          "     - Jinyu Wang",
          "     year: 2025",
          "-    venue: arXiv 2025",
          "+    venue: AAAI 2026",
          "     url: ''",
          "     doi: '2506.08018'",
          "     bibtex_key: li2025kvmix",
          "     category: Mixed-Precision Rate-Distortion",
          "-    role: method-component",
          "+    role: direct-competitor",
          "     relevance: Gradient-based importance for layer-wise KV cache bit-width allocation. Heuristic sensitivity-based approach vs our R-D optimal formulation. Achieves near-lossless at Key 2.19bit / Value 2.38bit.",
          "     abstract: KVmix employs gradient-based importance analysis to evaluate how individual Key and Value projection matrices affect model loss, enabling layer-specific bit-width allocation. Includes dynamic long-context optimization preserving full-precision KV pairs for recent pivotal tokens.",
          "     semantic_scholar_id: ''"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "3cb230a6-ad0f-44f9-83ab-6c2bc2334c5a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "0e163909-e397-4f29-9722-d542e29e1bd1",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-14T19:07:00.090Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01Xy2uN7pTRHSXB8nj4iknWy`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/literature_map.yaml",
  "old_string": "  # Cluster 2: KV Cache Quantization (6 papers)",
  "new_string": "  # Cluster 2: KV Cache Quantization (7 papers)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1470db3c-7791-419b-995c-5a48c3d1f9db",
  "isSidechain": false,
  "requestId": "req_011Cb2z6TkbpjSPt6dttLyrJ",
  "type": "assistant",
  "uuid": "7b3c84e6-06ed-4483-b730-59691508f88e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "0e163909-e397-4f29-9722-d542e29e1bd1",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JjhExUddExx4mzpX8wA1gG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1257,
      "cache_read_input_tokens": 58068,
      "output_tokens": 782,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1257,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 782,
          "cache_read_input_tokens": 58068,
          "cache_creation_input_tokens": 1257,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1257
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

_source line 34 · 2026-05-14T19:07:00.102Z_

<details><summary>↩ Tool result · `toolu_01Xy2uN7pTRHSXB8nj4iknWy`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/literature_map.yaml has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7b3c84e6-06ed-4483-b730-59691508f88e",
  "isSidechain": false,
  "promptId": "964448b9-9407-4006-b5f8-3afa58950999",
  "type": "user",
  "uuid": "dd038372-fda2-4bcc-9d83-8e9dca4f9a8c",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/literature_map.yaml",
    "oldString": "  # Cluster 2: KV Cache Quantization (6 papers)",
    "newString": "  # Cluster 2: KV Cache Quantization (7 papers)",
    "originalFile": null,
    "structuredPatch": [
      {
        "oldStart": 121,
        "oldLines": 7,
        "newStart": 121,
        "newLines": 7,
        "lines": [
          "     added_at: '2026-05-14T08:42:26.710Z'",
          " ",
          "   # ============================================================",
          "-  # Cluster 2: KV Cache Quantization (6 papers)",
          "+  # Cluster 2: KV Cache Quantization (7 papers)",
          "   # ============================================================",
          "   liu2024kivi:",
          "     title: 'KIVI: A Tuning-Free Asymmetric 2bit Quantization for KV Cache'"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "7b3c84e6-06ed-4483-b730-59691508f88e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "0e163909-e397-4f29-9722-d542e29e1bd1",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-14T19:07:00.961Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01VGaP46tQpsEm2P7aFMgioi`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/literature_map.yaml",
  "old_string": "  # Cluster 3: KV Cache Eviction (6 papers)",
  "new_string": "  # Cluster 3: KV Cache Eviction (8 papers)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dd038372-fda2-4bcc-9d83-8e9dca4f9a8c",
  "isSidechain": false,
  "requestId": "req_011Cb2z6TkbpjSPt6dttLyrJ",
  "type": "assistant",
  "uuid": "2ab141a4-5bd3-4a0d-b2e8-6952d99b5669",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "0e163909-e397-4f29-9722-d542e29e1bd1",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JjhExUddExx4mzpX8wA1gG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1257,
      "cache_read_input_tokens": 58068,
      "output_tokens": 782,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1257,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 782,
          "cache_read_input_tokens": 58068,
          "cache_creation_input_tokens": 1257,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1257
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

_source line 36 · 2026-05-14T19:07:00.981Z_

<details><summary>↩ Tool result · `toolu_01VGaP46tQpsEm2P7aFMgioi`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/literature_map.yaml has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2ab141a4-5bd3-4a0d-b2e8-6952d99b5669",
  "isSidechain": false,
  "promptId": "964448b9-9407-4006-b5f8-3afa58950999",
  "type": "user",
  "uuid": "62428db8-c2c8-44f8-8785-a6bfe05f79d4",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/literature_map.yaml",
    "oldString": "  # Cluster 3: KV Cache Eviction (6 papers)",
    "newString": "  # Cluster 3: KV Cache Eviction (8 papers)",
    "originalFile": null,
    "structuredPatch": [
      {
        "oldStart": 262,
        "oldLines": 7,
        "newStart": 262,
        "newLines": 7,
        "lines": [
          "     added_at: '2026-05-14T07:56:45.265Z'",
          " ",
          "   # ============================================================",
          "-  # Cluster 3: KV Cache Eviction (6 papers)",
          "+  # Cluster 3: KV Cache Eviction (8 papers)",
          "   # ============================================================",
          "   zhang2023h2o:",
          "     title: 'H2O: Heavy-Hitter Oracle for Efficient Generative Inference of Large Language Models'"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "2ab141a4-5bd3-4a0d-b2e8-6952d99b5669",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "0e163909-e397-4f29-9722-d542e29e1bd1",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-14T19:07:01.722Z_

<details open><summary>🔧 Tool call — Edit · `toolu_015NTZaUQfaVEGXcZpoA2kMB`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/literature_map.yaml",
  "old_string": "  # Cluster 4: Model Compression (6 papers)",
  "new_string": "  # Cluster 4: Model Compression (7 papers)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "62428db8-c2c8-44f8-8785-a6bfe05f79d4",
  "isSidechain": false,
  "requestId": "req_011Cb2z6TkbpjSPt6dttLyrJ",
  "type": "assistant",
  "uuid": "f215e660-5e90-4289-a09c-63ed1bb5a47f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "0e163909-e397-4f29-9722-d542e29e1bd1",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JjhExUddExx4mzpX8wA1gG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1257,
      "cache_read_input_tokens": 58068,
      "output_tokens": 782,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1257,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 782,
          "cache_read_input_tokens": 58068,
          "cache_creation_input_tokens": 1257,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1257
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

_source line 38 · 2026-05-14T19:07:01.788Z_

```json
{
  "parentUuid": "180b5f23-94e5-42a1-b079-83ce5ccd0e71",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "c05a7ca0-0ef5-45be-8feb-a31db8d46f69",
  "timestamp": "2026-05-14T19:07:01.788Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "0e163909-e397-4f29-9722-d542e29e1bd1",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Assistant

_source line 39 · 2026-05-14T19:07:04.339Z_

Now adding the 6 new paper entries.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c05a7ca0-0ef5-45be-8feb-a31db8d46f69",
  "isSidechain": false,
  "requestId": "req_011Cb2z768s6n4Br7fB6Kqhp",
  "type": "assistant",
  "uuid": "1d41be10-920f-483c-950a-7edc85cb4168",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "0e163909-e397-4f29-9722-d542e29e1bd1",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EtnJBJLMJMJ6iH4bXqBSNG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1294,
      "cache_read_input_tokens": 59325,
      "output_tokens": 821,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1294,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 821,
          "cache_read_input_tokens": 59325,
          "cache_creation_input_tokens": 1294,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1294
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

_source line 40 · 2026-05-14T19:07:17.023Z_

<details open><summary>🔧 Tool call — Edit · `toolu_016uQirt1ToyWFJczi382k9y`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/literature_map.yaml",
  "old_string": "    added_at: '2026-05-14T08:42:26.710Z'\n\n  # ============================================================\n  # Cluster 2: KV Cache Quantization (7 papers)",
  "new_string": "    added_at: '2026-05-14T08:42:26.710Z'\n  li2025kvtuner:\n    title: 'KVTuner: Sensitivity-Aware Layer-Wise Mixed-Precision KV Cache Quantization for Efficient and Nearly Lossless LLM Inference'\n    authors:\n    - Li et al.\n    year: 2025\n    venue: ICML 2025\n    url: ''\n    doi: ''\n    bibtex_key: li2025kvtuner\n    category: Mixed-Precision Rate-Distortion\n    role: direct-competitor\n    relevance: Layer-level mixed-precision KV cache via Pareto search over hardware-friendly precision pairs. Achieves nearly lossless 3.25-bit for Llama-3.1-8B. Operates at layer granularity vs our head granularity.\n    abstract: KVTuner uses Pareto search over hardware-friendly layer-wise K/V precision pairs. Gradient-based sensitivity shows U-shaped pattern (early+late layers sensitive). Achieves nearly lossless compression at 3.25-bit for Llama-3.1-8B and 4.0-bit for Qwen2.5-7B.\n    semantic_scholar_id: ''\n    verified: true\n    added_by: literature-survey\n    added_at: '2026-05-14T18:00:00.000Z'\n  chen2025pmkvq:\n    title: 'PM-KVQ: Progressive Mixed-Precision KV Cache Quantization for Long-CoT LLMs'\n    authors:\n    - Chen et al.\n    year: 2025\n    venue: arXiv 2025\n    url: ''\n    doi: '2505.18610'\n    bibtex_key: chen2025pmkvq\n    category: Mixed-Precision Rate-Distortion\n    role: method-component\n    relevance: Progressive quantization that gradually lowers bit-width over decoding steps. Temporal dimension orthogonal to our spatial (per-head) allocation. Uses integer programming for block-wise memory allocation.\n    abstract: PM-KVQ introduces a progressive quantization strategy that gradually lowers bit-width over decoding steps. Block-wise memory allocation assigns higher bits to sensitive transformer blocks via integer programming.\n    semantic_scholar_id: ''\n    verified: true\n    added_by: literature-survey\n    added_at: '2026-05-14T18:00:00.000Z'\n\n  # ============================================================\n  # Cluster 2: KV Cache Quantization (7 papers)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1d41be10-920f-483c-950a-7edc85cb4168",
  "isSidechain": false,
  "requestId": "req_011Cb2z768s6n4Br7fB6Kqhp",
  "type": "assistant",
  "uuid": "572a6f18-12ef-4ee4-8949-d41698369ea2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "0e163909-e397-4f29-9722-d542e29e1bd1",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EtnJBJLMJMJ6iH4bXqBSNG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1294,
      "cache_read_input_tokens": 59325,
      "output_tokens": 821,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1294,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 821,
          "cache_read_input_tokens": 59325,
          "cache_creation_input_tokens": 1294,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1294
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

_source line 41 · 2026-05-14T19:07:17.059Z_

<details><summary>↩ Tool result · `toolu_016uQirt1ToyWFJczi382k9y`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/literature_map.yaml has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "572a6f18-12ef-4ee4-8949-d41698369ea2",
  "isSidechain": false,
  "promptId": "964448b9-9407-4006-b5f8-3afa58950999",
  "type": "user",
  "uuid": "5a3598f9-13a4-49a3-b905-b1c5c9b631a3",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/literature_map.yaml",
    "oldString": "    added_at: '2026-05-14T08:42:26.710Z'\n\n  # ============================================================\n  # Cluster 2: KV Cache Quantization (7 papers)",
    "newString": "    added_at: '2026-05-14T08:42:26.710Z'\n  li2025kvtuner:\n    title: 'KVTuner: Sensitivity-Aware Layer-Wise Mixed-Precision KV Cache Quantization for Efficient and Nearly Lossless LLM Inference'\n    authors:\n    - Li et al.\n    year: 2025\n    venue: ICML 2025\n    url: ''\n    doi: ''\n    bibtex_key: li2025kvtuner\n    category: Mixed-Precision Rate-Distortion\n    role: direct-competitor\n    relevance: Layer-level mixed-precision KV cache via Pareto search over hardware-friendly precision pairs. Achieves nearly lossless 3.25-bit for Llama-3.1-8B. Operates at layer granularity vs our head granularity.\n    abstract: KVTuner uses Pareto search over hardware-friendly layer-wise K/V precision pairs. Gradient-based sensitivity shows U-shaped pattern (early+late layers sensitive). Achieves nearly lossless compression at 3.25-bit for Llama-3.1-8B and 4.0-bit for Qwen2.5-7B.\n    semantic_scholar_id: ''\n    verified: true\n    added_by: literature-survey\n    added_at: '2026-05-14T18:00:00.000Z'\n  chen2025pmkvq:\n    title: 'PM-KVQ: Progressive Mixed-Precision KV Cache Quantization for Long-CoT LLMs'\n    authors:\n    - Chen et al.\n    year: 2025\n    venue: arXiv 2025\n    url: ''\n    doi: '2505.18610'\n    bibtex_key: chen2025pmkvq\n    category: Mixed-Precision Rate-Distortion\n    role: method-component\n    relevance: Progressive quantization that gradually lowers bit-width over decoding steps. Temporal dimension orthogonal to our spatial (per-head) allocation. Uses integer programming for block-wise memory allocation.\n    abstract: PM-KVQ introduces a progressive quantization strategy that gradually lowers bit-width over decoding steps. Block-wise memory allocation assigns higher bits to sensitive transformer blocks via integer programming.\n    semantic_scholar_id: ''\n    verified: true\n    added_by: literature-survey\n    added_at: '2026-05-14T18:00:00.000Z'\n\n  # ============================================================\n  # Cluster 2: KV Cache Quantization (7 papers)",
    "originalFile": null,
    "structuredPatch": [
      {
        "oldStart": 119,
        "oldLines": 6,
        "newStart": 119,
        "newLines": 40,
        "lines": [
          "     verified: true",
          "     added_by: paper-research",
          "     added_at: '2026-05-14T08:42:26.710Z'",
          "+  li2025kvtuner:",
          "+    title: 'KVTuner: Sensitivity-Aware Layer-Wise Mixed-Precision KV Cache Quantization for Efficient and Nearly Lossless LLM Inference'",
          "+    authors:",
          "+    - Li et al.",
          "+    year: 2025",
          "+    venue: ICML 2025",
          "+    url: ''",
          "+    doi: ''",
          "+    bibtex_key: li2025kvtuner",
          "+    category: Mixed-Precision Rate-Distortion",
          "+    role: direct-competitor",
          "+    relevance: Layer-level mixed-precision KV cache via Pareto search over hardware-friendly precision pairs. Achieves nearly lossless 3.25-bit for Llama-3.1-8B. Operates at layer granularity vs our head granularity.",
          "+    abstract: KVTuner uses Pareto search over hardware-friendly layer-wise K/V precision pairs. Gradient-based sensitivity shows U-shaped pattern (early+late layers sensitive). Achieves nearly lossless compression at 3.25-bit for Llama-3.1-8B and 4.0-bit for Qwen2.5-7B.",
          "+    semantic_scholar_id: ''",
          "+    verified: true",
          "+    added_by: literature-survey",
          "+    added_at: '2026-05-14T18:00:00.000Z'",
          "+  chen2025pmkvq:",
          "+    title: 'PM-KVQ: Progressive Mixed-Precision KV Cache Quantization for Long-CoT LLMs'",
          "+    authors:",
          "+    - Chen et al.",
          "+    year: 2025",
          "+    venue: arXiv 2025",
          "+    url: ''",
          "+    doi: '2505.18610'",
          "+    bibtex_key: chen2025pmkvq",
          "+    category: Mixed-Precision Rate-Distortion",
          "+    role: method-component",
          "+    relevance: Progressive quantization that gradually lowers bit-width over decoding steps. Temporal dimension orthogonal to our spatial (per-head) allocation. Uses integer programming for block-wise memory allocation.",
          "+    abstract: PM-KVQ introduces a progressive quantization strategy that gradually lowers bit-width over decoding steps. Block-wise memory allocation assigns higher bits to sensitive transformer blocks via integer programming.",
          "+    semantic_scholar_id: ''",
          "+    verified: true",
          "+    added_by: literature-survey",
          "+    added_at: '2026-05-14T18:00:00.000Z'",
          " ",
          "   # ============================================================",
          "   # Cluster 2: KV Cache Quantization (7 papers)"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "572a6f18-12ef-4ee4-8949-d41698369ea2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "0e163909-e397-4f29-9722-d542e29e1bd1",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 42_

```json
{
  "type": "last-prompt",
  "leafUuid": "5a3598f9-13a4-49a3-b905-b1c5c9b631a3",
  "sessionId": "0e163909-e397-4f29-9722-d542e29e1bd1"
}
```

---

### Runtime record

_source line 43_

```json
{
  "type": "ai-title",
  "aiTitle": "Update literature map with KV cache quantization papers",
  "sessionId": "0e163909-e397-4f29-9722-d542e29e1bd1"
}
```

---

### Tool call

_source line 44 · 2026-05-14T19:07:26.534Z_

<details open><summary>🔧 Tool call — Edit · `toolu_0182vE8fe3MdrCiMY4DByy4H`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/literature_map.yaml",
  "old_string": "    added_at: '2026-05-14T07:56:45.265Z'\n\n  # ============================================================\n  # Cluster 3: KV Cache Eviction (8 papers)",
  "new_string": "    added_at: '2026-05-14T07:56:45.265Z'\n  li2025kitty:\n    title: 'Kitty: Accurate and Efficient 2-bit KV Cache Quantization with Dynamic Channel-wise Precision Boost'\n    authors:\n    - Li et al.\n    year: 2025\n    venue: arXiv 2025\n    url: ''\n    doi: '2511.18643'\n    bibtex_key: li2025kitty\n    category: KV Cache Quantization\n    role: background\n    relevance: Channel-wise precision boost for Key cache. Ranks channels by sensitivity and keeps critical fraction at higher precision. Decomposes mixed-precision pages into two uniform 2-bit tensors for hardware efficiency.\n    abstract: KITTY achieves accurate 2-bit KV cache quantization by dynamically boosting critical Key channels to higher precision. Decomposes mixed-precision Key pages into two uniform 2-bit tensors, enabling efficient hardware implementation without custom kernels.\n    semantic_scholar_id: ''\n    verified: true\n    added_by: literature-survey\n    added_at: '2026-05-14T18:00:00.000Z'\n\n  # ============================================================\n  # Cluster 3: KV Cache Eviction (8 papers)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5a3598f9-13a4-49a3-b905-b1c5c9b631a3",
  "isSidechain": false,
  "requestId": "req_011Cb2z8DUuruvbH9meXtvur",
  "type": "assistant",
  "uuid": "aad237b9-d903-4de8-9e38-3b7aef059a97",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "0e163909-e397-4f29-9722-d542e29e1bd1",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NGgsKpomCfZGP1ndnRH9A1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 870,
      "cache_read_input_tokens": 60619,
      "output_tokens": 498,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 870,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 498,
          "cache_read_input_tokens": 60619,
          "cache_creation_input_tokens": 870,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 870
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

_source line 45 · 2026-05-14T19:07:26.552Z_

<details><summary>↩ Tool result · `toolu_0182vE8fe3MdrCiMY4DByy4H`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/literature_map.yaml has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "aad237b9-d903-4de8-9e38-3b7aef059a97",
  "isSidechain": false,
  "promptId": "964448b9-9407-4006-b5f8-3afa58950999",
  "type": "user",
  "uuid": "8dd27786-f53d-40f9-af68-d5a304e1e742",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/literature_map.yaml",
    "oldString": "    added_at: '2026-05-14T07:56:45.265Z'\n\n  # ============================================================\n  # Cluster 3: KV Cache Eviction (8 papers)",
    "newString": "    added_at: '2026-05-14T07:56:45.265Z'\n  li2025kitty:\n    title: 'Kitty: Accurate and Efficient 2-bit KV Cache Quantization with Dynamic Channel-wise Precision Boost'\n    authors:\n    - Li et al.\n    year: 2025\n    venue: arXiv 2025\n    url: ''\n    doi: '2511.18643'\n    bibtex_key: li2025kitty\n    category: KV Cache Quantization\n    role: background\n    relevance: Channel-wise precision boost for Key cache. Ranks channels by sensitivity and keeps critical fraction at higher precision. Decomposes mixed-precision pages into two uniform 2-bit tensors for hardware efficiency.\n    abstract: KITTY achieves accurate 2-bit KV cache quantization by dynamically boosting critical Key channels to higher precision. Decomposes mixed-precision Key pages into two uniform 2-bit tensors, enabling efficient hardware implementation without custom kernels.\n    semantic_scholar_id: ''\n    verified: true\n    added_by: literature-survey\n    added_at: '2026-05-14T18:00:00.000Z'\n\n  # ============================================================\n  # Cluster 3: KV Cache Eviction (8 papers)",
    "originalFile": null,
    "structuredPatch": [
      {
        "oldStart": 294,
        "oldLines": 6,
        "newStart": 294,
        "newLines": 23,
        "lines": [
          "     verified: true",
          "     added_by: paper-research",
          "     added_at: '2026-05-14T07:56:45.265Z'",
          "+  li2025kitty:",
          "+    title: 'Kitty: Accurate and Efficient 2-bit KV Cache Quantization with Dynamic Channel-wise Precision Boost'",
          "+    authors:",
          "+    - Li et al.",
          "+    year: 2025",
          "+    venue: arXiv 2025",
          "+    url: ''",
          "+    doi: '2511.18643'",
          "+    bibtex_key: li2025kitty",
          "+    category: KV Cache Quantization",
          "+    role: background",
          "+    relevance: Channel-wise precision boost for Key cache. Ranks channels by sensitivity and keeps critical fraction at higher precision. Decomposes mixed-precision pages into two uniform 2-bit tensors for hardware efficiency.",
          "+    abstract: KITTY achieves accurate 2-bit KV cache quantization by dynamically boosting critical Key channels to higher precision. Decomposes mixed-precision Key pages into two uniform 2-bit tensors, enabling efficient hardware implementation without custom kernels.",
          "+    semantic_scholar_id: ''",
          "+    verified: true",
          "+    added_by: literature-survey",
          "+    added_at: '2026-05-14T18:00:00.000Z'",
          " ",
          "   # ============================================================",
          "   # Cluster 3: KV Cache Eviction (8 papers)"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "aad237b9-d903-4de8-9e38-3b7aef059a97",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "0e163909-e397-4f29-9722-d542e29e1bd1",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 46 · 2026-05-14T19:07:39.813Z_

<details open><summary>🔧 Tool call — Edit · `toolu_018hRSi4vaNkgmKEKiFHy3BK`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/literature_map.yaml",
  "old_string": "    added_at: '2026-05-14T08:10:15.562Z'\n\n  # ============================================================\n  # Cluster 4: Model Compression (7 papers)",
  "new_string": "    added_at: '2026-05-14T08:10:15.562Z'\n  fu2025headkv:\n    title: 'Not All Heads Matter: A Head-Level KV Cache Compression Method with Integrated Retrieval and Reasoning'\n    authors:\n    - Fu et al.\n    year: 2025\n    venue: ICLR 2025\n    url: ''\n    doi: '2410.19258'\n    bibtex_key: fu2025headkv\n    category: KV Cache Eviction\n    role: background\n    relevance: Head-level KV cache budget allocation for eviction based on importance scores from Needle-in-a-Haystack probing. Confirms head-level importance heterogeneity is exploitable. Eviction-based, not quantization-based.\n    abstract: HeadKV allocates KV cache budgets at the head level based on importance scores derived from Needle-in-a-Haystack probing. Different heads serve retrieval vs reasoning roles. Retains 1.5% KV cache with 97% performance preservation.\n    semantic_scholar_id: ''\n    verified: true\n    added_by: literature-survey\n    added_at: '2026-05-14T18:00:00.000Z'\n  feng2025adakv:\n    title: 'Ada-KV: Optimizing KV Cache Eviction by Adaptive Budget Allocation'\n    authors:\n    - Feng et al.\n    year: 2025\n    venue: NeurIPS 2025\n    url: ''\n    doi: '2407.11550'\n    bibtex_key: feng2025adakv\n    category: KV Cache Eviction\n    role: background\n    relevance: Adaptive per-head budget allocation for KV eviction. Key insight that uniform compression rate across heads is a rigidity that hurts performance. Supports our thesis that head-level heterogeneity matters.\n    abstract: Ada-KV extends SnapKV/PyramidKV with head-wise adaptive budget allocation for KV cache eviction. Shows that uniform compression rate across attention heads is suboptimal and adaptive per-head allocation significantly improves long-context performance.\n    semantic_scholar_id: ''\n    verified: true\n    added_by: literature-survey\n    added_at: '2026-05-14T18:00:00.000Z'\n\n  # ============================================================\n  # Cluster 4: Model Compression (7 papers)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8dd27786-f53d-40f9-af68-d5a304e1e742",
  "isSidechain": false,
  "requestId": "req_011Cb2z8v7B6r62Y87rxDzEw",
  "type": "assistant",
  "uuid": "9de95f24-0b80-4471-8859-61dc6b7b457f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "0e163909-e397-4f29-9722-d542e29e1bd1",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RJqUZ77AehfMNgr2kyH8Xg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 547,
      "cache_read_input_tokens": 61489,
      "output_tokens": 775,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 547,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 775,
          "cache_read_input_tokens": 61489,
          "cache_creation_input_tokens": 547,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 547
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

_source line 47 · 2026-05-14T19:07:39.853Z_

<details><summary>↩ Tool result · `toolu_018hRSi4vaNkgmKEKiFHy3BK`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/literature_map.yaml has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9de95f24-0b80-4471-8859-61dc6b7b457f",
  "isSidechain": false,
  "promptId": "964448b9-9407-4006-b5f8-3afa58950999",
  "type": "user",
  "uuid": "35703631-2514-4de1-b2dc-48fac68168cf",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/literature_map.yaml",
    "oldString": "    added_at: '2026-05-14T08:10:15.562Z'\n\n  # ============================================================\n  # Cluster 4: Model Compression (7 papers)",
    "newString": "    added_at: '2026-05-14T08:10:15.562Z'\n  fu2025headkv:\n    title: 'Not All Heads Matter: A Head-Level KV Cache Compression Method with Integrated Retrieval and Reasoning'\n    authors:\n    - Fu et al.\n    year: 2025\n    venue: ICLR 2025\n    url: ''\n    doi: '2410.19258'\n    bibtex_key: fu2025headkv\n    category: KV Cache Eviction\n    role: background\n    relevance: Head-level KV cache budget allocation for eviction based on importance scores from Needle-in-a-Haystack probing. Confirms head-level importance heterogeneity is exploitable. Eviction-based, not quantization-based.\n    abstract: HeadKV allocates KV cache budgets at the head level based on importance scores derived from Needle-in-a-Haystack probing. Different heads serve retrieval vs reasoning roles. Retains 1.5% KV cache with 97% performance preservation.\n    semantic_scholar_id: ''\n    verified: true\n    added_by: literature-survey\n    added_at: '2026-05-14T18:00:00.000Z'\n  feng2025adakv:\n    title: 'Ada-KV: Optimizing KV Cache Eviction by Adaptive Budget Allocation'\n    authors:\n    - Feng et al.\n    year: 2025\n    venue: NeurIPS 2025\n    url: ''\n    doi: '2407.11550'\n    bibtex_key: feng2025adakv\n    category: KV Cache Eviction\n    role: background\n    relevance: Adaptive per-head budget allocation for KV eviction. Key insight that uniform compression rate across heads is a rigidity that hurts performance. Supports our thesis that head-level heterogeneity matters.\n    abstract: Ada-KV extends SnapKV/PyramidKV with head-wise adaptive budget allocation for KV cache eviction. Shows that uniform compression rate across attention heads is suboptimal and adaptive per-head allocation significantly improves long-context performance.\n    semantic_scholar_id: ''\n    verified: true\n    added_by: literature-survey\n    added_at: '2026-05-14T18:00:00.000Z'\n\n  # ============================================================\n  # Cluster 4: Model Compression (7 papers)",
    "originalFile": null,
    "structuredPatch": [
      {
        "oldStart": 457,
        "oldLines": 6,
        "newStart": 457,
        "newLines": 40,
        "lines": [
          "     verified: true",
          "     added_by: paper-research",
          "     added_at: '2026-05-14T08:10:15.562Z'",
          "+  fu2025headkv:",
          "+    title: 'Not All Heads Matter: A Head-Level KV Cache Compression Method with Integrated Retrieval and Reasoning'",
          "+    authors:",
          "+    - Fu et al.",
          "+    year: 2025",
          "+    venue: ICLR 2025",
          "+    url: ''",
          "+    doi: '2410.19258'",
          "+    bibtex_key: fu2025headkv",
          "+    category: KV Cache Eviction",
          "+    role: background",
          "+    relevance: Head-level KV cache budget allocation for eviction based on importance scores from Needle-in-a-Haystack probing. Confirms head-level importance heterogeneity is exploitable. Eviction-based, not quantization-based.",
          "+    abstract: HeadKV allocates KV cache budgets at the head level based on importance scores derived from Needle-in-a-Haystack probing. Different heads serve retrieval vs reasoning roles. Retains 1.5% KV cache with 97% performance preservation.",
          "+    semantic_scholar_id: ''",
          "+    verified: true",
          "+    added_by: literature-survey",
          "+    added_at: '2026-05-14T18:00:00.000Z'",
          "+  feng2025adakv:",
          "+    title: 'Ada-KV: Optimizing KV Cache Eviction by Adaptive Budget Allocation'",
          "+    authors:",
          "+    - Feng et al.",
          "+    year: 2025",
          "+    venue: NeurIPS 2025",
          "+    url: ''",
          "+    doi: '2407.11550'",
          "+    bibtex_key: feng2025adakv",
          "+    category: KV Cache Eviction",
          "+    role: background",
          "+    relevance: Adaptive per-head budget allocation for KV eviction. Key insight that uniform compression rate across heads is a rigidity that hurts performance. Supports our thesis that head-level heterogeneity matters.",
          "+    abstract: Ada-KV extends SnapKV/PyramidKV with head-wise adaptive budget allocation for KV cache eviction. Shows that uniform compression rate across attention heads is suboptimal and adaptive per-head allocation significantly improves long-context performance.",
          "+    semantic_scholar_id: ''",
          "+    verified: true",
          "+    added_by: literature-survey",
          "+    added_at: '2026-05-14T18:00:00.000Z'",
          " ",
          "   # ============================================================",
          "   # Cluster 4: Model Compression (7 papers)"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "9de95f24-0b80-4471-8859-61dc6b7b457f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "0e163909-e397-4f29-9722-d542e29e1bd1",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 48 · 2026-05-14T19:07:52.844Z_

<details open><summary>🔧 Tool call — Edit · `toolu_013xMfAfchS3Aej5Zz3BCzR8`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/literature_map.yaml",
  "old_string": "    added_at: '2026-05-14T10:30:00.000Z'\n\n  # ============================================================\n  # Cluster 5: Attention Head Analysis (4 papers)",
  "new_string": "    added_at: '2026-05-14T10:30:00.000Z'\n  chen2026muxq:\n    title: 'MUXQ: Mixed-to-Uniform Precision Matrix Quantization via Low-Rank Outlier Decomposition'\n    authors:\n    - Chen et al.\n    year: 2026\n    venue: arXiv 2026\n    url: ''\n    doi: '2604.04701'\n    bibtex_key: chen2026muxq\n    category: Model Compression\n    role: background\n    relevance: Decomposes outlier channels into low-rank matrix to convert mixed-precision into uniform precision. Opposite philosophy to ours — eliminates heterogeneity (smoothing) vs exploiting it (our approach).\n    abstract: MUXQ decomposes outlier channels into a low-rank matrix, converting mixed-precision quantization into uniform precision. Applies rotation and permutation to redistribute outlier energy, enabling efficient uniform-precision hardware execution.\n    semantic_scholar_id: ''\n    verified: true\n    added_by: literature-survey\n    added_at: '2026-05-14T18:00:00.000Z'\n\n  # ============================================================\n  # Cluster 5: Attention Head Analysis (4 papers)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "35703631-2514-4de1-b2dc-48fac68168cf",
  "isSidechain": false,
  "requestId": "req_011Cb2z9tzjB5j55PMfcKc4k",
  "type": "assistant",
  "uuid": "31652190-535d-457b-8e4b-07454f76d40d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "0e163909-e397-4f29-9722-d542e29e1bd1",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MfNNxFZX1UAD5BUqjrKxo5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 824,
      "cache_read_input_tokens": 62036,
      "output_tokens": 488,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 824,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 488,
          "cache_read_input_tokens": 62036,
          "cache_creation_input_tokens": 824,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 824
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

_source line 49 · 2026-05-14T19:07:52.864Z_

<details><summary>↩ Tool result · `toolu_013xMfAfchS3Aej5Zz3BCzR8`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/literature_map.yaml has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "31652190-535d-457b-8e4b-07454f76d40d",
  "isSidechain": false,
  "promptId": "964448b9-9407-4006-b5f8-3afa58950999",
  "type": "user",
  "uuid": "033a41fe-ea6c-46cd-be69-2b40ce9fc9b7",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/literature_map.yaml",
    "oldString": "    added_at: '2026-05-14T10:30:00.000Z'\n\n  # ============================================================\n  # Cluster 5: Attention Head Analysis (4 papers)",
    "newString": "    added_at: '2026-05-14T10:30:00.000Z'\n  chen2026muxq:\n    title: 'MUXQ: Mixed-to-Uniform Precision Matrix Quantization via Low-Rank Outlier Decomposition'\n    authors:\n    - Chen et al.\n    year: 2026\n    venue: arXiv 2026\n    url: ''\n    doi: '2604.04701'\n    bibtex_key: chen2026muxq\n    category: Model Compression\n    role: background\n    relevance: Decomposes outlier channels into low-rank matrix to convert mixed-precision into uniform precision. Opposite philosophy to ours — eliminates heterogeneity (smoothing) vs exploiting it (our approach).\n    abstract: MUXQ decomposes outlier channels into a low-rank matrix, converting mixed-precision quantization into uniform precision. Applies rotation and permutation to redistribute outlier energy, enabling efficient uniform-precision hardware execution.\n    semantic_scholar_id: ''\n    verified: true\n    added_by: literature-survey\n    added_at: '2026-05-14T18:00:00.000Z'\n\n  # ============================================================\n  # Cluster 5: Attention Head Analysis (4 papers)",
    "originalFile": null,
    "structuredPatch": [
      {
        "oldStart": 630,
        "oldLines": 6,
        "newStart": 630,
        "newLines": 23,
        "lines": [
          "     verified: true",
          "     added_by: literature-survey",
          "     added_at: '2026-05-14T10:30:00.000Z'",
          "+  chen2026muxq:",
          "+    title: 'MUXQ: Mixed-to-Uniform Precision Matrix Quantization via Low-Rank Outlier Decomposition'",
          "+    authors:",
          "+    - Chen et al.",
          "+    year: 2026",
          "+    venue: arXiv 2026",
          "+    url: ''",
          "+    doi: '2604.04701'",
          "+    bibtex_key: chen2026muxq",
          "+    category: Model Compression",
          "+    role: background",
          "+    relevance: Decomposes outlier channels into low-rank matrix to convert mixed-precision into uniform precision. Opposite philosophy to ours — eliminates heterogeneity (smoothing) vs exploiting it (our approach).",
          "+    abstract: MUXQ decomposes outlier channels into a low-rank matrix, converting mixed-precision quantization into uniform precision. Applies rotation and permutation to redistribute outlier energy, enabling efficient uniform-precision hardware execution.",
          "+    semantic_scholar_id: ''",
          "+    verified: true",
          "+    added_by: literature-survey",
          "+    added_at: '2026-05-14T18:00:00.000Z'",
          " ",
          "   # ============================================================",
          "   # Cluster 5: Attention Head Analysis (4 papers)"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "31652190-535d-457b-8e4b-07454f76d40d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "0e163909-e397-4f29-9722-d542e29e1bd1",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 50 · 2026-05-14T19:07:56.148Z_

Let me verify the final file is valid YAML.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "033a41fe-ea6c-46cd-be69-2b40ce9fc9b7",
  "isSidechain": false,
  "requestId": "req_011Cb2zAs5Ag3hMNoU8M7j97",
  "type": "assistant",
  "uuid": "a9890ece-2193-4111-81d4-1600f74cd9bf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "0e163909-e397-4f29-9722-d542e29e1bd1",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KtQSHpwGCa1EvmdpkKb5GD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 537,
      "cache_read_input_tokens": 62860,
      "output_tokens": 220,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 537,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 220,
          "cache_read_input_tokens": 62860,
          "cache_creation_input_tokens": 537,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 537
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

_source line 51 · 2026-05-14T19:07:58.561Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01DYDYYcv5Xgrpa2tfHCpZSU`</summary>

```json
{
  "command": "python3 -c \"import yaml; data = yaml.safe_load(open('/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/literature_map.yaml')); print(f'total_papers: {data[\\\"meta\\\"][\\\"total_papers\\\"]}'); print(f'actual papers: {len(data[\\\"papers\\\"])}'); new = [k for k in data['papers'] if '18:00' in data['papers'][k].get('added_at','')]; print(f'new entries: {new}')\"",
  "description": "Validate YAML and count papers"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a9890ece-2193-4111-81d4-1600f74cd9bf",
  "isSidechain": false,
  "requestId": "req_011Cb2zAs5Ag3hMNoU8M7j97",
  "type": "assistant",
  "uuid": "145340a5-53d9-4328-b4f1-29a20aaf7739",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "0e163909-e397-4f29-9722-d542e29e1bd1",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KtQSHpwGCa1EvmdpkKb5GD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 537,
      "cache_read_input_tokens": 62860,
      "output_tokens": 220,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 537,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 220,
          "cache_read_input_tokens": 62860,
          "cache_creation_input_tokens": 537,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 537
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

_source line 52 · 2026-05-14T19:07:58.814Z_

<details><summary>↩ Tool result · `toolu_01DYDYYcv5Xgrpa2tfHCpZSU`</summary>

```text
total_papers: 41
actual papers: 41
new entries: ['li2025kvtuner', 'chen2025pmkvq', 'li2025kitty', 'fu2025headkv', 'feng2025adakv', 'chen2026muxq']
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "145340a5-53d9-4328-b4f1-29a20aaf7739",
  "isSidechain": false,
  "promptId": "964448b9-9407-4006-b5f8-3afa58950999",
  "type": "user",
  "uuid": "609cad80-d444-41e3-aef0-ebbe510db7d1",
  "toolUseResult": {
    "stdout": "total_papers: 41\nactual papers: 41\nnew entries: ['li2025kvtuner', 'chen2025pmkvq', 'li2025kitty', 'fu2025headkv', 'feng2025adakv', 'chen2026muxq']",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "145340a5-53d9-4328-b4f1-29a20aaf7739",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "0e163909-e397-4f29-9722-d542e29e1bd1",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 53 · 2026-05-14T19:08:06.283Z_

完成。添加了 6 篇缺失论文：

| 条目 | 论文 | Cluster | Role |
|------|------|---------|------|
| `li2025kvtuner` | KVTuner (ICML 2025) | Mixed-Precision R-D | direct-competitor |
| `chen2025pmkvq` | PM-KVQ (arXiv 2025) | Mixed-Precision R-D | method-component |
| `li2025kitty` | KITTY (arXiv 2025) | KV Cache Quantization | background |
| `fu2025headkv` | HeadKV (ICLR 2025) | KV Cache Eviction | background |
| `feng2025adakv` | AdaKV (NeurIPS 2025) | KV Cache Eviction | background |
| `chen2026muxq` | MUXQ (arXiv 2026) | Model Compression | background |

另外修正了 KVmix 的 venue（arXiv 2025 → AAAI 2026）和 role（method-component → direct-competitor）。RateQuant、KVmix、MixKVQ 已在 map 中，未重复添加。total_papers 更新为 41。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "609cad80-d444-41e3-aef0-ebbe510db7d1",
  "isSidechain": false,
  "requestId": "req_011Cb2zBHtf2bDgC8WbbdyHU",
  "type": "assistant",
  "uuid": "c0639290-e588-45ca-95d0-f9086b3c1567",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "0e163909-e397-4f29-9722-d542e29e1bd1",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LE3fPpLQegXLV81e36UCUi",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 300,
      "cache_read_input_tokens": 63397,
      "output_tokens": 334,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 300,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 334,
          "cache_read_input_tokens": 63397,
          "cache_creation_input_tokens": 300,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 300
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

_source line 54_

```json
{
  "type": "last-prompt",
  "leafUuid": "c0639290-e588-45ca-95d0-f9086b3c1567",
  "sessionId": "0e163909-e397-4f29-9722-d542e29e1bd1"
}
```

---

### Runtime record

_source line 55_

```json
{
  "type": "ai-title",
  "aiTitle": "Update literature map with KV cache quantization papers",
  "sessionId": "0e163909-e397-4f29-9722-d542e29e1bd1"
}
```

---
