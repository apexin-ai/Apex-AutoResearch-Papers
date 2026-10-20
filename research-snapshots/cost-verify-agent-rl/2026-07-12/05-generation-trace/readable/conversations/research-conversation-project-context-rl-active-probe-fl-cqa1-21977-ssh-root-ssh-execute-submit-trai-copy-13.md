# Research conversation: <project_context> # 项目: rl-active-probe-fl ## 运行环境 - 服务器名: cqa1-21977 - SSH 账户: root（调用 ssh_execute / submit_training_jo

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 30
- **Recorded user turns:** 1
- **Tool calls:** 6
- **Original source:** `logs/chats/exported-trajectories/account-2/2c8f695e-2726-4bc0-b978-178d488e8a4b.jsonl`
- **Structured JSON:** [`0dd8c7e24e98bba0402f.json`](../../sessions/0d/0dd8c7e24e98bba0402f.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-13T04:47:29.231Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-13T04:47:29.231Z",
  "sessionId": "2c8f695e-2726-4bc0-b978-178d488e8a4b",
  "content": "&lt;project_context>\n# 项目: rl-active-probe-fl\n\n## 运行环境\n- 服务器名: cqa1-21977\n- SSH 账户: root（调用 ssh_execute / submit_training_job 时传入 account=\"root\"）\n- SSH 连接命令: ssh connect.cqa1.seetacloud.com  # 必须用此命令，~/.ssh/config 自动应用密钥和跳板机，禁止用裸 IP\n- 项目代码根目录: /root/autodl-tmp/rl-active-probe-fl\n\n\n## 环境搭建\n连接服务器后先调 `detect_image` 检测是否为预置镜像。如果匹配，跳过基础环境搭建，只装项目特有依赖。已预装的包不要重复安装。\n\n## 输出风格\n回复简洁直接。只输出执行结果和必要信息，不要解释过程、不要客套、不要给未被要求的建议。\n&lt;/project_context>\n## 任务：编写 failure mode 描述性分析脚本\n\n写一个 `analyze_failure_modes.py`，v7 数据收集完成后可以直接跑。这是 P1 降级为描述性分析后的产物，用于论文的 failure mode characterization。\n\n### 背景\n- P1 (error type 统计检验) 已作废，降级为描述性分析\n- ETADN 的核心变量是 divergence position d = div_point / expert_length\n- 论文需要展示 failure mode 的分布特征，不再做 KW 检验\n\n### 先读取参考文件\n1. `/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl/src/build_dpo_pairs.py` — 了解 divergence point 计算逻辑和 JSONL 格式\n2. `/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl/artifacts/collect_trajectories_icl.py` — 了解 trajectory JSONL 输出格式\n3. `/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl/src/etadn_discount.py` — 了解 γ(d) 函数\n\n### 写入路径\n`/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl/src/analyze_failure_modes.py`\n\n### 功能要求\n\n**输入**：\n- `--failure_dir`: v7 trajectories 目录（含 train.jsonl 或多个 part JSONL）\n- `--expert_file`: alfworld_sft.json\n- `--output_dir`: 输出目录\n\n**分析内容**：\n\n1. **基本统计**\n   - 总 tasks、成功/失败数、成功率\n   - per-task-type 成功率 (6 种 ALFWorld task type: pick_and_place, clean, heat, cool, examine, pick_two)\n\n2. **Divergence 分析**（核心，论文需要）\n   - 计算每条失败轨迹的 divergence point（与 expert 首次不同 action 的位置）\n   - d = divergence_point / expert_length 的分布（mean, median, std, quartiles）\n   - d 值直方图数据（bins: 0-0.1, 0.1-0.2, ..., 0.9-1.0）\n   - per-task-type 的 d 分布\n   - early (d<0.33) / mid (0.33≤d<0.67) / late (d≥0.67) 三组的样本量\n\n3. **γ(d) 映射预览**\n   - 用 etadn_discount 的 γ(d) 函数，展示数据中 γ 值的分布\n   - γ_min=0.85, γ_max=0.97 下各样本的 γ 值\n\n4. **Expert/Failure 匹配统计**\n   - exact match rate（game_file 完全匹配）\n   - template match rate（同 task type）\n   - unmatched failures 数量\n\n5. **轨迹长度分析**\n   - 失败轨迹 vs expert 轨迹的长度分布\n   - correction span (expert_length - div_point) 分布\n\n**输出格式**：\n- `failure_mode_summary.json`: 所有统计数据的结构化 JSON\n- `failure_mode_report.md`: 论文可引用的 markdown 表格和描述\n- 打印 summary 到 stdout\n\n### Divergence point 计算逻辑\n参考 build_dpo_pairs.py 的实现。核心：\n1. 解析 failure trajectory 的 action 序列（从 conversation 中提取 assistant 消息）\n2. 解析 expert trajectory 的 action 序列\n3. 逐步比较，找到第一个 action 不同的位置 = divergence_point\n4. 如果所有 action 都相同但 failure 多了错误步骤，divergence_point = expert_length\n\n### 代码规范\n- 文件顶部写文件注释\n- 主要函数写 docstring\n- 使用 argparse CLI\n- 不依赖 vllm/torch（纯 CPU 分析脚本）\n\n### 验证\n写完后 `python -m py_compile src/analyze_failure_modes.py` 验证语法。\n\n### 完成标准\n1. 脚本语法正确\n2. 覆盖所有 5 类分析\n3. 输出 JSON + Markdown 两种格式\n4. 不依赖 GPU（纯 CPU）"
}
```

---

### Runtime record

_source line 2 · 2026-05-13T04:47:29.235Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-13T04:47:29.235Z",
  "sessionId": "2c8f695e-2726-4bc0-b978-178d488e8a4b"
}
```

---

## Round 1

28 recorded events

### User

_source line 3 · 2026-05-13T04:47:29.274Z_

&lt;project_context>
# 项目: rl-active-probe-fl

## 运行环境
- 服务器名: cqa1-21977
- SSH 账户: root（调用 ssh_execute / submit_training_job 时传入 account="root"）
- SSH 连接命令: ssh connect.cqa1.seetacloud.com  # 必须用此命令，~/.ssh/config 自动应用密钥和跳板机，禁止用裸 IP
- 项目代码根目录: /root/autodl-tmp/rl-active-probe-fl


## 环境搭建
连接服务器后先调 `detect_image` 检测是否为预置镜像。如果匹配，跳过基础环境搭建，只装项目特有依赖。已预装的包不要重复安装。

## 输出风格
回复简洁直接。只输出执行结果和必要信息，不要解释过程、不要客套、不要给未被要求的建议。
&lt;/project_context>
## 任务：编写 failure mode 描述性分析脚本

写一个 `analyze_failure_modes.py`，v7 数据收集完成后可以直接跑。这是 P1 降级为描述性分析后的产物，用于论文的 failure mode characterization。

### 背景
- P1 (error type 统计检验) 已作废，降级为描述性分析
- ETADN 的核心变量是 divergence position d = div_point / expert_length
- 论文需要展示 failure mode 的分布特征，不再做 KW 检验

### 先读取参考文件
1. `/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl/src/build_dpo_pairs.py` — 了解 divergence point 计算逻辑和 JSONL 格式
2. `/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl/artifacts/collect_trajectories_icl.py` — 了解 trajectory JSONL 输出格式
3. `/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl/src/etadn_discount.py` — 了解 γ(d) 函数

### 写入路径
`/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl/src/analyze_failure_modes.py`

### 功能要求

**输入**：
- `--failure_dir`: v7 trajectories 目录（含 train.jsonl 或多个 part JSONL）
- `--expert_file`: alfworld_sft.json
- `--output_dir`: 输出目录

**分析内容**：

1. **基本统计**
   - 总 tasks、成功/失败数、成功率
   - per-task-type 成功率 (6 种 ALFWorld task type: pick_and_place, clean, heat, cool, examine, pick_two)

2. **Divergence 分析**（核心，论文需要）
   - 计算每条失败轨迹的 divergence point（与 expert 首次不同 action 的位置）
   - d = divergence_point / expert_length 的分布（mean, median, std, quartiles）
   - d 值直方图数据（bins: 0-0.1, 0.1-0.2, ..., 0.9-1.0）
   - per-task-type 的 d 分布
   - early (d<0.33) / mid (0.33≤d<0.67) / late (d≥0.67) 三组的样本量

3. **γ(d) 映射预览**
   - 用 etadn_discount 的 γ(d) 函数，展示数据中 γ 值的分布
   - γ_min=0.85, γ_max=0.97 下各样本的 γ 值

4. **Expert/Failure 匹配统计**
   - exact match rate（game_file 完全匹配）
   - template match rate（同 task type）
   - unmatched failures 数量

5. **轨迹长度分析**
   - 失败轨迹 vs expert 轨迹的长度分布
   - correction span (expert_length - div_point) 分布

**输出格式**：
- `failure_mode_summary.json`: 所有统计数据的结构化 JSON
- `failure_mode_report.md`: 论文可引用的 markdown 表格和描述
- 打印 summary 到 stdout

### Divergence point 计算逻辑
参考 build_dpo_pairs.py 的实现。核心：
1. 解析 failure trajectory 的 action 序列（从 conversation 中提取 assistant 消息）
2. 解析 expert trajectory 的 action 序列
3. 逐步比较，找到第一个 action 不同的位置 = divergence_point
4. 如果所有 action 都相同但 failure 多了错误步骤，divergence_point = expert_length

### 代码规范
- 文件顶部写文件注释
- 主要函数写 docstring
- 使用 argparse CLI
- 不依赖 vllm/torch（纯 CPU 分析脚本）

### 验证
写完后 `python -m py_compile src/analyze_failure_modes.py` 验证语法。

### 完成标准
1. 脚本语法正确
2. 覆盖所有 5 类分析
3. 输出 JSON + Markdown 两种格式
4. 不依赖 GPU（纯 CPU）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "70d64043-cfe7-4c40-93f2-a3764a31ceea",
  "type": "user",
  "uuid": "3e689d68-a920-4a87-b1e0-84b012d15055",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl",
  "sessionId": "2c8f695e-2726-4bc0-b978-178d488e8a4b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-13T04:47:29.274Z_

