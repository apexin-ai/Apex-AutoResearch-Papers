# Research conversation: <project_context> # 项目: cost-verify-agent-rl ## 运行环境 - 服务器名: bjb1-17606 - SSH 账户: root（调用 ssh_execute / submit_training_

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 48
- **Recorded user turns:** 1
- **Tool calls:** 9
- **Original source:** `logs/chats/exported-trajectories/account-2/7317ebb2-d910-42e9-95dc-fa8559b8ce74.jsonl`
- **Structured JSON:** [`0858b5a894ae061d3ec5.json`](../../sessions/08/0858b5a894ae061d3ec5.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-17T13:45:42.060Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-17T13:45:42.060Z",
  "sessionId": "7317ebb2-d910-42e9-95dc-fa8559b8ce74",
  "content": "&lt;project_context>\n# 项目: cost-verify-agent-rl\n\n## 运行环境\n- 服务器名: bjb1-17606\n- SSH 账户: root（调用 ssh_execute / submit_training_job 时传入 account=\"root\"）\n- SSH 连接命令: ssh connect.bjb1.seetacloud.com  # 必须用此命令，~/.ssh/config 自动应用密钥和跳板机，禁止用裸 IP\n- 项目代码根目录: /root/cost-verify-agent-rl\n\n## ⚠️ 活跃约束（必须遵守）\n\n- **C001**: GPU 使用限定 cuda:0, cuda:1 @ bjb1-17606，禁止使用其他 GPU（原因：服务器为共享环境，存在其他项目残留。2× RTX PRO 6000 96GB 已分配给本项目。）\n- **C002**: 实验启动前必须执行 pre-flight checklist：(1) 确认入口点与最近成功实验一致 (2) df -h 检查磁盘 (3) 验证 config 参数与 vLLM/框架版本兼容 (4) 确认 checkpoint 路径存在。未通过不得启动。（原因：18 个实验仅 1 成功，exp012 用错入口点、exp007 磁盘满、exp003 格式不兼容——均为 pre-flight 可拦截的问题。） [来自 D009]\n- **C003**: 所有实验的 val/eval 必须使用 ≥16 episodes，禁止基于 4-episode 结果做 pass/fail 判定（原因：exp021 两次 eval 矛盾（4-ep: 25% vs 16-ep: 6.25%）证明 4 episodes 方差过大，基于此做决策导致 exp022 在不可靠前提下启动。Reviewer 已三次警告此问题。）\n- **C004**: Worker 禁止覆盖 memory.md，文献调研输出写 artifacts/literature_*.md（原因：2026-05-17 deep-read-turn-ppo-v2 worker 覆盖了 memory.md 全部原有内容（Citation Audit、Adaptive KL 分析、Ray raylet 记录等丢失）。literature 类 worker 输出一律写 artifacts/ 目录。）\n\n\n## 环境搭建\n连接服务器后先调 `detect_image` 检测是否为预置镜像。如果匹配，跳过基础环境搭建，只装项目特有依赖。已预装的包不要重复安装。\n\n## 输出风格\n回复简洁直接。只输出执行结果和必要信息，不要解释过程、不要客套、不要给未被要求的建议。\n&lt;/project_context>\n## 任务：验证并修正 Turn-PPO (arXiv 2512.17008) 的引用信息\n\n### 背景\nliterature_map.yaml 中 Turn-PPO 条目（id: turn-ppo2025）的标题/作者/会议可能与实际论文不一致。需要用 WebSearch 验证真实信息后统一修正。\n\n### 当前 literature_map.yaml 中的记录\n```yaml\n- id: turn-ppo2025\n  title: \"Turn-Level Policy Optimization for Multi-Turn Agent Reinforcement Learning\"\n  authors: \"Zhou et al.\"\n  venue: \"arXiv\"\n  year: 2025\n  arxiv_id: \"2512.17008\"\n```\n\n### 步骤\n1. WebSearch \"arXiv 2512.17008\" 获取论文真实标题、作者列表、发表会议/venue、年份\n2. 对比当前记录，列出差异\n3. 用 `read_project_file(project=\"cost-verify-agent-rl\", file=\"literature_map.yaml\", max_chars=0)` 读取完整 literature_map.yaml\n4. 修正 turn-ppo2025 条目的 title、authors、venue、year 字段为 WebSearch 验证版\n5. 用 `save_project_file(project=\"cost-verify-agent-rl\", file=\"literature_map.yaml\", content=...)` 保存修正后的完整文件\n\n### 产出\n- 修正后的 literature_map.yaml（仅改 turn-ppo2025 条目，其他不动）\n- 在 Worker 结束消息中报告：旧值 vs 新值的差异表\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-17T13:45:42.063Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-17T13:45:42.063Z",
  "sessionId": "7317ebb2-d910-42e9-95dc-fa8559b8ce74"
}
```

---

## Round 1

46 recorded events

### User

_source line 3 · 2026-05-17T13:45:42.099Z_

&lt;project_context>
# 项目: cost-verify-agent-rl

## 运行环境
- 服务器名: bjb1-17606
- SSH 账户: root（调用 ssh_execute / submit_training_job 时传入 account="root"）
- SSH 连接命令: ssh connect.bjb1.seetacloud.com  # 必须用此命令，~/.ssh/config 自动应用密钥和跳板机，禁止用裸 IP
- 项目代码根目录: /root/cost-verify-agent-rl

## ⚠️ 活跃约束（必须遵守）

- **C001**: GPU 使用限定 cuda:0, cuda:1 @ bjb1-17606，禁止使用其他 GPU（原因：服务器为共享环境，存在其他项目残留。2× RTX PRO 6000 96GB 已分配给本项目。）
- **C002**: 实验启动前必须执行 pre-flight checklist：(1) 确认入口点与最近成功实验一致 (2) df -h 检查磁盘 (3) 验证 config 参数与 vLLM/框架版本兼容 (4) 确认 checkpoint 路径存在。未通过不得启动。（原因：18 个实验仅 1 成功，exp012 用错入口点、exp007 磁盘满、exp003 格式不兼容——均为 pre-flight 可拦截的问题。） [来自 D009]
- **C003**: 所有实验的 val/eval 必须使用 ≥16 episodes，禁止基于 4-episode 结果做 pass/fail 判定（原因：exp021 两次 eval 矛盾（4-ep: 25% vs 16-ep: 6.25%）证明 4 episodes 方差过大，基于此做决策导致 exp022 在不可靠前提下启动。Reviewer 已三次警告此问题。）
- **C004**: Worker 禁止覆盖 memory.md，文献调研输出写 artifacts/literature_*.md（原因：2026-05-17 deep-read-turn-ppo-v2 worker 覆盖了 memory.md 全部原有内容（Citation Audit、Adaptive KL 分析、Ray raylet 记录等丢失）。literature 类 worker 输出一律写 artifacts/ 目录。）


## 环境搭建
连接服务器后先调 `detect_image` 检测是否为预置镜像。如果匹配，跳过基础环境搭建，只装项目特有依赖。已预装的包不要重复安装。

## 输出风格
回复简洁直接。只输出执行结果和必要信息，不要解释过程、不要客套、不要给未被要求的建议。
&lt;/project_context>
## 任务：验证并修正 Turn-PPO (arXiv 2512.17008) 的引用信息

### 背景
literature_map.yaml 中 Turn-PPO 条目（id: turn-ppo2025）的标题/作者/会议可能与实际论文不一致。需要用 WebSearch 验证真实信息后统一修正。

### 当前 literature_map.yaml 中的记录
```yaml
- id: turn-ppo2025
  title: "Turn-Level Policy Optimization for Multi-Turn Agent Reinforcement Learning"
  authors: "Zhou et al."
  venue: "arXiv"
  year: 2025
  arxiv_id: "2512.17008"
```

### 步骤
1. WebSearch "arXiv 2512.17008" 获取论文真实标题、作者列表、发表会议/venue、年份
2. 对比当前记录，列出差异
3. 用 `read_project_file(project="cost-verify-agent-rl", file="literature_map.yaml", max_chars=0)` 读取完整 literature_map.yaml
4. 修正 turn-ppo2025 条目的 title、authors、venue、year 字段为 WebSearch 验证版
5. 用 `save_project_file(project="cost-verify-agent-rl", file="literature_map.yaml", content=...)` 保存修正后的完整文件

### 产出
- 修正后的 literature_map.yaml（仅改 turn-ppo2025 条目，其他不动）
- 在 Worker 结束消息中报告：旧值 vs 新值的差异表


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "71e953e0-39de-4d6a-a9b9-c8a649da7bce",
  "type": "user",
  "uuid": "597b44a9-f341-4457-945a-93a9da574308",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "7317ebb2-d910-42e9-95dc-fa8559b8ce74",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-17T13:45:42.098Z_

```json
{
  "parentUuid": "597b44a9-f341-4457-945a-93a9da574308",
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
  "uuid": "e6471773-2158-4b57-8bdc-1a76cf22f53b",
  "timestamp": "2026-05-17T13:45:42.098Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "7317ebb2-d910-42e9-95dc-fa8559b8ce74",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-17T13:45:42.098Z_

```json
{
  "parentUuid": "e6471773-2158-4b57-8bdc-1a76cf22f53b",
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
  "uuid": "c073c558-a2a6-48a5-9d1a-86c8e8485d30",
  "timestamp": "2026-05-17T13:45:42.098Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "7317ebb2-d910-42e9-95dc-fa8559b8ce74",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6 · 2026-05-17T13:45:42.098Z_

```json
{
  "parentUuid": "c073c558-a2a6-48a5-9d1a-86c8e8485d30",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "a4088372-ef18-407e-942c-65962f9590d3",
  "timestamp": "2026-05-17T13:45:42.098Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "7317ebb2-d910-42e9-95dc-fa8559b8ce74",
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
  "aiTitle": "Verify and correct Turn-PPO citation information",
  "sessionId": "7317ebb2-d910-42e9-95dc-fa8559b8ce74"
}
```

---

### Assistant

_source line 8 · 2026-05-17T13:45:45.278Z_

<details><summary>Logged reasoning block</summary>

```text
Let me start by searching for the arXiv paper 2512.17008 to verify the Turn-PPO citation information, and simultaneously read the current literature_map.yaml.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a4088372-ef18-407e-942c-65962f9590d3",
  "isSidechain": false,
  "requestId": "req_011Cb8F2enXo5tgNNK8f9mzx",
  "type": "assistant",
  "uuid": "26b0ecd5-2f67-4f38-ba77-742003533572",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "7317ebb2-d910-42e9-95dc-fa8559b8ce74",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XJVbmkktum9SoY7nQEKEgH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 13008,
      "cache_read_input_tokens": 11841,
      "output_tokens": 195,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13008,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 195,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 13008,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13008
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

_source line 9 · 2026-05-17T13:45:45.846Z_

验证 arXiv 2512.17008 的真实引用信息，同时读取当前 literature_map.yaml。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "26b0ecd5-2f67-4f38-ba77-742003533572",
  "isSidechain": false,
  "requestId": "req_011Cb8F2enXo5tgNNK8f9mzx",
  "type": "assistant",
  "uuid": "2c89956d-ef79-4202-9279-69ec3e3e0c40",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "7317ebb2-d910-42e9-95dc-fa8559b8ce74",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XJVbmkktum9SoY7nQEKEgH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 13008,
      "cache_read_input_tokens": 11841,
      "output_tokens": 195,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13008,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 195,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 13008,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13008
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

_source line 10 · 2026-05-17T13:45:46.800Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01N55nDH5jERYsMGDpYQxFN5`</summary>

```json
{
  "query": "select:WebSearch,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__save_project_file",
  "max_results": 3
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2c89956d-ef79-4202-9279-69ec3e3e0c40",
  "isSidechain": false,
  "requestId": "req_011Cb8F2enXo5tgNNK8f9mzx",
  "type": "assistant",
  "uuid": "b4a30148-e969-4f5c-ba4f-6dfac6f4b278",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "7317ebb2-d910-42e9-95dc-fa8559b8ce74",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XJVbmkktum9SoY7nQEKEgH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 13008,
      "cache_read_input_tokens": 11841,
      "output_tokens": 195,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13008,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 195,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 13008,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13008
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

_source line 11 · 2026-05-17T13:45:46.806Z_

<details><summary>↩ Tool result · `toolu_01N55nDH5jERYsMGDpYQxFN5`</summary>

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
  "parentUuid": "b4a30148-e969-4f5c-ba4f-6dfac6f4b278",
  "isSidechain": false,
  "promptId": "71e953e0-39de-4d6a-a9b9-c8a649da7bce",
  "type": "user",
  "uuid": "94a927ca-a747-40b5-8f3e-db4baed73e0f",
  "toolUseResult": {
    "matches": [
      "WebSearch",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__save_project_file"
    ],
    "query": "select:WebSearch,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__save_project_file",
    "total_deferred_tools": 22
  },
  "sourceToolAssistantUUID": "b4a30148-e969-4f5c-ba4f-6dfac6f4b278",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "7317ebb2-d910-42e9-95dc-fa8559b8ce74",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-17T13:45:49.654Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018ZBgPNjvwk3HJomRDoPa8G`</summary>

```json
{
  "query": "arXiv 2512.17008 Turn-Level Policy Optimization"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "94a927ca-a747-40b5-8f3e-db4baed73e0f",
  "isSidechain": false,
  "requestId": "req_011Cb8F31B7jU87GozFdqJrY",
  "type": "assistant",
  "uuid": "8b12b63b-9a39-46e6-86ef-a95bff57a55b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "7317ebb2-d910-42e9-95dc-fa8559b8ce74",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PSi6bCWQzeqENeZhGWeQ7f",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1290,
      "cache_read_input_tokens": 24849,
      "output_tokens": 162,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1290,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 162,
          "cache_read_input_tokens": 24849,
          "cache_creation_input_tokens": 1290,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1290
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

_source line 13 · 2026-05-17T13:45:49.992Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01GP2LWrdjnao7dfnGvPbR8U`</summary>

```json
{
  "project": "cost-verify-agent-rl",
  "file": "literature_map.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8b12b63b-9a39-46e6-86ef-a95bff57a55b",
  "isSidechain": false,
  "requestId": "req_011Cb8F31B7jU87GozFdqJrY",
  "type": "assistant",
  "uuid": "24b94cba-878f-4f52-ba31-4ab2b9a86a4e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "7317ebb2-d910-42e9-95dc-fa8559b8ce74",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PSi6bCWQzeqENeZhGWeQ7f",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1290,
      "cache_read_input_tokens": 24849,
      "output_tokens": 162,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1290,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 162,
          "cache_read_input_tokens": 24849,
          "cache_creation_input_tokens": 1290,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1290
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

_source line 14 · 2026-05-17T13:45:55.734Z_

<details><summary>↩ Tool result · `toolu_018ZBgPNjvwk3HJomRDoPa8G`</summary>

```text
Web search results for query: "arXiv 2512.17008 Turn-Level Policy Optimization"

Links: [{"title":"[2512.17008] Turn-PPO: Turn-Level Advantage Estimation with PPO for Improved Multi-Turn RL in Agentic LLMs","url":"https://arxiv.org/abs/2512.17008"},{"title":"Turn-PPO: Turn-Level Advantage Estimation with PPO for Improved Multi-Turn RL in Agentic LLMs","url":"https://arxiv.org/html/2512.17008"},{"title":"Turn-PPO: Turn-Level Advantage Estimation with PPO for Improved","url":"https://arxiv.org/pdf/2512.17008"},{"title":"Paper page - Turn-PPO: Turn-Level Advantage Estimation with PPO for Improved Multi-Turn RL in Agentic LLMs","url":"https://huggingface.co/papers/2512.17008"},{"title":"TIPS: Turn-level Information-Potential Reward Shaping for Search-Augmented LLMs","url":"https://arxiv.org/html/2603.22293v1"},{"title":"Agentic Reinforced Policy Optimization | OpenReview","url":"https://openreview.net/forum?id=TX4k7BF6aO"},{"title":"AT2PO: Agentic Turn-based Policy Optimization via Tree Search","url":"https://arxiv.org/html/2601.04767v1"},{"title":"GitHub - RUC-NLPIR/ARPO: [ICLR 2026] Agentic Reinforced Policy Optimization (ARPO) · GitHub","url":"https://github.com/RUC-NLPIR/ARPO"},{"title":"[2512.19673] Bottom-up Policy Optimization: Your Language Model Policy Secretly Contains Internal Policies","url":"https://arxiv.org/abs/2512.19673"},{"title":"A2TGPO: Agentic Turn-Group Policy Optimization with Adaptive Turn-level Clipping","url":"https://arxiv.org/html/2605.06200"}]

Based on the search results, I found information about arXiv paper 2512.17008:

This paper is titled "Turn-PPO: Turn-Level Advantage Estimation with PPO for Improved Multi-Turn RL in Agentic LLMs" and was submitted on December 18, 2025, with the latest version on January 23, 2026.

**Overview:**
The paper addresses reinforcement learning for training interactive LLM agents in real-world environments, particularly identifying limitations when applying the Group Relative Policy Optimization (GRPO) algorithm to multi-turn tasks requiring long-horizon reasoning.

**Key Contributions:**
The authors explore Proximal Policy Optimization (PPO) as an alternative, finding it more robust than GRPO, and introduce turn-PPO, a variant that operates on a turn-level MDP formulation rather than the commonly used token-level MDP.

**Results:**
Their results on the WebShop and Sokoban datasets demonstrate the effectiveness of turn-PPO, both with and without long reasoning components.

**Authors:**
The paper is authored by Junbo Li, Peng Zhou, Rui Meng, Meet P. Vadera, Lihong Li, and Yang Li.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8b12b63b-9a39-46e6-86ef-a95bff57a55b",
  "isSidechain": false,
  "promptId": "71e953e0-39de-4d6a-a9b9-c8a649da7bce",
  "type": "user",
  "uuid": "7282c02f-0293-450e-9839-e8cf81f110af",
  "toolUseResult": {
    "query": "arXiv 2512.17008 Turn-Level Policy Optimization",
    "results": [
      {
        "tool_use_id": "srvtoolu_01DLEY5KLukg9A447vPyTuw9",
        "content": [
          {
            "title": "[2512.17008] Turn-PPO: Turn-Level Advantage Estimation with PPO for Improved Multi-Turn RL in Agentic LLMs",
            "url": "https://arxiv.org/abs/2512.17008"
          },
          {
            "title": "Turn-PPO: Turn-Level Advantage Estimation with PPO for Improved Multi-Turn RL in Agentic LLMs",
            "url": "https://arxiv.org/html/2512.17008"
          },
          {
            "title": "Turn-PPO: Turn-Level Advantage Estimation with PPO for Improved",
            "url": "https://arxiv.org/pdf/2512.17008"
          },
          {
            "title": "Paper page - Turn-PPO: Turn-Level Advantage Estimation with PPO for Improved Multi-Turn RL in Agentic LLMs",
            "url": "https://huggingface.co/papers/2512.17008"
          },
          {
            "title": "TIPS: Turn-level Information-Potential Reward Shaping for Search-Augmented LLMs",
            "url": "https://arxiv.org/html/2603.22293v1"
          },
          {
            "title": "Agentic Reinforced Policy Optimization | OpenReview",
            "url": "https://openreview.net/forum?id=TX4k7BF6aO"
          },
          {
            "title": "AT2PO: Agentic Turn-based Policy Optimization via Tree Search",
            "url": "https://arxiv.org/html/2601.04767v1"
          },
          {
            "title": "GitHub - RUC-NLPIR/ARPO: [ICLR 2026] Agentic Reinforced Policy Optimization (ARPO) · GitHub",
            "url": "https://github.com/RUC-NLPIR/ARPO"
          },
          {
            "title": "[2512.19673] Bottom-up Policy Optimization: Your Language Model Policy Secretly Contains Internal Policies",
            "url": "https://arxiv.org/abs/2512.19673"
          },
          {
            "title": "A2TGPO: Agentic Turn-Group Policy Optimization with Adaptive Turn-level Clipping",
            "url": "https://arxiv.org/html/2605.06200"
          }
        ]
      },
      "Based on the search results, I found information about arXiv paper 2512.17008:\n\nThis paper is titled \"Turn-PPO: Turn-Level Advantage Estimation with PPO for Improved Multi-Turn RL in Agentic LLMs\" and was submitted on December 18, 2025, with the latest version on January 23, 2026.\n\n**Overview:**\nThe paper addresses reinforcement learning for training interactive LLM agents in real-world environments, particularly identifying limitations when applying the Group Relative Policy Optimization (GRPO) algorithm to multi-turn tasks requiring long-horizon reasoning.\n\n**Key Contributions:**\nThe authors explore Proximal Policy Optimization (PPO) as an alternative, finding it more robust than GRPO, and introduce turn-PPO, a variant that operates on a turn-level MDP formulation rather than the commonly used token-level MDP.\n\n**Results:**\nTheir results on the WebShop and Sokoban datasets demonstrate the effectiveness of turn-PPO, both with and without long reasoning components.\n\n**Authors:**\nThe paper is authored by Junbo Li, Peng Zhou, Rui Meng, Meet P. Vadera, Lihong Li, and Yang Li."
    ],
    "durationSeconds": 6.0736684049999985
  },
  "sourceToolAssistantUUID": "8b12b63b-9a39-46e6-86ef-a95bff57a55b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "7317ebb2-d910-42e9-95dc-fa8559b8ce74",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-17T13:45:55.757Z_

<details><summary>↩ Tool result · `toolu_01GP2LWrdjnao7dfnGvPbR8U`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/literature_map.yaml\", \"content\": \"# B-IAVR Literature Map\\n# Updated: 2026-05-17\\n# Categories: direct-competitor, method-component, background, evaluation\\n# Roles: predecessor, competitor, baseline, evaluation, background\\n\\npapers:\\n\\n  # ============================================================\\n  # Direction 1: Self-Verification / Self-Correction in LLM Agents\\n  # ============================================================\\n\\n  - id: kamoi2024self-correction-survey\\n    title: \\\"When Can LLMs Actually Correct Their Own Mistakes? A Critical Survey of Self-Correction of LLMs\\\"\\n    authors: \\\"Kamoi et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2024\\n    arxiv_id: \\\"2406.01297\\\"\\n    category: background\\n    role: background\\n    relevance_note: >\\n      Foundational survey establishing that pure intrinsic self-correction is unreliable.\\n      Validates B-IAVR's use of grounded verification (environment re-observation) over prompted self-feedback.\\n\\n  - id: tie2025correctbench\\n    title: \\\"Can LLMs Correct Themselves? A Benchmark of Self-Correction in LLMs\\\"\\n    authors: \\\"Tie et al.\\\"\\n    venue: \\\"NeurIPS 2025 Datasets & Benchmarks\\\"\\n    year: 2025\\n    arxiv_id: \\\"2510.16062\\\"\\n    category: background\\n    role: background\\n    relevance_note: >\\n      Benchmark showing self-correction has diminishing returns when applied uniformly.\\n      Supports B-IAVR's selective verification design over blanket correction.\\n\\n  - id: self-verification-dilemma-2026\\n    title: \\\"Self-Verification Dilemma: Experience-Driven Suppression of Overused Checking in LLM Reasoning\\\"\\n    authors: \\\"Long et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2026\\n    arxiv_id: \\\"2602.03485\\\"\\n    category: background\\n    role: background\\n    relevance_note: >\\n      Empirically validates that >90% of self-verification is confirmatory, ~2% corrective.\\n      Directly supports B-IAVR's core thesis that verification should be selective.\\n      Their experience-pool approach is complementary to B-IAVR's action-change signal.\\n\\n  - id: zhang2025incentivize-self-verify\\n    title: \\\"Incentivizing LLMs to Self-Verify Their Answers\\\"\\n    authors: \\\"Zhang et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2025\\n    arxiv_id: \\\"2506.01369\\\"\\n    category: background\\n    role: background\\n    relevance_note: >\\n      Unifies answer generation and verification via single RL training process.\\n      Parallel to B-IAVR: they train verification into generation; B-IAVR trains when to trigger separate verification.\\n\\n  - id: mar2025\\n    title: \\\"MAR: Multi-Agent Reflexion Improves Reasoning Abilities in LLMs\\\"\\n    authors: \\\"Ozer et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2025\\n    arxiv_id: \\\"2512.20845\\\"\\n    category: background\\n    role: background\\n    relevance_note: >\\n      Multi-agent self-correction with diverse critic personas.\\n      Complementary: MAR improves correction quality; B-IAVR decides when to trigger correction.\\n\\n  - id: ssr2025\\n    title: \\\"SSR: Socratic Self-Refine for Large Language Model Reasoning\\\"\\n    authors: \\\"Shi et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2025\\n    arxiv_id: \\\"2511.10621\\\"\\n    category: background\\n    role: background\\n    relevance_note: >\\n      Structured Socratic questioning for self-refinement.\\n      Complementary: improves correction step quality; B-IAVR focuses on when to invoke correction.\\n\\n  - id: verifiagent2025\\n    title: \\\"VerifiAgent: a Unified Verification Agent in Language Model Reasoning\\\"\\n    authors: \\\"Han et al.\\\"\\n    venue: \\\"EMNLP 2025 Findings\\\"\\n    year: 2025\\n    arxiv_id: \\\"2504.00406\\\"\\n    category: background\\n    role: background\\n    relevance_note: >\\n      Unified verification agent with meta-verification + tool-based adaptive verification.\\n      Focuses on how to verify (tool selection); B-IAVR focuses on when to verify (policy learning).\\n      Complementary: VerifiAgent's verification quality could enhance B-IAVR's verification step.\\n\\n  # ============================================================\\n  # Direction 2: Agent RL Training\\n  # ============================================================\\n\\n  - id: feng2025gigpo\\n    title: \\\"GiGPO: Group-in-Group Policy Optimization for LLM Agent Training\\\"\\n    authors: \\\"Feng et al.\\\"\\n    venue: \\\"NeurIPS 2025\\\"\\n    year: 2025\\n    arxiv_id: \\\"2505.10978\\\"\\n    category: method-component\\n    role: predecessor\\n    relevance_note: >\\n      Core training algorithm for B-IAVR. Nested group structure provides step-level credit\\n      assignment without learned critic. >12% over GRPO on ALFWorld, >9% on WebShop.\\n\\n  - id: selfguide2026\\n    title: \\\"Co-Evolution of Policy and Internal Reward for Language Agents (Self-Guide)\\\"\\n    authors: \\\"Wang et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2026\\n    arxiv_id: \\\"2604.03098\\\"\\n    category: method-component\\n    role: predecessor\\n    relevance_note: >\\n      Direct predecessor. B-IAVR extends Self-Guide's co-evolving internal reward.\\n      The self-guidance signal is the foundation for action-change detection triggering verification.\\n      8% improvement over env-reward-only on ALFWorld with Qwen3-1.7B/4B.\\n\\n  - id: spear2025\\n    title: \\\"Learn the Ropes, Then Trust the Wins: Self-imitation with Progressive Exploration for Agentic Reinforcement Learning\\\"\\n    authors: \\\"Qin et al.\\\"\\n    venue: \\\"ICLR 2026\\\"\\n    year: 2025\\n    arxiv_id: \\\"2509.22601\\\"\\n    category: method-component\\n    role: background\\n    relevance_note: >\\n      Curriculum-based self-imitation for sparse-reward agent tasks.\\n      Up to +16.1% on ALFWorld over GRPO. Self-imitation curriculum could augment B-IAVR training.\\n\\n  - id: wei2025webagent-r1\\n    title: \\\"WebAgent-R1: Training Web Agents via End-to-End Multi-Turn RL\\\"\\n    authors: \\\"Wei et al.\\\"\\n    venue: \\\"EMNLP 2025\\\"\\n    year: 2025\\n    arxiv_id: \\\"2505.16421\\\"\\n    category: background\\n    role: background\\n    relevance_note: >\\n      Extends GRPO to multi-turn (M-GRPO) with dynamic context compression.\\n      Qwen-2.5-3B: 6.1% to 33.9% on WebArena-Lite. M-GRPO multi-turn extension relevant to B-IAVR.\\n\\n  - id: dapo2025\\n    title: \\\"DAPO: An Open-Source LLM Reinforcement Learning System at Scale\\\"\\n    authors: \\\"Yu et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2025\\n    arxiv_id: \\\"2503.14476\\\"\\n    category: method-component\\n    role: background\\n    relevance_note: >\\n      RL training stabilization techniques (Clip-Higher, Dynamic Sampling).\\n      Applicable to B-IAVR's RL training to prevent entropy collapse.\\n\\n  - id: digiRL2024\\n    title: \\\"DigiRL: Training In-The-Wild Device-Control Agents with Autonomous RL\\\"\\n    authors: \\\"Bai et al.\\\"\\n    venue: \\\"NeurIPS 2024\\\"\\n    year: 2024\\n    arxiv_id: \\\"2406.11896\\\"\\n    category: background\\n    role: background\\n    relevance_note: >\\n      Online RL for device control agents. Demonstrates online RL viability for interactive agents.\\n      49.5% absolute improvement over SFT. Parallel approach to B-IAVR in text-based setting.\\n\\n  - id: li2025sorl\\n    title: \\\"SORL: Stabilizing Off-Policy RL for Long-Horizon Agent Training\\\"\\n    authors: \\\"Li et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2025\\n    arxiv_id: \\\"2511.20718\\\"\\n    category: method-component\\n    role: background\\n    relevance_note: >\\n      Turn-level importance sampling + clipping-triggered normalization for stable multi-turn agent RL.\\n      Directly applicable to B-IAVR's multi-turn ALFWorld training stability.\\n\\n  - id: agentic-rl-survey-2025\\n    title: \\\"The Landscape of Agentic Reinforcement Learning for LLMs: A Survey\\\"\\n    authors: \\\"Zhang et al.\\\"\\n    venue: \\\"TMLR 2026\\\"\\n    year: 2025\\n    arxiv_id: \\\"2509.02547\\\"\\n    category: background\\n    role: background\\n    relevance_note: >\\n      Comprehensive survey formalizing agentic RL. Contextualizes B-IAVR as training agents\\n      to make meta-decisions (when to verify) via RL within the POMDP framework.\\n\\n  - id: skillmaster2026\\n    title: \\\"SkillMaster: Toward Autonomous Skill Mastery in LLM Agents\\\"\\n    authors: \\\"Yang et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2026\\n    arxiv_id: \\\"2605.08693\\\"\\n    category: method-component\\n    role: background\\n    relevance_note: >\\n      DualAdv-GRPO: separately estimates advantages for task-solving and skill-editing decisions.\\n      +8.8% on ALFWorld, +9.3% on WebShop. DualAdv structure could inform B-IAVR's\\n      separation of action and verification advantages.\\n\\n  - id: t2po2026\\n    title: \\\"T2PO: Uncertainty-Guided Exploration Control for Stable Multi-Turn Agentic RL\\\"\\n    authors: \\\"Wang et al.\\\"\\n    venue: \\\"ICML 2026 Spotlight\\\"\\n    year: 2026\\n    arxiv_id: \\\"2605.02178\\\"\\n    category: method-component\\n    role: background\\n    relevance_note: >\\n      Token- and turn-level uncertainty monitoring for stable multi-turn agent RL.\\n      Triggers thinking intervention when marginal uncertainty change drops below threshold.\\n      Evaluated on ALFWorld and WebShop. Conceptually related: uncertainty-based trigger vs\\n      B-IAVR's action-change trigger, but T2PO targets training stability, not deployment verification.\\n\\n  - id: gvpo2026\\n    title: \\\"GVPO: Group Verification-based Policy Optimization for Interactive Coding Agents\\\"\\n    authors: \\\"Dai et al.\\\"\\n    venue: \\\"ICLR 2026\\\"\\n    year: 2026\\n    arxiv_id: null  # no arXiv preprint; OpenReview ID: RY47Tq0VsV\\n    category: method-component\\n    role: background\\n    relevance_note: >\\n      Advantage shaping with outcome-verifiable + process-verifiable signals.\\n      +12.7% over o1 on AppWorld. Integrates intermediate execution feedback as step-level\\n      verification signals. Different focus: uses verification for credit assignment during\\n      training; B-IAVR learns when to invoke verification at deployment.\\n\\n  - id: agentv-rl2026\\n    title: \\\"AgentV-RL: Scaling Reward Modeling with Agentic Verifier\\\"\\n    authors: \\\"Zhang et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2026\\n    arxiv_id: \\\"2604.16004\\\"\\n    category: method-component\\n    role: background\\n    relevance_note: >\\n      Bidirectional forward/backward agentic verifier for reward modeling in RL.\\n      4B model surpasses SOTA ORMs by 25.2%. Addresses verification quality in reward modeling;\\n      B-IAVR addresses verification timing in agent deployment. Complementary.\\n\\n  - id: pa-moe2026\\n    title: \\\"PA-MoE: Phase-Aware Mixture of Experts for Agentic Reinforcement Learning\\\"\\n    authors: \\\"Li et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2026\\n    arxiv_id: \\\"2602.17038\\\"\\n    category: evaluation\\n    role: baseline\\n    relevance_note: >\\n      [NEW-0516] Lightweight phase router learns latent phase boundaries from RL objective.\\n      PA-MoE+GiGPO with Qwen2.5-1.5B achieves 93.8% on ALFWorld (+7.7 over GiGPO 86.1%).\\n      1.5B outperforms vanilla 7B GiGPO (90.2%). New small-model SOTA on ALFWorld.\\n      Orthogonal architecture innovation; important baseline to cite.\\n\\n  - id: sdar2026\\n    title: \\\"SDAR: Self-Distilled Agentic Reinforcement Learning\\\"\\n    authors: \\\"Lu et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2026\\n    arxiv_id: \\\"2605.15155\\\"\\n    category: method-component\\n    role: background\\n    relevance_note: >\\n      [NEW-0516] On-policy self-distillation as gated auxiliary objective during RL training.\\n      Token-level gate decides supervision intensity. +9.4% over GRPO on ALFWorld.\\n      Complementary: SDAR improves RL training; B-IAVR learns verification policy.\\n\\n  - id: hcapo2026\\n    title: \\\"HCAPO: Hindsight Credit Assignment for Long-Horizon LLM Agents\\\"\\n    authors: \\\"Tan et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2026\\n    arxiv_id: \\\"2603.08754\\\"\\n    category: method-component\\n    role: background\\n    relevance_note: >\\n      [NEW-0516] LLM-as-critic refines step-level Q-values via hindsight reasoning +\\n      multi-scale advantage for critical decision states.\\n      +13.8% on ALFWorld, +7.7% on WebShop over GRPO (Qwen2.5-7B).\\n      Could improve B-IAVR's reward signal for verification decision steps.\\n\\n  - id: act2026\\n    title: \\\"ACT: Agentic Critical Training\\\"\\n    authors: \\\"Liu et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2026\\n    arxiv_id: \\\"2603.08706\\\"\\n    category: method-component\\n    role: background\\n    relevance_note: >\\n      [NEW-0516] Trains agents to judge action quality via critical comparison reward.\\n      +5.07 over IL, +4.62 over RL. Different axis: ACT improves reflection quality;\\n      B-IAVR decides when to reflect.\\n\\n  - id: rwml2026\\n    title: \\\"RWML: Reinforcement World Model Learning for LLM-based Agents\\\"\\n    authors: \\\"Yu et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2026\\n    arxiv_id: \\\"2602.05842\\\"\\n    category: method-component\\n    role: background\\n    relevance_note: >\\n      [NEW-0516] Self-supervised world model via sim-to-real gap rewards in embedding space.\\n      +6.9 on ALFWorld over task-success-only RL. Matches expert-data training.\\n      Orthogonal: improves internal world model; B-IAVR adds selective verification.\\n\\n  - id: skill0-2026\\n    title: \\\"SKILL0: In-Context Agentic Reinforcement Learning for Skill Internalization\\\"\\n    authors: \\\"Lu et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2026\\n    arxiv_id: \\\"2604.02268\\\"\\n    category: method-component\\n    role: background\\n    relevance_note: >\\n      [NEW-0516] Training-time curriculum progressively withdraws skill context until zero-shot.\\n      +9.7% on ALFWorld over GRPO, <0.5k tokens per step.\\n      Complementary: SKILL0 internalizes skills; B-IAVR adds selective verification.\\n\\n  - id: fission-grpo2026\\n    title: \\\"Fission-GRPO: Robust Tool Use via Learning to Recover from Execution Errors\\\"\\n    authors: \\\"Zhang et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2026\\n    arxiv_id: \\\"2601.15625\\\"\\n    category: method-component\\n    role: background\\n    relevance_note: >\\n      [NEW-0516] Fissions failed trajectories into recovery training instances.\\n      +4% overall accuracy on BFCL v4 Multi-Turn over GRPO.\\n      Related: error recovery after failure vs B-IAVR's proactive verification.\\n\\n  - id: selfbudgeter2026\\n    title: \\\"SelfBudgeter: Adaptive Token Allocation for Efficient LLM Reasoning\\\"\\n    authors: \\\"Li et al.\\\"\\n    venue: \\\"ICLR 2026 (under review)\\\"\\n    year: 2025\\n    arxiv_id: \\\"2505.11274\\\"\\n    category: background\\n    role: background\\n    relevance_note: >\\n      [NEW-0516] Self-estimated token budgets + budget-guided GRPO. 61% token reduction.\\n      Parallel concept: SelfBudgeter allocates computation budget;\\n      B-IAVR makes binary verify/not-verify decision. Both use RL for adaptive compute.\\n\\n  - id: cove2026\\n    title: \\\"CoVe: Training Interactive Tool-Use Agents via Constraint-Guided Verification\\\"\\n    authors: \\\"Chen et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2026\\n    arxiv_id: \\\"2603.01940\\\"\\n    category: background\\n    role: background\\n    relevance_note: >\\n      [NEW-0516] Task constraints guide trajectory generation and serve as deterministic verifiers.\\n      Different: CoVe uses verification for data synthesis; B-IAVR learns when to verify at inference.\\n\\n  # ============================================================\\n  # Direction 3: Selective Verification / Adaptive Computation\\n  # ============================================================\\n\\n  - id: wan2025derailer-rerailer\\n    title: \\\"Derailer-Rerailer: Adaptive Verification for Efficient and Reliable LM Reasoning\\\"\\n    authors: \\\"Wan et al.\\\"\\n    venue: \\\"ACL 2025 Findings\\\"\\n    year: 2025\\n    arxiv_id: \\\"2408.13940\\\"\\n    category: direct-competitor\\n    role: competitor\\n    relevance_note: >\\n      Most directly related competitor. Both do selective verification with binary trigger.\\n      Key difference: operates on reasoning chains (single-turn); B-IAVR on agent trajectories (multi-turn).\\n      Uses heuristic instability signal; B-IAVR uses RL-trained action-change signal.\\n      8-11% accuracy gain, 2-3x efficiency over uniform verification.\\n\\n  - id: sherlock2025\\n    title: \\\"Sherlock: Reliable and Efficient Agentic Workflow Execution\\\"\\n    authors: \\\"Microsoft\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2025\\n    arxiv_id: \\\"2511.00330\\\"\\n    category: direct-competitor\\n    role: competitor\\n    relevance_note: >\\n      Selective verification for agentic workflows via offline counterfactual analysis + speculative execution.\\n      Different scope: workflow DAG level (offline); B-IAVR is step-level (online RL).\\n      18.3% accuracy gain, 26% cost reduction, 48.7% latency reduction.\\n\\n  - id: singhi2025when-to-verify\\n    title: \\\"When To Solve, When To Verify: Compute-Optimal Verification for LLM Reasoning\\\"\\n    authors: \\\"Singhi et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2025\\n    arxiv_id: \\\"2504.01005\\\"\\n    category: background\\n    role: background\\n    relevance_note: >\\n      Derives inference scaling laws for solve-vs-verify tradeoff.\\n      Finding that over-verification is suboptimal directly supports B-IAVR's selective approach.\\n      B-IAVR learns this allocation via RL rather than analytically.\\n\\n  - id: yang2026ares\\n    title: \\\"ARES: Adaptive Reasoning Effort Selection for Efficient LLM Agents\\\"\\n    authors: \\\"Yang et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2026\\n    arxiv_id: \\\"2603.07915\\\"\\n    category: direct-competitor\\n    role: competitor\\n    relevance_note: >\\n      Closest competitor in agent domain. Both train learned per-step compute allocation.\\n      ARES uses SFT-initialized router further refined via GRPO with outcome + token efficiency reward;\\n      B-IAVR trains binary verify/not-verify via RL with action-change signal.\\n      Key differences: (1) reward signal — ARES optimizes token efficiency, B-IAVR uses action-change\\n      as verification trigger; (2) data requirement — ARES needs difficulty-annotated training data\\n      to bootstrap the router, B-IAVR learns from environment interaction alone.\\n      Reduces reasoning tokens by up to 52.7%.\\n\\n  - id: tu2025autothink\\n    title: \\\"Learning When to Think: Shaping Adaptive Reasoning in R1-Style Models via Multi-Stage RL\\\"\\n    authors: \\\"Tu et al.\\\"\\n    venue: \\\"NeurIPS 2025\\\"\\n    year: 2025\\n    arxiv_id: \\\"2505.10832\\\"\\n    category: direct-competitor\\n    role: competitor\\n    relevance_note: >\\n      Analogous idea in reasoning domain: RL-trained adaptive computation trigger.\\n      Operates on single-turn reasoning; B-IAVR on multi-turn agent trajectories.\\n      +6.4% accuracy, -52% tokens on DeepSeek-R1-Distill-Qwen-1.5B.\\n\\n  - id: du2025thinkless\\n    title: \\\"Thinkless: LLM Learns When to Think\\\"\\n    authors: \\\"Fang et al.\\\"\\n    venue: \\\"NeurIPS 2025\\\"\\n    year: 2025\\n    arxiv_id: \\\"2505.13379\\\"\\n    category: direct-competitor\\n    role: competitor\\n    relevance_note: >\\n      RL-trained control token to decide when to invoke extended thinking.\\n      Methodologically closest to B-IAVR in reasoning domain; B-IAVR applies to interactive agent trajectories.\\n\\n  - id: wang2025efficient-agents\\n    title: \\\"Efficient Agents: Building Effective Agents While Reducing Cost\\\"\\n    authors: \\\"Wang et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2025\\n    arxiv_id: \\\"2508.02694\\\"\\n    category: background\\n    role: background\\n    relevance_note: >\\n      First systematic study of agent efficiency-effectiveness tradeoff.\\n      Framework-level cost reduction; B-IAVR addresses cost at verification-policy level.\\n      Retains 96.7% performance with 28.4% cost-of-pass improvement.\\n\\n  - id: venktesh2025trust-but-verify\\n    title: \\\"Trust but Verify! A Survey on Verification Design for Test-time Scaling\\\"\\n    authors: \\\"Venktesh et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2025\\n    arxiv_id: \\\"2508.16665\\\"\\n    category: background\\n    role: background\\n    relevance_note: >\\n      Survey of verification approaches for test-time compute scaling.\\n      Identifies verification timing as key open problem. B-IAVR provides concrete solution for agent setting.\\n\\n  - id: agent-omit2026\\n    title: \\\"Agent-Omit: Training Efficient LLM Agents for Adaptive Thought and Observation Omission via Agentic RL\\\"\\n    authors: \\\"Ning et al.\\\"\\n    venue: \\\"ICML 2026\\\"\\n    year: 2026\\n    arxiv_id: \\\"2602.04284\\\"\\n    category: direct-competitor\\n    role: competitor\\n    relevance_note: >\\n      RL-trained policy for adaptive omission of redundant thoughts and observations.\\n      Agent-Omit-8B matches frontier agents with best efficiency tradeoff on 5 benchmarks.\\n      Both use RL to learn cost-efficient agent behavior. Key difference: Agent-Omit subtracts\\n      (omits unnecessary context); B-IAVR selectively adds (verification steps).\\n      Opposite but complementary approaches to cost-efficiency. Potentially combinable.\\n\\n  - id: ava2026\\n    title: \\\"Anytime Verified Agents: Adaptive Compute Allocation for Reliable LLM Reasoning under Budget Constraints\\\"\\n    authors: \\\"Patel\\\"\\n    venue: \\\"TMLR 2026\\\"\\n    year: 2026\\n    arxiv_id: null  # no arXiv preprint; OpenReview ID: JMDCMf7mlF\\n    category: direct-competitor\\n    role: competitor\\n    relevance_note: >\\n      Dynamic compute allocation across search, sampling, and verification under budget.\\n      Uses calibrated uncertainty + value-of-information for selective verification cascades.\\n      Evaluated on GSM8K/MATH/HotpotQA/HumanEval (reasoning), not interactive agents.\\n      Key difference: analytical/heuristic allocation vs B-IAVR's RL-learned policy;\\n      single-turn reasoning vs multi-turn agent trajectories.\\n\\n  - id: cast2026\\n    title: \\\"CAST: Case-Based Calibration of Adaptive Reasoning and Execution for LLM Tool Use\\\"\\n    authors: \\\"Pang et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2026\\n    arxiv_id: \\\"2605.15041\\\"\\n    category: background\\n    role: background\\n    relevance_note: >\\n      Historical execution cases calibrate reasoning depth for tool use.\\n      Reduces reasoning length 26% with +5.85% accuracy on BFCLv2/ToolBench.\\n      Related: adaptive reasoning depth; different: case-based calibration vs RL-learned policy.\\n\\n  - id: marginal-token-allocators2026\\n    title: \\\"Agentic AI Systems Should Be Designed as Marginal Token Allocators\\\"\\n    authors: \\\"Zhu\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2026\\n    arxiv_id: \\\"2605.01214\\\"\\n    category: background\\n    role: background\\n    relevance_note: >\\n      Position paper framing agent cost-efficiency as marginal token allocation economics.\\n      Identifies under-verification as systematic failure mode. Supports B-IAVR's framing\\n      that verification decisions should reflect marginal cost-benefit analysis.\\n\\n  - id: argos2025\\n    title: \\\"Argos: Multimodal RL with Adaptive Verifier for AI Agents\\\"\\n    authors: \\\"Tan et al.\\\"\\n    venue: \\\"arXiv (revised April 2026)\\\"\\n    year: 2025\\n    arxiv_id: \\\"2512.03438\\\"\\n    category: background\\n    role: background\\n    relevance_note: >\\n      Agentic verifier that adaptively selects scoring functions for multimodal RL training.\\n      Different domain (multimodal/robotics). The adaptive verifier selection concept is\\n      complementary: Argos adapts how to verify; B-IAVR adapts when to verify.\\n\\n  # ============================================================\\n  # Direction 4: ALFWorld / Interactive Environment Benchmarks\\n  # ============================================================\\n\\n  - id: kim2025reflact\\n    title: \\\"ReflAct: World-Grounded Decision Making in LLM Agents via Goal-State Reflection\\\"\\n    authors: \\\"Kim et al.\\\"\\n    venue: \\\"EMNLP 2025\\\"\\n    year: 2025\\n    arxiv_id: \\\"2505.15182\\\"\\n    category: evaluation\\n    role: baseline\\n    relevance_note: >\\n      Prompting SOTA on ALFWorld at 93.3%. Replaces ReAct's next-action thinking with state-goal reflection.\\n      B-IAVR addresses different axis (cost-efficiency) since ALFWorld accuracy is near saturation.\\n\\n  - id: choudhury2025agentprm\\n    title: \\\"Process Reward Models for LLM Agents: Practical Framework and Directions\\\"\\n    authors: \\\"Choudhury\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2025\\n    arxiv_id: \\\"2502.10325\\\"\\n    category: evaluation\\n    role: baseline\\n    relevance_note: >\\n      Monte Carlo rollout-based process reward for agent training. 3B models achieve 91% on ALFWorld.\\n      Validates RL training approach; AgentPRM could serve as reward model for B-IAVR.\\n\\n  - id: xi2025agentprm\\n    title: \\\"AgentPRM: Process Reward Models for LLM Agents via Step-Wise Promise and Progress\\\"\\n    authors: \\\"Xi et al.\\\"\\n    venue: \\\"ACM Web Conference 2026\\\"\\n    year: 2025\\n    arxiv_id: \\\"2511.08325\\\"\\n    category: evaluation\\n    role: baseline\\n    relevance_note: >\\n      Independent work from Choudhury et al., using TD-based estimation with GAE for scalable\\n      PRM data labeling. 8x more compute-efficient than baselines with robust test-time scaling.\\n      Different approach: Choudhury uses MC rollouts; Xi uses TD+GAE for step-wise promise and progress.\\n\\n  - id: xiang2024retrospex\\n    title: \\\"Retrospex: Language Agent Meets Offline RL Critic\\\"\\n    authors: \\\"Xiang et al.\\\"\\n    venue: \\\"EMNLP 2024\\\"\\n    year: 2024\\n    arxiv_id: \\\"2505.11807\\\"\\n    category: background\\n    role: background\\n    relevance_note: >\\n      Offline RL Critic augments LLM agent action selection via dynamic rescoring.\\n      Similar architecture could inform B-IAVR's verification value estimation.\\n\\n  - id: cfgm2025\\n    title: \\\"CFGM: Coarse-to-Fine Grounded Memory for LLM Agent Planning\\\"\\n    authors: \\\"Yang et al.\\\"\\n    venue: \\\"EMNLP 2025\\\"\\n    year: 2025\\n    arxiv_id: \\\"2508.15305\\\"\\n    category: background\\n    role: background\\n    relevance_note: >\\n      Memory-augmented agent planning with episodic grounding.\\n      ALFWorld +10.40%, WebShop +20%. Complementary to B-IAVR's verification approach.\\n\\n  - id: respact2024\\n    title: \\\"ReSpAct: Harmonizing Reasoning, Speaking, and Acting\\\"\\n    authors: \\\"Dongre et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2024\\n    arxiv_id: \\\"2411.00927\\\"\\n    category: evaluation\\n    role: baseline\\n    relevance_note: >\\n      Integrates dialogue/reasoning/acting. +6% over ReAct on ALFWorld.\\n      Reduces invalid actions from 13% to 3%; B-IAVR's verification achieves error prevention differently.\\n\\n  # ============================================================\\n  # Direction 5: Multi-Turn Credit Assignment (Direct Competitors)\\n  # ============================================================\\n\\n  - id: turn-ppo2025\\n    title: \\\"Turn-Level Policy Optimization for Multi-Turn Agent Reinforcement Learning\\\"\\n    authors: \\\"Zhou et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2025\\n    arxiv_id: \\\"2512.17008\\\"\\n    category: direct-competitor\\n    role: competitor\\n    relevance_note: >\\n      [NEW-0517] Most direct competitor. Identifies \\\"uniform advantage\\\" problem in\\n      step-independent GRPO (subset of our \\\"sign misattribution\\\"). Proposes turn-level\\n      MDP + learned value function. Our differences: (1) more precise formalization\\n      (sign misattribution + gamma decay quantification), (2) contrarian solution\\n      (episode-level coarser credit vs their finer turn-level credit).\\n\\n  - id: gagpo2026\\n    title: \\\"GAGPO: Generalized Advantage Grouped Policy Optimization\\\"\\n    authors: \\\"Zhu et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2026\\n    arxiv_id: \\\"2605.13217\\\"\\n    category: direct-competitor\\n    role: competitor\\n    relevance_note: >\\n      [NEW-0517] Critic-free step-aligned credit via non-parametric grouped value proxy +\\n      TD/GAE-style temporal advantages. ALFWorld 93.5% (1.5B), 95.6% (7B).\\n      Pursues finer-grained credit to improve performance; our work diagnoses why\\n      step-independent fails (sign misattribution) and shows coarser episode-level suffices.\\n      Different contribution axis: performance optimization vs mechanism diagnosis.\\n\\n  - id: mt-grpo2025\\n    title: \\\"Reinforcing Multi-Turn Reasoning in LLM Agents via Turn-Level Reward Design\\\"\\n    authors: \\\"Wei et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2025\\n    arxiv_id: \\\"2505.11821\\\"\\n    category: direct-competitor\\n    role: competitor\\n    relevance_note: >\\n      [NEW-0517] Proposes MT-GRPO with turn-level reward design for multi-turn RL.\\n      Evaluated on QA search tasks (NQ, TriviaQA, HotpotQA), not ALFWorld.\\n      Qwen2.5-7B. Same direction as Turn-PPO (finer turn-level credit);\\n      our contrarian shows coarser episode-level eliminates sign misattribution.\\n\\n  - id: istar2025\\n    title: \\\"Agentic Reinforcement Learning with Implicit Step Rewards\\\"\\n    authors: \\\"Liu et al.\\\"\\n    venue: \\\"ICLR 2026\\\"\\n    year: 2025\\n    arxiv_id: \\\"2509.19199\\\"\\n    category: direct-competitor\\n    role: competitor\\n    relevance_note: >\\n      [NEW-0517] Implicit PRM + dual advantage (step + episode level) for agentic RL.\\n      WebShop 86.5%, VisualSokoban 91.7%. ICLR 2026 published.\\n      Learns step-level credit via implicit rewards without explicit labels;\\n      our work shows episode-level alone suffices when sign misattribution is the bottleneck.\\n      Validates that step-level credit helps, but doesn't diagnose when it hurts.\\n\\n  - id: archer2024\\n    title: \\\"ArCHer: Training Language Model Agents via Hierarchical Multi-Turn RL\\\"\\n    authors: \\\"Zhou, Zanette, Pan, Levine, Kumar\\\"\\n    venue: \\\"ICML 2024\\\"\\n    year: 2024\\n    arxiv_id: \\\"2402.19446\\\"\\n    category: method-component\\n    role: predecessor\\n    relevance_note: >\\n      [NEW-0517] Foundational hierarchical multi-turn RL framework (ICML 2024).\\n      High-level off-policy value RL (utterance-level) + low-level token policy.\\n      ~100x sample efficiency. Establishes that multi-turn RL needs hierarchical structure;\\n      our work specifically diagnoses why flat step-independent approaches fail.\\n\\n  - id: ca-survey2026\\n    title: \\\"From Reasoning to Agentic: Credit Assignment in Reinforcement Learning for Large Language Models\\\"\\n    authors: \\\"Zhang\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2026\\n    arxiv_id: \\\"2604.09459\\\"\\n    category: background\\n    role: background\\n    relevance_note: >\\n      [NEW-0517] Comprehensive survey of 47 CA methods (2024-2026). Two-dimensional\\n      taxonomy: granularity (token/segment/step/turn/multi-agent) x methodology\\n      (MC/TD/model-based/game-theoretic/information-theoretic). Contextualizes our\\n      sign misattribution diagnosis within the broader CA landscape.\\n\\n  - id: hiper2026\\n    title: \\\"HiPER: Hierarchical Reinforcement Learning with Explicit Credit Assignment for Large Language Model Agents\\\"\\n    authors: \\\"Peng et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2026\\n    arxiv_id: \\\"2602.16165\\\"\\n    category: method-component\\n    role: background\\n    relevance_note: >\\n      [NEW-0517] Hierarchical Plan-Execute RL. ALFWorld 97.4% (7B), 95.3% (1.5B).\\n      GRPO baseline: 71.1% (1.5B), 85.4% (7B). 2.8x training efficiency gain.\\n      Pursues SOTA performance via hierarchical plan-execute architecture;\\n      our work does mechanism diagnosis of why step-independent GRPO fails.\\n      Different contribution dimension: not comparable on performance axis.\\n\", \"total_chars\": 29915, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "24b94cba-878f-4f52-ba31-4ab2b9a86a4e",
  "isSidechain": false,
  "promptId": "71e953e0-39de-4d6a-a9b9-c8a649da7bce",
  "type": "user",
  "uuid": "c6a8ae9e-68d1-46f4-9de9-f2f90e977342",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/literature_map.yaml\\\", \\\"content\\\": \\\"# B-IAVR Literature Map\\\\n# Updated: 2026-05-17\\\\n# Categories: direct-competitor, method-component, background, evaluation\\\\n# Roles: predecessor, competitor, baseline, evaluation, background\\\\n\\\\npapers:\\\\n\\\\n  # ============================================================\\\\n  # Direction 1: Self-Verification / Self-Correction in LLM Agents\\\\n  # ============================================================\\\\n\\\\n  - id: kamoi2024self-correction-survey\\\\n    title: \\\\\\\"When Can LLMs Actually Correct Their Own Mistakes? A Critical Survey of Self-Correction of LLMs\\\\\\\"\\\\n    authors: \\\\\\\"Kamoi et al.\\\\\\\"\\\\n    venue: \\\\\\\"arXiv\\\\\\\"\\\\n    year: 2024\\\\n    arxiv_id: \\\\\\\"2406.01297\\\\\\\"\\\\n    category: background\\\\n    role: background\\\\n    relevance_note: >\\\\n      Foundational survey establishing that pure intrinsic self-correction is unreliable.\\\\n      Validates B-IAVR's use of grounded verification (environment re-observation) over prompted self-feedback.\\\\n\\\\n  - id: tie2025correctbench\\\\n    title: \\\\\\\"Can LLMs Correct Themselves? A Benchmark of Self-Correction in LLMs\\\\\\\"\\\\n    authors: \\\\\\\"Tie et al.\\\\\\\"\\\\n    venue: \\\\\\\"NeurIPS 2025 Datasets & Benchmarks\\\\\\\"\\\\n    year: 2025\\\\n    arxiv_id: \\\\\\\"2510.16062\\\\\\\"\\\\n    category: background\\\\n    role: background\\\\n    relevance_note: >\\\\n      Benchmark showing self-correction has diminishing returns when applied uniformly.\\\\n      Supports B-IAVR's selective verification design over blanket correction.\\\\n\\\\n  - id: self-verification-dilemma-2026\\\\n    title: \\\\\\\"Self-Verification Dilemma: Experience-Driven Suppression of Overused Checking in LLM Reasoning\\\\\\\"\\\\n    authors: \\\\\\\"Long et al.\\\\\\\"\\\\n    venue: \\\\\\\"arXiv\\\\\\\"\\\\n    year: 2026\\\\n    arxiv_id: \\\\\\\"2602.03485\\\\\\\"\\\\n    category: background\\\\n    role: background\\\\n    relevance_note: >\\\\n      Empirically validates that >90% of self-verification is confirmatory, ~2% corrective.\\\\n      Directly supports B-IAVR's core thesis that verification should be selective.\\\\n      Their experience-pool approach is complementary to B-IAVR's action-change signal.\\\\n\\\\n  - id: zhang2025incentivize-self-verify\\\\n    title: \\\\\\\"Incentivizing LLMs to Self-Verify Their Answers\\\\\\\"\\\\n    authors: \\\\\\\"Zhang et al.\\\\\\\"\\\\n    venue: \\\\\\\"arXiv\\\\\\\"\\\\n    year: 2025\\\\n    arxiv_id: \\\\\\\"2506.01369\\\\\\\"\\\\n    category: background\\\\n    role: background\\\\n    relevance_note: >\\\\n      Unifies answer generation and verification via single RL training process.\\\\n      Parallel to B-IAVR: they train verification into generation; B-IAVR trains when to trigger separate verification.\\\\n\\\\n  - id: mar2025\\\\n    title: \\\\\\\"MAR: Multi-Agent Reflexion Improves Reasoning Abilities in LLMs\\\\\\\"\\\\n    authors: \\\\\\\"Ozer et al.\\\\\\\"\\\\n    venue: \\\\\\\"arXiv\\\\\\\"\\\\n    year: 2025\\\\n    arxiv_id: \\\\\\\"2512.20845\\\\\\\"\\\\n    category: background\\\\n    role: background\\\\n    relevance_note: >\\\\n      Multi-agent self-correction with diverse critic personas.\\\\n      Complementary: MAR improves correction quality; B-IAVR decides when to trigger correction.\\\\n\\\\n  - id: ssr2025\\\\n    title: \\\\\\\"SSR: Socratic Self-Refine for Large Language Model Reasoning\\\\\\\"\\\\n    authors: \\\\\\\"Shi et al.\\\\\\\"\\\\n    venue: \\\\\\\"arXiv\\\\\\\"\\\\n    year: 2025\\\\n    arxiv_id: \\\\\\\"2511.10621\\\\\\\"\\\\n    category: background\\\\n    role: background\\\\n    relevance_note: >\\\\n      Structured Socratic questioning for self-refinement.\\\\n      Complementary: improves correction step quality; B-IAVR focuses on when to invoke correction.\\\\n\\\\n  - id: verifiagent2025\\\\n    title: \\\\\\\"VerifiAgent: a Unified Verification Agent in Language Model Reasoning\\\\\\\"\\\\n    authors: \\\\\\\"Han et al.\\\\\\\"\\\\n    venue: \\\\\\\"EMNLP 2025 Findings\\\\\\\"\\\\n    year: 2025\\\\n    arxiv_id: \\\\\\\"2504.00406\\\\\\\"\\\\n    category: background\\\\n    role: background\\\\n    relevance_note: >\\\\n      Unified verification agent with meta-verification + tool-based adaptive verification.\\\\n      Focuses on how to verify (tool selection); B-IAVR focuses on when to verify (policy learning).\\\\n      Complementary: VerifiAgent's verification quality could enhance B-IAVR's verification step.\\\\n\\\\n  # ============================================================\\\\n  # Direction 2: Agent RL Training\\\\n  # ============================================================\\\\n\\\\n  - id: feng2025gigpo\\\\n    title: \\\\\\\"GiGPO: Group-in-Group Policy Optimization for LLM Agent Training\\\\\\\"\\\\n    authors: \\\\\\\"Feng et al.\\\\\\\"\\\\n    venue: \\\\\\\"NeurIPS 2025\\\\\\\"\\\\n    year: 2025\\\\n    arxiv_id: \\\\\\\"2505.10978\\\\\\\"\\\\n    category: method-component\\\\n    role: predecessor\\\\n    relevance_note: >\\\\n      Core training algorithm for B-IAVR. Nested group structure provides step-level credit\\\\n      assignment without learned critic. >12% over GRPO on ALFWorld, >9% on WebShop.\\\\n\\\\n  - id: selfguide2026\\\\n    title: \\\\\\\"Co-Evolution of Policy and Internal Reward for Language Agents (Self-Guide)\\\\\\\"\\\\n    authors: \\\\\\\"Wang et al.\\\\\\\"\\\\n    venue: \\\\\\\"arXiv\\\\\\\"\\\\n    year: 2026\\\\n    arxiv_id: \\\\\\\"2604.03098\\\\\\\"\\\\n    category: method-component\\\\n    role: predecessor\\\\n    relevance_note: >\\\\n      Direct predecessor. B-IAVR extends Self-Guide's co-evolving internal reward.\\\\n      The self-guidance signal is the foundation for action-change detection triggering verification.\\\\n      8% improvement over env-reward-only on ALFWorld with Qwen3-1.7B/4B.\\\\n\\\\n  - id: spear2025\\\\n    title: \\\\\\\"Learn the Ropes, Then Trust the Wins: Self-imitation with Progressive Exploration for Agentic Reinforcement Learning\\\\\\\"\\\\n    authors: \\\\\\\"Qin et al.\\\\\\\"\\\\n    venue: \\\\\\\"ICLR 2026\\\\\\\"\\\\n    year: 2025\\\\n    arxiv_id: \\\\\\\"2509.22601\\\\\\\"\\\\n    category: method-component\\\\n    role: background\\\\n    relevance_note: >\\\\n      Curriculum-based self-imitation for sparse-reward agent tasks.\\\\n      Up to +16.1% on ALFWorld over GRPO. Self-imitation curriculum could augment B-IAVR training.\\\\n\\\\n  - id: wei2025webagent-r1\\\\n    title: \\\\\\\"WebAgent-R1: Training Web Agents via End-to-End Multi-Turn RL\\\\\\\"\\\\n    authors: \\\\\\\"Wei et al.\\\\\\\"\\\\n    venue: \\\\\\\"EMNLP 2025\\\\\\\"\\\\n    year: 2025\\\\n    arxiv_id: \\\\\\\"2505.16421\\\\\\\"\\\\n    category: background\\\\n    role: background\\\\n    relevance_note: >\\\\n      Extends GRPO to multi-turn (M-GRPO) with dynamic context compression.\\\\n      Qwen-2.5-3B: 6.1% to 33.9% on WebArena-Lite. M-GRPO multi-turn extension relevant to B-IAVR.\\\\n\\\\n  - id: dapo2025\\\\n    title: \\\\\\\"DAPO: An Open-Source LLM Reinforcement Learning System at Scale\\\\\\\"\\\\n    authors: \\\\\\\"Yu et al.\\\\\\\"\\\\n    venue: \\\\\\\"arXiv\\\\\\\"\\\\n    year: 2025\\\\n    arxiv_id: \\\\\\\"2503.14476\\\\\\\"\\\\n    category: method-component\\\\n    role: background\\\\n    relevance_note: >\\\\n      RL training stabilization techniques (Clip-Higher, Dynamic Sampling).\\\\n      Applicable to B-IAVR's RL training to prevent entropy collapse.\\\\n\\\\n  - id: digiRL2024\\\\n    title: \\\\\\\"DigiRL: Training In-The-Wild Device-Control Agents with Autonomous RL\\\\\\\"\\\\n    authors: \\\\\\\"Bai et al.\\\\\\\"\\\\n    venue: \\\\\\\"NeurIPS 2024\\\\\\\"\\\\n    year: 2024\\\\n    arxiv_id: \\\\\\\"2406.11896\\\\\\\"\\\\n    category: background\\\\n    role: background\\\\n    relevance_note: >\\\\n      Online RL for device control agents. Demonstrates online RL viability for interactive agents.\\\\n      49.5% absolute improvement over SFT. Parallel approach to B-IAVR in text-based setting.\\\\n\\\\n  - id: li2025sorl\\\\n    title: \\\\\\\"SORL: Stabilizing Off-Policy RL for Long-Horizon Agent Training\\\\\\\"\\\\n    authors: \\\\\\\"Li et al.\\\\\\\"\\\\n    venue: \\\\\\\"arXiv\\\\\\\"\\\\n    year: 2025\\\\n    arxiv_id: \\\\\\\"2511.20718\\\\\\\"\\\\n    category: method-component\\\\n    role: background\\\\n    relevance_note: >\\\\n      Turn-level importance sampling + clipping-triggered normalization for stable multi-turn agent RL.\\\\n      Directly applicable to B-IAVR's multi-turn ALFWorld training stability.\\\\n\\\\n  - id: agentic-rl-survey-2025\\\\n    title: \\\\\\\"The Landscape of Agentic Reinforcement Learning for LLMs: A Survey\\\\\\\"\\\\n    authors: \\\\\\\"Zhang et al.\\\\\\\"\\\\n    venue: \\\\\\\"TMLR 2026\\\\\\\"\\\\n    year: 2025\\\\n    arxiv_id: \\\\\\\"2509.02547\\\\\\\"\\\\n    category: background\\\\n    role: background\\\\n    relevance_note: >\\\\n      Comprehensive survey formalizing agentic RL. Contextualizes B-IAVR as training agents\\\\n      to make meta-decisions (when to verify) via RL within the POMDP framework.\\\\n\\\\n  - id: skillmaster2026\\\\n    title: \\\\\\\"SkillMaster: Toward Autonomous Skill Mastery in LLM Agents\\\\\\\"\\\\n    authors: \\\\\\\"Yang et al.\\\\\\\"\\\\n    venue: \\\\\\\"arXiv\\\\\\\"\\\\n    year: 2026\\\\n    arxiv_id: \\\\\\\"2605.08693\\\\\\\"\\\\n    category: method-component\\\\n    role: background\\\\n    relevance_note: >\\\\n      DualAdv-GRPO: separately estimates advantages for task-solving and skill-editing decisions.\\\\n      +8.8% on ALFWorld, +9.3% on WebShop. DualAdv structure could inform B-IAVR's\\\\n      separation of action and verification advantages.\\\\n\\\\n  - id: t2po2026\\\\n    title: \\\\\\\"T2PO: Uncertainty-Guided Exploration Control for Stable Multi-Turn Agentic RL\\\\\\\"\\\\n    authors: \\\\\\\"Wang et al.\\\\\\\"\\\\n    venue: \\\\\\\"ICML 2026 Spotlight\\\\\\\"\\\\n    year: 2026\\\\n    arxiv_id: \\\\\\\"2605.02178\\\\\\\"\\\\n    category: method-component\\\\n    role: background\\\\n    relevance_note: >\\\\n      Token- and turn-level uncertainty monitoring for stable multi-turn agent RL.\\\\n      Triggers thinking intervention when marginal uncertainty change drops below threshold.\\\\n      Evaluated on ALFWorld and WebShop. Conceptually related: uncertainty-based trigger vs\\\\n      B-IAVR's action-change trigger, but T2PO targets training stability, not deployment verification.\\\\n\\\\n  - id: gvpo2026\\\\n    title: \\\\\\\"GVPO: Group Verification-based Policy Optimization for Interactive Coding Agents\\\\\\\"\\\\n    authors: \\\\\\\"Dai et al.\\\\\\\"\\\\n    venue: \\\\\\\"ICLR 2026\\\\\\\"\\\\n    year: 2026\\\\n    arxiv_id: null  # no arXiv preprint; OpenReview ID: RY47Tq0VsV\\\\n    category: method-component\\\\n    role: background\\\\n    relevance_note: >\\\\n      Advantage shaping with outcome-verifiable + process-verifiable signals.\\\\n      +12.7% over o1 on AppWorld. Integrates intermediate execution feedback as step-level\\\\n      verification signals. Different focus: uses verification for credit assignment during\\\\n      training; B-IAVR learns when to invoke verification at deployment.\\\\n\\\\n  - id: agentv-rl2026\\\\n    title: \\\\\\\"AgentV-RL: Scaling Reward Modeling with Agentic Verifier\\\\\\\"\\\\n    authors: \\\\\\\"Zhang et al.\\\\\\\"\\\\n    venue: \\\\\\\"arXiv\\\\\\\"\\\\n    year: 2026\\\\n    arxiv_id: \\\\\\\"2604.16004\\\\\\\"\\\\n    category: method-component\\\\n    role: background\\\\n    relevance_note: >\\\\n      Bidirectional forward/backward agentic verifier for reward modeling in RL.\\\\n      4B model surpasses SOTA ORMs by 25.2%. Addresses verification quality in reward modeling;\\\\n      B-IAVR addresses verification timing in agent deployment. Complementary.\\\\n\\\\n  - id: pa-moe2026\\\\n    title: \\\\\\\"PA-MoE: Phase-Aware Mixture of Experts for Agentic Reinforcement Learning\\\\\\\"\\\\n    authors: \\\\\\\"Li et al.\\\\\\\"\\\\n    venue: \\\\\\\"arXiv\\\\\\\"\\\\n    year: 2026\\\\n    arxiv_id: \\\\\\\"2602.17038\\\\\\\"\\\\n    category: evaluation\\\\n    role: baseline\\\\n    relevance_note: >\\\\n      [NEW-0516] Lightweight phase router learns latent phase boundaries from RL objective.\\\\n      PA-MoE+GiGPO with Qwen2.5-1.5B achieves 93.8% on ALFWorld (+7.7 over GiGPO 86.1%).\\\\n      1.5B outperforms vanilla 7B GiGPO (90.2%). New small-model SOTA on ALFWorld.\\\\n      Orthogonal architecture innovation; important baseline to cite.\\\\n\\\\n  - id: sdar2026\\\\n    title: \\\\\\\"SDAR: Self-Distilled Agentic Reinforcement Learning\\\\\\\"\\\\n    authors: \\\\\\\"Lu et al.\\\\\\\"\\\\n    venue: \\\\\\\"arXiv\\\\\\\"\\\\n    year: 2026\\\\n    arxiv_id: \\\\\\\"2605.15155\\\\\\\"\\\\n    category: method-component\\\\n    role: background\\\\n    relevance_note: >\\\\n      [NEW-0516] On-policy self-distillation as gated auxiliary objective during RL training.\\\\n      Token-level gate decides supervision intensity. +9.4% over GRPO on ALFWorld.\\\\n      Complementary: SDAR improves RL training; B-IAVR learns verification policy.\\\\n\\\\n  - id: hcapo2026\\\\n    title: \\\\\\\"HCAPO: Hindsight Credit Assignment for Long-Horizon LLM Agents\\\\\\\"\\\\n    authors: \\\\\\\"Tan et al.\\\\\\\"\\\\n    venue: \\\\\\\"arXiv\\\\\\\"\\\\n    year: 2026\\\\n    arxiv_id: \\\\\\\"2603.08754\\\\\\\"\\\\n    category: method-component\\\\n    role: background\\\\n    relevance_note: >\\\\n      [NEW-0516] LLM-as-critic refines step-level Q-values via hindsight reasoning +\\\\n      multi-scale advantage for critical decision states.\\\\n      +13.8% on ALFWorld, +7.7% on WebShop over GRPO (Qwen2.5-7B).\\\\n      Could improve B-IAVR's reward signal for verification decision steps.\\\\n\\\\n  - id: act2026\\\\n    title: \\\\\\\"ACT: Agentic Critical Training\\\\\\\"\\\\n    authors: \\\\\\\"Liu et al.\\\\\\\"\\\\n    venue: \\\\\\\"arXiv\\\\\\\"\\\\n    year: 2026\\\\n    arxiv_id: \\\\\\\"2603.08706\\\\\\\"\\\\n    category: method-component\\\\n    role: background\\\\n    relevance_note: >\\\\n      [NEW-0516] Trains agents to judge action quality via critical comparison reward.\\\\n      +5.07 over IL, +4.62 over RL. Different axis: ACT improves reflection quality;\\\\n      B-IAVR decides when to reflect.\\\\n\\\\n  - id: rwml2026\\\\n    title: \\\\\\\"RWML: Reinforcement World Model Learning for LLM-based Agents\\\\\\\"\\\\n    authors: \\\\\\\"Yu et al.\\\\\\\"\\\\n    venue: \\\\\\\"arXiv\\\\\\\"\\\\n    year: 2026\\\\n    arxiv_id: \\\\\\\"2602.05842\\\\\\\"\\\\n    category: method-component\\\\n    role: background\\\\n    relevance_note: >\\\\n      [NEW-0516] Self-supervised world model via sim-to-real gap rewards in embedding space.\\\\n      +6.9 on ALFWorld over task-success-only RL. Matches expert-data training.\\\\n      Orthogonal: improves internal world model; B-IAVR adds selective verification.\\\\n\\\\n  - id: skill0-2026\\\\n    title: \\\\\\\"SKILL0: In-Context Agentic Reinforcement Learning for Skill Internalization\\\\\\\"\\\\n    authors: \\\\\\\"Lu et al.\\\\\\\"\\\\n    venue: \\\\\\\"arXiv\\\\\\\"\\\\n    year: 2026\\\\n    arxiv_id: \\\\\\\"2604.02268\\\\\\\"\\\\n    category: method-component\\\\n    role: background\\\\n    relevance_note: >\\\\n      [NEW-0516] Training-time curriculum progressively withdraws skill context until zero-shot.\\\\n      +9.7% on ALFWorld over GRPO, <0.5k tokens per step.\\\\n      Complementary: SKILL0 internalizes skills; B-IAVR adds selective verification.\\\\n\\\\n  - id: fission-grpo2026\\\\n    title: \\\\\\\"Fission-GRPO: Robust Tool Use via Learning to Recover from Execution Errors\\\\\\\"\\\\n    authors: \\\\\\\"Zhang et al.\\\\\\\"\\\\n    venue: \\\\\\\"arXiv\\\\\\\"\\\\n    year: 2026\\\\n    arxiv_id: \\\\\\\"2601.15625\\\\\\\"\\\\n    category: method-component\\\\n    role: background\\\\n    relevance_note: >\\\\n      [NEW-0516] Fissions failed trajectories into recovery training instances.\\\\n      +4% overall accuracy on BFCL v4 Multi-Turn over GRPO.\\\\n      Related: error recovery after failure vs B-IAVR's proactive verification.\\\\n\\\\n  - id: selfbudgeter2026\\\\n    title: \\\\\\\"SelfBudgeter: Adaptive Token Allocation for Efficient LLM Reasoning\\\\\\\"\\\\n    authors: \\\\\\\"Li et al.\\\\\\\"\\\\n    venue: \\\\\\\"ICLR 2026 (under review)\\\\\\\"\\\\n    year: 2025\\\\n    arxiv_id: \\\\\\\"2505.11274\\\\\\\"\\\\n    category: background\\\\n    role: background\\\\n    relevance_note: >\\\\n      [NEW-0516] Self-estimated token budgets + budget-guided GRPO. 61% token reduction.\\\\n      Parallel concept: SelfBudgeter allocates computation budget;\\\\n      B-IAVR makes binary verify/not-verify decision. Both use RL for adaptive compute.\\\\n\\\\n  - id: cove2026\\\\n    title: \\\\\\\"CoVe: Training Interactive Tool-Use Agents via Constraint-Guided Verification\\\\\\\"\\\\n    authors: \\\\\\\"Chen et al.\\\\\\\"\\\\n    venue: \\\\\\\"arXiv\\\\\\\"\\\\n    year: 2026\\\\n    arxiv_id: \\\\\\\"2603.01940\\\\\\\"\\\\n    category: background\\\\n    role: background\\\\n    relevance_note: >\\\\n      [NEW-0516] Task constraints guide trajectory generation and serve as deterministic verifiers.\\\\n      Different: CoVe uses verification for data synthesis; B-IAVR learns when to verify at inference.\\\\n\\\\n  # ============================================================\\\\n  # Direction 3: Selective Verification / Adaptive Computation\\\\n  # ============================================================\\\\n\\\\n  - id: wan2025derailer-rerailer\\\\n    title: \\\\\\\"Derailer-Rerailer: Adaptive Verification for Efficient and Reliable LM Reasoning\\\\\\\"\\\\n    authors: \\\\\\\"Wan et al.\\\\\\\"\\\\n    venue: \\\\\\\"ACL 2025 Findings\\\\\\\"\\\\n    year: 2025\\\\n    arxiv_id: \\\\\\\"2408.13940\\\\\\\"\\\\n    category: direct-competitor\\\\n    role: competitor\\\\n    relevance_note: >\\\\n      Most directly related competitor. Both do selective verification with binary trigger.\\\\n      Key difference: operates on reasoning chains (single-turn); B-IAVR on agent trajectories (multi-turn).\\\\n      Uses heuristic instability signal; B-IAVR uses RL-trained action-change signal.\\\\n      8-11% accuracy gain, 2-3x efficiency over uniform verification.\\\\n\\\\n  - id: sherlock2025\\\\n    title: \\\\\\\"Sherlock: Reliable and Efficient Agentic Workflow Execution\\\\\\\"\\\\n    authors: \\\\\\\"Microsoft\\\\\\\"\\\\n    venue: \\\\\\\"arXiv\\\\\\\"\\\\n    year: 2025\\\\n    arxiv_id: \\\\\\\"2511.00330\\\\\\\"\\\\n    category: direct-competitor\\\\n    role: competitor\\\\n    relevance_note: >\\\\n      Selective verification for agentic workflows via offline counterfactual analysis + speculative execution.\\\\n      Different scope: workflow DAG level (offline); B-IAVR is step-level (online RL).\\\\n      18.3% accuracy gain, 26% cost reduction, 48.7% latency reduction.\\\\n\\\\n  - id: singhi2025when-to-verify\\\\n    title: \\\\\\\"When To Solve, When To Verify: Compute-Optimal Verification for LLM Reasoning\\\\\\\"\\\\n    authors: \\\\\\\"Singhi et al.\\\\\\\"\\\\n    venue: \\\\\\\"arXiv\\\\\\\"\\\\n    year: 2025\\\\n    arxiv_id: \\\\\\\"2504.01005\\\\\\\"\\\\n    category: background\\\\n    role: background\\\\n    relevance_note: >\\\\n      Derives inference scaling laws for solve-vs-verify tradeoff.\\\\n      Finding that over-verification is suboptimal directly supports B-IAVR's selective approach.\\\\n      B-IAVR learns this allocation via RL rather than analytically.\\\\n\\\\n  - id: yang2026ares\\\\n    title: \\\\\\\"ARES: Adaptive Reasoning Effort Selection for Efficient LLM Agents\\\\\\\"\\\\n    authors: \\\\\\\"Yang et al.\\\\\\\"\\\\n    venue: \\\\\\\"arXiv\\\\\\\"\\\\n    year: 2026\\\\n    arxiv_id: \\\\\\\"2603.07915\\\\\\\"\\\\n    category: direct-competitor\\\\n    role: competitor\\\\n    relevance_note: >\\\\n      Closest competitor in agent domain. Both train learned per-step compute allocation.\\\\n      ARES uses SFT-initialized router further refined via GRPO with outcome + token efficiency reward;\\\\n      B-IAVR trains binary verify/not-verify via RL with action-change signal.\\\\n      Key differences: (1) reward signal — ARES optimizes token efficiency, B-IAVR uses action-change\\\\n      as verification trigger; (2) data requirement — ARES needs difficulty-annotated training data\\\\n      to bootstrap the router, B-IAVR learns from environment interaction alone.\\\\n      Reduces reasoning tokens by up to 52.7%.\\\\n\\\\n  - id: tu2025autothink\\\\n    title: \\\\\\\"Learning When to Think: Shaping Adaptive Reasoning in R1-Style Models via Multi-Stage RL\\\\\\\"\\\\n    authors: \\\\\\\"Tu et al.\\\\\\\"\\\\n    venue: \\\\\\\"NeurIPS 2025\\\\\\\"\\\\n    year: 2025\\\\n    arxiv_id: \\\\\\\"2505.10832\\\\\\\"\\\\n    category: direct-competitor\\\\n    role: competitor\\\\n    relevance_note: >\\\\n      Analogous idea in reasoning domain: RL-trained adaptive computation trigger.\\\\n      Operates on single-turn reasoning; B-IAVR on multi-turn agent trajectories.\\\\n      +6.4% accuracy, -52% tokens on DeepSeek-R1-Distill-Qwen-1.5B.\\\\n\\\\n  - id: du2025thinkless\\\\n    title: \\\\\\\"Thinkless: LLM Learns When to Think\\\\\\\"\\\\n    authors: \\\\\\\"Fang et al.\\\\\\\"\\\\n    venue: \\\\\\\"NeurIPS 2025\\\\\\\"\\\\n    year: 2025\\\\n    arxiv_id: \\\\\\\"2505.13379\\\\\\\"\\\\n    category: direct-competitor\\\\n    role: competitor\\\\n    relevance_note: >\\\\n      RL-trained control token to decide when to invoke extended thinking.\\\\n      Methodologically closest to B-IAVR in reasoning domain; B-IAVR applies to interactive agent trajectories.\\\\n\\\\n  - id: wang2025efficient-agents\\\\n    title: \\\\\\\"Efficient Agents: Building Effective Agents While Reducing Cost\\\\\\\"\\\\n    authors: \\\\\\\"Wang et al.\\\\\\\"\\\\n    venue: \\\\\\\"arXiv\\\\\\\"\\\\n    year: 2025\\\\n    arxiv_id: \\\\\\\"2508.02694\\\\\\\"\\\\n    category: background\\\\n    role: background\\\\n    relevance_note: >\\\\n      First systematic study of agent efficiency-effectiveness tradeoff.\\\\n      Framework-level cost reduction; B-IAVR addresses cost at verification-policy level.\\\\n      Retains 96.7% performance with 28.4% cost-of-pass improvement.\\\\n\\\\n  - id: venktesh2025trust-but-verify\\\\n    title: \\\\\\\"Trust but Verify! A Survey on Verification Design for Test-time Scaling\\\\\\\"\\\\n    authors: \\\\\\\"Venktesh et al.\\\\\\\"\\\\n    venue: \\\\\\\"arXiv\\\\\\\"\\\\n    year: 2025\\\\n    arxiv_id: \\\\\\\"2508.16665\\\\\\\"\\\\n    category: background\\\\n    role: background\\\\n    relevance_note: >\\\\n      Survey of verification approaches for test-time compute scaling.\\\\n      Identifies verification timing as key open problem. B-IAVR provides concrete solution for agent setting.\\\\n\\\\n  - id: agent-omit2026\\\\n    title: \\\\\\\"Agent-Omit: Training Efficient LLM Agents for Adaptive Thought and Observation Omission via Agentic RL\\\\\\\"\\\\n    authors: \\\\\\\"Ning et al.\\\\\\\"\\\\n    venue: \\\\\\\"ICML 2026\\\\\\\"\\\\n    year: 2026\\\\n    arxiv_id: \\\\\\\"2602.04284\\\\\\\"\\\\n    category: direct-competitor\\\\n    role: competitor\\\\n    relevance_note: >\\\\n      RL-trained policy for adaptive omission of redundant thoughts and observations.\\\\n      Agent-Omit-8B matches frontier agents with best efficiency tradeoff on 5 benchmarks.\\\\n      Both use RL to learn cost-efficient agent behavior. Key difference: Agent-Omit subtracts\\\\n      (omits unnecessary context); B-IAVR selectively adds (verification steps).\\\\n      Opposite but complementary approaches to cost-efficiency. Potentially combinable.\\\\n\\\\n  - id: ava2026\\\\n    title: \\\\\\\"Anytime Verified Agents: Adaptive Compute Allocation for Reliable LLM Reasoning under Budget Constraints\\\\\\\"\\\\n    authors: \\\\\\\"Patel\\\\\\\"\\\\n    venue: \\\\\\\"TMLR 2026\\\\\\\"\\\\n    year: 2026\\\\n    arxiv_id: null  # no arXiv preprint; OpenReview ID: JMDCMf7mlF\\\\n    category: direct-competitor\\\\n    role: competitor\\\\n    relevance_note: >\\\\n      Dynamic compute allocation across search, sampling, and verification under budget.\\\\n      Uses calibrated uncertainty + value-of-information for selective verification cascades.\\\\n      Evaluated on GSM8K/MATH/HotpotQA/HumanEval (reasoning), not interactive agents.\\\\n      Key difference: analytical/heuristic allocation vs B-IAVR's RL-learned policy;\\\\n      single-turn reasoning vs multi-turn agent trajectories.\\\\n\\\\n  - id: cast2026\\\\n    title: \\\\\\\"CAST: Case-Based Calibration of Adaptive Reasoning and Execution for LLM Tool Use\\\\\\\"\\\\n    authors: \\\\\\\"Pang et al.\\\\\\\"\\\\n    venue: \\\\\\\"arXiv\\\\\\\"\\\\n    year: 2026\\\\n    arxiv_id: \\\\\\\"2605.15041\\\\\\\"\\\\n    category: background\\\\n    role: background\\\\n    relevance_note: >\\\\n      Historical execution cases calibrate reasoning depth for tool use.\\\\n      Reduces reasoning length 26% with +5.85% accuracy on BFCLv2/ToolBench.\\\\n      Related: adaptive reasoning depth; different: case-based calibration vs RL-learned policy.\\\\n\\\\n  - id: marginal-token-allocators2026\\\\n    title: \\\\\\\"Agentic AI Systems Should Be Designed as Marginal Token Allocators\\\\\\\"\\\\n    authors: \\\\\\\"Zhu\\\\\\\"\\\\n    venue: \\\\\\\"arXiv\\\\\\\"\\\\n    year: 2026\\\\n    arxiv_id: \\\\\\\"2605.01214\\\\\\\"\\\\n    category: background\\\\n    role: background\\\\n    relevance_note: >\\\\n      Position paper framing agent cost-efficiency as marginal token allocation economics.\\\\n      Identifies under-verification as systematic failure mode. Supports B-IAVR's framing\\\\n      that verification decisions should reflect marginal cost-benefit analysis.\\\\n\\\\n  - id: argos2025\\\\n    title: \\\\\\\"Argos: Multimodal RL with Adaptive Verifier for AI Agents\\\\\\\"\\\\n    authors: \\\\\\\"Tan et al.\\\\\\\"\\\\n    venue: \\\\\\\"arXiv (revised April 2026)\\\\\\\"\\\\n    year: 2025\\\\n    arxiv_id: \\\\\\\"2512.03438\\\\\\\"\\\\n    category: background\\\\n    role: background\\\\n    relevance_note: >\\\\n      Agentic verifier that adaptively selects scoring functions for multimodal RL training.\\\\n      Different domain (multimodal/robotics). The adaptive verifier selection concept is\\\\n      complementary: Argos adapts how to verify; B-IAVR adapts when to verify.\\\\n\\\\n  # ============================================================\\\\n  # Direction 4: ALFWorld / Interactive Environment Benchmarks\\\\n  # ============================================================\\\\n\\\\n  - id: kim2025reflact\\\\n    title: \\\\\\\"ReflAct: World-Grounded Decision Making in LLM Agents via Goal-State Reflection\\\\\\\"\\\\n    authors: \\\\\\\"Kim et al.\\\\\\\"\\\\n    venue: \\\\\\\"EMNLP 2025\\\\\\\"\\\\n    year: 2025\\\\n    arxiv_id: \\\\\\\"2505.15182\\\\\\\"\\\\n    category: evaluation\\\\n    role: baseline\\\\n    relevance_note: >\\\\n      Prompting SOTA on ALFWorld at 93.3%. Replaces ReAct's next-action thinking with state-goal reflection.\\\\n      B-IAVR addresses different axis (cost-efficiency) since ALFWorld accuracy is near saturation.\\\\n\\\\n  - id: choudhury2025agentprm\\\\n    title: \\\\\\\"Process Reward Models for LLM Agents: Practical Framework and Directions\\\\\\\"\\\\n    authors: \\\\\\\"Choudhury\\\\\\\"\\\\n    venue: \\\\\\\"arXiv\\\\\\\"\\\\n    year: 2025\\\\n    arxiv_id: \\\\\\\"2502.10325\\\\\\\"\\\\n    category: evaluation\\\\n    role: baseline\\\\n    relevance_note: >\\\\n      Monte Carlo rollout-based process reward for agent training. 3B models achieve 91% on ALFWorld.\\\\n      Validates RL training approach; AgentPRM could serve as reward model for B-IAVR.\\\\n\\\\n  - id: xi2025agentprm\\\\n    title: \\\\\\\"AgentPRM: Process Reward Models for LLM Agents via Step-Wise Promise and Progress\\\\\\\"\\\\n    authors: \\\\\\\"Xi et al.\\\\\\\"\\\\n    venue: \\\\\\\"ACM Web Conference 2026\\\\\\\"\\\\n    year: 2025\\\\n    arxiv_id: \\\\\\\"2511.08325\\\\\\\"\\\\n    category: evaluation\\\\n    role: baseline\\\\n    relevance_note: >\\\\n      Independent work from Choudhury et al., using TD-based estimation with GAE for scalable\\\\n      PRM data labeling. 8x more compute-efficient than baselines with robust test-time scaling.\\\\n      Different approach: Choudhury uses MC rollouts; Xi uses TD+GAE for step-wise promise and progress.\\\\n\\\\n  - id: xiang2024retrospex\\\\n    title: \\\\\\\"Retrospex: Language Agent Meets Offline RL Critic\\\\\\\"\\\\n    authors: \\\\\\\"Xiang et al.\\\\\\\"\\\\n    venue: \\\\\\\"EMNLP 2024\\\\\\\"\\\\n    year: 2024\\\\n    arxiv_id: \\\\\\\"2505.11807\\\\\\\"\\\\n    category: background\\\\n    role: background\\\\n    relevance_note: >\\\\n      Offline RL Critic augments LLM agent action selection via dynamic rescoring.\\\\n      Similar architecture could inform B-IAVR's verification value estimation.\\\\n\\\\n  - id: cfgm2025\\\\n    title: \\\\\\\"CFGM: Coarse-to-Fine Grounded Memory for LLM Agent Planning\\\\\\\"\\\\n    authors: \\\\\\\"Yang et al.\\\\\\\"\\\\n    venue: \\\\\\\"EMNLP 2025\\\\\\\"\\\\n    year: 2025\\\\n    arxiv_id: \\\\\\\"2508.15305\\\\\\\"\\\\n    category: background\\\\n    role: background\\\\n    relevance_note: >\\\\n      Memory-augmented agent planning with episodic grounding.\\\\n      ALFWorld +10.40%, WebShop +20%. Complementary to B-IAVR's verification approach.\\\\n\\\\n  - id: respact2024\\\\n    title: \\\\\\\"ReSpAct: Harmonizing Reasoning, Speaking, and Acting\\\\\\\"\\\\n    authors: \\\\\\\"Dongre et al.\\\\\\\"\\\\n    venue: \\\\\\\"arXiv\\\\\\\"\\\\n    year: 2024\\\\n    arxiv_id: \\\\\\\"2411.00927\\\\\\\"\\\\n    category: evaluation\\\\n    role: baseline\\\\n    relevance_note: >\\\\n      Integrates dialogue/reasoning/acting. +6% over ReAct on ALFWorld.\\\\n      Reduces invalid actions from 13% to 3%; B-IAVR's verification achieves error prevention differently.\\\\n\\\\n  # ============================================================\\\\n  # Direction 5: Multi-Turn Credit Assignment (Direct Competitors)\\\\n  # ============================================================\\\\n\\\\n  - id: turn-ppo2025\\\\n    title: \\\\\\\"Turn-Level Policy Optimization for Multi-Turn Agent Reinforcement Learning\\\\\\\"\\\\n    authors: \\\\\\\"Zhou et al.\\\\\\\"\\\\n    venue: \\\\\\\"arXiv\\\\\\\"\\\\n    year: 2025\\\\n    arxiv_id: \\\\\\\"2512.17008\\\\\\\"\\\\n    category: direct-competitor\\\\n    role: competitor\\\\n    relevance_note: >\\\\n      [NEW-0517] Most direct competitor. Identifies \\\\\\\"uniform advantage\\\\\\\" problem in\\\\n      step-independent GRPO (subset of our \\\\\\\"sign misattribution\\\\\\\"). Proposes turn-level\\\\n      MDP + learned value function. Our differences: (1) more precise formalization\\\\n      (sign misattribution + gamma decay quantification), (2) contrarian solution\\\\n      (episode-level coarser credit vs their finer turn-level credit).\\\\n\\\\n  - id: gagpo2026\\\\n    title: \\\\\\\"GAGPO: Generalized Advantage Grouped Policy Optimization\\\\\\\"\\\\n    authors: \\\\\\\"Zhu et al.\\\\\\\"\\\\n    venue: \\\\\\\"arXiv\\\\\\\"\\\\n    year: 2026\\\\n    arxiv_id: \\\\\\\"2605.13217\\\\\\\"\\\\n    category: direct-competitor\\\\n    role: competitor\\\\n    relevance_note: >\\\\n      [NEW-0517] Critic-free step-aligned credit via non-parametric grouped value proxy +\\\\n      TD/GAE-style temporal advantages. ALFWorld 93.5% (1.5B), 95.6% (7B).\\\\n      Pursues finer-grained credit to improve performance; our work diagnoses why\\\\n      step-independent fails (sign misattribution) and shows coarser episode-level suffices.\\\\n      Different contribution axis: performance optimization vs mechanism diagnosis.\\\\n\\\\n  - id: mt-grpo2025\\\\n    title: \\\\\\\"Reinforcing Multi-Turn Reasoning in LLM Agents via Turn-Level Reward Design\\\\\\\"\\\\n    authors: \\\\\\\"Wei et al.\\\\\\\"\\\\n    venue: \\\\\\\"arXiv\\\\\\\"\\\\n    year: 2025\\\\n    arxiv_id: \\\\\\\"2505.11821\\\\\\\"\\\\n    category: direct-competitor\\\\n    role: competitor\\\\n    relevance_note: >\\\\n      [NEW-0517] Proposes MT-GRPO with turn-level reward design for multi-turn RL.\\\\n      Evaluated on QA search tasks (NQ, TriviaQA, HotpotQA), not ALFWorld.\\\\n      Qwen2.5-7B. Same direction as Turn-PPO (finer turn-level credit);\\\\n      our contrarian shows coarser episode-level eliminates sign misattribution.\\\\n\\\\n  - id: istar2025\\\\n    title: \\\\\\\"Agentic Reinforcement Learning with Implicit Step Rewards\\\\\\\"\\\\n    authors: \\\\\\\"Liu et al.\\\\\\\"\\\\n    venue: \\\\\\\"ICLR 2026\\\\\\\"\\\\n    year: 2025\\\\n    arxiv_id: \\\\\\\"2509.19199\\\\\\\"\\\\n    category: direct-competitor\\\\n    role: competitor\\\\n    relevance_note: >\\\\n      [NEW-0517] Implicit PRM + dual advantage (step + episode level) for agentic RL.\\\\n      WebShop 86.5%, VisualSokoban 91.7%. ICLR 2026 published.\\\\n      Learns step-level credit via implicit rewards without explicit labels;\\\\n      our work shows episode-level alone suffices when sign misattribution is the bottleneck.\\\\n      Validates that step-level credit helps, but doesn't diagnose when it hurts.\\\\n\\\\n  - id: archer2024\\\\n    title: \\\\\\\"ArCHer: Training Language Model Agents via Hierarchical Multi-Turn RL\\\\\\\"\\\\n    authors: \\\\\\\"Zhou, Zanette, Pan, Levine, Kumar\\\\\\\"\\\\n    venue: \\\\\\\"ICML 2024\\\\\\\"\\\\n    year: 2024\\\\n    arxiv_id: \\\\\\\"2402.19446\\\\\\\"\\\\n    category: method-component\\\\n    role: predecessor\\\\n    relevance_note: >\\\\n      [NEW-0517] Foundational hierarchical multi-turn RL framework (ICML 2024).\\\\n      High-level off-policy value RL (utterance-level) + low-level token policy.\\\\n      ~100x sample efficiency. Establishes that multi-turn RL needs hierarchical structure;\\\\n      our work specifically diagnoses why flat step-independent approaches fail.\\\\n\\\\n  - id: ca-survey2026\\\\n    title: \\\\\\\"From Reasoning to Agentic: Credit Assignment in Reinforcement Learning for Large Language Models\\\\\\\"\\\\n    authors: \\\\\\\"Zhang\\\\\\\"\\\\n    venue: \\\\\\\"arXiv\\\\\\\"\\\\n    year: 2026\\\\n    arxiv_id: \\\\\\\"2604.09459\\\\\\\"\\\\n    category: background\\\\n    role: background\\\\n    relevance_note: >\\\\n      [NEW-0517] Comprehensive survey of 47 CA methods (2024-2026). Two-dimensional\\\\n      taxonomy: granularity (token/segment/step/turn/multi-agent) x methodology\\\\n      (MC/TD/model-based/game-theoretic/information-theoretic). Contextualizes our\\\\n      sign misattribution diagnosis within the broader CA landscape.\\\\n\\\\n  - id: hiper2026\\\\n    title: \\\\\\\"HiPER: Hierarchical Reinforcement Learning with Explicit Credit Assignment for Large Language Model Agents\\\\\\\"\\\\n    authors: \\\\\\\"Peng et al.\\\\\\\"\\\\n    venue: \\\\\\\"arXiv\\\\\\\"\\\\n    year: 2026\\\\n    arxiv_id: \\\\\\\"2602.16165\\\\\\\"\\\\n    category: method-component\\\\n    role: background\\\\n    relevance_note: >\\\\n      [NEW-0517] Hierarchical Plan-Execute RL. ALFWorld 97.4% (7B), 95.3% (1.5B).\\\\n      GRPO baseline: 71.1% (1.5B), 85.4% (7B). 2.8x training efficiency gain.\\\\n      Pursues SOTA performance via hierarchical plan-execute architecture;\\\\n      our work does mechanism diagnosis of why step-independent GRPO fails.\\\\n      Different contribution dimension: not comparable on performance axis.\\\\n\\\", \\\"total_chars\\\": 29915, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/literature_map.yaml\", \"content\": \"# B-IAVR Literature Map\\n# Updated: 2026-05-17\\n# Categories: direct-competitor, method-component, background, evaluation\\n# Roles: predecessor, competitor, baseline, evaluation, background\\n\\npapers:\\n\\n  # ============================================================\\n  # Direction 1: Self-Verification / Self-Correction in LLM Agents\\n  # ============================================================\\n\\n  - id: kamoi2024self-correction-survey\\n    title: \\\"When Can LLMs Actually Correct Their Own Mistakes? A Critical Survey of Self-Correction of LLMs\\\"\\n    authors: \\\"Kamoi et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2024\\n    arxiv_id: \\\"2406.01297\\\"\\n    category: background\\n    role: background\\n    relevance_note: >\\n      Foundational survey establishing that pure intrinsic self-correction is unreliable.\\n      Validates B-IAVR's use of grounded verification (environment re-observation) over prompted self-feedback.\\n\\n  - id: tie2025correctbench\\n    title: \\\"Can LLMs Correct Themselves? A Benchmark of Self-Correction in LLMs\\\"\\n    authors: \\\"Tie et al.\\\"\\n    venue: \\\"NeurIPS 2025 Datasets & Benchmarks\\\"\\n    year: 2025\\n    arxiv_id: \\\"2510.16062\\\"\\n    category: background\\n    role: background\\n    relevance_note: >\\n      Benchmark showing self-correction has diminishing returns when applied uniformly.\\n      Supports B-IAVR's selective verification design over blanket correction.\\n\\n  - id: self-verification-dilemma-2026\\n    title: \\\"Self-Verification Dilemma: Experience-Driven Suppression of Overused Checking in LLM Reasoning\\\"\\n    authors: \\\"Long et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2026\\n    arxiv_id: \\\"2602.03485\\\"\\n    category: background\\n    role: background\\n    relevance_note: >\\n      Empirically validates that >90% of self-verification is confirmatory, ~2% corrective.\\n      Directly supports B-IAVR's core thesis that verification should be selective.\\n      Their experience-pool approach is complementary to B-IAVR's action-change signal.\\n\\n  - id: zhang2025incentivize-self-verify\\n    title: \\\"Incentivizing LLMs to Self-Verify Their Answers\\\"\\n    authors: \\\"Zhang et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2025\\n    arxiv_id: \\\"2506.01369\\\"\\n    category: background\\n    role: background\\n    relevance_note: >\\n      Unifies answer generation and verification via single RL training process.\\n      Parallel to B-IAVR: they train verification into generation; B-IAVR trains when to trigger separate verification.\\n\\n  - id: mar2025\\n    title: \\\"MAR: Multi-Agent Reflexion Improves Reasoning Abilities in LLMs\\\"\\n    authors: \\\"Ozer et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2025\\n    arxiv_id: \\\"2512.20845\\\"\\n    category: background\\n    role: background\\n    relevance_note: >\\n      Multi-agent self-correction with diverse critic personas.\\n      Complementary: MAR improves correction quality; B-IAVR decides when to trigger correction.\\n\\n  - id: ssr2025\\n    title: \\\"SSR: Socratic Self-Refine for Large Language Model Reasoning\\\"\\n    authors: \\\"Shi et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2025\\n    arxiv_id: \\\"2511.10621\\\"\\n    category: background\\n    role: background\\n    relevance_note: >\\n      Structured Socratic questioning for self-refinement.\\n      Complementary: improves correction step quality; B-IAVR focuses on when to invoke correction.\\n\\n  - id: verifiagent2025\\n    title: \\\"VerifiAgent: a Unified Verification Agent in Language Model Reasoning\\\"\\n    authors: \\\"Han et al.\\\"\\n    venue: \\\"EMNLP 2025 Findings\\\"\\n    year: 2025\\n    arxiv_id: \\\"2504.00406\\\"\\n    category: background\\n    role: background\\n    relevance_note: >\\n      Unified verification agent with meta-verification + tool-based adaptive verification.\\n      Focuses on how to verify (tool selection); B-IAVR focuses on when to verify (policy learning).\\n      Complementary: VerifiAgent's verification quality could enhance B-IAVR's verification step.\\n\\n  # ============================================================\\n  # Direction 2: Agent RL Training\\n  # ============================================================\\n\\n  - id: feng2025gigpo\\n    title: \\\"GiGPO: Group-in-Group Policy Optimization for LLM Agent Training\\\"\\n    authors: \\\"Feng et al.\\\"\\n    venue: \\\"NeurIPS 2025\\\"\\n    year: 2025\\n    arxiv_id: \\\"2505.10978\\\"\\n    category: method-component\\n    role: predecessor\\n    relevance_note: >\\n      Core training algorithm for B-IAVR. Nested group structure provides step-level credit\\n      assignment without learned critic. >12% over GRPO on ALFWorld, >9% on WebShop.\\n\\n  - id: selfguide2026\\n    title: \\\"Co-Evolution of Policy and Internal Reward for Language Agents (Self-Guide)\\\"\\n    authors: \\\"Wang et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2026\\n    arxiv_id: \\\"2604.03098\\\"\\n    category: method-component\\n    role: predecessor\\n    relevance_note: >\\n      Direct predecessor. B-IAVR extends Self-Guide's co-evolving internal reward.\\n      The self-guidance signal is the foundation for action-change detection triggering verification.\\n      8% improvement over env-reward-only on ALFWorld with Qwen3-1.7B/4B.\\n\\n  - id: spear2025\\n    title: \\\"Learn the Ropes, Then Trust the Wins: Self-imitation with Progressive Exploration for Agentic Reinforcement Learning\\\"\\n    authors: \\\"Qin et al.\\\"\\n    venue: \\\"ICLR 2026\\\"\\n    year: 2025\\n    arxiv_id: \\\"2509.22601\\\"\\n    category: method-component\\n    role: background\\n    relevance_note: >\\n      Curriculum-based self-imitation for sparse-reward agent tasks.\\n      Up to +16.1% on ALFWorld over GRPO. Self-imitation curriculum could augment B-IAVR training.\\n\\n  - id: wei2025webagent-r1\\n    title: \\\"WebAgent-R1: Training Web Agents via End-to-End Multi-Turn RL\\\"\\n    authors: \\\"Wei et al.\\\"\\n    venue: \\\"EMNLP 2025\\\"\\n    year: 2025\\n    arxiv_id: \\\"2505.16421\\\"\\n    category: background\\n    role: background\\n    relevance_note: >\\n      Extends GRPO to multi-turn (M-GRPO) with dynamic context compression.\\n      Qwen-2.5-3B: 6.1% to 33.9% on WebArena-Lite. M-GRPO multi-turn extension relevant to B-IAVR.\\n\\n  - id: dapo2025\\n    title: \\\"DAPO: An Open-Source LLM Reinforcement Learning System at Scale\\\"\\n    authors: \\\"Yu et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2025\\n    arxiv_id: \\\"2503.14476\\\"\\n    category: method-component\\n    role: background\\n    relevance_note: >\\n      RL training stabilization techniques (Clip-Higher, Dynamic Sampling).\\n      Applicable to B-IAVR's RL training to prevent entropy collapse.\\n\\n  - id: digiRL2024\\n    title: \\\"DigiRL: Training In-The-Wild Device-Control Agents with Autonomous RL\\\"\\n    authors: \\\"Bai et al.\\\"\\n    venue: \\\"NeurIPS 2024\\\"\\n    year: 2024\\n    arxiv_id: \\\"2406.11896\\\"\\n    category: background\\n    role: background\\n    relevance_note: >\\n      Online RL for device control agents. Demonstrates online RL viability for interactive agents.\\n      49.5% absolute improvement over SFT. Parallel approach to B-IAVR in text-based setting.\\n\\n  - id: li2025sorl\\n    title: \\\"SORL: Stabilizing Off-Policy RL for Long-Horizon Agent Training\\\"\\n    authors: \\\"Li et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2025\\n    arxiv_id: \\\"2511.20718\\\"\\n    category: method-component\\n    role: background\\n    relevance_note: >\\n      Turn-level importance sampling + clipping-triggered normalization for stable multi-turn agent RL.\\n      Directly applicable to B-IAVR's multi-turn ALFWorld training stability.\\n\\n  - id: agentic-rl-survey-2025\\n    title: \\\"The Landscape of Agentic Reinforcement Learning for LLMs: A Survey\\\"\\n    authors: \\\"Zhang et al.\\\"\\n    venue: \\\"TMLR 2026\\\"\\n    year: 2025\\n    arxiv_id: \\\"2509.02547\\\"\\n    category: background\\n    role: background\\n    relevance_note: >\\n      Comprehensive survey formalizing agentic RL. Contextualizes B-IAVR as training agents\\n      to make meta-decisions (when to verify) via RL within the POMDP framework.\\n\\n  - id: skillmaster2026\\n    title: \\\"SkillMaster: Toward Autonomous Skill Mastery in LLM Agents\\\"\\n    authors: \\\"Yang et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2026\\n    arxiv_id: \\\"2605.08693\\\"\\n    category: method-component\\n    role: background\\n    relevance_note: >\\n      DualAdv-GRPO: separately estimates advantages for task-solving and skill-editing decisions.\\n      +8.8% on ALFWorld, +9.3% on WebShop. DualAdv structure could inform B-IAVR's\\n      separation of action and verification advantages.\\n\\n  - id: t2po2026\\n    title: \\\"T2PO: Uncertainty-Guided Exploration Control for Stable Multi-Turn Agentic RL\\\"\\n    authors: \\\"Wang et al.\\\"\\n    venue: \\\"ICML 2026 Spotlight\\\"\\n    year: 2026\\n    arxiv_id: \\\"2605.02178\\\"\\n    category: method-component\\n    role: background\\n    relevance_note: >\\n      Token- and turn-level uncertainty monitoring for stable multi-turn agent RL.\\n      Triggers thinking intervention when marginal uncertainty change drops below threshold.\\n      Evaluated on ALFWorld and WebShop. Conceptually related: uncertainty-based trigger vs\\n      B-IAVR's action-change trigger, but T2PO targets training stability, not deployment verification.\\n\\n  - id: gvpo2026\\n    title: \\\"GVPO: Group Verification-based Policy Optimization for Interactive Coding Agents\\\"\\n    authors: \\\"Dai et al.\\\"\\n    venue: \\\"ICLR 2026\\\"\\n    year: 2026\\n    arxiv_id: null  # no arXiv preprint; OpenReview ID: RY47Tq0VsV\\n    category: method-component\\n    role: background\\n    relevance_note: >\\n      Advantage shaping with outcome-verifiable + process-verifiable signals.\\n      +12.7% over o1 on AppWorld. Integrates intermediate execution feedback as step-level\\n      verification signals. Different focus: uses verification for credit assignment during\\n      training; B-IAVR learns when to invoke verification at deployment.\\n\\n  - id: agentv-rl2026\\n    title: \\\"AgentV-RL: Scaling Reward Modeling with Agentic Verifier\\\"\\n    authors: \\\"Zhang et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2026\\n    arxiv_id: \\\"2604.16004\\\"\\n    category: method-component\\n    role: background\\n    relevance_note: >\\n      Bidirectional forward/backward agentic verifier for reward modeling in RL.\\n      4B model surpasses SOTA ORMs by 25.2%. Addresses verification quality in reward modeling;\\n      B-IAVR addresses verification timing in agent deployment. Complementary.\\n\\n  - id: pa-moe2026\\n    title: \\\"PA-MoE: Phase-Aware Mixture of Experts for Agentic Reinforcement Learning\\\"\\n    authors: \\\"Li et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2026\\n    arxiv_id: \\\"2602.17038\\\"\\n    category: evaluation\\n    role: baseline\\n    relevance_note: >\\n      [NEW-0516] Lightweight phase router learns latent phase boundaries from RL objective.\\n      PA-MoE+GiGPO with Qwen2.5-1.5B achieves 93.8% on ALFWorld (+7.7 over GiGPO 86.1%).\\n      1.5B outperforms vanilla 7B GiGPO (90.2%). New small-model SOTA on ALFWorld.\\n      Orthogonal architecture innovation; important baseline to cite.\\n\\n  - id: sdar2026\\n    title: \\\"SDAR: Self-Distilled Agentic Reinforcement Learning\\\"\\n    authors: \\\"Lu et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2026\\n    arxiv_id: \\\"2605.15155\\\"\\n    category: method-component\\n    role: background\\n    relevance_note: >\\n      [NEW-0516] On-policy self-distillation as gated auxiliary objective during RL training.\\n      Token-level gate decides supervision intensity. +9.4% over GRPO on ALFWorld.\\n      Complementary: SDAR improves RL training; B-IAVR learns verification policy.\\n\\n  - id: hcapo2026\\n    title: \\\"HCAPO: Hindsight Credit Assignment for Long-Horizon LLM Agents\\\"\\n    authors: \\\"Tan et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2026\\n    arxiv_id: \\\"2603.08754\\\"\\n    category: method-component\\n    role: background\\n    relevance_note: >\\n      [NEW-0516] LLM-as-critic refines step-level Q-values via hindsight reasoning +\\n      multi-scale advantage for critical decision states.\\n      +13.8% on ALFWorld, +7.7% on WebShop over GRPO (Qwen2.5-7B).\\n      Could improve B-IAVR's reward signal for verification decision steps.\\n\\n  - id: act2026\\n    title: \\\"ACT: Agentic Critical Training\\\"\\n    authors: \\\"Liu et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2026\\n    arxiv_id: \\\"2603.08706\\\"\\n    category: method-component\\n    role: background\\n    relevance_note: >\\n      [NEW-0516] Trains agents to judge action quality via critical comparison reward.\\n      +5.07 over IL, +4.62 over RL. Different axis: ACT improves reflection quality;\\n      B-IAVR decides when to reflect.\\n\\n  - id: rwml2026\\n    title: \\\"RWML: Reinforcement World Model Learning for LLM-based Agents\\\"\\n    authors: \\\"Yu et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2026\\n    arxiv_id: \\\"2602.05842\\\"\\n    category: method-component\\n    role: background\\n    relevance_note: >\\n      [NEW-0516] Self-supervised world model via sim-to-real gap rewards in embedding space.\\n      +6.9 on ALFWorld over task-success-only RL. Matches expert-data training.\\n      Orthogonal: improves internal world model; B-IAVR adds selective verification.\\n\\n  - id: skill0-2026\\n    title: \\\"SKILL0: In-Context Agentic Reinforcement Learning for Skill Internalization\\\"\\n    authors: \\\"Lu et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2026\\n    arxiv_id: \\\"2604.02268\\\"\\n    category: method-component\\n    role: background\\n    relevance_note: >\\n      [NEW-0516] Training-time curriculum progressively withdraws skill context until zero-shot.\\n      +9.7% on ALFWorld over GRPO, <0.5k tokens per step.\\n      Complementary: SKILL0 internalizes skills; B-IAVR adds selective verification.\\n\\n  - id: fission-grpo2026\\n    title: \\\"Fission-GRPO: Robust Tool Use via Learning to Recover from Execution Errors\\\"\\n    authors: \\\"Zhang et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2026\\n    arxiv_id: \\\"2601.15625\\\"\\n    category: method-component\\n    role: background\\n    relevance_note: >\\n      [NEW-0516] Fissions failed trajectories into recovery training instances.\\n      +4% overall accuracy on BFCL v4 Multi-Turn over GRPO.\\n      Related: error recovery after failure vs B-IAVR's proactive verification.\\n\\n  - id: selfbudgeter2026\\n    title: \\\"SelfBudgeter: Adaptive Token Allocation for Efficient LLM Reasoning\\\"\\n    authors: \\\"Li et al.\\\"\\n    venue: \\\"ICLR 2026 (under review)\\\"\\n    year: 2025\\n    arxiv_id: \\\"2505.11274\\\"\\n    category: background\\n    role: background\\n    relevance_note: >\\n      [NEW-0516] Self-estimated token budgets + budget-guided GRPO. 61% token reduction.\\n      Parallel concept: SelfBudgeter allocates computation budget;\\n      B-IAVR makes binary verify/not-verify decision. Both use RL for adaptive compute.\\n\\n  - id: cove2026\\n    title: \\\"CoVe: Training Interactive Tool-Use Agents via Constraint-Guided Verification\\\"\\n    authors: \\\"Chen et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2026\\n    arxiv_id: \\\"2603.01940\\\"\\n    category: background\\n    role: background\\n    relevance_note: >\\n      [NEW-0516] Task constraints guide trajectory generation and serve as deterministic verifiers.\\n      Different: CoVe uses verification for data synthesis; B-IAVR learns when to verify at inference.\\n\\n  # ============================================================\\n  # Direction 3: Selective Verification / Adaptive Computation\\n  # ============================================================\\n\\n  - id: wan2025derailer-rerailer\\n    title: \\\"Derailer-Rerailer: Adaptive Verification for Efficient and Reliable LM Reasoning\\\"\\n    authors: \\\"Wan et al.\\\"\\n    venue: \\\"ACL 2025 Findings\\\"\\n    year: 2025\\n    arxiv_id: \\\"2408.13940\\\"\\n    category: direct-competitor\\n    role: competitor\\n    relevance_note: >\\n      Most directly related competitor. Both do selective verification with binary trigger.\\n      Key difference: operates on reasoning chains (single-turn); B-IAVR on agent trajectories (multi-turn).\\n      Uses heuristic instability signal; B-IAVR uses RL-trained action-change signal.\\n      8-11% accuracy gain, 2-3x efficiency over uniform verification.\\n\\n  - id: sherlock2025\\n    title: \\\"Sherlock: Reliable and Efficient Agentic Workflow Execution\\\"\\n    authors: \\\"Microsoft\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2025\\n    arxiv_id: \\\"2511.00330\\\"\\n    category: direct-competitor\\n    role: competitor\\n    relevance_note: >\\n      Selective verification for agentic workflows via offline counterfactual analysis + speculative execution.\\n      Different scope: workflow DAG level (offline); B-IAVR is step-level (online RL).\\n      18.3% accuracy gain, 26% cost reduction, 48.7% latency reduction.\\n\\n  - id: singhi2025when-to-verify\\n    title: \\\"When To Solve, When To Verify: Compute-Optimal Verification for LLM Reasoning\\\"\\n    authors: \\\"Singhi et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2025\\n    arxiv_id: \\\"2504.01005\\\"\\n    category: background\\n    role: background\\n    relevance_note: >\\n      Derives inference scaling laws for solve-vs-verify tradeoff.\\n      Finding that over-verification is suboptimal directly supports B-IAVR's selective approach.\\n      B-IAVR learns this allocation via RL rather than analytically.\\n\\n  - id: yang2026ares\\n    title: \\\"ARES: Adaptive Reasoning Effort Selection for Efficient LLM Agents\\\"\\n    authors: \\\"Yang et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2026\\n    arxiv_id: \\\"2603.07915\\\"\\n    category: direct-competitor\\n    role: competitor\\n    relevance_note: >\\n      Closest competitor in agent domain. Both train learned per-step compute allocation.\\n      ARES uses SFT-initialized router further refined via GRPO with outcome + token efficiency reward;\\n      B-IAVR trains binary verify/not-verify via RL with action-change signal.\\n      Key differences: (1) reward signal — ARES optimizes token efficiency, B-IAVR uses action-change\\n      as verification trigger; (2) data requirement — ARES needs difficulty-annotated training data\\n      to bootstrap the router, B-IAVR learns from environment interaction alone.\\n      Reduces reasoning tokens by up to 52.7%.\\n\\n  - id: tu2025autothink\\n    title: \\\"Learning When to Think: Shaping Adaptive Reasoning in R1-Style Models via Multi-Stage RL\\\"\\n    authors: \\\"Tu et al.\\\"\\n    venue: \\\"NeurIPS 2025\\\"\\n    year: 2025\\n    arxiv_id: \\\"2505.10832\\\"\\n    category: direct-competitor\\n    role: competitor\\n    relevance_note: >\\n      Analogous idea in reasoning domain: RL-trained adaptive computation trigger.\\n      Operates on single-turn reasoning; B-IAVR on multi-turn agent trajectories.\\n      +6.4% accuracy, -52% tokens on DeepSeek-R1-Distill-Qwen-1.5B.\\n\\n  - id: du2025thinkless\\n    title: \\\"Thinkless: LLM Learns When to Think\\\"\\n    authors: \\\"Fang et al.\\\"\\n    venue: \\\"NeurIPS 2025\\\"\\n    year: 2025\\n    arxiv_id: \\\"2505.13379\\\"\\n    category: direct-competitor\\n    role: competitor\\n    relevance_note: >\\n      RL-trained control token to decide when to invoke extended thinking.\\n      Methodologically closest to B-IAVR in reasoning domain; B-IAVR applies to interactive agent trajectories.\\n\\n  - id: wang2025efficient-agents\\n    title: \\\"Efficient Agents: Building Effective Agents While Reducing Cost\\\"\\n    authors: \\\"Wang et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2025\\n    arxiv_id: \\\"2508.02694\\\"\\n    category: background\\n    role: background\\n    relevance_note: >\\n      First systematic study of agent efficiency-effectiveness tradeoff.\\n      Framework-level cost reduction; B-IAVR addresses cost at verification-policy level.\\n      Retains 96.7% performance with 28.4% cost-of-pass improvement.\\n\\n  - id: venktesh2025trust-but-verify\\n    title: \\\"Trust but Verify! A Survey on Verification Design for Test-time Scaling\\\"\\n    authors: \\\"Venktesh et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2025\\n    arxiv_id: \\\"2508.16665\\\"\\n    category: background\\n    role: background\\n    relevance_note: >\\n      Survey of verification approaches for test-time compute scaling.\\n      Identifies verification timing as key open problem. B-IAVR provides concrete solution for agent setting.\\n\\n  - id: agent-omit2026\\n    title: \\\"Agent-Omit: Training Efficient LLM Agents for Adaptive Thought and Observation Omission via Agentic RL\\\"\\n    authors: \\\"Ning et al.\\\"\\n    venue: \\\"ICML 2026\\\"\\n    year: 2026\\n    arxiv_id: \\\"2602.04284\\\"\\n    category: direct-competitor\\n    role: competitor\\n    relevance_note: >\\n      RL-trained policy for adaptive omission of redundant thoughts and observations.\\n      Agent-Omit-8B matches frontier agents with best efficiency tradeoff on 5 benchmarks.\\n      Both use RL to learn cost-efficient agent behavior. Key difference: Agent-Omit subtracts\\n      (omits unnecessary context); B-IAVR selectively adds (verification steps).\\n      Opposite but complementary approaches to cost-efficiency. Potentially combinable.\\n\\n  - id: ava2026\\n    title: \\\"Anytime Verified Agents: Adaptive Compute Allocation for Reliable LLM Reasoning under Budget Constraints\\\"\\n    authors: \\\"Patel\\\"\\n    venue: \\\"TMLR 2026\\\"\\n    year: 2026\\n    arxiv_id: null  # no arXiv preprint; OpenReview ID: JMDCMf7mlF\\n    category: direct-competitor\\n    role: competitor\\n    relevance_note: >\\n      Dynamic compute allocation across search, sampling, and verification under budget.\\n      Uses calibrated uncertainty + value-of-information for selective verification cascades.\\n      Evaluated on GSM8K/MATH/HotpotQA/HumanEval (reasoning), not interactive agents.\\n      Key difference: analytical/heuristic allocation vs B-IAVR's RL-learned policy;\\n      single-turn reasoning vs multi-turn agent trajectories.\\n\\n  - id: cast2026\\n    title: \\\"CAST: Case-Based Calibration of Adaptive Reasoning and Execution for LLM Tool Use\\\"\\n    authors: \\\"Pang et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2026\\n    arxiv_id: \\\"2605.15041\\\"\\n    category: background\\n    role: background\\n    relevance_note: >\\n      Historical execution cases calibrate reasoning depth for tool use.\\n      Reduces reasoning length 26% with +5.85% accuracy on BFCLv2/ToolBench.\\n      Related: adaptive reasoning depth; different: case-based calibration vs RL-learned policy.\\n\\n  - id: marginal-token-allocators2026\\n    title: \\\"Agentic AI Systems Should Be Designed as Marginal Token Allocators\\\"\\n    authors: \\\"Zhu\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2026\\n    arxiv_id: \\\"2605.01214\\\"\\n    category: background\\n    role: background\\n    relevance_note: >\\n      Position paper framing agent cost-efficiency as marginal token allocation economics.\\n      Identifies under-verification as systematic failure mode. Supports B-IAVR's framing\\n      that verification decisions should reflect marginal cost-benefit analysis.\\n\\n  - id: argos2025\\n    title: \\\"Argos: Multimodal RL with Adaptive Verifier for AI Agents\\\"\\n    authors: \\\"Tan et al.\\\"\\n    venue: \\\"arXiv (revised April 2026)\\\"\\n    year: 2025\\n    arxiv_id: \\\"2512.03438\\\"\\n    category: background\\n    role: background\\n    relevance_note: >\\n      Agentic verifier that adaptively selects scoring functions for multimodal RL training.\\n      Different domain (multimodal/robotics). The adaptive verifier selection concept is\\n      complementary: Argos adapts how to verify; B-IAVR adapts when to verify.\\n\\n  # ============================================================\\n  # Direction 4: ALFWorld / Interactive Environment Benchmarks\\n  # ============================================================\\n\\n  - id: kim2025reflact\\n    title: \\\"ReflAct: World-Grounded Decision Making in LLM Agents via Goal-State Reflection\\\"\\n    authors: \\\"Kim et al.\\\"\\n    venue: \\\"EMNLP 2025\\\"\\n    year: 2025\\n    arxiv_id: \\\"2505.15182\\\"\\n    category: evaluation\\n    role: baseline\\n    relevance_note: >\\n      Prompting SOTA on ALFWorld at 93.3%. Replaces ReAct's next-action thinking with state-goal reflection.\\n      B-IAVR addresses different axis (cost-efficiency) since ALFWorld accuracy is near saturation.\\n\\n  - id: choudhury2025agentprm\\n    title: \\\"Process Reward Models for LLM Agents: Practical Framework and Directions\\\"\\n    authors: \\\"Choudhury\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2025\\n    arxiv_id: \\\"2502.10325\\\"\\n    category: evaluation\\n    role: baseline\\n    relevance_note: >\\n      Monte Carlo rollout-based process reward for agent training. 3B models achieve 91% on ALFWorld.\\n      Validates RL training approach; AgentPRM could serve as reward model for B-IAVR.\\n\\n  - id: xi2025agentprm\\n    title: \\\"AgentPRM: Process Reward Models for LLM Agents via Step-Wise Promise and Progress\\\"\\n    authors: \\\"Xi et al.\\\"\\n    venue: \\\"ACM Web Conference 2026\\\"\\n    year: 2025\\n    arxiv_id: \\\"2511.08325\\\"\\n    category: evaluation\\n    role: baseline\\n    relevance_note: >\\n      Independent work from Choudhury et al., using TD-based estimation with GAE for scalable\\n      PRM data labeling. 8x more compute-efficient than baselines with robust test-time scaling.\\n      Different approach: Choudhury uses MC rollouts; Xi uses TD+GAE for step-wise promise and progress.\\n\\n  - id: xiang2024retrospex\\n    title: \\\"Retrospex: Language Agent Meets Offline RL Critic\\\"\\n    authors: \\\"Xiang et al.\\\"\\n    venue: \\\"EMNLP 2024\\\"\\n    year: 2024\\n    arxiv_id: \\\"2505.11807\\\"\\n    category: background\\n    role: background\\n    relevance_note: >\\n      Offline RL Critic augments LLM agent action selection via dynamic rescoring.\\n      Similar architecture could inform B-IAVR's verification value estimation.\\n\\n  - id: cfgm2025\\n    title: \\\"CFGM: Coarse-to-Fine Grounded Memory for LLM Agent Planning\\\"\\n    authors: \\\"Yang et al.\\\"\\n    venue: \\\"EMNLP 2025\\\"\\n    year: 2025\\n    arxiv_id: \\\"2508.15305\\\"\\n    category: background\\n    role: background\\n    relevance_note: >\\n      Memory-augmented agent planning with episodic grounding.\\n      ALFWorld +10.40%, WebShop +20%. Complementary to B-IAVR's verification approach.\\n\\n  - id: respact2024\\n    title: \\\"ReSpAct: Harmonizing Reasoning, Speaking, and Acting\\\"\\n    authors: \\\"Dongre et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2024\\n    arxiv_id: \\\"2411.00927\\\"\\n    category: evaluation\\n    role: baseline\\n    relevance_note: >\\n      Integrates dialogue/reasoning/acting. +6% over ReAct on ALFWorld.\\n      Reduces invalid actions from 13% to 3%; B-IAVR's verification achieves error prevention differently.\\n\\n  # ============================================================\\n  # Direction 5: Multi-Turn Credit Assignment (Direct Competitors)\\n  # ============================================================\\n\\n  - id: turn-ppo2025\\n    title: \\\"Turn-Level Policy Optimization for Multi-Turn Agent Reinforcement Learning\\\"\\n    authors: \\\"Zhou et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2025\\n    arxiv_id: \\\"2512.17008\\\"\\n    category: direct-competitor\\n    role: competitor\\n    relevance_note: >\\n      [NEW-0517] Most direct competitor. Identifies \\\"uniform advantage\\\" problem in\\n      step-independent GRPO (subset of our \\\"sign misattribution\\\"). Proposes turn-level\\n      MDP + learned value function. Our differences: (1) more precise formalization\\n      (sign misattribution + gamma decay quantification), (2) contrarian solution\\n      (episode-level coarser credit vs their finer turn-level credit).\\n\\n  - id: gagpo2026\\n    title: \\\"GAGPO: Generalized Advantage Grouped Policy Optimization\\\"\\n    authors: \\\"Zhu et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2026\\n    arxiv_id: \\\"2605.13217\\\"\\n    category: direct-competitor\\n    role: competitor\\n    relevance_note: >\\n      [NEW-0517] Critic-free step-aligned credit via non-parametric grouped value proxy +\\n      TD/GAE-style temporal advantages. ALFWorld 93.5% (1.5B), 95.6% (7B).\\n      Pursues finer-grained credit to improve performance; our work diagnoses why\\n      step-independent fails (sign misattribution) and shows coarser episode-level suffices.\\n      Different contribution axis: performance optimization vs mechanism diagnosis.\\n\\n  - id: mt-grpo2025\\n    title: \\\"Reinforcing Multi-Turn Reasoning in LLM Agents via Turn-Level Reward Design\\\"\\n    authors: \\\"Wei et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2025\\n    arxiv_id: \\\"2505.11821\\\"\\n    category: direct-competitor\\n    role: competitor\\n    relevance_note: >\\n      [NEW-0517] Proposes MT-GRPO with turn-level reward design for multi-turn RL.\\n      Evaluated on QA search tasks (NQ, TriviaQA, HotpotQA), not ALFWorld.\\n      Qwen2.5-7B. Same direction as Turn-PPO (finer turn-level credit);\\n      our contrarian shows coarser episode-level eliminates sign misattribution.\\n\\n  - id: istar2025\\n    title: \\\"Agentic Reinforcement Learning with Implicit Step Rewards\\\"\\n    authors: \\\"Liu et al.\\\"\\n    venue: \\\"ICLR 2026\\\"\\n    year: 2025\\n    arxiv_id: \\\"2509.19199\\\"\\n    category: direct-competitor\\n    role: competitor\\n    relevance_note: >\\n      [NEW-0517] Implicit PRM + dual advantage (step + episode level) for agentic RL.\\n      WebShop 86.5%, VisualSokoban 91.7%. ICLR 2026 published.\\n      Learns step-level credit via implicit rewards without explicit labels;\\n      our work shows episode-level alone suffices when sign misattribution is the bottleneck.\\n      Validates that step-level credit helps, but doesn't diagnose when it hurts.\\n\\n  - id: archer2024\\n    title: \\\"ArCHer: Training Language Model Agents via Hierarchical Multi-Turn RL\\\"\\n    authors: \\\"Zhou, Zanette, Pan, Levine, Kumar\\\"\\n    venue: \\\"ICML 2024\\\"\\n    year: 2024\\n    arxiv_id: \\\"2402.19446\\\"\\n    category: method-component\\n    role: predecessor\\n    relevance_note: >\\n      [NEW-0517] Foundational hierarchical multi-turn RL framework (ICML 2024).\\n      High-level off-policy value RL (utterance-level) + low-level token policy.\\n      ~100x sample efficiency. Establishes that multi-turn RL needs hierarchical structure;\\n      our work specifically diagnoses why flat step-independent approaches fail.\\n\\n  - id: ca-survey2026\\n    title: \\\"From Reasoning to Agentic: Credit Assignment in Reinforcement Learning for Large Language Models\\\"\\n    authors: \\\"Zhang\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2026\\n    arxiv_id: \\\"2604.09459\\\"\\n    category: background\\n    role: background\\n    relevance_note: >\\n      [NEW-0517] Comprehensive survey of 47 CA methods (2024-2026). Two-dimensional\\n      taxonomy: granularity (token/segment/step/turn/multi-agent) x methodology\\n      (MC/TD/model-based/game-theoretic/information-theoretic). Contextualizes our\\n      sign misattribution diagnosis within the broader CA landscape.\\n\\n  - id: hiper2026\\n    title: \\\"HiPER: Hierarchical Reinforcement Learning with Explicit Credit Assignment for Large Language Model Agents\\\"\\n    authors: \\\"Peng et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2026\\n    arxiv_id: \\\"2602.16165\\\"\\n    category: method-component\\n    role: background\\n    relevance_note: >\\n      [NEW-0517] Hierarchical Plan-Execute RL. ALFWorld 97.4% (7B), 95.3% (1.5B).\\n      GRPO baseline: 71.1% (1.5B), 85.4% (7B). 2.8x training efficiency gain.\\n      Pursues SOTA performance via hierarchical plan-execute architecture;\\n      our work does mechanism diagnosis of why step-independent GRPO fails.\\n      Different contribution dimension: not comparable on performance axis.\\n\", \"total_chars\": 29915, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "24b94cba-878f-4f52-ba31-4ab2b9a86a4e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "7317ebb2-d910-42e9-95dc-fa8559b8ce74",
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
  "leafUuid": "c6a8ae9e-68d1-46f4-9de9-f2f90e977342",
  "sessionId": "7317ebb2-d910-42e9-95dc-fa8559b8ce74"
}
```

---

### Runtime record

_source line 17_

```json
{
  "type": "ai-title",
  "aiTitle": "Verify and correct Turn-PPO citation information",
  "sessionId": "7317ebb2-d910-42e9-95dc-fa8559b8ce74"
}
```

---

### Assistant

_source line 18 · 2026-05-17T13:46:05.814Z_

<details><summary>Logged reasoning block</summary>

```text
From the WebSearch results, the actual paper information is:

- **Title**: "Turn-PPO: Turn-Level Advantage Estimation with PPO for Improved Multi-Turn RL in Agentic LLMs"
- **Authors**: Junbo Li, Peng Zhou, Rui Meng, Meet P. Vadera, Lihong Li, and Yang Li
- **Venue**: arXiv (preprint)
- **Year**: 2025 (submitted December 2025)
- **arxiv_id**: 2512.17008

Current record in literature_map.yaml:


- **Title**: "Turn-Level Policy Optimization for Multi-Turn Agent Reinforcement Learning"
- **Authors**: "Zhou et al."
- **Venue**: "arXiv"
- **Year**: 2025

I'm noticing several discrepancies between what's recorded and what the search found. The title is significantly different—the actual paper is "Turn-PPO" with a focus on advantage estimation, not just policy optimization. The authors are also wrong; it should be Li et al. with Junbo Li as the first author, not Zhou et al. The venue and year match correctly, but I need to update the record with the complete author list and the correct arxiv ID.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c6a8ae9e-68d1-46f4-9de9-f2f90e977342",
  "isSidechain": false,
  "requestId": "req_011Cb8F3euzcYiR9QPuwrkyV",
  "type": "assistant",
  "uuid": "378eb321-3ca1-4ba0-8478-c25ba7479bf2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "7317ebb2-d910-42e9-95dc-fa8559b8ce74",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HYFsHRqSwQQuQYnzZuTj9d",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11944,
      "cache_read_input_tokens": 26139,
      "output_tokens": 626,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11944,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 626,
          "cache_read_input_tokens": 26139,
          "cache_creation_input_tokens": 11944,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11944
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

_source line 19 · 2026-05-17T13:46:07.204Z_

WebSearch 结果确认了差异。现在修正 turn-ppo2025 条目。

差异：
| 字段 | 旧值 | 新值 |
|------|------|------|
| title | "Turn-Level Policy Optimization for Multi-Turn Agent Reinforcement Learning" | "Turn-PPO: Turn-Level Advantage Estimation with PPO for Improved Multi-Turn RL in Agentic LLMs" |
| authors | "Zhou et al." | "Li et al." |
| venue | 不变 (arXiv) | 不变 |
| year | 不变 (2025) | 不变 |

现在读取完整文件并替换条目。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "378eb321-3ca1-4ba0-8478-c25ba7479bf2",
  "isSidechain": false,
  "requestId": "req_011Cb8F3euzcYiR9QPuwrkyV",
  "type": "assistant",
  "uuid": "e24be16a-b51a-4e15-9d68-cd71eeac40c3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "7317ebb2-d910-42e9-95dc-fa8559b8ce74",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HYFsHRqSwQQuQYnzZuTj9d",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11944,
      "cache_read_input_tokens": 26139,
      "output_tokens": 626,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11944,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 626,
          "cache_read_input_tokens": 26139,
          "cache_creation_input_tokens": 11944,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11944
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

_source line 20 · 2026-05-17T13:46:08.263Z_

<details open><summary>🔧 Tool call — Read · `toolu_013ck7XkxGt7aVXtZakKsKQ3`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/literature_map.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e24be16a-b51a-4e15-9d68-cd71eeac40c3",
  "isSidechain": false,
  "requestId": "req_011Cb8F3euzcYiR9QPuwrkyV",
  "type": "assistant",
  "uuid": "477600c2-f803-4782-9c16-2d55175e0e2e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "7317ebb2-d910-42e9-95dc-fa8559b8ce74",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HYFsHRqSwQQuQYnzZuTj9d",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11944,
      "cache_read_input_tokens": 26139,
      "output_tokens": 626,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11944,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 626,
          "cache_read_input_tokens": 26139,
          "cache_creation_input_tokens": 11944,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11944
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

_source line 21 · 2026-05-17T13:46:08.539Z_

<details><summary>↩ Tool result · `toolu_013ck7XkxGt7aVXtZakKsKQ3`</summary>

```text
1	# B-IAVR Literature Map
2	# Updated: 2026-05-17
3	# Categories: direct-competitor, method-component, background, evaluation
4	# Roles: predecessor, competitor, baseline, evaluation, background
5	
6	papers:
7	
8	  # ============================================================
9	  # Direction 1: Self-Verification / Self-Correction in LLM Agents
10	  # ============================================================
11	
12	  - id: kamoi2024self-correction-survey
13	    title: "When Can LLMs Actually Correct Their Own Mistakes? A Critical Survey of Self-Correction of LLMs"
14	    authors: "Kamoi et al."
15	    venue: "arXiv"
16	    year: 2024
17	    arxiv_id: "2406.01297"
18	    category: background
19	    role: background
20	    relevance_note: >
21	      Foundational survey establishing that pure intrinsic self-correction is unreliable.
22	      Validates B-IAVR's use of grounded verification (environment re-observation) over prompted self-feedback.
23	
24	  - id: tie2025correctbench
25	    title: "Can LLMs Correct Themselves? A Benchmark of Self-Correction in LLMs"
26	    authors: "Tie et al."
27	    venue: "NeurIPS 2025 Datasets & Benchmarks"
28	    year: 2025
29	    arxiv_id: "2510.16062"
30	    category: background
31	    role: background
32	    relevance_note: >
33	      Benchmark showing self-correction has diminishing returns when applied uniformly.
34	      Supports B-IAVR's selective verification design over blanket correction.
35	
36	  - id: self-verification-dilemma-2026
37	    title: "Self-Verification Dilemma: Experience-Driven Suppression of Overused Checking in LLM Reasoning"
38	    authors: "Long et al."
39	    venue: "arXiv"
40	    year: 2026
41	    arxiv_id: "2602.03485"
42	    category: background
43	    role: background
44	    relevance_note: >
45	      Empirically validates that >90% of self-verification is confirmatory, ~2% corrective.
46	      Directly supports B-IAVR's core thesis that verification should be selective.
47	      Their experience-pool approach is complementary to B-IAVR's action-change signal.
48	
49	  - id: zhang2025incentivize-self-verify
50	    title: "Incentivizing LLMs to Self-Verify Their Answers"
51	    authors: "Zhang et al."
52	    venue: "arXiv"
53	    year: 2025
54	    arxiv_id: "2506.01369"
55	    category: background
56	    role: background
57	    relevance_note: >
58	      Unifies answer generation and verification via single RL training process.
59	      Parallel to B-IAVR: they train verification into generation; B-IAVR trains when to trigger separate verification.
60	
61	  - id: mar2025
62	    title: "MAR: Multi-Agent Reflexion Improves Reasoning Abilities in LLMs"
63	    authors: "Ozer et al."
64	    venue: "arXiv"
65	    year: 2025
66	    arxiv_id: "2512.20845"
67	    category: background
68	    role: background
69	    relevance_note: >
70	      Multi-agent self-correction with diverse critic personas.
71	      Complementary: MAR improves correction quality; B-IAVR decides when to trigger correction.
72	
73	  - id: ssr2025
74	    title: "SSR: Socratic Self-Refine for Large Language Model Reasoning"
75	    authors: "Shi et al."
76	    venue: "arXiv"
77	    year: 2025
78	    arxiv_id: "2511.10621"
79	    category: background
80	    role: background
81	    relevance_note: >
82	      Structured Socratic questioning for self-refinement.
83	      Complementary: improves correction step quality; B-IAVR focuses on when to invoke correction.
84	
85	  - id: verifiagent2025
86	    title: "VerifiAgent: a Unified Verification Agent in Language Model Reasoning"
87	    authors: "Han et al."
88	    venue: "EMNLP 2025 Findings"
89	    year: 2025
90	    arxiv_id: "2504.00406"
91	    category: background
92	    role: background
93	    relevance_note: >
94	      Unified verification agent with meta-verification + tool-based adaptive verification.
95	      Focuses on how to verify (tool selection); B-IAVR focuses on when to verify (policy learning).
96	      Complementary: VerifiAgent's verification quality could enhance B-IAVR's verification step.
97	
98	  # ============================================================
99	  # Direction 2: Agent RL Training
100	  # ============================================================
101	
102	  - id: feng2025gigpo
103	    title: "GiGPO: Group-in-Group Policy Optimization for LLM Agent Training"
104	    authors: "Feng et al."
105	    venue: "NeurIPS 2025"
106	    year: 2025
107	    arxiv_id: "2505.10978"
108	    category: method-component
109	    role: predecessor
110	    relevance_note: >
111	      Core training algorithm for B-IAVR. Nested group structure provides step-level credit
112	      assignment without learned critic. >12% over GRPO on ALFWorld, >9% on WebShop.
113	
114	  - id: selfguide2026
115	    title: "Co-Evolution of Policy and Internal Reward for Language Agents (Self-Guide)"
116	    authors: "Wang et al."
117	    venue: "arXiv"
118	    year: 2026
119	    arxiv_id: "2604.03098"
120	    category: method-component
121	    role: predecessor
122	    relevance_note: >
123	      Direct predecessor. B-IAVR extends Self-Guide's co-evolving internal reward.
124	      The self-guidance signal is the foundation for action-change detection triggering verification.
125	      8% improvement over env-reward-only on ALFWorld with Qwen3-1.7B/4B.
126	
127	  - id: spear2025
128	    title: "Learn the Ropes, Then Trust the Wins: Self-imitation with Progressive Exploration for Agentic Reinforcement Learning"
129	    authors: "Qin et al."
130	    venue: "ICLR 2026"
131	    year: 2025
132	    arxiv_id: "2509.22601"
133	    category: method-component
134	    role: background
135	    relevance_note: >
136	      Curriculum-based self-imitation for sparse-reward agent tasks.
137	      Up to +16.1% on ALFWorld over GRPO. Self-imitation curriculum could augment B-IAVR training.
138	
139	  - id: wei2025webagent-r1
140	    title: "WebAgent-R1: Training Web Agents via End-to-End Multi-Turn RL"
141	    authors: "Wei et al."
142	    venue: "EMNLP 2025"
143	    year: 2025
144	    arxiv_id: "2505.16421"
145	    category: background
146	    role: background
147	    relevance_note: >
148	      Extends GRPO to multi-turn (M-GRPO) with dynamic context compression.
149	      Qwen-2.5-3B: 6.1% to 33.9% on WebArena-Lite. M-GRPO multi-turn extension relevant to B-IAVR.
150	
151	  - id: dapo2025
152	    title: "DAPO: An Open-Source LLM Reinforcement Learning System at Scale"
153	    authors: "Yu et al."
154	    venue: "arXiv"
155	    year: 2025
156	    arxiv_id: "2503.14476"
157	    category: method-component
158	    role: background
159	    relevance_note: >
160	      RL training stabilization techniques (Clip-Higher, Dynamic Sampling).
161	      Applicable to B-IAVR's RL training to prevent entropy collapse.
162	
163	  - id: digiRL2024
164	    title: "DigiRL: Training In-The-Wild Device-Control Agents with Autonomous RL"
165	    authors: "Bai et al."
166	    venue: "NeurIPS 2024"
167	    year: 2024
168	    arxiv_id: "2406.11896"
169	    category: background
170	    role: background
171	    relevance_note: >
172	      Online RL for device control agents. Demonstrates online RL viability for interactive agents.
173	      49.5% absolute improvement over SFT. Parallel approach to B-IAVR in text-based setting.
174	
175	  - id: li2025sorl
176	    title: "SORL: Stabilizing Off-Policy RL for Long-Horizon Agent Training"
177	    authors: "Li et al."
178	    venue: "arXiv"
179	    year: 2025
180	    arxiv_id: "2511.20718"
181	    category: method-component
182	    role: background
183	    relevance_note: >
184	      Turn-level importance sampling + clipping-triggered normalization for stable multi-turn agent RL.
185	      Directly applicable to B-IAVR's multi-turn ALFWorld training stability.
186	
187	  - id: agentic-rl-survey-2025
188	    title: "The Landscape of Agentic Reinforcement Learning for LLMs: A Survey"
189	    authors: "Zhang et al."
190	    venue: "TMLR 2026"
191	    year: 2025
192	    arxiv_id: "2509.02547"
193	    category: background
194	    role: background
195	    relevance_note: >
196	      Comprehensive survey formalizing agentic RL. Contextualizes B-IAVR as training agents
197	      to make meta-decisions (when to verify) via RL within the POMDP framework.
198	
199	  - id: skillmaster2026
200	    title: "SkillMaster: Toward Autonomous Skill Mastery in LLM Agents"
201	    authors: "Yang et al."
202	    venue: "arXiv"
203	    year: 2026
204	    arxiv_id: "2605.08693"
205	    category: method-component
206	    role: background
207	    relevance_note: >
208	      DualAdv-GRPO: separately estimates advantages for task-solving and skill-editing decisions.
209	      +8.8% on ALFWorld, +9.3% on WebShop. DualAdv structure could inform B-IAVR's
210	      separation of action and verification advantages.
211	
212	  - id: t2po2026
213	    title: "T2PO: Uncertainty-Guided Exploration Control for Stable Multi-Turn Agentic RL"
214	    authors: "Wang et al."
215	    venue: "ICML 2026 Spotlight"
216	    year: 2026
217	    arxiv_id: "2605.02178"
218	    category: method-component
219	    role: background
220	    relevance_note: >
221	      Token- and turn-level uncertainty monitoring for stable multi-turn agent RL.
222	      Triggers thinking intervention when marginal uncertainty change drops below threshold.
223	      Evaluated on ALFWorld and WebShop. Conceptually related: uncertainty-based trigger vs
224	      B-IAVR's action-change trigger, but T2PO targets training stability, not deployment verification.
225	
226	  - id: gvpo2026
227	    title: "GVPO: Group Verification-based Policy Optimization for Interactive Coding Agents"
228	    authors: "Dai et al."
229	    venue: "ICLR 2026"
230	    year: 2026
231	    arxiv_id: null  # no arXiv preprint; OpenReview ID: RY47Tq0VsV
232	    category: method-component
233	    role: background
234	    relevance_note: >
235	      Advantage shaping with outcome-verifiable + process-verifiable signals.
236	      +12.7% over o1 on AppWorld. Integrates intermediate execution feedback as step-level
237	      verification signals. Different focus: uses verification for credit assignment during
238	      training; B-IAVR learns when to invoke verification at deployment.
239	
240	  - id: agentv-rl2026
241	    title: "AgentV-RL: Scaling Reward Modeling with Agentic Verifier"
242	    authors: "Zhang et al."
243	    venue: "arXiv"
244	    year: 2026
245	    arxiv_id: "2604.16004"
246	    category: method-component
247	    role: background
248	    relevance_note: >
249	      Bidirectional forward/backward agentic verifier for reward modeling in RL.
250	      4B model surpasses SOTA ORMs by 25.2%. Addresses verification quality in reward modeling;
251	      B-IAVR addresses verification timing in agent deployment. Complementary.
252	
253	  - id: pa-moe2026
254	    title: "PA-MoE: Phase-Aware Mixture of Experts for Agentic Reinforcement Learning"
255	    authors: "Li et al."
256	    venue: "arXiv"
257	    year: 2026
258	    arxiv_id: "2602.17038"
259	    category: evaluation
260	    role: baseline
261	    relevance_note: >
262	      [NEW-0516] Lightweight phase router learns latent phase boundaries from RL objective.
263	      PA-MoE+GiGPO with Qwen2.5-1.5B achieves 93.8% on ALFWorld (+7.7 over GiGPO 86.1%).
264	      1.5B outperforms vanilla 7B GiGPO (90.2%). New small-model SOTA on ALFWorld.
265	      Orthogonal architecture innovation; important baseline to cite.
266	
267	  - id: sdar2026
268	    title: "SDAR: Self-Distilled Agentic Reinforcement Learning"
269	    authors: "Lu et al."
270	    venue: "arXiv"
271	    year: 2026
272	    arxiv_id: "2605.15155"
273	    category: method-component
274	    role: background
275	    relevance_note: >
276	      [NEW-0516] On-policy self-distillation as gated auxiliary objective during RL training.
277	      Token-level gate decides supervision intensity. +9.4% over GRPO on ALFWorld.
278	      Complementary: SDAR improves RL training; B-IAVR learns verification policy.
279	
280	  - id: hcapo2026
281	    title: "HCAPO: Hindsight Credit Assignment for Long-Horizon LLM Agents"
282	    authors: "Tan et al."
283	    venue: "arXiv"
284	    year: 2026
285	    arxiv_id: "2603.08754"
286	    category: method-component
287	    role: background
288	    relevance_note: >
289	      [NEW-0516] LLM-as-critic refines step-level Q-values via hindsight reasoning +
290	      multi-scale advantage for critical decision states.
291	      +13.8% on ALFWorld, +7.7% on WebShop over GRPO (Qwen2.5-7B).
292	      Could improve B-IAVR's reward signal for verification decision steps.
293	
294	  - id: act2026
295	    title: "ACT: Agentic Critical Training"
296	    authors: "Liu et al."
297	    venue: "arXiv"
298	    year: 2026
299	    arxiv_id: "2603.08706"
300	    category: method-component
301	    role: background
302	    relevance_note: >
303	      [NEW-0516] Trains agents to judge action quality via critical comparison reward.
304	      +5.07 over IL, +4.62 over RL. Different axis: ACT improves reflection quality;
305	      B-IAVR decides when to reflect.
306	
307	  - id: rwml2026
308	    title: "RWML: Reinforcement World Model Learning for LLM-based Agents"
309	    authors: "Yu et al."
310	    venue: "arXiv"
311	    year: 2026
312	    arxiv_id: "2602.05842"
313	    category: method-component
314	    role: background
315	    relevance_note: >
316	      [NEW-0516] Self-supervised world model via sim-to-real gap rewards in embedding space.
317	      +6.9 on ALFWorld over task-success-only RL. Matches expert-data training.
318	      Orthogonal: improves internal world model; B-IAVR adds selective verification.
319	
320	  - id: skill0-2026
321	    title: "SKILL0: In-Context Agentic Reinforcement Learning for Skill Internalization"
322	    authors: "Lu et al."
323	    venue: "arXiv"
324	    year: 2026
325	    arxiv_id: "2604.02268"
326	    category: method-component
327	    role: background
328	    relevance_note: >
329	      [NEW-0516] Training-time curriculum progressively withdraws skill context until zero-shot.
330	      +9.7% on ALFWorld over GRPO, <0.5k tokens per step.
331	      Complementary: SKILL0 internalizes skills; B-IAVR adds selective verification.
332	
333	  - id: fission-grpo2026
334	    title: "Fission-GRPO: Robust Tool Use via Learning to Recover from Execution Errors"
335	    authors: "Zhang et al."
336	    venue: "arXiv"
337	    year: 2026
338	    arxiv_id: "2601.15625"
339	    category: method-component
340	    role: background
341	    relevance_note: >
342	      [NEW-0516] Fissions failed trajectories into recovery training instances.
343	      +4% overall accuracy on BFCL v4 Multi-Turn over GRPO.
344	      Related: error recovery after failure vs B-IAVR's proactive verification.
345	
346	  - id: selfbudgeter2026
347	    title: "SelfBudgeter: Adaptive Token Allocation for Efficient LLM Reasoning"
348	    authors: "Li et al."
349	    venue: "ICLR 2026 (under review)"
350	    year: 2025
351	    arxiv_id: "2505.11274"
352	    category: background
353	    role: background
354	    relevance_note: >
355	      [NEW-0516] Self-estimated token budgets + budget-guided GRPO. 61% token reduction.
356	      Parallel concept: SelfBudgeter allocates computation budget;
357	      B-IAVR makes binary verify/not-verify decision. Both use RL for adaptive compute.
358	
359	  - id: cove2026
360	    title: "CoVe: Training Interactive Tool-Use Agents via Constraint-Guided Verification"
361	    authors: "Chen et al."
362	    venue: "arXiv"
363	    year: 2026
364	    arxiv_id: "2603.01940"
365	    category: background
366	    role: background
367	    relevance_note: >
368	      [NEW-0516] Task constraints guide trajectory generation and serve as deterministic verifiers.
369	      Different: CoVe uses verification for data synthesis; B-IAVR learns when to verify at inference.
370	
371	  # ============================================================
372	  # Direction 3: Selective Verification / Adaptive Computation
373	  # ============================================================
374	
375	  - id: wan2025derailer-rerailer
376	    title: "Derailer-Rerailer: Adaptive Verification for Efficient and Reliable LM Reasoning"
377	    authors: "Wan et al."
378	    venue: "ACL 2025 Findings"
379	    year: 2025
380	    arxiv_id: "2408.13940"
381	    category: direct-competitor
382	    role: competitor
383	    relevance_note: >
384	      Most directly related competitor. Both do selective verification with binary trigger.
385	      Key difference: operates on reasoning chains (single-turn); B-IAVR on agent trajectories (multi-turn).
386	      Uses heuristic instability signal; B-IAVR uses RL-trained action-change signal.
387	      8-11% accuracy gain, 2-3x efficiency over uniform verification.
388	
389	  - id: sherlock2025
390	    title: "Sherlock: Reliable and Efficient Agentic Workflow Execution"
391	    authors: "Microsoft"
392	    venue: "arXiv"
393	    year: 2025
394	    arxiv_id: "2511.00330"
395	    category: direct-competitor
396	    role: competitor
397	    relevance_note: >
398	      Selective verification for agentic workflows via offline counterfactual analysis + speculative execution.
399	      Different scope: workflow DAG level (offline); B-IAVR is step-level (online RL).
400	      18.3% accuracy gain, 26% cost reduction, 48.7% latency reduction.
401	
402	  - id: singhi2025when-to-verify
403	    title: "When To Solve, When To Verify: Compute-Optimal Verification for LLM Reasoning"
404	    authors: "Singhi et al."
405	    venue: "arXiv"
406	    year: 2025
407	    arxiv_id: "2504.01005"
408	    category: background
409	    role: background
410	    relevance_note: >
411	      Derives inference scaling laws for solve-vs-verify tradeoff.
412	      Finding that over-verification is suboptimal directly supports B-IAVR's selective approach.
413	      B-IAVR learns this allocation via RL rather than analytically.
414	
415	  - id: yang2026ares
416	    title: "ARES: Adaptive Reasoning Effort Selection for Efficient LLM Agents"
417	    authors: "Yang et al."
418	    venue: "arXiv"
419	    year: 2026
420	    arxiv_id: "2603.07915"
421	    category: direct-competitor
422	    role: competitor
423	    relevance_note: >
424	      Closest competitor in agent domain. Both train learned per-step compute allocation.
425	      ARES uses SFT-initialized router further refined via GRPO with outcome + token efficiency reward;
426	      B-IAVR trains binary verify/not-verify via RL with action-change signal.
427	      Key differences: (1) reward signal — ARES optimizes token efficiency, B-IAVR uses action-change
428	      as verification trigger; (2) data requirement — ARES needs difficulty-annotated training data
429	      to bootstrap the router, B-IAVR learns from environment interaction alone.
430	      Reduces reasoning tokens by up to 52.7%.
431	
432	  - id: tu2025autothink
433	    title: "Learning When to Think: Shaping Adaptive Reasoning in R1-Style Models via Multi-Stage RL"
434	    authors: "Tu et al."
435	    venue: "NeurIPS 2025"
436	    year: 2025
437	    arxiv_id: "2505.10832"
438	    category: direct-competitor
439	    role: competitor
440	    relevance_note: >
441	      Analogous idea in reasoning domain: RL-trained adaptive computation trigger.
442	      Operates on single-turn reasoning; B-IAVR on multi-turn agent trajectories.
443	      +6.4% accuracy, -52% tokens on DeepSeek-R1-Distill-Qwen-1.5B.
444	
445	  - id: du2025thinkless
446	    title: "Thinkless: LLM Learns When to Think"
447	    authors: "Fang et al."
448	    venue: "NeurIPS 2025"
449	    year: 2025
450	    arxiv_id: "2505.13379"
451	    category: direct-competitor
452	    role: competitor
453	    relevance_note: >
454	      RL-trained control token to decide when to invoke extended thinking.
455	      Methodologically closest to B-IAVR in reasoning domain; B-IAVR applies to interactive agent trajectories.
456	
457	  - id: wang2025efficient-agents
458	    title: "Efficient Agents: Building Effective Agents While Reducing Cost"
459	    authors: "Wang et al."
460	    venue: "arXiv"
461	    year: 2025
462	    arxiv_id: "2508.02694"
463	    category: background
464	    role: background
465	    relevance_note: >
466	      First systematic study of agent efficiency-effectiveness tradeoff.
467	      Framework-level cost reduction; B-IAVR addresses cost at verification-policy level.
468	      Retains 96.7% performance with 28.4% cost-of-pass improvement.
469	
470	  - id: venktesh2025trust-but-verify
471	    title: "Trust but Verify! A Survey on Verification Design for Test-time Scaling"
472	    authors: "Venktesh et al."
473	    venue: "arXiv"
474	    year: 2025
475	    arxiv_id: "2508.16665"
476	    category: background
477	    role: background
478	    relevance_note: >
479	      Survey of verification approaches for test-time compute scaling.
480	      Identifies verification timing as key open problem. B-IAVR provides concrete solution for agent setting.
481	
482	  - id: agent-omit2026
483	    title: "Agent-Omit: Training Efficient LLM Agents for Adaptive Thought and Observation Omission via Agentic RL"
484	    authors: "Ning et al."
485	    venue: "ICML 2026"
486	    year: 2026
487	    arxiv_id: "2602.04284"
488	    category: direct-competitor
489	    role: competitor
490	    relevance_note: >
491	      RL-trained policy for adaptive omission of redundant thoughts and observations.
492	      Agent-Omit-8B matches frontier agents with best efficiency tradeoff on 5 benchmarks.
493	      Both use RL to learn cost-efficient agent behavior. Key difference: Agent-Omit subtracts
494	      (omits unnecessary context); B-IAVR selectively adds (verification steps).
495	      Opposite but complementary approaches to cost-efficiency. Potentially combinable.
496	
497	  - id: ava2026
498	    title: "Anytime Verified Agents: Adaptive Compute Allocation for Reliable LLM Reasoning under Budget Constraints"
499	    authors: "Patel"
500	    venue: "TMLR 2026"
501	    year: 2026
502	    arxiv_id: null  # no arXiv preprint; OpenReview ID: JMDCMf7mlF
503	    category: direct-competitor
504	    role: competitor
505	    relevance_note: >
506	      Dynamic compute allocation across search, sampling, and verification under budget.
507	      Uses calibrated uncertainty + value-of-information for selective verification cascades.
508	      Evaluated on GSM8K/MATH/HotpotQA/HumanEval (reasoning), not interactive agents.
509	      Key difference: analytical/heuristic allocation vs B-IAVR's RL-learned policy;
510	      single-turn reasoning vs multi-turn agent trajectories.
511	
512	  - id: cast2026
513	    title: "CAST: Case-Based Calibration of Adaptive Reasoning and Execution for LLM Tool Use"
514	    authors: "Pang et al."
515	    venue: "arXiv"
516	    year: 2026
517	    arxiv_id: "2605.15041"
518	    category: background
519	    role: background
520	    relevance_note: >
521	      Historical execution cases calibrate reasoning depth for tool use.
522	      Reduces reasoning length 26% with +5.85% accuracy on BFCLv2/ToolBench.
523	      Related: adaptive reasoning depth; different: case-based calibration vs RL-learned policy.
524	
525	  - id: marginal-token-allocators2026
526	    title: "Agentic AI Systems Should Be Designed as Marginal Token Allocators"
527	    authors: "Zhu"
528	    venue: "arXiv"
529	    year: 2026
530	    arxiv_id: "2605.01214"
531	    category: background
532	    role: background
533	    relevance_note: >
534	      Position paper framing agent cost-efficiency as marginal token allocation economics.
535	      Identifies under-verification as systematic failure mode. Supports B-IAVR's framing
536	      that verification decisions should reflect marginal cost-benefit analysis.
537	
538	  - id: argos2025
539	    title: "Argos: Multimodal RL with Adaptive Verifier for AI Agents"
540	    authors: "Tan et al."
541	    venue: "arXiv (revised April 2026)"
542	    year: 2025
543	    arxiv_id: "2512.03438"
544	    category: background
545	    role: background
546	    relevance_note: >
547	      Agentic verifier that adaptively selects scoring functions for multimodal RL training.
548	      Different domain (multimodal/robotics). The adaptive verifier selection concept is
549	      complementary: Argos adapts how to verify; B-IAVR adapts when to verify.
550	
551	  # ============================================================
552	  # Direction 4: ALFWorld / Interactive Environment Benchmarks
553	  # ============================================================
554	
555	  - id: kim2025reflact
556	    title: "ReflAct: World-Grounded Decision Making in LLM Agents via Goal-State Reflection"
557	    authors: "Kim et al."
558	    venue: "EMNLP 2025"
559	    year: 2025
560	    arxiv_id: "2505.15182"
561	    category: evaluation
562	    role: baseline
563	    relevance_note: >
564	      Prompting SOTA on ALFWorld at 93.3%. Replaces ReAct's next-action thinking with state-goal reflection.
565	      B-IAVR addresses different axis (cost-efficiency) since ALFWorld accuracy is near saturation.
566	
567	  - id: choudhury2025agentprm
568	    title: "Process Reward Models for LLM Agents: Practical Framework and Directions"
569	    authors: "Choudhury"
570	    venue: "arXiv"
571	    year: 2025
572	    arxiv_id: "2502.10325"
573	    category: evaluation
574	    role: baseline
575	    relevance_note: >
576	      Monte Carlo rollout-based process reward for agent training. 3B models achieve 91% on ALFWorld.
577	      Validates RL training approach; AgentPRM could serve as reward model for B-IAVR.
578	
579	  - id: xi2025agentprm
580	    title: "AgentPRM: Process Reward Models for LLM Agents via Step-Wise Promise and Progress"
581	    authors: "Xi et al."
582	    venue: "ACM Web Conference 2026"
583	    year: 2025
584	    arxiv_id: "2511.08325"
585	    category: evaluation
586	    role: baseline
587	    relevance_note: >
588	      Independent work from Choudhury et al., using TD-based estimation with GAE for scalable
589	      PRM data labeling. 8x more compute-efficient than baselines with robust test-time scaling.
590	      Different approach: Choudhury uses MC rollouts; Xi uses TD+GAE for step-wise promise and progress.
591	
592	  - id: xiang2024retrospex
593	    title: "Retrospex: Language Agent Meets Offline RL Critic"
594	    authors: "Xiang et al."
595	    venue: "EMNLP 2024"
596	    year: 2024
597	    arxiv_id: "2505.11807"
598	    category: background
599	    role: background
600	    relevance_note: >
601	      Offline RL Critic augments LLM agent action selection via dynamic rescoring.
602	      Similar architecture could inform B-IAVR's verification value estimation.
603	
604	  - id: cfgm2025
605	    title: "CFGM: Coarse-to-Fine Grounded Memory for LLM Agent Planning"
606	    authors: "Yang et al."
607	    venue: "EMNLP 2025"
608	    year: 2025
609	    arxiv_id: "2508.15305"
610	    category: background
611	    role: background
612	    relevance_note: >
613	      Memory-augmented agent planning with episodic grounding.
614	      ALFWorld +10.40%, WebShop +20%. Complementary to B-IAVR's verification approach.
615	
616	  - id: respact2024
617	    title: "ReSpAct: Harmonizing Reasoning, Speaking, and Acting"
618	    authors: "Dongre et al."
619	    venue: "arXiv"
620	    year: 2024
621	    arxiv_id: "2411.00927"
622	    category: evaluation
623	    role: baseline
624	    relevance_note: >
625	      Integrates dialogue/reasoning/acting. +6% over ReAct on ALFWorld.
626	      Reduces invalid actions from 13% to 3%; B-IAVR's verification achieves error prevention differently.
627	
628	  # ============================================================
629	  # Direction 5: Multi-Turn Credit Assignment (Direct Competitors)
630	  # ============================================================
631	
632	  - id: turn-ppo2025
633	    title: "Turn-Level Policy Optimization for Multi-Turn Agent Reinforcement Learning"
634	    authors: "Zhou et al."
635	    venue: "arXiv"
636	    year: 2025
637	    arxiv_id: "2512.17008"
638	    category: direct-competitor
639	    role: competitor
640	    relevance_note: >
641	      [NEW-0517] Most direct competitor. Identifies "uniform advantage" problem in
642	      step-independent GRPO (subset of our "sign misattribution"). Proposes turn-level
643	      MDP + learned value function. Our differences: (1) more precise formalization
644	      (sign misattribution + gamma decay quantification), (2) contrarian solution
645	      (episode-level coarser credit vs their finer turn-level credit).
646	
647	  - id: gagpo2026
648	    title: "GAGPO: Generalized Advantage Grouped Policy Optimization"
649	    authors: "Zhu et al."
650	    venue: "arXiv"
651	    year: 2026
652	    arxiv_id: "2605.13217"
653	    category: direct-competitor
654	    role: competitor
655	    relevance_note: >
656	      [NEW-0517] Critic-free step-aligned credit via non-parametric grouped value proxy +
657	      TD/GAE-style temporal advantages. ALFWorld 93.5% (1.5B), 95.6% (7B).
658	      Pursues finer-grained credit to improve performance; our work diagnoses why
659	      step-independent fails (sign misattribution) and shows coarser episode-level suffices.
660	      Different contribution axis: performance optimization vs mechanism diagnosis.
661	
662	  - id: mt-grpo2025
663	    title: "Reinforcing Multi-Turn Reasoning in LLM Agents via Turn-Level Reward Design"
664	    authors: "Wei et al."
665	    venue: "arXiv"
666	    year: 2025
667	    arxiv_id: "2505.11821"
668	    category: direct-competitor
669	    role: competitor
670	    relevance_note: >
671	      [NEW-0517] Proposes MT-GRPO with turn-level reward design for multi-turn RL.
672	      Evaluated on QA search tasks (NQ, TriviaQA, HotpotQA), not ALFWorld.
673	      Qwen2.5-7B. Same direction as Turn-PPO (finer turn-level credit);
674	      our contrarian shows coarser episode-level eliminates sign misattribution.
675	
676	  - id: istar2025
677	    title: "Agentic Reinforcement Learning with Implicit Step Rewards"
678	    authors: "Liu et al."
679	    venue: "ICLR 2026"
680	    year: 2025
681	    arxiv_id: "2509.19199"
682	    category: direct-competitor
683	    role: competitor
684	    relevance_note: >
685	      [NEW-0517] Implicit PRM + dual advantage (step + episode level) for agentic RL.
686	      WebShop 86.5%, VisualSokoban 91.7%. ICLR 2026 published.
687	      Learns step-level credit via implicit rewards without explicit labels;
688	      our work shows episode-level alone suffices when sign misattribution is the bottleneck.
689	      Validates that step-level credit helps, but doesn't diagnose when it hurts.
690	
691	  - id: archer2024
692	    title: "ArCHer: Training Language Model Agents via Hierarchical Multi-Turn RL"
693	    authors: "Zhou, Zanette, Pan, Levine, Kumar"
694	    venue: "ICML 2024"
695	    year: 2024
696	    arxiv_id: "2402.19446"
697	    category: method-component
698	    role: predecessor
699	    relevance_note: >
700	      [NEW-0517] Foundational hierarchical multi-turn RL framework (ICML 2024).
701	      High-level off-policy value RL (utterance-level) + low-level token policy.
702	      ~100x sample efficiency. Establishes that multi-turn RL needs hierarchical structure;
703	      our work specifically diagnoses why flat step-independent approaches fail.
704	
705	  - id: ca-survey2026
706	    title: "From Reasoning to Agentic: Credit Assignment in Reinforcement Learning for Large Language Models"
707	    authors: "Zhang"
708	    venue: "arXiv"
709	    year: 2026
710	    arxiv_id: "2604.09459"
711	    category: background
712	    role: background
713	    relevance_note: >
714	      [NEW-0517] Comprehensive survey of 47 CA methods (2024-2026). Two-dimensional
715	      taxonomy: granularity (token/segment/step/turn/multi-agent) x methodology
716	      (MC/TD/model-based/game-theoretic/information-theoretic). Contextualizes our
717	      sign misattribution diagnosis within the broader CA landscape.
718	
719	  - id: hiper2026
720	    title: "HiPER: Hierarchical Reinforcement Learning with Explicit Credit Assignment for Large Language Model Agents"
721	    authors: "Peng et al."
722	    venue: "arXiv"
723	    year: 2026
724	    arxiv_id: "2602.16165"
725	    category: method-component
726	    role: background
727	    relevance_note: >
728	      [NEW-0517] Hierarchical Plan-Execute RL. ALFWorld 97.4% (7B), 95.3% (1.5B).
729	      GRPO baseline: 71.1% (1.5B), 85.4% (7B). 2.8x training efficiency gain.
730	      Pursues SOTA performance via hierarchical plan-execute architecture;
731	      our work does mechanism diagnosis of why step-independent GRPO fails.
732	      Different contribution dimension: not comparable on performance axis.
733	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "477600c2-f803-4782-9c16-2d55175e0e2e",
  "isSidechain": false,
  "promptId": "71e953e0-39de-4d6a-a9b9-c8a649da7bce",
  "type": "user",
  "uuid": "5a16cba2-54e0-44c9-940d-fb2909f89be3",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/literature_map.yaml",
      "content": "# B-IAVR Literature Map\n# Updated: 2026-05-17\n# Categories: direct-competitor, method-component, background, evaluation\n# Roles: predecessor, competitor, baseline, evaluation, background\n\npapers:\n\n  # ============================================================\n  # Direction 1: Self-Verification / Self-Correction in LLM Agents\n  # ============================================================\n\n  - id: kamoi2024self-correction-survey\n    title: \"When Can LLMs Actually Correct Their Own Mistakes? A Critical Survey of Self-Correction of LLMs\"\n    authors: \"Kamoi et al.\"\n    venue: \"arXiv\"\n    year: 2024\n    arxiv_id: \"2406.01297\"\n    category: background\n    role: background\n    relevance_note: >\n      Foundational survey establishing that pure intrinsic self-correction is unreliable.\n      Validates B-IAVR's use of grounded verification (environment re-observation) over prompted self-feedback.\n\n  - id: tie2025correctbench\n    title: \"Can LLMs Correct Themselves? A Benchmark of Self-Correction in LLMs\"\n    authors: \"Tie et al.\"\n    venue: \"NeurIPS 2025 Datasets & Benchmarks\"\n    year: 2025\n    arxiv_id: \"2510.16062\"\n    category: background\n    role: background\n    relevance_note: >\n      Benchmark showing self-correction has diminishing returns when applied uniformly.\n      Supports B-IAVR's selective verification design over blanket correction.\n\n  - id: self-verification-dilemma-2026\n    title: \"Self-Verification Dilemma: Experience-Driven Suppression of Overused Checking in LLM Reasoning\"\n    authors: \"Long et al.\"\n    venue: \"arXiv\"\n    year: 2026\n    arxiv_id: \"2602.03485\"\n    category: background\n    role: background\n    relevance_note: >\n      Empirically validates that >90% of self-verification is confirmatory, ~2% corrective.\n      Directly supports B-IAVR's core thesis that verification should be selective.\n      Their experience-pool approach is complementary to B-IAVR's action-change signal.\n\n  - id: zhang2025incentivize-self-verify\n    title: \"Incentivizing LLMs to Self-Verify Their Answers\"\n    authors: \"Zhang et al.\"\n    venue: \"arXiv\"\n    year: 2025\n    arxiv_id: \"2506.01369\"\n    category: background\n    role: background\n    relevance_note: >\n      Unifies answer generation and verification via single RL training process.\n      Parallel to B-IAVR: they train verification into generation; B-IAVR trains when to trigger separate verification.\n\n  - id: mar2025\n    title: \"MAR: Multi-Agent Reflexion Improves Reasoning Abilities in LLMs\"\n    authors: \"Ozer et al.\"\n    venue: \"arXiv\"\n    year: 2025\n    arxiv_id: \"2512.20845\"\n    category: background\n    role: background\n    relevance_note: >\n      Multi-agent self-correction with diverse critic personas.\n      Complementary: MAR improves correction quality; B-IAVR decides when to trigger correction.\n\n  - id: ssr2025\n    title: \"SSR: Socratic Self-Refine for Large Language Model Reasoning\"\n    authors: \"Shi et al.\"\n    venue: \"arXiv\"\n    year: 2025\n    arxiv_id: \"2511.10621\"\n    category: background\n    role: background\n    relevance_note: >\n      Structured Socratic questioning for self-refinement.\n      Complementary: improves correction step quality; B-IAVR focuses on when to invoke correction.\n\n  - id: verifiagent2025\n    title: \"VerifiAgent: a Unified Verification Agent in Language Model Reasoning\"\n    authors: \"Han et al.\"\n    venue: \"EMNLP 2025 Findings\"\n    year: 2025\n    arxiv_id: \"2504.00406\"\n    category: background\n    role: background\n    relevance_note: >\n      Unified verification agent with meta-verification + tool-based adaptive verification.\n      Focuses on how to verify (tool selection); B-IAVR focuses on when to verify (policy learning).\n      Complementary: VerifiAgent's verification quality could enhance B-IAVR's verification step.\n\n  # ============================================================\n  # Direction 2: Agent RL Training\n  # ============================================================\n\n  - id: feng2025gigpo\n    title: \"GiGPO: Group-in-Group Policy Optimization for LLM Agent Training\"\n    authors: \"Feng et al.\"\n    venue: \"NeurIPS 2025\"\n    year: 2025\n    arxiv_id: \"2505.10978\"\n    category: method-component\n    role: predecessor\n    relevance_note: >\n      Core training algorithm for B-IAVR. Nested group structure provides step-level credit\n      assignment without learned critic. >12% over GRPO on ALFWorld, >9% on WebShop.\n\n  - id: selfguide2026\n    title: \"Co-Evolution of Policy and Internal Reward for Language Agents (Self-Guide)\"\n    authors: \"Wang et al.\"\n    venue: \"arXiv\"\n    year: 2026\n    arxiv_id: \"2604.03098\"\n    category: method-component\n    role: predecessor\n    relevance_note: >\n      Direct predecessor. B-IAVR extends Self-Guide's co-evolving internal reward.\n      The self-guidance signal is the foundation for action-change detection triggering verification.\n      8% improvement over env-reward-only on ALFWorld with Qwen3-1.7B/4B.\n\n  - id: spear2025\n    title: \"Learn the Ropes, Then Trust the Wins: Self-imitation with Progressive Exploration for Agentic Reinforcement Learning\"\n    authors: \"Qin et al.\"\n    venue: \"ICLR 2026\"\n    year: 2025\n    arxiv_id: \"2509.22601\"\n    category: method-component\n    role: background\n    relevance_note: >\n      Curriculum-based self-imitation for sparse-reward agent tasks.\n      Up to +16.1% on ALFWorld over GRPO. Self-imitation curriculum could augment B-IAVR training.\n\n  - id: wei2025webagent-r1\n    title: \"WebAgent-R1: Training Web Agents via End-to-End Multi-Turn RL\"\n    authors: \"Wei et al.\"\n    venue: \"EMNLP 2025\"\n    year: 2025\n    arxiv_id: \"2505.16421\"\n    category: background\n    role: background\n    relevance_note: >\n      Extends GRPO to multi-turn (M-GRPO) with dynamic context compression.\n      Qwen-2.5-3B: 6.1% to 33.9% on WebArena-Lite. M-GRPO multi-turn extension relevant to B-IAVR.\n\n  - id: dapo2025\n    title: \"DAPO: An Open-Source LLM Reinforcement Learning System at Scale\"\n    authors: \"Yu et al.\"\n    venue: \"arXiv\"\n    year: 2025\n    arxiv_id: \"2503.14476\"\n    category: method-component\n    role: background\n    relevance_note: >\n      RL training stabilization techniques (Clip-Higher, Dynamic Sampling).\n      Applicable to B-IAVR's RL training to prevent entropy collapse.\n\n  - id: digiRL2024\n    title: \"DigiRL: Training In-The-Wild Device-Control Agents with Autonomous RL\"\n    authors: \"Bai et al.\"\n    venue: \"NeurIPS 2024\"\n    year: 2024\n    arxiv_id: \"2406.11896\"\n    category: background\n    role: background\n    relevance_note: >\n      Online RL for device control agents. Demonstrates online RL viability for interactive agents.\n      49.5% absolute improvement over SFT. Parallel approach to B-IAVR in text-based setting.\n\n  - id: li2025sorl\n    title: \"SORL: Stabilizing Off-Policy RL for Long-Horizon Agent Training\"\n    authors: \"Li et al.\"\n    venue: \"arXiv\"\n    year: 2025\n    arxiv_id: \"2511.20718\"\n    category: method-component\n    role: background\n    relevance_note: >\n      Turn-level importance sampling + clipping-triggered normalization for stable multi-turn agent RL.\n      Directly applicable to B-IAVR's multi-turn ALFWorld training stability.\n\n  - id: agentic-rl-survey-2025\n    title: \"The Landscape of Agentic Reinforcement Learning for LLMs: A Survey\"\n    authors: \"Zhang et al.\"\n    venue: \"TMLR 2026\"\n    year: 2025\n    arxiv_id: \"2509.02547\"\n    category: background\n    role: background\n    relevance_note: >\n      Comprehensive survey formalizing agentic RL. Contextualizes B-IAVR as training agents\n      to make meta-decisions (when to verify) via RL within the POMDP framework.\n\n  - id: skillmaster2026\n    title: \"SkillMaster: Toward Autonomous Skill Mastery in LLM Agents\"\n    authors: \"Yang et al.\"\n    venue: \"arXiv\"\n    year: 2026\n    arxiv_id: \"2605.08693\"\n    category: method-component\n    role: background\n    relevance_note: >\n      DualAdv-GRPO: separately estimates advantages for task-solving and skill-editing decisions.\n      +8.8% on ALFWorld, +9.3% on WebShop. DualAdv structure could inform B-IAVR's\n      separation of action and verification advantages.\n\n  - id: t2po2026\n    title: \"T2PO: Uncertainty-Guided Exploration Control for Stable Multi-Turn Agentic RL\"\n    authors: \"Wang et al.\"\n    venue: \"ICML 2026 Spotlight\"\n    year: 2026\n    arxiv_id: \"2605.02178\"\n    category: method-component\n    role: background\n    relevance_note: >\n      Token- and turn-level uncertainty monitoring for stable multi-turn agent RL.\n      Triggers thinking intervention when marginal uncertainty change drops below threshold.\n      Evaluated on ALFWorld and WebShop. Conceptually related: uncertainty-based trigger vs\n      B-IAVR's action-change trigger, but T2PO targets training stability, not deployment verification.\n\n  - id: gvpo2026\n    title: \"GVPO: Group Verification-based Policy Optimization for Interactive Coding Agents\"\n    authors: \"Dai et al.\"\n    venue: \"ICLR 2026\"\n    year: 2026\n    arxiv_id: null  # no arXiv preprint; OpenReview ID: RY47Tq0VsV\n    category: method-component\n    role: background\n    relevance_note: >\n      Advantage shaping with outcome-verifiable + process-verifiable signals.\n      +12.7% over o1 on AppWorld. Integrates intermediate execution feedback as step-level\n      verification signals. Different focus: uses verification for credit assignment during\n      training; B-IAVR learns when to invoke verification at deployment.\n\n  - id: agentv-rl2026\n    title: \"AgentV-RL: Scaling Reward Modeling with Agentic Verifier\"\n    authors: \"Zhang et al.\"\n    venue: \"arXiv\"\n    year: 2026\n    arxiv_id: \"2604.16004\"\n    category: method-component\n    role: background\n    relevance_note: >\n      Bidirectional forward/backward agentic verifier for reward modeling in RL.\n      4B model surpasses SOTA ORMs by 25.2%. Addresses verification quality in reward modeling;\n      B-IAVR addresses verification timing in agent deployment. Complementary.\n\n  - id: pa-moe2026\n    title: \"PA-MoE: Phase-Aware Mixture of Experts for Agentic Reinforcement Learning\"\n    authors: \"Li et al.\"\n    venue: \"arXiv\"\n    year: 2026\n    arxiv_id: \"2602.17038\"\n    category: evaluation\n    role: baseline\n    relevance_note: >\n      [NEW-0516] Lightweight phase router learns latent phase boundaries from RL objective.\n      PA-MoE+GiGPO with Qwen2.5-1.5B achieves 93.8% on ALFWorld (+7.7 over GiGPO 86.1%).\n      1.5B outperforms vanilla 7B GiGPO (90.2%). New small-model SOTA on ALFWorld.\n      Orthogonal architecture innovation; important baseline to cite.\n\n  - id: sdar2026\n    title: \"SDAR: Self-Distilled Agentic Reinforcement Learning\"\n    authors: \"Lu et al.\"\n    venue: \"arXiv\"\n    year: 2026\n    arxiv_id: \"2605.15155\"\n    category: method-component\n    role: background\n    relevance_note: >\n      [NEW-0516] On-policy self-distillation as gated auxiliary objective during RL training.\n      Token-level gate decides supervision intensity. +9.4% over GRPO on ALFWorld.\n      Complementary: SDAR improves RL training; B-IAVR learns verification policy.\n\n  - id: hcapo2026\n    title: \"HCAPO: Hindsight Credit Assignment for Long-Horizon LLM Agents\"\n    authors: \"Tan et al.\"\n    venue: \"arXiv\"\n    year: 2026\n    arxiv_id: \"2603.08754\"\n    category: method-component\n    role: background\n    relevance_note: >\n      [NEW-0516] LLM-as-critic refines step-level Q-values via hindsight reasoning +\n      multi-scale advantage for critical decision states.\n      +13.8% on ALFWorld, +7.7% on WebShop over GRPO (Qwen2.5-7B).\n      Could improve B-IAVR's reward signal for verification decision steps.\n\n  - id: act2026\n    title: \"ACT: Agentic Critical Training\"\n    authors: \"Liu et al.\"\n    venue: \"arXiv\"\n    year: 2026\n    arxiv_id: \"2603.08706\"\n    category: method-component\n    role: background\n    relevance_note: >\n      [NEW-0516] Trains agents to judge action quality via critical comparison reward.\n      +5.07 over IL, +4.62 over RL. Different axis: ACT improves reflection quality;\n      B-IAVR decides when to reflect.\n\n  - id: rwml2026\n    title: \"RWML: Reinforcement World Model Learning for LLM-based Agents\"\n    authors: \"Yu et al.\"\n    venue: \"arXiv\"\n    year: 2026\n    arxiv_id: \"2602.05842\"\n    category: method-component\n    role: background\n    relevance_note: >\n      [NEW-0516] Self-supervised world model via sim-to-real gap rewards in embedding space.\n      +6.9 on ALFWorld over task-success-only RL. Matches expert-data training.\n      Orthogonal: improves internal world model; B-IAVR adds selective verification.\n\n  - id: skill0-2026\n    title: \"SKILL0: In-Context Agentic Reinforcement Learning for Skill Internalization\"\n    authors: \"Lu et al.\"\n    venue: \"arXiv\"\n    year: 2026\n    arxiv_id: \"2604.02268\"\n    category: method-component\n    role: background\n    relevance_note: >\n      [NEW-0516] Training-time curriculum progressively withdraws skill context until zero-shot.\n      +9.7% on ALFWorld over GRPO, <0.5k tokens per step.\n      Complementary: SKILL0 internalizes skills; B-IAVR adds selective verification.\n\n  - id: fission-grpo2026\n    title: \"Fission-GRPO: Robust Tool Use via Learning to Recover from Execution Errors\"\n    authors: \"Zhang et al.\"\n    venue: \"arXiv\"\n    year: 2026\n    arxiv_id: \"2601.15625\"\n    category: method-component\n    role: background\n    relevance_note: >\n      [NEW-0516] Fissions failed trajectories into recovery training instances.\n      +4% overall accuracy on BFCL v4 Multi-Turn over GRPO.\n      Related: error recovery after failure vs B-IAVR's proactive verification.\n\n  - id: selfbudgeter2026\n    title: \"SelfBudgeter: Adaptive Token Allocation for Efficient LLM Reasoning\"\n    authors: \"Li et al.\"\n    venue: \"ICLR 2026 (under review)\"\n    year: 2025\n    arxiv_id: \"2505.11274\"\n    category: background\n    role: background\n    relevance_note: >\n      [NEW-0516] Self-estimated token budgets + budget-guided GRPO. 61% token reduction.\n      Parallel concept: SelfBudgeter allocates computation budget;\n      B-IAVR makes binary verify/not-verify decision. Both use RL for adaptive compute.\n\n  - id: cove2026\n    title: \"CoVe: Training Interactive Tool-Use Agents via Constraint-Guided Verification\"\n    authors: \"Chen et al.\"\n    venue: \"arXiv\"\n    year: 2026\n    arxiv_id: \"2603.01940\"\n    category: background\n    role: background\n    relevance_note: >\n      [NEW-0516] Task constraints guide trajectory generation and serve as deterministic verifiers.\n      Different: CoVe uses verification for data synthesis; B-IAVR learns when to verify at inference.\n\n  # ============================================================\n  # Direction 3: Selective Verification / Adaptive Computation\n  # ============================================================\n\n  - id: wan2025derailer-rerailer\n    title: \"Derailer-Rerailer: Adaptive Verification for Efficient and Reliable LM Reasoning\"\n    authors: \"Wan et al.\"\n    venue: \"ACL 2025 Findings\"\n    year: 2025\n    arxiv_id: \"2408.13940\"\n    category: direct-competitor\n    role: competitor\n    relevance_note: >\n      Most directly related competitor. Both do selective verification with binary trigger.\n      Key difference: operates on reasoning chains (single-turn); B-IAVR on agent trajectories (multi-turn).\n      Uses heuristic instability signal; B-IAVR uses RL-trained action-change signal.\n      8-11% accuracy gain, 2-3x efficiency over uniform verification.\n\n  - id: sherlock2025\n    title: \"Sherlock: Reliable and Efficient Agentic Workflow Execution\"\n    authors: \"Microsoft\"\n    venue: \"arXiv\"\n    year: 2025\n    arxiv_id: \"2511.00330\"\n    category: direct-competitor\n    role: competitor\n    relevance_note: >\n      Selective verification for agentic workflows via offline counterfactual analysis + speculative execution.\n      Different scope: workflow DAG level (offline); B-IAVR is step-level (online RL).\n      18.3% accuracy gain, 26% cost reduction, 48.7% latency reduction.\n\n  - id: singhi2025when-to-verify\n    title: \"When To Solve, When To Verify: Compute-Optimal Verification for LLM Reasoning\"\n    authors: \"Singhi et al.\"\n    venue: \"arXiv\"\n    year: 2025\n    arxiv_id: \"2504.01005\"\n    category: background\n    role: background\n    relevance_note: >\n      Derives inference scaling laws for solve-vs-verify tradeoff.\n      Finding that over-verification is suboptimal directly supports B-IAVR's selective approach.\n      B-IAVR learns this allocation via RL rather than analytically.\n\n  - id: yang2026ares\n    title: \"ARES: Adaptive Reasoning Effort Selection for Efficient LLM Agents\"\n    authors: \"Yang et al.\"\n    venue: \"arXiv\"\n    year: 2026\n    arxiv_id: \"2603.07915\"\n    category: direct-competitor\n    role: competitor\n    relevance_note: >\n      Closest competitor in agent domain. Both train learned per-step compute allocation.\n      ARES uses SFT-initialized router further refined via GRPO with outcome + token efficiency reward;\n      B-IAVR trains binary verify/not-verify via RL with action-change signal.\n      Key differences: (1) reward signal — ARES optimizes token efficiency, B-IAVR uses action-change\n      as verification trigger; (2) data requirement — ARES needs difficulty-annotated training data\n      to bootstrap the router, B-IAVR learns from environment interaction alone.\n      Reduces reasoning tokens by up to 52.7%.\n\n  - id: tu2025autothink\n    title: \"Learning When to Think: Shaping Adaptive Reasoning in R1-Style Models via Multi-Stage RL\"\n    authors: \"Tu et al.\"\n    venue: \"NeurIPS 2025\"\n    year: 2025\n    arxiv_id: \"2505.10832\"\n    category: direct-competitor\n    role: competitor\n    relevance_note: >\n      Analogous idea in reasoning domain: RL-trained adaptive computation trigger.\n      Operates on single-turn reasoning; B-IAVR on multi-turn agent trajectories.\n      +6.4% accuracy, -52% tokens on DeepSeek-R1-Distill-Qwen-1.5B.\n\n  - id: du2025thinkless\n    title: \"Thinkless: LLM Learns When to Think\"\n    authors: \"Fang et al.\"\n    venue: \"NeurIPS 2025\"\n    year: 2025\n    arxiv_id: \"2505.13379\"\n    category: direct-competitor\n    role: competitor\n    relevance_note: >\n      RL-trained control token to decide when to invoke extended thinking.\n      Methodologically closest to B-IAVR in reasoning domain; B-IAVR applies to interactive agent trajectories.\n\n  - id: wang2025efficient-agents\n    title: \"Efficient Agents: Building Effective Agents While Reducing Cost\"\n    authors: \"Wang et al.\"\n    venue: \"arXiv\"\n    year: 2025\n    arxiv_id: \"2508.02694\"\n    category: background\n    role: background\n    relevance_note: >\n      First systematic study of agent efficiency-effectiveness tradeoff.\n      Framework-level cost reduction; B-IAVR addresses cost at verification-policy level.\n      Retains 96.7% performance with 28.4% cost-of-pass improvement.\n\n  - id: venktesh2025trust-but-verify\n    title: \"Trust but Verify! A Survey on Verification Design for Test-time Scaling\"\n    authors: \"Venktesh et al.\"\n    venue: \"arXiv\"\n    year: 2025\n    arxiv_id: \"2508.16665\"\n    category: background\n    role: background\n    relevance_note: >\n      Survey of verification approaches for test-time compute scaling.\n      Identifies verification timing as key open problem. B-IAVR provides concrete solution for agent setting.\n\n  - id: agent-omit2026\n    title: \"Agent-Omit: Training Efficient LLM Agents for Adaptive Thought and Observation Omission via Agentic RL\"\n    authors: \"Ning et al.\"\n    venue: \"ICML 2026\"\n    year: 2026\n    arxiv_id: \"2602.04284\"\n    category: direct-competitor\n    role: competitor\n    relevance_note: >\n      RL-trained policy for adaptive omission of redundant thoughts and observations.\n      Agent-Omit-8B matches frontier agents with best efficiency tradeoff on 5 benchmarks.\n      Both use RL to learn cost-efficient agent behavior. Key difference: Agent-Omit subtracts\n      (omits unnecessary context); B-IAVR selectively adds (verification steps).\n      Opposite but complementary approaches to cost-efficiency. Potentially combinable.\n\n  - id: ava2026\n    title: \"Anytime Verified Agents: Adaptive Compute Allocation for Reliable LLM Reasoning under Budget Constraints\"\n    authors: \"Patel\"\n    venue: \"TMLR 2026\"\n    year: 2026\n    arxiv_id: null  # no arXiv preprint; OpenReview ID: JMDCMf7mlF\n    category: direct-competitor\n    role: competitor\n    relevance_note: >\n      Dynamic compute allocation across search, sampling, and verification under budget.\n      Uses calibrated uncertainty + value-of-information for selective verification cascades.\n      Evaluated on GSM8K/MATH/HotpotQA/HumanEval (reasoning), not interactive agents.\n      Key difference: analytical/heuristic allocation vs B-IAVR's RL-learned policy;\n      single-turn reasoning vs multi-turn agent trajectories.\n\n  - id: cast2026\n    title: \"CAST: Case-Based Calibration of Adaptive Reasoning and Execution for LLM Tool Use\"\n    authors: \"Pang et al.\"\n    venue: \"arXiv\"\n    year: 2026\n    arxiv_id: \"2605.15041\"\n    category: background\n    role: background\n    relevance_note: >\n      Historical execution cases calibrate reasoning depth for tool use.\n      Reduces reasoning length 26% with +5.85% accuracy on BFCLv2/ToolBench.\n      Related: adaptive reasoning depth; different: case-based calibration vs RL-learned policy.\n\n  - id: marginal-token-allocators2026\n    title: \"Agentic AI Systems Should Be Designed as Marginal Token Allocators\"\n    authors: \"Zhu\"\n    venue: \"arXiv\"\n    year: 2026\n    arxiv_id: \"2605.01214\"\n    category: background\n    role: background\n    relevance_note: >\n      Position paper framing agent cost-efficiency as marginal token allocation economics.\n      Identifies under-verification as systematic failure mode. Supports B-IAVR's framing\n      that verification decisions should reflect marginal cost-benefit analysis.\n\n  - id: argos2025\n    title: \"Argos: Multimodal RL with Adaptive Verifier for AI Agents\"\n    authors: \"Tan et al.\"\n    venue: \"arXiv (revised April 2026)\"\n    year: 2025\n    arxiv_id: \"2512.03438\"\n    category: background\n    role: background\n    relevance_note: >\n      Agentic verifier that adaptively selects scoring functions for multimodal RL training.\n      Different domain (multimodal/robotics). The adaptive verifier selection concept is\n      complementary: Argos adapts how to verify; B-IAVR adapts when to verify.\n\n  # ============================================================\n  # Direction 4: ALFWorld / Interactive Environment Benchmarks\n  # ============================================================\n\n  - id: kim2025reflact\n    title: \"ReflAct: World-Grounded Decision Making in LLM Agents via Goal-State Reflection\"\n    authors: \"Kim et al.\"\n    venue: \"EMNLP 2025\"\n    year: 2025\n    arxiv_id: \"2505.15182\"\n    category: evaluation\n    role: baseline\n    relevance_note: >\n      Prompting SOTA on ALFWorld at 93.3%. Replaces ReAct's next-action thinking with state-goal reflection.\n      B-IAVR addresses different axis (cost-efficiency) since ALFWorld accuracy is near saturation.\n\n  - id: choudhury2025agentprm\n    title: \"Process Reward Models for LLM Agents: Practical Framework and Directions\"\n    authors: \"Choudhury\"\n    venue: \"arXiv\"\n    year: 2025\n    arxiv_id: \"2502.10325\"\n    category: evaluation\n    role: baseline\n    relevance_note: >\n      Monte Carlo rollout-based process reward for agent training. 3B models achieve 91% on ALFWorld.\n      Validates RL training approach; AgentPRM could serve as reward model for B-IAVR.\n\n  - id: xi2025agentprm\n    title: \"AgentPRM: Process Reward Models for LLM Agents via Step-Wise Promise and Progress\"\n    authors: \"Xi et al.\"\n    venue: \"ACM Web Conference 2026\"\n    year: 2025\n    arxiv_id: \"2511.08325\"\n    category: evaluation\n    role: baseline\n    relevance_note: >\n      Independent work from Choudhury et al., using TD-based estimation with GAE for scalable\n      PRM data labeling. 8x more compute-efficient than baselines with robust test-time scaling.\n      Different approach: Choudhury uses MC rollouts; Xi uses TD+GAE for step-wise promise and progress.\n\n  - id: xiang2024retrospex\n    title: \"Retrospex: Language Agent Meets Offline RL Critic\"\n    authors: \"Xiang et al.\"\n    venue: \"EMNLP 2024\"\n    year: 2024\n    arxiv_id: \"2505.11807\"\n    category: background\n    role: background\n    relevance_note: >\n      Offline RL Critic augments LLM agent action selection via dynamic rescoring.\n      Similar architecture could inform B-IAVR's verification value estimation.\n\n  - id: cfgm2025\n    title: \"CFGM: Coarse-to-Fine Grounded Memory for LLM Agent Planning\"\n    authors: \"Yang et al.\"\n    venue: \"EMNLP 2025\"\n    year: 2025\n    arxiv_id: \"2508.15305\"\n    category: background\n    role: background\n    relevance_note: >\n      Memory-augmented agent planning with episodic grounding.\n      ALFWorld +10.40%, WebShop +20%. Complementary to B-IAVR's verification approach.\n\n  - id: respact2024\n    title: \"ReSpAct: Harmonizing Reasoning, Speaking, and Acting\"\n    authors: \"Dongre et al.\"\n    venue: \"arXiv\"\n    year: 2024\n    arxiv_id: \"2411.00927\"\n    category: evaluation\n    role: baseline\n    relevance_note: >\n      Integrates dialogue/reasoning/acting. +6% over ReAct on ALFWorld.\n      Reduces invalid actions from 13% to 3%; B-IAVR's verification achieves error prevention differently.\n\n  # ============================================================\n  # Direction 5: Multi-Turn Credit Assignment (Direct Competitors)\n  # ============================================================\n\n  - id: turn-ppo2025\n    title: \"Turn-Level Policy Optimization for Multi-Turn Agent Reinforcement Learning\"\n    authors: \"Zhou et al.\"\n    venue: \"arXiv\"\n    year: 2025\n    arxiv_id: \"2512.17008\"\n    category: direct-competitor\n    role: competitor\n    relevance_note: >\n      [NEW-0517] Most direct competitor. Identifies \"uniform advantage\" problem in\n      step-independent GRPO (subset of our \"sign misattribution\"). Proposes turn-level\n      MDP + learned value function. Our differences: (1) more precise formalization\n      (sign misattribution + gamma decay quantification), (2) contrarian solution\n      (episode-level coarser credit vs their finer turn-level credit).\n\n  - id: gagpo2026\n    title: \"GAGPO: Generalized Advantage Grouped Policy Optimization\"\n    authors: \"Zhu et al.\"\n    venue: \"arXiv\"\n    year: 2026\n    arxiv_id: \"2605.13217\"\n    category: direct-competitor\n    role: competitor\n    relevance_note: >\n      [NEW-0517] Critic-free step-aligned credit via non-parametric grouped value proxy +\n      TD/GAE-style temporal advantages. ALFWorld 93.5% (1.5B), 95.6% (7B).\n      Pursues finer-grained credit to improve performance; our work diagnoses why\n      step-independent fails (sign misattribution) and shows coarser episode-level suffices.\n      Different contribution axis: performance optimization vs mechanism diagnosis.\n\n  - id: mt-grpo2025\n    title: \"Reinforcing Multi-Turn Reasoning in LLM Agents via Turn-Level Reward Design\"\n    authors: \"Wei et al.\"\n    venue: \"arXiv\"\n    year: 2025\n    arxiv_id: \"2505.11821\"\n    category: direct-competitor\n    role: competitor\n    relevance_note: >\n      [NEW-0517] Proposes MT-GRPO with turn-level reward design for multi-turn RL.\n      Evaluated on QA search tasks (NQ, TriviaQA, HotpotQA), not ALFWorld.\n      Qwen2.5-7B. Same direction as Turn-PPO (finer turn-level credit);\n      our contrarian shows coarser episode-level eliminates sign misattribution.\n\n  - id: istar2025\n    title: \"Agentic Reinforcement Learning with Implicit Step Rewards\"\n    authors: \"Liu et al.\"\n    venue: \"ICLR 2026\"\n    year: 2025\n    arxiv_id: \"2509.19199\"\n    category: direct-competitor\n    role: competitor\n    relevance_note: >\n      [NEW-0517] Implicit PRM + dual advantage (step + episode level) for agentic RL.\n      WebShop 86.5%, VisualSokoban 91.7%. ICLR 2026 published.\n      Learns step-level credit via implicit rewards without explicit labels;\n      our work shows episode-level alone suffices when sign misattribution is the bottleneck.\n      Validates that step-level credit helps, but doesn't diagnose when it hurts.\n\n  - id: archer2024\n    title: \"ArCHer: Training Language Model Agents via Hierarchical Multi-Turn RL\"\n    authors: \"Zhou, Zanette, Pan, Levine, Kumar\"\n    venue: \"ICML 2024\"\n    year: 2024\n    arxiv_id: \"2402.19446\"\n    category: method-component\n    role: predecessor\n    relevance_note: >\n      [NEW-0517] Foundational hierarchical multi-turn RL framework (ICML 2024).\n      High-level off-policy value RL (utterance-level) + low-level token policy.\n      ~100x sample efficiency. Establishes that multi-turn RL needs hierarchical structure;\n      our work specifically diagnoses why flat step-independent approaches fail.\n\n  - id: ca-survey2026\n    title: \"From Reasoning to Agentic: Credit Assignment in Reinforcement Learning for Large Language Models\"\n    authors: \"Zhang\"\n    venue: \"arXiv\"\n    year: 2026\n    arxiv_id: \"2604.09459\"\n    category: background\n    role: background\n    relevance_note: >\n      [NEW-0517] Comprehensive survey of 47 CA methods (2024-2026). Two-dimensional\n      taxonomy: granularity (token/segment/step/turn/multi-agent) x methodology\n      (MC/TD/model-based/game-theoretic/information-theoretic). Contextualizes our\n      sign misattribution diagnosis within the broader CA landscape.\n\n  - id: hiper2026\n    title: \"HiPER: Hierarchical Reinforcement Learning with Explicit Credit Assignment for Large Language Model Agents\"\n    authors: \"Peng et al.\"\n    venue: \"arXiv\"\n    year: 2026\n    arxiv_id: \"2602.16165\"\n    category: method-component\n    role: background\n    relevance_note: >\n      [NEW-0517] Hierarchical Plan-Execute RL. ALFWorld 97.4% (7B), 95.3% (1.5B).\n      GRPO baseline: 71.1% (1.5B), 85.4% (7B). 2.8x training efficiency gain.\n      Pursues SOTA performance via hierarchical plan-execute architecture;\n      our work does mechanism diagnosis of why step-independent GRPO fails.\n      Different contribution dimension: not comparable on performance axis.\n",
      "numLines": 733,
      "startLine": 1,
      "totalLines": 733
    }
  },
  "sourceToolAssistantUUID": "477600c2-f803-4782-9c16-2d55175e0e2e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "7317ebb2-d910-42e9-95dc-fa8559b8ce74",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 22_

```json
{
  "type": "last-prompt",
  "leafUuid": "5a16cba2-54e0-44c9-940d-fb2909f89be3",
  "sessionId": "7317ebb2-d910-42e9-95dc-fa8559b8ce74"
}
```

---

### Runtime record

_source line 23_

```json
{
  "type": "ai-title",
  "aiTitle": "Verify and correct Turn-PPO citation information",
  "sessionId": "7317ebb2-d910-42e9-95dc-fa8559b8ce74"
}
```

---

### Tool call

_source line 24 · 2026-05-17T13:46:14.174Z_

<details open><summary>🔧 Tool call — Edit · `toolu_016P7havNFJL69dw6xszyMpF`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/literature_map.yaml",
  "old_string": "  - id: turn-ppo2025\n    title: \"Turn-Level Policy Optimization for Multi-Turn Agent Reinforcement Learning\"\n    authors: \"Zhou et al.\"",
  "new_string": "  - id: turn-ppo2025\n    title: \"Turn-PPO: Turn-Level Advantage Estimation with PPO for Improved Multi-Turn RL in Agentic LLMs\"\n    authors: \"Li et al.\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5a16cba2-54e0-44c9-940d-fb2909f89be3",
  "isSidechain": false,
  "requestId": "req_011Cb8F4bXsfyZU81NpfG72q",
  "type": "assistant",
  "uuid": "2db8002d-1cc5-48d5-a1ae-66cf535e20b4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "7317ebb2-d910-42e9-95dc-fa8559b8ce74",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Gxc9dNV8UbecYXAMg7GJDP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11457,
      "cache_read_input_tokens": 38083,
      "output_tokens": 220,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11457,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 220,
          "cache_read_input_tokens": 38083,
          "cache_creation_input_tokens": 11457,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11457
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

_source line 25 · 2026-05-17T13:46:14.204Z_

<details><summary>↩ Tool result · `toolu_016P7havNFJL69dw6xszyMpF`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/literature_map.yaml has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2db8002d-1cc5-48d5-a1ae-66cf535e20b4",
  "isSidechain": false,
  "promptId": "71e953e0-39de-4d6a-a9b9-c8a649da7bce",
  "type": "user",
  "uuid": "e072cc87-a788-4b2c-88e3-a3f9ac7f54c1",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/literature_map.yaml",
    "oldString": "  - id: turn-ppo2025\n    title: \"Turn-Level Policy Optimization for Multi-Turn Agent Reinforcement Learning\"\n    authors: \"Zhou et al.\"",
    "newString": "  - id: turn-ppo2025\n    title: \"Turn-PPO: Turn-Level Advantage Estimation with PPO for Improved Multi-Turn RL in Agentic LLMs\"\n    authors: \"Li et al.\"",
    "originalFile": null,
    "structuredPatch": [
      {
        "oldStart": 630,
        "oldLines": 8,
        "newStart": 630,
        "newLines": 8,
        "lines": [
          "   # ============================================================",
          " ",
          "   - id: turn-ppo2025",
          "-    title: \"Turn-Level Policy Optimization for Multi-Turn Agent Reinforcement Learning\"",
          "-    authors: \"Zhou et al.\"",
          "+    title: \"Turn-PPO: Turn-Level Advantage Estimation with PPO for Improved Multi-Turn RL in Agentic LLMs\"",
          "+    authors: \"Li et al.\"",
          "     venue: \"arXiv\"",
          "     year: 2025",
          "     arxiv_id: \"2512.17008\""
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "2db8002d-1cc5-48d5-a1ae-66cf535e20b4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "7317ebb2-d910-42e9-95dc-fa8559b8ce74",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 26 · 2026-05-17T13:46:17.146Z_

Now save via the project file tool.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e072cc87-a788-4b2c-88e3-a3f9ac7f54c1",
  "isSidechain": false,
  "requestId": "req_011Cb8F52bWCZuw6yPG5ej8P",
  "type": "assistant",
  "uuid": "3e93825b-f36d-416a-a97d-e28b45e3c749",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "7317ebb2-d910-42e9-95dc-fa8559b8ce74",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KGjBB8XnPwewTbNBRkLArH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 293,
      "cache_read_input_tokens": 49540,
      "output_tokens": 131,
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
          "output_tokens": 131,
          "cache_read_input_tokens": 49540,
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

_source line 27 · 2026-05-17T13:46:17.668Z_

<details open><summary>🔧 Tool call — Read · `toolu_01DtkykLTsFaBjgN57EFa2Kf`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/literature_map.yaml",
  "offset": 628,
  "limit": 20
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3e93825b-f36d-416a-a97d-e28b45e3c749",
  "isSidechain": false,
  "requestId": "req_011Cb8F52bWCZuw6yPG5ej8P",
  "type": "assistant",
  "uuid": "7f90c7da-8178-4b34-9b7e-97fda1c81843",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "7317ebb2-d910-42e9-95dc-fa8559b8ce74",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KGjBB8XnPwewTbNBRkLArH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 293,
      "cache_read_input_tokens": 49540,
      "output_tokens": 131,
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
          "output_tokens": 131,
          "cache_read_input_tokens": 49540,
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

_source line 28 · 2026-05-17T13:46:17.673Z_

<details><summary>↩ Tool result · `toolu_01DtkykLTsFaBjgN57EFa2Kf`</summary>

```text
628	  # ============================================================
629	  # Direction 5: Multi-Turn Credit Assignment (Direct Competitors)
630	  # ============================================================
631	
632	  - id: turn-ppo2025
633	    title: "Turn-PPO: Turn-Level Advantage Estimation with PPO for Improved Multi-Turn RL in Agentic LLMs"
634	    authors: "Li et al."
635	    venue: "arXiv"
636	    year: 2025
637	    arxiv_id: "2512.17008"
638	    category: direct-competitor
639	    role: competitor
640	    relevance_note: >
641	      [NEW-0517] Most direct competitor. Identifies "uniform advantage" problem in
642	      step-independent GRPO (subset of our "sign misattribution"). Proposes turn-level
643	      MDP + learned value function. Our differences: (1) more precise formalization
644	      (sign misattribution + gamma decay quantification), (2) contrarian solution
645	      (episode-level coarser credit vs their finer turn-level credit).
646	
647	  - id: gagpo2026
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7f90c7da-8178-4b34-9b7e-97fda1c81843",
  "isSidechain": false,
  "promptId": "71e953e0-39de-4d6a-a9b9-c8a649da7bce",
  "type": "user",
  "uuid": "095fb3b3-e85a-4aaf-bc74-35a9c06344ee",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/literature_map.yaml",
      "content": "  # ============================================================\n  # Direction 5: Multi-Turn Credit Assignment (Direct Competitors)\n  # ============================================================\n\n  - id: turn-ppo2025\n    title: \"Turn-PPO: Turn-Level Advantage Estimation with PPO for Improved Multi-Turn RL in Agentic LLMs\"\n    authors: \"Li et al.\"\n    venue: \"arXiv\"\n    year: 2025\n    arxiv_id: \"2512.17008\"\n    category: direct-competitor\n    role: competitor\n    relevance_note: >\n      [NEW-0517] Most direct competitor. Identifies \"uniform advantage\" problem in\n      step-independent GRPO (subset of our \"sign misattribution\"). Proposes turn-level\n      MDP + learned value function. Our differences: (1) more precise formalization\n      (sign misattribution + gamma decay quantification), (2) contrarian solution\n      (episode-level coarser credit vs their finer turn-level credit).\n\n  - id: gagpo2026",
      "numLines": 20,
      "startLine": 628,
      "totalLines": 733
    }
  },
  "sourceToolAssistantUUID": "7f90c7da-8178-4b34-9b7e-97fda1c81843",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "7317ebb2-d910-42e9-95dc-fa8559b8ce74",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 29 · 2026-05-17T13:46:20.304Z_

修正已完成。现在同步到 MCP 项目文件。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "095fb3b3-e85a-4aaf-bc74-35a9c06344ee",
  "isSidechain": false,
  "requestId": "req_011Cb8F5Gn2wiUyHYodRvie8",
  "type": "assistant",
  "uuid": "9713f5cf-300e-4899-b832-4b13dc3eacb9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "7317ebb2-d910-42e9-95dc-fa8559b8ce74",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016JJRtpx9ATyUJeCtAaopa1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 430,
      "cache_read_input_tokens": 49833,
      "output_tokens": 109,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 430,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 109,
          "cache_read_input_tokens": 49833,
          "cache_creation_input_tokens": 430,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 430
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

_source line 30 · 2026-05-17T13:46:20.625Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Qb7Q3R5XNkeq3dEfYreTKt`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/literature_map.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9713f5cf-300e-4899-b832-4b13dc3eacb9",
  "isSidechain": false,
  "requestId": "req_011Cb8F5Gn2wiUyHYodRvie8",
  "type": "assistant",
  "uuid": "cce95bc1-b851-4a1e-aa34-da0f26f68eac",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "7317ebb2-d910-42e9-95dc-fa8559b8ce74",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016JJRtpx9ATyUJeCtAaopa1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 430,
      "cache_read_input_tokens": 49833,
      "output_tokens": 109,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 430,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 109,
          "cache_read_input_tokens": 49833,
          "cache_creation_input_tokens": 430,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 430
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

_source line 31 · 2026-05-17T13:46:20.960Z_

<details><summary>↩ Tool result · `toolu_01Qb7Q3R5XNkeq3dEfYreTKt`</summary>

```text
1	# B-IAVR Literature Map
2	# Updated: 2026-05-17
3	# Categories: direct-competitor, method-component, background, evaluation
4	# Roles: predecessor, competitor, baseline, evaluation, background
5	
6	papers:
7	
8	  # ============================================================
9	  # Direction 1: Self-Verification / Self-Correction in LLM Agents
10	  # ============================================================
11	
12	  - id: kamoi2024self-correction-survey
13	    title: "When Can LLMs Actually Correct Their Own Mistakes? A Critical Survey of Self-Correction of LLMs"
14	    authors: "Kamoi et al."
15	    venue: "arXiv"
16	    year: 2024
17	    arxiv_id: "2406.01297"
18	    category: background
19	    role: background
20	    relevance_note: >
21	      Foundational survey establishing that pure intrinsic self-correction is unreliable.
22	      Validates B-IAVR's use of grounded verification (environment re-observation) over prompted self-feedback.
23	
24	  - id: tie2025correctbench
25	    title: "Can LLMs Correct Themselves? A Benchmark of Self-Correction in LLMs"
26	    authors: "Tie et al."
27	    venue: "NeurIPS 2025 Datasets & Benchmarks"
28	    year: 2025
29	    arxiv_id: "2510.16062"
30	    category: background
31	    role: background
32	    relevance_note: >
33	      Benchmark showing self-correction has diminishing returns when applied uniformly.
34	      Supports B-IAVR's selective verification design over blanket correction.
35	
36	  - id: self-verification-dilemma-2026
37	    title: "Self-Verification Dilemma: Experience-Driven Suppression of Overused Checking in LLM Reasoning"
38	    authors: "Long et al."
39	    venue: "arXiv"
40	    year: 2026
41	    arxiv_id: "2602.03485"
42	    category: background
43	    role: background
44	    relevance_note: >
45	      Empirically validates that >90% of self-verification is confirmatory, ~2% corrective.
46	      Directly supports B-IAVR's core thesis that verification should be selective.
47	      Their experience-pool approach is complementary to B-IAVR's action-change signal.
48	
49	  - id: zhang2025incentivize-self-verify
50	    title: "Incentivizing LLMs to Self-Verify Their Answers"
51	    authors: "Zhang et al."
52	    venue: "arXiv"
53	    year: 2025
54	    arxiv_id: "2506.01369"
55	    category: background
56	    role: background
57	    relevance_note: >
58	      Unifies answer generation and verification via single RL training process.
59	      Parallel to B-IAVR: they train verification into generation; B-IAVR trains when to trigger separate verification.
60	
61	  - id: mar2025
62	    title: "MAR: Multi-Agent Reflexion Improves Reasoning Abilities in LLMs"
63	    authors: "Ozer et al."
64	    venue: "arXiv"
65	    year: 2025
66	    arxiv_id: "2512.20845"
67	    category: background
68	    role: background
69	    relevance_note: >
70	      Multi-agent self-correction with diverse critic personas.
71	      Complementary: MAR improves correction quality; B-IAVR decides when to trigger correction.
72	
73	  - id: ssr2025
74	    title: "SSR: Socratic Self-Refine for Large Language Model Reasoning"
75	    authors: "Shi et al."
76	    venue: "arXiv"
77	    year: 2025
78	    arxiv_id: "2511.10621"
79	    category: background
80	    role: background
81	    relevance_note: >
82	      Structured Socratic questioning for self-refinement.
83	      Complementary: improves correction step quality; B-IAVR focuses on when to invoke correction.
84	
85	  - id: verifiagent2025
86	    title: "VerifiAgent: a Unified Verification Agent in Language Model Reasoning"
87	    authors: "Han et al."
88	    venue: "EMNLP 2025 Findings"
89	    year: 2025
90	    arxiv_id: "2504.00406"
91	    category: background
92	    role: background
93	    relevance_note: >
94	      Unified verification agent with meta-verification + tool-based adaptive verification.
95	      Focuses on how to verify (tool selection); B-IAVR focuses on when to verify (policy learning).
96	      Complementary: VerifiAgent's verification quality could enhance B-IAVR's verification step.
97	
98	  # ============================================================
99	  # Direction 2: Agent RL Training
100	  # ============================================================
101	
102	  - id: feng2025gigpo
103	    title: "GiGPO: Group-in-Group Policy Optimization for LLM Agent Training"
104	    authors: "Feng et al."
105	    venue: "NeurIPS 2025"
106	    year: 2025
107	    arxiv_id: "2505.10978"
108	    category: method-component
109	    role: predecessor
110	    relevance_note: >
111	      Core training algorithm for B-IAVR. Nested group structure provides step-level credit
112	      assignment without learned critic. >12% over GRPO on ALFWorld, >9% on WebShop.
113	
114	  - id: selfguide2026
115	    title: "Co-Evolution of Policy and Internal Reward for Language Agents (Self-Guide)"
116	    authors: "Wang et al."
117	    venue: "arXiv"
118	    year: 2026
119	    arxiv_id: "2604.03098"
120	    category: method-component
121	    role: predecessor
122	    relevance_note: >
123	      Direct predecessor. B-IAVR extends Self-Guide's co-evolving internal reward.
124	      The self-guidance signal is the foundation for action-change detection triggering verification.
125	      8% improvement over env-reward-only on ALFWorld with Qwen3-1.7B/4B.
126	
127	  - id: spear2025
128	    title: "Learn the Ropes, Then Trust the Wins: Self-imitation with Progressive Exploration for Agentic Reinforcement Learning"
129	    authors: "Qin et al."
130	    venue: "ICLR 2026"
131	    year: 2025
132	    arxiv_id: "2509.22601"
133	    category: method-component
134	    role: background
135	    relevance_note: >
136	      Curriculum-based self-imitation for sparse-reward agent tasks.
137	      Up to +16.1% on ALFWorld over GRPO. Self-imitation curriculum could augment B-IAVR training.
138	
139	  - id: wei2025webagent-r1
140	    title: "WebAgent-R1: Training Web Agents via End-to-End Multi-Turn RL"
141	    authors: "Wei et al."
142	    venue: "EMNLP 2025"
143	    year: 2025
144	    arxiv_id: "2505.16421"
145	    category: background
146	    role: background
147	    relevance_note: >
148	      Extends GRPO to multi-turn (M-GRPO) with dynamic context compression.
149	      Qwen-2.5-3B: 6.1% to 33.9% on WebArena-Lite. M-GRPO multi-turn extension relevant to B-IAVR.
150	
151	  - id: dapo2025
152	    title: "DAPO: An Open-Source LLM Reinforcement Learning System at Scale"
153	    authors: "Yu et al."
154	    venue: "arXiv"
155	    year: 2025
156	    arxiv_id: "2503.14476"
157	    category: method-component
158	    role: background
159	    relevance_note: >
160	      RL training stabilization techniques (Clip-Higher, Dynamic Sampling).
161	      Applicable to B-IAVR's RL training to prevent entropy collapse.
162	
163	  - id: digiRL2024
164	    title: "DigiRL: Training In-The-Wild Device-Control Agents with Autonomous RL"
165	    authors: "Bai et al."
166	    venue: "NeurIPS 2024"
167	    year: 2024
168	    arxiv_id: "2406.11896"
169	    category: background
170	    role: background
171	    relevance_note: >
172	      Online RL for device control agents. Demonstrates online RL viability for interactive agents.
173	      49.5% absolute improvement over SFT. Parallel approach to B-IAVR in text-based setting.
174	
175	  - id: li2025sorl
176	    title: "SORL: Stabilizing Off-Policy RL for Long-Horizon Agent Training"
177	    authors: "Li et al."
178	    venue: "arXiv"
179	    year: 2025
180	    arxiv_id: "2511.20718"
181	    category: method-component
182	    role: background
183	    relevance_note: >
184	      Turn-level importance sampling + clipping-triggered normalization for stable multi-turn agent RL.
185	      Directly applicable to B-IAVR's multi-turn ALFWorld training stability.
186	
187	  - id: agentic-rl-survey-2025
188	    title: "The Landscape of Agentic Reinforcement Learning for LLMs: A Survey"
189	    authors: "Zhang et al."
190	    venue: "TMLR 2026"
191	    year: 2025
192	    arxiv_id: "2509.02547"
193	    category: background
194	    role: background
195	    relevance_note: >
196	      Comprehensive survey formalizing agentic RL. Contextualizes B-IAVR as training agents
197	      to make meta-decisions (when to verify) via RL within the POMDP framework.
198	
199	  - id: skillmaster2026
200	    title: "SkillMaster: Toward Autonomous Skill Mastery in LLM Agents"
201	    authors: "Yang et al."
202	    venue: "arXiv"
203	    year: 2026
204	    arxiv_id: "2605.08693"
205	    category: method-component
206	    role: background
207	    relevance_note: >
208	      DualAdv-GRPO: separately estimates advantages for task-solving and skill-editing decisions.
209	      +8.8% on ALFWorld, +9.3% on WebShop. DualAdv structure could inform B-IAVR's
210	      separation of action and verification advantages.
211	
212	  - id: t2po2026
213	    title: "T2PO: Uncertainty-Guided Exploration Control for Stable Multi-Turn Agentic RL"
214	    authors: "Wang et al."
215	    venue: "ICML 2026 Spotlight"
216	    year: 2026
217	    arxiv_id: "2605.02178"
218	    category: method-component
219	    role: background
220	    relevance_note: >
221	      Token- and turn-level uncertainty monitoring for stable multi-turn agent RL.
222	      Triggers thinking intervention when marginal uncertainty change drops below threshold.
223	      Evaluated on ALFWorld and WebShop. Conceptually related: uncertainty-based trigger vs
224	      B-IAVR's action-change trigger, but T2PO targets training stability, not deployment verification.
225	
226	  - id: gvpo2026
227	    title: "GVPO: Group Verification-based Policy Optimization for Interactive Coding Agents"
228	    authors: "Dai et al."
229	    venue: "ICLR 2026"
230	    year: 2026
231	    arxiv_id: null  # no arXiv preprint; OpenReview ID: RY47Tq0VsV
232	    category: method-component
233	    role: background
234	    relevance_note: >
235	      Advantage shaping with outcome-verifiable + process-verifiable signals.
236	      +12.7% over o1 on AppWorld. Integrates intermediate execution feedback as step-level
237	      verification signals. Different focus: uses verification for credit assignment during
238	      training; B-IAVR learns when to invoke verification at deployment.
239	
240	  - id: agentv-rl2026
241	    title: "AgentV-RL: Scaling Reward Modeling with Agentic Verifier"
242	    authors: "Zhang et al."
243	    venue: "arXiv"
244	    year: 2026
245	    arxiv_id: "2604.16004"
246	    category: method-component
247	    role: background
248	    relevance_note: >
249	      Bidirectional forward/backward agentic verifier for reward modeling in RL.
250	      4B model surpasses SOTA ORMs by 25.2%. Addresses verification quality in reward modeling;
251	      B-IAVR addresses verification timing in agent deployment. Complementary.
252	
253	  - id: pa-moe2026
254	    title: "PA-MoE: Phase-Aware Mixture of Experts for Agentic Reinforcement Learning"
255	    authors: "Li et al."
256	    venue: "arXiv"
257	    year: 2026
258	    arxiv_id: "2602.17038"
259	    category: evaluation
260	    role: baseline
261	    relevance_note: >
262	      [NEW-0516] Lightweight phase router learns latent phase boundaries from RL objective.
263	      PA-MoE+GiGPO with Qwen2.5-1.5B achieves 93.8% on ALFWorld (+7.7 over GiGPO 86.1%).
264	      1.5B outperforms vanilla 7B GiGPO (90.2%). New small-model SOTA on ALFWorld.
265	      Orthogonal architecture innovation; important baseline to cite.
266	
267	  - id: sdar2026
268	    title: "SDAR: Self-Distilled Agentic Reinforcement Learning"
269	    authors: "Lu et al."
270	    venue: "arXiv"
271	    year: 2026
272	    arxiv_id: "2605.15155"
273	    category: method-component
274	    role: background
275	    relevance_note: >
276	      [NEW-0516] On-policy self-distillation as gated auxiliary objective during RL training.
277	      Token-level gate decides supervision intensity. +9.4% over GRPO on ALFWorld.
278	      Complementary: SDAR improves RL training; B-IAVR learns verification policy.
279	
280	  - id: hcapo2026
281	    title: "HCAPO: Hindsight Credit Assignment for Long-Horizon LLM Agents"
282	    authors: "Tan et al."
283	    venue: "arXiv"
284	    year: 2026
285	    arxiv_id: "2603.08754"
286	    category: method-component
287	    role: background
288	    relevance_note: >
289	      [NEW-0516] LLM-as-critic refines step-level Q-values via hindsight reasoning +
290	      multi-scale advantage for critical decision states.
291	      +13.8% on ALFWorld, +7.7% on WebShop over GRPO (Qwen2.5-7B).
292	      Could improve B-IAVR's reward signal for verification decision steps.
293	
294	  - id: act2026
295	    title: "ACT: Agentic Critical Training"
296	    authors: "Liu et al."
297	    venue: "arXiv"
298	    year: 2026
299	    arxiv_id: "2603.08706"
300	    category: method-component
301	    role: background
302	    relevance_note: >
303	      [NEW-0516] Trains agents to judge action quality via critical comparison reward.
304	      +5.07 over IL, +4.62 over RL. Different axis: ACT improves reflection quality;
305	      B-IAVR decides when to reflect.
306	
307	  - id: rwml2026
308	    title: "RWML: Reinforcement World Model Learning for LLM-based Agents"
309	    authors: "Yu et al."
310	    venue: "arXiv"
311	    year: 2026
312	    arxiv_id: "2602.05842"
313	    category: method-component
314	    role: background
315	    relevance_note: >
316	      [NEW-0516] Self-supervised world model via sim-to-real gap rewards in embedding space.
317	      +6.9 on ALFWorld over task-success-only RL. Matches expert-data training.
318	      Orthogonal: improves internal world model; B-IAVR adds selective verification.
319	
320	  - id: skill0-2026
321	    title: "SKILL0: In-Context Agentic Reinforcement Learning for Skill Internalization"
322	    authors: "Lu et al."
323	    venue: "arXiv"
324	    year: 2026
325	    arxiv_id: "2604.02268"
326	    category: method-component
327	    role: background
328	    relevance_note: >
329	      [NEW-0516] Training-time curriculum progressively withdraws skill context until zero-shot.
330	      +9.7% on ALFWorld over GRPO, <0.5k tokens per step.
331	      Complementary: SKILL0 internalizes skills; B-IAVR adds selective verification.
332	
333	  - id: fission-grpo2026
334	    title: "Fission-GRPO: Robust Tool Use via Learning to Recover from Execution Errors"
335	    authors: "Zhang et al."
336	    venue: "arXiv"
337	    year: 2026
338	    arxiv_id: "2601.15625"
339	    category: method-component
340	    role: background
341	    relevance_note: >
342	      [NEW-0516] Fissions failed trajectories into recovery training instances.
343	      +4% overall accuracy on BFCL v4 Multi-Turn over GRPO.
344	      Related: error recovery after failure vs B-IAVR's proactive verification.
345	
346	  - id: selfbudgeter2026
347	    title: "SelfBudgeter: Adaptive Token Allocation for Efficient LLM Reasoning"
348	    authors: "Li et al."
349	    venue: "ICLR 2026 (under review)"
350	    year: 2025
351	    arxiv_id: "2505.11274"
352	    category: background
353	    role: background
354	    relevance_note: >
355	      [NEW-0516] Self-estimated token budgets + budget-guided GRPO. 61% token reduction.
356	      Parallel concept: SelfBudgeter allocates computation budget;
357	      B-IAVR makes binary verify/not-verify decision. Both use RL for adaptive compute.
358	
359	  - id: cove2026
360	    title: "CoVe: Training Interactive Tool-Use Agents via Constraint-Guided Verification"
361	    authors: "Chen et al."
362	    venue: "arXiv"
363	    year: 2026
364	    arxiv_id: "2603.01940"
365	    category: background
366	    role: background
367	    relevance_note: >
368	      [NEW-0516] Task constraints guide trajectory generation and serve as deterministic verifiers.
369	      Different: CoVe uses verification for data synthesis; B-IAVR learns when to verify at inference.
370	
371	  # ============================================================
372	  # Direction 3: Selective Verification / Adaptive Computation
373	  # ============================================================
374	
375	  - id: wan2025derailer-rerailer
376	    title: "Derailer-Rerailer: Adaptive Verification for Efficient and Reliable LM Reasoning"
377	    authors: "Wan et al."
378	    venue: "ACL 2025 Findings"
379	    year: 2025
380	    arxiv_id: "2408.13940"
381	    category: direct-competitor
382	    role: competitor
383	    relevance_note: >
384	      Most directly related competitor. Both do selective verification with binary trigger.
385	      Key difference: operates on reasoning chains (single-turn); B-IAVR on agent trajectories (multi-turn).
386	      Uses heuristic instability signal; B-IAVR uses RL-trained action-change signal.
387	      8-11% accuracy gain, 2-3x efficiency over uniform verification.
388	
389	  - id: sherlock2025
390	    title: "Sherlock: Reliable and Efficient Agentic Workflow Execution"
391	    authors: "Microsoft"
392	    venue: "arXiv"
393	    year: 2025
394	    arxiv_id: "2511.00330"
395	    category: direct-competitor
396	    role: competitor
397	    relevance_note: >
398	      Selective verification for agentic workflows via offline counterfactual analysis + speculative execution.
399	      Different scope: workflow DAG level (offline); B-IAVR is step-level (online RL).
400	      18.3% accuracy gain, 26% cost reduction, 48.7% latency reduction.
401	
402	  - id: singhi2025when-to-verify
403	    title: "When To Solve, When To Verify: Compute-Optimal Verification for LLM Reasoning"
404	    authors: "Singhi et al."
405	    venue: "arXiv"
406	    year: 2025
407	    arxiv_id: "2504.01005"
408	    category: background
409	    role: background
410	    relevance_note: >
411	      Derives inference scaling laws for solve-vs-verify tradeoff.
412	      Finding that over-verification is suboptimal directly supports B-IAVR's selective approach.
413	      B-IAVR learns this allocation via RL rather than analytically.
414	
415	  - id: yang2026ares
416	    title: "ARES: Adaptive Reasoning Effort Selection for Efficient LLM Agents"
417	    authors: "Yang et al."
418	    venue: "arXiv"
419	    year: 2026
420	    arxiv_id: "2603.07915"
421	    category: direct-competitor
422	    role: competitor
423	    relevance_note: >
424	      Closest competitor in agent domain. Both train learned per-step compute allocation.
425	      ARES uses SFT-initialized router further refined via GRPO with outcome + token efficiency reward;
426	      B-IAVR trains binary verify/not-verify via RL with action-change signal.
427	      Key differences: (1) reward signal — ARES optimizes token efficiency, B-IAVR uses action-change
428	      as verification trigger; (2) data requirement — ARES needs difficulty-annotated training data
429	      to bootstrap the router, B-IAVR learns from environment interaction alone.
430	      Reduces reasoning tokens by up to 52.7%.
431	
432	  - id: tu2025autothink
433	    title: "Learning When to Think: Shaping Adaptive Reasoning in R1-Style Models via Multi-Stage RL"
434	    authors: "Tu et al."
435	    venue: "NeurIPS 2025"
436	    year: 2025
437	    arxiv_id: "2505.10832"
438	    category: direct-competitor
439	    role: competitor
440	    relevance_note: >
441	      Analogous idea in reasoning domain: RL-trained adaptive computation trigger.
442	      Operates on single-turn reasoning; B-IAVR on multi-turn agent trajectories.
443	      +6.4% accuracy, -52% tokens on DeepSeek-R1-Distill-Qwen-1.5B.
444	
445	  - id: du2025thinkless
446	    title: "Thinkless: LLM Learns When to Think"
447	    authors: "Fang et al."
448	    venue: "NeurIPS 2025"
449	    year: 2025
450	    arxiv_id: "2505.13379"
451	    category: direct-competitor
452	    role: competitor
453	    relevance_note: >
454	      RL-trained control token to decide when to invoke extended thinking.
455	      Methodologically closest to B-IAVR in reasoning domain; B-IAVR applies to interactive agent trajectories.
456	
457	  - id: wang2025efficient-agents
458	    title: "Efficient Agents: Building Effective Agents While Reducing Cost"
459	    authors: "Wang et al."
460	    venue: "arXiv"
461	    year: 2025
462	    arxiv_id: "2508.02694"
463	    category: background
464	    role: background
465	    relevance_note: >
466	      First systematic study of agent efficiency-effectiveness tradeoff.
467	      Framework-level cost reduction; B-IAVR addresses cost at verification-policy level.
468	      Retains 96.7% performance with 28.4% cost-of-pass improvement.
469	
470	  - id: venktesh2025trust-but-verify
471	    title: "Trust but Verify! A Survey on Verification Design for Test-time Scaling"
472	    authors: "Venktesh et al."
473	    venue: "arXiv"
474	    year: 2025
475	    arxiv_id: "2508.16665"
476	    category: background
477	    role: background
478	    relevance_note: >
479	      Survey of verification approaches for test-time compute scaling.
480	      Identifies verification timing as key open problem. B-IAVR provides concrete solution for agent setting.
481	
482	  - id: agent-omit2026
483	    title: "Agent-Omit: Training Efficient LLM Agents for Adaptive Thought and Observation Omission via Agentic RL"
484	    authors: "Ning et al."
485	    venue: "ICML 2026"
486	    year: 2026
487	    arxiv_id: "2602.04284"
488	    category: direct-competitor
489	    role: competitor
490	    relevance_note: >
491	      RL-trained policy for adaptive omission of redundant thoughts and observations.
492	      Agent-Omit-8B matches frontier agents with best efficiency tradeoff on 5 benchmarks.
493	      Both use RL to learn cost-efficient agent behavior. Key difference: Agent-Omit subtracts
494	      (omits unnecessary context); B-IAVR selectively adds (verification steps).
495	      Opposite but complementary approaches to cost-efficiency. Potentially combinable.
496	
497	  - id: ava2026
498	    title: "Anytime Verified Agents: Adaptive Compute Allocation for Reliable LLM Reasoning under Budget Constraints"
499	    authors: "Patel"
500	    venue: "TMLR 2026"
501	    year: 2026
502	    arxiv_id: null  # no arXiv preprint; OpenReview ID: JMDCMf7mlF
503	    category: direct-competitor
504	    role: competitor
505	    relevance_note: >
506	      Dynamic compute allocation across search, sampling, and verification under budget.
507	      Uses calibrated uncertainty + value-of-information for selective verification cascades.
508	      Evaluated on GSM8K/MATH/HotpotQA/HumanEval (reasoning), not interactive agents.
509	      Key difference: analytical/heuristic allocation vs B-IAVR's RL-learned policy;
510	      single-turn reasoning vs multi-turn agent trajectories.
511	
512	  - id: cast2026
513	    title: "CAST: Case-Based Calibration of Adaptive Reasoning and Execution for LLM Tool Use"
514	    authors: "Pang et al."
515	    venue: "arXiv"
516	    year: 2026
517	    arxiv_id: "2605.15041"
518	    category: background
519	    role: background
520	    relevance_note: >
521	      Historical execution cases calibrate reasoning depth for tool use.
522	      Reduces reasoning length 26% with +5.85% accuracy on BFCLv2/ToolBench.
523	      Related: adaptive reasoning depth; different: case-based calibration vs RL-learned policy.
524	
525	  - id: marginal-token-allocators2026
526	    title: "Agentic AI Systems Should Be Designed as Marginal Token Allocators"
527	    authors: "Zhu"
528	    venue: "arXiv"
529	    year: 2026
530	    arxiv_id: "2605.01214"
531	    category: background
532	    role: background
533	    relevance_note: >
534	      Position paper framing agent cost-efficiency as marginal token allocation economics.
535	      Identifies under-verification as systematic failure mode. Supports B-IAVR's framing
536	      that verification decisions should reflect marginal cost-benefit analysis.
537	
538	  - id: argos2025
539	    title: "Argos: Multimodal RL with Adaptive Verifier for AI Agents"
540	    authors: "Tan et al."
541	    venue: "arXiv (revised April 2026)"
542	    year: 2025
543	    arxiv_id: "2512.03438"
544	    category: background
545	    role: background
546	    relevance_note: >
547	      Agentic verifier that adaptively selects scoring functions for multimodal RL training.
548	      Different domain (multimodal/robotics). The adaptive verifier selection concept is
549	      complementary: Argos adapts how to verify; B-IAVR adapts when to verify.
550	
551	  # ============================================================
552	  # Direction 4: ALFWorld / Interactive Environment Benchmarks
553	  # ============================================================
554	
555	  - id: kim2025reflact
556	    title: "ReflAct: World-Grounded Decision Making in LLM Agents via Goal-State Reflection"
557	    authors: "Kim et al."
558	    venue: "EMNLP 2025"
559	    year: 2025
560	    arxiv_id: "2505.15182"
561	    category: evaluation
562	    role: baseline
563	    relevance_note: >
564	      Prompting SOTA on ALFWorld at 93.3%. Replaces ReAct's next-action thinking with state-goal reflection.
565	      B-IAVR addresses different axis (cost-efficiency) since ALFWorld accuracy is near saturation.
566	
567	  - id: choudhury2025agentprm
568	    title: "Process Reward Models for LLM Agents: Practical Framework and Directions"
569	    authors: "Choudhury"
570	    venue: "arXiv"
571	    year: 2025
572	    arxiv_id: "2502.10325"
573	    category: evaluation
574	    role: baseline
575	    relevance_note: >
576	      Monte Carlo rollout-based process reward for agent training. 3B models achieve 91% on ALFWorld.
577	      Validates RL training approach; AgentPRM could serve as reward model for B-IAVR.
578	
579	  - id: xi2025agentprm
580	    title: "AgentPRM: Process Reward Models for LLM Agents via Step-Wise Promise and Progress"
581	    authors: "Xi et al."
582	    venue: "ACM Web Conference 2026"
583	    year: 2025
584	    arxiv_id: "2511.08325"
585	    category: evaluation
586	    role: baseline
587	    relevance_note: >
588	      Independent work from Choudhury et al., using TD-based estimation with GAE for scalable
589	      PRM data labeling. 8x more compute-efficient than baselines with robust test-time scaling.
590	      Different approach: Choudhury uses MC rollouts; Xi uses TD+GAE for step-wise promise and progress.
591	
592	  - id: xiang2024retrospex
593	    title: "Retrospex: Language Agent Meets Offline RL Critic"
594	    authors: "Xiang et al."
595	    venue: "EMNLP 2024"
596	    year: 2024
597	    arxiv_id: "2505.11807"
598	    category: background
599	    role: background
600	    relevance_note: >
601	      Offline RL Critic augments LLM agent action selection via dynamic rescoring.
602	      Similar architecture could inform B-IAVR's verification value estimation.
603	
604	  - id: cfgm2025
605	    title: "CFGM: Coarse-to-Fine Grounded Memory for LLM Agent Planning"
606	    authors: "Yang et al."
607	    venue: "EMNLP 2025"
608	    year: 2025
609	    arxiv_id: "2508.15305"
610	    category: background
611	    role: background
612	    relevance_note: >
613	      Memory-augmented agent planning with episodic grounding.
614	      ALFWorld +10.40%, WebShop +20%. Complementary to B-IAVR's verification approach.
615	
616	  - id: respact2024
617	    title: "ReSpAct: Harmonizing Reasoning, Speaking, and Acting"
618	    authors: "Dongre et al."
619	    venue: "arXiv"
620	    year: 2024
621	    arxiv_id: "2411.00927"
622	    category: evaluation
623	    role: baseline
624	    relevance_note: >
625	      Integrates dialogue/reasoning/acting. +6% over ReAct on ALFWorld.
626	      Reduces invalid actions from 13% to 3%; B-IAVR's verification achieves error prevention differently.
627	
628	  # ============================================================
629	  # Direction 5: Multi-Turn Credit Assignment (Direct Competitors)
630	  # ============================================================
631	
632	  - id: turn-ppo2025
633	    title: "Turn-PPO: Turn-Level Advantage Estimation with PPO for Improved Multi-Turn RL in Agentic LLMs"
634	    authors: "Li et al."
635	    venue: "arXiv"
636	    year: 2025
637	    arxiv_id: "2512.17008"
638	    category: direct-competitor
639	    role: competitor
640	    relevance_note: >
641	      [NEW-0517] Most direct competitor. Identifies "uniform advantage" problem in
642	      step-independent GRPO (subset of our "sign misattribution"). Proposes turn-level
643	      MDP + learned value function. Our differences: (1) more precise formalization
644	      (sign misattribution + gamma decay quantification), (2) contrarian solution
645	      (episode-level coarser credit vs their finer turn-level credit).
646	
647	  - id: gagpo2026
648	    title: "GAGPO: Generalized Advantage Grouped Policy Optimization"
649	    authors: "Zhu et al."
650	    venue: "arXiv"
651	    year: 2026
652	    arxiv_id: "2605.13217"
653	    category: direct-competitor
654	    role: competitor
655	    relevance_note: >
656	      [NEW-0517] Critic-free step-aligned credit via non-parametric grouped value proxy +
657	      TD/GAE-style temporal advantages. ALFWorld 93.5% (1.5B), 95.6% (7B).
658	      Pursues finer-grained credit to improve performance; our work diagnoses why
659	      step-independent fails (sign misattribution) and shows coarser episode-level suffices.
660	      Different contribution axis: performance optimization vs mechanism diagnosis.
661	
662	  - id: mt-grpo2025
663	    title: "Reinforcing Multi-Turn Reasoning in LLM Agents via Turn-Level Reward Design"
664	    authors: "Wei et al."
665	    venue: "arXiv"
666	    year: 2025
667	    arxiv_id: "2505.11821"
668	    category: direct-competitor
669	    role: competitor
670	    relevance_note: >
671	      [NEW-0517] Proposes MT-GRPO with turn-level reward design for multi-turn RL.
672	      Evaluated on QA search tasks (NQ, TriviaQA, HotpotQA), not ALFWorld.
673	      Qwen2.5-7B. Same direction as Turn-PPO (finer turn-level credit);
674	      our contrarian shows coarser episode-level eliminates sign misattribution.
675	
676	  - id: istar2025
677	    title: "Agentic Reinforcement Learning with Implicit Step Rewards"
678	    authors: "Liu et al."
679	    venue: "ICLR 2026"
680	    year: 2025
681	    arxiv_id: "2509.19199"
682	    category: direct-competitor
683	    role: competitor
684	    relevance_note: >
685	      [NEW-0517] Implicit PRM + dual advantage (step + episode level) for agentic RL.
686	      WebShop 86.5%, VisualSokoban 91.7%. ICLR 2026 published.
687	      Learns step-level credit via implicit rewards without explicit labels;
688	      our work shows episode-level alone suffices when sign misattribution is the bottleneck.
689	      Validates that step-level credit helps, but doesn't diagnose when it hurts.
690	
691	  - id: archer2024
692	    title: "ArCHer: Training Language Model Agents via Hierarchical Multi-Turn RL"
693	    authors: "Zhou, Zanette, Pan, Levine, Kumar"
694	    venue: "ICML 2024"
695	    year: 2024
696	    arxiv_id: "2402.19446"
697	    category: method-component
698	    role: predecessor
699	    relevance_note: >
700	      [NEW-0517] Foundational hierarchical multi-turn RL framework (ICML 2024).
701	      High-level off-policy value RL (utterance-level) + low-level token policy.
702	      ~100x sample efficiency. Establishes that multi-turn RL needs hierarchical structure;
703	      our work specifically diagnoses why flat step-independent approaches fail.
704	
705	  - id: ca-survey2026
706	    title: "From Reasoning to Agentic: Credit Assignment in Reinforcement Learning for Large Language Models"
707	    authors: "Zhang"
708	    venue: "arXiv"
709	    year: 2026
710	    arxiv_id: "2604.09459"
711	    category: background
712	    role: background
713	    relevance_note: >
714	      [NEW-0517] Comprehensive survey of 47 CA methods (2024-2026). Two-dimensional
715	      taxonomy: granularity (token/segment/step/turn/multi-agent) x methodology
716	      (MC/TD/model-based/game-theoretic/information-theoretic). Contextualizes our
717	      sign misattribution diagnosis within the broader CA landscape.
718	
719	  - id: hiper2026
720	    title: "HiPER: Hierarchical Reinforcement Learning with Explicit Credit Assignment for Large Language Model Agents"
721	    authors: "Peng et al."
722	    venue: "arXiv"
723	    year: 2026
724	    arxiv_id: "2602.16165"
725	    category: method-component
726	    role: background
727	    relevance_note: >
728	      [NEW-0517] Hierarchical Plan-Execute RL. ALFWorld 97.4% (7B), 95.3% (1.5B).
729	      GRPO baseline: 71.1% (1.5B), 85.4% (7B). 2.8x training efficiency gain.
730	      Pursues SOTA performance via hierarchical plan-execute architecture;
731	      our work does mechanism diagnosis of why step-independent GRPO fails.
732	      Different contribution dimension: not comparable on performance axis.
733	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cce95bc1-b851-4a1e-aa34-da0f26f68eac",
  "isSidechain": false,
  "promptId": "71e953e0-39de-4d6a-a9b9-c8a649da7bce",
  "type": "user",
  "uuid": "5f5fa9f7-dcb7-44ce-b881-d79e91eea8b6",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/literature_map.yaml",
      "content": "# B-IAVR Literature Map\n# Updated: 2026-05-17\n# Categories: direct-competitor, method-component, background, evaluation\n# Roles: predecessor, competitor, baseline, evaluation, background\n\npapers:\n\n  # ============================================================\n  # Direction 1: Self-Verification / Self-Correction in LLM Agents\n  # ============================================================\n\n  - id: kamoi2024self-correction-survey\n    title: \"When Can LLMs Actually Correct Their Own Mistakes? A Critical Survey of Self-Correction of LLMs\"\n    authors: \"Kamoi et al.\"\n    venue: \"arXiv\"\n    year: 2024\n    arxiv_id: \"2406.01297\"\n    category: background\n    role: background\n    relevance_note: >\n      Foundational survey establishing that pure intrinsic self-correction is unreliable.\n      Validates B-IAVR's use of grounded verification (environment re-observation) over prompted self-feedback.\n\n  - id: tie2025correctbench\n    title: \"Can LLMs Correct Themselves? A Benchmark of Self-Correction in LLMs\"\n    authors: \"Tie et al.\"\n    venue: \"NeurIPS 2025 Datasets & Benchmarks\"\n    year: 2025\n    arxiv_id: \"2510.16062\"\n    category: background\n    role: background\n    relevance_note: >\n      Benchmark showing self-correction has diminishing returns when applied uniformly.\n      Supports B-IAVR's selective verification design over blanket correction.\n\n  - id: self-verification-dilemma-2026\n    title: \"Self-Verification Dilemma: Experience-Driven Suppression of Overused Checking in LLM Reasoning\"\n    authors: \"Long et al.\"\n    venue: \"arXiv\"\n    year: 2026\n    arxiv_id: \"2602.03485\"\n    category: background\n    role: background\n    relevance_note: >\n      Empirically validates that >90% of self-verification is confirmatory, ~2% corrective.\n      Directly supports B-IAVR's core thesis that verification should be selective.\n      Their experience-pool approach is complementary to B-IAVR's action-change signal.\n\n  - id: zhang2025incentivize-self-verify\n    title: \"Incentivizing LLMs to Self-Verify Their Answers\"\n    authors: \"Zhang et al.\"\n    venue: \"arXiv\"\n    year: 2025\n    arxiv_id: \"2506.01369\"\n    category: background\n    role: background\n    relevance_note: >\n      Unifies answer generation and verification via single RL training process.\n      Parallel to B-IAVR: they train verification into generation; B-IAVR trains when to trigger separate verification.\n\n  - id: mar2025\n    title: \"MAR: Multi-Agent Reflexion Improves Reasoning Abilities in LLMs\"\n    authors: \"Ozer et al.\"\n    venue: \"arXiv\"\n    year: 2025\n    arxiv_id: \"2512.20845\"\n    category: background\n    role: background\n    relevance_note: >\n      Multi-agent self-correction with diverse critic personas.\n      Complementary: MAR improves correction quality; B-IAVR decides when to trigger correction.\n\n  - id: ssr2025\n    title: \"SSR: Socratic Self-Refine for Large Language Model Reasoning\"\n    authors: \"Shi et al.\"\n    venue: \"arXiv\"\n    year: 2025\n    arxiv_id: \"2511.10621\"\n    category: background\n    role: background\n    relevance_note: >\n      Structured Socratic questioning for self-refinement.\n      Complementary: improves correction step quality; B-IAVR focuses on when to invoke correction.\n\n  - id: verifiagent2025\n    title: \"VerifiAgent: a Unified Verification Agent in Language Model Reasoning\"\n    authors: \"Han et al.\"\n    venue: \"EMNLP 2025 Findings\"\n    year: 2025\n    arxiv_id: \"2504.00406\"\n    category: background\n    role: background\n    relevance_note: >\n      Unified verification agent with meta-verification + tool-based adaptive verification.\n      Focuses on how to verify (tool selection); B-IAVR focuses on when to verify (policy learning).\n      Complementary: VerifiAgent's verification quality could enhance B-IAVR's verification step.\n\n  # ============================================================\n  # Direction 2: Agent RL Training\n  # ============================================================\n\n  - id: feng2025gigpo\n    title: \"GiGPO: Group-in-Group Policy Optimization for LLM Agent Training\"\n    authors: \"Feng et al.\"\n    venue: \"NeurIPS 2025\"\n    year: 2025\n    arxiv_id: \"2505.10978\"\n    category: method-component\n    role: predecessor\n    relevance_note: >\n      Core training algorithm for B-IAVR. Nested group structure provides step-level credit\n      assignment without learned critic. >12% over GRPO on ALFWorld, >9% on WebShop.\n\n  - id: selfguide2026\n    title: \"Co-Evolution of Policy and Internal Reward for Language Agents (Self-Guide)\"\n    authors: \"Wang et al.\"\n    venue: \"arXiv\"\n    year: 2026\n    arxiv_id: \"2604.03098\"\n    category: method-component\n    role: predecessor\n    relevance_note: >\n      Direct predecessor. B-IAVR extends Self-Guide's co-evolving internal reward.\n      The self-guidance signal is the foundation for action-change detection triggering verification.\n      8% improvement over env-reward-only on ALFWorld with Qwen3-1.7B/4B.\n\n  - id: spear2025\n    title: \"Learn the Ropes, Then Trust the Wins: Self-imitation with Progressive Exploration for Agentic Reinforcement Learning\"\n    authors: \"Qin et al.\"\n    venue: \"ICLR 2026\"\n    year: 2025\n    arxiv_id: \"2509.22601\"\n    category: method-component\n    role: background\n    relevance_note: >\n      Curriculum-based self-imitation for sparse-reward agent tasks.\n      Up to +16.1% on ALFWorld over GRPO. Self-imitation curriculum could augment B-IAVR training.\n\n  - id: wei2025webagent-r1\n    title: \"WebAgent-R1: Training Web Agents via End-to-End Multi-Turn RL\"\n    authors: \"Wei et al.\"\n    venue: \"EMNLP 2025\"\n    year: 2025\n    arxiv_id: \"2505.16421\"\n    category: background\n    role: background\n    relevance_note: >\n      Extends GRPO to multi-turn (M-GRPO) with dynamic context compression.\n      Qwen-2.5-3B: 6.1% to 33.9% on WebArena-Lite. M-GRPO multi-turn extension relevant to B-IAVR.\n\n  - id: dapo2025\n    title: \"DAPO: An Open-Source LLM Reinforcement Learning System at Scale\"\n    authors: \"Yu et al.\"\n    venue: \"arXiv\"\n    year: 2025\n    arxiv_id: \"2503.14476\"\n    category: method-component\n    role: background\n    relevance_note: >\n      RL training stabilization techniques (Clip-Higher, Dynamic Sampling).\n      Applicable to B-IAVR's RL training to prevent entropy collapse.\n\n  - id: digiRL2024\n    title: \"DigiRL: Training In-The-Wild Device-Control Agents with Autonomous RL\"\n    authors: \"Bai et al.\"\n    venue: \"NeurIPS 2024\"\n    year: 2024\n    arxiv_id: \"2406.11896\"\n    category: background\n    role: background\n    relevance_note: >\n      Online RL for device control agents. Demonstrates online RL viability for interactive agents.\n      49.5% absolute improvement over SFT. Parallel approach to B-IAVR in text-based setting.\n\n  - id: li2025sorl\n    title: \"SORL: Stabilizing Off-Policy RL for Long-Horizon Agent Training\"\n    authors: \"Li et al.\"\n    venue: \"arXiv\"\n    year: 2025\n    arxiv_id: \"2511.20718\"\n    category: method-component\n    role: background\n    relevance_note: >\n      Turn-level importance sampling + clipping-triggered normalization for stable multi-turn agent RL.\n      Directly applicable to B-IAVR's multi-turn ALFWorld training stability.\n\n  - id: agentic-rl-survey-2025\n    title: \"The Landscape of Agentic Reinforcement Learning for LLMs: A Survey\"\n    authors: \"Zhang et al.\"\n    venue: \"TMLR 2026\"\n    year: 2025\n    arxiv_id: \"2509.02547\"\n    category: background\n    role: background\n    relevance_note: >\n      Comprehensive survey formalizing agentic RL. Contextualizes B-IAVR as training agents\n      to make meta-decisions (when to verify) via RL within the POMDP framework.\n\n  - id: skillmaster2026\n    title: \"SkillMaster: Toward Autonomous Skill Mastery in LLM Agents\"\n    authors: \"Yang et al.\"\n    venue: \"arXiv\"\n    year: 2026\n    arxiv_id: \"2605.08693\"\n    category: method-component\n    role: background\n    relevance_note: >\n      DualAdv-GRPO: separately estimates advantages for task-solving and skill-editing decisions.\n      +8.8% on ALFWorld, +9.3% on WebShop. DualAdv structure could inform B-IAVR's\n      separation of action and verification advantages.\n\n  - id: t2po2026\n    title: \"T2PO: Uncertainty-Guided Exploration Control for Stable Multi-Turn Agentic RL\"\n    authors: \"Wang et al.\"\n    venue: \"ICML 2026 Spotlight\"\n    year: 2026\n    arxiv_id: \"2605.02178\"\n    category: method-component\n    role: background\n    relevance_note: >\n      Token- and turn-level uncertainty monitoring for stable multi-turn agent RL.\n      Triggers thinking intervention when marginal uncertainty change drops below threshold.\n      Evaluated on ALFWorld and WebShop. Conceptually related: uncertainty-based trigger vs\n      B-IAVR's action-change trigger, but T2PO targets training stability, not deployment verification.\n\n  - id: gvpo2026\n    title: \"GVPO: Group Verification-based Policy Optimization for Interactive Coding Agents\"\n    authors: \"Dai et al.\"\n    venue: \"ICLR 2026\"\n    year: 2026\n    arxiv_id: null  # no arXiv preprint; OpenReview ID: RY47Tq0VsV\n    category: method-component\n    role: background\n    relevance_note: >\n      Advantage shaping with outcome-verifiable + process-verifiable signals.\n      +12.7% over o1 on AppWorld. Integrates intermediate execution feedback as step-level\n      verification signals. Different focus: uses verification for credit assignment during\n      training; B-IAVR learns when to invoke verification at deployment.\n\n  - id: agentv-rl2026\n    title: \"AgentV-RL: Scaling Reward Modeling with Agentic Verifier\"\n    authors: \"Zhang et al.\"\n    venue: \"arXiv\"\n    year: 2026\n    arxiv_id: \"2604.16004\"\n    category: method-component\n    role: background\n    relevance_note: >\n      Bidirectional forward/backward agentic verifier for reward modeling in RL.\n      4B model surpasses SOTA ORMs by 25.2%. Addresses verification quality in reward modeling;\n      B-IAVR addresses verification timing in agent deployment. Complementary.\n\n  - id: pa-moe2026\n    title: \"PA-MoE: Phase-Aware Mixture of Experts for Agentic Reinforcement Learning\"\n    authors: \"Li et al.\"\n    venue: \"arXiv\"\n    year: 2026\n    arxiv_id: \"2602.17038\"\n    category: evaluation\n    role: baseline\n    relevance_note: >\n      [NEW-0516] Lightweight phase router learns latent phase boundaries from RL objective.\n      PA-MoE+GiGPO with Qwen2.5-1.5B achieves 93.8% on ALFWorld (+7.7 over GiGPO 86.1%).\n      1.5B outperforms vanilla 7B GiGPO (90.2%). New small-model SOTA on ALFWorld.\n      Orthogonal architecture innovation; important baseline to cite.\n\n  - id: sdar2026\n    title: \"SDAR: Self-Distilled Agentic Reinforcement Learning\"\n    authors: \"Lu et al.\"\n    venue: \"arXiv\"\n    year: 2026\n    arxiv_id: \"2605.15155\"\n    category: method-component\n    role: background\n    relevance_note: >\n      [NEW-0516] On-policy self-distillation as gated auxiliary objective during RL training.\n      Token-level gate decides supervision intensity. +9.4% over GRPO on ALFWorld.\n      Complementary: SDAR improves RL training; B-IAVR learns verification policy.\n\n  - id: hcapo2026\n    title: \"HCAPO: Hindsight Credit Assignment for Long-Horizon LLM Agents\"\n    authors: \"Tan et al.\"\n    venue: \"arXiv\"\n    year: 2026\n    arxiv_id: \"2603.08754\"\n    category: method-component\n    role: background\n    relevance_note: >\n      [NEW-0516] LLM-as-critic refines step-level Q-values via hindsight reasoning +\n      multi-scale advantage for critical decision states.\n      +13.8% on ALFWorld, +7.7% on WebShop over GRPO (Qwen2.5-7B).\n      Could improve B-IAVR's reward signal for verification decision steps.\n\n  - id: act2026\n    title: \"ACT: Agentic Critical Training\"\n    authors: \"Liu et al.\"\n    venue: \"arXiv\"\n    year: 2026\n    arxiv_id: \"2603.08706\"\n    category: method-component\n    role: background\n    relevance_note: >\n      [NEW-0516] Trains agents to judge action quality via critical comparison reward.\n      +5.07 over IL, +4.62 over RL. Different axis: ACT improves reflection quality;\n      B-IAVR decides when to reflect.\n\n  - id: rwml2026\n    title: \"RWML: Reinforcement World Model Learning for LLM-based Agents\"\n    authors: \"Yu et al.\"\n    venue: \"arXiv\"\n    year: 2026\n    arxiv_id: \"2602.05842\"\n    category: method-component\n    role: background\n    relevance_note: >\n      [NEW-0516] Self-supervised world model via sim-to-real gap rewards in embedding space.\n      +6.9 on ALFWorld over task-success-only RL. Matches expert-data training.\n      Orthogonal: improves internal world model; B-IAVR adds selective verification.\n\n  - id: skill0-2026\n    title: \"SKILL0: In-Context Agentic Reinforcement Learning for Skill Internalization\"\n    authors: \"Lu et al.\"\n    venue: \"arXiv\"\n    year: 2026\n    arxiv_id: \"2604.02268\"\n    category: method-component\n    role: background\n    relevance_note: >\n      [NEW-0516] Training-time curriculum progressively withdraws skill context until zero-shot.\n      +9.7% on ALFWorld over GRPO, <0.5k tokens per step.\n      Complementary: SKILL0 internalizes skills; B-IAVR adds selective verification.\n\n  - id: fission-grpo2026\n    title: \"Fission-GRPO: Robust Tool Use via Learning to Recover from Execution Errors\"\n    authors: \"Zhang et al.\"\n    venue: \"arXiv\"\n    year: 2026\n    arxiv_id: \"2601.15625\"\n    category: method-component\n    role: background\n    relevance_note: >\n      [NEW-0516] Fissions failed trajectories into recovery training instances.\n      +4% overall accuracy on BFCL v4 Multi-Turn over GRPO.\n      Related: error recovery after failure vs B-IAVR's proactive verification.\n\n  - id: selfbudgeter2026\n    title: \"SelfBudgeter: Adaptive Token Allocation for Efficient LLM Reasoning\"\n    authors: \"Li et al.\"\n    venue: \"ICLR 2026 (under review)\"\n    year: 2025\n    arxiv_id: \"2505.11274\"\n    category: background\n    role: background\n    relevance_note: >\n      [NEW-0516] Self-estimated token budgets + budget-guided GRPO. 61% token reduction.\n      Parallel concept: SelfBudgeter allocates computation budget;\n      B-IAVR makes binary verify/not-verify decision. Both use RL for adaptive compute.\n\n  - id: cove2026\n    title: \"CoVe: Training Interactive Tool-Use Agents via Constraint-Guided Verification\"\n    authors: \"Chen et al.\"\n    venue: \"arXiv\"\n    year: 2026\n    arxiv_id: \"2603.01940\"\n    category: background\n    role: background\n    relevance_note: >\n      [NEW-0516] Task constraints guide trajectory generation and serve as deterministic verifiers.\n      Different: CoVe uses verification for data synthesis; B-IAVR learns when to verify at inference.\n\n  # ============================================================\n  # Direction 3: Selective Verification / Adaptive Computation\n  # ============================================================\n\n  - id: wan2025derailer-rerailer\n    title: \"Derailer-Rerailer: Adaptive Verification for Efficient and Reliable LM Reasoning\"\n    authors: \"Wan et al.\"\n    venue: \"ACL 2025 Findings\"\n    year: 2025\n    arxiv_id: \"2408.13940\"\n    category: direct-competitor\n    role: competitor\n    relevance_note: >\n      Most directly related competitor. Both do selective verification with binary trigger.\n      Key difference: operates on reasoning chains (single-turn); B-IAVR on agent trajectories (multi-turn).\n      Uses heuristic instability signal; B-IAVR uses RL-trained action-change signal.\n      8-11% accuracy gain, 2-3x efficiency over uniform verification.\n\n  - id: sherlock2025\n    title: \"Sherlock: Reliable and Efficient Agentic Workflow Execution\"\n    authors: \"Microsoft\"\n    venue: \"arXiv\"\n    year: 2025\n    arxiv_id: \"2511.00330\"\n    category: direct-competitor\n    role: competitor\n    relevance_note: >\n      Selective verification for agentic workflows via offline counterfactual analysis + speculative execution.\n      Different scope: workflow DAG level (offline); B-IAVR is step-level (online RL).\n      18.3% accuracy gain, 26% cost reduction, 48.7% latency reduction.\n\n  - id: singhi2025when-to-verify\n    title: \"When To Solve, When To Verify: Compute-Optimal Verification for LLM Reasoning\"\n    authors: \"Singhi et al.\"\n    venue: \"arXiv\"\n    year: 2025\n    arxiv_id: \"2504.01005\"\n    category: background\n    role: background\n    relevance_note: >\n      Derives inference scaling laws for solve-vs-verify tradeoff.\n      Finding that over-verification is suboptimal directly supports B-IAVR's selective approach.\n      B-IAVR learns this allocation via RL rather than analytically.\n\n  - id: yang2026ares\n    title: \"ARES: Adaptive Reasoning Effort Selection for Efficient LLM Agents\"\n    authors: \"Yang et al.\"\n    venue: \"arXiv\"\n    year: 2026\n    arxiv_id: \"2603.07915\"\n    category: direct-competitor\n    role: competitor\n    relevance_note: >\n      Closest competitor in agent domain. Both train learned per-step compute allocation.\n      ARES uses SFT-initialized router further refined via GRPO with outcome + token efficiency reward;\n      B-IAVR trains binary verify/not-verify via RL with action-change signal.\n      Key differences: (1) reward signal — ARES optimizes token efficiency, B-IAVR uses action-change\n      as verification trigger; (2) data requirement — ARES needs difficulty-annotated training data\n      to bootstrap the router, B-IAVR learns from environment interaction alone.\n      Reduces reasoning tokens by up to 52.7%.\n\n  - id: tu2025autothink\n    title: \"Learning When to Think: Shaping Adaptive Reasoning in R1-Style Models via Multi-Stage RL\"\n    authors: \"Tu et al.\"\n    venue: \"NeurIPS 2025\"\n    year: 2025\n    arxiv_id: \"2505.10832\"\n    category: direct-competitor\n    role: competitor\n    relevance_note: >\n      Analogous idea in reasoning domain: RL-trained adaptive computation trigger.\n      Operates on single-turn reasoning; B-IAVR on multi-turn agent trajectories.\n      +6.4% accuracy, -52% tokens on DeepSeek-R1-Distill-Qwen-1.5B.\n\n  - id: du2025thinkless\n    title: \"Thinkless: LLM Learns When to Think\"\n    authors: \"Fang et al.\"\n    venue: \"NeurIPS 2025\"\n    year: 2025\n    arxiv_id: \"2505.13379\"\n    category: direct-competitor\n    role: competitor\n    relevance_note: >\n      RL-trained control token to decide when to invoke extended thinking.\n      Methodologically closest to B-IAVR in reasoning domain; B-IAVR applies to interactive agent trajectories.\n\n  - id: wang2025efficient-agents\n    title: \"Efficient Agents: Building Effective Agents While Reducing Cost\"\n    authors: \"Wang et al.\"\n    venue: \"arXiv\"\n    year: 2025\n    arxiv_id: \"2508.02694\"\n    category: background\n    role: background\n    relevance_note: >\n      First systematic study of agent efficiency-effectiveness tradeoff.\n      Framework-level cost reduction; B-IAVR addresses cost at verification-policy level.\n      Retains 96.7% performance with 28.4% cost-of-pass improvement.\n\n  - id: venktesh2025trust-but-verify\n    title: \"Trust but Verify! A Survey on Verification Design for Test-time Scaling\"\n    authors: \"Venktesh et al.\"\n    venue: \"arXiv\"\n    year: 2025\n    arxiv_id: \"2508.16665\"\n    category: background\n    role: background\n    relevance_note: >\n      Survey of verification approaches for test-time compute scaling.\n      Identifies verification timing as key open problem. B-IAVR provides concrete solution for agent setting.\n\n  - id: agent-omit2026\n    title: \"Agent-Omit: Training Efficient LLM Agents for Adaptive Thought and Observation Omission via Agentic RL\"\n    authors: \"Ning et al.\"\n    venue: \"ICML 2026\"\n    year: 2026\n    arxiv_id: \"2602.04284\"\n    category: direct-competitor\n    role: competitor\n    relevance_note: >\n      RL-trained policy for adaptive omission of redundant thoughts and observations.\n      Agent-Omit-8B matches frontier agents with best efficiency tradeoff on 5 benchmarks.\n      Both use RL to learn cost-efficient agent behavior. Key difference: Agent-Omit subtracts\n      (omits unnecessary context); B-IAVR selectively adds (verification steps).\n      Opposite but complementary approaches to cost-efficiency. Potentially combinable.\n\n  - id: ava2026\n    title: \"Anytime Verified Agents: Adaptive Compute Allocation for Reliable LLM Reasoning under Budget Constraints\"\n    authors: \"Patel\"\n    venue: \"TMLR 2026\"\n    year: 2026\n    arxiv_id: null  # no arXiv preprint; OpenReview ID: JMDCMf7mlF\n    category: direct-competitor\n    role: competitor\n    relevance_note: >\n      Dynamic compute allocation across search, sampling, and verification under budget.\n      Uses calibrated uncertainty + value-of-information for selective verification cascades.\n      Evaluated on GSM8K/MATH/HotpotQA/HumanEval (reasoning), not interactive agents.\n      Key difference: analytical/heuristic allocation vs B-IAVR's RL-learned policy;\n      single-turn reasoning vs multi-turn agent trajectories.\n\n  - id: cast2026\n    title: \"CAST: Case-Based Calibration of Adaptive Reasoning and Execution for LLM Tool Use\"\n    authors: \"Pang et al.\"\n    venue: \"arXiv\"\n    year: 2026\n    arxiv_id: \"2605.15041\"\n    category: background\n    role: background\n    relevance_note: >\n      Historical execution cases calibrate reasoning depth for tool use.\n      Reduces reasoning length 26% with +5.85% accuracy on BFCLv2/ToolBench.\n      Related: adaptive reasoning depth; different: case-based calibration vs RL-learned policy.\n\n  - id: marginal-token-allocators2026\n    title: \"Agentic AI Systems Should Be Designed as Marginal Token Allocators\"\n    authors: \"Zhu\"\n    venue: \"arXiv\"\n    year: 2026\n    arxiv_id: \"2605.01214\"\n    category: background\n    role: background\n    relevance_note: >\n      Position paper framing agent cost-efficiency as marginal token allocation economics.\n      Identifies under-verification as systematic failure mode. Supports B-IAVR's framing\n      that verification decisions should reflect marginal cost-benefit analysis.\n\n  - id: argos2025\n    title: \"Argos: Multimodal RL with Adaptive Verifier for AI Agents\"\n    authors: \"Tan et al.\"\n    venue: \"arXiv (revised April 2026)\"\n    year: 2025\n    arxiv_id: \"2512.03438\"\n    category: background\n    role: background\n    relevance_note: >\n      Agentic verifier that adaptively selects scoring functions for multimodal RL training.\n      Different domain (multimodal/robotics). The adaptive verifier selection concept is\n      complementary: Argos adapts how to verify; B-IAVR adapts when to verify.\n\n  # ============================================================\n  # Direction 4: ALFWorld / Interactive Environment Benchmarks\n  # ============================================================\n\n  - id: kim2025reflact\n    title: \"ReflAct: World-Grounded Decision Making in LLM Agents via Goal-State Reflection\"\n    authors: \"Kim et al.\"\n    venue: \"EMNLP 2025\"\n    year: 2025\n    arxiv_id: \"2505.15182\"\n    category: evaluation\n    role: baseline\n    relevance_note: >\n      Prompting SOTA on ALFWorld at 93.3%. Replaces ReAct's next-action thinking with state-goal reflection.\n      B-IAVR addresses different axis (cost-efficiency) since ALFWorld accuracy is near saturation.\n\n  - id: choudhury2025agentprm\n    title: \"Process Reward Models for LLM Agents: Practical Framework and Directions\"\n    authors: \"Choudhury\"\n    venue: \"arXiv\"\n    year: 2025\n    arxiv_id: \"2502.10325\"\n    category: evaluation\n    role: baseline\n    relevance_note: >\n      Monte Carlo rollout-based process reward for agent training. 3B models achieve 91% on ALFWorld.\n      Validates RL training approach; AgentPRM could serve as reward model for B-IAVR.\n\n  - id: xi2025agentprm\n    title: \"AgentPRM: Process Reward Models for LLM Agents via Step-Wise Promise and Progress\"\n    authors: \"Xi et al.\"\n    venue: \"ACM Web Conference 2026\"\n    year: 2025\n    arxiv_id: \"2511.08325\"\n    category: evaluation\n    role: baseline\n    relevance_note: >\n      Independent work from Choudhury et al., using TD-based estimation with GAE for scalable\n      PRM data labeling. 8x more compute-efficient than baselines with robust test-time scaling.\n      Different approach: Choudhury uses MC rollouts; Xi uses TD+GAE for step-wise promise and progress.\n\n  - id: xiang2024retrospex\n    title: \"Retrospex: Language Agent Meets Offline RL Critic\"\n    authors: \"Xiang et al.\"\n    venue: \"EMNLP 2024\"\n    year: 2024\n    arxiv_id: \"2505.11807\"\n    category: background\n    role: background\n    relevance_note: >\n      Offline RL Critic augments LLM agent action selection via dynamic rescoring.\n      Similar architecture could inform B-IAVR's verification value estimation.\n\n  - id: cfgm2025\n    title: \"CFGM: Coarse-to-Fine Grounded Memory for LLM Agent Planning\"\n    authors: \"Yang et al.\"\n    venue: \"EMNLP 2025\"\n    year: 2025\n    arxiv_id: \"2508.15305\"\n    category: background\n    role: background\n    relevance_note: >\n      Memory-augmented agent planning with episodic grounding.\n      ALFWorld +10.40%, WebShop +20%. Complementary to B-IAVR's verification approach.\n\n  - id: respact2024\n    title: \"ReSpAct: Harmonizing Reasoning, Speaking, and Acting\"\n    authors: \"Dongre et al.\"\n    venue: \"arXiv\"\n    year: 2024\n    arxiv_id: \"2411.00927\"\n    category: evaluation\n    role: baseline\n    relevance_note: >\n      Integrates dialogue/reasoning/acting. +6% over ReAct on ALFWorld.\n      Reduces invalid actions from 13% to 3%; B-IAVR's verification achieves error prevention differently.\n\n  # ============================================================\n  # Direction 5: Multi-Turn Credit Assignment (Direct Competitors)\n  # ============================================================\n\n  - id: turn-ppo2025\n    title: \"Turn-PPO: Turn-Level Advantage Estimation with PPO for Improved Multi-Turn RL in Agentic LLMs\"\n    authors: \"Li et al.\"\n    venue: \"arXiv\"\n    year: 2025\n    arxiv_id: \"2512.17008\"\n    category: direct-competitor\n    role: competitor\n    relevance_note: >\n      [NEW-0517] Most direct competitor. Identifies \"uniform advantage\" problem in\n      step-independent GRPO (subset of our \"sign misattribution\"). Proposes turn-level\n      MDP + learned value function. Our differences: (1) more precise formalization\n      (sign misattribution + gamma decay quantification), (2) contrarian solution\n      (episode-level coarser credit vs their finer turn-level credit).\n\n  - id: gagpo2026\n    title: \"GAGPO: Generalized Advantage Grouped Policy Optimization\"\n    authors: \"Zhu et al.\"\n    venue: \"arXiv\"\n    year: 2026\n    arxiv_id: \"2605.13217\"\n    category: direct-competitor\n    role: competitor\n    relevance_note: >\n      [NEW-0517] Critic-free step-aligned credit via non-parametric grouped value proxy +\n      TD/GAE-style temporal advantages. ALFWorld 93.5% (1.5B), 95.6% (7B).\n      Pursues finer-grained credit to improve performance; our work diagnoses why\n      step-independent fails (sign misattribution) and shows coarser episode-level suffices.\n      Different contribution axis: performance optimization vs mechanism diagnosis.\n\n  - id: mt-grpo2025\n    title: \"Reinforcing Multi-Turn Reasoning in LLM Agents via Turn-Level Reward Design\"\n    authors: \"Wei et al.\"\n    venue: \"arXiv\"\n    year: 2025\n    arxiv_id: \"2505.11821\"\n    category: direct-competitor\n    role: competitor\n    relevance_note: >\n      [NEW-0517] Proposes MT-GRPO with turn-level reward design for multi-turn RL.\n      Evaluated on QA search tasks (NQ, TriviaQA, HotpotQA), not ALFWorld.\n      Qwen2.5-7B. Same direction as Turn-PPO (finer turn-level credit);\n      our contrarian shows coarser episode-level eliminates sign misattribution.\n\n  - id: istar2025\n    title: \"Agentic Reinforcement Learning with Implicit Step Rewards\"\n    authors: \"Liu et al.\"\n    venue: \"ICLR 2026\"\n    year: 2025\n    arxiv_id: \"2509.19199\"\n    category: direct-competitor\n    role: competitor\n    relevance_note: >\n      [NEW-0517] Implicit PRM + dual advantage (step + episode level) for agentic RL.\n      WebShop 86.5%, VisualSokoban 91.7%. ICLR 2026 published.\n      Learns step-level credit via implicit rewards without explicit labels;\n      our work shows episode-level alone suffices when sign misattribution is the bottleneck.\n      Validates that step-level credit helps, but doesn't diagnose when it hurts.\n\n  - id: archer2024\n    title: \"ArCHer: Training Language Model Agents via Hierarchical Multi-Turn RL\"\n    authors: \"Zhou, Zanette, Pan, Levine, Kumar\"\n    venue: \"ICML 2024\"\n    year: 2024\n    arxiv_id: \"2402.19446\"\n    category: method-component\n    role: predecessor\n    relevance_note: >\n      [NEW-0517] Foundational hierarchical multi-turn RL framework (ICML 2024).\n      High-level off-policy value RL (utterance-level) + low-level token policy.\n      ~100x sample efficiency. Establishes that multi-turn RL needs hierarchical structure;\n      our work specifically diagnoses why flat step-independent approaches fail.\n\n  - id: ca-survey2026\n    title: \"From Reasoning to Agentic: Credit Assignment in Reinforcement Learning for Large Language Models\"\n    authors: \"Zhang\"\n    venue: \"arXiv\"\n    year: 2026\n    arxiv_id: \"2604.09459\"\n    category: background\n    role: background\n    relevance_note: >\n      [NEW-0517] Comprehensive survey of 47 CA methods (2024-2026). Two-dimensional\n      taxonomy: granularity (token/segment/step/turn/multi-agent) x methodology\n      (MC/TD/model-based/game-theoretic/information-theoretic). Contextualizes our\n      sign misattribution diagnosis within the broader CA landscape.\n\n  - id: hiper2026\n    title: \"HiPER: Hierarchical Reinforcement Learning with Explicit Credit Assignment for Large Language Model Agents\"\n    authors: \"Peng et al.\"\n    venue: \"arXiv\"\n    year: 2026\n    arxiv_id: \"2602.16165\"\n    category: method-component\n    role: background\n    relevance_note: >\n      [NEW-0517] Hierarchical Plan-Execute RL. ALFWorld 97.4% (7B), 95.3% (1.5B).\n      GRPO baseline: 71.1% (1.5B), 85.4% (7B). 2.8x training efficiency gain.\n      Pursues SOTA performance via hierarchical plan-execute architecture;\n      our work does mechanism diagnosis of why step-independent GRPO fails.\n      Different contribution dimension: not comparable on performance axis.\n",
      "numLines": 733,
      "startLine": 1,
      "totalLines": 733
    }
  },
  "sourceToolAssistantUUID": "cce95bc1-b851-4a1e-aa34-da0f26f68eac",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "7317ebb2-d910-42e9-95dc-fa8559b8ce74",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 32 · 2026-05-17T13:46:20.965Z_

```json
{
  "parentUuid": "5f5fa9f7-dcb7-44ce-b881-d79e91eea8b6",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "917fd2e1-223c-4fdc-a934-5e4c11c62b79",
  "timestamp": "2026-05-17T13:46:20.965Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "7317ebb2-d910-42e9-95dc-fa8559b8ce74",
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
  "leafUuid": "917fd2e1-223c-4fdc-a934-5e4c11c62b79",
  "sessionId": "7317ebb2-d910-42e9-95dc-fa8559b8ce74"
}
```

---

### Runtime record

_source line 34_

```json
{
  "type": "ai-title",
  "aiTitle": "Verify and correct Turn-PPO citation information",
  "sessionId": "7317ebb2-d910-42e9-95dc-fa8559b8ce74"
}
```

---

### Assistant

_source line 35 · 2026-05-17T13:46:23.753Z_

<details><summary>Logged reasoning block</summary>

```text
The file has been edited correctly. Now I need to save it via the MCP tool. Let me read the full content and save it.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "917fd2e1-223c-4fdc-a934-5e4c11c62b79",
  "isSidechain": false,
  "requestId": "req_011Cb8F5WeDdUZbWSChSLgeb",
  "type": "assistant",
  "uuid": "0594f7b4-c9dc-4930-b2be-80aa7f5adbd6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "7317ebb2-d910-42e9-95dc-fa8559b8ce74",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YQdpnx9FD1AAQ725thV2wu",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11060,
      "cache_read_input_tokens": 50263,
      "output_tokens": 178,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11060,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 178,
          "cache_read_input_tokens": 50263,
          "cache_creation_input_tokens": 11060,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11060
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

_source line 36 · 2026-05-17T13:46:24.238Z_

本地文件已修改。现在通过 MCP 同步保存。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0594f7b4-c9dc-4930-b2be-80aa7f5adbd6",
  "isSidechain": false,
  "requestId": "req_011Cb8F5WeDdUZbWSChSLgeb",
  "type": "assistant",
  "uuid": "9fd6eba7-ebb9-463e-99a9-d200403e250f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "7317ebb2-d910-42e9-95dc-fa8559b8ce74",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YQdpnx9FD1AAQ725thV2wu",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11060,
      "cache_read_input_tokens": 50263,
      "output_tokens": 178,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11060,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 178,
          "cache_read_input_tokens": 50263,
          "cache_creation_input_tokens": 11060,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11060
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

_source line 37 · 2026-05-17T13:46:26.315Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01UKAsWGWgx5YWGu84e69RuY`</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/literature_map.yaml",
  "description": "Read full file content for MCP save"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9fd6eba7-ebb9-463e-99a9-d200403e250f",
  "isSidechain": false,
  "requestId": "req_011Cb8F5WeDdUZbWSChSLgeb",
  "type": "assistant",
  "uuid": "ca02f345-c5c1-474f-98f9-b51d23315472",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "7317ebb2-d910-42e9-95dc-fa8559b8ce74",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YQdpnx9FD1AAQ725thV2wu",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11060,
      "cache_read_input_tokens": 50263,
      "output_tokens": 178,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11060,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 178,
          "cache_read_input_tokens": 50263,
          "cache_creation_input_tokens": 11060,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11060
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

_source line 38 · 2026-05-17T13:46:26.480Z_

<details><summary>↩ Tool result · `toolu_01UKAsWGWgx5YWGu84e69RuY`</summary>

```text
# B-IAVR Literature Map
# Updated: 2026-05-17
# Categories: direct-competitor, method-component, background, evaluation
# Roles: predecessor, competitor, baseline, evaluation, background

papers:

  # ============================================================
  # Direction 1: Self-Verification / Self-Correction in LLM Agents
  # ============================================================

  - id: kamoi2024self-correction-survey
    title: "When Can LLMs Actually Correct Their Own Mistakes? A Critical Survey of Self-Correction of LLMs"
    authors: "Kamoi et al."
    venue: "arXiv"
    year: 2024
    arxiv_id: "2406.01297"
    category: background
    role: background
    relevance_note: >
      Foundational survey establishing that pure intrinsic self-correction is unreliable.
      Validates B-IAVR's use of grounded verification (environment re-observation) over prompted self-feedback.

  - id: tie2025correctbench
    title: "Can LLMs Correct Themselves? A Benchmark of Self-Correction in LLMs"
    authors: "Tie et al."
    venue: "NeurIPS 2025 Datasets & Benchmarks"
    year: 2025
    arxiv_id: "2510.16062"
    category: background
    role: background
    relevance_note: >
      Benchmark showing self-correction has diminishing returns when applied uniformly.
      Supports B-IAVR's selective verification design over blanket correction.

  - id: self-verification-dilemma-2026
    title: "Self-Verification Dilemma: Experience-Driven Suppression of Overused Checking in LLM Reasoning"
    authors: "Long et al."
    venue: "arXiv"
    year: 2026
    arxiv_id: "2602.03485"
    category: background
    role: background
    relevance_note: >
      Empirically validates that >90% of self-verification is confirmatory, ~2% corrective.
      Directly supports B-IAVR's core thesis that verification should be selective.
      Their experience-pool approach is complementary to B-IAVR's action-change signal.

  - id: zhang2025incentivize-self-verify
    title: "Incentivizing LLMs to Self-Verify Their Answers"
    authors: "Zhang et al."
    venue: "arXiv"
    year: 2025
    arxiv_id: "2506.01369"
    category: background
    role: background
    relevance_note: >
      Unifies answer generation and verification via single RL training process.
      Parallel to B-IAVR: they train verification into generation; B-IAVR trains when to trigger separate verification.

  - id: mar2025
    title: "MAR: Multi-Agent Reflexion Improves Reasoning Abilities in LLMs"
    authors: "Ozer et al."
    venue: "arXiv"
    year: 2025
    arxiv_id: "2512.20845"
    category: background
    role: background
    relevance_note: >
      Multi-agent self-correction with diverse critic personas.
      Complementary: MAR improves correction quality; B-IAVR decides when to trigger correction.

  - id: ssr2025
    title: "SSR: Socratic Self-Refine for Large Language Model Reasoning"
    authors: "Shi et al."
    venue: "arXiv"
    year: 2025
    arxiv_id: "2511.10621"
    category: background
    role: background
    relevance_note: >
      Structured Socratic questioning for self-refinement.
      Complementary: improves correction step quality; B-IAVR focuses on when to invoke correction.

  - id: verifiagent2025
    title: "VerifiAgent: a Unified Verification Agent in Language Model Reasoning"
    authors: "Han et al."
    venue: "EMNLP 2025 Findings"
    year: 2025
    arxiv_id: "2504.00406"
    category: background
    role: background
    relevance_note: >
      Unified verification agent with meta-verification + tool-based adaptive verification.
      Focuses on how to verify (tool selection); B-IAVR focuses on when to verify (policy learning).
      Complementary: VerifiAgent's verification quality could enhance B-IAVR's verification step.

  # ============================================================
  # Direction 2: Agent RL Training
  # ============================================================

  - id: feng2025gigpo
    title: "GiGPO: Group-in-Group Policy Optimization for LLM Agent Training"
    authors: "Feng et al."
    venue: "NeurIPS 2025"
    year: 2025
    arxiv_id: "2505.10978"
    category: method-component
    role: predecessor
    relevance_note: >
      Core training algorithm for B-IAVR. Nested group structure provides step-level credit
      assignment without learned critic. >12% over GRPO on ALFWorld, >9% on WebShop.

  - id: selfguide2026
    title: "Co-Evolution of Policy and Internal Reward for Language Agents (Self-Guide)"
    authors: "Wang et al."
    venue: "arXiv"
    year: 2026
    arxiv_id: "2604.03098"
    category: method-component
    role: predecessor
    relevance_note: >
      Direct predecessor. B-IAVR extends Self-Guide's co-evolving internal reward.
      The self-guidance signal is the foundation for action-change detection triggering verification.
      8% improvement over env-reward-only on ALFWorld with Qwen3-1.7B/4B.

  - id: spear2025
    title: "Learn the Ropes, Then Trust the Wins: Self-imitation with Progressive Exploration for Agentic Reinforcement Learning"
    authors: "Qin et al."
    venue: "ICLR 2026"
    year: 2025
    arxiv_id: "2509.22601"
    category: method-component
    role: background
    relevance_note: >
      Curriculum-based self-imitation for sparse-reward agent tasks.
      Up to +16.1% on ALFWorld over GRPO. Self-imitation curriculum could augment B-IAVR training.

  - id: wei2025webagent-r1
    title: "WebAgent-R1: Training Web Agents via End-to-End Multi-Turn RL"
    authors: "Wei et al."
    venue: "EMNLP 2025"
    year: 2025
    arxiv_id: "2505.16421"
    category: background
    role: background
    relevance_note: >
      Extends GRPO to multi-turn (M-GRPO) with dynamic context compression.
      Qwen-2.5-3B: 6.1% to 33.9% on WebArena-Lite. M-GRPO multi-turn extension relevant to B-IAVR.

  - id: dapo2025
    title: "DAPO: An Open-Source LLM Reinforcement Learning System at Scale"
    authors: "Yu et al."
    venue: "arXiv"
    year: 2025
    arxiv_id: "2503.14476"
    category: method-component
    role: background
    relevance_note: >
      RL training stabilization techniques (Clip-Higher, Dynamic Sampling).
      Applicable to B-IAVR's RL training to prevent entropy collapse.

  - id: digiRL2024
    title: "DigiRL: Training In-The-Wild Device-Control Agents with Autonomous RL"
    authors: "Bai et al."
    venue: "NeurIPS 2024"
    year: 2024
    arxiv_id: "2406.11896"
    category: background
    role: background
    relevance_note: >
      Online RL for device control agents. Demonstrates online RL viability for interactive agents.
      49.5% absolute improvement over SFT. Parallel approach to B-IAVR in text-based setting.

  - id: li2025sorl
    title: "SORL: Stabilizing Off-Policy RL for Long-Horizon Agent Training"
    authors: "Li et al."
    venue: "arXiv"
    year: 2025
    arxiv_id: "2511.20718"
    category: method-component
    role: background
    relevance_note: >
      Turn-level importance sampling + clipping-triggered normalization for stable multi-turn agent RL.
      Directly applicable to B-IAVR's multi-turn ALFWorld training stability.

  - id: agentic-rl-survey-2025
    title: "The Landscape of Agentic Reinforcement Learning for LLMs: A Survey"
    authors: "Zhang et al."
    venue: "TMLR 2026"
    year: 2025
    arxiv_id: "2509.02547"
    category: background
    role: background
    relevance_note: >
      Comprehensive survey formalizing agentic RL. Contextualizes B-IAVR as training agents
      to make meta-decisions (when to verify) via RL within the POMDP framework.

  - id: skillmaster2026
    title: "SkillMaster: Toward Autonomous Skill Mastery in LLM Agents"
    authors: "Yang et al."
    venue: "arXiv"
    year: 2026
    arxiv_id: "2605.08693"
    category: method-component
    role: background
    relevance_note: >
      DualAdv-GRPO: separately estimates advantages for task-solving and skill-editing decisions.
      +8.8% on ALFWorld, +9.3% on WebShop. DualAdv structure could inform B-IAVR's
      separation of action and verification advantages.

  - id: t2po2026
    title: "T2PO: Uncertainty-Guided Exploration Control for Stable Multi-Turn Agentic RL"
    authors: "Wang et al."
    venue: "ICML 2026 Spotlight"
    year: 2026
    arxiv_id: "2605.02178"
    category: method-component
    role: background
    relevance_note: >
      Token- and turn-level uncertainty monitoring for stable multi-turn agent RL.
      Triggers thinking intervention when marginal uncertainty change drops below threshold.
      Evaluated on ALFWorld and WebShop. Conceptually related: uncertainty-based trigger vs
      B-IAVR's action-change trigger, but T2PO targets training stability, not deployment verification.

  - id: gvpo2026
    title: "GVPO: Group Verification-based Policy Optimization for Interactive Coding Agents"
    authors: "Dai et al."
    venue: "ICLR 2026"
    year: 2026
    arxiv_id: null  # no arXiv preprint; OpenReview ID: RY47Tq0VsV
    category: method-component
    role: background
    relevance_note: >
      Advantage shaping with outcome-verifiable + process-verifiable signals.
      +12.7% over o1 on AppWorld. Integrates intermediate execution feedback as step-level
      verification signals. Different focus: uses verification for credit assignment during
      training; B-IAVR learns when to invoke verification at deployment.

  - id: agentv-rl2026
    title: "AgentV-RL: Scaling Reward Modeling with Agentic Verifier"
    authors: "Zhang et al."
    venue: "arXiv"
    year: 2026
    arxiv_id: "2604.16004"
    category: method-component
    role: background
    relevance_note: >
      Bidirectional forward/backward agentic verifier for reward modeling in RL.
      4B model surpasses SOTA ORMs by 25.2%. Addresses verification quality in reward modeling;
      B-IAVR addresses verification timing in agent deployment. Complementary.

  - id: pa-moe2026
    title: "PA-MoE: Phase-Aware Mixture of Experts for Agentic Reinforcement Learning"
    authors: "Li et al."
    venue: "arXiv"
    year: 2026
    arxiv_id: "2602.17038"
    category: evaluation
    role: baseline
    relevance_note: >
      [NEW-0516] Lightweight phase router learns latent phase boundaries from RL objective.
      PA-MoE+GiGPO with Qwen2.5-1.5B achieves 93.8% on ALFWorld (+7.7 over GiGPO 86.1%).
      1.5B outperforms vanilla 7B GiGPO (90.2%). New small-model SOTA on ALFWorld.
      Orthogonal architecture innovation; important baseline to cite.

  - id: sdar2026
    title: "SDAR: Self-Distilled Agentic Reinforcement Learning"
    authors: "Lu et al."
    venue: "arXiv"
    year: 2026
    arxiv_id: "2605.15155"
    category: method-component
    role: background
    relevance_note: >
      [NEW-0516] On-policy self-distillation as gated auxiliary objective during RL training.
      Token-level gate decides supervision intensity. +9.4% over GRPO on ALFWorld.
      Complementary: SDAR improves RL training; B-IAVR learns verification policy.

  - id: hcapo2026
    title: "HCAPO: Hindsight Credit Assignment for Long-Horizon LLM Agents"
    authors: "Tan et al."
    venue: "arXiv"
    year: 2026
    arxiv_id: "2603.08754"
    category: method-component
    role: background
    relevance_note: >
      [NEW-0516] LLM-as-critic refines step-level Q-values via hindsight reasoning +
      multi-scale advantage for critical decision states.
      +13.8% on ALFWorld, +7.7% on WebShop over GRPO (Qwen2.5-7B).
      Could improve B-IAVR's reward signal for verification decision steps.

  - id: act2026
    title: "ACT: Agentic Critical Training"
    authors: "Liu et al."
    venue: "arXiv"
    year: 2026
    arxiv_id: "2603.08706"
    category: method-component
    role: background
    relevance_note: >
      [NEW-0516] Trains agents to judge action quality via critical comparison reward.
      +5.07 over IL, +4.62 over RL. Different axis: ACT improves reflection quality;
      B-IAVR decides when to reflect.

  - id: rwml2026
    title: "RWML: Reinforcement World Model Learning for LLM-based Agents"
    authors: "Yu et al."
    venue: "arXiv"
    year: 2026
    arxiv_id: "2602.05842"
    category: method-component
    role: background
    relevance_note: >
      [NEW-0516] Self-supervised world model via sim-to-real gap rewards in embedding space.
      +6.9 on ALFWorld over task-success-only RL. Matches expert-data training.
      Orthogonal: improves internal world model; B-IAVR adds selective verification.

  - id: skill0-2026
    title: "SKILL0: In-Context Agentic Reinforcement Learning for Skill Internalization"
    authors: "Lu et al."
    venue: "arXiv"
    year: 2026
    arxiv_id: "2604.02268"
    category: method-component
    role: background
    relevance_note: >
      [NEW-0516] Training-time curriculum progressively withdraws skill context until zero-shot.
      +9.7% on ALFWorld over GRPO, <0.5k tokens per step.
      Complementary: SKILL0 internalizes skills; B-IAVR adds selective verification.

  - id: fission-grpo2026
    title: "Fission-GRPO: Robust Tool Use via Learning to Recover from Execution Errors"
    authors: "Zhang et al."
    venue: "arXiv"
    year: 2026
    arxiv_id: "2601.15625"
    category: method-component
    role: background
    relevance_note: >
      [NEW-0516] Fissions failed trajectories into recovery training instances.
      +4% overall accuracy on BFCL v4 Multi-Turn over GRPO.
      Related: error recovery after failure vs B-IAVR's proactive verification.

  - id: selfbudgeter2026
    title: "SelfBudgeter: Adaptive Token Allocation for Efficient LLM Reasoning"
    authors: "Li et al."
    venue: "ICLR 2026 (under review)"
    year: 2025
    arxiv_id: "2505.11274"
    category: background
    role: background
    relevance_note: >
      [NEW-0516] Self-estimated token budgets + budget-guided GRPO. 61% token reduction.
      Parallel concept: SelfBudgeter allocates computation budget;
      B-IAVR makes binary verify/not-verify decision. Both use RL for adaptive compute.

  - id: cove2026
    title: "CoVe: Training Interactive Tool-Use Agents via Constraint-Guided Verification"
    authors: "Chen et al."
    venue: "arXiv"
    year: 2026
    arxiv_id: "2603.01940"
    category: background
    role: background
    relevance_note: >
      [NEW-0516] Task constraints guide trajectory generation and serve as deterministic verifiers.
      Different: CoVe uses verification for data synthesis; B-IAVR learns when to verify at inference.

  # ============================================================
  # Direction 3: Selective Verification / Adaptive Computation
  # ============================================================

  - id: wan2025derailer-rerailer
    title: "Derailer-Rerailer: Adaptive Verification for Efficient and Reliable LM Reasoning"
    authors: "Wan et al."
    venue: "ACL 2025 Findings"
    year: 2025
    arxiv_id: "2408.13940"
    category: direct-competitor
    role: competitor
    relevance_note: >
      Most directly related competitor. Both do selective verification with binary trigger.
      Key difference: operates on reasoning chains (single-turn); B-IAVR on agent trajectories (multi-turn).
      Uses heuristic instability signal; B-IAVR uses RL-trained action-change signal.
      8-11% accuracy gain, 2-3x efficiency over uniform verification.

  - id: sherlock2025
    title: "Sherlock: Reliable and Efficient Agentic Workflow Execution"
    authors: "Microsoft"
    venue: "arXiv"
    year: 2025
    arxiv_id: "2511.00330"
    category: direct-competitor
    role: competitor
    relevance_note: >
      Selective verification for agentic workflows via offline counterfactual analysis + speculative execution.
      Different scope: workflow DAG level (offline); B-IAVR is step-level (online RL).
      18.3% accuracy gain, 26% cost reduction, 48.7% latency reduction.

  - id: singhi2025when-to-verify
    title: "When To Solve, When To Verify: Compute-Optimal Verification for LLM Reasoning"
    authors: "Singhi et al."
    venue: "arXiv"
    year: 2025
    arxiv_id: "2504.01005"
    category: background
    role: background
    relevance_note: >
      Derives inference scaling laws for solve-vs-verify tradeoff.
      Finding that over-verification is suboptimal directly supports B-IAVR's selective approach.
      B-IAVR learns this allocation via RL rather than analytically.

  - id: yang2026ares
    title: "ARES: Adaptive Reasoning Effort Selection for Efficient LLM Agents"
    authors: "Yang et al."
    venue: "arXiv"
    year: 2026
    arxiv_id: "2603.07915"
    category: direct-competitor
    role: competitor
    relevance_note: >
      Closest competitor in agent domain. Both train learned per-step compute allocation.
      ARES uses SFT-initialized router further refined via GRPO with outcome + token efficiency reward;
      B-IAVR trains binary verify/not-verify via RL with action-change signal.
      Key differences: (1) reward signal — ARES optimizes token efficiency, B-IAVR uses action-change
      as verification trigger; (2) data requirement — ARES needs difficulty-annotated training data
      to bootstrap the router, B-IAVR learns from environment interaction alone.
      Reduces reasoning tokens by up to 52.7%.

  - id: tu2025autothink
    title: "Learning When to Think: Shaping Adaptive Reasoning in R1-Style Models via Multi-Stage RL"
    authors: "Tu et al."
    venue: "NeurIPS 2025"
    year: 2025
    arxiv_id: "2505.10832"
    category: direct-competitor
    role: competitor
    relevance_note: >
      Analogous idea in reasoning domain: RL-trained adaptive computation trigger.
      Operates on single-turn reasoning; B-IAVR on multi-turn agent trajectories.
      +6.4% accuracy, -52% tokens on DeepSeek-R1-Distill-Qwen-1.5B.

  - id: du2025thinkless
    title: "Thinkless: LLM Learns When to Think"
    authors: "Fang et al."
    venue: "NeurIPS 2025"
    year: 2025
    arxiv_id: "2505.13379"
    category: direct-competitor
    role: competitor
    relevance_note: >
      RL-trained control token to decide when to invoke extended thinking.
      Methodologically closest to B-IAVR in reasoning domain; B-IAVR applies to interactive agent trajectories.

  - id: wang2025efficient-agents
    title: "Efficient Agents: Building Effective Agents While Reducing Cost"
    authors: "Wang et al."
    venue: "arXiv"
    year: 2025
    arxiv_id: "2508.02694"
    category: background
    role: background
    relevance_note: >
      First systematic study of agent efficiency-effectiveness tradeoff.
      Framework-level cost reduction; B-IAVR addresses cost at verification-policy level.
      Retains 96.7% performance with 28.4% cost-of-pass improvement.

  - id: venktesh2025trust-but-verify
    title: "Trust but Verify! A Survey on Verification Design for Test-time Scaling"
    authors: "Venktesh et al."
    venue: "arXiv"
    year: 2025
    arxiv_id: "2508.16665"
    category: background
    role: background
    relevance_note: >
      Survey of verification approaches for test-time compute scaling.
      Identifies verification timing as key open problem. B-IAVR provides concrete solution for agent setting.

  - id: agent-omit2026
    title: "Agent-Omit: Training Efficient LLM Agents for Adaptive Thought and Observation Omission via Agentic RL"
    authors: "Ning et al."
    venue: "ICML 2026"
    year: 2026
    arxiv_id: "2602.04284"
    category: direct-competitor
    role: competitor
    relevance_note: >
      RL-trained policy for adaptive omission of redundant thoughts and observations.
      Agent-Omit-8B matches frontier agents with best efficiency tradeoff on 5 benchmarks.
      Both use RL to learn cost-efficient agent behavior. Key difference: Agent-Omit subtracts
      (omits unnecessary context); B-IAVR selectively adds (verification steps).
      Opposite but complementary approaches to cost-efficiency. Potentially combinable.

  - id: ava2026
    title: "Anytime Verified Agents: Adaptive Compute Allocation for Reliable LLM Reasoning under Budget Constraints"
    authors: "Patel"
    venue: "TMLR 2026"
    year: 2026
    arxiv_id: null  # no arXiv preprint; OpenReview ID: JMDCMf7mlF
    category: direct-competitor
    role: competitor
    relevance_note: >
      Dynamic compute allocation across search, sampling, and verification under budget.
      Uses calibrated uncertainty + value-of-information for selective verification cascades.
      Evaluated on GSM8K/MATH/HotpotQA/HumanEval (reasoning), not interactive agents.
      Key difference: analytical/heuristic allocation vs B-IAVR's RL-learned policy;
      single-turn reasoning vs multi-turn agent trajectories.

  - id: cast2026
    title: "CAST: Case-Based Calibration of Adaptive Reasoning and Execution for LLM Tool Use"
    authors: "Pang et al."
    venue: "arXiv"
    year: 2026
    arxiv_id: "2605.15041"
    category: background
    role: background
    relevance_note: >
      Historical execution cases calibrate reasoning depth for tool use.
      Reduces reasoning length 26% with +5.85% accuracy on BFCLv2/ToolBench.
      Related: adaptive reasoning depth; different: case-based calibration vs RL-learned policy.

  - id: marginal-token-allocators2026
    title: "Agentic AI Systems Should Be Designed as Marginal Token Allocators"
    authors: "Zhu"
    venue: "arXiv"
    year: 2026
    arxiv_id: "2605.01214"
    category: background
    role: background
    relevance_note: >
      Position paper framing agent cost-efficiency as marginal token allocation economics.
      Identifies under-verification as systematic failure mode. Supports B-IAVR's framing
      that verification decisions should reflect marginal cost-benefit analysis.

  - id: argos2025
    title: "Argos: Multimodal RL with Adaptive Verifier for AI Agents"
    authors: "Tan et al."
    venue: "arXiv (revised April 2026)"
    year: 2025
    arxiv_id: "2512.03438"
    category: background
    role: background
    relevance_note: >
      Agentic verifier that adaptively selects scoring functions for multimodal RL training.
      Different domain (multimodal/robotics). The adaptive verifier selection concept is
      complementary: Argos adapts how to verify; B-IAVR adapts when to verify.

  # ============================================================
  # Direction 4: ALFWorld / Interactive Environment Benchmarks
  # ============================================================

  - id: kim2025reflact
    title: "ReflAct: World-Grounded Decision Making in LLM Agents via Goal-State Reflection"
    authors: "Kim et al."
    venue: "EMNLP 2025"
    year: 2025
    arxiv_id: "2505.15182"
    category: evaluation
    role: baseline
    relevance_note: >
      Prompting SOTA on ALFWorld at 93.3%. Replaces ReAct's next-action thinking with state-goal reflection.
      B-IAVR addresses different axis (cost-efficiency) since ALFWorld accuracy is near saturation.

  - id: choudhury2025agentprm
    title: "Process Reward Models for LLM Agents: Practical Framework and Directions"
    authors: "Choudhury"
    venue: "arXiv"
    year: 2025
    arxiv_id: "2502.10325"
    category: evaluation
    role: baseline
    relevance_note: >
      Monte Carlo rollout-based process reward for agent training. 3B models achieve 91% on ALFWorld.
      Validates RL training approach; AgentPRM could serve as reward model for B-IAVR.

  - id: xi2025agentprm
    title: "AgentPRM: Process Reward Models for LLM Agents via Step-Wise Promise and Progress"
    authors: "Xi et al."
    venue: "ACM Web Conference 2026"
    year: 2025
    arxiv_id: "2511.08325"
    category: evaluation
    role: baseline
    relevance_note: >
      Independent work from Choudhury et al., using TD-based estimation with GAE for scalable
      PRM data labeling. 8x more compute-efficient than baselines with robust test-time scaling.
      Different approach: Choudhury uses MC rollouts; Xi uses TD+GAE for step-wise promise and progress.

  - id: xiang2024retrospex
    title: "Retrospex: Language Agent Meets Offline RL Critic"
    authors: "Xiang et al."
    venue: "EMNLP 2024"
    year: 2024
    arxiv_id: "2505.11807"
    category: background
    role: background
    relevance_note: >
      Offline RL Critic augments LLM agent action selection via dynamic rescoring.
      Similar architecture could inform B-IAVR's verification value estimation.

  - id: cfgm2025
    title: "CFGM: Coarse-to-Fine Grounded Memory for LLM Agent Planning"
    authors: "Yang et al."
    venue: "EMNLP 2025"
    year: 2025
    arxiv_id: "2508.15305"
    category: background
    role: background
    relevance_note: >
      Memory-augmented agent planning with episodic grounding.
      ALFWorld +10.40%, WebShop +20%. Complementary to B-IAVR's verification approach.

  - id: respact2024
    title: "ReSpAct: Harmonizing Reasoning, Speaking, and Acting"
    authors: "Dongre et al."
    venue: "arXiv"
    year: 2024
    arxiv_id: "2411.00927"
    category: evaluation
    role: baseline
    relevance_note: >
      Integrates dialogue/reasoning/acting. +6% over ReAct on ALFWorld.
      Reduces invalid actions from 13% to 3%; B-IAVR's verification achieves error prevention differently.

  # ============================================================
  # Direction 5: Multi-Turn Credit Assignment (Direct Competitors)
  # ============================================================

  - id: turn-ppo2025
    title: "Turn-PPO: Turn-Level Advantage Estimation with PPO for Improved Multi-Turn RL in Agentic LLMs"
    authors: "Li et al."
    venue: "arXiv"
    year: 2025
    arxiv_id: "2512.17008"
    category: direct-competitor
    role: competitor
    relevance_note: >
      [NEW-0517] Most direct competitor. Identifies "uniform advantage" problem in
      step-independent GRPO (subset of our "sign misattribution"). Proposes turn-level
      MDP + learned value function. Our differences: (1) more precise formalization
      (sign misattribution + gamma decay quantification), (2) contrarian solution
      (episode-level coarser credit vs their finer turn-level credit).

  - id: gagpo2026
    title: "GAGPO: Generalized Advantage Grouped Policy Optimization"
    authors: "Zhu et al."
    venue: "arXiv"
    year: 2026
    arxiv_id: "2605.13217"
    category: direct-competitor
    role: competitor
    relevance_note: >
      [NEW-0517] Critic-free step-aligned credit via non-parametric grouped value proxy +
      TD/GAE-style temporal advantages. ALFWorld 93.5% (1.5B), 95.6% (7B).
      Pursues finer-grained credit to improve performance; our work diagnoses why
      step-independent fails (sign misattribution) and shows coarser episode-level suffices.
      Different contribution axis: performance optimization vs mechanism diagnosis.

  - id: mt-grpo2025
    title: "Reinforcing Multi-Turn Reasoning in LLM Agents via Turn-Level Reward Design"
    authors: "Wei et al."
    venue: "arXiv"
    year: 2025
    arxiv_id: "2505.11821"
    category: direct-competitor
    role: competitor
    relevance_note: >
      [NEW-0517] Proposes MT-GRPO with turn-level reward design for multi-turn RL.
      Evaluated on QA search tasks (NQ, TriviaQA, HotpotQA), not ALFWorld.
      Qwen2.5-7B. Same direction as Turn-PPO (finer turn-level credit);
      our contrarian shows coarser episode-level eliminates sign misattribution.

  - id: istar2025
    title: "Agentic Reinforcement Learning with Implicit Step Rewards"
    authors: "Liu et al."
    venue: "ICLR 2026"
    year: 2025
    arxiv_id: "2509.19199"
    category: direct-competitor
    role: competitor
    relevance_note: >
      [NEW-0517] Implicit PRM + dual advantage (step + episode level) for agentic RL.
      WebShop 86.5%, VisualSokoban 91.7%. ICLR 2026 published.
      Learns step-level credit via implicit rewards without explicit labels;
      our work shows episode-level alone suffices when sign misattribution is the bottleneck.
      Validates that step-level credit helps, but doesn't diagnose when it hurts.

  - id: archer2024
    title: "ArCHer: Training Language Model Agents via Hierarchical Multi-Turn RL"
    authors: "Zhou, Zanette, Pan, Levine, Kumar"
    venue: "ICML 2024"
    year: 2024
    arxiv_id: "2402.19446"
    category: method-component
    role: predecessor
    relevance_note: >
      [NEW-0517] Foundational hierarchical multi-turn RL framework (ICML 2024).
      High-level off-policy value RL (utterance-level) + low-level token policy.
      ~100x sample efficiency. Establishes that multi-turn RL needs hierarchical structure;
      our work specifically diagnoses why flat step-independent approaches fail.

  - id: ca-survey2026
    title: "From Reasoning to Agentic: Credit Assignment in Reinforcement Learning for Large Language Models"
    authors: "Zhang"
    venue: "arXiv"
    year: 2026
    arxiv_id: "2604.09459"
    category: background
    role: background
    relevance_note: >
      [NEW-0517] Comprehensive survey of 47 CA methods (2024-2026). Two-dimensional
      taxonomy: granularity (token/segment/step/turn/multi-agent) x methodology
      (MC/TD/model-based/game-theoretic/information-theoretic). Contextualizes our
      sign misattribution diagnosis within the broader CA landscape.

  - id: hiper2026
    title: "HiPER: Hierarchical Reinforcement Learning with Explicit Credit Assignment for Large Language Model Agents"
    authors: "Peng et al."
    venue: "arXiv"
    year: 2026
    arxiv_id: "2602.16165"
    category: method-component
    role: background
    relevance_note: >
      [NEW-0517] Hierarchical Plan-Execute RL. ALFWorld 97.4% (7B), 95.3% (1.5B).
      GRPO baseline: 71.1% (1.5B), 85.4% (7B). 2.8x training efficiency gain.
      Pursues SOTA performance via hierarchical plan-execute architecture;
      our work does mechanism diagnosis of why step-independent GRPO fails.
      Different contribution dimension: not comparable on performance axis.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ca02f345-c5c1-474f-98f9-b51d23315472",
  "isSidechain": false,
  "promptId": "71e953e0-39de-4d6a-a9b9-c8a649da7bce",
  "type": "user",
  "uuid": "3b6e44f0-4667-4397-9f08-ec17e956fedf",
  "toolUseResult": {
    "stdout": "# B-IAVR Literature Map\n# Updated: 2026-05-17\n# Categories: direct-competitor, method-component, background, evaluation\n# Roles: predecessor, competitor, baseline, evaluation, background\n\npapers:\n\n  # ============================================================\n  # Direction 1: Self-Verification / Self-Correction in LLM Agents\n  # ============================================================\n\n  - id: kamoi2024self-correction-survey\n    title: \"When Can LLMs Actually Correct Their Own Mistakes? A Critical Survey of Self-Correction of LLMs\"\n    authors: \"Kamoi et al.\"\n    venue: \"arXiv\"\n    year: 2024\n    arxiv_id: \"2406.01297\"\n    category: background\n    role: background\n    relevance_note: >\n      Foundational survey establishing that pure intrinsic self-correction is unreliable.\n      Validates B-IAVR's use of grounded verification (environment re-observation) over prompted self-feedback.\n\n  - id: tie2025correctbench\n    title: \"Can LLMs Correct Themselves? A Benchmark of Self-Correction in LLMs\"\n    authors: \"Tie et al.\"\n    venue: \"NeurIPS 2025 Datasets & Benchmarks\"\n    year: 2025\n    arxiv_id: \"2510.16062\"\n    category: background\n    role: background\n    relevance_note: >\n      Benchmark showing self-correction has diminishing returns when applied uniformly.\n      Supports B-IAVR's selective verification design over blanket correction.\n\n  - id: self-verification-dilemma-2026\n    title: \"Self-Verification Dilemma: Experience-Driven Suppression of Overused Checking in LLM Reasoning\"\n    authors: \"Long et al.\"\n    venue: \"arXiv\"\n    year: 2026\n    arxiv_id: \"2602.03485\"\n    category: background\n    role: background\n    relevance_note: >\n      Empirically validates that >90% of self-verification is confirmatory, ~2% corrective.\n      Directly supports B-IAVR's core thesis that verification should be selective.\n      Their experience-pool approach is complementary to B-IAVR's action-change signal.\n\n  - id: zhang2025incentivize-self-verify\n    title: \"Incentivizing LLMs to Self-Verify Their Answers\"\n    authors: \"Zhang et al.\"\n    venue: \"arXiv\"\n    year: 2025\n    arxiv_id: \"2506.01369\"\n    category: background\n    role: background\n    relevance_note: >\n      Unifies answer generation and verification via single RL training process.\n      Parallel to B-IAVR: they train verification into generation; B-IAVR trains when to trigger separate verification.\n\n  - id: mar2025\n    title: \"MAR: Multi-Agent Reflexion Improves Reasoning Abilities in LLMs\"\n    authors: \"Ozer et al.\"\n    venue: \"arXiv\"\n    year: 2025\n    arxiv_id: \"2512.20845\"\n    category: background\n    role: background\n    relevance_note: >\n      Multi-agent self-correction with diverse critic personas.\n      Complementary: MAR improves correction quality; B-IAVR decides when to trigger correction.\n\n  - id: ssr2025\n    title: \"SSR: Socratic Self-Refine for Large Language Model Reasoning\"\n    authors: \"Shi et al.\"\n    venue: \"arXiv\"\n    year: 2025\n    arxiv_id: \"2511.10621\"\n    category: background\n    role: background\n    relevance_note: >\n      Structured Socratic questioning for self-refinement.\n      Complementary: improves correction step quality; B-IAVR focuses on when to invoke correction.\n\n  - id: verifiagent2025\n    title: \"VerifiAgent: a Unified Verification Agent in Language Model Reasoning\"\n    authors: \"Han et al.\"\n    venue: \"EMNLP 2025 Findings\"\n    year: 2025\n    arxiv_id: \"2504.00406\"\n    category: background\n    role: background\n    relevance_note: >\n      Unified verification agent with meta-verification + tool-based adaptive verification.\n      Focuses on how to verify (tool selection); B-IAVR focuses on when to verify (policy learning).\n      Complementary: VerifiAgent's verification quality could enhance B-IAVR's verification step.\n\n  # ============================================================\n  # Direction 2: Agent RL Training\n  # ============================================================\n\n  - id: feng2025gigpo\n    title: \"GiGPO: Group-in-Group Policy Optimization for LLM Agent Training\"\n    authors: \"Feng et al.\"\n    venue: \"NeurIPS 2025\"\n    year: 2025\n    arxiv_id: \"2505.10978\"\n    category: method-component\n    role: predecessor\n    relevance_note: >\n      Core training algorithm for B-IAVR. Nested group structure provides step-level credit\n      assignment without learned critic. >12% over GRPO on ALFWorld, >9% on WebShop.\n\n  - id: selfguide2026\n    title: \"Co-Evolution of Policy and Internal Reward for Language Agents (Self-Guide)\"\n    authors: \"Wang et al.\"\n    venue: \"arXiv\"\n    year: 2026\n    arxiv_id: \"2604.03098\"\n    category: method-component\n    role: predecessor\n    relevance_note: >\n      Direct predecessor. B-IAVR extends Self-Guide's co-evolving internal reward.\n      The self-guidance signal is the foundation for action-change detection triggering verification.\n      8% improvement over env-reward-only on ALFWorld with Qwen3-1.7B/4B.\n\n  - id: spear2025\n    title: \"Learn the Ropes, Then Trust the Wins: Self-imitation with Progressive Exploration for Agentic Reinforcement Learning\"\n    authors: \"Qin et al.\"\n    venue: \"ICLR 2026\"\n    year: 2025\n    arxiv_id: \"2509.22601\"\n    category: method-component\n    role: background\n    relevance_note: >\n      Curriculum-based self-imitation for sparse-reward agent tasks.\n      Up to +16.1% on ALFWorld over GRPO. Self-imitation curriculum could augment B-IAVR training.\n\n  - id: wei2025webagent-r1\n    title: \"WebAgent-R1: Training Web Agents via End-to-End Multi-Turn RL\"\n    authors: \"Wei et al.\"\n    venue: \"EMNLP 2025\"\n    year: 2025\n    arxiv_id: \"2505.16421\"\n    category: background\n    role: background\n    relevance_note: >\n      Extends GRPO to multi-turn (M-GRPO) with dynamic context compression.\n      Qwen-2.5-3B: 6.1% to 33.9% on WebArena-Lite. M-GRPO multi-turn extension relevant to B-IAVR.\n\n  - id: dapo2025\n    title: \"DAPO: An Open-Source LLM Reinforcement Learning System at Scale\"\n    authors: \"Yu et al.\"\n    venue: \"arXiv\"\n    year: 2025\n    arxiv_id: \"2503.14476\"\n    category: method-component\n    role: background\n    relevance_note: >\n      RL training stabilization techniques (Clip-Higher, Dynamic Sampling).\n      Applicable to B-IAVR's RL training to prevent entropy collapse.\n\n  - id: digiRL2024\n    title: \"DigiRL: Training In-The-Wild Device-Control Agents with Autonomous RL\"\n    authors: \"Bai et al.\"\n    venue: \"NeurIPS 2024\"\n    year: 2024\n    arxiv_id: \"2406.11896\"\n    category: background\n    role: background\n    relevance_note: >\n      Online RL for device control agents. Demonstrates online RL viability for interactive agents.\n      49.5% absolute improvement over SFT. Parallel approach to B-IAVR in text-based setting.\n\n  - id: li2025sorl\n    title: \"SORL: Stabilizing Off-Policy RL for Long-Horizon Agent Training\"\n    authors: \"Li et al.\"\n    venue: \"arXiv\"\n    year: 2025\n    arxiv_id: \"2511.20718\"\n    category: method-component\n    role: background\n    relevance_note: >\n      Turn-level importance sampling + clipping-triggered normalization for stable multi-turn agent RL.\n      Directly applicable to B-IAVR's multi-turn ALFWorld training stability.\n\n  - id: agentic-rl-survey-2025\n    title: \"The Landscape of Agentic Reinforcement Learning for LLMs: A Survey\"\n    authors: \"Zhang et al.\"\n    venue: \"TMLR 2026\"\n    year: 2025\n    arxiv_id: \"2509.02547\"\n    category: background\n    role: background\n    relevance_note: >\n      Comprehensive survey formalizing agentic RL. Contextualizes B-IAVR as training agents\n      to make meta-decisions (when to verify) via RL within the POMDP framework.\n\n  - id: skillmaster2026\n    title: \"SkillMaster: Toward Autonomous Skill Mastery in LLM Agents\"\n    authors: \"Yang et al.\"\n    venue: \"arXiv\"\n    year: 2026\n    arxiv_id: \"2605.08693\"\n    category: method-component\n    role: background\n    relevance_note: >\n      DualAdv-GRPO: separately estimates advantages for task-solving and skill-editing decisions.\n      +8.8% on ALFWorld, +9.3% on WebShop. DualAdv structure could inform B-IAVR's\n      separation of action and verification advantages.\n\n  - id: t2po2026\n    title: \"T2PO: Uncertainty-Guided Exploration Control for Stable Multi-Turn Agentic RL\"\n    authors: \"Wang et al.\"\n    venue: \"ICML 2026 Spotlight\"\n    year: 2026\n    arxiv_id: \"2605.02178\"\n    category: method-component\n    role: background\n    relevance_note: >\n      Token- and turn-level uncertainty monitoring for stable multi-turn agent RL.\n      Triggers thinking intervention when marginal uncertainty change drops below threshold.\n      Evaluated on ALFWorld and WebShop. Conceptually related: uncertainty-based trigger vs\n      B-IAVR's action-change trigger, but T2PO targets training stability, not deployment verification.\n\n  - id: gvpo2026\n    title: \"GVPO: Group Verification-based Policy Optimization for Interactive Coding Agents\"\n    authors: \"Dai et al.\"\n    venue: \"ICLR 2026\"\n    year: 2026\n    arxiv_id: null  # no arXiv preprint; OpenReview ID: RY47Tq0VsV\n    category: method-component\n    role: background\n    relevance_note: >\n      Advantage shaping with outcome-verifiable + process-verifiable signals.\n      +12.7% over o1 on AppWorld. Integrates intermediate execution feedback as step-level\n      verification signals. Different focus: uses verification for credit assignment during\n      training; B-IAVR learns when to invoke verification at deployment.\n\n  - id: agentv-rl2026\n    title: \"AgentV-RL: Scaling Reward Modeling with Agentic Verifier\"\n    authors: \"Zhang et al.\"\n    venue: \"arXiv\"\n    year: 2026\n    arxiv_id: \"2604.16004\"\n    category: method-component\n    role: background\n    relevance_note: >\n      Bidirectional forward/backward agentic verifier for reward modeling in RL.\n      4B model surpasses SOTA ORMs by 25.2%. Addresses verification quality in reward modeling;\n      B-IAVR addresses verification timing in agent deployment. Complementary.\n\n  - id: pa-moe2026\n    title: \"PA-MoE: Phase-Aware Mixture of Experts for Agentic Reinforcement Learning\"\n    authors: \"Li et al.\"\n    venue: \"arXiv\"\n    year: 2026\n    arxiv_id: \"2602.17038\"\n    category: evaluation\n    role: baseline\n    relevance_note: >\n      [NEW-0516] Lightweight phase router learns latent phase boundaries from RL objective.\n      PA-MoE+GiGPO with Qwen2.5-1.5B achieves 93.8% on ALFWorld (+7.7 over GiGPO 86.1%).\n      1.5B outperforms vanilla 7B GiGPO (90.2%). New small-model SOTA on ALFWorld.\n      Orthogonal architecture innovation; important baseline to cite.\n\n  - id: sdar2026\n    title: \"SDAR: Self-Distilled Agentic Reinforcement Learning\"\n    authors: \"Lu et al.\"\n    venue: \"arXiv\"\n    year: 2026\n    arxiv_id: \"2605.15155\"\n    category: method-component\n    role: background\n    relevance_note: >\n      [NEW-0516] On-policy self-distillation as gated auxiliary objective during RL training.\n      Token-level gate decides supervision intensity. +9.4% over GRPO on ALFWorld.\n      Complementary: SDAR improves RL training; B-IAVR learns verification policy.\n\n  - id: hcapo2026\n    title: \"HCAPO: Hindsight Credit Assignment for Long-Horizon LLM Agents\"\n    authors: \"Tan et al.\"\n    venue: \"arXiv\"\n    year: 2026\n    arxiv_id: \"2603.08754\"\n    category: method-component\n    role: background\n    relevance_note: >\n      [NEW-0516] LLM-as-critic refines step-level Q-values via hindsight reasoning +\n      multi-scale advantage for critical decision states.\n      +13.8% on ALFWorld, +7.7% on WebShop over GRPO (Qwen2.5-7B).\n      Could improve B-IAVR's reward signal for verification decision steps.\n\n  - id: act2026\n    title: \"ACT: Agentic Critical Training\"\n    authors: \"Liu et al.\"\n    venue: \"arXiv\"\n    year: 2026\n    arxiv_id: \"2603.08706\"\n    category: method-component\n    role: background\n    relevance_note: >\n      [NEW-0516] Trains agents to judge action quality via critical comparison reward.\n      +5.07 over IL, +4.62 over RL. Different axis: ACT improves reflection quality;\n      B-IAVR decides when to reflect.\n\n  - id: rwml2026\n    title: \"RWML: Reinforcement World Model Learning for LLM-based Agents\"\n    authors: \"Yu et al.\"\n    venue: \"arXiv\"\n    year: 2026\n    arxiv_id: \"2602.05842\"\n    category: method-component\n    role: background\n    relevance_note: >\n      [NEW-0516] Self-supervised world model via sim-to-real gap rewards in embedding space.\n      +6.9 on ALFWorld over task-success-only RL. Matches expert-data training.\n      Orthogonal: improves internal world model; B-IAVR adds selective verification.\n\n  - id: skill0-2026\n    title: \"SKILL0: In-Context Agentic Reinforcement Learning for Skill Internalization\"\n    authors: \"Lu et al.\"\n    venue: \"arXiv\"\n    year: 2026\n    arxiv_id: \"2604.02268\"\n    category: method-component\n    role: background\n    relevance_note: >\n      [NEW-0516] Training-time curriculum progressively withdraws skill context until zero-shot.\n      +9.7% on ALFWorld over GRPO, <0.5k tokens per step.\n      Complementary: SKILL0 internalizes skills; B-IAVR adds selective verification.\n\n  - id: fission-grpo2026\n    title: \"Fission-GRPO: Robust Tool Use via Learning to Recover from Execution Errors\"\n    authors: \"Zhang et al.\"\n    venue: \"arXiv\"\n    year: 2026\n    arxiv_id: \"2601.15625\"\n    category: method-component\n    role: background\n    relevance_note: >\n      [NEW-0516] Fissions failed trajectories into recovery training instances.\n      +4% overall accuracy on BFCL v4 Multi-Turn over GRPO.\n      Related: error recovery after failure vs B-IAVR's proactive verification.\n\n  - id: selfbudgeter2026\n    title: \"SelfBudgeter: Adaptive Token Allocation for Efficient LLM Reasoning\"\n    authors: \"Li et al.\"\n    venue: \"ICLR 2026 (under review)\"\n    year: 2025\n    arxiv_id: \"2505.11274\"\n    category: background\n    role: background\n    relevance_note: >\n      [NEW-0516] Self-estimated token budgets + budget-guided GRPO. 61% token reduction.\n      Parallel concept: SelfBudgeter allocates computation budget;\n      B-IAVR makes binary verify/not-verify decision. Both use RL for adaptive compute.\n\n  - id: cove2026\n    title: \"CoVe: Training Interactive Tool-Use Agents via Constraint-Guided Verification\"\n    authors: \"Chen et al.\"\n    venue: \"arXiv\"\n    year: 2026\n    arxiv_id: \"2603.01940\"\n    category: background\n    role: background\n    relevance_note: >\n      [NEW-0516] Task constraints guide trajectory generation and serve as deterministic verifiers.\n      Different: CoVe uses verification for data synthesis; B-IAVR learns when to verify at inference.\n\n  # ============================================================\n  # Direction 3: Selective Verification / Adaptive Computation\n  # ============================================================\n\n  - id: wan2025derailer-rerailer\n    title: \"Derailer-Rerailer: Adaptive Verification for Efficient and Reliable LM Reasoning\"\n    authors: \"Wan et al.\"\n    venue: \"ACL 2025 Findings\"\n    year: 2025\n    arxiv_id: \"2408.13940\"\n    category: direct-competitor\n    role: competitor\n    relevance_note: >\n      Most directly related competitor. Both do selective verification with binary trigger.\n      Key difference: operates on reasoning chains (single-turn); B-IAVR on agent trajectories (multi-turn).\n      Uses heuristic instability signal; B-IAVR uses RL-trained action-change signal.\n      8-11% accuracy gain, 2-3x efficiency over uniform verification.\n\n  - id: sherlock2025\n    title: \"Sherlock: Reliable and Efficient Agentic Workflow Execution\"\n    authors: \"Microsoft\"\n    venue: \"arXiv\"\n    year: 2025\n    arxiv_id: \"2511.00330\"\n    category: direct-competitor\n    role: competitor\n    relevance_note: >\n      Selective verification for agentic workflows via offline counterfactual analysis + speculative execution.\n      Different scope: workflow DAG level (offline); B-IAVR is step-level (online RL).\n      18.3% accuracy gain, 26% cost reduction, 48.7% latency reduction.\n\n  - id: singhi2025when-to-verify\n    title: \"When To Solve, When To Verify: Compute-Optimal Verification for LLM Reasoning\"\n    authors: \"Singhi et al.\"\n    venue: \"arXiv\"\n    year: 2025\n    arxiv_id: \"2504.01005\"\n    category: background\n    role: background\n    relevance_note: >\n      Derives inference scaling laws for solve-vs-verify tradeoff.\n      Finding that over-verification is suboptimal directly supports B-IAVR's selective approach.\n      B-IAVR learns this allocation via RL rather than analytically.\n\n  - id: yang2026ares\n    title: \"ARES: Adaptive Reasoning Effort Selection for Efficient LLM Agents\"\n    authors: \"Yang et al.\"\n    venue: \"arXiv\"\n    year: 2026\n    arxiv_id: \"2603.07915\"\n    category: direct-competitor\n    role: competitor\n    relevance_note: >\n      Closest competitor in agent domain. Both train learned per-step compute allocation.\n      ARES uses SFT-initialized router further refined via GRPO with outcome + token efficiency reward;\n      B-IAVR trains binary verify/not-verify via RL with action-change signal.\n      Key differences: (1) reward signal — ARES optimizes token efficiency, B-IAVR uses action-change\n      as verification trigger; (2) data requirement — ARES needs difficulty-annotated training data\n      to bootstrap the router, B-IAVR learns from environment interaction alone.\n      Reduces reasoning tokens by up to 52.7%.\n\n  - id: tu2025autothink\n    title: \"Learning When to Think: Shaping Adaptive Reasoning in R1-Style Models via Multi-Stage RL\"\n    authors: \"Tu et al.\"\n    venue: \"NeurIPS 2025\"\n    year: 2025\n    arxiv_id: \"2505.10832\"\n    category: direct-competitor\n    role: competitor\n    relevance_note: >\n      Analogous idea in reasoning domain: RL-trained adaptive computation trigger.\n      Operates on single-turn reasoning; B-IAVR on multi-turn agent trajectories.\n      +6.4% accuracy, -52% tokens on DeepSeek-R1-Distill-Qwen-1.5B.\n\n  - id: du2025thinkless\n    title: \"Thinkless: LLM Learns When to Think\"\n    authors: \"Fang et al.\"\n    venue: \"NeurIPS 2025\"\n    year: 2025\n    arxiv_id: \"2505.13379\"\n    category: direct-competitor\n    role: competitor\n    relevance_note: >\n      RL-trained control token to decide when to invoke extended thinking.\n      Methodologically closest to B-IAVR in reasoning domain; B-IAVR applies to interactive agent trajectories.\n\n  - id: wang2025efficient-agents\n    title: \"Efficient Agents: Building Effective Agents While Reducing Cost\"\n    authors: \"Wang et al.\"\n    venue: \"arXiv\"\n    year: 2025\n    arxiv_id: \"2508.02694\"\n    category: background\n    role: background\n    relevance_note: >\n      First systematic study of agent efficiency-effectiveness tradeoff.\n      Framework-level cost reduction; B-IAVR addresses cost at verification-policy level.\n      Retains 96.7% performance with 28.4% cost-of-pass improvement.\n\n  - id: venktesh2025trust-but-verify\n    title: \"Trust but Verify! A Survey on Verification Design for Test-time Scaling\"\n    authors: \"Venktesh et al.\"\n    venue: \"arXiv\"\n    year: 2025\n    arxiv_id: \"2508.16665\"\n    category: background\n    role: background\n    relevance_note: >\n      Survey of verification approaches for test-time compute scaling.\n      Identifies verification timing as key open problem. B-IAVR provides concrete solution for agent setting.\n\n  - id: agent-omit2026\n    title: \"Agent-Omit: Training Efficient LLM Agents for Adaptive Thought and Observation Omission via Agentic RL\"\n    authors: \"Ning et al.\"\n    venue: \"ICML 2026\"\n    year: 2026\n    arxiv_id: \"2602.04284\"\n    category: direct-competitor\n    role: competitor\n    relevance_note: >\n      RL-trained policy for adaptive omission of redundant thoughts and observations.\n      Agent-Omit-8B matches frontier agents with best efficiency tradeoff on 5 benchmarks.\n      Both use RL to learn cost-efficient agent behavior. Key difference: Agent-Omit subtracts\n      (omits unnecessary context); B-IAVR selectively adds (verification steps).\n      Opposite but complementary approaches to cost-efficiency. Potentially combinable.\n\n  - id: ava2026\n    title: \"Anytime Verified Agents: Adaptive Compute Allocation for Reliable LLM Reasoning under Budget Constraints\"\n    authors: \"Patel\"\n    venue: \"TMLR 2026\"\n    year: 2026\n    arxiv_id: null  # no arXiv preprint; OpenReview ID: JMDCMf7mlF\n    category: direct-competitor\n    role: competitor\n    relevance_note: >\n      Dynamic compute allocation across search, sampling, and verification under budget.\n      Uses calibrated uncertainty + value-of-information for selective verification cascades.\n      Evaluated on GSM8K/MATH/HotpotQA/HumanEval (reasoning), not interactive agents.\n      Key difference: analytical/heuristic allocation vs B-IAVR's RL-learned policy;\n      single-turn reasoning vs multi-turn agent trajectories.\n\n  - id: cast2026\n    title: \"CAST: Case-Based Calibration of Adaptive Reasoning and Execution for LLM Tool Use\"\n    authors: \"Pang et al.\"\n    venue: \"arXiv\"\n    year: 2026\n    arxiv_id: \"2605.15041\"\n    category: background\n    role: background\n    relevance_note: >\n      Historical execution cases calibrate reasoning depth for tool use.\n      Reduces reasoning length 26% with +5.85% accuracy on BFCLv2/ToolBench.\n      Related: adaptive reasoning depth; different: case-based calibration vs RL-learned policy.\n\n  - id: marginal-token-allocators2026\n    title: \"Agentic AI Systems Should Be Designed as Marginal Token Allocators\"\n    authors: \"Zhu\"\n    venue: \"arXiv\"\n    year: 2026\n    arxiv_id: \"2605.01214\"\n    category: background\n    role: background\n    relevance_note: >\n      Position paper framing agent cost-efficiency as marginal token allocation economics.\n      Identifies under-verification as systematic failure mode. Supports B-IAVR's framing\n      that verification decisions should reflect marginal cost-benefit analysis.\n\n  - id: argos2025\n    title: \"Argos: Multimodal RL with Adaptive Verifier for AI Agents\"\n    authors: \"Tan et al.\"\n    venue: \"arXiv (revised April 2026)\"\n    year: 2025\n    arxiv_id: \"2512.03438\"\n    category: background\n    role: background\n    relevance_note: >\n      Agentic verifier that adaptively selects scoring functions for multimodal RL training.\n      Different domain (multimodal/robotics). The adaptive verifier selection concept is\n      complementary: Argos adapts how to verify; B-IAVR adapts when to verify.\n\n  # ============================================================\n  # Direction 4: ALFWorld / Interactive Environment Benchmarks\n  # ============================================================\n\n  - id: kim2025reflact\n    title: \"ReflAct: World-Grounded Decision Making in LLM Agents via Goal-State Reflection\"\n    authors: \"Kim et al.\"\n    venue: \"EMNLP 2025\"\n    year: 2025\n    arxiv_id: \"2505.15182\"\n    category: evaluation\n    role: baseline\n    relevance_note: >\n      Prompting SOTA on ALFWorld at 93.3%. Replaces ReAct's next-action thinking with state-goal reflection.\n      B-IAVR addresses different axis (cost-efficiency) since ALFWorld accuracy is near saturation.\n\n  - id: choudhury2025agentprm\n    title: \"Process Reward Models for LLM Agents: Practical Framework and Directions\"\n    authors: \"Choudhury\"\n    venue: \"arXiv\"\n    year: 2025\n    arxiv_id: \"2502.10325\"\n    category: evaluation\n    role: baseline\n    relevance_note: >\n      Monte Carlo rollout-based process reward for agent training. 3B models achieve 91% on ALFWorld.\n      Validates RL training approach; AgentPRM could serve as reward model for B-IAVR.\n\n  - id: xi2025agentprm\n    title: \"AgentPRM: Process Reward Models for LLM Agents via Step-Wise Promise and Progress\"\n    authors: \"Xi et al.\"\n    venue: \"ACM Web Conference 2026\"\n    year: 2025\n    arxiv_id: \"2511.08325\"\n    category: evaluation\n    role: baseline\n    relevance_note: >\n      Independent work from Choudhury et al., using TD-based estimation with GAE for scalable\n      PRM data labeling. 8x more compute-efficient than baselines with robust test-time scaling.\n      Different approach: Choudhury uses MC rollouts; Xi uses TD+GAE for step-wise promise and progress.\n\n  - id: xiang2024retrospex\n    title: \"Retrospex: Language Agent Meets Offline RL Critic\"\n    authors: \"Xiang et al.\"\n    venue: \"EMNLP 2024\"\n    year: 2024\n    arxiv_id: \"2505.11807\"\n    category: background\n    role: background\n    relevance_note: >\n      Offline RL Critic augments LLM agent action selection via dynamic rescoring.\n      Similar architecture could inform B-IAVR's verification value estimation.\n\n  - id: cfgm2025\n    title: \"CFGM: Coarse-to-Fine Grounded Memory for LLM Agent Planning\"\n    authors: \"Yang et al.\"\n    venue: \"EMNLP 2025\"\n    year: 2025\n    arxiv_id: \"2508.15305\"\n    category: background\n    role: background\n    relevance_note: >\n      Memory-augmented agent planning with episodic grounding.\n      ALFWorld +10.40%, WebShop +20%. Complementary to B-IAVR's verification approach.\n\n  - id: respact2024\n    title: \"ReSpAct: Harmonizing Reasoning, Speaking, and Acting\"\n    authors: \"Dongre et al.\"\n    venue: \"arXiv\"\n    year: 2024\n    arxiv_id: \"2411.00927\"\n    category: evaluation\n    role: baseline\n    relevance_note: >\n      Integrates dialogue/reasoning/acting. +6% over ReAct on ALFWorld.\n      Reduces invalid actions from 13% to 3%; B-IAVR's verification achieves error prevention differently.\n\n  # ============================================================\n  # Direction 5: Multi-Turn Credit Assignment (Direct Competitors)\n  # ============================================================\n\n  - id: turn-ppo2025\n    title: \"Turn-PPO: Turn-Level Advantage Estimation with PPO for Improved Multi-Turn RL in Agentic LLMs\"\n    authors: \"Li et al.\"\n    venue: \"arXiv\"\n    year: 2025\n    arxiv_id: \"2512.17008\"\n    category: direct-competitor\n    role: competitor\n    relevance_note: >\n      [NEW-0517] Most direct competitor. Identifies \"uniform advantage\" problem in\n      step-independent GRPO (subset of our \"sign misattribution\"). Proposes turn-level\n      MDP + learned value function. Our differences: (1) more precise formalization\n      (sign misattribution + gamma decay quantification), (2) contrarian solution\n      (episode-level coarser credit vs their finer turn-level credit).\n\n  - id: gagpo2026\n    title: \"GAGPO: Generalized Advantage Grouped Policy Optimization\"\n    authors: \"Zhu et al.\"\n    venue: \"arXiv\"\n    year: 2026\n    arxiv_id: \"2605.13217\"\n    category: direct-competitor\n    role: competitor\n    relevance_note: >\n      [NEW-0517] Critic-free step-aligned credit via non-parametric grouped value proxy +\n      TD/GAE-style temporal advantages. ALFWorld 93.5% (1.5B), 95.6% (7B).\n      Pursues finer-grained credit to improve performance; our work diagnoses why\n      step-independent fails (sign misattribution) and shows coarser episode-level suffices.\n      Different contribution axis: performance optimization vs mechanism diagnosis.\n\n  - id: mt-grpo2025\n    title: \"Reinforcing Multi-Turn Reasoning in LLM Agents via Turn-Level Reward Design\"\n    authors: \"Wei et al.\"\n    venue: \"arXiv\"\n    year: 2025\n    arxiv_id: \"2505.11821\"\n    category: direct-competitor\n    role: competitor\n    relevance_note: >\n      [NEW-0517] Proposes MT-GRPO with turn-level reward design for multi-turn RL.\n      Evaluated on QA search tasks (NQ, TriviaQA, HotpotQA), not ALFWorld.\n      Qwen2.5-7B. Same direction as Turn-PPO (finer turn-level credit);\n      our contrarian shows coarser episode-level eliminates sign misattribution.\n\n  - id: istar2025\n    title: \"Agentic Reinforcement Learning with Implicit Step Rewards\"\n    authors: \"Liu et al.\"\n    venue: \"ICLR 2026\"\n    year: 2025\n    arxiv_id: \"2509.19199\"\n    category: direct-competitor\n    role: competitor\n    relevance_note: >\n      [NEW-0517] Implicit PRM + dual advantage (step + episode level) for agentic RL.\n      WebShop 86.5%, VisualSokoban 91.7%. ICLR 2026 published.\n      Learns step-level credit via implicit rewards without explicit labels;\n      our work shows episode-level alone suffices when sign misattribution is the bottleneck.\n      Validates that step-level credit helps, but doesn't diagnose when it hurts.\n\n  - id: archer2024\n    title: \"ArCHer: Training Language Model Agents via Hierarchical Multi-Turn RL\"\n    authors: \"Zhou, Zanette, Pan, Levine, Kumar\"\n    venue: \"ICML 2024\"\n    year: 2024\n    arxiv_id: \"2402.19446\"\n    category: method-component\n    role: predecessor\n    relevance_note: >\n      [NEW-0517] Foundational hierarchical multi-turn RL framework (ICML 2024).\n      High-level off-policy value RL (utterance-level) + low-level token policy.\n      ~100x sample efficiency. Establishes that multi-turn RL needs hierarchical structure;\n      our work specifically diagnoses why flat step-independent approaches fail.\n\n  - id: ca-survey2026\n    title: \"From Reasoning to Agentic: Credit Assignment in Reinforcement Learning for Large Language Models\"\n    authors: \"Zhang\"\n    venue: \"arXiv\"\n    year: 2026\n    arxiv_id: \"2604.09459\"\n    category: background\n    role: background\n    relevance_note: >\n      [NEW-0517] Comprehensive survey of 47 CA methods (2024-2026). Two-dimensional\n      taxonomy: granularity (token/segment/step/turn/multi-agent) x methodology\n      (MC/TD/model-based/game-theoretic/information-theoretic). Contextualizes our\n      sign misattribution diagnosis within the broader CA landscape.\n\n  - id: hiper2026\n    title: \"HiPER: Hierarchical Reinforcement Learning with Explicit Credit Assignment for Large Language Model Agents\"\n    authors: \"Peng et al.\"\n    venue: \"arXiv\"\n    year: 2026\n    arxiv_id: \"2602.16165\"\n    category: method-component\n    role: background\n    relevance_note: >\n      [NEW-0517] Hierarchical Plan-Execute RL. ALFWorld 97.4% (7B), 95.3% (1.5B).\n      GRPO baseline: 71.1% (1.5B), 85.4% (7B). 2.8x training efficiency gain.\n      Pursues SOTA performance via hierarchical plan-execute architecture;\n      our work does mechanism diagnosis of why step-independent GRPO fails.\n      Different contribution dimension: not comparable on performance axis.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "ca02f345-c5c1-474f-98f9-b51d23315472",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "7317ebb2-d910-42e9-95dc-fa8559b8ce74",
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
  "leafUuid": "3b6e44f0-4667-4397-9f08-ec17e956fedf",
  "sessionId": "7317ebb2-d910-42e9-95dc-fa8559b8ce74"
}
```

---

### Runtime record

_source line 40_

```json
{
  "type": "ai-title",
  "aiTitle": "Verify and correct Turn-PPO citation information",
  "sessionId": "7317ebb2-d910-42e9-95dc-fa8559b8ce74"
}
```

---

### Assistant

_source line 41 · 2026-05-17T13:46:36.855Z_

<details><summary>Logged reasoning block</summary>

```text
The file is already updated locally. The MCP `save_project_file` tool's whitelist only allows writing to `memory.md`, `writing_plan.yaml`, and `paper_framing.md`. Let me check - the tool description says:

"Writable: memory.md, writing_plan.yaml, paper_framing.md. Other files have dedicated tools"

So `literature_map.yaml` is not in the whitelist. But the local file has already been edited correctly. Let me try saving it via MCP anyway since the task requires it, and if it fails, the local file is already correct.


I've already modified the local file directly, so let me attempt the MCP save to see if it works despite the whitelist restriction.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3b6e44f0-4667-4397-9f08-ec17e956fedf",
  "isSidechain": false,
  "requestId": "req_011Cb8F5vFY4WD8LMHqw2Yj1",
  "type": "assistant",
  "uuid": "c774b5fa-c3cb-46e4-96f7-cd212458fe2d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "7317ebb2-d910-42e9-95dc-fa8559b8ce74",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EWJQsYP1RKbzk9qMsXvzMQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9498,
      "cache_read_input_tokens": 61323,
      "output_tokens": 9653,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9498,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 9653,
          "cache_read_input_tokens": 61323,
          "cache_creation_input_tokens": 9498,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9498
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

_source line 42 · 2026-05-17T13:49:12.684Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__save_project_file · `toolu_01BVkBdTmgJoomLhWMXpTN4c`</summary>

```json
{
  "project": "cost-verify-agent-rl",
  "file": "literature_map.yaml",
  "content": "# B-IAVR Literature Map\n# Updated: 2026-05-17\n# Categories: direct-competitor, method-component, background, evaluation\n# Roles: predecessor, competitor, baseline, evaluation, background\n\npapers:\n\n  # ============================================================\n  # Direction 1: Self-Verification / Self-Correction in LLM Agents\n  # ============================================================\n\n  - id: kamoi2024self-correction-survey\n    title: \"When Can LLMs Actually Correct Their Own Mistakes? A Critical Survey of Self-Correction of LLMs\"\n    authors: \"Kamoi et al.\"\n    venue: \"arXiv\"\n    year: 2024\n    arxiv_id: \"2406.01297\"\n    category: background\n    role: background\n    relevance_note: >\n      Foundational survey establishing that pure intrinsic self-correction is unreliable.\n      Validates B-IAVR's use of grounded verification (environment re-observation) over prompted self-feedback.\n\n  - id: tie2025correctbench\n    title: \"Can LLMs Correct Themselves? A Benchmark of Self-Correction in LLMs\"\n    authors: \"Tie et al.\"\n    venue: \"NeurIPS 2025 Datasets & Benchmarks\"\n    year: 2025\n    arxiv_id: \"2510.16062\"\n    category: background\n    role: background\n    relevance_note: >\n      Benchmark showing self-correction has diminishing returns when applied uniformly.\n      Supports B-IAVR's selective verification design over blanket correction.\n\n  - id: self-verification-dilemma-2026\n    title: \"Self-Verification Dilemma: Experience-Driven Suppression of Overused Checking in LLM Reasoning\"\n    authors: \"Long et al.\"\n    venue: \"arXiv\"\n    year: 2026\n    arxiv_id: \"2602.03485\"\n    category: background\n    role: background\n    relevance_note: >\n      Empirically validates that >90% of self-verification is confirmatory, ~2% corrective.\n      Directly supports B-IAVR's core thesis that verification should be selective.\n      Their experience-pool approach is complementary to B-IAVR's action-change signal.\n\n  - id: zhang2025incentivize-self-verify\n    title: \"Incentivizing LLMs to Self-Verify Their Answers\"\n    authors: \"Zhang et al.\"\n    venue: \"arXiv\"\n    year: 2025\n    arxiv_id: \"2506.01369\"\n    category: background\n    role: background\n    relevance_note: >\n      Unifies answer generation and verification via single RL training process.\n      Parallel to B-IAVR: they train verification into generation; B-IAVR trains when to trigger separate verification.\n\n  - id: mar2025\n    title: \"MAR: Multi-Agent Reflexion Improves Reasoning Abilities in LLMs\"\n    authors: \"Ozer et al.\"\n    venue: \"arXiv\"\n    year: 2025\n    arxiv_id: \"2512.20845\"\n    category: background\n    role: background\n    relevance_note: >\n      Multi-agent self-correction with diverse critic personas.\n      Complementary: MAR improves correction quality; B-IAVR decides when to trigger correction.\n\n  - id: ssr2025\n    title: \"SSR: Socratic Self-Refine for Large Language Model Reasoning\"\n    authors: \"Shi et al.\"\n    venue: \"arXiv\"\n    year: 2025\n    arxiv_id: \"2511.10621\"\n    category: background\n    role: background\n    relevance_note: >\n      Structured Socratic questioning for self-refinement.\n      Complementary: improves correction step quality; B-IAVR focuses on when to invoke correction.\n\n  - id: verifiagent2025\n    title: \"VerifiAgent: a Unified Verification Agent in Language Model Reasoning\"\n    authors: \"Han et al.\"\n    venue: \"EMNLP 2025 Findings\"\n    year: 2025\n    arxiv_id: \"2504.00406\"\n    category: background\n    role: background\n    relevance_note: >\n      Unified verification agent with meta-verification + tool-based adaptive verification.\n      Focuses on how to verify (tool selection); B-IAVR focuses on when to verify (policy learning).\n      Complementary: VerifiAgent's verification quality could enhance B-IAVR's verification step.\n\n  # ============================================================\n  # Direction 2: Agent RL Training\n  # ============================================================\n\n  - id: feng2025gigpo\n    title: \"GiGPO: Group-in-Group Policy Optimization for LLM Agent Training\"\n    authors: \"Feng et al.\"\n    venue: \"NeurIPS 2025\"\n    year: 2025\n    arxiv_id: \"2505.10978\"\n    category: method-component\n    role: predecessor\n    relevance_note: >\n      Core training algorithm for B-IAVR. Nested group structure provides step-level credit\n      assignment without learned critic. >12% over GRPO on ALFWorld, >9% on WebShop.\n\n  - id: selfguide2026\n    title: \"Co-Evolution of Policy and Internal Reward for Language Agents (Self-Guide)\"\n    authors: \"Wang et al.\"\n    venue: \"arXiv\"\n    year: 2026\n    arxiv_id: \"2604.03098\"\n    category: method-component\n    role: predecessor\n    relevance_note: >\n      Direct predecessor. B-IAVR extends Self-Guide's co-evolving internal reward.\n      The self-guidance signal is the foundation for action-change detection triggering verification.\n      8% improvement over env-reward-only on ALFWorld with Qwen3-1.7B/4B.\n\n  - id: spear2025\n    title: \"Learn the Ropes, Then Trust the Wins: Self-imitation with Progressive Exploration for Agentic Reinforcement Learning\"\n    authors: \"Qin et al.\"\n    venue: \"ICLR 2026\"\n    year: 2025\n    arxiv_id: \"2509.22601\"\n    category: method-component\n    role: background\n    relevance_note: >\n      Curriculum-based self-imitation for sparse-reward agent tasks.\n      Up to +16.1% on ALFWorld over GRPO. Self-imitation curriculum could augment B-IAVR training.\n\n  - id: wei2025webagent-r1\n    title: \"WebAgent-R1: Training Web Agents via End-to-End Multi-Turn RL\"\n    authors: \"Wei et al.\"\n    venue: \"EMNLP 2025\"\n    year: 2025\n    arxiv_id: \"2505.16421\"\n    category: background\n    role: background\n    relevance_note: >\n      Extends GRPO to multi-turn (M-GRPO) with dynamic context compression.\n      Qwen-2.5-3B: 6.1% to 33.9% on WebArena-Lite. M-GRPO multi-turn extension relevant to B-IAVR.\n\n  - id: dapo2025\n    title: \"DAPO: An Open-Source LLM Reinforcement Learning System at Scale\"\n    authors: \"Yu et al.\"\n    venue: \"arXiv\"\n    year: 2025\n    arxiv_id: \"2503.14476\"\n    category: method-component\n    role: background\n    relevance_note: >\n      RL training stabilization techniques (Clip-Higher, Dynamic Sampling).\n      Applicable to B-IAVR's RL training to prevent entropy collapse.\n\n  - id: digiRL2024\n    title: \"DigiRL: Training In-The-Wild Device-Control Agents with Autonomous RL\"\n    authors: \"Bai et al.\"\n    venue: \"NeurIPS 2024\"\n    year: 2024\n    arxiv_id: \"2406.11896\"\n    category: background\n    role: background\n    relevance_note: >\n      Online RL for device control agents. Demonstrates online RL viability for interactive agents.\n      49.5% absolute improvement over SFT. Parallel approach to B-IAVR in text-based setting.\n\n  - id: li2025sorl\n    title: \"SORL: Stabilizing Off-Policy RL for Long-Horizon Agent Training\"\n    authors: \"Li et al.\"\n    venue: \"arXiv\"\n    year: 2025\n    arxiv_id: \"2511.20718\"\n    category: method-component\n    role: background\n    relevance_note: >\n      Turn-level importance sampling + clipping-triggered normalization for stable multi-turn agent RL.\n      Directly applicable to B-IAVR's multi-turn ALFWorld training stability.\n\n  - id: agentic-rl-survey-2025\n    title: \"The Landscape of Agentic Reinforcement Learning for LLMs: A Survey\"\n    authors: \"Zhang et al.\"\n    venue: \"TMLR 2026\"\n    year: 2025\n    arxiv_id: \"2509.02547\"\n    category: background\n    role: background\n    relevance_note: >\n      Comprehensive survey formalizing agentic RL. Contextualizes B-IAVR as training agents\n      to make meta-decisions (when to verify) via RL within the POMDP framework.\n\n  - id: skillmaster2026\n    title: \"SkillMaster: Toward Autonomous Skill Mastery in LLM Agents\"\n    authors: \"Yang et al.\"\n    venue: \"arXiv\"\n    year: 2026\n    arxiv_id: \"2605.08693\"\n    category: method-component\n    role: background\n    relevance_note: >\n      DualAdv-GRPO: separately estimates advantages for task-solving and skill-editing decisions.\n      +8.8% on ALFWorld, +9.3% on WebShop. DualAdv structure could inform B-IAVR's\n      separation of action and verification advantages.\n\n  - id: t2po2026\n    title: \"T2PO: Uncertainty-Guided Exploration Control for Stable Multi-Turn Agentic RL\"\n    authors: \"Wang et al.\"\n    venue: \"ICML 2026 Spotlight\"\n    year: 2026\n    arxiv_id: \"2605.02178\"\n    category: method-component\n    role: background\n    relevance_note: >\n      Token- and turn-level uncertainty monitoring for stable multi-turn agent RL.\n      Triggers thinking intervention when marginal uncertainty change drops below threshold.\n      Evaluated on ALFWorld and WebShop. Conceptually related: uncertainty-based trigger vs\n      B-IAVR's action-change trigger, but T2PO targets training stability, not deployment verification.\n\n  - id: gvpo2026\n    title: \"GVPO: Group Verification-based Policy Optimization for Interactive Coding Agents\"\n    authors: \"Dai et al.\"\n    venue: \"ICLR 2026\"\n    year: 2026\n    arxiv_id: null  # no arXiv preprint; OpenReview ID: RY47Tq0VsV\n    category: method-component\n    role: background\n    relevance_note: >\n      Advantage shaping with outcome-verifiable + process-verifiable signals.\n      +12.7% over o1 on AppWorld. Integrates intermediate execution feedback as step-level\n      verification signals. Different focus: uses verification for credit assignment during\n      training; B-IAVR learns when to invoke verification at deployment.\n\n  - id: agentv-rl2026\n    title: \"AgentV-RL: Scaling Reward Modeling with Agentic Verifier\"\n    authors: \"Zhang et al.\"\n    venue: \"arXiv\"\n    year: 2026\n    arxiv_id: \"2604.16004\"\n    category: method-component\n    role: background\n    relevance_note: >\n      Bidirectional forward/backward agentic verifier for reward modeling in RL.\n      4B model surpasses SOTA ORMs by 25.2%. Addresses verification quality in reward modeling;\n      B-IAVR addresses verification timing in agent deployment. Complementary.\n\n  - id: pa-moe2026\n    title: \"PA-MoE: Phase-Aware Mixture of Experts for Agentic Reinforcement Learning\"\n    authors: \"Li et al.\"\n    venue: \"arXiv\"\n    year: 2026\n    arxiv_id: \"2602.17038\"\n    category: evaluation\n    role: baseline\n    relevance_note: >\n      [NEW-0516] Lightweight phase router learns latent phase boundaries from RL objective.\n      PA-MoE+GiGPO with Qwen2.5-1.5B achieves 93.8% on ALFWorld (+7.7 over GiGPO 86.1%).\n      1.5B outperforms vanilla 7B GiGPO (90.2%). New small-model SOTA on ALFWorld.\n      Orthogonal architecture innovation; important baseline to cite.\n\n  - id: sdar2026\n    title: \"SDAR: Self-Distilled Agentic Reinforcement Learning\"\n    authors: \"Lu et al.\"\n    venue: \"arXiv\"\n    year: 2026\n    arxiv_id: \"2605.15155\"\n    category: method-component\n    role: background\n    relevance_note: >\n      [NEW-0516] On-policy self-distillation as gated auxiliary objective during RL training.\n      Token-level gate decides supervision intensity. +9.4% over GRPO on ALFWorld.\n      Complementary: SDAR improves RL training; B-IAVR learns verification policy.\n\n  - id: hcapo2026\n    title: \"HCAPO: Hindsight Credit Assignment for Long-Horizon LLM Agents\"\n    authors: \"Tan et al.\"\n    venue: \"arXiv\"\n    year: 2026\n    arxiv_id: \"2603.08754\"\n    category: method-component\n    role: background\n    relevance_note: >\n      [NEW-0516] LLM-as-critic refines step-level Q-values via hindsight reasoning +\n      multi-scale advantage for critical decision states.\n      +13.8% on ALFWorld, +7.7% on WebShop over GRPO (Qwen2.5-7B).\n      Could improve B-IAVR's reward signal for verification decision steps.\n\n  - id: act2026\n    title: \"ACT: Agentic Critical Training\"\n    authors: \"Liu et al.\"\n    venue: \"arXiv\"\n    year: 2026\n    arxiv_id: \"2603.08706\"\n    category: method-component\n    role: background\n    relevance_note: >\n      [NEW-0516] Trains agents to judge action quality via critical comparison reward.\n      +5.07 over IL, +4.62 over RL. Different axis: ACT improves reflection quality;\n      B-IAVR decides when to reflect.\n\n  - id: rwml2026\n    title: \"RWML: Reinforcement World Model Learning for LLM-based Agents\"\n    authors: \"Yu et al.\"\n    venue: \"arXiv\"\n    year: 2026\n    arxiv_id: \"2602.05842\"\n    category: method-component\n    role: background\n    relevance_note: >\n      [NEW-0516] Self-supervised world model via sim-to-real gap rewards in embedding space.\n      +6.9 on ALFWorld over task-success-only RL. Matches expert-data training.\n      Orthogonal: improves internal world model; B-IAVR adds selective verification.\n\n  - id: skill0-2026\n    title: \"SKILL0: In-Context Agentic Reinforcement Learning for Skill Internalization\"\n    authors: \"Lu et al.\"\n    venue: \"arXiv\"\n    year: 2026\n    arxiv_id: \"2604.02268\"\n    category: method-component\n    role: background\n    relevance_note: >\n      [NEW-0516] Training-time curriculum progressively withdraws skill context until zero-shot.\n      +9.7% on ALFWorld over GRPO, <0.5k tokens per step.\n      Complementary: SKILL0 internalizes skills; B-IAVR adds selective verification.\n\n  - id: fission-grpo2026\n    title: \"Fission-GRPO: Robust Tool Use via Learning to Recover from Execution Errors\"\n    authors: \"Zhang et al.\"\n    venue: \"arXiv\"\n    year: 2026\n    arxiv_id: \"2601.15625\"\n    category: method-component\n    role: background\n    relevance_note: >\n      [NEW-0516] Fissions failed trajectories into recovery training instances.\n      +4% overall accuracy on BFCL v4 Multi-Turn over GRPO.\n      Related: error recovery after failure vs B-IAVR's proactive verification.\n\n  - id: selfbudgeter2026\n    title: \"SelfBudgeter: Adaptive Token Allocation for Efficient LLM Reasoning\"\n    authors: \"Li et al.\"\n    venue: \"ICLR 2026 (under review)\"\n    year: 2025\n    arxiv_id: \"2505.11274\"\n    category: background\n    role: background\n    relevance_note: >\n      [NEW-0516] Self-estimated token budgets + budget-guided GRPO. 61% token reduction.\n      Parallel concept: SelfBudgeter allocates computation budget;\n      B-IAVR makes binary verify/not-verify decision. Both use RL for adaptive compute.\n\n  - id: cove2026\n    title: \"CoVe: Training Interactive Tool-Use Agents via Constraint-Guided Verification\"\n    authors: \"Chen et al.\"\n    venue: \"arXiv\"\n    year: 2026\n    arxiv_id: \"2603.01940\"\n    category: background\n    role: background\n    relevance_note: >\n      [NEW-0516] Task constraints guide trajectory generation and serve as deterministic verifiers.\n      Different: CoVe uses verification for data synthesis; B-IAVR learns when to verify at inference.\n\n  # ============================================================\n  # Direction 3: Selective Verification / Adaptive Computation\n  # ============================================================\n\n  - id: wan2025derailer-rerailer\n    title: \"Derailer-Rerailer: Adaptive Verification for Efficient and Reliable LM Reasoning\"\n    authors: \"Wan et al.\"\n    venue: \"ACL 2025 Findings\"\n    year: 2025\n    arxiv_id: \"2408.13940\"\n    category: direct-competitor\n    role: competitor\n    relevance_note: >\n      Most directly related competitor. Both do selective verification with binary trigger.\n      Key difference: operates on reasoning chains (single-turn); B-IAVR on agent trajectories (multi-turn).\n      Uses heuristic instability signal; B-IAVR uses RL-trained action-change signal.\n      8-11% accuracy gain, 2-3x efficiency over uniform verification.\n\n  - id: sherlock2025\n    title: \"Sherlock: Reliable and Efficient Agentic Workflow Execution\"\n    authors: \"Microsoft\"\n    venue: \"arXiv\"\n    year: 2025\n    arxiv_id: \"2511.00330\"\n    category: direct-competitor\n    role: competitor\n    relevance_note: >\n      Selective verification for agentic workflows via offline counterfactual analysis + speculative execution.\n      Different scope: workflow DAG level (offline); B-IAVR is step-level (online RL).\n      18.3% accuracy gain, 26% cost reduction, 48.7% latency reduction.\n\n  - id: singhi2025when-to-verify\n    title: \"When To Solve, When To Verify: Compute-Optimal Verification for LLM Reasoning\"\n    authors: \"Singhi et al.\"\n    venue: \"arXiv\"\n    year: 2025\n    arxiv_id: \"2504.01005\"\n    category: background\n    role: background\n    relevance_note: >\n      Derives inference scaling laws for solve-vs-verify tradeoff.\n      Finding that over-verification is suboptimal directly supports B-IAVR's selective approach.\n      B-IAVR learns this allocation via RL rather than analytically.\n\n  - id: yang2026ares\n    title: \"ARES: Adaptive Reasoning Effort Selection for Efficient LLM Agents\"\n    authors: \"Yang et al.\"\n    venue: \"arXiv\"\n    year: 2026\n    arxiv_id: \"2603.07915\"\n    category: direct-competitor\n    role: competitor\n    relevance_note: >\n      Closest competitor in agent domain. Both train learned per-step compute allocation.\n      ARES uses SFT-initialized router further refined via GRPO with outcome + token efficiency reward;\n      B-IAVR trains binary verify/not-verify via RL with action-change signal.\n      Key differences: (1) reward signal — ARES optimizes token efficiency, B-IAVR uses action-change\n      as verification trigger; (2) data requirement — ARES needs difficulty-annotated training data\n      to bootstrap the router, B-IAVR learns from environment interaction alone.\n      Reduces reasoning tokens by up to 52.7%.\n\n  - id: tu2025autothink\n    title: \"Learning When to Think: Shaping Adaptive Reasoning in R1-Style Models via Multi-Stage RL\"\n    authors: \"Tu et al.\"\n    venue: \"NeurIPS 2025\"\n    year: 2025\n    arxiv_id: \"2505.10832\"\n    category: direct-competitor\n    role: competitor\n    relevance_note: >\n      Analogous idea in reasoning domain: RL-trained adaptive computation trigger.\n      Operates on single-turn reasoning; B-IAVR on multi-turn agent trajectories.\n      +6.4% accuracy, -52% tokens on DeepSeek-R1-Distill-Qwen-1.5B.\n\n  - id: du2025thinkless\n    title: \"Thinkless: LLM Learns When to Think\"\n    authors: \"Fang et al.\"\n    venue: \"NeurIPS 2025\"\n    year: 2025\n    arxiv_id: \"2505.13379\"\n    category: direct-competitor\n    role: competitor\n    relevance_note: >\n      RL-trained control token to decide when to invoke extended thinking.\n      Methodologically closest to B-IAVR in reasoning domain; B-IAVR applies to interactive agent trajectories.\n\n  - id: wang2025efficient-agents\n    title: \"Efficient Agents: Building Effective Agents While Reducing Cost\"\n    authors: \"Wang et al.\"\n    venue: \"arXiv\"\n    year: 2025\n    arxiv_id: \"2508.02694\"\n    category: background\n    role: background\n    relevance_note: >\n      First systematic study of agent efficiency-effectiveness tradeoff.\n      Framework-level cost reduction; B-IAVR addresses cost at verification-policy level.\n      Retains 96.7% performance with 28.4% cost-of-pass improvement.\n\n  - id: venktesh2025trust-but-verify\n    title: \"Trust but Verify! A Survey on Verification Design for Test-time Scaling\"\n    authors: \"Venktesh et al.\"\n    venue: \"arXiv\"\n    year: 2025\n    arxiv_id: \"2508.16665\"\n    category: background\n    role: background\n    relevance_note: >\n      Survey of verification approaches for test-time compute scaling.\n      Identifies verification timing as key open problem. B-IAVR provides concrete solution for agent setting.\n\n  - id: agent-omit2026\n    title: \"Agent-Omit: Training Efficient LLM Agents for Adaptive Thought and Observation Omission via Agentic RL\"\n    authors: \"Ning et al.\"\n    venue: \"ICML 2026\"\n    year: 2026\n    arxiv_id: \"2602.04284\"\n    category: direct-competitor\n    role: competitor\n    relevance_note: >\n      RL-trained policy for adaptive omission of redundant thoughts and observations.\n      Agent-Omit-8B matches frontier agents with best efficiency tradeoff on 5 benchmarks.\n      Both use RL to learn cost-efficient agent behavior. Key difference: Agent-Omit subtracts\n      (omits unnecessary context); B-IAVR selectively adds (verification steps).\n      Opposite but complementary approaches to cost-efficiency. Potentially combinable.\n\n  - id: ava2026\n    title: \"Anytime Verified Agents: Adaptive Compute Allocation for Reliable LLM Reasoning under Budget Constraints\"\n    authors: \"Patel\"\n    venue: \"TMLR 2026\"\n    year: 2026\n    arxiv_id: null  # no arXiv preprint; OpenReview ID: JMDCMf7mlF\n    category: direct-competitor\n    role: competitor\n    relevance_note: >\n      Dynamic compute allocation across search, sampling, and verification under budget.\n      Uses calibrated uncertainty + value-of-information for selective verification cascades.\n      Evaluated on GSM8K/MATH/HotpotQA/HumanEval (reasoning), not interactive agents.\n      Key difference: analytical/heuristic allocation vs B-IAVR's RL-learned policy;\n      single-turn reasoning vs multi-turn agent trajectories.\n\n  - id: cast2026\n    title: \"CAST: Case-Based Calibration of Adaptive Reasoning and Execution for LLM Tool Use\"\n    authors: \"Pang et al.\"\n    venue: \"arXiv\"\n    year: 2026\n    arxiv_id: \"2605.15041\"\n    category: background\n    role: background\n    relevance_note: >\n      Historical execution cases calibrate reasoning depth for tool use.\n      Reduces reasoning length 26% with +5.85% accuracy on BFCLv2/ToolBench.\n      Related: adaptive reasoning depth; different: case-based calibration vs RL-learned policy.\n\n  - id: marginal-token-allocators2026\n    title: \"Agentic AI Systems Should Be Designed as Marginal Token Allocators\"\n    authors: \"Zhu\"\n    venue: \"arXiv\"\n    year: 2026\n    arxiv_id: \"2605.01214\"\n    category: background\n    role: background\n    relevance_note: >\n      Position paper framing agent cost-efficiency as marginal token allocation economics.\n      Identifies under-verification as systematic failure mode. Supports B-IAVR's framing\n      that verification decisions should reflect marginal cost-benefit analysis.\n\n  - id: argos2025\n    title: \"Argos: Multimodal RL with Adaptive Verifier for AI Agents\"\n    authors: \"Tan et al.\"\n    venue: \"arXiv (revised April 2026)\"\n    year: 2025\n    arxiv_id: \"2512.03438\"\n    category: background\n    role: background\n    relevance_note: >\n      Agentic verifier that adaptively selects scoring functions for multimodal RL training.\n      Different domain (multimodal/robotics). The adaptive verifier selection concept is\n      complementary: Argos adapts how to verify; B-IAVR adapts when to verify.\n\n  # ============================================================\n  # Direction 4: ALFWorld / Interactive Environment Benchmarks\n  # ============================================================\n\n  - id: kim2025reflact\n    title: \"ReflAct: World-Grounded Decision Making in LLM Agents via Goal-State Reflection\"\n    authors: \"Kim et al.\"\n    venue: \"EMNLP 2025\"\n    year: 2025\n    arxiv_id: \"2505.15182\"\n    category: evaluation\n    role: baseline\n    relevance_note: >\n      Prompting SOTA on ALFWorld at 93.3%. Replaces ReAct's next-action thinking with state-goal reflection.\n      B-IAVR addresses different axis (cost-efficiency) since ALFWorld accuracy is near saturation.\n\n  - id: choudhury2025agentprm\n    title: \"Process Reward Models for LLM Agents: Practical Framework and Directions\"\n    authors: \"Choudhury\"\n    venue: \"arXiv\"\n    year: 2025\n    arxiv_id: \"2502.10325\"\n    category: evaluation\n    role: baseline\n    relevance_note: >\n      Monte Carlo rollout-based process reward for agent training. 3B models achieve 91% on ALFWorld.\n      Validates RL training approach; AgentPRM could serve as reward model for B-IAVR.\n\n  - id: xi2025agentprm\n    title: \"AgentPRM: Process Reward Models for LLM Agents via Step-Wise Promise and Progress\"\n    authors: \"Xi et al.\"\n    venue: \"ACM Web Conference 2026\"\n    year: 2025\n    arxiv_id: \"2511.08325\"\n    category: evaluation\n    role: baseline\n    relevance_note: >\n      Independent work from Choudhury et al., using TD-based estimation with GAE for scalable\n      PRM data labeling. 8x more compute-efficient than baselines with robust test-time scaling.\n      Different approach: Choudhury uses MC rollouts; Xi uses TD+GAE for step-wise promise and progress.\n\n  - id: xiang2024retrospex\n    title: \"Retrospex: Language Agent Meets Offline RL Critic\"\n    authors: \"Xiang et al.\"\n    venue: \"EMNLP 2024\"\n    year: 2024\n    arxiv_id: \"2505.11807\"\n    category: background\n    role: background\n    relevance_note: >\n      Offline RL Critic augments LLM agent action selection via dynamic rescoring.\n      Similar architecture could inform B-IAVR's verification value estimation.\n\n  - id: cfgm2025\n    title: \"CFGM: Coarse-to-Fine Grounded Memory for LLM Agent Planning\"\n    authors: \"Yang et al.\"\n    venue: \"EMNLP 2025\"\n    year: 2025\n    arxiv_id: \"2508.15305\"\n    category: background\n    role: background\n    relevance_note: >\n      Memory-augmented agent planning with episodic grounding.\n      ALFWorld +10.40%, WebShop +20%. Complementary to B-IAVR's verification approach.\n\n  - id: respact2024\n    title: \"ReSpAct: Harmonizing Reasoning, Speaking, and Acting\"\n    authors: \"Dongre et al.\"\n    venue: \"arXiv\"\n    year: 2024\n    arxiv_id: \"2411.00927\"\n    category: evaluation\n    role: baseline\n    relevance_note: >\n      Integrates dialogue/reasoning/acting. +6% over ReAct on ALFWorld.\n      Reduces invalid actions from 13% to 3%; B-IAVR's verification achieves error prevention differently.\n\n  # ============================================================\n  # Direction 5: Multi-Turn Credit Assignment (Direct Competitors)\n  # ============================================================\n\n  - id: turn-ppo2025\n    title: \"Turn-PPO: Turn-Level Advantage Estimation with PPO for Improved Multi-Turn RL in Agentic LLMs\"\n    authors: \"Li et al.\"\n    venue: \"arXiv\"\n    year: 2025\n    arxiv_id: \"2512.17008\"\n    category: direct-competitor\n    role: competitor\n    relevance_note: >\n      [NEW-0517] Most direct competitor. Identifies \"uniform advantage\" problem in\n      step-independent GRPO (subset of our \"sign misattribution\"). Proposes turn-level\n      MDP + learned value function. Our differences: (1) more precise formalization\n      (sign misattribution + gamma decay quantification), (2) contrarian solution\n      (episode-level coarser credit vs their finer turn-level credit).\n\n  - id: gagpo2026\n    title: \"GAGPO: Generalized Advantage Grouped Policy Optimization\"\n    authors: \"Zhu et al.\"\n    venue: \"arXiv\"\n    year: 2026\n    arxiv_id: \"2605.13217\"\n    category: direct-competitor\n    role: competitor\n    relevance_note: >\n      [NEW-0517] Critic-free step-aligned credit via non-parametric grouped value proxy +\n      TD/GAE-style temporal advantages. ALFWorld 93.5% (1.5B), 95.6% (7B).\n      Pursues finer-grained credit to improve performance; our work diagnoses why\n      step-independent fails (sign misattribution) and shows coarser episode-level suffices.\n      Different contribution axis: performance optimization vs mechanism diagnosis.\n\n  - id: mt-grpo2025\n    title: \"Reinforcing Multi-Turn Reasoning in LLM Agents via Turn-Level Reward Design\"\n    authors: \"Wei et al.\"\n    venue: \"arXiv\"\n    year: 2025\n    arxiv_id: \"2505.11821\"\n    category: direct-competitor\n    role: competitor\n    relevance_note: >\n      [NEW-0517] Proposes MT-GRPO with turn-level reward design for multi-turn RL.\n      Evaluated on QA search tasks (NQ, TriviaQA, HotpotQA), not ALFWorld.\n      Qwen2.5-7B. Same direction as Turn-PPO (finer turn-level credit);\n      our contrarian shows coarser episode-level eliminates sign misattribution.\n\n  - id: istar2025\n    title: \"Agentic Reinforcement Learning with Implicit Step Rewards\"\n    authors: \"Liu et al.\"\n    venue: \"ICLR 2026\"\n    year: 2025\n    arxiv_id: \"2509.19199\"\n    category: direct-competitor\n    role: competitor\n    relevance_note: >\n      [NEW-0517] Implicit PRM + dual advantage (step + episode level) for agentic RL.\n      WebShop 86.5%, VisualSokoban 91.7%. ICLR 2026 published.\n      Learns step-level credit via implicit rewards without explicit labels;\n      our work shows episode-level alone suffices when sign misattribution is the bottleneck.\n      Validates that step-level credit helps, but doesn't diagnose when it hurts.\n\n  - id: archer2024\n    title: \"ArCHer: Training Language Model Agents via Hierarchical Multi-Turn RL\"\n    authors: \"Zhou, Zanette, Pan, Levine, Kumar\"\n    venue: \"ICML 2024\"\n    year: 2024\n    arxiv_id: \"2402.19446\"\n    category: method-component\n    role: predecessor\n    relevance_note: >\n      [NEW-0517] Foundational hierarchical multi-turn RL framework (ICML 2024).\n      High-level off-policy value RL (utterance-level) + low-level token policy.\n      ~100x sample efficiency. Establishes that multi-turn RL needs hierarchical structure;\n      our work specifically diagnoses why flat step-independent approaches fail.\n\n  - id: ca-survey2026\n    title: \"From Reasoning to Agentic: Credit Assignment in Reinforcement Learning for Large Language Models\"\n    authors: \"Zhang\"\n    venue: \"arXiv\"\n    year: 2026\n    arxiv_id: \"2604.09459\"\n    category: background\n    role: background\n    relevance_note: >\n      [NEW-0517] Comprehensive survey of 47 CA methods (2024-2026). Two-dimensional\n      taxonomy: granularity (token/segment/step/turn/multi-agent) x methodology\n      (MC/TD/model-based/game-theoretic/information-theoretic). Contextualizes our\n      sign misattribution diagnosis within the broader CA landscape.\n\n  - id: hiper2026\n    title: \"HiPER: Hierarchical Reinforcement Learning with Explicit Credit Assignment for Large Language Model Agents\"\n    authors: \"Peng et al.\"\n    venue: \"arXiv\"\n    year: 2026\n    arxiv_id: \"2602.16165\"\n    category: method-component\n    role: background\n    relevance_note: >\n      [NEW-0517] Hierarchical Plan-Execute RL. ALFWorld 97.4% (7B), 95.3% (1.5B).\n      GRPO baseline: 71.1% (1.5B), 85.4% (7B). 2.8x training efficiency gain.\n      Pursues SOTA performance via hierarchical plan-execute architecture;\n      our work does mechanism diagnosis of why step-independent GRPO fails.\n      Different contribution dimension: not comparable on performance axis.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c774b5fa-c3cb-46e4-96f7-cd212458fe2d",
  "isSidechain": false,
  "requestId": "req_011Cb8F5vFY4WD8LMHqw2Yj1",
  "type": "assistant",
  "uuid": "d2796f8c-124c-4b9d-850f-d5aa0262a363",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "7317ebb2-d910-42e9-95dc-fa8559b8ce74",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EWJQsYP1RKbzk9qMsXvzMQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9498,
      "cache_read_input_tokens": 61323,
      "output_tokens": 9653,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9498,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 9653,
          "cache_read_input_tokens": 61323,
          "cache_creation_input_tokens": 9498,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9498
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

_source line 43 · 2026-05-17T13:49:12.705Z_

<details><summary>↩ Tool result · `toolu_01BVkBdTmgJoomLhWMXpTN4c`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"file 'literature_map.yaml' is not writable via save_project_file. Writable: ['memory.md', 'paper_framing.md', 'writing_plan.yaml'].\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d2796f8c-124c-4b9d-850f-d5aa0262a363",
  "isSidechain": false,
  "promptId": "71e953e0-39de-4d6a-a9b9-c8a649da7bce",
  "type": "user",
  "uuid": "3859acf7-9ecd-4157-a466-283f25c27a61",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"file 'literature_map.yaml' is not writable via save_project_file. Writable: ['memory.md', 'paper_framing.md', 'writing_plan.yaml'].\\\", \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"file 'literature_map.yaml' is not writable via save_project_file. Writable: ['memory.md', 'paper_framing.md', 'writing_plan.yaml'].\", \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "d2796f8c-124c-4b9d-850f-d5aa0262a363",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "7317ebb2-d910-42e9-95dc-fa8559b8ce74",
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
  "leafUuid": "3859acf7-9ecd-4157-a466-283f25c27a61",
  "sessionId": "7317ebb2-d910-42e9-95dc-fa8559b8ce74"
}
```

---

### Runtime record

_source line 45_

```json
{
  "type": "ai-title",
  "aiTitle": "Verify and correct Turn-PPO citation information",
  "sessionId": "7317ebb2-d910-42e9-95dc-fa8559b8ce74"
}
```

---

### Assistant

_source line 46 · 2026-05-17T13:49:21.355Z_

MCP 的 `save_project_file` 不支持写 `literature_map.yaml`，但本地文件已通过 Edit 工具直接修改完成。

## 修正结果

| 字段 | 旧值 | 新值 |
|------|------|------|
| title | Turn-Level Policy Optimization for Multi-Turn Agent Reinforcement Learning | **Turn-PPO: Turn-Level Advantage Estimation with PPO for Improved Multi-Turn RL in Agentic LLMs** |
| authors | Zhou et al. | **Li et al.** (Junbo Li, Peng Zhou, Rui Meng, Meet P. Vadera, Lihong Li, Yang Li) |
| venue | arXiv | arXiv (unchanged) |
| year | 2025 | 2025 (unchanged) |

关键修正：第一作者是 Junbo Li 而非 Zhou；标题包含 "Turn-PPO:" 前缀且措辞不同。文件已就地更新，其余条目未改动。

Sources:
- [arXiv 2512.17008](https://arxiv.org/abs/2512.17008)
- [HuggingFace Papers](https://huggingface.co/papers/2512.17008)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3859acf7-9ecd-4157-a466-283f25c27a61",
  "isSidechain": false,
  "requestId": "req_011Cb8FJB75mLjfBW1pjWHpu",
  "type": "assistant",
  "uuid": "81c893a3-a517-4d51-8b2e-816b33764f76",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "7317ebb2-d910-42e9-95dc-fa8559b8ce74",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J4cK8fprcibqQkSmstvw2R",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9740,
      "cache_read_input_tokens": 70821,
      "output_tokens": 337,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9740,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 337,
          "cache_read_input_tokens": 70821,
          "cache_creation_input_tokens": 9740,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9740
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

_source line 47_

```json
{
  "type": "last-prompt",
  "leafUuid": "81c893a3-a517-4d51-8b2e-816b33764f76",
  "sessionId": "7317ebb2-d910-42e9-95dc-fa8559b8ce74"
}
```

---

### Runtime record

_source line 48_

```json
{
  "type": "ai-title",
  "aiTitle": "Verify and correct Turn-PPO citation information",
  "sessionId": "7317ebb2-d910-42e9-95dc-fa8559b8ce74"
}
```

---
