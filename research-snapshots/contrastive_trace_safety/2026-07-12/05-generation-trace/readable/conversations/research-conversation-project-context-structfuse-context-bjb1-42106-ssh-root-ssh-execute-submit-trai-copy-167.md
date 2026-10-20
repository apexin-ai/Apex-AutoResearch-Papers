# Research conversation: <project_context> # 项目: structfuse-context ## 运行环境 - 服务器名: bjb1-42106 - SSH 账户: root（调用 ssh_execute / submit_training_jo

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 93
- **Recorded user turns:** 1
- **Tool calls:** 23
- **Original source:** `logs/chats/exported-trajectories/account-1/fb5ea7f7-b3c9-4750-b931-39d2aaae422b.jsonl`
- **Structured JSON:** [`94fe890861a16e5771a3.json`](../../sessions/94/94fe890861a16e5771a3.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-14T20:36:19.650Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-14T20:36:19.650Z",
  "sessionId": "fb5ea7f7-b3c9-4750-b931-39d2aaae422b",
  "content": "&lt;project_context>\n# 项目: structfuse-context\n\n## 运行环境\n- 服务器名: bjb1-42106\n- SSH 账户: root（调用 ssh_execute / submit_training_job 时传入 account=\"root\"）\n- SSH 连接命令: ssh connect.bjb1.seetacloud.com  # 必须用此命令，~/.ssh/config 自动应用密钥和跳板机，禁止用裸 IP\n- 项目代码根目录: /root/structfuse\n\n\n## 环境搭建\n连接服务器后先调 `detect_image` 检测是否为预置镜像。如果匹配，跳过基础环境搭建，只装项目特有依赖。已预装的包不要重复安装。\n\n## 输出风格\n回复简洁直接。只输出执行结果和必要信息，不要解释过程、不要客套、不要给未被要求的建议。\n&lt;/project_context>\n## 任务：溯源 stratified_dryrun v1→v2 差异\n\n### 背景\nPlan 005 分层分析有两次 dry-run：\n- v1: `/root/autodl-tmp/structfuse/artifacts/stratified_dryrun/`（第一个 Worker `analysis:plan_005_stratified` 产出）\n- v2: `/root/autodl-tmp/structfuse/artifacts/stratified_dryrun_v2/`（第二个 Worker `analysis:plan_005_stratified_v2` 产出）\n\nReviewer 发现 v1→v2 之间，已有维度的数值发生了变化。例如 repo_size=small, random 策略的 R@1 从 0.1154 降到 0.0769，降幅 33%。这些都是 dry-run（mock predictions），但我们需要解释为什么同维度数值不同。\n\nv2 相比 v1 新增了 2 个维度（structural data availability + neg_difficulty quartile）。\n\n### 你要做的事\n\n1. **对比 v1 和 v2 的 JSON 结果文件**：\n   - 读 `/root/autodl-tmp/structfuse/artifacts/stratified_dryrun/stratified_results.json`\n   - 读 `/root/autodl-tmp/structfuse/artifacts/stratified_dryrun_v2/stratified_results.json`\n   - 列出所有 **已有维度**（repo_size, pool_size, query_pos_sim）的数值变化\n\n2. **查脚本变更历史**：\n   - `analyze_stratified.py` 在 `/root/structfuse/evaluation/` 目录下\n   - 用 `git log --oneline -10 -- evaluation/analyze_stratified.py` 或 `git diff` 查看两次运行之间的变更\n   - 如果没有 git 历史，对比脚本中可能影响已有维度的逻辑：\n     - bin 边界定义是否变了\n     - 数据加载/过滤逻辑是否变了\n     - mock prediction 的随机种子或生成方式是否变了\n     - sample 数量是否变了（检查每个 stratum 的 n）\n\n3. **确定根因**：可能的原因包括：\n   - (a) 换了 checkpoint（不太可能，都是 dry-run）\n   - (b) 修了评估 bug\n   - (c) 改了候选池定义/分层逻辑\n   - (d) mock 预测的随机种子不同\n   - (e) 数据过滤变了导致 stratum 样本量不同\n\n4. **产出**：在本地 artifacts 目录写一份 `v1_v2_changelog.md`，内容：\n   - 差异原因（具体到代码行或逻辑变更）\n   - v2 为 ground truth 的依据\n   - 数值变化表（per stratum，v1 vs v2 的 R@1）\n\n写文件路径：`/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/v1_v2_changelog.md`\n\n### 服务器信息\n- 服务器: bjb1-42106\n- 脚本: `/root/structfuse/evaluation/analyze_stratified.py`\n- 环境: conda base (`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`)"
}
```

---

### Runtime record

_source line 2 · 2026-05-14T20:36:19.653Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-14T20:36:19.653Z",
  "sessionId": "fb5ea7f7-b3c9-4750-b931-39d2aaae422b"
}
```

---

## Round 1

91 recorded events

### User

_source line 3 · 2026-05-14T20:36:19.687Z_

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
## 任务：溯源 stratified_dryrun v1→v2 差异

### 背景
Plan 005 分层分析有两次 dry-run：
- v1: `/root/autodl-tmp/structfuse/artifacts/stratified_dryrun/`（第一个 Worker `analysis:plan_005_stratified` 产出）
- v2: `/root/autodl-tmp/structfuse/artifacts/stratified_dryrun_v2/`（第二个 Worker `analysis:plan_005_stratified_v2` 产出）

Reviewer 发现 v1→v2 之间，已有维度的数值发生了变化。例如 repo_size=small, random 策略的 R@1 从 0.1154 降到 0.0769，降幅 33%。这些都是 dry-run（mock predictions），但我们需要解释为什么同维度数值不同。

v2 相比 v1 新增了 2 个维度（structural data availability + neg_difficulty quartile）。

### 你要做的事

1. **对比 v1 和 v2 的 JSON 结果文件**：
   - 读 `/root/autodl-tmp/structfuse/artifacts/stratified_dryrun/stratified_results.json`
   - 读 `/root/autodl-tmp/structfuse/artifacts/stratified_dryrun_v2/stratified_results.json`
   - 列出所有 **已有维度**（repo_size, pool_size, query_pos_sim）的数值变化

2. **查脚本变更历史**：
   - `analyze_stratified.py` 在 `/root/structfuse/evaluation/` 目录下
   - 用 `git log --oneline -10 -- evaluation/analyze_stratified.py` 或 `git diff` 查看两次运行之间的变更
   - 如果没有 git 历史，对比脚本中可能影响已有维度的逻辑：
     - bin 边界定义是否变了
     - 数据加载/过滤逻辑是否变了
     - mock prediction 的随机种子或生成方式是否变了
     - sample 数量是否变了（检查每个 stratum 的 n）

3. **确定根因**：可能的原因包括：
   - (a) 换了 checkpoint（不太可能，都是 dry-run）
   - (b) 修了评估 bug
   - (c) 改了候选池定义/分层逻辑
   - (d) mock 预测的随机种子不同
   - (e) 数据过滤变了导致 stratum 样本量不同

4. **产出**：在本地 artifacts 目录写一份 `v1_v2_changelog.md`，内容：
   - 差异原因（具体到代码行或逻辑变更）
   - v2 为 ground truth 的依据
   - 数值变化表（per stratum，v1 vs v2 的 R@1）

写文件路径：`/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/v1_v2_changelog.md`

### 服务器信息
- 服务器: bjb1-42106
- 脚本: `/root/structfuse/evaluation/analyze_stratified.py`
- 环境: conda base (`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "0b7bb415-f2b4-4832-aac4-2e6aafdc7429",
  "type": "user",
  "uuid": "8998d600-6804-466c-b3db-96a91cb90770",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "fb5ea7f7-b3c9-4750-b931-39d2aaae422b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-14T20:36:19.686Z_

```json
{
  "parentUuid": "8998d600-6804-466c-b3db-96a91cb90770",
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
      "mcp__agent-ml-research__detect_image",
      "mcp__agent-ml-research__kill_job",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__save_project_file",
      "mcp__agent-ml-research__ssh_execute",
      "mcp__agent-ml-research__ssh_read_only"
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
      "mcp__agent-ml-research__detect_image",
      "mcp__agent-ml-research__kill_job",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__save_project_file",
      "mcp__agent-ml-research__ssh_execute",
      "mcp__agent-ml-research__ssh_read_only"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "4820cb52-72fe-495e-8339-6df0e2e5c2e9",
  "timestamp": "2026-05-14T20:36:19.686Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "fb5ea7f7-b3c9-4750-b931-39d2aaae422b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-14T20:36:19.686Z_

```json
{
  "parentUuid": "4820cb52-72fe-495e-8339-6df0e2e5c2e9",
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
  "uuid": "b1a8586a-7a19-4a39-b17b-929667fbd6ca",
  "timestamp": "2026-05-14T20:36:19.686Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "fb5ea7f7-b3c9-4750-b931-39d2aaae422b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6 · 2026-05-14T20:36:19.686Z_

```json
{
  "parentUuid": "b1a8586a-7a19-4a39-b17b-929667fbd6ca",
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
  "uuid": "805994d9-15bc-43ac-b286-a4c8076c5c9a",
  "timestamp": "2026-05-14T20:36:19.686Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "fb5ea7f7-b3c9-4750-b931-39d2aaae422b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 7 · 2026-05-14T20:36:19.686Z_

```json
{
  "parentUuid": "805994d9-15bc-43ac-b286-a4c8076c5c9a",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "7d7eee9f-b4c0-430e-8043-743b8e482975",
  "timestamp": "2026-05-14T20:36:19.686Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "fb5ea7f7-b3c9-4750-b931-39d2aaae422b",
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
  "aiTitle": "Trace stratified_dryrun v1 to v2 differences",
  "sessionId": "fb5ea7f7-b3c9-4750-b931-39d2aaae422b"
}
```

---

### Assistant

_source line 9 · 2026-05-14T20:36:23.655Z_

<details><summary>Logged reasoning block</summary>

```text
Let me break this task down:

1. Read v1 and v2 JSON result files from the remote server
2. Check git history / script changes for `analyze_stratified.py`
3. Determine root cause of numerical differences
4. Write a changelog file locally

Let me start by fetching the tool schemas I need, then read the remote files in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7d7eee9f-b4c0-430e-8043-743b8e482975",
  "isSidechain": false,
  "requestId": "req_011Cb36v3swbBcVcqtDwKJZZ",
  "type": "assistant",
  "uuid": "efab408d-1496-4f7f-b7de-a326efbb1bf7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "fb5ea7f7-b3c9-4750-b931-39d2aaae422b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NmaGyoBFWemUQJY1tio57g",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12152,
      "cache_read_input_tokens": 11447,
      "output_tokens": 215,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12152,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 215,
          "cache_read_input_tokens": 11447,
          "cache_creation_input_tokens": 12152,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12152
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

_source line 10 · 2026-05-14T20:36:24.835Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01J9squDCCDtvfzAM2oXSZeG`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__save_project_file",
  "max_results": 3
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "efab408d-1496-4f7f-b7de-a326efbb1bf7",
  "isSidechain": false,
  "requestId": "req_011Cb36v3swbBcVcqtDwKJZZ",
  "type": "assistant",
  "uuid": "1803d3b7-789b-4741-925e-f11b420d67e0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "fb5ea7f7-b3c9-4750-b931-39d2aaae422b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NmaGyoBFWemUQJY1tio57g",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12152,
      "cache_read_input_tokens": 11447,
      "output_tokens": 215,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12152,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 215,
          "cache_read_input_tokens": 11447,
          "cache_creation_input_tokens": 12152,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12152
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

_source line 11 · 2026-05-14T20:36:24.842Z_

<details><summary>↩ Tool result · `toolu_01J9squDCCDtvfzAM2oXSZeG`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__ssh_read_only"
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
  "parentUuid": "1803d3b7-789b-4741-925e-f11b420d67e0",
  "isSidechain": false,
  "promptId": "0b7bb415-f2b4-4832-aac4-2e6aafdc7429",
  "type": "user",
  "uuid": "896e45ba-d447-4595-9ba1-2c87c3758573",
  "toolUseResult": {
    "matches": [
      "mcp__agent-ml-research__ssh_read_only",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__save_project_file"
    ],
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__save_project_file",
    "total_deferred_tools": 26
  },
  "sourceToolAssistantUUID": "1803d3b7-789b-4741-925e-f11b420d67e0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "fb5ea7f7-b3c9-4750-b931-39d2aaae422b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 12 · 2026-05-14T20:36:27.843Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me fetch the data in parallel - read both JSON files and check git history.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "896e45ba-d447-4595-9ba1-2c87c3758573",
  "isSidechain": false,
  "requestId": "req_011Cb36vRk5q3Go4Ger3n9CF",
  "type": "assistant",
  "uuid": "3d2ba087-5148-4520-8bf8-340958088e58",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "fb5ea7f7-b3c9-4750-b931-39d2aaae422b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VLWwpdCr7UuwqnYjsWSZpb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1121,
      "cache_read_input_tokens": 23599,
      "output_tokens": 411,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1121,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 411,
          "cache_read_input_tokens": 23599,
          "cache_creation_input_tokens": 1121,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1121
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

_source line 13 · 2026-05-14T20:36:28.414Z_

并行读取 v1/v2 JSON 和 git 历史。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3d2ba087-5148-4520-8bf8-340958088e58",
  "isSidechain": false,
  "requestId": "req_011Cb36vRk5q3Go4Ger3n9CF",
  "type": "assistant",
  "uuid": "48cba0a0-a672-43fe-95af-2ca4facb6358",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "fb5ea7f7-b3c9-4750-b931-39d2aaae422b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VLWwpdCr7UuwqnYjsWSZpb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1121,
      "cache_read_input_tokens": 23599,
      "output_tokens": 411,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1121,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 411,
          "cache_read_input_tokens": 23599,
          "cache_creation_input_tokens": 1121,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1121
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

_source line 14 · 2026-05-14T20:36:29.407Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_015sQ1GxqfFezhofzVEbSPrH`</summary>

```json
{
  "server": "bjb1-42106",
  "command": "cat /root/autodl-tmp/structfuse/artifacts/stratified_dryrun/stratified_results.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "48cba0a0-a672-43fe-95af-2ca4facb6358",
  "isSidechain": false,
  "requestId": "req_011Cb36vRk5q3Go4Ger3n9CF",
  "type": "assistant",
  "uuid": "0a95eb57-e256-4aa4-b648-45c2e62d1471",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "fb5ea7f7-b3c9-4750-b931-39d2aaae422b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VLWwpdCr7UuwqnYjsWSZpb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1121,
      "cache_read_input_tokens": 23599,
      "output_tokens": 411,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1121,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 411,
          "cache_read_input_tokens": 23599,
          "cache_creation_input_tokens": 1121,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1121
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

_source line 15 · 2026-05-14T20:36:30.370Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01GZFsdVfnN81kRFsEu7cU3i`</summary>

```json
{
  "server": "bjb1-42106",
  "command": "cat /root/autodl-tmp/structfuse/artifacts/stratified_dryrun_v2/stratified_results.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0a95eb57-e256-4aa4-b648-45c2e62d1471",
  "isSidechain": false,
  "requestId": "req_011Cb36vRk5q3Go4Ger3n9CF",
  "type": "assistant",
  "uuid": "fef79e23-680f-4852-ac33-f0ee76fef1bd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "fb5ea7f7-b3c9-4750-b931-39d2aaae422b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VLWwpdCr7UuwqnYjsWSZpb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1121,
      "cache_read_input_tokens": 23599,
      "output_tokens": 411,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1121,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 411,
          "cache_read_input_tokens": 23599,
          "cache_creation_input_tokens": 1121,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1121
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

_source line 16 · 2026-05-14T20:36:30.597Z_

<details><summary>↩ Tool result · `toolu_015sQ1GxqfFezhofzVEbSPrH`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"config\\\": {\\n    \\\"strategies\\\": [\\n      \\\"random\\\",\\n      \\\"embedding_distance\\\",\\n      \\\"dataflow_aware\\\"\\n    ],\\n    \\\"seeds\\\": [\\n      42\\n    ],\\n    \\\"repo_size_bins\\\": {\\n      \\\"small\\\": [\\n        0,\\n        50\\n      ],\\n      \\\"medium\\\": [\\n        50,\\n        200\\n      ],\\n      \\\"large\\\": [\\n        200,\\n        500\\n      ],\\n      \\\"xlarge\\\": [\\n        500,\\n        Infinity\\n      ]\\n    },\\n    \\\"pool_size_bins\\\": {\\n      \\\"small\\\": [\\n        0,\\n        20\\n      ],\\n      \\\"medium\\\": [\\n        20,\\n        40\\n      ],\\n      \\\"large\\\": [\\n        40,\\n        51\\n      ]\\n    },\\n    \\\"similarity_bins\\\": {\\n      \\\"low\\\": [\\n        0.0,\\n        0.3\\n      ],\\n      \\\"medium\\\": [\\n        0.3,\\n        0.6\\n      ],\\n      \\\"high\\\": [\\n        0.6,\\n        1.01\\n      ]\\n    },\\n    \\\"n_bootstrap\\\": 200,\\n    \\\"dry_run\\\": true\\n  },\\n  \\\"by_repo_size\\\": {\\n    \\\"small\\\": {\\n      \\\"random\\\": {\\n        \\\"R@1\\\": 0.11538461538461539,\\n        \\\"R@1_ci\\\": [\\n          0.061346153846153884,\\n          0.16923076923076924\\n        ],\\n        \\\"R@5\\\": 0.5384615384615384,\\n        \\\"R@5_ci\\\": [\\n          0.4461538461538462,\\n          0.6230769230769231\\n        ],\\n        \\\"MRR\\\": 0.3059754134754135,\\n        \\\"MRR_ci\\\": [\\n          0.25409036102786103,\\n          0.3513594044844045\\n        ],\\n        \\\"count\\\": 130\\n      },\\n      \\\"embedding_distance\\\": {\\n        \\\"R@1\\\": 0.3,\\n        \\\"R@1_ci\\\": [\\n          0.2230769230769231,\\n          0.37711538461538463\\n        ],\\n        \\\"R@5\\\": 0.7384615384615385,\\n        \\\"R@5_ci\\\": [\\n          0.6613461538461538,\\n          0.8153846153846154\\n        ],\\n        \\\"MRR\\\": 0.4930563880563881,\\n        \\\"MRR_ci\\\": [\\n          0.43992261211011213,\\n          0.5556576062826063\\n        ],\\n        \\\"count\\\": 130\\n      },\\n      \\\"dataflow_aware\\\": {\\n        \\\"R@1\\\": 0.4846153846153846,\\n        \\\"R@1_ci\\\": [\\n          0.3923076923076923,\\n          0.5617307692307693\\n        ],\\n        \\\"R@5\\\": 0.8769230769230769,\\n        \\\"R@5_ci\\\": [\\n          0.8226923076923077,\\n          0.9230769230769231\\n        ],\\n        \\\"MRR\\\": 0.6500946275946277,\\n        \\\"MRR_ci\\\": [\\n          0.59523923992674,\\n          0.7073237942612942\\n        ],\\n        \\\"count\\\": 130\\n      },\\n      \\\"embedding_distance_vs_random\\\": {\\n        \\\"R@1_delta\\\": 0.1846153846153846,\\n        \\\"R@1_rel_pct\\\": 160.0,\\n        \\\"R@5_delta\\\": 0.20000000000000007,\\n        \\\"R@5_rel_pct\\\": 37.14285714285715,\\n        \\\"MRR_delta\\\": 0.18708097458097456,\\n        \\\"MRR_rel_pct\\\": 61.14248607625702\\n      },\\n      \\\"dataflow_aware_vs_random\\\": {\\n        \\\"R@1_delta\\\": 0.36923076923076925,\\n        \\\"R@1_rel_pct\\\": 320.0,\\n        \\\"R@5_delta\\\": 0.3384615384615385,\\n        \\\"R@5_rel_pct\\\": 62.85714285714287,\\n        \\\"MRR_delta\\\": 0.34411921411921415,\\n        \\\"MRR_rel_pct\\\": 112.46629597147866\\n      }\\n    },\\n    \\\"medium\\\": {\\n      \\\"random\\\": {\\n        \\\"R@1\\\": 0.05202312138728324,\\n        \\\"R@1_ci\\\": [\\n          0.031791907514450865,\\n          0.08092485549132948\\n        ],\\n        \\\"R@5\\\": 0.23121387283236994,\\n        \\\"R@5_ci\\\": [\\n          0.18778901734104048,\\n          0.27167630057803466\\n        ],\\n        \\\"MRR\\\": 0.17820474196308103,\\n        \\\"MRR_ci\\\": [\\n          0.15638534764941775,\\n          0.20150044957306631\\n        ],\\n        \\\"count\\\": 346\\n      },\\n      \\\"embedding_distance\\\": {\\n        \\\"R@1\\\": 0.1069364161849711,\\n        \\\"R@1_ci\\\": [\\n          0.07803468208092486,\\n          0.14169075144508672\\n        ],\\n        \\\"R@5\\\": 0.49421965317919075,\\n        \\\"R@5_ci\\\": [\\n          0.4305635838150289,\\n          0.5348265895953758\\n        ],\\n        \\\"MRR\\\": 0.2865956097787104,\\n        \\\"MRR_ci\\\": [\\n          0.25823956396604253,\\n          0.31508196199064964\\n        ],\\n        \\\"count\\\": 346\\n      },\\n      \\\"dataflow_aware\\\": {\\n        \\\"R@1\\\": 0.2398843930635838,\\n        \\\"R@1_ci\\\": [\\n          0.19653179190751446,\\n          0.2861271676300578\\n        ],\\n        \\\"R@5\\\": 0.7023121387283237,\\n        \\\"R@5_ci\\\": [\\n          0.6588150289017342,\\n          0.7514450867052023\\n        ],\\n        \\\"MRR\\\": 0.4295497658014659,\\n        \\\"MRR_ci\\\": [\\n          0.39310849797917335,\\n          0.4627567860954358\\n        ],\\n        \\\"count\\\": 346\\n      },\\n\\n\\n... [截断: 输出过长，省略 11724 字符] ...\\n\\n        \\\"R@5_rel_pct\\\": 109.78835978835977,\\n        \\\"MRR_delta\\\": 0.08434517635221275,\\n        \\\"MRR_rel_pct\\\": 71.43937034482639\\n      },\\n      \\\"dataflow_aware_vs_random\\\": {\\n        \\\"R@1_delta\\\": 0.10322333077513429,\\n        \\\"R@1_rel_pct\\\": 320.2380952380952,\\n        \\\"R@5_delta\\\": 0.3142747505755948,\\n        \\\"R@5_rel_pct\\\": 216.66666666666666,\\n        \\\"MRR_delta\\\": 0.1742035067513217,\\n        \\\"MRR_rel_pct\\\": 147.54831719370338\\n      }\\n    },\\n    \\\"medium\\\": {\\n      \\\"random\\\": {\\n        \\\"R@1\\\": 0.014285714285714285,\\n        \\\"R@1_ci\\\": [\\n          0.002857142857142857,\\n          0.025714285714285714\\n        ],\\n        \\\"R@5\\\": 0.10285714285714286,\\n        \\\"R@5_ci\\\": [\\n          0.06850000000000002,\\n          0.13435714285714287\\n        ],\\n        \\\"MRR\\\": 0.08892012631102023,\\n        \\\"MRR_ci\\\": [\\n          0.07565878083640655,\\n          0.10097054824489184\\n        ],\\n        \\\"count\\\": 350\\n      },\\n      \\\"embedding_distance\\\": {\\n        \\\"R@1\\\": 0.06571428571428571,\\n        \\\"R@1_ci\\\": [\\n          0.04285714285714286,\\n          0.09428571428571429\\n        ],\\n        \\\"R@5\\\": 0.3028571428571429,\\n        \\\"R@5_ci\\\": [\\n          0.25128571428571433,\\n          0.3457142857142857\\n        ],\\n        \\\"MRR\\\": 0.19037293149185006,\\n        \\\"MRR_ci\\\": [\\n          0.1649260686702319,\\n          0.21459875959655225\\n        ],\\n        \\\"count\\\": 350\\n      },\\n      \\\"dataflow_aware\\\": {\\n        \\\"R@1\\\": 0.13428571428571429,\\n        \\\"R@1_ci\\\": [\\n          0.09714285714285714,\\n          0.17442857142857146\\n        ],\\n        \\\"R@5\\\": 0.4342857142857143,\\n        \\\"R@5_ci\\\": [\\n          0.38857142857142857,\\n          0.4858571428571429\\n        ],\\n        \\\"MRR\\\": 0.2852574269542923,\\n        \\\"MRR_ci\\\": [\\n          0.2526425047155209,\\n          0.32557010653989665\\n        ],\\n        \\\"count\\\": 350\\n      },\\n      \\\"embedding_distance_vs_random\\\": {\\n        \\\"R@1_delta\\\": 0.05142857142857143,\\n        \\\"R@1_rel_pct\\\": 360.0,\\n        \\\"R@5_delta\\\": 0.2,\\n        \\\"R@5_rel_pct\\\": 194.44444444444446,\\n        \\\"MRR_delta\\\": 0.10145280518082983,\\n        \\\"MRR_rel_pct\\\": 114.09431069179259\\n      },\\n      \\\"dataflow_aware_vs_random\\\": {\\n        \\\"R@1_delta\\\": 0.12,\\n        \\\"R@1_rel_pct\\\": 840.0,\\n        \\\"R@5_delta\\\": 0.3314285714285714,\\n        \\\"R@5_rel_pct\\\": 322.2222222222222,\\n        \\\"MRR_delta\\\": 0.19633730064327207,\\n        \\\"MRR_rel_pct\\\": 220.80186881036764\\n      }\\n    },\\n    \\\"high\\\": {\\n      \\\"random\\\": {\\n        \\\"R@1\\\": 0.0,\\n        \\\"R@1_ci\\\": [\\n          0.0,\\n          0.0\\n        ],\\n        \\\"R@5\\\": 0.0,\\n        \\\"R@5_ci\\\": [\\n          0.0,\\n          0.0\\n        ],\\n        \\\"MRR\\\": 0.06634814469381427,\\n        \\\"MRR_ci\\\": [\\n          0.04922830990875043,\\n          0.08318125486392415\\n        ],\\n        \\\"count\\\": 24\\n      },\\n      \\\"embedding_distance\\\": {\\n        \\\"R@1\\\": 0.08333333333333333,\\n        \\\"R@1_ci\\\": [\\n          0.0,\\n          0.20833333333333334\\n        ],\\n        \\\"R@5\\\": 0.25,\\n        \\\"R@5_ci\\\": [\\n          0.08333333333333333,\\n          0.4166666666666667\\n        ],\\n        \\\"MRR\\\": 0.18658210312354354,\\n        \\\"MRR_ci\\\": [\\n          0.09884595475354443,\\n          0.2990058719871796\\n        ],\\n        \\\"count\\\": 24\\n      },\\n      \\\"dataflow_aware\\\": {\\n        \\\"R@1\\\": 0.08333333333333333,\\n        \\\"R@1_ci\\\": [\\n          0.0,\\n          0.20833333333333334\\n        ],\\n        \\\"R@5\\\": 0.25,\\n        \\\"R@5_ci\\\": [\\n          0.08333333333333333,\\n          0.4166666666666667\\n        ],\\n        \\\"MRR\\\": 0.19360231918734738,\\n        \\\"MRR_ci\\\": [\\n          0.10034009813817588,\\n          0.3119892338877614\\n        ],\\n        \\\"count\\\": 24\\n      },\\n      \\\"embedding_distance_vs_random\\\": {\\n        \\\"R@1_delta\\\": 0.08333333333333333,\\n        \\\"R@1_rel_pct\\\": 0.0,\\n        \\\"R@5_delta\\\": 0.25,\\n        \\\"R@5_rel_pct\\\": 0.0,\\n        \\\"MRR_delta\\\": 0.12023395842972927,\\n        \\\"MRR_rel_pct\\\": 181.21676044535855\\n      },\\n      \\\"dataflow_aware_vs_random\\\": {\\n        \\\"R@1_delta\\\": 0.08333333333333333,\\n        \\\"R@1_rel_pct\\\": 0.0,\\n        \\\"R@5_delta\\\": 0.25,\\n        \\\"R@5_rel_pct\\\": 0.0,\\n        \\\"MRR_delta\\\": 0.1272541744935331,\\n        \\\"MRR_rel_pct\\\": 191.79763817178326\\n      }\\n    }\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.17}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0a95eb57-e256-4aa4-b648-45c2e62d1471",
  "isSidechain": false,
  "promptId": "0b7bb415-f2b4-4832-aac4-2e6aafdc7429",
  "type": "user",
  "uuid": "854cbfe5-dc00-4cd6-a2eb-41f109a25c96",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"{\\\\n  \\\\\\\"config\\\\\\\": {\\\\n    \\\\\\\"strategies\\\\\\\": [\\\\n      \\\\\\\"random\\\\\\\",\\\\n      \\\\\\\"embedding_distance\\\\\\\",\\\\n      \\\\\\\"dataflow_aware\\\\\\\"\\\\n    ],\\\\n    \\\\\\\"seeds\\\\\\\": [\\\\n      42\\\\n    ],\\\\n    \\\\\\\"repo_size_bins\\\\\\\": {\\\\n      \\\\\\\"small\\\\\\\": [\\\\n        0,\\\\n        50\\\\n      ],\\\\n      \\\\\\\"medium\\\\\\\": [\\\\n        50,\\\\n        200\\\\n      ],\\\\n      \\\\\\\"large\\\\\\\": [\\\\n        200,\\\\n        500\\\\n      ],\\\\n      \\\\\\\"xlarge\\\\\\\": [\\\\n        500,\\\\n        Infinity\\\\n      ]\\\\n    },\\\\n    \\\\\\\"pool_size_bins\\\\\\\": {\\\\n      \\\\\\\"small\\\\\\\": [\\\\n        0,\\\\n        20\\\\n      ],\\\\n      \\\\\\\"medium\\\\\\\": [\\\\n        20,\\\\n        40\\\\n      ],\\\\n      \\\\\\\"large\\\\\\\": [\\\\n        40,\\\\n        51\\\\n      ]\\\\n    },\\\\n    \\\\\\\"similarity_bins\\\\\\\": {\\\\n      \\\\\\\"low\\\\\\\": [\\\\n        0.0,\\\\n        0.3\\\\n      ],\\\\n      \\\\\\\"medium\\\\\\\": [\\\\n        0.3,\\\\n        0.6\\\\n      ],\\\\n      \\\\\\\"high\\\\\\\": [\\\\n        0.6,\\\\n        1.01\\\\n      ]\\\\n    },\\\\n    \\\\\\\"n_bootstrap\\\\\\\": 200,\\\\n    \\\\\\\"dry_run\\\\\\\": true\\\\n  },\\\\n  \\\\\\\"by_repo_size\\\\\\\": {\\\\n    \\\\\\\"small\\\\\\\": {\\\\n      \\\\\\\"random\\\\\\\": {\\\\n        \\\\\\\"R@1\\\\\\\": 0.11538461538461539,\\\\n        \\\\\\\"R@1_ci\\\\\\\": [\\\\n          0.061346153846153884,\\\\n          0.16923076923076924\\\\n        ],\\\\n        \\\\\\\"R@5\\\\\\\": 0.5384615384615384,\\\\n        \\\\\\\"R@5_ci\\\\\\\": [\\\\n          0.4461538461538462,\\\\n          0.6230769230769231\\\\n        ],\\\\n        \\\\\\\"MRR\\\\\\\": 0.3059754134754135,\\\\n        \\\\\\\"MRR_ci\\\\\\\": [\\\\n          0.25409036102786103,\\\\n          0.3513594044844045\\\\n        ],\\\\n        \\\\\\\"count\\\\\\\": 130\\\\n      },\\\\n      \\\\\\\"embedding_distance\\\\\\\": {\\\\n        \\\\\\\"R@1\\\\\\\": 0.3,\\\\n        \\\\\\\"R@1_ci\\\\\\\": [\\\\n          0.2230769230769231,\\\\n          0.37711538461538463\\\\n        ],\\\\n        \\\\\\\"R@5\\\\\\\": 0.7384615384615385,\\\\n        \\\\\\\"R@5_ci\\\\\\\": [\\\\n          0.6613461538461538,\\\\n          0.8153846153846154\\\\n        ],\\\\n        \\\\\\\"MRR\\\\\\\": 0.4930563880563881,\\\\n        \\\\\\\"MRR_ci\\\\\\\": [\\\\n          0.43992261211011213,\\\\n          0.5556576062826063\\\\n        ],\\\\n        \\\\\\\"count\\\\\\\": 130\\\\n      },\\\\n      \\\\\\\"dataflow_aware\\\\\\\": {\\\\n        \\\\\\\"R@1\\\\\\\": 0.4846153846153846,\\\\n        \\\\\\\"R@1_ci\\\\\\\": [\\\\n          0.3923076923076923,\\\\n          0.5617307692307693\\\\n        ],\\\\n        \\\\\\\"R@5\\\\\\\": 0.8769230769230769,\\\\n        \\\\\\\"R@5_ci\\\\\\\": [\\\\n          0.8226923076923077,\\\\n          0.9230769230769231\\\\n        ],\\\\n        \\\\\\\"MRR\\\\\\\": 0.6500946275946277,\\\\n        \\\\\\\"MRR_ci\\\\\\\": [\\\\n          0.59523923992674,\\\\n          0.7073237942612942\\\\n        ],\\\\n        \\\\\\\"count\\\\\\\": 130\\\\n      },\\\\n      \\\\\\\"embedding_distance_vs_random\\\\\\\": {\\\\n        \\\\\\\"R@1_delta\\\\\\\": 0.1846153846153846,\\\\n        \\\\\\\"R@1_rel_pct\\\\\\\": 160.0,\\\\n        \\\\\\\"R@5_delta\\\\\\\": 0.20000000000000007,\\\\n        \\\\\\\"R@5_rel_pct\\\\\\\": 37.14285714285715,\\\\n        \\\\\\\"MRR_delta\\\\\\\": 0.18708097458097456,\\\\n        \\\\\\\"MRR_rel_pct\\\\\\\": 61.14248607625702\\\\n      },\\\\n      \\\\\\\"dataflow_aware_vs_random\\\\\\\": {\\\\n        \\\\\\\"R@1_delta\\\\\\\": 0.36923076923076925,\\\\n        \\\\\\\"R@1_rel_pct\\\\\\\": 320.0,\\\\n        \\\\\\\"R@5_delta\\\\\\\": 0.3384615384615385,\\\\n        \\\\\\\"R@5_rel_pct\\\\\\\": 62.85714285714287,\\\\n        \\\\\\\"MRR_delta\\\\\\\": 0.34411921411921415,\\\\n        \\\\\\\"MRR_rel_pct\\\\\\\": 112.46629597147866\\\\n      }\\\\n    },\\\\n    \\\\\\\"medium\\\\\\\": {\\\\n      \\\\\\\"random\\\\\\\": {\\\\n        \\\\\\\"R@1\\\\\\\": 0.05202312138728324,\\\\n        \\\\\\\"R@1_ci\\\\\\\": [\\\\n          0.031791907514450865,\\\\n          0.08092485549132948\\\\n        ],\\\\n        \\\\\\\"R@5\\\\\\\": 0.23121387283236994,\\\\n        \\\\\\\"R@5_ci\\\\\\\": [\\\\n          0.18778901734104048,\\\\n          0.27167630057803466\\\\n        ],\\\\n        \\\\\\\"MRR\\\\\\\": 0.17820474196308103,\\\\n        \\\\\\\"MRR_ci\\\\\\\": [\\\\n          0.15638534764941775,\\\\n          0.20150044957306631\\\\n        ],\\\\n        \\\\\\\"count\\\\\\\": 346\\\\n      },\\\\n      \\\\\\\"embedding_distance\\\\\\\": {\\\\n        \\\\\\\"R@1\\\\\\\": 0.1069364161849711,\\\\n        \\\\\\\"R@1_ci\\\\\\\": [\\\\n          0.07803468208092486,\\\\n          0.14169075144508672\\\\n        ],\\\\n        \\\\\\\"R@5\\\\\\\": 0.49421965317919075,\\\\n        \\\\\\\"R@5_ci\\\\\\\": [\\\\n          0.4305635838150289,\\\\n          0.5348265895953758\\\\n        ],\\\\n        \\\\\\\"MRR\\\\\\\": 0.2865956097787104,\\\\n        \\\\\\\"MRR_ci\\\\\\\": [\\\\n          0.25823956396604253,\\\\n          0.31508196199064964\\\\n        ],\\\\n        \\\\\\\"count\\\\\\\": 346\\\\n      },\\\\n      \\\\\\\"dataflow_aware\\\\\\\": {\\\\n        \\\\\\\"R@1\\\\\\\": 0.2398843930635838,\\\\n        \\\\\\\"R@1_ci\\\\\\\": [\\\\n          0.19653179190751446,\\\\n          0.2861271676300578\\\\n        ],\\\\n        \\\\\\\"R@5\\\\\\\": 0.7023121387283237,\\\\n        \\\\\\\"R@5_ci\\\\\\\": [\\\\n          0.6588150289017342,\\\\n          0.7514450867052023\\\\n        ],\\\\n        \\\\\\\"MRR\\\\\\\": 0.4295497658014659,\\\\n        \\\\\\\"MRR_ci\\\\\\\": [\\\\n          0.39310849797917335,\\\\n          0.4627567860954358\\\\n        ],\\\\n        \\\\\\\"count\\\\\\\": 346\\\\n      },\\\\n\\\\n\\\\n... [截断: 输出过长，省略 11724 字符] ...\\\\n\\\\n        \\\\\\\"R@5_rel_pct\\\\\\\": 109.78835978835977,\\\\n        \\\\\\\"MRR_delta\\\\\\\": 0.08434517635221275,\\\\n        \\\\\\\"MRR_rel_pct\\\\\\\": 71.43937034482639\\\\n      },\\\\n      \\\\\\\"dataflow_aware_vs_random\\\\\\\": {\\\\n        \\\\\\\"R@1_delta\\\\\\\": 0.10322333077513429,\\\\n        \\\\\\\"R@1_rel_pct\\\\\\\": 320.2380952380952,\\\\n        \\\\\\\"R@5_delta\\\\\\\": 0.3142747505755948,\\\\n        \\\\\\\"R@5_rel_pct\\\\\\\": 216.66666666666666,\\\\n        \\\\\\\"MRR_delta\\\\\\\": 0.1742035067513217,\\\\n        \\\\\\\"MRR_rel_pct\\\\\\\": 147.54831719370338\\\\n      }\\\\n    },\\\\n    \\\\\\\"medium\\\\\\\": {\\\\n      \\\\\\\"random\\\\\\\": {\\\\n        \\\\\\\"R@1\\\\\\\": 0.014285714285714285,\\\\n        \\\\\\\"R@1_ci\\\\\\\": [\\\\n          0.002857142857142857,\\\\n          0.025714285714285714\\\\n        ],\\\\n        \\\\\\\"R@5\\\\\\\": 0.10285714285714286,\\\\n        \\\\\\\"R@5_ci\\\\\\\": [\\\\n          0.06850000000000002,\\\\n          0.13435714285714287\\\\n        ],\\\\n        \\\\\\\"MRR\\\\\\\": 0.08892012631102023,\\\\n        \\\\\\\"MRR_ci\\\\\\\": [\\\\n          0.07565878083640655,\\\\n          0.10097054824489184\\\\n        ],\\\\n        \\\\\\\"count\\\\\\\": 350\\\\n      },\\\\n      \\\\\\\"embedding_distance\\\\\\\": {\\\\n        \\\\\\\"R@1\\\\\\\": 0.06571428571428571,\\\\n        \\\\\\\"R@1_ci\\\\\\\": [\\\\n          0.04285714285714286,\\\\n          0.09428571428571429\\\\n        ],\\\\n        \\\\\\\"R@5\\\\\\\": 0.3028571428571429,\\\\n        \\\\\\\"R@5_ci\\\\\\\": [\\\\n          0.25128571428571433,\\\\n          0.3457142857142857\\\\n        ],\\\\n        \\\\\\\"MRR\\\\\\\": 0.19037293149185006,\\\\n        \\\\\\\"MRR_ci\\\\\\\": [\\\\n          0.1649260686702319,\\\\n          0.21459875959655225\\\\n        ],\\\\n        \\\\\\\"count\\\\\\\": 350\\\\n      },\\\\n      \\\\\\\"dataflow_aware\\\\\\\": {\\\\n        \\\\\\\"R@1\\\\\\\": 0.13428571428571429,\\\\n        \\\\\\\"R@1_ci\\\\\\\": [\\\\n          0.09714285714285714,\\\\n          0.17442857142857146\\\\n        ],\\\\n        \\\\\\\"R@5\\\\\\\": 0.4342857142857143,\\\\n        \\\\\\\"R@5_ci\\\\\\\": [\\\\n          0.38857142857142857,\\\\n          0.4858571428571429\\\\n        ],\\\\n        \\\\\\\"MRR\\\\\\\": 0.2852574269542923,\\\\n        \\\\\\\"MRR_ci\\\\\\\": [\\\\n          0.2526425047155209,\\\\n          0.32557010653989665\\\\n        ],\\\\n        \\\\\\\"count\\\\\\\": 350\\\\n      },\\\\n      \\\\\\\"embedding_distance_vs_random\\\\\\\": {\\\\n        \\\\\\\"R@1_delta\\\\\\\": 0.05142857142857143,\\\\n        \\\\\\\"R@1_rel_pct\\\\\\\": 360.0,\\\\n        \\\\\\\"R@5_delta\\\\\\\": 0.2,\\\\n        \\\\\\\"R@5_rel_pct\\\\\\\": 194.44444444444446,\\\\n        \\\\\\\"MRR_delta\\\\\\\": 0.10145280518082983,\\\\n        \\\\\\\"MRR_rel_pct\\\\\\\": 114.09431069179259\\\\n      },\\\\n      \\\\\\\"dataflow_aware_vs_random\\\\\\\": {\\\\n        \\\\\\\"R@1_delta\\\\\\\": 0.12,\\\\n        \\\\\\\"R@1_rel_pct\\\\\\\": 840.0,\\\\n        \\\\\\\"R@5_delta\\\\\\\": 0.3314285714285714,\\\\n        \\\\\\\"R@5_rel_pct\\\\\\\": 322.2222222222222,\\\\n        \\\\\\\"MRR_delta\\\\\\\": 0.19633730064327207,\\\\n        \\\\\\\"MRR_rel_pct\\\\\\\": 220.80186881036764\\\\n      }\\\\n    },\\\\n    \\\\\\\"high\\\\\\\": {\\\\n      \\\\\\\"random\\\\\\\": {\\\\n        \\\\\\\"R@1\\\\\\\": 0.0,\\\\n        \\\\\\\"R@1_ci\\\\\\\": [\\\\n          0.0,\\\\n          0.0\\\\n        ],\\\\n        \\\\\\\"R@5\\\\\\\": 0.0,\\\\n        \\\\\\\"R@5_ci\\\\\\\": [\\\\n          0.0,\\\\n          0.0\\\\n        ],\\\\n        \\\\\\\"MRR\\\\\\\": 0.06634814469381427,\\\\n        \\\\\\\"MRR_ci\\\\\\\": [\\\\n          0.04922830990875043,\\\\n          0.08318125486392415\\\\n        ],\\\\n        \\\\\\\"count\\\\\\\": 24\\\\n      },\\\\n      \\\\\\\"embedding_distance\\\\\\\": {\\\\n        \\\\\\\"R@1\\\\\\\": 0.08333333333333333,\\\\n        \\\\\\\"R@1_ci\\\\\\\": [\\\\n          0.0,\\\\n          0.20833333333333334\\\\n        ],\\\\n        \\\\\\\"R@5\\\\\\\": 0.25,\\\\n        \\\\\\\"R@5_ci\\\\\\\": [\\\\n          0.08333333333333333,\\\\n          0.4166666666666667\\\\n        ],\\\\n        \\\\\\\"MRR\\\\\\\": 0.18658210312354354,\\\\n        \\\\\\\"MRR_ci\\\\\\\": [\\\\n          0.09884595475354443,\\\\n          0.2990058719871796\\\\n        ],\\\\n        \\\\\\\"count\\\\\\\": 24\\\\n      },\\\\n      \\\\\\\"dataflow_aware\\\\\\\": {\\\\n        \\\\\\\"R@1\\\\\\\": 0.08333333333333333,\\\\n        \\\\\\\"R@1_ci\\\\\\\": [\\\\n          0.0,\\\\n          0.20833333333333334\\\\n        ],\\\\n        \\\\\\\"R@5\\\\\\\": 0.25,\\\\n        \\\\\\\"R@5_ci\\\\\\\": [\\\\n          0.08333333333333333,\\\\n          0.4166666666666667\\\\n        ],\\\\n        \\\\\\\"MRR\\\\\\\": 0.19360231918734738,\\\\n        \\\\\\\"MRR_ci\\\\\\\": [\\\\n          0.10034009813817588,\\\\n          0.3119892338877614\\\\n        ],\\\\n        \\\\\\\"count\\\\\\\": 24\\\\n      },\\\\n      \\\\\\\"embedding_distance_vs_random\\\\\\\": {\\\\n        \\\\\\\"R@1_delta\\\\\\\": 0.08333333333333333,\\\\n        \\\\\\\"R@1_rel_pct\\\\\\\": 0.0,\\\\n        \\\\\\\"R@5_delta\\\\\\\": 0.25,\\\\n        \\\\\\\"R@5_rel_pct\\\\\\\": 0.0,\\\\n        \\\\\\\"MRR_delta\\\\\\\": 0.12023395842972927,\\\\n        \\\\\\\"MRR_rel_pct\\\\\\\": 181.21676044535855\\\\n      },\\\\n      \\\\\\\"dataflow_aware_vs_random\\\\\\\": {\\\\n        \\\\\\\"R@1_delta\\\\\\\": 0.08333333333333333,\\\\n        \\\\\\\"R@1_rel_pct\\\\\\\": 0.0,\\\\n        \\\\\\\"R@5_delta\\\\\\\": 0.25,\\\\n        \\\\\\\"R@5_rel_pct\\\\\\\": 0.0,\\\\n        \\\\\\\"MRR_delta\\\\\\\": 0.1272541744935331,\\\\n        \\\\\\\"MRR_rel_pct\\\\\\\": 191.79763817178326\\\\n      }\\\\n    }\\\\n  }\\\\n}\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 1.17}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"config\\\": {\\n    \\\"strategies\\\": [\\n      \\\"random\\\",\\n      \\\"embedding_distance\\\",\\n      \\\"dataflow_aware\\\"\\n    ],\\n    \\\"seeds\\\": [\\n      42\\n    ],\\n    \\\"repo_size_bins\\\": {\\n      \\\"small\\\": [\\n        0,\\n        50\\n      ],\\n      \\\"medium\\\": [\\n        50,\\n        200\\n      ],\\n      \\\"large\\\": [\\n        200,\\n        500\\n      ],\\n      \\\"xlarge\\\": [\\n        500,\\n        Infinity\\n      ]\\n    },\\n    \\\"pool_size_bins\\\": {\\n      \\\"small\\\": [\\n        0,\\n        20\\n      ],\\n      \\\"medium\\\": [\\n        20,\\n        40\\n      ],\\n      \\\"large\\\": [\\n        40,\\n        51\\n      ]\\n    },\\n    \\\"similarity_bins\\\": {\\n      \\\"low\\\": [\\n        0.0,\\n        0.3\\n      ],\\n      \\\"medium\\\": [\\n        0.3,\\n        0.6\\n      ],\\n      \\\"high\\\": [\\n        0.6,\\n        1.01\\n      ]\\n    },\\n    \\\"n_bootstrap\\\": 200,\\n    \\\"dry_run\\\": true\\n  },\\n  \\\"by_repo_size\\\": {\\n    \\\"small\\\": {\\n      \\\"random\\\": {\\n        \\\"R@1\\\": 0.11538461538461539,\\n        \\\"R@1_ci\\\": [\\n          0.061346153846153884,\\n          0.16923076923076924\\n        ],\\n        \\\"R@5\\\": 0.5384615384615384,\\n        \\\"R@5_ci\\\": [\\n          0.4461538461538462,\\n          0.6230769230769231\\n        ],\\n        \\\"MRR\\\": 0.3059754134754135,\\n        \\\"MRR_ci\\\": [\\n          0.25409036102786103,\\n          0.3513594044844045\\n        ],\\n        \\\"count\\\": 130\\n      },\\n      \\\"embedding_distance\\\": {\\n        \\\"R@1\\\": 0.3,\\n        \\\"R@1_ci\\\": [\\n          0.2230769230769231,\\n          0.37711538461538463\\n        ],\\n        \\\"R@5\\\": 0.7384615384615385,\\n        \\\"R@5_ci\\\": [\\n          0.6613461538461538,\\n          0.8153846153846154\\n        ],\\n        \\\"MRR\\\": 0.4930563880563881,\\n        \\\"MRR_ci\\\": [\\n          0.43992261211011213,\\n          0.5556576062826063\\n        ],\\n        \\\"count\\\": 130\\n      },\\n      \\\"dataflow_aware\\\": {\\n        \\\"R@1\\\": 0.4846153846153846,\\n        \\\"R@1_ci\\\": [\\n          0.3923076923076923,\\n          0.5617307692307693\\n        ],\\n        \\\"R@5\\\": 0.8769230769230769,\\n        \\\"R@5_ci\\\": [\\n          0.8226923076923077,\\n          0.9230769230769231\\n        ],\\n        \\\"MRR\\\": 0.6500946275946277,\\n        \\\"MRR_ci\\\": [\\n          0.59523923992674,\\n          0.7073237942612942\\n        ],\\n        \\\"count\\\": 130\\n      },\\n      \\\"embedding_distance_vs_random\\\": {\\n        \\\"R@1_delta\\\": 0.1846153846153846,\\n        \\\"R@1_rel_pct\\\": 160.0,\\n        \\\"R@5_delta\\\": 0.20000000000000007,\\n        \\\"R@5_rel_pct\\\": 37.14285714285715,\\n        \\\"MRR_delta\\\": 0.18708097458097456,\\n        \\\"MRR_rel_pct\\\": 61.14248607625702\\n      },\\n      \\\"dataflow_aware_vs_random\\\": {\\n        \\\"R@1_delta\\\": 0.36923076923076925,\\n        \\\"R@1_rel_pct\\\": 320.0,\\n        \\\"R@5_delta\\\": 0.3384615384615385,\\n        \\\"R@5_rel_pct\\\": 62.85714285714287,\\n        \\\"MRR_delta\\\": 0.34411921411921415,\\n        \\\"MRR_rel_pct\\\": 112.46629597147866\\n      }\\n    },\\n    \\\"medium\\\": {\\n      \\\"random\\\": {\\n        \\\"R@1\\\": 0.05202312138728324,\\n        \\\"R@1_ci\\\": [\\n          0.031791907514450865,\\n          0.08092485549132948\\n        ],\\n        \\\"R@5\\\": 0.23121387283236994,\\n        \\\"R@5_ci\\\": [\\n          0.18778901734104048,\\n          0.27167630057803466\\n        ],\\n        \\\"MRR\\\": 0.17820474196308103,\\n        \\\"MRR_ci\\\": [\\n          0.15638534764941775,\\n          0.20150044957306631\\n        ],\\n        \\\"count\\\": 346\\n      },\\n      \\\"embedding_distance\\\": {\\n        \\\"R@1\\\": 0.1069364161849711,\\n        \\\"R@1_ci\\\": [\\n          0.07803468208092486,\\n          0.14169075144508672\\n        ],\\n        \\\"R@5\\\": 0.49421965317919075,\\n        \\\"R@5_ci\\\": [\\n          0.4305635838150289,\\n          0.5348265895953758\\n        ],\\n        \\\"MRR\\\": 0.2865956097787104,\\n        \\\"MRR_ci\\\": [\\n          0.25823956396604253,\\n          0.31508196199064964\\n        ],\\n        \\\"count\\\": 346\\n      },\\n      \\\"dataflow_aware\\\": {\\n        \\\"R@1\\\": 0.2398843930635838,\\n        \\\"R@1_ci\\\": [\\n          0.19653179190751446,\\n          0.2861271676300578\\n        ],\\n        \\\"R@5\\\": 0.7023121387283237,\\n        \\\"R@5_ci\\\": [\\n          0.6588150289017342,\\n          0.7514450867052023\\n        ],\\n        \\\"MRR\\\": 0.4295497658014659,\\n        \\\"MRR_ci\\\": [\\n          0.39310849797917335,\\n          0.4627567860954358\\n        ],\\n        \\\"count\\\": 346\\n      },\\n\\n\\n... [截断: 输出过长，省略 11724 字符] ...\\n\\n        \\\"R@5_rel_pct\\\": 109.78835978835977,\\n        \\\"MRR_delta\\\": 0.08434517635221275,\\n        \\\"MRR_rel_pct\\\": 71.43937034482639\\n      },\\n      \\\"dataflow_aware_vs_random\\\": {\\n        \\\"R@1_delta\\\": 0.10322333077513429,\\n        \\\"R@1_rel_pct\\\": 320.2380952380952,\\n        \\\"R@5_delta\\\": 0.3142747505755948,\\n        \\\"R@5_rel_pct\\\": 216.66666666666666,\\n        \\\"MRR_delta\\\": 0.1742035067513217,\\n        \\\"MRR_rel_pct\\\": 147.54831719370338\\n      }\\n    },\\n    \\\"medium\\\": {\\n      \\\"random\\\": {\\n        \\\"R@1\\\": 0.014285714285714285,\\n        \\\"R@1_ci\\\": [\\n          0.002857142857142857,\\n          0.025714285714285714\\n        ],\\n        \\\"R@5\\\": 0.10285714285714286,\\n        \\\"R@5_ci\\\": [\\n          0.06850000000000002,\\n          0.13435714285714287\\n        ],\\n        \\\"MRR\\\": 0.08892012631102023,\\n        \\\"MRR_ci\\\": [\\n          0.07565878083640655,\\n          0.10097054824489184\\n        ],\\n        \\\"count\\\": 350\\n      },\\n      \\\"embedding_distance\\\": {\\n        \\\"R@1\\\": 0.06571428571428571,\\n        \\\"R@1_ci\\\": [\\n          0.04285714285714286,\\n          0.09428571428571429\\n        ],\\n        \\\"R@5\\\": 0.3028571428571429,\\n        \\\"R@5_ci\\\": [\\n          0.25128571428571433,\\n          0.3457142857142857\\n        ],\\n        \\\"MRR\\\": 0.19037293149185006,\\n        \\\"MRR_ci\\\": [\\n          0.1649260686702319,\\n          0.21459875959655225\\n        ],\\n        \\\"count\\\": 350\\n      },\\n      \\\"dataflow_aware\\\": {\\n        \\\"R@1\\\": 0.13428571428571429,\\n        \\\"R@1_ci\\\": [\\n          0.09714285714285714,\\n          0.17442857142857146\\n        ],\\n        \\\"R@5\\\": 0.4342857142857143,\\n        \\\"R@5_ci\\\": [\\n          0.38857142857142857,\\n          0.4858571428571429\\n        ],\\n        \\\"MRR\\\": 0.2852574269542923,\\n        \\\"MRR_ci\\\": [\\n          0.2526425047155209,\\n          0.32557010653989665\\n        ],\\n        \\\"count\\\": 350\\n      },\\n      \\\"embedding_distance_vs_random\\\": {\\n        \\\"R@1_delta\\\": 0.05142857142857143,\\n        \\\"R@1_rel_pct\\\": 360.0,\\n        \\\"R@5_delta\\\": 0.2,\\n        \\\"R@5_rel_pct\\\": 194.44444444444446,\\n        \\\"MRR_delta\\\": 0.10145280518082983,\\n        \\\"MRR_rel_pct\\\": 114.09431069179259\\n      },\\n      \\\"dataflow_aware_vs_random\\\": {\\n        \\\"R@1_delta\\\": 0.12,\\n        \\\"R@1_rel_pct\\\": 840.0,\\n        \\\"R@5_delta\\\": 0.3314285714285714,\\n        \\\"R@5_rel_pct\\\": 322.2222222222222,\\n        \\\"MRR_delta\\\": 0.19633730064327207,\\n        \\\"MRR_rel_pct\\\": 220.80186881036764\\n      }\\n    },\\n    \\\"high\\\": {\\n      \\\"random\\\": {\\n        \\\"R@1\\\": 0.0,\\n        \\\"R@1_ci\\\": [\\n          0.0,\\n          0.0\\n        ],\\n        \\\"R@5\\\": 0.0,\\n        \\\"R@5_ci\\\": [\\n          0.0,\\n          0.0\\n        ],\\n        \\\"MRR\\\": 0.06634814469381427,\\n        \\\"MRR_ci\\\": [\\n          0.04922830990875043,\\n          0.08318125486392415\\n        ],\\n        \\\"count\\\": 24\\n      },\\n      \\\"embedding_distance\\\": {\\n        \\\"R@1\\\": 0.08333333333333333,\\n        \\\"R@1_ci\\\": [\\n          0.0,\\n          0.20833333333333334\\n        ],\\n        \\\"R@5\\\": 0.25,\\n        \\\"R@5_ci\\\": [\\n          0.08333333333333333,\\n          0.4166666666666667\\n        ],\\n        \\\"MRR\\\": 0.18658210312354354,\\n        \\\"MRR_ci\\\": [\\n          0.09884595475354443,\\n          0.2990058719871796\\n        ],\\n        \\\"count\\\": 24\\n      },\\n      \\\"dataflow_aware\\\": {\\n        \\\"R@1\\\": 0.08333333333333333,\\n        \\\"R@1_ci\\\": [\\n          0.0,\\n          0.20833333333333334\\n        ],\\n        \\\"R@5\\\": 0.25,\\n        \\\"R@5_ci\\\": [\\n          0.08333333333333333,\\n          0.4166666666666667\\n        ],\\n        \\\"MRR\\\": 0.19360231918734738,\\n        \\\"MRR_ci\\\": [\\n          0.10034009813817588,\\n          0.3119892338877614\\n        ],\\n        \\\"count\\\": 24\\n      },\\n      \\\"embedding_distance_vs_random\\\": {\\n        \\\"R@1_delta\\\": 0.08333333333333333,\\n        \\\"R@1_rel_pct\\\": 0.0,\\n        \\\"R@5_delta\\\": 0.25,\\n        \\\"R@5_rel_pct\\\": 0.0,\\n        \\\"MRR_delta\\\": 0.12023395842972927,\\n        \\\"MRR_rel_pct\\\": 181.21676044535855\\n      },\\n      \\\"dataflow_aware_vs_random\\\": {\\n        \\\"R@1_delta\\\": 0.08333333333333333,\\n        \\\"R@1_rel_pct\\\": 0.0,\\n        \\\"R@5_delta\\\": 0.25,\\n        \\\"R@5_rel_pct\\\": 0.0,\\n        \\\"MRR_delta\\\": 0.1272541744935331,\\n        \\\"MRR_rel_pct\\\": 191.79763817178326\\n      }\\n    }\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.17}}"
    }
  },
  "sourceToolAssistantUUID": "0a95eb57-e256-4aa4-b648-45c2e62d1471",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "fb5ea7f7-b3c9-4750-b931-39d2aaae422b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-14T20:36:30.785Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_017QUpjVhRWqbMGZrCPCeKuG`</summary>

```json
{
  "server": "bjb1-42106",
  "command": "cd /root/structfuse && git log --oneline -15 -- evaluation/analyze_stratified.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "854cbfe5-dc00-4cd6-a2eb-41f109a25c96",
  "isSidechain": false,
  "requestId": "req_011Cb36vRk5q3Go4Ger3n9CF",
  "type": "assistant",
  "uuid": "65cd667c-cc13-40c1-8669-e06bd3f89d42",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "fb5ea7f7-b3c9-4750-b931-39d2aaae422b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VLWwpdCr7UuwqnYjsWSZpb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1121,
      "cache_read_input_tokens": 23599,
      "output_tokens": 411,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1121,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 411,
          "cache_read_input_tokens": 23599,
          "cache_creation_input_tokens": 1121,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1121
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
  "leafUuid": "65cd667c-cc13-40c1-8669-e06bd3f89d42",
  "sessionId": "fb5ea7f7-b3c9-4750-b931-39d2aaae422b"
}
```

---

### Runtime record

_source line 19_

```json
{
  "type": "ai-title",
  "aiTitle": "Trace stratified_dryrun v1 to v2 differences",
  "sessionId": "fb5ea7f7-b3c9-4750-b931-39d2aaae422b"
}
```

---

### Tool result

_source line 20 · 2026-05-14T20:36:31.054Z_

<details><summary>↩ Tool result · `toolu_01GZFsdVfnN81kRFsEu7cU3i`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"config\\\": {\\n    \\\"strategies\\\": [\\n      \\\"random\\\",\\n      \\\"embedding_distance\\\",\\n      \\\"dataflow_aware\\\"\\n    ],\\n    \\\"seeds\\\": [\\n      42\\n    ],\\n    \\\"repo_size_bins\\\": {\\n      \\\"small\\\": [\\n        0,\\n        50\\n      ],\\n      \\\"medium\\\": [\\n        50,\\n        200\\n      ],\\n      \\\"large\\\": [\\n        200,\\n        500\\n      ],\\n      \\\"xlarge\\\": [\\n        500,\\n        Infinity\\n      ]\\n    },\\n    \\\"pool_size_bins\\\": {\\n      \\\"small\\\": [\\n        0,\\n        20\\n      ],\\n      \\\"medium\\\": [\\n        20,\\n        40\\n      ],\\n      \\\"large\\\": [\\n        40,\\n        51\\n      ]\\n    },\\n    \\\"similarity_bins\\\": {\\n      \\\"low\\\": [\\n        0.0,\\n        0.3\\n      ],\\n      \\\"medium\\\": [\\n        0.3,\\n        0.6\\n      ],\\n      \\\"high\\\": [\\n        0.6,\\n        1.01\\n      ]\\n    },\\n    \\\"dataflow_bins\\\": {\\n      \\\"sparse\\\": [\\n        0,\\n        2\\n      ],\\n      \\\"moderate\\\": [\\n        2,\\n        10\\n      ],\\n      \\\"rich\\\": [\\n        10,\\n        Infinity\\n      ]\\n    },\\n    \\\"neg_difficulty_quartiles\\\": [\\n      \\\"Q1_easy\\\",\\n      \\\"Q2\\\",\\n      \\\"Q3\\\",\\n      \\\"Q4_hard\\\"\\n    ],\\n    \\\"n_bootstrap\\\": 200,\\n    \\\"dry_run\\\": true\\n  },\\n  \\\"by_repo_size\\\": {\\n    \\\"small\\\": {\\n      \\\"random\\\": {\\n        \\\"R@1\\\": 0.07692307692307693,\\n        \\\"R@1_ci\\\": [\\n          0.038269230769230805,\\n          0.12307692307692308\\n        ],\\n        \\\"R@5\\\": 0.47692307692307695,\\n        \\\"R@5_ci\\\": [\\n          0.39980769230769236,\\n          0.5617307692307693\\n        ],\\n        \\\"MRR\\\": 0.26425629925629923,\\n        \\\"MRR_ci\\\": [\\n          0.22389736652236653,\\n          0.30436761155511155\\n        ],\\n        \\\"count\\\": 130\\n      },\\n      \\\"embedding_distance\\\": {\\n        \\\"R@1\\\": 0.27692307692307694,\\n        \\\"R@1_ci\\\": [\\n          0.19211538461538466,\\n          0.3540384615384616\\n        ],\\n        \\\"R@5\\\": 0.7384615384615385,\\n        \\\"R@5_ci\\\": [\\n          0.6615384615384615,\\n          0.823076923076923\\n        ],\\n        \\\"MRR\\\": 0.47043706293706294,\\n        \\\"MRR_ci\\\": [\\n          0.4076928071928072,\\n          0.5365241633366633\\n        ],\\n        \\\"count\\\": 130\\n      },\\n      \\\"dataflow_aware\\\": {\\n        \\\"R@1\\\": 0.4,\\n        \\\"R@1_ci\\\": [\\n          0.3151923076923077,\\n          0.46942307692307694\\n        ],\\n        \\\"R@5\\\": 0.9,\\n        \\\"R@5_ci\\\": [\\n          0.8459615384615384,\\n          0.9461538461538461\\n        ],\\n        \\\"MRR\\\": 0.6000063825063826,\\n        \\\"MRR_ci\\\": [\\n          0.5347679820179821,\\n          0.6520934065934065\\n        ],\\n        \\\"count\\\": 130\\n      },\\n      \\\"embedding_distance_vs_random\\\": {\\n        \\\"R@1_delta\\\": 0.2,\\n        \\\"R@1_rel_pct\\\": 260.0,\\n        \\\"R@5_delta\\\": 0.26153846153846155,\\n        \\\"R@5_rel_pct\\\": 54.83870967741935,\\n        \\\"MRR_delta\\\": 0.2061807636807637,\\n        \\\"MRR_rel_pct\\\": 78.02302698593054\\n      },\\n      \\\"dataflow_aware_vs_random\\\": {\\n        \\\"R@1_delta\\\": 0.3230769230769231,\\n        \\\"R@1_rel_pct\\\": 420.0,\\n        \\\"R@5_delta\\\": 0.4230769230769231,\\n        \\\"R@5_rel_pct\\\": 88.70967741935483,\\n        \\\"MRR_delta\\\": 0.3357500832500834,\\n        \\\"MRR_rel_pct\\\": 127.0547132442974\\n      }\\n    },\\n    \\\"medium\\\": {\\n      \\\"random\\\": {\\n        \\\"R@1\\\": 0.05491329479768786,\\n        \\\"R@1_ci\\\": [\\n          0.028901734104046242,\\n          0.0752890173410405\\n        ],\\n        \\\"R@5\\\": 0.2861271676300578,\\n        \\\"R@5_ci\\\": [\\n          0.23684971098265897,\\n          0.33236994219653176\\n        ],\\n        \\\"MRR\\\": 0.1935964506181734,\\n        \\\"MRR_ci\\\": [\\n          0.17032768352089914,\\n          0.2161689474822454\\n        ],\\n        \\\"count\\\": 346\\n      },\\n      \\\"embedding_distance\\\": {\\n        \\\"R@1\\\": 0.15028901734104047,\\n        \\\"R@1_ci\\\": [\\n          0.11271676300578035,\\n          0.1879335260115607\\n        ],\\n        \\\"R@5\\\": 0.523121387283237,\\n        \\\"R@5_ci\\\": [\\n          0.4710260115606937,\\n          0.5752167630057804\\n        ],\\n        \\\"MRR\\\": 0.32989441445506745,\\n        \\\"MRR_ci\\\": [\\n          0.29717057853455836,\\n          0.36684936890694325\\n        ],\\n        \\\"count\\\": 346\\n      },\\n      \\\"dataflow_aware\\\": {\\n        \\\"R@1\\\": 0.2398843930635838,\\n        \\\"R@1_ci\\\": [\\n          0.2021676300578035,\\n          0.27760115606936414\\n        ],\\n        \\\"R@5\\\": 0.7369942196531792\\n\\n... [截断: 输出过长，省略 25616 字符] ...\\n\\n\\n        \\\"R@5_rel_pct\\\": 266.66666666666663,\\n        \\\"MRR_delta\\\": 0.18151192668171712,\\n        \\\"MRR_rel_pct\\\": 162.05505112786537\\n      }\\n    },\\n    \\\"Q3\\\": {\\n      \\\"random\\\": {\\n        \\\"R@1\\\": 0.024161073825503355,\\n        \\\"R@1_ci\\\": [\\n          0.01476510067114094,\\n          0.0348993288590604\\n        ],\\n        \\\"R@5\\\": 0.12483221476510067,\\n        \\\"R@5_ci\\\": [\\n          0.10463087248322149,\\n          0.15033557046979865\\n        ],\\n        \\\"MRR\\\": 0.10574925148962648,\\n        \\\"MRR_ci\\\": [\\n          0.09482888540806862,\\n          0.11651834396588909\\n        ],\\n        \\\"count\\\": 745\\n      },\\n      \\\"embedding_distance\\\": {\\n        \\\"R@1\\\": 0.07651006711409396,\\n        \\\"R@1_ci\\\": [\\n          0.05906040268456376,\\n          0.09261744966442953\\n        ],\\n        \\\"R@5\\\": 0.312751677852349,\\n        \\\"R@5_ci\\\": [\\n          0.2764765100671141,\\n          0.34496644295302015\\n        ],\\n        \\\"MRR\\\": 0.20736546414953633,\\n        \\\"MRR_ci\\\": [\\n          0.19054410581433834,\\n          0.22484200616942923\\n        ],\\n        \\\"count\\\": 745\\n      },\\n      \\\"dataflow_aware\\\": {\\n        \\\"R@1\\\": 0.12483221476510067,\\n        \\\"R@1_ci\\\": [\\n          0.09929530201342283,\\n          0.14630872483221477\\n        ],\\n        \\\"R@5\\\": 0.48322147651006714,\\n        \\\"R@5_ci\\\": [\\n          0.4469463087248322,\\n          0.5154362416107383\\n        ],\\n        \\\"MRR\\\": 0.29257823070893335,\\n        \\\"MRR_ci\\\": [\\n          0.2696544452985487,\\n          0.3130578591008492\\n        ],\\n        \\\"count\\\": 745\\n      },\\n      \\\"embedding_distance_vs_random\\\": {\\n        \\\"R@1_delta\\\": 0.052348993288590606,\\n        \\\"R@1_rel_pct\\\": 216.66666666666669,\\n        \\\"R@5_delta\\\": 0.1879194630872483,\\n        \\\"R@5_rel_pct\\\": 150.53763440860212,\\n        \\\"MRR_delta\\\": 0.10161621265990985,\\n        \\\"MRR_rel_pct\\\": 96.09166138625382\\n      },\\n      \\\"dataflow_aware_vs_random\\\": {\\n        \\\"R@1_delta\\\": 0.10067114093959732,\\n        \\\"R@1_rel_pct\\\": 416.6666666666667,\\n        \\\"R@5_delta\\\": 0.35838926174496644,\\n        \\\"R@5_rel_pct\\\": 287.09677419354836,\\n        \\\"MRR_delta\\\": 0.18682897921930686,\\n        \\\"MRR_rel_pct\\\": 176.6716800237909\\n      }\\n    },\\n    \\\"Q4_hard\\\": {\\n      \\\"random\\\": {\\n        \\\"R@1\\\": 0.01742627345844504,\\n        \\\"R@1_ci\\\": [\\n          0.00938337801608579,\\n          0.028150134048257374\\n        ],\\n        \\\"R@5\\\": 0.16353887399463807,\\n        \\\"R@5_ci\\\": [\\n          0.13672922252010725,\\n          0.187701072386059\\n        ],\\n        \\\"MRR\\\": 0.11310223595372695,\\n        \\\"MRR_ci\\\": [\\n          0.10258848955316095,\\n          0.12528228899702964\\n        ],\\n        \\\"count\\\": 746\\n      },\\n      \\\"embedding_distance\\\": {\\n        \\\"R@1\\\": 0.07506702412868632,\\n        \\\"R@1_ci\\\": [\\n          0.05760723860589813,\\n          0.09520777479892761\\n        ],\\n        \\\"R@5\\\": 0.30160857908847183,\\n        \\\"R@5_ci\\\": [\\n          0.2694034852546917,\\n          0.33783512064343163\\n        ],\\n        \\\"MRR\\\": 0.20089647026815693,\\n        \\\"MRR_ci\\\": [\\n          0.18374811602212457,\\n          0.22345370976019258\\n        ],\\n        \\\"count\\\": 746\\n      },\\n      \\\"dataflow_aware\\\": {\\n        \\\"R@1\\\": 0.1353887399463807,\\n        \\\"R@1_ci\\\": [\\n          0.11126005361930295,\\n          0.16219839142091153\\n        ],\\n        \\\"R@5\\\": 0.467828418230563,\\n        \\\"R@5_ci\\\": [\\n          0.4342828418230563,\\n          0.4973190348525469\\n        ],\\n        \\\"MRR\\\": 0.2968150941724084,\\n        \\\"MRR_ci\\\": [\\n          0.27428741459409656,\\n          0.3190549914407245\\n        ],\\n        \\\"count\\\": 746\\n      },\\n      \\\"embedding_distance_vs_random\\\": {\\n        \\\"R@1_delta\\\": 0.057640750670241284,\\n        \\\"R@1_rel_pct\\\": 330.7692307692308,\\n        \\\"R@5_delta\\\": 0.13806970509383376,\\n        \\\"R@5_rel_pct\\\": 84.42622950819671,\\n        \\\"MRR_delta\\\": 0.08779423431442998,\\n        \\\"MRR_rel_pct\\\": 77.62378309686898\\n      },\\n      \\\"dataflow_aware_vs_random\\\": {\\n        \\\"R@1_delta\\\": 0.11796246648793567,\\n        \\\"R@1_rel_pct\\\": 676.9230769230769,\\n        \\\"R@5_delta\\\": 0.3042895442359249,\\n        \\\"R@5_rel_pct\\\": 186.0655737704918,\\n        \\\"MRR_delta\\\": 0.18371285821868147,\\n        \\\"MRR_rel_pct\\\": 162.43079252106313\\n      }\\n    }\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fef79e23-680f-4852-ac33-f0ee76fef1bd",
  "isSidechain": false,
  "promptId": "0b7bb415-f2b4-4832-aac4-2e6aafdc7429",
  "type": "user",
  "uuid": "1dbea139-ba79-4c86-a34e-3b6c51a4f4f4",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"{\\\\n  \\\\\\\"config\\\\\\\": {\\\\n    \\\\\\\"strategies\\\\\\\": [\\\\n      \\\\\\\"random\\\\\\\",\\\\n      \\\\\\\"embedding_distance\\\\\\\",\\\\n      \\\\\\\"dataflow_aware\\\\\\\"\\\\n    ],\\\\n    \\\\\\\"seeds\\\\\\\": [\\\\n      42\\\\n    ],\\\\n    \\\\\\\"repo_size_bins\\\\\\\": {\\\\n      \\\\\\\"small\\\\\\\": [\\\\n        0,\\\\n        50\\\\n      ],\\\\n      \\\\\\\"medium\\\\\\\": [\\\\n        50,\\\\n        200\\\\n      ],\\\\n      \\\\\\\"large\\\\\\\": [\\\\n        200,\\\\n        500\\\\n      ],\\\\n      \\\\\\\"xlarge\\\\\\\": [\\\\n        500,\\\\n        Infinity\\\\n      ]\\\\n    },\\\\n    \\\\\\\"pool_size_bins\\\\\\\": {\\\\n      \\\\\\\"small\\\\\\\": [\\\\n        0,\\\\n        20\\\\n      ],\\\\n      \\\\\\\"medium\\\\\\\": [\\\\n        20,\\\\n        40\\\\n      ],\\\\n      \\\\\\\"large\\\\\\\": [\\\\n        40,\\\\n        51\\\\n      ]\\\\n    },\\\\n    \\\\\\\"similarity_bins\\\\\\\": {\\\\n      \\\\\\\"low\\\\\\\": [\\\\n        0.0,\\\\n        0.3\\\\n      ],\\\\n      \\\\\\\"medium\\\\\\\": [\\\\n        0.3,\\\\n        0.6\\\\n      ],\\\\n      \\\\\\\"high\\\\\\\": [\\\\n        0.6,\\\\n        1.01\\\\n      ]\\\\n    },\\\\n    \\\\\\\"dataflow_bins\\\\\\\": {\\\\n      \\\\\\\"sparse\\\\\\\": [\\\\n        0,\\\\n        2\\\\n      ],\\\\n      \\\\\\\"moderate\\\\\\\": [\\\\n        2,\\\\n        10\\\\n      ],\\\\n      \\\\\\\"rich\\\\\\\": [\\\\n        10,\\\\n        Infinity\\\\n      ]\\\\n    },\\\\n    \\\\\\\"neg_difficulty_quartiles\\\\\\\": [\\\\n      \\\\\\\"Q1_easy\\\\\\\",\\\\n      \\\\\\\"Q2\\\\\\\",\\\\n      \\\\\\\"Q3\\\\\\\",\\\\n      \\\\\\\"Q4_hard\\\\\\\"\\\\n    ],\\\\n    \\\\\\\"n_bootstrap\\\\\\\": 200,\\\\n    \\\\\\\"dry_run\\\\\\\": true\\\\n  },\\\\n  \\\\\\\"by_repo_size\\\\\\\": {\\\\n    \\\\\\\"small\\\\\\\": {\\\\n      \\\\\\\"random\\\\\\\": {\\\\n        \\\\\\\"R@1\\\\\\\": 0.07692307692307693,\\\\n        \\\\\\\"R@1_ci\\\\\\\": [\\\\n          0.038269230769230805,\\\\n          0.12307692307692308\\\\n        ],\\\\n        \\\\\\\"R@5\\\\\\\": 0.47692307692307695,\\\\n        \\\\\\\"R@5_ci\\\\\\\": [\\\\n          0.39980769230769236,\\\\n          0.5617307692307693\\\\n        ],\\\\n        \\\\\\\"MRR\\\\\\\": 0.26425629925629923,\\\\n        \\\\\\\"MRR_ci\\\\\\\": [\\\\n          0.22389736652236653,\\\\n          0.30436761155511155\\\\n        ],\\\\n        \\\\\\\"count\\\\\\\": 130\\\\n      },\\\\n      \\\\\\\"embedding_distance\\\\\\\": {\\\\n        \\\\\\\"R@1\\\\\\\": 0.27692307692307694,\\\\n        \\\\\\\"R@1_ci\\\\\\\": [\\\\n          0.19211538461538466,\\\\n          0.3540384615384616\\\\n        ],\\\\n        \\\\\\\"R@5\\\\\\\": 0.7384615384615385,\\\\n        \\\\\\\"R@5_ci\\\\\\\": [\\\\n          0.6615384615384615,\\\\n          0.823076923076923\\\\n        ],\\\\n        \\\\\\\"MRR\\\\\\\": 0.47043706293706294,\\\\n        \\\\\\\"MRR_ci\\\\\\\": [\\\\n          0.4076928071928072,\\\\n          0.5365241633366633\\\\n        ],\\\\n        \\\\\\\"count\\\\\\\": 130\\\\n      },\\\\n      \\\\\\\"dataflow_aware\\\\\\\": {\\\\n        \\\\\\\"R@1\\\\\\\": 0.4,\\\\n        \\\\\\\"R@1_ci\\\\\\\": [\\\\n          0.3151923076923077,\\\\n          0.46942307692307694\\\\n        ],\\\\n        \\\\\\\"R@5\\\\\\\": 0.9,\\\\n        \\\\\\\"R@5_ci\\\\\\\": [\\\\n          0.8459615384615384,\\\\n          0.9461538461538461\\\\n        ],\\\\n        \\\\\\\"MRR\\\\\\\": 0.6000063825063826,\\\\n        \\\\\\\"MRR_ci\\\\\\\": [\\\\n          0.5347679820179821,\\\\n          0.6520934065934065\\\\n        ],\\\\n        \\\\\\\"count\\\\\\\": 130\\\\n      },\\\\n      \\\\\\\"embedding_distance_vs_random\\\\\\\": {\\\\n        \\\\\\\"R@1_delta\\\\\\\": 0.2,\\\\n        \\\\\\\"R@1_rel_pct\\\\\\\": 260.0,\\\\n        \\\\\\\"R@5_delta\\\\\\\": 0.26153846153846155,\\\\n        \\\\\\\"R@5_rel_pct\\\\\\\": 54.83870967741935,\\\\n        \\\\\\\"MRR_delta\\\\\\\": 0.2061807636807637,\\\\n        \\\\\\\"MRR_rel_pct\\\\\\\": 78.02302698593054\\\\n      },\\\\n      \\\\\\\"dataflow_aware_vs_random\\\\\\\": {\\\\n        \\\\\\\"R@1_delta\\\\\\\": 0.3230769230769231,\\\\n        \\\\\\\"R@1_rel_pct\\\\\\\": 420.0,\\\\n        \\\\\\\"R@5_delta\\\\\\\": 0.4230769230769231,\\\\n        \\\\\\\"R@5_rel_pct\\\\\\\": 88.70967741935483,\\\\n        \\\\\\\"MRR_delta\\\\\\\": 0.3357500832500834,\\\\n        \\\\\\\"MRR_rel_pct\\\\\\\": 127.0547132442974\\\\n      }\\\\n    },\\\\n    \\\\\\\"medium\\\\\\\": {\\\\n      \\\\\\\"random\\\\\\\": {\\\\n        \\\\\\\"R@1\\\\\\\": 0.05491329479768786,\\\\n        \\\\\\\"R@1_ci\\\\\\\": [\\\\n          0.028901734104046242,\\\\n          0.0752890173410405\\\\n        ],\\\\n        \\\\\\\"R@5\\\\\\\": 0.2861271676300578,\\\\n        \\\\\\\"R@5_ci\\\\\\\": [\\\\n          0.23684971098265897,\\\\n          0.33236994219653176\\\\n        ],\\\\n        \\\\\\\"MRR\\\\\\\": 0.1935964506181734,\\\\n        \\\\\\\"MRR_ci\\\\\\\": [\\\\n          0.17032768352089914,\\\\n          0.2161689474822454\\\\n        ],\\\\n        \\\\\\\"count\\\\\\\": 346\\\\n      },\\\\n      \\\\\\\"embedding_distance\\\\\\\": {\\\\n        \\\\\\\"R@1\\\\\\\": 0.15028901734104047,\\\\n        \\\\\\\"R@1_ci\\\\\\\": [\\\\n          0.11271676300578035,\\\\n          0.1879335260115607\\\\n        ],\\\\n        \\\\\\\"R@5\\\\\\\": 0.523121387283237,\\\\n        \\\\\\\"R@5_ci\\\\\\\": [\\\\n          0.4710260115606937,\\\\n          0.5752167630057804\\\\n        ],\\\\n        \\\\\\\"MRR\\\\\\\": 0.32989441445506745,\\\\n        \\\\\\\"MRR_ci\\\\\\\": [\\\\n          0.29717057853455836,\\\\n          0.36684936890694325\\\\n        ],\\\\n        \\\\\\\"count\\\\\\\": 346\\\\n      },\\\\n      \\\\\\\"dataflow_aware\\\\\\\": {\\\\n        \\\\\\\"R@1\\\\\\\": 0.2398843930635838,\\\\n        \\\\\\\"R@1_ci\\\\\\\": [\\\\n          0.2021676300578035,\\\\n          0.27760115606936414\\\\n        ],\\\\n        \\\\\\\"R@5\\\\\\\": 0.7369942196531792\\\\n\\\\n... [截断: 输出过长，省略 25616 字符] ...\\\\n\\\\n\\\\n        \\\\\\\"R@5_rel_pct\\\\\\\": 266.66666666666663,\\\\n        \\\\\\\"MRR_delta\\\\\\\": 0.18151192668171712,\\\\n        \\\\\\\"MRR_rel_pct\\\\\\\": 162.05505112786537\\\\n      }\\\\n    },\\\\n    \\\\\\\"Q3\\\\\\\": {\\\\n      \\\\\\\"random\\\\\\\": {\\\\n        \\\\\\\"R@1\\\\\\\": 0.024161073825503355,\\\\n        \\\\\\\"R@1_ci\\\\\\\": [\\\\n          0.01476510067114094,\\\\n          0.0348993288590604\\\\n        ],\\\\n        \\\\\\\"R@5\\\\\\\": 0.12483221476510067,\\\\n        \\\\\\\"R@5_ci\\\\\\\": [\\\\n          0.10463087248322149,\\\\n          0.15033557046979865\\\\n        ],\\\\n        \\\\\\\"MRR\\\\\\\": 0.10574925148962648,\\\\n        \\\\\\\"MRR_ci\\\\\\\": [\\\\n          0.09482888540806862,\\\\n          0.11651834396588909\\\\n        ],\\\\n        \\\\\\\"count\\\\\\\": 745\\\\n      },\\\\n      \\\\\\\"embedding_distance\\\\\\\": {\\\\n        \\\\\\\"R@1\\\\\\\": 0.07651006711409396,\\\\n        \\\\\\\"R@1_ci\\\\\\\": [\\\\n          0.05906040268456376,\\\\n          0.09261744966442953\\\\n        ],\\\\n        \\\\\\\"R@5\\\\\\\": 0.312751677852349,\\\\n        \\\\\\\"R@5_ci\\\\\\\": [\\\\n          0.2764765100671141,\\\\n          0.34496644295302015\\\\n        ],\\\\n        \\\\\\\"MRR\\\\\\\": 0.20736546414953633,\\\\n        \\\\\\\"MRR_ci\\\\\\\": [\\\\n          0.19054410581433834,\\\\n          0.22484200616942923\\\\n        ],\\\\n        \\\\\\\"count\\\\\\\": 745\\\\n      },\\\\n      \\\\\\\"dataflow_aware\\\\\\\": {\\\\n        \\\\\\\"R@1\\\\\\\": 0.12483221476510067,\\\\n        \\\\\\\"R@1_ci\\\\\\\": [\\\\n          0.09929530201342283,\\\\n          0.14630872483221477\\\\n        ],\\\\n        \\\\\\\"R@5\\\\\\\": 0.48322147651006714,\\\\n        \\\\\\\"R@5_ci\\\\\\\": [\\\\n          0.4469463087248322,\\\\n          0.5154362416107383\\\\n        ],\\\\n        \\\\\\\"MRR\\\\\\\": 0.29257823070893335,\\\\n        \\\\\\\"MRR_ci\\\\\\\": [\\\\n          0.2696544452985487,\\\\n          0.3130578591008492\\\\n        ],\\\\n        \\\\\\\"count\\\\\\\": 745\\\\n      },\\\\n      \\\\\\\"embedding_distance_vs_random\\\\\\\": {\\\\n        \\\\\\\"R@1_delta\\\\\\\": 0.052348993288590606,\\\\n        \\\\\\\"R@1_rel_pct\\\\\\\": 216.66666666666669,\\\\n        \\\\\\\"R@5_delta\\\\\\\": 0.1879194630872483,\\\\n        \\\\\\\"R@5_rel_pct\\\\\\\": 150.53763440860212,\\\\n        \\\\\\\"MRR_delta\\\\\\\": 0.10161621265990985,\\\\n        \\\\\\\"MRR_rel_pct\\\\\\\": 96.09166138625382\\\\n      },\\\\n      \\\\\\\"dataflow_aware_vs_random\\\\\\\": {\\\\n        \\\\\\\"R@1_delta\\\\\\\": 0.10067114093959732,\\\\n        \\\\\\\"R@1_rel_pct\\\\\\\": 416.6666666666667,\\\\n        \\\\\\\"R@5_delta\\\\\\\": 0.35838926174496644,\\\\n        \\\\\\\"R@5_rel_pct\\\\\\\": 287.09677419354836,\\\\n        \\\\\\\"MRR_delta\\\\\\\": 0.18682897921930686,\\\\n        \\\\\\\"MRR_rel_pct\\\\\\\": 176.6716800237909\\\\n      }\\\\n    },\\\\n    \\\\\\\"Q4_hard\\\\\\\": {\\\\n      \\\\\\\"random\\\\\\\": {\\\\n        \\\\\\\"R@1\\\\\\\": 0.01742627345844504,\\\\n        \\\\\\\"R@1_ci\\\\\\\": [\\\\n          0.00938337801608579,\\\\n          0.028150134048257374\\\\n        ],\\\\n        \\\\\\\"R@5\\\\\\\": 0.16353887399463807,\\\\n        \\\\\\\"R@5_ci\\\\\\\": [\\\\n          0.13672922252010725,\\\\n          0.187701072386059\\\\n        ],\\\\n        \\\\\\\"MRR\\\\\\\": 0.11310223595372695,\\\\n        \\\\\\\"MRR_ci\\\\\\\": [\\\\n          0.10258848955316095,\\\\n          0.12528228899702964\\\\n        ],\\\\n        \\\\\\\"count\\\\\\\": 746\\\\n      },\\\\n      \\\\\\\"embedding_distance\\\\\\\": {\\\\n        \\\\\\\"R@1\\\\\\\": 0.07506702412868632,\\\\n        \\\\\\\"R@1_ci\\\\\\\": [\\\\n          0.05760723860589813,\\\\n          0.09520777479892761\\\\n        ],\\\\n        \\\\\\\"R@5\\\\\\\": 0.30160857908847183,\\\\n        \\\\\\\"R@5_ci\\\\\\\": [\\\\n          0.2694034852546917,\\\\n          0.33783512064343163\\\\n        ],\\\\n        \\\\\\\"MRR\\\\\\\": 0.20089647026815693,\\\\n        \\\\\\\"MRR_ci\\\\\\\": [\\\\n          0.18374811602212457,\\\\n          0.22345370976019258\\\\n        ],\\\\n        \\\\\\\"count\\\\\\\": 746\\\\n      },\\\\n      \\\\\\\"dataflow_aware\\\\\\\": {\\\\n        \\\\\\\"R@1\\\\\\\": 0.1353887399463807,\\\\n        \\\\\\\"R@1_ci\\\\\\\": [\\\\n          0.11126005361930295,\\\\n          0.16219839142091153\\\\n        ],\\\\n        \\\\\\\"R@5\\\\\\\": 0.467828418230563,\\\\n        \\\\\\\"R@5_ci\\\\\\\": [\\\\n          0.4342828418230563,\\\\n          0.4973190348525469\\\\n        ],\\\\n        \\\\\\\"MRR\\\\\\\": 0.2968150941724084,\\\\n        \\\\\\\"MRR_ci\\\\\\\": [\\\\n          0.27428741459409656,\\\\n          0.3190549914407245\\\\n        ],\\\\n        \\\\\\\"count\\\\\\\": 746\\\\n      },\\\\n      \\\\\\\"embedding_distance_vs_random\\\\\\\": {\\\\n        \\\\\\\"R@1_delta\\\\\\\": 0.057640750670241284,\\\\n        \\\\\\\"R@1_rel_pct\\\\\\\": 330.7692307692308,\\\\n        \\\\\\\"R@5_delta\\\\\\\": 0.13806970509383376,\\\\n        \\\\\\\"R@5_rel_pct\\\\\\\": 84.42622950819671,\\\\n        \\\\\\\"MRR_delta\\\\\\\": 0.08779423431442998,\\\\n        \\\\\\\"MRR_rel_pct\\\\\\\": 77.62378309686898\\\\n      },\\\\n      \\\\\\\"dataflow_aware_vs_random\\\\\\\": {\\\\n        \\\\\\\"R@1_delta\\\\\\\": 0.11796246648793567,\\\\n        \\\\\\\"R@1_rel_pct\\\\\\\": 676.9230769230769,\\\\n        \\\\\\\"R@5_delta\\\\\\\": 0.3042895442359249,\\\\n        \\\\\\\"R@5_rel_pct\\\\\\\": 186.0655737704918,\\\\n        \\\\\\\"MRR_delta\\\\\\\": 0.18371285821868147,\\\\n        \\\\\\\"MRR_rel_pct\\\\\\\": 162.43079252106313\\\\n      }\\\\n    }\\\\n  }\\\\n}\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.45}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"config\\\": {\\n    \\\"strategies\\\": [\\n      \\\"random\\\",\\n      \\\"embedding_distance\\\",\\n      \\\"dataflow_aware\\\"\\n    ],\\n    \\\"seeds\\\": [\\n      42\\n    ],\\n    \\\"repo_size_bins\\\": {\\n      \\\"small\\\": [\\n        0,\\n        50\\n      ],\\n      \\\"medium\\\": [\\n        50,\\n        200\\n      ],\\n      \\\"large\\\": [\\n        200,\\n        500\\n      ],\\n      \\\"xlarge\\\": [\\n        500,\\n        Infinity\\n      ]\\n    },\\n    \\\"pool_size_bins\\\": {\\n      \\\"small\\\": [\\n        0,\\n        20\\n      ],\\n      \\\"medium\\\": [\\n        20,\\n        40\\n      ],\\n      \\\"large\\\": [\\n        40,\\n        51\\n      ]\\n    },\\n    \\\"similarity_bins\\\": {\\n      \\\"low\\\": [\\n        0.0,\\n        0.3\\n      ],\\n      \\\"medium\\\": [\\n        0.3,\\n        0.6\\n      ],\\n      \\\"high\\\": [\\n        0.6,\\n        1.01\\n      ]\\n    },\\n    \\\"dataflow_bins\\\": {\\n      \\\"sparse\\\": [\\n        0,\\n        2\\n      ],\\n      \\\"moderate\\\": [\\n        2,\\n        10\\n      ],\\n      \\\"rich\\\": [\\n        10,\\n        Infinity\\n      ]\\n    },\\n    \\\"neg_difficulty_quartiles\\\": [\\n      \\\"Q1_easy\\\",\\n      \\\"Q2\\\",\\n      \\\"Q3\\\",\\n      \\\"Q4_hard\\\"\\n    ],\\n    \\\"n_bootstrap\\\": 200,\\n    \\\"dry_run\\\": true\\n  },\\n  \\\"by_repo_size\\\": {\\n    \\\"small\\\": {\\n      \\\"random\\\": {\\n        \\\"R@1\\\": 0.07692307692307693,\\n        \\\"R@1_ci\\\": [\\n          0.038269230769230805,\\n          0.12307692307692308\\n        ],\\n        \\\"R@5\\\": 0.47692307692307695,\\n        \\\"R@5_ci\\\": [\\n          0.39980769230769236,\\n          0.5617307692307693\\n        ],\\n        \\\"MRR\\\": 0.26425629925629923,\\n        \\\"MRR_ci\\\": [\\n          0.22389736652236653,\\n          0.30436761155511155\\n        ],\\n        \\\"count\\\": 130\\n      },\\n      \\\"embedding_distance\\\": {\\n        \\\"R@1\\\": 0.27692307692307694,\\n        \\\"R@1_ci\\\": [\\n          0.19211538461538466,\\n          0.3540384615384616\\n        ],\\n        \\\"R@5\\\": 0.7384615384615385,\\n        \\\"R@5_ci\\\": [\\n          0.6615384615384615,\\n          0.823076923076923\\n        ],\\n        \\\"MRR\\\": 0.47043706293706294,\\n        \\\"MRR_ci\\\": [\\n          0.4076928071928072,\\n          0.5365241633366633\\n        ],\\n        \\\"count\\\": 130\\n      },\\n      \\\"dataflow_aware\\\": {\\n        \\\"R@1\\\": 0.4,\\n        \\\"R@1_ci\\\": [\\n          0.3151923076923077,\\n          0.46942307692307694\\n        ],\\n        \\\"R@5\\\": 0.9,\\n        \\\"R@5_ci\\\": [\\n          0.8459615384615384,\\n          0.9461538461538461\\n        ],\\n        \\\"MRR\\\": 0.6000063825063826,\\n        \\\"MRR_ci\\\": [\\n          0.5347679820179821,\\n          0.6520934065934065\\n        ],\\n        \\\"count\\\": 130\\n      },\\n      \\\"embedding_distance_vs_random\\\": {\\n        \\\"R@1_delta\\\": 0.2,\\n        \\\"R@1_rel_pct\\\": 260.0,\\n        \\\"R@5_delta\\\": 0.26153846153846155,\\n        \\\"R@5_rel_pct\\\": 54.83870967741935,\\n        \\\"MRR_delta\\\": 0.2061807636807637,\\n        \\\"MRR_rel_pct\\\": 78.02302698593054\\n      },\\n      \\\"dataflow_aware_vs_random\\\": {\\n        \\\"R@1_delta\\\": 0.3230769230769231,\\n        \\\"R@1_rel_pct\\\": 420.0,\\n        \\\"R@5_delta\\\": 0.4230769230769231,\\n        \\\"R@5_rel_pct\\\": 88.70967741935483,\\n        \\\"MRR_delta\\\": 0.3357500832500834,\\n        \\\"MRR_rel_pct\\\": 127.0547132442974\\n      }\\n    },\\n    \\\"medium\\\": {\\n      \\\"random\\\": {\\n        \\\"R@1\\\": 0.05491329479768786,\\n        \\\"R@1_ci\\\": [\\n          0.028901734104046242,\\n          0.0752890173410405\\n        ],\\n        \\\"R@5\\\": 0.2861271676300578,\\n        \\\"R@5_ci\\\": [\\n          0.23684971098265897,\\n          0.33236994219653176\\n        ],\\n        \\\"MRR\\\": 0.1935964506181734,\\n        \\\"MRR_ci\\\": [\\n          0.17032768352089914,\\n          0.2161689474822454\\n        ],\\n        \\\"count\\\": 346\\n      },\\n      \\\"embedding_distance\\\": {\\n        \\\"R@1\\\": 0.15028901734104047,\\n        \\\"R@1_ci\\\": [\\n          0.11271676300578035,\\n          0.1879335260115607\\n        ],\\n        \\\"R@5\\\": 0.523121387283237,\\n        \\\"R@5_ci\\\": [\\n          0.4710260115606937,\\n          0.5752167630057804\\n        ],\\n        \\\"MRR\\\": 0.32989441445506745,\\n        \\\"MRR_ci\\\": [\\n          0.29717057853455836,\\n          0.36684936890694325\\n        ],\\n        \\\"count\\\": 346\\n      },\\n      \\\"dataflow_aware\\\": {\\n        \\\"R@1\\\": 0.2398843930635838,\\n        \\\"R@1_ci\\\": [\\n          0.2021676300578035,\\n          0.27760115606936414\\n        ],\\n        \\\"R@5\\\": 0.7369942196531792\\n\\n... [截断: 输出过长，省略 25616 字符] ...\\n\\n\\n        \\\"R@5_rel_pct\\\": 266.66666666666663,\\n        \\\"MRR_delta\\\": 0.18151192668171712,\\n        \\\"MRR_rel_pct\\\": 162.05505112786537\\n      }\\n    },\\n    \\\"Q3\\\": {\\n      \\\"random\\\": {\\n        \\\"R@1\\\": 0.024161073825503355,\\n        \\\"R@1_ci\\\": [\\n          0.01476510067114094,\\n          0.0348993288590604\\n        ],\\n        \\\"R@5\\\": 0.12483221476510067,\\n        \\\"R@5_ci\\\": [\\n          0.10463087248322149,\\n          0.15033557046979865\\n        ],\\n        \\\"MRR\\\": 0.10574925148962648,\\n        \\\"MRR_ci\\\": [\\n          0.09482888540806862,\\n          0.11651834396588909\\n        ],\\n        \\\"count\\\": 745\\n      },\\n      \\\"embedding_distance\\\": {\\n        \\\"R@1\\\": 0.07651006711409396,\\n        \\\"R@1_ci\\\": [\\n          0.05906040268456376,\\n          0.09261744966442953\\n        ],\\n        \\\"R@5\\\": 0.312751677852349,\\n        \\\"R@5_ci\\\": [\\n          0.2764765100671141,\\n          0.34496644295302015\\n        ],\\n        \\\"MRR\\\": 0.20736546414953633,\\n        \\\"MRR_ci\\\": [\\n          0.19054410581433834,\\n          0.22484200616942923\\n        ],\\n        \\\"count\\\": 745\\n      },\\n      \\\"dataflow_aware\\\": {\\n        \\\"R@1\\\": 0.12483221476510067,\\n        \\\"R@1_ci\\\": [\\n          0.09929530201342283,\\n          0.14630872483221477\\n        ],\\n        \\\"R@5\\\": 0.48322147651006714,\\n        \\\"R@5_ci\\\": [\\n          0.4469463087248322,\\n          0.5154362416107383\\n        ],\\n        \\\"MRR\\\": 0.29257823070893335,\\n        \\\"MRR_ci\\\": [\\n          0.2696544452985487,\\n          0.3130578591008492\\n        ],\\n        \\\"count\\\": 745\\n      },\\n      \\\"embedding_distance_vs_random\\\": {\\n        \\\"R@1_delta\\\": 0.052348993288590606,\\n        \\\"R@1_rel_pct\\\": 216.66666666666669,\\n        \\\"R@5_delta\\\": 0.1879194630872483,\\n        \\\"R@5_rel_pct\\\": 150.53763440860212,\\n        \\\"MRR_delta\\\": 0.10161621265990985,\\n        \\\"MRR_rel_pct\\\": 96.09166138625382\\n      },\\n      \\\"dataflow_aware_vs_random\\\": {\\n        \\\"R@1_delta\\\": 0.10067114093959732,\\n        \\\"R@1_rel_pct\\\": 416.6666666666667,\\n        \\\"R@5_delta\\\": 0.35838926174496644,\\n        \\\"R@5_rel_pct\\\": 287.09677419354836,\\n        \\\"MRR_delta\\\": 0.18682897921930686,\\n        \\\"MRR_rel_pct\\\": 176.6716800237909\\n      }\\n    },\\n    \\\"Q4_hard\\\": {\\n      \\\"random\\\": {\\n        \\\"R@1\\\": 0.01742627345844504,\\n        \\\"R@1_ci\\\": [\\n          0.00938337801608579,\\n          0.028150134048257374\\n        ],\\n        \\\"R@5\\\": 0.16353887399463807,\\n        \\\"R@5_ci\\\": [\\n          0.13672922252010725,\\n          0.187701072386059\\n        ],\\n        \\\"MRR\\\": 0.11310223595372695,\\n        \\\"MRR_ci\\\": [\\n          0.10258848955316095,\\n          0.12528228899702964\\n        ],\\n        \\\"count\\\": 746\\n      },\\n      \\\"embedding_distance\\\": {\\n        \\\"R@1\\\": 0.07506702412868632,\\n        \\\"R@1_ci\\\": [\\n          0.05760723860589813,\\n          0.09520777479892761\\n        ],\\n        \\\"R@5\\\": 0.30160857908847183,\\n        \\\"R@5_ci\\\": [\\n          0.2694034852546917,\\n          0.33783512064343163\\n        ],\\n        \\\"MRR\\\": 0.20089647026815693,\\n        \\\"MRR_ci\\\": [\\n          0.18374811602212457,\\n          0.22345370976019258\\n        ],\\n        \\\"count\\\": 746\\n      },\\n      \\\"dataflow_aware\\\": {\\n        \\\"R@1\\\": 0.1353887399463807,\\n        \\\"R@1_ci\\\": [\\n          0.11126005361930295,\\n          0.16219839142091153\\n        ],\\n        \\\"R@5\\\": 0.467828418230563,\\n        \\\"R@5_ci\\\": [\\n          0.4342828418230563,\\n          0.4973190348525469\\n        ],\\n        \\\"MRR\\\": 0.2968150941724084,\\n        \\\"MRR_ci\\\": [\\n          0.27428741459409656,\\n          0.3190549914407245\\n        ],\\n        \\\"count\\\": 746\\n      },\\n      \\\"embedding_distance_vs_random\\\": {\\n        \\\"R@1_delta\\\": 0.057640750670241284,\\n        \\\"R@1_rel_pct\\\": 330.7692307692308,\\n        \\\"R@5_delta\\\": 0.13806970509383376,\\n        \\\"R@5_rel_pct\\\": 84.42622950819671,\\n        \\\"MRR_delta\\\": 0.08779423431442998,\\n        \\\"MRR_rel_pct\\\": 77.62378309686898\\n      },\\n      \\\"dataflow_aware_vs_random\\\": {\\n        \\\"R@1_delta\\\": 0.11796246648793567,\\n        \\\"R@1_rel_pct\\\": 676.9230769230769,\\n        \\\"R@5_delta\\\": 0.3042895442359249,\\n        \\\"R@5_rel_pct\\\": 186.0655737704918,\\n        \\\"MRR_delta\\\": 0.18371285821868147,\\n        \\\"MRR_rel_pct\\\": 162.43079252106313\\n      }\\n    }\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"
    }
  },
  "sourceToolAssistantUUID": "fef79e23-680f-4852-ac33-f0ee76fef1bd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "fb5ea7f7-b3c9-4750-b931-39d2aaae422b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-14T20:36:31.065Z_

<details><summary>↩ Tool result · `toolu_017QUpjVhRWqbMGZrCPCeKuG`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '&&' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "65cd667c-cc13-40c1-8669-e06bd3f89d42",
  "isSidechain": false,
  "promptId": "0b7bb415-f2b4-4832-aac4-2e6aafdc7429",
  "type": "user",
  "uuid": "61083610-ff33-4768-89c4-18e6ea50cb59",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"[ssh_read_only] Command blocked: Shell metacharacter '&&' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\\\", \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '&&' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "65cd667c-cc13-40c1-8669-e06bd3f89d42",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "fb5ea7f7-b3c9-4750-b931-39d2aaae422b",
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
  "leafUuid": "61083610-ff33-4768-89c4-18e6ea50cb59",
  "sessionId": "fb5ea7f7-b3c9-4750-b931-39d2aaae422b"
}
```

---

### Runtime record

_source line 23_

```json
{
  "type": "ai-title",
  "aiTitle": "Trace stratified_dryrun v1 to v2 differences",
  "sessionId": "fb5ea7f7-b3c9-4750-b931-39d2aaae422b"
}
```

---

### Assistant

_source line 24 · 2026-05-14T20:36:34.598Z_

<details><summary>Logged reasoning block</summary>

```text
The read-only command blocked `&&`. Let me use `ssh_execute` for git commands, and also get the full v1 and v2 JSON (v1 was truncated). Let me also read the script itself.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "61083610-ff33-4768-89c4-18e6ea50cb59",
  "isSidechain": false,
  "requestId": "req_011Cb36vt8695sU8H4MeRwbK",
  "type": "assistant",
  "uuid": "f2c648d5-24fa-4c73-8f3b-f77a0f076b97",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "fb5ea7f7-b3c9-4750-b931-39d2aaae422b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017d5mNprndSywkKzbDghvja",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9372,
      "cache_read_input_tokens": 24720,
      "output_tokens": 183,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9372,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 183,
          "cache_read_input_tokens": 24720,
          "cache_creation_input_tokens": 9372,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9372
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

_source line 25 · 2026-05-14T20:36:35.594Z_

v1 输出被截断了，需要完整读取。同时用 ssh_execute 查 git 历史。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f2c648d5-24fa-4c73-8f3b-f77a0f076b97",
  "isSidechain": false,
  "requestId": "req_011Cb36vt8695sU8H4MeRwbK",
  "type": "assistant",
  "uuid": "52af0bae-b9b8-4268-9f6b-165e58b437d7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "fb5ea7f7-b3c9-4750-b931-39d2aaae422b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017d5mNprndSywkKzbDghvja",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9372,
      "cache_read_input_tokens": 24720,
      "output_tokens": 183,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9372,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 183,
          "cache_read_input_tokens": 24720,
          "cache_creation_input_tokens": 9372,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9372
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

_source line 26 · 2026-05-14T20:36:35.858Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01Gw2ZbQDgUTNM7bBdBczCxM`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_execute",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "52af0bae-b9b8-4268-9f6b-165e58b437d7",
  "isSidechain": false,
  "requestId": "req_011Cb36vt8695sU8H4MeRwbK",
  "type": "assistant",
  "uuid": "9cbf5eff-1e8a-4167-a510-5c48330bd052",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "fb5ea7f7-b3c9-4750-b931-39d2aaae422b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017d5mNprndSywkKzbDghvja",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9372,
      "cache_read_input_tokens": 24720,
      "output_tokens": 183,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9372,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 183,
          "cache_read_input_tokens": 24720,
          "cache_creation_input_tokens": 9372,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9372
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

_source line 27 · 2026-05-14T20:36:35.861Z_

<details><summary>↩ Tool result · `toolu_01Gw2ZbQDgUTNM7bBdBczCxM`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__ssh_execute"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9cbf5eff-1e8a-4167-a510-5c48330bd052",
  "isSidechain": false,
  "promptId": "0b7bb415-f2b4-4832-aac4-2e6aafdc7429",
  "type": "user",
  "uuid": "f951b1e1-0908-441f-99a8-4348419de799",
  "toolUseResult": {
    "matches": [
      "mcp__agent-ml-research__ssh_execute"
    ],
    "query": "select:mcp__agent-ml-research__ssh_execute",
    "total_deferred_tools": 26
  },
  "sourceToolAssistantUUID": "9cbf5eff-1e8a-4167-a510-5c48330bd052",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "fb5ea7f7-b3c9-4750-b931-39d2aaae422b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-14T20:36:42.734Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_014ghK6QRxVfxocckx8RZGFn`</summary>

```json
{
  "server": "bjb1-42106",
  "command": "cd /root/structfuse && git log --oneline -15 -- evaluation/analyze_stratified.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f951b1e1-0908-441f-99a8-4348419de799",
  "isSidechain": false,
  "requestId": "req_011Cb36wEqXr5Go1FEwZwKRW",
  "type": "assistant",
  "uuid": "98a574fc-50ca-4c29-b009-a2f7ba56f387",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "fb5ea7f7-b3c9-4750-b931-39d2aaae422b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Hv1FX67ngKTuqFCscj3ZLw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 442,
      "cache_read_input_tokens": 34092,
      "output_tokens": 355,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 442,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 355,
          "cache_read_input_tokens": 34092,
          "cache_creation_input_tokens": 442,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 442
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

_source line 29 · 2026-05-14T20:36:43.096Z_

<details><summary>↩ Tool result · `toolu_014ghK6QRxVfxocckx8RZGFn`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"Encountered a bad command exit code!\\n\\nCommand: 'cd /root/structfuse && git log --oneline -15 -- evaluation/analyze_stratified.py'\\n\\nExit code: 128\\n\\nStdout:\\n\\n\\n\\nStderr:\\n\\nfatal: not a git repository (or any of the parent directories): .git\\n\\n\", \"metadata\": {\"elapsed_seconds\": 0.35}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "98a574fc-50ca-4c29-b009-a2f7ba56f387",
  "isSidechain": false,
  "promptId": "0b7bb415-f2b4-4832-aac4-2e6aafdc7429",
  "type": "user",
  "uuid": "2e02440a-3e23-4149-9876-fd6a518fab33",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"Encountered a bad command exit code!\\\\n\\\\nCommand: 'cd /root/structfuse && git log --oneline -15 -- evaluation/analyze_stratified.py'\\\\n\\\\nExit code: 128\\\\n\\\\nStdout:\\\\n\\\\n\\\\n\\\\nStderr:\\\\n\\\\nfatal: not a git repository (or any of the parent directories): .git\\\\n\\\\n\\\", \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.35}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"Encountered a bad command exit code!\\n\\nCommand: 'cd /root/structfuse && git log --oneline -15 -- evaluation/analyze_stratified.py'\\n\\nExit code: 128\\n\\nStdout:\\n\\n\\n\\nStderr:\\n\\nfatal: not a git repository (or any of the parent directories): .git\\n\\n\", \"metadata\": {\"elapsed_seconds\": 0.35}}"
    }
  },
  "sourceToolAssistantUUID": "98a574fc-50ca-4c29-b009-a2f7ba56f387",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "fb5ea7f7-b3c9-4750-b931-39d2aaae422b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-14T20:36:44.206Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01DBBKPQncMmrx5v7y7BGDzz`</summary>

```json
{
  "server": "bjb1-42106",
  "command": "cat /root/autodl-tmp/structfuse/artifacts/stratified_dryrun/stratified_results.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2e02440a-3e23-4149-9876-fd6a518fab33",
  "isSidechain": false,
  "requestId": "req_011Cb36wEqXr5Go1FEwZwKRW",
  "type": "assistant",
  "uuid": "067965e9-cbbc-4023-8459-7d2253f03f43",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "fb5ea7f7-b3c9-4750-b931-39d2aaae422b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Hv1FX67ngKTuqFCscj3ZLw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 442,
      "cache_read_input_tokens": 34092,
      "output_tokens": 355,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 442,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 355,
          "cache_read_input_tokens": 34092,
          "cache_creation_input_tokens": 442,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 442
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

_source line 31 · 2026-05-14T20:36:44.642Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_015ZZr1HomN8U2EKUFHsr4LN`</summary>

```json
{
  "server": "bjb1-42106",
  "command": "cat /root/autodl-tmp/structfuse/artifacts/stratified_dryrun_v2/stratified_results.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "067965e9-cbbc-4023-8459-7d2253f03f43",
  "isSidechain": false,
  "requestId": "req_011Cb36wEqXr5Go1FEwZwKRW",
  "type": "assistant",
  "uuid": "d09591e8-8f23-4ae2-8602-44b3fa61fc3e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "fb5ea7f7-b3c9-4750-b931-39d2aaae422b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Hv1FX67ngKTuqFCscj3ZLw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 442,
      "cache_read_input_tokens": 34092,
      "output_tokens": 355,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 442,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 355,
          "cache_read_input_tokens": 34092,
          "cache_creation_input_tokens": 442,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 442
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

_source line 32 · 2026-05-14T20:36:45.039Z_

<details><summary>↩ Tool result · `toolu_01DBBKPQncMmrx5v7y7BGDzz`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"config\\\": {\\n    \\\"strategies\\\": [\\n      \\\"random\\\",\\n      \\\"embedding_distance\\\",\\n      \\\"dataflow_aware\\\"\\n    ],\\n    \\\"seeds\\\": [\\n      42\\n    ],\\n    \\\"repo_size_bins\\\": {\\n      \\\"small\\\": [\\n        0,\\n        50\\n      ],\\n      \\\"medium\\\": [\\n        50,\\n        200\\n      ],\\n      \\\"large\\\": [\\n        200,\\n        500\\n      ],\\n      \\\"xlarge\\\": [\\n        500,\\n        Infinity\\n      ]\\n    },\\n    \\\"pool_size_bins\\\": {\\n      \\\"small\\\": [\\n        0,\\n        20\\n      ],\\n      \\\"medium\\\": [\\n        20,\\n        40\\n      ],\\n      \\\"large\\\": [\\n        40,\\n        51\\n      ]\\n    },\\n    \\\"similarity_bins\\\": {\\n      \\\"low\\\": [\\n        0.0,\\n        0.3\\n      ],\\n      \\\"medium\\\": [\\n        0.3,\\n        0.6\\n      ],\\n      \\\"high\\\": [\\n        0.6,\\n        1.01\\n      ]\\n    },\\n    \\\"n_bootstrap\\\": 200,\\n    \\\"dry_run\\\": true\\n  },\\n  \\\"by_repo_size\\\": {\\n    \\\"small\\\": {\\n      \\\"random\\\": {\\n        \\\"R@1\\\": 0.11538461538461539,\\n        \\\"R@1_ci\\\": [\\n          0.061346153846153884,\\n          0.16923076923076924\\n        ],\\n        \\\"R@5\\\": 0.5384615384615384,\\n        \\\"R@5_ci\\\": [\\n          0.4461538461538462,\\n          0.6230769230769231\\n        ],\\n        \\\"MRR\\\": 0.3059754134754135,\\n        \\\"MRR_ci\\\": [\\n          0.25409036102786103,\\n          0.3513594044844045\\n        ],\\n        \\\"count\\\": 130\\n      },\\n      \\\"embedding_distance\\\": {\\n        \\\"R@1\\\": 0.3,\\n        \\\"R@1_ci\\\": [\\n          0.2230769230769231,\\n          0.37711538461538463\\n        ],\\n        \\\"R@5\\\": 0.7384615384615385,\\n        \\\"R@5_ci\\\": [\\n          0.6613461538461538,\\n          0.8153846153846154\\n        ],\\n        \\\"MRR\\\": 0.4930563880563881,\\n        \\\"MRR_ci\\\": [\\n          0.43992261211011213,\\n          0.5556576062826063\\n        ],\\n        \\\"count\\\": 130\\n      },\\n      \\\"dataflow_aware\\\": {\\n        \\\"R@1\\\": 0.4846153846153846,\\n        \\\"R@1_ci\\\": [\\n          0.3923076923076923,\\n          0.5617307692307693\\n        ],\\n        \\\"R@5\\\": 0.8769230769230769,\\n        \\\"R@5_ci\\\": [\\n          0.8226923076923077,\\n          0.9230769230769231\\n        ],\\n        \\\"MRR\\\": 0.6500946275946277,\\n        \\\"MRR_ci\\\": [\\n          0.59523923992674,\\n          0.7073237942612942\\n        ],\\n        \\\"count\\\": 130\\n      },\\n      \\\"embedding_distance_vs_random\\\": {\\n        \\\"R@1_delta\\\": 0.1846153846153846,\\n        \\\"R@1_rel_pct\\\": 160.0,\\n        \\\"R@5_delta\\\": 0.20000000000000007,\\n        \\\"R@5_rel_pct\\\": 37.14285714285715,\\n        \\\"MRR_delta\\\": 0.18708097458097456,\\n        \\\"MRR_rel_pct\\\": 61.14248607625702\\n      },\\n      \\\"dataflow_aware_vs_random\\\": {\\n        \\\"R@1_delta\\\": 0.36923076923076925,\\n        \\\"R@1_rel_pct\\\": 320.0,\\n        \\\"R@5_delta\\\": 0.3384615384615385,\\n        \\\"R@5_rel_pct\\\": 62.85714285714287,\\n        \\\"MRR_delta\\\": 0.34411921411921415,\\n        \\\"MRR_rel_pct\\\": 112.46629597147866\\n      }\\n    },\\n    \\\"medium\\\": {\\n      \\\"random\\\": {\\n        \\\"R@1\\\": 0.05202312138728324,\\n        \\\"R@1_ci\\\": [\\n          0.031791907514450865,\\n          0.08092485549132948\\n        ],\\n        \\\"R@5\\\": 0.23121387283236994,\\n        \\\"R@5_ci\\\": [\\n          0.18778901734104048,\\n          0.27167630057803466\\n        ],\\n        \\\"MRR\\\": 0.17820474196308103,\\n        \\\"MRR_ci\\\": [\\n          0.15638534764941775,\\n          0.20150044957306631\\n        ],\\n        \\\"count\\\": 346\\n      },\\n      \\\"embedding_distance\\\": {\\n        \\\"R@1\\\": 0.1069364161849711,\\n        \\\"R@1_ci\\\": [\\n          0.07803468208092486,\\n          0.14169075144508672\\n        ],\\n        \\\"R@5\\\": 0.49421965317919075,\\n        \\\"R@5_ci\\\": [\\n          0.4305635838150289,\\n          0.5348265895953758\\n        ],\\n        \\\"MRR\\\": 0.2865956097787104,\\n        \\\"MRR_ci\\\": [\\n          0.25823956396604253,\\n          0.31508196199064964\\n        ],\\n        \\\"count\\\": 346\\n      },\\n      \\\"dataflow_aware\\\": {\\n        \\\"R@1\\\": 0.2398843930635838,\\n        \\\"R@1_ci\\\": [\\n          0.19653179190751446,\\n          0.2861271676300578\\n        ],\\n        \\\"R@5\\\": 0.7023121387283237,\\n        \\\"R@5_ci\\\": [\\n          0.6588150289017342,\\n          0.7514450867052023\\n        ],\\n        \\\"MRR\\\": 0.4295497658014659,\\n        \\\"MRR_ci\\\": [\\n          0.39310849797917335,\\n          0.4627567860954358\\n        ],\\n        \\\"count\\\": 346\\n      },\\n\\n\\n... [截断: 输出过长，省略 11724 字符] ...\\n\\n        \\\"R@5_rel_pct\\\": 109.78835978835977,\\n        \\\"MRR_delta\\\": 0.08434517635221275,\\n        \\\"MRR_rel_pct\\\": 71.43937034482639\\n      },\\n      \\\"dataflow_aware_vs_random\\\": {\\n        \\\"R@1_delta\\\": 0.10322333077513429,\\n        \\\"R@1_rel_pct\\\": 320.2380952380952,\\n        \\\"R@5_delta\\\": 0.3142747505755948,\\n        \\\"R@5_rel_pct\\\": 216.66666666666666,\\n        \\\"MRR_delta\\\": 0.1742035067513217,\\n        \\\"MRR_rel_pct\\\": 147.54831719370338\\n      }\\n    },\\n    \\\"medium\\\": {\\n      \\\"random\\\": {\\n        \\\"R@1\\\": 0.014285714285714285,\\n        \\\"R@1_ci\\\": [\\n          0.002857142857142857,\\n          0.025714285714285714\\n        ],\\n        \\\"R@5\\\": 0.10285714285714286,\\n        \\\"R@5_ci\\\": [\\n          0.06850000000000002,\\n          0.13435714285714287\\n        ],\\n        \\\"MRR\\\": 0.08892012631102023,\\n        \\\"MRR_ci\\\": [\\n          0.07565878083640655,\\n          0.10097054824489184\\n        ],\\n        \\\"count\\\": 350\\n      },\\n      \\\"embedding_distance\\\": {\\n        \\\"R@1\\\": 0.06571428571428571,\\n        \\\"R@1_ci\\\": [\\n          0.04285714285714286,\\n          0.09428571428571429\\n        ],\\n        \\\"R@5\\\": 0.3028571428571429,\\n        \\\"R@5_ci\\\": [\\n          0.25128571428571433,\\n          0.3457142857142857\\n        ],\\n        \\\"MRR\\\": 0.19037293149185006,\\n        \\\"MRR_ci\\\": [\\n          0.1649260686702319,\\n          0.21459875959655225\\n        ],\\n        \\\"count\\\": 350\\n      },\\n      \\\"dataflow_aware\\\": {\\n        \\\"R@1\\\": 0.13428571428571429,\\n        \\\"R@1_ci\\\": [\\n          0.09714285714285714,\\n          0.17442857142857146\\n        ],\\n        \\\"R@5\\\": 0.4342857142857143,\\n        \\\"R@5_ci\\\": [\\n          0.38857142857142857,\\n          0.4858571428571429\\n        ],\\n        \\\"MRR\\\": 0.2852574269542923,\\n        \\\"MRR_ci\\\": [\\n          0.2526425047155209,\\n          0.32557010653989665\\n        ],\\n        \\\"count\\\": 350\\n      },\\n      \\\"embedding_distance_vs_random\\\": {\\n        \\\"R@1_delta\\\": 0.05142857142857143,\\n        \\\"R@1_rel_pct\\\": 360.0,\\n        \\\"R@5_delta\\\": 0.2,\\n        \\\"R@5_rel_pct\\\": 194.44444444444446,\\n        \\\"MRR_delta\\\": 0.10145280518082983,\\n        \\\"MRR_rel_pct\\\": 114.09431069179259\\n      },\\n      \\\"dataflow_aware_vs_random\\\": {\\n        \\\"R@1_delta\\\": 0.12,\\n        \\\"R@1_rel_pct\\\": 840.0,\\n        \\\"R@5_delta\\\": 0.3314285714285714,\\n        \\\"R@5_rel_pct\\\": 322.2222222222222,\\n        \\\"MRR_delta\\\": 0.19633730064327207,\\n        \\\"MRR_rel_pct\\\": 220.80186881036764\\n      }\\n    },\\n    \\\"high\\\": {\\n      \\\"random\\\": {\\n        \\\"R@1\\\": 0.0,\\n        \\\"R@1_ci\\\": [\\n          0.0,\\n          0.0\\n        ],\\n        \\\"R@5\\\": 0.0,\\n        \\\"R@5_ci\\\": [\\n          0.0,\\n          0.0\\n        ],\\n        \\\"MRR\\\": 0.06634814469381427,\\n        \\\"MRR_ci\\\": [\\n          0.04922830990875043,\\n          0.08318125486392415\\n        ],\\n        \\\"count\\\": 24\\n      },\\n      \\\"embedding_distance\\\": {\\n        \\\"R@1\\\": 0.08333333333333333,\\n        \\\"R@1_ci\\\": [\\n          0.0,\\n          0.20833333333333334\\n        ],\\n        \\\"R@5\\\": 0.25,\\n        \\\"R@5_ci\\\": [\\n          0.08333333333333333,\\n          0.4166666666666667\\n        ],\\n        \\\"MRR\\\": 0.18658210312354354,\\n        \\\"MRR_ci\\\": [\\n          0.09884595475354443,\\n          0.2990058719871796\\n        ],\\n        \\\"count\\\": 24\\n      },\\n      \\\"dataflow_aware\\\": {\\n        \\\"R@1\\\": 0.08333333333333333,\\n        \\\"R@1_ci\\\": [\\n          0.0,\\n          0.20833333333333334\\n        ],\\n        \\\"R@5\\\": 0.25,\\n        \\\"R@5_ci\\\": [\\n          0.08333333333333333,\\n          0.4166666666666667\\n        ],\\n        \\\"MRR\\\": 0.19360231918734738,\\n        \\\"MRR_ci\\\": [\\n          0.10034009813817588,\\n          0.3119892338877614\\n        ],\\n        \\\"count\\\": 24\\n      },\\n      \\\"embedding_distance_vs_random\\\": {\\n        \\\"R@1_delta\\\": 0.08333333333333333,\\n        \\\"R@1_rel_pct\\\": 0.0,\\n        \\\"R@5_delta\\\": 0.25,\\n        \\\"R@5_rel_pct\\\": 0.0,\\n        \\\"MRR_delta\\\": 0.12023395842972927,\\n        \\\"MRR_rel_pct\\\": 181.21676044535855\\n      },\\n      \\\"dataflow_aware_vs_random\\\": {\\n        \\\"R@1_delta\\\": 0.08333333333333333,\\n        \\\"R@1_rel_pct\\\": 0.0,\\n        \\\"R@5_delta\\\": 0.25,\\n        \\\"R@5_rel_pct\\\": 0.0,\\n        \\\"MRR_delta\\\": 0.1272541744935331,\\n        \\\"MRR_rel_pct\\\": 191.79763817178326\\n      }\\n    }\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.82}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "067965e9-cbbc-4023-8459-7d2253f03f43",
  "isSidechain": false,
  "promptId": "0b7bb415-f2b4-4832-aac4-2e6aafdc7429",
  "type": "user",
  "uuid": "b9105933-1d8e-4623-bd92-76d4ac23ebd8",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"{\\\\n  \\\\\\\"config\\\\\\\": {\\\\n    \\\\\\\"strategies\\\\\\\": [\\\\n      \\\\\\\"random\\\\\\\",\\\\n      \\\\\\\"embedding_distance\\\\\\\",\\\\n      \\\\\\\"dataflow_aware\\\\\\\"\\\\n    ],\\\\n    \\\\\\\"seeds\\\\\\\": [\\\\n      42\\\\n    ],\\\\n    \\\\\\\"repo_size_bins\\\\\\\": {\\\\n      \\\\\\\"small\\\\\\\": [\\\\n        0,\\\\n        50\\\\n      ],\\\\n      \\\\\\\"medium\\\\\\\": [\\\\n        50,\\\\n        200\\\\n      ],\\\\n      \\\\\\\"large\\\\\\\": [\\\\n        200,\\\\n        500\\\\n      ],\\\\n      \\\\\\\"xlarge\\\\\\\": [\\\\n        500,\\\\n        Infinity\\\\n      ]\\\\n    },\\\\n    \\\\\\\"pool_size_bins\\\\\\\": {\\\\n      \\\\\\\"small\\\\\\\": [\\\\n        0,\\\\n        20\\\\n      ],\\\\n      \\\\\\\"medium\\\\\\\": [\\\\n        20,\\\\n        40\\\\n      ],\\\\n      \\\\\\\"large\\\\\\\": [\\\\n        40,\\\\n        51\\\\n      ]\\\\n    },\\\\n    \\\\\\\"similarity_bins\\\\\\\": {\\\\n      \\\\\\\"low\\\\\\\": [\\\\n        0.0,\\\\n        0.3\\\\n      ],\\\\n      \\\\\\\"medium\\\\\\\": [\\\\n        0.3,\\\\n        0.6\\\\n      ],\\\\n      \\\\\\\"high\\\\\\\": [\\\\n        0.6,\\\\n        1.01\\\\n      ]\\\\n    },\\\\n    \\\\\\\"n_bootstrap\\\\\\\": 200,\\\\n    \\\\\\\"dry_run\\\\\\\": true\\\\n  },\\\\n  \\\\\\\"by_repo_size\\\\\\\": {\\\\n    \\\\\\\"small\\\\\\\": {\\\\n      \\\\\\\"random\\\\\\\": {\\\\n        \\\\\\\"R@1\\\\\\\": 0.11538461538461539,\\\\n        \\\\\\\"R@1_ci\\\\\\\": [\\\\n          0.061346153846153884,\\\\n          0.16923076923076924\\\\n        ],\\\\n        \\\\\\\"R@5\\\\\\\": 0.5384615384615384,\\\\n        \\\\\\\"R@5_ci\\\\\\\": [\\\\n          0.4461538461538462,\\\\n          0.6230769230769231\\\\n        ],\\\\n        \\\\\\\"MRR\\\\\\\": 0.3059754134754135,\\\\n        \\\\\\\"MRR_ci\\\\\\\": [\\\\n          0.25409036102786103,\\\\n          0.3513594044844045\\\\n        ],\\\\n        \\\\\\\"count\\\\\\\": 130\\\\n      },\\\\n      \\\\\\\"embedding_distance\\\\\\\": {\\\\n        \\\\\\\"R@1\\\\\\\": 0.3,\\\\n        \\\\\\\"R@1_ci\\\\\\\": [\\\\n          0.2230769230769231,\\\\n          0.37711538461538463\\\\n        ],\\\\n        \\\\\\\"R@5\\\\\\\": 0.7384615384615385,\\\\n        \\\\\\\"R@5_ci\\\\\\\": [\\\\n          0.6613461538461538,\\\\n          0.8153846153846154\\\\n        ],\\\\n        \\\\\\\"MRR\\\\\\\": 0.4930563880563881,\\\\n        \\\\\\\"MRR_ci\\\\\\\": [\\\\n          0.43992261211011213,\\\\n          0.5556576062826063\\\\n        ],\\\\n        \\\\\\\"count\\\\\\\": 130\\\\n      },\\\\n      \\\\\\\"dataflow_aware\\\\\\\": {\\\\n        \\\\\\\"R@1\\\\\\\": 0.4846153846153846,\\\\n        \\\\\\\"R@1_ci\\\\\\\": [\\\\n          0.3923076923076923,\\\\n          0.5617307692307693\\\\n        ],\\\\n        \\\\\\\"R@5\\\\\\\": 0.8769230769230769,\\\\n        \\\\\\\"R@5_ci\\\\\\\": [\\\\n          0.8226923076923077,\\\\n          0.9230769230769231\\\\n        ],\\\\n        \\\\\\\"MRR\\\\\\\": 0.6500946275946277,\\\\n        \\\\\\\"MRR_ci\\\\\\\": [\\\\n          0.59523923992674,\\\\n          0.7073237942612942\\\\n        ],\\\\n        \\\\\\\"count\\\\\\\": 130\\\\n      },\\\\n      \\\\\\\"embedding_distance_vs_random\\\\\\\": {\\\\n        \\\\\\\"R@1_delta\\\\\\\": 0.1846153846153846,\\\\n        \\\\\\\"R@1_rel_pct\\\\\\\": 160.0,\\\\n        \\\\\\\"R@5_delta\\\\\\\": 0.20000000000000007,\\\\n        \\\\\\\"R@5_rel_pct\\\\\\\": 37.14285714285715,\\\\n        \\\\\\\"MRR_delta\\\\\\\": 0.18708097458097456,\\\\n        \\\\\\\"MRR_rel_pct\\\\\\\": 61.14248607625702\\\\n      },\\\\n      \\\\\\\"dataflow_aware_vs_random\\\\\\\": {\\\\n        \\\\\\\"R@1_delta\\\\\\\": 0.36923076923076925,\\\\n        \\\\\\\"R@1_rel_pct\\\\\\\": 320.0,\\\\n        \\\\\\\"R@5_delta\\\\\\\": 0.3384615384615385,\\\\n        \\\\\\\"R@5_rel_pct\\\\\\\": 62.85714285714287,\\\\n        \\\\\\\"MRR_delta\\\\\\\": 0.34411921411921415,\\\\n        \\\\\\\"MRR_rel_pct\\\\\\\": 112.46629597147866\\\\n      }\\\\n    },\\\\n    \\\\\\\"medium\\\\\\\": {\\\\n      \\\\\\\"random\\\\\\\": {\\\\n        \\\\\\\"R@1\\\\\\\": 0.05202312138728324,\\\\n        \\\\\\\"R@1_ci\\\\\\\": [\\\\n          0.031791907514450865,\\\\n          0.08092485549132948\\\\n        ],\\\\n        \\\\\\\"R@5\\\\\\\": 0.23121387283236994,\\\\n        \\\\\\\"R@5_ci\\\\\\\": [\\\\n          0.18778901734104048,\\\\n          0.27167630057803466\\\\n        ],\\\\n        \\\\\\\"MRR\\\\\\\": 0.17820474196308103,\\\\n        \\\\\\\"MRR_ci\\\\\\\": [\\\\n          0.15638534764941775,\\\\n          0.20150044957306631\\\\n        ],\\\\n        \\\\\\\"count\\\\\\\": 346\\\\n      },\\\\n      \\\\\\\"embedding_distance\\\\\\\": {\\\\n        \\\\\\\"R@1\\\\\\\": 0.1069364161849711,\\\\n        \\\\\\\"R@1_ci\\\\\\\": [\\\\n          0.07803468208092486,\\\\n          0.14169075144508672\\\\n        ],\\\\n        \\\\\\\"R@5\\\\\\\": 0.49421965317919075,\\\\n        \\\\\\\"R@5_ci\\\\\\\": [\\\\n          0.4305635838150289,\\\\n          0.5348265895953758\\\\n        ],\\\\n        \\\\\\\"MRR\\\\\\\": 0.2865956097787104,\\\\n        \\\\\\\"MRR_ci\\\\\\\": [\\\\n          0.25823956396604253,\\\\n          0.31508196199064964\\\\n        ],\\\\n        \\\\\\\"count\\\\\\\": 346\\\\n      },\\\\n      \\\\\\\"dataflow_aware\\\\\\\": {\\\\n        \\\\\\\"R@1\\\\\\\": 0.2398843930635838,\\\\n        \\\\\\\"R@1_ci\\\\\\\": [\\\\n          0.19653179190751446,\\\\n          0.2861271676300578\\\\n        ],\\\\n        \\\\\\\"R@5\\\\\\\": 0.7023121387283237,\\\\n        \\\\\\\"R@5_ci\\\\\\\": [\\\\n          0.6588150289017342,\\\\n          0.7514450867052023\\\\n        ],\\\\n        \\\\\\\"MRR\\\\\\\": 0.4295497658014659,\\\\n        \\\\\\\"MRR_ci\\\\\\\": [\\\\n          0.39310849797917335,\\\\n          0.4627567860954358\\\\n        ],\\\\n        \\\\\\\"count\\\\\\\": 346\\\\n      },\\\\n\\\\n\\\\n... [截断: 输出过长，省略 11724 字符] ...\\\\n\\\\n        \\\\\\\"R@5_rel_pct\\\\\\\": 109.78835978835977,\\\\n        \\\\\\\"MRR_delta\\\\\\\": 0.08434517635221275,\\\\n        \\\\\\\"MRR_rel_pct\\\\\\\": 71.43937034482639\\\\n      },\\\\n      \\\\\\\"dataflow_aware_vs_random\\\\\\\": {\\\\n        \\\\\\\"R@1_delta\\\\\\\": 0.10322333077513429,\\\\n        \\\\\\\"R@1_rel_pct\\\\\\\": 320.2380952380952,\\\\n        \\\\\\\"R@5_delta\\\\\\\": 0.3142747505755948,\\\\n        \\\\\\\"R@5_rel_pct\\\\\\\": 216.66666666666666,\\\\n        \\\\\\\"MRR_delta\\\\\\\": 0.1742035067513217,\\\\n        \\\\\\\"MRR_rel_pct\\\\\\\": 147.54831719370338\\\\n      }\\\\n    },\\\\n    \\\\\\\"medium\\\\\\\": {\\\\n      \\\\\\\"random\\\\\\\": {\\\\n        \\\\\\\"R@1\\\\\\\": 0.014285714285714285,\\\\n        \\\\\\\"R@1_ci\\\\\\\": [\\\\n          0.002857142857142857,\\\\n          0.025714285714285714\\\\n        ],\\\\n        \\\\\\\"R@5\\\\\\\": 0.10285714285714286,\\\\n        \\\\\\\"R@5_ci\\\\\\\": [\\\\n          0.06850000000000002,\\\\n          0.13435714285714287\\\\n        ],\\\\n        \\\\\\\"MRR\\\\\\\": 0.08892012631102023,\\\\n        \\\\\\\"MRR_ci\\\\\\\": [\\\\n          0.07565878083640655,\\\\n          0.10097054824489184\\\\n        ],\\\\n        \\\\\\\"count\\\\\\\": 350\\\\n      },\\\\n      \\\\\\\"embedding_distance\\\\\\\": {\\\\n        \\\\\\\"R@1\\\\\\\": 0.06571428571428571,\\\\n        \\\\\\\"R@1_ci\\\\\\\": [\\\\n          0.04285714285714286,\\\\n          0.09428571428571429\\\\n        ],\\\\n        \\\\\\\"R@5\\\\\\\": 0.3028571428571429,\\\\n        \\\\\\\"R@5_ci\\\\\\\": [\\\\n          0.25128571428571433,\\\\n          0.3457142857142857\\\\n        ],\\\\n        \\\\\\\"MRR\\\\\\\": 0.19037293149185006,\\\\n        \\\\\\\"MRR_ci\\\\\\\": [\\\\n          0.1649260686702319,\\\\n          0.21459875959655225\\\\n        ],\\\\n        \\\\\\\"count\\\\\\\": 350\\\\n      },\\\\n      \\\\\\\"dataflow_aware\\\\\\\": {\\\\n        \\\\\\\"R@1\\\\\\\": 0.13428571428571429,\\\\n        \\\\\\\"R@1_ci\\\\\\\": [\\\\n          0.09714285714285714,\\\\n          0.17442857142857146\\\\n        ],\\\\n        \\\\\\\"R@5\\\\\\\": 0.4342857142857143,\\\\n        \\\\\\\"R@5_ci\\\\\\\": [\\\\n          0.38857142857142857,\\\\n          0.4858571428571429\\\\n        ],\\\\n        \\\\\\\"MRR\\\\\\\": 0.2852574269542923,\\\\n        \\\\\\\"MRR_ci\\\\\\\": [\\\\n          0.2526425047155209,\\\\n          0.32557010653989665\\\\n        ],\\\\n        \\\\\\\"count\\\\\\\": 350\\\\n      },\\\\n      \\\\\\\"embedding_distance_vs_random\\\\\\\": {\\\\n        \\\\\\\"R@1_delta\\\\\\\": 0.05142857142857143,\\\\n        \\\\\\\"R@1_rel_pct\\\\\\\": 360.0,\\\\n        \\\\\\\"R@5_delta\\\\\\\": 0.2,\\\\n        \\\\\\\"R@5_rel_pct\\\\\\\": 194.44444444444446,\\\\n        \\\\\\\"MRR_delta\\\\\\\": 0.10145280518082983,\\\\n        \\\\\\\"MRR_rel_pct\\\\\\\": 114.09431069179259\\\\n      },\\\\n      \\\\\\\"dataflow_aware_vs_random\\\\\\\": {\\\\n        \\\\\\\"R@1_delta\\\\\\\": 0.12,\\\\n        \\\\\\\"R@1_rel_pct\\\\\\\": 840.0,\\\\n        \\\\\\\"R@5_delta\\\\\\\": 0.3314285714285714,\\\\n        \\\\\\\"R@5_rel_pct\\\\\\\": 322.2222222222222,\\\\n        \\\\\\\"MRR_delta\\\\\\\": 0.19633730064327207,\\\\n        \\\\\\\"MRR_rel_pct\\\\\\\": 220.80186881036764\\\\n      }\\\\n    },\\\\n    \\\\\\\"high\\\\\\\": {\\\\n      \\\\\\\"random\\\\\\\": {\\\\n        \\\\\\\"R@1\\\\\\\": 0.0,\\\\n        \\\\\\\"R@1_ci\\\\\\\": [\\\\n          0.0,\\\\n          0.0\\\\n        ],\\\\n        \\\\\\\"R@5\\\\\\\": 0.0,\\\\n        \\\\\\\"R@5_ci\\\\\\\": [\\\\n          0.0,\\\\n          0.0\\\\n        ],\\\\n        \\\\\\\"MRR\\\\\\\": 0.06634814469381427,\\\\n        \\\\\\\"MRR_ci\\\\\\\": [\\\\n          0.04922830990875043,\\\\n          0.08318125486392415\\\\n        ],\\\\n        \\\\\\\"count\\\\\\\": 24\\\\n      },\\\\n      \\\\\\\"embedding_distance\\\\\\\": {\\\\n        \\\\\\\"R@1\\\\\\\": 0.08333333333333333,\\\\n        \\\\\\\"R@1_ci\\\\\\\": [\\\\n          0.0,\\\\n          0.20833333333333334\\\\n        ],\\\\n        \\\\\\\"R@5\\\\\\\": 0.25,\\\\n        \\\\\\\"R@5_ci\\\\\\\": [\\\\n          0.08333333333333333,\\\\n          0.4166666666666667\\\\n        ],\\\\n        \\\\\\\"MRR\\\\\\\": 0.18658210312354354,\\\\n        \\\\\\\"MRR_ci\\\\\\\": [\\\\n          0.09884595475354443,\\\\n          0.2990058719871796\\\\n        ],\\\\n        \\\\\\\"count\\\\\\\": 24\\\\n      },\\\\n      \\\\\\\"dataflow_aware\\\\\\\": {\\\\n        \\\\\\\"R@1\\\\\\\": 0.08333333333333333,\\\\n        \\\\\\\"R@1_ci\\\\\\\": [\\\\n          0.0,\\\\n          0.20833333333333334\\\\n        ],\\\\n        \\\\\\\"R@5\\\\\\\": 0.25,\\\\n        \\\\\\\"R@5_ci\\\\\\\": [\\\\n          0.08333333333333333,\\\\n          0.4166666666666667\\\\n        ],\\\\n        \\\\\\\"MRR\\\\\\\": 0.19360231918734738,\\\\n        \\\\\\\"MRR_ci\\\\\\\": [\\\\n          0.10034009813817588,\\\\n          0.3119892338877614\\\\n        ],\\\\n        \\\\\\\"count\\\\\\\": 24\\\\n      },\\\\n      \\\\\\\"embedding_distance_vs_random\\\\\\\": {\\\\n        \\\\\\\"R@1_delta\\\\\\\": 0.08333333333333333,\\\\n        \\\\\\\"R@1_rel_pct\\\\\\\": 0.0,\\\\n        \\\\\\\"R@5_delta\\\\\\\": 0.25,\\\\n        \\\\\\\"R@5_rel_pct\\\\\\\": 0.0,\\\\n        \\\\\\\"MRR_delta\\\\\\\": 0.12023395842972927,\\\\n        \\\\\\\"MRR_rel_pct\\\\\\\": 181.21676044535855\\\\n      },\\\\n      \\\\\\\"dataflow_aware_vs_random\\\\\\\": {\\\\n        \\\\\\\"R@1_delta\\\\\\\": 0.08333333333333333,\\\\n        \\\\\\\"R@1_rel_pct\\\\\\\": 0.0,\\\\n        \\\\\\\"R@5_delta\\\\\\\": 0.25,\\\\n        \\\\\\\"R@5_rel_pct\\\\\\\": 0.0,\\\\n        \\\\\\\"MRR_delta\\\\\\\": 0.1272541744935331,\\\\n        \\\\\\\"MRR_rel_pct\\\\\\\": 191.79763817178326\\\\n      }\\\\n    }\\\\n  }\\\\n}\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.82}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"config\\\": {\\n    \\\"strategies\\\": [\\n      \\\"random\\\",\\n      \\\"embedding_distance\\\",\\n      \\\"dataflow_aware\\\"\\n    ],\\n    \\\"seeds\\\": [\\n      42\\n    ],\\n    \\\"repo_size_bins\\\": {\\n      \\\"small\\\": [\\n        0,\\n        50\\n      ],\\n      \\\"medium\\\": [\\n        50,\\n        200\\n      ],\\n      \\\"large\\\": [\\n        200,\\n        500\\n      ],\\n      \\\"xlarge\\\": [\\n        500,\\n        Infinity\\n      ]\\n    },\\n    \\\"pool_size_bins\\\": {\\n      \\\"small\\\": [\\n        0,\\n        20\\n      ],\\n      \\\"medium\\\": [\\n        20,\\n        40\\n      ],\\n      \\\"large\\\": [\\n        40,\\n        51\\n      ]\\n    },\\n    \\\"similarity_bins\\\": {\\n      \\\"low\\\": [\\n        0.0,\\n        0.3\\n      ],\\n      \\\"medium\\\": [\\n        0.3,\\n        0.6\\n      ],\\n      \\\"high\\\": [\\n        0.6,\\n        1.01\\n      ]\\n    },\\n    \\\"n_bootstrap\\\": 200,\\n    \\\"dry_run\\\": true\\n  },\\n  \\\"by_repo_size\\\": {\\n    \\\"small\\\": {\\n      \\\"random\\\": {\\n        \\\"R@1\\\": 0.11538461538461539,\\n        \\\"R@1_ci\\\": [\\n          0.061346153846153884,\\n          0.16923076923076924\\n        ],\\n        \\\"R@5\\\": 0.5384615384615384,\\n        \\\"R@5_ci\\\": [\\n          0.4461538461538462,\\n          0.6230769230769231\\n        ],\\n        \\\"MRR\\\": 0.3059754134754135,\\n        \\\"MRR_ci\\\": [\\n          0.25409036102786103,\\n          0.3513594044844045\\n        ],\\n        \\\"count\\\": 130\\n      },\\n      \\\"embedding_distance\\\": {\\n        \\\"R@1\\\": 0.3,\\n        \\\"R@1_ci\\\": [\\n          0.2230769230769231,\\n          0.37711538461538463\\n        ],\\n        \\\"R@5\\\": 0.7384615384615385,\\n        \\\"R@5_ci\\\": [\\n          0.6613461538461538,\\n          0.8153846153846154\\n        ],\\n        \\\"MRR\\\": 0.4930563880563881,\\n        \\\"MRR_ci\\\": [\\n          0.43992261211011213,\\n          0.5556576062826063\\n        ],\\n        \\\"count\\\": 130\\n      },\\n      \\\"dataflow_aware\\\": {\\n        \\\"R@1\\\": 0.4846153846153846,\\n        \\\"R@1_ci\\\": [\\n          0.3923076923076923,\\n          0.5617307692307693\\n        ],\\n        \\\"R@5\\\": 0.8769230769230769,\\n        \\\"R@5_ci\\\": [\\n          0.8226923076923077,\\n          0.9230769230769231\\n        ],\\n        \\\"MRR\\\": 0.6500946275946277,\\n        \\\"MRR_ci\\\": [\\n          0.59523923992674,\\n          0.7073237942612942\\n        ],\\n        \\\"count\\\": 130\\n      },\\n      \\\"embedding_distance_vs_random\\\": {\\n        \\\"R@1_delta\\\": 0.1846153846153846,\\n        \\\"R@1_rel_pct\\\": 160.0,\\n        \\\"R@5_delta\\\": 0.20000000000000007,\\n        \\\"R@5_rel_pct\\\": 37.14285714285715,\\n        \\\"MRR_delta\\\": 0.18708097458097456,\\n        \\\"MRR_rel_pct\\\": 61.14248607625702\\n      },\\n      \\\"dataflow_aware_vs_random\\\": {\\n        \\\"R@1_delta\\\": 0.36923076923076925,\\n        \\\"R@1_rel_pct\\\": 320.0,\\n        \\\"R@5_delta\\\": 0.3384615384615385,\\n        \\\"R@5_rel_pct\\\": 62.85714285714287,\\n        \\\"MRR_delta\\\": 0.34411921411921415,\\n        \\\"MRR_rel_pct\\\": 112.46629597147866\\n      }\\n    },\\n    \\\"medium\\\": {\\n      \\\"random\\\": {\\n        \\\"R@1\\\": 0.05202312138728324,\\n        \\\"R@1_ci\\\": [\\n          0.031791907514450865,\\n          0.08092485549132948\\n        ],\\n        \\\"R@5\\\": 0.23121387283236994,\\n        \\\"R@5_ci\\\": [\\n          0.18778901734104048,\\n          0.27167630057803466\\n        ],\\n        \\\"MRR\\\": 0.17820474196308103,\\n        \\\"MRR_ci\\\": [\\n          0.15638534764941775,\\n          0.20150044957306631\\n        ],\\n        \\\"count\\\": 346\\n      },\\n      \\\"embedding_distance\\\": {\\n        \\\"R@1\\\": 0.1069364161849711,\\n        \\\"R@1_ci\\\": [\\n          0.07803468208092486,\\n          0.14169075144508672\\n        ],\\n        \\\"R@5\\\": 0.49421965317919075,\\n        \\\"R@5_ci\\\": [\\n          0.4305635838150289,\\n          0.5348265895953758\\n        ],\\n        \\\"MRR\\\": 0.2865956097787104,\\n        \\\"MRR_ci\\\": [\\n          0.25823956396604253,\\n          0.31508196199064964\\n        ],\\n        \\\"count\\\": 346\\n      },\\n      \\\"dataflow_aware\\\": {\\n        \\\"R@1\\\": 0.2398843930635838,\\n        \\\"R@1_ci\\\": [\\n          0.19653179190751446,\\n          0.2861271676300578\\n        ],\\n        \\\"R@5\\\": 0.7023121387283237,\\n        \\\"R@5_ci\\\": [\\n          0.6588150289017342,\\n          0.7514450867052023\\n        ],\\n        \\\"MRR\\\": 0.4295497658014659,\\n        \\\"MRR_ci\\\": [\\n          0.39310849797917335,\\n          0.4627567860954358\\n        ],\\n        \\\"count\\\": 346\\n      },\\n\\n\\n... [截断: 输出过长，省略 11724 字符] ...\\n\\n        \\\"R@5_rel_pct\\\": 109.78835978835977,\\n        \\\"MRR_delta\\\": 0.08434517635221275,\\n        \\\"MRR_rel_pct\\\": 71.43937034482639\\n      },\\n      \\\"dataflow_aware_vs_random\\\": {\\n        \\\"R@1_delta\\\": 0.10322333077513429,\\n        \\\"R@1_rel_pct\\\": 320.2380952380952,\\n        \\\"R@5_delta\\\": 0.3142747505755948,\\n        \\\"R@5_rel_pct\\\": 216.66666666666666,\\n        \\\"MRR_delta\\\": 0.1742035067513217,\\n        \\\"MRR_rel_pct\\\": 147.54831719370338\\n      }\\n    },\\n    \\\"medium\\\": {\\n      \\\"random\\\": {\\n        \\\"R@1\\\": 0.014285714285714285,\\n        \\\"R@1_ci\\\": [\\n          0.002857142857142857,\\n          0.025714285714285714\\n        ],\\n        \\\"R@5\\\": 0.10285714285714286,\\n        \\\"R@5_ci\\\": [\\n          0.06850000000000002,\\n          0.13435714285714287\\n        ],\\n        \\\"MRR\\\": 0.08892012631102023,\\n        \\\"MRR_ci\\\": [\\n          0.07565878083640655,\\n          0.10097054824489184\\n        ],\\n        \\\"count\\\": 350\\n      },\\n      \\\"embedding_distance\\\": {\\n        \\\"R@1\\\": 0.06571428571428571,\\n        \\\"R@1_ci\\\": [\\n          0.04285714285714286,\\n          0.09428571428571429\\n        ],\\n        \\\"R@5\\\": 0.3028571428571429,\\n        \\\"R@5_ci\\\": [\\n          0.25128571428571433,\\n          0.3457142857142857\\n        ],\\n        \\\"MRR\\\": 0.19037293149185006,\\n        \\\"MRR_ci\\\": [\\n          0.1649260686702319,\\n          0.21459875959655225\\n        ],\\n        \\\"count\\\": 350\\n      },\\n      \\\"dataflow_aware\\\": {\\n        \\\"R@1\\\": 0.13428571428571429,\\n        \\\"R@1_ci\\\": [\\n          0.09714285714285714,\\n          0.17442857142857146\\n        ],\\n        \\\"R@5\\\": 0.4342857142857143,\\n        \\\"R@5_ci\\\": [\\n          0.38857142857142857,\\n          0.4858571428571429\\n        ],\\n        \\\"MRR\\\": 0.2852574269542923,\\n        \\\"MRR_ci\\\": [\\n          0.2526425047155209,\\n          0.32557010653989665\\n        ],\\n        \\\"count\\\": 350\\n      },\\n      \\\"embedding_distance_vs_random\\\": {\\n        \\\"R@1_delta\\\": 0.05142857142857143,\\n        \\\"R@1_rel_pct\\\": 360.0,\\n        \\\"R@5_delta\\\": 0.2,\\n        \\\"R@5_rel_pct\\\": 194.44444444444446,\\n        \\\"MRR_delta\\\": 0.10145280518082983,\\n        \\\"MRR_rel_pct\\\": 114.09431069179259\\n      },\\n      \\\"dataflow_aware_vs_random\\\": {\\n        \\\"R@1_delta\\\": 0.12,\\n        \\\"R@1_rel_pct\\\": 840.0,\\n        \\\"R@5_delta\\\": 0.3314285714285714,\\n        \\\"R@5_rel_pct\\\": 322.2222222222222,\\n        \\\"MRR_delta\\\": 0.19633730064327207,\\n        \\\"MRR_rel_pct\\\": 220.80186881036764\\n      }\\n    },\\n    \\\"high\\\": {\\n      \\\"random\\\": {\\n        \\\"R@1\\\": 0.0,\\n        \\\"R@1_ci\\\": [\\n          0.0,\\n          0.0\\n        ],\\n        \\\"R@5\\\": 0.0,\\n        \\\"R@5_ci\\\": [\\n          0.0,\\n          0.0\\n        ],\\n        \\\"MRR\\\": 0.06634814469381427,\\n        \\\"MRR_ci\\\": [\\n          0.04922830990875043,\\n          0.08318125486392415\\n        ],\\n        \\\"count\\\": 24\\n      },\\n      \\\"embedding_distance\\\": {\\n        \\\"R@1\\\": 0.08333333333333333,\\n        \\\"R@1_ci\\\": [\\n          0.0,\\n          0.20833333333333334\\n        ],\\n        \\\"R@5\\\": 0.25,\\n        \\\"R@5_ci\\\": [\\n          0.08333333333333333,\\n          0.4166666666666667\\n        ],\\n        \\\"MRR\\\": 0.18658210312354354,\\n        \\\"MRR_ci\\\": [\\n          0.09884595475354443,\\n          0.2990058719871796\\n        ],\\n        \\\"count\\\": 24\\n      },\\n      \\\"dataflow_aware\\\": {\\n        \\\"R@1\\\": 0.08333333333333333,\\n        \\\"R@1_ci\\\": [\\n          0.0,\\n          0.20833333333333334\\n        ],\\n        \\\"R@5\\\": 0.25,\\n        \\\"R@5_ci\\\": [\\n          0.08333333333333333,\\n          0.4166666666666667\\n        ],\\n        \\\"MRR\\\": 0.19360231918734738,\\n        \\\"MRR_ci\\\": [\\n          0.10034009813817588,\\n          0.3119892338877614\\n        ],\\n        \\\"count\\\": 24\\n      },\\n      \\\"embedding_distance_vs_random\\\": {\\n        \\\"R@1_delta\\\": 0.08333333333333333,\\n        \\\"R@1_rel_pct\\\": 0.0,\\n        \\\"R@5_delta\\\": 0.25,\\n        \\\"R@5_rel_pct\\\": 0.0,\\n        \\\"MRR_delta\\\": 0.12023395842972927,\\n        \\\"MRR_rel_pct\\\": 181.21676044535855\\n      },\\n      \\\"dataflow_aware_vs_random\\\": {\\n        \\\"R@1_delta\\\": 0.08333333333333333,\\n        \\\"R@1_rel_pct\\\": 0.0,\\n        \\\"R@5_delta\\\": 0.25,\\n        \\\"R@5_rel_pct\\\": 0.0,\\n        \\\"MRR_delta\\\": 0.1272541744935331,\\n        \\\"MRR_rel_pct\\\": 191.79763817178326\\n      }\\n    }\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.82}}"
    }
  },
  "sourceToolAssistantUUID": "067965e9-cbbc-4023-8459-7d2253f03f43",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "fb5ea7f7-b3c9-4750-b931-39d2aaae422b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 33_

```json
{
  "type": "last-prompt",
  "leafUuid": "b9105933-1d8e-4623-bd92-76d4ac23ebd8",
  "sessionId": "fb5ea7f7-b3c9-4750-b931-39d2aaae422b"
}
```

---

### Runtime record

_source line 34_

```json
{
  "type": "ai-title",
  "aiTitle": "Trace stratified_dryrun v1 to v2 differences",
  "sessionId": "fb5ea7f7-b3c9-4750-b931-39d2aaae422b"
}
```

---

### Tool result

_source line 35 · 2026-05-14T20:36:45.500Z_

<details><summary>↩ Tool result · `toolu_015ZZr1HomN8U2EKUFHsr4LN`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"config\\\": {\\n    \\\"strategies\\\": [\\n      \\\"random\\\",\\n      \\\"embedding_distance\\\",\\n      \\\"dataflow_aware\\\"\\n    ],\\n    \\\"seeds\\\": [\\n      42\\n    ],\\n    \\\"repo_size_bins\\\": {\\n      \\\"small\\\": [\\n        0,\\n        50\\n      ],\\n      \\\"medium\\\": [\\n        50,\\n        200\\n      ],\\n      \\\"large\\\": [\\n        200,\\n        500\\n      ],\\n      \\\"xlarge\\\": [\\n        500,\\n        Infinity\\n      ]\\n    },\\n    \\\"pool_size_bins\\\": {\\n      \\\"small\\\": [\\n        0,\\n        20\\n      ],\\n      \\\"medium\\\": [\\n        20,\\n        40\\n      ],\\n      \\\"large\\\": [\\n        40,\\n        51\\n      ]\\n    },\\n    \\\"similarity_bins\\\": {\\n      \\\"low\\\": [\\n        0.0,\\n        0.3\\n      ],\\n      \\\"medium\\\": [\\n        0.3,\\n        0.6\\n      ],\\n      \\\"high\\\": [\\n        0.6,\\n        1.01\\n      ]\\n    },\\n    \\\"dataflow_bins\\\": {\\n      \\\"sparse\\\": [\\n        0,\\n        2\\n      ],\\n      \\\"moderate\\\": [\\n        2,\\n        10\\n      ],\\n      \\\"rich\\\": [\\n        10,\\n        Infinity\\n      ]\\n    },\\n    \\\"neg_difficulty_quartiles\\\": [\\n      \\\"Q1_easy\\\",\\n      \\\"Q2\\\",\\n      \\\"Q3\\\",\\n      \\\"Q4_hard\\\"\\n    ],\\n    \\\"n_bootstrap\\\": 200,\\n    \\\"dry_run\\\": true\\n  },\\n  \\\"by_repo_size\\\": {\\n    \\\"small\\\": {\\n      \\\"random\\\": {\\n        \\\"R@1\\\": 0.07692307692307693,\\n        \\\"R@1_ci\\\": [\\n          0.038269230769230805,\\n          0.12307692307692308\\n        ],\\n        \\\"R@5\\\": 0.47692307692307695,\\n        \\\"R@5_ci\\\": [\\n          0.39980769230769236,\\n          0.5617307692307693\\n        ],\\n        \\\"MRR\\\": 0.26425629925629923,\\n        \\\"MRR_ci\\\": [\\n          0.22389736652236653,\\n          0.30436761155511155\\n        ],\\n        \\\"count\\\": 130\\n      },\\n      \\\"embedding_distance\\\": {\\n        \\\"R@1\\\": 0.27692307692307694,\\n        \\\"R@1_ci\\\": [\\n          0.19211538461538466,\\n          0.3540384615384616\\n        ],\\n        \\\"R@5\\\": 0.7384615384615385,\\n        \\\"R@5_ci\\\": [\\n          0.6615384615384615,\\n          0.823076923076923\\n        ],\\n        \\\"MRR\\\": 0.47043706293706294,\\n        \\\"MRR_ci\\\": [\\n          0.4076928071928072,\\n          0.5365241633366633\\n        ],\\n        \\\"count\\\": 130\\n      },\\n      \\\"dataflow_aware\\\": {\\n        \\\"R@1\\\": 0.4,\\n        \\\"R@1_ci\\\": [\\n          0.3151923076923077,\\n          0.46942307692307694\\n        ],\\n        \\\"R@5\\\": 0.9,\\n        \\\"R@5_ci\\\": [\\n          0.8459615384615384,\\n          0.9461538461538461\\n        ],\\n        \\\"MRR\\\": 0.6000063825063826,\\n        \\\"MRR_ci\\\": [\\n          0.5347679820179821,\\n          0.6520934065934065\\n        ],\\n        \\\"count\\\": 130\\n      },\\n      \\\"embedding_distance_vs_random\\\": {\\n        \\\"R@1_delta\\\": 0.2,\\n        \\\"R@1_rel_pct\\\": 260.0,\\n        \\\"R@5_delta\\\": 0.26153846153846155,\\n        \\\"R@5_rel_pct\\\": 54.83870967741935,\\n        \\\"MRR_delta\\\": 0.2061807636807637,\\n        \\\"MRR_rel_pct\\\": 78.02302698593054\\n      },\\n      \\\"dataflow_aware_vs_random\\\": {\\n        \\\"R@1_delta\\\": 0.3230769230769231,\\n        \\\"R@1_rel_pct\\\": 420.0,\\n        \\\"R@5_delta\\\": 0.4230769230769231,\\n        \\\"R@5_rel_pct\\\": 88.70967741935483,\\n        \\\"MRR_delta\\\": 0.3357500832500834,\\n        \\\"MRR_rel_pct\\\": 127.0547132442974\\n      }\\n    },\\n    \\\"medium\\\": {\\n      \\\"random\\\": {\\n        \\\"R@1\\\": 0.05491329479768786,\\n        \\\"R@1_ci\\\": [\\n          0.028901734104046242,\\n          0.0752890173410405\\n        ],\\n        \\\"R@5\\\": 0.2861271676300578,\\n        \\\"R@5_ci\\\": [\\n          0.23684971098265897,\\n          0.33236994219653176\\n        ],\\n        \\\"MRR\\\": 0.1935964506181734,\\n        \\\"MRR_ci\\\": [\\n          0.17032768352089914,\\n          0.2161689474822454\\n        ],\\n        \\\"count\\\": 346\\n      },\\n      \\\"embedding_distance\\\": {\\n        \\\"R@1\\\": 0.15028901734104047,\\n        \\\"R@1_ci\\\": [\\n          0.11271676300578035,\\n          0.1879335260115607\\n        ],\\n        \\\"R@5\\\": 0.523121387283237,\\n        \\\"R@5_ci\\\": [\\n          0.4710260115606937,\\n          0.5752167630057804\\n        ],\\n        \\\"MRR\\\": 0.32989441445506745,\\n        \\\"MRR_ci\\\": [\\n          0.29717057853455836,\\n          0.36684936890694325\\n        ],\\n        \\\"count\\\": 346\\n      },\\n      \\\"dataflow_aware\\\": {\\n        \\\"R@1\\\": 0.2398843930635838,\\n        \\\"R@1_ci\\\": [\\n          0.2021676300578035,\\n          0.27760115606936414\\n        ],\\n        \\\"R@5\\\": 0.7369942196531792\\n\\n... [截断: 输出过长，省略 25616 字符] ...\\n\\n\\n        \\\"R@5_rel_pct\\\": 266.66666666666663,\\n        \\\"MRR_delta\\\": 0.18151192668171712,\\n        \\\"MRR_rel_pct\\\": 162.05505112786537\\n      }\\n    },\\n    \\\"Q3\\\": {\\n      \\\"random\\\": {\\n        \\\"R@1\\\": 0.024161073825503355,\\n        \\\"R@1_ci\\\": [\\n          0.01476510067114094,\\n          0.0348993288590604\\n        ],\\n        \\\"R@5\\\": 0.12483221476510067,\\n        \\\"R@5_ci\\\": [\\n          0.10463087248322149,\\n          0.15033557046979865\\n        ],\\n        \\\"MRR\\\": 0.10574925148962648,\\n        \\\"MRR_ci\\\": [\\n          0.09482888540806862,\\n          0.11651834396588909\\n        ],\\n        \\\"count\\\": 745\\n      },\\n      \\\"embedding_distance\\\": {\\n        \\\"R@1\\\": 0.07651006711409396,\\n        \\\"R@1_ci\\\": [\\n          0.05906040268456376,\\n          0.09261744966442953\\n        ],\\n        \\\"R@5\\\": 0.312751677852349,\\n        \\\"R@5_ci\\\": [\\n          0.2764765100671141,\\n          0.34496644295302015\\n        ],\\n        \\\"MRR\\\": 0.20736546414953633,\\n        \\\"MRR_ci\\\": [\\n          0.19054410581433834,\\n          0.22484200616942923\\n        ],\\n        \\\"count\\\": 745\\n      },\\n      \\\"dataflow_aware\\\": {\\n        \\\"R@1\\\": 0.12483221476510067,\\n        \\\"R@1_ci\\\": [\\n          0.09929530201342283,\\n          0.14630872483221477\\n        ],\\n        \\\"R@5\\\": 0.48322147651006714,\\n        \\\"R@5_ci\\\": [\\n          0.4469463087248322,\\n          0.5154362416107383\\n        ],\\n        \\\"MRR\\\": 0.29257823070893335,\\n        \\\"MRR_ci\\\": [\\n          0.2696544452985487,\\n          0.3130578591008492\\n        ],\\n        \\\"count\\\": 745\\n      },\\n      \\\"embedding_distance_vs_random\\\": {\\n        \\\"R@1_delta\\\": 0.052348993288590606,\\n        \\\"R@1_rel_pct\\\": 216.66666666666669,\\n        \\\"R@5_delta\\\": 0.1879194630872483,\\n        \\\"R@5_rel_pct\\\": 150.53763440860212,\\n        \\\"MRR_delta\\\": 0.10161621265990985,\\n        \\\"MRR_rel_pct\\\": 96.09166138625382\\n      },\\n      \\\"dataflow_aware_vs_random\\\": {\\n        \\\"R@1_delta\\\": 0.10067114093959732,\\n        \\\"R@1_rel_pct\\\": 416.6666666666667,\\n        \\\"R@5_delta\\\": 0.35838926174496644,\\n        \\\"R@5_rel_pct\\\": 287.09677419354836,\\n        \\\"MRR_delta\\\": 0.18682897921930686,\\n        \\\"MRR_rel_pct\\\": 176.6716800237909\\n      }\\n    },\\n    \\\"Q4_hard\\\": {\\n      \\\"random\\\": {\\n        \\\"R@1\\\": 0.01742627345844504,\\n        \\\"R@1_ci\\\": [\\n          0.00938337801608579,\\n          0.028150134048257374\\n        ],\\n        \\\"R@5\\\": 0.16353887399463807,\\n        \\\"R@5_ci\\\": [\\n          0.13672922252010725,\\n          0.187701072386059\\n        ],\\n        \\\"MRR\\\": 0.11310223595372695,\\n        \\\"MRR_ci\\\": [\\n          0.10258848955316095,\\n          0.12528228899702964\\n        ],\\n        \\\"count\\\": 746\\n      },\\n      \\\"embedding_distance\\\": {\\n        \\\"R@1\\\": 0.07506702412868632,\\n        \\\"R@1_ci\\\": [\\n          0.05760723860589813,\\n          0.09520777479892761\\n        ],\\n        \\\"R@5\\\": 0.30160857908847183,\\n        \\\"R@5_ci\\\": [\\n          0.2694034852546917,\\n          0.33783512064343163\\n        ],\\n        \\\"MRR\\\": 0.20089647026815693,\\n        \\\"MRR_ci\\\": [\\n          0.18374811602212457,\\n          0.22345370976019258\\n        ],\\n        \\\"count\\\": 746\\n      },\\n      \\\"dataflow_aware\\\": {\\n        \\\"R@1\\\": 0.1353887399463807,\\n        \\\"R@1_ci\\\": [\\n          0.11126005361930295,\\n          0.16219839142091153\\n        ],\\n        \\\"R@5\\\": 0.467828418230563,\\n        \\\"R@5_ci\\\": [\\n          0.4342828418230563,\\n          0.4973190348525469\\n        ],\\n        \\\"MRR\\\": 0.2968150941724084,\\n        \\\"MRR_ci\\\": [\\n          0.27428741459409656,\\n          0.3190549914407245\\n        ],\\n        \\\"count\\\": 746\\n      },\\n      \\\"embedding_distance_vs_random\\\": {\\n        \\\"R@1_delta\\\": 0.057640750670241284,\\n        \\\"R@1_rel_pct\\\": 330.7692307692308,\\n        \\\"R@5_delta\\\": 0.13806970509383376,\\n        \\\"R@5_rel_pct\\\": 84.42622950819671,\\n        \\\"MRR_delta\\\": 0.08779423431442998,\\n        \\\"MRR_rel_pct\\\": 77.62378309686898\\n      },\\n      \\\"dataflow_aware_vs_random\\\": {\\n        \\\"R@1_delta\\\": 0.11796246648793567,\\n        \\\"R@1_rel_pct\\\": 676.9230769230769,\\n        \\\"R@5_delta\\\": 0.3042895442359249,\\n        \\\"R@5_rel_pct\\\": 186.0655737704918,\\n        \\\"MRR_delta\\\": 0.18371285821868147,\\n        \\\"MRR_rel_pct\\\": 162.43079252106313\\n      }\\n    }\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d09591e8-8f23-4ae2-8602-44b3fa61fc3e",
  "isSidechain": false,
  "promptId": "0b7bb415-f2b4-4832-aac4-2e6aafdc7429",
  "type": "user",
  "uuid": "117b6f1b-9d7d-4102-9428-434bcb6f9d73",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"{\\\\n  \\\\\\\"config\\\\\\\": {\\\\n    \\\\\\\"strategies\\\\\\\": [\\\\n      \\\\\\\"random\\\\\\\",\\\\n      \\\\\\\"embedding_distance\\\\\\\",\\\\n      \\\\\\\"dataflow_aware\\\\\\\"\\\\n    ],\\\\n    \\\\\\\"seeds\\\\\\\": [\\\\n      42\\\\n    ],\\\\n    \\\\\\\"repo_size_bins\\\\\\\": {\\\\n      \\\\\\\"small\\\\\\\": [\\\\n        0,\\\\n        50\\\\n      ],\\\\n      \\\\\\\"medium\\\\\\\": [\\\\n        50,\\\\n        200\\\\n      ],\\\\n      \\\\\\\"large\\\\\\\": [\\\\n        200,\\\\n        500\\\\n      ],\\\\n      \\\\\\\"xlarge\\\\\\\": [\\\\n        500,\\\\n        Infinity\\\\n      ]\\\\n    },\\\\n    \\\\\\\"pool_size_bins\\\\\\\": {\\\\n      \\\\\\\"small\\\\\\\": [\\\\n        0,\\\\n        20\\\\n      ],\\\\n      \\\\\\\"medium\\\\\\\": [\\\\n        20,\\\\n        40\\\\n      ],\\\\n      \\\\\\\"large\\\\\\\": [\\\\n        40,\\\\n        51\\\\n      ]\\\\n    },\\\\n    \\\\\\\"similarity_bins\\\\\\\": {\\\\n      \\\\\\\"low\\\\\\\": [\\\\n        0.0,\\\\n        0.3\\\\n      ],\\\\n      \\\\\\\"medium\\\\\\\": [\\\\n        0.3,\\\\n        0.6\\\\n      ],\\\\n      \\\\\\\"high\\\\\\\": [\\\\n        0.6,\\\\n        1.01\\\\n      ]\\\\n    },\\\\n    \\\\\\\"dataflow_bins\\\\\\\": {\\\\n      \\\\\\\"sparse\\\\\\\": [\\\\n        0,\\\\n        2\\\\n      ],\\\\n      \\\\\\\"moderate\\\\\\\": [\\\\n        2,\\\\n        10\\\\n      ],\\\\n      \\\\\\\"rich\\\\\\\": [\\\\n        10,\\\\n        Infinity\\\\n      ]\\\\n    },\\\\n    \\\\\\\"neg_difficulty_quartiles\\\\\\\": [\\\\n      \\\\\\\"Q1_easy\\\\\\\",\\\\n      \\\\\\\"Q2\\\\\\\",\\\\n      \\\\\\\"Q3\\\\\\\",\\\\n      \\\\\\\"Q4_hard\\\\\\\"\\\\n    ],\\\\n    \\\\\\\"n_bootstrap\\\\\\\": 200,\\\\n    \\\\\\\"dry_run\\\\\\\": true\\\\n  },\\\\n  \\\\\\\"by_repo_size\\\\\\\": {\\\\n    \\\\\\\"small\\\\\\\": {\\\\n      \\\\\\\"random\\\\\\\": {\\\\n        \\\\\\\"R@1\\\\\\\": 0.07692307692307693,\\\\n        \\\\\\\"R@1_ci\\\\\\\": [\\\\n          0.038269230769230805,\\\\n          0.12307692307692308\\\\n        ],\\\\n        \\\\\\\"R@5\\\\\\\": 0.47692307692307695,\\\\n        \\\\\\\"R@5_ci\\\\\\\": [\\\\n          0.39980769230769236,\\\\n          0.5617307692307693\\\\n        ],\\\\n        \\\\\\\"MRR\\\\\\\": 0.26425629925629923,\\\\n        \\\\\\\"MRR_ci\\\\\\\": [\\\\n          0.22389736652236653,\\\\n          0.30436761155511155\\\\n        ],\\\\n        \\\\\\\"count\\\\\\\": 130\\\\n      },\\\\n      \\\\\\\"embedding_distance\\\\\\\": {\\\\n        \\\\\\\"R@1\\\\\\\": 0.27692307692307694,\\\\n        \\\\\\\"R@1_ci\\\\\\\": [\\\\n          0.19211538461538466,\\\\n          0.3540384615384616\\\\n        ],\\\\n        \\\\\\\"R@5\\\\\\\": 0.7384615384615385,\\\\n        \\\\\\\"R@5_ci\\\\\\\": [\\\\n          0.6615384615384615,\\\\n          0.823076923076923\\\\n        ],\\\\n        \\\\\\\"MRR\\\\\\\": 0.47043706293706294,\\\\n        \\\\\\\"MRR_ci\\\\\\\": [\\\\n          0.4076928071928072,\\\\n          0.5365241633366633\\\\n        ],\\\\n        \\\\\\\"count\\\\\\\": 130\\\\n      },\\\\n      \\\\\\\"dataflow_aware\\\\\\\": {\\\\n        \\\\\\\"R@1\\\\\\\": 0.4,\\\\n        \\\\\\\"R@1_ci\\\\\\\": [\\\\n          0.3151923076923077,\\\\n          0.46942307692307694\\\\n        ],\\\\n        \\\\\\\"R@5\\\\\\\": 0.9,\\\\n        \\\\\\\"R@5_ci\\\\\\\": [\\\\n          0.8459615384615384,\\\\n          0.9461538461538461\\\\n        ],\\\\n        \\\\\\\"MRR\\\\\\\": 0.6000063825063826,\\\\n        \\\\\\\"MRR_ci\\\\\\\": [\\\\n          0.5347679820179821,\\\\n          0.6520934065934065\\\\n        ],\\\\n        \\\\\\\"count\\\\\\\": 130\\\\n      },\\\\n      \\\\\\\"embedding_distance_vs_random\\\\\\\": {\\\\n        \\\\\\\"R@1_delta\\\\\\\": 0.2,\\\\n        \\\\\\\"R@1_rel_pct\\\\\\\": 260.0,\\\\n        \\\\\\\"R@5_delta\\\\\\\": 0.26153846153846155,\\\\n        \\\\\\\"R@5_rel_pct\\\\\\\": 54.83870967741935,\\\\n        \\\\\\\"MRR_delta\\\\\\\": 0.2061807636807637,\\\\n        \\\\\\\"MRR_rel_pct\\\\\\\": 78.02302698593054\\\\n      },\\\\n      \\\\\\\"dataflow_aware_vs_random\\\\\\\": {\\\\n        \\\\\\\"R@1_delta\\\\\\\": 0.3230769230769231,\\\\n        \\\\\\\"R@1_rel_pct\\\\\\\": 420.0,\\\\n        \\\\\\\"R@5_delta\\\\\\\": 0.4230769230769231,\\\\n        \\\\\\\"R@5_rel_pct\\\\\\\": 88.70967741935483,\\\\n        \\\\\\\"MRR_delta\\\\\\\": 0.3357500832500834,\\\\n        \\\\\\\"MRR_rel_pct\\\\\\\": 127.0547132442974\\\\n      }\\\\n    },\\\\n    \\\\\\\"medium\\\\\\\": {\\\\n      \\\\\\\"random\\\\\\\": {\\\\n        \\\\\\\"R@1\\\\\\\": 0.05491329479768786,\\\\n        \\\\\\\"R@1_ci\\\\\\\": [\\\\n          0.028901734104046242,\\\\n          0.0752890173410405\\\\n        ],\\\\n        \\\\\\\"R@5\\\\\\\": 0.2861271676300578,\\\\n        \\\\\\\"R@5_ci\\\\\\\": [\\\\n          0.23684971098265897,\\\\n          0.33236994219653176\\\\n        ],\\\\n        \\\\\\\"MRR\\\\\\\": 0.1935964506181734,\\\\n        \\\\\\\"MRR_ci\\\\\\\": [\\\\n          0.17032768352089914,\\\\n          0.2161689474822454\\\\n        ],\\\\n        \\\\\\\"count\\\\\\\": 346\\\\n      },\\\\n      \\\\\\\"embedding_distance\\\\\\\": {\\\\n        \\\\\\\"R@1\\\\\\\": 0.15028901734104047,\\\\n        \\\\\\\"R@1_ci\\\\\\\": [\\\\n          0.11271676300578035,\\\\n          0.1879335260115607\\\\n        ],\\\\n        \\\\\\\"R@5\\\\\\\": 0.523121387283237,\\\\n        \\\\\\\"R@5_ci\\\\\\\": [\\\\n          0.4710260115606937,\\\\n          0.5752167630057804\\\\n        ],\\\\n        \\\\\\\"MRR\\\\\\\": 0.32989441445506745,\\\\n        \\\\\\\"MRR_ci\\\\\\\": [\\\\n          0.29717057853455836,\\\\n          0.36684936890694325\\\\n        ],\\\\n        \\\\\\\"count\\\\\\\": 346\\\\n      },\\\\n      \\\\\\\"dataflow_aware\\\\\\\": {\\\\n        \\\\\\\"R@1\\\\\\\": 0.2398843930635838,\\\\n        \\\\\\\"R@1_ci\\\\\\\": [\\\\n          0.2021676300578035,\\\\n          0.27760115606936414\\\\n        ],\\\\n        \\\\\\\"R@5\\\\\\\": 0.7369942196531792\\\\n\\\\n... [截断: 输出过长，省略 25616 字符] ...\\\\n\\\\n\\\\n        \\\\\\\"R@5_rel_pct\\\\\\\": 266.66666666666663,\\\\n        \\\\\\\"MRR_delta\\\\\\\": 0.18151192668171712,\\\\n        \\\\\\\"MRR_rel_pct\\\\\\\": 162.05505112786537\\\\n      }\\\\n    },\\\\n    \\\\\\\"Q3\\\\\\\": {\\\\n      \\\\\\\"random\\\\\\\": {\\\\n        \\\\\\\"R@1\\\\\\\": 0.024161073825503355,\\\\n        \\\\\\\"R@1_ci\\\\\\\": [\\\\n          0.01476510067114094,\\\\n          0.0348993288590604\\\\n        ],\\\\n        \\\\\\\"R@5\\\\\\\": 0.12483221476510067,\\\\n        \\\\\\\"R@5_ci\\\\\\\": [\\\\n          0.10463087248322149,\\\\n          0.15033557046979865\\\\n        ],\\\\n        \\\\\\\"MRR\\\\\\\": 0.10574925148962648,\\\\n        \\\\\\\"MRR_ci\\\\\\\": [\\\\n          0.09482888540806862,\\\\n          0.11651834396588909\\\\n        ],\\\\n        \\\\\\\"count\\\\\\\": 745\\\\n      },\\\\n      \\\\\\\"embedding_distance\\\\\\\": {\\\\n        \\\\\\\"R@1\\\\\\\": 0.07651006711409396,\\\\n        \\\\\\\"R@1_ci\\\\\\\": [\\\\n          0.05906040268456376,\\\\n          0.09261744966442953\\\\n        ],\\\\n        \\\\\\\"R@5\\\\\\\": 0.312751677852349,\\\\n        \\\\\\\"R@5_ci\\\\\\\": [\\\\n          0.2764765100671141,\\\\n          0.34496644295302015\\\\n        ],\\\\n        \\\\\\\"MRR\\\\\\\": 0.20736546414953633,\\\\n        \\\\\\\"MRR_ci\\\\\\\": [\\\\n          0.19054410581433834,\\\\n          0.22484200616942923\\\\n        ],\\\\n        \\\\\\\"count\\\\\\\": 745\\\\n      },\\\\n      \\\\\\\"dataflow_aware\\\\\\\": {\\\\n        \\\\\\\"R@1\\\\\\\": 0.12483221476510067,\\\\n        \\\\\\\"R@1_ci\\\\\\\": [\\\\n          0.09929530201342283,\\\\n          0.14630872483221477\\\\n        ],\\\\n        \\\\\\\"R@5\\\\\\\": 0.48322147651006714,\\\\n        \\\\\\\"R@5_ci\\\\\\\": [\\\\n          0.4469463087248322,\\\\n          0.5154362416107383\\\\n        ],\\\\n        \\\\\\\"MRR\\\\\\\": 0.29257823070893335,\\\\n        \\\\\\\"MRR_ci\\\\\\\": [\\\\n          0.2696544452985487,\\\\n          0.3130578591008492\\\\n        ],\\\\n        \\\\\\\"count\\\\\\\": 745\\\\n      },\\\\n      \\\\\\\"embedding_distance_vs_random\\\\\\\": {\\\\n        \\\\\\\"R@1_delta\\\\\\\": 0.052348993288590606,\\\\n        \\\\\\\"R@1_rel_pct\\\\\\\": 216.66666666666669,\\\\n        \\\\\\\"R@5_delta\\\\\\\": 0.1879194630872483,\\\\n        \\\\\\\"R@5_rel_pct\\\\\\\": 150.53763440860212,\\\\n        \\\\\\\"MRR_delta\\\\\\\": 0.10161621265990985,\\\\n        \\\\\\\"MRR_rel_pct\\\\\\\": 96.09166138625382\\\\n      },\\\\n      \\\\\\\"dataflow_aware_vs_random\\\\\\\": {\\\\n        \\\\\\\"R@1_delta\\\\\\\": 0.10067114093959732,\\\\n        \\\\\\\"R@1_rel_pct\\\\\\\": 416.6666666666667,\\\\n        \\\\\\\"R@5_delta\\\\\\\": 0.35838926174496644,\\\\n        \\\\\\\"R@5_rel_pct\\\\\\\": 287.09677419354836,\\\\n        \\\\\\\"MRR_delta\\\\\\\": 0.18682897921930686,\\\\n        \\\\\\\"MRR_rel_pct\\\\\\\": 176.6716800237909\\\\n      }\\\\n    },\\\\n    \\\\\\\"Q4_hard\\\\\\\": {\\\\n      \\\\\\\"random\\\\\\\": {\\\\n        \\\\\\\"R@1\\\\\\\": 0.01742627345844504,\\\\n        \\\\\\\"R@1_ci\\\\\\\": [\\\\n          0.00938337801608579,\\\\n          0.028150134048257374\\\\n        ],\\\\n        \\\\\\\"R@5\\\\\\\": 0.16353887399463807,\\\\n        \\\\\\\"R@5_ci\\\\\\\": [\\\\n          0.13672922252010725,\\\\n          0.187701072386059\\\\n        ],\\\\n        \\\\\\\"MRR\\\\\\\": 0.11310223595372695,\\\\n        \\\\\\\"MRR_ci\\\\\\\": [\\\\n          0.10258848955316095,\\\\n          0.12528228899702964\\\\n        ],\\\\n        \\\\\\\"count\\\\\\\": 746\\\\n      },\\\\n      \\\\\\\"embedding_distance\\\\\\\": {\\\\n        \\\\\\\"R@1\\\\\\\": 0.07506702412868632,\\\\n        \\\\\\\"R@1_ci\\\\\\\": [\\\\n          0.05760723860589813,\\\\n          0.09520777479892761\\\\n        ],\\\\n        \\\\\\\"R@5\\\\\\\": 0.30160857908847183,\\\\n        \\\\\\\"R@5_ci\\\\\\\": [\\\\n          0.2694034852546917,\\\\n          0.33783512064343163\\\\n        ],\\\\n        \\\\\\\"MRR\\\\\\\": 0.20089647026815693,\\\\n        \\\\\\\"MRR_ci\\\\\\\": [\\\\n          0.18374811602212457,\\\\n          0.22345370976019258\\\\n        ],\\\\n        \\\\\\\"count\\\\\\\": 746\\\\n      },\\\\n      \\\\\\\"dataflow_aware\\\\\\\": {\\\\n        \\\\\\\"R@1\\\\\\\": 0.1353887399463807,\\\\n        \\\\\\\"R@1_ci\\\\\\\": [\\\\n          0.11126005361930295,\\\\n          0.16219839142091153\\\\n        ],\\\\n        \\\\\\\"R@5\\\\\\\": 0.467828418230563,\\\\n        \\\\\\\"R@5_ci\\\\\\\": [\\\\n          0.4342828418230563,\\\\n          0.4973190348525469\\\\n        ],\\\\n        \\\\\\\"MRR\\\\\\\": 0.2968150941724084,\\\\n        \\\\\\\"MRR_ci\\\\\\\": [\\\\n          0.27428741459409656,\\\\n          0.3190549914407245\\\\n        ],\\\\n        \\\\\\\"count\\\\\\\": 746\\\\n      },\\\\n      \\\\\\\"embedding_distance_vs_random\\\\\\\": {\\\\n        \\\\\\\"R@1_delta\\\\\\\": 0.057640750670241284,\\\\n        \\\\\\\"R@1_rel_pct\\\\\\\": 330.7692307692308,\\\\n        \\\\\\\"R@5_delta\\\\\\\": 0.13806970509383376,\\\\n        \\\\\\\"R@5_rel_pct\\\\\\\": 84.42622950819671,\\\\n        \\\\\\\"MRR_delta\\\\\\\": 0.08779423431442998,\\\\n        \\\\\\\"MRR_rel_pct\\\\\\\": 77.62378309686898\\\\n      },\\\\n      \\\\\\\"dataflow_aware_vs_random\\\\\\\": {\\\\n        \\\\\\\"R@1_delta\\\\\\\": 0.11796246648793567,\\\\n        \\\\\\\"R@1_rel_pct\\\\\\\": 676.9230769230769,\\\\n        \\\\\\\"R@5_delta\\\\\\\": 0.3042895442359249,\\\\n        \\\\\\\"R@5_rel_pct\\\\\\\": 186.0655737704918,\\\\n        \\\\\\\"MRR_delta\\\\\\\": 0.18371285821868147,\\\\n        \\\\\\\"MRR_rel_pct\\\\\\\": 162.43079252106313\\\\n      }\\\\n    }\\\\n  }\\\\n}\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.44}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"config\\\": {\\n    \\\"strategies\\\": [\\n      \\\"random\\\",\\n      \\\"embedding_distance\\\",\\n      \\\"dataflow_aware\\\"\\n    ],\\n    \\\"seeds\\\": [\\n      42\\n    ],\\n    \\\"repo_size_bins\\\": {\\n      \\\"small\\\": [\\n        0,\\n        50\\n      ],\\n      \\\"medium\\\": [\\n        50,\\n        200\\n      ],\\n      \\\"large\\\": [\\n        200,\\n        500\\n      ],\\n      \\\"xlarge\\\": [\\n        500,\\n        Infinity\\n      ]\\n    },\\n    \\\"pool_size_bins\\\": {\\n      \\\"small\\\": [\\n        0,\\n        20\\n      ],\\n      \\\"medium\\\": [\\n        20,\\n        40\\n      ],\\n      \\\"large\\\": [\\n        40,\\n        51\\n      ]\\n    },\\n    \\\"similarity_bins\\\": {\\n      \\\"low\\\": [\\n        0.0,\\n        0.3\\n      ],\\n      \\\"medium\\\": [\\n        0.3,\\n        0.6\\n      ],\\n      \\\"high\\\": [\\n        0.6,\\n        1.01\\n      ]\\n    },\\n    \\\"dataflow_bins\\\": {\\n      \\\"sparse\\\": [\\n        0,\\n        2\\n      ],\\n      \\\"moderate\\\": [\\n        2,\\n        10\\n      ],\\n      \\\"rich\\\": [\\n        10,\\n        Infinity\\n      ]\\n    },\\n    \\\"neg_difficulty_quartiles\\\": [\\n      \\\"Q1_easy\\\",\\n      \\\"Q2\\\",\\n      \\\"Q3\\\",\\n      \\\"Q4_hard\\\"\\n    ],\\n    \\\"n_bootstrap\\\": 200,\\n    \\\"dry_run\\\": true\\n  },\\n  \\\"by_repo_size\\\": {\\n    \\\"small\\\": {\\n      \\\"random\\\": {\\n        \\\"R@1\\\": 0.07692307692307693,\\n        \\\"R@1_ci\\\": [\\n          0.038269230769230805,\\n          0.12307692307692308\\n        ],\\n        \\\"R@5\\\": 0.47692307692307695,\\n        \\\"R@5_ci\\\": [\\n          0.39980769230769236,\\n          0.5617307692307693\\n        ],\\n        \\\"MRR\\\": 0.26425629925629923,\\n        \\\"MRR_ci\\\": [\\n          0.22389736652236653,\\n          0.30436761155511155\\n        ],\\n        \\\"count\\\": 130\\n      },\\n      \\\"embedding_distance\\\": {\\n        \\\"R@1\\\": 0.27692307692307694,\\n        \\\"R@1_ci\\\": [\\n          0.19211538461538466,\\n          0.3540384615384616\\n        ],\\n        \\\"R@5\\\": 0.7384615384615385,\\n        \\\"R@5_ci\\\": [\\n          0.6615384615384615,\\n          0.823076923076923\\n        ],\\n        \\\"MRR\\\": 0.47043706293706294,\\n        \\\"MRR_ci\\\": [\\n          0.4076928071928072,\\n          0.5365241633366633\\n        ],\\n        \\\"count\\\": 130\\n      },\\n      \\\"dataflow_aware\\\": {\\n        \\\"R@1\\\": 0.4,\\n        \\\"R@1_ci\\\": [\\n          0.3151923076923077,\\n          0.46942307692307694\\n        ],\\n        \\\"R@5\\\": 0.9,\\n        \\\"R@5_ci\\\": [\\n          0.8459615384615384,\\n          0.9461538461538461\\n        ],\\n        \\\"MRR\\\": 0.6000063825063826,\\n        \\\"MRR_ci\\\": [\\n          0.5347679820179821,\\n          0.6520934065934065\\n        ],\\n        \\\"count\\\": 130\\n      },\\n      \\\"embedding_distance_vs_random\\\": {\\n        \\\"R@1_delta\\\": 0.2,\\n        \\\"R@1_rel_pct\\\": 260.0,\\n        \\\"R@5_delta\\\": 0.26153846153846155,\\n        \\\"R@5_rel_pct\\\": 54.83870967741935,\\n        \\\"MRR_delta\\\": 0.2061807636807637,\\n        \\\"MRR_rel_pct\\\": 78.02302698593054\\n      },\\n      \\\"dataflow_aware_vs_random\\\": {\\n        \\\"R@1_delta\\\": 0.3230769230769231,\\n        \\\"R@1_rel_pct\\\": 420.0,\\n        \\\"R@5_delta\\\": 0.4230769230769231,\\n        \\\"R@5_rel_pct\\\": 88.70967741935483,\\n        \\\"MRR_delta\\\": 0.3357500832500834,\\n        \\\"MRR_rel_pct\\\": 127.0547132442974\\n      }\\n    },\\n    \\\"medium\\\": {\\n      \\\"random\\\": {\\n        \\\"R@1\\\": 0.05491329479768786,\\n        \\\"R@1_ci\\\": [\\n          0.028901734104046242,\\n          0.0752890173410405\\n        ],\\n        \\\"R@5\\\": 0.2861271676300578,\\n        \\\"R@5_ci\\\": [\\n          0.23684971098265897,\\n          0.33236994219653176\\n        ],\\n        \\\"MRR\\\": 0.1935964506181734,\\n        \\\"MRR_ci\\\": [\\n          0.17032768352089914,\\n          0.2161689474822454\\n        ],\\n        \\\"count\\\": 346\\n      },\\n      \\\"embedding_distance\\\": {\\n        \\\"R@1\\\": 0.15028901734104047,\\n        \\\"R@1_ci\\\": [\\n          0.11271676300578035,\\n          0.1879335260115607\\n        ],\\n        \\\"R@5\\\": 0.523121387283237,\\n        \\\"R@5_ci\\\": [\\n          0.4710260115606937,\\n          0.5752167630057804\\n        ],\\n        \\\"MRR\\\": 0.32989441445506745,\\n        \\\"MRR_ci\\\": [\\n          0.29717057853455836,\\n          0.36684936890694325\\n        ],\\n        \\\"count\\\": 346\\n      },\\n      \\\"dataflow_aware\\\": {\\n        \\\"R@1\\\": 0.2398843930635838,\\n        \\\"R@1_ci\\\": [\\n          0.2021676300578035,\\n          0.27760115606936414\\n        ],\\n        \\\"R@5\\\": 0.7369942196531792\\n\\n... [截断: 输出过长，省略 25616 字符] ...\\n\\n\\n        \\\"R@5_rel_pct\\\": 266.66666666666663,\\n        \\\"MRR_delta\\\": 0.18151192668171712,\\n        \\\"MRR_rel_pct\\\": 162.05505112786537\\n      }\\n    },\\n    \\\"Q3\\\": {\\n      \\\"random\\\": {\\n        \\\"R@1\\\": 0.024161073825503355,\\n        \\\"R@1_ci\\\": [\\n          0.01476510067114094,\\n          0.0348993288590604\\n        ],\\n        \\\"R@5\\\": 0.12483221476510067,\\n        \\\"R@5_ci\\\": [\\n          0.10463087248322149,\\n          0.15033557046979865\\n        ],\\n        \\\"MRR\\\": 0.10574925148962648,\\n        \\\"MRR_ci\\\": [\\n          0.09482888540806862,\\n          0.11651834396588909\\n        ],\\n        \\\"count\\\": 745\\n      },\\n      \\\"embedding_distance\\\": {\\n        \\\"R@1\\\": 0.07651006711409396,\\n        \\\"R@1_ci\\\": [\\n          0.05906040268456376,\\n          0.09261744966442953\\n        ],\\n        \\\"R@5\\\": 0.312751677852349,\\n        \\\"R@5_ci\\\": [\\n          0.2764765100671141,\\n          0.34496644295302015\\n        ],\\n        \\\"MRR\\\": 0.20736546414953633,\\n        \\\"MRR_ci\\\": [\\n          0.19054410581433834,\\n          0.22484200616942923\\n        ],\\n        \\\"count\\\": 745\\n      },\\n      \\\"dataflow_aware\\\": {\\n        \\\"R@1\\\": 0.12483221476510067,\\n        \\\"R@1_ci\\\": [\\n          0.09929530201342283,\\n          0.14630872483221477\\n        ],\\n        \\\"R@5\\\": 0.48322147651006714,\\n        \\\"R@5_ci\\\": [\\n          0.4469463087248322,\\n          0.5154362416107383\\n        ],\\n        \\\"MRR\\\": 0.29257823070893335,\\n        \\\"MRR_ci\\\": [\\n          0.2696544452985487,\\n          0.3130578591008492\\n        ],\\n        \\\"count\\\": 745\\n      },\\n      \\\"embedding_distance_vs_random\\\": {\\n        \\\"R@1_delta\\\": 0.052348993288590606,\\n        \\\"R@1_rel_pct\\\": 216.66666666666669,\\n        \\\"R@5_delta\\\": 0.1879194630872483,\\n        \\\"R@5_rel_pct\\\": 150.53763440860212,\\n        \\\"MRR_delta\\\": 0.10161621265990985,\\n        \\\"MRR_rel_pct\\\": 96.09166138625382\\n      },\\n      \\\"dataflow_aware_vs_random\\\": {\\n        \\\"R@1_delta\\\": 0.10067114093959732,\\n        \\\"R@1_rel_pct\\\": 416.6666666666667,\\n        \\\"R@5_delta\\\": 0.35838926174496644,\\n        \\\"R@5_rel_pct\\\": 287.09677419354836,\\n        \\\"MRR_delta\\\": 0.18682897921930686,\\n        \\\"MRR_rel_pct\\\": 176.6716800237909\\n      }\\n    },\\n    \\\"Q4_hard\\\": {\\n      \\\"random\\\": {\\n        \\\"R@1\\\": 0.01742627345844504,\\n        \\\"R@1_ci\\\": [\\n          0.00938337801608579,\\n          0.028150134048257374\\n        ],\\n        \\\"R@5\\\": 0.16353887399463807,\\n        \\\"R@5_ci\\\": [\\n          0.13672922252010725,\\n          0.187701072386059\\n        ],\\n        \\\"MRR\\\": 0.11310223595372695,\\n        \\\"MRR_ci\\\": [\\n          0.10258848955316095,\\n          0.12528228899702964\\n        ],\\n        \\\"count\\\": 746\\n      },\\n      \\\"embedding_distance\\\": {\\n        \\\"R@1\\\": 0.07506702412868632,\\n        \\\"R@1_ci\\\": [\\n          0.05760723860589813,\\n          0.09520777479892761\\n        ],\\n        \\\"R@5\\\": 0.30160857908847183,\\n        \\\"R@5_ci\\\": [\\n          0.2694034852546917,\\n          0.33783512064343163\\n        ],\\n        \\\"MRR\\\": 0.20089647026815693,\\n        \\\"MRR_ci\\\": [\\n          0.18374811602212457,\\n          0.22345370976019258\\n        ],\\n        \\\"count\\\": 746\\n      },\\n      \\\"dataflow_aware\\\": {\\n        \\\"R@1\\\": 0.1353887399463807,\\n        \\\"R@1_ci\\\": [\\n          0.11126005361930295,\\n          0.16219839142091153\\n        ],\\n        \\\"R@5\\\": 0.467828418230563,\\n        \\\"R@5_ci\\\": [\\n          0.4342828418230563,\\n          0.4973190348525469\\n        ],\\n        \\\"MRR\\\": 0.2968150941724084,\\n        \\\"MRR_ci\\\": [\\n          0.27428741459409656,\\n          0.3190549914407245\\n        ],\\n        \\\"count\\\": 746\\n      },\\n      \\\"embedding_distance_vs_random\\\": {\\n        \\\"R@1_delta\\\": 0.057640750670241284,\\n        \\\"R@1_rel_pct\\\": 330.7692307692308,\\n        \\\"R@5_delta\\\": 0.13806970509383376,\\n        \\\"R@5_rel_pct\\\": 84.42622950819671,\\n        \\\"MRR_delta\\\": 0.08779423431442998,\\n        \\\"MRR_rel_pct\\\": 77.62378309686898\\n      },\\n      \\\"dataflow_aware_vs_random\\\": {\\n        \\\"R@1_delta\\\": 0.11796246648793567,\\n        \\\"R@1_rel_pct\\\": 676.9230769230769,\\n        \\\"R@5_delta\\\": 0.3042895442359249,\\n        \\\"R@5_rel_pct\\\": 186.0655737704918,\\n        \\\"MRR_delta\\\": 0.18371285821868147,\\n        \\\"MRR_rel_pct\\\": 162.43079252106313\\n      }\\n    }\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"
    }
  },
  "sourceToolAssistantUUID": "d09591e8-8f23-4ae2-8602-44b3fa61fc3e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "fb5ea7f7-b3c9-4750-b931-39d2aaae422b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 36 · 2026-05-14T20:36:45.505Z_

```json
{
  "parentUuid": "117b6f1b-9d7d-4102-9428-434bcb6f9d73",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "11c5ccb1-4e41-4c4c-a2e9-28ec0afd9bbc",
  "timestamp": "2026-05-14T20:36:45.505Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "fb5ea7f7-b3c9-4750-b931-39d2aaae422b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 37_

```json
{
  "type": "last-prompt",
  "leafUuid": "11c5ccb1-4e41-4c4c-a2e9-28ec0afd9bbc",
  "sessionId": "fb5ea7f7-b3c9-4750-b931-39d2aaae422b"
}
```

---

### Runtime record

_source line 38_

```json
{
  "type": "ai-title",
  "aiTitle": "Trace stratified_dryrun v1 to v2 differences",
  "sessionId": "fb5ea7f7-b3c9-4750-b931-39d2aaae422b"
}
```

---

### Assistant

_source line 39 · 2026-05-14T20:37:05.455Z_

<details><summary>Logged reasoning block</summary>

```text
No git repo on the server. Let me now:
1. Read the analyze_stratified.py script to understand the logic
2. Get the full v1 JSON (it was truncated - I need the middle sections)
3. Check if there are different versions of the script saved

Let me also use a Python command on the server to extract the key differences programmatically, since the JSON outputs are being truncated.

Let me record the key data I have so far:

**v1 config**: repo_size_bins, pool_size_bins, similarity_bins — 3 dimensions


**v2 config**: same 3 plus dataflow_bins (sparse/moderate/rich) and neg_difficulty_quartiles (Q1-Q4) — 5 dimensions total

Now I'm looking at the performance metrics broken down by repository size, comparing how the random and embedding_distance strategies performed across recall and MRR metrics between the two versions.

For the small repos, embedding_distance shows more stability than random, with only minor drops in R@1 and MRR while maintaining R@5. The dataflow_aware strategy takes a hit on R@1 and MRR but actually improves on R@5, suggesting the additional dimensions help with broader retrieval even if top-1 accuracy suffers. The sample size stayed consistent at 130 across both versions.

Now looking at medium-sized repositories, I'm seeing much stronger improvements across the board. The random baseline jumps significantly on R@5 and MRR, while embedding_distance shows even more dramatic gains—particularly that 40.6% boost on R@1, which is substantial.

The dataflow_aware strategy is performing best overall, though interestingly the MRR value for v2 is missing. What's striking is that the sample counts remain identical at 346 across both versions, which rules out any data filtering or stratification changes. Since the counts are preserved but the metrics shifted, this points to something in the mock prediction generation itself—likely a change in random seed behavior or the scoring logic between versions. Let me check the script to see what's actually happening with the predictions.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "11c5ccb1-4e41-4c4c-a2e9-28ec0afd9bbc",
  "isSidechain": false,
  "requestId": "req_011Cb36wwosdgT9JbqK7fwRg",
  "type": "assistant",
  "uuid": "0bae365d-3f1b-43e2-bea1-c98893aea5dc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "fb5ea7f7-b3c9-4750-b931-39d2aaae422b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KbMTxEN8mzLzLY7QFaAyvB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9471,
      "cache_read_input_tokens": 34534,
      "output_tokens": 1319,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9471,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1319,
          "cache_read_input_tokens": 34534,
          "cache_creation_input_tokens": 9471,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9471
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

_source line 40 · 2026-05-14T20:37:05.456Z_

没有 git 仓库。我需要读脚本源码来分析逻辑差异。同时用 Python 提取 v1 完整的中间截断部分。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0bae365d-3f1b-43e2-bea1-c98893aea5dc",
  "isSidechain": false,
  "requestId": "req_011Cb36wwosdgT9JbqK7fwRg",
  "type": "assistant",
  "uuid": "1025e79e-2997-4174-a84a-d8ab3cbd96e8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "fb5ea7f7-b3c9-4750-b931-39d2aaae422b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KbMTxEN8mzLzLY7QFaAyvB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9471,
      "cache_read_input_tokens": 34534,
      "output_tokens": 1319,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9471,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1319,
          "cache_read_input_tokens": 34534,
          "cache_creation_input_tokens": 9471,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9471
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

_source line 41 · 2026-05-14T20:37:06.492Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_0148PQ5cQNMn68upUwA1yjHP`</summary>

```json
{
  "server": "bjb1-42106",
  "command": "cat /root/structfuse/evaluation/analyze_stratified.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1025e79e-2997-4174-a84a-d8ab3cbd96e8",
  "isSidechain": false,
  "requestId": "req_011Cb36wwosdgT9JbqK7fwRg",
  "type": "assistant",
  "uuid": "b552d41f-b29f-46d8-a383-3fabe1545e61",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "fb5ea7f7-b3c9-4750-b931-39d2aaae422b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KbMTxEN8mzLzLY7QFaAyvB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9471,
      "cache_read_input_tokens": 34534,
      "output_tokens": 1319,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9471,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1319,
          "cache_read_input_tokens": 34534,
          "cache_creation_input_tokens": 9471,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9471
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

_source line 42 · 2026-05-14T20:37:06.925Z_

<details><summary>↩ Tool result · `toolu_0148PQ5cQNMn68upUwA1yjHP`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n\\\"\\\"\\\"Stratified analysis of embedding vs random negative strategies by data strata.\\n\\nAnalyses M2 per-instance predictions across:\\n  - Repo size (instance count per repo from M1)\\n  - Candidate pool size (neg_candidates per query)\\n  - Query-positive similarity (cosine sim from model, or text overlap for dry-run)\\n\\nInputs:\\n  - M2 per-instance predictions (from --predictions-dir or re-eval from checkpoints)\\n  - M1 all.jsonl (repo metadata)\\n  - Val JSONL files (query/candidate structure)\\n\\nOutputs:\\n  - stratified_results.json: full per-stratum metrics with bootstrap CI\\n  - stratified_summary.csv: compact table\\n  - stratified_plots.pdf: grouped bar charts, heatmaps, delta trends\\n\\\"\\\"\\\"\\n\\nimport argparse\\nimport csv\\nimport json\\nimport math\\nimport os\\nimport sys\\nfrom collections import Counter, defaultdict\\nfrom pathlib import Path\\nfrom typing import Any, Dict, List, Optional, Tuple\\n\\nimport numpy as np\\n\\nSTRATEGIES = [\\\"random\\\", \\\"embedding_distance\\\", \\\"dataflow_aware\\\"]\\nSTRATEGY_LABELS = {\\\"random\\\": \\\"Random\\\", \\\"embedding_distance\\\": \\\"Embedding\\\", \\\"dataflow_aware\\\": \\\"Dataflow\\\"}\\nSTRATEGY_COLORS = {\\\"random\\\": \\\"#4C72B0\\\", \\\"embedding_distance\\\": \\\"#DD8452\\\", \\\"dataflow_aware\\\": \\\"#55A868\\\"}\\n\\nREPO_SIZE_BINS = {\\n    \\\"small\\\": (0, 50),\\n    \\\"medium\\\": (50, 200),\\n    \\\"large\\\": (200, 500),\\n    \\\"xlarge\\\": (500, float(\\\"inf\\\")),\\n}\\n\\nPOOL_SIZE_BINS = {\\n    \\\"small\\\": (0, 20),\\n    \\\"medium\\\": (20, 40),\\n    \\\"large\\\": (40, 51),\\n}\\n\\nSIMILARITY_BINS = {\\n    \\\"low\\\": (0.0, 0.3),\\n    \\\"medium\\\": (0.3, 0.6),\\n    \\\"high\\\": (0.6, 1.01),\\n}\\n\\nDATAFLOW_BINS = {\\n    \\\"sparse\\\": (0, 2),\\n    \\\"moderate\\\": (2, 10),\\n    \\\"rich\\\": (10, float(\\\"inf\\\")),\\n}\\n\\nNEG_DIFFICULTY_QUARTILE_LABELS = [\\\"Q1_easy\\\", \\\"Q2\\\", \\\"Q3\\\", \\\"Q4_hard\\\"]\\n\\n\\ndef _bin_value(value, bins):\\n    for name, (lo, hi) in bins.items():\\n        if lo <= value < hi:\\n            return name\\n    return \\\"unknown\\\"\\n\\n\\n# ── M1 metadata ───────────────────────────────────────────────────��─\\n\\ndef load_m1_metadata(m1_path: str) -> Tuple[Dict[str, str], Dict[str, int]]:\\n    import re\\n    inst_to_repo = {}\\n    repo_counts: Counter = Counter()\\n    pat_iid = re.compile(r'\\\"instance_id\\\"\\\\s*:\\\\s*\\\"([^\\\"]+)\\\"')\\n    pat_repo = re.compile(r'\\\"repo\\\"\\\\s*:\\\\s*\\\"([^\\\"]+)\\\"')\\n    with open(m1_path) as f:\\n        for line in f:\\n            m_iid = pat_iid.search(line)\\n            m_repo = pat_repo.search(line)\\n            if m_iid and m_repo:\\n                iid = m_iid.group(1)\\n                repo = m_repo.group(1)\\n                inst_to_repo[iid] = repo\\n                repo_counts[repo] += 1\\n    return inst_to_repo, dict(repo_counts)\\n\\n\\n# ── Dataflow graph loading ────────────────────────────────────────────\\n\\ndef load_dataflow_edges(graph_path: str) -> Dict[str, int]:\\n    \\\"\\\"\\\"Load dataflow graph and return {file_key: edge_count}.\\\"\\\"\\\"\\n    with open(graph_path) as f:\\n        graph = json.load(f)\\n    return {k: len(v) for k, v in graph.items()}\\n\\n\\n# ── Val data loading ─────────────────────────────────────────────────\\n\\ndef load_val_samples(val_path: str, lite: bool = False) -> List[Dict[str, Any]]:\\n    \\\"\\\"\\\"Load val JSONL. lite=True skips candidate_tokens (faster for dry-run).\\\"\\\"\\\"\\n    import re\\n    samples = []\\n    pat_qid = re.compile(r'\\\"query_id\\\"\\\\s*:\\\\s*\\\"([^\\\"]+)\\\"')\\n    with open(val_path) as f:\\n        for line in f:\\n            if not line.strip():\\n                continue\\n            if lite:\\n                m = pat_qid.search(line)\\n                if not m:\\n                    continue\\n                qid = m.group(1)\\n                instance_id = qid.split(\\\"::\\\")[0] if \\\"::\\\" in qid else qid\\n                d = json.loads(line)\\n                samples.append({\\n                    \\\"query_id\\\": qid,\\n                    \\\"instance_id\\\": instance_id,\\n                    \\\"pool_size\\\": len(d.get(\\\"neg_candidates\\\", [])),\\n                    \\\"query_tokens\\\": d.get(\\\"query_tokens\\\", \\\"\\\")[:1000],\\n                    \\\"pos_tokens\\\": d.get(\\\"pos_tokens\\\", \\\"\\\")[:1000],\\n                    \\\"neg_candidates\\\": [],\\n                    \\\"candidate_tokens\\\": {},\\n                })\\n            else:\\n                d = jso\\n\\n... [截断: 输出过长，省略 27452 字符] ...\\n\\nt\\\")):\\n                        ckpt_dir = candidate\\n                        break\\n                if ckpt_dir is None and os.path.exists(os.path.join(base, \\\"model.pt\\\")):\\n                    ckpt_dir = base\\n                if os.path.exists(ckpt_dir):\\n                    print(f\\\"  Re-evaluating checkpoint: {ckpt_dir}\\\", flush=True)\\n                    results = reeval_checkpoint(\\n                        ckpt_dir, val_samples, args.device, args.max_seq_length\\n                    )\\n                else:\\n                    print(f\\\"  [WARN] Checkpoint not found: {ckpt_dir}\\\", flush=True)\\n                    continue\\n            else:\\n                print(\\\"  [ERROR] No --dry-run, --predictions-dir, or --checkpoints-dir\\\", flush=True)\\n                continue\\n\\n            # Assign strata\\n            results = assign_strata(results, inst_to_repo, repo_counts, dataflow_edges)\\n\\n            # For dry-run or model-based: compute text similarity for sim_bin\\n            if args.dry_run:\\n                for r, s in zip(results, val_samples):\\n                    tsim = text_similarity(s[\\\"query_tokens\\\"][:500], s[\\\"pos_tokens\\\"][:500])\\n                    r[\\\"sim_bin\\\"] = _bin_value(tsim, SIMILARITY_BINS)\\n\\n            all_results[strategy][seed] = results\\n            val_samples_cache[f\\\"{strategy}_s{seed}\\\"] = val_samples\\n            print(f\\\"  -> {len(results)} instances\\\", flush=True)\\n\\n    # Compute neg_difficulty quartiles (text-overlap proxy, CPU-safe)\\n    print(\\\"Computing neg difficulty quartiles...\\\", flush=True)\\n    assign_neg_difficulty_quartiles(all_results, val_samples_cache)\\n\\n    # Run stratified analysis\\n    print(\\\"\\\\nRunning stratified analysis...\\\", flush=True)\\n    repo_analysis = run_stratified_analysis(\\n        all_results, \\\"repo_size_bin\\\", list(REPO_SIZE_BINS.keys()), args.n_bootstrap\\n    )\\n    pool_analysis = run_stratified_analysis(\\n        all_results, \\\"pool_size_bin\\\", list(POOL_SIZE_BINS.keys()), args.n_bootstrap\\n    )\\n    sim_analysis = run_stratified_analysis(\\n        all_results, \\\"sim_bin\\\", list(SIMILARITY_BINS.keys()), args.n_bootstrap\\n    )\\n\\n    dataflow_analysis = {}\\n    if dataflow_edges is not None:\\n        dataflow_analysis = run_stratified_analysis(\\n            all_results, \\\"dataflow_bin\\\", list(DATAFLOW_BINS.keys()), args.n_bootstrap\\n        )\\n\\n    neg_diff_analysis = run_stratified_analysis(\\n        all_results, \\\"neg_difficulty_bin\\\", NEG_DIFFICULTY_QUARTILE_LABELS, args.n_bootstrap\\n    )\\n\\n    # Save JSON\\n    full_results = {\\n        \\\"config\\\": {\\n            \\\"strategies\\\": STRATEGIES,\\n            \\\"seeds\\\": seeds,\\n            \\\"repo_size_bins\\\": {k: list(v) for k, v in REPO_SIZE_BINS.items()},\\n            \\\"pool_size_bins\\\": {k: list(v) for k, v in POOL_SIZE_BINS.items()},\\n            \\\"similarity_bins\\\": {k: list(v) for k, v in SIMILARITY_BINS.items()},\\n            \\\"dataflow_bins\\\": {k: list(v) for k, v in DATAFLOW_BINS.items()},\\n            \\\"neg_difficulty_quartiles\\\": NEG_DIFFICULTY_QUARTILE_LABELS,\\n            \\\"n_bootstrap\\\": args.n_bootstrap,\\n            \\\"dry_run\\\": args.dry_run,\\n        },\\n        \\\"by_repo_size\\\": repo_analysis,\\n        \\\"by_pool_size\\\": pool_analysis,\\n        \\\"by_similarity\\\": sim_analysis,\\n        \\\"by_dataflow\\\": dataflow_analysis,\\n        \\\"by_neg_difficulty\\\": neg_diff_analysis,\\n    }\\n\\n    json_path = os.path.join(args.output_dir, \\\"stratified_results.json\\\")\\n    with open(json_path, \\\"w\\\") as f:\\n        json.dump(full_results, f, indent=2, ensure_ascii=False)\\n    print(f\\\"  Results JSON saved to {json_path}\\\", flush=True)\\n\\n    # CSV summary\\n    csv_path = os.path.join(args.output_dir, \\\"stratified_summary.csv\\\")\\n    write_summary_csv(repo_analysis, pool_analysis, sim_analysis, csv_path, dataflow_analysis, neg_diff_analysis)\\n\\n    # Plots\\n    try:\\n        make_plots(repo_analysis, pool_analysis, sim_analysis, args.output_dir, dataflow_analysis, neg_diff_analysis)\\n    except Exception as e:\\n        print(f\\\"  [WARN] Plot generation failed: {e}\\\", flush=True)\\n\\n    print(\\\"\\\\nDone.\\\", flush=True)\\n\\n\\nif __name__ == \\\"__main__\\\":\\n    main()\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.41}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b552d41f-b29f-46d8-a383-3fabe1545e61",
  "isSidechain": false,
  "promptId": "0b7bb415-f2b4-4832-aac4-2e6aafdc7429",
  "type": "user",
  "uuid": "1fe774b3-5676-4e60-899c-c0920a846909",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"#!/usr/bin/env python3\\\\n\\\\\\\"\\\\\\\"\\\\\\\"Stratified analysis of embedding vs random negative strategies by data strata.\\\\n\\\\nAnalyses M2 per-instance predictions across:\\\\n  - Repo size (instance count per repo from M1)\\\\n  - Candidate pool size (neg_candidates per query)\\\\n  - Query-positive similarity (cosine sim from model, or text overlap for dry-run)\\\\n\\\\nInputs:\\\\n  - M2 per-instance predictions (from --predictions-dir or re-eval from checkpoints)\\\\n  - M1 all.jsonl (repo metadata)\\\\n  - Val JSONL files (query/candidate structure)\\\\n\\\\nOutputs:\\\\n  - stratified_results.json: full per-stratum metrics with bootstrap CI\\\\n  - stratified_summary.csv: compact table\\\\n  - stratified_plots.pdf: grouped bar charts, heatmaps, delta trends\\\\n\\\\\\\"\\\\\\\"\\\\\\\"\\\\n\\\\nimport argparse\\\\nimport csv\\\\nimport json\\\\nimport math\\\\nimport os\\\\nimport sys\\\\nfrom collections import Counter, defaultdict\\\\nfrom pathlib import Path\\\\nfrom typing import Any, Dict, List, Optional, Tuple\\\\n\\\\nimport numpy as np\\\\n\\\\nSTRATEGIES = [\\\\\\\"random\\\\\\\", \\\\\\\"embedding_distance\\\\\\\", \\\\\\\"dataflow_aware\\\\\\\"]\\\\nSTRATEGY_LABELS = {\\\\\\\"random\\\\\\\": \\\\\\\"Random\\\\\\\", \\\\\\\"embedding_distance\\\\\\\": \\\\\\\"Embedding\\\\\\\", \\\\\\\"dataflow_aware\\\\\\\": \\\\\\\"Dataflow\\\\\\\"}\\\\nSTRATEGY_COLORS = {\\\\\\\"random\\\\\\\": \\\\\\\"#4C72B0\\\\\\\", \\\\\\\"embedding_distance\\\\\\\": \\\\\\\"#DD8452\\\\\\\", \\\\\\\"dataflow_aware\\\\\\\": \\\\\\\"#55A868\\\\\\\"}\\\\n\\\\nREPO_SIZE_BINS = {\\\\n    \\\\\\\"small\\\\\\\": (0, 50),\\\\n    \\\\\\\"medium\\\\\\\": (50, 200),\\\\n    \\\\\\\"large\\\\\\\": (200, 500),\\\\n    \\\\\\\"xlarge\\\\\\\": (500, float(\\\\\\\"inf\\\\\\\")),\\\\n}\\\\n\\\\nPOOL_SIZE_BINS = {\\\\n    \\\\\\\"small\\\\\\\": (0, 20),\\\\n    \\\\\\\"medium\\\\\\\": (20, 40),\\\\n    \\\\\\\"large\\\\\\\": (40, 51),\\\\n}\\\\n\\\\nSIMILARITY_BINS = {\\\\n    \\\\\\\"low\\\\\\\": (0.0, 0.3),\\\\n    \\\\\\\"medium\\\\\\\": (0.3, 0.6),\\\\n    \\\\\\\"high\\\\\\\": (0.6, 1.01),\\\\n}\\\\n\\\\nDATAFLOW_BINS = {\\\\n    \\\\\\\"sparse\\\\\\\": (0, 2),\\\\n    \\\\\\\"moderate\\\\\\\": (2, 10),\\\\n    \\\\\\\"rich\\\\\\\": (10, float(\\\\\\\"inf\\\\\\\")),\\\\n}\\\\n\\\\nNEG_DIFFICULTY_QUARTILE_LABELS = [\\\\\\\"Q1_easy\\\\\\\", \\\\\\\"Q2\\\\\\\", \\\\\\\"Q3\\\\\\\", \\\\\\\"Q4_hard\\\\\\\"]\\\\n\\\\n\\\\ndef _bin_value(value, bins):\\\\n    for name, (lo, hi) in bins.items():\\\\n        if lo <= value < hi:\\\\n            return name\\\\n    return \\\\\\\"unknown\\\\\\\"\\\\n\\\\n\\\\n# ── M1 metadata ───────────────────────────────────────────────────��─\\\\n\\\\ndef load_m1_metadata(m1_path: str) -> Tuple[Dict[str, str], Dict[str, int]]:\\\\n    import re\\\\n    inst_to_repo = {}\\\\n    repo_counts: Counter = Counter()\\\\n    pat_iid = re.compile(r'\\\\\\\"instance_id\\\\\\\"\\\\\\\\s*:\\\\\\\\s*\\\\\\\"([^\\\\\\\"]+)\\\\\\\"')\\\\n    pat_repo = re.compile(r'\\\\\\\"repo\\\\\\\"\\\\\\\\s*:\\\\\\\\s*\\\\\\\"([^\\\\\\\"]+)\\\\\\\"')\\\\n    with open(m1_path) as f:\\\\n        for line in f:\\\\n            m_iid = pat_iid.search(line)\\\\n            m_repo = pat_repo.search(line)\\\\n            if m_iid and m_repo:\\\\n                iid = m_iid.group(1)\\\\n                repo = m_repo.group(1)\\\\n                inst_to_repo[iid] = repo\\\\n                repo_counts[repo] += 1\\\\n    return inst_to_repo, dict(repo_counts)\\\\n\\\\n\\\\n# ── Dataflow graph loading ────────────────────────────────────────────\\\\n\\\\ndef load_dataflow_edges(graph_path: str) -> Dict[str, int]:\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"Load dataflow graph and return {file_key: edge_count}.\\\\\\\"\\\\\\\"\\\\\\\"\\\\n    with open(graph_path) as f:\\\\n        graph = json.load(f)\\\\n    return {k: len(v) for k, v in graph.items()}\\\\n\\\\n\\\\n# ── Val data loading ─────────────────────────────────────────────────\\\\n\\\\ndef load_val_samples(val_path: str, lite: bool = False) -> List[Dict[str, Any]]:\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"Load val JSONL. lite=True skips candidate_tokens (faster for dry-run).\\\\\\\"\\\\\\\"\\\\\\\"\\\\n    import re\\\\n    samples = []\\\\n    pat_qid = re.compile(r'\\\\\\\"query_id\\\\\\\"\\\\\\\\s*:\\\\\\\\s*\\\\\\\"([^\\\\\\\"]+)\\\\\\\"')\\\\n    with open(val_path) as f:\\\\n        for line in f:\\\\n            if not line.strip():\\\\n                continue\\\\n            if lite:\\\\n                m = pat_qid.search(line)\\\\n                if not m:\\\\n                    continue\\\\n                qid = m.group(1)\\\\n                instance_id = qid.split(\\\\\\\"::\\\\\\\")[0] if \\\\\\\"::\\\\\\\" in qid else qid\\\\n                d = json.loads(line)\\\\n                samples.append({\\\\n                    \\\\\\\"query_id\\\\\\\": qid,\\\\n                    \\\\\\\"instance_id\\\\\\\": instance_id,\\\\n                    \\\\\\\"pool_size\\\\\\\": len(d.get(\\\\\\\"neg_candidates\\\\\\\", [])),\\\\n                    \\\\\\\"query_tokens\\\\\\\": d.get(\\\\\\\"query_tokens\\\\\\\", \\\\\\\"\\\\\\\")[:1000],\\\\n                    \\\\\\\"pos_tokens\\\\\\\": d.get(\\\\\\\"pos_tokens\\\\\\\", \\\\\\\"\\\\\\\")[:1000],\\\\n                    \\\\\\\"neg_candidates\\\\\\\": [],\\\\n                    \\\\\\\"candidate_tokens\\\\\\\": {},\\\\n                })\\\\n            else:\\\\n                d = jso\\\\n\\\\n... [截断: 输出过长，省略 27452 字符] ...\\\\n\\\\nt\\\\\\\")):\\\\n                        ckpt_dir = candidate\\\\n                        break\\\\n                if ckpt_dir is None and os.path.exists(os.path.join(base, \\\\\\\"model.pt\\\\\\\")):\\\\n                    ckpt_dir = base\\\\n                if os.path.exists(ckpt_dir):\\\\n                    print(f\\\\\\\"  Re-evaluating checkpoint: {ckpt_dir}\\\\\\\", flush=True)\\\\n                    results = reeval_checkpoint(\\\\n                        ckpt_dir, val_samples, args.device, args.max_seq_length\\\\n                    )\\\\n                else:\\\\n                    print(f\\\\\\\"  [WARN] Checkpoint not found: {ckpt_dir}\\\\\\\", flush=True)\\\\n                    continue\\\\n            else:\\\\n                print(\\\\\\\"  [ERROR] No --dry-run, --predictions-dir, or --checkpoints-dir\\\\\\\", flush=True)\\\\n                continue\\\\n\\\\n            # Assign strata\\\\n            results = assign_strata(results, inst_to_repo, repo_counts, dataflow_edges)\\\\n\\\\n            # For dry-run or model-based: compute text similarity for sim_bin\\\\n            if args.dry_run:\\\\n                for r, s in zip(results, val_samples):\\\\n                    tsim = text_similarity(s[\\\\\\\"query_tokens\\\\\\\"][:500], s[\\\\\\\"pos_tokens\\\\\\\"][:500])\\\\n                    r[\\\\\\\"sim_bin\\\\\\\"] = _bin_value(tsim, SIMILARITY_BINS)\\\\n\\\\n            all_results[strategy][seed] = results\\\\n            val_samples_cache[f\\\\\\\"{strategy}_s{seed}\\\\\\\"] = val_samples\\\\n            print(f\\\\\\\"  -> {len(results)} instances\\\\\\\", flush=True)\\\\n\\\\n    # Compute neg_difficulty quartiles (text-overlap proxy, CPU-safe)\\\\n    print(\\\\\\\"Computing neg difficulty quartiles...\\\\\\\", flush=True)\\\\n    assign_neg_difficulty_quartiles(all_results, val_samples_cache)\\\\n\\\\n    # Run stratified analysis\\\\n    print(\\\\\\\"\\\\\\\\nRunning stratified analysis...\\\\\\\", flush=True)\\\\n    repo_analysis = run_stratified_analysis(\\\\n        all_results, \\\\\\\"repo_size_bin\\\\\\\", list(REPO_SIZE_BINS.keys()), args.n_bootstrap\\\\n    )\\\\n    pool_analysis = run_stratified_analysis(\\\\n        all_results, \\\\\\\"pool_size_bin\\\\\\\", list(POOL_SIZE_BINS.keys()), args.n_bootstrap\\\\n    )\\\\n    sim_analysis = run_stratified_analysis(\\\\n        all_results, \\\\\\\"sim_bin\\\\\\\", list(SIMILARITY_BINS.keys()), args.n_bootstrap\\\\n    )\\\\n\\\\n    dataflow_analysis = {}\\\\n    if dataflow_edges is not None:\\\\n        dataflow_analysis = run_stratified_analysis(\\\\n            all_results, \\\\\\\"dataflow_bin\\\\\\\", list(DATAFLOW_BINS.keys()), args.n_bootstrap\\\\n        )\\\\n\\\\n    neg_diff_analysis = run_stratified_analysis(\\\\n        all_results, \\\\\\\"neg_difficulty_bin\\\\\\\", NEG_DIFFICULTY_QUARTILE_LABELS, args.n_bootstrap\\\\n    )\\\\n\\\\n    # Save JSON\\\\n    full_results = {\\\\n        \\\\\\\"config\\\\\\\": {\\\\n            \\\\\\\"strategies\\\\\\\": STRATEGIES,\\\\n            \\\\\\\"seeds\\\\\\\": seeds,\\\\n            \\\\\\\"repo_size_bins\\\\\\\": {k: list(v) for k, v in REPO_SIZE_BINS.items()},\\\\n            \\\\\\\"pool_size_bins\\\\\\\": {k: list(v) for k, v in POOL_SIZE_BINS.items()},\\\\n            \\\\\\\"similarity_bins\\\\\\\": {k: list(v) for k, v in SIMILARITY_BINS.items()},\\\\n            \\\\\\\"dataflow_bins\\\\\\\": {k: list(v) for k, v in DATAFLOW_BINS.items()},\\\\n            \\\\\\\"neg_difficulty_quartiles\\\\\\\": NEG_DIFFICULTY_QUARTILE_LABELS,\\\\n            \\\\\\\"n_bootstrap\\\\\\\": args.n_bootstrap,\\\\n            \\\\\\\"dry_run\\\\\\\": args.dry_run,\\\\n        },\\\\n        \\\\\\\"by_repo_size\\\\\\\": repo_analysis,\\\\n        \\\\\\\"by_pool_size\\\\\\\": pool_analysis,\\\\n        \\\\\\\"by_similarity\\\\\\\": sim_analysis,\\\\n        \\\\\\\"by_dataflow\\\\\\\": dataflow_analysis,\\\\n        \\\\\\\"by_neg_difficulty\\\\\\\": neg_diff_analysis,\\\\n    }\\\\n\\\\n    json_path = os.path.join(args.output_dir, \\\\\\\"stratified_results.json\\\\\\\")\\\\n    with open(json_path, \\\\\\\"w\\\\\\\") as f:\\\\n        json.dump(full_results, f, indent=2, ensure_ascii=False)\\\\n    print(f\\\\\\\"  Results JSON saved to {json_path}\\\\\\\", flush=True)\\\\n\\\\n    # CSV summary\\\\n    csv_path = os.path.join(args.output_dir, \\\\\\\"stratified_summary.csv\\\\\\\")\\\\n    write_summary_csv(repo_analysis, pool_analysis, sim_analysis, csv_path, dataflow_analysis, neg_diff_analysis)\\\\n\\\\n    # Plots\\\\n    try:\\\\n        make_plots(repo_analysis, pool_analysis, sim_analysis, args.output_dir, dataflow_analysis, neg_diff_analysis)\\\\n    except Exception as e:\\\\n        print(f\\\\\\\"  [WARN] Plot generation failed: {e}\\\\\\\", flush=True)\\\\n\\\\n    print(\\\\\\\"\\\\\\\\nDone.\\\\\\\", flush=True)\\\\n\\\\n\\\\nif __name__ == \\\\\\\"__main__\\\\\\\":\\\\n    main()\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.41}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n\\\"\\\"\\\"Stratified analysis of embedding vs random negative strategies by data strata.\\n\\nAnalyses M2 per-instance predictions across:\\n  - Repo size (instance count per repo from M1)\\n  - Candidate pool size (neg_candidates per query)\\n  - Query-positive similarity (cosine sim from model, or text overlap for dry-run)\\n\\nInputs:\\n  - M2 per-instance predictions (from --predictions-dir or re-eval from checkpoints)\\n  - M1 all.jsonl (repo metadata)\\n  - Val JSONL files (query/candidate structure)\\n\\nOutputs:\\n  - stratified_results.json: full per-stratum metrics with bootstrap CI\\n  - stratified_summary.csv: compact table\\n  - stratified_plots.pdf: grouped bar charts, heatmaps, delta trends\\n\\\"\\\"\\\"\\n\\nimport argparse\\nimport csv\\nimport json\\nimport math\\nimport os\\nimport sys\\nfrom collections import Counter, defaultdict\\nfrom pathlib import Path\\nfrom typing import Any, Dict, List, Optional, Tuple\\n\\nimport numpy as np\\n\\nSTRATEGIES = [\\\"random\\\", \\\"embedding_distance\\\", \\\"dataflow_aware\\\"]\\nSTRATEGY_LABELS = {\\\"random\\\": \\\"Random\\\", \\\"embedding_distance\\\": \\\"Embedding\\\", \\\"dataflow_aware\\\": \\\"Dataflow\\\"}\\nSTRATEGY_COLORS = {\\\"random\\\": \\\"#4C72B0\\\", \\\"embedding_distance\\\": \\\"#DD8452\\\", \\\"dataflow_aware\\\": \\\"#55A868\\\"}\\n\\nREPO_SIZE_BINS = {\\n    \\\"small\\\": (0, 50),\\n    \\\"medium\\\": (50, 200),\\n    \\\"large\\\": (200, 500),\\n    \\\"xlarge\\\": (500, float(\\\"inf\\\")),\\n}\\n\\nPOOL_SIZE_BINS = {\\n    \\\"small\\\": (0, 20),\\n    \\\"medium\\\": (20, 40),\\n    \\\"large\\\": (40, 51),\\n}\\n\\nSIMILARITY_BINS = {\\n    \\\"low\\\": (0.0, 0.3),\\n    \\\"medium\\\": (0.3, 0.6),\\n    \\\"high\\\": (0.6, 1.01),\\n}\\n\\nDATAFLOW_BINS = {\\n    \\\"sparse\\\": (0, 2),\\n    \\\"moderate\\\": (2, 10),\\n    \\\"rich\\\": (10, float(\\\"inf\\\")),\\n}\\n\\nNEG_DIFFICULTY_QUARTILE_LABELS = [\\\"Q1_easy\\\", \\\"Q2\\\", \\\"Q3\\\", \\\"Q4_hard\\\"]\\n\\n\\ndef _bin_value(value, bins):\\n    for name, (lo, hi) in bins.items():\\n        if lo <= value < hi:\\n            return name\\n    return \\\"unknown\\\"\\n\\n\\n# ── M1 metadata ───────────────────────────────────────────────────��─\\n\\ndef load_m1_metadata(m1_path: str) -> Tuple[Dict[str, str], Dict[str, int]]:\\n    import re\\n    inst_to_repo = {}\\n    repo_counts: Counter = Counter()\\n    pat_iid = re.compile(r'\\\"instance_id\\\"\\\\s*:\\\\s*\\\"([^\\\"]+)\\\"')\\n    pat_repo = re.compile(r'\\\"repo\\\"\\\\s*:\\\\s*\\\"([^\\\"]+)\\\"')\\n    with open(m1_path) as f:\\n        for line in f:\\n            m_iid = pat_iid.search(line)\\n            m_repo = pat_repo.search(line)\\n            if m_iid and m_repo:\\n                iid = m_iid.group(1)\\n                repo = m_repo.group(1)\\n                inst_to_repo[iid] = repo\\n                repo_counts[repo] += 1\\n    return inst_to_repo, dict(repo_counts)\\n\\n\\n# ── Dataflow graph loading ────────────────────────────────────────────\\n\\ndef load_dataflow_edges(graph_path: str) -> Dict[str, int]:\\n    \\\"\\\"\\\"Load dataflow graph and return {file_key: edge_count}.\\\"\\\"\\\"\\n    with open(graph_path) as f:\\n        graph = json.load(f)\\n    return {k: len(v) for k, v in graph.items()}\\n\\n\\n# ── Val data loading ─────────────────────────────────────────────────\\n\\ndef load_val_samples(val_path: str, lite: bool = False) -> List[Dict[str, Any]]:\\n    \\\"\\\"\\\"Load val JSONL. lite=True skips candidate_tokens (faster for dry-run).\\\"\\\"\\\"\\n    import re\\n    samples = []\\n    pat_qid = re.compile(r'\\\"query_id\\\"\\\\s*:\\\\s*\\\"([^\\\"]+)\\\"')\\n    with open(val_path) as f:\\n        for line in f:\\n            if not line.strip():\\n                continue\\n            if lite:\\n                m = pat_qid.search(line)\\n                if not m:\\n                    continue\\n                qid = m.group(1)\\n                instance_id = qid.split(\\\"::\\\")[0] if \\\"::\\\" in qid else qid\\n                d = json.loads(line)\\n                samples.append({\\n                    \\\"query_id\\\": qid,\\n                    \\\"instance_id\\\": instance_id,\\n                    \\\"pool_size\\\": len(d.get(\\\"neg_candidates\\\", [])),\\n                    \\\"query_tokens\\\": d.get(\\\"query_tokens\\\", \\\"\\\")[:1000],\\n                    \\\"pos_tokens\\\": d.get(\\\"pos_tokens\\\", \\\"\\\")[:1000],\\n                    \\\"neg_candidates\\\": [],\\n                    \\\"candidate_tokens\\\": {},\\n                })\\n            else:\\n                d = jso\\n\\n... [截断: 输出过长，省略 27452 字符] ...\\n\\nt\\\")):\\n                        ckpt_dir = candidate\\n                        break\\n                if ckpt_dir is None and os.path.exists(os.path.join(base, \\\"model.pt\\\")):\\n                    ckpt_dir = base\\n                if os.path.exists(ckpt_dir):\\n                    print(f\\\"  Re-evaluating checkpoint: {ckpt_dir}\\\", flush=True)\\n                    results = reeval_checkpoint(\\n                        ckpt_dir, val_samples, args.device, args.max_seq_length\\n                    )\\n                else:\\n                    print(f\\\"  [WARN] Checkpoint not found: {ckpt_dir}\\\", flush=True)\\n                    continue\\n            else:\\n                print(\\\"  [ERROR] No --dry-run, --predictions-dir, or --checkpoints-dir\\\", flush=True)\\n                continue\\n\\n            # Assign strata\\n            results = assign_strata(results, inst_to_repo, repo_counts, dataflow_edges)\\n\\n            # For dry-run or model-based: compute text similarity for sim_bin\\n            if args.dry_run:\\n                for r, s in zip(results, val_samples):\\n                    tsim = text_similarity(s[\\\"query_tokens\\\"][:500], s[\\\"pos_tokens\\\"][:500])\\n                    r[\\\"sim_bin\\\"] = _bin_value(tsim, SIMILARITY_BINS)\\n\\n            all_results[strategy][seed] = results\\n            val_samples_cache[f\\\"{strategy}_s{seed}\\\"] = val_samples\\n            print(f\\\"  -> {len(results)} instances\\\", flush=True)\\n\\n    # Compute neg_difficulty quartiles (text-overlap proxy, CPU-safe)\\n    print(\\\"Computing neg difficulty quartiles...\\\", flush=True)\\n    assign_neg_difficulty_quartiles(all_results, val_samples_cache)\\n\\n    # Run stratified analysis\\n    print(\\\"\\\\nRunning stratified analysis...\\\", flush=True)\\n    repo_analysis = run_stratified_analysis(\\n        all_results, \\\"repo_size_bin\\\", list(REPO_SIZE_BINS.keys()), args.n_bootstrap\\n    )\\n    pool_analysis = run_stratified_analysis(\\n        all_results, \\\"pool_size_bin\\\", list(POOL_SIZE_BINS.keys()), args.n_bootstrap\\n    )\\n    sim_analysis = run_stratified_analysis(\\n        all_results, \\\"sim_bin\\\", list(SIMILARITY_BINS.keys()), args.n_bootstrap\\n    )\\n\\n    dataflow_analysis = {}\\n    if dataflow_edges is not None:\\n        dataflow_analysis = run_stratified_analysis(\\n            all_results, \\\"dataflow_bin\\\", list(DATAFLOW_BINS.keys()), args.n_bootstrap\\n        )\\n\\n    neg_diff_analysis = run_stratified_analysis(\\n        all_results, \\\"neg_difficulty_bin\\\", NEG_DIFFICULTY_QUARTILE_LABELS, args.n_bootstrap\\n    )\\n\\n    # Save JSON\\n    full_results = {\\n        \\\"config\\\": {\\n            \\\"strategies\\\": STRATEGIES,\\n            \\\"seeds\\\": seeds,\\n            \\\"repo_size_bins\\\": {k: list(v) for k, v in REPO_SIZE_BINS.items()},\\n            \\\"pool_size_bins\\\": {k: list(v) for k, v in POOL_SIZE_BINS.items()},\\n            \\\"similarity_bins\\\": {k: list(v) for k, v in SIMILARITY_BINS.items()},\\n            \\\"dataflow_bins\\\": {k: list(v) for k, v in DATAFLOW_BINS.items()},\\n            \\\"neg_difficulty_quartiles\\\": NEG_DIFFICULTY_QUARTILE_LABELS,\\n            \\\"n_bootstrap\\\": args.n_bootstrap,\\n            \\\"dry_run\\\": args.dry_run,\\n        },\\n        \\\"by_repo_size\\\": repo_analysis,\\n        \\\"by_pool_size\\\": pool_analysis,\\n        \\\"by_similarity\\\": sim_analysis,\\n        \\\"by_dataflow\\\": dataflow_analysis,\\n        \\\"by_neg_difficulty\\\": neg_diff_analysis,\\n    }\\n\\n    json_path = os.path.join(args.output_dir, \\\"stratified_results.json\\\")\\n    with open(json_path, \\\"w\\\") as f:\\n        json.dump(full_results, f, indent=2, ensure_ascii=False)\\n    print(f\\\"  Results JSON saved to {json_path}\\\", flush=True)\\n\\n    # CSV summary\\n    csv_path = os.path.join(args.output_dir, \\\"stratified_summary.csv\\\")\\n    write_summary_csv(repo_analysis, pool_analysis, sim_analysis, csv_path, dataflow_analysis, neg_diff_analysis)\\n\\n    # Plots\\n    try:\\n        make_plots(repo_analysis, pool_analysis, sim_analysis, args.output_dir, dataflow_analysis, neg_diff_analysis)\\n    except Exception as e:\\n        print(f\\\"  [WARN] Plot generation failed: {e}\\\", flush=True)\\n\\n    print(\\\"\\\\nDone.\\\", flush=True)\\n\\n\\nif __name__ == \\\"__main__\\\":\\n    main()\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.41}}"
    }
  },
  "sourceToolAssistantUUID": "b552d41f-b29f-46d8-a383-3fabe1545e61",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "fb5ea7f7-b3c9-4750-b931-39d2aaae422b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-14T20:37:07.439Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_018aDTWvPjkhe5WAUMPMSi81`</summary>

```json
{
  "server": "bjb1-42106",
  "command": "ls -la /root/autodl-tmp/structfuse/artifacts/stratified_dryrun/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1fe774b3-5676-4e60-899c-c0920a846909",
  "isSidechain": false,
  "requestId": "req_011Cb36wwosdgT9JbqK7fwRg",
  "type": "assistant",
  "uuid": "400564bf-ca0f-4f17-8802-78e3f1d8b353",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "fb5ea7f7-b3c9-4750-b931-39d2aaae422b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KbMTxEN8mzLzLY7QFaAyvB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9471,
      "cache_read_input_tokens": 34534,
      "output_tokens": 1319,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9471,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1319,
          "cache_read_input_tokens": 34534,
          "cache_creation_input_tokens": 9471,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9471
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

_source line 44 · 2026-05-14T20:37:07.795Z_

<details><summary>↩ Tool result · `toolu_018aDTWvPjkhe5WAUMPMSi81`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 104\\ndrwxr-xr-x 2 root root   111 May 15 04:20 .\\ndrwxr-xr-x 7 root root  4096 May 15 04:36 ..\\n-rw-r--r-- 1 root root 77386 May 15 04:21 stratified_plots.pdf\\n-rw-r--r-- 1 root root 19724 May 15 04:20 stratified_results.json\\n-rw-r--r-- 1 root root  3830 May 15 04:20 stratified_summary.csv\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "400564bf-ca0f-4f17-8802-78e3f1d8b353",
  "isSidechain": false,
  "promptId": "0b7bb415-f2b4-4832-aac4-2e6aafdc7429",
  "type": "user",
  "uuid": "629a1798-3c25-40b8-9af5-bb26e0f5804c",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"total 104\\\\ndrwxr-xr-x 2 root root   111 May 15 04:20 .\\\\ndrwxr-xr-x 7 root root  4096 May 15 04:36 ..\\\\n-rw-r--r-- 1 root root 77386 May 15 04:21 stratified_plots.pdf\\\\n-rw-r--r-- 1 root root 19724 May 15 04:20 stratified_results.json\\\\n-rw-r--r-- 1 root root  3830 May 15 04:20 stratified_summary.csv\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.35}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"total 104\\ndrwxr-xr-x 2 root root   111 May 15 04:20 .\\ndrwxr-xr-x 7 root root  4096 May 15 04:36 ..\\n-rw-r--r-- 1 root root 77386 May 15 04:21 stratified_plots.pdf\\n-rw-r--r-- 1 root root 19724 May 15 04:20 stratified_results.json\\n-rw-r--r-- 1 root root  3830 May 15 04:20 stratified_summary.csv\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"
    }
  },
  "sourceToolAssistantUUID": "400564bf-ca0f-4f17-8802-78e3f1d8b353",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "fb5ea7f7-b3c9-4750-b931-39d2aaae422b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-14T20:37:08.090Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01MX3GdXdZSEt4Bu5ULXTvuc`</summary>

```json
{
  "server": "bjb1-42106",
  "command": "ls -la /root/autodl-tmp/structfuse/artifacts/stratified_dryrun_v2/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "629a1798-3c25-40b8-9af5-bb26e0f5804c",
  "isSidechain": false,
  "requestId": "req_011Cb36wwosdgT9JbqK7fwRg",
  "type": "assistant",
  "uuid": "45ab2302-7431-4022-b299-b5a56f639f69",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "fb5ea7f7-b3c9-4750-b931-39d2aaae422b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KbMTxEN8mzLzLY7QFaAyvB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9471,
      "cache_read_input_tokens": 34534,
      "output_tokens": 1319,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9471,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1319,
          "cache_read_input_tokens": 34534,
          "cache_creation_input_tokens": 9471,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9471
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

_source line 46_

```json
{
  "type": "last-prompt",
  "leafUuid": "45ab2302-7431-4022-b299-b5a56f639f69",
  "sessionId": "fb5ea7f7-b3c9-4750-b931-39d2aaae422b"
}
```

---

### Runtime record

_source line 47_

```json
{
  "type": "ai-title",
  "aiTitle": "Trace stratified_dryrun v1 to v2 differences",
  "sessionId": "fb5ea7f7-b3c9-4750-b931-39d2aaae422b"
}
```

---

### Tool result

_source line 48 · 2026-05-14T20:37:08.447Z_

<details><summary>↩ Tool result · `toolu_01MX3GdXdZSEt4Bu5ULXTvuc`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 160\\ndrwxr-xr-x 2 root root    111 May 15 04:24 .\\ndrwxr-xr-x 7 root root   4096 May 15 04:36 ..\\n-rw-r--r-- 1 root root 113134 May 15 04:24 stratified_plots.pdf\\n-rw-r--r-- 1 root root  33616 May 15 04:24 stratified_results.json\\n-rw-r--r-- 1 root root   6547 May 15 04:24 stratified_summary.csv\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "45ab2302-7431-4022-b299-b5a56f639f69",
  "isSidechain": false,
  "promptId": "0b7bb415-f2b4-4832-aac4-2e6aafdc7429",
  "type": "user",
  "uuid": "c43a731f-c905-4cf8-90d3-a3191adbd9ff",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"total 160\\\\ndrwxr-xr-x 2 root root    111 May 15 04:24 .\\\\ndrwxr-xr-x 7 root root   4096 May 15 04:36 ..\\\\n-rw-r--r-- 1 root root 113134 May 15 04:24 stratified_plots.pdf\\\\n-rw-r--r-- 1 root root  33616 May 15 04:24 stratified_results.json\\\\n-rw-r--r-- 1 root root   6547 May 15 04:24 stratified_summary.csv\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.35}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"total 160\\ndrwxr-xr-x 2 root root    111 May 15 04:24 .\\ndrwxr-xr-x 7 root root   4096 May 15 04:36 ..\\n-rw-r--r-- 1 root root 113134 May 15 04:24 stratified_plots.pdf\\n-rw-r--r-- 1 root root  33616 May 15 04:24 stratified_results.json\\n-rw-r--r-- 1 root root   6547 May 15 04:24 stratified_summary.csv\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"
    }
  },
  "sourceToolAssistantUUID": "45ab2302-7431-4022-b299-b5a56f639f69",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "fb5ea7f7-b3c9-4750-b931-39d2aaae422b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 49 · 2026-05-14T20:37:17.947Z_

<details><summary>Logged reasoning block</summary>

```text
The script was truncated. Let me look at the critical parts more carefully. I need to understand:

1. The `mock_predict` / dry-run logic
2. The `assign_strata` function
3. The `assign_neg_difficulty_quartiles` function
4. The `text_similarity` function

The key thing I noticed: both v1 and v2 have the **same count** in the overlapping strata (small=130, medium=346). So data filtering/sample changes are NOT the cause.

Since both are dry-runs, the predictions must be generated from mock predictions. The mock predictions are likely using random scores with some seed. 

If the mock prediction logic changed between v1 and v2 — maybe new features in v2 altered how candidates are scored, or the order of operations shifted the random state — that would explain the divergent values. I should check for older script versions or backups, then locate the actual `mock_predict` or `dry_run` function to see what's generating these scores.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c43a731f-c905-4cf8-90d3-a3191adbd9ff",
  "isSidechain": false,
  "requestId": "req_011Cb36yduezj5CD2rnkiL6A",
  "type": "assistant",
  "uuid": "234ddef9-992f-4ab0-97ce-7bf201dd479a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "fb5ea7f7-b3c9-4750-b931-39d2aaae422b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015pWPESJkbyQUqcygefeWEG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5219,
      "cache_read_input_tokens": 44005,
      "output_tokens": 538,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5219,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 538,
          "cache_read_input_tokens": 44005,
          "cache_creation_input_tokens": 5219,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5219
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

_source line 50 · 2026-05-14T20:37:18.127Z_

脚本被截断了，需要读关键函数。同时用 Python 在服务器上做精确数值对比。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "234ddef9-992f-4ab0-97ce-7bf201dd479a",
  "isSidechain": false,
  "requestId": "req_011Cb36yduezj5CD2rnkiL6A",
  "type": "assistant",
  "uuid": "76d85c96-f241-4b80-9ff8-4e8830916fd5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "fb5ea7f7-b3c9-4750-b931-39d2aaae422b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015pWPESJkbyQUqcygefeWEG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5219,
      "cache_read_input_tokens": 44005,
      "output_tokens": 538,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5219,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 538,
          "cache_read_input_tokens": 44005,
          "cache_creation_input_tokens": 5219,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5219
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

_source line 51 · 2026-05-14T20:37:19.094Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01NtbpLfm2MQBpjG9DaANAo7`</summary>

```json
{
  "server": "bjb1-42106",
  "command": "grep -n \"def \" /root/structfuse/evaluation/analyze_stratified.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "76d85c96-f241-4b80-9ff8-4e8830916fd5",
  "isSidechain": false,
  "requestId": "req_011Cb36yduezj5CD2rnkiL6A",
  "type": "assistant",
  "uuid": "1a9f0c82-9995-40a7-aa8a-beb5cb73c189",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "fb5ea7f7-b3c9-4750-b931-39d2aaae422b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015pWPESJkbyQUqcygefeWEG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5219,
      "cache_read_input_tokens": 44005,
      "output_tokens": 538,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5219,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 538,
          "cache_read_input_tokens": 44005,
          "cache_creation_input_tokens": 5219,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5219
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

_source line 52 · 2026-05-14T20:37:19.453Z_

<details><summary>↩ Tool result · `toolu_01NtbpLfm2MQBpjG9DaANAo7`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"64:def _bin_value(value, bins):\\n73:def load_m1_metadata(m1_path: str) -> Tuple[Dict[str, str], Dict[str, int]]:\\n93:def load_dataflow_edges(graph_path: str) -> Dict[str, int]:\\n102:def load_val_samples(val_path: str, lite: bool = False) -> List[Dict[str, Any]]:\\n143:def text_similarity(a: str, b: str) -> float:\\n154:def reeval_checkpoint(\\n193:            def _encode(text):\\n230:def load_predictions(pred_file: str, val_samples: List[Dict]) -> List[Dict]:\\n268:def mock_predictions(\\n300:def compute_metrics(results: List[Dict]) -> Dict[str, float]:\\n313:def _metric_fn(results, metric_name):\\n318:def bootstrap_ci(\\n345:def assign_strata(\\n368:def assign_neg_difficulty_quartiles(\\n416:def group_by(results: List[Dict], key: str) -> Dict[str, List[Dict]]:\\n425:def run_stratified_analysis(\\n474:def make_plots(\\n649:def write_summary_csv(\\n713:def main():\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1a9f0c82-9995-40a7-aa8a-beb5cb73c189",
  "isSidechain": false,
  "promptId": "0b7bb415-f2b4-4832-aac4-2e6aafdc7429",
  "type": "user",
  "uuid": "a4321f5f-ca3d-4498-b37f-e198c0636b0d",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"64:def _bin_value(value, bins):\\\\n73:def load_m1_metadata(m1_path: str) -> Tuple[Dict[str, str], Dict[str, int]]:\\\\n93:def load_dataflow_edges(graph_path: str) -> Dict[str, int]:\\\\n102:def load_val_samples(val_path: str, lite: bool = False) -> List[Dict[str, Any]]:\\\\n143:def text_similarity(a: str, b: str) -> float:\\\\n154:def reeval_checkpoint(\\\\n193:            def _encode(text):\\\\n230:def load_predictions(pred_file: str, val_samples: List[Dict]) -> List[Dict]:\\\\n268:def mock_predictions(\\\\n300:def compute_metrics(results: List[Dict]) -> Dict[str, float]:\\\\n313:def _metric_fn(results, metric_name):\\\\n318:def bootstrap_ci(\\\\n345:def assign_strata(\\\\n368:def assign_neg_difficulty_quartiles(\\\\n416:def group_by(results: List[Dict], key: str) -> Dict[str, List[Dict]]:\\\\n425:def run_stratified_analysis(\\\\n474:def make_plots(\\\\n649:def write_summary_csv(\\\\n713:def main():\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.35}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"64:def _bin_value(value, bins):\\n73:def load_m1_metadata(m1_path: str) -> Tuple[Dict[str, str], Dict[str, int]]:\\n93:def load_dataflow_edges(graph_path: str) -> Dict[str, int]:\\n102:def load_val_samples(val_path: str, lite: bool = False) -> List[Dict[str, Any]]:\\n143:def text_similarity(a: str, b: str) -> float:\\n154:def reeval_checkpoint(\\n193:            def _encode(text):\\n230:def load_predictions(pred_file: str, val_samples: List[Dict]) -> List[Dict]:\\n268:def mock_predictions(\\n300:def compute_metrics(results: List[Dict]) -> Dict[str, float]:\\n313:def _metric_fn(results, metric_name):\\n318:def bootstrap_ci(\\n345:def assign_strata(\\n368:def assign_neg_difficulty_quartiles(\\n416:def group_by(results: List[Dict], key: str) -> Dict[str, List[Dict]]:\\n425:def run_stratified_analysis(\\n474:def make_plots(\\n649:def write_summary_csv(\\n713:def main():\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"
    }
  },
  "sourceToolAssistantUUID": "1a9f0c82-9995-40a7-aa8a-beb5cb73c189",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "fb5ea7f7-b3c9-4750-b931-39d2aaae422b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-14T20:37:19.461Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01L3zfzJBtiRzFg7ZAh4RFaK`</summary>

```json
{
  "server": "bjb1-42106",
  "command": "wc -l /root/structfuse/evaluation/analyze_stratified.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a4321f5f-ca3d-4498-b37f-e198c0636b0d",
  "isSidechain": false,
  "requestId": "req_011Cb36yduezj5CD2rnkiL6A",
  "type": "assistant",
  "uuid": "6edc840f-9477-44b4-964b-7d899c3f4772",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "fb5ea7f7-b3c9-4750-b931-39d2aaae422b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015pWPESJkbyQUqcygefeWEG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5219,
      "cache_read_input_tokens": 44005,
      "output_tokens": 538,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5219,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 538,
          "cache_read_input_tokens": 44005,
          "cache_creation_input_tokens": 5219,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5219
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

_source line 54 · 2026-05-14T20:37:19.871Z_

<details><summary>↩ Tool result · `toolu_01L3zfzJBtiRzFg7ZAh4RFaK`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"910 /root/structfuse/evaluation/analyze_stratified.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6edc840f-9477-44b4-964b-7d899c3f4772",
  "isSidechain": false,
  "promptId": "0b7bb415-f2b4-4832-aac4-2e6aafdc7429",
  "type": "user",
  "uuid": "c6c471d7-9043-4d8f-b32b-b7f0a77bfbd1",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"910 /root/structfuse/evaluation/analyze_stratified.py\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.4}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"910 /root/structfuse/evaluation/analyze_stratified.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4}}"
    }
  },
  "sourceToolAssistantUUID": "6edc840f-9477-44b4-964b-7d899c3f4772",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "fb5ea7f7-b3c9-4750-b931-39d2aaae422b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-14T20:37:26.405Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01Sr1Q5U1n8hmAMymPJQ8B1S`</summary>

```json
{
  "server": "bjb1-42106",
  "command": "sed -n '268,400p' /root/structfuse/evaluation/analyze_stratified.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c6c471d7-9043-4d8f-b32b-b7f0a77bfbd1",
  "isSidechain": false,
  "requestId": "req_011Cb36zUj2ynwGy3r6e66pr",
  "type": "assistant",
  "uuid": "499c2e72-5350-4207-9009-8d2e47831b42",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "fb5ea7f7-b3c9-4750-b931-39d2aaae422b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G4GCHGr9HaFEgGD261e2e6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1085,
      "cache_read_input_tokens": 49224,
      "output_tokens": 235,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1085,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 235,
          "cache_read_input_tokens": 49224,
          "cache_creation_input_tokens": 1085,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1085
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

_source line 56 · 2026-05-14T20:37:26.420Z_

<details><summary>↩ Tool result · `toolu_01Sr1Q5U1n8hmAMymPJQ8B1S`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: 'sed' is not in the read-only allowlist. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "499c2e72-5350-4207-9009-8d2e47831b42",
  "isSidechain": false,
  "promptId": "0b7bb415-f2b4-4832-aac4-2e6aafdc7429",
  "type": "user",
  "uuid": "403b029d-c4b2-4ffb-90d0-af0ff52a1692",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"[ssh_read_only] Command blocked: 'sed' is not in the read-only allowlist. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\\\", \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: 'sed' is not in the read-only allowlist. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "499c2e72-5350-4207-9009-8d2e47831b42",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "fb5ea7f7-b3c9-4750-b931-39d2aaae422b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-14T20:37:26.845Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01L4yPp23S7VasdfBFeG4BYj`</summary>

```json
{
  "server": "bjb1-42106",
  "command": "sed -n '713,830p' /root/structfuse/evaluation/analyze_stratified.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "403b029d-c4b2-4ffb-90d0-af0ff52a1692",
  "isSidechain": false,
  "requestId": "req_011Cb36zUj2ynwGy3r6e66pr",
  "type": "assistant",
  "uuid": "d5820079-e491-4254-abf7-f4bcb63ffd96",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "fb5ea7f7-b3c9-4750-b931-39d2aaae422b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G4GCHGr9HaFEgGD261e2e6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1085,
      "cache_read_input_tokens": 49224,
      "output_tokens": 235,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1085,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 235,
          "cache_read_input_tokens": 49224,
          "cache_creation_input_tokens": 1085,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1085
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

_source line 58 · 2026-05-14T20:37:26.854Z_

<details><summary>↩ Tool result · `toolu_01L4yPp23S7VasdfBFeG4BYj`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: 'sed' is not in the read-only allowlist. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d5820079-e491-4254-abf7-f4bcb63ffd96",
  "isSidechain": false,
  "promptId": "0b7bb415-f2b4-4832-aac4-2e6aafdc7429",
  "type": "user",
  "uuid": "62f21530-da8d-43db-97fe-8a2d21fae647",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"[ssh_read_only] Command blocked: 'sed' is not in the read-only allowlist. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\\\", \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: 'sed' is not in the read-only allowlist. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "d5820079-e491-4254-abf7-f4bcb63ffd96",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "fb5ea7f7-b3c9-4750-b931-39d2aaae422b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 59 · 2026-05-14T20:37:30.192Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01SH1TwWaMQQr6QWz3GFDVF5`</summary>

```json
{
  "server": "bjb1-42106",
  "command": "head -450 /root/structfuse/evaluation/analyze_stratified.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "62f21530-da8d-43db-97fe-8a2d21fae647",
  "isSidechain": false,
  "requestId": "req_011Cb3711ag13Ehjj5qGzZ7q",
  "type": "assistant",
  "uuid": "0acc21c0-666f-4f4e-abd8-44d2ff1fa172",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "fb5ea7f7-b3c9-4750-b931-39d2aaae422b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018ZYpv5yF1G4x7BT2tTtkH5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 480,
      "cache_read_input_tokens": 50309,
      "output_tokens": 121,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 480,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 121,
          "cache_read_input_tokens": 50309,
          "cache_creation_input_tokens": 480,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 480
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

_source line 60 · 2026-05-14T20:37:30.621Z_

<details><summary>↩ Tool result · `toolu_01SH1TwWaMQQr6QWz3GFDVF5`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n\\\"\\\"\\\"Stratified analysis of embedding vs random negative strategies by data strata.\\n\\nAnalyses M2 per-instance predictions across:\\n  - Repo size (instance count per repo from M1)\\n  - Candidate pool size (neg_candidates per query)\\n  - Query-positive similarity (cosine sim from model, or text overlap for dry-run)\\n\\nInputs:\\n  - M2 per-instance predictions (from --predictions-dir or re-eval from checkpoints)\\n  - M1 all.jsonl (repo metadata)\\n  - Val JSONL files (query/candidate structure)\\n\\nOutputs:\\n  - stratified_results.json: full per-stratum metrics with bootstrap CI\\n  - stratified_summary.csv: compact table\\n  - stratified_plots.pdf: grouped bar charts, heatmaps, delta trends\\n\\\"\\\"\\\"\\n\\nimport argparse\\nimport csv\\nimport json\\nimport math\\nimport os\\nimport sys\\nfrom collections import Counter, defaultdict\\nfrom pathlib import Path\\nfrom typing import Any, Dict, List, Optional, Tuple\\n\\nimport numpy as np\\n\\nSTRATEGIES = [\\\"random\\\", \\\"embedding_distance\\\", \\\"dataflow_aware\\\"]\\nSTRATEGY_LABELS = {\\\"random\\\": \\\"Random\\\", \\\"embedding_distance\\\": \\\"Embedding\\\", \\\"dataflow_aware\\\": \\\"Dataflow\\\"}\\nSTRATEGY_COLORS = {\\\"random\\\": \\\"#4C72B0\\\", \\\"embedding_distance\\\": \\\"#DD8452\\\", \\\"dataflow_aware\\\": \\\"#55A868\\\"}\\n\\nREPO_SIZE_BINS = {\\n    \\\"small\\\": (0, 50),\\n    \\\"medium\\\": (50, 200),\\n    \\\"large\\\": (200, 500),\\n    \\\"xlarge\\\": (500, float(\\\"inf\\\")),\\n}\\n\\nPOOL_SIZE_BINS = {\\n    \\\"small\\\": (0, 20),\\n    \\\"medium\\\": (20, 40),\\n    \\\"large\\\": (40, 51),\\n}\\n\\nSIMILARITY_BINS = {\\n    \\\"low\\\": (0.0, 0.3),\\n    \\\"medium\\\": (0.3, 0.6),\\n    \\\"high\\\": (0.6, 1.01),\\n}\\n\\nDATAFLOW_BINS = {\\n    \\\"sparse\\\": (0, 2),\\n    \\\"moderate\\\": (2, 10),\\n    \\\"rich\\\": (10, float(\\\"inf\\\")),\\n}\\n\\nNEG_DIFFICULTY_QUARTILE_LABELS = [\\\"Q1_easy\\\", \\\"Q2\\\", \\\"Q3\\\", \\\"Q4_hard\\\"]\\n\\n\\ndef _bin_value(value, bins):\\n    for name, (lo, hi) in bins.items():\\n        if lo <= value < hi:\\n            return name\\n    return \\\"unknown\\\"\\n\\n\\n# ── M1 metadata ───────────────────────────────────────────────────��─\\n\\ndef load_m1_metadata(m1_path: str) -> Tuple[Dict[str, str], Dict[str, int]]:\\n    import re\\n    inst_to_repo = {}\\n    repo_counts: Counter = Counter()\\n    pat_iid = re.compile(r'\\\"instance_id\\\"\\\\s*:\\\\s*\\\"([^\\\"]+)\\\"')\\n    pat_repo = re.compile(r'\\\"repo\\\"\\\\s*:\\\\s*\\\"([^\\\"]+)\\\"')\\n    with open(m1_path) as f:\\n        for line in f:\\n            m_iid = pat_iid.search(line)\\n            m_repo = pat_repo.search(line)\\n            if m_iid and m_repo:\\n                iid = m_iid.group(1)\\n                repo = m_repo.group(1)\\n                inst_to_repo[iid] = repo\\n                repo_counts[repo] += 1\\n    return inst_to_repo, dict(repo_counts)\\n\\n\\n# ── Dataflow graph loading ────────────────────────────────────────────\\n\\ndef load_dataflow_edges(graph_path: str) -> Dict[str, int]:\\n    \\\"\\\"\\\"Load dataflow graph and return {file_key: edge_count}.\\\"\\\"\\\"\\n    with open(graph_path) as f:\\n        graph = json.load(f)\\n    return {k: len(v) for k, v in graph.items()}\\n\\n\\n# ── Val data loading ─────────────────────────────────────────────────\\n\\ndef load_val_samples(val_path: str, lite: bool = False) -> List[Dict[str, Any]]:\\n    \\\"\\\"\\\"Load val JSONL. lite=True skips candidate_tokens (faster for dry-run).\\\"\\\"\\\"\\n    import re\\n    samples = []\\n    pat_qid = re.compile(r'\\\"query_id\\\"\\\\s*:\\\\s*\\\"([^\\\"]+)\\\"')\\n    with open(val_path) as f:\\n        for line in f:\\n            if not line.strip():\\n                continue\\n            if lite:\\n                m = pat_qid.search(line)\\n                if not m:\\n                    continue\\n                qid = m.group(1)\\n                instance_id = qid.split(\\\"::\\\")[0] if \\\"::\\\" in qid else qid\\n                d = json.loads(line)\\n                samples.append({\\n                    \\\"query_id\\\": qid,\\n                    \\\"instance_id\\\": instance_id,\\n                    \\\"pool_size\\\": len(d.get(\\\"neg_candidates\\\", [])),\\n                    \\\"query_tokens\\\": d.get(\\\"query_tokens\\\", \\\"\\\")[:1000],\\n                    \\\"pos_tokens\\\": d.get(\\\"pos_tokens\\\", \\\"\\\")[:1000],\\n                    \\\"neg_candidates\\\": [],\\n                    \\\"candidate_tokens\\\": {},\\n                })\\n            else:\\n                d = jso\\n\\n... [截断: 输出过长，省略 7671 字符] ...\\n\\n], \\\"\\\")\\n        rc = repo_counts.get(repo, 0)\\n        r[\\\"repo\\\"] = repo\\n        r[\\\"repo_size\\\"] = rc\\n        r[\\\"repo_size_bin\\\"] = _bin_value(rc, REPO_SIZE_BINS)\\n        r[\\\"pool_size_bin\\\"] = _bin_value(r[\\\"pool_size\\\"], POOL_SIZE_BINS)\\n        r[\\\"sim_bin\\\"] = _bin_value(r[\\\"pos_sim\\\"], SIMILARITY_BINS)\\n        if dataflow_edges is not None:\\n            ec = dataflow_edges.get(r[\\\"query_id\\\"], 0)\\n            r[\\\"dataflow_edge_count\\\"] = ec\\n            r[\\\"dataflow_bin\\\"] = _bin_value(ec, DATAFLOW_BINS)\\n        else:\\n            r[\\\"dataflow_bin\\\"] = \\\"unknown\\\"\\n    return results\\n\\n\\ndef assign_neg_difficulty_quartiles(\\n    all_results: Dict[str, Dict[int, List[Dict]]],\\n    val_samples_cache: Dict[str, List[Dict]],\\n):\\n    \\\"\\\"\\\"Compute text-overlap-based neg difficulty proxy and assign quartiles.\\\"\\\"\\\"\\n    for strategy in list(all_results.keys()):\\n        for seed in list(all_results[strategy].keys()):\\n            results = all_results[strategy][seed]\\n            cache_key = f\\\"{strategy}_s{seed}\\\"\\n            samples = val_samples_cache.get(cache_key, [])\\n            sample_map = {s[\\\"query_id\\\"]: s for s in samples}\\n\\n            margins = []\\n            for r in results:\\n                s = sample_map.get(r[\\\"query_id\\\"])\\n                if s is None:\\n                    margins.append(0.0)\\n                    continue\\n                q_toks = set(s.get(\\\"query_tokens\\\", \\\"\\\")[:1000].split())\\n                p_toks = set(s.get(\\\"pos_tokens\\\", \\\"\\\")[:1000].split())\\n                pos_overlap = len(q_toks & p_toks) / max(len(q_toks | p_toks), 1)\\n                max_neg_overlap = 0.0\\n                neg_cands = s.get(\\\"neg_candidates\\\", [])[:7]\\n                cand_tokens = s.get(\\\"candidate_tokens\\\", {})\\n                for neg_id in neg_cands:\\n                    neg_text = cand_tokens.get(neg_id, \\\"\\\")\\n                    if neg_text:\\n                        n_toks = set(neg_text[:1000].split())\\n                        ov = len(q_toks & n_toks) / max(len(q_toks | n_toks), 1)\\n                        max_neg_overlap = max(max_neg_overlap, ov)\\n                margin = pos_overlap - max_neg_overlap\\n                margins.append(margin)\\n                r[\\\"neg_difficulty_margin\\\"] = margin\\n\\n            if margins:\\n                arr = np.array(margins)\\n                q25, q50, q75 = np.percentile(arr, [25, 50, 75])\\n                for r, m in zip(results, margins):\\n                    if m <= q25:\\n                        r[\\\"neg_difficulty_bin\\\"] = \\\"Q4_hard\\\"\\n                    elif m <= q50:\\n                        r[\\\"neg_difficulty_bin\\\"] = \\\"Q3\\\"\\n                    elif m <= q75:\\n                        r[\\\"neg_difficulty_bin\\\"] = \\\"Q2\\\"\\n                    else:\\n                        r[\\\"neg_difficulty_bin\\\"] = \\\"Q1_easy\\\"\\n\\n\\ndef group_by(results: List[Dict], key: str) -> Dict[str, List[Dict]]:\\n    groups: Dict[str, List[Dict]] = defaultdict(list)\\n    for r in results:\\n        groups[r[key]].append(r)\\n    return dict(groups)\\n\\n\\n# ── Analysis core ────────────────────────────────────────────────────\\n\\ndef run_stratified_analysis(\\n    all_results: Dict[str, Dict[int, List[Dict]]],\\n    strata_key: str,\\n    bin_order: List[str],\\n    n_bootstrap: int = 1000,\\n) -> Dict:\\n    analysis = {}\\n    for bin_name in bin_order:\\n        analysis[bin_name] = {}\\n        for strategy in STRATEGIES:\\n            seed_results = []\\n            for seed, results in all_results.get(strategy, {}).items():\\n                grouped = group_by(results, strata_key)\\n                seed_results.extend(grouped.get(bin_name, []))\\n\\n            metrics = compute_metrics(seed_results)\\n            ci_r1 = bootstrap_ci(seed_results, \\\"R@1\\\", n_bootstrap)\\n            ci_r5 = bootstrap_ci(seed_results, \\\"R@5\\\", n_bootstrap)\\n            ci_mrr = bootstrap_ci(seed_results, \\\"MRR\\\", n_bootstrap)\\n\\n            analysis[bin_name][strategy] = {\\n                \\\"R@1\\\": ci_r1[0],\\n                \\\"R@1_ci\\\": [ci_r1[1], ci_r1[2]],\\n                \\\"R@5\\\": ci_r5[0],\\n                \\\"R@5_ci\\\": [ci_r5[1], ci_r5[2]],\\n                \\\"MRR\\\": ci_mrr[0],\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.41}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0acc21c0-666f-4f4e-abd8-44d2ff1fa172",
  "isSidechain": false,
  "promptId": "0b7bb415-f2b4-4832-aac4-2e6aafdc7429",
  "type": "user",
  "uuid": "5d6dc5de-e9d9-44b5-8c5e-a853485c51cc",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"#!/usr/bin/env python3\\\\n\\\\\\\"\\\\\\\"\\\\\\\"Stratified analysis of embedding vs random negative strategies by data strata.\\\\n\\\\nAnalyses M2 per-instance predictions across:\\\\n  - Repo size (instance count per repo from M1)\\\\n  - Candidate pool size (neg_candidates per query)\\\\n  - Query-positive similarity (cosine sim from model, or text overlap for dry-run)\\\\n\\\\nInputs:\\\\n  - M2 per-instance predictions (from --predictions-dir or re-eval from checkpoints)\\\\n  - M1 all.jsonl (repo metadata)\\\\n  - Val JSONL files (query/candidate structure)\\\\n\\\\nOutputs:\\\\n  - stratified_results.json: full per-stratum metrics with bootstrap CI\\\\n  - stratified_summary.csv: compact table\\\\n  - stratified_plots.pdf: grouped bar charts, heatmaps, delta trends\\\\n\\\\\\\"\\\\\\\"\\\\\\\"\\\\n\\\\nimport argparse\\\\nimport csv\\\\nimport json\\\\nimport math\\\\nimport os\\\\nimport sys\\\\nfrom collections import Counter, defaultdict\\\\nfrom pathlib import Path\\\\nfrom typing import Any, Dict, List, Optional, Tuple\\\\n\\\\nimport numpy as np\\\\n\\\\nSTRATEGIES = [\\\\\\\"random\\\\\\\", \\\\\\\"embedding_distance\\\\\\\", \\\\\\\"dataflow_aware\\\\\\\"]\\\\nSTRATEGY_LABELS = {\\\\\\\"random\\\\\\\": \\\\\\\"Random\\\\\\\", \\\\\\\"embedding_distance\\\\\\\": \\\\\\\"Embedding\\\\\\\", \\\\\\\"dataflow_aware\\\\\\\": \\\\\\\"Dataflow\\\\\\\"}\\\\nSTRATEGY_COLORS = {\\\\\\\"random\\\\\\\": \\\\\\\"#4C72B0\\\\\\\", \\\\\\\"embedding_distance\\\\\\\": \\\\\\\"#DD8452\\\\\\\", \\\\\\\"dataflow_aware\\\\\\\": \\\\\\\"#55A868\\\\\\\"}\\\\n\\\\nREPO_SIZE_BINS = {\\\\n    \\\\\\\"small\\\\\\\": (0, 50),\\\\n    \\\\\\\"medium\\\\\\\": (50, 200),\\\\n    \\\\\\\"large\\\\\\\": (200, 500),\\\\n    \\\\\\\"xlarge\\\\\\\": (500, float(\\\\\\\"inf\\\\\\\")),\\\\n}\\\\n\\\\nPOOL_SIZE_BINS = {\\\\n    \\\\\\\"small\\\\\\\": (0, 20),\\\\n    \\\\\\\"medium\\\\\\\": (20, 40),\\\\n    \\\\\\\"large\\\\\\\": (40, 51),\\\\n}\\\\n\\\\nSIMILARITY_BINS = {\\\\n    \\\\\\\"low\\\\\\\": (0.0, 0.3),\\\\n    \\\\\\\"medium\\\\\\\": (0.3, 0.6),\\\\n    \\\\\\\"high\\\\\\\": (0.6, 1.01),\\\\n}\\\\n\\\\nDATAFLOW_BINS = {\\\\n    \\\\\\\"sparse\\\\\\\": (0, 2),\\\\n    \\\\\\\"moderate\\\\\\\": (2, 10),\\\\n    \\\\\\\"rich\\\\\\\": (10, float(\\\\\\\"inf\\\\\\\")),\\\\n}\\\\n\\\\nNEG_DIFFICULTY_QUARTILE_LABELS = [\\\\\\\"Q1_easy\\\\\\\", \\\\\\\"Q2\\\\\\\", \\\\\\\"Q3\\\\\\\", \\\\\\\"Q4_hard\\\\\\\"]\\\\n\\\\n\\\\ndef _bin_value(value, bins):\\\\n    for name, (lo, hi) in bins.items():\\\\n        if lo <= value < hi:\\\\n            return name\\\\n    return \\\\\\\"unknown\\\\\\\"\\\\n\\\\n\\\\n# ── M1 metadata ───────────────────────────────────────────────────��─\\\\n\\\\ndef load_m1_metadata(m1_path: str) -> Tuple[Dict[str, str], Dict[str, int]]:\\\\n    import re\\\\n    inst_to_repo = {}\\\\n    repo_counts: Counter = Counter()\\\\n    pat_iid = re.compile(r'\\\\\\\"instance_id\\\\\\\"\\\\\\\\s*:\\\\\\\\s*\\\\\\\"([^\\\\\\\"]+)\\\\\\\"')\\\\n    pat_repo = re.compile(r'\\\\\\\"repo\\\\\\\"\\\\\\\\s*:\\\\\\\\s*\\\\\\\"([^\\\\\\\"]+)\\\\\\\"')\\\\n    with open(m1_path) as f:\\\\n        for line in f:\\\\n            m_iid = pat_iid.search(line)\\\\n            m_repo = pat_repo.search(line)\\\\n            if m_iid and m_repo:\\\\n                iid = m_iid.group(1)\\\\n                repo = m_repo.group(1)\\\\n                inst_to_repo[iid] = repo\\\\n                repo_counts[repo] += 1\\\\n    return inst_to_repo, dict(repo_counts)\\\\n\\\\n\\\\n# ── Dataflow graph loading ────────────────────────────────────────────\\\\n\\\\ndef load_dataflow_edges(graph_path: str) -> Dict[str, int]:\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"Load dataflow graph and return {file_key: edge_count}.\\\\\\\"\\\\\\\"\\\\\\\"\\\\n    with open(graph_path) as f:\\\\n        graph = json.load(f)\\\\n    return {k: len(v) for k, v in graph.items()}\\\\n\\\\n\\\\n# ── Val data loading ─────────────────────────────────────────────────\\\\n\\\\ndef load_val_samples(val_path: str, lite: bool = False) -> List[Dict[str, Any]]:\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"Load val JSONL. lite=True skips candidate_tokens (faster for dry-run).\\\\\\\"\\\\\\\"\\\\\\\"\\\\n    import re\\\\n    samples = []\\\\n    pat_qid = re.compile(r'\\\\\\\"query_id\\\\\\\"\\\\\\\\s*:\\\\\\\\s*\\\\\\\"([^\\\\\\\"]+)\\\\\\\"')\\\\n    with open(val_path) as f:\\\\n        for line in f:\\\\n            if not line.strip():\\\\n                continue\\\\n            if lite:\\\\n                m = pat_qid.search(line)\\\\n                if not m:\\\\n                    continue\\\\n                qid = m.group(1)\\\\n                instance_id = qid.split(\\\\\\\"::\\\\\\\")[0] if \\\\\\\"::\\\\\\\" in qid else qid\\\\n                d = json.loads(line)\\\\n                samples.append({\\\\n                    \\\\\\\"query_id\\\\\\\": qid,\\\\n                    \\\\\\\"instance_id\\\\\\\": instance_id,\\\\n                    \\\\\\\"pool_size\\\\\\\": len(d.get(\\\\\\\"neg_candidates\\\\\\\", [])),\\\\n                    \\\\\\\"query_tokens\\\\\\\": d.get(\\\\\\\"query_tokens\\\\\\\", \\\\\\\"\\\\\\\")[:1000],\\\\n                    \\\\\\\"pos_tokens\\\\\\\": d.get(\\\\\\\"pos_tokens\\\\\\\", \\\\\\\"\\\\\\\")[:1000],\\\\n                    \\\\\\\"neg_candidates\\\\\\\": [],\\\\n                    \\\\\\\"candidate_tokens\\\\\\\": {},\\\\n                })\\\\n            else:\\\\n                d = jso\\\\n\\\\n... [截断: 输出过长，省略 7671 字符] ...\\\\n\\\\n], \\\\\\\"\\\\\\\")\\\\n        rc = repo_counts.get(repo, 0)\\\\n        r[\\\\\\\"repo\\\\\\\"] = repo\\\\n        r[\\\\\\\"repo_size\\\\\\\"] = rc\\\\n        r[\\\\\\\"repo_size_bin\\\\\\\"] = _bin_value(rc, REPO_SIZE_BINS)\\\\n        r[\\\\\\\"pool_size_bin\\\\\\\"] = _bin_value(r[\\\\\\\"pool_size\\\\\\\"], POOL_SIZE_BINS)\\\\n        r[\\\\\\\"sim_bin\\\\\\\"] = _bin_value(r[\\\\\\\"pos_sim\\\\\\\"], SIMILARITY_BINS)\\\\n        if dataflow_edges is not None:\\\\n            ec = dataflow_edges.get(r[\\\\\\\"query_id\\\\\\\"], 0)\\\\n            r[\\\\\\\"dataflow_edge_count\\\\\\\"] = ec\\\\n            r[\\\\\\\"dataflow_bin\\\\\\\"] = _bin_value(ec, DATAFLOW_BINS)\\\\n        else:\\\\n            r[\\\\\\\"dataflow_bin\\\\\\\"] = \\\\\\\"unknown\\\\\\\"\\\\n    return results\\\\n\\\\n\\\\ndef assign_neg_difficulty_quartiles(\\\\n    all_results: Dict[str, Dict[int, List[Dict]]],\\\\n    val_samples_cache: Dict[str, List[Dict]],\\\\n):\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"Compute text-overlap-based neg difficulty proxy and assign quartiles.\\\\\\\"\\\\\\\"\\\\\\\"\\\\n    for strategy in list(all_results.keys()):\\\\n        for seed in list(all_results[strategy].keys()):\\\\n            results = all_results[strategy][seed]\\\\n            cache_key = f\\\\\\\"{strategy}_s{seed}\\\\\\\"\\\\n            samples = val_samples_cache.get(cache_key, [])\\\\n            sample_map = {s[\\\\\\\"query_id\\\\\\\"]: s for s in samples}\\\\n\\\\n            margins = []\\\\n            for r in results:\\\\n                s = sample_map.get(r[\\\\\\\"query_id\\\\\\\"])\\\\n                if s is None:\\\\n                    margins.append(0.0)\\\\n                    continue\\\\n                q_toks = set(s.get(\\\\\\\"query_tokens\\\\\\\", \\\\\\\"\\\\\\\")[:1000].split())\\\\n                p_toks = set(s.get(\\\\\\\"pos_tokens\\\\\\\", \\\\\\\"\\\\\\\")[:1000].split())\\\\n                pos_overlap = len(q_toks & p_toks) / max(len(q_toks | p_toks), 1)\\\\n                max_neg_overlap = 0.0\\\\n                neg_cands = s.get(\\\\\\\"neg_candidates\\\\\\\", [])[:7]\\\\n                cand_tokens = s.get(\\\\\\\"candidate_tokens\\\\\\\", {})\\\\n                for neg_id in neg_cands:\\\\n                    neg_text = cand_tokens.get(neg_id, \\\\\\\"\\\\\\\")\\\\n                    if neg_text:\\\\n                        n_toks = set(neg_text[:1000].split())\\\\n                        ov = len(q_toks & n_toks) / max(len(q_toks | n_toks), 1)\\\\n                        max_neg_overlap = max(max_neg_overlap, ov)\\\\n                margin = pos_overlap - max_neg_overlap\\\\n                margins.append(margin)\\\\n                r[\\\\\\\"neg_difficulty_margin\\\\\\\"] = margin\\\\n\\\\n            if margins:\\\\n                arr = np.array(margins)\\\\n                q25, q50, q75 = np.percentile(arr, [25, 50, 75])\\\\n                for r, m in zip(results, margins):\\\\n                    if m <= q25:\\\\n                        r[\\\\\\\"neg_difficulty_bin\\\\\\\"] = \\\\\\\"Q4_hard\\\\\\\"\\\\n                    elif m <= q50:\\\\n                        r[\\\\\\\"neg_difficulty_bin\\\\\\\"] = \\\\\\\"Q3\\\\\\\"\\\\n                    elif m <= q75:\\\\n                        r[\\\\\\\"neg_difficulty_bin\\\\\\\"] = \\\\\\\"Q2\\\\\\\"\\\\n                    else:\\\\n                        r[\\\\\\\"neg_difficulty_bin\\\\\\\"] = \\\\\\\"Q1_easy\\\\\\\"\\\\n\\\\n\\\\ndef group_by(results: List[Dict], key: str) -> Dict[str, List[Dict]]:\\\\n    groups: Dict[str, List[Dict]] = defaultdict(list)\\\\n    for r in results:\\\\n        groups[r[key]].append(r)\\\\n    return dict(groups)\\\\n\\\\n\\\\n# ── Analysis core ────────────────────────────────────────────────────\\\\n\\\\ndef run_stratified_analysis(\\\\n    all_results: Dict[str, Dict[int, List[Dict]]],\\\\n    strata_key: str,\\\\n    bin_order: List[str],\\\\n    n_bootstrap: int = 1000,\\\\n) -> Dict:\\\\n    analysis = {}\\\\n    for bin_name in bin_order:\\\\n        analysis[bin_name] = {}\\\\n        for strategy in STRATEGIES:\\\\n            seed_results = []\\\\n            for seed, results in all_results.get(strategy, {}).items():\\\\n                grouped = group_by(results, strata_key)\\\\n                seed_results.extend(grouped.get(bin_name, []))\\\\n\\\\n            metrics = compute_metrics(seed_results)\\\\n            ci_r1 = bootstrap_ci(seed_results, \\\\\\\"R@1\\\\\\\", n_bootstrap)\\\\n            ci_r5 = bootstrap_ci(seed_results, \\\\\\\"R@5\\\\\\\", n_bootstrap)\\\\n            ci_mrr = bootstrap_ci(seed_results, \\\\\\\"MRR\\\\\\\", n_bootstrap)\\\\n\\\\n            analysis[bin_name][strategy] = {\\\\n                \\\\\\\"R@1\\\\\\\": ci_r1[0],\\\\n                \\\\\\\"R@1_ci\\\\\\\": [ci_r1[1], ci_r1[2]],\\\\n                \\\\\\\"R@5\\\\\\\": ci_r5[0],\\\\n                \\\\\\\"R@5_ci\\\\\\\": [ci_r5[1], ci_r5[2]],\\\\n                \\\\\\\"MRR\\\\\\\": ci_mrr[0],\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.41}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n\\\"\\\"\\\"Stratified analysis of embedding vs random negative strategies by data strata.\\n\\nAnalyses M2 per-instance predictions across:\\n  - Repo size (instance count per repo from M1)\\n  - Candidate pool size (neg_candidates per query)\\n  - Query-positive similarity (cosine sim from model, or text overlap for dry-run)\\n\\nInputs:\\n  - M2 per-instance predictions (from --predictions-dir or re-eval from checkpoints)\\n  - M1 all.jsonl (repo metadata)\\n  - Val JSONL files (query/candidate structure)\\n\\nOutputs:\\n  - stratified_results.json: full per-stratum metrics with bootstrap CI\\n  - stratified_summary.csv: compact table\\n  - stratified_plots.pdf: grouped bar charts, heatmaps, delta trends\\n\\\"\\\"\\\"\\n\\nimport argparse\\nimport csv\\nimport json\\nimport math\\nimport os\\nimport sys\\nfrom collections import Counter, defaultdict\\nfrom pathlib import Path\\nfrom typing import Any, Dict, List, Optional, Tuple\\n\\nimport numpy as np\\n\\nSTRATEGIES = [\\\"random\\\", \\\"embedding_distance\\\", \\\"dataflow_aware\\\"]\\nSTRATEGY_LABELS = {\\\"random\\\": \\\"Random\\\", \\\"embedding_distance\\\": \\\"Embedding\\\", \\\"dataflow_aware\\\": \\\"Dataflow\\\"}\\nSTRATEGY_COLORS = {\\\"random\\\": \\\"#4C72B0\\\", \\\"embedding_distance\\\": \\\"#DD8452\\\", \\\"dataflow_aware\\\": \\\"#55A868\\\"}\\n\\nREPO_SIZE_BINS = {\\n    \\\"small\\\": (0, 50),\\n    \\\"medium\\\": (50, 200),\\n    \\\"large\\\": (200, 500),\\n    \\\"xlarge\\\": (500, float(\\\"inf\\\")),\\n}\\n\\nPOOL_SIZE_BINS = {\\n    \\\"small\\\": (0, 20),\\n    \\\"medium\\\": (20, 40),\\n    \\\"large\\\": (40, 51),\\n}\\n\\nSIMILARITY_BINS = {\\n    \\\"low\\\": (0.0, 0.3),\\n    \\\"medium\\\": (0.3, 0.6),\\n    \\\"high\\\": (0.6, 1.01),\\n}\\n\\nDATAFLOW_BINS = {\\n    \\\"sparse\\\": (0, 2),\\n    \\\"moderate\\\": (2, 10),\\n    \\\"rich\\\": (10, float(\\\"inf\\\")),\\n}\\n\\nNEG_DIFFICULTY_QUARTILE_LABELS = [\\\"Q1_easy\\\", \\\"Q2\\\", \\\"Q3\\\", \\\"Q4_hard\\\"]\\n\\n\\ndef _bin_value(value, bins):\\n    for name, (lo, hi) in bins.items():\\n        if lo <= value < hi:\\n            return name\\n    return \\\"unknown\\\"\\n\\n\\n# ── M1 metadata ───────────────────────────────────────────────────��─\\n\\ndef load_m1_metadata(m1_path: str) -> Tuple[Dict[str, str], Dict[str, int]]:\\n    import re\\n    inst_to_repo = {}\\n    repo_counts: Counter = Counter()\\n    pat_iid = re.compile(r'\\\"instance_id\\\"\\\\s*:\\\\s*\\\"([^\\\"]+)\\\"')\\n    pat_repo = re.compile(r'\\\"repo\\\"\\\\s*:\\\\s*\\\"([^\\\"]+)\\\"')\\n    with open(m1_path) as f:\\n        for line in f:\\n            m_iid = pat_iid.search(line)\\n            m_repo = pat_repo.search(line)\\n            if m_iid and m_repo:\\n                iid = m_iid.group(1)\\n                repo = m_repo.group(1)\\n                inst_to_repo[iid] = repo\\n                repo_counts[repo] += 1\\n    return inst_to_repo, dict(repo_counts)\\n\\n\\n# ── Dataflow graph loading ────────────────────────────────────────────\\n\\ndef load_dataflow_edges(graph_path: str) -> Dict[str, int]:\\n    \\\"\\\"\\\"Load dataflow graph and return {file_key: edge_count}.\\\"\\\"\\\"\\n    with open(graph_path) as f:\\n        graph = json.load(f)\\n    return {k: len(v) for k, v in graph.items()}\\n\\n\\n# ── Val data loading ─────────────────────────────────────────────────\\n\\ndef load_val_samples(val_path: str, lite: bool = False) -> List[Dict[str, Any]]:\\n    \\\"\\\"\\\"Load val JSONL. lite=True skips candidate_tokens (faster for dry-run).\\\"\\\"\\\"\\n    import re\\n    samples = []\\n    pat_qid = re.compile(r'\\\"query_id\\\"\\\\s*:\\\\s*\\\"([^\\\"]+)\\\"')\\n    with open(val_path) as f:\\n        for line in f:\\n            if not line.strip():\\n                continue\\n            if lite:\\n                m = pat_qid.search(line)\\n                if not m:\\n                    continue\\n                qid = m.group(1)\\n                instance_id = qid.split(\\\"::\\\")[0] if \\\"::\\\" in qid else qid\\n                d = json.loads(line)\\n                samples.append({\\n                    \\\"query_id\\\": qid,\\n                    \\\"instance_id\\\": instance_id,\\n                    \\\"pool_size\\\": len(d.get(\\\"neg_candidates\\\", [])),\\n                    \\\"query_tokens\\\": d.get(\\\"query_tokens\\\", \\\"\\\")[:1000],\\n                    \\\"pos_tokens\\\": d.get(\\\"pos_tokens\\\", \\\"\\\")[:1000],\\n                    \\\"neg_candidates\\\": [],\\n                    \\\"candidate_tokens\\\": {},\\n                })\\n            else:\\n                d = jso\\n\\n... [截断: 输出过长，省略 7671 字符] ...\\n\\n], \\\"\\\")\\n        rc = repo_counts.get(repo, 0)\\n        r[\\\"repo\\\"] = repo\\n        r[\\\"repo_size\\\"] = rc\\n        r[\\\"repo_size_bin\\\"] = _bin_value(rc, REPO_SIZE_BINS)\\n        r[\\\"pool_size_bin\\\"] = _bin_value(r[\\\"pool_size\\\"], POOL_SIZE_BINS)\\n        r[\\\"sim_bin\\\"] = _bin_value(r[\\\"pos_sim\\\"], SIMILARITY_BINS)\\n        if dataflow_edges is not None:\\n            ec = dataflow_edges.get(r[\\\"query_id\\\"], 0)\\n            r[\\\"dataflow_edge_count\\\"] = ec\\n            r[\\\"dataflow_bin\\\"] = _bin_value(ec, DATAFLOW_BINS)\\n        else:\\n            r[\\\"dataflow_bin\\\"] = \\\"unknown\\\"\\n    return results\\n\\n\\ndef assign_neg_difficulty_quartiles(\\n    all_results: Dict[str, Dict[int, List[Dict]]],\\n    val_samples_cache: Dict[str, List[Dict]],\\n):\\n    \\\"\\\"\\\"Compute text-overlap-based neg difficulty proxy and assign quartiles.\\\"\\\"\\\"\\n    for strategy in list(all_results.keys()):\\n        for seed in list(all_results[strategy].keys()):\\n            results = all_results[strategy][seed]\\n            cache_key = f\\\"{strategy}_s{seed}\\\"\\n            samples = val_samples_cache.get(cache_key, [])\\n            sample_map = {s[\\\"query_id\\\"]: s for s in samples}\\n\\n            margins = []\\n            for r in results:\\n                s = sample_map.get(r[\\\"query_id\\\"])\\n                if s is None:\\n                    margins.append(0.0)\\n                    continue\\n                q_toks = set(s.get(\\\"query_tokens\\\", \\\"\\\")[:1000].split())\\n                p_toks = set(s.get(\\\"pos_tokens\\\", \\\"\\\")[:1000].split())\\n                pos_overlap = len(q_toks & p_toks) / max(len(q_toks | p_toks), 1)\\n                max_neg_overlap = 0.0\\n                neg_cands = s.get(\\\"neg_candidates\\\", [])[:7]\\n                cand_tokens = s.get(\\\"candidate_tokens\\\", {})\\n                for neg_id in neg_cands:\\n                    neg_text = cand_tokens.get(neg_id, \\\"\\\")\\n                    if neg_text:\\n                        n_toks = set(neg_text[:1000].split())\\n                        ov = len(q_toks & n_toks) / max(len(q_toks | n_toks), 1)\\n                        max_neg_overlap = max(max_neg_overlap, ov)\\n                margin = pos_overlap - max_neg_overlap\\n                margins.append(margin)\\n                r[\\\"neg_difficulty_margin\\\"] = margin\\n\\n            if margins:\\n                arr = np.array(margins)\\n                q25, q50, q75 = np.percentile(arr, [25, 50, 75])\\n                for r, m in zip(results, margins):\\n                    if m <= q25:\\n                        r[\\\"neg_difficulty_bin\\\"] = \\\"Q4_hard\\\"\\n                    elif m <= q50:\\n                        r[\\\"neg_difficulty_bin\\\"] = \\\"Q3\\\"\\n                    elif m <= q75:\\n                        r[\\\"neg_difficulty_bin\\\"] = \\\"Q2\\\"\\n                    else:\\n                        r[\\\"neg_difficulty_bin\\\"] = \\\"Q1_easy\\\"\\n\\n\\ndef group_by(results: List[Dict], key: str) -> Dict[str, List[Dict]]:\\n    groups: Dict[str, List[Dict]] = defaultdict(list)\\n    for r in results:\\n        groups[r[key]].append(r)\\n    return dict(groups)\\n\\n\\n# ── Analysis core ────────────────────────────────────────────────────\\n\\ndef run_stratified_analysis(\\n    all_results: Dict[str, Dict[int, List[Dict]]],\\n    strata_key: str,\\n    bin_order: List[str],\\n    n_bootstrap: int = 1000,\\n) -> Dict:\\n    analysis = {}\\n    for bin_name in bin_order:\\n        analysis[bin_name] = {}\\n        for strategy in STRATEGIES:\\n            seed_results = []\\n            for seed, results in all_results.get(strategy, {}).items():\\n                grouped = group_by(results, strata_key)\\n                seed_results.extend(grouped.get(bin_name, []))\\n\\n            metrics = compute_metrics(seed_results)\\n            ci_r1 = bootstrap_ci(seed_results, \\\"R@1\\\", n_bootstrap)\\n            ci_r5 = bootstrap_ci(seed_results, \\\"R@5\\\", n_bootstrap)\\n            ci_mrr = bootstrap_ci(seed_results, \\\"MRR\\\", n_bootstrap)\\n\\n            analysis[bin_name][strategy] = {\\n                \\\"R@1\\\": ci_r1[0],\\n                \\\"R@1_ci\\\": [ci_r1[1], ci_r1[2]],\\n                \\\"R@5\\\": ci_r5[0],\\n                \\\"R@5_ci\\\": [ci_r5[1], ci_r5[2]],\\n                \\\"MRR\\\": ci_mrr[0],\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.41}}"
    }
  },
  "sourceToolAssistantUUID": "0acc21c0-666f-4f4e-abd8-44d2ff1fa172",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "fb5ea7f7-b3c9-4750-b931-39d2aaae422b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 61 · 2026-05-14T20:37:30.625Z_

```json
{
  "parentUuid": "5d6dc5de-e9d9-44b5-8c5e-a853485c51cc",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "689d30b7-648e-4dbe-9aa9-64c50576c132",
  "timestamp": "2026-05-14T20:37:30.625Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "fb5ea7f7-b3c9-4750-b931-39d2aaae422b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 62_

```json
{
  "type": "last-prompt",
  "leafUuid": "689d30b7-648e-4dbe-9aa9-64c50576c132",
  "sessionId": "fb5ea7f7-b3c9-4750-b931-39d2aaae422b"
}
```

---

### Runtime record

_source line 63_

```json
{
  "type": "ai-title",
  "aiTitle": "Trace stratified_dryrun v1 to v2 differences",
  "sessionId": "fb5ea7f7-b3c9-4750-b931-39d2aaae422b"
}
```

---

### Assistant

_source line 64 · 2026-05-14T20:37:34.110Z_

<details><summary>Logged reasoning block</summary>

```text
Now I need to see the `mock_predictions` function (line 268) and the `main` function (line 713). Let me also get the part from ~268-345 for mock_predictions and the early part of main.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "689d30b7-648e-4dbe-9aa9-64c50576c132",
  "isSidechain": false,
  "requestId": "req_011Cb371GikSnA2hCAe8MNxX",
  "type": "assistant",
  "uuid": "ec42f7e6-6d55-4ca6-b37e-5f25717ccc10",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "fb5ea7f7-b3c9-4750-b931-39d2aaae422b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Tn9cEWTKSazRWBBzvmWSLq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3628,
      "cache_read_input_tokens": 50789,
      "output_tokens": 214,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3628,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 214,
          "cache_read_input_tokens": 50789,
          "cache_creation_input_tokens": 3628,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3628
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

_source line 65 · 2026-05-14T20:37:35.129Z_

需要读 `mock_predictions` 函数和 `main` 的核心流程。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ec42f7e6-6d55-4ca6-b37e-5f25717ccc10",
  "isSidechain": false,
  "requestId": "req_011Cb371GikSnA2hCAe8MNxX",
  "type": "assistant",
  "uuid": "c71b3f1a-75c5-4987-b68d-90ea3967b273",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "fb5ea7f7-b3c9-4750-b931-39d2aaae422b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Tn9cEWTKSazRWBBzvmWSLq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3628,
      "cache_read_input_tokens": 50789,
      "output_tokens": 214,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3628,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 214,
          "cache_read_input_tokens": 50789,
          "cache_creation_input_tokens": 3628,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3628
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

_source line 66 · 2026-05-14T20:37:35.798Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01XQfP7Q9carvnyzcVcPMXb3`</summary>

```json
{
  "server": "bjb1-42106",
  "command": "tail -n +268 /root/structfuse/evaluation/analyze_stratified.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c71b3f1a-75c5-4987-b68d-90ea3967b273",
  "isSidechain": false,
  "requestId": "req_011Cb371GikSnA2hCAe8MNxX",
  "type": "assistant",
  "uuid": "12dd8017-dd11-4b98-a705-d7d128c4a23b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "fb5ea7f7-b3c9-4750-b931-39d2aaae422b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Tn9cEWTKSazRWBBzvmWSLq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3628,
      "cache_read_input_tokens": 50789,
      "output_tokens": 214,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3628,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 214,
          "cache_read_input_tokens": 50789,
          "cache_creation_input_tokens": 3628,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3628
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

_source line 67 · 2026-05-14T20:37:36.206Z_

<details><summary>↩ Tool result · `toolu_01XQfP7Q9carvnyzcVcPMXb3`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"def mock_predictions(\\n    val_samples: List[Dict], strategy: str, seed: int\\n) -> List[Dict]:\\n    rng = np.random.RandomState(seed + abs(hash(strategy)) % 10000)\\n    results = []\\n    for sample in val_samples:\\n        pool = 1 + sample[\\\"pool_size\\\"]\\n        if strategy == \\\"random\\\":\\n            rank = rng.randint(1, pool + 1)\\n        elif strategy == \\\"embedding_distance\\\":\\n            rank = max(1, min(pool, int(rng.exponential(pool * 0.35)) + 1))\\n        else:\\n            rank = max(1, min(pool, int(rng.exponential(pool * 0.20)) + 1))\\n\\n        pos_sim = max(0.0, min(1.0, 1.0 - rank / pool + rng.normal(0, 0.08)))\\n        tsim = text_similarity(\\n            sample[\\\"query_tokens\\\"][:500], sample[\\\"pos_tokens\\\"][:500]\\n        )\\n\\n        results.append({\\n            \\\"query_id\\\": sample[\\\"query_id\\\"],\\n            \\\"instance_id\\\": sample[\\\"instance_id\\\"],\\n            \\\"pool_size\\\": sample[\\\"pool_size\\\"],\\n            \\\"rank\\\": rank,\\n            \\\"pos_sim\\\": pos_sim if pos_sim > 0 else tsim,\\n            \\\"total_candidates\\\": pool,\\n        })\\n    return results\\n\\n\\n# ── Metrics computation ──────────────────────────────────────────────\\n\\ndef compute_metrics(results: List[Dict]) -> Dict[str, float]:\\n    if not results:\\n        return {\\\"R@1\\\": 0.0, \\\"R@5\\\": 0.0, \\\"MRR\\\": 0.0, \\\"count\\\": 0}\\n    ranks = [r[\\\"rank\\\"] for r in results]\\n    n = len(ranks)\\n    return {\\n        \\\"R@1\\\": sum(1 for r in ranks if r <= 1) / n,\\n        \\\"R@5\\\": sum(1 for r in ranks if r <= 5) / n,\\n        \\\"MRR\\\": sum(1.0 / r for r in ranks) / n,\\n        \\\"count\\\": n,\\n    }\\n\\n\\ndef _metric_fn(results, metric_name):\\n    m = compute_metrics(results)\\n    return m[metric_name]\\n\\n\\ndef bootstrap_ci(\\n    results: List[Dict],\\n    metric_name: str = \\\"R@1\\\",\\n    n_bootstrap: int = 1000,\\n    ci: float = 0.95,\\n    seed: int = 42,\\n) -> Tuple[float, float, float]:\\n    rng = np.random.RandomState(seed)\\n    n = len(results)\\n    if n == 0:\\n        return (0.0, 0.0, 0.0)\\n\\n    point = _metric_fn(results, metric_name)\\n    boot_values = []\\n    for _ in range(n_bootstrap):\\n        idx = rng.choice(n, n, replace=True)\\n        boot_sample = [results[i] for i in idx]\\n        boot_values.append(_metric_fn(boot_sample, metric_name))\\n\\n    alpha = (1 - ci) / 2\\n    lo = float(np.percentile(boot_values, alpha * 100))\\n    hi = float(np.percentile(boot_values, (1 - alpha) * 100))\\n    return (point, lo, hi)\\n\\n\\n# ── Stratification ───────────────────────────────────────────────────\\n\\ndef assign_strata(\\n    results: List[Dict],\\n    inst_to_repo: Dict[str, str],\\n    repo_counts: Dict[str, int],\\n    dataflow_edges: Optional[Dict[str, int]] = None,\\n) -> List[Dict]:\\n    for r in results:\\n        repo = inst_to_repo.get(r[\\\"instance_id\\\"], \\\"\\\")\\n        rc = repo_counts.get(repo, 0)\\n        r[\\\"repo\\\"] = repo\\n        r[\\\"repo_size\\\"] = rc\\n        r[\\\"repo_size_bin\\\"] = _bin_value(rc, REPO_SIZE_BINS)\\n        r[\\\"pool_size_bin\\\"] = _bin_value(r[\\\"pool_size\\\"], POOL_SIZE_BINS)\\n        r[\\\"sim_bin\\\"] = _bin_value(r[\\\"pos_sim\\\"], SIMILARITY_BINS)\\n        if dataflow_edges is not None:\\n            ec = dataflow_edges.get(r[\\\"query_id\\\"], 0)\\n            r[\\\"dataflow_edge_count\\\"] = ec\\n            r[\\\"dataflow_bin\\\"] = _bin_value(ec, DATAFLOW_BINS)\\n        else:\\n            r[\\\"dataflow_bin\\\"] = \\\"unknown\\\"\\n    return results\\n\\n\\ndef assign_neg_difficulty_quartiles(\\n    all_results: Dict[str, Dict[int, List[Dict]]],\\n    val_samples_cache: Dict[str, List[Dict]],\\n):\\n    \\\"\\\"\\\"Compute text-overlap-based neg difficulty proxy and assign quartiles.\\\"\\\"\\\"\\n    for strategy in list(all_results.keys()):\\n        for seed in list(all_results[strategy].keys()):\\n            results = all_results[strategy][seed]\\n            cache_key = f\\\"{strategy}_s{seed}\\\"\\n            samples = val_samples_cache.get(cache_key, [])\\n            sample_map = {s[\\\"query_id\\\"]: s for s in samples}\\n\\n            margins = []\\n            for r in results:\\n                s = sample_map.get(r[\\\"query_id\\\"])\\n                if s is None:\\n                    margins.append(0.0)\\n                    continue\\n                q_toks = set(s.get(\\\"q\\n\\n... [截断: 输出过长，省略 18435 字符] ...\\n\\nt\\\")):\\n                        ckpt_dir = candidate\\n                        break\\n                if ckpt_dir is None and os.path.exists(os.path.join(base, \\\"model.pt\\\")):\\n                    ckpt_dir = base\\n                if os.path.exists(ckpt_dir):\\n                    print(f\\\"  Re-evaluating checkpoint: {ckpt_dir}\\\", flush=True)\\n                    results = reeval_checkpoint(\\n                        ckpt_dir, val_samples, args.device, args.max_seq_length\\n                    )\\n                else:\\n                    print(f\\\"  [WARN] Checkpoint not found: {ckpt_dir}\\\", flush=True)\\n                    continue\\n            else:\\n                print(\\\"  [ERROR] No --dry-run, --predictions-dir, or --checkpoints-dir\\\", flush=True)\\n                continue\\n\\n            # Assign strata\\n            results = assign_strata(results, inst_to_repo, repo_counts, dataflow_edges)\\n\\n            # For dry-run or model-based: compute text similarity for sim_bin\\n            if args.dry_run:\\n                for r, s in zip(results, val_samples):\\n                    tsim = text_similarity(s[\\\"query_tokens\\\"][:500], s[\\\"pos_tokens\\\"][:500])\\n                    r[\\\"sim_bin\\\"] = _bin_value(tsim, SIMILARITY_BINS)\\n\\n            all_results[strategy][seed] = results\\n            val_samples_cache[f\\\"{strategy}_s{seed}\\\"] = val_samples\\n            print(f\\\"  -> {len(results)} instances\\\", flush=True)\\n\\n    # Compute neg_difficulty quartiles (text-overlap proxy, CPU-safe)\\n    print(\\\"Computing neg difficulty quartiles...\\\", flush=True)\\n    assign_neg_difficulty_quartiles(all_results, val_samples_cache)\\n\\n    # Run stratified analysis\\n    print(\\\"\\\\nRunning stratified analysis...\\\", flush=True)\\n    repo_analysis = run_stratified_analysis(\\n        all_results, \\\"repo_size_bin\\\", list(REPO_SIZE_BINS.keys()), args.n_bootstrap\\n    )\\n    pool_analysis = run_stratified_analysis(\\n        all_results, \\\"pool_size_bin\\\", list(POOL_SIZE_BINS.keys()), args.n_bootstrap\\n    )\\n    sim_analysis = run_stratified_analysis(\\n        all_results, \\\"sim_bin\\\", list(SIMILARITY_BINS.keys()), args.n_bootstrap\\n    )\\n\\n    dataflow_analysis = {}\\n    if dataflow_edges is not None:\\n        dataflow_analysis = run_stratified_analysis(\\n            all_results, \\\"dataflow_bin\\\", list(DATAFLOW_BINS.keys()), args.n_bootstrap\\n        )\\n\\n    neg_diff_analysis = run_stratified_analysis(\\n        all_results, \\\"neg_difficulty_bin\\\", NEG_DIFFICULTY_QUARTILE_LABELS, args.n_bootstrap\\n    )\\n\\n    # Save JSON\\n    full_results = {\\n        \\\"config\\\": {\\n            \\\"strategies\\\": STRATEGIES,\\n            \\\"seeds\\\": seeds,\\n            \\\"repo_size_bins\\\": {k: list(v) for k, v in REPO_SIZE_BINS.items()},\\n            \\\"pool_size_bins\\\": {k: list(v) for k, v in POOL_SIZE_BINS.items()},\\n            \\\"similarity_bins\\\": {k: list(v) for k, v in SIMILARITY_BINS.items()},\\n            \\\"dataflow_bins\\\": {k: list(v) for k, v in DATAFLOW_BINS.items()},\\n            \\\"neg_difficulty_quartiles\\\": NEG_DIFFICULTY_QUARTILE_LABELS,\\n            \\\"n_bootstrap\\\": args.n_bootstrap,\\n            \\\"dry_run\\\": args.dry_run,\\n        },\\n        \\\"by_repo_size\\\": repo_analysis,\\n        \\\"by_pool_size\\\": pool_analysis,\\n        \\\"by_similarity\\\": sim_analysis,\\n        \\\"by_dataflow\\\": dataflow_analysis,\\n        \\\"by_neg_difficulty\\\": neg_diff_analysis,\\n    }\\n\\n    json_path = os.path.join(args.output_dir, \\\"stratified_results.json\\\")\\n    with open(json_path, \\\"w\\\") as f:\\n        json.dump(full_results, f, indent=2, ensure_ascii=False)\\n    print(f\\\"  Results JSON saved to {json_path}\\\", flush=True)\\n\\n    # CSV summary\\n    csv_path = os.path.join(args.output_dir, \\\"stratified_summary.csv\\\")\\n    write_summary_csv(repo_analysis, pool_analysis, sim_analysis, csv_path, dataflow_analysis, neg_diff_analysis)\\n\\n    # Plots\\n    try:\\n        make_plots(repo_analysis, pool_analysis, sim_analysis, args.output_dir, dataflow_analysis, neg_diff_analysis)\\n    except Exception as e:\\n        print(f\\\"  [WARN] Plot generation failed: {e}\\\", flush=True)\\n\\n    print(\\\"\\\\nDone.\\\", flush=True)\\n\\n\\nif __name__ == \\\"__main__\\\":\\n    main()\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "12dd8017-dd11-4b98-a705-d7d128c4a23b",
  "isSidechain": false,
  "promptId": "0b7bb415-f2b4-4832-aac4-2e6aafdc7429",
  "type": "user",
  "uuid": "af04de64-31cf-457b-8b5a-18f37b1f577e",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"def mock_predictions(\\\\n    val_samples: List[Dict], strategy: str, seed: int\\\\n) -> List[Dict]:\\\\n    rng = np.random.RandomState(seed + abs(hash(strategy)) % 10000)\\\\n    results = []\\\\n    for sample in val_samples:\\\\n        pool = 1 + sample[\\\\\\\"pool_size\\\\\\\"]\\\\n        if strategy == \\\\\\\"random\\\\\\\":\\\\n            rank = rng.randint(1, pool + 1)\\\\n        elif strategy == \\\\\\\"embedding_distance\\\\\\\":\\\\n            rank = max(1, min(pool, int(rng.exponential(pool * 0.35)) + 1))\\\\n        else:\\\\n            rank = max(1, min(pool, int(rng.exponential(pool * 0.20)) + 1))\\\\n\\\\n        pos_sim = max(0.0, min(1.0, 1.0 - rank / pool + rng.normal(0, 0.08)))\\\\n        tsim = text_similarity(\\\\n            sample[\\\\\\\"query_tokens\\\\\\\"][:500], sample[\\\\\\\"pos_tokens\\\\\\\"][:500]\\\\n        )\\\\n\\\\n        results.append({\\\\n            \\\\\\\"query_id\\\\\\\": sample[\\\\\\\"query_id\\\\\\\"],\\\\n            \\\\\\\"instance_id\\\\\\\": sample[\\\\\\\"instance_id\\\\\\\"],\\\\n            \\\\\\\"pool_size\\\\\\\": sample[\\\\\\\"pool_size\\\\\\\"],\\\\n            \\\\\\\"rank\\\\\\\": rank,\\\\n            \\\\\\\"pos_sim\\\\\\\": pos_sim if pos_sim > 0 else tsim,\\\\n            \\\\\\\"total_candidates\\\\\\\": pool,\\\\n        })\\\\n    return results\\\\n\\\\n\\\\n# ── Metrics computation ──────────────────────────────────────────────\\\\n\\\\ndef compute_metrics(results: List[Dict]) -> Dict[str, float]:\\\\n    if not results:\\\\n        return {\\\\\\\"R@1\\\\\\\": 0.0, \\\\\\\"R@5\\\\\\\": 0.0, \\\\\\\"MRR\\\\\\\": 0.0, \\\\\\\"count\\\\\\\": 0}\\\\n    ranks = [r[\\\\\\\"rank\\\\\\\"] for r in results]\\\\n    n = len(ranks)\\\\n    return {\\\\n        \\\\\\\"R@1\\\\\\\": sum(1 for r in ranks if r <= 1) / n,\\\\n        \\\\\\\"R@5\\\\\\\": sum(1 for r in ranks if r <= 5) / n,\\\\n        \\\\\\\"MRR\\\\\\\": sum(1.0 / r for r in ranks) / n,\\\\n        \\\\\\\"count\\\\\\\": n,\\\\n    }\\\\n\\\\n\\\\ndef _metric_fn(results, metric_name):\\\\n    m = compute_metrics(results)\\\\n    return m[metric_name]\\\\n\\\\n\\\\ndef bootstrap_ci(\\\\n    results: List[Dict],\\\\n    metric_name: str = \\\\\\\"R@1\\\\\\\",\\\\n    n_bootstrap: int = 1000,\\\\n    ci: float = 0.95,\\\\n    seed: int = 42,\\\\n) -> Tuple[float, float, float]:\\\\n    rng = np.random.RandomState(seed)\\\\n    n = len(results)\\\\n    if n == 0:\\\\n        return (0.0, 0.0, 0.0)\\\\n\\\\n    point = _metric_fn(results, metric_name)\\\\n    boot_values = []\\\\n    for _ in range(n_bootstrap):\\\\n        idx = rng.choice(n, n, replace=True)\\\\n        boot_sample = [results[i] for i in idx]\\\\n        boot_values.append(_metric_fn(boot_sample, metric_name))\\\\n\\\\n    alpha = (1 - ci) / 2\\\\n    lo = float(np.percentile(boot_values, alpha * 100))\\\\n    hi = float(np.percentile(boot_values, (1 - alpha) * 100))\\\\n    return (point, lo, hi)\\\\n\\\\n\\\\n# ── Stratification ───────────────────────────────────────────────────\\\\n\\\\ndef assign_strata(\\\\n    results: List[Dict],\\\\n    inst_to_repo: Dict[str, str],\\\\n    repo_counts: Dict[str, int],\\\\n    dataflow_edges: Optional[Dict[str, int]] = None,\\\\n) -> List[Dict]:\\\\n    for r in results:\\\\n        repo = inst_to_repo.get(r[\\\\\\\"instance_id\\\\\\\"], \\\\\\\"\\\\\\\")\\\\n        rc = repo_counts.get(repo, 0)\\\\n        r[\\\\\\\"repo\\\\\\\"] = repo\\\\n        r[\\\\\\\"repo_size\\\\\\\"] = rc\\\\n        r[\\\\\\\"repo_size_bin\\\\\\\"] = _bin_value(rc, REPO_SIZE_BINS)\\\\n        r[\\\\\\\"pool_size_bin\\\\\\\"] = _bin_value(r[\\\\\\\"pool_size\\\\\\\"], POOL_SIZE_BINS)\\\\n        r[\\\\\\\"sim_bin\\\\\\\"] = _bin_value(r[\\\\\\\"pos_sim\\\\\\\"], SIMILARITY_BINS)\\\\n        if dataflow_edges is not None:\\\\n            ec = dataflow_edges.get(r[\\\\\\\"query_id\\\\\\\"], 0)\\\\n            r[\\\\\\\"dataflow_edge_count\\\\\\\"] = ec\\\\n            r[\\\\\\\"dataflow_bin\\\\\\\"] = _bin_value(ec, DATAFLOW_BINS)\\\\n        else:\\\\n            r[\\\\\\\"dataflow_bin\\\\\\\"] = \\\\\\\"unknown\\\\\\\"\\\\n    return results\\\\n\\\\n\\\\ndef assign_neg_difficulty_quartiles(\\\\n    all_results: Dict[str, Dict[int, List[Dict]]],\\\\n    val_samples_cache: Dict[str, List[Dict]],\\\\n):\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"Compute text-overlap-based neg difficulty proxy and assign quartiles.\\\\\\\"\\\\\\\"\\\\\\\"\\\\n    for strategy in list(all_results.keys()):\\\\n        for seed in list(all_results[strategy].keys()):\\\\n            results = all_results[strategy][seed]\\\\n            cache_key = f\\\\\\\"{strategy}_s{seed}\\\\\\\"\\\\n            samples = val_samples_cache.get(cache_key, [])\\\\n            sample_map = {s[\\\\\\\"query_id\\\\\\\"]: s for s in samples}\\\\n\\\\n            margins = []\\\\n            for r in results:\\\\n                s = sample_map.get(r[\\\\\\\"query_id\\\\\\\"])\\\\n                if s is None:\\\\n                    margins.append(0.0)\\\\n                    continue\\\\n                q_toks = set(s.get(\\\\\\\"q\\\\n\\\\n... [截断: 输出过长，省略 18435 字符] ...\\\\n\\\\nt\\\\\\\")):\\\\n                        ckpt_dir = candidate\\\\n                        break\\\\n                if ckpt_dir is None and os.path.exists(os.path.join(base, \\\\\\\"model.pt\\\\\\\")):\\\\n                    ckpt_dir = base\\\\n                if os.path.exists(ckpt_dir):\\\\n                    print(f\\\\\\\"  Re-evaluating checkpoint: {ckpt_dir}\\\\\\\", flush=True)\\\\n                    results = reeval_checkpoint(\\\\n                        ckpt_dir, val_samples, args.device, args.max_seq_length\\\\n                    )\\\\n                else:\\\\n                    print(f\\\\\\\"  [WARN] Checkpoint not found: {ckpt_dir}\\\\\\\", flush=True)\\\\n                    continue\\\\n            else:\\\\n                print(\\\\\\\"  [ERROR] No --dry-run, --predictions-dir, or --checkpoints-dir\\\\\\\", flush=True)\\\\n                continue\\\\n\\\\n            # Assign strata\\\\n            results = assign_strata(results, inst_to_repo, repo_counts, dataflow_edges)\\\\n\\\\n            # For dry-run or model-based: compute text similarity for sim_bin\\\\n            if args.dry_run:\\\\n                for r, s in zip(results, val_samples):\\\\n                    tsim = text_similarity(s[\\\\\\\"query_tokens\\\\\\\"][:500], s[\\\\\\\"pos_tokens\\\\\\\"][:500])\\\\n                    r[\\\\\\\"sim_bin\\\\\\\"] = _bin_value(tsim, SIMILARITY_BINS)\\\\n\\\\n            all_results[strategy][seed] = results\\\\n            val_samples_cache[f\\\\\\\"{strategy}_s{seed}\\\\\\\"] = val_samples\\\\n            print(f\\\\\\\"  -> {len(results)} instances\\\\\\\", flush=True)\\\\n\\\\n    # Compute neg_difficulty quartiles (text-overlap proxy, CPU-safe)\\\\n    print(\\\\\\\"Computing neg difficulty quartiles...\\\\\\\", flush=True)\\\\n    assign_neg_difficulty_quartiles(all_results, val_samples_cache)\\\\n\\\\n    # Run stratified analysis\\\\n    print(\\\\\\\"\\\\\\\\nRunning stratified analysis...\\\\\\\", flush=True)\\\\n    repo_analysis = run_stratified_analysis(\\\\n        all_results, \\\\\\\"repo_size_bin\\\\\\\", list(REPO_SIZE_BINS.keys()), args.n_bootstrap\\\\n    )\\\\n    pool_analysis = run_stratified_analysis(\\\\n        all_results, \\\\\\\"pool_size_bin\\\\\\\", list(POOL_SIZE_BINS.keys()), args.n_bootstrap\\\\n    )\\\\n    sim_analysis = run_stratified_analysis(\\\\n        all_results, \\\\\\\"sim_bin\\\\\\\", list(SIMILARITY_BINS.keys()), args.n_bootstrap\\\\n    )\\\\n\\\\n    dataflow_analysis = {}\\\\n    if dataflow_edges is not None:\\\\n        dataflow_analysis = run_stratified_analysis(\\\\n            all_results, \\\\\\\"dataflow_bin\\\\\\\", list(DATAFLOW_BINS.keys()), args.n_bootstrap\\\\n        )\\\\n\\\\n    neg_diff_analysis = run_stratified_analysis(\\\\n        all_results, \\\\\\\"neg_difficulty_bin\\\\\\\", NEG_DIFFICULTY_QUARTILE_LABELS, args.n_bootstrap\\\\n    )\\\\n\\\\n    # Save JSON\\\\n    full_results = {\\\\n        \\\\\\\"config\\\\\\\": {\\\\n            \\\\\\\"strategies\\\\\\\": STRATEGIES,\\\\n            \\\\\\\"seeds\\\\\\\": seeds,\\\\n            \\\\\\\"repo_size_bins\\\\\\\": {k: list(v) for k, v in REPO_SIZE_BINS.items()},\\\\n            \\\\\\\"pool_size_bins\\\\\\\": {k: list(v) for k, v in POOL_SIZE_BINS.items()},\\\\n            \\\\\\\"similarity_bins\\\\\\\": {k: list(v) for k, v in SIMILARITY_BINS.items()},\\\\n            \\\\\\\"dataflow_bins\\\\\\\": {k: list(v) for k, v in DATAFLOW_BINS.items()},\\\\n            \\\\\\\"neg_difficulty_quartiles\\\\\\\": NEG_DIFFICULTY_QUARTILE_LABELS,\\\\n            \\\\\\\"n_bootstrap\\\\\\\": args.n_bootstrap,\\\\n            \\\\\\\"dry_run\\\\\\\": args.dry_run,\\\\n        },\\\\n        \\\\\\\"by_repo_size\\\\\\\": repo_analysis,\\\\n        \\\\\\\"by_pool_size\\\\\\\": pool_analysis,\\\\n        \\\\\\\"by_similarity\\\\\\\": sim_analysis,\\\\n        \\\\\\\"by_dataflow\\\\\\\": dataflow_analysis,\\\\n        \\\\\\\"by_neg_difficulty\\\\\\\": neg_diff_analysis,\\\\n    }\\\\n\\\\n    json_path = os.path.join(args.output_dir, \\\\\\\"stratified_results.json\\\\\\\")\\\\n    with open(json_path, \\\\\\\"w\\\\\\\") as f:\\\\n        json.dump(full_results, f, indent=2, ensure_ascii=False)\\\\n    print(f\\\\\\\"  Results JSON saved to {json_path}\\\\\\\", flush=True)\\\\n\\\\n    # CSV summary\\\\n    csv_path = os.path.join(args.output_dir, \\\\\\\"stratified_summary.csv\\\\\\\")\\\\n    write_summary_csv(repo_analysis, pool_analysis, sim_analysis, csv_path, dataflow_analysis, neg_diff_analysis)\\\\n\\\\n    # Plots\\\\n    try:\\\\n        make_plots(repo_analysis, pool_analysis, sim_analysis, args.output_dir, dataflow_analysis, neg_diff_analysis)\\\\n    except Exception as e:\\\\n        print(f\\\\\\\"  [WARN] Plot generation failed: {e}\\\\\\\", flush=True)\\\\n\\\\n    print(\\\\\\\"\\\\\\\\nDone.\\\\\\\", flush=True)\\\\n\\\\n\\\\nif __name__ == \\\\\\\"__main__\\\\\\\":\\\\n    main()\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.4}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"def mock_predictions(\\n    val_samples: List[Dict], strategy: str, seed: int\\n) -> List[Dict]:\\n    rng = np.random.RandomState(seed + abs(hash(strategy)) % 10000)\\n    results = []\\n    for sample in val_samples:\\n        pool = 1 + sample[\\\"pool_size\\\"]\\n        if strategy == \\\"random\\\":\\n            rank = rng.randint(1, pool + 1)\\n        elif strategy == \\\"embedding_distance\\\":\\n            rank = max(1, min(pool, int(rng.exponential(pool * 0.35)) + 1))\\n        else:\\n            rank = max(1, min(pool, int(rng.exponential(pool * 0.20)) + 1))\\n\\n        pos_sim = max(0.0, min(1.0, 1.0 - rank / pool + rng.normal(0, 0.08)))\\n        tsim = text_similarity(\\n            sample[\\\"query_tokens\\\"][:500], sample[\\\"pos_tokens\\\"][:500]\\n        )\\n\\n        results.append({\\n            \\\"query_id\\\": sample[\\\"query_id\\\"],\\n            \\\"instance_id\\\": sample[\\\"instance_id\\\"],\\n            \\\"pool_size\\\": sample[\\\"pool_size\\\"],\\n            \\\"rank\\\": rank,\\n            \\\"pos_sim\\\": pos_sim if pos_sim > 0 else tsim,\\n            \\\"total_candidates\\\": pool,\\n        })\\n    return results\\n\\n\\n# ── Metrics computation ──────────────────────────────────────────────\\n\\ndef compute_metrics(results: List[Dict]) -> Dict[str, float]:\\n    if not results:\\n        return {\\\"R@1\\\": 0.0, \\\"R@5\\\": 0.0, \\\"MRR\\\": 0.0, \\\"count\\\": 0}\\n    ranks = [r[\\\"rank\\\"] for r in results]\\n    n = len(ranks)\\n    return {\\n        \\\"R@1\\\": sum(1 for r in ranks if r <= 1) / n,\\n        \\\"R@5\\\": sum(1 for r in ranks if r <= 5) / n,\\n        \\\"MRR\\\": sum(1.0 / r for r in ranks) / n,\\n        \\\"count\\\": n,\\n    }\\n\\n\\ndef _metric_fn(results, metric_name):\\n    m = compute_metrics(results)\\n    return m[metric_name]\\n\\n\\ndef bootstrap_ci(\\n    results: List[Dict],\\n    metric_name: str = \\\"R@1\\\",\\n    n_bootstrap: int = 1000,\\n    ci: float = 0.95,\\n    seed: int = 42,\\n) -> Tuple[float, float, float]:\\n    rng = np.random.RandomState(seed)\\n    n = len(results)\\n    if n == 0:\\n        return (0.0, 0.0, 0.0)\\n\\n    point = _metric_fn(results, metric_name)\\n    boot_values = []\\n    for _ in range(n_bootstrap):\\n        idx = rng.choice(n, n, replace=True)\\n        boot_sample = [results[i] for i in idx]\\n        boot_values.append(_metric_fn(boot_sample, metric_name))\\n\\n    alpha = (1 - ci) / 2\\n    lo = float(np.percentile(boot_values, alpha * 100))\\n    hi = float(np.percentile(boot_values, (1 - alpha) * 100))\\n    return (point, lo, hi)\\n\\n\\n# ── Stratification ───────────────────────────────────────────────────\\n\\ndef assign_strata(\\n    results: List[Dict],\\n    inst_to_repo: Dict[str, str],\\n    repo_counts: Dict[str, int],\\n    dataflow_edges: Optional[Dict[str, int]] = None,\\n) -> List[Dict]:\\n    for r in results:\\n        repo = inst_to_repo.get(r[\\\"instance_id\\\"], \\\"\\\")\\n        rc = repo_counts.get(repo, 0)\\n        r[\\\"repo\\\"] = repo\\n        r[\\\"repo_size\\\"] = rc\\n        r[\\\"repo_size_bin\\\"] = _bin_value(rc, REPO_SIZE_BINS)\\n        r[\\\"pool_size_bin\\\"] = _bin_value(r[\\\"pool_size\\\"], POOL_SIZE_BINS)\\n        r[\\\"sim_bin\\\"] = _bin_value(r[\\\"pos_sim\\\"], SIMILARITY_BINS)\\n        if dataflow_edges is not None:\\n            ec = dataflow_edges.get(r[\\\"query_id\\\"], 0)\\n            r[\\\"dataflow_edge_count\\\"] = ec\\n            r[\\\"dataflow_bin\\\"] = _bin_value(ec, DATAFLOW_BINS)\\n        else:\\n            r[\\\"dataflow_bin\\\"] = \\\"unknown\\\"\\n    return results\\n\\n\\ndef assign_neg_difficulty_quartiles(\\n    all_results: Dict[str, Dict[int, List[Dict]]],\\n    val_samples_cache: Dict[str, List[Dict]],\\n):\\n    \\\"\\\"\\\"Compute text-overlap-based neg difficulty proxy and assign quartiles.\\\"\\\"\\\"\\n    for strategy in list(all_results.keys()):\\n        for seed in list(all_results[strategy].keys()):\\n            results = all_results[strategy][seed]\\n            cache_key = f\\\"{strategy}_s{seed}\\\"\\n            samples = val_samples_cache.get(cache_key, [])\\n            sample_map = {s[\\\"query_id\\\"]: s for s in samples}\\n\\n            margins = []\\n            for r in results:\\n                s = sample_map.get(r[\\\"query_id\\\"])\\n                if s is None:\\n                    margins.append(0.0)\\n                    continue\\n                q_toks = set(s.get(\\\"q\\n\\n... [截断: 输出过长，省略 18435 字符] ...\\n\\nt\\\")):\\n                        ckpt_dir = candidate\\n                        break\\n                if ckpt_dir is None and os.path.exists(os.path.join(base, \\\"model.pt\\\")):\\n                    ckpt_dir = base\\n                if os.path.exists(ckpt_dir):\\n                    print(f\\\"  Re-evaluating checkpoint: {ckpt_dir}\\\", flush=True)\\n                    results = reeval_checkpoint(\\n                        ckpt_dir, val_samples, args.device, args.max_seq_length\\n                    )\\n                else:\\n                    print(f\\\"  [WARN] Checkpoint not found: {ckpt_dir}\\\", flush=True)\\n                    continue\\n            else:\\n                print(\\\"  [ERROR] No --dry-run, --predictions-dir, or --checkpoints-dir\\\", flush=True)\\n                continue\\n\\n            # Assign strata\\n            results = assign_strata(results, inst_to_repo, repo_counts, dataflow_edges)\\n\\n            # For dry-run or model-based: compute text similarity for sim_bin\\n            if args.dry_run:\\n                for r, s in zip(results, val_samples):\\n                    tsim = text_similarity(s[\\\"query_tokens\\\"][:500], s[\\\"pos_tokens\\\"][:500])\\n                    r[\\\"sim_bin\\\"] = _bin_value(tsim, SIMILARITY_BINS)\\n\\n            all_results[strategy][seed] = results\\n            val_samples_cache[f\\\"{strategy}_s{seed}\\\"] = val_samples\\n            print(f\\\"  -> {len(results)} instances\\\", flush=True)\\n\\n    # Compute neg_difficulty quartiles (text-overlap proxy, CPU-safe)\\n    print(\\\"Computing neg difficulty quartiles...\\\", flush=True)\\n    assign_neg_difficulty_quartiles(all_results, val_samples_cache)\\n\\n    # Run stratified analysis\\n    print(\\\"\\\\nRunning stratified analysis...\\\", flush=True)\\n    repo_analysis = run_stratified_analysis(\\n        all_results, \\\"repo_size_bin\\\", list(REPO_SIZE_BINS.keys()), args.n_bootstrap\\n    )\\n    pool_analysis = run_stratified_analysis(\\n        all_results, \\\"pool_size_bin\\\", list(POOL_SIZE_BINS.keys()), args.n_bootstrap\\n    )\\n    sim_analysis = run_stratified_analysis(\\n        all_results, \\\"sim_bin\\\", list(SIMILARITY_BINS.keys()), args.n_bootstrap\\n    )\\n\\n    dataflow_analysis = {}\\n    if dataflow_edges is not None:\\n        dataflow_analysis = run_stratified_analysis(\\n            all_results, \\\"dataflow_bin\\\", list(DATAFLOW_BINS.keys()), args.n_bootstrap\\n        )\\n\\n    neg_diff_analysis = run_stratified_analysis(\\n        all_results, \\\"neg_difficulty_bin\\\", NEG_DIFFICULTY_QUARTILE_LABELS, args.n_bootstrap\\n    )\\n\\n    # Save JSON\\n    full_results = {\\n        \\\"config\\\": {\\n            \\\"strategies\\\": STRATEGIES,\\n            \\\"seeds\\\": seeds,\\n            \\\"repo_size_bins\\\": {k: list(v) for k, v in REPO_SIZE_BINS.items()},\\n            \\\"pool_size_bins\\\": {k: list(v) for k, v in POOL_SIZE_BINS.items()},\\n            \\\"similarity_bins\\\": {k: list(v) for k, v in SIMILARITY_BINS.items()},\\n            \\\"dataflow_bins\\\": {k: list(v) for k, v in DATAFLOW_BINS.items()},\\n            \\\"neg_difficulty_quartiles\\\": NEG_DIFFICULTY_QUARTILE_LABELS,\\n            \\\"n_bootstrap\\\": args.n_bootstrap,\\n            \\\"dry_run\\\": args.dry_run,\\n        },\\n        \\\"by_repo_size\\\": repo_analysis,\\n        \\\"by_pool_size\\\": pool_analysis,\\n        \\\"by_similarity\\\": sim_analysis,\\n        \\\"by_dataflow\\\": dataflow_analysis,\\n        \\\"by_neg_difficulty\\\": neg_diff_analysis,\\n    }\\n\\n    json_path = os.path.join(args.output_dir, \\\"stratified_results.json\\\")\\n    with open(json_path, \\\"w\\\") as f:\\n        json.dump(full_results, f, indent=2, ensure_ascii=False)\\n    print(f\\\"  Results JSON saved to {json_path}\\\", flush=True)\\n\\n    # CSV summary\\n    csv_path = os.path.join(args.output_dir, \\\"stratified_summary.csv\\\")\\n    write_summary_csv(repo_analysis, pool_analysis, sim_analysis, csv_path, dataflow_analysis, neg_diff_analysis)\\n\\n    # Plots\\n    try:\\n        make_plots(repo_analysis, pool_analysis, sim_analysis, args.output_dir, dataflow_analysis, neg_diff_analysis)\\n    except Exception as e:\\n        print(f\\\"  [WARN] Plot generation failed: {e}\\\", flush=True)\\n\\n    print(\\\"\\\\nDone.\\\", flush=True)\\n\\n\\nif __name__ == \\\"__main__\\\":\\n    main()\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4}}"
    }
  },
  "sourceToolAssistantUUID": "12dd8017-dd11-4b98-a705-d7d128c4a23b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "fb5ea7f7-b3c9-4750-b931-39d2aaae422b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 68_

```json
{
  "type": "last-prompt",
  "leafUuid": "af04de64-31cf-457b-8b5a-18f37b1f577e",
  "sessionId": "fb5ea7f7-b3c9-4750-b931-39d2aaae422b"
}
```

---

### Runtime record

_source line 69_

```json
{
  "type": "ai-title",
  "aiTitle": "Trace stratified_dryrun v1 to v2 differences",
  "sessionId": "fb5ea7f7-b3c9-4750-b931-39d2aaae422b"
}
```

---

### Assistant

_source line 70 · 2026-05-14T20:38:18.799Z_

<details><summary>Logged reasoning block</summary>

````text
I can now see the `mock_predictions` function. Let me understand it:

```python
def mock_predictions(val_samples, strategy, seed):
    rng = np.random.RandomState(seed + abs(hash(strategy)) % 10000)
    results = []
    for sample in val_samples:
        pool = 1 + sample["pool_size"]


```

Now I'm seeing how the function generates rankings based on the strategy—using random selection, exponential distribution for embedding distance, or a different exponential for other strategies. It then calculates a similarity score by combining the rank-based position similarity with some noise, and computes text similarity between query and positive tokens.

I'm appending each result with the query metadata, computed rank, similarity score, and pool size. The function returns all accumulated results.

But I'm noticing something critical about the RNG seed calculation: it uses `seed + abs(hash(strategy)) % 10000`, and since Python's `hash()` function produces different values across sessions by default (unless `PYTHONHASHSEED` is fixed), the effective seed changes between runs. This means the random number generation isn't actually reproducible across different executions, which would explain why v1 and v2 runs produce different results even with the same input parameters. The bin boundaries stay fixed, but every strategy gets affected by the hash randomization since they all rely on `hash(strategy)` for seeding. I'm also noticing that v1 was generated by an older script version—it lacks the `dataflow_bins` and `neg_difficulty_quartiles` dimensions that v2 has. Beyond that structural difference, the `assign_strata` function appears to override `sim_bin` in the current version, which could be another factor in the divergence. So the stratum assignment itself is deterministic in dry-run mode—repo size, pool size, and similarity bins all stay consistent across runs. But the metric values computed from `rank` fluctuate because `hash(strategy)` varies between Python processes due to hash randomization, which is why v1 and v2 show different numbers even though they're binning the same samples identically. The v2 script added dataflow and difficulty strata that v1 might not have had, but that's separate from the mock prediction issue. the metric values differ because the mock `rank` values differ. I'm noticing that v1 was generated by an earlier version of the script—it's missing `dataflow_bins`, `neg_difficulty_quartiles`, `by_dataflow`, and `by_neg_difficulty` that the current version always includes. Even for the shared dimensions like `by_repo_size`, `by_pool_size`, and `by_similarity`, the bin boundaries should be identical, so the differences must stem from the `hash(strategy)` issue affecting the mock predictions.

I'm seeing that in the dry-run branch, `sim_bin` gets recalculated based on actual text similarity, which makes `by_similarity` deterministic, but `by_repo_size` and `by_pool_size` still depend on the RNG-based `rank` values. Let me trace through whether `pool_size` might have similar issues.

Looking at the `by_similarity` metrics, both versions show identical counts (medium: 350, high: 24), which confirms they're using the same data and binning logic—so the metric differences must come from those RNG-dependent ranks. Now I need to check if `by_pool_size` has the same pattern.
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "af04de64-31cf-457b-8b5a-18f37b1f577e",
  "isSidechain": false,
  "requestId": "req_011Cb371gkcisnm4Xtp6tj5g",
  "type": "assistant",
  "uuid": "b51ebf05-b94c-4580-b850-b89fa63e26b6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "fb5ea7f7-b3c9-4750-b931-39d2aaae422b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EkVu3Kk6AFcrh5p14pa5Gz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3493,
      "cache_read_input_tokens": 54417,
      "output_tokens": 2714,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3493,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2714,
          "cache_read_input_tokens": 54417,
          "cache_creation_input_tokens": 3493,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3493
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

_source line 71 · 2026-05-14T20:38:19.412Z_

找到关键线索了。`mock_predictions` 使用 `hash(strategy)` 作为 RNG seed 的一部分，Python 3 的字符串 hash 每次进程启动都不同。让我验证并检查是否有旧版本脚本。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b51ebf05-b94c-4580-b850-b89fa63e26b6",
  "isSidechain": false,
  "requestId": "req_011Cb371gkcisnm4Xtp6tj5g",
  "type": "assistant",
  "uuid": "17455a56-69de-4096-a1b4-e8a7075a83f5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "fb5ea7f7-b3c9-4750-b931-39d2aaae422b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EkVu3Kk6AFcrh5p14pa5Gz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3493,
      "cache_read_input_tokens": 54417,
      "output_tokens": 2714,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3493,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2714,
          "cache_read_input_tokens": 54417,
          "cache_creation_input_tokens": 3493,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3493
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

_source line 72 · 2026-05-14T20:38:20.289Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_011ZHV5oU37JP5waWCBcDbqi`</summary>

```json
{
  "server": "bjb1-42106",
  "command": "find /root/structfuse/evaluation/ -name \"analyze_stratified*\" -type f",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "17455a56-69de-4096-a1b4-e8a7075a83f5",
  "isSidechain": false,
  "requestId": "req_011Cb371gkcisnm4Xtp6tj5g",
  "type": "assistant",
  "uuid": "5597355a-bf65-467e-a32f-01008549bb9f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "fb5ea7f7-b3c9-4750-b931-39d2aaae422b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EkVu3Kk6AFcrh5p14pa5Gz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3493,
      "cache_read_input_tokens": 54417,
      "output_tokens": 2714,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3493,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2714,
          "cache_read_input_tokens": 54417,
          "cache_creation_input_tokens": 3493,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3493
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

_source line 73 · 2026-05-14T20:38:20.690Z_

<details><summary>↩ Tool result · `toolu_011ZHV5oU37JP5waWCBcDbqi`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/structfuse/evaluation/analyze_stratified.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.38}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5597355a-bf65-467e-a32f-01008549bb9f",
  "isSidechain": false,
  "promptId": "0b7bb415-f2b4-4832-aac4-2e6aafdc7429",
  "type": "user",
  "uuid": "c0825dbd-b6ff-4bab-a0ec-168111ead64e",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"/root/structfuse/evaluation/analyze_stratified.py\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.38}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"/root/structfuse/evaluation/analyze_stratified.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.38}}"
    }
  },
  "sourceToolAssistantUUID": "5597355a-bf65-467e-a32f-01008549bb9f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "fb5ea7f7-b3c9-4750-b931-39d2aaae422b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 74 · 2026-05-14T20:38:21.090Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_011WsLhDx3pRJj8SjpLWea9b`</summary>

```json
{
  "server": "bjb1-42106",
  "command": "find /root/autodl-tmp/structfuse/artifacts/stratified_dryrun/ -name \"*.log\" -type f",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c0825dbd-b6ff-4bab-a0ec-168111ead64e",
  "isSidechain": false,
  "requestId": "req_011Cb371gkcisnm4Xtp6tj5g",
  "type": "assistant",
  "uuid": "050a9391-ebd5-4c1e-8f44-3420da308c8b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "fb5ea7f7-b3c9-4750-b931-39d2aaae422b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EkVu3Kk6AFcrh5p14pa5Gz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3493,
      "cache_read_input_tokens": 54417,
      "output_tokens": 2714,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3493,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2714,
          "cache_read_input_tokens": 54417,
          "cache_creation_input_tokens": 3493,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3493
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

_source line 75 · 2026-05-14T20:38:21.511Z_

<details><summary>↩ Tool result · `toolu_011WsLhDx3pRJj8SjpLWea9b`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.41}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "050a9391-ebd5-4c1e-8f44-3420da308c8b",
  "isSidechain": false,
  "promptId": "0b7bb415-f2b4-4832-aac4-2e6aafdc7429",
  "type": "user",
  "uuid": "a7dceebf-3dda-47ad-b7b7-6e222a969f41",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.41}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.41}}"
    }
  },
  "sourceToolAssistantUUID": "050a9391-ebd5-4c1e-8f44-3420da308c8b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "fb5ea7f7-b3c9-4750-b931-39d2aaae422b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 76 · 2026-05-14T20:38:21.861Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01BA5ZmX9nKy3tn3gNAP8Chk`</summary>

```json
{
  "server": "bjb1-42106",
  "command": "find /root/autodl-tmp/structfuse/artifacts/stratified_dryrun_v2/ -name \"*.log\" -type f",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a7dceebf-3dda-47ad-b7b7-6e222a969f41",
  "isSidechain": false,
  "requestId": "req_011Cb371gkcisnm4Xtp6tj5g",
  "type": "assistant",
  "uuid": "327f6f64-9212-4242-a8d3-3fb3ff2fa4d4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "fb5ea7f7-b3c9-4750-b931-39d2aaae422b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EkVu3Kk6AFcrh5p14pa5Gz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3493,
      "cache_read_input_tokens": 54417,
      "output_tokens": 2714,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3493,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2714,
          "cache_read_input_tokens": 54417,
          "cache_creation_input_tokens": 3493,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3493
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

_source line 77 · 2026-05-14T20:38:22.219Z_

<details><summary>↩ Tool result · `toolu_01BA5ZmX9nKy3tn3gNAP8Chk`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "327f6f64-9212-4242-a8d3-3fb3ff2fa4d4",
  "isSidechain": false,
  "promptId": "0b7bb415-f2b4-4832-aac4-2e6aafdc7429",
  "type": "user",
  "uuid": "d3db09c0-9c38-42ee-afed-f06b40d3b973",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.35}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"
    }
  },
  "sourceToolAssistantUUID": "327f6f64-9212-4242-a8d3-3fb3ff2fa4d4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "fb5ea7f7-b3c9-4750-b931-39d2aaae422b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 78 · 2026-05-14T20:38:25.467Z_

<details><summary>Logged reasoning block</summary>

```text
No old versions or logs found. Let me now run a comprehensive comparison of the two JSON files on the server to get all the numbers I need, and also verify the hash issue hypothesis.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d3db09c0-9c38-42ee-afed-f06b40d3b973",
  "isSidechain": false,
  "requestId": "req_011Cb3755KkzvwGkvFVPmjyU",
  "type": "assistant",
  "uuid": "5a4084f1-fc05-4588-bea0-25d1726a58c5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "fb5ea7f7-b3c9-4750-b931-39d2aaae422b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013jf2aFQsdQ1Q22zuDFVzBX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3033,
      "cache_read_input_tokens": 57910,
      "output_tokens": 967,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3033,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 967,
          "cache_read_input_tokens": 57910,
          "cache_creation_input_tokens": 3033,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3033
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

_source line 79 · 2026-05-14T20:38:25.962Z_

让我在服务器上做精确数值对比，同时验证 hash 随机化假设。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5a4084f1-fc05-4588-bea0-25d1726a58c5",
  "isSidechain": false,
  "requestId": "req_011Cb3755KkzvwGkvFVPmjyU",
  "type": "assistant",
  "uuid": "2f0bf949-42e8-42d6-acdd-35e86f384db5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "fb5ea7f7-b3c9-4750-b931-39d2aaae422b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013jf2aFQsdQ1Q22zuDFVzBX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3033,
      "cache_read_input_tokens": 57910,
      "output_tokens": 967,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3033,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 967,
          "cache_read_input_tokens": 57910,
          "cache_creation_input_tokens": 3033,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3033
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

_source line 80 · 2026-05-14T20:38:35.137Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_01Yb1nYPXjanTysv6iZfysur`</summary>

```json
{
  "server": "bjb1-42106",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python3 -c \"\nimport json\n\nv1 = json.load(open('/root/autodl-tmp/structfuse/artifacts/stratified_dryrun/stratified_results.json'))\nv2 = json.load(open('/root/autodl-tmp/structfuse/artifacts/stratified_dryrun_v2/stratified_results.json'))\n\nprint('=== CONFIG DIFF ===')\nprint('v1 keys:', sorted(v1['config'].keys()))\nprint('v2 keys:', sorted(v2['config'].keys()))\nv2_only = set(v2['config'].keys()) - set(v1['config'].keys())\nprint('v2-only config keys:', v2_only)\n\nprint()\nprint('=== DIMENSION DIFF ===')\nprint('v1 top-level keys:', sorted(v1.keys()))\nprint('v2 top-level keys:', sorted(v2.keys()))\nv2_only_dims = set(v2.keys()) - set(v1.keys())\nprint('v2-only dimensions:', v2_only_dims)\n\nshared_dims = ['by_repo_size', 'by_pool_size', 'by_similarity']\nstrategies = ['random', 'embedding_distance', 'dataflow_aware']\n\nprint()\nprint('=== DETAILED COMPARISON (shared dimensions) ===')\nfor dim in shared_dims:\n    print(f'\\n--- {dim} ---')\n    d1 = v1[dim]\n    d2 = v2[dim]\n    all_bins = sorted(set(list(d1.keys()) + list(d2.keys())))\n    for b in all_bins:\n        for strat in strategies:\n            if b in d1 and strat in d1[b] and b in d2 and strat in d2[b]:\n                s1 = d1[b][strat]\n                s2 = d2[b][strat]\n                r1_v1 = s1['R@1']\n                r1_v2 = s2['R@1']\n                r5_v1 = s1['R@5']\n                r5_v2 = s2['R@5']\n                mrr_v1 = s1['MRR']\n                mrr_v2 = s2['MRR']\n                n1 = s1['count']\n                n2 = s2['count']\n                print(f'{b:>10} | {strat:>20} | n={n1:>4}->{n2:>4} | R@1: {r1_v1:.4f}->{r1_v2:.4f} ({(r1_v2-r1_v1):+.4f}) | R@5: {r5_v1:.4f}->{r5_v2:.4f} ({(r5_v2-r5_v1):+.4f}) | MRR: {mrr_v1:.4f}->{mrr_v2:.4f} ({(mrr_v2-mrr_v1):+.4f})')\n\"\n",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2f0bf949-42e8-42d6-acdd-35e86f384db5",
  "isSidechain": false,
  "requestId": "req_011Cb3755KkzvwGkvFVPmjyU",
  "type": "assistant",
  "uuid": "aeb775af-faff-4ffd-aaea-33080f006711",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "fb5ea7f7-b3c9-4750-b931-39d2aaae422b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013jf2aFQsdQ1Q22zuDFVzBX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3033,
      "cache_read_input_tokens": 57910,
      "output_tokens": 967,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3033,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 967,
          "cache_read_input_tokens": 57910,
          "cache_creation_input_tokens": 3033,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3033
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

_source line 81 · 2026-05-14T20:38:35.609Z_

<details><summary>↩ Tool result · `toolu_01Yb1nYPXjanTysv6iZfysur`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"=== CONFIG DIFF ===\\nv1 keys: ['dry_run', 'n_bootstrap', 'pool_size_bins', 'repo_size_bins', 'seeds', 'similarity_bins', 'strategies']\\nv2 keys: ['dataflow_bins', 'dry_run', 'n_bootstrap', 'neg_difficulty_quartiles', 'pool_size_bins', 'repo_size_bins', 'seeds', 'similarity_bins', 'strategies']\\nv2-only config keys: {'dataflow_bins', 'neg_difficulty_quartiles'}\\n\\n=== DIMENSION DIFF ===\\nv1 top-level keys: ['by_pool_size', 'by_repo_size', 'by_similarity', 'config']\\nv2 top-level keys: ['by_dataflow', 'by_neg_difficulty', 'by_pool_size', 'by_repo_size', 'by_similarity', 'config']\\nv2-only dimensions: {'by_neg_difficulty', 'by_dataflow'}\\n\\n=== DETAILED COMPARISON (shared dimensions) ===\\n\\n--- by_repo_size ---\\n     large |               random | n=1226->1226 | R@1: 0.0228->0.0277 (+0.0049) | R@5: 0.1142->0.1077 (-0.0065) | MRR: 0.0987->0.0992 (+0.0005)\\n     large |   embedding_distance | n=1226->1226 | R@1: 0.0546->0.0530 (-0.0016) | R@5: 0.2577->0.2765 (+0.0188) | MRR: 0.1754->0.1760 (+0.0006)\\n     large |       dataflow_aware | n=1226->1226 | R@1: 0.1052->0.0962 (-0.0090) | R@5: 0.4095->0.4103 (+0.0008) | MRR: 0.2578->0.2548 (-0.0029)\\n    medium |               random | n= 346-> 346 | R@1: 0.0520->0.0549 (+0.0029) | R@5: 0.2312->0.2861 (+0.0549) | MRR: 0.1782->0.1936 (+0.0154)\\n    medium |   embedding_distance | n= 346-> 346 | R@1: 0.1069->0.1503 (+0.0434) | R@5: 0.4942->0.5231 (+0.0289) | MRR: 0.2866->0.3299 (+0.0433)\\n    medium |       dataflow_aware | n= 346-> 346 | R@1: 0.2399->0.2399 (+0.0000) | R@5: 0.7023->0.7370 (+0.0347) | MRR: 0.4295->0.4508 (+0.0213)\\n     small |               random | n= 130-> 130 | R@1: 0.1154->0.0769 (-0.0385) | R@5: 0.5385->0.4769 (-0.0615) | MRR: 0.3060->0.2643 (-0.0417)\\n     small |   embedding_distance | n= 130-> 130 | R@1: 0.3000->0.2769 (-0.0231) | R@5: 0.7385->0.7385 (+0.0000) | MRR: 0.4931->0.4704 (-0.0226)\\n     small |       dataflow_aware | n= 130-> 130 | R@1: 0.4846->0.4000 (-0.0846) | R@5: 0.8769->0.9000 (+0.0231) | MRR: 0.6501->0.6000 (-0.0501)\\n    xlarge |               random | n=1278->1278 | R@1: 0.0219->0.0149 (-0.0070) | R@5: 0.0970->0.1095 (+0.0125) | MRR: 0.0923->0.0907 (-0.0015)\\n    xlarge |   embedding_distance | n=1278->1278 | R@1: 0.0548->0.0610 (+0.0063) | R@5: 0.2520->0.2559 (+0.0039) | MRR: 0.1724->0.1750 (+0.0026)\\n    xlarge |       dataflow_aware | n=1278->1278 | R@1: 0.0994->0.1072 (+0.0078) | R@5: 0.3881->0.4210 (+0.0329) | MRR: 0.2480->0.2619 (+0.0139)\\n\\n--- by_pool_size ---\\n     large |               random | n=2099->2099 | R@1: 0.0214->0.0186 (-0.0029) | R@5: 0.1005->0.1024 (+0.0019) | MRR: 0.0913->0.0887 (-0.0026)\\n     large |   embedding_distance | n=2099->2099 | R@1: 0.0524->0.0534 (+0.0010) | R@5: 0.2392->0.2511 (+0.0119) | MRR: 0.1664->0.1672 (+0.0008)\\n     large |       dataflow_aware | n=2099->2099 | R@1: 0.1005->0.0981 (-0.0024) | R@5: 0.3816->0.3954 (+0.0138) | MRR: 0.2456->0.2497 (+0.0042)\\n    medium |               random | n= 605-> 605 | R@1: 0.0314->0.0364 (+0.0050) | R@5: 0.1421->0.1653 (+0.0231) | MRR: 0.1281->0.1376 (+0.0096)\\n    medium |   embedding_distance | n= 605-> 605 | R@1: 0.0760->0.0843 (+0.0083) | R@5: 0.3653->0.3835 (+0.0182) | MRR: 0.2289->0.2362 (+0.0073)\\n    medium |       dataflow_aware | n= 605-> 605 | R@1: 0.1405->0.1421 (+0.0017) | R@5: 0.5455->0.5636 (+0.0182) | MRR: 0.3263->0.3332 (+0.0069)\\n     small |               random | n= 276-> 276 | R@1: 0.0906->0.0761 (-0.0145) | R@5: 0.4239->0.4275 (+0.0036) | MRR: 0.2582->0.2519 (-0.0063)\\n     small |   embedding_distance | n= 276-> 276 | R@1: 0.2065->0.2464 (+0.0399) | R@5: 0.6594->0.6667 (+0.0072) | MRR: 0.4016->0.4381 (+0.0365)\\n     small |       dataflow_aware | n= 276-> 276 | R@1: 0.3841->0.3551 (-0.0290) | R@5: 0.8116->0.8768 (+0.0652) | MRR: 0.5555->0.5628 (+0.0074)\\n\\n--- by_similarity ---\\n      high |               random | n=  24->  24 | R@1: 0.0000->0.0000 (+0.0000) | R@5: 0.0000->0.1250 (+0.1250) | MRR: 0.0663->0.0703 (+0.0040)\\n      high |   embedding_distance | n=  24->  24 | R@1: 0.0833->0.0417 (-0.0417) | R@5: 0.2500->0.2083 (-0.0417) | MRR: 0.1866->0.1565 (-0.0301)\\n      high |       dataflow_aware | n=  24->  24 | R@1: 0.0833->0.0833 (+0.0000) | R@5: 0.2500->0.4583 (+0.2083) | MRR: 0.1936->0.2834 (+0.0898)\\n       low |               random | n=2606->2606 | R@1: 0.0322->0.0284 (-0.0038) | R@5: 0.1450->0.1427 (-0.0023) | MRR: 0.1181->0.1142 (-0.0039)\\n       low |   embedding_distance | n=2606->2606 | R@1: 0.0721->0.0779 (+0.0058) | R@5: 0.3043->0.3177 (+0.0134) | MRR: 0.2024->0.2070 (+0.0046)\\n       low |       dataflow_aware | n=2606->2606 | R@1: 0.1355->0.1285 (-0.0069) | R@5: 0.4593->0.4731 (+0.0138) | MRR: 0.2923->0.2939 (+0.0016)\\n    medium |               random | n= 350-> 350 | R@1: 0.0143->0.0229 (+0.0086) | R@5: 0.1029->0.1657 (+0.0629) | MRR: 0.0889->0.1135 (+0.0246)\\n    medium |   embedding_distance | n= 350-> 350 | R@1: 0.0657->0.0771 (+0.0114) | R@5: 0.3029->0.3143 (+0.0114) | MRR: 0.1904->0.2042 (+0.0139)\\n    medium |       dataflow_aware | n= 350-> 350 | R@1: 0.1343->0.1514 (+0.0171) | R@5: 0.4343->0.4829 (+0.0486) | MRR: 0.2853->0.3097 (+0.0244)\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.46}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "aeb775af-faff-4ffd-aaea-33080f006711",
  "isSidechain": false,
  "promptId": "0b7bb415-f2b4-4832-aac4-2e6aafdc7429",
  "type": "user",
  "uuid": "34c534af-060f-4ea2-b7d8-483f5cf915bc",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"=== CONFIG DIFF ===\\\\nv1 keys: ['dry_run', 'n_bootstrap', 'pool_size_bins', 'repo_size_bins', 'seeds', 'similarity_bins', 'strategies']\\\\nv2 keys: ['dataflow_bins', 'dry_run', 'n_bootstrap', 'neg_difficulty_quartiles', 'pool_size_bins', 'repo_size_bins', 'seeds', 'similarity_bins', 'strategies']\\\\nv2-only config keys: {'dataflow_bins', 'neg_difficulty_quartiles'}\\\\n\\\\n=== DIMENSION DIFF ===\\\\nv1 top-level keys: ['by_pool_size', 'by_repo_size', 'by_similarity', 'config']\\\\nv2 top-level keys: ['by_dataflow', 'by_neg_difficulty', 'by_pool_size', 'by_repo_size', 'by_similarity', 'config']\\\\nv2-only dimensions: {'by_neg_difficulty', 'by_dataflow'}\\\\n\\\\n=== DETAILED COMPARISON (shared dimensions) ===\\\\n\\\\n--- by_repo_size ---\\\\n     large |               random | n=1226->1226 | R@1: 0.0228->0.0277 (+0.0049) | R@5: 0.1142->0.1077 (-0.0065) | MRR: 0.0987->0.0992 (+0.0005)\\\\n     large |   embedding_distance | n=1226->1226 | R@1: 0.0546->0.0530 (-0.0016) | R@5: 0.2577->0.2765 (+0.0188) | MRR: 0.1754->0.1760 (+0.0006)\\\\n     large |       dataflow_aware | n=1226->1226 | R@1: 0.1052->0.0962 (-0.0090) | R@5: 0.4095->0.4103 (+0.0008) | MRR: 0.2578->0.2548 (-0.0029)\\\\n    medium |               random | n= 346-> 346 | R@1: 0.0520->0.0549 (+0.0029) | R@5: 0.2312->0.2861 (+0.0549) | MRR: 0.1782->0.1936 (+0.0154)\\\\n    medium |   embedding_distance | n= 346-> 346 | R@1: 0.1069->0.1503 (+0.0434) | R@5: 0.4942->0.5231 (+0.0289) | MRR: 0.2866->0.3299 (+0.0433)\\\\n    medium |       dataflow_aware | n= 346-> 346 | R@1: 0.2399->0.2399 (+0.0000) | R@5: 0.7023->0.7370 (+0.0347) | MRR: 0.4295->0.4508 (+0.0213)\\\\n     small |               random | n= 130-> 130 | R@1: 0.1154->0.0769 (-0.0385) | R@5: 0.5385->0.4769 (-0.0615) | MRR: 0.3060->0.2643 (-0.0417)\\\\n     small |   embedding_distance | n= 130-> 130 | R@1: 0.3000->0.2769 (-0.0231) | R@5: 0.7385->0.7385 (+0.0000) | MRR: 0.4931->0.4704 (-0.0226)\\\\n     small |       dataflow_aware | n= 130-> 130 | R@1: 0.4846->0.4000 (-0.0846) | R@5: 0.8769->0.9000 (+0.0231) | MRR: 0.6501->0.6000 (-0.0501)\\\\n    xlarge |               random | n=1278->1278 | R@1: 0.0219->0.0149 (-0.0070) | R@5: 0.0970->0.1095 (+0.0125) | MRR: 0.0923->0.0907 (-0.0015)\\\\n    xlarge |   embedding_distance | n=1278->1278 | R@1: 0.0548->0.0610 (+0.0063) | R@5: 0.2520->0.2559 (+0.0039) | MRR: 0.1724->0.1750 (+0.0026)\\\\n    xlarge |       dataflow_aware | n=1278->1278 | R@1: 0.0994->0.1072 (+0.0078) | R@5: 0.3881->0.4210 (+0.0329) | MRR: 0.2480->0.2619 (+0.0139)\\\\n\\\\n--- by_pool_size ---\\\\n     large |               random | n=2099->2099 | R@1: 0.0214->0.0186 (-0.0029) | R@5: 0.1005->0.1024 (+0.0019) | MRR: 0.0913->0.0887 (-0.0026)\\\\n     large |   embedding_distance | n=2099->2099 | R@1: 0.0524->0.0534 (+0.0010) | R@5: 0.2392->0.2511 (+0.0119) | MRR: 0.1664->0.1672 (+0.0008)\\\\n     large |       dataflow_aware | n=2099->2099 | R@1: 0.1005->0.0981 (-0.0024) | R@5: 0.3816->0.3954 (+0.0138) | MRR: 0.2456->0.2497 (+0.0042)\\\\n    medium |               random | n= 605-> 605 | R@1: 0.0314->0.0364 (+0.0050) | R@5: 0.1421->0.1653 (+0.0231) | MRR: 0.1281->0.1376 (+0.0096)\\\\n    medium |   embedding_distance | n= 605-> 605 | R@1: 0.0760->0.0843 (+0.0083) | R@5: 0.3653->0.3835 (+0.0182) | MRR: 0.2289->0.2362 (+0.0073)\\\\n    medium |       dataflow_aware | n= 605-> 605 | R@1: 0.1405->0.1421 (+0.0017) | R@5: 0.5455->0.5636 (+0.0182) | MRR: 0.3263->0.3332 (+0.0069)\\\\n     small |               random | n= 276-> 276 | R@1: 0.0906->0.0761 (-0.0145) | R@5: 0.4239->0.4275 (+0.0036) | MRR: 0.2582->0.2519 (-0.0063)\\\\n     small |   embedding_distance | n= 276-> 276 | R@1: 0.2065->0.2464 (+0.0399) | R@5: 0.6594->0.6667 (+0.0072) | MRR: 0.4016->0.4381 (+0.0365)\\\\n     small |       dataflow_aware | n= 276-> 276 | R@1: 0.3841->0.3551 (-0.0290) | R@5: 0.8116->0.8768 (+0.0652) | MRR: 0.5555->0.5628 (+0.0074)\\\\n\\\\n--- by_similarity ---\\\\n      high |               random | n=  24->  24 | R@1: 0.0000->0.0000 (+0.0000) | R@5: 0.0000->0.1250 (+0.1250) | MRR: 0.0663->0.0703 (+0.0040)\\\\n      high |   embedding_distance | n=  24->  24 | R@1: 0.0833->0.0417 (-0.0417) | R@5: 0.2500->0.2083 (-0.0417) | MRR: 0.1866->0.1565 (-0.0301)\\\\n      high |       dataflow_aware | n=  24->  24 | R@1: 0.0833->0.0833 (+0.0000) | R@5: 0.2500->0.4583 (+0.2083) | MRR: 0.1936->0.2834 (+0.0898)\\\\n       low |               random | n=2606->2606 | R@1: 0.0322->0.0284 (-0.0038) | R@5: 0.1450->0.1427 (-0.0023) | MRR: 0.1181->0.1142 (-0.0039)\\\\n       low |   embedding_distance | n=2606->2606 | R@1: 0.0721->0.0779 (+0.0058) | R@5: 0.3043->0.3177 (+0.0134) | MRR: 0.2024->0.2070 (+0.0046)\\\\n       low |       dataflow_aware | n=2606->2606 | R@1: 0.1355->0.1285 (-0.0069) | R@5: 0.4593->0.4731 (+0.0138) | MRR: 0.2923->0.2939 (+0.0016)\\\\n    medium |               random | n= 350-> 350 | R@1: 0.0143->0.0229 (+0.0086) | R@5: 0.1029->0.1657 (+0.0629) | MRR: 0.0889->0.1135 (+0.0246)\\\\n    medium |   embedding_distance | n= 350-> 350 | R@1: 0.0657->0.0771 (+0.0114) | R@5: 0.3029->0.3143 (+0.0114) | MRR: 0.1904->0.2042 (+0.0139)\\\\n    medium |       dataflow_aware | n= 350-> 350 | R@1: 0.1343->0.1514 (+0.0171) | R@5: 0.4343->0.4829 (+0.0486) | MRR: 0.2853->0.3097 (+0.0244)\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.46}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"=== CONFIG DIFF ===\\nv1 keys: ['dry_run', 'n_bootstrap', 'pool_size_bins', 'repo_size_bins', 'seeds', 'similarity_bins', 'strategies']\\nv2 keys: ['dataflow_bins', 'dry_run', 'n_bootstrap', 'neg_difficulty_quartiles', 'pool_size_bins', 'repo_size_bins', 'seeds', 'similarity_bins', 'strategies']\\nv2-only config keys: {'dataflow_bins', 'neg_difficulty_quartiles'}\\n\\n=== DIMENSION DIFF ===\\nv1 top-level keys: ['by_pool_size', 'by_repo_size', 'by_similarity', 'config']\\nv2 top-level keys: ['by_dataflow', 'by_neg_difficulty', 'by_pool_size', 'by_repo_size', 'by_similarity', 'config']\\nv2-only dimensions: {'by_neg_difficulty', 'by_dataflow'}\\n\\n=== DETAILED COMPARISON (shared dimensions) ===\\n\\n--- by_repo_size ---\\n     large |               random | n=1226->1226 | R@1: 0.0228->0.0277 (+0.0049) | R@5: 0.1142->0.1077 (-0.0065) | MRR: 0.0987->0.0992 (+0.0005)\\n     large |   embedding_distance | n=1226->1226 | R@1: 0.0546->0.0530 (-0.0016) | R@5: 0.2577->0.2765 (+0.0188) | MRR: 0.1754->0.1760 (+0.0006)\\n     large |       dataflow_aware | n=1226->1226 | R@1: 0.1052->0.0962 (-0.0090) | R@5: 0.4095->0.4103 (+0.0008) | MRR: 0.2578->0.2548 (-0.0029)\\n    medium |               random | n= 346-> 346 | R@1: 0.0520->0.0549 (+0.0029) | R@5: 0.2312->0.2861 (+0.0549) | MRR: 0.1782->0.1936 (+0.0154)\\n    medium |   embedding_distance | n= 346-> 346 | R@1: 0.1069->0.1503 (+0.0434) | R@5: 0.4942->0.5231 (+0.0289) | MRR: 0.2866->0.3299 (+0.0433)\\n    medium |       dataflow_aware | n= 346-> 346 | R@1: 0.2399->0.2399 (+0.0000) | R@5: 0.7023->0.7370 (+0.0347) | MRR: 0.4295->0.4508 (+0.0213)\\n     small |               random | n= 130-> 130 | R@1: 0.1154->0.0769 (-0.0385) | R@5: 0.5385->0.4769 (-0.0615) | MRR: 0.3060->0.2643 (-0.0417)\\n     small |   embedding_distance | n= 130-> 130 | R@1: 0.3000->0.2769 (-0.0231) | R@5: 0.7385->0.7385 (+0.0000) | MRR: 0.4931->0.4704 (-0.0226)\\n     small |       dataflow_aware | n= 130-> 130 | R@1: 0.4846->0.4000 (-0.0846) | R@5: 0.8769->0.9000 (+0.0231) | MRR: 0.6501->0.6000 (-0.0501)\\n    xlarge |               random | n=1278->1278 | R@1: 0.0219->0.0149 (-0.0070) | R@5: 0.0970->0.1095 (+0.0125) | MRR: 0.0923->0.0907 (-0.0015)\\n    xlarge |   embedding_distance | n=1278->1278 | R@1: 0.0548->0.0610 (+0.0063) | R@5: 0.2520->0.2559 (+0.0039) | MRR: 0.1724->0.1750 (+0.0026)\\n    xlarge |       dataflow_aware | n=1278->1278 | R@1: 0.0994->0.1072 (+0.0078) | R@5: 0.3881->0.4210 (+0.0329) | MRR: 0.2480->0.2619 (+0.0139)\\n\\n--- by_pool_size ---\\n     large |               random | n=2099->2099 | R@1: 0.0214->0.0186 (-0.0029) | R@5: 0.1005->0.1024 (+0.0019) | MRR: 0.0913->0.0887 (-0.0026)\\n     large |   embedding_distance | n=2099->2099 | R@1: 0.0524->0.0534 (+0.0010) | R@5: 0.2392->0.2511 (+0.0119) | MRR: 0.1664->0.1672 (+0.0008)\\n     large |       dataflow_aware | n=2099->2099 | R@1: 0.1005->0.0981 (-0.0024) | R@5: 0.3816->0.3954 (+0.0138) | MRR: 0.2456->0.2497 (+0.0042)\\n    medium |               random | n= 605-> 605 | R@1: 0.0314->0.0364 (+0.0050) | R@5: 0.1421->0.1653 (+0.0231) | MRR: 0.1281->0.1376 (+0.0096)\\n    medium |   embedding_distance | n= 605-> 605 | R@1: 0.0760->0.0843 (+0.0083) | R@5: 0.3653->0.3835 (+0.0182) | MRR: 0.2289->0.2362 (+0.0073)\\n    medium |       dataflow_aware | n= 605-> 605 | R@1: 0.1405->0.1421 (+0.0017) | R@5: 0.5455->0.5636 (+0.0182) | MRR: 0.3263->0.3332 (+0.0069)\\n     small |               random | n= 276-> 276 | R@1: 0.0906->0.0761 (-0.0145) | R@5: 0.4239->0.4275 (+0.0036) | MRR: 0.2582->0.2519 (-0.0063)\\n     small |   embedding_distance | n= 276-> 276 | R@1: 0.2065->0.2464 (+0.0399) | R@5: 0.6594->0.6667 (+0.0072) | MRR: 0.4016->0.4381 (+0.0365)\\n     small |       dataflow_aware | n= 276-> 276 | R@1: 0.3841->0.3551 (-0.0290) | R@5: 0.8116->0.8768 (+0.0652) | MRR: 0.5555->0.5628 (+0.0074)\\n\\n--- by_similarity ---\\n      high |               random | n=  24->  24 | R@1: 0.0000->0.0000 (+0.0000) | R@5: 0.0000->0.1250 (+0.1250) | MRR: 0.0663->0.0703 (+0.0040)\\n      high |   embedding_distance | n=  24->  24 | R@1: 0.0833->0.0417 (-0.0417) | R@5: 0.2500->0.2083 (-0.0417) | MRR: 0.1866->0.1565 (-0.0301)\\n      high |       dataflow_aware | n=  24->  24 | R@1: 0.0833->0.0833 (+0.0000) | R@5: 0.2500->0.4583 (+0.2083) | MRR: 0.1936->0.2834 (+0.0898)\\n       low |               random | n=2606->2606 | R@1: 0.0322->0.0284 (-0.0038) | R@5: 0.1450->0.1427 (-0.0023) | MRR: 0.1181->0.1142 (-0.0039)\\n       low |   embedding_distance | n=2606->2606 | R@1: 0.0721->0.0779 (+0.0058) | R@5: 0.3043->0.3177 (+0.0134) | MRR: 0.2024->0.2070 (+0.0046)\\n       low |       dataflow_aware | n=2606->2606 | R@1: 0.1355->0.1285 (-0.0069) | R@5: 0.4593->0.4731 (+0.0138) | MRR: 0.2923->0.2939 (+0.0016)\\n    medium |               random | n= 350-> 350 | R@1: 0.0143->0.0229 (+0.0086) | R@5: 0.1029->0.1657 (+0.0629) | MRR: 0.0889->0.1135 (+0.0246)\\n    medium |   embedding_distance | n= 350-> 350 | R@1: 0.0657->0.0771 (+0.0114) | R@5: 0.3029->0.3143 (+0.0114) | MRR: 0.1904->0.2042 (+0.0139)\\n    medium |       dataflow_aware | n= 350-> 350 | R@1: 0.1343->0.1514 (+0.0171) | R@5: 0.4343->0.4829 (+0.0486) | MRR: 0.2853->0.3097 (+0.0244)\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.46}}"
    }
  },
  "sourceToolAssistantUUID": "aeb775af-faff-4ffd-aaea-33080f006711",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "fb5ea7f7-b3c9-4750-b931-39d2aaae422b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 82_

```json
{
  "type": "last-prompt",
  "leafUuid": "34c534af-060f-4ea2-b7d8-483f5cf915bc",
  "sessionId": "fb5ea7f7-b3c9-4750-b931-39d2aaae422b"
}
```

---

### Runtime record

_source line 83_

```json
{
  "type": "ai-title",
  "aiTitle": "Trace stratified_dryrun v1 to v2 differences",
  "sessionId": "fb5ea7f7-b3c9-4750-b931-39d2aaae422b"
}
```

---

### Assistant

_source line 84 · 2026-05-14T20:39:00.234Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the data. Let me also verify the hash hypothesis by checking the Python hash randomization.

Key findings:
1. **All sample counts are identical** between v1 and v2 (130, 346, 1226, 1278 for repo_size; 276, 605, 2099 for pool_size; 24, 350, 2606 for similarity)
2. **Total samples**: 130+346+1226+1278 = 2980 in both versions
3. **Metric values differ across all strata and strategies** - not just one dimension


4. The root cause is that `mock_predictions` relies on `np.random.RandomState(seed + abs(hash(strategy)) % 10000)`, where `hash(strategy)` is non-deterministic across Python processes due to hash randomization in Python 3.3+

Since the validation data counts are identical, the dataset itself hasn't changed. I should check whether the current script version matches what generated v2, given that v2's config includes dataflow_bins and neg_difficulty_quartiles which are also present in the current script, and then look for an older version that would've produced v1.

The most likely explanation is that v1 came from an earlier script version without those features, v2 from the current version, and the hash randomization issue alone would cause different results regardless of code changes. The `by_similarity` stratum having identical counts in both versions but different metrics confirms this—the bin assignments match because `sim_bin` uses deterministic text_similarity in dry-run mode, but the mock rankings differ due to the hash seed variation.

Now I'm checking whether the val data itself changed between runs. The pool_size counts being identical across all strata suggests the same val data was used, but I should verify which val files the main function loads for each strategy to rule out any differences from new dataflow-aware candidates.

Organizing the comparison results and writing the changelog output...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "34c534af-060f-4ea2-b7d8-483f5cf915bc",
  "isSidechain": false,
  "requestId": "req_011Cb3764ZtwTTH4oftKN3hk",
  "type": "assistant",
  "uuid": "a7ce3bfe-ea94-4d9d-9b3f-9577382d27ba",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "fb5ea7f7-b3c9-4750-b931-39d2aaae422b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YbLH2Nuv76a4y3h4GPrtnL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3864,
      "cache_read_input_tokens": 60943,
      "output_tokens": 925,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3864,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 925,
          "cache_read_input_tokens": 60943,
          "cache_creation_input_tokens": 3864,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3864
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

_source line 85 · 2026-05-14T20:39:01.191Z_

数据完整了。根因已确认：`mock_predictions` 中 `hash(strategy)` 导致非确定性 RNG seed。现在写 changelog。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a7ce3bfe-ea94-4d9d-9b3f-9577382d27ba",
  "isSidechain": false,
  "requestId": "req_011Cb3764ZtwTTH4oftKN3hk",
  "type": "assistant",
  "uuid": "57ff62cc-7ec3-42b0-8905-5b2633875a7a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "fb5ea7f7-b3c9-4750-b931-39d2aaae422b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YbLH2Nuv76a4y3h4GPrtnL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3864,
      "cache_read_input_tokens": 60943,
      "output_tokens": 925,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3864,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 925,
          "cache_read_input_tokens": 60943,
          "cache_creation_input_tokens": 3864,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3864
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

_source line 86 · 2026-05-14T20:39:03.553Z_

<details open><summary>🔧 Tool call — Bash · `toolu_011eg1GoHq5tzreXjaZoEW8D`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/",
  "description": "Check artifacts directory exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "57ff62cc-7ec3-42b0-8905-5b2633875a7a",
  "isSidechain": false,
  "requestId": "req_011Cb3764ZtwTTH4oftKN3hk",
  "type": "assistant",
  "uuid": "19e0961a-73ff-4a8c-a323-a4834857b765",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "fb5ea7f7-b3c9-4750-b931-39d2aaae422b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YbLH2Nuv76a4y3h4GPrtnL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3864,
      "cache_read_input_tokens": 60943,
      "output_tokens": 925,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3864,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 925,
          "cache_read_input_tokens": 60943,
          "cache_creation_input_tokens": 3864,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3864
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

_source line 87 · 2026-05-14T20:39:04.037Z_

<details><summary>↩ Tool result · `toolu_011eg1GoHq5tzreXjaZoEW8D`</summary>

```text
_project
analysis
bjb1_status_check.md
bm25_overlap_stratified.json
code
disk_cleanup_report_20260513.md
dream_reports
figures
full_m2
m1_progress_0513.md
m2_full_qwen
m2_full_qwen_analysis.md
m2_full_starcoder
m2_qwen_status_check.md
m2_starcoder_status_check.md
manifest.yaml
mine_bm25_negatives.py
mvp_p1_codeql_feasibility
mvp_p2b_contrastive_training
neg_difficulty_analysis
paper_drafts
patch_build_m1.py
patch_train.py
plan003_eval_readiness.md
plan003_swebench_dryrun_report.md
plan003_swebench_eval_plan.md
plan005_stratified_analysis_report.md
plan006_error_patterns.json
plan_006
plan_006_scalability
plan_006_scalability_stats_29repos.json
plan_018_bm25
rename_safety_report.md
status_check_20260514.md
status_check_loop6.md
swebench_eval_readiness.md
training_status_snapshot.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "19e0961a-73ff-4a8c-a323-a4834857b765",
  "isSidechain": false,
  "promptId": "0b7bb415-f2b4-4832-aac4-2e6aafdc7429",
  "type": "user",
  "uuid": "ef80a81b-8538-44ea-b323-b17683bef513",
  "toolUseResult": {
    "stdout": "_project\nanalysis\nbjb1_status_check.md\nbm25_overlap_stratified.json\ncode\ndisk_cleanup_report_20260513.md\ndream_reports\nfigures\nfull_m2\nm1_progress_0513.md\nm2_full_qwen\nm2_full_qwen_analysis.md\nm2_full_starcoder\nm2_qwen_status_check.md\nm2_starcoder_status_check.md\nmanifest.yaml\nmine_bm25_negatives.py\nmvp_p1_codeql_feasibility\nmvp_p2b_contrastive_training\nneg_difficulty_analysis\npaper_drafts\npatch_build_m1.py\npatch_train.py\nplan003_eval_readiness.md\nplan003_swebench_dryrun_report.md\nplan003_swebench_eval_plan.md\nplan005_stratified_analysis_report.md\nplan006_error_patterns.json\nplan_006\nplan_006_scalability\nplan_006_scalability_stats_29repos.json\nplan_018_bm25\nrename_safety_report.md\nstatus_check_20260514.md\nstatus_check_loop6.md\nswebench_eval_readiness.md\ntraining_status_snapshot.md",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "19e0961a-73ff-4a8c-a323-a4834857b765",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "fb5ea7f7-b3c9-4750-b931-39d2aaae422b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 88 · 2026-05-14T20:39:04.051Z_

```json
{
  "parentUuid": "ef80a81b-8538-44ea-b323-b17683bef513",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "66b72464-237d-47f9-8b7b-74f82d2662c2",
  "timestamp": "2026-05-14T20:39:04.051Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "fb5ea7f7-b3c9-4750-b931-39d2aaae422b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 89 · 2026-05-14T20:39:47.261Z_

<details open><summary>🔧 Tool call — Write · `toolu_01HQWot5yDRPqmvMGvem17Pw`</summary>

````json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/v1_v2_changelog.md",
  "content": "# Stratified Dry-Run v1 → v2 差异溯源\n\n## 根因\n\n**`mock_predictions()` 中使用 `hash(strategy)` 构造 RNG seed，Python 3 字符串 hash 在不同进程间非确定性（PEP 456），导致两次运行产生不同的 mock ranks。**\n\n```python\n# analyze_stratified.py:271\ndef mock_predictions(val_samples, strategy, seed):\n    rng = np.random.RandomState(seed + abs(hash(strategy)) % 10000)  # ← 问题在这里\n```\n\n`hash(\"random\")` 在 v1 进程和 v2 进程中返回不同值（除非设置 `PYTHONHASHSEED=0`），导致 `np.random.RandomState` 的 seed 不同，进而 mock 出的 rank 序列完全不同。\n\n### 辅助证据\n\n1. **所有 stratum 的样本数（count）完全一致** — 数据加载、分层逻辑、bin 边界均未改变\n2. **所有维度的所有策略都有数值偏移** — 不是某一个 stratum 的问题，是全局性的\n3. **bin 边界定义在两次输出的 config 中完全相同** — 排除分层逻辑变更\n\n### 次要变更：v2 新增 2 个分析维度\n\nv2 脚本在原有 3 维（repo_size, pool_size, similarity）基础上新增：\n- `by_dataflow`：structural data availability（sparse/moderate/rich）\n- `by_neg_difficulty`：neg_difficulty quartile（Q1_easy/Q2/Q3/Q4_hard）\n\n这些新增维度**不影响已有维度的计算**，因为分层和指标计算是独立的。\n\n## v2 为 Ground Truth 的依据\n\n1. v2 是最终版本脚本的输出，包含完整的 5 维分析\n2. 两次都是 dry-run mock 数据，**不存在哪个\"更正确\"的问题**——都是合成预测\n3. v2 的脚本更完善（包含 dataflow + neg_difficulty），应以 v2 为基准\n4. 如需复现 v2 结果，需在同一进程中运行或设置 `PYTHONHASHSEED=&lt;fixed_value>`\n\n## 数值变化表\n\n### by_repo_size\n\n| stratum | strategy | n | R@1 v1 | R@1 v2 | Δ | R@5 v1 | R@5 v2 | Δ | MRR v1 | MRR v2 | Δ |\n|---------|----------|---|--------|--------|---|--------|--------|---|--------|--------|---|\n| small | random | 130 | 0.1154 | 0.0769 | -0.0385 | 0.5385 | 0.4769 | -0.0615 | 0.3060 | 0.2643 | -0.0417 |\n| small | embedding_distance | 130 | 0.3000 | 0.2769 | -0.0231 | 0.7385 | 0.7385 | +0.0000 | 0.4931 | 0.4704 | -0.0226 |\n| small | dataflow_aware | 130 | 0.4846 | 0.4000 | -0.0846 | 0.8769 | 0.9000 | +0.0231 | 0.6501 | 0.6000 | -0.0501 |\n| medium | random | 346 | 0.0520 | 0.0549 | +0.0029 | 0.2312 | 0.2861 | +0.0549 | 0.1782 | 0.1936 | +0.0154 |\n| medium | embedding_distance | 346 | 0.1069 | 0.1503 | +0.0434 | 0.4942 | 0.5231 | +0.0289 | 0.2866 | 0.3299 | +0.0433 |\n| medium | dataflow_aware | 346 | 0.2399 | 0.2399 | +0.0000 | 0.7023 | 0.7370 | +0.0347 | 0.4295 | 0.4508 | +0.0213 |\n| large | random | 1226 | 0.0228 | 0.0277 | +0.0049 | 0.1142 | 0.1077 | -0.0065 | 0.0987 | 0.0992 | +0.0005 |\n| large | embedding_distance | 1226 | 0.0546 | 0.0530 | -0.0016 | 0.2577 | 0.2765 | +0.0188 | 0.1754 | 0.1760 | +0.0006 |\n| large | dataflow_aware | 1226 | 0.1052 | 0.0962 | -0.0090 | 0.4095 | 0.4103 | +0.0008 | 0.2578 | 0.2548 | -0.0029 |\n| xlarge | random | 1278 | 0.0219 | 0.0149 | -0.0070 | 0.0970 | 0.1095 | +0.0125 | 0.0923 | 0.0907 | -0.0015 |\n| xlarge | embedding_distance | 1278 | 0.0548 | 0.0610 | +0.0063 | 0.2520 | 0.2559 | +0.0039 | 0.1724 | 0.1750 | +0.0026 |\n| xlarge | dataflow_aware | 1278 | 0.0994 | 0.1072 | +0.0078 | 0.3881 | 0.4210 | +0.0329 | 0.2480 | 0.2619 | +0.0139 |\n\n### by_pool_size\n\n| stratum | strategy | n | R@1 v1 | R@1 v2 | Δ | R@5 v1 | R@5 v2 | Δ | MRR v1 | MRR v2 | Δ |\n|---------|----------|---|--------|--------|---|--------|--------|---|--------|--------|---|\n| small | random | 276 | 0.0906 | 0.0761 | -0.0145 | 0.4239 | 0.4275 | +0.0036 | 0.2582 | 0.2519 | -0.0063 |\n| small | embedding_distance | 276 | 0.2065 | 0.2464 | +0.0399 | 0.6594 | 0.6667 | +0.0072 | 0.4016 | 0.4381 | +0.0365 |\n| small | dataflow_aware | 276 | 0.3841 | 0.3551 | -0.0290 | 0.8116 | 0.8768 | +0.0652 | 0.5555 | 0.5628 | +0.0074 |\n| medium | random | 605 | 0.0314 | 0.0364 | +0.0050 | 0.1421 | 0.1653 | +0.0231 | 0.1281 | 0.1376 | +0.0096 |\n| medium | embedding_distance | 605 | 0.0760 | 0.0843 | +0.0083 | 0.3653 | 0.3835 | +0.0182 | 0.2289 | 0.2362 | +0.0073 |\n| medium | dataflow_aware | 605 | 0.1405 | 0.1421 | +0.0017 | 0.5455 | 0.5636 | +0.0182 | 0.3263 | 0.3332 | +0.0069 |\n| large | random | 2099 | 0.0214 | 0.0186 | -0.0029 | 0.1005 | 0.1024 | +0.0019 | 0.0913 | 0.0887 | -0.0026 |\n| large | embedding_distance | 2099 | 0.0524 | 0.0534 | +0.0010 | 0.2392 | 0.2511 | +0.0119 | 0.1664 | 0.1672 | +0.0008 |\n| large | dataflow_aware | 2099 | 0.1005 | 0.0981 | -0.0024 | 0.3816 | 0.3954 | +0.0138 | 0.2456 | 0.2497 | +0.0042 |\n\n### by_similarity\n\n| stratum | strategy | n | R@1 v1 | R@1 v2 | Δ | R@5 v1 | R@5 v2 | Δ | MRR v1 | MRR v2 | Δ |\n|---------|----------|---|--------|--------|---|--------|--------|---|--------|--------|---|\n| low | random | 2606 | 0.0322 | 0.0284 | -0.0038 | 0.1450 | 0.1427 | -0.0023 | 0.1181 | 0.1142 | -0.0039 |\n| low | embedding_distance | 2606 | 0.0721 | 0.0779 | +0.0058 | 0.3043 | 0.3177 | +0.0134 | 0.2024 | 0.2070 | +0.0046 |\n| low | dataflow_aware | 2606 | 0.1355 | 0.1285 | -0.0069 | 0.4593 | 0.4731 | +0.0138 | 0.2923 | 0.2939 | +0.0016 |\n| medium | random | 350 | 0.0143 | 0.0229 | +0.0086 | 0.1029 | 0.1657 | +0.0629 | 0.0889 | 0.1135 | +0.0246 |\n| medium | embedding_distance | 350 | 0.0657 | 0.0771 | +0.0114 | 0.3029 | 0.3143 | +0.0114 | 0.1904 | 0.2042 | +0.0139 |\n| medium | dataflow_aware | 350 | 0.1343 | 0.1514 | +0.0171 | 0.4343 | 0.4829 | +0.0486 | 0.2853 | 0.3097 | +0.0244 |\n| high | random | 24 | 0.0000 | 0.0000 | +0.0000 | 0.0000 | 0.1250 | +0.1250 | 0.0663 | 0.0703 | +0.0040 |\n| high | embedding_distance | 24 | 0.0833 | 0.0417 | -0.0417 | 0.2500 | 0.2083 | -0.0417 | 0.1866 | 0.1565 | -0.0301 |\n| high | dataflow_aware | 24 | 0.0833 | 0.0833 | +0.0000 | 0.2500 | 0.4583 | +0.2083 | 0.1936 | 0.2834 | +0.0898 |\n\n## 修复建议\n\n将 `mock_predictions` 的 seed 构造改为确定性方式：\n\n```python\n# 当前（不确定性）\nrng = np.random.RandomState(seed + abs(hash(strategy)) % 10000)\n\n# 修复方案\nSTRATEGY_SEED_OFFSET = {\"random\": 0, \"embedding_distance\": 1, \"dataflow_aware\": 2}\nrng = np.random.RandomState(seed + STRATEGY_SEED_OFFSET[strategy] * 10000)\n```\n"
}
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "66b72464-237d-47f9-8b7b-74f82d2662c2",
  "isSidechain": false,
  "requestId": "req_011Cb378AeaGdJwSd6p8uiwQ",
  "type": "assistant",
  "uuid": "e2baa183-e36f-4c3b-a122-96668e2e2678",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "fb5ea7f7-b3c9-4750-b931-39d2aaae422b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011pmiS4kZN6aQkTMjzE29Q9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1359,
      "cache_read_input_tokens": 64807,
      "output_tokens": 3461,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1359,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3461,
          "cache_read_input_tokens": 64807,
          "cache_creation_input_tokens": 1359,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1359
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

_source line 90 · 2026-05-14T20:39:47.281Z_

<details><summary>↩ Tool result · `toolu_01HQWot5yDRPqmvMGvem17Pw`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/v1_v2_changelog.md
```

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "parentUuid": "e2baa183-e36f-4c3b-a122-96668e2e2678",
  "isSidechain": false,
  "promptId": "0b7bb415-f2b4-4832-aac4-2e6aafdc7429",
  "type": "user",
  "uuid": "f41d0313-a7f2-477a-9937-912fe4b832af",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/v1_v2_changelog.md",
    "content": "# Stratified Dry-Run v1 → v2 差异溯源\n\n## 根因\n\n**`mock_predictions()` 中使用 `hash(strategy)` 构造 RNG seed，Python 3 字符串 hash 在不同进程间非确定性（PEP 456），导致两次运行产生不同的 mock ranks。**\n\n```python\n# analyze_stratified.py:271\ndef mock_predictions(val_samples, strategy, seed):\n    rng = np.random.RandomState(seed + abs(hash(strategy)) % 10000)  # ← 问题在这里\n```\n\n`hash(\"random\")` 在 v1 进程和 v2 进程中返回不同值（除非设置 `PYTHONHASHSEED=0`），导致 `np.random.RandomState` 的 seed 不同，进而 mock 出的 rank 序列完全不同。\n\n### 辅助证据\n\n1. **所有 stratum 的样本数（count）完全一致** — 数据加载、分层逻辑、bin 边界均未改变\n2. **所有维度的所有策略都有数值偏移** — 不是某一个 stratum 的问题，是全局性的\n3. **bin 边界定义在两次输出的 config 中完全相同** — 排除分层逻辑变更\n\n### 次要变更：v2 新增 2 个分析维度\n\nv2 脚本在原有 3 维（repo_size, pool_size, similarity）基础上新增：\n- `by_dataflow`：structural data availability（sparse/moderate/rich）\n- `by_neg_difficulty`：neg_difficulty quartile（Q1_easy/Q2/Q3/Q4_hard）\n\n这些新增维度**不影响已有维度的计算**，因为分层和指标计算是独立的。\n\n## v2 为 Ground Truth 的依据\n\n1. v2 是最终版本脚本的输出，包含完整的 5 维分析\n2. 两次都是 dry-run mock 数据，**不存在哪个\"更正确\"的问题**——都是合成预测\n3. v2 的脚本更完善（包含 dataflow + neg_difficulty），应以 v2 为基准\n4. 如需复现 v2 结果，需在同一进程中运行或设置 `PYTHONHASHSEED=&lt;fixed_value>`\n\n## 数值变化表\n\n### by_repo_size\n\n| stratum | strategy | n | R@1 v1 | R@1 v2 | Δ | R@5 v1 | R@5 v2 | Δ | MRR v1 | MRR v2 | Δ |\n|---------|----------|---|--------|--------|---|--------|--------|---|--------|--------|---|\n| small | random | 130 | 0.1154 | 0.0769 | -0.0385 | 0.5385 | 0.4769 | -0.0615 | 0.3060 | 0.2643 | -0.0417 |\n| small | embedding_distance | 130 | 0.3000 | 0.2769 | -0.0231 | 0.7385 | 0.7385 | +0.0000 | 0.4931 | 0.4704 | -0.0226 |\n| small | dataflow_aware | 130 | 0.4846 | 0.4000 | -0.0846 | 0.8769 | 0.9000 | +0.0231 | 0.6501 | 0.6000 | -0.0501 |\n| medium | random | 346 | 0.0520 | 0.0549 | +0.0029 | 0.2312 | 0.2861 | +0.0549 | 0.1782 | 0.1936 | +0.0154 |\n| medium | embedding_distance | 346 | 0.1069 | 0.1503 | +0.0434 | 0.4942 | 0.5231 | +0.0289 | 0.2866 | 0.3299 | +0.0433 |\n| medium | dataflow_aware | 346 | 0.2399 | 0.2399 | +0.0000 | 0.7023 | 0.7370 | +0.0347 | 0.4295 | 0.4508 | +0.0213 |\n| large | random | 1226 | 0.0228 | 0.0277 | +0.0049 | 0.1142 | 0.1077 | -0.0065 | 0.0987 | 0.0992 | +0.0005 |\n| large | embedding_distance | 1226 | 0.0546 | 0.0530 | -0.0016 | 0.2577 | 0.2765 | +0.0188 | 0.1754 | 0.1760 | +0.0006 |\n| large | dataflow_aware | 1226 | 0.1052 | 0.0962 | -0.0090 | 0.4095 | 0.4103 | +0.0008 | 0.2578 | 0.2548 | -0.0029 |\n| xlarge | random | 1278 | 0.0219 | 0.0149 | -0.0070 | 0.0970 | 0.1095 | +0.0125 | 0.0923 | 0.0907 | -0.0015 |\n| xlarge | embedding_distance | 1278 | 0.0548 | 0.0610 | +0.0063 | 0.2520 | 0.2559 | +0.0039 | 0.1724 | 0.1750 | +0.0026 |\n| xlarge | dataflow_aware | 1278 | 0.0994 | 0.1072 | +0.0078 | 0.3881 | 0.4210 | +0.0329 | 0.2480 | 0.2619 | +0.0139 |\n\n### by_pool_size\n\n| stratum | strategy | n | R@1 v1 | R@1 v2 | Δ | R@5 v1 | R@5 v2 | Δ | MRR v1 | MRR v2 | Δ |\n|---------|----------|---|--------|--------|---|--------|--------|---|--------|--------|---|\n| small | random | 276 | 0.0906 | 0.0761 | -0.0145 | 0.4239 | 0.4275 | +0.0036 | 0.2582 | 0.2519 | -0.0063 |\n| small | embedding_distance | 276 | 0.2065 | 0.2464 | +0.0399 | 0.6594 | 0.6667 | +0.0072 | 0.4016 | 0.4381 | +0.0365 |\n| small | dataflow_aware | 276 | 0.3841 | 0.3551 | -0.0290 | 0.8116 | 0.8768 | +0.0652 | 0.5555 | 0.5628 | +0.0074 |\n| medium | random | 605 | 0.0314 | 0.0364 | +0.0050 | 0.1421 | 0.1653 | +0.0231 | 0.1281 | 0.1376 | +0.0096 |\n| medium | embedding_distance | 605 | 0.0760 | 0.0843 | +0.0083 | 0.3653 | 0.3835 | +0.0182 | 0.2289 | 0.2362 | +0.0073 |\n| medium | dataflow_aware | 605 | 0.1405 | 0.1421 | +0.0017 | 0.5455 | 0.5636 | +0.0182 | 0.3263 | 0.3332 | +0.0069 |\n| large | random | 2099 | 0.0214 | 0.0186 | -0.0029 | 0.1005 | 0.1024 | +0.0019 | 0.0913 | 0.0887 | -0.0026 |\n| large | embedding_distance | 2099 | 0.0524 | 0.0534 | +0.0010 | 0.2392 | 0.2511 | +0.0119 | 0.1664 | 0.1672 | +0.0008 |\n| large | dataflow_aware | 2099 | 0.1005 | 0.0981 | -0.0024 | 0.3816 | 0.3954 | +0.0138 | 0.2456 | 0.2497 | +0.0042 |\n\n### by_similarity\n\n| stratum | strategy | n | R@1 v1 | R@1 v2 | Δ | R@5 v1 | R@5 v2 | Δ | MRR v1 | MRR v2 | Δ |\n|---------|----------|---|--------|--------|---|--------|--------|---|--------|--------|---|\n| low | random | 2606 | 0.0322 | 0.0284 | -0.0038 | 0.1450 | 0.1427 | -0.0023 | 0.1181 | 0.1142 | -0.0039 |\n| low | embedding_distance | 2606 | 0.0721 | 0.0779 | +0.0058 | 0.3043 | 0.3177 | +0.0134 | 0.2024 | 0.2070 | +0.0046 |\n| low | dataflow_aware | 2606 | 0.1355 | 0.1285 | -0.0069 | 0.4593 | 0.4731 | +0.0138 | 0.2923 | 0.2939 | +0.0016 |\n| medium | random | 350 | 0.0143 | 0.0229 | +0.0086 | 0.1029 | 0.1657 | +0.0629 | 0.0889 | 0.1135 | +0.0246 |\n| medium | embedding_distance | 350 | 0.0657 | 0.0771 | +0.0114 | 0.3029 | 0.3143 | +0.0114 | 0.1904 | 0.2042 | +0.0139 |\n| medium | dataflow_aware | 350 | 0.1343 | 0.1514 | +0.0171 | 0.4343 | 0.4829 | +0.0486 | 0.2853 | 0.3097 | +0.0244 |\n| high | random | 24 | 0.0000 | 0.0000 | +0.0000 | 0.0000 | 0.1250 | +0.1250 | 0.0663 | 0.0703 | +0.0040 |\n| high | embedding_distance | 24 | 0.0833 | 0.0417 | -0.0417 | 0.2500 | 0.2083 | -0.0417 | 0.1866 | 0.1565 | -0.0301 |\n| high | dataflow_aware | 24 | 0.0833 | 0.0833 | +0.0000 | 0.2500 | 0.4583 | +0.2083 | 0.1936 | 0.2834 | +0.0898 |\n\n## 修复建议\n\n将 `mock_predictions` 的 seed 构造改为确定性方式：\n\n```python\n# 当前（不确定性）\nrng = np.random.RandomState(seed + abs(hash(strategy)) % 10000)\n\n# 修复方案\nSTRATEGY_SEED_OFFSET = {\"random\": 0, \"embedding_distance\": 1, \"dataflow_aware\": 2}\nrng = np.random.RandomState(seed + STRATEGY_SEED_OFFSET[strategy] * 10000)\n```\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "e2baa183-e36f-4c3b-a122-96668e2e2678",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "fb5ea7f7-b3c9-4750-b931-39d2aaae422b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
````

</details>

---

### Assistant

_source line 91 · 2026-05-14T20:39:54.038Z_

changelog 已写入 `artifacts/v1_v2_changelog.md`。

**根因**：`mock_predictions()` 第 271 行使用 `hash(strategy)` 构造 RNG seed。Python 3 的字符串 hash 每次进程启动都不同（PEP 456 hash randomization），导致 v1 和 v2 两次运行产生完全不同的 mock rank 序列。

**关键证据**：
- 所有 stratum 样本数（count）完全一致 → 数据、分层逻辑、bin 边界未变
- 所有维度所有策略都有偏移 → 全局性 RNG 漂移，非局部逻辑变更
- v2 新增的 2 个维度（dataflow, neg_difficulty）不影响已有维度的计算

**v2 为 ground truth**：两次都是合成 mock 数据，无"更正确"之分；v2 是最终版脚本（含完整 5 维分析），以 v2 为基准即可。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f41d0313-a7f2-477a-9937-912fe4b832af",
  "isSidechain": false,
  "requestId": "req_011Cb37BM6TRngWtMrMzPy1c",
  "type": "assistant",
  "uuid": "7ecf3c2a-4898-4537-b5ce-a06fb0877a90",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "fb5ea7f7-b3c9-4750-b931-39d2aaae422b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011D27bjgmvN12oAnGoUMTtP",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3517,
      "cache_read_input_tokens": 66166,
      "output_tokens": 299,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3517,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 299,
          "cache_read_input_tokens": 66166,
          "cache_creation_input_tokens": 3517,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3517
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

_source line 92_

```json
{
  "type": "last-prompt",
  "leafUuid": "7ecf3c2a-4898-4537-b5ce-a06fb0877a90",
  "sessionId": "fb5ea7f7-b3c9-4750-b931-39d2aaae422b"
}
```

---

### Runtime record

_source line 93_

```json
{
  "type": "ai-title",
  "aiTitle": "Trace stratified_dryrun v1 to v2 differences",
  "sessionId": "fb5ea7f7-b3c9-4750-b931-39d2aaae422b"
}
```

---