```json
{
  "parentUuid": "3e689d68-a920-4a87-b1e0-84b012d15055",
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
  "uuid": "db841c7e-ef83-4334-b311-ceada789dc14",
  "timestamp": "2026-05-13T04:47:29.274Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl",
  "sessionId": "2c8f695e-2726-4bc0-b978-178d488e8a4b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-13T04:47:29.274Z_

```json
{
  "parentUuid": "db841c7e-ef83-4334-b311-ceada789dc14",
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
  "uuid": "7beb57f6-f059-44bc-b85a-e2b98a46084a",
  "timestamp": "2026-05-13T04:47:29.274Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl",
  "sessionId": "2c8f695e-2726-4bc0-b978-178d488e8a4b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6 · 2026-05-13T04:47:29.274Z_

```json
{
  "parentUuid": "7beb57f6-f059-44bc-b85a-e2b98a46084a",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "25758d73-6e2d-405e-ac4e-424350df913c",
  "timestamp": "2026-05-13T04:47:29.274Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl",
  "sessionId": "2c8f695e-2726-4bc0-b978-178d488e8a4b",
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
  "aiTitle": "Write failure mode analysis script for paper",
  "sessionId": "2c8f695e-2726-4bc0-b978-178d488e8a4b"
}
```

---

### Assistant

_source line 8 · 2026-05-13T04:47:33.198Z_

<details><summary>Logged reasoning block</summary>

```text
Let me start by reading the three reference files to understand the data formats and logic before writing the script.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "25758d73-6e2d-405e-ac4e-424350df913c",
  "isSidechain": false,
  "requestId": "req_011CayxkYRwncTvFsq3RBFk8",
  "type": "assistant",
  "uuid": "21231cf7-0556-40f4-a12b-ec00b4e9e5ae",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl",
  "sessionId": "2c8f695e-2726-4bc0-b978-178d488e8a4b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FE5dEVvEYJknH4gNfet4rs",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12080,
      "cache_read_input_tokens": 11841,
      "output_tokens": 293,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12080,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 293,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12080,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12080
          },
          "type": "message"
        }
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

_source line 9 · 2026-05-13T04:47:33.680Z_

先读取三个参考文件。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "21231cf7-0556-40f4-a12b-ec00b4e9e5ae",
  "isSidechain": false,
  "requestId": "req_011CayxkYRwncTvFsq3RBFk8",
  "type": "assistant",
  "uuid": "dc6e0c1b-06a8-40f5-820b-e08a37cd5241",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl",
  "sessionId": "2c8f695e-2726-4bc0-b978-178d488e8a4b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FE5dEVvEYJknH4gNfet4rs",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12080,
      "cache_read_input_tokens": 11841,
      "output_tokens": 293,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12080,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 293,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12080,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12080
          },
          "type": "message"
        }
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

_source line 10 · 2026-05-13T04:47:34.182Z_

<details open><summary>🔧 Tool call — Read · `toolu_01J135YR17tTJzA5vRw6pB52`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl/src/build_dpo_pairs.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dc6e0c1b-06a8-40f5-820b-e08a37cd5241",
  "isSidechain": false,
  "requestId": "req_011CayxkYRwncTvFsq3RBFk8",
  "type": "assistant",
  "uuid": "34cea4af-b63e-4c89-913c-54e4037c89e9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl",
  "sessionId": "2c8f695e-2726-4bc0-b978-178d488e8a4b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FE5dEVvEYJknH4gNfet4rs",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12080,
      "cache_read_input_tokens": 11841,
      "output_tokens": 293,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12080,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 293,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12080,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12080
          },
          "type": "message"
        }
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

_source line 11 · 2026-05-13T04:47:35.266Z_

<details><summary>↩ Tool result · `toolu_01MKBMiWyANdgaHKTigx73rb`</summary>

```text
1	#!/usr/bin/env python3
2	"""ETADN error-type-aware temporal discount for DMPO.
3	
4	Core formula:
5	    φ(t, T) = γ^t · (1 - γ^(T-t)) / (1 - γ^T)
6	
7	Where:
8	    t = current timestep (0-indexed)
9	    T = total trajectory length
10	    γ = gamma_e (error-type-specific discount factor)
11	
12	γ_e mapping:
13	    action errors      → γ_a = 0.85 (short correction span, concentrated credit)
14	    verification errors → γ_v = 0.92 (medium span, moderate spread)
15	    planning errors     → γ_p = 0.97 (long span, near-uniform credit)
16	
17	Integration with DPO/DMPO:
18	    Standard DPO loss: L = -log σ(β · (log π(y_w|x) - log π(y_l|x)))
19	    DMPO adds per-step weighting: replace uniform sum with φ-weighted sum
20	    ETADN: γ in φ varies by error_type of the (chosen, rejected) pair
21	
22	Dependencies: torch only
23	"""
24	import torch
25	import torch.nn.functional as F
26	from dataclasses import dataclass
27	
28	
29	@dataclass
30	class ETADNConfig:
31	    gamma_action: float = 0.85
32	    gamma_verification: float = 0.92
33	    gamma_planning: float = 0.97
34	    beta: float = 0.1
35	    label_smoothing: float = 0.0
36	
37	
38	def phi(t: int, T: int, gamma: float) -> float:
39	    """DMPO credit assignment weight for timestep t of T.
40	
41	    φ(t, T) = γ^t · (1 - γ^(T-t)) / (1 - γ^T)
42	
43	    Sums to 1 over t ∈ [0, T-1] for any γ ∈ (0, 1).
44	    """
45	    if T <= 0:
46	        return 0.0
47	    if abs(gamma - 1.0) < 1e-8:
48	        return 1.0 / T
49	    if abs(gamma) < 1e-12:
50	        return 1.0 if t == 0 else 0.0
51	    numerator = (gamma ** t) * (1.0 - gamma ** (T - t))
52	    denominator = 1.0 - gamma ** T
53	    return numerator / denominator
54	
55	
56	def compute_discount_weights(T: int, gamma: float) -> torch.Tensor:
57	    """φ weight vector of length T. Returns shape (T,) float32 tensor."""
58	    if T <= 0:
59	        return torch.tensor([], dtype=torch.float32)
60	    if abs(gamma - 1.0) < 1e-8:
61	        return torch.full((T,), 1.0 / T, dtype=torch.float32)
62	    if abs(gamma) < 1e-12:
63	        w = torch.zeros(T, dtype=torch.float32)
64	        w[0] = 1.0
65	        return w
66	    t = torch.arange(T, dtype=torch.float64)
67	    g = torch.tensor(gamma, dtype=torch.float64)
68	    numerator = g.pow(t) * (1 - g.pow(T - t))
69	    denominator = 1 - g.pow(torch.tensor(T, dtype=torch.float64))
70	    return (numerator / denominator).float()
71	
72	
73	def get_gamma_for_error_type(error_type: str, config: ETADNConfig) -> float:
74	    """Look up γ_e by error type string."""
75	    mapping = {
76	        "action": config.gamma_action,
77	        "verification": config.gamma_verification,
78	        "planning": config.gamma_planning,
79	    }
80	    return mapping.get(error_type, config.gamma_verification)
81	
82	
83	# ---------------------------------------------------------------------------
84	# DPO loss variants
85	# ---------------------------------------------------------------------------
86	
87	def _dpo_loss_from_logratios(
88	    chosen_logratios: torch.Tensor,
89	    rejected_logratios: torch.Tensor,
90	    beta: float,
91	    label_smoothing: float = 0.0,
92	) -> torch.Tensor:
93	    """Standard DPO loss from per-sample log-ratio scalars.
94	
95	    L = -log σ(β · (chosen_logratio - rejected_logratio))
96	    """
97	    logits = beta * (chosen_logratios - rejected_logratios)
98	    if label_smoothing > 0:
99	        loss = (
100	            (1 - label_smoothing) * F.logsigmoid(logits)
101	            + label_smoothing * F.logsigmoid(-logits)
102	        )
103	    else:
104	        loss = F.logsigmoid(logits)
105	    return -loss.mean()
106	
107	
108	def uniform_dpo_loss(
109	    chosen_logps: torch.Tensor,
110	    rejected_logps: torch.Tensor,
111	    ref_chosen_logps: torch.Tensor,
112	    ref_rejected_logps: torch.Tensor,
113	    lengths: torch.Tensor,
114	    beta: float = 0.1,
115	    label_smoothing: float = 0.0,
116	) -> torch.Tensor:
117	    """Standard DPO with uniform per-token weighting (baseline).
118	
119	    Args:
120	        chosen_logps: (batch, max_len) per-token log probs for chosen
121	        rejected_logps: (batch, max_len) per-token log probs for rejected
122	        ref_chosen_logps: (batch, max_len) reference model per-token log probs
123	        ref_rejected_logps: (batch, max_len) reference model per-token log probs
124	        lengths: (batch,) valid token count per sample
125	        beta: DPO temperature
126	        label_smoothing: label smoothing factor
127	    """
128	    batch_size, max_len = chosen_logps.shape
129	    mask = torch.arange(max_len, device=chosen_logps.device).unsqueeze(0) < lengths.unsqueeze(1)
130	    mask = mask.float()
131	
132	    chosen_sums = (chosen_logps * mask).sum(dim=1)
133	    rejected_sums = (rejected_logps * mask).sum(dim=1)
134	    ref_chosen_sums = (ref_chosen_logps * mask).sum(dim=1)
135	    ref_rejected_sums = (ref_rejected_logps * mask).sum(dim=1)
136	
137	    chosen_logratios = chosen_sums - ref_chosen_sums
138	    rejected_logratios = rejected_sums - ref_rejected_sums
139	
140	    return _dpo_loss_from_logratios(
141	        chosen_logratios, rejected_logratios, beta, label_smoothing
142	    )
143	
144	
145	def single_gamma_dpo_loss(
146	    chosen_logps: torch.Tensor,
147	    rejected_logps: torch.Tensor,
148	    ref_chosen_logps: torch.Tensor,
149	    ref_rejected_logps: torch.Tensor,
150	    lengths: torch.Tensor,
151	    gamma: float = 0.92,
152	    beta: float = 0.1,
153	    label_smoothing: float = 0.0,
154	) -> torch.Tensor:
155	    """DMPO with a single shared γ for all samples (ablation baseline)."""
156	    batch_size, max_len = chosen_logps.shape
157	    device = chosen_logps.device
158	
159	    results_chosen = torch.zeros(batch_size, device=device)
160	    results_rejected = torch.zeros(batch_size, device=device)
161	    results_ref_chosen = torch.zeros(batch_size, device=device)
162	    results_ref_rejected = torch.zeros(batch_size, device=device)
163	
164	    for i in range(batch_size):
165	        T = int(lengths[i].item())
166	        if T <= 0:
167	            continue
168	        w = compute_discount_weights(T, gamma).to(device)
169	        results_chosen[i] = (chosen_logps[i, :T] * w).sum()
170	        results_rejected[i] = (rejected_logps[i, :T] * w).sum()
171	        results_ref_chosen[i] = (ref_chosen_logps[i, :T] * w).sum()
172	        results_ref_rejected[i] = (ref_rejected_logps[i, :T] * w).sum()
173	
174	    chosen_logratios = results_chosen - results_ref_chosen
175	    rejected_logratios = results_rejected - results_ref_rejected
176	
177	    return _dpo_loss_from_logratios(
178	        chosen_logratios, rejected_logratios, beta, label_smoothing
179	    )
180	
181	
182	def etadn_dpo_loss(
183	    chosen_logps: torch.Tensor,
184	    rejected_logps: torch.Tensor,
185	    ref_chosen_logps: torch.Tensor,
186	    ref_rejected_logps: torch.Tensor,
187	    error_types: list[str],
188	    lengths: torch.Tensor,
189	    config: ETADNConfig,
190	) -> torch.Tensor:
191	    """ETADN-aware DPO loss with per-error-type temporal discount.
192	
193	    For each sample in the batch:
194	    1. Look up γ_e based on error_type
195	    2. Compute φ(t, T, γ_e) weights for sequence length T
196	    3. Compute weighted sum of per-token log prob differences
197	    4. Apply standard DPO loss with β
198	    """
199	    batch_size, max_len = chosen_logps.shape
200	    device = chosen_logps.device
201	
202	    results_chosen = torch.zeros(batch_size, device=device)
203	    results_rejected = torch.zeros(batch_size, device=device)
204	    results_ref_chosen = torch.zeros(batch_size, device=device)
205	    results_ref_rejected = torch.zeros(batch_size, device=device)
206	
207	    for i in range(batch_size):
208	        T = int(lengths[i].item())
209	        if T <= 0:
210	            continue
211	        gamma = get_gamma_for_error_type(error_types[i], config)
212	        w = compute_discount_weights(T, gamma).to(device)
213	        results_chosen[i] = (chosen_logps[i, :T] * w).sum()
214	        results_rejected[i] = (rejected_logps[i, :T] * w).sum()
215	        results_ref_chosen[i] = (ref_chosen_logps[i, :T] * w).sum()
216	        results_ref_rejected[i] = (ref_rejected_logps[i, :T] * w).sum()
217	
218	    chosen_logratios = results_chosen - results_ref_chosen
219	    rejected_logratios = results_rejected - results_ref_rejected
220	
221	    return _dpo_loss_from_logratios(
222	        chosen_logratios, rejected_logratios, config.beta, config.label_smoothing
223	    )
224	
225	
226	# ---------------------------------------------------------------------------
227	# Self-tests
228	# ---------------------------------------------------------------------------
229	
230	def _test_phi_weights_properties():
231	    """φ weights: positive, monotonically decreasing for γ<1, γ=1 is uniform."""
232	    for gamma in [0.5, 0.85, 0.92, 0.97, 0.99]:
233	        for T in [1, 3, 5, 10, 20]:
234	            w = compute_discount_weights(T, gamma)
235	            assert len(w) == T
236	            assert (w > 0).all(), f"gamma={gamma}, T={T}: non-positive weights"
237	            for i in range(1, T):
238	                assert w[i] <= w[i - 1] + 1e-6, (
239	                    f"gamma={gamma}, T={T}: not monotonically decreasing at {i}"
240	                )
241	    # γ=1 → uniform
242	    w_uniform = compute_discount_weights(5, 1.0)
243	    assert abs(w_uniform.sum().item() - 1.0) < 1e-5
244	    assert abs(w_uniform[0].item() - 0.2) < 1e-5
245	    # scalar φ matches vectorized
246	    for gamma in [0.85, 0.97]:
247	        T = 8
248	        w = compute_discount_weights(T, gamma)
249	        for t in range(T):
250	            assert abs(w[t].item() - phi(t, T, gamma)) < 1e-5, (
251	                f"phi mismatch at t={t}, T={T}, gamma={gamma}"
252	            )
253	    print("  phi weights properties: PASS")
254	
255	
256	def _test_phi_shape_by_gamma():
257	    """Lower γ → steeper decay; higher γ → more uniform."""
258	    T = 10
259	    w_low = compute_discount_weights(T, 0.85)
260	    w_high = compute_discount_weights(T, 0.97)
261	
262	    # φ(0,T,γ) = 1 for all γ, so first weight is the same
263	    assert abs(w_low[0].item() - 1.0) < 1e-5
264	    assert abs(w_high[0].item() - 1.0) < 1e-5
265	    # Lower γ decays faster → last weight should be smaller
266	    assert w_low[-1] < w_high[-1], "Low gamma should decay faster at the tail"
267	    # γ=0.97 should be more uniform (smaller max-min spread)
268	    spread_low = (w_low.max() - w_low.min()).item()
269	    spread_high = (w_high.max() - w_high.min()).item()
270	    assert spread_low > spread_high, "High gamma should be more uniform"
271	    print("  phi shape by gamma: PASS")
272	
273	
274	def _test_dpo_loss_gradients():
275	    """All three loss variants should produce finite loss and valid gradients."""
276	    torch.manual_seed(42)
277	    batch_size, max_len = 4, 8
278	    config = ETADNConfig()
279	
280	    chosen = torch.randn(batch_size, max_len, requires_grad=True)
281	    rejected = torch.randn(batch_size, max_len, requires_grad=True)
282	    ref_chosen = torch.randn(batch_size, max_len)
283	    ref_rejected = torch.randn(batch_size, max_len)
284	    lengths = torch.tensor([6, 8, 5, 7])
285	    error_types = ["action", "verification", "planning", "action"]
286	
287	    # Uniform DPO
288	    loss_u = uniform_dpo_loss(chosen, rejected, ref_chosen, ref_rejected, lengths)
289	    loss_u.backward(retain_graph=True)
290	    assert torch.isfinite(loss_u), f"uniform loss not finite: {loss_u}"
291	    assert chosen.grad is not None
292	    chosen.grad.zero_()
293	
294	    # Single-gamma DMPO
295	    loss_s = single_gamma_dpo_loss(
296	        chosen, rejected, ref_chosen, ref_rejected, lengths, gamma=0.92
297	    )
298	    loss_s.backward(retain_graph=True)
299	    assert torch.isfinite(loss_s), f"single_gamma loss not finite: {loss_s}"
300	    chosen.grad.zero_()
301	
302	    # ETADN
303	    loss_e = etadn_dpo_loss(
304	        chosen, rejected, ref_chosen, ref_rejected, error_types, lengths, config
305	    )
306	    loss_e.backward()
307	    assert torch.isfinite(loss_e), f"etadn loss not finite: {loss_e}"
308	
309	    print(f"  uniform_dpo_loss:      {loss_u.item():.4f}")
310	    print(f"  single_gamma_dpo_loss: {loss_s.item():.4f}")
311	    print(f"  etadn_dpo_loss:        {loss_e.item():.4f}")
312	    print("  gradient check: PASS")
313	
314	
315	def _test_gamma_lookup():
316	    """get_gamma_for_error_type should return correct values."""
317	    config = ETADNConfig()
318	    assert get_gamma_for_error_type("action", config) == 0.85
319	    assert get_gamma_for_error_type("verification", config) == 0.92
320	    assert get_gamma_for_error_type("planning", config) == 0.97
321	    assert get_gamma_for_error_type("unknown", config) == 0.92  # fallback
322	    print("  gamma lookup: PASS")
323	
324	
325	if __name__ == "__main__":
326	    print("ETADN discount module self-tests")
327	    print("=" * 40)
328	    _test_phi_weights_properties()
329	    _test_phi_shape_by_gamma()
330	    _test_gamma_lookup()
331	    _test_dpo_loss_gradients()
332	    print("=" * 40)
333	    print("All tests passed.")
334	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "294354ec-aa48-4a10-8c69-2a2bfb80fbb3",
  "isSidechain": false,
  "promptId": "70d64043-cfe7-4c40-93f2-a3764a31ceea",
  "type": "user",
  "uuid": "5f2b94c6-eb62-4738-b496-b7444b8a07d1",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl/src/etadn_discount.py",
      "content": "#!/usr/bin/env python3\n\"\"\"ETADN error-type-aware temporal discount for DMPO.\n\nCore formula:\n    φ(t, T) = γ^t · (1 - γ^(T-t)) / (1 - γ^T)\n\nWhere:\n    t = current timestep (0-indexed)\n    T = total trajectory length\n    γ = gamma_e (error-type-specific discount factor)\n\nγ_e mapping:\n    action errors      → γ_a = 0.85 (short correction span, concentrated credit)\n    verification errors → γ_v = 0.92 (medium span, moderate spread)\n    planning errors     → γ_p = 0.97 (long span, near-uniform credit)\n\nIntegration with DPO/DMPO:\n    Standard DPO loss: L = -log σ(β · (log π(y_w|x) - log π(y_l|x)))\n    DMPO adds per-step weighting: replace uniform sum with φ-weighted sum\n    ETADN: γ in φ varies by error_type of the (chosen, rejected) pair\n\nDependencies: torch only\n\"\"\"\nimport torch\nimport torch.nn.functional as F\nfrom dataclasses import dataclass\n\n\n@dataclass\nclass ETADNConfig:\n    gamma_action: float = 0.85\n    gamma_verification: float = 0.92\n    gamma_planning: float = 0.97\n    beta: float = 0.1\n    label_smoothing: float = 0.0\n\n\ndef phi(t: int, T: int, gamma: float) -> float:\n    \"\"\"DMPO credit assignment weight for timestep t of T.\n\n    φ(t, T) = γ^t · (1 - γ^(T-t)) / (1 - γ^T)\n\n    Sums to 1 over t ∈ [0, T-1] for any γ ∈ (0, 1).\n    \"\"\"\n    if T <= 0:\n        return 0.0\n    if abs(gamma - 1.0) < 1e-8:\n        return 1.0 / T\n    if abs(gamma) < 1e-12:\n        return 1.0 if t == 0 else 0.0\n    numerator = (gamma ** t) * (1.0 - gamma ** (T - t))\n    denominator = 1.0 - gamma ** T\n    return numerator / denominator\n\n\ndef compute_discount_weights(T: int, gamma: float) -> torch.Tensor:\n    \"\"\"φ weight vector of length T. Returns shape (T,) float32 tensor.\"\"\"\n    if T <= 0:\n        return torch.tensor([], dtype=torch.float32)\n    if abs(gamma - 1.0) < 1e-8:\n        return torch.full((T,), 1.0 / T, dtype=torch.float32)\n    if abs(gamma) < 1e-12:\n        w = torch.zeros(T, dtype=torch.float32)\n        w[0] = 1.0\n        return w\n    t = torch.arange(T, dtype=torch.float64)\n    g = torch.tensor(gamma, dtype=torch.float64)\n    numerator = g.pow(t) * (1 - g.pow(T - t))\n    denominator = 1 - g.pow(torch.tensor(T, dtype=torch.float64))\n    return (numerator / denominator).float()\n\n\ndef get_gamma_for_error_type(error_type: str, config: ETADNConfig) -> float:\n    \"\"\"Look up γ_e by error type string.\"\"\"\n    mapping = {\n        \"action\": config.gamma_action,\n        \"verification\": config.gamma_verification,\n        \"planning\": config.gamma_planning,\n    }\n    return mapping.get(error_type, config.gamma_verification)\n\n\n# ---------------------------------------------------------------------------\n# DPO loss variants\n# ---------------------------------------------------------------------------\n\ndef _dpo_loss_from_logratios(\n    chosen_logratios: torch.Tensor,\n    rejected_logratios: torch.Tensor,\n    beta: float,\n    label_smoothing: float = 0.0,\n) -> torch.Tensor:\n    \"\"\"Standard DPO loss from per-sample log-ratio scalars.\n\n    L = -log σ(β · (chosen_logratio - rejected_logratio))\n    \"\"\"\n    logits = beta * (chosen_logratios - rejected_logratios)\n    if label_smoothing > 0:\n        loss = (\n            (1 - label_smoothing) * F.logsigmoid(logits)\n            + label_smoothing * F.logsigmoid(-logits)\n        )\n    else:\n        loss = F.logsigmoid(logits)\n    return -loss.mean()\n\n\ndef uniform_dpo_loss(\n    chosen_logps: torch.Tensor,\n    rejected_logps: torch.Tensor,\n    ref_chosen_logps: torch.Tensor,\n    ref_rejected_logps: torch.Tensor,\n    lengths: torch.Tensor,\n    beta: float = 0.1,\n    label_smoothing: float = 0.0,\n) -> torch.Tensor:\n    \"\"\"Standard DPO with uniform per-token weighting (baseline).\n\n    Args:\n        chosen_logps: (batch, max_len) per-token log probs for chosen\n        rejected_logps: (batch, max_len) per-token log probs for rejected\n        ref_chosen_logps: (batch, max_len) reference model per-token log probs\n        ref_rejected_logps: (batch, max_len) reference model per-token log probs\n        lengths: (batch,) valid token count per sample\n        beta: DPO temperature\n        label_smoothing: label smoothing factor\n    \"\"\"\n    batch_size, max_len = chosen_logps.shape\n    mask = torch.arange(max_len, device=chosen_logps.device).unsqueeze(0) < lengths.unsqueeze(1)\n    mask = mask.float()\n\n    chosen_sums = (chosen_logps * mask).sum(dim=1)\n    rejected_sums = (rejected_logps * mask).sum(dim=1)\n    ref_chosen_sums = (ref_chosen_logps * mask).sum(dim=1)\n    ref_rejected_sums = (ref_rejected_logps * mask).sum(dim=1)\n\n    chosen_logratios = chosen_sums - ref_chosen_sums\n    rejected_logratios = rejected_sums - ref_rejected_sums\n\n    return _dpo_loss_from_logratios(\n        chosen_logratios, rejected_logratios, beta, label_smoothing\n    )\n\n\ndef single_gamma_dpo_loss(\n    chosen_logps: torch.Tensor,\n    rejected_logps: torch.Tensor,\n    ref_chosen_logps: torch.Tensor,\n    ref_rejected_logps: torch.Tensor,\n    lengths: torch.Tensor,\n    gamma: float = 0.92,\n    beta: float = 0.1,\n    label_smoothing: float = 0.0,\n) -> torch.Tensor:\n    \"\"\"DMPO with a single shared γ for all samples (ablation baseline).\"\"\"\n    batch_size, max_len = chosen_logps.shape\n    device = chosen_logps.device\n\n    results_chosen = torch.zeros(batch_size, device=device)\n    results_rejected = torch.zeros(batch_size, device=device)\n    results_ref_chosen = torch.zeros(batch_size, device=device)\n    results_ref_rejected = torch.zeros(batch_size, device=device)\n\n    for i in range(batch_size):\n        T = int(lengths[i].item())\n        if T <= 0:\n            continue\n        w = compute_discount_weights(T, gamma).to(device)\n        results_chosen[i] = (chosen_logps[i, :T] * w).sum()\n        results_rejected[i] = (rejected_logps[i, :T] * w).sum()\n        results_ref_chosen[i] = (ref_chosen_logps[i, :T] * w).sum()\n        results_ref_rejected[i] = (ref_rejected_logps[i, :T] * w).sum()\n\n    chosen_logratios = results_chosen - results_ref_chosen\n    rejected_logratios = results_rejected - results_ref_rejected\n\n    return _dpo_loss_from_logratios(\n        chosen_logratios, rejected_logratios, beta, label_smoothing\n    )\n\n\ndef etadn_dpo_loss(\n    chosen_logps: torch.Tensor,\n    rejected_logps: torch.Tensor,\n    ref_chosen_logps: torch.Tensor,\n    ref_rejected_logps: torch.Tensor,\n    error_types: list[str],\n    lengths: torch.Tensor,\n    config: ETADNConfig,\n) -> torch.Tensor:\n    \"\"\"ETADN-aware DPO loss with per-error-type temporal discount.\n\n    For each sample in the batch:\n    1. Look up γ_e based on error_type\n    2. Compute φ(t, T, γ_e) weights for sequence length T\n    3. Compute weighted sum of per-token log prob differences\n    4. Apply standard DPO loss with β\n    \"\"\"\n    batch_size, max_len = chosen_logps.shape\n    device = chosen_logps.device\n\n    results_chosen = torch.zeros(batch_size, device=device)\n    results_rejected = torch.zeros(batch_size, device=device)\n    results_ref_chosen = torch.zeros(batch_size, device=device)\n    results_ref_rejected = torch.zeros(batch_size, device=device)\n\n    for i in range(batch_size):\n        T = int(lengths[i].item())\n        if T <= 0:\n            continue\n        gamma = get_gamma_for_error_type(error_types[i], config)\n        w = compute_discount_weights(T, gamma).to(device)\n        results_chosen[i] = (chosen_logps[i, :T] * w).sum()\n        results_rejected[i] = (rejected_logps[i, :T] * w).sum()\n        results_ref_chosen[i] = (ref_chosen_logps[i, :T] * w).sum()\n        results_ref_rejected[i] = (ref_rejected_logps[i, :T] * w).sum()\n\n    chosen_logratios = results_chosen - results_ref_chosen\n    rejected_logratios = results_rejected - results_ref_rejected\n\n    return _dpo_loss_from_logratios(\n        chosen_logratios, rejected_logratios, config.beta, config.label_smoothing\n    )\n\n\n# ---------------------------------------------------------------------------\n# Self-tests\n# ---------------------------------------------------------------------------\n\ndef _test_phi_weights_properties():\n    \"\"\"φ weights: positive, monotonically decreasing for γ<1, γ=1 is uniform.\"\"\"\n    for gamma in [0.5, 0.85, 0.92, 0.97, 0.99]:\n        for T in [1, 3, 5, 10, 20]:\n            w = compute_discount_weights(T, gamma)\n            assert len(w) == T\n            assert (w > 0).all(), f\"gamma={gamma}, T={T}: non-positive weights\"\n            for i in range(1, T):\n                assert w[i] <= w[i - 1] + 1e-6, (\n                    f\"gamma={gamma}, T={T}: not monotonically decreasing at {i}\"\n                )\n    # γ=1 → uniform\n    w_uniform = compute_discount_weights(5, 1.0)\n    assert abs(w_uniform.sum().item() - 1.0) < 1e-5\n    assert abs(w_uniform[0].item() - 0.2) < 1e-5\n    # scalar φ matches vectorized\n    for gamma in [0.85, 0.97]:\n        T = 8\n        w = compute_discount_weights(T, gamma)\n        for t in range(T):\n            assert abs(w[t].item() - phi(t, T, gamma)) < 1e-5, (\n                f\"phi mismatch at t={t}, T={T}, gamma={gamma}\"\n            )\n    print(\"  phi weights properties: PASS\")\n\n\ndef _test_phi_shape_by_gamma():\n    \"\"\"Lower γ → steeper decay; higher γ → more uniform.\"\"\"\n    T = 10\n    w_low = compute_discount_weights(T, 0.85)\n    w_high = compute_discount_weights(T, 0.97)\n\n    # φ(0,T,γ) = 1 for all γ, so first weight is the same\n    assert abs(w_low[0].item() - 1.0) < 1e-5\n    assert abs(w_high[0].item() - 1.0) < 1e-5\n    # Lower γ decays faster → last weight should be smaller\n    assert w_low[-1] < w_high[-1], \"Low gamma should decay faster at the tail\"\n    # γ=0.97 should be more uniform (smaller max-min spread)\n    spread_low = (w_low.max() - w_low.min()).item()\n    spread_high = (w_high.max() - w_high.min()).item()\n    assert spread_low > spread_high, \"High gamma should be more uniform\"\n    print(\"  phi shape by gamma: PASS\")\n\n\ndef _test_dpo_loss_gradients():\n    \"\"\"All three loss variants should produce finite loss and valid gradients.\"\"\"\n    torch.manual_seed(42)\n    batch_size, max_len = 4, 8\n    config = ETADNConfig()\n\n    chosen = torch.randn(batch_size, max_len, requires_grad=True)\n    rejected = torch.randn(batch_size, max_len, requires_grad=True)\n    ref_chosen = torch.randn(batch_size, max_len)\n    ref_rejected = torch.randn(batch_size, max_len)\n    lengths = torch.tensor([6, 8, 5, 7])\n    error_types = [\"action\", \"verification\", \"planning\", \"action\"]\n\n    # Uniform DPO\n    loss_u = uniform_dpo_loss(chosen, rejected, ref_chosen, ref_rejected, lengths)\n    loss_u.backward(retain_graph=True)\n    assert torch.isfinite(loss_u), f\"uniform loss not finite: {loss_u}\"\n    assert chosen.grad is not None\n    chosen.grad.zero_()\n\n    # Single-gamma DMPO\n    loss_s = single_gamma_dpo_loss(\n        chosen, rejected, ref_chosen, ref_rejected, lengths, gamma=0.92\n    )\n    loss_s.backward(retain_graph=True)\n    assert torch.isfinite(loss_s), f\"single_gamma loss not finite: {loss_s}\"\n    chosen.grad.zero_()\n\n    # ETADN\n    loss_e = etadn_dpo_loss(\n        chosen, rejected, ref_chosen, ref_rejected, error_types, lengths, config\n    )\n    loss_e.backward()\n    assert torch.isfinite(loss_e), f\"etadn loss not finite: {loss_e}\"\n\n    print(f\"  uniform_dpo_loss:      {loss_u.item():.4f}\")\n    print(f\"  single_gamma_dpo_loss: {loss_s.item():.4f}\")\n    print(f\"  etadn_dpo_loss:        {loss_e.item():.4f}\")\n    print(\"  gradient check: PASS\")\n\n\ndef _test_gamma_lookup():\n    \"\"\"get_gamma_for_error_type should return correct values.\"\"\"\n    config = ETADNConfig()\n    assert get_gamma_for_error_type(\"action\", config) == 0.85\n    assert get_gamma_for_error_type(\"verification\", config) == 0.92\n    assert get_gamma_for_error_type(\"planning\", config) == 0.97\n    assert get_gamma_for_error_type(\"unknown\", config) == 0.92  # fallback\n    print(\"  gamma lookup: PASS\")\n\n\nif __name__ == \"__main__\":\n    print(\"ETADN discount module self-tests\")\n    print(\"=\" * 40)\n    _test_phi_weights_properties()\n    _test_phi_shape_by_gamma()\n    _test_gamma_lookup()\n    _test_dpo_loss_gradients()\n    print(\"=\" * 40)\n    print(\"All tests passed.\")\n",
      "numLines": 334,
      "startLine": 1,
      "totalLines": 334
    }
  },
  "sourceToolAssistantUUID": "294354ec-aa48-4a10-8c69-2a2bfb80fbb3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl",
  "sessionId": "2c8f695e-2726-4bc0-b978-178d488e8a4b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-13T04:47:34.194Z_

