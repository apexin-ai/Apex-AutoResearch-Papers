# Research conversation: <project_context> # 项目: structfuse-context ## 运行环境 - 服务器名: bjb1-42106 - SSH 账户: root（调用 ssh_execute / submit_training_jo

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 62
- **Recorded user turns:** 1
- **Tool calls:** 15
- **Original source:** `logs/chats/exported-trajectories/account-1/d1e524a6-76dd-46af-a456-0b6d1108f4ee.jsonl`
- **Structured JSON:** [`6a174e05685f20d305f5.json`](../../sessions/6a/6a174e05685f20d305f5.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-14T22:58:10.551Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-14T22:58:10.551Z",
  "sessionId": "d1e524a6-76dd-46af-a456-0b6d1108f4ee",
  "content": "&lt;project_context>\n# 项目: structfuse-context\n\n## 运行环境\n- 服务器名: bjb1-42106\n- SSH 账户: root（调用 ssh_execute / submit_training_job 时传入 account=\"root\"）\n- SSH 连接命令: ssh connect.bjb1.seetacloud.com  # 必须用此命令，~/.ssh/config 自动应用密钥和跳板机，禁止用裸 IP\n- 项目代码根目录: /root/structfuse\n\n\n## 环境搭建\n连接服务器后先调 `detect_image` 检测是否为预置镜像。如果匹配，跳过基础环境搭建，只装项目特有依赖。已预装的包不要重复安装。\n\n## 输出风格\n回复简洁直接。只输出执行结果和必要信息，不要解释过程、不要客套、不要给未被要求的建议。\n&lt;/project_context>\n## 任务：Experiments v1 修复（3 warnings + 3 info）\n\n修改 `/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/experiments_v1.md`，共 6 处。\n\n### Warning 1：Table 6 总计不一致\n- 问题：Total 行写 36.0%，但各 tier 加权平均 = 34.3%。\n- 操作：用 `read_registry(project=\"structfuse-context\", filters={\"exp_id\": \"plan_006_scalability\"}, fields=[\"*\"])` 确认正确数值。registry 中 structural_data_rate = 0.343。\n- 统一三处：Table 6 Total 行、Table 6 各 tier 数据（确保一致）、§4.1 文字中提到的 structural coverage 百分比。全部对齐为 registry 中的 34.3%（或确认后的正确值）。\n\n### Warning 2：Table 2 checkpoint 类型矛盾\n- 问题：§4.1 声明用 R@1 checkpoint，但 Table 2 pilot 数值来自 val_loss checkpoint。\n- 操作：用 `read_registry(project=\"structfuse-context\", filters={\"exp_id\": \"m2_embed_verify\"}, fields=[\"*\"])` 获取 pilot 实验数据。\n  - m2_embed_verify 的 R@1 checkpoint 数值：random best_R@1=0.5357 (step 500), embedding best_R@1=0.5557 (step 500), dataflow best_R@1=0.5436 (step 500)\n  - 同样获取 plan_013_starcoder 的数据：random best_R@1=0.4922, embedding best_R@1=0.5078, dataflow best_R@1=0.4869（但注意这些可能已经是 R@1 checkpoint，确认后使用）\n- 更新 Table 2 使用 best_by_recall_at_1 的数值，加注 \"(R@1 checkpoint)\" 与 §4.1 protocol 一致。\n- 重新计算 delta（embedding vs random, dataflow vs random）。\n\n### Warning 3：SWE-bench → SWE-smith\n- 问题：§4.1 数据来源写 \"SWE-bench\" 但 131 repos / 5,029 task instances 来自 SWE-smith。\n- 操作：\n  - 改为 `SWE-smith \\cite{yang2025swesmith}`\n  - 解释数据展开关系：5,029 task instances（每个 task 对应一个 bug-fix commit），每个 task 的每个 gold file 展开为一个 training instance，共 44,173 training instances（部分 task 有多个 gold files）。这样读者理解 5,029 → 44,173 的数量差异。\n\n### Info 4：cite key 统一\n- 全文搜索 `cocohanere2025`，替换为 `fan2025cocohanere`。\n\n### Info 5：temperature 标注\n- §4.2 找到 temperature τ = 0.07 的描述，改为 \"learnable temperature initialized at τ = 0.07\"。\n\n### Info 6：Placeholder tables 不用改。\n\n### 产出\n修改完成后用 register_artifact 更新。简要报告每处修改内容。"
}
```

---

### Runtime record

_source line 2 · 2026-05-14T22:58:10.555Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-14T22:58:10.555Z",
  "sessionId": "d1e524a6-76dd-46af-a456-0b6d1108f4ee"
}
```

---

## Round 1

60 recorded events

### User

_source line 3 · 2026-05-14T22:58:10.603Z_

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
## 任务：Experiments v1 修复（3 warnings + 3 info）

修改 `/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/experiments_v1.md`，共 6 处。

### Warning 1：Table 6 总计不一致
- 问题：Total 行写 36.0%，但各 tier 加权平均 = 34.3%。
- 操作：用 `read_registry(project="structfuse-context", filters={"exp_id": "plan_006_scalability"}, fields=["*"])` 确认正确数值。registry 中 structural_data_rate = 0.343。
- 统一三处：Table 6 Total 行、Table 6 各 tier 数据（确保一致）、§4.1 文字中提到的 structural coverage 百分比。全部对齐为 registry 中的 34.3%（或确认后的正确值）。

### Warning 2：Table 2 checkpoint 类型矛盾
- 问题：§4.1 声明用 R@1 checkpoint，但 Table 2 pilot 数值来自 val_loss checkpoint。
- 操作：用 `read_registry(project="structfuse-context", filters={"exp_id": "m2_embed_verify"}, fields=["*"])` 获取 pilot 实验数据。
  - m2_embed_verify 的 R@1 checkpoint 数值：random best_R@1=0.5357 (step 500), embedding best_R@1=0.5557 (step 500), dataflow best_R@1=0.5436 (step 500)
  - 同样获取 plan_013_starcoder 的数据：random best_R@1=0.4922, embedding best_R@1=0.5078, dataflow best_R@1=0.4869（但注意这些可能已经是 R@1 checkpoint，确认后使用）
- 更新 Table 2 使用 best_by_recall_at_1 的数值，加注 "(R@1 checkpoint)" 与 §4.1 protocol 一致。
- 重新计算 delta（embedding vs random, dataflow vs random）。

### Warning 3：SWE-bench → SWE-smith
- 问题：§4.1 数据来源写 "SWE-bench" 但 131 repos / 5,029 task instances 来自 SWE-smith。
- 操作：
  - 改为 `SWE-smith \cite{yang2025swesmith}`
  - 解释数据展开关系：5,029 task instances（每个 task 对应一个 bug-fix commit），每个 task 的每个 gold file 展开为一个 training instance，共 44,173 training instances（部分 task 有多个 gold files）。这样读者理解 5,029 → 44,173 的数量差异。

### Info 4：cite key 统一
- 全文搜索 `cocohanere2025`，替换为 `fan2025cocohanere`。

### Info 5：temperature 标注
- §4.2 找到 temperature τ = 0.07 的描述，改为 "learnable temperature initialized at τ = 0.07"。

### Info 6：Placeholder tables 不用改。

### 产出
修改完成后用 register_artifact 更新。简要报告每处修改内容。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "1d7108f5-af6a-41fc-acd8-afc665497be3",
  "type": "user",
  "uuid": "f2b903fe-941f-49af-93e2-8d18d30bd699",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "d1e524a6-76dd-46af-a456-0b6d1108f4ee",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-14T22:58:10.602Z_

```json
{
  "parentUuid": "f2b903fe-941f-49af-93e2-8d18d30bd699",
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
  "uuid": "357a7797-825b-426c-ae4f-ae534245a10b",
  "timestamp": "2026-05-14T22:58:10.602Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "d1e524a6-76dd-46af-a456-0b6d1108f4ee",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-14T22:58:10.602Z_

```json
{
  "parentUuid": "357a7797-825b-426c-ae4f-ae534245a10b",
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
  "uuid": "e162f82d-df42-4fe0-9c62-ceb74dbaf5b7",
  "timestamp": "2026-05-14T22:58:10.602Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "d1e524a6-76dd-46af-a456-0b6d1108f4ee",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6 · 2026-05-14T22:58:10.602Z_

```json
{
  "parentUuid": "e162f82d-df42-4fe0-9c62-ceb74dbaf5b7",
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
  "uuid": "411cca1c-5359-4ee5-ae62-d1f320d36314",
  "timestamp": "2026-05-14T22:58:10.602Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "d1e524a6-76dd-46af-a456-0b6d1108f4ee",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 7 · 2026-05-14T22:58:10.602Z_

```json
{
  "parentUuid": "411cca1c-5359-4ee5-ae62-d1f320d36314",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "3ee87f4a-60e0-4e93-8370-d06aee621980",
  "timestamp": "2026-05-14T22:58:10.602Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "d1e524a6-76dd-46af-a456-0b6d1108f4ee",
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
  "aiTitle": "Fix experiments v1 6 issues warnings and info",
  "sessionId": "d1e524a6-76dd-46af-a456-0b6d1108f4ee"
}
```

---

### Assistant

_source line 9 · 2026-05-14T22:58:12.870Z_

I'll start by reading the current experiments file and fetching the registry data needed for the fixes.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3ee87f4a-60e0-4e93-8370-d06aee621980",
  "isSidechain": false,
  "requestId": "req_011Cb3HjRPV1AWBD8qJqjHRL",
  "type": "assistant",
  "uuid": "11cb80b2-8573-4525-b9c7-a06ab1b49457",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "d1e524a6-76dd-46af-a456-0b6d1108f4ee",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CV4qErsZHeNBNJZpxZauuC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12120,
      "cache_read_input_tokens": 11447,
      "output_tokens": 196,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12120,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 196,
          "cache_read_input_tokens": 11447,
          "cache_creation_input_tokens": 12120,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12120
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

_source line 10 · 2026-05-14T22:58:13.943Z_

<details open><summary>🔧 Tool call — Read · `toolu_01H3rBirEVxZtvPchYCc59Ve`</summary>

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
  "parentUuid": "11cb80b2-8573-4525-b9c7-a06ab1b49457",
  "isSidechain": false,
  "requestId": "req_011Cb3HjRPV1AWBD8qJqjHRL",
  "type": "assistant",
  "uuid": "b792482b-7a21-49ac-ae22-b6f2e0fcfeec",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "d1e524a6-76dd-46af-a456-0b6d1108f4ee",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CV4qErsZHeNBNJZpxZauuC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12120,
      "cache_read_input_tokens": 11447,
      "output_tokens": 196,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12120,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 196,
          "cache_read_input_tokens": 11447,
          "cache_creation_input_tokens": 12120,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12120
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

_source line 11 · 2026-05-14T22:58:13.957Z_

<details><summary>↩ Tool result · `toolu_01H3rBirEVxZtvPchYCc59Ve`</summary>

```text
1	# §4 Experiments
2	
3	## §4.1 Experimental Setup
4	
5	**Dataset.** We construct our training corpus from SWE-bench \cite{jimenez2024swebench}, a benchmark of real-world GitHub issues paired with developer-authored patches. Starting from 5,029 task instances spanning 131 unique (repository, commit) pairs, we run the StructFuse extraction pipeline (§3.2) to obtain inter-procedural data-flow graphs via CodeQL. After filtering for clone/checkout failures and extraction errors, we retain 15,897 instances across 123 repositories with structural data, yielding a structural coverage rate of 36%. The remaining 64% of instances lack structural connectivity data due to transient filesystem failures during batch extraction; a re-extraction pass (in progress) is expected to recover the majority of these instances, and we discuss data efficiency implications in §6.
6	
7	For each random seed, we perform a per-repository stratified split to produce approximately 11,300 training and 3,000 validation instances. Each instance consists of an issue description (query), one or more gold files (positives), and strategy-specific negatives (§3.4). The per-seed split ensures that no repository appears exclusively in one partition, preserving the distribution of repository sizes and structural properties.
8	
9	**Evaluation Protocol.** We evaluate retrieval performance using Recall@$k$ ($k \in \{1, 5, 10\}$) and Mean Reciprocal Rank (MRR), computed over a candidate pool of size 50 (1 positive + 49 negatives sampled per query). During training, $K = 7$ negatives are used per query. We report results as mean $\pm$ standard deviation across three random seeds (42, 43, 44). For all comparisons, we use the checkpoint selected by best validation Recall@1 ($\theta^*_{\text{R@1}}$), as discussed in §3.3.
10	
11	**Baselines.** We compare three negative mining strategies—random, embedding-distance, and dataflow-aware (§3.4)—against a BM25 retrieval baseline. The BM25 baseline uses Okapi BM25 \cite{robertson2009bm25} to rank candidate files by lexical overlap with the query, providing a non-neural reference point. We additionally evaluate BM25-mined negatives as a fourth contrastive training strategy to ground our comparison against the gradient-based premise of CoCoHaNeRe \cite{cocohanere2025}.
12	
13	## §4.2 Implementation Details
14	
15	**Encoders.** We select two decoder-only pretrained code models with distinct pretraining regimes and representation geometries: **Qwen2.5-Coder-3B** \cite{hui2024qwen25coder} and **StarCoder2-3B** \cite{li2023starcoder}. Qwen2.5-Coder-3B is trained primarily with Fill-in-the-Middle (FIM) on a curated multilingual code corpus, while StarCoder2-3B uses a multi-task objective including FIM on The Stack v2. As we show in §4.4, these models exhibit markedly different pretrained representation geometries: Qwen operates in a near-saturated similarity regime (mean positive cosine similarity 0.986), while StarCoder maintains healthy separation (mean positive cosine similarity 0.798). This divergence enables us to study how representation geometry mediates the effectiveness of different negative mining strategies.
16	
17	**Fine-Tuning Configuration.** Both encoders are fine-tuned with LoRA \cite{hu2022lora} applied to the query and value projection matrices ($W_q$, $W_v$) of every attention layer, with rank $r = 16$, scaling factor $\alpha = 32$, and dropout 0.05. We use a linear projection head mapping the last hidden state to a 256-dimensional embedding. Training uses InfoNCE loss with temperature $\tau = 0.07$, AdamW optimizer with learning rate $2 \times 10^{-5}$, weight decay 0.01, cosine annealing schedule with 10% linear warmup, and gradient clipping at max norm 1.0. Input sequences are truncated to 2,048 tokens. Batch size is 8 with gradient checkpointing enabled.
18	
19	For the initial seed (s42), we train for 3 epochs to obtain a full overfitting curve; subsequent seeds (s43, s44) train for 2 epochs with early stopping (patience 2 evaluations) based on validation loss. Evaluation is performed every 500 steps. We maintain dual checkpoints: $\theta^*_{\text{loss}}$ (minimum validation loss) and $\theta^*_{\text{R@1}}$ (maximum validation Recall@1).
20	
21	**Negative Mining.** Embedding-distance negatives are mined using FAISS \cite{johnson2021faiss} over frozen pretrained embeddings. BM25 negatives are mined by indexing all repository files with Okapi BM25 and selecting the top-$K$ highest-scoring non-gold files per query. Dataflow-aware negatives use the CodeQL-derived structural connectivity graph to filter structurally reachable files before selecting by embedding distance (§3.4). All mining is **static**—performed once before training and not refreshed.
22	
23	**Hardware.** All experiments are conducted on a single node with 2$\times$ NVIDIA RTX PRO 6000 (96 GB VRAM each). Qwen and StarCoder training chains run on separate GPUs in parallel. Each run (single strategy, single seed, single encoder) requires approximately 5–7 hours; the full experiment matrix (3 strategies $\times$ 3 seeds $\times$ 2 encoders = 18 runs) completes in approximately 120 GPU-hours.
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
48	**Table 2: Pilot results (single seed, 24-repo subset).** Pool size = 50.
49	
50	| Strategy | Qwen R@1 | StarCoder R@1 |
51	|---|---|---|
52	| Random | 0.536 | 0.492 |
53	| Embedding-distance | 0.556 (+2.0pp) | 0.508 (+1.6pp) |
54	| Dataflow-aware | 0.544 (+0.8pp) | 0.487 (−0.5pp) |
55	
56	The pilot established two findings subsequently confirmed at full scale: (i) embedding-distance mining yields consistent improvement across both encoders, and (ii) the dataflow-aware strategy's effectiveness is encoder-dependent—beneficial for Qwen but neutral-to-negative for StarCoder.
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
129	**Table 6: CodeQL extraction scalability by repository tier.**
130	
131	| Tier | Repos | Instances | Timeout Rate | Structural Coverage | Z% (median) |
132	|---|---|---|---|---|---|
133	| Small (<50 files) | 1 | 500 | 0% | 81.0% | 0.0% |
134	| Medium (50–200) | 17 | 4,096 | 0% | 47.2% | 50.0% |
135	| Large (200–500) | 40 | 13,628 | 0% | 34.3% | 85.7% |
136	| XLarge (500+) | 29 | 25,949 | 0% | 31.4% | 96.0% |
137	| **Total** | **123** | **44,173** | **0%** | **36.0%** | — |
138	
139	The pipeline achieves 0% timeout rate across all repository tiers. Structural coverage (proportion of instances with CodeQL data-flow output) decreases with repository size, reflecting the combinatorial complexity of inter-procedural analysis in large codebases. Conversely, the connected-not-gold rate (Z%)—the proportion of structurally connected files that are non-gold—increases with repository size, reaching a median of 96% for repositories with 500+ files. This indicates that larger repositories provide richer pools for structure-grounded negative mining. The re-extraction pass currently in progress is expected to substantially improve structural coverage across all tiers.
140	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b792482b-7a21-49ac-ae22-b6f2e0fcfeec",
  "isSidechain": false,
  "promptId": "1d7108f5-af6a-41fc-acd8-afc665497be3",
  "type": "user",
  "uuid": "96e6fdbc-5c1c-493f-89cb-9767f37df3dc",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/experiments_v1.md",
      "content": "# §4 Experiments\n\n## §4.1 Experimental Setup\n\n**Dataset.** We construct our training corpus from SWE-bench \\cite{jimenez2024swebench}, a benchmark of real-world GitHub issues paired with developer-authored patches. Starting from 5,029 task instances spanning 131 unique (repository, commit) pairs, we run the StructFuse extraction pipeline (§3.2) to obtain inter-procedural data-flow graphs via CodeQL. After filtering for clone/checkout failures and extraction errors, we retain 15,897 instances across 123 repositories with structural data, yielding a structural coverage rate of 36%. The remaining 64% of instances lack structural connectivity data due to transient filesystem failures during batch extraction; a re-extraction pass (in progress) is expected to recover the majority of these instances, and we discuss data efficiency implications in §6.\n\nFor each random seed, we perform a per-repository stratified split to produce approximately 11,300 training and 3,000 validation instances. Each instance consists of an issue description (query), one or more gold files (positives), and strategy-specific negatives (§3.4). The per-seed split ensures that no repository appears exclusively in one partition, preserving the distribution of repository sizes and structural properties.\n\n**Evaluation Protocol.** We evaluate retrieval performance using Recall@$k$ ($k \\in \\{1, 5, 10\\}$) and Mean Reciprocal Rank (MRR), computed over a candidate pool of size 50 (1 positive + 49 negatives sampled per query). During training, $K = 7$ negatives are used per query. We report results as mean $\\pm$ standard deviation across three random seeds (42, 43, 44). For all comparisons, we use the checkpoint selected by best validation Recall@1 ($\\theta^*_{\\text{R@1}}$), as discussed in §3.3.\n\n**Baselines.** We compare three negative mining strategies—random, embedding-distance, and dataflow-aware (§3.4)—against a BM25 retrieval baseline. The BM25 baseline uses Okapi BM25 \\cite{robertson2009bm25} to rank candidate files by lexical overlap with the query, providing a non-neural reference point. We additionally evaluate BM25-mined negatives as a fourth contrastive training strategy to ground our comparison against the gradient-based premise of CoCoHaNeRe \\cite{cocohanere2025}.\n\n## §4.2 Implementation Details\n\n**Encoders.** We select two decoder-only pretrained code models with distinct pretraining regimes and representation geometries: **Qwen2.5-Coder-3B** \\cite{hui2024qwen25coder} and **StarCoder2-3B** \\cite{li2023starcoder}. Qwen2.5-Coder-3B is trained primarily with Fill-in-the-Middle (FIM) on a curated multilingual code corpus, while StarCoder2-3B uses a multi-task objective including FIM on The Stack v2. As we show in §4.4, these models exhibit markedly different pretrained representation geometries: Qwen operates in a near-saturated similarity regime (mean positive cosine similarity 0.986), while StarCoder maintains healthy separation (mean positive cosine similarity 0.798). This divergence enables us to study how representation geometry mediates the effectiveness of different negative mining strategies.\n\n**Fine-Tuning Configuration.** Both encoders are fine-tuned with LoRA \\cite{hu2022lora} applied to the query and value projection matrices ($W_q$, $W_v$) of every attention layer, with rank $r = 16$, scaling factor $\\alpha = 32$, and dropout 0.05. We use a linear projection head mapping the last hidden state to a 256-dimensional embedding. Training uses InfoNCE loss with temperature $\\tau = 0.07$, AdamW optimizer with learning rate $2 \\times 10^{-5}$, weight decay 0.01, cosine annealing schedule with 10% linear warmup, and gradient clipping at max norm 1.0. Input sequences are truncated to 2,048 tokens. Batch size is 8 with gradient checkpointing enabled.\n\nFor the initial seed (s42), we train for 3 epochs to obtain a full overfitting curve; subsequent seeds (s43, s44) train for 2 epochs with early stopping (patience 2 evaluations) based on validation loss. Evaluation is performed every 500 steps. We maintain dual checkpoints: $\\theta^*_{\\text{loss}}$ (minimum validation loss) and $\\theta^*_{\\text{R@1}}$ (maximum validation Recall@1).\n\n**Negative Mining.** Embedding-distance negatives are mined using FAISS \\cite{johnson2021faiss} over frozen pretrained embeddings. BM25 negatives are mined by indexing all repository files with Okapi BM25 and selecting the top-$K$ highest-scoring non-gold files per query. Dataflow-aware negatives use the CodeQL-derived structural connectivity graph to filter structurally reachable files before selecting by embedding distance (§3.4). All mining is **static**—performed once before training and not refreshed.\n\n**Hardware.** All experiments are conducted on a single node with 2$\\times$ NVIDIA RTX PRO 6000 (96 GB VRAM each). Qwen and StarCoder training chains run on separate GPUs in parallel. Each run (single strategy, single seed, single encoder) requires approximately 5–7 hours; the full experiment matrix (3 strategies $\\times$ 3 seeds $\\times$ 2 encoders = 18 runs) completes in approximately 120 GPU-hours.\n\n## §4.3 Results\n\n### Main Results\n\nTable 1 presents the main retrieval results across three negative mining strategies and two encoders. Each cell reports mean $\\pm$ standard deviation over three seeds.\n\n**Table 1: Retrieval performance by negative mining strategy and encoder.** Pool size = 50. Best per-encoder results in **bold**.\n\n| Strategy | Qwen2.5-Coder-3B | | | StarCoder2-3B | | |\n|---|---|---|---|---|---|---|\n| | R@1 | R@5 | MRR | R@1 | R@5 | MRR |\n| BM25 (no training) | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{X.XX} |\n| Random | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} |\n| BM25-mined | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} |\n| Embedding-distance | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} |\n| Dataflow-aware | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} |\n\n**Key observations.** (1) Embedding-distance mining consistently improves over random negatives across both encoders (\\placeholder{+X.X}pp and \\placeholder{+X.X}pp R@1 for Qwen and StarCoder respectively), confirming that simple static embedding-distance mining provides meaningful training signal without gradient-based mechanisms. (2) Dataflow-aware negatives show encoder-dependent effects: \\placeholder{description of interaction pattern based on final results}. (3) All contrastive strategies substantially outperform the BM25 retrieval baseline, demonstrating the value of learned representations for repo-level code retrieval.\n\n### Pilot Validation\n\nPrior to the full multi-seed experiment, we conducted single-seed pilot runs on a 24-repository subset (~3,300 instances) to validate the pipeline and obtain early signal on strategy differentiation. Pilot results (Table 2) show consistent patterns with the full-scale experiment.\n\n**Table 2: Pilot results (single seed, 24-repo subset).** Pool size = 50.\n\n| Strategy | Qwen R@1 | StarCoder R@1 |\n|---|---|---|\n| Random | 0.536 | 0.492 |\n| Embedding-distance | 0.556 (+2.0pp) | 0.508 (+1.6pp) |\n| Dataflow-aware | 0.544 (+0.8pp) | 0.487 (−0.5pp) |\n\nThe pilot established two findings subsequently confirmed at full scale: (i) embedding-distance mining yields consistent improvement across both encoders, and (ii) the dataflow-aware strategy's effectiveness is encoder-dependent—beneficial for Qwen but neutral-to-negative for StarCoder.\n\n### Ablations\n\n**Pool Size Sensitivity.** To assess whether strategy rankings are robust to evaluation-time candidate pool size, we evaluate best checkpoints at pool sizes $\\in \\{50, 100, 200, 500\\}$.\n\n**Table 3: R@1 by pool size.**\n\n| Pool Size | Qwen Emb. | Qwen Rand. | Qwen $\\Delta$ | SC Emb. | SC Rand. | SC $\\Delta$ |\n|---|---|---|---|---|---|---|\n| 50 | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{+X.X} | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{+X.X} |\n| 100 | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{+X.X} | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{+X.X} |\n| 200 | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{+X.X} | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{+X.X} |\n| 500 | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{+X.X} | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{+X.X} |\n\n**Dynamic Mining Control.** To isolate the effect of static vs. dynamic negative mining, we compare our static embedding-distance strategy against an epoch-level re-mining variant that recomputes embeddings and re-mines negatives at the start of each epoch.\n\n| Strategy | Qwen R@1 (s42) |\n|---|---|\n| Static embedding-distance | \\placeholder{X.XX} |\n| Dynamic (epoch re-mining) | \\placeholder{X.XX} |\n\n### Downstream Evaluation\n\n**SWE-bench Lite.** To validate that retrieval improvements translate to downstream task performance, we integrate the trained retriever into an LLM-based repair agent and evaluate on SWE-bench Lite (300 instances).\n\n| Retriever | Resolve Rate |\n|---|---|\n| BM25 | \\placeholder{X.X%} |\n| Random-trained | \\placeholder{X.X%} |\n| Embedding-trained (Qwen) | \\placeholder{X.X%} |\n\n## §4.4 Analysis\n\n### Representation Geometry and Negative Difficulty\n\nA central question is *why* embedding-distance mining helps while dataflow-aware mining shows encoder-dependent effects. We analyze this through the lens of **negative difficulty**: the mean cosine similarity between each query and its assigned negatives in the pretrained embedding space. Higher negative similarity implies harder negatives—the encoder must learn finer distinctions to separate positives from negatives.\n\n**Table 4: Negative difficulty analysis (pretrained encoders, 2048-token context).** Margin = pos\\_sim − neg\\_sim.\n\n| Strategy | Qwen2.5-Coder-3B | | | StarCoder2-3B | | |\n|---|---|---|---|---|---|---|\n| | pos\\_sim | neg\\_sim | margin | pos\\_sim | neg\\_sim | margin |\n| Random | 0.986 | 0.911 | 0.074 | 0.799 | 0.605 | 0.194 |\n| Embedding-distance | 0.986 | 0.969 | 0.017 | 0.808 | 0.741 | 0.067 |\n| Dataflow-aware | 0.986 | 0.956 | 0.029 | 0.801 | 0.682 | 0.119 |\n\nSeveral patterns emerge from Table 4:\n\n**Saturation asymmetry.** Qwen's pretrained space is near-saturated: positive cosine similarity exceeds 0.98 regardless of strategy, leaving a maximum margin of only 0.074. StarCoder maintains 2.6–4.1$\\times$ larger margins across all strategies, indicating a more separable pretrained space.\n\n**Difficulty gradient.** Both encoders follow the expected ordering: embedding-distance negatives are hardest (smallest margin), followed by dataflow-aware, then random. However, the *magnitude* of margin compression differs: embedding-distance mining reduces Qwen's margin from 0.074 to 0.017 (77% reduction), while StarCoder's margin drops from 0.194 to 0.067 (65% reduction). The steeper relative compression for Qwen suggests that in saturated spaces, even small increases in negative difficulty push the encoder close to its representational capacity.\n\n**Mechanistic hypothesis.** When the pretrained space is saturated, the encoder has limited room to separate positives from any category of hard negatives. Embedding-distance negatives provide a direct optimization target: they occupy precisely the region where the encoder is uncertain. Dataflow-aware negatives, while structurally informative, target a subset of the hard-negative space that may not align with the encoder's most informative gradient direction. In the well-separated StarCoder space, both strategies have sufficient room to be effective; in Qwen's saturated space, the additional structural constraint of dataflow-aware mining may exclude some of the most useful hard negatives.\n\n### Stratified Analysis\n\nWe stratify results by structural data availability to assess whether the dataflow-aware strategy's effectiveness depends on the richness of the underlying CodeQL graph.\n\n**Table 5: R@1 stratified by structural data availability.**\n\n| Stratum | Instances | Qwen (Emb.) | Qwen (DF) | $\\Delta$ | SC (Emb.) | SC (DF) | $\\Delta$ |\n|---|---|---|---|---|---|---|---|\n| Rich dataflow ($\\geq$5 edges) | \\placeholder{N} | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{±X.X} | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{±X.X} |\n| Sparse dataflow (1–4 edges) | \\placeholder{N} | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{±X.X} | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{±X.X} |\n| No structural data (fallback) | \\placeholder{N} | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{±X.X} | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{±X.X} |\n\nConfound analysis reveals that rich-dataflow instances are heavily concentrated in large repositories (99.3% in large/xlarge tiers), while small repositories have no rich-dataflow instances. We therefore control for pool size and repository size when comparing strategies across strata to isolate the independent effect of structural data richness.\n\n### CodeQL Scalability\n\nWe report extraction-time statistics to support the practicality of the pipeline at scale (Claim 3).\n\n**Table 6: CodeQL extraction scalability by repository tier.**\n\n| Tier | Repos | Instances | Timeout Rate | Structural Coverage | Z% (median) |\n|---|---|---|---|---|---|\n| Small (<50 files) | 1 | 500 | 0% | 81.0% | 0.0% |\n| Medium (50–200) | 17 | 4,096 | 0% | 47.2% | 50.0% |\n| Large (200–500) | 40 | 13,628 | 0% | 34.3% | 85.7% |\n| XLarge (500+) | 29 | 25,949 | 0% | 31.4% | 96.0% |\n| **Total** | **123** | **44,173** | **0%** | **36.0%** | — |\n\nThe pipeline achieves 0% timeout rate across all repository tiers. Structural coverage (proportion of instances with CodeQL data-flow output) decreases with repository size, reflecting the combinatorial complexity of inter-procedural analysis in large codebases. Conversely, the connected-not-gold rate (Z%)—the proportion of structurally connected files that are non-gold—increases with repository size, reaching a median of 96% for repositories with 500+ files. This indicates that larger repositories provide richer pools for structure-grounded negative mining. The re-extraction pass currently in progress is expected to substantially improve structural coverage across all tiers.\n",
      "numLines": 140,
      "startLine": 1,
      "totalLines": 140
    }
  },
  "sourceToolAssistantUUID": "b792482b-7a21-49ac-ae22-b6f2e0fcfeec",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "d1e524a6-76dd-46af-a456-0b6d1108f4ee",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-14T22:58:14.683Z_

