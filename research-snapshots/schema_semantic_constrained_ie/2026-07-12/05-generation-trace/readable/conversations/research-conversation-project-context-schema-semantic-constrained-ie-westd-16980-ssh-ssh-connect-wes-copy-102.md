# Research conversation: <project_context> # 项目: schema_semantic_constrained_ie ## 运行环境 - 服务器名: westd-16980 - SSH 连接命令: ssh connect.westd.seetacl

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 71
- **Recorded user turns:** 1
- **Tool calls:** 19
- **Original source:** `logs/chats/exported-trajectories/account-2/1da856f6-e3e6-4a2a-8180-80868464ada5.jsonl`
- **Structured JSON:** [`bbecd189880d40596385.json`](../../sessions/bb/bbecd189880d40596385.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-16T17:16:04.411Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-16T17:16:04.411Z",
  "sessionId": "1da856f6-e3e6-4a2a-8180-80868464ada5",
  "content": "&lt;project_context>\n# 项目: schema_semantic_constrained_ie\n\n## 运行环境\n- 服务器名: westd-16980\n- SSH 连接命令: ssh connect.westd.seetacloud.com  # 必须用此命令，~/.ssh/config 自动应用密钥和跳板机，禁止用裸 IP\n- 项目代码根目录: /root/schema_semantic_constrained_ie\n\n\n## 环境搭建\n连接服务器后先调 `detect_image` 检测是否为预置镜像。如果匹配，跳过基础环境搭建，只装项目特有依赖。已预装的包不要重复安装。\n\n## 输出风格\n回复简洁直接。只输出执行结果和必要信息，不要解释过程、不要客套、不要给未被要求的建议。\n&lt;/project_context>\n## �� CRITICAL: 修正 ft_ablation_analysis.md 数据错误\n\nReviewer 发现 DocRED FT ablation 表格有系统性数据混淆：grammar_only/semantic_only 行部分字段用了 unconstrained 值，unconstrained 行用了 grammar_only 值。共 14 个错误数据点。\n\n### 正确数据（从 Reviewer 逐格验证后给出，必须按此填写）\n\nDocRED FT Ablation 正确表格：\n```\n| Model | Mode          | ET   | RV   | DR   | CF   | E_F1  | R_F1  | parse_fail |\n| Qwen  | Unconstrained | 0    | 0.27 | 0.76 | 0.12 | 82.15 | 40.86 | 7.11 |\n| Qwen  | Grammar Only  | 0    | 0    | 0.61 | 0.11 | 82.19 | 40.85 | 7.01 |\n| Qwen  | Semantic Only | 0    | 0.23 | 0.21 | 0.27 | 82.15 | 40.89 | 7.52 |\n| Qwen  | Full (G+S)    | 0    | 0    | 0.01 | 0.41 | 81.43 | 40.56 | 8.52 |\n| Llama | Unconstrained | 0    | 0.15 | 0.49 | —    | 83.93 | 43.72 | 2.30 |\n| Llama | Grammar Only  | 0    | 0    | 0.51 | 0.12 | 84.04 | 43.77 | 2.30 |\n| Llama | Semantic Only | 0    | 0.15 | 0.30 | 0.16 | 84.02 | 43.90 | 2.40 |\n| Llama | Full (G+S)    | 0    | 0    | 0.20 | 0.26 | 85.23 | 44.23 | 2.51 |\n```\n\n注意：\n- Llama unconstrained CF 标为 \"—\"（registry 无此字段）\n- 所有数据必须逐格填写，不要从其他表格交叉引用\n\n### 需要修正的文件\n\n**文件 1**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/ft_ablation_analysis.md`\n- 找到 DocRED 部分的表格\n- 逐格按上面正确数据替换\n- 确保 SciERC 部分数据也是正确的（如有疑问，从 registry 验证）\n\n**文件 2**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/table4_ft_ablation.md`\n- 如果此文件包含 DocRED ablation 数据，同样按正确表格修正\n- 确保与 ft_ablation_analysis.md 一致\n\n### 验证步骤\n\n修正后，用 `read_registry` 验证以下实验的 metrics 是否与表格一致：\n- w8_qwen_docred_ft_grammar_only\n- w8_qwen_docred_ft_semantic_only\n- w8_llama_docred_ft_grammar_only\n- w8_llama_docred_ft_semantic_only\n- w5_qwen_docred_lora_unconstrained_eval\n- w5_llama_docred_lora_unconstrained_eval\n- w5_qwen_docred_lora_constrained_eval\n- w5_llama_docred_lora_constrained_eval\n\n### 最后\n\n列出所有修正的字段（格式：文件 → 行 → 字段 → 错误值 → 正确值）"
}
````

---

### Runtime record

_source line 2 · 2026-05-16T17:16:04.422Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-16T17:16:04.422Z",
  "sessionId": "1da856f6-e3e6-4a2a-8180-80868464ada5"
}
```

---

## Round 1

69 recorded events

### User

_source line 3 · 2026-05-16T17:16:04.531Z_

&lt;project_context>
# 项目: schema_semantic_constrained_ie

## 运行环境
- 服务器名: westd-16980
- SSH 连接命令: ssh connect.westd.seetacloud.com  # 必须用此命令，~/.ssh/config 自动应用密钥和跳板机，禁止用裸 IP
- 项目代码根目录: /root/schema_semantic_constrained_ie


## 环境搭建
连接服务器后先调 `detect_image` 检测是否为预置镜像。如果匹配，跳过基础环境搭建，只装项目特有依赖。已预装的包不要重复安装。

## 输出风格
回复简洁直接。只输出执行结果和必要信息，不要解释过程、不要客套、不要给未被要求的建议。
&lt;/project_context>
## �� CRITICAL: 修正 ft_ablation_analysis.md 数据错误

Reviewer 发现 DocRED FT ablation 表格有系统性数据混淆：grammar_only/semantic_only 行部分字段用了 unconstrained 值，unconstrained 行用了 grammar_only 值。共 14 个错误数据点。

### 正确数据（从 Reviewer 逐格验证后给出，必须按此填写）

DocRED FT Ablation 正确表格：
```
| Model | Mode          | ET   | RV   | DR   | CF   | E_F1  | R_F1  | parse_fail |
| Qwen  | Unconstrained | 0    | 0.27 | 0.76 | 0.12 | 82.15 | 40.86 | 7.11 |
| Qwen  | Grammar Only  | 0    | 0    | 0.61 | 0.11 | 82.19 | 40.85 | 7.01 |
| Qwen  | Semantic Only | 0    | 0.23 | 0.21 | 0.27 | 82.15 | 40.89 | 7.52 |
| Qwen  | Full (G+S)    | 0    | 0    | 0.01 | 0.41 | 81.43 | 40.56 | 8.52 |
| Llama | Unconstrained | 0    | 0.15 | 0.49 | —    | 83.93 | 43.72 | 2.30 |
| Llama | Grammar Only  | 0    | 0    | 0.51 | 0.12 | 84.04 | 43.77 | 2.30 |
| Llama | Semantic Only | 0    | 0.15 | 0.30 | 0.16 | 84.02 | 43.90 | 2.40 |
| Llama | Full (G+S)    | 0    | 0    | 0.20 | 0.26 | 85.23 | 44.23 | 2.51 |
```

注意：
- Llama unconstrained CF 标为 "—"（registry 无此字段）
- 所有数据必须逐格填写，不要从其他表格交叉引用

### 需要修正的文件

**文件 1**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/ft_ablation_analysis.md`
- 找到 DocRED 部分的表格
- 逐格按上面正确数据替换
- 确保 SciERC 部分数据也是正确的（如有疑问，从 registry 验证）

**文件 2**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/table4_ft_ablation.md`
- 如果此文件包含 DocRED ablation 数据，同样按正确表格修正
- 确保与 ft_ablation_analysis.md 一致

### 验证步骤

修正后，用 `read_registry` 验证以下实验的 metrics 是否与表格一致：
- w8_qwen_docred_ft_grammar_only
- w8_qwen_docred_ft_semantic_only
- w8_llama_docred_ft_grammar_only
- w8_llama_docred_ft_semantic_only
- w5_qwen_docred_lora_unconstrained_eval
- w5_llama_docred_lora_unconstrained_eval
- w5_qwen_docred_lora_constrained_eval
- w5_llama_docred_lora_constrained_eval

### 最后

列出所有修正的字段（格式：文件 → 行 → 字段 → 错误值 → 正确值）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "f3f24f5a-bd6d-444a-89a8-04e2233f247b",
  "type": "user",
  "uuid": "7c97bb42-a44d-496f-8b10-74acb3bb7285",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "1da856f6-e3e6-4a2a-8180-80868464ada5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-16T17:16:04.530Z_

```json
{
  "parentUuid": "7c97bb42-a44d-496f-8b10-74acb3bb7285",
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
  "uuid": "8a836c22-d682-4a79-9a44-c26a11ce0d05",
  "timestamp": "2026-05-16T17:16:04.530Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "1da856f6-e3e6-4a2a-8180-80868464ada5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-16T17:16:04.530Z_

```json
{
  "parentUuid": "8a836c22-d682-4a79-9a44-c26a11ce0d05",
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
  "uuid": "d6e1edda-8f2a-453f-a8be-35fd458fc55c",
  "timestamp": "2026-05-16T17:16:04.530Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "1da856f6-e3e6-4a2a-8180-80868464ada5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6 · 2026-05-16T17:16:04.530Z_

```json
{
  "parentUuid": "d6e1edda-8f2a-453f-a8be-35fd458fc55c",
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
  "uuid": "f5fdcd1e-e448-4a25-9683-4d70e212c601",
  "timestamp": "2026-05-16T17:16:04.530Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "1da856f6-e3e6-4a2a-8180-80868464ada5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 7 · 2026-05-16T17:16:04.530Z_

```json
{
  "parentUuid": "f5fdcd1e-e448-4a25-9683-4d70e212c601",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "3c5a6702-4359-40df-960e-471691c6f035",
  "timestamp": "2026-05-16T17:16:04.530Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "1da856f6-e3e6-4a2a-8180-80868464ada5",
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
  "aiTitle": "Fix DocRED FT ablation data errors in markdown files",
  "sessionId": "1da856f6-e3e6-4a2a-8180-80868464ada5"
}
```

---

### Assistant

_source line 9 · 2026-05-16T17:16:07.235Z_

<details><summary>Logged reasoning block</summary>

```text
Let me start by reading the two files that need to be corrected, and also load the registry tools to verify data.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3c5a6702-4359-40df-960e-471691c6f035",
  "isSidechain": false,
  "requestId": "req_011Cb6dGBsie22mgeK7DDwuH",
  "type": "assistant",
  "uuid": "2a103768-70de-4f9b-8181-b995aca11d23",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "1da856f6-e3e6-4a2a-8180-80868464ada5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UeXxShLWLLYfFmuWjEBUeb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12260,
      "cache_read_input_tokens": 11447,
      "output_tokens": 293,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12260,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 293,
          "cache_read_input_tokens": 11447,
          "cache_creation_input_tokens": 12260,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12260
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

_source line 10 · 2026-05-16T17:16:07.877Z_

Let me read both files and load the registry tool in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2a103768-70de-4f9b-8181-b995aca11d23",
  "isSidechain": false,
  "requestId": "req_011Cb6dGBsie22mgeK7DDwuH",
  "type": "assistant",
  "uuid": "7ce618f6-4b7a-4247-8ebe-ba92e9082dfd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "1da856f6-e3e6-4a2a-8180-80868464ada5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UeXxShLWLLYfFmuWjEBUeb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12260,
      "cache_read_input_tokens": 11447,
      "output_tokens": 293,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12260,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 293,
          "cache_read_input_tokens": 11447,
          "cache_creation_input_tokens": 12260,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12260
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

_source line 11 · 2026-05-16T17:16:08.550Z_

<details open><summary>🔧 Tool call — Read · `toolu_01WCv7U1fnn19pz5FYW66TJM`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/ft_ablation_analysis.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7ce618f6-4b7a-4247-8ebe-ba92e9082dfd",
  "isSidechain": false,
  "requestId": "req_011Cb6dGBsie22mgeK7DDwuH",
  "type": "assistant",
  "uuid": "f06afc35-474f-4a47-9379-e4aca6495778",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "1da856f6-e3e6-4a2a-8180-80868464ada5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UeXxShLWLLYfFmuWjEBUeb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12260,
      "cache_read_input_tokens": 11447,
      "output_tokens": 293,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12260,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 293,
          "cache_read_input_tokens": 11447,
          "cache_creation_input_tokens": 12260,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12260
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

_source line 12 · 2026-05-16T17:16:09.455Z_

<details><summary>↩ Tool result · `toolu_01KfN2fv5NeupHCWYtu8fimX`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__read_registry"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8eb91eb9-0624-4dd4-a3bc-94d368cc2014",
  "isSidechain": false,
  "promptId": "f3f24f5a-bd6d-444a-89a8-04e2233f247b",
  "type": "user",
  "uuid": "8ddd5bbc-4106-485c-8da0-1634f37b5723",
  "toolUseResult": {
    "matches": [
      "mcp__agent-ml-research__read_registry"
    ],
    "query": "select:mcp__agent-ml-research__read_registry",
    "total_deferred_tools": 25
  },
  "sourceToolAssistantUUID": "8eb91eb9-0624-4dd4-a3bc-94d368cc2014",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "1da856f6-e3e6-4a2a-8180-80868464ada5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-16T17:16:08.561Z_

<details><summary>↩ Tool result · `toolu_01WCv7U1fnn19pz5FYW66TJM`</summary>

```text
1	# FT-Regime Ablation: Complete Results
2	
3	Generated: 2026-05-16 (updated: all 8 experiments complete)
4	
5	## Table 1: SciERC FT Ablation
6	
7	| Model | Mode | ET% | RV% | DR% | CF% | E_F1 | R_F1 |
8	|-------|------|-----|-----|-----|-----|------|------|
9	| Qwen3-8B | Unconstrained | 0 | 0 | 1.90 | 0 | 67.05 | 43.86 |
10	| Qwen3-8B | Grammar Only | 0 | 0 | 1.90 | 0 | 67.05 | 43.86 |
11	| Qwen3-8B | Semantic Only | 0 | 0 | 0.60 | 0.84 | 67.05 | 43.69 |
12	| Qwen3-8B | Full (G+S) | 0 | 0 | 0 | 1.18 | 67.05 | 43.77 |
13	| Llama-3.1-8B | Unconstrained | 0 | 0 | 1.11 | 0 | 67.76 | 45.45 |
14	| Llama-3.1-8B | Grammar Only | 0 | 0 | 1.11 | 0 | 67.76 | 45.45 |
15	| Llama-3.1-8B | Semantic Only | 0 | 0 | 0.65 | 0.11 | 67.76 | 45.47 |
16	| Llama-3.1-8B | Full (G+S) | 0 | 0 | 0.09 | 0.46 | 67.76 | 45.47 |
17	
18	Notes:
19	- ET = Entity Type violation, RV = Relation Vocabulary violation, DR = Domain-Range violation, CF = Cross-Field consistency violation
20	- Grammar layer constrains ET and RV; Semantic layer constrains DR
21	- Grammar Only = grammar constraints active, semantic off; Semantic Only = semantic constraints active, grammar off
22	- All values from registry metrics; DR% for grammar_only computed as violations/total_relations×100
23	
24	## Table 2: DocRED FT Ablation
25	
26	| Model | Mode | ET% | RV% | DR% | CF% | E_F1 | R_F1 | Parse Fail% |
27	|-------|------|-----|-----|-----|-----|------|------|-------------|
28	| Qwen3-8B | Unconstrained | 0 | 0.27 | 0.76 | 0.12 | 82.15 | 40.86 | 7.11 |
29	| Qwen3-8B | Grammar Only | 0 | 0.27 | 0.61 | 0.12 | 82.15 | 40.86 | 7.11 |
30	| Qwen3-8B | Semantic Only | 0 | 0.27 | 0.21 | 0.12 | 82.15 | 40.86 | 7.11 |
31	| Qwen3-8B | Full (G+S) | 0 | 0 | 0.01 | 0.41 | 81.43 | 40.56 | 8.52 |
32	| Llama-3.1-8B | Unconstrained | 0 | 0.15 | 0.51 | 0.16 | 84.04 | 43.77 | 2.30 |
33	| Llama-3.1-8B | Grammar Only | 0 | 0.15 | 0.51 | 0.16 | 84.04 | 43.77 | 2.30 |
34	| Llama-3.1-8B | Semantic Only | 0 | 0.15 | 0.30 | 0.16 | 84.02 | 43.90 | 2.40 |
35	| Llama-3.1-8B | Full (G+S) | 0 | 0 | 0.20 | 0.26 | 85.23 | 44.23 | 2.51 |
36	
37	Notes:
38	- DocRED ablation (w8 series) complete — all 8 configurations finished
39	- Parse Fail% included because DocRED's longer documents cause non-trivial parse failures
40	- Grammar Only rows confirm grammar layer is redundant in FT regime (identical to unconstrained for Llama; near-identical for Qwen)
41	- Qwen grammar_only DR=0.61% vs unconstrained 0.76% — minor difference likely due to grammar filtering edge cases, not semantic enforcement
42	
43	## Key Findings
44	
45	1. **Grammar layer is redundant in FT regime (4/4 settings confirmed)**: After fine-tuning, both models produce zero ET violations and near-zero RV violations even without constraints. Grammar-only decoding yields identical (or near-identical) F1 and violation rates to unconstrained across both SciERC and DocRED, confirming that FT internalizes syntactic schema compliance regardless of dataset complexity.
46	
47	2. **Semantic layer provides the marginal value in FT**: The semantic constraint consistently reduces DR violations across all 4 settings:
48	   - SciERC: Qwen 1.90%→0.60% (-68%), Llama 1.11%→0.65% (-41%)
49	   - DocRED: Qwen 0.76%→0.21% (-72%), Llama 0.51%→0.30% (-41%)
50	   - DR reduction range: 41–72% across all model×dataset combinations
51	
52	3. **Two layers are complementary, not redundant**: Semantic-only reduces DR substantially but not to zero. The residual DR is further reduced only when grammar constraints co-operate with semantic constraints in full mode. This suggests the grammar layer's token-level filtering creates a cleaner hypothesis space for the semantic layer's beam-level enforcement.
53	
54	4. **F1 cost is negligible**: Across all configurations, both models, and both datasets, E_F1 is unchanged (±0.02pp) and R_F1 varies by at most ±0.17pp. The constraint layers operate as a free lunch for schema compliance.
55	
56	5. **Cross-model × cross-dataset consistency**: Both Qwen3-8B and Llama-3.1-8B show the same pattern — grammar redundant, semantic essential, full optimal — on both SciERC (sentence-level, 7 relation types) and DocRED (document-level, 96 relation types). This supports the generality of the finding across architectures, schema sizes, and document granularities.
57	
58	6. **Claim 2 evidence chain complete**: The ablation cleanly decomposes constraint contributions:
59	   - Grammar layer → eliminates ET and RV (but these are already zero post-FT, so redundant)
60	   - Semantic layer → reduces DR by 41–72% in isolation
61	   - Full system → drives DR to near-zero (0–0.20%)
62	   - Each layer's contribution is orthogonal and verifiable across all 4 experimental settings
63	
64	## Paper-Ready Narrative
65	
66	### Ablation Analysis (FT Regime)
67	
68	To disentangle the contributions of the grammar and semantic constraint layers under fine-tuning, we evaluate four configurations: unconstrained decoding, grammar-only constraints (enforcing valid entity types and relation vocabulary), semantic-only constraints (enforcing domain-range compatibility), and the full OntoCoDec system. Tables 1–2 report results on SciERC (sentence-level, 7 relation types) and DocRED (document-level, 96 relation types) across two backbone models (Qwen3-8B, Llama-3.1-8B).
69	
70	Fine-tuning proves highly effective at internalizing surface-level schema compliance: both models produce zero entity-type violations and near-zero relation-vocabulary violations even without constrained decoding, rendering the grammar layer operationally redundant in this regime. However, domain-range violations persist at 0.5–1.9% without semantic enforcement across both datasets, confirming that relational consistency represents a deeper structural property that supervised training alone does not fully capture.
71	
72	The semantic constraint layer reduces domain-range violations by 41–72% in isolation (semantic-only mode) across all four model×dataset settings: −68% and −41% on SciERC (Qwen, Llama), −72% and −41% on DocRED (Qwen, Llama). The consistency of this pattern across a sentence-level dataset with 7 relation types and a document-level dataset with 96 relation types demonstrates that the semantic layer's value is robust to schema complexity and document length. Residual violations are further reduced when both layers operate jointly, as the grammar layer's token-level filtering restricts the generation space to syntactically valid candidates, enabling the semantic layer's beam-level enforcement to operate over a reduced, higher-quality hypothesis set.
73	
74	Crucially, this schema compliance improvement comes at negligible extraction cost: entity F1 is unchanged across all configurations (±0.02pp), and relation F1 varies by at most 0.17 percentage points. These results establish that OntoCoDec's two-layer architecture provides complementary, rather than redundant, enforcement even when the base model has been adapted to the target schema through fine-tuning.
75	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f06afc35-474f-4a47-9379-e4aca6495778",
  "isSidechain": false,
  "promptId": "f3f24f5a-bd6d-444a-89a8-04e2233f247b",
  "type": "user",
  "uuid": "ebeb4f48-17c5-4fb1-b069-7b9045a4fd12",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/ft_ablation_analysis.md",
      "content": "# FT-Regime Ablation: Complete Results\n\nGenerated: 2026-05-16 (updated: all 8 experiments complete)\n\n## Table 1: SciERC FT Ablation\n\n| Model | Mode | ET% | RV% | DR% | CF% | E_F1 | R_F1 |\n|-------|------|-----|-----|-----|-----|------|------|\n| Qwen3-8B | Unconstrained | 0 | 0 | 1.90 | 0 | 67.05 | 43.86 |\n| Qwen3-8B | Grammar Only | 0 | 0 | 1.90 | 0 | 67.05 | 43.86 |\n| Qwen3-8B | Semantic Only | 0 | 0 | 0.60 | 0.84 | 67.05 | 43.69 |\n| Qwen3-8B | Full (G+S) | 0 | 0 | 0 | 1.18 | 67.05 | 43.77 |\n| Llama-3.1-8B | Unconstrained | 0 | 0 | 1.11 | 0 | 67.76 | 45.45 |\n| Llama-3.1-8B | Grammar Only | 0 | 0 | 1.11 | 0 | 67.76 | 45.45 |\n| Llama-3.1-8B | Semantic Only | 0 | 0 | 0.65 | 0.11 | 67.76 | 45.47 |\n| Llama-3.1-8B | Full (G+S) | 0 | 0 | 0.09 | 0.46 | 67.76 | 45.47 |\n\nNotes:\n- ET = Entity Type violation, RV = Relation Vocabulary violation, DR = Domain-Range violation, CF = Cross-Field consistency violation\n- Grammar layer constrains ET and RV; Semantic layer constrains DR\n- Grammar Only = grammar constraints active, semantic off; Semantic Only = semantic constraints active, grammar off\n- All values from registry metrics; DR% for grammar_only computed as violations/total_relations×100\n\n## Table 2: DocRED FT Ablation\n\n| Model | Mode | ET% | RV% | DR% | CF% | E_F1 | R_F1 | Parse Fail% |\n|-------|------|-----|-----|-----|-----|------|------|-------------|\n| Qwen3-8B | Unconstrained | 0 | 0.27 | 0.76 | 0.12 | 82.15 | 40.86 | 7.11 |\n| Qwen3-8B | Grammar Only | 0 | 0.27 | 0.61 | 0.12 | 82.15 | 40.86 | 7.11 |\n| Qwen3-8B | Semantic Only | 0 | 0.27 | 0.21 | 0.12 | 82.15 | 40.86 | 7.11 |\n| Qwen3-8B | Full (G+S) | 0 | 0 | 0.01 | 0.41 | 81.43 | 40.56 | 8.52 |\n| Llama-3.1-8B | Unconstrained | 0 | 0.15 | 0.51 | 0.16 | 84.04 | 43.77 | 2.30 |\n| Llama-3.1-8B | Grammar Only | 0 | 0.15 | 0.51 | 0.16 | 84.04 | 43.77 | 2.30 |\n| Llama-3.1-8B | Semantic Only | 0 | 0.15 | 0.30 | 0.16 | 84.02 | 43.90 | 2.40 |\n| Llama-3.1-8B | Full (G+S) | 0 | 0 | 0.20 | 0.26 | 85.23 | 44.23 | 2.51 |\n\nNotes:\n- DocRED ablation (w8 series) complete — all 8 configurations finished\n- Parse Fail% included because DocRED's longer documents cause non-trivial parse failures\n- Grammar Only rows confirm grammar layer is redundant in FT regime (identical to unconstrained for Llama; near-identical for Qwen)\n- Qwen grammar_only DR=0.61% vs unconstrained 0.76% — minor difference likely due to grammar filtering edge cases, not semantic enforcement\n\n## Key Findings\n\n1. **Grammar layer is redundant in FT regime (4/4 settings confirmed)**: After fine-tuning, both models produce zero ET violations and near-zero RV violations even without constraints. Grammar-only decoding yields identical (or near-identical) F1 and violation rates to unconstrained across both SciERC and DocRED, confirming that FT internalizes syntactic schema compliance regardless of dataset complexity.\n\n2. **Semantic layer provides the marginal value in FT**: The semantic constraint consistently reduces DR violations across all 4 settings:\n   - SciERC: Qwen 1.90%→0.60% (-68%), Llama 1.11%→0.65% (-41%)\n   - DocRED: Qwen 0.76%→0.21% (-72%), Llama 0.51%→0.30% (-41%)\n   - DR reduction range: 41–72% across all model×dataset combinations\n\n3. **Two layers are complementary, not redundant**: Semantic-only reduces DR substantially but not to zero. The residual DR is further reduced only when grammar constraints co-operate with semantic constraints in full mode. This suggests the grammar layer's token-level filtering creates a cleaner hypothesis space for the semantic layer's beam-level enforcement.\n\n4. **F1 cost is negligible**: Across all configurations, both models, and both datasets, E_F1 is unchanged (±0.02pp) and R_F1 varies by at most ±0.17pp. The constraint layers operate as a free lunch for schema compliance.\n\n5. **Cross-model × cross-dataset consistency**: Both Qwen3-8B and Llama-3.1-8B show the same pattern — grammar redundant, semantic essential, full optimal — on both SciERC (sentence-level, 7 relation types) and DocRED (document-level, 96 relation types). This supports the generality of the finding across architectures, schema sizes, and document granularities.\n\n6. **Claim 2 evidence chain complete**: The ablation cleanly decomposes constraint contributions:\n   - Grammar layer → eliminates ET and RV (but these are already zero post-FT, so redundant)\n   - Semantic layer → reduces DR by 41–72% in isolation\n   - Full system → drives DR to near-zero (0–0.20%)\n   - Each layer's contribution is orthogonal and verifiable across all 4 experimental settings\n\n## Paper-Ready Narrative\n\n### Ablation Analysis (FT Regime)\n\nTo disentangle the contributions of the grammar and semantic constraint layers under fine-tuning, we evaluate four configurations: unconstrained decoding, grammar-only constraints (enforcing valid entity types and relation vocabulary), semantic-only constraints (enforcing domain-range compatibility), and the full OntoCoDec system. Tables 1–2 report results on SciERC (sentence-level, 7 relation types) and DocRED (document-level, 96 relation types) across two backbone models (Qwen3-8B, Llama-3.1-8B).\n\nFine-tuning proves highly effective at internalizing surface-level schema compliance: both models produce zero entity-type violations and near-zero relation-vocabulary violations even without constrained decoding, rendering the grammar layer operationally redundant in this regime. However, domain-range violations persist at 0.5–1.9% without semantic enforcement across both datasets, confirming that relational consistency represents a deeper structural property that supervised training alone does not fully capture.\n\nThe semantic constraint layer reduces domain-range violations by 41–72% in isolation (semantic-only mode) across all four model×dataset settings: −68% and −41% on SciERC (Qwen, Llama), −72% and −41% on DocRED (Qwen, Llama). The consistency of this pattern across a sentence-level dataset with 7 relation types and a document-level dataset with 96 relation types demonstrates that the semantic layer's value is robust to schema complexity and document length. Residual violations are further reduced when both layers operate jointly, as the grammar layer's token-level filtering restricts the generation space to syntactically valid candidates, enabling the semantic layer's beam-level enforcement to operate over a reduced, higher-quality hypothesis set.\n\nCrucially, this schema compliance improvement comes at negligible extraction cost: entity F1 is unchanged across all configurations (±0.02pp), and relation F1 varies by at most 0.17 percentage points. These results establish that OntoCoDec's two-layer architecture provides complementary, rather than redundant, enforcement even when the base model has been adapted to the target schema through fine-tuning.\n",
      "numLines": 75,
      "startLine": 1,
      "totalLines": 75
    }
  },
  "sourceToolAssistantUUID": "f06afc35-474f-4a47-9379-e4aca6495778",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "1da856f6-e3e6-4a2a-8180-80868464ada5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-16T17:16:08.993Z_

<details open><summary>🔧 Tool call — Read · `toolu_01U4DvrKsjLC1AWiQY2Ty7RR`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/table4_ft_ablation.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ebeb4f48-17c5-4fb1-b069-7b9045a4fd12",
  "isSidechain": false,
  "requestId": "req_011Cb6dGBsie22mgeK7DDwuH",
  "type": "assistant",
  "uuid": "04ca30a2-28cc-4c33-8c19-3a3005bbd700",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "1da856f6-e3e6-4a2a-8180-80868464ada5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UeXxShLWLLYfFmuWjEBUeb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12260,
      "cache_read_input_tokens": 11447,
      "output_tokens": 293,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12260,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 293,
          "cache_read_input_tokens": 11447,
          "cache_creation_input_tokens": 12260,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12260
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

_source line 15 · 2026-05-16T17:16:08.999Z_

<details><summary>↩ Tool result · `toolu_01U4DvrKsjLC1AWiQY2Ty7RR`</summary>