<details><summary>↩ Tool result · `toolu_01J135YR17tTJzA5vRw6pB52`</summary>

```text
1	"""Build DPO preference pairs from classified failures and expert trajectories.
2	
3	Fix [2026-05-12]: Use true divergence point instead of LLM-reported failure_step.
4	Old logic used failure_step as split point, but expert and failure trajectories
5	may already differ before that step → prompt-chosen state inconsistency.
6	New logic compares action sequences step-by-step to find the real divergence.
7	
8	For each classified failure:
9	  1. Match expert trajectory by game_file
10	  2. Compare actions step-by-step to find divergence point
11	  3. Shared prefix = prompt, expert continuation = chosen, failure continuation = rejected
12	
13	Input:
14	  - classified_errors.jsonl (error_type, failure_step, conversations)
15	  - alfworld_sft.json (expert trajectories)
16	  - (optional) trajectory_dir with failure JSONL files
17	
18	Output per line:
19	  {prompt, chosen, rejected, error_type, gamma_e, correction_span,
20	   task_id, task_type, game_file, failure_step, divergence_step, metadata}
21	
22	Usage:
23	  python src/build_dpo_pairs.py \
24	    --classified outputs/classify_compare_with_hint_20.jsonl \
25	    --expert data/alfworld_sft.json \
26	    --output data/dpo_pairs_v2.jsonl \
27	    --gamma action=0.85,verification=0.92,planning=0.97
28	
29	Dependencies: (stdlib only)
30	"""
31	
32	import argparse
33	import json
34	import logging
35	from collections import Counter, defaultdict
36	from pathlib import Path
37	
38	logger = logging.getLogger("build_dpo")
39	
40	DEFAULT_GAMMA_MAP = {
41	    "action": 0.85,
42	    "verification": 0.92,
43	    "planning": 0.97,
44	}
45	
46	
47	def parse_gamma_arg(s: str) -> dict[str, float]:
48	    """Parse 'action=0.85,verification=0.92,planning=0.97' → dict."""
49	    gamma_map = dict(DEFAULT_GAMMA_MAP)
50	    for item in s.split(","):
51	        k, v = item.strip().split("=")
52	        gamma_map[k.strip()] = float(v.strip())
53	    return gamma_map
54	
55	
56	# ---------------------------------------------------------------------------
57	# Game file normalization
58	# ---------------------------------------------------------------------------
59	
60	def normalize_game_file(game_file: str) -> str:
61	    """Extract &lt;task_dir>/&lt;trial_dir> as matching key.
62	
63	    Expert:     data/json_2.1.1/train/&lt;task>/&lt;trial>
64	    Trajectory: /root/.../json_2.1.1/train/&lt;task>/&lt;trial>/game.tw-pddl
65	    """
66	    gf = game_file.rstrip("/")
67	    if gf.endswith("/game.tw-pddl"):
68	        gf = gf[: -len("/game.tw-pddl")]
69	    parts = gf.split("/")
70	    return "/".join(parts[-2:]) if len(parts) >= 2 else gf
71	
72	
73	# ---------------------------------------------------------------------------
74	# Message helpers
75	# ---------------------------------------------------------------------------
76	
77	def _role(msg: dict) -> str:
78	    """Get role from either format."""
79	    return msg.get("role") or {"human": "user", "gpt": "assistant"}.get(msg.get("from", ""), "")
80	
81	
82	def _content(msg: dict) -> str:
83	    """Get content from either format."""
84	    return msg.get("content") or msg.get("value", "")
85	
86	
87	def msg_to_standard(msg: dict) -> dict:
88	    return {"role": _role(msg), "content": _content(msg)}
89	
90	
91	# ---------------------------------------------------------------------------
92	# Step extraction
93	# ---------------------------------------------------------------------------
94	
95	def find_task_start(conversations: list) -> int:
96	    """Index of first action step after the actual task description.
97	
98	    Handles both expert (no ICL) and trajectory (with ICL prefix) formats by
99	    finding the LAST 'Your task is to:' user message, then the first action after it.
100	    """
101	    task_desc_idx = -1
102	    for i, msg in enumerate(conversations):
103	        if _role(msg) in ("user", "human") and "Your task is to:" in _content(msg):
104	            task_desc_idx = i
105	
106	    search_from = task_desc_idx + 1 if task_desc_idx >= 0 else 0
107	    for i in range(search_from, len(conversations)):
108	        if _role(conversations[i]) in ("assistant", "gpt") and "Action:" in _content(conversations[i]):
109	            return i
110	
111	    return len(conversations)
112	
113	
114	def extract_steps(conversations: list, start_idx: int) -> list[tuple[dict, dict | None]]:
115	    """Extract (action_msg, obs_msg|None) pairs from start_idx onward."""
116	    steps = []
117	    i = start_idx
118	    while i < len(conversations):
119	        if _role(conversations[i]) in ("assistant", "gpt"):
120	            action = conversations[i]
121	            obs = None
122	            if i + 1 < len(conversations) and _role(conversations[i + 1]) in ("user", "human"):
123	                obs = conversations[i + 1]
124	                i += 2
125	            else:
126	                i += 1
127	            steps.append((action, obs))
128	        else:
129	            i += 1
130	    return steps
131	
132	
133	def count_expert_action_steps(expert: dict) -> int:
134	    return sum(
135	        1
136	        for m in expert["conversations"]
137	        if m["from"] == "gpt" and "Action:" in m.get("value", "")
138	    )
139	
140	
141	# ---------------------------------------------------------------------------
142	# Action comparison
143	# ---------------------------------------------------------------------------
144	
145	def extract_action_text(content: str) -> str:
146	    """Extract normalized 'Action: ...' line from a step message.
147	
148	    ALFWorld actions follow "Thought: ...\\nAction: &lt;action>". We extract
149	    the action part and normalize whitespace + case for robust comparison.
150	    """
151	    for line in content.split("\n"):
152	        stripped = line.strip()
153	        if stripped.lower().startswith("action:"):
154	            return " ".join(stripped[len("action:"):].split()).lower()
155	    return " ".join(content.split()).lower()
156	
157	
158	def find_divergence_point(
159	    expert_steps: list[tuple[dict, dict | None]],
160	    fail_steps: list[tuple[dict, dict | None]],
161	) -> int:
162	    """Find the first step where expert and failure trajectories take different actions.
163	
164	    Compares normalized action strings step-by-step. In ALFWorld, same game_file
165	    + same actions → same observations, so action match guarantees state match.
166	
167	    Args:
168	        expert_steps: List of (action_msg, obs_msg|None) from expert trajectory.
169	        fail_steps: List of (action_msg, obs_msg|None) from failure trajectory.
170	
171	    Returns:
172	        0-based index of the first differing step. If one is a prefix of the
173	        other, returns the shorter length (no shared step beyond that).
174	    """
175	    min_len = min(len(expert_steps), len(fail_steps))
176	    for i in range(min_len):
177	        expert_action = extract_action_text(_content(expert_steps[i][0]))
178	        fail_action = extract_action_text(_content(fail_steps[i][0]))
179	        if expert_action != fail_action:
180	            return i
181	    return min_len
182	
183	
184	# ---------------------------------------------------------------------------
185	# Pair construction
186	# ---------------------------------------------------------------------------
187	
188	def build_pair(
189	    rec: dict,
190	    expert: dict,
191	    gamma_map: dict[str, float] | None = None,
192	) -> dict | None:
193	    """Build one DPO pair using true divergence point between expert and failure."""
194	    if gamma_map is None:
195	        gamma_map = DEFAULT_GAMMA_MAP
196	
197	    fail_convs = rec["conversations"]
198	    expert_convs = expert["conversations"]
199	
200	    fail_start = find_task_start(fail_convs)
201	    expert_start = find_task_start(expert_convs)
202	
203	    fail_steps = extract_steps(fail_convs, fail_start)
204	    expert_steps = extract_steps(expert_convs, expert_start)
205	
206	    if not fail_steps or not expert_steps:
207	        return None
208	
209	    divergence = find_divergence_point(expert_steps, fail_steps)
210	
211	    if divergence >= len(expert_steps) or divergence >= len(fail_steps):
212	        logger.debug(
213	            "task_id=%s: no divergence found (expert=%d, fail=%d steps, div=%d)",
214	            rec.get("task_id"), len(expert_steps), len(fail_steps), divergence,
215	        )
216	        return None
217	
218	    correction_span = len(expert_steps) - divergence
219	    error_type = rec.get("error_type", "unknown")
220	
221	    # Prompt: ICL/header + shared prefix steps (identical actions + observations)
222	    prompt_msgs = [msg_to_standard(m) for m in fail_convs[:fail_start]]
223	    for i in range(divergence):
224	        action, obs = expert_steps[i]
225	        prompt_msgs.append(msg_to_standard(action))
226	        if obs is not None:
227	            prompt_msgs.append(msg_to_standard(obs))
228	
229	    # Chosen: expert continuation from divergence point
230	    chosen_msgs = []
231	    for i in range(divergence, len(expert_steps)):
232	        action, obs = expert_steps[i]
233	        chosen_msgs.append(msg_to_standard(action))
234	        if obs is not None:
235	            chosen_msgs.append(msg_to_standard(obs))
236	
237	    # Rejected: failure continuation from divergence point
238	    rejected_msgs = []
239	    for i in range(divergence, len(fail_steps)):
240	        action, obs = fail_steps[i]
241	        rejected_msgs.append(msg_to_standard(action))
242	        if obs is not None:
243	            rejected_msgs.append(msg_to_standard(obs))
244	
245	    if not chosen_msgs or not rejected_msgs:
246	        return None
247	
248	    # Infer task_type from expert game_file (format: &lt;task_type>/&lt;trial_id>)
249	    gf = expert.get("game_file", "")
250	    parts = gf.split("/")
251	    task_type = ""
252	    for p in parts:
253	        if p.startswith(("pick_", "clean_", "heat_", "cool_", "put_", "examine_", "look_")):
254	            task_type = p
255	            break
256	    if not task_type:
257	        task_type = rec.get("task_type", "")
258	
259	    return {
260	        "prompt": prompt_msgs,
261	        "chosen": chosen_msgs,
262	        "rejected": rejected_msgs,
263	        "error_type": error_type,
264	        "gamma_e": gamma_map.get(error_type, gamma_map.get("verification", 0.92)),
265	        "correction_span": correction_span,
266	        "task_id": rec.get("task_id"),
267	        "task_type": task_type,
268	        "game_file": rec.get("game_file", ""),
269	        "failure_step": rec.get("failure_step", -1),
270	        "divergence_step": divergence + 1,
271	        "metadata": {
272	            "expert_steps": len(expert_steps),
273	            "model_steps": len(fail_steps),
274	            "divergence_step": divergence,
275	            "classification_source": rec.get("llm_original_type_source", "unknown"),
276	        },
277	    }
278	
279	
280	# ---------------------------------------------------------------------------
281	# Data loading
282	# ---------------------------------------------------------------------------
283	
284	def load_expert_index(path: str) -> dict:
285	    with open(path) as f:
286	        experts = json.load(f)
287	    index = {}
288	    for ex in experts:
289	        index[normalize_game_file(ex["game_file"])] = ex
290	    logger.info("Loaded %d experts", len(experts))
291	    return index
292	
293	
294	def load_classified(path: str) -> list:
295	    records = []
296	    with open(path) as f:
297	        for line in f:
298	            if line.strip():
299	                records.append(json.loads(line))
300	    logger.info("Loaded %d classified records", len(records))
301	    return records
302	
303	
304	def load_trajectories_from_dir(traj_dir: str) -> dict:
305	    """Index trajectory files by normalized game_file (fallback for missing conversations)."""
306	    index = {}
307	    for p in sorted(Path(traj_dir).glob("*.jsonl")):
308	        with open(p) as f:
309	            for line in f:
310	                if line.strip():
311	                    traj = json.loads(line)
312	                    index[normalize_game_file(traj.get("game_file", ""))] = traj
313	    logger.info("Loaded %d trajectories from %s", len(index), traj_dir)
314	    return index
315	
316	
317	# ---------------------------------------------------------------------------
318	# Main
319	# ---------------------------------------------------------------------------
320	
321	def main():
322	    parser = argparse.ArgumentParser(
323	        description="Build DPO pairs from classified failures + expert trajectories"
324	    )
325	    parser.add_argument(
326	        "--classified",
327	        type=str,
328	        default="data/classified/classified_errors.jsonl",
329	        help="Classified errors JSONL",
330	    )
331	    parser.add_argument(
332	        "--expert",
333	        type=str,
334	        default="eto_repo/data/alfworld_sft.json",
335	        help="Expert trajectories JSON",
336	    )
337	    parser.add_argument(
338	        "--trajectory_dir",
339	        type=str,
340	        default=None,
341	        help="Failure trajectory JSONL dir (optional; uses classified conversations if omitted)",
342	    )
343	    parser.add_argument(
344	        "--output",
345	        type=str,
346	        default="data/dpo_pairs_v2.jsonl",
347	        help="Output JSONL path",
348	    )
349	    parser.add_argument(
350	        "--gamma",
351	        type=str,
352	        default="action=0.85,verification=0.92,planning=0.97",
353	        help="Per-error-type γ_e values: action=0.85,verification=0.92,planning=0.97",
354	    )
355	    args = parser.parse_args()
356	
357	    logging.basicConfig(level=logging.INFO, format="%(name)s %(levelname)s %(message)s")
358	
359	    gamma_map = parse_gamma_arg(args.gamma)
360	    logger.info("γ_e map: %s", gamma_map)
361	
362	    expert_index = load_expert_index(args.expert)
363	    classified = load_classified(args.classified)
364	
365	    traj_index = None
366	    if args.trajectory_dir:
367	        traj_index = load_trajectories_from_dir(args.trajectory_dir)
368	
369	    out = Path(args.output)
370	    out.parent.mkdir(parents=True, exist_ok=True)
371	
372	    pairs = []
373	    skipped: Counter = Counter()
374	
375	    for rec in classified:
376	        if rec.get("error_type") in ("unknown", None):
377	            skipped["unknown_error_type"] += 1
378	            continue
379	
380	        key = normalize_game_file(rec.get("game_file", ""))
381	        expert = expert_index.get(key)
382	        if expert is None:
383	            skipped["no_expert_match"] += 1
384	            continue
385	
386	        if not rec.get("conversations"):
387	            if traj_index:
388	                traj = traj_index.get(key)
389	                if traj and traj.get("conversations"):
390	                    rec["conversations"] = traj["conversations"]
391	                else:
392	                    skipped["no_conversations"] += 1
393	                    continue
394	            else:
395	                skipped["no_conversations"] += 1
396	                continue
397	
398	        pair = build_pair(rec, expert, gamma_map)
399	        if pair is None:
400	            skipped["build_failed"] += 1
401	            continue
402	        pairs.append(pair)
403	
404	    with open(out, "w") as f:
405	        for pair in pairs:
406	            f.write(json.dumps(pair, ensure_ascii=False) + "\n")
407	
408	    logger.info("Built %d DPO pairs -> %s", len(pairs), out)
409	    if skipped:
410	        logger.info("Skipped: %s", dict(skipped))
411	
412	    # --- summary ---
413	    by_type: dict[str, list[int]] = defaultdict(list)
414	    div_steps: list[int] = []
415	    for p in pairs:
416	        by_type[p["error_type"]].append(p["correction_span"])
417	        div_steps.append(p["divergence_step"])
418	
419	    print(f"\n{'=' * 50}")
420	    print("DPO PAIR CONSTRUCTION SUMMARY")
421	    print(f"{'=' * 50}")
422	    print(f"Total pairs: {len(pairs)}")
423	    print(f"\n{'Type':<15} {'Count':>6} {'Avg CSpan':>10} {'γ_e':>6}")
424	    print("-" * 42)
425	    for et in ("action", "verification", "planning"):
426	        spans = by_type.get(et, [])
427	        ge = gamma_map.get(et, "-")
428	        if spans:
429	            avg = sum(spans) / len(spans)
430	            print(f"{et:<15} {len(spans):>6} {avg:>10.2f} {ge:>6}")
431	        else:
432	            print(f"{et:<15}      0          - {ge:>6}")
433	    if div_steps:
434	        print(f"\nDivergence step distribution:")
435	        print(f"  min={min(div_steps)}, max={max(div_steps)}, "
436	              f"mean={sum(div_steps)/len(div_steps):.1f}, "
437	              f"step1={sum(1 for d in div_steps if d == 1)}")
438	    if skipped:
439	        print(f"\nSkipped: {dict(skipped)}")
440	    print(f"{'=' * 50}")
441	
442	
443	if __name__ == "__main__":
444	    main()
445	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "34cea4af-b63e-4c89-913c-54e4037c89e9",
  "isSidechain": false,
  "promptId": "70d64043-cfe7-4c40-93f2-a3764a31ceea",
  "type": "user",
  "uuid": "eefa019e-89a6-495f-a2a8-495165e72351",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl/src/build_dpo_pairs.py",
      "content": "\"\"\"Build DPO preference pairs from classified failures and expert trajectories.\n\nFix [2026-05-12]: Use true divergence point instead of LLM-reported failure_step.\nOld logic used failure_step as split point, but expert and failure trajectories\nmay already differ before that step → prompt-chosen state inconsistency.\nNew logic compares action sequences step-by-step to find the real divergence.\n\nFor each classified failure:\n  1. Match expert trajectory by game_file\n  2. Compare actions step-by-step to find divergence point\n  3. Shared prefix = prompt, expert continuation = chosen, failure continuation = rejected\n\nInput:\n  - classified_errors.jsonl (error_type, failure_step, conversations)\n  - alfworld_sft.json (expert trajectories)\n  - (optional) trajectory_dir with failure JSONL files\n\nOutput per line:\n  {prompt, chosen, rejected, error_type, gamma_e, correction_span,\n   task_id, task_type, game_file, failure_step, divergence_step, metadata}\n\nUsage:\n  python src/build_dpo_pairs.py \\\n    --classified outputs/classify_compare_with_hint_20.jsonl \\\n    --expert data/alfworld_sft.json \\\n    --output data/dpo_pairs_v2.jsonl \\\n    --gamma action=0.85,verification=0.92,planning=0.97\n\nDependencies: (stdlib only)\n\"\"\"\n\nimport argparse\nimport json\nimport logging\nfrom collections import Counter, defaultdict\nfrom pathlib import Path\n\nlogger = logging.getLogger(\"build_dpo\")\n\nDEFAULT_GAMMA_MAP = {\n    \"action\": 0.85,\n    \"verification\": 0.92,\n    \"planning\": 0.97,\n}\n\n\ndef parse_gamma_arg(s: str) -> dict[str, float]:\n    \"\"\"Parse 'action=0.85,verification=0.92,planning=0.97' → dict.\"\"\"\n    gamma_map = dict(DEFAULT_GAMMA_MAP)\n    for item in s.split(\",\"):\n        k, v = item.strip().split(\"=\")\n        gamma_map[k.strip()] = float(v.strip())\n    return gamma_map\n\n\n# ---------------------------------------------------------------------------\n# Game file normalization\n# ---------------------------------------------------------------------------\n\ndef normalize_game_file(game_file: str) -> str:\n    \"\"\"Extract &lt;task_dir>/&lt;trial_dir> as matching key.\n\n    Expert:     data/json_2.1.1/train/&lt;task>/&lt;trial>\n    Trajectory: /root/.../json_2.1.1/train/&lt;task>/&lt;trial>/game.tw-pddl\n    \"\"\"\n    gf = game_file.rstrip(\"/\")\n    if gf.endswith(\"/game.tw-pddl\"):\n        gf = gf[: -len(\"/game.tw-pddl\")]\n    parts = gf.split(\"/\")\n    return \"/\".join(parts[-2:]) if len(parts) >= 2 else gf\n\n\n# ---------------------------------------------------------------------------\n# Message helpers\n# ---------------------------------------------------------------------------\n\ndef _role(msg: dict) -> str:\n    \"\"\"Get role from either format.\"\"\"\n    return msg.get(\"role\") or {\"human\": \"user\", \"gpt\": \"assistant\"}.get(msg.get(\"from\", \"\"), \"\")\n\n\ndef _content(msg: dict) -> str:\n    \"\"\"Get content from either format.\"\"\"\n    return msg.get(\"content\") or msg.get(\"value\", \"\")\n\n\ndef msg_to_standard(msg: dict) -> dict:\n    return {\"role\": _role(msg), \"content\": _content(msg)}\n\n\n# ---------------------------------------------------------------------------\n# Step extraction\n# ---------------------------------------------------------------------------\n\ndef find_task_start(conversations: list) -> int:\n    \"\"\"Index of first action step after the actual task description.\n\n    Handles both expert (no ICL) and trajectory (with ICL prefix) formats by\n    finding the LAST 'Your task is to:' user message, then the first action after it.\n    \"\"\"\n    task_desc_idx = -1\n    for i, msg in enumerate(conversations):\n        if _role(msg) in (\"user\", \"human\") and \"Your task is to:\" in _content(msg):\n            task_desc_idx = i\n\n    search_from = task_desc_idx + 1 if task_desc_idx >= 0 else 0\n    for i in range(search_from, len(conversations)):\n        if _role(conversations[i]) in (\"assistant\", \"gpt\") and \"Action:\" in _content(conversations[i]):\n            return i\n\n    return len(conversations)\n\n\ndef extract_steps(conversations: list, start_idx: int) -> list[tuple[dict, dict | None]]:\n    \"\"\"Extract (action_msg, obs_msg|None) pairs from start_idx onward.\"\"\"\n    steps = []\n    i = start_idx\n    while i < len(conversations):\n        if _role(conversations[i]) in (\"assistant\", \"gpt\"):\n            action = conversations[i]\n            obs = None\n            if i + 1 < len(conversations) and _role(conversations[i + 1]) in (\"user\", \"human\"):\n                obs = conversations[i + 1]\n                i += 2\n            else:\n                i += 1\n            steps.append((action, obs))\n        else:\n            i += 1\n    return steps\n\n\ndef count_expert_action_steps(expert: dict) -> int:\n    return sum(\n        1\n        for m in expert[\"conversations\"]\n        if m[\"from\"] == \"gpt\" and \"Action:\" in m.get(\"value\", \"\")\n    )\n\n\n# ---------------------------------------------------------------------------\n# Action comparison\n# ---------------------------------------------------------------------------\n\ndef extract_action_text(content: str) -> str:\n    \"\"\"Extract normalized 'Action: ...' line from a step message.\n\n    ALFWorld actions follow \"Thought: ...\\\\nAction: &lt;action>\". We extract\n    the action part and normalize whitespace + case for robust comparison.\n    \"\"\"\n    for line in content.split(\"\\n\"):\n        stripped = line.strip()\n        if stripped.lower().startswith(\"action:\"):\n            return \" \".join(stripped[len(\"action:\"):].split()).lower()\n    return \" \".join(content.split()).lower()\n\n\ndef find_divergence_point(\n    expert_steps: list[tuple[dict, dict | None]],\n    fail_steps: list[tuple[dict, dict | None]],\n) -> int:\n    \"\"\"Find the first step where expert and failure trajectories take different actions.\n\n    Compares normalized action strings step-by-step. In ALFWorld, same game_file\n    + same actions → same observations, so action match guarantees state match.\n\n    Args:\n        expert_steps: List of (action_msg, obs_msg|None) from expert trajectory.\n        fail_steps: List of (action_msg, obs_msg|None) from failure trajectory.\n\n    Returns:\n        0-based index of the first differing step. If one is a prefix of the\n        other, returns the shorter length (no shared step beyond that).\n    \"\"\"\n    min_len = min(len(expert_steps), len(fail_steps))\n    for i in range(min_len):\n        expert_action = extract_action_text(_content(expert_steps[i][0]))\n        fail_action = extract_action_text(_content(fail_steps[i][0]))\n        if expert_action != fail_action:\n            return i\n    return min_len\n\n\n# ---------------------------------------------------------------------------\n# Pair construction\n# ---------------------------------------------------------------------------\n\ndef build_pair(\n    rec: dict,\n    expert: dict,\n    gamma_map: dict[str, float] | None = None,\n) -> dict | None:\n    \"\"\"Build one DPO pair using true divergence point between expert and failure.\"\"\"\n    if gamma_map is None:\n        gamma_map = DEFAULT_GAMMA_MAP\n\n    fail_convs = rec[\"conversations\"]\n    expert_convs = expert[\"conversations\"]\n\n    fail_start = find_task_start(fail_convs)\n    expert_start = find_task_start(expert_convs)\n\n    fail_steps = extract_steps(fail_convs, fail_start)\n    expert_steps = extract_steps(expert_convs, expert_start)\n\n    if not fail_steps or not expert_steps:\n        return None\n\n    divergence = find_divergence_point(expert_steps, fail_steps)\n\n    if divergence >= len(expert_steps) or divergence >= len(fail_steps):\n        logger.debug(\n            \"task_id=%s: no divergence found (expert=%d, fail=%d steps, div=%d)\",\n            rec.get(\"task_id\"), len(expert_steps), len(fail_steps), divergence,\n        )\n        return None\n\n    correction_span = len(expert_steps) - divergence\n    error_type = rec.get(\"error_type\", \"unknown\")\n\n    # Prompt: ICL/header + shared prefix steps (identical actions + observations)\n    prompt_msgs = [msg_to_standard(m) for m in fail_convs[:fail_start]]\n    for i in range(divergence):\n        action, obs = expert_steps[i]\n        prompt_msgs.append(msg_to_standard(action))\n        if obs is not None:\n            prompt_msgs.append(msg_to_standard(obs))\n\n    # Chosen: expert continuation from divergence point\n    chosen_msgs = []\n    for i in range(divergence, len(expert_steps)):\n        action, obs = expert_steps[i]\n        chosen_msgs.append(msg_to_standard(action))\n        if obs is not None:\n            chosen_msgs.append(msg_to_standard(obs))\n\n    # Rejected: failure continuation from divergence point\n    rejected_msgs = []\n    for i in range(divergence, len(fail_steps)):\n        action, obs = fail_steps[i]\n        rejected_msgs.append(msg_to_standard(action))\n        if obs is not None:\n            rejected_msgs.append(msg_to_standard(obs))\n\n    if not chosen_msgs or not rejected_msgs:\n        return None\n\n    # Infer task_type from expert game_file (format: &lt;task_type>/&lt;trial_id>)\n    gf = expert.get(\"game_file\", \"\")\n    parts = gf.split(\"/\")\n    task_type = \"\"\n    for p in parts:\n        if p.startswith((\"pick_\", \"clean_\", \"heat_\", \"cool_\", \"put_\", \"examine_\", \"look_\")):\n            task_type = p\n            break\n    if not task_type:\n        task_type = rec.get(\"task_type\", \"\")\n\n    return {\n        \"prompt\": prompt_msgs,\n        \"chosen\": chosen_msgs,\n        \"rejected\": rejected_msgs,\n        \"error_type\": error_type,\n        \"gamma_e\": gamma_map.get(error_type, gamma_map.get(\"verification\", 0.92)),\n        \"correction_span\": correction_span,\n        \"task_id\": rec.get(\"task_id\"),\n        \"task_type\": task_type,\n        \"game_file\": rec.get(\"game_file\", \"\"),\n        \"failure_step\": rec.get(\"failure_step\", -1),\n        \"divergence_step\": divergence + 1,\n        \"metadata\": {\n            \"expert_steps\": len(expert_steps),\n            \"model_steps\": len(fail_steps),\n            \"divergence_step\": divergence,\n            \"classification_source\": rec.get(\"llm_original_type_source\", \"unknown\"),\n        },\n    }\n\n\n# ---------------------------------------------------------------------------\n# Data loading\n# ---------------------------------------------------------------------------\n\ndef load_expert_index(path: str) -> dict:\n    with open(path) as f:\n        experts = json.load(f)\n    index = {}\n    for ex in experts:\n        index[normalize_game_file(ex[\"game_file\"])] = ex\n    logger.info(\"Loaded %d experts\", len(experts))\n    return index\n\n\ndef load_classified(path: str) -> list:\n    records = []\n    with open(path) as f:\n        for line in f:\n            if line.strip():\n                records.append(json.loads(line))\n    logger.info(\"Loaded %d classified records\", len(records))\n    return records\n\n\ndef load_trajectories_from_dir(traj_dir: str) -> dict:\n    \"\"\"Index trajectory files by normalized game_file (fallback for missing conversations).\"\"\"\n    index = {}\n    for p in sorted(Path(traj_dir).glob(\"*.jsonl\")):\n        with open(p) as f:\n            for line in f:\n                if line.strip():\n                    traj = json.loads(line)\n                    index[normalize_game_file(traj.get(\"game_file\", \"\"))] = traj\n    logger.info(\"Loaded %d trajectories from %s\", len(index), traj_dir)\n    return index\n\n\n# ---------------------------------------------------------------------------\n# Main\n# ---------------------------------------------------------------------------\n\ndef main():\n    parser = argparse.ArgumentParser(\n        description=\"Build DPO pairs from classified failures + expert trajectories\"\n    )\n    parser.add_argument(\n        \"--classified\",\n        type=str,\n        default=\"data/classified/classified_errors.jsonl\",\n        help=\"Classified errors JSONL\",\n    )\n    parser.add_argument(\n        \"--expert\",\n        type=str,\n        default=\"eto_repo/data/alfworld_sft.json\",\n        help=\"Expert trajectories JSON\",\n    )\n    parser.add_argument(\n        \"--trajectory_dir\",\n        type=str,\n        default=None,\n        help=\"Failure trajectory JSONL dir (optional; uses classified conversations if omitted)\",\n    )\n    parser.add_argument(\n        \"--output\",\n        type=str,\n        default=\"data/dpo_pairs_v2.jsonl\",\n        help=\"Output JSONL path\",\n    )\n    parser.add_argument(\n        \"--gamma\",\n        type=str,\n        default=\"action=0.85,verification=0.92,planning=0.97\",\n        help=\"Per-error-type γ_e values: action=0.85,verification=0.92,planning=0.97\",\n    )\n    args = parser.parse_args()\n\n    logging.basicConfig(level=logging.INFO, format=\"%(name)s %(levelname)s %(message)s\")\n\n    gamma_map = parse_gamma_arg(args.gamma)\n    logger.info(\"γ_e map: %s\", gamma_map)\n\n    expert_index = load_expert_index(args.expert)\n    classified = load_classified(args.classified)\n\n    traj_index = None\n    if args.trajectory_dir:\n        traj_index = load_trajectories_from_dir(args.trajectory_dir)\n\n    out = Path(args.output)\n    out.parent.mkdir(parents=True, exist_ok=True)\n\n    pairs = []\n    skipped: Counter = Counter()\n\n    for rec in classified:\n        if rec.get(\"error_type\") in (\"unknown\", None):\n            skipped[\"unknown_error_type\"] += 1\n            continue\n\n        key = normalize_game_file(rec.get(\"game_file\", \"\"))\n        expert = expert_index.get(key)\n        if expert is None:\n            skipped[\"no_expert_match\"] += 1\n            continue\n\n        if not rec.get(\"conversations\"):\n            if traj_index:\n                traj = traj_index.get(key)\n                if traj and traj.get(\"conversations\"):\n                    rec[\"conversations\"] = traj[\"conversations\"]\n                else:\n                    skipped[\"no_conversations\"] += 1\n                    continue\n            else:\n                skipped[\"no_conversations\"] += 1\n                continue\n\n        pair = build_pair(rec, expert, gamma_map)\n        if pair is None:\n            skipped[\"build_failed\"] += 1\n            continue\n        pairs.append(pair)\n\n    with open(out, \"w\") as f:\n        for pair in pairs:\n            f.write(json.dumps(pair, ensure_ascii=False) + \"\\n\")\n\n    logger.info(\"Built %d DPO pairs -> %s\", len(pairs), out)\n    if skipped:\n        logger.info(\"Skipped: %s\", dict(skipped))\n\n    # --- summary ---\n    by_type: dict[str, list[int]] = defaultdict(list)\n    div_steps: list[int] = []\n    for p in pairs:\n        by_type[p[\"error_type\"]].append(p[\"correction_span\"])\n        div_steps.append(p[\"divergence_step\"])\n\n    print(f\"\\n{'=' * 50}\")\n    print(\"DPO PAIR CONSTRUCTION SUMMARY\")\n    print(f\"{'=' * 50}\")\n    print(f\"Total pairs: {len(pairs)}\")\n    print(f\"\\n{'Type':<15} {'Count':>6} {'Avg CSpan':>10} {'γ_e':>6}\")\n    print(\"-\" * 42)\n    for et in (\"action\", \"verification\", \"planning\"):\n        spans = by_type.get(et, [])\n        ge = gamma_map.get(et, \"-\")\n        if spans:\n            avg = sum(spans) / len(spans)\n            print(f\"{et:<15} {len(spans):>6} {avg:>10.2f} {ge:>6}\")\n        else:\n            print(f\"{et:<15}      0          - {ge:>6}\")\n    if div_steps:\n        print(f\"\\nDivergence step distribution:\")\n        print(f\"  min={min(div_steps)}, max={max(div_steps)}, \"\n              f\"mean={sum(div_steps)/len(div_steps):.1f}, \"\n              f\"step1={sum(1 for d in div_steps if d == 1)}\")\n    if skipped:\n        print(f\"\\nSkipped: {dict(skipped)}\")\n    print(f\"{'=' * 50}\")\n\n\nif __name__ == \"__main__\":\n    main()\n",
      "numLines": 445,
      "startLine": 1,
      "totalLines": 445
    }
  },
  "sourceToolAssistantUUID": "34cea4af-b63e-4c89-913c-54e4037c89e9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl",
  "sessionId": "2c8f695e-2726-4bc0-b978-178d488e8a4b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-13T04:47:35.105Z_

<details open><summary>🔧 Tool call — Read · `toolu_011LAsAHvdsQGiaDcbPdgiam`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl/artifacts/collect_trajectories_icl.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "eefa019e-89a6-495f-a2a8-495165e72351",
  "isSidechain": false,
  "requestId": "req_011CayxkYRwncTvFsq3RBFk8",
  "type": "assistant",
  "uuid": "4ec2bc25-5968-4ed7-ad1a-b8b489cea713",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl",
  "sessionId": "2c8f695e-2726-4bc0-b978-178d488e8a4b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FE5dEVvEYJknH4gNfet4rs",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12080,
      "cache_read_input_tokens": 11841,
      "output_tokens": 293,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12080,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 293,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12080,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12080
          },
          "type": "message"
        }
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

_source line 14 · 2026-05-13T04:47:35.115Z_

<details><summary>↩ Tool result · `toolu_011LAsAHvdsQGiaDcbPdgiam`</summary>

```text
1	"""ALFWorld trajectory collection with ICL few-shot from expert data.
2	
3	Uses Qwen3-14B-AWQ with task-type-aware ICL demonstrations sampled from
4	expert (SFT) trajectories. Supports dual-GPU collection via --part_num/--part_idx.
5	
6	Usage:
7	  CUDA_VISIBLE_DEVICES=0 python src/collect_trajectories_icl.py \
8	    --model_name /root/autodl-tmp/.hf_cache/Qwen/Qwen3-14B-AWQ \
9	    --gpu 0 --num_tasks 300 --seed 42 \
10	    --part_num 2 --part_idx 0 \
11	    --output_dir data/trajectories_v7_icl_cuda0
12	"""
13	
14	import os
15	import re
16	import json
17	import time
18	import random
19	import logging
20	import argparse
21	from pathlib import Path
22	from collections import defaultdict
23	
24	import yaml
25	import torch
26	import alfworld
27	from alfworld.agents.environment import get_environment
28	from transformers import AutoModelForCausalLM, AutoTokenizer
29	
30	logger = logging.getLogger("collect_traj_icl")
31	
32	PREFIXES = {
33	    "pick_and_place": "put",
34	    "pick_clean_then_place": "clean",
35	    "pick_heat_then_place": "heat",
36	    "pick_cool_then_place": "cool",
37	    "look_at_obj": "examine",
38	    "pick_two_obj": "puttwo",
39	}
40	
41	ALFWORLD_INSTRUCTION = (
42	    "Interact with a household to solve a task. Imagine you are an intelligent "
43	    "agent in a household environment and your target is to perform actions to "
44	    "complete the task goal. At the beginning of your interactions, you will be "
45	    "given the detailed description of the current environment and your goal to "
46	    "accomplish. \nFor each of your turn, you will be given the observation of "
47	    'the last turn. You should first think about the current condition and plan '
48	    'for your future actions, and then output your action in this turn. Your '
49	    'output must strictly follow this format:"Thought: your thoughts.\n'
50	    'Action: your next action".\n\n'
51	    "The available actions are:\n"
52	    "1. go to {recep}\n"
53	    "2. take {obj} from {recep}\n"
54	    "3. put {obj} in/on {recep}\n"
55	    "4. open {recep}\n"
56	    "5. close {recep}\n"
57	    "6. toggle {obj} {recep}\n"
58	    "7. clean {obj} with {recep}\n"
59	    "8. heat {obj} with {recep}\n"
60	    "9. cool {obj} with {recep}\n"
61	    "where {obj} and {recep} correspond to objects and receptacles.\n"
62	    "After your each turn, the environment will give you immediate feedback "
63	    'based on which you plan your next few steps. if the envrionment output '
64	    '"Nothing happened", that means the previous action is invalid and you '
65	    "should try more options.\n\n"
66	    "Your response should use the following format:\n\n"
67	    "Thought: &lt;your thoughts>\nAction: &lt;your next action>"
68	)
69	
70	
71	def get_task_type(game_file: str) -> str:
72	    for k in PREFIXES:
73	        if f"/{k}" in game_file:
74	            return k
75	    return "unknown"
76	
77	
78	def normalize_game_file(game_file: str) -> str:
79	    gf = game_file.rstrip("/")
80	    if gf.endswith("/game.tw-pddl"):
81	        gf = gf[: -len("/game.tw-pddl")]
82	    parts = gf.split("/")
83	    return "/".join(parts[-2:]) if len(parts) >= 2 else gf
84	
85	
86	def process_ob(ob: str) -> str:
87	    if ob.startswith("You arrive at loc "):
88	        ob = ob[ob.find(". ") + 2 :]
89	    return ob
90	
91	
92	def load_expert_data(expert_file: str, max_turns: int = 30) -> dict[str, list]:
93	    with open(expert_file) as f:
94	        sft_data = json.load(f)
95	
96	    by_type = defaultdict(list)
97	    for item in sft_data:
98	        tt = get_task_type(item["game_file"])
99	        convs = item["conversations"]
100	        if len(convs) > 2:
101	            interaction = convs[2:]
102	        else:
103	            continue
104	        n_turns = len(interaction)
105	        if n_turns <= max_turns:
106	            by_type[tt].append({
107	                "game_file": item["game_file"],
108	                "normalized_gf": normalize_game_file(item["game_file"]),
109	                "task_type": tt,
110	                "n_turns": n_turns,
111	                "interaction": interaction,
112	            })
113	
114	    for tt in by_type:
115	        by_type[tt].sort(key=lambda x: x["n_turns"])
116	
117	    total = sum(len(v) for v in by_type.values())
118	    logger.info("Loaded %d expert examples across %d task types", total, len(by_type))
119	    for tt, examples in sorted(by_type.items()):
120	        logger.info("  %s: %d examples", tt, len(examples))
121	
122	    return dict(by_type)
123	
124	
125	def sample_icl_examples(
126	    expert_by_type: dict[str, list],
127	    task_type: str,
128	    exclude_game_file: str,
129	    num_examples: int = 2,
130	    rng: random.Random = None,
131	) -> list[list[dict]]:
132	    if rng is None:
133	        rng = random.Random(42)
134	
135	    exclude_key = normalize_game_file(exclude_game_file)
136	
137	    same_type = [
138	        ex for ex in expert_by_type.get(task_type, [])
139	        if ex["normalized_gf"] != exclude_key
140	    ]
141	
142	    other_type = []
143	    for tt, examples in expert_by_type.items():
144	        if tt == task_type:
145	            continue
146	        for ex in examples:
147	            if ex["normalized_gf"] != exclude_key:
148	                other_type.append(ex)
149	    other_type.sort(key=lambda x: x["n_turns"])
150	
151	    selected = []
152	    if len(same_type) >= num_examples:
153	        selected = rng.sample(same_type, num_examples)
154	    else:
155	        selected = list(same_type)
156	        remaining = num_examples - len(selected)
157	        if remaining > 0 and other_type:
158	            supplement = other_type[:remaining]
159	            selected.extend(supplement)
160	
161	    icl_messages = []
162	    for ex in selected:
163	        msgs = []
164	        for turn in ex["interaction"]:
165	            role = "user" if turn["from"] == "human" else "assistant"
166	            msgs.append({"role": role, "content": turn["value"]})
167	        icl_messages.append(msgs)
168	
169	    return icl_messages
170	
171	
172	def load_alfworld_env(split: str, part_num: int = 1, part_idx: int = -1):
173	    alfworld_data = "/root/autodl-tmp/alfworld_data"
174	    os.environ["ALFWORLD_DATA"] = alfworld_data
175	
176	    with open(os.path.join(alfworld_data, "base_config.yaml")) as f:
177	        config = yaml.safe_load(f)
178	
179	    split_map = {
180	        "train": ("train", 3321),
181	        "dev": ("eval_in_distribution", 140),
182	        "test": ("eval_out_of_distribution", 134),
183	    }
184	    env_split, n_tasks = split_map[split]
185	
186	    EnvClass = get_environment(config["env"]["type"])
187	    env = EnvClass(config, train_eval=env_split)
188	    env = env.init_env(batch_size=1)
189	
190	    if part_num > 1:
191	        assert part_idx >= 0
192	        part_sizes = [n_tasks // part_num] * part_num
193	        part_sizes[-1] += n_tasks % part_num
194	        env.skip(sum(part_sizes[:part_idx]))
195	        n_tasks = part_sizes[part_idx]
196	
197	    def generator():
198	        for idx in range(n_tasks):
199	            obs, info = env.reset()
200	            obs_text = "\n".join(obs[0].split("\n\n")[1:])
201	            game_file = info["extra.gamefile"][0]
202	            yield {
203	                "task_id": idx,
204	                "game_file": game_file,
205	                "obs": obs_text,
206	                "env": env,
207	            }
208	
209	    return generator(), n_tasks
210	
211	
212	def load_model(model_name: str, gpu: int = 0):
213	    model = AutoModelForCausalLM.from_pretrained(
214	        model_name,
215	        device_map=f"cuda:{gpu}",
216	        trust_remote_code=True,
217	        torch_dtype=torch.float16,
218	    )
219	    tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
220	    model.eval()
221	    return model, tokenizer
222	
223	
224	def build_icl_messages(
225	    instruction: str, icl_examples: list[list[dict]], task_obs: str,
226	) -> list:
227	    messages = [
228	        {"role": "user", "content": instruction},
229	        {"role": "assistant", "content": "OK"},
230	    ]
231	    for example in icl_examples:
232	        for turn in example:
233	            messages.append({"role": turn["role"], "content": turn["content"]})
234	    messages.append({"role": "user", "content": task_obs})
235	    return messages
236	
237	
238	def generate_response(
239	    model, tokenizer, messages: list,
240	    temperature: float = 0.7, max_new_tokens: int = 256,
241	) -> str:
242	    try:
243	        text = tokenizer.apply_chat_template(
244	            messages, tokenize=False, add_generation_prompt=True,
245	            enable_thinking=False,
246	        )
247	    except TypeError:
248	        text = tokenizer.apply_chat_template(
249	            messages, tokenize=False, add_generation_prompt=True,
250	        )
251	
252	    inputs = tokenizer(text, return_tensors="pt").to(model.device)
253	
254	    with torch.no_grad():
255	        outputs = model.generate(
256	            **inputs,
257	            max_new_tokens=max_new_tokens,
258	            do_sample=temperature > 0,
259	            temperature=temperature if temperature > 0 else None,
260	            top_p=0.9 if temperature > 0 else None,
261	            pad_token_id=tokenizer.pad_token_id or tokenizer.eos_token_id,
262	        )
263	
264	    new_tokens = outputs[0][inputs["input_ids"].shape[1]:]
265	    response = tokenizer.decode(new_tokens, skip_special_tokens=True)
266	    response = re.sub(r"&lt;think>.*?&lt;/think>", "", response, flags=re.DOTALL).strip()
267	    return response
268	
269	
270	def parse_action(response: str) -> str:
271	    match = re.search(r"Action:\s*(.*)", response, re.DOTALL)
272	    if match:
273	        action = match.group(1).strip().split("\n")[0].strip()
274	        if action:
275	            return action
276	    return "look"
277	
278	
279	def collect_single_trajectory(
280	    task_info: dict,
281	    model, tokenizer,
282	    expert_by_type: dict,
283	    num_icl_examples: int = 2,
284	    temperature: float = 0.7,
285	    max_steps: int = 40,
286	    max_new_tokens: int = 256,
287	    rng: random.Random = None,
288	) -> dict:
289	    env = task_info["env"]
290	    task_obs = task_info["obs"]
291	    game_file = task_info["game_file"]
292	    task_id = task_info["task_id"]
293	    task_type = get_task_type(game_file)
294	
295	    icl_examples = sample_icl_examples(
296	        expert_by_type, task_type, game_file,
297	        num_examples=num_icl_examples, rng=rng,
298	    )
299	
300	    messages = build_icl_messages(ALFWORLD_INSTRUCTION, icl_examples, task_obs)
301	
302	    reward = False
303	    steps = 0
304	
305	    for _ in range(max_steps):
306	        response = generate_response(
307	            model, tokenizer, messages, temperature, max_new_tokens,
308	        )
309	        action = parse_action(response)
310	        messages.append({"role": "assistant", "content": response})
311	
312	        try:
313	            observation, env_reward, env_done, info = env.step([action])
314	            observation = process_ob(observation[0])
315	            reward = info["won"][0]
316	            done = env_done[0]
317	        except Exception as e:
318	            logger.warning("Task %d env.step error: %s", task_id, e)
319	            observation = "Invalid action."
320	            reward = False
321	            done = False
322	
323	        steps += 1
324	        messages.append({"role": "user", "content": f"Observation: {observation}"})
325	
326	        if done or reward:
327	            break
328	
329	    return {
330	        "task_id": task_id,
331	        "task_type": task_type,
332	        "game_file": game_file,
333	        "reward": bool(reward),
334	        "steps": steps,
335	        "conversations": messages,
336	    }
337	
338	
339	def main():
340	    parser = argparse.ArgumentParser("Collect ALFWorld trajectories with ICL few-shot")
341	    parser.add_argument("--model_name", type=str,
342	                        default="/root/autodl-tmp/.hf_cache/Qwen/Qwen3-14B-AWQ")
343	    parser.add_argument("--expert_file", type=str,
344	                        default="data/alfworld_sft.json")
345	    parser.add_argument("--output_dir", type=str, default="data/trajectories")
346	    parser.add_argument("--split", type=str, default="train",
347	                        choices=["train", "dev", "test"])
348	    parser.add_argument("--temperature", type=float, default=0.7)
349	    parser.add_argument("--max_steps", type=int, default=40)
350	    parser.add_argument("--max_new_tokens", type=int, default=256)
351	    parser.add_argument("--gpu", type=int, default=0)
352	    parser.add_argument("--num_tasks", type=int, default=-1, help="-1 = all tasks")
353	    parser.add_argument("--num_icl_examples", type=int, default=2)
354	    parser.add_argument("--part_num", type=int, default=1)
355	    parser.add_argument("--part_idx", type=int, default=-1)
356	    parser.add_argument("--seed", type=int, default=42)
357	    parser.add_argument("--dry_run", action="store_true",
358	                        help="Validate pipeline with 2 tasks then exit")
359	    args = parser.parse_args()
360	
361	    logging.basicConfig(
362	        level=logging.INFO,
363	        format="%(asctime)s %(levelname)s %(message)s",
364	    )
365	
366	    rng = random.Random(args.seed)
367	    torch.manual_seed(args.seed)
368	
369	    logger.info("Loading expert data from %s...", args.expert_file)
370	    expert_by_type = load_expert_data(args.expert_file)
371	
372	    logger.info("Loading model: %s", args.model_name)
373	    model, tokenizer = load_model(args.model_name, args.gpu)
374	
375	    logger.info("Loading ALFWorld %s environment...", args.split)
376	    task_gen, n_tasks = load_alfworld_env(args.split, args.part_num, args.part_idx)
377	
378	    if args.dry_run:
379	        n_tasks = min(2, n_tasks)
380	        logger.info("DRY RUN: collecting %d tasks only", n_tasks)
381	    elif args.num_tasks > 0:
382	        n_tasks = min(n_tasks, args.num_tasks)
383	
384	    output_dir = Path(args.output_dir)
385	    output_dir.mkdir(parents=True, exist_ok=True)
386	    suffix = f"_part{args.part_idx}" if args.part_num > 1 else ""
387	    output_file = output_dir / f"{args.split}{suffix}.jsonl"
388	
389	    logger.info("Collecting %d trajectories -> %s", n_tasks, output_file)
390	    logger.info("ICL examples per task: %d", args.num_icl_examples)
391	
392	    success_count = 0
393	    total_count = 0
394	
395	    with open(output_file, "w") as f:
396	        for i, task_info in enumerate(task_gen):
397	            if i >= n_tasks:
398	                break
399	
400	            t0 = time.time()
401	            traj = collect_single_trajectory(
402	                task_info, model, tokenizer,
403	                expert_by_type,
404	                num_icl_examples=args.num_icl_examples,
405	                temperature=args.temperature,
406	                max_steps=args.max_steps,
407	                max_new_tokens=args.max_new_tokens,
408	                rng=rng,
409	            )
410	            elapsed = time.time() - t0
411	
412	            total_count += 1
413	            if traj["reward"]:
414	                success_count += 1
415	
416	            f.write(json.dumps(traj, ensure_ascii=False) + "\n")
417	            f.flush()
418	
419	            logger.info(
420	                "[%d/%d] task=%d type=%s reward=%s steps=%d time=%.1fs sr=%d/%d",
421	                total_count, n_tasks, traj["task_id"],
422	                traj["task_type"], traj["reward"],
423	                traj["steps"], elapsed,
424	                success_count, total_count,
425	            )
426	
427	    logger.info(
428	        "Done. %d/%d succeeded (%.1f%%)",
429	        success_count, total_count,
430	        success_count / max(total_count, 1) * 100,
431	    )
432	
433	
434	if __name__ == "__main__":
435	    main()
436	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4ec2bc25-5968-4ed7-ad1a-b8b489cea713",
  "isSidechain": false,
  "promptId": "70d64043-cfe7-4c40-93f2-a3764a31ceea",
  "type": "user",
  "uuid": "46301ca3-a77d-430f-a791-938c302b3f5a",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl/artifacts/collect_trajectories_icl.py",
      "content": "\"\"\"ALFWorld trajectory collection with ICL few-shot from expert data.\n\nUses Qwen3-14B-AWQ with task-type-aware ICL demonstrations sampled from\nexpert (SFT) trajectories. Supports dual-GPU collection via --part_num/--part_idx.\n\nUsage:\n  CUDA_VISIBLE_DEVICES=0 python src/collect_trajectories_icl.py \\\n    --model_name /root/autodl-tmp/.hf_cache/Qwen/Qwen3-14B-AWQ \\\n    --gpu 0 --num_tasks 300 --seed 42 \\\n    --part_num 2 --part_idx 0 \\\n    --output_dir data/trajectories_v7_icl_cuda0\n\"\"\"\n\nimport os\nimport re\nimport json\nimport time\nimport random\nimport logging\nimport argparse\nfrom pathlib import Path\nfrom collections import defaultdict\n\nimport yaml\nimport torch\nimport alfworld\nfrom alfworld.agents.environment import get_environment\nfrom transformers import AutoModelForCausalLM, AutoTokenizer\n\nlogger = logging.getLogger(\"collect_traj_icl\")\n\nPREFIXES = {\n    \"pick_and_place\": \"put\",\n    \"pick_clean_then_place\": \"clean\",\n    \"pick_heat_then_place\": \"heat\",\n    \"pick_cool_then_place\": \"cool\",\n    \"look_at_obj\": \"examine\",\n    \"pick_two_obj\": \"puttwo\",\n}\n\nALFWORLD_INSTRUCTION = (\n    \"Interact with a household to solve a task. Imagine you are an intelligent \"\n    \"agent in a household environment and your target is to perform actions to \"\n    \"complete the task goal. At the beginning of your interactions, you will be \"\n    \"given the detailed description of the current environment and your goal to \"\n    \"accomplish. \\nFor each of your turn, you will be given the observation of \"\n    'the last turn. You should first think about the current condition and plan '\n    'for your future actions, and then output your action in this turn. Your '\n    'output must strictly follow this format:\"Thought: your thoughts.\\n'\n    'Action: your next action\".\\n\\n'\n    \"The available actions are:\\n\"\n    \"1. go to {recep}\\n\"\n    \"2. take {obj} from {recep}\\n\"\n    \"3. put {obj} in/on {recep}\\n\"\n    \"4. open {recep}\\n\"\n    \"5. close {recep}\\n\"\n    \"6. toggle {obj} {recep}\\n\"\n    \"7. clean {obj} with {recep}\\n\"\n    \"8. heat {obj} with {recep}\\n\"\n    \"9. cool {obj} with {recep}\\n\"\n    \"where {obj} and {recep} correspond to objects and receptacles.\\n\"\n    \"After your each turn, the environment will give you immediate feedback \"\n    'based on which you plan your next few steps. if the envrionment output '\n    '\"Nothing happened\", that means the previous action is invalid and you '\n    \"should try more options.\\n\\n\"\n    \"Your response should use the following format:\\n\\n\"\n    \"Thought: &lt;your thoughts>\\nAction: &lt;your next action>\"\n)\n\n\ndef get_task_type(game_file: str) -> str:\n    for k in PREFIXES:\n        if f\"/{k}\" in game_file:\n            return k\n    return \"unknown\"\n\n\ndef normalize_game_file(game_file: str) -> str:\n    gf = game_file.rstrip(\"/\")\n    if gf.endswith(\"/game.tw-pddl\"):\n        gf = gf[: -len(\"/game.tw-pddl\")]\n    parts = gf.split(\"/\")\n    return \"/\".join(parts[-2:]) if len(parts) >= 2 else gf\n\n\ndef process_ob(ob: str) -> str:\n    if ob.startswith(\"You arrive at loc \"):\n        ob = ob[ob.find(\". \") + 2 :]\n    return ob\n\n\ndef load_expert_data(expert_file: str, max_turns: int = 30) -> dict[str, list]:\n    with open(expert_file) as f:\n        sft_data = json.load(f)\n\n    by_type = defaultdict(list)\n    for item in sft_data:\n        tt = get_task_type(item[\"game_file\"])\n        convs = item[\"conversations\"]\n        if len(convs) > 2:\n            interaction = convs[2:]\n        else:\n            continue\n        n_turns = len(interaction)\n        if n_turns <= max_turns:\n            by_type[tt].append({\n                \"game_file\": item[\"game_file\"],\n                \"normalized_gf\": normalize_game_file(item[\"game_file\"]),\n                \"task_type\": tt,\n                \"n_turns\": n_turns,\n                \"interaction\": interaction,\n            })\n\n    for tt in by_type:\n        by_type[tt].sort(key=lambda x: x[\"n_turns\"])\n\n    total = sum(len(v) for v in by_type.values())\n    logger.info(\"Loaded %d expert examples across %d task types\", total, len(by_type))\n    for tt, examples in sorted(by_type.items()):\n        logger.info(\"  %s: %d examples\", tt, len(examples))\n\n    return dict(by_type)\n\n\ndef sample_icl_examples(\n    expert_by_type: dict[str, list],\n    task_type: str,\n    exclude_game_file: str,\n    num_examples: int = 2,\n    rng: random.Random = None,\n) -> list[list[dict]]:\n    if rng is None:\n        rng = random.Random(42)\n\n    exclude_key = normalize_game_file(exclude_game_file)\n\n    same_type = [\n        ex for ex in expert_by_type.get(task_type, [])\n        if ex[\"normalized_gf\"] != exclude_key\n    ]\n\n    other_type = []\n    for tt, examples in expert_by_type.items():\n        if tt == task_type:\n            continue\n        for ex in examples:\n            if ex[\"normalized_gf\"] != exclude_key:\n                other_type.append(ex)\n    other_type.sort(key=lambda x: x[\"n_turns\"])\n\n    selected = []\n    if len(same_type) >= num_examples:\n        selected = rng.sample(same_type, num_examples)\n    else:\n        selected = list(same_type)\n        remaining = num_examples - len(selected)\n        if remaining > 0 and other_type:\n            supplement = other_type[:remaining]\n            selected.extend(supplement)\n\n    icl_messages = []\n    for ex in selected:\n        msgs = []\n        for turn in ex[\"interaction\"]:\n            role = \"user\" if turn[\"from\"] == \"human\" else \"assistant\"\n            msgs.append({\"role\": role, \"content\": turn[\"value\"]})\n        icl_messages.append(msgs)\n\n    return icl_messages\n\n\ndef load_alfworld_env(split: str, part_num: int = 1, part_idx: int = -1):\n    alfworld_data = \"/root/autodl-tmp/alfworld_data\"\n    os.environ[\"ALFWORLD_DATA\"] = alfworld_data\n\n    with open(os.path.join(alfworld_data, \"base_config.yaml\")) as f:\n        config = yaml.safe_load(f)\n\n    split_map = {\n        \"train\": (\"train\", 3321),\n        \"dev\": (\"eval_in_distribution\", 140),\n        \"test\": (\"eval_out_of_distribution\", 134),\n    }\n    env_split, n_tasks = split_map[split]\n\n    EnvClass = get_environment(config[\"env\"][\"type\"])\n    env = EnvClass(config, train_eval=env_split)\n    env = env.init_env(batch_size=1)\n\n    if part_num > 1:\n        assert part_idx >= 0\n        part_sizes = [n_tasks // part_num] * part_num\n        part_sizes[-1] += n_tasks % part_num\n        env.skip(sum(part_sizes[:part_idx]))\n        n_tasks = part_sizes[part_idx]\n\n    def generator():\n        for idx in range(n_tasks):\n            obs, info = env.reset()\n            obs_text = \"\\n\".join(obs[0].split(\"\\n\\n\")[1:])\n            game_file = info[\"extra.gamefile\"][0]\n            yield {\n                \"task_id\": idx,\n                \"game_file\": game_file,\n                \"obs\": obs_text,\n                \"env\": env,\n            }\n\n    return generator(), n_tasks\n\n\ndef load_model(model_name: str, gpu: int = 0):\n    model = AutoModelForCausalLM.from_pretrained(\n        model_name,\n        device_map=f\"cuda:{gpu}\",\n        trust_remote_code=True,\n        torch_dtype=torch.float16,\n    )\n    tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)\n    model.eval()\n    return model, tokenizer\n\n\ndef build_icl_messages(\n    instruction: str, icl_examples: list[list[dict]], task_obs: str,\n) -> list:\n    messages = [\n        {\"role\": \"user\", \"content\": instruction},\n        {\"role\": \"assistant\", \"content\": \"OK\"},\n    ]\n    for example in icl_examples:\n        for turn in example:\n            messages.append({\"role\": turn[\"role\"], \"content\": turn[\"content\"]})\n    messages.append({\"role\": \"user\", \"content\": task_obs})\n    return messages\n\n\ndef generate_response(\n    model, tokenizer, messages: list,\n    temperature: float = 0.7, max_new_tokens: int = 256,\n) -> str:\n    try:\n        text = tokenizer.apply_chat_template(\n            messages, tokenize=False, add_generation_prompt=True,\n            enable_thinking=False,\n        )\n    except TypeError:\n        text = tokenizer.apply_chat_template(\n            messages, tokenize=False, add_generation_prompt=True,\n        )\n\n    inputs = tokenizer(text, return_tensors=\"pt\").to(model.device)\n\n    with torch.no_grad():\n        outputs = model.generate(\n            **inputs,\n            max_new_tokens=max_new_tokens,\n            do_sample=temperature > 0,\n            temperature=temperature if temperature > 0 else None,\n            top_p=0.9 if temperature > 0 else None,\n            pad_token_id=tokenizer.pad_token_id or tokenizer.eos_token_id,\n        )\n\n    new_tokens = outputs[0][inputs[\"input_ids\"].shape[1]:]\n    response = tokenizer.decode(new_tokens, skip_special_tokens=True)\n    response = re.sub(r\"&lt;think>.*?&lt;/think>\", \"\", response, flags=re.DOTALL).strip()\n    return response\n\n\ndef parse_action(response: str) -> str:\n    match = re.search(r\"Action:\\s*(.*)\", response, re.DOTALL)\n    if match:\n        action = match.group(1).strip().split(\"\\n\")[0].strip()\n        if action:\n            return action\n    return \"look\"\n\n\ndef collect_single_trajectory(\n    task_info: dict,\n    model, tokenizer,\n    expert_by_type: dict,\n    num_icl_examples: int = 2,\n    temperature: float = 0.7,\n    max_steps: int = 40,\n    max_new_tokens: int = 256,\n    rng: random.Random = None,\n) -> dict:\n    env = task_info[\"env\"]\n    task_obs = task_info[\"obs\"]\n    game_file = task_info[\"game_file\"]\n    task_id = task_info[\"task_id\"]\n    task_type = get_task_type(game_file)\n\n    icl_examples = sample_icl_examples(\n        expert_by_type, task_type, game_file,\n        num_examples=num_icl_examples, rng=rng,\n    )\n\n    messages = build_icl_messages(ALFWORLD_INSTRUCTION, icl_examples, task_obs)\n\n    reward = False\n    steps = 0\n\n    for _ in range(max_steps):\n        response = generate_response(\n            model, tokenizer, messages, temperature, max_new_tokens,\n        )\n        action = parse_action(response)\n        messages.append({\"role\": \"assistant\", \"content\": response})\n\n        try:\n            observation, env_reward, env_done, info = env.step([action])\n            observation = process_ob(observation[0])\n            reward = info[\"won\"][0]\n            done = env_done[0]\n        except Exception as e:\n            logger.warning(\"Task %d env.step error: %s\", task_id, e)\n            observation = \"Invalid action.\"\n            reward = False\n            done = False\n\n        steps += 1\n        messages.append({\"role\": \"user\", \"content\": f\"Observation: {observation}\"})\n\n        if done or reward:\n            break\n\n    return {\n        \"task_id\": task_id,\n        \"task_type\": task_type,\n        \"game_file\": game_file,\n        \"reward\": bool(reward),\n        \"steps\": steps,\n        \"conversations\": messages,\n    }\n\n\ndef main():\n    parser = argparse.ArgumentParser(\"Collect ALFWorld trajectories with ICL few-shot\")\n    parser.add_argument(\"--model_name\", type=str,\n                        default=\"/root/autodl-tmp/.hf_cache/Qwen/Qwen3-14B-AWQ\")\n    parser.add_argument(\"--expert_file\", type=str,\n                        default=\"data/alfworld_sft.json\")\n    parser.add_argument(\"--output_dir\", type=str, default=\"data/trajectories\")\n    parser.add_argument(\"--split\", type=str, default=\"train\",\n                        choices=[\"train\", \"dev\", \"test\"])\n    parser.add_argument(\"--temperature\", type=float, default=0.7)\n    parser.add_argument(\"--max_steps\", type=int, default=40)\n    parser.add_argument(\"--max_new_tokens\", type=int, default=256)\n    parser.add_argument(\"--gpu\", type=int, default=0)\n    parser.add_argument(\"--num_tasks\", type=int, default=-1, help=\"-1 = all tasks\")\n    parser.add_argument(\"--num_icl_examples\", type=int, default=2)\n    parser.add_argument(\"--part_num\", type=int, default=1)\n    parser.add_argument(\"--part_idx\", type=int, default=-1)\n    parser.add_argument(\"--seed\", type=int, default=42)\n    parser.add_argument(\"--dry_run\", action=\"store_true\",\n                        help=\"Validate pipeline with 2 tasks then exit\")\n    args = parser.parse_args()\n\n    logging.basicConfig(\n        level=logging.INFO,\n        format=\"%(asctime)s %(levelname)s %(message)s\",\n    )\n\n    rng = random.Random(args.seed)\n    torch.manual_seed(args.seed)\n\n    logger.info(\"Loading expert data from %s...\", args.expert_file)\n    expert_by_type = load_expert_data(args.expert_file)\n\n    logger.info(\"Loading model: %s\", args.model_name)\n    model, tokenizer = load_model(args.model_name, args.gpu)\n\n    logger.info(\"Loading ALFWorld %s environment...\", args.split)\n    task_gen, n_tasks = load_alfworld_env(args.split, args.part_num, args.part_idx)\n\n    if args.dry_run:\n        n_tasks = min(2, n_tasks)\n        logger.info(\"DRY RUN: collecting %d tasks only\", n_tasks)\n    elif args.num_tasks > 0:\n        n_tasks = min(n_tasks, args.num_tasks)\n\n    output_dir = Path(args.output_dir)\n    output_dir.mkdir(parents=True, exist_ok=True)\n    suffix = f\"_part{args.part_idx}\" if args.part_num > 1 else \"\"\n    output_file = output_dir / f\"{args.split}{suffix}.jsonl\"\n\n    logger.info(\"Collecting %d trajectories -> %s\", n_tasks, output_file)\n    logger.info(\"ICL examples per task: %d\", args.num_icl_examples)\n\n    success_count = 0\n    total_count = 0\n\n    with open(output_file, \"w\") as f:\n        for i, task_info in enumerate(task_gen):\n            if i >= n_tasks:\n                break\n\n            t0 = time.time()\n            traj = collect_single_trajectory(\n                task_info, model, tokenizer,\n                expert_by_type,\n                num_icl_examples=args.num_icl_examples,\n                temperature=args.temperature,\n                max_steps=args.max_steps,\n                max_new_tokens=args.max_new_tokens,\n                rng=rng,\n            )\n            elapsed = time.time() - t0\n\n            total_count += 1\n            if traj[\"reward\"]:\n                success_count += 1\n\n            f.write(json.dumps(traj, ensure_ascii=False) + \"\\n\")\n            f.flush()\n\n            logger.info(\n                \"[%d/%d] task=%d type=%s reward=%s steps=%d time=%.1fs sr=%d/%d\",\n                total_count, n_tasks, traj[\"task_id\"],\n                traj[\"task_type\"], traj[\"reward\"],\n                traj[\"steps\"], elapsed,\n                success_count, total_count,\n            )\n\n    logger.info(\n        \"Done. %d/%d succeeded (%.1f%%)\",\n        success_count, total_count,\n        success_count / max(total_count, 1) * 100,\n    )\n\n\nif __name__ == \"__main__\":\n    main()\n",
      "numLines": 436,
      "startLine": 1,
      "totalLines": 436
    }
  },
  "sourceToolAssistantUUID": "4ec2bc25-5968-4ed7-ad1a-b8b489cea713",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl",
  "sessionId": "2c8f695e-2726-4bc0-b978-178d488e8a4b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-13T04:47:35.261Z_

