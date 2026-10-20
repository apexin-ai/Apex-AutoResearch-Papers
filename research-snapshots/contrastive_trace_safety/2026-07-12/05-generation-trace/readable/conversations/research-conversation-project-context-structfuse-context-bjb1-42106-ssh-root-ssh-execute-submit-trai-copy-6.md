# Research conversation: <project_context> # 项目: structfuse-context ## 运行环境 - 服务器名: bjb1-42106 - SSH 账户: root（调用 ssh_execute / submit_training_jo

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 142
- **Recorded user turns:** 1
- **Tool calls:** 40
- **Original source:** `logs/chats/exported-trajectories/account-1/bda3dfbf-4b90-494d-b674-2597173fd381.jsonl`
- **Structured JSON:** [`ec14786eead088818683.json`](../../sessions/ec/ec14786eead088818683.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-14T20:46:26.725Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-14T20:46:26.725Z",
  "sessionId": "bda3dfbf-4b90-494d-b674-2597173fd381",
  "content": "&lt;project_context>\n# 项目: structfuse-context\n\n## 运行环境\n- 服务器名: bjb1-42106\n- SSH 账户: root（调用 ssh_execute / submit_training_job 时传入 account=\"root\"）\n- SSH 连接命令: ssh connect.bjb1.seetacloud.com  # 必须用此命令，~/.ssh/config 自动应用密钥和跳板机，禁止用裸 IP\n- 项目代码根目录: /root/structfuse\n\n\n## 环境搭建\n连接服务器后先调 `detect_image` 检测是否为预置镜像。如果匹配，跳过基础环境搭建，只装项目特有依赖。已预装的包不要重复安装。\n\n## 输出风格\n回复简洁直接。只输出执行结果和必要信息，不要解释过程、不要客套、不要给未被要求的建议。\n&lt;/project_context>\n## 任务：编写 plan_005 真实分层评估脚本\n\n### 背景\nplan_005 需要对 M2 训练出的 checkpoint 做分层评估。现有 `analyze_stratified.py` 已有 5 维度分层逻辑（repo_size, pool_size, similarity, dataflow_availability, neg_difficulty）。但 Director 要求：\n\n1. 真实评估脚本需要**接收 checkpoint 路径作为输入**（不是 dry-run mock）\n2. 新增**按 pool_size 控制变量**后的对比——confound 分析发现 pool_size 是真正 confound（非 repo_size），rich-dataflow instances 候选池更大导致 R@1 天然更低\n3. 修复 `mock_predictions()` 的确定性 seed（顺手改，低优先级）\n\n### 你要做的\n\n#### 1. 读现有脚本\nSSH 到 bjb1-42106，读取：\n- `/root/structfuse/evaluation/analyze_stratified.py`（910 行，现有脚本）\n- `/root/structfuse/evaluation/eval_retrieval.py`（如果存在，了解现有 eval 接口）\n\n#### 2. 修改 analyze_stratified.py，增加以下功能\n\n**A. pool_size 控制变量对比（核心新增）**：\n- 新增分析模式：在同一 pool_size bin 内，比较不同策略的 R@1\n- 实现 pool_size-matched 对比：对每个 (pool_size_bin, strategy) 组合计算 R@1，然后做 within-bin delta\n- 这样可以排除 \"rich-dataflow 的候选池更大导致 R@1 低\" 的 confound\n- 输出包含 pool_size_controlled_delta 表格\n\n**B. 按 dataflow richness 分层 + 控制 pool_size**：\n- 交叉分析：(dataflow_richness_bin × pool_size_bin) → R@1\n- 如果某个交叉格子样本量 < 30，标注 \"underpowered\"\n\n**C. 修复 mock_predictions 的确定性 seed**：\n```python\n# 当前（不确定性）\nrng = np.random.RandomState(seed + abs(hash(strategy)) % 10000)\n\n# 修复方案\nSTRATEGY_SEED_OFFSET = {\"random\": 0, \"embedding_distance\": 1, \"dataflow_aware\": 2, \"bm25\": 3}\nrng = np.random.RandomState(seed + STRATEGY_SEED_OFFSET.get(strategy, hash(strategy) % 10000) * 10000)\n```\n\n#### 3. 确保脚本可以直接接收 checkpoint 路径运行\n\n验证 `--checkpoints-dir` 模式正常工作（检查 checkpoint 发现逻辑：查找 best_by_recall_at_1/ 或 best/ 目录下的 model 文件）。\n\n#### 4. 写完后用 dry-run 验证\n\n```bash\ncd /root/structfuse && python3 evaluation/analyze_stratified.py \\\n  --m1-data /root/autodl-tmp/structfuse/full_m1_data/all.jsonl \\\n  --val-data-dir /root/autodl-tmp/structfuse/full_m2_training_data \\\n  --dataflow-graph /root/autodl-tmp/structfuse/full_m2_training_data/dataflow_graph.json \\\n  --output-dir /root/autodl-tmp/structfuse/artifacts/stratified_dryrun_v3 \\\n  --dry-run --seeds 42 --n-bootstrap 200\n```\n\n确认 v3 输出包含：\n- 原有 5 维度分层结果\n- 新增 pool_size-controlled delta 表\n- 新增 (dataflow × pool_size) 交叉分析\n\n### 代码规范\n- 文件顶部注释说明用途、输入输出\n- 新增函数写 docstring（目的、参数、返回值）\n- pool_size 控制逻辑需要注释说明 confound 背景\n\n### 服务器信息\n- 服务器: bjb1-42106\n- 环境: `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`\n- Python: /root/miniconda3/bin/python3\n- **禁止占用 GPU**——只改脚本和做 dry-run（CPU）"
}
````

---

### Runtime record

_source line 2 · 2026-05-14T20:46:26.729Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-14T20:46:26.729Z",
  "sessionId": "bda3dfbf-4b90-494d-b674-2597173fd381"
}
```

---

## Round 1

140 recorded events

### User

_source line 3 · 2026-05-14T20:46:26.772Z_

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
## 任务：编写 plan_005 真实分层评估脚本

### 背景
plan_005 需要对 M2 训练出的 checkpoint 做分层评估。现有 `analyze_stratified.py` 已有 5 维度分层逻辑（repo_size, pool_size, similarity, dataflow_availability, neg_difficulty）。但 Director 要求：

1. 真实评估脚本需要**接收 checkpoint 路径作为输入**（不是 dry-run mock）
2. 新增**按 pool_size 控制变量**后的对比——confound 分析发现 pool_size 是真正 confound（非 repo_size），rich-dataflow instances 候选池更大导致 R@1 天然更低
3. 修复 `mock_predictions()` 的确定性 seed（顺手改，低优先级）

### 你要做的

#### 1. 读现有脚本
SSH 到 bjb1-42106，读取：
- `/root/structfuse/evaluation/analyze_stratified.py`（910 行，现有脚本）
- `/root/structfuse/evaluation/eval_retrieval.py`（如果存在，了解现有 eval 接口）

#### 2. 修改 analyze_stratified.py，增加以下功能

**A. pool_size 控制变量对比（核心新增）**：
- 新增分析模式：在同一 pool_size bin 内，比较不同策略的 R@1
- 实现 pool_size-matched 对比：对每个 (pool_size_bin, strategy) 组合计算 R@1，然后做 within-bin delta
- 这样可以排除 "rich-dataflow 的候选池更大导致 R@1 低" 的 confound
- 输出包含 pool_size_controlled_delta 表格

**B. 按 dataflow richness 分层 + 控制 pool_size**：
- 交叉分析：(dataflow_richness_bin × pool_size_bin) → R@1
- 如果某个交叉格子样本量 < 30，标注 "underpowered"

**C. 修复 mock_predictions 的确定性 seed**：
```python
# 当前（不确定性）
rng = np.random.RandomState(seed + abs(hash(strategy)) % 10000)

# 修复方案
STRATEGY_SEED_OFFSET = {"random": 0, "embedding_distance": 1, "dataflow_aware": 2, "bm25": 3}
rng = np.random.RandomState(seed + STRATEGY_SEED_OFFSET.get(strategy, hash(strategy) % 10000) * 10000)
```

#### 3. 确保脚本可以直接接收 checkpoint 路径运行

验证 `--checkpoints-dir` 模式正常工作（检查 checkpoint 发现逻辑：查找 best_by_recall_at_1/ 或 best/ 目录下的 model 文件）。

#### 4. 写完后用 dry-run 验证

```bash
cd /root/structfuse && python3 evaluation/analyze_stratified.py \
  --m1-data /root/autodl-tmp/structfuse/full_m1_data/all.jsonl \
  --val-data-dir /root/autodl-tmp/structfuse/full_m2_training_data \
  --dataflow-graph /root/autodl-tmp/structfuse/full_m2_training_data/dataflow_graph.json \
  --output-dir /root/autodl-tmp/structfuse/artifacts/stratified_dryrun_v3 \
  --dry-run --seeds 42 --n-bootstrap 200
```

确认 v3 输出包含：
- 原有 5 维度分层结果
- 新增 pool_size-controlled delta 表
- 新增 (dataflow × pool_size) 交叉分析

### 代码规范
- 文件顶部注释说明用途、输入输出
- 新增函数写 docstring（目的、参数、返回值）
- pool_size 控制逻辑需要注释说明 confound 背景

### 服务器信息
- 服务器: bjb1-42106
- 环境: `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- Python: /root/miniconda3/bin/python3
- **禁止占用 GPU**——只改脚本和做 dry-run（CPU）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "22ffd1fb-240e-481f-9bcc-b3f6a42d6805",
  "type": "user",
  "uuid": "7a52b327-ebc8-4a0b-a45f-a9fca0029cc2",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "bda3dfbf-4b90-494d-b674-2597173fd381",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-14T20:46:26.771Z_

```json
{
  "parentUuid": "7a52b327-ebc8-4a0b-a45f-a9fca0029cc2",
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
      "mcp__agent-ml-research__detect_image",
      "mcp__agent-ml-research__kill_job",
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
      "mcp__agent-ml-research__detect_image",
      "mcp__agent-ml-research__kill_job",
      "mcp__agent-ml-research__ssh_execute",
      "mcp__agent-ml-research__ssh_read_only"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "494f5a0f-7836-45dc-b8fd-f9d23dacf3b8",
  "timestamp": "2026-05-14T20:46:26.771Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "bda3dfbf-4b90-494d-b674-2597173fd381",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-14T20:46:26.771Z_

```json
{
  "parentUuid": "494f5a0f-7836-45dc-b8fd-f9d23dacf3b8",
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
  "uuid": "d056a1fc-9c19-45ca-be07-cd56dc352d85",
  "timestamp": "2026-05-14T20:46:26.771Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "bda3dfbf-4b90-494d-b674-2597173fd381",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6 · 2026-05-14T20:46:26.771Z_

```json
{
  "parentUuid": "d056a1fc-9c19-45ca-be07-cd56dc352d85",
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
  "uuid": "8bf9418a-e48f-4312-b9a7-031959c0f311",
  "timestamp": "2026-05-14T20:46:26.771Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "bda3dfbf-4b90-494d-b674-2597173fd381",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 7 · 2026-05-14T20:46:26.771Z_

```json
{
  "parentUuid": "8bf9418a-e48f-4312-b9a7-031959c0f311",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "4fac1f7d-e5b7-4c02-863c-e152ec3ac51a",
  "timestamp": "2026-05-14T20:46:26.771Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "bda3dfbf-4b90-494d-b674-2597173fd381",
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
  "aiTitle": "Add pool-size controlled stratified evaluation to analysis script",
  "sessionId": "bda3dfbf-4b90-494d-b674-2597173fd381"
}
```

---

### Assistant

_source line 9 · 2026-05-14T20:46:30.169Z_

<details><summary>Logged reasoning block</summary>

```text
Let me start by reading the existing scripts on the server to understand the current codebase before making modifications.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4fac1f7d-e5b7-4c02-863c-e152ec3ac51a",
  "isSidechain": false,
  "requestId": "req_011Cb37go4Da1wD1TyvZ2CJh",
  "type": "assistant",
  "uuid": "73714f8d-cbb4-4fa7-a185-8b7120f1dfe0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "bda3dfbf-4b90-494d-b674-2597173fd381",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017DdZjDSRB2NVr8KCn1xNb7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12395,
      "cache_read_input_tokens": 11447,
      "output_tokens": 166,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12395,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 166,
          "cache_read_input_tokens": 11447,
          "cache_creation_input_tokens": 12395,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12395
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

_source line 10 · 2026-05-14T20:46:30.174Z_

先读取服务器上的现有脚本。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "73714f8d-cbb4-4fa7-a185-8b7120f1dfe0",
  "isSidechain": false,
  "requestId": "req_011Cb37go4Da1wD1TyvZ2CJh",
  "type": "assistant",
  "uuid": "bb619eb2-fe23-46d9-9f54-88ae56fa97bc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "bda3dfbf-4b90-494d-b674-2597173fd381",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017DdZjDSRB2NVr8KCn1xNb7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12395,
      "cache_read_input_tokens": 11447,
      "output_tokens": 166,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12395,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 166,
          "cache_read_input_tokens": 11447,
          "cache_creation_input_tokens": 12395,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12395
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

_source line 11 · 2026-05-14T20:46:31.178Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01DAKyd8AtMWHQi61jaoufnH`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__detect_image",
  "max_results": 3
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bb619eb2-fe23-46d9-9f54-88ae56fa97bc",
  "isSidechain": false,
  "requestId": "req_011Cb37go4Da1wD1TyvZ2CJh",
  "type": "assistant",
  "uuid": "cf90a49e-c24e-475d-b18d-8b10ae3bbdb0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "bda3dfbf-4b90-494d-b674-2597173fd381",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017DdZjDSRB2NVr8KCn1xNb7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12395,
      "cache_read_input_tokens": 11447,
      "output_tokens": 166,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12395,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 166,
          "cache_read_input_tokens": 11447,
          "cache_creation_input_tokens": 12395,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12395
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

_source line 12 · 2026-05-14T20:46:31.184Z_

<details><summary>↩ Tool result · `toolu_01DAKyd8AtMWHQi61jaoufnH`</summary>

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
  "tool_name": "mcp__agent-ml-research__ssh_execute"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__detect_image"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cf90a49e-c24e-475d-b18d-8b10ae3bbdb0",
  "isSidechain": false,
  "promptId": "22ffd1fb-240e-481f-9bcc-b3f6a42d6805",
  "type": "user",
  "uuid": "9670fae3-6529-4a03-845a-a053df9587de",
  "toolUseResult": {
    "matches": [
      "mcp__agent-ml-research__ssh_read_only",
      "mcp__agent-ml-research__ssh_execute",
      "mcp__agent-ml-research__detect_image"
    ],
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__detect_image",
    "total_deferred_tools": 23
  },
  "sourceToolAssistantUUID": "cf90a49e-c24e-475d-b18d-8b10ae3bbdb0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "bda3dfbf-4b90-494d-b674-2597173fd381",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-14T20:46:35.096Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01X4rMXTrvmGhp4mkdFXxjMs`</summary>

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
  "parentUuid": "9670fae3-6529-4a03-845a-a053df9587de",
  "isSidechain": false,
  "requestId": "req_011Cb37h87h3cRGEgjb6eeE9",
  "type": "assistant",
  "uuid": "9f0f0846-7423-49eb-8778-bf43ad9dde4b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "bda3dfbf-4b90-494d-b674-2597173fd381",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016G2ufEWq8xNuUDnAgoTtF9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 924,
      "cache_read_input_tokens": 23842,
      "output_tokens": 223,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 924,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 223,
          "cache_read_input_tokens": 23842,
          "cache_creation_input_tokens": 924,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 924
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

_source line 14 · 2026-05-14T20:46:35.502Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01JBE8KCDMUPNVjrEta6mnvb`</summary>

```json
{
  "server": "bjb1-42106",
  "command": "ls /root/structfuse/evaluation/eval_retrieval.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9f0f0846-7423-49eb-8778-bf43ad9dde4b",
  "isSidechain": false,
  "requestId": "req_011Cb37h87h3cRGEgjb6eeE9",
  "type": "assistant",
  "uuid": "1b4bae51-986b-4754-9285-83d03461811d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "bda3dfbf-4b90-494d-b674-2597173fd381",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016G2ufEWq8xNuUDnAgoTtF9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 924,
      "cache_read_input_tokens": 23842,
      "output_tokens": 223,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 924,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 223,
          "cache_read_input_tokens": 23842,
          "cache_creation_input_tokens": 924,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 924
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

_source line 15 · 2026-05-14T20:46:36.234Z_

<details><summary>↩ Tool result · `toolu_01X4rMXTrvmGhp4mkdFXxjMs`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"910 /root/structfuse/evaluation/analyze_stratified.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.12}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9f0f0846-7423-49eb-8778-bf43ad9dde4b",
  "isSidechain": false,
  "promptId": "22ffd1fb-240e-481f-9bcc-b3f6a42d6805",
  "type": "user",
  "uuid": "7ab7f6b5-f2c2-4650-920f-6cffe4f1d165",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"910 /root/structfuse/evaluation/analyze_stratified.py\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 1.12}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"910 /root/structfuse/evaluation/analyze_stratified.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.12}}"
    }
  },
  "sourceToolAssistantUUID": "9f0f0846-7423-49eb-8778-bf43ad9dde4b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "bda3dfbf-4b90-494d-b674-2597173fd381",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-14T20:46:36.655Z_

<details><summary>↩ Tool result · `toolu_01JBE8KCDMUPNVjrEta6mnvb`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/structfuse/evaluation/eval_retrieval.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.41}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1b4bae51-986b-4754-9285-83d03461811d",
  "isSidechain": false,
  "promptId": "22ffd1fb-240e-481f-9bcc-b3f6a42d6805",
  "type": "user",
  "uuid": "8acbfbc7-81a4-4d33-8e8a-5806588d9007",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"/root/structfuse/evaluation/eval_retrieval.py\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.41}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"/root/structfuse/evaluation/eval_retrieval.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.41}}"
    }
  },
  "sourceToolAssistantUUID": "1b4bae51-986b-4754-9285-83d03461811d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "bda3dfbf-4b90-494d-b674-2597173fd381",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-14T20:46:39.941Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_018bhguYnoLSfbJtoJQmoQKs`</summary>

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
  "parentUuid": "8acbfbc7-81a4-4d33-8e8a-5806588d9007",
  "isSidechain": false,
  "requestId": "req_011Cb37hXGDz228Q6p2QPHhh",
  "type": "assistant",
  "uuid": "9bdec257-1a82-491b-99d2-95f234b6a1dc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "bda3dfbf-4b90-494d-b674-2597173fd381",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GbucJms3MEpzHfZTLFrVXD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 468,
      "cache_read_input_tokens": 24766,
      "output_tokens": 219,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 468,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 219,
          "cache_read_input_tokens": 24766,
          "cache_creation_input_tokens": 468,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 468
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

_source line 18 · 2026-05-14T20:46:40.273Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01TuoifSWZCXzHMYEAkNy2Ft`</summary>

```json
{
  "server": "bjb1-42106",
  "command": "cat /root/structfuse/evaluation/eval_retrieval.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9bdec257-1a82-491b-99d2-95f234b6a1dc",
  "isSidechain": false,
  "requestId": "req_011Cb37hXGDz228Q6p2QPHhh",
  "type": "assistant",
  "uuid": "d46a3b5a-6c2d-4a6d-9dec-3beefa53c1a7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "bda3dfbf-4b90-494d-b674-2597173fd381",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GbucJms3MEpzHfZTLFrVXD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 468,
      "cache_read_input_tokens": 24766,
      "output_tokens": 219,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 468,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 219,
          "cache_read_input_tokens": 24766,
          "cache_creation_input_tokens": 468,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 468
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

_source line 19 · 2026-05-14T20:46:40.351Z_

<details><summary>↩ Tool result · `toolu_018bhguYnoLSfbJtoJQmoQKs`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n\\\"\\\"\\\"Stratified analysis of embedding vs random negative strategies by data strata.\\n\\nAnalyses M2 per-instance predictions across:\\n  - Repo size (instance count per repo from M1)\\n  - Candidate pool size (neg_candidates per query)\\n  - Query-positive similarity (cosine sim from model, or text overlap for dry-run)\\n\\nInputs:\\n  - M2 per-instance predictions (from --predictions-dir or re-eval from checkpoints)\\n  - M1 all.jsonl (repo metadata)\\n  - Val JSONL files (query/candidate structure)\\n\\nOutputs:\\n  - stratified_results.json: full per-stratum metrics with bootstrap CI\\n  - stratified_summary.csv: compact table\\n  - stratified_plots.pdf: grouped bar charts, heatmaps, delta trends\\n\\\"\\\"\\\"\\n\\nimport argparse\\nimport csv\\nimport json\\nimport math\\nimport os\\nimport sys\\nfrom collections import Counter, defaultdict\\nfrom pathlib import Path\\nfrom typing import Any, Dict, List, Optional, Tuple\\n\\nimport numpy as np\\n\\nSTRATEGIES = [\\\"random\\\", \\\"embedding_distance\\\", \\\"dataflow_aware\\\"]\\nSTRATEGY_LABELS = {\\\"random\\\": \\\"Random\\\", \\\"embedding_distance\\\": \\\"Embedding\\\", \\\"dataflow_aware\\\": \\\"Dataflow\\\"}\\nSTRATEGY_COLORS = {\\\"random\\\": \\\"#4C72B0\\\", \\\"embedding_distance\\\": \\\"#DD8452\\\", \\\"dataflow_aware\\\": \\\"#55A868\\\"}\\n\\nREPO_SIZE_BINS = {\\n    \\\"small\\\": (0, 50),\\n    \\\"medium\\\": (50, 200),\\n    \\\"large\\\": (200, 500),\\n    \\\"xlarge\\\": (500, float(\\\"inf\\\")),\\n}\\n\\nPOOL_SIZE_BINS = {\\n    \\\"small\\\": (0, 20),\\n    \\\"medium\\\": (20, 40),\\n    \\\"large\\\": (40, 51),\\n}\\n\\nSIMILARITY_BINS = {\\n    \\\"low\\\": (0.0, 0.3),\\n    \\\"medium\\\": (0.3, 0.6),\\n    \\\"high\\\": (0.6, 1.01),\\n}\\n\\nDATAFLOW_BINS = {\\n    \\\"sparse\\\": (0, 2),\\n    \\\"moderate\\\": (2, 10),\\n    \\\"rich\\\": (10, float(\\\"inf\\\")),\\n}\\n\\nNEG_DIFFICULTY_QUARTILE_LABELS = [\\\"Q1_easy\\\", \\\"Q2\\\", \\\"Q3\\\", \\\"Q4_hard\\\"]\\n\\n\\ndef _bin_value(value, bins):\\n    for name, (lo, hi) in bins.items():\\n        if lo <= value < hi:\\n            return name\\n    return \\\"unknown\\\"\\n\\n\\n# ── M1 metadata ───────────────────────────────────────────────────��─\\n\\ndef load_m1_metadata(m1_path: str) -> Tuple[Dict[str, str], Dict[str, int]]:\\n    import re\\n    inst_to_repo = {}\\n    repo_counts: Counter = Counter()\\n    pat_iid = re.compile(r'\\\"instance_id\\\"\\\\s*:\\\\s*\\\"([^\\\"]+)\\\"')\\n    pat_repo = re.compile(r'\\\"repo\\\"\\\\s*:\\\\s*\\\"([^\\\"]+)\\\"')\\n    with open(m1_path) as f:\\n        for line in f:\\n            m_iid = pat_iid.search(line)\\n            m_repo = pat_repo.search(line)\\n            if m_iid and m_repo:\\n                iid = m_iid.group(1)\\n                repo = m_repo.group(1)\\n                inst_to_repo[iid] = repo\\n                repo_counts[repo] += 1\\n    return inst_to_repo, dict(repo_counts)\\n\\n\\n# ── Dataflow graph loading ────────────────────────────────────────────\\n\\ndef load_dataflow_edges(graph_path: str) -> Dict[str, int]:\\n    \\\"\\\"\\\"Load dataflow graph and return {file_key: edge_count}.\\\"\\\"\\\"\\n    with open(graph_path) as f:\\n        graph = json.load(f)\\n    return {k: len(v) for k, v in graph.items()}\\n\\n\\n# ── Val data loading ─────────────────────────────────────────────────\\n\\ndef load_val_samples(val_path: str, lite: bool = False) -> List[Dict[str, Any]]:\\n    \\\"\\\"\\\"Load val JSONL. lite=True skips candidate_tokens (faster for dry-run).\\\"\\\"\\\"\\n    import re\\n    samples = []\\n    pat_qid = re.compile(r'\\\"query_id\\\"\\\\s*:\\\\s*\\\"([^\\\"]+)\\\"')\\n    with open(val_path) as f:\\n        for line in f:\\n            if not line.strip():\\n                continue\\n            if lite:\\n                m = pat_qid.search(line)\\n                if not m:\\n                    continue\\n                qid = m.group(1)\\n                instance_id = qid.split(\\\"::\\\")[0] if \\\"::\\\" in qid else qid\\n                d = json.loads(line)\\n                samples.append({\\n                    \\\"query_id\\\": qid,\\n                    \\\"instance_id\\\": instance_id,\\n                    \\\"pool_size\\\": len(d.get(\\\"neg_candidates\\\", [])),\\n                    \\\"query_tokens\\\": d.get(\\\"query_tokens\\\", \\\"\\\")[:1000],\\n                    \\\"pos_tokens\\\": d.get(\\\"pos_tokens\\\", \\\"\\\")[:1000],\\n                    \\\"neg_candidates\\\": [],\\n                    \\\"candidate_tokens\\\": {},\\n                })\\n            else:\\n                d = jso\\n\\n... [截断: 输出过长，省略 27452 字符] ...\\n\\nt\\\")):\\n                        ckpt_dir = candidate\\n                        break\\n                if ckpt_dir is None and os.path.exists(os.path.join(base, \\\"model.pt\\\")):\\n                    ckpt_dir = base\\n                if os.path.exists(ckpt_dir):\\n                    print(f\\\"  Re-evaluating checkpoint: {ckpt_dir}\\\", flush=True)\\n                    results = reeval_checkpoint(\\n                        ckpt_dir, val_samples, args.device, args.max_seq_length\\n                    )\\n                else:\\n                    print(f\\\"  [WARN] Checkpoint not found: {ckpt_dir}\\\", flush=True)\\n                    continue\\n            else:\\n                print(\\\"  [ERROR] No --dry-run, --predictions-dir, or --checkpoints-dir\\\", flush=True)\\n                continue\\n\\n            # Assign strata\\n            results = assign_strata(results, inst_to_repo, repo_counts, dataflow_edges)\\n\\n            # For dry-run or model-based: compute text similarity for sim_bin\\n            if args.dry_run:\\n                for r, s in zip(results, val_samples):\\n                    tsim = text_similarity(s[\\\"query_tokens\\\"][:500], s[\\\"pos_tokens\\\"][:500])\\n                    r[\\\"sim_bin\\\"] = _bin_value(tsim, SIMILARITY_BINS)\\n\\n            all_results[strategy][seed] = results\\n            val_samples_cache[f\\\"{strategy}_s{seed}\\\"] = val_samples\\n            print(f\\\"  -> {len(results)} instances\\\", flush=True)\\n\\n    # Compute neg_difficulty quartiles (text-overlap proxy, CPU-safe)\\n    print(\\\"Computing neg difficulty quartiles...\\\", flush=True)\\n    assign_neg_difficulty_quartiles(all_results, val_samples_cache)\\n\\n    # Run stratified analysis\\n    print(\\\"\\\\nRunning stratified analysis...\\\", flush=True)\\n    repo_analysis = run_stratified_analysis(\\n        all_results, \\\"repo_size_bin\\\", list(REPO_SIZE_BINS.keys()), args.n_bootstrap\\n    )\\n    pool_analysis = run_stratified_analysis(\\n        all_results, \\\"pool_size_bin\\\", list(POOL_SIZE_BINS.keys()), args.n_bootstrap\\n    )\\n    sim_analysis = run_stratified_analysis(\\n        all_results, \\\"sim_bin\\\", list(SIMILARITY_BINS.keys()), args.n_bootstrap\\n    )\\n\\n    dataflow_analysis = {}\\n    if dataflow_edges is not None:\\n        dataflow_analysis = run_stratified_analysis(\\n            all_results, \\\"dataflow_bin\\\", list(DATAFLOW_BINS.keys()), args.n_bootstrap\\n        )\\n\\n    neg_diff_analysis = run_stratified_analysis(\\n        all_results, \\\"neg_difficulty_bin\\\", NEG_DIFFICULTY_QUARTILE_LABELS, args.n_bootstrap\\n    )\\n\\n    # Save JSON\\n    full_results = {\\n        \\\"config\\\": {\\n            \\\"strategies\\\": STRATEGIES,\\n            \\\"seeds\\\": seeds,\\n            \\\"repo_size_bins\\\": {k: list(v) for k, v in REPO_SIZE_BINS.items()},\\n            \\\"pool_size_bins\\\": {k: list(v) for k, v in POOL_SIZE_BINS.items()},\\n            \\\"similarity_bins\\\": {k: list(v) for k, v in SIMILARITY_BINS.items()},\\n            \\\"dataflow_bins\\\": {k: list(v) for k, v in DATAFLOW_BINS.items()},\\n            \\\"neg_difficulty_quartiles\\\": NEG_DIFFICULTY_QUARTILE_LABELS,\\n            \\\"n_bootstrap\\\": args.n_bootstrap,\\n            \\\"dry_run\\\": args.dry_run,\\n        },\\n        \\\"by_repo_size\\\": repo_analysis,\\n        \\\"by_pool_size\\\": pool_analysis,\\n        \\\"by_similarity\\\": sim_analysis,\\n        \\\"by_dataflow\\\": dataflow_analysis,\\n        \\\"by_neg_difficulty\\\": neg_diff_analysis,\\n    }\\n\\n    json_path = os.path.join(args.output_dir, \\\"stratified_results.json\\\")\\n    with open(json_path, \\\"w\\\") as f:\\n        json.dump(full_results, f, indent=2, ensure_ascii=False)\\n    print(f\\\"  Results JSON saved to {json_path}\\\", flush=True)\\n\\n    # CSV summary\\n    csv_path = os.path.join(args.output_dir, \\\"stratified_summary.csv\\\")\\n    write_summary_csv(repo_analysis, pool_analysis, sim_analysis, csv_path, dataflow_analysis, neg_diff_analysis)\\n\\n    # Plots\\n    try:\\n        make_plots(repo_analysis, pool_analysis, sim_analysis, args.output_dir, dataflow_analysis, neg_diff_analysis)\\n    except Exception as e:\\n        print(f\\\"  [WARN] Plot generation failed: {e}\\\", flush=True)\\n\\n    print(\\\"\\\\nDone.\\\", flush=True)\\n\\n\\nif __name__ == \\\"__main__\\\":\\n    main()\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9bdec257-1a82-491b-99d2-95f234b6a1dc",
  "isSidechain": false,
  "promptId": "22ffd1fb-240e-481f-9bcc-b3f6a42d6805",
  "type": "user",
  "uuid": "ac4e0832-1ba0-4de8-a18e-6f17a2ca2e99",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"#!/usr/bin/env python3\\\\n\\\\\\\"\\\\\\\"\\\\\\\"Stratified analysis of embedding vs random negative strategies by data strata.\\\\n\\\\nAnalyses M2 per-instance predictions across:\\\\n  - Repo size (instance count per repo from M1)\\\\n  - Candidate pool size (neg_candidates per query)\\\\n  - Query-positive similarity (cosine sim from model, or text overlap for dry-run)\\\\n\\\\nInputs:\\\\n  - M2 per-instance predictions (from --predictions-dir or re-eval from checkpoints)\\\\n  - M1 all.jsonl (repo metadata)\\\\n  - Val JSONL files (query/candidate structure)\\\\n\\\\nOutputs:\\\\n  - stratified_results.json: full per-stratum metrics with bootstrap CI\\\\n  - stratified_summary.csv: compact table\\\\n  - stratified_plots.pdf: grouped bar charts, heatmaps, delta trends\\\\n\\\\\\\"\\\\\\\"\\\\\\\"\\\\n\\\\nimport argparse\\\\nimport csv\\\\nimport json\\\\nimport math\\\\nimport os\\\\nimport sys\\\\nfrom collections import Counter, defaultdict\\\\nfrom pathlib import Path\\\\nfrom typing import Any, Dict, List, Optional, Tuple\\\\n\\\\nimport numpy as np\\\\n\\\\nSTRATEGIES = [\\\\\\\"random\\\\\\\", \\\\\\\"embedding_distance\\\\\\\", \\\\\\\"dataflow_aware\\\\\\\"]\\\\nSTRATEGY_LABELS = {\\\\\\\"random\\\\\\\": \\\\\\\"Random\\\\\\\", \\\\\\\"embedding_distance\\\\\\\": \\\\\\\"Embedding\\\\\\\", \\\\\\\"dataflow_aware\\\\\\\": \\\\\\\"Dataflow\\\\\\\"}\\\\nSTRATEGY_COLORS = {\\\\\\\"random\\\\\\\": \\\\\\\"#4C72B0\\\\\\\", \\\\\\\"embedding_distance\\\\\\\": \\\\\\\"#DD8452\\\\\\\", \\\\\\\"dataflow_aware\\\\\\\": \\\\\\\"#55A868\\\\\\\"}\\\\n\\\\nREPO_SIZE_BINS = {\\\\n    \\\\\\\"small\\\\\\\": (0, 50),\\\\n    \\\\\\\"medium\\\\\\\": (50, 200),\\\\n    \\\\\\\"large\\\\\\\": (200, 500),\\\\n    \\\\\\\"xlarge\\\\\\\": (500, float(\\\\\\\"inf\\\\\\\")),\\\\n}\\\\n\\\\nPOOL_SIZE_BINS = {\\\\n    \\\\\\\"small\\\\\\\": (0, 20),\\\\n    \\\\\\\"medium\\\\\\\": (20, 40),\\\\n    \\\\\\\"large\\\\\\\": (40, 51),\\\\n}\\\\n\\\\nSIMILARITY_BINS = {\\\\n    \\\\\\\"low\\\\\\\": (0.0, 0.3),\\\\n    \\\\\\\"medium\\\\\\\": (0.3, 0.6),\\\\n    \\\\\\\"high\\\\\\\": (0.6, 1.01),\\\\n}\\\\n\\\\nDATAFLOW_BINS = {\\\\n    \\\\\\\"sparse\\\\\\\": (0, 2),\\\\n    \\\\\\\"moderate\\\\\\\": (2, 10),\\\\n    \\\\\\\"rich\\\\\\\": (10, float(\\\\\\\"inf\\\\\\\")),\\\\n}\\\\n\\\\nNEG_DIFFICULTY_QUARTILE_LABELS = [\\\\\\\"Q1_easy\\\\\\\", \\\\\\\"Q2\\\\\\\", \\\\\\\"Q3\\\\\\\", \\\\\\\"Q4_hard\\\\\\\"]\\\\n\\\\n\\\\ndef _bin_value(value, bins):\\\\n    for name, (lo, hi) in bins.items():\\\\n        if lo <= value < hi:\\\\n            return name\\\\n    return \\\\\\\"unknown\\\\\\\"\\\\n\\\\n\\\\n# ── M1 metadata ───────────────────────────────────────────────────��─\\\\n\\\\ndef load_m1_metadata(m1_path: str) -> Tuple[Dict[str, str], Dict[str, int]]:\\\\n    import re\\\\n    inst_to_repo = {}\\\\n    repo_counts: Counter = Counter()\\\\n    pat_iid = re.compile(r'\\\\\\\"instance_id\\\\\\\"\\\\\\\\s*:\\\\\\\\s*\\\\\\\"([^\\\\\\\"]+)\\\\\\\"')\\\\n    pat_repo = re.compile(r'\\\\\\\"repo\\\\\\\"\\\\\\\\s*:\\\\\\\\s*\\\\\\\"([^\\\\\\\"]+)\\\\\\\"')\\\\n    with open(m1_path) as f:\\\\n        for line in f:\\\\n            m_iid = pat_iid.search(line)\\\\n            m_repo = pat_repo.search(line)\\\\n            if m_iid and m_repo:\\\\n                iid = m_iid.group(1)\\\\n                repo = m_repo.group(1)\\\\n                inst_to_repo[iid] = repo\\\\n                repo_counts[repo] += 1\\\\n    return inst_to_repo, dict(repo_counts)\\\\n\\\\n\\\\n# ── Dataflow graph loading ────────────────────────────────────────────\\\\n\\\\ndef load_dataflow_edges(graph_path: str) -> Dict[str, int]:\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"Load dataflow graph and return {file_key: edge_count}.\\\\\\\"\\\\\\\"\\\\\\\"\\\\n    with open(graph_path) as f:\\\\n        graph = json.load(f)\\\\n    return {k: len(v) for k, v in graph.items()}\\\\n\\\\n\\\\n# ── Val data loading ─────────────────────────────────────────────────\\\\n\\\\ndef load_val_samples(val_path: str, lite: bool = False) -> List[Dict[str, Any]]:\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"Load val JSONL. lite=True skips candidate_tokens (faster for dry-run).\\\\\\\"\\\\\\\"\\\\\\\"\\\\n    import re\\\\n    samples = []\\\\n    pat_qid = re.compile(r'\\\\\\\"query_id\\\\\\\"\\\\\\\\s*:\\\\\\\\s*\\\\\\\"([^\\\\\\\"]+)\\\\\\\"')\\\\n    with open(val_path) as f:\\\\n        for line in f:\\\\n            if not line.strip():\\\\n                continue\\\\n            if lite:\\\\n                m = pat_qid.search(line)\\\\n                if not m:\\\\n                    continue\\\\n                qid = m.group(1)\\\\n                instance_id = qid.split(\\\\\\\"::\\\\\\\")[0] if \\\\\\\"::\\\\\\\" in qid else qid\\\\n                d = json.loads(line)\\\\n                samples.append({\\\\n                    \\\\\\\"query_id\\\\\\\": qid,\\\\n                    \\\\\\\"instance_id\\\\\\\": instance_id,\\\\n                    \\\\\\\"pool_size\\\\\\\": len(d.get(\\\\\\\"neg_candidates\\\\\\\", [])),\\\\n                    \\\\\\\"query_tokens\\\\\\\": d.get(\\\\\\\"query_tokens\\\\\\\", \\\\\\\"\\\\\\\")[:1000],\\\\n                    \\\\\\\"pos_tokens\\\\\\\": d.get(\\\\\\\"pos_tokens\\\\\\\", \\\\\\\"\\\\\\\")[:1000],\\\\n                    \\\\\\\"neg_candidates\\\\\\\": [],\\\\n                    \\\\\\\"candidate_tokens\\\\\\\": {},\\\\n                })\\\\n            else:\\\\n                d = jso\\\\n\\\\n... [截断: 输出过长，省略 27452 字符] ...\\\\n\\\\nt\\\\\\\")):\\\\n                        ckpt_dir = candidate\\\\n                        break\\\\n                if ckpt_dir is None and os.path.exists(os.path.join(base, \\\\\\\"model.pt\\\\\\\")):\\\\n                    ckpt_dir = base\\\\n                if os.path.exists(ckpt_dir):\\\\n                    print(f\\\\\\\"  Re-evaluating checkpoint: {ckpt_dir}\\\\\\\", flush=True)\\\\n                    results = reeval_checkpoint(\\\\n                        ckpt_dir, val_samples, args.device, args.max_seq_length\\\\n                    )\\\\n                else:\\\\n                    print(f\\\\\\\"  [WARN] Checkpoint not found: {ckpt_dir}\\\\\\\", flush=True)\\\\n                    continue\\\\n            else:\\\\n                print(\\\\\\\"  [ERROR] No --dry-run, --predictions-dir, or --checkpoints-dir\\\\\\\", flush=True)\\\\n                continue\\\\n\\\\n            # Assign strata\\\\n            results = assign_strata(results, inst_to_repo, repo_counts, dataflow_edges)\\\\n\\\\n            # For dry-run or model-based: compute text similarity for sim_bin\\\\n            if args.dry_run:\\\\n                for r, s in zip(results, val_samples):\\\\n                    tsim = text_similarity(s[\\\\\\\"query_tokens\\\\\\\"][:500], s[\\\\\\\"pos_tokens\\\\\\\"][:500])\\\\n                    r[\\\\\\\"sim_bin\\\\\\\"] = _bin_value(tsim, SIMILARITY_BINS)\\\\n\\\\n            all_results[strategy][seed] = results\\\\n            val_samples_cache[f\\\\\\\"{strategy}_s{seed}\\\\\\\"] = val_samples\\\\n            print(f\\\\\\\"  -> {len(results)} instances\\\\\\\", flush=True)\\\\n\\\\n    # Compute neg_difficulty quartiles (text-overlap proxy, CPU-safe)\\\\n    print(\\\\\\\"Computing neg difficulty quartiles...\\\\\\\", flush=True)\\\\n    assign_neg_difficulty_quartiles(all_results, val_samples_cache)\\\\n\\\\n    # Run stratified analysis\\\\n    print(\\\\\\\"\\\\\\\\nRunning stratified analysis...\\\\\\\", flush=True)\\\\n    repo_analysis = run_stratified_analysis(\\\\n        all_results, \\\\\\\"repo_size_bin\\\\\\\", list(REPO_SIZE_BINS.keys()), args.n_bootstrap\\\\n    )\\\\n    pool_analysis = run_stratified_analysis(\\\\n        all_results, \\\\\\\"pool_size_bin\\\\\\\", list(POOL_SIZE_BINS.keys()), args.n_bootstrap\\\\n    )\\\\n    sim_analysis = run_stratified_analysis(\\\\n        all_results, \\\\\\\"sim_bin\\\\\\\", list(SIMILARITY_BINS.keys()), args.n_bootstrap\\\\n    )\\\\n\\\\n    dataflow_analysis = {}\\\\n    if dataflow_edges is not None:\\\\n        dataflow_analysis = run_stratified_analysis(\\\\n            all_results, \\\\\\\"dataflow_bin\\\\\\\", list(DATAFLOW_BINS.keys()), args.n_bootstrap\\\\n        )\\\\n\\\\n    neg_diff_analysis = run_stratified_analysis(\\\\n        all_results, \\\\\\\"neg_difficulty_bin\\\\\\\", NEG_DIFFICULTY_QUARTILE_LABELS, args.n_bootstrap\\\\n    )\\\\n\\\\n    # Save JSON\\\\n    full_results = {\\\\n        \\\\\\\"config\\\\\\\": {\\\\n            \\\\\\\"strategies\\\\\\\": STRATEGIES,\\\\n            \\\\\\\"seeds\\\\\\\": seeds,\\\\n            \\\\\\\"repo_size_bins\\\\\\\": {k: list(v) for k, v in REPO_SIZE_BINS.items()},\\\\n            \\\\\\\"pool_size_bins\\\\\\\": {k: list(v) for k, v in POOL_SIZE_BINS.items()},\\\\n            \\\\\\\"similarity_bins\\\\\\\": {k: list(v) for k, v in SIMILARITY_BINS.items()},\\\\n            \\\\\\\"dataflow_bins\\\\\\\": {k: list(v) for k, v in DATAFLOW_BINS.items()},\\\\n            \\\\\\\"neg_difficulty_quartiles\\\\\\\": NEG_DIFFICULTY_QUARTILE_LABELS,\\\\n            \\\\\\\"n_bootstrap\\\\\\\": args.n_bootstrap,\\\\n            \\\\\\\"dry_run\\\\\\\": args.dry_run,\\\\n        },\\\\n        \\\\\\\"by_repo_size\\\\\\\": repo_analysis,\\\\n        \\\\\\\"by_pool_size\\\\\\\": pool_analysis,\\\\n        \\\\\\\"by_similarity\\\\\\\": sim_analysis,\\\\n        \\\\\\\"by_dataflow\\\\\\\": dataflow_analysis,\\\\n        \\\\\\\"by_neg_difficulty\\\\\\\": neg_diff_analysis,\\\\n    }\\\\n\\\\n    json_path = os.path.join(args.output_dir, \\\\\\\"stratified_results.json\\\\\\\")\\\\n    with open(json_path, \\\\\\\"w\\\\\\\") as f:\\\\n        json.dump(full_results, f, indent=2, ensure_ascii=False)\\\\n    print(f\\\\\\\"  Results JSON saved to {json_path}\\\\\\\", flush=True)\\\\n\\\\n    # CSV summary\\\\n    csv_path = os.path.join(args.output_dir, \\\\\\\"stratified_summary.csv\\\\\\\")\\\\n    write_summary_csv(repo_analysis, pool_analysis, sim_analysis, csv_path, dataflow_analysis, neg_diff_analysis)\\\\n\\\\n    # Plots\\\\n    try:\\\\n        make_plots(repo_analysis, pool_analysis, sim_analysis, args.output_dir, dataflow_analysis, neg_diff_analysis)\\\\n    except Exception as e:\\\\n        print(f\\\\\\\"  [WARN] Plot generation failed: {e}\\\\\\\", flush=True)\\\\n\\\\n    print(\\\\\\\"\\\\\\\\nDone.\\\\\\\", flush=True)\\\\n\\\\n\\\\nif __name__ == \\\\\\\"__main__\\\\\\\":\\\\n    main()\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.4}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n\\\"\\\"\\\"Stratified analysis of embedding vs random negative strategies by data strata.\\n\\nAnalyses M2 per-instance predictions across:\\n  - Repo size (instance count per repo from M1)\\n  - Candidate pool size (neg_candidates per query)\\n  - Query-positive similarity (cosine sim from model, or text overlap for dry-run)\\n\\nInputs:\\n  - M2 per-instance predictions (from --predictions-dir or re-eval from checkpoints)\\n  - M1 all.jsonl (repo metadata)\\n  - Val JSONL files (query/candidate structure)\\n\\nOutputs:\\n  - stratified_results.json: full per-stratum metrics with bootstrap CI\\n  - stratified_summary.csv: compact table\\n  - stratified_plots.pdf: grouped bar charts, heatmaps, delta trends\\n\\\"\\\"\\\"\\n\\nimport argparse\\nimport csv\\nimport json\\nimport math\\nimport os\\nimport sys\\nfrom collections import Counter, defaultdict\\nfrom pathlib import Path\\nfrom typing import Any, Dict, List, Optional, Tuple\\n\\nimport numpy as np\\n\\nSTRATEGIES = [\\\"random\\\", \\\"embedding_distance\\\", \\\"dataflow_aware\\\"]\\nSTRATEGY_LABELS = {\\\"random\\\": \\\"Random\\\", \\\"embedding_distance\\\": \\\"Embedding\\\", \\\"dataflow_aware\\\": \\\"Dataflow\\\"}\\nSTRATEGY_COLORS = {\\\"random\\\": \\\"#4C72B0\\\", \\\"embedding_distance\\\": \\\"#DD8452\\\", \\\"dataflow_aware\\\": \\\"#55A868\\\"}\\n\\nREPO_SIZE_BINS = {\\n    \\\"small\\\": (0, 50),\\n    \\\"medium\\\": (50, 200),\\n    \\\"large\\\": (200, 500),\\n    \\\"xlarge\\\": (500, float(\\\"inf\\\")),\\n}\\n\\nPOOL_SIZE_BINS = {\\n    \\\"small\\\": (0, 20),\\n    \\\"medium\\\": (20, 40),\\n    \\\"large\\\": (40, 51),\\n}\\n\\nSIMILARITY_BINS = {\\n    \\\"low\\\": (0.0, 0.3),\\n    \\\"medium\\\": (0.3, 0.6),\\n    \\\"high\\\": (0.6, 1.01),\\n}\\n\\nDATAFLOW_BINS = {\\n    \\\"sparse\\\": (0, 2),\\n    \\\"moderate\\\": (2, 10),\\n    \\\"rich\\\": (10, float(\\\"inf\\\")),\\n}\\n\\nNEG_DIFFICULTY_QUARTILE_LABELS = [\\\"Q1_easy\\\", \\\"Q2\\\", \\\"Q3\\\", \\\"Q4_hard\\\"]\\n\\n\\ndef _bin_value(value, bins):\\n    for name, (lo, hi) in bins.items():\\n        if lo <= value < hi:\\n            return name\\n    return \\\"unknown\\\"\\n\\n\\n# ── M1 metadata ───────────────────────────────────────────────────��─\\n\\ndef load_m1_metadata(m1_path: str) -> Tuple[Dict[str, str], Dict[str, int]]:\\n    import re\\n    inst_to_repo = {}\\n    repo_counts: Counter = Counter()\\n    pat_iid = re.compile(r'\\\"instance_id\\\"\\\\s*:\\\\s*\\\"([^\\\"]+)\\\"')\\n    pat_repo = re.compile(r'\\\"repo\\\"\\\\s*:\\\\s*\\\"([^\\\"]+)\\\"')\\n    with open(m1_path) as f:\\n        for line in f:\\n            m_iid = pat_iid.search(line)\\n            m_repo = pat_repo.search(line)\\n            if m_iid and m_repo:\\n                iid = m_iid.group(1)\\n                repo = m_repo.group(1)\\n                inst_to_repo[iid] = repo\\n                repo_counts[repo] += 1\\n    return inst_to_repo, dict(repo_counts)\\n\\n\\n# ── Dataflow graph loading ────────────────────────────────────────────\\n\\ndef load_dataflow_edges(graph_path: str) -> Dict[str, int]:\\n    \\\"\\\"\\\"Load dataflow graph and return {file_key: edge_count}.\\\"\\\"\\\"\\n    with open(graph_path) as f:\\n        graph = json.load(f)\\n    return {k: len(v) for k, v in graph.items()}\\n\\n\\n# ── Val data loading ─────────────────────────────────────────────────\\n\\ndef load_val_samples(val_path: str, lite: bool = False) -> List[Dict[str, Any]]:\\n    \\\"\\\"\\\"Load val JSONL. lite=True skips candidate_tokens (faster for dry-run).\\\"\\\"\\\"\\n    import re\\n    samples = []\\n    pat_qid = re.compile(r'\\\"query_id\\\"\\\\s*:\\\\s*\\\"([^\\\"]+)\\\"')\\n    with open(val_path) as f:\\n        for line in f:\\n            if not line.strip():\\n                continue\\n            if lite:\\n                m = pat_qid.search(line)\\n                if not m:\\n                    continue\\n                qid = m.group(1)\\n                instance_id = qid.split(\\\"::\\\")[0] if \\\"::\\\" in qid else qid\\n                d = json.loads(line)\\n                samples.append({\\n                    \\\"query_id\\\": qid,\\n                    \\\"instance_id\\\": instance_id,\\n                    \\\"pool_size\\\": len(d.get(\\\"neg_candidates\\\", [])),\\n                    \\\"query_tokens\\\": d.get(\\\"query_tokens\\\", \\\"\\\")[:1000],\\n                    \\\"pos_tokens\\\": d.get(\\\"pos_tokens\\\", \\\"\\\")[:1000],\\n                    \\\"neg_candidates\\\": [],\\n                    \\\"candidate_tokens\\\": {},\\n                })\\n            else:\\n                d = jso\\n\\n... [截断: 输出过长，省略 27452 字符] ...\\n\\nt\\\")):\\n                        ckpt_dir = candidate\\n                        break\\n                if ckpt_dir is None and os.path.exists(os.path.join(base, \\\"model.pt\\\")):\\n                    ckpt_dir = base\\n                if os.path.exists(ckpt_dir):\\n                    print(f\\\"  Re-evaluating checkpoint: {ckpt_dir}\\\", flush=True)\\n                    results = reeval_checkpoint(\\n                        ckpt_dir, val_samples, args.device, args.max_seq_length\\n                    )\\n                else:\\n                    print(f\\\"  [WARN] Checkpoint not found: {ckpt_dir}\\\", flush=True)\\n                    continue\\n            else:\\n                print(\\\"  [ERROR] No --dry-run, --predictions-dir, or --checkpoints-dir\\\", flush=True)\\n                continue\\n\\n            # Assign strata\\n            results = assign_strata(results, inst_to_repo, repo_counts, dataflow_edges)\\n\\n            # For dry-run or model-based: compute text similarity for sim_bin\\n            if args.dry_run:\\n                for r, s in zip(results, val_samples):\\n                    tsim = text_similarity(s[\\\"query_tokens\\\"][:500], s[\\\"pos_tokens\\\"][:500])\\n                    r[\\\"sim_bin\\\"] = _bin_value(tsim, SIMILARITY_BINS)\\n\\n            all_results[strategy][seed] = results\\n            val_samples_cache[f\\\"{strategy}_s{seed}\\\"] = val_samples\\n            print(f\\\"  -> {len(results)} instances\\\", flush=True)\\n\\n    # Compute neg_difficulty quartiles (text-overlap proxy, CPU-safe)\\n    print(\\\"Computing neg difficulty quartiles...\\\", flush=True)\\n    assign_neg_difficulty_quartiles(all_results, val_samples_cache)\\n\\n    # Run stratified analysis\\n    print(\\\"\\\\nRunning stratified analysis...\\\", flush=True)\\n    repo_analysis = run_stratified_analysis(\\n        all_results, \\\"repo_size_bin\\\", list(REPO_SIZE_BINS.keys()), args.n_bootstrap\\n    )\\n    pool_analysis = run_stratified_analysis(\\n        all_results, \\\"pool_size_bin\\\", list(POOL_SIZE_BINS.keys()), args.n_bootstrap\\n    )\\n    sim_analysis = run_stratified_analysis(\\n        all_results, \\\"sim_bin\\\", list(SIMILARITY_BINS.keys()), args.n_bootstrap\\n    )\\n\\n    dataflow_analysis = {}\\n    if dataflow_edges is not None:\\n        dataflow_analysis = run_stratified_analysis(\\n            all_results, \\\"dataflow_bin\\\", list(DATAFLOW_BINS.keys()), args.n_bootstrap\\n        )\\n\\n    neg_diff_analysis = run_stratified_analysis(\\n        all_results, \\\"neg_difficulty_bin\\\", NEG_DIFFICULTY_QUARTILE_LABELS, args.n_bootstrap\\n    )\\n\\n    # Save JSON\\n    full_results = {\\n        \\\"config\\\": {\\n            \\\"strategies\\\": STRATEGIES,\\n            \\\"seeds\\\": seeds,\\n            \\\"repo_size_bins\\\": {k: list(v) for k, v in REPO_SIZE_BINS.items()},\\n            \\\"pool_size_bins\\\": {k: list(v) for k, v in POOL_SIZE_BINS.items()},\\n            \\\"similarity_bins\\\": {k: list(v) for k, v in SIMILARITY_BINS.items()},\\n            \\\"dataflow_bins\\\": {k: list(v) for k, v in DATAFLOW_BINS.items()},\\n            \\\"neg_difficulty_quartiles\\\": NEG_DIFFICULTY_QUARTILE_LABELS,\\n            \\\"n_bootstrap\\\": args.n_bootstrap,\\n            \\\"dry_run\\\": args.dry_run,\\n        },\\n        \\\"by_repo_size\\\": repo_analysis,\\n        \\\"by_pool_size\\\": pool_analysis,\\n        \\\"by_similarity\\\": sim_analysis,\\n        \\\"by_dataflow\\\": dataflow_analysis,\\n        \\\"by_neg_difficulty\\\": neg_diff_analysis,\\n    }\\n\\n    json_path = os.path.join(args.output_dir, \\\"stratified_results.json\\\")\\n    with open(json_path, \\\"w\\\") as f:\\n        json.dump(full_results, f, indent=2, ensure_ascii=False)\\n    print(f\\\"  Results JSON saved to {json_path}\\\", flush=True)\\n\\n    # CSV summary\\n    csv_path = os.path.join(args.output_dir, \\\"stratified_summary.csv\\\")\\n    write_summary_csv(repo_analysis, pool_analysis, sim_analysis, csv_path, dataflow_analysis, neg_diff_analysis)\\n\\n    # Plots\\n    try:\\n        make_plots(repo_analysis, pool_analysis, sim_analysis, args.output_dir, dataflow_analysis, neg_diff_analysis)\\n    except Exception as e:\\n        print(f\\\"  [WARN] Plot generation failed: {e}\\\", flush=True)\\n\\n    print(\\\"\\\\nDone.\\\", flush=True)\\n\\n\\nif __name__ == \\\"__main__\\\":\\n    main()\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4}}"
    }
  },
  "sourceToolAssistantUUID": "9bdec257-1a82-491b-99d2-95f234b6a1dc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "bda3dfbf-4b90-494d-b674-2597173fd381",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 20_

```json
{
  "type": "last-prompt",
  "leafUuid": "ac4e0832-1ba0-4de8-a18e-6f17a2ca2e99",
  "sessionId": "bda3dfbf-4b90-494d-b674-2597173fd381"
}
```

---

### Runtime record

_source line 21_

```json
{
  "type": "ai-title",
  "aiTitle": "Add pool-size controlled stratified evaluation to analysis script",
  "sessionId": "bda3dfbf-4b90-494d-b674-2597173fd381"
}
```

---

### Tool result

_source line 22 · 2026-05-14T20:46:40.810Z_

<details><summary>↩ Tool result · `toolu_01TuoifSWZCXzHMYEAkNy2Ft`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"import os\\nos.environ[\\\"CUDA_VISIBLE_DEVICES\\\"] = \\\"4\\\"\\n\\n\\\"\\\"\\\"\\nStructFuse Retrieval Evaluation Script\\n\\nEvaluates the StructFuse contrastive retriever on file-level and function-level\\nretrieval tasks across SWE-bench Lite, RepoBench-R, and custom held-out sets.\\n\\nInput:\\n  - Trained StructFuse checkpoint(s)\\n  - Test file (JSON Lines): each line has {query, gold_files, gold_functions, repo_path}\\n  - (Optional) CodeQL data-flow output directory\\n\\nOutput:\\n  - JSON file with per-instance predictions and aggregate metrics:\\n    Recall@1/5/10, MRR, Structural Precision\\n\\nDependencies: transformers, torch, rank_bm25, faiss-cpu, numpy\\n\\\"\\\"\\\"\\n\\nimport argparse\\nimport json\\nimport os\\nimport glob\\nimport sys\\nimport time\\nfrom collections import defaultdict\\nfrom dataclasses import dataclass, field\\nfrom pathlib import Path\\nfrom typing import Optional\\n\\nimport jsonlines\\nimport numpy as np\\nimport torch\\nimport torch.nn.functional as F\\nfrom tqdm import tqdm\\nfrom transformers import AutoTokenizer\\nfrom rank_bm25 import BM25Okapi\\n\\nsys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), \\\"..\\\", \\\"training\\\"))\\nfrom contrastive_model import StructFuseEncoder\\n\\n\\n@dataclass\\nclass RetrievalInstance:\\n    query: str\\n    gold_files: list[str]\\n    gold_functions: list[str] = field(default_factory=list)\\n    repo_path: str = \\\"\\\"\\n    instance_id: str = \\\"\\\"\\n    metadata: dict = field(default_factory=dict)\\n\\n\\n@dataclass\\nclass RetrievalResult:\\n    instance_id: str\\n    query: str\\n    gold_files: list[str]\\n    predicted_files: list[str]\\n    scores: list[float]\\n    hits: dict[str, bool] = field(default_factory=dict)\\n\\n\\ndef load_test_data(test_file: str, dataset: str) -> list[RetrievalInstance]:\\n    \\\"\\\"\\\"Load test instances from JSON Lines file, adapting format per dataset.\\\"\\\"\\\"\\n    instances = []\\n    with jsonlines.open(test_file) as reader:\\n        for i, item in enumerate(reader):\\n            if dataset == \\\"swebench_lite\\\":\\n                inst = RetrievalInstance(\\n                    query=item.get(\\\"problem_statement\\\", item.get(\\\"query\\\", \\\"\\\")),\\n                    gold_files=item.get(\\\"gold_files\\\", []),\\n                    gold_functions=item.get(\\\"gold_functions\\\", []),\\n                    repo_path=item.get(\\\"repo_path\\\", item.get(\\\"repo\\\", \\\"\\\")),\\n                    instance_id=item.get(\\\"instance_id\\\", f\\\"swebench_{i}\\\"),\\n                )\\n            elif dataset == \\\"repobench\\\":\\n                inst = RetrievalInstance(\\n                    query=item.get(\\\"query\\\", \\\"\\\"),\\n                    gold_files=item.get(\\\"gold_files\\\", []),\\n                    gold_functions=item.get(\\\"gold_functions\\\", []),\\n                    repo_path=item.get(\\\"repo_path\\\", \\\"\\\"),\\n                    instance_id=item.get(\\\"instance_id\\\", f\\\"repobench_{i}\\\"),\\n                )\\n            else:\\n                inst = RetrievalInstance(\\n                    query=item[\\\"query\\\"],\\n                    gold_files=item[\\\"gold_files\\\"],\\n                    gold_functions=item.get(\\\"gold_functions\\\", []),\\n                    repo_path=item.get(\\\"repo_path\\\", \\\"\\\"),\\n                    instance_id=item.get(\\\"instance_id\\\", f\\\"custom_{i}\\\"),\\n                    metadata=item.get(\\\"metadata\\\", {}),\\n                )\\n            instances.append(inst)\\n    return instances\\n\\n\\ndef collect_candidate_files(repo_path: str, extensions: tuple[str, ...] = (\\\".py\\\",)) -> list[dict]:\\n    \\\"\\\"\\\"Walk repo and collect candidate source files with their content.\\\"\\\"\\\"\\n    candidates = []\\n    repo = Path(repo_path)\\n    if not repo.exists():\\n        return candidates\\n    for ext in extensions:\\n        for fpath in repo.rglob(f\\\"*{ext}\\\"):\\n            rel = str(fpath.relative_to(repo))\\n            if any(part.startswith(\\\".\\\") for part in fpath.parts):\\n                continue\\n            if \\\"__pycache__\\\" in rel:\\n                continue\\n            fname = fpath.name\\n            if (fname.startswith(\\\"test_\\\") and fname.endswith(\\\".py\\\")) or fname.endswith(\\\"_test.py\\\"):\\n                continue\\n            try:\\n                content = fpath.read_text(errors=\\\"replace\\\")\\n            exc\\n\\n... [截断: 输出过长，省略 9159 字符] ...\\n\\n if b[\\\"path\\\"] == r[\\\"path\\\"]:\\n                            ranked[i][\\\"bm25_score\\\"] = b.get(\\\"bm25_score\\\", 0.0)\\n                            break\\n                ranked = fusion.rerank(ranked, reachable)\\n\\n        predicted_files = [r[\\\"path\\\"] for r in ranked]\\n        score_key = \\\"fused_score\\\" if use_fusion else (\\\"structfuse_score\\\" if not bm25_only else \\\"bm25_score\\\")\\n        scores = [r.get(score_key, 0.0) for r in ranked]\\n\\n        results.append(RetrievalResult(\\n            instance_id=inst.instance_id,\\n            query=inst.query[:200],\\n            gold_files=inst.gold_files,\\n            predicted_files=predicted_files,\\n            scores=scores,\\n        ))\\n\\n    metrics = compute_metrics(results, k_values)\\n    if reachable_map:\\n        metrics[\\\"structural_precision\\\"] = compute_structural_precision(results, reachable_map)\\n\\n    return {\\n        \\\"model\\\": model_path,\\n        \\\"num_instances\\\": len(instances),\\n        \\\"metrics\\\": metrics,\\n        \\\"per_instance\\\": [\\n            {\\n                \\\"instance_id\\\": r.instance_id,\\n                \\\"gold_files\\\": r.gold_files,\\n                \\\"predicted_top10\\\": r.predicted_files[:10],\\n                \\\"scores_top10\\\": r.scores[:10],\\n            }\\n            for r in results\\n        ],\\n    }\\n\\n\\ndef main():\\n    parser = argparse.ArgumentParser(description=\\\"StructFuse Retrieval Evaluation\\\")\\n    parser.add_argument(\\\"--model-path\\\", type=str, required=True,\\n                        help=\\\"Checkpoint path(s), comma-separated for multi-model comparison\\\")\\n    parser.add_argument(\\\"--test-file\\\", type=str, required=True,\\n                        help=\\\"JSON Lines test file\\\")\\n    parser.add_argument(\\\"--dataflow-dir\\\", type=str, default=None,\\n                        help=\\\"CodeQL data-flow output directory\\\")\\n    parser.add_argument(\\\"--output-file\\\", type=str, default=\\\"retrieval_results.json\\\",\\n                        help=\\\"Output JSON file\\\")\\n    parser.add_argument(\\\"--top-k\\\", type=str, default=\\\"1,5,10\\\",\\n                        help=\\\"Comma-separated k values for Recall@k\\\")\\n    parser.add_argument(\\\"--batch-size\\\", type=int, default=32)\\n    parser.add_argument(\\\"--use-fusion\\\", action=\\\"store_true\\\",\\n                        help=\\\"Enable fusion head re-ranking\\\")\\n    parser.add_argument(\\\"--use-dataflow-filter\\\", action=\\\"store_true\\\",\\n                        help=\\\"Filter candidates by data-flow reachability\\\")\\n    parser.add_argument(\\\"--max-seq-length\\\", type=int, default=2048)\\n    parser.add_argument(\\\"--dataset\\\", type=str, default=\\\"custom\\\",\\n                        choices=[\\\"swebench_lite\\\", \\\"repobench\\\", \\\"custom\\\"])\\n    parser.add_argument(\\\"--bm25-only\\\", action=\\\"store_true\\\",\\n                        help=\\\"BM25 baseline mode (no model)\\\")\\n    args = parser.parse_args()\\n\\n    k_values = [int(k) for k in args.top_k.split(\\\",\\\")]\\n    model_paths = [p.strip() for p in args.model_path.split(\\\",\\\")]\\n\\n    print(f\\\"Dataset: {args.dataset}\\\")\\n    print(f\\\"Test file: {args.test_file}\\\")\\n    print(f\\\"K values: {k_values}\\\")\\n\\n    instances = load_test_data(args.test_file, args.dataset)\\n    print(f\\\"Loaded {len(instances)} test instances\\\")\\n\\n    all_results = []\\n    for mp in model_paths:\\n        result = evaluate_single_model(mp, instances, args, k_values)\\n        all_results.append(result)\\n        print(f\\\"\\\\n{'='*60}\\\")\\n        print(f\\\"Model: {mp}\\\")\\n        for metric_name, value in result[\\\"metrics\\\"].items():\\n            print(f\\\"  {metric_name}: {value:.4f}\\\")\\n\\n    output = {\\n        \\\"config\\\": {\\n            \\\"dataset\\\": args.dataset,\\n            \\\"test_file\\\": args.test_file,\\n            \\\"k_values\\\": k_values,\\n            \\\"use_fusion\\\": args.use_fusion,\\n            \\\"use_dataflow_filter\\\": args.use_dataflow_filter,\\n            \\\"bm25_only\\\": args.bm25_only,\\n        },\\n        \\\"results\\\": all_results,\\n    }\\n\\n    os.makedirs(os.path.dirname(os.path.abspath(args.output_file)), exist_ok=True)\\n    with open(args.output_file, \\\"w\\\") as f:\\n        json.dump(output, f, indent=2, ensure_ascii=False)\\n    print(f\\\"\\\\nResults saved to {args.output_file}\\\")\\n\\n\\nif __name__ == \\\"__main__\\\":\\n    main()\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d46a3b5a-6c2d-4a6d-9dec-3beefa53c1a7",
  "isSidechain": false,
  "promptId": "22ffd1fb-240e-481f-9bcc-b3f6a42d6805",
  "type": "user",
  "uuid": "356b9c0b-a6fd-4d8e-a1c0-701e842c11e2",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"import os\\\\nos.environ[\\\\\\\"CUDA_VISIBLE_DEVICES\\\\\\\"] = \\\\\\\"4\\\\\\\"\\\\n\\\\n\\\\\\\"\\\\\\\"\\\\\\\"\\\\nStructFuse Retrieval Evaluation Script\\\\n\\\\nEvaluates the StructFuse contrastive retriever on file-level and function-level\\\\nretrieval tasks across SWE-bench Lite, RepoBench-R, and custom held-out sets.\\\\n\\\\nInput:\\\\n  - Trained StructFuse checkpoint(s)\\\\n  - Test file (JSON Lines): each line has {query, gold_files, gold_functions, repo_path}\\\\n  - (Optional) CodeQL data-flow output directory\\\\n\\\\nOutput:\\\\n  - JSON file with per-instance predictions and aggregate metrics:\\\\n    Recall@1/5/10, MRR, Structural Precision\\\\n\\\\nDependencies: transformers, torch, rank_bm25, faiss-cpu, numpy\\\\n\\\\\\\"\\\\\\\"\\\\\\\"\\\\n\\\\nimport argparse\\\\nimport json\\\\nimport os\\\\nimport glob\\\\nimport sys\\\\nimport time\\\\nfrom collections import defaultdict\\\\nfrom dataclasses import dataclass, field\\\\nfrom pathlib import Path\\\\nfrom typing import Optional\\\\n\\\\nimport jsonlines\\\\nimport numpy as np\\\\nimport torch\\\\nimport torch.nn.functional as F\\\\nfrom tqdm import tqdm\\\\nfrom transformers import AutoTokenizer\\\\nfrom rank_bm25 import BM25Okapi\\\\n\\\\nsys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), \\\\\\\"..\\\\\\\", \\\\\\\"training\\\\\\\"))\\\\nfrom contrastive_model import StructFuseEncoder\\\\n\\\\n\\\\n@dataclass\\\\nclass RetrievalInstance:\\\\n    query: str\\\\n    gold_files: list[str]\\\\n    gold_functions: list[str] = field(default_factory=list)\\\\n    repo_path: str = \\\\\\\"\\\\\\\"\\\\n    instance_id: str = \\\\\\\"\\\\\\\"\\\\n    metadata: dict = field(default_factory=dict)\\\\n\\\\n\\\\n@dataclass\\\\nclass RetrievalResult:\\\\n    instance_id: str\\\\n    query: str\\\\n    gold_files: list[str]\\\\n    predicted_files: list[str]\\\\n    scores: list[float]\\\\n    hits: dict[str, bool] = field(default_factory=dict)\\\\n\\\\n\\\\ndef load_test_data(test_file: str, dataset: str) -> list[RetrievalInstance]:\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"Load test instances from JSON Lines file, adapting format per dataset.\\\\\\\"\\\\\\\"\\\\\\\"\\\\n    instances = []\\\\n    with jsonlines.open(test_file) as reader:\\\\n        for i, item in enumerate(reader):\\\\n            if dataset == \\\\\\\"swebench_lite\\\\\\\":\\\\n                inst = RetrievalInstance(\\\\n                    query=item.get(\\\\\\\"problem_statement\\\\\\\", item.get(\\\\\\\"query\\\\\\\", \\\\\\\"\\\\\\\")),\\\\n                    gold_files=item.get(\\\\\\\"gold_files\\\\\\\", []),\\\\n                    gold_functions=item.get(\\\\\\\"gold_functions\\\\\\\", []),\\\\n                    repo_path=item.get(\\\\\\\"repo_path\\\\\\\", item.get(\\\\\\\"repo\\\\\\\", \\\\\\\"\\\\\\\")),\\\\n                    instance_id=item.get(\\\\\\\"instance_id\\\\\\\", f\\\\\\\"swebench_{i}\\\\\\\"),\\\\n                )\\\\n            elif dataset == \\\\\\\"repobench\\\\\\\":\\\\n                inst = RetrievalInstance(\\\\n                    query=item.get(\\\\\\\"query\\\\\\\", \\\\\\\"\\\\\\\"),\\\\n                    gold_files=item.get(\\\\\\\"gold_files\\\\\\\", []),\\\\n                    gold_functions=item.get(\\\\\\\"gold_functions\\\\\\\", []),\\\\n                    repo_path=item.get(\\\\\\\"repo_path\\\\\\\", \\\\\\\"\\\\\\\"),\\\\n                    instance_id=item.get(\\\\\\\"instance_id\\\\\\\", f\\\\\\\"repobench_{i}\\\\\\\"),\\\\n                )\\\\n            else:\\\\n                inst = RetrievalInstance(\\\\n                    query=item[\\\\\\\"query\\\\\\\"],\\\\n                    gold_files=item[\\\\\\\"gold_files\\\\\\\"],\\\\n                    gold_functions=item.get(\\\\\\\"gold_functions\\\\\\\", []),\\\\n                    repo_path=item.get(\\\\\\\"repo_path\\\\\\\", \\\\\\\"\\\\\\\"),\\\\n                    instance_id=item.get(\\\\\\\"instance_id\\\\\\\", f\\\\\\\"custom_{i}\\\\\\\"),\\\\n                    metadata=item.get(\\\\\\\"metadata\\\\\\\", {}),\\\\n                )\\\\n            instances.append(inst)\\\\n    return instances\\\\n\\\\n\\\\ndef collect_candidate_files(repo_path: str, extensions: tuple[str, ...] = (\\\\\\\".py\\\\\\\",)) -> list[dict]:\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"Walk repo and collect candidate source files with their content.\\\\\\\"\\\\\\\"\\\\\\\"\\\\n    candidates = []\\\\n    repo = Path(repo_path)\\\\n    if not repo.exists():\\\\n        return candidates\\\\n    for ext in extensions:\\\\n        for fpath in repo.rglob(f\\\\\\\"*{ext}\\\\\\\"):\\\\n            rel = str(fpath.relative_to(repo))\\\\n            if any(part.startswith(\\\\\\\".\\\\\\\") for part in fpath.parts):\\\\n                continue\\\\n            if \\\\\\\"__pycache__\\\\\\\" in rel:\\\\n                continue\\\\n            fname = fpath.name\\\\n            if (fname.startswith(\\\\\\\"test_\\\\\\\") and fname.endswith(\\\\\\\".py\\\\\\\")) or fname.endswith(\\\\\\\"_test.py\\\\\\\"):\\\\n                continue\\\\n            try:\\\\n                content = fpath.read_text(errors=\\\\\\\"replace\\\\\\\")\\\\n            exc\\\\n\\\\n... [截断: 输出过长，省略 9159 字符] ...\\\\n\\\\n if b[\\\\\\\"path\\\\\\\"] == r[\\\\\\\"path\\\\\\\"]:\\\\n                            ranked[i][\\\\\\\"bm25_score\\\\\\\"] = b.get(\\\\\\\"bm25_score\\\\\\\", 0.0)\\\\n                            break\\\\n                ranked = fusion.rerank(ranked, reachable)\\\\n\\\\n        predicted_files = [r[\\\\\\\"path\\\\\\\"] for r in ranked]\\\\n        score_key = \\\\\\\"fused_score\\\\\\\" if use_fusion else (\\\\\\\"structfuse_score\\\\\\\" if not bm25_only else \\\\\\\"bm25_score\\\\\\\")\\\\n        scores = [r.get(score_key, 0.0) for r in ranked]\\\\n\\\\n        results.append(RetrievalResult(\\\\n            instance_id=inst.instance_id,\\\\n            query=inst.query[:200],\\\\n            gold_files=inst.gold_files,\\\\n            predicted_files=predicted_files,\\\\n            scores=scores,\\\\n        ))\\\\n\\\\n    metrics = compute_metrics(results, k_values)\\\\n    if reachable_map:\\\\n        metrics[\\\\\\\"structural_precision\\\\\\\"] = compute_structural_precision(results, reachable_map)\\\\n\\\\n    return {\\\\n        \\\\\\\"model\\\\\\\": model_path,\\\\n        \\\\\\\"num_instances\\\\\\\": len(instances),\\\\n        \\\\\\\"metrics\\\\\\\": metrics,\\\\n        \\\\\\\"per_instance\\\\\\\": [\\\\n            {\\\\n                \\\\\\\"instance_id\\\\\\\": r.instance_id,\\\\n                \\\\\\\"gold_files\\\\\\\": r.gold_files,\\\\n                \\\\\\\"predicted_top10\\\\\\\": r.predicted_files[:10],\\\\n                \\\\\\\"scores_top10\\\\\\\": r.scores[:10],\\\\n            }\\\\n            for r in results\\\\n        ],\\\\n    }\\\\n\\\\n\\\\ndef main():\\\\n    parser = argparse.ArgumentParser(description=\\\\\\\"StructFuse Retrieval Evaluation\\\\\\\")\\\\n    parser.add_argument(\\\\\\\"--model-path\\\\\\\", type=str, required=True,\\\\n                        help=\\\\\\\"Checkpoint path(s), comma-separated for multi-model comparison\\\\\\\")\\\\n    parser.add_argument(\\\\\\\"--test-file\\\\\\\", type=str, required=True,\\\\n                        help=\\\\\\\"JSON Lines test file\\\\\\\")\\\\n    parser.add_argument(\\\\\\\"--dataflow-dir\\\\\\\", type=str, default=None,\\\\n                        help=\\\\\\\"CodeQL data-flow output directory\\\\\\\")\\\\n    parser.add_argument(\\\\\\\"--output-file\\\\\\\", type=str, default=\\\\\\\"retrieval_results.json\\\\\\\",\\\\n                        help=\\\\\\\"Output JSON file\\\\\\\")\\\\n    parser.add_argument(\\\\\\\"--top-k\\\\\\\", type=str, default=\\\\\\\"1,5,10\\\\\\\",\\\\n                        help=\\\\\\\"Comma-separated k values for Recall@k\\\\\\\")\\\\n    parser.add_argument(\\\\\\\"--batch-size\\\\\\\", type=int, default=32)\\\\n    parser.add_argument(\\\\\\\"--use-fusion\\\\\\\", action=\\\\\\\"store_true\\\\\\\",\\\\n                        help=\\\\\\\"Enable fusion head re-ranking\\\\\\\")\\\\n    parser.add_argument(\\\\\\\"--use-dataflow-filter\\\\\\\", action=\\\\\\\"store_true\\\\\\\",\\\\n                        help=\\\\\\\"Filter candidates by data-flow reachability\\\\\\\")\\\\n    parser.add_argument(\\\\\\\"--max-seq-length\\\\\\\", type=int, default=2048)\\\\n    parser.add_argument(\\\\\\\"--dataset\\\\\\\", type=str, default=\\\\\\\"custom\\\\\\\",\\\\n                        choices=[\\\\\\\"swebench_lite\\\\\\\", \\\\\\\"repobench\\\\\\\", \\\\\\\"custom\\\\\\\"])\\\\n    parser.add_argument(\\\\\\\"--bm25-only\\\\\\\", action=\\\\\\\"store_true\\\\\\\",\\\\n                        help=\\\\\\\"BM25 baseline mode (no model)\\\\\\\")\\\\n    args = parser.parse_args()\\\\n\\\\n    k_values = [int(k) for k in args.top_k.split(\\\\\\\",\\\\\\\")]\\\\n    model_paths = [p.strip() for p in args.model_path.split(\\\\\\\",\\\\\\\")]\\\\n\\\\n    print(f\\\\\\\"Dataset: {args.dataset}\\\\\\\")\\\\n    print(f\\\\\\\"Test file: {args.test_file}\\\\\\\")\\\\n    print(f\\\\\\\"K values: {k_values}\\\\\\\")\\\\n\\\\n    instances = load_test_data(args.test_file, args.dataset)\\\\n    print(f\\\\\\\"Loaded {len(instances)} test instances\\\\\\\")\\\\n\\\\n    all_results = []\\\\n    for mp in model_paths:\\\\n        result = evaluate_single_model(mp, instances, args, k_values)\\\\n        all_results.append(result)\\\\n        print(f\\\\\\\"\\\\\\\\n{'='*60}\\\\\\\")\\\\n        print(f\\\\\\\"Model: {mp}\\\\\\\")\\\\n        for metric_name, value in result[\\\\\\\"metrics\\\\\\\"].items():\\\\n            print(f\\\\\\\"  {metric_name}: {value:.4f}\\\\\\\")\\\\n\\\\n    output = {\\\\n        \\\\\\\"config\\\\\\\": {\\\\n            \\\\\\\"dataset\\\\\\\": args.dataset,\\\\n            \\\\\\\"test_file\\\\\\\": args.test_file,\\\\n            \\\\\\\"k_values\\\\\\\": k_values,\\\\n            \\\\\\\"use_fusion\\\\\\\": args.use_fusion,\\\\n            \\\\\\\"use_dataflow_filter\\\\\\\": args.use_dataflow_filter,\\\\n            \\\\\\\"bm25_only\\\\\\\": args.bm25_only,\\\\n        },\\\\n        \\\\\\\"results\\\\\\\": all_results,\\\\n    }\\\\n\\\\n    os.makedirs(os.path.dirname(os.path.abspath(args.output_file)), exist_ok=True)\\\\n    with open(args.output_file, \\\\\\\"w\\\\\\\") as f:\\\\n        json.dump(output, f, indent=2, ensure_ascii=False)\\\\n    print(f\\\\\\\"\\\\\\\\nResults saved to {args.output_file}\\\\\\\")\\\\n\\\\n\\\\nif __name__ == \\\\\\\"__main__\\\\\\\":\\\\n    main()\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.45}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"import os\\nos.environ[\\\"CUDA_VISIBLE_DEVICES\\\"] = \\\"4\\\"\\n\\n\\\"\\\"\\\"\\nStructFuse Retrieval Evaluation Script\\n\\nEvaluates the StructFuse contrastive retriever on file-level and function-level\\nretrieval tasks across SWE-bench Lite, RepoBench-R, and custom held-out sets.\\n\\nInput:\\n  - Trained StructFuse checkpoint(s)\\n  - Test file (JSON Lines): each line has {query, gold_files, gold_functions, repo_path}\\n  - (Optional) CodeQL data-flow output directory\\n\\nOutput:\\n  - JSON file with per-instance predictions and aggregate metrics:\\n    Recall@1/5/10, MRR, Structural Precision\\n\\nDependencies: transformers, torch, rank_bm25, faiss-cpu, numpy\\n\\\"\\\"\\\"\\n\\nimport argparse\\nimport json\\nimport os\\nimport glob\\nimport sys\\nimport time\\nfrom collections import defaultdict\\nfrom dataclasses import dataclass, field\\nfrom pathlib import Path\\nfrom typing import Optional\\n\\nimport jsonlines\\nimport numpy as np\\nimport torch\\nimport torch.nn.functional as F\\nfrom tqdm import tqdm\\nfrom transformers import AutoTokenizer\\nfrom rank_bm25 import BM25Okapi\\n\\nsys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), \\\"..\\\", \\\"training\\\"))\\nfrom contrastive_model import StructFuseEncoder\\n\\n\\n@dataclass\\nclass RetrievalInstance:\\n    query: str\\n    gold_files: list[str]\\n    gold_functions: list[str] = field(default_factory=list)\\n    repo_path: str = \\\"\\\"\\n    instance_id: str = \\\"\\\"\\n    metadata: dict = field(default_factory=dict)\\n\\n\\n@dataclass\\nclass RetrievalResult:\\n    instance_id: str\\n    query: str\\n    gold_files: list[str]\\n    predicted_files: list[str]\\n    scores: list[float]\\n    hits: dict[str, bool] = field(default_factory=dict)\\n\\n\\ndef load_test_data(test_file: str, dataset: str) -> list[RetrievalInstance]:\\n    \\\"\\\"\\\"Load test instances from JSON Lines file, adapting format per dataset.\\\"\\\"\\\"\\n    instances = []\\n    with jsonlines.open(test_file) as reader:\\n        for i, item in enumerate(reader):\\n            if dataset == \\\"swebench_lite\\\":\\n                inst = RetrievalInstance(\\n                    query=item.get(\\\"problem_statement\\\", item.get(\\\"query\\\", \\\"\\\")),\\n                    gold_files=item.get(\\\"gold_files\\\", []),\\n                    gold_functions=item.get(\\\"gold_functions\\\", []),\\n                    repo_path=item.get(\\\"repo_path\\\", item.get(\\\"repo\\\", \\\"\\\")),\\n                    instance_id=item.get(\\\"instance_id\\\", f\\\"swebench_{i}\\\"),\\n                )\\n            elif dataset == \\\"repobench\\\":\\n                inst = RetrievalInstance(\\n                    query=item.get(\\\"query\\\", \\\"\\\"),\\n                    gold_files=item.get(\\\"gold_files\\\", []),\\n                    gold_functions=item.get(\\\"gold_functions\\\", []),\\n                    repo_path=item.get(\\\"repo_path\\\", \\\"\\\"),\\n                    instance_id=item.get(\\\"instance_id\\\", f\\\"repobench_{i}\\\"),\\n                )\\n            else:\\n                inst = RetrievalInstance(\\n                    query=item[\\\"query\\\"],\\n                    gold_files=item[\\\"gold_files\\\"],\\n                    gold_functions=item.get(\\\"gold_functions\\\", []),\\n                    repo_path=item.get(\\\"repo_path\\\", \\\"\\\"),\\n                    instance_id=item.get(\\\"instance_id\\\", f\\\"custom_{i}\\\"),\\n                    metadata=item.get(\\\"metadata\\\", {}),\\n                )\\n            instances.append(inst)\\n    return instances\\n\\n\\ndef collect_candidate_files(repo_path: str, extensions: tuple[str, ...] = (\\\".py\\\",)) -> list[dict]:\\n    \\\"\\\"\\\"Walk repo and collect candidate source files with their content.\\\"\\\"\\\"\\n    candidates = []\\n    repo = Path(repo_path)\\n    if not repo.exists():\\n        return candidates\\n    for ext in extensions:\\n        for fpath in repo.rglob(f\\\"*{ext}\\\"):\\n            rel = str(fpath.relative_to(repo))\\n            if any(part.startswith(\\\".\\\") for part in fpath.parts):\\n                continue\\n            if \\\"__pycache__\\\" in rel:\\n                continue\\n            fname = fpath.name\\n            if (fname.startswith(\\\"test_\\\") and fname.endswith(\\\".py\\\")) or fname.endswith(\\\"_test.py\\\"):\\n                continue\\n            try:\\n                content = fpath.read_text(errors=\\\"replace\\\")\\n            exc\\n\\n... [截断: 输出过长，省略 9159 字符] ...\\n\\n if b[\\\"path\\\"] == r[\\\"path\\\"]:\\n                            ranked[i][\\\"bm25_score\\\"] = b.get(\\\"bm25_score\\\", 0.0)\\n                            break\\n                ranked = fusion.rerank(ranked, reachable)\\n\\n        predicted_files = [r[\\\"path\\\"] for r in ranked]\\n        score_key = \\\"fused_score\\\" if use_fusion else (\\\"structfuse_score\\\" if not bm25_only else \\\"bm25_score\\\")\\n        scores = [r.get(score_key, 0.0) for r in ranked]\\n\\n        results.append(RetrievalResult(\\n            instance_id=inst.instance_id,\\n            query=inst.query[:200],\\n            gold_files=inst.gold_files,\\n            predicted_files=predicted_files,\\n            scores=scores,\\n        ))\\n\\n    metrics = compute_metrics(results, k_values)\\n    if reachable_map:\\n        metrics[\\\"structural_precision\\\"] = compute_structural_precision(results, reachable_map)\\n\\n    return {\\n        \\\"model\\\": model_path,\\n        \\\"num_instances\\\": len(instances),\\n        \\\"metrics\\\": metrics,\\n        \\\"per_instance\\\": [\\n            {\\n                \\\"instance_id\\\": r.instance_id,\\n                \\\"gold_files\\\": r.gold_files,\\n                \\\"predicted_top10\\\": r.predicted_files[:10],\\n                \\\"scores_top10\\\": r.scores[:10],\\n            }\\n            for r in results\\n        ],\\n    }\\n\\n\\ndef main():\\n    parser = argparse.ArgumentParser(description=\\\"StructFuse Retrieval Evaluation\\\")\\n    parser.add_argument(\\\"--model-path\\\", type=str, required=True,\\n                        help=\\\"Checkpoint path(s), comma-separated for multi-model comparison\\\")\\n    parser.add_argument(\\\"--test-file\\\", type=str, required=True,\\n                        help=\\\"JSON Lines test file\\\")\\n    parser.add_argument(\\\"--dataflow-dir\\\", type=str, default=None,\\n                        help=\\\"CodeQL data-flow output directory\\\")\\n    parser.add_argument(\\\"--output-file\\\", type=str, default=\\\"retrieval_results.json\\\",\\n                        help=\\\"Output JSON file\\\")\\n    parser.add_argument(\\\"--top-k\\\", type=str, default=\\\"1,5,10\\\",\\n                        help=\\\"Comma-separated k values for Recall@k\\\")\\n    parser.add_argument(\\\"--batch-size\\\", type=int, default=32)\\n    parser.add_argument(\\\"--use-fusion\\\", action=\\\"store_true\\\",\\n                        help=\\\"Enable fusion head re-ranking\\\")\\n    parser.add_argument(\\\"--use-dataflow-filter\\\", action=\\\"store_true\\\",\\n                        help=\\\"Filter candidates by data-flow reachability\\\")\\n    parser.add_argument(\\\"--max-seq-length\\\", type=int, default=2048)\\n    parser.add_argument(\\\"--dataset\\\", type=str, default=\\\"custom\\\",\\n                        choices=[\\\"swebench_lite\\\", \\\"repobench\\\", \\\"custom\\\"])\\n    parser.add_argument(\\\"--bm25-only\\\", action=\\\"store_true\\\",\\n                        help=\\\"BM25 baseline mode (no model)\\\")\\n    args = parser.parse_args()\\n\\n    k_values = [int(k) for k in args.top_k.split(\\\",\\\")]\\n    model_paths = [p.strip() for p in args.model_path.split(\\\",\\\")]\\n\\n    print(f\\\"Dataset: {args.dataset}\\\")\\n    print(f\\\"Test file: {args.test_file}\\\")\\n    print(f\\\"K values: {k_values}\\\")\\n\\n    instances = load_test_data(args.test_file, args.dataset)\\n    print(f\\\"Loaded {len(instances)} test instances\\\")\\n\\n    all_results = []\\n    for mp in model_paths:\\n        result = evaluate_single_model(mp, instances, args, k_values)\\n        all_results.append(result)\\n        print(f\\\"\\\\n{'='*60}\\\")\\n        print(f\\\"Model: {mp}\\\")\\n        for metric_name, value in result[\\\"metrics\\\"].items():\\n            print(f\\\"  {metric_name}: {value:.4f}\\\")\\n\\n    output = {\\n        \\\"config\\\": {\\n            \\\"dataset\\\": args.dataset,\\n            \\\"test_file\\\": args.test_file,\\n            \\\"k_values\\\": k_values,\\n            \\\"use_fusion\\\": args.use_fusion,\\n            \\\"use_dataflow_filter\\\": args.use_dataflow_filter,\\n            \\\"bm25_only\\\": args.bm25_only,\\n        },\\n        \\\"results\\\": all_results,\\n    }\\n\\n    os.makedirs(os.path.dirname(os.path.abspath(args.output_file)), exist_ok=True)\\n    with open(args.output_file, \\\"w\\\") as f:\\n        json.dump(output, f, indent=2, ensure_ascii=False)\\n    print(f\\\"\\\\nResults saved to {args.output_file}\\\")\\n\\n\\nif __name__ == \\\"__main__\\\":\\n    main()\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"
    }
  },
  "sourceToolAssistantUUID": "d46a3b5a-6c2d-4a6d-9dec-3beefa53c1a7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "bda3dfbf-4b90-494d-b674-2597173fd381",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 23 · 2026-05-14T20:46:44.884Z_

<details><summary>Logged reasoning block</summary>

```text
The output was truncated for analyze_stratified.py. I need to read it in sections to get the full content. Let me read the parts that were cut off. The output showed 910 lines. I got the beginning and the end but the middle was truncated. Let me read specific sections.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "356b9c0b-a6fd-4d8e-a1c0-701e842c11e2",
  "isSidechain": false,
  "requestId": "req_011Cb37hq2ovpPG5AiEjSamG",
  "type": "assistant",
  "uuid": "98d153a8-bc91-43f8-afa1-37e1bab028c2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "bda3dfbf-4b90-494d-b674-2597173fd381",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GHiKvKbD7Mv3AqCKKQMmZ5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6768,
      "cache_read_input_tokens": 25234,
      "output_tokens": 334,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6768,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 334,
          "cache_read_input_tokens": 25234,
          "cache_creation_input_tokens": 6768,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6768
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

_source line 24 · 2026-05-14T20:46:45.387Z_

输出被截断了，需要分段读取 `analyze_stratified.py` 的中间部分。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "98d153a8-bc91-43f8-afa1-37e1bab028c2",
  "isSidechain": false,
  "requestId": "req_011Cb37hq2ovpPG5AiEjSamG",
  "type": "assistant",
  "uuid": "f0169286-eb49-4378-8ba0-5b7d92c7c4a4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "bda3dfbf-4b90-494d-b674-2597173fd381",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GHiKvKbD7Mv3AqCKKQMmZ5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6768,
      "cache_read_input_tokens": 25234,
      "output_tokens": 334,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6768,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 334,
          "cache_read_input_tokens": 25234,
          "cache_creation_input_tokens": 6768,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6768
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

_source line 25 · 2026-05-14T20:46:46.828Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01VqqgekwJpabk9PB8sEotJX`</summary>

```json
{
  "server": "bjb1-42106",
  "command": "head -200 /root/structfuse/evaluation/analyze_stratified.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f0169286-eb49-4378-8ba0-5b7d92c7c4a4",
  "isSidechain": false,
  "requestId": "req_011Cb37hq2ovpPG5AiEjSamG",
  "type": "assistant",
  "uuid": "23c81284-6672-4841-9829-7bbafd973880",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "bda3dfbf-4b90-494d-b674-2597173fd381",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GHiKvKbD7Mv3AqCKKQMmZ5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6768,
      "cache_read_input_tokens": 25234,
      "output_tokens": 334,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6768,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 334,
          "cache_read_input_tokens": 25234,
          "cache_creation_input_tokens": 6768,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6768
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

_source line 26 · 2026-05-14T20:46:47.188Z_

<details><summary>↩ Tool result · `toolu_01VqqgekwJpabk9PB8sEotJX`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n\\\"\\\"\\\"Stratified analysis of embedding vs random negative strategies by data strata.\\n\\nAnalyses M2 per-instance predictions across:\\n  - Repo size (instance count per repo from M1)\\n  - Candidate pool size (neg_candidates per query)\\n  - Query-positive similarity (cosine sim from model, or text overlap for dry-run)\\n\\nInputs:\\n  - M2 per-instance predictions (from --predictions-dir or re-eval from checkpoints)\\n  - M1 all.jsonl (repo metadata)\\n  - Val JSONL files (query/candidate structure)\\n\\nOutputs:\\n  - stratified_results.json: full per-stratum metrics with bootstrap CI\\n  - stratified_summary.csv: compact table\\n  - stratified_plots.pdf: grouped bar charts, heatmaps, delta trends\\n\\\"\\\"\\\"\\n\\nimport argparse\\nimport csv\\nimport json\\nimport math\\nimport os\\nimport sys\\nfrom collections import Counter, defaultdict\\nfrom pathlib import Path\\nfrom typing import Any, Dict, List, Optional, Tuple\\n\\nimport numpy as np\\n\\nSTRATEGIES = [\\\"random\\\", \\\"embedding_distance\\\", \\\"dataflow_aware\\\"]\\nSTRATEGY_LABELS = {\\\"random\\\": \\\"Random\\\", \\\"embedding_distance\\\": \\\"Embedding\\\", \\\"dataflow_aware\\\": \\\"Dataflow\\\"}\\nSTRATEGY_COLORS = {\\\"random\\\": \\\"#4C72B0\\\", \\\"embedding_distance\\\": \\\"#DD8452\\\", \\\"dataflow_aware\\\": \\\"#55A868\\\"}\\n\\nREPO_SIZE_BINS = {\\n    \\\"small\\\": (0, 50),\\n    \\\"medium\\\": (50, 200),\\n    \\\"large\\\": (200, 500),\\n    \\\"xlarge\\\": (500, float(\\\"inf\\\")),\\n}\\n\\nPOOL_SIZE_BINS = {\\n    \\\"small\\\": (0, 20),\\n    \\\"medium\\\": (20, 40),\\n    \\\"large\\\": (40, 51),\\n}\\n\\nSIMILARITY_BINS = {\\n    \\\"low\\\": (0.0, 0.3),\\n    \\\"medium\\\": (0.3, 0.6),\\n    \\\"high\\\": (0.6, 1.01),\\n}\\n\\nDATAFLOW_BINS = {\\n    \\\"sparse\\\": (0, 2),\\n    \\\"moderate\\\": (2, 10),\\n    \\\"rich\\\": (10, float(\\\"inf\\\")),\\n}\\n\\nNEG_DIFFICULTY_QUARTILE_LABELS = [\\\"Q1_easy\\\", \\\"Q2\\\", \\\"Q3\\\", \\\"Q4_hard\\\"]\\n\\n\\ndef _bin_value(value, bins):\\n    for name, (lo, hi) in bins.items():\\n        if lo <= value < hi:\\n            return name\\n    return \\\"unknown\\\"\\n\\n\\n# ── M1 metadata ───────────────────────────────────────────────────��─\\n\\ndef load_m1_metadata(m1_path: str) -> Tuple[Dict[str, str], Dict[str, int]]:\\n    import re\\n    inst_to_repo = {}\\n    repo_counts: Counter = Counter()\\n    pat_iid = re.compile(r'\\\"instance_id\\\"\\\\s*:\\\\s*\\\"([^\\\"]+)\\\"')\\n    pat_repo = re.compile(r'\\\"repo\\\"\\\\s*:\\\\s*\\\"([^\\\"]+)\\\"')\\n    with open(m1_path) as f:\\n        for line in f:\\n            m_iid = pat_iid.search(line)\\n            m_repo = pat_repo.search(line)\\n            if m_iid and m_repo:\\n                iid = m_iid.group(1)\\n                repo = m_repo.group(1)\\n                inst_to_repo[iid] = repo\\n                repo_counts[repo] += 1\\n    return inst_to_repo, dict(repo_counts)\\n\\n\\n# ── Dataflow graph loading ────────────────────────────────────────────\\n\\ndef load_dataflow_edges(graph_path: str) -> Dict[str, int]:\\n    \\\"\\\"\\\"Load dataflow graph and return {file_key: edge_count}.\\\"\\\"\\\"\\n    with open(graph_path) as f:\\n        graph = json.load(f)\\n    return {k: len(v) for k, v in graph.items()}\\n\\n\\n# ── Val data loading ─────────────────────────────────────────────────\\n\\ndef load_val_samples(val_path: str, lite: bool = False) -> List[Dict[str, Any]]:\\n    \\\"\\\"\\\"Load val JSONL. lite=True skips candidate_tokens (faster for dry-run).\\\"\\\"\\\"\\n    import re\\n    samples = []\\n    pat_qid = re.compile(r'\\\"query_id\\\"\\\\s*:\\\\s*\\\"([^\\\"]+)\\\"')\\n    with open(val_path) as f:\\n        for line in f:\\n            if not line.strip():\\n                continue\\n            if lite:\\n                m = pat_qid.search(line)\\n                if not m:\\n                    continue\\n                qid = m.group(1)\\n                instance_id = qid.split(\\\"::\\\")[0] if \\\"::\\\" in qid else qid\\n                d = json.loads(line)\\n                samples.append({\\n                    \\\"query_id\\\": qid,\\n                    \\\"instance_id\\\": instance_id,\\n                    \\\"pool_size\\\": len(d.get(\\\"neg_candidates\\\", [])),\\n                    \\\"query_tokens\\\": d.get(\\\"query_tokens\\\", \\\"\\\")[:1000],\\n                    \\\"pos_tokens\\\": d.get(\\\"pos_tokens\\\", \\\"\\\")[:1000],\\n                    \\\"neg_candidates\\\": [],\\n                    \\\"candidate_tokens\\\": {},\\n                })\\n            else:\\n                d = json.loads(line)\\n                qid = d[\\\"query_id\\\"]\\n                instance_id = qid.split(\\\"::\\\")[0] if \\\"::\\\" in qid else qid\\n                samples.append({\\n                    \\\"query_id\\\": qid,\\n                    \\\"instance_id\\\": instance_id,\\n                    \\\"pool_size\\\": len(d.get(\\\"neg_candidates\\\", [])),\\n                    \\\"query_tokens\\\": d[\\\"query_tokens\\\"],\\n                    \\\"pos_tokens\\\": d[\\\"pos_tokens\\\"],\\n                    \\\"neg_candidates\\\": d.get(\\\"neg_candidates\\\", []),\\n                    \\\"candidate_tokens\\\": d.get(\\\"candidate_tokens\\\", {}),\\n                })\\n    return samples\\n\\n\\ndef text_similarity(a: str, b: str) -> float:\\n    \\\"\\\"\\\"Jaccard similarity on whitespace-split tokens as a proxy for code similarity.\\\"\\\"\\\"\\n    ta = set(a.split())\\n    tb = set(b.split())\\n    if not ta or not tb:\\n        return 0.0\\n    return len(ta & tb) / len(ta | tb)\\n\\n\\n# ── Re-evaluation from checkpoint ────────────────────────────────────\\n\\ndef reeval_checkpoint(\\n    checkpoint_dir: str,\\n    val_samples: List[Dict],\\n    device: str = \\\"cuda\\\",\\n    max_seq_length: int = 2048,\\n) -> List[Dict]:\\n    import torch\\n    from transformers import AutoTokenizer\\n\\n    train_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), \\\"..\\\", \\\"training\\\")\\n    if train_dir not in sys.path:\\n        sys.path.insert(0, train_dir)\\n    from contrastive_model import StructFuseEncoder\\n\\n    config_path = os.path.join(checkpoint_dir, \\\"training_config.json\\\")\\n    with open(config_path) as f:\\n        config = json.load(f)\\n\\n    model_name = config.get(\\\"model_name\\\", \\\"Qwen/Qwen2.5-Coder-3B\\\")\\n    tokenizer = AutoTokenizer.from_pretrained(checkpoint_dir, trust_remote_code=True)\\n\\n    model = StructFuseEncoder(\\n        model_name=model_name,\\n        proj_dim=config.get(\\\"proj_dim\\\", 256),\\n        use_projection=True,\\n        use_lora=config.get(\\\"use_lora\\\", False),\\n        lora_r=config.get(\\\"lora_r\\\", 16),\\n        use_fusion_head=config.get(\\\"use_fusion_head\\\", False),\\n    )\\n    state_dict = torch.load(os.path.join(checkpoint_dir, \\\"model.pt\\\"), map_location=\\\"cpu\\\")\\n    model.load_state_dict(state_dict, strict=False)\\n    model = model.to(device).eval()\\n\\n    results = []\\n    with torch.no_grad():\\n        for i, sample in enumerate(val_samples):\\n            if (i + 1) % 200 == 0:\\n                print(f\\\"  re-eval {i+1}/{len(val_samples)}\\\", flush=True)\\n\\n            def _encode(text):\\n                enc = tokenizer(text, truncation=True, max_length=max_seq_length,\\n                                padding=True, return_tensors=\\\"pt\\\")\\n                enc = {k: v.to(device) for k, v in enc.items()}\\n                return model.encode(enc[\\\"input_ids\\\"], enc[\\\"attention_mask\\\"])\\n\\n            q_emb = _encode(sample[\\\"query_tokens\\\"])\\n            p_emb = _encode(sample[\\\"pos_tokens\\\"])\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "23c81284-6672-4841-9829-7bbafd973880",
  "isSidechain": false,
  "promptId": "22ffd1fb-240e-481f-9bcc-b3f6a42d6805",
  "type": "user",
  "uuid": "abf20e10-7e63-4bb4-9206-e7fa1f0684ac",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"#!/usr/bin/env python3\\\\n\\\\\\\"\\\\\\\"\\\\\\\"Stratified analysis of embedding vs random negative strategies by data strata.\\\\n\\\\nAnalyses M2 per-instance predictions across:\\\\n  - Repo size (instance count per repo from M1)\\\\n  - Candidate pool size (neg_candidates per query)\\\\n  - Query-positive similarity (cosine sim from model, or text overlap for dry-run)\\\\n\\\\nInputs:\\\\n  - M2 per-instance predictions (from --predictions-dir or re-eval from checkpoints)\\\\n  - M1 all.jsonl (repo metadata)\\\\n  - Val JSONL files (query/candidate structure)\\\\n\\\\nOutputs:\\\\n  - stratified_results.json: full per-stratum metrics with bootstrap CI\\\\n  - stratified_summary.csv: compact table\\\\n  - stratified_plots.pdf: grouped bar charts, heatmaps, delta trends\\\\n\\\\\\\"\\\\\\\"\\\\\\\"\\\\n\\\\nimport argparse\\\\nimport csv\\\\nimport json\\\\nimport math\\\\nimport os\\\\nimport sys\\\\nfrom collections import Counter, defaultdict\\\\nfrom pathlib import Path\\\\nfrom typing import Any, Dict, List, Optional, Tuple\\\\n\\\\nimport numpy as np\\\\n\\\\nSTRATEGIES = [\\\\\\\"random\\\\\\\", \\\\\\\"embedding_distance\\\\\\\", \\\\\\\"dataflow_aware\\\\\\\"]\\\\nSTRATEGY_LABELS = {\\\\\\\"random\\\\\\\": \\\\\\\"Random\\\\\\\", \\\\\\\"embedding_distance\\\\\\\": \\\\\\\"Embedding\\\\\\\", \\\\\\\"dataflow_aware\\\\\\\": \\\\\\\"Dataflow\\\\\\\"}\\\\nSTRATEGY_COLORS = {\\\\\\\"random\\\\\\\": \\\\\\\"#4C72B0\\\\\\\", \\\\\\\"embedding_distance\\\\\\\": \\\\\\\"#DD8452\\\\\\\", \\\\\\\"dataflow_aware\\\\\\\": \\\\\\\"#55A868\\\\\\\"}\\\\n\\\\nREPO_SIZE_BINS = {\\\\n    \\\\\\\"small\\\\\\\": (0, 50),\\\\n    \\\\\\\"medium\\\\\\\": (50, 200),\\\\n    \\\\\\\"large\\\\\\\": (200, 500),\\\\n    \\\\\\\"xlarge\\\\\\\": (500, float(\\\\\\\"inf\\\\\\\")),\\\\n}\\\\n\\\\nPOOL_SIZE_BINS = {\\\\n    \\\\\\\"small\\\\\\\": (0, 20),\\\\n    \\\\\\\"medium\\\\\\\": (20, 40),\\\\n    \\\\\\\"large\\\\\\\": (40, 51),\\\\n}\\\\n\\\\nSIMILARITY_BINS = {\\\\n    \\\\\\\"low\\\\\\\": (0.0, 0.3),\\\\n    \\\\\\\"medium\\\\\\\": (0.3, 0.6),\\\\n    \\\\\\\"high\\\\\\\": (0.6, 1.01),\\\\n}\\\\n\\\\nDATAFLOW_BINS = {\\\\n    \\\\\\\"sparse\\\\\\\": (0, 2),\\\\n    \\\\\\\"moderate\\\\\\\": (2, 10),\\\\n    \\\\\\\"rich\\\\\\\": (10, float(\\\\\\\"inf\\\\\\\")),\\\\n}\\\\n\\\\nNEG_DIFFICULTY_QUARTILE_LABELS = [\\\\\\\"Q1_easy\\\\\\\", \\\\\\\"Q2\\\\\\\", \\\\\\\"Q3\\\\\\\", \\\\\\\"Q4_hard\\\\\\\"]\\\\n\\\\n\\\\ndef _bin_value(value, bins):\\\\n    for name, (lo, hi) in bins.items():\\\\n        if lo <= value < hi:\\\\n            return name\\\\n    return \\\\\\\"unknown\\\\\\\"\\\\n\\\\n\\\\n# ── M1 metadata ───────────────────────────────────────────────────��─\\\\n\\\\ndef load_m1_metadata(m1_path: str) -> Tuple[Dict[str, str], Dict[str, int]]:\\\\n    import re\\\\n    inst_to_repo = {}\\\\n    repo_counts: Counter = Counter()\\\\n    pat_iid = re.compile(r'\\\\\\\"instance_id\\\\\\\"\\\\\\\\s*:\\\\\\\\s*\\\\\\\"([^\\\\\\\"]+)\\\\\\\"')\\\\n    pat_repo = re.compile(r'\\\\\\\"repo\\\\\\\"\\\\\\\\s*:\\\\\\\\s*\\\\\\\"([^\\\\\\\"]+)\\\\\\\"')\\\\n    with open(m1_path) as f:\\\\n        for line in f:\\\\n            m_iid = pat_iid.search(line)\\\\n            m_repo = pat_repo.search(line)\\\\n            if m_iid and m_repo:\\\\n                iid = m_iid.group(1)\\\\n                repo = m_repo.group(1)\\\\n                inst_to_repo[iid] = repo\\\\n                repo_counts[repo] += 1\\\\n    return inst_to_repo, dict(repo_counts)\\\\n\\\\n\\\\n# ── Dataflow graph loading ────────────────────────────────────────────\\\\n\\\\ndef load_dataflow_edges(graph_path: str) -> Dict[str, int]:\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"Load dataflow graph and return {file_key: edge_count}.\\\\\\\"\\\\\\\"\\\\\\\"\\\\n    with open(graph_path) as f:\\\\n        graph = json.load(f)\\\\n    return {k: len(v) for k, v in graph.items()}\\\\n\\\\n\\\\n# ── Val data loading ─────────────────────────────────────────────────\\\\n\\\\ndef load_val_samples(val_path: str, lite: bool = False) -> List[Dict[str, Any]]:\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"Load val JSONL. lite=True skips candidate_tokens (faster for dry-run).\\\\\\\"\\\\\\\"\\\\\\\"\\\\n    import re\\\\n    samples = []\\\\n    pat_qid = re.compile(r'\\\\\\\"query_id\\\\\\\"\\\\\\\\s*:\\\\\\\\s*\\\\\\\"([^\\\\\\\"]+)\\\\\\\"')\\\\n    with open(val_path) as f:\\\\n        for line in f:\\\\n            if not line.strip():\\\\n                continue\\\\n            if lite:\\\\n                m = pat_qid.search(line)\\\\n                if not m:\\\\n                    continue\\\\n                qid = m.group(1)\\\\n                instance_id = qid.split(\\\\\\\"::\\\\\\\")[0] if \\\\\\\"::\\\\\\\" in qid else qid\\\\n                d = json.loads(line)\\\\n                samples.append({\\\\n                    \\\\\\\"query_id\\\\\\\": qid,\\\\n                    \\\\\\\"instance_id\\\\\\\": instance_id,\\\\n                    \\\\\\\"pool_size\\\\\\\": len(d.get(\\\\\\\"neg_candidates\\\\\\\", [])),\\\\n                    \\\\\\\"query_tokens\\\\\\\": d.get(\\\\\\\"query_tokens\\\\\\\", \\\\\\\"\\\\\\\")[:1000],\\\\n                    \\\\\\\"pos_tokens\\\\\\\": d.get(\\\\\\\"pos_tokens\\\\\\\", \\\\\\\"\\\\\\\")[:1000],\\\\n                    \\\\\\\"neg_candidates\\\\\\\": [],\\\\n                    \\\\\\\"candidate_tokens\\\\\\\": {},\\\\n                })\\\\n            else:\\\\n                d = json.loads(line)\\\\n                qid = d[\\\\\\\"query_id\\\\\\\"]\\\\n                instance_id = qid.split(\\\\\\\"::\\\\\\\")[0] if \\\\\\\"::\\\\\\\" in qid else qid\\\\n                samples.append({\\\\n                    \\\\\\\"query_id\\\\\\\": qid,\\\\n                    \\\\\\\"instance_id\\\\\\\": instance_id,\\\\n                    \\\\\\\"pool_size\\\\\\\": len(d.get(\\\\\\\"neg_candidates\\\\\\\", [])),\\\\n                    \\\\\\\"query_tokens\\\\\\\": d[\\\\\\\"query_tokens\\\\\\\"],\\\\n                    \\\\\\\"pos_tokens\\\\\\\": d[\\\\\\\"pos_tokens\\\\\\\"],\\\\n                    \\\\\\\"neg_candidates\\\\\\\": d.get(\\\\\\\"neg_candidates\\\\\\\", []),\\\\n                    \\\\\\\"candidate_tokens\\\\\\\": d.get(\\\\\\\"candidate_tokens\\\\\\\", {}),\\\\n                })\\\\n    return samples\\\\n\\\\n\\\\ndef text_similarity(a: str, b: str) -> float:\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"Jaccard similarity on whitespace-split tokens as a proxy for code similarity.\\\\\\\"\\\\\\\"\\\\\\\"\\\\n    ta = set(a.split())\\\\n    tb = set(b.split())\\\\n    if not ta or not tb:\\\\n        return 0.0\\\\n    return len(ta & tb) / len(ta | tb)\\\\n\\\\n\\\\n# ── Re-evaluation from checkpoint ────────────────────────────────────\\\\n\\\\ndef reeval_checkpoint(\\\\n    checkpoint_dir: str,\\\\n    val_samples: List[Dict],\\\\n    device: str = \\\\\\\"cuda\\\\\\\",\\\\n    max_seq_length: int = 2048,\\\\n) -> List[Dict]:\\\\n    import torch\\\\n    from transformers import AutoTokenizer\\\\n\\\\n    train_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), \\\\\\\"..\\\\\\\", \\\\\\\"training\\\\\\\")\\\\n    if train_dir not in sys.path:\\\\n        sys.path.insert(0, train_dir)\\\\n    from contrastive_model import StructFuseEncoder\\\\n\\\\n    config_path = os.path.join(checkpoint_dir, \\\\\\\"training_config.json\\\\\\\")\\\\n    with open(config_path) as f:\\\\n        config = json.load(f)\\\\n\\\\n    model_name = config.get(\\\\\\\"model_name\\\\\\\", \\\\\\\"Qwen/Qwen2.5-Coder-3B\\\\\\\")\\\\n    tokenizer = AutoTokenizer.from_pretrained(checkpoint_dir, trust_remote_code=True)\\\\n\\\\n    model = StructFuseEncoder(\\\\n        model_name=model_name,\\\\n        proj_dim=config.get(\\\\\\\"proj_dim\\\\\\\", 256),\\\\n        use_projection=True,\\\\n        use_lora=config.get(\\\\\\\"use_lora\\\\\\\", False),\\\\n        lora_r=config.get(\\\\\\\"lora_r\\\\\\\", 16),\\\\n        use_fusion_head=config.get(\\\\\\\"use_fusion_head\\\\\\\", False),\\\\n    )\\\\n    state_dict = torch.load(os.path.join(checkpoint_dir, \\\\\\\"model.pt\\\\\\\"), map_location=\\\\\\\"cpu\\\\\\\")\\\\n    model.load_state_dict(state_dict, strict=False)\\\\n    model = model.to(device).eval()\\\\n\\\\n    results = []\\\\n    with torch.no_grad():\\\\n        for i, sample in enumerate(val_samples):\\\\n            if (i + 1) % 200 == 0:\\\\n                print(f\\\\\\\"  re-eval {i+1}/{len(val_samples)}\\\\\\\", flush=True)\\\\n\\\\n            def _encode(text):\\\\n                enc = tokenizer(text, truncation=True, max_length=max_seq_length,\\\\n                                padding=True, return_tensors=\\\\\\\"pt\\\\\\\")\\\\n                enc = {k: v.to(device) for k, v in enc.items()}\\\\n                return model.encode(enc[\\\\\\\"input_ids\\\\\\\"], enc[\\\\\\\"attention_mask\\\\\\\"])\\\\n\\\\n            q_emb = _encode(sample[\\\\\\\"query_tokens\\\\\\\"])\\\\n            p_emb = _encode(sample[\\\\\\\"pos_tokens\\\\\\\"])\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.35}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n\\\"\\\"\\\"Stratified analysis of embedding vs random negative strategies by data strata.\\n\\nAnalyses M2 per-instance predictions across:\\n  - Repo size (instance count per repo from M1)\\n  - Candidate pool size (neg_candidates per query)\\n  - Query-positive similarity (cosine sim from model, or text overlap for dry-run)\\n\\nInputs:\\n  - M2 per-instance predictions (from --predictions-dir or re-eval from checkpoints)\\n  - M1 all.jsonl (repo metadata)\\n  - Val JSONL files (query/candidate structure)\\n\\nOutputs:\\n  - stratified_results.json: full per-stratum metrics with bootstrap CI\\n  - stratified_summary.csv: compact table\\n  - stratified_plots.pdf: grouped bar charts, heatmaps, delta trends\\n\\\"\\\"\\\"\\n\\nimport argparse\\nimport csv\\nimport json\\nimport math\\nimport os\\nimport sys\\nfrom collections import Counter, defaultdict\\nfrom pathlib import Path\\nfrom typing import Any, Dict, List, Optional, Tuple\\n\\nimport numpy as np\\n\\nSTRATEGIES = [\\\"random\\\", \\\"embedding_distance\\\", \\\"dataflow_aware\\\"]\\nSTRATEGY_LABELS = {\\\"random\\\": \\\"Random\\\", \\\"embedding_distance\\\": \\\"Embedding\\\", \\\"dataflow_aware\\\": \\\"Dataflow\\\"}\\nSTRATEGY_COLORS = {\\\"random\\\": \\\"#4C72B0\\\", \\\"embedding_distance\\\": \\\"#DD8452\\\", \\\"dataflow_aware\\\": \\\"#55A868\\\"}\\n\\nREPO_SIZE_BINS = {\\n    \\\"small\\\": (0, 50),\\n    \\\"medium\\\": (50, 200),\\n    \\\"large\\\": (200, 500),\\n    \\\"xlarge\\\": (500, float(\\\"inf\\\")),\\n}\\n\\nPOOL_SIZE_BINS = {\\n    \\\"small\\\": (0, 20),\\n    \\\"medium\\\": (20, 40),\\n    \\\"large\\\": (40, 51),\\n}\\n\\nSIMILARITY_BINS = {\\n    \\\"low\\\": (0.0, 0.3),\\n    \\\"medium\\\": (0.3, 0.6),\\n    \\\"high\\\": (0.6, 1.01),\\n}\\n\\nDATAFLOW_BINS = {\\n    \\\"sparse\\\": (0, 2),\\n    \\\"moderate\\\": (2, 10),\\n    \\\"rich\\\": (10, float(\\\"inf\\\")),\\n}\\n\\nNEG_DIFFICULTY_QUARTILE_LABELS = [\\\"Q1_easy\\\", \\\"Q2\\\", \\\"Q3\\\", \\\"Q4_hard\\\"]\\n\\n\\ndef _bin_value(value, bins):\\n    for name, (lo, hi) in bins.items():\\n        if lo <= value < hi:\\n            return name\\n    return \\\"unknown\\\"\\n\\n\\n# ── M1 metadata ───────────────────────────────────────────────────��─\\n\\ndef load_m1_metadata(m1_path: str) -> Tuple[Dict[str, str], Dict[str, int]]:\\n    import re\\n    inst_to_repo = {}\\n    repo_counts: Counter = Counter()\\n    pat_iid = re.compile(r'\\\"instance_id\\\"\\\\s*:\\\\s*\\\"([^\\\"]+)\\\"')\\n    pat_repo = re.compile(r'\\\"repo\\\"\\\\s*:\\\\s*\\\"([^\\\"]+)\\\"')\\n    with open(m1_path) as f:\\n        for line in f:\\n            m_iid = pat_iid.search(line)\\n            m_repo = pat_repo.search(line)\\n            if m_iid and m_repo:\\n                iid = m_iid.group(1)\\n                repo = m_repo.group(1)\\n                inst_to_repo[iid] = repo\\n                repo_counts[repo] += 1\\n    return inst_to_repo, dict(repo_counts)\\n\\n\\n# ── Dataflow graph loading ────────────────────────────────────────────\\n\\ndef load_dataflow_edges(graph_path: str) -> Dict[str, int]:\\n    \\\"\\\"\\\"Load dataflow graph and return {file_key: edge_count}.\\\"\\\"\\\"\\n    with open(graph_path) as f:\\n        graph = json.load(f)\\n    return {k: len(v) for k, v in graph.items()}\\n\\n\\n# ── Val data loading ─────────────────────────────────────────────────\\n\\ndef load_val_samples(val_path: str, lite: bool = False) -> List[Dict[str, Any]]:\\n    \\\"\\\"\\\"Load val JSONL. lite=True skips candidate_tokens (faster for dry-run).\\\"\\\"\\\"\\n    import re\\n    samples = []\\n    pat_qid = re.compile(r'\\\"query_id\\\"\\\\s*:\\\\s*\\\"([^\\\"]+)\\\"')\\n    with open(val_path) as f:\\n        for line in f:\\n            if not line.strip():\\n                continue\\n            if lite:\\n                m = pat_qid.search(line)\\n                if not m:\\n                    continue\\n                qid = m.group(1)\\n                instance_id = qid.split(\\\"::\\\")[0] if \\\"::\\\" in qid else qid\\n                d = json.loads(line)\\n                samples.append({\\n                    \\\"query_id\\\": qid,\\n                    \\\"instance_id\\\": instance_id,\\n                    \\\"pool_size\\\": len(d.get(\\\"neg_candidates\\\", [])),\\n                    \\\"query_tokens\\\": d.get(\\\"query_tokens\\\", \\\"\\\")[:1000],\\n                    \\\"pos_tokens\\\": d.get(\\\"pos_tokens\\\", \\\"\\\")[:1000],\\n                    \\\"neg_candidates\\\": [],\\n                    \\\"candidate_tokens\\\": {},\\n                })\\n            else:\\n                d = json.loads(line)\\n                qid = d[\\\"query_id\\\"]\\n                instance_id = qid.split(\\\"::\\\")[0] if \\\"::\\\" in qid else qid\\n                samples.append({\\n                    \\\"query_id\\\": qid,\\n                    \\\"instance_id\\\": instance_id,\\n                    \\\"pool_size\\\": len(d.get(\\\"neg_candidates\\\", [])),\\n                    \\\"query_tokens\\\": d[\\\"query_tokens\\\"],\\n                    \\\"pos_tokens\\\": d[\\\"pos_tokens\\\"],\\n                    \\\"neg_candidates\\\": d.get(\\\"neg_candidates\\\", []),\\n                    \\\"candidate_tokens\\\": d.get(\\\"candidate_tokens\\\", {}),\\n                })\\n    return samples\\n\\n\\ndef text_similarity(a: str, b: str) -> float:\\n    \\\"\\\"\\\"Jaccard similarity on whitespace-split tokens as a proxy for code similarity.\\\"\\\"\\\"\\n    ta = set(a.split())\\n    tb = set(b.split())\\n    if not ta or not tb:\\n        return 0.0\\n    return len(ta & tb) / len(ta | tb)\\n\\n\\n# ── Re-evaluation from checkpoint ────────────────────────────────────\\n\\ndef reeval_checkpoint(\\n    checkpoint_dir: str,\\n    val_samples: List[Dict],\\n    device: str = \\\"cuda\\\",\\n    max_seq_length: int = 2048,\\n) -> List[Dict]:\\n    import torch\\n    from transformers import AutoTokenizer\\n\\n    train_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), \\\"..\\\", \\\"training\\\")\\n    if train_dir not in sys.path:\\n        sys.path.insert(0, train_dir)\\n    from contrastive_model import StructFuseEncoder\\n\\n    config_path = os.path.join(checkpoint_dir, \\\"training_config.json\\\")\\n    with open(config_path) as f:\\n        config = json.load(f)\\n\\n    model_name = config.get(\\\"model_name\\\", \\\"Qwen/Qwen2.5-Coder-3B\\\")\\n    tokenizer = AutoTokenizer.from_pretrained(checkpoint_dir, trust_remote_code=True)\\n\\n    model = StructFuseEncoder(\\n        model_name=model_name,\\n        proj_dim=config.get(\\\"proj_dim\\\", 256),\\n        use_projection=True,\\n        use_lora=config.get(\\\"use_lora\\\", False),\\n        lora_r=config.get(\\\"lora_r\\\", 16),\\n        use_fusion_head=config.get(\\\"use_fusion_head\\\", False),\\n    )\\n    state_dict = torch.load(os.path.join(checkpoint_dir, \\\"model.pt\\\"), map_location=\\\"cpu\\\")\\n    model.load_state_dict(state_dict, strict=False)\\n    model = model.to(device).eval()\\n\\n    results = []\\n    with torch.no_grad():\\n        for i, sample in enumerate(val_samples):\\n            if (i + 1) % 200 == 0:\\n                print(f\\\"  re-eval {i+1}/{len(val_samples)}\\\", flush=True)\\n\\n            def _encode(text):\\n                enc = tokenizer(text, truncation=True, max_length=max_seq_length,\\n                                padding=True, return_tensors=\\\"pt\\\")\\n                enc = {k: v.to(device) for k, v in enc.items()}\\n                return model.encode(enc[\\\"input_ids\\\"], enc[\\\"attention_mask\\\"])\\n\\n            q_emb = _encode(sample[\\\"query_tokens\\\"])\\n            p_emb = _encode(sample[\\\"pos_tokens\\\"])\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"
    }
  },
  "sourceToolAssistantUUID": "23c81284-6672-4841-9829-7bbafd973880",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "bda3dfbf-4b90-494d-b674-2597173fd381",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-14T20:46:47.430Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_014bqYc6kckBnFbijmM3MZ4Z`</summary>

```json
{
  "server": "bjb1-42106",
  "command": "head -400 /root/structfuse/evaluation/analyze_stratified.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "abf20e10-7e63-4bb4-9206-e7fa1f0684ac",
  "isSidechain": false,
  "requestId": "req_011Cb37hq2ovpPG5AiEjSamG",
  "type": "assistant",
  "uuid": "7099782d-92b6-44d2-ad2e-7d08df0fa27c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "bda3dfbf-4b90-494d-b674-2597173fd381",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GHiKvKbD7Mv3AqCKKQMmZ5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6768,
      "cache_read_input_tokens": 25234,
      "output_tokens": 334,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6768,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 334,
          "cache_read_input_tokens": 25234,
          "cache_creation_input_tokens": 6768,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6768
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

_source line 28_

```json
{
  "type": "last-prompt",
  "leafUuid": "7099782d-92b6-44d2-ad2e-7d08df0fa27c",
  "sessionId": "bda3dfbf-4b90-494d-b674-2597173fd381"
}
```

---

### Runtime record

_source line 29_

```json
{
  "type": "ai-title",
  "aiTitle": "Add pool-size controlled stratified evaluation to analysis script",
  "sessionId": "bda3dfbf-4b90-494d-b674-2597173fd381"
}
```

---

### Tool result

_source line 30 · 2026-05-14T20:46:47.848Z_

<details><summary>↩ Tool result · `toolu_014bqYc6kckBnFbijmM3MZ4Z`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n\\\"\\\"\\\"Stratified analysis of embedding vs random negative strategies by data strata.\\n\\nAnalyses M2 per-instance predictions across:\\n  - Repo size (instance count per repo from M1)\\n  - Candidate pool size (neg_candidates per query)\\n  - Query-positive similarity (cosine sim from model, or text overlap for dry-run)\\n\\nInputs:\\n  - M2 per-instance predictions (from --predictions-dir or re-eval from checkpoints)\\n  - M1 all.jsonl (repo metadata)\\n  - Val JSONL files (query/candidate structure)\\n\\nOutputs:\\n  - stratified_results.json: full per-stratum metrics with bootstrap CI\\n  - stratified_summary.csv: compact table\\n  - stratified_plots.pdf: grouped bar charts, heatmaps, delta trends\\n\\\"\\\"\\\"\\n\\nimport argparse\\nimport csv\\nimport json\\nimport math\\nimport os\\nimport sys\\nfrom collections import Counter, defaultdict\\nfrom pathlib import Path\\nfrom typing import Any, Dict, List, Optional, Tuple\\n\\nimport numpy as np\\n\\nSTRATEGIES = [\\\"random\\\", \\\"embedding_distance\\\", \\\"dataflow_aware\\\"]\\nSTRATEGY_LABELS = {\\\"random\\\": \\\"Random\\\", \\\"embedding_distance\\\": \\\"Embedding\\\", \\\"dataflow_aware\\\": \\\"Dataflow\\\"}\\nSTRATEGY_COLORS = {\\\"random\\\": \\\"#4C72B0\\\", \\\"embedding_distance\\\": \\\"#DD8452\\\", \\\"dataflow_aware\\\": \\\"#55A868\\\"}\\n\\nREPO_SIZE_BINS = {\\n    \\\"small\\\": (0, 50),\\n    \\\"medium\\\": (50, 200),\\n    \\\"large\\\": (200, 500),\\n    \\\"xlarge\\\": (500, float(\\\"inf\\\")),\\n}\\n\\nPOOL_SIZE_BINS = {\\n    \\\"small\\\": (0, 20),\\n    \\\"medium\\\": (20, 40),\\n    \\\"large\\\": (40, 51),\\n}\\n\\nSIMILARITY_BINS = {\\n    \\\"low\\\": (0.0, 0.3),\\n    \\\"medium\\\": (0.3, 0.6),\\n    \\\"high\\\": (0.6, 1.01),\\n}\\n\\nDATAFLOW_BINS = {\\n    \\\"sparse\\\": (0, 2),\\n    \\\"moderate\\\": (2, 10),\\n    \\\"rich\\\": (10, float(\\\"inf\\\")),\\n}\\n\\nNEG_DIFFICULTY_QUARTILE_LABELS = [\\\"Q1_easy\\\", \\\"Q2\\\", \\\"Q3\\\", \\\"Q4_hard\\\"]\\n\\n\\ndef _bin_value(value, bins):\\n    for name, (lo, hi) in bins.items():\\n        if lo <= value < hi:\\n            return name\\n    return \\\"unknown\\\"\\n\\n\\n# ── M1 metadata ───────────────────────────────────────────────────��─\\n\\ndef load_m1_metadata(m1_path: str) -> Tuple[Dict[str, str], Dict[str, int]]:\\n    import re\\n    inst_to_repo = {}\\n    repo_counts: Counter = Counter()\\n    pat_iid = re.compile(r'\\\"instance_id\\\"\\\\s*:\\\\s*\\\"([^\\\"]+)\\\"')\\n    pat_repo = re.compile(r'\\\"repo\\\"\\\\s*:\\\\s*\\\"([^\\\"]+)\\\"')\\n    with open(m1_path) as f:\\n        for line in f:\\n            m_iid = pat_iid.search(line)\\n            m_repo = pat_repo.search(line)\\n            if m_iid and m_repo:\\n                iid = m_iid.group(1)\\n                repo = m_repo.group(1)\\n                inst_to_repo[iid] = repo\\n                repo_counts[repo] += 1\\n    return inst_to_repo, dict(repo_counts)\\n\\n\\n# ── Dataflow graph loading ────────────────────────────────────────────\\n\\ndef load_dataflow_edges(graph_path: str) -> Dict[str, int]:\\n    \\\"\\\"\\\"Load dataflow graph and return {file_key: edge_count}.\\\"\\\"\\\"\\n    with open(graph_path) as f:\\n        graph = json.load(f)\\n    return {k: len(v) for k, v in graph.items()}\\n\\n\\n# ── Val data loading ─────────────────────────────────────────────────\\n\\ndef load_val_samples(val_path: str, lite: bool = False) -> List[Dict[str, Any]]:\\n    \\\"\\\"\\\"Load val JSONL. lite=True skips candidate_tokens (faster for dry-run).\\\"\\\"\\\"\\n    import re\\n    samples = []\\n    pat_qid = re.compile(r'\\\"query_id\\\"\\\\s*:\\\\s*\\\"([^\\\"]+)\\\"')\\n    with open(val_path) as f:\\n        for line in f:\\n            if not line.strip():\\n                continue\\n            if lite:\\n                m = pat_qid.search(line)\\n                if not m:\\n                    continue\\n                qid = m.group(1)\\n                instance_id = qid.split(\\\"::\\\")[0] if \\\"::\\\" in qid else qid\\n                d = json.loads(line)\\n                samples.append({\\n                    \\\"query_id\\\": qid,\\n                    \\\"instance_id\\\": instance_id,\\n                    \\\"pool_size\\\": len(d.get(\\\"neg_candidates\\\", [])),\\n                    \\\"query_tokens\\\": d.get(\\\"query_tokens\\\", \\\"\\\")[:1000],\\n                    \\\"pos_tokens\\\": d.get(\\\"pos_tokens\\\", \\\"\\\")[:1000],\\n                    \\\"neg_candidates\\\": [],\\n                    \\\"candidate_tokens\\\": {},\\n                })\\n            else:\\n                d = jso\\n\\n... [截断: 输出过长，省略 5849 字符] ...\\n\\n\\\"instance_id\\\"],\\n            \\\"pool_size\\\": sample[\\\"pool_size\\\"],\\n            \\\"rank\\\": rank,\\n            \\\"pos_sim\\\": pos_sim if pos_sim > 0 else tsim,\\n            \\\"total_candidates\\\": pool,\\n        })\\n    return results\\n\\n\\n# ── Metrics computation ──────────────────────────────────────────────\\n\\ndef compute_metrics(results: List[Dict]) -> Dict[str, float]:\\n    if not results:\\n        return {\\\"R@1\\\": 0.0, \\\"R@5\\\": 0.0, \\\"MRR\\\": 0.0, \\\"count\\\": 0}\\n    ranks = [r[\\\"rank\\\"] for r in results]\\n    n = len(ranks)\\n    return {\\n        \\\"R@1\\\": sum(1 for r in ranks if r <= 1) / n,\\n        \\\"R@5\\\": sum(1 for r in ranks if r <= 5) / n,\\n        \\\"MRR\\\": sum(1.0 / r for r in ranks) / n,\\n        \\\"count\\\": n,\\n    }\\n\\n\\ndef _metric_fn(results, metric_name):\\n    m = compute_metrics(results)\\n    return m[metric_name]\\n\\n\\ndef bootstrap_ci(\\n    results: List[Dict],\\n    metric_name: str = \\\"R@1\\\",\\n    n_bootstrap: int = 1000,\\n    ci: float = 0.95,\\n    seed: int = 42,\\n) -> Tuple[float, float, float]:\\n    rng = np.random.RandomState(seed)\\n    n = len(results)\\n    if n == 0:\\n        return (0.0, 0.0, 0.0)\\n\\n    point = _metric_fn(results, metric_name)\\n    boot_values = []\\n    for _ in range(n_bootstrap):\\n        idx = rng.choice(n, n, replace=True)\\n        boot_sample = [results[i] for i in idx]\\n        boot_values.append(_metric_fn(boot_sample, metric_name))\\n\\n    alpha = (1 - ci) / 2\\n    lo = float(np.percentile(boot_values, alpha * 100))\\n    hi = float(np.percentile(boot_values, (1 - alpha) * 100))\\n    return (point, lo, hi)\\n\\n\\n# ── Stratification ───────────────────────────────────────────────────\\n\\ndef assign_strata(\\n    results: List[Dict],\\n    inst_to_repo: Dict[str, str],\\n    repo_counts: Dict[str, int],\\n    dataflow_edges: Optional[Dict[str, int]] = None,\\n) -> List[Dict]:\\n    for r in results:\\n        repo = inst_to_repo.get(r[\\\"instance_id\\\"], \\\"\\\")\\n        rc = repo_counts.get(repo, 0)\\n        r[\\\"repo\\\"] = repo\\n        r[\\\"repo_size\\\"] = rc\\n        r[\\\"repo_size_bin\\\"] = _bin_value(rc, REPO_SIZE_BINS)\\n        r[\\\"pool_size_bin\\\"] = _bin_value(r[\\\"pool_size\\\"], POOL_SIZE_BINS)\\n        r[\\\"sim_bin\\\"] = _bin_value(r[\\\"pos_sim\\\"], SIMILARITY_BINS)\\n        if dataflow_edges is not None:\\n            ec = dataflow_edges.get(r[\\\"query_id\\\"], 0)\\n            r[\\\"dataflow_edge_count\\\"] = ec\\n            r[\\\"dataflow_bin\\\"] = _bin_value(ec, DATAFLOW_BINS)\\n        else:\\n            r[\\\"dataflow_bin\\\"] = \\\"unknown\\\"\\n    return results\\n\\n\\ndef assign_neg_difficulty_quartiles(\\n    all_results: Dict[str, Dict[int, List[Dict]]],\\n    val_samples_cache: Dict[str, List[Dict]],\\n):\\n    \\\"\\\"\\\"Compute text-overlap-based neg difficulty proxy and assign quartiles.\\\"\\\"\\\"\\n    for strategy in list(all_results.keys()):\\n        for seed in list(all_results[strategy].keys()):\\n            results = all_results[strategy][seed]\\n            cache_key = f\\\"{strategy}_s{seed}\\\"\\n            samples = val_samples_cache.get(cache_key, [])\\n            sample_map = {s[\\\"query_id\\\"]: s for s in samples}\\n\\n            margins = []\\n            for r in results:\\n                s = sample_map.get(r[\\\"query_id\\\"])\\n                if s is None:\\n                    margins.append(0.0)\\n                    continue\\n                q_toks = set(s.get(\\\"query_tokens\\\", \\\"\\\")[:1000].split())\\n                p_toks = set(s.get(\\\"pos_tokens\\\", \\\"\\\")[:1000].split())\\n                pos_overlap = len(q_toks & p_toks) / max(len(q_toks | p_toks), 1)\\n                max_neg_overlap = 0.0\\n                neg_cands = s.get(\\\"neg_candidates\\\", [])[:7]\\n                cand_tokens = s.get(\\\"candidate_tokens\\\", {})\\n                for neg_id in neg_cands:\\n                    neg_text = cand_tokens.get(neg_id, \\\"\\\")\\n                    if neg_text:\\n                        n_toks = set(neg_text[:1000].split())\\n                        ov = len(q_toks & n_toks) / max(len(q_toks | n_toks), 1)\\n                        max_neg_overlap = max(max_neg_overlap, ov)\\n                margin = pos_overlap - max_neg_overlap\\n                margins.append(margin)\\n                r[\\\"neg_difficulty_margin\\\"] = margin\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7099782d-92b6-44d2-ad2e-7d08df0fa27c",
  "isSidechain": false,
  "promptId": "22ffd1fb-240e-481f-9bcc-b3f6a42d6805",
  "type": "user",
  "uuid": "718a78e4-2866-4cdb-83fb-8668af21e152",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"#!/usr/bin/env python3\\\\n\\\\\\\"\\\\\\\"\\\\\\\"Stratified analysis of embedding vs random negative strategies by data strata.\\\\n\\\\nAnalyses M2 per-instance predictions across:\\\\n  - Repo size (instance count per repo from M1)\\\\n  - Candidate pool size (neg_candidates per query)\\\\n  - Query-positive similarity (cosine sim from model, or text overlap for dry-run)\\\\n\\\\nInputs:\\\\n  - M2 per-instance predictions (from --predictions-dir or re-eval from checkpoints)\\\\n  - M1 all.jsonl (repo metadata)\\\\n  - Val JSONL files (query/candidate structure)\\\\n\\\\nOutputs:\\\\n  - stratified_results.json: full per-stratum metrics with bootstrap CI\\\\n  - stratified_summary.csv: compact table\\\\n  - stratified_plots.pdf: grouped bar charts, heatmaps, delta trends\\\\n\\\\\\\"\\\\\\\"\\\\\\\"\\\\n\\\\nimport argparse\\\\nimport csv\\\\nimport json\\\\nimport math\\\\nimport os\\\\nimport sys\\\\nfrom collections import Counter, defaultdict\\\\nfrom pathlib import Path\\\\nfrom typing import Any, Dict, List, Optional, Tuple\\\\n\\\\nimport numpy as np\\\\n\\\\nSTRATEGIES = [\\\\\\\"random\\\\\\\", \\\\\\\"embedding_distance\\\\\\\", \\\\\\\"dataflow_aware\\\\\\\"]\\\\nSTRATEGY_LABELS = {\\\\\\\"random\\\\\\\": \\\\\\\"Random\\\\\\\", \\\\\\\"embedding_distance\\\\\\\": \\\\\\\"Embedding\\\\\\\", \\\\\\\"dataflow_aware\\\\\\\": \\\\\\\"Dataflow\\\\\\\"}\\\\nSTRATEGY_COLORS = {\\\\\\\"random\\\\\\\": \\\\\\\"#4C72B0\\\\\\\", \\\\\\\"embedding_distance\\\\\\\": \\\\\\\"#DD8452\\\\\\\", \\\\\\\"dataflow_aware\\\\\\\": \\\\\\\"#55A868\\\\\\\"}\\\\n\\\\nREPO_SIZE_BINS = {\\\\n    \\\\\\\"small\\\\\\\": (0, 50),\\\\n    \\\\\\\"medium\\\\\\\": (50, 200),\\\\n    \\\\\\\"large\\\\\\\": (200, 500),\\\\n    \\\\\\\"xlarge\\\\\\\": (500, float(\\\\\\\"inf\\\\\\\")),\\\\n}\\\\n\\\\nPOOL_SIZE_BINS = {\\\\n    \\\\\\\"small\\\\\\\": (0, 20),\\\\n    \\\\\\\"medium\\\\\\\": (20, 40),\\\\n    \\\\\\\"large\\\\\\\": (40, 51),\\\\n}\\\\n\\\\nSIMILARITY_BINS = {\\\\n    \\\\\\\"low\\\\\\\": (0.0, 0.3),\\\\n    \\\\\\\"medium\\\\\\\": (0.3, 0.6),\\\\n    \\\\\\\"high\\\\\\\": (0.6, 1.01),\\\\n}\\\\n\\\\nDATAFLOW_BINS = {\\\\n    \\\\\\\"sparse\\\\\\\": (0, 2),\\\\n    \\\\\\\"moderate\\\\\\\": (2, 10),\\\\n    \\\\\\\"rich\\\\\\\": (10, float(\\\\\\\"inf\\\\\\\")),\\\\n}\\\\n\\\\nNEG_DIFFICULTY_QUARTILE_LABELS = [\\\\\\\"Q1_easy\\\\\\\", \\\\\\\"Q2\\\\\\\", \\\\\\\"Q3\\\\\\\", \\\\\\\"Q4_hard\\\\\\\"]\\\\n\\\\n\\\\ndef _bin_value(value, bins):\\\\n    for name, (lo, hi) in bins.items():\\\\n        if lo <= value < hi:\\\\n            return name\\\\n    return \\\\\\\"unknown\\\\\\\"\\\\n\\\\n\\\\n# ── M1 metadata ───────────────────────────────────────────────────��─\\\\n\\\\ndef load_m1_metadata(m1_path: str) -> Tuple[Dict[str, str], Dict[str, int]]:\\\\n    import re\\\\n    inst_to_repo = {}\\\\n    repo_counts: Counter = Counter()\\\\n    pat_iid = re.compile(r'\\\\\\\"instance_id\\\\\\\"\\\\\\\\s*:\\\\\\\\s*\\\\\\\"([^\\\\\\\"]+)\\\\\\\"')\\\\n    pat_repo = re.compile(r'\\\\\\\"repo\\\\\\\"\\\\\\\\s*:\\\\\\\\s*\\\\\\\"([^\\\\\\\"]+)\\\\\\\"')\\\\n    with open(m1_path) as f:\\\\n        for line in f:\\\\n            m_iid = pat_iid.search(line)\\\\n            m_repo = pat_repo.search(line)\\\\n            if m_iid and m_repo:\\\\n                iid = m_iid.group(1)\\\\n                repo = m_repo.group(1)\\\\n                inst_to_repo[iid] = repo\\\\n                repo_counts[repo] += 1\\\\n    return inst_to_repo, dict(repo_counts)\\\\n\\\\n\\\\n# ── Dataflow graph loading ────────────────────────────────────────────\\\\n\\\\ndef load_dataflow_edges(graph_path: str) -> Dict[str, int]:\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"Load dataflow graph and return {file_key: edge_count}.\\\\\\\"\\\\\\\"\\\\\\\"\\\\n    with open(graph_path) as f:\\\\n        graph = json.load(f)\\\\n    return {k: len(v) for k, v in graph.items()}\\\\n\\\\n\\\\n# ── Val data loading ─────────────────────────────────────────────────\\\\n\\\\ndef load_val_samples(val_path: str, lite: bool = False) -> List[Dict[str, Any]]:\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"Load val JSONL. lite=True skips candidate_tokens (faster for dry-run).\\\\\\\"\\\\\\\"\\\\\\\"\\\\n    import re\\\\n    samples = []\\\\n    pat_qid = re.compile(r'\\\\\\\"query_id\\\\\\\"\\\\\\\\s*:\\\\\\\\s*\\\\\\\"([^\\\\\\\"]+)\\\\\\\"')\\\\n    with open(val_path) as f:\\\\n        for line in f:\\\\n            if not line.strip():\\\\n                continue\\\\n            if lite:\\\\n                m = pat_qid.search(line)\\\\n                if not m:\\\\n                    continue\\\\n                qid = m.group(1)\\\\n                instance_id = qid.split(\\\\\\\"::\\\\\\\")[0] if \\\\\\\"::\\\\\\\" in qid else qid\\\\n                d = json.loads(line)\\\\n                samples.append({\\\\n                    \\\\\\\"query_id\\\\\\\": qid,\\\\n                    \\\\\\\"instance_id\\\\\\\": instance_id,\\\\n                    \\\\\\\"pool_size\\\\\\\": len(d.get(\\\\\\\"neg_candidates\\\\\\\", [])),\\\\n                    \\\\\\\"query_tokens\\\\\\\": d.get(\\\\\\\"query_tokens\\\\\\\", \\\\\\\"\\\\\\\")[:1000],\\\\n                    \\\\\\\"pos_tokens\\\\\\\": d.get(\\\\\\\"pos_tokens\\\\\\\", \\\\\\\"\\\\\\\")[:1000],\\\\n                    \\\\\\\"neg_candidates\\\\\\\": [],\\\\n                    \\\\\\\"candidate_tokens\\\\\\\": {},\\\\n                })\\\\n            else:\\\\n                d = jso\\\\n\\\\n... [截断: 输出过长，省略 5849 字符] ...\\\\n\\\\n\\\\\\\"instance_id\\\\\\\"],\\\\n            \\\\\\\"pool_size\\\\\\\": sample[\\\\\\\"pool_size\\\\\\\"],\\\\n            \\\\\\\"rank\\\\\\\": rank,\\\\n            \\\\\\\"pos_sim\\\\\\\": pos_sim if pos_sim > 0 else tsim,\\\\n            \\\\\\\"total_candidates\\\\\\\": pool,\\\\n        })\\\\n    return results\\\\n\\\\n\\\\n# ── Metrics computation ──────────────────────────────────────────────\\\\n\\\\ndef compute_metrics(results: List[Dict]) -> Dict[str, float]:\\\\n    if not results:\\\\n        return {\\\\\\\"R@1\\\\\\\": 0.0, \\\\\\\"R@5\\\\\\\": 0.0, \\\\\\\"MRR\\\\\\\": 0.0, \\\\\\\"count\\\\\\\": 0}\\\\n    ranks = [r[\\\\\\\"rank\\\\\\\"] for r in results]\\\\n    n = len(ranks)\\\\n    return {\\\\n        \\\\\\\"R@1\\\\\\\": sum(1 for r in ranks if r <= 1) / n,\\\\n        \\\\\\\"R@5\\\\\\\": sum(1 for r in ranks if r <= 5) / n,\\\\n        \\\\\\\"MRR\\\\\\\": sum(1.0 / r for r in ranks) / n,\\\\n        \\\\\\\"count\\\\\\\": n,\\\\n    }\\\\n\\\\n\\\\ndef _metric_fn(results, metric_name):\\\\n    m = compute_metrics(results)\\\\n    return m[metric_name]\\\\n\\\\n\\\\ndef bootstrap_ci(\\\\n    results: List[Dict],\\\\n    metric_name: str = \\\\\\\"R@1\\\\\\\",\\\\n    n_bootstrap: int = 1000,\\\\n    ci: float = 0.95,\\\\n    seed: int = 42,\\\\n) -> Tuple[float, float, float]:\\\\n    rng = np.random.RandomState(seed)\\\\n    n = len(results)\\\\n    if n == 0:\\\\n        return (0.0, 0.0, 0.0)\\\\n\\\\n    point = _metric_fn(results, metric_name)\\\\n    boot_values = []\\\\n    for _ in range(n_bootstrap):\\\\n        idx = rng.choice(n, n, replace=True)\\\\n        boot_sample = [results[i] for i in idx]\\\\n        boot_values.append(_metric_fn(boot_sample, metric_name))\\\\n\\\\n    alpha = (1 - ci) / 2\\\\n    lo = float(np.percentile(boot_values, alpha * 100))\\\\n    hi = float(np.percentile(boot_values, (1 - alpha) * 100))\\\\n    return (point, lo, hi)\\\\n\\\\n\\\\n# ── Stratification ───────────────────────────────────────────────────\\\\n\\\\ndef assign_strata(\\\\n    results: List[Dict],\\\\n    inst_to_repo: Dict[str, str],\\\\n    repo_counts: Dict[str, int],\\\\n    dataflow_edges: Optional[Dict[str, int]] = None,\\\\n) -> List[Dict]:\\\\n    for r in results:\\\\n        repo = inst_to_repo.get(r[\\\\\\\"instance_id\\\\\\\"], \\\\\\\"\\\\\\\")\\\\n        rc = repo_counts.get(repo, 0)\\\\n        r[\\\\\\\"repo\\\\\\\"] = repo\\\\n        r[\\\\\\\"repo_size\\\\\\\"] = rc\\\\n        r[\\\\\\\"repo_size_bin\\\\\\\"] = _bin_value(rc, REPO_SIZE_BINS)\\\\n        r[\\\\\\\"pool_size_bin\\\\\\\"] = _bin_value(r[\\\\\\\"pool_size\\\\\\\"], POOL_SIZE_BINS)\\\\n        r[\\\\\\\"sim_bin\\\\\\\"] = _bin_value(r[\\\\\\\"pos_sim\\\\\\\"], SIMILARITY_BINS)\\\\n        if dataflow_edges is not None:\\\\n            ec = dataflow_edges.get(r[\\\\\\\"query_id\\\\\\\"], 0)\\\\n            r[\\\\\\\"dataflow_edge_count\\\\\\\"] = ec\\\\n            r[\\\\\\\"dataflow_bin\\\\\\\"] = _bin_value(ec, DATAFLOW_BINS)\\\\n        else:\\\\n            r[\\\\\\\"dataflow_bin\\\\\\\"] = \\\\\\\"unknown\\\\\\\"\\\\n    return results\\\\n\\\\n\\\\ndef assign_neg_difficulty_quartiles(\\\\n    all_results: Dict[str, Dict[int, List[Dict]]],\\\\n    val_samples_cache: Dict[str, List[Dict]],\\\\n):\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"Compute text-overlap-based neg difficulty proxy and assign quartiles.\\\\\\\"\\\\\\\"\\\\\\\"\\\\n    for strategy in list(all_results.keys()):\\\\n        for seed in list(all_results[strategy].keys()):\\\\n            results = all_results[strategy][seed]\\\\n            cache_key = f\\\\\\\"{strategy}_s{seed}\\\\\\\"\\\\n            samples = val_samples_cache.get(cache_key, [])\\\\n            sample_map = {s[\\\\\\\"query_id\\\\\\\"]: s for s in samples}\\\\n\\\\n            margins = []\\\\n            for r in results:\\\\n                s = sample_map.get(r[\\\\\\\"query_id\\\\\\\"])\\\\n                if s is None:\\\\n                    margins.append(0.0)\\\\n                    continue\\\\n                q_toks = set(s.get(\\\\\\\"query_tokens\\\\\\\", \\\\\\\"\\\\\\\")[:1000].split())\\\\n                p_toks = set(s.get(\\\\\\\"pos_tokens\\\\\\\", \\\\\\\"\\\\\\\")[:1000].split())\\\\n                pos_overlap = len(q_toks & p_toks) / max(len(q_toks | p_toks), 1)\\\\n                max_neg_overlap = 0.0\\\\n                neg_cands = s.get(\\\\\\\"neg_candidates\\\\\\\", [])[:7]\\\\n                cand_tokens = s.get(\\\\\\\"candidate_tokens\\\\\\\", {})\\\\n                for neg_id in neg_cands:\\\\n                    neg_text = cand_tokens.get(neg_id, \\\\\\\"\\\\\\\")\\\\n                    if neg_text:\\\\n                        n_toks = set(neg_text[:1000].split())\\\\n                        ov = len(q_toks & n_toks) / max(len(q_toks | n_toks), 1)\\\\n                        max_neg_overlap = max(max_neg_overlap, ov)\\\\n                margin = pos_overlap - max_neg_overlap\\\\n                margins.append(margin)\\\\n                r[\\\\\\\"neg_difficulty_margin\\\\\\\"] = margin\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.4}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n\\\"\\\"\\\"Stratified analysis of embedding vs random negative strategies by data strata.\\n\\nAnalyses M2 per-instance predictions across:\\n  - Repo size (instance count per repo from M1)\\n  - Candidate pool size (neg_candidates per query)\\n  - Query-positive similarity (cosine sim from model, or text overlap for dry-run)\\n\\nInputs:\\n  - M2 per-instance predictions (from --predictions-dir or re-eval from checkpoints)\\n  - M1 all.jsonl (repo metadata)\\n  - Val JSONL files (query/candidate structure)\\n\\nOutputs:\\n  - stratified_results.json: full per-stratum metrics with bootstrap CI\\n  - stratified_summary.csv: compact table\\n  - stratified_plots.pdf: grouped bar charts, heatmaps, delta trends\\n\\\"\\\"\\\"\\n\\nimport argparse\\nimport csv\\nimport json\\nimport math\\nimport os\\nimport sys\\nfrom collections import Counter, defaultdict\\nfrom pathlib import Path\\nfrom typing import Any, Dict, List, Optional, Tuple\\n\\nimport numpy as np\\n\\nSTRATEGIES = [\\\"random\\\", \\\"embedding_distance\\\", \\\"dataflow_aware\\\"]\\nSTRATEGY_LABELS = {\\\"random\\\": \\\"Random\\\", \\\"embedding_distance\\\": \\\"Embedding\\\", \\\"dataflow_aware\\\": \\\"Dataflow\\\"}\\nSTRATEGY_COLORS = {\\\"random\\\": \\\"#4C72B0\\\", \\\"embedding_distance\\\": \\\"#DD8452\\\", \\\"dataflow_aware\\\": \\\"#55A868\\\"}\\n\\nREPO_SIZE_BINS = {\\n    \\\"small\\\": (0, 50),\\n    \\\"medium\\\": (50, 200),\\n    \\\"large\\\": (200, 500),\\n    \\\"xlarge\\\": (500, float(\\\"inf\\\")),\\n}\\n\\nPOOL_SIZE_BINS = {\\n    \\\"small\\\": (0, 20),\\n    \\\"medium\\\": (20, 40),\\n    \\\"large\\\": (40, 51),\\n}\\n\\nSIMILARITY_BINS = {\\n    \\\"low\\\": (0.0, 0.3),\\n    \\\"medium\\\": (0.3, 0.6),\\n    \\\"high\\\": (0.6, 1.01),\\n}\\n\\nDATAFLOW_BINS = {\\n    \\\"sparse\\\": (0, 2),\\n    \\\"moderate\\\": (2, 10),\\n    \\\"rich\\\": (10, float(\\\"inf\\\")),\\n}\\n\\nNEG_DIFFICULTY_QUARTILE_LABELS = [\\\"Q1_easy\\\", \\\"Q2\\\", \\\"Q3\\\", \\\"Q4_hard\\\"]\\n\\n\\ndef _bin_value(value, bins):\\n    for name, (lo, hi) in bins.items():\\n        if lo <= value < hi:\\n            return name\\n    return \\\"unknown\\\"\\n\\n\\n# ── M1 metadata ───────────────────────────────────────────────────��─\\n\\ndef load_m1_metadata(m1_path: str) -> Tuple[Dict[str, str], Dict[str, int]]:\\n    import re\\n    inst_to_repo = {}\\n    repo_counts: Counter = Counter()\\n    pat_iid = re.compile(r'\\\"instance_id\\\"\\\\s*:\\\\s*\\\"([^\\\"]+)\\\"')\\n    pat_repo = re.compile(r'\\\"repo\\\"\\\\s*:\\\\s*\\\"([^\\\"]+)\\\"')\\n    with open(m1_path) as f:\\n        for line in f:\\n            m_iid = pat_iid.search(line)\\n            m_repo = pat_repo.search(line)\\n            if m_iid and m_repo:\\n                iid = m_iid.group(1)\\n                repo = m_repo.group(1)\\n                inst_to_repo[iid] = repo\\n                repo_counts[repo] += 1\\n    return inst_to_repo, dict(repo_counts)\\n\\n\\n# ── Dataflow graph loading ────────────────────────────────────────────\\n\\ndef load_dataflow_edges(graph_path: str) -> Dict[str, int]:\\n    \\\"\\\"\\\"Load dataflow graph and return {file_key: edge_count}.\\\"\\\"\\\"\\n    with open(graph_path) as f:\\n        graph = json.load(f)\\n    return {k: len(v) for k, v in graph.items()}\\n\\n\\n# ── Val data loading ─────────────────────────────────────────────────\\n\\ndef load_val_samples(val_path: str, lite: bool = False) -> List[Dict[str, Any]]:\\n    \\\"\\\"\\\"Load val JSONL. lite=True skips candidate_tokens (faster for dry-run).\\\"\\\"\\\"\\n    import re\\n    samples = []\\n    pat_qid = re.compile(r'\\\"query_id\\\"\\\\s*:\\\\s*\\\"([^\\\"]+)\\\"')\\n    with open(val_path) as f:\\n        for line in f:\\n            if not line.strip():\\n                continue\\n            if lite:\\n                m = pat_qid.search(line)\\n                if not m:\\n                    continue\\n                qid = m.group(1)\\n                instance_id = qid.split(\\\"::\\\")[0] if \\\"::\\\" in qid else qid\\n                d = json.loads(line)\\n                samples.append({\\n                    \\\"query_id\\\": qid,\\n                    \\\"instance_id\\\": instance_id,\\n                    \\\"pool_size\\\": len(d.get(\\\"neg_candidates\\\", [])),\\n                    \\\"query_tokens\\\": d.get(\\\"query_tokens\\\", \\\"\\\")[:1000],\\n                    \\\"pos_tokens\\\": d.get(\\\"pos_tokens\\\", \\\"\\\")[:1000],\\n                    \\\"neg_candidates\\\": [],\\n                    \\\"candidate_tokens\\\": {},\\n                })\\n            else:\\n                d = jso\\n\\n... [截断: 输出过长，省略 5849 字符] ...\\n\\n\\\"instance_id\\\"],\\n            \\\"pool_size\\\": sample[\\\"pool_size\\\"],\\n            \\\"rank\\\": rank,\\n            \\\"pos_sim\\\": pos_sim if pos_sim > 0 else tsim,\\n            \\\"total_candidates\\\": pool,\\n        })\\n    return results\\n\\n\\n# ── Metrics computation ──────────────────────────────────────────────\\n\\ndef compute_metrics(results: List[Dict]) -> Dict[str, float]:\\n    if not results:\\n        return {\\\"R@1\\\": 0.0, \\\"R@5\\\": 0.0, \\\"MRR\\\": 0.0, \\\"count\\\": 0}\\n    ranks = [r[\\\"rank\\\"] for r in results]\\n    n = len(ranks)\\n    return {\\n        \\\"R@1\\\": sum(1 for r in ranks if r <= 1) / n,\\n        \\\"R@5\\\": sum(1 for r in ranks if r <= 5) / n,\\n        \\\"MRR\\\": sum(1.0 / r for r in ranks) / n,\\n        \\\"count\\\": n,\\n    }\\n\\n\\ndef _metric_fn(results, metric_name):\\n    m = compute_metrics(results)\\n    return m[metric_name]\\n\\n\\ndef bootstrap_ci(\\n    results: List[Dict],\\n    metric_name: str = \\\"R@1\\\",\\n    n_bootstrap: int = 1000,\\n    ci: float = 0.95,\\n    seed: int = 42,\\n) -> Tuple[float, float, float]:\\n    rng = np.random.RandomState(seed)\\n    n = len(results)\\n    if n == 0:\\n        return (0.0, 0.0, 0.0)\\n\\n    point = _metric_fn(results, metric_name)\\n    boot_values = []\\n    for _ in range(n_bootstrap):\\n        idx = rng.choice(n, n, replace=True)\\n        boot_sample = [results[i] for i in idx]\\n        boot_values.append(_metric_fn(boot_sample, metric_name))\\n\\n    alpha = (1 - ci) / 2\\n    lo = float(np.percentile(boot_values, alpha * 100))\\n    hi = float(np.percentile(boot_values, (1 - alpha) * 100))\\n    return (point, lo, hi)\\n\\n\\n# ── Stratification ───────────────────────────────────────────────────\\n\\ndef assign_strata(\\n    results: List[Dict],\\n    inst_to_repo: Dict[str, str],\\n    repo_counts: Dict[str, int],\\n    dataflow_edges: Optional[Dict[str, int]] = None,\\n) -> List[Dict]:\\n    for r in results:\\n        repo = inst_to_repo.get(r[\\\"instance_id\\\"], \\\"\\\")\\n        rc = repo_counts.get(repo, 0)\\n        r[\\\"repo\\\"] = repo\\n        r[\\\"repo_size\\\"] = rc\\n        r[\\\"repo_size_bin\\\"] = _bin_value(rc, REPO_SIZE_BINS)\\n        r[\\\"pool_size_bin\\\"] = _bin_value(r[\\\"pool_size\\\"], POOL_SIZE_BINS)\\n        r[\\\"sim_bin\\\"] = _bin_value(r[\\\"pos_sim\\\"], SIMILARITY_BINS)\\n        if dataflow_edges is not None:\\n            ec = dataflow_edges.get(r[\\\"query_id\\\"], 0)\\n            r[\\\"dataflow_edge_count\\\"] = ec\\n            r[\\\"dataflow_bin\\\"] = _bin_value(ec, DATAFLOW_BINS)\\n        else:\\n            r[\\\"dataflow_bin\\\"] = \\\"unknown\\\"\\n    return results\\n\\n\\ndef assign_neg_difficulty_quartiles(\\n    all_results: Dict[str, Dict[int, List[Dict]]],\\n    val_samples_cache: Dict[str, List[Dict]],\\n):\\n    \\\"\\\"\\\"Compute text-overlap-based neg difficulty proxy and assign quartiles.\\\"\\\"\\\"\\n    for strategy in list(all_results.keys()):\\n        for seed in list(all_results[strategy].keys()):\\n            results = all_results[strategy][seed]\\n            cache_key = f\\\"{strategy}_s{seed}\\\"\\n            samples = val_samples_cache.get(cache_key, [])\\n            sample_map = {s[\\\"query_id\\\"]: s for s in samples}\\n\\n            margins = []\\n            for r in results:\\n                s = sample_map.get(r[\\\"query_id\\\"])\\n                if s is None:\\n                    margins.append(0.0)\\n                    continue\\n                q_toks = set(s.get(\\\"query_tokens\\\", \\\"\\\")[:1000].split())\\n                p_toks = set(s.get(\\\"pos_tokens\\\", \\\"\\\")[:1000].split())\\n                pos_overlap = len(q_toks & p_toks) / max(len(q_toks | p_toks), 1)\\n                max_neg_overlap = 0.0\\n                neg_cands = s.get(\\\"neg_candidates\\\", [])[:7]\\n                cand_tokens = s.get(\\\"candidate_tokens\\\", {})\\n                for neg_id in neg_cands:\\n                    neg_text = cand_tokens.get(neg_id, \\\"\\\")\\n                    if neg_text:\\n                        n_toks = set(neg_text[:1000].split())\\n                        ov = len(q_toks & n_toks) / max(len(q_toks | n_toks), 1)\\n                        max_neg_overlap = max(max_neg_overlap, ov)\\n                margin = pos_overlap - max_neg_overlap\\n                margins.append(margin)\\n                r[\\\"neg_difficulty_margin\\\"] = margin\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4}}"
    }
  },
  "sourceToolAssistantUUID": "7099782d-92b6-44d2-ad2e-7d08df0fa27c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "bda3dfbf-4b90-494d-b674-2597173fd381",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 31_

```json
{
  "type": "last-prompt",
  "leafUuid": "718a78e4-2866-4cdb-83fb-8668af21e152",
  "sessionId": "bda3dfbf-4b90-494d-b674-2597173fd381"
}
```

---

### Runtime record

_source line 32_

```json
{
  "type": "ai-title",
  "aiTitle": "Add pool-size controlled stratified evaluation to analysis script",
  "sessionId": "bda3dfbf-4b90-494d-b674-2597173fd381"
}
```

---

### Assistant

_source line 33 · 2026-05-14T20:46:50.877Z_

<details><summary>Logged reasoning block</summary>

```text
Still truncated. Let me read the remaining parts - lines 400-600 and 600-910.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "718a78e4-2866-4cdb-83fb-8668af21e152",
  "isSidechain": false,
  "requestId": "req_011Cb37iMEFksACUwPWgLP8S",
  "type": "assistant",
  "uuid": "7ac58861-3bca-4ffb-bee5-81bc285cc361",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "bda3dfbf-4b90-494d-b674-2597173fd381",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G48b4oYuTYabT5H1kykEoQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6822,
      "cache_read_input_tokens": 32002,
      "output_tokens": 161,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6822,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 161,
          "cache_read_input_tokens": 32002,
          "cache_creation_input_tokens": 6822,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6822
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

_source line 34 · 2026-05-14T20:46:52.985Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01AaTbqWiCwxFCa97XVh3mtV`</summary>

```json
{
  "server": "bjb1-42106",
  "command": "tail -n +380 /root/structfuse/evaluation/analyze_stratified.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7ac58861-3bca-4ffb-bee5-81bc285cc361",
  "isSidechain": false,
  "requestId": "req_011Cb37iMEFksACUwPWgLP8S",
  "type": "assistant",
  "uuid": "170a9ecf-c4ef-430d-bf76-832eb10d4cb8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "bda3dfbf-4b90-494d-b674-2597173fd381",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G48b4oYuTYabT5H1kykEoQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6822,
      "cache_read_input_tokens": 32002,
      "output_tokens": 161,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6822,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 161,
          "cache_read_input_tokens": 32002,
          "cache_creation_input_tokens": 6822,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6822
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

_source line 35 · 2026-05-14T20:46:53.407Z_

<details><summary>↩ Tool result · `toolu_01AaTbqWiCwxFCa97XVh3mtV`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"            margins = []\\n            for r in results:\\n                s = sample_map.get(r[\\\"query_id\\\"])\\n                if s is None:\\n                    margins.append(0.0)\\n                    continue\\n                q_toks = set(s.get(\\\"query_tokens\\\", \\\"\\\")[:1000].split())\\n                p_toks = set(s.get(\\\"pos_tokens\\\", \\\"\\\")[:1000].split())\\n                pos_overlap = len(q_toks & p_toks) / max(len(q_toks | p_toks), 1)\\n                max_neg_overlap = 0.0\\n                neg_cands = s.get(\\\"neg_candidates\\\", [])[:7]\\n                cand_tokens = s.get(\\\"candidate_tokens\\\", {})\\n                for neg_id in neg_cands:\\n                    neg_text = cand_tokens.get(neg_id, \\\"\\\")\\n                    if neg_text:\\n                        n_toks = set(neg_text[:1000].split())\\n                        ov = len(q_toks & n_toks) / max(len(q_toks | n_toks), 1)\\n                        max_neg_overlap = max(max_neg_overlap, ov)\\n                margin = pos_overlap - max_neg_overlap\\n                margins.append(margin)\\n                r[\\\"neg_difficulty_margin\\\"] = margin\\n\\n            if margins:\\n                arr = np.array(margins)\\n                q25, q50, q75 = np.percentile(arr, [25, 50, 75])\\n                for r, m in zip(results, margins):\\n                    if m <= q25:\\n                        r[\\\"neg_difficulty_bin\\\"] = \\\"Q4_hard\\\"\\n                    elif m <= q50:\\n                        r[\\\"neg_difficulty_bin\\\"] = \\\"Q3\\\"\\n                    elif m <= q75:\\n                        r[\\\"neg_difficulty_bin\\\"] = \\\"Q2\\\"\\n                    else:\\n                        r[\\\"neg_difficulty_bin\\\"] = \\\"Q1_easy\\\"\\n\\n\\ndef group_by(results: List[Dict], key: str) -> Dict[str, List[Dict]]:\\n    groups: Dict[str, List[Dict]] = defaultdict(list)\\n    for r in results:\\n        groups[r[key]].append(r)\\n    return dict(groups)\\n\\n\\n# ── Analysis core ────────────────────────────────────────────────────\\n\\ndef run_stratified_analysis(\\n    all_results: Dict[str, Dict[int, List[Dict]]],\\n    strata_key: str,\\n    bin_order: List[str],\\n    n_bootstrap: int = 1000,\\n) -> Dict:\\n    analysis = {}\\n    for bin_name in bin_order:\\n        analysis[bin_name] = {}\\n        for strategy in STRATEGIES:\\n            seed_results = []\\n            for seed, results in all_results.get(strategy, {}).items():\\n                grouped = group_by(results, strata_key)\\n                seed_results.extend(grouped.get(bin_name, []))\\n\\n            metrics = compute_metrics(seed_results)\\n            ci_r1 = bootstrap_ci(seed_results, \\\"R@1\\\", n_bootstrap)\\n            ci_r5 = bootstrap_ci(seed_results, \\\"R@5\\\", n_bootstrap)\\n            ci_mrr = bootstrap_ci(seed_results, \\\"MRR\\\", n_bootstrap)\\n\\n            analysis[bin_name][strategy] = {\\n                \\\"R@1\\\": ci_r1[0],\\n                \\\"R@1_ci\\\": [ci_r1[1], ci_r1[2]],\\n                \\\"R@5\\\": ci_r5[0],\\n                \\\"R@5_ci\\\": [ci_r5[1], ci_r5[2]],\\n                \\\"MRR\\\": ci_mrr[0],\\n                \\\"MRR_ci\\\": [ci_mrr[1], ci_mrr[2]],\\n                \\\"count\\\": metrics[\\\"count\\\"],\\n            }\\n\\n        # Compute deltas (embedding - random)\\n        rand_m = analysis[bin_name].get(\\\"random\\\", {})\\n        for other in [\\\"embedding_distance\\\", \\\"dataflow_aware\\\"]:\\n            other_m = analysis[bin_name].get(other, {})\\n            delta_key = f\\\"{other}_vs_random\\\"\\n            if rand_m and other_m:\\n                for metric in [\\\"R@1\\\", \\\"R@5\\\", \\\"MRR\\\"]:\\n                    rv = rand_m.get(metric, 0)\\n                    ov = other_m.get(metric, 0)\\n                    analysis[bin_name].setdefault(delta_key, {})[f\\\"{metric}_delta\\\"] = ov - rv\\n                    analysis[bin_name][delta_key][f\\\"{metric}_rel_pct\\\"] = (\\n                        (ov - rv) / rv * 100 if rv > 0 else 0.0\\n                    )\\n\\n    return analysis\\n\\n\\n# ── Visualization ────────────────────────────────────────────────────\\n\\ndef make_plots(\\n    repo_analysis: Dict,\\n    pool_analysis: Dict,\\n    sim_analysis: Dict,\\n    output_dir: str,\\n    dataflow_analysis: Optional[Dict] = None,\\n    neg_diff_analysis: Optional[Dict] = No\\n\\n... [截断: 输出过长，省略 14676 字符] ...\\n\\nt\\\")):\\n                        ckpt_dir = candidate\\n                        break\\n                if ckpt_dir is None and os.path.exists(os.path.join(base, \\\"model.pt\\\")):\\n                    ckpt_dir = base\\n                if os.path.exists(ckpt_dir):\\n                    print(f\\\"  Re-evaluating checkpoint: {ckpt_dir}\\\", flush=True)\\n                    results = reeval_checkpoint(\\n                        ckpt_dir, val_samples, args.device, args.max_seq_length\\n                    )\\n                else:\\n                    print(f\\\"  [WARN] Checkpoint not found: {ckpt_dir}\\\", flush=True)\\n                    continue\\n            else:\\n                print(\\\"  [ERROR] No --dry-run, --predictions-dir, or --checkpoints-dir\\\", flush=True)\\n                continue\\n\\n            # Assign strata\\n            results = assign_strata(results, inst_to_repo, repo_counts, dataflow_edges)\\n\\n            # For dry-run or model-based: compute text similarity for sim_bin\\n            if args.dry_run:\\n                for r, s in zip(results, val_samples):\\n                    tsim = text_similarity(s[\\\"query_tokens\\\"][:500], s[\\\"pos_tokens\\\"][:500])\\n                    r[\\\"sim_bin\\\"] = _bin_value(tsim, SIMILARITY_BINS)\\n\\n            all_results[strategy][seed] = results\\n            val_samples_cache[f\\\"{strategy}_s{seed}\\\"] = val_samples\\n            print(f\\\"  -> {len(results)} instances\\\", flush=True)\\n\\n    # Compute neg_difficulty quartiles (text-overlap proxy, CPU-safe)\\n    print(\\\"Computing neg difficulty quartiles...\\\", flush=True)\\n    assign_neg_difficulty_quartiles(all_results, val_samples_cache)\\n\\n    # Run stratified analysis\\n    print(\\\"\\\\nRunning stratified analysis...\\\", flush=True)\\n    repo_analysis = run_stratified_analysis(\\n        all_results, \\\"repo_size_bin\\\", list(REPO_SIZE_BINS.keys()), args.n_bootstrap\\n    )\\n    pool_analysis = run_stratified_analysis(\\n        all_results, \\\"pool_size_bin\\\", list(POOL_SIZE_BINS.keys()), args.n_bootstrap\\n    )\\n    sim_analysis = run_stratified_analysis(\\n        all_results, \\\"sim_bin\\\", list(SIMILARITY_BINS.keys()), args.n_bootstrap\\n    )\\n\\n    dataflow_analysis = {}\\n    if dataflow_edges is not None:\\n        dataflow_analysis = run_stratified_analysis(\\n            all_results, \\\"dataflow_bin\\\", list(DATAFLOW_BINS.keys()), args.n_bootstrap\\n        )\\n\\n    neg_diff_analysis = run_stratified_analysis(\\n        all_results, \\\"neg_difficulty_bin\\\", NEG_DIFFICULTY_QUARTILE_LABELS, args.n_bootstrap\\n    )\\n\\n    # Save JSON\\n    full_results = {\\n        \\\"config\\\": {\\n            \\\"strategies\\\": STRATEGIES,\\n            \\\"seeds\\\": seeds,\\n            \\\"repo_size_bins\\\": {k: list(v) for k, v in REPO_SIZE_BINS.items()},\\n            \\\"pool_size_bins\\\": {k: list(v) for k, v in POOL_SIZE_BINS.items()},\\n            \\\"similarity_bins\\\": {k: list(v) for k, v in SIMILARITY_BINS.items()},\\n            \\\"dataflow_bins\\\": {k: list(v) for k, v in DATAFLOW_BINS.items()},\\n            \\\"neg_difficulty_quartiles\\\": NEG_DIFFICULTY_QUARTILE_LABELS,\\n            \\\"n_bootstrap\\\": args.n_bootstrap,\\n            \\\"dry_run\\\": args.dry_run,\\n        },\\n        \\\"by_repo_size\\\": repo_analysis,\\n        \\\"by_pool_size\\\": pool_analysis,\\n        \\\"by_similarity\\\": sim_analysis,\\n        \\\"by_dataflow\\\": dataflow_analysis,\\n        \\\"by_neg_difficulty\\\": neg_diff_analysis,\\n    }\\n\\n    json_path = os.path.join(args.output_dir, \\\"stratified_results.json\\\")\\n    with open(json_path, \\\"w\\\") as f:\\n        json.dump(full_results, f, indent=2, ensure_ascii=False)\\n    print(f\\\"  Results JSON saved to {json_path}\\\", flush=True)\\n\\n    # CSV summary\\n    csv_path = os.path.join(args.output_dir, \\\"stratified_summary.csv\\\")\\n    write_summary_csv(repo_analysis, pool_analysis, sim_analysis, csv_path, dataflow_analysis, neg_diff_analysis)\\n\\n    # Plots\\n    try:\\n        make_plots(repo_analysis, pool_analysis, sim_analysis, args.output_dir, dataflow_analysis, neg_diff_analysis)\\n    except Exception as e:\\n        print(f\\\"  [WARN] Plot generation failed: {e}\\\", flush=True)\\n\\n    print(\\\"\\\\nDone.\\\", flush=True)\\n\\n\\nif __name__ == \\\"__main__\\\":\\n    main()\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.41}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "170a9ecf-c4ef-430d-bf76-832eb10d4cb8",
  "isSidechain": false,
  "promptId": "22ffd1fb-240e-481f-9bcc-b3f6a42d6805",
  "type": "user",
  "uuid": "7d0b3d77-a5e3-4076-9e99-7bb7d39cf0ce",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"            margins = []\\\\n            for r in results:\\\\n                s = sample_map.get(r[\\\\\\\"query_id\\\\\\\"])\\\\n                if s is None:\\\\n                    margins.append(0.0)\\\\n                    continue\\\\n                q_toks = set(s.get(\\\\\\\"query_tokens\\\\\\\", \\\\\\\"\\\\\\\")[:1000].split())\\\\n                p_toks = set(s.get(\\\\\\\"pos_tokens\\\\\\\", \\\\\\\"\\\\\\\")[:1000].split())\\\\n                pos_overlap = len(q_toks & p_toks) / max(len(q_toks | p_toks), 1)\\\\n                max_neg_overlap = 0.0\\\\n                neg_cands = s.get(\\\\\\\"neg_candidates\\\\\\\", [])[:7]\\\\n                cand_tokens = s.get(\\\\\\\"candidate_tokens\\\\\\\", {})\\\\n                for neg_id in neg_cands:\\\\n                    neg_text = cand_tokens.get(neg_id, \\\\\\\"\\\\\\\")\\\\n                    if neg_text:\\\\n                        n_toks = set(neg_text[:1000].split())\\\\n                        ov = len(q_toks & n_toks) / max(len(q_toks | n_toks), 1)\\\\n                        max_neg_overlap = max(max_neg_overlap, ov)\\\\n                margin = pos_overlap - max_neg_overlap\\\\n                margins.append(margin)\\\\n                r[\\\\\\\"neg_difficulty_margin\\\\\\\"] = margin\\\\n\\\\n            if margins:\\\\n                arr = np.array(margins)\\\\n                q25, q50, q75 = np.percentile(arr, [25, 50, 75])\\\\n                for r, m in zip(results, margins):\\\\n                    if m <= q25:\\\\n                        r[\\\\\\\"neg_difficulty_bin\\\\\\\"] = \\\\\\\"Q4_hard\\\\\\\"\\\\n                    elif m <= q50:\\\\n                        r[\\\\\\\"neg_difficulty_bin\\\\\\\"] = \\\\\\\"Q3\\\\\\\"\\\\n                    elif m <= q75:\\\\n                        r[\\\\\\\"neg_difficulty_bin\\\\\\\"] = \\\\\\\"Q2\\\\\\\"\\\\n                    else:\\\\n                        r[\\\\\\\"neg_difficulty_bin\\\\\\\"] = \\\\\\\"Q1_easy\\\\\\\"\\\\n\\\\n\\\\ndef group_by(results: List[Dict], key: str) -> Dict[str, List[Dict]]:\\\\n    groups: Dict[str, List[Dict]] = defaultdict(list)\\\\n    for r in results:\\\\n        groups[r[key]].append(r)\\\\n    return dict(groups)\\\\n\\\\n\\\\n# ── Analysis core ────────────────────────────────────────────────────\\\\n\\\\ndef run_stratified_analysis(\\\\n    all_results: Dict[str, Dict[int, List[Dict]]],\\\\n    strata_key: str,\\\\n    bin_order: List[str],\\\\n    n_bootstrap: int = 1000,\\\\n) -> Dict:\\\\n    analysis = {}\\\\n    for bin_name in bin_order:\\\\n        analysis[bin_name] = {}\\\\n        for strategy in STRATEGIES:\\\\n            seed_results = []\\\\n            for seed, results in all_results.get(strategy, {}).items():\\\\n                grouped = group_by(results, strata_key)\\\\n                seed_results.extend(grouped.get(bin_name, []))\\\\n\\\\n            metrics = compute_metrics(seed_results)\\\\n            ci_r1 = bootstrap_ci(seed_results, \\\\\\\"R@1\\\\\\\", n_bootstrap)\\\\n            ci_r5 = bootstrap_ci(seed_results, \\\\\\\"R@5\\\\\\\", n_bootstrap)\\\\n            ci_mrr = bootstrap_ci(seed_results, \\\\\\\"MRR\\\\\\\", n_bootstrap)\\\\n\\\\n            analysis[bin_name][strategy] = {\\\\n                \\\\\\\"R@1\\\\\\\": ci_r1[0],\\\\n                \\\\\\\"R@1_ci\\\\\\\": [ci_r1[1], ci_r1[2]],\\\\n                \\\\\\\"R@5\\\\\\\": ci_r5[0],\\\\n                \\\\\\\"R@5_ci\\\\\\\": [ci_r5[1], ci_r5[2]],\\\\n                \\\\\\\"MRR\\\\\\\": ci_mrr[0],\\\\n                \\\\\\\"MRR_ci\\\\\\\": [ci_mrr[1], ci_mrr[2]],\\\\n                \\\\\\\"count\\\\\\\": metrics[\\\\\\\"count\\\\\\\"],\\\\n            }\\\\n\\\\n        # Compute deltas (embedding - random)\\\\n        rand_m = analysis[bin_name].get(\\\\\\\"random\\\\\\\", {})\\\\n        for other in [\\\\\\\"embedding_distance\\\\\\\", \\\\\\\"dataflow_aware\\\\\\\"]:\\\\n            other_m = analysis[bin_name].get(other, {})\\\\n            delta_key = f\\\\\\\"{other}_vs_random\\\\\\\"\\\\n            if rand_m and other_m:\\\\n                for metric in [\\\\\\\"R@1\\\\\\\", \\\\\\\"R@5\\\\\\\", \\\\\\\"MRR\\\\\\\"]:\\\\n                    rv = rand_m.get(metric, 0)\\\\n                    ov = other_m.get(metric, 0)\\\\n                    analysis[bin_name].setdefault(delta_key, {})[f\\\\\\\"{metric}_delta\\\\\\\"] = ov - rv\\\\n                    analysis[bin_name][delta_key][f\\\\\\\"{metric}_rel_pct\\\\\\\"] = (\\\\n                        (ov - rv) / rv * 100 if rv > 0 else 0.0\\\\n                    )\\\\n\\\\n    return analysis\\\\n\\\\n\\\\n# ── Visualization ────────────────────────────────────────────────────\\\\n\\\\ndef make_plots(\\\\n    repo_analysis: Dict,\\\\n    pool_analysis: Dict,\\\\n    sim_analysis: Dict,\\\\n    output_dir: str,\\\\n    dataflow_analysis: Optional[Dict] = None,\\\\n    neg_diff_analysis: Optional[Dict] = No\\\\n\\\\n... [截断: 输出过长，省略 14676 字符] ...\\\\n\\\\nt\\\\\\\")):\\\\n                        ckpt_dir = candidate\\\\n                        break\\\\n                if ckpt_dir is None and os.path.exists(os.path.join(base, \\\\\\\"model.pt\\\\\\\")):\\\\n                    ckpt_dir = base\\\\n                if os.path.exists(ckpt_dir):\\\\n                    print(f\\\\\\\"  Re-evaluating checkpoint: {ckpt_dir}\\\\\\\", flush=True)\\\\n                    results = reeval_checkpoint(\\\\n                        ckpt_dir, val_samples, args.device, args.max_seq_length\\\\n                    )\\\\n                else:\\\\n                    print(f\\\\\\\"  [WARN] Checkpoint not found: {ckpt_dir}\\\\\\\", flush=True)\\\\n                    continue\\\\n            else:\\\\n                print(\\\\\\\"  [ERROR] No --dry-run, --predictions-dir, or --checkpoints-dir\\\\\\\", flush=True)\\\\n                continue\\\\n\\\\n            # Assign strata\\\\n            results = assign_strata(results, inst_to_repo, repo_counts, dataflow_edges)\\\\n\\\\n            # For dry-run or model-based: compute text similarity for sim_bin\\\\n            if args.dry_run:\\\\n                for r, s in zip(results, val_samples):\\\\n                    tsim = text_similarity(s[\\\\\\\"query_tokens\\\\\\\"][:500], s[\\\\\\\"pos_tokens\\\\\\\"][:500])\\\\n                    r[\\\\\\\"sim_bin\\\\\\\"] = _bin_value(tsim, SIMILARITY_BINS)\\\\n\\\\n            all_results[strategy][seed] = results\\\\n            val_samples_cache[f\\\\\\\"{strategy}_s{seed}\\\\\\\"] = val_samples\\\\n            print(f\\\\\\\"  -> {len(results)} instances\\\\\\\", flush=True)\\\\n\\\\n    # Compute neg_difficulty quartiles (text-overlap proxy, CPU-safe)\\\\n    print(\\\\\\\"Computing neg difficulty quartiles...\\\\\\\", flush=True)\\\\n    assign_neg_difficulty_quartiles(all_results, val_samples_cache)\\\\n\\\\n    # Run stratified analysis\\\\n    print(\\\\\\\"\\\\\\\\nRunning stratified analysis...\\\\\\\", flush=True)\\\\n    repo_analysis = run_stratified_analysis(\\\\n        all_results, \\\\\\\"repo_size_bin\\\\\\\", list(REPO_SIZE_BINS.keys()), args.n_bootstrap\\\\n    )\\\\n    pool_analysis = run_stratified_analysis(\\\\n        all_results, \\\\\\\"pool_size_bin\\\\\\\", list(POOL_SIZE_BINS.keys()), args.n_bootstrap\\\\n    )\\\\n    sim_analysis = run_stratified_analysis(\\\\n        all_results, \\\\\\\"sim_bin\\\\\\\", list(SIMILARITY_BINS.keys()), args.n_bootstrap\\\\n    )\\\\n\\\\n    dataflow_analysis = {}\\\\n    if dataflow_edges is not None:\\\\n        dataflow_analysis = run_stratified_analysis(\\\\n            all_results, \\\\\\\"dataflow_bin\\\\\\\", list(DATAFLOW_BINS.keys()), args.n_bootstrap\\\\n        )\\\\n\\\\n    neg_diff_analysis = run_stratified_analysis(\\\\n        all_results, \\\\\\\"neg_difficulty_bin\\\\\\\", NEG_DIFFICULTY_QUARTILE_LABELS, args.n_bootstrap\\\\n    )\\\\n\\\\n    # Save JSON\\\\n    full_results = {\\\\n        \\\\\\\"config\\\\\\\": {\\\\n            \\\\\\\"strategies\\\\\\\": STRATEGIES,\\\\n            \\\\\\\"seeds\\\\\\\": seeds,\\\\n            \\\\\\\"repo_size_bins\\\\\\\": {k: list(v) for k, v in REPO_SIZE_BINS.items()},\\\\n            \\\\\\\"pool_size_bins\\\\\\\": {k: list(v) for k, v in POOL_SIZE_BINS.items()},\\\\n            \\\\\\\"similarity_bins\\\\\\\": {k: list(v) for k, v in SIMILARITY_BINS.items()},\\\\n            \\\\\\\"dataflow_bins\\\\\\\": {k: list(v) for k, v in DATAFLOW_BINS.items()},\\\\n            \\\\\\\"neg_difficulty_quartiles\\\\\\\": NEG_DIFFICULTY_QUARTILE_LABELS,\\\\n            \\\\\\\"n_bootstrap\\\\\\\": args.n_bootstrap,\\\\n            \\\\\\\"dry_run\\\\\\\": args.dry_run,\\\\n        },\\\\n        \\\\\\\"by_repo_size\\\\\\\": repo_analysis,\\\\n        \\\\\\\"by_pool_size\\\\\\\": pool_analysis,\\\\n        \\\\\\\"by_similarity\\\\\\\": sim_analysis,\\\\n        \\\\\\\"by_dataflow\\\\\\\": dataflow_analysis,\\\\n        \\\\\\\"by_neg_difficulty\\\\\\\": neg_diff_analysis,\\\\n    }\\\\n\\\\n    json_path = os.path.join(args.output_dir, \\\\\\\"stratified_results.json\\\\\\\")\\\\n    with open(json_path, \\\\\\\"w\\\\\\\") as f:\\\\n        json.dump(full_results, f, indent=2, ensure_ascii=False)\\\\n    print(f\\\\\\\"  Results JSON saved to {json_path}\\\\\\\", flush=True)\\\\n\\\\n    # CSV summary\\\\n    csv_path = os.path.join(args.output_dir, \\\\\\\"stratified_summary.csv\\\\\\\")\\\\n    write_summary_csv(repo_analysis, pool_analysis, sim_analysis, csv_path, dataflow_analysis, neg_diff_analysis)\\\\n\\\\n    # Plots\\\\n    try:\\\\n        make_plots(repo_analysis, pool_analysis, sim_analysis, args.output_dir, dataflow_analysis, neg_diff_analysis)\\\\n    except Exception as e:\\\\n        print(f\\\\\\\"  [WARN] Plot generation failed: {e}\\\\\\\", flush=True)\\\\n\\\\n    print(\\\\\\\"\\\\\\\\nDone.\\\\\\\", flush=True)\\\\n\\\\n\\\\nif __name__ == \\\\\\\"__main__\\\\\\\":\\\\n    main()\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.41}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"            margins = []\\n            for r in results:\\n                s = sample_map.get(r[\\\"query_id\\\"])\\n                if s is None:\\n                    margins.append(0.0)\\n                    continue\\n                q_toks = set(s.get(\\\"query_tokens\\\", \\\"\\\")[:1000].split())\\n                p_toks = set(s.get(\\\"pos_tokens\\\", \\\"\\\")[:1000].split())\\n                pos_overlap = len(q_toks & p_toks) / max(len(q_toks | p_toks), 1)\\n                max_neg_overlap = 0.0\\n                neg_cands = s.get(\\\"neg_candidates\\\", [])[:7]\\n                cand_tokens = s.get(\\\"candidate_tokens\\\", {})\\n                for neg_id in neg_cands:\\n                    neg_text = cand_tokens.get(neg_id, \\\"\\\")\\n                    if neg_text:\\n                        n_toks = set(neg_text[:1000].split())\\n                        ov = len(q_toks & n_toks) / max(len(q_toks | n_toks), 1)\\n                        max_neg_overlap = max(max_neg_overlap, ov)\\n                margin = pos_overlap - max_neg_overlap\\n                margins.append(margin)\\n                r[\\\"neg_difficulty_margin\\\"] = margin\\n\\n            if margins:\\n                arr = np.array(margins)\\n                q25, q50, q75 = np.percentile(arr, [25, 50, 75])\\n                for r, m in zip(results, margins):\\n                    if m <= q25:\\n                        r[\\\"neg_difficulty_bin\\\"] = \\\"Q4_hard\\\"\\n                    elif m <= q50:\\n                        r[\\\"neg_difficulty_bin\\\"] = \\\"Q3\\\"\\n                    elif m <= q75:\\n                        r[\\\"neg_difficulty_bin\\\"] = \\\"Q2\\\"\\n                    else:\\n                        r[\\\"neg_difficulty_bin\\\"] = \\\"Q1_easy\\\"\\n\\n\\ndef group_by(results: List[Dict], key: str) -> Dict[str, List[Dict]]:\\n    groups: Dict[str, List[Dict]] = defaultdict(list)\\n    for r in results:\\n        groups[r[key]].append(r)\\n    return dict(groups)\\n\\n\\n# ── Analysis core ────────────────────────────────────────────────────\\n\\ndef run_stratified_analysis(\\n    all_results: Dict[str, Dict[int, List[Dict]]],\\n    strata_key: str,\\n    bin_order: List[str],\\n    n_bootstrap: int = 1000,\\n) -> Dict:\\n    analysis = {}\\n    for bin_name in bin_order:\\n        analysis[bin_name] = {}\\n        for strategy in STRATEGIES:\\n            seed_results = []\\n            for seed, results in all_results.get(strategy, {}).items():\\n                grouped = group_by(results, strata_key)\\n                seed_results.extend(grouped.get(bin_name, []))\\n\\n            metrics = compute_metrics(seed_results)\\n            ci_r1 = bootstrap_ci(seed_results, \\\"R@1\\\", n_bootstrap)\\n            ci_r5 = bootstrap_ci(seed_results, \\\"R@5\\\", n_bootstrap)\\n            ci_mrr = bootstrap_ci(seed_results, \\\"MRR\\\", n_bootstrap)\\n\\n            analysis[bin_name][strategy] = {\\n                \\\"R@1\\\": ci_r1[0],\\n                \\\"R@1_ci\\\": [ci_r1[1], ci_r1[2]],\\n                \\\"R@5\\\": ci_r5[0],\\n                \\\"R@5_ci\\\": [ci_r5[1], ci_r5[2]],\\n                \\\"MRR\\\": ci_mrr[0],\\n                \\\"MRR_ci\\\": [ci_mrr[1], ci_mrr[2]],\\n                \\\"count\\\": metrics[\\\"count\\\"],\\n            }\\n\\n        # Compute deltas (embedding - random)\\n        rand_m = analysis[bin_name].get(\\\"random\\\", {})\\n        for other in [\\\"embedding_distance\\\", \\\"dataflow_aware\\\"]:\\n            other_m = analysis[bin_name].get(other, {})\\n            delta_key = f\\\"{other}_vs_random\\\"\\n            if rand_m and other_m:\\n                for metric in [\\\"R@1\\\", \\\"R@5\\\", \\\"MRR\\\"]:\\n                    rv = rand_m.get(metric, 0)\\n                    ov = other_m.get(metric, 0)\\n                    analysis[bin_name].setdefault(delta_key, {})[f\\\"{metric}_delta\\\"] = ov - rv\\n                    analysis[bin_name][delta_key][f\\\"{metric}_rel_pct\\\"] = (\\n                        (ov - rv) / rv * 100 if rv > 0 else 0.0\\n                    )\\n\\n    return analysis\\n\\n\\n# ── Visualization ────────────────────────────────────────────────────\\n\\ndef make_plots(\\n    repo_analysis: Dict,\\n    pool_analysis: Dict,\\n    sim_analysis: Dict,\\n    output_dir: str,\\n    dataflow_analysis: Optional[Dict] = None,\\n    neg_diff_analysis: Optional[Dict] = No\\n\\n... [截断: 输出过长，省略 14676 字符] ...\\n\\nt\\\")):\\n                        ckpt_dir = candidate\\n                        break\\n                if ckpt_dir is None and os.path.exists(os.path.join(base, \\\"model.pt\\\")):\\n                    ckpt_dir = base\\n                if os.path.exists(ckpt_dir):\\n                    print(f\\\"  Re-evaluating checkpoint: {ckpt_dir}\\\", flush=True)\\n                    results = reeval_checkpoint(\\n                        ckpt_dir, val_samples, args.device, args.max_seq_length\\n                    )\\n                else:\\n                    print(f\\\"  [WARN] Checkpoint not found: {ckpt_dir}\\\", flush=True)\\n                    continue\\n            else:\\n                print(\\\"  [ERROR] No --dry-run, --predictions-dir, or --checkpoints-dir\\\", flush=True)\\n                continue\\n\\n            # Assign strata\\n            results = assign_strata(results, inst_to_repo, repo_counts, dataflow_edges)\\n\\n            # For dry-run or model-based: compute text similarity for sim_bin\\n            if args.dry_run:\\n                for r, s in zip(results, val_samples):\\n                    tsim = text_similarity(s[\\\"query_tokens\\\"][:500], s[\\\"pos_tokens\\\"][:500])\\n                    r[\\\"sim_bin\\\"] = _bin_value(tsim, SIMILARITY_BINS)\\n\\n            all_results[strategy][seed] = results\\n            val_samples_cache[f\\\"{strategy}_s{seed}\\\"] = val_samples\\n            print(f\\\"  -> {len(results)} instances\\\", flush=True)\\n\\n    # Compute neg_difficulty quartiles (text-overlap proxy, CPU-safe)\\n    print(\\\"Computing neg difficulty quartiles...\\\", flush=True)\\n    assign_neg_difficulty_quartiles(all_results, val_samples_cache)\\n\\n    # Run stratified analysis\\n    print(\\\"\\\\nRunning stratified analysis...\\\", flush=True)\\n    repo_analysis = run_stratified_analysis(\\n        all_results, \\\"repo_size_bin\\\", list(REPO_SIZE_BINS.keys()), args.n_bootstrap\\n    )\\n    pool_analysis = run_stratified_analysis(\\n        all_results, \\\"pool_size_bin\\\", list(POOL_SIZE_BINS.keys()), args.n_bootstrap\\n    )\\n    sim_analysis = run_stratified_analysis(\\n        all_results, \\\"sim_bin\\\", list(SIMILARITY_BINS.keys()), args.n_bootstrap\\n    )\\n\\n    dataflow_analysis = {}\\n    if dataflow_edges is not None:\\n        dataflow_analysis = run_stratified_analysis(\\n            all_results, \\\"dataflow_bin\\\", list(DATAFLOW_BINS.keys()), args.n_bootstrap\\n        )\\n\\n    neg_diff_analysis = run_stratified_analysis(\\n        all_results, \\\"neg_difficulty_bin\\\", NEG_DIFFICULTY_QUARTILE_LABELS, args.n_bootstrap\\n    )\\n\\n    # Save JSON\\n    full_results = {\\n        \\\"config\\\": {\\n            \\\"strategies\\\": STRATEGIES,\\n            \\\"seeds\\\": seeds,\\n            \\\"repo_size_bins\\\": {k: list(v) for k, v in REPO_SIZE_BINS.items()},\\n            \\\"pool_size_bins\\\": {k: list(v) for k, v in POOL_SIZE_BINS.items()},\\n            \\\"similarity_bins\\\": {k: list(v) for k, v in SIMILARITY_BINS.items()},\\n            \\\"dataflow_bins\\\": {k: list(v) for k, v in DATAFLOW_BINS.items()},\\n            \\\"neg_difficulty_quartiles\\\": NEG_DIFFICULTY_QUARTILE_LABELS,\\n            \\\"n_bootstrap\\\": args.n_bootstrap,\\n            \\\"dry_run\\\": args.dry_run,\\n        },\\n        \\\"by_repo_size\\\": repo_analysis,\\n        \\\"by_pool_size\\\": pool_analysis,\\n        \\\"by_similarity\\\": sim_analysis,\\n        \\\"by_dataflow\\\": dataflow_analysis,\\n        \\\"by_neg_difficulty\\\": neg_diff_analysis,\\n    }\\n\\n    json_path = os.path.join(args.output_dir, \\\"stratified_results.json\\\")\\n    with open(json_path, \\\"w\\\") as f:\\n        json.dump(full_results, f, indent=2, ensure_ascii=False)\\n    print(f\\\"  Results JSON saved to {json_path}\\\", flush=True)\\n\\n    # CSV summary\\n    csv_path = os.path.join(args.output_dir, \\\"stratified_summary.csv\\\")\\n    write_summary_csv(repo_analysis, pool_analysis, sim_analysis, csv_path, dataflow_analysis, neg_diff_analysis)\\n\\n    # Plots\\n    try:\\n        make_plots(repo_analysis, pool_analysis, sim_analysis, args.output_dir, dataflow_analysis, neg_diff_analysis)\\n    except Exception as e:\\n        print(f\\\"  [WARN] Plot generation failed: {e}\\\", flush=True)\\n\\n    print(\\\"\\\\nDone.\\\", flush=True)\\n\\n\\nif __name__ == \\\"__main__\\\":\\n    main()\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.41}}"
    }
  },
  "sourceToolAssistantUUID": "170a9ecf-c4ef-430d-bf76-832eb10d4cb8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "bda3dfbf-4b90-494d-b674-2597173fd381",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 36 · 2026-05-14T20:46:53.416Z_

```json
{
  "parentUuid": "7d0b3d77-a5e3-4076-9e99-7bb7d39cf0ce",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "0d8b8203-802e-4094-ae0f-64aa43de74fc",
  "timestamp": "2026-05-14T20:46:53.416Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "bda3dfbf-4b90-494d-b674-2597173fd381",
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
  "leafUuid": "0d8b8203-802e-4094-ae0f-64aa43de74fc",
  "sessionId": "bda3dfbf-4b90-494d-b674-2597173fd381"
}
```

---

### Runtime record

_source line 38_

```json
{
  "type": "ai-title",
  "aiTitle": "Add pool-size controlled stratified evaluation to analysis script",
  "sessionId": "bda3dfbf-4b90-494d-b674-2597173fd381"
}
```

---

### Assistant

_source line 39 · 2026-05-14T20:47:01.632Z_

<details><summary>Logged reasoning block</summary>

```text
I still have truncation issues. Let me get specific line ranges to capture the full file content. I need to see:
1. Lines ~200-380 (the middle section I'm missing that includes reeval_checkpoint continuation, mock_predictions, etc.)
2. Lines ~480-700 (make_plots, write_summary_csv, and other functions)

Let me piece together what I have so far:
- Lines 1-200: imports, constants, bins, load_m1_metadata, load_dataflow_edges, load_val_samples, text_similarity, beginning of reeval_checkpoint
- Lines 200-400: rest of reeval_checkpoint, mock_predictions function, compute_metrics, bootstrap_ci, assign_strata, assign_neg_difficulty_quartiles (partially)


- Lines 380-end: end of assign_neg_difficulty_quartiles, group_by, run_stratified_analysis, make_plots (truncated), ..., main function

I need to request the middle sections to see the full implementations of mock_predictions, make_plots, and write_summary_csv.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0d8b8203-802e-4094-ae0f-64aa43de74fc",
  "isSidechain": false,
  "requestId": "req_011Cb37ikuJED13seYsfDvoC",
  "type": "assistant",
  "uuid": "0a1417a2-9394-44bb-bb10-f5e9e9d65a39",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "bda3dfbf-4b90-494d-b674-2597173fd381",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GvSW8cBC6cC7v3hrijke5z",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3379,
      "cache_read_input_tokens": 38824,
      "output_tokens": 396,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3379,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 396,
          "cache_read_input_tokens": 38824,
          "cache_creation_input_tokens": 3379,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3379
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

_source line 40 · 2026-05-14T20:47:01.643Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01B9oLexx5iFSxTp9SpYKiK7`</summary>

```json
{
  "server": "bjb1-42106",
  "command": "head -380 /root/structfuse/evaluation/analyze_stratified.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0a1417a2-9394-44bb-bb10-f5e9e9d65a39",
  "isSidechain": false,
  "requestId": "req_011Cb37ikuJED13seYsfDvoC",
  "type": "assistant",
  "uuid": "b76c2ae9-541d-4870-aaa5-90aafe06146b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "bda3dfbf-4b90-494d-b674-2597173fd381",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GvSW8cBC6cC7v3hrijke5z",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3379,
      "cache_read_input_tokens": 38824,
      "output_tokens": 396,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3379,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 396,
          "cache_read_input_tokens": 38824,
          "cache_creation_input_tokens": 3379,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3379
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

_source line 41 · 2026-05-14T20:47:02.065Z_

<details><summary>↩ Tool result · `toolu_01B9oLexx5iFSxTp9SpYKiK7`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n\\\"\\\"\\\"Stratified analysis of embedding vs random negative strategies by data strata.\\n\\nAnalyses M2 per-instance predictions across:\\n  - Repo size (instance count per repo from M1)\\n  - Candidate pool size (neg_candidates per query)\\n  - Query-positive similarity (cosine sim from model, or text overlap for dry-run)\\n\\nInputs:\\n  - M2 per-instance predictions (from --predictions-dir or re-eval from checkpoints)\\n  - M1 all.jsonl (repo metadata)\\n  - Val JSONL files (query/candidate structure)\\n\\nOutputs:\\n  - stratified_results.json: full per-stratum metrics with bootstrap CI\\n  - stratified_summary.csv: compact table\\n  - stratified_plots.pdf: grouped bar charts, heatmaps, delta trends\\n\\\"\\\"\\\"\\n\\nimport argparse\\nimport csv\\nimport json\\nimport math\\nimport os\\nimport sys\\nfrom collections import Counter, defaultdict\\nfrom pathlib import Path\\nfrom typing import Any, Dict, List, Optional, Tuple\\n\\nimport numpy as np\\n\\nSTRATEGIES = [\\\"random\\\", \\\"embedding_distance\\\", \\\"dataflow_aware\\\"]\\nSTRATEGY_LABELS = {\\\"random\\\": \\\"Random\\\", \\\"embedding_distance\\\": \\\"Embedding\\\", \\\"dataflow_aware\\\": \\\"Dataflow\\\"}\\nSTRATEGY_COLORS = {\\\"random\\\": \\\"#4C72B0\\\", \\\"embedding_distance\\\": \\\"#DD8452\\\", \\\"dataflow_aware\\\": \\\"#55A868\\\"}\\n\\nREPO_SIZE_BINS = {\\n    \\\"small\\\": (0, 50),\\n    \\\"medium\\\": (50, 200),\\n    \\\"large\\\": (200, 500),\\n    \\\"xlarge\\\": (500, float(\\\"inf\\\")),\\n}\\n\\nPOOL_SIZE_BINS = {\\n    \\\"small\\\": (0, 20),\\n    \\\"medium\\\": (20, 40),\\n    \\\"large\\\": (40, 51),\\n}\\n\\nSIMILARITY_BINS = {\\n    \\\"low\\\": (0.0, 0.3),\\n    \\\"medium\\\": (0.3, 0.6),\\n    \\\"high\\\": (0.6, 1.01),\\n}\\n\\nDATAFLOW_BINS = {\\n    \\\"sparse\\\": (0, 2),\\n    \\\"moderate\\\": (2, 10),\\n    \\\"rich\\\": (10, float(\\\"inf\\\")),\\n}\\n\\nNEG_DIFFICULTY_QUARTILE_LABELS = [\\\"Q1_easy\\\", \\\"Q2\\\", \\\"Q3\\\", \\\"Q4_hard\\\"]\\n\\n\\ndef _bin_value(value, bins):\\n    for name, (lo, hi) in bins.items():\\n        if lo <= value < hi:\\n            return name\\n    return \\\"unknown\\\"\\n\\n\\n# ── M1 metadata ───────────────────────────────────────────────────��─\\n\\ndef load_m1_metadata(m1_path: str) -> Tuple[Dict[str, str], Dict[str, int]]:\\n    import re\\n    inst_to_repo = {}\\n    repo_counts: Counter = Counter()\\n    pat_iid = re.compile(r'\\\"instance_id\\\"\\\\s*:\\\\s*\\\"([^\\\"]+)\\\"')\\n    pat_repo = re.compile(r'\\\"repo\\\"\\\\s*:\\\\s*\\\"([^\\\"]+)\\\"')\\n    with open(m1_path) as f:\\n        for line in f:\\n            m_iid = pat_iid.search(line)\\n            m_repo = pat_repo.search(line)\\n            if m_iid and m_repo:\\n                iid = m_iid.group(1)\\n                repo = m_repo.group(1)\\n                inst_to_repo[iid] = repo\\n                repo_counts[repo] += 1\\n    return inst_to_repo, dict(repo_counts)\\n\\n\\n# ── Dataflow graph loading ────────────────────────────────────────────\\n\\ndef load_dataflow_edges(graph_path: str) -> Dict[str, int]:\\n    \\\"\\\"\\\"Load dataflow graph and return {file_key: edge_count}.\\\"\\\"\\\"\\n    with open(graph_path) as f:\\n        graph = json.load(f)\\n    return {k: len(v) for k, v in graph.items()}\\n\\n\\n# ── Val data loading ─────────────────────────────────────────────────\\n\\ndef load_val_samples(val_path: str, lite: bool = False) -> List[Dict[str, Any]]:\\n    \\\"\\\"\\\"Load val JSONL. lite=True skips candidate_tokens (faster for dry-run).\\\"\\\"\\\"\\n    import re\\n    samples = []\\n    pat_qid = re.compile(r'\\\"query_id\\\"\\\\s*:\\\\s*\\\"([^\\\"]+)\\\"')\\n    with open(val_path) as f:\\n        for line in f:\\n            if not line.strip():\\n                continue\\n            if lite:\\n                m = pat_qid.search(line)\\n                if not m:\\n                    continue\\n                qid = m.group(1)\\n                instance_id = qid.split(\\\"::\\\")[0] if \\\"::\\\" in qid else qid\\n                d = json.loads(line)\\n                samples.append({\\n                    \\\"query_id\\\": qid,\\n                    \\\"instance_id\\\": instance_id,\\n                    \\\"pool_size\\\": len(d.get(\\\"neg_candidates\\\", [])),\\n                    \\\"query_tokens\\\": d.get(\\\"query_tokens\\\", \\\"\\\")[:1000],\\n                    \\\"pos_tokens\\\": d.get(\\\"pos_tokens\\\", \\\"\\\")[:1000],\\n                    \\\"neg_candidates\\\": [],\\n                    \\\"candidate_tokens\\\": {},\\n                })\\n            else:\\n                d = jso\\n\\n... [截断: 输出过长，省略 4801 字符] ...\\n\\ned.get(\\\"scores_top10\\\") else 0.0,\\n            \\\"total_candidates\\\": max(len(predicted), sample[\\\"pool_size\\\"] + 1),\\n        })\\n    return results\\n\\n\\n# ── Mock predictions (dry-run) ───────────────────────────────────────\\n\\ndef mock_predictions(\\n    val_samples: List[Dict], strategy: str, seed: int\\n) -> List[Dict]:\\n    rng = np.random.RandomState(seed + abs(hash(strategy)) % 10000)\\n    results = []\\n    for sample in val_samples:\\n        pool = 1 + sample[\\\"pool_size\\\"]\\n        if strategy == \\\"random\\\":\\n            rank = rng.randint(1, pool + 1)\\n        elif strategy == \\\"embedding_distance\\\":\\n            rank = max(1, min(pool, int(rng.exponential(pool * 0.35)) + 1))\\n        else:\\n            rank = max(1, min(pool, int(rng.exponential(pool * 0.20)) + 1))\\n\\n        pos_sim = max(0.0, min(1.0, 1.0 - rank / pool + rng.normal(0, 0.08)))\\n        tsim = text_similarity(\\n            sample[\\\"query_tokens\\\"][:500], sample[\\\"pos_tokens\\\"][:500]\\n        )\\n\\n        results.append({\\n            \\\"query_id\\\": sample[\\\"query_id\\\"],\\n            \\\"instance_id\\\": sample[\\\"instance_id\\\"],\\n            \\\"pool_size\\\": sample[\\\"pool_size\\\"],\\n            \\\"rank\\\": rank,\\n            \\\"pos_sim\\\": pos_sim if pos_sim > 0 else tsim,\\n            \\\"total_candidates\\\": pool,\\n        })\\n    return results\\n\\n\\n# ── Metrics computation ──────────────────────────────────────────────\\n\\ndef compute_metrics(results: List[Dict]) -> Dict[str, float]:\\n    if not results:\\n        return {\\\"R@1\\\": 0.0, \\\"R@5\\\": 0.0, \\\"MRR\\\": 0.0, \\\"count\\\": 0}\\n    ranks = [r[\\\"rank\\\"] for r in results]\\n    n = len(ranks)\\n    return {\\n        \\\"R@1\\\": sum(1 for r in ranks if r <= 1) / n,\\n        \\\"R@5\\\": sum(1 for r in ranks if r <= 5) / n,\\n        \\\"MRR\\\": sum(1.0 / r for r in ranks) / n,\\n        \\\"count\\\": n,\\n    }\\n\\n\\ndef _metric_fn(results, metric_name):\\n    m = compute_metrics(results)\\n    return m[metric_name]\\n\\n\\ndef bootstrap_ci(\\n    results: List[Dict],\\n    metric_name: str = \\\"R@1\\\",\\n    n_bootstrap: int = 1000,\\n    ci: float = 0.95,\\n    seed: int = 42,\\n) -> Tuple[float, float, float]:\\n    rng = np.random.RandomState(seed)\\n    n = len(results)\\n    if n == 0:\\n        return (0.0, 0.0, 0.0)\\n\\n    point = _metric_fn(results, metric_name)\\n    boot_values = []\\n    for _ in range(n_bootstrap):\\n        idx = rng.choice(n, n, replace=True)\\n        boot_sample = [results[i] for i in idx]\\n        boot_values.append(_metric_fn(boot_sample, metric_name))\\n\\n    alpha = (1 - ci) / 2\\n    lo = float(np.percentile(boot_values, alpha * 100))\\n    hi = float(np.percentile(boot_values, (1 - alpha) * 100))\\n    return (point, lo, hi)\\n\\n\\n# ── Stratification ───────────────────────────────────────────────────\\n\\ndef assign_strata(\\n    results: List[Dict],\\n    inst_to_repo: Dict[str, str],\\n    repo_counts: Dict[str, int],\\n    dataflow_edges: Optional[Dict[str, int]] = None,\\n) -> List[Dict]:\\n    for r in results:\\n        repo = inst_to_repo.get(r[\\\"instance_id\\\"], \\\"\\\")\\n        rc = repo_counts.get(repo, 0)\\n        r[\\\"repo\\\"] = repo\\n        r[\\\"repo_size\\\"] = rc\\n        r[\\\"repo_size_bin\\\"] = _bin_value(rc, REPO_SIZE_BINS)\\n        r[\\\"pool_size_bin\\\"] = _bin_value(r[\\\"pool_size\\\"], POOL_SIZE_BINS)\\n        r[\\\"sim_bin\\\"] = _bin_value(r[\\\"pos_sim\\\"], SIMILARITY_BINS)\\n        if dataflow_edges is not None:\\n            ec = dataflow_edges.get(r[\\\"query_id\\\"], 0)\\n            r[\\\"dataflow_edge_count\\\"] = ec\\n            r[\\\"dataflow_bin\\\"] = _bin_value(ec, DATAFLOW_BINS)\\n        else:\\n            r[\\\"dataflow_bin\\\"] = \\\"unknown\\\"\\n    return results\\n\\n\\ndef assign_neg_difficulty_quartiles(\\n    all_results: Dict[str, Dict[int, List[Dict]]],\\n    val_samples_cache: Dict[str, List[Dict]],\\n):\\n    \\\"\\\"\\\"Compute text-overlap-based neg difficulty proxy and assign quartiles.\\\"\\\"\\\"\\n    for strategy in list(all_results.keys()):\\n        for seed in list(all_results[strategy].keys()):\\n            results = all_results[strategy][seed]\\n            cache_key = f\\\"{strategy}_s{seed}\\\"\\n            samples = val_samples_cache.get(cache_key, [])\\n            sample_map = {s[\\\"query_id\\\"]: s for s in samples}\\n\\n            margins = []\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.41}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b76c2ae9-541d-4870-aaa5-90aafe06146b",
  "isSidechain": false,
  "promptId": "22ffd1fb-240e-481f-9bcc-b3f6a42d6805",
  "type": "user",
  "uuid": "a8729d8c-d15a-4932-abe3-89da32dd2b29",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"#!/usr/bin/env python3\\\\n\\\\\\\"\\\\\\\"\\\\\\\"Stratified analysis of embedding vs random negative strategies by data strata.\\\\n\\\\nAnalyses M2 per-instance predictions across:\\\\n  - Repo size (instance count per repo from M1)\\\\n  - Candidate pool size (neg_candidates per query)\\\\n  - Query-positive similarity (cosine sim from model, or text overlap for dry-run)\\\\n\\\\nInputs:\\\\n  - M2 per-instance predictions (from --predictions-dir or re-eval from checkpoints)\\\\n  - M1 all.jsonl (repo metadata)\\\\n  - Val JSONL files (query/candidate structure)\\\\n\\\\nOutputs:\\\\n  - stratified_results.json: full per-stratum metrics with bootstrap CI\\\\n  - stratified_summary.csv: compact table\\\\n  - stratified_plots.pdf: grouped bar charts, heatmaps, delta trends\\\\n\\\\\\\"\\\\\\\"\\\\\\\"\\\\n\\\\nimport argparse\\\\nimport csv\\\\nimport json\\\\nimport math\\\\nimport os\\\\nimport sys\\\\nfrom collections import Counter, defaultdict\\\\nfrom pathlib import Path\\\\nfrom typing import Any, Dict, List, Optional, Tuple\\\\n\\\\nimport numpy as np\\\\n\\\\nSTRATEGIES = [\\\\\\\"random\\\\\\\", \\\\\\\"embedding_distance\\\\\\\", \\\\\\\"dataflow_aware\\\\\\\"]\\\\nSTRATEGY_LABELS = {\\\\\\\"random\\\\\\\": \\\\\\\"Random\\\\\\\", \\\\\\\"embedding_distance\\\\\\\": \\\\\\\"Embedding\\\\\\\", \\\\\\\"dataflow_aware\\\\\\\": \\\\\\\"Dataflow\\\\\\\"}\\\\nSTRATEGY_COLORS = {\\\\\\\"random\\\\\\\": \\\\\\\"#4C72B0\\\\\\\", \\\\\\\"embedding_distance\\\\\\\": \\\\\\\"#DD8452\\\\\\\", \\\\\\\"dataflow_aware\\\\\\\": \\\\\\\"#55A868\\\\\\\"}\\\\n\\\\nREPO_SIZE_BINS = {\\\\n    \\\\\\\"small\\\\\\\": (0, 50),\\\\n    \\\\\\\"medium\\\\\\\": (50, 200),\\\\n    \\\\\\\"large\\\\\\\": (200, 500),\\\\n    \\\\\\\"xlarge\\\\\\\": (500, float(\\\\\\\"inf\\\\\\\")),\\\\n}\\\\n\\\\nPOOL_SIZE_BINS = {\\\\n    \\\\\\\"small\\\\\\\": (0, 20),\\\\n    \\\\\\\"medium\\\\\\\": (20, 40),\\\\n    \\\\\\\"large\\\\\\\": (40, 51),\\\\n}\\\\n\\\\nSIMILARITY_BINS = {\\\\n    \\\\\\\"low\\\\\\\": (0.0, 0.3),\\\\n    \\\\\\\"medium\\\\\\\": (0.3, 0.6),\\\\n    \\\\\\\"high\\\\\\\": (0.6, 1.01),\\\\n}\\\\n\\\\nDATAFLOW_BINS = {\\\\n    \\\\\\\"sparse\\\\\\\": (0, 2),\\\\n    \\\\\\\"moderate\\\\\\\": (2, 10),\\\\n    \\\\\\\"rich\\\\\\\": (10, float(\\\\\\\"inf\\\\\\\")),\\\\n}\\\\n\\\\nNEG_DIFFICULTY_QUARTILE_LABELS = [\\\\\\\"Q1_easy\\\\\\\", \\\\\\\"Q2\\\\\\\", \\\\\\\"Q3\\\\\\\", \\\\\\\"Q4_hard\\\\\\\"]\\\\n\\\\n\\\\ndef _bin_value(value, bins):\\\\n    for name, (lo, hi) in bins.items():\\\\n        if lo <= value < hi:\\\\n            return name\\\\n    return \\\\\\\"unknown\\\\\\\"\\\\n\\\\n\\\\n# ── M1 metadata ───────────────────────────────────────────────────��─\\\\n\\\\ndef load_m1_metadata(m1_path: str) -> Tuple[Dict[str, str], Dict[str, int]]:\\\\n    import re\\\\n    inst_to_repo = {}\\\\n    repo_counts: Counter = Counter()\\\\n    pat_iid = re.compile(r'\\\\\\\"instance_id\\\\\\\"\\\\\\\\s*:\\\\\\\\s*\\\\\\\"([^\\\\\\\"]+)\\\\\\\"')\\\\n    pat_repo = re.compile(r'\\\\\\\"repo\\\\\\\"\\\\\\\\s*:\\\\\\\\s*\\\\\\\"([^\\\\\\\"]+)\\\\\\\"')\\\\n    with open(m1_path) as f:\\\\n        for line in f:\\\\n            m_iid = pat_iid.search(line)\\\\n            m_repo = pat_repo.search(line)\\\\n            if m_iid and m_repo:\\\\n                iid = m_iid.group(1)\\\\n                repo = m_repo.group(1)\\\\n                inst_to_repo[iid] = repo\\\\n                repo_counts[repo] += 1\\\\n    return inst_to_repo, dict(repo_counts)\\\\n\\\\n\\\\n# ── Dataflow graph loading ────────────────────────────────────────────\\\\n\\\\ndef load_dataflow_edges(graph_path: str) -> Dict[str, int]:\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"Load dataflow graph and return {file_key: edge_count}.\\\\\\\"\\\\\\\"\\\\\\\"\\\\n    with open(graph_path) as f:\\\\n        graph = json.load(f)\\\\n    return {k: len(v) for k, v in graph.items()}\\\\n\\\\n\\\\n# ── Val data loading ─────────────────────────────────────────────────\\\\n\\\\ndef load_val_samples(val_path: str, lite: bool = False) -> List[Dict[str, Any]]:\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"Load val JSONL. lite=True skips candidate_tokens (faster for dry-run).\\\\\\\"\\\\\\\"\\\\\\\"\\\\n    import re\\\\n    samples = []\\\\n    pat_qid = re.compile(r'\\\\\\\"query_id\\\\\\\"\\\\\\\\s*:\\\\\\\\s*\\\\\\\"([^\\\\\\\"]+)\\\\\\\"')\\\\n    with open(val_path) as f:\\\\n        for line in f:\\\\n            if not line.strip():\\\\n                continue\\\\n            if lite:\\\\n                m = pat_qid.search(line)\\\\n                if not m:\\\\n                    continue\\\\n                qid = m.group(1)\\\\n                instance_id = qid.split(\\\\\\\"::\\\\\\\")[0] if \\\\\\\"::\\\\\\\" in qid else qid\\\\n                d = json.loads(line)\\\\n                samples.append({\\\\n                    \\\\\\\"query_id\\\\\\\": qid,\\\\n                    \\\\\\\"instance_id\\\\\\\": instance_id,\\\\n                    \\\\\\\"pool_size\\\\\\\": len(d.get(\\\\\\\"neg_candidates\\\\\\\", [])),\\\\n                    \\\\\\\"query_tokens\\\\\\\": d.get(\\\\\\\"query_tokens\\\\\\\", \\\\\\\"\\\\\\\")[:1000],\\\\n                    \\\\\\\"pos_tokens\\\\\\\": d.get(\\\\\\\"pos_tokens\\\\\\\", \\\\\\\"\\\\\\\")[:1000],\\\\n                    \\\\\\\"neg_candidates\\\\\\\": [],\\\\n                    \\\\\\\"candidate_tokens\\\\\\\": {},\\\\n                })\\\\n            else:\\\\n                d = jso\\\\n\\\\n... [截断: 输出过长，省略 4801 字符] ...\\\\n\\\\ned.get(\\\\\\\"scores_top10\\\\\\\") else 0.0,\\\\n            \\\\\\\"total_candidates\\\\\\\": max(len(predicted), sample[\\\\\\\"pool_size\\\\\\\"] + 1),\\\\n        })\\\\n    return results\\\\n\\\\n\\\\n# ── Mock predictions (dry-run) ───────────────────────────────────────\\\\n\\\\ndef mock_predictions(\\\\n    val_samples: List[Dict], strategy: str, seed: int\\\\n) -> List[Dict]:\\\\n    rng = np.random.RandomState(seed + abs(hash(strategy)) % 10000)\\\\n    results = []\\\\n    for sample in val_samples:\\\\n        pool = 1 + sample[\\\\\\\"pool_size\\\\\\\"]\\\\n        if strategy == \\\\\\\"random\\\\\\\":\\\\n            rank = rng.randint(1, pool + 1)\\\\n        elif strategy == \\\\\\\"embedding_distance\\\\\\\":\\\\n            rank = max(1, min(pool, int(rng.exponential(pool * 0.35)) + 1))\\\\n        else:\\\\n            rank = max(1, min(pool, int(rng.exponential(pool * 0.20)) + 1))\\\\n\\\\n        pos_sim = max(0.0, min(1.0, 1.0 - rank / pool + rng.normal(0, 0.08)))\\\\n        tsim = text_similarity(\\\\n            sample[\\\\\\\"query_tokens\\\\\\\"][:500], sample[\\\\\\\"pos_tokens\\\\\\\"][:500]\\\\n        )\\\\n\\\\n        results.append({\\\\n            \\\\\\\"query_id\\\\\\\": sample[\\\\\\\"query_id\\\\\\\"],\\\\n            \\\\\\\"instance_id\\\\\\\": sample[\\\\\\\"instance_id\\\\\\\"],\\\\n            \\\\\\\"pool_size\\\\\\\": sample[\\\\\\\"pool_size\\\\\\\"],\\\\n            \\\\\\\"rank\\\\\\\": rank,\\\\n            \\\\\\\"pos_sim\\\\\\\": pos_sim if pos_sim > 0 else tsim,\\\\n            \\\\\\\"total_candidates\\\\\\\": pool,\\\\n        })\\\\n    return results\\\\n\\\\n\\\\n# ── Metrics computation ──────────────────────────────────────────────\\\\n\\\\ndef compute_metrics(results: List[Dict]) -> Dict[str, float]:\\\\n    if not results:\\\\n        return {\\\\\\\"R@1\\\\\\\": 0.0, \\\\\\\"R@5\\\\\\\": 0.0, \\\\\\\"MRR\\\\\\\": 0.0, \\\\\\\"count\\\\\\\": 0}\\\\n    ranks = [r[\\\\\\\"rank\\\\\\\"] for r in results]\\\\n    n = len(ranks)\\\\n    return {\\\\n        \\\\\\\"R@1\\\\\\\": sum(1 for r in ranks if r <= 1) / n,\\\\n        \\\\\\\"R@5\\\\\\\": sum(1 for r in ranks if r <= 5) / n,\\\\n        \\\\\\\"MRR\\\\\\\": sum(1.0 / r for r in ranks) / n,\\\\n        \\\\\\\"count\\\\\\\": n,\\\\n    }\\\\n\\\\n\\\\ndef _metric_fn(results, metric_name):\\\\n    m = compute_metrics(results)\\\\n    return m[metric_name]\\\\n\\\\n\\\\ndef bootstrap_ci(\\\\n    results: List[Dict],\\\\n    metric_name: str = \\\\\\\"R@1\\\\\\\",\\\\n    n_bootstrap: int = 1000,\\\\n    ci: float = 0.95,\\\\n    seed: int = 42,\\\\n) -> Tuple[float, float, float]:\\\\n    rng = np.random.RandomState(seed)\\\\n    n = len(results)\\\\n    if n == 0:\\\\n        return (0.0, 0.0, 0.0)\\\\n\\\\n    point = _metric_fn(results, metric_name)\\\\n    boot_values = []\\\\n    for _ in range(n_bootstrap):\\\\n        idx = rng.choice(n, n, replace=True)\\\\n        boot_sample = [results[i] for i in idx]\\\\n        boot_values.append(_metric_fn(boot_sample, metric_name))\\\\n\\\\n    alpha = (1 - ci) / 2\\\\n    lo = float(np.percentile(boot_values, alpha * 100))\\\\n    hi = float(np.percentile(boot_values, (1 - alpha) * 100))\\\\n    return (point, lo, hi)\\\\n\\\\n\\\\n# ── Stratification ───────────────────────────────────────────────────\\\\n\\\\ndef assign_strata(\\\\n    results: List[Dict],\\\\n    inst_to_repo: Dict[str, str],\\\\n    repo_counts: Dict[str, int],\\\\n    dataflow_edges: Optional[Dict[str, int]] = None,\\\\n) -> List[Dict]:\\\\n    for r in results:\\\\n        repo = inst_to_repo.get(r[\\\\\\\"instance_id\\\\\\\"], \\\\\\\"\\\\\\\")\\\\n        rc = repo_counts.get(repo, 0)\\\\n        r[\\\\\\\"repo\\\\\\\"] = repo\\\\n        r[\\\\\\\"repo_size\\\\\\\"] = rc\\\\n        r[\\\\\\\"repo_size_bin\\\\\\\"] = _bin_value(rc, REPO_SIZE_BINS)\\\\n        r[\\\\\\\"pool_size_bin\\\\\\\"] = _bin_value(r[\\\\\\\"pool_size\\\\\\\"], POOL_SIZE_BINS)\\\\n        r[\\\\\\\"sim_bin\\\\\\\"] = _bin_value(r[\\\\\\\"pos_sim\\\\\\\"], SIMILARITY_BINS)\\\\n        if dataflow_edges is not None:\\\\n            ec = dataflow_edges.get(r[\\\\\\\"query_id\\\\\\\"], 0)\\\\n            r[\\\\\\\"dataflow_edge_count\\\\\\\"] = ec\\\\n            r[\\\\\\\"dataflow_bin\\\\\\\"] = _bin_value(ec, DATAFLOW_BINS)\\\\n        else:\\\\n            r[\\\\\\\"dataflow_bin\\\\\\\"] = \\\\\\\"unknown\\\\\\\"\\\\n    return results\\\\n\\\\n\\\\ndef assign_neg_difficulty_quartiles(\\\\n    all_results: Dict[str, Dict[int, List[Dict]]],\\\\n    val_samples_cache: Dict[str, List[Dict]],\\\\n):\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"Compute text-overlap-based neg difficulty proxy and assign quartiles.\\\\\\\"\\\\\\\"\\\\\\\"\\\\n    for strategy in list(all_results.keys()):\\\\n        for seed in list(all_results[strategy].keys()):\\\\n            results = all_results[strategy][seed]\\\\n            cache_key = f\\\\\\\"{strategy}_s{seed}\\\\\\\"\\\\n            samples = val_samples_cache.get(cache_key, [])\\\\n            sample_map = {s[\\\\\\\"query_id\\\\\\\"]: s for s in samples}\\\\n\\\\n            margins = []\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.41}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n\\\"\\\"\\\"Stratified analysis of embedding vs random negative strategies by data strata.\\n\\nAnalyses M2 per-instance predictions across:\\n  - Repo size (instance count per repo from M1)\\n  - Candidate pool size (neg_candidates per query)\\n  - Query-positive similarity (cosine sim from model, or text overlap for dry-run)\\n\\nInputs:\\n  - M2 per-instance predictions (from --predictions-dir or re-eval from checkpoints)\\n  - M1 all.jsonl (repo metadata)\\n  - Val JSONL files (query/candidate structure)\\n\\nOutputs:\\n  - stratified_results.json: full per-stratum metrics with bootstrap CI\\n  - stratified_summary.csv: compact table\\n  - stratified_plots.pdf: grouped bar charts, heatmaps, delta trends\\n\\\"\\\"\\\"\\n\\nimport argparse\\nimport csv\\nimport json\\nimport math\\nimport os\\nimport sys\\nfrom collections import Counter, defaultdict\\nfrom pathlib import Path\\nfrom typing import Any, Dict, List, Optional, Tuple\\n\\nimport numpy as np\\n\\nSTRATEGIES = [\\\"random\\\", \\\"embedding_distance\\\", \\\"dataflow_aware\\\"]\\nSTRATEGY_LABELS = {\\\"random\\\": \\\"Random\\\", \\\"embedding_distance\\\": \\\"Embedding\\\", \\\"dataflow_aware\\\": \\\"Dataflow\\\"}\\nSTRATEGY_COLORS = {\\\"random\\\": \\\"#4C72B0\\\", \\\"embedding_distance\\\": \\\"#DD8452\\\", \\\"dataflow_aware\\\": \\\"#55A868\\\"}\\n\\nREPO_SIZE_BINS = {\\n    \\\"small\\\": (0, 50),\\n    \\\"medium\\\": (50, 200),\\n    \\\"large\\\": (200, 500),\\n    \\\"xlarge\\\": (500, float(\\\"inf\\\")),\\n}\\n\\nPOOL_SIZE_BINS = {\\n    \\\"small\\\": (0, 20),\\n    \\\"medium\\\": (20, 40),\\n    \\\"large\\\": (40, 51),\\n}\\n\\nSIMILARITY_BINS = {\\n    \\\"low\\\": (0.0, 0.3),\\n    \\\"medium\\\": (0.3, 0.6),\\n    \\\"high\\\": (0.6, 1.01),\\n}\\n\\nDATAFLOW_BINS = {\\n    \\\"sparse\\\": (0, 2),\\n    \\\"moderate\\\": (2, 10),\\n    \\\"rich\\\": (10, float(\\\"inf\\\")),\\n}\\n\\nNEG_DIFFICULTY_QUARTILE_LABELS = [\\\"Q1_easy\\\", \\\"Q2\\\", \\\"Q3\\\", \\\"Q4_hard\\\"]\\n\\n\\ndef _bin_value(value, bins):\\n    for name, (lo, hi) in bins.items():\\n        if lo <= value < hi:\\n            return name\\n    return \\\"unknown\\\"\\n\\n\\n# ── M1 metadata ───────────────────────────────────────────────────��─\\n\\ndef load_m1_metadata(m1_path: str) -> Tuple[Dict[str, str], Dict[str, int]]:\\n    import re\\n    inst_to_repo = {}\\n    repo_counts: Counter = Counter()\\n    pat_iid = re.compile(r'\\\"instance_id\\\"\\\\s*:\\\\s*\\\"([^\\\"]+)\\\"')\\n    pat_repo = re.compile(r'\\\"repo\\\"\\\\s*:\\\\s*\\\"([^\\\"]+)\\\"')\\n    with open(m1_path) as f:\\n        for line in f:\\n            m_iid = pat_iid.search(line)\\n            m_repo = pat_repo.search(line)\\n            if m_iid and m_repo:\\n                iid = m_iid.group(1)\\n                repo = m_repo.group(1)\\n                inst_to_repo[iid] = repo\\n                repo_counts[repo] += 1\\n    return inst_to_repo, dict(repo_counts)\\n\\n\\n# ── Dataflow graph loading ────────────────────────────────────────────\\n\\ndef load_dataflow_edges(graph_path: str) -> Dict[str, int]:\\n    \\\"\\\"\\\"Load dataflow graph and return {file_key: edge_count}.\\\"\\\"\\\"\\n    with open(graph_path) as f:\\n        graph = json.load(f)\\n    return {k: len(v) for k, v in graph.items()}\\n\\n\\n# ── Val data loading ─────────────────────────────────────────────────\\n\\ndef load_val_samples(val_path: str, lite: bool = False) -> List[Dict[str, Any]]:\\n    \\\"\\\"\\\"Load val JSONL. lite=True skips candidate_tokens (faster for dry-run).\\\"\\\"\\\"\\n    import re\\n    samples = []\\n    pat_qid = re.compile(r'\\\"query_id\\\"\\\\s*:\\\\s*\\\"([^\\\"]+)\\\"')\\n    with open(val_path) as f:\\n        for line in f:\\n            if not line.strip():\\n                continue\\n            if lite:\\n                m = pat_qid.search(line)\\n                if not m:\\n                    continue\\n                qid = m.group(1)\\n                instance_id = qid.split(\\\"::\\\")[0] if \\\"::\\\" in qid else qid\\n                d = json.loads(line)\\n                samples.append({\\n                    \\\"query_id\\\": qid,\\n                    \\\"instance_id\\\": instance_id,\\n                    \\\"pool_size\\\": len(d.get(\\\"neg_candidates\\\", [])),\\n                    \\\"query_tokens\\\": d.get(\\\"query_tokens\\\", \\\"\\\")[:1000],\\n                    \\\"pos_tokens\\\": d.get(\\\"pos_tokens\\\", \\\"\\\")[:1000],\\n                    \\\"neg_candidates\\\": [],\\n                    \\\"candidate_tokens\\\": {},\\n                })\\n            else:\\n                d = jso\\n\\n... [截断: 输出过长，省略 4801 字符] ...\\n\\ned.get(\\\"scores_top10\\\") else 0.0,\\n            \\\"total_candidates\\\": max(len(predicted), sample[\\\"pool_size\\\"] + 1),\\n        })\\n    return results\\n\\n\\n# ── Mock predictions (dry-run) ───────────────────────────────────────\\n\\ndef mock_predictions(\\n    val_samples: List[Dict], strategy: str, seed: int\\n) -> List[Dict]:\\n    rng = np.random.RandomState(seed + abs(hash(strategy)) % 10000)\\n    results = []\\n    for sample in val_samples:\\n        pool = 1 + sample[\\\"pool_size\\\"]\\n        if strategy == \\\"random\\\":\\n            rank = rng.randint(1, pool + 1)\\n        elif strategy == \\\"embedding_distance\\\":\\n            rank = max(1, min(pool, int(rng.exponential(pool * 0.35)) + 1))\\n        else:\\n            rank = max(1, min(pool, int(rng.exponential(pool * 0.20)) + 1))\\n\\n        pos_sim = max(0.0, min(1.0, 1.0 - rank / pool + rng.normal(0, 0.08)))\\n        tsim = text_similarity(\\n            sample[\\\"query_tokens\\\"][:500], sample[\\\"pos_tokens\\\"][:500]\\n        )\\n\\n        results.append({\\n            \\\"query_id\\\": sample[\\\"query_id\\\"],\\n            \\\"instance_id\\\": sample[\\\"instance_id\\\"],\\n            \\\"pool_size\\\": sample[\\\"pool_size\\\"],\\n            \\\"rank\\\": rank,\\n            \\\"pos_sim\\\": pos_sim if pos_sim > 0 else tsim,\\n            \\\"total_candidates\\\": pool,\\n        })\\n    return results\\n\\n\\n# ── Metrics computation ──────────────────────────────────────────────\\n\\ndef compute_metrics(results: List[Dict]) -> Dict[str, float]:\\n    if not results:\\n        return {\\\"R@1\\\": 0.0, \\\"R@5\\\": 0.0, \\\"MRR\\\": 0.0, \\\"count\\\": 0}\\n    ranks = [r[\\\"rank\\\"] for r in results]\\n    n = len(ranks)\\n    return {\\n        \\\"R@1\\\": sum(1 for r in ranks if r <= 1) / n,\\n        \\\"R@5\\\": sum(1 for r in ranks if r <= 5) / n,\\n        \\\"MRR\\\": sum(1.0 / r for r in ranks) / n,\\n        \\\"count\\\": n,\\n    }\\n\\n\\ndef _metric_fn(results, metric_name):\\n    m = compute_metrics(results)\\n    return m[metric_name]\\n\\n\\ndef bootstrap_ci(\\n    results: List[Dict],\\n    metric_name: str = \\\"R@1\\\",\\n    n_bootstrap: int = 1000,\\n    ci: float = 0.95,\\n    seed: int = 42,\\n) -> Tuple[float, float, float]:\\n    rng = np.random.RandomState(seed)\\n    n = len(results)\\n    if n == 0:\\n        return (0.0, 0.0, 0.0)\\n\\n    point = _metric_fn(results, metric_name)\\n    boot_values = []\\n    for _ in range(n_bootstrap):\\n        idx = rng.choice(n, n, replace=True)\\n        boot_sample = [results[i] for i in idx]\\n        boot_values.append(_metric_fn(boot_sample, metric_name))\\n\\n    alpha = (1 - ci) / 2\\n    lo = float(np.percentile(boot_values, alpha * 100))\\n    hi = float(np.percentile(boot_values, (1 - alpha) * 100))\\n    return (point, lo, hi)\\n\\n\\n# ── Stratification ───────────────────────────────────────────────────\\n\\ndef assign_strata(\\n    results: List[Dict],\\n    inst_to_repo: Dict[str, str],\\n    repo_counts: Dict[str, int],\\n    dataflow_edges: Optional[Dict[str, int]] = None,\\n) -> List[Dict]:\\n    for r in results:\\n        repo = inst_to_repo.get(r[\\\"instance_id\\\"], \\\"\\\")\\n        rc = repo_counts.get(repo, 0)\\n        r[\\\"repo\\\"] = repo\\n        r[\\\"repo_size\\\"] = rc\\n        r[\\\"repo_size_bin\\\"] = _bin_value(rc, REPO_SIZE_BINS)\\n        r[\\\"pool_size_bin\\\"] = _bin_value(r[\\\"pool_size\\\"], POOL_SIZE_BINS)\\n        r[\\\"sim_bin\\\"] = _bin_value(r[\\\"pos_sim\\\"], SIMILARITY_BINS)\\n        if dataflow_edges is not None:\\n            ec = dataflow_edges.get(r[\\\"query_id\\\"], 0)\\n            r[\\\"dataflow_edge_count\\\"] = ec\\n            r[\\\"dataflow_bin\\\"] = _bin_value(ec, DATAFLOW_BINS)\\n        else:\\n            r[\\\"dataflow_bin\\\"] = \\\"unknown\\\"\\n    return results\\n\\n\\ndef assign_neg_difficulty_quartiles(\\n    all_results: Dict[str, Dict[int, List[Dict]]],\\n    val_samples_cache: Dict[str, List[Dict]],\\n):\\n    \\\"\\\"\\\"Compute text-overlap-based neg difficulty proxy and assign quartiles.\\\"\\\"\\\"\\n    for strategy in list(all_results.keys()):\\n        for seed in list(all_results[strategy].keys()):\\n            results = all_results[strategy][seed]\\n            cache_key = f\\\"{strategy}_s{seed}\\\"\\n            samples = val_samples_cache.get(cache_key, [])\\n            sample_map = {s[\\\"query_id\\\"]: s for s in samples}\\n\\n            margins = []\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.41}}"
    }
  },
  "sourceToolAssistantUUID": "b76c2ae9-541d-4870-aaa5-90aafe06146b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "bda3dfbf-4b90-494d-b674-2597173fd381",
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
  "leafUuid": "a8729d8c-d15a-4932-abe3-89da32dd2b29",
  "sessionId": "bda3dfbf-4b90-494d-b674-2597173fd381"
}
```

---

### Runtime record

_source line 43_

```json
{
  "type": "ai-title",
  "aiTitle": "Add pool-size controlled stratified evaluation to analysis script",
  "sessionId": "bda3dfbf-4b90-494d-b674-2597173fd381"
}
```

---

### Assistant

_source line 44 · 2026-05-14T20:47:20.671Z_

<details><summary>Logged reasoning block</summary>

```text
I'm getting truncated outputs. Let me try reading the middle section with `sed -n` or specific line ranges. Actually, ssh_read_only doesn't support pipes and shell metacharacters. Let me use `head` and `tail` in a different way.

Actually, looking at this more carefully, the ssh_read_only tool blocks `|` and other shell metacharacters. So I can't do `sed -n '200,400p'` or `tail -n +200 | head -200`.

Let me try reading ranges using `head -n` and focusing on what I haven't seen yet. I have:


- Lines 1-200 (first read)
- Lines 200-380 (the last read showed up to mock_predictions, metrics, stratification, assign_neg_difficulty_quartiles start)
- Lines 380-end (showed the rest of assign_neg_difficulty_quartiles, group_by, run_stratified_analysis, and then truncated at make_plots, then jumped to main)

The key sections I'm still missing are:
1. Lines ~200-290 (reeval_checkpoint end, and the functions between it and mock_predictions)
2. Lines ~490-700 (make_plots body, write_summary_csv, and anything between)

Let me try a different approach to read those missing sections.

I realize the ssh_read_only tool is truncating the output because the file is too long. I need to extract specific line ranges instead of reading the whole thing. Let me try using `head -n 300` combined with `tail -n +201` to get lines 201-300, though I'm not sure if pipes work with ssh_read_only. If not, I could use `awk` to print specific line ranges, but that might not be in the whitelist either. Let me test what tools are available.

Actually, I have enough context already to understand the overall structure. I should focus on the key functions I'm missing: the full body of `make_plots`, the `write_summary_csv` function, the complete `main` function, and any helper functions in between. I also want to see what `load_predictions` does since it's referenced in main. Let me try using grep to locate these function definitions and their line numbers so I can target my reads more efficiently.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a8729d8c-d15a-4932-abe3-89da32dd2b29",
  "isSidechain": false,
  "requestId": "req_011Cb37jPvWVUDbk4exrg1kB",
  "type": "assistant",
  "uuid": "6b512878-3425-406c-bf28-8e38ff843fe1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "bda3dfbf-4b90-494d-b674-2597173fd381",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RQPnMvyHJ7Hq4Di89iGKMG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3954,
      "cache_read_input_tokens": 42203,
      "output_tokens": 833,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3954,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 833,
          "cache_read_input_tokens": 42203,
          "cache_creation_input_tokens": 3954,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3954
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

_source line 45 · 2026-05-14T20:47:20.674Z_

Let me get the function structure and the sections I'm missing.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6b512878-3425-406c-bf28-8e38ff843fe1",
  "isSidechain": false,
  "requestId": "req_011Cb37jPvWVUDbk4exrg1kB",
  "type": "assistant",
  "uuid": "12600aea-db7a-4eee-b55a-9abedbfba249",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "bda3dfbf-4b90-494d-b674-2597173fd381",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RQPnMvyHJ7Hq4Di89iGKMG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3954,
      "cache_read_input_tokens": 42203,
      "output_tokens": 833,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3954,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 833,
          "cache_read_input_tokens": 42203,
          "cache_creation_input_tokens": 3954,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3954
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

_source line 46 · 2026-05-14T20:47:20.775Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01QVsZJYwomhEf574wq8qwBE`</summary>

```json
{
  "server": "bjb1-42106",
  "command": "grep -n \"^def \\|^class \" /root/structfuse/evaluation/analyze_stratified.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "12600aea-db7a-4eee-b55a-9abedbfba249",
  "isSidechain": false,
  "requestId": "req_011Cb37jPvWVUDbk4exrg1kB",
  "type": "assistant",
  "uuid": "a92d068c-fa00-4432-8498-d8065f51fed5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "bda3dfbf-4b90-494d-b674-2597173fd381",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RQPnMvyHJ7Hq4Di89iGKMG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3954,
      "cache_read_input_tokens": 42203,
      "output_tokens": 833,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3954,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 833,
          "cache_read_input_tokens": 42203,
          "cache_creation_input_tokens": 3954,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3954
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

_source line 47 · 2026-05-14T20:47:20.794Z_

<details><summary>↩ Tool result · `toolu_01QVsZJYwomhEf574wq8qwBE`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a92d068c-fa00-4432-8498-d8065f51fed5",
  "isSidechain": false,
  "promptId": "22ffd1fb-240e-481f-9bcc-b3f6a42d6805",
  "type": "user",
  "uuid": "233e403e-2b7f-41e1-9c1c-c5a89e6f120e",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\\\", \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "a92d068c-fa00-4432-8498-d8065f51fed5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "bda3dfbf-4b90-494d-b674-2597173fd381",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 48 · 2026-05-14T20:47:23.715Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_014TBxGLaRkYvRhD1124wqxX`</summary>

```json
{
  "server": "bjb1-42106",
  "command": "grep -n \"^def \" /root/structfuse/evaluation/analyze_stratified.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "233e403e-2b7f-41e1-9c1c-c5a89e6f120e",
  "isSidechain": false,
  "requestId": "req_011Cb37kn2p4ox8wFA4TscoN",
  "type": "assistant",
  "uuid": "553fcb92-ad83-4ead-a38b-b080abe29300",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "bda3dfbf-4b90-494d-b674-2597173fd381",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UPuYXqoiYiD964ZJsAau1x",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 926,
      "cache_read_input_tokens": 46157,
      "output_tokens": 124,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 926,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 124,
          "cache_read_input_tokens": 46157,
          "cache_creation_input_tokens": 926,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 926
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

_source line 49 · 2026-05-14T20:47:24.077Z_

<details><summary>↩ Tool result · `toolu_014TBxGLaRkYvRhD1124wqxX`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"64:def _bin_value(value, bins):\\n73:def load_m1_metadata(m1_path: str) -> Tuple[Dict[str, str], Dict[str, int]]:\\n93:def load_dataflow_edges(graph_path: str) -> Dict[str, int]:\\n102:def load_val_samples(val_path: str, lite: bool = False) -> List[Dict[str, Any]]:\\n143:def text_similarity(a: str, b: str) -> float:\\n154:def reeval_checkpoint(\\n230:def load_predictions(pred_file: str, val_samples: List[Dict]) -> List[Dict]:\\n268:def mock_predictions(\\n300:def compute_metrics(results: List[Dict]) -> Dict[str, float]:\\n313:def _metric_fn(results, metric_name):\\n318:def bootstrap_ci(\\n345:def assign_strata(\\n368:def assign_neg_difficulty_quartiles(\\n416:def group_by(results: List[Dict], key: str) -> Dict[str, List[Dict]]:\\n425:def run_stratified_analysis(\\n474:def make_plots(\\n649:def write_summary_csv(\\n713:def main():\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "553fcb92-ad83-4ead-a38b-b080abe29300",
  "isSidechain": false,
  "promptId": "22ffd1fb-240e-481f-9bcc-b3f6a42d6805",
  "type": "user",
  "uuid": "eecdd111-8e37-42b3-87d0-05d44eaf5aa7",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"64:def _bin_value(value, bins):\\\\n73:def load_m1_metadata(m1_path: str) -> Tuple[Dict[str, str], Dict[str, int]]:\\\\n93:def load_dataflow_edges(graph_path: str) -> Dict[str, int]:\\\\n102:def load_val_samples(val_path: str, lite: bool = False) -> List[Dict[str, Any]]:\\\\n143:def text_similarity(a: str, b: str) -> float:\\\\n154:def reeval_checkpoint(\\\\n230:def load_predictions(pred_file: str, val_samples: List[Dict]) -> List[Dict]:\\\\n268:def mock_predictions(\\\\n300:def compute_metrics(results: List[Dict]) -> Dict[str, float]:\\\\n313:def _metric_fn(results, metric_name):\\\\n318:def bootstrap_ci(\\\\n345:def assign_strata(\\\\n368:def assign_neg_difficulty_quartiles(\\\\n416:def group_by(results: List[Dict], key: str) -> Dict[str, List[Dict]]:\\\\n425:def run_stratified_analysis(\\\\n474:def make_plots(\\\\n649:def write_summary_csv(\\\\n713:def main():\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.35}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"64:def _bin_value(value, bins):\\n73:def load_m1_metadata(m1_path: str) -> Tuple[Dict[str, str], Dict[str, int]]:\\n93:def load_dataflow_edges(graph_path: str) -> Dict[str, int]:\\n102:def load_val_samples(val_path: str, lite: bool = False) -> List[Dict[str, Any]]:\\n143:def text_similarity(a: str, b: str) -> float:\\n154:def reeval_checkpoint(\\n230:def load_predictions(pred_file: str, val_samples: List[Dict]) -> List[Dict]:\\n268:def mock_predictions(\\n300:def compute_metrics(results: List[Dict]) -> Dict[str, float]:\\n313:def _metric_fn(results, metric_name):\\n318:def bootstrap_ci(\\n345:def assign_strata(\\n368:def assign_neg_difficulty_quartiles(\\n416:def group_by(results: List[Dict], key: str) -> Dict[str, List[Dict]]:\\n425:def run_stratified_analysis(\\n474:def make_plots(\\n649:def write_summary_csv(\\n713:def main():\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"
    }
  },
  "sourceToolAssistantUUID": "553fcb92-ad83-4ead-a38b-b080abe29300",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "bda3dfbf-4b90-494d-b674-2597173fd381",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 50 · 2026-05-14T20:47:28.278Z_

<details><summary>Logged reasoning block</summary>

```text
Now I know the function structure. The key sections I need to read are:
1. Lines 230-268: `load_predictions` function
2. Lines 474-649: `make_plots` function  
3. Lines 649-713: `write_summary_csv` function
4. Lines 713-910: `main` function

I already have good coverage of lines 1-470 and lines 830-910. Let me read the gaps.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "eecdd111-8e37-42b3-87d0-05d44eaf5aa7",
  "isSidechain": false,
  "requestId": "req_011Cb37m21CbhBuyETUV687V",
  "type": "assistant",
  "uuid": "c2217a9d-d8af-483e-b237-a6a36c7f30da",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "bda3dfbf-4b90-494d-b674-2597173fd381",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Pd7VuAaRYK2UcwpCVvve7h",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 507,
      "cache_read_input_tokens": 47083,
      "output_tokens": 241,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 507,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 241,
          "cache_read_input_tokens": 47083,
          "cache_creation_input_tokens": 507,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 507
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

_source line 51 · 2026-05-14T20:47:28.761Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01GM1fC2Uiz1yZsShSnp1XYh`</summary>

```json
{
  "server": "bjb1-42106",
  "command": "tail -n +474 /root/structfuse/evaluation/analyze_stratified.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c2217a9d-d8af-483e-b237-a6a36c7f30da",
  "isSidechain": false,
  "requestId": "req_011Cb37m21CbhBuyETUV687V",
  "type": "assistant",
  "uuid": "d371b5f1-7af6-4eb8-a09d-16488ec221be",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "bda3dfbf-4b90-494d-b674-2597173fd381",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Pd7VuAaRYK2UcwpCVvve7h",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 507,
      "cache_read_input_tokens": 47083,
      "output_tokens": 241,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 507,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 241,
          "cache_read_input_tokens": 47083,
          "cache_creation_input_tokens": 507,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 507
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

_source line 52 · 2026-05-14T20:47:29.171Z_

<details><summary>↩ Tool result · `toolu_01GM1fC2Uiz1yZsShSnp1XYh`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"def make_plots(\\n    repo_analysis: Dict,\\n    pool_analysis: Dict,\\n    sim_analysis: Dict,\\n    output_dir: str,\\n    dataflow_analysis: Optional[Dict] = None,\\n    neg_diff_analysis: Optional[Dict] = None,\\n):\\n    import matplotlib\\n    matplotlib.use(\\\"Agg\\\")\\n    import matplotlib.pyplot as plt\\n    from matplotlib.backends.backend_pdf import PdfPages\\n\\n    plt.rcParams.update({\\n        \\\"font.size\\\": 11,\\n        \\\"axes.titlesize\\\": 13,\\n        \\\"axes.labelsize\\\": 12,\\n        \\\"xtick.labelsize\\\": 10,\\n        \\\"ytick.labelsize\\\": 10,\\n        \\\"legend.fontsize\\\": 10,\\n        \\\"figure.dpi\\\": 150,\\n        \\\"savefig.dpi\\\": 300,\\n        \\\"font.family\\\": \\\"sans-serif\\\",\\n    })\\n\\n    pdf_path = os.path.join(output_dir, \\\"stratified_plots.pdf\\\")\\n    with PdfPages(pdf_path) as pdf:\\n        # ── Plot 1: Grouped bar chart per stratum dimension ──\\n        plot_dims = [\\n            (\\\"Repo Size\\\", repo_analysis, list(REPO_SIZE_BINS.keys())),\\n            (\\\"Candidate Pool Size\\\", pool_analysis, list(POOL_SIZE_BINS.keys())),\\n            (\\\"Query-Positive Similarity\\\", sim_analysis, list(SIMILARITY_BINS.keys())),\\n        ]\\n        if dataflow_analysis:\\n            plot_dims.append((\\\"Dataflow Availability\\\", dataflow_analysis, list(DATAFLOW_BINS.keys())))\\n        if neg_diff_analysis:\\n            plot_dims.append((\\\"Neg Difficulty Quartile\\\", neg_diff_analysis, NEG_DIFFICULTY_QUARTILE_LABELS))\\n        for title, analysis, bin_order in plot_dims:\\n            bins_present = [b for b in bin_order if b in analysis]\\n            if not bins_present:\\n                continue\\n\\n            fig, axes = plt.subplots(1, 3, figsize=(15, 5))\\n            fig.suptitle(f\\\"Stratified by {title}\\\", fontweight=\\\"bold\\\", y=1.02)\\n\\n            for ax_idx, metric in enumerate([\\\"R@1\\\", \\\"R@5\\\", \\\"MRR\\\"]):\\n                ax = axes[ax_idx]\\n                x = np.arange(len(bins_present))\\n                width = 0.25\\n\\n                for i, strategy in enumerate(STRATEGIES):\\n                    vals = []\\n                    errs_lo = []\\n                    errs_hi = []\\n                    for b in bins_present:\\n                        m = analysis[b].get(strategy, {})\\n                        v = m.get(metric, 0)\\n                        ci = m.get(f\\\"{metric}_ci\\\", [v, v])\\n                        vals.append(v)\\n                        errs_lo.append(v - ci[0])\\n                        errs_hi.append(ci[1] - v)\\n\\n                    offset = (i - 1) * width\\n                    bars = ax.bar(\\n                        x + offset, vals, width,\\n                        label=STRATEGY_LABELS[strategy],\\n                        color=STRATEGY_COLORS[strategy],\\n                        yerr=[errs_lo, errs_hi],\\n                        capsize=3, alpha=0.85,\\n                    )\\n\\n                ax.set_xlabel(title)\\n                ax.set_ylabel(metric)\\n                ax.set_title(metric)\\n                ax.set_xticks(x)\\n                ax.set_xticklabels(bins_present, rotation=0)\\n                ax.legend(loc=\\\"best\\\")\\n                ax.set_ylim(bottom=0)\\n\\n            plt.tight_layout()\\n            pdf.savefig(fig, bbox_inches=\\\"tight\\\")\\n            plt.close(fig)\\n\\n        # ── Plot 2: Heatmap — stratum × strategy for R@1 ──\\n        heatmap_dims = [\\n            (\\\"Repo Size\\\", repo_analysis, list(REPO_SIZE_BINS.keys())),\\n            (\\\"Pool Size\\\", pool_analysis, list(POOL_SIZE_BINS.keys())),\\n            (\\\"Similarity\\\", sim_analysis, list(SIMILARITY_BINS.keys())),\\n        ]\\n        if dataflow_analysis:\\n            heatmap_dims.append((\\\"Dataflow\\\", dataflow_analysis, list(DATAFLOW_BINS.keys())))\\n        if neg_diff_analysis:\\n            heatmap_dims.append((\\\"Neg Difficulty\\\", neg_diff_analysis, NEG_DIFFICULTY_QUARTILE_LABELS))\\n        for title, analysis, bin_order in heatmap_dims:\\n            bins_present = [b for b in bin_order if b in analysis]\\n            if not bins_present:\\n                continue\\n\\n            data_matrix = []\\n            for b in bins_present:\\n                row = []\\n                for s in STRATEGIES:\\n               \\n\\n... [截断: 输出过长，省略 10875 字符] ...\\n\\nt\\\")):\\n                        ckpt_dir = candidate\\n                        break\\n                if ckpt_dir is None and os.path.exists(os.path.join(base, \\\"model.pt\\\")):\\n                    ckpt_dir = base\\n                if os.path.exists(ckpt_dir):\\n                    print(f\\\"  Re-evaluating checkpoint: {ckpt_dir}\\\", flush=True)\\n                    results = reeval_checkpoint(\\n                        ckpt_dir, val_samples, args.device, args.max_seq_length\\n                    )\\n                else:\\n                    print(f\\\"  [WARN] Checkpoint not found: {ckpt_dir}\\\", flush=True)\\n                    continue\\n            else:\\n                print(\\\"  [ERROR] No --dry-run, --predictions-dir, or --checkpoints-dir\\\", flush=True)\\n                continue\\n\\n            # Assign strata\\n            results = assign_strata(results, inst_to_repo, repo_counts, dataflow_edges)\\n\\n            # For dry-run or model-based: compute text similarity for sim_bin\\n            if args.dry_run:\\n                for r, s in zip(results, val_samples):\\n                    tsim = text_similarity(s[\\\"query_tokens\\\"][:500], s[\\\"pos_tokens\\\"][:500])\\n                    r[\\\"sim_bin\\\"] = _bin_value(tsim, SIMILARITY_BINS)\\n\\n            all_results[strategy][seed] = results\\n            val_samples_cache[f\\\"{strategy}_s{seed}\\\"] = val_samples\\n            print(f\\\"  -> {len(results)} instances\\\", flush=True)\\n\\n    # Compute neg_difficulty quartiles (text-overlap proxy, CPU-safe)\\n    print(\\\"Computing neg difficulty quartiles...\\\", flush=True)\\n    assign_neg_difficulty_quartiles(all_results, val_samples_cache)\\n\\n    # Run stratified analysis\\n    print(\\\"\\\\nRunning stratified analysis...\\\", flush=True)\\n    repo_analysis = run_stratified_analysis(\\n        all_results, \\\"repo_size_bin\\\", list(REPO_SIZE_BINS.keys()), args.n_bootstrap\\n    )\\n    pool_analysis = run_stratified_analysis(\\n        all_results, \\\"pool_size_bin\\\", list(POOL_SIZE_BINS.keys()), args.n_bootstrap\\n    )\\n    sim_analysis = run_stratified_analysis(\\n        all_results, \\\"sim_bin\\\", list(SIMILARITY_BINS.keys()), args.n_bootstrap\\n    )\\n\\n    dataflow_analysis = {}\\n    if dataflow_edges is not None:\\n        dataflow_analysis = run_stratified_analysis(\\n            all_results, \\\"dataflow_bin\\\", list(DATAFLOW_BINS.keys()), args.n_bootstrap\\n        )\\n\\n    neg_diff_analysis = run_stratified_analysis(\\n        all_results, \\\"neg_difficulty_bin\\\", NEG_DIFFICULTY_QUARTILE_LABELS, args.n_bootstrap\\n    )\\n\\n    # Save JSON\\n    full_results = {\\n        \\\"config\\\": {\\n            \\\"strategies\\\": STRATEGIES,\\n            \\\"seeds\\\": seeds,\\n            \\\"repo_size_bins\\\": {k: list(v) for k, v in REPO_SIZE_BINS.items()},\\n            \\\"pool_size_bins\\\": {k: list(v) for k, v in POOL_SIZE_BINS.items()},\\n            \\\"similarity_bins\\\": {k: list(v) for k, v in SIMILARITY_BINS.items()},\\n            \\\"dataflow_bins\\\": {k: list(v) for k, v in DATAFLOW_BINS.items()},\\n            \\\"neg_difficulty_quartiles\\\": NEG_DIFFICULTY_QUARTILE_LABELS,\\n            \\\"n_bootstrap\\\": args.n_bootstrap,\\n            \\\"dry_run\\\": args.dry_run,\\n        },\\n        \\\"by_repo_size\\\": repo_analysis,\\n        \\\"by_pool_size\\\": pool_analysis,\\n        \\\"by_similarity\\\": sim_analysis,\\n        \\\"by_dataflow\\\": dataflow_analysis,\\n        \\\"by_neg_difficulty\\\": neg_diff_analysis,\\n    }\\n\\n    json_path = os.path.join(args.output_dir, \\\"stratified_results.json\\\")\\n    with open(json_path, \\\"w\\\") as f:\\n        json.dump(full_results, f, indent=2, ensure_ascii=False)\\n    print(f\\\"  Results JSON saved to {json_path}\\\", flush=True)\\n\\n    # CSV summary\\n    csv_path = os.path.join(args.output_dir, \\\"stratified_summary.csv\\\")\\n    write_summary_csv(repo_analysis, pool_analysis, sim_analysis, csv_path, dataflow_analysis, neg_diff_analysis)\\n\\n    # Plots\\n    try:\\n        make_plots(repo_analysis, pool_analysis, sim_analysis, args.output_dir, dataflow_analysis, neg_diff_analysis)\\n    except Exception as e:\\n        print(f\\\"  [WARN] Plot generation failed: {e}\\\", flush=True)\\n\\n    print(\\\"\\\\nDone.\\\", flush=True)\\n\\n\\nif __name__ == \\\"__main__\\\":\\n    main()\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d371b5f1-7af6-4eb8-a09d-16488ec221be",
  "isSidechain": false,
  "promptId": "22ffd1fb-240e-481f-9bcc-b3f6a42d6805",
  "type": "user",
  "uuid": "5868264b-e384-4f80-83ce-93260dd5f77f",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"def make_plots(\\\\n    repo_analysis: Dict,\\\\n    pool_analysis: Dict,\\\\n    sim_analysis: Dict,\\\\n    output_dir: str,\\\\n    dataflow_analysis: Optional[Dict] = None,\\\\n    neg_diff_analysis: Optional[Dict] = None,\\\\n):\\\\n    import matplotlib\\\\n    matplotlib.use(\\\\\\\"Agg\\\\\\\")\\\\n    import matplotlib.pyplot as plt\\\\n    from matplotlib.backends.backend_pdf import PdfPages\\\\n\\\\n    plt.rcParams.update({\\\\n        \\\\\\\"font.size\\\\\\\": 11,\\\\n        \\\\\\\"axes.titlesize\\\\\\\": 13,\\\\n        \\\\\\\"axes.labelsize\\\\\\\": 12,\\\\n        \\\\\\\"xtick.labelsize\\\\\\\": 10,\\\\n        \\\\\\\"ytick.labelsize\\\\\\\": 10,\\\\n        \\\\\\\"legend.fontsize\\\\\\\": 10,\\\\n        \\\\\\\"figure.dpi\\\\\\\": 150,\\\\n        \\\\\\\"savefig.dpi\\\\\\\": 300,\\\\n        \\\\\\\"font.family\\\\\\\": \\\\\\\"sans-serif\\\\\\\",\\\\n    })\\\\n\\\\n    pdf_path = os.path.join(output_dir, \\\\\\\"stratified_plots.pdf\\\\\\\")\\\\n    with PdfPages(pdf_path) as pdf:\\\\n        # ── Plot 1: Grouped bar chart per stratum dimension ──\\\\n        plot_dims = [\\\\n            (\\\\\\\"Repo Size\\\\\\\", repo_analysis, list(REPO_SIZE_BINS.keys())),\\\\n            (\\\\\\\"Candidate Pool Size\\\\\\\", pool_analysis, list(POOL_SIZE_BINS.keys())),\\\\n            (\\\\\\\"Query-Positive Similarity\\\\\\\", sim_analysis, list(SIMILARITY_BINS.keys())),\\\\n        ]\\\\n        if dataflow_analysis:\\\\n            plot_dims.append((\\\\\\\"Dataflow Availability\\\\\\\", dataflow_analysis, list(DATAFLOW_BINS.keys())))\\\\n        if neg_diff_analysis:\\\\n            plot_dims.append((\\\\\\\"Neg Difficulty Quartile\\\\\\\", neg_diff_analysis, NEG_DIFFICULTY_QUARTILE_LABELS))\\\\n        for title, analysis, bin_order in plot_dims:\\\\n            bins_present = [b for b in bin_order if b in analysis]\\\\n            if not bins_present:\\\\n                continue\\\\n\\\\n            fig, axes = plt.subplots(1, 3, figsize=(15, 5))\\\\n            fig.suptitle(f\\\\\\\"Stratified by {title}\\\\\\\", fontweight=\\\\\\\"bold\\\\\\\", y=1.02)\\\\n\\\\n            for ax_idx, metric in enumerate([\\\\\\\"R@1\\\\\\\", \\\\\\\"R@5\\\\\\\", \\\\\\\"MRR\\\\\\\"]):\\\\n                ax = axes[ax_idx]\\\\n                x = np.arange(len(bins_present))\\\\n                width = 0.25\\\\n\\\\n                for i, strategy in enumerate(STRATEGIES):\\\\n                    vals = []\\\\n                    errs_lo = []\\\\n                    errs_hi = []\\\\n                    for b in bins_present:\\\\n                        m = analysis[b].get(strategy, {})\\\\n                        v = m.get(metric, 0)\\\\n                        ci = m.get(f\\\\\\\"{metric}_ci\\\\\\\", [v, v])\\\\n                        vals.append(v)\\\\n                        errs_lo.append(v - ci[0])\\\\n                        errs_hi.append(ci[1] - v)\\\\n\\\\n                    offset = (i - 1) * width\\\\n                    bars = ax.bar(\\\\n                        x + offset, vals, width,\\\\n                        label=STRATEGY_LABELS[strategy],\\\\n                        color=STRATEGY_COLORS[strategy],\\\\n                        yerr=[errs_lo, errs_hi],\\\\n                        capsize=3, alpha=0.85,\\\\n                    )\\\\n\\\\n                ax.set_xlabel(title)\\\\n                ax.set_ylabel(metric)\\\\n                ax.set_title(metric)\\\\n                ax.set_xticks(x)\\\\n                ax.set_xticklabels(bins_present, rotation=0)\\\\n                ax.legend(loc=\\\\\\\"best\\\\\\\")\\\\n                ax.set_ylim(bottom=0)\\\\n\\\\n            plt.tight_layout()\\\\n            pdf.savefig(fig, bbox_inches=\\\\\\\"tight\\\\\\\")\\\\n            plt.close(fig)\\\\n\\\\n        # ── Plot 2: Heatmap — stratum × strategy for R@1 ──\\\\n        heatmap_dims = [\\\\n            (\\\\\\\"Repo Size\\\\\\\", repo_analysis, list(REPO_SIZE_BINS.keys())),\\\\n            (\\\\\\\"Pool Size\\\\\\\", pool_analysis, list(POOL_SIZE_BINS.keys())),\\\\n            (\\\\\\\"Similarity\\\\\\\", sim_analysis, list(SIMILARITY_BINS.keys())),\\\\n        ]\\\\n        if dataflow_analysis:\\\\n            heatmap_dims.append((\\\\\\\"Dataflow\\\\\\\", dataflow_analysis, list(DATAFLOW_BINS.keys())))\\\\n        if neg_diff_analysis:\\\\n            heatmap_dims.append((\\\\\\\"Neg Difficulty\\\\\\\", neg_diff_analysis, NEG_DIFFICULTY_QUARTILE_LABELS))\\\\n        for title, analysis, bin_order in heatmap_dims:\\\\n            bins_present = [b for b in bin_order if b in analysis]\\\\n            if not bins_present:\\\\n                continue\\\\n\\\\n            data_matrix = []\\\\n            for b in bins_present:\\\\n                row = []\\\\n                for s in STRATEGIES:\\\\n               \\\\n\\\\n... [截断: 输出过长，省略 10875 字符] ...\\\\n\\\\nt\\\\\\\")):\\\\n                        ckpt_dir = candidate\\\\n                        break\\\\n                if ckpt_dir is None and os.path.exists(os.path.join(base, \\\\\\\"model.pt\\\\\\\")):\\\\n                    ckpt_dir = base\\\\n                if os.path.exists(ckpt_dir):\\\\n                    print(f\\\\\\\"  Re-evaluating checkpoint: {ckpt_dir}\\\\\\\", flush=True)\\\\n                    results = reeval_checkpoint(\\\\n                        ckpt_dir, val_samples, args.device, args.max_seq_length\\\\n                    )\\\\n                else:\\\\n                    print(f\\\\\\\"  [WARN] Checkpoint not found: {ckpt_dir}\\\\\\\", flush=True)\\\\n                    continue\\\\n            else:\\\\n                print(\\\\\\\"  [ERROR] No --dry-run, --predictions-dir, or --checkpoints-dir\\\\\\\", flush=True)\\\\n                continue\\\\n\\\\n            # Assign strata\\\\n            results = assign_strata(results, inst_to_repo, repo_counts, dataflow_edges)\\\\n\\\\n            # For dry-run or model-based: compute text similarity for sim_bin\\\\n            if args.dry_run:\\\\n                for r, s in zip(results, val_samples):\\\\n                    tsim = text_similarity(s[\\\\\\\"query_tokens\\\\\\\"][:500], s[\\\\\\\"pos_tokens\\\\\\\"][:500])\\\\n                    r[\\\\\\\"sim_bin\\\\\\\"] = _bin_value(tsim, SIMILARITY_BINS)\\\\n\\\\n            all_results[strategy][seed] = results\\\\n            val_samples_cache[f\\\\\\\"{strategy}_s{seed}\\\\\\\"] = val_samples\\\\n            print(f\\\\\\\"  -> {len(results)} instances\\\\\\\", flush=True)\\\\n\\\\n    # Compute neg_difficulty quartiles (text-overlap proxy, CPU-safe)\\\\n    print(\\\\\\\"Computing neg difficulty quartiles...\\\\\\\", flush=True)\\\\n    assign_neg_difficulty_quartiles(all_results, val_samples_cache)\\\\n\\\\n    # Run stratified analysis\\\\n    print(\\\\\\\"\\\\\\\\nRunning stratified analysis...\\\\\\\", flush=True)\\\\n    repo_analysis = run_stratified_analysis(\\\\n        all_results, \\\\\\\"repo_size_bin\\\\\\\", list(REPO_SIZE_BINS.keys()), args.n_bootstrap\\\\n    )\\\\n    pool_analysis = run_stratified_analysis(\\\\n        all_results, \\\\\\\"pool_size_bin\\\\\\\", list(POOL_SIZE_BINS.keys()), args.n_bootstrap\\\\n    )\\\\n    sim_analysis = run_stratified_analysis(\\\\n        all_results, \\\\\\\"sim_bin\\\\\\\", list(SIMILARITY_BINS.keys()), args.n_bootstrap\\\\n    )\\\\n\\\\n    dataflow_analysis = {}\\\\n    if dataflow_edges is not None:\\\\n        dataflow_analysis = run_stratified_analysis(\\\\n            all_results, \\\\\\\"dataflow_bin\\\\\\\", list(DATAFLOW_BINS.keys()), args.n_bootstrap\\\\n        )\\\\n\\\\n    neg_diff_analysis = run_stratified_analysis(\\\\n        all_results, \\\\\\\"neg_difficulty_bin\\\\\\\", NEG_DIFFICULTY_QUARTILE_LABELS, args.n_bootstrap\\\\n    )\\\\n\\\\n    # Save JSON\\\\n    full_results = {\\\\n        \\\\\\\"config\\\\\\\": {\\\\n            \\\\\\\"strategies\\\\\\\": STRATEGIES,\\\\n            \\\\\\\"seeds\\\\\\\": seeds,\\\\n            \\\\\\\"repo_size_bins\\\\\\\": {k: list(v) for k, v in REPO_SIZE_BINS.items()},\\\\n            \\\\\\\"pool_size_bins\\\\\\\": {k: list(v) for k, v in POOL_SIZE_BINS.items()},\\\\n            \\\\\\\"similarity_bins\\\\\\\": {k: list(v) for k, v in SIMILARITY_BINS.items()},\\\\n            \\\\\\\"dataflow_bins\\\\\\\": {k: list(v) for k, v in DATAFLOW_BINS.items()},\\\\n            \\\\\\\"neg_difficulty_quartiles\\\\\\\": NEG_DIFFICULTY_QUARTILE_LABELS,\\\\n            \\\\\\\"n_bootstrap\\\\\\\": args.n_bootstrap,\\\\n            \\\\\\\"dry_run\\\\\\\": args.dry_run,\\\\n        },\\\\n        \\\\\\\"by_repo_size\\\\\\\": repo_analysis,\\\\n        \\\\\\\"by_pool_size\\\\\\\": pool_analysis,\\\\n        \\\\\\\"by_similarity\\\\\\\": sim_analysis,\\\\n        \\\\\\\"by_dataflow\\\\\\\": dataflow_analysis,\\\\n        \\\\\\\"by_neg_difficulty\\\\\\\": neg_diff_analysis,\\\\n    }\\\\n\\\\n    json_path = os.path.join(args.output_dir, \\\\\\\"stratified_results.json\\\\\\\")\\\\n    with open(json_path, \\\\\\\"w\\\\\\\") as f:\\\\n        json.dump(full_results, f, indent=2, ensure_ascii=False)\\\\n    print(f\\\\\\\"  Results JSON saved to {json_path}\\\\\\\", flush=True)\\\\n\\\\n    # CSV summary\\\\n    csv_path = os.path.join(args.output_dir, \\\\\\\"stratified_summary.csv\\\\\\\")\\\\n    write_summary_csv(repo_analysis, pool_analysis, sim_analysis, csv_path, dataflow_analysis, neg_diff_analysis)\\\\n\\\\n    # Plots\\\\n    try:\\\\n        make_plots(repo_analysis, pool_analysis, sim_analysis, args.output_dir, dataflow_analysis, neg_diff_analysis)\\\\n    except Exception as e:\\\\n        print(f\\\\\\\"  [WARN] Plot generation failed: {e}\\\\\\\", flush=True)\\\\n\\\\n    print(\\\\\\\"\\\\\\\\nDone.\\\\\\\", flush=True)\\\\n\\\\n\\\\nif __name__ == \\\\\\\"__main__\\\\\\\":\\\\n    main()\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.4}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"def make_plots(\\n    repo_analysis: Dict,\\n    pool_analysis: Dict,\\n    sim_analysis: Dict,\\n    output_dir: str,\\n    dataflow_analysis: Optional[Dict] = None,\\n    neg_diff_analysis: Optional[Dict] = None,\\n):\\n    import matplotlib\\n    matplotlib.use(\\\"Agg\\\")\\n    import matplotlib.pyplot as plt\\n    from matplotlib.backends.backend_pdf import PdfPages\\n\\n    plt.rcParams.update({\\n        \\\"font.size\\\": 11,\\n        \\\"axes.titlesize\\\": 13,\\n        \\\"axes.labelsize\\\": 12,\\n        \\\"xtick.labelsize\\\": 10,\\n        \\\"ytick.labelsize\\\": 10,\\n        \\\"legend.fontsize\\\": 10,\\n        \\\"figure.dpi\\\": 150,\\n        \\\"savefig.dpi\\\": 300,\\n        \\\"font.family\\\": \\\"sans-serif\\\",\\n    })\\n\\n    pdf_path = os.path.join(output_dir, \\\"stratified_plots.pdf\\\")\\n    with PdfPages(pdf_path) as pdf:\\n        # ── Plot 1: Grouped bar chart per stratum dimension ──\\n        plot_dims = [\\n            (\\\"Repo Size\\\", repo_analysis, list(REPO_SIZE_BINS.keys())),\\n            (\\\"Candidate Pool Size\\\", pool_analysis, list(POOL_SIZE_BINS.keys())),\\n            (\\\"Query-Positive Similarity\\\", sim_analysis, list(SIMILARITY_BINS.keys())),\\n        ]\\n        if dataflow_analysis:\\n            plot_dims.append((\\\"Dataflow Availability\\\", dataflow_analysis, list(DATAFLOW_BINS.keys())))\\n        if neg_diff_analysis:\\n            plot_dims.append((\\\"Neg Difficulty Quartile\\\", neg_diff_analysis, NEG_DIFFICULTY_QUARTILE_LABELS))\\n        for title, analysis, bin_order in plot_dims:\\n            bins_present = [b for b in bin_order if b in analysis]\\n            if not bins_present:\\n                continue\\n\\n            fig, axes = plt.subplots(1, 3, figsize=(15, 5))\\n            fig.suptitle(f\\\"Stratified by {title}\\\", fontweight=\\\"bold\\\", y=1.02)\\n\\n            for ax_idx, metric in enumerate([\\\"R@1\\\", \\\"R@5\\\", \\\"MRR\\\"]):\\n                ax = axes[ax_idx]\\n                x = np.arange(len(bins_present))\\n                width = 0.25\\n\\n                for i, strategy in enumerate(STRATEGIES):\\n                    vals = []\\n                    errs_lo = []\\n                    errs_hi = []\\n                    for b in bins_present:\\n                        m = analysis[b].get(strategy, {})\\n                        v = m.get(metric, 0)\\n                        ci = m.get(f\\\"{metric}_ci\\\", [v, v])\\n                        vals.append(v)\\n                        errs_lo.append(v - ci[0])\\n                        errs_hi.append(ci[1] - v)\\n\\n                    offset = (i - 1) * width\\n                    bars = ax.bar(\\n                        x + offset, vals, width,\\n                        label=STRATEGY_LABELS[strategy],\\n                        color=STRATEGY_COLORS[strategy],\\n                        yerr=[errs_lo, errs_hi],\\n                        capsize=3, alpha=0.85,\\n                    )\\n\\n                ax.set_xlabel(title)\\n                ax.set_ylabel(metric)\\n                ax.set_title(metric)\\n                ax.set_xticks(x)\\n                ax.set_xticklabels(bins_present, rotation=0)\\n                ax.legend(loc=\\\"best\\\")\\n                ax.set_ylim(bottom=0)\\n\\n            plt.tight_layout()\\n            pdf.savefig(fig, bbox_inches=\\\"tight\\\")\\n            plt.close(fig)\\n\\n        # ── Plot 2: Heatmap — stratum × strategy for R@1 ──\\n        heatmap_dims = [\\n            (\\\"Repo Size\\\", repo_analysis, list(REPO_SIZE_BINS.keys())),\\n            (\\\"Pool Size\\\", pool_analysis, list(POOL_SIZE_BINS.keys())),\\n            (\\\"Similarity\\\", sim_analysis, list(SIMILARITY_BINS.keys())),\\n        ]\\n        if dataflow_analysis:\\n            heatmap_dims.append((\\\"Dataflow\\\", dataflow_analysis, list(DATAFLOW_BINS.keys())))\\n        if neg_diff_analysis:\\n            heatmap_dims.append((\\\"Neg Difficulty\\\", neg_diff_analysis, NEG_DIFFICULTY_QUARTILE_LABELS))\\n        for title, analysis, bin_order in heatmap_dims:\\n            bins_present = [b for b in bin_order if b in analysis]\\n            if not bins_present:\\n                continue\\n\\n            data_matrix = []\\n            for b in bins_present:\\n                row = []\\n                for s in STRATEGIES:\\n               \\n\\n... [截断: 输出过长，省略 10875 字符] ...\\n\\nt\\\")):\\n                        ckpt_dir = candidate\\n                        break\\n                if ckpt_dir is None and os.path.exists(os.path.join(base, \\\"model.pt\\\")):\\n                    ckpt_dir = base\\n                if os.path.exists(ckpt_dir):\\n                    print(f\\\"  Re-evaluating checkpoint: {ckpt_dir}\\\", flush=True)\\n                    results = reeval_checkpoint(\\n                        ckpt_dir, val_samples, args.device, args.max_seq_length\\n                    )\\n                else:\\n                    print(f\\\"  [WARN] Checkpoint not found: {ckpt_dir}\\\", flush=True)\\n                    continue\\n            else:\\n                print(\\\"  [ERROR] No --dry-run, --predictions-dir, or --checkpoints-dir\\\", flush=True)\\n                continue\\n\\n            # Assign strata\\n            results = assign_strata(results, inst_to_repo, repo_counts, dataflow_edges)\\n\\n            # For dry-run or model-based: compute text similarity for sim_bin\\n            if args.dry_run:\\n                for r, s in zip(results, val_samples):\\n                    tsim = text_similarity(s[\\\"query_tokens\\\"][:500], s[\\\"pos_tokens\\\"][:500])\\n                    r[\\\"sim_bin\\\"] = _bin_value(tsim, SIMILARITY_BINS)\\n\\n            all_results[strategy][seed] = results\\n            val_samples_cache[f\\\"{strategy}_s{seed}\\\"] = val_samples\\n            print(f\\\"  -> {len(results)} instances\\\", flush=True)\\n\\n    # Compute neg_difficulty quartiles (text-overlap proxy, CPU-safe)\\n    print(\\\"Computing neg difficulty quartiles...\\\", flush=True)\\n    assign_neg_difficulty_quartiles(all_results, val_samples_cache)\\n\\n    # Run stratified analysis\\n    print(\\\"\\\\nRunning stratified analysis...\\\", flush=True)\\n    repo_analysis = run_stratified_analysis(\\n        all_results, \\\"repo_size_bin\\\", list(REPO_SIZE_BINS.keys()), args.n_bootstrap\\n    )\\n    pool_analysis = run_stratified_analysis(\\n        all_results, \\\"pool_size_bin\\\", list(POOL_SIZE_BINS.keys()), args.n_bootstrap\\n    )\\n    sim_analysis = run_stratified_analysis(\\n        all_results, \\\"sim_bin\\\", list(SIMILARITY_BINS.keys()), args.n_bootstrap\\n    )\\n\\n    dataflow_analysis = {}\\n    if dataflow_edges is not None:\\n        dataflow_analysis = run_stratified_analysis(\\n            all_results, \\\"dataflow_bin\\\", list(DATAFLOW_BINS.keys()), args.n_bootstrap\\n        )\\n\\n    neg_diff_analysis = run_stratified_analysis(\\n        all_results, \\\"neg_difficulty_bin\\\", NEG_DIFFICULTY_QUARTILE_LABELS, args.n_bootstrap\\n    )\\n\\n    # Save JSON\\n    full_results = {\\n        \\\"config\\\": {\\n            \\\"strategies\\\": STRATEGIES,\\n            \\\"seeds\\\": seeds,\\n            \\\"repo_size_bins\\\": {k: list(v) for k, v in REPO_SIZE_BINS.items()},\\n            \\\"pool_size_bins\\\": {k: list(v) for k, v in POOL_SIZE_BINS.items()},\\n            \\\"similarity_bins\\\": {k: list(v) for k, v in SIMILARITY_BINS.items()},\\n            \\\"dataflow_bins\\\": {k: list(v) for k, v in DATAFLOW_BINS.items()},\\n            \\\"neg_difficulty_quartiles\\\": NEG_DIFFICULTY_QUARTILE_LABELS,\\n            \\\"n_bootstrap\\\": args.n_bootstrap,\\n            \\\"dry_run\\\": args.dry_run,\\n        },\\n        \\\"by_repo_size\\\": repo_analysis,\\n        \\\"by_pool_size\\\": pool_analysis,\\n        \\\"by_similarity\\\": sim_analysis,\\n        \\\"by_dataflow\\\": dataflow_analysis,\\n        \\\"by_neg_difficulty\\\": neg_diff_analysis,\\n    }\\n\\n    json_path = os.path.join(args.output_dir, \\\"stratified_results.json\\\")\\n    with open(json_path, \\\"w\\\") as f:\\n        json.dump(full_results, f, indent=2, ensure_ascii=False)\\n    print(f\\\"  Results JSON saved to {json_path}\\\", flush=True)\\n\\n    # CSV summary\\n    csv_path = os.path.join(args.output_dir, \\\"stratified_summary.csv\\\")\\n    write_summary_csv(repo_analysis, pool_analysis, sim_analysis, csv_path, dataflow_analysis, neg_diff_analysis)\\n\\n    # Plots\\n    try:\\n        make_plots(repo_analysis, pool_analysis, sim_analysis, args.output_dir, dataflow_analysis, neg_diff_analysis)\\n    except Exception as e:\\n        print(f\\\"  [WARN] Plot generation failed: {e}\\\", flush=True)\\n\\n    print(\\\"\\\\nDone.\\\", flush=True)\\n\\n\\nif __name__ == \\\"__main__\\\":\\n    main()\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4}}"
    }
  },
  "sourceToolAssistantUUID": "d371b5f1-7af6-4eb8-a09d-16488ec221be",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "bda3dfbf-4b90-494d-b674-2597173fd381",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 53_

```json
{
  "type": "last-prompt",
  "leafUuid": "5868264b-e384-4f80-83ce-93260dd5f77f",
  "sessionId": "bda3dfbf-4b90-494d-b674-2597173fd381"
}
```

---

### Runtime record

_source line 54_

```json
{
  "type": "ai-title",
  "aiTitle": "Add pool-size controlled stratified evaluation to analysis script",
  "sessionId": "bda3dfbf-4b90-494d-b674-2597173fd381"
}
```

---

### Assistant

_source line 55 · 2026-05-14T20:47:33.782Z_

<details><summary>Logged reasoning block</summary>

```text
I still have truncation in the middle. Let me get the key middle sections I'm missing. I need:
1. Lines 574-649 (end of make_plots, specifically the heatmap section that was truncated)
2. Lines 649-713 (write_summary_csv)
3. Lines 713-830 (beginning of main, including argparse and data loading)

And also 230-268 (load_predictions function)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5868264b-e384-4f80-83ce-93260dd5f77f",
  "isSidechain": false,
  "requestId": "req_011Cb37mPjuMDioHqofaaPw4",
  "type": "assistant",
  "uuid": "2e785df4-adb3-4f22-b468-61a197ed33f9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "bda3dfbf-4b90-494d-b674-2597173fd381",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B3EKBPjXoiqmGntqrH9vnZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3271,
      "cache_read_input_tokens": 47590,
      "output_tokens": 237,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3271,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 237,
          "cache_read_input_tokens": 47590,
          "cache_creation_input_tokens": 3271,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3271
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

_source line 56 · 2026-05-14T20:47:34.153Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_018z5tTi4ZDjwYew6ie2qAu8`</summary>

```json
{
  "server": "bjb1-42106",
  "command": "head -268 /root/structfuse/evaluation/analyze_stratified.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2e785df4-adb3-4f22-b468-61a197ed33f9",
  "isSidechain": false,
  "requestId": "req_011Cb37mPjuMDioHqofaaPw4",
  "type": "assistant",
  "uuid": "6f64f635-9dc8-4767-ae58-b093b89db92b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "bda3dfbf-4b90-494d-b674-2597173fd381",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B3EKBPjXoiqmGntqrH9vnZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3271,
      "cache_read_input_tokens": 47590,
      "output_tokens": 237,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3271,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 237,
          "cache_read_input_tokens": 47590,
          "cache_creation_input_tokens": 3271,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3271
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

_source line 57 · 2026-05-14T20:47:34.521Z_

<details><summary>↩ Tool result · `toolu_018z5tTi4ZDjwYew6ie2qAu8`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n\\\"\\\"\\\"Stratified analysis of embedding vs random negative strategies by data strata.\\n\\nAnalyses M2 per-instance predictions across:\\n  - Repo size (instance count per repo from M1)\\n  - Candidate pool size (neg_candidates per query)\\n  - Query-positive similarity (cosine sim from model, or text overlap for dry-run)\\n\\nInputs:\\n  - M2 per-instance predictions (from --predictions-dir or re-eval from checkpoints)\\n  - M1 all.jsonl (repo metadata)\\n  - Val JSONL files (query/candidate structure)\\n\\nOutputs:\\n  - stratified_results.json: full per-stratum metrics with bootstrap CI\\n  - stratified_summary.csv: compact table\\n  - stratified_plots.pdf: grouped bar charts, heatmaps, delta trends\\n\\\"\\\"\\\"\\n\\nimport argparse\\nimport csv\\nimport json\\nimport math\\nimport os\\nimport sys\\nfrom collections import Counter, defaultdict\\nfrom pathlib import Path\\nfrom typing import Any, Dict, List, Optional, Tuple\\n\\nimport numpy as np\\n\\nSTRATEGIES = [\\\"random\\\", \\\"embedding_distance\\\", \\\"dataflow_aware\\\"]\\nSTRATEGY_LABELS = {\\\"random\\\": \\\"Random\\\", \\\"embedding_distance\\\": \\\"Embedding\\\", \\\"dataflow_aware\\\": \\\"Dataflow\\\"}\\nSTRATEGY_COLORS = {\\\"random\\\": \\\"#4C72B0\\\", \\\"embedding_distance\\\": \\\"#DD8452\\\", \\\"dataflow_aware\\\": \\\"#55A868\\\"}\\n\\nREPO_SIZE_BINS = {\\n    \\\"small\\\": (0, 50),\\n    \\\"medium\\\": (50, 200),\\n    \\\"large\\\": (200, 500),\\n    \\\"xlarge\\\": (500, float(\\\"inf\\\")),\\n}\\n\\nPOOL_SIZE_BINS = {\\n    \\\"small\\\": (0, 20),\\n    \\\"medium\\\": (20, 40),\\n    \\\"large\\\": (40, 51),\\n}\\n\\nSIMILARITY_BINS = {\\n    \\\"low\\\": (0.0, 0.3),\\n    \\\"medium\\\": (0.3, 0.6),\\n    \\\"high\\\": (0.6, 1.01),\\n}\\n\\nDATAFLOW_BINS = {\\n    \\\"sparse\\\": (0, 2),\\n    \\\"moderate\\\": (2, 10),\\n    \\\"rich\\\": (10, float(\\\"inf\\\")),\\n}\\n\\nNEG_DIFFICULTY_QUARTILE_LABELS = [\\\"Q1_easy\\\", \\\"Q2\\\", \\\"Q3\\\", \\\"Q4_hard\\\"]\\n\\n\\ndef _bin_value(value, bins):\\n    for name, (lo, hi) in bins.items():\\n        if lo <= value < hi:\\n            return name\\n    return \\\"unknown\\\"\\n\\n\\n# ── M1 metadata ───────────────────────────────────────────────────��─\\n\\ndef load_m1_metadata(m1_path: str) -> Tuple[Dict[str, str], Dict[str, int]]:\\n    import re\\n    inst_to_repo = {}\\n    repo_counts: Counter = Counter()\\n    pat_iid = re.compile(r'\\\"instance_id\\\"\\\\s*:\\\\s*\\\"([^\\\"]+)\\\"')\\n    pat_repo = re.compile(r'\\\"repo\\\"\\\\s*:\\\\s*\\\"([^\\\"]+)\\\"')\\n    with open(m1_path) as f:\\n        for line in f:\\n            m_iid = pat_iid.search(line)\\n            m_repo = pat_repo.search(line)\\n            if m_iid and m_repo:\\n                iid = m_iid.group(1)\\n                repo = m_repo.group(1)\\n                inst_to_repo[iid] = repo\\n                repo_counts[repo] += 1\\n    return inst_to_repo, dict(repo_counts)\\n\\n\\n# ── Dataflow graph loading ────────────────────────────────────────────\\n\\ndef load_dataflow_edges(graph_path: str) -> Dict[str, int]:\\n    \\\"\\\"\\\"Load dataflow graph and return {file_key: edge_count}.\\\"\\\"\\\"\\n    with open(graph_path) as f:\\n        graph = json.load(f)\\n    return {k: len(v) for k, v in graph.items()}\\n\\n\\n# ── Val data loading ─────────────────────────────────────────────────\\n\\ndef load_val_samples(val_path: str, lite: bool = False) -> List[Dict[str, Any]]:\\n    \\\"\\\"\\\"Load val JSONL. lite=True skips candidate_tokens (faster for dry-run).\\\"\\\"\\\"\\n    import re\\n    samples = []\\n    pat_qid = re.compile(r'\\\"query_id\\\"\\\\s*:\\\\s*\\\"([^\\\"]+)\\\"')\\n    with open(val_path) as f:\\n        for line in f:\\n            if not line.strip():\\n                continue\\n            if lite:\\n                m = pat_qid.search(line)\\n                if not m:\\n                    continue\\n                qid = m.group(1)\\n                instance_id = qid.split(\\\"::\\\")[0] if \\\"::\\\" in qid else qid\\n                d = json.loads(line)\\n                samples.append({\\n                    \\\"query_id\\\": qid,\\n                    \\\"instance_id\\\": instance_id,\\n                    \\\"pool_size\\\": len(d.get(\\\"neg_candidates\\\", [])),\\n                    \\\"query_tokens\\\": d.get(\\\"query_tokens\\\", \\\"\\\")[:1000],\\n                    \\\"pos_tokens\\\": d.get(\\\"pos_tokens\\\", \\\"\\\")[:1000],\\n                    \\\"neg_candidates\\\": [],\\n                    \\\"candidate_tokens\\\": {},\\n                })\\n            else:\\n                d = jso\\n\\n... [截断: 输出过长，省略 1039 字符] ...\\n\\nmax_seq_length: int = 2048,\\n) -> List[Dict]:\\n    import torch\\n    from transformers import AutoTokenizer\\n\\n    train_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), \\\"..\\\", \\\"training\\\")\\n    if train_dir not in sys.path:\\n        sys.path.insert(0, train_dir)\\n    from contrastive_model import StructFuseEncoder\\n\\n    config_path = os.path.join(checkpoint_dir, \\\"training_config.json\\\")\\n    with open(config_path) as f:\\n        config = json.load(f)\\n\\n    model_name = config.get(\\\"model_name\\\", \\\"Qwen/Qwen2.5-Coder-3B\\\")\\n    tokenizer = AutoTokenizer.from_pretrained(checkpoint_dir, trust_remote_code=True)\\n\\n    model = StructFuseEncoder(\\n        model_name=model_name,\\n        proj_dim=config.get(\\\"proj_dim\\\", 256),\\n        use_projection=True,\\n        use_lora=config.get(\\\"use_lora\\\", False),\\n        lora_r=config.get(\\\"lora_r\\\", 16),\\n        use_fusion_head=config.get(\\\"use_fusion_head\\\", False),\\n    )\\n    state_dict = torch.load(os.path.join(checkpoint_dir, \\\"model.pt\\\"), map_location=\\\"cpu\\\")\\n    model.load_state_dict(state_dict, strict=False)\\n    model = model.to(device).eval()\\n\\n    results = []\\n    with torch.no_grad():\\n        for i, sample in enumerate(val_samples):\\n            if (i + 1) % 200 == 0:\\n                print(f\\\"  re-eval {i+1}/{len(val_samples)}\\\", flush=True)\\n\\n            def _encode(text):\\n                enc = tokenizer(text, truncation=True, max_length=max_seq_length,\\n                                padding=True, return_tensors=\\\"pt\\\")\\n                enc = {k: v.to(device) for k, v in enc.items()}\\n                return model.encode(enc[\\\"input_ids\\\"], enc[\\\"attention_mask\\\"])\\n\\n            q_emb = _encode(sample[\\\"query_tokens\\\"])\\n            p_emb = _encode(sample[\\\"pos_tokens\\\"])\\n            pos_sim = (q_emb * p_emb).sum().item()\\n\\n            neg_sims = []\\n            for neg_id in sample[\\\"neg_candidates\\\"]:\\n                neg_text = sample[\\\"candidate_tokens\\\"].get(neg_id, \\\"\\\")\\n                if not neg_text:\\n                    continue\\n                n_emb = _encode(neg_text)\\n                neg_sims.append((q_emb * n_emb).sum().item())\\n\\n            rank = 1 + sum(1 for s in neg_sims if s >= pos_sim)\\n\\n            results.append({\\n                \\\"query_id\\\": sample[\\\"query_id\\\"],\\n                \\\"instance_id\\\": sample[\\\"instance_id\\\"],\\n                \\\"pool_size\\\": sample[\\\"pool_size\\\"],\\n                \\\"rank\\\": rank,\\n                \\\"pos_sim\\\": pos_sim,\\n                \\\"total_candidates\\\": 1 + len(neg_sims),\\n            })\\n\\n    del model\\n    if torch.cuda.is_available():\\n        torch.cuda.empty_cache()\\n    return results\\n\\n\\n# ── Predictions loading ──────────────────────────────────────────────\\n\\ndef load_predictions(pred_file: str, val_samples: List[Dict]) -> List[Dict]:\\n    \\\"\\\"\\\"Load predictions from eval_retrieval.py output format.\\\"\\\"\\\"\\n    with open(pred_file) as f:\\n        data = json.load(f)\\n\\n    per_inst = {}\\n    results_list = data.get(\\\"results\\\", [data]) if \\\"results\\\" in data else [data]\\n    for r in results_list:\\n        for pi in r.get(\\\"per_instance\\\", []):\\n            per_inst[pi[\\\"instance_id\\\"]] = pi\\n\\n    val_lookup = {s[\\\"query_id\\\"]: s for s in val_samples}\\n    results = []\\n    for sample in val_samples:\\n        iid = sample[\\\"instance_id\\\"]\\n        pred = per_inst.get(iid)\\n        if pred is None:\\n            continue\\n        gold = set(pred.get(\\\"gold_files\\\", []))\\n        predicted = pred.get(\\\"predicted_top10\\\", [])\\n        rank = len(predicted) + 1\\n        for j, pf in enumerate(predicted):\\n            if pf in gold:\\n                rank = j + 1\\n                break\\n        results.append({\\n            \\\"query_id\\\": sample[\\\"query_id\\\"],\\n            \\\"instance_id\\\": iid,\\n            \\\"pool_size\\\": sample[\\\"pool_size\\\"],\\n            \\\"rank\\\": rank,\\n            \\\"pos_sim\\\": pred.get(\\\"scores_top10\\\", [0.0])[0] if pred.get(\\\"scores_top10\\\") else 0.0,\\n            \\\"total_candidates\\\": max(len(predicted), sample[\\\"pool_size\\\"] + 1),\\n        })\\n    return results\\n\\n\\n# ── Mock predictions (dry-run) ───────────────────────────────────────\\n\\ndef mock_predictions(\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6f64f635-9dc8-4767-ae58-b093b89db92b",
  "isSidechain": false,
  "promptId": "22ffd1fb-240e-481f-9bcc-b3f6a42d6805",
  "type": "user",
  "uuid": "f9016569-26c2-4229-a760-83c5888893bb",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"#!/usr/bin/env python3\\\\n\\\\\\\"\\\\\\\"\\\\\\\"Stratified analysis of embedding vs random negative strategies by data strata.\\\\n\\\\nAnalyses M2 per-instance predictions across:\\\\n  - Repo size (instance count per repo from M1)\\\\n  - Candidate pool size (neg_candidates per query)\\\\n  - Query-positive similarity (cosine sim from model, or text overlap for dry-run)\\\\n\\\\nInputs:\\\\n  - M2 per-instance predictions (from --predictions-dir or re-eval from checkpoints)\\\\n  - M1 all.jsonl (repo metadata)\\\\n  - Val JSONL files (query/candidate structure)\\\\n\\\\nOutputs:\\\\n  - stratified_results.json: full per-stratum metrics with bootstrap CI\\\\n  - stratified_summary.csv: compact table\\\\n  - stratified_plots.pdf: grouped bar charts, heatmaps, delta trends\\\\n\\\\\\\"\\\\\\\"\\\\\\\"\\\\n\\\\nimport argparse\\\\nimport csv\\\\nimport json\\\\nimport math\\\\nimport os\\\\nimport sys\\\\nfrom collections import Counter, defaultdict\\\\nfrom pathlib import Path\\\\nfrom typing import Any, Dict, List, Optional, Tuple\\\\n\\\\nimport numpy as np\\\\n\\\\nSTRATEGIES = [\\\\\\\"random\\\\\\\", \\\\\\\"embedding_distance\\\\\\\", \\\\\\\"dataflow_aware\\\\\\\"]\\\\nSTRATEGY_LABELS = {\\\\\\\"random\\\\\\\": \\\\\\\"Random\\\\\\\", \\\\\\\"embedding_distance\\\\\\\": \\\\\\\"Embedding\\\\\\\", \\\\\\\"dataflow_aware\\\\\\\": \\\\\\\"Dataflow\\\\\\\"}\\\\nSTRATEGY_COLORS = {\\\\\\\"random\\\\\\\": \\\\\\\"#4C72B0\\\\\\\", \\\\\\\"embedding_distance\\\\\\\": \\\\\\\"#DD8452\\\\\\\", \\\\\\\"dataflow_aware\\\\\\\": \\\\\\\"#55A868\\\\\\\"}\\\\n\\\\nREPO_SIZE_BINS = {\\\\n    \\\\\\\"small\\\\\\\": (0, 50),\\\\n    \\\\\\\"medium\\\\\\\": (50, 200),\\\\n    \\\\\\\"large\\\\\\\": (200, 500),\\\\n    \\\\\\\"xlarge\\\\\\\": (500, float(\\\\\\\"inf\\\\\\\")),\\\\n}\\\\n\\\\nPOOL_SIZE_BINS = {\\\\n    \\\\\\\"small\\\\\\\": (0, 20),\\\\n    \\\\\\\"medium\\\\\\\": (20, 40),\\\\n    \\\\\\\"large\\\\\\\": (40, 51),\\\\n}\\\\n\\\\nSIMILARITY_BINS = {\\\\n    \\\\\\\"low\\\\\\\": (0.0, 0.3),\\\\n    \\\\\\\"medium\\\\\\\": (0.3, 0.6),\\\\n    \\\\\\\"high\\\\\\\": (0.6, 1.01),\\\\n}\\\\n\\\\nDATAFLOW_BINS = {\\\\n    \\\\\\\"sparse\\\\\\\": (0, 2),\\\\n    \\\\\\\"moderate\\\\\\\": (2, 10),\\\\n    \\\\\\\"rich\\\\\\\": (10, float(\\\\\\\"inf\\\\\\\")),\\\\n}\\\\n\\\\nNEG_DIFFICULTY_QUARTILE_LABELS = [\\\\\\\"Q1_easy\\\\\\\", \\\\\\\"Q2\\\\\\\", \\\\\\\"Q3\\\\\\\", \\\\\\\"Q4_hard\\\\\\\"]\\\\n\\\\n\\\\ndef _bin_value(value, bins):\\\\n    for name, (lo, hi) in bins.items():\\\\n        if lo <= value < hi:\\\\n            return name\\\\n    return \\\\\\\"unknown\\\\\\\"\\\\n\\\\n\\\\n# ── M1 metadata ───────────────────────────────────────────────────��─\\\\n\\\\ndef load_m1_metadata(m1_path: str) -> Tuple[Dict[str, str], Dict[str, int]]:\\\\n    import re\\\\n    inst_to_repo = {}\\\\n    repo_counts: Counter = Counter()\\\\n    pat_iid = re.compile(r'\\\\\\\"instance_id\\\\\\\"\\\\\\\\s*:\\\\\\\\s*\\\\\\\"([^\\\\\\\"]+)\\\\\\\"')\\\\n    pat_repo = re.compile(r'\\\\\\\"repo\\\\\\\"\\\\\\\\s*:\\\\\\\\s*\\\\\\\"([^\\\\\\\"]+)\\\\\\\"')\\\\n    with open(m1_path) as f:\\\\n        for line in f:\\\\n            m_iid = pat_iid.search(line)\\\\n            m_repo = pat_repo.search(line)\\\\n            if m_iid and m_repo:\\\\n                iid = m_iid.group(1)\\\\n                repo = m_repo.group(1)\\\\n                inst_to_repo[iid] = repo\\\\n                repo_counts[repo] += 1\\\\n    return inst_to_repo, dict(repo_counts)\\\\n\\\\n\\\\n# ── Dataflow graph loading ────────────────────────────────────────────\\\\n\\\\ndef load_dataflow_edges(graph_path: str) -> Dict[str, int]:\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"Load dataflow graph and return {file_key: edge_count}.\\\\\\\"\\\\\\\"\\\\\\\"\\\\n    with open(graph_path) as f:\\\\n        graph = json.load(f)\\\\n    return {k: len(v) for k, v in graph.items()}\\\\n\\\\n\\\\n# ── Val data loading ─────────────────────────────────────────────────\\\\n\\\\ndef load_val_samples(val_path: str, lite: bool = False) -> List[Dict[str, Any]]:\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"Load val JSONL. lite=True skips candidate_tokens (faster for dry-run).\\\\\\\"\\\\\\\"\\\\\\\"\\\\n    import re\\\\n    samples = []\\\\n    pat_qid = re.compile(r'\\\\\\\"query_id\\\\\\\"\\\\\\\\s*:\\\\\\\\s*\\\\\\\"([^\\\\\\\"]+)\\\\\\\"')\\\\n    with open(val_path) as f:\\\\n        for line in f:\\\\n            if not line.strip():\\\\n                continue\\\\n            if lite:\\\\n                m = pat_qid.search(line)\\\\n                if not m:\\\\n                    continue\\\\n                qid = m.group(1)\\\\n                instance_id = qid.split(\\\\\\\"::\\\\\\\")[0] if \\\\\\\"::\\\\\\\" in qid else qid\\\\n                d = json.loads(line)\\\\n                samples.append({\\\\n                    \\\\\\\"query_id\\\\\\\": qid,\\\\n                    \\\\\\\"instance_id\\\\\\\": instance_id,\\\\n                    \\\\\\\"pool_size\\\\\\\": len(d.get(\\\\\\\"neg_candidates\\\\\\\", [])),\\\\n                    \\\\\\\"query_tokens\\\\\\\": d.get(\\\\\\\"query_tokens\\\\\\\", \\\\\\\"\\\\\\\")[:1000],\\\\n                    \\\\\\\"pos_tokens\\\\\\\": d.get(\\\\\\\"pos_tokens\\\\\\\", \\\\\\\"\\\\\\\")[:1000],\\\\n                    \\\\\\\"neg_candidates\\\\\\\": [],\\\\n                    \\\\\\\"candidate_tokens\\\\\\\": {},\\\\n                })\\\\n            else:\\\\n                d = jso\\\\n\\\\n... [截断: 输出过长，省略 1039 字符] ...\\\\n\\\\nmax_seq_length: int = 2048,\\\\n) -> List[Dict]:\\\\n    import torch\\\\n    from transformers import AutoTokenizer\\\\n\\\\n    train_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), \\\\\\\"..\\\\\\\", \\\\\\\"training\\\\\\\")\\\\n    if train_dir not in sys.path:\\\\n        sys.path.insert(0, train_dir)\\\\n    from contrastive_model import StructFuseEncoder\\\\n\\\\n    config_path = os.path.join(checkpoint_dir, \\\\\\\"training_config.json\\\\\\\")\\\\n    with open(config_path) as f:\\\\n        config = json.load(f)\\\\n\\\\n    model_name = config.get(\\\\\\\"model_name\\\\\\\", \\\\\\\"Qwen/Qwen2.5-Coder-3B\\\\\\\")\\\\n    tokenizer = AutoTokenizer.from_pretrained(checkpoint_dir, trust_remote_code=True)\\\\n\\\\n    model = StructFuseEncoder(\\\\n        model_name=model_name,\\\\n        proj_dim=config.get(\\\\\\\"proj_dim\\\\\\\", 256),\\\\n        use_projection=True,\\\\n        use_lora=config.get(\\\\\\\"use_lora\\\\\\\", False),\\\\n        lora_r=config.get(\\\\\\\"lora_r\\\\\\\", 16),\\\\n        use_fusion_head=config.get(\\\\\\\"use_fusion_head\\\\\\\", False),\\\\n    )\\\\n    state_dict = torch.load(os.path.join(checkpoint_dir, \\\\\\\"model.pt\\\\\\\"), map_location=\\\\\\\"cpu\\\\\\\")\\\\n    model.load_state_dict(state_dict, strict=False)\\\\n    model = model.to(device).eval()\\\\n\\\\n    results = []\\\\n    with torch.no_grad():\\\\n        for i, sample in enumerate(val_samples):\\\\n            if (i + 1) % 200 == 0:\\\\n                print(f\\\\\\\"  re-eval {i+1}/{len(val_samples)}\\\\\\\", flush=True)\\\\n\\\\n            def _encode(text):\\\\n                enc = tokenizer(text, truncation=True, max_length=max_seq_length,\\\\n                                padding=True, return_tensors=\\\\\\\"pt\\\\\\\")\\\\n                enc = {k: v.to(device) for k, v in enc.items()}\\\\n                return model.encode(enc[\\\\\\\"input_ids\\\\\\\"], enc[\\\\\\\"attention_mask\\\\\\\"])\\\\n\\\\n            q_emb = _encode(sample[\\\\\\\"query_tokens\\\\\\\"])\\\\n            p_emb = _encode(sample[\\\\\\\"pos_tokens\\\\\\\"])\\\\n            pos_sim = (q_emb * p_emb).sum().item()\\\\n\\\\n            neg_sims = []\\\\n            for neg_id in sample[\\\\\\\"neg_candidates\\\\\\\"]:\\\\n                neg_text = sample[\\\\\\\"candidate_tokens\\\\\\\"].get(neg_id, \\\\\\\"\\\\\\\")\\\\n                if not neg_text:\\\\n                    continue\\\\n                n_emb = _encode(neg_text)\\\\n                neg_sims.append((q_emb * n_emb).sum().item())\\\\n\\\\n            rank = 1 + sum(1 for s in neg_sims if s >= pos_sim)\\\\n\\\\n            results.append({\\\\n                \\\\\\\"query_id\\\\\\\": sample[\\\\\\\"query_id\\\\\\\"],\\\\n                \\\\\\\"instance_id\\\\\\\": sample[\\\\\\\"instance_id\\\\\\\"],\\\\n                \\\\\\\"pool_size\\\\\\\": sample[\\\\\\\"pool_size\\\\\\\"],\\\\n                \\\\\\\"rank\\\\\\\": rank,\\\\n                \\\\\\\"pos_sim\\\\\\\": pos_sim,\\\\n                \\\\\\\"total_candidates\\\\\\\": 1 + len(neg_sims),\\\\n            })\\\\n\\\\n    del model\\\\n    if torch.cuda.is_available():\\\\n        torch.cuda.empty_cache()\\\\n    return results\\\\n\\\\n\\\\n# ── Predictions loading ──────────────────────────────────────────────\\\\n\\\\ndef load_predictions(pred_file: str, val_samples: List[Dict]) -> List[Dict]:\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"Load predictions from eval_retrieval.py output format.\\\\\\\"\\\\\\\"\\\\\\\"\\\\n    with open(pred_file) as f:\\\\n        data = json.load(f)\\\\n\\\\n    per_inst = {}\\\\n    results_list = data.get(\\\\\\\"results\\\\\\\", [data]) if \\\\\\\"results\\\\\\\" in data else [data]\\\\n    for r in results_list:\\\\n        for pi in r.get(\\\\\\\"per_instance\\\\\\\", []):\\\\n            per_inst[pi[\\\\\\\"instance_id\\\\\\\"]] = pi\\\\n\\\\n    val_lookup = {s[\\\\\\\"query_id\\\\\\\"]: s for s in val_samples}\\\\n    results = []\\\\n    for sample in val_samples:\\\\n        iid = sample[\\\\\\\"instance_id\\\\\\\"]\\\\n        pred = per_inst.get(iid)\\\\n        if pred is None:\\\\n            continue\\\\n        gold = set(pred.get(\\\\\\\"gold_files\\\\\\\", []))\\\\n        predicted = pred.get(\\\\\\\"predicted_top10\\\\\\\", [])\\\\n        rank = len(predicted) + 1\\\\n        for j, pf in enumerate(predicted):\\\\n            if pf in gold:\\\\n                rank = j + 1\\\\n                break\\\\n        results.append({\\\\n            \\\\\\\"query_id\\\\\\\": sample[\\\\\\\"query_id\\\\\\\"],\\\\n            \\\\\\\"instance_id\\\\\\\": iid,\\\\n            \\\\\\\"pool_size\\\\\\\": sample[\\\\\\\"pool_size\\\\\\\"],\\\\n            \\\\\\\"rank\\\\\\\": rank,\\\\n            \\\\\\\"pos_sim\\\\\\\": pred.get(\\\\\\\"scores_top10\\\\\\\", [0.0])[0] if pred.get(\\\\\\\"scores_top10\\\\\\\") else 0.0,\\\\n            \\\\\\\"total_candidates\\\\\\\": max(len(predicted), sample[\\\\\\\"pool_size\\\\\\\"] + 1),\\\\n        })\\\\n    return results\\\\n\\\\n\\\\n# ── Mock predictions (dry-run) ───────────────────────────────────────\\\\n\\\\ndef mock_predictions(\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.36}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n\\\"\\\"\\\"Stratified analysis of embedding vs random negative strategies by data strata.\\n\\nAnalyses M2 per-instance predictions across:\\n  - Repo size (instance count per repo from M1)\\n  - Candidate pool size (neg_candidates per query)\\n  - Query-positive similarity (cosine sim from model, or text overlap for dry-run)\\n\\nInputs:\\n  - M2 per-instance predictions (from --predictions-dir or re-eval from checkpoints)\\n  - M1 all.jsonl (repo metadata)\\n  - Val JSONL files (query/candidate structure)\\n\\nOutputs:\\n  - stratified_results.json: full per-stratum metrics with bootstrap CI\\n  - stratified_summary.csv: compact table\\n  - stratified_plots.pdf: grouped bar charts, heatmaps, delta trends\\n\\\"\\\"\\\"\\n\\nimport argparse\\nimport csv\\nimport json\\nimport math\\nimport os\\nimport sys\\nfrom collections import Counter, defaultdict\\nfrom pathlib import Path\\nfrom typing import Any, Dict, List, Optional, Tuple\\n\\nimport numpy as np\\n\\nSTRATEGIES = [\\\"random\\\", \\\"embedding_distance\\\", \\\"dataflow_aware\\\"]\\nSTRATEGY_LABELS = {\\\"random\\\": \\\"Random\\\", \\\"embedding_distance\\\": \\\"Embedding\\\", \\\"dataflow_aware\\\": \\\"Dataflow\\\"}\\nSTRATEGY_COLORS = {\\\"random\\\": \\\"#4C72B0\\\", \\\"embedding_distance\\\": \\\"#DD8452\\\", \\\"dataflow_aware\\\": \\\"#55A868\\\"}\\n\\nREPO_SIZE_BINS = {\\n    \\\"small\\\": (0, 50),\\n    \\\"medium\\\": (50, 200),\\n    \\\"large\\\": (200, 500),\\n    \\\"xlarge\\\": (500, float(\\\"inf\\\")),\\n}\\n\\nPOOL_SIZE_BINS = {\\n    \\\"small\\\": (0, 20),\\n    \\\"medium\\\": (20, 40),\\n    \\\"large\\\": (40, 51),\\n}\\n\\nSIMILARITY_BINS = {\\n    \\\"low\\\": (0.0, 0.3),\\n    \\\"medium\\\": (0.3, 0.6),\\n    \\\"high\\\": (0.6, 1.01),\\n}\\n\\nDATAFLOW_BINS = {\\n    \\\"sparse\\\": (0, 2),\\n    \\\"moderate\\\": (2, 10),\\n    \\\"rich\\\": (10, float(\\\"inf\\\")),\\n}\\n\\nNEG_DIFFICULTY_QUARTILE_LABELS = [\\\"Q1_easy\\\", \\\"Q2\\\", \\\"Q3\\\", \\\"Q4_hard\\\"]\\n\\n\\ndef _bin_value(value, bins):\\n    for name, (lo, hi) in bins.items():\\n        if lo <= value < hi:\\n            return name\\n    return \\\"unknown\\\"\\n\\n\\n# ── M1 metadata ───────────────────────────────────────────────────��─\\n\\ndef load_m1_metadata(m1_path: str) -> Tuple[Dict[str, str], Dict[str, int]]:\\n    import re\\n    inst_to_repo = {}\\n    repo_counts: Counter = Counter()\\n    pat_iid = re.compile(r'\\\"instance_id\\\"\\\\s*:\\\\s*\\\"([^\\\"]+)\\\"')\\n    pat_repo = re.compile(r'\\\"repo\\\"\\\\s*:\\\\s*\\\"([^\\\"]+)\\\"')\\n    with open(m1_path) as f:\\n        for line in f:\\n            m_iid = pat_iid.search(line)\\n            m_repo = pat_repo.search(line)\\n            if m_iid and m_repo:\\n                iid = m_iid.group(1)\\n                repo = m_repo.group(1)\\n                inst_to_repo[iid] = repo\\n                repo_counts[repo] += 1\\n    return inst_to_repo, dict(repo_counts)\\n\\n\\n# ── Dataflow graph loading ────────────────────────────────────────────\\n\\ndef load_dataflow_edges(graph_path: str) -> Dict[str, int]:\\n    \\\"\\\"\\\"Load dataflow graph and return {file_key: edge_count}.\\\"\\\"\\\"\\n    with open(graph_path) as f:\\n        graph = json.load(f)\\n    return {k: len(v) for k, v in graph.items()}\\n\\n\\n# ── Val data loading ─────────────────────────────────────────────────\\n\\ndef load_val_samples(val_path: str, lite: bool = False) -> List[Dict[str, Any]]:\\n    \\\"\\\"\\\"Load val JSONL. lite=True skips candidate_tokens (faster for dry-run).\\\"\\\"\\\"\\n    import re\\n    samples = []\\n    pat_qid = re.compile(r'\\\"query_id\\\"\\\\s*:\\\\s*\\\"([^\\\"]+)\\\"')\\n    with open(val_path) as f:\\n        for line in f:\\n            if not line.strip():\\n                continue\\n            if lite:\\n                m = pat_qid.search(line)\\n                if not m:\\n                    continue\\n                qid = m.group(1)\\n                instance_id = qid.split(\\\"::\\\")[0] if \\\"::\\\" in qid else qid\\n                d = json.loads(line)\\n                samples.append({\\n                    \\\"query_id\\\": qid,\\n                    \\\"instance_id\\\": instance_id,\\n                    \\\"pool_size\\\": len(d.get(\\\"neg_candidates\\\", [])),\\n                    \\\"query_tokens\\\": d.get(\\\"query_tokens\\\", \\\"\\\")[:1000],\\n                    \\\"pos_tokens\\\": d.get(\\\"pos_tokens\\\", \\\"\\\")[:1000],\\n                    \\\"neg_candidates\\\": [],\\n                    \\\"candidate_tokens\\\": {},\\n                })\\n            else:\\n                d = jso\\n\\n... [截断: 输出过长，省略 1039 字符] ...\\n\\nmax_seq_length: int = 2048,\\n) -> List[Dict]:\\n    import torch\\n    from transformers import AutoTokenizer\\n\\n    train_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), \\\"..\\\", \\\"training\\\")\\n    if train_dir not in sys.path:\\n        sys.path.insert(0, train_dir)\\n    from contrastive_model import StructFuseEncoder\\n\\n    config_path = os.path.join(checkpoint_dir, \\\"training_config.json\\\")\\n    with open(config_path) as f:\\n        config = json.load(f)\\n\\n    model_name = config.get(\\\"model_name\\\", \\\"Qwen/Qwen2.5-Coder-3B\\\")\\n    tokenizer = AutoTokenizer.from_pretrained(checkpoint_dir, trust_remote_code=True)\\n\\n    model = StructFuseEncoder(\\n        model_name=model_name,\\n        proj_dim=config.get(\\\"proj_dim\\\", 256),\\n        use_projection=True,\\n        use_lora=config.get(\\\"use_lora\\\", False),\\n        lora_r=config.get(\\\"lora_r\\\", 16),\\n        use_fusion_head=config.get(\\\"use_fusion_head\\\", False),\\n    )\\n    state_dict = torch.load(os.path.join(checkpoint_dir, \\\"model.pt\\\"), map_location=\\\"cpu\\\")\\n    model.load_state_dict(state_dict, strict=False)\\n    model = model.to(device).eval()\\n\\n    results = []\\n    with torch.no_grad():\\n        for i, sample in enumerate(val_samples):\\n            if (i + 1) % 200 == 0:\\n                print(f\\\"  re-eval {i+1}/{len(val_samples)}\\\", flush=True)\\n\\n            def _encode(text):\\n                enc = tokenizer(text, truncation=True, max_length=max_seq_length,\\n                                padding=True, return_tensors=\\\"pt\\\")\\n                enc = {k: v.to(device) for k, v in enc.items()}\\n                return model.encode(enc[\\\"input_ids\\\"], enc[\\\"attention_mask\\\"])\\n\\n            q_emb = _encode(sample[\\\"query_tokens\\\"])\\n            p_emb = _encode(sample[\\\"pos_tokens\\\"])\\n            pos_sim = (q_emb * p_emb).sum().item()\\n\\n            neg_sims = []\\n            for neg_id in sample[\\\"neg_candidates\\\"]:\\n                neg_text = sample[\\\"candidate_tokens\\\"].get(neg_id, \\\"\\\")\\n                if not neg_text:\\n                    continue\\n                n_emb = _encode(neg_text)\\n                neg_sims.append((q_emb * n_emb).sum().item())\\n\\n            rank = 1 + sum(1 for s in neg_sims if s >= pos_sim)\\n\\n            results.append({\\n                \\\"query_id\\\": sample[\\\"query_id\\\"],\\n                \\\"instance_id\\\": sample[\\\"instance_id\\\"],\\n                \\\"pool_size\\\": sample[\\\"pool_size\\\"],\\n                \\\"rank\\\": rank,\\n                \\\"pos_sim\\\": pos_sim,\\n                \\\"total_candidates\\\": 1 + len(neg_sims),\\n            })\\n\\n    del model\\n    if torch.cuda.is_available():\\n        torch.cuda.empty_cache()\\n    return results\\n\\n\\n# ── Predictions loading ──────────────────────────────────────────────\\n\\ndef load_predictions(pred_file: str, val_samples: List[Dict]) -> List[Dict]:\\n    \\\"\\\"\\\"Load predictions from eval_retrieval.py output format.\\\"\\\"\\\"\\n    with open(pred_file) as f:\\n        data = json.load(f)\\n\\n    per_inst = {}\\n    results_list = data.get(\\\"results\\\", [data]) if \\\"results\\\" in data else [data]\\n    for r in results_list:\\n        for pi in r.get(\\\"per_instance\\\", []):\\n            per_inst[pi[\\\"instance_id\\\"]] = pi\\n\\n    val_lookup = {s[\\\"query_id\\\"]: s for s in val_samples}\\n    results = []\\n    for sample in val_samples:\\n        iid = sample[\\\"instance_id\\\"]\\n        pred = per_inst.get(iid)\\n        if pred is None:\\n            continue\\n        gold = set(pred.get(\\\"gold_files\\\", []))\\n        predicted = pred.get(\\\"predicted_top10\\\", [])\\n        rank = len(predicted) + 1\\n        for j, pf in enumerate(predicted):\\n            if pf in gold:\\n                rank = j + 1\\n                break\\n        results.append({\\n            \\\"query_id\\\": sample[\\\"query_id\\\"],\\n            \\\"instance_id\\\": iid,\\n            \\\"pool_size\\\": sample[\\\"pool_size\\\"],\\n            \\\"rank\\\": rank,\\n            \\\"pos_sim\\\": pred.get(\\\"scores_top10\\\", [0.0])[0] if pred.get(\\\"scores_top10\\\") else 0.0,\\n            \\\"total_candidates\\\": max(len(predicted), sample[\\\"pool_size\\\"] + 1),\\n        })\\n    return results\\n\\n\\n# ── Mock predictions (dry-run) ───────────────────────────────────────\\n\\ndef mock_predictions(\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"
    }
  },
  "sourceToolAssistantUUID": "6f64f635-9dc8-4767-ae58-b093b89db92b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "bda3dfbf-4b90-494d-b674-2597173fd381",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 58_

```json
{
  "type": "last-prompt",
  "leafUuid": "f9016569-26c2-4229-a760-83c5888893bb",
  "sessionId": "bda3dfbf-4b90-494d-b674-2597173fd381"
}
```

---

### Runtime record

_source line 59_

```json
{
  "type": "ai-title",
  "aiTitle": "Add pool-size controlled stratified evaluation to analysis script",
  "sessionId": "bda3dfbf-4b90-494d-b674-2597173fd381"
}
```

---

### Assistant

_source line 60 · 2026-05-14T20:47:37.696Z_

<details><summary>Logged reasoning block</summary>

```text
Good, now I have load_predictions (lines 230-268) and all the key pieces. Now let me get the remaining truncated sections - `make_plots` heatmap continuation and `write_summary_csv`, and early `main`.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f9016569-26c2-4229-a760-83c5888893bb",
  "isSidechain": false,
  "requestId": "req_011Cb37mnhHPiTRGovxVcG2n",
  "type": "assistant",
  "uuid": "7283a93b-ef5a-4581-91d2-6ab4d6b2f6dc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "bda3dfbf-4b90-494d-b674-2597173fd381",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015PDpHdSwuRdttMR1GGSHax",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3671,
      "cache_read_input_tokens": 50861,
      "output_tokens": 191,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3671,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 191,
          "cache_read_input_tokens": 50861,
          "cache_creation_input_tokens": 3671,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3671
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

_source line 61 · 2026-05-14T20:47:38.370Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01RFLkcebvZiwZb2M9XmnvnL`</summary>

```json
{
  "server": "bjb1-42106",
  "command": "tail -n +570 /root/structfuse/evaluation/analyze_stratified.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7283a93b-ef5a-4581-91d2-6ab4d6b2f6dc",
  "isSidechain": false,
  "requestId": "req_011Cb37mnhHPiTRGovxVcG2n",
  "type": "assistant",
  "uuid": "2238b031-4f33-4075-8024-f0f6f1ea7394",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "bda3dfbf-4b90-494d-b674-2597173fd381",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015PDpHdSwuRdttMR1GGSHax",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3671,
      "cache_read_input_tokens": 50861,
      "output_tokens": 191,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3671,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 191,
          "cache_read_input_tokens": 50861,
          "cache_creation_input_tokens": 3671,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3671
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

_source line 62 · 2026-05-14T20:47:38.769Z_

<details><summary>↩ Tool result · `toolu_01RFLkcebvZiwZb2M9XmnvnL`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"                continue\\n\\n            data_matrix = []\\n            for b in bins_present:\\n                row = []\\n                for s in STRATEGIES:\\n                    row.append(analysis[b].get(s, {}).get(\\\"R@1\\\", 0))\\n                data_matrix.append(row)\\n            data_matrix = np.array(data_matrix)\\n\\n            fig, ax = plt.subplots(figsize=(6, max(3, len(bins_present) * 0.8 + 1)))\\n            im = ax.imshow(data_matrix, cmap=\\\"YlOrRd\\\", aspect=\\\"auto\\\", vmin=0)\\n            ax.set_xticks(range(len(STRATEGIES)))\\n            ax.set_xticklabels([STRATEGY_LABELS[s] for s in STRATEGIES])\\n            ax.set_yticks(range(len(bins_present)))\\n            ax.set_yticklabels(bins_present)\\n            ax.set_title(f\\\"R@1 Heatmap — {title}\\\", fontweight=\\\"bold\\\")\\n\\n            for i in range(len(bins_present)):\\n                for j in range(len(STRATEGIES)):\\n                    val = data_matrix[i, j]\\n                    color = \\\"white\\\" if val > data_matrix.max() * 0.6 else \\\"black\\\"\\n                    ax.text(j, i, f\\\"{val:.3f}\\\", ha=\\\"center\\\", va=\\\"center\\\",\\n                            color=color, fontsize=10, fontweight=\\\"bold\\\")\\n\\n            fig.colorbar(im, ax=ax, shrink=0.8)\\n            plt.tight_layout()\\n            pdf.savefig(fig, bbox_inches=\\\"tight\\\")\\n            plt.close(fig)\\n\\n        # ── Plot 3: Delta trends ──\\n        delta_dims = [\\n            (\\\"Repo Size\\\", repo_analysis, list(REPO_SIZE_BINS.keys())),\\n            (\\\"Pool Size\\\", pool_analysis, list(POOL_SIZE_BINS.keys())),\\n            (\\\"Similarity\\\", sim_analysis, list(SIMILARITY_BINS.keys())),\\n        ]\\n        if dataflow_analysis:\\n            delta_dims.append((\\\"Dataflow\\\", dataflow_analysis, list(DATAFLOW_BINS.keys())))\\n        if neg_diff_analysis:\\n            delta_dims.append((\\\"Neg Difficulty\\\", neg_diff_analysis, NEG_DIFFICULTY_QUARTILE_LABELS))\\n        for title, analysis, bin_order in delta_dims:\\n            bins_present = [b for b in bin_order if b in analysis]\\n            if not bins_present:\\n                continue\\n\\n            fig, ax = plt.subplots(figsize=(8, 5))\\n            x = np.arange(len(bins_present))\\n\\n            for other, color, marker in [\\n                (\\\"embedding_distance\\\", \\\"#DD8452\\\", \\\"o\\\"),\\n                (\\\"dataflow_aware\\\", \\\"#55A868\\\", \\\"s\\\"),\\n            ]:\\n                delta_key = f\\\"{other}_vs_random\\\"\\n                deltas = []\\n                for b in bins_present:\\n                    d = analysis[b].get(delta_key, {}).get(\\\"R@1_delta\\\", 0)\\n                    deltas.append(d)\\n\\n                ax.plot(x, deltas, marker=marker, linewidth=2, markersize=8,\\n                        color=color, label=f\\\"{STRATEGY_LABELS[other]} - Random\\\")\\n\\n            ax.axhline(y=0, color=\\\"gray\\\", linestyle=\\\"--\\\", linewidth=0.8)\\n            ax.set_xlabel(title)\\n            ax.set_ylabel(\\\"R@1 Delta (vs Random)\\\")\\n            ax.set_title(f\\\"R@1 Delta Trend — {title}\\\", fontweight=\\\"bold\\\")\\n            ax.set_xticks(x)\\n            ax.set_xticklabels(bins_present)\\n            ax.legend(loc=\\\"best\\\")\\n            plt.tight_layout()\\n            pdf.savefig(fig, bbox_inches=\\\"tight\\\")\\n            plt.close(fig)\\n\\n    # Also save individual PNGs\\n    print(f\\\"  Plots saved to {pdf_path}\\\", flush=True)\\n    return pdf_path\\n\\n\\n# ── CSV output ───────────────────────────────────────────────────────\\n\\ndef write_summary_csv(\\n    repo_analysis: Dict,\\n    pool_analysis: Dict,\\n    sim_analysis: Dict,\\n    output_path: str,\\n    dataflow_analysis: Optional[Dict] = None,\\n    neg_diff_analysis: Optional[Dict] = None,\\n):\\n    rows = []\\n    dimensions = [\\n        (\\\"repo_size\\\", repo_analysis, list(REPO_SIZE_BINS.keys())),\\n        (\\\"pool_size\\\", pool_analysis, list(POOL_SIZE_BINS.keys())),\\n        (\\\"similarity\\\", sim_analysis, list(SIMILARITY_BINS.keys())),\\n    ]\\n    if dataflow_analysis:\\n        dimensions.append((\\\"dataflow\\\", dataflow_analysis, list(DATAFLOW_BINS.keys())))\\n    if neg_diff_analysis:\\n        dimensions.append((\\\"neg_difficulty\\\", neg_diff_analysis, NEG_DIFFICULTY_QUARTILE_LABELS))\\n    for dim_name, analy\\n\\n... [截断: 输出过长，省略 7042 字符] ...\\n\\nt\\\")):\\n                        ckpt_dir = candidate\\n                        break\\n                if ckpt_dir is None and os.path.exists(os.path.join(base, \\\"model.pt\\\")):\\n                    ckpt_dir = base\\n                if os.path.exists(ckpt_dir):\\n                    print(f\\\"  Re-evaluating checkpoint: {ckpt_dir}\\\", flush=True)\\n                    results = reeval_checkpoint(\\n                        ckpt_dir, val_samples, args.device, args.max_seq_length\\n                    )\\n                else:\\n                    print(f\\\"  [WARN] Checkpoint not found: {ckpt_dir}\\\", flush=True)\\n                    continue\\n            else:\\n                print(\\\"  [ERROR] No --dry-run, --predictions-dir, or --checkpoints-dir\\\", flush=True)\\n                continue\\n\\n            # Assign strata\\n            results = assign_strata(results, inst_to_repo, repo_counts, dataflow_edges)\\n\\n            # For dry-run or model-based: compute text similarity for sim_bin\\n            if args.dry_run:\\n                for r, s in zip(results, val_samples):\\n                    tsim = text_similarity(s[\\\"query_tokens\\\"][:500], s[\\\"pos_tokens\\\"][:500])\\n                    r[\\\"sim_bin\\\"] = _bin_value(tsim, SIMILARITY_BINS)\\n\\n            all_results[strategy][seed] = results\\n            val_samples_cache[f\\\"{strategy}_s{seed}\\\"] = val_samples\\n            print(f\\\"  -> {len(results)} instances\\\", flush=True)\\n\\n    # Compute neg_difficulty quartiles (text-overlap proxy, CPU-safe)\\n    print(\\\"Computing neg difficulty quartiles...\\\", flush=True)\\n    assign_neg_difficulty_quartiles(all_results, val_samples_cache)\\n\\n    # Run stratified analysis\\n    print(\\\"\\\\nRunning stratified analysis...\\\", flush=True)\\n    repo_analysis = run_stratified_analysis(\\n        all_results, \\\"repo_size_bin\\\", list(REPO_SIZE_BINS.keys()), args.n_bootstrap\\n    )\\n    pool_analysis = run_stratified_analysis(\\n        all_results, \\\"pool_size_bin\\\", list(POOL_SIZE_BINS.keys()), args.n_bootstrap\\n    )\\n    sim_analysis = run_stratified_analysis(\\n        all_results, \\\"sim_bin\\\", list(SIMILARITY_BINS.keys()), args.n_bootstrap\\n    )\\n\\n    dataflow_analysis = {}\\n    if dataflow_edges is not None:\\n        dataflow_analysis = run_stratified_analysis(\\n            all_results, \\\"dataflow_bin\\\", list(DATAFLOW_BINS.keys()), args.n_bootstrap\\n        )\\n\\n    neg_diff_analysis = run_stratified_analysis(\\n        all_results, \\\"neg_difficulty_bin\\\", NEG_DIFFICULTY_QUARTILE_LABELS, args.n_bootstrap\\n    )\\n\\n    # Save JSON\\n    full_results = {\\n        \\\"config\\\": {\\n            \\\"strategies\\\": STRATEGIES,\\n            \\\"seeds\\\": seeds,\\n            \\\"repo_size_bins\\\": {k: list(v) for k, v in REPO_SIZE_BINS.items()},\\n            \\\"pool_size_bins\\\": {k: list(v) for k, v in POOL_SIZE_BINS.items()},\\n            \\\"similarity_bins\\\": {k: list(v) for k, v in SIMILARITY_BINS.items()},\\n            \\\"dataflow_bins\\\": {k: list(v) for k, v in DATAFLOW_BINS.items()},\\n            \\\"neg_difficulty_quartiles\\\": NEG_DIFFICULTY_QUARTILE_LABELS,\\n            \\\"n_bootstrap\\\": args.n_bootstrap,\\n            \\\"dry_run\\\": args.dry_run,\\n        },\\n        \\\"by_repo_size\\\": repo_analysis,\\n        \\\"by_pool_size\\\": pool_analysis,\\n        \\\"by_similarity\\\": sim_analysis,\\n        \\\"by_dataflow\\\": dataflow_analysis,\\n        \\\"by_neg_difficulty\\\": neg_diff_analysis,\\n    }\\n\\n    json_path = os.path.join(args.output_dir, \\\"stratified_results.json\\\")\\n    with open(json_path, \\\"w\\\") as f:\\n        json.dump(full_results, f, indent=2, ensure_ascii=False)\\n    print(f\\\"  Results JSON saved to {json_path}\\\", flush=True)\\n\\n    # CSV summary\\n    csv_path = os.path.join(args.output_dir, \\\"stratified_summary.csv\\\")\\n    write_summary_csv(repo_analysis, pool_analysis, sim_analysis, csv_path, dataflow_analysis, neg_diff_analysis)\\n\\n    # Plots\\n    try:\\n        make_plots(repo_analysis, pool_analysis, sim_analysis, args.output_dir, dataflow_analysis, neg_diff_analysis)\\n    except Exception as e:\\n        print(f\\\"  [WARN] Plot generation failed: {e}\\\", flush=True)\\n\\n    print(\\\"\\\\nDone.\\\", flush=True)\\n\\n\\nif __name__ == \\\"__main__\\\":\\n    main()\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.39}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2238b031-4f33-4075-8024-f0f6f1ea7394",
  "isSidechain": false,
  "promptId": "22ffd1fb-240e-481f-9bcc-b3f6a42d6805",
  "type": "user",
  "uuid": "ea0686c2-355f-47cf-93d5-e21e9f7d81be",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"                continue\\\\n\\\\n            data_matrix = []\\\\n            for b in bins_present:\\\\n                row = []\\\\n                for s in STRATEGIES:\\\\n                    row.append(analysis[b].get(s, {}).get(\\\\\\\"R@1\\\\\\\", 0))\\\\n                data_matrix.append(row)\\\\n            data_matrix = np.array(data_matrix)\\\\n\\\\n            fig, ax = plt.subplots(figsize=(6, max(3, len(bins_present) * 0.8 + 1)))\\\\n            im = ax.imshow(data_matrix, cmap=\\\\\\\"YlOrRd\\\\\\\", aspect=\\\\\\\"auto\\\\\\\", vmin=0)\\\\n            ax.set_xticks(range(len(STRATEGIES)))\\\\n            ax.set_xticklabels([STRATEGY_LABELS[s] for s in STRATEGIES])\\\\n            ax.set_yticks(range(len(bins_present)))\\\\n            ax.set_yticklabels(bins_present)\\\\n            ax.set_title(f\\\\\\\"R@1 Heatmap — {title}\\\\\\\", fontweight=\\\\\\\"bold\\\\\\\")\\\\n\\\\n            for i in range(len(bins_present)):\\\\n                for j in range(len(STRATEGIES)):\\\\n                    val = data_matrix[i, j]\\\\n                    color = \\\\\\\"white\\\\\\\" if val > data_matrix.max() * 0.6 else \\\\\\\"black\\\\\\\"\\\\n                    ax.text(j, i, f\\\\\\\"{val:.3f}\\\\\\\", ha=\\\\\\\"center\\\\\\\", va=\\\\\\\"center\\\\\\\",\\\\n                            color=color, fontsize=10, fontweight=\\\\\\\"bold\\\\\\\")\\\\n\\\\n            fig.colorbar(im, ax=ax, shrink=0.8)\\\\n            plt.tight_layout()\\\\n            pdf.savefig(fig, bbox_inches=\\\\\\\"tight\\\\\\\")\\\\n            plt.close(fig)\\\\n\\\\n        # ── Plot 3: Delta trends ──\\\\n        delta_dims = [\\\\n            (\\\\\\\"Repo Size\\\\\\\", repo_analysis, list(REPO_SIZE_BINS.keys())),\\\\n            (\\\\\\\"Pool Size\\\\\\\", pool_analysis, list(POOL_SIZE_BINS.keys())),\\\\n            (\\\\\\\"Similarity\\\\\\\", sim_analysis, list(SIMILARITY_BINS.keys())),\\\\n        ]\\\\n        if dataflow_analysis:\\\\n            delta_dims.append((\\\\\\\"Dataflow\\\\\\\", dataflow_analysis, list(DATAFLOW_BINS.keys())))\\\\n        if neg_diff_analysis:\\\\n            delta_dims.append((\\\\\\\"Neg Difficulty\\\\\\\", neg_diff_analysis, NEG_DIFFICULTY_QUARTILE_LABELS))\\\\n        for title, analysis, bin_order in delta_dims:\\\\n            bins_present = [b for b in bin_order if b in analysis]\\\\n            if not bins_present:\\\\n                continue\\\\n\\\\n            fig, ax = plt.subplots(figsize=(8, 5))\\\\n            x = np.arange(len(bins_present))\\\\n\\\\n            for other, color, marker in [\\\\n                (\\\\\\\"embedding_distance\\\\\\\", \\\\\\\"#DD8452\\\\\\\", \\\\\\\"o\\\\\\\"),\\\\n                (\\\\\\\"dataflow_aware\\\\\\\", \\\\\\\"#55A868\\\\\\\", \\\\\\\"s\\\\\\\"),\\\\n            ]:\\\\n                delta_key = f\\\\\\\"{other}_vs_random\\\\\\\"\\\\n                deltas = []\\\\n                for b in bins_present:\\\\n                    d = analysis[b].get(delta_key, {}).get(\\\\\\\"R@1_delta\\\\\\\", 0)\\\\n                    deltas.append(d)\\\\n\\\\n                ax.plot(x, deltas, marker=marker, linewidth=2, markersize=8,\\\\n                        color=color, label=f\\\\\\\"{STRATEGY_LABELS[other]} - Random\\\\\\\")\\\\n\\\\n            ax.axhline(y=0, color=\\\\\\\"gray\\\\\\\", linestyle=\\\\\\\"--\\\\\\\", linewidth=0.8)\\\\n            ax.set_xlabel(title)\\\\n            ax.set_ylabel(\\\\\\\"R@1 Delta (vs Random)\\\\\\\")\\\\n            ax.set_title(f\\\\\\\"R@1 Delta Trend — {title}\\\\\\\", fontweight=\\\\\\\"bold\\\\\\\")\\\\n            ax.set_xticks(x)\\\\n            ax.set_xticklabels(bins_present)\\\\n            ax.legend(loc=\\\\\\\"best\\\\\\\")\\\\n            plt.tight_layout()\\\\n            pdf.savefig(fig, bbox_inches=\\\\\\\"tight\\\\\\\")\\\\n            plt.close(fig)\\\\n\\\\n    # Also save individual PNGs\\\\n    print(f\\\\\\\"  Plots saved to {pdf_path}\\\\\\\", flush=True)\\\\n    return pdf_path\\\\n\\\\n\\\\n# ── CSV output ───────────────────────────────────────────────────────\\\\n\\\\ndef write_summary_csv(\\\\n    repo_analysis: Dict,\\\\n    pool_analysis: Dict,\\\\n    sim_analysis: Dict,\\\\n    output_path: str,\\\\n    dataflow_analysis: Optional[Dict] = None,\\\\n    neg_diff_analysis: Optional[Dict] = None,\\\\n):\\\\n    rows = []\\\\n    dimensions = [\\\\n        (\\\\\\\"repo_size\\\\\\\", repo_analysis, list(REPO_SIZE_BINS.keys())),\\\\n        (\\\\\\\"pool_size\\\\\\\", pool_analysis, list(POOL_SIZE_BINS.keys())),\\\\n        (\\\\\\\"similarity\\\\\\\", sim_analysis, list(SIMILARITY_BINS.keys())),\\\\n    ]\\\\n    if dataflow_analysis:\\\\n        dimensions.append((\\\\\\\"dataflow\\\\\\\", dataflow_analysis, list(DATAFLOW_BINS.keys())))\\\\n    if neg_diff_analysis:\\\\n        dimensions.append((\\\\\\\"neg_difficulty\\\\\\\", neg_diff_analysis, NEG_DIFFICULTY_QUARTILE_LABELS))\\\\n    for dim_name, analy\\\\n\\\\n... [截断: 输出过长，省略 7042 字符] ...\\\\n\\\\nt\\\\\\\")):\\\\n                        ckpt_dir = candidate\\\\n                        break\\\\n                if ckpt_dir is None and os.path.exists(os.path.join(base, \\\\\\\"model.pt\\\\\\\")):\\\\n                    ckpt_dir = base\\\\n                if os.path.exists(ckpt_dir):\\\\n                    print(f\\\\\\\"  Re-evaluating checkpoint: {ckpt_dir}\\\\\\\", flush=True)\\\\n                    results = reeval_checkpoint(\\\\n                        ckpt_dir, val_samples, args.device, args.max_seq_length\\\\n                    )\\\\n                else:\\\\n                    print(f\\\\\\\"  [WARN] Checkpoint not found: {ckpt_dir}\\\\\\\", flush=True)\\\\n                    continue\\\\n            else:\\\\n                print(\\\\\\\"  [ERROR] No --dry-run, --predictions-dir, or --checkpoints-dir\\\\\\\", flush=True)\\\\n                continue\\\\n\\\\n            # Assign strata\\\\n            results = assign_strata(results, inst_to_repo, repo_counts, dataflow_edges)\\\\n\\\\n            # For dry-run or model-based: compute text similarity for sim_bin\\\\n            if args.dry_run:\\\\n                for r, s in zip(results, val_samples):\\\\n                    tsim = text_similarity(s[\\\\\\\"query_tokens\\\\\\\"][:500], s[\\\\\\\"pos_tokens\\\\\\\"][:500])\\\\n                    r[\\\\\\\"sim_bin\\\\\\\"] = _bin_value(tsim, SIMILARITY_BINS)\\\\n\\\\n            all_results[strategy][seed] = results\\\\n            val_samples_cache[f\\\\\\\"{strategy}_s{seed}\\\\\\\"] = val_samples\\\\n            print(f\\\\\\\"  -> {len(results)} instances\\\\\\\", flush=True)\\\\n\\\\n    # Compute neg_difficulty quartiles (text-overlap proxy, CPU-safe)\\\\n    print(\\\\\\\"Computing neg difficulty quartiles...\\\\\\\", flush=True)\\\\n    assign_neg_difficulty_quartiles(all_results, val_samples_cache)\\\\n\\\\n    # Run stratified analysis\\\\n    print(\\\\\\\"\\\\\\\\nRunning stratified analysis...\\\\\\\", flush=True)\\\\n    repo_analysis = run_stratified_analysis(\\\\n        all_results, \\\\\\\"repo_size_bin\\\\\\\", list(REPO_SIZE_BINS.keys()), args.n_bootstrap\\\\n    )\\\\n    pool_analysis = run_stratified_analysis(\\\\n        all_results, \\\\\\\"pool_size_bin\\\\\\\", list(POOL_SIZE_BINS.keys()), args.n_bootstrap\\\\n    )\\\\n    sim_analysis = run_stratified_analysis(\\\\n        all_results, \\\\\\\"sim_bin\\\\\\\", list(SIMILARITY_BINS.keys()), args.n_bootstrap\\\\n    )\\\\n\\\\n    dataflow_analysis = {}\\\\n    if dataflow_edges is not None:\\\\n        dataflow_analysis = run_stratified_analysis(\\\\n            all_results, \\\\\\\"dataflow_bin\\\\\\\", list(DATAFLOW_BINS.keys()), args.n_bootstrap\\\\n        )\\\\n\\\\n    neg_diff_analysis = run_stratified_analysis(\\\\n        all_results, \\\\\\\"neg_difficulty_bin\\\\\\\", NEG_DIFFICULTY_QUARTILE_LABELS, args.n_bootstrap\\\\n    )\\\\n\\\\n    # Save JSON\\\\n    full_results = {\\\\n        \\\\\\\"config\\\\\\\": {\\\\n            \\\\\\\"strategies\\\\\\\": STRATEGIES,\\\\n            \\\\\\\"seeds\\\\\\\": seeds,\\\\n            \\\\\\\"repo_size_bins\\\\\\\": {k: list(v) for k, v in REPO_SIZE_BINS.items()},\\\\n            \\\\\\\"pool_size_bins\\\\\\\": {k: list(v) for k, v in POOL_SIZE_BINS.items()},\\\\n            \\\\\\\"similarity_bins\\\\\\\": {k: list(v) for k, v in SIMILARITY_BINS.items()},\\\\n            \\\\\\\"dataflow_bins\\\\\\\": {k: list(v) for k, v in DATAFLOW_BINS.items()},\\\\n            \\\\\\\"neg_difficulty_quartiles\\\\\\\": NEG_DIFFICULTY_QUARTILE_LABELS,\\\\n            \\\\\\\"n_bootstrap\\\\\\\": args.n_bootstrap,\\\\n            \\\\\\\"dry_run\\\\\\\": args.dry_run,\\\\n        },\\\\n        \\\\\\\"by_repo_size\\\\\\\": repo_analysis,\\\\n        \\\\\\\"by_pool_size\\\\\\\": pool_analysis,\\\\n        \\\\\\\"by_similarity\\\\\\\": sim_analysis,\\\\n        \\\\\\\"by_dataflow\\\\\\\": dataflow_analysis,\\\\n        \\\\\\\"by_neg_difficulty\\\\\\\": neg_diff_analysis,\\\\n    }\\\\n\\\\n    json_path = os.path.join(args.output_dir, \\\\\\\"stratified_results.json\\\\\\\")\\\\n    with open(json_path, \\\\\\\"w\\\\\\\") as f:\\\\n        json.dump(full_results, f, indent=2, ensure_ascii=False)\\\\n    print(f\\\\\\\"  Results JSON saved to {json_path}\\\\\\\", flush=True)\\\\n\\\\n    # CSV summary\\\\n    csv_path = os.path.join(args.output_dir, \\\\\\\"stratified_summary.csv\\\\\\\")\\\\n    write_summary_csv(repo_analysis, pool_analysis, sim_analysis, csv_path, dataflow_analysis, neg_diff_analysis)\\\\n\\\\n    # Plots\\\\n    try:\\\\n        make_plots(repo_analysis, pool_analysis, sim_analysis, args.output_dir, dataflow_analysis, neg_diff_analysis)\\\\n    except Exception as e:\\\\n        print(f\\\\\\\"  [WARN] Plot generation failed: {e}\\\\\\\", flush=True)\\\\n\\\\n    print(\\\\\\\"\\\\\\\\nDone.\\\\\\\", flush=True)\\\\n\\\\n\\\\nif __name__ == \\\\\\\"__main__\\\\\\\":\\\\n    main()\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.39}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"                continue\\n\\n            data_matrix = []\\n            for b in bins_present:\\n                row = []\\n                for s in STRATEGIES:\\n                    row.append(analysis[b].get(s, {}).get(\\\"R@1\\\", 0))\\n                data_matrix.append(row)\\n            data_matrix = np.array(data_matrix)\\n\\n            fig, ax = plt.subplots(figsize=(6, max(3, len(bins_present) * 0.8 + 1)))\\n            im = ax.imshow(data_matrix, cmap=\\\"YlOrRd\\\", aspect=\\\"auto\\\", vmin=0)\\n            ax.set_xticks(range(len(STRATEGIES)))\\n            ax.set_xticklabels([STRATEGY_LABELS[s] for s in STRATEGIES])\\n            ax.set_yticks(range(len(bins_present)))\\n            ax.set_yticklabels(bins_present)\\n            ax.set_title(f\\\"R@1 Heatmap — {title}\\\", fontweight=\\\"bold\\\")\\n\\n            for i in range(len(bins_present)):\\n                for j in range(len(STRATEGIES)):\\n                    val = data_matrix[i, j]\\n                    color = \\\"white\\\" if val > data_matrix.max() * 0.6 else \\\"black\\\"\\n                    ax.text(j, i, f\\\"{val:.3f}\\\", ha=\\\"center\\\", va=\\\"center\\\",\\n                            color=color, fontsize=10, fontweight=\\\"bold\\\")\\n\\n            fig.colorbar(im, ax=ax, shrink=0.8)\\n            plt.tight_layout()\\n            pdf.savefig(fig, bbox_inches=\\\"tight\\\")\\n            plt.close(fig)\\n\\n        # ── Plot 3: Delta trends ──\\n        delta_dims = [\\n            (\\\"Repo Size\\\", repo_analysis, list(REPO_SIZE_BINS.keys())),\\n            (\\\"Pool Size\\\", pool_analysis, list(POOL_SIZE_BINS.keys())),\\n            (\\\"Similarity\\\", sim_analysis, list(SIMILARITY_BINS.keys())),\\n        ]\\n        if dataflow_analysis:\\n            delta_dims.append((\\\"Dataflow\\\", dataflow_analysis, list(DATAFLOW_BINS.keys())))\\n        if neg_diff_analysis:\\n            delta_dims.append((\\\"Neg Difficulty\\\", neg_diff_analysis, NEG_DIFFICULTY_QUARTILE_LABELS))\\n        for title, analysis, bin_order in delta_dims:\\n            bins_present = [b for b in bin_order if b in analysis]\\n            if not bins_present:\\n                continue\\n\\n            fig, ax = plt.subplots(figsize=(8, 5))\\n            x = np.arange(len(bins_present))\\n\\n            for other, color, marker in [\\n                (\\\"embedding_distance\\\", \\\"#DD8452\\\", \\\"o\\\"),\\n                (\\\"dataflow_aware\\\", \\\"#55A868\\\", \\\"s\\\"),\\n            ]:\\n                delta_key = f\\\"{other}_vs_random\\\"\\n                deltas = []\\n                for b in bins_present:\\n                    d = analysis[b].get(delta_key, {}).get(\\\"R@1_delta\\\", 0)\\n                    deltas.append(d)\\n\\n                ax.plot(x, deltas, marker=marker, linewidth=2, markersize=8,\\n                        color=color, label=f\\\"{STRATEGY_LABELS[other]} - Random\\\")\\n\\n            ax.axhline(y=0, color=\\\"gray\\\", linestyle=\\\"--\\\", linewidth=0.8)\\n            ax.set_xlabel(title)\\n            ax.set_ylabel(\\\"R@1 Delta (vs Random)\\\")\\n            ax.set_title(f\\\"R@1 Delta Trend — {title}\\\", fontweight=\\\"bold\\\")\\n            ax.set_xticks(x)\\n            ax.set_xticklabels(bins_present)\\n            ax.legend(loc=\\\"best\\\")\\n            plt.tight_layout()\\n            pdf.savefig(fig, bbox_inches=\\\"tight\\\")\\n            plt.close(fig)\\n\\n    # Also save individual PNGs\\n    print(f\\\"  Plots saved to {pdf_path}\\\", flush=True)\\n    return pdf_path\\n\\n\\n# ── CSV output ───────────────────────────────────────────────────────\\n\\ndef write_summary_csv(\\n    repo_analysis: Dict,\\n    pool_analysis: Dict,\\n    sim_analysis: Dict,\\n    output_path: str,\\n    dataflow_analysis: Optional[Dict] = None,\\n    neg_diff_analysis: Optional[Dict] = None,\\n):\\n    rows = []\\n    dimensions = [\\n        (\\\"repo_size\\\", repo_analysis, list(REPO_SIZE_BINS.keys())),\\n        (\\\"pool_size\\\", pool_analysis, list(POOL_SIZE_BINS.keys())),\\n        (\\\"similarity\\\", sim_analysis, list(SIMILARITY_BINS.keys())),\\n    ]\\n    if dataflow_analysis:\\n        dimensions.append((\\\"dataflow\\\", dataflow_analysis, list(DATAFLOW_BINS.keys())))\\n    if neg_diff_analysis:\\n        dimensions.append((\\\"neg_difficulty\\\", neg_diff_analysis, NEG_DIFFICULTY_QUARTILE_LABELS))\\n    for dim_name, analy\\n\\n... [截断: 输出过长，省略 7042 字符] ...\\n\\nt\\\")):\\n                        ckpt_dir = candidate\\n                        break\\n                if ckpt_dir is None and os.path.exists(os.path.join(base, \\\"model.pt\\\")):\\n                    ckpt_dir = base\\n                if os.path.exists(ckpt_dir):\\n                    print(f\\\"  Re-evaluating checkpoint: {ckpt_dir}\\\", flush=True)\\n                    results = reeval_checkpoint(\\n                        ckpt_dir, val_samples, args.device, args.max_seq_length\\n                    )\\n                else:\\n                    print(f\\\"  [WARN] Checkpoint not found: {ckpt_dir}\\\", flush=True)\\n                    continue\\n            else:\\n                print(\\\"  [ERROR] No --dry-run, --predictions-dir, or --checkpoints-dir\\\", flush=True)\\n                continue\\n\\n            # Assign strata\\n            results = assign_strata(results, inst_to_repo, repo_counts, dataflow_edges)\\n\\n            # For dry-run or model-based: compute text similarity for sim_bin\\n            if args.dry_run:\\n                for r, s in zip(results, val_samples):\\n                    tsim = text_similarity(s[\\\"query_tokens\\\"][:500], s[\\\"pos_tokens\\\"][:500])\\n                    r[\\\"sim_bin\\\"] = _bin_value(tsim, SIMILARITY_BINS)\\n\\n            all_results[strategy][seed] = results\\n            val_samples_cache[f\\\"{strategy}_s{seed}\\\"] = val_samples\\n            print(f\\\"  -> {len(results)} instances\\\", flush=True)\\n\\n    # Compute neg_difficulty quartiles (text-overlap proxy, CPU-safe)\\n    print(\\\"Computing neg difficulty quartiles...\\\", flush=True)\\n    assign_neg_difficulty_quartiles(all_results, val_samples_cache)\\n\\n    # Run stratified analysis\\n    print(\\\"\\\\nRunning stratified analysis...\\\", flush=True)\\n    repo_analysis = run_stratified_analysis(\\n        all_results, \\\"repo_size_bin\\\", list(REPO_SIZE_BINS.keys()), args.n_bootstrap\\n    )\\n    pool_analysis = run_stratified_analysis(\\n        all_results, \\\"pool_size_bin\\\", list(POOL_SIZE_BINS.keys()), args.n_bootstrap\\n    )\\n    sim_analysis = run_stratified_analysis(\\n        all_results, \\\"sim_bin\\\", list(SIMILARITY_BINS.keys()), args.n_bootstrap\\n    )\\n\\n    dataflow_analysis = {}\\n    if dataflow_edges is not None:\\n        dataflow_analysis = run_stratified_analysis(\\n            all_results, \\\"dataflow_bin\\\", list(DATAFLOW_BINS.keys()), args.n_bootstrap\\n        )\\n\\n    neg_diff_analysis = run_stratified_analysis(\\n        all_results, \\\"neg_difficulty_bin\\\", NEG_DIFFICULTY_QUARTILE_LABELS, args.n_bootstrap\\n    )\\n\\n    # Save JSON\\n    full_results = {\\n        \\\"config\\\": {\\n            \\\"strategies\\\": STRATEGIES,\\n            \\\"seeds\\\": seeds,\\n            \\\"repo_size_bins\\\": {k: list(v) for k, v in REPO_SIZE_BINS.items()},\\n            \\\"pool_size_bins\\\": {k: list(v) for k, v in POOL_SIZE_BINS.items()},\\n            \\\"similarity_bins\\\": {k: list(v) for k, v in SIMILARITY_BINS.items()},\\n            \\\"dataflow_bins\\\": {k: list(v) for k, v in DATAFLOW_BINS.items()},\\n            \\\"neg_difficulty_quartiles\\\": NEG_DIFFICULTY_QUARTILE_LABELS,\\n            \\\"n_bootstrap\\\": args.n_bootstrap,\\n            \\\"dry_run\\\": args.dry_run,\\n        },\\n        \\\"by_repo_size\\\": repo_analysis,\\n        \\\"by_pool_size\\\": pool_analysis,\\n        \\\"by_similarity\\\": sim_analysis,\\n        \\\"by_dataflow\\\": dataflow_analysis,\\n        \\\"by_neg_difficulty\\\": neg_diff_analysis,\\n    }\\n\\n    json_path = os.path.join(args.output_dir, \\\"stratified_results.json\\\")\\n    with open(json_path, \\\"w\\\") as f:\\n        json.dump(full_results, f, indent=2, ensure_ascii=False)\\n    print(f\\\"  Results JSON saved to {json_path}\\\", flush=True)\\n\\n    # CSV summary\\n    csv_path = os.path.join(args.output_dir, \\\"stratified_summary.csv\\\")\\n    write_summary_csv(repo_analysis, pool_analysis, sim_analysis, csv_path, dataflow_analysis, neg_diff_analysis)\\n\\n    # Plots\\n    try:\\n        make_plots(repo_analysis, pool_analysis, sim_analysis, args.output_dir, dataflow_analysis, neg_diff_analysis)\\n    except Exception as e:\\n        print(f\\\"  [WARN] Plot generation failed: {e}\\\", flush=True)\\n\\n    print(\\\"\\\\nDone.\\\", flush=True)\\n\\n\\nif __name__ == \\\"__main__\\\":\\n    main()\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.39}}"
    }
  },
  "sourceToolAssistantUUID": "2238b031-4f33-4075-8024-f0f6f1ea7394",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "bda3dfbf-4b90-494d-b674-2597173fd381",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 63_

```json
{
  "type": "last-prompt",
  "leafUuid": "ea0686c2-355f-47cf-93d5-e21e9f7d81be",
  "sessionId": "bda3dfbf-4b90-494d-b674-2597173fd381"
}
```

---

### Runtime record

_source line 64_

```json
{
  "type": "ai-title",
  "aiTitle": "Add pool-size controlled stratified evaluation to analysis script",
  "sessionId": "bda3dfbf-4b90-494d-b674-2597173fd381"
}
```

---

### Assistant

_source line 65 · 2026-05-14T20:47:42.182Z_

<details><summary>Logged reasoning block</summary>

```text
I'm still getting truncated output in the middle. I need to see the `write_summary_csv` body and the beginning of `main()`. Let me try to target exactly those.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ea0686c2-355f-47cf-93d5-e21e9f7d81be",
  "isSidechain": false,
  "requestId": "req_011Cb37n6qvuSPpFCkFM3JDA",
  "type": "assistant",
  "uuid": "91227fba-18ca-45c1-94ee-395b73710b9c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "bda3dfbf-4b90-494d-b674-2597173fd381",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EqeCGp8vwSjREvgMzG18xB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3302,
      "cache_read_input_tokens": 54532,
      "output_tokens": 178,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3302,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 178,
          "cache_read_input_tokens": 54532,
          "cache_creation_input_tokens": 3302,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3302
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

_source line 66 · 2026-05-14T20:47:47.868Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01A3W6MgCkvNCpjvWRRCDrk2`</summary>

```json
{
  "server": "bjb1-42106",
  "command": "tail -n +660 /root/structfuse/evaluation/analyze_stratified.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "91227fba-18ca-45c1-94ee-395b73710b9c",
  "isSidechain": false,
  "requestId": "req_011Cb37n6qvuSPpFCkFM3JDA",
  "type": "assistant",
  "uuid": "80059ebb-0bda-4e93-a91f-0a404f014545",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "bda3dfbf-4b90-494d-b674-2597173fd381",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EqeCGp8vwSjREvgMzG18xB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3302,
      "cache_read_input_tokens": 54532,
      "output_tokens": 178,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3302,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 178,
          "cache_read_input_tokens": 54532,
          "cache_creation_input_tokens": 3302,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3302
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

_source line 67 · 2026-05-14T20:47:48.272Z_

<details><summary>↩ Tool result · `toolu_01A3W6MgCkvNCpjvWRRCDrk2`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"        (\\\"pool_size\\\", pool_analysis, list(POOL_SIZE_BINS.keys())),\\n        (\\\"similarity\\\", sim_analysis, list(SIMILARITY_BINS.keys())),\\n    ]\\n    if dataflow_analysis:\\n        dimensions.append((\\\"dataflow\\\", dataflow_analysis, list(DATAFLOW_BINS.keys())))\\n    if neg_diff_analysis:\\n        dimensions.append((\\\"neg_difficulty\\\", neg_diff_analysis, NEG_DIFFICULTY_QUARTILE_LABELS))\\n    for dim_name, analysis, bin_order in dimensions:\\n        for b in bin_order:\\n            if b not in analysis:\\n                continue\\n            for strategy in STRATEGIES:\\n                m = analysis[b].get(strategy, {})\\n                ci_r1 = m.get(\\\"R@1_ci\\\", [0, 0])\\n                row = {\\n                    \\\"dimension\\\": dim_name,\\n                    \\\"stratum\\\": b,\\n                    \\\"strategy\\\": strategy,\\n                    \\\"R@1\\\": f\\\"{m.get('R@1', 0):.4f}\\\",\\n                    \\\"R@1_ci95\\\": f\\\"[{ci_r1[0]:.4f}, {ci_r1[1]:.4f}]\\\",\\n                    \\\"R@5\\\": f\\\"{m.get('R@5', 0):.4f}\\\",\\n                    \\\"MRR\\\": f\\\"{m.get('MRR', 0):.4f}\\\",\\n                    \\\"count\\\": m.get(\\\"count\\\", 0),\\n                }\\n                rows.append(row)\\n\\n            # Deltas\\n            for other in [\\\"embedding_distance\\\", \\\"dataflow_aware\\\"]:\\n                dk = f\\\"{other}_vs_random\\\"\\n                d = analysis[b].get(dk, {})\\n                if d:\\n                    row = {\\n                        \\\"dimension\\\": dim_name,\\n                        \\\"stratum\\\": b,\\n                        \\\"strategy\\\": f\\\"DELTA({STRATEGY_LABELS[other]}-Random)\\\",\\n                        \\\"R@1\\\": f\\\"{d.get('R@1_delta', 0):+.4f}\\\",\\n                        \\\"R@1_ci95\\\": f\\\"({d.get('R@1_rel_pct', 0):+.1f}%)\\\",\\n                        \\\"R@5\\\": f\\\"{d.get('R@5_delta', 0):+.4f}\\\",\\n                        \\\"MRR\\\": f\\\"{d.get('MRR_delta', 0):+.4f}\\\",\\n                        \\\"count\\\": \\\"\\\",\\n                    }\\n                    rows.append(row)\\n\\n    fieldnames = [\\\"dimension\\\", \\\"stratum\\\", \\\"strategy\\\", \\\"R@1\\\", \\\"R@1_ci95\\\", \\\"R@5\\\", \\\"MRR\\\", \\\"count\\\"]\\n    with open(output_path, \\\"w\\\", newline=\\\"\\\") as f:\\n        writer = csv.DictWriter(f, fieldnames=fieldnames)\\n        writer.writeheader()\\n        writer.writerows(rows)\\n    print(f\\\"  Summary CSV saved to {output_path}\\\", flush=True)\\n\\n\\n# ── Main ─────────────────────────────────────────────────────────────\\n\\ndef main():\\n    parser = argparse.ArgumentParser(\\n        description=\\\"Stratified analysis of M2 strategies by data strata\\\"\\n    )\\n    parser.add_argument(\\\"--predictions-dir\\\", default=None,\\n                        help=\\\"Dir with per-strategy prediction JSONs (from eval_retrieval.py)\\\")\\n    parser.add_argument(\\\"--checkpoints-dir\\\", default=None,\\n                        help=\\\"Dir containing strategy/seed checkpoint subdirs\\\")\\n    parser.add_argument(\\\"--val-data-dir\\\", default=None,\\n                        help=\\\"Dir with val_&lt;strategy>_s&lt;seed>.jsonl files\\\")\\n    parser.add_argument(\\\"--m1-data\\\", required=True,\\n                        help=\\\"Path to M1 all.jsonl\\\")\\n    parser.add_argument(\\\"--output-dir\\\", required=True)\\n    parser.add_argument(\\\"--dry-run\\\", action=\\\"store_true\\\",\\n                        help=\\\"Use mock predictions to validate pipeline\\\")\\n    parser.add_argument(\\\"--seeds\\\", default=\\\"42,43,44\\\",\\n                        help=\\\"Comma-separated seed list\\\")\\n    parser.add_argument(\\\"--device\\\", default=\\\"cuda\\\")\\n    parser.add_argument(\\\"--max-seq-length\\\", type=int, default=2048)\\n    parser.add_argument(\\\"--n-bootstrap\\\", type=int, default=1000)\\n    parser.add_argument(\\\"--repo-size-bins\\\", default=None,\\n                        help='JSON dict: {\\\"small\\\": [0,50], \\\"medium\\\": [50,200], ...}')\\n    parser.add_argument(\\\"--pool-size-bins\\\", default=None,\\n                        help='JSON dict for pool size bins')\\n    parser.add_argument(\\\"--sim-bins\\\", default=None,\\n                        help='JSON dict for similarity bins')\\n    parser.add_argument(\\\"--dataflow-graph\\\", default=None,\\n                        help=\\\"Path to dataflow_graph.json for structural data availability dimension\\\")\\n    args = parser.parse_args()\\n\\n    s\\n\\n... [截断: 输出过长，省略 3442 字符] ...\\n\\nt\\\")):\\n                        ckpt_dir = candidate\\n                        break\\n                if ckpt_dir is None and os.path.exists(os.path.join(base, \\\"model.pt\\\")):\\n                    ckpt_dir = base\\n                if os.path.exists(ckpt_dir):\\n                    print(f\\\"  Re-evaluating checkpoint: {ckpt_dir}\\\", flush=True)\\n                    results = reeval_checkpoint(\\n                        ckpt_dir, val_samples, args.device, args.max_seq_length\\n                    )\\n                else:\\n                    print(f\\\"  [WARN] Checkpoint not found: {ckpt_dir}\\\", flush=True)\\n                    continue\\n            else:\\n                print(\\\"  [ERROR] No --dry-run, --predictions-dir, or --checkpoints-dir\\\", flush=True)\\n                continue\\n\\n            # Assign strata\\n            results = assign_strata(results, inst_to_repo, repo_counts, dataflow_edges)\\n\\n            # For dry-run or model-based: compute text similarity for sim_bin\\n            if args.dry_run:\\n                for r, s in zip(results, val_samples):\\n                    tsim = text_similarity(s[\\\"query_tokens\\\"][:500], s[\\\"pos_tokens\\\"][:500])\\n                    r[\\\"sim_bin\\\"] = _bin_value(tsim, SIMILARITY_BINS)\\n\\n            all_results[strategy][seed] = results\\n            val_samples_cache[f\\\"{strategy}_s{seed}\\\"] = val_samples\\n            print(f\\\"  -> {len(results)} instances\\\", flush=True)\\n\\n    # Compute neg_difficulty quartiles (text-overlap proxy, CPU-safe)\\n    print(\\\"Computing neg difficulty quartiles...\\\", flush=True)\\n    assign_neg_difficulty_quartiles(all_results, val_samples_cache)\\n\\n    # Run stratified analysis\\n    print(\\\"\\\\nRunning stratified analysis...\\\", flush=True)\\n    repo_analysis = run_stratified_analysis(\\n        all_results, \\\"repo_size_bin\\\", list(REPO_SIZE_BINS.keys()), args.n_bootstrap\\n    )\\n    pool_analysis = run_stratified_analysis(\\n        all_results, \\\"pool_size_bin\\\", list(POOL_SIZE_BINS.keys()), args.n_bootstrap\\n    )\\n    sim_analysis = run_stratified_analysis(\\n        all_results, \\\"sim_bin\\\", list(SIMILARITY_BINS.keys()), args.n_bootstrap\\n    )\\n\\n    dataflow_analysis = {}\\n    if dataflow_edges is not None:\\n        dataflow_analysis = run_stratified_analysis(\\n            all_results, \\\"dataflow_bin\\\", list(DATAFLOW_BINS.keys()), args.n_bootstrap\\n        )\\n\\n    neg_diff_analysis = run_stratified_analysis(\\n        all_results, \\\"neg_difficulty_bin\\\", NEG_DIFFICULTY_QUARTILE_LABELS, args.n_bootstrap\\n    )\\n\\n    # Save JSON\\n    full_results = {\\n        \\\"config\\\": {\\n            \\\"strategies\\\": STRATEGIES,\\n            \\\"seeds\\\": seeds,\\n            \\\"repo_size_bins\\\": {k: list(v) for k, v in REPO_SIZE_BINS.items()},\\n            \\\"pool_size_bins\\\": {k: list(v) for k, v in POOL_SIZE_BINS.items()},\\n            \\\"similarity_bins\\\": {k: list(v) for k, v in SIMILARITY_BINS.items()},\\n            \\\"dataflow_bins\\\": {k: list(v) for k, v in DATAFLOW_BINS.items()},\\n            \\\"neg_difficulty_quartiles\\\": NEG_DIFFICULTY_QUARTILE_LABELS,\\n            \\\"n_bootstrap\\\": args.n_bootstrap,\\n            \\\"dry_run\\\": args.dry_run,\\n        },\\n        \\\"by_repo_size\\\": repo_analysis,\\n        \\\"by_pool_size\\\": pool_analysis,\\n        \\\"by_similarity\\\": sim_analysis,\\n        \\\"by_dataflow\\\": dataflow_analysis,\\n        \\\"by_neg_difficulty\\\": neg_diff_analysis,\\n    }\\n\\n    json_path = os.path.join(args.output_dir, \\\"stratified_results.json\\\")\\n    with open(json_path, \\\"w\\\") as f:\\n        json.dump(full_results, f, indent=2, ensure_ascii=False)\\n    print(f\\\"  Results JSON saved to {json_path}\\\", flush=True)\\n\\n    # CSV summary\\n    csv_path = os.path.join(args.output_dir, \\\"stratified_summary.csv\\\")\\n    write_summary_csv(repo_analysis, pool_analysis, sim_analysis, csv_path, dataflow_analysis, neg_diff_analysis)\\n\\n    # Plots\\n    try:\\n        make_plots(repo_analysis, pool_analysis, sim_analysis, args.output_dir, dataflow_analysis, neg_diff_analysis)\\n    except Exception as e:\\n        print(f\\\"  [WARN] Plot generation failed: {e}\\\", flush=True)\\n\\n    print(\\\"\\\\nDone.\\\", flush=True)\\n\\n\\nif __name__ == \\\"__main__\\\":\\n    main()\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.39}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "80059ebb-0bda-4e93-a91f-0a404f014545",
  "isSidechain": false,
  "promptId": "22ffd1fb-240e-481f-9bcc-b3f6a42d6805",
  "type": "user",
  "uuid": "e8cb838f-5a39-4d1c-8f7d-5c106e1a38e6",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"        (\\\\\\\"pool_size\\\\\\\", pool_analysis, list(POOL_SIZE_BINS.keys())),\\\\n        (\\\\\\\"similarity\\\\\\\", sim_analysis, list(SIMILARITY_BINS.keys())),\\\\n    ]\\\\n    if dataflow_analysis:\\\\n        dimensions.append((\\\\\\\"dataflow\\\\\\\", dataflow_analysis, list(DATAFLOW_BINS.keys())))\\\\n    if neg_diff_analysis:\\\\n        dimensions.append((\\\\\\\"neg_difficulty\\\\\\\", neg_diff_analysis, NEG_DIFFICULTY_QUARTILE_LABELS))\\\\n    for dim_name, analysis, bin_order in dimensions:\\\\n        for b in bin_order:\\\\n            if b not in analysis:\\\\n                continue\\\\n            for strategy in STRATEGIES:\\\\n                m = analysis[b].get(strategy, {})\\\\n                ci_r1 = m.get(\\\\\\\"R@1_ci\\\\\\\", [0, 0])\\\\n                row = {\\\\n                    \\\\\\\"dimension\\\\\\\": dim_name,\\\\n                    \\\\\\\"stratum\\\\\\\": b,\\\\n                    \\\\\\\"strategy\\\\\\\": strategy,\\\\n                    \\\\\\\"R@1\\\\\\\": f\\\\\\\"{m.get('R@1', 0):.4f}\\\\\\\",\\\\n                    \\\\\\\"R@1_ci95\\\\\\\": f\\\\\\\"[{ci_r1[0]:.4f}, {ci_r1[1]:.4f}]\\\\\\\",\\\\n                    \\\\\\\"R@5\\\\\\\": f\\\\\\\"{m.get('R@5', 0):.4f}\\\\\\\",\\\\n                    \\\\\\\"MRR\\\\\\\": f\\\\\\\"{m.get('MRR', 0):.4f}\\\\\\\",\\\\n                    \\\\\\\"count\\\\\\\": m.get(\\\\\\\"count\\\\\\\", 0),\\\\n                }\\\\n                rows.append(row)\\\\n\\\\n            # Deltas\\\\n            for other in [\\\\\\\"embedding_distance\\\\\\\", \\\\\\\"dataflow_aware\\\\\\\"]:\\\\n                dk = f\\\\\\\"{other}_vs_random\\\\\\\"\\\\n                d = analysis[b].get(dk, {})\\\\n                if d:\\\\n                    row = {\\\\n                        \\\\\\\"dimension\\\\\\\": dim_name,\\\\n                        \\\\\\\"stratum\\\\\\\": b,\\\\n                        \\\\\\\"strategy\\\\\\\": f\\\\\\\"DELTA({STRATEGY_LABELS[other]}-Random)\\\\\\\",\\\\n                        \\\\\\\"R@1\\\\\\\": f\\\\\\\"{d.get('R@1_delta', 0):+.4f}\\\\\\\",\\\\n                        \\\\\\\"R@1_ci95\\\\\\\": f\\\\\\\"({d.get('R@1_rel_pct', 0):+.1f}%)\\\\\\\",\\\\n                        \\\\\\\"R@5\\\\\\\": f\\\\\\\"{d.get('R@5_delta', 0):+.4f}\\\\\\\",\\\\n                        \\\\\\\"MRR\\\\\\\": f\\\\\\\"{d.get('MRR_delta', 0):+.4f}\\\\\\\",\\\\n                        \\\\\\\"count\\\\\\\": \\\\\\\"\\\\\\\",\\\\n                    }\\\\n                    rows.append(row)\\\\n\\\\n    fieldnames = [\\\\\\\"dimension\\\\\\\", \\\\\\\"stratum\\\\\\\", \\\\\\\"strategy\\\\\\\", \\\\\\\"R@1\\\\\\\", \\\\\\\"R@1_ci95\\\\\\\", \\\\\\\"R@5\\\\\\\", \\\\\\\"MRR\\\\\\\", \\\\\\\"count\\\\\\\"]\\\\n    with open(output_path, \\\\\\\"w\\\\\\\", newline=\\\\\\\"\\\\\\\") as f:\\\\n        writer = csv.DictWriter(f, fieldnames=fieldnames)\\\\n        writer.writeheader()\\\\n        writer.writerows(rows)\\\\n    print(f\\\\\\\"  Summary CSV saved to {output_path}\\\\\\\", flush=True)\\\\n\\\\n\\\\n# ── Main ─────────────────────────────────────────────────────────────\\\\n\\\\ndef main():\\\\n    parser = argparse.ArgumentParser(\\\\n        description=\\\\\\\"Stratified analysis of M2 strategies by data strata\\\\\\\"\\\\n    )\\\\n    parser.add_argument(\\\\\\\"--predictions-dir\\\\\\\", default=None,\\\\n                        help=\\\\\\\"Dir with per-strategy prediction JSONs (from eval_retrieval.py)\\\\\\\")\\\\n    parser.add_argument(\\\\\\\"--checkpoints-dir\\\\\\\", default=None,\\\\n                        help=\\\\\\\"Dir containing strategy/seed checkpoint subdirs\\\\\\\")\\\\n    parser.add_argument(\\\\\\\"--val-data-dir\\\\\\\", default=None,\\\\n                        help=\\\\\\\"Dir with val_&lt;strategy>_s&lt;seed>.jsonl files\\\\\\\")\\\\n    parser.add_argument(\\\\\\\"--m1-data\\\\\\\", required=True,\\\\n                        help=\\\\\\\"Path to M1 all.jsonl\\\\\\\")\\\\n    parser.add_argument(\\\\\\\"--output-dir\\\\\\\", required=True)\\\\n    parser.add_argument(\\\\\\\"--dry-run\\\\\\\", action=\\\\\\\"store_true\\\\\\\",\\\\n                        help=\\\\\\\"Use mock predictions to validate pipeline\\\\\\\")\\\\n    parser.add_argument(\\\\\\\"--seeds\\\\\\\", default=\\\\\\\"42,43,44\\\\\\\",\\\\n                        help=\\\\\\\"Comma-separated seed list\\\\\\\")\\\\n    parser.add_argument(\\\\\\\"--device\\\\\\\", default=\\\\\\\"cuda\\\\\\\")\\\\n    parser.add_argument(\\\\\\\"--max-seq-length\\\\\\\", type=int, default=2048)\\\\n    parser.add_argument(\\\\\\\"--n-bootstrap\\\\\\\", type=int, default=1000)\\\\n    parser.add_argument(\\\\\\\"--repo-size-bins\\\\\\\", default=None,\\\\n                        help='JSON dict: {\\\\\\\"small\\\\\\\": [0,50], \\\\\\\"medium\\\\\\\": [50,200], ...}')\\\\n    parser.add_argument(\\\\\\\"--pool-size-bins\\\\\\\", default=None,\\\\n                        help='JSON dict for pool size bins')\\\\n    parser.add_argument(\\\\\\\"--sim-bins\\\\\\\", default=None,\\\\n                        help='JSON dict for similarity bins')\\\\n    parser.add_argument(\\\\\\\"--dataflow-graph\\\\\\\", default=None,\\\\n                        help=\\\\\\\"Path to dataflow_graph.json for structural data availability dimension\\\\\\\")\\\\n    args = parser.parse_args()\\\\n\\\\n    s\\\\n\\\\n... [截断: 输出过长，省略 3442 字符] ...\\\\n\\\\nt\\\\\\\")):\\\\n                        ckpt_dir = candidate\\\\n                        break\\\\n                if ckpt_dir is None and os.path.exists(os.path.join(base, \\\\\\\"model.pt\\\\\\\")):\\\\n                    ckpt_dir = base\\\\n                if os.path.exists(ckpt_dir):\\\\n                    print(f\\\\\\\"  Re-evaluating checkpoint: {ckpt_dir}\\\\\\\", flush=True)\\\\n                    results = reeval_checkpoint(\\\\n                        ckpt_dir, val_samples, args.device, args.max_seq_length\\\\n                    )\\\\n                else:\\\\n                    print(f\\\\\\\"  [WARN] Checkpoint not found: {ckpt_dir}\\\\\\\", flush=True)\\\\n                    continue\\\\n            else:\\\\n                print(\\\\\\\"  [ERROR] No --dry-run, --predictions-dir, or --checkpoints-dir\\\\\\\", flush=True)\\\\n                continue\\\\n\\\\n            # Assign strata\\\\n            results = assign_strata(results, inst_to_repo, repo_counts, dataflow_edges)\\\\n\\\\n            # For dry-run or model-based: compute text similarity for sim_bin\\\\n            if args.dry_run:\\\\n                for r, s in zip(results, val_samples):\\\\n                    tsim = text_similarity(s[\\\\\\\"query_tokens\\\\\\\"][:500], s[\\\\\\\"pos_tokens\\\\\\\"][:500])\\\\n                    r[\\\\\\\"sim_bin\\\\\\\"] = _bin_value(tsim, SIMILARITY_BINS)\\\\n\\\\n            all_results[strategy][seed] = results\\\\n            val_samples_cache[f\\\\\\\"{strategy}_s{seed}\\\\\\\"] = val_samples\\\\n            print(f\\\\\\\"  -> {len(results)} instances\\\\\\\", flush=True)\\\\n\\\\n    # Compute neg_difficulty quartiles (text-overlap proxy, CPU-safe)\\\\n    print(\\\\\\\"Computing neg difficulty quartiles...\\\\\\\", flush=True)\\\\n    assign_neg_difficulty_quartiles(all_results, val_samples_cache)\\\\n\\\\n    # Run stratified analysis\\\\n    print(\\\\\\\"\\\\\\\\nRunning stratified analysis...\\\\\\\", flush=True)\\\\n    repo_analysis = run_stratified_analysis(\\\\n        all_results, \\\\\\\"repo_size_bin\\\\\\\", list(REPO_SIZE_BINS.keys()), args.n_bootstrap\\\\n    )\\\\n    pool_analysis = run_stratified_analysis(\\\\n        all_results, \\\\\\\"pool_size_bin\\\\\\\", list(POOL_SIZE_BINS.keys()), args.n_bootstrap\\\\n    )\\\\n    sim_analysis = run_stratified_analysis(\\\\n        all_results, \\\\\\\"sim_bin\\\\\\\", list(SIMILARITY_BINS.keys()), args.n_bootstrap\\\\n    )\\\\n\\\\n    dataflow_analysis = {}\\\\n    if dataflow_edges is not None:\\\\n        dataflow_analysis = run_stratified_analysis(\\\\n            all_results, \\\\\\\"dataflow_bin\\\\\\\", list(DATAFLOW_BINS.keys()), args.n_bootstrap\\\\n        )\\\\n\\\\n    neg_diff_analysis = run_stratified_analysis(\\\\n        all_results, \\\\\\\"neg_difficulty_bin\\\\\\\", NEG_DIFFICULTY_QUARTILE_LABELS, args.n_bootstrap\\\\n    )\\\\n\\\\n    # Save JSON\\\\n    full_results = {\\\\n        \\\\\\\"config\\\\\\\": {\\\\n            \\\\\\\"strategies\\\\\\\": STRATEGIES,\\\\n            \\\\\\\"seeds\\\\\\\": seeds,\\\\n            \\\\\\\"repo_size_bins\\\\\\\": {k: list(v) for k, v in REPO_SIZE_BINS.items()},\\\\n            \\\\\\\"pool_size_bins\\\\\\\": {k: list(v) for k, v in POOL_SIZE_BINS.items()},\\\\n            \\\\\\\"similarity_bins\\\\\\\": {k: list(v) for k, v in SIMILARITY_BINS.items()},\\\\n            \\\\\\\"dataflow_bins\\\\\\\": {k: list(v) for k, v in DATAFLOW_BINS.items()},\\\\n            \\\\\\\"neg_difficulty_quartiles\\\\\\\": NEG_DIFFICULTY_QUARTILE_LABELS,\\\\n            \\\\\\\"n_bootstrap\\\\\\\": args.n_bootstrap,\\\\n            \\\\\\\"dry_run\\\\\\\": args.dry_run,\\\\n        },\\\\n        \\\\\\\"by_repo_size\\\\\\\": repo_analysis,\\\\n        \\\\\\\"by_pool_size\\\\\\\": pool_analysis,\\\\n        \\\\\\\"by_similarity\\\\\\\": sim_analysis,\\\\n        \\\\\\\"by_dataflow\\\\\\\": dataflow_analysis,\\\\n        \\\\\\\"by_neg_difficulty\\\\\\\": neg_diff_analysis,\\\\n    }\\\\n\\\\n    json_path = os.path.join(args.output_dir, \\\\\\\"stratified_results.json\\\\\\\")\\\\n    with open(json_path, \\\\\\\"w\\\\\\\") as f:\\\\n        json.dump(full_results, f, indent=2, ensure_ascii=False)\\\\n    print(f\\\\\\\"  Results JSON saved to {json_path}\\\\\\\", flush=True)\\\\n\\\\n    # CSV summary\\\\n    csv_path = os.path.join(args.output_dir, \\\\\\\"stratified_summary.csv\\\\\\\")\\\\n    write_summary_csv(repo_analysis, pool_analysis, sim_analysis, csv_path, dataflow_analysis, neg_diff_analysis)\\\\n\\\\n    # Plots\\\\n    try:\\\\n        make_plots(repo_analysis, pool_analysis, sim_analysis, args.output_dir, dataflow_analysis, neg_diff_analysis)\\\\n    except Exception as e:\\\\n        print(f\\\\\\\"  [WARN] Plot generation failed: {e}\\\\\\\", flush=True)\\\\n\\\\n    print(\\\\\\\"\\\\\\\\nDone.\\\\\\\", flush=True)\\\\n\\\\n\\\\nif __name__ == \\\\\\\"__main__\\\\\\\":\\\\n    main()\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.39}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"        (\\\"pool_size\\\", pool_analysis, list(POOL_SIZE_BINS.keys())),\\n        (\\\"similarity\\\", sim_analysis, list(SIMILARITY_BINS.keys())),\\n    ]\\n    if dataflow_analysis:\\n        dimensions.append((\\\"dataflow\\\", dataflow_analysis, list(DATAFLOW_BINS.keys())))\\n    if neg_diff_analysis:\\n        dimensions.append((\\\"neg_difficulty\\\", neg_diff_analysis, NEG_DIFFICULTY_QUARTILE_LABELS))\\n    for dim_name, analysis, bin_order in dimensions:\\n        for b in bin_order:\\n            if b not in analysis:\\n                continue\\n            for strategy in STRATEGIES:\\n                m = analysis[b].get(strategy, {})\\n                ci_r1 = m.get(\\\"R@1_ci\\\", [0, 0])\\n                row = {\\n                    \\\"dimension\\\": dim_name,\\n                    \\\"stratum\\\": b,\\n                    \\\"strategy\\\": strategy,\\n                    \\\"R@1\\\": f\\\"{m.get('R@1', 0):.4f}\\\",\\n                    \\\"R@1_ci95\\\": f\\\"[{ci_r1[0]:.4f}, {ci_r1[1]:.4f}]\\\",\\n                    \\\"R@5\\\": f\\\"{m.get('R@5', 0):.4f}\\\",\\n                    \\\"MRR\\\": f\\\"{m.get('MRR', 0):.4f}\\\",\\n                    \\\"count\\\": m.get(\\\"count\\\", 0),\\n                }\\n                rows.append(row)\\n\\n            # Deltas\\n            for other in [\\\"embedding_distance\\\", \\\"dataflow_aware\\\"]:\\n                dk = f\\\"{other}_vs_random\\\"\\n                d = analysis[b].get(dk, {})\\n                if d:\\n                    row = {\\n                        \\\"dimension\\\": dim_name,\\n                        \\\"stratum\\\": b,\\n                        \\\"strategy\\\": f\\\"DELTA({STRATEGY_LABELS[other]}-Random)\\\",\\n                        \\\"R@1\\\": f\\\"{d.get('R@1_delta', 0):+.4f}\\\",\\n                        \\\"R@1_ci95\\\": f\\\"({d.get('R@1_rel_pct', 0):+.1f}%)\\\",\\n                        \\\"R@5\\\": f\\\"{d.get('R@5_delta', 0):+.4f}\\\",\\n                        \\\"MRR\\\": f\\\"{d.get('MRR_delta', 0):+.4f}\\\",\\n                        \\\"count\\\": \\\"\\\",\\n                    }\\n                    rows.append(row)\\n\\n    fieldnames = [\\\"dimension\\\", \\\"stratum\\\", \\\"strategy\\\", \\\"R@1\\\", \\\"R@1_ci95\\\", \\\"R@5\\\", \\\"MRR\\\", \\\"count\\\"]\\n    with open(output_path, \\\"w\\\", newline=\\\"\\\") as f:\\n        writer = csv.DictWriter(f, fieldnames=fieldnames)\\n        writer.writeheader()\\n        writer.writerows(rows)\\n    print(f\\\"  Summary CSV saved to {output_path}\\\", flush=True)\\n\\n\\n# ── Main ─────────────────────────────────────────────────────────────\\n\\ndef main():\\n    parser = argparse.ArgumentParser(\\n        description=\\\"Stratified analysis of M2 strategies by data strata\\\"\\n    )\\n    parser.add_argument(\\\"--predictions-dir\\\", default=None,\\n                        help=\\\"Dir with per-strategy prediction JSONs (from eval_retrieval.py)\\\")\\n    parser.add_argument(\\\"--checkpoints-dir\\\", default=None,\\n                        help=\\\"Dir containing strategy/seed checkpoint subdirs\\\")\\n    parser.add_argument(\\\"--val-data-dir\\\", default=None,\\n                        help=\\\"Dir with val_&lt;strategy>_s&lt;seed>.jsonl files\\\")\\n    parser.add_argument(\\\"--m1-data\\\", required=True,\\n                        help=\\\"Path to M1 all.jsonl\\\")\\n    parser.add_argument(\\\"--output-dir\\\", required=True)\\n    parser.add_argument(\\\"--dry-run\\\", action=\\\"store_true\\\",\\n                        help=\\\"Use mock predictions to validate pipeline\\\")\\n    parser.add_argument(\\\"--seeds\\\", default=\\\"42,43,44\\\",\\n                        help=\\\"Comma-separated seed list\\\")\\n    parser.add_argument(\\\"--device\\\", default=\\\"cuda\\\")\\n    parser.add_argument(\\\"--max-seq-length\\\", type=int, default=2048)\\n    parser.add_argument(\\\"--n-bootstrap\\\", type=int, default=1000)\\n    parser.add_argument(\\\"--repo-size-bins\\\", default=None,\\n                        help='JSON dict: {\\\"small\\\": [0,50], \\\"medium\\\": [50,200], ...}')\\n    parser.add_argument(\\\"--pool-size-bins\\\", default=None,\\n                        help='JSON dict for pool size bins')\\n    parser.add_argument(\\\"--sim-bins\\\", default=None,\\n                        help='JSON dict for similarity bins')\\n    parser.add_argument(\\\"--dataflow-graph\\\", default=None,\\n                        help=\\\"Path to dataflow_graph.json for structural data availability dimension\\\")\\n    args = parser.parse_args()\\n\\n    s\\n\\n... [截断: 输出过长，省略 3442 字符] ...\\n\\nt\\\")):\\n                        ckpt_dir = candidate\\n                        break\\n                if ckpt_dir is None and os.path.exists(os.path.join(base, \\\"model.pt\\\")):\\n                    ckpt_dir = base\\n                if os.path.exists(ckpt_dir):\\n                    print(f\\\"  Re-evaluating checkpoint: {ckpt_dir}\\\", flush=True)\\n                    results = reeval_checkpoint(\\n                        ckpt_dir, val_samples, args.device, args.max_seq_length\\n                    )\\n                else:\\n                    print(f\\\"  [WARN] Checkpoint not found: {ckpt_dir}\\\", flush=True)\\n                    continue\\n            else:\\n                print(\\\"  [ERROR] No --dry-run, --predictions-dir, or --checkpoints-dir\\\", flush=True)\\n                continue\\n\\n            # Assign strata\\n            results = assign_strata(results, inst_to_repo, repo_counts, dataflow_edges)\\n\\n            # For dry-run or model-based: compute text similarity for sim_bin\\n            if args.dry_run:\\n                for r, s in zip(results, val_samples):\\n                    tsim = text_similarity(s[\\\"query_tokens\\\"][:500], s[\\\"pos_tokens\\\"][:500])\\n                    r[\\\"sim_bin\\\"] = _bin_value(tsim, SIMILARITY_BINS)\\n\\n            all_results[strategy][seed] = results\\n            val_samples_cache[f\\\"{strategy}_s{seed}\\\"] = val_samples\\n            print(f\\\"  -> {len(results)} instances\\\", flush=True)\\n\\n    # Compute neg_difficulty quartiles (text-overlap proxy, CPU-safe)\\n    print(\\\"Computing neg difficulty quartiles...\\\", flush=True)\\n    assign_neg_difficulty_quartiles(all_results, val_samples_cache)\\n\\n    # Run stratified analysis\\n    print(\\\"\\\\nRunning stratified analysis...\\\", flush=True)\\n    repo_analysis = run_stratified_analysis(\\n        all_results, \\\"repo_size_bin\\\", list(REPO_SIZE_BINS.keys()), args.n_bootstrap\\n    )\\n    pool_analysis = run_stratified_analysis(\\n        all_results, \\\"pool_size_bin\\\", list(POOL_SIZE_BINS.keys()), args.n_bootstrap\\n    )\\n    sim_analysis = run_stratified_analysis(\\n        all_results, \\\"sim_bin\\\", list(SIMILARITY_BINS.keys()), args.n_bootstrap\\n    )\\n\\n    dataflow_analysis = {}\\n    if dataflow_edges is not None:\\n        dataflow_analysis = run_stratified_analysis(\\n            all_results, \\\"dataflow_bin\\\", list(DATAFLOW_BINS.keys()), args.n_bootstrap\\n        )\\n\\n    neg_diff_analysis = run_stratified_analysis(\\n        all_results, \\\"neg_difficulty_bin\\\", NEG_DIFFICULTY_QUARTILE_LABELS, args.n_bootstrap\\n    )\\n\\n    # Save JSON\\n    full_results = {\\n        \\\"config\\\": {\\n            \\\"strategies\\\": STRATEGIES,\\n            \\\"seeds\\\": seeds,\\n            \\\"repo_size_bins\\\": {k: list(v) for k, v in REPO_SIZE_BINS.items()},\\n            \\\"pool_size_bins\\\": {k: list(v) for k, v in POOL_SIZE_BINS.items()},\\n            \\\"similarity_bins\\\": {k: list(v) for k, v in SIMILARITY_BINS.items()},\\n            \\\"dataflow_bins\\\": {k: list(v) for k, v in DATAFLOW_BINS.items()},\\n            \\\"neg_difficulty_quartiles\\\": NEG_DIFFICULTY_QUARTILE_LABELS,\\n            \\\"n_bootstrap\\\": args.n_bootstrap,\\n            \\\"dry_run\\\": args.dry_run,\\n        },\\n        \\\"by_repo_size\\\": repo_analysis,\\n        \\\"by_pool_size\\\": pool_analysis,\\n        \\\"by_similarity\\\": sim_analysis,\\n        \\\"by_dataflow\\\": dataflow_analysis,\\n        \\\"by_neg_difficulty\\\": neg_diff_analysis,\\n    }\\n\\n    json_path = os.path.join(args.output_dir, \\\"stratified_results.json\\\")\\n    with open(json_path, \\\"w\\\") as f:\\n        json.dump(full_results, f, indent=2, ensure_ascii=False)\\n    print(f\\\"  Results JSON saved to {json_path}\\\", flush=True)\\n\\n    # CSV summary\\n    csv_path = os.path.join(args.output_dir, \\\"stratified_summary.csv\\\")\\n    write_summary_csv(repo_analysis, pool_analysis, sim_analysis, csv_path, dataflow_analysis, neg_diff_analysis)\\n\\n    # Plots\\n    try:\\n        make_plots(repo_analysis, pool_analysis, sim_analysis, args.output_dir, dataflow_analysis, neg_diff_analysis)\\n    except Exception as e:\\n        print(f\\\"  [WARN] Plot generation failed: {e}\\\", flush=True)\\n\\n    print(\\\"\\\\nDone.\\\", flush=True)\\n\\n\\nif __name__ == \\\"__main__\\\":\\n    main()\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.39}}"
    }
  },
  "sourceToolAssistantUUID": "80059ebb-0bda-4e93-a91f-0a404f014545",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "bda3dfbf-4b90-494d-b674-2597173fd381",
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
  "leafUuid": "e8cb838f-5a39-4d1c-8f7d-5c106e1a38e6",
  "sessionId": "bda3dfbf-4b90-494d-b674-2597173fd381"
}
```

---

### Runtime record

_source line 69_

```json
{
  "type": "ai-title",
  "aiTitle": "Add pool-size controlled stratified evaluation to analysis script",
  "sessionId": "bda3dfbf-4b90-494d-b674-2597173fd381"
}
```

---

### Assistant

_source line 70 · 2026-05-14T20:47:51.036Z_

<details><summary>Logged reasoning block</summary>

```text
The main function is still getting truncated in the middle around line 755-770. Let me get that final piece.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e8cb838f-5a39-4d1c-8f7d-5c106e1a38e6",
  "isSidechain": false,
  "requestId": "req_011Cb37noSTYvRpm2Y88M17F",
  "type": "assistant",
  "uuid": "be1dbcf1-727f-47ae-94ca-a76785ae4d0d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "bda3dfbf-4b90-494d-b674-2597173fd381",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XVSnwVAppo2mFKtR9aS8nB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3366,
      "cache_read_input_tokens": 57834,
      "output_tokens": 163,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3366,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 163,
          "cache_read_input_tokens": 57834,
          "cache_creation_input_tokens": 3366,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3366
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

_source line 71 · 2026-05-14T20:47:51.767Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01Jz5J2FEwHoU7q8hUAHB8DZ`</summary>

```json
{
  "server": "bjb1-42106",
  "command": "tail -n +750 /root/structfuse/evaluation/analyze_stratified.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "be1dbcf1-727f-47ae-94ca-a76785ae4d0d",
  "isSidechain": false,
  "requestId": "req_011Cb37noSTYvRpm2Y88M17F",
  "type": "assistant",
  "uuid": "bc6af3e6-b801-46b9-8987-3fac4ba868cb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "bda3dfbf-4b90-494d-b674-2597173fd381",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XVSnwVAppo2mFKtR9aS8nB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3366,
      "cache_read_input_tokens": 57834,
      "output_tokens": 163,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3366,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 163,
          "cache_read_input_tokens": 57834,
          "cache_creation_input_tokens": 3366,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3366
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

_source line 72 · 2026-05-14T20:47:52.133Z_

<details><summary>↩ Tool result · `toolu_01Jz5J2FEwHoU7q8hUAHB8DZ`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"        REPO_SIZE_BINS.update({k: tuple(v) for k, v in custom.items()})\\n    if args.pool_size_bins:\\n        custom = json.loads(args.pool_size_bins)\\n        POOL_SIZE_BINS.clear()\\n        POOL_SIZE_BINS.update({k: tuple(v) for k, v in custom.items()})\\n    if args.sim_bins:\\n        custom = json.loads(args.sim_bins)\\n        SIMILARITY_BINS.clear()\\n        SIMILARITY_BINS.update({k: tuple(v) for k, v in custom.items()})\\n\\n    # Load M1 metadata\\n    print(f\\\"Loading M1 metadata from {args.m1_data}...\\\", flush=True)\\n    inst_to_repo, repo_counts = load_m1_metadata(args.m1_data)\\n    print(f\\\"  {len(inst_to_repo)} instances, {len(repo_counts)} repos\\\", flush=True)\\n\\n    # Load dataflow graph if provided\\n    dataflow_edges = None\\n    if args.dataflow_graph and os.path.exists(args.dataflow_graph):\\n        print(f\\\"Loading dataflow graph from {args.dataflow_graph}...\\\", flush=True)\\n        dataflow_edges = load_dataflow_edges(args.dataflow_graph)\\n        print(f\\\"  {len(dataflow_edges)} file entries\\\", flush=True)\\n\\n    # Determine val data directory\\n    val_dir = args.val_data_dir\\n    if val_dir is None and args.predictions_dir is None and not args.dry_run:\\n        val_dir = \\\"/root/autodl-tmp/structfuse/full_m2_training_data\\\"\\n    if val_dir is None and args.dry_run:\\n        val_dir = \\\"/root/autodl-tmp/structfuse/full_m2_training_data\\\"\\n\\n    # Collect per-instance results: {strategy: {seed: [results]}}\\n    all_results: Dict[str, Dict[int, List[Dict]]] = defaultdict(dict)\\n    val_samples_cache: Dict[str, List[Dict]] = {}\\n\\n    for strategy in STRATEGIES:\\n        for seed in seeds:\\n            val_file = os.path.join(val_dir, f\\\"val_{strategy}_s{seed}.jsonl\\\") if val_dir else None\\n\\n            if val_file and os.path.exists(val_file):\\n                print(f\\\"Loading val data: {strategy} seed={seed}...\\\", flush=True)\\n                lite = args.predictions_dir is not None\\n                val_samples = load_val_samples(val_file, lite=lite)\\n            else:\\n                print(f\\\"  [WARN] Val file not found: {val_file}, skipping\\\", flush=True)\\n                continue\\n\\n            if args.dry_run:\\n                print(f\\\"  Generating mock predictions: {strategy} seed={seed}\\\", flush=True)\\n                results = mock_predictions(val_samples, strategy, seed)\\n            elif args.predictions_dir:\\n                pred_pattern = os.path.join(\\n                    args.predictions_dir, f\\\"*{strategy}*s{seed}*.json\\\"\\n                )\\n                import glob\\n                pred_files = glob.glob(pred_pattern)\\n                if pred_files:\\n                    print(f\\\"  Loading predictions: {pred_files[0]}\\\", flush=True)\\n                    results = load_predictions(pred_files[0], val_samples)\\n                else:\\n                    print(f\\\"  [WARN] No prediction file matching {pred_pattern}\\\", flush=True)\\n                    continue\\n            elif args.checkpoints_dir:\\n                base = os.path.join(args.checkpoints_dir, f\\\"{strategy}_s{seed}\\\")\\n                ckpt_dir = None\\n                for subdir in [\\\"best\\\", \\\"best_by_recall_at_1\\\", \\\"best_by_val_loss\\\"]:\\n                    candidate = os.path.join(base, subdir)\\n                    if os.path.exists(os.path.join(candidate, \\\"model.pt\\\")):\\n                        ckpt_dir = candidate\\n                        break\\n                if ckpt_dir is None and os.path.exists(os.path.join(base, \\\"model.pt\\\")):\\n                    ckpt_dir = base\\n                if os.path.exists(ckpt_dir):\\n                    print(f\\\"  Re-evaluating checkpoint: {ckpt_dir}\\\", flush=True)\\n                    results = reeval_checkpoint(\\n                        ckpt_dir, val_samples, args.device, args.max_seq_length\\n                    )\\n                else:\\n                    print(f\\\"  [WARN] Checkpoint not found: {ckpt_dir}\\\", flush=True)\\n                    continue\\n            else:\\n                print(\\\"  [ERROR] No --dry-run, --predictions-dir, or --checkpoints-dir\\\", flush=True)\\n                continue\\n\\n            # Assign strata\\n            results = assign_strata(results, inst_to_repo, repo_counts, dataflow_edges)\\n\\n            # For dry-run or model-based: compute text similarity for sim_bin\\n            if args.dry_run:\\n                for r, s in zip(results, val_samples):\\n                    tsim = text_similarity(s[\\\"query_tokens\\\"][:500], s[\\\"pos_tokens\\\"][:500])\\n                    r[\\\"sim_bin\\\"] = _bin_value(tsim, SIMILARITY_BINS)\\n\\n            all_results[strategy][seed] = results\\n            val_samples_cache[f\\\"{strategy}_s{seed}\\\"] = val_samples\\n            print(f\\\"  -> {len(results)} instances\\\", flush=True)\\n\\n    # Compute neg_difficulty quartiles (text-overlap proxy, CPU-safe)\\n    print(\\\"Computing neg difficulty quartiles...\\\", flush=True)\\n    assign_neg_difficulty_quartiles(all_results, val_samples_cache)\\n\\n    # Run stratified analysis\\n    print(\\\"\\\\nRunning stratified analysis...\\\", flush=True)\\n    repo_analysis = run_stratified_analysis(\\n        all_results, \\\"repo_size_bin\\\", list(REPO_SIZE_BINS.keys()), args.n_bootstrap\\n    )\\n    pool_analysis = run_stratified_analysis(\\n        all_results, \\\"pool_size_bin\\\", list(POOL_SIZE_BINS.keys()), args.n_bootstrap\\n    )\\n    sim_analysis = run_stratified_analysis(\\n        all_results, \\\"sim_bin\\\", list(SIMILARITY_BINS.keys()), args.n_bootstrap\\n    )\\n\\n    dataflow_analysis = {}\\n    if dataflow_edges is not None:\\n        dataflow_analysis = run_stratified_analysis(\\n            all_results, \\\"dataflow_bin\\\", list(DATAFLOW_BINS.keys()), args.n_bootstrap\\n        )\\n\\n    neg_diff_analysis = run_stratified_analysis(\\n        all_results, \\\"neg_difficulty_bin\\\", NEG_DIFFICULTY_QUARTILE_LABELS, args.n_bootstrap\\n    )\\n\\n    # Save JSON\\n    full_results = {\\n        \\\"config\\\": {\\n            \\\"strategies\\\": STRATEGIES,\\n            \\\"seeds\\\": seeds,\\n            \\\"repo_size_bins\\\": {k: list(v) for k, v in REPO_SIZE_BINS.items()},\\n            \\\"pool_size_bins\\\": {k: list(v) for k, v in POOL_SIZE_BINS.items()},\\n            \\\"similarity_bins\\\": {k: list(v) for k, v in SIMILARITY_BINS.items()},\\n            \\\"dataflow_bins\\\": {k: list(v) for k, v in DATAFLOW_BINS.items()},\\n            \\\"neg_difficulty_quartiles\\\": NEG_DIFFICULTY_QUARTILE_LABELS,\\n            \\\"n_bootstrap\\\": args.n_bootstrap,\\n            \\\"dry_run\\\": args.dry_run,\\n        },\\n        \\\"by_repo_size\\\": repo_analysis,\\n        \\\"by_pool_size\\\": pool_analysis,\\n        \\\"by_similarity\\\": sim_analysis,\\n        \\\"by_dataflow\\\": dataflow_analysis,\\n        \\\"by_neg_difficulty\\\": neg_diff_analysis,\\n    }\\n\\n    json_path = os.path.join(args.output_dir, \\\"stratified_results.json\\\")\\n    with open(json_path, \\\"w\\\") as f:\\n        json.dump(full_results, f, indent=2, ensure_ascii=False)\\n    print(f\\\"  Results JSON saved to {json_path}\\\", flush=True)\\n\\n    # CSV summary\\n    csv_path = os.path.join(args.output_dir, \\\"stratified_summary.csv\\\")\\n    write_summary_csv(repo_analysis, pool_analysis, sim_analysis, csv_path, dataflow_analysis, neg_diff_analysis)\\n\\n    # Plots\\n    try:\\n        make_plots(repo_analysis, pool_analysis, sim_analysis, args.output_dir, dataflow_analysis, neg_diff_analysis)\\n    except Exception as e:\\n        print(f\\\"  [WARN] Plot generation failed: {e}\\\", flush=True)\\n\\n    print(\\\"\\\\nDone.\\\", flush=True)\\n\\n\\nif __name__ == \\\"__main__\\\":\\n    main()\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bc6af3e6-b801-46b9-8987-3fac4ba868cb",
  "isSidechain": false,
  "promptId": "22ffd1fb-240e-481f-9bcc-b3f6a42d6805",
  "type": "user",
  "uuid": "8a1375b6-d138-41e4-bb07-01689dc52496",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"        REPO_SIZE_BINS.update({k: tuple(v) for k, v in custom.items()})\\\\n    if args.pool_size_bins:\\\\n        custom = json.loads(args.pool_size_bins)\\\\n        POOL_SIZE_BINS.clear()\\\\n        POOL_SIZE_BINS.update({k: tuple(v) for k, v in custom.items()})\\\\n    if args.sim_bins:\\\\n        custom = json.loads(args.sim_bins)\\\\n        SIMILARITY_BINS.clear()\\\\n        SIMILARITY_BINS.update({k: tuple(v) for k, v in custom.items()})\\\\n\\\\n    # Load M1 metadata\\\\n    print(f\\\\\\\"Loading M1 metadata from {args.m1_data}...\\\\\\\", flush=True)\\\\n    inst_to_repo, repo_counts = load_m1_metadata(args.m1_data)\\\\n    print(f\\\\\\\"  {len(inst_to_repo)} instances, {len(repo_counts)} repos\\\\\\\", flush=True)\\\\n\\\\n    # Load dataflow graph if provided\\\\n    dataflow_edges = None\\\\n    if args.dataflow_graph and os.path.exists(args.dataflow_graph):\\\\n        print(f\\\\\\\"Loading dataflow graph from {args.dataflow_graph}...\\\\\\\", flush=True)\\\\n        dataflow_edges = load_dataflow_edges(args.dataflow_graph)\\\\n        print(f\\\\\\\"  {len(dataflow_edges)} file entries\\\\\\\", flush=True)\\\\n\\\\n    # Determine val data directory\\\\n    val_dir = args.val_data_dir\\\\n    if val_dir is None and args.predictions_dir is None and not args.dry_run:\\\\n        val_dir = \\\\\\\"/root/autodl-tmp/structfuse/full_m2_training_data\\\\\\\"\\\\n    if val_dir is None and args.dry_run:\\\\n        val_dir = \\\\\\\"/root/autodl-tmp/structfuse/full_m2_training_data\\\\\\\"\\\\n\\\\n    # Collect per-instance results: {strategy: {seed: [results]}}\\\\n    all_results: Dict[str, Dict[int, List[Dict]]] = defaultdict(dict)\\\\n    val_samples_cache: Dict[str, List[Dict]] = {}\\\\n\\\\n    for strategy in STRATEGIES:\\\\n        for seed in seeds:\\\\n            val_file = os.path.join(val_dir, f\\\\\\\"val_{strategy}_s{seed}.jsonl\\\\\\\") if val_dir else None\\\\n\\\\n            if val_file and os.path.exists(val_file):\\\\n                print(f\\\\\\\"Loading val data: {strategy} seed={seed}...\\\\\\\", flush=True)\\\\n                lite = args.predictions_dir is not None\\\\n                val_samples = load_val_samples(val_file, lite=lite)\\\\n            else:\\\\n                print(f\\\\\\\"  [WARN] Val file not found: {val_file}, skipping\\\\\\\", flush=True)\\\\n                continue\\\\n\\\\n            if args.dry_run:\\\\n                print(f\\\\\\\"  Generating mock predictions: {strategy} seed={seed}\\\\\\\", flush=True)\\\\n                results = mock_predictions(val_samples, strategy, seed)\\\\n            elif args.predictions_dir:\\\\n                pred_pattern = os.path.join(\\\\n                    args.predictions_dir, f\\\\\\\"*{strategy}*s{seed}*.json\\\\\\\"\\\\n                )\\\\n                import glob\\\\n                pred_files = glob.glob(pred_pattern)\\\\n                if pred_files:\\\\n                    print(f\\\\\\\"  Loading predictions: {pred_files[0]}\\\\\\\", flush=True)\\\\n                    results = load_predictions(pred_files[0], val_samples)\\\\n                else:\\\\n                    print(f\\\\\\\"  [WARN] No prediction file matching {pred_pattern}\\\\\\\", flush=True)\\\\n                    continue\\\\n            elif args.checkpoints_dir:\\\\n                base = os.path.join(args.checkpoints_dir, f\\\\\\\"{strategy}_s{seed}\\\\\\\")\\\\n                ckpt_dir = None\\\\n                for subdir in [\\\\\\\"best\\\\\\\", \\\\\\\"best_by_recall_at_1\\\\\\\", \\\\\\\"best_by_val_loss\\\\\\\"]:\\\\n                    candidate = os.path.join(base, subdir)\\\\n                    if os.path.exists(os.path.join(candidate, \\\\\\\"model.pt\\\\\\\")):\\\\n                        ckpt_dir = candidate\\\\n                        break\\\\n                if ckpt_dir is None and os.path.exists(os.path.join(base, \\\\\\\"model.pt\\\\\\\")):\\\\n                    ckpt_dir = base\\\\n                if os.path.exists(ckpt_dir):\\\\n                    print(f\\\\\\\"  Re-evaluating checkpoint: {ckpt_dir}\\\\\\\", flush=True)\\\\n                    results = reeval_checkpoint(\\\\n                        ckpt_dir, val_samples, args.device, args.max_seq_length\\\\n                    )\\\\n                else:\\\\n                    print(f\\\\\\\"  [WARN] Checkpoint not found: {ckpt_dir}\\\\\\\", flush=True)\\\\n                    continue\\\\n            else:\\\\n                print(\\\\\\\"  [ERROR] No --dry-run, --predictions-dir, or --checkpoints-dir\\\\\\\", flush=True)\\\\n                continue\\\\n\\\\n            # Assign strata\\\\n            results = assign_strata(results, inst_to_repo, repo_counts, dataflow_edges)\\\\n\\\\n            # For dry-run or model-based: compute text similarity for sim_bin\\\\n            if args.dry_run:\\\\n                for r, s in zip(results, val_samples):\\\\n                    tsim = text_similarity(s[\\\\\\\"query_tokens\\\\\\\"][:500], s[\\\\\\\"pos_tokens\\\\\\\"][:500])\\\\n                    r[\\\\\\\"sim_bin\\\\\\\"] = _bin_value(tsim, SIMILARITY_BINS)\\\\n\\\\n            all_results[strategy][seed] = results\\\\n            val_samples_cache[f\\\\\\\"{strategy}_s{seed}\\\\\\\"] = val_samples\\\\n            print(f\\\\\\\"  -> {len(results)} instances\\\\\\\", flush=True)\\\\n\\\\n    # Compute neg_difficulty quartiles (text-overlap proxy, CPU-safe)\\\\n    print(\\\\\\\"Computing neg difficulty quartiles...\\\\\\\", flush=True)\\\\n    assign_neg_difficulty_quartiles(all_results, val_samples_cache)\\\\n\\\\n    # Run stratified analysis\\\\n    print(\\\\\\\"\\\\\\\\nRunning stratified analysis...\\\\\\\", flush=True)\\\\n    repo_analysis = run_stratified_analysis(\\\\n        all_results, \\\\\\\"repo_size_bin\\\\\\\", list(REPO_SIZE_BINS.keys()), args.n_bootstrap\\\\n    )\\\\n    pool_analysis = run_stratified_analysis(\\\\n        all_results, \\\\\\\"pool_size_bin\\\\\\\", list(POOL_SIZE_BINS.keys()), args.n_bootstrap\\\\n    )\\\\n    sim_analysis = run_stratified_analysis(\\\\n        all_results, \\\\\\\"sim_bin\\\\\\\", list(SIMILARITY_BINS.keys()), args.n_bootstrap\\\\n    )\\\\n\\\\n    dataflow_analysis = {}\\\\n    if dataflow_edges is not None:\\\\n        dataflow_analysis = run_stratified_analysis(\\\\n            all_results, \\\\\\\"dataflow_bin\\\\\\\", list(DATAFLOW_BINS.keys()), args.n_bootstrap\\\\n        )\\\\n\\\\n    neg_diff_analysis = run_stratified_analysis(\\\\n        all_results, \\\\\\\"neg_difficulty_bin\\\\\\\", NEG_DIFFICULTY_QUARTILE_LABELS, args.n_bootstrap\\\\n    )\\\\n\\\\n    # Save JSON\\\\n    full_results = {\\\\n        \\\\\\\"config\\\\\\\": {\\\\n            \\\\\\\"strategies\\\\\\\": STRATEGIES,\\\\n            \\\\\\\"seeds\\\\\\\": seeds,\\\\n            \\\\\\\"repo_size_bins\\\\\\\": {k: list(v) for k, v in REPO_SIZE_BINS.items()},\\\\n            \\\\\\\"pool_size_bins\\\\\\\": {k: list(v) for k, v in POOL_SIZE_BINS.items()},\\\\n            \\\\\\\"similarity_bins\\\\\\\": {k: list(v) for k, v in SIMILARITY_BINS.items()},\\\\n            \\\\\\\"dataflow_bins\\\\\\\": {k: list(v) for k, v in DATAFLOW_BINS.items()},\\\\n            \\\\\\\"neg_difficulty_quartiles\\\\\\\": NEG_DIFFICULTY_QUARTILE_LABELS,\\\\n            \\\\\\\"n_bootstrap\\\\\\\": args.n_bootstrap,\\\\n            \\\\\\\"dry_run\\\\\\\": args.dry_run,\\\\n        },\\\\n        \\\\\\\"by_repo_size\\\\\\\": repo_analysis,\\\\n        \\\\\\\"by_pool_size\\\\\\\": pool_analysis,\\\\n        \\\\\\\"by_similarity\\\\\\\": sim_analysis,\\\\n        \\\\\\\"by_dataflow\\\\\\\": dataflow_analysis,\\\\n        \\\\\\\"by_neg_difficulty\\\\\\\": neg_diff_analysis,\\\\n    }\\\\n\\\\n    json_path = os.path.join(args.output_dir, \\\\\\\"stratified_results.json\\\\\\\")\\\\n    with open(json_path, \\\\\\\"w\\\\\\\") as f:\\\\n        json.dump(full_results, f, indent=2, ensure_ascii=False)\\\\n    print(f\\\\\\\"  Results JSON saved to {json_path}\\\\\\\", flush=True)\\\\n\\\\n    # CSV summary\\\\n    csv_path = os.path.join(args.output_dir, \\\\\\\"stratified_summary.csv\\\\\\\")\\\\n    write_summary_csv(repo_analysis, pool_analysis, sim_analysis, csv_path, dataflow_analysis, neg_diff_analysis)\\\\n\\\\n    # Plots\\\\n    try:\\\\n        make_plots(repo_analysis, pool_analysis, sim_analysis, args.output_dir, dataflow_analysis, neg_diff_analysis)\\\\n    except Exception as e:\\\\n        print(f\\\\\\\"  [WARN] Plot generation failed: {e}\\\\\\\", flush=True)\\\\n\\\\n    print(\\\\\\\"\\\\\\\\nDone.\\\\\\\", flush=True)\\\\n\\\\n\\\\nif __name__ == \\\\\\\"__main__\\\\\\\":\\\\n    main()\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.35}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"        REPO_SIZE_BINS.update({k: tuple(v) for k, v in custom.items()})\\n    if args.pool_size_bins:\\n        custom = json.loads(args.pool_size_bins)\\n        POOL_SIZE_BINS.clear()\\n        POOL_SIZE_BINS.update({k: tuple(v) for k, v in custom.items()})\\n    if args.sim_bins:\\n        custom = json.loads(args.sim_bins)\\n        SIMILARITY_BINS.clear()\\n        SIMILARITY_BINS.update({k: tuple(v) for k, v in custom.items()})\\n\\n    # Load M1 metadata\\n    print(f\\\"Loading M1 metadata from {args.m1_data}...\\\", flush=True)\\n    inst_to_repo, repo_counts = load_m1_metadata(args.m1_data)\\n    print(f\\\"  {len(inst_to_repo)} instances, {len(repo_counts)} repos\\\", flush=True)\\n\\n    # Load dataflow graph if provided\\n    dataflow_edges = None\\n    if args.dataflow_graph and os.path.exists(args.dataflow_graph):\\n        print(f\\\"Loading dataflow graph from {args.dataflow_graph}...\\\", flush=True)\\n        dataflow_edges = load_dataflow_edges(args.dataflow_graph)\\n        print(f\\\"  {len(dataflow_edges)} file entries\\\", flush=True)\\n\\n    # Determine val data directory\\n    val_dir = args.val_data_dir\\n    if val_dir is None and args.predictions_dir is None and not args.dry_run:\\n        val_dir = \\\"/root/autodl-tmp/structfuse/full_m2_training_data\\\"\\n    if val_dir is None and args.dry_run:\\n        val_dir = \\\"/root/autodl-tmp/structfuse/full_m2_training_data\\\"\\n\\n    # Collect per-instance results: {strategy: {seed: [results]}}\\n    all_results: Dict[str, Dict[int, List[Dict]]] = defaultdict(dict)\\n    val_samples_cache: Dict[str, List[Dict]] = {}\\n\\n    for strategy in STRATEGIES:\\n        for seed in seeds:\\n            val_file = os.path.join(val_dir, f\\\"val_{strategy}_s{seed}.jsonl\\\") if val_dir else None\\n\\n            if val_file and os.path.exists(val_file):\\n                print(f\\\"Loading val data: {strategy} seed={seed}...\\\", flush=True)\\n                lite = args.predictions_dir is not None\\n                val_samples = load_val_samples(val_file, lite=lite)\\n            else:\\n                print(f\\\"  [WARN] Val file not found: {val_file}, skipping\\\", flush=True)\\n                continue\\n\\n            if args.dry_run:\\n                print(f\\\"  Generating mock predictions: {strategy} seed={seed}\\\", flush=True)\\n                results = mock_predictions(val_samples, strategy, seed)\\n            elif args.predictions_dir:\\n                pred_pattern = os.path.join(\\n                    args.predictions_dir, f\\\"*{strategy}*s{seed}*.json\\\"\\n                )\\n                import glob\\n                pred_files = glob.glob(pred_pattern)\\n                if pred_files:\\n                    print(f\\\"  Loading predictions: {pred_files[0]}\\\", flush=True)\\n                    results = load_predictions(pred_files[0], val_samples)\\n                else:\\n                    print(f\\\"  [WARN] No prediction file matching {pred_pattern}\\\", flush=True)\\n                    continue\\n            elif args.checkpoints_dir:\\n                base = os.path.join(args.checkpoints_dir, f\\\"{strategy}_s{seed}\\\")\\n                ckpt_dir = None\\n                for subdir in [\\\"best\\\", \\\"best_by_recall_at_1\\\", \\\"best_by_val_loss\\\"]:\\n                    candidate = os.path.join(base, subdir)\\n                    if os.path.exists(os.path.join(candidate, \\\"model.pt\\\")):\\n                        ckpt_dir = candidate\\n                        break\\n                if ckpt_dir is None and os.path.exists(os.path.join(base, \\\"model.pt\\\")):\\n                    ckpt_dir = base\\n                if os.path.exists(ckpt_dir):\\n                    print(f\\\"  Re-evaluating checkpoint: {ckpt_dir}\\\", flush=True)\\n                    results = reeval_checkpoint(\\n                        ckpt_dir, val_samples, args.device, args.max_seq_length\\n                    )\\n                else:\\n                    print(f\\\"  [WARN] Checkpoint not found: {ckpt_dir}\\\", flush=True)\\n                    continue\\n            else:\\n                print(\\\"  [ERROR] No --dry-run, --predictions-dir, or --checkpoints-dir\\\", flush=True)\\n                continue\\n\\n            # Assign strata\\n            results = assign_strata(results, inst_to_repo, repo_counts, dataflow_edges)\\n\\n            # For dry-run or model-based: compute text similarity for sim_bin\\n            if args.dry_run:\\n                for r, s in zip(results, val_samples):\\n                    tsim = text_similarity(s[\\\"query_tokens\\\"][:500], s[\\\"pos_tokens\\\"][:500])\\n                    r[\\\"sim_bin\\\"] = _bin_value(tsim, SIMILARITY_BINS)\\n\\n            all_results[strategy][seed] = results\\n            val_samples_cache[f\\\"{strategy}_s{seed}\\\"] = val_samples\\n            print(f\\\"  -> {len(results)} instances\\\", flush=True)\\n\\n    # Compute neg_difficulty quartiles (text-overlap proxy, CPU-safe)\\n    print(\\\"Computing neg difficulty quartiles...\\\", flush=True)\\n    assign_neg_difficulty_quartiles(all_results, val_samples_cache)\\n\\n    # Run stratified analysis\\n    print(\\\"\\\\nRunning stratified analysis...\\\", flush=True)\\n    repo_analysis = run_stratified_analysis(\\n        all_results, \\\"repo_size_bin\\\", list(REPO_SIZE_BINS.keys()), args.n_bootstrap\\n    )\\n    pool_analysis = run_stratified_analysis(\\n        all_results, \\\"pool_size_bin\\\", list(POOL_SIZE_BINS.keys()), args.n_bootstrap\\n    )\\n    sim_analysis = run_stratified_analysis(\\n        all_results, \\\"sim_bin\\\", list(SIMILARITY_BINS.keys()), args.n_bootstrap\\n    )\\n\\n    dataflow_analysis = {}\\n    if dataflow_edges is not None:\\n        dataflow_analysis = run_stratified_analysis(\\n            all_results, \\\"dataflow_bin\\\", list(DATAFLOW_BINS.keys()), args.n_bootstrap\\n        )\\n\\n    neg_diff_analysis = run_stratified_analysis(\\n        all_results, \\\"neg_difficulty_bin\\\", NEG_DIFFICULTY_QUARTILE_LABELS, args.n_bootstrap\\n    )\\n\\n    # Save JSON\\n    full_results = {\\n        \\\"config\\\": {\\n            \\\"strategies\\\": STRATEGIES,\\n            \\\"seeds\\\": seeds,\\n            \\\"repo_size_bins\\\": {k: list(v) for k, v in REPO_SIZE_BINS.items()},\\n            \\\"pool_size_bins\\\": {k: list(v) for k, v in POOL_SIZE_BINS.items()},\\n            \\\"similarity_bins\\\": {k: list(v) for k, v in SIMILARITY_BINS.items()},\\n            \\\"dataflow_bins\\\": {k: list(v) for k, v in DATAFLOW_BINS.items()},\\n            \\\"neg_difficulty_quartiles\\\": NEG_DIFFICULTY_QUARTILE_LABELS,\\n            \\\"n_bootstrap\\\": args.n_bootstrap,\\n            \\\"dry_run\\\": args.dry_run,\\n        },\\n        \\\"by_repo_size\\\": repo_analysis,\\n        \\\"by_pool_size\\\": pool_analysis,\\n        \\\"by_similarity\\\": sim_analysis,\\n        \\\"by_dataflow\\\": dataflow_analysis,\\n        \\\"by_neg_difficulty\\\": neg_diff_analysis,\\n    }\\n\\n    json_path = os.path.join(args.output_dir, \\\"stratified_results.json\\\")\\n    with open(json_path, \\\"w\\\") as f:\\n        json.dump(full_results, f, indent=2, ensure_ascii=False)\\n    print(f\\\"  Results JSON saved to {json_path}\\\", flush=True)\\n\\n    # CSV summary\\n    csv_path = os.path.join(args.output_dir, \\\"stratified_summary.csv\\\")\\n    write_summary_csv(repo_analysis, pool_analysis, sim_analysis, csv_path, dataflow_analysis, neg_diff_analysis)\\n\\n    # Plots\\n    try:\\n        make_plots(repo_analysis, pool_analysis, sim_analysis, args.output_dir, dataflow_analysis, neg_diff_analysis)\\n    except Exception as e:\\n        print(f\\\"  [WARN] Plot generation failed: {e}\\\", flush=True)\\n\\n    print(\\\"\\\\nDone.\\\", flush=True)\\n\\n\\nif __name__ == \\\"__main__\\\":\\n    main()\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"
    }
  },
  "sourceToolAssistantUUID": "bc6af3e6-b801-46b9-8987-3fac4ba868cb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "bda3dfbf-4b90-494d-b674-2597173fd381",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 73 · 2026-05-14T20:49:31.412Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a comprehensive understanding of the full file. Let me summarize the structure:

**File structure (910 lines):**
1. Lines 1-62: Imports, STRATEGIES, bin definitions
2. Lines 64-70: `_bin_value()` 
3. Lines 73-90: `load_m1_metadata()`
4. Lines 93-99: `load_dataflow_edges()`
5. Lines 102-141: `load_val_samples()`
6. Lines 143-151: `text_similarity()`
7. Lines 154-228: `reeval_checkpoint()`


8. Lines 230-266: `load_predictions()`
9. Lines 268-297: `mock_predictions()` - this is where I need to fix the deterministic seed issue
10. Lines 300-310: `compute_metrics()`
11. Lines 313-315: `_metric_fn()`
12. Lines 318-342: `bootstrap_ci()`
13. Lines 345-365: `assign_strata()`
14. Lines 368-414: `assign_neg_difficulty_quartiles()`
15. Lines 416-422: `group_by()`
16. Lines 425-472: `run_stratified_analysis()`
17. Lines 474-647: `make_plots()`
18. Lines 649 onwards: remaining code including `write_summary_csv()` and `main()`

Now I need to add three major pieces: a pool-size controlled analysis that isolates the effect within each pool bin to remove the confound where larger pools artificially lower R@1, a cross-analysis function examining the dataflow and pool-size interaction with underpowered cell detection, fix the mock predictions to use a deterministic offset instead of hashing, and integrate all these into main with appropriate output saving.

Let me map out the changes strategically across the 910-line file.

Defining the strategy seed offset mapping...

Now I'm adding a new analysis function that controls for pool size confounding by binning results and comparing strategies within the same pool size ranges to isolate the true strategy effect from pool-size artifacts.

Filtering results by pool size bin and computing metrics for each strategy, then calculating bootstrap confidence intervals for R@1 performance and computing deltas between strategies within each bin...

Now I'm aggregating those within-bin deltas into a weighted average across all pool size bins, weighting by the count of results in each bin. Building the cross-tabulation analysis... Now I'm computing the performance delta between each strategy and the random baseline within each cell, then I need to implement several changes to the analysis pipeline including new CSV sections for pool-controlled and cross analysis, additional plots, and updates to the main function to orchestrate everything—I'm thinking the cleanest approach is to write out the full updated file and apply it all at once. I'm going back and forth on the best approach here. Writing a standalone Python script that reads the original file, applies all the modifications systematically, and outputs the result seems cleanest—I can use ssh_execute to run it directly on the server. Let me map out exactly which lines need changing so I can build the patch logic. I'm laying out the full scope of changes needed across multiple sections of the file, then deciding to write a comprehensive patch script that reads the original file and applies all the modifications systematically rather than trying to do complex inline edits. I'm mapping out all the changes needed across the file—updating function signatures, adding new analysis calls, inserting plot generation code, and modifying the CSV output. Rather than trying to write the entire 1000+ line file directly via SSH, I'll create a Python patch script that reads the original, makes targeted string replacements at specific line numbers, and writes the modified version back. I'm working through different strategies for modifying the file remotely. Writing it locally and transferring via heredoc syntax could get messy with escaping on a large Python file. Instead, I'll take a more practical approach: write the complete modified file locally, then use a series of smaller ssh commands to build it piece by piece on the server, or write a patch script that handles the modifications programmatically. Writing the patch script... Writing the patch script... I'm laying out the specific modifications needed: fixing the seed calculation for mock predictions with a strategy-based offset mapping, inserting two new analysis functions before the plotting routine, and updating the make_plots signature with additional parameters. I'm adding two new optional parameters to handle pool-controlled and cross-analysis data throughout the pipeline. I need to integrate these new analyses into the plotting function, CSV output, and main execution flow, computing them after the negative difference analysis and passing them through to the summary writer. Writing the patch script...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8a1375b6-d138-41e4-bb07-01689dc52496",
  "isSidechain": false,
  "requestId": "req_011Cb37o5zs8oHZ1Ltwy3wLy",
  "type": "assistant",
  "uuid": "c8e9ead3-1f0f-4280-ab23-cdf0d4d35a73",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "bda3dfbf-4b90-494d-b674-2597173fd381",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FZtRRf2s3JK5v8tk8b8VAc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2839,
      "cache_read_input_tokens": 61200,
      "output_tokens": 6288,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2839,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 6288,
          "cache_read_input_tokens": 61200,
          "cache_creation_input_tokens": 2839,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2839
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

_source line 74 · 2026-05-14T20:49:31.414Z_

Now I have a complete picture of the 910-line file. Let me write the patch. I'll create a Python patch script on the server and execute it.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c8e9ead3-1f0f-4280-ab23-cdf0d4d35a73",
  "isSidechain": false,
  "requestId": "req_011Cb37o5zs8oHZ1Ltwy3wLy",
  "type": "assistant",
  "uuid": "e9391981-657a-428b-85a4-83e56e3ad32c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "bda3dfbf-4b90-494d-b674-2597173fd381",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FZtRRf2s3JK5v8tk8b8VAc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2839,
      "cache_read_input_tokens": 61200,
      "output_tokens": 6288,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2839,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 6288,
          "cache_read_input_tokens": 61200,
          "cache_creation_input_tokens": 2839,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2839
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

_source line 75 · 2026-05-14T20:49:32.086Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_01P1Y2DuvAuz8LKyxo5tavJL`</summary>

```json
{
  "server": "bjb1-42106",
  "command": "cp /root/structfuse/evaluation/analyze_stratified.py /root/structfuse/evaluation/analyze_stratified.py.bak_v2",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e9391981-657a-428b-85a4-83e56e3ad32c",
  "isSidechain": false,
  "requestId": "req_011Cb37o5zs8oHZ1Ltwy3wLy",
  "type": "assistant",
  "uuid": "0f2fec09-25ed-4513-8ab7-6e34c6d345a4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "bda3dfbf-4b90-494d-b674-2597173fd381",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FZtRRf2s3JK5v8tk8b8VAc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2839,
      "cache_read_input_tokens": 61200,
      "output_tokens": 6288,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2839,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 6288,
          "cache_read_input_tokens": 61200,
          "cache_creation_input_tokens": 2839,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2839
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

_source line 76_

```json
{
  "type": "last-prompt",
  "leafUuid": "0f2fec09-25ed-4513-8ab7-6e34c6d345a4",
  "sessionId": "bda3dfbf-4b90-494d-b674-2597173fd381"
}
```

---

### Runtime record

_source line 77_

```json
{
  "type": "ai-title",
  "aiTitle": "Add pool-size controlled stratified evaluation to analysis script",
  "sessionId": "bda3dfbf-4b90-494d-b674-2597173fd381"
}
```

---

### Tool result

_source line 78 · 2026-05-14T20:49:32.466Z_

<details><summary>↩ Tool result · `toolu_01P1Y2DuvAuz8LKyxo5tavJL`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0f2fec09-25ed-4513-8ab7-6e34c6d345a4",
  "isSidechain": false,
  "promptId": "22ffd1fb-240e-481f-9bcc-b3f6a42d6805",
  "type": "user",
  "uuid": "70bd0f83-7af7-4d51-9883-156b9b9447df",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.36}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"
    }
  },
  "sourceToolAssistantUUID": "0f2fec09-25ed-4513-8ab7-6e34c6d345a4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "bda3dfbf-4b90-494d-b674-2597173fd381",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 79 · 2026-05-14T20:49:32.470Z_

```json
{
  "parentUuid": "70bd0f83-7af7-4d51-9883-156b9b9447df",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "281adda7-32f4-4b4a-8902-691ccfafceb6",
  "timestamp": "2026-05-14T20:49:32.470Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "bda3dfbf-4b90-494d-b674-2597173fd381",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 80 · 2026-05-14T20:51:02.240Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_011NdciqaqsKnWtEiuCSPKtY`</summary>

```json
{
  "server": "bjb1-42106",
  "command": "cat > /tmp/patch_stratified.py << 'PATCH_EOF'\n#!/usr/bin/env python3\n\"\"\"Patch analyze_stratified.py: add pool_size-controlled analysis, cross-analysis, fix seed.\"\"\"\nimport shutil\n\nSRC = '/root/structfuse/evaluation/analyze_stratified.py'\n\nwith open(SRC) as f:\n    content = f.read()\n\n# ═══════════════════════════════════════════════════════════════════\n# 1. Fix mock_predictions deterministic seed\n# ═══════════════════════════════════════════════════════════════════\ncontent = content.replace(\n    '    rng = np.random.RandomState(seed + abs(hash(strategy)) % 10000)',\n    '    STRATEGY_SEED_OFFSET = {\"random\": 0, \"embedding_distance\": 1, \"dataflow_aware\": 2, \"bm25\": 3}\\n'\n    '    rng = np.random.RandomState(seed + STRATEGY_SEED_OFFSET.get(strategy, hash(strategy) % 10000) * 10000)'\n)\n\n# ═══════════════════════════════════════════════════════════════════\n# 2. Insert new analysis functions before make_plots\n# ═══════════════════════════════════════════════════════════════════\nNEW_FUNCS = '''\n# ── Pool-size controlled analysis (confound adjustment) ──────────────\n\ndef run_pool_size_controlled_analysis(\n    all_results: Dict[str, Dict[int, List[Dict]]],\n    n_bootstrap: int = 1000,\n) -> Dict:\n    \"\"\"Compare strategies within same pool_size bins to control for pool size confound.\n\n    Rich-dataflow instances tend to have larger candidate pools, making R@1\n    inherently lower. By matching on pool_size before comparing strategies,\n    this isolates the true strategy effect from pool-size confounding.\n\n    Args:\n        all_results: {strategy: {seed: [result_dicts]}}\n        n_bootstrap: bootstrap iterations for CI\n\n    Returns:\n        Dict with per-pool_size_bin per-strategy metrics, within-bin deltas,\n        and aggregate weighted delta.\n    \"\"\"\n    analysis = {}\n    for pool_bin in POOL_SIZE_BINS:\n        analysis[pool_bin] = {}\n        for strategy in STRATEGIES:\n            bin_results = []\n            for seed, results in all_results.get(strategy, {}).items():\n                for r in results:\n                    if r.get(\"pool_size_bin\") == pool_bin:\n                        bin_results.append(r)\n\n            metrics = compute_metrics(bin_results)\n            ci_r1 = bootstrap_ci(bin_results, \"R@1\", n_bootstrap)\n            ci_r5 = bootstrap_ci(bin_results, \"R@5\", n_bootstrap)\n            ci_mrr = bootstrap_ci(bin_results, \"MRR\", n_bootstrap)\n            analysis[pool_bin][strategy] = {\n                \"R@1\": ci_r1[0],\n                \"R@1_ci\": [ci_r1[1], ci_r1[2]],\n                \"R@5\": ci_r5[0],\n                \"R@5_ci\": [ci_r5[1], ci_r5[2]],\n                \"MRR\": ci_mrr[0],\n                \"MRR_ci\": [ci_mrr[1], ci_mrr[2]],\n                \"count\": metrics[\"count\"],\n            }\n\n        # Within-bin deltas (controlled for pool size)\n        rand_m = analysis[pool_bin].get(\"random\", {})\n        for other in [\"embedding_distance\", \"dataflow_aware\"]:\n            other_m = analysis[pool_bin].get(other, {})\n            delta_key = f\"{other}_vs_random\"\n            if rand_m and other_m:\n                for metric in [\"R@1\", \"R@5\", \"MRR\"]:\n                    rv = rand_m.get(metric, 0)\n                    ov = other_m.get(metric, 0)\n                    analysis[pool_bin].setdefault(delta_key, {})[f\"{metric}_delta\"] = ov - rv\n                    analysis[pool_bin][delta_key][f\"{metric}_rel_pct\"] = (\n                        (ov - rv) / rv * 100 if rv > 0 else 0.0\n                    )\n\n    # Aggregate controlled delta: count-weighted average of within-bin deltas\n    for other in [\"embedding_distance\", \"dataflow_aware\"]:\n        delta_key = f\"{other}_vs_random\"\n        total_n = 0\n        weighted_delta = 0.0\n        for pool_bin in POOL_SIZE_BINS:\n            n = analysis[pool_bin].get(other, {}).get(\"count\", 0)\n            d = analysis[pool_bin].get(delta_key, {}).get(\"R@1_delta\", 0)\n            weighted_delta += d * n\n            total_n += n\n        analysis[f\"aggregate_{delta_key}\"] = {\n            \"R@1_weighted_delta\": weighted_delta / total_n if total_n > 0 else 0.0,\n            \"total_n\": total_n,\n        }\n\n    return analysis\n\n\ndef run_dataflow_pool_cross_analysis(\n    all_results: Dict[str, Dict[int, List[Dict]]],\n    n_bootstrap: int = 1000,\n    min_cell_size: int = 30,\n) -> Dict:\n    \"\"\"Cross-tabulation of (dataflow_bin x pool_size_bin) -> R@1 per strategy.\n\n    Cells with fewer than min_cell_size samples are flagged as underpowered.\n    This reveals whether the dataflow advantage holds after controlling for\n    pool size, and in which pool_size/dataflow combinations it is strongest.\n\n    Args:\n        all_results: {strategy: {seed: [result_dicts]}}\n        n_bootstrap: bootstrap iterations for CI\n        min_cell_size: minimum samples per cell; below this, flag underpowered\n\n    Returns:\n        Dict keyed by \"dataflow_bin::pool_size_bin\" with per-strategy R@1 and deltas.\n    \"\"\"\n    analysis = {}\n    for df_bin in DATAFLOW_BINS:\n        for pool_bin in POOL_SIZE_BINS:\n            cell_key = f\"{df_bin}::{pool_bin}\"\n            analysis[cell_key] = {}\n            for strategy in STRATEGIES:\n                cell_results = []\n                for seed, results in all_results.get(strategy, {}).items():\n                    for r in results:\n                        if r.get(\"dataflow_bin\") == df_bin and r.get(\"pool_size_bin\") == pool_bin:\n                            cell_results.append(r)\n\n                n = len(cell_results)\n                underpowered = n < min_cell_size\n\n                if n > 0:\n                    ci_r1 = bootstrap_ci(cell_results, \"R@1\", n_bootstrap)\n                    analysis[cell_key][strategy] = {\n                        \"R@1\": ci_r1[0],\n                        \"R@1_ci\": [ci_r1[1], ci_r1[2]],\n                        \"count\": n,\n                        \"underpowered\": underpowered,\n                    }\n                else:\n                    analysis[cell_key][strategy] = {\n                        \"R@1\": 0.0,\n                        \"R@1_ci\": [0.0, 0.0],\n                        \"count\": 0,\n                        \"underpowered\": True,\n                    }\n\n            # Within-cell deltas\n            rand_r1 = analysis[cell_key].get(\"random\", {}).get(\"R@1\", 0)\n            for other in [\"embedding_distance\", \"dataflow_aware\"]:\n                other_r1 = analysis[cell_key].get(other, {}).get(\"R@1\", 0)\n                delta_key = f\"{other}_vs_random\"\n                analysis[cell_key][delta_key] = {\n                    \"R@1_delta\": other_r1 - rand_r1,\n                    \"R@1_rel_pct\": (other_r1 - rand_r1) / rand_r1 * 100 if rand_r1 > 0 else 0.0,\n                }\n\n    return analysis\n\n\n'''\n\ncontent = content.replace(\n    '\\ndef make_plots(',\n    NEW_FUNCS + 'def make_plots(',\n    1\n)\n\n# ═══════════════════════════════════════════════════════════════════\n# 3. Add params to make_plots signature\n# ═══════════════════════════════════════════════════════════════════\ncontent = content.replace(\n    '''def make_plots(\n    repo_analysis: Dict,\n    pool_analysis: Dict,\n    sim_analysis: Dict,\n    output_dir: str,\n    dataflow_analysis: Optional[Dict] = None,\n    neg_diff_analysis: Optional[Dict] = None,\n):''',\n    '''def make_plots(\n    repo_analysis: Dict,\n    pool_analysis: Dict,\n    sim_analysis: Dict,\n    output_dir: str,\n    dataflow_analysis: Optional[Dict] = None,\n    neg_diff_analysis: Optional[Dict] = None,\n    pool_controlled_analysis: Optional[Dict] = None,\n    cross_analysis: Optional[Dict] = None,\n):'''\n)\n\n# ═══════════════════════════════════════════════════════════════════\n# 4. Add plots for pool-controlled and cross analysis (before \"Also save\")\n# ═══════════════════════════════════════════════════════════════════\nNEW_PLOTS = '''\n        # ── Plot 4: Pool-size controlled delta comparison ──\n        if pool_controlled_analysis:\n            pool_bins = [b for b in POOL_SIZE_BINS if b in pool_controlled_analysis]\n            if pool_bins:\n                fig, axes = plt.subplots(1, 2, figsize=(12, 5))\n                fig.suptitle(\"Pool-Size Controlled Strategy Comparison\", fontweight=\"bold\", y=1.02)\n\n                # Left: R@1 per pool_size bin per strategy\n                ax = axes[0]\n                x = np.arange(len(pool_bins))\n                width = 0.25\n                for i, strategy in enumerate(STRATEGIES):\n                    vals = [pool_controlled_analysis[b].get(strategy, {}).get(\"R@1\", 0) for b in pool_bins]\n                    offset = (i - 1) * width\n                    ax.bar(x + offset, vals, width, label=STRATEGY_LABELS[strategy],\n                           color=STRATEGY_COLORS[strategy], alpha=0.85)\n                ax.set_xlabel(\"Pool Size Bin\")\n                ax.set_ylabel(\"R@1\")\n                ax.set_title(\"R@1 by Pool Size (controlled)\")\n                ax.set_xticks(x)\n                ax.set_xticklabels(pool_bins)\n                ax.legend(loc=\"best\")\n                ax.set_ylim(bottom=0)\n\n                # Right: Within-bin delta\n                ax = axes[1]\n                for other, color, marker in [\n                    (\"embedding_distance\", \"#DD8452\", \"o\"),\n                    (\"dataflow_aware\", \"#55A868\", \"s\"),\n                ]:\n                    delta_key = f\"{other}_vs_random\"\n                    deltas = [pool_controlled_analysis[b].get(delta_key, {}).get(\"R@1_delta\", 0) for b in pool_bins]\n                    ax.plot(x, deltas, marker=marker, linewidth=2, markersize=8,\n                            color=color, label=f\"{STRATEGY_LABELS[other]} - Random\")\n\n                # Show aggregate weighted delta as horizontal lines\n                for other, color, ls in [\n                    (\"embedding_distance\", \"#DD8452\", \"--\"),\n                    (\"dataflow_aware\", \"#55A868\", \":\"),\n                ]:\n                    agg_key = f\"aggregate_{other}_vs_random\"\n                    agg = pool_controlled_analysis.get(agg_key, {})\n                    if agg:\n                        ax.axhline(y=agg[\"R@1_weighted_delta\"], color=color, linestyle=ls,\n                                   linewidth=1.5, alpha=0.7,\n                                   label=f\"{STRATEGY_LABELS[other]} wt.avg={agg['R@1_weighted_delta']:.4f}\")\n\n                ax.axhline(y=0, color=\"gray\", linestyle=\"--\", linewidth=0.8)\n                ax.set_xlabel(\"Pool Size Bin\")\n                ax.set_ylabel(\"R@1 Delta (vs Random)\")\n                ax.set_title(\"Within-Bin Delta (pool-size controlled)\")\n                ax.set_xticks(x)\n                ax.set_xticklabels(pool_bins)\n                ax.legend(loc=\"best\", fontsize=8)\n                plt.tight_layout()\n                pdf.savefig(fig, bbox_inches=\"tight\")\n                plt.close(fig)\n\n        # ── Plot 5: Dataflow × Pool Size cross-analysis heatmap ──\n        if cross_analysis:\n            df_bins = list(DATAFLOW_BINS.keys())\n            p_bins = list(POOL_SIZE_BINS.keys())\n            for strategy in STRATEGIES:\n                data_matrix = np.zeros((len(df_bins), len(p_bins)))\n                annot_matrix = []\n                for i, df_bin in enumerate(df_bins):\n                    row_annot = []\n                    for j, p_bin in enumerate(p_bins):\n                        cell_key = f\"{df_bin}::{p_bin}\"\n                        cell = cross_analysis.get(cell_key, {}).get(strategy, {})\n                        r1 = cell.get(\"R@1\", 0)\n                        n = cell.get(\"count\", 0)\n                        up = cell.get(\"underpowered\", True)\n                        data_matrix[i, j] = r1\n                        label = f\"{r1:.3f}\\\\n(n={n})\"\n                        if up:\n                            label += \"\\\\n*\"\n                        row_annot.append(label)\n                    annot_matrix.append(row_annot)\n\n                fig, ax = plt.subplots(figsize=(7, 4))\n                im = ax.imshow(data_matrix, cmap=\"YlOrRd\", aspect=\"auto\", vmin=0)\n                ax.set_xticks(range(len(p_bins)))\n                ax.set_xticklabels(p_bins)\n                ax.set_yticks(range(len(df_bins)))\n                ax.set_yticklabels(df_bins)\n                ax.set_xlabel(\"Pool Size Bin\")\n                ax.set_ylabel(\"Dataflow Bin\")\n                ax.set_title(f\"R@1: {STRATEGY_LABELS[strategy]} (dataflow x pool_size)\\\\n* = underpowered (n<30)\",\n                             fontweight=\"bold\")\n\n                for i in range(len(df_bins)):\n                    for j in range(len(p_bins)):\n                        val = data_matrix[i, j]\n                        color = \"white\" if val > data_matrix.max() * 0.6 else \"black\"\n                        ax.text(j, i, annot_matrix[i][j], ha=\"center\", va=\"center\",\n                                color=color, fontsize=8, fontweight=\"bold\")\n\n                fig.colorbar(im, ax=ax, shrink=0.8)\n                plt.tight_layout()\n                pdf.savefig(fig, bbox_inches=\"tight\")\n                plt.close(fig)\n\n'''\n\ncontent = content.replace(\n    '    # Also save individual PNGs',\n    NEW_PLOTS + '    # Also save individual PNGs'\n)\n\n# ═══════════════════════════════════════════════════════════════════\n# 5. Add params to write_summary_csv signature\n# ═══════════════════════════════════════════════════════════════════\ncontent = content.replace(\n    '''def write_summary_csv(\n    repo_analysis: Dict,\n    pool_analysis: Dict,\n    sim_analysis: Dict,\n    output_path: str,\n    dataflow_analysis: Optional[Dict] = None,\n    neg_diff_analysis: Optional[Dict] = None,\n):''',\n    '''def write_summary_csv(\n    repo_analysis: Dict,\n    pool_analysis: Dict,\n    sim_analysis: Dict,\n    output_path: str,\n    dataflow_analysis: Optional[Dict] = None,\n    neg_diff_analysis: Optional[Dict] = None,\n    pool_controlled_analysis: Optional[Dict] = None,\n    cross_analysis: Optional[Dict] = None,\n):'''\n)\n\n# ═══════════════════════════════════════════════════════════════════\n# 6. Add CSV rows for pool_controlled and cross analysis\n# ═══════════════════════════════════════════════════════════════════\nNEW_CSV_ROWS = '''\n    # Pool-size controlled rows\n    if pool_controlled_analysis:\n        for b in list(POOL_SIZE_BINS.keys()):\n            if b not in pool_controlled_analysis:\n                continue\n            for strategy in STRATEGIES:\n                m = pool_controlled_analysis[b].get(strategy, {})\n                ci_r1 = m.get(\"R@1_ci\", [0, 0])\n                row = {\n                    \"dimension\": \"pool_size_controlled\",\n                    \"stratum\": b,\n                    \"strategy\": strategy,\n                    \"R@1\": f\"{m.get('R@1', 0):.4f}\",\n                    \"R@1_ci95\": f\"[{ci_r1[0]:.4f}, {ci_r1[1]:.4f}]\",\n                    \"R@5\": f\"{m.get('R@5', 0):.4f}\",\n                    \"MRR\": f\"{m.get('MRR', 0):.4f}\",\n                    \"count\": m.get(\"count\", 0),\n                }\n                rows.append(row)\n            for other in [\"embedding_distance\", \"dataflow_aware\"]:\n                dk = f\"{other}_vs_random\"\n                d = pool_controlled_analysis[b].get(dk, {})\n                if d:\n                    row = {\n                        \"dimension\": \"pool_size_controlled\",\n                        \"stratum\": b,\n                        \"strategy\": f\"DELTA({STRATEGY_LABELS[other]}-Random)\",\n                        \"R@1\": f\"{d.get('R@1_delta', 0):+.4f}\",\n                        \"R@1_ci95\": f\"({d.get('R@1_rel_pct', 0):+.1f}%)\",\n                        \"R@5\": f\"{d.get('R@5_delta', 0):+.4f}\",\n                        \"MRR\": f\"{d.get('MRR_delta', 0):+.4f}\",\n                        \"count\": \"\",\n                    }\n                    rows.append(row)\n        # Aggregate weighted deltas\n        for other in [\"embedding_distance\", \"dataflow_aware\"]:\n            agg_key = f\"aggregate_{other}_vs_random\"\n            agg = pool_controlled_analysis.get(agg_key, {})\n            if agg:\n                row = {\n                    \"dimension\": \"pool_size_controlled\",\n                    \"stratum\": \"AGGREGATE\",\n                    \"strategy\": f\"WEIGHTED_DELTA({STRATEGY_LABELS[other]}-Random)\",\n                    \"R@1\": f\"{agg.get('R@1_weighted_delta', 0):+.4f}\",\n                    \"R@1_ci95\": \"\",\n                    \"R@5\": \"\",\n                    \"MRR\": \"\",\n                    \"count\": agg.get(\"total_n\", 0),\n                }\n                rows.append(row)\n\n    # Cross-analysis rows\n    if cross_analysis:\n        for df_bin in DATAFLOW_BINS:\n            for pool_bin in POOL_SIZE_BINS:\n                cell_key = f\"{df_bin}::{pool_bin}\"\n                if cell_key not in cross_analysis:\n                    continue\n                for strategy in STRATEGIES:\n                    m = cross_analysis[cell_key].get(strategy, {})\n                    ci_r1 = m.get(\"R@1_ci\", [0, 0])\n                    up_flag = \" *underpowered*\" if m.get(\"underpowered\", False) else \"\"\n                    row = {\n                        \"dimension\": \"dataflow_x_pool_size\",\n                        \"stratum\": cell_key,\n                        \"strategy\": strategy + up_flag,\n                        \"R@1\": f\"{m.get('R@1', 0):.4f}\",\n                        \"R@1_ci95\": f\"[{ci_r1[0]:.4f}, {ci_r1[1]:.4f}]\",\n                        \"R@5\": \"\",\n                        \"MRR\": \"\",\n                        \"count\": m.get(\"count\", 0),\n                    }\n                    rows.append(row)\n\n'''\n\ncontent = content.replace(\n    '    fieldnames = [\"dimension\", \"stratum\", \"strategy\", \"R@1\", \"R@1_ci95\", \"R@5\", \"MRR\", \"count\"]',\n    NEW_CSV_ROWS + '    fieldnames = [\"dimension\", \"stratum\", \"strategy\", \"R@1\", \"R@1_ci95\", \"R@5\", \"MRR\", \"count\"]'\n)\n\n# ═══════════════════════════════════════════════════════════════════\n# 7. In main(): add new analysis calls after neg_diff_analysis\n# ═══════════════════════════════════════════════════════════════════\ncontent = content.replace(\n    '''    neg_diff_analysis = run_stratified_analysis(\n        all_results, \"neg_difficulty_bin\", NEG_DIFFICULTY_QUARTILE_LABELS, args.n_bootstrap\n    )\n\n    # Save JSON''',\n    '''    neg_diff_analysis = run_stratified_analysis(\n        all_results, \"neg_difficulty_bin\", NEG_DIFFICULTY_QUARTILE_LABELS, args.n_bootstrap\n    )\n\n    # Pool-size controlled analysis (disentangles pool_size confound)\n    print(\"Running pool-size controlled analysis...\", flush=True)\n    pool_controlled_analysis = run_pool_size_controlled_analysis(all_results, args.n_bootstrap)\n\n    # Dataflow x pool_size cross-analysis\n    cross_analysis = {}\n    if dataflow_edges is not None:\n        print(\"Running dataflow x pool_size cross-analysis...\", flush=True)\n        cross_analysis = run_dataflow_pool_cross_analysis(all_results, args.n_bootstrap)\n\n    # Save JSON'''\n)\n\n# ═══════════════════════════════════════════════════════════════════\n# 8. Add new results to full_results dict\n# ═══════════════════════════════════════════════════════════════════\ncontent = content.replace(\n    '''        \"by_neg_difficulty\": neg_diff_analysis,\n    }''',\n    '''        \"by_neg_difficulty\": neg_diff_analysis,\n        \"by_pool_size_controlled\": pool_controlled_analysis,\n        \"by_dataflow_x_pool_size\": cross_analysis,\n    }'''\n)\n\n# ═══════════════════════════════════════════════════════════════════\n# 9. Update write_summary_csv call in main()\n# ═══════════════════════════════════════════════════════════════════\ncontent = content.replace(\n    '    write_summary_csv(repo_analysis, pool_analysis, sim_analysis, csv_path, dataflow_analysis, neg_diff_analysis)',\n    '    write_summary_csv(repo_analysis, pool_analysis, sim_analysis, csv_path, dataflow_analysis, neg_diff_analysis, pool_controlled_analysis, cross_analysis)'\n)\n\n# ═══════════════════════════════════════════════════════════════════\n# 10. Update make_plots call in main()\n# ═══════════════════════════════════════════════════════════════════\ncontent = content.replace(\n    '        make_plots(repo_analysis, pool_analysis, sim_analysis, args.output_dir, dataflow_analysis, neg_diff_analysis)',\n    '        make_plots(repo_analysis, pool_analysis, sim_analysis, args.output_dir, dataflow_analysis, neg_diff_analysis, pool_controlled_analysis, cross_analysis)'\n)\n\n# ═══════════════════════════════════════════════════════════════════\n# 11. Update docstring\n# ═══════════════════════════════════════════════════════════════════\ncontent = content.replace(\n    '''\"\"\"Stratified analysis of embedding vs random negative strategies by data strata.\n\nAnalyses M2 per-instance predictions across:\n  - Repo size (instance count per repo from M1)\n  - Candidate pool size (neg_candidates per query)\n  - Query-positive similarity (cosine sim from model, or text overlap for dry-run)\n\nInputs:\n  - M2 per-instance predictions (from --predictions-dir or re-eval from checkpoints)\n  - M1 all.jsonl (repo metadata)\n  - Val JSONL files (query/candidate structure)\n\nOutputs:\n  - stratified_results.json: full per-stratum metrics with bootstrap CI\n  - stratified_summary.csv: compact table\n  - stratified_plots.pdf: grouped bar charts, heatmaps, delta trends\n\"\"\"''',\n    '''\"\"\"Stratified analysis of M2 negative-sampling strategies by data strata.\n\nAnalyses M2 per-instance predictions across 5+2 dimensions:\n  - Repo size (instance count per repo from M1)\n  - Candidate pool size (neg_candidates per query)\n  - Query-positive similarity (cosine sim from model, or text overlap for dry-run)\n  - Dataflow availability (edge count from dataflow_graph.json)\n  - Negative difficulty (pos-neg margin quartiles)\n  - [NEW] Pool-size controlled comparison: within-bin delta to disentangle\n    the confound that rich-dataflow instances have larger candidate pools\n  - [NEW] Dataflow x pool_size cross-tabulation with underpowered flagging\n\nInputs:\n  - M2 per-instance predictions (from --predictions-dir or re-eval from checkpoints)\n  - M1 all.jsonl (repo metadata)\n  - Val JSONL files (query/candidate structure)\n  - dataflow_graph.json (optional, for dataflow dimension and cross-analysis)\n\nOutputs:\n  - stratified_results.json: full per-stratum metrics with bootstrap CI\n  - stratified_summary.csv: compact table (incl. pool_size_controlled and cross sections)\n  - stratified_plots.pdf: grouped bar charts, heatmaps, delta trends,\n    pool-controlled comparison, dataflow x pool_size heatmaps\n\"\"\"'''\n)\n\n# ═══════════════════════════════════════════════════════════════════\n# 12. Add pool_size_controlled config entry\n# ═══════════════════════════════════════════════════════════════════\ncontent = content.replace(\n    '''            \"n_bootstrap\": args.n_bootstrap,\n            \"dry_run\": args.dry_run,''',\n    '''            \"n_bootstrap\": args.n_bootstrap,\n            \"dry_run\": args.dry_run,\n            \"pool_size_controlled\": True,\n            \"cross_analysis_min_cell_size\": 30,'''\n)\n\n# Write back\nwith open(SRC, 'w') as f:\n    f.write(content)\n\nprint(\"Patch applied successfully.\")\n\n# Verify line count\nwith open(SRC) as f:\n    lines = f.readlines()\nprint(f\"New line count: {len(lines)}\")\nPATCH_EOF\n",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "281adda7-32f4-4b4a-8902-691ccfafceb6",
  "isSidechain": false,
  "requestId": "req_011Cb37vUvSwnpexg6PQMams",
  "type": "assistant",
  "uuid": "f7327b45-325a-421c-aec2-4f9451a5f20d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "bda3dfbf-4b90-494d-b674-2597173fd381",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WvLh3zKJAwiWQAPQCHQkC9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6448,
      "cache_read_input_tokens": 64039,
      "output_tokens": 7189,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6448,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 7189,
          "cache_read_input_tokens": 64039,
          "cache_creation_input_tokens": 6448,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6448
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

_source line 81 · 2026-05-14T20:51:02.701Z_

<details><summary>↩ Tool result · `toolu_011NdciqaqsKnWtEiuCSPKtY`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f7327b45-325a-421c-aec2-4f9451a5f20d",
  "isSidechain": false,
  "promptId": "22ffd1fb-240e-481f-9bcc-b3f6a42d6805",
  "type": "user",
  "uuid": "704ab353-1105-4bbb-9d0b-0814b842550d",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.44}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"
    }
  },
  "sourceToolAssistantUUID": "f7327b45-325a-421c-aec2-4f9451a5f20d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "bda3dfbf-4b90-494d-b674-2597173fd381",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 82 · 2026-05-14T20:51:07.718Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_01YaauBaUWumSWCtfFRAAYDf`</summary>

```json
{
  "server": "bjb1-42106",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python3 /tmp/patch_stratified.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "704ab353-1105-4bbb-9d0b-0814b842550d",
  "isSidechain": false,
  "requestId": "req_011Cb3838mwJ1fZWKMTdkP8X",
  "type": "assistant",
  "uuid": "db4f23e8-4993-47ec-a20a-ae24a0d61cc9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "bda3dfbf-4b90-494d-b674-2597173fd381",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013WEsmUV54iig3Jk8PCe62g",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7262,
      "cache_read_input_tokens": 70487,
      "output_tokens": 135,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7262,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 135,
          "cache_read_input_tokens": 70487,
          "cache_creation_input_tokens": 7262,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7262
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

_source line 83_

```json
{
  "type": "last-prompt",
  "leafUuid": "db4f23e8-4993-47ec-a20a-ae24a0d61cc9",
  "sessionId": "bda3dfbf-4b90-494d-b674-2597173fd381"
}
```

---

### Runtime record

_source line 84_

```json
{
  "type": "ai-title",
  "aiTitle": "Add pool-size controlled stratified evaluation to analysis script",
  "sessionId": "bda3dfbf-4b90-494d-b674-2597173fd381"
}
```

---

### Tool result

_source line 85 · 2026-05-14T20:51:08.214Z_

<details><summary>↩ Tool result · `toolu_01YaauBaUWumSWCtfFRAAYDf`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"Patch applied successfully.\\nNew line count: 1254\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.49}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "db4f23e8-4993-47ec-a20a-ae24a0d61cc9",
  "isSidechain": false,
  "promptId": "22ffd1fb-240e-481f-9bcc-b3f6a42d6805",
  "type": "user",
  "uuid": "f4d838f5-fdbc-4dd9-a3ef-9e5e6f85be95",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"Patch applied successfully.\\\\nNew line count: 1254\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.49}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"Patch applied successfully.\\nNew line count: 1254\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.49}}"
    }
  },
  "sourceToolAssistantUUID": "db4f23e8-4993-47ec-a20a-ae24a0d61cc9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "bda3dfbf-4b90-494d-b674-2597173fd381",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 86 · 2026-05-14T20:51:11.168Z_

Patch applied (910 → 1254 lines). Let me verify the key changes.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f4d838f5-fdbc-4dd9-a3ef-9e5e6f85be95",
  "isSidechain": false,
  "requestId": "req_011Cb383YK3NZMNNyaSYakhC",
  "type": "assistant",
  "uuid": "23ac9ec6-7f26-4b85-acad-ff7bb8e732ed",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "bda3dfbf-4b90-494d-b674-2597173fd381",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SFQeKjTVHZdKCHASWjmJqJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 224,
      "cache_read_input_tokens": 77749,
      "output_tokens": 205,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 224,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 205,
          "cache_read_input_tokens": 77749,
          "cache_creation_input_tokens": 224,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 224
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

_source line 87 · 2026-05-14T20:51:12.709Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01YS3XkVvCps8BRTLQMMrNrF`</summary>

```json
{
  "server": "bjb1-42106",
  "command": "grep -n \"def run_pool_size_controlled\\|def run_dataflow_pool_cross\\|STRATEGY_SEED_OFFSET\\|pool_controlled_analysis\\|cross_analysis\\|by_pool_size_controlled\\|by_dataflow_x_pool_size\" /root/structfuse/evaluation/analyze_stratified.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "23ac9ec6-7f26-4b85-acad-ff7bb8e732ed",
  "isSidechain": false,
  "requestId": "req_011Cb383YK3NZMNNyaSYakhC",
  "type": "assistant",
  "uuid": "c9346da4-4ff1-43e3-855a-1d74cc593056",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "bda3dfbf-4b90-494d-b674-2597173fd381",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SFQeKjTVHZdKCHASWjmJqJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 224,
      "cache_read_input_tokens": 77749,
      "output_tokens": 205,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 224,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 205,
          "cache_read_input_tokens": 77749,
          "cache_creation_input_tokens": 224,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 224
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

_source line 88 · 2026-05-14T20:51:12.717Z_

<details><summary>↩ Tool result · `toolu_01YS3XkVvCps8BRTLQMMrNrF`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c9346da4-4ff1-43e3-855a-1d74cc593056",
  "isSidechain": false,
  "promptId": "22ffd1fb-240e-481f-9bcc-b3f6a42d6805",
  "type": "user",
  "uuid": "b2f62374-004b-4f3c-a349-31ab24792bfb",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\\\", \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "c9346da4-4ff1-43e3-855a-1d74cc593056",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "bda3dfbf-4b90-494d-b674-2597173fd381",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 89 · 2026-05-14T20:51:15.923Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01HvhGbZ3zw1J345hVxCVqEc`</summary>

```json
{
  "server": "bjb1-42106",
  "command": "grep -n \"def run_pool_size_controlled\\|def run_dataflow_pool_cross\\|STRATEGY_SEED_OFFSET\\|by_pool_size_controlled\\|by_dataflow_x_pool_size\" /root/structfuse/evaluation/analyze_stratified.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b2f62374-004b-4f3c-a349-31ab24792bfb",
  "isSidechain": false,
  "requestId": "req_011Cb383sbeopM8oUZSmXzpv",
  "type": "assistant",
  "uuid": "6402478e-116c-4d2d-96d3-0bac7c786355",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "bda3dfbf-4b90-494d-b674-2597173fd381",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TggbNBD69Nu48ETbattmZT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 298,
      "cache_read_input_tokens": 77973,
      "output_tokens": 172,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 298,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 172,
          "cache_read_input_tokens": 77973,
          "cache_creation_input_tokens": 298,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 298
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

_source line 90 · 2026-05-14T20:51:15.932Z_

<details><summary>↩ Tool result · `toolu_01HvhGbZ3zw1J345hVxCVqEc`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6402478e-116c-4d2d-96d3-0bac7c786355",
  "isSidechain": false,
  "promptId": "22ffd1fb-240e-481f-9bcc-b3f6a42d6805",
  "type": "user",
  "uuid": "d757d972-4a72-4e6e-8edc-54fa90593502",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\\\", \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "6402478e-116c-4d2d-96d3-0bac7c786355",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "bda3dfbf-4b90-494d-b674-2597173fd381",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 91 · 2026-05-14T20:51:21.359Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01UvjQTKs6y3LTa8maqxdWVX`</summary>

```json
{
  "server": "bjb1-42106",
  "command": "grep -n \"STRATEGY_SEED_OFFSET\" /root/structfuse/evaluation/analyze_stratified.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d757d972-4a72-4e6e-8edc-54fa90593502",
  "isSidechain": false,
  "requestId": "req_011Cb3847R71zC82c4Pz5h1Q",
  "type": "assistant",
  "uuid": "f30777c3-7c5c-4a91-9a74-4eac8149dbfe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "bda3dfbf-4b90-494d-b674-2597173fd381",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T1k3HDorAwbthosYjDG97T",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 265,
      "cache_read_input_tokens": 78271,
      "output_tokens": 584,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 265,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 584,
          "cache_read_input_tokens": 78271,
          "cache_creation_input_tokens": 265,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 265
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

_source line 92 · 2026-05-14T20:51:21.719Z_

<details><summary>↩ Tool result · `toolu_01UvjQTKs6y3LTa8maqxdWVX`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"278:    STRATEGY_SEED_OFFSET = {\\\"random\\\": 0, \\\"embedding_distance\\\": 1, \\\"dataflow_aware\\\": 2, \\\"bm25\\\": 3}\\n279:    rng = np.random.RandomState(seed + STRATEGY_SEED_OFFSET.get(strategy, hash(strategy) % 10000) * 10000)\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f30777c3-7c5c-4a91-9a74-4eac8149dbfe",
  "isSidechain": false,
  "promptId": "22ffd1fb-240e-481f-9bcc-b3f6a42d6805",
  "type": "user",
  "uuid": "792141ef-ffed-41ea-8e8e-8b8daa8a0173",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"278:    STRATEGY_SEED_OFFSET = {\\\\\\\"random\\\\\\\": 0, \\\\\\\"embedding_distance\\\\\\\": 1, \\\\\\\"dataflow_aware\\\\\\\": 2, \\\\\\\"bm25\\\\\\\": 3}\\\\n279:    rng = np.random.RandomState(seed + STRATEGY_SEED_OFFSET.get(strategy, hash(strategy) % 10000) * 10000)\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.35}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"278:    STRATEGY_SEED_OFFSET = {\\\"random\\\": 0, \\\"embedding_distance\\\": 1, \\\"dataflow_aware\\\": 2, \\\"bm25\\\": 3}\\n279:    rng = np.random.RandomState(seed + STRATEGY_SEED_OFFSET.get(strategy, hash(strategy) % 10000) * 10000)\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"
    }
  },
  "sourceToolAssistantUUID": "f30777c3-7c5c-4a91-9a74-4eac8149dbfe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "bda3dfbf-4b90-494d-b674-2597173fd381",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 93 · 2026-05-14T20:51:22.299Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_016mBwPAYDwHfTZbP6tCiRKz`</summary>

```json
{
  "server": "bjb1-42106",
  "command": "grep -n \"def run_pool_size_controlled\" /root/structfuse/evaluation/analyze_stratified.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "792141ef-ffed-41ea-8e8e-8b8daa8a0173",
  "isSidechain": false,
  "requestId": "req_011Cb3847R71zC82c4Pz5h1Q",
  "type": "assistant",
  "uuid": "473c8cf9-83fc-4f1f-a0ad-b53169e78a0f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "bda3dfbf-4b90-494d-b674-2597173fd381",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T1k3HDorAwbthosYjDG97T",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 265,
      "cache_read_input_tokens": 78271,
      "output_tokens": 584,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 265,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 584,
          "cache_read_input_tokens": 78271,
          "cache_creation_input_tokens": 265,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 265
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

_source line 94 · 2026-05-14T20:51:22.665Z_

<details><summary>↩ Tool result · `toolu_016mBwPAYDwHfTZbP6tCiRKz`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"484:def run_pool_size_controlled_analysis(\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "473c8cf9-83fc-4f1f-a0ad-b53169e78a0f",
  "isSidechain": false,
  "promptId": "22ffd1fb-240e-481f-9bcc-b3f6a42d6805",
  "type": "user",
  "uuid": "3f974d2e-0339-4dda-9541-ea2b101ae418",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"484:def run_pool_size_controlled_analysis(\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.35}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"484:def run_pool_size_controlled_analysis(\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"
    }
  },
  "sourceToolAssistantUUID": "473c8cf9-83fc-4f1f-a0ad-b53169e78a0f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "bda3dfbf-4b90-494d-b674-2597173fd381",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 95 · 2026-05-14T20:51:22.886Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01D2bmcnCYJ4xVnnPRysfdvJ`</summary>

```json
{
  "server": "bjb1-42106",
  "command": "grep -n \"def run_dataflow_pool_cross\" /root/structfuse/evaluation/analyze_stratified.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3f974d2e-0339-4dda-9541-ea2b101ae418",
  "isSidechain": false,
  "requestId": "req_011Cb3847R71zC82c4Pz5h1Q",
  "type": "assistant",
  "uuid": "1f184731-e4c5-483c-905e-d4c77c6d1a39",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "bda3dfbf-4b90-494d-b674-2597173fd381",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T1k3HDorAwbthosYjDG97T",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 265,
      "cache_read_input_tokens": 78271,
      "output_tokens": 584,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 265,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 584,
          "cache_read_input_tokens": 78271,
          "cache_creation_input_tokens": 265,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 265
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

_source line 96 · 2026-05-14T20:51:23.252Z_

<details><summary>↩ Tool result · `toolu_01D2bmcnCYJ4xVnnPRysfdvJ`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"558:def run_dataflow_pool_cross_analysis(\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1f184731-e4c5-483c-905e-d4c77c6d1a39",
  "isSidechain": false,
  "promptId": "22ffd1fb-240e-481f-9bcc-b3f6a42d6805",
  "type": "user",
  "uuid": "0e078814-37f5-485d-add9-0db1c80e6023",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"558:def run_dataflow_pool_cross_analysis(\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.35}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"558:def run_dataflow_pool_cross_analysis(\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"
    }
  },
  "sourceToolAssistantUUID": "1f184731-e4c5-483c-905e-d4c77c6d1a39",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "bda3dfbf-4b90-494d-b674-2597173fd381",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 97 · 2026-05-14T20:51:23.848Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01VaiH81zhK5P6QV8SRyvQsb`</summary>

```json
{
  "server": "bjb1-42106",
  "command": "grep -n \"by_pool_size_controlled\" /root/structfuse/evaluation/analyze_stratified.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0e078814-37f5-485d-add9-0db1c80e6023",
  "isSidechain": false,
  "requestId": "req_011Cb3847R71zC82c4Pz5h1Q",
  "type": "assistant",
  "uuid": "b60240b2-9ece-41ce-ab1d-d8f2acf74831",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "bda3dfbf-4b90-494d-b674-2597173fd381",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T1k3HDorAwbthosYjDG97T",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 265,
      "cache_read_input_tokens": 78271,
      "output_tokens": 584,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 265,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 584,
          "cache_read_input_tokens": 78271,
          "cache_creation_input_tokens": 265,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 265
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

_source line 98 · 2026-05-14T20:51:24.203Z_

<details><summary>↩ Tool result · `toolu_01VaiH81zhK5P6QV8SRyvQsb`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"1231:        \\\"by_pool_size_controlled\\\": pool_controlled_analysis,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b60240b2-9ece-41ce-ab1d-d8f2acf74831",
  "isSidechain": false,
  "promptId": "22ffd1fb-240e-481f-9bcc-b3f6a42d6805",
  "type": "user",
  "uuid": "c352713e-bff1-4cea-8d61-2cbbf781d70e",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"1231:        \\\\\\\"by_pool_size_controlled\\\\\\\": pool_controlled_analysis,\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.35}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"1231:        \\\"by_pool_size_controlled\\\": pool_controlled_analysis,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"
    }
  },
  "sourceToolAssistantUUID": "b60240b2-9ece-41ce-ab1d-d8f2acf74831",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "bda3dfbf-4b90-494d-b674-2597173fd381",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 99 · 2026-05-14T20:51:24.478Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_013CYv3Ca1bzXo6YybSq2r4i`</summary>

```json
{
  "server": "bjb1-42106",
  "command": "grep -n \"by_dataflow_x_pool_size\" /root/structfuse/evaluation/analyze_stratified.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c352713e-bff1-4cea-8d61-2cbbf781d70e",
  "isSidechain": false,
  "requestId": "req_011Cb3847R71zC82c4Pz5h1Q",
  "type": "assistant",
  "uuid": "6fdacefd-9baf-4259-97d3-9b93741da52d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "bda3dfbf-4b90-494d-b674-2597173fd381",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T1k3HDorAwbthosYjDG97T",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 265,
      "cache_read_input_tokens": 78271,
      "output_tokens": 584,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 265,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 584,
          "cache_read_input_tokens": 78271,
          "cache_creation_input_tokens": 265,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 265
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

_source line 100 · 2026-05-14T20:51:24.845Z_

<details><summary>↩ Tool result · `toolu_013CYv3Ca1bzXo6YybSq2r4i`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"1232:        \\\"by_dataflow_x_pool_size\\\": cross_analysis,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6fdacefd-9baf-4259-97d3-9b93741da52d",
  "isSidechain": false,
  "promptId": "22ffd1fb-240e-481f-9bcc-b3f6a42d6805",
  "type": "user",
  "uuid": "6db18251-ddec-474d-969f-00685c9ff5ba",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"1232:        \\\\\\\"by_dataflow_x_pool_size\\\\\\\": cross_analysis,\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.36}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"1232:        \\\"by_dataflow_x_pool_size\\\": cross_analysis,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"
    }
  },
  "sourceToolAssistantUUID": "6fdacefd-9baf-4259-97d3-9b93741da52d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "bda3dfbf-4b90-494d-b674-2597173fd381",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 101 · 2026-05-14T20:51:24.849Z_

```json
{
  "parentUuid": "6db18251-ddec-474d-969f-00685c9ff5ba",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "daa35cda-95bb-42e4-975b-f52e9f8ee0f6",
  "timestamp": "2026-05-14T20:51:24.849Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "bda3dfbf-4b90-494d-b674-2597173fd381",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 102 · 2026-05-14T20:51:27.261Z_

All changes are in place. Let me verify syntax and run the dry-run.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "daa35cda-95bb-42e4-975b-f52e9f8ee0f6",
  "isSidechain": false,
  "requestId": "req_011Cb384mT68TkpDkRm2J2dj",
  "type": "assistant",
  "uuid": "d5885cf7-8052-48b7-b4bb-bafed00b976f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "bda3dfbf-4b90-494d-b674-2597173fd381",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LnNCXqBj4YySwnp3JjzKNy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1372,
      "cache_read_input_tokens": 78536,
      "output_tokens": 172,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1372,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 172,
          "cache_read_input_tokens": 78536,
          "cache_creation_input_tokens": 1372,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1372
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

_source line 103 · 2026-05-14T20:51:28.399Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_01FdWrD7VFZFAkyC4tr3E5QP`</summary>

```json
{
  "server": "bjb1-42106",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python3 -m py_compile /root/structfuse/evaluation/analyze_stratified.py && echo \"SYNTAX_OK\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d5885cf7-8052-48b7-b4bb-bafed00b976f",
  "isSidechain": false,
  "requestId": "req_011Cb384mT68TkpDkRm2J2dj",
  "type": "assistant",
  "uuid": "bcf38fa4-2bd7-45c4-b264-bcc82314ae7d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "bda3dfbf-4b90-494d-b674-2597173fd381",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LnNCXqBj4YySwnp3JjzKNy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1372,
      "cache_read_input_tokens": 78536,
      "output_tokens": 172,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1372,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 172,
          "cache_read_input_tokens": 78536,
          "cache_creation_input_tokens": 1372,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1372
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

_source line 104 · 2026-05-14T20:51:28.872Z_

<details><summary>↩ Tool result · `toolu_01FdWrD7VFZFAkyC4tr3E5QP`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"SYNTAX_OK\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.46}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bcf38fa4-2bd7-45c4-b264-bcc82314ae7d",
  "isSidechain": false,
  "promptId": "22ffd1fb-240e-481f-9bcc-b3f6a42d6805",
  "type": "user",
  "uuid": "4fb1acc3-0b17-4612-a9fc-2fdc06c6e0d7",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"SYNTAX_OK\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.46}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"SYNTAX_OK\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.46}}"
    }
  },
  "sourceToolAssistantUUID": "bcf38fa4-2bd7-45c4-b264-bcc82314ae7d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "bda3dfbf-4b90-494d-b674-2597173fd381",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 105 · 2026-05-14T20:51:31.300Z_

Syntax OK. Now run the dry-run validation.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4fb1acc3-0b17-4612-a9fc-2fdc06c6e0d7",
  "isSidechain": false,
  "requestId": "req_011Cb3854dTL7RpopTiXkgKG",
  "type": "assistant",
  "uuid": "d302d55f-6d36-4fb9-8bec-1d19b6d68a62",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "bda3dfbf-4b90-494d-b674-2597173fd381",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0166suXHbtuvG1Y6cMgZWwEZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 251,
      "cache_read_input_tokens": 79908,
      "output_tokens": 301,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 251,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 301,
          "cache_read_input_tokens": 79908,
          "cache_creation_input_tokens": 251,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 251
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

_source line 106 · 2026-05-14T20:51:34.303Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_01HbCUTmV6sEqLNGJJJ7b9VM`</summary>

```json
{
  "server": "bjb1-42106",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/structfuse && python3 evaluation/analyze_stratified.py --m1-data /root/autodl-tmp/structfuse/full_m1_data/all.jsonl --val-data-dir /root/autodl-tmp/structfuse/full_m2_training_data --dataflow-graph /root/autodl-tmp/structfuse/full_m2_training_data/dataflow_graph.json --output-dir /root/autodl-tmp/structfuse/artifacts/stratified_dryrun_v3 --dry-run --seeds 42 --n-bootstrap 200",
  "account": "root",
  "warn": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d302d55f-6d36-4fb9-8bec-1d19b6d68a62",
  "isSidechain": false,
  "requestId": "req_011Cb3854dTL7RpopTiXkgKG",
  "type": "assistant",
  "uuid": "ce8f1aaf-fcc5-4568-ba5d-e8e2e517ed79",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "bda3dfbf-4b90-494d-b674-2597173fd381",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0166suXHbtuvG1Y6cMgZWwEZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 251,
      "cache_read_input_tokens": 79908,
      "output_tokens": 301,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 251,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 301,
          "cache_read_input_tokens": 79908,
          "cache_creation_input_tokens": 251,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 251
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

_source line 107 · 2026-05-14T20:51:54.347Z_

<details><summary>↩ Tool result · `toolu_01HbCUTmV6sEqLNGJJJ7b9VM`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"Loading M1 metadata from /root/autodl-tmp/structfuse/full_m1_data/all.jsonl...\\n  44173 instances, 123 repos\\nLoading dataflow graph from /root/autodl-tmp/structfuse/full_m2_training_data/dataflow_graph.json...\\n  376069 file entries\\nLoading val data: random seed=42...\\n  Generating mock predictions: random seed=42\\n  -> 2980 instances\\nLoading val data: embedding_distance seed=42...\\n  Generating mock predictions: embedding_distance seed=42\\n  -> 2980 instances\\nLoading val data: dataflow_aware seed=42...\\n  Generating mock predictions: dataflow_aware seed=42\\n  -> 2980 instances\\nComputing neg difficulty quartiles...\\n\\nRunning stratified analysis...\\nRunning pool-size controlled analysis...\\nRunning dataflow x pool_size cross-analysis...\\n  Results JSON saved to /root/autodl-tmp/structfuse/artifacts/stratified_dryrun_v3/stratified_results.json\\n  Summary CSV saved to /root/autodl-tmp/structfuse/artifacts/stratified_dryrun_v3/stratified_summary.csv\\n  Plots saved to /root/autodl-tmp/structfuse/artifacts/stratified_dryrun_v3/stratified_plots.pdf\\n\\nDone.\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 20.03}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ce8f1aaf-fcc5-4568-ba5d-e8e2e517ed79",
  "isSidechain": false,
  "promptId": "22ffd1fb-240e-481f-9bcc-b3f6a42d6805",
  "type": "user",
  "uuid": "635b3af1-f425-43fd-af10-47efd34002df",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"Loading M1 metadata from /root/autodl-tmp/structfuse/full_m1_data/all.jsonl...\\\\n  44173 instances, 123 repos\\\\nLoading dataflow graph from /root/autodl-tmp/structfuse/full_m2_training_data/dataflow_graph.json...\\\\n  376069 file entries\\\\nLoading val data: random seed=42...\\\\n  Generating mock predictions: random seed=42\\\\n  -> 2980 instances\\\\nLoading val data: embedding_distance seed=42...\\\\n  Generating mock predictions: embedding_distance seed=42\\\\n  -> 2980 instances\\\\nLoading val data: dataflow_aware seed=42...\\\\n  Generating mock predictions: dataflow_aware seed=42\\\\n  -> 2980 instances\\\\nComputing neg difficulty quartiles...\\\\n\\\\nRunning stratified analysis...\\\\nRunning pool-size controlled analysis...\\\\nRunning dataflow x pool_size cross-analysis...\\\\n  Results JSON saved to /root/autodl-tmp/structfuse/artifacts/stratified_dryrun_v3/stratified_results.json\\\\n  Summary CSV saved to /root/autodl-tmp/structfuse/artifacts/stratified_dryrun_v3/stratified_summary.csv\\\\n  Plots saved to /root/autodl-tmp/structfuse/artifacts/stratified_dryrun_v3/stratified_plots.pdf\\\\n\\\\nDone.\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 20.03}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"Loading M1 metadata from /root/autodl-tmp/structfuse/full_m1_data/all.jsonl...\\n  44173 instances, 123 repos\\nLoading dataflow graph from /root/autodl-tmp/structfuse/full_m2_training_data/dataflow_graph.json...\\n  376069 file entries\\nLoading val data: random seed=42...\\n  Generating mock predictions: random seed=42\\n  -> 2980 instances\\nLoading val data: embedding_distance seed=42...\\n  Generating mock predictions: embedding_distance seed=42\\n  -> 2980 instances\\nLoading val data: dataflow_aware seed=42...\\n  Generating mock predictions: dataflow_aware seed=42\\n  -> 2980 instances\\nComputing neg difficulty quartiles...\\n\\nRunning stratified analysis...\\nRunning pool-size controlled analysis...\\nRunning dataflow x pool_size cross-analysis...\\n  Results JSON saved to /root/autodl-tmp/structfuse/artifacts/stratified_dryrun_v3/stratified_results.json\\n  Summary CSV saved to /root/autodl-tmp/structfuse/artifacts/stratified_dryrun_v3/stratified_summary.csv\\n  Plots saved to /root/autodl-tmp/structfuse/artifacts/stratified_dryrun_v3/stratified_plots.pdf\\n\\nDone.\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 20.03}}"
    }
  },
  "sourceToolAssistantUUID": "ce8f1aaf-fcc5-4568-ba5d-e8e2e517ed79",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "bda3dfbf-4b90-494d-b674-2597173fd381",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 108_

```json
{
  "type": "last-prompt",
  "leafUuid": "635b3af1-f425-43fd-af10-47efd34002df",
  "sessionId": "bda3dfbf-4b90-494d-b674-2597173fd381"
}
```

---

### Runtime record

_source line 109_

```json
{
  "type": "ai-title",
  "aiTitle": "Add pool-size controlled stratified evaluation to analysis script",
  "sessionId": "bda3dfbf-4b90-494d-b674-2597173fd381"
}
```

---

### Assistant

_source line 110 · 2026-05-14T20:51:57.420Z_

Dry-run 成功。验证输出内容。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "635b3af1-f425-43fd-af10-47efd34002df",
  "isSidechain": false,
  "requestId": "req_011Cb386wYcsNhBnc1J6ML9k",
  "type": "assistant",
  "uuid": "0ab0c1fb-0b5b-42e2-815b-7b8736caad90",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "bda3dfbf-4b90-494d-b674-2597173fd381",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ag3SSqXcnkqZ1mXRGsregz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 732,
      "cache_read_input_tokens": 80159,
      "output_tokens": 145,
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
          "input_tokens": 1,
          "output_tokens": 145,
          "cache_read_input_tokens": 80159,
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

_source line 111 · 2026-05-14T20:51:57.788Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01TZjfMD9rS9YQfgUaCTn6At`</summary>

```json
{
  "server": "bjb1-42106",
  "command": "ls -la /root/autodl-tmp/structfuse/artifacts/stratified_dryrun_v3/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0ab0c1fb-0b5b-42e2-815b-7b8736caad90",
  "isSidechain": false,
  "requestId": "req_011Cb386wYcsNhBnc1J6ML9k",
  "type": "assistant",
  "uuid": "185b57b3-fd4c-45da-9e29-29b837dd3564",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "bda3dfbf-4b90-494d-b674-2597173fd381",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ag3SSqXcnkqZ1mXRGsregz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 732,
      "cache_read_input_tokens": 80159,
      "output_tokens": 145,
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
          "input_tokens": 1,
          "output_tokens": 145,
          "cache_read_input_tokens": 80159,
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

### Tool result

_source line 112 · 2026-05-14T20:51:58.153Z_

<details><summary>↩ Tool result · `toolu_01TZjfMD9rS9YQfgUaCTn6At`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 212\\ndrwxr-xr-x 2 root root    111 May 15 04:51 .\\ndrwxr-xr-x 8 root root   4096 May 15 04:51 ..\\n-rw-r--r-- 1 root root 147571 May 15 04:51 stratified_plots.pdf\\n-rw-r--r-- 1 root root  47729 May 15 04:51 stratified_results.json\\n-rw-r--r-- 1 root root  10259 May 15 04:51 stratified_summary.csv\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "185b57b3-fd4c-45da-9e29-29b837dd3564",
  "isSidechain": false,
  "promptId": "22ffd1fb-240e-481f-9bcc-b3f6a42d6805",
  "type": "user",
  "uuid": "ff52d57d-e831-4054-ba8d-1c1125adc482",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"total 212\\\\ndrwxr-xr-x 2 root root    111 May 15 04:51 .\\\\ndrwxr-xr-x 8 root root   4096 May 15 04:51 ..\\\\n-rw-r--r-- 1 root root 147571 May 15 04:51 stratified_plots.pdf\\\\n-rw-r--r-- 1 root root  47729 May 15 04:51 stratified_results.json\\\\n-rw-r--r-- 1 root root  10259 May 15 04:51 stratified_summary.csv\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.35}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"total 212\\ndrwxr-xr-x 2 root root    111 May 15 04:51 .\\ndrwxr-xr-x 8 root root   4096 May 15 04:51 ..\\n-rw-r--r-- 1 root root 147571 May 15 04:51 stratified_plots.pdf\\n-rw-r--r-- 1 root root  47729 May 15 04:51 stratified_results.json\\n-rw-r--r-- 1 root root  10259 May 15 04:51 stratified_summary.csv\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"
    }
  },
  "sourceToolAssistantUUID": "185b57b3-fd4c-45da-9e29-29b837dd3564",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "bda3dfbf-4b90-494d-b674-2597173fd381",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 113 · 2026-05-14T20:52:02.069Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01JG3erR4yVfjJWTGEs3ZYBz`</summary>

```json
{
  "server": "bjb1-42106",
  "command": "grep -c \"pool_size_controlled\\|dataflow_x_pool_size\\|by_pool_size_controlled\\|by_dataflow_x_pool_size\" /root/autodl-tmp/structfuse/artifacts/stratified_dryrun_v3/stratified_results.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ff52d57d-e831-4054-ba8d-1c1125adc482",
  "isSidechain": false,
  "requestId": "req_011Cb387DoAmzh5RV4fL1vm1",
  "type": "assistant",
  "uuid": "cf07556e-407a-42d1-857a-3e44fb0caf9a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "bda3dfbf-4b90-494d-b674-2597173fd381",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BMLNgyfVdedKTZRYHE8LC1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 379,
      "cache_read_input_tokens": 80891,
      "output_tokens": 308,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 379,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 308,
          "cache_read_input_tokens": 80891,
          "cache_creation_input_tokens": 379,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 379
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

_source line 114 · 2026-05-14T20:52:02.081Z_

<details><summary>↩ Tool result · `toolu_01JG3erR4yVfjJWTGEs3ZYBz`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cf07556e-407a-42d1-857a-3e44fb0caf9a",
  "isSidechain": false,
  "promptId": "22ffd1fb-240e-481f-9bcc-b3f6a42d6805",
  "type": "user",
  "uuid": "49bebf71-a619-4c40-800b-77de9aef5117",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\\\", \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "cf07556e-407a-42d1-857a-3e44fb0caf9a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "bda3dfbf-4b90-494d-b674-2597173fd381",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 115 · 2026-05-14T20:52:02.967Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01KajBuc1TV7uUjuXi183P5C`</summary>

```json
{
  "server": "bjb1-42106",
  "command": "grep -c \"pool_size_controlled\\|dataflow_x_pool_size\" /root/autodl-tmp/structfuse/artifacts/stratified_dryrun_v3/stratified_summary.csv",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "49bebf71-a619-4c40-800b-77de9aef5117",
  "isSidechain": false,
  "requestId": "req_011Cb387DoAmzh5RV4fL1vm1",
  "type": "assistant",
  "uuid": "bb03115f-d82a-42a9-8304-74d9c081de64",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "bda3dfbf-4b90-494d-b674-2597173fd381",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BMLNgyfVdedKTZRYHE8LC1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 379,
      "cache_read_input_tokens": 80891,
      "output_tokens": 308,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 379,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 308,
          "cache_read_input_tokens": 80891,
          "cache_creation_input_tokens": 379,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 379
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

_source line 116 · 2026-05-14T20:52:02.994Z_

<details><summary>↩ Tool result · `toolu_01KajBuc1TV7uUjuXi183P5C`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bb03115f-d82a-42a9-8304-74d9c081de64",
  "isSidechain": false,
  "promptId": "22ffd1fb-240e-481f-9bcc-b3f6a42d6805",
  "type": "user",
  "uuid": "4e121891-bcd4-4622-9a69-3c1474d80c0d",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\\\", \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "bb03115f-d82a-42a9-8304-74d9c081de64",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "bda3dfbf-4b90-494d-b674-2597173fd381",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 117 · 2026-05-14T20:52:06.825Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01LSabazV32tcZq42MHXvJS7`</summary>

```json
{
  "server": "bjb1-42106",
  "command": "grep -c \"by_pool_size_controlled\" /root/autodl-tmp/structfuse/artifacts/stratified_dryrun_v3/stratified_results.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4e121891-bcd4-4622-9a69-3c1474d80c0d",
  "isSidechain": false,
  "requestId": "req_011Cb387ab56J9nuTJKZBBsn",
  "type": "assistant",
  "uuid": "030f54d0-b34a-4c1e-a087-1efdefe8ac01",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "bda3dfbf-4b90-494d-b674-2597173fd381",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J1ebzbXhoDNe7YGZhoBzjS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 555,
      "cache_read_input_tokens": 81270,
      "output_tokens": 527,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 555,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 527,
          "cache_read_input_tokens": 81270,
          "cache_creation_input_tokens": 555,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 555
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

_source line 118 · 2026-05-14T20:52:07.185Z_

<details><summary>↩ Tool result · `toolu_01LSabazV32tcZq42MHXvJS7`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"1\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "030f54d0-b34a-4c1e-a087-1efdefe8ac01",
  "isSidechain": false,
  "promptId": "22ffd1fb-240e-481f-9bcc-b3f6a42d6805",
  "type": "user",
  "uuid": "0e75f9ee-14a4-42ac-8eef-73f9bd0329d0",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"1\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.35}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"1\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"
    }
  },
  "sourceToolAssistantUUID": "030f54d0-b34a-4c1e-a087-1efdefe8ac01",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "bda3dfbf-4b90-494d-b674-2597173fd381",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 119 · 2026-05-14T20:52:07.823Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01A78hcNU48JhamrQ7dwsWHY`</summary>

```json
{
  "server": "bjb1-42106",
  "command": "grep -c \"by_dataflow_x_pool_size\" /root/autodl-tmp/structfuse/artifacts/stratified_dryrun_v3/stratified_results.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0e75f9ee-14a4-42ac-8eef-73f9bd0329d0",
  "isSidechain": false,
  "requestId": "req_011Cb387ab56J9nuTJKZBBsn",
  "type": "assistant",
  "uuid": "59c049c7-fbc4-4d51-8873-d5f4b17c0a77",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "bda3dfbf-4b90-494d-b674-2597173fd381",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J1ebzbXhoDNe7YGZhoBzjS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 555,
      "cache_read_input_tokens": 81270,
      "output_tokens": 527,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 555,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 527,
          "cache_read_input_tokens": 81270,
          "cache_creation_input_tokens": 555,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 555
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

_source line 120 · 2026-05-14T20:52:08.184Z_

<details><summary>↩ Tool result · `toolu_01A78hcNU48JhamrQ7dwsWHY`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"1\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "59c049c7-fbc4-4d51-8873-d5f4b17c0a77",
  "isSidechain": false,
  "promptId": "22ffd1fb-240e-481f-9bcc-b3f6a42d6805",
  "type": "user",
  "uuid": "45e2177f-f50f-4147-9d42-e4c6b4674d1e",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"1\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.35}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"1\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"
    }
  },
  "sourceToolAssistantUUID": "59c049c7-fbc4-4d51-8873-d5f4b17c0a77",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "bda3dfbf-4b90-494d-b674-2597173fd381",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 121 · 2026-05-14T20:52:08.939Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_013i3RHsLGGkycYkFGRuTUGK`</summary>

```json
{
  "server": "bjb1-42106",
  "command": "grep -c \"pool_size_controlled\" /root/autodl-tmp/structfuse/artifacts/stratified_dryrun_v3/stratified_summary.csv",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "45e2177f-f50f-4147-9d42-e4c6b4674d1e",
  "isSidechain": false,
  "requestId": "req_011Cb387ab56J9nuTJKZBBsn",
  "type": "assistant",
  "uuid": "0826b086-9038-4764-acff-60a503f91da6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "bda3dfbf-4b90-494d-b674-2597173fd381",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J1ebzbXhoDNe7YGZhoBzjS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 555,
      "cache_read_input_tokens": 81270,
      "output_tokens": 527,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 555,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 527,
          "cache_read_input_tokens": 81270,
          "cache_creation_input_tokens": 555,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 555
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

_source line 122 · 2026-05-14T20:52:09.300Z_

<details><summary>↩ Tool result · `toolu_013i3RHsLGGkycYkFGRuTUGK`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"17\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0826b086-9038-4764-acff-60a503f91da6",
  "isSidechain": false,
  "promptId": "22ffd1fb-240e-481f-9bcc-b3f6a42d6805",
  "type": "user",
  "uuid": "dc33d1f8-5752-4f23-aa59-4df5c879cce2",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"17\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.35}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"17\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"
    }
  },
  "sourceToolAssistantUUID": "0826b086-9038-4764-acff-60a503f91da6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "bda3dfbf-4b90-494d-b674-2597173fd381",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 123 · 2026-05-14T20:52:09.479Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_017uA36hko2Wfj3VNk5V9oMF`</summary>

```json
{
  "server": "bjb1-42106",
  "command": "grep -c \"dataflow_x_pool_size\" /root/autodl-tmp/structfuse/artifacts/stratified_dryrun_v3/stratified_summary.csv",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dc33d1f8-5752-4f23-aa59-4df5c879cce2",
  "isSidechain": false,
  "requestId": "req_011Cb387ab56J9nuTJKZBBsn",
  "type": "assistant",
  "uuid": "b286a12b-0eb5-4544-9f65-5069115cb5cc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "bda3dfbf-4b90-494d-b674-2597173fd381",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J1ebzbXhoDNe7YGZhoBzjS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 555,
      "cache_read_input_tokens": 81270,
      "output_tokens": 527,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 555,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 527,
          "cache_read_input_tokens": 81270,
          "cache_creation_input_tokens": 555,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 555
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

_source line 124 · 2026-05-14T20:52:09.840Z_

<details><summary>↩ Tool result · `toolu_017uA36hko2Wfj3VNk5V9oMF`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"27\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b286a12b-0eb5-4544-9f65-5069115cb5cc",
  "isSidechain": false,
  "promptId": "22ffd1fb-240e-481f-9bcc-b3f6a42d6805",
  "type": "user",
  "uuid": "2363d38d-cc52-4898-b31c-7cdb5d7788d9",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"27\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.35}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"27\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"
    }
  },
  "sourceToolAssistantUUID": "b286a12b-0eb5-4544-9f65-5069115cb5cc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "bda3dfbf-4b90-494d-b674-2597173fd381",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 125 · 2026-05-14T20:52:09.843Z_

```json
{
  "parentUuid": "2363d38d-cc52-4898-b31c-7cdb5d7788d9",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "2b2f5db1-7166-4aeb-b895-76147845b941",
  "timestamp": "2026-05-14T20:52:09.843Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "bda3dfbf-4b90-494d-b674-2597173fd381",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 126 · 2026-05-14T20:52:12.982Z_

Let me also verify the pool-controlled results content and check the aggregate weighted deltas.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2b2f5db1-7166-4aeb-b895-76147845b941",
  "isSidechain": false,
  "requestId": "req_011Cb3885jWwo6EghBwWKbFw",
  "type": "assistant",
  "uuid": "2e37b789-8ab5-401f-8a07-c832f8a8fd51",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "bda3dfbf-4b90-494d-b674-2597173fd381",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018kwspYmKeCJFiDuPcnEqKe",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1043,
      "cache_read_input_tokens": 81825,
      "output_tokens": 289,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1043,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 289,
          "cache_read_input_tokens": 81825,
          "cache_creation_input_tokens": 1043,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1043
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

_source line 127 · 2026-05-14T20:52:14.458Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01EmLYBxowofpQMZb52nCBNJ`</summary>

```json
{
  "server": "bjb1-42106",
  "command": "grep \"AGGREGATE\\|WEIGHTED_DELTA\\|underpowered\" /root/autodl-tmp/structfuse/artifacts/stratified_dryrun_v3/stratified_summary.csv",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2e37b789-8ab5-401f-8a07-c832f8a8fd51",
  "isSidechain": false,
  "requestId": "req_011Cb3885jWwo6EghBwWKbFw",
  "type": "assistant",
  "uuid": "5ca4f33c-6296-4d6c-b31b-a0f43bf458a2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "bda3dfbf-4b90-494d-b674-2597173fd381",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018kwspYmKeCJFiDuPcnEqKe",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1043,
      "cache_read_input_tokens": 81825,
      "output_tokens": 289,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1043,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 289,
          "cache_read_input_tokens": 81825,
          "cache_creation_input_tokens": 1043,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1043
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

_source line 128 · 2026-05-14T20:52:14.470Z_

<details><summary>↩ Tool result · `toolu_01EmLYBxowofpQMZb52nCBNJ`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5ca4f33c-6296-4d6c-b31b-a0f43bf458a2",
  "isSidechain": false,
  "promptId": "22ffd1fb-240e-481f-9bcc-b3f6a42d6805",
  "type": "user",
  "uuid": "1c5cfff1-0c77-48e3-8b81-5299f4399a3e",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\\\", \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "5ca4f33c-6296-4d6c-b31b-a0f43bf458a2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "bda3dfbf-4b90-494d-b674-2597173fd381",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 129 · 2026-05-14T20:52:15.082Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01HT4hK826Wr8syEmiR3j5VQ`</summary>

```json
{
  "server": "bjb1-42106",
  "command": "grep \"aggregate_\" /root/autodl-tmp/structfuse/artifacts/stratified_dryrun_v3/stratified_results.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1c5cfff1-0c77-48e3-8b81-5299f4399a3e",
  "isSidechain": false,
  "requestId": "req_011Cb3885jWwo6EghBwWKbFw",
  "type": "assistant",
  "uuid": "5cadbaca-1711-41c9-90a6-a90bc6ea5a28",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "bda3dfbf-4b90-494d-b674-2597173fd381",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018kwspYmKeCJFiDuPcnEqKe",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1043,
      "cache_read_input_tokens": 81825,
      "output_tokens": 289,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1043,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 289,
          "cache_read_input_tokens": 81825,
          "cache_creation_input_tokens": 1043,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1043
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

_source line 130 · 2026-05-14T20:52:15.464Z_

<details><summary>↩ Tool result · `toolu_01HT4hK826Wr8syEmiR3j5VQ`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"    \\\"aggregate_embedding_distance_vs_random\\\": {\\n    \\\"aggregate_dataflow_aware_vs_random\\\": {\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.37}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5cadbaca-1711-41c9-90a6-a90bc6ea5a28",
  "isSidechain": false,
  "promptId": "22ffd1fb-240e-481f-9bcc-b3f6a42d6805",
  "type": "user",
  "uuid": "1b7e9f26-d050-4f67-8f22-30f5ec5fef1e",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"    \\\\\\\"aggregate_embedding_distance_vs_random\\\\\\\": {\\\\n    \\\\\\\"aggregate_dataflow_aware_vs_random\\\\\\\": {\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.37}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"    \\\"aggregate_embedding_distance_vs_random\\\": {\\n    \\\"aggregate_dataflow_aware_vs_random\\\": {\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.37}}"
    }
  },
  "sourceToolAssistantUUID": "5cadbaca-1711-41c9-90a6-a90bc6ea5a28",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "bda3dfbf-4b90-494d-b674-2597173fd381",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 131 · 2026-05-14T20:52:19.839Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01XsCn6eYF4tzPYr2z53AwW4`</summary>

```json
{
  "server": "bjb1-42106",
  "command": "grep \"AGGREGATE\" /root/autodl-tmp/structfuse/artifacts/stratified_dryrun_v3/stratified_summary.csv",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1b7e9f26-d050-4f67-8f22-30f5ec5fef1e",
  "isSidechain": false,
  "requestId": "req_011Cb388Vqr6xu1Bzz4qyhJC",
  "type": "assistant",
  "uuid": "76646ec2-c301-400d-8cba-181bf74403b2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "bda3dfbf-4b90-494d-b674-2597173fd381",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014giAidFf94cE9xmBkyj6xs",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 555,
      "cache_read_input_tokens": 82868,
      "output_tokens": 259,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 555,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 259,
          "cache_read_input_tokens": 82868,
          "cache_creation_input_tokens": 555,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 555
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

_source line 132 · 2026-05-14T20:52:20.209Z_

<details><summary>↩ Tool result · `toolu_01XsCn6eYF4tzPYr2z53AwW4`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"pool_size_controlled,AGGREGATE,WEIGHTED_DELTA(Embedding-Random),+0.0473,,,,2980\\r\\npool_size_controlled,AGGREGATE,WEIGHTED_DELTA(Dataflow-Random),+0.0960,,,,2980\\r\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "76646ec2-c301-400d-8cba-181bf74403b2",
  "isSidechain": false,
  "promptId": "22ffd1fb-240e-481f-9bcc-b3f6a42d6805",
  "type": "user",
  "uuid": "dd895c70-c611-467a-b8ab-834089668aab",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"pool_size_controlled,AGGREGATE,WEIGHTED_DELTA(Embedding-Random),+0.0473,,,,2980\\\\r\\\\npool_size_controlled,AGGREGATE,WEIGHTED_DELTA(Dataflow-Random),+0.0960,,,,2980\\\\r\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.36}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"pool_size_controlled,AGGREGATE,WEIGHTED_DELTA(Embedding-Random),+0.0473,,,,2980\\r\\npool_size_controlled,AGGREGATE,WEIGHTED_DELTA(Dataflow-Random),+0.0960,,,,2980\\r\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"
    }
  },
  "sourceToolAssistantUUID": "76646ec2-c301-400d-8cba-181bf74403b2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "bda3dfbf-4b90-494d-b674-2597173fd381",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 133 · 2026-05-14T20:52:20.488Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01WZRg3cHarCLeLFfav7XnEQ`</summary>

```json
{
  "server": "bjb1-42106",
  "command": "grep \"underpowered\" /root/autodl-tmp/structfuse/artifacts/stratified_dryrun_v3/stratified_summary.csv",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dd895c70-c611-467a-b8ab-834089668aab",
  "isSidechain": false,
  "requestId": "req_011Cb388Vqr6xu1Bzz4qyhJC",
  "type": "assistant",
  "uuid": "068c7537-12e3-468c-a959-f7cd46ad72f2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "bda3dfbf-4b90-494d-b674-2597173fd381",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014giAidFf94cE9xmBkyj6xs",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 555,
      "cache_read_input_tokens": 82868,
      "output_tokens": 259,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 555,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 259,
          "cache_read_input_tokens": 82868,
          "cache_creation_input_tokens": 555,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 555
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

_source line 134_

```json
{
  "type": "last-prompt",
  "leafUuid": "068c7537-12e3-468c-a959-f7cd46ad72f2",
  "sessionId": "bda3dfbf-4b90-494d-b674-2597173fd381"
}
```

---

### Runtime record

_source line 135_

```json
{
  "type": "ai-title",
  "aiTitle": "Add pool-size controlled stratified evaluation to analysis script",
  "sessionId": "bda3dfbf-4b90-494d-b674-2597173fd381"
}
```

---

### Tool result

_source line 136 · 2026-05-14T20:52:20.853Z_

<details><summary>↩ Tool result · `toolu_01WZRg3cHarCLeLFfav7XnEQ`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"dataflow_x_pool_size,rich::small,random *underpowered*,0.0000,\\\"[0.0000, 0.0000]\\\",,,0\\r\\ndataflow_x_pool_size,rich::small,embedding_distance *underpowered*,0.0000,\\\"[0.0000, 0.0000]\\\",,,0\\r\\ndataflow_x_pool_size,rich::small,dataflow_aware *underpowered*,0.0000,\\\"[0.0000, 0.0000]\\\",,,0\\r\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "068c7537-12e3-468c-a959-f7cd46ad72f2",
  "isSidechain": false,
  "promptId": "22ffd1fb-240e-481f-9bcc-b3f6a42d6805",
  "type": "user",
  "uuid": "0010c612-21cf-4262-b2ec-dca71b02c176",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"dataflow_x_pool_size,rich::small,random *underpowered*,0.0000,\\\\\\\"[0.0000, 0.0000]\\\\\\\",,,0\\\\r\\\\ndataflow_x_pool_size,rich::small,embedding_distance *underpowered*,0.0000,\\\\\\\"[0.0000, 0.0000]\\\\\\\",,,0\\\\r\\\\ndataflow_x_pool_size,rich::small,dataflow_aware *underpowered*,0.0000,\\\\\\\"[0.0000, 0.0000]\\\\\\\",,,0\\\\r\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.35}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"dataflow_x_pool_size,rich::small,random *underpowered*,0.0000,\\\"[0.0000, 0.0000]\\\",,,0\\r\\ndataflow_x_pool_size,rich::small,embedding_distance *underpowered*,0.0000,\\\"[0.0000, 0.0000]\\\",,,0\\r\\ndataflow_x_pool_size,rich::small,dataflow_aware *underpowered*,0.0000,\\\"[0.0000, 0.0000]\\\",,,0\\r\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"
    }
  },
  "sourceToolAssistantUUID": "068c7537-12e3-468c-a959-f7cd46ad72f2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "bda3dfbf-4b90-494d-b674-2597173fd381",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 137 · 2026-05-14T20:52:23.676Z_

全部验证通过。让我验证 checkpoint 路径发现逻辑也正常。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0010c612-21cf-4262-b2ec-dca71b02c176",
  "isSidechain": false,
  "requestId": "req_011Cb388ttS3aoSzRLfSijY9",
  "type": "assistant",
  "uuid": "6e08c5d5-713f-4747-b8fe-e9cc6937748e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "bda3dfbf-4b90-494d-b674-2597173fd381",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Trbq1AESYRqK9or2nN8tss",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 682,
      "cache_read_input_tokens": 83423,
      "output_tokens": 158,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 682,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 158,
          "cache_read_input_tokens": 83423,
          "cache_creation_input_tokens": 682,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 682
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

_source line 138 · 2026-05-14T20:52:24.682Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01DSPfytpwDjJLhQXhrvvaR2`</summary>

```json
{
  "server": "bjb1-42106",
  "command": "grep -n \"best_by_recall_at_1\" /root/structfuse/evaluation/analyze_stratified.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6e08c5d5-713f-4747-b8fe-e9cc6937748e",
  "isSidechain": false,
  "requestId": "req_011Cb388ttS3aoSzRLfSijY9",
  "type": "assistant",
  "uuid": "2d4387a4-a7af-4f9a-8526-7ca0262a26ad",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "bda3dfbf-4b90-494d-b674-2597173fd381",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Trbq1AESYRqK9or2nN8tss",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 682,
      "cache_read_input_tokens": 83423,
      "output_tokens": 158,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 682,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 158,
          "cache_read_input_tokens": 83423,
          "cache_creation_input_tokens": 682,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 682
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

_source line 139 · 2026-05-14T20:52:25.040Z_

<details><summary>↩ Tool result · `toolu_01DSPfytpwDjJLhQXhrvvaR2`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"1143:                for subdir in [\\\"best\\\", \\\"best_by_recall_at_1\\\", \\\"best_by_val_loss\\\"]:\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2d4387a4-a7af-4f9a-8526-7ca0262a26ad",
  "isSidechain": false,
  "promptId": "22ffd1fb-240e-481f-9bcc-b3f6a42d6805",
  "type": "user",
  "uuid": "da533e3a-680f-4cb5-bb6c-3dbcb8370aab",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"1143:                for subdir in [\\\\\\\"best\\\\\\\", \\\\\\\"best_by_recall_at_1\\\\\\\", \\\\\\\"best_by_val_loss\\\\\\\"]:\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.35}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"1143:                for subdir in [\\\"best\\\", \\\"best_by_recall_at_1\\\", \\\"best_by_val_loss\\\"]:\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"
    }
  },
  "sourceToolAssistantUUID": "2d4387a4-a7af-4f9a-8526-7ca0262a26ad",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "bda3dfbf-4b90-494d-b674-2597173fd381",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 140 · 2026-05-14T20:52:36.580Z_

Checkpoint 发现逻辑已经存在（搜索 `best/`, `best_by_recall_at_1/`, `best_by_val_loss/` 子目录下的 `model.pt`），无需修改。

完成。修改总结：

1. **mock_predictions seed 修复** (line 278-279): `hash(strategy)` 替换为确定性 `STRATEGY_SEED_OFFSET` 字典
2. **`run_pool_size_controlled_analysis()`** (line 484): 在同一 pool_size bin 内比较策略 R@1，计算 within-bin delta 和 count-weighted aggregate delta，排除候选池大小 confound
3. **`run_dataflow_pool_cross_analysis()`** (line 558): (dataflow_bin × pool_size_bin) 交叉分析，n<30 标记 underpowered
4. **输出完整**:
   - JSON: 新增 `by_pool_size_controlled` 和 `by_dataflow_x_pool_size` 两节
   - CSV: 17 行 pool_size_controlled（含 AGGREGATE weighted delta）+ 27 行 cross-analysis（含 underpowered 标记）
   - PDF: 新增 pool-controlled 对比图 + dataflow×pool_size heatmap per strategy
5. **`--checkpoints-dir` 模式**: 已有 `best/`, `best_by_recall_at_1/`, `best_by_val_loss/` checkpoint 发现逻辑，无需改动

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "da533e3a-680f-4cb5-bb6c-3dbcb8370aab",
  "isSidechain": false,
  "requestId": "req_011Cb389Cnho2mXaN4zXB7WK",
  "type": "assistant",
  "uuid": "af37f8e8-75ce-4e91-a1b6-1edb9da3c149",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "bda3dfbf-4b90-494d-b674-2597173fd381",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X5rSKdZZdUqkJyCgm34xDG",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 276,
      "cache_read_input_tokens": 84105,
      "output_tokens": 417,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 276,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 417,
          "cache_read_input_tokens": 84105,
          "cache_creation_input_tokens": 276,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 276
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

_source line 141_

```json
{
  "type": "last-prompt",
  "leafUuid": "af37f8e8-75ce-4e91-a1b6-1edb9da3c149",
  "sessionId": "bda3dfbf-4b90-494d-b674-2597173fd381"
}
```

---

### Runtime record

_source line 142_

```json
{
  "type": "ai-title",
  "aiTitle": "Add pool-size controlled stratified evaluation to analysis script",
  "sessionId": "bda3dfbf-4b90-494d-b674-2597173fd381"
}
```

---