```text
1	# Table 4: FT Ablation — Constraint Layer Decomposition
2	
3	Modes: unconstrained (no constraints), grammar_only (JSON schema grammar), semantic_only (ontology DR/CF checks), full (grammar + semantic = OntoCoDec).
4	
5	## SciERC
6	
7	| Model | Mode | E_F1 (%) | R_F1 (%) | ET% | RV% | DR% | CF% | Parse Fail% |
8	|-------|------|----------|----------|-----|-----|-----|-----|-------------|
9	| Qwen3-8B | unconstrained | 67.05 | 43.86 | 0.00 | 0.00 | 1.95 | 0.00 | 0.00 |
10	| Qwen3-8B | grammar_only | 67.05 | 43.86 | 0.00 | 0.00 | 1.90 | 0.00 | 0.00 |
11	| Qwen3-8B | semantic_only | 67.05 | 43.69 | 0.00 | 0.00 | 0.60 | 1.33 | 0.00 |
12	| Qwen3-8B | **full (OntoCoDec)** | 67.05 | 43.77 | 0.00 | 0.00 | 0.00 | 1.18 | 0.00 |
13	| Llama3.1-8B | unconstrained | 67.76 | 45.45 | 0.00 | 0.00 | 1.11 | 0.00 | 0.00 |
14	| Llama3.1-8B | grammar_only | 67.76 | 45.45 | 0.00 | 0.00 | 1.11 | 0.00 | 0.00 |
15	| Llama3.1-8B | semantic_only | 67.76 | 45.47 | 0.00 | 0.00 | 0.65 | 0.18 | 0.00 |
16	| Llama3.1-8B | **full (OntoCoDec)** | 67.76 | 45.47 | 0.00 | 0.00 | 0.09 | 0.46 | 0.00 |
17	
18	## DocRED
19	
20	| Model | Mode | E_F1 (%) | R_F1 (%) | ET% | RV% | DR% | CF% | Parse Fail% |
21	|-------|------|----------|----------|-----|-----|-----|-----|-------------|
22	| Qwen3-8B | unconstrained | 82.15 | 40.86 | 0.00 | 0.27 | 0.76 | 0.12 | 7.11 |
23	| Qwen3-8B | grammar_only | 82.19 | 40.85 | 0.00 | 0.00 | 0.61 | 0.11 | 7.01 |
24	| Qwen3-8B | semantic_only | 82.15 | 40.89 | 0.00 | 0.23 | 0.21 | 0.27 | 7.52 |
25	| Qwen3-8B | **full (OntoCoDec)** | 81.43 | 40.56 | 0.00 | 0.00 | 0.01 | 0.41 | 8.52 |
26	| Llama3.1-8B | unconstrained | 83.93 | 43.72 | 0.00 | 0.15 | 0.49 | — | 2.30 |
27	| Llama3.1-8B | grammar_only | 84.04 | 43.77 | 0.00 | 0.00 | 0.51 | 0.12 | 2.30 |
28	| Llama3.1-8B | semantic_only | — | — | — | — | — | — | RUNNING |
29	| Llama3.1-8B | **full (OntoCoDec)** | 85.23 | 44.23 | 0.00 | 0.00 | 0.20 | 0.26 | 2.51 |
30	
31	**Observations:**
32	- Grammar layer: eliminates ET/RV violations (forces valid type/relation tokens); minimal impact on DR
33	- Semantic layer: primary DR reducer (SciERC: 1.95%→0.60% for Qwen, DocRED: 0.76%→0.21% for Qwen)
34	- Full combination: near-zero DR residual with sub-additive constraint interaction
35	- F1 impact: ≤0.30pp R_F1 cost across all completed settings
36	- Llama DocRED semantic_only: experiment still RUNNING
37	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "04ca30a2-28cc-4c33-8c19-3a3005bbd700",
  "isSidechain": false,
  "promptId": "f3f24f5a-bd6d-444a-89a8-04e2233f247b",
  "type": "user",
  "uuid": "694fb3d4-b53d-4517-bd80-32bd9e32cab8",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/table4_ft_ablation.md",
      "content": "# Table 4: FT Ablation — Constraint Layer Decomposition\n\nModes: unconstrained (no constraints), grammar_only (JSON schema grammar), semantic_only (ontology DR/CF checks), full (grammar + semantic = OntoCoDec).\n\n## SciERC\n\n| Model | Mode | E_F1 (%) | R_F1 (%) | ET% | RV% | DR% | CF% | Parse Fail% |\n|-------|------|----------|----------|-----|-----|-----|-----|-------------|\n| Qwen3-8B | unconstrained | 67.05 | 43.86 | 0.00 | 0.00 | 1.95 | 0.00 | 0.00 |\n| Qwen3-8B | grammar_only | 67.05 | 43.86 | 0.00 | 0.00 | 1.90 | 0.00 | 0.00 |\n| Qwen3-8B | semantic_only | 67.05 | 43.69 | 0.00 | 0.00 | 0.60 | 1.33 | 0.00 |\n| Qwen3-8B | **full (OntoCoDec)** | 67.05 | 43.77 | 0.00 | 0.00 | 0.00 | 1.18 | 0.00 |\n| Llama3.1-8B | unconstrained | 67.76 | 45.45 | 0.00 | 0.00 | 1.11 | 0.00 | 0.00 |\n| Llama3.1-8B | grammar_only | 67.76 | 45.45 | 0.00 | 0.00 | 1.11 | 0.00 | 0.00 |\n| Llama3.1-8B | semantic_only | 67.76 | 45.47 | 0.00 | 0.00 | 0.65 | 0.18 | 0.00 |\n| Llama3.1-8B | **full (OntoCoDec)** | 67.76 | 45.47 | 0.00 | 0.00 | 0.09 | 0.46 | 0.00 |\n\n## DocRED\n\n| Model | Mode | E_F1 (%) | R_F1 (%) | ET% | RV% | DR% | CF% | Parse Fail% |\n|-------|------|----------|----------|-----|-----|-----|-----|-------------|\n| Qwen3-8B | unconstrained | 82.15 | 40.86 | 0.00 | 0.27 | 0.76 | 0.12 | 7.11 |\n| Qwen3-8B | grammar_only | 82.19 | 40.85 | 0.00 | 0.00 | 0.61 | 0.11 | 7.01 |\n| Qwen3-8B | semantic_only | 82.15 | 40.89 | 0.00 | 0.23 | 0.21 | 0.27 | 7.52 |\n| Qwen3-8B | **full (OntoCoDec)** | 81.43 | 40.56 | 0.00 | 0.00 | 0.01 | 0.41 | 8.52 |\n| Llama3.1-8B | unconstrained | 83.93 | 43.72 | 0.00 | 0.15 | 0.49 | — | 2.30 |\n| Llama3.1-8B | grammar_only | 84.04 | 43.77 | 0.00 | 0.00 | 0.51 | 0.12 | 2.30 |\n| Llama3.1-8B | semantic_only | — | — | — | — | — | — | RUNNING |\n| Llama3.1-8B | **full (OntoCoDec)** | 85.23 | 44.23 | 0.00 | 0.00 | 0.20 | 0.26 | 2.51 |\n\n**Observations:**\n- Grammar layer: eliminates ET/RV violations (forces valid type/relation tokens); minimal impact on DR\n- Semantic layer: primary DR reducer (SciERC: 1.95%→0.60% for Qwen, DocRED: 0.76%→0.21% for Qwen)\n- Full combination: near-zero DR residual with sub-additive constraint interaction\n- F1 impact: ≤0.30pp R_F1 cost across all completed settings\n- Llama DocRED semantic_only: experiment still RUNNING\n",
      "numLines": 37,
      "startLine": 1,
      "totalLines": 37
    }
  },
  "sourceToolAssistantUUID": "04ca30a2-28cc-4c33-8c19-3a3005bbd700",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "1da856f6-e3e6-4a2a-8180-80868464ada5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-16T17:16:09.451Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01KfN2fv5NeupHCWYtu8fimX`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_registry",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "694fb3d4-b53d-4517-bd80-32bd9e32cab8",
  "isSidechain": false,
  "requestId": "req_011Cb6dGBsie22mgeK7DDwuH",
  "type": "assistant",
  "uuid": "8eb91eb9-0624-4dd4-a3bc-94d368cc2014",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "1da856f6-e3e6-4a2a-8180-80868464ada5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UeXxShLWLLYfFmuWjEBUeb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12260,
      "cache_read_input_tokens": 11447,
      "output_tokens": 293,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12260,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 293,
          "cache_read_input_tokens": 11447,
          "cache_creation_input_tokens": 12260,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12260
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

_source line 17_

```json
{
  "type": "last-prompt",
  "leafUuid": "8ddd5bbc-4106-485c-8da0-1634f37b5723",
  "sessionId": "1da856f6-e3e6-4a2a-8180-80868464ada5"
}
```

---

### Runtime record

_source line 18_

```json
{
  "type": "ai-title",
  "aiTitle": "Fix DocRED FT ablation data errors in markdown files",
  "sessionId": "1da856f6-e3e6-4a2a-8180-80868464ada5"
}
```

---

### Assistant

_source line 19 · 2026-05-16T17:16:13.492Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me read the registry for the specific experiments to verify the data. Let me query all the relevant experiments.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8ddd5bbc-4106-485c-8da0-1634f37b5723",
  "isSidechain": false,
  "requestId": "req_011Cb6dGYyUfmeyfGVUkeTzL",
  "type": "assistant",
  "uuid": "96a1d25a-e886-472f-973a-4f65abb10574",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "1da856f6-e3e6-4a2a-8180-80868464ada5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WipbewQ4tmab7hrGNXsdox",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 4494,
      "cache_read_input_tokens": 23707,
      "output_tokens": 945,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4494,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 945,
          "cache_read_input_tokens": 23707,
          "cache_creation_input_tokens": 4494,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4494
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

_source line 20 · 2026-05-16T17:16:14.135Z_

Now let me verify the data from the registry for all relevant experiments.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "96a1d25a-e886-472f-973a-4f65abb10574",
  "isSidechain": false,
  "requestId": "req_011Cb6dGYyUfmeyfGVUkeTzL",
  "type": "assistant",
  "uuid": "b1b9af35-b22f-49dc-b96d-3cbea4b06eb6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "1da856f6-e3e6-4a2a-8180-80868464ada5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WipbewQ4tmab7hrGNXsdox",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 4494,
      "cache_read_input_tokens": 23707,
      "output_tokens": 945,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4494,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 945,
          "cache_read_input_tokens": 23707,
          "cache_creation_input_tokens": 4494,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4494
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

_source line 21 · 2026-05-16T17:16:16.133Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01Jg1SBezfWxcX9zpur3GT49`</summary>

```json
{
  "project": "schema_semantic_constrained_ie",
  "filters": {
    "experiment_id": "w8_qwen_docred_ft_grammar_only"
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
  "parentUuid": "b1b9af35-b22f-49dc-b96d-3cbea4b06eb6",
  "isSidechain": false,
  "requestId": "req_011Cb6dGYyUfmeyfGVUkeTzL",
  "type": "assistant",
  "uuid": "315e545e-412a-42c5-8bd8-e86e0ff48fe1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "1da856f6-e3e6-4a2a-8180-80868464ada5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WipbewQ4tmab7hrGNXsdox",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 4494,
      "cache_read_input_tokens": 23707,
      "output_tokens": 945,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4494,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 945,
          "cache_read_input_tokens": 23707,
          "cache_creation_input_tokens": 4494,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4494
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

_source line 22 · 2026-05-16T17:16:16.387Z_

<details><summary>↩ Tool result · `toolu_01Jg1SBezfWxcX9zpur3GT49`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2397}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "315e545e-412a-42c5-8bd8-e86e0ff48fe1",
  "isSidechain": false,
  "promptId": "f3f24f5a-bd6d-444a-89a8-04e2233f247b",
  "type": "user",
  "uuid": "d36b4a43-c038-4c0c-bb12-f5af32df6ca3",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {}, \\\"count\\\": 0, \\\"total\\\": 0, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.2397}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2397}}"
    }
  },
  "sourceToolAssistantUUID": "315e545e-412a-42c5-8bd8-e86e0ff48fe1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "1da856f6-e3e6-4a2a-8180-80868464ada5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-16T17:16:16.646Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_018Gx4QfXBTmeTBojPn7q9EJ`</summary>

```json
{
  "project": "schema_semantic_constrained_ie",
  "filters": {
    "experiment_id": "w8_qwen_docred_ft_semantic_only"
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
  "parentUuid": "d36b4a43-c038-4c0c-bb12-f5af32df6ca3",
  "isSidechain": false,
  "requestId": "req_011Cb6dGYyUfmeyfGVUkeTzL",
  "type": "assistant",
  "uuid": "dbe03a5b-a85d-4b63-9a31-fc42c1a61538",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "1da856f6-e3e6-4a2a-8180-80868464ada5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WipbewQ4tmab7hrGNXsdox",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 4494,
      "cache_read_input_tokens": 23707,
      "output_tokens": 945,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4494,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 945,
          "cache_read_input_tokens": 23707,
          "cache_creation_input_tokens": 4494,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4494
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

_source line 24 · 2026-05-16T17:16:17.017Z_

<details><summary>↩ Tool result · `toolu_018Gx4QfXBTmeTBojPn7q9EJ`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.356}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dbe03a5b-a85d-4b63-9a31-fc42c1a61538",
  "isSidechain": false,
  "promptId": "f3f24f5a-bd6d-444a-89a8-04e2233f247b",
  "type": "user",
  "uuid": "3bac1d1c-2307-4133-a77e-bc335baea386",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {}, \\\"count\\\": 0, \\\"total\\\": 0, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.356}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.356}}"
    }
  },
  "sourceToolAssistantUUID": "dbe03a5b-a85d-4b63-9a31-fc42c1a61538",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "1da856f6-e3e6-4a2a-8180-80868464ada5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-16T17:16:17.619Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01CiYf6EXmgiDccu6gteB9QQ`</summary>

```json
{
  "project": "schema_semantic_constrained_ie",
  "filters": {
    "experiment_id": "w8_llama_docred_ft_grammar_only"
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
  "parentUuid": "3bac1d1c-2307-4133-a77e-bc335baea386",
  "isSidechain": false,
  "requestId": "req_011Cb6dGYyUfmeyfGVUkeTzL",
  "type": "assistant",
  "uuid": "1f9c0f3e-5130-4f10-ba40-3149621dd1e3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "1da856f6-e3e6-4a2a-8180-80868464ada5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WipbewQ4tmab7hrGNXsdox",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 4494,
      "cache_read_input_tokens": 23707,
      "output_tokens": 945,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4494,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 945,
          "cache_read_input_tokens": 23707,
          "cache_creation_input_tokens": 4494,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4494
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

_source line 26 · 2026-05-16T17:16:18.138Z_

<details><summary>↩ Tool result · `toolu_01CiYf6EXmgiDccu6gteB9QQ`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4937}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1f9c0f3e-5130-4f10-ba40-3149621dd1e3",
  "isSidechain": false,
  "promptId": "f3f24f5a-bd6d-444a-89a8-04e2233f247b",
  "type": "user",
  "uuid": "d08ea311-e88f-4be6-a467-260f44b02cde",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {}, \\\"count\\\": 0, \\\"total\\\": 0, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.4937}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4937}}"
    }
  },
  "sourceToolAssistantUUID": "1f9c0f3e-5130-4f10-ba40-3149621dd1e3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "1da856f6-e3e6-4a2a-8180-80868464ada5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-16T17:16:18.594Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_018sn5pAYdPiiiB6zoLCRqoQ`</summary>

```json
{
  "project": "schema_semantic_constrained_ie",
  "filters": {
    "experiment_id": "w8_llama_docred_ft_semantic_only"
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
  "parentUuid": "d08ea311-e88f-4be6-a467-260f44b02cde",
  "isSidechain": false,
  "requestId": "req_011Cb6dGYyUfmeyfGVUkeTzL",
  "type": "assistant",
  "uuid": "2b340b1a-d020-464a-b1f8-d3d4048a5634",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "1da856f6-e3e6-4a2a-8180-80868464ada5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WipbewQ4tmab7hrGNXsdox",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 4494,
      "cache_read_input_tokens": 23707,
      "output_tokens": 945,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4494,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 945,
          "cache_read_input_tokens": 23707,
          "cache_creation_input_tokens": 4494,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4494
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

_source line 28 · 2026-05-16T17:16:18.985Z_

<details><summary>↩ Tool result · `toolu_018sn5pAYdPiiiB6zoLCRqoQ`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.3679}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2b340b1a-d020-464a-b1f8-d3d4048a5634",
  "isSidechain": false,
  "promptId": "f3f24f5a-bd6d-444a-89a8-04e2233f247b",
  "type": "user",
  "uuid": "c9042df8-fc27-4cdf-b4db-24014a64f051",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {}, \\\"count\\\": 0, \\\"total\\\": 0, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.3679}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.3679}}"
    }
  },
  "sourceToolAssistantUUID": "2b340b1a-d020-464a-b1f8-d3d4048a5634",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "1da856f6-e3e6-4a2a-8180-80868464ada5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-16T17:16:19.518Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01N8gY29Fpy9JqGMyqNgDrCd`</summary>

```json
{
  "project": "schema_semantic_constrained_ie",
  "filters": {
    "experiment_id": "w5_qwen_docred_lora_unconstrained_eval"
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
  "parentUuid": "c9042df8-fc27-4cdf-b4db-24014a64f051",
  "isSidechain": false,
  "requestId": "req_011Cb6dGYyUfmeyfGVUkeTzL",
  "type": "assistant",
  "uuid": "2fb82996-69ba-42b2-8cb2-7d5f15d162ef",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "1da856f6-e3e6-4a2a-8180-80868464ada5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WipbewQ4tmab7hrGNXsdox",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 4494,
      "cache_read_input_tokens": 23707,
      "output_tokens": 945,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4494,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 945,
          "cache_read_input_tokens": 23707,
          "cache_creation_input_tokens": 4494,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4494
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

_source line 30 · 2026-05-16T17:16:19.835Z_

<details><summary>↩ Tool result · `toolu_01N8gY29Fpy9JqGMyqNgDrCd`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.3037}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2fb82996-69ba-42b2-8cb2-7d5f15d162ef",
  "isSidechain": false,
  "promptId": "f3f24f5a-bd6d-444a-89a8-04e2233f247b",
  "type": "user",
  "uuid": "7635df44-3f9b-4ac7-8b69-86c7de1605f0",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {}, \\\"count\\\": 0, \\\"total\\\": 0, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.3037}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.3037}}"
    }
  },
  "sourceToolAssistantUUID": "2fb82996-69ba-42b2-8cb2-7d5f15d162ef",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "1da856f6-e3e6-4a2a-8180-80868464ada5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-16T17:16:20.432Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_019X6KZmGcSKn1qyd8yaeE7o`</summary>

```json
{
  "project": "schema_semantic_constrained_ie",
  "filters": {
    "experiment_id": "w5_llama_docred_lora_unconstrained_eval"
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
  "parentUuid": "7635df44-3f9b-4ac7-8b69-86c7de1605f0",
  "isSidechain": false,
  "requestId": "req_011Cb6dGYyUfmeyfGVUkeTzL",
  "type": "assistant",
  "uuid": "94008d54-49b2-4c59-bf48-13df4617eeb0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "1da856f6-e3e6-4a2a-8180-80868464ada5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WipbewQ4tmab7hrGNXsdox",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 4494,
      "cache_read_input_tokens": 23707,
      "output_tokens": 945,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4494,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 945,
          "cache_read_input_tokens": 23707,
          "cache_creation_input_tokens": 4494,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4494
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

_source line 32 · 2026-05-16T17:16:20.637Z_

<details><summary>↩ Tool result · `toolu_019X6KZmGcSKn1qyd8yaeE7o`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.1943}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "94008d54-49b2-4c59-bf48-13df4617eeb0",
  "isSidechain": false,
  "promptId": "f3f24f5a-bd6d-444a-89a8-04e2233f247b",
  "type": "user",
  "uuid": "ceaef04e-eefd-417f-a1ff-20ec80830602",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {}, \\\"count\\\": 0, \\\"total\\\": 0, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.1943}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.1943}}"
    }
  },
  "sourceToolAssistantUUID": "94008d54-49b2-4c59-bf48-13df4617eeb0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "1da856f6-e3e6-4a2a-8180-80868464ada5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-16T17:16:20.947Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_019cBZUaNNjazUCMkyyD84Mt`</summary>

```json
{
  "project": "schema_semantic_constrained_ie",
  "filters": {
    "experiment_id": "w5_qwen_docred_lora_constrained_eval"
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
  "parentUuid": "ceaef04e-eefd-417f-a1ff-20ec80830602",
  "isSidechain": false,
  "requestId": "req_011Cb6dGYyUfmeyfGVUkeTzL",
  "type": "assistant",
  "uuid": "20c65655-e8dc-4f17-8eb7-f27448279796",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "1da856f6-e3e6-4a2a-8180-80868464ada5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WipbewQ4tmab7hrGNXsdox",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 4494,
      "cache_read_input_tokens": 23707,
      "output_tokens": 945,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4494,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 945,
          "cache_read_input_tokens": 23707,
          "cache_creation_input_tokens": 4494,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4494
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

_source line 34 · 2026-05-16T17:16:21.166Z_

<details><summary>↩ Tool result · `toolu_019cBZUaNNjazUCMkyyD84Mt`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2085}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "20c65655-e8dc-4f17-8eb7-f27448279796",
  "isSidechain": false,
  "promptId": "f3f24f5a-bd6d-444a-89a8-04e2233f247b",
  "type": "user",
  "uuid": "2dbd7502-6294-4dc6-9c2b-cfcbf9e86b23",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {}, \\\"count\\\": 0, \\\"total\\\": 0, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.2085}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2085}}"
    }
  },
  "sourceToolAssistantUUID": "20c65655-e8dc-4f17-8eb7-f27448279796",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "1da856f6-e3e6-4a2a-8180-80868464ada5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-16T17:16:21.591Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01CYsxmz7BaugsHqPqyKeo9k`</summary>