<details open><summary>🔧 Tool call — Read · `toolu_01MKBMiWyANdgaHKTigx73rb`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl/src/etadn_discount.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "46301ca3-a77d-430f-a791-938c302b3f5a",
  "isSidechain": false,
  "requestId": "req_011CayxkYRwncTvFsq3RBFk8",
  "type": "assistant",
  "uuid": "294354ec-aa48-4a10-8c69-2a2bfb80fbb3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl",
  "sessionId": "2c8f695e-2726-4bc0-b978-178d488e8a4b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FE5dEVvEYJknH4gNfet4rs",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12080,
      "cache_read_input_tokens": 11841,
      "output_tokens": 293,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12080,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 293,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12080,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12080
          },
          "type": "message"
        }
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
  "leafUuid": "5f2b94c6-eb62-4738-b496-b7444b8a07d1",
  "sessionId": "2c8f695e-2726-4bc0-b978-178d488e8a4b"
}
```

---

### Runtime record

_source line 17_

```json
{
  "type": "ai-title",
  "aiTitle": "Write failure mode analysis script for paper",
  "sessionId": "2c8f695e-2726-4bc0-b978-178d488e8a4b"
}
```

---

### Assistant

_source line 18 · 2026-05-13T04:48:05.944Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a good understanding of:

1. **Trajectory JSONL format** (from `collect_trajectories_icl.py`):
   - Each line: `{task_id, task_type, game_file, reward, steps, conversations}`
   - `conversations` is a list of `{role, content}` messages
   - `reward` = True/False for success/failure
   - `task_type` comes from `get_task_type()` using PREFIXES dict

2. **Expert format** (from `build_dpo_pairs.py`):
   - `alfworld_sft.json` is a JSON array
   - Each item: `{game_file, conversations}` where conversations use `{from: "human"/"gpt", value: ...}` format

3. **Divergence point calculation** (from `build_dpo_pairs.py`):
   - `find_task_start()` locates the first action step after "Your task is to:"
   - `extract_steps()` pulls (action_msg, obs_msg) pairs
   - `extract_action_text()` normalizes action strings
   - `find_divergence_point()` compares action sequences step by step

4. **γ(d) function** (from `etadn_discount.py`):
   - The `phi` function is being defined to calculate discount factors based on divergence distance.
   - I need to map the divergence position d to γ values, where γ_min=0.85 and γ_max=0.97, with d normalized as div_point / expert_length.
   - The mapping should treat early divergence as action errors (low γ) and late divergence as planning errors (high γ), though I'm reconsidering how the ETADN discount γ values actually relate to the divergence position d.

Looking back at what the task is actually asking for, it seems like I need to show a preview of what γ values each data point would receive under this mapping, displaying the distribution across the γ_min to γ_max range. _min + d * (γ_max - γ_min) = 0.85 + d * 0.12.

Now I need to write the actual script. The main steps are loading the failure trajectories from JSONL files (which might be split across multiple parts), loading the expert trajectories from JSON, matching them by game_file using the normalization function, computing where trajectories diverge, calculating the statistics, and outputting both JSON and Markdown results. I should also handle the fact that trajectory files could be named either `train.jsonl` or split into `train_part0.jsonl`, `train_part1.jsonl`, etc.

Writing the analysis script...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5f2b94c6-eb62-4738-b496-b7444b8a07d1",
  "isSidechain": false,
  "requestId": "req_011CayxkzFUHpA2VJphwmzFT",
  "type": "assistant",
  "uuid": "5df9e553-1faf-4d63-86e8-c064d2b89e84",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl",
  "sessionId": "2c8f695e-2726-4bc0-b978-178d488e8a4b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VHKi1Dgr66Y5seVTETJjZS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16189,
      "cache_read_input_tokens": 23921,
      "output_tokens": 8103,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 16189,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 8103,
          "cache_read_input_tokens": 23921,
          "cache_creation_input_tokens": 16189,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 16189
          },
          "type": "message"
        }
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

_source line 19 · 2026-05-13T04:48:05.946Z_

Now I have the full picture. Let me write the script.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5df9e553-1faf-4d63-86e8-c064d2b89e84",
  "isSidechain": false,
  "requestId": "req_011CayxkzFUHpA2VJphwmzFT",
  "type": "assistant",
  "uuid": "016c02fe-3950-4b7d-bcdb-ee49ba04f759",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl",
  "sessionId": "2c8f695e-2726-4bc0-b978-178d488e8a4b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VHKi1Dgr66Y5seVTETJjZS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16189,
      "cache_read_input_tokens": 23921,
      "output_tokens": 8103,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 16189,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 8103,
          "cache_read_input_tokens": 23921,
          "cache_creation_input_tokens": 16189,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 16189
          },
          "type": "message"
        }
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

_source line 20 · 2026-05-13T04:49:30.122Z_

<details open><summary>🔧 Tool call — Write · `toolu_01Hw9rrXwYJ3cux1EpR2kwUt`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl/src/analyze_failure_modes.py",
  "content": "\"\"\"Failure mode descriptive analysis for ETADN paper.\n\nAnalyzes divergence patterns between failure trajectories and expert trajectories.\nProduces structured JSON and Markdown report for paper's failure mode characterization.\n\nInput: v7 trajectory JSONL files + expert alfworld_sft.json\nOutput: failure_mode_summary.json + failure_mode_report.md\n\nUsage:\n  python src/analyze_failure_modes.py \\\n    --failure_dir data/trajectories_v7_icl \\\n    --expert_file data/alfworld_sft.json \\\n    --output_dir outputs/failure_analysis\n\"\"\"\n\nimport argparse\nimport json\nimport math\nimport statistics\nfrom collections import Counter, defaultdict\nfrom pathlib import Path\n\n\n# ---------------------------------------------------------------------------\n# Task type mapping\n# ---------------------------------------------------------------------------\n\nTASK_TYPE_FROM_PATH = {\n    \"pick_and_place\": \"pick_and_place\",\n    \"pick_clean_then_place\": \"clean\",\n    \"pick_heat_then_place\": \"heat\",\n    \"pick_cool_then_place\": \"cool\",\n    \"look_at_obj\": \"examine\",\n    \"pick_two_obj\": \"pick_two\",\n}\n\nCANONICAL_TASK_TYPES = [\"pick_and_place\", \"clean\", \"heat\", \"cool\", \"examine\", \"pick_two\"]\n\n\ndef get_task_type(game_file: str) -> str:\n    \"\"\"Infer canonical task type from game_file path.\"\"\"\n    for key, canonical in TASK_TYPE_FROM_PATH.items():\n        if f\"/{key}\" in game_file or game_file.startswith(key):\n            return canonical\n    return \"unknown\"\n\n\ndef normalize_game_file(game_file: str) -> str:\n    \"\"\"Extract &lt;task_dir>/&lt;trial_dir> as matching key.\"\"\"\n    gf = game_file.rstrip(\"/\")\n    if gf.endswith(\"/game.tw-pddl\"):\n        gf = gf[: -len(\"/game.tw-pddl\")]\n    parts = gf.split(\"/\")\n    return \"/\".join(parts[-2:]) if len(parts) >= 2 else gf\n\n\n# ---------------------------------------------------------------------------\n# Message helpers (handle both formats)\n# ---------------------------------------------------------------------------\n\ndef _role(msg: dict) -> str:\n    return msg.get(\"role\") or {\"human\": \"user\", \"gpt\": \"assistant\"}.get(msg.get(\"from\", \"\"), \"\")\n\n\ndef _content(msg: dict) -> str:\n    return msg.get(\"content\") or msg.get(\"value\", \"\")\n\n\ndef find_task_start(conversations: list) -> int:\n    \"\"\"Index of first action step after the last 'Your task is to:' message.\"\"\"\n    task_desc_idx = -1\n    for i, msg in enumerate(conversations):\n        if _role(msg) in (\"user\", \"human\") and \"Your task is to:\" in _content(msg):\n            task_desc_idx = i\n\n    search_from = task_desc_idx + 1 if task_desc_idx >= 0 else 0\n    for i in range(search_from, len(conversations)):\n        if _role(conversations[i]) in (\"assistant\", \"gpt\") and \"Action:\" in _content(conversations[i]):\n            return i\n    return len(conversations)\n\n\ndef extract_steps(conversations: list, start_idx: int) -> list[tuple[dict, dict | None]]:\n    \"\"\"Extract (action_msg, obs_msg|None) pairs from start_idx onward.\"\"\"\n    steps = []\n    i = start_idx\n    while i < len(conversations):\n        if _role(conversations[i]) in (\"assistant\", \"gpt\"):\n            action = conversations[i]\n            obs = None\n            if i + 1 < len(conversations) and _role(conversations[i + 1]) in (\"user\", \"human\"):\n                obs = conversations[i + 1]\n                i += 2\n            else:\n                i += 1\n            steps.append((action, obs))\n        else:\n            i += 1\n    return steps\n\n\ndef extract_action_text(content: str) -> str:\n    \"\"\"Extract and normalize 'Action: ...' from a step message.\"\"\"\n    for line in content.split(\"\\n\"):\n        stripped = line.strip()\n        if stripped.lower().startswith(\"action:\"):\n            return \" \".join(stripped[len(\"action:\"):].split()).lower()\n    return \" \".join(content.split()).lower()\n\n\n# ---------------------------------------------------------------------------\n# Divergence computation\n# ---------------------------------------------------------------------------\n\ndef find_divergence_point(expert_steps, fail_steps) -> int:\n    \"\"\"First step index where expert and failure take different actions.\"\"\"\n    min_len = min(len(expert_steps), len(fail_steps))\n    for i in range(min_len):\n        ea = extract_action_text(_content(expert_steps[i][0]))\n        fa = extract_action_text(_content(fail_steps[i][0]))\n        if ea != fa:\n            return i\n    return min_len\n\n\ndef compute_divergence(fail_traj: dict, expert: dict) -> dict | None:\n    \"\"\"Compute divergence metrics for a failure trajectory matched to an expert.\n\n    Returns dict with divergence_point, expert_length, d, correction_span,\n    or None if computation fails.\n    \"\"\"\n    fail_convs = fail_traj.get(\"conversations\", [])\n    expert_convs = expert.get(\"conversations\", [])\n    if not fail_convs or not expert_convs:\n        return None\n\n    fail_start = find_task_start(fail_convs)\n    expert_start = find_task_start(expert_convs)\n\n    fail_steps = extract_steps(fail_convs, fail_start)\n    expert_steps = extract_steps(expert_convs, expert_start)\n\n    if not fail_steps or not expert_steps:\n        return None\n\n    div_point = find_divergence_point(expert_steps, fail_steps)\n    expert_len = len(expert_steps)\n    d = div_point / expert_len if expert_len > 0 else 0.0\n    correction_span = expert_len - div_point\n\n    return {\n        \"divergence_point\": div_point,\n        \"expert_length\": expert_len,\n        \"failure_length\": len(fail_steps),\n        \"d\": d,\n        \"correction_span\": correction_span,\n    }\n\n\n# ---------------------------------------------------------------------------\n# γ(d) mapping\n# ---------------------------------------------------------------------------\n\ndef gamma_from_d(d: float, gamma_min: float = 0.85, gamma_max: float = 0.97) -> float:\n    \"\"\"Map divergence position d ∈ [0,1] to γ via linear interpolation.\n\n    Early divergence (d→0) → γ_min (action-error-like, concentrated credit).\n    Late divergence (d→1) → γ_max (planning-error-like, spread credit).\n    \"\"\"\n    return gamma_min + d * (gamma_max - gamma_min)\n\n\n# ---------------------------------------------------------------------------\n# Data loading\n# ---------------------------------------------------------------------------\n\ndef load_trajectories(failure_dir: str) -> list[dict]:\n    \"\"\"Load all trajectory JSONL files from a directory.\"\"\"\n    records = []\n    p = Path(failure_dir)\n    for jsonl_file in sorted(p.glob(\"*.jsonl\")):\n        with open(jsonl_file) as f:\n            for line in f:\n                if line.strip():\n                    records.append(json.loads(line))\n    return records\n\n\ndef load_expert_index(expert_file: str) -> dict[str, dict]:\n    \"\"\"Load expert trajectories indexed by normalized game_file.\"\"\"\n    with open(expert_file) as f:\n        experts = json.load(f)\n    return {normalize_game_file(ex[\"game_file\"]): ex for ex in experts}\n\n\n# ---------------------------------------------------------------------------\n# Analysis\n# ---------------------------------------------------------------------------\n\ndef analyze(trajectories: list[dict], expert_index: dict[str, dict],\n            gamma_min: float = 0.85, gamma_max: float = 0.97) -> dict:\n    \"\"\"Run all failure mode analyses. Returns structured results dict.\"\"\"\n\n    # -- 1. Basic statistics --\n    total = len(trajectories)\n    successes = [t for t in trajectories if t.get(\"reward\")]\n    failures = [t for t in trajectories if not t.get(\"reward\")]\n    n_success = len(successes)\n    n_failure = len(failures)\n    success_rate = n_success / total if total > 0 else 0.0\n\n    # Per-task-type success rate\n    type_total = Counter()\n    type_success = Counter()\n    for t in trajectories:\n        tt = t.get(\"task_type\") or get_task_type(t.get(\"game_file\", \"\"))\n        type_total[tt] += 1\n        if t.get(\"reward\"):\n            type_success[tt] += 1\n\n    per_type_sr = {}\n    for tt in CANONICAL_TASK_TYPES:\n        tot = type_total.get(tt, 0)\n        suc = type_success.get(tt, 0)\n        per_type_sr[tt] = {\n            \"total\": tot,\n            \"success\": suc,\n            \"failure\": tot - suc,\n            \"success_rate\": suc / tot if tot > 0 else None,\n        }\n\n    basic_stats = {\n        \"total_tasks\": total,\n        \"success\": n_success,\n        \"failure\": n_failure,\n        \"success_rate\": success_rate,\n        \"per_task_type\": per_type_sr,\n    }\n\n    # -- 4. Expert/Failure matching --\n    exact_match = 0\n    template_match = 0\n    unmatched = 0\n    matched_failures = []\n\n    for t in failures:\n        gf = t.get(\"game_file\", \"\")\n        key = normalize_game_file(gf)\n        expert = expert_index.get(key)\n\n        if expert is not None:\n            exact_match += 1\n            div_info = compute_divergence(t, expert)\n            if div_info is not None:\n                tt = t.get(\"task_type\") or get_task_type(gf)\n                matched_failures.append({\n                    \"task_type\": tt,\n                    \"game_file\": gf,\n                    **div_info,\n                })\n        else:\n            tt = t.get(\"task_type\") or get_task_type(gf)\n            found_template = False\n            for ek, ev in expert_index.items():\n                expert_tt = get_task_type(ev.get(\"game_file\", \"\"))\n                if expert_tt == tt:\n                    found_template = True\n                    break\n            if found_template:\n                template_match += 1\n            else:\n                unmatched += 1\n\n    match_stats = {\n        \"exact_match\": exact_match,\n        \"exact_match_rate\": exact_match / n_failure if n_failure > 0 else 0.0,\n        \"template_match_only\": template_match,\n        \"template_match_rate\": (exact_match + template_match) / n_failure if n_failure > 0 else 0.0,\n        \"unmatched\": unmatched,\n        \"divergence_computed\": len(matched_failures),\n    }\n\n    # -- 2. Divergence analysis --\n    d_values = [m[\"d\"] for m in matched_failures]\n    d_by_type = defaultdict(list)\n    for m in matched_failures:\n        d_by_type[m[\"task_type\"]].append(m[\"d\"])\n\n    bins = [(i / 10, (i + 1) / 10) for i in range(10)]\n    bin_labels = [f\"{lo:.1f}-{hi:.1f}\" for lo, hi in bins]\n    histogram = {label: 0 for label in bin_labels}\n    for d in d_values:\n        idx = min(int(d * 10), 9)\n        histogram[bin_labels[idx]] += 1\n\n    early = [d for d in d_values if d < 0.33]\n    mid = [d for d in d_values if 0.33 <= d < 0.67]\n    late = [d for d in d_values if d >= 0.67]\n\n    def _dist_stats(vals):\n        if not vals:\n            return None\n        return {\n            \"n\": len(vals),\n            \"mean\": statistics.mean(vals),\n            \"median\": statistics.median(vals),\n            \"std\": statistics.stdev(vals) if len(vals) > 1 else 0.0,\n            \"min\": min(vals),\n            \"max\": max(vals),\n            \"q1\": statistics.quantiles(vals, n=4)[0] if len(vals) >= 2 else vals[0],\n            \"q3\": statistics.quantiles(vals, n=4)[2] if len(vals) >= 2 else vals[0],\n        }\n\n    per_type_d = {}\n    for tt in CANONICAL_TASK_TYPES:\n        per_type_d[tt] = _dist_stats(d_by_type.get(tt, []))\n\n    divergence_analysis = {\n        \"overall\": _dist_stats(d_values),\n        \"histogram\": histogram,\n        \"temporal_groups\": {\n            \"early_d_lt_0.33\": {\"n\": len(early), \"mean_d\": statistics.mean(early) if early else None},\n            \"mid_0.33_le_d_lt_0.67\": {\"n\": len(mid), \"mean_d\": statistics.mean(mid) if mid else None},\n            \"late_d_ge_0.67\": {\"n\": len(late), \"mean_d\": statistics.mean(late) if late else None},\n        },\n        \"per_task_type\": per_type_d,\n    }\n\n    # -- 3. γ(d) mapping preview --\n    gamma_values = [gamma_from_d(d, gamma_min, gamma_max) for d in d_values]\n    gamma_analysis = {\n        \"gamma_min\": gamma_min,\n        \"gamma_max\": gamma_max,\n        \"distribution\": _dist_stats(gamma_values) if gamma_values else None,\n        \"temporal_group_gamma\": {\n            \"early\": statistics.mean([gamma_from_d(d, gamma_min, gamma_max) for d in early]) if early else None,\n            \"mid\": statistics.mean([gamma_from_d(d, gamma_min, gamma_max) for d in mid]) if mid else None,\n            \"late\": statistics.mean([gamma_from_d(d, gamma_min, gamma_max) for d in late]) if late else None,\n        },\n    }\n\n    # -- 5. Trajectory length analysis --\n    fail_lengths = [m[\"failure_length\"] for m in matched_failures]\n    expert_lengths = [m[\"expert_length\"] for m in matched_failures]\n    correction_spans = [m[\"correction_span\"] for m in matched_failures]\n\n    length_analysis = {\n        \"failure_trajectory_length\": _dist_stats(fail_lengths),\n        \"expert_trajectory_length\": _dist_stats(expert_lengths),\n        \"correction_span\": _dist_stats(correction_spans),\n    }\n\n    return {\n        \"basic_stats\": basic_stats,\n        \"divergence_analysis\": divergence_analysis,\n        \"gamma_mapping_preview\": gamma_analysis,\n        \"match_stats\": match_stats,\n        \"length_analysis\": length_analysis,\n    }\n\n\n# ---------------------------------------------------------------------------\n# Report generation\n# ---------------------------------------------------------------------------\n\ndef _fmt(val, decimals=3):\n    if val is None:\n        return \"-\"\n    if isinstance(val, float):\n        return f\"{val:.{decimals}f}\"\n    return str(val)\n\n\ndef generate_markdown(results: dict) -> str:\n    \"\"\"Generate Markdown report from analysis results.\"\"\"\n    lines = []\n    bs = results[\"basic_stats\"]\n    da = results[\"divergence_analysis\"]\n    gm = results[\"gamma_mapping_preview\"]\n    ms = results[\"match_stats\"]\n    la = results[\"length_analysis\"]\n\n    # -- Section 1 --\n    lines.append(\"# Failure Mode Analysis Report\\n\")\n    lines.append(\"## 1. Basic Statistics\\n\")\n    lines.append(f\"| Metric | Value |\")\n    lines.append(f\"|--------|-------|\")\n    lines.append(f\"| Total tasks | {bs['total_tasks']} |\")\n    lines.append(f\"| Success | {bs['success']} |\")\n    lines.append(f\"| Failure | {bs['failure']} |\")\n    lines.append(f\"| Success rate | {_fmt(bs['success_rate'])} |\")\n    lines.append(\"\")\n\n    lines.append(\"### Per-task-type Success Rate\\n\")\n    lines.append(\"| Task Type | Total | Success | Failure | Success Rate |\")\n    lines.append(\"|-----------|-------|---------|---------|--------------|\")\n    for tt in CANONICAL_TASK_TYPES:\n        info = bs[\"per_task_type\"].get(tt, {})\n        lines.append(\n            f\"| {tt} | {info.get('total', 0)} | {info.get('success', 0)} \"\n            f\"| {info.get('failure', 0)} | {_fmt(info.get('success_rate'))} |\"\n        )\n    lines.append(\"\")\n\n    # -- Section 2 --\n    lines.append(\"## 2. Divergence Analysis\\n\")\n    ov = da.get(\"overall\")\n    if ov:\n        lines.append(f\"Divergence position d = divergence_point / expert_length\\n\")\n        lines.append(\"| Statistic | Value |\")\n        lines.append(\"|-----------|-------|\")\n        for k in (\"n\", \"mean\", \"median\", \"std\", \"min\", \"max\", \"q1\", \"q3\"):\n            lines.append(f\"| {k} | {_fmt(ov[k])} |\")\n        lines.append(\"\")\n\n    lines.append(\"### d-value Histogram\\n\")\n    lines.append(\"| Bin | Count |\")\n    lines.append(\"|-----|-------|\")\n    for bin_label, count in da[\"histogram\"].items():\n        lines.append(f\"| {bin_label} | {count} |\")\n    lines.append(\"\")\n\n    lines.append(\"### Temporal Groups\\n\")\n    lines.append(\"| Group | n | Mean d |\")\n    lines.append(\"|-------|---|--------|\")\n    tg = da[\"temporal_groups\"]\n    for label, key in [(\"Early (d<0.33)\", \"early_d_lt_0.33\"),\n                        (\"Mid (0.33≤d<0.67)\", \"mid_0.33_le_d_lt_0.67\"),\n                        (\"Late (d≥0.67)\", \"late_d_ge_0.67\")]:\n        g = tg[key]\n        lines.append(f\"| {label} | {g['n']} | {_fmt(g.get('mean_d'))} |\")\n    lines.append(\"\")\n\n    lines.append(\"### Per-task-type d Distribution\\n\")\n    lines.append(\"| Task Type | n | Mean | Median | Std |\")\n    lines.append(\"|-----------|---|------|--------|-----|\")\n    for tt in CANONICAL_TASK_TYPES:\n        info = da[\"per_task_type\"].get(tt)\n        if info:\n            lines.append(\n                f\"| {tt} | {info['n']} | {_fmt(info['mean'])} \"\n                f\"| {_fmt(info['median'])} | {_fmt(info['std'])} |\"\n            )\n        else:\n            lines.append(f\"| {tt} | 0 | - | - | - |\")\n    lines.append(\"\")\n\n    # -- Section 3 --\n    lines.append(\"## 3. γ(d) Mapping Preview\\n\")\n    lines.append(f\"γ(d) = γ_min + d·(γ_max - γ_min), γ_min={gm['gamma_min']}, γ_max={gm['gamma_max']}\\n\")\n    gd = gm.get(\"distribution\")\n    if gd:\n        lines.append(\"| Statistic | γ value |\")\n        lines.append(\"|-----------|---------|\")\n        for k in (\"mean\", \"median\", \"std\", \"min\", \"max\"):\n            lines.append(f\"| {k} | {_fmt(gd[k], 4)} |\")\n        lines.append(\"\")\n\n    lines.append(\"### Mean γ by Temporal Group\\n\")\n    lines.append(\"| Group | Mean γ |\")\n    lines.append(\"|-------|--------|\")\n    tgg = gm[\"temporal_group_gamma\"]\n    for label, key in [(\"Early\", \"early\"), (\"Mid\", \"mid\"), (\"Late\", \"late\")]:\n        lines.append(f\"| {label} | {_fmt(tgg.get(key), 4)} |\")\n    lines.append(\"\")\n\n    # -- Section 4 --\n    lines.append(\"## 4. Expert/Failure Matching\\n\")\n    lines.append(\"| Metric | Value |\")\n    lines.append(\"|--------|-------|\")\n    lines.append(f\"| Exact match (game_file) | {ms['exact_match']} ({_fmt(ms['exact_match_rate'])}) |\")\n    lines.append(f\"| Template match (same task type) | {ms['template_match_only']} |\")\n    lines.append(f\"| Combined match rate | {_fmt(ms['template_match_rate'])} |\")\n    lines.append(f\"| Unmatched failures | {ms['unmatched']} |\")\n    lines.append(f\"| Divergence computed | {ms['divergence_computed']} |\")\n    lines.append(\"\")\n\n    # -- Section 5 --\n    lines.append(\"## 5. Trajectory Length Analysis\\n\")\n    lines.append(\"| Metric | Failure | Expert | Correction Span |\")\n    lines.append(\"|--------|---------|--------|-----------------|\")\n    fl = la.get(\"failure_trajectory_length\")\n    el = la.get(\"expert_trajectory_length\")\n    cs = la.get(\"correction_span\")\n    for stat in (\"n\", \"mean\", \"median\", \"std\", \"min\", \"max\"):\n        lines.append(\n            f\"| {stat} | {_fmt(fl.get(stat) if fl else None)} \"\n            f\"| {_fmt(el.get(stat) if el else None)} \"\n            f\"| {_fmt(cs.get(stat) if cs else None)} |\"\n        )\n    lines.append(\"\")\n\n    return \"\\n\".join(lines)\n\n\ndef print_summary(results: dict):\n    \"\"\"Print concise summary to stdout.\"\"\"\n    bs = results[\"basic_stats\"]\n    da = results[\"divergence_analysis\"]\n    ms = results[\"match_stats\"]\n\n    print(f\"\\n{'=' * 55}\")\n    print(\"FAILURE MODE ANALYSIS SUMMARY\")\n    print(f\"{'=' * 55}\")\n    print(f\"Tasks: {bs['total_tasks']}  Success: {bs['success']}  \"\n          f\"Failure: {bs['failure']}  SR: {bs['success_rate']:.3f}\")\n\n    print(f\"\\nPer-type SR:\")\n    for tt in CANONICAL_TASK_TYPES:\n        info = bs[\"per_task_type\"].get(tt, {})\n        sr = info.get(\"success_rate\")\n        sr_str = f\"{sr:.3f}\" if sr is not None else \"-\"\n        print(f\"  {tt:<16} {info.get('total', 0):>4} tasks  SR={sr_str}\")\n\n    print(f\"\\nMatching: exact={ms['exact_match']}  \"\n          f\"template_only={ms['template_match_only']}  \"\n          f\"unmatched={ms['unmatched']}  \"\n          f\"divergence_computed={ms['divergence_computed']}\")\n\n    ov = da.get(\"overall\")\n    if ov:\n        print(f\"\\nDivergence d (n={ov['n']}):\")\n        print(f\"  mean={ov['mean']:.3f}  median={ov['median']:.3f}  \"\n              f\"std={ov['std']:.3f}  [{ov['min']:.3f}, {ov['max']:.3f}]\")\n\n    tg = da[\"temporal_groups\"]\n    print(f\"\\nTemporal groups:\")\n    for label, key in [(\"Early  d<0.33 \", \"early_d_lt_0.33\"),\n                        (\"Mid    0.33-0.67\", \"mid_0.33_le_d_lt_0.67\"),\n                        (\"Late   d≥0.67 \", \"late_d_ge_0.67\")]:\n        g = tg[key]\n        print(f\"  {label}  n={g['n']}\")\n\n    print(f\"{'=' * 55}\")\n\n\n# ---------------------------------------------------------------------------\n# CLI\n# ---------------------------------------------------------------------------\n\ndef main():\n    parser = argparse.ArgumentParser(\n        description=\"Failure mode descriptive analysis for ETADN paper\"\n    )\n    parser.add_argument(\"--failure_dir\", type=str, required=True,\n                        help=\"Directory with trajectory JSONL files\")\n    parser.add_argument(\"--expert_file\", type=str, required=True,\n                        help=\"Expert trajectories JSON (alfworld_sft.json)\")\n    parser.add_argument(\"--output_dir\", type=str, required=True,\n                        help=\"Output directory for results\")\n    parser.add_argument(\"--gamma_min\", type=float, default=0.85,\n                        help=\"γ_min for γ(d) mapping (default: 0.85)\")\n    parser.add_argument(\"--gamma_max\", type=float, default=0.97,\n                        help=\"γ_max for γ(d) mapping (default: 0.97)\")\n    args = parser.parse_args()\n\n    trajectories = load_trajectories(args.failure_dir)\n    if not trajectories:\n        print(f\"ERROR: No trajectories found in {args.failure_dir}\")\n        return\n\n    expert_index = load_expert_index(args.expert_file)\n    print(f\"Loaded {len(trajectories)} trajectories, {len(expert_index)} experts\")\n\n    results = analyze(trajectories, expert_index, args.gamma_min, args.gamma_max)\n\n    out = Path(args.output_dir)\n    out.mkdir(parents=True, exist_ok=True)\n\n    json_path = out / \"failure_mode_summary.json\"\n    with open(json_path, \"w\") as f:\n        json.dump(results, f, indent=2, ensure_ascii=False)\n\n    md_path = out / \"failure_mode_report.md\"\n    report = generate_markdown(results)\n    with open(md_path, \"w\") as f:\n        f.write(report)\n\n    print_summary(results)\n    print(f\"\\nOutput: {json_path}\")\n    print(f\"        {md_path}\")\n\n\nif __name__ == \"__main__\":\n    main()\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "016c02fe-3950-4b7d-bcdb-ee49ba04f759",
  "isSidechain": false,
  "requestId": "req_011CayxkzFUHpA2VJphwmzFT",
  "type": "assistant",
  "uuid": "7d2cb803-ae80-4d8e-928e-73a418dd931e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl",
  "sessionId": "2c8f695e-2726-4bc0-b978-178d488e8a4b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VHKi1Dgr66Y5seVTETJjZS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16189,
      "cache_read_input_tokens": 23921,
      "output_tokens": 8103,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 16189,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 8103,
          "cache_read_input_tokens": 23921,
          "cache_creation_input_tokens": 16189,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 16189
          },
          "type": "message"
        }
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

_source line 21 · 2026-05-13T04:49:30.150Z_

<details><summary>↩ Tool result · `toolu_01Hw9rrXwYJ3cux1EpR2kwUt`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl/src/analyze_failure_modes.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7d2cb803-ae80-4d8e-928e-73a418dd931e",
  "isSidechain": false,
  "promptId": "70d64043-cfe7-4c40-93f2-a3764a31ceea",
  "type": "user",
  "uuid": "33b5f302-0b00-49a3-b39a-bb1939bbab5b",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl/src/analyze_failure_modes.py",
    "content": "\"\"\"Failure mode descriptive analysis for ETADN paper.\n\nAnalyzes divergence patterns between failure trajectories and expert trajectories.\nProduces structured JSON and Markdown report for paper's failure mode characterization.\n\nInput: v7 trajectory JSONL files + expert alfworld_sft.json\nOutput: failure_mode_summary.json + failure_mode_report.md\n\nUsage:\n  python src/analyze_failure_modes.py \\\n    --failure_dir data/trajectories_v7_icl \\\n    --expert_file data/alfworld_sft.json \\\n    --output_dir outputs/failure_analysis\n\"\"\"\n\nimport argparse\nimport json\nimport math\nimport statistics\nfrom collections import Counter, defaultdict\nfrom pathlib import Path\n\n\n# ---------------------------------------------------------------------------\n# Task type mapping\n# ---------------------------------------------------------------------------\n\nTASK_TYPE_FROM_PATH = {\n    \"pick_and_place\": \"pick_and_place\",\n    \"pick_clean_then_place\": \"clean\",\n    \"pick_heat_then_place\": \"heat\",\n    \"pick_cool_then_place\": \"cool\",\n    \"look_at_obj\": \"examine\",\n    \"pick_two_obj\": \"pick_two\",\n}\n\nCANONICAL_TASK_TYPES = [\"pick_and_place\", \"clean\", \"heat\", \"cool\", \"examine\", \"pick_two\"]\n\n\ndef get_task_type(game_file: str) -> str:\n    \"\"\"Infer canonical task type from game_file path.\"\"\"\n    for key, canonical in TASK_TYPE_FROM_PATH.items():\n        if f\"/{key}\" in game_file or game_file.startswith(key):\n            return canonical\n    return \"unknown\"\n\n\ndef normalize_game_file(game_file: str) -> str:\n    \"\"\"Extract &lt;task_dir>/&lt;trial_dir> as matching key.\"\"\"\n    gf = game_file.rstrip(\"/\")\n    if gf.endswith(\"/game.tw-pddl\"):\n        gf = gf[: -len(\"/game.tw-pddl\")]\n    parts = gf.split(\"/\")\n    return \"/\".join(parts[-2:]) if len(parts) >= 2 else gf\n\n\n# ---------------------------------------------------------------------------\n# Message helpers (handle both formats)\n# ---------------------------------------------------------------------------\n\ndef _role(msg: dict) -> str:\n    return msg.get(\"role\") or {\"human\": \"user\", \"gpt\": \"assistant\"}.get(msg.get(\"from\", \"\"), \"\")\n\n\ndef _content(msg: dict) -> str:\n    return msg.get(\"content\") or msg.get(\"value\", \"\")\n\n\ndef find_task_start(conversations: list) -> int:\n    \"\"\"Index of first action step after the last 'Your task is to:' message.\"\"\"\n    task_desc_idx = -1\n    for i, msg in enumerate(conversations):\n        if _role(msg) in (\"user\", \"human\") and \"Your task is to:\" in _content(msg):\n            task_desc_idx = i\n\n    search_from = task_desc_idx + 1 if task_desc_idx >= 0 else 0\n    for i in range(search_from, len(conversations)):\n        if _role(conversations[i]) in (\"assistant\", \"gpt\") and \"Action:\" in _content(conversations[i]):\n            return i\n    return len(conversations)\n\n\ndef extract_steps(conversations: list, start_idx: int) -> list[tuple[dict, dict | None]]:\n    \"\"\"Extract (action_msg, obs_msg|None) pairs from start_idx onward.\"\"\"\n    steps = []\n    i = start_idx\n    while i < len(conversations):\n        if _role(conversations[i]) in (\"assistant\", \"gpt\"):\n            action = conversations[i]\n            obs = None\n            if i + 1 < len(conversations) and _role(conversations[i + 1]) in (\"user\", \"human\"):\n                obs = conversations[i + 1]\n                i += 2\n            else:\n                i += 1\n            steps.append((action, obs))\n        else:\n            i += 1\n    return steps\n\n\ndef extract_action_text(content: str) -> str:\n    \"\"\"Extract and normalize 'Action: ...' from a step message.\"\"\"\n    for line in content.split(\"\\n\"):\n        stripped = line.strip()\n        if stripped.lower().startswith(\"action:\"):\n            return \" \".join(stripped[len(\"action:\"):].split()).lower()\n    return \" \".join(content.split()).lower()\n\n\n# ---------------------------------------------------------------------------\n# Divergence computation\n# ---------------------------------------------------------------------------\n\ndef find_divergence_point(expert_steps, fail_steps) -> int:\n    \"\"\"First step index where expert and failure take different actions.\"\"\"\n    min_len = min(len(expert_steps), len(fail_steps))\n    for i in range(min_len):\n        ea = extract_action_text(_content(expert_steps[i][0]))\n        fa = extract_action_text(_content(fail_steps[i][0]))\n        if ea != fa:\n            return i\n    return min_len\n\n\ndef compute_divergence(fail_traj: dict, expert: dict) -> dict | None:\n    \"\"\"Compute divergence metrics for a failure trajectory matched to an expert.\n\n    Returns dict with divergence_point, expert_length, d, correction_span,\n    or None if computation fails.\n    \"\"\"\n    fail_convs = fail_traj.get(\"conversations\", [])\n    expert_convs = expert.get(\"conversations\", [])\n    if not fail_convs or not expert_convs:\n        return None\n\n    fail_start = find_task_start(fail_convs)\n    expert_start = find_task_start(expert_convs)\n\n    fail_steps = extract_steps(fail_convs, fail_start)\n    expert_steps = extract_steps(expert_convs, expert_start)\n\n    if not fail_steps or not expert_steps:\n        return None\n\n    div_point = find_divergence_point(expert_steps, fail_steps)\n    expert_len = len(expert_steps)\n    d = div_point / expert_len if expert_len > 0 else 0.0\n    correction_span = expert_len - div_point\n\n    return {\n        \"divergence_point\": div_point,\n        \"expert_length\": expert_len,\n        \"failure_length\": len(fail_steps),\n        \"d\": d,\n        \"correction_span\": correction_span,\n    }\n\n\n# ---------------------------------------------------------------------------\n# γ(d) mapping\n# ---------------------------------------------------------------------------\n\ndef gamma_from_d(d: float, gamma_min: float = 0.85, gamma_max: float = 0.97) -> float:\n    \"\"\"Map divergence position d ∈ [0,1] to γ via linear interpolation.\n\n    Early divergence (d→0) → γ_min (action-error-like, concentrated credit).\n    Late divergence (d→1) → γ_max (planning-error-like, spread credit).\n    \"\"\"\n    return gamma_min + d * (gamma_max - gamma_min)\n\n\n# ---------------------------------------------------------------------------\n# Data loading\n# ---------------------------------------------------------------------------\n\ndef load_trajectories(failure_dir: str) -> list[dict]:\n    \"\"\"Load all trajectory JSONL files from a directory.\"\"\"\n    records = []\n    p = Path(failure_dir)\n    for jsonl_file in sorted(p.glob(\"*.jsonl\")):\n        with open(jsonl_file) as f:\n            for line in f:\n                if line.strip():\n                    records.append(json.loads(line))\n    return records\n\n\ndef load_expert_index(expert_file: str) -> dict[str, dict]:\n    \"\"\"Load expert trajectories indexed by normalized game_file.\"\"\"\n    with open(expert_file) as f:\n        experts = json.load(f)\n    return {normalize_game_file(ex[\"game_file\"]): ex for ex in experts}\n\n\n# ---------------------------------------------------------------------------\n# Analysis\n# ---------------------------------------------------------------------------\n\ndef analyze(trajectories: list[dict], expert_index: dict[str, dict],\n            gamma_min: float = 0.85, gamma_max: float = 0.97) -> dict:\n    \"\"\"Run all failure mode analyses. Returns structured results dict.\"\"\"\n\n    # -- 1. Basic statistics --\n    total = len(trajectories)\n    successes = [t for t in trajectories if t.get(\"reward\")]\n    failures = [t for t in trajectories if not t.get(\"reward\")]\n    n_success = len(successes)\n    n_failure = len(failures)\n    success_rate = n_success / total if total > 0 else 0.0\n\n    # Per-task-type success rate\n    type_total = Counter()\n    type_success = Counter()\n    for t in trajectories:\n        tt = t.get(\"task_type\") or get_task_type(t.get(\"game_file\", \"\"))\n        type_total[tt] += 1\n        if t.get(\"reward\"):\n            type_success[tt] += 1\n\n    per_type_sr = {}\n    for tt in CANONICAL_TASK_TYPES:\n        tot = type_total.get(tt, 0)\n        suc = type_success.get(tt, 0)\n        per_type_sr[tt] = {\n            \"total\": tot,\n            \"success\": suc,\n            \"failure\": tot - suc,\n            \"success_rate\": suc / tot if tot > 0 else None,\n        }\n\n    basic_stats = {\n        \"total_tasks\": total,\n        \"success\": n_success,\n        \"failure\": n_failure,\n        \"success_rate\": success_rate,\n        \"per_task_type\": per_type_sr,\n    }\n\n    # -- 4. Expert/Failure matching --\n    exact_match = 0\n    template_match = 0\n    unmatched = 0\n    matched_failures = []\n\n    for t in failures:\n        gf = t.get(\"game_file\", \"\")\n        key = normalize_game_file(gf)\n        expert = expert_index.get(key)\n\n        if expert is not None:\n            exact_match += 1\n            div_info = compute_divergence(t, expert)\n            if div_info is not None:\n                tt = t.get(\"task_type\") or get_task_type(gf)\n                matched_failures.append({\n                    \"task_type\": tt,\n                    \"game_file\": gf,\n                    **div_info,\n                })\n        else:\n            tt = t.get(\"task_type\") or get_task_type(gf)\n            found_template = False\n            for ek, ev in expert_index.items():\n                expert_tt = get_task_type(ev.get(\"game_file\", \"\"))\n                if expert_tt == tt:\n                    found_template = True\n                    break\n            if found_template:\n                template_match += 1\n            else:\n                unmatched += 1\n\n    match_stats = {\n        \"exact_match\": exact_match,\n        \"exact_match_rate\": exact_match / n_failure if n_failure > 0 else 0.0,\n        \"template_match_only\": template_match,\n        \"template_match_rate\": (exact_match + template_match) / n_failure if n_failure > 0 else 0.0,\n        \"unmatched\": unmatched,\n        \"divergence_computed\": len(matched_failures),\n    }\n\n    # -- 2. Divergence analysis --\n    d_values = [m[\"d\"] for m in matched_failures]\n    d_by_type = defaultdict(list)\n    for m in matched_failures:\n        d_by_type[m[\"task_type\"]].append(m[\"d\"])\n\n    bins = [(i / 10, (i + 1) / 10) for i in range(10)]\n    bin_labels = [f\"{lo:.1f}-{hi:.1f}\" for lo, hi in bins]\n    histogram = {label: 0 for label in bin_labels}\n    for d in d_values:\n        idx = min(int(d * 10), 9)\n        histogram[bin_labels[idx]] += 1\n\n    early = [d for d in d_values if d < 0.33]\n    mid = [d for d in d_values if 0.33 <= d < 0.67]\n    late = [d for d in d_values if d >= 0.67]\n\n    def _dist_stats(vals):\n        if not vals:\n            return None\n        return {\n            \"n\": len(vals),\n            \"mean\": statistics.mean(vals),\n            \"median\": statistics.median(vals),\n            \"std\": statistics.stdev(vals) if len(vals) > 1 else 0.0,\n            \"min\": min(vals),\n            \"max\": max(vals),\n            \"q1\": statistics.quantiles(vals, n=4)[0] if len(vals) >= 2 else vals[0],\n            \"q3\": statistics.quantiles(vals, n=4)[2] if len(vals) >= 2 else vals[0],\n        }\n\n    per_type_d = {}\n    for tt in CANONICAL_TASK_TYPES:\n        per_type_d[tt] = _dist_stats(d_by_type.get(tt, []))\n\n    divergence_analysis = {\n        \"overall\": _dist_stats(d_values),\n        \"histogram\": histogram,\n        \"temporal_groups\": {\n            \"early_d_lt_0.33\": {\"n\": len(early), \"mean_d\": statistics.mean(early) if early else None},\n            \"mid_0.33_le_d_lt_0.67\": {\"n\": len(mid), \"mean_d\": statistics.mean(mid) if mid else None},\n            \"late_d_ge_0.67\": {\"n\": len(late), \"mean_d\": statistics.mean(late) if late else None},\n        },\n        \"per_task_type\": per_type_d,\n    }\n\n    # -- 3. γ(d) mapping preview --\n    gamma_values = [gamma_from_d(d, gamma_min, gamma_max) for d in d_values]\n    gamma_analysis = {\n        \"gamma_min\": gamma_min,\n        \"gamma_max\": gamma_max,\n        \"distribution\": _dist_stats(gamma_values) if gamma_values else None,\n        \"temporal_group_gamma\": {\n            \"early\": statistics.mean([gamma_from_d(d, gamma_min, gamma_max) for d in early]) if early else None,\n            \"mid\": statistics.mean([gamma_from_d(d, gamma_min, gamma_max) for d in mid]) if mid else None,\n            \"late\": statistics.mean([gamma_from_d(d, gamma_min, gamma_max) for d in late]) if late else None,\n        },\n    }\n\n    # -- 5. Trajectory length analysis --\n    fail_lengths = [m[\"failure_length\"] for m in matched_failures]\n    expert_lengths = [m[\"expert_length\"] for m in matched_failures]\n    correction_spans = [m[\"correction_span\"] for m in matched_failures]\n\n    length_analysis = {\n        \"failure_trajectory_length\": _dist_stats(fail_lengths),\n        \"expert_trajectory_length\": _dist_stats(expert_lengths),\n        \"correction_span\": _dist_stats(correction_spans),\n    }\n\n    return {\n        \"basic_stats\": basic_stats,\n        \"divergence_analysis\": divergence_analysis,\n        \"gamma_mapping_preview\": gamma_analysis,\n        \"match_stats\": match_stats,\n        \"length_analysis\": length_analysis,\n    }\n\n\n# ---------------------------------------------------------------------------\n# Report generation\n# ---------------------------------------------------------------------------\n\ndef _fmt(val, decimals=3):\n    if val is None:\n        return \"-\"\n    if isinstance(val, float):\n        return f\"{val:.{decimals}f}\"\n    return str(val)\n\n\ndef generate_markdown(results: dict) -> str:\n    \"\"\"Generate Markdown report from analysis results.\"\"\"\n    lines = []\n    bs = results[\"basic_stats\"]\n    da = results[\"divergence_analysis\"]\n    gm = results[\"gamma_mapping_preview\"]\n    ms = results[\"match_stats\"]\n    la = results[\"length_analysis\"]\n\n    # -- Section 1 --\n    lines.append(\"# Failure Mode Analysis Report\\n\")\n    lines.append(\"## 1. Basic Statistics\\n\")\n    lines.append(f\"| Metric | Value |\")\n    lines.append(f\"|--------|-------|\")\n    lines.append(f\"| Total tasks | {bs['total_tasks']} |\")\n    lines.append(f\"| Success | {bs['success']} |\")\n    lines.append(f\"| Failure | {bs['failure']} |\")\n    lines.append(f\"| Success rate | {_fmt(bs['success_rate'])} |\")\n    lines.append(\"\")\n\n    lines.append(\"### Per-task-type Success Rate\\n\")\n    lines.append(\"| Task Type | Total | Success | Failure | Success Rate |\")\n    lines.append(\"|-----------|-------|---------|---------|--------------|\")\n    for tt in CANONICAL_TASK_TYPES:\n        info = bs[\"per_task_type\"].get(tt, {})\n        lines.append(\n            f\"| {tt} | {info.get('total', 0)} | {info.get('success', 0)} \"\n            f\"| {info.get('failure', 0)} | {_fmt(info.get('success_rate'))} |\"\n        )\n    lines.append(\"\")\n\n    # -- Section 2 --\n    lines.append(\"## 2. Divergence Analysis\\n\")\n    ov = da.get(\"overall\")\n    if ov:\n        lines.append(f\"Divergence position d = divergence_point / expert_length\\n\")\n        lines.append(\"| Statistic | Value |\")\n        lines.append(\"|-----------|-------|\")\n        for k in (\"n\", \"mean\", \"median\", \"std\", \"min\", \"max\", \"q1\", \"q3\"):\n            lines.append(f\"| {k} | {_fmt(ov[k])} |\")\n        lines.append(\"\")\n\n    lines.append(\"### d-value Histogram\\n\")\n    lines.append(\"| Bin | Count |\")\n    lines.append(\"|-----|-------|\")\n    for bin_label, count in da[\"histogram\"].items():\n        lines.append(f\"| {bin_label} | {count} |\")\n    lines.append(\"\")\n\n    lines.append(\"### Temporal Groups\\n\")\n    lines.append(\"| Group | n | Mean d |\")\n    lines.append(\"|-------|---|--------|\")\n    tg = da[\"temporal_groups\"]\n    for label, key in [(\"Early (d<0.33)\", \"early_d_lt_0.33\"),\n                        (\"Mid (0.33≤d<0.67)\", \"mid_0.33_le_d_lt_0.67\"),\n                        (\"Late (d≥0.67)\", \"late_d_ge_0.67\")]:\n        g = tg[key]\n        lines.append(f\"| {label} | {g['n']} | {_fmt(g.get('mean_d'))} |\")\n    lines.append(\"\")\n\n    lines.append(\"### Per-task-type d Distribution\\n\")\n    lines.append(\"| Task Type | n | Mean | Median | Std |\")\n    lines.append(\"|-----------|---|------|--------|-----|\")\n    for tt in CANONICAL_TASK_TYPES:\n        info = da[\"per_task_type\"].get(tt)\n        if info:\n            lines.append(\n                f\"| {tt} | {info['n']} | {_fmt(info['mean'])} \"\n                f\"| {_fmt(info['median'])} | {_fmt(info['std'])} |\"\n            )\n        else:\n            lines.append(f\"| {tt} | 0 | - | - | - |\")\n    lines.append(\"\")\n\n    # -- Section 3 --\n    lines.append(\"## 3. γ(d) Mapping Preview\\n\")\n    lines.append(f\"γ(d) = γ_min + d·(γ_max - γ_min), γ_min={gm['gamma_min']}, γ_max={gm['gamma_max']}\\n\")\n    gd = gm.get(\"distribution\")\n    if gd:\n        lines.append(\"| Statistic | γ value |\")\n        lines.append(\"|-----------|---------|\")\n        for k in (\"mean\", \"median\", \"std\", \"min\", \"max\"):\n            lines.append(f\"| {k} | {_fmt(gd[k], 4)} |\")\n        lines.append(\"\")\n\n    lines.append(\"### Mean γ by Temporal Group\\n\")\n    lines.append(\"| Group | Mean γ |\")\n    lines.append(\"|-------|--------|\")\n    tgg = gm[\"temporal_group_gamma\"]\n    for label, key in [(\"Early\", \"early\"), (\"Mid\", \"mid\"), (\"Late\", \"late\")]:\n        lines.append(f\"| {label} | {_fmt(tgg.get(key), 4)} |\")\n    lines.append(\"\")\n\n    # -- Section 4 --\n    lines.append(\"## 4. Expert/Failure Matching\\n\")\n    lines.append(\"| Metric | Value |\")\n    lines.append(\"|--------|-------|\")\n    lines.append(f\"| Exact match (game_file) | {ms['exact_match']} ({_fmt(ms['exact_match_rate'])}) |\")\n    lines.append(f\"| Template match (same task type) | {ms['template_match_only']} |\")\n    lines.append(f\"| Combined match rate | {_fmt(ms['template_match_rate'])} |\")\n    lines.append(f\"| Unmatched failures | {ms['unmatched']} |\")\n    lines.append(f\"| Divergence computed | {ms['divergence_computed']} |\")\n    lines.append(\"\")\n\n    # -- Section 5 --\n    lines.append(\"## 5. Trajectory Length Analysis\\n\")\n    lines.append(\"| Metric | Failure | Expert | Correction Span |\")\n    lines.append(\"|--------|---------|--------|-----------------|\")\n    fl = la.get(\"failure_trajectory_length\")\n    el = la.get(\"expert_trajectory_length\")\n    cs = la.get(\"correction_span\")\n    for stat in (\"n\", \"mean\", \"median\", \"std\", \"min\", \"max\"):\n        lines.append(\n            f\"| {stat} | {_fmt(fl.get(stat) if fl else None)} \"\n            f\"| {_fmt(el.get(stat) if el else None)} \"\n            f\"| {_fmt(cs.get(stat) if cs else None)} |\"\n        )\n    lines.append(\"\")\n\n    return \"\\n\".join(lines)\n\n\ndef print_summary(results: dict):\n    \"\"\"Print concise summary to stdout.\"\"\"\n    bs = results[\"basic_stats\"]\n    da = results[\"divergence_analysis\"]\n    ms = results[\"match_stats\"]\n\n    print(f\"\\n{'=' * 55}\")\n    print(\"FAILURE MODE ANALYSIS SUMMARY\")\n    print(f\"{'=' * 55}\")\n    print(f\"Tasks: {bs['total_tasks']}  Success: {bs['success']}  \"\n          f\"Failure: {bs['failure']}  SR: {bs['success_rate']:.3f}\")\n\n    print(f\"\\nPer-type SR:\")\n    for tt in CANONICAL_TASK_TYPES:\n        info = bs[\"per_task_type\"].get(tt, {})\n        sr = info.get(\"success_rate\")\n        sr_str = f\"{sr:.3f}\" if sr is not None else \"-\"\n        print(f\"  {tt:<16} {info.get('total', 0):>4} tasks  SR={sr_str}\")\n\n    print(f\"\\nMatching: exact={ms['exact_match']}  \"\n          f\"template_only={ms['template_match_only']}  \"\n          f\"unmatched={ms['unmatched']}  \"\n          f\"divergence_computed={ms['divergence_computed']}\")\n\n    ov = da.get(\"overall\")\n    if ov:\n        print(f\"\\nDivergence d (n={ov['n']}):\")\n        print(f\"  mean={ov['mean']:.3f}  median={ov['median']:.3f}  \"\n              f\"std={ov['std']:.3f}  [{ov['min']:.3f}, {ov['max']:.3f}]\")\n\n    tg = da[\"temporal_groups\"]\n    print(f\"\\nTemporal groups:\")\n    for label, key in [(\"Early  d<0.33 \", \"early_d_lt_0.33\"),\n                        (\"Mid    0.33-0.67\", \"mid_0.33_le_d_lt_0.67\"),\n                        (\"Late   d≥0.67 \", \"late_d_ge_0.67\")]:\n        g = tg[key]\n        print(f\"  {label}  n={g['n']}\")\n\n    print(f\"{'=' * 55}\")\n\n\n# ---------------------------------------------------------------------------\n# CLI\n# ---------------------------------------------------------------------------\n\ndef main():\n    parser = argparse.ArgumentParser(\n        description=\"Failure mode descriptive analysis for ETADN paper\"\n    )\n    parser.add_argument(\"--failure_dir\", type=str, required=True,\n                        help=\"Directory with trajectory JSONL files\")\n    parser.add_argument(\"--expert_file\", type=str, required=True,\n                        help=\"Expert trajectories JSON (alfworld_sft.json)\")\n    parser.add_argument(\"--output_dir\", type=str, required=True,\n                        help=\"Output directory for results\")\n    parser.add_argument(\"--gamma_min\", type=float, default=0.85,\n                        help=\"γ_min for γ(d) mapping (default: 0.85)\")\n    parser.add_argument(\"--gamma_max\", type=float, default=0.97,\n                        help=\"γ_max for γ(d) mapping (default: 0.97)\")\n    args = parser.parse_args()\n\n    trajectories = load_trajectories(args.failure_dir)\n    if not trajectories:\n        print(f\"ERROR: No trajectories found in {args.failure_dir}\")\n        return\n\n    expert_index = load_expert_index(args.expert_file)\n    print(f\"Loaded {len(trajectories)} trajectories, {len(expert_index)} experts\")\n\n    results = analyze(trajectories, expert_index, args.gamma_min, args.gamma_max)\n\n    out = Path(args.output_dir)\n    out.mkdir(parents=True, exist_ok=True)\n\n    json_path = out / \"failure_mode_summary.json\"\n    with open(json_path, \"w\") as f:\n        json.dump(results, f, indent=2, ensure_ascii=False)\n\n    md_path = out / \"failure_mode_report.md\"\n    report = generate_markdown(results)\n    with open(md_path, \"w\") as f:\n        f.write(report)\n\n    print_summary(results)\n    print(f\"\\nOutput: {json_path}\")\n    print(f\"        {md_path}\")\n\n\nif __name__ == \"__main__\":\n    main()\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "7d2cb803-ae80-4d8e-928e-73a418dd931e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl",
  "sessionId": "2c8f695e-2726-4bc0-b978-178d488e8a4b",
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
  "leafUuid": "33b5f302-0b00-49a3-b39a-bb1939bbab5b",
  "sessionId": "2c8f695e-2726-4bc0-b978-178d488e8a4b"
}
```