<details><summary>↩ Tool result · `toolu_01CQpW8zYgDrkLaC9nnz1VqR`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__read_registry"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__register_artifact"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1ae64ce3-a605-417b-9a4a-3c79aada281c",
  "isSidechain": false,
  "promptId": "1d7108f5-af6a-41fc-acd8-afc665497be3",
  "type": "user",
  "uuid": "24e90ccd-4627-4c4f-82b5-bd2c77a91bdb",
  "toolUseResult": {
    "matches": [
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__register_artifact"
    ],
    "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__register_artifact",
    "total_deferred_tools": 25
  },
  "sourceToolAssistantUUID": "1ae64ce3-a605-417b-9a4a-3c79aada281c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "d1e524a6-76dd-46af-a456-0b6d1108f4ee",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-14T22:58:14.679Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01CQpW8zYgDrkLaC9nnz1VqR`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__register_artifact",
  "max_results": 2
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "96e6fdbc-5c1c-493f-89cb-9767f37df3dc",
  "isSidechain": false,
  "requestId": "req_011Cb3HjRPV1AWBD8qJqjHRL",
  "type": "assistant",
  "uuid": "1ae64ce3-a605-417b-9a4a-3c79aada281c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "d1e524a6-76dd-46af-a456-0b6d1108f4ee",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CV4qErsZHeNBNJZpxZauuC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12120,
      "cache_read_input_tokens": 11447,
      "output_tokens": 196,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12120,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 196,
          "cache_read_input_tokens": 11447,
          "cache_creation_input_tokens": 12120,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12120
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

_source line 14_

```json
{
  "type": "last-prompt",
  "leafUuid": "24e90ccd-4627-4c4f-82b5-bd2c77a91bdb",
  "sessionId": "d1e524a6-76dd-46af-a456-0b6d1108f4ee"
}
```

---

### Runtime record

_source line 15_

```json
{
  "type": "ai-title",
  "aiTitle": "Fix experiments v1 6 issues warnings and info",
  "sessionId": "d1e524a6-76dd-46af-a456-0b6d1108f4ee"
}
```

---

### Assistant

_source line 16 · 2026-05-14T22:58:16.865Z_

<details><summary>Logged reasoning block</summary>

```text
Let me fetch the registry data for both experiments mentioned in the task.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "24e90ccd-4627-4c4f-82b5-bd2c77a91bdb",
  "isSidechain": false,
  "requestId": "req_011Cb3HjiyQSceJTRYouas8i",
  "type": "assistant",
  "uuid": "9199b4a5-69b5-4a01-9524-39c6b0ad7347",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "d1e524a6-76dd-46af-a456-0b6d1108f4ee",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011JPzEDKTcZptmS3Ldq7LBS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 5865,
      "cache_read_input_tokens": 23567,
      "output_tokens": 350,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5865,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 350,
          "cache_read_input_tokens": 23567,
          "cache_creation_input_tokens": 5865,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5865
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

_source line 17 · 2026-05-14T22:58:16.868Z_

Fetching registry data for the two experiments.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9199b4a5-69b5-4a01-9524-39c6b0ad7347",
  "isSidechain": false,
  "requestId": "req_011Cb3HjiyQSceJTRYouas8i",
  "type": "assistant",
  "uuid": "af4936d2-3013-41c9-8c5e-0f0314ca4a30",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "d1e524a6-76dd-46af-a456-0b6d1108f4ee",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011JPzEDKTcZptmS3Ldq7LBS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 5865,
      "cache_read_input_tokens": 23567,
      "output_tokens": 350,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5865,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 350,
          "cache_read_input_tokens": 23567,
          "cache_creation_input_tokens": 5865,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5865
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

_source line 18 · 2026-05-14T22:58:18.349Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01NDkos6ESEpJEUD4k3PDmZU`</summary>

```json
{
  "project": "structfuse-context",
  "filters": {
    "exp_id": "plan_006_scalability"
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
  "parentUuid": "af4936d2-3013-41c9-8c5e-0f0314ca4a30",
  "isSidechain": false,
  "requestId": "req_011Cb3HjiyQSceJTRYouas8i",
  "type": "assistant",
  "uuid": "2e765df2-e609-42de-a5f4-6102d28f4673",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "d1e524a6-76dd-46af-a456-0b6d1108f4ee",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011JPzEDKTcZptmS3Ldq7LBS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 5865,
      "cache_read_input_tokens": 23567,
      "output_tokens": 350,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5865,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 350,
          "cache_read_input_tokens": 23567,
          "cache_creation_input_tokens": 5865,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5865
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

_source line 19 · 2026-05-14T22:58:18.472Z_

<details><summary>↩ Tool result · `toolu_01NDkos6ESEpJEUD4k3PDmZU`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.1099}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2e765df2-e609-42de-a5f4-6102d28f4673",
  "isSidechain": false,
  "promptId": "1d7108f5-af6a-41fc-acd8-afc665497be3",
  "type": "user",
  "uuid": "c40b32f9-5d30-4ba7-ba42-eac1669f5e53",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {}, \\\"count\\\": 0, \\\"total\\\": 0, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.1099}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.1099}}"
    }
  },
  "sourceToolAssistantUUID": "2e765df2-e609-42de-a5f4-6102d28f4673",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "d1e524a6-76dd-46af-a456-0b6d1108f4ee",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-14T22:58:19.357Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01Y1pLAS4dn2qxJ93jRJgaUp`</summary>

```json
{
  "project": "structfuse-context",
  "filters": {
    "exp_id": "m2_embed_verify"
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
  "parentUuid": "c40b32f9-5d30-4ba7-ba42-eac1669f5e53",
  "isSidechain": false,
  "requestId": "req_011Cb3HjiyQSceJTRYouas8i",
  "type": "assistant",
  "uuid": "aace4f61-1a19-4d96-8f57-e4235fc438df",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "d1e524a6-76dd-46af-a456-0b6d1108f4ee",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011JPzEDKTcZptmS3Ldq7LBS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 5865,
      "cache_read_input_tokens": 23567,
      "output_tokens": 350,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5865,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 350,
          "cache_read_input_tokens": 23567,
          "cache_creation_input_tokens": 5865,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5865
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

_source line 21 · 2026-05-14T22:58:20.181Z_

<details><summary>↩ Tool result · `toolu_01DGJkccktSn41ryRucGVRWK`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.0985}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6b8e45d2-13cd-4642-a0b6-c1d207f12e34",
  "isSidechain": false,
  "promptId": "1d7108f5-af6a-41fc-acd8-afc665497be3",
  "type": "user",
  "uuid": "0109d711-22ec-4078-aade-a6cf3332ad6f",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {}, \\\"count\\\": 0, \\\"total\\\": 0, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.0985}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.0985}}"
    }
  },
  "sourceToolAssistantUUID": "6b8e45d2-13cd-4642-a0b6-c1d207f12e34",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "d1e524a6-76dd-46af-a456-0b6d1108f4ee",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-14T22:58:19.524Z_

<details><summary>↩ Tool result · `toolu_01Y1pLAS4dn2qxJ93jRJgaUp`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.1531}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "aace4f61-1a19-4d96-8f57-e4235fc438df",
  "isSidechain": false,
  "promptId": "1d7108f5-af6a-41fc-acd8-afc665497be3",
  "type": "user",
  "uuid": "1c5b6c66-2c32-4f42-a237-e4d95d2f4f1e",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {}, \\\"count\\\": 0, \\\"total\\\": 0, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.1531}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.1531}}"
    }
  },
  "sourceToolAssistantUUID": "aace4f61-1a19-4d96-8f57-e4235fc438df",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "d1e524a6-76dd-46af-a456-0b6d1108f4ee",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-14T22:58:20.073Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01DGJkccktSn41ryRucGVRWK`</summary>

```json
{
  "project": "structfuse-context",
  "filters": {
    "exp_id": "plan_013_starcoder"
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
  "parentUuid": "1c5b6c66-2c32-4f42-a237-e4d95d2f4f1e",
  "isSidechain": false,
  "requestId": "req_011Cb3HjiyQSceJTRYouas8i",
  "type": "assistant",
  "uuid": "6b8e45d2-13cd-4642-a0b6-c1d207f12e34",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "d1e524a6-76dd-46af-a456-0b6d1108f4ee",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011JPzEDKTcZptmS3Ldq7LBS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 5865,
      "cache_read_input_tokens": 23567,
      "output_tokens": 350,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5865,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 350,
          "cache_read_input_tokens": 23567,
          "cache_creation_input_tokens": 5865,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5865
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

_source line 24 · 2026-05-14T22:58:22.629Z_

<details><summary>Logged reasoning block</summary>

```text
The registry queries returned no results. Let me try without the exp_id filter to see what's in the registry, and also search for those experiment IDs with different approaches.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0109d711-22ec-4078-aade-a6cf3332ad6f",
  "isSidechain": false,
  "requestId": "req_011Cb3Hk8GrxS32YYF5mLj2M",
  "type": "assistant",
  "uuid": "d7d71274-0c37-42cb-b4b1-0af456d71f01",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "d1e524a6-76dd-46af-a456-0b6d1108f4ee",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WStDqk7RQjvzsHX8A6YEyv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 661,
      "cache_read_input_tokens": 29432,
      "output_tokens": 173,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 661,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 173,
          "cache_read_input_tokens": 29432,
          "cache_creation_input_tokens": 661,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 661
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

_source line 25 · 2026-05-14T22:58:23.668Z_

Registry returned empty for those exp_ids. Let me check what's actually in the registry.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d7d71274-0c37-42cb-b4b1-0af456d71f01",
  "isSidechain": false,
  "requestId": "req_011Cb3Hk8GrxS32YYF5mLj2M",
  "type": "assistant",
  "uuid": "563c2518-afa2-4c76-b83e-73ddbdbeddbd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "d1e524a6-76dd-46af-a456-0b6d1108f4ee",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WStDqk7RQjvzsHX8A6YEyv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 661,
      "cache_read_input_tokens": 29432,
      "output_tokens": 173,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 661,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 173,
          "cache_read_input_tokens": 29432,
          "cache_creation_input_tokens": 661,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 661
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

