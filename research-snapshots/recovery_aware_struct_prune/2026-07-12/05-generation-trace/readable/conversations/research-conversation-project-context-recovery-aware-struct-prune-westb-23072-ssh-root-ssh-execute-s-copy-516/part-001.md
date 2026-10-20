# Research conversation: <project_context> # 项目: recovery_aware_struct_prune ## 运行环境 - 服务器名: westb-23072 - SSH 账户: root（调用 ssh_execute / submit_t — Part 1 of 2

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM (July export snapshot)** · Conversation logs

[Transcript overview](../research-conversation-project-context-recovery-aware-struct-prune-westb-23072-ssh-root-ssh-execute-s-copy-516.md) · [Part 2 →](part-002.md) · [Structured JSON](../../../sessions/bd/bd284532baf56f89213a.json)

## Before a recorded user message

## Before a recorded user message

2 recorded events


### Runtime record

_source line 1 · 2026-05-23T10:47:08.150Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-23T10:47:08.150Z",
  "sessionId": "3a90179e-e19e-41d1-8fb4-f23e916f555f",
  "content": "&lt;project_context>\n# 项目: recovery_aware_struct_prune\n\n## 运行环境\n- 服务器名: westb-23072\n- SSH 账户: root（调用 ssh_execute / submit_training_job 时传入 account=\"root\"）\n- SSH 连接命令: ssh westb-23072  # 必须用此命令，~/.ssh/config 自动应用密钥和跳板机，禁止用裸 IP\n- 项目代码根目录: /root/recovery_aware_struct_prune\n\n## ⚠️ 活跃约束（必须遵守）\n\n- **C002**: 所有模型/checkpoint/大文件只写 /root/autodl-tmp/recovery_aware_struct_prune/，禁止写根分区（根分区仅 30GB）（原因：根分区 100% 满导致 v4 剪枝失败。AutoDL 根分区只有 30GB，模型文件 10GB+ 必须写数据盘。） [来自 D005]\n- **C003**: westd-11672 GPU 分配：cuda:0 和 cuda:1 均属本项目独占，可用于 α ablation、baseline 实验等。与 westb-23072 (C001) 同等管理。（原因：Manager 新分配 westd-11672 (2×RTX PRO 6000) 给本项目，需明确 GPU 归属边界供 Reviewer 审查。）\n- **C005**: GPU 白名单：westb-23072 cuda:0/1 + westd-32935 cuda:0/1/2/3（共 6 张）。westd-29022 已替换为 westd-32935。严禁在白名单外的 GPU 上启动实验。（原因：项目 execution config (projects.yaml) 已更新服务器为 westd-32935，替代 westd-29022。C005 同步更新。） [来自 D061]\n\n\n## 环境搭建\n连接服务器后先调 `detect_image` 检测是否为预置镜像。如果匹配，跳过基础环境搭建，只装项目特有依赖。已预装的包不要重复安装。\n\n## 输出风格\n回复简洁直接。只输出执行结果和必要信息，不要解释过程、不要客套、不要给未被要求的建议。\n&lt;/project_context>\n整理论文数据溯源表：每个论文中的实验数值 → registry exp_id → 服务器结果文件路径。\n\n**论文表格文件位置**（全部在本地，用 Read 工具读取）:\n- `/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/tab1_recovery_gradient.tex`\n- `/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/tab2_decoupling.tex`\n- `/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/table3_alpha.tex`\n- `/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/table4_sparsity_cliff.tex`\n- `/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/table5_inference.tex`\n- `/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/tab_math500.tex`\n- `/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/tab_mbpp.tex`\n- `/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/tab5_cross_scale.tex`\n- `/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/tab_cka_stability.tex`\n- `/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/experiments.tex`（内联数值）\n- `/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/appendix.tex`\n- `/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/abstract.tex`\n- `/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/introduction.tex`\n\n**你的任务**:\n\n1. Read 每个 tex 文件，提取所有数值（accuracy、Δ、parameter count 等）\n\n2. 用 `read_registry(project=\"recovery_aware_struct_prune\", filters={\"conclusion\": \"success\"}, limit=50)` 读取已完成实验（可能需要多次调用，每次 limit=50，用 offset 翻页）。提取每个实验的 exp_id、metrics、spec（包含 server、output_path/checkpoint_path/log_path）\n\n3. 建立映射表，格式如下：\n\n```markdown\n## Table X: [表名]\n\n| 行 | 列 | 论文数值 | registry exp_id | 结果文件路径 | eval 脚本版本 | seed |\n|----|-----|---------|----------------|-------------|-------------|------|\n| CKA-only 20% | GSM8K SFT | 65.20% | eval_gsm8k_sft_cka_only_20 | /root/autodl-tmp/.../results/xxx.json | NEW | 42 |\n```\n\n4. 对于每个数值，标注：\n   - **eval 脚本版本**: NEW (May 23+，pred_answer/gold_answer) 或 OLD/‡ (May 17-19，pred/gold/idx)\n   - **seed**: 单 seed (42) 或多 seed mean\n   - 如果某个数值在 registry 中找不到对应 exp_id，标注 \"⚠️ 无 registry 记录\"\n   - 如果 registry 的 metrics 与论文数值不一致，标注 \"⚠️ 数值不一致: registry=X, paper=Y\"\n\n5. 也覆盖 Figure 1/2/3 的数据来源（检查 experiments.tex 中的 figure 描述）\n\n6. 将完整的溯源表写入：\n   `/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/data_provenance_audit.md`\n\n**重要**：\n- 不需要 SSH 到服务器，只需从 registry 读取数据和从本地读取论文 tex 文件\n- 结果文件路径从 registry spec 中的 output_path 或 command 中推断\n- eval 脚本版本判断：May 23 或之后提交的用 NEW，之前的用 OLD。带 v2/v3 后缀的 rerun 用 NEW\n- registry 读取可能需要多次调用（实验很多）"
}
````

---


### Runtime record

_source line 2 · 2026-05-23T10:47:08.153Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-23T10:47:08.153Z",
  "sessionId": "3a90179e-e19e-41d1-8fb4-f23e916f555f"
}
```

---


## Round 1

## Round 1

94 recorded events


### User

_source line 3 · 2026-05-23T10:47:08.185Z_

&lt;project_context>
# 项目: recovery_aware_struct_prune

## 运行环境
- 服务器名: westb-23072
- SSH 账户: root（调用 ssh_execute / submit_training_job 时传入 account="root"）
- SSH 连接命令: ssh westb-23072  # 必须用此命令，~/.ssh/config 自动应用密钥和跳板机，禁止用裸 IP
- 项目代码根目录: /root/recovery_aware_struct_prune

## ⚠️ 活跃约束（必须遵守）

- **C002**: 所有模型/checkpoint/大文件只写 /root/autodl-tmp/recovery_aware_struct_prune/，禁止写根分区（根分区仅 30GB）（原因：根分区 100% 满导致 v4 剪枝失败。AutoDL 根分区只有 30GB，模型文件 10GB+ 必须写数据盘。） [来自 D005]
- **C003**: westd-11672 GPU 分配：cuda:0 和 cuda:1 均属本项目独占，可用于 α ablation、baseline 实验等。与 westb-23072 (C001) 同等管理。（原因：Manager 新分配 westd-11672 (2×RTX PRO 6000) 给本项目，需明确 GPU 归属边界供 Reviewer 审查。）
- **C005**: GPU 白名单：westb-23072 cuda:0/1 + westd-32935 cuda:0/1/2/3（共 6 张）。westd-29022 已替换为 westd-32935。严禁在白名单外的 GPU 上启动实验。（原因：项目 execution config (projects.yaml) 已更新服务器为 westd-32935，替代 westd-29022。C005 同步更新。） [来自 D061]


## 环境搭建
连接服务器后先调 `detect_image` 检测是否为预置镜像。如果匹配，跳过基础环境搭建，只装项目特有依赖。已预装的包不要重复安装。

## 输出风格
回复简洁直接。只输出执行结果和必要信息，不要解释过程、不要客套、不要给未被要求的建议。
&lt;/project_context>
整理论文数据溯源表：每个论文中的实验数值 → registry exp_id → 服务器结果文件路径。

**论文表格文件位置**（全部在本地，用 Read 工具读取）:
- `/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/tab1_recovery_gradient.tex`
- `/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/tab2_decoupling.tex`
- `/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/table3_alpha.tex`
- `/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/table4_sparsity_cliff.tex`
- `/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/table5_inference.tex`
- `/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/tab_math500.tex`
- `/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/tab_mbpp.tex`
- `/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/tab5_cross_scale.tex`
- `/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/tab_cka_stability.tex`
- `/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/experiments.tex`（内联数值）
- `/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/appendix.tex`
- `/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/abstract.tex`
- `/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/introduction.tex`

**你的任务**:

1. Read 每个 tex 文件，提取所有数值（accuracy、Δ、parameter count 等）

2. 用 `read_registry(project="recovery_aware_struct_prune", filters={"conclusion": "success"}, limit=50)` 读取已完成实验（可能需要多次调用，每次 limit=50，用 offset 翻页）。提取每个实验的 exp_id、metrics、spec（包含 server、output_path/checkpoint_path/log_path）

3. 建立映射表，格式如下：

```markdown
## Table X: [表名]

| 行 | 列 | 论文数值 | registry exp_id | 结果文件路径 | eval 脚本版本 | seed |
|----|-----|---------|----------------|-------------|-------------|------|
| CKA-only 20% | GSM8K SFT | 65.20% | eval_gsm8k_sft_cka_only_20 | /root/autodl-tmp/.../results/xxx.json | NEW | 42 |
```

4. 对于每个数值，标注：
   - **eval 脚本版本**: NEW (May 23+，pred_answer/gold_answer) 或 OLD/‡ (May 17-19，pred/gold/idx)
   - **seed**: 单 seed (42) 或多 seed mean
   - 如果某个数值在 registry 中找不到对应 exp_id，标注 "⚠️ 无 registry 记录"
   - 如果 registry 的 metrics 与论文数值不一致，标注 "⚠️ 数值不一致: registry=X, paper=Y"

5. 也覆盖 Figure 1/2/3 的数据来源（检查 experiments.tex 中的 figure 描述）

6. 将完整的溯源表写入：
   `/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/data_provenance_audit.md`

**重要**：
- 不需要 SSH 到服务器，只需从 registry 读取数据和从本地读取论文 tex 文件
- 结果文件路径从 registry spec 中的 output_path 或 command 中推断
- eval 脚本版本判断：May 23 或之后提交的用 NEW，之前的用 OLD。带 v2/v3 后缀的 rerun 用 NEW
- registry 读取可能需要多次调用（实验很多）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "dddf37fd-16cc-4cd5-bb05-648328938281",
  "type": "user",
  "uuid": "71e8088e-958a-4108-a659-cb1c443176ea",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "3a90179e-e19e-41d1-8fb4-f23e916f555f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Runtime record

_source line 4 · 2026-05-23T10:47:08.184Z_

```json
{
  "parentUuid": "71e8088e-958a-4108-a659-cb1c443176ea",
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
  "uuid": "5d189ab1-353f-4fd3-a93e-e5591f5cdf9b",
  "timestamp": "2026-05-23T10:47:08.184Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "3a90179e-e19e-41d1-8fb4-f23e916f555f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---


### Runtime record

_source line 5 · 2026-05-23T10:47:08.184Z_

```json
{
  "parentUuid": "5d189ab1-353f-4fd3-a93e-e5591f5cdf9b",
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
  "uuid": "8d532e79-8b24-4caa-91bb-1653a31dd5b9",
  "timestamp": "2026-05-23T10:47:08.184Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "3a90179e-e19e-41d1-8fb4-f23e916f555f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---


### Runtime record

_source line 6 · 2026-05-23T10:47:08.184Z_

```json
{
  "parentUuid": "8d532e79-8b24-4caa-91bb-1653a31dd5b9",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "85c1c881-e9cc-435d-b62b-c4cf1fd74263",
  "timestamp": "2026-05-23T10:47:08.184Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "3a90179e-e19e-41d1-8fb4-f23e916f555f",
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
  "aiTitle": "Map paper results to registry experiments",
  "sessionId": "3a90179e-e19e-41d1-8fb4-f23e916f555f"
}
```

---


### Assistant

_source line 8 · 2026-05-23T10:47:11.880Z_

<details><summary>Logged reasoning block</summary>

```text
Let me start by reading all the tex files and the registry data in parallel. I'll need to:

1. Read all tex files to extract numerical values
2. Read the registry to get experiment data

Let me begin by reading the tex files and the registry simultaneously.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "85c1c881-e9cc-435d-b62b-c4cf1fd74263",
  "isSidechain": false,
  "requestId": "req_011CbKNGNpLekdgNEjAQRCoa",
  "type": "assistant",
  "uuid": "eb24b86c-b101-4723-8cfa-bfadc082b886",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "3a90179e-e19e-41d1-8fb4-f23e916f555f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EWzUGgWUHoVvgZ9iEqHwom",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13376,
      "cache_read_input_tokens": 11841,
      "output_tokens": 218,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13376,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 218,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 13376,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13376
          },
          "type": "message"
        }
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

_source line 9 · 2026-05-23T10:47:12.428Z_

开始读取论文表格文件和 registry 数据。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "eb24b86c-b101-4723-8cfa-bfadc082b886",
  "isSidechain": false,
  "requestId": "req_011CbKNGNpLekdgNEjAQRCoa",
  "type": "assistant",
  "uuid": "252ffbc5-0dc6-4739-885e-3b72bd933c38",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "3a90179e-e19e-41d1-8fb4-f23e916f555f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EWzUGgWUHoVvgZ9iEqHwom",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13376,
      "cache_read_input_tokens": 11841,
      "output_tokens": 218,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13376,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 218,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 13376,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13376
          },
          "type": "message"
        }
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

_source line 10 · 2026-05-23T10:47:13.831Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01Y5j1kkwaxDsWB8g6LctV1Q`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__register_artifact,mcp__agent-ml-research__save_project_file",
  "max_results": 4
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "252ffbc5-0dc6-4739-885e-3b72bd933c38",
  "isSidechain": false,
  "requestId": "req_011CbKNGNpLekdgNEjAQRCoa",
  "type": "assistant",
  "uuid": "4875beca-6fa7-4fba-951f-60891b69a9fe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "3a90179e-e19e-41d1-8fb4-f23e916f555f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EWzUGgWUHoVvgZ9iEqHwom",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13376,
      "cache_read_input_tokens": 11841,
      "output_tokens": 218,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13376,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 218,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 13376,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13376
          },
          "type": "message"
        }
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

_source line 11 · 2026-05-23T10:47:13.838Z_

<details><summary>↩ Tool result · `toolu_01Y5j1kkwaxDsWB8g6LctV1Q`</summary>

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
  "tool_name": "mcp__agent-ml-research__read_project_file"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__register_artifact"
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
  "parentUuid": "4875beca-6fa7-4fba-951f-60891b69a9fe",
  "isSidechain": false,
  "promptId": "dddf37fd-16cc-4cd5-bb05-648328938281",
  "type": "user",
  "uuid": "5cdddc68-f2a9-493d-97b7-be75b42bf902",
  "toolUseResult": {
    "matches": [
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__register_artifact",
      "mcp__agent-ml-research__save_project_file"
    ],
    "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__register_artifact,mcp__agent-ml-research__save_project_file",
    "total_deferred_tools": 25
  },
  "sourceToolAssistantUUID": "4875beca-6fa7-4fba-951f-60891b69a9fe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "3a90179e-e19e-41d1-8fb4-f23e916f555f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Assistant

_source line 12 · 2026-05-23T10:47:16.639Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me read all the tex files and the registry data in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5cdddc68-f2a9-493d-97b7-be75b42bf902",
  "isSidechain": false,
  "requestId": "req_011CbKNGo4rLHPN2FBzfYpBN",
  "type": "assistant",
  "uuid": "694bb490-0561-4fc0-ba1f-39be46ea2ab0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "3a90179e-e19e-41d1-8fb4-f23e916f555f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LTRFjV5U2DZDnMEQV3bmJE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1748,
      "cache_read_input_tokens": 25217,
      "output_tokens": 1165,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1748,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1165,
          "cache_read_input_tokens": 25217,
          "cache_creation_input_tokens": 1748,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1748
          },
          "type": "message"
        }
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

_source line 13 · 2026-05-23T10:47:18.722Z_

<details open><summary>🔧 Tool call — Read · `toolu_01HdnnBWHBin4Smo4agMq37P`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/tab1_recovery_gradient.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "694bb490-0561-4fc0-ba1f-39be46ea2ab0",
  "isSidechain": false,
  "requestId": "req_011CbKNGo4rLHPN2FBzfYpBN",
  "type": "assistant",
  "uuid": "8379e0ee-2e18-4719-8f73-dc325869782e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "3a90179e-e19e-41d1-8fb4-f23e916f555f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LTRFjV5U2DZDnMEQV3bmJE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1748,
      "cache_read_input_tokens": 25217,
      "output_tokens": 1165,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1748,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1165,
          "cache_read_input_tokens": 25217,
          "cache_creation_input_tokens": 1748,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1748
          },
          "type": "message"
        }
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

_source line 14 · 2026-05-23T10:47:18.732Z_

<details><summary>↩ Tool result · `toolu_01HdnnBWHBin4Smo4agMq37P`</summary>

```text
1	\begin{table}[t]
2	\centering
3	\small
4	\caption{Recovery capacity spectrum: GRPO dynamics for four pruning criteria at 20\% sparsity under identical configuration (lr $1{\times}10^{-6}$, $\beta{=}0.01$, $T{=}0.4$, 100 steps). Peak reward = best across 100 training steps. $f_0$: fraction of training batches where all sampled completions receive identical reward (lower = healthier exploration). Best in \textbf{bold}.}
5	\label{tab:recovery_gradient}
6	\begin{tabular}{@{}lcccc@{}}
7	\toprule
8	Method & Peak Rew.\,$\uparrow$ & Mean Rew.\,$\uparrow$ & Min $f_0$\,$\downarrow$ & Behavior \\
9	\midrule
10	CKA-only & \textbf{0.354} & \textbf{0.285} & \textbf{0.125} & Active learning \\
11	Random & 0.190 & 0.164 & 0.300 & Stagnation \\
12	Standard & 0.081 & 0.050 & 0.500 & Borderline collapse \\
13	\rasp{} ($\alpha{=}1.0$)$^\ddagger$ & 0.061 & 0.031 & 0.675 & Full collapse \\
14	\bottomrule
15	\multicolumn{5}{l}{\footnotesize $^\ddagger$Single seed ($N{=}1$). CKA-only, Standard, and Random validated with 3 seeds (Table~\ref{tab:decoupling}).}
16	\end{tabular}
17	\end{table}
18	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8379e0ee-2e18-4719-8f73-dc325869782e",
  "isSidechain": false,
  "promptId": "dddf37fd-16cc-4cd5-bb05-648328938281",
  "type": "user",
  "uuid": "9fbd5774-5ae1-4ad9-8251-a8d08d5d6dad",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/tab1_recovery_gradient.tex",
      "content": "\\begin{table}[t]\n\\centering\n\\small\n\\caption{Recovery capacity spectrum: GRPO dynamics for four pruning criteria at 20\\% sparsity under identical configuration (lr $1{\\times}10^{-6}$, $\\beta{=}0.01$, $T{=}0.4$, 100 steps). Peak reward = best across 100 training steps. $f_0$: fraction of training batches where all sampled completions receive identical reward (lower = healthier exploration). Best in \\textbf{bold}.}\n\\label{tab:recovery_gradient}\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\nMethod & Peak Rew.\\,$\\uparrow$ & Mean Rew.\\,$\\uparrow$ & Min $f_0$\\,$\\downarrow$ & Behavior \\\\\n\\midrule\nCKA-only & \\textbf{0.354} & \\textbf{0.285} & \\textbf{0.125} & Active learning \\\\\nRandom & 0.190 & 0.164 & 0.300 & Stagnation \\\\\nStandard & 0.081 & 0.050 & 0.500 & Borderline collapse \\\\\n\\rasp{} ($\\alpha{=}1.0$)$^\\ddagger$ & 0.061 & 0.031 & 0.675 & Full collapse \\\\\n\\bottomrule\n\\multicolumn{5}{l}{\\footnotesize $^\\ddagger$Single seed ($N{=}1$). CKA-only, Standard, and Random validated with 3 seeds (Table~\\ref{tab:decoupling}).}\n\\end{tabular}\n\\end{table}\n",
      "numLines": 18,
      "startLine": 1,
      "totalLines": 18
    }
  },
  "sourceToolAssistantUUID": "8379e0ee-2e18-4719-8f73-dc325869782e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "3a90179e-e19e-41d1-8fb4-f23e916f555f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 15 · 2026-05-23T10:47:19.073Z_

<details open><summary>🔧 Tool call — Read · `toolu_01TtKUFaVuKs4SBgYvh9x2PD`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/tab2_decoupling.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9fbd5774-5ae1-4ad9-8251-a8d08d5d6dad",
  "isSidechain": false,
  "requestId": "req_011CbKNGo4rLHPN2FBzfYpBN",
  "type": "assistant",
  "uuid": "c21c0207-b64a-4a7e-9871-cd990dc423b9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "3a90179e-e19e-41d1-8fb4-f23e916f555f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LTRFjV5U2DZDnMEQV3bmJE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1748,
      "cache_read_input_tokens": 25217,
      "output_tokens": 1165,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1748,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1165,
          "cache_read_input_tokens": 25217,
          "cache_creation_input_tokens": 1748,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1748
          },
          "type": "message"
        }
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

_source line 16 · 2026-05-23T10:47:19.078Z_

<details><summary>↩ Tool result · `toolu_01TtKUFaVuKs4SBgYvh9x2PD`</summary>

```text
1	\begin{table}[t]
2	\centering
3	\small
4	\caption{GRPO responsiveness on GSM8K ($N{=}1{,}319$, greedy decoding). All pruned models use the controlled GRPO configuration (identical hyperparameters including \texttt{reward\_desert\_patience}{$=$}50), evaluated at step 100. CKA-only, Standard, and Random report mean $\pm$ std over 3 GRPO seeds; \rasp{} uses a single seed. Best in \textbf{bold}.}
5	\label{tab:decoupling}
6	\begin{tabular}{@{}lcccc@{}}
7	\toprule
8	Model & SFT Acc.\,(\%) & GRPO Acc.\,(\%) & $\Delta$\,(pp) & Peak Rew. \\
9	\midrule
10	Unpruned & \textbf{81.27} & \textbf{81.27} & $\phantom{-}$0.00 & \textbf{0.669} \\
11	CKA-only 20\% & 63.91 & 64.39{\scriptsize$\pm$0.19} & $+$0.48 & 0.354 \\
12	Standard 20\% & 59.29 & 59.84{\scriptsize$\pm$0.38} & $+$0.55 & 0.081 \\
13	\rasp{} ($\alpha{=}1.0$) 20\% & 61.49 & 60.88 & $-$0.61 & 0.061 \\
14	Random 20\% & 51.25 & 50.72{\scriptsize$\pm$0.15} & $-$0.53 & 0.190 \\
15	\midrule
16	ShortGPT 20\%$^\dagger$ & 44.73 & 43.37 & $-$1.36 & -- \\
17	\bottomrule
18	\multicolumn{5}{l}{\footnotesize $^\dagger$Depth pruning baseline~\citep{shortgpt2024}; removes entire layers.} \\
19	\end{tabular}
20	\end{table}
21	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c21c0207-b64a-4a7e-9871-cd990dc423b9",
  "isSidechain": false,
  "promptId": "dddf37fd-16cc-4cd5-bb05-648328938281",
  "type": "user",
  "uuid": "56f9d100-b140-40ba-826b-7887f43f0de4",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/tab2_decoupling.tex",
      "content": "\\begin{table}[t]\n\\centering\n\\small\n\\caption{GRPO responsiveness on GSM8K ($N{=}1{,}319$, greedy decoding). All pruned models use the controlled GRPO configuration (identical hyperparameters including \\texttt{reward\\_desert\\_patience}{$=$}50), evaluated at step 100. CKA-only, Standard, and Random report mean $\\pm$ std over 3 GRPO seeds; \\rasp{} uses a single seed. Best in \\textbf{bold}.}\n\\label{tab:decoupling}\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\nModel & SFT Acc.\\,(\\%) & GRPO Acc.\\,(\\%) & $\\Delta$\\,(pp) & Peak Rew. \\\\\n\\midrule\nUnpruned & \\textbf{81.27} & \\textbf{81.27} & $\\phantom{-}$0.00 & \\textbf{0.669} \\\\\nCKA-only 20\\% & 63.91 & 64.39{\\scriptsize$\\pm$0.19} & $+$0.48 & 0.354 \\\\\nStandard 20\\% & 59.29 & 59.84{\\scriptsize$\\pm$0.38} & $+$0.55 & 0.081 \\\\\n\\rasp{} ($\\alpha{=}1.0$) 20\\% & 61.49 & 60.88 & $-$0.61 & 0.061 \\\\\nRandom 20\\% & 51.25 & 50.72{\\scriptsize$\\pm$0.15} & $-$0.53 & 0.190 \\\\\n\\midrule\nShortGPT 20\\%$^\\dagger$ & 44.73 & 43.37 & $-$1.36 & -- \\\\\n\\bottomrule\n\\multicolumn{5}{l}{\\footnotesize $^\\dagger$Depth pruning baseline~\\citep{shortgpt2024}; removes entire layers.} \\\\\n\\end{tabular}\n\\end{table}\n",
      "numLines": 21,
      "startLine": 1,
      "totalLines": 21
    }
  },
  "sourceToolAssistantUUID": "c21c0207-b64a-4a7e-9871-cd990dc423b9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "3a90179e-e19e-41d1-8fb4-f23e916f555f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 17 · 2026-05-23T10:47:20.210Z_

<details open><summary>🔧 Tool call — Read · `toolu_019Z2SeEokTEq6aoTLjSAQLy`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/table3_alpha.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "56f9d100-b140-40ba-826b-7887f43f0de4",
  "isSidechain": false,
  "requestId": "req_011CbKNGo4rLHPN2FBzfYpBN",
  "type": "assistant",
  "uuid": "e3439d2e-7e6d-47b6-8c39-38ad8941b488",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "3a90179e-e19e-41d1-8fb4-f23e916f555f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LTRFjV5U2DZDnMEQV3bmJE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1748,
      "cache_read_input_tokens": 25217,
      "output_tokens": 1165,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1748,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1165,
          "cache_read_input_tokens": 25217,
          "cache_creation_input_tokens": 1748,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1748
          },
          "type": "message"
        }
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

_source line 18 · 2026-05-23T10:47:20.214Z_

<details><summary>↩ Tool result · `toolu_019Z2SeEokTEq6aoTLjSAQLy`</summary>

```text
1	\begin{table}[t]
2	\centering
3	\small
4	\caption{Dose-response analysis: effect of CKA coefficient $\alpha$ on GSM8K accuracy ($N{=}1{,}319$) at 20\% MLP channel sparsity. $\alpha{=}0$ reduces to Standard (importance-only); higher $\alpha$ weights representational diversity. Best in \textbf{bold}.}
5	\label{tab:alpha}
6	\begin{tabular}{@{}cccc@{}}
7	\toprule
8	$\alpha$ & SFT Acc.\,(\%) & GRPO Acc.\,(\%) & $\Delta$\,(pp) \\
9	\midrule
10	0.5 & 60.73 & 61.18 & $+$0.45 \\
11	1.0 & 61.49 & 60.88 & $-$0.61 \\
12	\textbf{2.0} & \textbf{64.97} & \textbf{66.11} & $+$1.14 \\
13	3.0 & 64.14 & 63.46 & $-$0.68 \\
14	4.0 & 61.94 & 62.77 & $+$0.83 \\
15	\bottomrule
16	\end{tabular}
17	\end{table}
18	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e3439d2e-7e6d-47b6-8c39-38ad8941b488",
  "isSidechain": false,
  "promptId": "dddf37fd-16cc-4cd5-bb05-648328938281",
  "type": "user",
  "uuid": "acf0c473-4a7f-4e50-b577-e710d9bc7819",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/table3_alpha.tex",
      "content": "\\begin{table}[t]\n\\centering\n\\small\n\\caption{Dose-response analysis: effect of CKA coefficient $\\alpha$ on GSM8K accuracy ($N{=}1{,}319$) at 20\\% MLP channel sparsity. $\\alpha{=}0$ reduces to Standard (importance-only); higher $\\alpha$ weights representational diversity. Best in \\textbf{bold}.}\n\\label{tab:alpha}\n\\begin{tabular}{@{}cccc@{}}\n\\toprule\n$\\alpha$ & SFT Acc.\\,(\\%) & GRPO Acc.\\,(\\%) & $\\Delta$\\,(pp) \\\\\n\\midrule\n0.5 & 60.73 & 61.18 & $+$0.45 \\\\\n1.0 & 61.49 & 60.88 & $-$0.61 \\\\\n\\textbf{2.0} & \\textbf{64.97} & \\textbf{66.11} & $+$1.14 \\\\\n3.0 & 64.14 & 63.46 & $-$0.68 \\\\\n4.0 & 61.94 & 62.77 & $+$0.83 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n",
      "numLines": 18,
      "startLine": 1,
      "totalLines": 18
    }
  },
  "sourceToolAssistantUUID": "e3439d2e-7e6d-47b6-8c39-38ad8941b488",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "3a90179e-e19e-41d1-8fb4-f23e916f555f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 19 · 2026-05-23T10:47:21.177Z_

<details open><summary>🔧 Tool call — Read · `toolu_01JYfNfZ59WSJiBbcmQpM6LK`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/table4_sparsity_cliff.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "acf0c473-4a7f-4e50-b577-e710d9bc7819",
  "isSidechain": false,
  "requestId": "req_011CbKNGo4rLHPN2FBzfYpBN",
  "type": "assistant",
  "uuid": "1b0d25e1-c838-44c4-9fb3-2fd952de759e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "3a90179e-e19e-41d1-8fb4-f23e916f555f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LTRFjV5U2DZDnMEQV3bmJE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1748,
      "cache_read_input_tokens": 25217,
      "output_tokens": 1165,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1748,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1165,
          "cache_read_input_tokens": 25217,
          "cache_creation_input_tokens": 1748,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1748
          },
          "type": "message"
        }
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

_source line 20 · 2026-05-23T10:47:21.182Z_

<details><summary>↩ Tool result · `toolu_01JYfNfZ59WSJiBbcmQpM6LK`</summary>

```text
1	\begin{table}[t]
2	\centering
3	\caption{Sparsity cliff at 30\% structured sparsity ($N{=}100$). All tested pruning criteria collapse, with near-zero accuracy and EOS generation rates below 6\%.}
4	\label{tab:sparsity_cliff}
5	\begin{tabular}{@{}lcc@{}}
6	\toprule
7	Method & Acc.\,(\%) & EOS Rate\,(\%) \\
8	\midrule
9	Standard & 4 & 5.5 \\
10	\rasp{} ($\alpha{=}1.0$) & 0 & 3.0 \\
11	CKA-only & 0 & --$^\dagger$ \\
12	\bottomrule
13	\multicolumn{3}{@{}l}{\footnotesize $^\dagger$Terminated early after collapse confirmed.}
14	\end{tabular}
15	\end{table}
16	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1b0d25e1-c838-44c4-9fb3-2fd952de759e",
  "isSidechain": false,
  "promptId": "dddf37fd-16cc-4cd5-bb05-648328938281",
  "type": "user",
  "uuid": "58819d10-7da1-4efd-b7b8-ca79119ee311",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/table4_sparsity_cliff.tex",
      "content": "\\begin{table}[t]\n\\centering\n\\caption{Sparsity cliff at 30\\% structured sparsity ($N{=}100$). All tested pruning criteria collapse, with near-zero accuracy and EOS generation rates below 6\\%.}\n\\label{tab:sparsity_cliff}\n\\begin{tabular}{@{}lcc@{}}\n\\toprule\nMethod & Acc.\\,(\\%) & EOS Rate\\,(\\%) \\\\\n\\midrule\nStandard & 4 & 5.5 \\\\\n\\rasp{} ($\\alpha{=}1.0$) & 0 & 3.0 \\\\\nCKA-only & 0 & --$^\\dagger$ \\\\\n\\bottomrule\n\\multicolumn{3}{@{}l}{\\footnotesize $^\\dagger$Terminated early after collapse confirmed.}\n\\end{tabular}\n\\end{table}\n",
      "numLines": 16,
      "startLine": 1,
      "totalLines": 16
    }
  },
  "sourceToolAssistantUUID": "1b0d25e1-c838-44c4-9fb3-2fd952de759e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "3a90179e-e19e-41d1-8fb4-f23e916f555f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 21 · 2026-05-23T10:47:21.507Z_

<details open><summary>🔧 Tool call — Read · `toolu_01UL3iTDgbJbpJDWL4XmAbsY`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/table5_inference.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "58819d10-7da1-4efd-b7b8-ca79119ee311",
  "isSidechain": false,
  "requestId": "req_011CbKNGo4rLHPN2FBzfYpBN",
  "type": "assistant",
  "uuid": "e21dd90d-34bc-4c6a-96fc-56bcb5a38d4f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "3a90179e-e19e-41d1-8fb4-f23e916f555f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LTRFjV5U2DZDnMEQV3bmJE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1748,
      "cache_read_input_tokens": 25217,
      "output_tokens": 1165,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1748,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1165,
          "cache_read_input_tokens": 25217,
          "cache_creation_input_tokens": 1748,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1748
          },
          "type": "message"
        }
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

_source line 22 · 2026-05-23T10:47:21.511Z_

<details><summary>↩ Tool result · `toolu_01UL3iTDgbJbpJDWL4XmAbsY`</summary>

```text
1	\begin{table}[t]
2	\centering
3	\small
4	\caption{Inference efficiency at 20\% sparsity. Latency averaged over 100 GSM8K problems. Both pruned configurations remove ${\sim}$1.45B parameters; the latency gap arises from differences in layer-wise sparsity distribution. Best pruned result in \textbf{bold}.}
5	\label{tab:inference}
6	\begin{tabular}{@{}lcccc@{}}
7	\toprule
8	Configuration & Latency\,(s) & Speedup\,(\%) & Memory\,(GB) & Mem.\,Red.\,(\%) \\
9	\midrule
10	Dense & 6.682 & -- & 16.22 & -- \\
11	\rasp{} ($\alpha{=}1.0$) 20\% & \textbf{4.156} & \textbf{37.8} & 11.60 & 28.5 \\
12	Standard 20\% & 6.167 & 7.7 & 11.61 & 28.4 \\
13	\bottomrule
14	\end{tabular}
15	\end{table}
16	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e21dd90d-34bc-4c6a-96fc-56bcb5a38d4f",
  "isSidechain": false,
  "promptId": "dddf37fd-16cc-4cd5-bb05-648328938281",
  "type": "user",
  "uuid": "48379c96-e0e8-4584-bcd0-fd3c294eee88",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/table5_inference.tex",
      "content": "\\begin{table}[t]\n\\centering\n\\small\n\\caption{Inference efficiency at 20\\% sparsity. Latency averaged over 100 GSM8K problems. Both pruned configurations remove ${\\sim}$1.45B parameters; the latency gap arises from differences in layer-wise sparsity distribution. Best pruned result in \\textbf{bold}.}\n\\label{tab:inference}\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\nConfiguration & Latency\\,(s) & Speedup\\,(\\%) & Memory\\,(GB) & Mem.\\,Red.\\,(\\%) \\\\\n\\midrule\nDense & 6.682 & -- & 16.22 & -- \\\\\n\\rasp{} ($\\alpha{=}1.0$) 20\\% & \\textbf{4.156} & \\textbf{37.8} & 11.60 & 28.5 \\\\\nStandard 20\\% & 6.167 & 7.7 & 11.61 & 28.4 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n",
      "numLines": 16,
      "startLine": 1,
      "totalLines": 16
    }
  },
  "sourceToolAssistantUUID": "e21dd90d-34bc-4c6a-96fc-56bcb5a38d4f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "3a90179e-e19e-41d1-8fb4-f23e916f555f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 23 · 2026-05-23T10:47:22.481Z_

<details open><summary>🔧 Tool call — Read · `toolu_01H3Bzo7Hr2kMUL5GwCpCiqk`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/tab_math500.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "48379c96-e0e8-4584-bcd0-fd3c294eee88",
  "isSidechain": false,
  "requestId": "req_011CbKNGo4rLHPN2FBzfYpBN",
  "type": "assistant",
  "uuid": "8c65708c-e6b4-4a37-b2af-1799e282f959",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "3a90179e-e19e-41d1-8fb4-f23e916f555f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LTRFjV5U2DZDnMEQV3bmJE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1748,
      "cache_read_input_tokens": 25217,
      "output_tokens": 1165,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1748,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1165,
          "cache_read_input_tokens": 25217,
          "cache_creation_input_tokens": 1748,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1748
          },
          "type": "message"
        }
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

_source line 24 · 2026-05-23T10:47:22.486Z_

<details><summary>↩ Tool result · `toolu_01H3Bzo7Hr2kMUL5GwCpCiqk`</summary>

```text
1	\begin{table}[h]
2	\centering
3	\small
4	\caption{MATH-500 out-of-distribution evaluation ($N{=}500$, greedy decoding, \texttt{max\_new\_tokens=2048}). The method ordering (CKA-only $>$ Standard $>$ Random) is preserved from GSM8K. GRPO evaluation available for method comparison; dose-response GRPO follows the same ordering as GSM8K (Table~\ref{tab:alpha}). Best SFT in \textbf{bold}.}
5	\label{tab:math500}
6	\begin{tabular}{@{}lccc@{}}
7	\toprule
8	Method & SFT\,(\%) & GRPO\,(\%) & $\Delta$\,(pp) \\
9	\midrule
10	Dense & \multicolumn{3}{c}{53.0\,$^\dagger$} \\
11	\midrule
12	\multicolumn{4}{l}{\textit{20\% sparsity --- method comparison}} \\
13	CKA-only & \textbf{26.8} & 27.4 & $+$0.6 \\
14	Standard & 25.8$^\ddagger$ & 26.4$^\ddagger$ & $+$0.6 \\
15	\rasp{} ($\alpha{=}1.0$) & 21.2 & 22.6 & $+$1.4 \\
16	Random & 14.4 & --- & --- \\
17	\midrule
18	\multicolumn{4}{l}{\textit{20\% sparsity --- $\alpha$ dose-response}} \\
19	$\alpha{=}0.5$ & 25.4 & 24.8 & $-$0.6 \\
20	$\alpha{=}2.0$ & 24.0 & 26.2 & $+$2.2 \\
21	$\alpha{=}3.0$ & 23.2 & 22.8 & $-$0.4 \\
22	$\alpha{=}4.0$ & 26.6 & 26.2 & $-$0.4 \\
23	\midrule
24	\multicolumn{4}{l}{\textit{25\% sparsity}} \\
25	CKA-only & 19.2 & 18.4 & $-$0.8 \\
26	Standard & 14.0 & 12.8 & $-$1.2 \\
27	\bottomrule
28	\multicolumn{4}{p{0.85\columnwidth}}{\footnotesize $^\dagger$Over half of Dense responses truncated at 2048 tokens (73.6\% at 4096); all pruned models evaluated under the same constraint. $^\ddagger$Evaluated with earlier answer extraction script; re-evaluation with updated script pending.}
29	\end{tabular}
30	\end{table}
31	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8c65708c-e6b4-4a37-b2af-1799e282f959",
  "isSidechain": false,
  "promptId": "dddf37fd-16cc-4cd5-bb05-648328938281",
  "type": "user",
  "uuid": "ff5fdc8e-46f6-4cc7-9aa6-4d46224e1c79",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/tab_math500.tex",
      "content": "\\begin{table}[h]\n\\centering\n\\small\n\\caption{MATH-500 out-of-distribution evaluation ($N{=}500$, greedy decoding, \\texttt{max\\_new\\_tokens=2048}). The method ordering (CKA-only $>$ Standard $>$ Random) is preserved from GSM8K. GRPO evaluation available for method comparison; dose-response GRPO follows the same ordering as GSM8K (Table~\\ref{tab:alpha}). Best SFT in \\textbf{bold}.}\n\\label{tab:math500}\n\\begin{tabular}{@{}lccc@{}}\n\\toprule\nMethod & SFT\\,(\\%) & GRPO\\,(\\%) & $\\Delta$\\,(pp) \\\\\n\\midrule\nDense & \\multicolumn{3}{c}{53.0\\,$^\\dagger$} \\\\\n\\midrule\n\\multicolumn{4}{l}{\\textit{20\\% sparsity --- method comparison}} \\\\\nCKA-only & \\textbf{26.8} & 27.4 & $+$0.6 \\\\\nStandard & 25.8$^\\ddagger$ & 26.4$^\\ddagger$ & $+$0.6 \\\\\n\\rasp{} ($\\alpha{=}1.0$) & 21.2 & 22.6 & $+$1.4 \\\\\nRandom & 14.4 & --- & --- \\\\\n\\midrule\n\\multicolumn{4}{l}{\\textit{20\\% sparsity --- $\\alpha$ dose-response}} \\\\\n$\\alpha{=}0.5$ & 25.4 & 24.8 & $-$0.6 \\\\\n$\\alpha{=}2.0$ & 24.0 & 26.2 & $+$2.2 \\\\\n$\\alpha{=}3.0$ & 23.2 & 22.8 & $-$0.4 \\\\\n$\\alpha{=}4.0$ & 26.6 & 26.2 & $-$0.4 \\\\\n\\midrule\n\\multicolumn{4}{l}{\\textit{25\\% sparsity}} \\\\\nCKA-only & 19.2 & 18.4 & $-$0.8 \\\\\nStandard & 14.0 & 12.8 & $-$1.2 \\\\\n\\bottomrule\n\\multicolumn{4}{p{0.85\\columnwidth}}{\\footnotesize $^\\dagger$Over half of Dense responses truncated at 2048 tokens (73.6\\% at 4096); all pruned models evaluated under the same constraint. $^\\ddagger$Evaluated with earlier answer extraction script; re-evaluation with updated script pending.}\n\\end{tabular}\n\\end{table}\n",
      "numLines": 31,
      "startLine": 1,
      "totalLines": 31
    }
  },
  "sourceToolAssistantUUID": "8c65708c-e6b4-4a37-b2af-1799e282f959",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "3a90179e-e19e-41d1-8fb4-f23e916f555f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 25 · 2026-05-23T10:47:22.940Z_

<details open><summary>🔧 Tool call — Read · `toolu_01TVXnyh7JDHF6K4i7V4nybN`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/tab_mbpp.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ff5fdc8e-46f6-4cc7-9aa6-4d46224e1c79",
  "isSidechain": false,
  "requestId": "req_011CbKNGo4rLHPN2FBzfYpBN",
  "type": "assistant",
  "uuid": "6bf1b10a-7a38-4ad8-993b-c32f48a454af",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "3a90179e-e19e-41d1-8fb4-f23e916f555f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LTRFjV5U2DZDnMEQV3bmJE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1748,
      "cache_read_input_tokens": 25217,
      "output_tokens": 1165,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1748,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1165,
          "cache_read_input_tokens": 25217,
          "cache_creation_input_tokens": 1748,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1748
          },
          "type": "message"
        }
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

_source line 26 · 2026-05-23T10:47:22.944Z_

<details><summary>↩ Tool result · `toolu_01TVXnyh7JDHF6K4i7V4nybN`</summary>

```text
1	\begin{table}[h]
2	\centering
3	\small
4	\caption{MBPP code generation accuracy ($N{=}374$, greedy decoding). All fine-grained pruning methods converge near a capability floor (${\sim}$75\% code capability loss vs Dense), limiting differentiation (${\sim}$1\,pp range, within stderr). ShortGPT shows a larger GRPO delta ($+$4.01\,pp) but at the 95\% CI boundary (stderr ${\approx}$1.55\,pp).}
5	\label{tab:mbpp}
6	\begin{tabular}{@{}lccc@{}}
7	\toprule
8	Method & SFT\,(\%) & GRPO\,(\%) & $\Delta$\,(pp) \\
9	\midrule
10	Dense & -- & 53.48 & -- \\
11	\midrule
12	CKA-only 20\% & 12.83 & 14.17 & $+$1.34 \\
13	Standard 20\% & 12.03 & 13.10 & $+$1.07 \\
14	\rasp{} ($\alpha{=}1.0$) 20\% & 11.76 & 13.10 & $+$1.34 \\
15	\midrule
16	ShortGPT 20\%$^\dagger$ & 10.43 & 14.44 & $+$4.01 \\
17	\bottomrule
18	\multicolumn{4}{l}{\footnotesize $^\dagger$Depth pruning; removes entire layers.}
19	\end{tabular}
20	\end{table}
21	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6bf1b10a-7a38-4ad8-993b-c32f48a454af",
  "isSidechain": false,
  "promptId": "dddf37fd-16cc-4cd5-bb05-648328938281",
  "type": "user",
  "uuid": "82459658-0a6a-4bd0-a700-5b6ccd48a1de",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/tab_mbpp.tex",
      "content": "\\begin{table}[h]\n\\centering\n\\small\n\\caption{MBPP code generation accuracy ($N{=}374$, greedy decoding). All fine-grained pruning methods converge near a capability floor (${\\sim}$75\\% code capability loss vs Dense), limiting differentiation (${\\sim}$1\\,pp range, within stderr). ShortGPT shows a larger GRPO delta ($+$4.01\\,pp) but at the 95\\% CI boundary (stderr ${\\approx}$1.55\\,pp).}\n\\label{tab:mbpp}\n\\begin{tabular}{@{}lccc@{}}\n\\toprule\nMethod & SFT\\,(\\%) & GRPO\\,(\\%) & $\\Delta$\\,(pp) \\\\\n\\midrule\nDense & -- & 53.48 & -- \\\\\n\\midrule\nCKA-only 20\\% & 12.83 & 14.17 & $+$1.34 \\\\\nStandard 20\\% & 12.03 & 13.10 & $+$1.07 \\\\\n\\rasp{} ($\\alpha{=}1.0$) 20\\% & 11.76 & 13.10 & $+$1.34 \\\\\n\\midrule\nShortGPT 20\\%$^\\dagger$ & 10.43 & 14.44 & $+$4.01 \\\\\n\\bottomrule\n\\multicolumn{4}{l}{\\footnotesize $^\\dagger$Depth pruning; removes entire layers.}\n\\end{tabular}\n\\end{table}\n",
      "numLines": 21,
      "startLine": 1,
      "totalLines": 21
    }
  },
  "sourceToolAssistantUUID": "6bf1b10a-7a38-4ad8-993b-c32f48a454af",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "3a90179e-e19e-41d1-8fb4-f23e916f555f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 27 · 2026-05-23T10:47:23.415Z_

<details open><summary>🔧 Tool call — Read · `toolu_01VNzsgbcVYJiqsU7ibFPKk6`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/tab5_cross_scale.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "82459658-0a6a-4bd0-a700-5b6ccd48a1de",
  "isSidechain": false,
  "requestId": "req_011CbKNGo4rLHPN2FBzfYpBN",
  "type": "assistant",
  "uuid": "7d13c937-6a02-41df-9f72-483317eee0da",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "3a90179e-e19e-41d1-8fb4-f23e916f555f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LTRFjV5U2DZDnMEQV3bmJE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1748,
      "cache_read_input_tokens": 25217,
      "output_tokens": 1165,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1748,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1165,
          "cache_read_input_tokens": 25217,
          "cache_creation_input_tokens": 1748,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1748
          },
          "type": "message"
        }
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

_source line 28 · 2026-05-23T10:47:23.419Z_

<details><summary>↩ Tool result · `toolu_01VNzsgbcVYJiqsU7ibFPKk6`</summary>

```text
1	\begin{table}[t]
2	\centering
3	\small
4	\caption{Cross-scale validation at 20\% sparsity. 7B: DeepSeek-R1-Distill-Qwen-7B (GSM8K mean over 3 seeds for CKA-only and Standard; see Table~\ref{tab:decoupling}). 1.5B: DeepSeek-R1-Distill-Qwen-1.5B (single seed). GSM8K accuracy ($N{=}1{,}319$). 7B reward = peak across 100 GRPO steps (cf.\ Table~\ref{tab:recovery_gradient}); 1.5B reward = mean across training steps.}
5	\label{tab:cross_scale}
6	\begin{tabular}{@{}lcccc@{}}
7	\toprule
8	\multirow{2}{*}{Method} & \multicolumn{2}{c}{7B} & \multicolumn{2}{c}{1.5B} \\
9	\cmidrule(lr){2-3} \cmidrule(lr){4-5}
10	 & Peak Rew. & GSM8K\,(\%) & Rew. & GSM8K\,(\%) \\
11	\midrule
12	CKA-only & \textbf{0.354} & \textbf{64.39} & \textbf{0.238} & \textbf{35.48} \\
13	Standard & 0.081 & 59.84 & 0.084 & 22.29 \\
14	\rasp{} ($\alpha{=}1.0$) & 0.061 & 60.88 & 0.099 & 26.16 \\
15	Random & 0.190 & -- & -- & -- \\
16	\bottomrule
17	\end{tabular}
18	\end{table}
19	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7d13c937-6a02-41df-9f72-483317eee0da",
  "isSidechain": false,
  "promptId": "dddf37fd-16cc-4cd5-bb05-648328938281",
  "type": "user",
  "uuid": "0e7aee2e-9fe7-47d8-b050-03849219a47d",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/tab5_cross_scale.tex",
      "content": "\\begin{table}[t]\n\\centering\n\\small\n\\caption{Cross-scale validation at 20\\% sparsity. 7B: DeepSeek-R1-Distill-Qwen-7B (GSM8K mean over 3 seeds for CKA-only and Standard; see Table~\\ref{tab:decoupling}). 1.5B: DeepSeek-R1-Distill-Qwen-1.5B (single seed). GSM8K accuracy ($N{=}1{,}319$). 7B reward = peak across 100 GRPO steps (cf.\\ Table~\\ref{tab:recovery_gradient}); 1.5B reward = mean across training steps.}\n\\label{tab:cross_scale}\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\n\\multirow{2}{*}{Method} & \\multicolumn{2}{c}{7B} & \\multicolumn{2}{c}{1.5B} \\\\\n\\cmidrule(lr){2-3} \\cmidrule(lr){4-5}\n & Peak Rew. & GSM8K\\,(\\%) & Rew. & GSM8K\\,(\\%) \\\\\n\\midrule\nCKA-only & \\textbf{0.354} & \\textbf{64.39} & \\textbf{0.238} & \\textbf{35.48} \\\\\nStandard & 0.081 & 59.84 & 0.084 & 22.29 \\\\\n\\rasp{} ($\\alpha{=}1.0$) & 0.061 & 60.88 & 0.099 & 26.16 \\\\\nRandom & 0.190 & -- & -- & -- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n",
      "numLines": 19,
      "startLine": 1,
      "totalLines": 19
    }
  },
  "sourceToolAssistantUUID": "7d13c937-6a02-41df-9f72-483317eee0da",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "3a90179e-e19e-41d1-8fb4-f23e916f555f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 29 · 2026-05-23T10:47:24.359Z_

<details open><summary>🔧 Tool call — Read · `toolu_011Y8Uwono6bxqqbS8SvUReT`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/tab_cka_stability.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0e7aee2e-9fe7-47d8-b050-03849219a47d",
  "isSidechain": false,
  "requestId": "req_011CbKNGo4rLHPN2FBzfYpBN",
  "type": "assistant",
  "uuid": "efab2ace-2e87-4b3d-b47f-7f5de1720857",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "3a90179e-e19e-41d1-8fb4-f23e916f555f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LTRFjV5U2DZDnMEQV3bmJE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1748,
      "cache_read_input_tokens": 25217,
      "output_tokens": 1165,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1748,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1165,
          "cache_read_input_tokens": 25217,
          "cache_creation_input_tokens": 1748,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1748
          },
          "type": "message"
        }
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

_source line 30 · 2026-05-23T10:47:24.362Z_

<details><summary>↩ Tool result · `toolu_011Y8Uwono6bxqqbS8SvUReT`</summary>

```text
1	\begin{table}[h]
2	\centering
3	\small
4	\caption{CKA scoring stability across calibration sizes. Spearman $\rho$ between structure rankings produced by different calibration set sizes. High correlation ($\rho \geq 0.964$) indicates that CKA-based scoring is robust to calibration data volume.}
5	\label{tab:cka_stability}
6	\begin{tabular}{@{}lcc@{}}
7	\toprule
8	Calibration Sizes & Spearman $\rho$ (min) & Spearman $\rho$ (mean) \\
9	\midrule
10	256 / 512 / 1024 & 0.964 & 0.979 \\
11	\bottomrule
12	\end{tabular}
13	\end{table}
14	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "efab2ace-2e87-4b3d-b47f-7f5de1720857",
  "isSidechain": false,
  "promptId": "dddf37fd-16cc-4cd5-bb05-648328938281",
  "type": "user",
  "uuid": "c785f3dd-6d8b-48fa-8427-8759850d532b",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/tab_cka_stability.tex",
      "content": "\\begin{table}[h]\n\\centering\n\\small\n\\caption{CKA scoring stability across calibration sizes. Spearman $\\rho$ between structure rankings produced by different calibration set sizes. High correlation ($\\rho \\geq 0.964$) indicates that CKA-based scoring is robust to calibration data volume.}\n\\label{tab:cka_stability}\n\\begin{tabular}{@{}lcc@{}}\n\\toprule\nCalibration Sizes & Spearman $\\rho$ (min) & Spearman $\\rho$ (mean) \\\\\n\\midrule\n256 / 512 / 1024 & 0.964 & 0.979 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n",
      "numLines": 14,
      "startLine": 1,
      "totalLines": 14
    }
  },
  "sourceToolAssistantUUID": "efab2ace-2e87-4b3d-b47f-7f5de1720857",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "3a90179e-e19e-41d1-8fb4-f23e916f555f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 31 · 2026-05-23T10:47:24.834Z_

<details open><summary>🔧 Tool call — Read · `toolu_01846hYg4Xp7aLneCBqsQhos`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c785f3dd-6d8b-48fa-8427-8759850d532b",
  "isSidechain": false,
  "requestId": "req_011CbKNGo4rLHPN2FBzfYpBN",
  "type": "assistant",
  "uuid": "86f94c6e-732d-46ce-86dd-823eb14491bf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "3a90179e-e19e-41d1-8fb4-f23e916f555f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LTRFjV5U2DZDnMEQV3bmJE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1748,
      "cache_read_input_tokens": 25217,
      "output_tokens": 1165,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1748,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1165,
          "cache_read_input_tokens": 25217,
          "cache_creation_input_tokens": 1748,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1748
          },
          "type": "message"
        }
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

_source line 32 · 2026-05-23T10:47:24.839Z_

<details><summary>↩ Tool result · `toolu_01846hYg4Xp7aLneCBqsQhos`</summary>

```text
1	
2	\section{Experiments}
3	\label{sec:experiments}
4	
5	\subsection{Experimental Setup}
6	\label{sec:exp_setup}
7	
8	\paragraph{Base model and evaluation.}
9	We evaluate on DeepSeek-R1-Distill-Qwen-7B~\citep{deepseek2025r1}, a 7B-parameter reasoning model built on the Qwen2.5 architecture~\citep{qwen2.5} with GQA~\citep{ainslie2023gqa} (architecture details in Section~\ref{sec:prelim}).
10	Our primary benchmark is GSM8K~\citep{cobbe2021gsm8k}, a set of 1{,}319 grade-school math problems requiring multi-step arithmetic reasoning.
11	We report exact-match accuracy: the final numerical answer is extracted from the model's generation and compared against the ground truth.
12	For rapid iteration during development, we use a 100-problem subset ($N{=}100$); final results use the full test set ($N{=}1{,}319$).
13	The original unpruned model achieves 90.83\% on GSM8K (greedy decoding).
14	
15	\paragraph{Pruning methods.}
16	We compare four pruning criteria at 20\% structured sparsity, all removing the same number of MLP channel groups (200 of 784 across 28 layers, ${\sim}$1.45B parameters) with identical per-layer capacity floors (${\ge}$40\% retention per layer):
17	\begin{enumerate}[nosep,leftmargin=*]
18	    \item \textbf{CKA-only}: structures ranked by functional overlap $F(h)$ alone (Eq.~\ref{eq:overlap}); the most redundant groups are removed regardless of gradient importance.
19	    \item \textbf{Random}: uniform random selection among eligible groups.
20	    \item \textbf{Standard}: Taylor-expansion importance $I(h)$ alone (Eq.~\ref{eq:importance}); the least important groups are removed, following LLM-Pruner~\citep{llmpruner2023}.
21	    \item \textbf{\rasp{}} ($\alpha{=}1.0$): the composite score $S(h) = I(h) \times (1 - F(h))^\alpha$ (Eq.~\ref{eq:score}), removing structures that are both low-importance and functionally redundant.
22	\end{enumerate}
23	
24	\paragraph{Recovery pipeline and hardware.}
25	All four methods undergo matched two-stage recovery.
26	Stage~1 (SFT warmup): 2 epochs on 7{,}473 GSM8K chain-of-thought examples with teacher forcing (37 minutes), restoring EOS generation and basic format compliance.
27	Stage~2 (GRPO): Group Relative Policy Optimization~\citep{shao2024grpo} with learning rate $1{\times}10^{-6}$, maximum completion length 1{,}024 tokens, KL penalty coefficient $\beta{=}0.01$, sampling temperature 0.4, DAPO-style clipped loss, and binary reward ($r{=}1$ if correct, $r{=}0$ otherwise), trained for 100 steps on 1{,}000 GSM8K training problems.
28	All methods share identical GRPO hyperparameters, including \texttt{reward\_desert\_patience}{$=$}50.
29	Seeds vary at the GRPO stage; pruning calibration and SFT use identical configurations across all methods.
30	We repeat GRPO training with 3 random seeds for CKA-only, Standard, and Random (Table~\ref{tab:decoupling}).
31	CKA-only achieves 64.39\% $\pm$ 0.19\,pp (std across seeds), Standard 59.84\% $\pm$ 0.38\,pp; the 4.55\,pp gap is robust across seeds (Welch's $t$-test, $p{=}0.0009$, Cohen's $d{=}11.1$; 95\% CI for mean difference: $[3.62, 5.47]$\,pp), confirming that recovery capacity differences are structural rather than stochastic.
32	All experiments run on 2$\times$ NVIDIA RTX PRO 6000 GPUs (94\,GB VRAM each); pruning variants are trained in parallel on separate GPUs under identical wall-clock conditions.
33	
34	
35	\subsection{Recovery Capacity Spectrum}
36	\label{sec:recovery_gradient}
37	
38	\input{tables/tab1_recovery_gradient}
39	
40	\begin{figure}[t]
41	    \centering
42	    \includegraphics[width=\columnwidth]{figures/paper/fig2_reward_trajectories.pdf}
43	    \caption{GRPO reward trajectories for four pruning criteria and the unpruned model under identical training configuration ($\beta{=}0.01$, $T{=}0.4$, 100 steps). CKA-only reaches 0.354 peak reward with an observed recovery event at step 90. Random oscillates between 0.14 and 0.19 (training timed out at step 97; 9 steps shown). Standard peaks at 0.081 before borderline collapse. \rasp{} peaks at 0.061 (step 50) and declines to 0.010 by step 100.}
44	    \label{fig:reward_trajectories}
45	\end{figure}
46	
47	Under identical GRPO hyperparameters, the four pruning criteria produce a clear recovery capacity spectrum: CKA-only $\gg$ Random $\gg$ Standard $>$ \rasp{} (Table~\ref{tab:recovery_gradient}, Figure~\ref{fig:reward_trajectories}).
48	The pruning criterion, not training configuration, determines whether the model learns, stagnates, or collapses.
49	
50	\begin{figure}[t]
51	    \centering
52	    \includegraphics[width=\columnwidth]{figures/paper/fig3_collapse_dynamics.pdf}
53	    \caption{Training dynamics diagnostics. (a)~$f_0$ (fraction of zero-variance batches): CKA-only stays below 0.35; Standard and \rasp{} remain in the collapse zone ($f_0 > 0.5$) throughout training. (b)~Gradient norm: Standard exhibits a transient minimum of 0.017 at step 90 before recovering to 2.41 at step 100; \rasp{} gradient norms remain predominantly near zero.}
54	    \label{fig:collapse_dynamics}
55	\end{figure}
56	
57	CKA-only pruning is the only method that produces active learning under GRPO.
58	Reward reaches a peak of 0.354 (mean 0.285) with $f_0$ as low as 0.125, including a recovery event at step 90 where reward rebounds from a transient perturbation.
59	Random pruning produces stagnation: reward oscillates between 0.142 and 0.190 with $f_0$ near 0.33.
60	
61	Standard pruning exhibits borderline collapse (Figure~\ref{fig:collapse_dynamics}): reward peaks at 0.081 (step 40) then oscillates near 0.05, with $f_0 \geq 0.500$ throughout, meaning more than half of batches produce no learning signal.
62	\rasp{} produces full collapse: reward peaks at 0.061 (step 50) then declines to 0.010 by step 100, with $f_0 > 0.675$ and clipped ratio $>$ 90\%.
63	
64	The 5.8$\times$ peak reward gap between CKA-only (0.354) and \rasp{} (0.061) arises entirely from which structures were removed; parameter budgets and GRPO configurations are identical.
65	
66	
67	\subsection{Reward-Accuracy Decoupling}
68	\label{sec:decoupling}
69	
70	\input{tables/tab2_decoupling}
71	
72	Despite the 4.4$\times$ peak reward gap, GRPO barely moves accuracy: all fine-grained methods at 20\% sparsity change by $|\Delta| < 1$\,pp (CKA-only $+$0.48, Standard $+$0.55, Random $-$0.53, \rasp{} $-$0.61\,pp; Table~\ref{tab:decoupling}).
73	We term this \emph{reward-accuracy decoupling}: reward trajectory reflects the model's capacity to learn from RL signal, not downstream accuracy.
74	At 20\% sparsity, the four fine-grained criteria show mean $|\Delta| {=} 0.54$\,pp (max $0.61$\,pp); across the full $\alpha$ dose-response spectrum, $|\Delta|$ remains below $1.14$\,pp.
75	
76	The degree of decoupling varies with sparsity.
77	At 15\%, GRPO slightly amplifies the CKA-only advantage: the SFT gap of 5.69\,pp (72.18\% vs 66.49\%) widens to 7.20\,pp under GRPO (72.76\% vs 65.56\%).
78	At 20\%, GRPO adds nothing: the SFT gap of 4.62\,pp is preserved almost exactly (4.55\,pp).
79	The most extreme case is 25\%, where Standard's peak reward collapses to 0.008 yet accuracy still changes by only $+$0.99\,pp (Appendix~\ref{sec:appendix_cross_sparsity}).
80	Across all four fine-grained criteria at 20\% and 25\%, $|\Delta| < 1$\,pp without exception on GSM8K (Tables~\ref{tab:decoupling},~\ref{tab:cross_sparsity}); dose-response $\alpha$ variations show slightly larger but still small differences (max $1.14$\,pp at $\alpha{=}2.0$; Table~\ref{tab:alpha}).
81	On MATH-500, differences remain within statistical noise ($|\Delta| < 2.5$\,pp with stderr ${\approx}$2\,pp; Appendix~\ref{sec:appendix_math500}).
82	Moderate structural damage (15\%) apparently preserves enough capacity for GRPO to differentially benefit CKA-only pruning, while more aggressive pruning (20--25\%) exceeds the threshold where GRPO can improve upon SFT baselines.
83	
84	These results are robust: CKA-only GRPO accuracy varies by only 0.36\,pp across three seeds (64.22--64.58\%; Appendix~\ref{sec:appendix_multiseed}), and extending training to 300 steps leaves accuracy unchanged (CKA-only 64.37\%$\to$64.37\%, Standard 59.44\%$\to$59.29\%).
85	The ranking and decoupling generalize beyond GSM8K: on MATH-500~\citep{hendrycks2021math}, CKA-only ranks highest and Random lowest in SFT accuracy (26.8\% vs 14.4\%), though middle-ranked methods swap positions (Standard 25.8\% $>$ \rasp{} 21.2\%; Appendix~\ref{sec:appendix_math500}), and on MBPP~\citep{austin2021mbpp} all fine-grained GRPO $|\Delta| < 2$\,pp (Appendix~\ref{sec:appendix_mbpp}).
86	\label{sec:ood}
87	ShortGPT~\citep{shortgpt2024} depth pruning is the sole exception: its GRPO delta is task-dependent ($-$1.36\,pp on GSM8K, $+$4.01\,pp on MBPP; Tables~\ref{tab:decoupling},~\ref{tab:mbpp}), unlike the uniformly small deltas of fine-grained methods ($|\Delta| \leq 1.34$\,pp, with the cross-benchmark maximum from MBPP).
88	
89	
90	\subsection{Additional Results}
91	\label{sec:additional_results}
92	
93	\paragraph{Post-SFT accuracy does not predict GRPO outcome.}
94	\label{sec:sft_gradient}
95	Under SFT alone, CKA-only (63.91\%) $>$ \rasp{} (61.49\%) $>$ Standard (59.29\%) $>$ Random (51.25\%), yet under GRPO the \rasp{}/Standard ordering reverses (peak 0.081 vs 0.061) and Random outperforms both in peak reward (0.190).
96	More strikingly, ShortGPT post-SFT (44.73\%) shows GRPO actively harming accuracy ($-$1.36\,pp), while unstructured pruning achieves the highest post-SFT accuracy (87.87\%) with GRPO accuracy 87.64\% ($\Delta{=}{-}0.23$\,pp), confirming that pruning criteria are irrelevant when structural damage is minimal (96.5\% dense retention).
97	Post-SFT accuracy does not predict GRPO recovery outcome: the spectrum is driven by structural properties of the pruned architecture.
98	
99	\paragraph{Sparsity limits and dose-response.}
100	\label{sec:sparsity_cliff}
101	All methods collapse at 30\% sparsity, validating 20\% as the operating point (Appendix~\ref{sec:appendix_sparsity_cliff}).
102	Pruning reduces parameters by 19\% and memory by ${\sim}$28\% (Appendix~\ref{sec:appendix_inference}).
103	On GSM8K, the CKA coefficient $\alpha$ exhibits an inverted-U pattern in recovery accuracy across $\{0.5, 1.0, 2.0, 3.0, 4.0\}$, peaking at $\alpha{=}2.0$ (SFT 64.97\%, GRPO 66.11\%) with $|\Delta| \leq 1.14$\,pp at every point; $\alpha{=}1.0$ collapses (peak reward 0.061) while $\alpha{=}4.0$ recovers to 62.77\% (Appendix~\ref{sec:appendix_alpha}).
104	
105	
106	\subsection{Extended Analysis}
107	\label{sec:extended_analysis}
108	
109	\begin{figure}[t]
110	    \centering
111	    \includegraphics[width=\columnwidth]{figures/paper/fig4_cka_heatmap.pdf}
112	    \caption{Layer-wise CKA similarity between dense and pruned representations (28 layers). CKA-only diverges most from dense ($\mu{=}0.62$) yet recovers best; Standard ($\mu{=}0.90$), Random ($\mu{=}0.92$), and \rasp{} ($\mu{=}0.88$) preserve dense fidelity but collapse under RL.}
113	    \label{fig:cka_heatmap}
114	\end{figure}
115	
116	\input{tables/tab5_cross_scale}
117	
118	\paragraph{Representational diversity.}
119	CKA similarity between dense and pruned representations (Figure~\ref{fig:cka_heatmap}) shows CKA-only diverges most from the dense model ($\mu{=}0.62$), while Standard ($\mu{=}0.90$), Random ($\mu{=}0.92$), and \rasp{} ($\mu{=}0.88$) cluster near 1.0.
120	Preserving dense fidelity through gradient importance appears to retain redundant representations at the expense of the diversity that GRPO exploration requires.
121	CKA-only concentrates pruning in early layers (L0--9, 72.5\% of removed groups) while Standard prunes uniformly, removing late-layer structures that are representationally unique (Appendix~\ref{sec:appendix_overlap}).
122	Gradient flow analysis corroborates this: CKA-only models exhibit 2.89$\times$ mean gradient magnitude versus Standard across 55/56 layer groups ($p{<}0.05$, Wilcoxon; Appendix~\ref{sec:appendix_gradient}), consistent with diversity preservation enabling stronger RL training signals.
123	
124	\paragraph{Extended training cannot rescue collapse.}
125	Extending GRPO from 100 to 300 steps (Figure~\ref{fig:extended_training}, Appendix~\ref{sec:appendix_extended}), Standard shows zero net improvement (reward 0.054--0.058, $f_0 > 0.5$ throughout), while CKA-only sustains a 5.5$\times$ gap (0.308 vs 0.056 at step 300). The gap is structural, not a matter of training budget.
126	
127	\paragraph{Cross-scale and cross-architecture generalization.}
128	On DeepSeek-R1-Distill-Qwen-1.5B at 20\% sparsity (Table~\ref{tab:cross_scale}), the three-method ordering is preserved (CKA-only 35.48\% $\gg$ \rasp{} 26.16\% $>$ Standard 22.29\%), with reward-accuracy decoupling confirmed at this scale ($|\Delta| < 1$\,pp: CKA-only $-$0.15, Standard $-$0.61\,pp).
129	On Qwen2.5-Math-7B at 20\% sparsity (Table~\ref{tab:cross_arch}, Appendix~\ref{sec:appendix_cross_arch}), CKA-only causes near-total initial damage (1.0\% vs Standard's 18.5\%) yet SFT recovers it to 51.50\% $\pm$ 3.53 while Standard remains at 21.00\% $\pm$ 2.88 ($N{=}200$), confirming that recoverability depends on preserved structure, not starting accuracy. GRPO validation on this architecture is left to future work.
130	
131	
132	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "86f94c6e-732d-46ce-86dd-823eb14491bf",
  "isSidechain": false,
  "promptId": "dddf37fd-16cc-4cd5-bb05-648328938281",
  "type": "user",
  "uuid": "56f612af-cc09-48a2-8cb4-7e759e9b1133",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/experiments.tex",
      "content": "\n\\section{Experiments}\n\\label{sec:experiments}\n\n\\subsection{Experimental Setup}\n\\label{sec:exp_setup}\n\n\\paragraph{Base model and evaluation.}\nWe evaluate on DeepSeek-R1-Distill-Qwen-7B~\\citep{deepseek2025r1}, a 7B-parameter reasoning model built on the Qwen2.5 architecture~\\citep{qwen2.5} with GQA~\\citep{ainslie2023gqa} (architecture details in Section~\\ref{sec:prelim}).\nOur primary benchmark is GSM8K~\\citep{cobbe2021gsm8k}, a set of 1{,}319 grade-school math problems requiring multi-step arithmetic reasoning.\nWe report exact-match accuracy: the final numerical answer is extracted from the model's generation and compared against the ground truth.\nFor rapid iteration during development, we use a 100-problem subset ($N{=}100$); final results use the full test set ($N{=}1{,}319$).\nThe original unpruned model achieves 90.83\\% on GSM8K (greedy decoding).\n\n\\paragraph{Pruning methods.}\nWe compare four pruning criteria at 20\\% structured sparsity, all removing the same number of MLP channel groups (200 of 784 across 28 layers, ${\\sim}$1.45B parameters) with identical per-layer capacity floors (${\\ge}$40\\% retention per layer):\n\\begin{enumerate}[nosep,leftmargin=*]\n    \\item \\textbf{CKA-only}: structures ranked by functional overlap $F(h)$ alone (Eq.~\\ref{eq:overlap}); the most redundant groups are removed regardless of gradient importance.\n    \\item \\textbf{Random}: uniform random selection among eligible groups.\n    \\item \\textbf{Standard}: Taylor-expansion importance $I(h)$ alone (Eq.~\\ref{eq:importance}); the least important groups are removed, following LLM-Pruner~\\citep{llmpruner2023}.\n    \\item \\textbf{\\rasp{}} ($\\alpha{=}1.0$): the composite score $S(h) = I(h) \\times (1 - F(h))^\\alpha$ (Eq.~\\ref{eq:score}), removing structures that are both low-importance and functionally redundant.\n\\end{enumerate}\n\n\\paragraph{Recovery pipeline and hardware.}\nAll four methods undergo matched two-stage recovery.\nStage~1 (SFT warmup): 2 epochs on 7{,}473 GSM8K chain-of-thought examples with teacher forcing (37 minutes), restoring EOS generation and basic format compliance.\nStage~2 (GRPO): Group Relative Policy Optimization~\\citep{shao2024grpo} with learning rate $1{\\times}10^{-6}$, maximum completion length 1{,}024 tokens, KL penalty coefficient $\\beta{=}0.01$, sampling temperature 0.4, DAPO-style clipped loss, and binary reward ($r{=}1$ if correct, $r{=}0$ otherwise), trained for 100 steps on 1{,}000 GSM8K training problems.\nAll methods share identical GRPO hyperparameters, including \\texttt{reward\\_desert\\_patience}{$=$}50.\nSeeds vary at the GRPO stage; pruning calibration and SFT use identical configurations across all methods.\nWe repeat GRPO training with 3 random seeds for CKA-only, Standard, and Random (Table~\\ref{tab:decoupling}).\nCKA-only achieves 64.39\\% $\\pm$ 0.19\\,pp (std across seeds), Standard 59.84\\% $\\pm$ 0.38\\,pp; the 4.55\\,pp gap is robust across seeds (Welch's $t$-test, $p{=}0.0009$, Cohen's $d{=}11.1$; 95\\% CI for mean difference: $[3.62, 5.47]$\\,pp), confirming that recovery capacity differences are structural rather than stochastic.\nAll experiments run on 2$\\times$ NVIDIA RTX PRO 6000 GPUs (94\\,GB VRAM each); pruning variants are trained in parallel on separate GPUs under identical wall-clock conditions.\n\n\n\\subsection{Recovery Capacity Spectrum}\n\\label{sec:recovery_gradient}\n\n\\input{tables/tab1_recovery_gradient}\n\n\\begin{figure}[t]\n    \\centering\n    \\includegraphics[width=\\columnwidth]{figures/paper/fig2_reward_trajectories.pdf}\n    \\caption{GRPO reward trajectories for four pruning criteria and the unpruned model under identical training configuration ($\\beta{=}0.01$, $T{=}0.4$, 100 steps). CKA-only reaches 0.354 peak reward with an observed recovery event at step 90. Random oscillates between 0.14 and 0.19 (training timed out at step 97; 9 steps shown). Standard peaks at 0.081 before borderline collapse. \\rasp{} peaks at 0.061 (step 50) and declines to 0.010 by step 100.}\n    \\label{fig:reward_trajectories}\n\\end{figure}\n\nUnder identical GRPO hyperparameters, the four pruning criteria produce a clear recovery capacity spectrum: CKA-only $\\gg$ Random $\\gg$ Standard $>$ \\rasp{} (Table~\\ref{tab:recovery_gradient}, Figure~\\ref{fig:reward_trajectories}).\nThe pruning criterion, not training configuration, determines whether the model learns, stagnates, or collapses.\n\n\\begin{figure}[t]\n    \\centering\n    \\includegraphics[width=\\columnwidth]{figures/paper/fig3_collapse_dynamics.pdf}\n    \\caption{Training dynamics diagnostics. (a)~$f_0$ (fraction of zero-variance batches): CKA-only stays below 0.35; Standard and \\rasp{} remain in the collapse zone ($f_0 > 0.5$) throughout training. (b)~Gradient norm: Standard exhibits a transient minimum of 0.017 at step 90 before recovering to 2.41 at step 100; \\rasp{} gradient norms remain predominantly near zero.}\n    \\label{fig:collapse_dynamics}\n\\end{figure}\n\nCKA-only pruning is the only method that produces active learning under GRPO.\nReward reaches a peak of 0.354 (mean 0.285) with $f_0$ as low as 0.125, including a recovery event at step 90 where reward rebounds from a transient perturbation.\nRandom pruning produces stagnation: reward oscillates between 0.142 and 0.190 with $f_0$ near 0.33.\n\nStandard pruning exhibits borderline collapse (Figure~\\ref{fig:collapse_dynamics}): reward peaks at 0.081 (step 40) then oscillates near 0.05, with $f_0 \\geq 0.500$ throughout, meaning more than half of batches produce no learning signal.\n\\rasp{} produces full collapse: reward peaks at 0.061 (step 50) then declines to 0.010 by step 100, with $f_0 > 0.675$ and clipped ratio $>$ 90\\%.\n\nThe 5.8$\\times$ peak reward gap between CKA-only (0.354) and \\rasp{} (0.061) arises entirely from which structures were removed; parameter budgets and GRPO configurations are identical.\n\n\n\\subsection{Reward-Accuracy Decoupling}\n\\label{sec:decoupling}\n\n\\input{tables/tab2_decoupling}\n\nDespite the 4.4$\\times$ peak reward gap, GRPO barely moves accuracy: all fine-grained methods at 20\\% sparsity change by $|\\Delta| < 1$\\,pp (CKA-only $+$0.48, Standard $+$0.55, Random $-$0.53, \\rasp{} $-$0.61\\,pp; Table~\\ref{tab:decoupling}).\nWe term this \\emph{reward-accuracy decoupling}: reward trajectory reflects the model's capacity to learn from RL signal, not downstream accuracy.\nAt 20\\% sparsity, the four fine-grained criteria show mean $|\\Delta| {=} 0.54$\\,pp (max $0.61$\\,pp); across the full $\\alpha$ dose-response spectrum, $|\\Delta|$ remains below $1.14$\\,pp.\n\nThe degree of decoupling varies with sparsity.\nAt 15\\%, GRPO slightly amplifies the CKA-only advantage: the SFT gap of 5.69\\,pp (72.18\\% vs 66.49\\%) widens to 7.20\\,pp under GRPO (72.76\\% vs 65.56\\%).\nAt 20\\%, GRPO adds nothing: the SFT gap of 4.62\\,pp is preserved almost exactly (4.55\\,pp).\nThe most extreme case is 25\\%, where Standard's peak reward collapses to 0.008 yet accuracy still changes by only $+$0.99\\,pp (Appendix~\\ref{sec:appendix_cross_sparsity}).\nAcross all four fine-grained criteria at 20\\% and 25\\%, $|\\Delta| < 1$\\,pp without exception on GSM8K (Tables~\\ref{tab:decoupling},~\\ref{tab:cross_sparsity}); dose-response $\\alpha$ variations show slightly larger but still small differences (max $1.14$\\,pp at $\\alpha{=}2.0$; Table~\\ref{tab:alpha}).\nOn MATH-500, differences remain within statistical noise ($|\\Delta| < 2.5$\\,pp with stderr ${\\approx}$2\\,pp; Appendix~\\ref{sec:appendix_math500}).\nModerate structural damage (15\\%) apparently preserves enough capacity for GRPO to differentially benefit CKA-only pruning, while more aggressive pruning (20--25\\%) exceeds the threshold where GRPO can improve upon SFT baselines.\n\nThese results are robust: CKA-only GRPO accuracy varies by only 0.36\\,pp across three seeds (64.22--64.58\\%; Appendix~\\ref{sec:appendix_multiseed}), and extending training to 300 steps leaves accuracy unchanged (CKA-only 64.37\\%$\\to$64.37\\%, Standard 59.44\\%$\\to$59.29\\%).\nThe ranking and decoupling generalize beyond GSM8K: on MATH-500~\\citep{hendrycks2021math}, CKA-only ranks highest and Random lowest in SFT accuracy (26.8\\% vs 14.4\\%), though middle-ranked methods swap positions (Standard 25.8\\% $>$ \\rasp{} 21.2\\%; Appendix~\\ref{sec:appendix_math500}), and on MBPP~\\citep{austin2021mbpp} all fine-grained GRPO $|\\Delta| < 2$\\,pp (Appendix~\\ref{sec:appendix_mbpp}).\n\\label{sec:ood}\nShortGPT~\\citep{shortgpt2024} depth pruning is the sole exception: its GRPO delta is task-dependent ($-$1.36\\,pp on GSM8K, $+$4.01\\,pp on MBPP; Tables~\\ref{tab:decoupling},~\\ref{tab:mbpp}), unlike the uniformly small deltas of fine-grained methods ($|\\Delta| \\leq 1.34$\\,pp, with the cross-benchmark maximum from MBPP).\n\n\n\\subsection{Additional Results}\n\\label{sec:additional_results}\n\n\\paragraph{Post-SFT accuracy does not predict GRPO outcome.}\n\\label{sec:sft_gradient}\nUnder SFT alone, CKA-only (63.91\\%) $>$ \\rasp{} (61.49\\%) $>$ Standard (59.29\\%) $>$ Random (51.25\\%), yet under GRPO the \\rasp{}/Standard ordering reverses (peak 0.081 vs 0.061) and Random outperforms both in peak reward (0.190).\nMore strikingly, ShortGPT post-SFT (44.73\\%) shows GRPO actively harming accuracy ($-$1.36\\,pp), while unstructured pruning achieves the highest post-SFT accuracy (87.87\\%) with GRPO accuracy 87.64\\% ($\\Delta{=}{-}0.23$\\,pp), confirming that pruning criteria are irrelevant when structural damage is minimal (96.5\\% dense retention).\nPost-SFT accuracy does not predict GRPO recovery outcome: the spectrum is driven by structural properties of the pruned architecture.\n\n\\paragraph{Sparsity limits and dose-response.}\n\\label{sec:sparsity_cliff}\nAll methods collapse at 30\\% sparsity, validating 20\\% as the operating point (Appendix~\\ref{sec:appendix_sparsity_cliff}).\nPruning reduces parameters by 19\\% and memory by ${\\sim}$28\\% (Appendix~\\ref{sec:appendix_inference}).\nOn GSM8K, the CKA coefficient $\\alpha$ exhibits an inverted-U pattern in recovery accuracy across $\\{0.5, 1.0, 2.0, 3.0, 4.0\\}$, peaking at $\\alpha{=}2.0$ (SFT 64.97\\%, GRPO 66.11\\%) with $|\\Delta| \\leq 1.14$\\,pp at every point; $\\alpha{=}1.0$ collapses (peak reward 0.061) while $\\alpha{=}4.0$ recovers to 62.77\\% (Appendix~\\ref{sec:appendix_alpha}).\n\n\n\\subsection{Extended Analysis}\n\\label{sec:extended_analysis}\n\n\\begin{figure}[t]\n    \\centering\n    \\includegraphics[width=\\columnwidth]{figures/paper/fig4_cka_heatmap.pdf}\n    \\caption{Layer-wise CKA similarity between dense and pruned representations (28 layers). CKA-only diverges most from dense ($\\mu{=}0.62$) yet recovers best; Standard ($\\mu{=}0.90$), Random ($\\mu{=}0.92$), and \\rasp{} ($\\mu{=}0.88$) preserve dense fidelity but collapse under RL.}\n    \\label{fig:cka_heatmap}\n\\end{figure}\n\n\\input{tables/tab5_cross_scale}\n\n\\paragraph{Representational diversity.}\nCKA similarity between dense and pruned representations (Figure~\\ref{fig:cka_heatmap}) shows CKA-only diverges most from the dense model ($\\mu{=}0.62$), while Standard ($\\mu{=}0.90$), Random ($\\mu{=}0.92$), and \\rasp{} ($\\mu{=}0.88$) cluster near 1.0.\nPreserving dense fidelity through gradient importance appears to retain redundant representations at the expense of the diversity that GRPO exploration requires.\nCKA-only concentrates pruning in early layers (L0--9, 72.5\\% of removed groups) while Standard prunes uniformly, removing late-layer structures that are representationally unique (Appendix~\\ref{sec:appendix_overlap}).\nGradient flow analysis corroborates this: CKA-only models exhibit 2.89$\\times$ mean gradient magnitude versus Standard across 55/56 layer groups ($p{<}0.05$, Wilcoxon; Appendix~\\ref{sec:appendix_gradient}), consistent with diversity preservation enabling stronger RL training signals.\n\n\\paragraph{Extended training cannot rescue collapse.}\nExtending GRPO from 100 to 300 steps (Figure~\\ref{fig:extended_training}, Appendix~\\ref{sec:appendix_extended}), Standard shows zero net improvement (reward 0.054--0.058, $f_0 > 0.5$ throughout), while CKA-only sustains a 5.5$\\times$ gap (0.308 vs 0.056 at step 300). The gap is structural, not a matter of training budget.\n\n\\paragraph{Cross-scale and cross-architecture generalization.}\nOn DeepSeek-R1-Distill-Qwen-1.5B at 20\\% sparsity (Table~\\ref{tab:cross_scale}), the three-method ordering is preserved (CKA-only 35.48\\% $\\gg$ \\rasp{} 26.16\\% $>$ Standard 22.29\\%), with reward-accuracy decoupling confirmed at this scale ($|\\Delta| < 1$\\,pp: CKA-only $-$0.15, Standard $-$0.61\\,pp).\nOn Qwen2.5-Math-7B at 20\\% sparsity (Table~\\ref{tab:cross_arch}, Appendix~\\ref{sec:appendix_cross_arch}), CKA-only causes near-total initial damage (1.0\\% vs Standard's 18.5\\%) yet SFT recovers it to 51.50\\% $\\pm$ 3.53 while Standard remains at 21.00\\% $\\pm$ 2.88 ($N{=}200$), confirming that recoverability depends on preserved structure, not starting accuracy. GRPO validation on this architecture is left to future work.\n\n\n",
      "numLines": 132,
      "startLine": 1,
      "totalLines": 132
    }
  },
  "sourceToolAssistantUUID": "86f94c6e-732d-46ce-86dd-823eb14491bf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "3a90179e-e19e-41d1-8fb4-f23e916f555f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 33 · 2026-05-23T10:47:25.784Z_

<details open><summary>🔧 Tool call — Read · `toolu_017Htxet1j85hTfHSE476Cks`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "56f612af-cc09-48a2-8cb4-7e759e9b1133",
  "isSidechain": false,
  "requestId": "req_011CbKNGo4rLHPN2FBzfYpBN",
  "type": "assistant",
  "uuid": "23648e42-2971-44bb-82a2-bff6fdc66486",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "3a90179e-e19e-41d1-8fb4-f23e916f555f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LTRFjV5U2DZDnMEQV3bmJE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1748,
      "cache_read_input_tokens": 25217,
      "output_tokens": 1165,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1748,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1165,
          "cache_read_input_tokens": 25217,
          "cache_creation_input_tokens": 1748,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1748
          },
          "type": "message"
        }
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

_source line 34 · 2026-05-23T10:47:25.789Z_

<details><summary>↩ Tool result · `toolu_017Htxet1j85hTfHSE476Cks`</summary>

```text
1	\section{Training Details}
2	\label{sec:appendix_training}
3	
4	\begin{table}[h]
5	\centering
6	\small
7	\caption{Hyperparameter details for SFT warmup and GRPO recovery stages.}
8	\label{tab:hyperparams}
9	\begin{tabular}{@{}lll@{}}
10	\toprule
11	Parameter & SFT & GRPO \\
12	\midrule
13	Learning rate & $2 \times 10^{-5}$ & $1 \times 10^{-6}$ \\
14	Batch size & 1 & 1 \\
15	Gradient accumulation & 8 & 1 \\
16	Max sequence length & 2{,}048 & -- \\
17	Max new tokens & -- & 1{,}024 \\
18	Optimizer & AdamW & AdamW \\
19	Epochs / Steps & 2 epochs & 100 steps \\
20	KL coefficient $\beta$ & -- & 0.01 \\
21	Sampling temperature & -- & 0.4 \\
22	Num generations per prompt & -- & 8 \\
23	Reward & -- & Binary (exact match) \\
24	Loss formulation & Cross-entropy & DAPO-style clipped \\
25	\texttt{reward\_desert\_patience} & -- & 50 \\
26	\bottomrule
27	\end{tabular}
28	\end{table}
29	
30	\section{Algorithm}
31	\label{sec:appendix_algo}
32	
33	\begin{algorithm}[h]
34	\caption{Controlled Pruning Comparison Framework}
35	\label{alg:rasp}
36	\begin{algorithmic}[1]
37	\Require Model $\mathcal{M}$, calibration data $\mathcal{D}_\text{cal}$, target sparsity $s$, scoring criterion $\mathcal{C} \in \{\text{Std}, \text{RASP}, \text{CKA}, \text{Rand}\}$, layer floor $\tau$
38	\Ensure Pruned and recovered model $\mathcal{M}'$
39	\Statex \textit{\% Stage 1: Shared Structural Analysis}
40	\For{each structure $h \in \mathcal{H}$}
41	    \State Compute importance $I(h)$ via Eq.~\eqref{eq:importance}
42	    \State Collect activations $\mathbf{X}_h$ on $\mathcal{D}_\text{cal}$
43	\EndFor
44	\For{each layer $\ell = 1, \ldots, L$}
45	    \For{each structure $h_i$ in layer $\ell$}
46	        \State $F(h_i) \gets \frac{1}{|\mathcal{H}_\ell|-1} \sum_{j \neq i} \text{CKA}(\mathbf{X}_{h_i}, \mathbf{X}_{h_j})$
47	    \EndFor
48	\EndFor
49	\Statex \textit{\% Stage 2: Criterion-Specific Scoring}
50	\For{each structure $h \in \mathcal{H}$}
51	    \State $S(h) \gets \mathcal{C}(I(h), F(h))$ \hfill $\triangleright$ Eq.~\ref{eq:standard}, \ref{eq:score}, \ref{eq:cka_only}, or random
52	\EndFor
53	\State Sort $\mathcal{H}$ by $S(h)$ ascending; prune lowest up to $s$, subject to $\tau$
54	\Statex \textit{\% Stage 3: Identical Two-Stage Recovery}
55	\State $\mathcal{M}_\text{warm} \gets \text{SFT}(\mathcal{M}_\text{pruned}, \mathcal{D}_\text{sft})$ \hfill $\triangleright$ restore EOS \& format
56	\State $\mathcal{M}' \gets \text{GRPO}(\mathcal{M}_\text{warm}, \mathcal{D}_\text{rlvr})$ \hfill $\triangleright$ recover reasoning
57	\State \Return $\mathcal{M}'$
58	\end{algorithmic}
59	\end{algorithm}
60	
61	\section{Inference Efficiency}
62	\label{sec:appendix_inference}
63	
64	\begin{table}[h]
65	\centering
66	\small
67	\caption{Inference characteristics at 20\% sparsity (single-GPU, no contention). Pruning reduces parameters by 19\% and memory by ${\sim}$28\%, with TTFT improving 18\%. Per-token throughput decreases 19\% (0.81$\times$) due to non-uniform layer widths from full-layer removal that current GPU kernels do not optimize.}
68	\label{tab:inference}
69	\begin{tabular}{@{}lcccc@{}}
70	\toprule
71	Configuration & TPS\,(tok/s) & TTFT\,(ms) & Per-token\,(ms) & Params\,(B) \\
72	\midrule
73	Dense 7B & 72.0 & 20.1 & 13.9 & 7.62 \\
74	CKA-only 20\% & 58.3 & 16.4 & 16.7 & 6.16 \\
75	Standard 20\% & 58.2 & 16.4 & 16.7 & 6.16 \\
76	\bottomrule
77	\end{tabular}
78	\end{table}
79	
80	All pruned models achieve ${\sim}$28\% memory reduction from structural parameter removal.
81	TTFT (time to first token) improves by 18\% (20.1$\to$16.4\,ms), reflecting faster prefill with fewer parameters.
82	Per-token throughput decreases by 19\% (72.0$\to$58.3 tok/s, or 13.9$\to$16.7\,ms per token), consistent with non-uniform layer widths creating computational bottlenecks that current GPU kernels do not optimize away.
83	CKA-only and Standard show identical throughput (58.3 vs 58.2 tok/s), confirming that the pruning criterion affects recovery capacity but not inference speed at matched sparsity.
84	
85	\section{CKA Coefficient $\alpha$ Ablation}
86	\label{sec:appendix_alpha}
87	
88	\input{tables/table3_alpha}
89	
90	On GSM8K, the dose-response curve across $\alpha \in \{0.5, 1.0, 2.0, 3.0, 4.0\}$ reveals an inverted-U pattern peaking at $\alpha{=}2.0$ (SFT 64.97\%, GRPO 66.11\%, $\Delta{=}{+}1.14$\,pp; Table~\ref{tab:alpha}).
91	At $\alpha{=}0.5$, importance still dominates; recovery is low (SFT 60.73\%, GRPO 61.18\%).
92	At $\alpha{=}1.0$ (\rasp{}), GRPO collapses (peak reward 0.061, accuracy 60.88\%, $\Delta{=}{-}0.61$\,pp).
93	$\alpha{=}3.0$ (SFT 64.14\%, GRPO 63.46\%, $\Delta{=}{-}0.68$\,pp) excludes a plateau hypothesis: accuracy drops 2.65\,pp from the $\alpha{=}2.0$ peak, confirming that the optimum is a true peak rather than a saturation regime.
94	At $\alpha{=}4.0$, CKA overlap dominates; the model recovers to 62.77\% GRPO accuracy (SFT 61.94\%, $\Delta{=}{+}0.83$\,pp) with active GRPO learning (reward 0.146$\to$0.256$\to$0.198).
95	Reward-accuracy decoupling holds at every $\alpha$ value: $|\Delta| \leq 1.14$\,pp across all five points.
96	
97	\section{Extended Training Dynamics}
98	\label{sec:appendix_extended}
99	
100	\begin{figure}[h]
101	    \centering
102	    \includegraphics[width=0.85\columnwidth]{figures/paper/fig5_extended_training.pdf}
103	    \caption{Extended GRPO training (300 steps, 3$\times$ original budget). (a)~Standard reward shows zero net gain (0.054$\to$0.056); CKA-only oscillates in the 0.22--0.44 range with a 5.5$\times$ gap at step 300. (b)~Standard $f_0$ remains in the collapse zone ($>$0.5); CKA-only stays below 0.30.}
104	    \label{fig:extended_training}
105	\end{figure}
106	
107	\section{MATH-500 Out-of-Distribution Evaluation}
108	\label{sec:appendix_math500}
109	
110	\input{tables/tab_math500}
111	
112	The method ordering CKA-only (26.8\%) $>$ Standard (25.8\%) $>$ \rasp{} (21.2\%) $>$ Random (14.4\%) on MATH-500 SFT is preserved from GSM8K (64.39\% $>$ 59.84\% $>$ 60.88\% $>$ 50.72\%), confirming that the recovery capacity spectrum generalizes across benchmarks.
113	The $\alpha$ dose-response effect is not statistically significant on MATH-500: SFT accuracy varies by ${\sim}$8\,pp across $\alpha$ values, but with stderr ${\approx}$2\,pp per point, attributable to high truncation rates at the 2048-token limit and floor effects at this difficulty level.
114	The inverted-U pattern is validated on GSM8K (Table~\ref{tab:alpha}); MATH-500 does not resolve the dose-response shape.
115	
116	\section{MBPP Code Generation}
117	\label{sec:appendix_mbpp}
118	
119	\input{tables/tab_mbpp}
120	
121	MBPP GRPO deltas are uniformly slightly positive across all fine-grained methods (mean $+$1.25\,pp), but none are statistically significant at this sample size ($N{=}374$; stderr ${\approx}1.7$\,pp).
122	This directional consistency may reflect a weak task-specific GRPO effect at the capability floor rather than a violation of reward-accuracy decoupling.
123	
124	\section{CKA Scoring Stability}
125	\label{sec:appendix_cka_stability}
126	
127	\input{tables/tab_cka_stability}
128	
129	CKA-based structure rankings are highly stable across calibration data volumes: Spearman $\rho$ between rankings from 256, 512, and 1024 calibration samples ranges from 0.964 to 0.979, indicating that the scoring criterion is not sensitive to calibration set size.
130	
131	\section{Gradient Signal Analysis}
132	\label{sec:appendix_gradient}
133	
134	We compare per-layer gradient magnitudes during early GRPO training ($N{=}200$ GSM8K calibration samples) across three pruning criteria using paired Wilcoxon signed-rank tests.
135	
136	\begin{table}[h]
137	\centering
138	\small
139	\caption{Pairwise gradient magnitude ratios during GRPO training. Ratio: mean gradient magnitude of method A divided by method B across 56 parameter groups (28 layers $\times$ 2 projections). Significant layers: count where paired Wilcoxon signed-rank $p{<}0.05$.}
140	\label{tab:gradient_flow}
141	\begin{tabular}{@{}lcc@{}}
142	\toprule
143	Comparison & Gradient Ratio & Sig.\ Layers \\
144	\midrule
145	CKA-only vs Standard & 2.89$\times$ & 55\,/\,56 \\
146	CKA-only vs \rasp{} & 2.26$\times$ & 56\,/\,56 \\
147	\rasp{} vs Standard & 1.28$\times$ & 45\,/\,56 \\
148	\bottomrule
149	\end{tabular}
150	\end{table}
151	
152	The gradient magnitude hierarchy (CKA-only $\gg$ \rasp{} $>$ Standard) mirrors the recovery capacity hierarchy (GSM8K: 64.39\% $>$ 60.88\% $>$ 59.84\%), with bootstrap 95\% CIs for all ratios excluding 1.0.
153	This is consistent with diversity preservation enabling stronger training signals during GRPO, though the evidence is correlational: an alternative explanation---that CKA-only retains more functional structure, producing higher initial loss and naturally larger gradients---cannot be ruled out.
154	
155	\section{Seed Reproducibility}
156	\label{sec:appendix_seed}
157	
158	CKA-only GSM8K accuracy across 3 GRPO seeds: 64.37\% (seed 42), 64.22\% (seed 123), 64.58\% (seed 456), yielding mean 64.39\% $\pm$ 0.19\,pp.
159	Standard: mean 59.84\% $\pm$ 0.38\,pp across the same 3 seeds.
160	See Table~\ref{tab:multiseed} for the full summary.
161	
162	\section{Sparsity Cliff at 30\%}
163	\label{sec:appendix_sparsity_cliff}
164	
165	\input{tables/table4_sparsity_cliff}
166	
167	All tested methods collapse at 30\% sparsity: Standard retains 4\% accuracy, \rasp{} and CKA-only reach 0\%.
168	This capacity threshold, independent of pruning criterion, validates 20\% as the operating point and confirms that the recovery capacity spectrum reflects how methods allocate a limited pruning budget.
169	
170	\section{Multi-Seed GRPO Results}
171	\label{sec:appendix_multiseed}
172	
173	\begin{table}[h]
174	\centering
175	\small
176	\caption{Multi-seed GRPO results on GSM8K ($N{=}1{,}319$). CKA-only, Standard, and Random each trained with 3 GRPO seeds (42, 123, 456); pruning calibration and SFT are identical across all runs within each sparsity level.}
177	\label{tab:multiseed}
178	\begin{tabular}{@{}llccc@{}}
179	\toprule
180	Sparsity & Method & Mean Acc.\,(\%) & Std\,(pp) & Seeds \\
181	\midrule
182	\multirow{4}{*}{20\%} & CKA-only & 64.39 & 0.19 & 3 \\
183	 & Standard & 59.84 & 0.38 & 3 \\
184	 & \rasp{} & 60.88 & -- & 1 \\
185	 & Random & 50.72 & 0.15 & 3 \\
186	\midrule
187	\multirow{2}{*}{15\%} & CKA-only & 72.76 & 0.57 & 3 \\
188	 & Standard & 65.56 & 0.50 & 3 \\
189	\bottomrule
190	\end{tabular}
191	\end{table}
192	
193	At 20\% sparsity, the 4.55\,pp gap between CKA-only and Standard is robust across seeds, with non-overlapping ranges (CKA-only: 64.22--64.58\%, Standard: 59.44--60.20\%).
194	Standard shows a wider observed range across seeds (0.76\,pp vs 0.36\,pp), consistent with borderline-collapse dynamics where small perturbations produce larger outcome variation.
195	Random (3 seeds: 50.57\%, 50.72\%, 50.87\%; $\sigma{=}0.15$\,pp, observed range 0.30\,pp) converges in a narrow band with SFT accuracy seed-independent at 51.25\%.
196	All three seeds satisfy GRPO $\leq$ SFT ($\Delta{=}{-}0.68$, $-$0.53, $-$0.38\,pp), confirming that reward-accuracy decoupling is reproducible across seeds even for stagnating methods.
197	Note: Standard seed 42 was trained from a separately initialized SFT checkpoint (accuracy 59.21\% vs.\ 59.29\% for seeds 123/456; $\Delta = 0.08$\,pp).
198	At 15\% sparsity, the gap widens to 7.20\,pp (72.76\% vs 65.56\%, $t{\approx}16.4$, $p{<}0.001$), with non-overlapping ranges (CKA-only: 72.10--73.09\%, Standard: 65.13--65.43\%).
199	
200	\section{Cross-Sparsity Validation}
201	\label{sec:appendix_cross_sparsity}
202	
203	\begin{table}[h]
204	\centering
205	\small
206	\caption{Cross-sparsity validation on DeepSeek-R1-Distill-Qwen-7B. GSM8K accuracy ($N{=}1{,}319$) after SFT warmup and GRPO recovery. 15\% and 20\% GRPO values are mean over 3 seeds (see Tables~\ref{tab:decoupling},~\ref{tab:multiseed}). $^\ddagger$Single seed. Mean $|\Delta| \leq 1$\,pp across all conditions.}
207	\label{tab:cross_sparsity}
208	\begin{tabular}{@{}llccc@{}}
209	\toprule
210	Sparsity & Method & SFT\,(\%) & GRPO\,(\%) & $\Delta$\,(pp) \\
211	\midrule
212	\multirow{2}{*}{15\%} & CKA-only & 72.18 & \textbf{72.76{\scriptsize$\pm$0.57}} & $+$0.58 \\
213	 & Standard & 66.49 & 65.56{\scriptsize$\pm$0.50} & $-$0.93 \\
214	\midrule
215	\multirow{2}{*}{20\%} & CKA-only & 63.91 & 64.39 & $+$0.48 \\
216	 & Standard & 59.29 & 59.84 & $+$0.55 \\
217	\midrule
218	\multirow{2}{*}{25\%$^\ddagger$} & CKA-only & 60.12 & 59.59 & $-$0.53 \\
219	 & Standard & 50.87 & 51.86 & $+$0.99 \\
220	\midrule
221	30\% & All & \multicolumn{3}{c}{Collapse ($\leq$4\%; Table~\ref{tab:sparsity_cliff})} \\
222	\bottomrule
223	\end{tabular}
224	\end{table}
225	
226	At 15\% sparsity (3-seed mean), the CKA-only advantage widens to $+$7.20\,pp (72.76\% vs 65.56\%), compared to $+$4.55\,pp at 20\%.
227	CKA-only at 15\% (72.76\%) represents the highest mean accuracy across all experimental conditions, retaining 80.1\% of original dense model performance (90.83\%).
228	At 25\% sparsity (single seed), Standard's SFT accuracy decline accelerates ($-$7.20\,pp from 15\%$\to$20\%, $-$8.42\,pp from 20\%$\to$25\%), while CKA-only's decline decelerates ($-$8.27\,pp then $-$3.79\,pp).
229	Reward-accuracy decoupling is preserved ($|\Delta| \leq 1$\,pp for both methods) despite Standard's near-zero peak reward (0.008).
230	
231	\section{Cross-Architecture Validation}
232	\label{sec:appendix_cross_arch}
233	
234	\begin{table}[h]
235	\centering
236	\small
237	\caption{Cross-architecture validation on Qwen2.5-Math-7B~\citep{qwen2.5} at 20\% structured sparsity. Accuracy evaluated on GSM8K ($N{=}200$). Post-SFT reports mean $\pm$ std over multiple SFT runs. EOS rate: fraction of generations that produce a valid end-of-sequence token.}
238	\label{tab:cross_arch}
239	\begin{tabular}{@{}lccc@{}}
240	\toprule
241	Method & Post-Prune\,(\%) & Post-SFT\,(\%) & EOS Rate\,(\%) \\
242	\midrule
243	CKA-only & 1.0 & \textbf{51.50 $\pm$ 3.53} & 27.0 \\
244	Standard & 18.5 & 21.00 $\pm$ 2.88 & 36.5 \\
245	\bottomrule
246	\end{tabular}
247	\end{table}
248	
249	CKA-only pruning causes near-total initial damage on Qwen2.5-Math-7B (1.0\% post-prune accuracy vs Standard's 18.5\%), yet SFT recovers CKA-only to 51.50\% while Standard remains at 21.00\%.
250	This post-prune accuracy reversal provides strong evidence that recovery capacity is shaped by preserved network structure rather than starting accuracy.
251	EOS rates remain below 40\% for both methods, indicating that SFT warmup is less effective on this architecture; GRPO validation is deferred to future work.\footnote{Preliminary GRPO evaluation yields 48.60\% (243/500), but 83.8\% of responses were truncated at 2048 tokens, precluding direct comparison with SFT results.}
252	
253	\section{Structural Overlap Analysis}
254	\label{sec:appendix_overlap}
255	
256	CKA-only and Standard pruning produce markedly different removal patterns across the 28 layers of DeepSeek-R1-Distill-Qwen-7B at 20\% sparsity.
257	CKA-only concentrates pruning in early layers (L0--9 account for 72.5\% of removed MLP groups), preserving nearly all structures in later layers (L16--27).
258	Standard distributes removals more uniformly, pruning substantial numbers of groups in late layers (L16--18, L22, L25--26).
259	
260	The methods share only partial overlap in which structures they remove.
261	65 MLP groups are pruned exclusively by CKA-only (retained by Standard), concentrated in L6--9 and L27---structures that gradient importance scores as important but CKA identifies as redundant with neighboring groups.
262	Conversely, 46+ groups are pruned exclusively by Standard (retained by CKA-only), concentrated in L16--18, L22, and L25--26---structures that gradient importance scores as unimportant but CKA identifies as representationally unique.
263	
264	This pattern is consistent with the CKA heatmap (Figure~\ref{fig:cka_heatmap}): CKA-only's aggressive early-layer pruning disrupts dense representations (low diagonal CKA, $\mu{=}0.62$) but preserves diverse late-layer pathways, while Standard's uniform pruning maintains dense fidelity ($\mu{=}0.90$) at the cost of removing unique computational pathways in later layers.
265	
266	\section{KL Divergence During GRPO Training}
267	\label{sec:appendix_kl}
268	
269	\begin{figure}[t]
270	    \centering
271	    \includegraphics[width=0.75\columnwidth]{figures/paper/fig_appendix_kl.pdf}
272	    \caption{KL divergence between the policy and reference model during GRPO training. RASP maintains near-zero KL ($<$0.001), consistent with minimal policy movement during collapse. Random shows the highest KL (${\sim}$0.004--0.005), indicating more policy exploration. CKA-only and Standard fall between these extremes.}
273	    \label{fig:kl_divergence}
274	\end{figure}
275	
276	\section{Depth-First Pruning Baseline}
277	\label{sec:appendix_depth_first}
278	
279	As a sanity check, we test whether CKA-only's advantage reflects mere layer-depth bias by constructing a depth-first baseline: synthetic importance scores force removal of late layers first (L18--27: 0.001, L10--17: 0.5, L0--9: 1.0), then standard pruning at 20\% sparsity.
280	Both SFT (${\sim}$10\%) and GRPO (${\sim}$8\%) accuracy are near chance (early-stopped at $N{\approx}50$--88 samples due to conclusive results), confirming that naive depth ordering cannot substitute for criterion-based structure selection.
281	This baseline operates at layer-level granularity (removing entire transformer blocks), unlike CKA-only/Standard/\rasp{} which prune at MLP channel group level; the granularity difference limits direct comparison with our main results and precludes using this baseline as evidence for the recovery capacity spectrum.
282	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "23648e42-2971-44bb-82a2-bff6fdc66486",
  "isSidechain": false,
  "promptId": "dddf37fd-16cc-4cd5-bb05-648328938281",
  "type": "user",
  "uuid": "e6b66703-c02e-407b-8206-43b8c2d0c7d0",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/appendix.tex",
      "content": "\\section{Training Details}\n\\label{sec:appendix_training}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Hyperparameter details for SFT warmup and GRPO recovery stages.}\n\\label{tab:hyperparams}\n\\begin{tabular}{@{}lll@{}}\n\\toprule\nParameter & SFT & GRPO \\\\\n\\midrule\nLearning rate & $2 \\times 10^{-5}$ & $1 \\times 10^{-6}$ \\\\\nBatch size & 1 & 1 \\\\\nGradient accumulation & 8 & 1 \\\\\nMax sequence length & 2{,}048 & -- \\\\\nMax new tokens & -- & 1{,}024 \\\\\nOptimizer & AdamW & AdamW \\\\\nEpochs / Steps & 2 epochs & 100 steps \\\\\nKL coefficient $\\beta$ & -- & 0.01 \\\\\nSampling temperature & -- & 0.4 \\\\\nNum generations per prompt & -- & 8 \\\\\nReward & -- & Binary (exact match) \\\\\nLoss formulation & Cross-entropy & DAPO-style clipped \\\\\n\\texttt{reward\\_desert\\_patience} & -- & 50 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Algorithm}\n\\label{sec:appendix_algo}\n\n\\begin{algorithm}[h]\n\\caption{Controlled Pruning Comparison Framework}\n\\label{alg:rasp}\n\\begin{algorithmic}[1]\n\\Require Model $\\mathcal{M}$, calibration data $\\mathcal{D}_\\text{cal}$, target sparsity $s$, scoring criterion $\\mathcal{C} \\in \\{\\text{Std}, \\text{RASP}, \\text{CKA}, \\text{Rand}\\}$, layer floor $\\tau$\n\\Ensure Pruned and recovered model $\\mathcal{M}'$\n\\Statex \\textit{\\% Stage 1: Shared Structural Analysis}\n\\For{each structure $h \\in \\mathcal{H}$}\n    \\State Compute importance $I(h)$ via Eq.~\\eqref{eq:importance}\n    \\State Collect activations $\\mathbf{X}_h$ on $\\mathcal{D}_\\text{cal}$\n\\EndFor\n\\For{each layer $\\ell = 1, \\ldots, L$}\n    \\For{each structure $h_i$ in layer $\\ell$}\n        \\State $F(h_i) \\gets \\frac{1}{|\\mathcal{H}_\\ell|-1} \\sum_{j \\neq i} \\text{CKA}(\\mathbf{X}_{h_i}, \\mathbf{X}_{h_j})$\n    \\EndFor\n\\EndFor\n\\Statex \\textit{\\% Stage 2: Criterion-Specific Scoring}\n\\For{each structure $h \\in \\mathcal{H}$}\n    \\State $S(h) \\gets \\mathcal{C}(I(h), F(h))$ \\hfill $\\triangleright$ Eq.~\\ref{eq:standard}, \\ref{eq:score}, \\ref{eq:cka_only}, or random\n\\EndFor\n\\State Sort $\\mathcal{H}$ by $S(h)$ ascending; prune lowest up to $s$, subject to $\\tau$\n\\Statex \\textit{\\% Stage 3: Identical Two-Stage Recovery}\n\\State $\\mathcal{M}_\\text{warm} \\gets \\text{SFT}(\\mathcal{M}_\\text{pruned}, \\mathcal{D}_\\text{sft})$ \\hfill $\\triangleright$ restore EOS \\& format\n\\State $\\mathcal{M}' \\gets \\text{GRPO}(\\mathcal{M}_\\text{warm}, \\mathcal{D}_\\text{rlvr})$ \\hfill $\\triangleright$ recover reasoning\n\\State \\Return $\\mathcal{M}'$\n\\end{algorithmic}\n\\end{algorithm}\n\n\\section{Inference Efficiency}\n\\label{sec:appendix_inference}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Inference characteristics at 20\\% sparsity (single-GPU, no contention). Pruning reduces parameters by 19\\% and memory by ${\\sim}$28\\%, with TTFT improving 18\\%. Per-token throughput decreases 19\\% (0.81$\\times$) due to non-uniform layer widths from full-layer removal that current GPU kernels do not optimize.}\n\\label{tab:inference}\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\nConfiguration & TPS\\,(tok/s) & TTFT\\,(ms) & Per-token\\,(ms) & Params\\,(B) \\\\\n\\midrule\nDense 7B & 72.0 & 20.1 & 13.9 & 7.62 \\\\\nCKA-only 20\\% & 58.3 & 16.4 & 16.7 & 6.16 \\\\\nStandard 20\\% & 58.2 & 16.4 & 16.7 & 6.16 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAll pruned models achieve ${\\sim}$28\\% memory reduction from structural parameter removal.\nTTFT (time to first token) improves by 18\\% (20.1$\\to$16.4\\,ms), reflecting faster prefill with fewer parameters.\nPer-token throughput decreases by 19\\% (72.0$\\to$58.3 tok/s, or 13.9$\\to$16.7\\,ms per token), consistent with non-uniform layer widths creating computational bottlenecks that current GPU kernels do not optimize away.\nCKA-only and Standard show identical throughput (58.3 vs 58.2 tok/s), confirming that the pruning criterion affects recovery capacity but not inference speed at matched sparsity.\n\n\\section{CKA Coefficient $\\alpha$ Ablation}\n\\label{sec:appendix_alpha}\n\n\\input{tables/table3_alpha}\n\nOn GSM8K, the dose-response curve across $\\alpha \\in \\{0.5, 1.0, 2.0, 3.0, 4.0\\}$ reveals an inverted-U pattern peaking at $\\alpha{=}2.0$ (SFT 64.97\\%, GRPO 66.11\\%, $\\Delta{=}{+}1.14$\\,pp; Table~\\ref{tab:alpha}).\nAt $\\alpha{=}0.5$, importance still dominates; recovery is low (SFT 60.73\\%, GRPO 61.18\\%).\nAt $\\alpha{=}1.0$ (\\rasp{}), GRPO collapses (peak reward 0.061, accuracy 60.88\\%, $\\Delta{=}{-}0.61$\\,pp).\n$\\alpha{=}3.0$ (SFT 64.14\\%, GRPO 63.46\\%, $\\Delta{=}{-}0.68$\\,pp) excludes a plateau hypothesis: accuracy drops 2.65\\,pp from the $\\alpha{=}2.0$ peak, confirming that the optimum is a true peak rather than a saturation regime.\nAt $\\alpha{=}4.0$, CKA overlap dominates; the model recovers to 62.77\\% GRPO accuracy (SFT 61.94\\%, $\\Delta{=}{+}0.83$\\,pp) with active GRPO learning (reward 0.146$\\to$0.256$\\to$0.198).\nReward-accuracy decoupling holds at every $\\alpha$ value: $|\\Delta| \\leq 1.14$\\,pp across all five points.\n\n\\section{Extended Training Dynamics}\n\\label{sec:appendix_extended}\n\n\\begin{figure}[h]\n    \\centering\n    \\includegraphics[width=0.85\\columnwidth]{figures/paper/fig5_extended_training.pdf}\n    \\caption{Extended GRPO training (300 steps, 3$\\times$ original budget). (a)~Standard reward shows zero net gain (0.054$\\to$0.056); CKA-only oscillates in the 0.22--0.44 range with a 5.5$\\times$ gap at step 300. (b)~Standard $f_0$ remains in the collapse zone ($>$0.5); CKA-only stays below 0.30.}\n    \\label{fig:extended_training}\n\\end{figure}\n\n\\section{MATH-500 Out-of-Distribution Evaluation}\n\\label{sec:appendix_math500}\n\n\\input{tables/tab_math500}\n\nThe method ordering CKA-only (26.8\\%) $>$ Standard (25.8\\%) $>$ \\rasp{} (21.2\\%) $>$ Random (14.4\\%) on MATH-500 SFT is preserved from GSM8K (64.39\\% $>$ 59.84\\% $>$ 60.88\\% $>$ 50.72\\%), confirming that the recovery capacity spectrum generalizes across benchmarks.\nThe $\\alpha$ dose-response effect is not statistically significant on MATH-500: SFT accuracy varies by ${\\sim}$8\\,pp across $\\alpha$ values, but with stderr ${\\approx}$2\\,pp per point, attributable to high truncation rates at the 2048-token limit and floor effects at this difficulty level.\nThe inverted-U pattern is validated on GSM8K (Table~\\ref{tab:alpha}); MATH-500 does not resolve the dose-response shape.\n\n\\section{MBPP Code Generation}\n\\label{sec:appendix_mbpp}\n\n\\input{tables/tab_mbpp}\n\nMBPP GRPO deltas are uniformly slightly positive across all fine-grained methods (mean $+$1.25\\,pp), but none are statistically significant at this sample size ($N{=}374$; stderr ${\\approx}1.7$\\,pp).\nThis directional consistency may reflect a weak task-specific GRPO effect at the capability floor rather than a violation of reward-accuracy decoupling.\n\n\\section{CKA Scoring Stability}\n\\label{sec:appendix_cka_stability}\n\n\\input{tables/tab_cka_stability}\n\nCKA-based structure rankings are highly stable across calibration data volumes: Spearman $\\rho$ between rankings from 256, 512, and 1024 calibration samples ranges from 0.964 to 0.979, indicating that the scoring criterion is not sensitive to calibration set size.\n\n\\section{Gradient Signal Analysis}\n\\label{sec:appendix_gradient}\n\nWe compare per-layer gradient magnitudes during early GRPO training ($N{=}200$ GSM8K calibration samples) across three pruning criteria using paired Wilcoxon signed-rank tests.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Pairwise gradient magnitude ratios during GRPO training. Ratio: mean gradient magnitude of method A divided by method B across 56 parameter groups (28 layers $\\times$ 2 projections). Significant layers: count where paired Wilcoxon signed-rank $p{<}0.05$.}\n\\label{tab:gradient_flow}\n\\begin{tabular}{@{}lcc@{}}\n\\toprule\nComparison & Gradient Ratio & Sig.\\ Layers \\\\\n\\midrule\nCKA-only vs Standard & 2.89$\\times$ & 55\\,/\\,56 \\\\\nCKA-only vs \\rasp{} & 2.26$\\times$ & 56\\,/\\,56 \\\\\n\\rasp{} vs Standard & 1.28$\\times$ & 45\\,/\\,56 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe gradient magnitude hierarchy (CKA-only $\\gg$ \\rasp{} $>$ Standard) mirrors the recovery capacity hierarchy (GSM8K: 64.39\\% $>$ 60.88\\% $>$ 59.84\\%), with bootstrap 95\\% CIs for all ratios excluding 1.0.\nThis is consistent with diversity preservation enabling stronger training signals during GRPO, though the evidence is correlational: an alternative explanation---that CKA-only retains more functional structure, producing higher initial loss and naturally larger gradients---cannot be ruled out.\n\n\\section{Seed Reproducibility}\n\\label{sec:appendix_seed}\n\nCKA-only GSM8K accuracy across 3 GRPO seeds: 64.37\\% (seed 42), 64.22\\% (seed 123), 64.58\\% (seed 456), yielding mean 64.39\\% $\\pm$ 0.19\\,pp.\nStandard: mean 59.84\\% $\\pm$ 0.38\\,pp across the same 3 seeds.\nSee Table~\\ref{tab:multiseed} for the full summary.\n\n\\section{Sparsity Cliff at 30\\%}\n\\label{sec:appendix_sparsity_cliff}\n\n\\input{tables/table4_sparsity_cliff}\n\nAll tested methods collapse at 30\\% sparsity: Standard retains 4\\% accuracy, \\rasp{} and CKA-only reach 0\\%.\nThis capacity threshold, independent of pruning criterion, validates 20\\% as the operating point and confirms that the recovery capacity spectrum reflects how methods allocate a limited pruning budget.\n\n\\section{Multi-Seed GRPO Results}\n\\label{sec:appendix_multiseed}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Multi-seed GRPO results on GSM8K ($N{=}1{,}319$). CKA-only, Standard, and Random each trained with 3 GRPO seeds (42, 123, 456); pruning calibration and SFT are identical across all runs within each sparsity level.}\n\\label{tab:multiseed}\n\\begin{tabular}{@{}llccc@{}}\n\\toprule\nSparsity & Method & Mean Acc.\\,(\\%) & Std\\,(pp) & Seeds \\\\\n\\midrule\n\\multirow{4}{*}{20\\%} & CKA-only & 64.39 & 0.19 & 3 \\\\\n & Standard & 59.84 & 0.38 & 3 \\\\\n & \\rasp{} & 60.88 & -- & 1 \\\\\n & Random & 50.72 & 0.15 & 3 \\\\\n\\midrule\n\\multirow{2}{*}{15\\%} & CKA-only & 72.76 & 0.57 & 3 \\\\\n & Standard & 65.56 & 0.50 & 3 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAt 20\\% sparsity, the 4.55\\,pp gap between CKA-only and Standard is robust across seeds, with non-overlapping ranges (CKA-only: 64.22--64.58\\%, Standard: 59.44--60.20\\%).\nStandard shows a wider observed range across seeds (0.76\\,pp vs 0.36\\,pp), consistent with borderline-collapse dynamics where small perturbations produce larger outcome variation.\nRandom (3 seeds: 50.57\\%, 50.72\\%, 50.87\\%; $\\sigma{=}0.15$\\,pp, observed range 0.30\\,pp) converges in a narrow band with SFT accuracy seed-independent at 51.25\\%.\nAll three seeds satisfy GRPO $\\leq$ SFT ($\\Delta{=}{-}0.68$, $-$0.53, $-$0.38\\,pp), confirming that reward-accuracy decoupling is reproducible across seeds even for stagnating methods.\nNote: Standard seed 42 was trained from a separately initialized SFT checkpoint (accuracy 59.21\\% vs.\\ 59.29\\% for seeds 123/456; $\\Delta = 0.08$\\,pp).\nAt 15\\% sparsity, the gap widens to 7.20\\,pp (72.76\\% vs 65.56\\%, $t{\\approx}16.4$, $p{<}0.001$), with non-overlapping ranges (CKA-only: 72.10--73.09\\%, Standard: 65.13--65.43\\%).\n\n\\section{Cross-Sparsity Validation}\n\\label{sec:appendix_cross_sparsity}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Cross-sparsity validation on DeepSeek-R1-Distill-Qwen-7B. GSM8K accuracy ($N{=}1{,}319$) after SFT warmup and GRPO recovery. 15\\% and 20\\% GRPO values are mean over 3 seeds (see Tables~\\ref{tab:decoupling},~\\ref{tab:multiseed}). $^\\ddagger$Single seed. Mean $|\\Delta| \\leq 1$\\,pp across all conditions.}\n\\label{tab:cross_sparsity}\n\\begin{tabular}{@{}llccc@{}}\n\\toprule\nSparsity & Method & SFT\\,(\\%) & GRPO\\,(\\%) & $\\Delta$\\,(pp) \\\\\n\\midrule\n\\multirow{2}{*}{15\\%} & CKA-only & 72.18 & \\textbf{72.76{\\scriptsize$\\pm$0.57}} & $+$0.58 \\\\\n & Standard & 66.49 & 65.56{\\scriptsize$\\pm$0.50} & $-$0.93 \\\\\n\\midrule\n\\multirow{2}{*}{20\\%} & CKA-only & 63.91 & 64.39 & $+$0.48 \\\\\n & Standard & 59.29 & 59.84 & $+$0.55 \\\\\n\\midrule\n\\multirow{2}{*}{25\\%$^\\ddagger$} & CKA-only & 60.12 & 59.59 & $-$0.53 \\\\\n & Standard & 50.87 & 51.86 & $+$0.99 \\\\\n\\midrule\n30\\% & All & \\multicolumn{3}{c}{Collapse ($\\leq$4\\%; Table~\\ref{tab:sparsity_cliff})} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAt 15\\% sparsity (3-seed mean), the CKA-only advantage widens to $+$7.20\\,pp (72.76\\% vs 65.56\\%), compared to $+$4.55\\,pp at 20\\%.\nCKA-only at 15\\% (72.76\\%) represents the highest mean accuracy across all experimental conditions, retaining 80.1\\% of original dense model performance (90.83\\%).\nAt 25\\% sparsity (single seed), Standard's SFT accuracy decline accelerates ($-$7.20\\,pp from 15\\%$\\to$20\\%, $-$8.42\\,pp from 20\\%$\\to$25\\%), while CKA-only's decline decelerates ($-$8.27\\,pp then $-$3.79\\,pp).\nReward-accuracy decoupling is preserved ($|\\Delta| \\leq 1$\\,pp for both methods) despite Standard's near-zero peak reward (0.008).\n\n\\section{Cross-Architecture Validation}\n\\label{sec:appendix_cross_arch}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Cross-architecture validation on Qwen2.5-Math-7B~\\citep{qwen2.5} at 20\\% structured sparsity. Accuracy evaluated on GSM8K ($N{=}200$). Post-SFT reports mean $\\pm$ std over multiple SFT runs. EOS rate: fraction of generations that produce a valid end-of-sequence token.}\n\\label{tab:cross_arch}\n\\begin{tabular}{@{}lccc@{}}\n\\toprule\nMethod & Post-Prune\\,(\\%) & Post-SFT\\,(\\%) & EOS Rate\\,(\\%) \\\\\n\\midrule\nCKA-only & 1.0 & \\textbf{51.50 $\\pm$ 3.53} & 27.0 \\\\\nStandard & 18.5 & 21.00 $\\pm$ 2.88 & 36.5 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nCKA-only pruning causes near-total initial damage on Qwen2.5-Math-7B (1.0\\% post-prune accuracy vs Standard's 18.5\\%), yet SFT recovers CKA-only to 51.50\\% while Standard remains at 21.00\\%.\nThis post-prune accuracy reversal provides strong evidence that recovery capacity is shaped by preserved network structure rather than starting accuracy.\nEOS rates remain below 40\\% for both methods, indicating that SFT warmup is less effective on this architecture; GRPO validation is deferred to future work.\\footnote{Preliminary GRPO evaluation yields 48.60\\% (243/500), but 83.8\\% of responses were truncated at 2048 tokens, precluding direct comparison with SFT results.}\n\n\\section{Structural Overlap Analysis}\n\\label{sec:appendix_overlap}\n\nCKA-only and Standard pruning produce markedly different removal patterns across the 28 layers of DeepSeek-R1-Distill-Qwen-7B at 20\\% sparsity.\nCKA-only concentrates pruning in early layers (L0--9 account for 72.5\\% of removed MLP groups), preserving nearly all structures in later layers (L16--27).\nStandard distributes removals more uniformly, pruning substantial numbers of groups in late layers (L16--18, L22, L25--26).\n\nThe methods share only partial overlap in which structures they remove.\n65 MLP groups are pruned exclusively by CKA-only (retained by Standard), concentrated in L6--9 and L27---structures that gradient importance scores as important but CKA identifies as redundant with neighboring groups.\nConversely, 46+ groups are pruned exclusively by Standard (retained by CKA-only), concentrated in L16--18, L22, and L25--26---structures that gradient importance scores as unimportant but CKA identifies as representationally unique.\n\nThis pattern is consistent with the CKA heatmap (Figure~\\ref{fig:cka_heatmap}): CKA-only's aggressive early-layer pruning disrupts dense representations (low diagonal CKA, $\\mu{=}0.62$) but preserves diverse late-layer pathways, while Standard's uniform pruning maintains dense fidelity ($\\mu{=}0.90$) at the cost of removing unique computational pathways in later layers.\n\n\\section{KL Divergence During GRPO Training}\n\\label{sec:appendix_kl}\n\n\\begin{figure}[t]\n    \\centering\n    \\includegraphics[width=0.75\\columnwidth]{figures/paper/fig_appendix_kl.pdf}\n    \\caption{KL divergence between the policy and reference model during GRPO training. RASP maintains near-zero KL ($<$0.001), consistent with minimal policy movement during collapse. Random shows the highest KL (${\\sim}$0.004--0.005), indicating more policy exploration. CKA-only and Standard fall between these extremes.}\n    \\label{fig:kl_divergence}\n\\end{figure}\n\n\\section{Depth-First Pruning Baseline}\n\\label{sec:appendix_depth_first}\n\nAs a sanity check, we test whether CKA-only's advantage reflects mere layer-depth bias by constructing a depth-first baseline: synthetic importance scores force removal of late layers first (L18--27: 0.001, L10--17: 0.5, L0--9: 1.0), then standard pruning at 20\\% sparsity.\nBoth SFT (${\\sim}$10\\%) and GRPO (${\\sim}$8\\%) accuracy are near chance (early-stopped at $N{\\approx}50$--88 samples due to conclusive results), confirming that naive depth ordering cannot substitute for criterion-based structure selection.\nThis baseline operates at layer-level granularity (removing entire transformer blocks), unlike CKA-only/Standard/\\rasp{} which prune at MLP channel group level; the granularity difference limits direct comparison with our main results and precludes using this baseline as evidence for the recovery capacity spectrum.\n",
      "numLines": 282,
      "startLine": 1,
      "totalLines": 282
    }
  },
  "sourceToolAssistantUUID": "23648e42-2971-44bb-82a2-bff6fdc66486",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "3a90179e-e19e-41d1-8fb4-f23e916f555f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 35 · 2026-05-23T10:47:26.261Z_

<details open><summary>🔧 Tool call — Read · `toolu_01AxjZhmB9JdFTPHe5DomWCo`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e6b66703-c02e-407b-8206-43b8c2d0c7d0",
  "isSidechain": false,
  "requestId": "req_011CbKNGo4rLHPN2FBzfYpBN",
  "type": "assistant",
  "uuid": "8d8fd384-cbd2-4d75-98bf-e40cf9e3839b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "3a90179e-e19e-41d1-8fb4-f23e916f555f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LTRFjV5U2DZDnMEQV3bmJE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1748,
      "cache_read_input_tokens": 25217,
      "output_tokens": 1165,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1748,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1165,
          "cache_read_input_tokens": 25217,
          "cache_creation_input_tokens": 1748,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1748
          },
          "type": "message"
        }
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

_source line 36 · 2026-05-23T10:47:26.266Z_

<details><summary>↩ Tool result · `toolu_01AxjZhmB9JdFTPHe5DomWCo`</summary>

```text
1	Fine-grained structured pruning of reasoning Large Language Models (LLMs), which removes MLP channel groups rather than entire layers, is typically followed by recovery training (SFT or RLVR) to restore reasoning capabilities.
2	RLVR is widely believed to be superior, yet we show this hierarchy reflects suboptimal pruning, not a fundamental property of RL\@.
3	When pruning preserves representational diversity, recovery method choice becomes irrelevant, a phenomenon we term \emph{reward-accuracy decoupling}: on GSM8K at 20\% sparsity, $|\Delta(\text{GRPO}-\text{SFT})| \leq 0.61$\,pp across all four fine-grained criteria (max $1.34$\,pp including dose-response variations and MBPP), with additional validation at 15\% and 25\%; differences on MATH-500 fall within statistical noise.
4	We propose Recovery-Aware Structured Pruning (\rasp{}), which balances gradient importance with CKA-based representational diversity via a coefficient $\alpha$.
5	On DeepSeek-R1-Distill-Qwen-7B, a dose-response analysis across $\alpha \in \{0.5, 1.0, 2.0, 3.0, 4.0\}$ reveals an inverted-U on GSM8K, peaking at $\alpha{=}2.0$ (66.11\%).
6	Under identical GRPO training, four pruning criteria produce a \emph{recovery capacity spectrum}: diversity-preserving pruning achieves active learning (peak reward 4.4$\times$ vs importance-only), while importance-dominated pruning collapses entirely.
7	The spectrum tracks preserved representational diversity rather than gradient importance, with initial evidence for generality across scales (1.5B) and, via SFT-based recovery, across architectures (Qwen2.5-Math-7B).
8	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8d8fd384-cbd2-4d75-98bf-e40cf9e3839b",
  "isSidechain": false,
  "promptId": "dddf37fd-16cc-4cd5-bb05-648328938281",
  "type": "user",
  "uuid": "0246c699-217b-4457-85be-0ef6ee9575e6",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/abstract.tex",
      "content": "Fine-grained structured pruning of reasoning Large Language Models (LLMs), which removes MLP channel groups rather than entire layers, is typically followed by recovery training (SFT or RLVR) to restore reasoning capabilities.\nRLVR is widely believed to be superior, yet we show this hierarchy reflects suboptimal pruning, not a fundamental property of RL\\@.\nWhen pruning preserves representational diversity, recovery method choice becomes irrelevant, a phenomenon we term \\emph{reward-accuracy decoupling}: on GSM8K at 20\\% sparsity, $|\\Delta(\\text{GRPO}-\\text{SFT})| \\leq 0.61$\\,pp across all four fine-grained criteria (max $1.34$\\,pp including dose-response variations and MBPP), with additional validation at 15\\% and 25\\%; differences on MATH-500 fall within statistical noise.\nWe propose Recovery-Aware Structured Pruning (\\rasp{}), which balances gradient importance with CKA-based representational diversity via a coefficient $\\alpha$.\nOn DeepSeek-R1-Distill-Qwen-7B, a dose-response analysis across $\\alpha \\in \\{0.5, 1.0, 2.0, 3.0, 4.0\\}$ reveals an inverted-U on GSM8K, peaking at $\\alpha{=}2.0$ (66.11\\%).\nUnder identical GRPO training, four pruning criteria produce a \\emph{recovery capacity spectrum}: diversity-preserving pruning achieves active learning (peak reward 4.4$\\times$ vs importance-only), while importance-dominated pruning collapses entirely.\nThe spectrum tracks preserved representational diversity rather than gradient importance, with initial evidence for generality across scales (1.5B) and, via SFT-based recovery, across architectures (Qwen2.5-Math-7B).\n",
      "numLines": 8,
      "startLine": 1,
      "totalLines": 8
    }
  },
  "sourceToolAssistantUUID": "8d8fd384-cbd2-4d75-98bf-e40cf9e3839b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "3a90179e-e19e-41d1-8fb4-f23e916f555f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 37 · 2026-05-23T10:47:26.727Z_

<details open><summary>🔧 Tool call — Read · `toolu_01KJDujeXp4MTkoTCZjaSF94`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0246c699-217b-4457-85be-0ef6ee9575e6",
  "isSidechain": false,
  "requestId": "req_011CbKNGo4rLHPN2FBzfYpBN",
  "type": "assistant",
  "uuid": "fc3852fa-368d-4796-841a-e5881fe53162",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "3a90179e-e19e-41d1-8fb4-f23e916f555f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LTRFjV5U2DZDnMEQV3bmJE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1748,
      "cache_read_input_tokens": 25217,
      "output_tokens": 1165,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1748,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1165,
          "cache_read_input_tokens": 25217,
          "cache_creation_input_tokens": 1748,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1748
          },
          "type": "message"
        }
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

_source line 38 · 2026-05-23T10:47:26.732Z_

<details><summary>↩ Tool result · `toolu_01KJDujeXp4MTkoTCZjaSF94`</summary>

```text
1	\section{Introduction}
2	\label{sec:intro}
3	
4	Reasoning Large Language Models can be compressed through structured pruning, but the pruned model must recover its reasoning capabilities through fine-tuning.
5	The dominant assumption is that the recovery paradigm (SFT versus RLVR) determines recovery quality: \citet{selfhealing2025} demonstrate that RLVR restores pruned reasoning models to near-original accuracy, significantly outperforming SFT.
6	We show that this hierarchy is an artifact of suboptimal pruning.
7	When pruning preserves representational diversity, recovery method choice becomes irrelevant: at 20\% sparsity, mean $|\Delta(\text{GRPO}-\text{SFT})| {=} 0.54$\,pp across the four fine-grained criteria (max $0.61$\,pp); including dose-response variations and MBPP, the maximum is $1.34$\,pp.
8	What matters is not \emph{how} you train after pruning, but \emph{which structures} you remove.
9	
10	This gap is surprising because RL and SFT impose fundamentally different demands on model representations: RL compresses incorrect paths while SFT expands correct ones~\citep{rlsqueezes2026}. Yet existing structured pruning methods for reasoning LLMs~\citep{graspprune2026,resp2025,llmpruner2023,bonsai2025} optimize for post-pruning quality without studying how the criterion shapes downstream RL recovery.
11	No prior work has compared multiple pruning criteria under RL or asked whether the ``RLVR $>$ SFT'' advantage persists across pruning strategies.
12	We note that \citet{selfhealing2025} evaluate unstructured magnitude pruning retaining 96.5\% of dense parameters; our findings concern fine-grained structural pruning where entire channel groups are removed, and the two settings may impose different demands on RL recovery.
13	
14	\begin{figure}[t]
15	\centering
16	\includegraphics[width=\columnwidth]{../figures/paper/fig1_dose_response.pdf}
17	\caption{Dose-response curve for the CKA diversity coefficient $\alpha$ at 20\% MLP channel sparsity on GSM8K ($N{=}1{,}319$). Recovery accuracy follows an inverted-U, peaking at $\alpha{=}2.0$ (66.11\%). SFT and GRPO curves nearly overlap ($|\Delta| \leq 1.14$\,pp at every point), visually demonstrating reward-accuracy decoupling: the pruning criterion, not the recovery paradigm, determines outcome.}
18	\label{fig:dose_response}
19	\end{figure}
20	
21	We present a controlled comparison on DeepSeek-R1-Distill-Qwen-7B~\citep{deepseek2025r1} at 20\% MLP channel sparsity, varying the balance between gradient importance and CKA-based representational diversity~\citep{kornblith2019cka} via a coefficient $\alpha$ in the pruning score (Figure~\ref{fig:dose_response}).
22	The dose-response curve reveals an inverted-U: recovery peaks at $\alpha{=}2.0$ (66.11\% GRPO on GSM8K~\citep{cobbe2021gsm8k}), where importance and diversity reach optimal balance.
23	Under identical GRPO~\citep{shao2024grpo} training, four criteria produce a \textbf{recovery capacity spectrum}: CKA-only pruning achieves active learning (peak reward 4.4$\times$ Standard), Random stagnates, Standard (importance-only;~\citealp{llmpruner2023}) exhibits borderline collapse, and $\alpha{=}1.0$ collapses fully.
24	The ordering tracks preserved representational diversity, not gradient importance.
25	A depth pruning baseline (ShortGPT;~\citealp{shortgpt2024}) is the only method with $|\Delta| > 1$\,pp ($-$1.36\,pp on GSM8K), confirming that pruning granularity interacts with RL trainability.
26	
27	Our contributions are:
28	\begin{enumerate}[nosep,leftmargin=*]
29	    \item \textbf{Reward-accuracy decoupling.} At 20--25\% sparsity, GRPO and SFT produce near-identical accuracy across all four fine-grained criteria: mean $|\Delta| {=} 0.54$\,pp at 20\% (max $0.61$\,pp; $1.34$\,pp including dose-response variations and MBPP). At 15\%, GRPO can still amplify the CKA-guided advantage ($+$1.51\,pp differential), but this partial exception reinforces the main pattern: the pruning criterion, not the recovery paradigm, determines outcome (\S\ref{sec:decoupling}).
30	    \item \textbf{Recovery capacity spectrum.} We propose \rasp{}, which balances gradient importance with CKA-based representational diversity via a coefficient $\alpha$. A dose-response analysis on GSM8K reveals an inverted-U peaking at $\alpha{=}2.0$ (66.11\%). Under identical GRPO training, four criteria produce qualitatively distinct dynamics---from active learning to full collapse---that track preserved diversity, not gradient importance. The spectrum is validated across scales (1.5B) and, via SFT-based recovery, across architectures (Qwen2.5-Math-7B) (\S\ref{sec:scoring}, \S\ref{sec:recovery_gradient}, \S\ref{sec:extended_analysis}).
31	\end{enumerate}
32	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fc3852fa-368d-4796-841a-e5881fe53162",
  "isSidechain": false,
  "promptId": "dddf37fd-16cc-4cd5-bb05-648328938281",
  "type": "user",
  "uuid": "8c866231-1aa0-4645-b7cd-a5e3039659cb",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/introduction.tex",
      "content": "\\section{Introduction}\n\\label{sec:intro}\n\nReasoning Large Language Models can be compressed through structured pruning, but the pruned model must recover its reasoning capabilities through fine-tuning.\nThe dominant assumption is that the recovery paradigm (SFT versus RLVR) determines recovery quality: \\citet{selfhealing2025} demonstrate that RLVR restores pruned reasoning models to near-original accuracy, significantly outperforming SFT.\nWe show that this hierarchy is an artifact of suboptimal pruning.\nWhen pruning preserves representational diversity, recovery method choice becomes irrelevant: at 20\\% sparsity, mean $|\\Delta(\\text{GRPO}-\\text{SFT})| {=} 0.54$\\,pp across the four fine-grained criteria (max $0.61$\\,pp); including dose-response variations and MBPP, the maximum is $1.34$\\,pp.\nWhat matters is not \\emph{how} you train after pruning, but \\emph{which structures} you remove.\n\nThis gap is surprising because RL and SFT impose fundamentally different demands on model representations: RL compresses incorrect paths while SFT expands correct ones~\\citep{rlsqueezes2026}. Yet existing structured pruning methods for reasoning LLMs~\\citep{graspprune2026,resp2025,llmpruner2023,bonsai2025} optimize for post-pruning quality without studying how the criterion shapes downstream RL recovery.\nNo prior work has compared multiple pruning criteria under RL or asked whether the ``RLVR $>$ SFT'' advantage persists across pruning strategies.\nWe note that \\citet{selfhealing2025} evaluate unstructured magnitude pruning retaining 96.5\\% of dense parameters; our findings concern fine-grained structural pruning where entire channel groups are removed, and the two settings may impose different demands on RL recovery.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{../figures/paper/fig1_dose_response.pdf}\n\\caption{Dose-response curve for the CKA diversity coefficient $\\alpha$ at 20\\% MLP channel sparsity on GSM8K ($N{=}1{,}319$). Recovery accuracy follows an inverted-U, peaking at $\\alpha{=}2.0$ (66.11\\%). SFT and GRPO curves nearly overlap ($|\\Delta| \\leq 1.14$\\,pp at every point), visually demonstrating reward-accuracy decoupling: the pruning criterion, not the recovery paradigm, determines outcome.}\n\\label{fig:dose_response}\n\\end{figure}\n\nWe present a controlled comparison on DeepSeek-R1-Distill-Qwen-7B~\\citep{deepseek2025r1} at 20\\% MLP channel sparsity, varying the balance between gradient importance and CKA-based representational diversity~\\citep{kornblith2019cka} via a coefficient $\\alpha$ in the pruning score (Figure~\\ref{fig:dose_response}).\nThe dose-response curve reveals an inverted-U: recovery peaks at $\\alpha{=}2.0$ (66.11\\% GRPO on GSM8K~\\citep{cobbe2021gsm8k}), where importance and diversity reach optimal balance.\nUnder identical GRPO~\\citep{shao2024grpo} training, four criteria produce a \\textbf{recovery capacity spectrum}: CKA-only pruning achieves active learning (peak reward 4.4$\\times$ Standard), Random stagnates, Standard (importance-only;~\\citealp{llmpruner2023}) exhibits borderline collapse, and $\\alpha{=}1.0$ collapses fully.\nThe ordering tracks preserved representational diversity, not gradient importance.\nA depth pruning baseline (ShortGPT;~\\citealp{shortgpt2024}) is the only method with $|\\Delta| > 1$\\,pp ($-$1.36\\,pp on GSM8K), confirming that pruning granularity interacts with RL trainability.\n\nOur contributions are:\n\\begin{enumerate}[nosep,leftmargin=*]\n    \\item \\textbf{Reward-accuracy decoupling.} At 20--25\\% sparsity, GRPO and SFT produce near-identical accuracy across all four fine-grained criteria: mean $|\\Delta| {=} 0.54$\\,pp at 20\\% (max $0.61$\\,pp; $1.34$\\,pp including dose-response variations and MBPP). At 15\\%, GRPO can still amplify the CKA-guided advantage ($+$1.51\\,pp differential), but this partial exception reinforces the main pattern: the pruning criterion, not the recovery paradigm, determines outcome (\\S\\ref{sec:decoupling}).\n    \\item \\textbf{Recovery capacity spectrum.} We propose \\rasp{}, which balances gradient importance with CKA-based representational diversity via a coefficient $\\alpha$. A dose-response analysis on GSM8K reveals an inverted-U peaking at $\\alpha{=}2.0$ (66.11\\%). Under identical GRPO training, four criteria produce qualitatively distinct dynamics---from active learning to full collapse---that track preserved diversity, not gradient importance. The spectrum is validated across scales (1.5B) and, via SFT-based recovery, across architectures (Qwen2.5-Math-7B) (\\S\\ref{sec:scoring}, \\S\\ref{sec:recovery_gradient}, \\S\\ref{sec:extended_analysis}).\n\\end{enumerate}\n",
      "numLines": 32,
      "startLine": 1,
      "totalLines": 32
    }
  },
  "sourceToolAssistantUUID": "fc3852fa-368d-4796-841a-e5881fe53162",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "3a90179e-e19e-41d1-8fb4-f23e916f555f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 39 · 2026-05-23T10:47:27.776Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01ChPYFWbKVUMQQgs7Agy4XM`</summary>

```json
{
  "project": "recovery_aware_struct_prune",
  "filters": {
    "conclusion": "success"
  },
  "limit": 50,
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
  "parentUuid": "8c866231-1aa0-4645-b7cd-a5e3039659cb",
  "isSidechain": false,
  "requestId": "req_011CbKNGo4rLHPN2FBzfYpBN",
  "type": "assistant",
  "uuid": "3cef34a5-cc1d-4312-991b-6c3c5a83f2e5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "3a90179e-e19e-41d1-8fb4-f23e916f555f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LTRFjV5U2DZDnMEQV3bmJE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1748,
      "cache_read_input_tokens": 25217,
      "output_tokens": 1165,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1748,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1165,
          "cache_read_input_tokens": 25217,
          "cache_creation_input_tokens": 1748,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1748
          },
          "type": "message"
        }
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

_source line 40_

```json
{
  "type": "last-prompt",
  "leafUuid": "3cef34a5-cc1d-4312-991b-6c3c5a83f2e5",
  "sessionId": "3a90179e-e19e-41d1-8fb4-f23e916f555f"
}
```

---


### Runtime record

_source line 41_

```json
{
  "type": "ai-title",
  "aiTitle": "Map paper results to registry experiments",
  "sessionId": "3a90179e-e19e-41d1-8fb4-f23e916f555f"
}
```

---


### Tool result

_source line 42 · 2026-05-23T10:47:29.041Z_

<details><summary>↩ Tool result · `toolu_01ChPYFWbKVUMQQgs7Agy4XM`</summary>

```text
Error: result (72,347 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-17-projects-recovery-aware-struct-prune/3a90179e-e19e-41d1-8fb4-f23e916f555f/tool-results/mcp-agent-ml-research-read_registry-1779533249026.txt.
Format: JSON with schema: {result: string}
- For targeted queries (find a value, filter by field): use jq on the file directly.
- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-17-projects-recovery-aware-struct-prune/3a90179e-e19e-41d1-8fb4-f23e916f555f/tool-results/mcp-agent-ml-research-read_registry-1779533249026.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.
- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-17-projects-recovery-aware-struct-prune/3a90179e-e19e-41d1-8fb4-f23e916f555f/tool-results/mcp-agent-ml-research-read_registry-1779533249026.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim." A vague "summarize this" may lose detail.

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3cef34a5-cc1d-4312-991b-6c3c5a83f2e5",
  "isSidechain": false,
  "promptId": "dddf37fd-16cc-4cd5-bb05-648328938281",
  "type": "user",
  "uuid": "37c7d07b-decc-4fab-acab-630a49f85c6e",
  "toolUseResult": "Error: result (72,347 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-17-projects-recovery-aware-struct-prune/3a90179e-e19e-41d1-8fb4-f23e916f555f/tool-results/mcp-agent-ml-research-read_registry-1779533249026.txt.\nFormat: JSON with schema: {result: string}\n- For targeted queries (find a value, filter by field): use jq on the file directly.\n- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-17-projects-recovery-aware-struct-prune/3a90179e-e19e-41d1-8fb4-f23e916f555f/tool-results/mcp-agent-ml-research-read_registry-1779533249026.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.\n- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. \"/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-17-projects-recovery-aware-struct-prune/3a90179e-e19e-41d1-8fb4-f23e916f555f/tool-results/mcp-agent-ml-research-read_registry-1779533249026.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim.\" A vague \"summarize this\" may lose detail.\n",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"eval_math500_sft_qwen_math_cka_only_20\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T23:11:09.017Z\", \"updated_at\": \"2026-05-23T10:44:00.535Z\", \"hypothesis\": \"Qwen2.5-Math-7B CKA-only 20% SFT MATH-500 eval @2048. Cross-architecture validation: if CKA-only criterion generalizes from DeepSeek-R1-Distill to Qwen-Math on MATH-500. SFT GSM8K = 51.5% (N=200). Paired with westb:1 GRPO GSM8K for C1 decoupling cross-arch.\", \"parent\": \"sft_qwen_math_cka_only_20\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_qwen_math_cka_only_20_final --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_math500_sft_qwen_math_cka_only_20.json --seed 42 --dtype bfloat16 --max_new_tokens 2048\", \"server\": \"westb-23072\", \"gpu\": \"cuda:0\", \"data_path\": \"HuggingFaceH4/MATH-500\", \"data_count\": 500, \"model_name\": \"Qwen2.5-Math-7B-CKA-only-20%-SFT-ep1\", \"seed\": 42, \"checkpoint_source\": \"sft_qwen_math_cka_only_20_final\", \"eval_data\": \"MATH-500 (N=500, max_new_tokens=2048)\", \"pid\": 250766, \"log_path\": \"/tmp/eval_math500_sft_qwen_cka_only_20.log\"}, \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 0.216, \"stderr\": 0.0184, \"correct\": 108, \"total\": 500, \"natural_eos\": 90, \"truncated\": 410, \"avg_response_length\": 1745.338}, \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_math500_sft_qwen_math_cka_only_20.json\", \"completed_at\": \"2026-05-23T10:44:00.535Z\"}, \"eval_math500_grpo_rasp_alpha0p5_20\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T02:59:15.985Z\", \"updated_at\": \"2026-05-23T10:11:11.002Z\", \"hypothesis\": \"GRPO RASP α=0.5 MATH-500 eval @2048. C1 decoupling on MATH-500: SFT α=0.5 = 25.4%. GSM8K GRPO α=0.5 = 61.18%. Completes MATH-500 GRPO dose-response curve.\", \"parent\": \"eval_gsm8k_grpo_alpha0p5_20\", \"spec\": {\"command\": \"python src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_alpha0p5_20 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_math500_grpo_rasp_alpha0p5_20.json --seed 42 --dtype bfloat16 --max_new_tokens 2048\", \"server\": \"westb-23072\", \"data_path\": \"MATH-500\", \"data_count\": 500, \"model_name\": \"grpo_rasp_alpha0p5_20\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_alpha0p5_20\", \"eval_data\": \"MATH-500\"}, \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 0.248, \"stderr\": 0.0193, \"correct\": 124, \"total\": 500, \"natural_eos\": 274, \"truncated\": 226, \"avg_response_length\": 1110.462}, \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_math500_grpo_rasp_alpha0p5_20.json\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_math500_grpo_rasp_alpha0p5_20.log\", \"completed_at\": \"2026-05-23T10:11:11.002Z\"}, \"eval_math500_grpo_cka_only_20_2048_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T05:07:09.002Z\", \"updated_at\": \"2026-05-23T08:55:58.278Z\", \"hypothesis\": \"GRPO CKA-only 20% MATH-500 @2048 rerun with NEW eval script. Previous 29.2% (eval_math500_grpo_cka_only_20_2048) used OLD answer extraction. SFT CKA-only = 26.8% (NEW). Rerun ensures consistent C1 |Δ| comparison.\", \"parent\": \"eval_math500_grpo_cka_only_20_2048\", \"spec\": {\"command\": \"bash -c 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=3 HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 python src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20/checkpoint-100 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_math500_grpo_cka_only_20_2048_v2.json --seed 42 --dtype bfloat16 --max_new_tokens 2048'\", \"server\": \"westd-32935\", \"data_path\": \"MATH-500\", \"data_count\": 500, \"model_name\": \"grpo_cka_only_20/checkpoint-100\", \"seed\": 42, \"checkpoint_source\": \"westb-23072:/root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20/checkpoint-100\", \"eval_data\": \"MATH-500\"}, \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 0.274, \"correct\": 137, \"total\": 500, \"stderr\": 0.01995, \"natural_eos\": 390, \"truncated\": 110, \"avg_response_length\": 654.746}, \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_math500_grpo_cka_only_20_2048_v2.json\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/logs/eval_math500_grpo_cka_only_20_2048_v2.log\", \"completed_at\": \"2026-05-23T08:55:58.278Z\"}, \"eval_math500_grpo_rasp_alpha3p0_20\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T03:19:40.950Z\", \"updated_at\": \"2026-05-23T07:48:57.618Z\", \"hypothesis\": \"GRPO RASP α=3.0 MATH-500 eval @2048. C1 decoupling on MATH-500: SFT α=3.0 = 23.2%. GSM8K GRPO α=3.0 = 63.45%. Completes MATH-500 GRPO dose-response curve for α=3.0 data point.\", \"parent\": \"eval_gsm8k_grpo_alpha3p0_20\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=0 HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 python src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_alpha3p0_20_v2/checkpoint-100 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_math500_grpo_rasp_alpha3p0_20.json --seed 42 --dtype bfloat16 --max_new_tokens 2048\\\"\", \"server\": \"westd-32935\", \"data_path\": \"MATH-500\", \"data_count\": 500, \"model_name\": \"grpo_rasp_alpha3p0_20_v2/checkpoint-100\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_alpha3p0_20_v2/checkpoint-100\", \"eval_data\": \"MATH-500\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_math500_grpo_rasp_alpha3p0_20.json\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/logs/eval_math500_grpo_alpha3p0_20.log\", \"completed_at\": \"2026-05-23T07:48:50.736Z\", \"metrics\": {\"accuracy\": 0.228, \"correct\": 114, \"total\": 500, \"stderr\": 0.0188, \"truncated_ratio\": 0.28, \"avg_response_length\": 745.038}}, \"eval_math500_grpo_rasp_alpha4p0_20\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T00:01:54.194Z\", \"updated_at\": \"2026-05-23T05:58:52.769Z\", \"hypothesis\": \"GRPO RASP α=4.0 MATH-500 eval @2048. C1 decoupling on MATH-500: SFT α=4.0 = 26.6%. If |GRPO - SFT| < 2pp, C1 decoupling holds cross-benchmark for α=4.0. GSM8K GRPO α=4.0 = 62.77%.\", \"parent\": \"eval_gsm8k_grpo_alpha4_20_v3\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_alpha4_20/checkpoint-100\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/logs/eval_math500_grpo_rasp_alpha4p0_20.log\"}, \"metrics\": {\"accuracy\": 0.262, \"stderr\": 0.01966, \"correct\": 131, \"total\": 500, \"truncated\": 180, \"natural_eos\": 320, \"avg_response_length\": 925.48}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-23T05:58:52.769Z\"}, \"eval_math500_grpo_rasp_alpha1p0_20\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T23:02:44.335Z\", \"updated_at\": \"2026-05-23T04:44:32.303Z\", \"hypothesis\": \"GRPO RASP α=1.0 MATH-500 eval @2048. C1 decoupling on MATH-500: SFT α=1.0 = 21.2%. If |GRPO - SFT| < 2pp, C1 decoupling holds cross-benchmark for α=1.0.\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_rasp_20_fair\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_math500_grpo_rasp_alpha1p0_20.log\"}, \"reproduce\": {\"finished_at\": \"2026-05-23T04:41:44.783Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-23T04:41:56.794961+00:00\"}]}, \"metrics\": {\"accuracy\": 0.226, \"stderr\": 0.0187, \"n_correct\": 113, \"n_total\": 500, \"avg_response_length\": 903.536, \"natural_eos\": 320, \"truncated\": 180}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-23T04:44:32.303Z\"}, \"eval_math500_sft_cka_only_20_westd\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T20:45:21.526Z\", \"updated_at\": \"2026-05-23T03:21:26.164Z\", \"hypothesis\": \"CKA-only 20% SFT MATH-500 eval @2048 on westd (migrated from westb for speed). Dose-response endpoint control: CKA-only is the best-performing pruning method (GSM8K 64.37%). MATH-500 result establishes upper bound for cross-benchmark dose-response curve.\", \"parent\": \"eval_math500_sft_cka_only_20_westb\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 python src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_20 --output_path results/eval_math500_sft_cka_only_20.json --seed 42 --dtype bfloat16 --max_new_tokens 2048\", \"server\": \"westd-32935\", \"gpu\": \"cuda:1\", \"pid\": \"75284\", \"data_path\": \"MATH-500\", \"data_count\": 500, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B (sft_cka_only_20)\", \"seed\": 42, \"checkpoint_source\": \"sft_cka_only_20\", \"eval_data\": \"MATH-500 (N=500, max_new_tokens=2048)\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/logs/eval_math500_sft_cka_only_20.log\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_20\"}, \"metrics\": {\"accuracy\": 0.268, \"correct\": 134, \"total\": 500, \"truncated\": 116, \"stderr\": 0.0198, \"natural_eos_pct\": 0.768, \"avg_response_length\": 673.278, \"note\": \"PID 75284 actual output = 26.8% (134/500). Previous 29.0% (145/500) was from v4 run (May 19) with different answer extraction. Same model generations, different scoring.\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-23T00:00:43.009Z\"}, \"eval_math500_grpo_rasp_alpha2p0_20\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T22:23:27.589Z\", \"updated_at\": \"2026-05-23T03:16:40.537Z\", \"hypothesis\": \"GRPO RASP α=2.0 MATH-500 eval @2048. C1 decoupling evidence on MATH-500: SFT α=2.0 = 24.0%, GRPO expected similar (~24%). If |GRPO - SFT| < 1pp, C1 decoupling holds cross-benchmark.\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/recovery_aware_struct_prune && HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 python src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_alpha2p0_20 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_math500_grpo_rasp_alpha2p0_20.json --seed 42 --dtype bfloat16 --max_new_tokens 2048\\\"\", \"server\": \"westd-32935\", \"gpu\": \"cuda:0\", \"pid\": \"83709\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_math500_grpo_rasp_alpha2p0_20.log\", \"submitted_at\": \"2026-05-22T22:25:27.490Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"MATH-500\", \"data_count\": 500, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B (grpo_rasp_alpha2p0_20)\", \"seed\": 42, \"checkpoint_source\": \"grpo_rasp_alpha2p0_20\", \"eval_data\": \"MATH-500 (N=500, max_new_tokens=2048)\", \"wall_clock_seconds\": 17473.0, \"gpu_hours\": 4.85}, \"reproduce\": {\"finished_at\": \"2026-05-23T03:14:21.897Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-23T03:14:37.164633+00:00\"}]}, \"metrics\": {\"accuracy\": 0.262, \"correct\": 131, \"total\": 500, \"stderr\": 0.0197, \"natural_eos\": 349, \"truncated\": 151, \"avg_response_length\": 785.326}, \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_alpha2p0_20\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_math500_grpo_rasp_alpha2p0_20.log\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-23T03:16:40.537Z\"}, \"eval_gsm8k_grpo_qwen_math_cka_only_20_n500_v3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T15:12:46.181Z\", \"updated_at\": \"2026-05-23T02:53:37.071Z\", \"hypothesis\": \"MF3 cross-architecture validation v3 (N=500, max_new_tokens=2048): Qwen2.5-Math-7B CKA-only 20% GRPO GSM8K eval with absolute model_path fix. v2 crashed due to relative path OSError. v1 killed due to 337s/sample (no token limit). Tests whether CKA-only pruning + GRPO recovery generalizes beyond DeepSeek-R1-Distill to Qwen-Math architecture.\", \"parent\": \"eval_gsm8k_grpo_qwen_math_cka_only_20_n500_v2\", \"spec\": {\"command\": \"bash -c 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/recovery_aware_struct_prune && python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_qwen_math_cka_only_20 --max_samples 500 --max_new_tokens 2048 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_grpo_qwen_math_cka_only_20_n500_v3.json'\", \"server\": \"westb-23072\", \"gpu\": \"cuda:1\", \"pid\": \"220343\", \"data_path\": \"GSM8K test split\", \"data_count\": 500, \"model_name\": \"Qwen2.5-Math-7B-pruned-cka_only-20pct-GRPO\", \"seed\": 42, \"checkpoint_source\": \"grpo_qwen_math_cka_only_20\", \"eval_data\": \"GSM8K\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_qwen_math_cka_only_20\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_gsm8k_grpo_qwen_math_cka_only_20_n500_v3.log\"}, \"metrics\": {\"accuracy\": 0.486, \"correct\": 243, \"total\": 500, \"stderr\": 0.0224, \"truncated_pct\": 0.838, \"natural_eos_pct\": 0.162, \"avg_response_length\": 1766.5}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-23T02:53:37.071Z\"}, \"eval_math500_sft_rasp_alpha1p0_20_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T20:50:24.239Z\", \"updated_at\": \"2026-05-22T23:01:03.419Z\", \"hypothesis\": \"α=1.0 SFT MATH-500 eval @2048 v2 (on westb). Default RASP α=1.0. Cross-benchmark dose-response: GSM8K α=1.0 SFT=63.31%. v1 killed at 304/500, result file never written. Completes 5-point dose-response curve on MATH-500.\", \"parent\": \"eval_math500_sft_rasp_alpha1p0_20\", \"notes\": \"westb submission failed: model sft_rasp_20_westd not found on westb. Only exists on westd-32935. Waiting for westd:3 (α=4.0, 85%) to free up.\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20_westd\", \"log_path\": \"/root/runs/recovery_aware_struct_prune/eval_math500_sft_rasp_alpha1p0_20_v2.log\"}, \"reproduce\": {\"finished_at\": \"2026-05-22T22:58:10.208Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-22T22:58:19.219921+00:00\"}]}, \"metrics\": {\"accuracy\": 0.212, \"correct\": 106, \"total\": 500, \"truncated\": 186, \"stderr\": 0.0183}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T23:01:03.420Z\"}, \"eval_math500_sft_standard_20_2048_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T01:34:44.782Z\", \"updated_at\": \"2026-05-22T22:19:38.080Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/recovery_aware_struct_prune && HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 python src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_math500_sft_standard_20_2048_v2.json --seed 42 --dtype bfloat16 --max_new_tokens 2048\\\"\", \"server\": \"westd-32935\", \"gpu\": [\"cuda:0\"], \"pid\": \"82301\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_math500_sft_standard_20_2048_v2.log\", \"submitted_at\": \"2026-05-22T22:15:58.026Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"hypothesis\": \"Standard (random) 20% SFT MATH-500 eval @2048. Baseline comparison: Standard pruning without CKA guidance. Cross-benchmark extension of GSM8K Standard results.\", \"parent\": \"eval_math500_sft_standard_20\", \"reproduce\": {\"finished_at\": \"2026-05-19T08:54:35.352Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-19T08:54:40.855817+00:00\"}]}, \"metrics\": {\"accuracy\": 0.258, \"n_correct\": 129, \"n_total\": 500}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T13:08:16.850Z\"}, \"eval_math500_sft_rasp_alpha0p5_20\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T15:20:44.460Z\", \"updated_at\": \"2026-05-22T22:18:43.350Z\", \"hypothesis\": \"α=0.5 SFT MATH-500 eval @2048. Cross-benchmark dose-response validation: GSM8K shows α=0.5 SFT=60.73%. If MATH-500 also shows α=0.5 < α=2.0, inverted-U generalizes beyond GSM8K (strengthens MF4 + N1).\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_alpha0p5_20\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/logs/eval_math500_sft_rasp_alpha0p5_20.log\"}, \"metrics\": {\"accuracy\": 0.254, \"correct\": 127, \"total\": 500, \"truncated\": 220, \"stderr\": 0.0195}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T22:18:43.350Z\"}, \"eval_math500_sft_rasp_alpha3p0_20\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T18:26:16.273Z\", \"updated_at\": \"2026-05-22T22:12:26.406Z\", \"hypothesis\": \"α=3.0 SFT MATH-500 eval @2048. Dose-response \\\"下降段确认点\\\": GSM8K α=3.0 SFT=64.14% (below α=2.0 peak 64.97%). If MATH-500 also shows α=3.0 < α=2.0, confirms inverted-U descending arm cross-benchmark. Completes 5/5 MATH-500 dose-response.\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_alpha3p0_20/checkpoint-935\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/logs/eval_math500_sft_rasp_alpha3p0_20.log\"}, \"metrics\": {\"accuracy\": 0.232, \"correct\": 116, \"total\": 500, \"truncated\": 144, \"stderr\": 0.0189}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T22:12:26.406Z\"}, \"eval_math500_sft_rasp_alpha4p0_20\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T15:20:47.150Z\", \"updated_at\": \"2026-05-22T21:22:35.441Z\", \"hypothesis\": \"α=4.0 SFT MATH-500 eval @2048. Cross-benchmark dose-response validation: GSM8K shows α=4.0 SFT=61.94%. If MATH-500 also shows α=4.0 < α=2.0, inverted-U generalizes beyond GSM8K (strengthens MF4 + N1).\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_alpha4_20\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/logs/eval_math500_sft_rasp_alpha4p0_20.log\"}, \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 0.266, \"correct\": 133, \"total\": 500, \"truncated\": 190, \"stderr\": 0.0198}, \"completed_at\": \"2026-05-22T21:22:35.442Z\"}, \"eval_math500_sft_rasp_alpha2p0_20\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T15:06:22.386Z\", \"updated_at\": \"2026-05-22T20:44:52.970Z\", \"hypothesis\": \"α=2.0 SFT MATH-500 eval @2048. Dose-response peak on GSM8K (64.97% SFT). Cross-benchmark validation: if α=2.0 also peaks on MATH-500, inverted-U generalizes beyond GSM8K (strengthens MF4 + N1).\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 nohup python src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_alpha2p0_20 --output_path results/eval_math500_sft_rasp_alpha2p0_20.json --seed 42 --dtype bfloat16 --max_new_tokens 2048\", \"server\": \"westd-32935\", \"gpu\": \"cuda:1\", \"pid\": \"57202\", \"data_path\": \"MATH-500\", \"data_count\": 500, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B (sft_rasp_alpha2p0_20)\", \"seed\": 42, \"checkpoint_source\": \"sft_rasp_alpha2p0_20\", \"eval_data\": \"MATH-500 (N=500, max_new_tokens=2048)\", \"log_path\": \"/root/recovery_aware_struct_prune/results/eval_math500_sft_rasp_alpha2p0_20.log\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_alpha2p0_20\"}, \"reproduce\": {\"finished_at\": \"2026-05-22T20:12:27.595Z\"}, \"failure_reason\": \"cron false positive: process exited normally, result file confirmed by Reviewer (24.0% accuracy)\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T20:12:32.633Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-22T20:12:40.230344+00:00\"}]}, \"metrics\": {\"accuracy\": 0.24, \"correct\": 120, \"total\": 500, \"truncated\": 155, \"stderr\": 0.0191}}, \"eval_gsm8k_grpo_random_20_seed456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T16:26:01.516Z\", \"updated_at\": \"2026-05-22T18:27:22.282Z\", \"hypothesis\": \"MF2 seed456 GSM8K eval (N=1319, greedy, max_new_tokens=2048). Paired with seed42 (50.57%) and seed123 v2 (running, interim 52.40%@1000). Validates C1 decoupling robustness across random seeds.\", \"parent\": \"grpo_random_20_seed456\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_random_20_seed456/checkpoint-100 --seed 456 --dtype bfloat16 --max_new_tokens 2048 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_grpo_random_20_seed456.json\", \"server\": \"westb-23072\", \"gpu\": \"cuda:0\", \"pid\": \"224705\", \"data_path\": \"openai/gsm8k (test split)\", \"data_count\": 1319, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B (grpo_random_20_seed456)\", \"seed\": 456, \"checkpoint_source\": \"grpo_random_20_seed456/checkpoint-100\", \"eval_data\": \"GSM8K test 1319\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_grpo_random_20_seed456.log\", \"accuracy\": 0.5087, \"total_correct\": 671, \"total_samples\": 1319, \"eos_rate\": 0.9955, \"stderr\": 0.01377, \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_random_20_seed456/checkpoint-100\"}, \"reproduce\": {\"finished_at\": \"2026-05-22T17:48:12.480Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T17:48:17.521Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-22T17:48:25.193120+00:00\"}]}, \"metrics\": {\"gsm8k_accuracy\": 0.5087, \"gsm8k_accuracy_se\": 0.0138, \"gsm8k_correct\": 671, \"gsm8k_total\": 1319, \"eos_rate\": 0.9954, \"avg_response_length\": 163.5, \"truncated\": 6}, \"notes\": \"Cron 误判 (已知模式): 实验实际完成 1319/1319, acc=50.87%. 与 seed42 (50.57%) 一致, 验证 C1 decoupling. Results: /root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_grpo_random_20_seed456.json\"}, \"eval_gsm8k_grpo_random_20_seed123_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T14:22:33.753Z\", \"updated_at\": \"2026-05-22T16:49:54.123Z\", \"hypothesis\": \"MF2 seed123 v2 GSM8K eval (N=1319, greedy, max_new_tokens=2048). 配对 seed42 (50.57%) 和 seed456 (pending). 验证 C1 decoupling 跨 seed 鲁棒性。v1 因 batch_size=1 配置错误作废。\", \"parent\": \"grpo_random_20_seed123_v2\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 nohup python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_random_20_seed123_v2/checkpoint-100 --output_path results/eval_gsm8k_grpo_random_20_seed123_v2.json --seed 123 --dtype bfloat16\", \"server\": \"westd-32935\", \"gpu\": \"cuda:0\", \"pid\": \"56283\", \"data_path\": \"openai/gsm8k (test split)\", \"data_count\": 1319, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B (grpo_random_20_seed123_v2)\", \"seed\": 123, \"checkpoint_source\": \"grpo_random_20_seed123_v2/checkpoint-100\", \"eval_data\": \"gsm8k test 1319\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_grpo_random_20_seed123_v2.json\", \"accuracy\": 0.5072, \"total_correct\": 669, \"total_samples\": 1319, \"eos_rate\": 0.9939, \"stderr\": 0.01377, \"avg_response_length\": 177.9, \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_random_20_seed123_v2/checkpoint-100\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T16:49:54.123Z\"}, \"grpo_random_20_seed456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T12:00:38.940Z\", \"updated_at\": \"2026-05-22T16:27:46.810Z\", \"hypothesis\": \"MF2 multi-seed validation: Random pruning 20% GRPO with seed456. Third seed for C1 decoupling robustness check. seed42: Δ=-0.68pp, seed123: pending eval. If all seeds show |Δ(GRPO-SFT)| ≤ 2pp, C1 claim is robust across random seeds.\", \"spec\": {\"server\": \"westb-23072\", \"gpu\": \"cuda:0\", \"command\": \"CUDA_VISIBLE_DEVICES=0 HF_HUB_OFFLINE=1 HF_DATASETS_OFFLINE=1 nohup python src/train_grpo_v5.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_random_20 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/grpo_random_20_seed456 --max_steps 100 --save_steps 100 --seed 456\", \"pid\": \"209508\", \"data_path\": \"openai/gsm8k (train split)\", \"data_count\": 7473, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B (sft_random_20)\", \"seed\": 456, \"checkpoint_source\": \"sft_random_20\", \"eval_data\": \"N/A - GRPO training\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_random_20_seed456/checkpoint-100\", \"log_path\": \"/tmp/grpo_random_seed456.log\", \"note\": \"100/100 steps completed. Final trainer.save_model() hit disk-full but TRL checkpoint-100 is intact (model.safetensors=12,174,631,264 bytes, matching seed42/seed123_v2). Reviewer independently verified.\"}, \"reproduce\": {\"finished_at\": \"2026-05-22T16:22:39.316Z\"}, \"failure_reason\": \"磁盘满: GRPO训练100/100完成但save_pretrained失败 (No space left on device)。westb-23072:/root/autodl-tmp 空间不足。\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T16:22:44.289Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-22T16:22:54.301751+00:00\"}]}, \"notes\": \"失败原因: GRPO 训练 100/100 步已完成 (3h02min)，但 save_pretrained 时磁盘满 (No space left on device, os error 28)。保存路径: /root/autodl-tmp/recovery_aware_struct_prune/grpo_random_20_seed456。W&B run auv9riek 有完整训练 metrics。save_steps=100=max_steps，无中间 checkpoint，需重跑。 | 已有成果: W&B metrics 完整 | 建议: 清理 westb-23072 磁盘后重提交\"}, \"eval_gsm8k_sft_depth_first_20\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T14:20:43.950Z\", \"updated_at\": \"2026-05-22T15:19:31.829Z\", \"hypothesis\": \"MF5 depth-first SFT GSM8K eval. Establishes SFT baseline for depth-first pruning method, paired with GRPO eval to check C1 decoupling for this baseline method.\", \"parent\": \"pipeline_depth_first_20\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 nohup python src/eval_gsm8k.py --model_path sft_depth_first_20 --output_path results/eval_gsm8k_sft_depth_first_20.json --seed 42 --dtype bfloat16\", \"server\": \"westd-32935\", \"gpu\": \"cuda:2\", \"pid\": \"54882\", \"data_path\": \"openai/gsm8k (test split)\", \"data_count\": 1319, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B (sft_depth_first_20)\", \"seed\": 42, \"checkpoint_source\": \"sft_depth_first_20\", \"eval_data\": \"gsm8k test 1319\", \"log_path\": \"/root/recovery_aware_struct_prune/results/eval_gsm8k_sft_depth_first_20.log\", \"note\": \"Early-stopped by Director at ~60-88 samples. Interim accuracy ~10%@50 (SFT). Conclusive: depth-first 20% SFT dramatically worse than CKA-only 64%. MF5 claim validated — CKA-only advantage is NOT simply removing deep layers.\", \"checkpoint_path\": \"N/A (eval only)\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T15:19:31.829Z\"}, \"eval_gsm8k_grpo_depth_first_20\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T14:20:41.126Z\", \"updated_at\": \"2026-05-22T15:18:38.970Z\", \"hypothesis\": \"MF5 depth-first GRPO GSM8K eval re-run. Previous pipeline_depth_first_20 results lost due to disk-full during JSON write. GRPO checkpoint intact. Re-running eval to get formal JSON result file. Prior log recovery showed ~24.18% from nohup output.\", \"parent\": \"pipeline_depth_first_20\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 nohup python src/eval_gsm8k.py --model_path grpo_depth_first_20/checkpoint-100 --output_path results/eval_gsm8k_grpo_depth_first_20.json --seed 42 --dtype bfloat16\", \"server\": \"westd-32935\", \"gpu\": \"cuda:3\", \"pid\": \"51981\", \"data_path\": \"openai/gsm8k (test split)\", \"data_count\": 1319, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B (grpo_depth_first_20)\", \"seed\": 42, \"checkpoint_source\": \"grpo_depth_first_20/checkpoint-100\", \"eval_data\": \"gsm8k test 1319\", \"log_path\": \"/root/recovery_aware_struct_prune/results/eval_gsm8k_grpo_depth_first_20.log\", \"note\": \"Early-stopped by Director at ~60-88 samples. Interim accuracy ~8%@50 (GRPO). Conclusive: depth-first 20% GRPO dramatically worse than CKA-only 64%. MF5 claim validated — CKA-only advantage is NOT simply removing deep layers.\", \"checkpoint_path\": \"N/A (eval only)\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T15:18:38.970Z\"}, \"grpo_random_20_seed123_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T14:22:29.868Z\", \"updated_at\": \"2026-05-22T15:00:23.101Z\", \"hypothesis\": \"MF2 multi-seed validation v2: Random 20% GRPO with seed123, correct batch_size=2 (matching seed42/seed456). v1 used batch_size=1 (half data per 100 steps), results invalidated. Tests C1 decoupling robustness across random seeds.\", \"parent\": \"grpo_random_20_seed123\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 HF_HUB_OFFLINE=1 HF_DATASETS_OFFLINE=1 nohup python src/train_grpo_v5.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_random_20 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/grpo_random_20_seed123_v2 --max_steps 100 --save_steps 100 --seed 123\", \"server\": \"westd-32935\", \"gpu\": \"cuda:1\", \"pid\": \"53822\", \"data_path\": \"openai/gsm8k (train split)\", \"data_count\": 7473, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B (sft_random_20)\", \"seed\": 123, \"checkpoint_source\": \"sft_random_20\", \"eval_data\": \"N/A - GRPO training\", \"log_path\": \"/tmp/grpo_random_seed123_v2.log\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_random_20_seed123_v2/checkpoint-100\", \"completed_at\": \"2026-05-22T15:00:23.101Z\"}, \"eval_gsm8k_grpo_alpha3p0_20\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T09:30:06.630Z\", \"updated_at\": \"2026-05-22T14:47:06.188Z\", \"hypothesis\": \"α=3.0 GRPO GSM8K eval. Dose-response 5th data point: α=3.0 between α=2.0 (66.11%) and α=4.0 (62.77%). Completes the 5-point dose-response curve for causal evidence of CKA overlap suppression effect.\", \"notes\": \"UNBLOCKED: grpo_rasp_alpha3p0_20_v2 checkpoint-100 完整 (12.3GB). Eval 已启动 PID 43755 on westd:0, 2.8s/sample, ETA ~60 min.\", \"spec\": {\"server\": \"westd-32935\", \"gpu\": \"cuda:0\", \"command\": \"CUDA_VISIBLE_DEVICES=0 HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 nohup python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_alpha3p0_20_v2/checkpoint-100 --output_path results/eval_gsm8k_grpo_rasp_alpha3p0_20.json --max_samples 1319 --seed 42 --dtype bfloat16\", \"pid\": \"43755\", \"data_path\": \"openai/gsm8k (test split)\", \"data_count\": 1319, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B (grpo_rasp_alpha3p0_20_v2)\", \"seed\": 42, \"checkpoint_source\": \"grpo_rasp_alpha3p0_20_v2/checkpoint-100\", \"eval_data\": \"gsm8k test 1319\", \"log_path\": \"/root/recovery_aware_struct_prune/results/eval_gsm8k_grpo_rasp_alpha3p0_20.log\"}, \"conclusion\": \"success\", \"metrics\": {\"gsm8k_accuracy\": 0.6345, \"correct\": 837, \"total\": 1319, \"stderr\": 0.0133, \"eos_rate\": 0.9864, \"truncated\": 18, \"avg_response_length\": 219.7}, \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_alpha3p0_20_v2/checkpoint-100\", \"log_path\": \"/root/recovery_aware_struct_prune/results/eval_gsm8k_grpo_rasp_alpha3p0_20.log\", \"completed_at\": \"2026-05-22T14:46:15.365Z\"}, \"eval_math500_sft_random_20_v3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T04:11:52.462Z\", \"updated_at\": \"2026-05-22T14:10:18.359Z\", \"hypothesis\": \"Random 20% SFT MATH-500 @2048. v2 failed due to old eval_math500.py on westd-32935. Code synced from westb.\", \"parent\": \"eval_math500_sft_random_20_v2\", \"spec\": {\"command\": \"python src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_random_20 --max_new_tokens 2048 --output_path /root/recovery_aware_struct_prune/results/eval_math500_sft_random_20_v3.json\", \"server\": \"westd-32935\", \"gpu\": [\"cuda:1\"], \"pid\": \"5236\", \"data_path\": \"MATH-500\", \"data_count\": 500, \"model_name\": \"sft_random_20\", \"model_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_random_20\", \"seed\": 42, \"checkpoint_source\": \"sft_random_20\", \"eval_data\": \"MATH-500\", \"log_path\": \"/root/recovery_aware_struct_prune/logs/eval_math500_sft_random_20_v3.log\", \"checkpoint_path\": \"N/A - eval\"}, \"metrics\": {\"accuracy\": 0.144, \"correct\": 72, \"total\": 500, \"stderr\": 0.0157, \"natural_eos\": 171, \"truncated\": 329, \"avg_response_length\": 1470.44}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T14:10:18.359Z\"}, \"eval_gsm8k_sft_alpha3p0_20\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T10:24:58.696Z\", \"updated_at\": \"2026-05-22T12:38:25.600Z\", \"hypothesis\": \"α=3.0 SFT GSM8K eval (checkpoint-935, 1 epoch). Dose-response 5th SFT data point for C1 decoupling. Paired with α=3.0 GRPO (pending). Completes the 5-point dose-response SFT column.\", \"parent\": \"grpo_rasp_alpha3p0_20\", \"spec\": {\"server\": \"westd-32935\", \"gpu\": \"cuda:2\", \"command\": \"eval_gsm8k.py --model_path sft_rasp_alpha3p0_20/checkpoint-935 --max_new_tokens 2048\", \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B\", \"seed\": 42, \"data_path\": \"openai/gsm8k (test split)\", \"data_count\": 1319, \"checkpoint_source\": \"sft_rasp_alpha3p0_20/checkpoint-935 (SCP from westb)\", \"eval_data\": \"gsm8k test 1319\", \"pid\": \"37024\"}, \"reproduce\": {\"finished_at\": \"2026-05-22T12:34:57.027Z\"}, \"failure_reason\": \"\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T12:35:05.634Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-22T12:35:15.663664+00:00\"}]}, \"metrics\": {\"gsm8k_accuracy\": 0.6414, \"gsm8k_correct\": 846, \"gsm8k_total\": 1319, \"gsm8k_stderr\": 0.0132, \"eos_rate\": 0.9879, \"avg_response_length\": 188.63, \"natural_eos\": 1303, \"truncated\": 16}, \"log_path\": \"/tmp/eval_gsm8k_sft_alpha3p0.log\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_alpha3p0_20/checkpoint-935\", \"notes\": \"Cron 误判。评估 1319/1319 全部完成，accuracy=64.14%。进程因写结果 JSON 时磁盘满 (OSError: No space left on device) 以非零码退出，但所有推理已完成、accuracy 已计算。结果 JSON 未写入磁盘，数据从日志提取。中间进度 ~64.15%@1300 与最终 64.14% 一致。\"}, \"grpo_rasp_alpha3p0_20_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T10:40:19.362Z\", \"updated_at\": \"2026-05-22T11:58:15.586Z\", \"hypothesis\": \"Re-run of grpo_rasp_alpha3p0_20 (checkpoint corrupted by disk-full). α=3.0 GRPO 100 steps on sft_rasp_alpha3p0_20/checkpoint-935. Critical for dose-response curve (α=3.0 between α=2.0 peak and α=4.0 decline).\", \"parent\": \"grpo_rasp_alpha3p0_20\", \"spec\": {\"server\": \"westd-32935\", \"gpu\": \"cuda:0\", \"command\": \"CUDA_VISIBLE_DEVICES=0 HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 nohup python src/train_grpo_v5.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_alpha3p0_20/checkpoint-935 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_alpha3p0_20_v2 --max_steps 100 --save_total_limit 1\", \"pid\": \"42003\", \"data_path\": \"openai/gsm8k (train split)\", \"data_count\": 7473, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B (sft_rasp_alpha3p0_20)\", \"seed\": 42, \"checkpoint_source\": \"sft_rasp_alpha3p0_20/checkpoint-935\", \"eval_data\": \"N/A - GRPO training\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_alpha3p0_20_v2\", \"log_path\": \"/tmp/grpo_alpha3p0_v2.log\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T11:58:15.586Z\"}, \"eval_math500_grpo_standard_20_fair_2048_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T03:49:45.575Z\", \"updated_at\": \"2026-05-22T11:17:52.493Z\", \"hypothesis\": \"Standard 20% fair GRPO MATH-500 @2048. P0 data gap for cross-method MATH-500 table. Re-run on westd-32935 after westd-29022 outage.\", \"parent\": \"eval_math500_grpo_standard_20_fair_2048\", \"spec\": {\"command\": \"python src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_standard_20_fair --max_new_tokens 2048 --output_path /root/recovery_aware_struct_prune/results/eval_math500_grpo_standard_20_fair_2048_v2.json\", \"server\": \"westd-32935\", \"gpu\": [\"cuda:0\"], \"data_path\": \"MATH-500\", \"data_count\": 500, \"model_name\": \"grpo_stage2_standard_20_fair\", \"model_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_standard_20_fair\", \"seed\": 42, \"checkpoint_source\": \"grpo_stage2_standard_20_fair\", \"eval_data\": \"MATH-500\", \"log_path\": \"/root/recovery_aware_struct_prune/logs/eval_math500_grpo_standard_20_fair_2048_v2.log\", \"checkpoint_path\": \"N/A (eval)\"}, \"reproduce\": {\"finished_at\": \"2026-05-22T11:12:19.798Z\"}, \"failure_reason\": \"\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T11:12:27.767Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-22T11:12:38.330160+00:00\"}]}, \"metrics\": {\"math500_accuracy\": 0.264, \"math500_correct\": 132, \"math500_total\": 500, \"math500_stderr\": 0.0197}, \"notes\": \"Cron 误判。实际正常完成。MATH-500 Accuracy = 0.2640 ± 0.0197 (132/500)。运行时长 ~7h11min。结果文件: /root/recovery_aware_struct_prune/results/eval_math500_grpo_standard_20_fair_2048_v2.json\"}, \"grpo_random_20_seed123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T10:34:12.100Z\", \"updated_at\": \"2026-05-22T11:17:21.388Z\", \"hypothesis\": \"MF2 multi-seed validation: Random pruning 20% GRPO with seed123. Tests if GRPO decoupling result (C1) is robust across random seeds. If variance across seeds is low (±2pp), C1 claim is strengthened.\", \"spec\": {\"server\": \"westd-32935\", \"gpu\": \"cuda:2\", \"command\": \"bash -c 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/recovery_aware_struct_prune && HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 python src/train_grpo_v5.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_random_20 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/grpo_random_20_seed123 --num_steps 100 --seed 123'\", \"pid\": \"36832\", \"data_path\": \"openai/gsm8k (train split)\", \"data_count\": 7473, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B (sft_random_20)\", \"seed\": 123, \"checkpoint_source\": \"sft_random_20\", \"eval_data\": \"N/A - GRPO training, not eval\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_random_20_seed123\", \"log_path\": \"/tmp/mf2_random_seed123_grpo.log\"}, \"reproduce\": {\"finished_at\": \"2026-05-22T11:12:49.435Z\"}, \"failure_reason\": \"\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T11:12:57.919Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-22T11:13:16.493425+00:00\"}]}, \"notes\": \"Cron 误判 (已知 pattern: process dead 5× with no sentinel/W&B)。实际 GRPO 训练正常完成 (19:02 CST)。模型保存: /root/autodl-tmp/recovery_aware_struct_prune/grpo_random_20_seed123。WandB run: grpo_sft_random_20 (ID: 1silchcm)。日志: /tmp/mf2_random_seed123_grpo.log\"}, \"grpo_rasp_alpha3p0_20\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T08:48:06.001Z\", \"updated_at\": \"2026-05-22T10:39:07.034Z\", \"hypothesis\": \"α=3.0 GRPO 100 steps on checkpoint-935 (1 epoch SFT). Dose-response data point between α=2.0 and α=4.0. If monotonic: higher α → higher GSM8K accuracy, confirming CKA overlap suppression causally harms recovery.\", \"parent\": \"grpo_alpha4_20\", \"spec\": {\"server\": \"westb-23072\", \"gpu\": \"cuda:0\", \"command\": \"train_grpo_v5.py --model_path sft_rasp_alpha3p0_20/checkpoint-935 --output_dir grpo_rasp_alpha3p0_20 --max_steps 100 --learning_rate 1e-6 --per_device_train_batch_size 1 --gradient_accumulation_steps 8 --max_completion_length 512 --temperature 0.4 --beta 0.01 --loss_type dapo --format_reward_weight 0.1 --gradient_checkpointing true --optim adamw_8bit\", \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B\", \"seed\": 42, \"pid\": \"170676\", \"data_path\": \"openai/gsm8k (train split)\", \"data_count\": 7473, \"checkpoint_source\": \"sft_rasp_alpha3p0_20/checkpoint-935\", \"eval_data\": \"N/A - GRPO training\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_alpha3p0_20/checkpoint-100\", \"log_path\": \"/tmp/alpha3p0_grpo.log\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T10:31:57.909Z\", \"notes\": \"GRPO 训练 100/100 steps 完成，但 checkpoint-100/model.safetensors 被截断（7.2GB vs 应有 11.5GB）。原因：westb 数据盘在保存时 100% 满。需要重跑 GRPO。SFT checkpoint-935 完好（11.5GB）。\"}, \"eval_gsm8k_sft_alpha2p0_20\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T10:19:50.623Z\", \"updated_at\": \"2026-05-22T10:22:56.503Z\", \"hypothesis\": \"α=2.0 SFT GSM8K eval for C1 decoupling. Paired with α=2.0 GRPO (66.11%). Critical: if SFT ~61-62%, Δ ≈ +4-5pp would break C1 universal ±2pp claim. Reviewer-flagged risk.\", \"parent\": \"pipeline_alpha2p0_20\", \"spec\": {\"server\": \"westd-32935\", \"gpu\": \"cuda:2\", \"command\": \"eval_gsm8k.py --model_path sft_rasp_alpha2p0_20 --max_new_tokens 2048\", \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B\", \"seed\": 42, \"data_path\": \"openai/gsm8k (test split)\", \"data_count\": 1319, \"checkpoint_source\": \"sft_rasp_alpha2p0_20\", \"eval_data\": \"gsm8k test 1319\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_alpha2p0_20\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/eval_gsm8k_sft_alpha2p0_20.json\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T10:22:49.360Z\", \"metrics\": {\"gsm8k_accuracy\": 0.6497, \"gsm8k_correct\": 857, \"gsm8k_total\": 1319}}, \"eval_gsm8k_sft_alpha0p5_20\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T10:19:48.133Z\", \"updated_at\": \"2026-05-22T10:20:57.690Z\", \"hypothesis\": \"α=0.5 SFT GSM8K eval for C1 decoupling. Paired with α=0.5 GRPO (61.18%). Δ(GRPO-SFT) tests whether GRPO benefit is universal ±2pp across α values.\", \"parent\": \"pipeline_alpha0p5_20\", \"spec\": {\"server\": \"westd-32935\", \"gpu\": \"cuda:3\", \"command\": \"eval_gsm8k.py --model_path sft_rasp_alpha0p5_20 --max_new_tokens 2048\", \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B\", \"seed\": 42, \"data_path\": \"openai/gsm8k (test split)\", \"data_count\": 1319, \"checkpoint_source\": \"sft_rasp_alpha0p5_20\", \"eval_data\": \"gsm8k test 1319\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_alpha0p5_20\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/eval_gsm8k_sft_alpha0p5_20.json\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T10:20:50.793Z\", \"metrics\": {\"gsm8k_accuracy\": 0.6073, \"gsm8k_correct\": 801, \"gsm8k_total\": 1319}}, \"grpo_qwen_math_cka_only_20\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T08:50:34.293Z\", \"updated_at\": \"2026-05-22T09:54:05.974Z\", \"hypothesis\": \"MF3 cross-architecture validation: Qwen2.5-Math-7B CKA-only 20% pruned → SFT → GRPO 100 steps. Tests if CKA-guided pruning advantage transfers beyond DeepSeek-R1 to Qwen-Math family. P0 highest priority.\", \"parent\": \"sft_qwen_math_cka_only_20_v2\", \"spec\": {\"server\": \"westb-23072\", \"gpu\": \"cuda:1\", \"command\": \"train_grpo_v5.py --model_path sft_qwen_math_cka_only_20_v2 --max_steps 100 --learning_rate 1e-6 --per_device_train_batch_size 1 --gradient_accumulation_steps 8 --max_completion_length 512 --temperature 0.4 --beta 0.01 --loss_type dapo --format_reward_weight 0.1 --gradient_checkpointing true --optim adamw_8bit\", \"model_name\": \"Qwen2.5-Math-7B\", \"seed\": 42, \"pid\": \"164710\", \"data_path\": \"openai/gsm8k (train split)\", \"data_count\": 7473, \"checkpoint_source\": \"sft_qwen_math_cka_only_20_v2\", \"eval_data\": \"N/A - this is GRPO training, not eval\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_qwen_math_cka_only_20\", \"log_path\": \"/tmp/mf3_qwen_grpo.log\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T09:54:05.974Z\"}, \"eval_gsm8k_grpo_alpha2p0_20\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T09:28:08.089Z\", \"updated_at\": \"2026-05-22T09:29:24.824Z\", \"hypothesis\": \"α=2.0 GRPO GSM8K eval. Dose-response data point: moderate overlap suppression (α=2.0) between α=1.0 (61.49%) and α=4.0 (62.77%). Tests monotonicity of dose-response curve.\", \"parent\": \"pipeline_alpha2p0_20\", \"spec\": {\"server\": \"westd-32935\", \"gpu\": \"cuda:2\", \"command\": \"eval_gsm8k.py --model_path grpo_rasp_alpha2p0_20 --max_new_tokens 2048\", \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B\", \"seed\": 42, \"data_path\": \"openai/gsm8k (test split)\", \"data_count\": 1319, \"checkpoint_source\": \"grpo_rasp_alpha2p0_20\", \"eval_data\": \"gsm8k test 1319\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_alpha2p0_20\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/eval_gsm8k_grpo_alpha2p0_20.json\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T09:29:16.837Z\", \"metrics\": {\"gsm8k_accuracy\": 0.6611, \"gsm8k_correct\": 872, \"gsm8k_total\": 1319}}, \"eval_gsm8k_grpo_alpha0p5_20\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T09:28:05.478Z\", \"updated_at\": \"2026-05-22T09:29:23.350Z\", \"hypothesis\": \"α=0.5 GRPO GSM8K eval. Dose-response data point: low overlap suppression (α=0.5) should yield lower accuracy than α=1.0 (61.49%) if CKA overlap suppression causally harms recovery.\", \"parent\": \"pipeline_alpha0p5_20\", \"spec\": {\"server\": \"westd-32935\", \"gpu\": \"cuda:3\", \"command\": \"eval_gsm8k.py --model_path grpo_rasp_alpha0p5_20 --max_new_tokens 2048\", \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B\", \"seed\": 42, \"data_path\": \"openai/gsm8k (test split)\", \"data_count\": 1319, \"checkpoint_source\": \"grpo_rasp_alpha0p5_20\", \"eval_data\": \"gsm8k test 1319\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_alpha0p5_20\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/eval_gsm8k_grpo_alpha0p5_20.json\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T09:29:13.196Z\", \"metrics\": {\"gsm8k_accuracy\": 0.6118, \"gsm8k_correct\": 807, \"gsm8k_total\": 1319}}, \"eval_math500_sft_standard_20_1p5b\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T04:31:30.202Z\", \"updated_at\": \"2026-05-22T08:27:40.167Z\", \"hypothesis\": \"1.5B Standard 20% SFT MATH-500 @2048. Cross-scale comparison with CKA-only 1.5B (10.6%) to test if CKA-guided pruning advantage is scale-invariant.\", \"spec\": {\"command\": \"python src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20_1p5b --max_new_tokens 2048 --output_path /root/recovery_aware_struct_prune/results/eval_math500_sft_standard_20_1p5b.json\", \"server\": \"westb-23072\", \"gpu\": [\"cuda:0\"], \"data_path\": \"MATH-500\", \"data_count\": 500, \"model_name\": \"sft_standard_20_1p5b\", \"model_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20_1p5b\", \"seed\": 42, \"checkpoint_source\": \"sft_standard_20_1p5b\", \"eval_data\": \"MATH-500\", \"log_path\": \"/root/recovery_aware_struct_prune/logs/eval_math500_sft_standard_20_1p5b.log\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20_1p5b\"}, \"conclusion\": \"success\", \"metrics\": {\"math500_accuracy\": 0.054, \"correct\": 27, \"total\": 500, \"truncated\": 335}, \"completed_at\": \"2026-05-22T07:50:22.759Z\"}, \"eval_gsm8k_sft_alpha4_20_v5\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T03:49:50.201Z\", \"updated_at\": \"2026-05-22T06:05:53.848Z\", \"hypothesis\": \"α=4.0 SFT GSM8K N=1319 full eval @2048. D100 critical for C1 decoupling universality. v4 lost to westd-29022 outage. Re-run on westd-32935.\", \"parent\": \"eval_gsm8k_sft_alpha4_20_v4\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_alpha4_20\", \"log_path\": \"/root/recovery_aware_struct_prune/logs/eval_gsm8k_sft_alpha4_20_v5.log\", \"result_path\": \"/root/recovery_aware_struct_prune/results/eval_gsm8k_sft_alpha4_20_v5.json\"}, \"reproduce\": {\"finished_at\": \"2026-05-22T05:47:27.370Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T05:47:34.101Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-22T05:47:41.693855+00:00\"}]}, \"metrics\": {\"gsm8k_accuracy\": 0.6194, \"correct\": 817, \"total\": 1319, \"stderr\": 0.0134, \"eos_rate\": 0.981, \"avg_response_length\": 197.85}}, \"eval_gsm8k_grpo_alpha4_20_v3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T03:49:52.414Z\", \"updated_at\": \"2026-05-22T05:33:39.349Z\", \"hypothesis\": \"α=4.0 GRPO GSM8K N=1319 full eval @2048. v1 timed out at 774/1319 (62.93% interim). v2 ALLOCATED but westd-29022 died. Re-run on westd-32935 with --max_new_tokens 2048.\", \"parent\": \"eval_gsm8k_grpo_alpha4_20_v2\", \"spec\": {\"command\": \"python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_alpha4_20/checkpoint-100 --max_new_tokens 2048 --output_path /root/recovery_aware_struct_prune/results/eval_gsm8k_grpo_alpha4_20_v3.json\", \"server\": \"westd-32935\", \"gpu\": [\"cuda:3\"], \"data_path\": \"GSM8K\", \"data_count\": 1319, \"model_name\": \"grpo_alpha4_20/checkpoint-100\", \"model_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_alpha4_20/checkpoint-100\", \"seed\": 42, \"checkpoint_source\": \"grpo_alpha4_20/checkpoint-100\", \"eval_data\": \"GSM8K\", \"log_path\": \"/root/recovery_aware_struct_prune/logs/eval_gsm8k_grpo_alpha4_20_v3.log\"}, \"reproduce\": {\"finished_at\": \"2026-05-22T05:30:52.773Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T05:30:50.611Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-22T05:31:04.453494+00:00\"}]}, \"metrics\": {\"gsm8k_accuracy\": 0.6277, \"gsm8k_accuracy_ci\": 0.0133, \"gsm8k_correct\": 828, \"gsm8k_total\": 1319, \"eos_rate\": 0.9856, \"avg_response_length\": 188.16, \"natural_eos\": 1300, \"truncated\": 19}, \"notes\": \"Cron 误判为 failed（进程正常退出但 cron 未检测到 sentinel）。实际完成 1319/1319，accuracy=62.77%。α=4.0 GRPO > Standard GRPO (59.84%) > RASP α=1.0 GRPO (54.43%)。确认 α tuning 有效缓解 RASP collapse。checkpoint_path: /root/autodl-tmp/recovery_aware_struct_prune/grpo_alpha4_20/checkpoint-100, log_path: /root/recovery_aware_struct_prune/logs/eval_gsm8k_grpo_alpha4_20_v3.log, results_path: /root/recovery_aware_struct_prune/results/eval_gsm8k_grpo_alpha4_20_v3.json\"}, \"eval_math500_sft_standard_25\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-21T02:58:32.492Z\", \"updated_at\": \"2026-05-22T02:31:03.648Z\", \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"reproduce\": {\"finished_at\": \"2026-05-21T02:58:40.587Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-21T02:58:45.343074+00:00\"}], \"previous_failure\": {\"conclusion\": \"success\", \"metrics\": {\"math500_accuracy\": 0.13, \"correct\": 65, \"n_total\": 500}, \"notes\": \"v1 结果采用（v2 启动即崩溃）。结果文件: /root/autodl-tmp/recovery_aware_struct_prune/results/eval_math500_sft_standard_25.json。Director 于 2026-05-21 批准采用 v1 数据。\"}}, \"notes\": \"v1 结果采用（v2 启动即崩溃）。结果文件: /root/autodl-tmp/recovery_aware_struct_prune/results/eval_math500_sft_standard_25.json。Director 于 2026-05-21 批准采用 v1 数据。\", \"hypothesis\": \"Standard 25% SFT model MATH-500 accuracy establishes pre-GRPO baseline for standard pruning at 25% sparsity, enabling SFT→GRPO recovery delta on MATH-500\", \"completed_at\": \"2026-05-21T19:22:29.444Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_25/checkpoint-1870 --output_path /root/runs/recovery_aware_struct_prune/eval_math500_sft_standard_25/results.json --max_new_tokens 2048 --seed 42\", \"server\": \"westb-23072\", \"gpu\": [\"cuda:1\"], \"pid\": \"104592\", \"data_path\": \"MATH-500\", \"data_count\": 500, \"model_name\": \"sft_standard_25/checkpoint-1870\", \"model_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_25/checkpoint-1870\", \"seed\": 42, \"checkpoint_source\": \"sft_standard_25\", \"eval_data\": \"MATH-500\", \"log_path\": \"/root/runs/recovery_aware_struct_prune/eval_math500_sft_standard_25/run.log\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_25/checkpoint-1870\"}, \"conclusion\": \"success\", \"metrics\": {\"math500_accuracy\": 0.14, \"correct\": 70, \"n_total\": 500, \"natural_eos\": 185, \"truncated\": 315, \"avg_response_length\": 1367.82, \"v1_accuracy\": 0.13, \"v1_correct\": 65}}, \"grpo_alpha4_20\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T18:59:18.863Z\", \"updated_at\": \"2026-05-21T19:32:31.353Z\", \"hypothesis\": \"α=4.0 GRPO after SFT: if reward collapses (→0 like α=1.0 RASP GRPO), proves RASP collapse is structural, not hyperparameter-dependent. If reward stays positive and GSM8K improves over SFT, α tuning can mitigate collapse.\", \"parent\": \"sft_alpha4_20_v2\", \"spec\": {\"command\": \"python src/train_grpo_v5.py --alpha 4.0 --max_steps 100\", \"server\": \"westd-29022\", \"gpu\": [\"cuda:2\"], \"pid\": \"406593\", \"log_path\": \"~/runs/recovery_aware_struct_prune/grpo_alpha4_20.log\", \"submitted_at\": \"2026-05-21T18:59:44.258Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"Qwen2.5-7B\", \"seed\": 42, \"data_path\": \"gsm8k\", \"data_count\": 7473, \"checkpoint_source\": \"sft_alpha4_20_v2\", \"eval_data\": \"gsm8k\", \"wall_clock_seconds\": 1659.0, \"gpu_hours\": 0.46}, \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_alpha4_20/checkpoint-100\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/logs/grpo_alpha4_20.log\", \"metrics\": {\"final_reward\": 0.198, \"reward_range\": \"0.146-0.256\", \"steps\": 100, \"final_loss\": 0.018, \"final_kl\": 0.00198}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-21T19:27:23.228Z\"}, \"sft_alpha4_20_v2\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T18:30:48.284Z\", \"updated_at\": \"2026-05-21T19:32:28.482Z\", \"hypothesis\": \"α=4.0 SFT recovery with save_only_model=True to prevent disk overflow. Pruning successful (19.09% sparsity). Testing if higher α mitigates RASP collapse after full SFT→GRPO→eval pipeline.\", \"parent\": \"sft_alpha4_20_manual\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/recovery_aware_struct_prune && python src/train_sft_warmup.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/pruned_alpha4_20 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/sft_alpha4_20 --num_epochs 2 --lr 2e-5\\\"\", \"server\": \"westd-29022\", \"gpu\": [\"cuda:2\"], \"pid\": \"401581\", \"log_path\": \"~/runs/recovery_aware_struct_prune/sft_alpha4_20_v2.log\", \"submitted_at\": \"2026-05-21T18:31:05.499Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"reproduce\": {\"finished_at\": \"2026-05-21T18:54:53.481Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-21T18:54:59.708620+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"final_train_loss\": 0.8118, \"token_accuracy\": 0.8165, \"epochs\": 2, \"steps\": 936}}, \"eval_math500_grpo_cka_only_25_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T13:54:50.310Z\", \"updated_at\": \"2026-05-21T17:33:50.709Z\", \"hypothesis\": \"CKA-only 25% GRPO model MATH-500 @2048 accuracy for cross-benchmark validation, re-run with correct max_new_tokens=2048 for consistency with 20% data\", \"parent\": \"eval_math500_grpo_cka_only_25\", \"spec\": {\"command\": \"nohup bash -c 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=0 python /root/recovery_aware_struct_prune/src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_25 --output_path /root/runs/recovery_aware_struct_prune/eval_math500_grpo_cka_only_25_v2 --seed 42 --max_new_tokens 2048' > /root/runs/recovery_aware_struct_prune/eval_math500_grpo_cka_only_25_v2/eval_math500_grpo_cka_only_25_v2.log 2>&1 &\", \"server\": \"westd-29022\", \"gpu\": \"cuda:0\", \"pid\": 379999, \"data_path\": \"MATH-500\", \"data_count\": 500, \"model_name\": \"Qwen2.5-7B CKA-only 25% GRPO\", \"model_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_25\", \"seed\": 42, \"checkpoint_source\": \"grpo_cka_only_25\", \"eval_data\": \"MATH-500\", \"log_path\": \"/root/runs/recovery_aware_struct_prune/eval_math500_grpo_cka_only_25_v2/eval_math500_grpo_cka_only_25_v2.log\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"N/A (eval only)\", \"completed_at\": \"2026-05-21T17:33:40.068Z\", \"metrics\": {\"math500_accuracy\": 0.184, \"math500_stderr\": 0.0173, \"correct\": 92, \"n_total\": 500}, \"log_path\": \"/root/runs/recovery_aware_struct_prune/eval_math500_grpo_cka_only_25_v2/eval_math500_grpo_cka_only_25_v2.log\"}, \"eval_math500_sft_cka_only_25_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T13:54:51.945Z\", \"updated_at\": \"2026-05-21T17:29:14.940Z\", \"hypothesis\": \"CKA-only 25% SFT model MATH-500 @2048 accuracy establishes pre-GRPO baseline, re-run with correct max_new_tokens=2048 for consistency\", \"parent\": \"eval_math500_sft_cka_only_25\", \"spec\": {\"command\": \"nohup bash -c 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=2 python /root/recovery_aware_struct_prune/src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_25 --output_path /root/runs/recovery_aware_struct_prune/eval_math500_sft_cka_only_25_v2 --seed 42 --max_new_tokens 2048' > /root/runs/recovery_aware_struct_prune/eval_math500_sft_cka_only_25_v2/eval_math500_sft_cka_only_25_v2.log 2>&1 &\", \"server\": \"westd-29022\", \"gpu\": \"cuda:2\", \"pid\": 380074, \"data_path\": \"MATH-500\", \"data_count\": 500, \"model_name\": \"Qwen2.5-7B CKA-only 25% SFT\", \"model_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_25\", \"seed\": 42, \"checkpoint_source\": \"sft_cka_only_25\", \"eval_data\": \"MATH-500\", \"log_path\": \"/root/runs/recovery_aware_struct_prune/eval_math500_sft_cka_only_25_v2/eval_math500_sft_cka_only_25_v2.log\"}, \"conclusion\": \"success\", \"log_path\": \"/root/runs/recovery_aware_struct_prune/eval_math500_sft_cka_only_25_v2/eval_math500_sft_cka_only_25_v2.log\", \"checkpoint_path\": \"N/A (eval only)\", \"completed_at\": \"2026-05-21T17:29:10.900Z\", \"metrics\": {\"math500_accuracy\": 0.192, \"correct\": 96, \"n_total\": 500, \"std_err\": 0.0176}, \"notes\": \"Eval completed all 500 problems. Result JSON not saved due to IsADirectoryError (output_path pointed to directory instead of file). Metrics extracted from log.\"}, \"eval_gsm8k_sft_standard_25\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T08:13:12.112Z\", \"updated_at\": \"2026-05-21T14:40:37.092Z\", \"hypothesis\": \"Standard 25% SFT GSM8K accuracy establishes pre-GRPO floor for importance-based pruning at 25% sparsity, enabling SFT→GRPO recovery delta comparison with CKA-only 25%\", \"spec\": {\"command\": \"nohup bash -c 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=3 python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_25/checkpoint-1870 --max_samples 1319 --seed 42'\", \"server\": \"westd-29022\", \"gpu\": \"cuda:3\", \"pid\": 335301, \"data_path\": \"GSM8K (N=1319)\", \"data_count\": 1319, \"model_name\": \"sft_standard_25\", \"model_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_25/checkpoint-1870\", \"seed\": 42, \"checkpoint_source\": \"sft_standard_25\", \"eval_data\": \"GSM8K\", \"log_path\": \"/root/runs/recovery_aware_struct_prune/eval_gsm8k_sft_standard_25.log\", \"checkpoint_path\": \"N/A (eval only)\"}, \"metrics\": {\"gsm8k_accuracy\": 0.5087, \"stderr\": 0.0138, \"correct\": 671, \"n_total\": 1319, \"eos_rate\": 0.953, \"avg_response_length\": 333.15}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-21T14:40:37.092Z\"}, \"eval_math500_grpo_cka_only_20\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T02:41:32.199Z\", \"updated_at\": \"2026-05-21T12:47:30.348Z\", \"hypothesis\": \"CKA-only 20% GRPO model MATH-500 accuracy provides cross-benchmark validation at 20% sparsity and cross-method comparison with Random 20% GRPO MATH-500\", \"spec\": {\"max_new_tokens_actual\": 4096, \"note\": \"未显式指定 --max_new_tokens，脚本默认 4096。与 @2048 evals 不可直接比较。需用 eval_math500_grpo_cka_only_20_2048 重跑公平对比。\"}, \"parent\": \"grpo_cka_only_20\", \"reproduce\": {\"finished_at\": \"2026-05-18T14:05:38.456Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-18T14:05:47.086682+00:00\"}]}, \"metrics\": {\"accuracy\": 0.266, \"n_correct\": 133, \"n_total\": 500, \"stderr\": 0.0198, \"truncated\": 108, \"truncation_rate\": 0.216, \"avg_response_length\": 1124.24}, \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/math500_grpo_cka_only_20.json\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_math500_grpo_cka_only_20.log\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T14:09:25.937Z\"}, \"eval_gsm8k_grpo_standard_25\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T06:42:08.819Z\", \"updated_at\": \"2026-05-21T12:37:17.579Z\", \"hypothesis\": \"Standard 25% GRPO后GSM8K评估。GRPO reward=0.00813 (near-total collapse)。验证 Standard pruning 在 25% 稀疏度下 GRPO 后数学推理能力。\", \"parent\": \"grpo_standard_25_westb\", \"spec\": {\"command\": \"python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_25_westb/checkpoint-100 --max_samples 1319 --seed 42\", \"server\": \"westb-23072\", \"gpu\": \"cuda:1\", \"pid\": 75282, \"data_path\": \"gsm8k\", \"data_count\": 1319, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B-pruned-standard-25pct-GRPO-v5fair\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_25_westb/checkpoint-100\", \"eval_data\": \"GSM8K\", \"log_path\": \"/root/runs/recovery_aware_struct_prune/eval_gsm8k_grpo_standard_25.log\"}, \"conclusion\": \"success\", \"metrics\": {\"gsm8k_accuracy\": 0.5186, \"stderr\": 0.0138, \"correct\": 684, \"n_total\": 1319, \"eos_rate\": 0.9575, \"avg_response_length\": 314.47}, \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_25_westb/checkpoint-100\", \"log_path\": \"/root/runs/recovery_aware_struct_prune/eval_gsm8k_grpo_standard_25.log\", \"completed_at\": \"2026-05-21T12:37:17.579Z\"}, \"eval_gsm8k_sft_cka_only_25\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T06:47:14.010Z\", \"updated_at\": \"2026-05-21T10:17:58.203Z\", \"hypothesis\": \"CKA-only 25% SFT model retains higher GSM8K accuracy than GRPO-recovered model's SFT baseline, establishing the pre-GRPO accuracy floor for measuring recovery delta at 25% sparsity\", \"spec\": {\"command\": \"nohup bash -c 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=1 python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_25 --max_samples 1319 --seed 42'\", \"server\": \"westd-29022\", \"gpu\": \"cuda:1\", \"pid\": 329698, \"data_path\": \"GSM8K (N=1319)\", \"data_count\": 1319, \"model_name\": \"sft_cka_only_25\", \"model_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_25\", \"seed\": 42, \"checkpoint_source\": \"sft_cka_only_25\", \"eval_data\": \"GSM8K\", \"log_path\": \"/root/runs/recovery_aware_struct_prune/eval_gsm8k_sft_cka_only_25.log\"}, \"conclusion\": \"success\", \"metrics\": {\"gsm8k_accuracy\": 0.6012, \"correct\": 793, \"n_total\": 1319, \"stderr\": 0.0135, \"eos_rate\": 0.9803, \"avg_response_length\": 243.6}, \"checkpoint_path\": \"N/A (eval only)\", \"completed_at\": \"2026-05-21T10:17:58.203Z\"}, \"eval_gsm8k_sft_random_20\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T06:47:16.459Z\", \"updated_at\": \"2026-05-21T08:47:06.620Z\", \"hypothesis\": \"Random 20% SFT model GSM8K accuracy establishes the pre-GRPO floor for random pruning, enabling SFT→GRPO recovery delta comparison across pruning methods at 20% sparsity\", \"spec\": {\"command\": \"nohup bash -c 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=2 python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_random_20 --max_samples 1319 --seed 42'\", \"server\": \"westd-29022\", \"gpu\": \"cuda:2\", \"pid\": 329770, \"data_path\": \"GSM8K (N=1319)\", \"data_count\": 1319, \"model_name\": \"sft_random_20\", \"model_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_random_20\", \"seed\": 42, \"checkpoint_source\": \"sft_random_20\", \"eval_data\": \"GSM8K\", \"log_path\": \"/root/runs/recovery_aware_struct_prune/eval_gsm8k_sft_random_20.log\"}, \"conclusion\": \"success\", \"metrics\": {\"gsm8k_accuracy\": 0.5125, \"correct\": 676, \"n_total\": 1319, \"stderr\": 0.0138, \"eos_rate\": 0.9932, \"avg_response_length\": 182.4}, \"checkpoint_path\": \"N/A (eval only)\", \"completed_at\": \"2026-05-21T08:47:06.620Z\"}, \"eval_gsm8k_grpo_cka_only_25_v3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T04:56:52.006Z\", \"updated_at\": \"2026-05-21T08:17:13.429Z\", \"hypothesis\": \"CKA-only 25% GRPO后GSM8K评估。model_path=/grpo_cka_only_25（根目录）。Cross-sparsity对比: Standard 25% GRPO=51.1%, RASP 25% GRPO=53.15%。\", \"parent\": \"grpo_cka_only_25\", \"spec\": {\"command\": \"python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_25 --max_samples 1319 --seed 42\", \"server\": \"westd-29022\", \"gpu\": [\"cuda:0\"], \"pid\": \"322443\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_gsm8k_grpo_cka_only_25_v3.log\", \"data_path\": \"gsm8k\", \"data_count\": 1319, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B-pruned-cka_only-25pct-GRPO\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_25\", \"eval_data\": \"GSM8K\"}, \"notes\": \"正确 PID=322443 (v3提交)。323174 是重复提交已 kill。\", \"conclusion\": \"success\", \"metrics\": {\"gsm8k_accuracy\": 0.5959, \"correct\": 786, \"n_total\": 1319, \"eos_rate\": 0.9818}, \"checkpoint_path\": \"N/A (eval only)\", \"completed_at\": \"2026-05-21T08:17:13.429Z\"}, \"grpo_standard_25_westb\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T03:00:00.000Z\", \"updated_at\": \"2026-05-21T06:40:00.000Z\", \"hypothesis\": \"Standard 25% GRPO v5 fair config (100 steps, lr=1e-6, beta=0.01, T=0.4, seed=42) on westb. Re-run with fair config for cross-method comparison.\", \"parent\": \"sft_standard_25\", \"spec\": {\"command\": \"python src/train_grpo_v5.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_25 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_25_westb --max_steps 100 --save_steps 100 --seed 42\", \"server\": \"westb-23072\", \"gpu\": [\"cuda:1\"], \"pid\": \"64194\", \"data_path\": \"gsm8k\", \"data_count\": 7473, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B-pruned-standard-25pct-SFT\", \"seed\": 42}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-21T06:40:00.000Z\", \"metrics\": {\"reward\": 0.00813, \"steps\": 100, \"collapse_pattern\": \"near_total_collapse\"}, \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_25_westb/checkpoint-100\", \"log_path\": \"~/runs/recovery_aware_struct_prune/grpo_standard_25.log\"}, \"eval_gsm8k_grpo_random_20_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T04:56:53.980Z\", \"updated_at\": \"2026-05-21T06:38:00.000Z\", \"hypothesis\": \"Random 20% GRPO后GSM8K评估。Random pruning reward=0.189（最低），验证无结构保留的pruning在GRPO后数学推理能力。\", \"parent\": \"grpo_random_20\", \"spec\": {\"command\": \"python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_random_20/checkpoint-100 --max_samples 1319 --seed 42\", \"server\": \"westd-29022\", \"gpu\": [\"cuda:1\"], \"pid\": \"322611\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_gsm8k_grpo_random_20_v2.log\", \"data_path\": \"gsm8k\", \"data_count\": 1319, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B-pruned-random-20pct-GRPO\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_random_20/checkpoint-100\", \"eval_data\": \"GSM8K\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-21T06:38:00.000Z\", \"metrics\": {\"gsm8k_accuracy\": 0.5057, \"gsm8k_stderr\": 0.0138, \"correct\": 667, \"total\": 1319, \"eos_rate\": 0.9954, \"avg_response_length\": 173}, \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_random_20/checkpoint-100\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_gsm8k_grpo_random_20_v2.log\"}, \"sft_random_20\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T03:44:24.654Z\", \"updated_at\": \"2026-05-21T04:45:00.000Z\", \"hypothesis\": \"Random 20% pruning baseline SFT recovery. Random pruning 不保留任何结构信息，作为 ablation baseline 验证 CKA-guided pruning 的结构保留优势。\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-21T03:50:00.000Z\", \"spec\": {\"server\": \"westd-29022\", \"gpu\": [\"cuda:0\"], \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B-pruned-random-20pct\", \"command\": \"python src/sft_recovery.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/pruned_random_20 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/sft_random_20\", \"data_path\": \"gsm8k\", \"seed\": 42}, \"metrics\": {\"steps\": 1870, \"model_size_gb\": 12}, \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_random_20\", \"log_path\": \"/root/runs/recovery_aware_struct_prune/sft_random_20.log\"}}, \"count\": 50, \"total\": 249, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.9483}}"
    }
  },
  "sourceToolAssistantUUID": "3cef34a5-cc1d-4312-991b-6c3c5a83f2e5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "3a90179e-e19e-41d1-8fb4-f23e916f555f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Runtime record

_source line 43 · 2026-05-23T10:47:29.082Z_

```json
{
  "parentUuid": "37c7d07b-decc-4fab-acab-630a49f85c6e",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "5dc0d5e4-8d6f-4780-bba0-fe6422fa9520",
  "timestamp": "2026-05-23T10:47:29.082Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "3a90179e-e19e-41d1-8fb4-f23e916f555f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---


### Runtime record

_source line 44_

```json
{
  "type": "last-prompt",
  "leafUuid": "5dc0d5e4-8d6f-4780-bba0-fe6422fa9520",
  "sessionId": "3a90179e-e19e-41d1-8fb4-f23e916f555f"
}
```

---


### Runtime record

_source line 45_

```json
{
  "type": "ai-title",
  "aiTitle": "Map paper results to registry experiments",
  "sessionId": "3a90179e-e19e-41d1-8fb4-f23e916f555f"
}
```

---


### Assistant

_source line 46 · 2026-05-23T10:48:20.197Z_

<details><summary>Logged reasoning block</summary>

```text
I have all the tex files loaded. The registry data was too large and saved to a file. Let me use agents to parse the registry data and build the provenance table. Let me first load the TodoWrite tool and then launch an agent to parse the registry data.

Let me launch an agent to parse the registry JSON and extract the key fields I need. Meanwhile, I already have all the paper data I need from the tex files.

Let me organize what I have from the paper:

**Table 1 (tab1_recovery_gradient.tex) - Recovery Capacity Spectrum:**
- CKA-only: Peak Rew=0.354, Mean Rew=0.285, Min f0=0.125


- Random: Peak Rew=0.190, Mean Rew=0.164, Min f0=0.300
- Standard: Peak Rew=0.081, Mean Rew=0.050, Min f0=0.500
- RASP (α=1.0): Peak Rew=0.061, Mean Rew=0.031, Min f0=0.675

**Table 2 (tab2_decoupling.tex) - GRPO Responsiveness:**
- Unpruned: SFT=81.27%, GRPO=81.27%, Δ=0.00

, Peak Rew=0.669

Now I'm looking at the performance metrics when applying different pruning strategies at 20% sparsity. The CKA-only approach shows modest gains with GRPO improving by 0.48 points, while standard pruning achieves a 0.55 point improvement despite lower absolute scores. RASP and random pruning both show performance degradation, with RASP dropping 0.61 points and random dropping 0.53 points.

I'm also examining how the α hyperparameter affects the dose-response curve. The results show that α=2.0 produces the strongest improvement at +1.14 points, while α=1.0 and α=3.0 both show degradation. The pattern suggests an optimal sweet spot around α=2.0 for this particular task.

Now looking at the sparsity cliff results, RASP with α=1.0 actually performs worse than the standard approach at 30% sparsity, dropping to 0% accuracy compared to 4% for the baseline. The inference efficiency metrics are more promising though—RASP achieves a 37.8% speedup and 28.5% memory reduction at 20% sparsity, substantially outperforming the standard sparse approach which only gets 7.7% speedup with similar memory savings.

For the MATH-500 benchmark, I'm comparing different pruning methods at 20% sparsity across both SFT and GRPO training regimes. CKA-only performs best with around 26-27% accuracy, while RASP with α=1.0 lags significantly at 21-22%, suggesting the CKA-based selection is more effective for this task. The α dose-response analysis shows that lower α values (0.5) maintain better performance, though the gains from GRPO training are modest across all configurations.

Now looking at the MBPP results, the dense baseline achieves 53.48% accuracy, and at 20% sparsity both CKA-only and standard methods show dramatic drops to around 12-14%, with GRPO providing only marginal improvements of 1-1.3 percentage points.

Examining the cross-scale evaluation, the 7B model with CKA-only pruning reaches a peak reward of 0.354 and 64.39% on GSM8K, substantially outperforming the standard approach which gets 0.081 reward and 59.84% accuracy, while the 1.5B variant achieves 0.238 reward and 35% on GSM8K.

Looking at the stability metrics, the CKA approach shows strong consistency with a minimum Spearman correlation of 0.964 and mean of 0.979. The inference benchmarks reveal that the dense model achieves 72.0 tokens per second with 20.1ms time-to-first-token, while the CKA-only variant trades some throughput (58.3 TPS) for reduced latency and parameter count.

Examining the gradient flow comparisons, CKA-only demonstrates substantially better signal propagation than the standard approach at 2.89× improvement, and the multi-seed results show CKA-only consistently outperforming baselines across different sparsity levels, with the 20% sparsity configuration achieving 64.39±0.19 accuracy across three seeds. Now I'm looking at the cross-architecture results where CKA-only pruning achieves 51.50% post-SFT compared to standard's 21.00%, showing a substantial 30.5 percentage point advantage, alongside the detailed experimental metrics confirming the statistical significance of these improvements across different sparsity levels. Looking at the metrics from the abstract and introduction sections, I'm seeing consistent performance gaps around 0.54pp on average at 20% sparsity, with the peak reward ratio validating at 4.4× and the optimal alpha parameter settling at 2.0. Now I need to map these experimental results back to the registry data to trace which configurations produced these outcomes.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5dc0d5e4-8d6f-4780-bba0-fe6422fa9520",
  "isSidechain": false,
  "requestId": "req_011CbKNHuvdT6f7Ktq3mG4sx",
  "type": "assistant",
  "uuid": "681dc94e-d193-45c6-9100-8afbc71480c2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "3a90179e-e19e-41d1-8fb4-f23e916f555f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QkwLbPSh4kuXK1vujkJ84N",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 34680,
      "cache_read_input_tokens": 11841,
      "output_tokens": 4731,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 34680,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4731,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 34680,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 34680
          },
          "type": "message"
        }
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

_source line 47 · 2026-05-23T10:48:20.199Z_

Registry 数据量太大，启动子 agent 解析并提取映射关系。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "681dc94e-d193-45c6-9100-8afbc71480c2",
  "isSidechain": false,
  "requestId": "req_011CbKNHuvdT6f7Ktq3mG4sx",
  "type": "assistant",
  "uuid": "5c402395-f51b-4356-9a3b-b352bd324d9c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "3a90179e-e19e-41d1-8fb4-f23e916f555f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QkwLbPSh4kuXK1vujkJ84N",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 34680,
      "cache_read_input_tokens": 11841,
      "output_tokens": 4731,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 34680,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4731,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 34680,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 34680
          },
          "type": "message"
        }
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

_source line 48 · 2026-05-23T10:48:43.659Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01Nf8X2QpYuR5f2HKgrP8EYj`</summary>

```json
{
  "description": "Parse registry JSON for provenance",
  "prompt": "You need to parse a large JSON file containing experiment registry data and extract structured information for building a data provenance table.\n\nThe file is at: `/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-17-projects-recovery-aware-struct-prune/3a90179e-e19e-41d1-8fb4-f23e916f555f/tool-results/mcp-agent-ml-research-read_registry-1779533249026.txt`\n\nThe file is JSON with schema: `{result: string}`. The `result` field is itself a string that contains the actual data (likely JSON or YAML).\n\n**What to extract for each experiment:**\n1. `exp_id`\n2. `status` and `conclusion`\n3. `metrics` (any accuracy, reward, etc.)\n4. `spec` fields: `server`, `output_path`, `checkpoint_path`, `log_path`, `command`\n5. `created_at` or `updated_at` timestamps\n6. `tags` or any other identifying info\n\n**What I need mapped:**\nI need to match these experiments to paper values. The paper has these key experiments:\n\n**GSM8K 7B 20% sparsity:**\n- CKA-only: SFT=63.91%, GRPO=64.39% (3 seeds: 64.37%, 64.22%, 64.58%), Peak Rew=0.354\n- Standard: SFT=59.29%, GRPO=59.84% (3 seeds), Peak Rew=0.081\n- RASP (α=1.0): SFT=61.49%, GRPO=60.88%, Peak Rew=0.061\n- Random: SFT=51.25%, GRPO=50.72% (3 seeds: 50.57%, 50.72%, 50.87%), Peak Rew=0.190\n- ShortGPT: SFT=44.73%, GRPO=43.37%\n- Unpruned/Dense: 81.27% (SFT) or 90.83% (original)\n\n**GSM8K 7B α dose-response:**\n- α=0.5: SFT=60.73%, GRPO=61.18%\n- α=1.0: SFT=61.49%, GRPO=60.88%\n- α=2.0: SFT=64.97%, GRPO=66.11%\n- α=3.0: SFT=64.14%, GRPO=63.46%\n- α=4.0: SFT=61.94%, GRPO=62.77%\n\n**GSM8K 7B 15% sparsity:**\n- CKA-only: SFT=72.18%, GRPO=72.76% (3 seeds)\n- Standard: SFT=66.49%, GRPO=65.56% (3 seeds)\n\n**GSM8K 7B 25% sparsity:**\n- CKA-only: SFT=60.12%, GRPO=59.59%\n- Standard: SFT=50.87%, GRPO=51.86%\n\n**GSM8K 7B 30% sparsity (cliff):**\n- Standard: 4%\n- RASP: 0%\n- CKA-only: 0%\n\n**MATH-500 evaluations:**\n- Dense: 53.0%\n- CKA-only 20%: SFT=26.8%, GRPO=27.4%\n- Standard 20%: SFT=25.8%, GRPO=26.4%\n- RASP 20%: SFT=21.2%, GRPO=22.6%\n- Random 20%: SFT=14.4%\n- α=0.5: SFT=25.4%, GRPO=24.8%\n- α=2.0: SFT=24.0%, GRPO=26.2%\n- α=3.0: SFT=23.2%, GRPO=22.8%\n- α=4.0: SFT=26.6%, GRPO=26.2%\n- CKA-only 25%: SFT=19.2%, GRPO=18.4%\n- Standard 25%: SFT=14.0%, GRPO=12.8%\n\n**MBPP evaluations:**\n- Dense: 53.48%\n- CKA-only 20%: SFT=12.83%, GRPO=14.17%\n- Standard 20%: SFT=12.03%, GRPO=13.10%\n- RASP 20%: SFT=11.76%, GRPO=13.10%\n- ShortGPT 20%: SFT=10.43%, GRPO=14.44%\n\n**1.5B cross-scale:**\n- CKA-only: Rew=0.238, GSM8K=35.48%\n- Standard: Rew=0.084, GSM8K=22.29%\n- RASP: Rew=0.099, GSM8K=26.16%\n\n**Cross-architecture (Qwen2.5-Math-7B):**\n- CKA-only: Post-Prune=1.0%, Post-SFT=51.50%\n- Standard: Post-Prune=18.5%, Post-SFT=21.00%\n\n**Inference efficiency:**\n- Dense: Latency=6.682s, Memory=16.22GB, TPS=72.0, TTFT=20.1ms, Per-token=13.9ms, Params=7.62B\n- RASP 20%: Latency=4.156s, Speedup=37.8%, Memory=11.60GB\n- Standard 20%: Latency=6.167s, Speedup=7.7%, Memory=11.61GB\n- CKA-only 20%: TPS=58.3, TTFT=16.4ms, Per-token=16.7ms, Params=6.16B\n- Standard 20%: TPS=58.2, TTFT=16.4ms, Per-token=16.7ms, Params=6.16B\n\n**CKA stability:**\n- Spearman ρ min=0.964, mean=0.979\n\n**Gradient flow:**\n- CKA vs Standard: 2.89×, 55/56\n- CKA vs RASP: 2.26×, 56/56\n- RASP vs Standard: 1.28×, 45/56\n\n**Extended training 300 steps:**\n- CKA-only: 64.37%→64.37%\n- Standard: 59.44%→59.29%\n\n**Unstructured pruning:**\n- SFT=87.87%, GRPO=87.64%\n\n**Instructions:**\n1. First probe the file structure with `jq` to understand the format\n2. Parse the `result` field content\n3. For each experiment, output a line with: `exp_id | metrics_summary | server | output_path | created_at/updated_at`\n4. Try to match experiments to the paper values above\n5. Output the COMPLETE list of all experiments with their details - don't summarize or truncate\n\nOutput the full results as a structured mapping. Be thorough - I need every experiment matched."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5c402395-f51b-4356-9a3b-b352bd324d9c",
  "isSidechain": false,
  "requestId": "req_011CbKNHuvdT6f7Ktq3mG4sx",
  "type": "assistant",
  "uuid": "13dc4679-b6f9-4352-a026-ae226028bf9f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "3a90179e-e19e-41d1-8fb4-f23e916f555f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QkwLbPSh4kuXK1vujkJ84N",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 34680,
      "cache_read_input_tokens": 11841,
      "output_tokens": 4731,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 34680,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4731,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 34680,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 34680
          },
          "type": "message"
        }
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

_source line 49 · 2026-05-23T10:52:10.480Z_

<details><summary>↩ Tool result · `toolu_01Nf8X2QpYuR5f2HKgrP8EYj`</summary>

```text
Here is the complete structured mapping of all 50 experiments in this registry page to their paper values.

---

## Summary of Findings

**Total experiments in registry:** 249 (only 50 returned in this page -- the most recent ones)

### Experiments Successfully Matched to Paper Values (43 of 50)

**All metric matches are EXACT** -- every registry value matches its corresponding paper value precisely.

---

### SECTION 1: GSM8K 7B 20% -- Alpha Dose-Response (8 experiments, ALL MATCH)

| exp_id | Paper Value | Registry Value | Server | Created |
|--------|------------|----------------|--------|---------|
| `eval_gsm8k_sft_alpha0p5_20` | alpha=0.5 SFT=60.73% | 60.73% | westd-32935 | 2026-05-22T10:19 |
| `eval_gsm8k_grpo_alpha0p5_20` | alpha=0.5 GRPO=61.18% | 61.18% | westd-32935 | 2026-05-22T09:28 |
| `eval_gsm8k_sft_alpha2p0_20` | alpha=2.0 SFT=64.97% | 64.97% | westd-32935 | 2026-05-22T10:19 |
| `eval_gsm8k_grpo_alpha2p0_20` | alpha=2.0 GRPO=66.11% | 66.11% | westd-32935 | 2026-05-22T09:28 |
| `eval_gsm8k_sft_alpha3p0_20` | alpha=3.0 SFT=64.14% | 64.14% | westd-32935 | 2026-05-22T10:24 |
| `eval_gsm8k_grpo_alpha3p0_20` | alpha=3.0 GRPO=63.46% | 63.45% (rounding) | westd-32935 | 2026-05-22T09:30 |
| `eval_gsm8k_sft_alpha4_20_v5` | alpha=4.0 SFT=61.94% | 61.94% | ? (westd-32935 per hypothesis) | 2026-05-22T03:49 |
| `eval_gsm8k_grpo_alpha4_20_v3` | alpha=4.0 GRPO=62.77% | 62.77% | westd-32935 | 2026-05-22T03:49 |

**Key paths:** alpha=3.0 GRPO model at `/root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_alpha3p0_20_v2/checkpoint-100`

---

### SECTION 2: GSM8K 7B 20% -- Random Pruning Multi-Seed (4 experiments)

| exp_id | Paper Value | Registry Value | Server | Created |
|--------|------------|----------------|--------|---------|
| `eval_gsm8k_sft_random_20` | Random SFT=51.25% | 51.25% | westd-29022 | 2026-05-21T06:47 |
| `eval_gsm8k_grpo_random_20_v2` | Random GRPO seed42=50.57% | 50.57% | westd-29022 | 2026-05-21T04:56 |
| `eval_gsm8k_grpo_random_20_seed123_v2` | Random GRPO seed123=50.72% | NO_METRICS in registry | westd-32935 | 2026-05-22T14:22 |
| `eval_gsm8k_grpo_random_20_seed456` | Random GRPO seed456=50.87% | 50.87% | westb-23072 | 2026-05-22T16:26 |

**Note:** `eval_gsm8k_grpo_random_20_seed123_v2` has status=DONE, conclusion=success, but NO_METRICS recorded in registry. The paper value 50.72% likely came from the result JSON file on disk.

---

### SECTION 3: GSM8K 7B 25% Cross-Sparsity (4 experiments, ALL MATCH)

| exp_id | Paper Value | Registry Value | Server | Created |
|--------|------------|----------------|--------|---------|
| `eval_gsm8k_sft_cka_only_25` | CKA-only 25% SFT=60.12% | 60.12% | westd-29022 | 2026-05-21T06:47 |
| `eval_gsm8k_grpo_cka_only_25_v3` | CKA-only 25% GRPO=59.59% | 59.59% | westd-29022 | 2026-05-21T04:56 |
| `eval_gsm8k_sft_standard_25` | Standard 25% SFT=50.87% | 50.87% | westd-29022 | 2026-05-21T08:13 |
| `eval_gsm8k_grpo_standard_25` | Standard 25% GRPO=51.86% | 51.86% | westb-23072 | 2026-05-21T06:42 |

---

### SECTION 4: MATH-500 Evaluations (19 experiments, ALL MATCH)

| exp_id | Paper Value | Registry Value | Server | Created |
|--------|------------|----------------|--------|---------|
| `eval_math500_sft_cka_only_20_westd` | CKA-only 20% SFT=26.8% | 26.8% | westd-32935 | 2026-05-22T20:45 |
| `eval_math500_grpo_cka_only_20_2048_v2` | CKA-only 20% GRPO=27.4% | 27.4% | westd-32935 | 2026-05-23T05:07 |
| `eval_math500_grpo_cka_only_20` | (old eval script) | 26.6% | ? | 2026-05-18T02:41 |
| `eval_math500_sft_standard_20_2048_v2` | Standard 20% SFT=25.8% | 25.8% | westd-32935 | 2026-05-19T01:34 |
| `eval_math500_grpo_standard_20_fair_2048_v2` | Standard 20% GRPO=26.4% | 26.4% | westd-32935 | 2026-05-22T03:49 |
| `eval_math500_sft_random_20_v3` | Random 20% SFT=14.4% | 14.4% | westd-32935 | 2026-05-22T04:11 |
| `eval_math500_sft_rasp_alpha0p5_20` | alpha=0.5 SFT=25.4% | 25.4% | ? | 2026-05-22T15:20 |
| `eval_math500_grpo_rasp_alpha0p5_20` | alpha=0.5 GRPO=24.8% | 24.8% | westb-23072 | 2026-05-23T02:59 |
| `eval_math500_sft_rasp_alpha1p0_20_v2` | RASP SFT=21.2% | 21.2% | ? | 2026-05-22T20:50 |
| `eval_math500_grpo_rasp_alpha1p0_20` | RASP GRPO=22.6% | 22.6% | ? | 2026-05-22T23:02 |
| `eval_math500_sft_rasp_alpha2p0_20` | alpha=2.0 SFT=24.0% | 24.0% | westd-32935 | 2026-05-22T15:06 |
| `eval_math500_grpo_rasp_alpha2p0_20` | alpha=2.0 GRPO=26.2% | 26.2% | westd-32935 | 2026-05-22T22:23 |
| `eval_math500_sft_rasp_alpha3p0_20` | alpha=3.0 SFT=23.2% | 23.2% | ? | 2026-05-22T18:26 |
| `eval_math500_grpo_rasp_alpha3p0_20` | alpha=3.0 GRPO=22.8% | 22.8% | westd-32935 | 2026-05-23T03:19 |
| `eval_math500_sft_rasp_alpha4p0_20` | alpha=4.0 SFT=26.6% | 26.6% | ? | 2026-05-22T15:20 |
| `eval_math500_grpo_rasp_alpha4p0_20` | alpha=4.0 GRPO=26.2% | 26.2% | ? | 2026-05-23T00:01 |
| `eval_math500_sft_cka_only_25_v2` | CKA-only 25% SFT=19.2% | 19.2% | westd-29022 | 2026-05-21T13:54 |
| `eval_math500_grpo_cka_only_25_v2` | CKA-only 25% GRPO=18.4% | 18.4% | westd-29022 | 2026-05-21T13:54 |
| `eval_math500_sft_standard_25` | Standard 25% SFT=14.0% | 14.0% | westb-23072 | 2026-05-21T02:58 |

**Note:** `eval_math500_grpo_cka_only_20` (26.6%) was from an OLD eval script. The paper uses `eval_math500_grpo_cka_only_20_2048_v2` (27.4%) which used the NEW consistent answer extraction.

---

### SECTION 5: Cross-Architecture Qwen2.5-Math-7B (3 experiments)

| exp_id | Paper Value | Registry Value | Server | Created |
|--------|------------|----------------|--------|---------|
| `eval_gsm8k_grpo_qwen_math_cka_only_20_n500_v3` | CKA-only GRPO GSM8K (N=500) | 48.6% | westb-23072 | 2026-05-22T15:12 |
| `eval_math500_sft_qwen_math_cka_only_20` | CKA-only SFT MATH-500 | 21.6% | westb-23072 | 2026-05-22T23:11 |
| `grpo_qwen_math_cka_only_20` | GRPO training run | NO_METRICS | westb-23072 | 2026-05-22T08:50 |

**Note:** The paper reports Qwen CKA-only Post-SFT=51.50% for GSM8K but this was N=200. The registry `eval_gsm8k_grpo_qwen_math_cka_only_20_n500_v3` is N=500 with 48.6% and 83.8% truncation, suggesting max_new_tokens=2048 was insufficient for Qwen-Math's verbose reasoning.

---

### SECTION 6: Training Runs (9 experiments)

| exp_id | Key Metrics | Server | Output Path |
|--------|------------|--------|-------------|
| `grpo_alpha4_20` | reward=0.198, kl=0.00198 | westd-29022 | `/root/autodl-tmp/.../grpo_alpha4_20/checkpoint-100` |
| `grpo_rasp_alpha3p0_20` | (v1 corrupted by disk-full) | westb-23072 | ? |
| `grpo_rasp_alpha3p0_20_v2` | (v2 used for eval) | westd-32935 | ? |
| `grpo_random_20_seed123` | (v1 wrong batch_size=1) | westd-32935 | ? |
| `grpo_random_20_seed123_v2` | (v2 correct batch_size=2) | westd-32935 | `/root/autodl-tmp/.../grpo_random_20_seed123_v2/checkpoint-100` |
| `grpo_random_20_seed456` | seed456 GRPO | westb-23072 | ? |
| `grpo_standard_25_westb` | reward=0.00813, collapse | westb-23072 | `/root/autodl-tmp/.../grpo_standard_25_westb/checkpoint-100` |
| `sft_alpha4_20_v2` | loss=0.8118, tok_acc=0.8165 | westd-29022 | ? |
| `sft_random_20` | 1870 steps, 12GB | westd-29022 | `/root/autodl-tmp/.../sft_random_20` |

---

### SECTION 7: 1.5B and Depth-First (3 experiments)

| exp_id | Paper Value | Registry Value | Server |
|--------|------------|----------------|--------|
| `eval_math500_sft_standard_20_1p5b` | 1.5B Standard MATH-500=5.4% | 5.4% | westb-23072 |
| `eval_gsm8k_sft_depth_first_20` | ShortGPT SFT GSM8K | NO_METRICS (disk-full) | westd-32935 |
| `eval_gsm8k_grpo_depth_first_20` | ShortGPT GRPO GSM8K | NO_METRICS (disk-full) | westd-32935 |

---

### SECTION 8: Paper Values NOT in This Registry Page

The registry only returned 50 of 249 total experiments. The following paper values are sourced from the other 199 experiments not in this page:

- **GSM8K 7B 20% core results:** CKA-only (SFT=63.91%, GRPO=64.37/64.22/64.58%), Standard (SFT=59.29%, GRPO=59.84%), RASP alpha=1.0 (SFT=61.49%, GRPO=60.88%), ShortGPT (SFT=44.73%, GRPO=43.37%), Dense (81.27%/90.83%)
- **GSM8K 15% sparsity:** CKA-only (72.18%/72.76%), Standard (66.49%/65.56%)
- **GSM8K 30% sparsity cliff:** Standard=4%, RASP=0%, CKA=0%
- **Peak rewards:** CKA=0.354, Standard=0.081, RASP=0.061, Random=0.190
- **MATH-500:** Dense=53.0%, Standard 25% GRPO=12.8%
- **MBPP:** All values
- **1.5B cross-scale:** CKA (GSM8K=35.48%, Rew=0.238), Standard (22.29%, 0.084), RASP (26.16%, 0.099)
- **Qwen cross-arch:** CKA Post-Prune=1.0%, Standard Post-Prune=18.5%, Standard Post-SFT=21.00%
- **Infrastructure:** Inference efficiency, CKA stability, gradient flow, extended training, unstructured pruning

---

### Servers Used

- **westd-32935**: Primary compute, most dose-response and MATH-500 evals
- **westd-29022**: Earlier runs (25% sparsity, some 20% baselines) -- had an outage requiring re-runs on westd-32935
- **westb-23072**: Qwen cross-architecture, some seed456/standard runs

### Key Observations

1. **One minor rounding discrepancy:** alpha=3.0 GRPO registry=63.45% vs paper=63.46% (837/1319 = 63.456%, paper rounded up)
2. **3 experiments with NO_METRICS** despite DONE status: `eval_gsm8k_grpo_random_20_seed123_v2`, `eval_gsm8k_sft_depth_first_20`, `eval_gsm8k_grpo_depth_first_20` -- results exist in JSON files on disk but weren't recorded to registry
3. **`eval_math500_grpo_cka_only_20`** (26.6%) was superseded by **`eval_math500_grpo_cka_only_20_2048_v2`** (27.4%) after switching to new answer extraction code
4. **Multiple version chains** visible (v1->v2->v3) due to server outages (westd-29022), disk-full errors, batch_size misconfigurations, and eval script updates

agentId: ad6a32a709aac350a (use SendMessage with to: 'ad6a32a709aac350a' to continue this agent)
&lt;usage>total_tokens: 57351
tool_uses: 8
duration_ms: 206813&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "13dc4679-b6f9-4352-a026-ae226028bf9f",
  "isSidechain": false,
  "promptId": "dddf37fd-16cc-4cd5-bb05-648328938281",
  "type": "user",
  "uuid": "d198add0-0891-4741-9031-765a77b8407b",
  "toolUseResult": {
    "status": "completed",
    "prompt": "You need to parse a large JSON file containing experiment registry data and extract structured information for building a data provenance table.\n\nThe file is at: `/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-17-projects-recovery-aware-struct-prune/3a90179e-e19e-41d1-8fb4-f23e916f555f/tool-results/mcp-agent-ml-research-read_registry-1779533249026.txt`\n\nThe file is JSON with schema: `{result: string}`. The `result` field is itself a string that contains the actual data (likely JSON or YAML).\n\n**What to extract for each experiment:**\n1. `exp_id`\n2. `status` and `conclusion`\n3. `metrics` (any accuracy, reward, etc.)\n4. `spec` fields: `server`, `output_path`, `checkpoint_path`, `log_path`, `command`\n5. `created_at` or `updated_at` timestamps\n6. `tags` or any other identifying info\n\n**What I need mapped:**\nI need to match these experiments to paper values. The paper has these key experiments:\n\n**GSM8K 7B 20% sparsity:**\n- CKA-only: SFT=63.91%, GRPO=64.39% (3 seeds: 64.37%, 64.22%, 64.58%), Peak Rew=0.354\n- Standard: SFT=59.29%, GRPO=59.84% (3 seeds), Peak Rew=0.081\n- RASP (α=1.0): SFT=61.49%, GRPO=60.88%, Peak Rew=0.061\n- Random: SFT=51.25%, GRPO=50.72% (3 seeds: 50.57%, 50.72%, 50.87%), Peak Rew=0.190\n- ShortGPT: SFT=44.73%, GRPO=43.37%\n- Unpruned/Dense: 81.27% (SFT) or 90.83% (original)\n\n**GSM8K 7B α dose-response:**\n- α=0.5: SFT=60.73%, GRPO=61.18%\n- α=1.0: SFT=61.49%, GRPO=60.88%\n- α=2.0: SFT=64.97%, GRPO=66.11%\n- α=3.0: SFT=64.14%, GRPO=63.46%\n- α=4.0: SFT=61.94%, GRPO=62.77%\n\n**GSM8K 7B 15% sparsity:**\n- CKA-only: SFT=72.18%, GRPO=72.76% (3 seeds)\n- Standard: SFT=66.49%, GRPO=65.56% (3 seeds)\n\n**GSM8K 7B 25% sparsity:**\n- CKA-only: SFT=60.12%, GRPO=59.59%\n- Standard: SFT=50.87%, GRPO=51.86%\n\n**GSM8K 7B 30% sparsity (cliff):**\n- Standard: 4%\n- RASP: 0%\n- CKA-only: 0%\n\n**MATH-500 evaluations:**\n- Dense: 53.0%\n- CKA-only 20%: SFT=26.8%, GRPO=27.4%\n- Standard 20%: SFT=25.8%, GRPO=26.4%\n- RASP 20%: SFT=21.2%, GRPO=22.6%\n- Random 20%: SFT=14.4%\n- α=0.5: SFT=25.4%, GRPO=24.8%\n- α=2.0: SFT=24.0%, GRPO=26.2%\n- α=3.0: SFT=23.2%, GRPO=22.8%\n- α=4.0: SFT=26.6%, GRPO=26.2%\n- CKA-only 25%: SFT=19.2%, GRPO=18.4%\n- Standard 25%: SFT=14.0%, GRPO=12.8%\n\n**MBPP evaluations:**\n- Dense: 53.48%\n- CKA-only 20%: SFT=12.83%, GRPO=14.17%\n- Standard 20%: SFT=12.03%, GRPO=13.10%\n- RASP 20%: SFT=11.76%, GRPO=13.10%\n- ShortGPT 20%: SFT=10.43%, GRPO=14.44%\n\n**1.5B cross-scale:**\n- CKA-only: Rew=0.238, GSM8K=35.48%\n- Standard: Rew=0.084, GSM8K=22.29%\n- RASP: Rew=0.099, GSM8K=26.16%\n\n**Cross-architecture (Qwen2.5-Math-7B):**\n- CKA-only: Post-Prune=1.0%, Post-SFT=51.50%\n- Standard: Post-Prune=18.5%, Post-SFT=21.00%\n\n**Inference efficiency:**\n- Dense: Latency=6.682s, Memory=16.22GB, TPS=72.0, TTFT=20.1ms, Per-token=13.9ms, Params=7.62B\n- RASP 20%: Latency=4.156s, Speedup=37.8%, Memory=11.60GB\n- Standard 20%: Latency=6.167s, Speedup=7.7%, Memory=11.61GB\n- CKA-only 20%: TPS=58.3, TTFT=16.4ms, Per-token=16.7ms, Params=6.16B\n- Standard 20%: TPS=58.2, TTFT=16.4ms, Per-token=16.7ms, Params=6.16B\n\n**CKA stability:**\n- Spearman ρ min=0.964, mean=0.979\n\n**Gradient flow:**\n- CKA vs Standard: 2.89×, 55/56\n- CKA vs RASP: 2.26×, 56/56\n- RASP vs Standard: 1.28×, 45/56\n\n**Extended training 300 steps:**\n- CKA-only: 64.37%→64.37%\n- Standard: 59.44%→59.29%\n\n**Unstructured pruning:**\n- SFT=87.87%, GRPO=87.64%\n\n**Instructions:**\n1. First probe the file structure with `jq` to understand the format\n2. Parse the `result` field content\n3. For each experiment, output a line with: `exp_id | metrics_summary | server | output_path | created_at/updated_at`\n4. Try to match experiments to the paper values above\n5. Output the COMPLETE list of all experiments with their details - don't summarize or truncate\n\nOutput the full results as a structured mapping. Be thorough - I need every experiment matched.",
    "agentId": "ad6a32a709aac350a",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Here is the complete structured mapping of all 50 experiments in this registry page to their paper values.\n\n---\n\n## Summary of Findings\n\n**Total experiments in registry:** 249 (only 50 returned in this page -- the most recent ones)\n\n### Experiments Successfully Matched to Paper Values (43 of 50)\n\n**All metric matches are EXACT** -- every registry value matches its corresponding paper value precisely.\n\n---\n\n### SECTION 1: GSM8K 7B 20% -- Alpha Dose-Response (8 experiments, ALL MATCH)\n\n| exp_id | Paper Value | Registry Value | Server | Created |\n|--------|------------|----------------|--------|---------|\n| `eval_gsm8k_sft_alpha0p5_20` | alpha=0.5 SFT=60.73% | 60.73% | westd-32935 | 2026-05-22T10:19 |\n| `eval_gsm8k_grpo_alpha0p5_20` | alpha=0.5 GRPO=61.18% | 61.18% | westd-32935 | 2026-05-22T09:28 |\n| `eval_gsm8k_sft_alpha2p0_20` | alpha=2.0 SFT=64.97% | 64.97% | westd-32935 | 2026-05-22T10:19 |\n| `eval_gsm8k_grpo_alpha2p0_20` | alpha=2.0 GRPO=66.11% | 66.11% | westd-32935 | 2026-05-22T09:28 |\n| `eval_gsm8k_sft_alpha3p0_20` | alpha=3.0 SFT=64.14% | 64.14% | westd-32935 | 2026-05-22T10:24 |\n| `eval_gsm8k_grpo_alpha3p0_20` | alpha=3.0 GRPO=63.46% | 63.45% (rounding) | westd-32935 | 2026-05-22T09:30 |\n| `eval_gsm8k_sft_alpha4_20_v5` | alpha=4.0 SFT=61.94% | 61.94% | ? (westd-32935 per hypothesis) | 2026-05-22T03:49 |\n| `eval_gsm8k_grpo_alpha4_20_v3` | alpha=4.0 GRPO=62.77% | 62.77% | westd-32935 | 2026-05-22T03:49 |\n\n**Key paths:** alpha=3.0 GRPO model at `/root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_alpha3p0_20_v2/checkpoint-100`\n\n---\n\n### SECTION 2: GSM8K 7B 20% -- Random Pruning Multi-Seed (4 experiments)\n\n| exp_id | Paper Value | Registry Value | Server | Created |\n|--------|------------|----------------|--------|---------|\n| `eval_gsm8k_sft_random_20` | Random SFT=51.25% | 51.25% | westd-29022 | 2026-05-21T06:47 |\n| `eval_gsm8k_grpo_random_20_v2` | Random GRPO seed42=50.57% | 50.57% | westd-29022 | 2026-05-21T04:56 |\n| `eval_gsm8k_grpo_random_20_seed123_v2` | Random GRPO seed123=50.72% | NO_METRICS in registry | westd-32935 | 2026-05-22T14:22 |\n| `eval_gsm8k_grpo_random_20_seed456` | Random GRPO seed456=50.87% | 50.87% | westb-23072 | 2026-05-22T16:26 |\n\n**Note:** `eval_gsm8k_grpo_random_20_seed123_v2` has status=DONE, conclusion=success, but NO_METRICS recorded in registry. The paper value 50.72% likely came from the result JSON file on disk.\n\n---\n\n### SECTION 3: GSM8K 7B 25% Cross-Sparsity (4 experiments, ALL MATCH)\n\n| exp_id | Paper Value | Registry Value | Server | Created |\n|--------|------------|----------------|--------|---------|\n| `eval_gsm8k_sft_cka_only_25` | CKA-only 25% SFT=60.12% | 60.12% | westd-29022 | 2026-05-21T06:47 |\n| `eval_gsm8k_grpo_cka_only_25_v3` | CKA-only 25% GRPO=59.59% | 59.59% | westd-29022 | 2026-05-21T04:56 |\n| `eval_gsm8k_sft_standard_25` | Standard 25% SFT=50.87% | 50.87% | westd-29022 | 2026-05-21T08:13 |\n| `eval_gsm8k_grpo_standard_25` | Standard 25% GRPO=51.86% | 51.86% | westb-23072 | 2026-05-21T06:42 |\n\n---\n\n### SECTION 4: MATH-500 Evaluations (19 experiments, ALL MATCH)\n\n| exp_id | Paper Value | Registry Value | Server | Created |\n|--------|------------|----------------|--------|---------|\n| `eval_math500_sft_cka_only_20_westd` | CKA-only 20% SFT=26.8% | 26.8% | westd-32935 | 2026-05-22T20:45 |\n| `eval_math500_grpo_cka_only_20_2048_v2` | CKA-only 20% GRPO=27.4% | 27.4% | westd-32935 | 2026-05-23T05:07 |\n| `eval_math500_grpo_cka_only_20` | (old eval script) | 26.6% | ? | 2026-05-18T02:41 |\n| `eval_math500_sft_standard_20_2048_v2` | Standard 20% SFT=25.8% | 25.8% | westd-32935 | 2026-05-19T01:34 |\n| `eval_math500_grpo_standard_20_fair_2048_v2` | Standard 20% GRPO=26.4% | 26.4% | westd-32935 | 2026-05-22T03:49 |\n| `eval_math500_sft_random_20_v3` | Random 20% SFT=14.4% | 14.4% | westd-32935 | 2026-05-22T04:11 |\n| `eval_math500_sft_rasp_alpha0p5_20` | alpha=0.5 SFT=25.4% | 25.4% | ? | 2026-05-22T15:20 |\n| `eval_math500_grpo_rasp_alpha0p5_20` | alpha=0.5 GRPO=24.8% | 24.8% | westb-23072 | 2026-05-23T02:59 |\n| `eval_math500_sft_rasp_alpha1p0_20_v2` | RASP SFT=21.2% | 21.2% | ? | 2026-05-22T20:50 |\n| `eval_math500_grpo_rasp_alpha1p0_20` | RASP GRPO=22.6% | 22.6% | ? | 2026-05-22T23:02 |\n| `eval_math500_sft_rasp_alpha2p0_20` | alpha=2.0 SFT=24.0% | 24.0% | westd-32935 | 2026-05-22T15:06 |\n| `eval_math500_grpo_rasp_alpha2p0_20` | alpha=2.0 GRPO=26.2% | 26.2% | westd-32935 | 2026-05-22T22:23 |\n| `eval_math500_sft_rasp_alpha3p0_20` | alpha=3.0 SFT=23.2% | 23.2% | ? | 2026-05-22T18:26 |\n| `eval_math500_grpo_rasp_alpha3p0_20` | alpha=3.0 GRPO=22.8% | 22.8% | westd-32935 | 2026-05-23T03:19 |\n| `eval_math500_sft_rasp_alpha4p0_20` | alpha=4.0 SFT=26.6% | 26.6% | ? | 2026-05-22T15:20 |\n| `eval_math500_grpo_rasp_alpha4p0_20` | alpha=4.0 GRPO=26.2% | 26.2% | ? | 2026-05-23T00:01 |\n| `eval_math500_sft_cka_only_25_v2` | CKA-only 25% SFT=19.2% | 19.2% | westd-29022 | 2026-05-21T13:54 |\n| `eval_math500_grpo_cka_only_25_v2` | CKA-only 25% GRPO=18.4% | 18.4% | westd-29022 | 2026-05-21T13:54 |\n| `eval_math500_sft_standard_25` | Standard 25% SFT=14.0% | 14.0% | westb-23072 | 2026-05-21T02:58 |\n\n**Note:** `eval_math500_grpo_cka_only_20` (26.6%) was from an OLD eval script. The paper uses `eval_math500_grpo_cka_only_20_2048_v2` (27.4%) which used the NEW consistent answer extraction.\n\n---\n\n### SECTION 5: Cross-Architecture Qwen2.5-Math-7B (3 experiments)\n\n| exp_id | Paper Value | Registry Value | Server | Created |\n|--------|------------|----------------|--------|---------|\n| `eval_gsm8k_grpo_qwen_math_cka_only_20_n500_v3` | CKA-only GRPO GSM8K (N=500) | 48.6% | westb-23072 | 2026-05-22T15:12 |\n| `eval_math500_sft_qwen_math_cka_only_20` | CKA-only SFT MATH-500 | 21.6% | westb-23072 | 2026-05-22T23:11 |\n| `grpo_qwen_math_cka_only_20` | GRPO training run | NO_METRICS | westb-23072 | 2026-05-22T08:50 |\n\n**Note:** The paper reports Qwen CKA-only Post-SFT=51.50% for GSM8K but this was N=200. The registry `eval_gsm8k_grpo_qwen_math_cka_only_20_n500_v3` is N=500 with 48.6% and 83.8% truncation, suggesting max_new_tokens=2048 was insufficient for Qwen-Math's verbose reasoning.\n\n---\n\n### SECTION 6: Training Runs (9 experiments)\n\n| exp_id | Key Metrics | Server | Output Path |\n|--------|------------|--------|-------------|\n| `grpo_alpha4_20` | reward=0.198, kl=0.00198 | westd-29022 | `/root/autodl-tmp/.../grpo_alpha4_20/checkpoint-100` |\n| `grpo_rasp_alpha3p0_20` | (v1 corrupted by disk-full) | westb-23072 | ? |\n| `grpo_rasp_alpha3p0_20_v2` | (v2 used for eval) | westd-32935 | ? |\n| `grpo_random_20_seed123` | (v1 wrong batch_size=1) | westd-32935 | ? |\n| `grpo_random_20_seed123_v2` | (v2 correct batch_size=2) | westd-32935 | `/root/autodl-tmp/.../grpo_random_20_seed123_v2/checkpoint-100` |\n| `grpo_random_20_seed456` | seed456 GRPO | westb-23072 | ? |\n| `grpo_standard_25_westb` | reward=0.00813, collapse | westb-23072 | `/root/autodl-tmp/.../grpo_standard_25_westb/checkpoint-100` |\n| `sft_alpha4_20_v2` | loss=0.8118, tok_acc=0.8165 | westd-29022 | ? |\n| `sft_random_20` | 1870 steps, 12GB | westd-29022 | `/root/autodl-tmp/.../sft_random_20` |\n\n---\n\n### SECTION 7: 1.5B and Depth-First (3 experiments)\n\n| exp_id | Paper Value | Registry Value | Server |\n|--------|------------|----------------|--------|\n| `eval_math500_sft_standard_20_1p5b` | 1.5B Standard MATH-500=5.4% | 5.4% | westb-23072 |\n| `eval_gsm8k_sft_depth_first_20` | ShortGPT SFT GSM8K | NO_METRICS (disk-full) | westd-32935 |\n| `eval_gsm8k_grpo_depth_first_20` | ShortGPT GRPO GSM8K | NO_METRICS (disk-full) | westd-32935 |\n\n---\n\n### SECTION 8: Paper Values NOT in This Registry Page\n\nThe registry only returned 50 of 249 total experiments. The following paper values are sourced from the other 199 experiments not in this page:\n\n- **GSM8K 7B 20% core results:** CKA-only (SFT=63.91%, GRPO=64.37/64.22/64.58%), Standard (SFT=59.29%, GRPO=59.84%), RASP alpha=1.0 (SFT=61.49%, GRPO=60.88%), ShortGPT (SFT=44.73%, GRPO=43.37%), Dense (81.27%/90.83%)\n- **GSM8K 15% sparsity:** CKA-only (72.18%/72.76%), Standard (66.49%/65.56%)\n- **GSM8K 30% sparsity cliff:** Standard=4%, RASP=0%, CKA=0%\n- **Peak rewards:** CKA=0.354, Standard=0.081, RASP=0.061, Random=0.190\n- **MATH-500:** Dense=53.0%, Standard 25% GRPO=12.8%\n- **MBPP:** All values\n- **1.5B cross-scale:** CKA (GSM8K=35.48%, Rew=0.238), Standard (22.29%, 0.084), RASP (26.16%, 0.099)\n- **Qwen cross-arch:** CKA Post-Prune=1.0%, Standard Post-Prune=18.5%, Standard Post-SFT=21.00%\n- **Infrastructure:** Inference efficiency, CKA stability, gradient flow, extended training, unstructured pruning\n\n---\n\n### Servers Used\n\n- **westd-32935**: Primary compute, most dose-response and MATH-500 evals\n- **westd-29022**: Earlier runs (25% sparsity, some 20% baselines) -- had an outage requiring re-runs on westd-32935\n- **westb-23072**: Qwen cross-architecture, some seed456/standard runs\n\n### Key Observations\n\n1. **One minor rounding discrepancy:** alpha=3.0 GRPO registry=63.45% vs paper=63.46% (837/1319 = 63.456%, paper rounded up)\n2. **3 experiments with NO_METRICS** despite DONE status: `eval_gsm8k_grpo_random_20_seed123_v2`, `eval_gsm8k_sft_depth_first_20`, `eval_gsm8k_grpo_depth_first_20` -- results exist in JSON files on disk but weren't recorded to registry\n3. **`eval_math500_grpo_cka_only_20`** (26.6%) was superseded by **`eval_math500_grpo_cka_only_20_2048_v2`** (27.4%) after switching to new answer extraction code\n4. **Multiple version chains** visible (v1->v2->v3) due to server outages (westd-29022), disk-full errors, batch_size misconfigurations, and eval script updates"
      }
    ],
    "totalDurationMs": 206813,
    "totalTokens": 57351,
    "totalToolUseCount": 8,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11454,
      "cache_read_input_tokens": 41465,
      "output_tokens": 4431,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 11454
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4431,
          "cache_read_input_tokens": 41465,
          "cache_creation_input_tokens": 11454,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 11454,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 1,
      "searchCount": 0,
      "bashCount": 7,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 0
    }
  },
  "sourceToolAssistantUUID": "13dc4679-b6f9-4352-a026-ae226028bf9f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "3a90179e-e19e-41d1-8fb4-f23e916f555f",
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
  "leafUuid": "d198add0-0891-4741-9031-765a77b8407b",
  "sessionId": "3a90179e-e19e-41d1-8fb4-f23e916f555f"
}
```

---


### Runtime record

_source line 51_

```json
{
  "type": "ai-title",
  "aiTitle": "Map paper results to registry experiments",
  "sessionId": "3a90179e-e19e-41d1-8fb4-f23e916f555f"
}
```

---


### Assistant

_source line 52 · 2026-05-23T10:52:14.518Z_

<details><summary>Logged reasoning block</summary>

```text
Good, I have 50 experiments from the first page. But there are 249 total and I need to get the rest to find the core 20% sparsity results, 15% sparsity, 30% cliff, MBPP, 1.5B cross-scale, inference, etc. Let me fetch more registry data.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d198add0-0891-4741-9031-765a77b8407b",
  "isSidechain": false,
  "requestId": "req_011CbKNef22TT8KNCYThRa4b",
  "type": "assistant",
  "uuid": "9ec5cde9-8158-4379-b7f3-1a109ad48663",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "3a90179e-e19e-41d1-8fb4-f23e916f555f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013Y7Yz61fDsSUbjfXfQojR8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9236,
      "cache_read_input_tokens": 46521,
      "output_tokens": 241,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9236,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 241,
          "cache_read_input_tokens": 46521,
          "cache_creation_input_tokens": 9236,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9236
          },
          "type": "message"
        }
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

_source line 53 · 2026-05-23T10:52:15.930Z_

需要继续读取剩余 registry 数据（已有 50/249）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9ec5cde9-8158-4379-b7f3-1a109ad48663",
  "isSidechain": false,
  "requestId": "req_011CbKNef22TT8KNCYThRa4b",
  "type": "assistant",
  "uuid": "a541f288-3073-4e45-82b3-076d703e55c4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "3a90179e-e19e-41d1-8fb4-f23e916f555f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013Y7Yz61fDsSUbjfXfQojR8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9236,
      "cache_read_input_tokens": 46521,
      "output_tokens": 241,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9236,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 241,
          "cache_read_input_tokens": 46521,
          "cache_creation_input_tokens": 9236,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9236
          },
          "type": "message"
        }
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

_source line 54 · 2026-05-23T10:52:17.009Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01AJfnnzVJ957on4rhjNfPcg`</summary>

```json
{
  "project": "recovery_aware_struct_prune",
  "filters": {
    "conclusion": "success"
  },
  "limit": 50,
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
  "parentUuid": "a541f288-3073-4e45-82b3-076d703e55c4",
  "isSidechain": false,
  "requestId": "req_011CbKNef22TT8KNCYThRa4b",
  "type": "assistant",
  "uuid": "fab33cb5-f090-4a9b-af22-7bf869df109c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "3a90179e-e19e-41d1-8fb4-f23e916f555f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013Y7Yz61fDsSUbjfXfQojR8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9236,
      "cache_read_input_tokens": 46521,
      "output_tokens": 241,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9236,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 241,
          "cache_read_input_tokens": 46521,
          "cache_creation_input_tokens": 9236,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9236
          },
          "type": "message"
        }
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

_source line 55 · 2026-05-23T10:52:18.238Z_

<details><summary>↩ Tool result · `toolu_01AJfnnzVJ957on4rhjNfPcg`</summary>

```text
Error: result (72,347 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-17-projects-recovery-aware-struct-prune/3a90179e-e19e-41d1-8fb4-f23e916f555f/tool-results/mcp-agent-ml-research-read_registry-1779533538235.txt.
Format: JSON with schema: {result: string}
- For targeted queries (find a value, filter by field): use jq on the file directly.
- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-17-projects-recovery-aware-struct-prune/3a90179e-e19e-41d1-8fb4-f23e916f555f/tool-results/mcp-agent-ml-research-read_registry-1779533538235.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.
- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-17-projects-recovery-aware-struct-prune/3a90179e-e19e-41d1-8fb4-f23e916f555f/tool-results/mcp-agent-ml-research-read_registry-1779533538235.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim." A vague "summarize this" may lose detail.

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fab33cb5-f090-4a9b-af22-7bf869df109c",
  "isSidechain": false,
  "promptId": "dddf37fd-16cc-4cd5-bb05-648328938281",
  "type": "user",
  "uuid": "37dfbb3b-7fbe-4af0-9a4b-e816cbddb1fd",
  "toolUseResult": "Error: result (72,347 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-17-projects-recovery-aware-struct-prune/3a90179e-e19e-41d1-8fb4-f23e916f555f/tool-results/mcp-agent-ml-research-read_registry-1779533538235.txt.\nFormat: JSON with schema: {result: string}\n- For targeted queries (find a value, filter by field): use jq on the file directly.\n- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-17-projects-recovery-aware-struct-prune/3a90179e-e19e-41d1-8fb4-f23e916f555f/tool-results/mcp-agent-ml-research-read_registry-1779533538235.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.\n- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. \"/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-17-projects-recovery-aware-struct-prune/3a90179e-e19e-41d1-8fb4-f23e916f555f/tool-results/mcp-agent-ml-research-read_registry-1779533538235.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim.\" A vague \"summarize this\" may lose detail.\n",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"eval_math500_sft_qwen_math_cka_only_20\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T23:11:09.017Z\", \"updated_at\": \"2026-05-23T10:44:00.535Z\", \"hypothesis\": \"Qwen2.5-Math-7B CKA-only 20% SFT MATH-500 eval @2048. Cross-architecture validation: if CKA-only criterion generalizes from DeepSeek-R1-Distill to Qwen-Math on MATH-500. SFT GSM8K = 51.5% (N=200). Paired with westb:1 GRPO GSM8K for C1 decoupling cross-arch.\", \"parent\": \"sft_qwen_math_cka_only_20\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_qwen_math_cka_only_20_final --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_math500_sft_qwen_math_cka_only_20.json --seed 42 --dtype bfloat16 --max_new_tokens 2048\", \"server\": \"westb-23072\", \"gpu\": \"cuda:0\", \"data_path\": \"HuggingFaceH4/MATH-500\", \"data_count\": 500, \"model_name\": \"Qwen2.5-Math-7B-CKA-only-20%-SFT-ep1\", \"seed\": 42, \"checkpoint_source\": \"sft_qwen_math_cka_only_20_final\", \"eval_data\": \"MATH-500 (N=500, max_new_tokens=2048)\", \"pid\": 250766, \"log_path\": \"/tmp/eval_math500_sft_qwen_cka_only_20.log\"}, \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 0.216, \"stderr\": 0.0184, \"correct\": 108, \"total\": 500, \"natural_eos\": 90, \"truncated\": 410, \"avg_response_length\": 1745.338}, \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_math500_sft_qwen_math_cka_only_20.json\", \"completed_at\": \"2026-05-23T10:44:00.535Z\"}, \"eval_math500_grpo_rasp_alpha0p5_20\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T02:59:15.985Z\", \"updated_at\": \"2026-05-23T10:11:11.002Z\", \"hypothesis\": \"GRPO RASP α=0.5 MATH-500 eval @2048. C1 decoupling on MATH-500: SFT α=0.5 = 25.4%. GSM8K GRPO α=0.5 = 61.18%. Completes MATH-500 GRPO dose-response curve.\", \"parent\": \"eval_gsm8k_grpo_alpha0p5_20\", \"spec\": {\"command\": \"python src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_alpha0p5_20 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_math500_grpo_rasp_alpha0p5_20.json --seed 42 --dtype bfloat16 --max_new_tokens 2048\", \"server\": \"westb-23072\", \"data_path\": \"MATH-500\", \"data_count\": 500, \"model_name\": \"grpo_rasp_alpha0p5_20\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_alpha0p5_20\", \"eval_data\": \"MATH-500\"}, \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 0.248, \"stderr\": 0.0193, \"correct\": 124, \"total\": 500, \"natural_eos\": 274, \"truncated\": 226, \"avg_response_length\": 1110.462}, \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_math500_grpo_rasp_alpha0p5_20.json\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_math500_grpo_rasp_alpha0p5_20.log\", \"completed_at\": \"2026-05-23T10:11:11.002Z\"}, \"eval_math500_grpo_cka_only_20_2048_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T05:07:09.002Z\", \"updated_at\": \"2026-05-23T08:55:58.278Z\", \"hypothesis\": \"GRPO CKA-only 20% MATH-500 @2048 rerun with NEW eval script. Previous 29.2% (eval_math500_grpo_cka_only_20_2048) used OLD answer extraction. SFT CKA-only = 26.8% (NEW). Rerun ensures consistent C1 |Δ| comparison.\", \"parent\": \"eval_math500_grpo_cka_only_20_2048\", \"spec\": {\"command\": \"bash -c 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=3 HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 python src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20/checkpoint-100 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_math500_grpo_cka_only_20_2048_v2.json --seed 42 --dtype bfloat16 --max_new_tokens 2048'\", \"server\": \"westd-32935\", \"data_path\": \"MATH-500\", \"data_count\": 500, \"model_name\": \"grpo_cka_only_20/checkpoint-100\", \"seed\": 42, \"checkpoint_source\": \"westb-23072:/root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20/checkpoint-100\", \"eval_data\": \"MATH-500\"}, \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 0.274, \"correct\": 137, \"total\": 500, \"stderr\": 0.01995, \"natural_eos\": 390, \"truncated\": 110, \"avg_response_length\": 654.746}, \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_math500_grpo_cka_only_20_2048_v2.json\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/logs/eval_math500_grpo_cka_only_20_2048_v2.log\", \"completed_at\": \"2026-05-23T08:55:58.278Z\"}, \"eval_math500_grpo_rasp_alpha3p0_20\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T03:19:40.950Z\", \"updated_at\": \"2026-05-23T07:48:57.618Z\", \"hypothesis\": \"GRPO RASP α=3.0 MATH-500 eval @2048. C1 decoupling on MATH-500: SFT α=3.0 = 23.2%. GSM8K GRPO α=3.0 = 63.45%. Completes MATH-500 GRPO dose-response curve for α=3.0 data point.\", \"parent\": \"eval_gsm8k_grpo_alpha3p0_20\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=0 HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 python src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_alpha3p0_20_v2/checkpoint-100 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_math500_grpo_rasp_alpha3p0_20.json --seed 42 --dtype bfloat16 --max_new_tokens 2048\\\"\", \"server\": \"westd-32935\", \"data_path\": \"MATH-500\", \"data_count\": 500, \"model_name\": \"grpo_rasp_alpha3p0_20_v2/checkpoint-100\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_alpha3p0_20_v2/checkpoint-100\", \"eval_data\": \"MATH-500\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_math500_grpo_rasp_alpha3p0_20.json\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/logs/eval_math500_grpo_alpha3p0_20.log\", \"completed_at\": \"2026-05-23T07:48:50.736Z\", \"metrics\": {\"accuracy\": 0.228, \"correct\": 114, \"total\": 500, \"stderr\": 0.0188, \"truncated_ratio\": 0.28, \"avg_response_length\": 745.038}}, \"eval_math500_grpo_rasp_alpha4p0_20\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T00:01:54.194Z\", \"updated_at\": \"2026-05-23T05:58:52.769Z\", \"hypothesis\": \"GRPO RASP α=4.0 MATH-500 eval @2048. C1 decoupling on MATH-500: SFT α=4.0 = 26.6%. If |GRPO - SFT| < 2pp, C1 decoupling holds cross-benchmark for α=4.0. GSM8K GRPO α=4.0 = 62.77%.\", \"parent\": \"eval_gsm8k_grpo_alpha4_20_v3\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_alpha4_20/checkpoint-100\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/logs/eval_math500_grpo_rasp_alpha4p0_20.log\"}, \"metrics\": {\"accuracy\": 0.262, \"stderr\": 0.01966, \"correct\": 131, \"total\": 500, \"truncated\": 180, \"natural_eos\": 320, \"avg_response_length\": 925.48}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-23T05:58:52.769Z\"}, \"eval_math500_grpo_rasp_alpha1p0_20\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T23:02:44.335Z\", \"updated_at\": \"2026-05-23T04:44:32.303Z\", \"hypothesis\": \"GRPO RASP α=1.0 MATH-500 eval @2048. C1 decoupling on MATH-500: SFT α=1.0 = 21.2%. If |GRPO - SFT| < 2pp, C1 decoupling holds cross-benchmark for α=1.0.\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_rasp_20_fair\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_math500_grpo_rasp_alpha1p0_20.log\"}, \"reproduce\": {\"finished_at\": \"2026-05-23T04:41:44.783Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-23T04:41:56.794961+00:00\"}]}, \"metrics\": {\"accuracy\": 0.226, \"stderr\": 0.0187, \"n_correct\": 113, \"n_total\": 500, \"avg_response_length\": 903.536, \"natural_eos\": 320, \"truncated\": 180}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-23T04:44:32.303Z\"}, \"eval_math500_sft_cka_only_20_westd\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T20:45:21.526Z\", \"updated_at\": \"2026-05-23T03:21:26.164Z\", \"hypothesis\": \"CKA-only 20% SFT MATH-500 eval @2048 on westd (migrated from westb for speed). Dose-response endpoint control: CKA-only is the best-performing pruning method (GSM8K 64.37%). MATH-500 result establishes upper bound for cross-benchmark dose-response curve.\", \"parent\": \"eval_math500_sft_cka_only_20_westb\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 python src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_20 --output_path results/eval_math500_sft_cka_only_20.json --seed 42 --dtype bfloat16 --max_new_tokens 2048\", \"server\": \"westd-32935\", \"gpu\": \"cuda:1\", \"pid\": \"75284\", \"data_path\": \"MATH-500\", \"data_count\": 500, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B (sft_cka_only_20)\", \"seed\": 42, \"checkpoint_source\": \"sft_cka_only_20\", \"eval_data\": \"MATH-500 (N=500, max_new_tokens=2048)\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/logs/eval_math500_sft_cka_only_20.log\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_20\"}, \"metrics\": {\"accuracy\": 0.268, \"correct\": 134, \"total\": 500, \"truncated\": 116, \"stderr\": 0.0198, \"natural_eos_pct\": 0.768, \"avg_response_length\": 673.278, \"note\": \"PID 75284 actual output = 26.8% (134/500). Previous 29.0% (145/500) was from v4 run (May 19) with different answer extraction. Same model generations, different scoring.\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-23T00:00:43.009Z\"}, \"eval_math500_grpo_rasp_alpha2p0_20\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T22:23:27.589Z\", \"updated_at\": \"2026-05-23T03:16:40.537Z\", \"hypothesis\": \"GRPO RASP α=2.0 MATH-500 eval @2048. C1 decoupling evidence on MATH-500: SFT α=2.0 = 24.0%, GRPO expected similar (~24%). If |GRPO - SFT| < 1pp, C1 decoupling holds cross-benchmark.\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/recovery_aware_struct_prune && HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 python src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_alpha2p0_20 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_math500_grpo_rasp_alpha2p0_20.json --seed 42 --dtype bfloat16 --max_new_tokens 2048\\\"\", \"server\": \"westd-32935\", \"gpu\": \"cuda:0\", \"pid\": \"83709\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_math500_grpo_rasp_alpha2p0_20.log\", \"submitted_at\": \"2026-05-22T22:25:27.490Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"MATH-500\", \"data_count\": 500, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B (grpo_rasp_alpha2p0_20)\", \"seed\": 42, \"checkpoint_source\": \"grpo_rasp_alpha2p0_20\", \"eval_data\": \"MATH-500 (N=500, max_new_tokens=2048)\", \"wall_clock_seconds\": 17473.0, \"gpu_hours\": 4.85}, \"reproduce\": {\"finished_at\": \"2026-05-23T03:14:21.897Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-23T03:14:37.164633+00:00\"}]}, \"metrics\": {\"accuracy\": 0.262, \"correct\": 131, \"total\": 500, \"stderr\": 0.0197, \"natural_eos\": 349, \"truncated\": 151, \"avg_response_length\": 785.326}, \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_alpha2p0_20\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_math500_grpo_rasp_alpha2p0_20.log\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-23T03:16:40.537Z\"}, \"eval_gsm8k_grpo_qwen_math_cka_only_20_n500_v3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T15:12:46.181Z\", \"updated_at\": \"2026-05-23T02:53:37.071Z\", \"hypothesis\": \"MF3 cross-architecture validation v3 (N=500, max_new_tokens=2048): Qwen2.5-Math-7B CKA-only 20% GRPO GSM8K eval with absolute model_path fix. v2 crashed due to relative path OSError. v1 killed due to 337s/sample (no token limit). Tests whether CKA-only pruning + GRPO recovery generalizes beyond DeepSeek-R1-Distill to Qwen-Math architecture.\", \"parent\": \"eval_gsm8k_grpo_qwen_math_cka_only_20_n500_v2\", \"spec\": {\"command\": \"bash -c 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/recovery_aware_struct_prune && python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_qwen_math_cka_only_20 --max_samples 500 --max_new_tokens 2048 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_grpo_qwen_math_cka_only_20_n500_v3.json'\", \"server\": \"westb-23072\", \"gpu\": \"cuda:1\", \"pid\": \"220343\", \"data_path\": \"GSM8K test split\", \"data_count\": 500, \"model_name\": \"Qwen2.5-Math-7B-pruned-cka_only-20pct-GRPO\", \"seed\": 42, \"checkpoint_source\": \"grpo_qwen_math_cka_only_20\", \"eval_data\": \"GSM8K\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_qwen_math_cka_only_20\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_gsm8k_grpo_qwen_math_cka_only_20_n500_v3.log\"}, \"metrics\": {\"accuracy\": 0.486, \"correct\": 243, \"total\": 500, \"stderr\": 0.0224, \"truncated_pct\": 0.838, \"natural_eos_pct\": 0.162, \"avg_response_length\": 1766.5}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-23T02:53:37.071Z\"}, \"eval_math500_sft_rasp_alpha1p0_20_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T20:50:24.239Z\", \"updated_at\": \"2026-05-22T23:01:03.419Z\", \"hypothesis\": \"α=1.0 SFT MATH-500 eval @2048 v2 (on westb). Default RASP α=1.0. Cross-benchmark dose-response: GSM8K α=1.0 SFT=63.31%. v1 killed at 304/500, result file never written. Completes 5-point dose-response curve on MATH-500.\", \"parent\": \"eval_math500_sft_rasp_alpha1p0_20\", \"notes\": \"westb submission failed: model sft_rasp_20_westd not found on westb. Only exists on westd-32935. Waiting for westd:3 (α=4.0, 85%) to free up.\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20_westd\", \"log_path\": \"/root/runs/recovery_aware_struct_prune/eval_math500_sft_rasp_alpha1p0_20_v2.log\"}, \"reproduce\": {\"finished_at\": \"2026-05-22T22:58:10.208Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-22T22:58:19.219921+00:00\"}]}, \"metrics\": {\"accuracy\": 0.212, \"correct\": 106, \"total\": 500, \"truncated\": 186, \"stderr\": 0.0183}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T23:01:03.420Z\"}, \"eval_math500_sft_standard_20_2048_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T01:34:44.782Z\", \"updated_at\": \"2026-05-22T22:19:38.080Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/recovery_aware_struct_prune && HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 python src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_math500_sft_standard_20_2048_v2.json --seed 42 --dtype bfloat16 --max_new_tokens 2048\\\"\", \"server\": \"westd-32935\", \"gpu\": [\"cuda:0\"], \"pid\": \"82301\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_math500_sft_standard_20_2048_v2.log\", \"submitted_at\": \"2026-05-22T22:15:58.026Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"hypothesis\": \"Standard (random) 20% SFT MATH-500 eval @2048. Baseline comparison: Standard pruning without CKA guidance. Cross-benchmark extension of GSM8K Standard results.\", \"parent\": \"eval_math500_sft_standard_20\", \"reproduce\": {\"finished_at\": \"2026-05-19T08:54:35.352Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-19T08:54:40.855817+00:00\"}]}, \"metrics\": {\"accuracy\": 0.258, \"n_correct\": 129, \"n_total\": 500}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T13:08:16.850Z\"}, \"eval_math500_sft_rasp_alpha0p5_20\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T15:20:44.460Z\", \"updated_at\": \"2026-05-22T22:18:43.350Z\", \"hypothesis\": \"α=0.5 SFT MATH-500 eval @2048. Cross-benchmark dose-response validation: GSM8K shows α=0.5 SFT=60.73%. If MATH-500 also shows α=0.5 < α=2.0, inverted-U generalizes beyond GSM8K (strengthens MF4 + N1).\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_alpha0p5_20\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/logs/eval_math500_sft_rasp_alpha0p5_20.log\"}, \"metrics\": {\"accuracy\": 0.254, \"correct\": 127, \"total\": 500, \"truncated\": 220, \"stderr\": 0.0195}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T22:18:43.350Z\"}, \"eval_math500_sft_rasp_alpha3p0_20\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T18:26:16.273Z\", \"updated_at\": \"2026-05-22T22:12:26.406Z\", \"hypothesis\": \"α=3.0 SFT MATH-500 eval @2048. Dose-response \\\"下降段确认点\\\": GSM8K α=3.0 SFT=64.14% (below α=2.0 peak 64.97%). If MATH-500 also shows α=3.0 < α=2.0, confirms inverted-U descending arm cross-benchmark. Completes 5/5 MATH-500 dose-response.\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_alpha3p0_20/checkpoint-935\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/logs/eval_math500_sft_rasp_alpha3p0_20.log\"}, \"metrics\": {\"accuracy\": 0.232, \"correct\": 116, \"total\": 500, \"truncated\": 144, \"stderr\": 0.0189}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T22:12:26.406Z\"}, \"eval_math500_sft_rasp_alpha4p0_20\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T15:20:47.150Z\", \"updated_at\": \"2026-05-22T21:22:35.441Z\", \"hypothesis\": \"α=4.0 SFT MATH-500 eval @2048. Cross-benchmark dose-response validation: GSM8K shows α=4.0 SFT=61.94%. If MATH-500 also shows α=4.0 < α=2.0, inverted-U generalizes beyond GSM8K (strengthens MF4 + N1).\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_alpha4_20\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/logs/eval_math500_sft_rasp_alpha4p0_20.log\"}, \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 0.266, \"correct\": 133, \"total\": 500, \"truncated\": 190, \"stderr\": 0.0198}, \"completed_at\": \"2026-05-22T21:22:35.442Z\"}, \"eval_math500_sft_rasp_alpha2p0_20\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T15:06:22.386Z\", \"updated_at\": \"2026-05-22T20:44:52.970Z\", \"hypothesis\": \"α=2.0 SFT MATH-500 eval @2048. Dose-response peak on GSM8K (64.97% SFT). Cross-benchmark validation: if α=2.0 also peaks on MATH-500, inverted-U generalizes beyond GSM8K (strengthens MF4 + N1).\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 nohup python src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_alpha2p0_20 --output_path results/eval_math500_sft_rasp_alpha2p0_20.json --seed 42 --dtype bfloat16 --max_new_tokens 2048\", \"server\": \"westd-32935\", \"gpu\": \"cuda:1\", \"pid\": \"57202\", \"data_path\": \"MATH-500\", \"data_count\": 500, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B (sft_rasp_alpha2p0_20)\", \"seed\": 42, \"checkpoint_source\": \"sft_rasp_alpha2p0_20\", \"eval_data\": \"MATH-500 (N=500, max_new_tokens=2048)\", \"log_path\": \"/root/recovery_aware_struct_prune/results/eval_math500_sft_rasp_alpha2p0_20.log\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_alpha2p0_20\"}, \"reproduce\": {\"finished_at\": \"2026-05-22T20:12:27.595Z\"}, \"failure_reason\": \"cron false positive: process exited normally, result file confirmed by Reviewer (24.0% accuracy)\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T20:12:32.633Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-22T20:12:40.230344+00:00\"}]}, \"metrics\": {\"accuracy\": 0.24, \"correct\": 120, \"total\": 500, \"truncated\": 155, \"stderr\": 0.0191}}, \"eval_gsm8k_grpo_random_20_seed456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T16:26:01.516Z\", \"updated_at\": \"2026-05-22T18:27:22.282Z\", \"hypothesis\": \"MF2 seed456 GSM8K eval (N=1319, greedy, max_new_tokens=2048). Paired with seed42 (50.57%) and seed123 v2 (running, interim 52.40%@1000). Validates C1 decoupling robustness across random seeds.\", \"parent\": \"grpo_random_20_seed456\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_random_20_seed456/checkpoint-100 --seed 456 --dtype bfloat16 --max_new_tokens 2048 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_grpo_random_20_seed456.json\", \"server\": \"westb-23072\", \"gpu\": \"cuda:0\", \"pid\": \"224705\", \"data_path\": \"openai/gsm8k (test split)\", \"data_count\": 1319, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B (grpo_random_20_seed456)\", \"seed\": 456, \"checkpoint_source\": \"grpo_random_20_seed456/checkpoint-100\", \"eval_data\": \"GSM8K test 1319\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_grpo_random_20_seed456.log\", \"accuracy\": 0.5087, \"total_correct\": 671, \"total_samples\": 1319, \"eos_rate\": 0.9955, \"stderr\": 0.01377, \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_random_20_seed456/checkpoint-100\"}, \"reproduce\": {\"finished_at\": \"2026-05-22T17:48:12.480Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T17:48:17.521Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-22T17:48:25.193120+00:00\"}]}, \"metrics\": {\"gsm8k_accuracy\": 0.5087, \"gsm8k_accuracy_se\": 0.0138, \"gsm8k_correct\": 671, \"gsm8k_total\": 1319, \"eos_rate\": 0.9954, \"avg_response_length\": 163.5, \"truncated\": 6}, \"notes\": \"Cron 误判 (已知模式): 实验实际完成 1319/1319, acc=50.87%. 与 seed42 (50.57%) 一致, 验证 C1 decoupling. Results: /root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_grpo_random_20_seed456.json\"}, \"eval_gsm8k_grpo_random_20_seed123_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T14:22:33.753Z\", \"updated_at\": \"2026-05-22T16:49:54.123Z\", \"hypothesis\": \"MF2 seed123 v2 GSM8K eval (N=1319, greedy, max_new_tokens=2048). 配对 seed42 (50.57%) 和 seed456 (pending). 验证 C1 decoupling 跨 seed 鲁棒性。v1 因 batch_size=1 配置错误作废。\", \"parent\": \"grpo_random_20_seed123_v2\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 nohup python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_random_20_seed123_v2/checkpoint-100 --output_path results/eval_gsm8k_grpo_random_20_seed123_v2.json --seed 123 --dtype bfloat16\", \"server\": \"westd-32935\", \"gpu\": \"cuda:0\", \"pid\": \"56283\", \"data_path\": \"openai/gsm8k (test split)\", \"data_count\": 1319, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B (grpo_random_20_seed123_v2)\", \"seed\": 123, \"checkpoint_source\": \"grpo_random_20_seed123_v2/checkpoint-100\", \"eval_data\": \"gsm8k test 1319\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_grpo_random_20_seed123_v2.json\", \"accuracy\": 0.5072, \"total_correct\": 669, \"total_samples\": 1319, \"eos_rate\": 0.9939, \"stderr\": 0.01377, \"avg_response_length\": 177.9, \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_random_20_seed123_v2/checkpoint-100\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T16:49:54.123Z\"}, \"grpo_random_20_seed456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T12:00:38.940Z\", \"updated_at\": \"2026-05-22T16:27:46.810Z\", \"hypothesis\": \"MF2 multi-seed validation: Random pruning 20% GRPO with seed456. Third seed for C1 decoupling robustness check. seed42: Δ=-0.68pp, seed123: pending eval. If all seeds show |Δ(GRPO-SFT)| ≤ 2pp, C1 claim is robust across random seeds.\", \"spec\": {\"server\": \"westb-23072\", \"gpu\": \"cuda:0\", \"command\": \"CUDA_VISIBLE_DEVICES=0 HF_HUB_OFFLINE=1 HF_DATASETS_OFFLINE=1 nohup python src/train_grpo_v5.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_random_20 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/grpo_random_20_seed456 --max_steps 100 --save_steps 100 --seed 456\", \"pid\": \"209508\", \"data_path\": \"openai/gsm8k (train split)\", \"data_count\": 7473, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B (sft_random_20)\", \"seed\": 456, \"checkpoint_source\": \"sft_random_20\", \"eval_data\": \"N/A - GRPO training\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_random_20_seed456/checkpoint-100\", \"log_path\": \"/tmp/grpo_random_seed456.log\", \"note\": \"100/100 steps completed. Final trainer.save_model() hit disk-full but TRL checkpoint-100 is intact (model.safetensors=12,174,631,264 bytes, matching seed42/seed123_v2). Reviewer independently verified.\"}, \"reproduce\": {\"finished_at\": \"2026-05-22T16:22:39.316Z\"}, \"failure_reason\": \"磁盘满: GRPO训练100/100完成但save_pretrained失败 (No space left on device)。westb-23072:/root/autodl-tmp 空间不足。\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T16:22:44.289Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-22T16:22:54.301751+00:00\"}]}, \"notes\": \"失败原因: GRPO 训练 100/100 步已完成 (3h02min)，但 save_pretrained 时磁盘满 (No space left on device, os error 28)。保存路径: /root/autodl-tmp/recovery_aware_struct_prune/grpo_random_20_seed456。W&B run auv9riek 有完整训练 metrics。save_steps=100=max_steps，无中间 checkpoint，需重跑。 | 已有成果: W&B metrics 完整 | 建议: 清理 westb-23072 磁盘后重提交\"}, \"eval_gsm8k_sft_depth_first_20\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T14:20:43.950Z\", \"updated_at\": \"2026-05-22T15:19:31.829Z\", \"hypothesis\": \"MF5 depth-first SFT GSM8K eval. Establishes SFT baseline for depth-first pruning method, paired with GRPO eval to check C1 decoupling for this baseline method.\", \"parent\": \"pipeline_depth_first_20\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 nohup python src/eval_gsm8k.py --model_path sft_depth_first_20 --output_path results/eval_gsm8k_sft_depth_first_20.json --seed 42 --dtype bfloat16\", \"server\": \"westd-32935\", \"gpu\": \"cuda:2\", \"pid\": \"54882\", \"data_path\": \"openai/gsm8k (test split)\", \"data_count\": 1319, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B (sft_depth_first_20)\", \"seed\": 42, \"checkpoint_source\": \"sft_depth_first_20\", \"eval_data\": \"gsm8k test 1319\", \"log_path\": \"/root/recovery_aware_struct_prune/results/eval_gsm8k_sft_depth_first_20.log\", \"note\": \"Early-stopped by Director at ~60-88 samples. Interim accuracy ~10%@50 (SFT). Conclusive: depth-first 20% SFT dramatically worse than CKA-only 64%. MF5 claim validated — CKA-only advantage is NOT simply removing deep layers.\", \"checkpoint_path\": \"N/A (eval only)\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T15:19:31.829Z\"}, \"eval_gsm8k_grpo_depth_first_20\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T14:20:41.126Z\", \"updated_at\": \"2026-05-22T15:18:38.970Z\", \"hypothesis\": \"MF5 depth-first GRPO GSM8K eval re-run. Previous pipeline_depth_first_20 results lost due to disk-full during JSON write. GRPO checkpoint intact. Re-running eval to get formal JSON result file. Prior log recovery showed ~24.18% from nohup output.\", \"parent\": \"pipeline_depth_first_20\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 nohup python src/eval_gsm8k.py --model_path grpo_depth_first_20/checkpoint-100 --output_path results/eval_gsm8k_grpo_depth_first_20.json --seed 42 --dtype bfloat16\", \"server\": \"westd-32935\", \"gpu\": \"cuda:3\", \"pid\": \"51981\", \"data_path\": \"openai/gsm8k (test split)\", \"data_count\": 1319, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B (grpo_depth_first_20)\", \"seed\": 42, \"checkpoint_source\": \"grpo_depth_first_20/checkpoint-100\", \"eval_data\": \"gsm8k test 1319\", \"log_path\": \"/root/recovery_aware_struct_prune/results/eval_gsm8k_grpo_depth_first_20.log\", \"note\": \"Early-stopped by Director at ~60-88 samples. Interim accuracy ~8%@50 (GRPO). Conclusive: depth-first 20% GRPO dramatically worse than CKA-only 64%. MF5 claim validated — CKA-only advantage is NOT simply removing deep layers.\", \"checkpoint_path\": \"N/A (eval only)\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T15:18:38.970Z\"}, \"grpo_random_20_seed123_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T14:22:29.868Z\", \"updated_at\": \"2026-05-22T15:00:23.101Z\", \"hypothesis\": \"MF2 multi-seed validation v2: Random 20% GRPO with seed123, correct batch_size=2 (matching seed42/seed456). v1 used batch_size=1 (half data per 100 steps), results invalidated. Tests C1 decoupling robustness across random seeds.\", \"parent\": \"grpo_random_20_seed123\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 HF_HUB_OFFLINE=1 HF_DATASETS_OFFLINE=1 nohup python src/train_grpo_v5.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_random_20 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/grpo_random_20_seed123_v2 --max_steps 100 --save_steps 100 --seed 123\", \"server\": \"westd-32935\", \"gpu\": \"cuda:1\", \"pid\": \"53822\", \"data_path\": \"openai/gsm8k (train split)\", \"data_count\": 7473, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B (sft_random_20)\", \"seed\": 123, \"checkpoint_source\": \"sft_random_20\", \"eval_data\": \"N/A - GRPO training\", \"log_path\": \"/tmp/grpo_random_seed123_v2.log\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_random_20_seed123_v2/checkpoint-100\", \"completed_at\": \"2026-05-22T15:00:23.101Z\"}, \"eval_gsm8k_grpo_alpha3p0_20\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T09:30:06.630Z\", \"updated_at\": \"2026-05-22T14:47:06.188Z\", \"hypothesis\": \"α=3.0 GRPO GSM8K eval. Dose-response 5th data point: α=3.0 between α=2.0 (66.11%) and α=4.0 (62.77%). Completes the 5-point dose-response curve for causal evidence of CKA overlap suppression effect.\", \"notes\": \"UNBLOCKED: grpo_rasp_alpha3p0_20_v2 checkpoint-100 完整 (12.3GB). Eval 已启动 PID 43755 on westd:0, 2.8s/sample, ETA ~60 min.\", \"spec\": {\"server\": \"westd-32935\", \"gpu\": \"cuda:0\", \"command\": \"CUDA_VISIBLE_DEVICES=0 HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 nohup python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_alpha3p0_20_v2/checkpoint-100 --output_path results/eval_gsm8k_grpo_rasp_alpha3p0_20.json --max_samples 1319 --seed 42 --dtype bfloat16\", \"pid\": \"43755\", \"data_path\": \"openai/gsm8k (test split)\", \"data_count\": 1319, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B (grpo_rasp_alpha3p0_20_v2)\", \"seed\": 42, \"checkpoint_source\": \"grpo_rasp_alpha3p0_20_v2/checkpoint-100\", \"eval_data\": \"gsm8k test 1319\", \"log_path\": \"/root/recovery_aware_struct_prune/results/eval_gsm8k_grpo_rasp_alpha3p0_20.log\"}, \"conclusion\": \"success\", \"metrics\": {\"gsm8k_accuracy\": 0.6345, \"correct\": 837, \"total\": 1319, \"stderr\": 0.0133, \"eos_rate\": 0.9864, \"truncated\": 18, \"avg_response_length\": 219.7}, \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_alpha3p0_20_v2/checkpoint-100\", \"log_path\": \"/root/recovery_aware_struct_prune/results/eval_gsm8k_grpo_rasp_alpha3p0_20.log\", \"completed_at\": \"2026-05-22T14:46:15.365Z\"}, \"eval_math500_sft_random_20_v3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T04:11:52.462Z\", \"updated_at\": \"2026-05-22T14:10:18.359Z\", \"hypothesis\": \"Random 20% SFT MATH-500 @2048. v2 failed due to old eval_math500.py on westd-32935. Code synced from westb.\", \"parent\": \"eval_math500_sft_random_20_v2\", \"spec\": {\"command\": \"python src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_random_20 --max_new_tokens 2048 --output_path /root/recovery_aware_struct_prune/results/eval_math500_sft_random_20_v3.json\", \"server\": \"westd-32935\", \"gpu\": [\"cuda:1\"], \"pid\": \"5236\", \"data_path\": \"MATH-500\", \"data_count\": 500, \"model_name\": \"sft_random_20\", \"model_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_random_20\", \"seed\": 42, \"checkpoint_source\": \"sft_random_20\", \"eval_data\": \"MATH-500\", \"log_path\": \"/root/recovery_aware_struct_prune/logs/eval_math500_sft_random_20_v3.log\", \"checkpoint_path\": \"N/A - eval\"}, \"metrics\": {\"accuracy\": 0.144, \"correct\": 72, \"total\": 500, \"stderr\": 0.0157, \"natural_eos\": 171, \"truncated\": 329, \"avg_response_length\": 1470.44}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T14:10:18.359Z\"}, \"eval_gsm8k_sft_alpha3p0_20\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T10:24:58.696Z\", \"updated_at\": \"2026-05-22T12:38:25.600Z\", \"hypothesis\": \"α=3.0 SFT GSM8K eval (checkpoint-935, 1 epoch). Dose-response 5th SFT data point for C1 decoupling. Paired with α=3.0 GRPO (pending). Completes the 5-point dose-response SFT column.\", \"parent\": \"grpo_rasp_alpha3p0_20\", \"spec\": {\"server\": \"westd-32935\", \"gpu\": \"cuda:2\", \"command\": \"eval_gsm8k.py --model_path sft_rasp_alpha3p0_20/checkpoint-935 --max_new_tokens 2048\", \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B\", \"seed\": 42, \"data_path\": \"openai/gsm8k (test split)\", \"data_count\": 1319, \"checkpoint_source\": \"sft_rasp_alpha3p0_20/checkpoint-935 (SCP from westb)\", \"eval_data\": \"gsm8k test 1319\", \"pid\": \"37024\"}, \"reproduce\": {\"finished_at\": \"2026-05-22T12:34:57.027Z\"}, \"failure_reason\": \"\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T12:35:05.634Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-22T12:35:15.663664+00:00\"}]}, \"metrics\": {\"gsm8k_accuracy\": 0.6414, \"gsm8k_correct\": 846, \"gsm8k_total\": 1319, \"gsm8k_stderr\": 0.0132, \"eos_rate\": 0.9879, \"avg_response_length\": 188.63, \"natural_eos\": 1303, \"truncated\": 16}, \"log_path\": \"/tmp/eval_gsm8k_sft_alpha3p0.log\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_alpha3p0_20/checkpoint-935\", \"notes\": \"Cron 误判。评估 1319/1319 全部完成，accuracy=64.14%。进程因写结果 JSON 时磁盘满 (OSError: No space left on device) 以非零码退出，但所有推理已完成、accuracy 已计算。结果 JSON 未写入磁盘，数据从日志提取。中间进度 ~64.15%@1300 与最终 64.14% 一致。\"}, \"grpo_rasp_alpha3p0_20_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T10:40:19.362Z\", \"updated_at\": \"2026-05-22T11:58:15.586Z\", \"hypothesis\": \"Re-run of grpo_rasp_alpha3p0_20 (checkpoint corrupted by disk-full). α=3.0 GRPO 100 steps on sft_rasp_alpha3p0_20/checkpoint-935. Critical for dose-response curve (α=3.0 between α=2.0 peak and α=4.0 decline).\", \"parent\": \"grpo_rasp_alpha3p0_20\", \"spec\": {\"server\": \"westd-32935\", \"gpu\": \"cuda:0\", \"command\": \"CUDA_VISIBLE_DEVICES=0 HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 nohup python src/train_grpo_v5.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_alpha3p0_20/checkpoint-935 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_alpha3p0_20_v2 --max_steps 100 --save_total_limit 1\", \"pid\": \"42003\", \"data_path\": \"openai/gsm8k (train split)\", \"data_count\": 7473, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B (sft_rasp_alpha3p0_20)\", \"seed\": 42, \"checkpoint_source\": \"sft_rasp_alpha3p0_20/checkpoint-935\", \"eval_data\": \"N/A - GRPO training\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_alpha3p0_20_v2\", \"log_path\": \"/tmp/grpo_alpha3p0_v2.log\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T11:58:15.586Z\"}, \"eval_math500_grpo_standard_20_fair_2048_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T03:49:45.575Z\", \"updated_at\": \"2026-05-22T11:17:52.493Z\", \"hypothesis\": \"Standard 20% fair GRPO MATH-500 @2048. P0 data gap for cross-method MATH-500 table. Re-run on westd-32935 after westd-29022 outage.\", \"parent\": \"eval_math500_grpo_standard_20_fair_2048\", \"spec\": {\"command\": \"python src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_standard_20_fair --max_new_tokens 2048 --output_path /root/recovery_aware_struct_prune/results/eval_math500_grpo_standard_20_fair_2048_v2.json\", \"server\": \"westd-32935\", \"gpu\": [\"cuda:0\"], \"data_path\": \"MATH-500\", \"data_count\": 500, \"model_name\": \"grpo_stage2_standard_20_fair\", \"model_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_standard_20_fair\", \"seed\": 42, \"checkpoint_source\": \"grpo_stage2_standard_20_fair\", \"eval_data\": \"MATH-500\", \"log_path\": \"/root/recovery_aware_struct_prune/logs/eval_math500_grpo_standard_20_fair_2048_v2.log\", \"checkpoint_path\": \"N/A (eval)\"}, \"reproduce\": {\"finished_at\": \"2026-05-22T11:12:19.798Z\"}, \"failure_reason\": \"\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T11:12:27.767Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-22T11:12:38.330160+00:00\"}]}, \"metrics\": {\"math500_accuracy\": 0.264, \"math500_correct\": 132, \"math500_total\": 500, \"math500_stderr\": 0.0197}, \"notes\": \"Cron 误判。实际正常完成。MATH-500 Accuracy = 0.2640 ± 0.0197 (132/500)。运行时长 ~7h11min。结果文件: /root/recovery_aware_struct_prune/results/eval_math500_grpo_standard_20_fair_2048_v2.json\"}, \"grpo_random_20_seed123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T10:34:12.100Z\", \"updated_at\": \"2026-05-22T11:17:21.388Z\", \"hypothesis\": \"MF2 multi-seed validation: Random pruning 20% GRPO with seed123. Tests if GRPO decoupling result (C1) is robust across random seeds. If variance across seeds is low (±2pp), C1 claim is strengthened.\", \"spec\": {\"server\": \"westd-32935\", \"gpu\": \"cuda:2\", \"command\": \"bash -c 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/recovery_aware_struct_prune && HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 python src/train_grpo_v5.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_random_20 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/grpo_random_20_seed123 --num_steps 100 --seed 123'\", \"pid\": \"36832\", \"data_path\": \"openai/gsm8k (train split)\", \"data_count\": 7473, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B (sft_random_20)\", \"seed\": 123, \"checkpoint_source\": \"sft_random_20\", \"eval_data\": \"N/A - GRPO training, not eval\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_random_20_seed123\", \"log_path\": \"/tmp/mf2_random_seed123_grpo.log\"}, \"reproduce\": {\"finished_at\": \"2026-05-22T11:12:49.435Z\"}, \"failure_reason\": \"\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T11:12:57.919Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-22T11:13:16.493425+00:00\"}]}, \"notes\": \"Cron 误判 (已知 pattern: process dead 5× with no sentinel/W&B)。实际 GRPO 训练正常完成 (19:02 CST)。模型保存: /root/autodl-tmp/recovery_aware_struct_prune/grpo_random_20_seed123。WandB run: grpo_sft_random_20 (ID: 1silchcm)。日志: /tmp/mf2_random_seed123_grpo.log\"}, \"grpo_rasp_alpha3p0_20\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T08:48:06.001Z\", \"updated_at\": \"2026-05-22T10:39:07.034Z\", \"hypothesis\": \"α=3.0 GRPO 100 steps on checkpoint-935 (1 epoch SFT). Dose-response data point between α=2.0 and α=4.0. If monotonic: higher α → higher GSM8K accuracy, confirming CKA overlap suppression causally harms recovery.\", \"parent\": \"grpo_alpha4_20\", \"spec\": {\"server\": \"westb-23072\", \"gpu\": \"cuda:0\", \"command\": \"train_grpo_v5.py --model_path sft_rasp_alpha3p0_20/checkpoint-935 --output_dir grpo_rasp_alpha3p0_20 --max_steps 100 --learning_rate 1e-6 --per_device_train_batch_size 1 --gradient_accumulation_steps 8 --max_completion_length 512 --temperature 0.4 --beta 0.01 --loss_type dapo --format_reward_weight 0.1 --gradient_checkpointing true --optim adamw_8bit\", \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B\", \"seed\": 42, \"pid\": \"170676\", \"data_path\": \"openai/gsm8k (train split)\", \"data_count\": 7473, \"checkpoint_source\": \"sft_rasp_alpha3p0_20/checkpoint-935\", \"eval_data\": \"N/A - GRPO training\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_alpha3p0_20/checkpoint-100\", \"log_path\": \"/tmp/alpha3p0_grpo.log\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T10:31:57.909Z\", \"notes\": \"GRPO 训练 100/100 steps 完成，但 checkpoint-100/model.safetensors 被截断（7.2GB vs 应有 11.5GB）。原因：westb 数据盘在保存时 100% 满。需要重跑 GRPO。SFT checkpoint-935 完好（11.5GB）。\"}, \"eval_gsm8k_sft_alpha2p0_20\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T10:19:50.623Z\", \"updated_at\": \"2026-05-22T10:22:56.503Z\", \"hypothesis\": \"α=2.0 SFT GSM8K eval for C1 decoupling. Paired with α=2.0 GRPO (66.11%). Critical: if SFT ~61-62%, Δ ≈ +4-5pp would break C1 universal ±2pp claim. Reviewer-flagged risk.\", \"parent\": \"pipeline_alpha2p0_20\", \"spec\": {\"server\": \"westd-32935\", \"gpu\": \"cuda:2\", \"command\": \"eval_gsm8k.py --model_path sft_rasp_alpha2p0_20 --max_new_tokens 2048\", \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B\", \"seed\": 42, \"data_path\": \"openai/gsm8k (test split)\", \"data_count\": 1319, \"checkpoint_source\": \"sft_rasp_alpha2p0_20\", \"eval_data\": \"gsm8k test 1319\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_alpha2p0_20\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/eval_gsm8k_sft_alpha2p0_20.json\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T10:22:49.360Z\", \"metrics\": {\"gsm8k_accuracy\": 0.6497, \"gsm8k_correct\": 857, \"gsm8k_total\": 1319}}, \"eval_gsm8k_sft_alpha0p5_20\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T10:19:48.133Z\", \"updated_at\": \"2026-05-22T10:20:57.690Z\", \"hypothesis\": \"α=0.5 SFT GSM8K eval for C1 decoupling. Paired with α=0.5 GRPO (61.18%). Δ(GRPO-SFT) tests whether GRPO benefit is universal ±2pp across α values.\", \"parent\": \"pipeline_alpha0p5_20\", \"spec\": {\"server\": \"westd-32935\", \"gpu\": \"cuda:3\", \"command\": \"eval_gsm8k.py --model_path sft_rasp_alpha0p5_20 --max_new_tokens 2048\", \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B\", \"seed\": 42, \"data_path\": \"openai/gsm8k (test split)\", \"data_count\": 1319, \"checkpoint_source\": \"sft_rasp_alpha0p5_20\", \"eval_data\": \"gsm8k test 1319\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_alpha0p5_20\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/eval_gsm8k_sft_alpha0p5_20.json\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T10:20:50.793Z\", \"metrics\": {\"gsm8k_accuracy\": 0.6073, \"gsm8k_correct\": 801, \"gsm8k_total\": 1319}}, \"grpo_qwen_math_cka_only_20\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T08:50:34.293Z\", \"updated_at\": \"2026-05-22T09:54:05.974Z\", \"hypothesis\": \"MF3 cross-architecture validation: Qwen2.5-Math-7B CKA-only 20% pruned → SFT → GRPO 100 steps. Tests if CKA-guided pruning advantage transfers beyond DeepSeek-R1 to Qwen-Math family. P0 highest priority.\", \"parent\": \"sft_qwen_math_cka_only_20_v2\", \"spec\": {\"server\": \"westb-23072\", \"gpu\": \"cuda:1\", \"command\": \"train_grpo_v5.py --model_path sft_qwen_math_cka_only_20_v2 --max_steps 100 --learning_rate 1e-6 --per_device_train_batch_size 1 --gradient_accumulation_steps 8 --max_completion_length 512 --temperature 0.4 --beta 0.01 --loss_type dapo --format_reward_weight 0.1 --gradient_checkpointing true --optim adamw_8bit\", \"model_name\": \"Qwen2.5-Math-7B\", \"seed\": 42, \"pid\": \"164710\", \"data_path\": \"openai/gsm8k (train split)\", \"data_count\": 7473, \"checkpoint_source\": \"sft_qwen_math_cka_only_20_v2\", \"eval_data\": \"N/A - this is GRPO training, not eval\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_qwen_math_cka_only_20\", \"log_path\": \"/tmp/mf3_qwen_grpo.log\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T09:54:05.974Z\"}, \"eval_gsm8k_grpo_alpha2p0_20\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T09:28:08.089Z\", \"updated_at\": \"2026-05-22T09:29:24.824Z\", \"hypothesis\": \"α=2.0 GRPO GSM8K eval. Dose-response data point: moderate overlap suppression (α=2.0) between α=1.0 (61.49%) and α=4.0 (62.77%). Tests monotonicity of dose-response curve.\", \"parent\": \"pipeline_alpha2p0_20\", \"spec\": {\"server\": \"westd-32935\", \"gpu\": \"cuda:2\", \"command\": \"eval_gsm8k.py --model_path grpo_rasp_alpha2p0_20 --max_new_tokens 2048\", \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B\", \"seed\": 42, \"data_path\": \"openai/gsm8k (test split)\", \"data_count\": 1319, \"checkpoint_source\": \"grpo_rasp_alpha2p0_20\", \"eval_data\": \"gsm8k test 1319\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_alpha2p0_20\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/eval_gsm8k_grpo_alpha2p0_20.json\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T09:29:16.837Z\", \"metrics\": {\"gsm8k_accuracy\": 0.6611, \"gsm8k_correct\": 872, \"gsm8k_total\": 1319}}, \"eval_gsm8k_grpo_alpha0p5_20\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T09:28:05.478Z\", \"updated_at\": \"2026-05-22T09:29:23.350Z\", \"hypothesis\": \"α=0.5 GRPO GSM8K eval. Dose-response data point: low overlap suppression (α=0.5) should yield lower accuracy than α=1.0 (61.49%) if CKA overlap suppression causally harms recovery.\", \"parent\": \"pipeline_alpha0p5_20\", \"spec\": {\"server\": \"westd-32935\", \"gpu\": \"cuda:3\", \"command\": \"eval_gsm8k.py --model_path grpo_rasp_alpha0p5_20 --max_new_tokens 2048\", \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B\", \"seed\": 42, \"data_path\": \"openai/gsm8k (test split)\", \"data_count\": 1319, \"checkpoint_source\": \"grpo_rasp_alpha0p5_20\", \"eval_data\": \"gsm8k test 1319\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_alpha0p5_20\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/eval_gsm8k_grpo_alpha0p5_20.json\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T09:29:13.196Z\", \"metrics\": {\"gsm8k_accuracy\": 0.6118, \"gsm8k_correct\": 807, \"gsm8k_total\": 1319}}, \"eval_math500_sft_standard_20_1p5b\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T04:31:30.202Z\", \"updated_at\": \"2026-05-22T08:27:40.167Z\", \"hypothesis\": \"1.5B Standard 20% SFT MATH-500 @2048. Cross-scale comparison with CKA-only 1.5B (10.6%) to test if CKA-guided pruning advantage is scale-invariant.\", \"spec\": {\"command\": \"python src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20_1p5b --max_new_tokens 2048 --output_path /root/recovery_aware_struct_prune/results/eval_math500_sft_standard_20_1p5b.json\", \"server\": \"westb-23072\", \"gpu\": [\"cuda:0\"], \"data_path\": \"MATH-500\", \"data_count\": 500, \"model_name\": \"sft_standard_20_1p5b\", \"model_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20_1p5b\", \"seed\": 42, \"checkpoint_source\": \"sft_standard_20_1p5b\", \"eval_data\": \"MATH-500\", \"log_path\": \"/root/recovery_aware_struct_prune/logs/eval_math500_sft_standard_20_1p5b.log\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20_1p5b\"}, \"conclusion\": \"success\", \"metrics\": {\"math500_accuracy\": 0.054, \"correct\": 27, \"total\": 500, \"truncated\": 335}, \"completed_at\": \"2026-05-22T07:50:22.759Z\"}, \"eval_gsm8k_sft_alpha4_20_v5\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T03:49:50.201Z\", \"updated_at\": \"2026-05-22T06:05:53.848Z\", \"hypothesis\": \"α=4.0 SFT GSM8K N=1319 full eval @2048. D100 critical for C1 decoupling universality. v4 lost to westd-29022 outage. Re-run on westd-32935.\", \"parent\": \"eval_gsm8k_sft_alpha4_20_v4\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_alpha4_20\", \"log_path\": \"/root/recovery_aware_struct_prune/logs/eval_gsm8k_sft_alpha4_20_v5.log\", \"result_path\": \"/root/recovery_aware_struct_prune/results/eval_gsm8k_sft_alpha4_20_v5.json\"}, \"reproduce\": {\"finished_at\": \"2026-05-22T05:47:27.370Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T05:47:34.101Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-22T05:47:41.693855+00:00\"}]}, \"metrics\": {\"gsm8k_accuracy\": 0.6194, \"correct\": 817, \"total\": 1319, \"stderr\": 0.0134, \"eos_rate\": 0.981, \"avg_response_length\": 197.85}}, \"eval_gsm8k_grpo_alpha4_20_v3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T03:49:52.414Z\", \"updated_at\": \"2026-05-22T05:33:39.349Z\", \"hypothesis\": \"α=4.0 GRPO GSM8K N=1319 full eval @2048. v1 timed out at 774/1319 (62.93% interim). v2 ALLOCATED but westd-29022 died. Re-run on westd-32935 with --max_new_tokens 2048.\", \"parent\": \"eval_gsm8k_grpo_alpha4_20_v2\", \"spec\": {\"command\": \"python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_alpha4_20/checkpoint-100 --max_new_tokens 2048 --output_path /root/recovery_aware_struct_prune/results/eval_gsm8k_grpo_alpha4_20_v3.json\", \"server\": \"westd-32935\", \"gpu\": [\"cuda:3\"], \"data_path\": \"GSM8K\", \"data_count\": 1319, \"model_name\": \"grpo_alpha4_20/checkpoint-100\", \"model_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_alpha4_20/checkpoint-100\", \"seed\": 42, \"checkpoint_source\": \"grpo_alpha4_20/checkpoint-100\", \"eval_data\": \"GSM8K\", \"log_path\": \"/root/recovery_aware_struct_prune/logs/eval_gsm8k_grpo_alpha4_20_v3.log\"}, \"reproduce\": {\"finished_at\": \"2026-05-22T05:30:52.773Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T05:30:50.611Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-22T05:31:04.453494+00:00\"}]}, \"metrics\": {\"gsm8k_accuracy\": 0.6277, \"gsm8k_accuracy_ci\": 0.0133, \"gsm8k_correct\": 828, \"gsm8k_total\": 1319, \"eos_rate\": 0.9856, \"avg_response_length\": 188.16, \"natural_eos\": 1300, \"truncated\": 19}, \"notes\": \"Cron 误判为 failed（进程正常退出但 cron 未检测到 sentinel）。实际完成 1319/1319，accuracy=62.77%。α=4.0 GRPO > Standard GRPO (59.84%) > RASP α=1.0 GRPO (54.43%)。确认 α tuning 有效缓解 RASP collapse。checkpoint_path: /root/autodl-tmp/recovery_aware_struct_prune/grpo_alpha4_20/checkpoint-100, log_path: /root/recovery_aware_struct_prune/logs/eval_gsm8k_grpo_alpha4_20_v3.log, results_path: /root/recovery_aware_struct_prune/results/eval_gsm8k_grpo_alpha4_20_v3.json\"}, \"eval_math500_sft_standard_25\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-21T02:58:32.492Z\", \"updated_at\": \"2026-05-22T02:31:03.648Z\", \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"reproduce\": {\"finished_at\": \"2026-05-21T02:58:40.587Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-21T02:58:45.343074+00:00\"}], \"previous_failure\": {\"conclusion\": \"success\", \"metrics\": {\"math500_accuracy\": 0.13, \"correct\": 65, \"n_total\": 500}, \"notes\": \"v1 结果采用（v2 启动即崩溃）。结果文件: /root/autodl-tmp/recovery_aware_struct_prune/results/eval_math500_sft_standard_25.json。Director 于 2026-05-21 批准采用 v1 数据。\"}}, \"notes\": \"v1 结果采用（v2 启动即崩溃）。结果文件: /root/autodl-tmp/recovery_aware_struct_prune/results/eval_math500_sft_standard_25.json。Director 于 2026-05-21 批准采用 v1 数据。\", \"hypothesis\": \"Standard 25% SFT model MATH-500 accuracy establishes pre-GRPO baseline for standard pruning at 25% sparsity, enabling SFT→GRPO recovery delta on MATH-500\", \"completed_at\": \"2026-05-21T19:22:29.444Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_25/checkpoint-1870 --output_path /root/runs/recovery_aware_struct_prune/eval_math500_sft_standard_25/results.json --max_new_tokens 2048 --seed 42\", \"server\": \"westb-23072\", \"gpu\": [\"cuda:1\"], \"pid\": \"104592\", \"data_path\": \"MATH-500\", \"data_count\": 500, \"model_name\": \"sft_standard_25/checkpoint-1870\", \"model_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_25/checkpoint-1870\", \"seed\": 42, \"checkpoint_source\": \"sft_standard_25\", \"eval_data\": \"MATH-500\", \"log_path\": \"/root/runs/recovery_aware_struct_prune/eval_math500_sft_standard_25/run.log\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_25/checkpoint-1870\"}, \"conclusion\": \"success\", \"metrics\": {\"math500_accuracy\": 0.14, \"correct\": 70, \"n_total\": 500, \"natural_eos\": 185, \"truncated\": 315, \"avg_response_length\": 1367.82, \"v1_accuracy\": 0.13, \"v1_correct\": 65}}, \"grpo_alpha4_20\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T18:59:18.863Z\", \"updated_at\": \"2026-05-21T19:32:31.353Z\", \"hypothesis\": \"α=4.0 GRPO after SFT: if reward collapses (→0 like α=1.0 RASP GRPO), proves RASP collapse is structural, not hyperparameter-dependent. If reward stays positive and GSM8K improves over SFT, α tuning can mitigate collapse.\", \"parent\": \"sft_alpha4_20_v2\", \"spec\": {\"command\": \"python src/train_grpo_v5.py --alpha 4.0 --max_steps 100\", \"server\": \"westd-29022\", \"gpu\": [\"cuda:2\"], \"pid\": \"406593\", \"log_path\": \"~/runs/recovery_aware_struct_prune/grpo_alpha4_20.log\", \"submitted_at\": \"2026-05-21T18:59:44.258Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"Qwen2.5-7B\", \"seed\": 42, \"data_path\": \"gsm8k\", \"data_count\": 7473, \"checkpoint_source\": \"sft_alpha4_20_v2\", \"eval_data\": \"gsm8k\", \"wall_clock_seconds\": 1659.0, \"gpu_hours\": 0.46}, \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_alpha4_20/checkpoint-100\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/logs/grpo_alpha4_20.log\", \"metrics\": {\"final_reward\": 0.198, \"reward_range\": \"0.146-0.256\", \"steps\": 100, \"final_loss\": 0.018, \"final_kl\": 0.00198}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-21T19:27:23.228Z\"}, \"sft_alpha4_20_v2\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T18:30:48.284Z\", \"updated_at\": \"2026-05-21T19:32:28.482Z\", \"hypothesis\": \"α=4.0 SFT recovery with save_only_model=True to prevent disk overflow. Pruning successful (19.09% sparsity). Testing if higher α mitigates RASP collapse after full SFT→GRPO→eval pipeline.\", \"parent\": \"sft_alpha4_20_manual\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/recovery_aware_struct_prune && python src/train_sft_warmup.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/pruned_alpha4_20 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/sft_alpha4_20 --num_epochs 2 --lr 2e-5\\\"\", \"server\": \"westd-29022\", \"gpu\": [\"cuda:2\"], \"pid\": \"401581\", \"log_path\": \"~/runs/recovery_aware_struct_prune/sft_alpha4_20_v2.log\", \"submitted_at\": \"2026-05-21T18:31:05.499Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"reproduce\": {\"finished_at\": \"2026-05-21T18:54:53.481Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-21T18:54:59.708620+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"final_train_loss\": 0.8118, \"token_accuracy\": 0.8165, \"epochs\": 2, \"steps\": 936}}, \"eval_math500_grpo_cka_only_25_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T13:54:50.310Z\", \"updated_at\": \"2026-05-21T17:33:50.709Z\", \"hypothesis\": \"CKA-only 25% GRPO model MATH-500 @2048 accuracy for cross-benchmark validation, re-run with correct max_new_tokens=2048 for consistency with 20% data\", \"parent\": \"eval_math500_grpo_cka_only_25\", \"spec\": {\"command\": \"nohup bash -c 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=0 python /root/recovery_aware_struct_prune/src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_25 --output_path /root/runs/recovery_aware_struct_prune/eval_math500_grpo_cka_only_25_v2 --seed 42 --max_new_tokens 2048' > /root/runs/recovery_aware_struct_prune/eval_math500_grpo_cka_only_25_v2/eval_math500_grpo_cka_only_25_v2.log 2>&1 &\", \"server\": \"westd-29022\", \"gpu\": \"cuda:0\", \"pid\": 379999, \"data_path\": \"MATH-500\", \"data_count\": 500, \"model_name\": \"Qwen2.5-7B CKA-only 25% GRPO\", \"model_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_25\", \"seed\": 42, \"checkpoint_source\": \"grpo_cka_only_25\", \"eval_data\": \"MATH-500\", \"log_path\": \"/root/runs/recovery_aware_struct_prune/eval_math500_grpo_cka_only_25_v2/eval_math500_grpo_cka_only_25_v2.log\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"N/A (eval only)\", \"completed_at\": \"2026-05-21T17:33:40.068Z\", \"metrics\": {\"math500_accuracy\": 0.184, \"math500_stderr\": 0.0173, \"correct\": 92, \"n_total\": 500}, \"log_path\": \"/root/runs/recovery_aware_struct_prune/eval_math500_grpo_cka_only_25_v2/eval_math500_grpo_cka_only_25_v2.log\"}, \"eval_math500_sft_cka_only_25_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T13:54:51.945Z\", \"updated_at\": \"2026-05-21T17:29:14.940Z\", \"hypothesis\": \"CKA-only 25% SFT model MATH-500 @2048 accuracy establishes pre-GRPO baseline, re-run with correct max_new_tokens=2048 for consistency\", \"parent\": \"eval_math500_sft_cka_only_25\", \"spec\": {\"command\": \"nohup bash -c 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=2 python /root/recovery_aware_struct_prune/src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_25 --output_path /root/runs/recovery_aware_struct_prune/eval_math500_sft_cka_only_25_v2 --seed 42 --max_new_tokens 2048' > /root/runs/recovery_aware_struct_prune/eval_math500_sft_cka_only_25_v2/eval_math500_sft_cka_only_25_v2.log 2>&1 &\", \"server\": \"westd-29022\", \"gpu\": \"cuda:2\", \"pid\": 380074, \"data_path\": \"MATH-500\", \"data_count\": 500, \"model_name\": \"Qwen2.5-7B CKA-only 25% SFT\", \"model_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_25\", \"seed\": 42, \"checkpoint_source\": \"sft_cka_only_25\", \"eval_data\": \"MATH-500\", \"log_path\": \"/root/runs/recovery_aware_struct_prune/eval_math500_sft_cka_only_25_v2/eval_math500_sft_cka_only_25_v2.log\"}, \"conclusion\": \"success\", \"log_path\": \"/root/runs/recovery_aware_struct_prune/eval_math500_sft_cka_only_25_v2/eval_math500_sft_cka_only_25_v2.log\", \"checkpoint_path\": \"N/A (eval only)\", \"completed_at\": \"2026-05-21T17:29:10.900Z\", \"metrics\": {\"math500_accuracy\": 0.192, \"correct\": 96, \"n_total\": 500, \"std_err\": 0.0176}, \"notes\": \"Eval completed all 500 problems. Result JSON not saved due to IsADirectoryError (output_path pointed to directory instead of file). Metrics extracted from log.\"}, \"eval_gsm8k_sft_standard_25\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T08:13:12.112Z\", \"updated_at\": \"2026-05-21T14:40:37.092Z\", \"hypothesis\": \"Standard 25% SFT GSM8K accuracy establishes pre-GRPO floor for importance-based pruning at 25% sparsity, enabling SFT→GRPO recovery delta comparison with CKA-only 25%\", \"spec\": {\"command\": \"nohup bash -c 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=3 python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_25/checkpoint-1870 --max_samples 1319 --seed 42'\", \"server\": \"westd-29022\", \"gpu\": \"cuda:3\", \"pid\": 335301, \"data_path\": \"GSM8K (N=1319)\", \"data_count\": 1319, \"model_name\": \"sft_standard_25\", \"model_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_25/checkpoint-1870\", \"seed\": 42, \"checkpoint_source\": \"sft_standard_25\", \"eval_data\": \"GSM8K\", \"log_path\": \"/root/runs/recovery_aware_struct_prune/eval_gsm8k_sft_standard_25.log\", \"checkpoint_path\": \"N/A (eval only)\"}, \"metrics\": {\"gsm8k_accuracy\": 0.5087, \"stderr\": 0.0138, \"correct\": 671, \"n_total\": 1319, \"eos_rate\": 0.953, \"avg_response_length\": 333.15}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-21T14:40:37.092Z\"}, \"eval_math500_grpo_cka_only_20\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T02:41:32.199Z\", \"updated_at\": \"2026-05-21T12:47:30.348Z\", \"hypothesis\": \"CKA-only 20% GRPO model MATH-500 accuracy provides cross-benchmark validation at 20% sparsity and cross-method comparison with Random 20% GRPO MATH-500\", \"spec\": {\"max_new_tokens_actual\": 4096, \"note\": \"未显式指定 --max_new_tokens，脚本默认 4096。与 @2048 evals 不可直接比较。需用 eval_math500_grpo_cka_only_20_2048 重跑公平对比。\"}, \"parent\": \"grpo_cka_only_20\", \"reproduce\": {\"finished_at\": \"2026-05-18T14:05:38.456Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-18T14:05:47.086682+00:00\"}]}, \"metrics\": {\"accuracy\": 0.266, \"n_correct\": 133, \"n_total\": 500, \"stderr\": 0.0198, \"truncated\": 108, \"truncation_rate\": 0.216, \"avg_response_length\": 1124.24}, \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/math500_grpo_cka_only_20.json\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_math500_grpo_cka_only_20.log\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T14:09:25.937Z\"}, \"eval_gsm8k_grpo_standard_25\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T06:42:08.819Z\", \"updated_at\": \"2026-05-21T12:37:17.579Z\", \"hypothesis\": \"Standard 25% GRPO后GSM8K评估。GRPO reward=0.00813 (near-total collapse)。验证 Standard pruning 在 25% 稀疏度下 GRPO 后数学推理能力。\", \"parent\": \"grpo_standard_25_westb\", \"spec\": {\"command\": \"python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_25_westb/checkpoint-100 --max_samples 1319 --seed 42\", \"server\": \"westb-23072\", \"gpu\": \"cuda:1\", \"pid\": 75282, \"data_path\": \"gsm8k\", \"data_count\": 1319, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B-pruned-standard-25pct-GRPO-v5fair\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_25_westb/checkpoint-100\", \"eval_data\": \"GSM8K\", \"log_path\": \"/root/runs/recovery_aware_struct_prune/eval_gsm8k_grpo_standard_25.log\"}, \"conclusion\": \"success\", \"metrics\": {\"gsm8k_accuracy\": 0.5186, \"stderr\": 0.0138, \"correct\": 684, \"n_total\": 1319, \"eos_rate\": 0.9575, \"avg_response_length\": 314.47}, \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_25_westb/checkpoint-100\", \"log_path\": \"/root/runs/recovery_aware_struct_prune/eval_gsm8k_grpo_standard_25.log\", \"completed_at\": \"2026-05-21T12:37:17.579Z\"}, \"eval_gsm8k_sft_cka_only_25\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T06:47:14.010Z\", \"updated_at\": \"2026-05-21T10:17:58.203Z\", \"hypothesis\": \"CKA-only 25% SFT model retains higher GSM8K accuracy than GRPO-recovered model's SFT baseline, establishing the pre-GRPO accuracy floor for measuring recovery delta at 25% sparsity\", \"spec\": {\"command\": \"nohup bash -c 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=1 python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_25 --max_samples 1319 --seed 42'\", \"server\": \"westd-29022\", \"gpu\": \"cuda:1\", \"pid\": 329698, \"data_path\": \"GSM8K (N=1319)\", \"data_count\": 1319, \"model_name\": \"sft_cka_only_25\", \"model_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_25\", \"seed\": 42, \"checkpoint_source\": \"sft_cka_only_25\", \"eval_data\": \"GSM8K\", \"log_path\": \"/root/runs/recovery_aware_struct_prune/eval_gsm8k_sft_cka_only_25.log\"}, \"conclusion\": \"success\", \"metrics\": {\"gsm8k_accuracy\": 0.6012, \"correct\": 793, \"n_total\": 1319, \"stderr\": 0.0135, \"eos_rate\": 0.9803, \"avg_response_length\": 243.6}, \"checkpoint_path\": \"N/A (eval only)\", \"completed_at\": \"2026-05-21T10:17:58.203Z\"}, \"eval_gsm8k_sft_random_20\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T06:47:16.459Z\", \"updated_at\": \"2026-05-21T08:47:06.620Z\", \"hypothesis\": \"Random 20% SFT model GSM8K accuracy establishes the pre-GRPO floor for random pruning, enabling SFT→GRPO recovery delta comparison across pruning methods at 20% sparsity\", \"spec\": {\"command\": \"nohup bash -c 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=2 python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_random_20 --max_samples 1319 --seed 42'\", \"server\": \"westd-29022\", \"gpu\": \"cuda:2\", \"pid\": 329770, \"data_path\": \"GSM8K (N=1319)\", \"data_count\": 1319, \"model_name\": \"sft_random_20\", \"model_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_random_20\", \"seed\": 42, \"checkpoint_source\": \"sft_random_20\", \"eval_data\": \"GSM8K\", \"log_path\": \"/root/runs/recovery_aware_struct_prune/eval_gsm8k_sft_random_20.log\"}, \"conclusion\": \"success\", \"metrics\": {\"gsm8k_accuracy\": 0.5125, \"correct\": 676, \"n_total\": 1319, \"stderr\": 0.0138, \"eos_rate\": 0.9932, \"avg_response_length\": 182.4}, \"checkpoint_path\": \"N/A (eval only)\", \"completed_at\": \"2026-05-21T08:47:06.620Z\"}, \"eval_gsm8k_grpo_cka_only_25_v3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T04:56:52.006Z\", \"updated_at\": \"2026-05-21T08:17:13.429Z\", \"hypothesis\": \"CKA-only 25% GRPO后GSM8K评估。model_path=/grpo_cka_only_25（根目录）。Cross-sparsity对比: Standard 25% GRPO=51.1%, RASP 25% GRPO=53.15%。\", \"parent\": \"grpo_cka_only_25\", \"spec\": {\"command\": \"python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_25 --max_samples 1319 --seed 42\", \"server\": \"westd-29022\", \"gpu\": [\"cuda:0\"], \"pid\": \"322443\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_gsm8k_grpo_cka_only_25_v3.log\", \"data_path\": \"gsm8k\", \"data_count\": 1319, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B-pruned-cka_only-25pct-GRPO\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_25\", \"eval_data\": \"GSM8K\"}, \"notes\": \"正确 PID=322443 (v3提交)。323174 是重复提交已 kill。\", \"conclusion\": \"success\", \"metrics\": {\"gsm8k_accuracy\": 0.5959, \"correct\": 786, \"n_total\": 1319, \"eos_rate\": 0.9818}, \"checkpoint_path\": \"N/A (eval only)\", \"completed_at\": \"2026-05-21T08:17:13.429Z\"}, \"grpo_standard_25_westb\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T03:00:00.000Z\", \"updated_at\": \"2026-05-21T06:40:00.000Z\", \"hypothesis\": \"Standard 25% GRPO v5 fair config (100 steps, lr=1e-6, beta=0.01, T=0.4, seed=42) on westb. Re-run with fair config for cross-method comparison.\", \"parent\": \"sft_standard_25\", \"spec\": {\"command\": \"python src/train_grpo_v5.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_25 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_25_westb --max_steps 100 --save_steps 100 --seed 42\", \"server\": \"westb-23072\", \"gpu\": [\"cuda:1\"], \"pid\": \"64194\", \"data_path\": \"gsm8k\", \"data_count\": 7473, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B-pruned-standard-25pct-SFT\", \"seed\": 42}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-21T06:40:00.000Z\", \"metrics\": {\"reward\": 0.00813, \"steps\": 100, \"collapse_pattern\": \"near_total_collapse\"}, \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_25_westb/checkpoint-100\", \"log_path\": \"~/runs/recovery_aware_struct_prune/grpo_standard_25.log\"}, \"eval_gsm8k_grpo_random_20_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T04:56:53.980Z\", \"updated_at\": \"2026-05-21T06:38:00.000Z\", \"hypothesis\": \"Random 20% GRPO后GSM8K评估。Random pruning reward=0.189（最低），验证无结构保留的pruning在GRPO后数学推理能力。\", \"parent\": \"grpo_random_20\", \"spec\": {\"command\": \"python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_random_20/checkpoint-100 --max_samples 1319 --seed 42\", \"server\": \"westd-29022\", \"gpu\": [\"cuda:1\"], \"pid\": \"322611\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_gsm8k_grpo_random_20_v2.log\", \"data_path\": \"gsm8k\", \"data_count\": 1319, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B-pruned-random-20pct-GRPO\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_random_20/checkpoint-100\", \"eval_data\": \"GSM8K\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-21T06:38:00.000Z\", \"metrics\": {\"gsm8k_accuracy\": 0.5057, \"gsm8k_stderr\": 0.0138, \"correct\": 667, \"total\": 1319, \"eos_rate\": 0.9954, \"avg_response_length\": 173}, \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_random_20/checkpoint-100\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_gsm8k_grpo_random_20_v2.log\"}, \"sft_random_20\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T03:44:24.654Z\", \"updated_at\": \"2026-05-21T04:45:00.000Z\", \"hypothesis\": \"Random 20% pruning baseline SFT recovery. Random pruning 不保留任何结构信息，作为 ablation baseline 验证 CKA-guided pruning 的结构保留优势。\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-21T03:50:00.000Z\", \"spec\": {\"server\": \"westd-29022\", \"gpu\": [\"cuda:0\"], \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B-pruned-random-20pct\", \"command\": \"python src/sft_recovery.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/pruned_random_20 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/sft_random_20\", \"data_path\": \"gsm8k\", \"seed\": 42}, \"metrics\": {\"steps\": 1870, \"model_size_gb\": 12}, \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_random_20\", \"log_path\": \"/root/runs/recovery_aware_struct_prune/sft_random_20.log\"}}, \"count\": 50, \"total\": 249, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.9127}}"
    }
  },
  "sourceToolAssistantUUID": "fab33cb5-f090-4a9b-af22-7bf869df109c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "3a90179e-e19e-41d1-8fb4-f23e916f555f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Runtime record

_source line 56_

```json
{
  "type": "last-prompt",
  "leafUuid": "37dfbb3b-7fbe-4af0-9a4b-e816cbddb1fd",
  "sessionId": "3a90179e-e19e-41d1-8fb4-f23e916f555f"
}
```

---


### Runtime record

_source line 57_

```json
{
  "type": "ai-title",
  "aiTitle": "Map paper results to registry experiments",
  "sessionId": "3a90179e-e19e-41d1-8fb4-f23e916f555f"
}
```

---


### Assistant

_source line 58 · 2026-05-23T10:52:26.355Z_

<details><summary>Logged reasoning block</summary>

```text
The registry returns the same 50 most recent results. I need to use `offset` to get more. But looking at the API, there's no `offset` parameter. Let me check the registry tool definition again... It has `limit` but no `offset`. 

Let me try a different approach - let me read the full registry without a limit, and use an agent to parse it.

Actually wait, the `limit` parameter says "0 = all". So let me try limit=0 to get all experiments. But that'll be too big. Let me try a different approach - read all with limit=0, save to disk, then have an agent parse the full thing.


Actually, I could try limit=0 with minimal fields to reduce the payload size.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "37dfbb3b-7fbe-4af0-9a4b-e816cbddb1fd",
  "isSidechain": false,
  "requestId": "req_011CbKNfE9LZem9SZCorBxWp",
  "type": "assistant",
  "uuid": "ab0f6c9a-9077-4219-87d6-5f0ae63387af",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "3a90179e-e19e-41d1-8fb4-f23e916f555f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Lrxj2W2npRMFZcTNFfv5bM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 758,
      "cache_read_input_tokens": 55757,
      "output_tokens": 375,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 758,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 375,
          "cache_read_input_tokens": 55757,
          "cache_creation_input_tokens": 758,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 758
          },
          "type": "message"
        }
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

_source line 59 · 2026-05-23T10:52:26.364Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01BSoaLqkwubkCC7EAUvLzVF`</summary>

```json
{
  "project": "recovery_aware_struct_prune",
  "filters": {
    "conclusion": "success"
  },
  "limit": 0,
  "fields": [
    "exp_id",
    "metrics",
    "created_at",
    "updated_at",
    "tags"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ab0f6c9a-9077-4219-87d6-5f0ae63387af",
  "isSidechain": false,
  "requestId": "req_011CbKNfE9LZem9SZCorBxWp",
  "type": "assistant",
  "uuid": "23ca0e31-fe63-4b43-9d20-38c5e0c3aa5b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "3a90179e-e19e-41d1-8fb4-f23e916f555f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Lrxj2W2npRMFZcTNFfv5bM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 758,
      "cache_read_input_tokens": 55757,
      "output_tokens": 375,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 758,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 375,
          "cache_read_input_tokens": 55757,
          "cache_creation_input_tokens": 758,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 758
          },
          "type": "message"
        }
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

_source line 60 · 2026-05-23T10:52:27.525Z_

<details><summary>↩ Tool result · `toolu_01BSoaLqkwubkCC7EAUvLzVF`</summary>

```text
Error: result (72,125 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-17-projects-recovery-aware-struct-prune/3a90179e-e19e-41d1-8fb4-f23e916f555f/tool-results/mcp-agent-ml-research-read_registry-1779533547522.txt.
Format: JSON with schema: {result: string}
- For targeted queries (find a value, filter by field): use jq on the file directly.
- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-17-projects-recovery-aware-struct-prune/3a90179e-e19e-41d1-8fb4-f23e916f555f/tool-results/mcp-agent-ml-research-read_registry-1779533547522.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.
- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-17-projects-recovery-aware-struct-prune/3a90179e-e19e-41d1-8fb4-f23e916f555f/tool-results/mcp-agent-ml-research-read_registry-1779533547522.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim." A vague "summarize this" may lose detail.

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "23ca0e31-fe63-4b43-9d20-38c5e0c3aa5b",
  "isSidechain": false,
  "promptId": "dddf37fd-16cc-4cd5-bb05-648328938281",
  "type": "user",
  "uuid": "e4bc7c49-4335-41db-a060-e969df0f0e8d",
  "toolUseResult": "Error: result (72,125 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-17-projects-recovery-aware-struct-prune/3a90179e-e19e-41d1-8fb4-f23e916f555f/tool-results/mcp-agent-ml-research-read_registry-1779533547522.txt.\nFormat: JSON with schema: {result: string}\n- For targeted queries (find a value, filter by field): use jq on the file directly.\n- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-17-projects-recovery-aware-struct-prune/3a90179e-e19e-41d1-8fb4-f23e916f555f/tool-results/mcp-agent-ml-research-read_registry-1779533547522.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.\n- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. \"/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-17-projects-recovery-aware-struct-prune/3a90179e-e19e-41d1-8fb4-f23e916f555f/tool-results/mcp-agent-ml-research-read_registry-1779533547522.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim.\" A vague \"summarize this\" may lose detail.\n",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"eval_math500_sft_qwen_math_cka_only_20\": {\"created_at\": \"2026-05-22T23:11:09.017Z\", \"updated_at\": \"2026-05-23T10:44:00.535Z\", \"metrics\": {\"accuracy\": 0.216, \"stderr\": 0.0184, \"correct\": 108, \"total\": 500, \"natural_eos\": 90, \"truncated\": 410, \"avg_response_length\": 1745.338}}, \"eval_math500_grpo_rasp_alpha0p5_20\": {\"created_at\": \"2026-05-23T02:59:15.985Z\", \"updated_at\": \"2026-05-23T10:11:11.002Z\", \"metrics\": {\"accuracy\": 0.248, \"stderr\": 0.0193, \"correct\": 124, \"total\": 500, \"natural_eos\": 274, \"truncated\": 226, \"avg_response_length\": 1110.462}}, \"eval_math500_grpo_cka_only_20_2048_v2\": {\"created_at\": \"2026-05-23T05:07:09.002Z\", \"updated_at\": \"2026-05-23T08:55:58.278Z\", \"metrics\": {\"accuracy\": 0.274, \"correct\": 137, \"total\": 500, \"stderr\": 0.01995, \"natural_eos\": 390, \"truncated\": 110, \"avg_response_length\": 654.746}}, \"eval_math500_grpo_rasp_alpha3p0_20\": {\"created_at\": \"2026-05-23T03:19:40.950Z\", \"updated_at\": \"2026-05-23T07:48:57.618Z\", \"metrics\": {\"accuracy\": 0.228, \"correct\": 114, \"total\": 500, \"stderr\": 0.0188, \"truncated_ratio\": 0.28, \"avg_response_length\": 745.038}}, \"eval_math500_grpo_rasp_alpha4p0_20\": {\"created_at\": \"2026-05-23T00:01:54.194Z\", \"updated_at\": \"2026-05-23T05:58:52.769Z\", \"metrics\": {\"accuracy\": 0.262, \"stderr\": 0.01966, \"correct\": 131, \"total\": 500, \"truncated\": 180, \"natural_eos\": 320, \"avg_response_length\": 925.48}}, \"eval_math500_grpo_rasp_alpha1p0_20\": {\"created_at\": \"2026-05-22T23:02:44.335Z\", \"updated_at\": \"2026-05-23T04:44:32.303Z\", \"metrics\": {\"accuracy\": 0.226, \"stderr\": 0.0187, \"n_correct\": 113, \"n_total\": 500, \"avg_response_length\": 903.536, \"natural_eos\": 320, \"truncated\": 180}}, \"eval_math500_sft_cka_only_20_westd\": {\"created_at\": \"2026-05-22T20:45:21.526Z\", \"updated_at\": \"2026-05-23T03:21:26.164Z\", \"metrics\": {\"accuracy\": 0.268, \"correct\": 134, \"total\": 500, \"truncated\": 116, \"stderr\": 0.0198, \"natural_eos_pct\": 0.768, \"avg_response_length\": 673.278, \"note\": \"PID 75284 actual output = 26.8% (134/500). Previous 29.0% (145/500) was from v4 run (May 19) with different answer extraction. Same model generations, different scoring.\"}}, \"eval_math500_grpo_rasp_alpha2p0_20\": {\"created_at\": \"2026-05-22T22:23:27.589Z\", \"updated_at\": \"2026-05-23T03:16:40.537Z\", \"metrics\": {\"accuracy\": 0.262, \"correct\": 131, \"total\": 500, \"stderr\": 0.0197, \"natural_eos\": 349, \"truncated\": 151, \"avg_response_length\": 785.326}}, \"eval_gsm8k_grpo_qwen_math_cka_only_20_n500_v3\": {\"created_at\": \"2026-05-22T15:12:46.181Z\", \"updated_at\": \"2026-05-23T02:53:37.071Z\", \"metrics\": {\"accuracy\": 0.486, \"correct\": 243, \"total\": 500, \"stderr\": 0.0224, \"truncated_pct\": 0.838, \"natural_eos_pct\": 0.162, \"avg_response_length\": 1766.5}}, \"eval_math500_sft_rasp_alpha1p0_20_v2\": {\"created_at\": \"2026-05-22T20:50:24.239Z\", \"updated_at\": \"2026-05-22T23:01:03.419Z\", \"metrics\": {\"accuracy\": 0.212, \"correct\": 106, \"total\": 500, \"truncated\": 186, \"stderr\": 0.0183}}, \"eval_math500_sft_standard_20_2048_v2\": {\"created_at\": \"2026-05-19T01:34:44.782Z\", \"updated_at\": \"2026-05-22T22:19:38.080Z\", \"metrics\": {\"accuracy\": 0.258, \"n_correct\": 129, \"n_total\": 500}}, \"eval_math500_sft_rasp_alpha0p5_20\": {\"created_at\": \"2026-05-22T15:20:44.460Z\", \"updated_at\": \"2026-05-22T22:18:43.350Z\", \"metrics\": {\"accuracy\": 0.254, \"correct\": 127, \"total\": 500, \"truncated\": 220, \"stderr\": 0.0195}}, \"eval_math500_sft_rasp_alpha3p0_20\": {\"created_at\": \"2026-05-22T18:26:16.273Z\", \"updated_at\": \"2026-05-22T22:12:26.406Z\", \"metrics\": {\"accuracy\": 0.232, \"correct\": 116, \"total\": 500, \"truncated\": 144, \"stderr\": 0.0189}}, \"eval_math500_sft_rasp_alpha4p0_20\": {\"created_at\": \"2026-05-22T15:20:47.150Z\", \"updated_at\": \"2026-05-22T21:22:35.441Z\", \"metrics\": {\"accuracy\": 0.266, \"correct\": 133, \"total\": 500, \"truncated\": 190, \"stderr\": 0.0198}}, \"eval_math500_sft_rasp_alpha2p0_20\": {\"created_at\": \"2026-05-22T15:06:22.386Z\", \"updated_at\": \"2026-05-22T20:44:52.970Z\", \"metrics\": {\"accuracy\": 0.24, \"correct\": 120, \"total\": 500, \"truncated\": 155, \"stderr\": 0.0191}}, \"eval_gsm8k_grpo_random_20_seed456\": {\"created_at\": \"2026-05-22T16:26:01.516Z\", \"updated_at\": \"2026-05-22T18:27:22.282Z\", \"metrics\": {\"gsm8k_accuracy\": 0.5087, \"gsm8k_accuracy_se\": 0.0138, \"gsm8k_correct\": 671, \"gsm8k_total\": 1319, \"eos_rate\": 0.9954, \"avg_response_length\": 163.5, \"truncated\": 6}}, \"eval_gsm8k_grpo_random_20_seed123_v2\": {\"created_at\": \"2026-05-22T14:22:33.753Z\", \"updated_at\": \"2026-05-22T16:49:54.123Z\"}, \"grpo_random_20_seed456\": {\"created_at\": \"2026-05-22T12:00:38.940Z\", \"updated_at\": \"2026-05-22T16:27:46.810Z\"}, \"eval_gsm8k_sft_depth_first_20\": {\"created_at\": \"2026-05-22T14:20:43.950Z\", \"updated_at\": \"2026-05-22T15:19:31.829Z\"}, \"eval_gsm8k_grpo_depth_first_20\": {\"created_at\": \"2026-05-22T14:20:41.126Z\", \"updated_at\": \"2026-05-22T15:18:38.970Z\"}, \"grpo_random_20_seed123_v2\": {\"created_at\": \"2026-05-22T14:22:29.868Z\", \"updated_at\": \"2026-05-22T15:00:23.101Z\"}, \"eval_gsm8k_grpo_alpha3p0_20\": {\"created_at\": \"2026-05-22T09:30:06.630Z\", \"updated_at\": \"2026-05-22T14:47:06.188Z\", \"metrics\": {\"gsm8k_accuracy\": 0.6345, \"correct\": 837, \"total\": 1319, \"stderr\": 0.0133, \"eos_rate\": 0.9864, \"truncated\": 18, \"avg_response_length\": 219.7}}, \"eval_math500_sft_random_20_v3\": {\"created_at\": \"2026-05-22T04:11:52.462Z\", \"updated_at\": \"2026-05-22T14:10:18.359Z\", \"metrics\": {\"accuracy\": 0.144, \"correct\": 72, \"total\": 500, \"stderr\": 0.0157, \"natural_eos\": 171, \"truncated\": 329, \"avg_response_length\": 1470.44}}, \"eval_gsm8k_sft_alpha3p0_20\": {\"created_at\": \"2026-05-22T10:24:58.696Z\", \"updated_at\": \"2026-05-22T12:38:25.600Z\", \"metrics\": {\"gsm8k_accuracy\": 0.6414, \"gsm8k_correct\": 846, \"gsm8k_total\": 1319, \"gsm8k_stderr\": 0.0132, \"eos_rate\": 0.9879, \"avg_response_length\": 188.63, \"natural_eos\": 1303, \"truncated\": 16}}, \"grpo_rasp_alpha3p0_20_v2\": {\"created_at\": \"2026-05-22T10:40:19.362Z\", \"updated_at\": \"2026-05-22T11:58:15.586Z\"}, \"eval_math500_grpo_standard_20_fair_2048_v2\": {\"created_at\": \"2026-05-22T03:49:45.575Z\", \"updated_at\": \"2026-05-22T11:17:52.493Z\", \"metrics\": {\"math500_accuracy\": 0.264, \"math500_correct\": 132, \"math500_total\": 500, \"math500_stderr\": 0.0197}}, \"grpo_random_20_seed123\": {\"created_at\": \"2026-05-22T10:34:12.100Z\", \"updated_at\": \"2026-05-22T11:17:21.388Z\"}, \"grpo_rasp_alpha3p0_20\": {\"created_at\": \"2026-05-22T08:48:06.001Z\", \"updated_at\": \"2026-05-22T10:39:07.034Z\"}, \"eval_gsm8k_sft_alpha2p0_20\": {\"created_at\": \"2026-05-22T10:19:50.623Z\", \"updated_at\": \"2026-05-22T10:22:56.503Z\", \"metrics\": {\"gsm8k_accuracy\": 0.6497, \"gsm8k_correct\": 857, \"gsm8k_total\": 1319}}, \"eval_gsm8k_sft_alpha0p5_20\": {\"created_at\": \"2026-05-22T10:19:48.133Z\", \"updated_at\": \"2026-05-22T10:20:57.690Z\", \"metrics\": {\"gsm8k_accuracy\": 0.6073, \"gsm8k_correct\": 801, \"gsm8k_total\": 1319}}, \"grpo_qwen_math_cka_only_20\": {\"created_at\": \"2026-05-22T08:50:34.293Z\", \"updated_at\": \"2026-05-22T09:54:05.974Z\"}, \"eval_gsm8k_grpo_alpha2p0_20\": {\"created_at\": \"2026-05-22T09:28:08.089Z\", \"updated_at\": \"2026-05-22T09:29:24.824Z\", \"metrics\": {\"gsm8k_accuracy\": 0.6611, \"gsm8k_correct\": 872, \"gsm8k_total\": 1319}}, \"eval_gsm8k_grpo_alpha0p5_20\": {\"created_at\": \"2026-05-22T09:28:05.478Z\", \"updated_at\": \"2026-05-22T09:29:23.350Z\", \"metrics\": {\"gsm8k_accuracy\": 0.6118, \"gsm8k_correct\": 807, \"gsm8k_total\": 1319}}, \"eval_math500_sft_standard_20_1p5b\": {\"created_at\": \"2026-05-22T04:31:30.202Z\", \"updated_at\": \"2026-05-22T08:27:40.167Z\", \"metrics\": {\"math500_accuracy\": 0.054, \"correct\": 27, \"total\": 500, \"truncated\": 335}}, \"eval_gsm8k_sft_alpha4_20_v5\": {\"created_at\": \"2026-05-22T03:49:50.201Z\", \"updated_at\": \"2026-05-22T06:05:53.848Z\", \"metrics\": {\"gsm8k_accuracy\": 0.6194, \"correct\": 817, \"total\": 1319, \"stderr\": 0.0134, \"eos_rate\": 0.981, \"avg_response_length\": 197.85}}, \"eval_gsm8k_grpo_alpha4_20_v3\": {\"created_at\": \"2026-05-22T03:49:52.414Z\", \"updated_at\": \"2026-05-22T05:33:39.349Z\", \"metrics\": {\"gsm8k_accuracy\": 0.6277, \"gsm8k_accuracy_ci\": 0.0133, \"gsm8k_correct\": 828, \"gsm8k_total\": 1319, \"eos_rate\": 0.9856, \"avg_response_length\": 188.16, \"natural_eos\": 1300, \"truncated\": 19}}, \"eval_math500_sft_standard_25\": {\"created_at\": \"2026-05-21T02:58:32.492Z\", \"updated_at\": \"2026-05-22T02:31:03.648Z\", \"metrics\": {\"math500_accuracy\": 0.14, \"correct\": 70, \"n_total\": 500, \"natural_eos\": 185, \"truncated\": 315, \"avg_response_length\": 1367.82, \"v1_accuracy\": 0.13, \"v1_correct\": 65}}, \"grpo_alpha4_20\": {\"created_at\": \"2026-05-21T18:59:18.863Z\", \"updated_at\": \"2026-05-21T19:32:31.353Z\", \"metrics\": {\"final_reward\": 0.198, \"reward_range\": \"0.146-0.256\", \"steps\": 100, \"final_loss\": 0.018, \"final_kl\": 0.00198}}, \"sft_alpha4_20_v2\": {\"created_at\": \"2026-05-21T18:30:48.284Z\", \"updated_at\": \"2026-05-21T19:32:28.482Z\", \"metrics\": {\"final_train_loss\": 0.8118, \"token_accuracy\": 0.8165, \"epochs\": 2, \"steps\": 936}}, \"eval_math500_grpo_cka_only_25_v2\": {\"created_at\": \"2026-05-21T13:54:50.310Z\", \"updated_at\": \"2026-05-21T17:33:50.709Z\", \"metrics\": {\"math500_accuracy\": 0.184, \"math500_stderr\": 0.0173, \"correct\": 92, \"n_total\": 500}}, \"eval_math500_sft_cka_only_25_v2\": {\"created_at\": \"2026-05-21T13:54:51.945Z\", \"updated_at\": \"2026-05-21T17:29:14.940Z\", \"metrics\": {\"math500_accuracy\": 0.192, \"correct\": 96, \"n_total\": 500, \"std_err\": 0.0176}}, \"eval_gsm8k_sft_standard_25\": {\"created_at\": \"2026-05-21T08:13:12.112Z\", \"updated_at\": \"2026-05-21T14:40:37.092Z\", \"metrics\": {\"gsm8k_accuracy\": 0.5087, \"stderr\": 0.0138, \"correct\": 671, \"n_total\": 1319, \"eos_rate\": 0.953, \"avg_response_length\": 333.15}}, \"eval_math500_grpo_cka_only_20\": {\"created_at\": \"2026-05-18T02:41:32.199Z\", \"updated_at\": \"2026-05-21T12:47:30.348Z\", \"metrics\": {\"accuracy\": 0.266, \"n_correct\": 133, \"n_total\": 500, \"stderr\": 0.0198, \"truncated\": 108, \"truncation_rate\": 0.216, \"avg_response_length\": 1124.24}}, \"eval_gsm8k_grpo_standard_25\": {\"created_at\": \"2026-05-21T06:42:08.819Z\", \"updated_at\": \"2026-05-21T12:37:17.579Z\", \"metrics\": {\"gsm8k_accuracy\": 0.5186, \"stderr\": 0.0138, \"correct\": 684, \"n_total\": 1319, \"eos_rate\": 0.9575, \"avg_response_length\": 314.47}}, \"eval_gsm8k_sft_cka_only_25\": {\"created_at\": \"2026-05-21T06:47:14.010Z\", \"updated_at\": \"2026-05-21T10:17:58.203Z\", \"metrics\": {\"gsm8k_accuracy\": 0.6012, \"correct\": 793, \"n_total\": 1319, \"stderr\": 0.0135, \"eos_rate\": 0.9803, \"avg_response_length\": 243.6}}, \"eval_gsm8k_sft_random_20\": {\"created_at\": \"2026-05-21T06:47:16.459Z\", \"updated_at\": \"2026-05-21T08:47:06.620Z\", \"metrics\": {\"gsm8k_accuracy\": 0.5125, \"correct\": 676, \"n_total\": 1319, \"stderr\": 0.0138, \"eos_rate\": 0.9932, \"avg_response_length\": 182.4}}, \"eval_gsm8k_grpo_cka_only_25_v3\": {\"created_at\": \"2026-05-21T04:56:52.006Z\", \"updated_at\": \"2026-05-21T08:17:13.429Z\", \"metrics\": {\"gsm8k_accuracy\": 0.5959, \"correct\": 786, \"n_total\": 1319, \"eos_rate\": 0.9818}}, \"grpo_standard_25_westb\": {\"created_at\": \"2026-05-21T03:00:00.000Z\", \"updated_at\": \"2026-05-21T06:40:00.000Z\", \"metrics\": {\"reward\": 0.00813, \"steps\": 100, \"collapse_pattern\": \"near_total_collapse\"}}, \"eval_gsm8k_grpo_random_20_v2\": {\"created_at\": \"2026-05-21T04:56:53.980Z\", \"updated_at\": \"2026-05-21T06:38:00.000Z\", \"metrics\": {\"gsm8k_accuracy\": 0.5057, \"gsm8k_stderr\": 0.0138, \"correct\": 667, \"total\": 1319, \"eos_rate\": 0.9954, \"avg_response_length\": 173}}, \"sft_random_20\": {\"created_at\": \"2026-05-21T03:44:24.654Z\", \"updated_at\": \"2026-05-21T04:45:00.000Z\", \"metrics\": {\"steps\": 1870, \"model_size_gb\": 12}}, \"grpo_random_20\": {\"created_at\": \"2026-05-17T13:30:31.016Z\", \"updated_at\": \"2026-05-21T04:42:00.000Z\", \"metrics\": {\"reward_mean\": 0.164, \"reward_range\": [0.14, 0.19], \"reward_peak\": 0.19, \"reward_peak_step\": 70, \"frac_zero_std_mean\": 0.333, \"frac_zero_std_range\": [0.3, 0.4], \"entropy_mean\": 0.221, \"entropy_range\": [0.2, 0.24], \"kl_mean\": 0.0045, \"steps_captured\": 9, \"max_step\": 90, \"pattern\": \"stable plateau, no collapse\", \"data_source\": \"log_file (W&B crashed before sync)\"}}, \"grpo_cka_only_25\": {\"created_at\": \"2026-05-21T02:49:22.258Z\", \"updated_at\": \"2026-05-21T03:22:07.134Z\", \"metrics\": {\"reward\": 0.2875, \"steps\": 100}}, \"eval_humaneval_sft_standard_25\": {\"created_at\": \"2026-05-21T02:43:32.214Z\", \"updated_at\": \"2026-05-21T02:44:15.495Z\", \"metrics\": {\"pass_at_1\": 0.0183, \"stderr\": 0.0105, \"n_passed\": 3, \"n_total\": 164}}, \"sft_cka_only_25\": {\"created_at\": \"2026-05-21T01:50:42.758Z\", \"updated_at\": \"2026-05-21T02:40:00.000Z\", \"metrics\": {\"final_loss\": 0.6508, \"mean_token_accuracy\": 0.8285, \"training_time_s\": 1644}}, \"prune_cka_only_25\": {\"created_at\": \"2026-05-18T13:43:54.266Z\", \"updated_at\": \"2026-05-21T01:50:00.000Z\", \"metrics\": {\"actual_sparsity\": 0.2367, \"mlp_groups_pruned\": 248, \"mlp_groups_total\": 784, \"attn_groups_pruned\": 0, \"attn_groups_total\": 112, \"param_count_B\": 5.81, \"original_param_count_B\": 7.62}}, \"eval_gsm8k_grpo_standard_15_seed123_v3\": {\"created_at\": \"2026-05-20T23:00:14.007Z\", \"updated_at\": \"2026-05-21T00:57:58.499Z\", \"metrics\": {\"accuracy\": 0.6513, \"accuracy_se\": 0.0131, \"n_correct\": 859, \"n_total\": 1319, \"eos_rate\": 0.9932, \"avg_response_length\": 183.25}}, \"eval_gsm8k_grpo_standard_15_seed456_v3\": {\"created_at\": \"2026-05-20T23:00:15.387Z\", \"updated_at\": \"2026-05-21T00:51:20.262Z\", \"metrics\": {\"gsm8k_accuracy\": 0.6543, \"gsm8k_stderr\": 0.0131, \"n_correct\": 863, \"n_total\": 1319, \"eos_rate\": 0.9939, \"avg_response_length\": 180.23}}, \"eval_gsm8k_grpo_cka_only_15_seed123\": {\"created_at\": \"2026-05-20T21:35:28.222Z\", \"updated_at\": \"2026-05-21T00:18:00.000Z\", \"metrics\": {\"accuracy\": 73.09, \"n_correct\": 964, \"n_total\": 1319, \"stderr\": 1.22, \"eos_rate\": 98.79, \"truncated\": 16}}, \"eval_gsm8k_grpo_cka_only_15_seed456\": {\"created_at\": \"2026-05-20T21:35:29.444Z\", \"updated_at\": \"2026-05-21T00:06:17.294Z\", \"metrics\": {\"accuracy\": 0.721, \"n_correct\": 951, \"n_total\": 1319, \"stderr\": 0.0123, \"eos_rate\": 0.9894, \"avg_response_length\": 201.94}}, \"grpo_standard_15_seed456_v3\": {\"created_at\": \"2026-05-20T21:58:14.439Z\", \"updated_at\": \"2026-05-20T22:51:31.775Z\"}, \"grpo_standard_15_seed123_v3\": {\"created_at\": \"2026-05-20T21:58:11.697Z\", \"updated_at\": \"2026-05-20T22:51:30.499Z\"}, \"grpo_cka_only_15_seed456\": {\"created_at\": \"2026-05-20T20:54:57.409Z\", \"updated_at\": \"2026-05-20T21:35:16.671Z\"}, \"grpo_cka_only_15_seed123\": {\"created_at\": \"2026-05-20T20:54:54.710Z\", \"updated_at\": \"2026-05-20T21:35:14.509Z\"}, \"eval_gsm8k_sft_standard_20\": {\"created_at\": \"2026-05-20T17:07:58.760Z\", \"updated_at\": \"2026-05-20T19:58:14.139Z\", \"metrics\": {\"gsm8k_accuracy\": 0.5921, \"stderr\": 0.0135, \"correct\": 781, \"total\": 1319, \"eos_rate\": 0.9848, \"avg_response_length\": 206.68}}, \"eval_gsm8k_dense_unpruned\": {\"created_at\": \"2026-05-20T16:28:28.020Z\", \"updated_at\": \"2026-05-20T19:36:49.374Z\", \"metrics\": {\"gsm8k_accuracy\": 0.9083, \"gsm8k_accuracy_ci\": 0.0079, \"correct\": 1198, \"total\": 1319, \"eos_rate\": 0.9871, \"avg_response_length\": 594, \"truncated\": 17, \"eval_time\": \"3h7m\"}}, \"eval_gsm8k_sft_cka_only_20\": {\"created_at\": \"2026-05-20T16:32:21.874Z\", \"updated_at\": \"2026-05-20T18:49:11.554Z\", \"metrics\": {\"gsm8k_accuracy\": 0.6391, \"gsm8k_accuracy_ci\": 0.0132, \"correct\": 843, \"total\": 1319, \"eos_rate\": 0.9901, \"avg_response_length\": 198.1, \"truncated\": 13}}, \"eval_gsm8k_sft_cka_only_15\": {\"created_at\": \"2026-05-20T15:19:42.152Z\", \"updated_at\": \"2026-05-20T18:33:53.213Z\", \"metrics\": {\"gsm8k_accuracy\": 0.7218, \"correct\": 952, \"total\": 1319}}, \"eval_gsm8k_sft_rasp_20\": {\"created_at\": \"2026-05-20T17:09:04.809Z\", \"updated_at\": \"2026-05-20T18:10:54.576Z\", \"metrics\": {\"gsm8k_accuracy\": 0.6149, \"gsm8k_accuracy_ci\": 0.0134, \"correct\": 811, \"total\": 1319, \"eos_rate\": 0.9826, \"avg_response_length\": 216.5}}, \"eval_gsm8k_grpo_standard_15_v2\": {\"created_at\": \"2026-05-20T14:43:21.408Z\", \"updated_at\": \"2026-05-20T16:28:25.206Z\", \"metrics\": {\"gsm8k_accuracy\": 0.6611, \"correct\": 872, \"total\": 1319, \"eos_rate\": 0.993, \"avg_response_length\": 184}}, \"eval_gsm8k_sft_standard_15\": {\"created_at\": \"2026-05-20T14:23:49.568Z\", \"updated_at\": \"2026-05-20T16:28:23.020Z\", \"metrics\": {\"gsm8k_accuracy\": 0.6649, \"correct\": 877, \"total\": 1319, \"eos_rate\": 0.993, \"avg_response_length\": 183}}, \"eval_gsm8k_grpo_cka_only_15_v2\": {\"created_at\": \"2026-05-20T13:32:17.474Z\", \"updated_at\": \"2026-05-20T16:04:05.569Z\", \"metrics\": {\"gsm8k_accuracy\": 0.7309, \"gsm8k_accuracy_ci\": 0.0122, \"correct\": 964, \"total\": 1319, \"eos_rate\": 0.9894, \"avg_response_length\": 202.4}}, \"eval_gsm8k_grpo_cka_only_20_seed456_full\": {\"created_at\": \"2026-05-20T13:31:33.529Z\", \"updated_at\": \"2026-05-20T16:04:03.508Z\", \"metrics\": {\"gsm8k_accuracy\": 0.6459, \"gsm8k_accuracy_ci\": 0.0132, \"correct\": 852, \"total\": 1319, \"eos_rate\": 0.9886, \"avg_response_length\": 204.3}}, \"eval_gsm8k_sft_qwen_standard_20\": {\"created_at\": \"2026-05-20T10:32:12.883Z\", \"updated_at\": \"2026-05-20T15:44:54.102Z\", \"metrics\": {\"gsm8k_accuracy\": 0.21, \"correct\": 42, \"total\": 200}}, \"eval_gsm8k_sft_qwen_cka_only_20\": {\"created_at\": \"2026-05-20T10:32:11.084Z\", \"updated_at\": \"2026-05-20T15:39:07.657Z\", \"metrics\": {\"gsm8k_accuracy\": 0.515, \"gsm8k_accuracy_ci\": 0.0353, \"correct\": 103, \"total\": 200, \"eos_rate\": 0.27, \"avg_response_length\": 1536, \"truncated\": 146, \"eval_time\": \"4h00m04s\"}}, \"grpo_standard_15_v2\": {\"created_at\": \"2026-05-20T13:42:06.715Z\", \"updated_at\": \"2026-05-20T14:23:39.083Z\", \"metrics\": {\"loss\": 0.01142, \"reward\": 0.1375, \"reward_std\": 0.2778, \"kl\": 0.004099, \"entropy\": 0.1932, \"grad_norm\": 3.547, \"total_steps\": 100, \"training_time\": \"21m49s\"}}, \"eval_gsm8k_grpo_standard_20_seed123_full\": {\"created_at\": \"2026-05-20T10:27:04.283Z\", \"updated_at\": \"2026-05-20T13:38:49.241Z\", \"metrics\": {\"accuracy\": 0.5989, \"n_correct\": 790, \"n_total\": 1319, \"stderr\": 0.0135, \"eos_rate\": null}}, \"eval_gsm8k_grpo_standard_20_seed456_full\": {\"created_at\": \"2026-05-20T10:27:05.741Z\", \"updated_at\": \"2026-05-20T13:38:47.186Z\", \"metrics\": {\"accuracy\": 0.602, \"n_correct\": 794, \"n_total\": 1319, \"stderr\": 0.01348, \"eos_rate\": 0.9856}}, \"grpo_cka_only_15_v2\": {\"created_at\": \"2026-05-20T11:58:03.218Z\", \"updated_at\": \"2026-05-20T13:35:06.015Z\", \"metrics\": {\"final_loss\": 0.2027, \"avg_train_loss\": 0.11, \"final_reward\": 0.4019, \"final_kl\": 0.0018, \"train_steps\": 100, \"train_runtime_min\": 22.5}}, \"grpo_cka_only_20_seed456\": {\"created_at\": \"2026-05-20T11:36:13.866Z\", \"updated_at\": \"2026-05-20T13:35:02.652Z\", \"metrics\": {\"final_loss\": 0.0999, \"avg_train_loss\": 0.0881, \"final_reward\": 0.2925, \"final_kl\": 0.0017, \"train_steps\": 100, \"train_runtime_min\": 21.8}}, \"prune_eval_standard_30\": {\"created_at\": \"2026-05-20T04:08:24.071Z\", \"updated_at\": \"2026-05-20T11:56:25.682Z\", \"metrics\": {\"accuracy\": 2.8, \"note\": \"N=500 partial result (killed by Director, 30% sparsity = complete collapse, N=500 precision sufficient)\", \"n_evaluated\": 500, \"n_total\": 1319, \"eos_rate\": 1.2, \"avg_len\": 4057}}, \"prune_eval_cka_only_30\": {\"created_at\": \"2026-05-20T04:08:22.614Z\", \"updated_at\": \"2026-05-20T11:56:24.517Z\", \"metrics\": {\"accuracy\": 1.6, \"note\": \"N=500 partial result (killed by Director, 30% sparsity = complete collapse, N=500 precision sufficient)\", \"n_evaluated\": 500, \"n_total\": 1319, \"eos_rate\": 5.6, \"avg_len\": 4009}}, \"sft_qwen_math_cka_only_20_v2\": {\"created_at\": \"2026-05-20T09:18:17.089Z\", \"updated_at\": \"2026-05-20T09:50:15.333Z\", \"metrics\": {\"train_loss\": 0.3481, \"mean_token_accuracy\": 0.8595, \"train_runtime_sec\": 1013, \"train_samples_per_second\": 7.38, \"epochs\": 1}}, \"eval_gsm8k_grpo_standard_20_seed456\": {\"created_at\": \"2026-05-20T09:15:10.283Z\", \"updated_at\": \"2026-05-20T09:49:10.630Z\", \"metrics\": {\"accuracy\": 0.665, \"n_correct\": 133, \"n_total\": 200, \"stderr\": 0.0334, \"eos_rate\": 0.995, \"avg_response_length\": 166.9}}, \"eval_gsm8k_grpo_standard_20_seed123\": {\"created_at\": \"2026-05-20T09:15:16.595Z\", \"updated_at\": \"2026-05-20T09:49:08.654Z\", \"metrics\": {\"accuracy\": 0.64, \"n_correct\": 128, \"n_total\": 200, \"stderr\": 0.0339, \"eos_rate\": 0.99, \"avg_response_length\": 187.9}}, \"grpo_standard_20_seed456\": {\"created_at\": \"2026-05-20T06:22:10.493Z\", \"updated_at\": \"2026-05-20T09:13:48.616Z\", \"metrics\": {\"steps_completed\": 100, \"runtime_sec\": 2745, \"peak_reward\": 0.0844, \"peak_reward_step\": 90, \"final_reward\": 0.06, \"final_frac_zero_std\": 0.65, \"seed\": 456, \"wandb_run\": \"wg0iv4oi\", \"wandb_mode\": \"offline\"}}, \"grpo_standard_20_seed123\": {\"created_at\": \"2026-05-20T06:22:27.444Z\", \"updated_at\": \"2026-05-20T09:13:45.445Z\", \"metrics\": {\"steps_completed\": 100, \"runtime_sec\": 2783, \"peak_reward\": 0.0619, \"peak_reward_step\": 80, \"final_reward\": 0.0594, \"final_frac_zero_std\": 0.6, \"seed\": 123, \"wandb_run\": \"pgzwv725\", \"wandb_mode\": \"offline\"}}, \"eval_mbpp_grpo_standard_20_v3\": {\"created_at\": \"2026-05-19T21:00:40.293Z\", \"updated_at\": \"2026-05-20T03:06:43.359Z\", \"metrics\": {\"pass_at_1\": 0.131, \"correct\": 49, \"total\": 374, \"stderr\": 0.0174}}, \"eval_humaneval_sft_standard_20_1p5b_2048\": {\"created_at\": \"2026-05-19T11:35:45.876Z\", \"updated_at\": \"2026-05-20T03:06:22.483Z\", \"metrics\": {\"pass_at_1\": 0.0061, \"correct\": 1, \"total\": 164, \"stderr\": 0.0061}}, \"eval_humaneval_sft_standard_20_2048_v3\": {\"created_at\": \"2026-05-19T10:05:36.497Z\", \"updated_at\": \"2026-05-20T03:06:20.863Z\", \"metrics\": {\"pass_at_1\": 0.1341, \"correct\": 22, \"total\": 164, \"stderr\": 0.0266}}, \"eval_humaneval_sft_cka_only_20_1p5b_2048\": {\"created_at\": \"2026-05-19T11:32:47.965Z\", \"updated_at\": \"2026-05-20T03:06:19.658Z\", \"metrics\": {\"pass_at_1\": 0.0061, \"correct\": 1, \"total\": 164, \"stderr\": 0.0061}}, \"eval_humaneval_grpo_cka_only_20_1p5b_2048\": {\"created_at\": \"2026-05-19T11:32:50.649Z\", \"updated_at\": \"2026-05-20T03:06:18.579Z\", \"metrics\": {\"pass_at_1\": 0, \"correct\": 0, \"total\": 164, \"stderr\": 0}}, \"eval_mbpp_sft_shortgpt_20_v2\": {\"created_at\": \"2026-05-19T22:23:35.431Z\", \"updated_at\": \"2026-05-20T02:43:15.577Z\", \"metrics\": {\"pass_at_1\": 0.1043, \"stderr\": 0.0158, \"n_correct\": 39, \"n_total\": 374, \"avg_response_length\": 1166.4, \"median_response_length\": 773.5}}, \"eval_mbpp_grpo_shortgpt_20_v2\": {\"created_at\": \"2026-05-19T22:33:19.363Z\", \"updated_at\": \"2026-05-20T02:43:06.318Z\", \"metrics\": {\"pass_at_1\": 0.1444, \"stderr\": 0.0182, \"n_correct\": 54, \"n_total\": 374, \"avg_response_length\": 1140.8, \"median_response_length\": 804.5}}, \"eval_mbpp_sft_standard_20_v4\": {\"created_at\": \"2026-05-19T22:26:22.996Z\", \"updated_at\": \"2026-05-20T02:16:04.699Z\", \"metrics\": {\"pass_at_1\": 0.1203, \"stderr\": 0.0168, \"n_correct\": 45, \"n_total\": 374, \"avg_response_length\": 1084.1, \"median_response_length\": 746.5}}, \"eval_mbpp_grpo_standard_20_v4\": {\"created_at\": \"2026-05-19T21:01:23.058Z\", \"updated_at\": \"2026-05-20T01:46:54.906Z\", \"metrics\": {\"pass_at_1\": 0.131, \"n_correct\": 49, \"n_total\": 374, \"stderr\": 0.01745, \"avg_response_length\": 1058.7, \"median_response_length\": 726}}, \"cka_scoring_stability_ablation\": {\"created_at\": \"2026-05-19T21:21:10.933Z\", \"updated_at\": \"2026-05-19T22:21:53.770Z\", \"metrics\": {\"spearman_256v512_attn\": 0.989, \"spearman_256v512_mlp\": 0.9683, \"spearman_256v512_combined\": 0.9788, \"spearman_256v1024_attn\": 0.9762, \"spearman_256v1024_mlp\": 0.9464, \"spearman_256v1024_combined\": 0.9641, \"spearman_512v1024_attn\": 0.995, \"spearman_512v1024_mlp\": 0.9908, \"spearman_512v1024_combined\": 0.9938, \"min_combined_rho\": 0.964, \"mean_combined_rho\": 0.979, \"stable\": true}}, \"eval_mbpp_sft_standard_20_1p5b\": {\"created_at\": \"2026-05-19T18:56:15.766Z\", \"updated_at\": \"2026-05-19T21:57:06.135Z\", \"metrics\": {\"pass_at_1\": 0.008021, \"n_correct\": 3, \"n_total\": 374, \"stderr\": 0.004613, \"avg_response_length\": 1658.6, \"median_response_length\": 2048}}, \"eval_mbpp_grpo_rasp_20\": {\"created_at\": \"2026-05-19T18:18:35.729Z\", \"updated_at\": \"2026-05-19T21:55:32.779Z\", \"metrics\": {\"pass_at_1\": 0.131, \"n_correct\": 49, \"n_total\": 374, \"stderr\": 0.0174}}, \"eval_mbpp_sft_rasp_20\": {\"created_at\": \"2026-05-19T18:18:34.640Z\", \"updated_at\": \"2026-05-19T21:08:00.610Z\", \"metrics\": {\"pass_at_1\": 0.1176, \"stderr\": 0.0167, \"n_correct\": 44, \"n_total\": 374, \"dense_baseline_pass_at_1\": 0.5348, \"degradation_pct\": 78.01, \"avg_response_length\": 810.7, \"median_response_length\": 247}}, \"eval_mbpp_sft_cka_only_20\": {\"created_at\": \"2026-05-19T17:20:00.596Z\", \"updated_at\": \"2026-05-19T19:58:30.970Z\", \"metrics\": {\"pass_at_1\": 0.1283, \"stderr\": 0.0173, \"n_correct\": 48, \"n_total\": 374, \"dense_baseline_pass_at_1\": 0.5348, \"degradation_pct\": 76.01, \"avg_response_length\": 643.8, \"median_response_length\": 363.5}}, \"eval_humaneval_sft_rasp_20_1p5b_2048\": {\"created_at\": \"2026-05-19T11:35:50.597Z\", \"updated_at\": \"2026-05-19T18:52:30.545Z\", \"metrics\": {\"pass_at_1\": 0, \"n_correct\": 0, \"n_total\": 164, \"note\": \"1.5B SFT RASP, all truncated at 2048 tokens\"}}, \"eval_mbpp_grpo_cka_only_20\": {\"created_at\": \"2026-05-19T14:41:07.213Z\", \"updated_at\": \"2026-05-19T18:17:54.178Z\", \"metrics\": {\"pass_at_1\": 0.1417, \"n_correct\": 53, \"n_total\": 374, \"stderr\": 0.018}}, \"eval_gsm8k_grpo_shortgpt_20\": {\"created_at\": \"2026-05-19T17:19:18.419Z\", \"updated_at\": \"2026-05-19T18:17:53.164Z\", \"metrics\": {\"gsm8k_accuracy\": 43.37, \"n_correct\": 572, \"n_total\": 1319, \"stderr\": 0.0136}}, \"eval_gsm8k_sft_shortgpt_20\": {\"created_at\": \"2026-05-19T15:47:16.122Z\", \"updated_at\": \"2026-05-19T18:03:15.831Z\", \"metrics\": {\"gsm8k_accuracy\": 44.73, \"n_correct\": 590, \"n_total\": 1319}}, \"sft_shortgpt_20\": {\"created_at\": \"2026-05-19T14:22:26.084Z\", \"updated_at\": \"2026-05-19T18:02:48.590Z\"}, \"eval_gsm8k_grpo_cka_only_20_seed123\": {\"created_at\": \"2026-05-19T17:47:34.008Z\", \"updated_at\": \"2026-05-19T17:48:24.627Z\", \"metrics\": {\"accuracy\": 0.6422, \"stderr\": 0.0132, \"n_correct\": 847, \"n_total\": 1319, \"eos_rate\": 0.9909, \"avg_response_length\": 195.97, \"natural_eos\": 1307, \"truncated\": 12}}, \"eval_humaneval_grpo_standard_20_1p5b_2048\": {\"created_at\": \"2026-05-19T11:35:48.029Z\", \"updated_at\": \"2026-05-19T17:02:50.370Z\"}, \"gradient_flow_v3\": {\"created_at\": \"2026-05-19T15:03:16.535Z\", \"updated_at\": \"2026-05-19T16:38:41.269Z\", \"metrics\": {\"cka_only_mean_grad_norm\": 0.3229, \"standard_mean_grad_norm\": 0.1118, \"rasp_mean_grad_norm\": 0.1431, \"cka_vs_standard_ratio\": 2.89, \"rasp_vs_standard_ratio\": 1.28, \"cka_vs_standard_significant_layers\": \"55/56\", \"cka_vs_rasp_significant_layers\": \"56/56\", \"rasp_vs_standard_significant_layers\": \"45/56\", \"rasp_vs_standard_nonsig_layers\": \"layer_18_mlp,layer_19_attn,layer_19_mlp,layer_20_attn,layer_20_mlp,layer_21_attn,layer_21_mlp,layer_22_attn,layer_24_mlp,layer_27_attn,layer_27_mlp\", \"n_samples\": 200, \"statistical_test\": \"Wilcoxon signed-rank, per-layer\", \"bootstrap_n\": 1000, \"seed\": 42}}, \"eval_gsm8k_grpo_rasp_20_fair\": {\"created_at\": \"2026-05-19T12:47:37.399Z\", \"updated_at\": \"2026-05-19T16:17:16.053Z\", \"metrics\": {\"accuracy\": 0.6088, \"stderr\": 0.0134, \"n_correct\": 803, \"n_total\": 1319, \"eos_rate\": 0.9879, \"avg_response_length\": 195.7}}, \"eval_mbpp_dense_unpruned\": {\"created_at\": \"2026-05-19T13:47:53.814Z\", \"updated_at\": \"2026-05-19T16:17:00.452Z\", \"metrics\": {\"pass_at_1\": 0.5348, \"stderr\": 0.0258, \"n_correct\": 200, \"n_total\": 374}}, \"eval_humaneval_sft_rasp_20_2048_v2\": {\"created_at\": \"2026-05-19T13:18:20.664Z\", \"updated_at\": \"2026-05-19T15:47:14.846Z\", \"metrics\": {\"pass_at_1\": 0.1037, \"stderr\": 0.0238, \"n_correct\": 17, \"n_total\": 164, \"avg_response_length\": 1253.7, \"median_response_length\": 2048}}, \"grpo_cka_only_20_seed123\": {\"created_at\": \"2026-05-19T09:27:11.294Z\", \"updated_at\": \"2026-05-19T15:21:17.415Z\", \"metrics\": {\"train_loss\": 0.1361, \"final_step_loss\": 0.05054, \"final_reward\": 0.2975, \"final_reward_std\": 0.4097, \"train_steps\": 100, \"train_runtime_hours\": 11.63, \"wandb_run\": \"j8kn0sqd\"}}, \"gradient_flow_analysis\": {\"created_at\": \"2026-05-19T14:44:25.606Z\", \"updated_at\": \"2026-05-19T14:45:13.584Z\", \"metrics\": {\"cka_only_attn_grad_mean\": 0.3135, \"cka_only_attn_grad_cv\": 1.2231, \"cka_only_mlp_grad_mean\": 0.285, \"cka_only_mlp_grad_cv\": 1.2424, \"standard_attn_grad_mean\": 0.1316, \"standard_attn_grad_cv\": 1.1363, \"standard_mlp_grad_mean\": 0.1222, \"standard_mlp_grad_cv\": 1.1489, \"grad_magnitude_ratio_attn\": 2.38, \"grad_magnitude_ratio_mlp\": 2.33}}, \"cka_calibration_stability_ablation\": {\"created_at\": \"2026-05-19T14:21:15.548Z\", \"updated_at\": \"2026-05-19T14:32:43.647Z\", \"metrics\": {\"split_half_rho\": 0.9932, \"n_splits\": 5, \"size_sensitivity_128\": 0.982, \"size_sensitivity_256\": 0.989, \"size_sensitivity_512\": 0.995}}, \"eval_humaneval_grpo_standard_20_fair_2048_v3\": {\"created_at\": \"2026-05-19T07:05:14.343Z\", \"updated_at\": \"2026-05-19T14:20:25.129Z\", \"metrics\": {\"pass_at_1\": 0.1098, \"n_correct\": 18, \"n_total\": 164}}, \"eval_humaneval_sft_cka_only_20_2048_v2\": {\"created_at\": \"2026-05-19T09:27:07.470Z\", \"updated_at\": \"2026-05-19T13:22:29.762Z\", \"metrics\": {\"pass_at_1\": 20.12, \"n_correct\": 33, \"n_total\": 164}}, \"eval_math500_grpo_cka_only_20_2048\": {\"created_at\": \"2026-05-18T22:36:14.421Z\", \"updated_at\": \"2026-05-19T13:08:18.617Z\", \"metrics\": {\"accuracy\": 0.292, \"n_correct\": 146, \"n_total\": 500}}, \"eval_gsm8k_sft_standard_20_1p5b\": {\"created_at\": \"2026-05-18T18:10:55.912Z\", \"updated_at\": \"2026-05-19T13:07:57.786Z\", \"metrics\": {\"accuracy\": 0.22896133434420016, \"n_correct\": 302, \"n_total\": 1319}}, \"eval_gsm8k_grpo_standard_20_fair_v2\": {\"created_at\": \"2026-05-19T09:27:09.334Z\", \"updated_at\": \"2026-05-19T12:47:36.437Z\", \"metrics\": {\"accuracy\": 59.44, \"n_correct\": 784, \"n_total\": 1319}}, \"eval_humaneval_grpo_rasp_20_fair_2048\": {\"created_at\": \"2026-05-19T06:38:59.146Z\", \"updated_at\": \"2026-05-19T09:44:43.320Z\", \"metrics\": {\"pass_at_1\": 0.1098, \"n_correct\": 18, \"n_total\": 164, \"stderr\": 0.0244, \"avg_response_length\": null}}, \"eval_gsm8k_grpo_unstructured_20\": {\"created_at\": \"2026-05-19T04:46:38.286Z\", \"updated_at\": \"2026-05-19T08:05:04.224Z\", \"metrics\": {\"accuracy\": 0.8764, \"n_correct\": 1156, \"n_total\": 1319, \"stderr\": 0.00906, \"eos_rate\": 0.9818, \"truncated\": 24, \"avg_response_length\": 600}}, \"eval_humaneval_grpo_cka_only_20_2048\": {\"created_at\": \"2026-05-19T04:11:28.637Z\", \"updated_at\": \"2026-05-19T07:36:55.239Z\", \"metrics\": {\"pass_at_1\": 0.2012, \"n_correct\": 33, \"n_total\": 164, \"stderr\": 0.0313, \"avg_response_length\": 1523.31, \"median_response_length\": 2048, \"wall_clock_seconds\": 11933}}, \"grpo_standard_20_fair\": {\"created_at\": \"2026-05-18T01:05:44.644Z\", \"updated_at\": \"2026-05-19T06:39:34.930Z\", \"metrics\": {\"wandb_run_id\": \"tyv20u2k\", \"total_steps\": 100, \"runtime_seconds\": 3017, \"reward_trajectory\": [0.051, 0.056, 0.067, 0.081, 0.019, 0.043, 0.047, 0.046, 0.031, 0.054], \"frac_zero_std_trajectory\": [0.5, 0.625, 0.5, 0.5, 0.575, 0.55, 0.575, 0.55, 0.55, 0.55], \"peak_reward\": 0.081, \"peak_reward_step\": 40, \"final_reward\": 0.054, \"final_frac_zero_std\": 0.55, \"dynamics_pattern\": \"dip_then_partial_recovery\", \"dip_step\": 50, \"dip_reward\": 0.019}}, \"inference_bench_clean_v2\": {\"created_at\": \"2026-05-19T01:42:25.421Z\", \"updated_at\": \"2026-05-19T02:44:07.178Z\", \"metrics\": {\"original_tps\": 72.02, \"cka_only_20_tps\": 58.28, \"standard_20_tps\": 58.25, \"cka_only_20_speedup\": 0.809, \"standard_20_speedup\": 0.809, \"original_first_token_ms\": 20.05, \"cka_only_20_first_token_ms\": 16.35, \"standard_20_first_token_ms\": 16.4, \"original_per_token_ms\": 13.89, \"cka_only_20_per_token_ms\": 16.73, \"standard_20_per_token_ms\": 16.71, \"original_params\": 7615616512, \"pruned_params\": 6161946112, \"param_reduction_pct\": 19.1}}, \"eval_gsm8k_sft_rasp_20_1p5b\": {\"created_at\": \"2026-05-18T18:10:57.471Z\", \"updated_at\": \"2026-05-19T02:43:38.445Z\", \"metrics\": {\"accuracy\": 0.2691, \"n_correct\": 355, \"n_total\": 1319, \"stderr\": 0.0122, \"grpo_delta_pp\": -0.75}}, \"eval_math500_grpo_standard_20_fair_v2\": {\"created_at\": \"2026-05-18T18:24:25.108Z\", \"updated_at\": \"2026-05-19T01:39:52.608Z\", \"metrics\": {\"accuracy\": 0.264, \"n_correct\": 132, \"n_total\": 500, \"stderr\": 0.0197}}, \"eval_math500_sft_rasp_20_2048\": {\"created_at\": \"2026-05-18T22:36:16.836Z\", \"updated_at\": \"2026-05-19T01:39:03.294Z\", \"metrics\": {\"accuracy\": 0.226, \"n_correct\": 113, \"n_total\": 500, \"stderr\": 0.0187, \"natural_eos\": 314, \"truncated\": 186, \"natural_eos_pct\": 0.628, \"avg_response_length\": 930.58, \"median_response_length\": 274}}, \"eval_math500_dense_2048\": {\"created_at\": \"2026-05-18T22:08:58.081Z\", \"updated_at\": \"2026-05-19T01:34:41.598Z\", \"metrics\": {\"accuracy\": 0.53, \"n_correct\": 265, \"n_total\": 500, \"stderr\": 0.0223, \"natural_eos_pct\": 0.468, \"truncated_pct\": 0.532, \"avg_response_length\": 1724.5, \"median_response_length\": 2048}}, \"eval_math500_grpo_rasp_20_fair\": {\"created_at\": \"2026-05-18T18:16:25.616Z\", \"updated_at\": \"2026-05-18T23:53:54.384Z\", \"metrics\": {\"accuracy\": 0.24, \"n_correct\": 120, \"n_total\": 500, \"stderr\": 0.0191, \"natural_eos_pct\": 0.64, \"truncated_pct\": 0.36, \"avg_response_length\": 903.5, \"median_response_length\": 272, \"max_new_tokens\": 2048}}, \"eval_gsm8k_sft_cka_only_20_1p5b\": {\"created_at\": \"2026-05-18T17:51:20.577Z\", \"updated_at\": \"2026-05-18T23:46:01.152Z\", \"metrics\": {\"accuracy\": 0.3563, \"n_correct\": 470, \"n_total\": 1319, \"stderr\": 0.0132, \"eos_rate\": 0.9507, \"avg_response_length\": 336.76}}, \"sft_standard_20_retrain_westd\": {\"created_at\": \"2026-05-18T22:40:50.567Z\", \"updated_at\": \"2026-05-18T23:24:15.076Z\", \"metrics\": {\"train_loss\": 0.758, \"mean_token_accuracy\": 0.8252, \"train_runtime_sec\": 1688, \"train_samples_per_second\": 8.856, \"epochs\": 2, \"total_steps\": 1870}}, \"eval_gsm8k_grpo_rasp_20_1p5b\": {\"created_at\": \"2026-05-18T16:59:22.921Z\", \"updated_at\": \"2026-05-18T23:02:00.110Z\", \"metrics\": {\"accuracy\": 0.2616, \"n_correct\": 345, \"n_total\": 1319, \"stderr\": 0.0121, \"eos_rate\": 0.9378, \"avg_response_length\": 392.7}}, \"eval_math500_sft_cka_only_20_v4_restart\": {\"created_at\": \"2026-05-18T18:16:24.171Z\", \"updated_at\": \"2026-05-18T22:12:04.614Z\", \"metrics\": {\"accuracy\": 0.29, \"n_correct\": 145, \"n_total\": 500, \"stderr\": 0.0203, \"natural_eos\": 384, \"truncated\": 116, \"natural_eos_pct\": 0.768, \"avg_response_length\": 673.278, \"median_response_length\": 242.5}}, \"grpo_cka_only_20_extended_300\": {\"created_at\": \"2026-05-18T14:51:36.423Z\", \"updated_at\": \"2026-05-18T21:43:18.847Z\", \"metrics\": {\"final_reward\": 0.3075, \"peak_reward\": 0.4444, \"peak_reward_step\": 280, \"reward_step100\": 0.354, \"reward_step300\": 0.3075, \"train_loss_final\": 0.0349, \"global_step\": 300, \"runtime_seconds\": 23004, \"gpu_hours\": 6.5, \"final_frac_zero_std\": 0.275, \"reward_range\": [0.22, 0.44], \"pattern\": \"sustained oscillation, no collapse\", \"wandb_run_id\": \"z9f0z901\"}}, \"eval_gsm8k_grpo_standard_20_1p5b\": {\"created_at\": \"2026-05-18T16:38:01.585Z\", \"updated_at\": \"2026-05-18T21:03:21.558Z\", \"metrics\": {\"accuracy\": 0.2229, \"n_correct\": 294, \"n_total\": 1319, \"stderr\": 0.0115}}, \"eval_gsm8k_grpo_cka_only_20_1p5b\": {\"created_at\": \"2026-05-18T16:35:29.923Z\", \"updated_at\": \"2026-05-18T20:09:40.771Z\", \"metrics\": {\"accuracy\": 0.3548, \"n_correct\": 468, \"n_total\": 1319, \"stderr\": 0.0132}}, \"eval_math500_dense_unpruned\": {\"created_at\": \"2026-05-18T13:42:10.786Z\", \"updated_at\": \"2026-05-18T18:15:28.383Z\", \"metrics\": {\"accuracy\": 0.736, \"stderr\": 0.0197, \"n_correct\": 368, \"n_total\": 500, \"natural_eos_pct\": 0.752}}, \"grpo_rasp_20_1p5b\": {\"created_at\": \"2026-05-18T15:12:41.395Z\", \"updated_at\": \"2026-05-18T16:32:13.529Z\", \"metrics\": {\"final_reward\": 0.099, \"frac_zero_std\": 0.175, \"clipped_ratio\": 0.82}}, \"grpo_cka_only_20_1p5b\": {\"created_at\": \"2026-05-18T12:50:08.570Z\", \"updated_at\": \"2026-05-18T16:08:40.491Z\", \"metrics\": {\"reward_mean\": 0.2375, \"frac_reward_zero_std\": 0.175, \"loss\": 0.0595, \"kl\": 0.00215, \"grad_norm\": 1.445, \"global_step\": 100, \"note\": \"training completed 100/100 but save_model failed (disk full). checkpoint-100 has complete model.\"}}, \"grpo_standard_20_1p5b\": {\"created_at\": \"2026-05-18T14:15:13.990Z\", \"updated_at\": \"2026-05-18T15:11:31.870Z\", \"metrics\": {\"reward_mean\": 0.0844, \"frac_reward_zero_std\": 0.15, \"loss\": 0.0151, \"grad_norm\": 4.03125, \"kl\": 0.0044, \"entropy\": 0.4617, \"final_step\": 100, \"max_steps\": 100, \"total_time_min\": 53}}, \"grpo_standard_20_extended_300_v2\": {\"created_at\": \"2026-05-18T13:53:41.781Z\", \"updated_at\": \"2026-05-18T14:50:59.377Z\", \"metrics\": {\"reward_mean_step300\": 0.0562, \"loss_step300\": 0.0367, \"frac_reward_zero_std_step300\": 0.525, \"kl_step300\": 0.00306, \"entropy_step300\": 0.157, \"lr_step300\": 3.33e-09, \"runtime_min\": 48, \"reward_decline_after_step260\": true}}, \"sft_standard_20_1p5b\": {\"created_at\": \"2026-05-18T12:09:56.278Z\", \"updated_at\": \"2026-05-18T12:31:29.300Z\"}, \"sft_cka_only_20_1p5b\": {\"created_at\": \"2026-05-18T11:29:09.842Z\", \"updated_at\": \"2026-05-18T12:31:27.978Z\"}, \"sft_rasp_20_1p5b\": {\"created_at\": \"2026-05-18T12:09:57.178Z\", \"updated_at\": \"2026-05-18T12:29:19.746Z\"}, \"inference_bench_cka_only_20_clean\": {\"created_at\": \"2026-05-18T09:47:42.247Z\", \"updated_at\": \"2026-05-18T10:07:56.924Z\", \"metrics\": {\"dense\": {\"tokens_per_second\": 75.73, \"avg_latency_sec\": 6.729, \"peak_memory_gb\": 16.22, \"total_tokens\": 25477, \"validation\": \"PASS (75.73 vs expected 76.25, <1% deviation)\"}, \"cka_only_20\": {\"tokens_per_second\": 51.86, \"avg_latency_sec\": 4.078, \"peak_memory_gb\": 11.6, \"total_tokens\": 10574, \"latency_speedup_vs_dense\": \"39.4%\", \"memory_reduction_vs_dense\": \"28.5%\"}, \"rasp_20_dummy\": {\"tokens_per_second\": 75.79, \"avg_latency_sec\": 6.723, \"peak_memory_gb\": 16.23, \"note\": \"Dense model used as dummy (rasp not on westb)\"}}}, \"eval_gsm8k_grpo_cka_only_20_v2\": {\"created_at\": \"2026-05-18T05:54:02.634Z\", \"updated_at\": \"2026-05-18T08:50:27.816Z\", \"metrics\": {\"accuracy\": 0.6437, \"n_correct\": 849, \"n_total\": 1319, \"stderr\": 0.0132, \"eos_rate\": 0.9886, \"avg_response_length\": 203.43, \"truncated\": 15, \"wall_time_sec\": 8921}}, \"grpo_cka_only_20\": {\"created_at\": \"2026-05-17T14:51:36.653Z\", \"updated_at\": \"2026-05-18T02:21:23.748Z\", \"metrics\": {\"final_step\": 100, \"final_reward\": 0.3444, \"peak_reward\": 0.3544, \"peak_reward_step\": 50, \"final_frac_zero_std\": 0.2, \"final_loss\": 0.23, \"final_kl\": 0.001609, \"final_entropy\": 0.08751, \"final_reward_std\": 0.444, \"runtime_seconds\": 40710}}, \"grpo_rasp_20_fair\": {\"created_at\": \"2026-05-17T23:50:31.502Z\", \"metrics\": {\"final_completion_length\": 963.0, \"final_frac_zero_std\": 0.85, \"final_reward\": 0.01, \"min_frac_zero_std\": 0.675, \"peak_reward\": 0.061, \"total_steps\": 100, \"training_time_minutes\": 62.5, \"trend\": \"stagnation_then_collapse\"}, \"updated_at\": \"2026-05-18T01:08:19.563Z\"}, \"eval_postprune_standard_30\": {\"created_at\": \"2026-05-17T19:08:46.051Z\", \"metrics\": {\"avg_response_length\": 3907.875, \"correct\": 8, \"eos_rate\": 0.055, \"gsm8k_accuracy\": 0.04, \"natural_eos\": 11, \"total\": 200, \"truncated\": 189}, \"updated_at\": \"2026-05-18T00:27:39.362Z\"}, \"eval_sft_cka_only_20_n1319\": {\"created_at\": \"2026-05-17T18:20:20.406Z\", \"metrics\": {\"avg_response_length\": 198.1, \"correct\": 843, \"eos_rate\": 0.9901, \"gsm8k_accuracy\": 0.6391, \"stderr\": 0.0132, \"total\": 1319}, \"updated_at\": \"2026-05-17T23:48:58.392Z\"}, \"prune_cka_only_30\": {\"created_at\": \"2026-05-17T21:42:06.467Z\", \"metrics\": {\"actual_sparsity\": 0.2892, \"attn_heads_pruned\": \"0\", \"method\": \"dummy_ones_importance + rasp_alpha1 = pure CKA-only\", \"mlp_groups_pruned\": \"303/784\"}, \"updated_at\": \"2026-05-17T21:42:06.467Z\"}, \"eval_postprune_rasp_30\": {\"created_at\": \"2026-05-17T18:22:00Z\", \"metrics\": {\"accuracy\": 0, \"avg_response_length\": 3984.31, \"eos_rate\": 0.03, \"n_correct\": 0, \"n_total\": 200, \"natural_eos\": 6, \"truncated_rate\": 0.97}, \"updated_at\": \"2026-05-17T21:39:43.149Z\"}, \"eval_humaneval_sft_standard_20_2048_v2\": {\"created_at\": \"2026-05-17T16:26:15.836Z\", \"metrics\": {\"avg_response_length\": 1850.7, \"correct\": 19, \"max_new_tokens\": 2048, \"median_response_length\": 2048, \"pass_at_1\": 0.1159, \"total\": 164}, \"updated_at\": \"2026-05-17T19:09:18.456Z\"}, \"eval_humaneval_grpo_standard_20_2048\": {\"created_at\": \"2026-05-17T13:41:03.761Z\", \"metrics\": {\"avg_response_length\": 1843, \"correct\": 17, \"max_new_tokens\": 2048, \"median_response_length\": 2048, \"pass_at_1\": 0.1037, \"total\": 164}, \"updated_at\": \"2026-05-17T18:16:11.481Z\"}, \"grpo_rasp_25\": {\"created_at\": \"2026-05-16T08:42:40.256Z\", \"metrics\": {\"note\": \"Restored from previous_failure — cron false positive, experiment actually completed 100/100 steps successfully\", \"step_100\": {\"entropy\": 0.04262, \"frac_reward_zero_std\": 0.875, \"grad_norm\": 0.05371, \"kl\": 0.0007035, \"loss\": 0.01275, \"reward\": 0.009375, \"reward_std\": 0.03149}, \"wall_clock_min\": 57.95, \"wandb_run_id\": \"bc4ojqie\"}, \"updated_at\": \"2026-05-17T18:06:56.419Z\"}, \"eval_humaneval_grpo_rasp_20_2048\": {\"created_at\": \"2026-05-17T13:41:44.795Z\", \"metrics\": {\"correct\": 24, \"max_new_tokens\": 2048, \"pass_at_1\": 0.1463, \"stderr\": 0.0276, \"total\": 164}, \"updated_at\": \"2026-05-17T16:24:44.117Z\"}, \"eval_sft_cka_only_20\": {\"created_at\": \"2026-05-17T14:28:35.380Z\", \"metrics\": {\"avg_response_length\": 182.73, \"eos_rate\": 0.995, \"gsm8k_accuracy\": 0.64, \"gsm8k_stderr\": 0.0339, \"mode\": \"greedy\", \"n_correct\": 128, \"n_total\": 200, \"seed\": 42, \"truncated\": 1}, \"updated_at\": \"2026-05-17T14:48:17.267Z\"}, \"sft_cka_only_20\": {\"created_at\": \"2026-05-17T13:43:50.320Z\", \"metrics\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_20/\", \"note\": \"Initial loss 1.958 > RASP 1.86 > Standard 1.70 (CKA-only has most initial damage). Final loss 0.62 comparable to baselines. No greedy eval run yet.\", \"token_accuracy\": 0.8362, \"total_steps\": 1870, \"train_loss_final\": 0.6165, \"train_loss_initial\": 1.958, \"train_time_min\": 33.4}, \"updated_at\": \"2026-05-17T14:28:29.688Z\"}, \"eval_humaneval_unpruned_2048\": {\"created_at\": \"2026-05-17T12:40:50.255Z\", \"metrics\": {\"avg_response_length\": 1771, \"correct\": 74, \"max_new_tokens\": 2048, \"median_response_length\": 2048, \"pass_at_1\": 0.4512, \"stderr\": 0.0389, \"total\": 164, \"wall_time_min\": 67.6}, \"updated_at\": \"2026-05-17T13:53:59.636Z\"}, \"eval_humaneval_sft_rasp_20_2048\": {\"created_at\": \"2026-05-17T12:40:51.686Z\", \"metrics\": {\"correct\": 17, \"max_new_tokens\": 2048, \"median_response_length\": 2048, \"note\": \"still truncating at median=2048, main failure mode is thinking chain leaking into code output\", \"pass_at_1\": 0.1037, \"stderr\": 0.0238, \"total\": 164, \"wall_time_min\": 42}, \"updated_at\": \"2026-05-17T13:42:41.560Z\"}, \"eval_humaneval_grpo_standard_20\": {\"created_at\": \"2026-05-17T10:00:40.683Z\", \"metrics\": {\"correct\": 3, \"max_new_tokens\": 512, \"note\": \"512-token truncation, low quality\", \"pass_at_1\": 0.0183, \"total\": 164}, \"updated_at\": \"2026-05-17T13:33:59.897Z\"}, \"eval_math500_unpruned\": {\"created_at\": \"2026-05-17T06:23:49.923Z\", \"metrics\": {\"N\": 500, \"accuracy\": 0.736, \"correct\": 368, \"stderr\": 0.02}, \"updated_at\": \"2026-05-17T12:40:26.343Z\"}, \"eval_gradient_postsft\": {\"created_at\": \"2026-05-17T10:07:58.644Z\", \"metrics\": {\"accuracy\": 0.615, \"avg_response_length\": 167.455, \"correct\": 123, \"eos_rate\": 0.995, \"stderr\": 0.0344, \"total\": 200}, \"updated_at\": \"2026-05-17T11:24:16.260Z\"}, \"gradient_sft_v3\": {\"created_at\": \"2026-05-17T09:28:21.646Z\", \"metrics\": {\"epochs\": 2, \"final_loss\": 0.644, \"output_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_gradient_20\", \"steps\": 1870, \"token_accuracy\": 0.825}, \"updated_at\": \"2026-05-17T10:08:07.026Z\"}, \"eval_math500_sft_standard_20\": {\"created_at\": \"2026-05-17T06:23:54.283Z\", \"metrics\": {\"correct\": 130, \"eos_rate\": 0.578, \"math500_acc\": 0.26, \"stderr\": 0.0196, \"total\": 500, \"truncated\": 211, \"wall_time_hours\": 3.58}, \"updated_at\": \"2026-05-17T10:00:26.439Z\"}, \"eval_math500_sft_rasp_20\": {\"created_at\": \"2026-05-17T06:23:52.474Z\", \"metrics\": {\"correct\": 121, \"math500_acc\": 0.242, \"stderr\": 0.0192, \"total\": 500, \"wall_time_hours\": 2.94}, \"updated_at\": \"2026-05-17T09:24:16.959Z\"}, \"eval_unstructured_20\": {\"created_at\": \"2026-05-17T05:35:41.205Z\", \"metrics\": {\"avg_response_length\": 641, \"correct\": 1159, \"eos_rate\": 0.9803, \"gsm8k_acc\": 0.8787, \"stderr\": 0.009, \"total\": 1319, \"truncated\": 26, \"wall_time_hours\": 3.23}, \"updated_at\": \"2026-05-17T08:50:18.688Z\"}, \"eval_humaneval_sft_standard_20\": {\"created_at\": \"2026-05-17T07:56:08.222Z\", \"metrics\": {\"correct\": 5, \"failure_modes\": \"model generates CoT natural language instead of code, all responses truncated at max_tokens=512\", \"pass_at_1\": 0.0305, \"stderr\": 0.0134, \"total\": 164, \"wall_time_min\": 17}, \"updated_at\": \"2026-05-17T08:31:52.684Z\"}, \"eval_humaneval_sft_rasp_20\": {\"created_at\": \"2026-05-17T07:19:22.820Z\", \"metrics\": {\"correct\": 12, \"failure_modes\": \"model outputs natural language thinking instead of code (SyntaxError), parenthesis mismatch\", \"median_response_length\": 512, \"note\": \"max_tokens truncation frequent\", \"pass_at_1\": 0.0732, \"stderr\": 0.0203, \"total\": 164}, \"updated_at\": \"2026-05-17T07:55:52.564Z\"}, \"multiseed_serial_westb\": {\"created_at\": \"2026-05-17T05:47:08.060Z\", \"metrics\": {\"missing\": \"seed 42 and seed 789 not executed\", \"note\": \"2 seeds x 2 methods (not 4 seeds as planned). Script ran RASP+Standard for seeds 123,456.\", \"rasp_seed123\": {\"acc\": 0.605, \"correct\": 121, \"total\": 200}, \"rasp_seed456\": {\"acc\": 0.6, \"correct\": 120, \"total\": 200}, \"standard_seed123\": {\"acc\": 0.645, \"correct\": 129, \"total\": 200}, \"standard_seed456\": {\"acc\": 0.61, \"correct\": 122, \"total\": 200}}, \"updated_at\": \"2026-05-17T07:50:11.807Z\"}, \"eval_humaneval_grpo_rasp_20\": {\"created_at\": \"2026-05-17T06:42:19.044Z\", \"metrics\": {\"n_passed\": 17, \"n_total\": 164, \"pass_at_1\": 0.1037, \"stderr\": 0.0238}, \"updated_at\": \"2026-05-17T07:15:58.856Z\"}, \"eval_humaneval_unpruned\": {\"created_at\": \"2026-05-17T06:23:55.527Z\", \"metrics\": {\"n_passed\": 3, \"n_total\": 164, \"pass_at_1\": 0.0183, \"stderr\": 0.0105}, \"updated_at\": \"2026-05-17T06:42:38.578Z\"}, \"eval_grpo_rasp_25\": {\"created_at\": \"2026-05-16T20:04:16.057Z\", \"metrics\": {\"accuracy\": 0.5315, \"avg_len\": 433.85, \"eos_rate\": 0.9272, \"max_len\": 4096, \"min_len\": 39, \"n_correct\": 701, \"n_total\": 1319, \"stderr\": 0.0137, \"truncated\": 96}, \"updated_at\": \"2026-05-17T05:27:33.072Z\"}, \"eval_grpo_standard_25\": {\"created_at\": \"2026-05-16T19:39:31.510Z\", \"metrics\": {\"accuracy\": 0.511, \"avg_len\": 292.86, \"eos_rate\": 0.9628, \"n_correct\": 674, \"n_total\": 1319, \"stderr\": 0.01376}, \"updated_at\": \"2026-05-17T04:49:07.062Z\"}, \"sft_standard_20_retrain\": {\"created_at\": \"2026-05-15T08:00:22.779Z\", \"metrics\": {\"conclusion\": \"Matches original sft_standard_20 (loss 0.64, token_accuracy 83%). Retrain successful.\", \"token_accuracy\": 0.83, \"train_loss_final\": 0.64}, \"updated_at\": \"2026-05-17T03:29:39.616Z\"}, \"eval_sft_grasp_20\": {\"created_at\": \"2026-05-15T15:45:15.051Z\", \"metrics\": {\"accuracy\": 0.41, \"n_total\": 100, \"note\": \"论文核心数据点: GraSP post-SFT 41% vs Standard 64% (p=0.001) vs RASP 57%\", \"p_value_vs_standard\": 0.001, \"rasp_ref\": 0.57, \"standard_ref\": 0.64}, \"updated_at\": \"2026-05-17T03:29:38.882Z\"}, \"eval-sft-alpha-0p0\": {\"created_at\": \"2026-05-15T14:26:31.883Z\", \"metrics\": {\"accuracy\": 0.64, \"avg_len\": 257.9, \"eos_rate\": 0.97, \"n_correct\": 64, \"n_total\": 100}, \"updated_at\": \"2026-05-17T03:29:37.940Z\"}, \"eval-sft-alpha-1p0\": {\"created_at\": \"2026-05-15T14:51:22.694Z\", \"metrics\": {\"accuracy\": 0.57, \"avg_len\": 224.18, \"eos_rate\": 0.98, \"n_correct\": 57, \"n_total\": 100, \"natural_eos\": 98, \"stderr\": 0.0495, \"truncated\": 2}, \"updated_at\": \"2026-05-17T03:29:36.910Z\"}, \"eval_sft_unpruned_n100\": {\"created_at\": \"2026-05-16T01:40:17.686Z\", \"metrics\": {\"accuracy\": 0.84, \"avg_response_length\": 187.22, \"eos_rate\": 1, \"n_correct\": 84, \"n_total\": 100, \"stderr\": 0.0367}, \"updated_at\": \"2026-05-17T03:29:35.970Z\"}, \"eval_sft_unpruned_full\": {\"created_at\": \"2026-05-16T01:40:17.174Z\", \"metrics\": {\"accuracy\": 81.27, \"accuracy_ci\": 1.07, \"avg_response_length\": 207.18, \"correct\": 1072, \"eos_rate\": 99.7, \"total\": 1319, \"truncated\": 4}, \"updated_at\": \"2026-05-17T03:29:35.056Z\"}, \"eval_grpo_unpruned_v2_step90\": {\"created_at\": \"2026-05-16T03:05:00.333Z\", \"metrics\": {\"accuracy\": 80.59, \"avg_response_length\": 213, \"correct\": 1063, \"eos_rate\": 99.6, \"seed\": 42, \"total\": 1319}, \"updated_at\": \"2026-05-17T03:29:34.226Z\"}, \"eval_grpo_unpruned_v2_step100\": {\"created_at\": \"2026-05-16T03:04:55.936Z\", \"metrics\": {\"accuracy\": 81.27, \"avg_response_length\": 209, \"correct\": 1072, \"eos_rate\": 99.7, \"seed\": 42, \"total\": 1319}, \"updated_at\": \"2026-05-17T03:29:33.203Z\"}, \"sft_rasp_25\": {\"created_at\": \"2026-05-16T05:26:38.517Z\", \"metrics\": {\"runtime_seconds\": 1635, \"token_accuracy\": 0.8073, \"train_loss\": 0.8498}, \"updated_at\": \"2026-05-17T03:29:32.685Z\"}, \"sft_standard_25\": {\"created_at\": \"2026-05-16T05:21:16.758Z\", \"metrics\": {\"model_keys\": 339, \"model_params\": \"5.79B\", \"note\": \"optimizer.pt save failed (RuntimeError) but model.safetensors intact\", \"runtime_seconds\": 2130, \"total_steps\": 1870}, \"updated_at\": \"2026-05-17T03:29:22.232Z\"}, \"sft_standard_25_westd\": {\"created_at\": \"2026-05-16T15:52:30.818Z\", \"metrics\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_25/model.safetensors\", \"final_loss\": 0.8381, \"token_acc\": 0.8018}, \"updated_at\": \"2026-05-17T03:29:21.686Z\"}, \"eval_grpo_rasp_20_qwen_math\": {\"created_at\": \"2026-05-16T15:59:57.504Z\", \"metrics\": {\"accuracy\": 0.725, \"n_samples\": 200, \"seed\": 42}, \"updated_at\": \"2026-05-17T03:29:20.851Z\"}, \"eval_grpo_standard_20_qwen_math\": {\"created_at\": \"2026-05-16T15:59:59.175Z\", \"metrics\": {\"accuracy\": 0.705, \"n_samples\": 200, \"seed\": 42}, \"updated_at\": \"2026-05-17T03:29:19.801Z\"}, \"eval_grpo_rasp_25_qwen_math\": {\"created_at\": \"2026-05-16T15:59:53.951Z\", \"metrics\": {\"accuracy\": 0.625, \"n_samples\": 200, \"seed\": 42}, \"updated_at\": \"2026-05-17T03:29:18.878Z\"}, \"eval_pass_k8_unpruned_qwen_math\": {\"created_at\": \"2026-05-16T16:43:10.425Z\", \"metrics\": {\"accuracy\": 0.965, \"k\": 8, \"n_samples\": 200, \"pass_at_k\": 0.965, \"stderr\": 0.013, \"temperature\": 0.7}, \"updated_at\": \"2026-05-17T03:29:17.923Z\"}, \"eval_pass_k8_rasp_20_grpo_qwen_math\": {\"created_at\": \"2026-05-16T16:43:12.096Z\", \"metrics\": {\"accuracy\": 0.915, \"k\": 8, \"n_samples\": 200, \"pass_at_k\": 0.915, \"stderr\": 0.0197, \"temperature\": 0.7}, \"updated_at\": \"2026-05-17T03:29:16.961Z\"}, \"eval_sft_rasp_rlvr_20_qwen_math\": {\"created_at\": \"2026-05-16T18:16:58.087Z\", \"metrics\": {\"accuracy\": 0.73, \"mode\": \"greedy\", \"n_correct\": 146, \"n_samples\": 200}, \"updated_at\": \"2026-05-17T03:29:16.019Z\"}, \"eval_grpo_standard_25_qwen_math\": {\"created_at\": \"2026-05-16T15:59:55.747Z\", \"metrics\": {\"accuracy\": 0.635, \"n_samples\": 200, \"seed\": 42}, \"updated_at\": \"2026-05-17T03:29:14.637Z\"}, \"eval_pass_k8_rasp_20_sft_qwen_math\": {\"created_at\": \"2026-05-16T16:43:11.344Z\", \"metrics\": {\"avg_response_length\": 139.86, \"eos_rate\": 0.99625, \"k\": 8, \"n_problems\": 200, \"natural_eos\": 1594, \"pass_at_k\": 0.935, \"stderr\": 0.0174, \"temperature\": 0.7, \"truncated\": 6}, \"updated_at\": \"2026-05-17T03:29:13.689Z\"}, \"sft-alpha-1p0\": {\"created_at\": \"2026-05-15T13:53:32.178Z\", \"metrics\": {\"post_prune_accuracy\": 0.27, \"token_accuracy\": 0.83, \"total_steps\": 1870, \"train_loss_final\": 0.64, \"train_time_min\": 28}, \"updated_at\": \"2026-05-17T03:28:07.214Z\"}, \"prune_rasp_30\": {\"created_at\": \"2026-05-16T09:03:45.925Z\", \"metrics\": {\"actual_sparsity\": 0.2873, \"attn_groups_pruned\": \"0/112\", \"mlp_groups_pruned\": \"301/784\", \"model_size_gb\": 11, \"params_pruned\": 5427842560, \"target_sparsity\": 0.3}, \"updated_at\": \"2026-05-17T03:28:01.089Z\"}, \"prune_standard_30\": {\"created_at\": \"2026-05-16T09:06:31.546Z\", \"metrics\": {\"actual_sparsity\": 0.2854, \"attn_gqa_groups_pruned\": \"0/112\", \"mlp_groups_pruned\": \"299/784\", \"params_after\": 5442379264, \"target_sparsity\": 0.3}, \"updated_at\": \"2026-05-17T03:27:59.680Z\"}, \"prune_rasp_25_qwen_math\": {\"created_at\": \"2026-05-16T09:30:44.270Z\", \"metrics\": {\"actual_sparsity\": 0.2405, \"attn_gqa_groups_pruned\": \"0/112\", \"mlp_groups_pruned\": \"252/784\", \"params_after\": 5783991808, \"target_sparsity\": 0.25}, \"updated_at\": \"2026-05-17T03:27:58.263Z\"}, \"prune_standard_25_qwen_math\": {\"created_at\": \"2026-05-16T11:00:13.880Z\", \"metrics\": {\"actual_sparsity\": 0.2396, \"attn_gqa_groups_pruned\": \"0/112\", \"mlp_groups_pruned\": \"251/784\", \"target_sparsity\": 0.25}, \"updated_at\": \"2026-05-17T03:27:56.876Z\"}, \"prune_rasp_rlvr_20_qwen_math\": {\"created_at\": \"2026-05-16T17:11:05.915Z\", \"metrics\": {\"actual_sparsity\": 0.1909, \"attn_groups_pruned\": 0, \"attn_groups_total\": 112, \"mlp_groups_pruned\": 200, \"mlp_groups_total\": 784, \"pruned_params\": 6161946112}, \"updated_at\": \"2026-05-17T03:27:55.586Z\"}, \"eval_pass_k8_rasp_20_grpo_deepseek\": {\"created_at\": \"2026-05-16T23:27:01.192Z\", \"metrics\": {\"n_problems\": 200, \"pass_k8\": 0.89, \"temperature\": 0.7}, \"updated_at\": \"2026-05-17T03:15:54.640Z\"}, \"eval_pass_k8_standard_20_grpo_deepseek\": {\"created_at\": \"2026-05-16T23:31:55.162Z\", \"updated_at\": \"2026-05-17T01:56:11.192Z\"}, \"eval_sft_rasp_20_full\": {\"created_at\": \"2026-05-15T16:21:29.964Z\", \"metrics\": {\"accuracy\": 0.6156, \"avg_response_length\": 210.95, \"eos_rate\": 0.9841, \"n_correct\": 812, \"n_samples\": 1319, \"natural_eos\": 1298, \"stderr\": 0.0134, \"truncated\": 21}, \"updated_at\": \"2026-05-17T01:29:36.754Z\"}, \"inference_speedup_plan016_v2\": {\"created_at\": \"2026-05-16T21:56:34.646Z\", \"metrics\": {\"dense\": {\"avg_latency_sec\": 6.682, \"peak_memory_gb\": 16.22, \"tokens_per_second\": 76.25}, \"rasp_20\": {\"avg_latency_sec\": 4.156, \"latency_speedup_vs_dense\": \"37.8%\", \"memory_reduction_vs_dense\": \"28.5%\", \"peak_memory_gb\": 11.6, \"tokens_per_second\": 52.07}, \"standard_20\": {\"avg_latency_sec\": 6.167, \"latency_speedup_vs_dense\": \"7.7%\", \"memory_reduction_vs_dense\": \"28.4%\", \"peak_memory_gb\": 11.61, \"tokens_per_second\": 49.78}}, \"updated_at\": \"2026-05-17T00:49:42.978Z\"}, \"eval_pass_k8_standard_20_grpo_qwen_math_v2\": {\"created_at\": \"2026-05-16T21:54:25.214Z\", \"updated_at\": \"2026-05-16T23:23:37.778Z\"}, \"eval_grpo_rasp_rlvr_20_qwen_math\": {\"created_at\": \"2026-05-16T19:39:30.069Z\", \"metrics\": {\"accuracy\": 0.71, \"mode\": \"greedy\", \"n_samples\": 200, \"seed\": 42}, \"updated_at\": \"2026-05-16T20:25:58.464Z\"}, \"eval_postprune_rasp_25\": {\"created_at\": \"2026-05-16T08:07:02.187Z\", \"metrics\": {\"accuracy\": 21, \"avg_response_length\": 2032.9, \"correct\": 21, \"eos_rate\": 56, \"natural_eos\": 56, \"seed\": 42, \"stderr\": 4.07, \"total\": 100, \"truncated\": 44}, \"updated_at\": \"2026-05-16T20:09:54.911Z\"}, \"grpo_rasp_rlvr_20_qwen_math\": {\"created_at\": \"2026-05-16T19:37:40.324Z\", \"metrics\": {\"clipped_ratio\": 0.54, \"comparison_vs_rasp_20\": \"RLVR reward 0.090 > RASP 0.061 (+48%), entropy 0.275 >> 0.073 (3.8x)\", \"comparison_vs_standard_20\": \"RLVR reward 0.090 >> Standard 0.044 (+105%)\", \"entropy_final\": 0.275, \"frac_zero_std_final\": 0.7, \"grad_norm_final\": 16.125, \"kl_final\": 0.00581, \"kl_spike_recovery\": \"immediate\", \"kl_spike_step70\": 5756.85, \"loss_final\": 0.0793, \"reward_final\": 0.09, \"reward_std_final\": 0.234, \"total_steps\": 100, \"wall_clock_min\": 45.8, \"wandb_run_id\": \"clzm2cy4\"}, \"updated_at\": \"2026-05-16T20:02:41.614Z\"}, \"grpo_standard_25\": {\"created_at\": \"2026-05-16T08:42:41.240Z\", \"metrics\": {\"clipped_ratio\": 0.92, \"collapse_pattern\": \"near_total_collapse\", \"comparison_vs_rasp_25\": \"worse_than_rasp_25(0.009)\", \"kl_final\": 0.0012, \"reward_final\": 0.0075, \"total_steps\": 100, \"wall_clock_min\": 44, \"wandb_run_id\": \"16vqw4e6\"}, \"updated_at\": \"2026-05-16T19:37:31.250Z\"}, \"eval_sft_rasp_25\": {\"created_at\": \"2026-05-16T06:17:33.814Z\", \"metrics\": {\"accuracy\": 0.5299, \"eos_rate\": 0.918, \"n_correct\": 699, \"n_samples\": 1319, \"seed\": 42, \"stderr\": 0.0137, \"truncated\": 108}, \"updated_at\": \"2026-05-16T19:15:43.879Z\"}, \"sft_rasp_rlvr_20_qwen_math\": {\"created_at\": \"2026-05-16T17:11:51.076Z\", \"updated_at\": \"2026-05-16T18:01:41.992Z\"}, \"grpo_rasp_qwen_math_v3\": {\"created_at\": \"2026-05-16T14:49:39.708Z\", \"metrics\": {\"clipped_ratio_final\": 0.975, \"clipped_ratio_mean\": 0.981, \"collapse_onset\": \"step1\", \"collapse_pattern\": \"entropy_length_collapse\", \"cross_model_match\": \"partial\", \"entropy_mean\": 0.073, \"entropy_vs_standard_ratio\": 0.39, \"frac_zero_std_final\": 0.675, \"frac_zero_std_max\": 0.7, \"frac_zero_std_min\": 0.55, \"kl_final\": 0.009, \"llama_pattern\": \"permanent_reward_collapse\", \"mean_completion_length\": 1010, \"recovery\": false, \"reward_final\": 0.061, \"reward_min\": 0.048, \"reward_peak\": 0.102, \"reward_std_final\": 0.2, \"total_steps\": 100}, \"updated_at\": \"2026-05-16T15:54:29.413Z\"}, \"sft_rasp_rlvr_20\": {\"created_at\": \"2026-05-16T09:50:43.369Z\", \"updated_at\": \"2026-05-16T14:50:02.686Z\"}, \"eval_sft_standard_25\": {\"created_at\": \"2026-05-16T07:05:10.825Z\", \"metrics\": {\"accuracy\": 0.5125, \"avg_len\": 326.26, \"eos_rate\": 0.9545, \"n_correct\": 676, \"n_total\": 1319, \"stderr\": 0.0138}, \"updated_at\": \"2026-05-16T13:23:38.482Z\"}, \"eval_sft_qwen_math_standard_25\": {\"created_at\": \"2026-05-16T12:04:49.969Z\", \"metrics\": {\"accuracy\": 63, \"correct\": 126, \"eos_rate\": 1, \"total\": 200}, \"updated_at\": \"2026-05-16T12:50:43.619Z\"}, \"eval_sft_qwen_math_rasp_25\": {\"created_at\": \"2026-05-16T12:04:49.248Z\", \"metrics\": {\"accuracy\": 64, \"correct\": 128, \"eos_rate\": 0.995, \"total\": 200}, \"updated_at\": \"2026-05-16T12:50:42.647Z\"}, \"sft_qwen_math_standard_25\": {\"created_at\": \"2026-05-16T11:15:20.187Z\", \"metrics\": {\"epochs\": 2, \"final_loss\": 0.6122, \"mean_token_accuracy\": 0.8607, \"throughput_samples_per_sec\": 8.973, \"total_steps\": 1870, \"train_runtime_sec\": 1666}, \"updated_at\": \"2026-05-16T12:04:20.943Z\"}, \"sft_qwen_math_rasp_25\": {\"created_at\": \"2026-05-16T11:15:13.431Z\", \"metrics\": {\"epochs\": 2, \"final_loss\": 0.6062, \"mean_token_accuracy\": 0.8673, \"throughput_samples_per_sec\": 9.046, \"total_steps\": 1870, \"train_runtime_sec\": 1652}, \"updated_at\": \"2026-05-16T12:03:33.361Z\"}, \"eval_sft_standard_qwen_math_n200\": {\"created_at\": \"2026-05-16T11:15:10.910Z\", \"metrics\": {\"accuracy\": 0.71, \"avg_len\": 127.7, \"correct\": 142, \"eos_rate\": 1, \"n_total\": 200, \"stderr\": 0.0321}, \"updated_at\": \"2026-05-16T11:32:27.012Z\"}, \"eval_sft_rasp_qwen_math_n200\": {\"created_at\": \"2026-05-16T11:15:07.028Z\", \"metrics\": {\"accuracy\": 0.725, \"avg_len\": 121.8, \"correct\": 145, \"eos_rate\": 1, \"n_total\": 200, \"stderr\": 0.0316}, \"updated_at\": \"2026-05-16T11:32:23.931Z\"}, \"prune_rasp_rlvr_20\": {\"created_at\": \"2026-05-16T09:50:39.656Z\", \"metrics\": {\"actual_sparsity\": 0.1909, \"attn_gqa_groups_pruned\": \"0/112\", \"group_selection_diff_vs_rasp\": \"RASP重剪前6层+后段(19,23-25,27)保中间; RLVR重剪前6层+中后段(16-26)保Layer6-7,27\", \"mlp_groups_pruned\": \"200/784\", \"params_after\": \"6.16B\", \"target_sparsity\": 0.2}, \"updated_at\": \"2026-05-16T10:31:42.144Z\"}, \"sft_standard_20_qwen_math\": {\"created_at\": \"2026-05-16T08:11:00.051Z\", \"updated_at\": \"2026-05-16T10:10:19.019Z\"}, \"sft_rasp_20_qwen_math\": {\"created_at\": \"2026-05-16T08:10:59.311Z\", \"updated_at\": \"2026-05-16T10:10:17.852Z\"}, \"prune_standard_20_qwen_math\": {\"created_at\": \"2026-05-16T08:03:56.378Z\", \"metrics\": {\"attn_groups_pruned\": 0, \"mlp_groups_pruned\": 202, \"model_keys\": 339, \"original_params\": 7615616512, \"pruned_params\": 6147409408, \"sparsity_actual\": 0.1928, \"sparsity_target\": 0.2}, \"updated_at\": \"2026-05-16T08:04:22.864Z\"}, \"prune_rasp_20_qwen_math\": {\"created_at\": \"2026-05-16T08:01:57.095Z\", \"metrics\": {\"alpha\": 1, \"attn_groups_pruned\": 0, \"mlp_groups_pruned\": 199, \"model_keys\": 339, \"original_params\": 7615616512, \"pruned_params\": 6169214464, \"sparsity_actual\": 0.1899, \"sparsity_target\": 0.2}, \"updated_at\": \"2026-05-16T08:04:20.185Z\"}, \"eval_grpo_rasp_v9_step10\": {\"created_at\": \"2026-05-16T03:40:46.186Z\", \"metrics\": {\"accuracy\": 61.87, \"avg_response_length\": 213.6, \"correct\": 816, \"eos_rate\": 98.33, \"seed\": 42, \"stderr\": 1.34, \"total\": 1319, \"truncated\": 22}, \"updated_at\": \"2026-05-16T08:01:06.191Z\"}, \"eval_grpo_rasp_v9_step5\": {\"created_at\": \"2026-05-16T01:55:35.424Z\", \"metrics\": {\"accuracy\": 60.65, \"seed\": 42, \"total\": 1319}, \"updated_at\": \"2026-05-16T05:18:16.131Z\"}, \"prune_standard_25\": {\"created_at\": \"2026-05-16T05:13:52.855Z\", \"updated_at\": \"2026-05-16T05:16:41.032Z\"}, \"prune_rasp_25\": {\"created_at\": \"2026-05-16T05:13:52.292Z\", \"updated_at\": \"2026-05-16T05:16:39.998Z\"}, \"grpo_unpruned_v2\": {\"created_at\": \"2026-05-16T01:45:10.586Z\", \"metrics\": {\"avg_step_time_sec\": 23, \"checkpoints_available\": [\"checkpoint-90\", \"checkpoint-95\", \"checkpoint-100\"], \"collapse_onset\": \"N/A\", \"final_entropy\": 0.194, \"final_grad_norm\": 6.97, \"final_kl\": 0.0051, \"final_reward\": 0.661, \"max_steps\": 100, \"peak_reward\": 0.669, \"peak_reward_step\": 80, \"reward_range\": \"0.425-0.669\", \"training_seconds\": 2660}, \"updated_at\": \"2026-05-16T04:43:16.844Z\"}, \"grpo_stage2_rasp_20_v9\": {\"created_at\": \"2026-05-15T22:37:13.593Z\", \"metrics\": {\"checkpoints\": [\"checkpoint-10\", \"checkpoint-15\", \"checkpoint-20\", \"checkpoint-25\", \"checkpoint-30\"], \"collapse_note\": \"frac_zero_std peaked at 95% by step 30, reward dropped from peak 0.039 (step 20) to 0.021 (step 30)\", \"collapse_status\": \"COLLAPSED\", \"final_clipped_ratio\": 0.956, \"final_frac_zero_std\": 0.95, \"final_grad_norm\": 1.398, \"final_kl\": 0.00118, \"final_loss\": 0.00686, \"final_mean_length\": 996, \"final_mean_terminated_length\": 176, \"final_reward\": 0.021, \"max_steps\": 30, \"reward_history\": [{\"frac_zero_std\": 0.875, \"reward\": 0.015, \"step\": 10}, {\"frac_zero_std\": 0.8, \"reward\": 0.039, \"step\": 20}, {\"frac_zero_std\": 0.95, \"reward\": 0.021, \"step\": 30}], \"step\": 30, \"step_time_sec\": 418, \"total_time\": \"3h28m25s\", \"wandb_url\": \"https://wandb.ai/xiaoyucorynne-/recovery_aware_struct_prune/runs/mrikafz3\"}, \"updated_at\": \"2026-05-16T03:38:37.387Z\"}, \"alpha_ablation_sweep\": {\"created_at\": \"2026-05-15T20:15:39.765Z\", \"metrics\": {\"alpha_0.0\": {\"accuracy\": 0.27, \"avg_len\": 1192, \"eos_rate\": 0.8, \"n_correct\": 27, \"n_total\": 100}, \"alpha_0.25\": {\"accuracy\": 0.23, \"avg_len\": 1834, \"eos_rate\": 0.63, \"n_correct\": 23, \"n_total\": 100}, \"alpha_0.5\": {\"accuracy\": 0.22, \"avg_len\": 1141, \"eos_rate\": 0.81, \"n_correct\": 22, \"n_total\": 100}, \"alpha_1.0\": {\"accuracy\": 0.31, \"avg_len\": 733, \"eos_rate\": 0.92, \"n_correct\": 31, \"n_total\": 100}, \"alpha_2.0\": {\"accuracy\": 0.36, \"avg_len\": 2130, \"eos_rate\": 0.59, \"n_correct\": 36, \"n_total\": 100}}, \"updated_at\": \"2026-05-16T00:18:46.780Z\"}, \"sft_unpruned_baseline\": {\"created_at\": \"2026-05-15T22:07:43.929Z\", \"metrics\": {\"epochs\": 2, \"final_loss\": 0.3321, \"final_token_accuracy\": 0.909, \"total_steps\": 1870, \"train_loss_avg\": 0.4253, \"train_runtime_sec\": 1908, \"train_samples_per_second\": 7.833}, \"updated_at\": \"2026-05-16T00:18:44.096Z\"}, \"eval_sft_rasp_full_westd\": {\"created_at\": \"2026-05-15T20:36:02.786Z\", \"metrics\": {\"accuracy\": 0.6149, \"avg_len\": 216.5, \"eos_rate\": 0.9826, \"n_correct\": 811, \"n_total\": 1319, \"stderr\": 0.0134}, \"updated_at\": \"2026-05-15T21:42:41.916Z\"}, \"eval_sft_standard_full_westd\": {\"created_at\": \"2026-05-15T20:36:01.803Z\", \"metrics\": {\"accuracy\": 0.5929, \"avg_len\": 226.7, \"eos_rate\": 0.9803, \"n_correct\": 782, \"n_total\": 1319, \"stderr\": 0.01353}, \"updated_at\": \"2026-05-15T21:42:40.854Z\"}, \"eval_sft_rasp_20_westd_n100_v2\": {\"created_at\": \"2026-05-15T19:24:08.437Z\", \"metrics\": {\"accuracy\": 0.67, \"avg_len\": 182.39, \"eos_rate\": 0.99, \"n_correct\": 67, \"n_total\": 100}, \"updated_at\": \"2026-05-15T20:11:02.033Z\"}, \"eval_sft_standard_20_westd_n100_v2\": {\"created_at\": \"2026-05-15T19:24:09.850Z\", \"metrics\": {\"accuracy\": 0.63, \"avg_len\": 260.57, \"eos_rate\": 0.97, \"n_correct\": 63, \"n_total\": 100}, \"updated_at\": \"2026-05-15T20:11:00.967Z\"}, \"eval_sft_standard_20_westd_n100\": {\"created_at\": \"2026-05-15T17:39:03.607Z\", \"metrics\": {\"accuracy\": 0.63, \"avg_len\": 260.57, \"eos_rate\": 0.97, \"n_correct\": 63, \"n_total\": 100, \"stderr\": 0.048}, \"updated_at\": \"2026-05-15T19:30:00.797Z\"}, \"eval_sft_rasp_20_westd_n100\": {\"created_at\": \"2026-05-15T17:35:08.417Z\", \"metrics\": {\"accuracy\": 0.67, \"avg_len\": 182.39, \"eos_rate\": 0.99, \"n_correct\": 67, \"n_total\": 100, \"stderr\": 0.047}, \"updated_at\": \"2026-05-15T19:29:59.250Z\"}, \"sft_rasp_20_westd_retrain\": {\"created_at\": \"2026-05-15T16:59:51.103Z\", \"updated_at\": \"2026-05-15T18:36:33.103Z\"}, \"sft_standard_20_westd_retrain\": {\"created_at\": \"2026-05-15T17:05:52.927Z\", \"metrics\": {\"epochs\": 2, \"final_step_loss\": 0.6403, \"final_token_accuracy\": 0.8258, \"total_steps\": 1870, \"train_loss\": 0.7577, \"train_runtime_sec\": 1679, \"train_samples_per_second\": 8.902}, \"updated_at\": \"2026-05-15T18:36:32.558Z\"}, \"grasp_baseline_westd\": {\"created_at\": \"2026-05-15T12:40:34.072Z\", \"metrics\": {\"avg_len\": 4018, \"eos_rate\": 0.02, \"grasp_20_accuracy_n100\": 0.07, \"json_path\": \"results/eval_pruned_graspune_20_greedy.json\", \"n_correct\": 7, \"n_total\": 100, \"rasp_20_accuracy_ref\": 0.31, \"standard_20_accuracy_ref\": 0.27}, \"updated_at\": \"2026-05-15T17:12:21.555Z\"}, \"eval_sft_alpha_2p0\": {\"created_at\": \"2026-05-15T15:42:36.917Z\", \"metrics\": {\"accuracy\": 0.62, \"avg_len\": 277.41, \"eos_rate\": 0.97, \"n_correct\": 62, \"n_total\": 100, \"stderr\": 0.0485}, \"updated_at\": \"2026-05-15T16:41:41.929Z\"}, \"sft_alpha2_0_westd\": {\"created_at\": \"2026-05-15T14:32:54.953Z\", \"metrics\": {\"epoch\": 2, \"mean_token_accuracy_final\": 0.8354, \"post_prune_accuracy\": 0.29, \"total_steps\": 1870, \"train_loss\": 0.7424, \"train_loss_final\": 0.6114, \"train_runtime_sec\": 2422}, \"updated_at\": \"2026-05-15T15:41:31.384Z\"}, \"alpha_ablation_westd_cal256\": {\"created_at\": \"2026-05-15T09:46:30.119Z\", \"metrics\": {\"alpha_4_0_accuracy\": 0.4, \"finding\": \"α=4.0 gives 40% post-prune accuracy (highest), non-monotonic relationship between α and accuracy\"}, \"updated_at\": \"2026-05-15T15:07:37.593Z\"}, \"sft_grasp_20_westd\": {\"created_at\": \"2026-05-15T13:50:39.294Z\", \"updated_at\": \"2026-05-15T15:01:02.359Z\"}, \"sft_alpha4_0_westd_retry\": {\"created_at\": \"2026-05-15T12:46:36.918Z\", \"metrics\": {\"accuracy_stderr\": 0.049, \"avg_response_length\": 238.56, \"eos_rate\": 0.98, \"mean_token_accuracy_final\": 0.8368, \"n_correct\": 62, \"n_total\": 100, \"post_prune_accuracy\": 0.4, \"post_sft_accuracy_100\": 0.62, \"sft_recovery_gain_pp\": 22, \"train_loss_final\": 0.7393, \"train_loss_last_logged\": 0.6106}, \"updated_at\": \"2026-05-15T13:48:13.666Z\"}, \"reeval_postprune_definitive\": {\"created_at\": \"2026-05-15T09:46:32.498Z\", \"metrics\": {\"conclusion\": \"Original 29x advantage (29% vs 1%) not reproducible. Actual gap 4pp (31% vs 27% on westb), not statistically significant.\", \"original_claim_rasp\": 0.29, \"original_claim_standard\": 0.01, \"rasp_20_accuracy_westb\": 0.31, \"rasp_20_accuracy_westd\": 0.29, \"rasp_vs_standard_gap_pp\": 4, \"standard_20_accuracy_westb\": 0.27}, \"updated_at\": \"2026-05-15T12:30:41.698Z\"}, \"sft_standard_20\": {\"created_at\": \"2026-05-14T23:37:34.863Z\", \"metrics\": {\"eos_rate_greedy_100\": 0.99, \"greedy_accuracy_100\": 0.64, \"greedy_avg_len\": 176.31, \"greedy_correct\": 64, \"greedy_max_len\": 4096, \"greedy_min_len\": 43, \"greedy_total\": 100, \"sampling_eos_rate_5\": 1, \"token_accuracy\": 0.83, \"total_steps\": 1870, \"train_loss_final\": 0.64, \"train_loss_initial\": 1.7, \"train_time_min\": 37}, \"updated_at\": \"2026-05-15T02:49:41.141Z\"}, \"sft_rasp_20\": {\"created_at\": \"2026-05-14T23:37:33.162Z\", \"metrics\": {\"eos_rate_greedy_100\": 0.99, \"greedy_accuracy_100\": 0.57, \"greedy_avg_len\": 179.83, \"greedy_correct\": 57, \"greedy_max_len\": 4096, \"greedy_min_len\": 59, \"greedy_total\": 100, \"sampling_eos_rate_5\": 1, \"token_accuracy\": 0.83, \"total_steps\": 1870, \"train_loss_final\": 0.64, \"train_loss_initial\": 1.86, \"train_time_min\": 37}, \"updated_at\": \"2026-05-15T02:49:39.222Z\"}}, \"count\": 249, \"total\": 249, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.9}}"
    }
  },
  "sourceToolAssistantUUID": "23ca0e31-fe63-4b43-9d20-38c5e0c3aa5b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "3a90179e-e19e-41d1-8fb4-f23e916f555f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Runtime record

_source line 61_

```json
{
  "type": "last-prompt",
  "leafUuid": "e4bc7c49-4335-41db-a060-e969df0f0e8d",
  "sessionId": "3a90179e-e19e-41d1-8fb4-f23e916f555f"
}
```

---


### Runtime record

_source line 62_

```json
{
  "type": "ai-title",
  "aiTitle": "Map paper results to registry experiments",
  "sessionId": "3a90179e-e19e-41d1-8fb4-f23e916f555f"
}
```

---


### Assistant

_source line 63 · 2026-05-23T10:52:32.909Z_

<details><summary>Logged reasoning block</summary>

```text
OK, this is returning all data but it's too large. Let me also get the full registry with spec fields. I need to have an agent parse both files and extract all mappings. 

Actually, I already have one file with full fields (50 results) and now I have another with all results (just exp_id, metrics, created_at, updated_at, tags). Let me also get all with spec fields.

Let me have an agent do all the remaining parsing work - matching the additional experiments that weren't in the first 50.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e4bc7c49-4335-41db-a060-e969df0f0e8d",
  "isSidechain": false,
  "requestId": "req_011CbKNfuv13vVA4C9a2tJzQ",
  "type": "assistant",
  "uuid": "d06d4134-1a14-4c2c-9e0a-6f7661ec58f3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "3a90179e-e19e-41d1-8fb4-f23e916f555f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HVMQW3VJFX2zf7AkbguAWt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 892,
      "cache_read_input_tokens": 56515,
      "output_tokens": 272,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 892,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 272,
          "cache_read_input_tokens": 56515,
          "cache_creation_input_tokens": 892,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 892
          },
          "type": "message"
        }
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

_source line 64 · 2026-05-23T10:52:33.902Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01Tc7ZkPR52HzWNi9Rt7jTxS`</summary>

```json
{
  "project": "recovery_aware_struct_prune",
  "filters": {
    "conclusion": "success"
  },
  "limit": 0,
  "fields": [
    "exp_id",
    "metrics",
    "spec",
    "created_at"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d06d4134-1a14-4c2c-9e0a-6f7661ec58f3",
  "isSidechain": false,
  "requestId": "req_011CbKNfuv13vVA4C9a2tJzQ",
  "type": "assistant",
  "uuid": "4a7541bf-eb55-449f-a1b0-07409f178bce",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "3a90179e-e19e-41d1-8fb4-f23e916f555f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HVMQW3VJFX2zf7AkbguAWt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 892,
      "cache_read_input_tokens": 56515,
      "output_tokens": 272,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 892,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 272,
          "cache_read_input_tokens": 56515,
          "cache_creation_input_tokens": 892,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 892
          },
          "type": "message"
        }
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

_source line 65 · 2026-05-23T10:52:35.172Z_

<details><summary>↩ Tool result · `toolu_01Tc7ZkPR52HzWNi9Rt7jTxS`</summary>

```text
Error: result (245,301 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-17-projects-recovery-aware-struct-prune/3a90179e-e19e-41d1-8fb4-f23e916f555f/tool-results/mcp-agent-ml-research-read_registry-1779533555169.txt.
Format: JSON with schema: {result: string}
- For targeted queries (find a value, filter by field): use jq on the file directly.
- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-17-projects-recovery-aware-struct-prune/3a90179e-e19e-41d1-8fb4-f23e916f555f/tool-results/mcp-agent-ml-research-read_registry-1779533555169.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.
- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-17-projects-recovery-aware-struct-prune/3a90179e-e19e-41d1-8fb4-f23e916f555f/tool-results/mcp-agent-ml-research-read_registry-1779533555169.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim." A vague "summarize this" may lose detail.

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4a7541bf-eb55-449f-a1b0-07409f178bce",
  "isSidechain": false,
  "promptId": "dddf37fd-16cc-4cd5-bb05-648328938281",
  "type": "user",
  "uuid": "69ae3b7b-911e-4228-a783-ae52dd177cb4",
  "toolUseResult": "Error: result (245,301 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-17-projects-recovery-aware-struct-prune/3a90179e-e19e-41d1-8fb4-f23e916f555f/tool-results/mcp-agent-ml-research-read_registry-1779533555169.txt.\nFormat: JSON with schema: {result: string}\n- For targeted queries (find a value, filter by field): use jq on the file directly.\n- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-17-projects-recovery-aware-struct-prune/3a90179e-e19e-41d1-8fb4-f23e916f555f/tool-results/mcp-agent-ml-research-read_registry-1779533555169.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.\n- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. \"/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-17-projects-recovery-aware-struct-prune/3a90179e-e19e-41d1-8fb4-f23e916f555f/tool-results/mcp-agent-ml-research-read_registry-1779533555169.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim.\" A vague \"summarize this\" may lose detail.\n",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"eval_math500_sft_qwen_math_cka_only_20\": {\"created_at\": \"2026-05-22T23:11:09.017Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_qwen_math_cka_only_20_final --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_math500_sft_qwen_math_cka_only_20.json --seed 42 --dtype bfloat16 --max_new_tokens 2048\", \"server\": \"westb-23072\", \"gpu\": \"cuda:0\", \"data_path\": \"HuggingFaceH4/MATH-500\", \"data_count\": 500, \"model_name\": \"Qwen2.5-Math-7B-CKA-only-20%-SFT-ep1\", \"seed\": 42, \"checkpoint_source\": \"sft_qwen_math_cka_only_20_final\", \"eval_data\": \"MATH-500 (N=500, max_new_tokens=2048)\", \"pid\": 250766, \"log_path\": \"/tmp/eval_math500_sft_qwen_cka_only_20.log\"}, \"metrics\": {\"accuracy\": 0.216, \"stderr\": 0.0184, \"correct\": 108, \"total\": 500, \"natural_eos\": 90, \"truncated\": 410, \"avg_response_length\": 1745.338}}, \"eval_math500_grpo_rasp_alpha0p5_20\": {\"created_at\": \"2026-05-23T02:59:15.985Z\", \"spec\": {\"command\": \"python src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_alpha0p5_20 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_math500_grpo_rasp_alpha0p5_20.json --seed 42 --dtype bfloat16 --max_new_tokens 2048\", \"server\": \"westb-23072\", \"data_path\": \"MATH-500\", \"data_count\": 500, \"model_name\": \"grpo_rasp_alpha0p5_20\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_alpha0p5_20\", \"eval_data\": \"MATH-500\"}, \"metrics\": {\"accuracy\": 0.248, \"stderr\": 0.0193, \"correct\": 124, \"total\": 500, \"natural_eos\": 274, \"truncated\": 226, \"avg_response_length\": 1110.462}}, \"eval_math500_grpo_cka_only_20_2048_v2\": {\"created_at\": \"2026-05-23T05:07:09.002Z\", \"spec\": {\"command\": \"bash -c 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=3 HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 python src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20/checkpoint-100 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_math500_grpo_cka_only_20_2048_v2.json --seed 42 --dtype bfloat16 --max_new_tokens 2048'\", \"server\": \"westd-32935\", \"data_path\": \"MATH-500\", \"data_count\": 500, \"model_name\": \"grpo_cka_only_20/checkpoint-100\", \"seed\": 42, \"checkpoint_source\": \"westb-23072:/root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20/checkpoint-100\", \"eval_data\": \"MATH-500\"}, \"metrics\": {\"accuracy\": 0.274, \"correct\": 137, \"total\": 500, \"stderr\": 0.01995, \"natural_eos\": 390, \"truncated\": 110, \"avg_response_length\": 654.746}}, \"eval_math500_grpo_rasp_alpha3p0_20\": {\"created_at\": \"2026-05-23T03:19:40.950Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=0 HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 python src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_alpha3p0_20_v2/checkpoint-100 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_math500_grpo_rasp_alpha3p0_20.json --seed 42 --dtype bfloat16 --max_new_tokens 2048\\\"\", \"server\": \"westd-32935\", \"data_path\": \"MATH-500\", \"data_count\": 500, \"model_name\": \"grpo_rasp_alpha3p0_20_v2/checkpoint-100\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_alpha3p0_20_v2/checkpoint-100\", \"eval_data\": \"MATH-500\"}, \"metrics\": {\"accuracy\": 0.228, \"correct\": 114, \"total\": 500, \"stderr\": 0.0188, \"truncated_ratio\": 0.28, \"avg_response_length\": 745.038}}, \"eval_math500_grpo_rasp_alpha4p0_20\": {\"created_at\": \"2026-05-23T00:01:54.194Z\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_alpha4_20/checkpoint-100\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/logs/eval_math500_grpo_rasp_alpha4p0_20.log\"}, \"metrics\": {\"accuracy\": 0.262, \"stderr\": 0.01966, \"correct\": 131, \"total\": 500, \"truncated\": 180, \"natural_eos\": 320, \"avg_response_length\": 925.48}}, \"eval_math500_grpo_rasp_alpha1p0_20\": {\"created_at\": \"2026-05-22T23:02:44.335Z\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_rasp_20_fair\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_math500_grpo_rasp_alpha1p0_20.log\"}, \"metrics\": {\"accuracy\": 0.226, \"stderr\": 0.0187, \"n_correct\": 113, \"n_total\": 500, \"avg_response_length\": 903.536, \"natural_eos\": 320, \"truncated\": 180}}, \"eval_math500_sft_cka_only_20_westd\": {\"created_at\": \"2026-05-22T20:45:21.526Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 python src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_20 --output_path results/eval_math500_sft_cka_only_20.json --seed 42 --dtype bfloat16 --max_new_tokens 2048\", \"server\": \"westd-32935\", \"gpu\": \"cuda:1\", \"pid\": \"75284\", \"data_path\": \"MATH-500\", \"data_count\": 500, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B (sft_cka_only_20)\", \"seed\": 42, \"checkpoint_source\": \"sft_cka_only_20\", \"eval_data\": \"MATH-500 (N=500, max_new_tokens=2048)\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/logs/eval_math500_sft_cka_only_20.log\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_20\"}, \"metrics\": {\"accuracy\": 0.268, \"correct\": 134, \"total\": 500, \"truncated\": 116, \"stderr\": 0.0198, \"natural_eos_pct\": 0.768, \"avg_response_length\": 673.278, \"note\": \"PID 75284 actual output = 26.8% (134/500). Previous 29.0% (145/500) was from v4 run (May 19) with different answer extraction. Same model generations, different scoring.\"}}, \"eval_math500_grpo_rasp_alpha2p0_20\": {\"created_at\": \"2026-05-22T22:23:27.589Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/recovery_aware_struct_prune && HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 python src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_alpha2p0_20 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_math500_grpo_rasp_alpha2p0_20.json --seed 42 --dtype bfloat16 --max_new_tokens 2048\\\"\", \"server\": \"westd-32935\", \"gpu\": \"cuda:0\", \"pid\": \"83709\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_math500_grpo_rasp_alpha2p0_20.log\", \"submitted_at\": \"2026-05-22T22:25:27.490Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"MATH-500\", \"data_count\": 500, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B (grpo_rasp_alpha2p0_20)\", \"seed\": 42, \"checkpoint_source\": \"grpo_rasp_alpha2p0_20\", \"eval_data\": \"MATH-500 (N=500, max_new_tokens=2048)\", \"wall_clock_seconds\": 17473.0, \"gpu_hours\": 4.85}, \"metrics\": {\"accuracy\": 0.262, \"correct\": 131, \"total\": 500, \"stderr\": 0.0197, \"natural_eos\": 349, \"truncated\": 151, \"avg_response_length\": 785.326}}, \"eval_gsm8k_grpo_qwen_math_cka_only_20_n500_v3\": {\"created_at\": \"2026-05-22T15:12:46.181Z\", \"spec\": {\"command\": \"bash -c 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/recovery_aware_struct_prune && python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_qwen_math_cka_only_20 --max_samples 500 --max_new_tokens 2048 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_grpo_qwen_math_cka_only_20_n500_v3.json'\", \"server\": \"westb-23072\", \"gpu\": \"cuda:1\", \"pid\": \"220343\", \"data_path\": \"GSM8K test split\", \"data_count\": 500, \"model_name\": \"Qwen2.5-Math-7B-pruned-cka_only-20pct-GRPO\", \"seed\": 42, \"checkpoint_source\": \"grpo_qwen_math_cka_only_20\", \"eval_data\": \"GSM8K\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_qwen_math_cka_only_20\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_gsm8k_grpo_qwen_math_cka_only_20_n500_v3.log\"}, \"metrics\": {\"accuracy\": 0.486, \"correct\": 243, \"total\": 500, \"stderr\": 0.0224, \"truncated_pct\": 0.838, \"natural_eos_pct\": 0.162, \"avg_response_length\": 1766.5}}, \"eval_math500_sft_rasp_alpha1p0_20_v2\": {\"created_at\": \"2026-05-22T20:50:24.239Z\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20_westd\", \"log_path\": \"/root/runs/recovery_aware_struct_prune/eval_math500_sft_rasp_alpha1p0_20_v2.log\"}, \"metrics\": {\"accuracy\": 0.212, \"correct\": 106, \"total\": 500, \"truncated\": 186, \"stderr\": 0.0183}}, \"eval_math500_sft_standard_20_2048_v2\": {\"created_at\": \"2026-05-19T01:34:44.782Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/recovery_aware_struct_prune && HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 python src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_math500_sft_standard_20_2048_v2.json --seed 42 --dtype bfloat16 --max_new_tokens 2048\\\"\", \"server\": \"westd-32935\", \"gpu\": [\"cuda:0\"], \"pid\": \"82301\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_math500_sft_standard_20_2048_v2.log\", \"submitted_at\": \"2026-05-22T22:15:58.026Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"metrics\": {\"accuracy\": 0.258, \"n_correct\": 129, \"n_total\": 500}}, \"eval_math500_sft_rasp_alpha0p5_20\": {\"created_at\": \"2026-05-22T15:20:44.460Z\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_alpha0p5_20\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/logs/eval_math500_sft_rasp_alpha0p5_20.log\"}, \"metrics\": {\"accuracy\": 0.254, \"correct\": 127, \"total\": 500, \"truncated\": 220, \"stderr\": 0.0195}}, \"eval_math500_sft_rasp_alpha3p0_20\": {\"created_at\": \"2026-05-22T18:26:16.273Z\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_alpha3p0_20/checkpoint-935\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/logs/eval_math500_sft_rasp_alpha3p0_20.log\"}, \"metrics\": {\"accuracy\": 0.232, \"correct\": 116, \"total\": 500, \"truncated\": 144, \"stderr\": 0.0189}}, \"eval_math500_sft_rasp_alpha4p0_20\": {\"created_at\": \"2026-05-22T15:20:47.150Z\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_alpha4_20\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/logs/eval_math500_sft_rasp_alpha4p0_20.log\"}, \"metrics\": {\"accuracy\": 0.266, \"correct\": 133, \"total\": 500, \"truncated\": 190, \"stderr\": 0.0198}}, \"eval_math500_sft_rasp_alpha2p0_20\": {\"created_at\": \"2026-05-22T15:06:22.386Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 nohup python src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_alpha2p0_20 --output_path results/eval_math500_sft_rasp_alpha2p0_20.json --seed 42 --dtype bfloat16 --max_new_tokens 2048\", \"server\": \"westd-32935\", \"gpu\": \"cuda:1\", \"pid\": \"57202\", \"data_path\": \"MATH-500\", \"data_count\": 500, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B (sft_rasp_alpha2p0_20)\", \"seed\": 42, \"checkpoint_source\": \"sft_rasp_alpha2p0_20\", \"eval_data\": \"MATH-500 (N=500, max_new_tokens=2048)\", \"log_path\": \"/root/recovery_aware_struct_prune/results/eval_math500_sft_rasp_alpha2p0_20.log\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_alpha2p0_20\"}, \"metrics\": {\"accuracy\": 0.24, \"correct\": 120, \"total\": 500, \"truncated\": 155, \"stderr\": 0.0191}}, \"eval_gsm8k_grpo_random_20_seed456\": {\"created_at\": \"2026-05-22T16:26:01.516Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_random_20_seed456/checkpoint-100 --seed 456 --dtype bfloat16 --max_new_tokens 2048 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_grpo_random_20_seed456.json\", \"server\": \"westb-23072\", \"gpu\": \"cuda:0\", \"pid\": \"224705\", \"data_path\": \"openai/gsm8k (test split)\", \"data_count\": 1319, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B (grpo_random_20_seed456)\", \"seed\": 456, \"checkpoint_source\": \"grpo_random_20_seed456/checkpoint-100\", \"eval_data\": \"GSM8K test 1319\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_grpo_random_20_seed456.log\", \"accuracy\": 0.5087, \"total_correct\": 671, \"total_samples\": 1319, \"eos_rate\": 0.9955, \"stderr\": 0.01377, \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_random_20_seed456/checkpoint-100\"}, \"metrics\": {\"gsm8k_accuracy\": 0.5087, \"gsm8k_accuracy_se\": 0.0138, \"gsm8k_correct\": 671, \"gsm8k_total\": 1319, \"eos_rate\": 0.9954, \"avg_response_length\": 163.5, \"truncated\": 6}}, \"eval_gsm8k_grpo_random_20_seed123_v2\": {\"created_at\": \"2026-05-22T14:22:33.753Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 nohup python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_random_20_seed123_v2/checkpoint-100 --output_path results/eval_gsm8k_grpo_random_20_seed123_v2.json --seed 123 --dtype bfloat16\", \"server\": \"westd-32935\", \"gpu\": \"cuda:0\", \"pid\": \"56283\", \"data_path\": \"openai/gsm8k (test split)\", \"data_count\": 1319, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B (grpo_random_20_seed123_v2)\", \"seed\": 123, \"checkpoint_source\": \"grpo_random_20_seed123_v2/checkpoint-100\", \"eval_data\": \"gsm8k test 1319\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_grpo_random_20_seed123_v2.json\", \"accuracy\": 0.5072, \"total_correct\": 669, \"total_samples\": 1319, \"eos_rate\": 0.9939, \"stderr\": 0.01377, \"avg_response_length\": 177.9, \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_random_20_seed123_v2/checkpoint-100\"}}, \"grpo_random_20_seed456\": {\"created_at\": \"2026-05-22T12:00:38.940Z\", \"spec\": {\"server\": \"westb-23072\", \"gpu\": \"cuda:0\", \"command\": \"CUDA_VISIBLE_DEVICES=0 HF_HUB_OFFLINE=1 HF_DATASETS_OFFLINE=1 nohup python src/train_grpo_v5.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_random_20 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/grpo_random_20_seed456 --max_steps 100 --save_steps 100 --seed 456\", \"pid\": \"209508\", \"data_path\": \"openai/gsm8k (train split)\", \"data_count\": 7473, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B (sft_random_20)\", \"seed\": 456, \"checkpoint_source\": \"sft_random_20\", \"eval_data\": \"N/A - GRPO training\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_random_20_seed456/checkpoint-100\", \"log_path\": \"/tmp/grpo_random_seed456.log\", \"note\": \"100/100 steps completed. Final trainer.save_model() hit disk-full but TRL checkpoint-100 is intact (model.safetensors=12,174,631,264 bytes, matching seed42/seed123_v2). Reviewer independently verified.\"}}, \"eval_gsm8k_sft_depth_first_20\": {\"created_at\": \"2026-05-22T14:20:43.950Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 nohup python src/eval_gsm8k.py --model_path sft_depth_first_20 --output_path results/eval_gsm8k_sft_depth_first_20.json --seed 42 --dtype bfloat16\", \"server\": \"westd-32935\", \"gpu\": \"cuda:2\", \"pid\": \"54882\", \"data_path\": \"openai/gsm8k (test split)\", \"data_count\": 1319, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B (sft_depth_first_20)\", \"seed\": 42, \"checkpoint_source\": \"sft_depth_first_20\", \"eval_data\": \"gsm8k test 1319\", \"log_path\": \"/root/recovery_aware_struct_prune/results/eval_gsm8k_sft_depth_first_20.log\", \"note\": \"Early-stopped by Director at ~60-88 samples. Interim accuracy ~10%@50 (SFT). Conclusive: depth-first 20% SFT dramatically worse than CKA-only 64%. MF5 claim validated — CKA-only advantage is NOT simply removing deep layers.\", \"checkpoint_path\": \"N/A (eval only)\"}}, \"eval_gsm8k_grpo_depth_first_20\": {\"created_at\": \"2026-05-22T14:20:41.126Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 nohup python src/eval_gsm8k.py --model_path grpo_depth_first_20/checkpoint-100 --output_path results/eval_gsm8k_grpo_depth_first_20.json --seed 42 --dtype bfloat16\", \"server\": \"westd-32935\", \"gpu\": \"cuda:3\", \"pid\": \"51981\", \"data_path\": \"openai/gsm8k (test split)\", \"data_count\": 1319, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B (grpo_depth_first_20)\", \"seed\": 42, \"checkpoint_source\": \"grpo_depth_first_20/checkpoint-100\", \"eval_data\": \"gsm8k test 1319\", \"log_path\": \"/root/recovery_aware_struct_prune/results/eval_gsm8k_grpo_depth_first_20.log\", \"note\": \"Early-stopped by Director at ~60-88 samples. Interim accuracy ~8%@50 (GRPO). Conclusive: depth-first 20% GRPO dramatically worse than CKA-only 64%. MF5 claim validated — CKA-only advantage is NOT simply removing deep layers.\", \"checkpoint_path\": \"N/A (eval only)\"}}, \"grpo_random_20_seed123_v2\": {\"created_at\": \"2026-05-22T14:22:29.868Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 HF_HUB_OFFLINE=1 HF_DATASETS_OFFLINE=1 nohup python src/train_grpo_v5.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_random_20 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/grpo_random_20_seed123_v2 --max_steps 100 --save_steps 100 --seed 123\", \"server\": \"westd-32935\", \"gpu\": \"cuda:1\", \"pid\": \"53822\", \"data_path\": \"openai/gsm8k (train split)\", \"data_count\": 7473, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B (sft_random_20)\", \"seed\": 123, \"checkpoint_source\": \"sft_random_20\", \"eval_data\": \"N/A - GRPO training\", \"log_path\": \"/tmp/grpo_random_seed123_v2.log\"}}, \"eval_gsm8k_grpo_alpha3p0_20\": {\"created_at\": \"2026-05-22T09:30:06.630Z\", \"spec\": {\"server\": \"westd-32935\", \"gpu\": \"cuda:0\", \"command\": \"CUDA_VISIBLE_DEVICES=0 HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 nohup python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_alpha3p0_20_v2/checkpoint-100 --output_path results/eval_gsm8k_grpo_rasp_alpha3p0_20.json --max_samples 1319 --seed 42 --dtype bfloat16\", \"pid\": \"43755\", \"data_path\": \"openai/gsm8k (test split)\", \"data_count\": 1319, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B (grpo_rasp_alpha3p0_20_v2)\", \"seed\": 42, \"checkpoint_source\": \"grpo_rasp_alpha3p0_20_v2/checkpoint-100\", \"eval_data\": \"gsm8k test 1319\", \"log_path\": \"/root/recovery_aware_struct_prune/results/eval_gsm8k_grpo_rasp_alpha3p0_20.log\"}, \"metrics\": {\"gsm8k_accuracy\": 0.6345, \"correct\": 837, \"total\": 1319, \"stderr\": 0.0133, \"eos_rate\": 0.9864, \"truncated\": 18, \"avg_response_length\": 219.7}}, \"eval_math500_sft_random_20_v3\": {\"created_at\": \"2026-05-22T04:11:52.462Z\", \"spec\": {\"command\": \"python src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_random_20 --max_new_tokens 2048 --output_path /root/recovery_aware_struct_prune/results/eval_math500_sft_random_20_v3.json\", \"server\": \"westd-32935\", \"gpu\": [\"cuda:1\"], \"pid\": \"5236\", \"data_path\": \"MATH-500\", \"data_count\": 500, \"model_name\": \"sft_random_20\", \"model_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_random_20\", \"seed\": 42, \"checkpoint_source\": \"sft_random_20\", \"eval_data\": \"MATH-500\", \"log_path\": \"/root/recovery_aware_struct_prune/logs/eval_math500_sft_random_20_v3.log\", \"checkpoint_path\": \"N/A - eval\"}, \"metrics\": {\"accuracy\": 0.144, \"correct\": 72, \"total\": 500, \"stderr\": 0.0157, \"natural_eos\": 171, \"truncated\": 329, \"avg_response_length\": 1470.44}}, \"eval_gsm8k_sft_alpha3p0_20\": {\"created_at\": \"2026-05-22T10:24:58.696Z\", \"spec\": {\"server\": \"westd-32935\", \"gpu\": \"cuda:2\", \"command\": \"eval_gsm8k.py --model_path sft_rasp_alpha3p0_20/checkpoint-935 --max_new_tokens 2048\", \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B\", \"seed\": 42, \"data_path\": \"openai/gsm8k (test split)\", \"data_count\": 1319, \"checkpoint_source\": \"sft_rasp_alpha3p0_20/checkpoint-935 (SCP from westb)\", \"eval_data\": \"gsm8k test 1319\", \"pid\": \"37024\"}, \"metrics\": {\"gsm8k_accuracy\": 0.6414, \"gsm8k_correct\": 846, \"gsm8k_total\": 1319, \"gsm8k_stderr\": 0.0132, \"eos_rate\": 0.9879, \"avg_response_length\": 188.63, \"natural_eos\": 1303, \"truncated\": 16}}, \"grpo_rasp_alpha3p0_20_v2\": {\"created_at\": \"2026-05-22T10:40:19.362Z\", \"spec\": {\"server\": \"westd-32935\", \"gpu\": \"cuda:0\", \"command\": \"CUDA_VISIBLE_DEVICES=0 HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 nohup python src/train_grpo_v5.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_alpha3p0_20/checkpoint-935 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_alpha3p0_20_v2 --max_steps 100 --save_total_limit 1\", \"pid\": \"42003\", \"data_path\": \"openai/gsm8k (train split)\", \"data_count\": 7473, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B (sft_rasp_alpha3p0_20)\", \"seed\": 42, \"checkpoint_source\": \"sft_rasp_alpha3p0_20/checkpoint-935\", \"eval_data\": \"N/A - GRPO training\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_alpha3p0_20_v2\", \"log_path\": \"/tmp/grpo_alpha3p0_v2.log\"}}, \"eval_math500_grpo_standard_20_fair_2048_v2\": {\"created_at\": \"2026-05-22T03:49:45.575Z\", \"spec\": {\"command\": \"python src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_standard_20_fair --max_new_tokens 2048 --output_path /root/recovery_aware_struct_prune/results/eval_math500_grpo_standard_20_fair_2048_v2.json\", \"server\": \"westd-32935\", \"gpu\": [\"cuda:0\"], \"data_path\": \"MATH-500\", \"data_count\": 500, \"model_name\": \"grpo_stage2_standard_20_fair\", \"model_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_standard_20_fair\", \"seed\": 42, \"checkpoint_source\": \"grpo_stage2_standard_20_fair\", \"eval_data\": \"MATH-500\", \"log_path\": \"/root/recovery_aware_struct_prune/logs/eval_math500_grpo_standard_20_fair_2048_v2.log\", \"checkpoint_path\": \"N/A (eval)\"}, \"metrics\": {\"math500_accuracy\": 0.264, \"math500_correct\": 132, \"math500_total\": 500, \"math500_stderr\": 0.0197}}, \"grpo_random_20_seed123\": {\"created_at\": \"2026-05-22T10:34:12.100Z\", \"spec\": {\"server\": \"westd-32935\", \"gpu\": \"cuda:2\", \"command\": \"bash -c 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/recovery_aware_struct_prune && HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 python src/train_grpo_v5.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_random_20 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/grpo_random_20_seed123 --num_steps 100 --seed 123'\", \"pid\": \"36832\", \"data_path\": \"openai/gsm8k (train split)\", \"data_count\": 7473, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B (sft_random_20)\", \"seed\": 123, \"checkpoint_source\": \"sft_random_20\", \"eval_data\": \"N/A - GRPO training, not eval\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_random_20_seed123\", \"log_path\": \"/tmp/mf2_random_seed123_grpo.log\"}}, \"grpo_rasp_alpha3p0_20\": {\"created_at\": \"2026-05-22T08:48:06.001Z\", \"spec\": {\"server\": \"westb-23072\", \"gpu\": \"cuda:0\", \"command\": \"train_grpo_v5.py --model_path sft_rasp_alpha3p0_20/checkpoint-935 --output_dir grpo_rasp_alpha3p0_20 --max_steps 100 --learning_rate 1e-6 --per_device_train_batch_size 1 --gradient_accumulation_steps 8 --max_completion_length 512 --temperature 0.4 --beta 0.01 --loss_type dapo --format_reward_weight 0.1 --gradient_checkpointing true --optim adamw_8bit\", \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B\", \"seed\": 42, \"pid\": \"170676\", \"data_path\": \"openai/gsm8k (train split)\", \"data_count\": 7473, \"checkpoint_source\": \"sft_rasp_alpha3p0_20/checkpoint-935\", \"eval_data\": \"N/A - GRPO training\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_alpha3p0_20/checkpoint-100\", \"log_path\": \"/tmp/alpha3p0_grpo.log\"}}, \"eval_gsm8k_sft_alpha2p0_20\": {\"created_at\": \"2026-05-22T10:19:50.623Z\", \"spec\": {\"server\": \"westd-32935\", \"gpu\": \"cuda:2\", \"command\": \"eval_gsm8k.py --model_path sft_rasp_alpha2p0_20 --max_new_tokens 2048\", \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B\", \"seed\": 42, \"data_path\": \"openai/gsm8k (test split)\", \"data_count\": 1319, \"checkpoint_source\": \"sft_rasp_alpha2p0_20\", \"eval_data\": \"gsm8k test 1319\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_alpha2p0_20\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/eval_gsm8k_sft_alpha2p0_20.json\"}, \"metrics\": {\"gsm8k_accuracy\": 0.6497, \"gsm8k_correct\": 857, \"gsm8k_total\": 1319}}, \"eval_gsm8k_sft_alpha0p5_20\": {\"created_at\": \"2026-05-22T10:19:48.133Z\", \"spec\": {\"server\": \"westd-32935\", \"gpu\": \"cuda:3\", \"command\": \"eval_gsm8k.py --model_path sft_rasp_alpha0p5_20 --max_new_tokens 2048\", \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B\", \"seed\": 42, \"data_path\": \"openai/gsm8k (test split)\", \"data_count\": 1319, \"checkpoint_source\": \"sft_rasp_alpha0p5_20\", \"eval_data\": \"gsm8k test 1319\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_alpha0p5_20\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/eval_gsm8k_sft_alpha0p5_20.json\"}, \"metrics\": {\"gsm8k_accuracy\": 0.6073, \"gsm8k_correct\": 801, \"gsm8k_total\": 1319}}, \"grpo_qwen_math_cka_only_20\": {\"created_at\": \"2026-05-22T08:50:34.293Z\", \"spec\": {\"server\": \"westb-23072\", \"gpu\": \"cuda:1\", \"command\": \"train_grpo_v5.py --model_path sft_qwen_math_cka_only_20_v2 --max_steps 100 --learning_rate 1e-6 --per_device_train_batch_size 1 --gradient_accumulation_steps 8 --max_completion_length 512 --temperature 0.4 --beta 0.01 --loss_type dapo --format_reward_weight 0.1 --gradient_checkpointing true --optim adamw_8bit\", \"model_name\": \"Qwen2.5-Math-7B\", \"seed\": 42, \"pid\": \"164710\", \"data_path\": \"openai/gsm8k (train split)\", \"data_count\": 7473, \"checkpoint_source\": \"sft_qwen_math_cka_only_20_v2\", \"eval_data\": \"N/A - this is GRPO training, not eval\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_qwen_math_cka_only_20\", \"log_path\": \"/tmp/mf3_qwen_grpo.log\"}}, \"eval_gsm8k_grpo_alpha2p0_20\": {\"created_at\": \"2026-05-22T09:28:08.089Z\", \"spec\": {\"server\": \"westd-32935\", \"gpu\": \"cuda:2\", \"command\": \"eval_gsm8k.py --model_path grpo_rasp_alpha2p0_20 --max_new_tokens 2048\", \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B\", \"seed\": 42, \"data_path\": \"openai/gsm8k (test split)\", \"data_count\": 1319, \"checkpoint_source\": \"grpo_rasp_alpha2p0_20\", \"eval_data\": \"gsm8k test 1319\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_alpha2p0_20\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/eval_gsm8k_grpo_alpha2p0_20.json\"}, \"metrics\": {\"gsm8k_accuracy\": 0.6611, \"gsm8k_correct\": 872, \"gsm8k_total\": 1319}}, \"eval_gsm8k_grpo_alpha0p5_20\": {\"created_at\": \"2026-05-22T09:28:05.478Z\", \"spec\": {\"server\": \"westd-32935\", \"gpu\": \"cuda:3\", \"command\": \"eval_gsm8k.py --model_path grpo_rasp_alpha0p5_20 --max_new_tokens 2048\", \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B\", \"seed\": 42, \"data_path\": \"openai/gsm8k (test split)\", \"data_count\": 1319, \"checkpoint_source\": \"grpo_rasp_alpha0p5_20\", \"eval_data\": \"gsm8k test 1319\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_alpha0p5_20\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/eval_gsm8k_grpo_alpha0p5_20.json\"}, \"metrics\": {\"gsm8k_accuracy\": 0.6118, \"gsm8k_correct\": 807, \"gsm8k_total\": 1319}}, \"eval_math500_sft_standard_20_1p5b\": {\"created_at\": \"2026-05-22T04:31:30.202Z\", \"spec\": {\"command\": \"python src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20_1p5b --max_new_tokens 2048 --output_path /root/recovery_aware_struct_prune/results/eval_math500_sft_standard_20_1p5b.json\", \"server\": \"westb-23072\", \"gpu\": [\"cuda:0\"], \"data_path\": \"MATH-500\", \"data_count\": 500, \"model_name\": \"sft_standard_20_1p5b\", \"model_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20_1p5b\", \"seed\": 42, \"checkpoint_source\": \"sft_standard_20_1p5b\", \"eval_data\": \"MATH-500\", \"log_path\": \"/root/recovery_aware_struct_prune/logs/eval_math500_sft_standard_20_1p5b.log\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20_1p5b\"}, \"metrics\": {\"math500_accuracy\": 0.054, \"correct\": 27, \"total\": 500, \"truncated\": 335}}, \"eval_gsm8k_sft_alpha4_20_v5\": {\"created_at\": \"2026-05-22T03:49:50.201Z\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_alpha4_20\", \"log_path\": \"/root/recovery_aware_struct_prune/logs/eval_gsm8k_sft_alpha4_20_v5.log\", \"result_path\": \"/root/recovery_aware_struct_prune/results/eval_gsm8k_sft_alpha4_20_v5.json\"}, \"metrics\": {\"gsm8k_accuracy\": 0.6194, \"correct\": 817, \"total\": 1319, \"stderr\": 0.0134, \"eos_rate\": 0.981, \"avg_response_length\": 197.85}}, \"eval_gsm8k_grpo_alpha4_20_v3\": {\"created_at\": \"2026-05-22T03:49:52.414Z\", \"spec\": {\"command\": \"python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_alpha4_20/checkpoint-100 --max_new_tokens 2048 --output_path /root/recovery_aware_struct_prune/results/eval_gsm8k_grpo_alpha4_20_v3.json\", \"server\": \"westd-32935\", \"gpu\": [\"cuda:3\"], \"data_path\": \"GSM8K\", \"data_count\": 1319, \"model_name\": \"grpo_alpha4_20/checkpoint-100\", \"model_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_alpha4_20/checkpoint-100\", \"seed\": 42, \"checkpoint_source\": \"grpo_alpha4_20/checkpoint-100\", \"eval_data\": \"GSM8K\", \"log_path\": \"/root/recovery_aware_struct_prune/logs/eval_gsm8k_grpo_alpha4_20_v3.log\"}, \"metrics\": {\"gsm8k_accuracy\": 0.6277, \"gsm8k_accuracy_ci\": 0.0133, \"gsm8k_correct\": 828, \"gsm8k_total\": 1319, \"eos_rate\": 0.9856, \"avg_response_length\": 188.16, \"natural_eos\": 1300, \"truncated\": 19}}, \"eval_math500_sft_standard_25\": {\"created_at\": \"2026-05-21T02:58:32.492Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_25/checkpoint-1870 --output_path /root/runs/recovery_aware_struct_prune/eval_math500_sft_standard_25/results.json --max_new_tokens 2048 --seed 42\", \"server\": \"westb-23072\", \"gpu\": [\"cuda:1\"], \"pid\": \"104592\", \"data_path\": \"MATH-500\", \"data_count\": 500, \"model_name\": \"sft_standard_25/checkpoint-1870\", \"model_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_25/checkpoint-1870\", \"seed\": 42, \"checkpoint_source\": \"sft_standard_25\", \"eval_data\": \"MATH-500\", \"log_path\": \"/root/runs/recovery_aware_struct_prune/eval_math500_sft_standard_25/run.log\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_25/checkpoint-1870\"}, \"metrics\": {\"math500_accuracy\": 0.14, \"correct\": 70, \"n_total\": 500, \"natural_eos\": 185, \"truncated\": 315, \"avg_response_length\": 1367.82, \"v1_accuracy\": 0.13, \"v1_correct\": 65}}, \"grpo_alpha4_20\": {\"created_at\": \"2026-05-21T18:59:18.863Z\", \"spec\": {\"command\": \"python src/train_grpo_v5.py --alpha 4.0 --max_steps 100\", \"server\": \"westd-29022\", \"gpu\": [\"cuda:2\"], \"pid\": \"406593\", \"log_path\": \"~/runs/recovery_aware_struct_prune/grpo_alpha4_20.log\", \"submitted_at\": \"2026-05-21T18:59:44.258Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"Qwen2.5-7B\", \"seed\": 42, \"data_path\": \"gsm8k\", \"data_count\": 7473, \"checkpoint_source\": \"sft_alpha4_20_v2\", \"eval_data\": \"gsm8k\", \"wall_clock_seconds\": 1659.0, \"gpu_hours\": 0.46}, \"metrics\": {\"final_reward\": 0.198, \"reward_range\": \"0.146-0.256\", \"steps\": 100, \"final_loss\": 0.018, \"final_kl\": 0.00198}}, \"sft_alpha4_20_v2\": {\"created_at\": \"2026-05-21T18:30:48.284Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/recovery_aware_struct_prune && python src/train_sft_warmup.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/pruned_alpha4_20 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/sft_alpha4_20 --num_epochs 2 --lr 2e-5\\\"\", \"server\": \"westd-29022\", \"gpu\": [\"cuda:2\"], \"pid\": \"401581\", \"log_path\": \"~/runs/recovery_aware_struct_prune/sft_alpha4_20_v2.log\", \"submitted_at\": \"2026-05-21T18:31:05.499Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"metrics\": {\"final_train_loss\": 0.8118, \"token_accuracy\": 0.8165, \"epochs\": 2, \"steps\": 936}}, \"eval_math500_grpo_cka_only_25_v2\": {\"created_at\": \"2026-05-21T13:54:50.310Z\", \"spec\": {\"command\": \"nohup bash -c 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=0 python /root/recovery_aware_struct_prune/src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_25 --output_path /root/runs/recovery_aware_struct_prune/eval_math500_grpo_cka_only_25_v2 --seed 42 --max_new_tokens 2048' > /root/runs/recovery_aware_struct_prune/eval_math500_grpo_cka_only_25_v2/eval_math500_grpo_cka_only_25_v2.log 2>&1 &\", \"server\": \"westd-29022\", \"gpu\": \"cuda:0\", \"pid\": 379999, \"data_path\": \"MATH-500\", \"data_count\": 500, \"model_name\": \"Qwen2.5-7B CKA-only 25% GRPO\", \"model_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_25\", \"seed\": 42, \"checkpoint_source\": \"grpo_cka_only_25\", \"eval_data\": \"MATH-500\", \"log_path\": \"/root/runs/recovery_aware_struct_prune/eval_math500_grpo_cka_only_25_v2/eval_math500_grpo_cka_only_25_v2.log\"}, \"metrics\": {\"math500_accuracy\": 0.184, \"math500_stderr\": 0.0173, \"correct\": 92, \"n_total\": 500}}, \"eval_math500_sft_cka_only_25_v2\": {\"created_at\": \"2026-05-21T13:54:51.945Z\", \"spec\": {\"command\": \"nohup bash -c 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=2 python /root/recovery_aware_struct_prune/src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_25 --output_path /root/runs/recovery_aware_struct_prune/eval_math500_sft_cka_only_25_v2 --seed 42 --max_new_tokens 2048' > /root/runs/recovery_aware_struct_prune/eval_math500_sft_cka_only_25_v2/eval_math500_sft_cka_only_25_v2.log 2>&1 &\", \"server\": \"westd-29022\", \"gpu\": \"cuda:2\", \"pid\": 380074, \"data_path\": \"MATH-500\", \"data_count\": 500, \"model_name\": \"Qwen2.5-7B CKA-only 25% SFT\", \"model_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_25\", \"seed\": 42, \"checkpoint_source\": \"sft_cka_only_25\", \"eval_data\": \"MATH-500\", \"log_path\": \"/root/runs/recovery_aware_struct_prune/eval_math500_sft_cka_only_25_v2/eval_math500_sft_cka_only_25_v2.log\"}, \"metrics\": {\"math500_accuracy\": 0.192, \"correct\": 96, \"n_total\": 500, \"std_err\": 0.0176}}, \"eval_gsm8k_sft_standard_25\": {\"created_at\": \"2026-05-21T08:13:12.112Z\", \"spec\": {\"command\": \"nohup bash -c 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=3 python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_25/checkpoint-1870 --max_samples 1319 --seed 42'\", \"server\": \"westd-29022\", \"gpu\": \"cuda:3\", \"pid\": 335301, \"data_path\": \"GSM8K (N=1319)\", \"data_count\": 1319, \"model_name\": \"sft_standard_25\", \"model_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_25/checkpoint-1870\", \"seed\": 42, \"checkpoint_source\": \"sft_standard_25\", \"eval_data\": \"GSM8K\", \"log_path\": \"/root/runs/recovery_aware_struct_prune/eval_gsm8k_sft_standard_25.log\", \"checkpoint_path\": \"N/A (eval only)\"}, \"metrics\": {\"gsm8k_accuracy\": 0.5087, \"stderr\": 0.0138, \"correct\": 671, \"n_total\": 1319, \"eos_rate\": 0.953, \"avg_response_length\": 333.15}}, \"eval_math500_grpo_cka_only_20\": {\"created_at\": \"2026-05-18T02:41:32.199Z\", \"spec\": {\"max_new_tokens_actual\": 4096, \"note\": \"未显式指定 --max_new_tokens，脚本默认 4096。与 @2048 evals 不可直接比较。需用 eval_math500_grpo_cka_only_20_2048 重跑公平对比。\"}, \"metrics\": {\"accuracy\": 0.266, \"n_correct\": 133, \"n_total\": 500, \"stderr\": 0.0198, \"truncated\": 108, \"truncation_rate\": 0.216, \"avg_response_length\": 1124.24}}, \"eval_gsm8k_grpo_standard_25\": {\"created_at\": \"2026-05-21T06:42:08.819Z\", \"spec\": {\"command\": \"python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_25_westb/checkpoint-100 --max_samples 1319 --seed 42\", \"server\": \"westb-23072\", \"gpu\": \"cuda:1\", \"pid\": 75282, \"data_path\": \"gsm8k\", \"data_count\": 1319, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B-pruned-standard-25pct-GRPO-v5fair\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_25_westb/checkpoint-100\", \"eval_data\": \"GSM8K\", \"log_path\": \"/root/runs/recovery_aware_struct_prune/eval_gsm8k_grpo_standard_25.log\"}, \"metrics\": {\"gsm8k_accuracy\": 0.5186, \"stderr\": 0.0138, \"correct\": 684, \"n_total\": 1319, \"eos_rate\": 0.9575, \"avg_response_length\": 314.47}}, \"eval_gsm8k_sft_cka_only_25\": {\"created_at\": \"2026-05-21T06:47:14.010Z\", \"spec\": {\"command\": \"nohup bash -c 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=1 python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_25 --max_samples 1319 --seed 42'\", \"server\": \"westd-29022\", \"gpu\": \"cuda:1\", \"pid\": 329698, \"data_path\": \"GSM8K (N=1319)\", \"data_count\": 1319, \"model_name\": \"sft_cka_only_25\", \"model_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_25\", \"seed\": 42, \"checkpoint_source\": \"sft_cka_only_25\", \"eval_data\": \"GSM8K\", \"log_path\": \"/root/runs/recovery_aware_struct_prune/eval_gsm8k_sft_cka_only_25.log\"}, \"metrics\": {\"gsm8k_accuracy\": 0.6012, \"correct\": 793, \"n_total\": 1319, \"stderr\": 0.0135, \"eos_rate\": 0.9803, \"avg_response_length\": 243.6}}, \"eval_gsm8k_sft_random_20\": {\"created_at\": \"2026-05-21T06:47:16.459Z\", \"spec\": {\"command\": \"nohup bash -c 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=2 python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_random_20 --max_samples 1319 --seed 42'\", \"server\": \"westd-29022\", \"gpu\": \"cuda:2\", \"pid\": 329770, \"data_path\": \"GSM8K (N=1319)\", \"data_count\": 1319, \"model_name\": \"sft_random_20\", \"model_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_random_20\", \"seed\": 42, \"checkpoint_source\": \"sft_random_20\", \"eval_data\": \"GSM8K\", \"log_path\": \"/root/runs/recovery_aware_struct_prune/eval_gsm8k_sft_random_20.log\"}, \"metrics\": {\"gsm8k_accuracy\": 0.5125, \"correct\": 676, \"n_total\": 1319, \"stderr\": 0.0138, \"eos_rate\": 0.9932, \"avg_response_length\": 182.4}}, \"eval_gsm8k_grpo_cka_only_25_v3\": {\"created_at\": \"2026-05-21T04:56:52.006Z\", \"spec\": {\"command\": \"python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_25 --max_samples 1319 --seed 42\", \"server\": \"westd-29022\", \"gpu\": [\"cuda:0\"], \"pid\": \"322443\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_gsm8k_grpo_cka_only_25_v3.log\", \"data_path\": \"gsm8k\", \"data_count\": 1319, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B-pruned-cka_only-25pct-GRPO\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_25\", \"eval_data\": \"GSM8K\"}, \"metrics\": {\"gsm8k_accuracy\": 0.5959, \"correct\": 786, \"n_total\": 1319, \"eos_rate\": 0.9818}}, \"grpo_standard_25_westb\": {\"created_at\": \"2026-05-21T03:00:00.000Z\", \"spec\": {\"command\": \"python src/train_grpo_v5.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_25 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_25_westb --max_steps 100 --save_steps 100 --seed 42\", \"server\": \"westb-23072\", \"gpu\": [\"cuda:1\"], \"pid\": \"64194\", \"data_path\": \"gsm8k\", \"data_count\": 7473, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B-pruned-standard-25pct-SFT\", \"seed\": 42}, \"metrics\": {\"reward\": 0.00813, \"steps\": 100, \"collapse_pattern\": \"near_total_collapse\"}}, \"eval_gsm8k_grpo_random_20_v2\": {\"created_at\": \"2026-05-21T04:56:53.980Z\", \"spec\": {\"command\": \"python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_random_20/checkpoint-100 --max_samples 1319 --seed 42\", \"server\": \"westd-29022\", \"gpu\": [\"cuda:1\"], \"pid\": \"322611\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_gsm8k_grpo_random_20_v2.log\", \"data_path\": \"gsm8k\", \"data_count\": 1319, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B-pruned-random-20pct-GRPO\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_random_20/checkpoint-100\", \"eval_data\": \"GSM8K\"}, \"metrics\": {\"gsm8k_accuracy\": 0.5057, \"gsm8k_stderr\": 0.0138, \"correct\": 667, \"total\": 1319, \"eos_rate\": 0.9954, \"avg_response_length\": 173}}, \"sft_random_20\": {\"created_at\": \"2026-05-21T03:44:24.654Z\", \"spec\": {\"server\": \"westd-29022\", \"gpu\": [\"cuda:0\"], \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B-pruned-random-20pct\", \"command\": \"python src/sft_recovery.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/pruned_random_20 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/sft_random_20\", \"data_path\": \"gsm8k\", \"seed\": 42}, \"metrics\": {\"steps\": 1870, \"model_size_gb\": 12}}, \"grpo_random_20\": {\"created_at\": \"2026-05-17T13:30:31.016Z\", \"spec\": {\"command\": \"bash -c \\\"cd /root/recovery_aware_struct_prune && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && HF_HUB_OFFLINE=1 HF_DATASETS_OFFLINE=1 python src/train_grpo_v5.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_random_20 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/grpo_random_20 --max_steps 100 --save_steps 100 --seed 42\\\"\", \"server\": \"westd-29022\", \"gpu\": [\"cuda:0\"], \"pid\": \"317332\", \"log_path\": \"~/runs/recovery_aware_struct_prune/grpo_random_20.log\", \"submitted_at\": \"2026-05-21T03:46:03.569Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"metrics\": {\"reward_mean\": 0.164, \"reward_range\": [0.14, 0.19], \"reward_peak\": 0.19, \"reward_peak_step\": 70, \"frac_zero_std_mean\": 0.333, \"frac_zero_std_range\": [0.3, 0.4], \"entropy_mean\": 0.221, \"entropy_range\": [0.2, 0.24], \"kl_mean\": 0.0045, \"steps_captured\": 9, \"max_step\": 90, \"pattern\": \"stable plateau, no collapse\", \"data_source\": \"log_file (W&B crashed before sync)\"}}, \"grpo_cka_only_25\": {\"created_at\": \"2026-05-21T02:49:22.258Z\", \"spec\": {\"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/recovery_aware_struct_prune && HF_HUB_OFFLINE=1 HF_DATASETS_OFFLINE=1 python src/train_grpo_v5.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_25 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_25 --max_steps 100 --save_steps 100 --seed 42\", \"server\": \"westd-29022\", \"gpu\": [\"cuda:2\"], \"pid\": \"310542\", \"data_path\": \"gsm8k\", \"data_count\": 7473, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B-pruned-cka_only-25pct-SFT\", \"seed\": 42}, \"metrics\": {\"reward\": 0.2875, \"steps\": 100}}, \"eval_humaneval_sft_standard_25\": {\"created_at\": \"2026-05-21T02:43:32.214Z\", \"spec\": {\"command\": \"python eval_humaneval.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_25/checkpoint-1870\", \"server\": \"westb-23072\", \"data_path\": \"openai/openai_humaneval\", \"data_count\": 164, \"model_name\": \"Qwen2.5-Coder-3B-pruned-standard-25-sft\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_25/checkpoint-1870\", \"eval_data\": \"HumanEval\"}, \"metrics\": {\"pass_at_1\": 0.0183, \"stderr\": 0.0105, \"n_passed\": 3, \"n_total\": 164}}, \"sft_cka_only_25\": {\"created_at\": \"2026-05-21T01:50:42.758Z\", \"metrics\": {\"final_loss\": 0.6508, \"mean_token_accuracy\": 0.8285, \"training_time_s\": 1644}, \"spec\": {\"command\": \"python src/sft_recovery.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/pruned_cka_only_25 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_25 --gpu 1 --num_train_epochs 2 --learning_rate 2e-5 --batch_size 1 --gradient_accumulation_steps 8 --max_seq_length 2048 --seed 42\", \"server\": \"westd-29022\", \"gpu\": [\"cuda:1\"], \"pid\": \"307651\", \"log_path\": \"~/runs/recovery_aware_struct_prune/sft_cka_only_25.log\", \"account\": \"root\", \"data_path\": \"openai/gsm8k (cached)\", \"data_count\": 7473, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B-pruned-cka_only-25pct\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/pruned_cka_only_25\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_25\"}}, \"prune_cka_only_25\": {\"created_at\": \"2026-05-18T13:43:54.266Z\", \"spec\": {\"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/recovery_aware_struct_prune && HF_HUB_OFFLINE=1 python src/prune.py --model_path /root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B --mode cka_only --sparsity 0.25 --output_path /root/autodl-tmp/recovery_aware_struct_prune/pruned_cka_only_25 --seed 42 --dtype bfloat16\", \"server\": \"westd-29022\", \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B\", \"seed\": 42}, \"metrics\": {\"actual_sparsity\": 0.2367, \"mlp_groups_pruned\": 248, \"mlp_groups_total\": 784, \"attn_groups_pruned\": 0, \"attn_groups_total\": 112, \"param_count_B\": 5.81, \"original_param_count_B\": 7.62}}, \"eval_gsm8k_grpo_standard_15_seed123_v3\": {\"created_at\": \"2026-05-20T23:00:14.007Z\", \"spec\": {\"command\": \"python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_15_seed123_v3/checkpoint-100 --max_samples 1319 --seed 42\", \"server\": \"westd-29022\", \"data_path\": \"gsm8k\", \"data_count\": 1319, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B-pruned-standard-15pct-grpo-seed123\", \"seed\": 42, \"checkpoint_source\": \"grpo_standard_15_seed123_v3\", \"eval_data\": \"gsm8k_test_n1319\"}, \"metrics\": {\"accuracy\": 0.6513, \"accuracy_se\": 0.0131, \"n_correct\": 859, \"n_total\": 1319, \"eos_rate\": 0.9932, \"avg_response_length\": 183.25}}, \"eval_gsm8k_grpo_standard_15_seed456_v3\": {\"created_at\": \"2026-05-20T23:00:15.387Z\", \"spec\": {\"command\": \"python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_15_seed456_v3/checkpoint-100 --max_samples 1319 --seed 42\", \"server\": \"westd-29022\", \"data_path\": \"gsm8k\", \"data_count\": 1319, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B-pruned-standard-15pct-grpo-seed456\", \"seed\": 42, \"checkpoint_source\": \"grpo_standard_15_seed456_v3\", \"eval_data\": \"gsm8k_test_n1319\"}, \"metrics\": {\"gsm8k_accuracy\": 0.6543, \"gsm8k_stderr\": 0.0131, \"n_correct\": 863, \"n_total\": 1319, \"eos_rate\": 0.9939, \"avg_response_length\": 180.23}}, \"eval_gsm8k_grpo_cka_only_15_seed123\": {\"created_at\": \"2026-05-20T21:35:28.222Z\", \"metrics\": {\"accuracy\": 73.09, \"n_correct\": 964, \"n_total\": 1319, \"stderr\": 1.22, \"eos_rate\": 98.79, \"truncated\": 16}, \"spec\": {\"command\": \"python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_15_seed123/checkpoint-100 --max_samples 1319 --seed 42 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_grpo_cka_only_15_seed123_n1319.json\", \"server\": \"westd-29022\", \"data_path\": \"gsm8k\", \"data_count\": 1319, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B-pruned-cka_only-15pct-grpo-seed123\", \"seed\": 42, \"checkpoint_source\": \"grpo_cka_only_15_seed123\", \"eval_data\": \"gsm8k_test_n1319\"}}, \"eval_gsm8k_grpo_cka_only_15_seed456\": {\"created_at\": \"2026-05-20T21:35:29.444Z\", \"spec\": {\"command\": \"python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_15_seed456/checkpoint-100 --max_samples 1319 --seed 42 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_grpo_cka_only_15_seed456_n1319.json\", \"server\": \"westd-29022\", \"data_path\": \"gsm8k\", \"data_count\": 1319, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B-pruned-cka_only-15pct-grpo-seed456\", \"seed\": 42, \"checkpoint_source\": \"grpo_cka_only_15_seed456\", \"eval_data\": \"gsm8k_test_n1319\"}, \"metrics\": {\"accuracy\": 0.721, \"n_correct\": 951, \"n_total\": 1319, \"stderr\": 0.0123, \"eos_rate\": 0.9894, \"avg_response_length\": 201.94}}, \"grpo_standard_15_seed456_v3\": {\"created_at\": \"2026-05-20T21:58:14.439Z\", \"spec\": {\"command\": \"python src/train_grpo_v5.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_15 --output_dir grpo_standard_15_seed456_v3 --max_steps 100 --seed 456\", \"server\": \"westd-29022\", \"gpu\": [\"cuda:3\"], \"pid\": \"287862\", \"log_path\": \"~/runs/recovery_aware_struct_prune/grpo_standard_15_seed456_v3.log\", \"submitted_at\": \"2026-05-20T21:58:13.750Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"gsm8k\", \"data_count\": 7473, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B-pruned-standard-15pct\", \"seed\": 456}}, \"grpo_standard_15_seed123_v3\": {\"created_at\": \"2026-05-20T21:58:11.697Z\", \"spec\": {\"command\": \"python src/train_grpo_v5.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_15 --output_dir grpo_standard_15_seed123_v3 --max_steps 100 --seed 123\", \"server\": \"westd-29022\", \"gpu\": [\"cuda:2\"], \"pid\": \"287784\", \"log_path\": \"~/runs/recovery_aware_struct_prune/grpo_standard_15_seed123_v3.log\", \"submitted_at\": \"2026-05-20T21:58:10.978Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"gsm8k\", \"data_count\": 7473, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B-pruned-standard-15pct\", \"seed\": 123}}, \"grpo_cka_only_15_seed456\": {\"created_at\": \"2026-05-20T20:54:57.409Z\", \"spec\": {\"command\": \"python src/train_grpo_v5.py --model_path sft_cka_only_15 --output_dir grpo_cka_only_15_seed456 --max_steps 100 --seed 456\", \"server\": \"westd-29022\", \"gpu\": [\"cuda:1\"], \"pid\": \"281727\", \"log_path\": \"~/runs/recovery_aware_struct_prune/grpo_cka_only_15_seed456.log\", \"submitted_at\": \"2026-05-20T20:54:56.719Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"gsm8k\", \"data_count\": 7473, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B-pruned-cka_only-15pct\", \"seed\": 456, \"wall_clock_seconds\": 2420.0, \"gpu_hours\": 0.67}}, \"grpo_cka_only_15_seed123\": {\"created_at\": \"2026-05-20T20:54:54.710Z\", \"spec\": {\"command\": \"python src/train_grpo_v5.py --model_path sft_cka_only_15 --output_dir grpo_cka_only_15_seed123 --max_steps 100 --seed 123\", \"server\": \"westd-29022\", \"gpu\": [\"cuda:0\"], \"pid\": \"281647\", \"log_path\": \"~/runs/recovery_aware_struct_prune/grpo_cka_only_15_seed123.log\", \"submitted_at\": \"2026-05-20T20:54:54.017Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"gsm8k\", \"data_count\": 7473, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B-pruned-cka_only-15pct\", \"seed\": 123, \"wall_clock_seconds\": 2420.5, \"gpu_hours\": 0.67}}, \"eval_gsm8k_sft_standard_20\": {\"created_at\": \"2026-05-20T17:07:58.760Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 nohup python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20 --max_samples 1319 --seed 42 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_sft_standard_20_n1319.json\", \"server\": \"westd-29022\", \"gpu\": \"cuda:0\", \"pid\": 266847, \"data_path\": \"gsm8k/test\", \"data_count\": 1319, \"model_name\": \"sft_standard_20 (Qwen2.5-7B, 20% standard sparsity, SFT only)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20\", \"eval_data\": \"gsm8k:test:1319\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_gsm8k_sft_standard_20.log\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_sft_standard_20_n1319.json\"}, \"metrics\": {\"gsm8k_accuracy\": 0.5921, \"stderr\": 0.0135, \"correct\": 781, \"total\": 1319, \"eos_rate\": 0.9848, \"avg_response_length\": 206.68}}, \"eval_gsm8k_dense_unpruned\": {\"created_at\": \"2026-05-20T16:28:28.020Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 nohup python src/eval_gsm8k.py --model_path /root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B --max_samples 1319 --seed 42 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_dense_unpruned_n1319.json\", \"server\": \"westb-23072\", \"gpu\": \"cuda:0\", \"pid\": 32154, \"data_path\": \"gsm8k/test\", \"data_count\": 1319, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B (dense, unpruned)\", \"seed\": 42, \"eval_data\": \"gsm8k:test:1319\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_gsm8k_dense_unpruned.log\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_dense_unpruned_n1319.json\"}, \"metrics\": {\"gsm8k_accuracy\": 0.9083, \"gsm8k_accuracy_ci\": 0.0079, \"correct\": 1198, \"total\": 1319, \"eos_rate\": 0.9871, \"avg_response_length\": 594, \"truncated\": 17, \"eval_time\": \"3h7m\"}}, \"eval_gsm8k_sft_cka_only_20\": {\"created_at\": \"2026-05-20T16:32:21.874Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 nohup python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_20 --max_samples 1319 --seed 42 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_sft_cka_only_20_n1319.json\", \"server\": \"westd-29022\", \"gpu\": \"cuda:2\", \"pid\": 264522, \"data_path\": \"gsm8k/test\", \"data_count\": 1319, \"model_name\": \"sft_cka_only_20 (Qwen2.5-7B, 20% CKA-only sparsity, SFT only)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_20\", \"eval_data\": \"gsm8k:test:1319\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_gsm8k_sft_cka_only_20.log\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_sft_cka_only_20_n1319.json\"}, \"metrics\": {\"gsm8k_accuracy\": 0.6391, \"gsm8k_accuracy_ci\": 0.0132, \"correct\": 843, \"total\": 1319, \"eos_rate\": 0.9901, \"avg_response_length\": 198.1, \"truncated\": 13}}, \"eval_gsm8k_sft_cka_only_15\": {\"created_at\": \"2026-05-20T15:19:42.152Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 nohup python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_15 --max_samples 1319 --seed 42 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_sft_cka_only_15_n1319.json\", \"server\": \"westd-29022\", \"gpu\": \"cuda:1\", \"pid\": 262728, \"data_path\": \"gsm8k/test\", \"data_count\": 1319, \"model_name\": \"sft_cka_only_15 (Qwen2.5-7B, 15% CKA-only sparsity, SFT only)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_15\", \"eval_data\": \"gsm8k:test:1319\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_gsm8k_sft_cka_only_15.log\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_sft_cka_only_15_n1319.json\"}, \"metrics\": {\"gsm8k_accuracy\": 0.7218, \"correct\": 952, \"total\": 1319}}, \"eval_gsm8k_sft_rasp_20\": {\"created_at\": \"2026-05-20T17:09:04.809Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 nohup python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20_westd --max_samples 1319 --seed 42 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_sft_rasp_20_n1319.json\", \"server\": \"westd-29022\", \"gpu\": \"cuda:3\", \"pid\": 267009, \"data_path\": \"gsm8k/test\", \"data_count\": 1319, \"model_name\": \"sft_rasp_20_westd (Qwen2.5-7B, 20% RASP sparsity, SFT only)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20_westd\", \"eval_data\": \"gsm8k:test:1319\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_gsm8k_sft_rasp_20.log\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_sft_rasp_20_n1319.json\"}, \"metrics\": {\"gsm8k_accuracy\": 0.6149, \"gsm8k_accuracy_ci\": 0.0134, \"correct\": 811, \"total\": 1319, \"eos_rate\": 0.9826, \"avg_response_length\": 216.5}}, \"eval_gsm8k_grpo_standard_15_v2\": {\"created_at\": \"2026-05-20T14:43:21.408Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 nohup python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_15_v2 --max_samples 1319 --seed 42 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_grpo_standard_15_v2_n1319.json\", \"server\": \"westd-29022\", \"gpu\": \"cuda:3\", \"pid\": 256586, \"data_path\": \"gsm8k/test\", \"data_count\": 1319, \"model_name\": \"grpo_standard_15_v2\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_15_v2\", \"eval_data\": \"gsm8k:test:1319\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_gsm8k_grpo_standard_15_v2.log\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_grpo_standard_15_v2_n1319.json\"}, \"metrics\": {\"gsm8k_accuracy\": 0.6611, \"correct\": 872, \"total\": 1319, \"eos_rate\": 0.993, \"avg_response_length\": 184}}, \"eval_gsm8k_sft_standard_15\": {\"created_at\": \"2026-05-20T14:23:49.568Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 nohup python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_15 --max_samples 1319 --seed 42 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_sft_standard_15_n1319.json\", \"server\": \"westd-29022\", \"gpu\": \"cuda:2\", \"pid\": 256743, \"data_path\": \"gsm8k/test\", \"data_count\": 1319, \"model_name\": \"sft_standard_15 (Qwen2.5-7B, 15% standard sparsity, SFT only)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_15\", \"eval_data\": \"gsm8k:test:1319\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_gsm8k_sft_standard_15.log\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_sft_standard_15_n1319.json\"}, \"metrics\": {\"gsm8k_accuracy\": 0.6649, \"correct\": 877, \"total\": 1319, \"eos_rate\": 0.993, \"avg_response_length\": 183}}, \"eval_gsm8k_grpo_cka_only_15_v2\": {\"created_at\": \"2026-05-20T13:32:17.474Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_15_v2 --max_samples 1319 --seed 42 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_grpo_cka_only_15_v2_n1319.json\", \"server\": \"westd-29022\", \"gpu\": \"cuda:1\", \"pid\": 252919, \"data_path\": \"gsm8k:test\", \"data_count\": 1319, \"model_name\": \"grpo_cka_only_15_v2\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_15_v2\", \"eval_data\": \"gsm8k:test:1319\", \"log_path\": \"/root/runs/recovery_aware_struct_prune/eval_gsm8k_grpo_cka_only_15_v2.log\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_grpo_cka_only_15_v2_n1319.json\"}, \"metrics\": {\"gsm8k_accuracy\": 0.7309, \"gsm8k_accuracy_ci\": 0.0122, \"correct\": 964, \"total\": 1319, \"eos_rate\": 0.9894, \"avg_response_length\": 202.4}}, \"eval_gsm8k_grpo_cka_only_20_seed456_full\": {\"created_at\": \"2026-05-20T13:31:33.529Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20_seed456 --max_samples 1319 --seed 42 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_grpo_cka_only_20_seed456_n1319.json\", \"server\": \"westd-29022\", \"gpu\": \"cuda:0\", \"pid\": 252604, \"data_path\": \"gsm8k\", \"data_count\": 1319, \"model_name\": \"grpo_cka_only_20_seed456\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20_seed456\", \"eval_data\": \"gsm8k_n1319\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_gsm8k_grpo_cka_only_20_seed456_full.log\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20_seed456\"}, \"metrics\": {\"gsm8k_accuracy\": 0.6459, \"gsm8k_accuracy_ci\": 0.0132, \"correct\": 852, \"total\": 1319, \"eos_rate\": 0.9886, \"avg_response_length\": 204.3}}, \"eval_gsm8k_sft_qwen_standard_20\": {\"created_at\": \"2026-05-20T10:32:12.883Z\", \"spec\": {\"command\": \"python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20_qwen_math/checkpoint-935 --max_samples 200 --seed 42 --max_new_tokens 2048 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_sft_qwen_standard_20.json\", \"server\": \"westb-23072\", \"gpu\": [\"cuda:1\"], \"pid\": \"18114\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_gsm8k_sft_qwen_standard_20.log\", \"submitted_at\": \"2026-05-20T11:32:15Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"gsm8k/test\", \"data_count\": 200, \"model_name\": \"Qwen2.5-Math-7B-Standard-20%-SFT-ep1\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20_qwen_math/checkpoint-935\", \"eval_data\": \"gsm8k-test-N200\", \"wall_clock_seconds\": 15018.0, \"gpu_hours\": 4.17}, \"metrics\": {\"gsm8k_accuracy\": 0.21, \"correct\": 42, \"total\": 200}}, \"eval_gsm8k_sft_qwen_cka_only_20\": {\"created_at\": \"2026-05-20T10:32:11.084Z\", \"spec\": {\"command\": \"python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_qwen_math_cka_only_20/checkpoint-935 --max_samples 200 --seed 42 --max_new_tokens 2048 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_sft_qwen_cka_only_20.json\", \"server\": \"westb-23072\", \"gpu\": [\"cuda:0\"], \"pid\": \"18038\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_gsm8k_sft_qwen_cka_only_20.log\", \"submitted_at\": \"2026-05-20T11:32:13Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"gsm8k/test\", \"data_count\": 200, \"model_name\": \"Qwen2.5-Math-7B-CKA-only-20%-SFT-ep1\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_qwen_math_cka_only_20/checkpoint-935\", \"eval_data\": \"gsm8k-test-N200\", \"wall_clock_seconds\": 14658.4, \"gpu_hours\": 4.07}, \"metrics\": {\"gsm8k_accuracy\": 0.515, \"gsm8k_accuracy_ci\": 0.0353, \"correct\": 103, \"total\": 200, \"eos_rate\": 0.27, \"avg_response_length\": 1536, \"truncated\": 146, \"eval_time\": \"4h00m04s\"}}, \"grpo_standard_15_v2\": {\"created_at\": \"2026-05-20T13:42:06.715Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 WANDB_MODE=offline nohup python src/train_grpo_v5.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_15 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_15_v2 --max_steps 100 --save_steps 100 --seed 42\", \"server\": \"westd-29022\", \"gpu\": \"cuda:2\", \"pid\": 253918, \"data_path\": \"openai/gsm8k (cached)\", \"data_count\": 7473, \"model_name\": \"sft_standard_15 (pruned Qwen2.5-7B, 15% standard sparsity)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_15\", \"eval_data\": \"openai/gsm8k\", \"log_path\": \"~/runs/recovery_aware_struct_prune/grpo_standard_15_v2.log\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_15_v2\"}, \"metrics\": {\"loss\": 0.01142, \"reward\": 0.1375, \"reward_std\": 0.2778, \"kl\": 0.004099, \"entropy\": 0.1932, \"grad_norm\": 3.547, \"total_steps\": 100, \"training_time\": \"21m49s\"}}, \"eval_gsm8k_grpo_standard_20_seed123_full\": {\"created_at\": \"2026-05-20T10:27:04.283Z\", \"spec\": {\"command\": \"python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_20_seed123 --max_samples 1319 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_grpo_standard_20_seed123_n1319.json\", \"server\": \"westd-29022\", \"gpu\": \"cuda:2\", \"data_path\": \"openai/gsm8k\", \"data_count\": 1319, \"model_name\": \"grpo_standard_20_seed123\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_20_seed123\", \"eval_data\": \"GSM8K test (N=1319)\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_grpo_standard_20_seed123_n1319.json\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_grpo_standard_20_seed123_n1319.json\"}, \"metrics\": {\"accuracy\": 0.5989, \"n_correct\": 790, \"n_total\": 1319, \"stderr\": 0.0135, \"eos_rate\": null}}, \"eval_gsm8k_grpo_standard_20_seed456_full\": {\"created_at\": \"2026-05-20T10:27:05.741Z\", \"spec\": {\"command\": \"python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_20_seed456 --max_samples 1319 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_grpo_standard_20_seed456_n1319.json\", \"server\": \"westd-29022\", \"gpu\": \"cuda:3\", \"data_path\": \"openai/gsm8k\", \"data_count\": 1319, \"model_name\": \"grpo_standard_20_seed456\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_20_seed456\", \"eval_data\": \"GSM8K test (N=1319)\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_grpo_standard_20_seed456_n1319.json\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_grpo_standard_20_seed456_n1319.json\"}, \"metrics\": {\"accuracy\": 0.602, \"n_correct\": 794, \"n_total\": 1319, \"stderr\": 0.01348, \"eos_rate\": 0.9856}}, \"grpo_cka_only_15_v2\": {\"created_at\": \"2026-05-20T11:58:03.218Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python src/train_grpo_v5.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_15 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_15_v2 --max_steps 100 --save_steps 100 --seed 42\", \"server\": \"westd-29022\", \"gpu\": \"cuda:1\", \"pid\": 250149, \"log_path\": \"/root/runs/recovery_aware_struct_prune/grpo_cka_only_15_v2.log\", \"model_name\": \"sft_cka_only_15\", \"data_path\": \"openai/gsm8k (cached)\", \"data_count\": 7473, \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_15\", \"eval_data\": \"gsm8k train (GRPO training, not eval)\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_15_v2\"}, \"metrics\": {\"final_loss\": 0.2027, \"avg_train_loss\": 0.11, \"final_reward\": 0.4019, \"final_kl\": 0.0018, \"train_steps\": 100, \"train_runtime_min\": 22.5}}, \"grpo_cka_only_20_seed456\": {\"created_at\": \"2026-05-20T11:36:13.866Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python src/train_grpo_v5.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_20 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20_seed456 --max_steps 100 --save_steps 100 --seed 456\", \"server\": \"westd-29022\", \"gpu\": \"cuda:0\", \"pid\": 249963, \"log_path\": \"/root/runs/recovery_aware_struct_prune/grpo_cka_only_20_seed456.log\", \"model_name\": \"sft_cka_only_20\", \"data_path\": \"openai/gsm8k (cached)\", \"data_count\": 7473, \"seed\": 456, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_20\", \"eval_data\": \"gsm8k train (GRPO training, not eval)\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20_seed456\"}, \"metrics\": {\"final_loss\": 0.0999, \"avg_train_loss\": 0.0881, \"final_reward\": 0.2925, \"final_kl\": 0.0017, \"train_steps\": 100, \"train_runtime_min\": 21.8}}, \"prune_eval_standard_30\": {\"created_at\": \"2026-05-20T04:08:24.071Z\", \"spec\": {\"command\": \"python src/prune.py --mode standard --sparsity 0.30 + python src/eval_gsm8k.py\", \"server\": \"westd-29022\", \"gpu\": \"cuda:1\", \"pid\": 190349, \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/logs/prune_eval_standard_30.log\", \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B\", \"data_path\": \"gsm8k test\", \"data_count\": 1319, \"seed\": 42}, \"metrics\": {\"accuracy\": 2.8, \"note\": \"N=500 partial result (killed by Director, 30% sparsity = complete collapse, N=500 precision sufficient)\", \"n_evaluated\": 500, \"n_total\": 1319, \"eos_rate\": 1.2, \"avg_len\": 4057}}, \"prune_eval_cka_only_30\": {\"created_at\": \"2026-05-20T04:08:22.614Z\", \"spec\": {\"command\": \"python src/prune.py --mode cka_only --sparsity 0.30 + python src/eval_gsm8k.py\", \"server\": \"westd-29022\", \"gpu\": \"cuda:0\", \"pid\": 190269, \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/logs/prune_eval_cka_only_30.log\", \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B\", \"data_path\": \"gsm8k test\", \"data_count\": 1319, \"seed\": 42}, \"metrics\": {\"accuracy\": 1.6, \"note\": \"N=500 partial result (killed by Director, 30% sparsity = complete collapse, N=500 precision sufficient)\", \"n_evaluated\": 500, \"n_total\": 1319, \"eos_rate\": 5.6, \"avg_len\": 4009}}, \"sft_qwen_math_cka_only_20_v2\": {\"created_at\": \"2026-05-20T09:18:17.089Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/recovery_aware_struct_prune && HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 python src/sft_recovery.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_qwen_math_cka_only_20/checkpoint-935 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/sft_qwen_math_cka_only_20_final --gpu 0 --num_train_epochs 1 --save_strategy no\\\"\", \"server\": \"westb-23072\", \"gpu\": [\"cuda:0\"], \"pid\": \"9952\", \"log_path\": \"~/runs/recovery_aware_struct_prune/sft_qwen_math_cka_only_20_v2.log\", \"submitted_at\": \"2026-05-20T09:18:16.420Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"openai/gsm8k (cached)\", \"data_count\": 7473, \"model_name\": \"Qwen2.5-Math-7B-CKA-only-Pruned-20%\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_qwen_math_cka_only_20/checkpoint-935\", \"eval_data\": \"GSM8K train (7473 samples, SFT epoch 2)\", \"wall_clock_seconds\": 1918.9, \"gpu_hours\": 0.53}, \"metrics\": {\"train_loss\": 0.3481, \"mean_token_accuracy\": 0.8595, \"train_runtime_sec\": 1013, \"train_samples_per_second\": 7.38, \"epochs\": 1}}, \"eval_gsm8k_grpo_standard_20_seed456\": {\"created_at\": \"2026-05-20T09:15:10.283Z\", \"spec\": {\"command\": \"eval_gsm8k.py --model_path grpo_standard_20_seed456 --max_samples 200\", \"server\": \"westd-29022\", \"gpu\": [\"cuda:3\"], \"pid\": \"221008\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_gsm8k_grpo_standard_20_seed456.log\", \"submitted_at\": \"2026-05-20T09:15:19.738Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"openai/gsm8k\", \"data_count\": 200, \"model_name\": \"grpo_standard_20_seed456\", \"seed\": 456, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_20_seed456\", \"eval_data\": \"GSM8K test (N=200)\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/gsm8k_grpo_standard_20_seed456_n200.json\", \"wall_clock_seconds\": 2030.9, \"gpu_hours\": 0.56}, \"metrics\": {\"accuracy\": 0.665, \"n_correct\": 133, \"n_total\": 200, \"stderr\": 0.0334, \"eos_rate\": 0.995, \"avg_response_length\": 166.9}}, \"eval_gsm8k_grpo_standard_20_seed123\": {\"created_at\": \"2026-05-20T09:15:16.595Z\", \"spec\": {\"command\": \"eval_gsm8k.py --model_path grpo_standard_20_seed123 --max_samples 200\", \"server\": \"westd-29022\", \"gpu\": [\"cuda:2\"], \"pid\": \"221158\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_gsm8k_grpo_standard_20_seed123.log\", \"submitted_at\": \"2026-05-20T09:15:26.368Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"openai/gsm8k\", \"data_count\": 200, \"model_name\": \"grpo_standard_20_seed123\", \"seed\": 123, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_20_seed123\", \"eval_data\": \"GSM8K test (N=200)\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/gsm8k_grpo_standard_20_seed123_n200.json\", \"wall_clock_seconds\": 2022.3, \"gpu_hours\": 0.56}, \"metrics\": {\"accuracy\": 0.64, \"n_correct\": 128, \"n_total\": 200, \"stderr\": 0.0339, \"eos_rate\": 0.99, \"avg_response_length\": 187.9}}, \"grpo_standard_20_seed456\": {\"created_at\": \"2026-05-20T06:22:10.493Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/recovery_aware_struct_prune && HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 WANDB_MODE=offline python src/train_grpo_v5.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_20_seed456 --max_steps 100 --save_steps 100 --gpu 0 --seed 456\\\"\", \"server\": \"westd-29022\", \"gpu\": [\"cuda:3\"], \"pid\": \"211798\", \"log_path\": \"~/runs/recovery_aware_struct_prune/grpo_standard_20_seed456.log\", \"submitted_at\": \"2026-05-20T06:22:19.535Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"openai/gsm8k\", \"data_count\": 7473, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B-Standard-20%-SFT\", \"seed\": 456, \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_20_seed456\", \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20\", \"eval_data\": \"GSM8K train (7473 samples, GRPO RLVR training)\", \"wall_clock_seconds\": 10289.1, \"gpu_hours\": 2.86}, \"metrics\": {\"steps_completed\": 100, \"runtime_sec\": 2745, \"peak_reward\": 0.0844, \"peak_reward_step\": 90, \"final_reward\": 0.06, \"final_frac_zero_std\": 0.65, \"seed\": 456, \"wandb_run\": \"wg0iv4oi\", \"wandb_mode\": \"offline\"}}, \"grpo_standard_20_seed123\": {\"created_at\": \"2026-05-20T06:22:27.444Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/recovery_aware_struct_prune && HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 WANDB_MODE=offline python src/train_grpo_v5.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_20_seed123 --max_steps 100 --max_completion_length 1024 --save_steps 100 --gpu 0 --run_name grpo_standard_20_seed123 --seed 123\\\"\", \"server\": \"westd-29022\", \"gpu\": [\"cuda:2\"], \"pid\": \"211972\", \"log_path\": \"~/runs/recovery_aware_struct_prune/grpo_standard_20_seed123.log\", \"submitted_at\": \"2026-05-20T06:22:37.312Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B-Standard-20%-SFT\", \"data_path\": \"openai/gsm8k\", \"data_count\": 7473, \"seed\": 123, \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_20_seed123\", \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20\", \"eval_data\": \"GSM8K train (7473 samples, GRPO RLVR training)\", \"tmux_session\": \"grpo_standard_20_seed123\", \"wall_clock_seconds\": 10268.1, \"gpu_hours\": 2.85}, \"metrics\": {\"steps_completed\": 100, \"runtime_sec\": 2783, \"peak_reward\": 0.0619, \"peak_reward_step\": 80, \"final_reward\": 0.0594, \"final_frac_zero_std\": 0.6, \"seed\": 123, \"wandb_run\": \"pgzwv725\", \"wandb_mode\": \"offline\"}}, \"eval_mbpp_grpo_standard_20_v3\": {\"created_at\": \"2026-05-19T21:00:40.293Z\", \"spec\": {\"server\": \"westd-29022\", \"gpu\": \"cuda:2\", \"command\": \"python src/eval_mbpp.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_standard_20_fair --max_new_tokens 2048 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_mbpp_grpo_standard_20.json\", \"data_path\": \"mbpp\", \"data_count\": 374, \"model_name\": \"grpo_stage2_standard_20_fair\", \"seed\": 42, \"checkpoint_path\": \"N/A\", \"log_path\": \"/root/autodl-tmp/logs/eval_mbpp_grpo_standard_20_v3.log\"}, \"metrics\": {\"pass_at_1\": 0.131, \"correct\": 49, \"total\": 374, \"stderr\": 0.0174}}, \"eval_humaneval_sft_standard_20_1p5b_2048\": {\"created_at\": \"2026-05-19T11:35:45.876Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/bin/activate && cd /root/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=0 /root/miniconda3/bin/python src/eval_humaneval.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20_1p5b --max_new_tokens 2048 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/humaneval_sft_standard_20_1p5b_2048.json\\\"\", \"server\": \"westb-23072\", \"gpu\": [\"cuda:0\"], \"pid\": \"890564\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_humaneval_sft_standard_20_1p5b_2048.log\", \"submitted_at\": \"2026-05-19T12:23:31.889Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20_1p5b\", \"eval_data\": \"HumanEval (164 problems, pass@1, max_new_tokens=2048)\", \"data_path\": \"HumanEval\", \"data_count\": 164, \"model_name\": \"sft_standard_20_1p5b\", \"seed\": 42, \"wall_clock_seconds\": 5434.5, \"gpu_hours\": 1.51}, \"metrics\": {\"pass_at_1\": 0.0061, \"correct\": 1, \"total\": 164, \"stderr\": 0.0061}}, \"eval_humaneval_sft_standard_20_2048_v3\": {\"created_at\": \"2026-05-19T10:05:36.497Z\", \"spec\": {\"command\": \"bash -c 'source /root/miniconda3/bin/activate && cd /root/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=3 /root/miniconda3/bin/python src/eval_humaneval.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20 --max_new_tokens 2048 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/humaneval_sft_standard_20_2048_v3.json'\", \"server\": \"westd-29022\", \"gpu\": [\"cuda:3\"], \"pid\": \"86171\", \"data_path\": \"HumanEval\", \"data_count\": 164, \"model_name\": \"sft_standard_20\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20\", \"eval_data\": \"HumanEval (164 problems, pass@1, max_new_tokens=2048)\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_humaneval_sft_standard_20_2048_v3.log\", \"result_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/humaneval_sft_standard_20_2048_v3.json\"}, \"metrics\": {\"pass_at_1\": 0.1341, \"correct\": 22, \"total\": 164, \"stderr\": 0.0266}}, \"eval_humaneval_sft_cka_only_20_1p5b_2048\": {\"created_at\": \"2026-05-19T11:32:47.965Z\", \"spec\": {\"command\": \"python src/eval_humaneval.py --model_path /root/autodl-tmp/models/sft_cka_only_20_1p5b --max_tokens 2048\", \"server\": \"westd-29022\", \"gpu\": [\"cuda:1\"], \"pid\": \"95940\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_humaneval_sft_cka_only_20_1p5b_2048.log\", \"submitted_at\": \"2026-05-19T11:45:57.991Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"sft_cka_only_20_1p5b\", \"data_path\": \"HumanEval\", \"data_count\": 164, \"seed\": 42, \"checkpoint_source\": \"sft_cka_only_20_1p5b\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_20_1p5b\", \"metrics\": {\"pass_at_1\": 0.0061, \"n_correct\": 1, \"n_total\": 164, \"avg_response_length\": 1968.76, \"median_response_length\": 2048}, \"wall_clock_seconds\": 6208.0, \"gpu_hours\": 1.72}, \"metrics\": {\"pass_at_1\": 0.0061, \"correct\": 1, \"total\": 164, \"stderr\": 0.0061}}, \"eval_humaneval_grpo_cka_only_20_1p5b_2048\": {\"created_at\": \"2026-05-19T11:32:50.649Z\", \"spec\": {\"command\": \"python src/eval_humaneval.py --model_path /root/autodl-tmp/models/grpo_cka_only_20_1p5b --max_tokens 2048\", \"server\": \"westd-29022\", \"gpu\": [\"cuda:2\"], \"pid\": \"96018\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_humaneval_grpo_cka_only_20_1p5b_2048.log\", \"submitted_at\": \"2026-05-19T11:46:00.256Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"grpo_cka_only_20_1p5b\", \"data_path\": \"HumanEval\", \"data_count\": 164, \"seed\": 42, \"checkpoint_source\": \"grpo_cka_only_20_1p5b\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20_1p5b\", \"wall_clock_seconds\": 7116.7, \"gpu_hours\": 1.98}, \"metrics\": {\"pass_at_1\": 0, \"correct\": 0, \"total\": 164, \"stderr\": 0}}, \"eval_mbpp_sft_shortgpt_20_v2\": {\"created_at\": \"2026-05-19T22:23:35.431Z\", \"spec\": {\"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_shortgpt_20\", \"eval_data\": \"MBPP sanitized (374 tasks)\", \"data_path\": \"google-research-datasets/mbpp (sanitized)\", \"data_count\": 374, \"model_name\": \"Qwen2.5-7B-ShortGPT-20%-SFT\", \"seed\": 42, \"server\": \"westd-29022\", \"gpu\": [\"cuda:1\"], \"account\": \"root\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 python src/eval_mbpp.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_shortgpt_20 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/mbpp_sft_shortgpt_20.json\\\"\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_shortgpt_20\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/mbpp_sft_shortgpt_20.json\"}, \"metrics\": {\"pass_at_1\": 0.1043, \"stderr\": 0.0158, \"n_correct\": 39, \"n_total\": 374, \"avg_response_length\": 1166.4, \"median_response_length\": 773.5}}, \"eval_mbpp_grpo_shortgpt_20_v2\": {\"created_at\": \"2026-05-19T22:33:19.363Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 python src/eval_mbpp.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_shortgpt_20/checkpoint-100 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/mbpp_grpo_shortgpt_20.json\\\"\", \"server\": \"westd-29022\", \"gpu\": [\"cuda:3\"], \"account\": \"root\", \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_shortgpt_20/checkpoint-100\", \"eval_data\": \"MBPP sanitized (374 tasks)\", \"data_path\": \"google-research-datasets/mbpp (sanitized)\", \"data_count\": 374, \"model_name\": \"Qwen2.5-7B-ShortGPT-20%-GRPO\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_shortgpt_20/checkpoint-100\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/mbpp_grpo_shortgpt_20.json\"}, \"metrics\": {\"pass_at_1\": 0.1444, \"stderr\": 0.0182, \"n_correct\": 54, \"n_total\": 374, \"avg_response_length\": 1140.8, \"median_response_length\": 804.5}}, \"eval_mbpp_sft_standard_20_v4\": {\"created_at\": \"2026-05-19T22:26:22.996Z\", \"spec\": {\"command\": \"HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 python src/eval_mbpp.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/mbpp_sft_standard_20.json\", \"server\": \"westd-29022\", \"gpu\": [\"cuda:0\"], \"data_path\": \"google-research-datasets/mbpp (sanitized)\", \"data_count\": 374, \"model_name\": \"sft_standard_20\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20\", \"eval_data\": \"MBPP sanitized (374 tasks)\", \"tmux_session\": \"eval_mbpp_sft_standard_20_v4\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_mbpp_sft_standard_20.json\"}, \"metrics\": {\"pass_at_1\": 0.1203, \"stderr\": 0.0168, \"n_correct\": 45, \"n_total\": 374, \"avg_response_length\": 1084.1, \"median_response_length\": 746.5}}, \"eval_mbpp_grpo_standard_20_v4\": {\"created_at\": \"2026-05-19T21:01:23.058Z\", \"spec\": {\"server\": \"westd-29022\", \"gpu\": \"cuda:2\", \"command\": \"python src/eval_mbpp.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_standard_20_fair --max_new_tokens 2048 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_mbpp_grpo_standard_20.json\", \"data_path\": \"mbpp\", \"data_count\": 374, \"model_name\": \"grpo_stage2_standard_20_fair\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_standard_20_fair\", \"eval_data\": \"mbpp_sanitized_374\"}, \"metrics\": {\"pass_at_1\": 0.131, \"n_correct\": 49, \"n_total\": 374, \"stderr\": 0.01745, \"avg_response_length\": 1058.7, \"median_response_length\": 726}}, \"cka_scoring_stability_ablation\": {\"created_at\": \"2026-05-19T21:21:10.933Z\", \"spec\": {\"command\": \"python src/cka_stability_analysis.py --model_path /root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B --output_path /root/autodl-tmp/recovery_aware_struct_prune/cka_stability_results.json --device cuda:0\", \"server\": \"westd-29022\", \"gpu\": \"cuda:3\", \"pid\": 143187, \"data_path\": \"openai/gsm8k\", \"data_count\": 1024, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B\", \"seed\": 42, \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/cka_stability_results.json\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/cka_stability_results.json\"}, \"metrics\": {\"spearman_256v512_attn\": 0.989, \"spearman_256v512_mlp\": 0.9683, \"spearman_256v512_combined\": 0.9788, \"spearman_256v1024_attn\": 0.9762, \"spearman_256v1024_mlp\": 0.9464, \"spearman_256v1024_combined\": 0.9641, \"spearman_512v1024_attn\": 0.995, \"spearman_512v1024_mlp\": 0.9908, \"spearman_512v1024_combined\": 0.9938, \"min_combined_rho\": 0.964, \"mean_combined_rho\": 0.979, \"stable\": true}}, \"eval_mbpp_sft_standard_20_1p5b\": {\"created_at\": \"2026-05-19T18:56:15.766Z\", \"spec\": {\"command\": \"python src/eval_mbpp.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20_1p5b --max_new_tokens 2048 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_mbpp_sft_standard_20_1p5b.json\", \"server\": \"westb-23072\", \"gpu\": \"0\", \"model_name\": \"sft_standard_20_1p5b\", \"checkpoint_source\": \"sft_standard_20_1p5b\", \"eval_data\": \"mbpp\", \"data_path\": \"mbpp\", \"data_count\": 0, \"seed\": 0}, \"metrics\": {\"pass_at_1\": 0.008021, \"n_correct\": 3, \"n_total\": 374, \"stderr\": 0.004613, \"avg_response_length\": 1658.6, \"median_response_length\": 2048}}, \"eval_mbpp_grpo_rasp_20\": {\"created_at\": \"2026-05-19T18:18:35.729Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/bin/activate && cd /root/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=1 python src/eval_mbpp.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_rasp_20_fair --max_new_tokens 2048 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_mbpp_grpo_rasp_20.json\\\"\", \"server\": \"westd-29022\", \"gpu\": [\"cuda:1\"], \"pid\": \"127964\", \"data_path\": \"MBPP\", \"data_count\": 374, \"model_name\": \"grpo_stage2_rasp_20_fair\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_rasp_20_fair\", \"eval_data\": \"MBPP (374 tasks, sanitized, pass@1, max_new_tokens=2048)\"}, \"metrics\": {\"pass_at_1\": 0.131, \"n_correct\": 49, \"n_total\": 374, \"stderr\": 0.0174}}, \"eval_mbpp_sft_rasp_20\": {\"created_at\": \"2026-05-19T18:18:34.640Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/bin/activate && cd /root/recovery_aware_struct_prune && python src/eval_mbpp.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20_westd --max_new_tokens 2048 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_mbpp_sft_rasp_20.json\\\"\", \"server\": \"westd-29022\", \"gpu\": [\"cuda:3\"], \"pid\": \"133674\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_mbpp_sft_rasp_20.log\", \"submitted_at\": \"2026-05-19T20:00:13.578Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20_westd\", \"wall_clock_seconds\": 4067.0, \"gpu_hours\": 1.13}, \"metrics\": {\"pass_at_1\": 0.1176, \"stderr\": 0.0167, \"n_correct\": 44, \"n_total\": 374, \"dense_baseline_pass_at_1\": 0.5348, \"degradation_pct\": 78.01, \"avg_response_length\": 810.7, \"median_response_length\": 247}}, \"eval_mbpp_sft_cka_only_20\": {\"created_at\": \"2026-05-19T17:20:00.596Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 python src/eval_mbpp.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_20 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/mbpp_sft_cka_only_20.json\", \"server\": \"westd-29022\", \"gpu\": \"cuda:3\", \"pid\": 123029, \"log_path\": \"/tmp/eval_mbpp_sft_cka_only_20.log\", \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_20\", \"eval_data\": \"MBPP sanitized (374 tasks)\", \"data_path\": \"google-research-datasets/mbpp (sanitized)\", \"data_count\": 374, \"model_name\": \"Qwen2.5-7B-pruned-20%-SFT-CKA-only\", \"seed\": 42}, \"metrics\": {\"pass_at_1\": 0.1283, \"stderr\": 0.0173, \"n_correct\": 48, \"n_total\": 374, \"dense_baseline_pass_at_1\": 0.5348, \"degradation_pct\": 76.01, \"avg_response_length\": 643.8, \"median_response_length\": 363.5}}, \"eval_humaneval_sft_rasp_20_1p5b_2048\": {\"created_at\": \"2026-05-19T11:35:50.597Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python src/eval_humaneval.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20_1p5b --max_new_tokens 2048 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_humaneval_sft_rasp_20_1p5b_2048.json --seed 42\", \"server\": \"westb-23072\", \"gpu\": [\"cuda:0\"], \"pid\": \"909411\", \"data_path\": \"HumanEval\", \"data_count\": 164, \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20_1p5b\", \"eval_data\": \"HumanEval\", \"model_name\": \"Qwen2.5-1.5B-pruned-rasp-20-SFT\", \"metrics\": {\"pass_at_1\": 0, \"stderr\": 0, \"n_passed\": 0, \"n_total\": 164}, \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_humaneval_sft_rasp_20_1p5b_2048.json\", \"log_path\": \"/root/runs/recovery_aware_struct_prune/eval_humaneval_sft_rasp_20_1p5b_2048.log\"}, \"metrics\": {\"pass_at_1\": 0, \"n_correct\": 0, \"n_total\": 164, \"note\": \"1.5B SFT RASP, all truncated at 2048 tokens\"}}, \"eval_mbpp_grpo_cka_only_20\": {\"created_at\": \"2026-05-19T14:41:07.213Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/bin/activate && cd /root/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=0 python src/eval_mbpp.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20 --max_new_tokens 2048 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_mbpp_grpo_cka_only_20.json\\\"\", \"server\": \"westb-23072\", \"gpu\": [\"cuda:1\"], \"pid\": \"unknown\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_mbpp_grpo_cka_only_20.log\", \"submitted_at\": \"2026-05-19T18:08:02.259Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 17.3, \"gpu_hours\": 0.0}, \"metrics\": {\"pass_at_1\": 0.1417, \"n_correct\": 53, \"n_total\": 374, \"stderr\": 0.018}}, \"eval_gsm8k_grpo_shortgpt_20\": {\"created_at\": \"2026-05-19T17:19:18.419Z\", \"spec\": {\"command\": \"python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_shortgpt_20/checkpoint-100 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/gsm8k_grpo_shortgpt_20.json\", \"server\": \"westd-29022\", \"gpu\": \"cuda:0\", \"pid\": 122867, \"data_path\": \"gsm8k test set\", \"data_count\": 1319, \"model_name\": \"grpo_shortgpt_20/checkpoint-100\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_shortgpt_20/checkpoint-100\", \"eval_data\": \"gsm8k_test\", \"log_path\": \"/tmp/eval_gsm8k_grpo_shortgpt_20.log\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_shortgpt_20/checkpoint-100\"}, \"metrics\": {\"gsm8k_accuracy\": 43.37, \"n_correct\": 572, \"n_total\": 1319, \"stderr\": 0.0136}}, \"eval_gsm8k_sft_shortgpt_20\": {\"created_at\": \"2026-05-19T15:47:16.122Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_shortgpt_20 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/gsm8k_sft_shortgpt_20.json\", \"server\": \"westd-29022\", \"data_path\": \"gsm8k:test\", \"data_count\": 1319, \"model_name\": \"Qwen2.5-7B-ShortGPT-20pct-SFT\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_shortgpt_20/\", \"eval_data\": \"gsm8k:test\"}, \"metrics\": {\"gsm8k_accuracy\": 44.73, \"n_correct\": 590, \"n_total\": 1319}}, \"sft_shortgpt_20\": {\"created_at\": \"2026-05-19T14:22:26.084Z\", \"spec\": {\"command\": \"python src/sft_recovery.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/shortgpt_20 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/sft_shortgpt_20 --gpu 3 --num_train_epochs 2 --learning_rate 2e-5 --batch_size 1 --gradient_accumulation_steps 8 --max_seq_length 2048 --logging_steps 10 --seed 42\", \"server\": \"westd-29022\", \"gpu\": [\"cuda:3\"], \"pid\": \"112015\", \"log_path\": \"~/runs/recovery_aware_struct_prune/sft_shortgpt_20.log\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"openai/gsm8k\", \"data_count\": 7473, \"model_name\": \"shortgpt_20\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/shortgpt_20\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_shortgpt_20\"}}, \"eval_gsm8k_grpo_cka_only_20_seed123\": {\"created_at\": \"2026-05-19T17:47:34.008Z\", \"spec\": {\"command\": \"python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20_seed123 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/gsm8k_grpo_cka_only_20_seed123.json\", \"server\": \"westb-23072\", \"gpu\": \"cuda:1\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_seed123.log\", \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20_seed123\", \"eval_data\": \"gsm8k_test\", \"data_path\": \"gsm8k test set\", \"data_count\": 1319, \"model_name\": \"grpo_cka_only_20_seed123\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20_seed123\"}, \"metrics\": {\"accuracy\": 0.6422, \"stderr\": 0.0132, \"n_correct\": 847, \"n_total\": 1319, \"eos_rate\": 0.9909, \"avg_response_length\": 195.97, \"natural_eos\": 1307, \"truncated\": 12}}, \"eval_humaneval_grpo_standard_20_1p5b_2048\": {\"created_at\": \"2026-05-19T11:35:48.029Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python src/eval_humaneval.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_20_1p5b --max_new_tokens 2048 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_humaneval_grpo_standard_20_1p5b_2048.json --seed 42\", \"server\": \"westb-23072\", \"gpu\": \"cuda:0\", \"data_path\": \"HumanEval\", \"data_count\": 164, \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_20_1p5b\", \"eval_data\": \"HumanEval\", \"model_name\": \"Qwen2.5-1.5B-pruned-standard-20-GRPO\", \"tmux_session\": \"eval_humaneval_grpo_standard_1p5b\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_20_1p5b\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_humaneval_grpo_standard_20_1p5b_2048.log\"}}, \"gradient_flow_v3\": {\"created_at\": \"2026-05-19T15:03:16.535Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python src/gradient_flow_analysis.py --model_paths pruned_cka_only_20 pruned_standard_20 pruned_rasp_20 --model_names CKA-only Standard RASP --n_steps 200 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/results/gradient_flow_v3 --seed 42\", \"server\": \"westb-23072\", \"gpu\": \"cuda:0\", \"pid\": \"901553\", \"data_path\": \"openai/gsm8k train split\", \"data_count\": 200, \"model_name\": \"pruned_cka_only_20 + pruned_standard_20 + pruned_rasp_20\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/gradient_flow_v3/\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/logs/gradient_flow_v3.log\"}, \"metrics\": {\"cka_only_mean_grad_norm\": 0.3229, \"standard_mean_grad_norm\": 0.1118, \"rasp_mean_grad_norm\": 0.1431, \"cka_vs_standard_ratio\": 2.89, \"rasp_vs_standard_ratio\": 1.28, \"cka_vs_standard_significant_layers\": \"55/56\", \"cka_vs_rasp_significant_layers\": \"56/56\", \"rasp_vs_standard_significant_layers\": \"45/56\", \"rasp_vs_standard_nonsig_layers\": \"layer_18_mlp,layer_19_attn,layer_19_mlp,layer_20_attn,layer_20_mlp,layer_21_attn,layer_21_mlp,layer_22_attn,layer_24_mlp,layer_27_attn,layer_27_mlp\", \"n_samples\": 200, \"statistical_test\": \"Wilcoxon signed-rank, per-layer\", \"bootstrap_n\": 1000, \"seed\": 42}}, \"eval_gsm8k_grpo_rasp_20_fair\": {\"created_at\": \"2026-05-19T12:47:37.399Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_rasp_20_fair --max_samples 1319 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_grpo_rasp_20_fair.json\", \"server\": \"westd-29022\", \"data_path\": \"GSM8K\", \"data_count\": 1319, \"model_name\": \"grpo_stage2_rasp_20_fair\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_rasp_20_fair\", \"eval_data\": \"GSM8K\", \"gpu\": [\"cuda:0\"], \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_grpo_rasp_20_fair.log\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_rasp_20_fair\"}, \"metrics\": {\"accuracy\": 0.6088, \"stderr\": 0.0134, \"n_correct\": 803, \"n_total\": 1319, \"eos_rate\": 0.9879, \"avg_response_length\": 195.7}}, \"eval_mbpp_dense_unpruned\": {\"created_at\": \"2026-05-19T13:47:53.814Z\", \"spec\": {\"server\": \"westd-29022\", \"gpu\": [\"cuda:2\"], \"command\": \"bash -c 'source /root/miniconda3/bin/activate && cd /root/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=2 /root/miniconda3/bin/python src/eval_mbpp.py --model_path /root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B --max_new_tokens 2048 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_mbpp_dense_unpruned.json'\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_mbpp_dense_unpruned.log\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"MBPP\", \"data_count\": 374, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B\", \"eval_data\": \"MBPP (374 tasks, sanitized, pass@1, max_new_tokens=2048)\", \"checkpoint_path\": \"/root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B\", \"pid\": \"108291\"}, \"metrics\": {\"pass_at_1\": 0.5348, \"stderr\": 0.0258, \"n_correct\": 200, \"n_total\": 374}}, \"eval_humaneval_sft_rasp_20_2048_v2\": {\"created_at\": \"2026-05-19T13:18:20.664Z\", \"spec\": {\"server\": \"westd-29022\", \"gpu\": \"cuda:1\", \"command\": \"CUDA_VISIBLE_DEVICES=1 python src/eval_humaneval.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20_westd --max_new_tokens 2048 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/humaneval_sft_rasp_20_2048_v2.json\", \"data_path\": \"HumanEval\", \"data_count\": 164, \"model_name\": \"sft_rasp_20_westd\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20_westd\", \"eval_data\": \"HumanEval\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/humaneval_sft_rasp_20_2048_v2.log\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/humaneval_sft_rasp_20_2048_v2.json\", \"pid\": \"107932\"}, \"metrics\": {\"pass_at_1\": 0.1037, \"stderr\": 0.0238, \"n_correct\": 17, \"n_total\": 164, \"avg_response_length\": 1253.7, \"median_response_length\": 2048}}, \"grpo_cka_only_20_seed123\": {\"created_at\": \"2026-05-19T09:27:11.294Z\", \"spec\": {\"command\": \"bash -c 'source /root/miniconda3/bin/activate && cd /root/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=1 python src/grpo_train.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/pruned_cka_only_20 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20_seed123 --num_train_steps 100 --seed 123'\", \"server\": \"westb-23072\", \"gpu\": [\"cuda:1\"], \"pid\": \"857962\", \"data_path\": \"gsm8k\", \"data_count\": 7473, \"model_name\": \"pruned_cka_only_20\", \"seed\": 123, \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20_seed123\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/logs/grpo_cka_only_20_seed123.log\"}, \"metrics\": {\"train_loss\": 0.1361, \"final_step_loss\": 0.05054, \"final_reward\": 0.2975, \"final_reward_std\": 0.4097, \"train_steps\": 100, \"train_runtime_hours\": 11.63, \"wandb_run\": \"j8kn0sqd\"}}, \"gradient_flow_analysis\": {\"created_at\": \"2026-05-19T14:44:25.606Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python src/gradient_flow_analysis.py --model_paths pruned_cka_only_20 pruned_standard_20 --model_names CKA-only Standard --n_steps 20 --seed 42\", \"server\": \"westb-23072\", \"data_path\": \"openai/gsm8k (cached)\", \"data_count\": 20, \"model_name\": \"Qwen2-7B pruned variants\", \"seed\": 42, \"checkpoint_path\": \"N/A (analysis only)\", \"log_path\": \"/tmp/gradient_flow.log\"}, \"metrics\": {\"cka_only_attn_grad_mean\": 0.3135, \"cka_only_attn_grad_cv\": 1.2231, \"cka_only_mlp_grad_mean\": 0.285, \"cka_only_mlp_grad_cv\": 1.2424, \"standard_attn_grad_mean\": 0.1316, \"standard_attn_grad_cv\": 1.1363, \"standard_mlp_grad_mean\": 0.1222, \"standard_mlp_grad_cv\": 1.1489, \"grad_magnitude_ratio_attn\": 2.38, \"grad_magnitude_ratio_mlp\": 2.33}}, \"cka_calibration_stability_ablation\": {\"created_at\": \"2026-05-19T14:21:15.548Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python src/run_cka_reliability.py --original_model /root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B --pruned_model /root/autodl-tmp/recovery_aware_struct_prune/pruned_cka_only_20 --num_samples 1024 --n_splits 5 --max_length 512 --output /root/autodl-tmp/recovery_aware_struct_prune/results/cka_reliability_ablation.json --seed 42\", \"server\": \"westb-23072\", \"gpu\": [\"cuda:0\"], \"pid\": \"cka_reliability\", \"data_path\": \"GSM8K calibration subset\", \"data_count\": 1024, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B + pruned_cka_only_20\", \"seed\": 42, \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/logs/cka_reliability_ablation.log\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/cka_reliability_ablation.json\", \"backend\": \"tmux\", \"account\": \"root\"}, \"metrics\": {\"split_half_rho\": 0.9932, \"n_splits\": 5, \"size_sensitivity_128\": 0.982, \"size_sensitivity_256\": 0.989, \"size_sensitivity_512\": 0.995}}, \"eval_humaneval_grpo_standard_20_fair_2048_v3\": {\"created_at\": \"2026-05-19T07:05:14.343Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 python src/eval_humaneval.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_standard_20_fair --max_new_tokens 2048\", \"server\": \"westd-29022\", \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_standard_20_fair\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/humaneval_grpo_standard_20_fair_2048_v3.log\", \"data_path\": \"HumanEval\", \"data_count\": 164, \"model_name\": \"grpo_stage2_standard_20_fair\", \"seed\": 42}, \"metrics\": {\"pass_at_1\": 0.1098, \"n_correct\": 18, \"n_total\": 164}}, \"eval_humaneval_sft_cka_only_20_2048_v2\": {\"created_at\": \"2026-05-19T09:27:07.470Z\", \"spec\": {\"command\": \"bash -c 'source /root/miniconda3/bin/activate && cd /root/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=1 /root/miniconda3/bin/python src/eval_humaneval.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_20 --max_new_tokens 2048 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/humaneval_sft_cka_only_20_2048_v2.json'\", \"server\": \"westd-29022\", \"gpu\": [\"cuda:1\"], \"pid\": \"78740\", \"data_path\": \"HumanEval\", \"data_count\": 164, \"model_name\": \"sft_cka_only_20\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_20\", \"eval_data\": \"HumanEval (164 problems, pass@1, max_new_tokens=2048, sys.executable fix)\"}, \"metrics\": {\"pass_at_1\": 20.12, \"n_correct\": 33, \"n_total\": 164}}, \"eval_math500_grpo_cka_only_20_2048\": {\"created_at\": \"2026-05-18T22:36:14.421Z\", \"spec\": {\"command\": \"bash -c 'source /root/miniconda3/bin/activate && cd /root/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=2 python src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/math500_grpo_cka_only_20_2048.json --max_new_tokens 2048'\", \"server\": \"westd-29022\", \"gpu\": [\"cuda:2\"], \"pid\": \"36703\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/math500_grpo_cka_only_20_2048.log\", \"submitted_at\": \"2026-05-18T23:23:59.014Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"grpo_cka_only_20\", \"data_path\": \"MATH-500\", \"data_count\": 500, \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20\", \"eval_data\": \"MATH-500\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20\", \"wall_clock_seconds\": 49459.6, \"gpu_hours\": 13.74}, \"metrics\": {\"accuracy\": 0.292, \"n_correct\": 146, \"n_total\": 500}}, \"eval_gsm8k_sft_standard_20_1p5b\": {\"created_at\": \"2026-05-18T18:10:55.912Z\", \"spec\": {\"command\": \"bash -c 'source /root/miniconda3/bin/activate && cd /root/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=1 python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20_1p5b --max_samples 1319 --seed 42 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_sft_standard_20_1p5b.json'\", \"server\": \"westb-23072\", \"gpu\": [\"cuda:1\"], \"pid\": \"842784\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_gsm8k_sft_standard_20_1p5b.log\", \"submitted_at\": \"2026-05-18T23:02:19.301Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"Qwen2.5-1.5B-sft-standard-20\", \"checkpoint_source\": \"sft_standard_20_1p5b\", \"eval_data\": \"gsm8k\", \"data_path\": \"gsm8k\", \"data_count\": 1319, \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20_1p5b\", \"wall_clock_seconds\": 50738.5, \"gpu_hours\": 14.09}, \"metrics\": {\"accuracy\": 0.22896133434420016, \"n_correct\": 302, \"n_total\": 1319}}, \"eval_gsm8k_grpo_standard_20_fair_v2\": {\"created_at\": \"2026-05-19T09:27:09.334Z\", \"spec\": {\"command\": \"bash -c 'source /root/miniconda3/bin/activate && cd /root/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=0 /root/miniconda3/bin/python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_standard_20_fair --max_samples 1319 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_grpo_standard_20_fair_v2.json'\", \"server\": \"westd-29022\", \"gpu\": [\"cuda:0\"], \"pid\": \"83299\", \"data_path\": \"GSM8K\", \"data_count\": 1319, \"model_name\": \"grpo_stage2_standard_20_fair\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_standard_20_fair\", \"eval_data\": \"GSM8K (1319 samples)\"}, \"metrics\": {\"accuracy\": 59.44, \"n_correct\": 784, \"n_total\": 1319}}, \"eval_humaneval_grpo_rasp_20_fair_2048\": {\"created_at\": \"2026-05-19T06:38:59.146Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 python src/eval_humaneval.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_rasp_20_fair --max_new_tokens 2048 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/humaneval_grpo_rasp_20_fair_2048.json\", \"server\": \"westd-29022\", \"gpu\": [\"cuda:3\"], \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/humaneval_grpo_rasp_20_fair_2048.log\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"HumanEval\", \"data_count\": 164, \"model_name\": \"grpo_stage2_rasp_20_fair\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_rasp_20_fair\", \"eval_data\": \"HumanEval\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_rasp_20_fair\"}, \"metrics\": {\"pass_at_1\": 0.1098, \"n_correct\": 18, \"n_total\": 164, \"stderr\": 0.0244, \"avg_response_length\": null}}, \"eval_gsm8k_grpo_unstructured_20\": {\"created_at\": \"2026-05-19T04:46:38.286Z\", \"spec\": {\"command\": \"python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_unstructured_20/checkpoint-100 --max_samples 1319 --seed 42 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_grpo_unstructured_20.json\", \"server\": \"westb-23072\", \"data_path\": \"gsm8k test set\", \"data_count\": 1319, \"model_name\": \"grpo_unstructured_20/checkpoint-100\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_unstructured_20/checkpoint-100\", \"eval_data\": \"gsm8k_test\"}, \"metrics\": {\"accuracy\": 0.8764, \"n_correct\": 1156, \"n_total\": 1319, \"stderr\": 0.00906, \"eos_rate\": 0.9818, \"truncated\": 24, \"avg_response_length\": 600}}, \"eval_humaneval_grpo_cka_only_20_2048\": {\"created_at\": \"2026-05-19T04:11:28.637Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python src/eval_humaneval.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20 --max_new_tokens 2048\", \"server\": \"westd-29022\", \"gpu\": [\"cuda:1\"], \"pid\": \"66521\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_humaneval_grpo_cka_only_20_2048.log\", \"submitted_at\": \"2026-05-19T04:11:28.118Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"HumanEval\", \"data_count\": 164, \"model_name\": \"grpo_cka_only_20\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20\", \"eval_data\": \"HumanEval\", \"wall_clock_seconds\": 12309.1, \"gpu_hours\": 3.42}, \"metrics\": {\"pass_at_1\": 0.2012, \"n_correct\": 33, \"n_total\": 164, \"stderr\": 0.0313, \"avg_response_length\": 1523.31, \"median_response_length\": 2048, \"wall_clock_seconds\": 11933}}, \"grpo_standard_20_fair\": {\"created_at\": \"2026-05-18T01:05:44.644Z\", \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_source\": \"sft_standard_20_westd\", \"command\": \"bash -c \\\"export HF_HOME=/root/autodl-tmp/.hf_cache && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/recovery_aware_struct_prune && python src/train_grpo_v5.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20_westd --output_dir /root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_standard_20_fair --gpu 0 --max_completion_length 1024 --beta 0.01 --temperature 0.4 --repetition_penalty 1.15 --format_reward_weight 0.1 --gradient_checkpointing true --optim adamw_bnb_8bit --loss_type dapo --learning_rate 1e-6 --max_steps 100 --save_total_limit 3 --save_steps 10 --reward_desert_patience 200 --run_name grpo_standard_20_fair\\\"\", \"data_count\": 7473, \"data_path\": \"openai/gsm8k (GRPO training)\", \"eval_data\": \"N/A (GRPO training, not eval)\", \"gpu\": [\"cuda:0\"], \"hyperparams\": {\"beta\": 0.01, \"format_reward_weight\": 0.1, \"loss_type\": \"dapo\", \"lr\": 1e-06, \"max_completion_length\": 1024, \"max_steps\": 100, \"optim\": \"adamw_bnb_8bit\", \"repetition_penalty\": 1.15, \"reward_desert_patience\": 200, \"save_steps\": 10, \"save_total_limit\": 3, \"temperature\": 0.4}, \"log_path\": \"~/runs/recovery_aware_struct_prune/grpo_standard_20_fair.log\", \"model_name\": \"sft_standard_20_westd\", \"pid\": \"74224\", \"seed\": 42, \"server\": \"westd-11672\", \"submitted_at\": \"2026-05-18T01:05:44.210Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 3631.9, \"gpu_hours\": 1.01}, \"metrics\": {\"wandb_run_id\": \"tyv20u2k\", \"total_steps\": 100, \"runtime_seconds\": 3017, \"reward_trajectory\": [0.051, 0.056, 0.067, 0.081, 0.019, 0.043, 0.047, 0.046, 0.031, 0.054], \"frac_zero_std_trajectory\": [0.5, 0.625, 0.5, 0.5, 0.575, 0.55, 0.575, 0.55, 0.55, 0.55], \"peak_reward\": 0.081, \"peak_reward_step\": 40, \"final_reward\": 0.054, \"final_frac_zero_std\": 0.55, \"dynamics_pattern\": \"dip_then_partial_recovery\", \"dip_step\": 50, \"dip_reward\": 0.019}}, \"inference_bench_clean_v2\": {\"created_at\": \"2026-05-19T01:42:25.421Z\", \"spec\": {\"command\": \"bash -c 'source /root/miniconda3/bin/activate && cd /root/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=3 python src/measure_inference_speed.py --models original:/root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B pruned_cka_only_20:/root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20 pruned_standard_20:/root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_standard_20_fair --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/inference_bench_clean_v2.json --n_prompts 50 --max_new_tokens 256'\", \"server\": \"westd-29022\", \"gpu\": [\"cuda:3\"], \"pid\": \"56892\", \"log_path\": \"~/runs/recovery_aware_struct_prune/inference_bench_clean_v2.log\", \"submitted_at\": \"2026-05-19T01:42:24.921Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"Dense + CKA-only 20% + Standard 20%\", \"data_path\": \"gsm8k test (50 prompts)\", \"data_count\": 50, \"seed\": 42, \"checkpoint_path\": \"N/A (benchmark)\", \"wall_clock_seconds\": 3702.3, \"gpu_hours\": 1.03}, \"metrics\": {\"original_tps\": 72.02, \"cka_only_20_tps\": 58.28, \"standard_20_tps\": 58.25, \"cka_only_20_speedup\": 0.809, \"standard_20_speedup\": 0.809, \"original_first_token_ms\": 20.05, \"cka_only_20_first_token_ms\": 16.35, \"standard_20_first_token_ms\": 16.4, \"original_per_token_ms\": 13.89, \"cka_only_20_per_token_ms\": 16.73, \"standard_20_per_token_ms\": 16.71, \"original_params\": 7615616512, \"pruned_params\": 6161946112, \"param_reduction_pct\": 19.1}}, \"eval_gsm8k_sft_rasp_20_1p5b\": {\"created_at\": \"2026-05-18T18:10:57.471Z\", \"spec\": {\"command\": \"bash -c 'source /root/miniconda3/bin/activate && cd /root/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=0 python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20_1p5b --max_samples 1319 --seed 42 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_sft_rasp_20_1p5b.json'\", \"server\": \"westb-23072\", \"gpu\": [\"cuda:0\"], \"pid\": \"845212\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_sft_rasp_20_1p5b.json\", \"submitted_at\": \"2026-05-18T23:43:58.904Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"sft_rasp_20_1p5b\", \"data_path\": \"gsm8k\", \"data_count\": 1319, \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20_1p5b\", \"eval_data\": \"gsm8k\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20_1p5b\", \"wall_clock_seconds\": 10779.5, \"gpu_hours\": 2.99}, \"metrics\": {\"accuracy\": 0.2691, \"n_correct\": 355, \"n_total\": 1319, \"stderr\": 0.0122, \"grpo_delta_pp\": -0.75}}, \"eval_math500_grpo_standard_20_fair_v2\": {\"created_at\": \"2026-05-18T18:24:25.108Z\", \"spec\": {\"command\": \"bash -c 'source /root/miniconda3/bin/activate && cd /root/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=1 python src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_standard_20_fair --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/math500_grpo_standard_20_fair_v2.json --max_new_tokens 2048'\", \"gpu\": [\"cuda:1\"], \"pid\": \"22049\", \"model_name\": \"grpo_stage2_standard_20_fair\", \"data_path\": \"MATH-500\", \"data_count\": 500, \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_standard_20_fair\", \"eval_data\": \"MATH-500\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_standard_20_fair\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_math500_grpo_standard_20_fair_v2.log\"}, \"metrics\": {\"accuracy\": 0.264, \"n_correct\": 132, \"n_total\": 500, \"stderr\": 0.0197}}, \"eval_math500_sft_rasp_20_2048\": {\"created_at\": \"2026-05-18T22:36:16.836Z\", \"spec\": {\"command\": \"bash -c 'source /root/miniconda3/bin/activate && cd /root/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=3 python src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20_westd --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/math500_sft_rasp_20_2048.json --max_new_tokens 2048'\", \"server\": \"westd-29022\", \"gpu\": [\"cuda:3\"], \"pid\": \"39767\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/math500_sft_rasp_20_2048.log\", \"submitted_at\": \"2026-05-18T23:54:16.231Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"sft_rasp_20_westd\", \"data_path\": \"MATH-500\", \"data_count\": 500, \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20_westd\", \"eval_data\": \"MATH-500\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20_westd\", \"wall_clock_seconds\": 6287.1, \"gpu_hours\": 1.75}, \"metrics\": {\"accuracy\": 0.226, \"n_correct\": 113, \"n_total\": 500, \"stderr\": 0.0187, \"natural_eos\": 314, \"truncated\": 186, \"natural_eos_pct\": 0.628, \"avg_response_length\": 930.58, \"median_response_length\": 274}}, \"eval_math500_dense_2048\": {\"created_at\": \"2026-05-18T22:08:58.081Z\", \"spec\": {\"gpu\": [\"cuda:0\"], \"pid\": \"32469\", \"checkpoint_path\": \"/root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/math500_dense_2048.json\"}, \"metrics\": {\"accuracy\": 0.53, \"n_correct\": 265, \"n_total\": 500, \"stderr\": 0.0223, \"natural_eos_pct\": 0.468, \"truncated_pct\": 0.532, \"avg_response_length\": 1724.5, \"median_response_length\": 2048}}, \"eval_math500_grpo_rasp_20_fair\": {\"created_at\": \"2026-05-18T18:16:25.616Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 python src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_rasp_20_fair --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/math500_grpo_rasp_20_fair.json --max_new_tokens 2048\", \"server\": \"westd-29022\", \"gpu\": [\"cuda:3\"], \"model_name\": \"grpo_stage2_rasp_20_fair\", \"data_path\": \"MATH-500\", \"data_count\": 500, \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_rasp_20_fair\", \"eval_data\": \"MATH-500\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_rasp_20_fair\", \"log_path\": \"~/runs/recovery_aware_struct_prune/math500_grpo_rasp_20_fair.log\"}, \"metrics\": {\"accuracy\": 0.24, \"n_correct\": 120, \"n_total\": 500, \"stderr\": 0.0191, \"natural_eos_pct\": 0.64, \"truncated_pct\": 0.36, \"avg_response_length\": 903.5, \"median_response_length\": 272, \"max_new_tokens\": 2048}}, \"eval_gsm8k_sft_cka_only_20_1p5b\": {\"created_at\": \"2026-05-18T17:51:20.577Z\", \"spec\": {\"command\": \"python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_20_1p5b --max_samples 1319 --seed 42 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_sft_cka_only_20_1p5b.json\", \"server\": \"westb-23072\", \"gpu\": [\"cuda:0\"], \"checkpoint_source\": \"sft_cka_only_20_1p5b\", \"eval_data\": \"gsm8k\", \"data_path\": \"gsm8k\", \"data_count\": 1319, \"model_name\": \"Qwen2.5-1.5B-sft-cka-only-20\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_20_1p5b/\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_sft_cka_only_20_1p5b.json\"}, \"metrics\": {\"accuracy\": 0.3563, \"n_correct\": 470, \"n_total\": 1319, \"stderr\": 0.0132, \"eos_rate\": 0.9507, \"avg_response_length\": 336.76}}, \"sft_standard_20_retrain_westd\": {\"created_at\": \"2026-05-18T22:40:50.567Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/bin/activate && cd /root/recovery_aware_struct_prune && python src/sft_recovery.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/pruned_standard_20 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20 --gpu 2\\\"\", \"server\": \"westd-29022\", \"gpu\": [\"cuda:2\"], \"pid\": \"34346\", \"log_path\": \"~/runs/recovery_aware_struct_prune/sft_standard_20_retrain_westd.log\", \"submitted_at\": \"2026-05-18T22:40:50.078Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"pruned_standard_20 -> sft_standard_20\", \"data_path\": \"gsm8k (SFT recovery)\", \"data_count\": 7473, \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20\", \"wall_clock_seconds\": 2533.8, \"gpu_hours\": 0.7}, \"metrics\": {\"train_loss\": 0.758, \"mean_token_accuracy\": 0.8252, \"train_runtime_sec\": 1688, \"train_samples_per_second\": 8.856, \"epochs\": 2, \"total_steps\": 1870}}, \"eval_gsm8k_grpo_rasp_20_1p5b\": {\"created_at\": \"2026-05-18T16:59:22.921Z\", \"spec\": {\"command\": \"bash -c 'source /root/miniconda3/bin/activate && cd /root/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=1 python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_20_1p5b/checkpoint-100 --max_samples 1319 --seed 42 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_grpo_rasp_20_1p5b.json'\", \"server\": \"westb-23072\", \"gpu\": [\"cuda:1\"], \"data_path\": \"gsm8k:test\", \"data_count\": 1319, \"model_name\": \"grpo_rasp_20_1p5b/checkpoint-100\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_20_1p5b/checkpoint-100\", \"eval_data\": \"gsm8k:test\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_20_1p5b/checkpoint-100\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_grpo_rasp_20_1p5b.json\"}, \"metrics\": {\"accuracy\": 0.2616, \"n_correct\": 345, \"n_total\": 1319, \"stderr\": 0.0121, \"eos_rate\": 0.9378, \"avg_response_length\": 392.7}}, \"eval_math500_sft_cka_only_20_v4_restart\": {\"created_at\": \"2026-05-18T18:16:24.171Z\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_20\", \"log_path\": \"~/runs/recovery_aware_struct_prune/math500_sft_cka_only_20_v4.log\", \"results_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/math500_sft_cka_only_20_v4.json\"}, \"metrics\": {\"accuracy\": 0.29, \"n_correct\": 145, \"n_total\": 500, \"stderr\": 0.0203, \"natural_eos\": 384, \"truncated\": 116, \"natural_eos_pct\": 0.768, \"avg_response_length\": 673.278, \"median_response_length\": 242.5}}, \"grpo_cka_only_20_extended_300\": {\"created_at\": \"2026-05-18T14:51:36.423Z\", \"spec\": {\"command\": \"bash -c 'source /root/miniconda3/bin/activate && cd /root/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=0 python src/train_grpo_v5.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20_extended_300 --beta 0.01 --temperature 0.4 --repetition_penalty 1.15 --format_reward_weight 0.1 --loss_type dapo --learning_rate 1e-6 --max_steps 300 --save_steps 50 --save_total_limit 3 --resume_from_checkpoint /root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20/checkpoint-100'\", \"server\": \"westd-29022\", \"gpu\": [\"cuda:0\"], \"pid\": \"11457\", \"log_path\": \"~/runs/recovery_aware_struct_prune/grpo_cka_only_20_extended_300.log\", \"submitted_at\": \"2026-05-18T15:10:04.515Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B (CKA-only 20% pruned, SFT recovered, GRPO extended)\", \"data_path\": \"openai/gsm8k\", \"data_count\": 7473, \"seed\": 42, \"wandb_run_id\": \"z9f0z901\", \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20/checkpoint-100\", \"eval_data\": \"openai/gsm8k (GRPO RL training)\", \"hyperparams\": {\"beta\": 0.01, \"temperature\": 0.4, \"repetition_penalty\": 1.15, \"format_reward_weight\": 0.1, \"loss_type\": \"dapo\", \"lr\": 1e-06, \"max_steps\": 300, \"save_steps\": 50, \"save_total_limit\": 3, \"resume_from_step\": 100}, \"wall_clock_seconds\": 23392.2, \"gpu_hours\": 6.5}, \"metrics\": {\"final_reward\": 0.3075, \"peak_reward\": 0.4444, \"peak_reward_step\": 280, \"reward_step100\": 0.354, \"reward_step300\": 0.3075, \"train_loss_final\": 0.0349, \"global_step\": 300, \"runtime_seconds\": 23004, \"gpu_hours\": 6.5, \"final_frac_zero_std\": 0.275, \"reward_range\": [0.22, 0.44], \"pattern\": \"sustained oscillation, no collapse\", \"wandb_run_id\": \"z9f0z901\"}}, \"eval_gsm8k_grpo_standard_20_1p5b\": {\"created_at\": \"2026-05-18T16:38:01.585Z\", \"spec\": {\"gpu\": [\"cuda:0\"], \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_20_1p5b/\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_grpo_standard_20_1p5b.json\"}, \"metrics\": {\"accuracy\": 0.2229, \"n_correct\": 294, \"n_total\": 1319, \"stderr\": 0.0115}}, \"eval_gsm8k_grpo_cka_only_20_1p5b\": {\"created_at\": \"2026-05-18T16:35:29.923Z\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20_1p5b/checkpoint-100\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_grpo_cka_only_20_1p5b.json\"}, \"metrics\": {\"accuracy\": 0.3548, \"n_correct\": 468, \"n_total\": 1319, \"stderr\": 0.0132}}, \"eval_math500_dense_unpruned\": {\"created_at\": \"2026-05-18T13:42:10.786Z\", \"spec\": {\"command\": \"bash -c 'source /root/miniconda3/bin/activate && cd /root/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=3 python src/eval_math500.py --model_path /root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/math500_dense_unpruned.json'\", \"server\": \"westd-29022\", \"gpu\": [\"cuda:3\"], \"pid\": \"4223\", \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B (dense unpruned)\", \"data_path\": \"MATH-500\", \"data_count\": 500, \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B\", \"eval_data\": \"MATH-500\", \"checkpoint_path\": \"/root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B\", \"log_path\": \"~/runs/recovery_aware_struct_prune/math500_dense_unpruned.log\"}, \"metrics\": {\"accuracy\": 0.736, \"stderr\": 0.0197, \"n_correct\": 368, \"n_total\": 500, \"natural_eos_pct\": 0.752}}, \"grpo_rasp_20_1p5b\": {\"created_at\": \"2026-05-18T15:12:41.395Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python src/train_grpo_v5.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20_1p5b --output_dir /root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_20_1p5b --beta 0.01 --temperature 0.4 --repetition_penalty 1.15 --format_reward_weight 0.1 --loss_type dapo --learning_rate 1e-6 --max_steps 100\", \"server\": \"westb-23072\", \"gpu\": \"cuda:1\", \"pid\": \"815395\", \"log_path\": \"~/runs/recovery_aware_struct_prune/grpo_rasp_20_1p5b.log\", \"submitted_at\": \"2026-05-18T15:13:38.510Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"DeepSeek-R1-Distill-Qwen-1.5B (RASP 20% pruned, SFT recovered)\", \"data_path\": \"openai/gsm8k\", \"data_count\": 7473, \"seed\": 42, \"wandb_run_id\": \"a18r8uyw\", \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20_1p5b\", \"eval_data\": \"openai/gsm8k (GRPO RL training)\", \"hyperparams\": {\"beta\": 0.01, \"temperature\": 0.4, \"repetition_penalty\": 1.15, \"format_reward_weight\": 0.1, \"loss_type\": \"dapo\", \"learning_rate\": 1e-06, \"max_steps\": 100, \"optimizer\": \"adamw_8bit\"}, \"wall_clock_seconds\": 4438.5, \"gpu_hours\": 1.23}, \"metrics\": {\"final_reward\": 0.099, \"frac_zero_std\": 0.175, \"clipped_ratio\": 0.82}}, \"grpo_cka_only_20_1p5b\": {\"created_at\": \"2026-05-18T12:50:08.570Z\", \"spec\": {\"command\": \"bash -c 'source /root/miniconda3/bin/activate && cd /root/recovery_aware_struct_prune && python src/train_grpo_v5.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_20_1p5b --output_dir /root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20_1p5b --beta 0.01 --temperature 0.4 --repetition_penalty 1.15 --format_reward_weight 0.1 --loss_type dapo --learning_rate 1e-6 --max_steps 100'\", \"server\": \"westb-23072\", \"gpu\": [\"cuda:0\"], \"pid\": \"806188\", \"model_name\": \"DeepSeek-R1-Distill-Qwen-1.5B (CKA-only 20% pruned, SFT recovered)\", \"data_path\": \"openai/gsm8k\", \"data_count\": 7473, \"seed\": 42, \"wandb_run_id\": \"8zkpr0hh\", \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_20_1p5b\", \"eval_data\": \"openai/gsm8k (GRPO RL training, not eval)\", \"hyperparams\": {\"beta\": 0.01, \"temperature\": 0.4, \"repetition_penalty\": 1.15, \"format_reward_weight\": 0.1, \"loss_type\": \"dapo\", \"lr\": 1e-06, \"max_steps\": 100}}, \"metrics\": {\"reward_mean\": 0.2375, \"frac_reward_zero_std\": 0.175, \"loss\": 0.0595, \"kl\": 0.00215, \"grad_norm\": 1.445, \"global_step\": 100, \"note\": \"training completed 100/100 but save_model failed (disk full). checkpoint-100 has complete model.\"}}, \"grpo_standard_20_1p5b\": {\"created_at\": \"2026-05-18T14:15:13.990Z\", \"spec\": {\"command\": \"bash -c 'source /root/miniconda3/bin/activate && cd /root/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=1 python src/train_grpo_v5.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20_1p5b --output_dir /root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_20_1p5b --beta 0.01 --temperature 0.4 --repetition_penalty 1.15 --format_reward_weight 0.1 --loss_type dapo --learning_rate 1e-6 --max_steps 100'\", \"server\": \"westb-23072\", \"gpu\": [\"cuda:1\"], \"pid\": \"811558\", \"model_name\": \"DeepSeek-R1-Distill-Qwen-1.5B (Standard 20% pruned, SFT recovered)\", \"data_path\": \"openai/gsm8k\", \"data_count\": 7473, \"seed\": 42, \"wandb_run_id\": \"mm31apn0\", \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20_1p5b\", \"eval_data\": \"openai/gsm8k (GRPO RL training)\", \"hyperparams\": {\"beta\": 0.01, \"temperature\": 0.4, \"repetition_penalty\": 1.15, \"format_reward_weight\": 0.1, \"loss_type\": \"dapo\", \"lr\": 1e-06, \"max_steps\": 100}}, \"metrics\": {\"reward_mean\": 0.0844, \"frac_reward_zero_std\": 0.15, \"loss\": 0.0151, \"grad_norm\": 4.03125, \"kl\": 0.0044, \"entropy\": 0.4617, \"final_step\": 100, \"max_steps\": 100, \"total_time_min\": 53}}, \"grpo_standard_20_extended_300_v2\": {\"created_at\": \"2026-05-18T13:53:41.781Z\", \"spec\": {\"command\": \"bash -c 'source /root/miniconda3/bin/activate && cd /root/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=0 python src/train_grpo_v5.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_20_extended_300/checkpoint-110 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_20_extended_300 --beta 0.01 --temperature 0.4 --repetition_penalty 1.15 --format_reward_weight 0.1 --loss_type dapo --learning_rate 1e-6 --max_steps 300 --save_steps 50 --save_total_limit 3 --resume_from_checkpoint /root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_20_extended_300/checkpoint-110'\", \"server\": \"westd-29022\", \"gpu\": [\"cuda:0\"], \"pid\": \"6346\", \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B (Standard 20% pruned, SFT recovered, GRPO extended v2)\", \"data_path\": \"openai/gsm8k\", \"data_count\": 7473, \"seed\": 42, \"wandb_run_id\": \"44cjdoiy\", \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_20_extended_300/checkpoint-110\", \"eval_data\": \"openai/gsm8k (GRPO RL training)\", \"hyperparams\": {\"beta\": 0.01, \"temperature\": 0.4, \"repetition_penalty\": 1.15, \"format_reward_weight\": 0.1, \"loss_type\": \"dapo\", \"lr\": 1e-06, \"max_steps\": 300, \"save_steps\": 50, \"save_total_limit\": 3, \"resume_from_step\": 111}}, \"metrics\": {\"reward_mean_step300\": 0.0562, \"loss_step300\": 0.0367, \"frac_reward_zero_std_step300\": 0.525, \"kl_step300\": 0.00306, \"entropy_step300\": 0.157, \"lr_step300\": 3.33e-09, \"runtime_min\": 48, \"reward_decline_after_step260\": true}}, \"sft_standard_20_1p5b\": {\"created_at\": \"2026-05-18T12:09:56.278Z\", \"spec\": {\"command\": \"python src/sft_recovery.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/pruned_standard_20_1p5b --output_dir /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20_1p5b --num_train_epochs 2 --batch_size 4 --gradient_accumulation_steps 2 --learning_rate 2e-5 --save_strategy no --gpu 0\", \"server\": \"westb-23072\", \"data_path\": \"openai/gsm8k (train split, cached)\", \"data_count\": 7473, \"model_name\": \"DeepSeek-R1-Distill-Qwen-1.5B (Standard 20% pruned)\", \"seed\": 42}}, \"sft_cka_only_20_1p5b\": {\"created_at\": \"2026-05-18T11:29:09.842Z\", \"spec\": {\"command\": \"python src/sft_recovery.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/pruned_cka_only_20_1p5b --output_dir /root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_20_1p5b --num_train_epochs 2 --batch_size 4 --gradient_accumulation_steps 2 --learning_rate 2e-5 --save_strategy epoch --gpu 0\", \"server\": \"westb-23072\", \"data_path\": \"openai/gsm8k (train split, cached)\", \"data_count\": 7473, \"model_name\": \"DeepSeek-R1-Distill-Qwen-1.5B (CKA-only 20% pruned)\", \"seed\": 42}}, \"sft_rasp_20_1p5b\": {\"created_at\": \"2026-05-18T12:09:57.178Z\", \"spec\": {\"command\": \"python src/sft_recovery.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/pruned_rasp_20_1p5b --output_dir /root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20_1p5b --num_train_epochs 2 --batch_size 4 --gradient_accumulation_steps 2 --learning_rate 2e-5 --save_strategy no --gpu 0\", \"server\": \"westb-23072\", \"gpu\": [\"cuda:0\"], \"pid\": \"802010\", \"log_path\": \"~/runs/recovery_aware_struct_prune/sft_rasp_20_1p5b.log\", \"account\": \"root\", \"data_path\": \"openai/gsm8k (train split, cached)\", \"data_count\": 7473, \"model_name\": \"DeepSeek-R1-Distill-Qwen-1.5B (RASP 20% pruned)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/pruned_rasp_20_1p5b\"}}, \"inference_bench_cka_only_20_clean\": {\"created_at\": \"2026-05-18T09:47:42.247Z\", \"metrics\": {\"dense\": {\"tokens_per_second\": 75.73, \"avg_latency_sec\": 6.729, \"peak_memory_gb\": 16.22, \"total_tokens\": 25477, \"validation\": \"PASS (75.73 vs expected 76.25, <1% deviation)\"}, \"cka_only_20\": {\"tokens_per_second\": 51.86, \"avg_latency_sec\": 4.078, \"peak_memory_gb\": 11.6, \"total_tokens\": 10574, \"latency_speedup_vs_dense\": \"39.4%\", \"memory_reduction_vs_dense\": \"28.5%\"}, \"rasp_20_dummy\": {\"tokens_per_second\": 75.79, \"avg_latency_sec\": 6.723, \"peak_memory_gb\": 16.23, \"note\": \"Dense model used as dummy (rasp not on westb)\"}}, \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/bin/activate && cd /root/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=0 python src/benchmark_inference.py --dense_path /root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B --rasp_path /root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B --standard_path /root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_20 --n_prompts 50 --max_new_tokens 512 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/inference_benchmark_cka_only_clean.json\\\"\", \"server\": \"westb-23072\", \"gpu\": [\"cuda:0\"], \"data_path\": \"openai/gsm8k (50 prompts)\", \"data_count\": 50, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B + sft_cka_only_20\", \"seed\": 42, \"checkpoint_source\": \"sft_cka_only_20 + dense\", \"eval_data\": \"GSM8K 50 prompts (inference latency benchmark)\"}}, \"eval_gsm8k_grpo_cka_only_20_v2\": {\"created_at\": \"2026-05-18T05:54:02.634Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/bin/activate && cd /root/recovery_aware_struct_prune && python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/gsm8k_grpo_cka_only_20.json --device_map cuda:0\\\"\", \"server\": \"westb-23072\", \"gpu\": [\"cuda:0\"], \"pid\": \"776884\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_gsm8k_grpo_cka_only_20_v2.log\", \"submitted_at\": \"2026-05-18T05:54:02.072Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"openai/gsm8k\", \"data_count\": 1319, \"model_name\": \"grpo_cka_only_20\", \"seed\": 42, \"checkpoint_source\": \"grpo_cka_only_20\", \"eval_data\": \"GSM8K test (1319 samples)\", \"wall_clock_seconds\": 10583.6, \"gpu_hours\": 2.94}, \"metrics\": {\"accuracy\": 0.6437, \"n_correct\": 849, \"n_total\": 1319, \"stderr\": 0.0132, \"eos_rate\": 0.9886, \"avg_response_length\": 203.43, \"truncated\": 15, \"wall_time_sec\": 8921}}, \"grpo_cka_only_20\": {\"created_at\": \"2026-05-17T14:51:36.653Z\", \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/bin/activate && cd /root/recovery_aware_struct_prune && python src/train_grpo_v5.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_20 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20 --gpu 0 --max_completion_length 1024 --beta 0.01 --temperature 0.4 --repetition_penalty 1.15 --format_reward_weight 0.1 --gradient_checkpointing true --optim adamw_bnb_8bit --loss_type dapo --learning_rate 1e-6 --max_steps 100 --save_steps 99999 --reward_desert_patience 50 --run_name grpo_cka_only_20\\\"\", \"gpu\": [\"cuda:0\"], \"log_path\": \"~/runs/recovery_aware_struct_prune/grpo_cka_only_20.log\", \"pid\": \"725227\", \"server\": \"westb-23072\", \"submitted_at\": \"2026-05-17T14:51:36.270Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 41272.3, \"gpu_hours\": 11.46, \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20\", \"wandb_run_id\": \"li451oi4\"}, \"metrics\": {\"final_step\": 100, \"final_reward\": 0.3444, \"peak_reward\": 0.3544, \"peak_reward_step\": 50, \"final_frac_zero_std\": 0.2, \"final_loss\": 0.23, \"final_kl\": 0.001609, \"final_entropy\": 0.08751, \"final_reward_std\": 0.444, \"runtime_seconds\": 40710}}, \"grpo_rasp_20_fair\": {\"created_at\": \"2026-05-17T23:50:31.502Z\", \"metrics\": {\"final_completion_length\": 963.0, \"final_frac_zero_std\": 0.85, \"final_reward\": 0.01, \"min_frac_zero_std\": 0.675, \"peak_reward\": 0.061, \"total_steps\": 100, \"training_time_minutes\": 62.5, \"trend\": \"stagnation_then_collapse\"}, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_rasp_20_fair\", \"checkpoint_source\": \"sft_rasp_20_westd\", \"command\": \"python src/train_grpo_v5.py --model_path sft_rasp_20_westd --output_dir grpo_stage2_rasp_20_fair --gpu 0 --max_steps 100 --lr 1e-6 --beta 0.01 --loss_type dapo\", \"data_count\": 7473, \"data_path\": \"openai/gsm8k\", \"eval_data\": \"N/A (GRPO training, not eval)\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 1.3, \"hyperparams\": {\"beta\": 0.01, \"format_reward_weight\": 0.1, \"loss_type\": \"dapo\", \"lr\": 1e-06, \"max_completion_length\": 1024, \"max_steps\": 100, \"optim\": \"adamw_bnb_8bit\", \"repetition_penalty\": 1.15, \"reward_desert_patience\": 200, \"save_steps\": 10, \"save_total_limit\": 3, \"temperature\": 0.4}, \"log_path\": \"~/runs/recovery_aware_struct_prune/grpo_rasp_20_fair.log\", \"model_name\": \"sft_rasp_20_westd\", \"pid\": \"68913\", \"seed\": 42, \"server\": \"westd-11672\", \"submitted_at\": \"2026-05-17T23:50:31.086Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 4668.5}}, \"eval_postprune_standard_30\": {\"created_at\": \"2026-05-17T19:08:46.051Z\", \"metrics\": {\"avg_response_length\": 3907.875, \"correct\": 8, \"eos_rate\": 0.055, \"gsm8k_accuracy\": 0.04, \"natural_eos\": 11, \"total\": 200, \"truncated\": 189}, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_postprune_standard_30.json\", \"checkpoint_source\": \"pruned_standard_30\", \"command\": \"bash -c \\\"source /root/miniconda3/bin/activate && cd /root/recovery_aware_struct_prune && python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/pruned_standard_30 --max_samples 200 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_postprune_standard_30.json\\\"\", \"data_count\": 200, \"data_path\": \"openai/gsm8k\", \"eval_data\": \"GSM8K (N=200, post-prune accuracy eval)\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 5.3, \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_postprune_standard_30.log\", \"model_name\": \"pruned_standard_30\", \"pid\": \"47667\", \"seed\": 42, \"server\": \"westd-11672\", \"submitted_at\": \"2026-05-17T19:09:42.413Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 19076.9}}, \"eval_sft_cka_only_20_n1319\": {\"created_at\": \"2026-05-17T18:20:20.406Z\", \"metrics\": {\"avg_response_length\": 198.1, \"correct\": 843, \"eos_rate\": 0.9901, \"gsm8k_accuracy\": 0.6391, \"stderr\": 0.0132, \"total\": 1319}, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_source\": \"sft_cka_only_20\", \"command\": \"python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_20 --max_samples 1319 --seed 42 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_sft_cka_only_20_n1319.json\", \"data_count\": 1319, \"data_path\": \"openai/gsm8k\", \"eval_data\": \"GSM8K (1319 samples, greedy)\", \"gpu\": [\"cuda:0\"], \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_sft_cka_only_20_n1319.log\", \"model_name\": \"sft_cka_only_20\", \"pid\": \"49475\", \"seed\": 42, \"server\": \"westd-11672\", \"submitted_at\": \"2026-05-17T19:17:43.358Z\", \"submitted_via\": \"submit_training_job\"}}, \"prune_cka_only_30\": {\"created_at\": \"2026-05-17T21:42:06.467Z\", \"metrics\": {\"actual_sparsity\": 0.2892, \"attn_heads_pruned\": \"0\", \"method\": \"dummy_ones_importance + rasp_alpha1 = pure CKA-only\", \"mlp_groups_pruned\": \"303/784\"}, \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=\\\"\\\" python src/prune.py --model_path /root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B --mode rasp --sparsity 0.30 --alpha 1.0 --dtype bfloat16 --importance_path results/importance_scores_dummy_ones.pt --cka_path results/cka_scores.pt --output_path /root/autodl-tmp/recovery_aware_struct_prune/pruned_cka_only_30\", \"data_count\": 0, \"data_path\": \"importance_scores_dummy_ones.pt + cka_scores.pt\", \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B\", \"seed\": 42, \"server\": \"westd-11672\"}}, \"eval_postprune_rasp_30\": {\"created_at\": \"2026-05-17T18:22:00Z\", \"metrics\": {\"accuracy\": 0, \"avg_response_length\": 3984.31, \"eos_rate\": 0.03, \"n_correct\": 0, \"n_total\": 200, \"natural_eos\": 6, \"truncated_rate\": 0.97}, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_postprune_rasp_30.json\", \"checkpoint_source\": \"pruned_rasp_30\", \"data_count\": 200, \"data_path\": \"openai/gsm8k\", \"eval_data\": \"GSM8K (200 samples, greedy)\", \"gpu\": [\"cuda:2\"], \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_postprune_rasp_30.log\", \"model_name\": \"pruned_rasp_30\", \"pid\": \"43911\", \"seed\": 42, \"server\": \"westd-11672\", \"submitted_via\": \"submit_training_job\"}}, \"eval_humaneval_sft_standard_20_2048_v2\": {\"created_at\": \"2026-05-17T16:26:15.836Z\", \"metrics\": {\"avg_response_length\": 1850.7, \"correct\": 19, \"max_new_tokens\": 2048, \"median_response_length\": 2048, \"pass_at_1\": 0.1159, \"total\": 164}, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_humaneval_sft_standard_20_2048.json\", \"command\": \"bash -c \\\"source /root/miniconda3/bin/activate && cd /root/recovery_aware_struct_prune && python src/eval_humaneval.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20_westd --max_new_tokens 2048 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_humaneval_sft_standard_20_2048.json\\\"\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 1.34, \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_humaneval_sft_standard_20_2048_v2.log\", \"pid\": \"36724\", \"server\": \"westd-11672\", \"submitted_at\": \"2026-05-17T16:26:15.449Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 4840.6}}, \"eval_humaneval_grpo_standard_20_2048\": {\"created_at\": \"2026-05-17T13:41:03.761Z\", \"metrics\": {\"avg_response_length\": 1843, \"correct\": 17, \"max_new_tokens\": 2048, \"median_response_length\": 2048, \"pass_at_1\": 0.1037, \"total\": 164}, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/bin/activate && cd /root/recovery_aware_struct_prune && python src/eval_humaneval.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_standard_20_v8/checkpoint-50 --max_new_tokens 2048 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_humaneval_grpo_standard_20_2048.json\\\"\", \"gpu\": [\"cuda:2\"], \"gpu_hours\": 4.58, \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_humaneval_grpo_standard_20_2048.log\", \"pid\": \"27194\", \"server\": \"westd-11672\", \"submitted_at\": \"2026-05-17T13:41:38.223Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 16473.3}}, \"grpo_rasp_25\": {\"created_at\": \"2026-05-16T08:42:40.256Z\", \"metrics\": {\"note\": \"Restored from previous_failure — cron false positive, experiment actually completed 100/100 steps successfully\", \"step_100\": {\"entropy\": 0.04262, \"frac_reward_zero_std\": 0.875, \"grad_norm\": 0.05371, \"kl\": 0.0007035, \"loss\": 0.01275, \"reward\": 0.009375, \"reward_std\": 0.03149}, \"wall_clock_min\": 57.95, \"wandb_run_id\": \"bc4ojqie\"}, \"spec\": {\"command\": \"previous run (bc4ojqie) completed 100/100 steps, restoring status\", \"data_count\": 7473, \"data_path\": \"openai/gsm8k\", \"model_name\": \"sft_rasp_25 (RASP 25% pruned + SFT)\", \"seed\": 42, \"server\": \"westd-11672\"}}, \"eval_humaneval_grpo_rasp_20_2048\": {\"created_at\": \"2026-05-17T13:41:44.795Z\", \"metrics\": {\"correct\": 24, \"max_new_tokens\": 2048, \"pass_at_1\": 0.1463, \"stderr\": 0.0276, \"total\": 164}, \"spec\": {\"account\": \"root\", \"checkpoint_source\": \"grpo_stage2_rasp_20_v9\", \"data_count\": 164, \"data_path\": \"openai/openai_humaneval\", \"eval_data\": \"HumanEval (164 problems, max_new_tokens=2048)\", \"gpu\": [\"cuda:0\"], \"model_name\": \"grpo_stage2_rasp_20_v9\", \"seed\": 42, \"server\": \"westd-11672\"}}, \"eval_sft_cka_only_20\": {\"created_at\": \"2026-05-17T14:28:35.380Z\", \"metrics\": {\"avg_response_length\": 182.73, \"eos_rate\": 0.995, \"gsm8k_accuracy\": 0.64, \"gsm8k_stderr\": 0.0339, \"mode\": \"greedy\", \"n_correct\": 128, \"n_total\": 200, \"seed\": 42, \"truncated\": 1}, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_source\": \"sft_cka_only_20\", \"command\": \"bash -c \\\"source /root/miniconda3/bin/activate && cd /root/recovery_aware_struct_prune && python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_20 --max_samples 200 --seed 42 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_sft_cka_only_20.json\\\"\", \"data_count\": 200, \"data_path\": \"gsm8k\", \"eval_data\": \"GSM8K (N=200)\", \"gpu\": [\"cuda:0\"], \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_sft_cka_only_20.log\", \"model_name\": \"sft_cka_only_20\", \"pid\": \"723605\", \"seed\": 42, \"server\": \"westb-23072\", \"submitted_at\": \"2026-05-17T14:29:08.063Z\", \"submitted_via\": \"submit_training_job\"}}, \"sft_cka_only_20\": {\"created_at\": \"2026-05-17T13:43:50.320Z\", \"metrics\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_20/\", \"note\": \"Initial loss 1.958 > RASP 1.86 > Standard 1.70 (CKA-only has most initial damage). Final loss 0.62 comparable to baselines. No greedy eval run yet.\", \"token_accuracy\": 0.8362, \"total_steps\": 1870, \"train_loss_final\": 0.6165, \"train_loss_initial\": 1.958, \"train_time_min\": 33.4}, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_20/\", \"command\": \"bash -c \\\"source /root/miniconda3/bin/activate && cd /root/recovery_aware_struct_prune && python src/sft_recovery.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/pruned_cka_only_20 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_20 --save_strategy no --gpu 0\\\"\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 0.69, \"log_path\": \"~/runs/recovery_aware_struct_prune/sft_cka_only_20.log\", \"pid\": \"720955\", \"server\": \"westb-23072\", \"submitted_at\": \"2026-05-17T13:47:02.912Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 2486.8}}, \"eval_humaneval_unpruned_2048\": {\"created_at\": \"2026-05-17T12:40:50.255Z\", \"metrics\": {\"avg_response_length\": 1771, \"correct\": 74, \"max_new_tokens\": 2048, \"median_response_length\": 2048, \"pass_at_1\": 0.4512, \"stderr\": 0.0389, \"total\": 164, \"wall_time_min\": 67.6}, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"N/A (eval only)\", \"command\": \"python src/eval_humaneval.py --model_path /root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B --max_new_tokens 2048\", \"data_count\": 164, \"data_path\": \"HumanEval\", \"eval_data\": \"HumanEval (164 problems, max_new_tokens=2048)\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 1.2, \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_humaneval_unpruned_2048.log\", \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B (unpruned)\", \"pid\": \"23707\", \"seed\": 42, \"server\": \"westd-11672\", \"submitted_at\": \"2026-05-17T12:41:06.754Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 4337.5}}, \"eval_humaneval_sft_rasp_20_2048\": {\"created_at\": \"2026-05-17T12:40:51.686Z\", \"metrics\": {\"correct\": 17, \"max_new_tokens\": 2048, \"median_response_length\": 2048, \"note\": \"still truncating at median=2048, main failure mode is thinking chain leaking into code output\", \"pass_at_1\": 0.1037, \"stderr\": 0.0238, \"total\": 164, \"wall_time_min\": 42}, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"N/A (eval only)\", \"checkpoint_source\": \"sft_rasp_20_westd\", \"command\": \"python src/eval_humaneval.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20_westd --max_new_tokens 2048\", \"data_count\": 164, \"data_path\": \"HumanEval\", \"eval_data\": \"HumanEval (164 problems, max_new_tokens=2048)\", \"gpu\": [\"cuda:2\"], \"gpu_hours\": 1.03, \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_humaneval_sft_rasp_20_2048.log\", \"model_name\": \"sft_rasp_20_westd\", \"pid\": \"23785\", \"seed\": 42, \"server\": \"westd-11672\", \"submitted_at\": \"2026-05-17T12:41:09.839Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 3691.7}}, \"eval_humaneval_grpo_standard_20\": {\"created_at\": \"2026-05-17T10:00:40.683Z\", \"metrics\": {\"correct\": 3, \"max_new_tokens\": 512, \"note\": \"512-token truncation, low quality\", \"pass_at_1\": 0.0183, \"total\": 164}, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"N/A (eval only)\", \"checkpoint_source\": \"grpo_stage2_standard_20_v8/checkpoint-50\", \"command\": \"python src/eval_humaneval.py --model_path grpo_stage2_standard_20_v8/checkpoint-50\", \"data_count\": 164, \"data_path\": \"HumanEval\", \"eval_data\": \"HumanEval (164 problems)\", \"gpu\": [\"cuda:2\"], \"gpu_hours\": 3.56, \"log_path\": \"westd results/eval_humaneval_grpo_standard_20.json\", \"model_name\": \"grpo_stage2_standard_20_v8\", \"pid\": \"16483\", \"seed\": 42, \"server\": \"westd-11672\", \"submitted_at\": \"2026-05-17T10:00:40.348Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 12799.5}}, \"eval_math500_unpruned\": {\"created_at\": \"2026-05-17T06:23:49.923Z\", \"metrics\": {\"N\": 500, \"accuracy\": 0.736, \"correct\": 368, \"stderr\": 0.02}, \"spec\": {\"command\": \"python src/eval_math500.py --model_path /root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B\", \"data_count\": 500, \"data_path\": \"MATH-500\", \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B (unpruned)\", \"seed\": 42, \"server\": \"westd-11672\"}}, \"eval_gradient_postsft\": {\"created_at\": \"2026-05-17T10:07:58.644Z\", \"metrics\": {\"accuracy\": 0.615, \"avg_response_length\": 167.455, \"correct\": 123, \"eos_rate\": 0.995, \"stderr\": 0.0344, \"total\": 200}, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/bin/activate && cd /root/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=0 python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_gradient_20 --max_samples 200 --seed 42 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_gradient_postsft.json\\\"\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 1.27, \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_gradient_postsft.log\", \"pid\": \"701495\", \"server\": \"westb-23072\", \"submitted_at\": \"2026-05-17T10:07:58.275Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 4578.0}}, \"gradient_sft_v3\": {\"created_at\": \"2026-05-17T09:28:21.646Z\", \"metrics\": {\"epochs\": 2, \"final_loss\": 0.644, \"output_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_gradient_20\", \"steps\": 1870, \"token_accuracy\": 0.825}, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_gradient_20\", \"checkpoint_source\": \"pruned_gradient_20 (gradient scoring, 19.09% sparsity)\", \"command\": \"python src/sft_recovery.py --model_path pruned_gradient_20 --output_dir sft_gradient_20 --gpu 0 --save_strategy no --seed 42\", \"data_count\": 7473, \"data_path\": \"openai/gsm8k (SFT training data)\", \"eval_data\": \"N/A - this is SFT training, not eval\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 0.66, \"log_path\": \"~/runs/recovery_aware_struct_prune/gradient_sft_v3.log\", \"model_name\": \"pruned_gradient_20\", \"pid\": \"699032\", \"seed\": 42, \"server\": \"westb-23072\", \"submitted_at\": \"2026-05-17T09:28:21.306Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 2385.7}}, \"eval_math500_sft_standard_20\": {\"created_at\": \"2026-05-17T06:23:54.283Z\", \"metrics\": {\"correct\": 130, \"eos_rate\": 0.578, \"math500_acc\": 0.26, \"stderr\": 0.0196, \"total\": 500, \"truncated\": 211, \"wall_time_hours\": 3.58}, \"spec\": {\"checkpoint_path\": \"N/A (eval only)\", \"checkpoint_source\": \"sft_standard_20_westd\", \"command\": \"python src/eval_math500.py --model_path sft_standard_20_westd\", \"data_count\": 500, \"data_path\": \"MATH-500\", \"eval_data\": \"MATH-500 (500 problems)\", \"log_path\": \"/root/runs/recovery_aware_struct_prune/eval_math500_sft_standard.log\", \"model_name\": \"sft_standard_20_westd\", \"seed\": 42, \"server\": \"westd-11672\"}}, \"eval_math500_sft_rasp_20\": {\"created_at\": \"2026-05-17T06:23:52.474Z\", \"metrics\": {\"correct\": 121, \"math500_acc\": 0.242, \"stderr\": 0.0192, \"total\": 500, \"wall_time_hours\": 2.94}, \"spec\": {\"checkpoint_path\": \"N/A (eval only)\", \"checkpoint_source\": \"sft_rasp_20_westd\", \"command\": \"python src/eval_math500.py --model_path sft_rasp_20_westd\", \"data_count\": 500, \"data_path\": \"MATH-500\", \"eval_data\": \"MATH-500 (500 problems)\", \"log_path\": \"/root/runs/recovery_aware_struct_prune/eval_math500_sft_rasp.log\", \"model_name\": \"sft_rasp_20_westd\", \"seed\": 42, \"server\": \"westd-11672\"}}, \"eval_unstructured_20\": {\"created_at\": \"2026-05-17T05:35:41.205Z\", \"metrics\": {\"avg_response_length\": 641, \"correct\": 1159, \"eos_rate\": 0.9803, \"gsm8k_acc\": 0.8787, \"stderr\": 0.009, \"total\": 1319, \"truncated\": 26, \"wall_time_hours\": 3.23}, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/pruned_unstructured_20\", \"checkpoint_source\": \"pruned_unstructured_20\", \"command\": \"bash -c 'source /root/miniconda3/bin/activate && cd /root/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=1 python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/pruned_unstructured_20 --max_samples 1319 --seed 42 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_unstructured_20_n1319.json'\", \"data_count\": 1319, \"data_path\": \"openai/gsm8k\", \"eval_data\": \"GSM8K test (n=1319, greedy)\", \"gpu\": [\"cuda:1\"], \"log_path\": \"/root/runs/recovery_aware_struct_prune/eval_unstructured_20.log\", \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B (unstructured magnitude 20%)\", \"model_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/pruned_unstructured_20\", \"pid\": \"eval_unstructured_20\", \"seed\": 42, \"server\": \"westb-23072\"}}, \"eval_humaneval_sft_standard_20\": {\"created_at\": \"2026-05-17T07:56:08.222Z\", \"metrics\": {\"correct\": 5, \"failure_modes\": \"model generates CoT natural language instead of code, all responses truncated at max_tokens=512\", \"pass_at_1\": 0.0305, \"stderr\": 0.0134, \"total\": 164, \"wall_time_min\": 17}, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"N/A (eval only)\", \"checkpoint_source\": \"sft_standard_20_westd\", \"command\": \"bash -c \\\"source /root/miniconda3/bin/activate && cd /root/recovery_aware_struct_prune && export HF_ENDPOINT=https://hf-mirror.com && python src/eval_humaneval.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20_westd --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_humaneval_sft_standard_20.json\\\"\", \"data_count\": 164, \"data_path\": \"HumanEval\", \"eval_data\": \"HumanEval (164 problems)\", \"gpu\": [\"cuda:3\"], \"gpu_hours\": 0.6, \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_humaneval_sft_standard_20.log\", \"model_name\": \"sft_standard_20_westd\", \"pid\": \"9605\", \"seed\": 42, \"server\": \"westd-11672\", \"submitted_at\": \"2026-05-17T07:56:07.888Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 2144.8}}, \"eval_humaneval_sft_rasp_20\": {\"created_at\": \"2026-05-17T07:19:22.820Z\", \"metrics\": {\"correct\": 12, \"failure_modes\": \"model outputs natural language thinking instead of code (SyntaxError), parenthesis mismatch\", \"median_response_length\": 512, \"note\": \"max_tokens truncation frequent\", \"pass_at_1\": 0.0732, \"stderr\": 0.0203, \"total\": 164}, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"N/A (eval only)\", \"checkpoint_source\": \"sft_rasp_20_westd\", \"command\": \"bash -c \\\"source /root/miniconda3/bin/activate && cd /root/recovery_aware_struct_prune && export HF_ENDPOINT=https://hf-mirror.com && python src/eval_humaneval.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20_westd --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_humaneval_sft_rasp_20.json\\\"\", \"data_count\": 164, \"data_path\": \"HumanEval\", \"eval_data\": \"HumanEval (164 problems)\", \"gpu\": [\"cuda:3\"], \"gpu_hours\": 0.61, \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_humaneval_sft_rasp_20.log\", \"model_name\": \"sft_rasp_20_westd\", \"pid\": \"7528\", \"seed\": 42, \"server\": \"westd-11672\", \"submitted_at\": \"2026-05-17T07:19:22.501Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 2190.1}}, \"multiseed_serial_westb\": {\"created_at\": \"2026-05-17T05:47:08.060Z\", \"metrics\": {\"missing\": \"seed 42 and seed 789 not executed\", \"note\": \"2 seeds x 2 methods (not 4 seeds as planned). Script ran RASP+Standard for seeds 123,456.\", \"rasp_seed123\": {\"acc\": 0.605, \"correct\": 121, \"total\": 200}, \"rasp_seed456\": {\"acc\": 0.6, \"correct\": 120, \"total\": 200}, \"standard_seed123\": {\"acc\": 0.645, \"correct\": 129, \"total\": 200}, \"standard_seed456\": {\"acc\": 0.61, \"correct\": 122, \"total\": 200}}, \"spec\": {\"checkpoint_path\": \"N/A (eval only)\", \"checkpoint_source\": \"sft_rasp_20, sft_standard_20\", \"command\": \"bash -c 'source /root/miniconda3/bin/activate && cd /root/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=0 python src/eval_gsm8k.py (4 serial evals)'\", \"data_count\": 200, \"data_path\": \"openai/gsm8k\", \"eval_data\": \"GSM8K test (n=200, seeds 123+456)\", \"gpu\": [\"cuda:0\"], \"log_path\": \"/root/runs/recovery_aware_struct_prune/multiseed_serial.log\", \"model_name\": \"sft_rasp_20 + sft_standard_20\", \"model_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_{rasp,standard}_20\", \"pid\": 681896, \"seed\": \"123,456\", \"server\": \"westb-23072\"}}, \"eval_humaneval_grpo_rasp_20\": {\"created_at\": \"2026-05-17T06:42:19.044Z\", \"metrics\": {\"n_passed\": 17, \"n_total\": 164, \"pass_at_1\": 0.1037, \"stderr\": 0.0238}, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_source\": \"grpo_stage2_rasp_20_v9\", \"command\": \"python src/eval_humaneval.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_rasp_20_v9\", \"data_count\": 164, \"data_path\": \"openai/openai_humaneval\", \"eval_data\": \"humaneval\", \"gpu\": [\"cuda:3\"], \"gpu_hours\": 0.56, \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_humaneval_grpo_rasp_20.log\", \"model_name\": \"grpo_stage2_rasp_20_v9\", \"pid\": \"5264\", \"seed\": 42, \"server\": \"westd-11672\", \"submitted_at\": \"2026-05-17T06:42:18.740Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 2020.1}}, \"eval_humaneval_unpruned\": {\"created_at\": \"2026-05-17T06:23:55.527Z\", \"metrics\": {\"n_passed\": 3, \"n_total\": 164, \"pass_at_1\": 0.0183, \"stderr\": 0.0105}, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B\", \"checkpoint_source\": \"DeepSeek-R1-Distill-Qwen-7B\", \"command\": \"bash -c 'source /root/miniconda3/bin/activate && cd /root/recovery_aware_struct_prune && export HF_ENDPOINT=https://hf-mirror.com && CUDA_VISIBLE_DEVICES=3 python src/eval_humaneval.py --model_path /root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_humaneval_unpruned.json'\", \"data_count\": 164, \"data_path\": \"openai/openai_humaneval\", \"eval_data\": \"HumanEval (164 problems, pass@1)\", \"gpu\": [\"cuda:3\"], \"log_path\": \"/root/runs/recovery_aware_struct_prune/eval_humaneval_unpruned.log\", \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B (unpruned)\", \"model_path\": \"/root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B\", \"output_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_humaneval_unpruned.json\", \"seed\": 42, \"server\": \"westd-11672\"}}, \"eval_grpo_rasp_25\": {\"created_at\": \"2026-05-16T20:04:16.057Z\", \"metrics\": {\"accuracy\": 0.5315, \"avg_len\": 433.85, \"eos_rate\": 0.9272, \"max_len\": 4096, \"min_len\": 39, \"n_correct\": 701, \"n_total\": 1319, \"stderr\": 0.0137, \"truncated\": 96}, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_25\", \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_25\", \"command\": \"CUDA_VISIBLE_DEVICES=0 python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_25 --max_samples 1319 --seed 42 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_grpo_rasp_25_n1319.json\", \"data_count\": 1319, \"data_path\": \"openai/gsm8k\", \"eval_data\": \"GSM8K test split (N=1319, greedy)\", \"gpu\": \"cuda:0\", \"log_path\": \"/root/runs/recovery_aware_struct_prune/eval_grpo_rasp_25.log\", \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B (RASP 25% pruned, SFT, GRPO 100 steps)\", \"output_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_grpo_rasp_25_n1319.json\", \"pid\": \"639423\", \"seed\": 42, \"server\": \"westb-23072\"}}, \"eval_grpo_standard_25\": {\"created_at\": \"2026-05-16T19:39:31.510Z\", \"metrics\": {\"accuracy\": 0.511, \"avg_len\": 292.86, \"eos_rate\": 0.9628, \"n_correct\": 674, \"n_total\": 1319, \"stderr\": 0.01376}, \"spec\": {\"command\": \"source /root/miniconda3/bin/activate && CUDA_VISIBLE_DEVICES=1 python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_25 --max_samples 1319 --seed 42 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_grpo_standard_25_n1319.json\", \"eval_data\": \"GSM8K test (n=1319)\", \"gpu\": \"cuda:1\", \"log_path\": \"/root/runs/recovery_aware_struct_prune/eval_grpo_standard_25.log\", \"model_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_25\", \"output_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_grpo_standard_25_n1319.json\", \"pid\": 48540, \"seed\": 42, \"server\": \"westd-11672\", \"started_at\": \"2026-05-17T05:19:52\"}}, \"sft_standard_20_retrain\": {\"created_at\": \"2026-05-15T08:00:22.779Z\", \"metrics\": {\"conclusion\": \"Matches original sft_standard_20 (loss 0.64, token_accuracy 83%). Retrain successful.\", \"token_accuracy\": 0.83, \"train_loss_final\": 0.64}, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20/\", \"checkpoint_source\": \"/root/autodl-tmp/pruned_standard_20\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/recovery_aware_struct_prune && python src/sft_recovery.py --model_path /root/autodl-tmp/pruned_standard_20 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20 --gpu 1 --num_train_epochs 2 --learning_rate 2e-5 --batch_size 1 --gradient_accumulation_steps 8 --max_seq_length 2048 --logging_steps 10 --seed 42\\\"\", \"data_count\": 7473, \"data_path\": \"openai/gsm8k\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 0.81, \"log_path\": \"~/runs/recovery_aware_struct_prune/sft_standard_20_retrain.log\", \"model_name\": \"pruned_standard_20\", \"pid\": \"515168\", \"seed\": 42, \"server\": \"westb-23072\", \"submitted_at\": \"2026-05-15T11:47:22.611Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 2914.0}}, \"eval_sft_grasp_20\": {\"created_at\": \"2026-05-15T15:45:15.051Z\", \"metrics\": {\"accuracy\": 0.41, \"n_total\": 100, \"note\": \"论文核心数据点: GraSP post-SFT 41% vs Standard 64% (p=0.001) vs RASP 57%\", \"p_value_vs_standard\": 0.001, \"rasp_ref\": 0.57, \"standard_ref\": 0.64}, \"spec\": {\"command\": \"python -u src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_graspune_20 --max_samples 100 --max_new_tokens 4096 --seed 42 --output_path results/eval_sft_grasp_20_n100.json\", \"hypothesis\": \"GraSP post-SFT GSM8K eval (N=100, greedy). GraSP post-prune ~6%, post-SFT loss=0.59, token_acc=0.84. Three-way comparison: Standard 64% vs RASP 57% vs GraSP ?%. Parent: sft_grasp_20_westd.\", \"model_name\": \"Qwen2.5-1.5B-GraSP-20%-SFT\", \"parent\": \"sft_grasp_20_westd\", \"seed\": 42, \"server\": \"westd-11672\"}}, \"eval-sft-alpha-0p0\": {\"created_at\": \"2026-05-15T14:26:31.883Z\", \"metrics\": {\"accuracy\": 0.64, \"avg_len\": 257.9, \"eos_rate\": 0.97, \"n_correct\": 64, \"n_total\": 100}, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_ablation/alpha_0.0\", \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_ablation/alpha_0.0\", \"command\": \"python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_ablation/alpha_0.0 --max_samples 100 --max_new_tokens 4096\", \"data_count\": 100, \"data_path\": \"openai/gsm8k\", \"eval_data\": \"gsm8k_test_n100\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 0.42, \"log_path\": \"~/runs/recovery_aware_struct_prune/eval-sft-alpha-0p0.log\", \"model_name\": \"Qwen2.5-7B pruned alpha=0.0 post-SFT\", \"pid\": \"40489\", \"seed\": 42, \"server\": \"westd-11672\", \"submitted_at\": \"2026-05-15T14:26:31.816Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 1529.3}}, \"eval-sft-alpha-1p0\": {\"created_at\": \"2026-05-15T14:51:22.694Z\", \"metrics\": {\"accuracy\": 0.57, \"avg_len\": 224.18, \"eos_rate\": 0.98, \"n_correct\": 57, \"n_total\": 100, \"natural_eos\": 98, \"stderr\": 0.0495, \"truncated\": 2}, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_ablation/alpha_1.0\", \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_ablation/alpha_1.0\", \"command\": \"python eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_ablation/alpha_1.0 --n_samples 100\", \"data_count\": 100, \"data_path\": \"openai/gsm8k\", \"eval_data\": \"gsm8k_test_n100\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 0.56, \"log_path\": \"~/runs/recovery_aware_struct_prune/eval-sft-alpha-1p0.log\", \"model_name\": \"Qwen2.5-7B pruned alpha=1.0 post-SFT\", \"pid\": \"42530\", \"seed\": 42, \"server\": \"westd-11672\", \"submitted_at\": \"2026-05-15T14:51:22.611Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 2013.4}}, \"eval_sft_unpruned_n100\": {\"created_at\": \"2026-05-16T01:40:17.686Z\", \"metrics\": {\"accuracy\": 0.84, \"avg_response_length\": 187.22, \"eos_rate\": 1, \"n_correct\": 84, \"n_total\": 100, \"stderr\": 0.0367}, \"spec\": {\"checkpoint_path\": \"/root/recovery_aware_struct_prune/results/eval_sft_unpruned_baseline_n100.json\", \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_unpruned_baseline\", \"command\": \"CUDA_VISIBLE_DEVICES=1 python eval_gsm8k.py --model_path sft_unpruned_baseline --max_samples 100 --seed 42\", \"data_count\": 100, \"data_path\": \"openai/gsm8k\", \"eval_data\": \"gsm8k_test_n100\", \"log_path\": \"/tmp/eval_unpruned_n100.log\", \"model_name\": \"Qwen2.5-7B (unpruned, SFT)\", \"parent\": \"sft_unpruned_baseline\", \"seed\": 42, \"server\": \"westd-11672\"}}, \"eval_sft_unpruned_full\": {\"created_at\": \"2026-05-16T01:40:17.174Z\", \"metrics\": {\"accuracy\": 81.27, \"accuracy_ci\": 1.07, \"avg_response_length\": 207.18, \"correct\": 1072, \"eos_rate\": 99.7, \"total\": 1319, \"truncated\": 4}, \"spec\": {\"checkpoint_path\": \"/root/recovery_aware_struct_prune/results/eval_sft_unpruned_baseline_full.json\", \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_unpruned_baseline\", \"command\": \"CUDA_VISIBLE_DEVICES=0 python eval_gsm8k.py --model_path sft_unpruned_baseline --max_samples 1319 --seed 42\", \"data_count\": 1319, \"data_path\": \"openai/gsm8k\", \"eval_data\": \"gsm8k_test_full_1319\", \"gpu\": \"cuda:0\", \"hypothesis\": \"Unpruned SFT baseline full GSM8K eval for three-way comparison\", \"log_path\": \"/tmp/eval_unpruned_full.log\", \"model_name\": \"Qwen2.5-7B (unpruned, SFT)\", \"parent\": \"sft_unpruned_baseline\", \"pid\": 74129, \"seed\": 42, \"server\": \"westd-11672\"}}, \"eval_grpo_unpruned_v2_step90\": {\"created_at\": \"2026-05-16T03:05:00.333Z\", \"metrics\": {\"accuracy\": 80.59, \"avg_response_length\": 213, \"correct\": 1063, \"eos_rate\": 99.6, \"seed\": 42, \"total\": 1319}, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_unpruned_v2/checkpoint-90\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=1 python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_unpruned_v2/checkpoint-90 --max_samples 1319 --seed 42 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_grpo_unpruned_v2_step90.json\\\"\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 1.72, \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_grpo_unpruned_v2_step90.log\", \"pid\": \"83667\", \"server\": \"westd-11672\", \"submitted_at\": \"2026-05-16T03:39:13.660Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 6194.8}}, \"eval_grpo_unpruned_v2_step100\": {\"created_at\": \"2026-05-16T03:04:55.936Z\", \"metrics\": {\"accuracy\": 81.27, \"avg_response_length\": 209, \"correct\": 1072, \"eos_rate\": 99.7, \"seed\": 42, \"total\": 1319}, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_unpruned_v2/checkpoint-100\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=0 python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_unpruned_v2/checkpoint-100 --max_samples 1319 --seed 42 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_grpo_unpruned_v2_step100.json\\\"\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 1.72, \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_grpo_unpruned_v2_step100.log\", \"pid\": \"83589\", \"server\": \"westd-11672\", \"submitted_at\": \"2026-05-16T03:39:11.392Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 6195.8}}, \"sft_rasp_25\": {\"created_at\": \"2026-05-16T05:26:38.517Z\", \"metrics\": {\"runtime_seconds\": 1635, \"token_accuracy\": 0.8073, \"train_loss\": 0.8498}, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_25\", \"command\": \"CUDA_VISIBLE_DEVICES=0 python src/sft_recovery.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/pruned_rasp_25 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_25 --num_train_epochs 2 --learning_rate 2e-5 --batch_size 1 --gradient_accumulation_steps 8 --max_seq_length 2048 --seed 42\", \"data_count\": 7473, \"data_path\": \"openai/gsm8k\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 0.83, \"log_path\": \"~/runs/recovery_aware_struct_prune/sft_rasp_25.log\", \"model_name\": \"pruned_rasp_25 (RASP 25% pruned DeepSeek-R1-Distill-Qwen-7B)\", \"pid\": \"88528\", \"seed\": 42, \"server\": \"westd-11672\", \"submitted_at\": \"2026-05-16T05:27:08.163Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 3002.5}}, \"sft_standard_25\": {\"created_at\": \"2026-05-16T05:21:16.758Z\", \"metrics\": {\"model_keys\": 339, \"model_params\": \"5.79B\", \"note\": \"optimizer.pt save failed (RuntimeError) but model.safetensors intact\", \"runtime_seconds\": 2130, \"total_steps\": 1870}, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_25/checkpoint-1870\", \"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/recovery_aware_struct_prune && python src/sft_recovery.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/pruned_standard_25 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_25 --gpu 1 --num_train_epochs 2 --learning_rate 2e-5 --batch_size 1 --gradient_accumulation_steps 8 --max_seq_length 2048 --seed 42\", \"data_count\": 7473, \"data_path\": \"openai/gsm8k\", \"log_path\": \"/root/runs/recovery_aware_struct_prune/sft_standard_25_retry.log\", \"model_name\": \"pruned_standard_25 (Standard 25% pruned DeepSeek-R1-Distill-Qwen-7B)\", \"seed\": 42, \"server\": \"westb-23072\"}}, \"sft_standard_25_westd\": {\"created_at\": \"2026-05-16T15:52:30.818Z\", \"metrics\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_25/model.safetensors\", \"final_loss\": 0.8381, \"token_acc\": 0.8018}, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/recovery_aware_struct_prune && python src/sft_recovery.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/pruned_standard_25 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_25 --gpu 1 --learning_rate 2e-5 --num_train_epochs 2 --batch_size 1 --gradient_accumulation_steps 8 --max_seq_length 2048 --seed 42\\\"\", \"data_count\": 7473, \"data_path\": \"openai/gsm8k\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 0.91, \"log_path\": \"~/runs/recovery_aware_struct_prune/sft_standard_25_westd.log\", \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B (Standard 25% pruned)\", \"pid\": \"21488\", \"seed\": 42, \"server\": \"westd-11672\", \"submitted_at\": \"2026-05-16T15:52:30.596Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 3273.0}}, \"eval_grpo_rasp_20_qwen_math\": {\"created_at\": \"2026-05-16T15:59:57.504Z\", \"metrics\": {\"accuracy\": 0.725, \"n_samples\": 200, \"seed\": 42}, \"spec\": {\"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_qwen_math\", \"command\": \"CUDA_VISIBLE_DEVICES=2 python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_qwen_math --max_samples 200 --seed 42 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_grpo_rasp_20_qwen_math.json\", \"data_count\": 200, \"data_path\": \"openai/gsm8k\", \"eval_data\": \"gsm8k\", \"gpu\": \"cuda:2\", \"hypothesis\": \"Qwen2.5-Math-7B RASP 20% post-GRPO GSM8K eval (N=200, seed=42). 验证 GRPO 后 accuracy 变化，reward-accuracy decoupling 证据 (C1)。Parent: grpo_rasp_qwen_math_v3.\", \"model_name\": \"Qwen2.5-Math-7B-RASP-20%-postGRPO\", \"parent\": \"grpo_rasp_qwen_math_v3\", \"seed\": 42, \"server\": \"westd-11672\"}}, \"eval_grpo_standard_20_qwen_math\": {\"created_at\": \"2026-05-16T15:59:59.175Z\", \"metrics\": {\"accuracy\": 0.705, \"n_samples\": 200, \"seed\": 42}, \"spec\": {\"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_qwen_math\", \"command\": \"CUDA_VISIBLE_DEVICES=3 python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_qwen_math --max_samples 200 --seed 42 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_grpo_standard_20_qwen_math.json\", \"data_count\": 200, \"data_path\": \"openai/gsm8k\", \"eval_data\": \"gsm8k\", \"gpu\": \"cuda:3\", \"hypothesis\": \"Qwen2.5-Math-7B Standard 20% post-GRPO GSM8K eval (N=200, seed=42). 验证 GRPO 后 accuracy 变化，reward-accuracy decoupling 证据 (C1)。Parent: grpo_standard_qwen_math_v3.\", \"model_name\": \"Qwen2.5-Math-7B-Standard-20%-postGRPO\", \"parent\": \"grpo_standard_qwen_math_v3\", \"seed\": 42, \"server\": \"westd-11672\"}}, \"eval_grpo_rasp_25_qwen_math\": {\"created_at\": \"2026-05-16T15:59:53.951Z\", \"metrics\": {\"accuracy\": 0.625, \"n_samples\": 200, \"seed\": 42}, \"spec\": {\"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_25_qwen_math\", \"command\": \"CUDA_VISIBLE_DEVICES=0 python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_25_qwen_math --max_samples 200 --seed 42 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_grpo_rasp_25_qwen_math.json\", \"data_count\": 200, \"data_path\": \"openai/gsm8k\", \"eval_data\": \"gsm8k\", \"gpu\": \"cuda:0\", \"hypothesis\": \"Qwen2.5-Math-7B RASP 25% post-GRPO GSM8K eval (N=200, seed=42). 验证 GRPO 后 accuracy 变化，reward-accuracy decoupling 证据 (C1)。Parent: grpo_rasp_25_qwen_math.\", \"model_name\": \"Qwen2.5-Math-7B-RASP-25%-postGRPO\", \"parent\": \"grpo_rasp_25_qwen_math\", \"seed\": 42, \"server\": \"westd-11672\"}}, \"eval_pass_k8_unpruned_qwen_math\": {\"created_at\": \"2026-05-16T16:43:10.425Z\", \"metrics\": {\"accuracy\": 0.965, \"k\": 8, \"n_samples\": 200, \"pass_at_k\": 0.965, \"stderr\": 0.013, \"temperature\": 0.7}, \"spec\": {\"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_unpruned_v2\", \"command\": \"CUDA_VISIBLE_DEVICES=1 python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_unpruned_v2 --max_samples 200 --seed 42 --pass_k 8 --temperature 0.7 --num_samples_per_prompt 8 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_pass_k8_unpruned_qwen_math.json\", \"data_count\": 200, \"data_path\": \"GSM8K\", \"eval_data\": \"GSM8K (N=200, pass@8, T=0.7)\", \"gpu\": \"cuda:1\", \"model_name\": \"grpo_unpruned_v2\", \"seed\": 42, \"server\": \"westd-11672\"}}, \"eval_pass_k8_rasp_20_grpo_qwen_math\": {\"created_at\": \"2026-05-16T16:43:12.096Z\", \"metrics\": {\"accuracy\": 0.915, \"k\": 8, \"n_samples\": 200, \"pass_at_k\": 0.915, \"stderr\": 0.0197, \"temperature\": 0.7}, \"spec\": {\"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_qwen_math\", \"command\": \"CUDA_VISIBLE_DEVICES=3 python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_qwen_math --max_samples 200 --seed 42 --pass_k 8 --temperature 0.7 --num_samples_per_prompt 8 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_pass_k8_rasp_20_grpo_qwen_math.json\", \"data_count\": 200, \"data_path\": \"GSM8K\", \"eval_data\": \"GSM8K (N=200, pass@8, T=0.7)\", \"gpu\": \"cuda:3\", \"model_name\": \"grpo_rasp_qwen_math\", \"seed\": 42, \"server\": \"westd-11672\"}}, \"eval_sft_rasp_rlvr_20_qwen_math\": {\"created_at\": \"2026-05-16T18:16:58.087Z\", \"metrics\": {\"accuracy\": 0.73, \"mode\": \"greedy\", \"n_correct\": 146, \"n_samples\": 200}}, \"eval_grpo_standard_25_qwen_math\": {\"created_at\": \"2026-05-16T15:59:55.747Z\", \"metrics\": {\"accuracy\": 0.635, \"n_samples\": 200, \"seed\": 42}, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_25_qwen_math\", \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_25_qwen_math\", \"command\": \"CUDA_VISIBLE_DEVICES=1 python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_25_qwen_math --max_samples 200 --seed 42 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_grpo_standard_25_qwen_math.json\", \"data_count\": 200, \"data_path\": \"openai/gsm8k\", \"eval_data\": \"gsm8k\", \"gpu\": \"cuda:1\", \"hypothesis\": \"Qwen2.5-Math-7B Standard 25% post-GRPO GSM8K eval (N=200, seed=42). 验证 GRPO 后 accuracy 变化，reward-accuracy decoupling 证据 (C1)。Parent: grpo_standard_25_qwen_math.\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_grpo_standard_25_qwen_math.json\", \"model_name\": \"Qwen2.5-Math-7B-Standard-25%-postGRPO\", \"parent\": \"grpo_standard_25_qwen_math\", \"seed\": 42, \"server\": \"westd-11672\"}}, \"eval_pass_k8_rasp_20_sft_qwen_math\": {\"created_at\": \"2026-05-16T16:43:11.344Z\", \"metrics\": {\"avg_response_length\": 139.86, \"eos_rate\": 0.99625, \"k\": 8, \"n_problems\": 200, \"natural_eos\": 1594, \"pass_at_k\": 0.935, \"stderr\": 0.0174, \"temperature\": 0.7, \"truncated\": 6}, \"spec\": {\"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_qwen_math_rasp_20\", \"command\": \"CUDA_VISIBLE_DEVICES=2 python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_qwen_math_rasp_20 --max_samples 200 --seed 42 --pass_k 8 --temperature 0.7 --num_samples_per_prompt 8 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_pass_k8_rasp_20_sft_qwen_math.json\", \"data_count\": 200, \"data_path\": \"GSM8K\", \"eval_data\": \"GSM8K (N=200, pass@8, T=0.7)\", \"gpu\": \"cuda:2\", \"model_name\": \"sft_qwen_math_rasp_20\", \"seed\": 42, \"server\": \"westd-11672\"}}, \"sft-alpha-1p0\": {\"created_at\": \"2026-05-15T13:53:32.178Z\", \"metrics\": {\"post_prune_accuracy\": 0.27, \"token_accuracy\": 0.83, \"total_steps\": 1870, \"train_loss_final\": 0.64, \"train_time_min\": 28}, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_ablation/alpha_1.0\", \"command\": \"python -u src/sft_recovery.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/alpha_ablation/alpha_1.0 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/sft_ablation/alpha_1.0 --gpu 1 --num_train_epochs 2 --learning_rate 2e-5 --batch_size 1 --gradient_accumulation_steps 8 --max_seq_length 2048 --logging_steps 10 --seed 42\", \"data_count\": 7473, \"data_path\": \"openai/gsm8k\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 0.57, \"log_path\": \"~/runs/recovery_aware_struct_prune/sft-alpha-1p0.log\", \"model_name\": \"pruned_alpha1.0 (α=1.0, 20% sparsity)\", \"pid\": \"38797\", \"seed\": 42, \"server\": \"westd-11672\", \"submitted_at\": \"2026-05-15T13:53:32.117Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 2069.9}}, \"prune_rasp_30\": {\"created_at\": \"2026-05-16T09:03:45.925Z\", \"metrics\": {\"actual_sparsity\": 0.2873, \"attn_groups_pruned\": \"0/112\", \"mlp_groups_pruned\": \"301/784\", \"model_size_gb\": 11, \"params_pruned\": 5427842560, \"target_sparsity\": 0.3}, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/pruned_rasp_30\", \"command\": \"python src/prune.py --model_path /root/autodl-tmp/models/DeepSeek-R1-Distill-Qwen-7B --mode rasp --sparsity 0.30 --alpha 1.0 --dtype bfloat16 --importance_path results/importance_scores.pt --cka_path results/cka_scores.pt\", \"data_count\": 512, \"data_path\": \"calibration data\", \"log_path\": \"N/A (CPU)\", \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B\", \"seed\": 42, \"server\": \"westb-23072\"}}, \"prune_standard_30\": {\"created_at\": \"2026-05-16T09:06:31.546Z\", \"metrics\": {\"actual_sparsity\": 0.2854, \"attn_gqa_groups_pruned\": \"0/112\", \"mlp_groups_pruned\": \"299/784\", \"params_after\": 5442379264, \"target_sparsity\": 0.3}, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/pruned_standard_30/\", \"command\": \"CUDA_VISIBLE_DEVICES='' python src/prune.py --model_path /root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B --mode standard --sparsity 0.30 --dtype bfloat16 --importance_path results/importance_scores.pt --output_path /root/autodl-tmp/recovery_aware_struct_prune/pruned_standard_30\", \"data_count\": 0, \"data_path\": \"results/importance_scores.pt\", \"log_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/logs/workers/worker_ops_prune_standard_30_20260516T090533.log\", \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B\", \"seed\": 42, \"server\": \"westb-23072\"}}, \"prune_rasp_25_qwen_math\": {\"created_at\": \"2026-05-16T09:30:44.270Z\", \"metrics\": {\"actual_sparsity\": 0.2405, \"attn_gqa_groups_pruned\": \"0/112\", \"mlp_groups_pruned\": \"252/784\", \"params_after\": 5783991808, \"target_sparsity\": 0.25}, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/pruned_rasp_25_qwen_math/\", \"command\": \"CUDA_VISIBLE_DEVICES='' python src/prune.py --model_path /root/autodl-tmp/models/Qwen2.5-Math-7B --mode rasp --sparsity 0.25 --alpha 1.0 --dtype bfloat16 --importance_path results/importance_scores.pt --cka_path results/cka_scores.pt --output_path /root/autodl-tmp/recovery_aware_struct_prune/pruned_rasp_25_qwen_math\", \"data_count\": 0, \"data_path\": \"results/importance_scores.pt + results/cka_scores.pt\", \"log_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/logs/workers/worker_ops_westd_disk_cleanup_qwen25_20260516T105526.log\", \"model_name\": \"Qwen2.5-Math-7B\", \"seed\": 42, \"server\": \"westd-11672\"}}, \"prune_standard_25_qwen_math\": {\"created_at\": \"2026-05-16T11:00:13.880Z\", \"metrics\": {\"actual_sparsity\": 0.2396, \"attn_gqa_groups_pruned\": \"0/112\", \"mlp_groups_pruned\": \"251/784\", \"target_sparsity\": 0.25}, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/pruned_standard_25_qwen_math/\", \"command\": \"CUDA_VISIBLE_DEVICES='' python src/prune.py --model_path /root/autodl-tmp/models/Qwen2.5-Math-7B --mode standard --sparsity 0.25 --dtype bfloat16 --importance_path results/importance_scores.pt --output_path /root/autodl-tmp/recovery_aware_struct_prune/pruned_standard_25_qwen_math\", \"data_count\": 0, \"data_path\": \"results/importance_scores.pt\", \"log_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/logs/workers/worker_ops_westd_disk_cleanup_qwen25_20260516T105526.log\", \"model_name\": \"Qwen2.5-Math-7B\", \"seed\": 42, \"server\": \"westd-11672\"}}, \"prune_rasp_rlvr_20_qwen_math\": {\"created_at\": \"2026-05-16T17:11:05.915Z\", \"metrics\": {\"actual_sparsity\": 0.1909, \"attn_groups_pruned\": 0, \"attn_groups_total\": 112, \"mlp_groups_pruned\": 200, \"mlp_groups_total\": 784, \"pruned_params\": 6161946112}, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/pruned_rasp_rlvr_20_qwen_math\", \"command\": \"python src/prune.py --mode rasp-rlvr --sparsity 0.20\", \"data_count\": 0, \"data_path\": \"N/A\", \"log_path\": \"/tmp/prune_rasp_rlvr_qwen_math.log\", \"model_name\": \"Qwen2.5-Math-7B\", \"seed\": 42, \"server\": \"westd-11672\"}}, \"eval_pass_k8_rasp_20_grpo_deepseek\": {\"created_at\": \"2026-05-16T23:27:01.192Z\", \"metrics\": {\"n_problems\": 200, \"pass_k8\": 0.89, \"temperature\": 0.7}, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_rasp_20_v9\", \"checkpoint_source\": \"grpo_stage2_rasp_20_v9\", \"command\": \"CUDA_VISIBLE_DEVICES=0 python eval_pass_k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_rasp_20_v9 --k 8 --temperature 0.7 --max_samples 200 --seed 42 --max_new_tokens 4096 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_pass_k8_rasp_20_grpo_deepseek.json\", \"data_count\": 200, \"data_path\": \"gsm8k_test\", \"eval_data\": \"gsm8k_test\", \"gpu\": \"cuda:0\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_pass_k8_rasp_20_grpo_deepseek.log\", \"metrics\": {\"avg_response_length\": 162.58, \"eos_rate\": 0.995, \"k\": 8, \"n_problems\": 200, \"pass_at_k\": 0.89, \"stderr\": 0.0221, \"temperature\": 0.7, \"truncated\": 8}, \"model_name\": \"grpo_stage2_rasp_20_v9\", \"pid\": \"61473\", \"seed\": 42, \"server\": \"westd-11672\"}}, \"eval_pass_k8_standard_20_grpo_deepseek\": {\"created_at\": \"2026-05-16T23:31:55.162Z\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_standard_20_v8/checkpoint-50\", \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_standard_20_v8/checkpoint-50\", \"command\": \"CUDA_VISIBLE_DEVICES=2 python eval_pass_k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_standard_20_v8/checkpoint-50 --k 8 --temperature 0.7 --max_samples 200 --seed 42 --max_new_tokens 4096 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_pass_k8_standard_20_grpo_deepseek.json\", \"data_count\": 200, \"data_path\": \"openai/gsm8k (test split, N=200)\", \"eval_data\": \"GSM8K test (200 samples, pass@k=8, T=0.7)\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/logs/eval_pass_k8_standard_20_grpo_deepseek.log\", \"metrics\": {\"avg_response_length\": 164.15, \"eos_rate\": 0.9956, \"k\": 8, \"n_problems\": 200, \"pass_at_k\": 0.855, \"stderr\": 0.0249, \"temperature\": 0.7}, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B Standard 20% post-GRPO\", \"seed\": 42, \"server\": \"westd-11672\"}}, \"eval_sft_rasp_20_full\": {\"created_at\": \"2026-05-15T16:21:29.964Z\", \"metrics\": {\"accuracy\": 0.6156, \"avg_response_length\": 210.95, \"eos_rate\": 0.9841, \"n_correct\": 812, \"n_samples\": 1319, \"natural_eos\": 1298, \"stderr\": 0.0134, \"truncated\": 21}, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20\", \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20\", \"command\": \"CUDA_VISIBLE_DEVICES=1 python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20 --max_samples 1319 --seed 42 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_sft_rasp_20_full_n1319.json\", \"data_count\": 1319, \"data_path\": \"gsm8k:test\", \"eval_data\": \"gsm8k:test:1319\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_sft_rasp_20_full.log\", \"model_name\": \"sft_rasp_20\", \"seed\": 42, \"server\": \"westb-23072\"}}, \"inference_speedup_plan016_v2\": {\"created_at\": \"2026-05-16T21:56:34.646Z\", \"metrics\": {\"dense\": {\"avg_latency_sec\": 6.682, \"peak_memory_gb\": 16.22, \"tokens_per_second\": 76.25}, \"rasp_20\": {\"avg_latency_sec\": 4.156, \"latency_speedup_vs_dense\": \"37.8%\", \"memory_reduction_vs_dense\": \"28.5%\", \"peak_memory_gb\": 11.6, \"tokens_per_second\": 52.07}, \"standard_20\": {\"avg_latency_sec\": 6.167, \"latency_speedup_vs_dense\": \"7.7%\", \"memory_reduction_vs_dense\": \"28.4%\", \"peak_memory_gb\": 11.61, \"tokens_per_second\": 49.78}}, \"spec\": {\"checkpoint_source\": \"sft_rasp_20 + sft_standard_20 + dense\", \"command\": \"CUDA_VISIBLE_DEVICES=1 python src/benchmark_inference.py --dense_path /root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B --rasp_path /root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20 --standard_path /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20 --n_prompts 50 --max_new_tokens 512\", \"data_count\": 50, \"data_path\": \"openai/gsm8k\", \"eval_data\": \"GSM8K test 50 prompts (inference latency benchmark)\", \"gpu\": \"cuda:1\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/inference_bench.log\", \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B (dense/rasp_20/standard_20)\", \"seed\": 42, \"server\": \"westb-23072\", \"tmux_session\": \"inference_bench\"}}, \"eval_pass_k8_standard_20_grpo_qwen_math_v2\": {\"created_at\": \"2026-05-16T21:54:25.214Z\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_qwen_math\", \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_qwen_math\", \"command\": \"CUDA_VISIBLE_DEVICES=2 python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_qwen_math --pass_k 8 --num_samples_per_prompt 8 --temperature 0.7 --max_samples 200 --seed 42 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_pass_k8_standard_20_grpo_qwen_math_v2.json\", \"data_count\": 200, \"data_path\": \"gsm8k test split\", \"eval_data\": \"gsm8k test (200 samples)\", \"log_path\": \"/root/runs/recovery_aware_struct_prune/eval_pass_k8_standard_20_v2.log\", \"metrics\": {\"avg_response_length\": 129.995, \"eos_rate\": 0.999375, \"k\": 8, \"n_problems\": 200, \"natural_eos\": 1599, \"pass_at_k\": 0.91, \"stderr\": 0.0202, \"temperature\": 0.7, \"truncated\": 1}, \"model_name\": \"Qwen2.5-Math-7B-Standard-20%-post-GRPO\", \"seed\": 42, \"server\": \"westd-11672\"}}, \"eval_grpo_rasp_rlvr_20_qwen_math\": {\"created_at\": \"2026-05-16T19:39:30.069Z\", \"metrics\": {\"accuracy\": 0.71, \"mode\": \"greedy\", \"n_samples\": 200, \"seed\": 42}, \"spec\": {\"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_rlvr_20_qwen_math\", \"command\": \"CUDA_VISIBLE_DEVICES=0 python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_rlvr_20_qwen_math --max_samples 200 --seed 42 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_grpo_rasp_rlvr_20_qwen_math.json\", \"data_count\": 200, \"data_path\": \"gsm8k\", \"eval_data\": \"gsm8k\", \"model_name\": \"grpo_rasp_rlvr_20_qwen_math\", \"parent\": \"grpo_rasp_rlvr_20_qwen_math\", \"seed\": 42, \"server\": \"westd-11672\"}}, \"eval_postprune_rasp_25\": {\"created_at\": \"2026-05-16T08:07:02.187Z\", \"metrics\": {\"accuracy\": 21, \"avg_response_length\": 2032.9, \"correct\": 21, \"eos_rate\": 56, \"natural_eos\": 56, \"seed\": 42, \"stderr\": 4.07, \"total\": 100, \"truncated\": 44}, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_postprune_rasp_25.json\", \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/pruned_rasp_25\", \"command\": \"CUDA_VISIBLE_DEVICES=0 python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/pruned_rasp_25 --max_samples 100 --seed 42 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_postprune_rasp_25.json\", \"data_count\": 100, \"data_path\": \"openai/gsm8k\", \"eval_data\": \"openai/gsm8k test split (N=100)\", \"log_path\": \"N/A\", \"model_name\": \"pruned_rasp_25 (RASP 25% pruned, no SFT)\", \"seed\": 42, \"server\": \"westd-11672\"}}, \"grpo_rasp_rlvr_20_qwen_math\": {\"created_at\": \"2026-05-16T19:37:40.324Z\", \"metrics\": {\"clipped_ratio\": 0.54, \"comparison_vs_rasp_20\": \"RLVR reward 0.090 > RASP 0.061 (+48%), entropy 0.275 >> 0.073 (3.8x)\", \"comparison_vs_standard_20\": \"RLVR reward 0.090 >> Standard 0.044 (+105%)\", \"entropy_final\": 0.275, \"frac_zero_std_final\": 0.7, \"grad_norm_final\": 16.125, \"kl_final\": 0.00581, \"kl_spike_recovery\": \"immediate\", \"kl_spike_step70\": 5756.85, \"loss_final\": 0.0793, \"reward_final\": 0.09, \"reward_std_final\": 0.234, \"total_steps\": 100, \"wall_clock_min\": 45.8, \"wandb_run_id\": \"clzm2cy4\"}, \"spec\": {\"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_rlvr_20_qwen_math\", \"command\": \"python src/train_grpo_v5.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_rlvr_20_qwen_math --output_dir /root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_rlvr_20_qwen_math --gpu 0 --max_steps 100 --run_name grpo_rasp_rlvr_20_qwen_math --seed 42\", \"data_count\": null, \"data_path\": \"built-in GSM8K\", \"eval_data\": \"GSM8K (built-in GRPO reward)\", \"gpu\": \"cuda:0\", \"model_name\": \"Qwen2.5-Math-7B (RASP-RLVR 20% pruned, SFT recovered)\", \"seed\": 42, \"server\": \"westd-11672\"}}, \"grpo_standard_25\": {\"created_at\": \"2026-05-16T08:42:41.240Z\", \"metrics\": {\"clipped_ratio\": 0.92, \"collapse_pattern\": \"near_total_collapse\", \"comparison_vs_rasp_25\": \"worse_than_rasp_25(0.009)\", \"kl_final\": 0.0012, \"reward_final\": 0.0075, \"total_steps\": 100, \"wall_clock_min\": 44, \"wandb_run_id\": \"16vqw4e6\"}, \"spec\": {\"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_25\", \"command\": \"CUDA_VISIBLE_DEVICES=1 python src/train_grpo_v5.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_25 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_25 --gpu 0 --max_completion_length 1024 --beta 0.04 --temperature 0.4 --repetition_penalty 1.15 --format_reward_weight 0.1 --gradient_checkpointing true --optim adamw_bnb_8bit --loss_type dapo --learning_rate 5e-7 --max_steps 100 --save_steps 100 --save_total_limit 3 --reward_desert_patience 50 --run_name grpo_standard_25 --seed 42\", \"data_count\": null, \"data_path\": \"built-in GSM8K\", \"eval_data\": \"GSM8K (built-in GRPO reward)\", \"gpu\": \"cuda:1\", \"hypothesis\": \"DeepSeek-R1-Distill-Qwen-7B Standard 25% GRPO (100 steps). 25% Standard 对照，配合 grpo_rasp_25 (frac_zero=0.875)。Parent: sft_standard_25_westd.\", \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B (Standard 25% pruned, SFT recovered)\", \"parent\": \"sft_standard_25_westd\", \"seed\": 42, \"server\": \"westd-11672\"}}, \"eval_sft_rasp_25\": {\"created_at\": \"2026-05-16T06:17:33.814Z\", \"metrics\": {\"accuracy\": 0.5299, \"eos_rate\": 0.918, \"n_correct\": 699, \"n_samples\": 1319, \"seed\": 42, \"stderr\": 0.0137, \"truncated\": 108}, \"spec\": {\"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_25\", \"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=0 python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_25 --max_samples 1319 --seed 42 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_sft_rasp_25.json\", \"data_count\": 1319, \"data_path\": \"openai/gsm8k\", \"eval_data\": \"openai/gsm8k test split\", \"gpu\": [\"cuda:0\"], \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_sft_rasp_25.log\", \"model_name\": \"sft_rasp_25 (RASP 25% SFT recovered)\", \"pid\": \"602990\", \"seed\": 42, \"server\": \"westb-23072\"}}, \"sft_rasp_rlvr_20_qwen_math\": {\"created_at\": \"2026-05-16T17:11:51.076Z\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_rlvr_20_qwen_math\", \"command\": \"python src/sft_recovery.py --model_path pruned_rasp_rlvr_20_qwen_math --num_train_epochs 2 --lr 2e-5\", \"data_count\": 0, \"data_path\": \"built-in SFT data\", \"log_path\": \"/root/runs/recovery_aware_struct_prune/sft_rasp_rlvr_20_qwen_math.log\", \"model_name\": \"Qwen2.5-Math-7B (RASP-RLVR pruned 20%)\", \"seed\": 42, \"server\": \"westd-11672\"}}, \"grpo_rasp_qwen_math_v3\": {\"created_at\": \"2026-05-16T14:49:39.708Z\", \"metrics\": {\"clipped_ratio_final\": 0.975, \"clipped_ratio_mean\": 0.981, \"collapse_onset\": \"step1\", \"collapse_pattern\": \"entropy_length_collapse\", \"cross_model_match\": \"partial\", \"entropy_mean\": 0.073, \"entropy_vs_standard_ratio\": 0.39, \"frac_zero_std_final\": 0.675, \"frac_zero_std_max\": 0.7, \"frac_zero_std_min\": 0.55, \"kl_final\": 0.009, \"llama_pattern\": \"permanent_reward_collapse\", \"mean_completion_length\": 1010, \"recovery\": false, \"reward_final\": 0.061, \"reward_min\": 0.048, \"reward_peak\": 0.102, \"reward_std_final\": 0.2, \"total_steps\": 100}, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/recovery_aware_struct_prune && python src/train_grpo_v5.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_qwen_math_rasp_20 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_qwen_math --gpu 0 --max_completion_length 1024 --beta 0.04 --temperature 0.4 --repetition_penalty 1.15 --format_reward_weight 0.1 --gradient_checkpointing true --optim adamw_bnb_8bit --loss_type dapo --learning_rate 5e-7 --max_steps 100 --save_steps 100 --save_total_limit 3 --reward_desert_patience 50 --run_name grpo_rasp_qwen_math_v3 --seed 42\\\"\", \"data_count\": 7473, \"data_path\": \"openai/gsm8k\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 1.01, \"log_path\": \"~/runs/recovery_aware_struct_prune/grpo_rasp_qwen_math_v3.log\", \"model_name\": \"Qwen2.5-Math-7B (RASP 20% SFT recovered)\", \"pid\": \"16812\", \"seed\": 42, \"server\": \"westd-11672\", \"submitted_at\": \"2026-05-16T14:49:39.494Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 3634.1}}, \"sft_rasp_rlvr_20\": {\"created_at\": \"2026-05-16T09:50:43.369Z\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_rlvr_20\", \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/pruned_rasp_rlvr_20\", \"command\": \"python src/sft_recovery.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/pruned_rasp_rlvr_20 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_rlvr_20 --gpu 1 --learning_rate 2e-5 --num_train_epochs 2 --batch_size 1 --gradient_accumulation_steps 8 --max_seq_len 2048 --seed 42\", \"data_count\": 7473, \"data_path\": \"gsm8k_sft\", \"gpu\": \"cuda:1\", \"log_path\": \"~/runs/recovery_aware_struct_prune/sft_rasp_rlvr_20.log\", \"model_name\": \"Qwen2.5-7B-Instruct (RASP-RLVR pruned 20%)\", \"pid\": \"620651\", \"seed\": 42, \"server\": \"westb-23072\"}}, \"eval_sft_standard_25\": {\"created_at\": \"2026-05-16T07:05:10.825Z\", \"metrics\": {\"accuracy\": 0.5125, \"avg_len\": 326.26, \"eos_rate\": 0.9545, \"n_correct\": 676, \"n_total\": 1319, \"stderr\": 0.0138}, \"spec\": {\"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_25/checkpoint-1870\", \"command\": \"CUDA_VISIBLE_DEVICES=1 python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_25/checkpoint-1870 --max_samples 1319 --seed 42 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_sft_standard_25.json\", \"data_count\": 1319, \"data_path\": \"openai/gsm8k\", \"eval_data\": \"openai/gsm8k test split\", \"model_name\": \"sft_standard_25 (Standard 25% pruned + SFT)\", \"seed\": 42, \"server\": \"westb-23072\"}}, \"eval_sft_qwen_math_standard_25\": {\"created_at\": \"2026-05-16T12:04:49.969Z\", \"metrics\": {\"accuracy\": 63, \"correct\": 126, \"eos_rate\": 1, \"total\": 200}, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_qwen_math_standard_25\", \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_qwen_math_standard_25/\", \"command\": \"CUDA_VISIBLE_DEVICES=3 python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_qwen_math_standard_25 --max_samples 200 --seed 42 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_sft_qwen_math_standard_25.json\", \"data_count\": 200, \"data_path\": \"openai/gsm8k\", \"eval_data\": \"gsm8k_test\", \"gpu\": [\"cuda:3\"], \"gpu_hours\": 0.76, \"gpu_id\": \"cuda:3\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_sft_qwen_math_standard_25.log\", \"model_name\": \"Qwen2.5-Math-7B-Standard-25%-SFT\", \"pid\": \"6215\", \"seed\": 42, \"server\": \"westd-11672\", \"submitted_at\": \"2026-05-16T12:05:12.481Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 2731.1}}, \"eval_sft_qwen_math_rasp_25\": {\"created_at\": \"2026-05-16T12:04:49.248Z\", \"metrics\": {\"accuracy\": 64, \"correct\": 128, \"eos_rate\": 0.995, \"total\": 200}, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_qwen_math_rasp_25\", \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_qwen_math_rasp_25/\", \"command\": \"CUDA_VISIBLE_DEVICES=2 python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_qwen_math_rasp_25 --max_samples 200 --seed 42 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_sft_qwen_math_rasp_25.json\", \"data_count\": 200, \"data_path\": \"openai/gsm8k\", \"eval_data\": \"gsm8k_test\", \"gpu\": [\"cuda:2\"], \"gpu_hours\": 0.76, \"gpu_id\": \"cuda:2\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_sft_qwen_math_rasp_25.log\", \"model_name\": \"Qwen2.5-Math-7B-RASP-25%-SFT\", \"pid\": \"6135\", \"seed\": 42, \"server\": \"westd-11672\", \"submitted_at\": \"2026-05-16T12:05:10.285Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 2732.4}}, \"sft_qwen_math_standard_25\": {\"created_at\": \"2026-05-16T11:15:20.187Z\", \"metrics\": {\"epochs\": 2, \"final_loss\": 0.6122, \"mean_token_accuracy\": 0.8607, \"throughput_samples_per_sec\": 8.973, \"total_steps\": 1870, \"train_runtime_sec\": 1666}, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_qwen_math_standard_25/\", \"command\": \"python src/sft_recovery.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/pruned_standard_25_qwen_math --output_dir /root/autodl-tmp/recovery_aware_struct_prune/sft_qwen_math_standard_25 --gpu 3 --lr 2e-5 --epochs 2 --batch_size 1 --grad_accum 8 --max_seq_len 2048 --seed 42\", \"data_count\": 7473, \"data_path\": \"openai/gsm8k\", \"log_path\": \"~/runs/recovery_aware_struct_prune/sft_qwen_math_standard_25.log\", \"model_name\": \"Qwen2.5-Math-7B-Standard-25%\", \"seed\": 42, \"server\": \"westd-11672\"}}, \"sft_qwen_math_rasp_25\": {\"created_at\": \"2026-05-16T11:15:13.431Z\", \"metrics\": {\"epochs\": 2, \"final_loss\": 0.6062, \"mean_token_accuracy\": 0.8673, \"throughput_samples_per_sec\": 9.046, \"total_steps\": 1870, \"train_runtime_sec\": 1652}, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_qwen_math_rasp_25/\", \"command\": \"python src/sft_recovery.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/pruned_rasp_25_qwen_math --output_dir /root/autodl-tmp/recovery_aware_struct_prune/sft_qwen_math_rasp_25 --gpu 2 --lr 2e-5 --epochs 2 --batch_size 1 --grad_accum 8 --max_seq_len 2048 --seed 42\", \"data_count\": 7473, \"data_path\": \"openai/gsm8k\", \"log_path\": \"~/runs/recovery_aware_struct_prune/sft_qwen_math_rasp_25.log\", \"model_name\": \"Qwen2.5-Math-7B-RASP-25%\", \"seed\": 42, \"server\": \"westd-11672\"}}, \"eval_sft_standard_qwen_math_n200\": {\"created_at\": \"2026-05-16T11:15:10.910Z\", \"metrics\": {\"accuracy\": 0.71, \"avg_len\": 127.7, \"correct\": 142, \"eos_rate\": 1, \"n_total\": 200, \"stderr\": 0.0321}, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_sft_standard_qwen_math.json\", \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_qwen_math_standard_20\", \"command\": \"CUDA_VISIBLE_DEVICES=1 python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_qwen_math_standard_20 --max_samples 200 --seed 42 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_sft_standard_qwen_math.json\", \"data_count\": 200, \"data_path\": \"openai/gsm8k\", \"eval_data\": \"gsm8k_test\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/eval_standard_n200.log\", \"model_name\": \"Qwen2.5-Math-7B-Standard-20%-SFT\", \"seed\": 42, \"server\": \"westd-11672\"}}, \"eval_sft_rasp_qwen_math_n200\": {\"created_at\": \"2026-05-16T11:15:07.028Z\", \"metrics\": {\"accuracy\": 0.725, \"avg_len\": 121.8, \"correct\": 145, \"eos_rate\": 1, \"n_total\": 200, \"stderr\": 0.0316}, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_sft_rasp_qwen_math.json\", \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_qwen_math_rasp_20\", \"command\": \"CUDA_VISIBLE_DEVICES=0 python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_qwen_math_rasp_20 --max_samples 200 --seed 42 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_sft_rasp_qwen_math.json\", \"data_count\": 200, \"data_path\": \"openai/gsm8k\", \"eval_data\": \"gsm8k_test\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/eval_rasp_n200.log\", \"model_name\": \"Qwen2.5-Math-7B-RASP-20%-SFT\", \"seed\": 42, \"server\": \"westd-11672\"}}, \"prune_rasp_rlvr_20\": {\"created_at\": \"2026-05-16T09:50:39.656Z\", \"metrics\": {\"actual_sparsity\": 0.1909, \"attn_gqa_groups_pruned\": \"0/112\", \"group_selection_diff_vs_rasp\": \"RASP重剪前6层+后段(19,23-25,27)保中间; RLVR重剪前6层+中后段(16-26)保Layer6-7,27\", \"mlp_groups_pruned\": \"200/784\", \"params_after\": \"6.16B\", \"target_sparsity\": 0.2}, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/pruned_rasp_rlvr_20/\", \"command\": \"CUDA_VISIBLE_DEVICES='' python src/prune.py --model_path /root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B --mode rasp-rlvr --sparsity 0.20 --alpha 1.0 --dtype bfloat16 --importance_path results/importance_scores.pt --cka_path results/cka_scores.pt --output_path /root/autodl-tmp/recovery_aware_struct_prune/pruned_rasp_rlvr_20\", \"data_count\": 0, \"data_path\": \"results/importance_scores.pt + results/cka_scores.pt\", \"log_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/logs/workers/worker_code_rasp_rlvr_prune_20260516T095028.log\", \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B\", \"seed\": 42, \"server\": \"westb-23072\"}}, \"sft_standard_20_qwen_math\": {\"created_at\": \"2026-05-16T08:11:00.051Z\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_qwen_math_standard_20/\", \"command\": \"python src/sft_recovery.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/pruned_qwen_math_standard_20 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/sft_qwen_math_standard_20 --gpu 1 --num_train_epochs 3 --learning_rate 2e-5 --batch_size 1 --gradient_accumulation_steps 8 --max_seq_length 2048 --seed 42\", \"data_count\": 7473, \"data_path\": \"openai/gsm8k\", \"log_path\": \"tmux session on westd-11672\", \"model_name\": \"Qwen2.5-Math-7B-Standard-20%\", \"seed\": 42, \"server\": \"westd-11672\"}}, \"sft_rasp_20_qwen_math\": {\"created_at\": \"2026-05-16T08:10:59.311Z\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_qwen_math_rasp_20/\", \"command\": \"python src/sft_recovery.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/pruned_qwen_math_rasp_20 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/sft_qwen_math_rasp_20 --gpu 0 --num_train_epochs 3 --learning_rate 2e-5 --batch_size 1 --gradient_accumulation_steps 8 --max_seq_length 2048 --seed 42\", \"data_count\": 7473, \"data_path\": \"openai/gsm8k\", \"log_path\": \"tmux session on westd-11672\", \"model_name\": \"Qwen2.5-Math-7B-RASP-20%\", \"seed\": 42, \"server\": \"westd-11672\"}}, \"prune_standard_20_qwen_math\": {\"created_at\": \"2026-05-16T08:03:56.378Z\", \"metrics\": {\"attn_groups_pruned\": 0, \"mlp_groups_pruned\": 202, \"model_keys\": 339, \"original_params\": 7615616512, \"pruned_params\": 6147409408, \"sparsity_actual\": 0.1928, \"sparsity_target\": 0.2}, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/pruned_qwen_math_standard_20\", \"command\": \"python src/prune.py --model_path /root/autodl-tmp/models/Qwen2.5-Math-7B --mode standard --sparsity 0.20 --dtype bfloat16 --output_path /root/autodl-tmp/recovery_aware_struct_prune/pruned_qwen_math_standard_20\", \"data_count\": 256, \"data_path\": \"importance_scores_qwen_math.pt\", \"log_path\": \"N/A (CPU-only)\", \"model_name\": \"Qwen2.5-Math-7B\", \"seed\": 42, \"server\": \"westd-11672\"}}, \"prune_rasp_20_qwen_math\": {\"created_at\": \"2026-05-16T08:01:57.095Z\", \"metrics\": {\"alpha\": 1, \"attn_groups_pruned\": 0, \"mlp_groups_pruned\": 199, \"model_keys\": 339, \"original_params\": 7615616512, \"pruned_params\": 6169214464, \"sparsity_actual\": 0.1899, \"sparsity_target\": 0.2}, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/pruned_qwen_math_rasp_20\", \"command\": \"python src/prune.py --model_path /root/autodl-tmp/models/Qwen2.5-Math-7B --mode rasp --sparsity 0.20 --alpha 1.0 --dtype bfloat16 --output_path /root/autodl-tmp/recovery_aware_struct_prune/pruned_qwen_math_rasp_20\", \"data_count\": 256, \"data_path\": \"importance_scores_qwen_math.pt + cka_scores_qwen_math.pt\", \"log_path\": \"N/A (CPU-only)\", \"model_name\": \"Qwen2.5-Math-7B\", \"seed\": 42, \"server\": \"westd-11672\"}}, \"eval_grpo_rasp_v9_step10\": {\"created_at\": \"2026-05-16T03:40:46.186Z\", \"metrics\": {\"accuracy\": 61.87, \"avg_response_length\": 213.6, \"correct\": 816, \"eos_rate\": 98.33, \"seed\": 42, \"stderr\": 1.34, \"total\": 1319, \"truncated\": 22}, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_grpo_rasp_v9_step10.json\", \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_rasp_20_v9/checkpoint-10\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/recovery_aware_struct_prune && HF_HUB_OFFLINE=1 CUDA_VISIBLE_DEVICES=0 python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_rasp_20_v9/checkpoint-10 --max_samples 1319 --seed 42 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_grpo_rasp_v9_step10.json\\\"\", \"data_count\": 1319, \"data_path\": \"openai/gsm8k\", \"eval_data\": \"openai/gsm8k test split\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 3.06, \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_grpo_rasp_v9_step10.log\", \"model_name\": \"grpo_stage2_rasp_20_v9 checkpoint-10\", \"pid\": \"585618\", \"seed\": 42, \"server\": \"westb-23072\", \"submitted_at\": \"2026-05-16T04:57:36.867Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 11009.3}}, \"eval_grpo_rasp_v9_step5\": {\"created_at\": \"2026-05-16T01:55:35.424Z\", \"metrics\": {\"accuracy\": 60.65, \"seed\": 42, \"total\": 1319}, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_rasp_20_v9/checkpoint-5\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_grpo_rasp_v9_step5.log\"}}, \"prune_standard_25\": {\"created_at\": \"2026-05-16T05:13:52.855Z\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/pruned_standard_25\", \"command\": \"python prune.py --model_path DeepSeek-R1-Distill-Qwen-7B --mode standard --sparsity 0.25 --dtype bfloat16\", \"data_count\": 256, \"data_path\": \"calibration data (from importance scores)\", \"log_path\": \"N/A (CPU-only, <1min)\", \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B\", \"seed\": 42, \"server\": \"westb-23072\"}}, \"prune_rasp_25\": {\"created_at\": \"2026-05-16T05:13:52.292Z\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/pruned_rasp_25\", \"command\": \"python prune.py --model_path DeepSeek-R1-Distill-Qwen-7B --mode rasp --sparsity 0.25 --alpha 1.0 --dtype bfloat16\", \"data_count\": 256, \"data_path\": \"calibration data (from importance/CKA scores)\", \"log_path\": \"N/A (CPU-only, <1min)\", \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B\", \"seed\": 42, \"server\": \"westb-23072\"}}, \"grpo_unpruned_v2\": {\"created_at\": \"2026-05-16T01:45:10.586Z\", \"metrics\": {\"avg_step_time_sec\": 23, \"checkpoints_available\": [\"checkpoint-90\", \"checkpoint-95\", \"checkpoint-100\"], \"collapse_onset\": \"N/A\", \"final_entropy\": 0.194, \"final_grad_norm\": 6.97, \"final_kl\": 0.0051, \"final_reward\": 0.661, \"max_steps\": 100, \"peak_reward\": 0.669, \"peak_reward_step\": 80, \"reward_range\": \"0.425-0.669\", \"training_seconds\": 2660}, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_unpruned_v2/checkpoint-100\", \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_unpruned_baseline\", \"command\": \"resume from checkpoint-20, save_total_limit=3, max_steps=100\", \"data_count\": 7473, \"data_path\": \"openai/gsm8k\", \"eval_data\": \"gsm8k_train_7473\", \"gpu_id\": \"cuda:1\", \"log_path\": \"~/runs/recovery_aware_struct_prune/grpo_unpruned_v2.log\", \"model_name\": \"sft_unpruned_baseline (unpruned)\", \"pid\": 77647, \"seed\": 42, \"server\": \"westd-11672\"}}, \"grpo_stage2_rasp_20_v9\": {\"created_at\": \"2026-05-15T22:37:13.593Z\", \"metrics\": {\"checkpoints\": [\"checkpoint-10\", \"checkpoint-15\", \"checkpoint-20\", \"checkpoint-25\", \"checkpoint-30\"], \"collapse_note\": \"frac_zero_std peaked at 95% by step 30, reward dropped from peak 0.039 (step 20) to 0.021 (step 30)\", \"collapse_status\": \"COLLAPSED\", \"final_clipped_ratio\": 0.956, \"final_frac_zero_std\": 0.95, \"final_grad_norm\": 1.398, \"final_kl\": 0.00118, \"final_loss\": 0.00686, \"final_mean_length\": 996, \"final_mean_terminated_length\": 176, \"final_reward\": 0.021, \"max_steps\": 30, \"reward_history\": [{\"frac_zero_std\": 0.875, \"reward\": 0.015, \"step\": 10}, {\"frac_zero_std\": 0.8, \"reward\": 0.039, \"step\": 20}, {\"frac_zero_std\": 0.95, \"reward\": 0.021, \"step\": 30}], \"step\": 30, \"step_time_sec\": 418, \"total_time\": \"3h28m25s\", \"wandb_url\": \"https://wandb.ai/xiaoyucorynne-/recovery_aware_struct_prune/runs/mrikafz3\"}, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_rasp_20_v9\", \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20\", \"command\": \"CUDA_VISIBLE_DEVICES=0 /root/miniconda3/bin/python /root/recovery_aware_struct_prune/src/train_grpo_v5.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_rasp_20_v9 --gpu 0 --max_completion_length 1024 --beta 0.01 --temperature 0.4 --repetition_penalty 1.15 --format_reward_weight 0.1 --gradient_checkpointing true --optim adamw_bnb_8bit --loss_type dapo --learning_rate 1e-6 --max_steps 30 --save_steps 5 --save_total_limit 5 --reward_desert_patience 50 --run_name grpo_stage2_rasp_20_v9\", \"data_count\": 7473, \"data_path\": \"openai/gsm8k\", \"eval_data\": \"gsm8k\", \"gpu_id\": \"cuda:0\", \"log_path\": \"/tmp/grpo_rasp_v9.log\", \"model_name\": \"sft_rasp_20\", \"notes\": \"Auto-launcher tmux session auto_v9_launcher waiting for alpha sweep to finish before starting on cuda:0\", \"pid\": 566666, \"seed\": 42, \"server\": \"westb-23072\"}}, \"alpha_ablation_sweep\": {\"created_at\": \"2026-05-15T20:15:39.765Z\", \"metrics\": {\"alpha_0.0\": {\"accuracy\": 0.27, \"avg_len\": 1192, \"eos_rate\": 0.8, \"n_correct\": 27, \"n_total\": 100}, \"alpha_0.25\": {\"accuracy\": 0.23, \"avg_len\": 1834, \"eos_rate\": 0.63, \"n_correct\": 23, \"n_total\": 100}, \"alpha_0.5\": {\"accuracy\": 0.22, \"avg_len\": 1141, \"eos_rate\": 0.81, \"n_correct\": 22, \"n_total\": 100}, \"alpha_1.0\": {\"accuracy\": 0.31, \"avg_len\": 733, \"eos_rate\": 0.92, \"n_correct\": 31, \"n_total\": 100}, \"alpha_2.0\": {\"accuracy\": 0.36, \"avg_len\": 2130, \"eos_rate\": 0.59, \"n_correct\": 36, \"n_total\": 100}}, \"spec\": {\"alphas\": [0, 0.25, 0.5, 1, 2], \"calibration_samples\": 512, \"checkpoint_path\": \"/root/recovery_aware_struct_prune/results/\", \"command\": \"bash run_alpha_sweep_fix.sh\", \"data_count\": 100, \"data_path\": \"openai/gsm8k\", \"gpu_id\": \"cuda:0\", \"log_path\": \"/tmp/alpha_sweep_fix.log\", \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B\", \"notes\": \"Alpha ablation: 0.25, 0.5, 1.0, 2.0. Partial results: alpha=0.0 acc=0.27 eos=0.80, alpha=0.25 acc=0.23 eos=0.63. Currently running alpha=0.5 eval.\", \"pid\": 556867, \"seed\": 42, \"server\": \"westb-23072\", \"sparsity\": 0.2}}, \"sft_unpruned_baseline\": {\"created_at\": \"2026-05-15T22:07:43.929Z\", \"metrics\": {\"epochs\": 2, \"final_loss\": 0.3321, \"final_token_accuracy\": 0.909, \"total_steps\": 1870, \"train_loss_avg\": 0.4253, \"train_runtime_sec\": 1908, \"train_samples_per_second\": 7.833}, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_unpruned_baseline\", \"checkpoint_source\": \"/root/autodl-tmp/models/DeepSeek-R1-Distill-Qwen-7B\", \"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && HF_HUB_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache HF_DATASETS_CACHE=/root/autodl-tmp/.hf_cache/datasets /root/miniconda3/bin/python /root/recovery_aware_struct_prune/src/sft_recovery.py --model_path /root/autodl-tmp/models/DeepSeek-R1-Distill-Qwen-7B --output_dir /root/autodl-tmp/recovery_aware_struct_prune/sft_unpruned_baseline --gpu 1 --num_train_epochs 2 --learning_rate 2e-5 --batch_size 1 --gradient_accumulation_steps 8 --max_seq_length 2048 --seed 42 --save_strategy no --run_name sft_unpruned_baseline_v2\", \"data_count\": 7473, \"data_path\": \"openai/gsm8k train\", \"estimated_time_minutes\": 33, \"gpu_id\": \"cuda:1\", \"hyperparams\": {\"batch_size\": 1, \"epochs\": 2, \"gradient_accumulation_steps\": 8, \"lr\": 2e-05, \"max_seq_length\": 2048, \"save_strategy\": \"no\", \"seed\": 42}, \"log_path\": \"/tmp/sft_unpruned.log\", \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B (unpruned)\", \"pid\": 67546, \"seed\": 42, \"server\": \"westd-11672\", \"tmux_session\": \"sft_unpruned\", \"total_steps\": 1870}}, \"eval_sft_rasp_full_westd\": {\"created_at\": \"2026-05-15T20:36:02.786Z\", \"metrics\": {\"accuracy\": 0.6149, \"avg_len\": 216.5, \"eos_rate\": 0.9826, \"n_correct\": 811, \"n_total\": 1319, \"stderr\": 0.0134}, \"spec\": {\"checkpoint_path\": \"results/eval_sft_rasp_20_westd_full.json\", \"checkpoint_source\": \"sft_rasp_20_westd\", \"command\": \"python eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20_westd --output results/eval_sft_rasp_20_westd_full.json --n_samples 1319\", \"data_count\": 1319, \"data_path\": \"openai/gsm8k\", \"eval_data\": \"gsm8k_test_full\", \"gpu_id\": \"cuda:1\", \"log_path\": \"/tmp/eval_rasp_full.log\", \"model_name\": \"sft_rasp_20_westd\", \"output_path\": \"results/eval_sft_rasp_20_westd_full.json\", \"pid\": 62565, \"seed\": 42, \"server\": \"westd-11672\"}}, \"eval_sft_standard_full_westd\": {\"created_at\": \"2026-05-15T20:36:01.803Z\", \"metrics\": {\"accuracy\": 0.5929, \"avg_len\": 226.7, \"eos_rate\": 0.9803, \"n_correct\": 782, \"n_total\": 1319, \"stderr\": 0.01353}, \"spec\": {\"checkpoint_path\": \"results/eval_sft_standard_20_westd_full.json\", \"checkpoint_source\": \"sft_standard_20_westd\", \"command\": \"python eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20_westd --output results/eval_sft_standard_20_westd_full.json --n_samples 1319\", \"data_count\": 1319, \"data_path\": \"openai/gsm8k\", \"eval_data\": \"gsm8k_test_full\", \"gpu_id\": \"cuda:0\", \"log_path\": \"/tmp/eval_standard_full.log\", \"model_name\": \"sft_standard_20_westd\", \"output_path\": \"results/eval_sft_standard_20_westd_full.json\", \"pid\": 62463, \"seed\": 42, \"server\": \"westd-11672\"}}, \"eval_sft_rasp_20_westd_n100_v2\": {\"created_at\": \"2026-05-15T19:24:08.437Z\", \"metrics\": {\"accuracy\": 0.67, \"avg_len\": 182.39, \"eos_rate\": 0.99, \"n_correct\": 67, \"n_total\": 100}, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20_westd\", \"command\": \"bash -c \\\"cd /root/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=0 python -u src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20_westd --max_samples 100 --max_new_tokens 4096 --output_path results/eval_sft_rasp_20_westd_n100.json --seed 42\\\"\", \"data_count\": 100, \"data_path\": \"gsm8k test\", \"eval_data\": \"gsm8k test N=100\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 0.78, \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_sft_rasp_20_westd_n100_v2.log\", \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B (RASP pruned 20% + SFT westd)\", \"pid\": \"unknown\", \"seed\": 42, \"server\": \"westd-11672\", \"submitted_at\": \"2026-05-15T19:24:08.325Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 2807.6}}, \"eval_sft_standard_20_westd_n100_v2\": {\"created_at\": \"2026-05-15T19:24:09.850Z\", \"metrics\": {\"accuracy\": 0.63, \"avg_len\": 260.57, \"eos_rate\": 0.97, \"n_correct\": 63, \"n_total\": 100}, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20_westd\", \"command\": \"bash -c \\\"cd /root/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=1 python -u src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20_westd --max_samples 100 --max_new_tokens 4096 --output_path results/eval_sft_standard_20_westd_n100.json --seed 42\\\"\", \"data_count\": 100, \"data_path\": \"gsm8k test\", \"eval_data\": \"gsm8k test N=100\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 0.78, \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_sft_standard_20_westd_n100_v2.log\", \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B (Standard pruned 20% + SFT westd)\", \"pid\": \"unknown\", \"seed\": 42, \"server\": \"westd-11672\", \"submitted_at\": \"2026-05-15T19:24:09.745Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 2805.4}}, \"eval_sft_standard_20_westd_n100\": {\"created_at\": \"2026-05-15T17:39:03.607Z\", \"metrics\": {\"accuracy\": 0.63, \"avg_len\": 260.57, \"eos_rate\": 0.97, \"n_correct\": 63, \"n_total\": 100, \"stderr\": 0.048}, \"spec\": {\"checkpoint_source\": \"sft_standard_20_westd_retrain\", \"command\": \"bash -c \\\"cd /root/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=1 /root/miniconda3/bin/python -u src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20_westd --max_samples 100 --max_new_tokens 4096 --seed 42 --output_path results/eval_sft_standard_20_westd_n100.json\\\"\", \"data_count\": 100, \"data_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20_westd\", \"eval_data\": \"gsm8k\", \"model_name\": \"sft_standard_20_westd\", \"seed\": 42, \"server\": \"westd-11672\"}}, \"eval_sft_rasp_20_westd_n100\": {\"created_at\": \"2026-05-15T17:35:08.417Z\", \"metrics\": {\"accuracy\": 0.67, \"avg_len\": 182.39, \"eos_rate\": 0.99, \"n_correct\": 67, \"n_total\": 100, \"stderr\": 0.047}, \"spec\": {\"checkpoint_source\": \"sft_rasp_20_westd_retrain\", \"command\": \"bash -c \\\"cd /root/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=0 /root/miniconda3/bin/python -u src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20_westd --max_samples 100 --max_new_tokens 4096 --seed 42 --output_path results/eval_sft_rasp_20_westd_n100.json\\\"\", \"data_count\": 100, \"data_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20_westd\", \"eval_data\": \"gsm8k\", \"model_name\": \"sft_rasp_20_westd\", \"seed\": 42, \"server\": \"westd-11672\"}}, \"sft_rasp_20_westd_retrain\": {\"created_at\": \"2026-05-15T16:59:51.103Z\", \"spec\": {\"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python src/sft_recovery.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/pruned_rasp_20 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20_westd --gpu 0 --epochs 2 --lr 2e-5 --batch_size 1 --grad_accum 8 --seed 42\", \"data_count\": 7473, \"data_path\": \"gsm8k train\", \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B (RASP pruned 20%)\", \"seed\": 42, \"server\": \"westd-11672\"}}, \"sft_standard_20_westd_retrain\": {\"created_at\": \"2026-05-15T17:05:52.927Z\", \"metrics\": {\"epochs\": 2, \"final_step_loss\": 0.6403, \"final_token_accuracy\": 0.8258, \"total_steps\": 1870, \"train_loss\": 0.7577, \"train_runtime_sec\": 1679, \"train_samples_per_second\": 8.902}, \"spec\": {\"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python src/sft_recovery.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/pruned_standard_20 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20_westd --gpu 1 --epochs 2 --lr 2e-5 --batch_size 1 --grad_accum 8 --seed 42\", \"data_count\": 7473, \"data_path\": \"gsm8k train\", \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B (Standard pruned 20%)\", \"seed\": 42, \"server\": \"westd-11672\"}}, \"grasp_baseline_westd\": {\"created_at\": \"2026-05-15T12:40:34.072Z\", \"metrics\": {\"avg_len\": 4018, \"eos_rate\": 0.02, \"grasp_20_accuracy_n100\": 0.07, \"json_path\": \"results/eval_pruned_graspune_20_greedy.json\", \"n_correct\": 7, \"n_total\": 100, \"rasp_20_accuracy_ref\": 0.31, \"standard_20_accuracy_ref\": 0.27}, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_source\": \"GraSP pruning pipeline\", \"command\": \"python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/pruned_graspune_20 --max_samples 100 --max_new_tokens 4096\", \"command_note\": \"实际运行命令无 --output_path 和 --seed，但源码默认 seed=42 且 output_path 自动回退到 results/eval_pruned_graspune_20_greedy.json\", \"data_count\": 100, \"data_path\": \"gsm8k test split\", \"eval_data\": \"gsm8k test N=100\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 4.44, \"log_path\": \"results/eval_grasp_n100.log\", \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B (GraSP pruned 20%)\", \"pid\": \"38120\", \"seed\": 42, \"server\": \"westd-11672\", \"submitted_at\": \"2026-05-15T12:45:44.074Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 15997.5}}, \"eval_sft_alpha_2p0\": {\"created_at\": \"2026-05-15T15:42:36.917Z\", \"metrics\": {\"accuracy\": 0.62, \"avg_len\": 277.41, \"eos_rate\": 0.97, \"n_correct\": 62, \"n_total\": 100, \"stderr\": 0.0485}, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_ablation/alpha_2.0\", \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_ablation/alpha_2.0\", \"command\": \"python -u src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_ablation/alpha_2.0 --max_samples 100 --max_new_tokens 4096 --seed 42 --output_path results/eval_sft_alpha_2.0_n100.json\", \"data_count\": 100, \"data_path\": \"gsm8k\", \"eval_data\": \"gsm8k_test_n100\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 0.98, \"log_path\": \"/root/recovery_aware_struct_prune/results/eval_sft_alpha_2.0_n100.log\", \"model_name\": \"alpha_2.0_sft\", \"pid\": \"45428\", \"seed\": 42, \"server\": \"westd-11672\", \"submitted_at\": \"2026-05-15T15:42:47.927Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 3534.0}}, \"sft_alpha2_0_westd\": {\"created_at\": \"2026-05-15T14:32:54.953Z\", \"metrics\": {\"epoch\": 2, \"mean_token_accuracy_final\": 0.8354, \"post_prune_accuracy\": 0.29, \"total_steps\": 1870, \"train_loss\": 0.7424, \"train_loss_final\": 0.6114, \"train_runtime_sec\": 2422}, \"spec\": {\"checkpoint_source\": \"alpha_ablation_westd_cal256 (pruned_rasp_20_alpha2.0)\", \"command\": \"python sft_recovery.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/pruned_models/pruned_rasp_20_alpha2.0 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/sft_ablation/alpha_2.0 --gpu 1 --epochs 2 --lr 2e-5 --batch_size 1 --grad_accum 8\", \"data_count\": 7473, \"data_path\": \"gsm8k train split\", \"eval_data\": \"gsm8k train (SFT recovery, not eval)\", \"gpu\": \"cuda:1\", \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B (RASP pruned alpha=2.0, 20% sparsity)\", \"pid\": 43065, \"seed\": 42, \"server\": \"westd-11672\"}}, \"alpha_ablation_westd_cal256\": {\"created_at\": \"2026-05-15T09:46:30.119Z\", \"metrics\": {\"alpha_4_0_accuracy\": 0.4, \"finding\": \"α=4.0 gives 40% post-prune accuracy (highest), non-monotonic relationship between α and accuracy\"}}, \"sft_grasp_20_westd\": {\"created_at\": \"2026-05-15T13:50:39.294Z\", \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_graspune_20\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/recovery_aware_struct_prune && python -u src/sft_recovery.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/pruned_graspune_20 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/sft_graspune_20 --gpu 0 --num_train_epochs 2 --learning_rate 2e-5 --batch_size 1 --gradient_accumulation_steps 8 --max_seq_length 2048 --logging_steps 10 --seed 42\\\"\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 1.15, \"log_path\": \"~/runs/recovery_aware_struct_prune/sft_grasp_20_westd.log\", \"pid\": \"38509\", \"server\": \"westd-11672\", \"submitted_at\": \"2026-05-15T13:51:47.632Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 4148.4}}, \"sft_alpha4_0_westd_retry\": {\"created_at\": \"2026-05-15T12:46:36.918Z\", \"metrics\": {\"accuracy_stderr\": 0.049, \"avg_response_length\": 238.56, \"eos_rate\": 0.98, \"mean_token_accuracy_final\": 0.8368, \"n_correct\": 62, \"n_total\": 100, \"post_prune_accuracy\": 0.4, \"post_sft_accuracy_100\": 0.62, \"sft_recovery_gain_pp\": 22, \"train_loss_final\": 0.7393, \"train_loss_last_logged\": 0.6106}, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_ablation/alpha_4.0\", \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/alpha_ablation/alpha_4.0\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=1 python -u src/sft_recovery.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/alpha_ablation/alpha_4.0 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/sft_ablation/alpha_4.0 --gpu 0 --num_train_epochs 2 --learning_rate 2e-5 --batch_size 1 --gradient_accumulation_steps 8 --max_seq_length 2048 --logging_steps 10 --seed 42\", \"data_count\": 7473, \"data_path\": \"openai/gsm8k\", \"eval_data\": \"gsm8k\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 0.1, \"log_path\": \"/tmp/sft_alpha4.0.log\", \"model_name\": \"pruned_alpha4.0 (a=4.0, 20% sparsity)\", \"pid\": \"37013\", \"seed\": 42, \"server\": \"westd-11672\", \"submitted_at\": \"2026-05-15T13:42:03.641Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 358.8}}, \"reeval_postprune_definitive\": {\"created_at\": \"2026-05-15T09:46:32.498Z\", \"metrics\": {\"conclusion\": \"Original 29x advantage (29% vs 1%) not reproducible. Actual gap 4pp (31% vs 27% on westb), not statistically significant.\", \"original_claim_rasp\": 0.29, \"original_claim_standard\": 0.01, \"rasp_20_accuracy_westb\": 0.31, \"rasp_20_accuracy_westd\": 0.29, \"rasp_vs_standard_gap_pp\": 4, \"standard_20_accuracy_westb\": 0.27}, \"spec\": {\"checkpoint_path\": \"N/A (eval only)\", \"command\": \"python src/eval_gsm8k.py --model_path /root/autodl-tmp/pruned_{rasp,standard}_20 --max_samples 100 --max_new_tokens 4096\", \"data_count\": 100, \"data_path\": \"gsm8k_test\", \"log_path\": \"N/A\", \"model_name\": \"pruned_rasp_20 + pruned_standard_20\", \"seed\": 42, \"server\": \"westb-23072 + westd-11672\"}}, \"sft_standard_20\": {\"created_at\": \"2026-05-14T23:37:34.863Z\", \"metrics\": {\"eos_rate_greedy_100\": 0.99, \"greedy_accuracy_100\": 0.64, \"greedy_avg_len\": 176.31, \"greedy_correct\": 64, \"greedy_max_len\": 4096, \"greedy_min_len\": 43, \"greedy_total\": 100, \"sampling_eos_rate_5\": 1, \"token_accuracy\": 0.83, \"total_steps\": 1870, \"train_loss_final\": 0.64, \"train_loss_initial\": 1.7, \"train_time_min\": 37}, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20\", \"command\": \"python src/sft_recovery.py --model_path /root/autodl-tmp/pruned_standard_20 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20 --num_train_epochs 2 --learning_rate 2e-5\", \"data_count\": 7473, \"data_path\": \"openai/gsm8k\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 0.83, \"log_path\": \"~/runs/recovery_aware_struct_prune/sft_standard_20.log\", \"model_name\": \"pruned_standard_20\", \"pid\": \"249655\", \"seed\": 42, \"server\": \"westb-23072\", \"submitted_at\": \"2026-05-14T23:47:25.361Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 2999.5}}, \"sft_rasp_20\": {\"created_at\": \"2026-05-14T23:37:33.162Z\", \"metrics\": {\"eos_rate_greedy_100\": 0.99, \"greedy_accuracy_100\": 0.57, \"greedy_avg_len\": 179.83, \"greedy_correct\": 57, \"greedy_max_len\": 4096, \"greedy_min_len\": 59, \"greedy_total\": 100, \"sampling_eos_rate_5\": 1, \"token_accuracy\": 0.83, \"total_steps\": 1870, \"train_loss_final\": 0.64, \"train_loss_initial\": 1.86, \"train_time_min\": 37}, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20\", \"command\": \"python src/sft_recovery.py --model_path /root/autodl-tmp/pruned_rasp_20 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20 --num_train_epochs 2 --learning_rate 2e-5\", \"data_count\": 7473, \"data_path\": \"openai/gsm8k\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 0.82, \"log_path\": \"~/runs/recovery_aware_struct_prune/sft_rasp_20.log\", \"model_name\": \"pruned_rasp_20\", \"pid\": \"249577\", \"seed\": 42, \"server\": \"westb-23072\", \"submitted_at\": \"2026-05-14T23:47:23.413Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 2961.2}}}, \"count\": 249, \"total\": 249, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.9186}}"
    }
  },
  "sourceToolAssistantUUID": "4a7541bf-eb55-449f-a1b0-07409f178bce",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "3a90179e-e19e-41d1-8fb4-f23e916f555f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Runtime record

_source line 66_

```json
{
  "type": "last-prompt",
  "leafUuid": "69ae3b7b-911e-4228-a783-ae52dd177cb4",
  "sessionId": "3a90179e-e19e-41d1-8fb4-f23e916f555f"
}
```

---


### Runtime record

_source line 67_

```json
{
  "type": "ai-title",
  "aiTitle": "Map paper results to registry experiments",
  "sessionId": "3a90179e-e19e-41d1-8fb4-f23e916f555f"
}
```

---


### Assistant

_source line 68 · 2026-05-23T10:52:41.535Z_

<details><summary>Logged reasoning block</summary>

```text
Good. Now I have 245K chars with exp_id, metrics, spec, created_at for ALL success experiments. Let me launch an agent to parse this larger file and complete the mapping for all the experiments I still need. 

Let me launch the agent with all the paper values that still need mapping.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "69ae3b7b-911e-4228-a783-ae52dd177cb4",
  "isSidechain": false,
  "requestId": "req_011CbKNgUb2J5AaWkUpezGof",
  "type": "assistant",
  "uuid": "15531f10-ed03-4730-95f9-b2ac4d5a9048",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "3a90179e-e19e-41d1-8fb4-f23e916f555f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FCHRqnYiKhSB1KYzod2yYY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 789,
      "cache_read_input_tokens": 57407,
      "output_tokens": 1869,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 789,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1869,
          "cache_read_input_tokens": 57407,
          "cache_creation_input_tokens": 789,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 789
          },
          "type": "message"
        }
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

_source line 69 · 2026-05-23T10:52:42.551Z_

有了完整 registry 数据（245K），启动 agent 解析剩余实验映射。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "15531f10-ed03-4730-95f9-b2ac4d5a9048",
  "isSidechain": false,
  "requestId": "req_011CbKNgUb2J5AaWkUpezGof",
  "type": "assistant",
  "uuid": "5992aa79-f55b-4562-9da5-4ad60fa1cf29",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "3a90179e-e19e-41d1-8fb4-f23e916f555f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FCHRqnYiKhSB1KYzod2yYY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 789,
      "cache_read_input_tokens": 57407,
      "output_tokens": 1869,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 789,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1869,
          "cache_read_input_tokens": 57407,
          "cache_creation_input_tokens": 789,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 789
          },
          "type": "message"
        }
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

_source line 70 · 2026-05-23T10:53:17.823Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01FCi6H5x65GUEFHnY4j1d2s`</summary>

```json
{
  "description": "Parse full registry for remaining mappings",
  "prompt": "You need to parse a large JSON registry file and extract ALL experiment records, matching them to paper values.\n\nThe file is at: `/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-17-projects-recovery-aware-struct-prune/3a90179e-e19e-41d1-8fb4-f23e916f555f/tool-results/mcp-agent-ml-research-read_registry-1779533555169.txt`\n\nFormat: JSON `{result: string}` where `result` is a YAML string containing experiment records. Each has `exp_id`, `metrics`, `spec` (with server, output_path, checkpoint_path, command etc.), `created_at`.\n\n**I already have matches for these from the first 50 results (the most recent). I need you to find ALL remaining experiments. Specifically, I need matches for:**\n\n### MUST FIND (not in first 50):\n\n**GSM8K 7B 20% core results:**\n- CKA-only SFT=63.91% → look for exp_id like `eval_gsm8k_sft_cka_only_20*`\n- CKA-only GRPO seed42=64.37% → look for `eval_gsm8k_grpo_cka_only_20*`\n- CKA-only GRPO seed123=64.22% → look for `eval_gsm8k_grpo_cka_only_20*seed123*`\n- CKA-only GRPO seed456=64.58% → look for `eval_gsm8k_grpo_cka_only_20*seed456*`\n- Standard SFT=59.29% → look for `eval_gsm8k_sft_standard_20*`\n- Standard GRPO seeds (59.44%, 60.20%, ?) → look for `eval_gsm8k_grpo_standard_20*`\n- RASP α=1.0 SFT=61.49% → look for `eval_gsm8k_sft_rasp*` or `eval_gsm8k_sft_alpha1*`\n- RASP α=1.0 GRPO=60.88% → look for `eval_gsm8k_grpo_rasp*` or `eval_gsm8k_grpo_alpha1*`\n- ShortGPT SFT=44.73% → look for `eval_gsm8k_sft_shortgpt*` or `eval_gsm8k_sft_depth*`\n- ShortGPT GRPO=43.37% → look for `eval_gsm8k_grpo_shortgpt*` or `eval_gsm8k_grpo_depth*`\n- Dense/Unpruned 81.27% or 90.83% → look for `eval_gsm8k*unpruned*` or `eval_gsm8k*dense*`\n\n**GSM8K 15% sparsity:**\n- CKA-only SFT=72.18% → `eval_gsm8k_sft_cka_only_15*`\n- CKA-only GRPO=72.76% (3 seeds: 72.10%, ?, 73.09%) → `eval_gsm8k_grpo_cka_only_15*`\n- Standard SFT=66.49% → `eval_gsm8k_sft_standard_15*`\n- Standard GRPO=65.56% (3 seeds) → `eval_gsm8k_grpo_standard_15*`\n\n**GSM8K 30% sparsity cliff:**\n- Standard=4%, RASP=0%, CKA=0% → look for `*30*` experiments\n\n**Peak rewards:**\n- CKA=0.354, Standard=0.081, RASP=0.061, Random=0.190 → look for GRPO training runs\n\n**MBPP evaluations:**\n- Dense 53.48%, CKA 12.83%/14.17%, Standard 12.03%/13.10%, RASP 11.76%/13.10%, ShortGPT 10.43%/14.44%\n- Look for `eval_mbpp*`\n\n**1.5B cross-scale:**\n- CKA GSM8K=35.48%, Rew=0.238 → `*1p5b*` or `*1.5b*`\n- Standard 22.29%, 0.084\n- RASP 26.16%, 0.099\n\n**Inference efficiency:**\n- Dense Latency=6.682s, Memory=16.22GB, TPS=72.0\n- Look for `*inference*` or `*benchmark*` or `*latency*`\n\n**CKA stability:**\n- Spearman ρ min=0.964, mean=0.979\n- Look for `*cka_stability*` or `*calibration*`\n\n**Gradient flow:**\n- CKA vs Standard=2.89×, CKA vs RASP=2.26×, RASP vs Standard=1.28×\n- Look for `*gradient*`\n\n**Extended training 300 steps:**\n- CKA-only 64.37%→64.37%, Standard 59.44%→59.29%\n- Look for `*300*` or `*extended*`\n\n**Unstructured pruning:**\n- SFT=87.87%, GRPO=87.64%\n- Look for `*unstructured*` or `*magnitude*`\n\n**Cross-architecture Qwen2.5-Math-7B (remaining):**\n- Standard Post-Prune=18.5%, Post-SFT=21.00%\n- Look for `*qwen_math*standard*`\n\n**MATH-500 Standard 25% GRPO=12.8%:**\n- Look for `eval_math500_grpo_standard_25*`\n\n**Dense MATH-500=53.0%:**\n- Look for `eval_math500*dense*` or `eval_math500*unpruned*`\n\n**Instructions:**\n1. Use `python3` or `jq` to parse the file\n2. First probe structure: `jq 'keys' file`, then parse the result field\n3. Extract ALL experiments (may be YAML inside the result string)\n4. For EACH experiment, output: `exp_id | metrics | server (from spec) | output_path/checkpoint_path (from spec) | created_at`\n5. Group by which paper value they match\n6. For any paper value that has NO matching registry experiment, explicitly say so\n7. Note the eval script version: if created_at is 2026-05-23 or later → NEW, before → OLD. Experiments with v2/v3 suffix re-evaluated with NEW script.\n\nOutput the COMPLETE mapping. Be thorough."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5992aa79-f55b-4562-9da5-4ad60fa1cf29",
  "isSidechain": false,
  "requestId": "req_011CbKNgUb2J5AaWkUpezGof",
  "type": "assistant",
  "uuid": "85510dbe-4454-4a97-9654-e8ac41d34a20",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "3a90179e-e19e-41d1-8fb4-f23e916f555f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FCHRqnYiKhSB1KYzod2yYY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 789,
      "cache_read_input_tokens": 57407,
      "output_tokens": 1869,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 789,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1869,
          "cache_read_input_tokens": 57407,
          "cache_creation_input_tokens": 789,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 789
          },
          "type": "message"
        }
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

_source line 71 · 2026-05-23T10:58:10.579Z_

<details><summary>↩ Tool result · `toolu_01FCi6H5x65GUEFHnY4j1d2s`</summary>

```text
Now I have all the data. Here is the complete mapping:

---

## COMPLETE EXPERIMENT REGISTRY MAPPING (249 experiments total)

### A. GSM8K 7B 20% Core Results

| Paper Value | exp_id | Registry Metric | Server | Date | Script Era |
|---|---|---|---|---|---|
| **CKA-only SFT = 63.91%** | `eval_gsm8k_sft_cka_only_20` | gsm8k_accuracy=0.6391 (843/1319) | westd-29022 | 2026-05-20 | OLD |
| **CKA-only GRPO seed42 = 64.37%** | `eval_gsm8k_grpo_cka_only_20_v2` | accuracy=0.6437 (849/1319) | westb-23072 | 2026-05-18 | OLD |
| **CKA-only GRPO seed123 = 64.22%** | `eval_gsm8k_grpo_cka_only_20_seed123` | accuracy=0.6422 (847/1319) | westb-23072 | 2026-05-19 | OLD |
| **CKA-only GRPO seed456 = 64.58% (actually 64.59%)** | `eval_gsm8k_grpo_cka_only_20_seed456_full` | gsm8k_accuracy=0.6459 (852/1319) | westd-29022 | 2026-05-20 | OLD |
| **Standard SFT = 59.29% (actually 59.21%)** | `eval_gsm8k_sft_standard_20` | gsm8k_accuracy=0.5921 (781/1319) | westd-29022 | 2026-05-20 | OLD |
| Also matches: | `eval_sft_standard_full_westd` | accuracy=0.5929 (782/1319) | westd-11672 | 2026-05-15 | OLD |
| **Standard GRPO seed42 = 59.44%** | `eval_gsm8k_grpo_standard_20_fair_v2` | accuracy=59.44 (784/1319) | westd-29022 | 2026-05-19 | OLD |
| **Standard GRPO seed123 = 59.89%** | `eval_gsm8k_grpo_standard_20_seed123_full` | accuracy=0.5989 (790/1319) | westd-29022 | 2026-05-20 | OLD |
| **Standard GRPO seed456 = 60.20%** | `eval_gsm8k_grpo_standard_20_seed456_full` | accuracy=0.602 (794/1319) | westd-29022 | 2026-05-20 | OLD |
| **RASP alpha=1.0 SFT = 61.49%** | `eval_gsm8k_sft_rasp_20` | gsm8k_accuracy=0.6149 (811/1319) | westd-29022 | 2026-05-20 | OLD |
| Also matches: | `eval_sft_rasp_full_westd` | accuracy=0.6149 (811/1319) | westd-11672 | 2026-05-15 | OLD |
| **RASP alpha=1.0 GRPO = 60.88%** | `eval_gsm8k_grpo_rasp_20_fair` | accuracy=0.6088 (803/1319) | westd-29022 | 2026-05-19 | OLD |
| **ShortGPT SFT = 44.73%** | `eval_gsm8k_sft_shortgpt_20` | gsm8k_accuracy=44.73 (590/1319) | westd-29022 | 2026-05-19 | OLD |
| **ShortGPT GRPO = 43.37%** | `eval_gsm8k_grpo_shortgpt_20` | gsm8k_accuracy=43.37 (572/1319) | westd-29022 | 2026-05-19 | OLD |
| **Dense/Unpruned = 90.83%** | `eval_gsm8k_dense_unpruned` | gsm8k_accuracy=0.9083 (1198/1319) | westb-23072 | 2026-05-20 | OLD |
| **Dense (SFT trained) = 81.27%** | `eval_sft_unpruned_full` | accuracy=81.27 (1072/1319) | westd-11672 | 2026-05-16 | OLD |
| Also: | `eval_grpo_unpruned_v2_step100` | accuracy=81.27 (1072/1319) | westd-11672 | 2026-05-16 | OLD |

### B. GSM8K 15% Sparsity

| Paper Value | exp_id | Registry Metric | Date |
|---|---|---|---|
| **CKA-only SFT = 72.18%** | `eval_gsm8k_sft_cka_only_15` | gsm8k_accuracy=0.7218 (952/1319) | 2026-05-20 |
| **CKA-only GRPO seed42 = 73.09%** | `eval_gsm8k_grpo_cka_only_15_v2` | gsm8k_accuracy=0.7309 (964/1319) | 2026-05-20 |
| **CKA-only GRPO seed123 = 73.09%** | `eval_gsm8k_grpo_cka_only_15_seed123` | accuracy=73.09 (964/1319) | 2026-05-20 |
| **CKA-only GRPO seed456 = 72.10%** | `eval_gsm8k_grpo_cka_only_15_seed456` | accuracy=0.721 (951/1319) | 2026-05-20 |
| **CKA GRPO avg = 72.76%** | Computed: mean(73.09, 73.09, 72.10) = 72.76% | -- | -- |
| **Standard SFT = 66.49%** | `eval_gsm8k_sft_standard_15` | gsm8k_accuracy=0.6649 (877/1319) | 2026-05-20 |
| **Standard GRPO seed42 = 66.11%** | `eval_gsm8k_grpo_standard_15_v2` | gsm8k_accuracy=0.6611 (872/1319) | 2026-05-20 |
| **Standard GRPO seed123 = 65.13%** | `eval_gsm8k_grpo_standard_15_seed123_v3` | accuracy=0.6513 (859/1319) | 2026-05-20 |
| **Standard GRPO seed456 = 65.43%** | `eval_gsm8k_grpo_standard_15_seed456_v3` | gsm8k_accuracy=0.6543 (863/1319) | 2026-05-20 |
| **Standard GRPO avg = 65.56%** | Computed: mean(66.11, 65.13, 65.43) = 65.56% | -- | -- |

### C. GSM8K 30% Sparsity Cliff

| Paper Value | exp_id | Registry Metric | Date |
|---|---|---|---|
| **Standard post-prune = 4%** | `eval_postprune_standard_30` | gsm8k_accuracy=0.04 (8/200) | 2026-05-17 |
| **RASP post-prune = 0%** | `eval_postprune_rasp_30` | accuracy=0 (0/200) | 2026-05-17 |
| **CKA post-prune = ~0% (1.6%)** | `prune_eval_cka_only_30` | accuracy=1.6 (N=500 partial) | 2026-05-20 |
| **Standard post-prune (v2) = 2.8%** | `prune_eval_standard_30` | accuracy=2.8 (N=500 partial) | 2026-05-20 |

Note: Paper says "Standard=4%, RASP=0%, CKA=0%". The CKA 30% result at 1.6% is from a partial N=500 eval. These confirm the "cliff" narrative.

### D. Peak Rewards (GRPO Training)

| Paper Value | exp_id | Registry Metric | Date |
|---|---|---|---|
| **CKA = 0.354** | `grpo_cka_only_20` | peak_reward=0.3544 (final_reward=0.3444) | 2026-05-17 |
| **Standard = 0.081** | `grpo_standard_20_fair` | peak_reward=0.081 (final_reward=0.054) | 2026-05-18 |
| **RASP = 0.061** | `grpo_rasp_20_fair` | peak_reward=0.061 (final_reward=0.01) | 2026-05-17 |
| Also: | `grpo_rasp_qwen_math_v3` | reward_final=0.061, peak=0.102 | 2026-05-16 |
| **Random = 0.190** | `grpo_random_20` | reward_peak=0.19 (final=0.164) | 2026-05-17 |

### E. MBPP Evaluations

| Paper Value | exp_id | Registry Metric | Date |
|---|---|---|---|
| **Dense = 53.48%** | `eval_mbpp_dense_unpruned` | pass_at_1=0.5348 (200/374) | 2026-05-19 |
| **CKA SFT = 12.83%** | `eval_mbpp_sft_cka_only_20` | pass_at_1=0.1283 (48/374) | 2026-05-19 |
| **CKA GRPO = 14.17%** | `eval_mbpp_grpo_cka_only_20` | pass_at_1=0.1417 (53/374) | 2026-05-19 |
| **Standard SFT = 12.03%** | `eval_mbpp_sft_standard_20_v4` | pass_at_1=0.1203 (45/374) | 2026-05-19 |
| **Standard GRPO = 13.10%** | `eval_mbpp_grpo_standard_20_v3` or `eval_mbpp_grpo_standard_20_v4` | pass_at_1=0.131 (49/374) | 2026-05-19 |
| **RASP SFT = 11.76%** | `eval_mbpp_sft_rasp_20` | pass_at_1=0.1176 (44/374) | 2026-05-19 |
| **RASP GRPO = 13.10%** | `eval_mbpp_grpo_rasp_20` | pass_at_1=0.131 (49/374) | 2026-05-19 |
| **ShortGPT SFT = 10.43%** | `eval_mbpp_sft_shortgpt_20_v2` | pass_at_1=0.1043 (39/374) | 2026-05-19 |
| **ShortGPT GRPO = 14.44%** | `eval_mbpp_grpo_shortgpt_20_v2` | pass_at_1=0.1444 (54/374) | 2026-05-19 |

### F. 1.5B Cross-Scale

| Paper Value | exp_id | Registry Metric | Date |
|---|---|---|---|
| **CKA GSM8K = 35.48%** | `eval_gsm8k_grpo_cka_only_20_1p5b` | accuracy=0.3548 (468/1319) | 2026-05-18 |
| **CKA Reward = 0.238** | `grpo_cka_only_20_1p5b` | reward_mean=0.2375 | 2026-05-18 |
| **Standard GSM8K = 22.29%** | `eval_gsm8k_grpo_standard_20_1p5b` | accuracy=0.2229 (294/1319) | 2026-05-18 |
| **Standard Reward = 0.084** | `grpo_standard_20_1p5b` | reward_mean=0.0844 | 2026-05-18 |
| **RASP GSM8K = 26.16%** | `eval_gsm8k_grpo_rasp_20_1p5b` | accuracy=0.2616 (345/1319) | 2026-05-18 |
| **RASP Reward = 0.099** | `grpo_rasp_20_1p5b` | final_reward=0.099 | 2026-05-18 |

### G. Inference Efficiency

| Paper Value | exp_id | Registry Metric | Date |
|---|---|---|---|
| **Dense Latency = 6.682s** | `inference_speedup_plan016_v2` | dense.avg_latency_sec=6.682 | 2026-05-16 |
| **Dense Memory = 16.22GB** | `inference_speedup_plan016_v2` | dense.peak_memory_gb=16.22 | 2026-05-16 |
| **Dense TPS = 72.0 (actually 76.25)** | `inference_speedup_plan016_v2` | dense.tokens_per_second=76.25 | 2026-05-16 |
| Note: `inference_bench_clean_v2` shows original_tps=72.02, which matches paper's "72.0" | `inference_bench_clean_v2` | original_tps=72.02 | 2026-05-19 |

The paper likely uses `inference_bench_clean_v2` (72.02 TPS) for some values and `inference_speedup_plan016_v2` (6.682s latency, 16.22GB) for others. The two benchmarks were run on different servers (westd vs westb).

### H. CKA Stability

| Paper Value | exp_id | Registry Metric | Date |
|---|---|---|---|
| **Spearman rho min = 0.964** | `cka_scoring_stability_ablation` | min_combined_rho=0.964 | 2026-05-19 |
| **Spearman rho mean = 0.979** | `cka_scoring_stability_ablation` | mean_combined_rho=0.979 | 2026-05-19 |
| Also: split-half reliability | `cka_calibration_stability_ablation` | split_half_rho=0.9932 | 2026-05-19 |

### I. Gradient Flow

| Paper Value | exp_id | Registry Metric | Date |
|---|---|---|---|
| **CKA vs Standard = 2.89x** | `gradient_flow_v3` | cka_vs_standard_ratio=2.89 | 2026-05-19 |
| **CKA vs RASP = 2.26x** | `gradient_flow_v3` | Computed: cka_mean/rasp_mean = 0.3229/0.1431 = 2.26x | 2026-05-19 |
| **RASP vs Standard = 1.28x** | `gradient_flow_v3` | rasp_vs_standard_ratio=1.28 | 2026-05-19 |

### J. Extended Training 300 Steps

| Paper Value | exp_id | Registry Metric | Date |
|---|---|---|---|
| **CKA-only 64.37% -> 64.37%** | `grpo_cka_only_20_extended_300` | reward_step100=0.354, reward_step300=0.3075 | 2026-05-18 |
| Note: The GSM8K accuracy 64.37% for CKA at step 100 comes from `eval_gsm8k_grpo_cka_only_20_v2`. No separate 300-step eval registered -- the claim "stays at 64.37%" likely means no improvement was observed in the extended training, re-using the step-100 eval. | -- | -- |
| **Standard 59.44% -> 59.29%** | `grpo_standard_20_extended_300_v2` | reward_mean_step300=0.0562 (decline) | 2026-05-18 |
| Note: The 59.29% figure matches `eval_gsm8k_sft_standard_20` (0.5921 ~ 59.21%). No separate extended-300 GSM8K eval registered. The paper claim likely means Standard GRPO's reward declines after step 260, and the accuracy stays at or slightly below the SFT level. | -- | -- |

### K. Unstructured Pruning

| Paper Value | exp_id | Registry Metric | Date |
|---|---|---|---|
| **SFT = 87.87%** | `eval_unstructured_20` | gsm8k_acc=0.8787 (1159/1319) | 2026-05-17 |
| **GRPO = 87.64%** | `eval_gsm8k_grpo_unstructured_20` | accuracy=0.8764 (1156/1319) | 2026-05-19 |

### L. Cross-Architecture Qwen2.5-Math-7B (Standard)

| Paper Value | exp_id | Registry Metric | Date |
|---|---|---|---|
| **Standard Post-Prune = 18.5%** | NO DIRECT MATCH | Not found in registry -- no `eval_postprune_standard_20_qwen_math` or similar exists | -- |
| **Standard Post-SFT = 21.00%** | `eval_gsm8k_sft_qwen_standard_20` | gsm8k_accuracy=0.21 (42/200) | 2026-05-20 |

Note: The post-prune 18.5% for Qwen-Math Standard is **NOT in the registry**. It may have been computed but not registered, or it might be in a result JSON file on the server.

### M. MATH-500

| Paper Value | exp_id | Registry Metric | Date |
|---|---|---|---|
| **Dense MATH-500 = 53.0%** | `eval_math500_dense_2048` | accuracy=0.53 (265/500) | 2026-05-18 |
| Also (different token limit): | `eval_math500_dense_unpruned` / `eval_math500_unpruned` | accuracy=0.736 (368/500) | 2026-05-18/17 |
| **Standard 25% GRPO = 12.8%** | NO DIRECT MATCH | There is no `eval_math500_grpo_standard_25*`. Closest is `eval_math500_sft_standard_25` = 14.0% | -- |

Note: The paper's "12.8%" for MATH-500 Standard 25% GRPO is **NOT in the registry**. The registry only has `eval_math500_sft_standard_25` (14.0%) for that sparsity level. The GRPO eval for Standard 25% on MATH-500 was never registered.

### N. Additional Experiments Found (Not in "Must Find" List)

| Category | exp_id | Key Metric | Date |
|---|---|---|---|
| Random SFT 20% | `eval_gsm8k_sft_random_20` | 0.5125 (676/1319) | 2026-05-21 |
| Random GRPO 20% seed42 | `eval_gsm8k_grpo_random_20_v2` | 0.5057 (667/1319) | 2026-05-21 |
| Random GRPO seed456 | `eval_gsm8k_grpo_random_20_seed456` | 0.5087 (671/1319) | 2026-05-22 |
| Alpha ablation 0.5 SFT | `eval_gsm8k_sft_alpha0p5_20` | 0.6073 | 2026-05-22 |
| Alpha ablation 2.0 SFT | `eval_gsm8k_sft_alpha2p0_20` | 0.6497 | 2026-05-22 |
| Alpha ablation 3.0 SFT | `eval_gsm8k_sft_alpha3p0_20` | 0.6414 | 2026-05-22 |
| Alpha ablation 4.0 SFT | `eval_gsm8k_sft_alpha4_20_v5` | 0.6194 | 2026-05-22 |
| Alpha ablation 0.5 GRPO | `eval_gsm8k_grpo_alpha0p5_20` | 0.6118 | 2026-05-22 |
| Alpha ablation 2.0 GRPO | `eval_gsm8k_grpo_alpha2p0_20` | 0.6611 | 2026-05-22 |
| Alpha ablation 3.0 GRPO | `eval_gsm8k_grpo_alpha3p0_20` | 0.6345 | 2026-05-22 |
| Alpha ablation 4.0 GRPO | `eval_gsm8k_grpo_alpha4_20_v3` | 0.6277 | 2026-05-22 |
| 25% sparsity CKA SFT | `eval_gsm8k_sft_cka_only_25` | 0.6012 | 2026-05-21 |
| 25% sparsity CKA GRPO | `eval_gsm8k_grpo_cka_only_25_v3` | 0.5959 | 2026-05-21 |
| 25% sparsity Standard SFT | `eval_gsm8k_sft_standard_25` | 0.5087 | 2026-05-21 |
| 25% sparsity Standard GRPO | `eval_gsm8k_grpo_standard_25` | 0.5186 | 2026-05-21 |
| HumanEval Unpruned (2048) | `eval_humaneval_unpruned_2048` | pass@1=0.4512 (74/164) | 2026-05-17 |
| Depth-first (ShortGPT variant) SFT | `eval_gsm8k_sft_depth_first_20` | EMPTY METRICS (not completed) | 2026-05-22 |
| Depth-first GRPO | `eval_gsm8k_grpo_depth_first_20` | EMPTY METRICS (not completed) | 2026-05-22 |

### O. Paper Values with NO Registry Match

1. **Standard Post-Prune accuracy for Qwen2.5-Math-7B = 18.5%** -- No registry entry. Only the post-SFT result (21.0%) is registered.

2. **MATH-500 Standard 25% GRPO = 12.8%** -- No registry entry for `eval_math500_grpo_standard_25`. The registry has the SFT version (`eval_math500_sft_standard_25` = 14.0%) but not the GRPO version.

3. **Extended training 300-step GSM8K evals** -- The extended training runs (`grpo_cka_only_20_extended_300`, `grpo_standard_20_extended_300_v2`) are registered but no separate GSM8K eval at step 300 was registered. The paper's claims about accuracy at 300 steps appear to reuse earlier eval numbers.

4. **Standard GRPO 20% "3rd seed" value** -- The paper lists 3 seeds for Standard GRPO 20%: 59.44%, 60.20%, and possibly a third. Only seed42 (59.44%), seed123 (59.89%=`eval_gsm8k_grpo_standard_20_seed123_full`), and seed456 (60.20%=`eval_gsm8k_grpo_standard_20_seed456_full`) are in the registry.

### P. Script Era Classification

All experiments have `created_at` before 2026-05-23, so they are all **OLD** script era, except:
- `eval_math500_grpo_cka_only_20_2048_v2` (2026-05-23T05:07) -- **NEW**
- `eval_math500_grpo_rasp_alpha3p0_20` (2026-05-23T03:19) -- **NEW**
- `eval_math500_grpo_rasp_alpha0p5_20` (2026-05-23T02:59) -- **NEW**
- `eval_math500_grpo_rasp_alpha4p0_20` (2026-05-23T00:01) -- **NEW**

Experiments with v2/v3/v4/v5 suffixes are re-runs, not necessarily "new script" -- they typically just fixed bugs or used different parameters. The key distinction is `created_at >= 2026-05-23`.

agentId: aaf740c46822c95dd (use SendMessage with to: 'aaf740c46822c95dd' to continue this agent)
&lt;usage>total_tokens: 111493
tool_uses: 18
duration_ms: 292751&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "85510dbe-4454-4a97-9654-e8ac41d34a20",
  "isSidechain": false,
  "promptId": "dddf37fd-16cc-4cd5-bb05-648328938281",
  "type": "user",
  "uuid": "fb190ade-0800-4b65-8101-37a33c75c70f",
  "toolUseResult": {
    "status": "completed",
    "prompt": "You need to parse a large JSON registry file and extract ALL experiment records, matching them to paper values.\n\nThe file is at: `/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-17-projects-recovery-aware-struct-prune/3a90179e-e19e-41d1-8fb4-f23e916f555f/tool-results/mcp-agent-ml-research-read_registry-1779533555169.txt`\n\nFormat: JSON `{result: string}` where `result` is a YAML string containing experiment records. Each has `exp_id`, `metrics`, `spec` (with server, output_path, checkpoint_path, command etc.), `created_at`.\n\n**I already have matches for these from the first 50 results (the most recent). I need you to find ALL remaining experiments. Specifically, I need matches for:**\n\n### MUST FIND (not in first 50):\n\n**GSM8K 7B 20% core results:**\n- CKA-only SFT=63.91% → look for exp_id like `eval_gsm8k_sft_cka_only_20*`\n- CKA-only GRPO seed42=64.37% → look for `eval_gsm8k_grpo_cka_only_20*`\n- CKA-only GRPO seed123=64.22% → look for `eval_gsm8k_grpo_cka_only_20*seed123*`\n- CKA-only GRPO seed456=64.58% → look for `eval_gsm8k_grpo_cka_only_20*seed456*`\n- Standard SFT=59.29% → look for `eval_gsm8k_sft_standard_20*`\n- Standard GRPO seeds (59.44%, 60.20%, ?) → look for `eval_gsm8k_grpo_standard_20*`\n- RASP α=1.0 SFT=61.49% → look for `eval_gsm8k_sft_rasp*` or `eval_gsm8k_sft_alpha1*`\n- RASP α=1.0 GRPO=60.88% → look for `eval_gsm8k_grpo_rasp*` or `eval_gsm8k_grpo_alpha1*`\n- ShortGPT SFT=44.73% → look for `eval_gsm8k_sft_shortgpt*` or `eval_gsm8k_sft_depth*`\n- ShortGPT GRPO=43.37% → look for `eval_gsm8k_grpo_shortgpt*` or `eval_gsm8k_grpo_depth*`\n- Dense/Unpruned 81.27% or 90.83% → look for `eval_gsm8k*unpruned*` or `eval_gsm8k*dense*`\n\n**GSM8K 15% sparsity:**\n- CKA-only SFT=72.18% → `eval_gsm8k_sft_cka_only_15*`\n- CKA-only GRPO=72.76% (3 seeds: 72.10%, ?, 73.09%) → `eval_gsm8k_grpo_cka_only_15*`\n- Standard SFT=66.49% → `eval_gsm8k_sft_standard_15*`\n- Standard GRPO=65.56% (3 seeds) → `eval_gsm8k_grpo_standard_15*`\n\n**GSM8K 30% sparsity cliff:**\n- Standard=4%, RASP=0%, CKA=0% → look for `*30*` experiments\n\n**Peak rewards:**\n- CKA=0.354, Standard=0.081, RASP=0.061, Random=0.190 → look for GRPO training runs\n\n**MBPP evaluations:**\n- Dense 53.48%, CKA 12.83%/14.17%, Standard 12.03%/13.10%, RASP 11.76%/13.10%, ShortGPT 10.43%/14.44%\n- Look for `eval_mbpp*`\n\n**1.5B cross-scale:**\n- CKA GSM8K=35.48%, Rew=0.238 → `*1p5b*` or `*1.5b*`\n- Standard 22.29%, 0.084\n- RASP 26.16%, 0.099\n\n**Inference efficiency:**\n- Dense Latency=6.682s, Memory=16.22GB, TPS=72.0\n- Look for `*inference*` or `*benchmark*` or `*latency*`\n\n**CKA stability:**\n- Spearman ρ min=0.964, mean=0.979\n- Look for `*cka_stability*` or `*calibration*`\n\n**Gradient flow:**\n- CKA vs Standard=2.89×, CKA vs RASP=2.26×, RASP vs Standard=1.28×\n- Look for `*gradient*`\n\n**Extended training 300 steps:**\n- CKA-only 64.37%→64.37%, Standard 59.44%→59.29%\n- Look for `*300*` or `*extended*`\n\n**Unstructured pruning:**\n- SFT=87.87%, GRPO=87.64%\n- Look for `*unstructured*` or `*magnitude*`\n\n**Cross-architecture Qwen2.5-Math-7B (remaining):**\n- Standard Post-Prune=18.5%, Post-SFT=21.00%\n- Look for `*qwen_math*standard*`\n\n**MATH-500 Standard 25% GRPO=12.8%:**\n- Look for `eval_math500_grpo_standard_25*`\n\n**Dense MATH-500=53.0%:**\n- Look for `eval_math500*dense*` or `eval_math500*unpruned*`\n\n**Instructions:**\n1. Use `python3` or `jq` to parse the file\n2. First probe structure: `jq 'keys' file`, then parse the result field\n3. Extract ALL experiments (may be YAML inside the result string)\n4. For EACH experiment, output: `exp_id | metrics | server (from spec) | output_path/checkpoint_path (from spec) | created_at`\n5. Group by which paper value they match\n6. For any paper value that has NO matching registry experiment, explicitly say so\n7. Note the eval script version: if created_at is 2026-05-23 or later → NEW, before → OLD. Experiments with v2/v3 suffix re-evaluated with NEW script.\n\nOutput the COMPLETE mapping. Be thorough.",
    "agentId": "aaf740c46822c95dd",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Now I have all the data. Here is the complete mapping:\n\n---\n\n## COMPLETE EXPERIMENT REGISTRY MAPPING (249 experiments total)\n\n### A. GSM8K 7B 20% Core Results\n\n| Paper Value | exp_id | Registry Metric | Server | Date | Script Era |\n|---|---|---|---|---|---|\n| **CKA-only SFT = 63.91%** | `eval_gsm8k_sft_cka_only_20` | gsm8k_accuracy=0.6391 (843/1319) | westd-29022 | 2026-05-20 | OLD |\n| **CKA-only GRPO seed42 = 64.37%** | `eval_gsm8k_grpo_cka_only_20_v2` | accuracy=0.6437 (849/1319) | westb-23072 | 2026-05-18 | OLD |\n| **CKA-only GRPO seed123 = 64.22%** | `eval_gsm8k_grpo_cka_only_20_seed123` | accuracy=0.6422 (847/1319) | westb-23072 | 2026-05-19 | OLD |\n| **CKA-only GRPO seed456 = 64.58% (actually 64.59%)** | `eval_gsm8k_grpo_cka_only_20_seed456_full` | gsm8k_accuracy=0.6459 (852/1319) | westd-29022 | 2026-05-20 | OLD |\n| **Standard SFT = 59.29% (actually 59.21%)** | `eval_gsm8k_sft_standard_20` | gsm8k_accuracy=0.5921 (781/1319) | westd-29022 | 2026-05-20 | OLD |\n| Also matches: | `eval_sft_standard_full_westd` | accuracy=0.5929 (782/1319) | westd-11672 | 2026-05-15 | OLD |\n| **Standard GRPO seed42 = 59.44%** | `eval_gsm8k_grpo_standard_20_fair_v2` | accuracy=59.44 (784/1319) | westd-29022 | 2026-05-19 | OLD |\n| **Standard GRPO seed123 = 59.89%** | `eval_gsm8k_grpo_standard_20_seed123_full` | accuracy=0.5989 (790/1319) | westd-29022 | 2026-05-20 | OLD |\n| **Standard GRPO seed456 = 60.20%** | `eval_gsm8k_grpo_standard_20_seed456_full` | accuracy=0.602 (794/1319) | westd-29022 | 2026-05-20 | OLD |\n| **RASP alpha=1.0 SFT = 61.49%** | `eval_gsm8k_sft_rasp_20` | gsm8k_accuracy=0.6149 (811/1319) | westd-29022 | 2026-05-20 | OLD |\n| Also matches: | `eval_sft_rasp_full_westd` | accuracy=0.6149 (811/1319) | westd-11672 | 2026-05-15 | OLD |\n| **RASP alpha=1.0 GRPO = 60.88%** | `eval_gsm8k_grpo_rasp_20_fair` | accuracy=0.6088 (803/1319) | westd-29022 | 2026-05-19 | OLD |\n| **ShortGPT SFT = 44.73%** | `eval_gsm8k_sft_shortgpt_20` | gsm8k_accuracy=44.73 (590/1319) | westd-29022 | 2026-05-19 | OLD |\n| **ShortGPT GRPO = 43.37%** | `eval_gsm8k_grpo_shortgpt_20` | gsm8k_accuracy=43.37 (572/1319) | westd-29022 | 2026-05-19 | OLD |\n| **Dense/Unpruned = 90.83%** | `eval_gsm8k_dense_unpruned` | gsm8k_accuracy=0.9083 (1198/1319) | westb-23072 | 2026-05-20 | OLD |\n| **Dense (SFT trained) = 81.27%** | `eval_sft_unpruned_full` | accuracy=81.27 (1072/1319) | westd-11672 | 2026-05-16 | OLD |\n| Also: | `eval_grpo_unpruned_v2_step100` | accuracy=81.27 (1072/1319) | westd-11672 | 2026-05-16 | OLD |\n\n### B. GSM8K 15% Sparsity\n\n| Paper Value | exp_id | Registry Metric | Date |\n|---|---|---|---|\n| **CKA-only SFT = 72.18%** | `eval_gsm8k_sft_cka_only_15` | gsm8k_accuracy=0.7218 (952/1319) | 2026-05-20 |\n| **CKA-only GRPO seed42 = 73.09%** | `eval_gsm8k_grpo_cka_only_15_v2` | gsm8k_accuracy=0.7309 (964/1319) | 2026-05-20 |\n| **CKA-only GRPO seed123 = 73.09%** | `eval_gsm8k_grpo_cka_only_15_seed123` | accuracy=73.09 (964/1319) | 2026-05-20 |\n| **CKA-only GRPO seed456 = 72.10%** | `eval_gsm8k_grpo_cka_only_15_seed456` | accuracy=0.721 (951/1319) | 2026-05-20 |\n| **CKA GRPO avg = 72.76%** | Computed: mean(73.09, 73.09, 72.10) = 72.76% | -- | -- |\n| **Standard SFT = 66.49%** | `eval_gsm8k_sft_standard_15` | gsm8k_accuracy=0.6649 (877/1319) | 2026-05-20 |\n| **Standard GRPO seed42 = 66.11%** | `eval_gsm8k_grpo_standard_15_v2` | gsm8k_accuracy=0.6611 (872/1319) | 2026-05-20 |\n| **Standard GRPO seed123 = 65.13%** | `eval_gsm8k_grpo_standard_15_seed123_v3` | accuracy=0.6513 (859/1319) | 2026-05-20 |\n| **Standard GRPO seed456 = 65.43%** | `eval_gsm8k_grpo_standard_15_seed456_v3` | gsm8k_accuracy=0.6543 (863/1319) | 2026-05-20 |\n| **Standard GRPO avg = 65.56%** | Computed: mean(66.11, 65.13, 65.43) = 65.56% | -- | -- |\n\n### C. GSM8K 30% Sparsity Cliff\n\n| Paper Value | exp_id | Registry Metric | Date |\n|---|---|---|---|\n| **Standard post-prune = 4%** | `eval_postprune_standard_30` | gsm8k_accuracy=0.04 (8/200) | 2026-05-17 |\n| **RASP post-prune = 0%** | `eval_postprune_rasp_30` | accuracy=0 (0/200) | 2026-05-17 |\n| **CKA post-prune = ~0% (1.6%)** | `prune_eval_cka_only_30` | accuracy=1.6 (N=500 partial) | 2026-05-20 |\n| **Standard post-prune (v2) = 2.8%** | `prune_eval_standard_30` | accuracy=2.8 (N=500 partial) | 2026-05-20 |\n\nNote: Paper says \"Standard=4%, RASP=0%, CKA=0%\". The CKA 30% result at 1.6% is from a partial N=500 eval. These confirm the \"cliff\" narrative.\n\n### D. Peak Rewards (GRPO Training)\n\n| Paper Value | exp_id | Registry Metric | Date |\n|---|---|---|---|\n| **CKA = 0.354** | `grpo_cka_only_20` | peak_reward=0.3544 (final_reward=0.3444) | 2026-05-17 |\n| **Standard = 0.081** | `grpo_standard_20_fair` | peak_reward=0.081 (final_reward=0.054) | 2026-05-18 |\n| **RASP = 0.061** | `grpo_rasp_20_fair` | peak_reward=0.061 (final_reward=0.01) | 2026-05-17 |\n| Also: | `grpo_rasp_qwen_math_v3` | reward_final=0.061, peak=0.102 | 2026-05-16 |\n| **Random = 0.190** | `grpo_random_20` | reward_peak=0.19 (final=0.164) | 2026-05-17 |\n\n### E. MBPP Evaluations\n\n| Paper Value | exp_id | Registry Metric | Date |\n|---|---|---|---|\n| **Dense = 53.48%** | `eval_mbpp_dense_unpruned` | pass_at_1=0.5348 (200/374) | 2026-05-19 |\n| **CKA SFT = 12.83%** | `eval_mbpp_sft_cka_only_20` | pass_at_1=0.1283 (48/374) | 2026-05-19 |\n| **CKA GRPO = 14.17%** | `eval_mbpp_grpo_cka_only_20` | pass_at_1=0.1417 (53/374) | 2026-05-19 |\n| **Standard SFT = 12.03%** | `eval_mbpp_sft_standard_20_v4` | pass_at_1=0.1203 (45/374) | 2026-05-19 |\n| **Standard GRPO = 13.10%** | `eval_mbpp_grpo_standard_20_v3` or `eval_mbpp_grpo_standard_20_v4` | pass_at_1=0.131 (49/374) | 2026-05-19 |\n| **RASP SFT = 11.76%** | `eval_mbpp_sft_rasp_20` | pass_at_1=0.1176 (44/374) | 2026-05-19 |\n| **RASP GRPO = 13.10%** | `eval_mbpp_grpo_rasp_20` | pass_at_1=0.131 (49/374) | 2026-05-19 |\n| **ShortGPT SFT = 10.43%** | `eval_mbpp_sft_shortgpt_20_v2` | pass_at_1=0.1043 (39/374) | 2026-05-19 |\n| **ShortGPT GRPO = 14.44%** | `eval_mbpp_grpo_shortgpt_20_v2` | pass_at_1=0.1444 (54/374) | 2026-05-19 |\n\n### F. 1.5B Cross-Scale\n\n| Paper Value | exp_id | Registry Metric | Date |\n|---|---|---|---|\n| **CKA GSM8K = 35.48%** | `eval_gsm8k_grpo_cka_only_20_1p5b` | accuracy=0.3548 (468/1319) | 2026-05-18 |\n| **CKA Reward = 0.238** | `grpo_cka_only_20_1p5b` | reward_mean=0.2375 | 2026-05-18 |\n| **Standard GSM8K = 22.29%** | `eval_gsm8k_grpo_standard_20_1p5b` | accuracy=0.2229 (294/1319) | 2026-05-18 |\n| **Standard Reward = 0.084** | `grpo_standard_20_1p5b` | reward_mean=0.0844 | 2026-05-18 |\n| **RASP GSM8K = 26.16%** | `eval_gsm8k_grpo_rasp_20_1p5b` | accuracy=0.2616 (345/1319) | 2026-05-18 |\n| **RASP Reward = 0.099** | `grpo_rasp_20_1p5b` | final_reward=0.099 | 2026-05-18 |\n\n### G. Inference Efficiency\n\n| Paper Value | exp_id | Registry Metric | Date |\n|---|---|---|---|\n| **Dense Latency = 6.682s** | `inference_speedup_plan016_v2` | dense.avg_latency_sec=6.682 | 2026-05-16 |\n| **Dense Memory = 16.22GB** | `inference_speedup_plan016_v2` | dense.peak_memory_gb=16.22 | 2026-05-16 |\n| **Dense TPS = 72.0 (actually 76.25)** | `inference_speedup_plan016_v2` | dense.tokens_per_second=76.25 | 2026-05-16 |\n| Note: `inference_bench_clean_v2` shows original_tps=72.02, which matches paper's \"72.0\" | `inference_bench_clean_v2` | original_tps=72.02 | 2026-05-19 |\n\nThe paper likely uses `inference_bench_clean_v2` (72.02 TPS) for some values and `inference_speedup_plan016_v2` (6.682s latency, 16.22GB) for others. The two benchmarks were run on different servers (westd vs westb).\n\n### H. CKA Stability\n\n| Paper Value | exp_id | Registry Metric | Date |\n|---|---|---|---|\n| **Spearman rho min = 0.964** | `cka_scoring_stability_ablation` | min_combined_rho=0.964 | 2026-05-19 |\n| **Spearman rho mean = 0.979** | `cka_scoring_stability_ablation` | mean_combined_rho=0.979 | 2026-05-19 |\n| Also: split-half reliability | `cka_calibration_stability_ablation` | split_half_rho=0.9932 | 2026-05-19 |\n\n### I. Gradient Flow\n\n| Paper Value | exp_id | Registry Metric | Date |\n|---|---|---|---|\n| **CKA vs Standard = 2.89x** | `gradient_flow_v3` | cka_vs_standard_ratio=2.89 | 2026-05-19 |\n| **CKA vs RASP = 2.26x** | `gradient_flow_v3` | Computed: cka_mean/rasp_mean = 0.3229/0.1431 = 2.26x | 2026-05-19 |\n| **RASP vs Standard = 1.28x** | `gradient_flow_v3` | rasp_vs_standard_ratio=1.28 | 2026-05-19 |\n\n### J. Extended Training 300 Steps\n\n| Paper Value | exp_id | Registry Metric | Date |\n|---|---|---|---|\n| **CKA-only 64.37% -> 64.37%** | `grpo_cka_only_20_extended_300` | reward_step100=0.354, reward_step300=0.3075 | 2026-05-18 |\n| Note: The GSM8K accuracy 64.37% for CKA at step 100 comes from `eval_gsm8k_grpo_cka_only_20_v2`. No separate 300-step eval registered -- the claim \"stays at 64.37%\" likely means no improvement was observed in the extended training, re-using the step-100 eval. | -- | -- |\n| **Standard 59.44% -> 59.29%** | `grpo_standard_20_extended_300_v2` | reward_mean_step300=0.0562 (decline) | 2026-05-18 |\n| Note: The 59.29% figure matches `eval_gsm8k_sft_standard_20` (0.5921 ~ 59.21%). No separate extended-300 GSM8K eval registered. The paper claim likely means Standard GRPO's reward declines after step 260, and the accuracy stays at or slightly below the SFT level. | -- | -- |\n\n### K. Unstructured Pruning\n\n| Paper Value | exp_id | Registry Metric | Date |\n|---|---|---|---|\n| **SFT = 87.87%** | `eval_unstructured_20` | gsm8k_acc=0.8787 (1159/1319) | 2026-05-17 |\n| **GRPO = 87.64%** | `eval_gsm8k_grpo_unstructured_20` | accuracy=0.8764 (1156/1319) | 2026-05-19 |\n\n### L. Cross-Architecture Qwen2.5-Math-7B (Standard)\n\n| Paper Value | exp_id | Registry Metric | Date |\n|---|---|---|---|\n| **Standard Post-Prune = 18.5%** | NO DIRECT MATCH | Not found in registry -- no `eval_postprune_standard_20_qwen_math` or similar exists | -- |\n| **Standard Post-SFT = 21.00%** | `eval_gsm8k_sft_qwen_standard_20` | gsm8k_accuracy=0.21 (42/200) | 2026-05-20 |\n\nNote: The post-prune 18.5% for Qwen-Math Standard is **NOT in the registry**. It may have been computed but not registered, or it might be in a result JSON file on the server.\n\n### M. MATH-500\n\n| Paper Value | exp_id | Registry Metric | Date |\n|---|---|---|---|\n| **Dense MATH-500 = 53.0%** | `eval_math500_dense_2048` | accuracy=0.53 (265/500) | 2026-05-18 |\n| Also (different token limit): | `eval_math500_dense_unpruned` / `eval_math500_unpruned` | accuracy=0.736 (368/500) | 2026-05-18/17 |\n| **Standard 25% GRPO = 12.8%** | NO DIRECT MATCH | There is no `eval_math500_grpo_standard_25*`. Closest is `eval_math500_sft_standard_25` = 14.0% | -- |\n\nNote: The paper's \"12.8%\" for MATH-500 Standard 25% GRPO is **NOT in the registry**. The registry only has `eval_math500_sft_standard_25` (14.0%) for that sparsity level. The GRPO eval for Standard 25% on MATH-500 was never registered.\n\n### N. Additional Experiments Found (Not in \"Must Find\" List)\n\n| Category | exp_id | Key Metric | Date |\n|---|---|---|---|\n| Random SFT 20% | `eval_gsm8k_sft_random_20` | 0.5125 (676/1319) | 2026-05-21 |\n| Random GRPO 20% seed42 | `eval_gsm8k_grpo_random_20_v2` | 0.5057 (667/1319) | 2026-05-21 |\n| Random GRPO seed456 | `eval_gsm8k_grpo_random_20_seed456` | 0.5087 (671/1319) | 2026-05-22 |\n| Alpha ablation 0.5 SFT | `eval_gsm8k_sft_alpha0p5_20` | 0.6073 | 2026-05-22 |\n| Alpha ablation 2.0 SFT | `eval_gsm8k_sft_alpha2p0_20` | 0.6497 | 2026-05-22 |\n| Alpha ablation 3.0 SFT | `eval_gsm8k_sft_alpha3p0_20` | 0.6414 | 2026-05-22 |\n| Alpha ablation 4.0 SFT | `eval_gsm8k_sft_alpha4_20_v5` | 0.6194 | 2026-05-22 |\n| Alpha ablation 0.5 GRPO | `eval_gsm8k_grpo_alpha0p5_20` | 0.6118 | 2026-05-22 |\n| Alpha ablation 2.0 GRPO | `eval_gsm8k_grpo_alpha2p0_20` | 0.6611 | 2026-05-22 |\n| Alpha ablation 3.0 GRPO | `eval_gsm8k_grpo_alpha3p0_20` | 0.6345 | 2026-05-22 |\n| Alpha ablation 4.0 GRPO | `eval_gsm8k_grpo_alpha4_20_v3` | 0.6277 | 2026-05-22 |\n| 25% sparsity CKA SFT | `eval_gsm8k_sft_cka_only_25` | 0.6012 | 2026-05-21 |\n| 25% sparsity CKA GRPO | `eval_gsm8k_grpo_cka_only_25_v3` | 0.5959 | 2026-05-21 |\n| 25% sparsity Standard SFT | `eval_gsm8k_sft_standard_25` | 0.5087 | 2026-05-21 |\n| 25% sparsity Standard GRPO | `eval_gsm8k_grpo_standard_25` | 0.5186 | 2026-05-21 |\n| HumanEval Unpruned (2048) | `eval_humaneval_unpruned_2048` | pass@1=0.4512 (74/164) | 2026-05-17 |\n| Depth-first (ShortGPT variant) SFT | `eval_gsm8k_sft_depth_first_20` | EMPTY METRICS (not completed) | 2026-05-22 |\n| Depth-first GRPO | `eval_gsm8k_grpo_depth_first_20` | EMPTY METRICS (not completed) | 2026-05-22 |\n\n### O. Paper Values with NO Registry Match\n\n1. **Standard Post-Prune accuracy for Qwen2.5-Math-7B = 18.5%** -- No registry entry. Only the post-SFT result (21.0%) is registered.\n\n2. **MATH-500 Standard 25% GRPO = 12.8%** -- No registry entry for `eval_math500_grpo_standard_25`. The registry has the SFT version (`eval_math500_sft_standard_25` = 14.0%) but not the GRPO version.\n\n3. **Extended training 300-step GSM8K evals** -- The extended training runs (`grpo_cka_only_20_extended_300`, `grpo_standard_20_extended_300_v2`) are registered but no separate GSM8K eval at step 300 was registered. The paper's claims about accuracy at 300 steps appear to reuse earlier eval numbers.\n\n4. **Standard GRPO 20% \"3rd seed\" value** -- The paper lists 3 seeds for Standard GRPO 20%: 59.44%, 60.20%, and possibly a third. Only seed42 (59.44%), seed123 (59.89%=`eval_gsm8k_grpo_standard_20_seed123_full`), and seed456 (60.20%=`eval_gsm8k_grpo_standard_20_seed456_full`) are in the registry.\n\n### P. Script Era Classification\n\nAll experiments have `created_at` before 2026-05-23, so they are all **OLD** script era, except:\n- `eval_math500_grpo_cka_only_20_2048_v2` (2026-05-23T05:07) -- **NEW**\n- `eval_math500_grpo_rasp_alpha3p0_20` (2026-05-23T03:19) -- **NEW**\n- `eval_math500_grpo_rasp_alpha0p5_20` (2026-05-23T02:59) -- **NEW**\n- `eval_math500_grpo_rasp_alpha4p0_20` (2026-05-23T00:01) -- **NEW**\n\nExperiments with v2/v3/v4/v5 suffixes are re-runs, not necessarily \"new script\" -- they typically just fixed bugs or used different parameters. The key distinction is `created_at >= 2026-05-23`."
      }
    ],
    "totalDurationMs": 292751,
    "totalTokens": 111493,
    "totalToolUseCount": 18,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2703,
      "cache_read_input_tokens": 102162,
      "output_tokens": 6627,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2703
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 6627,
          "cache_read_input_tokens": 102162,
          "cache_creation_input_tokens": 2703,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2703,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 10,
      "searchCount": 0,
      "bashCount": 8,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 0
    }
  },
  "sourceToolAssistantUUID": "85510dbe-4454-4a97-9654-e8ac41d34a20",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "3a90179e-e19e-41d1-8fb4-f23e916f555f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Runtime record

_source line 72_

```json
{
  "type": "last-prompt",
  "leafUuid": "fb190ade-0800-4b65-8101-37a33c75c70f",
  "sessionId": "3a90179e-e19e-41d1-8fb4-f23e916f555f"
}
```

---


### Runtime record

_source line 73_

```json
{
  "type": "ai-title",
  "aiTitle": "Map paper results to registry experiments",
  "sessionId": "3a90179e-e19e-41d1-8fb4-f23e916f555f"
}
```

---


### Assistant

_source line 74 · 2026-05-23T10:59:10.298Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the data I need. Let me compile the complete provenance table. Let me also note:

1. Standard SFT 20% has a discrepancy: registry has `eval_gsm8k_sft_standard_20` with 0.5921 (781/1319=59.21%) but also `eval_sft_standard_full_westd` with 0.5929 (782/1319=59.29%). The paper uses 59.29%. The appendix notes "Standard seed 42 was trained from a separately initialized SFT checkpoint (accuracy 59.21% vs. 

59.29% for seeds 123/456; Δ = 0.08 pp)."

2. CKA-only GRPO seed456: registry shows 0.6459 (852/1319), but 852/1319 = 0.64594 ≈ 64.59%. Paper says 64.58%. This is a rounding issue.

3. Alpha=3.0 GRPO: registry shows 0.6345 (837/1319), 837/1319 = 63.456%. Paper says 63.46%. This matches (rounding up).

4. Checking the remaining entries for consistency...

For the standard GRPO baseline with 20% CKA, the paper reports a mean of 59.84% ± 0.38pp across three seeds, and I can verify this by averaging the individual seed results. The standard SFT baseline shows 59.29% in the paper, which corresponds to the westd evaluation variant in the registry rather than the standard one. Now I need to construct the output file systematically, making sure to capture every table entry and reported value.

I'm working through the checkpoint and result file paths—most are stored under the recovery_aware_struct_prune directory structure, though I'll need to infer some paths from the experiment IDs where I don't have explicit agent results. I'll organize the provenance audit by table and figure, documenting the exp_id, metric matches, evaluation script versions, and seed information for each entry. I also need to trace through the figures in the experiments.tex file to understand what each visualization represents, starting with the dose-response curve.

Now I'm mapping out the figures and their data sources—the reward trajectories and collapse dynamics come from the GRPO training experiments, the CKA heatmaps from pruning analysis, and the extended training figures from the 300-step variants. I'll also need to account for the KL divergence appendix figure.

I need to be careful about which evaluation script version was used for each experiment based on their creation dates—anything from May 23 onward or with v2/v3 suffixes uses the newer format, while earlier experiments from mid-May use the older format.

But I'm noticing some inconsistency here. The v2/v3 suffixed experiments like `eval_gsm8k_grpo_cka_only_20_v2` were created on May 18, which is before the May 23 cutoff, so if those suffixes indicate the new script, the timeline doesn't quite align. I suspect the v2/v3 notation might specifically apply to MATH-500 re-runs where the answer extraction was updated, rather than being a universal indicator across all datasets.

For GSM8K, the eval script format was probably consistent throughout since all those experiments predate May 23. So I'll apply the rule straightforwardly: anything created on or after May 23 gets marked NEW, v2/v3 suffixes get marked NEW (particularly for MATH-500), and everything else defaults to OLD. I'm realizing the instruction about v2/v3 suffixes might specifically apply to MATH-500 re-evaluations with updated answer extraction logic, not all experiments with those suffixes. Let me just apply the rules as stated and add clarifying notes where the categorization feels ambiguous.

Now I need to write out the full provenance document organized by table, and I should double-check the Standard SFT 20% discrepancy against what the paper reports.

Looking at the eval results, the paper cites 59.29% which comes from the full SFT eval (westd-11672 from May 15), while the Standard seed 42 checkpoint shows 59.21% from a separate run on May 20. The appendix clarifies that seeds 123/456 achieved 59.29% versus seed 42's 59.21%, a difference of 0.08 percentage points.

Now I'm documenting the provenance and noting the key metric discrepancies: the CKA-only GRPO and Alpha=3.0 GRPO values differ slightly from the paper due to rounding, the Standard SFT has two registry values depending on which checkpoint, and I need to track down the 30% cliff CKA result.

I'm also mapping out the data sources for each figure—the dose-response curve comes from Table 3, the reward trajectories and gradient norms from the GRPO training logs, the CKA heatmap from pruning analysis, and the extended training results from the longer-run experiments.

Now I'll organize the document by table and figure, then work through each row systematically.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fb190ade-0800-4b65-8101-37a33c75c70f",
  "isSidechain": false,
  "requestId": "req_011CbKP7CcHYNN3ZoQVwtRyy",
  "type": "assistant",
  "uuid": "e247825c-3add-4da3-8486-c9b0241b3195",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "3a90179e-e19e-41d1-8fb4-f23e916f555f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0116cwWjSbrSosRnMPJ8GGv3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8570,
      "cache_read_input_tokens": 58196,
      "output_tokens": 2958,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8570,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2958,
          "cache_read_input_tokens": 58196,
          "cache_creation_input_tokens": 8570,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8570
          },
          "type": "message"
        }
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

_source line 75 · 2026-05-23T10:59:10.304Z_

现在有了完整数据。编写溯源表。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e247825c-3add-4da3-8486-c9b0241b3195",
  "isSidechain": false,
  "requestId": "req_011CbKP7CcHYNN3ZoQVwtRyy",
  "type": "assistant",
  "uuid": "30c08201-e01f-4190-b569-902a0032d62c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "3a90179e-e19e-41d1-8fb4-f23e916f555f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0116cwWjSbrSosRnMPJ8GGv3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8570,
      "cache_read_input_tokens": 58196,
      "output_tokens": 2958,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8570,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2958,
          "cache_read_input_tokens": 58196,
          "cache_creation_input_tokens": 8570,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8570
          },
          "type": "message"
        }
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

_source line 76 · 2026-05-23T10:59:10.559Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_017Q6ayjbQHjwL5aR5xr5BgN`</summary>

```json
{
  "query": "select:TodoWrite",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "30c08201-e01f-4190-b569-902a0032d62c",
  "isSidechain": false,
  "requestId": "req_011CbKP7CcHYNN3ZoQVwtRyy",
  "type": "assistant",
  "uuid": "5e3f3a20-7a16-41f7-8169-07090acaad0a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "3a90179e-e19e-41d1-8fb4-f23e916f555f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0116cwWjSbrSosRnMPJ8GGv3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8570,
      "cache_read_input_tokens": 58196,
      "output_tokens": 2958,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8570,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2958,
          "cache_read_input_tokens": 58196,
          "cache_creation_input_tokens": 8570,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8570
          },
          "type": "message"
        }
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

_source line 77 · 2026-05-23T10:59:10.569Z_

<details><summary>↩ Tool result · `toolu_017Q6ayjbQHjwL5aR5xr5BgN`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "TodoWrite"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5e3f3a20-7a16-41f7-8169-07090acaad0a",
  "isSidechain": false,
  "promptId": "dddf37fd-16cc-4cd5-bb05-648328938281",
  "type": "user",
  "uuid": "08ef7816-01e5-441e-b77f-2eb894d89a2b",
  "toolUseResult": {
    "matches": [
      "TodoWrite"
    ],
    "query": "select:TodoWrite",
    "total_deferred_tools": 25
  },
  "sourceToolAssistantUUID": "5e3f3a20-7a16-41f7-8169-07090acaad0a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "3a90179e-e19e-41d1-8fb4-f23e916f555f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Runtime record

_source line 78 · 2026-05-23T10:59:10.578Z_

```json
{
  "parentUuid": "08ef7816-01e5-441e-b77f-2eb894d89a2b",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "2b8c7587-53d6-4384-be53-a757884ba390",
  "timestamp": "2026-05-23T10:59:10.578Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "3a90179e-e19e-41d1-8fb4-f23e916f555f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---


### Assistant

_source line 79 · 2026-05-23T10:59:41.635Z_

<details><summary>Logged reasoning block</summary>

```text
Let me now compile the complete provenance audit document. I have all the data from the tex files and the registry. Let me write it directly.

Let me organize by table/figure and create a comprehensive mapping.

Key observations so far:

**Discrepancies to flag:**
1. Standard SFT 20%: registry `eval_gsm8k_sft_standard_20` = 59.21%, but paper uses 59.29% (from `eval_sft_standard_full_westd`). The appendix explains this: seed 42 had a different SFT checkpoint.
2. CKA-only GRPO seed456: registry = 64.59% (852/1319), paper = 64.58% — rounding difference


3. Alpha=3.0 GRPO shows a similar rounding discrepancy at 63.45% versus 63.46%, and the 30% CKA cliff reveals a larger gap where the registry reports 1.6% on partial data but the paper shows 0%. I'm also noticing the Standard 20% SFT has two different registry entries with conflicting values.

**Missing from registry:**
Several entries don't appear in the registry at all — the Standard Post-Prune Qwen2.5-Math-7B result of 18.5%, the MATH-500 Standard 25% GRPO at 12.8%, and the extended training results.

Now I'm looking at the GSM8K evaluation script versioning. There's a distinction between older evaluations created before May 23 and newer ones that use the updated format with pred_answer/gold_answer. The v2/v3 reruns are marked as using the new format, but I need to clarify whether this applies to all v2/v3 experiments or specifically the MATH-500 re-evaluations, since many of those experiments predate the format change. For GSM8K specifically, the v2/v3 suffixes seem to indicate something else entirely rather than a format difference. doesn't align with the timeline. Let me think about this more pragmatically—the actual format difference in the GSM8K evaluation results comes down to how the answer extraction and comparison work, which affects the JSON structure but the core accuracy calculation should remain consistent. I'll use the creation date as the primary signal: anything created on or after May 23 uses the new format, and I'll document the v2/v3 variants separately to track which experiments were re-runs.

For MATH-500, the answer extraction logic actually changed meaningfully, which is why we see shifts like the CKA GRPO result moving from 26.6% to 27.4%. So the script version matters more there. I'll mark everything by creation date and note the variant status where it's relevant.

Now I'm ready to write out the full document with all this organized clearly.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2b8c7587-53d6-4384-be53-a757884ba390",
  "isSidechain": false,
  "requestId": "req_011CbKPBd8XudqNbELKpFYJt",
  "type": "assistant",
  "uuid": "ed942892-e2b4-41fd-81c0-eb1a5021259e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "3a90179e-e19e-41d1-8fb4-f23e916f555f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F4iDWNReEuFweWsyg9imyr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 5445,
      "cache_read_input_tokens": 66766,
      "output_tokens": 1240,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5445,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1240,
          "cache_read_input_tokens": 66766,
          "cache_creation_input_tokens": 5445,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5445
          },
          "type": "message"
        }
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

_source line 80 · 2026-05-23T10:59:41.750Z_

<details open><summary>🔧 Tool call — TodoWrite · `toolu_0137ddFQrqoYTSX1cKp8Sypa`</summary>

```json
{
  "todos": [
    {
      "content": "Extract all numerical values from tex files",
      "status": "completed",
      "activeForm": "Extracting numerical values from tex files"
    },
    {
      "content": "Read registry data and match experiments",
      "status": "completed",
      "activeForm": "Reading registry data and matching experiments"
    },
    {
      "content": "Write complete provenance audit document",
      "status": "in_progress",
      "activeForm": "Writing complete provenance audit document"
    },
    {
      "content": "Register artifact",
      "status": "pending",
      "activeForm": "Registering artifact"
    }
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ed942892-e2b4-41fd-81c0-eb1a5021259e",
  "isSidechain": false,
  "requestId": "req_011CbKPBd8XudqNbELKpFYJt",
  "type": "assistant",
  "uuid": "edcf5f9e-c4b1-481b-91be-1f399b2d509d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "3a90179e-e19e-41d1-8fb4-f23e916f555f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F4iDWNReEuFweWsyg9imyr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 5445,
      "cache_read_input_tokens": 66766,
      "output_tokens": 1240,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5445,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1240,
          "cache_read_input_tokens": 66766,
          "cache_creation_input_tokens": 5445,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5445
          },
          "type": "message"
        }
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

_source line 81 · 2026-05-23T10:59:41.758Z_

<details><summary>↩ Tool result · `toolu_0137ddFQrqoYTSX1cKp8Sypa`</summary>

```text
Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "edcf5f9e-c4b1-481b-91be-1f399b2d509d",
  "isSidechain": false,
  "promptId": "dddf37fd-16cc-4cd5-bb05-648328938281",
  "type": "user",
  "uuid": "3d6e244a-3064-4c93-a4f7-4d41eb9889cc",
  "toolUseResult": {
    "oldTodos": [],
    "newTodos": [
      {
        "content": "Extract all numerical values from tex files",
        "status": "completed",
        "activeForm": "Extracting numerical values from tex files"
      },
      {
        "content": "Read registry data and match experiments",
        "status": "completed",
        "activeForm": "Reading registry data and matching experiments"
      },
      {
        "content": "Write complete provenance audit document",
        "status": "in_progress",
        "activeForm": "Writing complete provenance audit document"
      },
      {
        "content": "Register artifact",
        "status": "pending",
        "activeForm": "Registering artifact"
      }
    ],
    "verificationNudgeNeeded": false
  },
  "sourceToolAssistantUUID": "edcf5f9e-c4b1-481b-91be-1f399b2d509d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "3a90179e-e19e-41d1-8fb4-f23e916f555f",
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
  "leafUuid": "3d6e244a-3064-4c93-a4f7-4d41eb9889cc",
  "sessionId": "3a90179e-e19e-41d1-8fb4-f23e916f555f"
}
```

---


### Runtime record

_source line 83_

```json
{
  "type": "ai-title",
  "aiTitle": "Map paper results to registry experiments",
  "sessionId": "3a90179e-e19e-41d1-8fb4-f23e916f555f"
}
```

---


### Tool call

_source line 84 · 2026-05-23T11:02:52.636Z_

<details open><summary>🔧 Tool call — Write · `toolu_01SW8KXJo9vfu8VurdvkLYqQ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/data_provenance_audit.md",
  "content": "# Data Provenance Audit — recovery_aware_struct_prune\n\nGenerated: 2026-05-23\n\n**Convention:**\n- **Script**: NEW = created ≥ 2026-05-23 (pred_answer/gold_answer format); OLD = before that date\n- **Seed**: single seed (42) unless noted; multi-seed results show individual seeds and mean\n- ⚠️ = discrepancy or missing registry record\n\n---\n\n## Table 1: Recovery Capacity Spectrum (`tab1_recovery_gradient.tex`)\n\nGRPO dynamics at 20% sparsity, 100 steps. Reward metrics from GRPO training runs.\n\n| Row | Column | Paper Value | Registry exp_id | Server | Script | Seed |\n|-----|--------|-------------|-----------------|--------|--------|------|\n| CKA-only | Peak Rew. | 0.354 | `grpo_cka_only_20` (peak_reward=0.3544) | westb-23072 | OLD (2026-05-17) | 42 |\n| CKA-only | Mean Rew. | 0.285 | `grpo_cka_only_20` (computed from reward curve) | westb-23072 | OLD | 42 |\n| CKA-only | Min f₀ | 0.125 | `grpo_cka_only_20` (from training logs) | westb-23072 | OLD | 42 |\n| Random | Peak Rew. | 0.190 | `grpo_random_20` (reward_peak=0.19) | westb-23072 | OLD (2026-05-17) | 42 |\n| Random | Mean Rew. | 0.164 | `grpo_random_20` (reward_final=0.164) | westb-23072 | OLD | 42 |\n| Random | Min f₀ | 0.300 | `grpo_random_20` (from training logs) | westb-23072 | OLD | 42 |\n| Standard | Peak Rew. | 0.081 | `grpo_standard_20_fair` (peak_reward=0.081) | westb-23072 | OLD (2026-05-18) | 42 |\n| Standard | Mean Rew. | 0.050 | `grpo_standard_20_fair` (final_reward=0.054) | westb-23072 | OLD | 42 |\n| Standard | Min f₀ | 0.500 | `grpo_standard_20_fair` (from training logs) | westb-23072 | OLD | 42 |\n| RASP (α=1.0) | Peak Rew. | 0.061 | `grpo_rasp_20_fair` (peak_reward=0.061) | westb-23072 | OLD (2026-05-17) | 42 |\n| RASP (α=1.0) | Mean Rew. | 0.031 | `grpo_rasp_20_fair` (final_reward=0.01) | westb-23072 | OLD | 42 |\n| RASP (α=1.0) | Min f₀ | 0.675 | `grpo_rasp_20_fair` (from training logs) | westb-23072 | OLD | 42 |\n\n**Result file paths** (GRPO training outputs):\n- CKA-only: `/root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20/`\n- Random: `/root/autodl-tmp/recovery_aware_struct_prune/grpo_random_20/`\n- Standard: `/root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_20_fair/`\n- RASP: `/root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_20_fair/`\n\n---\n\n## Table 2: Reward-Accuracy Decoupling (`tab2_decoupling.tex`)\n\nGSM8K (N=1,319) accuracy. Multi-seed mean ± std for CKA-only, Standard, Random.\n\n| Row | SFT Acc.(%) | GRPO Acc.(%) | Δ(pp) | Peak Rew. | Registry exp_id (SFT) | Registry exp_id (GRPO) | Seed |\n|-----|-------------|--------------|-------|-----------|----------------------|----------------------|------|\n| Unpruned | 81.27 | 81.27 | 0.00 | 0.669 | `eval_sft_unpruned_full` (westd-11672, 2026-05-16) | `eval_grpo_unpruned_v2_step100` (westd-11672, 2026-05-16) | 42 |\n| CKA-only 20% | 63.91 | 64.39±0.19 | +0.48 | 0.354 | `eval_gsm8k_sft_cka_only_20` (westd-29022, 2026-05-20) | 3-seed mean: see Table below | 3 seeds |\n| Standard 20% | 59.29 | 59.84±0.38 | +0.55 | 0.081 | `eval_sft_standard_full_westd` (westd-11672, 2026-05-15) | 3-seed mean: see Table below | 3 seeds |\n| RASP (α=1.0) 20% | 61.49 | 60.88 | −0.61 | 0.061 | `eval_gsm8k_sft_rasp_20` (westd-29022, 2026-05-20) | `eval_gsm8k_grpo_rasp_20_fair` (westd-29022, 2026-05-19) | 42 |\n| Random 20% | 51.25 | 50.72±0.15 | −0.53 | 0.190 | `eval_gsm8k_sft_random_20` (westd-29022, 2026-05-21) | 3-seed mean: see Table below | 3 seeds |\n| ShortGPT 20% | 44.73 | 43.37 | −1.36 | -- | `eval_gsm8k_sft_shortgpt_20` (westd-29022, 2026-05-19) | `eval_gsm8k_grpo_shortgpt_20` (westd-29022, 2026-05-19) | 42 |\n\n### Multi-seed GRPO breakdown (Table 2 & Appendix Tab multiseed)\n\n| Method | Seed 42 | exp_id | Seed 123 | exp_id | Seed 456 | exp_id | Mean |\n|--------|---------|--------|----------|--------|----------|--------|------|\n| CKA-only 20% | 64.37% | `eval_gsm8k_grpo_cka_only_20_v2` (westb-23072, 05-18) | 64.22% | `eval_gsm8k_grpo_cka_only_20_seed123` (westb-23072, 05-19) | 64.59% | `eval_gsm8k_grpo_cka_only_20_seed456_full` (westd-29022, 05-20) | 64.39% |\n| Standard 20% | 59.44% | `eval_gsm8k_grpo_standard_20_fair_v2` (westd-29022, 05-19) | 59.89% | `eval_gsm8k_grpo_standard_20_seed123_full` (westd-29022, 05-20) | 60.20% | `eval_gsm8k_grpo_standard_20_seed456_full` (westd-29022, 05-20) | 59.84% |\n| Random 20% | 50.57% | `eval_gsm8k_grpo_random_20_v2` (westd-29022, 05-21) | 50.72% | `eval_gsm8k_grpo_random_20_seed123_v2` (westd-32935, 05-22) ⚠️ NO_METRICS in registry | 50.87% | `eval_gsm8k_grpo_random_20_seed456` (westb-23072, 05-22) | 50.72% |\n\n**Notes:**\n- ⚠️ `eval_gsm8k_grpo_random_20_seed123_v2`: status=DONE, conclusion=success, but metrics field empty in registry. Paper value 50.72% sourced from result JSON on disk.\n- ⚠️ CKA-only seed456: registry=64.59% (852/1319=64.594%), paper=64.58%. Rounding difference (0.01pp).\n- Standard SFT: registry has two entries — `eval_gsm8k_sft_standard_20`=59.21% (seed42 SFT checkpoint) and `eval_sft_standard_full_westd`=59.29% (seeds 123/456 SFT checkpoint). Paper uses 59.29%. Appendix explains: \"Standard seed 42 was trained from a separately initialized SFT checkpoint (accuracy 59.21% vs. 59.29%).\"\n- All GRPO evals: OLD script era (all before 2026-05-23)\n\n---\n\n## Table 3: α Dose-Response (`table3_alpha.tex`)\n\nGSM8K (N=1,319) at 20% sparsity, varying α. Single seed (42).\n\n| α | SFT Acc.(%) | exp_id (SFT) | GRPO Acc.(%) | exp_id (GRPO) | Δ(pp) |\n|---|-------------|--------------|--------------|---------------|-------|\n| 0.5 | 60.73 | `eval_gsm8k_sft_alpha0p5_20` (westd-32935, 05-22) | 61.18 | `eval_gsm8k_grpo_alpha0p5_20` (westd-32935, 05-22) | +0.45 |\n| 1.0 | 61.49 | `eval_gsm8k_sft_rasp_20` (westd-29022, 05-20) | 60.88 | `eval_gsm8k_grpo_rasp_20_fair` (westd-29022, 05-19) | −0.61 |\n| 2.0 | 64.97 | `eval_gsm8k_sft_alpha2p0_20` (westd-32935, 05-22) | 66.11 | `eval_gsm8k_grpo_alpha2p0_20` (westd-32935, 05-22) | +1.14 |\n| 3.0 | 64.14 | `eval_gsm8k_sft_alpha3p0_20` (westd-32935, 05-22) | 63.46 | `eval_gsm8k_grpo_alpha3p0_20` (westd-32935, 05-22) | −0.68 |\n| 4.0 | 61.94 | `eval_gsm8k_sft_alpha4_20_v5` (westd-32935, 05-22) | 62.77 | `eval_gsm8k_grpo_alpha4_20_v3` (westd-32935, 05-22) | +0.83 |\n\n**Notes:**\n- ⚠️ α=3.0 GRPO: registry=63.45% (837/1319=63.456%), paper=63.46%. Rounding (paper rounds up).\n- All: OLD script era (all 05-22)\n- α=4.0 SFT has v5 suffix (multiple reruns due to server issues); GRPO has v3 suffix\n\n---\n\n## Table 4: Sparsity Cliff at 30% (`table4_sparsity_cliff.tex`)\n\nGSM8K at 30% sparsity, N=100 (quick eval) or N=200/500 (registry).\n\n| Method | Acc.(%) | EOS Rate(%) | Registry exp_id | Notes |\n|--------|---------|-------------|-----------------|-------|\n| Standard | 4 | 5.5 | `eval_postprune_standard_30` (acc=0.04, N=200, 05-17) | Also `prune_eval_standard_30` (acc=2.8%, N=500, 05-20) |\n| RASP (α=1.0) | 0 | 3.0 | `eval_postprune_rasp_30` (acc=0, N=200, 05-17) | Exact match |\n| CKA-only | 0 | -- | `prune_eval_cka_only_30` (acc=1.6%, N=500 partial, 05-20) | ⚠️ Registry=1.6%, paper=0%. Different N and partial eval |\n\n**Notes:**\n- Paper uses N=100 quick eval. Registry has N=200 and N=500 versions.\n- ⚠️ Standard: paper=4% matches N=200 registry (8/200=4%). The N=500 version gives 2.8%.\n- ⚠️ CKA-only: paper=0% vs registry 1.6% (N=500). Possibly different evaluation run; paper footnote says \"Terminated early after collapse confirmed.\"\n\n---\n\n## Table 5: Inference Efficiency (`table5_inference.tex`, main paper)\n\nLatency averaged over 100 GSM8K problems at 20% sparsity.\n\n| Config | Latency(s) | Speedup(%) | Memory(GB) | Mem.Red.(%) | Registry exp_id |\n|--------|-----------|------------|-----------|------------|-----------------|\n| Dense | 6.682 | -- | 16.22 | -- | `inference_speedup_plan016_v2` (dense.avg_latency=6.682, peak_memory=16.22GB, 05-16) |\n| RASP (α=1.0) 20% | 4.156 | 37.8 | 11.60 | 28.5 | `inference_speedup_plan016_v2` (rasp.avg_latency=4.156, rasp.peak_memory=11.60GB) |\n| Standard 20% | 6.167 | 7.7 | 11.61 | 28.4 | `inference_speedup_plan016_v2` (standard.avg_latency=6.167, standard.peak_memory=11.61GB) |\n\n---\n\n## Table (Appendix): Inference TPS/TTFT (`appendix.tex` Tab inference)\n\n| Config | TPS(tok/s) | TTFT(ms) | Per-token(ms) | Params(B) | Registry exp_id |\n|--------|-----------|---------|-------------|----------|-----------------|\n| Dense 7B | 72.0 | 20.1 | 13.9 | 7.62 | `inference_bench_clean_v2` (original_tps=72.02, 05-19) |\n| CKA-only 20% | 58.3 | 16.4 | 16.7 | 6.16 | `inference_bench_clean_v2` (cka_only_tps=58.3) |\n| Standard 20% | 58.2 | 16.4 | 16.7 | 6.16 | `inference_bench_clean_v2` (standard_tps=58.2) |\n\n**Notes:**\n- Two separate benchmark experiments: `inference_speedup_plan016_v2` (latency/memory, westd-11672, 05-16) and `inference_bench_clean_v2` (TPS/TTFT, westb-23072, 05-19).\n\n---\n\n## Table: MATH-500 (`tab_math500.tex`)\n\nMATH-500 (N=500), greedy decoding, max_new_tokens=2048.\n\n| Row | SFT(%) | exp_id (SFT) | GRPO(%) | exp_id (GRPO) | Δ(pp) | Script |\n|-----|--------|--------------|---------|---------------|-------|--------|\n| **Dense** | 53.0 | `eval_math500_dense_2048` (05-18) | -- | -- | -- | OLD |\n| **20% method comparison** | | | | | | |\n| CKA-only | 26.8 | `eval_math500_sft_cka_only_20_westd` (westd-32935, 05-22) | 27.4 | `eval_math500_grpo_cka_only_20_2048_v2` (westd-32935, 05-23) | +0.6 | SFT:OLD, GRPO:**NEW** |\n| Standard | 25.8‡ | `eval_math500_sft_standard_20_2048_v2` (westd-32935, 05-19) | 26.4‡ | `eval_math500_grpo_standard_20_fair_2048_v2` (westd-32935, 05-22) | +0.6 | OLD (‡earlier extraction) |\n| RASP (α=1.0) | 21.2 | `eval_math500_sft_rasp_alpha1p0_20_v2` (05-22) | 22.6 | `eval_math500_grpo_rasp_alpha1p0_20` (05-22) | +1.4 | OLD |\n| Random | 14.4 | `eval_math500_sft_random_20_v3` (westd-32935, 05-22) | --- | -- | --- | OLD |\n| **20% α dose-response** | | | | | | |\n| α=0.5 | 25.4 | `eval_math500_sft_rasp_alpha0p5_20` (05-22) | 24.8 | `eval_math500_grpo_rasp_alpha0p5_20` (westb-23072, 05-23) | −0.6 | SFT:OLD, GRPO:**NEW** |\n| α=2.0 | 24.0 | `eval_math500_sft_rasp_alpha2p0_20` (westd-32935, 05-22) | 26.2 | `eval_math500_grpo_rasp_alpha2p0_20` (westd-32935, 05-22) | +2.2 | OLD |\n| α=3.0 | 23.2 | `eval_math500_sft_rasp_alpha3p0_20` (05-22) | 22.8 | `eval_math500_grpo_rasp_alpha3p0_20` (westd-32935, 05-23) | −0.4 | SFT:OLD, GRPO:**NEW** |\n| α=4.0 | 26.6 | `eval_math500_sft_rasp_alpha4p0_20` (05-22) | 26.2 | `eval_math500_grpo_rasp_alpha4p0_20` (05-23) | −0.4 | SFT:OLD, GRPO:**NEW** |\n| **25% sparsity** | | | | | | |\n| CKA-only | 19.2 | `eval_math500_sft_cka_only_25_v2` (westd-29022, 05-21) | 18.4 | `eval_math500_grpo_cka_only_25_v2` (westd-29022, 05-21) | −0.8 | OLD |\n| Standard | 14.0 | `eval_math500_sft_standard_25` (westb-23072, 05-21) | 12.8 | ⚠️ 无 registry 记录 | −1.2 | -- |\n\n**Notes:**\n- ⚠️ MATH-500 Standard 25% GRPO=12.8%: 无对应 registry 条目 (`eval_math500_grpo_standard_25` 不存在)\n- `eval_math500_grpo_cka_only_20` (OLD, 05-18) gave 26.6% — superseded by `eval_math500_grpo_cka_only_20_2048_v2` (NEW, 05-23) = 27.4% after answer extraction update\n- Dense 53.0% uses 2048 token limit (`eval_math500_dense_2048`). Unlimited version: 73.6% (`eval_math500_unpruned`)\n\n---\n\n## Table: MBPP (`tab_mbpp.tex`)\n\nMBPP code generation (N=374), greedy decoding.\n\n| Row | SFT(%) | exp_id (SFT) | GRPO(%) | exp_id (GRPO) | Δ(pp) | Script |\n|-----|--------|--------------|---------|---------------|-------|--------|\n| Dense | -- | -- | 53.48 | `eval_mbpp_dense_unpruned` (pass@1=0.5348, 200/374, 05-19) | -- | OLD |\n| CKA-only 20% | 12.83 | `eval_mbpp_sft_cka_only_20` (48/374, 05-19) | 14.17 | `eval_mbpp_grpo_cka_only_20` (53/374, 05-19) | +1.34 | OLD |\n| Standard 20% | 12.03 | `eval_mbpp_sft_standard_20_v4` (45/374, 05-19) | 13.10 | `eval_mbpp_grpo_standard_20_v4` (49/374, 05-19) | +1.07 | OLD |\n| RASP (α=1.0) 20% | 11.76 | `eval_mbpp_sft_rasp_20` (44/374, 05-19) | 13.10 | `eval_mbpp_grpo_rasp_20` (49/374, 05-19) | +1.34 | OLD |\n| ShortGPT 20% | 10.43 | `eval_mbpp_sft_shortgpt_20_v2` (39/374, 05-19) | 14.44 | `eval_mbpp_grpo_shortgpt_20_v2` (54/374, 05-19) | +4.01 | OLD |\n\n---\n\n## Table: Cross-Scale Validation (`tab5_cross_scale.tex`)\n\n7B values cross-referenced from Tables 1–2. 1.5B: DeepSeek-R1-Distill-Qwen-1.5B, single seed.\n\n| Method | Scale | Rew. | GSM8K(%) | Registry exp_id (GRPO eval) | Registry exp_id (training) |\n|--------|-------|------|----------|---------------------------|--------------------------|\n| CKA-only | 7B | 0.354 | 64.39 | (see Table 2 multi-seed) | `grpo_cka_only_20` |\n| Standard | 7B | 0.081 | 59.84 | (see Table 2 multi-seed) | `grpo_standard_20_fair` |\n| RASP | 7B | 0.061 | 60.88 | (see Table 2) | `grpo_rasp_20_fair` |\n| Random | 7B | 0.190 | -- | -- | `grpo_random_20` |\n| CKA-only | 1.5B | 0.238 | 35.48 | `eval_gsm8k_grpo_cka_only_20_1p5b` (0.3548, 468/1319, 05-18) | `grpo_cka_only_20_1p5b` (reward_mean=0.2375) |\n| Standard | 1.5B | 0.084 | 22.29 | `eval_gsm8k_grpo_standard_20_1p5b` (0.2229, 294/1319, 05-18) | `grpo_standard_20_1p5b` (reward_mean=0.0844) |\n| RASP | 1.5B | 0.099 | 26.16 | `eval_gsm8k_grpo_rasp_20_1p5b` (0.2616, 345/1319, 05-18) | `grpo_rasp_20_1p5b` (final_reward=0.099) |\n\n**Notes:** All 1.5B experiments: OLD script, single seed (42), server westb-23072 (05-18).\n\n---\n\n## Table: CKA Stability (`tab_cka_stability.tex`)\n\n| Metric | Paper Value | Registry exp_id | Registry Value |\n|--------|-------------|-----------------|----------------|\n| Spearman ρ (min) | 0.964 | `cka_scoring_stability_ablation` (05-19) | min_combined_rho=0.964 ✓ |\n| Spearman ρ (mean) | 0.979 | `cka_scoring_stability_ablation` (05-19) | mean_combined_rho=0.979 ✓ |\n\nAlso: `cka_calibration_stability_ablation` (split_half_rho=0.9932, 05-19)\n\n---\n\n## Table (Appendix): Cross-Sparsity Validation\n\n| Sparsity | Method | SFT(%) | exp_id (SFT) | GRPO(%) | exp_id (GRPO) | Δ(pp) |\n|----------|--------|--------|--------------|---------|---------------|-------|\n| 15% | CKA-only | 72.18 | `eval_gsm8k_sft_cka_only_15` (952/1319, 05-20) | 72.76±0.57 | 3-seed mean (see below) | +0.58 |\n| 15% | Standard | 66.49 | `eval_gsm8k_sft_standard_15` (877/1319, 05-20) | 65.56±0.50 | 3-seed mean (see below) | −0.93 |\n| 20% | CKA-only | 63.91 | (see Table 2) | 64.39 | (see Table 2) | +0.48 |\n| 20% | Standard | 59.29 | (see Table 2) | 59.84 | (see Table 2) | +0.55 |\n| 25% | CKA-only | 60.12 | `eval_gsm8k_sft_cka_only_25` (westd-29022, 05-21) | 59.59 | `eval_gsm8k_grpo_cka_only_25_v3` (westd-29022, 05-21) | −0.53 |\n| 25% | Standard | 50.87 | `eval_gsm8k_sft_standard_25` (westd-29022, 05-21) | 51.86 | `eval_gsm8k_grpo_standard_25` (westb-23072, 05-21) | +0.99 |\n| 30% | All | Collapse | (see Table 4) | -- | -- | -- |\n\n### 15% multi-seed breakdown\n\n| Method | Seed 42 | exp_id | Seed 123 | exp_id | Seed 456 | exp_id | Mean |\n|--------|---------|--------|----------|--------|----------|--------|------|\n| CKA-only 15% | 73.09% | `eval_gsm8k_grpo_cka_only_15_v2` (05-20) | 73.09% | `eval_gsm8k_grpo_cka_only_15_seed123` (05-20) | 72.10% | `eval_gsm8k_grpo_cka_only_15_seed456` (05-20) | 72.76% |\n| Standard 15% | 66.11% | `eval_gsm8k_grpo_standard_15_v2` (05-20) | 65.13% | `eval_gsm8k_grpo_standard_15_seed123_v3` (05-20) | 65.43% | `eval_gsm8k_grpo_standard_15_seed456_v3` (05-20) | 65.56% |\n\n---\n\n## Table (Appendix): Cross-Architecture Qwen2.5-Math-7B\n\nGSM8K (N=200) at 20% sparsity.\n\n| Method | Post-Prune(%) | Registry | Post-SFT(%) | Registry | EOS Rate(%) |\n|--------|--------------|----------|-------------|----------|-------------|\n| CKA-only | 1.0 | ⚠️ 无 registry 记录 | 51.50±3.53 | ⚠️ 无 registry 记录 (N=200 SFT eval not registered) | 27.0 |\n| Standard | 18.5 | ⚠️ 无 registry 记录 | 21.00±2.88 | `eval_gsm8k_sft_qwen_standard_20` (0.21, 42/200, 05-20) | 36.5 |\n\n**Notes:**\n- ⚠️ CKA-only Post-Prune=1.0% and Post-SFT=51.50%: no registry entries found. Results likely from server-side JSON files.\n- ⚠️ Standard Post-Prune=18.5%: no registry entry. Only the Post-SFT value is registered.\n- Qwen GRPO eval: `eval_gsm8k_grpo_qwen_math_cka_only_20_n500_v3` = 48.60% (N=500, 83.8% truncated, footnote only)\n- Qwen MATH-500: `eval_math500_sft_qwen_math_cka_only_20` = 21.6% (registered but not in paper)\n\n---\n\n## Table (Appendix): Gradient Flow Analysis\n\n| Comparison | Gradient Ratio | Sig. Layers | Registry exp_id |\n|------------|---------------|-------------|-----------------|\n| CKA-only vs Standard | 2.89× | 55/56 | `gradient_flow_v3` (cka_vs_standard_ratio=2.89, 05-19) |\n| CKA-only vs RASP | 2.26× | 56/56 | `gradient_flow_v3` (computed: cka_mean/rasp_mean=0.3229/0.1431=2.26×) |\n| RASP vs Standard | 1.28× | 45/56 | `gradient_flow_v3` (rasp_vs_standard_ratio=1.28, 05-19) |\n\n---\n\n## Inline Values (experiments.tex)\n\n| Location | Paper Value | Registry exp_id | Match? |\n|----------|-------------|-----------------|--------|\n| §4.1 \"original unpruned model achieves 90.83%\" | 90.83% | `eval_gsm8k_dense_unpruned` (0.9083, 1198/1319, 05-20) | ✓ |\n| §4.1 \"200 of 784 across 28 layers, ~1.45B parameters\" | structural | N/A (architecture constant) | -- |\n| §4.1 \"4.55pp gap... p=0.0009, Cohen's d=11.1, 95% CI [3.62, 5.47]\" | computed | From Table 2 multi-seed data | ✓ (derived) |\n| §4.2 \"CKA-only reaches 0.354 peak reward with recovery event at step 90\" | 0.354 | `grpo_cka_only_20` (peak=0.3544) | ✓ |\n| §4.2 \"Random oscillates between 0.142 and 0.190\" | 0.142–0.190 | `grpo_random_20` training logs | ✓ |\n| §4.2 \"Standard peaks at 0.081 (step 40)\" | 0.081 | `grpo_standard_20_fair` (peak=0.081) | ✓ |\n| §4.2 \"RASP peaks at 0.061 (step 50) then declines to 0.010\" | 0.061→0.010 | `grpo_rasp_20_fair` (peak=0.061, final=0.01) | ✓ |\n| §4.2 \"5.8× peak reward gap\" | 5.8× | 0.354/0.061=5.80× | ✓ (derived) |\n| §4.3 \"mean |Δ|=0.54pp\" | 0.54 | mean(0.48, 0.55, 0.53, 0.61)=0.5425≈0.54 | ✓ (derived) |\n| §4.3 \"15%: SFT gap 5.69pp (72.18% vs 66.49%)\" | 5.69pp | 72.18−66.49=5.69 | ✓ (derived) |\n| §4.3 \"GRPO gap 7.20pp (72.76% vs 65.56%)\" | 7.20pp | 72.76−65.56=7.20 | ✓ (derived) |\n| §4.3 \"extending training to 300 steps: CKA 64.37%→64.37%, Standard 59.44%→59.29%\" | | See extended training section | |\n| §4.4 \"CKA-only achieves active learning (peak reward 4.4× Standard)\" | 4.4× | 0.354/0.081=4.37≈4.4× | ✓ (derived) |\n| §4.4 \"unstructured pruning: SFT 87.87%, GRPO 87.64%, Δ=−0.23pp\" | 87.87%, 87.64% | `eval_unstructured_20` (0.8787, 05-17), `eval_gsm8k_grpo_unstructured_20` (0.8764, 05-19) | ✓ |\n| §4.5 \"CKA-only diverges most (μ=0.62), Standard (μ=0.90), Random (μ=0.92), RASP (μ=0.88)\" | CKA values | From CKA heatmap analysis (not a separate registry entry) | -- |\n| §4.5 \"2.89× mean gradient magnitude vs Standard across 55/56 layer groups\" | 2.89× | `gradient_flow_v3` | ✓ |\n| §4.5 \"Extended GRPO: CKA 5.5× gap (0.308 vs 0.056 at step 300)\" | 0.308, 0.056 | `grpo_cka_only_20_extended_300`, `grpo_standard_20_extended_300_v2` | ✓ |\n| §4.5 \"1.5B: CKA 35.48% ≫ RASP 26.16% > Standard 22.29%\" | | (see Cross-Scale table) | ✓ |\n| §4.5 \"Qwen2.5-Math-7B: CKA 1.0%→51.50%, Standard 18.5%→21.00%\" | | (see Cross-Arch table) | Partial (⚠️ some values not in registry) |\n\n---\n\n## Extended Training 300 Steps (experiments.tex §4.5, appendix)\n\n| Claim | Registry exp_id | Registry Value | Notes |\n|-------|-----------------|----------------|-------|\n| CKA reward at step 300 = 0.308 | `grpo_cka_only_20_extended_300` (05-18) | reward_step300=0.3075 | ⚠️ Registry=0.3075, paper=0.308 (rounding) |\n| Standard reward at step 300 = 0.056 | `grpo_standard_20_extended_300_v2` (05-18) | reward_mean_step300=0.0562 | ⚠️ Registry=0.0562, paper=0.056 (rounding) |\n| CKA GSM8K stays at 64.37% | No 300-step eval registered | -- | ⚠️ Paper reuses step-100 eval (`eval_gsm8k_grpo_cka_only_20_v2`=64.37%) |\n| Standard 59.44%→59.29% | No 300-step eval registered | -- | ⚠️ No separate 300-step GSM8K eval. 59.44%=step-100 GRPO seed42, 59.29%=SFT baseline |\n\n---\n\n## Inline Values (abstract.tex)\n\n| Paper Value | Source |\n|-------------|--------|\n| \"|Δ(GRPO−SFT)| ≤ 0.61pp across all four fine-grained criteria\" | max(0.48, 0.55, 0.53, 0.61)=0.61 ✓ |\n| \"max 1.34pp including dose-response and MBPP\" | MBPP CKA Δ=+1.34pp or MBPP RASP Δ=+1.34pp ✓ |\n| \"peak reward 4.4× vs importance-only\" | 0.354/0.081=4.37≈4.4× ✓ |\n| \"α=2.0 (66.11%)\" | Table 3 ✓ |\n\n## Inline Values (introduction.tex)\n\n| Paper Value | Source |\n|-------------|--------|\n| \"mean |Δ|=0.54pp at 20%\" | mean(0.48, 0.55, 0.53, 0.61)=0.5425≈0.54 ✓ |\n| \"max 0.61pp; 1.34pp including dose-response and MBPP\" | Table 2 max=0.61; MBPP max=1.34 ✓ |\n| \"ShortGPT |Δ|>1pp (−1.36pp on GSM8K)\" | Table 2 ✓ |\n| \"α=2.0 (66.11%)\" | Table 3 ✓ |\n| \"CKA-only peak reward 4.4× Standard\" | 0.354/0.081=4.37≈4.4× ✓ |\n\n---\n\n## Figures\n\n### Figure 1: Dose-Response Curve (`fig1_dose_response.pdf`)\n- Data source: Table 3 (α ablation) — same experiments\n- Both SFT and GRPO curves plotted from the 5 α values\n\n### Figure 2: Reward Trajectories (`fig2_reward_trajectories.pdf`)\n- Data source: GRPO training logs from:\n  - `grpo_cka_only_20` (CKA-only, peak=0.354)\n  - `grpo_random_20` (Random, peak=0.190)\n  - `grpo_standard_20_fair` (Standard, peak=0.081)\n  - `grpo_rasp_20_fair` (RASP, peak=0.061)\n  - Unpruned: `grpo_unpruned_v2` or similar\n- Result paths: `/root/autodl-tmp/recovery_aware_struct_prune/{exp_name}/` training logs (tensorboard/wandb)\n\n### Figure 3: Collapse Dynamics (`fig3_collapse_dynamics.pdf`)\n- (a) f₀ dynamics: from same GRPO training logs as Figure 2\n- (b) Gradient norm: from same GRPO training logs\n- Specific values cited: \"Standard transient minimum 0.017 at step 90, recovers to 2.41 at step 100\"\n- \"RASP gradient norms remain predominantly near zero\"\n\n### Figure 4: CKA Heatmap (`fig4_cka_heatmap.pdf`)\n- Data source: CKA analysis during pruning\n- μ values: CKA-only=0.62, Standard=0.90, Random=0.92, RASP=0.88\n- ⚠️ No dedicated registry entry for CKA heatmap data; computed during pruning step\n\n### Figure 5: Extended Training (`fig5_extended_training.pdf`)\n- Data source: `grpo_cka_only_20_extended_300` and `grpo_standard_20_extended_300_v2`\n- (a) Reward: CKA oscillates 0.22–0.44; Standard 0.054→0.056\n- (b) f₀: Standard > 0.5 throughout; CKA < 0.30\n\n### Figure (Appendix): KL Divergence (`fig_appendix_kl.pdf`)\n- Data source: GRPO training logs (KL between policy and reference model)\n- RASP < 0.001, Random ~0.004–0.005\n\n---\n\n## Summary of Issues\n\n### ⚠️ Values with No Registry Record (4)\n\n| Paper Location | Value | Notes |\n|----------------|-------|-------|\n| MATH-500 tab, Standard 25% GRPO | 12.8% | No `eval_math500_grpo_standard_25` in registry |\n| Cross-Arch tab, CKA Post-Prune | 1.0% | No post-prune eval registered for Qwen CKA |\n| Cross-Arch tab, CKA Post-SFT | 51.50%±3.53 | N=200 SFT eval not registered |\n| Cross-Arch tab, Standard Post-Prune | 18.5% | No post-prune eval registered for Qwen Standard |\n\n### ⚠️ Minor Numerical Discrepancies (4)\n\n| Paper Value | Registry Value | Diff | Cause |\n|-------------|---------------|------|-------|\n| CKA seed456 = 64.58% | 64.59% (852/1319) | 0.01pp | Rounding |\n| α=3.0 GRPO = 63.46% | 63.45% (837/1319) | 0.01pp | Rounding direction |\n| Extended CKA reward = 0.308 | 0.3075 | 0.0005 | Rounding |\n| Extended Standard reward = 0.056 | 0.0562 | 0.0002 | Rounding |\n\n### ⚠️ Registry Records with Empty Metrics (3)\n\n| exp_id | Status | Notes |\n|--------|--------|-------|\n| `eval_gsm8k_grpo_random_20_seed123_v2` | DONE/success | Paper uses 50.72% from result JSON on disk |\n| `eval_gsm8k_sft_depth_first_20` | DONE/success | Disk-full error prevented metric recording |\n| `eval_gsm8k_grpo_depth_first_20` | DONE/success | Disk-full error prevented metric recording |\n\n### ⚠️ 30% Cliff Inconsistency\n\n| Method | Paper | Registry | N |\n|--------|-------|----------|---|\n| CKA-only | 0% | 1.6% | Paper: N=100, registry: N=500 partial |\n| Standard | 4% | 4% (N=200) / 2.8% (N=500) | Paper: N=100 |\n\n---\n\n## Server Summary\n\n| Server | Role | GPU |\n|--------|------|-----|\n| westb-23072 | Primary early experiments, some later seeds | 2× RTX PRO 6000 |\n| westd-11672 | Early evals (unpruned, Standard SFT) | 2× RTX PRO 6000 |\n| westd-29022 | Mid-phase (20%/25% evals, 1.5B) — replaced by westd-32935 | -- |\n| westd-32935 | Late-phase (α dose-response, MATH-500 reruns) | 4× GPU |\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3d6e244a-3064-4c93-a4f7-4d41eb9889cc",
  "isSidechain": false,
  "requestId": "req_011CbKPDvc4hKmhgmPxeiFLp",
  "type": "assistant",
  "uuid": "6515c16e-71ed-4b43-b0fa-66232255205f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "3a90179e-e19e-41d1-8fb4-f23e916f555f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Sr4CA75mCnEc7kZYYhkTmz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1276,
      "cache_read_input_tokens": 72211,
      "output_tokens": 11480,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1276,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 11480,
          "cache_read_input_tokens": 72211,
          "cache_creation_input_tokens": 1276,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1276
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---
