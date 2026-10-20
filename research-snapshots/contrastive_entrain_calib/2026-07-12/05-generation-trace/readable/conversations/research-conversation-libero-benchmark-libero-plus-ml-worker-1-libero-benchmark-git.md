# Research conversation: 任务：调研 LIBERO Benchmark + LIBERO-Plus 评测 你是 ML 研究团队的调研 Worker。请深入调研以下内容，产出一份结构化报告。 ### 调研目标 1. **LIBERO Benchmark** - Git

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 31
- **Recorded user turns:** 1
- **Tool calls:** 6
- **Original source:** `logs/chats/exported-trajectories/account-1/2e86c8de-c2a5-4dae-af4d-f49fa73af83b.jsonl`
- **Structured JSON:** [`25785fb5c9933a75126c.json`](../../sessions/25/25785fb5c9933a75126c.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-15T11:11:42.940Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-15T11:11:42.940Z",
  "sessionId": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "content": "## 任务：调研 LIBERO Benchmark + LIBERO-Plus 评测\n\n你是 ML 研究团队的调研 Worker。请深入调研以下内容，产出一份结构化报告。\n\n### 调研目标\n\n1. **LIBERO Benchmark**\n   - GitHub repo 地址\n   - 安装方式（pip install 还是 from source）\n   - 5 个 task suites 的名称和内容（LIBERO-Spatial, LIBERO-Object, LIBERO-Goal, LIBERO-Long, LIBERO-90）\n   - 数据下载方式和大小（每个 suite 的 demo 数据）\n   - 数据格式（观测空间、动作空间的维度和含义）\n   - 评测脚本的使用方式（如何运行 evaluation，输出什么指标）\n\n2. **LIBERO-Plus 扰动评测**\n   - LIBERO-Plus 是什么（在 LIBERO 基础上增加了什么）\n   - GitHub repo 或论文来源\n   - 4 维扰动的具体定义：camera perturbation, lighting change, texture swap, sensor noise\n   - 安装和运行方式\n   - 如何与 LIBERO 标准评测配合使用\n\n3. **数据增强相关**\n   - LIBERO 环境是否内置随机化选项（camera jitter, color/lighting, background texture）\n   - 如果有，如何配置这些随机化\n   - 如果没有，LIBERO-Plus 的扰动实现方式是否可以复用为训练时的数据增强\n\n4. **与 LeRobot 的集成**\n   - LeRobot 是否原生支持 LIBERO 数据集\n   - 如果支持，数据集在 HuggingFace Hub 上的名称\n   - 数据转换流程（LIBERO 原始格式 → LeRobot 格式）\n\n### 调研方法\n- WebSearch 搜索 LIBERO benchmark 论文、GitHub repo\n- WebSearch 搜索 LIBERO-Plus 论文和代码\n- WebFetch 访问相关 GitHub repo 查看安装说明和关键文件\n- 搜索 HuggingFace Hub 上的 LIBERO 数据集\n\n### 产出\n将调研报告写入 `/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/action_cond_info_bottleneck/artifacts/research_libero_benchmark.md`\n\n报告必须包含：\n- 每个问题的具体答案\n- 安装命令和数据下载命令（可直接复制执行的）\n- 关键文件路径和 API 调用示例\n- 不确定的地方明确标注 [UNVERIFIED]\n"
}
```

---

### Runtime record

_source line 2 · 2026-05-15T11:11:42.944Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-15T11:11:42.944Z",
  "sessionId": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b"
}
```

---

## Round 1

29 recorded events

### User

_source line 3 · 2026-05-15T11:11:42.977Z_

## 任务：调研 LIBERO Benchmark + LIBERO-Plus 评测

你是 ML 研究团队的调研 Worker。请深入调研以下内容，产出一份结构化报告。

### 调研目标

1. **LIBERO Benchmark**
   - GitHub repo 地址
   - 安装方式（pip install 还是 from source）
   - 5 个 task suites 的名称和内容（LIBERO-Spatial, LIBERO-Object, LIBERO-Goal, LIBERO-Long, LIBERO-90）
   - 数据下载方式和大小（每个 suite 的 demo 数据）
   - 数据格式（观测空间、动作空间的维度和含义）
   - 评测脚本的使用方式（如何运行 evaluation，输出什么指标）

2. **LIBERO-Plus 扰动评测**
   - LIBERO-Plus 是什么（在 LIBERO 基础上增加了什么）
   - GitHub repo 或论文来源
   - 4 维扰动的具体定义：camera perturbation, lighting change, texture swap, sensor noise
   - 安装和运行方式
   - 如何与 LIBERO 标准评测配合使用

3. **数据增强相关**
   - LIBERO 环境是否内置随机化选项（camera jitter, color/lighting, background texture）
   - 如果有，如何配置这些随机化
   - 如果没有，LIBERO-Plus 的扰动实现方式是否可以复用为训练时的数据增强

4. **与 LeRobot 的集成**
   - LeRobot 是否原生支持 LIBERO 数据集
   - 如果支持，数据集在 HuggingFace Hub 上的名称
   - 数据转换流程（LIBERO 原始格式 → LeRobot 格式）

### 调研方法
- WebSearch 搜索 LIBERO benchmark 论文、GitHub repo
- WebSearch 搜索 LIBERO-Plus 论文和代码
- WebFetch 访问相关 GitHub repo 查看安装说明和关键文件
- 搜索 HuggingFace Hub 上的 LIBERO 数据集

### 产出
将调研报告写入 `/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/action_cond_info_bottleneck/artifacts/research_libero_benchmark.md`

报告必须包含：
- 每个问题的具体答案
- 安装命令和数据下载命令（可直接复制执行的）
- 关键文件路径和 API 调用示例
- 不确定的地方明确标注 [UNVERIFIED]


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "d2c42f79-e375-4b9b-b7c3-7e1496f88b5b",
  "type": "user",
  "uuid": "3da00984-9645-40a7-b0cd-82bc1dd3b9ef",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/action_cond_info_bottleneck",
  "sessionId": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-15T11:11:42.977Z_