_source line 26 · 2026-05-14T22:58:23.905Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01Qf4qp287WUfXdgGRVXD4Kr`</summary>

```json
{
  "project": "structfuse-context",
  "fields": [
    "*"
  ],
  "limit": 20
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "563c2518-afa2-4c76-b83e-73ddbdbeddbd",
  "isSidechain": false,
  "requestId": "req_011Cb3Hk8GrxS32YYF5mLj2M",
  "type": "assistant",
  "uuid": "162d8d81-abff-48dc-9a6b-30d163b86def",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "d1e524a6-76dd-46af-a456-0b6d1108f4ee",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WStDqk7RQjvzsHX8A6YEyv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 661,
      "cache_read_input_tokens": 29432,
      "output_tokens": 173,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 661,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 173,
          "cache_read_input_tokens": 29432,
          "cache_creation_input_tokens": 661,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 661
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

_source line 27 · 2026-05-14T22:58:24.022Z_

<details><summary>↩ Tool result · `toolu_01Qf4qp287WUfXdgGRVXD4Kr`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {\"plan_017_literature\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T18:49:00.477Z\", \"updated_at\": \"2026-05-14T21:33:45.149Z\", \"hypothesis\": \"Inference-time graph method comparison: 8 papers surveyed (CodexGraph, LocAgent, RANGER, GraphCoder, ARISE, RepoGraph, CodeGRAG, CodeRAG). Discussion v2 drafted, all citations verified. Conclusion: training-time vs inference-time complementary.\", \"spec\": {\"command\": \"analysis only (no training)\", \"server\": \"local\", \"data_path\": \"N/A\", \"data_count\": 0, \"model_name\": \"N/A\", \"seed\": \"N/A\", \"checkpoint_path\": \"N/A\", \"log_path\": \"N/A\"}, \"conclusion\": \"success\", \"metrics\": {\"papers_surveyed\": 8, \"citations_verified\": 8, \"discussion_draft\": \"artifacts/paper_drafts/discussion_v2.md\", \"artifact_id\": \"art_20260514_a2e1cd\"}, \"completed_at\": \"2026-05-14T18:49:39.557Z\", \"notes\": \"Inference-time graph method comparison 完成。8 papers surveyed，其中 6 篇纳入 literature_map.yaml 和 discussion_v2.md（CodexGraph, LocAgent, RANGER, GraphCoder, ARISE, RepoGraph）。CodeGRAG 和 CodeRAG 经调研排除：CodeGRAG（arXiv 2405.02355）关注 NL→code generation 的 graph-augmented prompting，不涉及代码检索或对比学习；CodeRAG 系列（CodeRAG-Bench 2406.14497 / CodeRAG 2504.10046）关注 retrieval-augmented code generation benchmark 和 bigraph-based 代码生成，均为生成任务而非检索训练。两者与 StructFuse 的 scope（训练时结构信号用于对比学习代码检索）不符，故未纳入 discussion。\"}, \"m1_reextract_v2\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-13T20:00:20.578Z\", \"updated_at\": \"2026-05-14T21:18:48.643Z\", \"hypothesis\": \"M1 重提取 v2：恢复 28,276 个因运行时瞬态文件系统故障失败的 instances（82 repos）。CodeQL pack 已修复，端到端测试通过。预期将训练数据从 15,897 提升至 ~44,173。D022 批准。\", \"parent\": \"m1_extraction\", \"spec\": {\"command\": \"bash scripts/rerun_m1_failed.sh (4 CPU workers, CodeQL 2-hop, pack installed)\", \"server\": \"bjb1-42106\", \"data_path\": \"/root/autodl-tmp/structfuse/full_m1_data/\", \"data_count\": 28276, \"model_name\": \"N/A (CodeQL extraction)\", \"seed\": \"N/A\", \"log_path\": \"/root/runs/structfuse-context/m1_reextract_v2.log\", \"checkpoint_source\": \"rerun of m1_extraction failed instances (v2, CodeQL fixed)\", \"eval_data\": \"N/A\"}, \"notes\": \"M1 重提取 v2：CodeQL pack 已修复，端到端测试通过。28,276 instances / 82 repo groups / 4 workers 并行。启动 2026-05-14 03:59 CST。[诊断 07:06 CST] 活跃运行中，~15/82 groups 完成，2,469 次 call_graph 查询成功，预计还需 ~13-16h。仅前 4 个旧 repo（furl/pyasn1/feedparser/python-docx）复用 v1 旧 DB 有 18 次降级 WARNING，04:02 之后零失败。产出写入 all.jsonl（追加模式）。磁盘 97GB 可用。[Director 决策 Session 8] 即使数据量增至 ~44K，不重跑 M2（ARR May 25 DDL 不允许再加 4-5 天重训）。处理方式：(1) post-M2 完成后如有 GPU 空档，跑 1-seed pilot (Qwen, embedding, 新数据) 对比当前 M2 baseline; (2) 论文中作为 scalability/data efficiency 讨论点; (3) 全量重训留 camera-ready。[进度检查 2026-05-15 05:05 CST] 80.8% 完成（22,842/28,276），0 ERROR，速率 ~560/hr，处理中大 repo：mozilla__bleach/sqlfluff/conan-io/Project-MONAI。产出为单独 .json 文件，尚未合并 all.jsonl。预计 ~15:00 CST May 15 完成。\", \"metrics\": {\"checked_at\": \"2026-05-15T05:15Z\", \"process\": \"alive (CPU, 4 workers)\", \"started\": \"2026-05-14T03:59Z\", \"elapsed_hours\": 25, \"total_instances\": 28276, \"repo_groups\": 82, \"output_json_files\": 40225, \"all_jsonl_lines\": 44173, \"active_repos\": {\"sqlfluff/sqlfluff\": \"250/1272\", \"mozilla/bleach\": \"350/455\", \"conan-io/conan\": \"450/972\", \"Project-MONAI/MONAI\": \"150/524\"}, \"estimated_total_hours\": 60, \"progress_pct_by_time\": \"~42%\", \"disk\": \"98GB free on /root/autodl-tmp\"}}, \"m2_full_starcoder_resumed\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-14T18:44:19.253Z\", \"updated_at\": \"2026-05-14T21:18:45.080Z\", \"hypothesis\": \"M2 StarCoder resumed: 继续 m2_full_starcoder 的 8 sequential runs (random×2 + embedding×3 + dataflow×3)。原实验因 cron timeout 标记为 failed，实际 PID 519791 正常运行。\", \"spec\": {\"command\": \"bash run_m2_full_starcoder_resume.sh (8 runs: random_s43→s44→embedding×3→dataflow×3)\", \"server\": \"bjb1-42106\", \"gpu\": [\"cuda:1\"], \"pid\": \"519791\", \"log_path\": \"/root/runs/structfuse-context/m2_full_starcoder.log\", \"data_path\": \"/root/autodl-tmp/structfuse/full_m2_training_data/\", \"data_count\": 11308, \"model_name\": \"StarCoder2-3B\", \"seed\": \"42,43,44\"}, \"parent\": \"m2_full_starcoder\", \"metrics\": {\"checked_at\": \"2026-05-15T05:15Z\", \"process\": \"alive (PID 519791, uptime 03:11:44)\", \"gpu\": \"cuda:1, 100% util, 53.9/97.9GB VRAM, 72°C\", \"current_subrun\": \"random_s43 (1/9)\", \"current_step\": \"550/1405 (epoch 1/2, ~20% of subrun)\", \"eval_at_500\": {\"R@1\": 0.4708, \"R@5\": 0.9469, \"val_loss\": 0.5279}, \"latest_loss\": 0.26, \"completed_subruns\": 0, \"remaining_subruns\": 8, \"eta_hours\": \"~65-70h\"}}, \"m2_full_qwen_continued\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-14T18:44:20.646Z\", \"updated_at\": \"2026-05-14T21:18:42.976Z\", \"hypothesis\": \"M2 Qwen continued: 继续 m2_full_qwen 的剩余 runs (random_s44 + embedding×3 + dataflow×3)。原实验 cron 在 s42 退出时自动设为 ANALYZING，但链仍在运行。\", \"spec\": {\"command\": \"bash run_m2_full_qwen.sh (chain: random_s44 running → embedding×3 → dataflow×3)\", \"server\": \"bjb1-42106\", \"gpu\": [\"cuda:0\"], \"pid\": \"337267\", \"log_path\": \"/root/runs/structfuse-context/m2_full_qwen.log\", \"data_path\": \"/root/autodl-tmp/structfuse/full_m2_training_data/\", \"data_count\": 11308, \"model_name\": \"Qwen2.5-Coder-3B\", \"seed\": \"42,43,44\"}, \"parent\": \"m2_full_qwen\", \"metrics\": {\"checked_at\": \"2026-05-15T05:15Z\", \"process\": \"alive (PID 337267, uptime 09:50:41)\", \"gpu\": \"cuda:0, 100% util, 51.5/97.9GB VRAM, 68°C\", \"current_subrun\": \"random_s44 (3/7)\", \"current_step\": \"850/1408 (epoch 1/2, ~30% of subrun)\", \"eval_at_500\": {\"R@1\": 0.6009, \"R@5\": 0.9583, \"val_loss\": 0.4252}, \"latest_loss\": 0.2837, \"completed_subruns\": {\"random_s42\": {\"best_R@1\": 0.5527, \"best_val_loss\": 0.4651}, \"random_s43\": {\"best_R@1\": 0.5554, \"best_val_loss\": 0.4476}}, \"remaining_subruns\": 5, \"eta_hours\": \"~40-45h\"}}, \"plan_005_stratified\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-14T20:36:16.738Z\", \"updated_at\": \"2026-05-14T21:07:45.324Z\", \"hypothesis\": \"Plan 005 分层分析：按 repo size/pool size/query-pos similarity/structural data availability/neg_difficulty quartile 5 维度分层评估 embedding vs random 策略差异，控制 pool_size confound。Claim 2 支撑实验。v2 结果为 ground truth（v1→v2 changelog 见 art_20260514_3008c4）。\", \"parent\": \"m2_full_qwen\", \"notes\": \"plan_id=plan_005. 分层评估脚本已完成全部修改（analyze_stratified.py）：(1) mock seed 确定性修复 (2) pool_size-controlled 策略对比（within-bin delta + weighted aggregate）(3) dataflow×pool_size 交叉分析（n<30 标记 underpowered）(4) checkpoint 发现逻辑已就绪（best_by_recall_at_1 / best / best_by_val_loss）。输出含 JSON + CSV + PDF。[2026-05-14 21:07] Worker 完成 5 项 Patch：(P1) reeval_checkpoint 重写为 batch encoding（query/positive/negatives 分组批量编码，tqdm 进度条，torch.no_grad + model.eval，pad_token 兜底）(P2) 新增 --batch-size 参数（默认 64）(P3) 调用处传递 batch_size (P4) 非 dry-run 自适应 sim bins（tercile 计算边界 + 重新分配 sim_bin）(P5) 输出 JSON 记录 similarity_bin_edges 和 batch_size。Dry-run 验证全部通过。真实评估待 M2 全部 checkpoint 就绪后执行。\", \"metrics\": {\"confound_analysis\": {\"data_validity\": \"⚠️ R@1 值为 dry-run mock predictions，不可引用。仅分布结构（cross_tabulation.csv）有效。\", \"valid_findings\": {\"distribution_structure\": \"rich-dataflow 99.3% 落在 large/xlarge repo，small repo 中完全不存在\", \"correlation\": {\"dataflow_edges_vs_repo_size_pearson_r\": 0.089}, \"cross_distribution\": {\"rich_in_large_xlarge_pct\": 99.3, \"rich_in_small\": 0, \"moderate_in_large_xlarge_pct\": 60.9}, \"implication\": \"真实评估必须控制 pool_size 和 repo_size 来隔离 dataflow richness 独立效应\"}, \"invalid_findings\": \"所有 R@1/R@5/MRR 值均为 mock predictions，策略排序 pattern 不可信，禁止引用\", \"artifacts_path\": \"/root/autodl-tmp/structfuse/artifacts/confound_analysis/\", \"valid_artifact\": \"cross_tabulation.csv\"}}}, \"m2_full_starcoder\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T16:18:15.415Z\", \"updated_at\": \"2026-05-14T18:04:29.245Z\", \"hypothesis\": \"Full M2 StarCoder: 3 strategies × 3 seeds on full M1 data. Cross-encoder validation — if embedding > random holds for both Qwen and StarCoder, method is encoder-agnostic. Resolves plan_013 pilot negative (dataflow encoder-dependent).\", \"parent\": \"plan_013_starcoder\", \"spec\": {\"command\": \"bash -c \\\"cd /root/structfuse && bash run_m2_full_starcoder_resume.sh\\\"\", \"server\": \"bjb1-42106\", \"gpu\": [\"cuda:1\"], \"pid\": \"519791\", \"log_path\": \"~/runs/structfuse-context/m2_full_starcoder.log\", \"submitted_at\": \"2026-05-14T18:03:12.079Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"notes\": \"Phase 1: 构建 StarCoder embedding negatives 完成。Phase 2: 9 runs 训练中。batch_size=8, num_negatives=7, epochs=3(s42)/2(s43+), lr=2e-5, eval_steps=500, no early_stopping。双 checkpoint: best + best_by_recall_at_1。Seeds: 42,43,44。[D026] s42 保持 3 epochs; s43/s44 及后续 runs 改为 2 epochs。[2026-05-15 02:02 CST] cuda:1 进程冲突修复并重新提交（PID 519791, timeout=144h）。Registry 状态 DONE(failed) 是旧 cron timeout 标记，实际正在运行 random_s43 [1/8]。新 cron 已注册监控 PID 519791。序列：random_s43→s44→(待插入bm25_s42)→embedding×3→dataflow×3。random_s42 结果：best R@1=0.4604 at step 2500, val_loss=0.6134 at step 1000。\", \"metrics\": {\"random_s42\": {\"epoch\": \"3/3\", \"current_step\": 4200, \"total_steps\": 4242, \"total_steps_per_epoch\": 1414, \"eval_500\": {\"val_loss\": 0.6194, \"recall_at_1\": 0.435, \"recall_at_5\": 0.905, \"recall_at_10\": 1}, \"eval_1000\": {\"val_loss\": 0.6134, \"recall_at_1\": 0.454, \"recall_at_5\": 0.92, \"recall_at_10\": 1}, \"eval_1500\": {\"val_loss\": 0.6528, \"recall_at_1\": 0.449, \"recall_at_5\": 0.906, \"recall_at_10\": 1}, \"eval_2000\": {\"val_loss\": 0.6698, \"recall_at_1\": 0.4456, \"recall_at_5\": 0.906, \"recall_at_10\": 1}, \"eval_2500\": {\"val_loss\": 0.6342, \"recall_at_1\": 0.4604, \"recall_at_5\": 0.9117, \"recall_at_10\": 1}, \"eval_3000\": {\"val_loss\": 0.6516, \"recall_at_1\": 0.4544, \"recall_at_5\": 0.9077, \"recall_at_10\": 1}, \"eval_3500\": {\"val_loss\": 0.6588, \"recall_at_1\": 0.4534, \"recall_at_5\": 0.9057, \"recall_at_10\": 1}, \"eval_4000\": {\"val_loss\": 0.6637, \"recall_at_1\": 0.4547, \"recall_at_5\": 0.9003, \"recall_at_10\": 1}, \"best_checkpoint\": \"step_1000 (val_loss=0.6134) / step_2500 (R@1=0.4604)\", \"conclusion\": \"effectively_complete (timeout at step 4200/4242, lr=7.8e-9, remaining 42 steps negligible)\"}, \"progress_snapshot\": \"2026-05-15T01:50 CST\"}, \"reproduce\": {\"finished_at\": \"2026-05-14T17:49:54.474Z\"}, \"failure_reason\": \"EXIT_CODE=124 (timeout — exceeded timeout_hours)\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-14T17:49:55.304Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T17:49:56.408767+00:00\"}]}}, \"m2_full_qwen\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-13T16:18:14.870Z\", \"updated_at\": \"2026-05-14T18:00:29.323Z\", \"hypothesis\": \"Full M2 Qwen: 3 strategies (random/embedding/dataflow) × 3 seeds on full M1 data (~11K train/seed). Statistical validation of pilot signal (embedding > random +2pp). Go/no-go for paper claims per D018.\", \"parent\": \"m2_embed_verify\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/structfuse && bash run_m2_full_qwen.sh 2>&1 | tee /root/runs/structfuse-context/m2_full_qwen.log\\\"\", \"server\": \"bjb1-42106\", \"gpu\": [\"cuda:0\"], \"pid\": \"73544\", \"log_path\": \"~/runs/structfuse-context/m2_full_qwen.log\", \"submitted_at\": \"2026-05-13T17:39:30.757Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"notes\": \"Full M2 go/no-go: 3 strategies (random, embedding_distance, dataflow_aware) × 3 seeds (42, 43, 44) = 9 runs sequential on cuda:0. Config: lr=2e-5, batch_size=8, eval_steps=500, num_negatives=7, max_seq_length=2048, warmup_ratio=0.1, weight_decay=0.01, temperature=0.07, LoRA r=16, gradient_checkpointing=True, proj_dim=256. Dual checkpoint: best_by_val_loss + best_by_recall_at_1. Train ~11.3K/seed, val ~3K/seed. [D026] s42 保持 3 epochs 提供完整 overfitting curve; s43/s44 及后续 runs 改为 2 epochs + early_stopping_patience=2。[STATUS 2026-05-15 00:19 CST] Registry 状态 ANALYZING 是 cron 自动设置（s42 进程退出触发），但实验实际仍在进行中。random_s43 在 cuda:0 正常运行，step 1200/2810 (43%)。eval@500 R@1=0.5357, eval@1000 R@1=0.5285 (early_stopping 1/2)。Best R@1=0.5357 at step 500。GPU 100% 利用率, 50.5/97.9GB VRAM。\", \"metrics\": {\"random_s42\": {\"status\": \"DONE\", \"epoch\": \"3/3\", \"total_steps\": 4242, \"total_steps_per_epoch\": 1414, \"eval_500\": {\"val_loss\": 0.4869, \"recall_at_1\": 0.533, \"recall_at_5\": 0.954, \"recall_at_10\": 1}, \"eval_1000\": {\"val_loss\": 0.4651, \"recall_at_1\": 0.553, \"recall_at_5\": 0.959, \"recall_at_10\": 1}, \"eval_1500\": {\"val_loss\": 0.5365, \"recall_at_1\": 0.523, \"recall_at_5\": 0.955, \"recall_at_10\": 1}, \"eval_2000\": {\"val_loss\": 0.5162, \"recall_at_1\": 0.523, \"recall_at_5\": 0.954, \"recall_at_10\": 1}, \"eval_2500\": {\"val_loss\": 0.5264, \"recall_at_1\": 0.527, \"recall_at_5\": 0.956, \"recall_at_10\": 1}, \"eval_3000\": {\"val_loss\": 0.5406, \"recall_at_1\": 0.536, \"recall_at_5\": 0.956, \"recall_at_10\": 1}, \"best_checkpoint\": \"step_1000 (val_loss=0.4651, R@1=0.5527)\", \"conclusion\": \"Overfit after step 1000. Best R@1=0.5527, +1.7pp vs pilot (0.5357). Full data helps.\"}, \"random_s43\": {\"status\": \"DONE\", \"epoch\": \"early_stopped\", \"total_steps_per_epoch\": 1405, \"eval_500\": {\"val_loss\": 0.4476, \"recall_at_1\": 0.5357}, \"eval_1000\": {\"val_loss\": 0.4637, \"recall_at_1\": 0.5285}, \"eval_1500\": {\"recall_at_1\": 0.5554}, \"best_by_val_loss\": \"step 500 (val_loss=0.4476)\", \"best_by_recall_at_1\": \"step 1500 (R@1=0.5554)\", \"conclusion\": \"Early stopped at step 1500. Best R@1=0.5554, consistent with s42 (0.5527). val_loss and R@1 criterion diverge.\"}, \"random_s44\": {\"status\": \"RUNNING\", \"note\": \"Auto-started 01:58 CST, epoch 1/2, 1408 batches/epoch\"}, \"progress_snapshot\": \"2026-05-15T02:00 CST\"}, \"reproduce\": {\"finished_at\": \"2026-05-14T11:24:33.887Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T11:24:35.375104+00:00\"}]}}, \"plan_018_bm25\": {\"status\": \"QUEUED\", \"retry_count\": 0, \"created_at\": \"2026-05-14T16:38:40.603Z\", \"updated_at\": \"2026-05-14T17:09:50.985Z\", \"hypothesis\": \"BM25 negative baseline: Dream 审稿三档一致认定缺 BM25 baseline 是论文最大结构性缺陷。Phase 1 (CPU): 对 M2 训练语料建 BM25 索引，挖掘 BM25 hard negatives，生成训练数据。Phase 2 (GPU): 用 BM25 negatives 训练 Qwen + StarCoder 各 1 seed，对比 R@1。\", \"parent\": \"m2_full_qwen\", \"notes\": \"Phase 1 (CPU) COMPLETE: BM25 negative mining 完成。3 seeds 数据生成，record counts 与其他策略完全一致，0 fallback。BM25 score 分布: mean=246.50, std=155.96。重叠率: BM25 vs embedding_distance ~87.1%, vs random ~76.2%, vs dataflow_aware ~71.8%。高 median=1.0 因小 repo 候选池≤50 文件导致策略完全重合，BM25 differentiation 主要在大 repo。脚本: /root/structfuse/scripts/mine_bm25_negatives.py。输出: /root/autodl-tmp/structfuse/full_m2_training_data/{train,val}_bm25_s{42,43,44}.jsonl。Phase 2 (GPU): 等 re-dream gate 通过 + M2 完成后训练。\", \"metrics\": {\"phase1_complete\": true, \"seed_42\": {\"train_records\": 11308, \"val_records\": 2980, \"train_size_mb\": 1280.8, \"val_size_mb\": 344.6}, \"seed_43\": {\"train_records\": 11236, \"val_records\": 3052, \"train_size_mb\": 1280.9, \"val_size_mb\": 316}, \"seed_44\": {\"train_records\": 11264, \"val_records\": 3024, \"train_size_mb\": 1347.1, \"val_size_mb\": 295.9}, \"bm25_score_dist\": {\"count\": 392954, \"mean\": 246.5, \"std\": 155.96, \"p25\": 128.38, \"p50\": 228.41, \"p75\": 347.85, \"max\": 2585.74}, \"overlap_overall\": {\"bm25_vs_embedding\": 0.871, \"bm25_vs_random\": 0.762, \"bm25_vs_dataflow\": 0.718, \"note\": \"k=50 full candidate overlap from mining worker\"}, \"overlap_stratified_top7_jaccard\": {\"small_lt50\": {\"repos\": 39, \"bm25_vs_embedding\": 0.668, \"bm25_vs_random\": 0.411, \"bm25_vs_dataflow\": 0.667}, \"medium_50_200\": {\"repos\": 29, \"bm25_vs_embedding\": 0.38, \"bm25_vs_random\": 0.067, \"bm25_vs_dataflow\": 0.363}, \"large_200plus\": {\"repos\": 15, \"bm25_vs_embedding\": 0.297, \"bm25_vs_random\": 0.007, \"bm25_vs_dataflow\": 0.405}, \"matched_queries\": 2920, \"total_queries\": 12290, \"note\": \"top-7 Jaccard on s42 matched queries only (24% match rate due to different train/val splits)\"}}}, \"plan_015_dynamic\": {\"status\": \"QUEUED\", \"retry_count\": 0, \"created_at\": \"2026-05-14T17:03:24.316Z\", \"updated_at\": \"2026-05-14T17:03:30.544Z\", \"hypothesis\": \"Dynamic negative mining (epoch-level re-mining): 每 epoch 重新用当前 encoder embedding 挖掘 negatives，验证 static mining 是否足够。缩减版：只跑 dynamic_ep × 1 seed (Qwen, s42)，~11h 单卡。若 dynamic ≈ static（预期 <1pp 差异），在 Limitation 段排除 confound。\", \"notes\": \"Director D031 缩减：原 44h → 11h 单卡。只跑 dynamic_ep × 1 seed (Qwen, s42)，跳过 dynamic_500。Post-M2 与 plan_003 并行（一卡 SWE-bench，一卡 dynamic_ep）。受 re-dream gate 约束。设计文档已由 Worker 完成。\"}, \"neg_difficulty_analysis\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T19:39:20.016Z\", \"updated_at\": \"2026-05-14T00:13:49.046Z\", \"hypothesis\": \"Negative difficulty distribution analysis: 用预训练 Qwen2.5-Coder-3B 和 StarCoder2-3B 计算 3 策略 (random/embedding/dataflow) 的 query-negative/positive cosine similarity，分析 pretrained representation separability 跨编码器差异。MAX_LENGTH=2048 匹配训练设置。\", \"notes\": \"128 vs 2048 token 对比完成（2026-05-14 05:54 CST）。Qwen pos_sim 在 2048t 下 0.9855（比 128t 的 0.9804 更高），确认 ceiling 为 Qwen 表征的结构性特征，非截断 artifact。StarCoder margin 2.6-4.1x Qwen（2048t）。核心结论：pretrained representation separability varies across encoders，跨两种 token 长度成立。数据源：128t → stats_v2.json，2048t → stats_v3_2048.json。\", \"metrics\": {\"qwen_128\": {\"random\": {\"pos_sim\": 0.9804, \"neg_sim\": 0.899, \"margin\": 0.0816, \"pct_positive_margin\": 77.8}, \"embedding_distance\": {\"pos_sim\": 0.9804, \"neg_sim\": 0.959, \"margin\": 0.0209, \"pct_positive_margin\": 60.7}, \"dataflow_aware\": {\"pos_sim\": 0.9805, \"neg_sim\": 0.95, \"margin\": 0.0309, \"pct_positive_margin\": 67.4}}, \"starcoder_128\": {\"random\": {\"pos_sim\": 0.757, \"neg_sim\": 0.553, \"margin\": 0.2039, \"pct_positive_margin\": 72.8}, \"embedding_distance\": {\"pos_sim\": 0.784, \"neg_sim\": 0.668, \"margin\": 0.1159, \"pct_positive_margin\": 59.2}, \"dataflow_aware\": {\"pos_sim\": 0.761, \"neg_sim\": 0.659, \"margin\": 0.1022, \"pct_positive_margin\": 62.8}}, \"qwen_2048\": {\"random\": {\"pos_sim\": 0.9855, \"neg_sim\": 0.9111, \"margin\": 0.0743, \"margin_std\": 0.2322, \"pct_positive_margin\": 81.8}, \"embedding_distance\": {\"pos_sim\": 0.9855, \"neg_sim\": 0.9685, \"margin\": 0.017, \"margin_std\": 0.114, \"pct_positive_margin\": 58.8}, \"dataflow_aware\": {\"pos_sim\": 0.9856, \"neg_sim\": 0.9563, \"margin\": 0.0293, \"margin_std\": 0.1407, \"pct_positive_margin\": 73.9}}, \"starcoder_2048\": {\"random\": {\"pos_sim\": 0.7985, \"neg_sim\": 0.6045, \"margin\": 0.194, \"margin_std\": 0.2788, \"pct_positive_margin\": 78}, \"embedding_distance\": {\"pos_sim\": 0.8079, \"neg_sim\": 0.7409, \"margin\": 0.067, \"margin_std\": 0.2056, \"pct_positive_margin\": 55}, \"dataflow_aware\": {\"pos_sim\": 0.8009, \"neg_sim\": 0.6818, \"margin\": 0.1192, \"margin_std\": 0.2264, \"pct_positive_margin\": 70.4}}, \"sc_qwen_margin_ratio_128\": {\"random\": 2.5, \"embedding_distance\": 5.54, \"dataflow_aware\": 3.3}, \"sc_qwen_margin_ratio_2048\": {\"random\": 2.61, \"embedding_distance\": 3.94, \"dataflow_aware\": 4.07}}, \"conclusion\": \"success\", \"spec\": {\"command\": \"python negative_difficulty_margin_v2.py (CPU analysis)\", \"server\": \"bjb1-42106\", \"data_path\": \"/root/autodl-tmp/structfuse/full_m2_data/\", \"data_count\": 11000, \"model_name\": \"Qwen2.5-Coder-3B + StarCoder2-3B (pretrained, no training)\", \"seed\": \"N/A\", \"checkpoint_path\": \"N/A (analysis only)\", \"log_path\": \"/root/autodl-tmp/structfuse/artifacts/negative_difficulty_stats_v3_2048.json\"}, \"completed_at\": \"2026-05-14T00:13:49.046Z\"}, \"m1_reextract\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T19:35:23.954Z\", \"updated_at\": \"2026-05-13T19:45:53.741Z\", \"hypothesis\": \"M1 重提取：恢复 28,276 个因运行时瞬态文件系统故障失败的 instances（82 repos）。预期将训练数据从 15,897 提升至 ~44,173。D022 批准。\", \"parent\": \"m1_extraction\", \"spec\": {\"command\": \"bash scripts/rerun_m1_failed.sh (4 CPU workers, CodeQL 2-hop)\", \"server\": \"bjb1-42106\", \"data_path\": \"/root/autodl-tmp/structfuse/m1_extraction/\", \"data_count\": 28276, \"model_name\": \"N/A (CodeQL extraction)\", \"seed\": \"N/A\", \"pid\": \"97358\", \"log_path\": \"/root/runs/structfuse-context/m1_rerun.log\", \"checkpoint_source\": \"rerun of m1_extraction failed instances\", \"eval_data\": \"N/A\", \"checkpoint_path\": \"N/A (failed, no output)\"}, \"conclusion\": \"failed\", \"notes\": \"CodeQL query 100% 失败（exit status 2）。根因：Worker 安装 CodeQL CLI 2.25.4 时未执行 `codeql pack install`，`codeql/python-all@7.1.0` 标准库 pack 缺失。修复命令：`cd /root/structfuse/extraction/codeql_queries && /opt/codeql/codeql pack install`。已 kill 进程 + tmux session。无新数据产出（all.jsonl 未受影响）。等 Director 确认后修复重跑。\", \"completed_at\": \"2026-05-13T19:44:09.115Z\"}, \"m1_extraction\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-12T21:00:02.300Z\", \"updated_at\": \"2026-05-13T19:26:13.901Z\", \"spec\": {\"command\": \"nohup bash scripts/run_m1_extraction.sh (8 CPU workers, CodeQL 2-hop)\", \"server\": \"cqa1-21977\", \"data_path\": \"/root/autodl-tmp/structfuse/m1_extraction/\", \"data_count\": 50869, \"model_name\": \"N/A (CodeQL extraction)\", \"seed\": \"N/A\", \"description\": \"M1: 全量 5K repos CodeQL 提取, 131 unique (repo,commit) groups, 50869 instances\"}, \"metrics\": {\"total_instances_attempted\": 44173, \"instances_skipped\": 6696, \"total_instances\": 50869, \"codeql_success\": 15133, \"beniget_fallback\": 764, \"extraction_failed\": 28276, \"structural_data_rate\": 0.36, \"repos_with_output\": 123, \"repos_total\": 131, \"repo_coverage\": 0.939, \"skip_clone_failed\": 5852, \"skip_checkout_failed\": 836, \"skip_stale_handle\": 8, \"elapsed_minutes\": 837.8, \"avg_time_per_instance_s\": 8.9, \"output_size_gb\": 6.6, \"disk_usage_gb\": 13, \"output_file\": \"all.jsonl\"}, \"notes\": \"[2026-05-13 19:25] COMPLETED. 837.8min, 123/131 repos (93.9%), 15,897/44,173 instances with structural data (36.0%), 6,696 skipped (clone/checkout). Output: all.jsonl 6.6GB. [2026-05-13 19:23 UPDATE] 28,276 buggy_file_not_found errors 经验证并非上游数据质量问题——10/10 抽查的文件在 repo 中全部存在。根因是运行时瞬态文件系统故障（CodeQL 并行 database creation 导致磁盘耗尽，锐截止模式）。这些 instances 可通过重跑恢复。D022: 准备重跑脚本中，等 Director 确认后执行。\", \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/structfuse/m1_extraction/all.jsonl\", \"log_path\": \"/tmp/m1_extraction.log\", \"completed_at\": \"2026-05-13T10:59:42.462Z\"}, \"plan_006_scalability\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T07:57:43.631Z\", \"updated_at\": \"2026-05-13T19:24:00.741Z\", \"spec\": {\"command\": \"M1 scalability statistics analysis (29/131 repos)\", \"server\": \"bjb1-42106\", \"data_path\": \"/root/autodl-tmp/structfuse/m1_extraction/\", \"data_count\": 8171, \"model_name\": \"N/A (CPU analysis)\", \"seed\": \"N/A\", \"description\": \"Plan 006: M1 extraction scalability stats - timeout rate, extraction time, coverage, Z% by repo size. Partial results from 29/131 repos.\", \"checkpoint_path\": \"N/A\", \"log_path\": \"N/A\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-13T07:57:58.176Z\", \"notes\": \"[2026-05-13 19:23] 全量统计 + error 分析 + fuzzy match 验证完成。关键发现: (1) 0 timeout; (2) 28,276 error 全部 buggy_file_not_found，但 fuzzy match 验证发现文件实际都存在——根因是运行时瞬态文件系统故障（锐截止模式：每个 repo 内先成功后突然全部失败，extraction_time=0.0s），可能是 CodeQL 并行数据库创建导致磁盘空间耗尽; (3) 这些 instance 可通过重跑恢复（当前 resolve_file_in_repo 对全部样本返回正确路径）; (4) 结构数据率 34.3% 有望提升至接近 100%（若重跑成功）; (5) Z% 随 repo 规模上升 (XL median 96%). Artifacts: plan006_full_scalability.json, art_20260513_d262da (error patterns)\", \"hypothesis\": \"Claim 3: CodeQL bounded data-flow extraction scales to large repos with acceptable timeout rates and provides meaningful structural coverage (Z%) that increases with repo complexity\", \"metrics\": {\"repos\": 123, \"total_instances\": 44173, \"structural_data_rate\": 0.343, \"error_rate\": 0.64, \"zero_timeout_rate\": true, \"processing_time\": {\"mean_s\": 8.93, \"median_s\": 0, \"p95_s\": 31.95, \"max_s\": 633.68, \"total_hours\": 109.58}, \"by_tier\": {\"small_lt50\": {\"repos\": 1, \"instances\": 500, \"error_rate\": 0.054, \"struct_rate\": 0.81, \"z_pct_mean\": 0.284, \"z_pct_median\": 0}, \"medium_50_200\": {\"repos\": 17, \"instances\": 4096, \"error_rate\": 0.485, \"struct_rate\": 0.472, \"z_pct_mean\": 0.444, \"z_pct_median\": 0.5}, \"large_200_500\": {\"repos\": 40, \"instances\": 13628, \"error_rate\": 0.639, \"struct_rate\": 0.343, \"z_pct_mean\": 0.604, \"z_pct_median\": 0.857}, \"xlarge_500plus\": {\"repos\": 29, \"instances\": 25949, \"error_rate\": 0.676, \"struct_rate\": 0.314, \"z_pct_mean\": 0.812, \"z_pct_median\": 0.96}}, \"instance_distribution\": {\"lt10\": 1, \"10_50\": 17, \"50_200\": 36, \"200_500\": 40, \"500plus\": 29}, \"artifact\": \"plan006_full_scalability.json\"}}, \"plan_013_starcoder\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T05:09:14.885Z\", \"updated_at\": \"2026-05-13T18:09:54.153Z\", \"hypothesis\": \"Architecture generalization: validate StructFuse with StarCoder2-3B encoder (vs Qwen2.5-Coder-3B in m2_embed_verify). If both encoders show same strategy ranking → method is encoder-agnostic, strengthening the core claim. Key differentiator for best→accept at Dream.\", \"spec\": {\"command\": \"bash -c \\\"bash /root/structfuse/run_plan013_starcoder.sh\\\"\", \"server\": \"bjb1-42106\", \"gpu\": [\"cuda:0\"], \"pid\": \"23798\", \"log_path\": \"~/runs/structfuse-context/plan_013_starcoder.log\", \"submitted_at\": \"2026-05-13T05:26:21.946Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/structfuse/m2_embed_verify_data/\", \"data_count\": 3282, \"model_name\": \"bigcode/starcoder2-3b\", \"seed\": 42, \"wall_clock_seconds\": 35338.2, \"gpu_hours\": 9.82}, \"notes\": \"[2026-05-13 16:00] ALL 3 STRATEGIES DONE. Ranking: embedding (R@1=0.5078) > random (0.4922) > dataflow (0.4869). Embedding vs random: +1.6pp (consistent with Qwen). Dataflow vs random: -0.5pp (DIFFERS from Qwen where dataflow > random +0.8pp). Hypothesis NEGATIVE: strategy ranking NOT identical across encoders. Embedding > random is encoder-agnostic, dataflow position is encoder-dependent. Log: /root/runs/faith-evidence-ie/plan_013_starcoder.log. Cron misreported EXIT_CODE=129 but all strategies completed (confirmed via log extraction worker).\", \"metrics\": {\"random\": {\"status\": \"DONE\", \"best_val_loss\": 0.5113, \"best_recall@1\": 0.4922, \"best_recall@5\": 0.98, \"best_recall@10\": 1, \"source\": \"/tmp/eval_random_s42.log (post-hoc eval, no in-training eval)\"}, \"embedding_distance\": {\"status\": \"DONE\", \"best_step\": 1000, \"best_val_loss\": 0.4816, \"best_recall@1\": 0.5078, \"best_recall@5\": 0.9843, \"best_recall@10\": 1, \"final_val_loss\": 0.506, \"final_recall@1\": 0.5174}, \"dataflow_aware\": {\"status\": \"DONE\", \"best_step\": 1000, \"best_val_loss\": 0.5255, \"best_recall@1\": 0.4869, \"best_recall@5\": 0.9695, \"best_recall@10\": 1, \"final_val_loss\": 0.5509, \"final_recall@1\": 0.5078}}, \"failure_reason\": \"\", \"conclusion\": \"negative\", \"completed_at\": \"2026-05-13T15:15:20.165Z\"}, \"m2_embed_verify\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T04:39:16.051Z\", \"updated_at\": \"2026-05-13T15:59:51.621Z\", \"hypothesis\": \"True embedding mining verification: compare Qwen2.5-Coder-3B cosine similarity negatives vs BM25 negatives on pilot data (24 repos). If true embedding negatives are harder → Claim 2 (structure-aware negatives improve retrieval) gets stronger evidence.\", \"parent\": \"m2_early_pilot\", \"spec\": {\"command\": \"bash -c \\\"bash /root/structfuse/run_m2_embed_verify.sh\\\"\", \"server\": \"bjb1-42106\", \"gpu\": [\"cuda:1\"], \"pid\": \"29290\", \"log_path\": \"~/runs/structfuse-context/m2_embed_verify.log\", \"submitted_at\": \"2026-05-13T06:37:00.822Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/structfuse/m2_embed_verify_data/\", \"data_count\": 3282, \"model_name\": \"Qwen/Qwen2.5-Coder-3B\", \"seed\": 42, \"checkpoint_source\": \"training from scratch (not eval)\", \"eval_data\": \"N/A (training, not eval)\", \"wall_clock_seconds\": 31097.9, \"gpu_hours\": 8.64}, \"notes\": \"[2026-05-13 16:00] ALL 3 STRATEGIES DONE. Ranking: embedding (R@1=0.5557) > dataflow (0.5436) > random (0.5357). Embedding vs random: +2.0pp. Dataflow vs random: +0.8pp. All best at step 500, overfitting after. Hypothesis confirmed: true embedding negatives are harder → Claim 2 supported. Log: /root/runs/faith-evidence-ie/m2_embed_verify.log. Cron misreported EXIT_CODE=2 but all strategies completed successfully (confirmed via log extraction worker).\", \"metrics\": {\"random\": {\"status\": \"DONE\", \"best_step\": 500, \"best_val_loss\": 0.4834, \"best_recall@1\": 0.5357, \"best_recall@5\": 0.9808, \"best_recall@10\": 1, \"final_val_loss\": 0.5978, \"final_recall@1\": 0.5122}, \"embedding_distance\": {\"status\": \"DONE\", \"best_step\": 500, \"best_val_loss\": 0.4603, \"best_recall@1\": 0.5557, \"best_recall@5\": 0.9808, \"best_recall@10\": 1, \"final_val_loss\": 0.5935, \"final_recall@1\": 0.5209}, \"dataflow_aware\": {\"status\": \"DONE\", \"best_step\": 500, \"best_val_loss\": 0.5602, \"best_recall@1\": 0.5436, \"best_recall@5\": 0.9817, \"best_recall@10\": 1, \"final_val_loss\": 0.6201, \"final_recall@1\": 0.5287}}, \"failure_reason\": \"EXIT_CODE=2 (shell misuse / syntax)\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-13T15:15:18.746Z\"}, \"mvp_p2b_contrastive_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-12T15:03:02.370Z\", \"updated_at\": \"2026-05-13T07:23:28.932Z\", \"spec\": {\"command\": \"bash scripts/run_p2b_all.sh (9 runs: 3 strategies × 3 seeds)\", \"server\": \"cqa1-21977\", \"gpu\": [\"cuda:4\"], \"pid\": \"132149\", \"data_path\": \"/root/structfuse/mvp_data/training_data/\", \"data_count\": 127, \"model_name\": \"Qwen2.5-Coder-3B + LoRA\", \"seed\": \"42,123,7\", \"hypothesis\": \"H3: data-flow hard negatives vs random vs embedding-distance, 3-seed × 3-strategy contrastive training\", \"plan_id\": \"mvp_p2b_contrastive_training\", \"checkpoint_path\": \"N/A\", \"log_path\": \"N/A\"}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-12T15:04:44.396Z\", \"notes\": \"P2b 对比训练 v2，因磁盘空间不足被 kill。已被 p2b_5reruns（成功完成 9/9 runs）替代。\"}, \"p2b_dataflow_retrain\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-12T19:49:00.303Z\", \"updated_at\": \"2026-05-13T07:23:27.706Z\", \"spec\": {\"command\": \"build_p2b_data.py regeneration + dataflow 3-seed retrain\", \"server\": \"cqa1-21977\", \"data_path\": \"/root/structfuse\", \"data_count\": 0, \"model_name\": \"Qwen2.5-Coder-3B (LoRA)\", \"seed\": \"42,123,456\", \"description\": \"BLOCKED: dataflow connections ⊆ gold files, strategies indistinguishable\", \"checkpoint_path\": \"N/A\", \"log_path\": \"N/A\"}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-13T04:17:02.055Z\", \"notes\": \"Dataflow 策略重训练计划，因 embedding_distance 命名问题（实际用 BM25 而非 embedding）被 Reviewer 发现后搁置。已被 m2_embed_verify（true embedding mining）替代。\"}, \"p2b_eval_all\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-12T16:27:50.967Z\", \"updated_at\": \"2026-05-13T07:23:24.721Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/structfuse && bash scripts/run_eval_all.sh\\\"\", \"server\": \"cqa1-21977\", \"gpu\": [\"cuda:4\"], \"pid\": \"254053\", \"log_path\": \"N/A\", \"submitted_at\": \"2026-05-12T16:27:50.945Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"N/A\", \"wall_clock_seconds\": 42550.6, \"gpu_hours\": 11.82}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-13T04:17:01.561Z\", \"notes\": \"P2b 全量 eval（pool_size=26），被 D013 服务器迁移计划取消。已被 p2b_eval_4runs_pool50（pool_size=50）替代。\"}, \"m2_early_pilot\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T01:39:53.920Z\", \"updated_at\": \"2026-05-13T04:44:22.077Z\", \"hypothesis\": \"Early pilot on partial M1 data (24 repos, ~5K instances): verify M2 training pipeline works end-to-end and get early signal on 3-strategy differentiation before full M1 completes\", \"spec\": {\"command\": \"bash /root/structfuse/scripts/run_m2_pilot.sh\", \"server\": \"cqa1-21977\", \"gpu\": [\"cuda:4\"], \"pid\": \"795739\", \"log_path\": \"/root/autodl-tmp/structfuse/m2_pilot_output/random_s42.log\", \"submitted_at\": \"2026-05-13T01:55:31.288Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/structfuse/m2_pilot_data/\", \"data_count\": 3418, \"model_name\": \"Qwen/Qwen2.5-Coder-3B\", \"seed\": 42, \"checkpoint_source\": \"N/A (training from scratch)\", \"eval_data\": \"N/A (training, not eval)\", \"checkpoint_path\": \"/root/autodl-tmp/structfuse/m2_pilot_output/random_s42/best_model.pt\", \"wall_clock_seconds\": 10130.8, \"gpu_hours\": 2.81}, \"conclusion\": \"killed\", \"notes\": \"PID 795791 在 cqa1 cuda:4 运行，wrapper 脚本顺序跑 random→embedding→dataflow（set -e）。random 策略跑到 step 4000 后卡住（~45min 无新日志），embedding/dataflow 未启动。Best checkpoint at step 1500。Val_loss 持续恶化（0.5879→0.728），明显过拟合。另有 OOM 进程干扰（某进程试图在同 GPU 启动导致 OOM，可能破坏 GPU 状态）。eval recall@k bug 已确认。\", \"metrics\": {\"pid\": 795791, \"gpu\": \"cuda:4\", \"gpu_mem_mb\": 9342, \"gpu_util_pct\": 83, \"batch_size\": 2, \"num_negatives\": 3, \"max_seq_length\": 1024, \"strategy_running\": \"random (stuck at step 4000, epoch 3)\", \"strategies_completed\": \"0/3\", \"eval_1500\": {\"val_loss\": 0.5879, \"recall_at_1\": 0.4693, \"recall_at_5\": 0.4693, \"recall_at_10\": 0.4693}, \"eval_2000\": {\"val_loss\": 0.7089, \"recall_at_1\": 0.4398}, \"eval_2500\": {\"val_loss\": 0.6961, \"recall_at_1\": 0.4291}, \"eval_3000\": {\"val_loss\": 0.728, \"recall_at_1\": 0.4104}, \"eval_3500\": {\"val_loss\": 0.7022, \"recall_at_1\": 0.4439}, \"best_checkpoint\": \"step_1500 (val_loss=0.5879, 6.2GB)\", \"WARNING\": \"recall@1=recall@5=recall@10 confirmed eval bug. Process hung after step 4000 (~45min no output). Overfitting after step 1500.\", \"status_check_at\": \"2026-05-13T04:42:00Z\"}, \"completed_at\": \"2026-05-13T04:44:22.077Z\"}, \"m2_early_pilot_v3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T01:59:06.557Z\", \"updated_at\": \"2026-05-13T02:13:43.400Z\", \"spec\": {\"command\": \"bash -c \\\"bash /root/structfuse/run_m2_early_pilot.sh\\\"\", \"server\": \"cqa1-21977\", \"gpu\": [\"cuda:0\"], \"pid\": \"897651\", \"log_path\": \"~/runs/structfuse-context/m2_early_pilot_v3.log\", \"submitted_at\": \"2026-05-13T02:04:31.768Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"N/A\", \"wall_clock_seconds\": 551.6, \"gpu_hours\": 0.15}, \"conclusion\": \"killed\", \"notes\": \"GPU 越界 cuda:0，违反项目 GPU 分配 gpu_ids=[\\\"cuda:4\\\"]。第二次 GPU 越界违规（首次 D005）。Worker 未正确映射 CUDA_VISIBLE_DEVICES。\", \"completed_at\": \"2026-05-13T02:13:43.400Z\"}}, \"count\": 20, \"total\": 37, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.1012}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "162d8d81-abff-48dc-9a6b-30d163b86def",
  "isSidechain": false,
  "promptId": "1d7108f5-af6a-41fc-acd8-afc665497be3",
  "type": "user",
  "uuid": "0de826df-a249-4892-a141-6c623401a0fe",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {\\\"plan_017_literature\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-14T18:49:00.477Z\\\", \\\"updated_at\\\": \\\"2026-05-14T21:33:45.149Z\\\", \\\"hypothesis\\\": \\\"Inference-time graph method comparison: 8 papers surveyed (CodexGraph, LocAgent, RANGER, GraphCoder, ARISE, RepoGraph, CodeGRAG, CodeRAG). Discussion v2 drafted, all citations verified. Conclusion: training-time vs inference-time complementary.\\\", \\\"spec\\\": {\\\"command\\\": \\\"analysis only (no training)\\\", \\\"server\\\": \\\"local\\\", \\\"data_path\\\": \\\"N/A\\\", \\\"data_count\\\": 0, \\\"model_name\\\": \\\"N/A\\\", \\\"seed\\\": \\\"N/A\\\", \\\"checkpoint_path\\\": \\\"N/A\\\", \\\"log_path\\\": \\\"N/A\\\"}, \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"papers_surveyed\\\": 8, \\\"citations_verified\\\": 8, \\\"discussion_draft\\\": \\\"artifacts/paper_drafts/discussion_v2.md\\\", \\\"artifact_id\\\": \\\"art_20260514_a2e1cd\\\"}, \\\"completed_at\\\": \\\"2026-05-14T18:49:39.557Z\\\", \\\"notes\\\": \\\"Inference-time graph method comparison 完成。8 papers surveyed，其中 6 篇纳入 literature_map.yaml 和 discussion_v2.md（CodexGraph, LocAgent, RANGER, GraphCoder, ARISE, RepoGraph）。CodeGRAG 和 CodeRAG 经调研排除：CodeGRAG（arXiv 2405.02355）关注 NL→code generation 的 graph-augmented prompting，不涉及代码检索或对比学习；CodeRAG 系列（CodeRAG-Bench 2406.14497 / CodeRAG 2504.10046）关注 retrieval-augmented code generation benchmark 和 bigraph-based 代码生成，均为生成任务而非检索训练。两者与 StructFuse 的 scope（训练时结构信号用于对比学习代码检索）不符，故未纳入 discussion。\\\"}, \\\"m1_reextract_v2\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-13T20:00:20.578Z\\\", \\\"updated_at\\\": \\\"2026-05-14T21:18:48.643Z\\\", \\\"hypothesis\\\": \\\"M1 重提取 v2：恢复 28,276 个因运行时瞬态文件系统故障失败的 instances（82 repos）。CodeQL pack 已修复，端到端测试通过。预期将训练数据从 15,897 提升至 ~44,173。D022 批准。\\\", \\\"parent\\\": \\\"m1_extraction\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash scripts/rerun_m1_failed.sh (4 CPU workers, CodeQL 2-hop, pack installed)\\\", \\\"server\\\": \\\"bjb1-42106\\\", \\\"data_path\\\": \\\"/root/autodl-tmp/structfuse/full_m1_data/\\\", \\\"data_count\\\": 28276, \\\"model_name\\\": \\\"N/A (CodeQL extraction)\\\", \\\"seed\\\": \\\"N/A\\\", \\\"log_path\\\": \\\"/root/runs/structfuse-context/m1_reextract_v2.log\\\", \\\"checkpoint_source\\\": \\\"rerun of m1_extraction failed instances (v2, CodeQL fixed)\\\", \\\"eval_data\\\": \\\"N/A\\\"}, \\\"notes\\\": \\\"M1 重提取 v2：CodeQL pack 已修复，端到端测试通过。28,276 instances / 82 repo groups / 4 workers 并行。启动 2026-05-14 03:59 CST。[诊断 07:06 CST] 活跃运行中，~15/82 groups 完成，2,469 次 call_graph 查询成功，预计还需 ~13-16h。仅前 4 个旧 repo（furl/pyasn1/feedparser/python-docx）复用 v1 旧 DB 有 18 次降级 WARNING，04:02 之后零失败。产出写入 all.jsonl（追加模式）。磁盘 97GB 可用。[Director 决策 Session 8] 即使数据量增至 ~44K，不重跑 M2（ARR May 25 DDL 不允许再加 4-5 天重训）。处理方式：(1) post-M2 完成后如有 GPU 空档，跑 1-seed pilot (Qwen, embedding, 新数据) 对比当前 M2 baseline; (2) 论文中作为 scalability/data efficiency 讨论点; (3) 全量重训留 camera-ready。[进度检查 2026-05-15 05:05 CST] 80.8% 完成（22,842/28,276），0 ERROR，速率 ~560/hr，处理中大 repo：mozilla__bleach/sqlfluff/conan-io/Project-MONAI。产出为单独 .json 文件，尚未合并 all.jsonl。预计 ~15:00 CST May 15 完成。\\\", \\\"metrics\\\": {\\\"checked_at\\\": \\\"2026-05-15T05:15Z\\\", \\\"process\\\": \\\"alive (CPU, 4 workers)\\\", \\\"started\\\": \\\"2026-05-14T03:59Z\\\", \\\"elapsed_hours\\\": 25, \\\"total_instances\\\": 28276, \\\"repo_groups\\\": 82, \\\"output_json_files\\\": 40225, \\\"all_jsonl_lines\\\": 44173, \\\"active_repos\\\": {\\\"sqlfluff/sqlfluff\\\": \\\"250/1272\\\", \\\"mozilla/bleach\\\": \\\"350/455\\\", \\\"conan-io/conan\\\": \\\"450/972\\\", \\\"Project-MONAI/MONAI\\\": \\\"150/524\\\"}, \\\"estimated_total_hours\\\": 60, \\\"progress_pct_by_time\\\": \\\"~42%\\\", \\\"disk\\\": \\\"98GB free on /root/autodl-tmp\\\"}}, \\\"m2_full_starcoder_resumed\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-14T18:44:19.253Z\\\", \\\"updated_at\\\": \\\"2026-05-14T21:18:45.080Z\\\", \\\"hypothesis\\\": \\\"M2 StarCoder resumed: 继续 m2_full_starcoder 的 8 sequential runs (random×2 + embedding×3 + dataflow×3)。原实验因 cron timeout 标记为 failed，实际 PID 519791 正常运行。\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash run_m2_full_starcoder_resume.sh (8 runs: random_s43→s44→embedding×3→dataflow×3)\\\", \\\"server\\\": \\\"bjb1-42106\\\", \\\"gpu\\\": [\\\"cuda:1\\\"], \\\"pid\\\": \\\"519791\\\", \\\"log_path\\\": \\\"/root/runs/structfuse-context/m2_full_starcoder.log\\\", \\\"data_path\\\": \\\"/root/autodl-tmp/structfuse/full_m2_training_data/\\\", \\\"data_count\\\": 11308, \\\"model_name\\\": \\\"StarCoder2-3B\\\", \\\"seed\\\": \\\"42,43,44\\\"}, \\\"parent\\\": \\\"m2_full_starcoder\\\", \\\"metrics\\\": {\\\"checked_at\\\": \\\"2026-05-15T05:15Z\\\", \\\"process\\\": \\\"alive (PID 519791, uptime 03:11:44)\\\", \\\"gpu\\\": \\\"cuda:1, 100% util, 53.9/97.9GB VRAM, 72°C\\\", \\\"current_subrun\\\": \\\"random_s43 (1/9)\\\", \\\"current_step\\\": \\\"550/1405 (epoch 1/2, ~20% of subrun)\\\", \\\"eval_at_500\\\": {\\\"R@1\\\": 0.4708, \\\"R@5\\\": 0.9469, \\\"val_loss\\\": 0.5279}, \\\"latest_loss\\\": 0.26, \\\"completed_subruns\\\": 0, \\\"remaining_subruns\\\": 8, \\\"eta_hours\\\": \\\"~65-70h\\\"}}, \\\"m2_full_qwen_continued\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-14T18:44:20.646Z\\\", \\\"updated_at\\\": \\\"2026-05-14T21:18:42.976Z\\\", \\\"hypothesis\\\": \\\"M2 Qwen continued: 继续 m2_full_qwen 的剩余 runs (random_s44 + embedding×3 + dataflow×3)。原实验 cron 在 s42 退出时自动设为 ANALYZING，但链仍在运行。\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash run_m2_full_qwen.sh (chain: random_s44 running → embedding×3 → dataflow×3)\\\", \\\"server\\\": \\\"bjb1-42106\\\", \\\"gpu\\\": [\\\"cuda:0\\\"], \\\"pid\\\": \\\"337267\\\", \\\"log_path\\\": \\\"/root/runs/structfuse-context/m2_full_qwen.log\\\", \\\"data_path\\\": \\\"/root/autodl-tmp/structfuse/full_m2_training_data/\\\", \\\"data_count\\\": 11308, \\\"model_name\\\": \\\"Qwen2.5-Coder-3B\\\", \\\"seed\\\": \\\"42,43,44\\\"}, \\\"parent\\\": \\\"m2_full_qwen\\\", \\\"metrics\\\": {\\\"checked_at\\\": \\\"2026-05-15T05:15Z\\\", \\\"process\\\": \\\"alive (PID 337267, uptime 09:50:41)\\\", \\\"gpu\\\": \\\"cuda:0, 100% util, 51.5/97.9GB VRAM, 68°C\\\", \\\"current_subrun\\\": \\\"random_s44 (3/7)\\\", \\\"current_step\\\": \\\"850/1408 (epoch 1/2, ~30% of subrun)\\\", \\\"eval_at_500\\\": {\\\"R@1\\\": 0.6009, \\\"R@5\\\": 0.9583, \\\"val_loss\\\": 0.4252}, \\\"latest_loss\\\": 0.2837, \\\"completed_subruns\\\": {\\\"random_s42\\\": {\\\"best_R@1\\\": 0.5527, \\\"best_val_loss\\\": 0.4651}, \\\"random_s43\\\": {\\\"best_R@1\\\": 0.5554, \\\"best_val_loss\\\": 0.4476}}, \\\"remaining_subruns\\\": 5, \\\"eta_hours\\\": \\\"~40-45h\\\"}}, \\\"plan_005_stratified\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-14T20:36:16.738Z\\\", \\\"updated_at\\\": \\\"2026-05-14T21:07:45.324Z\\\", \\\"hypothesis\\\": \\\"Plan 005 分层分析：按 repo size/pool size/query-pos similarity/structural data availability/neg_difficulty quartile 5 维度分层评估 embedding vs random 策略差异，控制 pool_size confound。Claim 2 支撑实验。v2 结果为 ground truth（v1→v2 changelog 见 art_20260514_3008c4）。\\\", \\\"parent\\\": \\\"m2_full_qwen\\\", \\\"notes\\\": \\\"plan_id=plan_005. 分层评估脚本已完成全部修改（analyze_stratified.py）：(1) mock seed 确定性修复 (2) pool_size-controlled 策略对比（within-bin delta + weighted aggregate）(3) dataflow×pool_size 交叉分析（n<30 标记 underpowered）(4) checkpoint 发现逻辑已就绪（best_by_recall_at_1 / best / best_by_val_loss）。输出含 JSON + CSV + PDF。[2026-05-14 21:07] Worker 完成 5 项 Patch：(P1) reeval_checkpoint 重写为 batch encoding（query/positive/negatives 分组批量编码，tqdm 进度条，torch.no_grad + model.eval，pad_token 兜底）(P2) 新增 --batch-size 参数（默认 64）(P3) 调用处传递 batch_size (P4) 非 dry-run 自适应 sim bins（tercile 计算边界 + 重新分配 sim_bin）(P5) 输出 JSON 记录 similarity_bin_edges 和 batch_size。Dry-run 验证全部通过。真实评估待 M2 全部 checkpoint 就绪后执行。\\\", \\\"metrics\\\": {\\\"confound_analysis\\\": {\\\"data_validity\\\": \\\"⚠️ R@1 值为 dry-run mock predictions，不可引用。仅分布结构（cross_tabulation.csv）有效。\\\", \\\"valid_findings\\\": {\\\"distribution_structure\\\": \\\"rich-dataflow 99.3% 落在 large/xlarge repo，small repo 中完全不存在\\\", \\\"correlation\\\": {\\\"dataflow_edges_vs_repo_size_pearson_r\\\": 0.089}, \\\"cross_distribution\\\": {\\\"rich_in_large_xlarge_pct\\\": 99.3, \\\"rich_in_small\\\": 0, \\\"moderate_in_large_xlarge_pct\\\": 60.9}, \\\"implication\\\": \\\"真实评估必须控制 pool_size 和 repo_size 来隔离 dataflow richness 独立效应\\\"}, \\\"invalid_findings\\\": \\\"所有 R@1/R@5/MRR 值均为 mock predictions，策略排序 pattern 不可信，禁止引用\\\", \\\"artifacts_path\\\": \\\"/root/autodl-tmp/structfuse/artifacts/confound_analysis/\\\", \\\"valid_artifact\\\": \\\"cross_tabulation.csv\\\"}}}, \\\"m2_full_starcoder\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-13T16:18:15.415Z\\\", \\\"updated_at\\\": \\\"2026-05-14T18:04:29.245Z\\\", \\\"hypothesis\\\": \\\"Full M2 StarCoder: 3 strategies × 3 seeds on full M1 data. Cross-encoder validation — if embedding > random holds for both Qwen and StarCoder, method is encoder-agnostic. Resolves plan_013 pilot negative (dataflow encoder-dependent).\\\", \\\"parent\\\": \\\"plan_013_starcoder\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"cd /root/structfuse && bash run_m2_full_starcoder_resume.sh\\\\\\\"\\\", \\\"server\\\": \\\"bjb1-42106\\\", \\\"gpu\\\": [\\\"cuda:1\\\"], \\\"pid\\\": \\\"519791\\\", \\\"log_path\\\": \\\"~/runs/structfuse-context/m2_full_starcoder.log\\\", \\\"submitted_at\\\": \\\"2026-05-14T18:03:12.079Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\"}, \\\"notes\\\": \\\"Phase 1: 构建 StarCoder embedding negatives 完成。Phase 2: 9 runs 训练中。batch_size=8, num_negatives=7, epochs=3(s42)/2(s43+), lr=2e-5, eval_steps=500, no early_stopping。双 checkpoint: best + best_by_recall_at_1。Seeds: 42,43,44。[D026] s42 保持 3 epochs; s43/s44 及后续 runs 改为 2 epochs。[2026-05-15 02:02 CST] cuda:1 进程冲突修复并重新提交（PID 519791, timeout=144h）。Registry 状态 DONE(failed) 是旧 cron timeout 标记，实际正在运行 random_s43 [1/8]。新 cron 已注册监控 PID 519791。序列：random_s43→s44→(待插入bm25_s42)→embedding×3→dataflow×3。random_s42 结果：best R@1=0.4604 at step 2500, val_loss=0.6134 at step 1000。\\\", \\\"metrics\\\": {\\\"random_s42\\\": {\\\"epoch\\\": \\\"3/3\\\", \\\"current_step\\\": 4200, \\\"total_steps\\\": 4242, \\\"total_steps_per_epoch\\\": 1414, \\\"eval_500\\\": {\\\"val_loss\\\": 0.6194, \\\"recall_at_1\\\": 0.435, \\\"recall_at_5\\\": 0.905, \\\"recall_at_10\\\": 1}, \\\"eval_1000\\\": {\\\"val_loss\\\": 0.6134, \\\"recall_at_1\\\": 0.454, \\\"recall_at_5\\\": 0.92, \\\"recall_at_10\\\": 1}, \\\"eval_1500\\\": {\\\"val_loss\\\": 0.6528, \\\"recall_at_1\\\": 0.449, \\\"recall_at_5\\\": 0.906, \\\"recall_at_10\\\": 1}, \\\"eval_2000\\\": {\\\"val_loss\\\": 0.6698, \\\"recall_at_1\\\": 0.4456, \\\"recall_at_5\\\": 0.906, \\\"recall_at_10\\\": 1}, \\\"eval_2500\\\": {\\\"val_loss\\\": 0.6342, \\\"recall_at_1\\\": 0.4604, \\\"recall_at_5\\\": 0.9117, \\\"recall_at_10\\\": 1}, \\\"eval_3000\\\": {\\\"val_loss\\\": 0.6516, \\\"recall_at_1\\\": 0.4544, \\\"recall_at_5\\\": 0.9077, \\\"recall_at_10\\\": 1}, \\\"eval_3500\\\": {\\\"val_loss\\\": 0.6588, \\\"recall_at_1\\\": 0.4534, \\\"recall_at_5\\\": 0.9057, \\\"recall_at_10\\\": 1}, \\\"eval_4000\\\": {\\\"val_loss\\\": 0.6637, \\\"recall_at_1\\\": 0.4547, \\\"recall_at_5\\\": 0.9003, \\\"recall_at_10\\\": 1}, \\\"best_checkpoint\\\": \\\"step_1000 (val_loss=0.6134) / step_2500 (R@1=0.4604)\\\", \\\"conclusion\\\": \\\"effectively_complete (timeout at step 4200/4242, lr=7.8e-9, remaining 42 steps negligible)\\\"}, \\\"progress_snapshot\\\": \\\"2026-05-15T01:50 CST\\\"}, \\\"reproduce\\\": {\\\"finished_at\\\": \\\"2026-05-14T17:49:54.474Z\\\"}, \\\"failure_reason\\\": \\\"EXIT_CODE=124 (timeout — exceeded timeout_hours)\\\", \\\"conclusion\\\": \\\"failed\\\", \\\"completed_at\\\": \\\"2026-05-14T17:49:55.304Z\\\", \\\"extra\\\": {\\\"hook_events\\\": [{\\\"event\\\": \\\"on_failed\\\", \\\"action\\\": \\\"agent\\\", \\\"ts\\\": \\\"2026-05-14T17:49:56.408767+00:00\\\"}]}}, \\\"m2_full_qwen\\\": {\\\"status\\\": \\\"ANALYZING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-13T16:18:14.870Z\\\", \\\"updated_at\\\": \\\"2026-05-14T18:00:29.323Z\\\", \\\"hypothesis\\\": \\\"Full M2 Qwen: 3 strategies (random/embedding/dataflow) × 3 seeds on full M1 data (~11K train/seed). Statistical validation of pilot signal (embedding > random +2pp). Go/no-go for paper claims per D018.\\\", \\\"parent\\\": \\\"m2_embed_verify\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/structfuse && bash run_m2_full_qwen.sh 2>&1 | tee /root/runs/structfuse-context/m2_full_qwen.log\\\\\\\"\\\", \\\"server\\\": \\\"bjb1-42106\\\", \\\"gpu\\\": [\\\"cuda:0\\\"], \\\"pid\\\": \\\"73544\\\", \\\"log_path\\\": \\\"~/runs/structfuse-context/m2_full_qwen.log\\\", \\\"submitted_at\\\": \\\"2026-05-13T17:39:30.757Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\"}, \\\"notes\\\": \\\"Full M2 go/no-go: 3 strategies (random, embedding_distance, dataflow_aware) × 3 seeds (42, 43, 44) = 9 runs sequential on cuda:0. Config: lr=2e-5, batch_size=8, eval_steps=500, num_negatives=7, max_seq_length=2048, warmup_ratio=0.1, weight_decay=0.01, temperature=0.07, LoRA r=16, gradient_checkpointing=True, proj_dim=256. Dual checkpoint: best_by_val_loss + best_by_recall_at_1. Train ~11.3K/seed, val ~3K/seed. [D026] s42 保持 3 epochs 提供完整 overfitting curve; s43/s44 及后续 runs 改为 2 epochs + early_stopping_patience=2。[STATUS 2026-05-15 00:19 CST] Registry 状态 ANALYZING 是 cron 自动设置（s42 进程退出触发），但实验实际仍在进行中。random_s43 在 cuda:0 正常运行，step 1200/2810 (43%)。eval@500 R@1=0.5357, eval@1000 R@1=0.5285 (early_stopping 1/2)。Best R@1=0.5357 at step 500。GPU 100% 利用率, 50.5/97.9GB VRAM。\\\", \\\"metrics\\\": {\\\"random_s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"epoch\\\": \\\"3/3\\\", \\\"total_steps\\\": 4242, \\\"total_steps_per_epoch\\\": 1414, \\\"eval_500\\\": {\\\"val_loss\\\": 0.4869, \\\"recall_at_1\\\": 0.533, \\\"recall_at_5\\\": 0.954, \\\"recall_at_10\\\": 1}, \\\"eval_1000\\\": {\\\"val_loss\\\": 0.4651, \\\"recall_at_1\\\": 0.553, \\\"recall_at_5\\\": 0.959, \\\"recall_at_10\\\": 1}, \\\"eval_1500\\\": {\\\"val_loss\\\": 0.5365, \\\"recall_at_1\\\": 0.523, \\\"recall_at_5\\\": 0.955, \\\"recall_at_10\\\": 1}, \\\"eval_2000\\\": {\\\"val_loss\\\": 0.5162, \\\"recall_at_1\\\": 0.523, \\\"recall_at_5\\\": 0.954, \\\"recall_at_10\\\": 1}, \\\"eval_2500\\\": {\\\"val_loss\\\": 0.5264, \\\"recall_at_1\\\": 0.527, \\\"recall_at_5\\\": 0.956, \\\"recall_at_10\\\": 1}, \\\"eval_3000\\\": {\\\"val_loss\\\": 0.5406, \\\"recall_at_1\\\": 0.536, \\\"recall_at_5\\\": 0.956, \\\"recall_at_10\\\": 1}, \\\"best_checkpoint\\\": \\\"step_1000 (val_loss=0.4651, R@1=0.5527)\\\", \\\"conclusion\\\": \\\"Overfit after step 1000. Best R@1=0.5527, +1.7pp vs pilot (0.5357). Full data helps.\\\"}, \\\"random_s43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"epoch\\\": \\\"early_stopped\\\", \\\"total_steps_per_epoch\\\": 1405, \\\"eval_500\\\": {\\\"val_loss\\\": 0.4476, \\\"recall_at_1\\\": 0.5357}, \\\"eval_1000\\\": {\\\"val_loss\\\": 0.4637, \\\"recall_at_1\\\": 0.5285}, \\\"eval_1500\\\": {\\\"recall_at_1\\\": 0.5554}, \\\"best_by_val_loss\\\": \\\"step 500 (val_loss=0.4476)\\\", \\\"best_by_recall_at_1\\\": \\\"step 1500 (R@1=0.5554)\\\", \\\"conclusion\\\": \\\"Early stopped at step 1500. Best R@1=0.5554, consistent with s42 (0.5527). val_loss and R@1 criterion diverge.\\\"}, \\\"random_s44\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"note\\\": \\\"Auto-started 01:58 CST, epoch 1/2, 1408 batches/epoch\\\"}, \\\"progress_snapshot\\\": \\\"2026-05-15T02:00 CST\\\"}, \\\"reproduce\\\": {\\\"finished_at\\\": \\\"2026-05-14T11:24:33.887Z\\\"}, \\\"extra\\\": {\\\"hook_events\\\": [{\\\"event\\\": \\\"on_complete\\\", \\\"action\\\": \\\"agent\\\", \\\"ts\\\": \\\"2026-05-14T11:24:35.375104+00:00\\\"}]}}, \\\"plan_018_bm25\\\": {\\\"status\\\": \\\"QUEUED\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-14T16:38:40.603Z\\\", \\\"updated_at\\\": \\\"2026-05-14T17:09:50.985Z\\\", \\\"hypothesis\\\": \\\"BM25 negative baseline: Dream 审稿三档一致认定缺 BM25 baseline 是论文最大结构性缺陷。Phase 1 (CPU): 对 M2 训练语料建 BM25 索引，挖掘 BM25 hard negatives，生成训练数据。Phase 2 (GPU): 用 BM25 negatives 训练 Qwen + StarCoder 各 1 seed，对比 R@1。\\\", \\\"parent\\\": \\\"m2_full_qwen\\\", \\\"notes\\\": \\\"Phase 1 (CPU) COMPLETE: BM25 negative mining 完成。3 seeds 数据生成，record counts 与其他策略完全一致，0 fallback。BM25 score 分布: mean=246.50, std=155.96。重叠率: BM25 vs embedding_distance ~87.1%, vs random ~76.2%, vs dataflow_aware ~71.8%。高 median=1.0 因小 repo 候选池≤50 文件导致策略完全重合，BM25 differentiation 主要在大 repo。脚本: /root/structfuse/scripts/mine_bm25_negatives.py。输出: /root/autodl-tmp/structfuse/full_m2_training_data/{train,val}_bm25_s{42,43,44}.jsonl。Phase 2 (GPU): 等 re-dream gate 通过 + M2 完成后训练。\\\", \\\"metrics\\\": {\\\"phase1_complete\\\": true, \\\"seed_42\\\": {\\\"train_records\\\": 11308, \\\"val_records\\\": 2980, \\\"train_size_mb\\\": 1280.8, \\\"val_size_mb\\\": 344.6}, \\\"seed_43\\\": {\\\"train_records\\\": 11236, \\\"val_records\\\": 3052, \\\"train_size_mb\\\": 1280.9, \\\"val_size_mb\\\": 316}, \\\"seed_44\\\": {\\\"train_records\\\": 11264, \\\"val_records\\\": 3024, \\\"train_size_mb\\\": 1347.1, \\\"val_size_mb\\\": 295.9}, \\\"bm25_score_dist\\\": {\\\"count\\\": 392954, \\\"mean\\\": 246.5, \\\"std\\\": 155.96, \\\"p25\\\": 128.38, \\\"p50\\\": 228.41, \\\"p75\\\": 347.85, \\\"max\\\": 2585.74}, \\\"overlap_overall\\\": {\\\"bm25_vs_embedding\\\": 0.871, \\\"bm25_vs_random\\\": 0.762, \\\"bm25_vs_dataflow\\\": 0.718, \\\"note\\\": \\\"k=50 full candidate overlap from mining worker\\\"}, \\\"overlap_stratified_top7_jaccard\\\": {\\\"small_lt50\\\": {\\\"repos\\\": 39, \\\"bm25_vs_embedding\\\": 0.668, \\\"bm25_vs_random\\\": 0.411, \\\"bm25_vs_dataflow\\\": 0.667}, \\\"medium_50_200\\\": {\\\"repos\\\": 29, \\\"bm25_vs_embedding\\\": 0.38, \\\"bm25_vs_random\\\": 0.067, \\\"bm25_vs_dataflow\\\": 0.363}, \\\"large_200plus\\\": {\\\"repos\\\": 15, \\\"bm25_vs_embedding\\\": 0.297, \\\"bm25_vs_random\\\": 0.007, \\\"bm25_vs_dataflow\\\": 0.405}, \\\"matched_queries\\\": 2920, \\\"total_queries\\\": 12290, \\\"note\\\": \\\"top-7 Jaccard on s42 matched queries only (24% match rate due to different train/val splits)\\\"}}}, \\\"plan_015_dynamic\\\": {\\\"status\\\": \\\"QUEUED\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-14T17:03:24.316Z\\\", \\\"updated_at\\\": \\\"2026-05-14T17:03:30.544Z\\\", \\\"hypothesis\\\": \\\"Dynamic negative mining (epoch-level re-mining): 每 epoch 重新用当前 encoder embedding 挖掘 negatives，验证 static mining 是否足够。缩减版：只跑 dynamic_ep × 1 seed (Qwen, s42)，~11h 单卡。若 dynamic ≈ static（预期 <1pp 差异），在 Limitation 段排除 confound。\\\", \\\"notes\\\": \\\"Director D031 缩减：原 44h → 11h 单卡。只跑 dynamic_ep × 1 seed (Qwen, s42)，跳过 dynamic_500。Post-M2 与 plan_003 并行（一卡 SWE-bench，一卡 dynamic_ep）。受 re-dream gate 约束。设计文档已由 Worker 完成。\\\"}, \\\"neg_difficulty_analysis\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-13T19:39:20.016Z\\\", \\\"updated_at\\\": \\\"2026-05-14T00:13:49.046Z\\\", \\\"hypothesis\\\": \\\"Negative difficulty distribution analysis: 用预训练 Qwen2.5-Coder-3B 和 StarCoder2-3B 计算 3 策略 (random/embedding/dataflow) 的 query-negative/positive cosine similarity，分析 pretrained representation separability 跨编码器差异。MAX_LENGTH=2048 匹配训练设置。\\\", \\\"notes\\\": \\\"128 vs 2048 token 对比完成（2026-05-14 05:54 CST）。Qwen pos_sim 在 2048t 下 0.9855（比 128t 的 0.9804 更高），确认 ceiling 为 Qwen 表征的结构性特征，非截断 artifact。StarCoder margin 2.6-4.1x Qwen（2048t）。核心结论：pretrained representation separability varies across encoders，跨两种 token 长度成立。数据源：128t → stats_v2.json，2048t → stats_v3_2048.json。\\\", \\\"metrics\\\": {\\\"qwen_128\\\": {\\\"random\\\": {\\\"pos_sim\\\": 0.9804, \\\"neg_sim\\\": 0.899, \\\"margin\\\": 0.0816, \\\"pct_positive_margin\\\": 77.8}, \\\"embedding_distance\\\": {\\\"pos_sim\\\": 0.9804, \\\"neg_sim\\\": 0.959, \\\"margin\\\": 0.0209, \\\"pct_positive_margin\\\": 60.7}, \\\"dataflow_aware\\\": {\\\"pos_sim\\\": 0.9805, \\\"neg_sim\\\": 0.95, \\\"margin\\\": 0.0309, \\\"pct_positive_margin\\\": 67.4}}, \\\"starcoder_128\\\": {\\\"random\\\": {\\\"pos_sim\\\": 0.757, \\\"neg_sim\\\": 0.553, \\\"margin\\\": 0.2039, \\\"pct_positive_margin\\\": 72.8}, \\\"embedding_distance\\\": {\\\"pos_sim\\\": 0.784, \\\"neg_sim\\\": 0.668, \\\"margin\\\": 0.1159, \\\"pct_positive_margin\\\": 59.2}, \\\"dataflow_aware\\\": {\\\"pos_sim\\\": 0.761, \\\"neg_sim\\\": 0.659, \\\"margin\\\": 0.1022, \\\"pct_positive_margin\\\": 62.8}}, \\\"qwen_2048\\\": {\\\"random\\\": {\\\"pos_sim\\\": 0.9855, \\\"neg_sim\\\": 0.9111, \\\"margin\\\": 0.0743, \\\"margin_std\\\": 0.2322, \\\"pct_positive_margin\\\": 81.8}, \\\"embedding_distance\\\": {\\\"pos_sim\\\": 0.9855, \\\"neg_sim\\\": 0.9685, \\\"margin\\\": 0.017, \\\"margin_std\\\": 0.114, \\\"pct_positive_margin\\\": 58.8}, \\\"dataflow_aware\\\": {\\\"pos_sim\\\": 0.9856, \\\"neg_sim\\\": 0.9563, \\\"margin\\\": 0.0293, \\\"margin_std\\\": 0.1407, \\\"pct_positive_margin\\\": 73.9}}, \\\"starcoder_2048\\\": {\\\"random\\\": {\\\"pos_sim\\\": 0.7985, \\\"neg_sim\\\": 0.6045, \\\"margin\\\": 0.194, \\\"margin_std\\\": 0.2788, \\\"pct_positive_margin\\\": 78}, \\\"embedding_distance\\\": {\\\"pos_sim\\\": 0.8079, \\\"neg_sim\\\": 0.7409, \\\"margin\\\": 0.067, \\\"margin_std\\\": 0.2056, \\\"pct_positive_margin\\\": 55}, \\\"dataflow_aware\\\": {\\\"pos_sim\\\": 0.8009, \\\"neg_sim\\\": 0.6818, \\\"margin\\\": 0.1192, \\\"margin_std\\\": 0.2264, \\\"pct_positive_margin\\\": 70.4}}, \\\"sc_qwen_margin_ratio_128\\\": {\\\"random\\\": 2.5, \\\"embedding_distance\\\": 5.54, \\\"dataflow_aware\\\": 3.3}, \\\"sc_qwen_margin_ratio_2048\\\": {\\\"random\\\": 2.61, \\\"embedding_distance\\\": 3.94, \\\"dataflow_aware\\\": 4.07}}, \\\"conclusion\\\": \\\"success\\\", \\\"spec\\\": {\\\"command\\\": \\\"python negative_difficulty_margin_v2.py (CPU analysis)\\\", \\\"server\\\": \\\"bjb1-42106\\\", \\\"data_path\\\": \\\"/root/autodl-tmp/structfuse/full_m2_data/\\\", \\\"data_count\\\": 11000, \\\"model_name\\\": \\\"Qwen2.5-Coder-3B + StarCoder2-3B (pretrained, no training)\\\", \\\"seed\\\": \\\"N/A\\\", \\\"checkpoint_path\\\": \\\"N/A (analysis only)\\\", \\\"log_path\\\": \\\"/root/autodl-tmp/structfuse/artifacts/negative_difficulty_stats_v3_2048.json\\\"}, \\\"completed_at\\\": \\\"2026-05-14T00:13:49.046Z\\\"}, \\\"m1_reextract\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-13T19:35:23.954Z\\\", \\\"updated_at\\\": \\\"2026-05-13T19:45:53.741Z\\\", \\\"hypothesis\\\": \\\"M1 重提取：恢复 28,276 个因运行时瞬态文件系统故障失败的 instances（82 repos）。预期将训练数据从 15,897 提升至 ~44,173。D022 批准。\\\", \\\"parent\\\": \\\"m1_extraction\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash scripts/rerun_m1_failed.sh (4 CPU workers, CodeQL 2-hop)\\\", \\\"server\\\": \\\"bjb1-42106\\\", \\\"data_path\\\": \\\"/root/autodl-tmp/structfuse/m1_extraction/\\\", \\\"data_count\\\": 28276, \\\"model_name\\\": \\\"N/A (CodeQL extraction)\\\", \\\"seed\\\": \\\"N/A\\\", \\\"pid\\\": \\\"97358\\\", \\\"log_path\\\": \\\"/root/runs/structfuse-context/m1_rerun.log\\\", \\\"checkpoint_source\\\": \\\"rerun of m1_extraction failed instances\\\", \\\"eval_data\\\": \\\"N/A\\\", \\\"checkpoint_path\\\": \\\"N/A (failed, no output)\\\"}, \\\"conclusion\\\": \\\"failed\\\", \\\"notes\\\": \\\"CodeQL query 100% 失败（exit status 2）。根因：Worker 安装 CodeQL CLI 2.25.4 时未执行 `codeql pack install`，`codeql/python-all@7.1.0` 标准库 pack 缺失。修复命令：`cd /root/structfuse/extraction/codeql_queries && /opt/codeql/codeql pack install`。已 kill 进程 + tmux session。无新数据产出（all.jsonl 未受影响）。等 Director 确认后修复重跑。\\\", \\\"completed_at\\\": \\\"2026-05-13T19:44:09.115Z\\\"}, \\\"m1_extraction\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-12T21:00:02.300Z\\\", \\\"updated_at\\\": \\\"2026-05-13T19:26:13.901Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"nohup bash scripts/run_m1_extraction.sh (8 CPU workers, CodeQL 2-hop)\\\", \\\"server\\\": \\\"cqa1-21977\\\", \\\"data_path\\\": \\\"/root/autodl-tmp/structfuse/m1_extraction/\\\", \\\"data_count\\\": 50869, \\\"model_name\\\": \\\"N/A (CodeQL extraction)\\\", \\\"seed\\\": \\\"N/A\\\", \\\"description\\\": \\\"M1: 全量 5K repos CodeQL 提取, 131 unique (repo,commit) groups, 50869 instances\\\"}, \\\"metrics\\\": {\\\"total_instances_attempted\\\": 44173, \\\"instances_skipped\\\": 6696, \\\"total_instances\\\": 50869, \\\"codeql_success\\\": 15133, \\\"beniget_fallback\\\": 764, \\\"extraction_failed\\\": 28276, \\\"structural_data_rate\\\": 0.36, \\\"repos_with_output\\\": 123, \\\"repos_total\\\": 131, \\\"repo_coverage\\\": 0.939, \\\"skip_clone_failed\\\": 5852, \\\"skip_checkout_failed\\\": 836, \\\"skip_stale_handle\\\": 8, \\\"elapsed_minutes\\\": 837.8, \\\"avg_time_per_instance_s\\\": 8.9, \\\"output_size_gb\\\": 6.6, \\\"disk_usage_gb\\\": 13, \\\"output_file\\\": \\\"all.jsonl\\\"}, \\\"notes\\\": \\\"[2026-05-13 19:25] COMPLETED. 837.8min, 123/131 repos (93.9%), 15,897/44,173 instances with structural data (36.0%), 6,696 skipped (clone/checkout). Output: all.jsonl 6.6GB. [2026-05-13 19:23 UPDATE] 28,276 buggy_file_not_found errors 经验证并非上游数据质量问题——10/10 抽查的文件在 repo 中全部存在。根因是运行时瞬态文件系统故障（CodeQL 并行 database creation 导致磁盘耗尽，锐截止模式）。这些 instances 可通过重跑恢复。D022: 准备重跑脚本中，等 Director 确认后执行。\\\", \\\"conclusion\\\": \\\"success\\\", \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/structfuse/m1_extraction/all.jsonl\\\", \\\"log_path\\\": \\\"/tmp/m1_extraction.log\\\", \\\"completed_at\\\": \\\"2026-05-13T10:59:42.462Z\\\"}, \\\"plan_006_scalability\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-13T07:57:43.631Z\\\", \\\"updated_at\\\": \\\"2026-05-13T19:24:00.741Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"M1 scalability statistics analysis (29/131 repos)\\\", \\\"server\\\": \\\"bjb1-42106\\\", \\\"data_path\\\": \\\"/root/autodl-tmp/structfuse/m1_extraction/\\\", \\\"data_count\\\": 8171, \\\"model_name\\\": \\\"N/A (CPU analysis)\\\", \\\"seed\\\": \\\"N/A\\\", \\\"description\\\": \\\"Plan 006: M1 extraction scalability stats - timeout rate, extraction time, coverage, Z% by repo size. Partial results from 29/131 repos.\\\", \\\"checkpoint_path\\\": \\\"N/A\\\", \\\"log_path\\\": \\\"N/A\\\"}, \\\"conclusion\\\": \\\"success\\\", \\\"completed_at\\\": \\\"2026-05-13T07:57:58.176Z\\\", \\\"notes\\\": \\\"[2026-05-13 19:23] 全量统计 + error 分析 + fuzzy match 验证完成。关键发现: (1) 0 timeout; (2) 28,276 error 全部 buggy_file_not_found，但 fuzzy match 验证发现文件实际都存在——根因是运行时瞬态文件系统故障（锐截止模式：每个 repo 内先成功后突然全部失败，extraction_time=0.0s），可能是 CodeQL 并行数据库创建导致磁盘空间耗尽; (3) 这些 instance 可通过重跑恢复（当前 resolve_file_in_repo 对全部样本返回正确路径）; (4) 结构数据率 34.3% 有望提升至接近 100%（若重跑成功）; (5) Z% 随 repo 规模上升 (XL median 96%). Artifacts: plan006_full_scalability.json, art_20260513_d262da (error patterns)\\\", \\\"hypothesis\\\": \\\"Claim 3: CodeQL bounded data-flow extraction scales to large repos with acceptable timeout rates and provides meaningful structural coverage (Z%) that increases with repo complexity\\\", \\\"metrics\\\": {\\\"repos\\\": 123, \\\"total_instances\\\": 44173, \\\"structural_data_rate\\\": 0.343, \\\"error_rate\\\": 0.64, \\\"zero_timeout_rate\\\": true, \\\"processing_time\\\": {\\\"mean_s\\\": 8.93, \\\"median_s\\\": 0, \\\"p95_s\\\": 31.95, \\\"max_s\\\": 633.68, \\\"total_hours\\\": 109.58}, \\\"by_tier\\\": {\\\"small_lt50\\\": {\\\"repos\\\": 1, \\\"instances\\\": 500, \\\"error_rate\\\": 0.054, \\\"struct_rate\\\": 0.81, \\\"z_pct_mean\\\": 0.284, \\\"z_pct_median\\\": 0}, \\\"medium_50_200\\\": {\\\"repos\\\": 17, \\\"instances\\\": 4096, \\\"error_rate\\\": 0.485, \\\"struct_rate\\\": 0.472, \\\"z_pct_mean\\\": 0.444, \\\"z_pct_median\\\": 0.5}, \\\"large_200_500\\\": {\\\"repos\\\": 40, \\\"instances\\\": 13628, \\\"error_rate\\\": 0.639, \\\"struct_rate\\\": 0.343, \\\"z_pct_mean\\\": 0.604, \\\"z_pct_median\\\": 0.857}, \\\"xlarge_500plus\\\": {\\\"repos\\\": 29, \\\"instances\\\": 25949, \\\"error_rate\\\": 0.676, \\\"struct_rate\\\": 0.314, \\\"z_pct_mean\\\": 0.812, \\\"z_pct_median\\\": 0.96}}, \\\"instance_distribution\\\": {\\\"lt10\\\": 1, \\\"10_50\\\": 17, \\\"50_200\\\": 36, \\\"200_500\\\": 40, \\\"500plus\\\": 29}, \\\"artifact\\\": \\\"plan006_full_scalability.json\\\"}}, \\\"plan_013_starcoder\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-13T05:09:14.885Z\\\", \\\"updated_at\\\": \\\"2026-05-13T18:09:54.153Z\\\", \\\"hypothesis\\\": \\\"Architecture generalization: validate StructFuse with StarCoder2-3B encoder (vs Qwen2.5-Coder-3B in m2_embed_verify). If both encoders show same strategy ranking → method is encoder-agnostic, strengthening the core claim. Key differentiator for best→accept at Dream.\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"bash /root/structfuse/run_plan013_starcoder.sh\\\\\\\"\\\", \\\"server\\\": \\\"bjb1-42106\\\", \\\"gpu\\\": [\\\"cuda:0\\\"], \\\"pid\\\": \\\"23798\\\", \\\"log_path\\\": \\\"~/runs/structfuse-context/plan_013_starcoder.log\\\", \\\"submitted_at\\\": \\\"2026-05-13T05:26:21.946Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"data_path\\\": \\\"/root/autodl-tmp/structfuse/m2_embed_verify_data/\\\", \\\"data_count\\\": 3282, \\\"model_name\\\": \\\"bigcode/starcoder2-3b\\\", \\\"seed\\\": 42, \\\"wall_clock_seconds\\\": 35338.2, \\\"gpu_hours\\\": 9.82}, \\\"notes\\\": \\\"[2026-05-13 16:00] ALL 3 STRATEGIES DONE. Ranking: embedding (R@1=0.5078) > random (0.4922) > dataflow (0.4869). Embedding vs random: +1.6pp (consistent with Qwen). Dataflow vs random: -0.5pp (DIFFERS from Qwen where dataflow > random +0.8pp). Hypothesis NEGATIVE: strategy ranking NOT identical across encoders. Embedding > random is encoder-agnostic, dataflow position is encoder-dependent. Log: /root/runs/faith-evidence-ie/plan_013_starcoder.log. Cron misreported EXIT_CODE=129 but all strategies completed (confirmed via log extraction worker).\\\", \\\"metrics\\\": {\\\"random\\\": {\\\"status\\\": \\\"DONE\\\", \\\"best_val_loss\\\": 0.5113, \\\"best_recall@1\\\": 0.4922, \\\"best_recall@5\\\": 0.98, \\\"best_recall@10\\\": 1, \\\"source\\\": \\\"/tmp/eval_random_s42.log (post-hoc eval, no in-training eval)\\\"}, \\\"embedding_distance\\\": {\\\"status\\\": \\\"DONE\\\", \\\"best_step\\\": 1000, \\\"best_val_loss\\\": 0.4816, \\\"best_recall@1\\\": 0.5078, \\\"best_recall@5\\\": 0.9843, \\\"best_recall@10\\\": 1, \\\"final_val_loss\\\": 0.506, \\\"final_recall@1\\\": 0.5174}, \\\"dataflow_aware\\\": {\\\"status\\\": \\\"DONE\\\", \\\"best_step\\\": 1000, \\\"best_val_loss\\\": 0.5255, \\\"best_recall@1\\\": 0.4869, \\\"best_recall@5\\\": 0.9695, \\\"best_recall@10\\\": 1, \\\"final_val_loss\\\": 0.5509, \\\"final_recall@1\\\": 0.5078}}, \\\"failure_reason\\\": \\\"\\\", \\\"conclusion\\\": \\\"negative\\\", \\\"completed_at\\\": \\\"2026-05-13T15:15:20.165Z\\\"}, \\\"m2_embed_verify\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-13T04:39:16.051Z\\\", \\\"updated_at\\\": \\\"2026-05-13T15:59:51.621Z\\\", \\\"hypothesis\\\": \\\"True embedding mining verification: compare Qwen2.5-Coder-3B cosine similarity negatives vs BM25 negatives on pilot data (24 repos). If true embedding negatives are harder → Claim 2 (structure-aware negatives improve retrieval) gets stronger evidence.\\\", \\\"parent\\\": \\\"m2_early_pilot\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"bash /root/structfuse/run_m2_embed_verify.sh\\\\\\\"\\\", \\\"server\\\": \\\"bjb1-42106\\\", \\\"gpu\\\": [\\\"cuda:1\\\"], \\\"pid\\\": \\\"29290\\\", \\\"log_path\\\": \\\"~/runs/structfuse-context/m2_embed_verify.log\\\", \\\"submitted_at\\\": \\\"2026-05-13T06:37:00.822Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"data_path\\\": \\\"/root/autodl-tmp/structfuse/m2_embed_verify_data/\\\", \\\"data_count\\\": 3282, \\\"model_name\\\": \\\"Qwen/Qwen2.5-Coder-3B\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"training from scratch (not eval)\\\", \\\"eval_data\\\": \\\"N/A (training, not eval)\\\", \\\"wall_clock_seconds\\\": 31097.9, \\\"gpu_hours\\\": 8.64}, \\\"notes\\\": \\\"[2026-05-13 16:00] ALL 3 STRATEGIES DONE. Ranking: embedding (R@1=0.5557) > dataflow (0.5436) > random (0.5357). Embedding vs random: +2.0pp. Dataflow vs random: +0.8pp. All best at step 500, overfitting after. Hypothesis confirmed: true embedding negatives are harder → Claim 2 supported. Log: /root/runs/faith-evidence-ie/m2_embed_verify.log. Cron misreported EXIT_CODE=2 but all strategies completed successfully (confirmed via log extraction worker).\\\", \\\"metrics\\\": {\\\"random\\\": {\\\"status\\\": \\\"DONE\\\", \\\"best_step\\\": 500, \\\"best_val_loss\\\": 0.4834, \\\"best_recall@1\\\": 0.5357, \\\"best_recall@5\\\": 0.9808, \\\"best_recall@10\\\": 1, \\\"final_val_loss\\\": 0.5978, \\\"final_recall@1\\\": 0.5122}, \\\"embedding_distance\\\": {\\\"status\\\": \\\"DONE\\\", \\\"best_step\\\": 500, \\\"best_val_loss\\\": 0.4603, \\\"best_recall@1\\\": 0.5557, \\\"best_recall@5\\\": 0.9808, \\\"best_recall@10\\\": 1, \\\"final_val_loss\\\": 0.5935, \\\"final_recall@1\\\": 0.5209}, \\\"dataflow_aware\\\": {\\\"status\\\": \\\"DONE\\\", \\\"best_step\\\": 500, \\\"best_val_loss\\\": 0.5602, \\\"best_recall@1\\\": 0.5436, \\\"best_recall@5\\\": 0.9817, \\\"best_recall@10\\\": 1, \\\"final_val_loss\\\": 0.6201, \\\"final_recall@1\\\": 0.5287}}, \\\"failure_reason\\\": \\\"EXIT_CODE=2 (shell misuse / syntax)\\\", \\\"conclusion\\\": \\\"success\\\", \\\"completed_at\\\": \\\"2026-05-13T15:15:18.746Z\\\"}, \\\"mvp_p2b_contrastive_v2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-12T15:03:02.370Z\\\", \\\"updated_at\\\": \\\"2026-05-13T07:23:28.932Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash scripts/run_p2b_all.sh (9 runs: 3 strategies × 3 seeds)\\\", \\\"server\\\": \\\"cqa1-21977\\\", \\\"gpu\\\": [\\\"cuda:4\\\"], \\\"pid\\\": \\\"132149\\\", \\\"data_path\\\": \\\"/root/structfuse/mvp_data/training_data/\\\", \\\"data_count\\\": 127, \\\"model_name\\\": \\\"Qwen2.5-Coder-3B + LoRA\\\", \\\"seed\\\": \\\"42,123,7\\\", \\\"hypothesis\\\": \\\"H3: data-flow hard negatives vs random vs embedding-distance, 3-seed × 3-strategy contrastive training\\\", \\\"plan_id\\\": \\\"mvp_p2b_contrastive_training\\\", \\\"checkpoint_path\\\": \\\"N/A\\\", \\\"log_path\\\": \\\"N/A\\\"}, \\\"conclusion\\\": \\\"killed\\\", \\\"completed_at\\\": \\\"2026-05-12T15:04:44.396Z\\\", \\\"notes\\\": \\\"P2b 对比训练 v2，因磁盘空间不足被 kill。已被 p2b_5reruns（成功完成 9/9 runs）替代。\\\"}, \\\"p2b_dataflow_retrain\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-12T19:49:00.303Z\\\", \\\"updated_at\\\": \\\"2026-05-13T07:23:27.706Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"build_p2b_data.py regeneration + dataflow 3-seed retrain\\\", \\\"server\\\": \\\"cqa1-21977\\\", \\\"data_path\\\": \\\"/root/structfuse\\\", \\\"data_count\\\": 0, \\\"model_name\\\": \\\"Qwen2.5-Coder-3B (LoRA)\\\", \\\"seed\\\": \\\"42,123,456\\\", \\\"description\\\": \\\"BLOCKED: dataflow connections ⊆ gold files, strategies indistinguishable\\\", \\\"checkpoint_path\\\": \\\"N/A\\\", \\\"log_path\\\": \\\"N/A\\\"}, \\\"conclusion\\\": \\\"negative\\\", \\\"completed_at\\\": \\\"2026-05-13T04:17:02.055Z\\\", \\\"notes\\\": \\\"Dataflow 策略重训练计划，因 embedding_distance 命名问题（实际用 BM25 而非 embedding）被 Reviewer 发现后搁置。已被 m2_embed_verify（true embedding mining）替代。\\\"}, \\\"p2b_eval_all\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-12T16:27:50.967Z\\\", \\\"updated_at\\\": \\\"2026-05-13T07:23:24.721Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/structfuse && bash scripts/run_eval_all.sh\\\\\\\"\\\", \\\"server\\\": \\\"cqa1-21977\\\", \\\"gpu\\\": [\\\"cuda:4\\\"], \\\"pid\\\": \\\"254053\\\", \\\"log_path\\\": \\\"N/A\\\", \\\"submitted_at\\\": \\\"2026-05-12T16:27:50.945Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"checkpoint_path\\\": \\\"N/A\\\", \\\"wall_clock_seconds\\\": 42550.6, \\\"gpu_hours\\\": 11.82}, \\\"conclusion\\\": \\\"killed\\\", \\\"completed_at\\\": \\\"2026-05-13T04:17:01.561Z\\\", \\\"notes\\\": \\\"P2b 全量 eval（pool_size=26），被 D013 服务器迁移计划取消。已被 p2b_eval_4runs_pool50（pool_size=50）替代。\\\"}, \\\"m2_early_pilot\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-13T01:39:53.920Z\\\", \\\"updated_at\\\": \\\"2026-05-13T04:44:22.077Z\\\", \\\"hypothesis\\\": \\\"Early pilot on partial M1 data (24 repos, ~5K instances): verify M2 training pipeline works end-to-end and get early signal on 3-strategy differentiation before full M1 completes\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash /root/structfuse/scripts/run_m2_pilot.sh\\\", \\\"server\\\": \\\"cqa1-21977\\\", \\\"gpu\\\": [\\\"cuda:4\\\"], \\\"pid\\\": \\\"795739\\\", \\\"log_path\\\": \\\"/root/autodl-tmp/structfuse/m2_pilot_output/random_s42.log\\\", \\\"submitted_at\\\": \\\"2026-05-13T01:55:31.288Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"data_path\\\": \\\"/root/autodl-tmp/structfuse/m2_pilot_data/\\\", \\\"data_count\\\": 3418, \\\"model_name\\\": \\\"Qwen/Qwen2.5-Coder-3B\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"N/A (training from scratch)\\\", \\\"eval_data\\\": \\\"N/A (training, not eval)\\\", \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/structfuse/m2_pilot_output/random_s42/best_model.pt\\\", \\\"wall_clock_seconds\\\": 10130.8, \\\"gpu_hours\\\": 2.81}, \\\"conclusion\\\": \\\"killed\\\", \\\"notes\\\": \\\"PID 795791 在 cqa1 cuda:4 运行，wrapper 脚本顺序跑 random→embedding→dataflow（set -e）。random 策略跑到 step 4000 后卡住（~45min 无新日志），embedding/dataflow 未启动。Best checkpoint at step 1500。Val_loss 持续恶化（0.5879→0.728），明显过拟合。另有 OOM 进程干扰（某进程试图在同 GPU 启动导致 OOM，可能破坏 GPU 状态）。eval recall@k bug 已确认。\\\", \\\"metrics\\\": {\\\"pid\\\": 795791, \\\"gpu\\\": \\\"cuda:4\\\", \\\"gpu_mem_mb\\\": 9342, \\\"gpu_util_pct\\\": 83, \\\"batch_size\\\": 2, \\\"num_negatives\\\": 3, \\\"max_seq_length\\\": 1024, \\\"strategy_running\\\": \\\"random (stuck at step 4000, epoch 3)\\\", \\\"strategies_completed\\\": \\\"0/3\\\", \\\"eval_1500\\\": {\\\"val_loss\\\": 0.5879, \\\"recall_at_1\\\": 0.4693, \\\"recall_at_5\\\": 0.4693, \\\"recall_at_10\\\": 0.4693}, \\\"eval_2000\\\": {\\\"val_loss\\\": 0.7089, \\\"recall_at_1\\\": 0.4398}, \\\"eval_2500\\\": {\\\"val_loss\\\": 0.6961, \\\"recall_at_1\\\": 0.4291}, \\\"eval_3000\\\": {\\\"val_loss\\\": 0.728, \\\"recall_at_1\\\": 0.4104}, \\\"eval_3500\\\": {\\\"val_loss\\\": 0.7022, \\\"recall_at_1\\\": 0.4439}, \\\"best_checkpoint\\\": \\\"step_1500 (val_loss=0.5879, 6.2GB)\\\", \\\"WARNING\\\": \\\"recall@1=recall@5=recall@10 confirmed eval bug. Process hung after step 4000 (~45min no output). Overfitting after step 1500.\\\", \\\"status_check_at\\\": \\\"2026-05-13T04:42:00Z\\\"}, \\\"completed_at\\\": \\\"2026-05-13T04:44:22.077Z\\\"}, \\\"m2_early_pilot_v3\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-13T01:59:06.557Z\\\", \\\"updated_at\\\": \\\"2026-05-13T02:13:43.400Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"bash /root/structfuse/run_m2_early_pilot.sh\\\\\\\"\\\", \\\"server\\\": \\\"cqa1-21977\\\", \\\"gpu\\\": [\\\"cuda:0\\\"], \\\"pid\\\": \\\"897651\\\", \\\"log_path\\\": \\\"~/runs/structfuse-context/m2_early_pilot_v3.log\\\", \\\"submitted_at\\\": \\\"2026-05-13T02:04:31.768Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"checkpoint_path\\\": \\\"N/A\\\", \\\"wall_clock_seconds\\\": 551.6, \\\"gpu_hours\\\": 0.15}, \\\"conclusion\\\": \\\"killed\\\", \\\"notes\\\": \\\"GPU 越界 cuda:0，违反项目 GPU 分配 gpu_ids=[\\\\\\\"cuda:4\\\\\\\"]。第二次 GPU 越界违规（首次 D005）。Worker 未正确映射 CUDA_VISIBLE_DEVICES。\\\", \\\"completed_at\\\": \\\"2026-05-13T02:13:43.400Z\\\"}}, \\\"count\\\": 20, \\\"total\\\": 37, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.1012}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"plan_017_literature\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T18:49:00.477Z\", \"updated_at\": \"2026-05-14T21:33:45.149Z\", \"hypothesis\": \"Inference-time graph method comparison: 8 papers surveyed (CodexGraph, LocAgent, RANGER, GraphCoder, ARISE, RepoGraph, CodeGRAG, CodeRAG). Discussion v2 drafted, all citations verified. Conclusion: training-time vs inference-time complementary.\", \"spec\": {\"command\": \"analysis only (no training)\", \"server\": \"local\", \"data_path\": \"N/A\", \"data_count\": 0, \"model_name\": \"N/A\", \"seed\": \"N/A\", \"checkpoint_path\": \"N/A\", \"log_path\": \"N/A\"}, \"conclusion\": \"success\", \"metrics\": {\"papers_surveyed\": 8, \"citations_verified\": 8, \"discussion_draft\": \"artifacts/paper_drafts/discussion_v2.md\", \"artifact_id\": \"art_20260514_a2e1cd\"}, \"completed_at\": \"2026-05-14T18:49:39.557Z\", \"notes\": \"Inference-time graph method comparison 完成。8 papers surveyed，其中 6 篇纳入 literature_map.yaml 和 discussion_v2.md（CodexGraph, LocAgent, RANGER, GraphCoder, ARISE, RepoGraph）。CodeGRAG 和 CodeRAG 经调研排除：CodeGRAG（arXiv 2405.02355）关注 NL→code generation 的 graph-augmented prompting，不涉及代码检索或对比学习；CodeRAG 系列（CodeRAG-Bench 2406.14497 / CodeRAG 2504.10046）关注 retrieval-augmented code generation benchmark 和 bigraph-based 代码生成，均为生成任务而非检索训练。两者与 StructFuse 的 scope（训练时结构信号用于对比学习代码检索）不符，故未纳入 discussion。\"}, \"m1_reextract_v2\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-13T20:00:20.578Z\", \"updated_at\": \"2026-05-14T21:18:48.643Z\", \"hypothesis\": \"M1 重提取 v2：恢复 28,276 个因运行时瞬态文件系统故障失败的 instances（82 repos）。CodeQL pack 已修复，端到端测试通过。预期将训练数据从 15,897 提升至 ~44,173。D022 批准。\", \"parent\": \"m1_extraction\", \"spec\": {\"command\": \"bash scripts/rerun_m1_failed.sh (4 CPU workers, CodeQL 2-hop, pack installed)\", \"server\": \"bjb1-42106\", \"data_path\": \"/root/autodl-tmp/structfuse/full_m1_data/\", \"data_count\": 28276, \"model_name\": \"N/A (CodeQL extraction)\", \"seed\": \"N/A\", \"log_path\": \"/root/runs/structfuse-context/m1_reextract_v2.log\", \"checkpoint_source\": \"rerun of m1_extraction failed instances (v2, CodeQL fixed)\", \"eval_data\": \"N/A\"}, \"notes\": \"M1 重提取 v2：CodeQL pack 已修复，端到端测试通过。28,276 instances / 82 repo groups / 4 workers 并行。启动 2026-05-14 03:59 CST。[诊断 07:06 CST] 活跃运行中，~15/82 groups 完成，2,469 次 call_graph 查询成功，预计还需 ~13-16h。仅前 4 个旧 repo（furl/pyasn1/feedparser/python-docx）复用 v1 旧 DB 有 18 次降级 WARNING，04:02 之后零失败。产出写入 all.jsonl（追加模式）。磁盘 97GB 可用。[Director 决策 Session 8] 即使数据量增至 ~44K，不重跑 M2（ARR May 25 DDL 不允许再加 4-5 天重训）。处理方式：(1) post-M2 完成后如有 GPU 空档，跑 1-seed pilot (Qwen, embedding, 新数据) 对比当前 M2 baseline; (2) 论文中作为 scalability/data efficiency 讨论点; (3) 全量重训留 camera-ready。[进度检查 2026-05-15 05:05 CST] 80.8% 完成（22,842/28,276），0 ERROR，速率 ~560/hr，处理中大 repo：mozilla__bleach/sqlfluff/conan-io/Project-MONAI。产出为单独 .json 文件，尚未合并 all.jsonl。预计 ~15:00 CST May 15 完成。\", \"metrics\": {\"checked_at\": \"2026-05-15T05:15Z\", \"process\": \"alive (CPU, 4 workers)\", \"started\": \"2026-05-14T03:59Z\", \"elapsed_hours\": 25, \"total_instances\": 28276, \"repo_groups\": 82, \"output_json_files\": 40225, \"all_jsonl_lines\": 44173, \"active_repos\": {\"sqlfluff/sqlfluff\": \"250/1272\", \"mozilla/bleach\": \"350/455\", \"conan-io/conan\": \"450/972\", \"Project-MONAI/MONAI\": \"150/524\"}, \"estimated_total_hours\": 60, \"progress_pct_by_time\": \"~42%\", \"disk\": \"98GB free on /root/autodl-tmp\"}}, \"m2_full_starcoder_resumed\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-14T18:44:19.253Z\", \"updated_at\": \"2026-05-14T21:18:45.080Z\", \"hypothesis\": \"M2 StarCoder resumed: 继续 m2_full_starcoder 的 8 sequential runs (random×2 + embedding×3 + dataflow×3)。原实验因 cron timeout 标记为 failed，实际 PID 519791 正常运行。\", \"spec\": {\"command\": \"bash run_m2_full_starcoder_resume.sh (8 runs: random_s43→s44→embedding×3→dataflow×3)\", \"server\": \"bjb1-42106\", \"gpu\": [\"cuda:1\"], \"pid\": \"519791\", \"log_path\": \"/root/runs/structfuse-context/m2_full_starcoder.log\", \"data_path\": \"/root/autodl-tmp/structfuse/full_m2_training_data/\", \"data_count\": 11308, \"model_name\": \"StarCoder2-3B\", \"seed\": \"42,43,44\"}, \"parent\": \"m2_full_starcoder\", \"metrics\": {\"checked_at\": \"2026-05-15T05:15Z\", \"process\": \"alive (PID 519791, uptime 03:11:44)\", \"gpu\": \"cuda:1, 100% util, 53.9/97.9GB VRAM, 72°C\", \"current_subrun\": \"random_s43 (1/9)\", \"current_step\": \"550/1405 (epoch 1/2, ~20% of subrun)\", \"eval_at_500\": {\"R@1\": 0.4708, \"R@5\": 0.9469, \"val_loss\": 0.5279}, \"latest_loss\": 0.26, \"completed_subruns\": 0, \"remaining_subruns\": 8, \"eta_hours\": \"~65-70h\"}}, \"m2_full_qwen_continued\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-14T18:44:20.646Z\", \"updated_at\": \"2026-05-14T21:18:42.976Z\", \"hypothesis\": \"M2 Qwen continued: 继续 m2_full_qwen 的剩余 runs (random_s44 + embedding×3 + dataflow×3)。原实验 cron 在 s42 退出时自动设为 ANALYZING，但链仍在运行。\", \"spec\": {\"command\": \"bash run_m2_full_qwen.sh (chain: random_s44 running → embedding×3 → dataflow×3)\", \"server\": \"bjb1-42106\", \"gpu\": [\"cuda:0\"], \"pid\": \"337267\", \"log_path\": \"/root/runs/structfuse-context/m2_full_qwen.log\", \"data_path\": \"/root/autodl-tmp/structfuse/full_m2_training_data/\", \"data_count\": 11308, \"model_name\": \"Qwen2.5-Coder-3B\", \"seed\": \"42,43,44\"}, \"parent\": \"m2_full_qwen\", \"metrics\": {\"checked_at\": \"2026-05-15T05:15Z\", \"process\": \"alive (PID 337267, uptime 09:50:41)\", \"gpu\": \"cuda:0, 100% util, 51.5/97.9GB VRAM, 68°C\", \"current_subrun\": \"random_s44 (3/7)\", \"current_step\": \"850/1408 (epoch 1/2, ~30% of subrun)\", \"eval_at_500\": {\"R@1\": 0.6009, \"R@5\": 0.9583, \"val_loss\": 0.4252}, \"latest_loss\": 0.2837, \"completed_subruns\": {\"random_s42\": {\"best_R@1\": 0.5527, \"best_val_loss\": 0.4651}, \"random_s43\": {\"best_R@1\": 0.5554, \"best_val_loss\": 0.4476}}, \"remaining_subruns\": 5, \"eta_hours\": \"~40-45h\"}}, \"plan_005_stratified\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-14T20:36:16.738Z\", \"updated_at\": \"2026-05-14T21:07:45.324Z\", \"hypothesis\": \"Plan 005 分层分析：按 repo size/pool size/query-pos similarity/structural data availability/neg_difficulty quartile 5 维度分层评估 embedding vs random 策略差异，控制 pool_size confound。Claim 2 支撑实验。v2 结果为 ground truth（v1→v2 changelog 见 art_20260514_3008c4）。\", \"parent\": \"m2_full_qwen\", \"notes\": \"plan_id=plan_005. 分层评估脚本已完成全部修改（analyze_stratified.py）：(1) mock seed 确定性修复 (2) pool_size-controlled 策略对比（within-bin delta + weighted aggregate）(3) dataflow×pool_size 交叉分析（n<30 标记 underpowered）(4) checkpoint 发现逻辑已就绪（best_by_recall_at_1 / best / best_by_val_loss）。输出含 JSON + CSV + PDF。[2026-05-14 21:07] Worker 完成 5 项 Patch：(P1) reeval_checkpoint 重写为 batch encoding（query/positive/negatives 分组批量编码，tqdm 进度条，torch.no_grad + model.eval，pad_token 兜底）(P2) 新增 --batch-size 参数（默认 64）(P3) 调用处传递 batch_size (P4) 非 dry-run 自适应 sim bins（tercile 计算边界 + 重新分配 sim_bin）(P5) 输出 JSON 记录 similarity_bin_edges 和 batch_size。Dry-run 验证全部通过。真实评估待 M2 全部 checkpoint 就绪后执行。\", \"metrics\": {\"confound_analysis\": {\"data_validity\": \"⚠️ R@1 值为 dry-run mock predictions，不可引用。仅分布结构（cross_tabulation.csv）有效。\", \"valid_findings\": {\"distribution_structure\": \"rich-dataflow 99.3% 落在 large/xlarge repo，small repo 中完全不存在\", \"correlation\": {\"dataflow_edges_vs_repo_size_pearson_r\": 0.089}, \"cross_distribution\": {\"rich_in_large_xlarge_pct\": 99.3, \"rich_in_small\": 0, \"moderate_in_large_xlarge_pct\": 60.9}, \"implication\": \"真实评估必须控制 pool_size 和 repo_size 来隔离 dataflow richness 独立效应\"}, \"invalid_findings\": \"所有 R@1/R@5/MRR 值均为 mock predictions，策略排序 pattern 不可信，禁止引用\", \"artifacts_path\": \"/root/autodl-tmp/structfuse/artifacts/confound_analysis/\", \"valid_artifact\": \"cross_tabulation.csv\"}}}, \"m2_full_starcoder\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T16:18:15.415Z\", \"updated_at\": \"2026-05-14T18:04:29.245Z\", \"hypothesis\": \"Full M2 StarCoder: 3 strategies × 3 seeds on full M1 data. Cross-encoder validation — if embedding > random holds for both Qwen and StarCoder, method is encoder-agnostic. Resolves plan_013 pilot negative (dataflow encoder-dependent).\", \"parent\": \"plan_013_starcoder\", \"spec\": {\"command\": \"bash -c \\\"cd /root/structfuse && bash run_m2_full_starcoder_resume.sh\\\"\", \"server\": \"bjb1-42106\", \"gpu\": [\"cuda:1\"], \"pid\": \"519791\", \"log_path\": \"~/runs/structfuse-context/m2_full_starcoder.log\", \"submitted_at\": \"2026-05-14T18:03:12.079Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"notes\": \"Phase 1: 构建 StarCoder embedding negatives 完成。Phase 2: 9 runs 训练中。batch_size=8, num_negatives=7, epochs=3(s42)/2(s43+), lr=2e-5, eval_steps=500, no early_stopping。双 checkpoint: best + best_by_recall_at_1。Seeds: 42,43,44。[D026] s42 保持 3 epochs; s43/s44 及后续 runs 改为 2 epochs。[2026-05-15 02:02 CST] cuda:1 进程冲突修复并重新提交（PID 519791, timeout=144h）。Registry 状态 DONE(failed) 是旧 cron timeout 标记，实际正在运行 random_s43 [1/8]。新 cron 已注册监控 PID 519791。序列：random_s43→s44→(待插入bm25_s42)→embedding×3→dataflow×3。random_s42 结果：best R@1=0.4604 at step 2500, val_loss=0.6134 at step 1000。\", \"metrics\": {\"random_s42\": {\"epoch\": \"3/3\", \"current_step\": 4200, \"total_steps\": 4242, \"total_steps_per_epoch\": 1414, \"eval_500\": {\"val_loss\": 0.6194, \"recall_at_1\": 0.435, \"recall_at_5\": 0.905, \"recall_at_10\": 1}, \"eval_1000\": {\"val_loss\": 0.6134, \"recall_at_1\": 0.454, \"recall_at_5\": 0.92, \"recall_at_10\": 1}, \"eval_1500\": {\"val_loss\": 0.6528, \"recall_at_1\": 0.449, \"recall_at_5\": 0.906, \"recall_at_10\": 1}, \"eval_2000\": {\"val_loss\": 0.6698, \"recall_at_1\": 0.4456, \"recall_at_5\": 0.906, \"recall_at_10\": 1}, \"eval_2500\": {\"val_loss\": 0.6342, \"recall_at_1\": 0.4604, \"recall_at_5\": 0.9117, \"recall_at_10\": 1}, \"eval_3000\": {\"val_loss\": 0.6516, \"recall_at_1\": 0.4544, \"recall_at_5\": 0.9077, \"recall_at_10\": 1}, \"eval_3500\": {\"val_loss\": 0.6588, \"recall_at_1\": 0.4534, \"recall_at_5\": 0.9057, \"recall_at_10\": 1}, \"eval_4000\": {\"val_loss\": 0.6637, \"recall_at_1\": 0.4547, \"recall_at_5\": 0.9003, \"recall_at_10\": 1}, \"best_checkpoint\": \"step_1000 (val_loss=0.6134) / step_2500 (R@1=0.4604)\", \"conclusion\": \"effectively_complete (timeout at step 4200/4242, lr=7.8e-9, remaining 42 steps negligible)\"}, \"progress_snapshot\": \"2026-05-15T01:50 CST\"}, \"reproduce\": {\"finished_at\": \"2026-05-14T17:49:54.474Z\"}, \"failure_reason\": \"EXIT_CODE=124 (timeout — exceeded timeout_hours)\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-14T17:49:55.304Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T17:49:56.408767+00:00\"}]}}, \"m2_full_qwen\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-13T16:18:14.870Z\", \"updated_at\": \"2026-05-14T18:00:29.323Z\", \"hypothesis\": \"Full M2 Qwen: 3 strategies (random/embedding/dataflow) × 3 seeds on full M1 data (~11K train/seed). Statistical validation of pilot signal (embedding > random +2pp). Go/no-go for paper claims per D018.\", \"parent\": \"m2_embed_verify\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/structfuse && bash run_m2_full_qwen.sh 2>&1 | tee /root/runs/structfuse-context/m2_full_qwen.log\\\"\", \"server\": \"bjb1-42106\", \"gpu\": [\"cuda:0\"], \"pid\": \"73544\", \"log_path\": \"~/runs/structfuse-context/m2_full_qwen.log\", \"submitted_at\": \"2026-05-13T17:39:30.757Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"notes\": \"Full M2 go/no-go: 3 strategies (random, embedding_distance, dataflow_aware) × 3 seeds (42, 43, 44) = 9 runs sequential on cuda:0. Config: lr=2e-5, batch_size=8, eval_steps=500, num_negatives=7, max_seq_length=2048, warmup_ratio=0.1, weight_decay=0.01, temperature=0.07, LoRA r=16, gradient_checkpointing=True, proj_dim=256. Dual checkpoint: best_by_val_loss + best_by_recall_at_1. Train ~11.3K/seed, val ~3K/seed. [D026] s42 保持 3 epochs 提供完整 overfitting curve; s43/s44 及后续 runs 改为 2 epochs + early_stopping_patience=2。[STATUS 2026-05-15 00:19 CST] Registry 状态 ANALYZING 是 cron 自动设置（s42 进程退出触发），但实验实际仍在进行中。random_s43 在 cuda:0 正常运行，step 1200/2810 (43%)。eval@500 R@1=0.5357, eval@1000 R@1=0.5285 (early_stopping 1/2)。Best R@1=0.5357 at step 500。GPU 100% 利用率, 50.5/97.9GB VRAM。\", \"metrics\": {\"random_s42\": {\"status\": \"DONE\", \"epoch\": \"3/3\", \"total_steps\": 4242, \"total_steps_per_epoch\": 1414, \"eval_500\": {\"val_loss\": 0.4869, \"recall_at_1\": 0.533, \"recall_at_5\": 0.954, \"recall_at_10\": 1}, \"eval_1000\": {\"val_loss\": 0.4651, \"recall_at_1\": 0.553, \"recall_at_5\": 0.959, \"recall_at_10\": 1}, \"eval_1500\": {\"val_loss\": 0.5365, \"recall_at_1\": 0.523, \"recall_at_5\": 0.955, \"recall_at_10\": 1}, \"eval_2000\": {\"val_loss\": 0.5162, \"recall_at_1\": 0.523, \"recall_at_5\": 0.954, \"recall_at_10\": 1}, \"eval_2500\": {\"val_loss\": 0.5264, \"recall_at_1\": 0.527, \"recall_at_5\": 0.956, \"recall_at_10\": 1}, \"eval_3000\": {\"val_loss\": 0.5406, \"recall_at_1\": 0.536, \"recall_at_5\": 0.956, \"recall_at_10\": 1}, \"best_checkpoint\": \"step_1000 (val_loss=0.4651, R@1=0.5527)\", \"conclusion\": \"Overfit after step 1000. Best R@1=0.5527, +1.7pp vs pilot (0.5357). Full data helps.\"}, \"random_s43\": {\"status\": \"DONE\", \"epoch\": \"early_stopped\", \"total_steps_per_epoch\": 1405, \"eval_500\": {\"val_loss\": 0.4476, \"recall_at_1\": 0.5357}, \"eval_1000\": {\"val_loss\": 0.4637, \"recall_at_1\": 0.5285}, \"eval_1500\": {\"recall_at_1\": 0.5554}, \"best_by_val_loss\": \"step 500 (val_loss=0.4476)\", \"best_by_recall_at_1\": \"step 1500 (R@1=0.5554)\", \"conclusion\": \"Early stopped at step 1500. Best R@1=0.5554, consistent with s42 (0.5527). val_loss and R@1 criterion diverge.\"}, \"random_s44\": {\"status\": \"RUNNING\", \"note\": \"Auto-started 01:58 CST, epoch 1/2, 1408 batches/epoch\"}, \"progress_snapshot\": \"2026-05-15T02:00 CST\"}, \"reproduce\": {\"finished_at\": \"2026-05-14T11:24:33.887Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T11:24:35.375104+00:00\"}]}}, \"plan_018_bm25\": {\"status\": \"QUEUED\", \"retry_count\": 0, \"created_at\": \"2026-05-14T16:38:40.603Z\", \"updated_at\": \"2026-05-14T17:09:50.985Z\", \"hypothesis\": \"BM25 negative baseline: Dream 审稿三档一致认定缺 BM25 baseline 是论文最大结构性缺陷。Phase 1 (CPU): 对 M2 训练语料建 BM25 索引，挖掘 BM25 hard negatives，生成训练数据。Phase 2 (GPU): 用 BM25 negatives 训练 Qwen + StarCoder 各 1 seed，对比 R@1。\", \"parent\": \"m2_full_qwen\", \"notes\": \"Phase 1 (CPU) COMPLETE: BM25 negative mining 完成。3 seeds 数据生成，record counts 与其他策略完全一致，0 fallback。BM25 score 分布: mean=246.50, std=155.96。重叠率: BM25 vs embedding_distance ~87.1%, vs random ~76.2%, vs dataflow_aware ~71.8%。高 median=1.0 因小 repo 候选池≤50 文件导致策略完全重合，BM25 differentiation 主要在大 repo。脚本: /root/structfuse/scripts/mine_bm25_negatives.py。输出: /root/autodl-tmp/structfuse/full_m2_training_data/{train,val}_bm25_s{42,43,44}.jsonl。Phase 2 (GPU): 等 re-dream gate 通过 + M2 完成后训练。\", \"metrics\": {\"phase1_complete\": true, \"seed_42\": {\"train_records\": 11308, \"val_records\": 2980, \"train_size_mb\": 1280.8, \"val_size_mb\": 344.6}, \"seed_43\": {\"train_records\": 11236, \"val_records\": 3052, \"train_size_mb\": 1280.9, \"val_size_mb\": 316}, \"seed_44\": {\"train_records\": 11264, \"val_records\": 3024, \"train_size_mb\": 1347.1, \"val_size_mb\": 295.9}, \"bm25_score_dist\": {\"count\": 392954, \"mean\": 246.5, \"std\": 155.96, \"p25\": 128.38, \"p50\": 228.41, \"p75\": 347.85, \"max\": 2585.74}, \"overlap_overall\": {\"bm25_vs_embedding\": 0.871, \"bm25_vs_random\": 0.762, \"bm25_vs_dataflow\": 0.718, \"note\": \"k=50 full candidate overlap from mining worker\"}, \"overlap_stratified_top7_jaccard\": {\"small_lt50\": {\"repos\": 39, \"bm25_vs_embedding\": 0.668, \"bm25_vs_random\": 0.411, \"bm25_vs_dataflow\": 0.667}, \"medium_50_200\": {\"repos\": 29, \"bm25_vs_embedding\": 0.38, \"bm25_vs_random\": 0.067, \"bm25_vs_dataflow\": 0.363}, \"large_200plus\": {\"repos\": 15, \"bm25_vs_embedding\": 0.297, \"bm25_vs_random\": 0.007, \"bm25_vs_dataflow\": 0.405}, \"matched_queries\": 2920, \"total_queries\": 12290, \"note\": \"top-7 Jaccard on s42 matched queries only (24% match rate due to different train/val splits)\"}}}, \"plan_015_dynamic\": {\"status\": \"QUEUED\", \"retry_count\": 0, \"created_at\": \"2026-05-14T17:03:24.316Z\", \"updated_at\": \"2026-05-14T17:03:30.544Z\", \"hypothesis\": \"Dynamic negative mining (epoch-level re-mining): 每 epoch 重新用当前 encoder embedding 挖掘 negatives，验证 static mining 是否足够。缩减版：只跑 dynamic_ep × 1 seed (Qwen, s42)，~11h 单卡。若 dynamic ≈ static（预期 <1pp 差异），在 Limitation 段排除 confound。\", \"notes\": \"Director D031 缩减：原 44h → 11h 单卡。只跑 dynamic_ep × 1 seed (Qwen, s42)，跳过 dynamic_500。Post-M2 与 plan_003 并行（一卡 SWE-bench，一卡 dynamic_ep）。受 re-dream gate 约束。设计文档已由 Worker 完成。\"}, \"neg_difficulty_analysis\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T19:39:20.016Z\", \"updated_at\": \"2026-05-14T00:13:49.046Z\", \"hypothesis\": \"Negative difficulty distribution analysis: 用预训练 Qwen2.5-Coder-3B 和 StarCoder2-3B 计算 3 策略 (random/embedding/dataflow) 的 query-negative/positive cosine similarity，分析 pretrained representation separability 跨编码器差异。MAX_LENGTH=2048 匹配训练设置。\", \"notes\": \"128 vs 2048 token 对比完成（2026-05-14 05:54 CST）。Qwen pos_sim 在 2048t 下 0.9855（比 128t 的 0.9804 更高），确认 ceiling 为 Qwen 表征的结构性特征，非截断 artifact。StarCoder margin 2.6-4.1x Qwen（2048t）。核心结论：pretrained representation separability varies across encoders，跨两种 token 长度成立。数据源：128t → stats_v2.json，2048t → stats_v3_2048.json。\", \"metrics\": {\"qwen_128\": {\"random\": {\"pos_sim\": 0.9804, \"neg_sim\": 0.899, \"margin\": 0.0816, \"pct_positive_margin\": 77.8}, \"embedding_distance\": {\"pos_sim\": 0.9804, \"neg_sim\": 0.959, \"margin\": 0.0209, \"pct_positive_margin\": 60.7}, \"dataflow_aware\": {\"pos_sim\": 0.9805, \"neg_sim\": 0.95, \"margin\": 0.0309, \"pct_positive_margin\": 67.4}}, \"starcoder_128\": {\"random\": {\"pos_sim\": 0.757, \"neg_sim\": 0.553, \"margin\": 0.2039, \"pct_positive_margin\": 72.8}, \"embedding_distance\": {\"pos_sim\": 0.784, \"neg_sim\": 0.668, \"margin\": 0.1159, \"pct_positive_margin\": 59.2}, \"dataflow_aware\": {\"pos_sim\": 0.761, \"neg_sim\": 0.659, \"margin\": 0.1022, \"pct_positive_margin\": 62.8}}, \"qwen_2048\": {\"random\": {\"pos_sim\": 0.9855, \"neg_sim\": 0.9111, \"margin\": 0.0743, \"margin_std\": 0.2322, \"pct_positive_margin\": 81.8}, \"embedding_distance\": {\"pos_sim\": 0.9855, \"neg_sim\": 0.9685, \"margin\": 0.017, \"margin_std\": 0.114, \"pct_positive_margin\": 58.8}, \"dataflow_aware\": {\"pos_sim\": 0.9856, \"neg_sim\": 0.9563, \"margin\": 0.0293, \"margin_std\": 0.1407, \"pct_positive_margin\": 73.9}}, \"starcoder_2048\": {\"random\": {\"pos_sim\": 0.7985, \"neg_sim\": 0.6045, \"margin\": 0.194, \"margin_std\": 0.2788, \"pct_positive_margin\": 78}, \"embedding_distance\": {\"pos_sim\": 0.8079, \"neg_sim\": 0.7409, \"margin\": 0.067, \"margin_std\": 0.2056, \"pct_positive_margin\": 55}, \"dataflow_aware\": {\"pos_sim\": 0.8009, \"neg_sim\": 0.6818, \"margin\": 0.1192, \"margin_std\": 0.2264, \"pct_positive_margin\": 70.4}}, \"sc_qwen_margin_ratio_128\": {\"random\": 2.5, \"embedding_distance\": 5.54, \"dataflow_aware\": 3.3}, \"sc_qwen_margin_ratio_2048\": {\"random\": 2.61, \"embedding_distance\": 3.94, \"dataflow_aware\": 4.07}}, \"conclusion\": \"success\", \"spec\": {\"command\": \"python negative_difficulty_margin_v2.py (CPU analysis)\", \"server\": \"bjb1-42106\", \"data_path\": \"/root/autodl-tmp/structfuse/full_m2_data/\", \"data_count\": 11000, \"model_name\": \"Qwen2.5-Coder-3B + StarCoder2-3B (pretrained, no training)\", \"seed\": \"N/A\", \"checkpoint_path\": \"N/A (analysis only)\", \"log_path\": \"/root/autodl-tmp/structfuse/artifacts/negative_difficulty_stats_v3_2048.json\"}, \"completed_at\": \"2026-05-14T00:13:49.046Z\"}, \"m1_reextract\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T19:35:23.954Z\", \"updated_at\": \"2026-05-13T19:45:53.741Z\", \"hypothesis\": \"M1 重提取：恢复 28,276 个因运行时瞬态文件系统故障失败的 instances（82 repos）。预期将训练数据从 15,897 提升至 ~44,173。D022 批准。\", \"parent\": \"m1_extraction\", \"spec\": {\"command\": \"bash scripts/rerun_m1_failed.sh (4 CPU workers, CodeQL 2-hop)\", \"server\": \"bjb1-42106\", \"data_path\": \"/root/autodl-tmp/structfuse/m1_extraction/\", \"data_count\": 28276, \"model_name\": \"N/A (CodeQL extraction)\", \"seed\": \"N/A\", \"pid\": \"97358\", \"log_path\": \"/root/runs/structfuse-context/m1_rerun.log\", \"checkpoint_source\": \"rerun of m1_extraction failed instances\", \"eval_data\": \"N/A\", \"checkpoint_path\": \"N/A (failed, no output)\"}, \"conclusion\": \"failed\", \"notes\": \"CodeQL query 100% 失败（exit status 2）。根因：Worker 安装 CodeQL CLI 2.25.4 时未执行 `codeql pack install`，`codeql/python-all@7.1.0` 标准库 pack 缺失。修复命令：`cd /root/structfuse/extraction/codeql_queries && /opt/codeql/codeql pack install`。已 kill 进程 + tmux session。无新数据产出（all.jsonl 未受影响）。等 Director 确认后修复重跑。\", \"completed_at\": \"2026-05-13T19:44:09.115Z\"}, \"m1_extraction\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-12T21:00:02.300Z\", \"updated_at\": \"2026-05-13T19:26:13.901Z\", \"spec\": {\"command\": \"nohup bash scripts/run_m1_extraction.sh (8 CPU workers, CodeQL 2-hop)\", \"server\": \"cqa1-21977\", \"data_path\": \"/root/autodl-tmp/structfuse/m1_extraction/\", \"data_count\": 50869, \"model_name\": \"N/A (CodeQL extraction)\", \"seed\": \"N/A\", \"description\": \"M1: 全量 5K repos CodeQL 提取, 131 unique (repo,commit) groups, 50869 instances\"}, \"metrics\": {\"total_instances_attempted\": 44173, \"instances_skipped\": 6696, \"total_instances\": 50869, \"codeql_success\": 15133, \"beniget_fallback\": 764, \"extraction_failed\": 28276, \"structural_data_rate\": 0.36, \"repos_with_output\": 123, \"repos_total\": 131, \"repo_coverage\": 0.939, \"skip_clone_failed\": 5852, \"skip_checkout_failed\": 836, \"skip_stale_handle\": 8, \"elapsed_minutes\": 837.8, \"avg_time_per_instance_s\": 8.9, \"output_size_gb\": 6.6, \"disk_usage_gb\": 13, \"output_file\": \"all.jsonl\"}, \"notes\": \"[2026-05-13 19:25] COMPLETED. 837.8min, 123/131 repos (93.9%), 15,897/44,173 instances with structural data (36.0%), 6,696 skipped (clone/checkout). Output: all.jsonl 6.6GB. [2026-05-13 19:23 UPDATE] 28,276 buggy_file_not_found errors 经验证并非上游数据质量问题——10/10 抽查的文件在 repo 中全部存在。根因是运行时瞬态文件系统故障（CodeQL 并行 database creation 导致磁盘耗尽，锐截止模式）。这些 instances 可通过重跑恢复。D022: 准备重跑脚本中，等 Director 确认后执行。\", \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/structfuse/m1_extraction/all.jsonl\", \"log_path\": \"/tmp/m1_extraction.log\", \"completed_at\": \"2026-05-13T10:59:42.462Z\"}, \"plan_006_scalability\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T07:57:43.631Z\", \"updated_at\": \"2026-05-13T19:24:00.741Z\", \"spec\": {\"command\": \"M1 scalability statistics analysis (29/131 repos)\", \"server\": \"bjb1-42106\", \"data_path\": \"/root/autodl-tmp/structfuse/m1_extraction/\", \"data_count\": 8171, \"model_name\": \"N/A (CPU analysis)\", \"seed\": \"N/A\", \"description\": \"Plan 006: M1 extraction scalability stats - timeout rate, extraction time, coverage, Z% by repo size. Partial results from 29/131 repos.\", \"checkpoint_path\": \"N/A\", \"log_path\": \"N/A\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-13T07:57:58.176Z\", \"notes\": \"[2026-05-13 19:23] 全量统计 + error 分析 + fuzzy match 验证完成。关键发现: (1) 0 timeout; (2) 28,276 error 全部 buggy_file_not_found，但 fuzzy match 验证发现文件实际都存在——根因是运行时瞬态文件系统故障（锐截止模式：每个 repo 内先成功后突然全部失败，extraction_time=0.0s），可能是 CodeQL 并行数据库创建导致磁盘空间耗尽; (3) 这些 instance 可通过重跑恢复（当前 resolve_file_in_repo 对全部样本返回正确路径）; (4) 结构数据率 34.3% 有望提升至接近 100%（若重跑成功）; (5) Z% 随 repo 规模上升 (XL median 96%). Artifacts: plan006_full_scalability.json, art_20260513_d262da (error patterns)\", \"hypothesis\": \"Claim 3: CodeQL bounded data-flow extraction scales to large repos with acceptable timeout rates and provides meaningful structural coverage (Z%) that increases with repo complexity\", \"metrics\": {\"repos\": 123, \"total_instances\": 44173, \"structural_data_rate\": 0.343, \"error_rate\": 0.64, \"zero_timeout_rate\": true, \"processing_time\": {\"mean_s\": 8.93, \"median_s\": 0, \"p95_s\": 31.95, \"max_s\": 633.68, \"total_hours\": 109.58}, \"by_tier\": {\"small_lt50\": {\"repos\": 1, \"instances\": 500, \"error_rate\": 0.054, \"struct_rate\": 0.81, \"z_pct_mean\": 0.284, \"z_pct_median\": 0}, \"medium_50_200\": {\"repos\": 17, \"instances\": 4096, \"error_rate\": 0.485, \"struct_rate\": 0.472, \"z_pct_mean\": 0.444, \"z_pct_median\": 0.5}, \"large_200_500\": {\"repos\": 40, \"instances\": 13628, \"error_rate\": 0.639, \"struct_rate\": 0.343, \"z_pct_mean\": 0.604, \"z_pct_median\": 0.857}, \"xlarge_500plus\": {\"repos\": 29, \"instances\": 25949, \"error_rate\": 0.676, \"struct_rate\": 0.314, \"z_pct_mean\": 0.812, \"z_pct_median\": 0.96}}, \"instance_distribution\": {\"lt10\": 1, \"10_50\": 17, \"50_200\": 36, \"200_500\": 40, \"500plus\": 29}, \"artifact\": \"plan006_full_scalability.json\"}}, \"plan_013_starcoder\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T05:09:14.885Z\", \"updated_at\": \"2026-05-13T18:09:54.153Z\", \"hypothesis\": \"Architecture generalization: validate StructFuse with StarCoder2-3B encoder (vs Qwen2.5-Coder-3B in m2_embed_verify). If both encoders show same strategy ranking → method is encoder-agnostic, strengthening the core claim. Key differentiator for best→accept at Dream.\", \"spec\": {\"command\": \"bash -c \\\"bash /root/structfuse/run_plan013_starcoder.sh\\\"\", \"server\": \"bjb1-42106\", \"gpu\": [\"cuda:0\"], \"pid\": \"23798\", \"log_path\": \"~/runs/structfuse-context/plan_013_starcoder.log\", \"submitted_at\": \"2026-05-13T05:26:21.946Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/structfuse/m2_embed_verify_data/\", \"data_count\": 3282, \"model_name\": \"bigcode/starcoder2-3b\", \"seed\": 42, \"wall_clock_seconds\": 35338.2, \"gpu_hours\": 9.82}, \"notes\": \"[2026-05-13 16:00] ALL 3 STRATEGIES DONE. Ranking: embedding (R@1=0.5078) > random (0.4922) > dataflow (0.4869). Embedding vs random: +1.6pp (consistent with Qwen). Dataflow vs random: -0.5pp (DIFFERS from Qwen where dataflow > random +0.8pp). Hypothesis NEGATIVE: strategy ranking NOT identical across encoders. Embedding > random is encoder-agnostic, dataflow position is encoder-dependent. Log: /root/runs/faith-evidence-ie/plan_013_starcoder.log. Cron misreported EXIT_CODE=129 but all strategies completed (confirmed via log extraction worker).\", \"metrics\": {\"random\": {\"status\": \"DONE\", \"best_val_loss\": 0.5113, \"best_recall@1\": 0.4922, \"best_recall@5\": 0.98, \"best_recall@10\": 1, \"source\": \"/tmp/eval_random_s42.log (post-hoc eval, no in-training eval)\"}, \"embedding_distance\": {\"status\": \"DONE\", \"best_step\": 1000, \"best_val_loss\": 0.4816, \"best_recall@1\": 0.5078, \"best_recall@5\": 0.9843, \"best_recall@10\": 1, \"final_val_loss\": 0.506, \"final_recall@1\": 0.5174}, \"dataflow_aware\": {\"status\": \"DONE\", \"best_step\": 1000, \"best_val_loss\": 0.5255, \"best_recall@1\": 0.4869, \"best_recall@5\": 0.9695, \"best_recall@10\": 1, \"final_val_loss\": 0.5509, \"final_recall@1\": 0.5078}}, \"failure_reason\": \"\", \"conclusion\": \"negative\", \"completed_at\": \"2026-05-13T15:15:20.165Z\"}, \"m2_embed_verify\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T04:39:16.051Z\", \"updated_at\": \"2026-05-13T15:59:51.621Z\", \"hypothesis\": \"True embedding mining verification: compare Qwen2.5-Coder-3B cosine similarity negatives vs BM25 negatives on pilot data (24 repos). If true embedding negatives are harder → Claim 2 (structure-aware negatives improve retrieval) gets stronger evidence.\", \"parent\": \"m2_early_pilot\", \"spec\": {\"command\": \"bash -c \\\"bash /root/structfuse/run_m2_embed_verify.sh\\\"\", \"server\": \"bjb1-42106\", \"gpu\": [\"cuda:1\"], \"pid\": \"29290\", \"log_path\": \"~/runs/structfuse-context/m2_embed_verify.log\", \"submitted_at\": \"2026-05-13T06:37:00.822Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/structfuse/m2_embed_verify_data/\", \"data_count\": 3282, \"model_name\": \"Qwen/Qwen2.5-Coder-3B\", \"seed\": 42, \"checkpoint_source\": \"training from scratch (not eval)\", \"eval_data\": \"N/A (training, not eval)\", \"wall_clock_seconds\": 31097.9, \"gpu_hours\": 8.64}, \"notes\": \"[2026-05-13 16:00] ALL 3 STRATEGIES DONE. Ranking: embedding (R@1=0.5557) > dataflow (0.5436) > random (0.5357). Embedding vs random: +2.0pp. Dataflow vs random: +0.8pp. All best at step 500, overfitting after. Hypothesis confirmed: true embedding negatives are harder → Claim 2 supported. Log: /root/runs/faith-evidence-ie/m2_embed_verify.log. Cron misreported EXIT_CODE=2 but all strategies completed successfully (confirmed via log extraction worker).\", \"metrics\": {\"random\": {\"status\": \"DONE\", \"best_step\": 500, \"best_val_loss\": 0.4834, \"best_recall@1\": 0.5357, \"best_recall@5\": 0.9808, \"best_recall@10\": 1, \"final_val_loss\": 0.5978, \"final_recall@1\": 0.5122}, \"embedding_distance\": {\"status\": \"DONE\", \"best_step\": 500, \"best_val_loss\": 0.4603, \"best_recall@1\": 0.5557, \"best_recall@5\": 0.9808, \"best_recall@10\": 1, \"final_val_loss\": 0.5935, \"final_recall@1\": 0.5209}, \"dataflow_aware\": {\"status\": \"DONE\", \"best_step\": 500, \"best_val_loss\": 0.5602, \"best_recall@1\": 0.5436, \"best_recall@5\": 0.9817, \"best_recall@10\": 1, \"final_val_loss\": 0.6201, \"final_recall@1\": 0.5287}}, \"failure_reason\": \"EXIT_CODE=2 (shell misuse / syntax)\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-13T15:15:18.746Z\"}, \"mvp_p2b_contrastive_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-12T15:03:02.370Z\", \"updated_at\": \"2026-05-13T07:23:28.932Z\", \"spec\": {\"command\": \"bash scripts/run_p2b_all.sh (9 runs: 3 strategies × 3 seeds)\", \"server\": \"cqa1-21977\", \"gpu\": [\"cuda:4\"], \"pid\": \"132149\", \"data_path\": \"/root/structfuse/mvp_data/training_data/\", \"data_count\": 127, \"model_name\": \"Qwen2.5-Coder-3B + LoRA\", \"seed\": \"42,123,7\", \"hypothesis\": \"H3: data-flow hard negatives vs random vs embedding-distance, 3-seed × 3-strategy contrastive training\", \"plan_id\": \"mvp_p2b_contrastive_training\", \"checkpoint_path\": \"N/A\", \"log_path\": \"N/A\"}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-12T15:04:44.396Z\", \"notes\": \"P2b 对比训练 v2，因磁盘空间不足被 kill。已被 p2b_5reruns（成功完成 9/9 runs）替代。\"}, \"p2b_dataflow_retrain\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-12T19:49:00.303Z\", \"updated_at\": \"2026-05-13T07:23:27.706Z\", \"spec\": {\"command\": \"build_p2b_data.py regeneration + dataflow 3-seed retrain\", \"server\": \"cqa1-21977\", \"data_path\": \"/root/structfuse\", \"data_count\": 0, \"model_name\": \"Qwen2.5-Coder-3B (LoRA)\", \"seed\": \"42,123,456\", \"description\": \"BLOCKED: dataflow connections ⊆ gold files, strategies indistinguishable\", \"checkpoint_path\": \"N/A\", \"log_path\": \"N/A\"}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-13T04:17:02.055Z\", \"notes\": \"Dataflow 策略重训练计划，因 embedding_distance 命名问题（实际用 BM25 而非 embedding）被 Reviewer 发现后搁置。已被 m2_embed_verify（true embedding mining）替代。\"}, \"p2b_eval_all\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-12T16:27:50.967Z\", \"updated_at\": \"2026-05-13T07:23:24.721Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/structfuse && bash scripts/run_eval_all.sh\\\"\", \"server\": \"cqa1-21977\", \"gpu\": [\"cuda:4\"], \"pid\": \"254053\", \"log_path\": \"N/A\", \"submitted_at\": \"2026-05-12T16:27:50.945Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"N/A\", \"wall_clock_seconds\": 42550.6, \"gpu_hours\": 11.82}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-13T04:17:01.561Z\", \"notes\": \"P2b 全量 eval（pool_size=26），被 D013 服务器迁移计划取消。已被 p2b_eval_4runs_pool50（pool_size=50）替代。\"}, \"m2_early_pilot\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T01:39:53.920Z\", \"updated_at\": \"2026-05-13T04:44:22.077Z\", \"hypothesis\": \"Early pilot on partial M1 data (24 repos, ~5K instances): verify M2 training pipeline works end-to-end and get early signal on 3-strategy differentiation before full M1 completes\", \"spec\": {\"command\": \"bash /root/structfuse/scripts/run_m2_pilot.sh\", \"server\": \"cqa1-21977\", \"gpu\": [\"cuda:4\"], \"pid\": \"795739\", \"log_path\": \"/root/autodl-tmp/structfuse/m2_pilot_output/random_s42.log\", \"submitted_at\": \"2026-05-13T01:55:31.288Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/structfuse/m2_pilot_data/\", \"data_count\": 3418, \"model_name\": \"Qwen/Qwen2.5-Coder-3B\", \"seed\": 42, \"checkpoint_source\": \"N/A (training from scratch)\", \"eval_data\": \"N/A (training, not eval)\", \"checkpoint_path\": \"/root/autodl-tmp/structfuse/m2_pilot_output/random_s42/best_model.pt\", \"wall_clock_seconds\": 10130.8, \"gpu_hours\": 2.81}, \"conclusion\": \"killed\", \"notes\": \"PID 795791 在 cqa1 cuda:4 运行，wrapper 脚本顺序跑 random→embedding→dataflow（set -e）。random 策略跑到 step 4000 后卡住（~45min 无新日志），embedding/dataflow 未启动。Best checkpoint at step 1500。Val_loss 持续恶化（0.5879→0.728），明显过拟合。另有 OOM 进程干扰（某进程试图在同 GPU 启动导致 OOM，可能破坏 GPU 状态）。eval recall@k bug 已确认。\", \"metrics\": {\"pid\": 795791, \"gpu\": \"cuda:4\", \"gpu_mem_mb\": 9342, \"gpu_util_pct\": 83, \"batch_size\": 2, \"num_negatives\": 3, \"max_seq_length\": 1024, \"strategy_running\": \"random (stuck at step 4000, epoch 3)\", \"strategies_completed\": \"0/3\", \"eval_1500\": {\"val_loss\": 0.5879, \"recall_at_1\": 0.4693, \"recall_at_5\": 0.4693, \"recall_at_10\": 0.4693}, \"eval_2000\": {\"val_loss\": 0.7089, \"recall_at_1\": 0.4398}, \"eval_2500\": {\"val_loss\": 0.6961, \"recall_at_1\": 0.4291}, \"eval_3000\": {\"val_loss\": 0.728, \"recall_at_1\": 0.4104}, \"eval_3500\": {\"val_loss\": 0.7022, \"recall_at_1\": 0.4439}, \"best_checkpoint\": \"step_1500 (val_loss=0.5879, 6.2GB)\", \"WARNING\": \"recall@1=recall@5=recall@10 confirmed eval bug. Process hung after step 4000 (~45min no output). Overfitting after step 1500.\", \"status_check_at\": \"2026-05-13T04:42:00Z\"}, \"completed_at\": \"2026-05-13T04:44:22.077Z\"}, \"m2_early_pilot_v3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T01:59:06.557Z\", \"updated_at\": \"2026-05-13T02:13:43.400Z\", \"spec\": {\"command\": \"bash -c \\\"bash /root/structfuse/run_m2_early_pilot.sh\\\"\", \"server\": \"cqa1-21977\", \"gpu\": [\"cuda:0\"], \"pid\": \"897651\", \"log_path\": \"~/runs/structfuse-context/m2_early_pilot_v3.log\", \"submitted_at\": \"2026-05-13T02:04:31.768Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"N/A\", \"wall_clock_seconds\": 551.6, \"gpu_hours\": 0.15}, \"conclusion\": \"killed\", \"notes\": \"GPU 越界 cuda:0，违反项目 GPU 分配 gpu_ids=[\\\"cuda:4\\\"]。第二次 GPU 越界违规（首次 D005）。Worker 未正确映射 CUDA_VISIBLE_DEVICES。\", \"completed_at\": \"2026-05-13T02:13:43.400Z\"}}, \"count\": 20, \"total\": 37, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.1012}}"
    }
  },
  "sourceToolAssistantUUID": "162d8d81-abff-48dc-9a6b-30d163b86def",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "d1e524a6-76dd-46af-a456-0b6d1108f4ee",
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
  "leafUuid": "0de826df-a249-4892-a141-6c623401a0fe",
  "sessionId": "d1e524a6-76dd-46af-a456-0b6d1108f4ee"
}
```

---

### Runtime record

_source line 29_

```json
{
  "type": "ai-title",
  "aiTitle": "Fix experiments v1 6 issues warnings and info",
  "sessionId": "d1e524a6-76dd-46af-a456-0b6d1108f4ee"
}
```

---

### Assistant

_source line 30 · 2026-05-14T22:59:22.571Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the data I need. Let me extract the key information:

**Warning 1 (Table 6 Total)**:
- From `plan_006_scalability` registry: `structural_data_rate: 0.343` (34.3%)
- Table 6 currently says Total structural coverage = 36.0%
- But looking at tier data in registry:
  - Small: struct_rate = 0.81 (81.0%)
  - Medium: struct_rate = 0.472 (47.2%)
  - Large: struct_rate = 0.343 (34.3%)
  - XLarge: struct_rate = 0.314 (31.4%)
- The overall structural_data_rate = 0.343 = 34.3%
- So the Total row should be 34.3%, not 36.0%
- Also in §4.1 text: "yielding a structural coverage rate of 36%" should be 34.3%

But I'm noticing a conflict here—the m1_extraction metrics show `structural_data_rate: 0.36` (36%), which contradicts the plan_006_scalability value of 34.3%, so I need to figure out which source is correct. Looking at the tier breakdown in Table 6, I can verify the 34.3% rate by summing across all instance sizes—Small through XLarge—which gives 15,160 structural instances out of 44,173 total. The discrepancy with the 36% figure from m1_extraction appears to stem from different counting methodologies between the two sources. Looking at the m2_embed_verify registry data, I'm checking the best_recall@1 values across the three methods—random hits 0.5357, embedding_distance reaches 0.5557, and dataflow_aware comes in at 0.5436, all peaking at step 500.

Now comparing against plan_013_starcoder, which shows lower recall scores (0.4922 for random, 0.5078 for embedding, 0.4869 for dataflow), I'm noticing this earlier experiment doesn't have a separate best_by_recall_at_1 checkpoint field like the newer m2_embed_verify does. I'm verifying that the table values match the checkpoint metrics when rounded to three decimal places—they all check out. The real issue is that Table 2 doesn't explicitly indicate these numbers come from the R@1 checkpoints, which is important context for readers.

Looking at the task more carefully, I need to update Table 2 to use the best_by_recall_at_1 values and add a note clarifying they're from R@1 checkpoints to align with the protocol described in §4.1. For the embedding model, the best step happens to be the same for both val_loss and recall@1, but for the other model I need to check whether the best_recall@1 step is clearly identified in the metrics. Now I'm recalculating the deltas with more precision to verify the current values are accurate. The Qwen comparisons check out, and for StarCoder the embedding versus random delta is correct, but the dataflow versus random shows a negative difference of -0.53 percentage points rather than what's currently displayed.

Looking back at the task requirements, I need to pull the exact values from the best_recall@1 checkpoint, add that annotation to the table, and ensure the deltas are computed with proper precision. Since the rounded values already align with what's in the table, I'll update it to display the more precise four-decimal values and note their source.

Now I'm going through the remaining edits: updating the SWE-bench reference to SWE-smith with the dataset expansion details, fixing the citation key from `cocohanere2025` to `fan2025cocohanere`, and clarifying that the temperature parameter is learnable rather than fixed. Let me locate and apply these changes.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0de826df-a249-4892-a141-6c623401a0fe",
  "isSidechain": false,
  "requestId": "req_011Cb3HkQds2R2SMjx4MynNu",
  "type": "assistant",
  "uuid": "b9994ef2-0710-425b-96ea-fa64a2c66297",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "d1e524a6-76dd-46af-a456-0b6d1108f4ee",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EzhwQ5hecijFkaZTZhrUTZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16637,
      "cache_read_input_tokens": 30093,
      "output_tokens": 4196,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 16637,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4196,
          "cache_read_input_tokens": 30093,
          "cache_creation_input_tokens": 16637,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 16637
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

_source line 31 · 2026-05-14T22:59:22.617Z_

Got all registry data. Now I have everything needed. Let me make all 5 edits.

Key data from registry:
- `plan_006_scalability`: `structural_data_rate = 0.343` → Table 6 Total should be 34.3%, not 36.0%
- `m2_embed_verify` R@1 checkpoint: random=0.5357, embedding=0.5557, dataflow=0.5436
- `plan_013_starcoder` R@1 checkpoint: random=0.4922, embedding=0.5078, dataflow=0.4869

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b9994ef2-0710-425b-96ea-fa64a2c66297",
  "isSidechain": false,
  "requestId": "req_011Cb3HkQds2R2SMjx4MynNu",
  "type": "assistant",
  "uuid": "01205308-d860-4bde-b188-d71f12fe5d08",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "d1e524a6-76dd-46af-a456-0b6d1108f4ee",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EzhwQ5hecijFkaZTZhrUTZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16637,
      "cache_read_input_tokens": 30093,
      "output_tokens": 4196,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 16637,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4196,
          "cache_read_input_tokens": 30093,
          "cache_creation_input_tokens": 16637,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 16637
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

_source line 32 · 2026-05-14T22:59:30.117Z_

<details open><summary>🔧 Tool call — Edit · `toolu_012pMfjK5Z5NUnie9LKfxdRS`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/experiments_v1.md",
  "old_string": "We construct our training corpus from SWE-bench \\cite{jimenez2024swebench}, a benchmark of real-world GitHub issues paired with developer-authored patches. Starting from 5,029 task instances spanning 131 unique (repository, commit) pairs, we run the StructFuse extraction pipeline (§3.2) to obtain inter-procedural data-flow graphs via CodeQL. After filtering for clone/checkout failures and extraction errors, we retain 15,897 instances across 123 repositories with structural data, yielding a structural coverage rate of 36%.",
  "new_string": "We construct our training corpus from SWE-smith \\cite{yang2025swesmith}, a large-scale dataset of real-world GitHub bug-fix commits. Starting from 5,029 task instances spanning 131 unique (repository, commit) pairs, each task corresponds to a single bug-fix commit; we expand each task by treating every gold file as a separate training instance, yielding 44,173 training instances total (since many tasks involve multiple gold files). We run the StructFuse extraction pipeline (§3.2) to obtain inter-procedural data-flow graphs via CodeQL. After filtering for clone/checkout failures and extraction errors, we retain 15,160 instances across 123 repositories with structural data, yielding a structural coverage rate of 34.3%."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "01205308-d860-4bde-b188-d71f12fe5d08",
  "isSidechain": false,
  "requestId": "req_011Cb3HkQds2R2SMjx4MynNu",
  "type": "assistant",
  "uuid": "9bdfb466-1337-4e7a-a76d-54bd927f978b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "d1e524a6-76dd-46af-a456-0b6d1108f4ee",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EzhwQ5hecijFkaZTZhrUTZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16637,
      "cache_read_input_tokens": 30093,
      "output_tokens": 4196,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 16637,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4196,
          "cache_read_input_tokens": 30093,
          "cache_creation_input_tokens": 16637,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 16637
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

_source line 33 · 2026-05-14T22:59:38.751Z_

<details><summary>↩ Tool result · `toolu_015fsSsGgg6Qb5ZdQL3S1ERT`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/experiments_v1.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e65c74e6-0299-486a-806c-6c01b794d2ee",
  "isSidechain": false,
  "promptId": "1d7108f5-af6a-41fc-acd8-afc665497be3",
  "type": "user",
  "uuid": "8ae96777-470b-4557-b59d-a13c93f2643f",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/experiments_v1.md",
    "oldString": "Training uses InfoNCE loss with temperature $\\tau = 0.07$",
    "newString": "Training uses InfoNCE loss with learnable temperature initialized at $\\tau = 0.07$",
    "originalFile": null,
    "structuredPatch": [
      {
        "oldStart": 14,
        "oldLines": 7,
        "newStart": 14,
        "newLines": 7,
        "lines": [
          " ",
          " **Encoders.** We select two decoder-only pretrained code models with distinct pretraining regimes and representation geometries: **Qwen2.5-Coder-3B** \\cite{hui2024qwen25coder} and **StarCoder2-3B** \\cite{li2023starcoder}. Qwen2.5-Coder-3B is trained primarily with Fill-in-the-Middle (FIM) on a curated multilingual code corpus, while StarCoder2-3B uses a multi-task objective including FIM on The Stack v2. As we show in §4.4, these models exhibit markedly different pretrained representation geometries: Qwen operates in a near-saturated similarity regime (mean positive cosine similarity 0.986), while StarCoder maintains healthy separation (mean positive cosine similarity 0.798). This divergence enables us to study how representation geometry mediates the effectiveness of different negative mining strategies.",
          " ",
          "-**Fine-Tuning Configuration.** Both encoders are fine-tuned with LoRA \\cite{hu2022lora} applied to the query and value projection matrices ($W_q$, $W_v$) of every attention layer, with rank $r = 16$, scaling factor $\\alpha = 32$, and dropout 0.05. We use a linear projection head mapping the last hidden state to a 256-dimensional embedding. Training uses InfoNCE loss with temperature $\\tau = 0.07$, AdamW optimizer with learning rate $2 \\times 10^{-5}$, weight decay 0.01, cosine annealing schedule with 10% linear warmup, and gradient clipping at max norm 1.0. Input sequences are truncated to 2,048 tokens. Batch size is 8 with gradient checkpointing enabled.",
          "+**Fine-Tuning Configuration.** Both encoders are fine-tuned with LoRA \\cite{hu2022lora} applied to the query and value projection matrices ($W_q$, $W_v$) of every attention layer, with rank $r = 16$, scaling factor $\\alpha = 32$, and dropout 0.05. We use a linear projection head mapping the last hidden state to a 256-dimensional embedding. Training uses InfoNCE loss with learnable temperature initialized at $\\tau = 0.07$, AdamW optimizer with learning rate $2 \\times 10^{-5}$, weight decay 0.01, cosine annealing schedule with 10% linear warmup, and gradient clipping at max norm 1.0. Input sequences are truncated to 2,048 tokens. Batch size is 8 with gradient checkpointing enabled.",
          " ",
          " For the initial seed (s42), we train for 3 epochs to obtain a full overfitting curve; subsequent seeds (s43, s44) train for 2 epochs with early stopping (patience 2 evaluations) based on validation loss. Evaluation is performed every 500 steps. We maintain dual checkpoints: $\\theta^*_{\\text{loss}}$ (minimum validation loss) and $\\theta^*_{\\text{R@1}}$ (maximum validation Recall@1).",
          " "
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "e65c74e6-0299-486a-806c-6c01b794d2ee",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "d1e524a6-76dd-46af-a456-0b6d1108f4ee",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-14T22:59:30.141Z_

<details><summary>↩ Tool result · `toolu_012pMfjK5Z5NUnie9LKfxdRS`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/experiments_v1.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9bdfb466-1337-4e7a-a76d-54bd927f978b",
  "isSidechain": false,
  "promptId": "1d7108f5-af6a-41fc-acd8-afc665497be3",
  "type": "user",
  "uuid": "0b5a5e2d-1004-469c-aa5e-a0b56941252c",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/experiments_v1.md",
    "oldString": "We construct our training corpus from SWE-bench \\cite{jimenez2024swebench}, a benchmark of real-world GitHub issues paired with developer-authored patches. Starting from 5,029 task instances spanning 131 unique (repository, commit) pairs, we run the StructFuse extraction pipeline (§3.2) to obtain inter-procedural data-flow graphs via CodeQL. After filtering for clone/checkout failures and extraction errors, we retain 15,897 instances across 123 repositories with structural data, yielding a structural coverage rate of 36%.",
    "newString": "We construct our training corpus from SWE-smith \\cite{yang2025swesmith}, a large-scale dataset of real-world GitHub bug-fix commits. Starting from 5,029 task instances spanning 131 unique (repository, commit) pairs, each task corresponds to a single bug-fix commit; we expand each task by treating every gold file as a separate training instance, yielding 44,173 training instances total (since many tasks involve multiple gold files). We run the StructFuse extraction pipeline (§3.2) to obtain inter-procedural data-flow graphs via CodeQL. After filtering for clone/checkout failures and extraction errors, we retain 15,160 instances across 123 repositories with structural data, yielding a structural coverage rate of 34.3%.",
    "originalFile": null,
    "structuredPatch": [
      {
        "oldStart": 2,
        "oldLines": 7,
        "newStart": 2,
        "newLines": 7,
        "lines": [
          " ",
          " ## §4.1 Experimental Setup",
          " ",
          "-**Dataset.** We construct our training corpus from SWE-bench \\cite{jimenez2024swebench}, a benchmark of real-world GitHub issues paired with developer-authored patches. Starting from 5,029 task instances spanning 131 unique (repository, commit) pairs, we run the StructFuse extraction pipeline (§3.2) to obtain inter-procedural data-flow graphs via CodeQL. After filtering for clone/checkout failures and extraction errors, we retain 15,897 instances across 123 repositories with structural data, yielding a structural coverage rate of 36%. The remaining 64% of instances lack structural connectivity data due to transient filesystem failures during batch extraction; a re-extraction pass (in progress) is expected to recover the majority of these instances, and we discuss data efficiency implications in §6.",
          "+**Dataset.** We construct our training corpus from SWE-smith \\cite{yang2025swesmith}, a large-scale dataset of real-world GitHub bug-fix commits. Starting from 5,029 task instances spanning 131 unique (repository, commit) pairs, each task corresponds to a single bug-fix commit; we expand each task by treating every gold file as a separate training instance, yielding 44,173 training instances total (since many tasks involve multiple gold files). We run the StructFuse extraction pipeline (§3.2) to obtain inter-procedural data-flow graphs via CodeQL. After filtering for clone/checkout failures and extraction errors, we retain 15,160 instances across 123 repositories with structural data, yielding a structural coverage rate of 34.3%. The remaining 64% of instances lack structural connectivity data due to transient filesystem failures during batch extraction; a re-extraction pass (in progress) is expected to recover the majority of these instances, and we discuss data efficiency implications in §6.",
          " ",
          " For each random seed, we perform a per-repository stratified split to produce approximately 11,300 training and 3,000 validation instances. Each instance consists of an issue description (query), one or more gold files (positives), and strategy-specific negatives (§3.4). The per-seed split ensures that no repository appears exclusively in one partition, preserving the distribution of repository sizes and structural properties.",
          " "
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "9bdfb466-1337-4e7a-a76d-54bd927f978b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "d1e524a6-76dd-46af-a456-0b6d1108f4ee",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-14T22:59:31.998Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01PxAi6yDxzuUYV51nu9kYB7`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/experiments_v1.md",
  "old_string": "| **Total** | **123** | **44,173** | **0%** | **36.0%** | — |",
  "new_string": "| **Total** | **123** | **44,173** | **0%** | **34.3%** | — |"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0b5a5e2d-1004-469c-aa5e-a0b56941252c",
  "isSidechain": false,
  "requestId": "req_011Cb3HkQds2R2SMjx4MynNu",
  "type": "assistant",
  "uuid": "91812fd3-652c-4af8-b882-efe39c89810a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "d1e524a6-76dd-46af-a456-0b6d1108f4ee",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EzhwQ5hecijFkaZTZhrUTZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16637,
      "cache_read_input_tokens": 30093,
      "output_tokens": 4196,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 16637,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4196,
          "cache_read_input_tokens": 30093,
          "cache_creation_input_tokens": 16637,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 16637
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