---

### Runtime record

_source line 23_

```json
{
  "type": "ai-title",
  "aiTitle": "Write failure mode analysis script for paper",
  "sessionId": "2c8f695e-2726-4bc0-b978-178d488e8a4b"
}
```

---

### Tool call

_source line 24 · 2026-05-13T04:49:37.082Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01MMjoi6R3y2su4joZj7THH8`</summary>

```json
{
  "command": "python -m py_compile src/analyze_failure_modes.py && echo \"OK\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "33b5f302-0b00-49a3-b39a-bb1939bbab5b",
  "isSidechain": false,
  "requestId": "req_011CayxuTDRMgwLEwQLWisY2",
  "type": "assistant",
  "uuid": "f3123e1a-0783-4d93-9cad-0a46f5e5e786",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl",
  "sessionId": "2c8f695e-2726-4bc0-b978-178d488e8a4b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Tof2QitUpCHEjtYCgep4Ec",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8155,
      "cache_read_input_tokens": 40110,
      "output_tokens": 103,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8155,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 103,
          "cache_read_input_tokens": 40110,
          "cache_creation_input_tokens": 8155,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8155
          },
          "type": "message"
        }
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

_source line 25 · 2026-05-13T04:49:37.256Z_

<details><summary>↩ Tool result · reported error · `toolu_01MMjoi6R3y2su4joZj7THH8`</summary>