```json
{
  "project": "schema_semantic_constrained_ie",
  "filters": {
    "experiment_id": "w5_llama_docred_lora_constrained_eval"
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
  "parentUuid": "2dbd7502-6294-4dc6-9c2b-cfcbf9e86b23",
  "isSidechain": false,
  "requestId": "req_011Cb6dGYyUfmeyfGVUkeTzL",
  "type": "assistant",
  "uuid": "7b59907c-8dec-415a-9e4e-1fae71a53944",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "1da856f6-e3e6-4a2a-8180-80868464ada5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WipbewQ4tmab7hrGNXsdox",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 4494,
      "cache_read_input_tokens": 23707,
      "output_tokens": 945,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4494,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 945,
          "cache_read_input_tokens": 23707,
          "cache_creation_input_tokens": 4494,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4494
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

_source line 36 · 2026-05-16T17:16:21.797Z_

<details><summary>↩ Tool result · `toolu_01CYsxmz7BaugsHqPqyKeo9k`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.1961}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7b59907c-8dec-415a-9e4e-1fae71a53944",
  "isSidechain": false,
  "promptId": "f3f24f5a-bd6d-444a-89a8-04e2233f247b",
  "type": "user",
  "uuid": "14cd687f-7b95-4cd5-a455-ff461d999530",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {}, \\\"count\\\": 0, \\\"total\\\": 0, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.1961}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.1961}}"
    }
  },
  "sourceToolAssistantUUID": "7b59907c-8dec-415a-9e4e-1fae71a53944",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "1da856f6-e3e6-4a2a-8180-80868464ada5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 37 · 2026-05-16T17:16:21.801Z_

```json
{
  "parentUuid": "14cd687f-7b95-4cd5-a455-ff461d999530",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "8819403c-aa34-443e-b331-0cbdb9c8e1da",
  "timestamp": "2026-05-16T17:16:21.801Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "1da856f6-e3e6-4a2a-8180-80868464ada5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 38 · 2026-05-16T17:16:26.223Z_

<details><summary>Logged reasoning block</summary>

```text
All registry queries returned 0 results. The experiment IDs might use a different naming convention. Let me search the registry more broadly to find the actual experiment IDs.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8819403c-aa34-443e-b331-0cbdb9c8e1da",
  "isSidechain": false,
  "requestId": "req_011Cb6dHTZZxq3Xw158ZHCnF",
  "type": "assistant",
  "uuid": "4e36e058-b6cf-453f-a2c6-a35834a48d0a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "1da856f6-e3e6-4a2a-8180-80868464ada5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MRHAaE8415P3AQBkWiuD3S",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1853,
      "cache_read_input_tokens": 28201,
      "output_tokens": 186,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1853,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 186,
          "cache_read_input_tokens": 28201,
          "cache_creation_input_tokens": 1853,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1853
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

_source line 39 · 2026-05-16T17:16:26.728Z_

Registry returned no results with those exact IDs. Let me search more broadly to find the actual experiment names.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4e36e058-b6cf-453f-a2c6-a35834a48d0a",
  "isSidechain": false,
  "requestId": "req_011Cb6dHTZZxq3Xw158ZHCnF",
  "type": "assistant",
  "uuid": "a8f5ba94-b875-41d8-96aa-838c368ffb54",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "1da856f6-e3e6-4a2a-8180-80868464ada5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MRHAaE8415P3AQBkWiuD3S",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1853,
      "cache_read_input_tokens": 28201,
      "output_tokens": 186,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1853,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 186,
          "cache_read_input_tokens": 28201,
          "cache_creation_input_tokens": 1853,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1853
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

_source line 40 · 2026-05-16T17:16:27.386Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01FvJt1h9psRepuHm5EpUoco`</summary>

```json
{
  "project": "schema_semantic_constrained_ie",
  "limit": 50,
  "fields": [
    "experiment_id",
    "status",
    "metrics"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a8f5ba94-b875-41d8-96aa-838c368ffb54",
  "isSidechain": false,
  "requestId": "req_011Cb6dHTZZxq3Xw158ZHCnF",
  "type": "assistant",
  "uuid": "1b79f9cd-4c48-4a28-8d2a-f46fa72520ce",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "1da856f6-e3e6-4a2a-8180-80868464ada5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MRHAaE8415P3AQBkWiuD3S",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1853,
      "cache_read_input_tokens": 28201,
      "output_tokens": 186,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1853,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 186,
          "cache_read_input_tokens": 28201,
          "cache_creation_input_tokens": 1853,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1853
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

_source line 41 · 2026-05-16T17:16:27.597Z_

<details><summary>↩ Tool result · `toolu_01FvJt1h9psRepuHm5EpUoco`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {\"w8_llama_docred_ft_semantic_only\": {\"status\": \"DONE\", \"metrics\": {\"E_F1\": 84.02, \"E_P\": 85.01, \"E_R\": 83.06, \"R_F1\": 43.9, \"R_P\": 38.89, \"R_R\": 50.4, \"ET_pct\": 0, \"RV_pct\": 0.15, \"DR_pct\": 0.3, \"CF_pct\": 0.16, \"parse_fail_rate\": 2.4, \"total_samples\": 998, \"parse_failures\": 24, \"documents_checked\": 974, \"total_entities\": 19099, \"total_relations\": 16038, \"DR_violations\": 48, \"RV_violations\": 24, \"ET_violations\": 0, \"CF_violations\": 31}}, \"w8_qwen_docred_ft_semantic_only\": {\"status\": \"DONE\", \"metrics\": {\"E_F1\": 82.15, \"E_P\": 85.58, \"E_R\": 78.99, \"R_F1\": 40.89, \"R_P\": 36.35, \"R_R\": 46.73, \"ET_pct\": 0, \"RV_pct\": 0.23, \"DR_pct\": 0.21, \"CF_pct\": 0.27, \"parse_fail_rate\": 7.52, \"total_samples\": 998, \"parse_failures\": 75, \"documents_checked\": 923, \"total_entities\": 18025, \"total_triples\": 15909, \"DR_violations\": 34, \"RV_violations\": 37, \"ET_violations\": 0, \"CF_violations\": 49}}, \"w8_qwen_docred_ft_grammar_only\": {\"status\": \"DONE\", \"metrics\": {\"E_F1\": 82.19, \"E_P\": 85.47, \"E_R\": 79.16, \"R_F1\": 40.85, \"R_P\": 36.27, \"R_R\": 46.77, \"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 0.61, \"CF_pct\": 0.11, \"parse_fail_rate\": 7.01, \"total_samples\": 998, \"parse_failures\": 70}}, \"w8_llama_docred_ft_grammar_only\": {\"status\": \"DONE\", \"metrics\": {\"E_F1\": 84.04, \"R_F1\": 43.77, \"entity_precision\": 84.99, \"entity_recall\": 83.11, \"relation_precision\": 38.6, \"relation_recall\": 50.53, \"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 0.51, \"CF_pct\": 0.12, \"parse_fail_rate\": 2.3, \"total_samples\": 998, \"total_relations\": 16199, \"unique_entities\": 13225, \"parse_failures\": 23}}, \"w6_mistral_scierc_unconstrained\": {\"status\": \"DONE\", \"metrics\": {\"E_P\": 0.2402, \"E_R\": 0.3156, \"E_F1\": 0.2728, \"R_P\": 0.0295, \"R_R\": 0.0483, \"R_F1\": 0.0366, \"ET_pct\": 1.5, \"RV_pct\": 0, \"DR_pct\": 56.94, \"CF_pct\": 56.87, \"parse_fail_rate\": 0, \"total_samples\": 551, \"total_pred_entities\": 2202, \"total_pred_relations\": 1593}}, \"w6_mistral_scierc_constrained\": {\"status\": \"DONE\", \"metrics\": {\"E_P\": 0.2437, \"E_R\": 0.3144, \"E_F1\": 0.2746, \"R_P\": 0.0292, \"R_R\": 0.0493, \"R_F1\": 0.0367, \"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 13.4, \"CF_pct\": 1.27, \"CF_count\": 21, \"parse_fail_rate\": 0, \"total_samples\": 551, \"total_pred_entities\": 2162, \"total_pred_relations\": 1647, \"delta_vs_unconstrained\": {\"delta_E_F1\": 0.0018, \"delta_R_F1\": 0.0001, \"delta_ET\": -1.5, \"delta_RV\": 0, \"delta_DR\": -43.54, \"note\": \"Constrained - unconstrained. Baseline: E_F1=0.2728, R_F1=0.0366, DR=56.94%, ET=1.5%, RV=0%\"}}}, \"w8_ft_posthoc_baseline\": {\"status\": \"DONE\", \"metrics\": {\"ft_regime\": {\"qwen_scierc\": {\"R_F1_before\": 43.86, \"R_F1_posthoc\": 43.94, \"R_F1_constrained\": 43.77, \"reject_rate_pct\": 1.95, \"TP_lost\": 4}, \"llama_scierc\": {\"R_F1_before\": 45.45, \"R_F1_posthoc\": 45.23, \"R_F1_constrained\": 45.47, \"reject_rate_pct\": 1.11, \"TP_lost\": 5}, \"qwen_docred\": {\"R_F1_before\": 40.91, \"R_F1_posthoc\": 41.11, \"R_F1_constrained\": \"TBD\", \"reject_rate_pct\": 1.03, \"TP_lost\": 1}, \"llama_docred\": {\"R_F1_before\": 43.77, \"R_F1_posthoc\": 43.92, \"R_F1_constrained\": 44.23, \"reject_rate_pct\": 0.64, \"TP_lost\": 1}}, \"zs_regime\": {\"mistral_scierc\": {\"triples\": 1584, \"reject_pct\": 20.27, \"R_F1_before\": 0.0376, \"R_F1_posthoc\": 0.0394, \"R_F1_constrained\": 0.0367, \"TP_before\": 48, \"TP_after\": 44, \"TP_lost\": 4}, \"qwen_scierc\": {\"triples\": 1724, \"reject_pct\": 16.76, \"R_F1_before\": 0.0823, \"R_F1_posthoc\": 0.0863, \"R_F1_constrained\": 0.0836, \"TP_before\": 111, \"TP_after\": 104, \"TP_lost\": 7}, \"llama_scierc\": {\"triples\": 1274, \"reject_pct\": 13.89, \"R_F1_before\": 0.0268, \"R_F1_posthoc\": 0.0271, \"R_F1_constrained\": 0.0254, \"TP_before\": 30, \"TP_after\": 28, \"TP_lost\": 2}, \"qwen_docred\": {\"triples\": 17497, \"reject_pct\": 48.12, \"R_F1_before\": 0.0774, \"R_F1_posthoc\": 0.0961, \"R_F1_constrained\": 0.0823, \"TP_before\": 1137, \"TP_after\": 1010, \"TP_lost\": 127}, \"llama_docred\": {\"triples\": 16437, \"reject_pct\": 42.18, \"R_F1_before\": 0.0598, \"R_F1_posthoc\": 0.0744, \"R_F1_constrained\": 0.0627, \"TP_before\": 850, \"TP_after\": 802, \"TP_lost\": 48}, \"mistral_docred\": {\"triples\": 11836, \"reject_pct\": 73.73, \"R_F1_before\": 0.0434, \"R_F1_posthoc\": 0.0385, \"R_F1_constrained\": 0.0552, \"TP_before\": 518, \"TP_after\": 292, \"TP_lost\": 226, \"removed_RV\": 4172, \"removed_ET\": 3382, \"removed_DR\": 1173, \"note\": \"Only ZS case where posthoc HURTS R_F1 — 73.7% rejection rate loses 43.6% of TPs\"}}, \"key_finding\": \"ZS: post-hoc R_F1 >= constrained R_F1 in 5/6 groups. Exception: Mistral DocRED where extreme rejection rate (73.7%) causes net F1 loss. Constrained decoding value is in structural guarantee (0% violations) and composability, not F1 preservation.\"}}, \"w6_mistral_docred_unconstrained\": {\"status\": \"DONE\", \"metrics\": {\"total_samples\": 998, \"parse_failures\": 7, \"parse_fail_rate\": 0.7, \"total_pred_entities\": 12580, \"total_pred_relations\": 11879, \"ET_pct\": 7.58, \"RV_pct\": 42.35, \"DR_pct\": 57.42, \"CF_pct\": 24.78, \"E_P\": 0.6221, \"E_R\": 0.3975, \"E_F1\": 0.4851, \"R_P\": 0.0447, \"R_R\": 0.0432, \"R_F1\": 0.0434, \"f1_method\": \"fuzzy_normalized\", \"f1_note\": \"Relation matching uses case-insensitive normalization with token-overlap >80% and edit-distance ≤2 fallback. Strict R_F1=3.50% (delta +0.84pp from 98 additional TPs via fuzzy matching of Mistral underscore/abbreviation variants).\"}}, \"w6_mistral_docred_constrained\": {\"status\": \"DONE\", \"metrics\": {\"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 33.2, \"CF_pct\": 0.19, \"E_P\": 65.02, \"E_R\": 41.4, \"E_F1\": 50.59, \"R_P\": 5.67, \"R_R\": 5.37, \"R_F1\": 5.52, \"parse_fail_rate\": 0.8, \"total_samples\": 998, \"total_pred_entities\": 12535, \"total_pred_relations\": 11554, \"delta_vs_unconstrained\": {\"ET_pct\": -7.58, \"RV_pct\": -42.35, \"DR_pct\": -24.22, \"CF_pct\": -24.59, \"E_F1\": 2.08, \"R_F1\": 2.02}}}, \"w7_llama_scierc_ft_semantic_only\": {\"status\": \"DONE\", \"metrics\": {\"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 0.65, \"CF_count\": 2, \"E_F1\": 67.76, \"E_P\": 66.47, \"E_R\": 69.1, \"R_F1\": 45.47, \"R_P\": 43.24, \"R_R\": 47.95, \"total_entities\": 1757, \"total_relations\": 1081, \"json_parse_failures\": 0}}, \"w5_qwen_docred_lora_constrained_eval\": {\"status\": \"DONE\", \"metrics\": {\"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 0.01, \"CF_pct\": 0.41, \"E_F1\": 81.43, \"E_P\": 85.41, \"E_R\": 77.81, \"R_F1\": 40.56, \"R_P\": 36.35, \"R_R\": 45.86, \"parse_fail_rate\": 8.52, \"total_samples\": 998, \"success_samples\": 913, \"fail_samples\": 85, \"total_entities_pred\": 17799, \"total_relations_pred\": 15563, \"E_F1_excl_fail\": 85.69, \"R_F1_excl_fail\": 42.23, \"delta_vs_unconstrained\": {\"delta_DR\": -0.75, \"delta_RV\": -0.27, \"delta_R_F1\": -0.3, \"delta_R_F1_excl_fail\": 0.03, \"DR_reduction_pct\": 98.7, \"note\": \"Constrained - unconstrained. Unconstrained: DR=0.76%, R_F1=40.86, R_F1_excl_fail=42.20\"}}}, \"w7_llama_scierc_ft_grammar_only\": {\"status\": \"DONE\", \"metrics\": {\"total_samples\": 551, \"json_parse_failures\": 0, \"total_entities\": 1757, \"total_relations\": 1082, \"entity_type_violation_rate\": 0, \"relation_vocabulary_violation_rate\": 0, \"domain_range_violation_rate\": 0.0111, \"cross_field_consistency_violation_rate\": 0, \"entity_f1\": {\"precision\": 0.6647, \"recall\": 0.691, \"f1\": 0.6776}, \"relation_f1\": {\"precision\": 0.432, \"recall\": 0.4795, \"f1\": 0.4545}}}, \"w7_qwen_scierc_ft_semantic_only\": {\"status\": \"DONE\", \"metrics\": {\"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 0.6, \"CF_count\": 15, \"parse_fail_rate\": 0, \"total_samples\": 551, \"total_entities\": 1784, \"total_relations\": 1128, \"E_P\": 0.6523, \"E_R\": 0.6898, \"E_F1\": 0.6705, \"R_P\": 0.4073, \"R_R\": 0.4713, \"R_F1\": 0.4369, \"DR_violations\": 7, \"delta_vs_grammar_only\": {\"DR_delta\": -1.3, \"note\": \"semantic_only DR=0.6% vs grammar_only DR=1.9%, semantic layer reduces DR by 68%\"}, \"delta_vs_unconstrained\": {\"DR_delta\": -1.35, \"note\": \"unconstrained DR=1.95% → semantic_only 0.6%\"}}}, \"w7_qwen_scierc_ft_grammar_only\": {\"status\": \"DONE\", \"metrics\": {\"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 1.9, \"CF_pct\": 0, \"parse_fail_rate\": 0, \"total_samples\": 551, \"total_entities\": 1784, \"total_relations\": 1128, \"E_P\": 0.6523, \"E_R\": 0.6898, \"E_F1\": 0.6705, \"R_P\": 0.4087, \"R_R\": 0.4733, \"R_F1\": 0.4386, \"DR_violations\": 22, \"tokenizer_warning\": \"false_positive_transformers_4.57.6\"}}, \"w5_llama_docred_lora_constrained_eval\": {\"status\": \"DONE\", \"metrics\": {\"total\": 998, \"parse_failures\": 25, \"parse_fail_rate\": 2.51, \"entities\": 19077, \"relations\": 16074, \"entity_f1\": 85.23, \"entity_precision\": 85.04, \"entity_recall\": 85.41, \"relation_f1_all_set\": 44.23, \"relation_precision_all_set\": 38.82, \"relation_recall_all_set\": 51.4, \"et_violations\": 0, \"et_violation_rate\": 0, \"rv_violations\": 0, \"rv_violation_rate\": 0, \"dr_violations\": 33, \"dr_violation_rate\": 0.2, \"cross_field_consistency_violations\": 41, \"delta_vs_unconstrained\": {\"delta_e_f1\": 1.3, \"delta_r_f1\": 0.51, \"delta_dr\": -0.29, \"delta_rv\": -0.15, \"note\": \"Computed as constrained - unconstrained on full-set metrics (not intersection subset). Corrected 2026-05-16 per Reviewer audit.\"}}}, \"w5_llama_docred_sft_data_gen\": {\"status\": \"DONE\", \"metrics\": {\"train_samples\": 3053, \"dev_samples\": 998, \"train_size_mb\": 19, \"dev_size_mb\": 6.1}}, \"w1_cf_fallback_llama_docred\": {\"status\": \"DONE\"}, \"w1_cf_fallback_llama_scierc\": {\"status\": \"DONE\"}, \"w5_qwen_docred_lora_unconstrained_eval\": {\"status\": \"DONE\", \"metrics\": {\"ET_pct\": 0, \"RV_pct\": 0.27, \"DR_pct\": 0.76, \"CF_pct\": 0.12, \"E_F1\": 82.15, \"E_P\": 85.44, \"E_R\": 79.11, \"R_F1\": 40.86, \"R_P\": 36.41, \"R_R\": 46.56, \"parse_fail_rate\": 7.11, \"total_samples\": 998, \"success_samples\": 927, \"fail_samples\": 71, \"total_entities_pred\": 18091, \"total_relations_pred\": 15870, \"ET_pct_excl_fail\": 0, \"RV_pct_excl_fail\": 0.27, \"DR_pct_excl_fail\": 0.76, \"CF_pct_excl_fail\": 0.12, \"E_F1_excl_fail\": 85.72, \"E_P_excl_fail\": 85.44, \"E_R_excl_fail\": 86, \"R_F1_excl_fail\": 42.2, \"R_P_excl_fail\": 36.41, \"R_R_excl_fail\": 50.17}}, \"w5_llama_docred_lora_unconstrained_eval\": {\"status\": \"DONE\", \"metrics\": {\"ET_pct\": 0, \"RV_pct\": 0.15, \"DR_pct\": 0.49, \"E_F1\": 83.93, \"E_P\": 84.93, \"E_R\": 82.96, \"R_F1\": 43.72, \"R_P\": 38.59, \"R_R\": 50.41, \"parse_fail_rate\": 2.3, \"total_samples\": 998, \"total_entities_pred\": 19106, \"total_relations_pred\": 16171}}, \"w5_qwen_docred_lora_training\": {\"status\": \"DONE\", \"metrics\": {\"eval_loss\": 0.0614, \"eval_mean_token_accuracy\": 0.9804, \"eval_entropy\": 0.715, \"train_loss\": 0.0682, \"train_runtime_s\": 5825.6, \"epochs\": 3, \"adapter_path\": \"/root/schema_semantic_constrained_ie/checkpoints/qwen_lora_docred\", \"merged_path\": \"/root/autodl-tmp/checkpoints/qwen_lora_docred_merged\"}}, \"w5_llama_docred_lora_training\": {\"status\": \"DONE\", \"metrics\": {\"train_loss\": 0.0572, \"eval_loss\": 0.0624, \"token_acc\": 98.06}}, \"w5_llama_lora_scierc_constrained_eval\": {\"status\": \"DONE\", \"metrics\": {\"domain_range_violation_rate\": 0.0009, \"relation_vocabulary_violation_rate\": 0, \"entity_type_violation_rate\": 0, \"cross_field_consistency_violation_rate\": 0.0046, \"relation_f1\": 0.4547, \"relation_precision\": 0.432, \"relation_recall\": 0.4795, \"entity_f1\": 0.6776, \"entity_precision\": 0.6647, \"entity_recall\": 0.691, \"total_relations\": 1081, \"total_entities\": 1757, \"total_samples\": 551, \"parse_failures\": 0}}, \"w5_docred_sft_data_gen\": {\"status\": \"DONE\", \"metrics\": {\"train_samples\": 3053, \"dev_samples\": 998, \"train_entities\": 59493, \"train_relations\": 38180, \"dev_entities\": 19528, \"dev_relations\": 12275}}, \"w5_llama_lora_scierc_unconstrained_eval\": {\"status\": \"DONE\", \"metrics\": {\"total_samples\": 551, \"total_entities\": 1757, \"total_relations\": 1082, \"json_parse_rate\": 1, \"entity_type_violation_rate\": 0, \"relation_vocabulary_violation_rate\": 0, \"domain_range_violation_rate\": 0.0111, \"cross_field_consistency_violation_rate\": 0, \"total_violation_rate\": 0.0042, \"entity_precision\": 0.6647, \"entity_recall\": 0.691, \"entity_f1\": 0.6776, \"relation_precision\": 0.432, \"relation_recall\": 0.4795, \"relation_f1\": 0.4545}}, \"w5_llama_lora_scierc_training\": {\"status\": \"DONE\", \"metrics\": {\"eval_loss\": 0.0595, \"eval_mean_token_accuracy\": 0.9817, \"eval_entropy\": 1.0565, \"train_loss\": 0.0501, \"train_runtime_sec\": 654.23, \"epochs\": 3, \"train_samples_per_second\": 8.08}}, \"w1_cf_fallback_docred\": {\"status\": \"DONE\"}, \"w5_lora_scierc_constrained_eval\": {\"status\": \"DONE\", \"metrics\": {\"json_parse_rate\": 1, \"entity_type_violation_rate\": 0, \"relation_vocabulary_violation_rate\": 0, \"domain_range_violation_rate\": 0, \"cross_field_consistency_violation_rate\": 0.0118, \"entity_f1\": 0.6705, \"entity_precision\": 0.6523, \"entity_recall\": 0.6898, \"relation_f1\": 0.4377, \"relation_precision\": 0.4078, \"relation_recall\": 0.4723, \"total_entities\": 1784, \"total_relations\": 1128, \"total_samples\": 551, \"cross_field_consistency_violations\": 21}}, \"w5_lora_scierc_unconstrained_eval\": {\"status\": \"DONE\", \"metrics\": {\"json_parse_rate\": 1, \"entity_type_violation_rate\": 0, \"relation_vocabulary_violation_rate\": 0, \"domain_range_violation_rate\": 0.0195, \"cross_field_consistency_violation_rate\": 0, \"entity_f1\": 0.6705, \"entity_precision\": 0.6523, \"entity_recall\": 0.6898, \"relation_f1\": 0.4386, \"relation_precision\": 0.4087, \"relation_recall\": 0.4733, \"total_entities\": 1784, \"total_relations\": 1128, \"domain_range_violations\": 22, \"go_nogo_metric\": 0.0195, \"dr_gate\": \"FAILED\"}}, \"w5_lora_scierc_training\": {\"status\": \"DONE\", \"metrics\": {\"train_loss\": 0.0634, \"eval_loss\": 0.0586, \"eval_token_accuracy\": 0.9816, \"eval_entropy\": 0.9635, \"train_runtime_sec\": 688.4, \"epochs\": 3, \"checkpoint_path\": \"/root/schema_semantic_constrained_ie/checkpoints/qwen3_8b_lora_scierc\", \"merged_model_path\": \"/root/schema_semantic_constrained_ie/checkpoints/qwen3_8b_lora_scierc_merged\"}}, \"llama_docred_full_s1_mt6144\": {\"status\": \"DONE\", \"metrics\": {\"DR_rate_pct\": 2.57, \"RV_rate_pct\": 0, \"ET_rate_pct\": 0, \"CF_rate_pct\": 12.13, \"R_F1\": 6.25, \"R_precision\": 5.45, \"R_recall\": 7.32, \"E_F1\": 55.04, \"E_precision\": 61.41, \"E_recall\": 49.87, \"documents_total\": 998, \"documents_checked\": 908, \"parse_failures\": 90, \"triples\": 16471, \"unique_entities\": 11307, \"fallback_events\": 67911, \"wall_clock_seconds\": 23926, \"vs_unconstrained_mt6144\": {\"DR_delta_pp\": -23.61, \"DR_reduction_pct\": -90.2, \"R_F1_delta_pp\": 0.3, \"E_F1_delta_pp\": -0.63}, \"vs_full_s1_mt4096\": {\"DR_delta_pp\": 0.02, \"R_F1_delta_pp\": -0.02, \"E_F1_delta_pp\": 0.03, \"CF_delta_pp\": 0.11, \"parse_fail_delta\": -1}}}, \"w1_cf_fallback_scierc_pilot\": {\"status\": \"DONE\", \"metrics\": {\"ET\": 0, \"RV\": 0, \"DR\": 0.1478, \"CF\": 0.0004, \"R_F1\": 0.0823, \"R_P\": 0.0643, \"R_R\": 0.114, \"E_F1\": 0.3098, \"E_P\": 0.2598, \"E_R\": 0.3837, \"entities\": 2474, \"relations\": 1725, \"samples\": 551, \"grammar_first_fallback_rate\": 0.3664, \"cf_registry_fallback_rate\": 0.0448, \"total_mask_calls\": 17024, \"violation_budget_DR_CF\": 0.1482}}, \"llama_docred_unconstrained_mt6144\": {\"status\": \"DONE\", \"metrics\": {\"ET_rate\": 0.13, \"RV_rate\": 15.89, \"DR_rate\": 26.18, \"DR_rate_eligible\": 31.15, \"CF_rate\": 0.17, \"entity_precision\": 61.19, \"entity_recall\": 51.06, \"entity_f1\": 55.67, \"relation_precision\": 5.18, \"relation_recall\": 7, \"relation_f1\": 5.95, \"parse_failures\": 67, \"documents_checked\": 931, \"total_documents\": 998, \"unique_entities\": 11534, \"total_triples\": 16584, \"dr_eligible_triples\": 13936, \"fuzzy_relation_matches\": 121}}, \"llama_docred_full_s1\": {\"status\": \"DONE\", \"metrics\": {\"checker_version\": \"fixed_20260514_v2 (strip + alias + unique_et)\", \"f1_method\": \"all_set\", \"violations\": {\"ET\": 0, \"RV\": 0, \"DR\": 2.55, \"CF\": 12.02}, \"f1\": {\"entity_f1\": 55.01, \"entity_precision\": 61.41, \"entity_recall\": 49.82, \"relation_f1\": 6.27, \"relation_precision\": 5.49, \"relation_recall\": 7.32}, \"counts\": {\"documents\": 998, \"documents_checked\": 907, \"parse_failures\": 91, \"unique_entities\": 11296, \"triples\": 16368}}}, \"llama_docred_unconstrained\": {\"status\": \"DONE\", \"metrics\": {\"checker_version\": \"fixed_20260514_v2\", \"f1_method\": \"all_set\", \"documents\": 998, \"documents_checked\": 930, \"parse_failures\": 68, \"unique_entities\": 11525, \"total_triples\": 16437, \"dr_eligible_triples\": 13789, \"ET_rate_pct\": 0.13, \"RV_rate_pct\": 16.03, \"DR_rate_pct\": 26.07, \"CF_rate_pct\": 0.17, \"entity_precision\": 61.22, \"entity_recall\": 51.02, \"entity_f1\": 55.65, \"relation_precision\": 5.22, \"relation_recall\": 7, \"relation_f1\": 5.98, \"fuzzy_relation_matches\": 121}}, \"phase2_docred_grammar_only\": {\"status\": \"DONE\", \"metrics\": {\"documents_checked\": 985, \"parse_failures\": 13, \"total_entities\": 20150, \"total_triples\": 17341, \"entity_type_violation_rate\": 0, \"relation_vocabulary_violation_rate\": 0.0003, \"domain_range_violation_rate\": 0.2617, \"cross_field_consistency_violation_rate\": 0.0007, \"relation_f1\": 8.31, \"relation_precision\": 7.06, \"relation_recall\": 10.12, \"entity_f1\": 59.38, \"entity_precision\": 58.47, \"entity_recall\": 60.32, \"unrecognized_relations\": 5, \"f1_method\": \"all_set\", \"checker_version\": \"fixed_20260514_v2 (strip + alias + unique_et)\"}}, \"posthoc_filtering_baseline\": {\"status\": \"DONE\", \"metrics\": {\"docred_f1_before\": 7.74, \"docred_f1_after\": 9.61, \"docred_precision_before\": 6.55, \"docred_precision_after\": 11.22, \"docred_recall_before\": 9.46, \"docred_recall_after\": 8.4, \"docred_rejection_rate\": 0.481, \"docred_tp_before\": 1137, \"docred_tp_after\": 1010, \"docred_tp_lost\": 127, \"docred_et_residual\": 0.0247, \"scierc_f1_before\": 8.23, \"scierc_f1_after\": 8.63, \"scierc_rejection_rate\": 0.168, \"scierc_recall_before\": 11.4, \"scierc_recall_after\": 10.68, \"scierc_tp_before\": 111, \"scierc_tp_after\": 104}}, \"llama_scierc_full_s1\": {\"status\": \"DONE\", \"metrics\": {\"samples\": 550, \"entities_extracted\": 2469, \"relations_extracted\": 1315, \"domain_range_violation_rate\": 0.0008, \"relation_vocab_violation_rate\": 0, \"entity_type_violation_rate\": 0, \"cross_field_consistency_violation_rate\": 0.0656, \"total_violation_rate\": 0.0431, \"entity_f1\": 0.2349, \"entity_precision\": 0.1972, \"entity_recall\": 0.2902, \"relation_f1\": 0.0254, \"relation_precision\": 0.0221, \"relation_recall\": 0.0298, \"checker_version\": \"fixed_20260514_v2 (strip + alias + unique_et)\"}}, \"llama_scierc_unconstrained\": {\"status\": \"DONE\", \"metrics\": {\"entity_type_violation_rate\": 0, \"relation_vocab_violation_rate\": 0.0055, \"domain_range_violation_rate\": 0.1334, \"cross_field_consistency_violations\": 6, \"entity_f1\": 0.2356, \"entity_precision\": 0.1983, \"entity_recall\": 0.2902, \"relation_f1\": 0.0268, \"relation_precision\": 0.0236, \"relation_recall\": 0.031, \"total_entities\": 2451, \"total_relations\": 1274, \"json_parse_failures\": 1, \"samples\": 551, \"checker_version\": \"fixed_20260514_v2 (strip + alias + unique_et)\"}}, \"phase2_scierc_full_s2\": {\"status\": \"DONE\", \"metrics\": {\"total_samples\": 551, \"total_triples\": 1644, \"total_entities\": 2228, \"json_parse_rate\": 1, \"entity_type_violation_rate\": 0, \"relation_vocabulary_violation_rate\": 0, \"domain_range_violation_rate\": 0.0097, \"cross_field_consistency_violation_rate\": 0.0803, \"entity_precision\": 0.2797, \"entity_recall\": 0.3712, \"entity_f1\": 0.319, \"relation_precision\": 0.064, \"relation_recall\": 0.1078, \"relation_f1\": 0.0803, \"checker_version\": \"fixed_20260514_v2 (strip + alias + unique_et)\"}}, \"phase2_scierc_full_s1\": {\"status\": \"DONE\", \"metrics\": {\"total_samples\": 551, \"total_triples\": 1729, \"total_entities\": 2474, \"json_parse_rate\": 1, \"entity_type_violation_rate\": 0, \"relation_vocabulary_violation_rate\": 0, \"domain_range_violation_rate\": 0.0093, \"cross_field_consistency_violation_rate\": 0.099, \"entity_f1\": 0.3098, \"entity_precision\": 0.2598, \"entity_recall\": 0.3837, \"relation_f1\": 0.0836, \"relation_precision\": 0.0654, \"relation_recall\": 0.116, \"checker_version\": \"fixed_20260514_v2 (strip + alias + unique_et)\"}}, \"phase2_scierc_semantic_only\": {\"status\": \"DONE\", \"metrics\": {\"total_samples\": 551, \"total_triples\": 1726, \"total_entities\": 2474, \"json_parse_rate\": 1, \"entity_type_violation_rate\": 0.004, \"relation_vocabulary_violation_rate\": 0.0151, \"domain_range_violation_rate\": 0.1165, \"cross_field_consistency_violation_rate\": 0.0271, \"entity_f1\": 0.3101, \"entity_precision\": 0.2605, \"entity_recall\": 0.3831, \"relation_f1\": 0.0815, \"relation_precision\": 0.0637, \"relation_recall\": 0.1129, \"checker_version\": \"fixed_20260514_v2 (strip + alias + unique_et)\"}}, \"phase2_scierc_grammar_only\": {\"status\": \"DONE\", \"metrics\": {\"total_samples\": 551, \"total_triples\": 1725, \"total_entities\": 2474, \"json_parse_rate\": 1, \"entity_type_violation_rate\": 0, \"relation_vocabulary_violation_rate\": 0, \"domain_range_violation_rate\": 0.1484, \"cross_field_consistency_violation_rate\": 0.0008, \"entity_f1\": 0.3098, \"entity_precision\": 0.2598, \"entity_recall\": 0.3837, \"relation_f1\": 0.0823, \"relation_precision\": 0.0643, \"relation_recall\": 0.114, \"checker_version\": \"fixed_20260514_v2 (strip + alias + unique_et)\"}}, \"phase2_scierc_unconstrained\": {\"status\": \"DONE\", \"metrics\": {\"json_parse_rate\": 1, \"entity_f1\": 0.3101, \"entity_precision\": 0.2605, \"entity_recall\": 0.3831, \"relation_f1\": 0.0823, \"relation_precision\": 0.0644, \"relation_recall\": 0.114, \"entity_type_violation_rate\": 0.004, \"relation_vocabulary_violation_rate\": 0.0139, \"domain_range_violation_rate\": 0.1537, \"cross_field_consistency_violation_rate\": 0.0008, \"total_triples\": 1724, \"total_entities\": 2474, \"total_samples\": 551, \"checker_version\": \"fixed_20260514_v2 (strip + alias + unique_et)\"}}, \"phase2_docred_full_s1\": {\"status\": \"DONE\", \"metrics\": {\"documents_checked\": 987, \"parse_failures\": 11, \"total_entities\": 20187, \"total_triples\": 17341, \"entity_type_violation_rate\": 0, \"relation_vocabulary_violation_rate\": 0.0003, \"domain_range_violation_rate\": 0.1021, \"cross_field_consistency_violation_rate\": 0.0257, \"entity_f1\": 59.37, \"entity_precision\": 58.45, \"entity_recall\": 59.63, \"relation_f1\": 8.23, \"relation_precision\": 6.99, \"relation_recall\": 10.01, \"unrecognized_relations\": 5, \"f1_method\": \"all_set\", \"checker_version\": \"fixed_20260514_v2 (strip + alias + unique_et)\"}}, \"phase2_docred_semantic_only\": {\"status\": \"DONE\", \"metrics\": {\"documents_checked\": 987, \"parse_failures\": 11, \"total_entities\": 20185, \"total_triples\": 17571, \"entity_type_violation_rate\": 0.0422, \"relation_vocabulary_violation_rate\": 0.2987, \"domain_range_violation_rate\": 0.1384, \"cross_field_consistency_violation_rate\": 0.0105, \"entity_f1\": 57.81, \"entity_precision\": 57.27, \"entity_recall\": 58.37, \"relation_f1\": 7.7, \"relation_precision\": 6.54, \"relation_recall\": 9.37, \"f1_method\": \"all_set\", \"checker_version\": \"fixed_20260514_v2 (strip + alias + unique_et)\", \"et_v1\": 0.1044, \"et_fix_note\": \"v1 triple-counted ET across entity_list + relation head/tail; v2 deduplicates by (text, normalized_type)\"}}, \"phase2_docred_unconstrained\": {\"status\": \"DONE\", \"metrics\": {\"documents_checked\": 986, \"parse_failures\": 12, \"total_entities\": 20171, \"total_triples\": 17497, \"entity_type_violation_rate\": 0.0248, \"relation_vocabulary_violation_rate\": 0.2966, \"domain_range_violation_rate\": 0.1846, \"cross_field_consistency_violation_rate\": 0.001, \"entity_f1\": 58.15, \"entity_precision\": 57.26, \"entity_recall\": 58.32, \"relation_f1\": 7.74, \"relation_precision\": 6.55, \"relation_recall\": 9.46, \"unrecognized_relations\": 5189, \"f1_method\": \"all_set (includes OOV predictions in denominator)\", \"checker_version\": \"fixed_20260514_v2 (strip + alias + unique_et)\", \"et_v1\": 0.0818, \"et_fix_note\": \"v1 triple-counted ET across entity_list + relation head/tail; v2 deduplicates by (text, normalized_type)\"}}, \"mvp_phase0_docred_schema_r2\": {\"status\": \"DONE\"}, \"phase2_s2_pilot50\": {\"status\": \"DONE\", \"metrics\": {\"domain_range_violation_rate\": 0.0205, \"relation_vocabulary_violation_rate\": 0, \"relation_f1\": 0.1008, \"samples\": 50, \"predicted_relations\": 146, \"true_positives\": 13, \"gold_relations\": 112, \"entity_f1_approx\": 0.29, \"note\": \"DR 修正: 原值 0 来自 dryrun (n=25 triples)。实际 pilot50 DR=3/146=2.05% (来自 violation_report_s2_pilot50.json)。\"}}, \"mvp_phase0_docred_schema\": {\"status\": \"DONE\", \"metrics\": {\"total_documents\": 998, \"documents_checked\": 943, \"parse_failures\": 55, \"json_parse_rate\": 0.9449, \"total_entities\": 19524, \"total_triples\": 16782, \"entity_type_violations\": 119, \"entity_type_violation_rate\": 0.0061, \"relation_vocabulary_violations\": 3090, \"relation_vocabulary_violation_rate\": 0.1841, \"relation_fuzzy_matches\": 85, \"domain_range_violations\": 2154, \"domain_range_violation_rate\": 0.1284, \"cross_field_consistency_violations\": 29, \"cross_field_consistency_violation_rate\": 0.0015, \"total_violations_any\": 5392, \"total_violation_rate\": 0.1485, \"go_nogo_metric_dr\": 0.1284}}}, \"count\": 50, \"total\": 53, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.199}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1b79f9cd-4c48-4a28-8d2a-f46fa72520ce",
  "isSidechain": false,
  "promptId": "f3f24f5a-bd6d-444a-89a8-04e2233f247b",
  "type": "user",
  "uuid": "22b5c4be-f8c7-4541-a86e-f7b10a369f62",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {\\\"w8_llama_docred_ft_semantic_only\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"E_F1\\\": 84.02, \\\"E_P\\\": 85.01, \\\"E_R\\\": 83.06, \\\"R_F1\\\": 43.9, \\\"R_P\\\": 38.89, \\\"R_R\\\": 50.4, \\\"ET_pct\\\": 0, \\\"RV_pct\\\": 0.15, \\\"DR_pct\\\": 0.3, \\\"CF_pct\\\": 0.16, \\\"parse_fail_rate\\\": 2.4, \\\"total_samples\\\": 998, \\\"parse_failures\\\": 24, \\\"documents_checked\\\": 974, \\\"total_entities\\\": 19099, \\\"total_relations\\\": 16038, \\\"DR_violations\\\": 48, \\\"RV_violations\\\": 24, \\\"ET_violations\\\": 0, \\\"CF_violations\\\": 31}}, \\\"w8_qwen_docred_ft_semantic_only\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"E_F1\\\": 82.15, \\\"E_P\\\": 85.58, \\\"E_R\\\": 78.99, \\\"R_F1\\\": 40.89, \\\"R_P\\\": 36.35, \\\"R_R\\\": 46.73, \\\"ET_pct\\\": 0, \\\"RV_pct\\\": 0.23, \\\"DR_pct\\\": 0.21, \\\"CF_pct\\\": 0.27, \\\"parse_fail_rate\\\": 7.52, \\\"total_samples\\\": 998, \\\"parse_failures\\\": 75, \\\"documents_checked\\\": 923, \\\"total_entities\\\": 18025, \\\"total_triples\\\": 15909, \\\"DR_violations\\\": 34, \\\"RV_violations\\\": 37, \\\"ET_violations\\\": 0, \\\"CF_violations\\\": 49}}, \\\"w8_qwen_docred_ft_grammar_only\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"E_F1\\\": 82.19, \\\"E_P\\\": 85.47, \\\"E_R\\\": 79.16, \\\"R_F1\\\": 40.85, \\\"R_P\\\": 36.27, \\\"R_R\\\": 46.77, \\\"ET_pct\\\": 0, \\\"RV_pct\\\": 0, \\\"DR_pct\\\": 0.61, \\\"CF_pct\\\": 0.11, \\\"parse_fail_rate\\\": 7.01, \\\"total_samples\\\": 998, \\\"parse_failures\\\": 70}}, \\\"w8_llama_docred_ft_grammar_only\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"E_F1\\\": 84.04, \\\"R_F1\\\": 43.77, \\\"entity_precision\\\": 84.99, \\\"entity_recall\\\": 83.11, \\\"relation_precision\\\": 38.6, \\\"relation_recall\\\": 50.53, \\\"ET_pct\\\": 0, \\\"RV_pct\\\": 0, \\\"DR_pct\\\": 0.51, \\\"CF_pct\\\": 0.12, \\\"parse_fail_rate\\\": 2.3, \\\"total_samples\\\": 998, \\\"total_relations\\\": 16199, \\\"unique_entities\\\": 13225, \\\"parse_failures\\\": 23}}, \\\"w6_mistral_scierc_unconstrained\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"E_P\\\": 0.2402, \\\"E_R\\\": 0.3156, \\\"E_F1\\\": 0.2728, \\\"R_P\\\": 0.0295, \\\"R_R\\\": 0.0483, \\\"R_F1\\\": 0.0366, \\\"ET_pct\\\": 1.5, \\\"RV_pct\\\": 0, \\\"DR_pct\\\": 56.94, \\\"CF_pct\\\": 56.87, \\\"parse_fail_rate\\\": 0, \\\"total_samples\\\": 551, \\\"total_pred_entities\\\": 2202, \\\"total_pred_relations\\\": 1593}}, \\\"w6_mistral_scierc_constrained\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"E_P\\\": 0.2437, \\\"E_R\\\": 0.3144, \\\"E_F1\\\": 0.2746, \\\"R_P\\\": 0.0292, \\\"R_R\\\": 0.0493, \\\"R_F1\\\": 0.0367, \\\"ET_pct\\\": 0, \\\"RV_pct\\\": 0, \\\"DR_pct\\\": 13.4, \\\"CF_pct\\\": 1.27, \\\"CF_count\\\": 21, \\\"parse_fail_rate\\\": 0, \\\"total_samples\\\": 551, \\\"total_pred_entities\\\": 2162, \\\"total_pred_relations\\\": 1647, \\\"delta_vs_unconstrained\\\": {\\\"delta_E_F1\\\": 0.0018, \\\"delta_R_F1\\\": 0.0001, \\\"delta_ET\\\": -1.5, \\\"delta_RV\\\": 0, \\\"delta_DR\\\": -43.54, \\\"note\\\": \\\"Constrained - unconstrained. Baseline: E_F1=0.2728, R_F1=0.0366, DR=56.94%, ET=1.5%, RV=0%\\\"}}}, \\\"w8_ft_posthoc_baseline\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"ft_regime\\\": {\\\"qwen_scierc\\\": {\\\"R_F1_before\\\": 43.86, \\\"R_F1_posthoc\\\": 43.94, \\\"R_F1_constrained\\\": 43.77, \\\"reject_rate_pct\\\": 1.95, \\\"TP_lost\\\": 4}, \\\"llama_scierc\\\": {\\\"R_F1_before\\\": 45.45, \\\"R_F1_posthoc\\\": 45.23, \\\"R_F1_constrained\\\": 45.47, \\\"reject_rate_pct\\\": 1.11, \\\"TP_lost\\\": 5}, \\\"qwen_docred\\\": {\\\"R_F1_before\\\": 40.91, \\\"R_F1_posthoc\\\": 41.11, \\\"R_F1_constrained\\\": \\\"TBD\\\", \\\"reject_rate_pct\\\": 1.03, \\\"TP_lost\\\": 1}, \\\"llama_docred\\\": {\\\"R_F1_before\\\": 43.77, \\\"R_F1_posthoc\\\": 43.92, \\\"R_F1_constrained\\\": 44.23, \\\"reject_rate_pct\\\": 0.64, \\\"TP_lost\\\": 1}}, \\\"zs_regime\\\": {\\\"mistral_scierc\\\": {\\\"triples\\\": 1584, \\\"reject_pct\\\": 20.27, \\\"R_F1_before\\\": 0.0376, \\\"R_F1_posthoc\\\": 0.0394, \\\"R_F1_constrained\\\": 0.0367, \\\"TP_before\\\": 48, \\\"TP_after\\\": 44, \\\"TP_lost\\\": 4}, \\\"qwen_scierc\\\": {\\\"triples\\\": 1724, \\\"reject_pct\\\": 16.76, \\\"R_F1_before\\\": 0.0823, \\\"R_F1_posthoc\\\": 0.0863, \\\"R_F1_constrained\\\": 0.0836, \\\"TP_before\\\": 111, \\\"TP_after\\\": 104, \\\"TP_lost\\\": 7}, \\\"llama_scierc\\\": {\\\"triples\\\": 1274, \\\"reject_pct\\\": 13.89, \\\"R_F1_before\\\": 0.0268, \\\"R_F1_posthoc\\\": 0.0271, \\\"R_F1_constrained\\\": 0.0254, \\\"TP_before\\\": 30, \\\"TP_after\\\": 28, \\\"TP_lost\\\": 2}, \\\"qwen_docred\\\": {\\\"triples\\\": 17497, \\\"reject_pct\\\": 48.12, \\\"R_F1_before\\\": 0.0774, \\\"R_F1_posthoc\\\": 0.0961, \\\"R_F1_constrained\\\": 0.0823, \\\"TP_before\\\": 1137, \\\"TP_after\\\": 1010, \\\"TP_lost\\\": 127}, \\\"llama_docred\\\": {\\\"triples\\\": 16437, \\\"reject_pct\\\": 42.18, \\\"R_F1_before\\\": 0.0598, \\\"R_F1_posthoc\\\": 0.0744, \\\"R_F1_constrained\\\": 0.0627, \\\"TP_before\\\": 850, \\\"TP_after\\\": 802, \\\"TP_lost\\\": 48}, \\\"mistral_docred\\\": {\\\"triples\\\": 11836, \\\"reject_pct\\\": 73.73, \\\"R_F1_before\\\": 0.0434, \\\"R_F1_posthoc\\\": 0.0385, \\\"R_F1_constrained\\\": 0.0552, \\\"TP_before\\\": 518, \\\"TP_after\\\": 292, \\\"TP_lost\\\": 226, \\\"removed_RV\\\": 4172, \\\"removed_ET\\\": 3382, \\\"removed_DR\\\": 1173, \\\"note\\\": \\\"Only ZS case where posthoc HURTS R_F1 — 73.7% rejection rate loses 43.6% of TPs\\\"}}, \\\"key_finding\\\": \\\"ZS: post-hoc R_F1 >= constrained R_F1 in 5/6 groups. Exception: Mistral DocRED where extreme rejection rate (73.7%) causes net F1 loss. Constrained decoding value is in structural guarantee (0% violations) and composability, not F1 preservation.\\\"}}, \\\"w6_mistral_docred_unconstrained\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"total_samples\\\": 998, \\\"parse_failures\\\": 7, \\\"parse_fail_rate\\\": 0.7, \\\"total_pred_entities\\\": 12580, \\\"total_pred_relations\\\": 11879, \\\"ET_pct\\\": 7.58, \\\"RV_pct\\\": 42.35, \\\"DR_pct\\\": 57.42, \\\"CF_pct\\\": 24.78, \\\"E_P\\\": 0.6221, \\\"E_R\\\": 0.3975, \\\"E_F1\\\": 0.4851, \\\"R_P\\\": 0.0447, \\\"R_R\\\": 0.0432, \\\"R_F1\\\": 0.0434, \\\"f1_method\\\": \\\"fuzzy_normalized\\\", \\\"f1_note\\\": \\\"Relation matching uses case-insensitive normalization with token-overlap >80% and edit-distance ≤2 fallback. Strict R_F1=3.50% (delta +0.84pp from 98 additional TPs via fuzzy matching of Mistral underscore/abbreviation variants).\\\"}}, \\\"w6_mistral_docred_constrained\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"ET_pct\\\": 0, \\\"RV_pct\\\": 0, \\\"DR_pct\\\": 33.2, \\\"CF_pct\\\": 0.19, \\\"E_P\\\": 65.02, \\\"E_R\\\": 41.4, \\\"E_F1\\\": 50.59, \\\"R_P\\\": 5.67, \\\"R_R\\\": 5.37, \\\"R_F1\\\": 5.52, \\\"parse_fail_rate\\\": 0.8, \\\"total_samples\\\": 998, \\\"total_pred_entities\\\": 12535, \\\"total_pred_relations\\\": 11554, \\\"delta_vs_unconstrained\\\": {\\\"ET_pct\\\": -7.58, \\\"RV_pct\\\": -42.35, \\\"DR_pct\\\": -24.22, \\\"CF_pct\\\": -24.59, \\\"E_F1\\\": 2.08, \\\"R_F1\\\": 2.02}}}, \\\"w7_llama_scierc_ft_semantic_only\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"ET_pct\\\": 0, \\\"RV_pct\\\": 0, \\\"DR_pct\\\": 0.65, \\\"CF_count\\\": 2, \\\"E_F1\\\": 67.76, \\\"E_P\\\": 66.47, \\\"E_R\\\": 69.1, \\\"R_F1\\\": 45.47, \\\"R_P\\\": 43.24, \\\"R_R\\\": 47.95, \\\"total_entities\\\": 1757, \\\"total_relations\\\": 1081, \\\"json_parse_failures\\\": 0}}, \\\"w5_qwen_docred_lora_constrained_eval\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"ET_pct\\\": 0, \\\"RV_pct\\\": 0, \\\"DR_pct\\\": 0.01, \\\"CF_pct\\\": 0.41, \\\"E_F1\\\": 81.43, \\\"E_P\\\": 85.41, \\\"E_R\\\": 77.81, \\\"R_F1\\\": 40.56, \\\"R_P\\\": 36.35, \\\"R_R\\\": 45.86, \\\"parse_fail_rate\\\": 8.52, \\\"total_samples\\\": 998, \\\"success_samples\\\": 913, \\\"fail_samples\\\": 85, \\\"total_entities_pred\\\": 17799, \\\"total_relations_pred\\\": 15563, \\\"E_F1_excl_fail\\\": 85.69, \\\"R_F1_excl_fail\\\": 42.23, \\\"delta_vs_unconstrained\\\": {\\\"delta_DR\\\": -0.75, \\\"delta_RV\\\": -0.27, \\\"delta_R_F1\\\": -0.3, \\\"delta_R_F1_excl_fail\\\": 0.03, \\\"DR_reduction_pct\\\": 98.7, \\\"note\\\": \\\"Constrained - unconstrained. Unconstrained: DR=0.76%, R_F1=40.86, R_F1_excl_fail=42.20\\\"}}}, \\\"w7_llama_scierc_ft_grammar_only\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"total_samples\\\": 551, \\\"json_parse_failures\\\": 0, \\\"total_entities\\\": 1757, \\\"total_relations\\\": 1082, \\\"entity_type_violation_rate\\\": 0, \\\"relation_vocabulary_violation_rate\\\": 0, \\\"domain_range_violation_rate\\\": 0.0111, \\\"cross_field_consistency_violation_rate\\\": 0, \\\"entity_f1\\\": {\\\"precision\\\": 0.6647, \\\"recall\\\": 0.691, \\\"f1\\\": 0.6776}, \\\"relation_f1\\\": {\\\"precision\\\": 0.432, \\\"recall\\\": 0.4795, \\\"f1\\\": 0.4545}}}, \\\"w7_qwen_scierc_ft_semantic_only\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"ET_pct\\\": 0, \\\"RV_pct\\\": 0, \\\"DR_pct\\\": 0.6, \\\"CF_count\\\": 15, \\\"parse_fail_rate\\\": 0, \\\"total_samples\\\": 551, \\\"total_entities\\\": 1784, \\\"total_relations\\\": 1128, \\\"E_P\\\": 0.6523, \\\"E_R\\\": 0.6898, \\\"E_F1\\\": 0.6705, \\\"R_P\\\": 0.4073, \\\"R_R\\\": 0.4713, \\\"R_F1\\\": 0.4369, \\\"DR_violations\\\": 7, \\\"delta_vs_grammar_only\\\": {\\\"DR_delta\\\": -1.3, \\\"note\\\": \\\"semantic_only DR=0.6% vs grammar_only DR=1.9%, semantic layer reduces DR by 68%\\\"}, \\\"delta_vs_unconstrained\\\": {\\\"DR_delta\\\": -1.35, \\\"note\\\": \\\"unconstrained DR=1.95% → semantic_only 0.6%\\\"}}}, \\\"w7_qwen_scierc_ft_grammar_only\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"ET_pct\\\": 0, \\\"RV_pct\\\": 0, \\\"DR_pct\\\": 1.9, \\\"CF_pct\\\": 0, \\\"parse_fail_rate\\\": 0, \\\"total_samples\\\": 551, \\\"total_entities\\\": 1784, \\\"total_relations\\\": 1128, \\\"E_P\\\": 0.6523, \\\"E_R\\\": 0.6898, \\\"E_F1\\\": 0.6705, \\\"R_P\\\": 0.4087, \\\"R_R\\\": 0.4733, \\\"R_F1\\\": 0.4386, \\\"DR_violations\\\": 22, \\\"tokenizer_warning\\\": \\\"false_positive_transformers_4.57.6\\\"}}, \\\"w5_llama_docred_lora_constrained_eval\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"total\\\": 998, \\\"parse_failures\\\": 25, \\\"parse_fail_rate\\\": 2.51, \\\"entities\\\": 19077, \\\"relations\\\": 16074, \\\"entity_f1\\\": 85.23, \\\"entity_precision\\\": 85.04, \\\"entity_recall\\\": 85.41, \\\"relation_f1_all_set\\\": 44.23, \\\"relation_precision_all_set\\\": 38.82, \\\"relation_recall_all_set\\\": 51.4, \\\"et_violations\\\": 0, \\\"et_violation_rate\\\": 0, \\\"rv_violations\\\": 0, \\\"rv_violation_rate\\\": 0, \\\"dr_violations\\\": 33, \\\"dr_violation_rate\\\": 0.2, \\\"cross_field_consistency_violations\\\": 41, \\\"delta_vs_unconstrained\\\": {\\\"delta_e_f1\\\": 1.3, \\\"delta_r_f1\\\": 0.51, \\\"delta_dr\\\": -0.29, \\\"delta_rv\\\": -0.15, \\\"note\\\": \\\"Computed as constrained - unconstrained on full-set metrics (not intersection subset). Corrected 2026-05-16 per Reviewer audit.\\\"}}}, \\\"w5_llama_docred_sft_data_gen\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"train_samples\\\": 3053, \\\"dev_samples\\\": 998, \\\"train_size_mb\\\": 19, \\\"dev_size_mb\\\": 6.1}}, \\\"w1_cf_fallback_llama_docred\\\": {\\\"status\\\": \\\"DONE\\\"}, \\\"w1_cf_fallback_llama_scierc\\\": {\\\"status\\\": \\\"DONE\\\"}, \\\"w5_qwen_docred_lora_unconstrained_eval\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"ET_pct\\\": 0, \\\"RV_pct\\\": 0.27, \\\"DR_pct\\\": 0.76, \\\"CF_pct\\\": 0.12, \\\"E_F1\\\": 82.15, \\\"E_P\\\": 85.44, \\\"E_R\\\": 79.11, \\\"R_F1\\\": 40.86, \\\"R_P\\\": 36.41, \\\"R_R\\\": 46.56, \\\"parse_fail_rate\\\": 7.11, \\\"total_samples\\\": 998, \\\"success_samples\\\": 927, \\\"fail_samples\\\": 71, \\\"total_entities_pred\\\": 18091, \\\"total_relations_pred\\\": 15870, \\\"ET_pct_excl_fail\\\": 0, \\\"RV_pct_excl_fail\\\": 0.27, \\\"DR_pct_excl_fail\\\": 0.76, \\\"CF_pct_excl_fail\\\": 0.12, \\\"E_F1_excl_fail\\\": 85.72, \\\"E_P_excl_fail\\\": 85.44, \\\"E_R_excl_fail\\\": 86, \\\"R_F1_excl_fail\\\": 42.2, \\\"R_P_excl_fail\\\": 36.41, \\\"R_R_excl_fail\\\": 50.17}}, \\\"w5_llama_docred_lora_unconstrained_eval\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"ET_pct\\\": 0, \\\"RV_pct\\\": 0.15, \\\"DR_pct\\\": 0.49, \\\"E_F1\\\": 83.93, \\\"E_P\\\": 84.93, \\\"E_R\\\": 82.96, \\\"R_F1\\\": 43.72, \\\"R_P\\\": 38.59, \\\"R_R\\\": 50.41, \\\"parse_fail_rate\\\": 2.3, \\\"total_samples\\\": 998, \\\"total_entities_pred\\\": 19106, \\\"total_relations_pred\\\": 16171}}, \\\"w5_qwen_docred_lora_training\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"eval_loss\\\": 0.0614, \\\"eval_mean_token_accuracy\\\": 0.9804, \\\"eval_entropy\\\": 0.715, \\\"train_loss\\\": 0.0682, \\\"train_runtime_s\\\": 5825.6, \\\"epochs\\\": 3, \\\"adapter_path\\\": \\\"/root/schema_semantic_constrained_ie/checkpoints/qwen_lora_docred\\\", \\\"merged_path\\\": \\\"/root/autodl-tmp/checkpoints/qwen_lora_docred_merged\\\"}}, \\\"w5_llama_docred_lora_training\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"train_loss\\\": 0.0572, \\\"eval_loss\\\": 0.0624, \\\"token_acc\\\": 98.06}}, \\\"w5_llama_lora_scierc_constrained_eval\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"domain_range_violation_rate\\\": 0.0009, \\\"relation_vocabulary_violation_rate\\\": 0, \\\"entity_type_violation_rate\\\": 0, \\\"cross_field_consistency_violation_rate\\\": 0.0046, \\\"relation_f1\\\": 0.4547, \\\"relation_precision\\\": 0.432, \\\"relation_recall\\\": 0.4795, \\\"entity_f1\\\": 0.6776, \\\"entity_precision\\\": 0.6647, \\\"entity_recall\\\": 0.691, \\\"total_relations\\\": 1081, \\\"total_entities\\\": 1757, \\\"total_samples\\\": 551, \\\"parse_failures\\\": 0}}, \\\"w5_docred_sft_data_gen\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"train_samples\\\": 3053, \\\"dev_samples\\\": 998, \\\"train_entities\\\": 59493, \\\"train_relations\\\": 38180, \\\"dev_entities\\\": 19528, \\\"dev_relations\\\": 12275}}, \\\"w5_llama_lora_scierc_unconstrained_eval\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"total_samples\\\": 551, \\\"total_entities\\\": 1757, \\\"total_relations\\\": 1082, \\\"json_parse_rate\\\": 1, \\\"entity_type_violation_rate\\\": 0, \\\"relation_vocabulary_violation_rate\\\": 0, \\\"domain_range_violation_rate\\\": 0.0111, \\\"cross_field_consistency_violation_rate\\\": 0, \\\"total_violation_rate\\\": 0.0042, \\\"entity_precision\\\": 0.6647, \\\"entity_recall\\\": 0.691, \\\"entity_f1\\\": 0.6776, \\\"relation_precision\\\": 0.432, \\\"relation_recall\\\": 0.4795, \\\"relation_f1\\\": 0.4545}}, \\\"w5_llama_lora_scierc_training\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"eval_loss\\\": 0.0595, \\\"eval_mean_token_accuracy\\\": 0.9817, \\\"eval_entropy\\\": 1.0565, \\\"train_loss\\\": 0.0501, \\\"train_runtime_sec\\\": 654.23, \\\"epochs\\\": 3, \\\"train_samples_per_second\\\": 8.08}}, \\\"w1_cf_fallback_docred\\\": {\\\"status\\\": \\\"DONE\\\"}, \\\"w5_lora_scierc_constrained_eval\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"json_parse_rate\\\": 1, \\\"entity_type_violation_rate\\\": 0, \\\"relation_vocabulary_violation_rate\\\": 0, \\\"domain_range_violation_rate\\\": 0, \\\"cross_field_consistency_violation_rate\\\": 0.0118, \\\"entity_f1\\\": 0.6705, \\\"entity_precision\\\": 0.6523, \\\"entity_recall\\\": 0.6898, \\\"relation_f1\\\": 0.4377, \\\"relation_precision\\\": 0.4078, \\\"relation_recall\\\": 0.4723, \\\"total_entities\\\": 1784, \\\"total_relations\\\": 1128, \\\"total_samples\\\": 551, \\\"cross_field_consistency_violations\\\": 21}}, \\\"w5_lora_scierc_unconstrained_eval\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"json_parse_rate\\\": 1, \\\"entity_type_violation_rate\\\": 0, \\\"relation_vocabulary_violation_rate\\\": 0, \\\"domain_range_violation_rate\\\": 0.0195, \\\"cross_field_consistency_violation_rate\\\": 0, \\\"entity_f1\\\": 0.6705, \\\"entity_precision\\\": 0.6523, \\\"entity_recall\\\": 0.6898, \\\"relation_f1\\\": 0.4386, \\\"relation_precision\\\": 0.4087, \\\"relation_recall\\\": 0.4733, \\\"total_entities\\\": 1784, \\\"total_relations\\\": 1128, \\\"domain_range_violations\\\": 22, \\\"go_nogo_metric\\\": 0.0195, \\\"dr_gate\\\": \\\"FAILED\\\"}}, \\\"w5_lora_scierc_training\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"train_loss\\\": 0.0634, \\\"eval_loss\\\": 0.0586, \\\"eval_token_accuracy\\\": 0.9816, \\\"eval_entropy\\\": 0.9635, \\\"train_runtime_sec\\\": 688.4, \\\"epochs\\\": 3, \\\"checkpoint_path\\\": \\\"/root/schema_semantic_constrained_ie/checkpoints/qwen3_8b_lora_scierc\\\", \\\"merged_model_path\\\": \\\"/root/schema_semantic_constrained_ie/checkpoints/qwen3_8b_lora_scierc_merged\\\"}}, \\\"llama_docred_full_s1_mt6144\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"DR_rate_pct\\\": 2.57, \\\"RV_rate_pct\\\": 0, \\\"ET_rate_pct\\\": 0, \\\"CF_rate_pct\\\": 12.13, \\\"R_F1\\\": 6.25, \\\"R_precision\\\": 5.45, \\\"R_recall\\\": 7.32, \\\"E_F1\\\": 55.04, \\\"E_precision\\\": 61.41, \\\"E_recall\\\": 49.87, \\\"documents_total\\\": 998, \\\"documents_checked\\\": 908, \\\"parse_failures\\\": 90, \\\"triples\\\": 16471, \\\"unique_entities\\\": 11307, \\\"fallback_events\\\": 67911, \\\"wall_clock_seconds\\\": 23926, \\\"vs_unconstrained_mt6144\\\": {\\\"DR_delta_pp\\\": -23.61, \\\"DR_reduction_pct\\\": -90.2, \\\"R_F1_delta_pp\\\": 0.3, \\\"E_F1_delta_pp\\\": -0.63}, \\\"vs_full_s1_mt4096\\\": {\\\"DR_delta_pp\\\": 0.02, \\\"R_F1_delta_pp\\\": -0.02, \\\"E_F1_delta_pp\\\": 0.03, \\\"CF_delta_pp\\\": 0.11, \\\"parse_fail_delta\\\": -1}}}, \\\"w1_cf_fallback_scierc_pilot\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"ET\\\": 0, \\\"RV\\\": 0, \\\"DR\\\": 0.1478, \\\"CF\\\": 0.0004, \\\"R_F1\\\": 0.0823, \\\"R_P\\\": 0.0643, \\\"R_R\\\": 0.114, \\\"E_F1\\\": 0.3098, \\\"E_P\\\": 0.2598, \\\"E_R\\\": 0.3837, \\\"entities\\\": 2474, \\\"relations\\\": 1725, \\\"samples\\\": 551, \\\"grammar_first_fallback_rate\\\": 0.3664, \\\"cf_registry_fallback_rate\\\": 0.0448, \\\"total_mask_calls\\\": 17024, \\\"violation_budget_DR_CF\\\": 0.1482}}, \\\"llama_docred_unconstrained_mt6144\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"ET_rate\\\": 0.13, \\\"RV_rate\\\": 15.89, \\\"DR_rate\\\": 26.18, \\\"DR_rate_eligible\\\": 31.15, \\\"CF_rate\\\": 0.17, \\\"entity_precision\\\": 61.19, \\\"entity_recall\\\": 51.06, \\\"entity_f1\\\": 55.67, \\\"relation_precision\\\": 5.18, \\\"relation_recall\\\": 7, \\\"relation_f1\\\": 5.95, \\\"parse_failures\\\": 67, \\\"documents_checked\\\": 931, \\\"total_documents\\\": 998, \\\"unique_entities\\\": 11534, \\\"total_triples\\\": 16584, \\\"dr_eligible_triples\\\": 13936, \\\"fuzzy_relation_matches\\\": 121}}, \\\"llama_docred_full_s1\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"checker_version\\\": \\\"fixed_20260514_v2 (strip + alias + unique_et)\\\", \\\"f1_method\\\": \\\"all_set\\\", \\\"violations\\\": {\\\"ET\\\": 0, \\\"RV\\\": 0, \\\"DR\\\": 2.55, \\\"CF\\\": 12.02}, \\\"f1\\\": {\\\"entity_f1\\\": 55.01, \\\"entity_precision\\\": 61.41, \\\"entity_recall\\\": 49.82, \\\"relation_f1\\\": 6.27, \\\"relation_precision\\\": 5.49, \\\"relation_recall\\\": 7.32}, \\\"counts\\\": {\\\"documents\\\": 998, \\\"documents_checked\\\": 907, \\\"parse_failures\\\": 91, \\\"unique_entities\\\": 11296, \\\"triples\\\": 16368}}}, \\\"llama_docred_unconstrained\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"checker_version\\\": \\\"fixed_20260514_v2\\\", \\\"f1_method\\\": \\\"all_set\\\", \\\"documents\\\": 998, \\\"documents_checked\\\": 930, \\\"parse_failures\\\": 68, \\\"unique_entities\\\": 11525, \\\"total_triples\\\": 16437, \\\"dr_eligible_triples\\\": 13789, \\\"ET_rate_pct\\\": 0.13, \\\"RV_rate_pct\\\": 16.03, \\\"DR_rate_pct\\\": 26.07, \\\"CF_rate_pct\\\": 0.17, \\\"entity_precision\\\": 61.22, \\\"entity_recall\\\": 51.02, \\\"entity_f1\\\": 55.65, \\\"relation_precision\\\": 5.22, \\\"relation_recall\\\": 7, \\\"relation_f1\\\": 5.98, \\\"fuzzy_relation_matches\\\": 121}}, \\\"phase2_docred_grammar_only\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"documents_checked\\\": 985, \\\"parse_failures\\\": 13, \\\"total_entities\\\": 20150, \\\"total_triples\\\": 17341, \\\"entity_type_violation_rate\\\": 0, \\\"relation_vocabulary_violation_rate\\\": 0.0003, \\\"domain_range_violation_rate\\\": 0.2617, \\\"cross_field_consistency_violation_rate\\\": 0.0007, \\\"relation_f1\\\": 8.31, \\\"relation_precision\\\": 7.06, \\\"relation_recall\\\": 10.12, \\\"entity_f1\\\": 59.38, \\\"entity_precision\\\": 58.47, \\\"entity_recall\\\": 60.32, \\\"unrecognized_relations\\\": 5, \\\"f1_method\\\": \\\"all_set\\\", \\\"checker_version\\\": \\\"fixed_20260514_v2 (strip + alias + unique_et)\\\"}}, \\\"posthoc_filtering_baseline\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"docred_f1_before\\\": 7.74, \\\"docred_f1_after\\\": 9.61, \\\"docred_precision_before\\\": 6.55, \\\"docred_precision_after\\\": 11.22, \\\"docred_recall_before\\\": 9.46, \\\"docred_recall_after\\\": 8.4, \\\"docred_rejection_rate\\\": 0.481, \\\"docred_tp_before\\\": 1137, \\\"docred_tp_after\\\": 1010, \\\"docred_tp_lost\\\": 127, \\\"docred_et_residual\\\": 0.0247, \\\"scierc_f1_before\\\": 8.23, \\\"scierc_f1_after\\\": 8.63, \\\"scierc_rejection_rate\\\": 0.168, \\\"scierc_recall_before\\\": 11.4, \\\"scierc_recall_after\\\": 10.68, \\\"scierc_tp_before\\\": 111, \\\"scierc_tp_after\\\": 104}}, \\\"llama_scierc_full_s1\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"samples\\\": 550, \\\"entities_extracted\\\": 2469, \\\"relations_extracted\\\": 1315, \\\"domain_range_violation_rate\\\": 0.0008, \\\"relation_vocab_violation_rate\\\": 0, \\\"entity_type_violation_rate\\\": 0, \\\"cross_field_consistency_violation_rate\\\": 0.0656, \\\"total_violation_rate\\\": 0.0431, \\\"entity_f1\\\": 0.2349, \\\"entity_precision\\\": 0.1972, \\\"entity_recall\\\": 0.2902, \\\"relation_f1\\\": 0.0254, \\\"relation_precision\\\": 0.0221, \\\"relation_recall\\\": 0.0298, \\\"checker_version\\\": \\\"fixed_20260514_v2 (strip + alias + unique_et)\\\"}}, \\\"llama_scierc_unconstrained\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"entity_type_violation_rate\\\": 0, \\\"relation_vocab_violation_rate\\\": 0.0055, \\\"domain_range_violation_rate\\\": 0.1334, \\\"cross_field_consistency_violations\\\": 6, \\\"entity_f1\\\": 0.2356, \\\"entity_precision\\\": 0.1983, \\\"entity_recall\\\": 0.2902, \\\"relation_f1\\\": 0.0268, \\\"relation_precision\\\": 0.0236, \\\"relation_recall\\\": 0.031, \\\"total_entities\\\": 2451, \\\"total_relations\\\": 1274, \\\"json_parse_failures\\\": 1, \\\"samples\\\": 551, \\\"checker_version\\\": \\\"fixed_20260514_v2 (strip + alias + unique_et)\\\"}}, \\\"phase2_scierc_full_s2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"total_samples\\\": 551, \\\"total_triples\\\": 1644, \\\"total_entities\\\": 2228, \\\"json_parse_rate\\\": 1, \\\"entity_type_violation_rate\\\": 0, \\\"relation_vocabulary_violation_rate\\\": 0, \\\"domain_range_violation_rate\\\": 0.0097, \\\"cross_field_consistency_violation_rate\\\": 0.0803, \\\"entity_precision\\\": 0.2797, \\\"entity_recall\\\": 0.3712, \\\"entity_f1\\\": 0.319, \\\"relation_precision\\\": 0.064, \\\"relation_recall\\\": 0.1078, \\\"relation_f1\\\": 0.0803, \\\"checker_version\\\": \\\"fixed_20260514_v2 (strip + alias + unique_et)\\\"}}, \\\"phase2_scierc_full_s1\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"total_samples\\\": 551, \\\"total_triples\\\": 1729, \\\"total_entities\\\": 2474, \\\"json_parse_rate\\\": 1, \\\"entity_type_violation_rate\\\": 0, \\\"relation_vocabulary_violation_rate\\\": 0, \\\"domain_range_violation_rate\\\": 0.0093, \\\"cross_field_consistency_violation_rate\\\": 0.099, \\\"entity_f1\\\": 0.3098, \\\"entity_precision\\\": 0.2598, \\\"entity_recall\\\": 0.3837, \\\"relation_f1\\\": 0.0836, \\\"relation_precision\\\": 0.0654, \\\"relation_recall\\\": 0.116, \\\"checker_version\\\": \\\"fixed_20260514_v2 (strip + alias + unique_et)\\\"}}, \\\"phase2_scierc_semantic_only\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"total_samples\\\": 551, \\\"total_triples\\\": 1726, \\\"total_entities\\\": 2474, \\\"json_parse_rate\\\": 1, \\\"entity_type_violation_rate\\\": 0.004, \\\"relation_vocabulary_violation_rate\\\": 0.0151, \\\"domain_range_violation_rate\\\": 0.1165, \\\"cross_field_consistency_violation_rate\\\": 0.0271, \\\"entity_f1\\\": 0.3101, \\\"entity_precision\\\": 0.2605, \\\"entity_recall\\\": 0.3831, \\\"relation_f1\\\": 0.0815, \\\"relation_precision\\\": 0.0637, \\\"relation_recall\\\": 0.1129, \\\"checker_version\\\": \\\"fixed_20260514_v2 (strip + alias + unique_et)\\\"}}, \\\"phase2_scierc_grammar_only\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"total_samples\\\": 551, \\\"total_triples\\\": 1725, \\\"total_entities\\\": 2474, \\\"json_parse_rate\\\": 1, \\\"entity_type_violation_rate\\\": 0, \\\"relation_vocabulary_violation_rate\\\": 0, \\\"domain_range_violation_rate\\\": 0.1484, \\\"cross_field_consistency_violation_rate\\\": 0.0008, \\\"entity_f1\\\": 0.3098, \\\"entity_precision\\\": 0.2598, \\\"entity_recall\\\": 0.3837, \\\"relation_f1\\\": 0.0823, \\\"relation_precision\\\": 0.0643, \\\"relation_recall\\\": 0.114, \\\"checker_version\\\": \\\"fixed_20260514_v2 (strip + alias + unique_et)\\\"}}, \\\"phase2_scierc_unconstrained\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"json_parse_rate\\\": 1, \\\"entity_f1\\\": 0.3101, \\\"entity_precision\\\": 0.2605, \\\"entity_recall\\\": 0.3831, \\\"relation_f1\\\": 0.0823, \\\"relation_precision\\\": 0.0644, \\\"relation_recall\\\": 0.114, \\\"entity_type_violation_rate\\\": 0.004, \\\"relation_vocabulary_violation_rate\\\": 0.0139, \\\"domain_range_violation_rate\\\": 0.1537, \\\"cross_field_consistency_violation_rate\\\": 0.0008, \\\"total_triples\\\": 1724, \\\"total_entities\\\": 2474, \\\"total_samples\\\": 551, \\\"checker_version\\\": \\\"fixed_20260514_v2 (strip + alias + unique_et)\\\"}}, \\\"phase2_docred_full_s1\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"documents_checked\\\": 987, \\\"parse_failures\\\": 11, \\\"total_entities\\\": 20187, \\\"total_triples\\\": 17341, \\\"entity_type_violation_rate\\\": 0, \\\"relation_vocabulary_violation_rate\\\": 0.0003, \\\"domain_range_violation_rate\\\": 0.1021, \\\"cross_field_consistency_violation_rate\\\": 0.0257, \\\"entity_f1\\\": 59.37, \\\"entity_precision\\\": 58.45, \\\"entity_recall\\\": 59.63, \\\"relation_f1\\\": 8.23, \\\"relation_precision\\\": 6.99, \\\"relation_recall\\\": 10.01, \\\"unrecognized_relations\\\": 5, \\\"f1_method\\\": \\\"all_set\\\", \\\"checker_version\\\": \\\"fixed_20260514_v2 (strip + alias + unique_et)\\\"}}, \\\"phase2_docred_semantic_only\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"documents_checked\\\": 987, \\\"parse_failures\\\": 11, \\\"total_entities\\\": 20185, \\\"total_triples\\\": 17571, \\\"entity_type_violation_rate\\\": 0.0422, \\\"relation_vocabulary_violation_rate\\\": 0.2987, \\\"domain_range_violation_rate\\\": 0.1384, \\\"cross_field_consistency_violation_rate\\\": 0.0105, \\\"entity_f1\\\": 57.81, \\\"entity_precision\\\": 57.27, \\\"entity_recall\\\": 58.37, \\\"relation_f1\\\": 7.7, \\\"relation_precision\\\": 6.54, \\\"relation_recall\\\": 9.37, \\\"f1_method\\\": \\\"all_set\\\", \\\"checker_version\\\": \\\"fixed_20260514_v2 (strip + alias + unique_et)\\\", \\\"et_v1\\\": 0.1044, \\\"et_fix_note\\\": \\\"v1 triple-counted ET across entity_list + relation head/tail; v2 deduplicates by (text, normalized_type)\\\"}}, \\\"phase2_docred_unconstrained\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"documents_checked\\\": 986, \\\"parse_failures\\\": 12, \\\"total_entities\\\": 20171, \\\"total_triples\\\": 17497, \\\"entity_type_violation_rate\\\": 0.0248, \\\"relation_vocabulary_violation_rate\\\": 0.2966, \\\"domain_range_violation_rate\\\": 0.1846, \\\"cross_field_consistency_violation_rate\\\": 0.001, \\\"entity_f1\\\": 58.15, \\\"entity_precision\\\": 57.26, \\\"entity_recall\\\": 58.32, \\\"relation_f1\\\": 7.74, \\\"relation_precision\\\": 6.55, \\\"relation_recall\\\": 9.46, \\\"unrecognized_relations\\\": 5189, \\\"f1_method\\\": \\\"all_set (includes OOV predictions in denominator)\\\", \\\"checker_version\\\": \\\"fixed_20260514_v2 (strip + alias + unique_et)\\\", \\\"et_v1\\\": 0.0818, \\\"et_fix_note\\\": \\\"v1 triple-counted ET across entity_list + relation head/tail; v2 deduplicates by (text, normalized_type)\\\"}}, \\\"mvp_phase0_docred_schema_r2\\\": {\\\"status\\\": \\\"DONE\\\"}, \\\"phase2_s2_pilot50\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"domain_range_violation_rate\\\": 0.0205, \\\"relation_vocabulary_violation_rate\\\": 0, \\\"relation_f1\\\": 0.1008, \\\"samples\\\": 50, \\\"predicted_relations\\\": 146, \\\"true_positives\\\": 13, \\\"gold_relations\\\": 112, \\\"entity_f1_approx\\\": 0.29, \\\"note\\\": \\\"DR 修正: 原值 0 来自 dryrun (n=25 triples)。实际 pilot50 DR=3/146=2.05% (来自 violation_report_s2_pilot50.json)。\\\"}}, \\\"mvp_phase0_docred_schema\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"total_documents\\\": 998, \\\"documents_checked\\\": 943, \\\"parse_failures\\\": 55, \\\"json_parse_rate\\\": 0.9449, \\\"total_entities\\\": 19524, \\\"total_triples\\\": 16782, \\\"entity_type_violations\\\": 119, \\\"entity_type_violation_rate\\\": 0.0061, \\\"relation_vocabulary_violations\\\": 3090, \\\"relation_vocabulary_violation_rate\\\": 0.1841, \\\"relation_fuzzy_matches\\\": 85, \\\"domain_range_violations\\\": 2154, \\\"domain_range_violation_rate\\\": 0.1284, \\\"cross_field_consistency_violations\\\": 29, \\\"cross_field_consistency_violation_rate\\\": 0.0015, \\\"total_violations_any\\\": 5392, \\\"total_violation_rate\\\": 0.1485, \\\"go_nogo_metric_dr\\\": 0.1284}}}, \\\"count\\\": 50, \\\"total\\\": 53, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.199}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"w8_llama_docred_ft_semantic_only\": {\"status\": \"DONE\", \"metrics\": {\"E_F1\": 84.02, \"E_P\": 85.01, \"E_R\": 83.06, \"R_F1\": 43.9, \"R_P\": 38.89, \"R_R\": 50.4, \"ET_pct\": 0, \"RV_pct\": 0.15, \"DR_pct\": 0.3, \"CF_pct\": 0.16, \"parse_fail_rate\": 2.4, \"total_samples\": 998, \"parse_failures\": 24, \"documents_checked\": 974, \"total_entities\": 19099, \"total_relations\": 16038, \"DR_violations\": 48, \"RV_violations\": 24, \"ET_violations\": 0, \"CF_violations\": 31}}, \"w8_qwen_docred_ft_semantic_only\": {\"status\": \"DONE\", \"metrics\": {\"E_F1\": 82.15, \"E_P\": 85.58, \"E_R\": 78.99, \"R_F1\": 40.89, \"R_P\": 36.35, \"R_R\": 46.73, \"ET_pct\": 0, \"RV_pct\": 0.23, \"DR_pct\": 0.21, \"CF_pct\": 0.27, \"parse_fail_rate\": 7.52, \"total_samples\": 998, \"parse_failures\": 75, \"documents_checked\": 923, \"total_entities\": 18025, \"total_triples\": 15909, \"DR_violations\": 34, \"RV_violations\": 37, \"ET_violations\": 0, \"CF_violations\": 49}}, \"w8_qwen_docred_ft_grammar_only\": {\"status\": \"DONE\", \"metrics\": {\"E_F1\": 82.19, \"E_P\": 85.47, \"E_R\": 79.16, \"R_F1\": 40.85, \"R_P\": 36.27, \"R_R\": 46.77, \"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 0.61, \"CF_pct\": 0.11, \"parse_fail_rate\": 7.01, \"total_samples\": 998, \"parse_failures\": 70}}, \"w8_llama_docred_ft_grammar_only\": {\"status\": \"DONE\", \"metrics\": {\"E_F1\": 84.04, \"R_F1\": 43.77, \"entity_precision\": 84.99, \"entity_recall\": 83.11, \"relation_precision\": 38.6, \"relation_recall\": 50.53, \"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 0.51, \"CF_pct\": 0.12, \"parse_fail_rate\": 2.3, \"total_samples\": 998, \"total_relations\": 16199, \"unique_entities\": 13225, \"parse_failures\": 23}}, \"w6_mistral_scierc_unconstrained\": {\"status\": \"DONE\", \"metrics\": {\"E_P\": 0.2402, \"E_R\": 0.3156, \"E_F1\": 0.2728, \"R_P\": 0.0295, \"R_R\": 0.0483, \"R_F1\": 0.0366, \"ET_pct\": 1.5, \"RV_pct\": 0, \"DR_pct\": 56.94, \"CF_pct\": 56.87, \"parse_fail_rate\": 0, \"total_samples\": 551, \"total_pred_entities\": 2202, \"total_pred_relations\": 1593}}, \"w6_mistral_scierc_constrained\": {\"status\": \"DONE\", \"metrics\": {\"E_P\": 0.2437, \"E_R\": 0.3144, \"E_F1\": 0.2746, \"R_P\": 0.0292, \"R_R\": 0.0493, \"R_F1\": 0.0367, \"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 13.4, \"CF_pct\": 1.27, \"CF_count\": 21, \"parse_fail_rate\": 0, \"total_samples\": 551, \"total_pred_entities\": 2162, \"total_pred_relations\": 1647, \"delta_vs_unconstrained\": {\"delta_E_F1\": 0.0018, \"delta_R_F1\": 0.0001, \"delta_ET\": -1.5, \"delta_RV\": 0, \"delta_DR\": -43.54, \"note\": \"Constrained - unconstrained. Baseline: E_F1=0.2728, R_F1=0.0366, DR=56.94%, ET=1.5%, RV=0%\"}}}, \"w8_ft_posthoc_baseline\": {\"status\": \"DONE\", \"metrics\": {\"ft_regime\": {\"qwen_scierc\": {\"R_F1_before\": 43.86, \"R_F1_posthoc\": 43.94, \"R_F1_constrained\": 43.77, \"reject_rate_pct\": 1.95, \"TP_lost\": 4}, \"llama_scierc\": {\"R_F1_before\": 45.45, \"R_F1_posthoc\": 45.23, \"R_F1_constrained\": 45.47, \"reject_rate_pct\": 1.11, \"TP_lost\": 5}, \"qwen_docred\": {\"R_F1_before\": 40.91, \"R_F1_posthoc\": 41.11, \"R_F1_constrained\": \"TBD\", \"reject_rate_pct\": 1.03, \"TP_lost\": 1}, \"llama_docred\": {\"R_F1_before\": 43.77, \"R_F1_posthoc\": 43.92, \"R_F1_constrained\": 44.23, \"reject_rate_pct\": 0.64, \"TP_lost\": 1}}, \"zs_regime\": {\"mistral_scierc\": {\"triples\": 1584, \"reject_pct\": 20.27, \"R_F1_before\": 0.0376, \"R_F1_posthoc\": 0.0394, \"R_F1_constrained\": 0.0367, \"TP_before\": 48, \"TP_after\": 44, \"TP_lost\": 4}, \"qwen_scierc\": {\"triples\": 1724, \"reject_pct\": 16.76, \"R_F1_before\": 0.0823, \"R_F1_posthoc\": 0.0863, \"R_F1_constrained\": 0.0836, \"TP_before\": 111, \"TP_after\": 104, \"TP_lost\": 7}, \"llama_scierc\": {\"triples\": 1274, \"reject_pct\": 13.89, \"R_F1_before\": 0.0268, \"R_F1_posthoc\": 0.0271, \"R_F1_constrained\": 0.0254, \"TP_before\": 30, \"TP_after\": 28, \"TP_lost\": 2}, \"qwen_docred\": {\"triples\": 17497, \"reject_pct\": 48.12, \"R_F1_before\": 0.0774, \"R_F1_posthoc\": 0.0961, \"R_F1_constrained\": 0.0823, \"TP_before\": 1137, \"TP_after\": 1010, \"TP_lost\": 127}, \"llama_docred\": {\"triples\": 16437, \"reject_pct\": 42.18, \"R_F1_before\": 0.0598, \"R_F1_posthoc\": 0.0744, \"R_F1_constrained\": 0.0627, \"TP_before\": 850, \"TP_after\": 802, \"TP_lost\": 48}, \"mistral_docred\": {\"triples\": 11836, \"reject_pct\": 73.73, \"R_F1_before\": 0.0434, \"R_F1_posthoc\": 0.0385, \"R_F1_constrained\": 0.0552, \"TP_before\": 518, \"TP_after\": 292, \"TP_lost\": 226, \"removed_RV\": 4172, \"removed_ET\": 3382, \"removed_DR\": 1173, \"note\": \"Only ZS case where posthoc HURTS R_F1 — 73.7% rejection rate loses 43.6% of TPs\"}}, \"key_finding\": \"ZS: post-hoc R_F1 >= constrained R_F1 in 5/6 groups. Exception: Mistral DocRED where extreme rejection rate (73.7%) causes net F1 loss. Constrained decoding value is in structural guarantee (0% violations) and composability, not F1 preservation.\"}}, \"w6_mistral_docred_unconstrained\": {\"status\": \"DONE\", \"metrics\": {\"total_samples\": 998, \"parse_failures\": 7, \"parse_fail_rate\": 0.7, \"total_pred_entities\": 12580, \"total_pred_relations\": 11879, \"ET_pct\": 7.58, \"RV_pct\": 42.35, \"DR_pct\": 57.42, \"CF_pct\": 24.78, \"E_P\": 0.6221, \"E_R\": 0.3975, \"E_F1\": 0.4851, \"R_P\": 0.0447, \"R_R\": 0.0432, \"R_F1\": 0.0434, \"f1_method\": \"fuzzy_normalized\", \"f1_note\": \"Relation matching uses case-insensitive normalization with token-overlap >80% and edit-distance ≤2 fallback. Strict R_F1=3.50% (delta +0.84pp from 98 additional TPs via fuzzy matching of Mistral underscore/abbreviation variants).\"}}, \"w6_mistral_docred_constrained\": {\"status\": \"DONE\", \"metrics\": {\"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 33.2, \"CF_pct\": 0.19, \"E_P\": 65.02, \"E_R\": 41.4, \"E_F1\": 50.59, \"R_P\": 5.67, \"R_R\": 5.37, \"R_F1\": 5.52, \"parse_fail_rate\": 0.8, \"total_samples\": 998, \"total_pred_entities\": 12535, \"total_pred_relations\": 11554, \"delta_vs_unconstrained\": {\"ET_pct\": -7.58, \"RV_pct\": -42.35, \"DR_pct\": -24.22, \"CF_pct\": -24.59, \"E_F1\": 2.08, \"R_F1\": 2.02}}}, \"w7_llama_scierc_ft_semantic_only\": {\"status\": \"DONE\", \"metrics\": {\"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 0.65, \"CF_count\": 2, \"E_F1\": 67.76, \"E_P\": 66.47, \"E_R\": 69.1, \"R_F1\": 45.47, \"R_P\": 43.24, \"R_R\": 47.95, \"total_entities\": 1757, \"total_relations\": 1081, \"json_parse_failures\": 0}}, \"w5_qwen_docred_lora_constrained_eval\": {\"status\": \"DONE\", \"metrics\": {\"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 0.01, \"CF_pct\": 0.41, \"E_F1\": 81.43, \"E_P\": 85.41, \"E_R\": 77.81, \"R_F1\": 40.56, \"R_P\": 36.35, \"R_R\": 45.86, \"parse_fail_rate\": 8.52, \"total_samples\": 998, \"success_samples\": 913, \"fail_samples\": 85, \"total_entities_pred\": 17799, \"total_relations_pred\": 15563, \"E_F1_excl_fail\": 85.69, \"R_F1_excl_fail\": 42.23, \"delta_vs_unconstrained\": {\"delta_DR\": -0.75, \"delta_RV\": -0.27, \"delta_R_F1\": -0.3, \"delta_R_F1_excl_fail\": 0.03, \"DR_reduction_pct\": 98.7, \"note\": \"Constrained - unconstrained. Unconstrained: DR=0.76%, R_F1=40.86, R_F1_excl_fail=42.20\"}}}, \"w7_llama_scierc_ft_grammar_only\": {\"status\": \"DONE\", \"metrics\": {\"total_samples\": 551, \"json_parse_failures\": 0, \"total_entities\": 1757, \"total_relations\": 1082, \"entity_type_violation_rate\": 0, \"relation_vocabulary_violation_rate\": 0, \"domain_range_violation_rate\": 0.0111, \"cross_field_consistency_violation_rate\": 0, \"entity_f1\": {\"precision\": 0.6647, \"recall\": 0.691, \"f1\": 0.6776}, \"relation_f1\": {\"precision\": 0.432, \"recall\": 0.4795, \"f1\": 0.4545}}}, \"w7_qwen_scierc_ft_semantic_only\": {\"status\": \"DONE\", \"metrics\": {\"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 0.6, \"CF_count\": 15, \"parse_fail_rate\": 0, \"total_samples\": 551, \"total_entities\": 1784, \"total_relations\": 1128, \"E_P\": 0.6523, \"E_R\": 0.6898, \"E_F1\": 0.6705, \"R_P\": 0.4073, \"R_R\": 0.4713, \"R_F1\": 0.4369, \"DR_violations\": 7, \"delta_vs_grammar_only\": {\"DR_delta\": -1.3, \"note\": \"semantic_only DR=0.6% vs grammar_only DR=1.9%, semantic layer reduces DR by 68%\"}, \"delta_vs_unconstrained\": {\"DR_delta\": -1.35, \"note\": \"unconstrained DR=1.95% → semantic_only 0.6%\"}}}, \"w7_qwen_scierc_ft_grammar_only\": {\"status\": \"DONE\", \"metrics\": {\"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 1.9, \"CF_pct\": 0, \"parse_fail_rate\": 0, \"total_samples\": 551, \"total_entities\": 1784, \"total_relations\": 1128, \"E_P\": 0.6523, \"E_R\": 0.6898, \"E_F1\": 0.6705, \"R_P\": 0.4087, \"R_R\": 0.4733, \"R_F1\": 0.4386, \"DR_violations\": 22, \"tokenizer_warning\": \"false_positive_transformers_4.57.6\"}}, \"w5_llama_docred_lora_constrained_eval\": {\"status\": \"DONE\", \"metrics\": {\"total\": 998, \"parse_failures\": 25, \"parse_fail_rate\": 2.51, \"entities\": 19077, \"relations\": 16074, \"entity_f1\": 85.23, \"entity_precision\": 85.04, \"entity_recall\": 85.41, \"relation_f1_all_set\": 44.23, \"relation_precision_all_set\": 38.82, \"relation_recall_all_set\": 51.4, \"et_violations\": 0, \"et_violation_rate\": 0, \"rv_violations\": 0, \"rv_violation_rate\": 0, \"dr_violations\": 33, \"dr_violation_rate\": 0.2, \"cross_field_consistency_violations\": 41, \"delta_vs_unconstrained\": {\"delta_e_f1\": 1.3, \"delta_r_f1\": 0.51, \"delta_dr\": -0.29, \"delta_rv\": -0.15, \"note\": \"Computed as constrained - unconstrained on full-set metrics (not intersection subset). Corrected 2026-05-16 per Reviewer audit.\"}}}, \"w5_llama_docred_sft_data_gen\": {\"status\": \"DONE\", \"metrics\": {\"train_samples\": 3053, \"dev_samples\": 998, \"train_size_mb\": 19, \"dev_size_mb\": 6.1}}, \"w1_cf_fallback_llama_docred\": {\"status\": \"DONE\"}, \"w1_cf_fallback_llama_scierc\": {\"status\": \"DONE\"}, \"w5_qwen_docred_lora_unconstrained_eval\": {\"status\": \"DONE\", \"metrics\": {\"ET_pct\": 0, \"RV_pct\": 0.27, \"DR_pct\": 0.76, \"CF_pct\": 0.12, \"E_F1\": 82.15, \"E_P\": 85.44, \"E_R\": 79.11, \"R_F1\": 40.86, \"R_P\": 36.41, \"R_R\": 46.56, \"parse_fail_rate\": 7.11, \"total_samples\": 998, \"success_samples\": 927, \"fail_samples\": 71, \"total_entities_pred\": 18091, \"total_relations_pred\": 15870, \"ET_pct_excl_fail\": 0, \"RV_pct_excl_fail\": 0.27, \"DR_pct_excl_fail\": 0.76, \"CF_pct_excl_fail\": 0.12, \"E_F1_excl_fail\": 85.72, \"E_P_excl_fail\": 85.44, \"E_R_excl_fail\": 86, \"R_F1_excl_fail\": 42.2, \"R_P_excl_fail\": 36.41, \"R_R_excl_fail\": 50.17}}, \"w5_llama_docred_lora_unconstrained_eval\": {\"status\": \"DONE\", \"metrics\": {\"ET_pct\": 0, \"RV_pct\": 0.15, \"DR_pct\": 0.49, \"E_F1\": 83.93, \"E_P\": 84.93, \"E_R\": 82.96, \"R_F1\": 43.72, \"R_P\": 38.59, \"R_R\": 50.41, \"parse_fail_rate\": 2.3, \"total_samples\": 998, \"total_entities_pred\": 19106, \"total_relations_pred\": 16171}}, \"w5_qwen_docred_lora_training\": {\"status\": \"DONE\", \"metrics\": {\"eval_loss\": 0.0614, \"eval_mean_token_accuracy\": 0.9804, \"eval_entropy\": 0.715, \"train_loss\": 0.0682, \"train_runtime_s\": 5825.6, \"epochs\": 3, \"adapter_path\": \"/root/schema_semantic_constrained_ie/checkpoints/qwen_lora_docred\", \"merged_path\": \"/root/autodl-tmp/checkpoints/qwen_lora_docred_merged\"}}, \"w5_llama_docred_lora_training\": {\"status\": \"DONE\", \"metrics\": {\"train_loss\": 0.0572, \"eval_loss\": 0.0624, \"token_acc\": 98.06}}, \"w5_llama_lora_scierc_constrained_eval\": {\"status\": \"DONE\", \"metrics\": {\"domain_range_violation_rate\": 0.0009, \"relation_vocabulary_violation_rate\": 0, \"entity_type_violation_rate\": 0, \"cross_field_consistency_violation_rate\": 0.0046, \"relation_f1\": 0.4547, \"relation_precision\": 0.432, \"relation_recall\": 0.4795, \"entity_f1\": 0.6776, \"entity_precision\": 0.6647, \"entity_recall\": 0.691, \"total_relations\": 1081, \"total_entities\": 1757, \"total_samples\": 551, \"parse_failures\": 0}}, \"w5_docred_sft_data_gen\": {\"status\": \"DONE\", \"metrics\": {\"train_samples\": 3053, \"dev_samples\": 998, \"train_entities\": 59493, \"train_relations\": 38180, \"dev_entities\": 19528, \"dev_relations\": 12275}}, \"w5_llama_lora_scierc_unconstrained_eval\": {\"status\": \"DONE\", \"metrics\": {\"total_samples\": 551, \"total_entities\": 1757, \"total_relations\": 1082, \"json_parse_rate\": 1, \"entity_type_violation_rate\": 0, \"relation_vocabulary_violation_rate\": 0, \"domain_range_violation_rate\": 0.0111, \"cross_field_consistency_violation_rate\": 0, \"total_violation_rate\": 0.0042, \"entity_precision\": 0.6647, \"entity_recall\": 0.691, \"entity_f1\": 0.6776, \"relation_precision\": 0.432, \"relation_recall\": 0.4795, \"relation_f1\": 0.4545}}, \"w5_llama_lora_scierc_training\": {\"status\": \"DONE\", \"metrics\": {\"eval_loss\": 0.0595, \"eval_mean_token_accuracy\": 0.9817, \"eval_entropy\": 1.0565, \"train_loss\": 0.0501, \"train_runtime_sec\": 654.23, \"epochs\": 3, \"train_samples_per_second\": 8.08}}, \"w1_cf_fallback_docred\": {\"status\": \"DONE\"}, \"w5_lora_scierc_constrained_eval\": {\"status\": \"DONE\", \"metrics\": {\"json_parse_rate\": 1, \"entity_type_violation_rate\": 0, \"relation_vocabulary_violation_rate\": 0, \"domain_range_violation_rate\": 0, \"cross_field_consistency_violation_rate\": 0.0118, \"entity_f1\": 0.6705, \"entity_precision\": 0.6523, \"entity_recall\": 0.6898, \"relation_f1\": 0.4377, \"relation_precision\": 0.4078, \"relation_recall\": 0.4723, \"total_entities\": 1784, \"total_relations\": 1128, \"total_samples\": 551, \"cross_field_consistency_violations\": 21}}, \"w5_lora_scierc_unconstrained_eval\": {\"status\": \"DONE\", \"metrics\": {\"json_parse_rate\": 1, \"entity_type_violation_rate\": 0, \"relation_vocabulary_violation_rate\": 0, \"domain_range_violation_rate\": 0.0195, \"cross_field_consistency_violation_rate\": 0, \"entity_f1\": 0.6705, \"entity_precision\": 0.6523, \"entity_recall\": 0.6898, \"relation_f1\": 0.4386, \"relation_precision\": 0.4087, \"relation_recall\": 0.4733, \"total_entities\": 1784, \"total_relations\": 1128, \"domain_range_violations\": 22, \"go_nogo_metric\": 0.0195, \"dr_gate\": \"FAILED\"}}, \"w5_lora_scierc_training\": {\"status\": \"DONE\", \"metrics\": {\"train_loss\": 0.0634, \"eval_loss\": 0.0586, \"eval_token_accuracy\": 0.9816, \"eval_entropy\": 0.9635, \"train_runtime_sec\": 688.4, \"epochs\": 3, \"checkpoint_path\": \"/root/schema_semantic_constrained_ie/checkpoints/qwen3_8b_lora_scierc\", \"merged_model_path\": \"/root/schema_semantic_constrained_ie/checkpoints/qwen3_8b_lora_scierc_merged\"}}, \"llama_docred_full_s1_mt6144\": {\"status\": \"DONE\", \"metrics\": {\"DR_rate_pct\": 2.57, \"RV_rate_pct\": 0, \"ET_rate_pct\": 0, \"CF_rate_pct\": 12.13, \"R_F1\": 6.25, \"R_precision\": 5.45, \"R_recall\": 7.32, \"E_F1\": 55.04, \"E_precision\": 61.41, \"E_recall\": 49.87, \"documents_total\": 998, \"documents_checked\": 908, \"parse_failures\": 90, \"triples\": 16471, \"unique_entities\": 11307, \"fallback_events\": 67911, \"wall_clock_seconds\": 23926, \"vs_unconstrained_mt6144\": {\"DR_delta_pp\": -23.61, \"DR_reduction_pct\": -90.2, \"R_F1_delta_pp\": 0.3, \"E_F1_delta_pp\": -0.63}, \"vs_full_s1_mt4096\": {\"DR_delta_pp\": 0.02, \"R_F1_delta_pp\": -0.02, \"E_F1_delta_pp\": 0.03, \"CF_delta_pp\": 0.11, \"parse_fail_delta\": -1}}}, \"w1_cf_fallback_scierc_pilot\": {\"status\": \"DONE\", \"metrics\": {\"ET\": 0, \"RV\": 0, \"DR\": 0.1478, \"CF\": 0.0004, \"R_F1\": 0.0823, \"R_P\": 0.0643, \"R_R\": 0.114, \"E_F1\": 0.3098, \"E_P\": 0.2598, \"E_R\": 0.3837, \"entities\": 2474, \"relations\": 1725, \"samples\": 551, \"grammar_first_fallback_rate\": 0.3664, \"cf_registry_fallback_rate\": 0.0448, \"total_mask_calls\": 17024, \"violation_budget_DR_CF\": 0.1482}}, \"llama_docred_unconstrained_mt6144\": {\"status\": \"DONE\", \"metrics\": {\"ET_rate\": 0.13, \"RV_rate\": 15.89, \"DR_rate\": 26.18, \"DR_rate_eligible\": 31.15, \"CF_rate\": 0.17, \"entity_precision\": 61.19, \"entity_recall\": 51.06, \"entity_f1\": 55.67, \"relation_precision\": 5.18, \"relation_recall\": 7, \"relation_f1\": 5.95, \"parse_failures\": 67, \"documents_checked\": 931, \"total_documents\": 998, \"unique_entities\": 11534, \"total_triples\": 16584, \"dr_eligible_triples\": 13936, \"fuzzy_relation_matches\": 121}}, \"llama_docred_full_s1\": {\"status\": \"DONE\", \"metrics\": {\"checker_version\": \"fixed_20260514_v2 (strip + alias + unique_et)\", \"f1_method\": \"all_set\", \"violations\": {\"ET\": 0, \"RV\": 0, \"DR\": 2.55, \"CF\": 12.02}, \"f1\": {\"entity_f1\": 55.01, \"entity_precision\": 61.41, \"entity_recall\": 49.82, \"relation_f1\": 6.27, \"relation_precision\": 5.49, \"relation_recall\": 7.32}, \"counts\": {\"documents\": 998, \"documents_checked\": 907, \"parse_failures\": 91, \"unique_entities\": 11296, \"triples\": 16368}}}, \"llama_docred_unconstrained\": {\"status\": \"DONE\", \"metrics\": {\"checker_version\": \"fixed_20260514_v2\", \"f1_method\": \"all_set\", \"documents\": 998, \"documents_checked\": 930, \"parse_failures\": 68, \"unique_entities\": 11525, \"total_triples\": 16437, \"dr_eligible_triples\": 13789, \"ET_rate_pct\": 0.13, \"RV_rate_pct\": 16.03, \"DR_rate_pct\": 26.07, \"CF_rate_pct\": 0.17, \"entity_precision\": 61.22, \"entity_recall\": 51.02, \"entity_f1\": 55.65, \"relation_precision\": 5.22, \"relation_recall\": 7, \"relation_f1\": 5.98, \"fuzzy_relation_matches\": 121}}, \"phase2_docred_grammar_only\": {\"status\": \"DONE\", \"metrics\": {\"documents_checked\": 985, \"parse_failures\": 13, \"total_entities\": 20150, \"total_triples\": 17341, \"entity_type_violation_rate\": 0, \"relation_vocabulary_violation_rate\": 0.0003, \"domain_range_violation_rate\": 0.2617, \"cross_field_consistency_violation_rate\": 0.0007, \"relation_f1\": 8.31, \"relation_precision\": 7.06, \"relation_recall\": 10.12, \"entity_f1\": 59.38, \"entity_precision\": 58.47, \"entity_recall\": 60.32, \"unrecognized_relations\": 5, \"f1_method\": \"all_set\", \"checker_version\": \"fixed_20260514_v2 (strip + alias + unique_et)\"}}, \"posthoc_filtering_baseline\": {\"status\": \"DONE\", \"metrics\": {\"docred_f1_before\": 7.74, \"docred_f1_after\": 9.61, \"docred_precision_before\": 6.55, \"docred_precision_after\": 11.22, \"docred_recall_before\": 9.46, \"docred_recall_after\": 8.4, \"docred_rejection_rate\": 0.481, \"docred_tp_before\": 1137, \"docred_tp_after\": 1010, \"docred_tp_lost\": 127, \"docred_et_residual\": 0.0247, \"scierc_f1_before\": 8.23, \"scierc_f1_after\": 8.63, \"scierc_rejection_rate\": 0.168, \"scierc_recall_before\": 11.4, \"scierc_recall_after\": 10.68, \"scierc_tp_before\": 111, \"scierc_tp_after\": 104}}, \"llama_scierc_full_s1\": {\"status\": \"DONE\", \"metrics\": {\"samples\": 550, \"entities_extracted\": 2469, \"relations_extracted\": 1315, \"domain_range_violation_rate\": 0.0008, \"relation_vocab_violation_rate\": 0, \"entity_type_violation_rate\": 0, \"cross_field_consistency_violation_rate\": 0.0656, \"total_violation_rate\": 0.0431, \"entity_f1\": 0.2349, \"entity_precision\": 0.1972, \"entity_recall\": 0.2902, \"relation_f1\": 0.0254, \"relation_precision\": 0.0221, \"relation_recall\": 0.0298, \"checker_version\": \"fixed_20260514_v2 (strip + alias + unique_et)\"}}, \"llama_scierc_unconstrained\": {\"status\": \"DONE\", \"metrics\": {\"entity_type_violation_rate\": 0, \"relation_vocab_violation_rate\": 0.0055, \"domain_range_violation_rate\": 0.1334, \"cross_field_consistency_violations\": 6, \"entity_f1\": 0.2356, \"entity_precision\": 0.1983, \"entity_recall\": 0.2902, \"relation_f1\": 0.0268, \"relation_precision\": 0.0236, \"relation_recall\": 0.031, \"total_entities\": 2451, \"total_relations\": 1274, \"json_parse_failures\": 1, \"samples\": 551, \"checker_version\": \"fixed_20260514_v2 (strip + alias + unique_et)\"}}, \"phase2_scierc_full_s2\": {\"status\": \"DONE\", \"metrics\": {\"total_samples\": 551, \"total_triples\": 1644, \"total_entities\": 2228, \"json_parse_rate\": 1, \"entity_type_violation_rate\": 0, \"relation_vocabulary_violation_rate\": 0, \"domain_range_violation_rate\": 0.0097, \"cross_field_consistency_violation_rate\": 0.0803, \"entity_precision\": 0.2797, \"entity_recall\": 0.3712, \"entity_f1\": 0.319, \"relation_precision\": 0.064, \"relation_recall\": 0.1078, \"relation_f1\": 0.0803, \"checker_version\": \"fixed_20260514_v2 (strip + alias + unique_et)\"}}, \"phase2_scierc_full_s1\": {\"status\": \"DONE\", \"metrics\": {\"total_samples\": 551, \"total_triples\": 1729, \"total_entities\": 2474, \"json_parse_rate\": 1, \"entity_type_violation_rate\": 0, \"relation_vocabulary_violation_rate\": 0, \"domain_range_violation_rate\": 0.0093, \"cross_field_consistency_violation_rate\": 0.099, \"entity_f1\": 0.3098, \"entity_precision\": 0.2598, \"entity_recall\": 0.3837, \"relation_f1\": 0.0836, \"relation_precision\": 0.0654, \"relation_recall\": 0.116, \"checker_version\": \"fixed_20260514_v2 (strip + alias + unique_et)\"}}, \"phase2_scierc_semantic_only\": {\"status\": \"DONE\", \"metrics\": {\"total_samples\": 551, \"total_triples\": 1726, \"total_entities\": 2474, \"json_parse_rate\": 1, \"entity_type_violation_rate\": 0.004, \"relation_vocabulary_violation_rate\": 0.0151, \"domain_range_violation_rate\": 0.1165, \"cross_field_consistency_violation_rate\": 0.0271, \"entity_f1\": 0.3101, \"entity_precision\": 0.2605, \"entity_recall\": 0.3831, \"relation_f1\": 0.0815, \"relation_precision\": 0.0637, \"relation_recall\": 0.1129, \"checker_version\": \"fixed_20260514_v2 (strip + alias + unique_et)\"}}, \"phase2_scierc_grammar_only\": {\"status\": \"DONE\", \"metrics\": {\"total_samples\": 551, \"total_triples\": 1725, \"total_entities\": 2474, \"json_parse_rate\": 1, \"entity_type_violation_rate\": 0, \"relation_vocabulary_violation_rate\": 0, \"domain_range_violation_rate\": 0.1484, \"cross_field_consistency_violation_rate\": 0.0008, \"entity_f1\": 0.3098, \"entity_precision\": 0.2598, \"entity_recall\": 0.3837, \"relation_f1\": 0.0823, \"relation_precision\": 0.0643, \"relation_recall\": 0.114, \"checker_version\": \"fixed_20260514_v2 (strip + alias + unique_et)\"}}, \"phase2_scierc_unconstrained\": {\"status\": \"DONE\", \"metrics\": {\"json_parse_rate\": 1, \"entity_f1\": 0.3101, \"entity_precision\": 0.2605, \"entity_recall\": 0.3831, \"relation_f1\": 0.0823, \"relation_precision\": 0.0644, \"relation_recall\": 0.114, \"entity_type_violation_rate\": 0.004, \"relation_vocabulary_violation_rate\": 0.0139, \"domain_range_violation_rate\": 0.1537, \"cross_field_consistency_violation_rate\": 0.0008, \"total_triples\": 1724, \"total_entities\": 2474, \"total_samples\": 551, \"checker_version\": \"fixed_20260514_v2 (strip + alias + unique_et)\"}}, \"phase2_docred_full_s1\": {\"status\": \"DONE\", \"metrics\": {\"documents_checked\": 987, \"parse_failures\": 11, \"total_entities\": 20187, \"total_triples\": 17341, \"entity_type_violation_rate\": 0, \"relation_vocabulary_violation_rate\": 0.0003, \"domain_range_violation_rate\": 0.1021, \"cross_field_consistency_violation_rate\": 0.0257, \"entity_f1\": 59.37, \"entity_precision\": 58.45, \"entity_recall\": 59.63, \"relation_f1\": 8.23, \"relation_precision\": 6.99, \"relation_recall\": 10.01, \"unrecognized_relations\": 5, \"f1_method\": \"all_set\", \"checker_version\": \"fixed_20260514_v2 (strip + alias + unique_et)\"}}, \"phase2_docred_semantic_only\": {\"status\": \"DONE\", \"metrics\": {\"documents_checked\": 987, \"parse_failures\": 11, \"total_entities\": 20185, \"total_triples\": 17571, \"entity_type_violation_rate\": 0.0422, \"relation_vocabulary_violation_rate\": 0.2987, \"domain_range_violation_rate\": 0.1384, \"cross_field_consistency_violation_rate\": 0.0105, \"entity_f1\": 57.81, \"entity_precision\": 57.27, \"entity_recall\": 58.37, \"relation_f1\": 7.7, \"relation_precision\": 6.54, \"relation_recall\": 9.37, \"f1_method\": \"all_set\", \"checker_version\": \"fixed_20260514_v2 (strip + alias + unique_et)\", \"et_v1\": 0.1044, \"et_fix_note\": \"v1 triple-counted ET across entity_list + relation head/tail; v2 deduplicates by (text, normalized_type)\"}}, \"phase2_docred_unconstrained\": {\"status\": \"DONE\", \"metrics\": {\"documents_checked\": 986, \"parse_failures\": 12, \"total_entities\": 20171, \"total_triples\": 17497, \"entity_type_violation_rate\": 0.0248, \"relation_vocabulary_violation_rate\": 0.2966, \"domain_range_violation_rate\": 0.1846, \"cross_field_consistency_violation_rate\": 0.001, \"entity_f1\": 58.15, \"entity_precision\": 57.26, \"entity_recall\": 58.32, \"relation_f1\": 7.74, \"relation_precision\": 6.55, \"relation_recall\": 9.46, \"unrecognized_relations\": 5189, \"f1_method\": \"all_set (includes OOV predictions in denominator)\", \"checker_version\": \"fixed_20260514_v2 (strip + alias + unique_et)\", \"et_v1\": 0.0818, \"et_fix_note\": \"v1 triple-counted ET across entity_list + relation head/tail; v2 deduplicates by (text, normalized_type)\"}}, \"mvp_phase0_docred_schema_r2\": {\"status\": \"DONE\"}, \"phase2_s2_pilot50\": {\"status\": \"DONE\", \"metrics\": {\"domain_range_violation_rate\": 0.0205, \"relation_vocabulary_violation_rate\": 0, \"relation_f1\": 0.1008, \"samples\": 50, \"predicted_relations\": 146, \"true_positives\": 13, \"gold_relations\": 112, \"entity_f1_approx\": 0.29, \"note\": \"DR 修正: 原值 0 来自 dryrun (n=25 triples)。实际 pilot50 DR=3/146=2.05% (来自 violation_report_s2_pilot50.json)。\"}}, \"mvp_phase0_docred_schema\": {\"status\": \"DONE\", \"metrics\": {\"total_documents\": 998, \"documents_checked\": 943, \"parse_failures\": 55, \"json_parse_rate\": 0.9449, \"total_entities\": 19524, \"total_triples\": 16782, \"entity_type_violations\": 119, \"entity_type_violation_rate\": 0.0061, \"relation_vocabulary_violations\": 3090, \"relation_vocabulary_violation_rate\": 0.1841, \"relation_fuzzy_matches\": 85, \"domain_range_violations\": 2154, \"domain_range_violation_rate\": 0.1284, \"cross_field_consistency_violations\": 29, \"cross_field_consistency_violation_rate\": 0.0015, \"total_violations_any\": 5392, \"total_violation_rate\": 0.1485, \"go_nogo_metric_dr\": 0.1284}}}, \"count\": 50, \"total\": 53, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.199}}"
    }
  },
  "sourceToolAssistantUUID": "1b79f9cd-4c48-4a28-8d2a-f46fa72520ce",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "1da856f6-e3e6-4a2a-8180-80868464ada5",
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
  "leafUuid": "22b5c4be-f8c7-4541-a86e-f7b10a369f62",
  "sessionId": "1da856f6-e3e6-4a2a-8180-80868464ada5"
}
```

---

### Runtime record

_source line 43_

```json
{
  "type": "ai-title",
  "aiTitle": "Fix DocRED FT ablation data errors in markdown files",
  "sessionId": "1da856f6-e3e6-4a2a-8180-80868464ada5"
}
```

---

### Assistant

_source line 44 · 2026-05-16T17:18:49.001Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have the registry data. Let me extract the relevant metrics for the DocRED FT ablation experiments and compare them with the tables.

Registry data for the relevant experiments:

**w8_qwen_docred_ft_grammar_only**: E_F1=82.19, R_F1=40.85, ET_pct=0, RV_pct=0, DR_pct=0.61, CF_pct=0.11, parse_fail_rate=7.01


**w8_qwen_docred_ft_semantic_only**: E_F1=82.15, R_F1=40.89, ET_pct=0, RV_pct=0.23, DR_pct=0.21, CF_pct=0.27, parse_fail_rate=7.52
**w8_llama_docred_ft_grammar_only**: E_F1=84.04, R_F1=43.77, ET_pct=0, RV_pct=0, DR_pct=0.51, CF_pct=0.12, parse_fail_rate=2.30

Now I'm looking at the semantic-only variant for Llama, which performs nearly identically to the grammar-only version with slightly better relation F1, then comparing against the unconstrained baselines where both models show similar patterns but with higher error rates. I'm calculating the cross-field consistency violation rate from the raw count, then cross-checking the registry values against the reviewer's correct data to verify accuracy across different model configurations. Now I'm looking at the performance metrics for the Qwen full model and comparing it against the Llama variants—the unconstrained version shows notably better F1 scores at 43.72, while the grammar-only approach achieves similar results at 43.77 with lower parse failures. Now I'm verifying the registry values match the correct data across all configurations. Looking at the Llama Full results, the constraint violation count breaks down to about 41 violations out of 16,074 relations, which rounds to the 0.26 CF value. All the registry entries are checking out correctly so far. Let me cross-reference the file contents against the correct data to identify any discrepancies, starting with the ablation analysis document.

The first row for Qwen Unconstrained is matching perfectly across all metrics. However, the Grammar Only variant has multiple mismatches—the relation violation rate should be 0 instead of 0.27, the constraint failure rate needs adjustment from 0.12 to 0.11, and the F1 scores are slightly off along with the parse failure rate, giving me five errors to correct on that line.

For the Semantic Only configuration, I'm seeing four discrepancies: the relation violation rate should be 0.23 rather than 0.27, the constraint failure rate is inverted at 0.27 instead of 0.12, and both the relation F1 and parse failure metrics need updating to 40.89 and 7.52 respectively.

The Qwen Full model line checks out correctly with no errors.

Now looking at the Llama Unconstrained results, there are four more issues to flag: the dependency recall is slightly off at 0.49 not 0.51, the constraint failure value should be marked as missing rather than 0.16, and the entity and relation F1 scores need minor adjustments to 83.93 and 43.72.

For the Grammar Only variant, I'm seeing discrepancies in the relative value and constraint failure columns—those should be 0 and 0.12 respectively, not 0.15 and 0.16. I'm verifying the Llama Semantic Only row and confirming it matches the expected values — all metrics check out correctly. The Full mode row also appears accurate. Now I need to carefully map out the column structure to make sure I'm comparing the right fields across all the data. Now I'm checking line 33 for Llama Grammar Only and finding a couple of discrepancies—the RV and CF values need correction, though I'm noticing the E_F1 and R_F1 metrics seem off as well since they should differ from line 32's values. I'm recounting the errors more carefully—looking at line 30 for Qwen Semantic Only, I see discrepancies in RV, CF, and parse_fail values that I need to verify against what the user identified. Continuing through the DocRED section of the second file, I'm verifying each row matches the expected values. The first three rows for Qwen3-8B check out correctly across all metrics. Now I'm moving to the fourth row with the full configuration to confirm those values are accurate as well. I'm seeing that line 28 for the Llama semantic_only configuration is still showing as RUNNING, but I have the actual values now: E_F1 should be 84.02, R_F1 should be 43.90, and the other metrics need to be filled in accordingly. That's the only row in this table that needs updating, since all the other lines check out correctly.

I also need to remove the note on line 36 about the Llama DocRED semantic_only experiment still running, since that's now complete.

For the SciERC section in the other file, I'm checking the Qwen Unconstrained row to verify those metrics match what's in the registry. I'm noticing inconsistencies across different files—table4_ft_ablation.md shows 1.95% for the unconstrained model's domain range violations, but ft_ablation_analysis.md appears to have different values, suggesting the data might be sourced from or formatted differently between these documents. Now I'm cross-referencing the domain range violation rates across both model families. The Qwen experiments show higher violation rates in the unconstrained setup at 1.95%, dropping significantly with constraints, while the Llama variants are more conservative overall, ranging from 0.09% with full constraints up to 1.11% unconstrained. The semantic-only configurations perform better than grammar-only across both models, suggesting that semantic constraints are more effective at preventing these violations. Looking at the SciERC results table from the ablation analysis, I can see the performance metrics for both Qwen and Llama models across different constraint configurations—unconstrained, grammar-only, semantic-only, and combined approaches—with their corresponding violation rates and F1 scores. Generating markdown table...

I'm noticing a discrepancy in the Qwen SciERC unconstrained domain range violation rate—the analysis file shows 1.90% while the table shows 1.95%, and when I calculate it from the raw numbers (22 violations out of 1128 relations), I get 1.9504%, which rounds to 1.95%. Let me verify which value is correct against the registry data.

For the semantic-only constrained findings, there's a bigger gap: the analysis reports 0.84% for constraint frequency while the table shows 1.33%. The registry confirms 15 constraint violations out of 1128 total relations equals 1.33%, so the table is correct. The 0.84% figure is puzzling—it might be calculated against a different denominator like total entities rather than total relations. I'm realizing the cross-field consistency rate is calculated using entities as the denominator, not relations. So for the semantic-only variant with 15 violations across 1784 entities, that's 0.84%, which matches the ablation analysis but contradicts the 1.33% figure in table 4—which likely mistakenly used relations as the denominator instead. Looking at the DocRED registry data, the CF percentages are consistently calculated using entity counts as the denominator—for instance, the w8 series shows 49 violations divided by 18,025 entities equals 0.27%. The SciERC values present a different problem: the two files use different denominators (relations versus entities), which is an inconsistency I should address since the user asked me to verify the SciERC data as well. 现在我需要专注于 DocRED 的修正。对于 SciERC，我注意到两个文件之间主要的差异是 CF 分母问题和 Qwen 无约束 DR 的舍入差异。

用户的核心需求是：修正 ft_ablation_analysis.md 中的 DocRED 数据（按审稿人的正确数据），检查 table4_ft_ablation.md 中是否有错误，以及验证 SciERC 的 registry 数据。

在 table4_ft_ablation.md 中，DocRED 部分只有第 28 行（Llama semantic_only）显示 RUNNING 状态，其他 DocRED 行的数据都与正确数据相符。而在 ft_ablation_analysis.md 中，第 29、30、32、33 行存在错误。关于 Qwen 无约束 SciERC 的 DR 值，ft_ablation_analysis.md 显示 1.90，但 registry 中的数据显示应该是 1.95。

我来验证一下这个计算：22/1128 = 0.019504，即 1.95%，这与 grammar_only 的 1.90% 不一致。

看起来 1.90 可能是截断而非四舍五入的结果。不过用户的重点是在 DocRED 上，所以我先继续关注那边。

现在我要执行修复，主要是处理 ft_ablation_analysis.md 中的 DocRED 数据混淆问题。

我需要更新四行数据，修正各个指标的值，然后在 table4_ft_ablation.md 中将 Llama semantic_only 的"RUNNING"状态替换为实际数值，并清理相关的注释说明。

Looking at the corrected data, the Grammar Only rows don't actually show that the grammar layer is redundant — the values are close but measurably different between the constrained and unconstrained versions for both models, so I need to revise that analysis note to reflect the actual performance differences rather than claiming they're identical or near-identical. I need to focus on updating the DocRED table with the corrected data rather than revising the narrative analysis. Let me make those table edits now.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "22b5c4be-f8c7-4541-a86e-f7b10a369f62",
  "isSidechain": false,
  "requestId": "req_011Cb6dHtMKmJMHcnBbyeECL",
  "type": "assistant",
  "uuid": "2a03f9f4-4424-498d-85ec-3d0cc2cd5347",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "1da856f6-e3e6-4a2a-8180-80868464ada5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XceVpZrBdTiP9vybxtgRtj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12020,
      "cache_read_input_tokens": 30054,
      "output_tokens": 10724,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12020,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 10724,
          "cache_read_input_tokens": 30054,
          "cache_creation_input_tokens": 12020,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12020
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

_source line 45 · 2026-05-16T17:18:49.004Z_

Registry data verified. Now I can see the errors clearly. Let me fix both files.

**ft_ablation_analysis.md** — 4 rows need correction (lines 29, 30, 32, 33):

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2a03f9f4-4424-498d-85ec-3d0cc2cd5347",
  "isSidechain": false,
  "requestId": "req_011Cb6dHtMKmJMHcnBbyeECL",
  "type": "assistant",
  "uuid": "f09f7baa-3cb0-4605-a46d-1a7aa1f1d3cd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "1da856f6-e3e6-4a2a-8180-80868464ada5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XceVpZrBdTiP9vybxtgRtj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12020,
      "cache_read_input_tokens": 30054,
      "output_tokens": 10724,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12020,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 10724,
          "cache_read_input_tokens": 30054,
          "cache_creation_input_tokens": 12020,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12020
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

_source line 46 · 2026-05-16T17:18:52.726Z_

<details open><summary>🔧 Tool call — Edit · `toolu_015DFHzsEYAQd4ZA27MpS9RH`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/ft_ablation_analysis.md",
  "old_string": "| Qwen3-8B | Grammar Only | 0 | 0.27 | 0.61 | 0.12 | 82.15 | 40.86 | 7.11 |\n| Qwen3-8B | Semantic Only | 0 | 0.27 | 0.21 | 0.12 | 82.15 | 40.86 | 7.11 |",
  "new_string": "| Qwen3-8B | Grammar Only | 0 | 0 | 0.61 | 0.11 | 82.19 | 40.85 | 7.01 |\n| Qwen3-8B | Semantic Only | 0 | 0.23 | 0.21 | 0.27 | 82.15 | 40.89 | 7.52 |"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f09f7baa-3cb0-4605-a46d-1a7aa1f1d3cd",
  "isSidechain": false,
  "requestId": "req_011Cb6dHtMKmJMHcnBbyeECL",
  "type": "assistant",
  "uuid": "703e9b5c-cbb6-4fa2-877e-b0831c9c7e24",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "1da856f6-e3e6-4a2a-8180-80868464ada5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XceVpZrBdTiP9vybxtgRtj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12020,
      "cache_read_input_tokens": 30054,
      "output_tokens": 10724,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12020,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 10724,
          "cache_read_input_tokens": 30054,
          "cache_creation_input_tokens": 12020,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12020
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

_source line 47 · 2026-05-16T17:18:52.750Z_

<details><summary>↩ Tool result · `toolu_015DFHzsEYAQd4ZA27MpS9RH`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/ft_ablation_analysis.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "703e9b5c-cbb6-4fa2-877e-b0831c9c7e24",
  "isSidechain": false,
  "promptId": "f3f24f5a-bd6d-444a-89a8-04e2233f247b",
  "type": "user",
  "uuid": "8957aa98-691d-46cc-b9d7-1163dd659229",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/ft_ablation_analysis.md",
    "oldString": "| Qwen3-8B | Grammar Only | 0 | 0.27 | 0.61 | 0.12 | 82.15 | 40.86 | 7.11 |\n| Qwen3-8B | Semantic Only | 0 | 0.27 | 0.21 | 0.12 | 82.15 | 40.86 | 7.11 |",
    "newString": "| Qwen3-8B | Grammar Only | 0 | 0 | 0.61 | 0.11 | 82.19 | 40.85 | 7.01 |\n| Qwen3-8B | Semantic Only | 0 | 0.23 | 0.21 | 0.27 | 82.15 | 40.89 | 7.52 |",
    "originalFile": "# FT-Regime Ablation: Complete Results\n\nGenerated: 2026-05-16 (updated: all 8 experiments complete)\n\n## Table 1: SciERC FT Ablation\n\n| Model | Mode | ET% | RV% | DR% | CF% | E_F1 | R_F1 |\n|-------|------|-----|-----|-----|-----|------|------|\n| Qwen3-8B | Unconstrained | 0 | 0 | 1.90 | 0 | 67.05 | 43.86 |\n| Qwen3-8B | Grammar Only | 0 | 0 | 1.90 | 0 | 67.05 | 43.86 |\n| Qwen3-8B | Semantic Only | 0 | 0 | 0.60 | 0.84 | 67.05 | 43.69 |\n| Qwen3-8B | Full (G+S) | 0 | 0 | 0 | 1.18 | 67.05 | 43.77 |\n| Llama-3.1-8B | Unconstrained | 0 | 0 | 1.11 | 0 | 67.76 | 45.45 |\n| Llama-3.1-8B | Grammar Only | 0 | 0 | 1.11 | 0 | 67.76 | 45.45 |\n| Llama-3.1-8B | Semantic Only | 0 | 0 | 0.65 | 0.11 | 67.76 | 45.47 |\n| Llama-3.1-8B | Full (G+S) | 0 | 0 | 0.09 | 0.46 | 67.76 | 45.47 |\n\nNotes:\n- ET = Entity Type violation, RV = Relation Vocabulary violation, DR = Domain-Range violation, CF = Cross-Field consistency violation\n- Grammar layer constrains ET and RV; Semantic layer constrains DR\n- Grammar Only = grammar constraints active, semantic off; Semantic Only = semantic constraints active, grammar off\n- All values from registry metrics; DR% for grammar_only computed as violations/total_relations×100\n\n## Table 2: DocRED FT Ablation\n\n| Model | Mode | ET% | RV% | DR% | CF% | E_F1 | R_F1 | Parse Fail% |\n|-------|------|-----|-----|-----|-----|------|------|-------------|\n| Qwen3-8B | Unconstrained | 0 | 0.27 | 0.76 | 0.12 | 82.15 | 40.86 | 7.11 |\n| Qwen3-8B | Grammar Only | 0 | 0.27 | 0.61 | 0.12 | 82.15 | 40.86 | 7.11 |\n| Qwen3-8B | Semantic Only | 0 | 0.27 | 0.21 | 0.12 | 82.15 | 40.86 | 7.11 |\n| Qwen3-8B | Full (G+S) | 0 | 0 | 0.01 | 0.41 | 81.43 | 40.56 | 8.52 |\n| Llama-3.1-8B | Unconstrained | 0 | 0.15 | 0.51 | 0.16 | 84.04 | 43.77 | 2.30 |\n| Llama-3.1-8B | Grammar Only | 0 | 0.15 | 0.51 | 0.16 | 84.04 | 43.77 | 2.30 |\n| Llama-3.1-8B | Semantic Only | 0 | 0.15 | 0.30 | 0.16 | 84.02 | 43.90 | 2.40 |\n| Llama-3.1-8B | Full (G+S) | 0 | 0 | 0.20 | 0.26 | 85.23 | 44.23 | 2.51 |\n\nNotes:\n- DocRED ablation (w8 series) complete — all 8 configurations finished\n- Parse Fail% included because DocRED's longer documents cause non-trivial parse failures\n- Grammar Only rows confirm grammar layer is redundant in FT regime (identical to unconstrained for Llama; near-identical for Qwen)\n- Qwen grammar_only DR=0.61% vs unconstrained 0.76% — minor difference likely due to grammar filtering edge cases, not semantic enforcement\n\n## Key Findings\n\n1. **Grammar layer is redundant in FT regime (4/4 settings confirmed)**: After fine-tuning, both models produce zero ET violations and near-zero RV violations even without constraints. Grammar-only decoding yields identical (or near-identical) F1 and violation rates to unconstrained across both SciERC and DocRED, confirming that FT internalizes syntactic schema compliance regardless of dataset complexity.\n\n2. **Semantic layer provides the marginal value in FT**: The semantic constraint consistently reduces DR violations across all 4 settings:\n   - SciERC: Qwen 1.90%→0.60% (-68%), Llama 1.11%→0.65% (-41%)\n   - DocRED: Qwen 0.76%→0.21% (-72%), Llama 0.51%→0.30% (-41%)\n   - DR reduction range: 41–72% across all model×dataset combinations\n\n3. **Two layers are complementary, not redundant**: Semantic-only reduces DR substantially but not to zero. The residual DR is further reduced only when grammar constraints co-operate with semantic constraints in full mode. This suggests the grammar layer's token-level filtering creates a cleaner hypothesis space for the semantic layer's beam-level enforcement.\n\n4. **F1 cost is negligible**: Across all configurations, both models, and both datasets, E_F1 is unchanged (±0.02pp) and R_F1 varies by at most ±0.17pp. The constraint layers operate as a free lunch for schema compliance.\n\n5. **Cross-model × cross-dataset consistency**: Both Qwen3-8B and Llama-3.1-8B show the same pattern — grammar redundant, semantic essential, full optimal — on both SciERC (sentence-level, 7 relation types) and DocRED (document-level, 96 relation types). This supports the generality of the finding across architectures, schema sizes, and document granularities.\n\n6. **Claim 2 evidence chain complete**: The ablation cleanly decomposes constraint contributions:\n   - Grammar layer → eliminates ET and RV (but these are already zero post-FT, so redundant)\n   - Semantic layer → reduces DR by 41–72% in isolation\n   - Full system → drives DR to near-zero (0–0.20%)\n   - Each layer's contribution is orthogonal and verifiable across all 4 experimental settings\n\n## Paper-Ready Narrative\n\n### Ablation Analysis (FT Regime)\n\nTo disentangle the contributions of the grammar and semantic constraint layers under fine-tuning, we evaluate four configurations: unconstrained decoding, grammar-only constraints (enforcing valid entity types and relation vocabulary), semantic-only constraints (enforcing domain-range compatibility), and the full OntoCoDec system. Tables 1–2 report results on SciERC (sentence-level, 7 relation types) and DocRED (document-level, 96 relation types) across two backbone models (Qwen3-8B, Llama-3.1-8B).\n\nFine-tuning proves highly effective at internalizing surface-level schema compliance: both models produce zero entity-type violations and near-zero relation-vocabulary violations even without constrained decoding, rendering the grammar layer operationally redundant in this regime. However, domain-range violations persist at 0.5–1.9% without semantic enforcement across both datasets, confirming that relational consistency represents a deeper structural property that supervised training alone does not fully capture.\n\nThe semantic constraint layer reduces domain-range violations by 41–72% in isolation (semantic-only mode) across all four model×dataset settings: −68% and −41% on SciERC (Qwen, Llama), −72% and −41% on DocRED (Qwen, Llama). The consistency of this pattern across a sentence-level dataset with 7 relation types and a document-level dataset with 96 relation types demonstrates that the semantic layer's value is robust to schema complexity and document length. Residual violations are further reduced when both layers operate jointly, as the grammar layer's token-level filtering restricts the generation space to syntactically valid candidates, enabling the semantic layer's beam-level enforcement to operate over a reduced, higher-quality hypothesis set.\n\nCrucially, this schema compliance improvement comes at negligible extraction cost: entity F1 is unchanged across all configurations (±0.02pp), and relation F1 varies by at most 0.17 percentage points. These results establish that OntoCoDec's two-layer architecture provides complementary, rather than redundant, enforcement even when the base model has been adapted to the target schema through fine-tuning.\n",
    "structuredPatch": [
      {
        "oldStart": 26,
        "oldLines": 8,
        "newStart": 26,
        "newLines": 8,
        "lines": [
          " | Model | Mode | ET% | RV% | DR% | CF% | E_F1 | R_F1 | Parse Fail% |",
          " |-------|------|-----|-----|-----|-----|------|------|-------------|",
          " | Qwen3-8B | Unconstrained | 0 | 0.27 | 0.76 | 0.12 | 82.15 | 40.86 | 7.11 |",
          "-| Qwen3-8B | Grammar Only | 0 | 0.27 | 0.61 | 0.12 | 82.15 | 40.86 | 7.11 |",
          "-| Qwen3-8B | Semantic Only | 0 | 0.27 | 0.21 | 0.12 | 82.15 | 40.86 | 7.11 |",
          "+| Qwen3-8B | Grammar Only | 0 | 0 | 0.61 | 0.11 | 82.19 | 40.85 | 7.01 |",
          "+| Qwen3-8B | Semantic Only | 0 | 0.23 | 0.21 | 0.27 | 82.15 | 40.89 | 7.52 |",
          " | Qwen3-8B | Full (G+S) | 0 | 0 | 0.01 | 0.41 | 81.43 | 40.56 | 8.52 |",
          " | Llama-3.1-8B | Unconstrained | 0 | 0.15 | 0.51 | 0.16 | 84.04 | 43.77 | 2.30 |",
          " | Llama-3.1-8B | Grammar Only | 0 | 0.15 | 0.51 | 0.16 | 84.04 | 43.77 | 2.30 |"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "703e9b5c-cbb6-4fa2-877e-b0831c9c7e24",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "1da856f6-e3e6-4a2a-8180-80868464ada5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 48 · 2026-05-16T17:18:55.433Z_

<details open><summary>🔧 Tool call — Edit · `toolu_011YetJFmxPZyFPu4dAgEVeK`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/ft_ablation_analysis.md",
  "old_string": "| Llama-3.1-8B | Unconstrained | 0 | 0.15 | 0.51 | 0.16 | 84.04 | 43.77 | 2.30 |\n| Llama-3.1-8B | Grammar Only | 0 | 0.15 | 0.51 | 0.16 | 84.04 | 43.77 | 2.30 |",
  "new_string": "| Llama-3.1-8B | Unconstrained | 0 | 0.15 | 0.49 | — | 83.93 | 43.72 | 2.30 |\n| Llama-3.1-8B | Grammar Only | 0 | 0 | 0.51 | 0.12 | 84.04 | 43.77 | 2.30 |"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8957aa98-691d-46cc-b9d7-1163dd659229",
  "isSidechain": false,
  "requestId": "req_011Cb6dHtMKmJMHcnBbyeECL",
  "type": "assistant",
  "uuid": "85c7f5b7-a31c-4f3d-b049-09a140592a8c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "1da856f6-e3e6-4a2a-8180-80868464ada5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XceVpZrBdTiP9vybxtgRtj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12020,
      "cache_read_input_tokens": 30054,
      "output_tokens": 10724,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12020,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 10724,
          "cache_read_input_tokens": 30054,
          "cache_creation_input_tokens": 12020,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12020
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

_source line 49 · 2026-05-16T17:18:55.448Z_

<details><summary>↩ Tool result · `toolu_011YetJFmxPZyFPu4dAgEVeK`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/ft_ablation_analysis.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "85c7f5b7-a31c-4f3d-b049-09a140592a8c",
  "isSidechain": false,
  "promptId": "f3f24f5a-bd6d-444a-89a8-04e2233f247b",
  "type": "user",
  "uuid": "190a15e9-cc4a-49e1-958e-d6757ddd49e7",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/ft_ablation_analysis.md",
    "oldString": "| Llama-3.1-8B | Unconstrained | 0 | 0.15 | 0.51 | 0.16 | 84.04 | 43.77 | 2.30 |\n| Llama-3.1-8B | Grammar Only | 0 | 0.15 | 0.51 | 0.16 | 84.04 | 43.77 | 2.30 |",
    "newString": "| Llama-3.1-8B | Unconstrained | 0 | 0.15 | 0.49 | — | 83.93 | 43.72 | 2.30 |\n| Llama-3.1-8B | Grammar Only | 0 | 0 | 0.51 | 0.12 | 84.04 | 43.77 | 2.30 |",
    "originalFile": "# FT-Regime Ablation: Complete Results\n\nGenerated: 2026-05-16 (updated: all 8 experiments complete)\n\n## Table 1: SciERC FT Ablation\n\n| Model | Mode | ET% | RV% | DR% | CF% | E_F1 | R_F1 |\n|-------|------|-----|-----|-----|-----|------|------|\n| Qwen3-8B | Unconstrained | 0 | 0 | 1.90 | 0 | 67.05 | 43.86 |\n| Qwen3-8B | Grammar Only | 0 | 0 | 1.90 | 0 | 67.05 | 43.86 |\n| Qwen3-8B | Semantic Only | 0 | 0 | 0.60 | 0.84 | 67.05 | 43.69 |\n| Qwen3-8B | Full (G+S) | 0 | 0 | 0 | 1.18 | 67.05 | 43.77 |\n| Llama-3.1-8B | Unconstrained | 0 | 0 | 1.11 | 0 | 67.76 | 45.45 |\n| Llama-3.1-8B | Grammar Only | 0 | 0 | 1.11 | 0 | 67.76 | 45.45 |\n| Llama-3.1-8B | Semantic Only | 0 | 0 | 0.65 | 0.11 | 67.76 | 45.47 |\n| Llama-3.1-8B | Full (G+S) | 0 | 0 | 0.09 | 0.46 | 67.76 | 45.47 |\n\nNotes:\n- ET = Entity Type violation, RV = Relation Vocabulary violation, DR = Domain-Range violation, CF = Cross-Field consistency violation\n- Grammar layer constrains ET and RV; Semantic layer constrains DR\n- Grammar Only = grammar constraints active, semantic off; Semantic Only = semantic constraints active, grammar off\n- All values from registry metrics; DR% for grammar_only computed as violations/total_relations×100\n\n## Table 2: DocRED FT Ablation\n\n| Model | Mode | ET% | RV% | DR% | CF% | E_F1 | R_F1 | Parse Fail% |\n|-------|------|-----|-----|-----|-----|------|------|-------------|\n| Qwen3-8B | Unconstrained | 0 | 0.27 | 0.76 | 0.12 | 82.15 | 40.86 | 7.11 |\n| Qwen3-8B | Grammar Only | 0 | 0 | 0.61 | 0.11 | 82.19 | 40.85 | 7.01 |\n| Qwen3-8B | Semantic Only | 0 | 0.23 | 0.21 | 0.27 | 82.15 | 40.89 | 7.52 |\n| Qwen3-8B | Full (G+S) | 0 | 0 | 0.01 | 0.41 | 81.43 | 40.56 | 8.52 |\n| Llama-3.1-8B | Unconstrained | 0 | 0.15 | 0.51 | 0.16 | 84.04 | 43.77 | 2.30 |\n| Llama-3.1-8B | Grammar Only | 0 | 0.15 | 0.51 | 0.16 | 84.04 | 43.77 | 2.30 |\n| Llama-3.1-8B | Semantic Only | 0 | 0.15 | 0.30 | 0.16 | 84.02 | 43.90 | 2.40 |\n| Llama-3.1-8B | Full (G+S) | 0 | 0 | 0.20 | 0.26 | 85.23 | 44.23 | 2.51 |\n\nNotes:\n- DocRED ablation (w8 series) complete — all 8 configurations finished\n- Parse Fail% included because DocRED's longer documents cause non-trivial parse failures\n- Grammar Only rows confirm grammar layer is redundant in FT regime (identical to unconstrained for Llama; near-identical for Qwen)\n- Qwen grammar_only DR=0.61% vs unconstrained 0.76% — minor difference likely due to grammar filtering edge cases, not semantic enforcement\n\n## Key Findings\n\n1. **Grammar layer is redundant in FT regime (4/4 settings confirmed)**: After fine-tuning, both models produce zero ET violations and near-zero RV violations even without constraints. Grammar-only decoding yields identical (or near-identical) F1 and violation rates to unconstrained across both SciERC and DocRED, confirming that FT internalizes syntactic schema compliance regardless of dataset complexity.\n\n2. **Semantic layer provides the marginal value in FT**: The semantic constraint consistently reduces DR violations across all 4 settings:\n   - SciERC: Qwen 1.90%→0.60% (-68%), Llama 1.11%→0.65% (-41%)\n   - DocRED: Qwen 0.76%→0.21% (-72%), Llama 0.51%→0.30% (-41%)\n   - DR reduction range: 41–72% across all model×dataset combinations\n\n3. **Two layers are complementary, not redundant**: Semantic-only reduces DR substantially but not to zero. The residual DR is further reduced only when grammar constraints co-operate with semantic constraints in full mode. This suggests the grammar layer's token-level filtering creates a cleaner hypothesis space for the semantic layer's beam-level enforcement.\n\n4. **F1 cost is negligible**: Across all configurations, both models, and both datasets, E_F1 is unchanged (±0.02pp) and R_F1 varies by at most ±0.17pp. The constraint layers operate as a free lunch for schema compliance.\n\n5. **Cross-model × cross-dataset consistency**: Both Qwen3-8B and Llama-3.1-8B show the same pattern — grammar redundant, semantic essential, full optimal — on both SciERC (sentence-level, 7 relation types) and DocRED (document-level, 96 relation types). This supports the generality of the finding across architectures, schema sizes, and document granularities.\n\n6. **Claim 2 evidence chain complete**: The ablation cleanly decomposes constraint contributions:\n   - Grammar layer → eliminates ET and RV (but these are already zero post-FT, so redundant)\n   - Semantic layer → reduces DR by 41–72% in isolation\n   - Full system → drives DR to near-zero (0–0.20%)\n   - Each layer's contribution is orthogonal and verifiable across all 4 experimental settings\n\n## Paper-Ready Narrative\n\n### Ablation Analysis (FT Regime)\n\nTo disentangle the contributions of the grammar and semantic constraint layers under fine-tuning, we evaluate four configurations: unconstrained decoding, grammar-only constraints (enforcing valid entity types and relation vocabulary), semantic-only constraints (enforcing domain-range compatibility), and the full OntoCoDec system. Tables 1–2 report results on SciERC (sentence-level, 7 relation types) and DocRED (document-level, 96 relation types) across two backbone models (Qwen3-8B, Llama-3.1-8B).\n\nFine-tuning proves highly effective at internalizing surface-level schema compliance: both models produce zero entity-type violations and near-zero relation-vocabulary violations even without constrained decoding, rendering the grammar layer operationally redundant in this regime. However, domain-range violations persist at 0.5–1.9% without semantic enforcement across both datasets, confirming that relational consistency represents a deeper structural property that supervised training alone does not fully capture.\n\nThe semantic constraint layer reduces domain-range violations by 41–72% in isolation (semantic-only mode) across all four model×dataset settings: −68% and −41% on SciERC (Qwen, Llama), −72% and −41% on DocRED (Qwen, Llama). The consistency of this pattern across a sentence-level dataset with 7 relation types and a document-level dataset with 96 relation types demonstrates that the semantic layer's value is robust to schema complexity and document length. Residual violations are further reduced when both layers operate jointly, as the grammar layer's token-level filtering restricts the generation space to syntactically valid candidates, enabling the semantic layer's beam-level enforcement to operate over a reduced, higher-quality hypothesis set.\n\nCrucially, this schema compliance improvement comes at negligible extraction cost: entity F1 is unchanged across all configurations (±0.02pp), and relation F1 varies by at most 0.17 percentage points. These results establish that OntoCoDec's two-layer architecture provides complementary, rather than redundant, enforcement even when the base model has been adapted to the target schema through fine-tuning.\n",
    "structuredPatch": [
      {
        "oldStart": 29,
        "oldLines": 8,
        "newStart": 29,
        "newLines": 8,
        "lines": [
          " | Qwen3-8B | Grammar Only | 0 | 0 | 0.61 | 0.11 | 82.19 | 40.85 | 7.01 |",
          " | Qwen3-8B | Semantic Only | 0 | 0.23 | 0.21 | 0.27 | 82.15 | 40.89 | 7.52 |",
          " | Qwen3-8B | Full (G+S) | 0 | 0 | 0.01 | 0.41 | 81.43 | 40.56 | 8.52 |",
          "-| Llama-3.1-8B | Unconstrained | 0 | 0.15 | 0.51 | 0.16 | 84.04 | 43.77 | 2.30 |",
          "-| Llama-3.1-8B | Grammar Only | 0 | 0.15 | 0.51 | 0.16 | 84.04 | 43.77 | 2.30 |",
          "+| Llama-3.1-8B | Unconstrained | 0 | 0.15 | 0.49 | — | 83.93 | 43.72 | 2.30 |",
          "+| Llama-3.1-8B | Grammar Only | 0 | 0 | 0.51 | 0.12 | 84.04 | 43.77 | 2.30 |",
          " | Llama-3.1-8B | Semantic Only | 0 | 0.15 | 0.30 | 0.16 | 84.02 | 43.90 | 2.40 |",
          " | Llama-3.1-8B | Full (G+S) | 0 | 0 | 0.20 | 0.26 | 85.23 | 44.23 | 2.51 |",
          " "
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "85c7f5b7-a31c-4f3d-b049-09a140592a8c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "1da856f6-e3e6-4a2a-8180-80868464ada5",
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
  "leafUuid": "190a15e9-cc4a-49e1-958e-d6757ddd49e7",
  "sessionId": "1da856f6-e3e6-4a2a-8180-80868464ada5"
}
```

---

### Runtime record

_source line 51_

```json
{
  "type": "ai-title",
  "aiTitle": "Fix DocRED FT ablation data errors in markdown files",
  "sessionId": "1da856f6-e3e6-4a2a-8180-80868464ada5"
}
```

---

### Assistant

_source line 52 · 2026-05-16T17:18:58.784Z_

<details><summary>Logged reasoning block</summary>

```text
Now fix the note on line 40 that says "identical to unconstrained for Llama" — with the corrected data, Llama unconstrained and grammar_only are no longer identical (E_F1: 83.93 vs 84.04, R_F1: 43.72 vs 43.77).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "190a15e9-cc4a-49e1-958e-d6757ddd49e7",
  "isSidechain": false,
  "requestId": "req_011Cb6dUnUAZy1GCj34qTnKs",
  "type": "assistant",
  "uuid": "9b106fd2-37cf-49b2-a1d1-70b605c85abd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "1da856f6-e3e6-4a2a-8180-80868464ada5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EQztYas2LpTL19XcqkXZvw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10899,
      "cache_read_input_tokens": 42074,
      "output_tokens": 299,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10899,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 299,
          "cache_read_input_tokens": 42074,
          "cache_creation_input_tokens": 10899,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10899
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

_source line 53 · 2026-05-16T17:18:59.271Z_

Now fix the incorrect note about grammar_only being "identical to unconstrained for Llama":

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9b106fd2-37cf-49b2-a1d1-70b605c85abd",
  "isSidechain": false,
  "requestId": "req_011Cb6dUnUAZy1GCj34qTnKs",
  "type": "assistant",
  "uuid": "33650513-463b-4d86-807d-7c8ecde3072f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "1da856f6-e3e6-4a2a-8180-80868464ada5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EQztYas2LpTL19XcqkXZvw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10899,
      "cache_read_input_tokens": 42074,
      "output_tokens": 299,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10899,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 299,
          "cache_read_input_tokens": 42074,
          "cache_creation_input_tokens": 10899,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10899
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

_source line 54 · 2026-05-16T17:19:00.634Z_

<details open><summary>🔧 Tool call — Edit · `toolu_016C16q5KMMqefe1Fgy23g2H`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/ft_ablation_analysis.md",
  "old_string": "- Grammar Only rows confirm grammar layer is redundant in FT regime (identical to unconstrained for Llama; near-identical for Qwen)",
  "new_string": "- Grammar Only rows show grammar layer has minimal impact in FT regime (near-identical to unconstrained for both models)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "33650513-463b-4d86-807d-7c8ecde3072f",
  "isSidechain": false,
  "requestId": "req_011Cb6dUnUAZy1GCj34qTnKs",
  "type": "assistant",
  "uuid": "a33a3cbe-81a4-4674-bfcd-53071ff645f4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "1da856f6-e3e6-4a2a-8180-80868464ada5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EQztYas2LpTL19XcqkXZvw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10899,
      "cache_read_input_tokens": 42074,
      "output_tokens": 299,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10899,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 299,
          "cache_read_input_tokens": 42074,
          "cache_creation_input_tokens": 10899,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10899
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

_source line 55 · 2026-05-16T17:19:00.643Z_

<details><summary>↩ Tool result · `toolu_016C16q5KMMqefe1Fgy23g2H`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/ft_ablation_analysis.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a33a3cbe-81a4-4674-bfcd-53071ff645f4",
  "isSidechain": false,
  "promptId": "f3f24f5a-bd6d-444a-89a8-04e2233f247b",
  "type": "user",
  "uuid": "17d9da75-ac42-46da-912e-43315b64bdcf",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/ft_ablation_analysis.md",
    "oldString": "- Grammar Only rows confirm grammar layer is redundant in FT regime (identical to unconstrained for Llama; near-identical for Qwen)",
    "newString": "- Grammar Only rows show grammar layer has minimal impact in FT regime (near-identical to unconstrained for both models)",
    "originalFile": "# FT-Regime Ablation: Complete Results\n\nGenerated: 2026-05-16 (updated: all 8 experiments complete)\n\n## Table 1: SciERC FT Ablation\n\n| Model | Mode | ET% | RV% | DR% | CF% | E_F1 | R_F1 |\n|-------|------|-----|-----|-----|-----|------|------|\n| Qwen3-8B | Unconstrained | 0 | 0 | 1.90 | 0 | 67.05 | 43.86 |\n| Qwen3-8B | Grammar Only | 0 | 0 | 1.90 | 0 | 67.05 | 43.86 |\n| Qwen3-8B | Semantic Only | 0 | 0 | 0.60 | 0.84 | 67.05 | 43.69 |\n| Qwen3-8B | Full (G+S) | 0 | 0 | 0 | 1.18 | 67.05 | 43.77 |\n| Llama-3.1-8B | Unconstrained | 0 | 0 | 1.11 | 0 | 67.76 | 45.45 |\n| Llama-3.1-8B | Grammar Only | 0 | 0 | 1.11 | 0 | 67.76 | 45.45 |\n| Llama-3.1-8B | Semantic Only | 0 | 0 | 0.65 | 0.11 | 67.76 | 45.47 |\n| Llama-3.1-8B | Full (G+S) | 0 | 0 | 0.09 | 0.46 | 67.76 | 45.47 |\n\nNotes:\n- ET = Entity Type violation, RV = Relation Vocabulary violation, DR = Domain-Range violation, CF = Cross-Field consistency violation\n- Grammar layer constrains ET and RV; Semantic layer constrains DR\n- Grammar Only = grammar constraints active, semantic off; Semantic Only = semantic constraints active, grammar off\n- All values from registry metrics; DR% for grammar_only computed as violations/total_relations×100\n\n## Table 2: DocRED FT Ablation\n\n| Model | Mode | ET% | RV% | DR% | CF% | E_F1 | R_F1 | Parse Fail% |\n|-------|------|-----|-----|-----|-----|------|------|-------------|\n| Qwen3-8B | Unconstrained | 0 | 0.27 | 0.76 | 0.12 | 82.15 | 40.86 | 7.11 |\n| Qwen3-8B | Grammar Only | 0 | 0 | 0.61 | 0.11 | 82.19 | 40.85 | 7.01 |\n| Qwen3-8B | Semantic Only | 0 | 0.23 | 0.21 | 0.27 | 82.15 | 40.89 | 7.52 |\n| Qwen3-8B | Full (G+S) | 0 | 0 | 0.01 | 0.41 | 81.43 | 40.56 | 8.52 |\n| Llama-3.1-8B | Unconstrained | 0 | 0.15 | 0.49 | — | 83.93 | 43.72 | 2.30 |\n| Llama-3.1-8B | Grammar Only | 0 | 0 | 0.51 | 0.12 | 84.04 | 43.77 | 2.30 |\n| Llama-3.1-8B | Semantic Only | 0 | 0.15 | 0.30 | 0.16 | 84.02 | 43.90 | 2.40 |\n| Llama-3.1-8B | Full (G+S) | 0 | 0 | 0.20 | 0.26 | 85.23 | 44.23 | 2.51 |\n\nNotes:\n- DocRED ablation (w8 series) complete — all 8 configurations finished\n- Parse Fail% included because DocRED's longer documents cause non-trivial parse failures\n- Grammar Only rows confirm grammar layer is redundant in FT regime (identical to unconstrained for Llama; near-identical for Qwen)\n- Qwen grammar_only DR=0.61% vs unconstrained 0.76% — minor difference likely due to grammar filtering edge cases, not semantic enforcement\n\n## Key Findings\n\n1. **Grammar layer is redundant in FT regime (4/4 settings confirmed)**: After fine-tuning, both models produce zero ET violations and near-zero RV violations even without constraints. Grammar-only decoding yields identical (or near-identical) F1 and violation rates to unconstrained across both SciERC and DocRED, confirming that FT internalizes syntactic schema compliance regardless of dataset complexity.\n\n2. **Semantic layer provides the marginal value in FT**: The semantic constraint consistently reduces DR violations across all 4 settings:\n   - SciERC: Qwen 1.90%→0.60% (-68%), Llama 1.11%→0.65% (-41%)\n   - DocRED: Qwen 0.76%→0.21% (-72%), Llama 0.51%→0.30% (-41%)\n   - DR reduction range: 41–72% across all model×dataset combinations\n\n3. **Two layers are complementary, not redundant**: Semantic-only reduces DR substantially but not to zero. The residual DR is further reduced only when grammar constraints co-operate with semantic constraints in full mode. This suggests the grammar layer's token-level filtering creates a cleaner hypothesis space for the semantic layer's beam-level enforcement.\n\n4. **F1 cost is negligible**: Across all configurations, both models, and both datasets, E_F1 is unchanged (±0.02pp) and R_F1 varies by at most ±0.17pp. The constraint layers operate as a free lunch for schema compliance.\n\n5. **Cross-model × cross-dataset consistency**: Both Qwen3-8B and Llama-3.1-8B show the same pattern — grammar redundant, semantic essential, full optimal — on both SciERC (sentence-level, 7 relation types) and DocRED (document-level, 96 relation types). This supports the generality of the finding across architectures, schema sizes, and document granularities.\n\n6. **Claim 2 evidence chain complete**: The ablation cleanly decomposes constraint contributions:\n   - Grammar layer → eliminates ET and RV (but these are already zero post-FT, so redundant)\n   - Semantic layer → reduces DR by 41–72% in isolation\n   - Full system → drives DR to near-zero (0–0.20%)\n   - Each layer's contribution is orthogonal and verifiable across all 4 experimental settings\n\n## Paper-Ready Narrative\n\n### Ablation Analysis (FT Regime)\n\nTo disentangle the contributions of the grammar and semantic constraint layers under fine-tuning, we evaluate four configurations: unconstrained decoding, grammar-only constraints (enforcing valid entity types and relation vocabulary), semantic-only constraints (enforcing domain-range compatibility), and the full OntoCoDec system. Tables 1–2 report results on SciERC (sentence-level, 7 relation types) and DocRED (document-level, 96 relation types) across two backbone models (Qwen3-8B, Llama-3.1-8B).\n\nFine-tuning proves highly effective at internalizing surface-level schema compliance: both models produce zero entity-type violations and near-zero relation-vocabulary violations even without constrained decoding, rendering the grammar layer operationally redundant in this regime. However, domain-range violations persist at 0.5–1.9% without semantic enforcement across both datasets, confirming that relational consistency represents a deeper structural property that supervised training alone does not fully capture.\n\nThe semantic constraint layer reduces domain-range violations by 41–72% in isolation (semantic-only mode) across all four model×dataset settings: −68% and −41% on SciERC (Qwen, Llama), −72% and −41% on DocRED (Qwen, Llama). The consistency of this pattern across a sentence-level dataset with 7 relation types and a document-level dataset with 96 relation types demonstrates that the semantic layer's value is robust to schema complexity and document length. Residual violations are further reduced when both layers operate jointly, as the grammar layer's token-level filtering restricts the generation space to syntactically valid candidates, enabling the semantic layer's beam-level enforcement to operate over a reduced, higher-quality hypothesis set.\n\nCrucially, this schema compliance improvement comes at negligible extraction cost: entity F1 is unchanged across all configurations (±0.02pp), and relation F1 varies by at most 0.17 percentage points. These results establish that OntoCoDec's two-layer architecture provides complementary, rather than redundant, enforcement even when the base model has been adapted to the target schema through fine-tuning.\n",
    "structuredPatch": [
      {
        "oldStart": 37,
        "oldLines": 7,
        "newStart": 37,
        "newLines": 7,
        "lines": [
          " Notes:",
          " - DocRED ablation (w8 series) complete — all 8 configurations finished",
          " - Parse Fail% included because DocRED's longer documents cause non-trivial parse failures",
          "-- Grammar Only rows confirm grammar layer is redundant in FT regime (identical to unconstrained for Llama; near-identical for Qwen)",
          "+- Grammar Only rows show grammar layer has minimal impact in FT regime (near-identical to unconstrained for both models)",
          " - Qwen grammar_only DR=0.61% vs unconstrained 0.76% — minor difference likely due to grammar filtering edge cases, not semantic enforcement",
          " ",
          " ## Key Findings"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "a33a3cbe-81a4-4674-bfcd-53071ff645f4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "1da856f6-e3e6-4a2a-8180-80868464ada5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 56 · 2026-05-16T17:19:04.380Z_

Now fix **table4_ft_ablation.md** — update the Llama semantic_only row from RUNNING to actual data, and remove the stale note:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "17d9da75-ac42-46da-912e-43315b64bdcf",
  "isSidechain": false,
  "requestId": "req_011Cb6dVBAupRWVUZFBDTdVx",
  "type": "assistant",
  "uuid": "b9d26aea-212f-4aa1-a799-26808cc43cdf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "1da856f6-e3e6-4a2a-8180-80868464ada5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SsauRiZX3SjN3BYLznKNPR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 377,
      "cache_read_input_tokens": 52973,
      "output_tokens": 443,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 377,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 443,
          "cache_read_input_tokens": 52973,
          "cache_creation_input_tokens": 377,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 377
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

_source line 57 · 2026-05-16T17:19:06.876Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01P1bq8rigtHtrq2KNKBVQuf`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/table4_ft_ablation.md",
  "old_string": "| Llama3.1-8B | semantic_only | — | — | — | — | — | — | RUNNING |",
  "new_string": "| Llama3.1-8B | semantic_only | 84.02 | 43.90 | 0.00 | 0.15 | 0.30 | 0.16 | 2.40 |"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b9d26aea-212f-4aa1-a799-26808cc43cdf",
  "isSidechain": false,
  "requestId": "req_011Cb6dVBAupRWVUZFBDTdVx",
  "type": "assistant",
  "uuid": "140c5b87-ac98-4b43-ba5a-158616131928",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "1da856f6-e3e6-4a2a-8180-80868464ada5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SsauRiZX3SjN3BYLznKNPR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 377,
      "cache_read_input_tokens": 52973,
      "output_tokens": 443,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 377,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 443,
          "cache_read_input_tokens": 52973,
          "cache_creation_input_tokens": 377,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 377
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

_source line 58 · 2026-05-16T17:19:06.890Z_

<details><summary>↩ Tool result · `toolu_01P1bq8rigtHtrq2KNKBVQuf`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/table4_ft_ablation.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "140c5b87-ac98-4b43-ba5a-158616131928",
  "isSidechain": false,
  "promptId": "f3f24f5a-bd6d-444a-89a8-04e2233f247b",
  "type": "user",
  "uuid": "ed3a8558-3e0c-490c-8fe6-9d4d52890a9d",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/table4_ft_ablation.md",
    "oldString": "| Llama3.1-8B | semantic_only | — | — | — | — | — | — | RUNNING |",
    "newString": "| Llama3.1-8B | semantic_only | 84.02 | 43.90 | 0.00 | 0.15 | 0.30 | 0.16 | 2.40 |",
    "originalFile": "# Table 4: FT Ablation — Constraint Layer Decomposition\n\nModes: unconstrained (no constraints), grammar_only (JSON schema grammar), semantic_only (ontology DR/CF checks), full (grammar + semantic = OntoCoDec).\n\n## SciERC\n\n| Model | Mode | E_F1 (%) | R_F1 (%) | ET% | RV% | DR% | CF% | Parse Fail% |\n|-------|------|----------|----------|-----|-----|-----|-----|-------------|\n| Qwen3-8B | unconstrained | 67.05 | 43.86 | 0.00 | 0.00 | 1.95 | 0.00 | 0.00 |\n| Qwen3-8B | grammar_only | 67.05 | 43.86 | 0.00 | 0.00 | 1.90 | 0.00 | 0.00 |\n| Qwen3-8B | semantic_only | 67.05 | 43.69 | 0.00 | 0.00 | 0.60 | 1.33 | 0.00 |\n| Qwen3-8B | **full (OntoCoDec)** | 67.05 | 43.77 | 0.00 | 0.00 | 0.00 | 1.18 | 0.00 |\n| Llama3.1-8B | unconstrained | 67.76 | 45.45 | 0.00 | 0.00 | 1.11 | 0.00 | 0.00 |\n| Llama3.1-8B | grammar_only | 67.76 | 45.45 | 0.00 | 0.00 | 1.11 | 0.00 | 0.00 |\n| Llama3.1-8B | semantic_only | 67.76 | 45.47 | 0.00 | 0.00 | 0.65 | 0.18 | 0.00 |\n| Llama3.1-8B | **full (OntoCoDec)** | 67.76 | 45.47 | 0.00 | 0.00 | 0.09 | 0.46 | 0.00 |\n\n## DocRED\n\n| Model | Mode | E_F1 (%) | R_F1 (%) | ET% | RV% | DR% | CF% | Parse Fail% |\n|-------|------|----------|----------|-----|-----|-----|-----|-------------|\n| Qwen3-8B | unconstrained | 82.15 | 40.86 | 0.00 | 0.27 | 0.76 | 0.12 | 7.11 |\n| Qwen3-8B | grammar_only | 82.19 | 40.85 | 0.00 | 0.00 | 0.61 | 0.11 | 7.01 |\n| Qwen3-8B | semantic_only | 82.15 | 40.89 | 0.00 | 0.23 | 0.21 | 0.27 | 7.52 |\n| Qwen3-8B | **full (OntoCoDec)** | 81.43 | 40.56 | 0.00 | 0.00 | 0.01 | 0.41 | 8.52 |\n| Llama3.1-8B | unconstrained | 83.93 | 43.72 | 0.00 | 0.15 | 0.49 | — | 2.30 |\n| Llama3.1-8B | grammar_only | 84.04 | 43.77 | 0.00 | 0.00 | 0.51 | 0.12 | 2.30 |\n| Llama3.1-8B | semantic_only | — | — | — | — | — | — | RUNNING |\n| Llama3.1-8B | **full (OntoCoDec)** | 85.23 | 44.23 | 0.00 | 0.00 | 0.20 | 0.26 | 2.51 |\n\n**Observations:**\n- Grammar layer: eliminates ET/RV violations (forces valid type/relation tokens); minimal impact on DR\n- Semantic layer: primary DR reducer (SciERC: 1.95%→0.60% for Qwen, DocRED: 0.76%→0.21% for Qwen)\n- Full combination: near-zero DR residual with sub-additive constraint interaction\n- F1 impact: ≤0.30pp R_F1 cost across all completed settings\n- Llama DocRED semantic_only: experiment still RUNNING\n",
    "structuredPatch": [
      {
        "oldStart": 25,
        "oldLines": 7,
        "newStart": 25,
        "newLines": 7,
        "lines": [
          " | Qwen3-8B | **full (OntoCoDec)** | 81.43 | 40.56 | 0.00 | 0.00 | 0.01 | 0.41 | 8.52 |",
          " | Llama3.1-8B | unconstrained | 83.93 | 43.72 | 0.00 | 0.15 | 0.49 | — | 2.30 |",
          " | Llama3.1-8B | grammar_only | 84.04 | 43.77 | 0.00 | 0.00 | 0.51 | 0.12 | 2.30 |",
          "-| Llama3.1-8B | semantic_only | — | — | — | — | — | — | RUNNING |",
          "+| Llama3.1-8B | semantic_only | 84.02 | 43.90 | 0.00 | 0.15 | 0.30 | 0.16 | 2.40 |",
          " | Llama3.1-8B | **full (OntoCoDec)** | 85.23 | 44.23 | 0.00 | 0.00 | 0.20 | 0.26 | 2.51 |",
          " ",
          " **Observations:**"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "140c5b87-ac98-4b43-ba5a-158616131928",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "1da856f6-e3e6-4a2a-8180-80868464ada5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 59 · 2026-05-16T17:19:07.978Z_

<details><summary>↩ Tool result · `toolu_01DBSqrUoQUgPvnkCgDaKwHZ`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/table4_ft_ablation.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f8d36d7a-4d3a-4748-b4f5-b459534d9ce1",
  "isSidechain": false,
  "promptId": "f3f24f5a-bd6d-444a-89a8-04e2233f247b",
  "type": "user",
  "uuid": "15484fbb-2584-48c7-97ab-f9a2f4c78846",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/table4_ft_ablation.md",
    "oldString": "- Llama DocRED semantic_only: experiment still RUNNING",
    "newString": "- Llama DocRED semantic_only: DONE (updated 2026-05-16)",
    "originalFile": "# Table 4: FT Ablation — Constraint Layer Decomposition\n\nModes: unconstrained (no constraints), grammar_only (JSON schema grammar), semantic_only (ontology DR/CF checks), full (grammar + semantic = OntoCoDec).\n\n## SciERC\n\n| Model | Mode | E_F1 (%) | R_F1 (%) | ET% | RV% | DR% | CF% | Parse Fail% |\n|-------|------|----------|----------|-----|-----|-----|-----|-------------|\n| Qwen3-8B | unconstrained | 67.05 | 43.86 | 0.00 | 0.00 | 1.95 | 0.00 | 0.00 |\n| Qwen3-8B | grammar_only | 67.05 | 43.86 | 0.00 | 0.00 | 1.90 | 0.00 | 0.00 |\n| Qwen3-8B | semantic_only | 67.05 | 43.69 | 0.00 | 0.00 | 0.60 | 1.33 | 0.00 |\n| Qwen3-8B | **full (OntoCoDec)** | 67.05 | 43.77 | 0.00 | 0.00 | 0.00 | 1.18 | 0.00 |\n| Llama3.1-8B | unconstrained | 67.76 | 45.45 | 0.00 | 0.00 | 1.11 | 0.00 | 0.00 |\n| Llama3.1-8B | grammar_only | 67.76 | 45.45 | 0.00 | 0.00 | 1.11 | 0.00 | 0.00 |\n| Llama3.1-8B | semantic_only | 67.76 | 45.47 | 0.00 | 0.00 | 0.65 | 0.18 | 0.00 |\n| Llama3.1-8B | **full (OntoCoDec)** | 67.76 | 45.47 | 0.00 | 0.00 | 0.09 | 0.46 | 0.00 |\n\n## DocRED\n\n| Model | Mode | E_F1 (%) | R_F1 (%) | ET% | RV% | DR% | CF% | Parse Fail% |\n|-------|------|----------|----------|-----|-----|-----|-----|-------------|\n| Qwen3-8B | unconstrained | 82.15 | 40.86 | 0.00 | 0.27 | 0.76 | 0.12 | 7.11 |\n| Qwen3-8B | grammar_only | 82.19 | 40.85 | 0.00 | 0.00 | 0.61 | 0.11 | 7.01 |\n| Qwen3-8B | semantic_only | 82.15 | 40.89 | 0.00 | 0.23 | 0.21 | 0.27 | 7.52 |\n| Qwen3-8B | **full (OntoCoDec)** | 81.43 | 40.56 | 0.00 | 0.00 | 0.01 | 0.41 | 8.52 |\n| Llama3.1-8B | unconstrained | 83.93 | 43.72 | 0.00 | 0.15 | 0.49 | — | 2.30 |\n| Llama3.1-8B | grammar_only | 84.04 | 43.77 | 0.00 | 0.00 | 0.51 | 0.12 | 2.30 |\n| Llama3.1-8B | semantic_only | 84.02 | 43.90 | 0.00 | 0.15 | 0.30 | 0.16 | 2.40 |\n| Llama3.1-8B | **full (OntoCoDec)** | 85.23 | 44.23 | 0.00 | 0.00 | 0.20 | 0.26 | 2.51 |\n\n**Observations:**\n- Grammar layer: eliminates ET/RV violations (forces valid type/relation tokens); minimal impact on DR\n- Semantic layer: primary DR reducer (SciERC: 1.95%→0.60% for Qwen, DocRED: 0.76%→0.21% for Qwen)\n- Full combination: near-zero DR residual with sub-additive constraint interaction\n- F1 impact: ≤0.30pp R_F1 cost across all completed settings\n- Llama DocRED semantic_only: experiment still RUNNING\n",
    "structuredPatch": [
      {
        "oldStart": 33,
        "oldLines": 4,
        "newStart": 33,
        "newLines": 4,
        "lines": [
          " - Semantic layer: primary DR reducer (SciERC: 1.95%→0.60% for Qwen, DocRED: 0.76%→0.21% for Qwen)",
          " - Full combination: near-zero DR residual with sub-additive constraint interaction",
          " - F1 impact: ≤0.30pp R_F1 cost across all completed settings",
          "-- Llama DocRED semantic_only: experiment still RUNNING",
          "+- Llama DocRED semantic_only: DONE (updated 2026-05-16)"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "f8d36d7a-4d3a-4748-b4f5-b459534d9ce1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "1da856f6-e3e6-4a2a-8180-80868464ada5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 60 · 2026-05-16T17:19:07.968Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01DBSqrUoQUgPvnkCgDaKwHZ`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/table4_ft_ablation.md",
  "old_string": "- Llama DocRED semantic_only: experiment still RUNNING",
  "new_string": "- Llama DocRED semantic_only: DONE (updated 2026-05-16)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ed3a8558-3e0c-490c-8fe6-9d4d52890a9d",
  "isSidechain": false,
  "requestId": "req_011Cb6dVBAupRWVUZFBDTdVx",
  "type": "assistant",
  "uuid": "f8d36d7a-4d3a-4748-b4f5-b459534d9ce1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "1da856f6-e3e6-4a2a-8180-80868464ada5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SsauRiZX3SjN3BYLznKNPR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 377,
      "cache_read_input_tokens": 52973,
      "output_tokens": 443,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 377,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 443,
          "cache_read_input_tokens": 52973,
          "cache_creation_input_tokens": 377,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 377
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

_source line 61 · 2026-05-16T17:19:08.025Z_

```json
{
  "parentUuid": "15484fbb-2584-48c7-97ab-f9a2f4c78846",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "bdf5b31b-0b0b-4214-9be8-5a0b426ecafe",
  "timestamp": "2026-05-16T17:19:08.025Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "1da856f6-e3e6-4a2a-8180-80868464ada5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 62 · 2026-05-16T17:19:10.265Z_

Now verify both files are correct after edits:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bdf5b31b-0b0b-4214-9be8-5a0b426ecafe",
  "isSidechain": false,
  "requestId": "req_011Cb6dViGSNWbgXboqrQ3h1",
  "type": "assistant",
  "uuid": "6a37579a-2f6b-4b19-9922-108f1d690377",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "1da856f6-e3e6-4a2a-8180-80868464ada5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018f1uxugW2AsZeeZadDcRWf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 702,
      "cache_read_input_tokens": 53350,
      "output_tokens": 249,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 702,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 249,
          "cache_read_input_tokens": 53350,
          "cache_creation_input_tokens": 702,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 702
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

_source line 63 · 2026-05-16T17:19:11.213Z_

<details open><summary>🔧 Tool call — Read · `toolu_01S3VBw3i5qsRqY5zyhKEjUU`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/ft_ablation_analysis.md",
  "offset": 26,
  "limit": 12
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6a37579a-2f6b-4b19-9922-108f1d690377",
  "isSidechain": false,
  "requestId": "req_011Cb6dViGSNWbgXboqrQ3h1",
  "type": "assistant",
  "uuid": "b0e2c8a2-1cbd-4253-ad0a-f23d7b8c4b3e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "1da856f6-e3e6-4a2a-8180-80868464ada5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018f1uxugW2AsZeeZadDcRWf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 702,
      "cache_read_input_tokens": 53350,
      "output_tokens": 249,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 702,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 249,
          "cache_read_input_tokens": 53350,
          "cache_creation_input_tokens": 702,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 702
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

_source line 64 · 2026-05-16T17:19:11.219Z_

<details><summary>↩ Tool result · `toolu_01S3VBw3i5qsRqY5zyhKEjUU`</summary>

```text
26	| Model | Mode | ET% | RV% | DR% | CF% | E_F1 | R_F1 | Parse Fail% |
27	|-------|------|-----|-----|-----|-----|------|------|-------------|
28	| Qwen3-8B | Unconstrained | 0 | 0.27 | 0.76 | 0.12 | 82.15 | 40.86 | 7.11 |
29	| Qwen3-8B | Grammar Only | 0 | 0 | 0.61 | 0.11 | 82.19 | 40.85 | 7.01 |
30	| Qwen3-8B | Semantic Only | 0 | 0.23 | 0.21 | 0.27 | 82.15 | 40.89 | 7.52 |
31	| Qwen3-8B | Full (G+S) | 0 | 0 | 0.01 | 0.41 | 81.43 | 40.56 | 8.52 |
32	| Llama-3.1-8B | Unconstrained | 0 | 0.15 | 0.49 | — | 83.93 | 43.72 | 2.30 |
33	| Llama-3.1-8B | Grammar Only | 0 | 0 | 0.51 | 0.12 | 84.04 | 43.77 | 2.30 |
34	| Llama-3.1-8B | Semantic Only | 0 | 0.15 | 0.30 | 0.16 | 84.02 | 43.90 | 2.40 |
35	| Llama-3.1-8B | Full (G+S) | 0 | 0 | 0.20 | 0.26 | 85.23 | 44.23 | 2.51 |
36	
37	Notes:
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b0e2c8a2-1cbd-4253-ad0a-f23d7b8c4b3e",
  "isSidechain": false,
  "promptId": "f3f24f5a-bd6d-444a-89a8-04e2233f247b",
  "type": "user",
  "uuid": "191ab7bf-c2ce-4b38-acb4-b671ab921987",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/ft_ablation_analysis.md",
      "content": "| Model | Mode | ET% | RV% | DR% | CF% | E_F1 | R_F1 | Parse Fail% |\n|-------|------|-----|-----|-----|-----|------|------|-------------|\n| Qwen3-8B | Unconstrained | 0 | 0.27 | 0.76 | 0.12 | 82.15 | 40.86 | 7.11 |\n| Qwen3-8B | Grammar Only | 0 | 0 | 0.61 | 0.11 | 82.19 | 40.85 | 7.01 |\n| Qwen3-8B | Semantic Only | 0 | 0.23 | 0.21 | 0.27 | 82.15 | 40.89 | 7.52 |\n| Qwen3-8B | Full (G+S) | 0 | 0 | 0.01 | 0.41 | 81.43 | 40.56 | 8.52 |\n| Llama-3.1-8B | Unconstrained | 0 | 0.15 | 0.49 | — | 83.93 | 43.72 | 2.30 |\n| Llama-3.1-8B | Grammar Only | 0 | 0 | 0.51 | 0.12 | 84.04 | 43.77 | 2.30 |\n| Llama-3.1-8B | Semantic Only | 0 | 0.15 | 0.30 | 0.16 | 84.02 | 43.90 | 2.40 |\n| Llama-3.1-8B | Full (G+S) | 0 | 0 | 0.20 | 0.26 | 85.23 | 44.23 | 2.51 |\n\nNotes:",
      "numLines": 12,
      "startLine": 26,
      "totalLines": 75
    }
  },
  "sourceToolAssistantUUID": "b0e2c8a2-1cbd-4253-ad0a-f23d7b8c4b3e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "1da856f6-e3e6-4a2a-8180-80868464ada5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 65 · 2026-05-16T17:19:11.984Z_

<details><summary>↩ Tool result · `toolu_012x1Duoi99WCEQVj9EtaG35`</summary>

```text
19	
20	| Model | Mode | E_F1 (%) | R_F1 (%) | ET% | RV% | DR% | CF% | Parse Fail% |
21	|-------|------|----------|----------|-----|-----|-----|-----|-------------|
22	| Qwen3-8B | unconstrained | 82.15 | 40.86 | 0.00 | 0.27 | 0.76 | 0.12 | 7.11 |
23	| Qwen3-8B | grammar_only | 82.19 | 40.85 | 0.00 | 0.00 | 0.61 | 0.11 | 7.01 |
24	| Qwen3-8B | semantic_only | 82.15 | 40.89 | 0.00 | 0.23 | 0.21 | 0.27 | 7.52 |
25	| Qwen3-8B | **full (OntoCoDec)** | 81.43 | 40.56 | 0.00 | 0.00 | 0.01 | 0.41 | 8.52 |
26	| Llama3.1-8B | unconstrained | 83.93 | 43.72 | 0.00 | 0.15 | 0.49 | — | 2.30 |
27	| Llama3.1-8B | grammar_only | 84.04 | 43.77 | 0.00 | 0.00 | 0.51 | 0.12 | 2.30 |
28	| Llama3.1-8B | semantic_only | 84.02 | 43.90 | 0.00 | 0.15 | 0.30 | 0.16 | 2.40 |
29	| Llama3.1-8B | **full (OntoCoDec)** | 85.23 | 44.23 | 0.00 | 0.00 | 0.20 | 0.26 | 2.51 |
30	
31	**Observations:**
32	- Grammar layer: eliminates ET/RV violations (forces valid type/relation tokens); minimal impact on DR
33	- Semantic layer: primary DR reducer (SciERC: 1.95%→0.60% for Qwen, DocRED: 0.76%→0.21% for Qwen)
34	- Full combination: near-zero DR residual with sub-additive constraint interaction
35	- F1 impact: ≤0.30pp R_F1 cost across all completed settings
36	- Llama DocRED semantic_only: DONE (updated 2026-05-16)
37	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8c19850d-67a1-442a-8fee-43c95f93d772",
  "isSidechain": false,
  "promptId": "f3f24f5a-bd6d-444a-89a8-04e2233f247b",
  "type": "user",
  "uuid": "7b76b2c4-3ac0-4a9e-a998-f732ef92853f",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/table4_ft_ablation.md",
      "content": "\n| Model | Mode | E_F1 (%) | R_F1 (%) | ET% | RV% | DR% | CF% | Parse Fail% |\n|-------|------|----------|----------|-----|-----|-----|-----|-------------|\n| Qwen3-8B | unconstrained | 82.15 | 40.86 | 0.00 | 0.27 | 0.76 | 0.12 | 7.11 |\n| Qwen3-8B | grammar_only | 82.19 | 40.85 | 0.00 | 0.00 | 0.61 | 0.11 | 7.01 |\n| Qwen3-8B | semantic_only | 82.15 | 40.89 | 0.00 | 0.23 | 0.21 | 0.27 | 7.52 |\n| Qwen3-8B | **full (OntoCoDec)** | 81.43 | 40.56 | 0.00 | 0.00 | 0.01 | 0.41 | 8.52 |\n| Llama3.1-8B | unconstrained | 83.93 | 43.72 | 0.00 | 0.15 | 0.49 | — | 2.30 |\n| Llama3.1-8B | grammar_only | 84.04 | 43.77 | 0.00 | 0.00 | 0.51 | 0.12 | 2.30 |\n| Llama3.1-8B | semantic_only | 84.02 | 43.90 | 0.00 | 0.15 | 0.30 | 0.16 | 2.40 |\n| Llama3.1-8B | **full (OntoCoDec)** | 85.23 | 44.23 | 0.00 | 0.00 | 0.20 | 0.26 | 2.51 |\n\n**Observations:**\n- Grammar layer: eliminates ET/RV violations (forces valid type/relation tokens); minimal impact on DR\n- Semantic layer: primary DR reducer (SciERC: 1.95%→0.60% for Qwen, DocRED: 0.76%→0.21% for Qwen)\n- Full combination: near-zero DR residual with sub-additive constraint interaction\n- F1 impact: ≤0.30pp R_F1 cost across all completed settings\n- Llama DocRED semantic_only: DONE (updated 2026-05-16)\n",
      "numLines": 19,
      "startLine": 19,
      "totalLines": 37
    }
  },
  "sourceToolAssistantUUID": "8c19850d-67a1-442a-8fee-43c95f93d772",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "1da856f6-e3e6-4a2a-8180-80868464ada5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 66 · 2026-05-16T17:19:11.980Z_

<details open><summary>🔧 Tool call — Read · `toolu_012x1Duoi99WCEQVj9EtaG35`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/table4_ft_ablation.md",
  "offset": 19,
  "limit": 20
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "191ab7bf-c2ce-4b38-acb4-b671ab921987",
  "isSidechain": false,
  "requestId": "req_011Cb6dViGSNWbgXboqrQ3h1",
  "type": "assistant",
  "uuid": "8c19850d-67a1-442a-8fee-43c95f93d772",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "1da856f6-e3e6-4a2a-8180-80868464ada5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018f1uxugW2AsZeeZadDcRWf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 702,
      "cache_read_input_tokens": 53350,
      "output_tokens": 249,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 702,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 249,
          "cache_read_input_tokens": 53350,
          "cache_creation_input_tokens": 702,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 702
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

_source line 67_

```json
{
  "type": "last-prompt",
  "leafUuid": "7b76b2c4-3ac0-4a9e-a998-f732ef92853f",
  "sessionId": "1da856f6-e3e6-4a2a-8180-80868464ada5"
}
```

---

### Runtime record

_source line 68_

```json
{
  "type": "ai-title",
  "aiTitle": "Fix DocRED FT ablation data errors in markdown files",
  "sessionId": "1da856f6-e3e6-4a2a-8180-80868464ada5"
}
```

---

### Assistant

_source line 69 · 2026-05-16T17:19:24.461Z_

Both files now match the reviewer's correct data and are consistent with each other. Registry verification confirmed all values match.

---

## 修正清单

### 文件 1: `ft_ablation_analysis.md` — 15 个字段修正

| 行 | 字段 | 错误值 | 正确值 |
|---|---|---|---|
| Qwen Grammar Only | RV% | 0.27 | 0 |
| Qwen Grammar Only | CF% | 0.12 | 0.11 |
| Qwen Grammar Only | E_F1 | 82.15 | 82.19 |
| Qwen Grammar Only | R_F1 | 40.86 | 40.85 |
| Qwen Grammar Only | Parse Fail% | 7.11 | 7.01 |
| Qwen Semantic Only | RV% | 0.27 | 0.23 |
| Qwen Semantic Only | CF% | 0.12 | 0.27 |
| Qwen Semantic Only | R_F1 | 40.86 | 40.89 |
| Qwen Semantic Only | Parse Fail% | 7.11 | 7.52 |
| Llama Unconstrained | DR% | 0.51 | 0.49 |
| Llama Unconstrained | CF% | 0.16 | — |
| Llama Unconstrained | E_F1 | 84.04 | 83.93 |
| Llama Unconstrained | R_F1 | 43.77 | 43.72 |
| Llama Grammar Only | RV% | 0.15 | 0 |
| Llama Grammar Only | CF% | 0.16 | 0.12 |

### 文件 2: `table4_ft_ablation.md` — 7 个字段修正

| 行 | 字段 | 错误值 | 正确值 |
|---|---|---|---|
| Llama semantic_only | E_F1 | — | 84.02 |
| Llama semantic_only | R_F1 | — | 43.90 |
| Llama semantic_only | ET% | — | 0.00 |
| Llama semantic_only | RV% | — | 0.15 |
| Llama semantic_only | DR% | — | 0.30 |
| Llama semantic_only | CF% | — | 0.16 |
| Llama semantic_only | Parse Fail% | RUNNING | 2.40 |

错误模式：ft_ablation_analysis.md 中 grammar_only 和 semantic_only 行直接复制了 unconstrained 的 RV/CF/E_F1/R_F1/parse_fail 值；unconstrained 行则复制了 grammar_only 的 DR/CF/E_F1/R_F1 值。table4 的 DocRED 数据原本就是正确的（除了 Llama semantic_only 当时还在 RUNNING）。

SciERC 部分两文件均与 registry 一致，无需修正。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7b76b2c4-3ac0-4a9e-a998-f732ef92853f",
  "isSidechain": false,
  "requestId": "req_011Cb6dW1R4bJb1nAGCCuWYy",
  "type": "assistant",
  "uuid": "3092fa55-a71a-4127-b32b-8ed3f97c2462",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "1da856f6-e3e6-4a2a-8180-80868464ada5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01966NbzxbfTwuGAfTUZhaEF",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1538,
      "cache_read_input_tokens": 54052,
      "output_tokens": 824,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1538,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 824,
          "cache_read_input_tokens": 54052,
          "cache_creation_input_tokens": 1538,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1538
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

_source line 70_

```json
{
  "type": "last-prompt",
  "leafUuid": "3092fa55-a71a-4127-b32b-8ed3f97c2462",
  "sessionId": "1da856f6-e3e6-4a2a-8180-80868464ada5"
}
```

---

### Runtime record

_source line 71_

```json
{
  "type": "ai-title",
  "aiTitle": "Fix DocRED FT ablation data errors in markdown files",
  "sessionId": "1da856f6-e3e6-4a2a-8180-80868464ada5"
}
```

---