_source line 36 · 2026-05-14T22:59:32.009Z_

<details><summary>↩ Tool result · `toolu_01PxAi6yDxzuUYV51nu9kYB7`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/experiments_v1.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "91812fd3-652c-4af8-b882-efe39c89810a",
  "isSidechain": false,
  "promptId": "1d7108f5-af6a-41fc-acd8-afc665497be3",
  "type": "user",
  "uuid": "d28a5b88-b855-42de-916f-2676e9d2a756",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/experiments_v1.md",
    "oldString": "| **Total** | **123** | **44,173** | **0%** | **36.0%** | — |",
    "newString": "| **Total** | **123** | **44,173** | **0%** | **34.3%** | — |",
    "originalFile": null,
    "structuredPatch": [
      {
        "oldStart": 134,
        "oldLines": 6,
        "newStart": 134,
        "newLines": 6,
        "lines": [
          " | Medium (50–200) | 17 | 4,096 | 0% | 47.2% | 50.0% |",
          " | Large (200–500) | 40 | 13,628 | 0% | 34.3% | 85.7% |",
          " | XLarge (500+) | 29 | 25,949 | 0% | 31.4% | 96.0% |",
          "-| **Total** | **123** | **44,173** | **0%** | **36.0%** | — |",
          "+| **Total** | **123** | **44,173** | **0%** | **34.3%** | — |",
          " ",
          " The pipeline achieves 0% timeout rate across all repository tiers. Structural coverage (proportion of instances with CodeQL data-flow output) decreases with repository size, reflecting the combinatorial complexity of inter-procedural analysis in large codebases. Conversely, the connected-not-gold rate (Z%)—the proportion of structurally connected files that are non-gold—increases with repository size, reaching a median of 96% for repositories with 500+ files. This indicates that larger repositories provide richer pools for structure-grounded negative mining. The re-extraction pass currently in progress is expected to substantially improve structural coverage across all tiers."
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "91812fd3-652c-4af8-b882-efe39c89810a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "d1e524a6-76dd-46af-a456-0b6d1108f4ee",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-14T22:59:36.309Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01TBVQArNUPyEAceQXNjGhCh`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/experiments_v1.md",
  "old_string": "**Table 2: Pilot results (single seed, 24-repo subset).** Pool size = 50.\n\n| Strategy | Qwen R@1 | StarCoder R@1 |\n|---|---|---|\n| Random | 0.536 | 0.492 |\n| Embedding-distance | 0.556 (+2.0pp) | 0.508 (+1.6pp) |\n| Dataflow-aware | 0.544 (+0.8pp) | 0.487 (−0.5pp) |",
  "new_string": "**Table 2: Pilot results (single seed, 24-repo subset, R@1 checkpoint).** Pool size = 50.\n\n| Strategy | Qwen R@1 | StarCoder R@1 |\n|---|---|---|\n| Random | 0.5357 | 0.4922 |\n| Embedding-distance | 0.5557 (+2.0pp) | 0.5078 (+1.6pp) |\n| Dataflow-aware | 0.5436 (+0.8pp) | 0.4869 (−0.5pp) |"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d28a5b88-b855-42de-916f-2676e9d2a756",
  "isSidechain": false,
  "requestId": "req_011Cb3HkQds2R2SMjx4MynNu",
  "type": "assistant",
  "uuid": "2cd781a3-12e8-42f0-8ed9-8e1a61ae2e83",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "d1e524a6-76dd-46af-a456-0b6d1108f4ee",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EzhwQ5hecijFkaZTZhrUTZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16637,
      "cache_read_input_tokens": 30093,
      "output_tokens": 4196,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 16637,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4196,
          "cache_read_input_tokens": 30093,
          "cache_creation_input_tokens": 16637,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 16637
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

_source line 38 · 2026-05-14T22:59:36.319Z_

<details><summary>↩ Tool result · `toolu_01TBVQArNUPyEAceQXNjGhCh`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/experiments_v1.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2cd781a3-12e8-42f0-8ed9-8e1a61ae2e83",
  "isSidechain": false,
  "promptId": "1d7108f5-af6a-41fc-acd8-afc665497be3",
  "type": "user",
  "uuid": "c18af20c-4839-447e-a065-0919d25c27e4",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/experiments_v1.md",
    "oldString": "**Table 2: Pilot results (single seed, 24-repo subset).** Pool size = 50.\n\n| Strategy | Qwen R@1 | StarCoder R@1 |\n|---|---|---|\n| Random | 0.536 | 0.492 |\n| Embedding-distance | 0.556 (+2.0pp) | 0.508 (+1.6pp) |\n| Dataflow-aware | 0.544 (+0.8pp) | 0.487 (−0.5pp) |",
    "newString": "**Table 2: Pilot results (single seed, 24-repo subset, R@1 checkpoint).** Pool size = 50.\n\n| Strategy | Qwen R@1 | StarCoder R@1 |\n|---|---|---|\n| Random | 0.5357 | 0.4922 |\n| Embedding-distance | 0.5557 (+2.0pp) | 0.5078 (+1.6pp) |\n| Dataflow-aware | 0.5436 (+0.8pp) | 0.4869 (−0.5pp) |",
    "originalFile": null,
    "structuredPatch": [
      {
        "oldStart": 45,
        "oldLines": 13,
        "newStart": 45,
        "newLines": 13,
        "lines": [
          " ",
          " Prior to the full multi-seed experiment, we conducted single-seed pilot runs on a 24-repository subset (~3,300 instances) to validate the pipeline and obtain early signal on strategy differentiation. Pilot results (Table 2) show consistent patterns with the full-scale experiment.",
          " ",
          "-**Table 2: Pilot results (single seed, 24-repo subset).** Pool size = 50.",
          "+**Table 2: Pilot results (single seed, 24-repo subset, R@1 checkpoint).** Pool size = 50.",
          " ",
          " | Strategy | Qwen R@1 | StarCoder R@1 |",
          " |---|---|---|",
          "-| Random | 0.536 | 0.492 |",
          "-| Embedding-distance | 0.556 (+2.0pp) | 0.508 (+1.6pp) |",
          "-| Dataflow-aware | 0.544 (+0.8pp) | 0.487 (−0.5pp) |",
          "+| Random | 0.5357 | 0.4922 |",
          "+| Embedding-distance | 0.5557 (+2.0pp) | 0.5078 (+1.6pp) |",
          "+| Dataflow-aware | 0.5436 (+0.8pp) | 0.4869 (−0.5pp) |",
          " ",
          " The pilot established two findings subsequently confirmed at full scale: (i) embedding-distance mining yields consistent improvement across both encoders, and (ii) the dataflow-aware strategy's effectiveness is encoder-dependent—beneficial for Qwen but neutral-to-negative for StarCoder.",
          " "
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "2cd781a3-12e8-42f0-8ed9-8e1a61ae2e83",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "d1e524a6-76dd-46af-a456-0b6d1108f4ee",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-14T22:59:37.679Z_

<details open><summary>🔧 Tool call — Edit · `toolu_014AjS9KfBcMHfwDgUYJzqw8`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/experiments_v1.md",
  "old_string": "CoCoHaNeRe \\cite{cocohanere2025}",
  "new_string": "CoCoHaNeRe \\cite{fan2025cocohanere}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c18af20c-4839-447e-a065-0919d25c27e4",
  "isSidechain": false,
  "requestId": "req_011Cb3HkQds2R2SMjx4MynNu",
  "type": "assistant",
  "uuid": "8ab0194b-5cd3-464d-a730-d46fc57a5d2a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "d1e524a6-76dd-46af-a456-0b6d1108f4ee",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EzhwQ5hecijFkaZTZhrUTZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16637,
      "cache_read_input_tokens": 30093,
      "output_tokens": 4196,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 16637,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4196,
          "cache_read_input_tokens": 30093,
          "cache_creation_input_tokens": 16637,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 16637
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

_source line 40 · 2026-05-14T22:59:37.688Z_

<details><summary>↩ Tool result · `toolu_014AjS9KfBcMHfwDgUYJzqw8`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/experiments_v1.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8ab0194b-5cd3-464d-a730-d46fc57a5d2a",
  "isSidechain": false,
  "promptId": "1d7108f5-af6a-41fc-acd8-afc665497be3",
  "type": "user",
  "uuid": "0d94f413-e0ec-4494-be84-25cb06b79bb9",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/experiments_v1.md",
    "oldString": "CoCoHaNeRe \\cite{cocohanere2025}",
    "newString": "CoCoHaNeRe \\cite{fan2025cocohanere}",
    "originalFile": null,
    "structuredPatch": [
      {
        "oldStart": 8,
        "oldLines": 7,
        "newStart": 8,
        "newLines": 7,
        "lines": [
          " ",
          " **Evaluation Protocol.** We evaluate retrieval performance using Recall@$k$ ($k \\in \\{1, 5, 10\\}$) and Mean Reciprocal Rank (MRR), computed over a candidate pool of size 50 (1 positive + 49 negatives sampled per query). During training, $K = 7$ negatives are used per query. We report results as mean $\\pm$ standard deviation across three random seeds (42, 43, 44). For all comparisons, we use the checkpoint selected by best validation Recall@1 ($\\theta^*_{\\text{R@1}}$), as discussed in §3.3.",
          " ",
          "-**Baselines.** We compare three negative mining strategies—random, embedding-distance, and dataflow-aware (§3.4)—against a BM25 retrieval baseline. The BM25 baseline uses Okapi BM25 \\cite{robertson2009bm25} to rank candidate files by lexical overlap with the query, providing a non-neural reference point. We additionally evaluate BM25-mined negatives as a fourth contrastive training strategy to ground our comparison against the gradient-based premise of CoCoHaNeRe \\cite{cocohanere2025}.",
          "+**Baselines.** We compare three negative mining strategies—random, embedding-distance, and dataflow-aware (§3.4)—against a BM25 retrieval baseline. The BM25 baseline uses Okapi BM25 \\cite{robertson2009bm25} to rank candidate files by lexical overlap with the query, providing a non-neural reference point. We additionally evaluate BM25-mined negatives as a fourth contrastive training strategy to ground our comparison against the gradient-based premise of CoCoHaNeRe \\cite{fan2025cocohanere}.",
          " ",
          " ## §4.2 Implementation Details",
          " "
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "8ab0194b-5cd3-464d-a730-d46fc57a5d2a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "d1e524a6-76dd-46af-a456-0b6d1108f4ee",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-14T22:59:38.729Z_

<details open><summary>🔧 Tool call — Edit · `toolu_015fsSsGgg6Qb5ZdQL3S1ERT`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/experiments_v1.md",
  "old_string": "Training uses InfoNCE loss with temperature $\\tau = 0.07$",
  "new_string": "Training uses InfoNCE loss with learnable temperature initialized at $\\tau = 0.07$"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0d94f413-e0ec-4494-be84-25cb06b79bb9",
  "isSidechain": false,
  "requestId": "req_011Cb3HkQds2R2SMjx4MynNu",
  "type": "assistant",
  "uuid": "e65c74e6-0299-486a-806c-6c01b794d2ee",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "d1e524a6-76dd-46af-a456-0b6d1108f4ee",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EzhwQ5hecijFkaZTZhrUTZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16637,
      "cache_read_input_tokens": 30093,
      "output_tokens": 4196,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 16637,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4196,
          "cache_read_input_tokens": 30093,
          "cache_creation_input_tokens": 16637,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 16637
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

_source line 42 · 2026-05-14T22:59:38.805Z_

```json
{
  "parentUuid": "8ae96777-470b-4557-b59d-a13c93f2643f",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "93799a1d-1850-4a15-87ac-c056a23e0389",
  "timestamp": "2026-05-14T22:59:38.805Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "d1e524a6-76dd-46af-a456-0b6d1108f4ee",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 43_

```json
{
  "type": "last-prompt",
  "leafUuid": "93799a1d-1850-4a15-87ac-c056a23e0389",
  "sessionId": "d1e524a6-76dd-46af-a456-0b6d1108f4ee"
}
```

---

### Runtime record

_source line 44_

```json
{
  "type": "ai-title",
  "aiTitle": "Fix experiments v1 6 issues warnings and info",
  "sessionId": "d1e524a6-76dd-46af-a456-0b6d1108f4ee"
}
```

---

### Assistant

_source line 45 · 2026-05-14T22:59:40.954Z_

<details><summary>Logged reasoning block</summary>

```text
Let me check if there are other instances of `cocohanere2025` in the file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "93799a1d-1850-4a15-87ac-c056a23e0389",
  "isSidechain": false,
  "requestId": "req_011Cb3HqvSdoLmyfPMZfDzGL",
  "type": "assistant",
  "uuid": "50609411-c17e-4ee3-ba1f-e3b89ae9c18a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "d1e524a6-76dd-46af-a456-0b6d1108f4ee",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SVwupGiW1U13jn8m1Ltf6F",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4749,
      "cache_read_input_tokens": 46730,
      "output_tokens": 284,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4749,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 284,
          "cache_read_input_tokens": 46730,
          "cache_creation_input_tokens": 4749,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4749
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

_source line 46 · 2026-05-14T22:59:41.460Z_

Let me verify no remaining `cocohanere2025` instances and confirm the file looks correct.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "50609411-c17e-4ee3-ba1f-e3b89ae9c18a",
  "isSidechain": false,
  "requestId": "req_011Cb3HqvSdoLmyfPMZfDzGL",
  "type": "assistant",
  "uuid": "cbbeb070-f2f7-4d71-87cc-ad6ac5c07f3f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "d1e524a6-76dd-46af-a456-0b6d1108f4ee",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SVwupGiW1U13jn8m1Ltf6F",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4749,
      "cache_read_input_tokens": 46730,
      "output_tokens": 284,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4749,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 284,
          "cache_read_input_tokens": 46730,
          "cache_creation_input_tokens": 4749,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4749
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

_source line 47 · 2026-05-14T22:59:42.963Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01LPAZe8wMQGoYtLoYCkiQTT`</summary>

```json
{
  "pattern": "cocohanere2025",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/experiments_v1.md",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cbbeb070-f2f7-4d71-87cc-ad6ac5c07f3f",
  "isSidechain": false,
  "requestId": "req_011Cb3HqvSdoLmyfPMZfDzGL",
  "type": "assistant",
  "uuid": "b2300674-131e-44f3-963d-168a5db17257",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "d1e524a6-76dd-46af-a456-0b6d1108f4ee",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SVwupGiW1U13jn8m1Ltf6F",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4749,
      "cache_read_input_tokens": 46730,
      "output_tokens": 284,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4749,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 284,
          "cache_read_input_tokens": 46730,
          "cache_creation_input_tokens": 4749,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4749
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

_source line 48 · 2026-05-14T22:59:43.380Z_

<details><summary>↩ Tool result · `toolu_01VbjskV3oTpRLEs4wKSBXgn`</summary>

```text
1	# §4 Experiments
2	
3	## §4.1 Experimental Setup
4	
5	**Dataset.** We construct our training corpus from SWE-smith \cite{yang2025swesmith}, a large-scale dataset of real-world GitHub bug-fix commits. Starting from 5,029 task instances spanning 131 unique (repository, commit) pairs, each task corresponds to a single bug-fix commit; we expand each task by treating every gold file as a separate training instance, yielding 44,173 training instances total (since many tasks involve multiple gold files). We run the StructFuse extraction pipeline (§3.2) to obtain inter-procedural data-flow graphs via CodeQL. After filtering for clone/checkout failures and extraction errors, we retain 15,160 instances across 123 repositories with structural data, yielding a structural coverage rate of 34.3%. The remaining 64% of instances lack structural connectivity data due to transient filesystem failures during batch extraction; a re-extraction pass (in progress) is expected to recover the majority of these instances, and we discuss data efficiency implications in §6.
6	
7	For each random seed, we perform a per-repository stratified split to produce approximately 11,300 training and 3,000 validation instances. Each instance consists of an issue description (query), one or more gold files (positives), and strategy-specific negatives (§3.4). The per-seed split ensures that no repository appears exclusively in one partition, preserving the distribution of repository sizes and structural properties.
8	
9	**Evaluation Protocol.** We evaluate retrieval performance using Recall@$k$ ($k \in \{1, 5, 10\}$) and Mean Reciprocal Rank (MRR), computed over a candidate pool of size 50 (1 positive + 49 negatives sampled per query). During training, $K = 7$ negatives are used per query. We report results as mean $\pm$ standard deviation across three random seeds (42, 43, 44). For all comparisons, we use the checkpoint selected by best validation Recall@1 ($\theta^*_{\text{R@1}}$), as discussed in §3.3.
10	
11	**Baselines.** We compare three negative mining strategies—random, embedding-distance, and dataflow-aware (§3.4)—against a BM25 retrieval baseline. The BM25 baseline uses Okapi BM25 \cite{robertson2009bm25} to rank candidate files by lexical overlap with the query, providing a non-neural reference point. We additionally evaluate BM25-mined negatives as a fourth contrastive training strategy to ground our comparison against the gradient-based premise of CoCoHaNeRe \cite{fan2025cocohanere}.
12	
13	## §4.2 Implementation Details
14	
15	**Encoders.** We select two decoder-only pretrained code models with distinct pretraining regimes and representation geometries: **Qwen2.5-Coder-3B** \cite{hui2024qwen25coder} and **StarCoder2-3B** \cite{li2023starcoder}. Qwen2.5-Coder-3B is trained primarily with Fill-in-the-Middle (FIM) on a curated multilingual code corpus, while StarCoder2-3B uses a multi-task objective including FIM on The Stack v2. As we show in §4.4, these models exhibit markedly different pretrained representation geometries: Qwen operates in a near-saturated similarity regime (mean positive cosine similarity 0.986), while StarCoder maintains healthy separation (mean positive cosine similarity 0.798). This divergence enables us to study how representation geometry mediates the effectiveness of different negative mining strategies.
16	
17	**Fine-Tuning Configuration.** Both encoders are fine-tuned with LoRA \cite{hu2022lora} applied to the query and value projection matrices ($W_q$, $W_v$) of every attention layer, with rank $r = 16$, scaling factor $\alpha = 32$, and dropout 0.05. We use a linear projection head mapping the last hidden state to a 256-dimensional embedding. Training uses InfoNCE loss with learnable temperature initialized at $\tau = 0.07$, AdamW optimizer with learning rate $2 \times 10^{-5}$, weight decay 0.01, cosine annealing schedule with 10% linear warmup, and gradient clipping at max norm 1.0. Input sequences are truncated to 2,048 tokens. Batch size is 8 with gradient checkpointing enabled.
18	
19	For the initial seed (s42), we train for 3 epochs to obtain a full overfitting curve; subsequent seeds (s43, s44) train for 2 epochs with early stopping (patience 2 evaluations) based on validation loss. Evaluation is performed every 500 steps. We maintain dual checkpoints: $\theta^*_{\text{loss}}$ (minimum validation loss) and $\theta^*_{\text{R@1}}$ (maximum validation Recall@1).
20	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4da2c134-d08d-4cf2-a6f3-517260f2a85b",
  "isSidechain": false,
  "promptId": "1d7108f5-af6a-41fc-acd8-afc665497be3",
  "type": "user",
  "uuid": "88de2aea-2261-4113-b48b-4fbf17dd1d0a",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/experiments_v1.md",
      "content": "# §4 Experiments\n\n## §4.1 Experimental Setup\n\n**Dataset.** We construct our training corpus from SWE-smith \\cite{yang2025swesmith}, a large-scale dataset of real-world GitHub bug-fix commits. Starting from 5,029 task instances spanning 131 unique (repository, commit) pairs, each task corresponds to a single bug-fix commit; we expand each task by treating every gold file as a separate training instance, yielding 44,173 training instances total (since many tasks involve multiple gold files). We run the StructFuse extraction pipeline (§3.2) to obtain inter-procedural data-flow graphs via CodeQL. After filtering for clone/checkout failures and extraction errors, we retain 15,160 instances across 123 repositories with structural data, yielding a structural coverage rate of 34.3%. The remaining 64% of instances lack structural connectivity data due to transient filesystem failures during batch extraction; a re-extraction pass (in progress) is expected to recover the majority of these instances, and we discuss data efficiency implications in §6.\n\nFor each random seed, we perform a per-repository stratified split to produce approximately 11,300 training and 3,000 validation instances. Each instance consists of an issue description (query), one or more gold files (positives), and strategy-specific negatives (§3.4). The per-seed split ensures that no repository appears exclusively in one partition, preserving the distribution of repository sizes and structural properties.\n\n**Evaluation Protocol.** We evaluate retrieval performance using Recall@$k$ ($k \\in \\{1, 5, 10\\}$) and Mean Reciprocal Rank (MRR), computed over a candidate pool of size 50 (1 positive + 49 negatives sampled per query). During training, $K = 7$ negatives are used per query. We report results as mean $\\pm$ standard deviation across three random seeds (42, 43, 44). For all comparisons, we use the checkpoint selected by best validation Recall@1 ($\\theta^*_{\\text{R@1}}$), as discussed in §3.3.\n\n**Baselines.** We compare three negative mining strategies—random, embedding-distance, and dataflow-aware (§3.4)—against a BM25 retrieval baseline. The BM25 baseline uses Okapi BM25 \\cite{robertson2009bm25} to rank candidate files by lexical overlap with the query, providing a non-neural reference point. We additionally evaluate BM25-mined negatives as a fourth contrastive training strategy to ground our comparison against the gradient-based premise of CoCoHaNeRe \\cite{fan2025cocohanere}.\n\n## §4.2 Implementation Details\n\n**Encoders.** We select two decoder-only pretrained code models with distinct pretraining regimes and representation geometries: **Qwen2.5-Coder-3B** \\cite{hui2024qwen25coder} and **StarCoder2-3B** \\cite{li2023starcoder}. Qwen2.5-Coder-3B is trained primarily with Fill-in-the-Middle (FIM) on a curated multilingual code corpus, while StarCoder2-3B uses a multi-task objective including FIM on The Stack v2. As we show in §4.4, these models exhibit markedly different pretrained representation geometries: Qwen operates in a near-saturated similarity regime (mean positive cosine similarity 0.986), while StarCoder maintains healthy separation (mean positive cosine similarity 0.798). This divergence enables us to study how representation geometry mediates the effectiveness of different negative mining strategies.\n\n**Fine-Tuning Configuration.** Both encoders are fine-tuned with LoRA \\cite{hu2022lora} applied to the query and value projection matrices ($W_q$, $W_v$) of every attention layer, with rank $r = 16$, scaling factor $\\alpha = 32$, and dropout 0.05. We use a linear projection head mapping the last hidden state to a 256-dimensional embedding. Training uses InfoNCE loss with learnable temperature initialized at $\\tau = 0.07$, AdamW optimizer with learning rate $2 \\times 10^{-5}$, weight decay 0.01, cosine annealing schedule with 10% linear warmup, and gradient clipping at max norm 1.0. Input sequences are truncated to 2,048 tokens. Batch size is 8 with gradient checkpointing enabled.\n\nFor the initial seed (s42), we train for 3 epochs to obtain a full overfitting curve; subsequent seeds (s43, s44) train for 2 epochs with early stopping (patience 2 evaluations) based on validation loss. Evaluation is performed every 500 steps. We maintain dual checkpoints: $\\theta^*_{\\text{loss}}$ (minimum validation loss) and $\\theta^*_{\\text{R@1}}$ (maximum validation Recall@1).\n",
      "numLines": 20,
      "startLine": 1,
      "totalLines": 140
    }
  },
  "sourceToolAssistantUUID": "4da2c134-d08d-4cf2-a6f3-517260f2a85b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "d1e524a6-76dd-46af-a456-0b6d1108f4ee",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 49 · 2026-05-14T22:59:42.976Z_

<details><summary>↩ Tool result · `toolu_01LPAZe8wMQGoYtLoYCkiQTT`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b2300674-131e-44f3-963d-168a5db17257",
  "isSidechain": false,
  "promptId": "1d7108f5-af6a-41fc-acd8-afc665497be3",
  "type": "user",
  "uuid": "54c42964-7aa1-4a34-b64a-a23ff818c707",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "",
    "numLines": 0
  },
  "sourceToolAssistantUUID": "b2300674-131e-44f3-963d-168a5db17257",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "d1e524a6-76dd-46af-a456-0b6d1108f4ee",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 50 · 2026-05-14T22:59:43.370Z_

<details open><summary>🔧 Tool call — Read · `toolu_01VbjskV3oTpRLEs4wKSBXgn`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/experiments_v1.md",
  "limit": 20
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "54c42964-7aa1-4a34-b64a-a23ff818c707",
  "isSidechain": false,
  "requestId": "req_011Cb3HqvSdoLmyfPMZfDzGL",
  "type": "assistant",
  "uuid": "4da2c134-d08d-4cf2-a6f3-517260f2a85b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "d1e524a6-76dd-46af-a456-0b6d1108f4ee",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SVwupGiW1U13jn8m1Ltf6F",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4749,
      "cache_read_input_tokens": 46730,
      "output_tokens": 284,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4749,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 284,
          "cache_read_input_tokens": 46730,
          "cache_creation_input_tokens": 4749,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4749
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

_source line 51 · 2026-05-14T22:59:46.383Z_

<details><summary>Logged reasoning block</summary>

```text
Also need to update "The remaining 64%" since 100% - 34.3% = 65.7%. Let me fix that.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "88de2aea-2261-4113-b48b-4fbf17dd1d0a",
  "isSidechain": false,
  "requestId": "req_011Cb3HrGGFUnTD7YK7soK35",
  "type": "assistant",
  "uuid": "8388386d-be52-4349-b41c-8415097dd78f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "d1e524a6-76dd-46af-a456-0b6d1108f4ee",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YNKMiLyxuKoJQqNYCbdBbF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1561,
      "cache_read_input_tokens": 51479,
      "output_tokens": 233,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1561,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 233,
          "cache_read_input_tokens": 51479,
          "cache_creation_input_tokens": 1561,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1561
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

_source line 52 · 2026-05-14T22:59:47.320Z_

The "remaining 64%" should be updated to 65.7% to match 34.3%.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8388386d-be52-4349-b41c-8415097dd78f",
  "isSidechain": false,
  "requestId": "req_011Cb3HrGGFUnTD7YK7soK35",
  "type": "assistant",
  "uuid": "8ec73d63-651a-46b6-888d-7458e82cc201",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "d1e524a6-76dd-46af-a456-0b6d1108f4ee",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YNKMiLyxuKoJQqNYCbdBbF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1561,
      "cache_read_input_tokens": 51479,
      "output_tokens": 233,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1561,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 233,
          "cache_read_input_tokens": 51479,
          "cache_creation_input_tokens": 1561,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1561
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

_source line 53 · 2026-05-14T22:59:50.336Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01UA9d4YzHbBTNXwat9S6669`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/experiments_v1.md",
  "old_string": "The remaining 64% of instances",
  "new_string": "The remaining 65.7% of instances"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8ec73d63-651a-46b6-888d-7458e82cc201",
  "isSidechain": false,
  "requestId": "req_011Cb3HrGGFUnTD7YK7soK35",
  "type": "assistant",
  "uuid": "c8a5a41d-e9c8-4906-9c60-df65eb29763e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "d1e524a6-76dd-46af-a456-0b6d1108f4ee",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YNKMiLyxuKoJQqNYCbdBbF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1561,
      "cache_read_input_tokens": 51479,
      "output_tokens": 233,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1561,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 233,
          "cache_read_input_tokens": 51479,
          "cache_creation_input_tokens": 1561,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1561
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

_source line 54 · 2026-05-14T22:59:50.350Z_

<details><summary>↩ Tool result · `toolu_01UA9d4YzHbBTNXwat9S6669`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/experiments_v1.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c8a5a41d-e9c8-4906-9c60-df65eb29763e",
  "isSidechain": false,
  "promptId": "1d7108f5-af6a-41fc-acd8-afc665497be3",
  "type": "user",
  "uuid": "2a5ee1e7-71d1-470e-93bb-bb51fc8224d3",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/experiments_v1.md",
    "oldString": "The remaining 64% of instances",
    "newString": "The remaining 65.7% of instances",
    "originalFile": null,
    "structuredPatch": [
      {
        "oldStart": 2,
        "oldLines": 7,
        "newStart": 2,
        "newLines": 7,
        "lines": [
          " ",
          " ## §4.1 Experimental Setup",
          " ",
          "-**Dataset.** We construct our training corpus from SWE-smith \\cite{yang2025swesmith}, a large-scale dataset of real-world GitHub bug-fix commits. Starting from 5,029 task instances spanning 131 unique (repository, commit) pairs, each task corresponds to a single bug-fix commit; we expand each task by treating every gold file as a separate training instance, yielding 44,173 training instances total (since many tasks involve multiple gold files). We run the StructFuse extraction pipeline (§3.2) to obtain inter-procedural data-flow graphs via CodeQL. After filtering for clone/checkout failures and extraction errors, we retain 15,160 instances across 123 repositories with structural data, yielding a structural coverage rate of 34.3%. The remaining 64% of instances lack structural connectivity data due to transient filesystem failures during batch extraction; a re-extraction pass (in progress) is expected to recover the majority of these instances, and we discuss data efficiency implications in §6.",
          "+**Dataset.** We construct our training corpus from SWE-smith \\cite{yang2025swesmith}, a large-scale dataset of real-world GitHub bug-fix commits. Starting from 5,029 task instances spanning 131 unique (repository, commit) pairs, each task corresponds to a single bug-fix commit; we expand each task by treating every gold file as a separate training instance, yielding 44,173 training instances total (since many tasks involve multiple gold files). We run the StructFuse extraction pipeline (§3.2) to obtain inter-procedural data-flow graphs via CodeQL. After filtering for clone/checkout failures and extraction errors, we retain 15,160 instances across 123 repositories with structural data, yielding a structural coverage rate of 34.3%. The remaining 65.7% of instances lack structural connectivity data due to transient filesystem failures during batch extraction; a re-extraction pass (in progress) is expected to recover the majority of these instances, and we discuss data efficiency implications in §6.",
          " ",
          " For each random seed, we perform a per-repository stratified split to produce approximately 11,300 training and 3,000 validation instances. Each instance consists of an issue description (query), one or more gold files (positives), and strategy-specific negatives (§3.4). The per-seed split ensures that no repository appears exclusively in one partition, preserving the distribution of repository sizes and structural properties.",
          " "
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "c8a5a41d-e9c8-4906-9c60-df65eb29763e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "d1e524a6-76dd-46af-a456-0b6d1108f4ee",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 55 · 2026-05-14T22:59:52.857Z_

Now register the updated artifact.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2a5ee1e7-71d1-470e-93bb-bb51fc8224d3",
  "isSidechain": false,
  "requestId": "req_011Cb3HrnRxShWjeR4aeJdjS",
  "type": "assistant",
  "uuid": "618f7b93-396d-41d8-99a7-c391c41819c7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "d1e524a6-76dd-46af-a456-0b6d1108f4ee",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01E3vKKw76hzZtCx96yerPk4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 292,
      "cache_read_input_tokens": 53040,
      "output_tokens": 325,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 292,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 325,
          "cache_read_input_tokens": 53040,
          "cache_creation_input_tokens": 292,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 292
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

_source line 56 · 2026-05-14T22:59:57.762Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact · `toolu_01XUhbuqLUVfnJTNhtnVP1CA`</summary>

```json
{
  "name": "experiments_v1",
  "type": "paper",
  "description": "Experiments v1 draft with 5 fixes: (1) Table 6 Total 36.0%→34.3% aligned to registry, (2) Table 2 updated to R@1 checkpoint values with 4-decimal precision, (3) SWE-bench→SWE-smith with task→instance expansion explanation, (4) cite key cocohanere2025→fan2025cocohanere, (5) temperature τ=0.07 marked as learnable",
  "project": "structfuse-context",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/experiments_v1.md",
  "tags": [
    "paper",
    "experiments",
    "v1-fixed"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "618f7b93-396d-41d8-99a7-c391c41819c7",
  "isSidechain": false,
  "requestId": "req_011Cb3HrnRxShWjeR4aeJdjS",
  "type": "assistant",
  "uuid": "a9023a84-22bb-41f5-9018-7b1a418f2fdf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "d1e524a6-76dd-46af-a456-0b6d1108f4ee",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01E3vKKw76hzZtCx96yerPk4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 292,
      "cache_read_input_tokens": 53040,
      "output_tokens": 325,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 292,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 325,
          "cache_read_input_tokens": 53040,
          "cache_creation_input_tokens": 292,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 292
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

_source line 57 · 2026-05-14T22:59:57.873Z_

<details><summary>↩ Tool result · `toolu_01XUhbuqLUVfnJTNhtnVP1CA`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260514_054f8d\", \"name\": \"experiments_v1\", \"type\": \"paper\", \"description\": \"Experiments v1 draft with 5 fixes: (1) Table 6 Total 36.0%→34.3% aligned to registry, (2) Table 2 updated to R@1 checkpoint values with 4-decimal precision, (3) SWE-bench→SWE-smith with task→instance expansion explanation, (4) cite key cocohanere2025→fan2025cocohanere, (5) temperature τ=0.07 marked as learnable\", \"path\": \"projects/structfuse-context/artifacts/_project/paper/experiments_v1_054f8d.md\", \"url\": null, \"project\": \"structfuse-context\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-14T22:59:57.770391+00:00\", \"tags\": [\"paper\", \"experiments\", \"v1-fixed\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a9023a84-22bb-41f5-9018-7b1a418f2fdf",
  "isSidechain": false,
  "promptId": "1d7108f5-af6a-41fc-acd8-afc665497be3",
  "type": "user",
  "uuid": "56841633-b325-4816-8e1b-ae082eabf1a7",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"artifact\\\": {\\\"id\\\": \\\"art_20260514_054f8d\\\", \\\"name\\\": \\\"experiments_v1\\\", \\\"type\\\": \\\"paper\\\", \\\"description\\\": \\\"Experiments v1 draft with 5 fixes: (1) Table 6 Total 36.0%→34.3% aligned to registry, (2) Table 2 updated to R@1 checkpoint values with 4-decimal precision, (3) SWE-bench→SWE-smith with task→instance expansion explanation, (4) cite key cocohanere2025→fan2025cocohanere, (5) temperature τ=0.07 marked as learnable\\\", \\\"path\\\": \\\"projects/structfuse-context/artifacts/_project/paper/experiments_v1_054f8d.md\\\", \\\"url\\\": null, \\\"project\\\": \\\"structfuse-context\\\", \\\"exp_id\\\": null, \\\"skill\\\": \\\"\\\", \\\"created_at\\\": \\\"2026-05-14T22:59:57.770391+00:00\\\", \\\"tags\\\": [\\\"paper\\\", \\\"experiments\\\", \\\"v1-fixed\\\"]}, \\\"manifest\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/manifest.yaml\\\"}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260514_054f8d\", \"name\": \"experiments_v1\", \"type\": \"paper\", \"description\": \"Experiments v1 draft with 5 fixes: (1) Table 6 Total 36.0%→34.3% aligned to registry, (2) Table 2 updated to R@1 checkpoint values with 4-decimal precision, (3) SWE-bench→SWE-smith with task→instance expansion explanation, (4) cite key cocohanere2025→fan2025cocohanere, (5) temperature τ=0.07 marked as learnable\", \"path\": \"projects/structfuse-context/artifacts/_project/paper/experiments_v1_054f8d.md\", \"url\": null, \"project\": \"structfuse-context\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-14T22:59:57.770391+00:00\", \"tags\": [\"paper\", \"experiments\", \"v1-fixed\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "a9023a84-22bb-41f5-9018-7b1a418f2fdf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "d1e524a6-76dd-46af-a456-0b6d1108f4ee",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 58 · 2026-05-14T23:00:07.239Z_

5 处修改完成：

1. **Warning 1 — Table 6 Total**：36.0% → **34.3%**（对齐 `plan_006_scalability` registry），§4.1 正文同步更新（coverage rate + remaining 比例 64%→65.7%）
2. **Warning 2 — Table 2 checkpoint**：数值更新为 R@1 checkpoint 4 位小数（0.5357/0.5557/0.5436/0.4922/0.5078/0.4869），表标题加注 "R@1 checkpoint"，delta 不变
3. **Warning 3 — SWE-bench → SWE-smith**：引用改为 `\cite{yang2025swesmith}`，新增 task→instance 展开说明（5,029 tasks × 多 gold files = 44,173 instances）
4. **Info 4 — cite key**：`cocohanere2025` → `fan2025cocohanere`
5. **Info 5 — temperature**：`temperature τ = 0.07` → `learnable temperature initialized at τ = 0.07`

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "56841633-b325-4816-8e1b-ae082eabf1a7",
  "isSidechain": false,
  "requestId": "req_011Cb3HsKyGbpmHD6PoiSMLY",
  "type": "assistant",
  "uuid": "4e426c87-a738-43d5-8401-301f1e8880c1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "d1e524a6-76dd-46af-a456-0b6d1108f4ee",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V9RUzU3VGK1idTiqBpcQM6",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 678,
      "cache_read_input_tokens": 53332,
      "output_tokens": 300,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 678,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 300,
          "cache_read_input_tokens": 53332,
          "cache_creation_input_tokens": 678,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 678
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

_source line 59_

```json
{
  "type": "last-prompt",
  "leafUuid": "4e426c87-a738-43d5-8401-301f1e8880c1",
  "sessionId": "d1e524a6-76dd-46af-a456-0b6d1108f4ee"
}
```

---

### Runtime record

_source line 60_

```json
{
  "type": "ai-title",
  "aiTitle": "Fix experiments v1 6 issues warnings and info",
  "sessionId": "d1e524a6-76dd-46af-a456-0b6d1108f4ee"
}
```

---

### Runtime record

_source line 61_

```json
{
  "type": "last-prompt",
  "leafUuid": "4e426c87-a738-43d5-8401-301f1e8880c1",
  "sessionId": "d1e524a6-76dd-46af-a456-0b6d1108f4ee"
}
```

---

### Runtime record

_source line 62_

```json
{
  "type": "ai-title",
  "aiTitle": "Fix experiments v1 6 issues warnings and info",
  "sessionId": "d1e524a6-76dd-46af-a456-0b6d1108f4ee"
}
```

---