```text
Exit code 127
/bin/bash: line 1: python: command not found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f3123e1a-0783-4d93-9cad-0a46f5e5e786",
  "isSidechain": false,
  "promptId": "70d64043-cfe7-4c40-93f2-a3764a31ceea",
  "type": "user",
  "uuid": "8d392bd2-82f4-456f-9037-fd1483ca2f99",
  "toolUseResult": "Error: Exit code 127\n/bin/bash: line 1: python: command not found",
  "sourceToolAssistantUUID": "f3123e1a-0783-4d93-9cad-0a46f5e5e786",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl",
  "sessionId": "2c8f695e-2726-4bc0-b978-178d488e8a4b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-13T04:49:49.273Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01EXxVyM18kr18eSnfaTNi55`</summary>

```json
{
  "command": "python3 -m py_compile src/analyze_failure_modes.py && echo \"OK\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8d392bd2-82f4-456f-9037-fd1483ca2f99",
  "isSidechain": false,
  "requestId": "req_011Cayxuya3aEUoiBugzBUNF",
  "type": "assistant",
  "uuid": "b10c4c1d-c28a-41aa-9a0f-715eef7e573f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl",
  "sessionId": "2c8f695e-2726-4bc0-b978-178d488e8a4b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PMzFcV17xmjcE2NJJARcPv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 110,
      "cache_read_input_tokens": 48265,
      "output_tokens": 105,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 110,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 105,
          "cache_read_input_tokens": 48265,
          "cache_creation_input_tokens": 110,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 110
          },
          "type": "message"
        }
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

_source line 27 · 2026-05-13T04:49:49.400Z_

<details><summary>↩ Tool result · `toolu_01EXxVyM18kr18eSnfaTNi55`</summary>

```text
OK
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b10c4c1d-c28a-41aa-9a0f-715eef7e573f",
  "isSidechain": false,
  "promptId": "70d64043-cfe7-4c40-93f2-a3764a31ceea",
  "type": "user",
  "uuid": "02b98753-6c49-4743-8c1e-21d2ffd5024e",
  "toolUseResult": {
    "stdout": "OK",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "b10c4c1d-c28a-41aa-9a0f-715eef7e573f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl",
  "sessionId": "2c8f695e-2726-4bc0-b978-178d488e8a4b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 28 · 2026-05-13T04:49:58.241Z_

语法验证通过。脚本写入 `src/analyze_failure_modes.py`，覆盖全部 5 类分析：

1. **基本统计** — 总体成功率 + 6 种 task type 分别统计
2. **Divergence 分析** — d 分布统计、10-bin 直方图、early/mid/late 三组、per-type d 分布
3. **γ(d) 映射预览** — 线性插值 γ(d)=γ_min+d·(γ_max-γ_min)，各组均值 γ
4. **Expert/Failure 匹配** — exact match / template match / unmatched 统计
5. **轨迹长度** — failure vs expert 长度分布 + correction span

输出 `failure_mode_summary.json` + `failure_mode_report.md`，纯 CPU，无 GPU 依赖。divergence 计算逻辑直接复用 `build_dpo_pairs.py` 的 action 对比方式。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "02b98753-6c49-4743-8c1e-21d2ffd5024e",
  "isSidechain": false,
  "requestId": "req_011CayxvsUTbzd1jVF19Lsxt",
  "type": "assistant",
  "uuid": "e02410d4-fe70-48b0-ad01-426da006ae0e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl",
  "sessionId": "2c8f695e-2726-4bc0-b978-178d488e8a4b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JbBzoRzzgrTvvqxE78xJLT",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 86,
      "cache_read_input_tokens": 48375,
      "output_tokens": 289,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 86,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 289,
          "cache_read_input_tokens": 48375,
          "cache_creation_input_tokens": 86,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 86
          },
          "type": "message"
        }
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

_source line 29_

```json
{
  "type": "last-prompt",
  "leafUuid": "e02410d4-fe70-48b0-ad01-426da006ae0e",
  "sessionId": "2c8f695e-2726-4bc0-b978-178d488e8a4b"
}
```

---

### Runtime record

_source line 30_

```json
{
  "type": "ai-title",
  "aiTitle": "Write failure mode analysis script for paper",
  "sessionId": "2c8f695e-2726-4bc0-b978-178d488e8a4b"
}
```

---