```json
{
  "parentUuid": "3da00984-9645-40a7-b0cd-82bc1dd3b9ef",
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
  "uuid": "cd92fd5d-58ca-458e-a116-1b570c802102",
  "timestamp": "2026-05-15T11:11:42.977Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/action_cond_info_bottleneck",
  "sessionId": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-15T11:11:42.977Z_

```json
{
  "parentUuid": "cd92fd5d-58ca-458e-a116-1b570c802102",
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
  "uuid": "b6b50fe0-c0d5-4489-b8df-5184b11d7206",
  "timestamp": "2026-05-15T11:11:42.977Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/action_cond_info_bottleneck",
  "sessionId": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6 · 2026-05-15T11:11:42.977Z_

```json
{
  "parentUuid": "b6b50fe0-c0d5-4489-b8df-5184b11d7206",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "c4312104-f721-4f17-b201-eabcd865ce2a",
  "timestamp": "2026-05-15T11:11:42.977Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/action_cond_info_bottleneck",
  "sessionId": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
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
  "aiTitle": "Research LIBERO Benchmark and LIBERO-Plus evaluation",
  "sessionId": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b"
}
```

---

### Assistant

_source line 8 · 2026-05-15T11:11:45.786Z_

I'll research LIBERO Benchmark, LIBERO-Plus, and related topics in parallel using multiple agents.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c4312104-f721-4f17-b201-eabcd865ce2a",
  "isSidechain": false,
  "requestId": "req_011Cb4Ffm6JyCXDBpbjJr35A",
  "type": "assistant",
  "uuid": "a90e10fa-81df-4052-9617-3763a8fa3b10",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/action_cond_info_bottleneck",
  "sessionId": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NAU3tgzscA2UzDvFrTpVNL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11281,
      "cache_read_input_tokens": 11841,
      "output_tokens": 947,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11281,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 947,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11281,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11281
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

_source line 9 · 2026-05-15T11:11:49.706Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01HzxqFJcSQ9LxVeV3zrEHSz`</summary>

```json
{
  "description": "Research LIBERO Benchmark",
  "subagent_type": "general-purpose",
  "prompt": "Research the LIBERO Benchmark for robot manipulation. I need detailed information about:\n\n1. GitHub repo URL\n2. Installation method (pip or from source)\n3. The 5 task suites: LIBERO-Spatial, LIBERO-Object, LIBERO-Goal, LIBERO-Long, LIBERO-90 — what each contains\n4. Data download method and size for each suite\n5. Data format: observation space dimensions/meaning, action space dimensions/meaning\n6. Evaluation scripts: how to run evaluation, what metrics are output\n\nUse WebSearch to find the LIBERO benchmark paper and GitHub repo. Then use WebFetch to read the GitHub README, installation docs, and key source files to get specific details about data format, task suites, and evaluation.\n\nBe thorough — I need exact commands, file paths, and API details. Report everything you find in a structured format."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a90e10fa-81df-4052-9617-3763a8fa3b10",
  "isSidechain": false,
  "requestId": "req_011Cb4Ffm6JyCXDBpbjJr35A",
  "type": "assistant",
  "uuid": "e2518827-e059-43d9-b14a-18c346715d28",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/action_cond_info_bottleneck",
  "sessionId": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NAU3tgzscA2UzDvFrTpVNL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11281,
      "cache_read_input_tokens": 11841,
      "output_tokens": 947,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11281,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 947,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11281,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11281
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

_source line 10 · 2026-05-15T11:11:54.411Z_

<details open><summary>🔧 Tool call — Agent · `toolu_016hJaz9VaWPx61DxYHc9fM9`</summary>

```json
{
  "description": "Research LIBERO-Plus perturbation",
  "subagent_type": "general-purpose",
  "prompt": "Research LIBERO-Plus, which is a perturbation-based evaluation extension for the LIBERO benchmark in robot manipulation.\n\nI need to find:\n1. What LIBERO-Plus is — what it adds on top of LIBERO\n2. GitHub repo or paper source\n3. The 4 perturbation dimensions: camera perturbation, lighting change, texture swap, sensor noise — exact definitions\n4. Installation and running instructions\n5. How it integrates with standard LIBERO evaluation\n\nAlso research whether LIBERO's simulation environment has built-in randomization options (camera jitter, color/lighting changes, background texture randomization). If it does, how to configure them. If not, whether LIBERO-Plus perturbation implementations can be reused as training-time data augmentation.\n\nUse WebSearch to find papers and repos related to \"LIBERO-Plus\" or \"LIBERO perturbation evaluation\" or \"LIBERO robustness\". Then use WebFetch to read relevant GitHub repos and paper details.\n\nReport everything in structured format with exact commands and code paths where possible."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e2518827-e059-43d9-b14a-18c346715d28",
  "isSidechain": false,
  "requestId": "req_011Cb4Ffm6JyCXDBpbjJr35A",
  "type": "assistant",
  "uuid": "1d3a0bfe-fd61-442e-b494-7532786fad11",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/action_cond_info_bottleneck",
  "sessionId": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NAU3tgzscA2UzDvFrTpVNL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11281,
      "cache_read_input_tokens": 11841,
      "output_tokens": 947,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11281,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 947,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11281,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11281
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

_source line 11 · 2026-05-15T11:11:58.754Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01DvNbgBP79dBVtsQLdBJJGb`</summary>

```json
{
  "description": "Research LeRobot LIBERO integration",
  "subagent_type": "general-purpose",
  "prompt": "Research the integration between LeRobot (HuggingFace's robot learning framework) and the LIBERO benchmark.\n\nI need to find:\n1. Does LeRobot natively support LIBERO datasets?\n2. If yes, what are the dataset names on HuggingFace Hub?\n3. What is the data conversion pipeline from LIBERO's native HDF5 format to LeRobot format?\n4. Any conversion scripts or utilities available\n\nUse WebSearch to search for:\n- \"LeRobot LIBERO\" \n- \"lerobot libero dataset\"\n- HuggingFace Hub LIBERO datasets\n- \"lerobot convert libero\"\n\nThen use WebFetch to check:\n- The LeRobot GitHub repo for LIBERO-related code\n- HuggingFace Hub for LIBERO datasets in LeRobot format\n- Any conversion scripts or documentation\n\nReport everything in structured format with exact dataset names, commands, and code paths."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1d3a0bfe-fd61-442e-b494-7532786fad11",
  "isSidechain": false,
  "requestId": "req_011Cb4Ffm6JyCXDBpbjJr35A",
  "type": "assistant",
  "uuid": "bd377f1a-e349-420c-a437-30f04cb64faa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/action_cond_info_bottleneck",
  "sessionId": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NAU3tgzscA2UzDvFrTpVNL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11281,
      "cache_read_input_tokens": 11841,
      "output_tokens": 947,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11281,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 947,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11281,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11281
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

_source line 12 · 2026-05-15T11:14:16.729Z_

<details><summary>↩ Tool result · `toolu_01DvNbgBP79dBVtsQLdBJJGb`</summary>

````text


Here is the structured research report.

---

## 1. Does LeRobot Natively Support LIBERO?

**Yes.** LIBERO is a first-class benchmark in LeRobot. It is installed via:

```bash
pip install -e ".[libero]"
```

LeRobot provides native environment wrappers (`--env.type=libero`), official documentation at [huggingface.co/docs/lerobot/en/libero](https://huggingface.co/docs/lerobot/en/libero), and a dedicated fork of the LIBERO codebase at [github.com/huggingface/lerobot-libero](https://github.com/huggingface/lerobot-libero).

LIBERO covers **130 tasks** across **5 task suites**:

| Suite | CLI name | Tasks | Description |
|-------|----------|-------|-------------|
| LIBERO-Spatial | `libero_spatial` | 10 | Spatial relation reasoning |
| LIBERO-Object | `libero_object` | 10 | Object manipulation |
| LIBERO-Goal | `libero_goal` | 10 | Goal-conditioned tasks |
| LIBERO-90 | `libero_90` | 90 | Short-horizon tasks |
| LIBERO-Long | `libero_10` | 10 | Long-horizon tasks |

There is also **LIBERO-plus** (`--env.type=libero_plus`), a robustness extension with ~10,000 perturbed task variants across 7 dimensions (camera, lighting, layout, language, etc.).

---

## 2. Dataset Names on HuggingFace Hub

### Primary datasets (recommended for training)

| Dataset ID | Episodes | Tasks | Size | Notes |
|------------|----------|-------|------|-------|
| `HuggingFaceVLA/libero` | 148 | 10 | ~1.9 GB | Official preprocessed dataset, recommended by LeRobot docs |
| `lerobot/libero` | 1,693 | 40 | ~1.94 GB | All 4 standard suites combined (video format, AV1 codec) |
| `physical-intelligence/libero` | 147 | 10 | ~34.9 GB | PI's conversion, RLDS-origin, CC-BY-4.0 |
| `lerobot/libero_plus` | — | — | — | LIBERO-plus training data |

### Per-suite image datasets

| Dataset ID | Tasks | Episodes |
|------------|-------|----------|
| `lerobot/libero_10_image` | 10 | 148 |
| `lerobot/libero_object_image` | 10 | 454 |
| `lerobot/libero_spatial_image` | 10 | — |
| `lerobot/libero_goal_image` | 10 | — |

### Community datasets

| Dataset ID | Notes |
|------------|-------|
| `IPEC-COMMUNITY/libero_90_no_noops_lerobot` | LIBERO-90 with no-ops removed |

---

## 3. Data Format Mapping (LIBERO HDF5/RLDS to LeRobot)

### Observation/Action schema

| LIBERO Field | LeRobot Feature | Type | Shape |
|---|---|---|---|
| `observation["image"]` / `agentview_image` | `observation.images.image` | Video/Image | (256, 256, 3) |
| `observation["wrist_image"]` / `robot0_eye_in_hand_image` | `observation.images.image2` (or `.wrist_image`) | Video/Image | (256, 256, 3) |
| `observation["state"]` | `observation.state` | float32 | (8,) |
| `action` | `action` | float32 | (7,) |
| `language_instruction` | `task` (task_index) | string/int | — |

### LeRobot dataset metadata

- **robot_type**: `panda`
- **fps**: `10`
- **Video codec**: AV1, yuv420p (for video datasets)
- **Storage**: Parquet for tabular data + MP4 for video streams

### State vector (8-dim)
End-effector position (3) + axis-angle orientation (3) + gripper qpos (2)

### Action vector (7-dim)
6D end-effector delta + 1D gripper command. Range: `Box(-1, 1, shape=(7,))`

---

## 4. Conversion Scripts and Utilities

### A. Physical Intelligence's OpenPI conversion script (primary)

**Path**: [`Physical-Intelligence/openpi/examples/libero/convert_libero_data_to_lerobot.py`](https://github.com/Physical-Intelligence/openpi/blob/main/examples/libero/convert_libero_data_to_lerobot.py)

**Prerequisites**:
```bash
uv pip install tensorflow tensorflow_datasets
```

**Raw data source**: Download from `https://huggingface.co/datasets/openvla/modified_libero_rlds`

**Usage**:
```bash
uv run examples/libero/convert_libero_data_to_lerobot.py \
  --data_dir /path/to/your/data \
  --push_to_hub
```

**What it does**:
1. Reads 4 raw RLDS datasets: `libero_10_no_noops`, `libero_goal_no_noops`, `libero_object_no_noops`, `libero_spatial_no_noops`
2. Creates a `LeRobotDataset` with robot_type=panda, fps=10
3. Iterates episodes, calling `dataset.add_frame()` per step
4. Calls `dataset.save_episode()` per episode
5. Optionally pushes to HuggingFace Hub

**Processing time**: ~30 minutes.

**Key imports**:
```python
from lerobot.common.datasets.lerobot_dataset import LeRobotDataset
import tensorflow_datasets as tfds
```

### B. Generic HDF5 to LeRobot converter

**Repo**: [github.com/anarnuri/hdf5_to_lerobot_converter](https://github.com/anarnuri/hdf5_to_lerobot_converter)

Works with custom HDF5 formats including LIBERO's native format.

### C. Using pre-converted datasets (no conversion needed)

The simplest path is to use the already-converted datasets directly:

```python
from lerobot.common.datasets.lerobot_dataset import LeRobotDataset

dataset = LeRobotDataset("HuggingFaceVLA/libero")
# or
dataset = LeRobotDataset("lerobot/libero")
```

### D. Training command (end-to-end example)

```bash
lerobot-train \
  --policy.type=smolvla \
  --policy.repo_id=${HF_USER}/libero-test \
  --policy.load_vlm_weights=true \
  --dataset.repo_id=HuggingFaceVLA/libero \
  --env.type=libero \
  --env.task=libero_10 \
  --output_dir=./outputs/ \
  --steps=100000 \
  --batch_size=4 \
  --eval.batch_size=1 \
  --eval.n_episodes=1 \
  --eval_freq=1000
```

### E. Evaluation command

```bash
lerobot-eval \
  --policy.path="your-policy-id" \
  --env.type=libero \
  --env.task=libero_spatial,libero_object,libero_goal,libero_10 \
  --eval.batch_size=1 \
  --eval.n_episodes=10 \
  --env.max_parallel_tasks=1
```

---

## Key Takeaways for This Project

1. **No conversion work needed** if using the pre-converted `HuggingFaceVLA/libero` or `lerobot/libero` datasets.
2. If you need LIBERO-90 data specifically, it is NOT in the standard pre-converted datasets. You would need the OpenPI conversion script or the community `IPEC-COMMUNITY/libero_90_no_noops_lerobot` dataset.
3. The LeRobot LIBERO env wrapper handles MuJoCo simulation natively (Linux only, `MUJOCO_GL=egl` for headless).
4. Control modes: `relative` (default) vs `absolute` -- must match your policy's action parameterization.

Sources:
- [LeRobot LIBERO Documentation](https://huggingface.co/docs/lerobot/en/libero)
- [LeRobot LIBERO-plus Documentation](https://huggingface.co/docs/lerobot/main/libero_plus)
- [lerobot/libero dataset](https://huggingface.co/datasets/lerobot/libero)
- [HuggingFaceVLA/libero dataset](https://huggingface.co/datasets/HuggingFaceVLA/libero)
- [physical-intelligence/libero dataset](https://huggingface.co/datasets/physical-intelligence/libero)
- [OpenPI LIBERO conversion script](https://github.com/Physical-Intelligence/openpi/blob/main/examples/libero/convert_libero_data_to_lerobot.py)
- [huggingface/lerobot-libero fork](https://github.com/huggingface/lerobot-libero)
- [huggingface/lerobot main repo](https://github.com/huggingface/lerobot)
- [lerobot/libero_10_image](https://huggingface.co/datasets/lerobot/libero_10_image)
- [lerobot/libero_object_image](https://huggingface.co/datasets/lerobot/libero_object_image)
- [lerobot/libero_spatial_image](https://huggingface.co/datasets/lerobot/libero_spatial_image)
- [HDF5 to LeRobot converter](https://github.com/anarnuri/hdf5_to_lerobot_converter)

agentId: a1a91bef0d6739352 (use SendMessage with to: 'a1a91bef0d6739352' to continue this agent)
&lt;usage>total_tokens: 36471
tool_uses: 18
duration_ms: 137969&lt;/usage>
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "parentUuid": "bd377f1a-e349-420c-a437-30f04cb64faa",
  "isSidechain": false,
  "promptId": "d2c42f79-e375-4b9b-b7c3-7e1496f88b5b",
  "type": "user",
  "uuid": "7ced5aba-bb85-44c7-b518-7eed96e90e1d",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Research the integration between LeRobot (HuggingFace's robot learning framework) and the LIBERO benchmark.\n\nI need to find:\n1. Does LeRobot natively support LIBERO datasets?\n2. If yes, what are the dataset names on HuggingFace Hub?\n3. What is the data conversion pipeline from LIBERO's native HDF5 format to LeRobot format?\n4. Any conversion scripts or utilities available\n\nUse WebSearch to search for:\n- \"LeRobot LIBERO\" \n- \"lerobot libero dataset\"\n- HuggingFace Hub LIBERO datasets\n- \"lerobot convert libero\"\n\nThen use WebFetch to check:\n- The LeRobot GitHub repo for LIBERO-related code\n- HuggingFace Hub for LIBERO datasets in LeRobot format\n- Any conversion scripts or documentation\n\nReport everything in structured format with exact dataset names, commands, and code paths.",
    "agentId": "a1a91bef0d6739352",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "\n\nHere is the structured research report.\n\n---\n\n## 1. Does LeRobot Natively Support LIBERO?\n\n**Yes.** LIBERO is a first-class benchmark in LeRobot. It is installed via:\n\n```bash\npip install -e \".[libero]\"\n```\n\nLeRobot provides native environment wrappers (`--env.type=libero`), official documentation at [huggingface.co/docs/lerobot/en/libero](https://huggingface.co/docs/lerobot/en/libero), and a dedicated fork of the LIBERO codebase at [github.com/huggingface/lerobot-libero](https://github.com/huggingface/lerobot-libero).\n\nLIBERO covers **130 tasks** across **5 task suites**:\n\n| Suite | CLI name | Tasks | Description |\n|-------|----------|-------|-------------|\n| LIBERO-Spatial | `libero_spatial` | 10 | Spatial relation reasoning |\n| LIBERO-Object | `libero_object` | 10 | Object manipulation |\n| LIBERO-Goal | `libero_goal` | 10 | Goal-conditioned tasks |\n| LIBERO-90 | `libero_90` | 90 | Short-horizon tasks |\n| LIBERO-Long | `libero_10` | 10 | Long-horizon tasks |\n\nThere is also **LIBERO-plus** (`--env.type=libero_plus`), a robustness extension with ~10,000 perturbed task variants across 7 dimensions (camera, lighting, layout, language, etc.).\n\n---\n\n## 2. Dataset Names on HuggingFace Hub\n\n### Primary datasets (recommended for training)\n\n| Dataset ID | Episodes | Tasks | Size | Notes |\n|------------|----------|-------|------|-------|\n| `HuggingFaceVLA/libero` | 148 | 10 | ~1.9 GB | Official preprocessed dataset, recommended by LeRobot docs |\n| `lerobot/libero` | 1,693 | 40 | ~1.94 GB | All 4 standard suites combined (video format, AV1 codec) |\n| `physical-intelligence/libero` | 147 | 10 | ~34.9 GB | PI's conversion, RLDS-origin, CC-BY-4.0 |\n| `lerobot/libero_plus` | — | — | — | LIBERO-plus training data |\n\n### Per-suite image datasets\n\n| Dataset ID | Tasks | Episodes |\n|------------|-------|----------|\n| `lerobot/libero_10_image` | 10 | 148 |\n| `lerobot/libero_object_image` | 10 | 454 |\n| `lerobot/libero_spatial_image` | 10 | — |\n| `lerobot/libero_goal_image` | 10 | — |\n\n### Community datasets\n\n| Dataset ID | Notes |\n|------------|-------|\n| `IPEC-COMMUNITY/libero_90_no_noops_lerobot` | LIBERO-90 with no-ops removed |\n\n---\n\n## 3. Data Format Mapping (LIBERO HDF5/RLDS to LeRobot)\n\n### Observation/Action schema\n\n| LIBERO Field | LeRobot Feature | Type | Shape |\n|---|---|---|---|\n| `observation[\"image\"]` / `agentview_image` | `observation.images.image` | Video/Image | (256, 256, 3) |\n| `observation[\"wrist_image\"]` / `robot0_eye_in_hand_image` | `observation.images.image2` (or `.wrist_image`) | Video/Image | (256, 256, 3) |\n| `observation[\"state\"]` | `observation.state` | float32 | (8,) |\n| `action` | `action` | float32 | (7,) |\n| `language_instruction` | `task` (task_index) | string/int | — |\n\n### LeRobot dataset metadata\n\n- **robot_type**: `panda`\n- **fps**: `10`\n- **Video codec**: AV1, yuv420p (for video datasets)\n- **Storage**: Parquet for tabular data + MP4 for video streams\n\n### State vector (8-dim)\nEnd-effector position (3) + axis-angle orientation (3) + gripper qpos (2)\n\n### Action vector (7-dim)\n6D end-effector delta + 1D gripper command. Range: `Box(-1, 1, shape=(7,))`\n\n---\n\n## 4. Conversion Scripts and Utilities\n\n### A. Physical Intelligence's OpenPI conversion script (primary)\n\n**Path**: [`Physical-Intelligence/openpi/examples/libero/convert_libero_data_to_lerobot.py`](https://github.com/Physical-Intelligence/openpi/blob/main/examples/libero/convert_libero_data_to_lerobot.py)\n\n**Prerequisites**:\n```bash\nuv pip install tensorflow tensorflow_datasets\n```\n\n**Raw data source**: Download from `https://huggingface.co/datasets/openvla/modified_libero_rlds`\n\n**Usage**:\n```bash\nuv run examples/libero/convert_libero_data_to_lerobot.py \\\n  --data_dir /path/to/your/data \\\n  --push_to_hub\n```\n\n**What it does**:\n1. Reads 4 raw RLDS datasets: `libero_10_no_noops`, `libero_goal_no_noops`, `libero_object_no_noops`, `libero_spatial_no_noops`\n2. Creates a `LeRobotDataset` with robot_type=panda, fps=10\n3. Iterates episodes, calling `dataset.add_frame()` per step\n4. Calls `dataset.save_episode()` per episode\n5. Optionally pushes to HuggingFace Hub\n\n**Processing time**: ~30 minutes.\n\n**Key imports**:\n```python\nfrom lerobot.common.datasets.lerobot_dataset import LeRobotDataset\nimport tensorflow_datasets as tfds\n```\n\n### B. Generic HDF5 to LeRobot converter\n\n**Repo**: [github.com/anarnuri/hdf5_to_lerobot_converter](https://github.com/anarnuri/hdf5_to_lerobot_converter)\n\nWorks with custom HDF5 formats including LIBERO's native format.\n\n### C. Using pre-converted datasets (no conversion needed)\n\nThe simplest path is to use the already-converted datasets directly:\n\n```python\nfrom lerobot.common.datasets.lerobot_dataset import LeRobotDataset\n\ndataset = LeRobotDataset(\"HuggingFaceVLA/libero\")\n# or\ndataset = LeRobotDataset(\"lerobot/libero\")\n```\n\n### D. Training command (end-to-end example)\n\n```bash\nlerobot-train \\\n  --policy.type=smolvla \\\n  --policy.repo_id=${HF_USER}/libero-test \\\n  --policy.load_vlm_weights=true \\\n  --dataset.repo_id=HuggingFaceVLA/libero \\\n  --env.type=libero \\\n  --env.task=libero_10 \\\n  --output_dir=./outputs/ \\\n  --steps=100000 \\\n  --batch_size=4 \\\n  --eval.batch_size=1 \\\n  --eval.n_episodes=1 \\\n  --eval_freq=1000\n```\n\n### E. Evaluation command\n\n```bash\nlerobot-eval \\\n  --policy.path=\"your-policy-id\" \\\n  --env.type=libero \\\n  --env.task=libero_spatial,libero_object,libero_goal,libero_10 \\\n  --eval.batch_size=1 \\\n  --eval.n_episodes=10 \\\n  --env.max_parallel_tasks=1\n```\n\n---\n\n## Key Takeaways for This Project\n\n1. **No conversion work needed** if using the pre-converted `HuggingFaceVLA/libero` or `lerobot/libero` datasets.\n2. If you need LIBERO-90 data specifically, it is NOT in the standard pre-converted datasets. You would need the OpenPI conversion script or the community `IPEC-COMMUNITY/libero_90_no_noops_lerobot` dataset.\n3. The LeRobot LIBERO env wrapper handles MuJoCo simulation natively (Linux only, `MUJOCO_GL=egl` for headless).\n4. Control modes: `relative` (default) vs `absolute` -- must match your policy's action parameterization.\n\nSources:\n- [LeRobot LIBERO Documentation](https://huggingface.co/docs/lerobot/en/libero)\n- [LeRobot LIBERO-plus Documentation](https://huggingface.co/docs/lerobot/main/libero_plus)\n- [lerobot/libero dataset](https://huggingface.co/datasets/lerobot/libero)\n- [HuggingFaceVLA/libero dataset](https://huggingface.co/datasets/HuggingFaceVLA/libero)\n- [physical-intelligence/libero dataset](https://huggingface.co/datasets/physical-intelligence/libero)\n- [OpenPI LIBERO conversion script](https://github.com/Physical-Intelligence/openpi/blob/main/examples/libero/convert_libero_data_to_lerobot.py)\n- [huggingface/lerobot-libero fork](https://github.com/huggingface/lerobot-libero)\n- [huggingface/lerobot main repo](https://github.com/huggingface/lerobot)\n- [lerobot/libero_10_image](https://huggingface.co/datasets/lerobot/libero_10_image)\n- [lerobot/libero_object_image](https://huggingface.co/datasets/lerobot/libero_object_image)\n- [lerobot/libero_spatial_image](https://huggingface.co/datasets/lerobot/libero_spatial_image)\n- [HDF5 to LeRobot converter](https://github.com/anarnuri/hdf5_to_lerobot_converter)"
      }
    ],
    "totalDurationMs": 137969,
    "totalTokens": 36471,
    "totalToolUseCount": 18,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 305,
      "cache_read_input_tokens": 33565,
      "output_tokens": 2598,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 305
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2598,
          "cache_read_input_tokens": 33565,
          "cache_creation_input_tokens": 305,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 305,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 0,
      "searchCount": 0,
      "bashCount": 0,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 18
    }
  },
  "sourceToolAssistantUUID": "bd377f1a-e349-420c-a437-30f04cb64faa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/action_cond_info_bottleneck",
  "sessionId": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
````

</details>

---

### Runtime record

_source line 13_

```json
{
  "type": "last-prompt",
  "lastPrompt": "## 任务：调研 LIBERO Benchmark + LIBERO-Plus 评测  你是 ML 研究团队的调研 Worker。请深入调研以下内容，产出一份结构化报告。  ### 调研目标  1. **LIBERO Benchmark**    - GitHub repo 地址    - 安装方式（pip install 还是 from source）    - 5 个 task suites…",
  "leafUuid": "7ced5aba-bb85-44c7-b518-7eed96e90e1d",
  "sessionId": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b"
}
```

---

### Runtime record

_source line 14_

```json
{
  "type": "ai-title",
  "aiTitle": "Research LIBERO Benchmark and LIBERO-Plus evaluation",
  "sessionId": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b"
}
```

---

### Tool result

_source line 15 · 2026-05-15T11:14:56.862Z_

<details><summary>↩ Tool result · `toolu_016hJaz9VaWPx61DxYHc9fM9`</summary>

````text


Here is the structured research report.

---

## 1. What LIBERO-Plus Is

LIBERO-Plus is a robustness evaluation benchmark that extends the original LIBERO robot manipulation benchmark. It was published as "LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models" (arXiv:2510.13626, accepted at CVPR 2026).

**What it adds on top of LIBERO:**
- **10,030 task variants** generated by applying systematic perturbations to original LIBERO tasks
- **7 perturbation dimensions** with **21 sub-dimensions**
- **5 difficulty levels** (L1-L5) stratified by multi-model consensus (how many of 4 reference models solve the task)
- **20,000+ training trajectories** collected under varied conditions (stored in RLDS format)
- Drop-in replacement for vanilla LIBERO — same Python interface, same camera names, same observation/action format

## 2. Source

- **Paper:** [arXiv:2510.13626](https://arxiv.org/abs/2510.13626)
- **GitHub:** [github.com/sylvestf/LIBERO-plus](https://github.com/sylvestf/LIBERO-plus)
- **Project page:** [sylvestf.github.io/LIBERO-plus](https://sylvestf.github.io/LIBERO-plus/)
- **Assets (HuggingFace):** [Sylvest/LIBERO-plus](https://huggingface.co/datasets/Sylvest/LIBERO-plus)
- **Training dataset (RLDS):** [Sylvest/libero_plus_rlds](https://huggingface.co/datasets/Sylvest/libero_plus_rlds)
- **LeRobot-format dataset:** [lerobot/libero_plus](https://huggingface.co/datasets/lerobot/libero_plus)

## 3. The 7 Perturbation Dimensions (Exact Definitions)

Note: The user asked about 4 dimensions. LIBERO-Plus actually defines **7**, not 4.

### 3.1 Objects Layout (O1, O2)
- **O1 — Confounding objects:** Adds n additional unseen distractor objects into the scene from a pool of 416 objects, implemented by modifying BDDL task description files.
- **O2 — Target displacement:** Applies random perturbations to the target object's initial position (x, y, z) and orientation while preserving semantic relationships.

### 3.2 Camera Viewpoints (C1, C2, C3)
- **C1 — Distance scaling:** Scales camera distance from 1.01x to 2.00x the original value along the optical axis.
- **C2 — Spherical position:** Changes azimuth (delta-theta) and elevation (delta-phi) within 15 to 75 degree cones.
- **C3 — Orientation perturbation:** Perturbs yaw, pitch, roll within 2 to 10 degrees.

Implementation: Modifies the `Problem` class interface; parameters derived from task filenames. Targets the third-person camera primarily (not wrist camera).

### 3.3 Robot Initial States
- Applies random perturbations to the robot arm's initial joint positions with magnitudes 0.1 to 0.5.
- Implementation: Modifies the `Problem` class interface.

### 3.4 Language Instructions (R1, R2, R3)
- **R1 — Distraction rewrites:** Adds task-irrelevant contextual information.
- **R2 — Commonsense substitution:** Replaces object descriptions with commonsense-based alternatives.
- **R3 — Reasoning complexity:** Alters reasoning complexity for multi-step tasks.
- Implementation: LLM-based instruction rewriting.

### 3.5 Light Conditions (L1, L2, L3, L4)
- **L1 — Diffuse color:** RGB channel adjustment of diffuse lighting.
- **L2 — Direction:** Parallel light source direction changes.
- **L3 — Specular intensity:** Specular highlight intensity (reflective surfaces).
- **L4 — Shadow casting:** Boolean shadow on/off control.
- Implementation: Modifies MuJoCo scene XML definition files, registers new scene classes.

### 3.6 Background Textures (B1, B2)
- **B1 — Scene texture:** Changes the environment scene texture using 950 curated textures via XML scene files.
- **B2 — Surface texture:** Randomly alters working surface texture (tabletop, floor).
- Implementation: Modifies XML scene definition files with new texture assets.

### 3.7 Sensor Noise (N1-N5)
Applied as image-space post-processing (not physics-level):
- **N1 — Motion blur:** Kernel radius r=5-35, Gaussian sigma=2-20, angle theta in U(-45, 45) degrees.
- **N2 — Gaussian blur:** Sigma from 1 to 10.
- **N3 — Zoom blur:** Scaling factors [s_min, s_max, step] from [1, 1.11, 0.01] to [1, 1.56, 0.03].
- **N4 — Fog:** Density alpha=0.5-5.0, decay rate beta=1.3-3.0.
- **N5 — Glass blur:** Sigma=0.5-2.5, pixel displacement delta=1-5, iterations=1-3.

### Difficulty Levels (L1-L5)
Stratified by how many of 4 reference models (OpenVLA-OFT, pi0, pi0-fast, UniVLA) solve each task:
- L1: All 4 solve it. L2: 3 solve. L3: 2 solve. L4: 1 solves. L5: None solve.

## 4. Installation and Running

### Installation

```bash
# System dependencies
sudo apt install libexpat1 libfontconfig1-dev libmagickwand-dev

# Clone and install
git clone https://github.com/sylvestf/LIBERO-plus.git
cd LIBERO-plus
pip install -e .
pip install -r extra_requirements.txt

# If vanilla LIBERO was installed, uninstall first
pip uninstall -y hf-libero

# Set rendering backend
export MUJOCO_GL=egl
```

### Download assets

Download `assets.zip` from [HuggingFace](https://huggingface.co/datasets/Sylvest/LIBERO-plus/tree/main) and extract to `LIBERO-plus/libero/libero/assets/`.

Expected structure:
```
libero/libero/assets/
├── articulated_objects/
├── new_objects/
├── scenes/
├── stable_hope_objects/
├── stable_scanned_objects/
├── textures/
├── turbosquid_objects/
├── serving_region.xml
├── wall_frames.stl
└── wall.xml
```

### Configuration

Verify config at `/root/.libero/config.yaml`. Key change for evaluation: set `num_trials_per_task: 1` (instead of 50).

Task-to-perturbation-category mappings: `.libero/libero/benchmark/task_classification.json`.

### Evaluation via LeRobot

```bash
lerobot-eval \
  --policy.path="your-policy-id" \
  --env.type=libero_plus \
  --env.task=libero_spatial,libero_object,libero_goal,libero_10 \
  --eval.batch_size=1 \
  --eval.n_episodes=10 \
  --env.max_parallel_tasks=1
```

Observations: `observation.images.image` (agentview), `observation.images.image2` (wrist cam), `observation.state` (8-dim proprioception). Actions: `Box(-1, 1, shape=(7,))` — 6D EEF delta + 1D gripper. Control modes: `relative` (default) or `absolute`.

## 5. Integration with Standard LIBERO Evaluation

LIBERO-Plus is a **drop-in replacement** for vanilla LIBERO:
- Installs under the same `libero` Python package name (replaces it)
- Same `LiberoEnv` gym interface
- Same camera names (`agentview_image`, `robot0_eye_in_hand_image`)
- Same observation/action format
- Same task suite names (`libero_spatial`, `libero_object`, `libero_goal`, `libero_10`, `libero_90`)
- You can swap by doing `pip install -e .` in the LIBERO-plus repo without modifying evaluation code

**You cannot have both vanilla LIBERO and LIBERO-Plus installed simultaneously.** Switching back requires uninstalling the fork and reinstalling vanilla LIBERO.

## 6. LIBERO's Built-in Randomization (via robosuite)

LIBERO is built on **robosuite** (which uses MuJoCo). Robosuite **does** have built-in domain randomization via `DomainRandomizationWrapper` and three visual Modder classes. These are available to any robosuite-based environment, including LIBERO.

### DomainRandomizationWrapper

```python
from robosuite.wrappers import DomainRandomizationWrapper

env = DomainRandomizationWrapper(
    env=base_env,
    seed=42,
    randomize_color=True,        # Geom/texture color randomization
    randomize_camera=True,       # Camera position/orientation/FOV
    randomize_lighting=True,     # Light position/direction/color
    randomize_dynamics=True,     # Physics parameters
    randomize_on_reset=True,     # Randomize at episode reset
    randomize_every_n_steps=1,   # Frequency during rollout
    # Optional: pass detailed config dicts
    color_randomization_args={...},
    camera_randomization_args={...},
    lighting_randomization_args={...},
    dynamics_randomization_args={...},
)
```

### CameraModder (built-in)
- **Position** perturbation: default size 0.01
- **Rotation** perturbation (quaternion): default size 0.087 (~5 degrees)
- **FOV** perturbation: default size 5.0 degrees

### LightingModder (built-in)
- **Position** perturbation: default size 0.1
- **Direction** perturbation: default size 0.35
- **Specular** perturbation: default size 0.1
- **Ambient** perturbation: default size 0.1
- **Diffuse** perturbation: default size 0.1
- **Active** status: on/off toggle

### TextureModder (built-in)
- RGB color randomization (local interpolation 0.1)
- Texture patterns: RGB, checker, noise, gradient
- Material properties: reflectance, shininess, specular (local interpolation 0.2)
- Skybox randomization (optional)
- Note: For full effect, set all material RGBA to [1,1,1,1]

### Demo script
`robosuite/demos/demo_domain_randomization.py` showcases all modders.

## 7. Can LIBERO-Plus Perturbations Be Reused for Training-Time Augmentation?

**Yes, and the paper explicitly does this.** LIBERO-Plus provides both evaluation tasks AND a training dataset:

### What's already provided
- **22,400 training trajectories** (20,000+ after filtering) generated under varied perturbation conditions
- Breakdown: 2,400 with object layout variations + 4,000 each for light/camera/background/language/noise dimensions
- Stored in RLDS format, also available in LeRobot format at `lerobot/libero_plus`
- The paper shows that training with this diverse data ("mix-SFT") improves robustness — the OpenVLA-OFT+ model trained on this data achieves 79.6% average vs. much lower for vanilla-trained models

### Two paths for training-time augmentation

**Path A — Use LIBERO-Plus training data directly:**
```bash
lerobot-train \
    --policy.type=smolvla \
    --dataset.repo_id=lerobot/libero_plus \
    --env.type=libero_plus \
    ...
```

**Path B — Use robosuite's built-in DomainRandomizationWrapper for online augmentation during training:**
This covers camera jitter, lighting changes, texture/color randomization natively. Wrap the LIBERO environment:
```python
from robosuite.wrappers import DomainRandomizationWrapper
env = DomainRandomizationWrapper(env=libero_env, randomize_camera=True, randomize_lighting=True, randomize_color=True)
```

**Path C — Reuse LIBERO-Plus perturbation code for custom augmentation:**
- Lighting/texture perturbations: Modify scene XML files + register new scenes (same approach as LIBERO-Plus)
- Camera perturbations: Modify the `Problem` class interface
- Sensor noise (blur, fog, etc.): Image-space post-processing — trivially reusable as training-time augmentation since it's just image transforms applied after rendering

### Key distinction
- Robosuite's built-in randomization (Path B) is **online** — applies random perturbations every N steps during simulation. Good for training-time augmentation but less controllable.
- LIBERO-Plus perturbations (Path C) are **structured** with specific parameter ranges per sub-dimension and difficulty stratification. More suitable for systematic robustness training.
- Sensor noise (N1-N5) is pure image-space post-processing and can be applied as standard data augmentation on any stored trajectory without re-rendering.

### Paper's finding on augmentation effectiveness
Training strategies emphasizing diversity consistently yield more robust models. Models with wrist camera input show superior generalization. The paper demonstrates that combining perturbation-augmented training data with mix-SFT is the most effective approach.

---

Sources:
- [LIBERO-Plus paper (arXiv)](https://arxiv.org/abs/2510.13626)
- [LIBERO-Plus GitHub](https://github.com/sylvestf/LIBERO-plus)
- [LIBERO-Plus project page](https://sylvestf.github.io/LIBERO-plus/)
- [LIBERO-Plus HuggingFace dataset](https://huggingface.co/datasets/Sylvest/LIBERO-plus)
- [LIBERO-Plus LeRobot docs](https://huggingface.co/docs/lerobot/main/libero_plus)
- [robosuite Sim2Real / Domain Randomization](https://robosuite.ai/docs/algorithms/sim2real.html)
- [robosuite mjmod.py (Modder classes)](https://github.com/ARISE-Initiative/robosuite/blob/master/robosuite/utils/mjmod.py)
- [Original LIBERO repo](https://github.com/Lifelong-Robot-Learning/LIBERO)

agentId: aada8a30ff0506204 (use SendMessage with to: 'aada8a30ff0506204' to continue this agent)
&lt;usage>total_tokens: 37597
tool_uses: 20
duration_ms: 182445&lt;/usage>
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "parentUuid": "1d3a0bfe-fd61-442e-b494-7532786fad11",
  "isSidechain": false,
  "promptId": "d2c42f79-e375-4b9b-b7c3-7e1496f88b5b",
  "type": "user",
  "uuid": "c0629f71-11c2-4ab5-954b-9f543bc4cb23",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Research LIBERO-Plus, which is a perturbation-based evaluation extension for the LIBERO benchmark in robot manipulation.\n\nI need to find:\n1. What LIBERO-Plus is — what it adds on top of LIBERO\n2. GitHub repo or paper source\n3. The 4 perturbation dimensions: camera perturbation, lighting change, texture swap, sensor noise — exact definitions\n4. Installation and running instructions\n5. How it integrates with standard LIBERO evaluation\n\nAlso research whether LIBERO's simulation environment has built-in randomization options (camera jitter, color/lighting changes, background texture randomization). If it does, how to configure them. If not, whether LIBERO-Plus perturbation implementations can be reused as training-time data augmentation.\n\nUse WebSearch to find papers and repos related to \"LIBERO-Plus\" or \"LIBERO perturbation evaluation\" or \"LIBERO robustness\". Then use WebFetch to read relevant GitHub repos and paper details.\n\nReport everything in structured format with exact commands and code paths where possible.",
    "agentId": "aada8a30ff0506204",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "\n\nHere is the structured research report.\n\n---\n\n## 1. What LIBERO-Plus Is\n\nLIBERO-Plus is a robustness evaluation benchmark that extends the original LIBERO robot manipulation benchmark. It was published as \"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models\" (arXiv:2510.13626, accepted at CVPR 2026).\n\n**What it adds on top of LIBERO:**\n- **10,030 task variants** generated by applying systematic perturbations to original LIBERO tasks\n- **7 perturbation dimensions** with **21 sub-dimensions**\n- **5 difficulty levels** (L1-L5) stratified by multi-model consensus (how many of 4 reference models solve the task)\n- **20,000+ training trajectories** collected under varied conditions (stored in RLDS format)\n- Drop-in replacement for vanilla LIBERO — same Python interface, same camera names, same observation/action format\n\n## 2. Source\n\n- **Paper:** [arXiv:2510.13626](https://arxiv.org/abs/2510.13626)\n- **GitHub:** [github.com/sylvestf/LIBERO-plus](https://github.com/sylvestf/LIBERO-plus)\n- **Project page:** [sylvestf.github.io/LIBERO-plus](https://sylvestf.github.io/LIBERO-plus/)\n- **Assets (HuggingFace):** [Sylvest/LIBERO-plus](https://huggingface.co/datasets/Sylvest/LIBERO-plus)\n- **Training dataset (RLDS):** [Sylvest/libero_plus_rlds](https://huggingface.co/datasets/Sylvest/libero_plus_rlds)\n- **LeRobot-format dataset:** [lerobot/libero_plus](https://huggingface.co/datasets/lerobot/libero_plus)\n\n## 3. The 7 Perturbation Dimensions (Exact Definitions)\n\nNote: The user asked about 4 dimensions. LIBERO-Plus actually defines **7**, not 4.\n\n### 3.1 Objects Layout (O1, O2)\n- **O1 — Confounding objects:** Adds n additional unseen distractor objects into the scene from a pool of 416 objects, implemented by modifying BDDL task description files.\n- **O2 — Target displacement:** Applies random perturbations to the target object's initial position (x, y, z) and orientation while preserving semantic relationships.\n\n### 3.2 Camera Viewpoints (C1, C2, C3)\n- **C1 — Distance scaling:** Scales camera distance from 1.01x to 2.00x the original value along the optical axis.\n- **C2 — Spherical position:** Changes azimuth (delta-theta) and elevation (delta-phi) within 15 to 75 degree cones.\n- **C3 — Orientation perturbation:** Perturbs yaw, pitch, roll within 2 to 10 degrees.\n\nImplementation: Modifies the `Problem` class interface; parameters derived from task filenames. Targets the third-person camera primarily (not wrist camera).\n\n### 3.3 Robot Initial States\n- Applies random perturbations to the robot arm's initial joint positions with magnitudes 0.1 to 0.5.\n- Implementation: Modifies the `Problem` class interface.\n\n### 3.4 Language Instructions (R1, R2, R3)\n- **R1 — Distraction rewrites:** Adds task-irrelevant contextual information.\n- **R2 — Commonsense substitution:** Replaces object descriptions with commonsense-based alternatives.\n- **R3 — Reasoning complexity:** Alters reasoning complexity for multi-step tasks.\n- Implementation: LLM-based instruction rewriting.\n\n### 3.5 Light Conditions (L1, L2, L3, L4)\n- **L1 — Diffuse color:** RGB channel adjustment of diffuse lighting.\n- **L2 — Direction:** Parallel light source direction changes.\n- **L3 — Specular intensity:** Specular highlight intensity (reflective surfaces).\n- **L4 — Shadow casting:** Boolean shadow on/off control.\n- Implementation: Modifies MuJoCo scene XML definition files, registers new scene classes.\n\n### 3.6 Background Textures (B1, B2)\n- **B1 — Scene texture:** Changes the environment scene texture using 950 curated textures via XML scene files.\n- **B2 — Surface texture:** Randomly alters working surface texture (tabletop, floor).\n- Implementation: Modifies XML scene definition files with new texture assets.\n\n### 3.7 Sensor Noise (N1-N5)\nApplied as image-space post-processing (not physics-level):\n- **N1 — Motion blur:** Kernel radius r=5-35, Gaussian sigma=2-20, angle theta in U(-45, 45) degrees.\n- **N2 — Gaussian blur:** Sigma from 1 to 10.\n- **N3 — Zoom blur:** Scaling factors [s_min, s_max, step] from [1, 1.11, 0.01] to [1, 1.56, 0.03].\n- **N4 — Fog:** Density alpha=0.5-5.0, decay rate beta=1.3-3.0.\n- **N5 — Glass blur:** Sigma=0.5-2.5, pixel displacement delta=1-5, iterations=1-3.\n\n### Difficulty Levels (L1-L5)\nStratified by how many of 4 reference models (OpenVLA-OFT, pi0, pi0-fast, UniVLA) solve each task:\n- L1: All 4 solve it. L2: 3 solve. L3: 2 solve. L4: 1 solves. L5: None solve.\n\n## 4. Installation and Running\n\n### Installation\n\n```bash\n# System dependencies\nsudo apt install libexpat1 libfontconfig1-dev libmagickwand-dev\n\n# Clone and install\ngit clone https://github.com/sylvestf/LIBERO-plus.git\ncd LIBERO-plus\npip install -e .\npip install -r extra_requirements.txt\n\n# If vanilla LIBERO was installed, uninstall first\npip uninstall -y hf-libero\n\n# Set rendering backend\nexport MUJOCO_GL=egl\n```\n\n### Download assets\n\nDownload `assets.zip` from [HuggingFace](https://huggingface.co/datasets/Sylvest/LIBERO-plus/tree/main) and extract to `LIBERO-plus/libero/libero/assets/`.\n\nExpected structure:\n```\nlibero/libero/assets/\n├── articulated_objects/\n├── new_objects/\n├── scenes/\n├── stable_hope_objects/\n├── stable_scanned_objects/\n├── textures/\n├── turbosquid_objects/\n├── serving_region.xml\n├── wall_frames.stl\n└── wall.xml\n```\n\n### Configuration\n\nVerify config at `/root/.libero/config.yaml`. Key change for evaluation: set `num_trials_per_task: 1` (instead of 50).\n\nTask-to-perturbation-category mappings: `.libero/libero/benchmark/task_classification.json`.\n\n### Evaluation via LeRobot\n\n```bash\nlerobot-eval \\\n  --policy.path=\"your-policy-id\" \\\n  --env.type=libero_plus \\\n  --env.task=libero_spatial,libero_object,libero_goal,libero_10 \\\n  --eval.batch_size=1 \\\n  --eval.n_episodes=10 \\\n  --env.max_parallel_tasks=1\n```\n\nObservations: `observation.images.image` (agentview), `observation.images.image2` (wrist cam), `observation.state` (8-dim proprioception). Actions: `Box(-1, 1, shape=(7,))` — 6D EEF delta + 1D gripper. Control modes: `relative` (default) or `absolute`.\n\n## 5. Integration with Standard LIBERO Evaluation\n\nLIBERO-Plus is a **drop-in replacement** for vanilla LIBERO:\n- Installs under the same `libero` Python package name (replaces it)\n- Same `LiberoEnv` gym interface\n- Same camera names (`agentview_image`, `robot0_eye_in_hand_image`)\n- Same observation/action format\n- Same task suite names (`libero_spatial`, `libero_object`, `libero_goal`, `libero_10`, `libero_90`)\n- You can swap by doing `pip install -e .` in the LIBERO-plus repo without modifying evaluation code\n\n**You cannot have both vanilla LIBERO and LIBERO-Plus installed simultaneously.** Switching back requires uninstalling the fork and reinstalling vanilla LIBERO.\n\n## 6. LIBERO's Built-in Randomization (via robosuite)\n\nLIBERO is built on **robosuite** (which uses MuJoCo). Robosuite **does** have built-in domain randomization via `DomainRandomizationWrapper` and three visual Modder classes. These are available to any robosuite-based environment, including LIBERO.\n\n### DomainRandomizationWrapper\n\n```python\nfrom robosuite.wrappers import DomainRandomizationWrapper\n\nenv = DomainRandomizationWrapper(\n    env=base_env,\n    seed=42,\n    randomize_color=True,        # Geom/texture color randomization\n    randomize_camera=True,       # Camera position/orientation/FOV\n    randomize_lighting=True,     # Light position/direction/color\n    randomize_dynamics=True,     # Physics parameters\n    randomize_on_reset=True,     # Randomize at episode reset\n    randomize_every_n_steps=1,   # Frequency during rollout\n    # Optional: pass detailed config dicts\n    color_randomization_args={...},\n    camera_randomization_args={...},\n    lighting_randomization_args={...},\n    dynamics_randomization_args={...},\n)\n```\n\n### CameraModder (built-in)\n- **Position** perturbation: default size 0.01\n- **Rotation** perturbation (quaternion): default size 0.087 (~5 degrees)\n- **FOV** perturbation: default size 5.0 degrees\n\n### LightingModder (built-in)\n- **Position** perturbation: default size 0.1\n- **Direction** perturbation: default size 0.35\n- **Specular** perturbation: default size 0.1\n- **Ambient** perturbation: default size 0.1\n- **Diffuse** perturbation: default size 0.1\n- **Active** status: on/off toggle\n\n### TextureModder (built-in)\n- RGB color randomization (local interpolation 0.1)\n- Texture patterns: RGB, checker, noise, gradient\n- Material properties: reflectance, shininess, specular (local interpolation 0.2)\n- Skybox randomization (optional)\n- Note: For full effect, set all material RGBA to [1,1,1,1]\n\n### Demo script\n`robosuite/demos/demo_domain_randomization.py` showcases all modders.\n\n## 7. Can LIBERO-Plus Perturbations Be Reused for Training-Time Augmentation?\n\n**Yes, and the paper explicitly does this.** LIBERO-Plus provides both evaluation tasks AND a training dataset:\n\n### What's already provided\n- **22,400 training trajectories** (20,000+ after filtering) generated under varied perturbation conditions\n- Breakdown: 2,400 with object layout variations + 4,000 each for light/camera/background/language/noise dimensions\n- Stored in RLDS format, also available in LeRobot format at `lerobot/libero_plus`\n- The paper shows that training with this diverse data (\"mix-SFT\") improves robustness — the OpenVLA-OFT+ model trained on this data achieves 79.6% average vs. much lower for vanilla-trained models\n\n### Two paths for training-time augmentation\n\n**Path A — Use LIBERO-Plus training data directly:**\n```bash\nlerobot-train \\\n    --policy.type=smolvla \\\n    --dataset.repo_id=lerobot/libero_plus \\\n    --env.type=libero_plus \\\n    ...\n```\n\n**Path B — Use robosuite's built-in DomainRandomizationWrapper for online augmentation during training:**\nThis covers camera jitter, lighting changes, texture/color randomization natively. Wrap the LIBERO environment:\n```python\nfrom robosuite.wrappers import DomainRandomizationWrapper\nenv = DomainRandomizationWrapper(env=libero_env, randomize_camera=True, randomize_lighting=True, randomize_color=True)\n```\n\n**Path C — Reuse LIBERO-Plus perturbation code for custom augmentation:**\n- Lighting/texture perturbations: Modify scene XML files + register new scenes (same approach as LIBERO-Plus)\n- Camera perturbations: Modify the `Problem` class interface\n- Sensor noise (blur, fog, etc.): Image-space post-processing — trivially reusable as training-time augmentation since it's just image transforms applied after rendering\n\n### Key distinction\n- Robosuite's built-in randomization (Path B) is **online** — applies random perturbations every N steps during simulation. Good for training-time augmentation but less controllable.\n- LIBERO-Plus perturbations (Path C) are **structured** with specific parameter ranges per sub-dimension and difficulty stratification. More suitable for systematic robustness training.\n- Sensor noise (N1-N5) is pure image-space post-processing and can be applied as standard data augmentation on any stored trajectory without re-rendering.\n\n### Paper's finding on augmentation effectiveness\nTraining strategies emphasizing diversity consistently yield more robust models. Models with wrist camera input show superior generalization. The paper demonstrates that combining perturbation-augmented training data with mix-SFT is the most effective approach.\n\n---\n\nSources:\n- [LIBERO-Plus paper (arXiv)](https://arxiv.org/abs/2510.13626)\n- [LIBERO-Plus GitHub](https://github.com/sylvestf/LIBERO-plus)\n- [LIBERO-Plus project page](https://sylvestf.github.io/LIBERO-plus/)\n- [LIBERO-Plus HuggingFace dataset](https://huggingface.co/datasets/Sylvest/LIBERO-plus)\n- [LIBERO-Plus LeRobot docs](https://huggingface.co/docs/lerobot/main/libero_plus)\n- [robosuite Sim2Real / Domain Randomization](https://robosuite.ai/docs/algorithms/sim2real.html)\n- [robosuite mjmod.py (Modder classes)](https://github.com/ARISE-Initiative/robosuite/blob/master/robosuite/utils/mjmod.py)\n- [Original LIBERO repo](https://github.com/Lifelong-Robot-Learning/LIBERO)"
      }
    ],
    "totalDurationMs": 182445,
    "totalTokens": 37597,
    "totalToolUseCount": 20,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 379,
      "cache_read_input_tokens": 33443,
      "output_tokens": 3772,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 379
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 3772,
          "cache_read_input_tokens": 33443,
          "cache_creation_input_tokens": 379,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 379,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 0,
      "searchCount": 0,
      "bashCount": 0,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 20
    }
  },
  "sourceToolAssistantUUID": "1d3a0bfe-fd61-442e-b494-7532786fad11",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/action_cond_info_bottleneck",
  "sessionId": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
````

</details>

---

### Tool result

_source line 16 · 2026-05-15T11:15:32.422Z_

<details><summary>↩ Tool result · `toolu_01HzxqFJcSQ9LxVeV3zrEHSz`</summary>

````text
Now I have comprehensive information. Let me compile the final report.

---

## LIBERO Benchmark: Comprehensive Technical Reference

### 1. GitHub Repo URL

**Official:** https://github.com/Lifelong-Robot-Learning/LIBERO

**Paper:** [arXiv:2306.03310](https://arxiv.org/abs/2306.03310) (NeurIPS 2023 Datasets & Benchmarks)

**Project website:** https://libero-project.github.io

**HuggingFace fork (LeRobot integration):** https://github.com/huggingface/lerobot-libero

---

### 2. Installation

**Method A: pip (simplest)**
```bash
pip install libero
```
Current version: 0.1.1. Requires Python >= 3.

**Method B: From source (recommended for development)**
```bash
conda create -n libero python=3.8.13
conda activate libero
git clone https://github.com/Lifelong-Robot-Learning/LIBERO.git
cd LIBERO
pip install -r requirements.txt
pip install torch==1.11.0+cu113 torchvision==0.12.0+cu113 torchaudio==0.11.0 --extra-index-url https://download.pytorch.org/whl/cu113
pip install -e .
```

**Method C: Via LeRobot**
```bash
pip install -e ".[libero]"
```

Underlying simulator: **robosuite** (MuJoCo-based). For headless rendering: `export MUJOCO_GL=egl`.

Licenses: MIT (code), CC BY 4.0 (datasets).

---

### 3. The 5 Task Suites

All tasks are language-conditioned manipulation with a Franka Panda arm.

| Suite | CLI name | Tasks | Description |
|-------|----------|-------|-------------|
| **LIBERO-Spatial** | `libero_spatial` | 10 | Same goal (pick black bowl, place on plate) but bowl is in different spatial locations. Tests transfer of **spatial relationship knowledge**. |
| **LIBERO-Object** | `libero_object` | 10 | Same goal structure (pick X, place in basket) but with different objects (soup, cream cheese, ketchup, etc.). Tests transfer of **object knowledge**. |
| **LIBERO-Goal** | `libero_goal` | 10 | Same scene but different goals (open drawer, put bowl on stove, turn on stove, etc.). Tests transfer of **goal/procedural knowledge**. |
| **LIBERO-90** | `libero_90` | 90 | Short-horizon tasks from LIBERO-100. Entangled distribution shifts across spatial, object, and goal axes. Used for pretraining. |
| **LIBERO-Long** | `libero_10` | 10 | Long-horizon multi-step tasks from LIBERO-100. Used for downstream evaluation after pretraining on LIBERO-90. |

**LIBERO-Spatial example tasks** (all 10):
1. pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate
2. pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate
3. pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate
4. pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate
5. pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate
6. pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate
7. pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate
8. pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate
9. pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate
10. pick_up_the_black_bowl_on_the_wooden_cabinet_and_place_it_on_the_plate

**LIBERO-Object example tasks**: pick_up_the_{alphabet_soup, cream_cheese, salad_dressing, bbq_sauce, ketchup, tomato_sauce, butter, milk, chocolate_pudding, orange_juice}_and_place_it_in_the_basket

**LIBERO-Goal example tasks**: open_the_middle_drawer_of_the_cabinet, put_the_bowl_on_the_stove, put_the_wine_bottle_on_top_of_the_cabinet, open_the_top_drawer_and_put_the_bowl_inside, put_the_bowl_on_top_of_the_cabinet, push_the_plate_to_the_front_of_the_stove, put_the_cream_cheese_in_the_bowl, turn_on_the_stove, put_the_bowl_on_the_plate, put_the_wine_bottle_on_the_rack

---

### 4. Data Download

**50 human teleoperation demonstrations per task**, collected via SpaceMouse at 20 Hz.

**Method A: Official script**
```bash
# All datasets
python benchmark_scripts/download_libero_datasets.py

# Specific suite
python benchmark_scripts/download_libero_datasets.py --datasets libero_spatial
python benchmark_scripts/download_libero_datasets.py --datasets libero_object
python benchmark_scripts/download_libero_datasets.py --datasets libero_goal
python benchmark_scripts/download_libero_datasets.py --datasets libero_100  # contains both libero_90 and libero_10

# Via HuggingFace (recommended, original links may expire)
python benchmark_scripts/download_libero_datasets.py --use-huggingface
```
Default download location: `./datasets/` under the LIBERO root.

**Method B: HuggingFace direct**

Multiple HF dataset repos exist:
- Original HDF5: https://huggingface.co/datasets/yifengzhu-hf/LIBERO-datasets (~100 GB total)
- Physical Intelligence (LeRobot format): https://huggingface.co/datasets/physical-intelligence/libero (~34.9 GB, 4 suites, parquet)
- HuggingFace VLA (LeRobot format): https://huggingface.co/datasets/HuggingFaceVLA/libero

**Approximate sizes (original HDF5 format):**

| Suite | Approx Size |
|-------|-------------|
| libero_spatial | ~6.6 GB |
| libero_object | ~9.3 GB |
| libero_goal | ~6-9 GB |
| libero_10 (Long) | ~12.8 GB |
| libero_90 | ~60-70 GB |
| **Total** | **~100 GB** |

---

### 5. Data Format

**File format:** HDF5 (one `.hdf5` file per task)

**HDF5 structure:**
```
data/
  demo_0/
    obs/
      agentview_rgb          # (T, 128, 128, 3) uint8 — third-person camera
      eye_in_hand_rgb        # (T, 128, 128, 3) uint8 — wrist camera
      gripper_states         # (T, 1) — gripper aperture (from robot0_gripper_qpos)
      joint_states           # (T, 7) — 7 joint positions (from robot0_joint_pos)
      ee_states              # (T, 6) — end-effector position + axis-angle orientation
      ee_pos                 # (T, 3) — end-effector position
      ee_ori                 # (T, 3) — end-effector axis-angle orientation
    actions                  # (T, 7) — 7-DOF action
    states                   # (T, D) — full simulator state
    robot_states             # (T, D) — concatenation of gripper_pos, ee_pos, ee_quat
    rewards                  # (T,) — sparse: 0 everywhere, 1 at final success step
    dones                    # (T,) — 1 at episode end
  demo_1/
    ...
  demo_49/
    ...
```

**Observation space (used in default config):**

| Key | Dimension | Meaning |
|-----|-----------|---------|
| `agentview_rgb` (maps to `agentview_image`) | (128, 128, 3) | RGB from workspace camera |
| `eye_in_hand_rgb` (maps to `robot0_eye_in_hand_image`) | (128, 128, 3) | RGB from wrist-mounted camera |
| `gripper_states` (maps to `robot0_gripper_qpos`) | (1,) or (2,) | Gripper finger position(s) |
| `joint_states` (maps to `robot0_joint_pos`) | (7,) | 7 joint angles of the Franka Panda |
| `ee_pos` | (3,) | End-effector xyz position |
| `ee_ori` | (3,) | End-effector axis-angle orientation |

**In LeRobot format**, the proprioceptive state is an 8-dimensional vector: `observation.state` = [ee_pos (3) + ee_axis_angle (3) + gripper_qpos (2)] or [ee_pos (3) + ee_axis_angle (3) + gripper_qpos (1) + padding (1)].

**Action space:**

| Dimension | Meaning |
|-----------|---------|
| 0-2 | End-effector position delta (dx, dy, dz) |
| 3-5 | End-effector orientation delta (axis-angle or Euler) |
| 6 | Gripper command (1 = close, -1 = open) |

Total: **7-dimensional continuous**, Box(-1, 1, shape=(7,)). Control mode: **OSC_POSE** (Operational Space Control). Frequency: **20 Hz**. Supports both `relative` (delta, default) and `absolute` control modes.

**Reward:** Sparse — 0 for all intermediate steps, +1 only upon successful task completion.

**Default config values (from `libero/configs/data/default.yaml`):**
- Image resolution: 128x128
- Sequence length: 10
- Frame stacking: 1
- Obs modalities: `rgb` = [agentview_rgb, eye_in_hand_rgb], `low_dim` = [gripper_states, joint_states]
- Train ratio: 0.8

---

### 6. Evaluation

**Native LIBERO evaluation:**

```bash
python libero/lifelong/evaluate.py \
  --benchmark LIBERO_SPATIAL \
  --task_id 0 \
  --algo base \
  --policy bc_transformer_policy \
  --seed 10000 \
  --ep 50 \
  --load_task 0 \
  --device_id 0
```

Arguments:
- `--benchmark`: One of `LIBERO_SPATIAL`, `LIBERO_OBJECT`, `LIBERO_GOAL`, `LIBERO_90`, `LIBERO_10`
- `--task_id`: Task index within the suite
- `--algo`: Lifelong learning algorithm (`base`, `er`, `ewc`, `packnet`, `multitask`)
- `--policy`: Policy architecture (`bc_rnn_policy`, `bc_transformer_policy`, `bc_vilt_policy`)
- `--seed`: Random seed
- `--ep`: Epoch checkpoint to load (for multitask)
- `--load_task`: Which task's checkpoint to load
- `--device_id`: GPU ID
- `--save-videos`: Optional flag to record evaluation videos

**Evaluation protocol:**
- 20 parallel environments run simultaneously (`n_eval: 20`, `num_procs: 20`)
- Max 600 steps per episode (`max_steps: 600`)
- 5 initial zero-action steps for physics settling
- Episode terminates when `done` flag is set or max steps reached

**Output metrics:**
- **Success rate** = num_success / num_envs (per task)
- **Loss** = test set loss
- Saved to: `{save_dir}/{benchmark}_{algo}_{policy}_{seed}_[ep|load]_{task_id}.stats` (PyTorch tensor dict)

**Lifelong learning metrics (across task sequences):**
- **FWT (Forward Transfer)**: Success rate on new tasks after sequential training
- **NBT (Negative Backward Transfer)**: Performance degradation on earlier tasks (catastrophic forgetting)
- **AUC (Area Under Curve)**: Cumulative success rate integrating both FWT and NBT over the task sequence

**Native training command:**
```bash
export CUDA_VISIBLE_DEVICES=0 && \
export MUJOCO_EGL_DEVICE_ID=0 && \
python libero/lifelong/main.py seed=10000 \
  benchmark_name=LIBERO_SPATIAL \
  policy=bc_transformer_policy \
  lifelong=base
```

**LeRobot evaluation (alternative):**
```bash
lerobot-eval \
  --policy.path="your-policy-id" \
  --env.type=libero \
  --env.task=libero_spatial,libero_object,libero_goal,libero_10 \
  --eval.batch_size=1 \
  --eval.n_episodes=10 \
  --env.max_parallel_tasks=1
```
Standard protocol: 10 episodes per task across all 4 standard suites = 400 total episodes.

agentId: a708484d135d02b9a (use SendMessage with to: 'a708484d135d02b9a' to continue this agent)
&lt;usage>total_tokens: 42739
tool_uses: 35
duration_ms: 222710&lt;/usage>
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "parentUuid": "e2518827-e059-43d9-b14a-18c346715d28",
  "isSidechain": false,
  "promptId": "d2c42f79-e375-4b9b-b7c3-7e1496f88b5b",
  "type": "user",
  "uuid": "83653f9d-75ae-462b-84df-4b644c391c7e",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Research the LIBERO Benchmark for robot manipulation. I need detailed information about:\n\n1. GitHub repo URL\n2. Installation method (pip or from source)\n3. The 5 task suites: LIBERO-Spatial, LIBERO-Object, LIBERO-Goal, LIBERO-Long, LIBERO-90 — what each contains\n4. Data download method and size for each suite\n5. Data format: observation space dimensions/meaning, action space dimensions/meaning\n6. Evaluation scripts: how to run evaluation, what metrics are output\n\nUse WebSearch to find the LIBERO benchmark paper and GitHub repo. Then use WebFetch to read the GitHub README, installation docs, and key source files to get specific details about data format, task suites, and evaluation.\n\nBe thorough — I need exact commands, file paths, and API details. Report everything you find in a structured format.",
    "agentId": "a708484d135d02b9a",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Now I have comprehensive information. Let me compile the final report.\n\n---\n\n## LIBERO Benchmark: Comprehensive Technical Reference\n\n### 1. GitHub Repo URL\n\n**Official:** https://github.com/Lifelong-Robot-Learning/LIBERO\n\n**Paper:** [arXiv:2306.03310](https://arxiv.org/abs/2306.03310) (NeurIPS 2023 Datasets & Benchmarks)\n\n**Project website:** https://libero-project.github.io\n\n**HuggingFace fork (LeRobot integration):** https://github.com/huggingface/lerobot-libero\n\n---\n\n### 2. Installation\n\n**Method A: pip (simplest)**\n```bash\npip install libero\n```\nCurrent version: 0.1.1. Requires Python >= 3.\n\n**Method B: From source (recommended for development)**\n```bash\nconda create -n libero python=3.8.13\nconda activate libero\ngit clone https://github.com/Lifelong-Robot-Learning/LIBERO.git\ncd LIBERO\npip install -r requirements.txt\npip install torch==1.11.0+cu113 torchvision==0.12.0+cu113 torchaudio==0.11.0 --extra-index-url https://download.pytorch.org/whl/cu113\npip install -e .\n```\n\n**Method C: Via LeRobot**\n```bash\npip install -e \".[libero]\"\n```\n\nUnderlying simulator: **robosuite** (MuJoCo-based). For headless rendering: `export MUJOCO_GL=egl`.\n\nLicenses: MIT (code), CC BY 4.0 (datasets).\n\n---\n\n### 3. The 5 Task Suites\n\nAll tasks are language-conditioned manipulation with a Franka Panda arm.\n\n| Suite | CLI name | Tasks | Description |\n|-------|----------|-------|-------------|\n| **LIBERO-Spatial** | `libero_spatial` | 10 | Same goal (pick black bowl, place on plate) but bowl is in different spatial locations. Tests transfer of **spatial relationship knowledge**. |\n| **LIBERO-Object** | `libero_object` | 10 | Same goal structure (pick X, place in basket) but with different objects (soup, cream cheese, ketchup, etc.). Tests transfer of **object knowledge**. |\n| **LIBERO-Goal** | `libero_goal` | 10 | Same scene but different goals (open drawer, put bowl on stove, turn on stove, etc.). Tests transfer of **goal/procedural knowledge**. |\n| **LIBERO-90** | `libero_90` | 90 | Short-horizon tasks from LIBERO-100. Entangled distribution shifts across spatial, object, and goal axes. Used for pretraining. |\n| **LIBERO-Long** | `libero_10` | 10 | Long-horizon multi-step tasks from LIBERO-100. Used for downstream evaluation after pretraining on LIBERO-90. |\n\n**LIBERO-Spatial example tasks** (all 10):\n1. pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate\n2. pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate\n3. pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate\n4. pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate\n5. pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate\n6. pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate\n7. pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate\n8. pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate\n9. pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate\n10. pick_up_the_black_bowl_on_the_wooden_cabinet_and_place_it_on_the_plate\n\n**LIBERO-Object example tasks**: pick_up_the_{alphabet_soup, cream_cheese, salad_dressing, bbq_sauce, ketchup, tomato_sauce, butter, milk, chocolate_pudding, orange_juice}_and_place_it_in_the_basket\n\n**LIBERO-Goal example tasks**: open_the_middle_drawer_of_the_cabinet, put_the_bowl_on_the_stove, put_the_wine_bottle_on_top_of_the_cabinet, open_the_top_drawer_and_put_the_bowl_inside, put_the_bowl_on_top_of_the_cabinet, push_the_plate_to_the_front_of_the_stove, put_the_cream_cheese_in_the_bowl, turn_on_the_stove, put_the_bowl_on_the_plate, put_the_wine_bottle_on_the_rack\n\n---\n\n### 4. Data Download\n\n**50 human teleoperation demonstrations per task**, collected via SpaceMouse at 20 Hz.\n\n**Method A: Official script**\n```bash\n# All datasets\npython benchmark_scripts/download_libero_datasets.py\n\n# Specific suite\npython benchmark_scripts/download_libero_datasets.py --datasets libero_spatial\npython benchmark_scripts/download_libero_datasets.py --datasets libero_object\npython benchmark_scripts/download_libero_datasets.py --datasets libero_goal\npython benchmark_scripts/download_libero_datasets.py --datasets libero_100  # contains both libero_90 and libero_10\n\n# Via HuggingFace (recommended, original links may expire)\npython benchmark_scripts/download_libero_datasets.py --use-huggingface\n```\nDefault download location: `./datasets/` under the LIBERO root.\n\n**Method B: HuggingFace direct**\n\nMultiple HF dataset repos exist:\n- Original HDF5: https://huggingface.co/datasets/yifengzhu-hf/LIBERO-datasets (~100 GB total)\n- Physical Intelligence (LeRobot format): https://huggingface.co/datasets/physical-intelligence/libero (~34.9 GB, 4 suites, parquet)\n- HuggingFace VLA (LeRobot format): https://huggingface.co/datasets/HuggingFaceVLA/libero\n\n**Approximate sizes (original HDF5 format):**\n\n| Suite | Approx Size |\n|-------|-------------|\n| libero_spatial | ~6.6 GB |\n| libero_object | ~9.3 GB |\n| libero_goal | ~6-9 GB |\n| libero_10 (Long) | ~12.8 GB |\n| libero_90 | ~60-70 GB |\n| **Total** | **~100 GB** |\n\n---\n\n### 5. Data Format\n\n**File format:** HDF5 (one `.hdf5` file per task)\n\n**HDF5 structure:**\n```\ndata/\n  demo_0/\n    obs/\n      agentview_rgb          # (T, 128, 128, 3) uint8 — third-person camera\n      eye_in_hand_rgb        # (T, 128, 128, 3) uint8 — wrist camera\n      gripper_states         # (T, 1) — gripper aperture (from robot0_gripper_qpos)\n      joint_states           # (T, 7) — 7 joint positions (from robot0_joint_pos)\n      ee_states              # (T, 6) — end-effector position + axis-angle orientation\n      ee_pos                 # (T, 3) — end-effector position\n      ee_ori                 # (T, 3) — end-effector axis-angle orientation\n    actions                  # (T, 7) — 7-DOF action\n    states                   # (T, D) — full simulator state\n    robot_states             # (T, D) — concatenation of gripper_pos, ee_pos, ee_quat\n    rewards                  # (T,) — sparse: 0 everywhere, 1 at final success step\n    dones                    # (T,) — 1 at episode end\n  demo_1/\n    ...\n  demo_49/\n    ...\n```\n\n**Observation space (used in default config):**\n\n| Key | Dimension | Meaning |\n|-----|-----------|---------|\n| `agentview_rgb` (maps to `agentview_image`) | (128, 128, 3) | RGB from workspace camera |\n| `eye_in_hand_rgb` (maps to `robot0_eye_in_hand_image`) | (128, 128, 3) | RGB from wrist-mounted camera |\n| `gripper_states` (maps to `robot0_gripper_qpos`) | (1,) or (2,) | Gripper finger position(s) |\n| `joint_states` (maps to `robot0_joint_pos`) | (7,) | 7 joint angles of the Franka Panda |\n| `ee_pos` | (3,) | End-effector xyz position |\n| `ee_ori` | (3,) | End-effector axis-angle orientation |\n\n**In LeRobot format**, the proprioceptive state is an 8-dimensional vector: `observation.state` = [ee_pos (3) + ee_axis_angle (3) + gripper_qpos (2)] or [ee_pos (3) + ee_axis_angle (3) + gripper_qpos (1) + padding (1)].\n\n**Action space:**\n\n| Dimension | Meaning |\n|-----------|---------|\n| 0-2 | End-effector position delta (dx, dy, dz) |\n| 3-5 | End-effector orientation delta (axis-angle or Euler) |\n| 6 | Gripper command (1 = close, -1 = open) |\n\nTotal: **7-dimensional continuous**, Box(-1, 1, shape=(7,)). Control mode: **OSC_POSE** (Operational Space Control). Frequency: **20 Hz**. Supports both `relative` (delta, default) and `absolute` control modes.\n\n**Reward:** Sparse — 0 for all intermediate steps, +1 only upon successful task completion.\n\n**Default config values (from `libero/configs/data/default.yaml`):**\n- Image resolution: 128x128\n- Sequence length: 10\n- Frame stacking: 1\n- Obs modalities: `rgb` = [agentview_rgb, eye_in_hand_rgb], `low_dim` = [gripper_states, joint_states]\n- Train ratio: 0.8\n\n---\n\n### 6. Evaluation\n\n**Native LIBERO evaluation:**\n\n```bash\npython libero/lifelong/evaluate.py \\\n  --benchmark LIBERO_SPATIAL \\\n  --task_id 0 \\\n  --algo base \\\n  --policy bc_transformer_policy \\\n  --seed 10000 \\\n  --ep 50 \\\n  --load_task 0 \\\n  --device_id 0\n```\n\nArguments:\n- `--benchmark`: One of `LIBERO_SPATIAL`, `LIBERO_OBJECT`, `LIBERO_GOAL`, `LIBERO_90`, `LIBERO_10`\n- `--task_id`: Task index within the suite\n- `--algo`: Lifelong learning algorithm (`base`, `er`, `ewc`, `packnet`, `multitask`)\n- `--policy`: Policy architecture (`bc_rnn_policy`, `bc_transformer_policy`, `bc_vilt_policy`)\n- `--seed`: Random seed\n- `--ep`: Epoch checkpoint to load (for multitask)\n- `--load_task`: Which task's checkpoint to load\n- `--device_id`: GPU ID\n- `--save-videos`: Optional flag to record evaluation videos\n\n**Evaluation protocol:**\n- 20 parallel environments run simultaneously (`n_eval: 20`, `num_procs: 20`)\n- Max 600 steps per episode (`max_steps: 600`)\n- 5 initial zero-action steps for physics settling\n- Episode terminates when `done` flag is set or max steps reached\n\n**Output metrics:**\n- **Success rate** = num_success / num_envs (per task)\n- **Loss** = test set loss\n- Saved to: `{save_dir}/{benchmark}_{algo}_{policy}_{seed}_[ep|load]_{task_id}.stats` (PyTorch tensor dict)\n\n**Lifelong learning metrics (across task sequences):**\n- **FWT (Forward Transfer)**: Success rate on new tasks after sequential training\n- **NBT (Negative Backward Transfer)**: Performance degradation on earlier tasks (catastrophic forgetting)\n- **AUC (Area Under Curve)**: Cumulative success rate integrating both FWT and NBT over the task sequence\n\n**Native training command:**\n```bash\nexport CUDA_VISIBLE_DEVICES=0 && \\\nexport MUJOCO_EGL_DEVICE_ID=0 && \\\npython libero/lifelong/main.py seed=10000 \\\n  benchmark_name=LIBERO_SPATIAL \\\n  policy=bc_transformer_policy \\\n  lifelong=base\n```\n\n**LeRobot evaluation (alternative):**\n```bash\nlerobot-eval \\\n  --policy.path=\"your-policy-id\" \\\n  --env.type=libero \\\n  --env.task=libero_spatial,libero_object,libero_goal,libero_10 \\\n  --eval.batch_size=1 \\\n  --eval.n_episodes=10 \\\n  --env.max_parallel_tasks=1\n```\nStandard protocol: 10 episodes per task across all 4 standard suites = 400 total episodes."
      }
    ],
    "totalDurationMs": 222710,
    "totalTokens": 42739,
    "totalToolUseCount": 35,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1841,
      "cache_read_input_tokens": 37394,
      "output_tokens": 3503,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1841
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3503,
          "cache_read_input_tokens": 37394,
          "cache_creation_input_tokens": 1841,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1841,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 0,
      "searchCount": 0,
      "bashCount": 0,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 35
    }
  },
  "sourceToolAssistantUUID": "e2518827-e059-43d9-b14a-18c346715d28",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/action_cond_info_bottleneck",
  "sessionId": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
````

</details>

---

### Runtime record

_source line 17_

```json
{
  "type": "last-prompt",
  "lastPrompt": "## 任务：调研 LIBERO Benchmark + LIBERO-Plus 评测  你是 ML 研究团队的调研 Worker。请深入调研以下内容，产出一份结构化报告。  ### 调研目标  1. **LIBERO Benchmark**    - GitHub repo 地址    - 安装方式（pip install 还是 from source）    - 5 个 task suites…",
  "leafUuid": "83653f9d-75ae-462b-84df-4b644c391c7e",
  "sessionId": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b"
}
```

---

### Runtime record

_source line 18_

```json
{
  "type": "ai-title",
  "aiTitle": "Research LIBERO Benchmark and LIBERO-Plus evaluation",
  "sessionId": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b"
}
```

---

### Assistant

_source line 19 · 2026-05-15T11:15:34.576Z_

<details><summary>Logged reasoning block</summary>

```text
All three agents have returned comprehensive results. Let me now compile the final report and write it to the specified path.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "83653f9d-75ae-462b-84df-4b644c391c7e",
  "isSidechain": false,
  "requestId": "req_011Cb4Fxg4ATCFpiXw4wPAie",
  "type": "assistant",
  "uuid": "c825ea6f-1f9b-4187-a019-f45bebdfeb73",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/action_cond_info_bottleneck",
  "sessionId": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AsqznMtCNdspEULyo6rq5X",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6565,
      "cache_creation_input_tokens": 4550,
      "cache_read_input_tokens": 23122,
      "output_tokens": 162,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4550,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6565,
          "output_tokens": 162,
          "cache_read_input_tokens": 23122,
          "cache_creation_input_tokens": 4550,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4550
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

_source line 20 · 2026-05-15T11:15:35.073Z_

All three research agents returned comprehensive results. Writing the consolidated report now.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c825ea6f-1f9b-4187-a019-f45bebdfeb73",
  "isSidechain": false,
  "requestId": "req_011Cb4Fxg4ATCFpiXw4wPAie",
  "type": "assistant",
  "uuid": "711cd119-d50d-43a2-8b50-75047f4e60c0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/action_cond_info_bottleneck",
  "sessionId": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AsqznMtCNdspEULyo6rq5X",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6565,
      "cache_creation_input_tokens": 4550,
      "cache_read_input_tokens": 23122,
      "output_tokens": 162,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4550,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6565,
          "output_tokens": 162,
          "cache_read_input_tokens": 23122,
          "cache_creation_input_tokens": 4550,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4550
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

_source line 21 · 2026-05-15T11:15:37.169Z_

<details open><summary>🔧 Tool call — Bash · `toolu_0166WiuqUw5L1GnHyjYMaFfA`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/action_cond_info_bottleneck/artifacts/",
  "description": "Check artifacts directory exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "711cd119-d50d-43a2-8b50-75047f4e60c0",
  "isSidechain": false,
  "requestId": "req_011Cb4Fxg4ATCFpiXw4wPAie",
  "type": "assistant",
  "uuid": "f4ff6798-33e8-489f-b5e2-9488c45dde3c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/action_cond_info_bottleneck",
  "sessionId": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AsqznMtCNdspEULyo6rq5X",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6565,
      "cache_creation_input_tokens": 4550,
      "cache_read_input_tokens": 23122,
      "output_tokens": 162,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4550,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6565,
          "output_tokens": 162,
          "cache_read_input_tokens": 23122,
          "cache_creation_input_tokens": 4550,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4550
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

_source line 22 · 2026-05-15T11:15:37.351Z_

<details><summary>↩ Tool result · reported error · `toolu_0166WiuqUw5L1GnHyjYMaFfA`</summary>

```text
Exit code 2
ls: cannot access '/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/action_cond_info_bottleneck/artifacts/': No such file or directory
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f4ff6798-33e8-489f-b5e2-9488c45dde3c",
  "isSidechain": false,
  "promptId": "d2c42f79-e375-4b9b-b7c3-7e1496f88b5b",
  "type": "user",
  "uuid": "ccc677fe-5d3a-4a42-9992-a51e7463583b",
  "toolUseResult": "Error: Exit code 2\nls: cannot access '/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/action_cond_info_bottleneck/artifacts/': No such file or directory",
  "sourceToolAssistantUUID": "f4ff6798-33e8-489f-b5e2-9488c45dde3c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/action_cond_info_bottleneck",
  "sessionId": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-15T11:15:39.398Z_

<details open><summary>🔧 Tool call — Bash · `toolu_018fwoX7PoXe5FVZxaNi1GLq`</summary>

```json
{
  "command": "mkdir -p /home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/action_cond_info_bottleneck/artifacts",
  "description": "Create artifacts directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ccc677fe-5d3a-4a42-9992-a51e7463583b",
  "isSidechain": false,
  "requestId": "req_011Cb4Fy3BfL8yrnazYFRmLw",
  "type": "assistant",
  "uuid": "1eeddd23-8a98-40bd-8566-49a86b5ef94f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/action_cond_info_bottleneck",
  "sessionId": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013rbdCPs5FHi7yuTRLTCwDK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6798,
      "cache_read_input_tokens": 27672,
      "output_tokens": 109,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6798,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 109,
          "cache_read_input_tokens": 27672,
          "cache_creation_input_tokens": 6798,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6798
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

_source line 24 · 2026-05-15T11:15:39.455Z_

<details><summary>↩ Tool result · `toolu_018fwoX7PoXe5FVZxaNi1GLq`</summary>

```text
(Bash completed with no output)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1eeddd23-8a98-40bd-8566-49a86b5ef94f",
  "isSidechain": false,
  "promptId": "d2c42f79-e375-4b9b-b7c3-7e1496f88b5b",
  "type": "user",
  "uuid": "8c6877a9-6401-4fd8-b850-340cdb0f7244",
  "toolUseResult": {
    "stdout": "",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": true
  },
  "sourceToolAssistantUUID": "1eeddd23-8a98-40bd-8566-49a86b5ef94f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/action_cond_info_bottleneck",
  "sessionId": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-15T11:18:28.053Z_

<details open><summary>🔧 Tool call — Write · `toolu_01LrSHXmQBaHspBqcmLQUt3W`</summary>

````json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/action_cond_info_bottleneck/artifacts/research_libero_benchmark.md",
  "content": "# LIBERO Benchmark + LIBERO-Plus 调研报告\n\n调研日期：2026-05-15\n\n---\n\n## 1. LIBERO Benchmark\n\n### 1.1 基本信息\n\n| 项目 | 内容 |\n|------|------|\n| 论文 | [LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning](https://arxiv.org/abs/2306.03310) (NeurIPS 2023 D&B) |\n| GitHub | https://github.com/Lifelong-Robot-Learning/LIBERO |\n| 项目主页 | https://libero-project.github.io |\n| License | MIT (代码), CC BY 4.0 (数据集) |\n| 模拟器 | robosuite (MuJoCo) |\n| 机器人 | Franka Panda 7-DOF |\n\n### 1.2 安装\n\n**方式 A：pip**\n```bash\npip install libero\n```\n\n**方式 B：from source（推荐）**\n```bash\nconda create -n libero python=3.8.13\nconda activate libero\ngit clone https://github.com/Lifelong-Robot-Learning/LIBERO.git\ncd LIBERO\npip install -r requirements.txt\npip install torch==1.11.0+cu113 torchvision==0.12.0+cu113 torchaudio==0.11.0 --extra-index-url https://download.pytorch.org/whl/cu113\npip install -e .\n```\n\n**方式 C：通过 LeRobot**\n```bash\npip install -e \".[libero]\"\n```\n\n无头渲染需设置：`export MUJOCO_GL=egl`\n\n### 1.3 五个 Task Suite\n\n所有任务都是 language-conditioned manipulation，使用 Franka Panda 机械臂。\n\n| Suite | CLI 名称 | 任务数 | 描述 |\n|-------|----------|--------|------|\n| **LIBERO-Spatial** | `libero_spatial` | 10 | 同一目标（拿黑碗放盘子），碗在不同空间位置。测试 **空间关系知识** 迁移 |\n| **LIBERO-Object** | `libero_object` | 10 | 同一目标结构（拿 X 放篮子），不同物体。测试 **物体知识** 迁移 |\n| **LIBERO-Goal** | `libero_goal` | 10 | 同一场景，不同目标（开抽屉、放碗到炉子上等）。测试 **目标/程序知识** 迁移 |\n| **LIBERO-90** | `libero_90` | 90 | LIBERO-100 中的短期任务，跨 spatial/object/goal 的混合分布偏移。用于 **预训练** |\n| **LIBERO-Long** | `libero_10` | 10 | LIBERO-100 中的长期多步骤任务。用于预训练后的 **下游评测** |\n\n**LIBERO-Spatial 示例任务（全部 10 个）：**\n1. pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate\n2. pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate\n3. pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate\n4. pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate\n5. pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate\n6. pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate\n7. pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate\n8. pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate\n9. pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate\n10. pick_up_the_black_bowl_on_the_wooden_cabinet_and_place_it_on_the_plate\n\n**LIBERO-Object 示例任务：** pick_up_the_{alphabet_soup, cream_cheese, salad_dressing, bbq_sauce, ketchup, tomato_sauce, butter, milk, chocolate_pudding, orange_juice}_and_place_it_in_the_basket\n\n**LIBERO-Goal 示例任务：** open_the_middle_drawer_of_the_cabinet, put_the_bowl_on_the_stove, put_the_wine_bottle_on_top_of_the_cabinet, open_the_top_drawer_and_put_the_bowl_inside, put_the_bowl_on_top_of_the_cabinet, push_the_plate_to_the_front_of_the_stove, put_the_cream_cheese_in_the_bowl, turn_on_the_stove, put_the_bowl_on_the_plate, put_the_wine_bottle_on_the_rack\n\n### 1.4 数据下载\n\n每个任务有 **50 条人类遥操作演示**，通过 SpaceMouse 以 20 Hz 采集。\n\n**方式 A：官方脚本**\n```bash\n# 全部下载\npython benchmark_scripts/download_libero_datasets.py\n\n# 下载特定 suite\npython benchmark_scripts/download_libero_datasets.py --datasets libero_spatial\npython benchmark_scripts/download_libero_datasets.py --datasets libero_object\npython benchmark_scripts/download_libero_datasets.py --datasets libero_goal\npython benchmark_scripts/download_libero_datasets.py --datasets libero_100  # 含 libero_90 + libero_10\n\n# 通过 HuggingFace 下载（推荐，原始链接可能过期）\npython benchmark_scripts/download_libero_datasets.py --use-huggingface\n```\n\n默认下载位置：LIBERO 根目录下的 `./datasets/`\n\n**方式 B：HuggingFace 直接下载**\n\n| 数据集 | 格式 | 大小 |\n|--------|------|------|\n| `yifengzhu-hf/LIBERO-datasets` | 原始 HDF5 | ~100 GB 总计 |\n| `physical-intelligence/libero` | LeRobot (Parquet) | ~34.9 GB |\n| `HuggingFaceVLA/libero` | LeRobot | ~1.9 GB |\n| `lerobot/libero` | LeRobot (视频 AV1) | ~1.94 GB |\n\n**各 suite 近似大小（原始 HDF5 格式）：**\n\n| Suite | 大小 |\n|-------|------|\n| libero_spatial | ~6.6 GB |\n| libero_object | ~9.3 GB |\n| libero_goal | ~6-9 GB |\n| libero_10 (Long) | ~12.8 GB |\n| libero_90 | ~60-70 GB |\n| **总计** | **~100 GB** |\n\n### 1.5 数据格式\n\n**文件格式：** HDF5（每个任务一个 `.hdf5` 文件）\n\n**HDF5 结构：**\n```\ndata/\n  demo_0/\n    obs/\n      agentview_rgb          # (T, 128, 128, 3) uint8 — 第三人称相机\n      eye_in_hand_rgb        # (T, 128, 128, 3) uint8 — 腕部相机\n      gripper_states         # (T, 1) — 夹爪开合度\n      joint_states           # (T, 7) — 7 个关节角度\n      ee_states              # (T, 6) — 末端执行器位置 + 轴角朝向\n      ee_pos                 # (T, 3) — 末端执行器 xyz 位置\n      ee_ori                 # (T, 3) — 末端执行器轴角朝向\n    actions                  # (T, 7) — 7-DOF 动作\n    states                   # (T, D) — 完整模拟器状态\n    robot_states             # (T, D) — gripper_pos + ee_pos + ee_quat 拼接\n    rewards                  # (T,) — 稀疏: 全 0，最后成功步为 1\n    dones                    # (T,) — episode 结束时为 1\n  demo_1/ ...\n  demo_49/ ...\n```\n\n**观测空间：**\n\n| 键 | 维度 | 含义 |\n|----|------|------|\n| `agentview_rgb` (→ `agentview_image`) | (128, 128, 3) | 工作区 RGB 图像 |\n| `eye_in_hand_rgb` (→ `robot0_eye_in_hand_image`) | (128, 128, 3) | 腕部 RGB 图像 |\n| `gripper_states` (→ `robot0_gripper_qpos`) | (1,) 或 (2,) | 夹爪指位置 |\n| `joint_states` (→ `robot0_joint_pos`) | (7,) | Franka Panda 7 关节角 |\n| `ee_pos` | (3,) | 末端执行器 xyz 位置 |\n| `ee_ori` | (3,) | 末端执行器轴角朝向 |\n\n**LeRobot 格式中** proprioceptive state 为 8 维：`observation.state` = [ee_pos (3) + ee_axis_angle (3) + gripper_qpos (2)]\n\n**动作空间：**\n\n| 维度 | 含义 |\n|------|------|\n| 0-2 | 末端执行器位置增量 (dx, dy, dz) |\n| 3-5 | 末端执行器朝向增量 (轴角 / 欧拉角) |\n| 6 | 夹爪命令 (1=闭合, -1=打开) |\n\n- 总计 **7 维连续动作**，Box(-1, 1, shape=(7,))\n- 控制模式：**OSC_POSE**（操作空间控制）\n- 频率：**20 Hz**（原始），LeRobot 格式 **10 Hz**\n- 支持 `relative`（增量，默认）和 `absolute` 两种控制模式\n- 奖励：稀疏 — 中间步全 0，任务完成时 +1\n\n### 1.6 评测\n\n**原生 LIBERO 评测：**\n\n```bash\npython libero/lifelong/evaluate.py \\\n  --benchmark LIBERO_SPATIAL \\\n  --task_id 0 \\\n  --algo base \\\n  --policy bc_transformer_policy \\\n  --seed 10000 \\\n  --ep 50 \\\n  --load_task 0 \\\n  --device_id 0\n```\n\n参数说明：\n- `--benchmark`: `LIBERO_SPATIAL` / `LIBERO_OBJECT` / `LIBERO_GOAL` / `LIBERO_90` / `LIBERO_10`\n- `--task_id`: suite 内的任务索引\n- `--algo`: 终身学习算法 (`base`, `er`, `ewc`, `packnet`, `multitask`)\n- `--policy`: 策略架构 (`bc_rnn_policy`, `bc_transformer_policy`, `bc_vilt_policy`)\n- `--save-videos`: 可选，录制评测视频\n\n**评测协议：**\n- 20 个并行环境同时运行 (`n_eval: 20`, `num_procs: 20`)\n- 每个 episode 最多 600 步 (`max_steps: 600`)\n- 开头 5 步零动作用于物理稳定\n- episode 在 `done=True` 或达到最大步数时终止\n\n**输出指标：**\n- **Success rate** = num_success / num_envs（每个任务）\n- **Loss** = 测试集损失\n- 结果保存路径：`{save_dir}/{benchmark}_{algo}_{policy}_{seed}_[ep|load]_{task_id}.stats`\n\n**终身学习指标（跨任务序列）：**\n- **FWT (Forward Transfer)**: 序列训练后在新任务上的成功率\n- **NBT (Negative Backward Transfer)**: 早期任务性能退化（灾难性遗忘）\n- **AUC (Area Under Curve)**: 综合 FWT 和 NBT 的累积成功率\n\n**原生训练命令：**\n```bash\nexport CUDA_VISIBLE_DEVICES=0 && \\\nexport MUJOCO_EGL_DEVICE_ID=0 && \\\npython libero/lifelong/main.py seed=10000 \\\n  benchmark_name=LIBERO_SPATIAL \\\n  policy=bc_transformer_policy \\\n  lifelong=base\n```\n\n**LeRobot 评测：**\n```bash\nlerobot-eval \\\n  --policy.path=\"your-policy-id\" \\\n  --env.type=libero \\\n  --env.task=libero_spatial,libero_object,libero_goal,libero_10 \\\n  --eval.batch_size=1 \\\n  --eval.n_episodes=10 \\\n  --env.max_parallel_tasks=1\n```\n标准协议：每个任务 10 个 episode，4 个标准 suite = 400 个 episode。\n\n---\n\n## 2. LIBERO-Plus 扰动评测\n\n### 2.1 基本信息\n\n| 项目 | 内容 |\n|------|------|\n| 论文 | [LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models](https://arxiv.org/abs/2510.13626) (CVPR 2026) |\n| GitHub | https://github.com/sylvestf/LIBERO-plus |\n| 项目主页 | https://sylvestf.github.io/LIBERO-plus/ |\n| HF 资产 | https://huggingface.co/datasets/Sylvest/LIBERO-plus |\n| 训练数据 (RLDS) | https://huggingface.co/datasets/Sylvest/libero_plus_rlds |\n| LeRobot 格式 | https://huggingface.co/datasets/lerobot/libero_plus |\n\n### 2.2 LIBERO-Plus 是什么\n\n在原始 LIBERO 基础上增加了：\n- **10,030 个任务变体**，通过系统化扰动生成\n- **7 个扰动维度**，**21 个子维度**\n- **5 个难度级别** (L1-L5)，按多模型共识分层（4 个参考模型中几个能解决该任务）\n- **20,000+ 训练轨迹**（RLDS 格式）\n- 与 vanilla LIBERO 完全兼容的 drop-in replacement\n\n### 2.3 七个扰动维度（精确定义）\n\n#### 2.3.1 物体布局 (Objects Layout)\n- **O1 — 干扰物体 (Confounding objects):** 从 416 个物体池中随机添加 n 个未见过的干扰物体，通过修改 BDDL 任务描述文件实现\n- **O2 — 目标位移 (Target displacement):** 对目标物体初始位置 (x, y, z) 和朝向施加随机扰动，保持语义关系\n\n#### 2.3.2 相机视角 (Camera Viewpoints)\n- **C1 — 距离缩放 (Distance scaling):** 沿光轴将相机距离缩放 1.01x-2.00x\n- **C2 — 球坐标位置 (Spherical position):** 改变方位角 (delta-theta) 和仰角 (delta-phi)，范围 15-75 度\n- **C3 — 朝向扰动 (Orientation perturbation):** 扰动 yaw/pitch/roll，范围 2-10 度\n\n实现：修改 `Problem` 类接口；主要针对第三人称相机（非腕部相机）\n\n#### 2.3.3 机器人初始状态 (Robot Initial States)\n- 对机械臂初始关节位置施加随机扰动，幅度 0.1-0.5\n- 实现：修改 `Problem` 类接口\n\n#### 2.3.4 语言指令 (Language Instructions)\n- **R1 — 干扰改写 (Distraction rewrites):** 添加与任务无关的上下文信息\n- **R2 — 常识替换 (Commonsense substitution):** 用常识性替代描述替换物体名称\n- **R3 — 推理复杂度 (Reasoning complexity):** 改变多步骤任务的推理复杂度\n- 实现：基于 LLM 的指令改写\n\n#### 2.3.5 光照条件 (Light Conditions)\n- **L1 — 漫射颜色 (Diffuse color):** RGB 通道漫射光照调整\n- **L2 — 方向 (Direction):** 平行光源方向变化\n- **L3 — 镜面强度 (Specular intensity):** 镜面高光强度（反射表面）\n- **L4 — 阴影 (Shadow casting):** 阴影开关控制\n- 实现：修改 MuJoCo 场景 XML 定义文件，注册新场景类\n\n#### 2.3.6 背景纹理 (Background Textures)\n- **B1 — 场景纹理 (Scene texture):** 使用 950 张精选纹理通过 XML 场景文件替换环境纹理\n- **B2 — 表面纹理 (Surface texture):** 随机改变工作表面纹理（桌面、地板）\n- 实现：修改 XML 场景定义文件，添加新纹理资产\n\n#### 2.3.7 传感器噪声 (Sensor Noise)\n图像空间后处理（非物理层级）：\n- **N1 — 运动模糊 (Motion blur):** kernel 半径 r=5-35，高斯 sigma=2-20，角度 U(-45, 45)度\n- **N2 — 高斯模糊 (Gaussian blur):** sigma 1-10\n- **N3 — 缩放模糊 (Zoom blur):** 缩放因子 [s_min, s_max, step] 从 [1, 1.11, 0.01] 到 [1, 1.56, 0.03]\n- **N4 — 雾 (Fog):** 密度 alpha=0.5-5.0，衰减率 beta=1.3-3.0\n- **N5 — 毛玻璃模糊 (Glass blur):** sigma=0.5-2.5，像素位移 delta=1-5，迭代 1-3 次\n\n### 2.4 难度级别 (L1-L5)\n\n按 4 个参考模型（OpenVLA-OFT, pi0, pi0-fast, UniVLA）能否解决分层：\n- L1: 4 个都能解决\n- L2: 3 个能解决\n- L3: 2 个能解决\n- L4: 1 个能解决\n- L5: 无一能解决\n\n### 2.5 安装和运行\n\n**安装：**\n```bash\n# 系统依赖\nsudo apt install libexpat1 libfontconfig1-dev libmagickwand-dev\n\n# 克隆安装\ngit clone https://github.com/sylvestf/LIBERO-plus.git\ncd LIBERO-plus\npip install -e .\npip install -r extra_requirements.txt\n\n# 如果已装 vanilla LIBERO，需先卸载\npip uninstall -y hf-libero\n\nexport MUJOCO_GL=egl\n```\n\n**下载资产：**\n\n从 [HuggingFace](https://huggingface.co/datasets/Sylvest/LIBERO-plus/tree/main) 下载 `assets.zip`，解压到 `LIBERO-plus/libero/libero/assets/`。\n\n期望结构：\n```\nlibero/libero/assets/\n├── articulated_objects/\n├── new_objects/\n├── scenes/\n├── stable_hope_objects/\n├── stable_scanned_objects/\n├── textures/\n├── turbosquid_objects/\n├── serving_region.xml\n├── wall_frames.stl\n└── wall.xml\n```\n\n**配置：** 检查 `/root/.libero/config.yaml`。评测时设 `num_trials_per_task: 1`。\n\n任务到扰动类别映射：`.libero/libero/benchmark/task_classification.json`\n\n**LeRobot 评测：**\n```bash\nlerobot-eval \\\n  --policy.path=\"your-policy-id\" \\\n  --env.type=libero_plus \\\n  --env.task=libero_spatial,libero_object,libero_goal,libero_10 \\\n  --eval.batch_size=1 \\\n  --eval.n_episodes=10 \\\n  --env.max_parallel_tasks=1\n```\n\n### 2.6 与标准 LIBERO 的关系\n\nLIBERO-Plus 是 vanilla LIBERO 的 **drop-in replacement**：\n- 安装在同一个 `libero` Python 包名下（替换原版）\n- 相同的 `LiberoEnv` gym 接口\n- 相同的相机名称 (`agentview_image`, `robot0_eye_in_hand_image`)\n- 相同的观测/动作格式\n- 相同的 task suite 名称\n- **不能同时安装 vanilla LIBERO 和 LIBERO-Plus**，切换需要先卸载再安装\n\n---\n\n## 3. 数据增强相关\n\n### 3.1 robosuite 内置随机化\n\nLIBERO 基于 robosuite (MuJoCo)，robosuite 提供了 `DomainRandomizationWrapper` 和三个 Modder 类，可用于任何 robosuite 环境包括 LIBERO。\n\n**DomainRandomizationWrapper：**\n```python\nfrom robosuite.wrappers import DomainRandomizationWrapper\n\nenv = DomainRandomizationWrapper(\n    env=base_env,\n    seed=42,\n    randomize_color=True,        # 几何体/纹理颜色随机化\n    randomize_camera=True,       # 相机位置/朝向/FOV\n    randomize_lighting=True,     # 光源位置/方向/颜色\n    randomize_dynamics=True,     # 物理参数\n    randomize_on_reset=True,     # episode 重置时随机化\n    randomize_every_n_steps=1,   # rollout 中的频率\n)\n```\n\n**CameraModder（内置）：**\n- 位置扰动：默认 size 0.01\n- 旋转扰动（四元数）：默认 size 0.087 (~5 度)\n- FOV 扰动：默认 size 5.0 度\n\n**LightingModder（内置）：**\n- 位置扰动：默认 size 0.1\n- 方向扰动：默认 size 0.35\n- 镜面/环境光/漫射扰动：默认 size 0.1\n- 开关控制：on/off\n\n**TextureModder（内置）：**\n- RGB 颜色随机化 (local interpolation 0.1)\n- 纹理模式：RGB, checker, noise, gradient\n- 材质属性：反射率、光泽度、镜面反射 (local interpolation 0.2)\n- 天空盒随机化（可选）\n\nDemo 脚本：`robosuite/demos/demo_domain_randomization.py`\n\n### 3.2 LIBERO-Plus 扰动可否复用为训练时数据增强\n\n**可以，且论文已经这样做了。** LIBERO-Plus 同时提供评测任务和训练数据集：\n\n**已提供的训练数据：**\n- **22,400 条训练轨迹**（过滤后 20,000+），在各种扰动条件下生成\n- 分布：2,400 物体布局变体 + 各 4,000 光照/相机/背景/语言/噪声维度\n- RLDS 格式存储，LeRobot 格式见 `lerobot/libero_plus`\n- 论文证明混合 SFT (mix-SFT) 训练显著提升鲁棒性：OpenVLA-OFT+ 平均 79.6%\n\n**三条数据增强路径：**\n\n**路径 A — 直接使用 LIBERO-Plus 训练数据：**\n```bash\nlerobot-train \\\n    --policy.type=smolvla \\\n    --dataset.repo_id=lerobot/libero_plus \\\n    --env.type=libero_plus \\\n    ...\n```\n\n**路径 B — 使用 robosuite 内置 DomainRandomizationWrapper 在线增强：**\n```python\nfrom robosuite.wrappers import DomainRandomizationWrapper\nenv = DomainRandomizationWrapper(\n    env=libero_env,\n    randomize_camera=True,\n    randomize_lighting=True,\n    randomize_color=True\n)\n```\n在线随机化，每 N 步应用随机扰动。适合训练时增强但可控性较低。\n\n**路径 C — 复用 LIBERO-Plus 扰动代码做自定义增强：**\n- 光照/纹理扰动：修改场景 XML + 注册新场景\n- 相机扰动：修改 `Problem` 类接口\n- 传感器噪声 (N1-N5)：纯图像空间后处理，可直接作为标准数据增强应用于任何存储轨迹，无需重新渲染\n\n**关键区别：**\n- robosuite 内置随机化（路径 B）是 **在线** 的，可控性低\n- LIBERO-Plus 扰动（路径 C）是 **结构化** 的，有明确参数范围和难度分层，更适合系统性鲁棒性训练\n- 传感器噪声 (N1-N5) 是纯图像后处理，可以零成本复用为数据增强\n\n---\n\n## 4. 与 LeRobot 的集成\n\n### 4.1 原生支持\n\nLeRobot **原生支持** LIBERO，是一级基准测试环境。\n\n安装：`pip install -e \".[libero]\"`\n\n文档：https://huggingface.co/docs/lerobot/en/libero\n\nHuggingFace 维护了 LIBERO fork：https://github.com/huggingface/lerobot-libero\n\n### 4.2 HuggingFace Hub 数据集\n\n**主要数据集（推荐用于训练）：**\n\n| 数据集 ID | Episodes | 任务数 | 大小 | 说明 |\n|-----------|----------|--------|------|------|\n| `HuggingFaceVLA/libero` | 148 | 10 | ~1.9 GB | 官方预处理数据集，LeRobot 文档推荐 |\n| `lerobot/libero` | 1,693 | 40 | ~1.94 GB | 4 个标准 suite 合并（视频格式, AV1 编码） |\n| `physical-intelligence/libero` | 147 | 10 | ~34.9 GB | PI 的转换版本, RLDS 来源, CC-BY-4.0 |\n| `lerobot/libero_plus` | — | — | — | LIBERO-Plus 训练数据 |\n\n**每个 suite 的图像数据集：**\n\n| 数据集 ID | 任务数 |\n|-----------|--------|\n| `lerobot/libero_10_image` | 10 |\n| `lerobot/libero_object_image` | 10 |\n| `lerobot/libero_spatial_image` | 10 |\n| `lerobot/libero_goal_image` | 10 |\n\n**社区数据集：**\n- `IPEC-COMMUNITY/libero_90_no_noops_lerobot` — LIBERO-90 去除 no-op 版本\n\n### 4.3 数据格式映射\n\n| LIBERO 字段 | LeRobot 特征 | 类型 | 形状 |\n|-------------|-------------|------|------|\n| `agentview_image` | `observation.images.image` | Video/Image | (256, 256, 3) |\n| `robot0_eye_in_hand_image` | `observation.images.image2` | Video/Image | (256, 256, 3) |\n| `observation[\"state\"]` | `observation.state` | float32 | (8,) |\n| `action` | `action` | float32 | (7,) |\n| `language_instruction` | `task` (task_index) | string/int | — |\n\nLeRobot 元数据：robot_type=`panda`，fps=`10`，视频编码=AV1 yuv420p，表格数据用 Parquet 存储\n\n### 4.4 转换脚本\n\n**方式 A：Physical Intelligence 的 OpenPI 转换脚本（主要）**\n\n脚本路径：[`Physical-Intelligence/openpi/examples/libero/convert_libero_data_to_lerobot.py`](https://github.com/Physical-Intelligence/openpi/blob/main/examples/libero/convert_libero_data_to_lerobot.py)\n\n```bash\n# 前置依赖\nuv pip install tensorflow tensorflow_datasets\n\n# 原始数据来源\n# https://huggingface.co/datasets/openvla/modified_libero_rlds\n\n# 执行转换\nuv run examples/libero/convert_libero_data_to_lerobot.py \\\n  --data_dir /path/to/your/data \\\n  --push_to_hub\n```\n\n处理流程：\n1. 读取 4 个 RLDS 数据集：`libero_10_no_noops`, `libero_goal_no_noops`, `libero_object_no_noops`, `libero_spatial_no_noops`\n2. 创建 `LeRobotDataset`，robot_type=panda, fps=10\n3. 逐 episode 迭代，每步调用 `dataset.add_frame()`\n4. 每个 episode 调用 `dataset.save_episode()`\n5. 可选推送到 HuggingFace Hub\n\n处理时间：约 30 分钟\n\n**方式 B：通用 HDF5 → LeRobot 转换器**\n\n仓库：https://github.com/anarnuri/hdf5_to_lerobot_converter\n\n支持 LIBERO 原生 HDF5 格式。\n\n**方式 C：直接使用预转换数据集（无需转换）**\n\n```python\nfrom lerobot.common.datasets.lerobot_dataset import LeRobotDataset\n\ndataset = LeRobotDataset(\"HuggingFaceVLA/libero\")\n# 或\ndataset = LeRobotDataset(\"lerobot/libero\")\n```\n\n### 4.5 端到端训练和评测示例\n\n**训练：**\n```bash\nlerobot-train \\\n  --policy.type=smolvla \\\n  --policy.repo_id=${HF_USER}/libero-test \\\n  --policy.load_vlm_weights=true \\\n  --dataset.repo_id=HuggingFaceVLA/libero \\\n  --env.type=libero \\\n  --env.task=libero_10 \\\n  --output_dir=./outputs/ \\\n  --steps=100000 \\\n  --batch_size=4 \\\n  --eval.batch_size=1 \\\n  --eval.n_episodes=1 \\\n  --eval_freq=1000\n```\n\n**评测：**\n```bash\nlerobot-eval \\\n  --policy.path=\"your-policy-id\" \\\n  --env.type=libero \\\n  --env.task=libero_spatial,libero_object,libero_goal,libero_10 \\\n  --eval.batch_size=1 \\\n  --eval.n_episodes=10 \\\n  --env.max_parallel_tasks=1\n```\n\n---\n\n## 5. 关键注意事项\n\n1. **LIBERO-90 数据** 不在标准预转换数据集中。需要用 OpenPI 转换脚本或社区数据集 `IPEC-COMMUNITY/libero_90_no_noops_lerobot`\n2. **控制模式** (`relative` vs `absolute`) 必须与策略的动作参数化匹配\n3. **vanilla LIBERO 和 LIBERO-Plus 不能同时安装**，两者共用同一 Python 包名\n4. LeRobot 中 LIBERO 仅支持 Linux（MuJoCo 渲染需 EGL）\n5. LeRobot 格式的图像分辨率为 256x256，而原始 LIBERO 为 128x128 [UNVERIFIED — 需确认是否做了上采样或 LeRobot 环境重新渲染]\n6. 原始 LIBERO 采集频率 20Hz，LeRobot 格式为 10Hz（可能做了下采样）[UNVERIFIED — 需确认具体降频策略]\n"
}
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8c6877a9-6401-4fd8-b850-340cdb0f7244",
  "isSidechain": false,
  "requestId": "req_011Cb4FyC8Rc5Vk81K4HHPva",
  "type": "assistant",
  "uuid": "ed1e3f2b-5dd1-4f43-aec9-4e1690c42692",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/action_cond_info_bottleneck",
  "sessionId": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KaXfrY7rLugJND194qYAkg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 127,
      "cache_read_input_tokens": 34470,
      "output_tokens": 9430,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 127,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 9430,
          "cache_read_input_tokens": 34470,
          "cache_creation_input_tokens": 127,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 127
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

_source line 26 · 2026-05-15T11:18:28.110Z_

<details><summary>↩ Tool result · `toolu_01LrSHXmQBaHspBqcmLQUt3W`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/action_cond_info_bottleneck/artifacts/research_libero_benchmark.md
```

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "parentUuid": "ed1e3f2b-5dd1-4f43-aec9-4e1690c42692",
  "isSidechain": false,
  "promptId": "d2c42f79-e375-4b9b-b7c3-7e1496f88b5b",
  "type": "user",
  "uuid": "5c7adfbe-4759-45e3-a443-1b40911a2ad5",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/action_cond_info_bottleneck/artifacts/research_libero_benchmark.md",
    "content": "# LIBERO Benchmark + LIBERO-Plus 调研报告\n\n调研日期：2026-05-15\n\n---\n\n## 1. LIBERO Benchmark\n\n### 1.1 基本信息\n\n| 项目 | 内容 |\n|------|------|\n| 论文 | [LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning](https://arxiv.org/abs/2306.03310) (NeurIPS 2023 D&B) |\n| GitHub | https://github.com/Lifelong-Robot-Learning/LIBERO |\n| 项目主页 | https://libero-project.github.io |\n| License | MIT (代码), CC BY 4.0 (数据集) |\n| 模拟器 | robosuite (MuJoCo) |\n| 机器人 | Franka Panda 7-DOF |\n\n### 1.2 安装\n\n**方式 A：pip**\n```bash\npip install libero\n```\n\n**方式 B：from source（推荐）**\n```bash\nconda create -n libero python=3.8.13\nconda activate libero\ngit clone https://github.com/Lifelong-Robot-Learning/LIBERO.git\ncd LIBERO\npip install -r requirements.txt\npip install torch==1.11.0+cu113 torchvision==0.12.0+cu113 torchaudio==0.11.0 --extra-index-url https://download.pytorch.org/whl/cu113\npip install -e .\n```\n\n**方式 C：通过 LeRobot**\n```bash\npip install -e \".[libero]\"\n```\n\n无头渲染需设置：`export MUJOCO_GL=egl`\n\n### 1.3 五个 Task Suite\n\n所有任务都是 language-conditioned manipulation，使用 Franka Panda 机械臂。\n\n| Suite | CLI 名称 | 任务数 | 描述 |\n|-------|----------|--------|------|\n| **LIBERO-Spatial** | `libero_spatial` | 10 | 同一目标（拿黑碗放盘子），碗在不同空间位置。测试 **空间关系知识** 迁移 |\n| **LIBERO-Object** | `libero_object` | 10 | 同一目标结构（拿 X 放篮子），不同物体。测试 **物体知识** 迁移 |\n| **LIBERO-Goal** | `libero_goal` | 10 | 同一场景，不同目标（开抽屉、放碗到炉子上等）。测试 **目标/程序知识** 迁移 |\n| **LIBERO-90** | `libero_90` | 90 | LIBERO-100 中的短期任务，跨 spatial/object/goal 的混合分布偏移。用于 **预训练** |\n| **LIBERO-Long** | `libero_10` | 10 | LIBERO-100 中的长期多步骤任务。用于预训练后的 **下游评测** |\n\n**LIBERO-Spatial 示例任务（全部 10 个）：**\n1. pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate\n2. pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate\n3. pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate\n4. pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate\n5. pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate\n6. pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate\n7. pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate\n8. pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate\n9. pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate\n10. pick_up_the_black_bowl_on_the_wooden_cabinet_and_place_it_on_the_plate\n\n**LIBERO-Object 示例任务：** pick_up_the_{alphabet_soup, cream_cheese, salad_dressing, bbq_sauce, ketchup, tomato_sauce, butter, milk, chocolate_pudding, orange_juice}_and_place_it_in_the_basket\n\n**LIBERO-Goal 示例任务：** open_the_middle_drawer_of_the_cabinet, put_the_bowl_on_the_stove, put_the_wine_bottle_on_top_of_the_cabinet, open_the_top_drawer_and_put_the_bowl_inside, put_the_bowl_on_top_of_the_cabinet, push_the_plate_to_the_front_of_the_stove, put_the_cream_cheese_in_the_bowl, turn_on_the_stove, put_the_bowl_on_the_plate, put_the_wine_bottle_on_the_rack\n\n### 1.4 数据下载\n\n每个任务有 **50 条人类遥操作演示**，通过 SpaceMouse 以 20 Hz 采集。\n\n**方式 A：官方脚本**\n```bash\n# 全部下载\npython benchmark_scripts/download_libero_datasets.py\n\n# 下载特定 suite\npython benchmark_scripts/download_libero_datasets.py --datasets libero_spatial\npython benchmark_scripts/download_libero_datasets.py --datasets libero_object\npython benchmark_scripts/download_libero_datasets.py --datasets libero_goal\npython benchmark_scripts/download_libero_datasets.py --datasets libero_100  # 含 libero_90 + libero_10\n\n# 通过 HuggingFace 下载（推荐，原始链接可能过期）\npython benchmark_scripts/download_libero_datasets.py --use-huggingface\n```\n\n默认下载位置：LIBERO 根目录下的 `./datasets/`\n\n**方式 B：HuggingFace 直接下载**\n\n| 数据集 | 格式 | 大小 |\n|--------|------|------|\n| `yifengzhu-hf/LIBERO-datasets` | 原始 HDF5 | ~100 GB 总计 |\n| `physical-intelligence/libero` | LeRobot (Parquet) | ~34.9 GB |\n| `HuggingFaceVLA/libero` | LeRobot | ~1.9 GB |\n| `lerobot/libero` | LeRobot (视频 AV1) | ~1.94 GB |\n\n**各 suite 近似大小（原始 HDF5 格式）：**\n\n| Suite | 大小 |\n|-------|------|\n| libero_spatial | ~6.6 GB |\n| libero_object | ~9.3 GB |\n| libero_goal | ~6-9 GB |\n| libero_10 (Long) | ~12.8 GB |\n| libero_90 | ~60-70 GB |\n| **总计** | **~100 GB** |\n\n### 1.5 数据格式\n\n**文件格式：** HDF5（每个任务一个 `.hdf5` 文件）\n\n**HDF5 结构：**\n```\ndata/\n  demo_0/\n    obs/\n      agentview_rgb          # (T, 128, 128, 3) uint8 — 第三人称相机\n      eye_in_hand_rgb        # (T, 128, 128, 3) uint8 — 腕部相机\n      gripper_states         # (T, 1) — 夹爪开合度\n      joint_states           # (T, 7) — 7 个关节角度\n      ee_states              # (T, 6) — 末端执行器位置 + 轴角朝向\n      ee_pos                 # (T, 3) — 末端执行器 xyz 位置\n      ee_ori                 # (T, 3) — 末端执行器轴角朝向\n    actions                  # (T, 7) — 7-DOF 动作\n    states                   # (T, D) — 完整模拟器状态\n    robot_states             # (T, D) — gripper_pos + ee_pos + ee_quat 拼接\n    rewards                  # (T,) — 稀疏: 全 0，最后成功步为 1\n    dones                    # (T,) — episode 结束时为 1\n  demo_1/ ...\n  demo_49/ ...\n```\n\n**观测空间：**\n\n| 键 | 维度 | 含义 |\n|----|------|------|\n| `agentview_rgb` (→ `agentview_image`) | (128, 128, 3) | 工作区 RGB 图像 |\n| `eye_in_hand_rgb` (→ `robot0_eye_in_hand_image`) | (128, 128, 3) | 腕部 RGB 图像 |\n| `gripper_states` (→ `robot0_gripper_qpos`) | (1,) 或 (2,) | 夹爪指位置 |\n| `joint_states` (→ `robot0_joint_pos`) | (7,) | Franka Panda 7 关节角 |\n| `ee_pos` | (3,) | 末端执行器 xyz 位置 |\n| `ee_ori` | (3,) | 末端执行器轴角朝向 |\n\n**LeRobot 格式中** proprioceptive state 为 8 维：`observation.state` = [ee_pos (3) + ee_axis_angle (3) + gripper_qpos (2)]\n\n**动作空间：**\n\n| 维度 | 含义 |\n|------|------|\n| 0-2 | 末端执行器位置增量 (dx, dy, dz) |\n| 3-5 | 末端执行器朝向增量 (轴角 / 欧拉角) |\n| 6 | 夹爪命令 (1=闭合, -1=打开) |\n\n- 总计 **7 维连续动作**，Box(-1, 1, shape=(7,))\n- 控制模式：**OSC_POSE**（操作空间控制）\n- 频率：**20 Hz**（原始），LeRobot 格式 **10 Hz**\n- 支持 `relative`（增量，默认）和 `absolute` 两种控制模式\n- 奖励：稀疏 — 中间步全 0，任务完成时 +1\n\n### 1.6 评测\n\n**原生 LIBERO 评测：**\n\n```bash\npython libero/lifelong/evaluate.py \\\n  --benchmark LIBERO_SPATIAL \\\n  --task_id 0 \\\n  --algo base \\\n  --policy bc_transformer_policy \\\n  --seed 10000 \\\n  --ep 50 \\\n  --load_task 0 \\\n  --device_id 0\n```\n\n参数说明：\n- `--benchmark`: `LIBERO_SPATIAL` / `LIBERO_OBJECT` / `LIBERO_GOAL` / `LIBERO_90` / `LIBERO_10`\n- `--task_id`: suite 内的任务索引\n- `--algo`: 终身学习算法 (`base`, `er`, `ewc`, `packnet`, `multitask`)\n- `--policy`: 策略架构 (`bc_rnn_policy`, `bc_transformer_policy`, `bc_vilt_policy`)\n- `--save-videos`: 可选，录制评测视频\n\n**评测协议：**\n- 20 个并行环境同时运行 (`n_eval: 20`, `num_procs: 20`)\n- 每个 episode 最多 600 步 (`max_steps: 600`)\n- 开头 5 步零动作用于物理稳定\n- episode 在 `done=True` 或达到最大步数时终止\n\n**输出指标：**\n- **Success rate** = num_success / num_envs（每个任务）\n- **Loss** = 测试集损失\n- 结果保存路径：`{save_dir}/{benchmark}_{algo}_{policy}_{seed}_[ep|load]_{task_id}.stats`\n\n**终身学习指标（跨任务序列）：**\n- **FWT (Forward Transfer)**: 序列训练后在新任务上的成功率\n- **NBT (Negative Backward Transfer)**: 早期任务性能退化（灾难性遗忘）\n- **AUC (Area Under Curve)**: 综合 FWT 和 NBT 的累积成功率\n\n**原生训练命令：**\n```bash\nexport CUDA_VISIBLE_DEVICES=0 && \\\nexport MUJOCO_EGL_DEVICE_ID=0 && \\\npython libero/lifelong/main.py seed=10000 \\\n  benchmark_name=LIBERO_SPATIAL \\\n  policy=bc_transformer_policy \\\n  lifelong=base\n```\n\n**LeRobot 评测：**\n```bash\nlerobot-eval \\\n  --policy.path=\"your-policy-id\" \\\n  --env.type=libero \\\n  --env.task=libero_spatial,libero_object,libero_goal,libero_10 \\\n  --eval.batch_size=1 \\\n  --eval.n_episodes=10 \\\n  --env.max_parallel_tasks=1\n```\n标准协议：每个任务 10 个 episode，4 个标准 suite = 400 个 episode。\n\n---\n\n## 2. LIBERO-Plus 扰动评测\n\n### 2.1 基本信息\n\n| 项目 | 内容 |\n|------|------|\n| 论文 | [LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models](https://arxiv.org/abs/2510.13626) (CVPR 2026) |\n| GitHub | https://github.com/sylvestf/LIBERO-plus |\n| 项目主页 | https://sylvestf.github.io/LIBERO-plus/ |\n| HF 资产 | https://huggingface.co/datasets/Sylvest/LIBERO-plus |\n| 训练数据 (RLDS) | https://huggingface.co/datasets/Sylvest/libero_plus_rlds |\n| LeRobot 格式 | https://huggingface.co/datasets/lerobot/libero_plus |\n\n### 2.2 LIBERO-Plus 是什么\n\n在原始 LIBERO 基础上增加了：\n- **10,030 个任务变体**，通过系统化扰动生成\n- **7 个扰动维度**，**21 个子维度**\n- **5 个难度级别** (L1-L5)，按多模型共识分层（4 个参考模型中几个能解决该任务）\n- **20,000+ 训练轨迹**（RLDS 格式）\n- 与 vanilla LIBERO 完全兼容的 drop-in replacement\n\n### 2.3 七个扰动维度（精确定义）\n\n#### 2.3.1 物体布局 (Objects Layout)\n- **O1 — 干扰物体 (Confounding objects):** 从 416 个物体池中随机添加 n 个未见过的干扰物体，通过修改 BDDL 任务描述文件实现\n- **O2 — 目标位移 (Target displacement):** 对目标物体初始位置 (x, y, z) 和朝向施加随机扰动，保持语义关系\n\n#### 2.3.2 相机视角 (Camera Viewpoints)\n- **C1 — 距离缩放 (Distance scaling):** 沿光轴将相机距离缩放 1.01x-2.00x\n- **C2 — 球坐标位置 (Spherical position):** 改变方位角 (delta-theta) 和仰角 (delta-phi)，范围 15-75 度\n- **C3 — 朝向扰动 (Orientation perturbation):** 扰动 yaw/pitch/roll，范围 2-10 度\n\n实现：修改 `Problem` 类接口；主要针对第三人称相机（非腕部相机）\n\n#### 2.3.3 机器人初始状态 (Robot Initial States)\n- 对机械臂初始关节位置施加随机扰动，幅度 0.1-0.5\n- 实现：修改 `Problem` 类接口\n\n#### 2.3.4 语言指令 (Language Instructions)\n- **R1 — 干扰改写 (Distraction rewrites):** 添加与任务无关的上下文信息\n- **R2 — 常识替换 (Commonsense substitution):** 用常识性替代描述替换物体名称\n- **R3 — 推理复杂度 (Reasoning complexity):** 改变多步骤任务的推理复杂度\n- 实现：基于 LLM 的指令改写\n\n#### 2.3.5 光照条件 (Light Conditions)\n- **L1 — 漫射颜色 (Diffuse color):** RGB 通道漫射光照调整\n- **L2 — 方向 (Direction):** 平行光源方向变化\n- **L3 — 镜面强度 (Specular intensity):** 镜面高光强度（反射表面）\n- **L4 — 阴影 (Shadow casting):** 阴影开关控制\n- 实现：修改 MuJoCo 场景 XML 定义文件，注册新场景类\n\n#### 2.3.6 背景纹理 (Background Textures)\n- **B1 — 场景纹理 (Scene texture):** 使用 950 张精选纹理通过 XML 场景文件替换环境纹理\n- **B2 — 表面纹理 (Surface texture):** 随机改变工作表面纹理（桌面、地板）\n- 实现：修改 XML 场景定义文件，添加新纹理资产\n\n#### 2.3.7 传感器噪声 (Sensor Noise)\n图像空间后处理（非物理层级）：\n- **N1 — 运动模糊 (Motion blur):** kernel 半径 r=5-35，高斯 sigma=2-20，角度 U(-45, 45)度\n- **N2 — 高斯模糊 (Gaussian blur):** sigma 1-10\n- **N3 — 缩放模糊 (Zoom blur):** 缩放因子 [s_min, s_max, step] 从 [1, 1.11, 0.01] 到 [1, 1.56, 0.03]\n- **N4 — 雾 (Fog):** 密度 alpha=0.5-5.0，衰减率 beta=1.3-3.0\n- **N5 — 毛玻璃模糊 (Glass blur):** sigma=0.5-2.5，像素位移 delta=1-5，迭代 1-3 次\n\n### 2.4 难度级别 (L1-L5)\n\n按 4 个参考模型（OpenVLA-OFT, pi0, pi0-fast, UniVLA）能否解决分层：\n- L1: 4 个都能解决\n- L2: 3 个能解决\n- L3: 2 个能解决\n- L4: 1 个能解决\n- L5: 无一能解决\n\n### 2.5 安装和运行\n\n**安装：**\n```bash\n# 系统依赖\nsudo apt install libexpat1 libfontconfig1-dev libmagickwand-dev\n\n# 克隆安装\ngit clone https://github.com/sylvestf/LIBERO-plus.git\ncd LIBERO-plus\npip install -e .\npip install -r extra_requirements.txt\n\n# 如果已装 vanilla LIBERO，需先卸载\npip uninstall -y hf-libero\n\nexport MUJOCO_GL=egl\n```\n\n**下载资产：**\n\n从 [HuggingFace](https://huggingface.co/datasets/Sylvest/LIBERO-plus/tree/main) 下载 `assets.zip`，解压到 `LIBERO-plus/libero/libero/assets/`。\n\n期望结构：\n```\nlibero/libero/assets/\n├── articulated_objects/\n├── new_objects/\n├── scenes/\n├── stable_hope_objects/\n├── stable_scanned_objects/\n├── textures/\n├── turbosquid_objects/\n├── serving_region.xml\n├── wall_frames.stl\n└── wall.xml\n```\n\n**配置：** 检查 `/root/.libero/config.yaml`。评测时设 `num_trials_per_task: 1`。\n\n任务到扰动类别映射：`.libero/libero/benchmark/task_classification.json`\n\n**LeRobot 评测：**\n```bash\nlerobot-eval \\\n  --policy.path=\"your-policy-id\" \\\n  --env.type=libero_plus \\\n  --env.task=libero_spatial,libero_object,libero_goal,libero_10 \\\n  --eval.batch_size=1 \\\n  --eval.n_episodes=10 \\\n  --env.max_parallel_tasks=1\n```\n\n### 2.6 与标准 LIBERO 的关系\n\nLIBERO-Plus 是 vanilla LIBERO 的 **drop-in replacement**：\n- 安装在同一个 `libero` Python 包名下（替换原版）\n- 相同的 `LiberoEnv` gym 接口\n- 相同的相机名称 (`agentview_image`, `robot0_eye_in_hand_image`)\n- 相同的观测/动作格式\n- 相同的 task suite 名称\n- **不能同时安装 vanilla LIBERO 和 LIBERO-Plus**，切换需要先卸载再安装\n\n---\n\n## 3. 数据增强相关\n\n### 3.1 robosuite 内置随机化\n\nLIBERO 基于 robosuite (MuJoCo)，robosuite 提供了 `DomainRandomizationWrapper` 和三个 Modder 类，可用于任何 robosuite 环境包括 LIBERO。\n\n**DomainRandomizationWrapper：**\n```python\nfrom robosuite.wrappers import DomainRandomizationWrapper\n\nenv = DomainRandomizationWrapper(\n    env=base_env,\n    seed=42,\n    randomize_color=True,        # 几何体/纹理颜色随机化\n    randomize_camera=True,       # 相机位置/朝向/FOV\n    randomize_lighting=True,     # 光源位置/方向/颜色\n    randomize_dynamics=True,     # 物理参数\n    randomize_on_reset=True,     # episode 重置时随机化\n    randomize_every_n_steps=1,   # rollout 中的频率\n)\n```\n\n**CameraModder（内置）：**\n- 位置扰动：默认 size 0.01\n- 旋转扰动（四元数）：默认 size 0.087 (~5 度)\n- FOV 扰动：默认 size 5.0 度\n\n**LightingModder（内置）：**\n- 位置扰动：默认 size 0.1\n- 方向扰动：默认 size 0.35\n- 镜面/环境光/漫射扰动：默认 size 0.1\n- 开关控制：on/off\n\n**TextureModder（内置）：**\n- RGB 颜色随机化 (local interpolation 0.1)\n- 纹理模式：RGB, checker, noise, gradient\n- 材质属性：反射率、光泽度、镜面反射 (local interpolation 0.2)\n- 天空盒随机化（可选）\n\nDemo 脚本：`robosuite/demos/demo_domain_randomization.py`\n\n### 3.2 LIBERO-Plus 扰动可否复用为训练时数据增强\n\n**可以，且论文已经这样做了。** LIBERO-Plus 同时提供评测任务和训练数据集：\n\n**已提供的训练数据：**\n- **22,400 条训练轨迹**（过滤后 20,000+），在各种扰动条件下生成\n- 分布：2,400 物体布局变体 + 各 4,000 光照/相机/背景/语言/噪声维度\n- RLDS 格式存储，LeRobot 格式见 `lerobot/libero_plus`\n- 论文证明混合 SFT (mix-SFT) 训练显著提升鲁棒性：OpenVLA-OFT+ 平均 79.6%\n\n**三条数据增强路径：**\n\n**路径 A — 直接使用 LIBERO-Plus 训练数据：**\n```bash\nlerobot-train \\\n    --policy.type=smolvla \\\n    --dataset.repo_id=lerobot/libero_plus \\\n    --env.type=libero_plus \\\n    ...\n```\n\n**路径 B — 使用 robosuite 内置 DomainRandomizationWrapper 在线增强：**\n```python\nfrom robosuite.wrappers import DomainRandomizationWrapper\nenv = DomainRandomizationWrapper(\n    env=libero_env,\n    randomize_camera=True,\n    randomize_lighting=True,\n    randomize_color=True\n)\n```\n在线随机化，每 N 步应用随机扰动。适合训练时增强但可控性较低。\n\n**路径 C — 复用 LIBERO-Plus 扰动代码做自定义增强：**\n- 光照/纹理扰动：修改场景 XML + 注册新场景\n- 相机扰动：修改 `Problem` 类接口\n- 传感器噪声 (N1-N5)：纯图像空间后处理，可直接作为标准数据增强应用于任何存储轨迹，无需重新渲染\n\n**关键区别：**\n- robosuite 内置随机化（路径 B）是 **在线** 的，可控性低\n- LIBERO-Plus 扰动（路径 C）是 **结构化** 的，有明确参数范围和难度分层，更适合系统性鲁棒性训练\n- 传感器噪声 (N1-N5) 是纯图像后处理，可以零成本复用为数据增强\n\n---\n\n## 4. 与 LeRobot 的集成\n\n### 4.1 原生支持\n\nLeRobot **原生支持** LIBERO，是一级基准测试环境。\n\n安装：`pip install -e \".[libero]\"`\n\n文档：https://huggingface.co/docs/lerobot/en/libero\n\nHuggingFace 维护了 LIBERO fork：https://github.com/huggingface/lerobot-libero\n\n### 4.2 HuggingFace Hub 数据集\n\n**主要数据集（推荐用于训练）：**\n\n| 数据集 ID | Episodes | 任务数 | 大小 | 说明 |\n|-----------|----------|--------|------|------|\n| `HuggingFaceVLA/libero` | 148 | 10 | ~1.9 GB | 官方预处理数据集，LeRobot 文档推荐 |\n| `lerobot/libero` | 1,693 | 40 | ~1.94 GB | 4 个标准 suite 合并（视频格式, AV1 编码） |\n| `physical-intelligence/libero` | 147 | 10 | ~34.9 GB | PI 的转换版本, RLDS 来源, CC-BY-4.0 |\n| `lerobot/libero_plus` | — | — | — | LIBERO-Plus 训练数据 |\n\n**每个 suite 的图像数据集：**\n\n| 数据集 ID | 任务数 |\n|-----------|--------|\n| `lerobot/libero_10_image` | 10 |\n| `lerobot/libero_object_image` | 10 |\n| `lerobot/libero_spatial_image` | 10 |\n| `lerobot/libero_goal_image` | 10 |\n\n**社区数据集：**\n- `IPEC-COMMUNITY/libero_90_no_noops_lerobot` — LIBERO-90 去除 no-op 版本\n\n### 4.3 数据格式映射\n\n| LIBERO 字段 | LeRobot 特征 | 类型 | 形状 |\n|-------------|-------------|------|------|\n| `agentview_image` | `observation.images.image` | Video/Image | (256, 256, 3) |\n| `robot0_eye_in_hand_image` | `observation.images.image2` | Video/Image | (256, 256, 3) |\n| `observation[\"state\"]` | `observation.state` | float32 | (8,) |\n| `action` | `action` | float32 | (7,) |\n| `language_instruction` | `task` (task_index) | string/int | — |\n\nLeRobot 元数据：robot_type=`panda`，fps=`10`，视频编码=AV1 yuv420p，表格数据用 Parquet 存储\n\n### 4.4 转换脚本\n\n**方式 A：Physical Intelligence 的 OpenPI 转换脚本（主要）**\n\n脚本路径：[`Physical-Intelligence/openpi/examples/libero/convert_libero_data_to_lerobot.py`](https://github.com/Physical-Intelligence/openpi/blob/main/examples/libero/convert_libero_data_to_lerobot.py)\n\n```bash\n# 前置依赖\nuv pip install tensorflow tensorflow_datasets\n\n# 原始数据来源\n# https://huggingface.co/datasets/openvla/modified_libero_rlds\n\n# 执行转换\nuv run examples/libero/convert_libero_data_to_lerobot.py \\\n  --data_dir /path/to/your/data \\\n  --push_to_hub\n```\n\n处理流程：\n1. 读取 4 个 RLDS 数据集：`libero_10_no_noops`, `libero_goal_no_noops`, `libero_object_no_noops`, `libero_spatial_no_noops`\n2. 创建 `LeRobotDataset`，robot_type=panda, fps=10\n3. 逐 episode 迭代，每步调用 `dataset.add_frame()`\n4. 每个 episode 调用 `dataset.save_episode()`\n5. 可选推送到 HuggingFace Hub\n\n处理时间：约 30 分钟\n\n**方式 B：通用 HDF5 → LeRobot 转换器**\n\n仓库：https://github.com/anarnuri/hdf5_to_lerobot_converter\n\n支持 LIBERO 原生 HDF5 格式。\n\n**方式 C：直接使用预转换数据集（无需转换）**\n\n```python\nfrom lerobot.common.datasets.lerobot_dataset import LeRobotDataset\n\ndataset = LeRobotDataset(\"HuggingFaceVLA/libero\")\n# 或\ndataset = LeRobotDataset(\"lerobot/libero\")\n```\n\n### 4.5 端到端训练和评测示例\n\n**训练：**\n```bash\nlerobot-train \\\n  --policy.type=smolvla \\\n  --policy.repo_id=${HF_USER}/libero-test \\\n  --policy.load_vlm_weights=true \\\n  --dataset.repo_id=HuggingFaceVLA/libero \\\n  --env.type=libero \\\n  --env.task=libero_10 \\\n  --output_dir=./outputs/ \\\n  --steps=100000 \\\n  --batch_size=4 \\\n  --eval.batch_size=1 \\\n  --eval.n_episodes=1 \\\n  --eval_freq=1000\n```\n\n**评测：**\n```bash\nlerobot-eval \\\n  --policy.path=\"your-policy-id\" \\\n  --env.type=libero \\\n  --env.task=libero_spatial,libero_object,libero_goal,libero_10 \\\n  --eval.batch_size=1 \\\n  --eval.n_episodes=10 \\\n  --env.max_parallel_tasks=1\n```\n\n---\n\n## 5. 关键注意事项\n\n1. **LIBERO-90 数据** 不在标准预转换数据集中。需要用 OpenPI 转换脚本或社区数据集 `IPEC-COMMUNITY/libero_90_no_noops_lerobot`\n2. **控制模式** (`relative` vs `absolute`) 必须与策略的动作参数化匹配\n3. **vanilla LIBERO 和 LIBERO-Plus 不能同时安装**，两者共用同一 Python 包名\n4. LeRobot 中 LIBERO 仅支持 Linux（MuJoCo 渲染需 EGL）\n5. LeRobot 格式的图像分辨率为 256x256，而原始 LIBERO 为 128x128 [UNVERIFIED — 需确认是否做了上采样或 LeRobot 环境重新渲染]\n6. 原始 LIBERO 采集频率 20Hz，LeRobot 格式为 10Hz（可能做了下采样）[UNVERIFIED — 需确认具体降频策略]\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "ed1e3f2b-5dd1-4f43-aec9-4e1690c42692",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/action_cond_info_bottleneck",
  "sessionId": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
````

</details>

---

### Runtime record

_source line 27_

```json
{
  "type": "last-prompt",
  "lastPrompt": "## 任务：调研 LIBERO Benchmark + LIBERO-Plus 评测  你是 ML 研究团队的调研 Worker。请深入调研以下内容，产出一份结构化报告。  ### 调研目标  1. **LIBERO Benchmark**    - GitHub repo 地址    - 安装方式（pip install 还是 from source）    - 5 个 task suites…",
  "leafUuid": "5c7adfbe-4759-45e3-a443-1b40911a2ad5",
  "sessionId": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b"
}
```

---

### Runtime record

_source line 28_

```json
{
  "type": "ai-title",
  "aiTitle": "Research LIBERO Benchmark and LIBERO-Plus evaluation",
  "sessionId": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b"
}
```

---

### Assistant

_source line 29 · 2026-05-15T11:18:41.151Z_

报告已写入 `artifacts/research_libero_benchmark.md`。

覆盖的内容：
- **LIBERO Benchmark**：GitHub/安装/5 个 task suite 详情/HDF5 数据格式（观测 128x128 双相机 + 7D 关节 + 6D EE，动作 7D OSC_POSE）/评测脚本命令和指标（success rate, FWT, NBT, AUC）
- **LIBERO-Plus**：实际是 7 个扰动维度 21 个子维度（不只是 4 个），含物体布局/相机/机器人初态/语言指令/光照/背景纹理/传感器噪声，CVPR 2026 论文，drop-in replacement 架构
- **数据增强**：robosuite 内置 DomainRandomizationWrapper + 三个 Modder 可直接用；LIBERO-Plus 同时提供 22,400 条增强训练轨迹；传感器噪声为纯图像后处理可零成本复用
- **LeRobot 集成**：原生支持，HuggingFace 上有 `lerobot/libero`、`HuggingFaceVLA/libero` 等预转换数据集，附 OpenPI 转换脚本路径

两处标注了 `[UNVERIFIED]`：LeRobot 格式图像分辨率（256 vs 128）和采样率降频策略。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5c7adfbe-4759-45e3-a443-1b40911a2ad5",
  "isSidechain": false,
  "requestId": "req_011Cb4GBdE7jTaLuisPGqKoY",
  "type": "assistant",
  "uuid": "90d84658-7f4e-4438-bb8a-7d984bf66ad4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/action_cond_info_bottleneck",
  "sessionId": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H9D7EhqfnN1pMNr7WeroNJ",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9492,
      "cache_read_input_tokens": 34597,
      "output_tokens": 415,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9492,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 415,
          "cache_read_input_tokens": 34597,
          "cache_creation_input_tokens": 9492,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9492
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
  "lastPrompt": "## 任务：调研 LIBERO Benchmark + LIBERO-Plus 评测  你是 ML 研究团队的调研 Worker。请深入调研以下内容，产出一份结构化报告。  ### 调研目标  1. **LIBERO Benchmark**    - GitHub repo 地址    - 安装方式（pip install 还是 from source）    - 5 个 task suites…",
  "leafUuid": "90d84658-7f4e-4438-bb8a-7d984bf66ad4",
  "sessionId": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b"
}
```

---

### Runtime record

_source line 31_

```json
{
  "type": "ai-title",
  "aiTitle": "Research LIBERO Benchmark and LIBERO-Plus evaluation",
  "sessionId": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b"
}
```

---
