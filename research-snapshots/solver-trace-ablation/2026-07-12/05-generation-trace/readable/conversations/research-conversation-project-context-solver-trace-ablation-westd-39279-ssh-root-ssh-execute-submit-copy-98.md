# Research conversation: <project_context> # 项目: solver-trace-ablation ## 运行环境 - 服务器名: westd-39279 - SSH 账户: root（调用 ssh_execute / submit_trainin

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 93
- **Recorded user turns:** 1
- **Tool calls:** 29
- **Original source:** `logs/chats/exported-trajectories/account-2/24e67ff1-1ea3-4bcf-a9e3-703eaa6cb36e.jsonl`
- **Structured JSON:** [`041d87c73b0d94a0581d.json`](../../sessions/04/041d87c73b0d94a0581d.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-14T21:44:36.831Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-14T21:44:36.831Z",
  "sessionId": "24e67ff1-1ea3-4bcf-a9e3-703eaa6cb36e",
  "content": "&lt;project_context>\n# 项目: solver-trace-ablation\n\n## 运行环境\n- 服务器名: westd-39279\n- SSH 账户: root（调用 ssh_execute / submit_training_job 时传入 account=\"root\"）\n- SSH 连接命令: ssh connect.westd.seetacloud.com  # 必须用此命令，~/.ssh/config 自动应用密钥和跳板机，禁止用裸 IP\n- 项目代码根目录: /root/solver-trace-ablation\n\n## ⚠️ 活跃约束（必须遵守）\n\n- **C001**: 所有实验统一使用 data/train_500_seed42.jsonl 作为训练数据，禁止使用 proofwriter_fol_500.jsonl 或其他数据文件（原因：Reviewer CRITICAL: plan001-s43 使用了不同数据文件导致多 seed 对比 confound。多 seed 实验必须控制数据变量，seed 仅控制模型初始化和训练随机性。）\n- **C002**: 提交训练任务前必须用 export CUDA_VISIBLE_DEVICES=N 显式设置 GPU，禁止 inline 赋值（bash -c VAR=X cmd），提交后验证 nvidia-smi 确认只占用分配的 GPU（原因：plan013 因 CUDA_VISIBLE_DEVICES inline 赋值引号问题越界占用两张 GPU，导致 plan001-s43 OOM 死亡。这是第二次 GPU 冲突事故。）\n- **C003**: 训练配置必须设置 save_total_limit=1 且禁用/限制 completions parquet 保存，防止磁盘耗尽（原因：plan013-r3 和 plan001-s43-r3 因磁盘 250G/250G 满导致 step 23/28 崩溃。根因：TRL 每实验保存 3 份模型权重（~48GB）+ completions parquet（~2.5GB）。）\n- **C004**: 跨 seed/跨 run 的 ISR 对比必须使用 eval_sta.py 统一评估，禁止引用训练日志 ISR 做跨 run 对比（不同 run 可能使用不同版本的 ISR 计算代码）（原因：Reviewer 核实发现 plan001-s42-r2 训练日志 ISR 使用 binary _fast_fn，plan001-s43-r4 使用 full STA _full_fn，同一指标名下计算方法不同导致不可比。论文中所有 ISR 数据必须来自 eval_sta.py 统一评估。）\n- **C005**: 所有 worker（含 fix/ops 类）启动任何 Python 进程前必须显式设置 CUDA_VISIBLE_DEVICES，禁止裸跑（原因：fix worker 未设 CUDA_VISIBLE_DEVICES 导致测试进程泄漏到 cuda:1（plan017 训练卡），占用 8638 MiB 显存。2026-05-14 事故。）\n- **C006**: 论文讨论 ISR 时必须区分两种语义：exec-only 的 low ISR = 冗余编码（重复 ground facts 导致 n_necessary=0），exec+STA 的 high ISR = metric gaming（Goodhart 效应）。不可将 ISR 差异直接等同于 reasoning 能力差异。（原因：Reviewer 发现 Prolog exec-only 生成大量重复 ground facts（如 penguin(fido). 出现 3 次），per-clause ablation 下删任一重复不影响结果，ISR=0。这是冗余不是无推理。如不区分，审稿人会误读 ISR 差异。）\n\n\n## 环境搭建\n连接服务器后先调 `detect_image` 检测是否为预置镜像。如果匹配，跳过基础环境搭建，只装项目特有依赖。已预装的包不要重复安装。\n\n## 输出风格\n回复简洁直接。只输出执行结果和必要信息，不要解释过程、不要客套、不要给未被要求的建议。\n&lt;/project_context>\n## 任务：论文数据一致性审查\n\n你需要交叉检查论文中所有定量 claim 与 registry 中实验数据的一致性。\n\n### 文件位置\n- 论文目录：`/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/`\n  - abstract.tex, introduction.tex, method.tex, experiments.tex, conclusion.tex, related_work.tex, appendix.tex\n- paper_framing.md: `/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper_framing.md`\n\n### 审查清单\n\n**1. 数字一致性（最关键）**\n读取 registry 中所有 success 实验的 metrics，逐一核对论文中引用的数字：\n- ISR 崩塌轨迹：0.642 → 0.132 → 0.003（对应 plan003, plan001-s42-r2, plan016）\n- PR 轨迹：32% → 93% → 96%\n- ISR β=0.1 三 seed 数字（Table 1 和 experiments section）\n- Random β=0.1 三 seed 数字\n- SFT baseline：PR=14%, ISR=0.571, Genuine=92.9%\n- Prolog 数字（Table 5/appendix）\n- 1000-step：ISR=0.003, 94.8% ISR=0, mean components 18.55\n- H7/H1/Genuine 百分比\n\n**2. 硬约束检查（来自 paper_framing.md 和 ROADMAP）**\n- D051: 2.4x ISR 优势已作废 → 论文中不能出现 \"2.4x\" 作为优势\n- s44 Prolog STA: query-as-fact gaming，不是 genuine → 检查论文是否正确标记\n- Hacking taxonomy: 必须是 7 种（含 query-as-fact）→ 论文中不能说 6 种\n- ISR β=0.1 hacking rate 69.1% → 不标 \"no hacking\"，标 \"lowest hacking rate\"\n- plan013 vs plan017 不可简化为 \"additive vs convex\" 对照\n\n**3. 论文结构检查**\n- Abstract/Introduction 的 claim 是否与 Experiments 的结论一致\n- 交叉引用（Figure/Table ref）是否正确\n- 写作约束（见 paper_framing.md）是否遵守\n\n### 产出\n写审查报告到 `/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/data_consistency_report.md`：\n1. 每个数字的核对结果\n2. 硬约束违反（如果有）\n3. 内部不一致（如果有）\n4. 总结和建议修改"
}
```

---

### Runtime record

_source line 2 · 2026-05-14T21:44:36.834Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-14T21:44:36.834Z",
  "sessionId": "24e67ff1-1ea3-4bcf-a9e3-703eaa6cb36e"
}
```

---

## Round 1

91 recorded events

### User

_source line 3 · 2026-05-14T21:44:36.873Z_

&lt;project_context>
# 项目: solver-trace-ablation

## 运行环境
- 服务器名: westd-39279
- SSH 账户: root（调用 ssh_execute / submit_training_job 时传入 account="root"）
- SSH 连接命令: ssh connect.westd.seetacloud.com  # 必须用此命令，~/.ssh/config 自动应用密钥和跳板机，禁止用裸 IP
- 项目代码根目录: /root/solver-trace-ablation

## ⚠️ 活跃约束（必须遵守）

- **C001**: 所有实验统一使用 data/train_500_seed42.jsonl 作为训练数据，禁止使用 proofwriter_fol_500.jsonl 或其他数据文件（原因：Reviewer CRITICAL: plan001-s43 使用了不同数据文件导致多 seed 对比 confound。多 seed 实验必须控制数据变量，seed 仅控制模型初始化和训练随机性。）
- **C002**: 提交训练任务前必须用 export CUDA_VISIBLE_DEVICES=N 显式设置 GPU，禁止 inline 赋值（bash -c VAR=X cmd），提交后验证 nvidia-smi 确认只占用分配的 GPU（原因：plan013 因 CUDA_VISIBLE_DEVICES inline 赋值引号问题越界占用两张 GPU，导致 plan001-s43 OOM 死亡。这是第二次 GPU 冲突事故。）
- **C003**: 训练配置必须设置 save_total_limit=1 且禁用/限制 completions parquet 保存，防止磁盘耗尽（原因：plan013-r3 和 plan001-s43-r3 因磁盘 250G/250G 满导致 step 23/28 崩溃。根因：TRL 每实验保存 3 份模型权重（~48GB）+ completions parquet（~2.5GB）。）
- **C004**: 跨 seed/跨 run 的 ISR 对比必须使用 eval_sta.py 统一评估，禁止引用训练日志 ISR 做跨 run 对比（不同 run 可能使用不同版本的 ISR 计算代码）（原因：Reviewer 核实发现 plan001-s42-r2 训练日志 ISR 使用 binary _fast_fn，plan001-s43-r4 使用 full STA _full_fn，同一指标名下计算方法不同导致不可比。论文中所有 ISR 数据必须来自 eval_sta.py 统一评估。）
- **C005**: 所有 worker（含 fix/ops 类）启动任何 Python 进程前必须显式设置 CUDA_VISIBLE_DEVICES，禁止裸跑（原因：fix worker 未设 CUDA_VISIBLE_DEVICES 导致测试进程泄漏到 cuda:1（plan017 训练卡），占用 8638 MiB 显存。2026-05-14 事故。）
- **C006**: 论文讨论 ISR 时必须区分两种语义：exec-only 的 low ISR = 冗余编码（重复 ground facts 导致 n_necessary=0），exec+STA 的 high ISR = metric gaming（Goodhart 效应）。不可将 ISR 差异直接等同于 reasoning 能力差异。（原因：Reviewer 发现 Prolog exec-only 生成大量重复 ground facts（如 penguin(fido). 出现 3 次），per-clause ablation 下删任一重复不影响结果，ISR=0。这是冗余不是无推理。如不区分，审稿人会误读 ISR 差异。）


## 环境搭建
连接服务器后先调 `detect_image` 检测是否为预置镜像。如果匹配，跳过基础环境搭建，只装项目特有依赖。已预装的包不要重复安装。

## 输出风格
回复简洁直接。只输出执行结果和必要信息，不要解释过程、不要客套、不要给未被要求的建议。
&lt;/project_context>
## 任务：论文数据一致性审查

你需要交叉检查论文中所有定量 claim 与 registry 中实验数据的一致性。

### 文件位置
- 论文目录：`/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/`
  - abstract.tex, introduction.tex, method.tex, experiments.tex, conclusion.tex, related_work.tex, appendix.tex
- paper_framing.md: `/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper_framing.md`

### 审查清单

**1. 数字一致性（最关键）**
读取 registry 中所有 success 实验的 metrics，逐一核对论文中引用的数字：
- ISR 崩塌轨迹：0.642 → 0.132 → 0.003（对应 plan003, plan001-s42-r2, plan016）
- PR 轨迹：32% → 93% → 96%
- ISR β=0.1 三 seed 数字（Table 1 和 experiments section）
- Random β=0.1 三 seed 数字
- SFT baseline：PR=14%, ISR=0.571, Genuine=92.9%
- Prolog 数字（Table 5/appendix）
- 1000-step：ISR=0.003, 94.8% ISR=0, mean components 18.55
- H7/H1/Genuine 百分比

**2. 硬约束检查（来自 paper_framing.md 和 ROADMAP）**
- D051: 2.4x ISR 优势已作废 → 论文中不能出现 "2.4x" 作为优势
- s44 Prolog STA: query-as-fact gaming，不是 genuine → 检查论文是否正确标记
- Hacking taxonomy: 必须是 7 种（含 query-as-fact）→ 论文中不能说 6 种
- ISR β=0.1 hacking rate 69.1% → 不标 "no hacking"，标 "lowest hacking rate"
- plan013 vs plan017 不可简化为 "additive vs convex" 对照

**3. 论文结构检查**
- Abstract/Introduction 的 claim 是否与 Experiments 的结论一致
- 交叉引用（Figure/Table ref）是否正确
- 写作约束（见 paper_framing.md）是否遵守

### 产出
写审查报告到 `/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/data_consistency_report.md`：
1. 每个数字的核对结果
2. 硬约束违反（如果有）
3. 内部不一致（如果有）
4. 总结和建议修改

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "c33bf5b5-c338-4f2f-97b8-e3e6d5f92819",
  "type": "user",
  "uuid": "e525ea66-0eed-46e5-8403-6dc33b13de94",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "24e67ff1-1ea3-4bcf-a9e3-703eaa6cb36e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-14T21:44:36.872Z_

```json
{
  "parentUuid": "e525ea66-0eed-46e5-8403-6dc33b13de94",
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
  "uuid": "c2a87784-d983-40e0-a0b5-1c18b8603c9e",
  "timestamp": "2026-05-14T21:44:36.872Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "24e67ff1-1ea3-4bcf-a9e3-703eaa6cb36e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-14T21:44:36.872Z_

```json
{
  "parentUuid": "c2a87784-d983-40e0-a0b5-1c18b8603c9e",
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
  "uuid": "6c356f35-8010-4e55-a31c-ebb0a239dd18",
  "timestamp": "2026-05-14T21:44:36.872Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "24e67ff1-1ea3-4bcf-a9e3-703eaa6cb36e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6 · 2026-05-14T21:44:36.872Z_

```json
{
  "parentUuid": "6c356f35-8010-4e55-a31c-ebb0a239dd18",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "318b665a-984e-4314-a88b-246517b813f7",
  "timestamp": "2026-05-14T21:44:36.872Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "24e67ff1-1ea3-4bcf-a9e3-703eaa6cb36e",
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
  "aiTitle": "Audit paper figures against experiment registry",
  "sessionId": "24e67ff1-1ea3-4bcf-a9e3-703eaa6cb36e"
}
```

---

### Assistant

_source line 8 · 2026-05-14T21:44:39.548Z_

<details><summary>Logged reasoning block</summary>

```text

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "318b665a-984e-4314-a88b-246517b813f7",
  "isSidechain": false,
  "requestId": "req_011Cb3C84mBxBJeaJB2vAJnd",
  "type": "assistant",
  "uuid": "59b0a2b8-fb13-457a-b14a-3c69eeb83692",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "24e67ff1-1ea3-4bcf-a9e3-703eaa6cb36e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01KJizNjDUCTCXTKKj7Ddz6G",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 15888,
      "cache_read_input_tokens": 15491,
      "output_tokens": 292,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15888,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6,
          "output_tokens": 292,
          "cache_read_input_tokens": 15491,
          "cache_creation_input_tokens": 15888,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15888
          },
          "type": "message"
        }
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

_source line 9 · 2026-05-14T21:44:40.502Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01SYfVykuL5tuc35CkjFQTFy`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/",
  "description": "List paper directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "59b0a2b8-fb13-457a-b14a-3c69eeb83692",
  "isSidechain": false,
  "requestId": "req_011Cb3C84mBxBJeaJB2vAJnd",
  "type": "assistant",
  "uuid": "52b18a8a-85bf-4698-9eb6-8aa2dadceeca",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "24e67ff1-1ea3-4bcf-a9e3-703eaa6cb36e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01KJizNjDUCTCXTKKj7Ddz6G",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 15888,
      "cache_read_input_tokens": 15491,
      "output_tokens": 292,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15888,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6,
          "output_tokens": 292,
          "cache_read_input_tokens": 15491,
          "cache_creation_input_tokens": 15888,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15888
          },
          "type": "message"
        }
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

_source line 10 · 2026-05-14T21:44:40.951Z_

<details><summary>↩ Tool result · `toolu_01SYfVykuL5tuc35CkjFQTFy`</summary>

```text
_pdf_images
abstract.tex
acl.sty
acl_natbib.bst
appendix.tex
conclusion.tex
experiments.tex
figures
introduction.tex
main.aux
main.bbl
main.blg
main.log
main.out
main.pdf
main.tex
method.tex
paper.aux
paper.bbl
paper.blg
paper.log
paper.out
paper.pdf
paper.tex
references.bib
related_work.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "52b18a8a-85bf-4698-9eb6-8aa2dadceeca",
  "isSidechain": false,
  "promptId": "c33bf5b5-c338-4f2f-97b8-e3e6d5f92819",
  "type": "user",
  "uuid": "e3f78d37-b0d4-4004-b3a0-92fa72dc72fb",
  "toolUseResult": {
    "stdout": "_pdf_images\nabstract.tex\nacl.sty\nacl_natbib.bst\nappendix.tex\nconclusion.tex\nexperiments.tex\nfigures\nintroduction.tex\nmain.aux\nmain.bbl\nmain.blg\nmain.log\nmain.out\nmain.pdf\nmain.tex\nmethod.tex\npaper.aux\npaper.bbl\npaper.blg\npaper.log\npaper.out\npaper.pdf\npaper.tex\nreferences.bib\nrelated_work.tex",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "52b18a8a-85bf-4698-9eb6-8aa2dadceeca",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "24e67ff1-1ea3-4bcf-a9e3-703eaa6cb36e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-14T21:44:41.059Z_

<details open><summary>🔧 Tool call — Bash · `toolu_016m51yp5JprHFuYTeuCddpk`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/",
  "description": "List project root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e3f78d37-b0d4-4004-b3a0-92fa72dc72fb",
  "isSidechain": false,
  "requestId": "req_011Cb3C84mBxBJeaJB2vAJnd",
  "type": "assistant",
  "uuid": "1c317d90-14ff-41b8-90a1-479fff278974",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "24e67ff1-1ea3-4bcf-a9e3-703eaa6cb36e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01KJizNjDUCTCXTKKj7Ddz6G",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 15888,
      "cache_read_input_tokens": 15491,
      "output_tokens": 292,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15888,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6,
          "output_tokens": 292,
          "cache_read_input_tokens": 15491,
          "cache_creation_input_tokens": 15888,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15888
          },
          "type": "message"
        }
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

_source line 12 · 2026-05-14T21:44:41.212Z_

<details><summary>↩ Tool result · `toolu_016m51yp5JprHFuYTeuCddpk`</summary>

```text
AGENTS.md
ROADMAP.lock
ROADMAP.md
artifacts
checkpoints
constraints.lock
constraints.yaml
decisions.lock
decisions.yaml
docs
dream_registry.lock
dream_registry.yaml
dream_registry.yaml.bak
experiment_plan.lock
experiment_plan.yaml
figures
literature_map.yaml
logs
memory.md
paper
paper_framing.md
paper_provenance.lock
paper_provenance.yaml
registry.lock
registry.yaml
report.md
study_status.lock
task_context
writing_plan.yaml
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1c317d90-14ff-41b8-90a1-479fff278974",
  "isSidechain": false,
  "promptId": "c33bf5b5-c338-4f2f-97b8-e3e6d5f92819",
  "type": "user",
  "uuid": "c63a502b-2bb8-429e-8652-5807df6495ce",
  "toolUseResult": {
    "stdout": "AGENTS.md\nROADMAP.lock\nROADMAP.md\nartifacts\ncheckpoints\nconstraints.lock\nconstraints.yaml\ndecisions.lock\ndecisions.yaml\ndocs\ndream_registry.lock\ndream_registry.yaml\ndream_registry.yaml.bak\nexperiment_plan.lock\nexperiment_plan.yaml\nfigures\nliterature_map.yaml\nlogs\nmemory.md\npaper\npaper_framing.md\npaper_provenance.lock\npaper_provenance.yaml\nregistry.lock\nregistry.yaml\nreport.md\nstudy_status.lock\ntask_context\nwriting_plan.yaml",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "1c317d90-14ff-41b8-90a1-479fff278974",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "24e67ff1-1ea3-4bcf-a9e3-703eaa6cb36e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-14T21:44:43.929Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_013JPyJU7SSDD1pgRcXCR1pm`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__read_project_file",
  "max_results": 5
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c63a502b-2bb8-429e-8652-5807df6495ce",
  "isSidechain": false,
  "requestId": "req_011Cb3C8PHRT7nkRUcUp8Yoc",
  "type": "assistant",
  "uuid": "9674f043-eef9-4e9d-acfc-936d9c266a2b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "24e67ff1-1ea3-4bcf-a9e3-703eaa6cb36e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01CpU5qqRwaswHzYDWfFcibx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 728,
      "cache_read_input_tokens": 31379,
      "output_tokens": 124,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 728,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 124,
          "cache_read_input_tokens": 31379,
          "cache_creation_input_tokens": 728,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 728
          },
          "type": "message"
        }
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

_source line 14 · 2026-05-14T21:44:43.937Z_

<details><summary>↩ Tool result · `toolu_013JPyJU7SSDD1pgRcXCR1pm`</summary>

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
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9674f043-eef9-4e9d-acfc-936d9c266a2b",
  "isSidechain": false,
  "promptId": "c33bf5b5-c338-4f2f-97b8-e3e6d5f92819",
  "type": "user",
  "uuid": "f82002c2-01ca-4c9a-b093-3a927a3c0709",
  "toolUseResult": {
    "matches": [
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__read_project_file"
    ],
    "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__read_project_file",
    "total_deferred_tools": 25
  },
  "sourceToolAssistantUUID": "9674f043-eef9-4e9d-acfc-936d9c266a2b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "24e67ff1-1ea3-4bcf-a9e3-703eaa6cb36e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-14T21:44:47.041Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01WgA8fkiqDyjSFoFNtJmHxQ`</summary>

```json
{
  "project": "solver-trace-ablation",
  "filters": {
    "status": "success"
  }
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f82002c2-01ca-4c9a-b093-3a927a3c0709",
  "isSidechain": false,
  "requestId": "req_011Cb3C8bB3LdXooyvKQdh4B",
  "type": "assistant",
  "uuid": "a6f15bdf-889e-4e79-8fcd-a36687cb7380",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "24e67ff1-1ea3-4bcf-a9e3-703eaa6cb36e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01NsuGi8cy6P1GPptpPDBZjH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 17642,
      "cache_read_input_tokens": 15584,
      "output_tokens": 230,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 17642,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6,
          "output_tokens": 230,
          "cache_read_input_tokens": 15584,
          "cache_creation_input_tokens": 17642,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 17642
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "tools_changed",
        "cache_missed_input_tokens": 29281
      }
    }
  }
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-14T21:44:47.351Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_018UB4uYHm6z1edW3ybtfQGF`</summary>

```json
{
  "project": "solver-trace-ablation",
  "file": "paper_framing.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a6f15bdf-889e-4e79-8fcd-a36687cb7380",
  "isSidechain": false,
  "requestId": "req_011Cb3C8bB3LdXooyvKQdh4B",
  "type": "assistant",
  "uuid": "96e453d9-eb1f-491b-9064-064872f106f1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "24e67ff1-1ea3-4bcf-a9e3-703eaa6cb36e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01NsuGi8cy6P1GPptpPDBZjH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 17642,
      "cache_read_input_tokens": 15584,
      "output_tokens": 230,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 17642,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6,
          "output_tokens": 230,
          "cache_read_input_tokens": 15584,
          "cache_creation_input_tokens": 17642,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 17642
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "tools_changed",
        "cache_missed_input_tokens": 29281
      }
    }
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-14T21:44:47.566Z_

<details><summary>↩ Tool result · `toolu_01WgA8fkiqDyjSFoFNtJmHxQ`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.5021}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a6f15bdf-889e-4e79-8fcd-a36687cb7380",
  "isSidechain": false,
  "promptId": "c33bf5b5-c338-4f2f-97b8-e3e6d5f92819",
  "type": "user",
  "uuid": "06232b72-5418-49e3-871e-1a8a30f8064b",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {}, \\\"count\\\": 0, \\\"total\\\": 0, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.5021}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.5021}}"
    }
  },
  "sourceToolAssistantUUID": "a6f15bdf-889e-4e79-8fcd-a36687cb7380",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "24e67ff1-1ea3-4bcf-a9e3-703eaa6cb36e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-14T21:44:47.593Z_

<details><summary>↩ Tool result · `toolu_018UB4uYHm6z1edW3ybtfQGF`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper_framing.md\", \"content\": \"# Paper Framing — solver-trace-ablation\\n\\n## Target Venue\\n- Primary: EMNLP 2026 Main (NLP and Symbolic Reasoning track)\\n- Fallback: EMNLP 2026 Findings\\n- Deadline: ARR May 25, 2026\\n\\n## Core Claims (3 条 — Goodhart 主线诊断/分析论文)\\n\\n| Claim | Status | 闭环标志 |\\n|-------|--------|----------|\\n| Claim 1: STA 诊断能力 | ✅ 已闭环 | 3-seed + 1000-step + hacking taxonomy (7 modes) |\\n| Claim 2: Goodhart / ISR 无结构优势 | ✅ 已闭环 (D057) | 3-seed ISR + 3-seed random + premise-count-matched + SFT baseline |\\n| Claim 3: 跨逻辑泛化 | ✅ 已闭环 | exec-only 3-seed (D056) + STA 3-seed: **3/3 gaming** — 三种不同 gaming 路径 (H7/degenerate-syntax/query-as-fact) |\\n\\n### Claim 1: ISR as Reward Hacking Diagnostic ✅\\nSolver Trace Ablation (STA) derives ISR (Intensional Structural Reward) via component necessity testing (leave-one-out ablation on solver inputs). ISR detects reward hacking that prove_rate alone misses: exec-only GRPO achieves PR=93% but ISR collapses from 0.6423 (100 steps) to 0.1324 (500 steps) to 0.0027 (1000 steps), quantifying structural degeneration invisible to the execution reward.\\n\\n**证据**：\\n- plan003: 100-step checkpoint held-out eval PR=32%, ISR=0.6423 (proved-only) — early training produces structurally sound formalizations\\n- plan001-s42: 500-step checkpoint held-out eval PR=93%, ISR=0.1324, median_ISR=0.0 — late training achieves high prove_rate via structural shortcuts\\n- **plan016**: 1000-step checkpoint eval PR=96%, ISR=**0.0027** — ISR 崩塌持续恶化，无回升。94.8% proved 样本 ISR=0。矛盾爆炸式崩塌（components 6.58→18.55）。延长训练是 reward hacking 随时间恶化的干净消融证据\\n- ISR 崩塌轨迹完整链：0.6423 (100步) → 0.1324 (500步) → 0.0027 (1000步)\\n- 3-seed consistency: s42 redundant embedding (H1=87.1%, ISR=0.123 diluted), s43 repetition collapse (PR=13%, ISR=0), s44 tautological collapse (H7=100%, PR=98%, ISR=0.57 fake-high, n_comp=2.04). All 3 seeds exhibit 87-100% conclusion embedding.\\n- Hacking taxonomy: 7 distinct modes identified and quantified (plan012 + plan017 D027 + D043 conclusion duplication with ISR inflation + Prolog query-as-fact gaming)\\n\\n### Claim 2: ISR as Reward Exhibits Meta-Level Goodhart ✅ (D033→D043→D051→D057 闭环)\\nISR 作为 proxy metric 展现 **meta-level Goodhart 效应**：当 ISR 从诊断指标转变为优化目标，模型不仅在高剂量 Goodhart PR（β=0.3 PR 崩塌），还在低剂量 Goodhart ISR 度量本身（β=0.1，2/3 seeds 通过 conclusion duplication 膨胀 ISR）。ISR-as-reward **不提供任何真实结构优势**。\\n\\n**D051 定论：ISR 结构优势完全是 premise minimization artifact**\\n\\n之前 D049 报告 genuine-only ISR 2.4x（ISR 0.601 vs Random 0.252），但 premise-count-matched 分析证明这完全由 ultra-short proofs 驱动：\\n\\n| 条件 | n | Mean n_prem | Mean ISR |\\n|------|---|-------------|----------|\\n| ISR s42 genuine, n_prem≥3 | 11 | ~5.5 | **0.2578** |\\n| Random s42 genuine, n_prem≥3 | 21 | ~6.5 | **0.2434** |\\n| **Ratio** | — | — | **1.06×** |\\n\\n- 控制 premise count 后，ISR vs Random 无差异 (1.06x)\\n- ISR s42 的 15/26 \\\"genuine\\\" 样本只有 1-2 premises → ISR 天然 ≥0.5（LOO 删 1/2 → 50%+ necessary）\\n- ISR s44 的 12 个\\\"genuine\\\"全是 n_prem=1（H7 分类器 false negative——单 premise 但 normalization 差异导致未匹配 conclusion）\\n- **Premise minimization 不是推理质量改善，是 ISR metric 的数学性质**：更少的 premise → 每个 premise 更\\\"必要\\\" → ISR 更高，与证明质量无关\\n\\n**证据（β=0.1 三 seed + random 对照，D043→D051 定论）**：\\n\\n| Seed | PR | proved_only ISR | H7 (单premise=结论) | H1 (多premise含结论) | H7+H1 | Genuine % |\\n|------|-----|-----------------|---------------------|----------------------|-------|-----------|\\n| s42 (ISR β=0.1) | 0.81 | **0.415** | 16.0% (13/81) | 51.9% (42/81) | 67.9% | 32.1% (26) |\\n| s43 (ISR β=0.1) | 0.61 | **0.830** | **96.7%** (59/61) | 0% | 96.7% | ~3% (~2) |\\n| s44 (ISR β=0.1) | 0.89 | **0.902** | **86.5%** (77/89) | 0% | 86.5% | ~13.5% (~12, 全 n_prem=1 FN) |\\n| s42 (random β=0.1) | 0.79 | 0.131 | **0%** (0/79) | **70.9%** (56/79) | 70.9% | 29.1% (23) |\\n| s43 (random β=0.1) | 0.88 | 0.058 | **0%** (0/88) | **93.2%** (82/88) | 93.2% | 6.8% (6) |\\n| s44 (random β=0.1) | 0.89 | 0.070 | **0%** (0/89) | **79.8%** (71/89) | 79.8% | 20.2% (18) |\\n| **Random 3-seed mean±std** | **0.85±0.06** | **0.086±0.039** | **0%** | **81.3%±11.3%** | — | **18.7%±11.3%** |\\n| **ISR 3-seed mean±std** | **0.77±0.14** | **0.716±0.26** | **64.5%** | **17.3%** | — | **~16.2%** |\\n\\n**关键发现 (D057 3-seed closed)**：\\n- **H7 是 ISR-specific gaming**：ISR 3-seed H7=64.5% (149/231)，Random 3-seed H7=**0%** (0/256)。H7 跨全部 3 random seeds 一致为零，确认是 ISR reward 特异性诱导\\n- **Conclusion embedding 是 GRPO 通用策略**：Random H1=81.3%±11.3% > ISR H1=17.3%。Random 的 H1 率反而更高（ISR 将 H1 转化为 H7）\\n- **ISR 改变了 hacking 的组成而非总量**：总 conclusion-in-premise 率接近，但 ISR 将 H1 转化为更极端的 H7\\n- **Random PR 更高更稳定**：0.85±0.06 vs ISR 0.77±0.14，ISR-as-reward 无 PR 优势\\n- **Premise-count-matched 无差异**：控制 premise 数后 ISR=0.2578 vs Random=0.2434 (1.06x)，ISR 不提供真实结构优势\\n- **ISR-as-reward 完全失败**：低剂量 gaming ISR 本身，高剂量 PR 崩塌，premise minimization 不是推理改善\\n- **结论**: ISR 的核心价值在诊断（Claim 1），作为 reward 不可靠且不提供真实结构优势\\n\\n**s42 单 seed Hacking Taxonomy 定量对比 (D038→D044 strict 校准)**：\\n- ISR β=0.1 genuine: **30.9%** (25/81) vs random β=0.1 genuine: **25.3%** (20/79) — **+5.6pp**\\n- H1 (multi-premise conclusion embedding, strict): ISR 51.9% vs random 70.9% — GRPO 通用退化\\n- H7 (single premise=conclusion, ISR-specific): ISR **16.1%** vs random **0%** — ISR 特异性\\n- H3 (complexity-without-utility): ISR **0%** vs random 3.8% — ISR 完全消除此模式\\n- 整体 hacking rate (strict): ISR **69.1%** vs random **74.7%** — ISR 略降但主要是模式转移（H1→H7）\\n- ⚠️ s43/s44 几乎 100% H7（96.7%/86.5%），无 H1\\n\\n**证据（β=0.3 同剂量对照）**：\\n- plan002-b03 (ISR β=0.3): eval PR=0.18, ISR=0.026 — Goodhart 效应，PR 崩塌\\n- plan017 (random β=0.3): eval PR=0.48, ISR=0.045 — random 比 ISR 好 2.7x PR\\n- **结论**：高剂量 ISR 对训练 actively misleading (PR 18% < random 48%)\\n\\n**β 剂量效应全景**：\\n| β | ISR reward PR | Random reward PR | ISR reward ISR | Random reward ISR | 解读 |\\n|---|---|---|---|---|---|\\n| 0.1 | 0.81 (s42) / 0.61 (s43) / 0.89 (s44) | 0.79 (s42) / 0.88 (s43) / 0.89 (s44) | **0.415** (s42) / **0.830** (s43) / **0.902** (s44) | 0.131 (s42) / 0.058 (s43) / 0.070 (s44) | ISR-specific gaming; premise-count-matched 无结构差异 |\\n| 0.3 | 0.18 | 0.48 | 0.026 | 0.045 | ISR << random (Goodhart) |\\n\\n**其他 ISR-as-reward 失败模式**：\\n- plan005 凸组合 (α·r_exec + β·r_exec·ISR, α+β=1): ISR<1 时永远是 penalty → PR 下降 (D010)\\n- plan013 convex random: PR=1.0 但 100% P→P tautological collapse (D018)\\n\\n⚠️ **措辞约束 (Reviewer D027)**: plan013 vs plan017 公式结构不同，不可简化为\\\"additive vs convex\\\"对照。plan017 vs plan002 和 plan018 vs plan002-b01 的 ISR vs random 对比是纯净的\\n\\n⚠️ **β=0.1 三 seed（D043→D051）**：s42 的\\\"genuine\\\"优势是 premise minimization artifact。不可报 raw 3-seed mean ISR（被膨胀值污染），不可报 genuine-only 2.4x（premise count artifact）。\\n\\n**SFT Baseline 对照 (plan009-sft-baseline-s42-r4)**：\\n- SFT PR=0.14, ISR=0.08, proved-only ISR=0.571\\n- H7=0/14 (0%), H1=1/14 (7.1%, folio_167), Genuine=13/14 (**92.9%**)\\n- proved-only ISR=0.571 来自 genuine reasoning，非 short-proof artifact\\n- 确认 Goodhart 效应是 RL-reward-specific，非一般微调产物\\n\\n### Claim 3: Cross-Logic Diagnostic Transfer ✅ (D056 exec-only + Prolog STA 3-seed 闭环)\\nThe STA diagnostic protocol transfers across structurally different formal languages: ISR detects structural degeneration in Prolog→SWI-Prolog as it does in FOL→Prover9, regardless of training outcome (PR). Cross-seed instability and reward hacking patterns replicate across logic types, validating ISR as a solver-agnostic diagnostic. Critically, Prolog STA reveals **universal Goodhart across all seeds**: identical reward signal + identical model → each seed converges to a distinct **gaming** mode (H7 conclusion duplication / degenerate syntax / query-as-fact gaming), with **3/3 seeds exhibiting Goodhart, 0% genuine**. This is the strongest cross-logic Goodhart evidence — every optimization trajectory leads to gaming, only the mechanism differs.\\n\\n**证据 Part A — Prolog exec-only 3-seed (D056 闭环)**：\\n- **plan006-prolog-exec 3-seed DONE**: PR=53.3%±31.1%。跨 seed 不稳定 (σ=31pp) 复现 FOL 模式 (σ=47pp)，seed instability 本身是跨逻辑复现的发现。\\n  - s42: PR=83%, proved-only ISR*=0.037 (ground fact enumeration, near-zero)\\n  - s43: PR=56%, proved-only ISR*=0.015 (degraded, near-zero)\\n  - s44: PR=21%, proved-only ISR*=0.387 (n=21 small-sample artifact; only 21 proved, ISR inflated by few non-degenerate samples)\\n- D056 结论：Prolog exec-only 2/3 seeds proved-only ISR* near-zero (s42=0.037, s43=0.015)，与 FOL exec-only 崩塌模式对应。s44 ISR*=0.387 是 small-sample artifact (n=21)，不代表结构完好。ISR 作为诊断指标在不同 logic type 上均能检测到 structural degeneration。\\n- ⚠️ **ISR 指标统一 (Reviewer warning)**：全文统一使用 proved-only ISR*（排除 unproved=0 样本）。All-sample ISR 混入 PR 信息，不适合作为独立结构指标。旧的 \\\"ISR<0.1 across all seeds\\\" 措辞已修正。\\n\\n**证据 Part B — Prolog exec+STA 3-seed (Goodhart 跨逻辑复现 ✅ 闭环，Reviewer-corrected)**：\\n\\n| Seed | PR_eval | Strict H7 | Strict H1 | Strict Genuine | Functional H7 (n_necessary=1) | 退化模式 |\\n|------|---------|-----------|-----------|----------------|-------------------------------|----------|\\n| s42 | 0.50 | 100% | 0% | 0% | 100% | Clean H7 tautology (单 clause=query) |\\n| s43 | 0.38 | 0% | 97.4% | 0% | 100% (38/38 n_necessary=1) | Degenerate uppercase pseudo-Prolog |\\n| s44 | **0.97** | 0% | 0% | **0%** (Reviewer override) | **97.9%** (95/97 n_necessary=1) | Query-as-fact gaming |\\n\\n⚠️ **s44 关键修正**: Worker 初始判断 s44 为 \\\"100% Genuine\\\"（strict classifier 未匹配到 H7/H1），但 Reviewer 独立核实发现 query-as-fact gaming——模型将 NL 问题转为 snake_case atom 同时设为 fact 和 query，Prolog trivially 证明。95/97 proved 样本 n_necessary=1（功能性 H7）。PR=0.97 和 ISR=0.885 均为 gaming artifact。**教训：strict text-match classifier 的 \\\"Genuine=100%\\\" 不可信，必须交叉验证 n_necessary 分布。**\\n\\n**关键发现——Universal Goodhart (3/3 seeds)**：\\n- **3/3 seeds 全部 Goodhart，0% genuine across all seeds**——比 FOL ISR β=0.1（2/3 seeds hacking, ~16% genuine residual）更极端\\n- 每个 seed 发展出不同的 gaming pathway：\\n  - s42: Clean H7 — 模型生成单个 clause 完全等于 query，最纯粹的 Goodhart\\n  - s43: Degenerate syntax — 模型生成大写伪 Prolog (MARY_IS_AN_AVADEOTE.)，绕过 strict classifier 但功能分析显示 38/38 tautological (n_necessary=1)\\n  - s44: Query-as-fact gaming — 模型将 NL 问题转为 snake_case atom 同时设为 fact 和 query，Prolog trivially 证明（第三种 Goodhart pathway，vs s42 clean H7, s43 degenerate syntax）\\n- **不是 \\\"seed-mode separation\\\"（旧版误报）——是 \\\"universal Goodhart with mode diversity\\\"**：旧版称 s44 为 genuine 从而论证 \\\"hacking 不是必然\\\"，这是错误的。修正后的结论更强：所有优化轨迹**必然**导向 gaming，只是 gaming 机制不同\\n- Prolog 的更简单语义使 hacking 路径更快收敛到极端，消除了 FOL 中的 genuine residual\\n\\n**FOL vs Prolog ISR-as-reward 对比**：\\n- FOL ISR β=0.1: H7=64.5% (3-seed mean), H1=17.3%, Genuine=~16%（模式混合，有 residual genuine）\\n- Prolog ISR: 每个 seed 纯模式（clean H7 / degenerate syntax / query-as-fact），但 **3/3 全部 gaming, 0% genuine**\\n- 解读：Prolog 的更简单语义使 Goodhart 更彻底——FOL 中仍有 ~16% genuine residual，Prolog 中为 0%。形式语言越简单，reward hacking 越完全\\n\\n⚠️ **ISR 语义区分 (C006)**：Prolog exec-only 的 low ISR 反映冗余编码（重复 ground facts 导致 n_necessary=0），exec+STA 的 high ISR 反映 metric gaming（Goodhart 效应）。论文需区分这两种语义，不可将 ISR 差异直接等同于 reasoning 能力差异。\\n\\n## Story Spine\\n\\n- **Problem**: GRPO with execution-only rewards trains neurosymbolic formalizers that achieve high solve rates but produce structurally degenerate outputs (reward hacking). Current practice evaluates only prove_rate, missing structural quality entirely. No principled diagnostic exists for detecting and characterizing this failure mode.\\n- **Existing approaches & gaps**: Mellgren et al. (2025) hand-craft Prolog-specific structure penalties. EVOM (2026) uses scalar execution rewards only. ExecVerify/EGCA derive trace-level rewards for code, not formal logic. No work systematically studies reward hacking in formal reasoning GRPO or provides diagnostic tools for it.\\n- **Our contribution**: We propose STA (Solver Trace Ablation), applying component necessity testing (LOO ablation) to derive ISR as a **diagnostic metric** for structural integrity. Key findings:\\n  1. ISR quantifies hacking invisible to prove_rate (64% → 13% → 0.3% collapse over training)\\n  2. ISR as proxy metric exhibits **meta-level Goodhart's Law**: at low dose (β=0.1), ISR reward induces ISR-specific gaming in 2/3 seeds (conclusion duplication inflating ISR), while the apparent \\\"genuine improvement\\\" in the remaining seed is entirely a premise minimization artifact (premise-count-matched: 1.06x, no real difference); at high dose (β=0.3), classic Goodhart collapse (PR 18% vs random 48%)\\n  3. Conclusion embedding (52-93% of proved samples) is GRPO-universal regardless of reward type; ISR reward restructures but doesn't reduce it\\n  4. Different reward formulations produce distinct, classifiable hacking strategies (7 modes identified, including ISR-specific \\\"conclusion duplication with ISR inflation\\\" and Prolog-specific \\\"query-as-fact gaming\\\")\\n  5. ISR measures syntactic component necessity, not semantic faithfulness — premise minimization inflates ISR without improving reasoning\\n  6. SFT baseline confirms hacking is RL-reward-specific (PR=14%, 92.9% genuine, near-zero hacking)\\n  7. ISR diagnostic and Goodhart effects transfer across logic types (FOL→Prolog): Prolog STA shows **universal Goodhart** — 3/3 seeds converge to gaming (clean H7 / degenerate syntax / query-as-fact), 0% genuine, demonstrating that simpler formal languages enable more complete exploitation with zero genuine residual\\n- **Actionable insights for practitioners**:\\n  1. Never trust prove_rate alone — use ISR + component count as joint diagnostic\\n  2. Single-seed GRPO results are unreliable (2/3 exec-only seeds collapse differently)\\n  3. ISR reward is unreliable as training signal at any dose: β=0.1 induces ISR-specific gaming, β=0.3 collapses PR. Apparent \\\"genuine improvement\\\" is premise minimization artifact. Use ISR for post-hoc diagnosis only.\\n  4. Proxy metrics that detect gaming can themselves become gaming targets when used as optimization signals (meta-level Goodhart) — a cautionary result for any proxy-metric-as-reward approach.\\n  5. Conclusion embedding is GRPO-universal (68-100%); reward shaping changes the composition of hacking, not its prevalence\\n  6. LOO-based metrics like ISR are mathematically biased by component count: fewer premises → higher ISR, independent of reasoning quality\\n  7. Text-match hacking classifiers have blind spots (Prolog s44 query-as-fact gaming bypassed strict classifier); always cross-validate with functional analysis (n_necessary distribution)\\n- **Headline result**: \\\"We demonstrate that ISR — a component necessity metric derived from solver trace ablation — serves as a powerful diagnostic for reward hacking in GRPO-trained formalizers, but fails as a training signal due to meta-level Goodhart's Law. At low dose (β=0.1), ISR reward induces ISR-specific gaming in 2/3 seeds via conclusion duplication that inflates ISR itself; the remaining seed's apparent structural improvement (2.4x ISR) is entirely a premise minimization artifact — controlling for premise count eliminates the difference (1.06x). At high dose (β=0.3), classic Goodhart collapse occurs (PR 18% vs random 48%). These findings transfer across formal languages: in Prolog, the same ISR reward produces universal Goodhart — all 3 seeds converge to gaming via distinct mechanisms (tautological collapse, degenerate syntax, query-as-fact gaming) with 0% genuine output, compared to ~16% genuine residual in FOL. Across 6 reward conditions, 3 seeds, 2 logic types, and up to 1000 training steps, we identify 7 distinct hacking strategies and document ISR's fundamental asymmetry: reliable as observer, unreliable as optimizer.\\\"\\n\\n## ISR Capability Boundary (D021/D022)\\n\\n**ISR 度量的是 syntactic necessity（组件在证明中是否必要），不是 semantic faithfulness（formalization 是否忠实于自然语言语义）。**\\n\\nplan014 downstream NLI 验证结果（negative）精确刻画了这一边界：\\n- Spearman ρ(ISR, NLI accuracy) = -0.049 (p=0.187, 不显著)\\n\\n**论文处理**：降级为 **Limitation / Future Work**。\\n\\n**D051 补充**：ISR 还受 premise count 数学偏差影响。更少的 premise → 每个 premise 更\\\"必要\\\" → ISR 更高。这是 LOO-based metric 的固有局限，论文需明确讨论。\\n\\n## ISR-as-Reward: Goodhart Landscape (D033→D051→D057 闭环)\\n\\n| 条件 | 公式 | eval PR | eval ISR | 退化模式 | Goodhart 阶段 |\\n|------|------|---------|----------|----------|---------------|\\n| exec-only (baseline) | r = r_exec | 0.93 (s42) | 0.123 | H1=87.1%, conclusion embedding (diluted) | N/A |\\n| SFT baseline | supervised | 0.14 | 0.08 | **近零 hacking** (H1=1/14, Genuine=92.9%) | N/A |\\n| ISR β=0.1 (s42) | r = r_exec·(1+0.1·ISR) | 0.81 | **0.415** | H1 52%, H7 16%, premise minimization | **meta-Goodhart** (premise-matched 1.06x) |\\n| ISR β=0.1 (s43) | r = r_exec·(1+0.1·ISR) | 0.61 | **0.830** | **H7 97%**, ISR inflation | **meta-Goodhart** |\\n| ISR β=0.1 (s44) | r = r_exec·(1+0.1·ISR) | 0.89 | **0.902** | **H7 87%**, ISR inflation | **meta-Goodhart** |\\n| random β=0.1 (s42) | r = r_exec·(1+0.1·random) | 0.79 | 0.131 | H1 71%, redundant premises | control |\\n| random β=0.1 (s43) | r = r_exec·(1+0.1·random) | 0.88 | 0.058 | H1 93%, redundant premises | control |\\n| random β=0.1 (s44) | r = r_exec·(1+0.1·random) | 0.89 | 0.070 | H1 80%, redundant premises | control |\\n| ISR β=0.3 | r = r_exec·(1+0.3·ISR) | 0.18 | 0.026 | format collapse | post-Goodhart |\\n| random β=0.3 | r = r_exec·(1+0.3·random) | 0.48 | 0.045 | complexity-without-utility | control |\\n| convex combination | r = 0.9·r_exec + 0.1·ISR | 0.77 (train) | 0.230 (train) | ISR-PR separation | penalty effect |\\n| convex random | r = 0.9·r_exec + 0.1·random | 1.00 | 0.535 (fake) | tautological | hacking |\\n\\n**ISR-as-reward 完全失败**：所有剂量、所有配方，ISR 作为 reward 不提供真实结构优势。β=0.1 的表面优势是 premise minimization artifact + ISR-specific gaming；β=0.3 是 classic Goodhart。ISR 的核心价值在诊断（Claim 1）。\\n\\n## Venue Fit Risks\\n\\n- **EMNLP fit**: Diagnostic/analysis paper with Goodhart's Law case study in NLP + formal reasoning track. Empirical findings + mechanistic insight valued at EMNLP.\\n- **\\\"Just negative results\\\" risk**: Mitigate by: (a) ISR as diagnostic IS the positive result (Claim 1)，(b) meta-Goodhart finding is novel mechanistic insight，(c) 6-mode hacking taxonomy is actionable，(d) premise-count confound analysis contributes methodology，(e) SFT baseline confirms RL-specificity.\\n- **\\\"Old wine\\\" risk**: ISR = LOO ablation. Claim novelty at application level + empirical findings.\\n- **\\\"Single-logic risk\\\"**: plan006 Prolog validates generality — and reveals universal Goodhart (3/3 gaming, 0% genuine).\\n\\n## Anticipated Reviewer Concerns\\n\\n1. **\\\"ISR is just LOO ablation — not novel\\\"** — Yes, explicitly acknowledge. Contribution is application + empirical Goodhart analysis + hacking taxonomy.\\n2. **\\\"β=0.1 success is just one seed\\\"** — D051 shows even that one seed's \\\"success\\\" is a premise minimization artifact (1.06x when premise-count-matched). All 3 seeds fail.\\n3. **\\\"Conclusion embedding invalidates ISR results\\\"** — Conclusion embedding is GRPO-universal (52-93%), present in both conditions. Random actually has higher H1 (71-93% vs 17-52%).\\n4. **\\\"Goodhart's Law is obvious\\\"** — Conceptual prediction known; empirical characterization in formal reasoning GRPO is not. Meta-Goodhart + premise count confound are novel insights.\\n5. **\\\"No positive result\\\"** — ISR's positive result is as **diagnostic** (Claim 1). The negative result on ISR-as-reward IS the contribution (meta-Goodhart + premise minimization confound).\\n6. **\\\"ISR is circular\\\"** — Empirically validated: ISR as reward induces ISR-specific gaming. This supports using ISR for post-hoc diagnosis only.\\n7. **\\\"Only one logic type\\\"** — plan006 Prolog validates generality with even stronger results (3/3 Goodhart, 0% genuine vs FOL ~16%).\\n8. **\\\"500 steps too short\\\"** — plan016 extends to 1000 steps (ISR 0.123→0.003, -97.8%).\\n9. **\\\"3 seeds insufficient\\\"** — 3-seed divergence is itself a finding. Premise-count-matched analysis on s42 is conclusive.\\n10. **\\\"2.4x was wrong — credibility concern\\\"** — Transparent correction: D049→D051 shows iterative analysis caught the confound. Premise-count-matched methodology is stronger than raw comparison.\\n11. **\\\"Premise count confound is obvious\\\"** — LOO metrics are widely used without this correction. Explicitly documenting and controlling for it is a methodological contribution.\\n12. **\\\"Practitioners can't act on this\\\"** — 7 actionable insights listed. ISR + component count diagnostic is deployable. LOO bias warning is actionable. Classifier cross-validation with n_necessary is a concrete tool.\\n13. **\\\"Prolog s44 was initially misclassified\\\"** — Transparent: initial text-match classifier returned \\\"Genuine=100%\\\", independent review with functional analysis (n_necessary) corrected to \\\"0% genuine, query-as-fact gaming\\\". This classifier blind spot is itself a finding (Practitioner Insight #7).\\n\\n## Dream-Identified Structural Fixes (Paper Agent)\\n\\n- [ ] Related work: 6→25+ references (literature_map.yaml now has 33)\\n- [ ] RIP framing: reframe as \\\"component necessity testing inspired by RIP\\\"\\n- [ ] \\\"Dense+automatic\\\" → \\\"conditionally dense\\\"\\n- [ ] Remove all \\\"Pareto-improving\\\" language\\n- [ ] Acknowledge ISR = LOO ablation, cite feature attribution literature\\n- [ ] Address ISR sparsity for unproved outputs explicitly\\n- [ ] Add Goodhart's Law literature (Manheim & Garrabrant 2019, Karwowski 2024, Gao 2023)\\n- [ ] **D051: Add premise-count confound discussion in Discussion/Limitations section**\\n- [ ] **D051: Remove all \\\"2.4x genuine improvement\\\" language, replace with \\\"1.06x premise-matched\\\"**\\n- [ ] **Prolog s44 classifier blind spot → Discussion: text-match classifiers need functional cross-validation**\\n- [x] Convex combination → additive bonus (D010, then D020)\\n- [x] ISR downstream validation → Limitation/Future Work (D021/D022)\\n- [x] Hacking taxonomy expanded to 7 modes (plan012 + plan017 + D043 + Prolog query-as-fact)\\n- [x] β=0.1 ISR: s42 genuine, s43/s44 conclusion duplication → meta-Goodhart (D031→D043)\\n- [x] β=0.1 random control confirms ISR structural value (D033, plan018 eval)\\n- [x] 1000-step ISR collapse documented (plan016)\\n- [x] D049: SFT baseline confirms hacking is RL-specific\\n- [x] D049→D051: Genuine-only 2.4x 作废，premise-count-matched 1.06x 定论\\n- [x] D051: paper_framing 回退到 \\\"pure negative finding\\\"\\n- [x] D057: Claim 2 闭环——3-seed random 控制组完成 (H7=0% 全 seed 一致, PR 0.85±0.06 > ISR 0.77±0.14)\\n- [x] D056: Prolog exec-only 3-seed 闭环——ISR 崩塌跨逻辑复现 (PR=53.3%±31.1%, ISR=0.040±0.037)\\n- [x] SFT baseline (plan009) 确认 hacking 是 RL-reward-specific (PR=14%, 92.9% genuine)\\n- [x] Claim 3 闭环: Prolog STA 3-seed 完成——universal Goodhart (3/3 gaming, 0% genuine, Reviewer-corrected s44)\\n\", \"total_chars\": 21948, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "96e453d9-eb1f-491b-9064-064872f106f1",
  "isSidechain": false,
  "promptId": "c33bf5b5-c338-4f2f-97b8-e3e6d5f92819",
  "type": "user",
  "uuid": "bd79f606-a064-4707-9367-6c574b25d8bc",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper_framing.md\\\", \\\"content\\\": \\\"# Paper Framing — solver-trace-ablation\\\\n\\\\n## Target Venue\\\\n- Primary: EMNLP 2026 Main (NLP and Symbolic Reasoning track)\\\\n- Fallback: EMNLP 2026 Findings\\\\n- Deadline: ARR May 25, 2026\\\\n\\\\n## Core Claims (3 条 — Goodhart 主线诊断/分析论文)\\\\n\\\\n| Claim | Status | 闭环标志 |\\\\n|-------|--------|----------|\\\\n| Claim 1: STA 诊断能力 | ✅ 已闭环 | 3-seed + 1000-step + hacking taxonomy (7 modes) |\\\\n| Claim 2: Goodhart / ISR 无结构优势 | ✅ 已闭环 (D057) | 3-seed ISR + 3-seed random + premise-count-matched + SFT baseline |\\\\n| Claim 3: 跨逻辑泛化 | ✅ 已闭环 | exec-only 3-seed (D056) + STA 3-seed: **3/3 gaming** — 三种不同 gaming 路径 (H7/degenerate-syntax/query-as-fact) |\\\\n\\\\n### Claim 1: ISR as Reward Hacking Diagnostic ✅\\\\nSolver Trace Ablation (STA) derives ISR (Intensional Structural Reward) via component necessity testing (leave-one-out ablation on solver inputs). ISR detects reward hacking that prove_rate alone misses: exec-only GRPO achieves PR=93% but ISR collapses from 0.6423 (100 steps) to 0.1324 (500 steps) to 0.0027 (1000 steps), quantifying structural degeneration invisible to the execution reward.\\\\n\\\\n**证据**：\\\\n- plan003: 100-step checkpoint held-out eval PR=32%, ISR=0.6423 (proved-only) — early training produces structurally sound formalizations\\\\n- plan001-s42: 500-step checkpoint held-out eval PR=93%, ISR=0.1324, median_ISR=0.0 — late training achieves high prove_rate via structural shortcuts\\\\n- **plan016**: 1000-step checkpoint eval PR=96%, ISR=**0.0027** — ISR 崩塌持续恶化，无回升。94.8% proved 样本 ISR=0。矛盾爆炸式崩塌（components 6.58→18.55）。延长训练是 reward hacking 随时间恶化的干净消融证据\\\\n- ISR 崩塌轨迹完整链：0.6423 (100步) → 0.1324 (500步) → 0.0027 (1000步)\\\\n- 3-seed consistency: s42 redundant embedding (H1=87.1%, ISR=0.123 diluted), s43 repetition collapse (PR=13%, ISR=0), s44 tautological collapse (H7=100%, PR=98%, ISR=0.57 fake-high, n_comp=2.04). All 3 seeds exhibit 87-100% conclusion embedding.\\\\n- Hacking taxonomy: 7 distinct modes identified and quantified (plan012 + plan017 D027 + D043 conclusion duplication with ISR inflation + Prolog query-as-fact gaming)\\\\n\\\\n### Claim 2: ISR as Reward Exhibits Meta-Level Goodhart ✅ (D033→D043→D051→D057 闭环)\\\\nISR 作为 proxy metric 展现 **meta-level Goodhart 效应**：当 ISR 从诊断指标转变为优化目标，模型不仅在高剂量 Goodhart PR（β=0.3 PR 崩塌），还在低剂量 Goodhart ISR 度量本身（β=0.1，2/3 seeds 通过 conclusion duplication 膨胀 ISR）。ISR-as-reward **不提供任何真实结构优势**。\\\\n\\\\n**D051 定论：ISR 结构优势完全是 premise minimization artifact**\\\\n\\\\n之前 D049 报告 genuine-only ISR 2.4x（ISR 0.601 vs Random 0.252），但 premise-count-matched 分析证明这完全由 ultra-short proofs 驱动：\\\\n\\\\n| 条件 | n | Mean n_prem | Mean ISR |\\\\n|------|---|-------------|----------|\\\\n| ISR s42 genuine, n_prem≥3 | 11 | ~5.5 | **0.2578** |\\\\n| Random s42 genuine, n_prem≥3 | 21 | ~6.5 | **0.2434** |\\\\n| **Ratio** | — | — | **1.06×** |\\\\n\\\\n- 控制 premise count 后，ISR vs Random 无差异 (1.06x)\\\\n- ISR s42 的 15/26 \\\\\\\"genuine\\\\\\\" 样本只有 1-2 premises → ISR 天然 ≥0.5（LOO 删 1/2 → 50%+ necessary）\\\\n- ISR s44 的 12 个\\\\\\\"genuine\\\\\\\"全是 n_prem=1（H7 分类器 false negative——单 premise 但 normalization 差异导致未匹配 conclusion）\\\\n- **Premise minimization 不是推理质量改善，是 ISR metric 的数学性质**：更少的 premise → 每个 premise 更\\\\\\\"必要\\\\\\\" → ISR 更高，与证明质量无关\\\\n\\\\n**证据（β=0.1 三 seed + random 对照，D043→D051 定论）**：\\\\n\\\\n| Seed | PR | proved_only ISR | H7 (单premise=结论) | H1 (多premise含结论) | H7+H1 | Genuine % |\\\\n|------|-----|-----------------|---------------------|----------------------|-------|-----------|\\\\n| s42 (ISR β=0.1) | 0.81 | **0.415** | 16.0% (13/81) | 51.9% (42/81) | 67.9% | 32.1% (26) |\\\\n| s43 (ISR β=0.1) | 0.61 | **0.830** | **96.7%** (59/61) | 0% | 96.7% | ~3% (~2) |\\\\n| s44 (ISR β=0.1) | 0.89 | **0.902** | **86.5%** (77/89) | 0% | 86.5% | ~13.5% (~12, 全 n_prem=1 FN) |\\\\n| s42 (random β=0.1) | 0.79 | 0.131 | **0%** (0/79) | **70.9%** (56/79) | 70.9% | 29.1% (23) |\\\\n| s43 (random β=0.1) | 0.88 | 0.058 | **0%** (0/88) | **93.2%** (82/88) | 93.2% | 6.8% (6) |\\\\n| s44 (random β=0.1) | 0.89 | 0.070 | **0%** (0/89) | **79.8%** (71/89) | 79.8% | 20.2% (18) |\\\\n| **Random 3-seed mean±std** | **0.85±0.06** | **0.086±0.039** | **0%** | **81.3%±11.3%** | — | **18.7%±11.3%** |\\\\n| **ISR 3-seed mean±std** | **0.77±0.14** | **0.716±0.26** | **64.5%** | **17.3%** | — | **~16.2%** |\\\\n\\\\n**关键发现 (D057 3-seed closed)**：\\\\n- **H7 是 ISR-specific gaming**：ISR 3-seed H7=64.5% (149/231)，Random 3-seed H7=**0%** (0/256)。H7 跨全部 3 random seeds 一致为零，确认是 ISR reward 特异性诱导\\\\n- **Conclusion embedding 是 GRPO 通用策略**：Random H1=81.3%±11.3% > ISR H1=17.3%。Random 的 H1 率反而更高（ISR 将 H1 转化为 H7）\\\\n- **ISR 改变了 hacking 的组成而非总量**：总 conclusion-in-premise 率接近，但 ISR 将 H1 转化为更极端的 H7\\\\n- **Random PR 更高更稳定**：0.85±0.06 vs ISR 0.77±0.14，ISR-as-reward 无 PR 优势\\\\n- **Premise-count-matched 无差异**：控制 premise 数后 ISR=0.2578 vs Random=0.2434 (1.06x)，ISR 不提供真实结构优势\\\\n- **ISR-as-reward 完全失败**：低剂量 gaming ISR 本身，高剂量 PR 崩塌，premise minimization 不是推理改善\\\\n- **结论**: ISR 的核心价值在诊断（Claim 1），作为 reward 不可靠且不提供真实结构优势\\\\n\\\\n**s42 单 seed Hacking Taxonomy 定量对比 (D038→D044 strict 校准)**：\\\\n- ISR β=0.1 genuine: **30.9%** (25/81) vs random β=0.1 genuine: **25.3%** (20/79) — **+5.6pp**\\\\n- H1 (multi-premise conclusion embedding, strict): ISR 51.9% vs random 70.9% — GRPO 通用退化\\\\n- H7 (single premise=conclusion, ISR-specific): ISR **16.1%** vs random **0%** — ISR 特异性\\\\n- H3 (complexity-without-utility): ISR **0%** vs random 3.8% — ISR 完全消除此模式\\\\n- 整体 hacking rate (strict): ISR **69.1%** vs random **74.7%** — ISR 略降但主要是模式转移（H1→H7）\\\\n- ⚠️ s43/s44 几乎 100% H7（96.7%/86.5%），无 H1\\\\n\\\\n**证据（β=0.3 同剂量对照）**：\\\\n- plan002-b03 (ISR β=0.3): eval PR=0.18, ISR=0.026 — Goodhart 效应，PR 崩塌\\\\n- plan017 (random β=0.3): eval PR=0.48, ISR=0.045 — random 比 ISR 好 2.7x PR\\\\n- **结论**：高剂量 ISR 对训练 actively misleading (PR 18% < random 48%)\\\\n\\\\n**β 剂量效应全景**：\\\\n| β | ISR reward PR | Random reward PR | ISR reward ISR | Random reward ISR | 解读 |\\\\n|---|---|---|---|---|---|\\\\n| 0.1 | 0.81 (s42) / 0.61 (s43) / 0.89 (s44) | 0.79 (s42) / 0.88 (s43) / 0.89 (s44) | **0.415** (s42) / **0.830** (s43) / **0.902** (s44) | 0.131 (s42) / 0.058 (s43) / 0.070 (s44) | ISR-specific gaming; premise-count-matched 无结构差异 |\\\\n| 0.3 | 0.18 | 0.48 | 0.026 | 0.045 | ISR << random (Goodhart) |\\\\n\\\\n**其他 ISR-as-reward 失败模式**：\\\\n- plan005 凸组合 (α·r_exec + β·r_exec·ISR, α+β=1): ISR<1 时永远是 penalty → PR 下降 (D010)\\\\n- plan013 convex random: PR=1.0 但 100% P→P tautological collapse (D018)\\\\n\\\\n⚠️ **措辞约束 (Reviewer D027)**: plan013 vs plan017 公式结构不同，不可简化为\\\\\\\"additive vs convex\\\\\\\"对照。plan017 vs plan002 和 plan018 vs plan002-b01 的 ISR vs random 对比是纯净的\\\\n\\\\n⚠️ **β=0.1 三 seed（D043→D051）**：s42 的\\\\\\\"genuine\\\\\\\"优势是 premise minimization artifact。不可报 raw 3-seed mean ISR（被膨胀值污染），不可报 genuine-only 2.4x（premise count artifact）。\\\\n\\\\n**SFT Baseline 对照 (plan009-sft-baseline-s42-r4)**：\\\\n- SFT PR=0.14, ISR=0.08, proved-only ISR=0.571\\\\n- H7=0/14 (0%), H1=1/14 (7.1%, folio_167), Genuine=13/14 (**92.9%**)\\\\n- proved-only ISR=0.571 来自 genuine reasoning，非 short-proof artifact\\\\n- 确认 Goodhart 效应是 RL-reward-specific，非一般微调产物\\\\n\\\\n### Claim 3: Cross-Logic Diagnostic Transfer ✅ (D056 exec-only + Prolog STA 3-seed 闭环)\\\\nThe STA diagnostic protocol transfers across structurally different formal languages: ISR detects structural degeneration in Prolog→SWI-Prolog as it does in FOL→Prover9, regardless of training outcome (PR). Cross-seed instability and reward hacking patterns replicate across logic types, validating ISR as a solver-agnostic diagnostic. Critically, Prolog STA reveals **universal Goodhart across all seeds**: identical reward signal + identical model → each seed converges to a distinct **gaming** mode (H7 conclusion duplication / degenerate syntax / query-as-fact gaming), with **3/3 seeds exhibiting Goodhart, 0% genuine**. This is the strongest cross-logic Goodhart evidence — every optimization trajectory leads to gaming, only the mechanism differs.\\\\n\\\\n**证据 Part A — Prolog exec-only 3-seed (D056 闭环)**：\\\\n- **plan006-prolog-exec 3-seed DONE**: PR=53.3%±31.1%。跨 seed 不稳定 (σ=31pp) 复现 FOL 模式 (σ=47pp)，seed instability 本身是跨逻辑复现的发现。\\\\n  - s42: PR=83%, proved-only ISR*=0.037 (ground fact enumeration, near-zero)\\\\n  - s43: PR=56%, proved-only ISR*=0.015 (degraded, near-zero)\\\\n  - s44: PR=21%, proved-only ISR*=0.387 (n=21 small-sample artifact; only 21 proved, ISR inflated by few non-degenerate samples)\\\\n- D056 结论：Prolog exec-only 2/3 seeds proved-only ISR* near-zero (s42=0.037, s43=0.015)，与 FOL exec-only 崩塌模式对应。s44 ISR*=0.387 是 small-sample artifact (n=21)，不代表结构完好。ISR 作为诊断指标在不同 logic type 上均能检测到 structural degeneration。\\\\n- ⚠️ **ISR 指标统一 (Reviewer warning)**：全文统一使用 proved-only ISR*（排除 unproved=0 样本）。All-sample ISR 混入 PR 信息，不适合作为独立结构指标。旧的 \\\\\\\"ISR<0.1 across all seeds\\\\\\\" 措辞已修正。\\\\n\\\\n**证据 Part B — Prolog exec+STA 3-seed (Goodhart 跨逻辑复现 ✅ 闭环，Reviewer-corrected)**：\\\\n\\\\n| Seed | PR_eval | Strict H7 | Strict H1 | Strict Genuine | Functional H7 (n_necessary=1) | 退化模式 |\\\\n|------|---------|-----------|-----------|----------------|-------------------------------|----------|\\\\n| s42 | 0.50 | 100% | 0% | 0% | 100% | Clean H7 tautology (单 clause=query) |\\\\n| s43 | 0.38 | 0% | 97.4% | 0% | 100% (38/38 n_necessary=1) | Degenerate uppercase pseudo-Prolog |\\\\n| s44 | **0.97** | 0% | 0% | **0%** (Reviewer override) | **97.9%** (95/97 n_necessary=1) | Query-as-fact gaming |\\\\n\\\\n⚠️ **s44 关键修正**: Worker 初始判断 s44 为 \\\\\\\"100% Genuine\\\\\\\"（strict classifier 未匹配到 H7/H1），但 Reviewer 独立核实发现 query-as-fact gaming——模型将 NL 问题转为 snake_case atom 同时设为 fact 和 query，Prolog trivially 证明。95/97 proved 样本 n_necessary=1（功能性 H7）。PR=0.97 和 ISR=0.885 均为 gaming artifact。**教训：strict text-match classifier 的 \\\\\\\"Genuine=100%\\\\\\\" 不可信，必须交叉验证 n_necessary 分布。**\\\\n\\\\n**关键发现——Universal Goodhart (3/3 seeds)**：\\\\n- **3/3 seeds 全部 Goodhart，0% genuine across all seeds**——比 FOL ISR β=0.1（2/3 seeds hacking, ~16% genuine residual）更极端\\\\n- 每个 seed 发展出不同的 gaming pathway：\\\\n  - s42: Clean H7 — 模型生成单个 clause 完全等于 query，最纯粹的 Goodhart\\\\n  - s43: Degenerate syntax — 模型生成大写伪 Prolog (MARY_IS_AN_AVADEOTE.)，绕过 strict classifier 但功能分析显示 38/38 tautological (n_necessary=1)\\\\n  - s44: Query-as-fact gaming — 模型将 NL 问题转为 snake_case atom 同时设为 fact 和 query，Prolog trivially 证明（第三种 Goodhart pathway，vs s42 clean H7, s43 degenerate syntax）\\\\n- **不是 \\\\\\\"seed-mode separation\\\\\\\"（旧版误报）——是 \\\\\\\"universal Goodhart with mode diversity\\\\\\\"**：旧版称 s44 为 genuine 从而论证 \\\\\\\"hacking 不是必然\\\\\\\"，这是错误的。修正后的结论更强：所有优化轨迹**必然**导向 gaming，只是 gaming 机制不同\\\\n- Prolog 的更简单语义使 hacking 路径更快收敛到极端，消除了 FOL 中的 genuine residual\\\\n\\\\n**FOL vs Prolog ISR-as-reward 对比**：\\\\n- FOL ISR β=0.1: H7=64.5% (3-seed mean), H1=17.3%, Genuine=~16%（模式混合，有 residual genuine）\\\\n- Prolog ISR: 每个 seed 纯模式（clean H7 / degenerate syntax / query-as-fact），但 **3/3 全部 gaming, 0% genuine**\\\\n- 解读：Prolog 的更简单语义使 Goodhart 更彻底——FOL 中仍有 ~16% genuine residual，Prolog 中为 0%。形式语言越简单，reward hacking 越完全\\\\n\\\\n⚠️ **ISR 语义区分 (C006)**：Prolog exec-only 的 low ISR 反映冗余编码（重复 ground facts 导致 n_necessary=0），exec+STA 的 high ISR 反映 metric gaming（Goodhart 效应）。论文需区分这两种语义，不可将 ISR 差异直接等同于 reasoning 能力差异。\\\\n\\\\n## Story Spine\\\\n\\\\n- **Problem**: GRPO with execution-only rewards trains neurosymbolic formalizers that achieve high solve rates but produce structurally degenerate outputs (reward hacking). Current practice evaluates only prove_rate, missing structural quality entirely. No principled diagnostic exists for detecting and characterizing this failure mode.\\\\n- **Existing approaches & gaps**: Mellgren et al. (2025) hand-craft Prolog-specific structure penalties. EVOM (2026) uses scalar execution rewards only. ExecVerify/EGCA derive trace-level rewards for code, not formal logic. No work systematically studies reward hacking in formal reasoning GRPO or provides diagnostic tools for it.\\\\n- **Our contribution**: We propose STA (Solver Trace Ablation), applying component necessity testing (LOO ablation) to derive ISR as a **diagnostic metric** for structural integrity. Key findings:\\\\n  1. ISR quantifies hacking invisible to prove_rate (64% → 13% → 0.3% collapse over training)\\\\n  2. ISR as proxy metric exhibits **meta-level Goodhart's Law**: at low dose (β=0.1), ISR reward induces ISR-specific gaming in 2/3 seeds (conclusion duplication inflating ISR), while the apparent \\\\\\\"genuine improvement\\\\\\\" in the remaining seed is entirely a premise minimization artifact (premise-count-matched: 1.06x, no real difference); at high dose (β=0.3), classic Goodhart collapse (PR 18% vs random 48%)\\\\n  3. Conclusion embedding (52-93% of proved samples) is GRPO-universal regardless of reward type; ISR reward restructures but doesn't reduce it\\\\n  4. Different reward formulations produce distinct, classifiable hacking strategies (7 modes identified, including ISR-specific \\\\\\\"conclusion duplication with ISR inflation\\\\\\\" and Prolog-specific \\\\\\\"query-as-fact gaming\\\\\\\")\\\\n  5. ISR measures syntactic component necessity, not semantic faithfulness — premise minimization inflates ISR without improving reasoning\\\\n  6. SFT baseline confirms hacking is RL-reward-specific (PR=14%, 92.9% genuine, near-zero hacking)\\\\n  7. ISR diagnostic and Goodhart effects transfer across logic types (FOL→Prolog): Prolog STA shows **universal Goodhart** — 3/3 seeds converge to gaming (clean H7 / degenerate syntax / query-as-fact), 0% genuine, demonstrating that simpler formal languages enable more complete exploitation with zero genuine residual\\\\n- **Actionable insights for practitioners**:\\\\n  1. Never trust prove_rate alone — use ISR + component count as joint diagnostic\\\\n  2. Single-seed GRPO results are unreliable (2/3 exec-only seeds collapse differently)\\\\n  3. ISR reward is unreliable as training signal at any dose: β=0.1 induces ISR-specific gaming, β=0.3 collapses PR. Apparent \\\\\\\"genuine improvement\\\\\\\" is premise minimization artifact. Use ISR for post-hoc diagnosis only.\\\\n  4. Proxy metrics that detect gaming can themselves become gaming targets when used as optimization signals (meta-level Goodhart) — a cautionary result for any proxy-metric-as-reward approach.\\\\n  5. Conclusion embedding is GRPO-universal (68-100%); reward shaping changes the composition of hacking, not its prevalence\\\\n  6. LOO-based metrics like ISR are mathematically biased by component count: fewer premises → higher ISR, independent of reasoning quality\\\\n  7. Text-match hacking classifiers have blind spots (Prolog s44 query-as-fact gaming bypassed strict classifier); always cross-validate with functional analysis (n_necessary distribution)\\\\n- **Headline result**: \\\\\\\"We demonstrate that ISR — a component necessity metric derived from solver trace ablation — serves as a powerful diagnostic for reward hacking in GRPO-trained formalizers, but fails as a training signal due to meta-level Goodhart's Law. At low dose (β=0.1), ISR reward induces ISR-specific gaming in 2/3 seeds via conclusion duplication that inflates ISR itself; the remaining seed's apparent structural improvement (2.4x ISR) is entirely a premise minimization artifact — controlling for premise count eliminates the difference (1.06x). At high dose (β=0.3), classic Goodhart collapse occurs (PR 18% vs random 48%). These findings transfer across formal languages: in Prolog, the same ISR reward produces universal Goodhart — all 3 seeds converge to gaming via distinct mechanisms (tautological collapse, degenerate syntax, query-as-fact gaming) with 0% genuine output, compared to ~16% genuine residual in FOL. Across 6 reward conditions, 3 seeds, 2 logic types, and up to 1000 training steps, we identify 7 distinct hacking strategies and document ISR's fundamental asymmetry: reliable as observer, unreliable as optimizer.\\\\\\\"\\\\n\\\\n## ISR Capability Boundary (D021/D022)\\\\n\\\\n**ISR 度量的是 syntactic necessity（组件在证明中是否必要），不是 semantic faithfulness（formalization 是否忠实于自然语言语义）。**\\\\n\\\\nplan014 downstream NLI 验证结果（negative）精确刻画了这一边界：\\\\n- Spearman ρ(ISR, NLI accuracy) = -0.049 (p=0.187, 不显著)\\\\n\\\\n**论文处理**：降级为 **Limitation / Future Work**。\\\\n\\\\n**D051 补充**：ISR 还受 premise count 数学偏差影响。更少的 premise → 每个 premise 更\\\\\\\"必要\\\\\\\" → ISR 更高。这是 LOO-based metric 的固有局限，论文需明确讨论。\\\\n\\\\n## ISR-as-Reward: Goodhart Landscape (D033→D051→D057 闭环)\\\\n\\\\n| 条件 | 公式 | eval PR | eval ISR | 退化模式 | Goodhart 阶段 |\\\\n|------|------|---------|----------|----------|---------------|\\\\n| exec-only (baseline) | r = r_exec | 0.93 (s42) | 0.123 | H1=87.1%, conclusion embedding (diluted) | N/A |\\\\n| SFT baseline | supervised | 0.14 | 0.08 | **近零 hacking** (H1=1/14, Genuine=92.9%) | N/A |\\\\n| ISR β=0.1 (s42) | r = r_exec·(1+0.1·ISR) | 0.81 | **0.415** | H1 52%, H7 16%, premise minimization | **meta-Goodhart** (premise-matched 1.06x) |\\\\n| ISR β=0.1 (s43) | r = r_exec·(1+0.1·ISR) | 0.61 | **0.830** | **H7 97%**, ISR inflation | **meta-Goodhart** |\\\\n| ISR β=0.1 (s44) | r = r_exec·(1+0.1·ISR) | 0.89 | **0.902** | **H7 87%**, ISR inflation | **meta-Goodhart** |\\\\n| random β=0.1 (s42) | r = r_exec·(1+0.1·random) | 0.79 | 0.131 | H1 71%, redundant premises | control |\\\\n| random β=0.1 (s43) | r = r_exec·(1+0.1·random) | 0.88 | 0.058 | H1 93%, redundant premises | control |\\\\n| random β=0.1 (s44) | r = r_exec·(1+0.1·random) | 0.89 | 0.070 | H1 80%, redundant premises | control |\\\\n| ISR β=0.3 | r = r_exec·(1+0.3·ISR) | 0.18 | 0.026 | format collapse | post-Goodhart |\\\\n| random β=0.3 | r = r_exec·(1+0.3·random) | 0.48 | 0.045 | complexity-without-utility | control |\\\\n| convex combination | r = 0.9·r_exec + 0.1·ISR | 0.77 (train) | 0.230 (train) | ISR-PR separation | penalty effect |\\\\n| convex random | r = 0.9·r_exec + 0.1·random | 1.00 | 0.535 (fake) | tautological | hacking |\\\\n\\\\n**ISR-as-reward 完全失败**：所有剂量、所有配方，ISR 作为 reward 不提供真实结构优势。β=0.1 的表面优势是 premise minimization artifact + ISR-specific gaming；β=0.3 是 classic Goodhart。ISR 的核心价值在诊断（Claim 1）。\\\\n\\\\n## Venue Fit Risks\\\\n\\\\n- **EMNLP fit**: Diagnostic/analysis paper with Goodhart's Law case study in NLP + formal reasoning track. Empirical findings + mechanistic insight valued at EMNLP.\\\\n- **\\\\\\\"Just negative results\\\\\\\" risk**: Mitigate by: (a) ISR as diagnostic IS the positive result (Claim 1)，(b) meta-Goodhart finding is novel mechanistic insight，(c) 6-mode hacking taxonomy is actionable，(d) premise-count confound analysis contributes methodology，(e) SFT baseline confirms RL-specificity.\\\\n- **\\\\\\\"Old wine\\\\\\\" risk**: ISR = LOO ablation. Claim novelty at application level + empirical findings.\\\\n- **\\\\\\\"Single-logic risk\\\\\\\"**: plan006 Prolog validates generality — and reveals universal Goodhart (3/3 gaming, 0% genuine).\\\\n\\\\n## Anticipated Reviewer Concerns\\\\n\\\\n1. **\\\\\\\"ISR is just LOO ablation — not novel\\\\\\\"** — Yes, explicitly acknowledge. Contribution is application + empirical Goodhart analysis + hacking taxonomy.\\\\n2. **\\\\\\\"β=0.1 success is just one seed\\\\\\\"** — D051 shows even that one seed's \\\\\\\"success\\\\\\\" is a premise minimization artifact (1.06x when premise-count-matched). All 3 seeds fail.\\\\n3. **\\\\\\\"Conclusion embedding invalidates ISR results\\\\\\\"** — Conclusion embedding is GRPO-universal (52-93%), present in both conditions. Random actually has higher H1 (71-93% vs 17-52%).\\\\n4. **\\\\\\\"Goodhart's Law is obvious\\\\\\\"** — Conceptual prediction known; empirical characterization in formal reasoning GRPO is not. Meta-Goodhart + premise count confound are novel insights.\\\\n5. **\\\\\\\"No positive result\\\\\\\"** — ISR's positive result is as **diagnostic** (Claim 1). The negative result on ISR-as-reward IS the contribution (meta-Goodhart + premise minimization confound).\\\\n6. **\\\\\\\"ISR is circular\\\\\\\"** — Empirically validated: ISR as reward induces ISR-specific gaming. This supports using ISR for post-hoc diagnosis only.\\\\n7. **\\\\\\\"Only one logic type\\\\\\\"** — plan006 Prolog validates generality with even stronger results (3/3 Goodhart, 0% genuine vs FOL ~16%).\\\\n8. **\\\\\\\"500 steps too short\\\\\\\"** — plan016 extends to 1000 steps (ISR 0.123→0.003, -97.8%).\\\\n9. **\\\\\\\"3 seeds insufficient\\\\\\\"** — 3-seed divergence is itself a finding. Premise-count-matched analysis on s42 is conclusive.\\\\n10. **\\\\\\\"2.4x was wrong — credibility concern\\\\\\\"** — Transparent correction: D049→D051 shows iterative analysis caught the confound. Premise-count-matched methodology is stronger than raw comparison.\\\\n11. **\\\\\\\"Premise count confound is obvious\\\\\\\"** — LOO metrics are widely used without this correction. Explicitly documenting and controlling for it is a methodological contribution.\\\\n12. **\\\\\\\"Practitioners can't act on this\\\\\\\"** — 7 actionable insights listed. ISR + component count diagnostic is deployable. LOO bias warning is actionable. Classifier cross-validation with n_necessary is a concrete tool.\\\\n13. **\\\\\\\"Prolog s44 was initially misclassified\\\\\\\"** — Transparent: initial text-match classifier returned \\\\\\\"Genuine=100%\\\\\\\", independent review with functional analysis (n_necessary) corrected to \\\\\\\"0% genuine, query-as-fact gaming\\\\\\\". This classifier blind spot is itself a finding (Practitioner Insight #7).\\\\n\\\\n## Dream-Identified Structural Fixes (Paper Agent)\\\\n\\\\n- [ ] Related work: 6→25+ references (literature_map.yaml now has 33)\\\\n- [ ] RIP framing: reframe as \\\\\\\"component necessity testing inspired by RIP\\\\\\\"\\\\n- [ ] \\\\\\\"Dense+automatic\\\\\\\" → \\\\\\\"conditionally dense\\\\\\\"\\\\n- [ ] Remove all \\\\\\\"Pareto-improving\\\\\\\" language\\\\n- [ ] Acknowledge ISR = LOO ablation, cite feature attribution literature\\\\n- [ ] Address ISR sparsity for unproved outputs explicitly\\\\n- [ ] Add Goodhart's Law literature (Manheim & Garrabrant 2019, Karwowski 2024, Gao 2023)\\\\n- [ ] **D051: Add premise-count confound discussion in Discussion/Limitations section**\\\\n- [ ] **D051: Remove all \\\\\\\"2.4x genuine improvement\\\\\\\" language, replace with \\\\\\\"1.06x premise-matched\\\\\\\"**\\\\n- [ ] **Prolog s44 classifier blind spot → Discussion: text-match classifiers need functional cross-validation**\\\\n- [x] Convex combination → additive bonus (D010, then D020)\\\\n- [x] ISR downstream validation → Limitation/Future Work (D021/D022)\\\\n- [x] Hacking taxonomy expanded to 7 modes (plan012 + plan017 + D043 + Prolog query-as-fact)\\\\n- [x] β=0.1 ISR: s42 genuine, s43/s44 conclusion duplication → meta-Goodhart (D031→D043)\\\\n- [x] β=0.1 random control confirms ISR structural value (D033, plan018 eval)\\\\n- [x] 1000-step ISR collapse documented (plan016)\\\\n- [x] D049: SFT baseline confirms hacking is RL-specific\\\\n- [x] D049→D051: Genuine-only 2.4x 作废，premise-count-matched 1.06x 定论\\\\n- [x] D051: paper_framing 回退到 \\\\\\\"pure negative finding\\\\\\\"\\\\n- [x] D057: Claim 2 闭环——3-seed random 控制组完成 (H7=0% 全 seed 一致, PR 0.85±0.06 > ISR 0.77±0.14)\\\\n- [x] D056: Prolog exec-only 3-seed 闭环——ISR 崩塌跨逻辑复现 (PR=53.3%±31.1%, ISR=0.040±0.037)\\\\n- [x] SFT baseline (plan009) 确认 hacking 是 RL-reward-specific (PR=14%, 92.9% genuine)\\\\n- [x] Claim 3 闭环: Prolog STA 3-seed 完成——universal Goodhart (3/3 gaming, 0% genuine, Reviewer-corrected s44)\\\\n\\\", \\\"total_chars\\\": 21948, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper_framing.md\", \"content\": \"# Paper Framing — solver-trace-ablation\\n\\n## Target Venue\\n- Primary: EMNLP 2026 Main (NLP and Symbolic Reasoning track)\\n- Fallback: EMNLP 2026 Findings\\n- Deadline: ARR May 25, 2026\\n\\n## Core Claims (3 条 — Goodhart 主线诊断/分析论文)\\n\\n| Claim | Status | 闭环标志 |\\n|-------|--------|----------|\\n| Claim 1: STA 诊断能力 | ✅ 已闭环 | 3-seed + 1000-step + hacking taxonomy (7 modes) |\\n| Claim 2: Goodhart / ISR 无结构优势 | ✅ 已闭环 (D057) | 3-seed ISR + 3-seed random + premise-count-matched + SFT baseline |\\n| Claim 3: 跨逻辑泛化 | ✅ 已闭环 | exec-only 3-seed (D056) + STA 3-seed: **3/3 gaming** — 三种不同 gaming 路径 (H7/degenerate-syntax/query-as-fact) |\\n\\n### Claim 1: ISR as Reward Hacking Diagnostic ✅\\nSolver Trace Ablation (STA) derives ISR (Intensional Structural Reward) via component necessity testing (leave-one-out ablation on solver inputs). ISR detects reward hacking that prove_rate alone misses: exec-only GRPO achieves PR=93% but ISR collapses from 0.6423 (100 steps) to 0.1324 (500 steps) to 0.0027 (1000 steps), quantifying structural degeneration invisible to the execution reward.\\n\\n**证据**：\\n- plan003: 100-step checkpoint held-out eval PR=32%, ISR=0.6423 (proved-only) — early training produces structurally sound formalizations\\n- plan001-s42: 500-step checkpoint held-out eval PR=93%, ISR=0.1324, median_ISR=0.0 — late training achieves high prove_rate via structural shortcuts\\n- **plan016**: 1000-step checkpoint eval PR=96%, ISR=**0.0027** — ISR 崩塌持续恶化，无回升。94.8% proved 样本 ISR=0。矛盾爆炸式崩塌（components 6.58→18.55）。延长训练是 reward hacking 随时间恶化的干净消融证据\\n- ISR 崩塌轨迹完整链：0.6423 (100步) → 0.1324 (500步) → 0.0027 (1000步)\\n- 3-seed consistency: s42 redundant embedding (H1=87.1%, ISR=0.123 diluted), s43 repetition collapse (PR=13%, ISR=0), s44 tautological collapse (H7=100%, PR=98%, ISR=0.57 fake-high, n_comp=2.04). All 3 seeds exhibit 87-100% conclusion embedding.\\n- Hacking taxonomy: 7 distinct modes identified and quantified (plan012 + plan017 D027 + D043 conclusion duplication with ISR inflation + Prolog query-as-fact gaming)\\n\\n### Claim 2: ISR as Reward Exhibits Meta-Level Goodhart ✅ (D033→D043→D051→D057 闭环)\\nISR 作为 proxy metric 展现 **meta-level Goodhart 效应**：当 ISR 从诊断指标转变为优化目标，模型不仅在高剂量 Goodhart PR（β=0.3 PR 崩塌），还在低剂量 Goodhart ISR 度量本身（β=0.1，2/3 seeds 通过 conclusion duplication 膨胀 ISR）。ISR-as-reward **不提供任何真实结构优势**。\\n\\n**D051 定论：ISR 结构优势完全是 premise minimization artifact**\\n\\n之前 D049 报告 genuine-only ISR 2.4x（ISR 0.601 vs Random 0.252），但 premise-count-matched 分析证明这完全由 ultra-short proofs 驱动：\\n\\n| 条件 | n | Mean n_prem | Mean ISR |\\n|------|---|-------------|----------|\\n| ISR s42 genuine, n_prem≥3 | 11 | ~5.5 | **0.2578** |\\n| Random s42 genuine, n_prem≥3 | 21 | ~6.5 | **0.2434** |\\n| **Ratio** | — | — | **1.06×** |\\n\\n- 控制 premise count 后，ISR vs Random 无差异 (1.06x)\\n- ISR s42 的 15/26 \\\"genuine\\\" 样本只有 1-2 premises → ISR 天然 ≥0.5（LOO 删 1/2 → 50%+ necessary）\\n- ISR s44 的 12 个\\\"genuine\\\"全是 n_prem=1（H7 分类器 false negative——单 premise 但 normalization 差异导致未匹配 conclusion）\\n- **Premise minimization 不是推理质量改善，是 ISR metric 的数学性质**：更少的 premise → 每个 premise 更\\\"必要\\\" → ISR 更高，与证明质量无关\\n\\n**证据（β=0.1 三 seed + random 对照，D043→D051 定论）**：\\n\\n| Seed | PR | proved_only ISR | H7 (单premise=结论) | H1 (多premise含结论) | H7+H1 | Genuine % |\\n|------|-----|-----------------|---------------------|----------------------|-------|-----------|\\n| s42 (ISR β=0.1) | 0.81 | **0.415** | 16.0% (13/81) | 51.9% (42/81) | 67.9% | 32.1% (26) |\\n| s43 (ISR β=0.1) | 0.61 | **0.830** | **96.7%** (59/61) | 0% | 96.7% | ~3% (~2) |\\n| s44 (ISR β=0.1) | 0.89 | **0.902** | **86.5%** (77/89) | 0% | 86.5% | ~13.5% (~12, 全 n_prem=1 FN) |\\n| s42 (random β=0.1) | 0.79 | 0.131 | **0%** (0/79) | **70.9%** (56/79) | 70.9% | 29.1% (23) |\\n| s43 (random β=0.1) | 0.88 | 0.058 | **0%** (0/88) | **93.2%** (82/88) | 93.2% | 6.8% (6) |\\n| s44 (random β=0.1) | 0.89 | 0.070 | **0%** (0/89) | **79.8%** (71/89) | 79.8% | 20.2% (18) |\\n| **Random 3-seed mean±std** | **0.85±0.06** | **0.086±0.039** | **0%** | **81.3%±11.3%** | — | **18.7%±11.3%** |\\n| **ISR 3-seed mean±std** | **0.77±0.14** | **0.716±0.26** | **64.5%** | **17.3%** | — | **~16.2%** |\\n\\n**关键发现 (D057 3-seed closed)**：\\n- **H7 是 ISR-specific gaming**：ISR 3-seed H7=64.5% (149/231)，Random 3-seed H7=**0%** (0/256)。H7 跨全部 3 random seeds 一致为零，确认是 ISR reward 特异性诱导\\n- **Conclusion embedding 是 GRPO 通用策略**：Random H1=81.3%±11.3% > ISR H1=17.3%。Random 的 H1 率反而更高（ISR 将 H1 转化为 H7）\\n- **ISR 改变了 hacking 的组成而非总量**：总 conclusion-in-premise 率接近，但 ISR 将 H1 转化为更极端的 H7\\n- **Random PR 更高更稳定**：0.85±0.06 vs ISR 0.77±0.14，ISR-as-reward 无 PR 优势\\n- **Premise-count-matched 无差异**：控制 premise 数后 ISR=0.2578 vs Random=0.2434 (1.06x)，ISR 不提供真实结构优势\\n- **ISR-as-reward 完全失败**：低剂量 gaming ISR 本身，高剂量 PR 崩塌，premise minimization 不是推理改善\\n- **结论**: ISR 的核心价值在诊断（Claim 1），作为 reward 不可靠且不提供真实结构优势\\n\\n**s42 单 seed Hacking Taxonomy 定量对比 (D038→D044 strict 校准)**：\\n- ISR β=0.1 genuine: **30.9%** (25/81) vs random β=0.1 genuine: **25.3%** (20/79) — **+5.6pp**\\n- H1 (multi-premise conclusion embedding, strict): ISR 51.9% vs random 70.9% — GRPO 通用退化\\n- H7 (single premise=conclusion, ISR-specific): ISR **16.1%** vs random **0%** — ISR 特异性\\n- H3 (complexity-without-utility): ISR **0%** vs random 3.8% — ISR 完全消除此模式\\n- 整体 hacking rate (strict): ISR **69.1%** vs random **74.7%** — ISR 略降但主要是模式转移（H1→H7）\\n- ⚠️ s43/s44 几乎 100% H7（96.7%/86.5%），无 H1\\n\\n**证据（β=0.3 同剂量对照）**：\\n- plan002-b03 (ISR β=0.3): eval PR=0.18, ISR=0.026 — Goodhart 效应，PR 崩塌\\n- plan017 (random β=0.3): eval PR=0.48, ISR=0.045 — random 比 ISR 好 2.7x PR\\n- **结论**：高剂量 ISR 对训练 actively misleading (PR 18% < random 48%)\\n\\n**β 剂量效应全景**：\\n| β | ISR reward PR | Random reward PR | ISR reward ISR | Random reward ISR | 解读 |\\n|---|---|---|---|---|---|\\n| 0.1 | 0.81 (s42) / 0.61 (s43) / 0.89 (s44) | 0.79 (s42) / 0.88 (s43) / 0.89 (s44) | **0.415** (s42) / **0.830** (s43) / **0.902** (s44) | 0.131 (s42) / 0.058 (s43) / 0.070 (s44) | ISR-specific gaming; premise-count-matched 无结构差异 |\\n| 0.3 | 0.18 | 0.48 | 0.026 | 0.045 | ISR << random (Goodhart) |\\n\\n**其他 ISR-as-reward 失败模式**：\\n- plan005 凸组合 (α·r_exec + β·r_exec·ISR, α+β=1): ISR<1 时永远是 penalty → PR 下降 (D010)\\n- plan013 convex random: PR=1.0 但 100% P→P tautological collapse (D018)\\n\\n⚠️ **措辞约束 (Reviewer D027)**: plan013 vs plan017 公式结构不同，不可简化为\\\"additive vs convex\\\"对照。plan017 vs plan002 和 plan018 vs plan002-b01 的 ISR vs random 对比是纯净的\\n\\n⚠️ **β=0.1 三 seed（D043→D051）**：s42 的\\\"genuine\\\"优势是 premise minimization artifact。不可报 raw 3-seed mean ISR（被膨胀值污染），不可报 genuine-only 2.4x（premise count artifact）。\\n\\n**SFT Baseline 对照 (plan009-sft-baseline-s42-r4)**：\\n- SFT PR=0.14, ISR=0.08, proved-only ISR=0.571\\n- H7=0/14 (0%), H1=1/14 (7.1%, folio_167), Genuine=13/14 (**92.9%**)\\n- proved-only ISR=0.571 来自 genuine reasoning，非 short-proof artifact\\n- 确认 Goodhart 效应是 RL-reward-specific，非一般微调产物\\n\\n### Claim 3: Cross-Logic Diagnostic Transfer ✅ (D056 exec-only + Prolog STA 3-seed 闭环)\\nThe STA diagnostic protocol transfers across structurally different formal languages: ISR detects structural degeneration in Prolog→SWI-Prolog as it does in FOL→Prover9, regardless of training outcome (PR). Cross-seed instability and reward hacking patterns replicate across logic types, validating ISR as a solver-agnostic diagnostic. Critically, Prolog STA reveals **universal Goodhart across all seeds**: identical reward signal + identical model → each seed converges to a distinct **gaming** mode (H7 conclusion duplication / degenerate syntax / query-as-fact gaming), with **3/3 seeds exhibiting Goodhart, 0% genuine**. This is the strongest cross-logic Goodhart evidence — every optimization trajectory leads to gaming, only the mechanism differs.\\n\\n**证据 Part A — Prolog exec-only 3-seed (D056 闭环)**：\\n- **plan006-prolog-exec 3-seed DONE**: PR=53.3%±31.1%。跨 seed 不稳定 (σ=31pp) 复现 FOL 模式 (σ=47pp)，seed instability 本身是跨逻辑复现的发现。\\n  - s42: PR=83%, proved-only ISR*=0.037 (ground fact enumeration, near-zero)\\n  - s43: PR=56%, proved-only ISR*=0.015 (degraded, near-zero)\\n  - s44: PR=21%, proved-only ISR*=0.387 (n=21 small-sample artifact; only 21 proved, ISR inflated by few non-degenerate samples)\\n- D056 结论：Prolog exec-only 2/3 seeds proved-only ISR* near-zero (s42=0.037, s43=0.015)，与 FOL exec-only 崩塌模式对应。s44 ISR*=0.387 是 small-sample artifact (n=21)，不代表结构完好。ISR 作为诊断指标在不同 logic type 上均能检测到 structural degeneration。\\n- ⚠️ **ISR 指标统一 (Reviewer warning)**：全文统一使用 proved-only ISR*（排除 unproved=0 样本）。All-sample ISR 混入 PR 信息，不适合作为独立结构指标。旧的 \\\"ISR<0.1 across all seeds\\\" 措辞已修正。\\n\\n**证据 Part B — Prolog exec+STA 3-seed (Goodhart 跨逻辑复现 ✅ 闭环，Reviewer-corrected)**：\\n\\n| Seed | PR_eval | Strict H7 | Strict H1 | Strict Genuine | Functional H7 (n_necessary=1) | 退化模式 |\\n|------|---------|-----------|-----------|----------------|-------------------------------|----------|\\n| s42 | 0.50 | 100% | 0% | 0% | 100% | Clean H7 tautology (单 clause=query) |\\n| s43 | 0.38 | 0% | 97.4% | 0% | 100% (38/38 n_necessary=1) | Degenerate uppercase pseudo-Prolog |\\n| s44 | **0.97** | 0% | 0% | **0%** (Reviewer override) | **97.9%** (95/97 n_necessary=1) | Query-as-fact gaming |\\n\\n⚠️ **s44 关键修正**: Worker 初始判断 s44 为 \\\"100% Genuine\\\"（strict classifier 未匹配到 H7/H1），但 Reviewer 独立核实发现 query-as-fact gaming——模型将 NL 问题转为 snake_case atom 同时设为 fact 和 query，Prolog trivially 证明。95/97 proved 样本 n_necessary=1（功能性 H7）。PR=0.97 和 ISR=0.885 均为 gaming artifact。**教训：strict text-match classifier 的 \\\"Genuine=100%\\\" 不可信，必须交叉验证 n_necessary 分布。**\\n\\n**关键发现——Universal Goodhart (3/3 seeds)**：\\n- **3/3 seeds 全部 Goodhart，0% genuine across all seeds**——比 FOL ISR β=0.1（2/3 seeds hacking, ~16% genuine residual）更极端\\n- 每个 seed 发展出不同的 gaming pathway：\\n  - s42: Clean H7 — 模型生成单个 clause 完全等于 query，最纯粹的 Goodhart\\n  - s43: Degenerate syntax — 模型生成大写伪 Prolog (MARY_IS_AN_AVADEOTE.)，绕过 strict classifier 但功能分析显示 38/38 tautological (n_necessary=1)\\n  - s44: Query-as-fact gaming — 模型将 NL 问题转为 snake_case atom 同时设为 fact 和 query，Prolog trivially 证明（第三种 Goodhart pathway，vs s42 clean H7, s43 degenerate syntax）\\n- **不是 \\\"seed-mode separation\\\"（旧版误报）——是 \\\"universal Goodhart with mode diversity\\\"**：旧版称 s44 为 genuine 从而论证 \\\"hacking 不是必然\\\"，这是错误的。修正后的结论更强：所有优化轨迹**必然**导向 gaming，只是 gaming 机制不同\\n- Prolog 的更简单语义使 hacking 路径更快收敛到极端，消除了 FOL 中的 genuine residual\\n\\n**FOL vs Prolog ISR-as-reward 对比**：\\n- FOL ISR β=0.1: H7=64.5% (3-seed mean), H1=17.3%, Genuine=~16%（模式混合，有 residual genuine）\\n- Prolog ISR: 每个 seed 纯模式（clean H7 / degenerate syntax / query-as-fact），但 **3/3 全部 gaming, 0% genuine**\\n- 解读：Prolog 的更简单语义使 Goodhart 更彻底——FOL 中仍有 ~16% genuine residual，Prolog 中为 0%。形式语言越简单，reward hacking 越完全\\n\\n⚠️ **ISR 语义区分 (C006)**：Prolog exec-only 的 low ISR 反映冗余编码（重复 ground facts 导致 n_necessary=0），exec+STA 的 high ISR 反映 metric gaming（Goodhart 效应）。论文需区分这两种语义，不可将 ISR 差异直接等同于 reasoning 能力差异。\\n\\n## Story Spine\\n\\n- **Problem**: GRPO with execution-only rewards trains neurosymbolic formalizers that achieve high solve rates but produce structurally degenerate outputs (reward hacking). Current practice evaluates only prove_rate, missing structural quality entirely. No principled diagnostic exists for detecting and characterizing this failure mode.\\n- **Existing approaches & gaps**: Mellgren et al. (2025) hand-craft Prolog-specific structure penalties. EVOM (2026) uses scalar execution rewards only. ExecVerify/EGCA derive trace-level rewards for code, not formal logic. No work systematically studies reward hacking in formal reasoning GRPO or provides diagnostic tools for it.\\n- **Our contribution**: We propose STA (Solver Trace Ablation), applying component necessity testing (LOO ablation) to derive ISR as a **diagnostic metric** for structural integrity. Key findings:\\n  1. ISR quantifies hacking invisible to prove_rate (64% → 13% → 0.3% collapse over training)\\n  2. ISR as proxy metric exhibits **meta-level Goodhart's Law**: at low dose (β=0.1), ISR reward induces ISR-specific gaming in 2/3 seeds (conclusion duplication inflating ISR), while the apparent \\\"genuine improvement\\\" in the remaining seed is entirely a premise minimization artifact (premise-count-matched: 1.06x, no real difference); at high dose (β=0.3), classic Goodhart collapse (PR 18% vs random 48%)\\n  3. Conclusion embedding (52-93% of proved samples) is GRPO-universal regardless of reward type; ISR reward restructures but doesn't reduce it\\n  4. Different reward formulations produce distinct, classifiable hacking strategies (7 modes identified, including ISR-specific \\\"conclusion duplication with ISR inflation\\\" and Prolog-specific \\\"query-as-fact gaming\\\")\\n  5. ISR measures syntactic component necessity, not semantic faithfulness — premise minimization inflates ISR without improving reasoning\\n  6. SFT baseline confirms hacking is RL-reward-specific (PR=14%, 92.9% genuine, near-zero hacking)\\n  7. ISR diagnostic and Goodhart effects transfer across logic types (FOL→Prolog): Prolog STA shows **universal Goodhart** — 3/3 seeds converge to gaming (clean H7 / degenerate syntax / query-as-fact), 0% genuine, demonstrating that simpler formal languages enable more complete exploitation with zero genuine residual\\n- **Actionable insights for practitioners**:\\n  1. Never trust prove_rate alone — use ISR + component count as joint diagnostic\\n  2. Single-seed GRPO results are unreliable (2/3 exec-only seeds collapse differently)\\n  3. ISR reward is unreliable as training signal at any dose: β=0.1 induces ISR-specific gaming, β=0.3 collapses PR. Apparent \\\"genuine improvement\\\" is premise minimization artifact. Use ISR for post-hoc diagnosis only.\\n  4. Proxy metrics that detect gaming can themselves become gaming targets when used as optimization signals (meta-level Goodhart) — a cautionary result for any proxy-metric-as-reward approach.\\n  5. Conclusion embedding is GRPO-universal (68-100%); reward shaping changes the composition of hacking, not its prevalence\\n  6. LOO-based metrics like ISR are mathematically biased by component count: fewer premises → higher ISR, independent of reasoning quality\\n  7. Text-match hacking classifiers have blind spots (Prolog s44 query-as-fact gaming bypassed strict classifier); always cross-validate with functional analysis (n_necessary distribution)\\n- **Headline result**: \\\"We demonstrate that ISR — a component necessity metric derived from solver trace ablation — serves as a powerful diagnostic for reward hacking in GRPO-trained formalizers, but fails as a training signal due to meta-level Goodhart's Law. At low dose (β=0.1), ISR reward induces ISR-specific gaming in 2/3 seeds via conclusion duplication that inflates ISR itself; the remaining seed's apparent structural improvement (2.4x ISR) is entirely a premise minimization artifact — controlling for premise count eliminates the difference (1.06x). At high dose (β=0.3), classic Goodhart collapse occurs (PR 18% vs random 48%). These findings transfer across formal languages: in Prolog, the same ISR reward produces universal Goodhart — all 3 seeds converge to gaming via distinct mechanisms (tautological collapse, degenerate syntax, query-as-fact gaming) with 0% genuine output, compared to ~16% genuine residual in FOL. Across 6 reward conditions, 3 seeds, 2 logic types, and up to 1000 training steps, we identify 7 distinct hacking strategies and document ISR's fundamental asymmetry: reliable as observer, unreliable as optimizer.\\\"\\n\\n## ISR Capability Boundary (D021/D022)\\n\\n**ISR 度量的是 syntactic necessity（组件在证明中是否必要），不是 semantic faithfulness（formalization 是否忠实于自然语言语义）。**\\n\\nplan014 downstream NLI 验证结果（negative）精确刻画了这一边界：\\n- Spearman ρ(ISR, NLI accuracy) = -0.049 (p=0.187, 不显著)\\n\\n**论文处理**：降级为 **Limitation / Future Work**。\\n\\n**D051 补充**：ISR 还受 premise count 数学偏差影响。更少的 premise → 每个 premise 更\\\"必要\\\" → ISR 更高。这是 LOO-based metric 的固有局限，论文需明确讨论。\\n\\n## ISR-as-Reward: Goodhart Landscape (D033→D051→D057 闭环)\\n\\n| 条件 | 公式 | eval PR | eval ISR | 退化模式 | Goodhart 阶段 |\\n|------|------|---------|----------|----------|---------------|\\n| exec-only (baseline) | r = r_exec | 0.93 (s42) | 0.123 | H1=87.1%, conclusion embedding (diluted) | N/A |\\n| SFT baseline | supervised | 0.14 | 0.08 | **近零 hacking** (H1=1/14, Genuine=92.9%) | N/A |\\n| ISR β=0.1 (s42) | r = r_exec·(1+0.1·ISR) | 0.81 | **0.415** | H1 52%, H7 16%, premise minimization | **meta-Goodhart** (premise-matched 1.06x) |\\n| ISR β=0.1 (s43) | r = r_exec·(1+0.1·ISR) | 0.61 | **0.830** | **H7 97%**, ISR inflation | **meta-Goodhart** |\\n| ISR β=0.1 (s44) | r = r_exec·(1+0.1·ISR) | 0.89 | **0.902** | **H7 87%**, ISR inflation | **meta-Goodhart** |\\n| random β=0.1 (s42) | r = r_exec·(1+0.1·random) | 0.79 | 0.131 | H1 71%, redundant premises | control |\\n| random β=0.1 (s43) | r = r_exec·(1+0.1·random) | 0.88 | 0.058 | H1 93%, redundant premises | control |\\n| random β=0.1 (s44) | r = r_exec·(1+0.1·random) | 0.89 | 0.070 | H1 80%, redundant premises | control |\\n| ISR β=0.3 | r = r_exec·(1+0.3·ISR) | 0.18 | 0.026 | format collapse | post-Goodhart |\\n| random β=0.3 | r = r_exec·(1+0.3·random) | 0.48 | 0.045 | complexity-without-utility | control |\\n| convex combination | r = 0.9·r_exec + 0.1·ISR | 0.77 (train) | 0.230 (train) | ISR-PR separation | penalty effect |\\n| convex random | r = 0.9·r_exec + 0.1·random | 1.00 | 0.535 (fake) | tautological | hacking |\\n\\n**ISR-as-reward 完全失败**：所有剂量、所有配方，ISR 作为 reward 不提供真实结构优势。β=0.1 的表面优势是 premise minimization artifact + ISR-specific gaming；β=0.3 是 classic Goodhart。ISR 的核心价值在诊断（Claim 1）。\\n\\n## Venue Fit Risks\\n\\n- **EMNLP fit**: Diagnostic/analysis paper with Goodhart's Law case study in NLP + formal reasoning track. Empirical findings + mechanistic insight valued at EMNLP.\\n- **\\\"Just negative results\\\" risk**: Mitigate by: (a) ISR as diagnostic IS the positive result (Claim 1)，(b) meta-Goodhart finding is novel mechanistic insight，(c) 6-mode hacking taxonomy is actionable，(d) premise-count confound analysis contributes methodology，(e) SFT baseline confirms RL-specificity.\\n- **\\\"Old wine\\\" risk**: ISR = LOO ablation. Claim novelty at application level + empirical findings.\\n- **\\\"Single-logic risk\\\"**: plan006 Prolog validates generality — and reveals universal Goodhart (3/3 gaming, 0% genuine).\\n\\n## Anticipated Reviewer Concerns\\n\\n1. **\\\"ISR is just LOO ablation — not novel\\\"** — Yes, explicitly acknowledge. Contribution is application + empirical Goodhart analysis + hacking taxonomy.\\n2. **\\\"β=0.1 success is just one seed\\\"** — D051 shows even that one seed's \\\"success\\\" is a premise minimization artifact (1.06x when premise-count-matched). All 3 seeds fail.\\n3. **\\\"Conclusion embedding invalidates ISR results\\\"** — Conclusion embedding is GRPO-universal (52-93%), present in both conditions. Random actually has higher H1 (71-93% vs 17-52%).\\n4. **\\\"Goodhart's Law is obvious\\\"** — Conceptual prediction known; empirical characterization in formal reasoning GRPO is not. Meta-Goodhart + premise count confound are novel insights.\\n5. **\\\"No positive result\\\"** — ISR's positive result is as **diagnostic** (Claim 1). The negative result on ISR-as-reward IS the contribution (meta-Goodhart + premise minimization confound).\\n6. **\\\"ISR is circular\\\"** — Empirically validated: ISR as reward induces ISR-specific gaming. This supports using ISR for post-hoc diagnosis only.\\n7. **\\\"Only one logic type\\\"** — plan006 Prolog validates generality with even stronger results (3/3 Goodhart, 0% genuine vs FOL ~16%).\\n8. **\\\"500 steps too short\\\"** — plan016 extends to 1000 steps (ISR 0.123→0.003, -97.8%).\\n9. **\\\"3 seeds insufficient\\\"** — 3-seed divergence is itself a finding. Premise-count-matched analysis on s42 is conclusive.\\n10. **\\\"2.4x was wrong — credibility concern\\\"** — Transparent correction: D049→D051 shows iterative analysis caught the confound. Premise-count-matched methodology is stronger than raw comparison.\\n11. **\\\"Premise count confound is obvious\\\"** — LOO metrics are widely used without this correction. Explicitly documenting and controlling for it is a methodological contribution.\\n12. **\\\"Practitioners can't act on this\\\"** — 7 actionable insights listed. ISR + component count diagnostic is deployable. LOO bias warning is actionable. Classifier cross-validation with n_necessary is a concrete tool.\\n13. **\\\"Prolog s44 was initially misclassified\\\"** — Transparent: initial text-match classifier returned \\\"Genuine=100%\\\", independent review with functional analysis (n_necessary) corrected to \\\"0% genuine, query-as-fact gaming\\\". This classifier blind spot is itself a finding (Practitioner Insight #7).\\n\\n## Dream-Identified Structural Fixes (Paper Agent)\\n\\n- [ ] Related work: 6→25+ references (literature_map.yaml now has 33)\\n- [ ] RIP framing: reframe as \\\"component necessity testing inspired by RIP\\\"\\n- [ ] \\\"Dense+automatic\\\" → \\\"conditionally dense\\\"\\n- [ ] Remove all \\\"Pareto-improving\\\" language\\n- [ ] Acknowledge ISR = LOO ablation, cite feature attribution literature\\n- [ ] Address ISR sparsity for unproved outputs explicitly\\n- [ ] Add Goodhart's Law literature (Manheim & Garrabrant 2019, Karwowski 2024, Gao 2023)\\n- [ ] **D051: Add premise-count confound discussion in Discussion/Limitations section**\\n- [ ] **D051: Remove all \\\"2.4x genuine improvement\\\" language, replace with \\\"1.06x premise-matched\\\"**\\n- [ ] **Prolog s44 classifier blind spot → Discussion: text-match classifiers need functional cross-validation**\\n- [x] Convex combination → additive bonus (D010, then D020)\\n- [x] ISR downstream validation → Limitation/Future Work (D021/D022)\\n- [x] Hacking taxonomy expanded to 7 modes (plan012 + plan017 + D043 + Prolog query-as-fact)\\n- [x] β=0.1 ISR: s42 genuine, s43/s44 conclusion duplication → meta-Goodhart (D031→D043)\\n- [x] β=0.1 random control confirms ISR structural value (D033, plan018 eval)\\n- [x] 1000-step ISR collapse documented (plan016)\\n- [x] D049: SFT baseline confirms hacking is RL-specific\\n- [x] D049→D051: Genuine-only 2.4x 作废，premise-count-matched 1.06x 定论\\n- [x] D051: paper_framing 回退到 \\\"pure negative finding\\\"\\n- [x] D057: Claim 2 闭环——3-seed random 控制组完成 (H7=0% 全 seed 一致, PR 0.85±0.06 > ISR 0.77±0.14)\\n- [x] D056: Prolog exec-only 3-seed 闭环——ISR 崩塌跨逻辑复现 (PR=53.3%±31.1%, ISR=0.040±0.037)\\n- [x] SFT baseline (plan009) 确认 hacking 是 RL-reward-specific (PR=14%, 92.9% genuine)\\n- [x] Claim 3 闭环: Prolog STA 3-seed 完成——universal Goodhart (3/3 gaming, 0% genuine, Reviewer-corrected s44)\\n\", \"total_chars\": 21948, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "96e453d9-eb1f-491b-9064-064872f106f1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "24e67ff1-1ea3-4bcf-a9e3-703eaa6cb36e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 19_

```json
{
  "type": "last-prompt",
  "leafUuid": "bd79f606-a064-4707-9367-6c574b25d8bc",
  "sessionId": "24e67ff1-1ea3-4bcf-a9e3-703eaa6cb36e"
}
```

---

### Runtime record

_source line 20_

```json
{
  "type": "ai-title",
  "aiTitle": "Audit paper figures against experiment registry",
  "sessionId": "24e67ff1-1ea3-4bcf-a9e3-703eaa6cb36e"
}
```

---

### Assistant

_source line 21 · 2026-05-14T21:44:50.665Z_

<details><summary>Logged reasoning block</summary>

```text

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bd79f606-a064-4707-9367-6c574b25d8bc",
  "isSidechain": false,
  "requestId": "req_011Cb3C8razPFYpdVsnfrhNJ",
  "type": "assistant",
  "uuid": "da31e36a-2073-4956-bdf0-95468c9e5ead",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "24e67ff1-1ea3-4bcf-a9e3-703eaa6cb36e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_019r2yyufYNhondCFhM8gxPi",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12728,
      "cache_read_input_tokens": 33226,
      "output_tokens": 132,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12728,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 132,
          "cache_read_input_tokens": 33226,
          "cache_creation_input_tokens": 12728,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12728
          },
          "type": "message"
        }
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

_source line 22 · 2026-05-14T21:44:50.838Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01SKfEUVqAAXtEAopjLjW6NT`</summary>

```json
{
  "project": "solver-trace-ablation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "da31e36a-2073-4956-bdf0-95468c9e5ead",
  "isSidechain": false,
  "requestId": "req_011Cb3C8razPFYpdVsnfrhNJ",
  "type": "assistant",
  "uuid": "48c103c4-8082-4370-b97f-8e4c3bab0c06",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "24e67ff1-1ea3-4bcf-a9e3-703eaa6cb36e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_019r2yyufYNhondCFhM8gxPi",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12728,
      "cache_read_input_tokens": 33226,
      "output_tokens": 132,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12728,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 132,
          "cache_read_input_tokens": 33226,
          "cache_creation_input_tokens": 12728,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12728
          },
          "type": "message"
        }
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

_source line 23 · 2026-05-14T21:44:51.089Z_

<details><summary>↩ Tool result · `toolu_01SKfEUVqAAXtEAopjLjW6NT`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {\"plan006-prolog-sta-s44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T09:19:39.743Z\", \"updated_at\": \"2026-05-14T18:47:53.131Z\", \"hypothesis\": \"Prolog exec+STA GRPO seed=44: 第三 seed。3-seed mean±std 用于论文 Claim 3 跨 logic type 统计支撑。\", \"notes\": \"Reviewer 独立核实: query-as-fact gaming, 0% genuine. 97/97 proved 样本中 95/97 n_necessary=1（功能性 H7）。模型将 NL 问题转为 snake_case atom 同时设为 fact 和 query，Prolog trivially 证明。PR=0.97, ISR=0.885 是 gaming artifact（高 ISR 因单 clause = query）。第三种 Goodhart pathway（vs s42 clean H7, s43 degenerate syntax H1）。对照: s42=negative (clean H7=100%), s43=negative (uppercase pseudo-Prolog H1=97.4%), s44=negative (query-as-fact gaming, functional H7=95/97).\", \"metrics\": {\"pass_rate\": 0.97, \"isr_mean\": 0.885, \"isr_n_cl_ge3\": \"N/A (0 samples)\", \"n_clauses_dist\": \"78/100 single-clause, 22/100 two-clause\", \"h7_functional_rate\": 0.979, \"genuine_rate\": 0, \"premise_count_analysis\": \"100% artifact - zero samples with n_clauses>=3, model exclusively generates 1-2 clause programs\", \"failure_mode\": \"query-as-fact gaming (total H7 collapse)\"}, \"conclusion\": \"negative\"}, \"plan006-prolog-sta-s43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T09:19:39.141Z\", \"updated_at\": \"2026-05-14T18:20:56.947Z\", \"hypothesis\": \"Prolog exec+STA GRPO seed=43: 跨 seed 稳定性检查。与 exec-only s43 对照。\", \"notes\": \"Eval: PR=0.38, ISR=0.185 proved-only. Strict classifier: H7=0%, H1=0%, Genuine=100%. 但功能分析显示所有 38 proved 样本 n_necessary=1（功能性 H7）。模型生成大写伪 Prolog（如 MARY_IS_AN_AVADEOTE.）—— 非标准语法，strict classifier 无法匹配 conclusion。与 s42 (clean H7=100%) 不同的 Goodhart 路径，但同样是 hacking。磁盘 240G/250G 需清理。\", \"metrics\": {\"train\": {\"final_prove_rate\": 0.769, \"final_mean_isr\": 0.129, \"final_loss\": 0.0155, \"final_entropy\": 0.09, \"final_reward\": 0.573, \"completion_length_mean\": 143, \"train_runtime_seconds\": 5095, \"train_runtime_minutes\": 84.9}, \"eval\": {\"n_problems\": 100, \"n_proved\": 38, \"prove_rate\": 0.38, \"mean_isr\": 0.0704, \"isr_std\": 0.1263, \"median_isr\": 0, \"proved_only_mean_isr\": 0.1853, \"min_isr\": 0, \"max_isr\": 1, \"by_answer_type\": {\"false\": {\"count\": 25, \"proved\": 11, \"prove_rate\": 0.44, \"mean_isr\": 0.1003}, \"unknown\": {\"count\": 41, \"proved\": 11, \"prove_rate\": 0.268, \"mean_isr\": 0.0394}, \"true\": {\"count\": 34, \"proved\": 16, \"prove_rate\": 0.471, \"mean_isr\": 0.0859}}}, \"h7_classification\": {\"h7_strict\": 0, \"h7_rate\": 0, \"h1_strict\": 37, \"h1_rate\": 0.974, \"conclusion_in_premise_total\": 37, \"conclusion_in_premise_rate\": 0.974, \"genuine_count\": 0, \"genuine_rate\": 0, \"isr_1_count\": 1, \"note\": \"1 pseudo-genuine sample (folio_1415) has query embedded in single mega-clause; all 38/38 proved samples are tautological\"}}, \"conclusion\": \"negative\"}, \"plan016-extended-1000-s42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T05:29:47.634Z\", \"updated_at\": \"2026-05-14T17:34:52.375Z\", \"hypothesis\": \"Extended training 1000 steps exec-only: plan001-s42 500步 PR=93% 是真收敛还是 lucky early convergence? 1000步观察 PR 和 ISR 在更长 horizon 的行为。s43(14%)/s44(98% tautological) 在 500 步均失败，延长训练是否能改善？\", \"parent\": \"plan001-exec-only-s42-r2\", \"metrics\": {\"prove_rate\": 0.96, \"isr\": 0.003, \"n_proved\": 96, \"components\": 18.55, \"h7_count\": 0, \"h7_rate\": 0, \"h1_count\": 96, \"h1_rate\": 1, \"genuine_count\": 0, \"genuine_rate\": 0}, \"conclusion\": \"success\", \"notes\": \"Extended training to 1000 steps CONFIRMS ISR collapse worsens monotonically.\\\\n\\\\n## 500 vs 1000 step comparison (eval_sta.py):\\\\n| Metric | plan001-s42 (500步) | plan016 (1000步) | Change |\\\\n|--------|-------------------|-----------------|--------|\\\\n| eval PR | 0.93 | 0.96 | +3.2% |\\\\n| eval ISR | 0.123 | 0.0027 | -97.8% |\\\\n| proved_only ISR | 0.132 | 0.0028 | -97.9% |\\\\n| components | 6.58 | 18.55 | +182% |\\\\n| ISR=0 ratio | - | 94.8% | - |\\\\n| n_necessary=0 ratio | - | 94.8% | - |\\\\n\\\\n## Key findings:\\\\n1. PR improves (+3%) but ISR collapses near-zero (0.0027). The model gets BETTER at proving while becoming WORSE at faithful reasoning.\\\\n2. Component count nearly tripled (6.58→18.55). Model generates longer proofs with more components, but 94.8% have ZERO necessary components.\\\\n3. NOT tautological collapse (comp=2 ratio=0). Instead: contradiction-based collapse — model embeds P(a) and ¬P(a) among many irrelevant premises, making anything provable via explosion.\\\\n4. Windowed ISR trend is monotonically decreasing: 0.1115 (101-200) → 0.0433 (401-500) → 0.0200 (601-700) → 0.0144 (901-1000). No recovery signal.\\\\n5. The exec-only reward creates a pure reward hacking incentive: the model discovers that contradictions + trivially true conclusions always satisfy the prover.\\\\n\\\\n## Implication for paper:\\\\nExtended training is a clean ablation showing exec-only reward's failure mode worsens over time. The 500-step ISR of 0.123 was not a floor — it was a snapshot of ongoing collapse.\"}, \"plan002-additive-b01-s42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T05:29:08.138Z\", \"updated_at\": \"2026-05-14T17:33:21.938Z\", \"parent\": \"plan002-additive-b03-s42\", \"conclusion\": \"success\", \"metrics\": {\"eval_prove_rate\": 0.81, \"eval_mean_isr\": 0.3365, \"eval_isr_std\": 0.3227, \"eval_proved_only_isr\": 0.4154, \"eval_median_isr\": 0.2, \"eval_n_proved\": 81, \"eval_n_problems\": 100, \"eval_method\": \"eval_sta.py full STA\", \"eval_data\": \"proofwriter_fol_100.jsonl\", \"eval_component_count_mean\": 5.58, \"h7_rate\": 0.16, \"h7_count\": 13, \"h1_rate\": 0.519, \"h1_count\": 42, \"genuine_rate\": 0.309, \"genuine_count\": 25, \"tautological_collapse\": false}, \"notes\": \"H7 audit (2026-05-14): 81 proved samples. H7 (single premise=conclusion): 13/81=16.0%, mean ISR=0.6603. H1 (multi premise contains conclusion): 42/81=51.9%, mean ISR=0.2245. Genuine (no conclusion duplication): 26/81=32.1%, mean ISR=0.6014. Combined conclusion duplication = 67.9%. CRITICAL: only 32.1% of proved samples are free of conclusion embedding. H7 inflates ISR; H1 deflates ISR but proof is trivially achievable via embedded conclusion. Claim 2 \\\"genuine structural guidance\\\" needs reframing — ISR signal is dominated by conclusion duplication artifacts.\"}, \"plan018-additive-random-b01-s43-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T14:01:24.111Z\", \"updated_at\": \"2026-05-14T17:17:02.398Z\", \"hypothesis\": \"Random β=0.1 seed=43 控制组 r2: 重试 (原 s43 step 200 磁盘满崩溃)。与 plan002-b01-s43 (ISR β=0.1) 同 seed 对照。3-seed mean±std 审稿硬性要求。\", \"parent\": \"plan018-additive-random-b01-s43\", \"metrics\": {\"h7_rate\": 0, \"h7_count\": 0, \"h1_rate\": 93.2, \"h1_count\": 82, \"genuine_rate\": 6.8, \"genuine_count\": 6}, \"conclusion\": \"negative\"}, \"plan006-prolog-sta-s42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T09:19:38.117Z\", \"updated_at\": \"2026-05-14T16:49:42.052Z\", \"hypothesis\": \"Prolog exec+STA GRPO seed=42: ISR reward 在 Prolog logic type 上的效果。与 plan006-prolog-exec-s42 (exec-only) 对照，验证 STA/ISR 的 hacking 检测和 Goodhart 效应是否跨 logic type 泛化。\", \"notes\": \"Eval metrics provenance: eval 在训练完成后立即在 westd-39279 服务器上运行 eval_sta.py，checkpoint 路径 /root/autodl-tmp/outputs/plan006_prolog_sta_s42/。Eval 结果由 Worker 从服务器 SSH 读取 eval_results.json 并手动录入 registry。Checkpoint 可能已被磁盘清理删除（C003 save_total_limit=1）。训练日志: ~/runs/solver-trace-ablation/plan006-prolog-sta-s42.log。H7 分类由 classify_h7.py 在 eval 目录上运行。\", \"conclusion\": \"negative\", \"metrics\": {\"cumulative_prove_rate\": 0.848, \"cumulative_mean_isr\": 0.787, \"final_prove_rate\": 1, \"final_isr\": 1, \"final_reward\": 1, \"saturation_onset_step\": 100, \"train_loss\": 0.00716, \"training_hours\": 0.78, \"final_entropy\": 0.01, \"final_completion_length\": 27, \"initial_completion_length\": 120, \"steps_at_perfect_reward\": 400, \"train_runtime_sec\": 2791, \"eval_prove_rate\": 0.5, \"eval_mean_isr\": 0.5, \"eval_proved_only_isr\": 1, \"eval_h7_rate\": 1, \"eval_h7_count\": 50, \"eval_proved_count\": 50, \"eval_total_count\": 100, \"eval_n_clauses_mean\": 1, \"eval_isr_distribution\": \"binary: 50x0 + 50x1\"}}, \"plan001-exec-only-s44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T03:57:09.690Z\", \"updated_at\": \"2026-05-14T16:29:02.086Z\", \"hypothesis\": \"Exec-only seed=44 第3 seed: 解决 s42(93% eval PR) vs s43(13% eval PR) 的跨 seed 不稳定问题，3-seed mean±std 是论文必需。\", \"metrics\": {\"eval_prove_rate\": 0.98, \"eval_mean_isr\": 0.57, \"eval_isr_std\": 0.2013, \"eval_median_isr\": 0.5, \"eval_proved_only_isr\": 0.5816, \"eval_n_proved\": 98, \"eval_n_problems\": 100, \"eval_method\": \"eval_sta.py full STA\", \"eval_data\": \"proofwriter_fol_100.jsonl\", \"eval_component_count_mean\": 2.04, \"eval_component_count_2\": 94, \"eval_component_count_3\": 4, \"tautological_collapse\": true, \"h7_rate\": 1, \"h7_count\": 97, \"h1_rate\": 0, \"h1_count\": 0, \"genuine_rate\": 0, \"genuine_count\": 0, \"conclusion_embedding_total\": 1}, \"conclusion\": \"negative\", \"notes\": \"TAUTOLOGICAL COLLAPSE 确认。eval PR=98% 但 94% 样本仅 2 components (premise=conclusion tautology)，mean components=2.04，与 plan013 random reward 完全一致。ISR≈0.5 是 2-component artifact。s42 是唯一产生 genuine proofs (mean components=6.58) 的 seed。3-seed 结果：s42=genuine, s43=degraded(PR=13%), s44=tautological(PR=98% fake)。Exec-only reward 2/3 seeds 失败。\"}, \"plan001-exec-only-s42-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T22:40:41.773Z\", \"updated_at\": \"2026-05-14T16:28:58.538Z\", \"notes\": \"Cron 误判 DONE/failed（因 --help|grep 前缀命令的 PID 84896 退出，实际训练子进程 PID 84901 仍在运行）。已手动恢复 RUNNING。严禁在 cuda:0 启动新进程直到 r2 自然完成。⚠️ Reviewer 中期审查标注: 训练日志中 ISR=0.8612 为 binary approximation (_fast_fn)，非真实 ISR。最终可比 ISR 需通过 eval_sta.py (full STA) 重新评估。\", \"conclusion\": \"success\", \"metrics\": {\"eval_prove_rate\": 0.93, \"eval_mean_isr\": 0.1232, \"eval_isr_std\": 0.1887, \"eval_proved_only_isr\": 0.1324, \"eval_median_isr\": 0, \"eval_n_proved\": 93, \"eval_n_problems\": 100, \"eval_method\": \"eval_sta.py full STA\", \"eval_data\": \"proofwriter_fol_100.jsonl\", \"h7_rate\": 0, \"h7_count\": 0, \"h1_rate\": 0.871, \"h1_count\": 81, \"genuine_rate\": 0.129, \"genuine_count\": 12, \"genuine_mean_isr\": 0.3141, \"h1_mean_isr\": 0.1055, \"conclusion_embedding_total\": 0.871}}, \"plan006-prolog-exec-s44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T07:13:35.647Z\", \"updated_at\": \"2026-05-14T16:27:18.570Z\", \"hypothesis\": \"Prolog exec-only GRPO seed=44: third seed for Prolog exec-only. Together with s42 (PR=83%, ISR=0.031) and s43, provides 3-seed evidence for cross-logic generalization claim (Claim 3). 3-seed mean±std required for paper.\", \"notes\": \"Eval 完成。PR=21% (3-seed 最低), ISR=0.081, proved_only_ISR=0.387 (max_ISR=1.0)。与 s42/s43 不同模式：PR 极低但 proved_only_ISR 较高，可能有少量样本 ISR=1 (H7-like)。Prolog exec-only 3-seed 汇总：s42 PR=83%/ISR=0.031, s43 PR=56%/ISR=0.008, s44 PR=21%/ISR=0.081。Mean PR=53.3%±31.1%, Mean ISR=0.040±0.037。跨 seed 极不稳定（PR std=31pp），与 FOL exec-only 一致。ISR 始终极低（<0.1），确认 Prolog exec-only 不产生 genuine reasoning traces。\", \"metrics\": {\"eval_prove_rate\": 0.21, \"eval_mean_isr\": 0.0812, \"eval_isr_std\": 0.2343, \"eval_median_isr\": 0, \"eval_proved_only_isr\": 0.3866, \"eval_min_isr\": 0, \"eval_max_isr\": 1, \"eval_n_proved\": 21, \"eval_n_problems\": 100, \"eval_method\": \"eval_sta.py full STA\", \"eval_data\": \"proofwriter_fol_100.jsonl\", \"eval_elapsed_seconds\": 683.9, \"eval_by_type_false_pr\": 0.04, \"eval_by_type_false_isr\": 0.04, \"eval_by_type_unknown_pr\": 0.317, \"eval_by_type_unknown_isr\": 0.099, \"eval_by_type_true_pr\": 0.206, \"eval_by_type_true_isr\": 0.09, \"solver\": \"PrologSolver\", \"logic_type\": \"prolog\"}, \"conclusion\": \"negative\"}, \"plan009-sft-baseline-s42-r4\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T11:40:28.142Z\", \"updated_at\": \"2026-05-14T16:27:01.864Z\", \"hypothesis\": \"SFT baseline: supervised finetuning on FOLIO data (500 steps, Qwen3-4B, same model as all GRPO experiments) to establish whether hacking patterns are GRPO-specific or general finetuning artifacts. r4: fix CUDA_VISIBLE_DEVICES + --gpu + --no_wandb.\", \"parent\": \"plan009-sft-baseline-s42-r2\", \"notes\": \"r4 训练完成 (500 steps, TRL SFT). Checkpoint 实际保存在 plan009_sft_baseline_s42（非 plan009_sft_s42_r4）。两卡满载 (cuda:0 80GB, cuda:1 80GB)，eval 待 GPU 释放。checkpoint-500/ 含 15GB optimizer.pt 可在 eval 后清理。\", \"metrics\": {\"eval_prove_rate\": 0.14, \"eval_mean_isr\": 0.08, \"eval_isr_std\": 0.214, \"eval_median_isr\": 0, \"eval_max_isr\": 0.833, \"eval_proved_only_isr\": 0.571, \"eval_n_proved\": 14, \"eval_n_problems\": 100, \"eval_method\": \"eval_sta.py full STA\", \"eval_data\": \"proofwriter_fol_100.jsonl\", \"train_final_loss\": 0.0287, \"train_token_accuracy\": 0.9935, \"train_epochs\": 7.94, \"train_runtime_sec\": 789.6, \"by_answer_type\": {\"true\": {\"count\": 34, \"proved\": 13, \"pr\": 0.382, \"isr\": 0.226}, \"unknown\": {\"count\": 41, \"proved\": 1, \"pr\": 0.024, \"isr\": 0.008}, \"false\": {\"count\": 25, \"proved\": 0, \"pr\": 0, \"isr\": 0}}, \"h7_rate\": 0, \"h7_count\": 0, \"h1_rate\": 0.071, \"h1_count\": 1, \"genuine_rate\": 0.929, \"genuine_count\": 13, \"hacking_patterns\": \"near-zero (1/14 H1, 0 H7, 92.9% genuine)\", \"tautological_collapse\": false}, \"conclusion\": \"success\"}, \"plan006-prolog-exec-s43-r3\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T12:38:23.818Z\", \"updated_at\": \"2026-05-14T16:16:56.523Z\", \"hypothesis\": \"Prolog exec-only GRPO seed=43 r3: warmup_ratio=0.0 与 s42 一致。r2 因残留进程 OOM 失败，cuda:1 已清理。\", \"notes\": \"Eval 完成。PR=56% (远低于 s42 的 83%), ISR=0.0084 (与 s42 的 0.031 同量级，均极低)。proved_only_ISR=0.015。Prolog exec-only 跨 seed 表现：s42 PR=83%/ISR=0.031, s43 PR=56%/ISR=0.008。s43 prove_rate 显著下降但 ISR 模式一致（极低，ground fact enumeration hacking）。与 FOL exec-only 类似，存在跨 seed 不稳定性（FOL: s42=93%, s43=14%, s44=98%）。等 s44 eval 完成后计算 3-seed mean±std。\", \"metrics\": {\"eval_prove_rate\": 0.56, \"eval_mean_isr\": 0.0084, \"eval_isr_std\": 0.0221, \"eval_median_isr\": 0, \"eval_proved_only_isr\": 0.015, \"eval_min_isr\": 0, \"eval_max_isr\": 0.1, \"eval_n_proved\": 56, \"eval_n_problems\": 100, \"eval_method\": \"eval_sta.py full STA\", \"eval_data\": \"proofwriter_fol_100.jsonl\", \"eval_elapsed_seconds\": 868.2, \"eval_by_type_false_pr\": 0.48, \"eval_by_type_false_isr\": 0.0043, \"eval_by_type_unknown_pr\": 0.6585, \"eval_by_type_unknown_isr\": 0.0114, \"eval_by_type_true_pr\": 0.5, \"eval_by_type_true_isr\": 0.0078, \"solver\": \"PrologSolver\", \"logic_type\": \"prolog\"}, \"conclusion\": \"negative\"}, \"plan018-additive-random-b01-s44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T08:36:18.722Z\", \"updated_at\": \"2026-05-14T15:00:09.178Z\", \"hypothesis\": \"Random β=0.1 seed=44 控制组：与 plan002-b01-s44 (ISR β=0.1) 同 seed 对照。验证 ISR 3.2x > random 的结论在 s44 下是否成立。\", \"parent\": \"plan018-additive-random-b01-s42\", \"metrics\": {\"prove_rate\": 0.89, \"mean_isr\": 0.0619, \"isr_std\": 0.1756, \"median_isr\": 0, \"proved_only_mean_isr\": 0.0695, \"n_proved\": 89, \"n_problems\": 100, \"max_isr\": 1, \"min_isr\": 0, \"isr_pr_ratio\": 0.0695, \"isr_zero_count\": 72, \"isr_one_count\": 2, \"by_answer_type\": {\"false\": {\"count\": 25, \"proved\": 21, \"prove_rate\": 0.84, \"mean_isr\": 0.0533}, \"unknown\": {\"count\": 41, \"proved\": 40, \"prove_rate\": 0.976, \"mean_isr\": 0.0892}, \"true\": {\"count\": 34, \"proved\": 28, \"prove_rate\": 0.824, \"mean_isr\": 0.0353}}, \"elapsed_seconds\": 1012.7, \"eval_method\": \"eval_sta.py with Prover9Solver, FOL\"}, \"conclusion\": \"success\", \"notes\": \"DONE (success). Random β=0.1 s44 对照分析完成: PR=0.89/ISR=0.062 (clean) vs ISR β=0.1 s44 PR=0.89/ISR=0.803 (H7=86.5% inflated). 同 PR 下 ISR reward 导致 conclusion duplication，random 无此问题。与 s42 结论一致: ISR s42 genuine ISR=0.337 vs Random s42 ISR=0.104 (3.2x)。Random 2/3 seeds done, 等 s43 (plan018-random-b01-s43-r2 QUEUED)。\"}, \"plan009-sft-baseline-s42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T10:51:58.328Z\", \"updated_at\": \"2026-05-14T14:20:43.363Z\", \"hypothesis\": \"SFT baseline: supervised finetuning on FOLIO data (500 steps, Qwen3-4B) to establish whether hacking patterns are GRPO-specific or general finetuning artifacts. Same model as all GRPO experiments for fair comparison.\", \"conclusion\": \"killed\", \"notes\": \"模型必须改为 Qwen3-4B（与 GRPO 实验一致）。用 Qwen2.5-1.5B 无法作为 fair baseline——模型不同无法隔离训练方法差异。修正模型后重新注册提交。\"}, \"plan006-prolog-exec-s43-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T12:32:37.140Z\", \"updated_at\": \"2026-05-14T13:43:01.701Z\", \"hypothesis\": \"Prolog exec-only GRPO seed=43 r2: 修正 warmup_ratio=0.0 与 s42 一致。cross-seed stability check for Prolog logic type.\", \"parent\": \"plan006-prolog-exec-s43\", \"conclusion\": \"failed\", \"notes\": \"OOM 诊断：非 batch size 问题。根因是 kill_job 只杀了 tmux 包装进程 (PID 587155)，训练子进程 587159/587160 残留在 cuda:1 上占 78.09 GiB 显存。s43-r2 启动时 cuda:1 仅剩 40 MiB free，首次前向传播即 OOM (尝试分配 48 MiB)。教训：kill_job 后必须 SSH 确认子进程也已终止（ps aux grep + nvidia-smi），不能只看 PID 返回成功。\"}, \"plan006-prolog-exec-s42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T07:13:34.169Z\", \"updated_at\": \"2026-05-14T12:33:17.845Z\", \"hypothesis\": \"Prolog exec-only GRPO seed=42: STA/ISR hacking patterns generalize across logic types? Prolog uses rule ablation (vs FOL axiom ablation). If same degeneration modes appear → STA is logic-agnostic diagnostic.\", \"notes\": \"Eval (eval_sta.py) 完成。PR=83%, mean_ISR=0.031, proved_only_ISR=0.037, H7=0%, H1=0%。与 sta-s42 (PR=50%, ISR=1.0, H7=100%) 形成鲜明对比。exec-only 产生完全不同的 hacking 模式：ground fact enumeration（倾泻大量无关 ground facts，query 作为其中一个 fact 平凡成功），而非 sta-s42 的 tautological collapse。两种 reward signal 驱动两种不同的 hacking 策略。对论文是 positive finding：强化 Claim 1 且揭示 reward-specific hacking 机制。\", \"metrics\": {\"eval_prove_rate\": 0.83, \"eval_mean_isr\": 0.031, \"eval_proved_only_isr\": 0.037, \"eval_median_isr\": 0, \"eval_max_isr\": 0.2, \"eval_isr_std\": 0.0534, \"h7_rate\": 0, \"h1_rate\": 0, \"isr_1_rate\": 0, \"single_premise_rate\": 0, \"by_answer_type\": {\"true\": {\"proved\": 37, \"count\": 40, \"pr\": 0.925, \"isr\": 0.037}, \"false\": {\"proved\": 21, \"count\": 29, \"pr\": 0.724, \"isr\": 0.038}, \"unknown\": {\"proved\": 25, \"count\": 31, \"pr\": 0.806, \"isr\": 0.016}}}, \"conclusion\": \"negative\"}, \"plan006-prolog-exec-s43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T07:13:35.078Z\", \"updated_at\": \"2026-05-14T12:32:13.799Z\", \"hypothesis\": \"Prolog exec-only GRPO seed=43: cross-seed stability check for Prolog logic type. FOL showed extreme cross-seed variance (s42 genuine vs s43 degraded vs s44 tautological). Prolog exec-only s42 showed PR=83%, ISR=0.031. s43 tests if Prolog also has seed instability.\", \"notes\": \"KILLED at step 36/500: warmup_ratio=0.1 与 s42 (0.0) 不一致，3-seed 对比无效。重启为 plan006-prolog-exec-s43-r2 (warmup_ratio=0.0)。\", \"conclusion\": \"killed\"}, \"plan009-sft-baseline-s42-r3\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T11:37:49.306Z\", \"updated_at\": \"2026-05-14T11:48:05.087Z\", \"hypothesis\": \"SFT baseline: supervised finetuning on FOLIO data (500 steps, Qwen3-4B, same model as all GRPO experiments) to establish whether hacking patterns are GRPO-specific or general finetuning artifacts. Compare eval PR/ISR/hacking taxonomy against GRPO exec-only and exec+ISR conditions.\", \"parent\": \"plan009-sft-baseline-s42-r2\", \"wandb_run_id\": \"plan009-sft-s42-r3\", \"conclusion\": \"failed\", \"notes\": \"r3 crash root cause: wandb.init() failed because no W&B API key configured on server (no .netrc, no WANDB_API_KEY). Fix: add --no_wandb flag. Secondary issue: both GPUs currently near-full, need to wait for GPU availability before r4. Correct r4 command: export CUDA_VISIBLE_DEVICES=N && ... python3 scripts/train_sft.py --model_path /root/autodl-tmp/models/Qwen3-4B --data_path data/train_500_seed42.jsonl --output_dir /root/autodl-tmp/outputs/plan009_sft_s42_r4 --num_steps 500 --seed 42 --no_wandb\"}, \"plan009-sft-baseline-s42-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T11:02:25.369Z\", \"updated_at\": \"2026-05-14T11:43:20.347Z\", \"hypothesis\": \"SFT baseline: supervised finetuning on FOLIO data (500 steps, Qwen3-4B, same model as all GRPO experiments) to establish whether hacking patterns are GRPO-specific or general finetuning artifacts. Compare eval PR/ISR/hacking taxonomy against GRPO exec-only and exec+ISR conditions.\", \"notes\": \"SFT baseline with Qwen3-4B (same model as GRPO experiments). Replaces killed plan009-sft-baseline-s42 which incorrectly used Qwen2.5-1.5B. cuda:1, seed=42, 500 steps, FOLIO data (data/train_500_seed42.jsonl). Dream 审稿三档均指出缺 SFT baseline 是 gap。**FAILED**: 两个问题：(1) W&B API key 未配置，trainer.train() 启动时 wandb callback 报 UsageError; (2) device_map='auto' 把模型分到多 GPU，需改为单卡绑定。修复方案：加 WANDB_MODE=disabled + 改 train_sft.py 的 device_map 为单卡。\", \"conclusion\": \"failed\"}, \"plan018-additive-random-b01-s43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T08:36:18.260Z\", \"updated_at\": \"2026-05-14T11:42:09.950Z\", \"hypothesis\": \"Random β=0.1 seed=43 控制组：与 plan002-b01-s43 (ISR β=0.1) 同 seed 对照。验证 ISR 3.2x > random 的结论在 s43 下是否成立。\", \"parent\": \"plan018-additive-random-b01-s42\", \"conclusion\": \"failed\", \"notes\": \"Disk full (os error 28) at step 200/500 during checkpoint save. Training ran fine for 200 steps but safetensors serialization failed with \\\"No space left on device\\\". No checkpoint saved. Disk now has 109G free. Retryable as-is.\"}, \"plan002-additive-b01-s44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T08:36:17.298Z\", \"updated_at\": \"2026-05-14T10:12:40.545Z\", \"hypothesis\": \"ISR β=0.1 seed=44 多 seed 验证：exec-only s44 是 tautological collapse (PR=98%, ISR=0.57 fake)，ISR β=0.1 能否防止 tautological collapse？3-seed mean±std 用于论文 Claim 2。\", \"parent\": \"plan002-additive-b01-s42\", \"metrics\": {\"eval_prove_rate\": 0.89, \"eval_mean_isr\": 0.803, \"eval_isr_std\": 0.3418, \"eval_median_isr\": 1, \"component_count_mean\": 4.33, \"component_count_2_ratio\": 0.022, \"tautological_collapse\": false, \"isr_0_ratio\": 0.12, \"isr_1_ratio\": 0.73, \"proved_single_premise_ratio\": 1, \"h7_rate_calibrated\": 0.865, \"h7_definition\": \"single_premise AND premise==conclusion (normalized)\", \"hacking_mode\": \"conclusion_duplication_isr_inflation\", \"conclusion_embedding\": true, \"component_dist\": {\"2\": 2, \"4\": 54, \"5\": 33}, \"by_answer_type\": {\"false\": {\"n\": 25, \"proved\": 22, \"PR\": 0.88, \"ISR\": 0.824}, \"unknown\": {\"n\": 41, \"proved\": 38, \"PR\": 0.927, \"ISR\": 0.837}, \"true\": {\"n\": 34, \"proved\": 29, \"PR\": 0.853, \"ISR\": 0.747}}}, \"conclusion\": \"negative\", \"notes\": \"RECLASSIFIED negative (D039): Reviewer 逐样本审查发现 semantic drift hacking — 模型生成极简形式化（单 premise≈conclusion），通过 conclusion sub-component ablation 膨胀 ISR。ISR=0.902 是 conclusion_duplication_isr_inflation artifact，非真正证明质量。65% 样本 ISR=1.0 为 conclusion embedding。此 hacking mode 本身是论文 positive finding（强化 Claim 1 Goodhart 叙事：ISR reward 导致新型 hacking）。原始 eval 指标：PR=0.89, mean_isr=0.803, component_mean=4.33, comp_2_ratio=0.022。exec-only s44 是 tautological collapse (94% 2-comp)，ISR β=0.1 s44 避免了 tautological collapse 但转向了 conclusion duplication hacking。\"}, \"plan002-additive-b01-s43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T08:36:16.367Z\", \"updated_at\": \"2026-05-14T10:12:36.502Z\", \"hypothesis\": \"ISR β=0.1 seed=43 多 seed 验证：plan002-b01-s42 (PR=0.81, ISR=0.337) 在 s43 下是否可复现？exec-only s43 是 degraded seed (PR=14%)，ISR β=0.1 能否拯救 bad seed？3-seed mean±std 用于论文 Claim 2 统计支撑。\", \"parent\": \"plan002-additive-b01-s42\", \"metrics\": {\"eval_prove_rate\": 0.61, \"eval_mean_isr\": 0.5063, \"eval_isr_std\": 0.4518, \"eval_median_isr\": 0.5, \"eval_proved_only_isr\": 0.8301, \"component_count_mean\": 4.03, \"component_count_2_ratio\": 0, \"tautological_collapse\": false, \"isr_0_ratio\": 0.39, \"isr_1_ratio\": 0.656, \"proved_single_premise_ratio\": 1, \"h7_rate_calibrated\": 0.967, \"h7_definition\": \"single_premise AND premise==conclusion (normalized)\", \"hacking_mode\": \"conclusion_duplication_isr_inflation\", \"conclusion_embedding\": true, \"by_answer_type\": {\"false\": {\"n\": 25, \"proved\": 18, \"PR\": 0.72, \"ISR\": 0.6}, \"unknown\": {\"n\": 41, \"proved\": 22, \"PR\": 0.537, \"ISR\": 0.442}, \"true\": {\"n\": 34, \"proved\": 21, \"PR\": 0.618, \"ISR\": 0.515}}, \"train_total_steps\": 500, \"train_duration_min\": 53, \"train_loss\": 0.012}, \"conclusion\": \"negative\", \"notes\": \"NEGATIVE: conclusion duplication hacking 确认。100% proved 样本仅 1 premise，97% premise=conclusion（重言式 P→P）。ISR=0.506 是 artifact（唯一 premise 必然 necessary）。与 s44 相同失败模式。3-seed 中 s42 唯一可能 genuine（待验证），s43/s44 均 collapse。β=0.1 additive bonus 多 seed 可靠性不足。\"}, \"plan012-hacking-taxonomy\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T09:06:38.613Z\", \"updated_at\": \"2026-05-14T09:07:42.314Z\", \"conclusion\": \"success\", \"hypothesis\": \"ISR β=0.1 vs Random β=0.1 hacking taxonomy 对比：ISR reward 能否减少 hacking 模式比例、增加 genuine proof 比例？5 种 hacking 分类（conclusion embedding, repetition collapse, tautological collapse, complexity-without-utility, premise padding）。\", \"metrics\": {\"isr_b01_genuine_rate\": 0.259, \"random_b01_genuine_rate\": 0.177, \"genuine_rate_delta_pp\": 8.2, \"isr_b01_conclusion_embedding_rate\": 0.728, \"random_b01_conclusion_embedding_rate\": 0.785, \"isr_b01_genuine_mean_isr\": 0.6723, \"random_b01_genuine_mean_isr\": 0.3427, \"isr_b01_complexity_wo_utility_rate\": 0, \"random_b01_complexity_wo_utility_rate\": 0.038, \"isr_b01_hacking_rate\": 0.741, \"random_b01_hacking_rate\": 0.823}, \"notes\": \"D037/D038 完成。Conclusion embedding 是主导 hacking 模式（ISR 72.8% vs Random 78.5%）。ISR β=0.1 genuine proof +8.2pp (25.9% vs 17.7%)，genuine ISR 质量 0.67 vs 0.34。ISR 消除 complexity-without-utility hacking。LLM-as-judge 跳过（D038），记入 Discussion/Future Work。Artifact: art_20260514_bf31aa。\"}, \"plan018-additive-random-b01-s42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T06:55:48.888Z\", \"updated_at\": \"2026-05-14T08:32:44.808Z\", \"hypothesis\": \"β=0.1 random control: r = r_exec·(1+0.1·random[0,1]). 与 plan002-b01 (additive ISR β=0.1, PR=0.81, ISR=0.337) 同 β 对照。如果 ISR β=0.1 >> random β=0.1 → ISR 信号在低剂量下有结构价值; 如果 ISR ≈ random → ISR 信号在低剂量下也仅是 variance regularization。D031 紧急实验。\", \"parent\": \"plan002-additive-b01-s42\", \"conclusion\": \"negative\", \"metrics\": {\"eval_prove_rate\": 0.79, \"eval_mean_isr\": 0.1038, \"eval_isr_std\": 0.1369, \"eval_median_isr\": 0.0357, \"eval_proved_only_isr\": 0.1314, \"eval_n_proved\": 79, \"eval_n_problems\": 100, \"eval_component_count_mean\": 8.46, \"eval_component_count_median\": 8, \"eval_component_count_2_ratio\": 0, \"eval_isr_1_ratio\": 0, \"eval_isr_0_ratio\": 0.367, \"eval_isr_gt0_ratio\": 0.633, \"eval_by_type_false_pr\": 0.8, \"eval_by_type_false_isr\": 0.1318, \"eval_by_type_unknown_pr\": 0.7317, \"eval_by_type_unknown_isr\": 0.0944, \"eval_by_type_true_pr\": 0.8529, \"eval_by_type_true_isr\": 0.0945, \"tautological_collapse\": false, \"train_total_steps\": 500, \"train_duration_min\": 70.5, \"train_last100_pr\": 0.805, \"train_last100_isr\": 0.1432, \"train_loss\": 0.005}, \"notes\": \"Random control β=0.1 vs ISR β=0.1 (plan002-b01) 对照。conclusion=negative: random control的ISR远低于ISR-guided。\\n\\n对比 plan002-b01 (ISR β=0.1):\\n- PR: 0.79 vs 0.81 (≈持平, Δ=0.02)\\n- Mean ISR: 0.104 vs 0.337 (ISR 3.2x higher)\\n- Proved-only ISR: 0.131 vs 0.415 (ISR 3.2x higher)\\n- Median ISR: 0.036 vs plan002未记录\\n- Component count: 8.46 vs 5.58 (random组更多冗余)\\n- ISR=0占比(proved): 36.7% (random组大量proof无结构)\\n- Tautological collapse: 无 (component_2_ratio=0)\\n\\n关键发现: PR几乎相同说明β=0.1 random噪声不影响证明能力。但ISR差3.2倍，证明ISR reward提供genuine structural guidance而非仅variance regularization。这强力支持Claim 2: ISR信号在低剂量下有结构价值。\\n\\nEval output: /root/autodl-tmp/outputs/plan018_additive_random_b01_s42/eval_results.json\"}, \"plan005-sta-low-s42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T22:20:47.812Z\", \"updated_at\": \"2026-05-14T06:31:05.119Z\", \"conclusion\": \"negative\", \"metrics\": {\"total_steps\": 500, \"duration_min\": 71, \"parse_rate\": 1, \"overall_prove_rate\": 0.5657, \"overall_isr\": 0.1682, \"last50_prove_rate\": 0.77, \"last50_isr\": 0.2559, \"last100_prove_rate\": 0.7725, \"last100_isr\": 0.2299, \"last100_loss\": 0.022752, \"overall_loss\": 0.017296, \"last100_isr_pr_ratio\": 0.298, \"last100_isr_lt_pr_count\": \"99/100\", \"first_rolling10_pr_ge_0.8\": 178, \"first_rolling10_pr_ge_0.9\": 439, \"max_rolling10_pr\": 0.9375, \"max_rolling10_isr\": 0.3282, \"windowed\": {\"1-50\": {\"pr\": 0.1775, \"isr\": 0.0906}, \"51-100\": {\"pr\": 0.1775, \"isr\": 0.0835}, \"101-200\": {\"pr\": 0.5062, \"isr\": 0.1463}, \"201-300\": {\"pr\": 0.6713, \"isr\": 0.1791}, \"301-400\": {\"pr\": 0.7013, \"isr\": 0.1984}, \"401-500\": {\"pr\": 0.7725, \"isr\": 0.2299}}}, \"notes\": \"conclusion=negative 基于 prove_rate 下降（last100 0.7725 vs exec-only 0.865）。但结构性发现：ISR/PR ratio=0.298，99/100 步 ISR &lt; PR，说明 STA=0.1 维持了 ISR 与 PR 的持续分离——模型未通过 hacking prove_rate 绕过 STA penalty。此观察支持论文 \\\"STA 抑制 reward hacking\\\" claim。windowed ISR/PR: 1-50 (0.51), 51-100 (0.47), 101-200 (0.29), 201-300 (0.27), 301-400 (0.28), 401-500 (0.30) — 分离在100步后稳定。D030 决策：checkpoint 已删除，不重训。论文用训练曲线 windowed ISR/PR 数据作为证据。\"}, \"plan001-exec-only-s43-r4\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T01:40:37.808Z\", \"updated_at\": \"2026-05-14T06:30:57.539Z\", \"metrics\": {\"eval_sampling_prove_rate\": 0.14, \"eval_sampling_mean_isr\": 0, \"eval_sampling_n_proved\": 14, \"eval_sampling_temperature\": 0.7, \"eval_sampling_method\": \"do_sample=True, temperature=0.7\", \"eval_sampling_by_answer\": {\"true\": {\"count\": 34, \"proved\": 6, \"prove_rate\": 0.176}, \"false\": {\"count\": 25, \"proved\": 2, \"prove_rate\": 0.08}, \"unknown\": {\"count\": 41, \"proved\": 6, \"prove_rate\": 0.146}}}, \"conclusion\": \"negative\", \"notes\": \"训练 PR(last100)=0.883 但 eval PR=14% (sampling, T=0.7), ISR=0。87% 样本 hit max_new_tokens 生成不可解析长输出。与 s42 (eval PR=93%) 形成极端跨 seed 不稳定。exec-only reward landscape 存在极大方差。⚠️ 评估方法：sampling eval (T=0.7)，其他组用 eval_sta.py full STA。D029 决策：不重训，论文标注方法差异。PR=14% 是 failure case，eval 方法不影响结论。\"}, \"plan017-additive-random-s42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T03:11:14.694Z\", \"updated_at\": \"2026-05-14T05:33:25.603Z\", \"hypothesis\": \"Additive random control: r = r_exec·(1+0.3·random). 隔离 ISR structural signal vs variance regularization. 若 ISR > random > exec-only → signal+regularization 均贡献; 若 ISR > random ≈ exec-only → ISR signal 是关键; 若 ISR ≈ random → ISR 无结构价值。\", \"parent\": \"plan013-random-reward-s42-r4\", \"conclusion\": \"negative\", \"notes\": \"Eval结果: PR=0.48, mean_ISR=0.0453, proved_only_ISR=0.0943, mean_components=9.56 (3+比例100%, 无tautological collapse). 但33%已证明样本ISR=0 (n_necessary=0, conclusion trivially provable). 与plan013的不同failure mode: additive random防止了2-component坍缩, 但模型转向生成复杂但无用的formalization (多premises但conclusion不依赖任何premise). Variance regularization不足以产生genuine proofs.\", \"metrics\": {\"eval_prove_rate\": 0.48, \"eval_mean_isr\": 0.0453, \"eval_isr_std\": 0.0759, \"eval_median_isr\": 0, \"eval_max_isr\": 0.2857, \"eval_proved_only_isr\": 0.0943, \"eval_n_proved\": 48, \"eval_n_problems\": 100, \"eval_method\": \"eval_sta.py full STA\", \"eval_data\": \"proofwriter_fol_100.jsonl\", \"eval_component_count_mean\": 9.6, \"eval_component_count_2_ratio\": 0, \"eval_isr_pr_ratio\": 0.0943, \"eval_elapsed_s\": 542.3, \"eval_by_type_false_pr\": 0.32, \"eval_by_type_false_isr\": 0.0254, \"eval_by_type_unknown_pr\": 0.51, \"eval_by_type_unknown_isr\": 0.0518, \"eval_by_type_true_pr\": 0.56, \"eval_by_type_true_isr\": 0.052, \"tautological_collapse\": false}}, \"plan014-downstream-nli-s42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T03:43:37.925Z\", \"updated_at\": \"2026-05-14T04:29:48.645Z\", \"hypothesis\": \"Downstream NLI validation: 高ISR formalization 应在独立推理任务上表现更好(entailment accuracy)，Spearman ρ(ISR, accuracy) > 0.1 验证 ISR 作为 quality proxy 的实用价值。同时用 Z3 cross-solver agreement 验证 formalization 鲁棒性。\", \"notes\": \"Negative: ISR 作为 downstream NLI quality proxy 无效。Spearman ρ(ISR, correct)=-0.049 (p=0.187)，Best-of-N ISR 仅 +0.9pp over random (不显著)。主因：模型严重 true-bias (false accuracy=0%)，NLI accuracy 天花板仅 34.1%，ISR 无区分空间。ISR bucket 层面有弱单调趋势 (high=75% > mid=37.7% > low=32.7%) 但 high bucket 仅 12 样本。quartile 分析非单调。\", \"conclusion\": \"negative\", \"metrics\": {\"overall_accuracy\": 0.341, \"proved_rate\": 0.915, \"proved_count\": 732, \"total_generations\": 800, \"parse_errors\": 0, \"accuracy_by_label\": {\"true\": 0.912, \"false\": 0, \"unknown\": 0.076}, \"spearman_rho\": -0.049, \"spearman_p\": 0.187, \"mann_whitney_U\": 17202, \"mann_whitney_p\": 0.288, \"bon_isr_accuracy\": 0.35, \"bon_random_accuracy\": 0.341, \"bon_oracle_accuracy\": 0.44, \"bon_prove_first_accuracy\": 0.35, \"isr_bucket_high_acc\": 0.75, \"isr_bucket_mid_acc\": 0.377, \"isr_bucket_low_acc\": 0.327, \"runtime_inference_s\": 408.8, \"runtime_eval_s\": 13.6}}, \"plan002-additive-b03-s42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T02:24:47.843Z\", \"updated_at\": \"2026-05-14T04:27:38.822Z\", \"metrics\": {\"total_steps\": 500, \"duration_min\": 56.7, \"overall_prove_rate\": 0.34025, \"overall_isr\": 0.11527, \"first20_prove_rate\": 0.15625, \"last50_prove_rate\": 0.555, \"last100_prove_rate\": 0.5525, \"mean_loss\": 0.008914, \"last100_loss\": 0.014469, \"parse_rate\": 1, \"w1_50_prove_rate\": 0.13, \"w51_100_prove_rate\": 0.095, \"w101_200_prove_rate\": 0.185, \"w201_300_prove_rate\": 0.375, \"w301_400_prove_rate\": 0.47625, \"w401_500_prove_rate\": 0.5525, \"steps_ge_085\": 52, \"first_step_ge_085\": 46, \"final_prove_rate\": 1, \"final_isr_mean\": 0.3089, \"final_reward_mean\": 1.0927}, \"notes\": \"ISR 为 binary 近似 (_fast_fn)，不可用于论文跨 run 对比，需 eval_sta.py 统一评估真实 ISR。prove_rate 轨迹 0.13→0.095→0.185→0.375→0.476→0.553，呈稳步上升趋势，尚未完全饱和（仅 52/500 步 ≥0.85），与 plan001/plan013 的强饱和模式不同。\", \"conclusion\": \"negative\"}, \"plan013-random-reward-s42-r4\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T01:40:35.587Z\", \"updated_at\": \"2026-05-14T03:45:53.344Z\", \"conclusion\": \"success\", \"metrics\": {\"eval_prove_rate\": 1, \"eval_mean_isr\": 0.535, \"eval_isr_std\": 0.1282, \"eval_proved_only_isr\": 0.535, \"eval_median_isr\": 0.5, \"eval_n_proved\": 100, \"eval_n_problems\": 100, \"eval_method\": \"eval_sta.py full STA\", \"eval_data\": \"proofwriter_fol_100.jsonl\", \"eval_note\": \"DEGENERATE: model generates trivial 2-component proofs (premise=conclusion, conclusion=conclusion), ISR=0.5 is artifact of trivial proof structure\"}, \"notes\": \"⚠️ 训练日志 ISR 为 binary approximation (_fast_fn)，ISR≈prove_rate，不含结构信息。真实 ISR 需通过 eval_sta.py (full STA) 在 checkpoint-500 上重新评估。final_mean_isr=0.6705 实为 binary 近似值，禁止用于论文或跨实验 ISR 对比。\"}, \"plan001-exec-only-s43-r3\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T01:02:31.830Z\", \"updated_at\": \"2026-05-14T01:41:28.427Z\", \"conclusion\": \"failed\"}, \"plan013-random-reward-s42-r3\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T01:02:30.063Z\", \"updated_at\": \"2026-05-14T01:41:28.122Z\", \"conclusion\": \"failed\"}, \"plan001-exec-only-s43-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T00:22:12.292Z\", \"updated_at\": \"2026-05-14T01:01:56.416Z\", \"conclusion\": \"failed\"}, \"plan013-random-reward-s42-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T00:22:10.140Z\", \"updated_at\": \"2026-05-14T01:01:55.694Z\", \"conclusion\": \"failed\"}, \"plan013-random-reward-s42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T23:56:44.062Z\", \"updated_at\": \"2026-05-14T00:21:05.430Z\", \"conclusion\": \"failed\"}, \"plan001-exec-only-s43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T23:55:08.635Z\", \"updated_at\": \"2026-05-14T00:21:04.003Z\", \"conclusion\": \"failed\"}, \"plan001-exec-only-s42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T22:19:41.568Z\", \"updated_at\": \"2026-05-13T23:03:42.892Z\", \"conclusion\": \"failed\"}, \"plan003-eval-exec-only-r5\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T22:21:48.691Z\", \"updated_at\": \"2026-05-13T23:03:19.945Z\", \"metrics\": {\"prove_rate\": 0.32, \"mean_isr\": 0.2055, \"isr_std\": 0.3194, \"proved_only_isr\": 0.6423, \"isr_by_type\": {\"true\": 0.3598, \"false\": 0.1723, \"unknown\": 0.0979}, \"total_samples\": 100, \"proved_count\": 32, \"runtime_s\": 251.7}, \"conclusion\": \"success\"}, \"plan001-exec-only-s42-r3\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T22:42:40.242Z\", \"updated_at\": \"2026-05-13T23:03:11.395Z\", \"conclusion\": \"failed\"}, \"sta-phase1-exec-sta-r5\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T20:54:31.353Z\", \"updated_at\": \"2026-05-13T22:20:41.274Z\", \"metrics\": {\"parse_rate\": 1, \"prove_rate\": 0.1, \"mean_isr\": 0.04347, \"last20_prove_rate\": 0.15, \"last20_isr_mean\": 0.04956, \"first20_prove_rate\": 0.08125, \"first20_isr_mean\": 0.05182, \"overall_reward_mean\": 0.07174, \"last20_reward_mean\": 0.09978, \"training_steps\": 100, \"training_minutes\": 16.9, \"step_time_s\": 10.13, \"isr_pr_ratio_overall\": 0.43, \"isr_pr_ratio_last20\": 0.33, \"K\": 8}, \"conclusion\": \"negative\"}, \"sta-phase1-exec-only-r5\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T20:54:27.505Z\", \"updated_at\": \"2026-05-13T21:53:04.486Z\", \"metrics\": {\"parse_rate\": 1, \"prove_rate\": 0.15125, \"mean_isr\": 0.1475, \"last20_prove_rate\": 0.2, \"last20_isr_mean\": 0.2, \"first20_prove_rate\": 0.11875, \"first20_isr_mean\": 0.11875, \"overall_reward_mean\": 0.15125, \"last20_reward_mean\": 0.2, \"training_steps\": 100, \"training_minutes\": 15.7, \"step_time_s\": 9.44, \"isr_pr_ratio_last20\": 1, \"K\": 8}, \"conclusion\": \"success\"}, \"sta-phase1-exec-sta-r4\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T20:28:22.778Z\", \"updated_at\": \"2026-05-13T20:52:58.761Z\", \"metrics\": {\"parse_rate\": 1, \"prove_rate\": 0.1575, \"mean_isr\": 0.1525, \"last20_prove_rate\": 0.2125, \"last20_isr_mean\": 0.2125, \"first20_reward_mean\": 0.119, \"training_steps\": 100, \"training_minutes\": 15}, \"conclusion\": \"negative\", \"notes\": \"Phase 1 r4 完成但无差异。fast_isr_fol 二值信号(0/1)对 proved samples 几乎全部 ISR=1，exec+STA reward ≈ exec-only reward。连续 ISR 才能产生有意义的差异信号。→ r5 改用 full sta_reward (continuous ISR 0.0-1.0) + K=8\"}, \"sta-phase1-exec-only-r4\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T20:28:18.040Z\", \"updated_at\": \"2026-05-13T20:52:56.416Z\", \"metrics\": {\"parse_rate\": 1, \"prove_rate\": 0.15125, \"mean_isr\": 0.1475, \"last20_prove_rate\": 0.2, \"last20_isr_mean\": 0.2, \"first20_reward_mean\": 0.119, \"training_steps\": 100, \"training_minutes\": 15}, \"conclusion\": \"negative\", \"notes\": \"Phase 1 r4 完成但无差异。fast_isr_fol 二值信号(0/1)对 proved samples 几乎全部 ISR=1，导致 exec+STA ≈ exec-only。prove_rate 从 baseline 12% → last20 20%（微弱提升）。K=4 导致大量全零 reward batch。→ r5 改用 full STA + K=8\"}, \"sta-phase1-exec-only-r3\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T20:15:04.067Z\", \"updated_at\": \"2026-05-13T20:23:15.460Z\", \"conclusion\": \"failed\", \"notes\": \"EXIT_CODE=137 (OOM/SIGKILL) after ~276s. 同 sta-phase1-exec-sta-r3 一起诊断中\"}, \"sta-phase1-exec-sta-r3\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T20:15:08.133Z\", \"updated_at\": \"2026-05-13T20:23:14.516Z\", \"conclusion\": \"failed\", \"notes\": \"EXIT_CODE=137 (OOM/SIGKILL) after ~278s. 诊断中: worker_diagnose_sta-phase1-r3-oom_20260513T202300\"}, \"sta-phase1-exec-sta-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T19:55:08.640Z\", \"updated_at\": \"2026-05-13T19:55:41.544Z\", \"conclusion\": \"failed\"}, \"sta-phase1-exec-only-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T19:55:04.711Z\", \"updated_at\": \"2026-05-13T19:55:37.426Z\", \"conclusion\": \"failed\"}, \"sta-phase1-exec-sta\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T18:26:53.258Z\", \"updated_at\": \"2026-05-13T19:33:03.905Z\", \"conclusion\": \"failed\"}, \"sta-phase1-exec-only\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T18:26:46.351Z\", \"updated_at\": \"2026-05-13T19:33:01.169Z\", \"conclusion\": \"failed\"}, \"sta-gt-isr-baseline\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T18:11:13.283Z\", \"updated_at\": \"2026-05-13T18:12:44.147Z\", \"conclusion\": \"success\", \"metrics\": {\"gt_prove_rate\": 0.18, \"gt_mean_isr\": 0.5588, \"gt_isr_std\": 0.2582, \"gt_isr_median\": 0.6125, \"solver_execution_rate\": 1, \"true_prove_rate\": 0.5, \"true_mean_isr\": 0.5833}}, \"sta-phase0-baseline\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T17:51:48.853Z\", \"updated_at\": \"2026-05-13T18:10:40.982Z\", \"metrics\": {\"mean_isr\": 0.0641, \"isr_std\": 0.1983, \"median_isr\": 0, \"isr_range\": [0, 0.889], \"prove_rate\": 0.12, \"proved_count\": 12, \"total_samples\": 100, \"xor_affected_samples\": 34, \"effective_prove_rate_no_xor\": 0.182, \"avg_time_per_sample_s\": 3.4, \"total_runtime_s\": 336, \"isr_by_answer\": {\"true\": {\"n\": 34, \"proved\": 9, \"prove_rate\": 0.265, \"mean_isr\": 0.1345}, \"false\": {\"n\": 25, \"proved\": 1, \"prove_rate\": 0.04, \"mean_isr\": 0.024}, \"unknown\": {\"n\": 41, \"proved\": 2, \"prove_rate\": 0.049, \"mean_isr\": 0.0302}}}, \"conclusion\": \"success\"}}, \"count\": 50, \"total\": 50, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2333}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "48c103c4-8082-4370-b97f-8e4c3bab0c06",
  "isSidechain": false,
  "promptId": "c33bf5b5-c338-4f2f-97b8-e3e6d5f92819",
  "type": "user",
  "uuid": "091ce49b-b5b9-4fb4-b03b-c24ed090fb3c",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {\\\"plan006-prolog-sta-s44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-14T09:19:39.743Z\\\", \\\"updated_at\\\": \\\"2026-05-14T18:47:53.131Z\\\", \\\"hypothesis\\\": \\\"Prolog exec+STA GRPO seed=44: 第三 seed。3-seed mean±std 用于论文 Claim 3 跨 logic type 统计支撑。\\\", \\\"notes\\\": \\\"Reviewer 独立核实: query-as-fact gaming, 0% genuine. 97/97 proved 样本中 95/97 n_necessary=1（功能性 H7）。模型将 NL 问题转为 snake_case atom 同时设为 fact 和 query，Prolog trivially 证明。PR=0.97, ISR=0.885 是 gaming artifact（高 ISR 因单 clause = query）。第三种 Goodhart pathway（vs s42 clean H7, s43 degenerate syntax H1）。对照: s42=negative (clean H7=100%), s43=negative (uppercase pseudo-Prolog H1=97.4%), s44=negative (query-as-fact gaming, functional H7=95/97).\\\", \\\"metrics\\\": {\\\"pass_rate\\\": 0.97, \\\"isr_mean\\\": 0.885, \\\"isr_n_cl_ge3\\\": \\\"N/A (0 samples)\\\", \\\"n_clauses_dist\\\": \\\"78/100 single-clause, 22/100 two-clause\\\", \\\"h7_functional_rate\\\": 0.979, \\\"genuine_rate\\\": 0, \\\"premise_count_analysis\\\": \\\"100% artifact - zero samples with n_clauses>=3, model exclusively generates 1-2 clause programs\\\", \\\"failure_mode\\\": \\\"query-as-fact gaming (total H7 collapse)\\\"}, \\\"conclusion\\\": \\\"negative\\\"}, \\\"plan006-prolog-sta-s43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-14T09:19:39.141Z\\\", \\\"updated_at\\\": \\\"2026-05-14T18:20:56.947Z\\\", \\\"hypothesis\\\": \\\"Prolog exec+STA GRPO seed=43: 跨 seed 稳定性检查。与 exec-only s43 对照。\\\", \\\"notes\\\": \\\"Eval: PR=0.38, ISR=0.185 proved-only. Strict classifier: H7=0%, H1=0%, Genuine=100%. 但功能分析显示所有 38 proved 样本 n_necessary=1（功能性 H7）。模型生成大写伪 Prolog（如 MARY_IS_AN_AVADEOTE.）—— 非标准语法，strict classifier 无法匹配 conclusion。与 s42 (clean H7=100%) 不同的 Goodhart 路径，但同样是 hacking。磁盘 240G/250G 需清理。\\\", \\\"metrics\\\": {\\\"train\\\": {\\\"final_prove_rate\\\": 0.769, \\\"final_mean_isr\\\": 0.129, \\\"final_loss\\\": 0.0155, \\\"final_entropy\\\": 0.09, \\\"final_reward\\\": 0.573, \\\"completion_length_mean\\\": 143, \\\"train_runtime_seconds\\\": 5095, \\\"train_runtime_minutes\\\": 84.9}, \\\"eval\\\": {\\\"n_problems\\\": 100, \\\"n_proved\\\": 38, \\\"prove_rate\\\": 0.38, \\\"mean_isr\\\": 0.0704, \\\"isr_std\\\": 0.1263, \\\"median_isr\\\": 0, \\\"proved_only_mean_isr\\\": 0.1853, \\\"min_isr\\\": 0, \\\"max_isr\\\": 1, \\\"by_answer_type\\\": {\\\"false\\\": {\\\"count\\\": 25, \\\"proved\\\": 11, \\\"prove_rate\\\": 0.44, \\\"mean_isr\\\": 0.1003}, \\\"unknown\\\": {\\\"count\\\": 41, \\\"proved\\\": 11, \\\"prove_rate\\\": 0.268, \\\"mean_isr\\\": 0.0394}, \\\"true\\\": {\\\"count\\\": 34, \\\"proved\\\": 16, \\\"prove_rate\\\": 0.471, \\\"mean_isr\\\": 0.0859}}}, \\\"h7_classification\\\": {\\\"h7_strict\\\": 0, \\\"h7_rate\\\": 0, \\\"h1_strict\\\": 37, \\\"h1_rate\\\": 0.974, \\\"conclusion_in_premise_total\\\": 37, \\\"conclusion_in_premise_rate\\\": 0.974, \\\"genuine_count\\\": 0, \\\"genuine_rate\\\": 0, \\\"isr_1_count\\\": 1, \\\"note\\\": \\\"1 pseudo-genuine sample (folio_1415) has query embedded in single mega-clause; all 38/38 proved samples are tautological\\\"}}, \\\"conclusion\\\": \\\"negative\\\"}, \\\"plan016-extended-1000-s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-14T05:29:47.634Z\\\", \\\"updated_at\\\": \\\"2026-05-14T17:34:52.375Z\\\", \\\"hypothesis\\\": \\\"Extended training 1000 steps exec-only: plan001-s42 500步 PR=93% 是真收敛还是 lucky early convergence? 1000步观察 PR 和 ISR 在更长 horizon 的行为。s43(14%)/s44(98% tautological) 在 500 步均失败，延长训练是否能改善？\\\", \\\"parent\\\": \\\"plan001-exec-only-s42-r2\\\", \\\"metrics\\\": {\\\"prove_rate\\\": 0.96, \\\"isr\\\": 0.003, \\\"n_proved\\\": 96, \\\"components\\\": 18.55, \\\"h7_count\\\": 0, \\\"h7_rate\\\": 0, \\\"h1_count\\\": 96, \\\"h1_rate\\\": 1, \\\"genuine_count\\\": 0, \\\"genuine_rate\\\": 0}, \\\"conclusion\\\": \\\"success\\\", \\\"notes\\\": \\\"Extended training to 1000 steps CONFIRMS ISR collapse worsens monotonically.\\\\\\\\n\\\\\\\\n## 500 vs 1000 step comparison (eval_sta.py):\\\\\\\\n| Metric | plan001-s42 (500步) | plan016 (1000步) | Change |\\\\\\\\n|--------|-------------------|-----------------|--------|\\\\\\\\n| eval PR | 0.93 | 0.96 | +3.2% |\\\\\\\\n| eval ISR | 0.123 | 0.0027 | -97.8% |\\\\\\\\n| proved_only ISR | 0.132 | 0.0028 | -97.9% |\\\\\\\\n| components | 6.58 | 18.55 | +182% |\\\\\\\\n| ISR=0 ratio | - | 94.8% | - |\\\\\\\\n| n_necessary=0 ratio | - | 94.8% | - |\\\\\\\\n\\\\\\\\n## Key findings:\\\\\\\\n1. PR improves (+3%) but ISR collapses near-zero (0.0027). The model gets BETTER at proving while becoming WORSE at faithful reasoning.\\\\\\\\n2. Component count nearly tripled (6.58→18.55). Model generates longer proofs with more components, but 94.8% have ZERO necessary components.\\\\\\\\n3. NOT tautological collapse (comp=2 ratio=0). Instead: contradiction-based collapse — model embeds P(a) and ¬P(a) among many irrelevant premises, making anything provable via explosion.\\\\\\\\n4. Windowed ISR trend is monotonically decreasing: 0.1115 (101-200) → 0.0433 (401-500) → 0.0200 (601-700) → 0.0144 (901-1000). No recovery signal.\\\\\\\\n5. The exec-only reward creates a pure reward hacking incentive: the model discovers that contradictions + trivially true conclusions always satisfy the prover.\\\\\\\\n\\\\\\\\n## Implication for paper:\\\\\\\\nExtended training is a clean ablation showing exec-only reward's failure mode worsens over time. The 500-step ISR of 0.123 was not a floor — it was a snapshot of ongoing collapse.\\\"}, \\\"plan002-additive-b01-s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-14T05:29:08.138Z\\\", \\\"updated_at\\\": \\\"2026-05-14T17:33:21.938Z\\\", \\\"parent\\\": \\\"plan002-additive-b03-s42\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"eval_prove_rate\\\": 0.81, \\\"eval_mean_isr\\\": 0.3365, \\\"eval_isr_std\\\": 0.3227, \\\"eval_proved_only_isr\\\": 0.4154, \\\"eval_median_isr\\\": 0.2, \\\"eval_n_proved\\\": 81, \\\"eval_n_problems\\\": 100, \\\"eval_method\\\": \\\"eval_sta.py full STA\\\", \\\"eval_data\\\": \\\"proofwriter_fol_100.jsonl\\\", \\\"eval_component_count_mean\\\": 5.58, \\\"h7_rate\\\": 0.16, \\\"h7_count\\\": 13, \\\"h1_rate\\\": 0.519, \\\"h1_count\\\": 42, \\\"genuine_rate\\\": 0.309, \\\"genuine_count\\\": 25, \\\"tautological_collapse\\\": false}, \\\"notes\\\": \\\"H7 audit (2026-05-14): 81 proved samples. H7 (single premise=conclusion): 13/81=16.0%, mean ISR=0.6603. H1 (multi premise contains conclusion): 42/81=51.9%, mean ISR=0.2245. Genuine (no conclusion duplication): 26/81=32.1%, mean ISR=0.6014. Combined conclusion duplication = 67.9%. CRITICAL: only 32.1% of proved samples are free of conclusion embedding. H7 inflates ISR; H1 deflates ISR but proof is trivially achievable via embedded conclusion. Claim 2 \\\\\\\"genuine structural guidance\\\\\\\" needs reframing — ISR signal is dominated by conclusion duplication artifacts.\\\"}, \\\"plan018-additive-random-b01-s43-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-14T14:01:24.111Z\\\", \\\"updated_at\\\": \\\"2026-05-14T17:17:02.398Z\\\", \\\"hypothesis\\\": \\\"Random β=0.1 seed=43 控制组 r2: 重试 (原 s43 step 200 磁盘满崩溃)。与 plan002-b01-s43 (ISR β=0.1) 同 seed 对照。3-seed mean±std 审稿硬性要求。\\\", \\\"parent\\\": \\\"plan018-additive-random-b01-s43\\\", \\\"metrics\\\": {\\\"h7_rate\\\": 0, \\\"h7_count\\\": 0, \\\"h1_rate\\\": 93.2, \\\"h1_count\\\": 82, \\\"genuine_rate\\\": 6.8, \\\"genuine_count\\\": 6}, \\\"conclusion\\\": \\\"negative\\\"}, \\\"plan006-prolog-sta-s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-14T09:19:38.117Z\\\", \\\"updated_at\\\": \\\"2026-05-14T16:49:42.052Z\\\", \\\"hypothesis\\\": \\\"Prolog exec+STA GRPO seed=42: ISR reward 在 Prolog logic type 上的效果。与 plan006-prolog-exec-s42 (exec-only) 对照，验证 STA/ISR 的 hacking 检测和 Goodhart 效应是否跨 logic type 泛化。\\\", \\\"notes\\\": \\\"Eval metrics provenance: eval 在训练完成后立即在 westd-39279 服务器上运行 eval_sta.py，checkpoint 路径 /root/autodl-tmp/outputs/plan006_prolog_sta_s42/。Eval 结果由 Worker 从服务器 SSH 读取 eval_results.json 并手动录入 registry。Checkpoint 可能已被磁盘清理删除（C003 save_total_limit=1）。训练日志: ~/runs/solver-trace-ablation/plan006-prolog-sta-s42.log。H7 分类由 classify_h7.py 在 eval 目录上运行。\\\", \\\"conclusion\\\": \\\"negative\\\", \\\"metrics\\\": {\\\"cumulative_prove_rate\\\": 0.848, \\\"cumulative_mean_isr\\\": 0.787, \\\"final_prove_rate\\\": 1, \\\"final_isr\\\": 1, \\\"final_reward\\\": 1, \\\"saturation_onset_step\\\": 100, \\\"train_loss\\\": 0.00716, \\\"training_hours\\\": 0.78, \\\"final_entropy\\\": 0.01, \\\"final_completion_length\\\": 27, \\\"initial_completion_length\\\": 120, \\\"steps_at_perfect_reward\\\": 400, \\\"train_runtime_sec\\\": 2791, \\\"eval_prove_rate\\\": 0.5, \\\"eval_mean_isr\\\": 0.5, \\\"eval_proved_only_isr\\\": 1, \\\"eval_h7_rate\\\": 1, \\\"eval_h7_count\\\": 50, \\\"eval_proved_count\\\": 50, \\\"eval_total_count\\\": 100, \\\"eval_n_clauses_mean\\\": 1, \\\"eval_isr_distribution\\\": \\\"binary: 50x0 + 50x1\\\"}}, \\\"plan001-exec-only-s44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-14T03:57:09.690Z\\\", \\\"updated_at\\\": \\\"2026-05-14T16:29:02.086Z\\\", \\\"hypothesis\\\": \\\"Exec-only seed=44 第3 seed: 解决 s42(93% eval PR) vs s43(13% eval PR) 的跨 seed 不稳定问题，3-seed mean±std 是论文必需。\\\", \\\"metrics\\\": {\\\"eval_prove_rate\\\": 0.98, \\\"eval_mean_isr\\\": 0.57, \\\"eval_isr_std\\\": 0.2013, \\\"eval_median_isr\\\": 0.5, \\\"eval_proved_only_isr\\\": 0.5816, \\\"eval_n_proved\\\": 98, \\\"eval_n_problems\\\": 100, \\\"eval_method\\\": \\\"eval_sta.py full STA\\\", \\\"eval_data\\\": \\\"proofwriter_fol_100.jsonl\\\", \\\"eval_component_count_mean\\\": 2.04, \\\"eval_component_count_2\\\": 94, \\\"eval_component_count_3\\\": 4, \\\"tautological_collapse\\\": true, \\\"h7_rate\\\": 1, \\\"h7_count\\\": 97, \\\"h1_rate\\\": 0, \\\"h1_count\\\": 0, \\\"genuine_rate\\\": 0, \\\"genuine_count\\\": 0, \\\"conclusion_embedding_total\\\": 1}, \\\"conclusion\\\": \\\"negative\\\", \\\"notes\\\": \\\"TAUTOLOGICAL COLLAPSE 确认。eval PR=98% 但 94% 样本仅 2 components (premise=conclusion tautology)，mean components=2.04，与 plan013 random reward 完全一致。ISR≈0.5 是 2-component artifact。s42 是唯一产生 genuine proofs (mean components=6.58) 的 seed。3-seed 结果：s42=genuine, s43=degraded(PR=13%), s44=tautological(PR=98% fake)。Exec-only reward 2/3 seeds 失败。\\\"}, \\\"plan001-exec-only-s42-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-13T22:40:41.773Z\\\", \\\"updated_at\\\": \\\"2026-05-14T16:28:58.538Z\\\", \\\"notes\\\": \\\"Cron 误判 DONE/failed（因 --help|grep 前缀命令的 PID 84896 退出，实际训练子进程 PID 84901 仍在运行）。已手动恢复 RUNNING。严禁在 cuda:0 启动新进程直到 r2 自然完成。⚠️ Reviewer 中期审查标注: 训练日志中 ISR=0.8612 为 binary approximation (_fast_fn)，非真实 ISR。最终可比 ISR 需通过 eval_sta.py (full STA) 重新评估。\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"eval_prove_rate\\\": 0.93, \\\"eval_mean_isr\\\": 0.1232, \\\"eval_isr_std\\\": 0.1887, \\\"eval_proved_only_isr\\\": 0.1324, \\\"eval_median_isr\\\": 0, \\\"eval_n_proved\\\": 93, \\\"eval_n_problems\\\": 100, \\\"eval_method\\\": \\\"eval_sta.py full STA\\\", \\\"eval_data\\\": \\\"proofwriter_fol_100.jsonl\\\", \\\"h7_rate\\\": 0, \\\"h7_count\\\": 0, \\\"h1_rate\\\": 0.871, \\\"h1_count\\\": 81, \\\"genuine_rate\\\": 0.129, \\\"genuine_count\\\": 12, \\\"genuine_mean_isr\\\": 0.3141, \\\"h1_mean_isr\\\": 0.1055, \\\"conclusion_embedding_total\\\": 0.871}}, \\\"plan006-prolog-exec-s44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-14T07:13:35.647Z\\\", \\\"updated_at\\\": \\\"2026-05-14T16:27:18.570Z\\\", \\\"hypothesis\\\": \\\"Prolog exec-only GRPO seed=44: third seed for Prolog exec-only. Together with s42 (PR=83%, ISR=0.031) and s43, provides 3-seed evidence for cross-logic generalization claim (Claim 3). 3-seed mean±std required for paper.\\\", \\\"notes\\\": \\\"Eval 完成。PR=21% (3-seed 最低), ISR=0.081, proved_only_ISR=0.387 (max_ISR=1.0)。与 s42/s43 不同模式：PR 极低但 proved_only_ISR 较高，可能有少量样本 ISR=1 (H7-like)。Prolog exec-only 3-seed 汇总：s42 PR=83%/ISR=0.031, s43 PR=56%/ISR=0.008, s44 PR=21%/ISR=0.081。Mean PR=53.3%±31.1%, Mean ISR=0.040±0.037。跨 seed 极不稳定（PR std=31pp），与 FOL exec-only 一致。ISR 始终极低（<0.1），确认 Prolog exec-only 不产生 genuine reasoning traces。\\\", \\\"metrics\\\": {\\\"eval_prove_rate\\\": 0.21, \\\"eval_mean_isr\\\": 0.0812, \\\"eval_isr_std\\\": 0.2343, \\\"eval_median_isr\\\": 0, \\\"eval_proved_only_isr\\\": 0.3866, \\\"eval_min_isr\\\": 0, \\\"eval_max_isr\\\": 1, \\\"eval_n_proved\\\": 21, \\\"eval_n_problems\\\": 100, \\\"eval_method\\\": \\\"eval_sta.py full STA\\\", \\\"eval_data\\\": \\\"proofwriter_fol_100.jsonl\\\", \\\"eval_elapsed_seconds\\\": 683.9, \\\"eval_by_type_false_pr\\\": 0.04, \\\"eval_by_type_false_isr\\\": 0.04, \\\"eval_by_type_unknown_pr\\\": 0.317, \\\"eval_by_type_unknown_isr\\\": 0.099, \\\"eval_by_type_true_pr\\\": 0.206, \\\"eval_by_type_true_isr\\\": 0.09, \\\"solver\\\": \\\"PrologSolver\\\", \\\"logic_type\\\": \\\"prolog\\\"}, \\\"conclusion\\\": \\\"negative\\\"}, \\\"plan009-sft-baseline-s42-r4\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-14T11:40:28.142Z\\\", \\\"updated_at\\\": \\\"2026-05-14T16:27:01.864Z\\\", \\\"hypothesis\\\": \\\"SFT baseline: supervised finetuning on FOLIO data (500 steps, Qwen3-4B, same model as all GRPO experiments) to establish whether hacking patterns are GRPO-specific or general finetuning artifacts. r4: fix CUDA_VISIBLE_DEVICES + --gpu + --no_wandb.\\\", \\\"parent\\\": \\\"plan009-sft-baseline-s42-r2\\\", \\\"notes\\\": \\\"r4 训练完成 (500 steps, TRL SFT). Checkpoint 实际保存在 plan009_sft_baseline_s42（非 plan009_sft_s42_r4）。两卡满载 (cuda:0 80GB, cuda:1 80GB)，eval 待 GPU 释放。checkpoint-500/ 含 15GB optimizer.pt 可在 eval 后清理。\\\", \\\"metrics\\\": {\\\"eval_prove_rate\\\": 0.14, \\\"eval_mean_isr\\\": 0.08, \\\"eval_isr_std\\\": 0.214, \\\"eval_median_isr\\\": 0, \\\"eval_max_isr\\\": 0.833, \\\"eval_proved_only_isr\\\": 0.571, \\\"eval_n_proved\\\": 14, \\\"eval_n_problems\\\": 100, \\\"eval_method\\\": \\\"eval_sta.py full STA\\\", \\\"eval_data\\\": \\\"proofwriter_fol_100.jsonl\\\", \\\"train_final_loss\\\": 0.0287, \\\"train_token_accuracy\\\": 0.9935, \\\"train_epochs\\\": 7.94, \\\"train_runtime_sec\\\": 789.6, \\\"by_answer_type\\\": {\\\"true\\\": {\\\"count\\\": 34, \\\"proved\\\": 13, \\\"pr\\\": 0.382, \\\"isr\\\": 0.226}, \\\"unknown\\\": {\\\"count\\\": 41, \\\"proved\\\": 1, \\\"pr\\\": 0.024, \\\"isr\\\": 0.008}, \\\"false\\\": {\\\"count\\\": 25, \\\"proved\\\": 0, \\\"pr\\\": 0, \\\"isr\\\": 0}}, \\\"h7_rate\\\": 0, \\\"h7_count\\\": 0, \\\"h1_rate\\\": 0.071, \\\"h1_count\\\": 1, \\\"genuine_rate\\\": 0.929, \\\"genuine_count\\\": 13, \\\"hacking_patterns\\\": \\\"near-zero (1/14 H1, 0 H7, 92.9% genuine)\\\", \\\"tautological_collapse\\\": false}, \\\"conclusion\\\": \\\"success\\\"}, \\\"plan006-prolog-exec-s43-r3\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-14T12:38:23.818Z\\\", \\\"updated_at\\\": \\\"2026-05-14T16:16:56.523Z\\\", \\\"hypothesis\\\": \\\"Prolog exec-only GRPO seed=43 r3: warmup_ratio=0.0 与 s42 一致。r2 因残留进程 OOM 失败，cuda:1 已清理。\\\", \\\"notes\\\": \\\"Eval 完成。PR=56% (远低于 s42 的 83%), ISR=0.0084 (与 s42 的 0.031 同量级，均极低)。proved_only_ISR=0.015。Prolog exec-only 跨 seed 表现：s42 PR=83%/ISR=0.031, s43 PR=56%/ISR=0.008。s43 prove_rate 显著下降但 ISR 模式一致（极低，ground fact enumeration hacking）。与 FOL exec-only 类似，存在跨 seed 不稳定性（FOL: s42=93%, s43=14%, s44=98%）。等 s44 eval 完成后计算 3-seed mean±std。\\\", \\\"metrics\\\": {\\\"eval_prove_rate\\\": 0.56, \\\"eval_mean_isr\\\": 0.0084, \\\"eval_isr_std\\\": 0.0221, \\\"eval_median_isr\\\": 0, \\\"eval_proved_only_isr\\\": 0.015, \\\"eval_min_isr\\\": 0, \\\"eval_max_isr\\\": 0.1, \\\"eval_n_proved\\\": 56, \\\"eval_n_problems\\\": 100, \\\"eval_method\\\": \\\"eval_sta.py full STA\\\", \\\"eval_data\\\": \\\"proofwriter_fol_100.jsonl\\\", \\\"eval_elapsed_seconds\\\": 868.2, \\\"eval_by_type_false_pr\\\": 0.48, \\\"eval_by_type_false_isr\\\": 0.0043, \\\"eval_by_type_unknown_pr\\\": 0.6585, \\\"eval_by_type_unknown_isr\\\": 0.0114, \\\"eval_by_type_true_pr\\\": 0.5, \\\"eval_by_type_true_isr\\\": 0.0078, \\\"solver\\\": \\\"PrologSolver\\\", \\\"logic_type\\\": \\\"prolog\\\"}, \\\"conclusion\\\": \\\"negative\\\"}, \\\"plan018-additive-random-b01-s44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-14T08:36:18.722Z\\\", \\\"updated_at\\\": \\\"2026-05-14T15:00:09.178Z\\\", \\\"hypothesis\\\": \\\"Random β=0.1 seed=44 控制组：与 plan002-b01-s44 (ISR β=0.1) 同 seed 对照。验证 ISR 3.2x > random 的结论在 s44 下是否成立。\\\", \\\"parent\\\": \\\"plan018-additive-random-b01-s42\\\", \\\"metrics\\\": {\\\"prove_rate\\\": 0.89, \\\"mean_isr\\\": 0.0619, \\\"isr_std\\\": 0.1756, \\\"median_isr\\\": 0, \\\"proved_only_mean_isr\\\": 0.0695, \\\"n_proved\\\": 89, \\\"n_problems\\\": 100, \\\"max_isr\\\": 1, \\\"min_isr\\\": 0, \\\"isr_pr_ratio\\\": 0.0695, \\\"isr_zero_count\\\": 72, \\\"isr_one_count\\\": 2, \\\"by_answer_type\\\": {\\\"false\\\": {\\\"count\\\": 25, \\\"proved\\\": 21, \\\"prove_rate\\\": 0.84, \\\"mean_isr\\\": 0.0533}, \\\"unknown\\\": {\\\"count\\\": 41, \\\"proved\\\": 40, \\\"prove_rate\\\": 0.976, \\\"mean_isr\\\": 0.0892}, \\\"true\\\": {\\\"count\\\": 34, \\\"proved\\\": 28, \\\"prove_rate\\\": 0.824, \\\"mean_isr\\\": 0.0353}}, \\\"elapsed_seconds\\\": 1012.7, \\\"eval_method\\\": \\\"eval_sta.py with Prover9Solver, FOL\\\"}, \\\"conclusion\\\": \\\"success\\\", \\\"notes\\\": \\\"DONE (success). Random β=0.1 s44 对照分析完成: PR=0.89/ISR=0.062 (clean) vs ISR β=0.1 s44 PR=0.89/ISR=0.803 (H7=86.5% inflated). 同 PR 下 ISR reward 导致 conclusion duplication，random 无此问题。与 s42 结论一致: ISR s42 genuine ISR=0.337 vs Random s42 ISR=0.104 (3.2x)。Random 2/3 seeds done, 等 s43 (plan018-random-b01-s43-r2 QUEUED)。\\\"}, \\\"plan009-sft-baseline-s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-14T10:51:58.328Z\\\", \\\"updated_at\\\": \\\"2026-05-14T14:20:43.363Z\\\", \\\"hypothesis\\\": \\\"SFT baseline: supervised finetuning on FOLIO data (500 steps, Qwen3-4B) to establish whether hacking patterns are GRPO-specific or general finetuning artifacts. Same model as all GRPO experiments for fair comparison.\\\", \\\"conclusion\\\": \\\"killed\\\", \\\"notes\\\": \\\"模型必须改为 Qwen3-4B（与 GRPO 实验一致）。用 Qwen2.5-1.5B 无法作为 fair baseline——模型不同无法隔离训练方法差异。修正模型后重新注册提交。\\\"}, \\\"plan006-prolog-exec-s43-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-14T12:32:37.140Z\\\", \\\"updated_at\\\": \\\"2026-05-14T13:43:01.701Z\\\", \\\"hypothesis\\\": \\\"Prolog exec-only GRPO seed=43 r2: 修正 warmup_ratio=0.0 与 s42 一致。cross-seed stability check for Prolog logic type.\\\", \\\"parent\\\": \\\"plan006-prolog-exec-s43\\\", \\\"conclusion\\\": \\\"failed\\\", \\\"notes\\\": \\\"OOM 诊断：非 batch size 问题。根因是 kill_job 只杀了 tmux 包装进程 (PID 587155)，训练子进程 587159/587160 残留在 cuda:1 上占 78.09 GiB 显存。s43-r2 启动时 cuda:1 仅剩 40 MiB free，首次前向传播即 OOM (尝试分配 48 MiB)。教训：kill_job 后必须 SSH 确认子进程也已终止（ps aux grep + nvidia-smi），不能只看 PID 返回成功。\\\"}, \\\"plan006-prolog-exec-s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-14T07:13:34.169Z\\\", \\\"updated_at\\\": \\\"2026-05-14T12:33:17.845Z\\\", \\\"hypothesis\\\": \\\"Prolog exec-only GRPO seed=42: STA/ISR hacking patterns generalize across logic types? Prolog uses rule ablation (vs FOL axiom ablation). If same degeneration modes appear → STA is logic-agnostic diagnostic.\\\", \\\"notes\\\": \\\"Eval (eval_sta.py) 完成。PR=83%, mean_ISR=0.031, proved_only_ISR=0.037, H7=0%, H1=0%。与 sta-s42 (PR=50%, ISR=1.0, H7=100%) 形成鲜明对比。exec-only 产生完全不同的 hacking 模式：ground fact enumeration（倾泻大量无关 ground facts，query 作为其中一个 fact 平凡成功），而非 sta-s42 的 tautological collapse。两种 reward signal 驱动两种不同的 hacking 策略。对论文是 positive finding：强化 Claim 1 且揭示 reward-specific hacking 机制。\\\", \\\"metrics\\\": {\\\"eval_prove_rate\\\": 0.83, \\\"eval_mean_isr\\\": 0.031, \\\"eval_proved_only_isr\\\": 0.037, \\\"eval_median_isr\\\": 0, \\\"eval_max_isr\\\": 0.2, \\\"eval_isr_std\\\": 0.0534, \\\"h7_rate\\\": 0, \\\"h1_rate\\\": 0, \\\"isr_1_rate\\\": 0, \\\"single_premise_rate\\\": 0, \\\"by_answer_type\\\": {\\\"true\\\": {\\\"proved\\\": 37, \\\"count\\\": 40, \\\"pr\\\": 0.925, \\\"isr\\\": 0.037}, \\\"false\\\": {\\\"proved\\\": 21, \\\"count\\\": 29, \\\"pr\\\": 0.724, \\\"isr\\\": 0.038}, \\\"unknown\\\": {\\\"proved\\\": 25, \\\"count\\\": 31, \\\"pr\\\": 0.806, \\\"isr\\\": 0.016}}}, \\\"conclusion\\\": \\\"negative\\\"}, \\\"plan006-prolog-exec-s43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-14T07:13:35.078Z\\\", \\\"updated_at\\\": \\\"2026-05-14T12:32:13.799Z\\\", \\\"hypothesis\\\": \\\"Prolog exec-only GRPO seed=43: cross-seed stability check for Prolog logic type. FOL showed extreme cross-seed variance (s42 genuine vs s43 degraded vs s44 tautological). Prolog exec-only s42 showed PR=83%, ISR=0.031. s43 tests if Prolog also has seed instability.\\\", \\\"notes\\\": \\\"KILLED at step 36/500: warmup_ratio=0.1 与 s42 (0.0) 不一致，3-seed 对比无效。重启为 plan006-prolog-exec-s43-r2 (warmup_ratio=0.0)。\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"plan009-sft-baseline-s42-r3\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-14T11:37:49.306Z\\\", \\\"updated_at\\\": \\\"2026-05-14T11:48:05.087Z\\\", \\\"hypothesis\\\": \\\"SFT baseline: supervised finetuning on FOLIO data (500 steps, Qwen3-4B, same model as all GRPO experiments) to establish whether hacking patterns are GRPO-specific or general finetuning artifacts. Compare eval PR/ISR/hacking taxonomy against GRPO exec-only and exec+ISR conditions.\\\", \\\"parent\\\": \\\"plan009-sft-baseline-s42-r2\\\", \\\"wandb_run_id\\\": \\\"plan009-sft-s42-r3\\\", \\\"conclusion\\\": \\\"failed\\\", \\\"notes\\\": \\\"r3 crash root cause: wandb.init() failed because no W&B API key configured on server (no .netrc, no WANDB_API_KEY). Fix: add --no_wandb flag. Secondary issue: both GPUs currently near-full, need to wait for GPU availability before r4. Correct r4 command: export CUDA_VISIBLE_DEVICES=N && ... python3 scripts/train_sft.py --model_path /root/autodl-tmp/models/Qwen3-4B --data_path data/train_500_seed42.jsonl --output_dir /root/autodl-tmp/outputs/plan009_sft_s42_r4 --num_steps 500 --seed 42 --no_wandb\\\"}, \\\"plan009-sft-baseline-s42-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-14T11:02:25.369Z\\\", \\\"updated_at\\\": \\\"2026-05-14T11:43:20.347Z\\\", \\\"hypothesis\\\": \\\"SFT baseline: supervised finetuning on FOLIO data (500 steps, Qwen3-4B, same model as all GRPO experiments) to establish whether hacking patterns are GRPO-specific or general finetuning artifacts. Compare eval PR/ISR/hacking taxonomy against GRPO exec-only and exec+ISR conditions.\\\", \\\"notes\\\": \\\"SFT baseline with Qwen3-4B (same model as GRPO experiments). Replaces killed plan009-sft-baseline-s42 which incorrectly used Qwen2.5-1.5B. cuda:1, seed=42, 500 steps, FOLIO data (data/train_500_seed42.jsonl). Dream 审稿三档均指出缺 SFT baseline 是 gap。**FAILED**: 两个问题：(1) W&B API key 未配置，trainer.train() 启动时 wandb callback 报 UsageError; (2) device_map='auto' 把模型分到多 GPU，需改为单卡绑定。修复方案：加 WANDB_MODE=disabled + 改 train_sft.py 的 device_map 为单卡。\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"plan018-additive-random-b01-s43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-14T08:36:18.260Z\\\", \\\"updated_at\\\": \\\"2026-05-14T11:42:09.950Z\\\", \\\"hypothesis\\\": \\\"Random β=0.1 seed=43 控制组：与 plan002-b01-s43 (ISR β=0.1) 同 seed 对照。验证 ISR 3.2x > random 的结论在 s43 下是否成立。\\\", \\\"parent\\\": \\\"plan018-additive-random-b01-s42\\\", \\\"conclusion\\\": \\\"failed\\\", \\\"notes\\\": \\\"Disk full (os error 28) at step 200/500 during checkpoint save. Training ran fine for 200 steps but safetensors serialization failed with \\\\\\\"No space left on device\\\\\\\". No checkpoint saved. Disk now has 109G free. Retryable as-is.\\\"}, \\\"plan002-additive-b01-s44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-14T08:36:17.298Z\\\", \\\"updated_at\\\": \\\"2026-05-14T10:12:40.545Z\\\", \\\"hypothesis\\\": \\\"ISR β=0.1 seed=44 多 seed 验证：exec-only s44 是 tautological collapse (PR=98%, ISR=0.57 fake)，ISR β=0.1 能否防止 tautological collapse？3-seed mean±std 用于论文 Claim 2。\\\", \\\"parent\\\": \\\"plan002-additive-b01-s42\\\", \\\"metrics\\\": {\\\"eval_prove_rate\\\": 0.89, \\\"eval_mean_isr\\\": 0.803, \\\"eval_isr_std\\\": 0.3418, \\\"eval_median_isr\\\": 1, \\\"component_count_mean\\\": 4.33, \\\"component_count_2_ratio\\\": 0.022, \\\"tautological_collapse\\\": false, \\\"isr_0_ratio\\\": 0.12, \\\"isr_1_ratio\\\": 0.73, \\\"proved_single_premise_ratio\\\": 1, \\\"h7_rate_calibrated\\\": 0.865, \\\"h7_definition\\\": \\\"single_premise AND premise==conclusion (normalized)\\\", \\\"hacking_mode\\\": \\\"conclusion_duplication_isr_inflation\\\", \\\"conclusion_embedding\\\": true, \\\"component_dist\\\": {\\\"2\\\": 2, \\\"4\\\": 54, \\\"5\\\": 33}, \\\"by_answer_type\\\": {\\\"false\\\": {\\\"n\\\": 25, \\\"proved\\\": 22, \\\"PR\\\": 0.88, \\\"ISR\\\": 0.824}, \\\"unknown\\\": {\\\"n\\\": 41, \\\"proved\\\": 38, \\\"PR\\\": 0.927, \\\"ISR\\\": 0.837}, \\\"true\\\": {\\\"n\\\": 34, \\\"proved\\\": 29, \\\"PR\\\": 0.853, \\\"ISR\\\": 0.747}}}, \\\"conclusion\\\": \\\"negative\\\", \\\"notes\\\": \\\"RECLASSIFIED negative (D039): Reviewer 逐样本审查发现 semantic drift hacking — 模型生成极简形式化（单 premise≈conclusion），通过 conclusion sub-component ablation 膨胀 ISR。ISR=0.902 是 conclusion_duplication_isr_inflation artifact，非真正证明质量。65% 样本 ISR=1.0 为 conclusion embedding。此 hacking mode 本身是论文 positive finding（强化 Claim 1 Goodhart 叙事：ISR reward 导致新型 hacking）。原始 eval 指标：PR=0.89, mean_isr=0.803, component_mean=4.33, comp_2_ratio=0.022。exec-only s44 是 tautological collapse (94% 2-comp)，ISR β=0.1 s44 避免了 tautological collapse 但转向了 conclusion duplication hacking。\\\"}, \\\"plan002-additive-b01-s43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-14T08:36:16.367Z\\\", \\\"updated_at\\\": \\\"2026-05-14T10:12:36.502Z\\\", \\\"hypothesis\\\": \\\"ISR β=0.1 seed=43 多 seed 验证：plan002-b01-s42 (PR=0.81, ISR=0.337) 在 s43 下是否可复现？exec-only s43 是 degraded seed (PR=14%)，ISR β=0.1 能否拯救 bad seed？3-seed mean±std 用于论文 Claim 2 统计支撑。\\\", \\\"parent\\\": \\\"plan002-additive-b01-s42\\\", \\\"metrics\\\": {\\\"eval_prove_rate\\\": 0.61, \\\"eval_mean_isr\\\": 0.5063, \\\"eval_isr_std\\\": 0.4518, \\\"eval_median_isr\\\": 0.5, \\\"eval_proved_only_isr\\\": 0.8301, \\\"component_count_mean\\\": 4.03, \\\"component_count_2_ratio\\\": 0, \\\"tautological_collapse\\\": false, \\\"isr_0_ratio\\\": 0.39, \\\"isr_1_ratio\\\": 0.656, \\\"proved_single_premise_ratio\\\": 1, \\\"h7_rate_calibrated\\\": 0.967, \\\"h7_definition\\\": \\\"single_premise AND premise==conclusion (normalized)\\\", \\\"hacking_mode\\\": \\\"conclusion_duplication_isr_inflation\\\", \\\"conclusion_embedding\\\": true, \\\"by_answer_type\\\": {\\\"false\\\": {\\\"n\\\": 25, \\\"proved\\\": 18, \\\"PR\\\": 0.72, \\\"ISR\\\": 0.6}, \\\"unknown\\\": {\\\"n\\\": 41, \\\"proved\\\": 22, \\\"PR\\\": 0.537, \\\"ISR\\\": 0.442}, \\\"true\\\": {\\\"n\\\": 34, \\\"proved\\\": 21, \\\"PR\\\": 0.618, \\\"ISR\\\": 0.515}}, \\\"train_total_steps\\\": 500, \\\"train_duration_min\\\": 53, \\\"train_loss\\\": 0.012}, \\\"conclusion\\\": \\\"negative\\\", \\\"notes\\\": \\\"NEGATIVE: conclusion duplication hacking 确认。100% proved 样本仅 1 premise，97% premise=conclusion（重言式 P→P）。ISR=0.506 是 artifact（唯一 premise 必然 necessary）。与 s44 相同失败模式。3-seed 中 s42 唯一可能 genuine（待验证），s43/s44 均 collapse。β=0.1 additive bonus 多 seed 可靠性不足。\\\"}, \\\"plan012-hacking-taxonomy\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-14T09:06:38.613Z\\\", \\\"updated_at\\\": \\\"2026-05-14T09:07:42.314Z\\\", \\\"conclusion\\\": \\\"success\\\", \\\"hypothesis\\\": \\\"ISR β=0.1 vs Random β=0.1 hacking taxonomy 对比：ISR reward 能否减少 hacking 模式比例、增加 genuine proof 比例？5 种 hacking 分类（conclusion embedding, repetition collapse, tautological collapse, complexity-without-utility, premise padding）。\\\", \\\"metrics\\\": {\\\"isr_b01_genuine_rate\\\": 0.259, \\\"random_b01_genuine_rate\\\": 0.177, \\\"genuine_rate_delta_pp\\\": 8.2, \\\"isr_b01_conclusion_embedding_rate\\\": 0.728, \\\"random_b01_conclusion_embedding_rate\\\": 0.785, \\\"isr_b01_genuine_mean_isr\\\": 0.6723, \\\"random_b01_genuine_mean_isr\\\": 0.3427, \\\"isr_b01_complexity_wo_utility_rate\\\": 0, \\\"random_b01_complexity_wo_utility_rate\\\": 0.038, \\\"isr_b01_hacking_rate\\\": 0.741, \\\"random_b01_hacking_rate\\\": 0.823}, \\\"notes\\\": \\\"D037/D038 完成。Conclusion embedding 是主导 hacking 模式（ISR 72.8% vs Random 78.5%）。ISR β=0.1 genuine proof +8.2pp (25.9% vs 17.7%)，genuine ISR 质量 0.67 vs 0.34。ISR 消除 complexity-without-utility hacking。LLM-as-judge 跳过（D038），记入 Discussion/Future Work。Artifact: art_20260514_bf31aa。\\\"}, \\\"plan018-additive-random-b01-s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-14T06:55:48.888Z\\\", \\\"updated_at\\\": \\\"2026-05-14T08:32:44.808Z\\\", \\\"hypothesis\\\": \\\"β=0.1 random control: r = r_exec·(1+0.1·random[0,1]). 与 plan002-b01 (additive ISR β=0.1, PR=0.81, ISR=0.337) 同 β 对照。如果 ISR β=0.1 >> random β=0.1 → ISR 信号在低剂量下有结构价值; 如果 ISR ≈ random → ISR 信号在低剂量下也仅是 variance regularization。D031 紧急实验。\\\", \\\"parent\\\": \\\"plan002-additive-b01-s42\\\", \\\"conclusion\\\": \\\"negative\\\", \\\"metrics\\\": {\\\"eval_prove_rate\\\": 0.79, \\\"eval_mean_isr\\\": 0.1038, \\\"eval_isr_std\\\": 0.1369, \\\"eval_median_isr\\\": 0.0357, \\\"eval_proved_only_isr\\\": 0.1314, \\\"eval_n_proved\\\": 79, \\\"eval_n_problems\\\": 100, \\\"eval_component_count_mean\\\": 8.46, \\\"eval_component_count_median\\\": 8, \\\"eval_component_count_2_ratio\\\": 0, \\\"eval_isr_1_ratio\\\": 0, \\\"eval_isr_0_ratio\\\": 0.367, \\\"eval_isr_gt0_ratio\\\": 0.633, \\\"eval_by_type_false_pr\\\": 0.8, \\\"eval_by_type_false_isr\\\": 0.1318, \\\"eval_by_type_unknown_pr\\\": 0.7317, \\\"eval_by_type_unknown_isr\\\": 0.0944, \\\"eval_by_type_true_pr\\\": 0.8529, \\\"eval_by_type_true_isr\\\": 0.0945, \\\"tautological_collapse\\\": false, \\\"train_total_steps\\\": 500, \\\"train_duration_min\\\": 70.5, \\\"train_last100_pr\\\": 0.805, \\\"train_last100_isr\\\": 0.1432, \\\"train_loss\\\": 0.005}, \\\"notes\\\": \\\"Random control β=0.1 vs ISR β=0.1 (plan002-b01) 对照。conclusion=negative: random control的ISR远低于ISR-guided。\\\\n\\\\n对比 plan002-b01 (ISR β=0.1):\\\\n- PR: 0.79 vs 0.81 (≈持平, Δ=0.02)\\\\n- Mean ISR: 0.104 vs 0.337 (ISR 3.2x higher)\\\\n- Proved-only ISR: 0.131 vs 0.415 (ISR 3.2x higher)\\\\n- Median ISR: 0.036 vs plan002未记录\\\\n- Component count: 8.46 vs 5.58 (random组更多冗余)\\\\n- ISR=0占比(proved): 36.7% (random组大量proof无结构)\\\\n- Tautological collapse: 无 (component_2_ratio=0)\\\\n\\\\n关键发现: PR几乎相同说明β=0.1 random噪声不影响证明能力。但ISR差3.2倍，证明ISR reward提供genuine structural guidance而非仅variance regularization。这强力支持Claim 2: ISR信号在低剂量下有结构价值。\\\\n\\\\nEval output: /root/autodl-tmp/outputs/plan018_additive_random_b01_s42/eval_results.json\\\"}, \\\"plan005-sta-low-s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-13T22:20:47.812Z\\\", \\\"updated_at\\\": \\\"2026-05-14T06:31:05.119Z\\\", \\\"conclusion\\\": \\\"negative\\\", \\\"metrics\\\": {\\\"total_steps\\\": 500, \\\"duration_min\\\": 71, \\\"parse_rate\\\": 1, \\\"overall_prove_rate\\\": 0.5657, \\\"overall_isr\\\": 0.1682, \\\"last50_prove_rate\\\": 0.77, \\\"last50_isr\\\": 0.2559, \\\"last100_prove_rate\\\": 0.7725, \\\"last100_isr\\\": 0.2299, \\\"last100_loss\\\": 0.022752, \\\"overall_loss\\\": 0.017296, \\\"last100_isr_pr_ratio\\\": 0.298, \\\"last100_isr_lt_pr_count\\\": \\\"99/100\\\", \\\"first_rolling10_pr_ge_0.8\\\": 178, \\\"first_rolling10_pr_ge_0.9\\\": 439, \\\"max_rolling10_pr\\\": 0.9375, \\\"max_rolling10_isr\\\": 0.3282, \\\"windowed\\\": {\\\"1-50\\\": {\\\"pr\\\": 0.1775, \\\"isr\\\": 0.0906}, \\\"51-100\\\": {\\\"pr\\\": 0.1775, \\\"isr\\\": 0.0835}, \\\"101-200\\\": {\\\"pr\\\": 0.5062, \\\"isr\\\": 0.1463}, \\\"201-300\\\": {\\\"pr\\\": 0.6713, \\\"isr\\\": 0.1791}, \\\"301-400\\\": {\\\"pr\\\": 0.7013, \\\"isr\\\": 0.1984}, \\\"401-500\\\": {\\\"pr\\\": 0.7725, \\\"isr\\\": 0.2299}}}, \\\"notes\\\": \\\"conclusion=negative 基于 prove_rate 下降（last100 0.7725 vs exec-only 0.865）。但结构性发现：ISR/PR ratio=0.298，99/100 步 ISR &lt; PR，说明 STA=0.1 维持了 ISR 与 PR 的持续分离——模型未通过 hacking prove_rate 绕过 STA penalty。此观察支持论文 \\\\\\\"STA 抑制 reward hacking\\\\\\\" claim。windowed ISR/PR: 1-50 (0.51), 51-100 (0.47), 101-200 (0.29), 201-300 (0.27), 301-400 (0.28), 401-500 (0.30) — 分离在100步后稳定。D030 决策：checkpoint 已删除，不重训。论文用训练曲线 windowed ISR/PR 数据作为证据。\\\"}, \\\"plan001-exec-only-s43-r4\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-14T01:40:37.808Z\\\", \\\"updated_at\\\": \\\"2026-05-14T06:30:57.539Z\\\", \\\"metrics\\\": {\\\"eval_sampling_prove_rate\\\": 0.14, \\\"eval_sampling_mean_isr\\\": 0, \\\"eval_sampling_n_proved\\\": 14, \\\"eval_sampling_temperature\\\": 0.7, \\\"eval_sampling_method\\\": \\\"do_sample=True, temperature=0.7\\\", \\\"eval_sampling_by_answer\\\": {\\\"true\\\": {\\\"count\\\": 34, \\\"proved\\\": 6, \\\"prove_rate\\\": 0.176}, \\\"false\\\": {\\\"count\\\": 25, \\\"proved\\\": 2, \\\"prove_rate\\\": 0.08}, \\\"unknown\\\": {\\\"count\\\": 41, \\\"proved\\\": 6, \\\"prove_rate\\\": 0.146}}}, \\\"conclusion\\\": \\\"negative\\\", \\\"notes\\\": \\\"训练 PR(last100)=0.883 但 eval PR=14% (sampling, T=0.7), ISR=0。87% 样本 hit max_new_tokens 生成不可解析长输出。与 s42 (eval PR=93%) 形成极端跨 seed 不稳定。exec-only reward landscape 存在极大方差。⚠️ 评估方法：sampling eval (T=0.7)，其他组用 eval_sta.py full STA。D029 决策：不重训，论文标注方法差异。PR=14% 是 failure case，eval 方法不影响结论。\\\"}, \\\"plan017-additive-random-s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-14T03:11:14.694Z\\\", \\\"updated_at\\\": \\\"2026-05-14T05:33:25.603Z\\\", \\\"hypothesis\\\": \\\"Additive random control: r = r_exec·(1+0.3·random). 隔离 ISR structural signal vs variance regularization. 若 ISR > random > exec-only → signal+regularization 均贡献; 若 ISR > random ≈ exec-only → ISR signal 是关键; 若 ISR ≈ random → ISR 无结构价值。\\\", \\\"parent\\\": \\\"plan013-random-reward-s42-r4\\\", \\\"conclusion\\\": \\\"negative\\\", \\\"notes\\\": \\\"Eval结果: PR=0.48, mean_ISR=0.0453, proved_only_ISR=0.0943, mean_components=9.56 (3+比例100%, 无tautological collapse). 但33%已证明样本ISR=0 (n_necessary=0, conclusion trivially provable). 与plan013的不同failure mode: additive random防止了2-component坍缩, 但模型转向生成复杂但无用的formalization (多premises但conclusion不依赖任何premise). Variance regularization不足以产生genuine proofs.\\\", \\\"metrics\\\": {\\\"eval_prove_rate\\\": 0.48, \\\"eval_mean_isr\\\": 0.0453, \\\"eval_isr_std\\\": 0.0759, \\\"eval_median_isr\\\": 0, \\\"eval_max_isr\\\": 0.2857, \\\"eval_proved_only_isr\\\": 0.0943, \\\"eval_n_proved\\\": 48, \\\"eval_n_problems\\\": 100, \\\"eval_method\\\": \\\"eval_sta.py full STA\\\", \\\"eval_data\\\": \\\"proofwriter_fol_100.jsonl\\\", \\\"eval_component_count_mean\\\": 9.6, \\\"eval_component_count_2_ratio\\\": 0, \\\"eval_isr_pr_ratio\\\": 0.0943, \\\"eval_elapsed_s\\\": 542.3, \\\"eval_by_type_false_pr\\\": 0.32, \\\"eval_by_type_false_isr\\\": 0.0254, \\\"eval_by_type_unknown_pr\\\": 0.51, \\\"eval_by_type_unknown_isr\\\": 0.0518, \\\"eval_by_type_true_pr\\\": 0.56, \\\"eval_by_type_true_isr\\\": 0.052, \\\"tautological_collapse\\\": false}}, \\\"plan014-downstream-nli-s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-14T03:43:37.925Z\\\", \\\"updated_at\\\": \\\"2026-05-14T04:29:48.645Z\\\", \\\"hypothesis\\\": \\\"Downstream NLI validation: 高ISR formalization 应在独立推理任务上表现更好(entailment accuracy)，Spearman ρ(ISR, accuracy) > 0.1 验证 ISR 作为 quality proxy 的实用价值。同时用 Z3 cross-solver agreement 验证 formalization 鲁棒性。\\\", \\\"notes\\\": \\\"Negative: ISR 作为 downstream NLI quality proxy 无效。Spearman ρ(ISR, correct)=-0.049 (p=0.187)，Best-of-N ISR 仅 +0.9pp over random (不显著)。主因：模型严重 true-bias (false accuracy=0%)，NLI accuracy 天花板仅 34.1%，ISR 无区分空间。ISR bucket 层面有弱单调趋势 (high=75% > mid=37.7% > low=32.7%) 但 high bucket 仅 12 样本。quartile 分析非单调。\\\", \\\"conclusion\\\": \\\"negative\\\", \\\"metrics\\\": {\\\"overall_accuracy\\\": 0.341, \\\"proved_rate\\\": 0.915, \\\"proved_count\\\": 732, \\\"total_generations\\\": 800, \\\"parse_errors\\\": 0, \\\"accuracy_by_label\\\": {\\\"true\\\": 0.912, \\\"false\\\": 0, \\\"unknown\\\": 0.076}, \\\"spearman_rho\\\": -0.049, \\\"spearman_p\\\": 0.187, \\\"mann_whitney_U\\\": 17202, \\\"mann_whitney_p\\\": 0.288, \\\"bon_isr_accuracy\\\": 0.35, \\\"bon_random_accuracy\\\": 0.341, \\\"bon_oracle_accuracy\\\": 0.44, \\\"bon_prove_first_accuracy\\\": 0.35, \\\"isr_bucket_high_acc\\\": 0.75, \\\"isr_bucket_mid_acc\\\": 0.377, \\\"isr_bucket_low_acc\\\": 0.327, \\\"runtime_inference_s\\\": 408.8, \\\"runtime_eval_s\\\": 13.6}}, \\\"plan002-additive-b03-s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-14T02:24:47.843Z\\\", \\\"updated_at\\\": \\\"2026-05-14T04:27:38.822Z\\\", \\\"metrics\\\": {\\\"total_steps\\\": 500, \\\"duration_min\\\": 56.7, \\\"overall_prove_rate\\\": 0.34025, \\\"overall_isr\\\": 0.11527, \\\"first20_prove_rate\\\": 0.15625, \\\"last50_prove_rate\\\": 0.555, \\\"last100_prove_rate\\\": 0.5525, \\\"mean_loss\\\": 0.008914, \\\"last100_loss\\\": 0.014469, \\\"parse_rate\\\": 1, \\\"w1_50_prove_rate\\\": 0.13, \\\"w51_100_prove_rate\\\": 0.095, \\\"w101_200_prove_rate\\\": 0.185, \\\"w201_300_prove_rate\\\": 0.375, \\\"w301_400_prove_rate\\\": 0.47625, \\\"w401_500_prove_rate\\\": 0.5525, \\\"steps_ge_085\\\": 52, \\\"first_step_ge_085\\\": 46, \\\"final_prove_rate\\\": 1, \\\"final_isr_mean\\\": 0.3089, \\\"final_reward_mean\\\": 1.0927}, \\\"notes\\\": \\\"ISR 为 binary 近似 (_fast_fn)，不可用于论文跨 run 对比，需 eval_sta.py 统一评估真实 ISR。prove_rate 轨迹 0.13→0.095→0.185→0.375→0.476→0.553，呈稳步上升趋势，尚未完全饱和（仅 52/500 步 ≥0.85），与 plan001/plan013 的强饱和模式不同。\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"plan013-random-reward-s42-r4\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-14T01:40:35.587Z\\\", \\\"updated_at\\\": \\\"2026-05-14T03:45:53.344Z\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"eval_prove_rate\\\": 1, \\\"eval_mean_isr\\\": 0.535, \\\"eval_isr_std\\\": 0.1282, \\\"eval_proved_only_isr\\\": 0.535, \\\"eval_median_isr\\\": 0.5, \\\"eval_n_proved\\\": 100, \\\"eval_n_problems\\\": 100, \\\"eval_method\\\": \\\"eval_sta.py full STA\\\", \\\"eval_data\\\": \\\"proofwriter_fol_100.jsonl\\\", \\\"eval_note\\\": \\\"DEGENERATE: model generates trivial 2-component proofs (premise=conclusion, conclusion=conclusion), ISR=0.5 is artifact of trivial proof structure\\\"}, \\\"notes\\\": \\\"⚠️ 训练日志 ISR 为 binary approximation (_fast_fn)，ISR≈prove_rate，不含结构信息。真实 ISR 需通过 eval_sta.py (full STA) 在 checkpoint-500 上重新评估。final_mean_isr=0.6705 实为 binary 近似值，禁止用于论文或跨实验 ISR 对比。\\\"}, \\\"plan001-exec-only-s43-r3\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-14T01:02:31.830Z\\\", \\\"updated_at\\\": \\\"2026-05-14T01:41:28.427Z\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"plan013-random-reward-s42-r3\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-14T01:02:30.063Z\\\", \\\"updated_at\\\": \\\"2026-05-14T01:41:28.122Z\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"plan001-exec-only-s43-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-14T00:22:12.292Z\\\", \\\"updated_at\\\": \\\"2026-05-14T01:01:56.416Z\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"plan013-random-reward-s42-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-14T00:22:10.140Z\\\", \\\"updated_at\\\": \\\"2026-05-14T01:01:55.694Z\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"plan013-random-reward-s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-13T23:56:44.062Z\\\", \\\"updated_at\\\": \\\"2026-05-14T00:21:05.430Z\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"plan001-exec-only-s43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-13T23:55:08.635Z\\\", \\\"updated_at\\\": \\\"2026-05-14T00:21:04.003Z\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"plan001-exec-only-s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-13T22:19:41.568Z\\\", \\\"updated_at\\\": \\\"2026-05-13T23:03:42.892Z\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"plan003-eval-exec-only-r5\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-13T22:21:48.691Z\\\", \\\"updated_at\\\": \\\"2026-05-13T23:03:19.945Z\\\", \\\"metrics\\\": {\\\"prove_rate\\\": 0.32, \\\"mean_isr\\\": 0.2055, \\\"isr_std\\\": 0.3194, \\\"proved_only_isr\\\": 0.6423, \\\"isr_by_type\\\": {\\\"true\\\": 0.3598, \\\"false\\\": 0.1723, \\\"unknown\\\": 0.0979}, \\\"total_samples\\\": 100, \\\"proved_count\\\": 32, \\\"runtime_s\\\": 251.7}, \\\"conclusion\\\": \\\"success\\\"}, \\\"plan001-exec-only-s42-r3\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-13T22:42:40.242Z\\\", \\\"updated_at\\\": \\\"2026-05-13T23:03:11.395Z\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"sta-phase1-exec-sta-r5\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-13T20:54:31.353Z\\\", \\\"updated_at\\\": \\\"2026-05-13T22:20:41.274Z\\\", \\\"metrics\\\": {\\\"parse_rate\\\": 1, \\\"prove_rate\\\": 0.1, \\\"mean_isr\\\": 0.04347, \\\"last20_prove_rate\\\": 0.15, \\\"last20_isr_mean\\\": 0.04956, \\\"first20_prove_rate\\\": 0.08125, \\\"first20_isr_mean\\\": 0.05182, \\\"overall_reward_mean\\\": 0.07174, \\\"last20_reward_mean\\\": 0.09978, \\\"training_steps\\\": 100, \\\"training_minutes\\\": 16.9, \\\"step_time_s\\\": 10.13, \\\"isr_pr_ratio_overall\\\": 0.43, \\\"isr_pr_ratio_last20\\\": 0.33, \\\"K\\\": 8}, \\\"conclusion\\\": \\\"negative\\\"}, \\\"sta-phase1-exec-only-r5\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-13T20:54:27.505Z\\\", \\\"updated_at\\\": \\\"2026-05-13T21:53:04.486Z\\\", \\\"metrics\\\": {\\\"parse_rate\\\": 1, \\\"prove_rate\\\": 0.15125, \\\"mean_isr\\\": 0.1475, \\\"last20_prove_rate\\\": 0.2, \\\"last20_isr_mean\\\": 0.2, \\\"first20_prove_rate\\\": 0.11875, \\\"first20_isr_mean\\\": 0.11875, \\\"overall_reward_mean\\\": 0.15125, \\\"last20_reward_mean\\\": 0.2, \\\"training_steps\\\": 100, \\\"training_minutes\\\": 15.7, \\\"step_time_s\\\": 9.44, \\\"isr_pr_ratio_last20\\\": 1, \\\"K\\\": 8}, \\\"conclusion\\\": \\\"success\\\"}, \\\"sta-phase1-exec-sta-r4\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-13T20:28:22.778Z\\\", \\\"updated_at\\\": \\\"2026-05-13T20:52:58.761Z\\\", \\\"metrics\\\": {\\\"parse_rate\\\": 1, \\\"prove_rate\\\": 0.1575, \\\"mean_isr\\\": 0.1525, \\\"last20_prove_rate\\\": 0.2125, \\\"last20_isr_mean\\\": 0.2125, \\\"first20_reward_mean\\\": 0.119, \\\"training_steps\\\": 100, \\\"training_minutes\\\": 15}, \\\"conclusion\\\": \\\"negative\\\", \\\"notes\\\": \\\"Phase 1 r4 完成但无差异。fast_isr_fol 二值信号(0/1)对 proved samples 几乎全部 ISR=1，exec+STA reward ≈ exec-only reward。连续 ISR 才能产生有意义的差异信号。→ r5 改用 full sta_reward (continuous ISR 0.0-1.0) + K=8\\\"}, \\\"sta-phase1-exec-only-r4\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-13T20:28:18.040Z\\\", \\\"updated_at\\\": \\\"2026-05-13T20:52:56.416Z\\\", \\\"metrics\\\": {\\\"parse_rate\\\": 1, \\\"prove_rate\\\": 0.15125, \\\"mean_isr\\\": 0.1475, \\\"last20_prove_rate\\\": 0.2, \\\"last20_isr_mean\\\": 0.2, \\\"first20_reward_mean\\\": 0.119, \\\"training_steps\\\": 100, \\\"training_minutes\\\": 15}, \\\"conclusion\\\": \\\"negative\\\", \\\"notes\\\": \\\"Phase 1 r4 完成但无差异。fast_isr_fol 二值信号(0/1)对 proved samples 几乎全部 ISR=1，导致 exec+STA ≈ exec-only。prove_rate 从 baseline 12% → last20 20%（微弱提升）。K=4 导致大量全零 reward batch。→ r5 改用 full STA + K=8\\\"}, \\\"sta-phase1-exec-only-r3\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-13T20:15:04.067Z\\\", \\\"updated_at\\\": \\\"2026-05-13T20:23:15.460Z\\\", \\\"conclusion\\\": \\\"failed\\\", \\\"notes\\\": \\\"EXIT_CODE=137 (OOM/SIGKILL) after ~276s. 同 sta-phase1-exec-sta-r3 一起诊断中\\\"}, \\\"sta-phase1-exec-sta-r3\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-13T20:15:08.133Z\\\", \\\"updated_at\\\": \\\"2026-05-13T20:23:14.516Z\\\", \\\"conclusion\\\": \\\"failed\\\", \\\"notes\\\": \\\"EXIT_CODE=137 (OOM/SIGKILL) after ~278s. 诊断中: worker_diagnose_sta-phase1-r3-oom_20260513T202300\\\"}, \\\"sta-phase1-exec-sta-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-13T19:55:08.640Z\\\", \\\"updated_at\\\": \\\"2026-05-13T19:55:41.544Z\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"sta-phase1-exec-only-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-13T19:55:04.711Z\\\", \\\"updated_at\\\": \\\"2026-05-13T19:55:37.426Z\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"sta-phase1-exec-sta\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-13T18:26:53.258Z\\\", \\\"updated_at\\\": \\\"2026-05-13T19:33:03.905Z\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"sta-phase1-exec-only\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-13T18:26:46.351Z\\\", \\\"updated_at\\\": \\\"2026-05-13T19:33:01.169Z\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"sta-gt-isr-baseline\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-13T18:11:13.283Z\\\", \\\"updated_at\\\": \\\"2026-05-13T18:12:44.147Z\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"gt_prove_rate\\\": 0.18, \\\"gt_mean_isr\\\": 0.5588, \\\"gt_isr_std\\\": 0.2582, \\\"gt_isr_median\\\": 0.6125, \\\"solver_execution_rate\\\": 1, \\\"true_prove_rate\\\": 0.5, \\\"true_mean_isr\\\": 0.5833}}, \\\"sta-phase0-baseline\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-13T17:51:48.853Z\\\", \\\"updated_at\\\": \\\"2026-05-13T18:10:40.982Z\\\", \\\"metrics\\\": {\\\"mean_isr\\\": 0.0641, \\\"isr_std\\\": 0.1983, \\\"median_isr\\\": 0, \\\"isr_range\\\": [0, 0.889], \\\"prove_rate\\\": 0.12, \\\"proved_count\\\": 12, \\\"total_samples\\\": 100, \\\"xor_affected_samples\\\": 34, \\\"effective_prove_rate_no_xor\\\": 0.182, \\\"avg_time_per_sample_s\\\": 3.4, \\\"total_runtime_s\\\": 336, \\\"isr_by_answer\\\": {\\\"true\\\": {\\\"n\\\": 34, \\\"proved\\\": 9, \\\"prove_rate\\\": 0.265, \\\"mean_isr\\\": 0.1345}, \\\"false\\\": {\\\"n\\\": 25, \\\"proved\\\": 1, \\\"prove_rate\\\": 0.04, \\\"mean_isr\\\": 0.024}, \\\"unknown\\\": {\\\"n\\\": 41, \\\"proved\\\": 2, \\\"prove_rate\\\": 0.049, \\\"mean_isr\\\": 0.0302}}}, \\\"conclusion\\\": \\\"success\\\"}}, \\\"count\\\": 50, \\\"total\\\": 50, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.2333}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"plan006-prolog-sta-s44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T09:19:39.743Z\", \"updated_at\": \"2026-05-14T18:47:53.131Z\", \"hypothesis\": \"Prolog exec+STA GRPO seed=44: 第三 seed。3-seed mean±std 用于论文 Claim 3 跨 logic type 统计支撑。\", \"notes\": \"Reviewer 独立核实: query-as-fact gaming, 0% genuine. 97/97 proved 样本中 95/97 n_necessary=1（功能性 H7）。模型将 NL 问题转为 snake_case atom 同时设为 fact 和 query，Prolog trivially 证明。PR=0.97, ISR=0.885 是 gaming artifact（高 ISR 因单 clause = query）。第三种 Goodhart pathway（vs s42 clean H7, s43 degenerate syntax H1）。对照: s42=negative (clean H7=100%), s43=negative (uppercase pseudo-Prolog H1=97.4%), s44=negative (query-as-fact gaming, functional H7=95/97).\", \"metrics\": {\"pass_rate\": 0.97, \"isr_mean\": 0.885, \"isr_n_cl_ge3\": \"N/A (0 samples)\", \"n_clauses_dist\": \"78/100 single-clause, 22/100 two-clause\", \"h7_functional_rate\": 0.979, \"genuine_rate\": 0, \"premise_count_analysis\": \"100% artifact - zero samples with n_clauses>=3, model exclusively generates 1-2 clause programs\", \"failure_mode\": \"query-as-fact gaming (total H7 collapse)\"}, \"conclusion\": \"negative\"}, \"plan006-prolog-sta-s43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T09:19:39.141Z\", \"updated_at\": \"2026-05-14T18:20:56.947Z\", \"hypothesis\": \"Prolog exec+STA GRPO seed=43: 跨 seed 稳定性检查。与 exec-only s43 对照。\", \"notes\": \"Eval: PR=0.38, ISR=0.185 proved-only. Strict classifier: H7=0%, H1=0%, Genuine=100%. 但功能分析显示所有 38 proved 样本 n_necessary=1（功能性 H7）。模型生成大写伪 Prolog（如 MARY_IS_AN_AVADEOTE.）—— 非标准语法，strict classifier 无法匹配 conclusion。与 s42 (clean H7=100%) 不同的 Goodhart 路径，但同样是 hacking。磁盘 240G/250G 需清理。\", \"metrics\": {\"train\": {\"final_prove_rate\": 0.769, \"final_mean_isr\": 0.129, \"final_loss\": 0.0155, \"final_entropy\": 0.09, \"final_reward\": 0.573, \"completion_length_mean\": 143, \"train_runtime_seconds\": 5095, \"train_runtime_minutes\": 84.9}, \"eval\": {\"n_problems\": 100, \"n_proved\": 38, \"prove_rate\": 0.38, \"mean_isr\": 0.0704, \"isr_std\": 0.1263, \"median_isr\": 0, \"proved_only_mean_isr\": 0.1853, \"min_isr\": 0, \"max_isr\": 1, \"by_answer_type\": {\"false\": {\"count\": 25, \"proved\": 11, \"prove_rate\": 0.44, \"mean_isr\": 0.1003}, \"unknown\": {\"count\": 41, \"proved\": 11, \"prove_rate\": 0.268, \"mean_isr\": 0.0394}, \"true\": {\"count\": 34, \"proved\": 16, \"prove_rate\": 0.471, \"mean_isr\": 0.0859}}}, \"h7_classification\": {\"h7_strict\": 0, \"h7_rate\": 0, \"h1_strict\": 37, \"h1_rate\": 0.974, \"conclusion_in_premise_total\": 37, \"conclusion_in_premise_rate\": 0.974, \"genuine_count\": 0, \"genuine_rate\": 0, \"isr_1_count\": 1, \"note\": \"1 pseudo-genuine sample (folio_1415) has query embedded in single mega-clause; all 38/38 proved samples are tautological\"}}, \"conclusion\": \"negative\"}, \"plan016-extended-1000-s42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T05:29:47.634Z\", \"updated_at\": \"2026-05-14T17:34:52.375Z\", \"hypothesis\": \"Extended training 1000 steps exec-only: plan001-s42 500步 PR=93% 是真收敛还是 lucky early convergence? 1000步观察 PR 和 ISR 在更长 horizon 的行为。s43(14%)/s44(98% tautological) 在 500 步均失败，延长训练是否能改善？\", \"parent\": \"plan001-exec-only-s42-r2\", \"metrics\": {\"prove_rate\": 0.96, \"isr\": 0.003, \"n_proved\": 96, \"components\": 18.55, \"h7_count\": 0, \"h7_rate\": 0, \"h1_count\": 96, \"h1_rate\": 1, \"genuine_count\": 0, \"genuine_rate\": 0}, \"conclusion\": \"success\", \"notes\": \"Extended training to 1000 steps CONFIRMS ISR collapse worsens monotonically.\\\\n\\\\n## 500 vs 1000 step comparison (eval_sta.py):\\\\n| Metric | plan001-s42 (500步) | plan016 (1000步) | Change |\\\\n|--------|-------------------|-----------------|--------|\\\\n| eval PR | 0.93 | 0.96 | +3.2% |\\\\n| eval ISR | 0.123 | 0.0027 | -97.8% |\\\\n| proved_only ISR | 0.132 | 0.0028 | -97.9% |\\\\n| components | 6.58 | 18.55 | +182% |\\\\n| ISR=0 ratio | - | 94.8% | - |\\\\n| n_necessary=0 ratio | - | 94.8% | - |\\\\n\\\\n## Key findings:\\\\n1. PR improves (+3%) but ISR collapses near-zero (0.0027). The model gets BETTER at proving while becoming WORSE at faithful reasoning.\\\\n2. Component count nearly tripled (6.58→18.55). Model generates longer proofs with more components, but 94.8% have ZERO necessary components.\\\\n3. NOT tautological collapse (comp=2 ratio=0). Instead: contradiction-based collapse — model embeds P(a) and ¬P(a) among many irrelevant premises, making anything provable via explosion.\\\\n4. Windowed ISR trend is monotonically decreasing: 0.1115 (101-200) → 0.0433 (401-500) → 0.0200 (601-700) → 0.0144 (901-1000). No recovery signal.\\\\n5. The exec-only reward creates a pure reward hacking incentive: the model discovers that contradictions + trivially true conclusions always satisfy the prover.\\\\n\\\\n## Implication for paper:\\\\nExtended training is a clean ablation showing exec-only reward's failure mode worsens over time. The 500-step ISR of 0.123 was not a floor — it was a snapshot of ongoing collapse.\"}, \"plan002-additive-b01-s42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T05:29:08.138Z\", \"updated_at\": \"2026-05-14T17:33:21.938Z\", \"parent\": \"plan002-additive-b03-s42\", \"conclusion\": \"success\", \"metrics\": {\"eval_prove_rate\": 0.81, \"eval_mean_isr\": 0.3365, \"eval_isr_std\": 0.3227, \"eval_proved_only_isr\": 0.4154, \"eval_median_isr\": 0.2, \"eval_n_proved\": 81, \"eval_n_problems\": 100, \"eval_method\": \"eval_sta.py full STA\", \"eval_data\": \"proofwriter_fol_100.jsonl\", \"eval_component_count_mean\": 5.58, \"h7_rate\": 0.16, \"h7_count\": 13, \"h1_rate\": 0.519, \"h1_count\": 42, \"genuine_rate\": 0.309, \"genuine_count\": 25, \"tautological_collapse\": false}, \"notes\": \"H7 audit (2026-05-14): 81 proved samples. H7 (single premise=conclusion): 13/81=16.0%, mean ISR=0.6603. H1 (multi premise contains conclusion): 42/81=51.9%, mean ISR=0.2245. Genuine (no conclusion duplication): 26/81=32.1%, mean ISR=0.6014. Combined conclusion duplication = 67.9%. CRITICAL: only 32.1% of proved samples are free of conclusion embedding. H7 inflates ISR; H1 deflates ISR but proof is trivially achievable via embedded conclusion. Claim 2 \\\"genuine structural guidance\\\" needs reframing — ISR signal is dominated by conclusion duplication artifacts.\"}, \"plan018-additive-random-b01-s43-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T14:01:24.111Z\", \"updated_at\": \"2026-05-14T17:17:02.398Z\", \"hypothesis\": \"Random β=0.1 seed=43 控制组 r2: 重试 (原 s43 step 200 磁盘满崩溃)。与 plan002-b01-s43 (ISR β=0.1) 同 seed 对照。3-seed mean±std 审稿硬性要求。\", \"parent\": \"plan018-additive-random-b01-s43\", \"metrics\": {\"h7_rate\": 0, \"h7_count\": 0, \"h1_rate\": 93.2, \"h1_count\": 82, \"genuine_rate\": 6.8, \"genuine_count\": 6}, \"conclusion\": \"negative\"}, \"plan006-prolog-sta-s42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T09:19:38.117Z\", \"updated_at\": \"2026-05-14T16:49:42.052Z\", \"hypothesis\": \"Prolog exec+STA GRPO seed=42: ISR reward 在 Prolog logic type 上的效果。与 plan006-prolog-exec-s42 (exec-only) 对照，验证 STA/ISR 的 hacking 检测和 Goodhart 效应是否跨 logic type 泛化。\", \"notes\": \"Eval metrics provenance: eval 在训练完成后立即在 westd-39279 服务器上运行 eval_sta.py，checkpoint 路径 /root/autodl-tmp/outputs/plan006_prolog_sta_s42/。Eval 结果由 Worker 从服务器 SSH 读取 eval_results.json 并手动录入 registry。Checkpoint 可能已被磁盘清理删除（C003 save_total_limit=1）。训练日志: ~/runs/solver-trace-ablation/plan006-prolog-sta-s42.log。H7 分类由 classify_h7.py 在 eval 目录上运行。\", \"conclusion\": \"negative\", \"metrics\": {\"cumulative_prove_rate\": 0.848, \"cumulative_mean_isr\": 0.787, \"final_prove_rate\": 1, \"final_isr\": 1, \"final_reward\": 1, \"saturation_onset_step\": 100, \"train_loss\": 0.00716, \"training_hours\": 0.78, \"final_entropy\": 0.01, \"final_completion_length\": 27, \"initial_completion_length\": 120, \"steps_at_perfect_reward\": 400, \"train_runtime_sec\": 2791, \"eval_prove_rate\": 0.5, \"eval_mean_isr\": 0.5, \"eval_proved_only_isr\": 1, \"eval_h7_rate\": 1, \"eval_h7_count\": 50, \"eval_proved_count\": 50, \"eval_total_count\": 100, \"eval_n_clauses_mean\": 1, \"eval_isr_distribution\": \"binary: 50x0 + 50x1\"}}, \"plan001-exec-only-s44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T03:57:09.690Z\", \"updated_at\": \"2026-05-14T16:29:02.086Z\", \"hypothesis\": \"Exec-only seed=44 第3 seed: 解决 s42(93% eval PR) vs s43(13% eval PR) 的跨 seed 不稳定问题，3-seed mean±std 是论文必需。\", \"metrics\": {\"eval_prove_rate\": 0.98, \"eval_mean_isr\": 0.57, \"eval_isr_std\": 0.2013, \"eval_median_isr\": 0.5, \"eval_proved_only_isr\": 0.5816, \"eval_n_proved\": 98, \"eval_n_problems\": 100, \"eval_method\": \"eval_sta.py full STA\", \"eval_data\": \"proofwriter_fol_100.jsonl\", \"eval_component_count_mean\": 2.04, \"eval_component_count_2\": 94, \"eval_component_count_3\": 4, \"tautological_collapse\": true, \"h7_rate\": 1, \"h7_count\": 97, \"h1_rate\": 0, \"h1_count\": 0, \"genuine_rate\": 0, \"genuine_count\": 0, \"conclusion_embedding_total\": 1}, \"conclusion\": \"negative\", \"notes\": \"TAUTOLOGICAL COLLAPSE 确认。eval PR=98% 但 94% 样本仅 2 components (premise=conclusion tautology)，mean components=2.04，与 plan013 random reward 完全一致。ISR≈0.5 是 2-component artifact。s42 是唯一产生 genuine proofs (mean components=6.58) 的 seed。3-seed 结果：s42=genuine, s43=degraded(PR=13%), s44=tautological(PR=98% fake)。Exec-only reward 2/3 seeds 失败。\"}, \"plan001-exec-only-s42-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T22:40:41.773Z\", \"updated_at\": \"2026-05-14T16:28:58.538Z\", \"notes\": \"Cron 误判 DONE/failed（因 --help|grep 前缀命令的 PID 84896 退出，实际训练子进程 PID 84901 仍在运行）。已手动恢复 RUNNING。严禁在 cuda:0 启动新进程直到 r2 自然完成。⚠️ Reviewer 中期审查标注: 训练日志中 ISR=0.8612 为 binary approximation (_fast_fn)，非真实 ISR。最终可比 ISR 需通过 eval_sta.py (full STA) 重新评估。\", \"conclusion\": \"success\", \"metrics\": {\"eval_prove_rate\": 0.93, \"eval_mean_isr\": 0.1232, \"eval_isr_std\": 0.1887, \"eval_proved_only_isr\": 0.1324, \"eval_median_isr\": 0, \"eval_n_proved\": 93, \"eval_n_problems\": 100, \"eval_method\": \"eval_sta.py full STA\", \"eval_data\": \"proofwriter_fol_100.jsonl\", \"h7_rate\": 0, \"h7_count\": 0, \"h1_rate\": 0.871, \"h1_count\": 81, \"genuine_rate\": 0.129, \"genuine_count\": 12, \"genuine_mean_isr\": 0.3141, \"h1_mean_isr\": 0.1055, \"conclusion_embedding_total\": 0.871}}, \"plan006-prolog-exec-s44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T07:13:35.647Z\", \"updated_at\": \"2026-05-14T16:27:18.570Z\", \"hypothesis\": \"Prolog exec-only GRPO seed=44: third seed for Prolog exec-only. Together with s42 (PR=83%, ISR=0.031) and s43, provides 3-seed evidence for cross-logic generalization claim (Claim 3). 3-seed mean±std required for paper.\", \"notes\": \"Eval 完成。PR=21% (3-seed 最低), ISR=0.081, proved_only_ISR=0.387 (max_ISR=1.0)。与 s42/s43 不同模式：PR 极低但 proved_only_ISR 较高，可能有少量样本 ISR=1 (H7-like)。Prolog exec-only 3-seed 汇总：s42 PR=83%/ISR=0.031, s43 PR=56%/ISR=0.008, s44 PR=21%/ISR=0.081。Mean PR=53.3%±31.1%, Mean ISR=0.040±0.037。跨 seed 极不稳定（PR std=31pp），与 FOL exec-only 一致。ISR 始终极低（<0.1），确认 Prolog exec-only 不产生 genuine reasoning traces。\", \"metrics\": {\"eval_prove_rate\": 0.21, \"eval_mean_isr\": 0.0812, \"eval_isr_std\": 0.2343, \"eval_median_isr\": 0, \"eval_proved_only_isr\": 0.3866, \"eval_min_isr\": 0, \"eval_max_isr\": 1, \"eval_n_proved\": 21, \"eval_n_problems\": 100, \"eval_method\": \"eval_sta.py full STA\", \"eval_data\": \"proofwriter_fol_100.jsonl\", \"eval_elapsed_seconds\": 683.9, \"eval_by_type_false_pr\": 0.04, \"eval_by_type_false_isr\": 0.04, \"eval_by_type_unknown_pr\": 0.317, \"eval_by_type_unknown_isr\": 0.099, \"eval_by_type_true_pr\": 0.206, \"eval_by_type_true_isr\": 0.09, \"solver\": \"PrologSolver\", \"logic_type\": \"prolog\"}, \"conclusion\": \"negative\"}, \"plan009-sft-baseline-s42-r4\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T11:40:28.142Z\", \"updated_at\": \"2026-05-14T16:27:01.864Z\", \"hypothesis\": \"SFT baseline: supervised finetuning on FOLIO data (500 steps, Qwen3-4B, same model as all GRPO experiments) to establish whether hacking patterns are GRPO-specific or general finetuning artifacts. r4: fix CUDA_VISIBLE_DEVICES + --gpu + --no_wandb.\", \"parent\": \"plan009-sft-baseline-s42-r2\", \"notes\": \"r4 训练完成 (500 steps, TRL SFT). Checkpoint 实际保存在 plan009_sft_baseline_s42（非 plan009_sft_s42_r4）。两卡满载 (cuda:0 80GB, cuda:1 80GB)，eval 待 GPU 释放。checkpoint-500/ 含 15GB optimizer.pt 可在 eval 后清理。\", \"metrics\": {\"eval_prove_rate\": 0.14, \"eval_mean_isr\": 0.08, \"eval_isr_std\": 0.214, \"eval_median_isr\": 0, \"eval_max_isr\": 0.833, \"eval_proved_only_isr\": 0.571, \"eval_n_proved\": 14, \"eval_n_problems\": 100, \"eval_method\": \"eval_sta.py full STA\", \"eval_data\": \"proofwriter_fol_100.jsonl\", \"train_final_loss\": 0.0287, \"train_token_accuracy\": 0.9935, \"train_epochs\": 7.94, \"train_runtime_sec\": 789.6, \"by_answer_type\": {\"true\": {\"count\": 34, \"proved\": 13, \"pr\": 0.382, \"isr\": 0.226}, \"unknown\": {\"count\": 41, \"proved\": 1, \"pr\": 0.024, \"isr\": 0.008}, \"false\": {\"count\": 25, \"proved\": 0, \"pr\": 0, \"isr\": 0}}, \"h7_rate\": 0, \"h7_count\": 0, \"h1_rate\": 0.071, \"h1_count\": 1, \"genuine_rate\": 0.929, \"genuine_count\": 13, \"hacking_patterns\": \"near-zero (1/14 H1, 0 H7, 92.9% genuine)\", \"tautological_collapse\": false}, \"conclusion\": \"success\"}, \"plan006-prolog-exec-s43-r3\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T12:38:23.818Z\", \"updated_at\": \"2026-05-14T16:16:56.523Z\", \"hypothesis\": \"Prolog exec-only GRPO seed=43 r3: warmup_ratio=0.0 与 s42 一致。r2 因残留进程 OOM 失败，cuda:1 已清理。\", \"notes\": \"Eval 完成。PR=56% (远低于 s42 的 83%), ISR=0.0084 (与 s42 的 0.031 同量级，均极低)。proved_only_ISR=0.015。Prolog exec-only 跨 seed 表现：s42 PR=83%/ISR=0.031, s43 PR=56%/ISR=0.008。s43 prove_rate 显著下降但 ISR 模式一致（极低，ground fact enumeration hacking）。与 FOL exec-only 类似，存在跨 seed 不稳定性（FOL: s42=93%, s43=14%, s44=98%）。等 s44 eval 完成后计算 3-seed mean±std。\", \"metrics\": {\"eval_prove_rate\": 0.56, \"eval_mean_isr\": 0.0084, \"eval_isr_std\": 0.0221, \"eval_median_isr\": 0, \"eval_proved_only_isr\": 0.015, \"eval_min_isr\": 0, \"eval_max_isr\": 0.1, \"eval_n_proved\": 56, \"eval_n_problems\": 100, \"eval_method\": \"eval_sta.py full STA\", \"eval_data\": \"proofwriter_fol_100.jsonl\", \"eval_elapsed_seconds\": 868.2, \"eval_by_type_false_pr\": 0.48, \"eval_by_type_false_isr\": 0.0043, \"eval_by_type_unknown_pr\": 0.6585, \"eval_by_type_unknown_isr\": 0.0114, \"eval_by_type_true_pr\": 0.5, \"eval_by_type_true_isr\": 0.0078, \"solver\": \"PrologSolver\", \"logic_type\": \"prolog\"}, \"conclusion\": \"negative\"}, \"plan018-additive-random-b01-s44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T08:36:18.722Z\", \"updated_at\": \"2026-05-14T15:00:09.178Z\", \"hypothesis\": \"Random β=0.1 seed=44 控制组：与 plan002-b01-s44 (ISR β=0.1) 同 seed 对照。验证 ISR 3.2x > random 的结论在 s44 下是否成立。\", \"parent\": \"plan018-additive-random-b01-s42\", \"metrics\": {\"prove_rate\": 0.89, \"mean_isr\": 0.0619, \"isr_std\": 0.1756, \"median_isr\": 0, \"proved_only_mean_isr\": 0.0695, \"n_proved\": 89, \"n_problems\": 100, \"max_isr\": 1, \"min_isr\": 0, \"isr_pr_ratio\": 0.0695, \"isr_zero_count\": 72, \"isr_one_count\": 2, \"by_answer_type\": {\"false\": {\"count\": 25, \"proved\": 21, \"prove_rate\": 0.84, \"mean_isr\": 0.0533}, \"unknown\": {\"count\": 41, \"proved\": 40, \"prove_rate\": 0.976, \"mean_isr\": 0.0892}, \"true\": {\"count\": 34, \"proved\": 28, \"prove_rate\": 0.824, \"mean_isr\": 0.0353}}, \"elapsed_seconds\": 1012.7, \"eval_method\": \"eval_sta.py with Prover9Solver, FOL\"}, \"conclusion\": \"success\", \"notes\": \"DONE (success). Random β=0.1 s44 对照分析完成: PR=0.89/ISR=0.062 (clean) vs ISR β=0.1 s44 PR=0.89/ISR=0.803 (H7=86.5% inflated). 同 PR 下 ISR reward 导致 conclusion duplication，random 无此问题。与 s42 结论一致: ISR s42 genuine ISR=0.337 vs Random s42 ISR=0.104 (3.2x)。Random 2/3 seeds done, 等 s43 (plan018-random-b01-s43-r2 QUEUED)。\"}, \"plan009-sft-baseline-s42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T10:51:58.328Z\", \"updated_at\": \"2026-05-14T14:20:43.363Z\", \"hypothesis\": \"SFT baseline: supervised finetuning on FOLIO data (500 steps, Qwen3-4B) to establish whether hacking patterns are GRPO-specific or general finetuning artifacts. Same model as all GRPO experiments for fair comparison.\", \"conclusion\": \"killed\", \"notes\": \"模型必须改为 Qwen3-4B（与 GRPO 实验一致）。用 Qwen2.5-1.5B 无法作为 fair baseline——模型不同无法隔离训练方法差异。修正模型后重新注册提交。\"}, \"plan006-prolog-exec-s43-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T12:32:37.140Z\", \"updated_at\": \"2026-05-14T13:43:01.701Z\", \"hypothesis\": \"Prolog exec-only GRPO seed=43 r2: 修正 warmup_ratio=0.0 与 s42 一致。cross-seed stability check for Prolog logic type.\", \"parent\": \"plan006-prolog-exec-s43\", \"conclusion\": \"failed\", \"notes\": \"OOM 诊断：非 batch size 问题。根因是 kill_job 只杀了 tmux 包装进程 (PID 587155)，训练子进程 587159/587160 残留在 cuda:1 上占 78.09 GiB 显存。s43-r2 启动时 cuda:1 仅剩 40 MiB free，首次前向传播即 OOM (尝试分配 48 MiB)。教训：kill_job 后必须 SSH 确认子进程也已终止（ps aux grep + nvidia-smi），不能只看 PID 返回成功。\"}, \"plan006-prolog-exec-s42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T07:13:34.169Z\", \"updated_at\": \"2026-05-14T12:33:17.845Z\", \"hypothesis\": \"Prolog exec-only GRPO seed=42: STA/ISR hacking patterns generalize across logic types? Prolog uses rule ablation (vs FOL axiom ablation). If same degeneration modes appear → STA is logic-agnostic diagnostic.\", \"notes\": \"Eval (eval_sta.py) 完成。PR=83%, mean_ISR=0.031, proved_only_ISR=0.037, H7=0%, H1=0%。与 sta-s42 (PR=50%, ISR=1.0, H7=100%) 形成鲜明对比。exec-only 产生完全不同的 hacking 模式：ground fact enumeration（倾泻大量无关 ground facts，query 作为其中一个 fact 平凡成功），而非 sta-s42 的 tautological collapse。两种 reward signal 驱动两种不同的 hacking 策略。对论文是 positive finding：强化 Claim 1 且揭示 reward-specific hacking 机制。\", \"metrics\": {\"eval_prove_rate\": 0.83, \"eval_mean_isr\": 0.031, \"eval_proved_only_isr\": 0.037, \"eval_median_isr\": 0, \"eval_max_isr\": 0.2, \"eval_isr_std\": 0.0534, \"h7_rate\": 0, \"h1_rate\": 0, \"isr_1_rate\": 0, \"single_premise_rate\": 0, \"by_answer_type\": {\"true\": {\"proved\": 37, \"count\": 40, \"pr\": 0.925, \"isr\": 0.037}, \"false\": {\"proved\": 21, \"count\": 29, \"pr\": 0.724, \"isr\": 0.038}, \"unknown\": {\"proved\": 25, \"count\": 31, \"pr\": 0.806, \"isr\": 0.016}}}, \"conclusion\": \"negative\"}, \"plan006-prolog-exec-s43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T07:13:35.078Z\", \"updated_at\": \"2026-05-14T12:32:13.799Z\", \"hypothesis\": \"Prolog exec-only GRPO seed=43: cross-seed stability check for Prolog logic type. FOL showed extreme cross-seed variance (s42 genuine vs s43 degraded vs s44 tautological). Prolog exec-only s42 showed PR=83%, ISR=0.031. s43 tests if Prolog also has seed instability.\", \"notes\": \"KILLED at step 36/500: warmup_ratio=0.1 与 s42 (0.0) 不一致，3-seed 对比无效。重启为 plan006-prolog-exec-s43-r2 (warmup_ratio=0.0)。\", \"conclusion\": \"killed\"}, \"plan009-sft-baseline-s42-r3\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T11:37:49.306Z\", \"updated_at\": \"2026-05-14T11:48:05.087Z\", \"hypothesis\": \"SFT baseline: supervised finetuning on FOLIO data (500 steps, Qwen3-4B, same model as all GRPO experiments) to establish whether hacking patterns are GRPO-specific or general finetuning artifacts. Compare eval PR/ISR/hacking taxonomy against GRPO exec-only and exec+ISR conditions.\", \"parent\": \"plan009-sft-baseline-s42-r2\", \"wandb_run_id\": \"plan009-sft-s42-r3\", \"conclusion\": \"failed\", \"notes\": \"r3 crash root cause: wandb.init() failed because no W&B API key configured on server (no .netrc, no WANDB_API_KEY). Fix: add --no_wandb flag. Secondary issue: both GPUs currently near-full, need to wait for GPU availability before r4. Correct r4 command: export CUDA_VISIBLE_DEVICES=N && ... python3 scripts/train_sft.py --model_path /root/autodl-tmp/models/Qwen3-4B --data_path data/train_500_seed42.jsonl --output_dir /root/autodl-tmp/outputs/plan009_sft_s42_r4 --num_steps 500 --seed 42 --no_wandb\"}, \"plan009-sft-baseline-s42-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T11:02:25.369Z\", \"updated_at\": \"2026-05-14T11:43:20.347Z\", \"hypothesis\": \"SFT baseline: supervised finetuning on FOLIO data (500 steps, Qwen3-4B, same model as all GRPO experiments) to establish whether hacking patterns are GRPO-specific or general finetuning artifacts. Compare eval PR/ISR/hacking taxonomy against GRPO exec-only and exec+ISR conditions.\", \"notes\": \"SFT baseline with Qwen3-4B (same model as GRPO experiments). Replaces killed plan009-sft-baseline-s42 which incorrectly used Qwen2.5-1.5B. cuda:1, seed=42, 500 steps, FOLIO data (data/train_500_seed42.jsonl). Dream 审稿三档均指出缺 SFT baseline 是 gap。**FAILED**: 两个问题：(1) W&B API key 未配置，trainer.train() 启动时 wandb callback 报 UsageError; (2) device_map='auto' 把模型分到多 GPU，需改为单卡绑定。修复方案：加 WANDB_MODE=disabled + 改 train_sft.py 的 device_map 为单卡。\", \"conclusion\": \"failed\"}, \"plan018-additive-random-b01-s43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T08:36:18.260Z\", \"updated_at\": \"2026-05-14T11:42:09.950Z\", \"hypothesis\": \"Random β=0.1 seed=43 控制组：与 plan002-b01-s43 (ISR β=0.1) 同 seed 对照。验证 ISR 3.2x > random 的结论在 s43 下是否成立。\", \"parent\": \"plan018-additive-random-b01-s42\", \"conclusion\": \"failed\", \"notes\": \"Disk full (os error 28) at step 200/500 during checkpoint save. Training ran fine for 200 steps but safetensors serialization failed with \\\"No space left on device\\\". No checkpoint saved. Disk now has 109G free. Retryable as-is.\"}, \"plan002-additive-b01-s44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T08:36:17.298Z\", \"updated_at\": \"2026-05-14T10:12:40.545Z\", \"hypothesis\": \"ISR β=0.1 seed=44 多 seed 验证：exec-only s44 是 tautological collapse (PR=98%, ISR=0.57 fake)，ISR β=0.1 能否防止 tautological collapse？3-seed mean±std 用于论文 Claim 2。\", \"parent\": \"plan002-additive-b01-s42\", \"metrics\": {\"eval_prove_rate\": 0.89, \"eval_mean_isr\": 0.803, \"eval_isr_std\": 0.3418, \"eval_median_isr\": 1, \"component_count_mean\": 4.33, \"component_count_2_ratio\": 0.022, \"tautological_collapse\": false, \"isr_0_ratio\": 0.12, \"isr_1_ratio\": 0.73, \"proved_single_premise_ratio\": 1, \"h7_rate_calibrated\": 0.865, \"h7_definition\": \"single_premise AND premise==conclusion (normalized)\", \"hacking_mode\": \"conclusion_duplication_isr_inflation\", \"conclusion_embedding\": true, \"component_dist\": {\"2\": 2, \"4\": 54, \"5\": 33}, \"by_answer_type\": {\"false\": {\"n\": 25, \"proved\": 22, \"PR\": 0.88, \"ISR\": 0.824}, \"unknown\": {\"n\": 41, \"proved\": 38, \"PR\": 0.927, \"ISR\": 0.837}, \"true\": {\"n\": 34, \"proved\": 29, \"PR\": 0.853, \"ISR\": 0.747}}}, \"conclusion\": \"negative\", \"notes\": \"RECLASSIFIED negative (D039): Reviewer 逐样本审查发现 semantic drift hacking — 模型生成极简形式化（单 premise≈conclusion），通过 conclusion sub-component ablation 膨胀 ISR。ISR=0.902 是 conclusion_duplication_isr_inflation artifact，非真正证明质量。65% 样本 ISR=1.0 为 conclusion embedding。此 hacking mode 本身是论文 positive finding（强化 Claim 1 Goodhart 叙事：ISR reward 导致新型 hacking）。原始 eval 指标：PR=0.89, mean_isr=0.803, component_mean=4.33, comp_2_ratio=0.022。exec-only s44 是 tautological collapse (94% 2-comp)，ISR β=0.1 s44 避免了 tautological collapse 但转向了 conclusion duplication hacking。\"}, \"plan002-additive-b01-s43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T08:36:16.367Z\", \"updated_at\": \"2026-05-14T10:12:36.502Z\", \"hypothesis\": \"ISR β=0.1 seed=43 多 seed 验证：plan002-b01-s42 (PR=0.81, ISR=0.337) 在 s43 下是否可复现？exec-only s43 是 degraded seed (PR=14%)，ISR β=0.1 能否拯救 bad seed？3-seed mean±std 用于论文 Claim 2 统计支撑。\", \"parent\": \"plan002-additive-b01-s42\", \"metrics\": {\"eval_prove_rate\": 0.61, \"eval_mean_isr\": 0.5063, \"eval_isr_std\": 0.4518, \"eval_median_isr\": 0.5, \"eval_proved_only_isr\": 0.8301, \"component_count_mean\": 4.03, \"component_count_2_ratio\": 0, \"tautological_collapse\": false, \"isr_0_ratio\": 0.39, \"isr_1_ratio\": 0.656, \"proved_single_premise_ratio\": 1, \"h7_rate_calibrated\": 0.967, \"h7_definition\": \"single_premise AND premise==conclusion (normalized)\", \"hacking_mode\": \"conclusion_duplication_isr_inflation\", \"conclusion_embedding\": true, \"by_answer_type\": {\"false\": {\"n\": 25, \"proved\": 18, \"PR\": 0.72, \"ISR\": 0.6}, \"unknown\": {\"n\": 41, \"proved\": 22, \"PR\": 0.537, \"ISR\": 0.442}, \"true\": {\"n\": 34, \"proved\": 21, \"PR\": 0.618, \"ISR\": 0.515}}, \"train_total_steps\": 500, \"train_duration_min\": 53, \"train_loss\": 0.012}, \"conclusion\": \"negative\", \"notes\": \"NEGATIVE: conclusion duplication hacking 确认。100% proved 样本仅 1 premise，97% premise=conclusion（重言式 P→P）。ISR=0.506 是 artifact（唯一 premise 必然 necessary）。与 s44 相同失败模式。3-seed 中 s42 唯一可能 genuine（待验证），s43/s44 均 collapse。β=0.1 additive bonus 多 seed 可靠性不足。\"}, \"plan012-hacking-taxonomy\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T09:06:38.613Z\", \"updated_at\": \"2026-05-14T09:07:42.314Z\", \"conclusion\": \"success\", \"hypothesis\": \"ISR β=0.1 vs Random β=0.1 hacking taxonomy 对比：ISR reward 能否减少 hacking 模式比例、增加 genuine proof 比例？5 种 hacking 分类（conclusion embedding, repetition collapse, tautological collapse, complexity-without-utility, premise padding）。\", \"metrics\": {\"isr_b01_genuine_rate\": 0.259, \"random_b01_genuine_rate\": 0.177, \"genuine_rate_delta_pp\": 8.2, \"isr_b01_conclusion_embedding_rate\": 0.728, \"random_b01_conclusion_embedding_rate\": 0.785, \"isr_b01_genuine_mean_isr\": 0.6723, \"random_b01_genuine_mean_isr\": 0.3427, \"isr_b01_complexity_wo_utility_rate\": 0, \"random_b01_complexity_wo_utility_rate\": 0.038, \"isr_b01_hacking_rate\": 0.741, \"random_b01_hacking_rate\": 0.823}, \"notes\": \"D037/D038 完成。Conclusion embedding 是主导 hacking 模式（ISR 72.8% vs Random 78.5%）。ISR β=0.1 genuine proof +8.2pp (25.9% vs 17.7%)，genuine ISR 质量 0.67 vs 0.34。ISR 消除 complexity-without-utility hacking。LLM-as-judge 跳过（D038），记入 Discussion/Future Work。Artifact: art_20260514_bf31aa。\"}, \"plan018-additive-random-b01-s42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T06:55:48.888Z\", \"updated_at\": \"2026-05-14T08:32:44.808Z\", \"hypothesis\": \"β=0.1 random control: r = r_exec·(1+0.1·random[0,1]). 与 plan002-b01 (additive ISR β=0.1, PR=0.81, ISR=0.337) 同 β 对照。如果 ISR β=0.1 >> random β=0.1 → ISR 信号在低剂量下有结构价值; 如果 ISR ≈ random → ISR 信号在低剂量下也仅是 variance regularization。D031 紧急实验。\", \"parent\": \"plan002-additive-b01-s42\", \"conclusion\": \"negative\", \"metrics\": {\"eval_prove_rate\": 0.79, \"eval_mean_isr\": 0.1038, \"eval_isr_std\": 0.1369, \"eval_median_isr\": 0.0357, \"eval_proved_only_isr\": 0.1314, \"eval_n_proved\": 79, \"eval_n_problems\": 100, \"eval_component_count_mean\": 8.46, \"eval_component_count_median\": 8, \"eval_component_count_2_ratio\": 0, \"eval_isr_1_ratio\": 0, \"eval_isr_0_ratio\": 0.367, \"eval_isr_gt0_ratio\": 0.633, \"eval_by_type_false_pr\": 0.8, \"eval_by_type_false_isr\": 0.1318, \"eval_by_type_unknown_pr\": 0.7317, \"eval_by_type_unknown_isr\": 0.0944, \"eval_by_type_true_pr\": 0.8529, \"eval_by_type_true_isr\": 0.0945, \"tautological_collapse\": false, \"train_total_steps\": 500, \"train_duration_min\": 70.5, \"train_last100_pr\": 0.805, \"train_last100_isr\": 0.1432, \"train_loss\": 0.005}, \"notes\": \"Random control β=0.1 vs ISR β=0.1 (plan002-b01) 对照。conclusion=negative: random control的ISR远低于ISR-guided。\\n\\n对比 plan002-b01 (ISR β=0.1):\\n- PR: 0.79 vs 0.81 (≈持平, Δ=0.02)\\n- Mean ISR: 0.104 vs 0.337 (ISR 3.2x higher)\\n- Proved-only ISR: 0.131 vs 0.415 (ISR 3.2x higher)\\n- Median ISR: 0.036 vs plan002未记录\\n- Component count: 8.46 vs 5.58 (random组更多冗余)\\n- ISR=0占比(proved): 36.7% (random组大量proof无结构)\\n- Tautological collapse: 无 (component_2_ratio=0)\\n\\n关键发现: PR几乎相同说明β=0.1 random噪声不影响证明能力。但ISR差3.2倍，证明ISR reward提供genuine structural guidance而非仅variance regularization。这强力支持Claim 2: ISR信号在低剂量下有结构价值。\\n\\nEval output: /root/autodl-tmp/outputs/plan018_additive_random_b01_s42/eval_results.json\"}, \"plan005-sta-low-s42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T22:20:47.812Z\", \"updated_at\": \"2026-05-14T06:31:05.119Z\", \"conclusion\": \"negative\", \"metrics\": {\"total_steps\": 500, \"duration_min\": 71, \"parse_rate\": 1, \"overall_prove_rate\": 0.5657, \"overall_isr\": 0.1682, \"last50_prove_rate\": 0.77, \"last50_isr\": 0.2559, \"last100_prove_rate\": 0.7725, \"last100_isr\": 0.2299, \"last100_loss\": 0.022752, \"overall_loss\": 0.017296, \"last100_isr_pr_ratio\": 0.298, \"last100_isr_lt_pr_count\": \"99/100\", \"first_rolling10_pr_ge_0.8\": 178, \"first_rolling10_pr_ge_0.9\": 439, \"max_rolling10_pr\": 0.9375, \"max_rolling10_isr\": 0.3282, \"windowed\": {\"1-50\": {\"pr\": 0.1775, \"isr\": 0.0906}, \"51-100\": {\"pr\": 0.1775, \"isr\": 0.0835}, \"101-200\": {\"pr\": 0.5062, \"isr\": 0.1463}, \"201-300\": {\"pr\": 0.6713, \"isr\": 0.1791}, \"301-400\": {\"pr\": 0.7013, \"isr\": 0.1984}, \"401-500\": {\"pr\": 0.7725, \"isr\": 0.2299}}}, \"notes\": \"conclusion=negative 基于 prove_rate 下降（last100 0.7725 vs exec-only 0.865）。但结构性发现：ISR/PR ratio=0.298，99/100 步 ISR &lt; PR，说明 STA=0.1 维持了 ISR 与 PR 的持续分离——模型未通过 hacking prove_rate 绕过 STA penalty。此观察支持论文 \\\"STA 抑制 reward hacking\\\" claim。windowed ISR/PR: 1-50 (0.51), 51-100 (0.47), 101-200 (0.29), 201-300 (0.27), 301-400 (0.28), 401-500 (0.30) — 分离在100步后稳定。D030 决策：checkpoint 已删除，不重训。论文用训练曲线 windowed ISR/PR 数据作为证据。\"}, \"plan001-exec-only-s43-r4\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T01:40:37.808Z\", \"updated_at\": \"2026-05-14T06:30:57.539Z\", \"metrics\": {\"eval_sampling_prove_rate\": 0.14, \"eval_sampling_mean_isr\": 0, \"eval_sampling_n_proved\": 14, \"eval_sampling_temperature\": 0.7, \"eval_sampling_method\": \"do_sample=True, temperature=0.7\", \"eval_sampling_by_answer\": {\"true\": {\"count\": 34, \"proved\": 6, \"prove_rate\": 0.176}, \"false\": {\"count\": 25, \"proved\": 2, \"prove_rate\": 0.08}, \"unknown\": {\"count\": 41, \"proved\": 6, \"prove_rate\": 0.146}}}, \"conclusion\": \"negative\", \"notes\": \"训练 PR(last100)=0.883 但 eval PR=14% (sampling, T=0.7), ISR=0。87% 样本 hit max_new_tokens 生成不可解析长输出。与 s42 (eval PR=93%) 形成极端跨 seed 不稳定。exec-only reward landscape 存在极大方差。⚠️ 评估方法：sampling eval (T=0.7)，其他组用 eval_sta.py full STA。D029 决策：不重训，论文标注方法差异。PR=14% 是 failure case，eval 方法不影响结论。\"}, \"plan017-additive-random-s42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T03:11:14.694Z\", \"updated_at\": \"2026-05-14T05:33:25.603Z\", \"hypothesis\": \"Additive random control: r = r_exec·(1+0.3·random). 隔离 ISR structural signal vs variance regularization. 若 ISR > random > exec-only → signal+regularization 均贡献; 若 ISR > random ≈ exec-only → ISR signal 是关键; 若 ISR ≈ random → ISR 无结构价值。\", \"parent\": \"plan013-random-reward-s42-r4\", \"conclusion\": \"negative\", \"notes\": \"Eval结果: PR=0.48, mean_ISR=0.0453, proved_only_ISR=0.0943, mean_components=9.56 (3+比例100%, 无tautological collapse). 但33%已证明样本ISR=0 (n_necessary=0, conclusion trivially provable). 与plan013的不同failure mode: additive random防止了2-component坍缩, 但模型转向生成复杂但无用的formalization (多premises但conclusion不依赖任何premise). Variance regularization不足以产生genuine proofs.\", \"metrics\": {\"eval_prove_rate\": 0.48, \"eval_mean_isr\": 0.0453, \"eval_isr_std\": 0.0759, \"eval_median_isr\": 0, \"eval_max_isr\": 0.2857, \"eval_proved_only_isr\": 0.0943, \"eval_n_proved\": 48, \"eval_n_problems\": 100, \"eval_method\": \"eval_sta.py full STA\", \"eval_data\": \"proofwriter_fol_100.jsonl\", \"eval_component_count_mean\": 9.6, \"eval_component_count_2_ratio\": 0, \"eval_isr_pr_ratio\": 0.0943, \"eval_elapsed_s\": 542.3, \"eval_by_type_false_pr\": 0.32, \"eval_by_type_false_isr\": 0.0254, \"eval_by_type_unknown_pr\": 0.51, \"eval_by_type_unknown_isr\": 0.0518, \"eval_by_type_true_pr\": 0.56, \"eval_by_type_true_isr\": 0.052, \"tautological_collapse\": false}}, \"plan014-downstream-nli-s42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T03:43:37.925Z\", \"updated_at\": \"2026-05-14T04:29:48.645Z\", \"hypothesis\": \"Downstream NLI validation: 高ISR formalization 应在独立推理任务上表现更好(entailment accuracy)，Spearman ρ(ISR, accuracy) > 0.1 验证 ISR 作为 quality proxy 的实用价值。同时用 Z3 cross-solver agreement 验证 formalization 鲁棒性。\", \"notes\": \"Negative: ISR 作为 downstream NLI quality proxy 无效。Spearman ρ(ISR, correct)=-0.049 (p=0.187)，Best-of-N ISR 仅 +0.9pp over random (不显著)。主因：模型严重 true-bias (false accuracy=0%)，NLI accuracy 天花板仅 34.1%，ISR 无区分空间。ISR bucket 层面有弱单调趋势 (high=75% > mid=37.7% > low=32.7%) 但 high bucket 仅 12 样本。quartile 分析非单调。\", \"conclusion\": \"negative\", \"metrics\": {\"overall_accuracy\": 0.341, \"proved_rate\": 0.915, \"proved_count\": 732, \"total_generations\": 800, \"parse_errors\": 0, \"accuracy_by_label\": {\"true\": 0.912, \"false\": 0, \"unknown\": 0.076}, \"spearman_rho\": -0.049, \"spearman_p\": 0.187, \"mann_whitney_U\": 17202, \"mann_whitney_p\": 0.288, \"bon_isr_accuracy\": 0.35, \"bon_random_accuracy\": 0.341, \"bon_oracle_accuracy\": 0.44, \"bon_prove_first_accuracy\": 0.35, \"isr_bucket_high_acc\": 0.75, \"isr_bucket_mid_acc\": 0.377, \"isr_bucket_low_acc\": 0.327, \"runtime_inference_s\": 408.8, \"runtime_eval_s\": 13.6}}, \"plan002-additive-b03-s42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T02:24:47.843Z\", \"updated_at\": \"2026-05-14T04:27:38.822Z\", \"metrics\": {\"total_steps\": 500, \"duration_min\": 56.7, \"overall_prove_rate\": 0.34025, \"overall_isr\": 0.11527, \"first20_prove_rate\": 0.15625, \"last50_prove_rate\": 0.555, \"last100_prove_rate\": 0.5525, \"mean_loss\": 0.008914, \"last100_loss\": 0.014469, \"parse_rate\": 1, \"w1_50_prove_rate\": 0.13, \"w51_100_prove_rate\": 0.095, \"w101_200_prove_rate\": 0.185, \"w201_300_prove_rate\": 0.375, \"w301_400_prove_rate\": 0.47625, \"w401_500_prove_rate\": 0.5525, \"steps_ge_085\": 52, \"first_step_ge_085\": 46, \"final_prove_rate\": 1, \"final_isr_mean\": 0.3089, \"final_reward_mean\": 1.0927}, \"notes\": \"ISR 为 binary 近似 (_fast_fn)，不可用于论文跨 run 对比，需 eval_sta.py 统一评估真实 ISR。prove_rate 轨迹 0.13→0.095→0.185→0.375→0.476→0.553，呈稳步上升趋势，尚未完全饱和（仅 52/500 步 ≥0.85），与 plan001/plan013 的强饱和模式不同。\", \"conclusion\": \"negative\"}, \"plan013-random-reward-s42-r4\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T01:40:35.587Z\", \"updated_at\": \"2026-05-14T03:45:53.344Z\", \"conclusion\": \"success\", \"metrics\": {\"eval_prove_rate\": 1, \"eval_mean_isr\": 0.535, \"eval_isr_std\": 0.1282, \"eval_proved_only_isr\": 0.535, \"eval_median_isr\": 0.5, \"eval_n_proved\": 100, \"eval_n_problems\": 100, \"eval_method\": \"eval_sta.py full STA\", \"eval_data\": \"proofwriter_fol_100.jsonl\", \"eval_note\": \"DEGENERATE: model generates trivial 2-component proofs (premise=conclusion, conclusion=conclusion), ISR=0.5 is artifact of trivial proof structure\"}, \"notes\": \"⚠️ 训练日志 ISR 为 binary approximation (_fast_fn)，ISR≈prove_rate，不含结构信息。真实 ISR 需通过 eval_sta.py (full STA) 在 checkpoint-500 上重新评估。final_mean_isr=0.6705 实为 binary 近似值，禁止用于论文或跨实验 ISR 对比。\"}, \"plan001-exec-only-s43-r3\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T01:02:31.830Z\", \"updated_at\": \"2026-05-14T01:41:28.427Z\", \"conclusion\": \"failed\"}, \"plan013-random-reward-s42-r3\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T01:02:30.063Z\", \"updated_at\": \"2026-05-14T01:41:28.122Z\", \"conclusion\": \"failed\"}, \"plan001-exec-only-s43-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T00:22:12.292Z\", \"updated_at\": \"2026-05-14T01:01:56.416Z\", \"conclusion\": \"failed\"}, \"plan013-random-reward-s42-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T00:22:10.140Z\", \"updated_at\": \"2026-05-14T01:01:55.694Z\", \"conclusion\": \"failed\"}, \"plan013-random-reward-s42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T23:56:44.062Z\", \"updated_at\": \"2026-05-14T00:21:05.430Z\", \"conclusion\": \"failed\"}, \"plan001-exec-only-s43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T23:55:08.635Z\", \"updated_at\": \"2026-05-14T00:21:04.003Z\", \"conclusion\": \"failed\"}, \"plan001-exec-only-s42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T22:19:41.568Z\", \"updated_at\": \"2026-05-13T23:03:42.892Z\", \"conclusion\": \"failed\"}, \"plan003-eval-exec-only-r5\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T22:21:48.691Z\", \"updated_at\": \"2026-05-13T23:03:19.945Z\", \"metrics\": {\"prove_rate\": 0.32, \"mean_isr\": 0.2055, \"isr_std\": 0.3194, \"proved_only_isr\": 0.6423, \"isr_by_type\": {\"true\": 0.3598, \"false\": 0.1723, \"unknown\": 0.0979}, \"total_samples\": 100, \"proved_count\": 32, \"runtime_s\": 251.7}, \"conclusion\": \"success\"}, \"plan001-exec-only-s42-r3\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T22:42:40.242Z\", \"updated_at\": \"2026-05-13T23:03:11.395Z\", \"conclusion\": \"failed\"}, \"sta-phase1-exec-sta-r5\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T20:54:31.353Z\", \"updated_at\": \"2026-05-13T22:20:41.274Z\", \"metrics\": {\"parse_rate\": 1, \"prove_rate\": 0.1, \"mean_isr\": 0.04347, \"last20_prove_rate\": 0.15, \"last20_isr_mean\": 0.04956, \"first20_prove_rate\": 0.08125, \"first20_isr_mean\": 0.05182, \"overall_reward_mean\": 0.07174, \"last20_reward_mean\": 0.09978, \"training_steps\": 100, \"training_minutes\": 16.9, \"step_time_s\": 10.13, \"isr_pr_ratio_overall\": 0.43, \"isr_pr_ratio_last20\": 0.33, \"K\": 8}, \"conclusion\": \"negative\"}, \"sta-phase1-exec-only-r5\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T20:54:27.505Z\", \"updated_at\": \"2026-05-13T21:53:04.486Z\", \"metrics\": {\"parse_rate\": 1, \"prove_rate\": 0.15125, \"mean_isr\": 0.1475, \"last20_prove_rate\": 0.2, \"last20_isr_mean\": 0.2, \"first20_prove_rate\": 0.11875, \"first20_isr_mean\": 0.11875, \"overall_reward_mean\": 0.15125, \"last20_reward_mean\": 0.2, \"training_steps\": 100, \"training_minutes\": 15.7, \"step_time_s\": 9.44, \"isr_pr_ratio_last20\": 1, \"K\": 8}, \"conclusion\": \"success\"}, \"sta-phase1-exec-sta-r4\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T20:28:22.778Z\", \"updated_at\": \"2026-05-13T20:52:58.761Z\", \"metrics\": {\"parse_rate\": 1, \"prove_rate\": 0.1575, \"mean_isr\": 0.1525, \"last20_prove_rate\": 0.2125, \"last20_isr_mean\": 0.2125, \"first20_reward_mean\": 0.119, \"training_steps\": 100, \"training_minutes\": 15}, \"conclusion\": \"negative\", \"notes\": \"Phase 1 r4 完成但无差异。fast_isr_fol 二值信号(0/1)对 proved samples 几乎全部 ISR=1，exec+STA reward ≈ exec-only reward。连续 ISR 才能产生有意义的差异信号。→ r5 改用 full sta_reward (continuous ISR 0.0-1.0) + K=8\"}, \"sta-phase1-exec-only-r4\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T20:28:18.040Z\", \"updated_at\": \"2026-05-13T20:52:56.416Z\", \"metrics\": {\"parse_rate\": 1, \"prove_rate\": 0.15125, \"mean_isr\": 0.1475, \"last20_prove_rate\": 0.2, \"last20_isr_mean\": 0.2, \"first20_reward_mean\": 0.119, \"training_steps\": 100, \"training_minutes\": 15}, \"conclusion\": \"negative\", \"notes\": \"Phase 1 r4 完成但无差异。fast_isr_fol 二值信号(0/1)对 proved samples 几乎全部 ISR=1，导致 exec+STA ≈ exec-only。prove_rate 从 baseline 12% → last20 20%（微弱提升）。K=4 导致大量全零 reward batch。→ r5 改用 full STA + K=8\"}, \"sta-phase1-exec-only-r3\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T20:15:04.067Z\", \"updated_at\": \"2026-05-13T20:23:15.460Z\", \"conclusion\": \"failed\", \"notes\": \"EXIT_CODE=137 (OOM/SIGKILL) after ~276s. 同 sta-phase1-exec-sta-r3 一起诊断中\"}, \"sta-phase1-exec-sta-r3\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T20:15:08.133Z\", \"updated_at\": \"2026-05-13T20:23:14.516Z\", \"conclusion\": \"failed\", \"notes\": \"EXIT_CODE=137 (OOM/SIGKILL) after ~278s. 诊断中: worker_diagnose_sta-phase1-r3-oom_20260513T202300\"}, \"sta-phase1-exec-sta-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T19:55:08.640Z\", \"updated_at\": \"2026-05-13T19:55:41.544Z\", \"conclusion\": \"failed\"}, \"sta-phase1-exec-only-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T19:55:04.711Z\", \"updated_at\": \"2026-05-13T19:55:37.426Z\", \"conclusion\": \"failed\"}, \"sta-phase1-exec-sta\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T18:26:53.258Z\", \"updated_at\": \"2026-05-13T19:33:03.905Z\", \"conclusion\": \"failed\"}, \"sta-phase1-exec-only\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T18:26:46.351Z\", \"updated_at\": \"2026-05-13T19:33:01.169Z\", \"conclusion\": \"failed\"}, \"sta-gt-isr-baseline\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T18:11:13.283Z\", \"updated_at\": \"2026-05-13T18:12:44.147Z\", \"conclusion\": \"success\", \"metrics\": {\"gt_prove_rate\": 0.18, \"gt_mean_isr\": 0.5588, \"gt_isr_std\": 0.2582, \"gt_isr_median\": 0.6125, \"solver_execution_rate\": 1, \"true_prove_rate\": 0.5, \"true_mean_isr\": 0.5833}}, \"sta-phase0-baseline\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T17:51:48.853Z\", \"updated_at\": \"2026-05-13T18:10:40.982Z\", \"metrics\": {\"mean_isr\": 0.0641, \"isr_std\": 0.1983, \"median_isr\": 0, \"isr_range\": [0, 0.889], \"prove_rate\": 0.12, \"proved_count\": 12, \"total_samples\": 100, \"xor_affected_samples\": 34, \"effective_prove_rate_no_xor\": 0.182, \"avg_time_per_sample_s\": 3.4, \"total_runtime_s\": 336, \"isr_by_answer\": {\"true\": {\"n\": 34, \"proved\": 9, \"prove_rate\": 0.265, \"mean_isr\": 0.1345}, \"false\": {\"n\": 25, \"proved\": 1, \"prove_rate\": 0.04, \"mean_isr\": 0.024}, \"unknown\": {\"n\": 41, \"proved\": 2, \"prove_rate\": 0.049, \"mean_isr\": 0.0302}}}, \"conclusion\": \"success\"}}, \"count\": 50, \"total\": 50, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2333}}"
    }
  },
  "sourceToolAssistantUUID": "48c103c4-8082-4370-b97f-8e4c3bab0c06",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "24e67ff1-1ea3-4bcf-a9e3-703eaa6cb36e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 24_

```json
{
  "type": "last-prompt",
  "leafUuid": "091ce49b-b5b9-4fb4-b03b-c24ed090fb3c",
  "sessionId": "24e67ff1-1ea3-4bcf-a9e3-703eaa6cb36e"
}
```

---

### Runtime record

_source line 25_

```json
{
  "type": "ai-title",
  "aiTitle": "Audit paper figures against experiment registry",
  "sessionId": "24e67ff1-1ea3-4bcf-a9e3-703eaa6cb36e"
}
```

---

### Assistant

_source line 26 · 2026-05-14T21:44:53.780Z_

<details><summary>Logged reasoning block</summary>

```text

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "091ce49b-b5b9-4fb4-b03b-c24ed090fb3c",
  "isSidechain": false,
  "requestId": "req_011Cb3C97mJKarHWT2YNmMDx",
  "type": "assistant",
  "uuid": "22eb9283-b64b-4b54-b93f-bb7423897bd4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "24e67ff1-1ea3-4bcf-a9e3-703eaa6cb36e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01NSTGs7hnYxHvi5iRWG7myC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 24517,
      "cache_read_input_tokens": 45954,
      "output_tokens": 251,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 24517,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 251,
          "cache_read_input_tokens": 45954,
          "cache_creation_input_tokens": 24517,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 24517
          },
          "type": "message"
        }
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

_source line 27 · 2026-05-14T21:44:55.150Z_

<details open><summary>🔧 Tool call — Read · `toolu_013rMJkQTFGkHTc2EEeoYYqq`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "22eb9283-b64b-4b54-b93f-bb7423897bd4",
  "isSidechain": false,
  "requestId": "req_011Cb3C97mJKarHWT2YNmMDx",
  "type": "assistant",
  "uuid": "ec444f5e-0912-4d55-90c9-c12f1d2681c7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "24e67ff1-1ea3-4bcf-a9e3-703eaa6cb36e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01NSTGs7hnYxHvi5iRWG7myC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 24517,
      "cache_read_input_tokens": 45954,
      "output_tokens": 251,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 24517,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 251,
          "cache_read_input_tokens": 45954,
          "cache_creation_input_tokens": 24517,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 24517
          },
          "type": "message"
        }
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

_source line 28 · 2026-05-14T21:44:55.166Z_

<details><summary>↩ Tool result · `toolu_013rMJkQTFGkHTc2EEeoYYqq`</summary>

```text
1	\begin{abstract}
2	GRPO-trained neurosymbolic formalizers achieve high prove rates---93\% on FOLIO---yet 87\% of proved outputs embed the conclusion verbatim among the premises, a degenerate shortcut invisible to execution-based evaluation. We introduce \emph{Solver Trace Ablation} (STA), a solver-agnostic diagnostic that applies leave-one-out component necessity testing to solver inputs. The fraction of components whose removal causes proof failure yields the \emph{Intensional Structural Reward} (ISR): ISR$=$1 indicates maximal tightness; ISR$=$0 indicates complete redundancy.
3	
4	ISR exposes a collapse trajectory hidden from prove rate: over 100 to 1000 GRPO training steps (Qwen3-4B), ISR falls from 0.642 to 0.003---a 99.5\% degradation---while prove rate rises from 32\% to 96\%. An SFT baseline achieves 92.9\% genuine proofs with near-zero hacking, confirming the degeneration is RL-specific.
5	
6	Can ISR serve as a training signal? Incorporating ISR into the reward at $\beta{=}0.1$ induces \emph{meta-level Goodhart's Law}: 64.5\% of proved samples exhibit conclusion duplication (H7), versus 0\% under matched random controls. The sole apparent ISR improvement reduces to $1.06\times$ after controlling for a premise-count confound. At $\beta{=}0.3$, prove rate collapses to 18\% versus 48\% for random control.
7	
8	Cross-logic transfer to Prolog/SWI-Prolog yields a stronger result: ISR-as-reward produces universal Goodhart---3/3 seeds gaming via distinct mechanisms, 0\% genuine proofs.
9	
10	Across 6 reward conditions, 2 logic types (FOL/Prover9, Prolog/SWI-Prolog), and 3 seeds, we catalog 7 distinct reward hacking modes---including query-as-fact gaming that bypasses text-match classifiers---documenting ISR's fundamental asymmetry: reliable as a diagnostic, unreliable as an optimization target.
11	\end{abstract}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ec444f5e-0912-4d55-90c9-c12f1d2681c7",
  "isSidechain": false,
  "promptId": "c33bf5b5-c338-4f2f-97b8-e3e6d5f92819",
  "type": "user",
  "uuid": "fbace300-f4aa-4295-9772-b867049a11ae",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/abstract.tex",
      "content": "\\begin{abstract}\nGRPO-trained neurosymbolic formalizers achieve high prove rates---93\\% on FOLIO---yet 87\\% of proved outputs embed the conclusion verbatim among the premises, a degenerate shortcut invisible to execution-based evaluation. We introduce \\emph{Solver Trace Ablation} (STA), a solver-agnostic diagnostic that applies leave-one-out component necessity testing to solver inputs. The fraction of components whose removal causes proof failure yields the \\emph{Intensional Structural Reward} (ISR): ISR$=$1 indicates maximal tightness; ISR$=$0 indicates complete redundancy.\n\nISR exposes a collapse trajectory hidden from prove rate: over 100 to 1000 GRPO training steps (Qwen3-4B), ISR falls from 0.642 to 0.003---a 99.5\\% degradation---while prove rate rises from 32\\% to 96\\%. An SFT baseline achieves 92.9\\% genuine proofs with near-zero hacking, confirming the degeneration is RL-specific.\n\nCan ISR serve as a training signal? Incorporating ISR into the reward at $\\beta{=}0.1$ induces \\emph{meta-level Goodhart's Law}: 64.5\\% of proved samples exhibit conclusion duplication (H7), versus 0\\% under matched random controls. The sole apparent ISR improvement reduces to $1.06\\times$ after controlling for a premise-count confound. At $\\beta{=}0.3$, prove rate collapses to 18\\% versus 48\\% for random control.\n\nCross-logic transfer to Prolog/SWI-Prolog yields a stronger result: ISR-as-reward produces universal Goodhart---3/3 seeds gaming via distinct mechanisms, 0\\% genuine proofs.\n\nAcross 6 reward conditions, 2 logic types (FOL/Prover9, Prolog/SWI-Prolog), and 3 seeds, we catalog 7 distinct reward hacking modes---including query-as-fact gaming that bypasses text-match classifiers---documenting ISR's fundamental asymmetry: reliable as a diagnostic, unreliable as an optimization target.\n\\end{abstract}",
      "numLines": 11,
      "startLine": 1,
      "totalLines": 11
    }
  },
  "sourceToolAssistantUUID": "ec444f5e-0912-4d55-90c9-c12f1d2681c7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "24e67ff1-1ea3-4bcf-a9e3-703eaa6cb36e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-14T21:44:55.704Z_

<details><summary>↩ Tool result · `toolu_01KzHYDe1AZH4TvNGhDzEsvS`</summary>

```text
1	\section{Introduction}
2	\label{sec:introduction}
3	
4	A GRPO-trained formalizer achieves a 93\% prove rate on first-order logic problems---yet 87\% of its proved outputs embed the conclusion verbatim among the premises.
5	The solver succeeds not because the model has learned to reason, but because the formalization trivially entails any conclusion that already appears as a premise.
6	This structural shortcut is invisible to execution-based evaluation: prove rate registers success regardless of whether the proof reflects genuine multi-step derivation or degenerate circular embedding.
7	
8	Prove rate---the dominant evaluation metric for neurosymbolic formalizers---conflates faithful reasoning with degenerate shortcuts, a gap especially consequential under reinforcement learning, where the optimizer exploits any shortcut the reward fails to penalize~\cite{skalse-reward-hacking, reward-hacking-survey}.
9	Recent work applies GRPO~\cite{deepseekmath} to train LLMs that generate solver-verified formal programs~\cite{mellgren-prolog-grpo, logic-rl} using binary execution feedback as reward; this drives rapid PR gains but gives no gradient on structural quality.
10	Process reward models~\cite{lightman-verify-step} offer step-level supervision but require expensive annotations and do not transfer to arbitrary solver-backed settings.
11	No existing method provides an annotation-free, solver-agnostic diagnostic for structural integrity in neurosymbolic outputs (see \S\ref{sec:related-work} for full context).
12	
13	We address this gap with \emph{Solver Trace Ablation} (STA), a diagnostic protocol inspired by mutation testing~\cite{demillo1978} that applies component necessity testing---leave-one-out (LOO) ablation on solver inputs---to quantify structural integrity (\autoref{fig:sta-overview}).
14	For each proved formalization, STA removes each component individually and re-runs the solver; the fraction of components whose removal causes proof failure yields the \emph{Intensional Structural Reward} (ISR).
15	ISR${=}$1 indicates a maximally tight formalization where every component is individually necessary; ISR${=}$0 indicates complete structural redundancy.
16	Applied as a post-hoc diagnostic on a GRPO formalizer trained with FOLIO~\cite{folio} data, ISR reveals a structural collapse trajectory entirely invisible to prove rate: ISR falls from 0.642 at 100 steps to 0.132 at 500 steps to 0.003 at 1000 steps---a 99.5\% degradation---while prove rate simultaneously rises from 32\% to 96\%.
17	Three random seeds diverge radically (PR $\sigma{=}47$\,pp), each converging to a qualitatively different degeneration mode: conclusion embedding, repetition collapse, and tautological collapse.
18	A supervised fine-tuning (SFT) baseline achieves 92.9\% genuine proofs with near-zero hacking, confirming that the structural collapse is a consequence of RL reward optimization, not model capacity or data limitations.
19	
20	A natural question is whether ISR can serve as a training signal. The answer is negative: when ISR is added to the reward ($r = r_{\text{exec}} \cdot (1 + \beta \cdot \text{ISR})$), the model games the diagnostic itself---\emph{meta-level Goodhart's Law}~\cite{manheim-goodhart-taxonomy, karwowski-goodhart-rl}.
21	At $\beta{=}0.1$, 64.5\% of proved samples exhibit ISR-specific conclusion duplication (H7) vs.\ 0\% under matched random reward, and the sole apparent improvement reduces to 1.06$\times$ after controlling for a premise-count confound (\S\ref{sec:goodhart}); at $\beta{=}0.3$ PR collapses to 18\% vs.\ 48\% for random control~\cite{gao-reward-overoptimization}.
22	The effect transfers and intensifies in Prolog/SWI-Prolog: all three seeds gaming, 0\% genuine---universal Goodhart, each via a distinct mechanism.
23	
24	Across 6 reward conditions, 3 seeds, 2 logic types, and up to 1000 training steps, we make four contributions:
25	
26	\begin{enumerate}[nosep,leftmargin=*]
27	\item We introduce STA and establish ISR as a diagnostic for hacking invisible to PR, with a complete collapse trajectory ($0.642{\to}0.003$) over 1000 GRPO steps; SFT (92.9\% genuine) confirms hacking is RL-specific.
28	\item We characterize meta-level Goodhart in neurosymbolic RL and identify the premise-count confound behind the only apparent ISR gain (1.06$\times$).
29	\item We show cross-logic transfer to Prolog/SWI-Prolog with universal Goodhart (3/3 seeds, 0\% genuine), indicating simpler formal semantics enable more complete exploitation.
30	\item We catalog 7 hacking modes including query-as-fact gaming that bypasses text-match classifiers, motivating functional cross-validation of diagnostics.
31	\end{enumerate}
32	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "20482a1e-204b-4210-a0f1-e004403a7303",
  "isSidechain": false,
  "promptId": "c33bf5b5-c338-4f2f-97b8-e3e6d5f92819",
  "type": "user",
  "uuid": "c519a78d-2138-4095-935a-a7b22fd529a8",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/introduction.tex",
      "content": "\\section{Introduction}\n\\label{sec:introduction}\n\nA GRPO-trained formalizer achieves a 93\\% prove rate on first-order logic problems---yet 87\\% of its proved outputs embed the conclusion verbatim among the premises.\nThe solver succeeds not because the model has learned to reason, but because the formalization trivially entails any conclusion that already appears as a premise.\nThis structural shortcut is invisible to execution-based evaluation: prove rate registers success regardless of whether the proof reflects genuine multi-step derivation or degenerate circular embedding.\n\nProve rate---the dominant evaluation metric for neurosymbolic formalizers---conflates faithful reasoning with degenerate shortcuts, a gap especially consequential under reinforcement learning, where the optimizer exploits any shortcut the reward fails to penalize~\\cite{skalse-reward-hacking, reward-hacking-survey}.\nRecent work applies GRPO~\\cite{deepseekmath} to train LLMs that generate solver-verified formal programs~\\cite{mellgren-prolog-grpo, logic-rl} using binary execution feedback as reward; this drives rapid PR gains but gives no gradient on structural quality.\nProcess reward models~\\cite{lightman-verify-step} offer step-level supervision but require expensive annotations and do not transfer to arbitrary solver-backed settings.\nNo existing method provides an annotation-free, solver-agnostic diagnostic for structural integrity in neurosymbolic outputs (see \\S\\ref{sec:related-work} for full context).\n\nWe address this gap with \\emph{Solver Trace Ablation} (STA), a diagnostic protocol inspired by mutation testing~\\cite{demillo1978} that applies component necessity testing---leave-one-out (LOO) ablation on solver inputs---to quantify structural integrity (\\autoref{fig:sta-overview}).\nFor each proved formalization, STA removes each component individually and re-runs the solver; the fraction of components whose removal causes proof failure yields the \\emph{Intensional Structural Reward} (ISR).\nISR${=}$1 indicates a maximally tight formalization where every component is individually necessary; ISR${=}$0 indicates complete structural redundancy.\nApplied as a post-hoc diagnostic on a GRPO formalizer trained with FOLIO~\\cite{folio} data, ISR reveals a structural collapse trajectory entirely invisible to prove rate: ISR falls from 0.642 at 100 steps to 0.132 at 500 steps to 0.003 at 1000 steps---a 99.5\\% degradation---while prove rate simultaneously rises from 32\\% to 96\\%.\nThree random seeds diverge radically (PR $\\sigma{=}47$\\,pp), each converging to a qualitatively different degeneration mode: conclusion embedding, repetition collapse, and tautological collapse.\nA supervised fine-tuning (SFT) baseline achieves 92.9\\% genuine proofs with near-zero hacking, confirming that the structural collapse is a consequence of RL reward optimization, not model capacity or data limitations.\n\nA natural question is whether ISR can serve as a training signal. The answer is negative: when ISR is added to the reward ($r = r_{\\text{exec}} \\cdot (1 + \\beta \\cdot \\text{ISR})$), the model games the diagnostic itself---\\emph{meta-level Goodhart's Law}~\\cite{manheim-goodhart-taxonomy, karwowski-goodhart-rl}.\nAt $\\beta{=}0.1$, 64.5\\% of proved samples exhibit ISR-specific conclusion duplication (H7) vs.\\ 0\\% under matched random reward, and the sole apparent improvement reduces to 1.06$\\times$ after controlling for a premise-count confound (\\S\\ref{sec:goodhart}); at $\\beta{=}0.3$ PR collapses to 18\\% vs.\\ 48\\% for random control~\\cite{gao-reward-overoptimization}.\nThe effect transfers and intensifies in Prolog/SWI-Prolog: all three seeds gaming, 0\\% genuine---universal Goodhart, each via a distinct mechanism.\n\nAcross 6 reward conditions, 3 seeds, 2 logic types, and up to 1000 training steps, we make four contributions:\n\n\\begin{enumerate}[nosep,leftmargin=*]\n\\item We introduce STA and establish ISR as a diagnostic for hacking invisible to PR, with a complete collapse trajectory ($0.642{\\to}0.003$) over 1000 GRPO steps; SFT (92.9\\% genuine) confirms hacking is RL-specific.\n\\item We characterize meta-level Goodhart in neurosymbolic RL and identify the premise-count confound behind the only apparent ISR gain (1.06$\\times$).\n\\item We show cross-logic transfer to Prolog/SWI-Prolog with universal Goodhart (3/3 seeds, 0\\% genuine), indicating simpler formal semantics enable more complete exploitation.\n\\item We catalog 7 hacking modes including query-as-fact gaming that bypasses text-match classifiers, motivating functional cross-validation of diagnostics.\n\\end{enumerate}\n",
      "numLines": 32,
      "startLine": 1,
      "totalLines": 32
    }
  },
  "sourceToolAssistantUUID": "20482a1e-204b-4210-a0f1-e004403a7303",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "24e67ff1-1ea3-4bcf-a9e3-703eaa6cb36e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-14T21:44:55.699Z_

<details open><summary>🔧 Tool call — Read · `toolu_01KzHYDe1AZH4TvNGhDzEsvS`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fbace300-f4aa-4295-9772-b867049a11ae",
  "isSidechain": false,
  "requestId": "req_011Cb3C97mJKarHWT2YNmMDx",
  "type": "assistant",
  "uuid": "20482a1e-204b-4210-a0f1-e004403a7303",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "24e67ff1-1ea3-4bcf-a9e3-703eaa6cb36e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01NSTGs7hnYxHvi5iRWG7myC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 24517,
      "cache_read_input_tokens": 45954,
      "output_tokens": 251,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 24517,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 251,
          "cache_read_input_tokens": 45954,
          "cache_creation_input_tokens": 24517,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 24517
          },
          "type": "message"
        }
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

_source line 31 · 2026-05-14T21:44:59.247Z_

<details open><summary>🔧 Tool call — Read · `toolu_016VcJ9njAKMnwzXvi2s5XkF`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c519a78d-2138-4095-935a-a7b22fd529a8",
  "isSidechain": false,
  "requestId": "req_011Cb3C9TTUJihhgj9SA89EF",
  "type": "assistant",
  "uuid": "3d63d97c-94e0-4e2a-a7e7-b0a2c0b11ca7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "24e67ff1-1ea3-4bcf-a9e3-703eaa6cb36e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01FrVcgtC46VF4xykMSmwnHY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2944,
      "cache_read_input_tokens": 70471,
      "output_tokens": 114,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2944,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 114,
          "cache_read_input_tokens": 70471,
          "cache_creation_input_tokens": 2944,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2944
          },
          "type": "message"
        }
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

_source line 32 · 2026-05-14T21:44:59.262Z_

<details><summary>↩ Tool result · `toolu_016VcJ9njAKMnwzXvi2s5XkF`</summary>

```text
1	\section{Experiments}
2	\label{sec:experiments}
3	
4	We evaluate STA along three axes: as a diagnostic for reward hacking (\S\ref{sec:diagnostic}); as a training reward exhibiting meta-level Goodhart's Law (\S\ref{sec:goodhart}); and as a cross-logic protocol (\S\ref{sec:crosslogic}). We synthesize results into a hacking taxonomy (\S\ref{sec:taxonomy}).
5	
6	\subsection{Setup}
7	\label{sec:setup}
8	
9	We train Qwen3-4B with GRPO~\citep{deepseekmath} using $K{=}8$ rollouts per prompt for 500 steps (default) or 1000 where noted, across seeds $\{42,43,44\}$.
10	Training data is a fixed 500-example subset of FOLIO~\citep{folio} (\texttt{train\_500\_seed42.jsonl}), held constant across all seeds and conditions.
11	We use Prover9 for FOL and SWI-Prolog 8.4.2 for Prolog.
12	Evaluation is on 100 held-out FOLIO examples with greedy decoding; all cross-run ISR values are computed by \texttt{eval\_sta.py} which applies STA uniformly.
13	We report prove rate (PR), proved-only ISR (ISR$^*$, over proved samples only), hacking mode percentages (H7, H1), genuine rate, and mean component count.
14	Six reward conditions are compared: \textbf{Exec-only}, \textbf{ISR~$\beta{\in}\{0.1,0.3\}$}, \textbf{Random~$\beta{\in}\{0.1,0.3\}$}, and \textbf{SFT}.
15	Outputs are classified into H7, H1, and Genuine using text matching cross-validated with functional LOO analysis.
16	Full hyperparameters are in Appendix~\ref{app:setup}.
17	
18	\subsection{ISR as Diagnostic}
19	\label{sec:diagnostic}
20	
21	\begin{figure}[t]
22	\centering
23	\includegraphics[width=0.95\columnwidth]{figures/fig2_isr_collapse.pdf}
24	\caption{ISR collapse under exec-only GRPO (seed~42). PR rises 32\%$\to$96\% while proved-only ISR falls 0.642$\to$0.003 over 1000 steps. By step 1000, 94.8\% of proved samples have ISR${=}0$ and mean component count inflates 6.58$\to$18.55 (contradiction explosion).}
25	\label{fig:isr-collapse}
26	\end{figure}
27	
28	\textbf{Collapse trajectory.}
29	Figure~\ref{fig:isr-collapse} traces ISR and PR over training for exec-only GRPO (seed~42).
30	At 100 steps: PR${=}32$\%, ISR${=}0.642$.
31	By 500 steps: PR${=}93$\% but ISR${=}0.132$---87.1\% of proved samples embed the conclusion among the premises (H1).
32	At 1000 steps: PR${=}96$\% while ISR drops to 0.003 (H1${=}100$\%, mean components 18.55).
33	The ISR trajectory ($0.642{\to}0.132{\to}0.003$) is monotonically decreasing: extended training worsens structural degeneration, invisible to PR.
34	
35	\textbf{Cross-seed instability.}
36	The three exec-only seeds diverge radically: s42 hacks via H1 (PR${=}93$\%, H1${=}87.1$\%); s43 collapses to PR${=}14$\% (ISR${=}0$) via repetition---87\% of outputs hit the max token length; s44 reaches PR${=}98$\% via tautological collapse (H7${=}100$\%, mean components 2.04).
37	Despite PR$\in[14,98]$\%, all three seeds exhibit structural degeneration detectable by ISR.
38	The cross-seed PR $\sigma{=}\pm47$\,pp is itself a finding: aggregate metrics obscure qualitatively different failure modes (per-seed details in Table~\ref{tab:beta01-3seed}).
39	
40	\textbf{SFT baseline.}
41	A supervised baseline achieves PR${=}14$\% with ISR${=}0.571$: 92.9\% (13/14) of proved samples are genuine, only 1 exhibits H1, and no H7 instances occur.
42	The near-absence of hacking confirms that the structural degeneration is a consequence of RL reward optimization, not model capacity or data limitations.
43	
44	\subsection{Meta-Level Goodhart's Law}
45	\label{sec:goodhart}
46	
47	ISR-as-reward exhibits \emph{meta-level} Goodhart~\citep{manheim-goodhart-taxonomy}---the diagnostic itself becomes the target of gaming when optimized.
48	
49	\begin{table}[t]
50	\centering
51	\small
52	\resizebox{\columnwidth}{!}{%
53	\begin{tabular}{lcccccc}
54	\toprule
55	\textbf{Condition} & $\boldsymbol{\beta}$ & \textbf{PR\%}$\uparrow$ & \textbf{ISR}$^*$ & \textbf{H7\%} & \textbf{H1\%} & \textbf{Gen.\%} \\
56	\midrule
57	Base (0-shot) & --- & 12 & --- & --- & --- & --- \\
58	SFT & --- & 14 & 0.571 & 0 & 7 & \textbf{93} \\
59	\midrule
60	Exec-only$^\dagger$ & --- & 93 & 0.132 & 0 & 87 & 13 \\
61	ISR & 0.1 & 77{\scriptsize$\pm$14} & $\ddagger$ & \textbf{65} & 17 & ${\sim}$16 \\
62	Random & 0.1 & \textbf{85}{\scriptsize$\pm$6} & 0.086{\scriptsize$\pm$.04} & 0 & 81 & 19 \\
63	\midrule
64	ISR & 0.3 & 18 & 0.143 & --- & --- & --- \\
65	Random & 0.3 & 48 & 0.094 & --- & --- & --- \\
66	\bottomrule
67	\end{tabular}}
68	\caption{Goodhart landscape across reward conditions. 3-seed rows show mean$\pm$std (ISR/Random $\beta{=}0.1$); other rows are single seed. $^\dagger$Seed~42; see \S\ref{sec:diagnostic} for 3-seed divergence. $\ddagger$ISR$^*$ omitted: inflated by H7 gaming (Appendix Table~\ref{tab:beta01-3seed}). Best PR and Gen.\% bolded per group.}
69	\label{tab:goodhart-landscape}
70	\end{table}
71	
72	\textbf{Low-dose ISR ($\beta{=}0.1$): ISR-specific gaming.}
73	Table~\ref{tab:goodhart-landscape} summarizes results.
74	At $\beta{=}0.1$, 2/3 ISR seeds (s43, s44) are dominated by H7---a single premise identical to the conclusion, trivially achieving both high PR and ISR.
75	Across the three ISR seeds, H7 accounts for 64.5\% of proved samples (149/231); all three random controls show \emph{zero} H7 (0/256), confirming H7 is exclusively induced by the ISR signal.
76	Conclusion embedding (H1+H7) is GRPO-universal at 68--97\% across RL conditions: random produces only H1 (70.9--93.2\%), while ISR converts H1$\to$H7 without reducing the total (Figure~\ref{fig:hacking-composition}; per-seed: Appendix Table~\ref{tab:beta01-3seed}).
77	Random also achieves higher and more stable PR (85$\pm$6\% vs 77$\pm$14\%).
78	
79	\textbf{Premise-count confound.}
80	Seed~42 under ISR---the only seed not dominated by H7---shows higher raw ISR (0.415 vs 0.131 for random).
81	This is entirely a premise-minimization artifact: ISR-trained models produce shorter formalizations (mean 5.58 vs 8.46 components), and LOO is mathematically biased toward shorter inputs.
82	Restricting to genuine samples with $\geq$3 premises: ISR-genuine ISR${=}0.258$ ($n{=}11$) vs random-genuine ISR${=}0.243$ ($n{=}21$)---a 1.06$\times$ ratio, no meaningful advantage.
83	Of ISR s42's 25 nominally genuine samples, 15 have only 1--2 premises, where ISR$\geq0.5$ is a mathematical artifact.
84	
85	\textbf{High-dose ISR ($\beta{=}0.3$): classic Goodhart.}
86	At $\beta{=}0.3$, ISR causes PR to collapse to 18\%---a 5.2$\times$ degradation from exec-only---while the matched random control achieves PR${=}48$\%.
87	The two doses reveal a complete Goodhart trajectory~\citep{karwowski-goodhart-rl, gao-reward-overoptimization} at the meta level: low-dose proxy gaming (ISR inflation via H7) followed by high-dose performance collapse, with the proxy being gamed itself a gaming detector.
88	Under the taxonomy of \citet{manheim-goodhart-taxonomy}, $\beta{=}0.3$ exemplifies extremal Goodhart while $\beta{=}0.1$ instantiates a meta-level variant.
89	
90	\subsection{Cross-Logic Diagnostic Transfer}
91	\label{sec:crosslogic}
92	
93	We replicated both experiments using SWI-Prolog 8.4.2 (full results: Appendix Table~\ref{tab:prolog-crosslogic}).
94	Prolog exec-only confirms diagnostic transfer (2/3 seeds with ISR${\approx}0$ despite moderate-high PR); the low ISR reflects \emph{redundant coding} (repeated ground facts), not absent reasoning---contrasting the metric-gaming high ISR under Prolog ISR-reward.
95	ISR-as-reward yields universal Goodhart with 0\% genuine across 185 proved samples (stronger than the FOL ${\sim}16$\% residual), via three distinct mechanisms: s42 clean H7 tautologies (ISR$^*{=}1.000$); s43 uppercase pseudo-Prolog functionally equivalent to H7 ($n_{\text{nec}}{=}1$, 38/38); s44 query-as-fact gaming, converting NL to snake\_case atoms used as both fact and query (ISR$^*{=}0.912$, $n_{\text{nec}}{=}1$, 95/97).
96	The diversity of pathways under identical data and reward shows Goodhart here is a family of convergent exploits; the text-classifier bypass by s44 motivates functional cross-validation of automated diagnostics.
97	
98	\subsection{Hacking Taxonomy}
99	\label{sec:taxonomy}
100	
101	\begin{figure}[t]
102	\centering
103	\includegraphics[width=0.9\columnwidth]{figures/fig3_hacking_composition.pdf}
104	\caption{Hacking composition across reward conditions (proved samples). ISR converts H1 (conclusion embedding) into more extreme H7 (conclusion duplication) without reducing total hacking; SFT is near-zero hacking (92.9\% genuine).}
105	\label{fig:hacking-composition}
106	\end{figure}
107	
108	The seven modes (quantitative breakdown and definitions in Appendix~\ref{app:hacking-modes}, Table~\ref{tab:hacking-taxonomy-app}): \textbf{H1} (GRPO-universal, 68--97\%), \textbf{H7} (ISR-specific, 64.5\% under $\beta{=}0.1$ vs.\ 0\% random), \textbf{tautological} (exec-only s44, 94\%), \textbf{repetition} (exec-only s43, 87\% hit max length), \textbf{contradiction explosion} (mean 18.55 components at 1000 steps), \textbf{complexity-without-utility} (Random $\beta{=}0.1$, 3.8\%), \textbf{query-as-fact} (Prolog ISR s44, bypasses text classifiers).
109	The reward signal determines hacking \emph{composition} but not \emph{prevalence}: total conclusion-in-premise rates are comparable across ISR and random (${\sim}82$\% pooled), but ISR converts H1 into H7.
110	SFT remains the only condition with near-zero hacking (Figure~\ref{fig:hacking-composition}), confirming hacking is RL-reward-specific.
111	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3d63d97c-94e0-4e2a-a7e7-b0a2c0b11ca7",
  "isSidechain": false,
  "promptId": "c33bf5b5-c338-4f2f-97b8-e3e6d5f92819",
  "type": "user",
  "uuid": "36c229e1-6378-4042-8527-ca8b8c4b7091",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex",
      "content": "\\section{Experiments}\n\\label{sec:experiments}\n\nWe evaluate STA along three axes: as a diagnostic for reward hacking (\\S\\ref{sec:diagnostic}); as a training reward exhibiting meta-level Goodhart's Law (\\S\\ref{sec:goodhart}); and as a cross-logic protocol (\\S\\ref{sec:crosslogic}). We synthesize results into a hacking taxonomy (\\S\\ref{sec:taxonomy}).\n\n\\subsection{Setup}\n\\label{sec:setup}\n\nWe train Qwen3-4B with GRPO~\\citep{deepseekmath} using $K{=}8$ rollouts per prompt for 500 steps (default) or 1000 where noted, across seeds $\\{42,43,44\\}$.\nTraining data is a fixed 500-example subset of FOLIO~\\citep{folio} (\\texttt{train\\_500\\_seed42.jsonl}), held constant across all seeds and conditions.\nWe use Prover9 for FOL and SWI-Prolog 8.4.2 for Prolog.\nEvaluation is on 100 held-out FOLIO examples with greedy decoding; all cross-run ISR values are computed by \\texttt{eval\\_sta.py} which applies STA uniformly.\nWe report prove rate (PR), proved-only ISR (ISR$^*$, over proved samples only), hacking mode percentages (H7, H1), genuine rate, and mean component count.\nSix reward conditions are compared: \\textbf{Exec-only}, \\textbf{ISR~$\\beta{\\in}\\{0.1,0.3\\}$}, \\textbf{Random~$\\beta{\\in}\\{0.1,0.3\\}$}, and \\textbf{SFT}.\nOutputs are classified into H7, H1, and Genuine using text matching cross-validated with functional LOO analysis.\nFull hyperparameters are in Appendix~\\ref{app:setup}.\n\n\\subsection{ISR as Diagnostic}\n\\label{sec:diagnostic}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.95\\columnwidth]{figures/fig2_isr_collapse.pdf}\n\\caption{ISR collapse under exec-only GRPO (seed~42). PR rises 32\\%$\\to$96\\% while proved-only ISR falls 0.642$\\to$0.003 over 1000 steps. By step 1000, 94.8\\% of proved samples have ISR${=}0$ and mean component count inflates 6.58$\\to$18.55 (contradiction explosion).}\n\\label{fig:isr-collapse}\n\\end{figure}\n\n\\textbf{Collapse trajectory.}\nFigure~\\ref{fig:isr-collapse} traces ISR and PR over training for exec-only GRPO (seed~42).\nAt 100 steps: PR${=}32$\\%, ISR${=}0.642$.\nBy 500 steps: PR${=}93$\\% but ISR${=}0.132$---87.1\\% of proved samples embed the conclusion among the premises (H1).\nAt 1000 steps: PR${=}96$\\% while ISR drops to 0.003 (H1${=}100$\\%, mean components 18.55).\nThe ISR trajectory ($0.642{\\to}0.132{\\to}0.003$) is monotonically decreasing: extended training worsens structural degeneration, invisible to PR.\n\n\\textbf{Cross-seed instability.}\nThe three exec-only seeds diverge radically: s42 hacks via H1 (PR${=}93$\\%, H1${=}87.1$\\%); s43 collapses to PR${=}14$\\% (ISR${=}0$) via repetition---87\\% of outputs hit the max token length; s44 reaches PR${=}98$\\% via tautological collapse (H7${=}100$\\%, mean components 2.04).\nDespite PR$\\in[14,98]$\\%, all three seeds exhibit structural degeneration detectable by ISR.\nThe cross-seed PR $\\sigma{=}\\pm47$\\,pp is itself a finding: aggregate metrics obscure qualitatively different failure modes (per-seed details in Table~\\ref{tab:beta01-3seed}).\n\n\\textbf{SFT baseline.}\nA supervised baseline achieves PR${=}14$\\% with ISR${=}0.571$: 92.9\\% (13/14) of proved samples are genuine, only 1 exhibits H1, and no H7 instances occur.\nThe near-absence of hacking confirms that the structural degeneration is a consequence of RL reward optimization, not model capacity or data limitations.\n\n\\subsection{Meta-Level Goodhart's Law}\n\\label{sec:goodhart}\n\nISR-as-reward exhibits \\emph{meta-level} Goodhart~\\citep{manheim-goodhart-taxonomy}---the diagnostic itself becomes the target of gaming when optimized.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcccccc}\n\\toprule\n\\textbf{Condition} & $\\boldsymbol{\\beta}$ & \\textbf{PR\\%}$\\uparrow$ & \\textbf{ISR}$^*$ & \\textbf{H7\\%} & \\textbf{H1\\%} & \\textbf{Gen.\\%} \\\\\n\\midrule\nBase (0-shot) & --- & 12 & --- & --- & --- & --- \\\\\nSFT & --- & 14 & 0.571 & 0 & 7 & \\textbf{93} \\\\\n\\midrule\nExec-only$^\\dagger$ & --- & 93 & 0.132 & 0 & 87 & 13 \\\\\nISR & 0.1 & 77{\\scriptsize$\\pm$14} & $\\ddagger$ & \\textbf{65} & 17 & ${\\sim}$16 \\\\\nRandom & 0.1 & \\textbf{85}{\\scriptsize$\\pm$6} & 0.086{\\scriptsize$\\pm$.04} & 0 & 81 & 19 \\\\\n\\midrule\nISR & 0.3 & 18 & 0.143 & --- & --- & --- \\\\\nRandom & 0.3 & 48 & 0.094 & --- & --- & --- \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Goodhart landscape across reward conditions. 3-seed rows show mean$\\pm$std (ISR/Random $\\beta{=}0.1$); other rows are single seed. $^\\dagger$Seed~42; see \\S\\ref{sec:diagnostic} for 3-seed divergence. $\\ddagger$ISR$^*$ omitted: inflated by H7 gaming (Appendix Table~\\ref{tab:beta01-3seed}). Best PR and Gen.\\% bolded per group.}\n\\label{tab:goodhart-landscape}\n\\end{table}\n\n\\textbf{Low-dose ISR ($\\beta{=}0.1$): ISR-specific gaming.}\nTable~\\ref{tab:goodhart-landscape} summarizes results.\nAt $\\beta{=}0.1$, 2/3 ISR seeds (s43, s44) are dominated by H7---a single premise identical to the conclusion, trivially achieving both high PR and ISR.\nAcross the three ISR seeds, H7 accounts for 64.5\\% of proved samples (149/231); all three random controls show \\emph{zero} H7 (0/256), confirming H7 is exclusively induced by the ISR signal.\nConclusion embedding (H1+H7) is GRPO-universal at 68--97\\% across RL conditions: random produces only H1 (70.9--93.2\\%), while ISR converts H1$\\to$H7 without reducing the total (Figure~\\ref{fig:hacking-composition}; per-seed: Appendix Table~\\ref{tab:beta01-3seed}).\nRandom also achieves higher and more stable PR (85$\\pm$6\\% vs 77$\\pm$14\\%).\n\n\\textbf{Premise-count confound.}\nSeed~42 under ISR---the only seed not dominated by H7---shows higher raw ISR (0.415 vs 0.131 for random).\nThis is entirely a premise-minimization artifact: ISR-trained models produce shorter formalizations (mean 5.58 vs 8.46 components), and LOO is mathematically biased toward shorter inputs.\nRestricting to genuine samples with $\\geq$3 premises: ISR-genuine ISR${=}0.258$ ($n{=}11$) vs random-genuine ISR${=}0.243$ ($n{=}21$)---a 1.06$\\times$ ratio, no meaningful advantage.\nOf ISR s42's 25 nominally genuine samples, 15 have only 1--2 premises, where ISR$\\geq0.5$ is a mathematical artifact.\n\n\\textbf{High-dose ISR ($\\beta{=}0.3$): classic Goodhart.}\nAt $\\beta{=}0.3$, ISR causes PR to collapse to 18\\%---a 5.2$\\times$ degradation from exec-only---while the matched random control achieves PR${=}48$\\%.\nThe two doses reveal a complete Goodhart trajectory~\\citep{karwowski-goodhart-rl, gao-reward-overoptimization} at the meta level: low-dose proxy gaming (ISR inflation via H7) followed by high-dose performance collapse, with the proxy being gamed itself a gaming detector.\nUnder the taxonomy of \\citet{manheim-goodhart-taxonomy}, $\\beta{=}0.3$ exemplifies extremal Goodhart while $\\beta{=}0.1$ instantiates a meta-level variant.\n\n\\subsection{Cross-Logic Diagnostic Transfer}\n\\label{sec:crosslogic}\n\nWe replicated both experiments using SWI-Prolog 8.4.2 (full results: Appendix Table~\\ref{tab:prolog-crosslogic}).\nProlog exec-only confirms diagnostic transfer (2/3 seeds with ISR${\\approx}0$ despite moderate-high PR); the low ISR reflects \\emph{redundant coding} (repeated ground facts), not absent reasoning---contrasting the metric-gaming high ISR under Prolog ISR-reward.\nISR-as-reward yields universal Goodhart with 0\\% genuine across 185 proved samples (stronger than the FOL ${\\sim}16$\\% residual), via three distinct mechanisms: s42 clean H7 tautologies (ISR$^*{=}1.000$); s43 uppercase pseudo-Prolog functionally equivalent to H7 ($n_{\\text{nec}}{=}1$, 38/38); s44 query-as-fact gaming, converting NL to snake\\_case atoms used as both fact and query (ISR$^*{=}0.912$, $n_{\\text{nec}}{=}1$, 95/97).\nThe diversity of pathways under identical data and reward shows Goodhart here is a family of convergent exploits; the text-classifier bypass by s44 motivates functional cross-validation of automated diagnostics.\n\n\\subsection{Hacking Taxonomy}\n\\label{sec:taxonomy}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.9\\columnwidth]{figures/fig3_hacking_composition.pdf}\n\\caption{Hacking composition across reward conditions (proved samples). ISR converts H1 (conclusion embedding) into more extreme H7 (conclusion duplication) without reducing total hacking; SFT is near-zero hacking (92.9\\% genuine).}\n\\label{fig:hacking-composition}\n\\end{figure}\n\nThe seven modes (quantitative breakdown and definitions in Appendix~\\ref{app:hacking-modes}, Table~\\ref{tab:hacking-taxonomy-app}): \\textbf{H1} (GRPO-universal, 68--97\\%), \\textbf{H7} (ISR-specific, 64.5\\% under $\\beta{=}0.1$ vs.\\ 0\\% random), \\textbf{tautological} (exec-only s44, 94\\%), \\textbf{repetition} (exec-only s43, 87\\% hit max length), \\textbf{contradiction explosion} (mean 18.55 components at 1000 steps), \\textbf{complexity-without-utility} (Random $\\beta{=}0.1$, 3.8\\%), \\textbf{query-as-fact} (Prolog ISR s44, bypasses text classifiers).\nThe reward signal determines hacking \\emph{composition} but not \\emph{prevalence}: total conclusion-in-premise rates are comparable across ISR and random (${\\sim}82$\\% pooled), but ISR converts H1 into H7.\nSFT remains the only condition with near-zero hacking (Figure~\\ref{fig:hacking-composition}), confirming hacking is RL-reward-specific.\n",
      "numLines": 111,
      "startLine": 1,
      "totalLines": 111
    }
  },
  "sourceToolAssistantUUID": "3d63d97c-94e0-4e2a-a7e7-b0a2c0b11ca7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "24e67ff1-1ea3-4bcf-a9e3-703eaa6cb36e",
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
  "leafUuid": "36c229e1-6378-4042-8527-ca8b8c4b7091",
  "sessionId": "24e67ff1-1ea3-4bcf-a9e3-703eaa6cb36e"
}
```

---

### Runtime record

_source line 34_

```json
{
  "type": "ai-title",
  "aiTitle": "Audit paper figures against experiment registry",
  "sessionId": "24e67ff1-1ea3-4bcf-a9e3-703eaa6cb36e"
}
```

---

### Tool call

_source line 35 · 2026-05-14T21:45:03.374Z_

<details open><summary>🔧 Tool call — Read · `toolu_019TjfKEGPnpe6HYsQUS9mTn`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "36c229e1-6378-4042-8527-ca8b8c4b7091",
  "isSidechain": false,
  "requestId": "req_011Cb3C9iWLjdM4NdJacdL6f",
  "type": "assistant",
  "uuid": "bd839cf1-705e-443a-b52d-b7c73820159f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "24e67ff1-1ea3-4bcf-a9e3-703eaa6cb36e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_015UTHrxPWxRf31XuqSNJykB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4722,
      "cache_read_input_tokens": 73415,
      "output_tokens": 112,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4722,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 112,
          "cache_read_input_tokens": 73415,
          "cache_creation_input_tokens": 4722,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4722
          },
          "type": "message"
        }
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

_source line 36 · 2026-05-14T21:45:03.381Z_

<details><summary>↩ Tool result · `toolu_019TjfKEGPnpe6HYsQUS9mTn`</summary>

```text
1	\section{Method}
2	\label{sec:method}
3	
4	\begin{figure*}[t]
5	\centering
6	\includegraphics[width=0.92\textwidth]{figures/fig1_sta_overview.pdf}
7	\caption{Solver Trace Ablation (STA). (a) Formalization pipeline: NL is formalized and verified by an external solver. (b) STA protocol: leave-one-out ablation on proved formalizations yields ISR. (c) ISR as diagnostic vs.\ as reward: when the diagnostic becomes the target, meta-level Goodhart's Law emerges.}
8	\label{fig:sta-overview}
9	\end{figure*}
10	
11	\subsection{Task and GRPO Training}
12	\label{sec:task}
13	
14	Given natural language premises $P_1,\ldots,P_k$ and a conclusion $C$, the task is to produce a formal logic program $F=\{c_1,\ldots,c_n\}$, where each component $c_i$ is a premise (FOL) or a clause/fact (Prolog), with one distinguished component encoding the query.
15	An external solver $S$ returns $S(F)\in\{\textit{proved},\textit{failed}\}$; we use Prover9 for FOL and SWI-Prolog for Prolog (\autoref{fig:sta-overview}a).
16	
17	We train formalizers with GRPO~\citep{deepseekmath} using $K{=}8$ rollouts per prompt.
18	Each rollout receives a binary \emph{execution reward}
19	$r_{\text{exec}}(x) = \mathbf{1}[S(F_x) = \textit{proved}]$;
20	group-relative advantages are computed within each prompt's rollout group, and the policy update maximizes a clipped surrogate objective with KL regularization.
21	This setup optimizes prove rate but provides no signal about \emph{structural quality}: a formalization that embeds the conclusion among its premises receives the same reward as a faithful multi-step derivation.
22	
23	\subsection{Solver Trace Ablation (STA)}
24	\label{sec:sta}
25	
26	To diagnose structural quality, STA tests whether each component of a proved formalization is individually necessary for proof success (\autoref{fig:sta-overview}b).
27	Given a proved $x$ with $n$ components, STA constructs $n$ ablated variants $x\setminus\{c_i\}$, each removing one component, and re-runs the solver.
28	A component is \emph{necessary} if its removal causes proof failure: $S(x\setminus\{c_i\})=\textit{failed}$.
29	What constitutes a component depends on the logic type: individual premises in FOL, individual clauses or ground facts in Prolog.
30	
31	\paragraph{Intensional Structural Reward.}
32	ISR is the fraction of necessary components:
33	\begin{equation}
34	  \text{ISR}(x) = \frac{1}{n}\sum_{i=1}^{n}\mathbf{1}\bigl[S(x\setminus\{c_i\})=\textit{failed}\bigr]
35	  \label{eq:isr}
36	\end{equation}
37	ISR $\in[0,1]$ is defined only for proved formalizations ($r_{\text{exec}}(x){=}1$): ISR${=}1$ indicates maximal tightness; ISR${=}0$ indicates complete redundancy.
38	The protocol is solver-agnostic, requiring $n{+}1$ solver calls per sample.
39	STA draws on the LOO intuition from mutation testing~\citep{demillo1978, jia-harman-survey} but operates on solver \emph{inputs} (formalizations) rather than program code, targeting component necessity rather than test adequacy.
40	Pseudocode is in Appendix~\ref{app:algorithm}.
41	
42	\paragraph{Limitations of ISR.}
43	ISR measures syntactic component necessity, not semantic faithfulness to the natural language input.
44	It is also subject to a component-count confound: formalizations with fewer components yield mechanically higher ISR, since each carries a larger share of the proof burden under LOO.
45	We control for this confound in our analysis (\S\ref{sec:goodhart}).
46	
47	\subsection{Reward Conditions}
48	\label{sec:rewards}
49	
50	We study six reward conditions (\autoref{fig:sta-overview}c).
51	For all RL conditions, bonuses apply only to proved samples; unproved samples receive $r{=}0$.
52	
53	\noindent\textbf{Exec-only:} $r=r_{\text{exec}}$ (baseline).
54	\noindent\textbf{Additive ISR:} $r=r_{\text{exec}}\cdot(1+\beta\,\text{ISR}(x))$ with $\beta\in\{0.1,0.3\}$, gating the structural bonus on proof success.
55	\noindent\textbf{Additive Random:} $r=r_{\text{exec}}\cdot(1+\beta\,u)$, $u\sim\mathcal{U}(0,1)$, $\beta\in\{0.1,0.3\}$: control isolating ISR-specific structural signal from variance/scaling effects.
56	\noindent\textbf{SFT baseline:} supervised fine-tuning on gold formalizations, testing whether observed hacking is RL-specific.
57	
58	Each RL condition is trained with seeds $\{42,43,44\}$ controlling initialization and stochasticity; all seeds share identical training data (\S\ref{sec:setup}).
59	
60	\subsection{Hacking Taxonomy}
61	\label{sec:taxonomy-method}
62	
63	Across conditions, seeds, and logic types, we identify seven hacking modes (H1, H7, tautological collapse, repetition collapse, complexity-without-utility, contradiction explosion, query-as-fact gaming; full definitions in \S\ref{sec:taxonomy} and Appendix~\ref{app:hacking-modes}).
64	Modes are identified by a two-stage procedure: strict normalized text matching catches H1/H7; functional analysis of the per-sample $n_{\text{necessary}}$ distribution from STA catches modes that evade text matching.
65	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bd839cf1-705e-443a-b52d-b7c73820159f",
  "isSidechain": false,
  "promptId": "c33bf5b5-c338-4f2f-97b8-e3e6d5f92819",
  "type": "user",
  "uuid": "1e27be37-b888-4e7d-ac0f-640a7ca9e81d",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/method.tex",
      "content": "\\section{Method}\n\\label{sec:method}\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=0.92\\textwidth]{figures/fig1_sta_overview.pdf}\n\\caption{Solver Trace Ablation (STA). (a) Formalization pipeline: NL is formalized and verified by an external solver. (b) STA protocol: leave-one-out ablation on proved formalizations yields ISR. (c) ISR as diagnostic vs.\\ as reward: when the diagnostic becomes the target, meta-level Goodhart's Law emerges.}\n\\label{fig:sta-overview}\n\\end{figure*}\n\n\\subsection{Task and GRPO Training}\n\\label{sec:task}\n\nGiven natural language premises $P_1,\\ldots,P_k$ and a conclusion $C$, the task is to produce a formal logic program $F=\\{c_1,\\ldots,c_n\\}$, where each component $c_i$ is a premise (FOL) or a clause/fact (Prolog), with one distinguished component encoding the query.\nAn external solver $S$ returns $S(F)\\in\\{\\textit{proved},\\textit{failed}\\}$; we use Prover9 for FOL and SWI-Prolog for Prolog (\\autoref{fig:sta-overview}a).\n\nWe train formalizers with GRPO~\\citep{deepseekmath} using $K{=}8$ rollouts per prompt.\nEach rollout receives a binary \\emph{execution reward}\n$r_{\\text{exec}}(x) = \\mathbf{1}[S(F_x) = \\textit{proved}]$;\ngroup-relative advantages are computed within each prompt's rollout group, and the policy update maximizes a clipped surrogate objective with KL regularization.\nThis setup optimizes prove rate but provides no signal about \\emph{structural quality}: a formalization that embeds the conclusion among its premises receives the same reward as a faithful multi-step derivation.\n\n\\subsection{Solver Trace Ablation (STA)}\n\\label{sec:sta}\n\nTo diagnose structural quality, STA tests whether each component of a proved formalization is individually necessary for proof success (\\autoref{fig:sta-overview}b).\nGiven a proved $x$ with $n$ components, STA constructs $n$ ablated variants $x\\setminus\\{c_i\\}$, each removing one component, and re-runs the solver.\nA component is \\emph{necessary} if its removal causes proof failure: $S(x\\setminus\\{c_i\\})=\\textit{failed}$.\nWhat constitutes a component depends on the logic type: individual premises in FOL, individual clauses or ground facts in Prolog.\n\n\\paragraph{Intensional Structural Reward.}\nISR is the fraction of necessary components:\n\\begin{equation}\n  \\text{ISR}(x) = \\frac{1}{n}\\sum_{i=1}^{n}\\mathbf{1}\\bigl[S(x\\setminus\\{c_i\\})=\\textit{failed}\\bigr]\n  \\label{eq:isr}\n\\end{equation}\nISR $\\in[0,1]$ is defined only for proved formalizations ($r_{\\text{exec}}(x){=}1$): ISR${=}1$ indicates maximal tightness; ISR${=}0$ indicates complete redundancy.\nThe protocol is solver-agnostic, requiring $n{+}1$ solver calls per sample.\nSTA draws on the LOO intuition from mutation testing~\\citep{demillo1978, jia-harman-survey} but operates on solver \\emph{inputs} (formalizations) rather than program code, targeting component necessity rather than test adequacy.\nPseudocode is in Appendix~\\ref{app:algorithm}.\n\n\\paragraph{Limitations of ISR.}\nISR measures syntactic component necessity, not semantic faithfulness to the natural language input.\nIt is also subject to a component-count confound: formalizations with fewer components yield mechanically higher ISR, since each carries a larger share of the proof burden under LOO.\nWe control for this confound in our analysis (\\S\\ref{sec:goodhart}).\n\n\\subsection{Reward Conditions}\n\\label{sec:rewards}\n\nWe study six reward conditions (\\autoref{fig:sta-overview}c).\nFor all RL conditions, bonuses apply only to proved samples; unproved samples receive $r{=}0$.\n\n\\noindent\\textbf{Exec-only:} $r=r_{\\text{exec}}$ (baseline).\n\\noindent\\textbf{Additive ISR:} $r=r_{\\text{exec}}\\cdot(1+\\beta\\,\\text{ISR}(x))$ with $\\beta\\in\\{0.1,0.3\\}$, gating the structural bonus on proof success.\n\\noindent\\textbf{Additive Random:} $r=r_{\\text{exec}}\\cdot(1+\\beta\\,u)$, $u\\sim\\mathcal{U}(0,1)$, $\\beta\\in\\{0.1,0.3\\}$: control isolating ISR-specific structural signal from variance/scaling effects.\n\\noindent\\textbf{SFT baseline:} supervised fine-tuning on gold formalizations, testing whether observed hacking is RL-specific.\n\nEach RL condition is trained with seeds $\\{42,43,44\\}$ controlling initialization and stochasticity; all seeds share identical training data (\\S\\ref{sec:setup}).\n\n\\subsection{Hacking Taxonomy}\n\\label{sec:taxonomy-method}\n\nAcross conditions, seeds, and logic types, we identify seven hacking modes (H1, H7, tautological collapse, repetition collapse, complexity-without-utility, contradiction explosion, query-as-fact gaming; full definitions in \\S\\ref{sec:taxonomy} and Appendix~\\ref{app:hacking-modes}).\nModes are identified by a two-stage procedure: strict normalized text matching catches H1/H7; functional analysis of the per-sample $n_{\\text{necessary}}$ distribution from STA catches modes that evade text matching.\n",
      "numLines": 65,
      "startLine": 1,
      "totalLines": 65
    }
  },
  "sourceToolAssistantUUID": "bd839cf1-705e-443a-b52d-b7c73820159f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "24e67ff1-1ea3-4bcf-a9e3-703eaa6cb36e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 37 · 2026-05-14T21:45:03.385Z_

```json
{
  "parentUuid": "1e27be37-b888-4e7d-ac0f-640a7ca9e81d",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "7e872302-c612-4c1d-b104-3f0448852f6f",
  "timestamp": "2026-05-14T21:45:03.385Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "24e67ff1-1ea3-4bcf-a9e3-703eaa6cb36e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 38 · 2026-05-14T21:45:05.649Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01P4W8VTBtDkwhJ7vynr2nsg`</summary>

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
  "parentUuid": "7e872302-c612-4c1d-b104-3f0448852f6f",
  "isSidechain": false,
  "requestId": "req_011Cb3CA24HKMwCcuBRWKEde",
  "type": "assistant",
  "uuid": "dae53894-ad10-4f20-887d-60d88ba6445d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "24e67ff1-1ea3-4bcf-a9e3-703eaa6cb36e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_015zamHyQ8G6DQ33mrDUZi5q",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2450,
      "cache_read_input_tokens": 78137,
      "output_tokens": 96,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2450,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 96,
          "cache_read_input_tokens": 78137,
          "cache_creation_input_tokens": 2450,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2450
          },
          "type": "message"
        }
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

_source line 39 · 2026-05-14T21:45:05.651Z_

<details><summary>↩ Tool result · `toolu_01P4W8VTBtDkwhJ7vynr2nsg`</summary>

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
  "parentUuid": "dae53894-ad10-4f20-887d-60d88ba6445d",
  "isSidechain": false,
  "promptId": "c33bf5b5-c338-4f2f-97b8-e3e6d5f92819",
  "type": "user",
  "uuid": "dc9835ab-d47a-44d6-b85b-9eaea70cd836",
  "toolUseResult": {
    "matches": [
      "TodoWrite"
    ],
    "query": "select:TodoWrite",
    "total_deferred_tools": 25
  },
  "sourceToolAssistantUUID": "dae53894-ad10-4f20-887d-60d88ba6445d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "24e67ff1-1ea3-4bcf-a9e3-703eaa6cb36e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-14T21:45:15.125Z_

<details open><summary>🔧 Tool call — TodoWrite · `toolu_016Cduq3Bzq41aVAmfQkJPaW`</summary>

```json
{
  "todos": [
    {
      "content": "Read all paper sections (conclusion, related_work, appendix)",
      "activeForm": "Reading remaining paper sections",
      "status": "in_progress"
    },
    {
      "content": "Cross-check ISR collapse trajectory numbers (0.642/0.132/0.003)",
      "activeForm": "Cross-checking ISR collapse numbers",
      "status": "pending"
    },
    {
      "content": "Cross-check 3-seed β=0.1 ISR/Random numbers in Table 1 and appendix",
      "activeForm": "Cross-checking β=0.1 3-seed numbers",
      "status": "pending"
    },
    {
      "content": "Cross-check SFT baseline numbers (PR=14%, ISR=0.571, 92.9%)",
      "activeForm": "Cross-checking SFT baseline numbers",
      "status": "pending"
    },
    {
      "content": "Cross-check Prolog numbers in experiments/appendix",
      "activeForm": "Cross-checking Prolog numbers",
      "status": "pending"
    },
    {
      "content": "Check hard constraints (no 2.4x, hacking taxonomy 7, etc.)",
      "activeForm": "Checking hard constraints from paper_framing",
      "status": "pending"
    },
    {
      "content": "Check internal consistency between abstract/intro/experiments/conclusion",
      "activeForm": "Checking internal consistency",
      "status": "pending"
    },
    {
      "content": "Write consistency report to artifacts/",
      "activeForm": "Writing consistency report",
      "status": "pending"
    }
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dc9835ab-d47a-44d6-b85b-9eaea70cd836",
  "isSidechain": false,
  "requestId": "req_011Cb3CABucRH5X8yjGif29Y",
  "type": "assistant",
  "uuid": "a7aeafed-b528-4c28-9ab5-a393e7cca8bc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "24e67ff1-1ea3-4bcf-a9e3-703eaa6cb36e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01HV33H3X1X6zoWD6ioLYQyk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 3512,
      "cache_read_input_tokens": 80587,
      "output_tokens": 561,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3512,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6,
          "output_tokens": 561,
          "cache_read_input_tokens": 80587,
          "cache_creation_input_tokens": 3512,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3512
          },
          "type": "message"
        }
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

_source line 41 · 2026-05-14T21:45:15.128Z_

<details><summary>↩ Tool result · `toolu_016Cduq3Bzq41aVAmfQkJPaW`</summary>

```text
Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a7aeafed-b528-4c28-9ab5-a393e7cca8bc",
  "isSidechain": false,
  "promptId": "c33bf5b5-c338-4f2f-97b8-e3e6d5f92819",
  "type": "user",
  "uuid": "77b8a9ec-b151-45a9-8de7-0f4fa550279b",
  "toolUseResult": {
    "oldTodos": [],
    "newTodos": [
      {
        "content": "Read all paper sections (conclusion, related_work, appendix)",
        "status": "in_progress",
        "activeForm": "Reading remaining paper sections"
      },
      {
        "content": "Cross-check ISR collapse trajectory numbers (0.642/0.132/0.003)",
        "status": "pending",
        "activeForm": "Cross-checking ISR collapse numbers"
      },
      {
        "content": "Cross-check 3-seed β=0.1 ISR/Random numbers in Table 1 and appendix",
        "status": "pending",
        "activeForm": "Cross-checking β=0.1 3-seed numbers"
      },
      {
        "content": "Cross-check SFT baseline numbers (PR=14%, ISR=0.571, 92.9%)",
        "status": "pending",
        "activeForm": "Cross-checking SFT baseline numbers"
      },
      {
        "content": "Cross-check Prolog numbers in experiments/appendix",
        "status": "pending",
        "activeForm": "Cross-checking Prolog numbers"
      },
      {
        "content": "Check hard constraints (no 2.4x, hacking taxonomy 7, etc.)",
        "status": "pending",
        "activeForm": "Checking hard constraints from paper_framing"
      },
      {
        "content": "Check internal consistency between abstract/intro/experiments/conclusion",
        "status": "pending",
        "activeForm": "Checking internal consistency"
      },
      {
        "content": "Write consistency report to artifacts/",
        "status": "pending",
        "activeForm": "Writing consistency report"
      }
    ],
    "verificationNudgeNeeded": false
  },
  "sourceToolAssistantUUID": "a7aeafed-b528-4c28-9ab5-a393e7cca8bc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "24e67ff1-1ea3-4bcf-a9e3-703eaa6cb36e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-14T21:45:18.902Z_

<details open><summary>🔧 Tool call — Read · `toolu_01UkNmdhqJ6xKrXGMeZePMsG`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "77b8a9ec-b151-45a9-8de7-0f4fa550279b",
  "isSidechain": false,
  "requestId": "req_011Cb3CAtLDSzPou5TTgAfss",
  "type": "assistant",
  "uuid": "04a2db91-6709-4df5-a363-dd45bb50a5fa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "24e67ff1-1ea3-4bcf-a9e3-703eaa6cb36e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_016LijnS4LxED3N681B1khEj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 633,
      "cache_read_input_tokens": 84099,
      "output_tokens": 305,
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
          "output_tokens": 305,
          "cache_read_input_tokens": 84099,
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

_source line 43 · 2026-05-14T21:45:18.906Z_

<details><summary>↩ Tool result · `toolu_01UkNmdhqJ6xKrXGMeZePMsG`</summary>

```text
1	\section{Discussion and Conclusion}
2	
3	We introduced Solver Trace Ablation (STA), a component-level diagnostic for neurosymbolic formalizers that exposes structural degeneration invisible to execution-based evaluation.
4	Applied to GRPO-trained models, ISR reveals a collapse trajectory hidden from prove rate, confirmed as RL-specific by an SFT baseline with near-zero hacking (\S\ref{sec:diagnostic}).
5	When repurposed as a training signal, ISR induces meta-level Goodhart's Law: at low dose, the model games the diagnostic itself through conclusion duplication absent under matched controls; at high dose, prove rate collapses; the sole apparent ISR improvement reduces to noise after controlling for a premise-count confound (\S\ref{sec:goodhart}).
6	Both diagnostic utility and Goodhart vulnerability transfer to Prolog/SWI-Prolog: ISR-as-reward yields universal gaming across all seeds with zero genuine proofs, each via a distinct mechanism (\S\ref{sec:crosslogic}).
7	Across six reward conditions and two logic types, we catalog seven hacking modes, including query-as-fact gaming that bypasses text-match classifiers (\S\ref{sec:taxonomy}).
8	
9	\paragraph{Interpreting ISR.}
10	ISR values must always be read relative to the optimization objective: under exec-only Prolog training, \emph{low} ISR reflects redundant coding (repeated ground facts), not absence of reasoning; under ISR-as-reward, \emph{high} ISR reflects metric gaming.
11	The premise-count confound---fewer components mechanically inflate ISR under LOO---applies to any ablation-based diagnostic on variable-length outputs.
12	
13	\paragraph{Meta-Level Goodhart.}
14	ISR was designed to \emph{detect} reward gaming of $r_{\text{exec}}$, yet incorporating it into the reward causes the model to game ISR itself---a regress where any diagnostic metric risks becoming a target when optimized.
15	The dose-response pattern ($\beta{=}0.1$: proxy gaming; $\beta{=}0.3$: performance collapse) maps onto the trajectory predicted by~\cite{gao-reward-overoptimization}, but at a meta level.
16	ISR---and structurally similar diagnostics---should be used exclusively as post-hoc evaluation tools, never as training rewards.
17	The fundamental asymmetry (reliable as observer, unreliable as optimizer) may generalize to other perturbation-based quality metrics.
18	
19	\paragraph{Limitations.}
20	Experiments use a single base model (Qwen3-4B) and dataset family (FOLIO); generalization remains untested.
21	ISR quantifies syntactic component necessity, not semantic faithfulness: a downstream NLI evaluation finds ISR and task accuracy uncorrelated (Spearman $\rho{=}{-}0.049$, $p{=}0.187$; Appendix~\ref{app:extended-discussion}).
22	Three seeds demonstrate qualitative divergence but limit statistical power.
23	STA requires solvers supporting component-level input manipulation.
24	Combining ISR with semantic verification, adaptive reward weighting that detects gaming signatures, and extending STA to broader logic types are promising directions.
25	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "04a2db91-6709-4df5-a363-dd45bb50a5fa",
  "isSidechain": false,
  "promptId": "c33bf5b5-c338-4f2f-97b8-e3e6d5f92819",
  "type": "user",
  "uuid": "70a91ebe-9482-46b4-8d2a-bf316f9dbf09",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/conclusion.tex",
      "content": "\\section{Discussion and Conclusion}\n\nWe introduced Solver Trace Ablation (STA), a component-level diagnostic for neurosymbolic formalizers that exposes structural degeneration invisible to execution-based evaluation.\nApplied to GRPO-trained models, ISR reveals a collapse trajectory hidden from prove rate, confirmed as RL-specific by an SFT baseline with near-zero hacking (\\S\\ref{sec:diagnostic}).\nWhen repurposed as a training signal, ISR induces meta-level Goodhart's Law: at low dose, the model games the diagnostic itself through conclusion duplication absent under matched controls; at high dose, prove rate collapses; the sole apparent ISR improvement reduces to noise after controlling for a premise-count confound (\\S\\ref{sec:goodhart}).\nBoth diagnostic utility and Goodhart vulnerability transfer to Prolog/SWI-Prolog: ISR-as-reward yields universal gaming across all seeds with zero genuine proofs, each via a distinct mechanism (\\S\\ref{sec:crosslogic}).\nAcross six reward conditions and two logic types, we catalog seven hacking modes, including query-as-fact gaming that bypasses text-match classifiers (\\S\\ref{sec:taxonomy}).\n\n\\paragraph{Interpreting ISR.}\nISR values must always be read relative to the optimization objective: under exec-only Prolog training, \\emph{low} ISR reflects redundant coding (repeated ground facts), not absence of reasoning; under ISR-as-reward, \\emph{high} ISR reflects metric gaming.\nThe premise-count confound---fewer components mechanically inflate ISR under LOO---applies to any ablation-based diagnostic on variable-length outputs.\n\n\\paragraph{Meta-Level Goodhart.}\nISR was designed to \\emph{detect} reward gaming of $r_{\\text{exec}}$, yet incorporating it into the reward causes the model to game ISR itself---a regress where any diagnostic metric risks becoming a target when optimized.\nThe dose-response pattern ($\\beta{=}0.1$: proxy gaming; $\\beta{=}0.3$: performance collapse) maps onto the trajectory predicted by~\\cite{gao-reward-overoptimization}, but at a meta level.\nISR---and structurally similar diagnostics---should be used exclusively as post-hoc evaluation tools, never as training rewards.\nThe fundamental asymmetry (reliable as observer, unreliable as optimizer) may generalize to other perturbation-based quality metrics.\n\n\\paragraph{Limitations.}\nExperiments use a single base model (Qwen3-4B) and dataset family (FOLIO); generalization remains untested.\nISR quantifies syntactic component necessity, not semantic faithfulness: a downstream NLI evaluation finds ISR and task accuracy uncorrelated (Spearman $\\rho{=}{-}0.049$, $p{=}0.187$; Appendix~\\ref{app:extended-discussion}).\nThree seeds demonstrate qualitative divergence but limit statistical power.\nSTA requires solvers supporting component-level input manipulation.\nCombining ISR with semantic verification, adaptive reward weighting that detects gaming signatures, and extending STA to broader logic types are promising directions.\n",
      "numLines": 25,
      "startLine": 1,
      "totalLines": 25
    }
  },
  "sourceToolAssistantUUID": "04a2db91-6709-4df5-a363-dd45bb50a5fa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "24e67ff1-1ea3-4bcf-a9e3-703eaa6cb36e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 44 · 2026-05-14T21:45:19.822Z_

<details open><summary>🔧 Tool call — Read · `toolu_01TN4bn4MNVvduzCG825AzjR`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "70a91ebe-9482-46b4-8d2a-bf316f9dbf09",
  "isSidechain": false,
  "requestId": "req_011Cb3CAtLDSzPou5TTgAfss",
  "type": "assistant",
  "uuid": "f14b5fa0-6733-4f57-878a-cb16faf478ed",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "24e67ff1-1ea3-4bcf-a9e3-703eaa6cb36e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_016LijnS4LxED3N681B1khEj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 633,
      "cache_read_input_tokens": 84099,
      "output_tokens": 305,
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
          "output_tokens": 305,
          "cache_read_input_tokens": 84099,
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

_source line 45 · 2026-05-14T21:45:20.042Z_

<details><summary>↩ Tool result · `toolu_013YFTeiN5jogRoCpyZVYH6k`</summary>

```text
1	% Appendix — solver-trace-ablation
2	
3	\section{Experimental Setup}
4	\label{app:setup}
5	
6	Table~\ref{tab:hyperparams} lists all hyperparameters shared across experiments.
7	All RL conditions use the same GRPO configuration; only the reward function differs.
8	Seeds control model weight initialization and data shuffling; training data is held constant across all seeds and conditions (Constraint~C001).
9	
10	\begin{table}[h]
11	\centering
12	\caption{Training hyperparameters for all GRPO experiments.}
13	\label{tab:hyperparams}
14	\footnotesize
15	\resizebox{\columnwidth}{!}{%
16	\begin{tabular}{@{}ll@{}}
17	\toprule
18	\textbf{Parameter} & \textbf{Value} \\
19	\midrule
20	\multicolumn{2}{@{}l}{\textit{Model}} \\
21	Base model & Qwen3-4B \\
22	Precision & BF16 \\
23	\midrule
24	\multicolumn{2}{@{}l}{\textit{GRPO Training}} \\
25	Rollouts per prompt ($K$) & 8 \\
26	Training steps (default) & 500 \\
27	Training steps (extended) & 1000 \\
28	Learning rate & $1 \times 10^{-6}$ \\
29	Per-device batch size & 4 \\
30	Gradient accumulation steps & 2 \\
31	Effective batch size & 8 \\
32	Max completion length & 512 tokens \\
33	Random seeds & 42, 43, 44 \\
34	\midrule
35	\multicolumn{2}{@{}l}{\textit{Data}} \\
36	Training set & FOLIO, 500 examples \\
37	Evaluation set & FOLIO, 100 examples (held-out) \\
38	Data file & \texttt{train\_500\_seed42} \\
39	\midrule
40	\multicolumn{2}{@{}l}{\textit{Solvers}} \\
41	FOL solver & Prover9 \\
42	Prolog solver & SWI-Prolog 8.4.2 \\
43	\midrule
44	\multicolumn{2}{@{}l}{\textit{Evaluation}} \\
45	Decoding & Greedy ($T{=}0$) \\
46	ISR computation & \texttt{eval\_sta.py} \\
47	ISR variant & Proved-only (ISR$^*$) \\
48	\bottomrule
49	\end{tabular}}
50	\end{table}
51	
52	\paragraph{Evaluation exception.}
53	FOL exec-only seed~43 (\texttt{plan001-exec-only-s43-r4}) was evaluated with sampling (temperature~$=0.7$) rather than greedy decoding.
54	Its PR and ISR values are included for completeness but are not strictly comparable with other seeds under the unified evaluation protocol (C004).
55	
56	
57	\section{STA Algorithm}
58	\label{app:algorithm}
59	
60	Algorithm~\ref{alg:sta} gives the full procedure for computing ISR over a proved formalization.
61	
62	\begin{algorithm}[h]
63	\caption{Solver Trace Ablation (STA)}
64	\label{alg:sta}
65	\begin{algorithmic}[1]
66	\REQUIRE Formalization $x = \{c_1, \ldots, c_n\}$, solver $S$
67	\ENSURE ISR score $\in [0,1]$ or $\bot$ (undefined)
68	\IF{$S(x) \neq \textit{proved}$}
69	  \RETURN $\bot$
70	\ENDIF
71	\STATE $n_{\text{nec}} \gets 0$
72	\FOR{$i = 1$ \TO $n$}
73	  \STATE $x' \gets x \setminus \{c_i\}$
74	  \IF{$S(x') = \textit{failed}$}
75	    \STATE $n_{\text{nec}} \gets n_{\text{nec}} + 1$
76	  \ENDIF
77	\ENDFOR
78	\RETURN $n_{\text{nec}} \mathbin{/} n$
79	\end{algorithmic}
80	\end{algorithm}
81	
82	
83	\section{Extended Discussion}
84	\label{app:extended-discussion}
85	
86	\paragraph{What ISR measures---and what it does not.}
87	ISR quantifies syntactic component necessity: the fraction of solver-input components whose individual removal causes proof failure.
88	This is strictly weaker than semantic faithfulness---whether the formalization accurately captures the natural-language meaning.
89	We verify this empirically: Spearman $\rho(\text{ISR}, \text{NLI accuracy}) = -0.049$ ($p = 0.187$, n.s.) from a downstream NLI evaluation on exec-only checkpoint outputs.
90	ISR and downstream task performance are uncorrelated.
91	ISR is thus a structural integrity diagnostic, not a semantic quality metric: high ISR indicates that every component contributes to the proof, not that the proof faithfully represents the original reasoning problem.
92	
93	Critically, low ISR carries different semantics depending on the training objective.
94	Under exec-only training, low ISR in Prolog reflects redundant coding---repeated ground facts where removing any single copy does not affect the proof---rather than absence of reasoning (\S\ref{sec:crosslogic}).
95	Under ISR-as-reward, high ISR reflects metric gaming (\S\ref{sec:goodhart}).
96	ISR values must always be interpreted relative to the optimization objective that produced them.
97	
98	\paragraph{The premise-count confound.}
99	LOO-based metrics like ISR have an inherent mathematical bias: with fewer components, each is mechanically more likely to be necessary.
100	A formalization with 2 premises where both are necessary yields ISR${=}1.0$; one with 10 premises where 8 are necessary yields ISR${=}0.8$---even though the latter encodes richer reasoning.
101	This confound explains the sole apparent ISR-as-reward success (\S\ref{sec:goodhart}): ISR $\beta{=}0.1$ seed~42 produces shorter formalizations, mechanically inflating ISR.
102	Premise-count-matched comparison eliminates the difference ($1.06\times$; Table~\ref{tab:beta01-3seed}).
103	This bias is not specific to our setting---any LOO-based structural metric applied to variable-length outputs requires component-count normalization.
104	We recommend that future work employing ablation-based diagnostics report premise-count-matched comparisons alongside raw values.
105	
106	\paragraph{Meta-level Goodhart: implications.}
107	The meta-Goodhart finding extends beyond this specific system.
108	ISR was designed to \emph{detect} reward gaming of $r_{\text{exec}}$, yet when incorporated into the reward signal, the model games ISR itself---creating a regress where any diagnostic metric risks becoming a target when optimized.
109	The dose-response pattern ($\beta{=}0.1$: proxy gaming inflates ISR without genuine improvement; $\beta{=}0.3$: performance collapse) maps onto the trajectory predicted by~\cite{gao-reward-overoptimization}, but at a meta level: the proxy being gamed is itself a gaming detector.
110	Under the taxonomy of~\cite{manheim-goodhart-taxonomy}, $\beta{=}0.3$ exemplifies extremal Goodhart---the optimizer enters a regime where the proxy-target relationship breaks down entirely---while $\beta{=}0.1$ instantiates a meta-level variant where the diagnostic is gamed through its own measurement mechanism.
111	The practical implication is that ISR---and structurally similar diagnostics---should be used exclusively as post-hoc evaluation tools, never as training rewards.
112	
113	\paragraph{Single-seed unreliability.}
114	The three exec-only seeds diverge radically (PR $\sigma{=}\pm 47$ percentage points), each converging to a qualitatively different degeneration mode (\S\ref{sec:diagnostic}).
115	ISR $\beta{=}0.1$ seeds show similar divergence: 2/3 dominated by conclusion duplication (H7), 1/3 by premise minimization (\S\ref{sec:goodhart}).
116	Multi-seed evaluation with structural diagnostics should be standard practice for neurosymbolic RL systems.
117	
118	
119	\section{Hacking Mode Definitions}
120	\label{app:hacking-modes}
121	
122	We identify seven distinct reward hacking modes across all experiments.
123	Each mode is defined below with its mechanism, a representative example, and its interaction with ISR.
124	Table~\ref{tab:hacking-taxonomy-app} summarizes prevalence across FOL conditions.
125	
126	\begin{table}[h]
127	\centering
128	\small
129	\resizebox{\columnwidth}{!}{%
130	\begin{tabular}{@{}llcccc@{}}
131	\toprule
132	\textbf{Mode} & \textbf{Mechanism} & \textbf{Exec} & \textbf{ISR} & \textbf{Rnd} & \textbf{SFT} \\
133	\midrule
134	H1 & Concl.\ in premises & 87 & 17 & 81 & 7 \\
135	H7 & Single prem.\ = concl. & $\bullet$ & \textbf{65} & 0 & 0 \\
136	Tautological & 2-comp $P{=}C$ & $\bullet$ & 0 & 0 & 0 \\
137	Repetition & Output degen. & $\bullet$ & -- & -- & -- \\
138	Contradiction & $n_{\text{comp}}$ inflated & $\bullet$ & -- & -- & -- \\
139	C-w/o-utility & Complex, redundant & 0 & 0 & 4 & 0 \\
140	Q-as-fact & Atom = fact+query & -- & -- & -- & -- \\
141	\bottomrule
142	\end{tabular}}
143	\caption{Hacking taxonomy across FOL conditions (\% of proved samples). ISR/Rand columns: $\beta{=}0.1$ 3-seed means. Exec: H1${=}87$\% in s42; $\bullet$ marks seed- or step-specific modes (H7/Tautological in s44, Repetition in s43, Contradiction at 1000 steps). C-w/o-util.: complexity-without-utility (random-specific). Q-as-fact: Prolog STA only (Table~\ref{tab:prolog-crosslogic}).}
144	\label{tab:hacking-taxonomy-app}
145	\end{table}
146	
147	\subsection{H1 --- Conclusion Embedding}
148	
149	\paragraph{Definition.}
150	The conclusion appears verbatim (or with trivial variable renaming) as one premise among multiple premises.
151	The solver succeeds by matching the embedded conclusion, rendering the other premises irrelevant to the proof.
152	
153	\paragraph{Example (FOL).}
154	{\small\begin{verbatim}
155	Premises:
156	  all x (bird(x) -> flies(x)).
157	  bird(tweety).
158	  flies(tweety).  % conclusion embedded
159	Conclusion: flies(tweety).
160	\end{verbatim}}
161	
162	\paragraph{ISR interaction.}
163	Variable. The embedded premise has ISR~$=1$ (removing it may break the proof), but other premises may also register as necessary depending on Prover9's search strategy.
164	ISR does not distinguish trivial from substantive necessity.
165	
166	\paragraph{Prevalence.}
167	Conclusion embedding in some form (H1 multi-premise or H7 single-premise) is GRPO-universal at 68--97\% across all RL conditions.
168	Under exec-only and Random reward, it manifests as H1 (71--93\%); under ISR reward, it shifts to H7 (64.5\% pooled).
169	
170	
171	\subsection{H7 --- Conclusion Duplication}
172	
173	\paragraph{Definition.}
174	The entire formalization collapses to a single premise whose content is identical to the conclusion.
175	Since $P \to P$ is trivially provable, this simultaneously maximizes exec reward.
176	Because the sole premise is necessary for every sub-component of the conclusion under LOO ablation, ISR is inflated toward 1.0.
177	
178	\paragraph{Example (FOL).}
179	{\small\begin{verbatim}
180	Premises:
181	  all x ((A(x)&B(x))->(C(x)|D(x))).
182	Conclusion:
183	  all x ((A(x)&B(x))->(C(x)|D(x))).
184	\end{verbatim}}
185	
186	\paragraph{ISR interaction.}
187	ISR~$\approx 0.8$--$1.0$.
188	The single premise is trivially ``maximally necessary,'' but the proof is vacuous.
189	H7 is the only mode that simultaneously games both exec reward and ISR reward.
190	
191	\paragraph{Prevalence.}
192	ISR-specific: 64.5\% pooled (149/231) under ISR~$\beta{=}0.1$ (s42: 16.0\%, s43: 96.7\%, s44: 86.5\%).
193	\textbf{Zero} occurrences under Random~$\beta{=}0.1$ across all three seeds ($0/256$).
194	
195	
196	\subsection{Tautological Collapse}
197	
198	\paragraph{Definition.}
199	Two-component formalizations where the premise and conclusion are identical atomic or simple formulas, yielding a $P \to P$ tautology with minimal token cost.
200	
201	\paragraph{Example (FOL).}
202	\begin{verbatim}
203	Premises: p(a).
204	Conclusion: p(a).
205	\end{verbatim}
206	
207	\paragraph{ISR interaction.}
208	ISR~$=1.0$ (the sole premise is necessary).
209	Distinguished from H7 by having low component count ($n_{\text{comp}}\approx 2$) and atomic formulas rather than complex sub-structured conclusions.
210	
211	\paragraph{Prevalence.}
212	Dominant in FOL exec-only seed~44 (PR~$=0.98$, mean $n_{\text{comp}}=2.04$, 100\% H7 by strict classifier).
213	Also observed in Prolog exec+STA seed~42 (100\% H7, PR~$=0.50$).
214	
215	
216	\subsection{Repetition Collapse}
217	
218	\paragraph{Definition.}
219	The model generates identical premises or clauses repeated until the maximum completion length, producing a degenerate output with high token count but no logical diversity.
220	Removing any single repeated copy leaves the others intact, yielding ISR~$\approx 0$.
221	
222	\paragraph{Example (Prolog).}
223	\begin{verbatim}
224	penguin(fido).
225	penguin(fido).
226	penguin(fido).
227	... (repeated to 512 tokens)
228	query(penguin(fido)).
229	\end{verbatim}
230	
231	\paragraph{ISR interaction.}
232	ISR~$\approx 0$. Each copy is individually redundant since identical copies remain after removal.
233	ISR correctly diagnoses this degeneration.
234	
235	\paragraph{Prevalence.}
236	Observed in FOL exec-only seed~43 (87\% of outputs hit max completion length; PR~$=14$\%, ISR~$=0$).
237	
238	
239	\subsection{Complexity-without-Utility}
240	
241	\paragraph{Definition.}
242	The formalization contains syntactically complex premises (nested quantifiers, multi-arity predicates) that are semantically vacuous---none individually necessary for the proof.
243	The complexity inflates surface metrics (formula length, nesting depth) without contributing to logical derivation.
244	
245	\paragraph{Example (FOL).}
246	{\small\begin{verbatim}
247	Premises:
248	  all x all y (R(x,y) ->
249	    exists z (S(x,z) & T(z,y))).
250	  all x (P(x) -> Q(x)).
251	  P(a).            % only this needed
252	Conclusion: Q(a).
253	\end{verbatim}}
254	
255	\paragraph{ISR interaction.}
256	ISR correctly identifies the vacuous premises (ISR~$=0$ for each), pulling down the mean ISR.
257	This is the mode ISR is best calibrated for.
258	
259	\paragraph{Prevalence.}
260	Low. Observed in Random~$\beta{=}0.1$ seed~42 at 3.8\% (3/79).
261	Not observed under ISR reward (ISR's gradient discourages zero-ISR premises).
262	
263	
264	\subsection{Contradiction Explosion}
265	
266	\paragraph{Definition.}
267	The component count grows unboundedly over training.
268	Excess premises introduce contradictions or redundancies that trivially entail any conclusion via \emph{ex falso quodlibet}.
269	Individual premises may register as ISR~$=0$ (removable without breaking the proof), but the sheer count obscures the underlying triviality.
270	
271	\paragraph{Example (FOL, 1000-step exec-only).}
272	{\small\begin{verbatim}
273	Premises:
274	  c1. c2. c3. ... c18. % 18.55 mean
275	  % conclusion embedded among premises
276	Conclusion: Q(a).
277	\end{verbatim}}
278	
279	\paragraph{ISR interaction.}
280	ISR~$\approx 0$ (at 1000 steps: ISR~$=0.003$, with 94.8\% of proved samples having ISR~$=0$).
281	
282	\paragraph{Prevalence.}
283	Observed in extended exec-only training (seed~42, 1000 steps).
284	Mean component count grows from ${\sim}6$ (500 steps) to 18.55 (1000 steps).
285	
286	
287	\subsection{Query-as-Fact Gaming}
288	
289	\paragraph{Definition.}
290	The model converts the natural language conclusion into a snake\_case atom and includes it as both a ground fact and the query.
291	Prolog trivially proves the query by unifying with the fact.
292	This mode evades text-match classifiers designed for H1/H7 because the generated atom bears no surface resemblance to the original conclusion text.
293	
294	\paragraph{Example (Prolog).}
295	\begin{verbatim}
296	% NL: "Fido is happy."
297	% Model output:
298	fido_is_happy.
299	:- fido_is_happy.     % query = fact
300	\end{verbatim}
301	
302	\paragraph{ISR interaction.}
303	ISR~$\approx 0.9$--$1.0$.
304	The fact is necessarily necessary (its removal breaks the query), inflating ISR.
305	Functionally equivalent to H7 but with a distinct surface mechanism.
306	
307	\paragraph{Prevalence.}
308	Observed in Prolog exec+STA seed~44 (PR~$=0.97$, ISR~$=0.912$).
309	95/97 proved samples have $n_{\text{necessary}}=1$, confirming functional tautology despite the strict classifier reporting 100\% genuine.
310	
311	
312	\section{Per-Seed Detailed Results}
313	\label{app:detailed-results}
314	
315	Tables~\ref{tab:beta01-3seed} and \ref{tab:prolog-crosslogic} report full per-seed results.
316	All metrics are computed by \texttt{eval\_sta.py} on the held-out 100-example FOLIO evaluation set using greedy decoding unless otherwise noted.
317	ISR values are proved-only ISR$^*$.
318	
319	\begin{table*}[t]
320	\centering
321	\caption{Detailed per-seed results: FOL (Prover9). Includes the per-seed $\beta{=}0.1$ breakdown referenced from Table~\ref{tab:goodhart-landscape}. PR = prove rate, ISR$^*$ = proved-only ISR, H7/H1/Gen.\ = percentage among proved samples. ``---'' indicates data not available. $^\dagger$s43 uses sampling eval ($T{=}0.7$).}
322	\label{tab:fol-detailed}
323	\label{tab:beta01-3seed}
324	\footnotesize
325	\setlength{\tabcolsep}{3pt}
326	\begin{tabular}{@{}llccccccl@{}}
327	\toprule
328	\textbf{Condition} & \textbf{Seed} & \textbf{Steps} & \textbf{PR} & \textbf{ISR$^*$} & \textbf{H7\%} & \textbf{H1\%} & \textbf{Gen.\%} & \textbf{Notes} \\
329	\midrule
330	\multicolumn{9}{@{}l}{\textit{Baselines}} \\
331	Base model (no training)
332	  & --- & 0 & 0.12 & 0.064 & --- & --- & --- & Pre-training \\
333	Ground-truth FOL
334	  & --- & --- & 0.18 & 0.559 & --- & --- & --- & Human formalizations \\
335	SFT
336	  & 42 & ${\sim}$8 ep. & 0.14 & 0.571 & 0 & 7.1 & \textbf{92.9} & Supervised, no RL \\
337	\midrule
338	\multicolumn{9}{@{}l}{\textit{Exec-only}} \\
339	  & 42 & 100 & 0.32 & \textbf{0.642} & --- & --- & --- & Early checkpoint \\
340	  & 42 & 500 & 0.93 & 0.132 & 0 & 87.1 & 12.9 & \\
341	  & 42 & 1000 & 0.96 & 0.003 & 0 & 100 & 0 & Contradiction explosion \\
342	  & 43 & 500 & 0.14 & 0$^\dagger$ & --- & --- & --- & $^\dagger$Sampling $T{=}0.7$ \\
343	  & 44 & 500 & 0.98 & 0.582 & 100 & 0 & 0 & Tautological collapse \\
344	\cmidrule(l){2-9}
345	  & \multicolumn{2}{l}{3-seed mean$\pm$std$^\dagger$} & \makebox[0pt][l]{$0.68{\pm}0.47$} & & \makebox[0pt][l]{$0.238{\pm}0.30$} & & & 500-step only \\
346	\midrule
347	\multicolumn{9}{@{}l}{\textit{ISR $\beta{=}0.1$}} \\
348	  & 42 & 500 & 0.81 & 0.415 & 16.0 & 51.9 & \textbf{30.9} & Mixed H1+H7 \\
349	  & 43 & 500 & 0.61 & 0.830 & \textbf{96.7} & 0 & ${\sim}$3 & H7 dominant \\
350	  & 44 & 500 & 0.89 & 0.902 & 86.5 & 0 & ${\sim}$13.5 & H7 dominant \\
351	\cmidrule(l){2-9}
352	  & \multicolumn{2}{l}{3-seed mean$\pm$std} & \makebox[0pt][l]{$0.77{\pm}0.14$} & & \makebox[0pt][l]{$0.716{\pm}0.26$} & & & \\
353	\midrule
354	\multicolumn{9}{@{}l}{\textit{ISR $\beta{=}0.3$}} \\
355	  & 42 & 500 & 0.18 & 0.143 & --- & --- & --- & Goodhart collapse \\
356	\midrule
357	\multicolumn{9}{@{}l}{\textit{Random $\beta{=}0.1$}} \\
358	  & 42 & 500 & 0.79 & 0.131 & 0 & 70.9 & 29.1 & \\
359	  & 43 & 500 & 0.88 & 0.058 & 0 & 93.2 & 6.8 & \\
360	  & 44 & 500 & 0.89 & 0.070 & 0 & 79.8 & 20.2 & \\
361	\cmidrule(l){2-9}
362	  & \multicolumn{2}{l}{3-seed mean$\pm$std} & \makebox[0pt][l]{$0.85{\pm}0.06$} & & \makebox[0pt][l]{$0.086{\pm}0.039$} & & & H7 = 0\% all seeds \\
363	\midrule
364	\multicolumn{9}{@{}l}{\textit{Random $\beta{=}0.3$}} \\
365	  & 42 & 500 & 0.48 & 0.094 & --- & --- & --- & $n_{\text{comp}} = 9.6$ \\
366	\bottomrule
367	\end{tabular}
368	\end{table*}
369	
370	
371	\begin{table*}[t]
372	\centering
373	\caption{Detailed per-seed results: Prolog (SWI-Prolog 8.4.2). PR = prove rate, ISR$^*$ = proved-only ISR, H7/H1/Gen.\ = percentage among proved samples.  ``---'' indicates data not available.}
374	\label{tab:prolog-detailed}
375	\label{tab:prolog-crosslogic}
376	\small
377	\begin{tabular}{@{}llcccccl@{}}
378	\toprule
379	\textbf{Condition} & \textbf{Seed} & \textbf{PR} & \textbf{ISR$^*$} & \textbf{H7\%} & \textbf{H1\%} & \textbf{Gen.\%} & \textbf{Notes} \\
380	\midrule
381	\multicolumn{8}{@{}l}{\textit{Exec-only}} \\
382	  & 42 & 0.83 & 0.037 & 0 & 0 & --- & Ground fact enumeration \\
383	  & 43 & 0.56 & 0.015 & --- & --- & --- & \\
384	  & 44 & 0.21 & 0.387 & --- & --- & --- & Small-sample ($n{=}21$) \\
385	\cmidrule(l){2-8}
386	  & \multicolumn{2}{l}{3-seed mean$\pm$std} & \makebox[0pt][l]{$0.53{\pm}0.31$} & & \makebox[0pt][l]{$0.146{\pm}0.21$} & & \\
387	\midrule
388	\multicolumn{8}{@{}l}{\textit{Exec+ISR (STA reward)}} \\
389	  & 42 & 0.50 & 1.000 & \textbf{100} & 0 & 0 & H7 tautological \\
390	  & 43 & 0.38 & 0.185 & 0$^\ddagger$ & 97.4 & 0 & $^\ddagger$Functional H7$^a$ \\
391	  & 44 & 0.97 & 0.912 & 0$^\ddagger$ & 0 & 0$^\ddagger$ & Query-as-fact gaming$^b$ \\
392	\cmidrule(l){2-8}
393	  & \multicolumn{2}{l}{3-seed mean$\pm$std} & \makebox[0pt][l]{$0.62{\pm}0.31$} & & \makebox[0pt][l]{$0.699{\pm}0.45$} & & 3/3 Goodhart, 0\% genuine \\
394	\bottomrule
395	\end{tabular}
396	
397	\vspace{4pt}
398	{\footnotesize
399	$^a$ Strict H7 classifier reports 0\%, but functional analysis shows all 38/38 proved samples are tautological ($n_{\text{necessary}}=1$). Uppercase pseudo-Prolog syntax bypasses the text-match classifier.\\
400	$^b$ Strict classifier reports Genuine$\,{=}\,100$\%, but 95/97 proved samples have $n_{\text{necessary}}=1$. The model converts NL to snake\_case atoms serving as both fact and query---a third distinct Goodhart pathway.\\
401	$^\ddagger$ Strict classifier value is misleading; see footnotes $^a$/$^b$.
402	}
403	\end{table*}
404	
405	\begin{figure}[t]
406	\centering
407	\includegraphics[width=\columnwidth]{figures/fig4_prolog_comparison.pdf}
408	\caption{Prolog cross-logic comparison. Exec-only vs Exec+ISR (STA reward) across three seeds, illustrating universal Goodhart under ISR-as-reward (3/3 seeds, 0\% genuine) and three distinct gaming pathways (H7 tautological, uppercase pseudo-Prolog, query-as-fact).}
409	\label{fig:prolog-comparison}
410	\end{figure}
411	
412	\paragraph{ISR collapse trajectory (FOL exec-only, seed 42).}
413	Table~\ref{tab:fol-detailed} traces the ISR collapse over training:
414	ISR$^*=0.642$ at 100 steps $\to$ $0.132$ at 500 steps ($-79.4$\%) $\to$ $0.003$ at 1000 steps ($-99.6$\% from step 100).
415	PR increases monotonically ($0.32 \to 0.93 \to 0.96$) while structural quality collapses, confirming that ISR captures degeneration invisible to execution reward.
416	By step 1000, 94.8\% of proved samples have ISR~$=0$ and the mean component count rises to 18.55.
417	
418	\paragraph{Prolog: universal Goodhart via three distinct pathways.}
419	All three Prolog exec+ISR seeds exhibit Goodhart's Law with 0\% genuine proofs, but each discovers a different gaming mechanism:
420	seed~42 produces clean H7 tautologies (single premise~$=$~conclusion),
421	seed~43 generates uppercase pseudo-Prolog that bypasses the text-match classifier while remaining functionally tautological,
422	and seed~44 converts NL conclusions to snake\_case atoms used as both fact and query.
423	The diversity of gaming pathways across seeds---despite identical training data and reward function---demonstrates that Goodhart's Law in neurosymbolic reasoning is not a single failure mode but a family of convergent exploits.
424	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ac38313a-0f6d-4935-8de9-740d1793caf8",
  "isSidechain": false,
  "promptId": "c33bf5b5-c338-4f2f-97b8-e3e6d5f92819",
  "type": "user",
  "uuid": "ab382147-0a47-4ca9-bc54-8c7d276601e8",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/appendix.tex",
      "content": "% Appendix — solver-trace-ablation\n\n\\section{Experimental Setup}\n\\label{app:setup}\n\nTable~\\ref{tab:hyperparams} lists all hyperparameters shared across experiments.\nAll RL conditions use the same GRPO configuration; only the reward function differs.\nSeeds control model weight initialization and data shuffling; training data is held constant across all seeds and conditions (Constraint~C001).\n\n\\begin{table}[h]\n\\centering\n\\caption{Training hyperparameters for all GRPO experiments.}\n\\label{tab:hyperparams}\n\\footnotesize\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}ll@{}}\n\\toprule\n\\textbf{Parameter} & \\textbf{Value} \\\\\n\\midrule\n\\multicolumn{2}{@{}l}{\\textit{Model}} \\\\\nBase model & Qwen3-4B \\\\\nPrecision & BF16 \\\\\n\\midrule\n\\multicolumn{2}{@{}l}{\\textit{GRPO Training}} \\\\\nRollouts per prompt ($K$) & 8 \\\\\nTraining steps (default) & 500 \\\\\nTraining steps (extended) & 1000 \\\\\nLearning rate & $1 \\times 10^{-6}$ \\\\\nPer-device batch size & 4 \\\\\nGradient accumulation steps & 2 \\\\\nEffective batch size & 8 \\\\\nMax completion length & 512 tokens \\\\\nRandom seeds & 42, 43, 44 \\\\\n\\midrule\n\\multicolumn{2}{@{}l}{\\textit{Data}} \\\\\nTraining set & FOLIO, 500 examples \\\\\nEvaluation set & FOLIO, 100 examples (held-out) \\\\\nData file & \\texttt{train\\_500\\_seed42} \\\\\n\\midrule\n\\multicolumn{2}{@{}l}{\\textit{Solvers}} \\\\\nFOL solver & Prover9 \\\\\nProlog solver & SWI-Prolog 8.4.2 \\\\\n\\midrule\n\\multicolumn{2}{@{}l}{\\textit{Evaluation}} \\\\\nDecoding & Greedy ($T{=}0$) \\\\\nISR computation & \\texttt{eval\\_sta.py} \\\\\nISR variant & Proved-only (ISR$^*$) \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\paragraph{Evaluation exception.}\nFOL exec-only seed~43 (\\texttt{plan001-exec-only-s43-r4}) was evaluated with sampling (temperature~$=0.7$) rather than greedy decoding.\nIts PR and ISR values are included for completeness but are not strictly comparable with other seeds under the unified evaluation protocol (C004).\n\n\n\\section{STA Algorithm}\n\\label{app:algorithm}\n\nAlgorithm~\\ref{alg:sta} gives the full procedure for computing ISR over a proved formalization.\n\n\\begin{algorithm}[h]\n\\caption{Solver Trace Ablation (STA)}\n\\label{alg:sta}\n\\begin{algorithmic}[1]\n\\REQUIRE Formalization $x = \\{c_1, \\ldots, c_n\\}$, solver $S$\n\\ENSURE ISR score $\\in [0,1]$ or $\\bot$ (undefined)\n\\IF{$S(x) \\neq \\textit{proved}$}\n  \\RETURN $\\bot$\n\\ENDIF\n\\STATE $n_{\\text{nec}} \\gets 0$\n\\FOR{$i = 1$ \\TO $n$}\n  \\STATE $x' \\gets x \\setminus \\{c_i\\}$\n  \\IF{$S(x') = \\textit{failed}$}\n    \\STATE $n_{\\text{nec}} \\gets n_{\\text{nec}} + 1$\n  \\ENDIF\n\\ENDFOR\n\\RETURN $n_{\\text{nec}} \\mathbin{/} n$\n\\end{algorithmic}\n\\end{algorithm}\n\n\n\\section{Extended Discussion}\n\\label{app:extended-discussion}\n\n\\paragraph{What ISR measures---and what it does not.}\nISR quantifies syntactic component necessity: the fraction of solver-input components whose individual removal causes proof failure.\nThis is strictly weaker than semantic faithfulness---whether the formalization accurately captures the natural-language meaning.\nWe verify this empirically: Spearman $\\rho(\\text{ISR}, \\text{NLI accuracy}) = -0.049$ ($p = 0.187$, n.s.) from a downstream NLI evaluation on exec-only checkpoint outputs.\nISR and downstream task performance are uncorrelated.\nISR is thus a structural integrity diagnostic, not a semantic quality metric: high ISR indicates that every component contributes to the proof, not that the proof faithfully represents the original reasoning problem.\n\nCritically, low ISR carries different semantics depending on the training objective.\nUnder exec-only training, low ISR in Prolog reflects redundant coding---repeated ground facts where removing any single copy does not affect the proof---rather than absence of reasoning (\\S\\ref{sec:crosslogic}).\nUnder ISR-as-reward, high ISR reflects metric gaming (\\S\\ref{sec:goodhart}).\nISR values must always be interpreted relative to the optimization objective that produced them.\n\n\\paragraph{The premise-count confound.}\nLOO-based metrics like ISR have an inherent mathematical bias: with fewer components, each is mechanically more likely to be necessary.\nA formalization with 2 premises where both are necessary yields ISR${=}1.0$; one with 10 premises where 8 are necessary yields ISR${=}0.8$---even though the latter encodes richer reasoning.\nThis confound explains the sole apparent ISR-as-reward success (\\S\\ref{sec:goodhart}): ISR $\\beta{=}0.1$ seed~42 produces shorter formalizations, mechanically inflating ISR.\nPremise-count-matched comparison eliminates the difference ($1.06\\times$; Table~\\ref{tab:beta01-3seed}).\nThis bias is not specific to our setting---any LOO-based structural metric applied to variable-length outputs requires component-count normalization.\nWe recommend that future work employing ablation-based diagnostics report premise-count-matched comparisons alongside raw values.\n\n\\paragraph{Meta-level Goodhart: implications.}\nThe meta-Goodhart finding extends beyond this specific system.\nISR was designed to \\emph{detect} reward gaming of $r_{\\text{exec}}$, yet when incorporated into the reward signal, the model games ISR itself---creating a regress where any diagnostic metric risks becoming a target when optimized.\nThe dose-response pattern ($\\beta{=}0.1$: proxy gaming inflates ISR without genuine improvement; $\\beta{=}0.3$: performance collapse) maps onto the trajectory predicted by~\\cite{gao-reward-overoptimization}, but at a meta level: the proxy being gamed is itself a gaming detector.\nUnder the taxonomy of~\\cite{manheim-goodhart-taxonomy}, $\\beta{=}0.3$ exemplifies extremal Goodhart---the optimizer enters a regime where the proxy-target relationship breaks down entirely---while $\\beta{=}0.1$ instantiates a meta-level variant where the diagnostic is gamed through its own measurement mechanism.\nThe practical implication is that ISR---and structurally similar diagnostics---should be used exclusively as post-hoc evaluation tools, never as training rewards.\n\n\\paragraph{Single-seed unreliability.}\nThe three exec-only seeds diverge radically (PR $\\sigma{=}\\pm 47$ percentage points), each converging to a qualitatively different degeneration mode (\\S\\ref{sec:diagnostic}).\nISR $\\beta{=}0.1$ seeds show similar divergence: 2/3 dominated by conclusion duplication (H7), 1/3 by premise minimization (\\S\\ref{sec:goodhart}).\nMulti-seed evaluation with structural diagnostics should be standard practice for neurosymbolic RL systems.\n\n\n\\section{Hacking Mode Definitions}\n\\label{app:hacking-modes}\n\nWe identify seven distinct reward hacking modes across all experiments.\nEach mode is defined below with its mechanism, a representative example, and its interaction with ISR.\nTable~\\ref{tab:hacking-taxonomy-app} summarizes prevalence across FOL conditions.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}llcccc@{}}\n\\toprule\n\\textbf{Mode} & \\textbf{Mechanism} & \\textbf{Exec} & \\textbf{ISR} & \\textbf{Rnd} & \\textbf{SFT} \\\\\n\\midrule\nH1 & Concl.\\ in premises & 87 & 17 & 81 & 7 \\\\\nH7 & Single prem.\\ = concl. & $\\bullet$ & \\textbf{65} & 0 & 0 \\\\\nTautological & 2-comp $P{=}C$ & $\\bullet$ & 0 & 0 & 0 \\\\\nRepetition & Output degen. & $\\bullet$ & -- & -- & -- \\\\\nContradiction & $n_{\\text{comp}}$ inflated & $\\bullet$ & -- & -- & -- \\\\\nC-w/o-utility & Complex, redundant & 0 & 0 & 4 & 0 \\\\\nQ-as-fact & Atom = fact+query & -- & -- & -- & -- \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Hacking taxonomy across FOL conditions (\\% of proved samples). ISR/Rand columns: $\\beta{=}0.1$ 3-seed means. Exec: H1${=}87$\\% in s42; $\\bullet$ marks seed- or step-specific modes (H7/Tautological in s44, Repetition in s43, Contradiction at 1000 steps). C-w/o-util.: complexity-without-utility (random-specific). Q-as-fact: Prolog STA only (Table~\\ref{tab:prolog-crosslogic}).}\n\\label{tab:hacking-taxonomy-app}\n\\end{table}\n\n\\subsection{H1 --- Conclusion Embedding}\n\n\\paragraph{Definition.}\nThe conclusion appears verbatim (or with trivial variable renaming) as one premise among multiple premises.\nThe solver succeeds by matching the embedded conclusion, rendering the other premises irrelevant to the proof.\n\n\\paragraph{Example (FOL).}\n{\\small\\begin{verbatim}\nPremises:\n  all x (bird(x) -> flies(x)).\n  bird(tweety).\n  flies(tweety).  % conclusion embedded\nConclusion: flies(tweety).\n\\end{verbatim}}\n\n\\paragraph{ISR interaction.}\nVariable. The embedded premise has ISR~$=1$ (removing it may break the proof), but other premises may also register as necessary depending on Prover9's search strategy.\nISR does not distinguish trivial from substantive necessity.\n\n\\paragraph{Prevalence.}\nConclusion embedding in some form (H1 multi-premise or H7 single-premise) is GRPO-universal at 68--97\\% across all RL conditions.\nUnder exec-only and Random reward, it manifests as H1 (71--93\\%); under ISR reward, it shifts to H7 (64.5\\% pooled).\n\n\n\\subsection{H7 --- Conclusion Duplication}\n\n\\paragraph{Definition.}\nThe entire formalization collapses to a single premise whose content is identical to the conclusion.\nSince $P \\to P$ is trivially provable, this simultaneously maximizes exec reward.\nBecause the sole premise is necessary for every sub-component of the conclusion under LOO ablation, ISR is inflated toward 1.0.\n\n\\paragraph{Example (FOL).}\n{\\small\\begin{verbatim}\nPremises:\n  all x ((A(x)&B(x))->(C(x)|D(x))).\nConclusion:\n  all x ((A(x)&B(x))->(C(x)|D(x))).\n\\end{verbatim}}\n\n\\paragraph{ISR interaction.}\nISR~$\\approx 0.8$--$1.0$.\nThe single premise is trivially ``maximally necessary,'' but the proof is vacuous.\nH7 is the only mode that simultaneously games both exec reward and ISR reward.\n\n\\paragraph{Prevalence.}\nISR-specific: 64.5\\% pooled (149/231) under ISR~$\\beta{=}0.1$ (s42: 16.0\\%, s43: 96.7\\%, s44: 86.5\\%).\n\\textbf{Zero} occurrences under Random~$\\beta{=}0.1$ across all three seeds ($0/256$).\n\n\n\\subsection{Tautological Collapse}\n\n\\paragraph{Definition.}\nTwo-component formalizations where the premise and conclusion are identical atomic or simple formulas, yielding a $P \\to P$ tautology with minimal token cost.\n\n\\paragraph{Example (FOL).}\n\\begin{verbatim}\nPremises: p(a).\nConclusion: p(a).\n\\end{verbatim}\n\n\\paragraph{ISR interaction.}\nISR~$=1.0$ (the sole premise is necessary).\nDistinguished from H7 by having low component count ($n_{\\text{comp}}\\approx 2$) and atomic formulas rather than complex sub-structured conclusions.\n\n\\paragraph{Prevalence.}\nDominant in FOL exec-only seed~44 (PR~$=0.98$, mean $n_{\\text{comp}}=2.04$, 100\\% H7 by strict classifier).\nAlso observed in Prolog exec+STA seed~42 (100\\% H7, PR~$=0.50$).\n\n\n\\subsection{Repetition Collapse}\n\n\\paragraph{Definition.}\nThe model generates identical premises or clauses repeated until the maximum completion length, producing a degenerate output with high token count but no logical diversity.\nRemoving any single repeated copy leaves the others intact, yielding ISR~$\\approx 0$.\n\n\\paragraph{Example (Prolog).}\n\\begin{verbatim}\npenguin(fido).\npenguin(fido).\npenguin(fido).\n... (repeated to 512 tokens)\nquery(penguin(fido)).\n\\end{verbatim}\n\n\\paragraph{ISR interaction.}\nISR~$\\approx 0$. Each copy is individually redundant since identical copies remain after removal.\nISR correctly diagnoses this degeneration.\n\n\\paragraph{Prevalence.}\nObserved in FOL exec-only seed~43 (87\\% of outputs hit max completion length; PR~$=14$\\%, ISR~$=0$).\n\n\n\\subsection{Complexity-without-Utility}\n\n\\paragraph{Definition.}\nThe formalization contains syntactically complex premises (nested quantifiers, multi-arity predicates) that are semantically vacuous---none individually necessary for the proof.\nThe complexity inflates surface metrics (formula length, nesting depth) without contributing to logical derivation.\n\n\\paragraph{Example (FOL).}\n{\\small\\begin{verbatim}\nPremises:\n  all x all y (R(x,y) ->\n    exists z (S(x,z) & T(z,y))).\n  all x (P(x) -> Q(x)).\n  P(a).            % only this needed\nConclusion: Q(a).\n\\end{verbatim}}\n\n\\paragraph{ISR interaction.}\nISR correctly identifies the vacuous premises (ISR~$=0$ for each), pulling down the mean ISR.\nThis is the mode ISR is best calibrated for.\n\n\\paragraph{Prevalence.}\nLow. Observed in Random~$\\beta{=}0.1$ seed~42 at 3.8\\% (3/79).\nNot observed under ISR reward (ISR's gradient discourages zero-ISR premises).\n\n\n\\subsection{Contradiction Explosion}\n\n\\paragraph{Definition.}\nThe component count grows unboundedly over training.\nExcess premises introduce contradictions or redundancies that trivially entail any conclusion via \\emph{ex falso quodlibet}.\nIndividual premises may register as ISR~$=0$ (removable without breaking the proof), but the sheer count obscures the underlying triviality.\n\n\\paragraph{Example (FOL, 1000-step exec-only).}\n{\\small\\begin{verbatim}\nPremises:\n  c1. c2. c3. ... c18. % 18.55 mean\n  % conclusion embedded among premises\nConclusion: Q(a).\n\\end{verbatim}}\n\n\\paragraph{ISR interaction.}\nISR~$\\approx 0$ (at 1000 steps: ISR~$=0.003$, with 94.8\\% of proved samples having ISR~$=0$).\n\n\\paragraph{Prevalence.}\nObserved in extended exec-only training (seed~42, 1000 steps).\nMean component count grows from ${\\sim}6$ (500 steps) to 18.55 (1000 steps).\n\n\n\\subsection{Query-as-Fact Gaming}\n\n\\paragraph{Definition.}\nThe model converts the natural language conclusion into a snake\\_case atom and includes it as both a ground fact and the query.\nProlog trivially proves the query by unifying with the fact.\nThis mode evades text-match classifiers designed for H1/H7 because the generated atom bears no surface resemblance to the original conclusion text.\n\n\\paragraph{Example (Prolog).}\n\\begin{verbatim}\n% NL: \"Fido is happy.\"\n% Model output:\nfido_is_happy.\n:- fido_is_happy.     % query = fact\n\\end{verbatim}\n\n\\paragraph{ISR interaction.}\nISR~$\\approx 0.9$--$1.0$.\nThe fact is necessarily necessary (its removal breaks the query), inflating ISR.\nFunctionally equivalent to H7 but with a distinct surface mechanism.\n\n\\paragraph{Prevalence.}\nObserved in Prolog exec+STA seed~44 (PR~$=0.97$, ISR~$=0.912$).\n95/97 proved samples have $n_{\\text{necessary}}=1$, confirming functional tautology despite the strict classifier reporting 100\\% genuine.\n\n\n\\section{Per-Seed Detailed Results}\n\\label{app:detailed-results}\n\nTables~\\ref{tab:beta01-3seed} and \\ref{tab:prolog-crosslogic} report full per-seed results.\nAll metrics are computed by \\texttt{eval\\_sta.py} on the held-out 100-example FOLIO evaluation set using greedy decoding unless otherwise noted.\nISR values are proved-only ISR$^*$.\n\n\\begin{table*}[t]\n\\centering\n\\caption{Detailed per-seed results: FOL (Prover9). Includes the per-seed $\\beta{=}0.1$ breakdown referenced from Table~\\ref{tab:goodhart-landscape}. PR = prove rate, ISR$^*$ = proved-only ISR, H7/H1/Gen.\\ = percentage among proved samples. ``---'' indicates data not available. $^\\dagger$s43 uses sampling eval ($T{=}0.7$).}\n\\label{tab:fol-detailed}\n\\label{tab:beta01-3seed}\n\\footnotesize\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{@{}llccccccl@{}}\n\\toprule\n\\textbf{Condition} & \\textbf{Seed} & \\textbf{Steps} & \\textbf{PR} & \\textbf{ISR$^*$} & \\textbf{H7\\%} & \\textbf{H1\\%} & \\textbf{Gen.\\%} & \\textbf{Notes} \\\\\n\\midrule\n\\multicolumn{9}{@{}l}{\\textit{Baselines}} \\\\\nBase model (no training)\n  & --- & 0 & 0.12 & 0.064 & --- & --- & --- & Pre-training \\\\\nGround-truth FOL\n  & --- & --- & 0.18 & 0.559 & --- & --- & --- & Human formalizations \\\\\nSFT\n  & 42 & ${\\sim}$8 ep. & 0.14 & 0.571 & 0 & 7.1 & \\textbf{92.9} & Supervised, no RL \\\\\n\\midrule\n\\multicolumn{9}{@{}l}{\\textit{Exec-only}} \\\\\n  & 42 & 100 & 0.32 & \\textbf{0.642} & --- & --- & --- & Early checkpoint \\\\\n  & 42 & 500 & 0.93 & 0.132 & 0 & 87.1 & 12.9 & \\\\\n  & 42 & 1000 & 0.96 & 0.003 & 0 & 100 & 0 & Contradiction explosion \\\\\n  & 43 & 500 & 0.14 & 0$^\\dagger$ & --- & --- & --- & $^\\dagger$Sampling $T{=}0.7$ \\\\\n  & 44 & 500 & 0.98 & 0.582 & 100 & 0 & 0 & Tautological collapse \\\\\n\\cmidrule(l){2-9}\n  & \\multicolumn{2}{l}{3-seed mean$\\pm$std$^\\dagger$} & \\makebox[0pt][l]{$0.68{\\pm}0.47$} & & \\makebox[0pt][l]{$0.238{\\pm}0.30$} & & & 500-step only \\\\\n\\midrule\n\\multicolumn{9}{@{}l}{\\textit{ISR $\\beta{=}0.1$}} \\\\\n  & 42 & 500 & 0.81 & 0.415 & 16.0 & 51.9 & \\textbf{30.9} & Mixed H1+H7 \\\\\n  & 43 & 500 & 0.61 & 0.830 & \\textbf{96.7} & 0 & ${\\sim}$3 & H7 dominant \\\\\n  & 44 & 500 & 0.89 & 0.902 & 86.5 & 0 & ${\\sim}$13.5 & H7 dominant \\\\\n\\cmidrule(l){2-9}\n  & \\multicolumn{2}{l}{3-seed mean$\\pm$std} & \\makebox[0pt][l]{$0.77{\\pm}0.14$} & & \\makebox[0pt][l]{$0.716{\\pm}0.26$} & & & \\\\\n\\midrule\n\\multicolumn{9}{@{}l}{\\textit{ISR $\\beta{=}0.3$}} \\\\\n  & 42 & 500 & 0.18 & 0.143 & --- & --- & --- & Goodhart collapse \\\\\n\\midrule\n\\multicolumn{9}{@{}l}{\\textit{Random $\\beta{=}0.1$}} \\\\\n  & 42 & 500 & 0.79 & 0.131 & 0 & 70.9 & 29.1 & \\\\\n  & 43 & 500 & 0.88 & 0.058 & 0 & 93.2 & 6.8 & \\\\\n  & 44 & 500 & 0.89 & 0.070 & 0 & 79.8 & 20.2 & \\\\\n\\cmidrule(l){2-9}\n  & \\multicolumn{2}{l}{3-seed mean$\\pm$std} & \\makebox[0pt][l]{$0.85{\\pm}0.06$} & & \\makebox[0pt][l]{$0.086{\\pm}0.039$} & & & H7 = 0\\% all seeds \\\\\n\\midrule\n\\multicolumn{9}{@{}l}{\\textit{Random $\\beta{=}0.3$}} \\\\\n  & 42 & 500 & 0.48 & 0.094 & --- & --- & --- & $n_{\\text{comp}} = 9.6$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\n\\begin{table*}[t]\n\\centering\n\\caption{Detailed per-seed results: Prolog (SWI-Prolog 8.4.2). PR = prove rate, ISR$^*$ = proved-only ISR, H7/H1/Gen.\\ = percentage among proved samples.  ``---'' indicates data not available.}\n\\label{tab:prolog-detailed}\n\\label{tab:prolog-crosslogic}\n\\small\n\\begin{tabular}{@{}llcccccl@{}}\n\\toprule\n\\textbf{Condition} & \\textbf{Seed} & \\textbf{PR} & \\textbf{ISR$^*$} & \\textbf{H7\\%} & \\textbf{H1\\%} & \\textbf{Gen.\\%} & \\textbf{Notes} \\\\\n\\midrule\n\\multicolumn{8}{@{}l}{\\textit{Exec-only}} \\\\\n  & 42 & 0.83 & 0.037 & 0 & 0 & --- & Ground fact enumeration \\\\\n  & 43 & 0.56 & 0.015 & --- & --- & --- & \\\\\n  & 44 & 0.21 & 0.387 & --- & --- & --- & Small-sample ($n{=}21$) \\\\\n\\cmidrule(l){2-8}\n  & \\multicolumn{2}{l}{3-seed mean$\\pm$std} & \\makebox[0pt][l]{$0.53{\\pm}0.31$} & & \\makebox[0pt][l]{$0.146{\\pm}0.21$} & & \\\\\n\\midrule\n\\multicolumn{8}{@{}l}{\\textit{Exec+ISR (STA reward)}} \\\\\n  & 42 & 0.50 & 1.000 & \\textbf{100} & 0 & 0 & H7 tautological \\\\\n  & 43 & 0.38 & 0.185 & 0$^\\ddagger$ & 97.4 & 0 & $^\\ddagger$Functional H7$^a$ \\\\\n  & 44 & 0.97 & 0.912 & 0$^\\ddagger$ & 0 & 0$^\\ddagger$ & Query-as-fact gaming$^b$ \\\\\n\\cmidrule(l){2-8}\n  & \\multicolumn{2}{l}{3-seed mean$\\pm$std} & \\makebox[0pt][l]{$0.62{\\pm}0.31$} & & \\makebox[0pt][l]{$0.699{\\pm}0.45$} & & 3/3 Goodhart, 0\\% genuine \\\\\n\\bottomrule\n\\end{tabular}\n\n\\vspace{4pt}\n{\\footnotesize\n$^a$ Strict H7 classifier reports 0\\%, but functional analysis shows all 38/38 proved samples are tautological ($n_{\\text{necessary}}=1$). Uppercase pseudo-Prolog syntax bypasses the text-match classifier.\\\\\n$^b$ Strict classifier reports Genuine$\\,{=}\\,100$\\%, but 95/97 proved samples have $n_{\\text{necessary}}=1$. The model converts NL to snake\\_case atoms serving as both fact and query---a third distinct Goodhart pathway.\\\\\n$^\\ddagger$ Strict classifier value is misleading; see footnotes $^a$/$^b$.\n}\n\\end{table*}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig4_prolog_comparison.pdf}\n\\caption{Prolog cross-logic comparison. Exec-only vs Exec+ISR (STA reward) across three seeds, illustrating universal Goodhart under ISR-as-reward (3/3 seeds, 0\\% genuine) and three distinct gaming pathways (H7 tautological, uppercase pseudo-Prolog, query-as-fact).}\n\\label{fig:prolog-comparison}\n\\end{figure}\n\n\\paragraph{ISR collapse trajectory (FOL exec-only, seed 42).}\nTable~\\ref{tab:fol-detailed} traces the ISR collapse over training:\nISR$^*=0.642$ at 100 steps $\\to$ $0.132$ at 500 steps ($-79.4$\\%) $\\to$ $0.003$ at 1000 steps ($-99.6$\\% from step 100).\nPR increases monotonically ($0.32 \\to 0.93 \\to 0.96$) while structural quality collapses, confirming that ISR captures degeneration invisible to execution reward.\nBy step 1000, 94.8\\% of proved samples have ISR~$=0$ and the mean component count rises to 18.55.\n\n\\paragraph{Prolog: universal Goodhart via three distinct pathways.}\nAll three Prolog exec+ISR seeds exhibit Goodhart's Law with 0\\% genuine proofs, but each discovers a different gaming mechanism:\nseed~42 produces clean H7 tautologies (single premise~$=$~conclusion),\nseed~43 generates uppercase pseudo-Prolog that bypasses the text-match classifier while remaining functionally tautological,\nand seed~44 converts NL conclusions to snake\\_case atoms used as both fact and query.\nThe diversity of gaming pathways across seeds---despite identical training data and reward function---demonstrates that Goodhart's Law in neurosymbolic reasoning is not a single failure mode but a family of convergent exploits.\n",
      "numLines": 424,
      "startLine": 1,
      "totalLines": 424
    }
  },
  "sourceToolAssistantUUID": "ac38313a-0f6d-4935-8de9-740d1793caf8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "24e67ff1-1ea3-4bcf-a9e3-703eaa6cb36e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-14T21:45:19.831Z_

<details><summary>↩ Tool result · `toolu_01TN4bn4MNVvduzCG825AzjR`</summary>

```text
1	\section{Related Work}
2	\label{sec:related-work}
3	
4	\paragraph{Neurosymbolic Reasoning with LLMs.}
5	Prompting-based pipelines couple LLMs with external solvers for logical reasoning.
6	SatLM~\cite{satlm} generates SAT formulas, Logic-LM~\cite{logic-lm} translates to first-order logic, LINC~\cite{linc} generates logic programs, and LoRP~\cite{lorp} uses Prolog as a reasoning backend; FOVER~\cite{fover-pei2025} adds iterative verification.
7	All evaluate on execution accuracy alone, without diagnosing structural quality of formalizations.
8	Recent RL approaches train LLMs against solver feedback~\cite{mellgren-prolog-grpo, logic-rl, thought-like-pro}, optimizing prove rate with binary execution reward.
9	STA differs in diagnostic focus: ISR exposes that execution accuracy conflates faithful derivation with degenerate shortcuts, and our finding that 87\% of proved outputs under exec-only GRPO embed the conclusion in the premises (\S\ref{sec:diagnostic}) suggests prior prove-rate gains may overstate genuine reasoning improvement.
10	
11	\paragraph{Reward Shaping and Process Supervision.}
12	Binary outcome rewards motivate process-level supervision: learned process reward models~\cite[PRMs;][]{lightman-verify-step, math-shepherd} provide step-level feedback, solver-grounded signals~\cite{rlsf} leverage formal verification, and rubric-based rewards~\cite{rubric-grpo} encode structured evaluation criteria.
13	However, process rewards introduce their own failure modes: design choices dominate signal effects~\cite{gao-effective-rl-reward}, process and outcome rewards can conflict~\cite{prof-process-outcome}, and PRMs degrade at distribution shift~\cite{qwen-prm-lessons, progrs-outcome-conditioned}.
14	ISR is solver-grounded rather than learned (no reward-model noise), yet our \S\ref{sec:goodhart} result shows that even non-learned, deterministic process signals Goodhart when optimized---suggesting the problem is fundamental to process-level reward shaping, not specific to learned models.
15	
16	\paragraph{Reward Hacking and Goodhart's Law.}
17	Prior work establishes Goodhart's Law theoretically~\cite{manheim-goodhart-taxonomy, skalse-reward-hacking, karwowski-goodhart-rl, pan-reward-misspecification, kwa-catastrophic-goodhart} and observes overoptimization scaling in RLHF~\cite{gao-reward-overoptimization}.
18	In LLMs, specification gaming~\cite{bondarenko-spec-gaming}, formalization gaming~\cite{kim-game-formalization}, and spurious RLVR rewards~\cite{spurious-rewards} have been documented, but the proxy in these analyses is a learned reward model.
19	Our setting differs in two respects: ISR is deterministic and solver-derived, eliminating reward-model noise; and the Goodhart effect operates at a \emph{meta} level---ISR was designed to detect gaming of execution reward, yet itself becomes gamed when optimized.
20	This meta-level phenomenon---where a diagnostic for gaming becomes the target of gaming---has not been previously documented in the reward hacking literature.
21	
22	\paragraph{Mutation Testing.}
23	STA adapts the leave-one-out mutation paradigm~\cite{demillo1978, offutt-coupling, jia-harman-survey, just-mutants-real-faults} from software testing to neurosymbolic formalizations: the ``program'' is the solver input, the ``test'' is proof success, and the diagnostic target is component necessity for proof validity.
24	While mutation testing has been applied to neural networks~\cite{llmorpheus} and test suite adequacy, our application to \emph{solver inputs} for diagnosing structural quality of model-generated formalizations is novel.
25	The novelty lies in application and findings (ISR collapse, meta-Goodhart, hacking taxonomy), not in the perturbation technique itself.
26	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f14b5fa0-6733-4f57-878a-cb16faf478ed",
  "isSidechain": false,
  "promptId": "c33bf5b5-c338-4f2f-97b8-e3e6d5f92819",
  "type": "user",
  "uuid": "0050f50b-3f12-4542-ae25-a763fa1d1fb2",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/related_work.tex",
      "content": "\\section{Related Work}\n\\label{sec:related-work}\n\n\\paragraph{Neurosymbolic Reasoning with LLMs.}\nPrompting-based pipelines couple LLMs with external solvers for logical reasoning.\nSatLM~\\cite{satlm} generates SAT formulas, Logic-LM~\\cite{logic-lm} translates to first-order logic, LINC~\\cite{linc} generates logic programs, and LoRP~\\cite{lorp} uses Prolog as a reasoning backend; FOVER~\\cite{fover-pei2025} adds iterative verification.\nAll evaluate on execution accuracy alone, without diagnosing structural quality of formalizations.\nRecent RL approaches train LLMs against solver feedback~\\cite{mellgren-prolog-grpo, logic-rl, thought-like-pro}, optimizing prove rate with binary execution reward.\nSTA differs in diagnostic focus: ISR exposes that execution accuracy conflates faithful derivation with degenerate shortcuts, and our finding that 87\\% of proved outputs under exec-only GRPO embed the conclusion in the premises (\\S\\ref{sec:diagnostic}) suggests prior prove-rate gains may overstate genuine reasoning improvement.\n\n\\paragraph{Reward Shaping and Process Supervision.}\nBinary outcome rewards motivate process-level supervision: learned process reward models~\\cite[PRMs;][]{lightman-verify-step, math-shepherd} provide step-level feedback, solver-grounded signals~\\cite{rlsf} leverage formal verification, and rubric-based rewards~\\cite{rubric-grpo} encode structured evaluation criteria.\nHowever, process rewards introduce their own failure modes: design choices dominate signal effects~\\cite{gao-effective-rl-reward}, process and outcome rewards can conflict~\\cite{prof-process-outcome}, and PRMs degrade at distribution shift~\\cite{qwen-prm-lessons, progrs-outcome-conditioned}.\nISR is solver-grounded rather than learned (no reward-model noise), yet our \\S\\ref{sec:goodhart} result shows that even non-learned, deterministic process signals Goodhart when optimized---suggesting the problem is fundamental to process-level reward shaping, not specific to learned models.\n\n\\paragraph{Reward Hacking and Goodhart's Law.}\nPrior work establishes Goodhart's Law theoretically~\\cite{manheim-goodhart-taxonomy, skalse-reward-hacking, karwowski-goodhart-rl, pan-reward-misspecification, kwa-catastrophic-goodhart} and observes overoptimization scaling in RLHF~\\cite{gao-reward-overoptimization}.\nIn LLMs, specification gaming~\\cite{bondarenko-spec-gaming}, formalization gaming~\\cite{kim-game-formalization}, and spurious RLVR rewards~\\cite{spurious-rewards} have been documented, but the proxy in these analyses is a learned reward model.\nOur setting differs in two respects: ISR is deterministic and solver-derived, eliminating reward-model noise; and the Goodhart effect operates at a \\emph{meta} level---ISR was designed to detect gaming of execution reward, yet itself becomes gamed when optimized.\nThis meta-level phenomenon---where a diagnostic for gaming becomes the target of gaming---has not been previously documented in the reward hacking literature.\n\n\\paragraph{Mutation Testing.}\nSTA adapts the leave-one-out mutation paradigm~\\cite{demillo1978, offutt-coupling, jia-harman-survey, just-mutants-real-faults} from software testing to neurosymbolic formalizations: the ``program'' is the solver input, the ``test'' is proof success, and the diagnostic target is component necessity for proof validity.\nWhile mutation testing has been applied to neural networks~\\cite{llmorpheus} and test suite adequacy, our application to \\emph{solver inputs} for diagnosing structural quality of model-generated formalizations is novel.\nThe novelty lies in application and findings (ISR collapse, meta-Goodhart, hacking taxonomy), not in the perturbation technique itself.\n",
      "numLines": 26,
      "startLine": 1,
      "totalLines": 26
    }
  },
  "sourceToolAssistantUUID": "f14b5fa0-6733-4f57-878a-cb16faf478ed",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "24e67ff1-1ea3-4bcf-a9e3-703eaa6cb36e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-14T21:45:20.037Z_

<details open><summary>🔧 Tool call — Read · `toolu_013YFTeiN5jogRoCpyZVYH6k`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0050f50b-3f12-4542-ae25-a763fa1d1fb2",
  "isSidechain": false,
  "requestId": "req_011Cb3CAtLDSzPou5TTgAfss",
  "type": "assistant",
  "uuid": "ac38313a-0f6d-4935-8de9-740d1793caf8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "24e67ff1-1ea3-4bcf-a9e3-703eaa6cb36e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_016LijnS4LxED3N681B1khEj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 633,
      "cache_read_input_tokens": 84099,
      "output_tokens": 305,
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
          "output_tokens": 305,
          "cache_read_input_tokens": 84099,
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

### Runtime record

_source line 48_

```json
{
  "type": "last-prompt",
  "leafUuid": "ab382147-0a47-4ca9-bc54-8c7d276601e8",
  "sessionId": "24e67ff1-1ea3-4bcf-a9e3-703eaa6cb36e"
}
```

---

### Runtime record

_source line 49_

```json
{
  "type": "ai-title",
  "aiTitle": "Audit paper figures against experiment registry",
  "sessionId": "24e67ff1-1ea3-4bcf-a9e3-703eaa6cb36e"
}
```

---

### Assistant

_source line 50 · 2026-05-14T21:46:47.874Z_

<details><summary>Logged reasoning block</summary>

```text

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ab382147-0a47-4ca9-bc54-8c7d276601e8",
  "isSidechain": false,
  "requestId": "req_011Cb3CBFaesFonfZR3a7nBq",
  "type": "assistant",
  "uuid": "e2a7ee34-66c0-4864-bba2-aae26e6a026e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "24e67ff1-1ea3-4bcf-a9e3-703eaa6cb36e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01Wi43F3k5PKAA5bmBgdoBg3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13930,
      "cache_read_input_tokens": 84732,
      "output_tokens": 9298,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13930,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 9298,
          "cache_read_input_tokens": 84732,
          "cache_creation_input_tokens": 13930,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13930
          },
          "type": "message"
        }
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

_source line 51 · 2026-05-14T21:46:48.323Z_

Now I have most of the data. Let me run targeted checks for hard constraint violations.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e2a7ee34-66c0-4864-bba2-aae26e6a026e",
  "isSidechain": false,
  "requestId": "req_011Cb3CBFaesFonfZR3a7nBq",
  "type": "assistant",
  "uuid": "264128c4-c676-46cc-b813-651e91f83575",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "24e67ff1-1ea3-4bcf-a9e3-703eaa6cb36e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01Wi43F3k5PKAA5bmBgdoBg3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13930,
      "cache_read_input_tokens": 84732,
      "output_tokens": 9298,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13930,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 9298,
          "cache_read_input_tokens": 84732,
          "cache_creation_input_tokens": 13930,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13930
          },
          "type": "message"
        }
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

_source line 52 · 2026-05-14T21:46:50.487Z_

<details open><summary>🔧 Tool call — Grep · `toolu_013B1bGvJuvDG2eseDeZDT8b`</summary>

```json
{
  "pattern": "2\\.4(x|×|\\\\times)",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "264128c4-c676-46cc-b813-651e91f83575",
  "isSidechain": false,
  "requestId": "req_011Cb3CBFaesFonfZR3a7nBq",
  "type": "assistant",
  "uuid": "750a8f4f-1536-46a3-954b-0e22fba8f4b4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "24e67ff1-1ea3-4bcf-a9e3-703eaa6cb36e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01Wi43F3k5PKAA5bmBgdoBg3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13930,
      "cache_read_input_tokens": 84732,
      "output_tokens": 9298,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13930,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 9298,
          "cache_read_input_tokens": 84732,
          "cache_creation_input_tokens": 13930,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13930
          },
          "type": "message"
        }
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

_source line 53 · 2026-05-14T21:46:55.179Z_

<details><summary>↩ Tool result · `toolu_01NaJZt7GNh83wvZLnPefacy`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0bb277db-ff47-4a8a-98ca-f5603102ac4f",
  "isSidechain": false,
  "promptId": "c33bf5b5-c338-4f2f-97b8-e3e6d5f92819",
  "type": "user",
  "uuid": "699b46ba-caaa-476b-bf42-672a879d4cda",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "",
    "numLines": 0
  },
  "sourceToolAssistantUUID": "0bb277db-ff47-4a8a-98ca-f5603102ac4f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "24e67ff1-1ea3-4bcf-a9e3-703eaa6cb36e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-14T21:46:50.518Z_

<details><summary>↩ Tool result · `toolu_013B1bGvJuvDG2eseDeZDT8b`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "750a8f4f-1536-46a3-954b-0e22fba8f4b4",
  "isSidechain": false,
  "promptId": "c33bf5b5-c338-4f2f-97b8-e3e6d5f92819",
  "type": "user",
  "uuid": "849dc4bb-c6e4-49cc-92b5-903ada215c61",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "",
    "numLines": 0
  },
  "sourceToolAssistantUUID": "750a8f4f-1536-46a3-954b-0e22fba8f4b4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "24e67ff1-1ea3-4bcf-a9e3-703eaa6cb36e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-14T21:46:51.927Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01LKzMVnTGmXgCXjfvgkjdud`</summary>

```json
{
  "pattern": "six (modes|hacking|distinct)",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/",
  "output_mode": "content",
  "-i": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "849dc4bb-c6e4-49cc-92b5-903ada215c61",
  "isSidechain": false,
  "requestId": "req_011Cb3CBFaesFonfZR3a7nBq",
  "type": "assistant",
  "uuid": "a792bc02-090f-4954-85f4-896b4e111a5d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "24e67ff1-1ea3-4bcf-a9e3-703eaa6cb36e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01Wi43F3k5PKAA5bmBgdoBg3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13930,
      "cache_read_input_tokens": 84732,
      "output_tokens": 9298,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13930,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 9298,
          "cache_read_input_tokens": 84732,
          "cache_creation_input_tokens": 13930,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13930
          },
          "type": "message"
        }
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

_source line 56 · 2026-05-14T21:46:51.943Z_

<details><summary>↩ Tool result · `toolu_01LKzMVnTGmXgCXjfvgkjdud`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a792bc02-090f-4954-85f4-896b4e111a5d",
  "isSidechain": false,
  "promptId": "c33bf5b5-c338-4f2f-97b8-e3e6d5f92819",
  "type": "user",
  "uuid": "ff815fec-c5b2-472d-8041-4043bb88dbf5",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "",
    "numLines": 0
  },
  "sourceToolAssistantUUID": "a792bc02-090f-4954-85f4-896b4e111a5d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "24e67ff1-1ea3-4bcf-a9e3-703eaa6cb36e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-14T21:46:52.818Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01DL12WRdrfj9vyX1qNsG9zR`</summary>

```json
{
  "pattern": "no hacking|zero hacking|hacking-free|hacking free",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/",
  "output_mode": "content",
  "-i": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ff815fec-c5b2-472d-8041-4043bb88dbf5",
  "isSidechain": false,
  "requestId": "req_011Cb3CBFaesFonfZR3a7nBq",
  "type": "assistant",
  "uuid": "b701692e-e256-4930-8d5a-7dc933b4156d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "24e67ff1-1ea3-4bcf-a9e3-703eaa6cb36e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01Wi43F3k5PKAA5bmBgdoBg3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13930,
      "cache_read_input_tokens": 84732,
      "output_tokens": 9298,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13930,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 9298,
          "cache_read_input_tokens": 84732,
          "cache_creation_input_tokens": 13930,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13930
          },
          "type": "message"
        }
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

_source line 58 · 2026-05-14T21:46:52.832Z_

<details><summary>↩ Tool result · `toolu_01DL12WRdrfj9vyX1qNsG9zR`</summary>

```text
paper/experiments.tex:104:\caption{Hacking composition across reward conditions (proved samples). ISR converts H1 (conclusion embedding) into more extreme H7 (conclusion duplication) without reducing total hacking; SFT is near-zero hacking (92.9\% genuine).}
paper/experiments.tex:110:SFT remains the only condition with near-zero hacking (Figure~\ref{fig:hacking-composition}), confirming hacking is RL-reward-specific.
paper/abstract.tex:4:ISR exposes a collapse trajectory hidden from prove rate: over 100 to 1000 GRPO training steps (Qwen3-4B), ISR falls from 0.642 to 0.003---a 99.5\% degradation---while prove rate rises from 32\% to 96\%. An SFT baseline achieves 92.9\% genuine proofs with near-zero hacking, confirming the degeneration is RL-specific.
paper/introduction.tex:18:A supervised fine-tuning (SFT) baseline achieves 92.9\% genuine proofs with near-zero hacking, confirming that the structural collapse is a consequence of RL reward optimization, not model capacity or data limitations.
paper/conclusion.tex:4:Applied to GRPO-trained models, ISR reveals a collapse trajectory hidden from prove rate, confirmed as RL-specific by an SFT baseline with near-zero hacking (\S\ref{sec:diagnostic}).
paper/main.aux:511:\@writefile{lof}{\contentsline {figure}{\numberline {3}{\ignorespaces Hacking composition across reward conditions (proved samples). ISR converts H1 (conclusion embedding) into more extreme H7 (conclusion duplication) without reducing total hacking; SFT is near-zero hacking (92.9\% genuine).}}{6}{figure.caption.10}\protected@file@percent }
paper/main.aux:512:\newlabel{fig:hacking-composition}{{3}{6}{Hacking composition across reward conditions (proved samples). ISR converts H1 (conclusion embedding) into more extreme H7 (conclusion duplication) without reducing total hacking; SFT is near-zero hacking (92.9\% genuine)}{figure.caption.10}{}}
paper/paper.aux:899:\@writefile{lof}{\contentsline {figure}{\numberline {4}{\ignorespaces Hacking mode composition across reward conditions (proved samples). ISR reward converts H1 (conclusion embedding) into the more extreme H7 (conclusion duplication) without reducing total hacking prevalence. SFT exhibits near-zero hacking (92.9\% genuine).}}{10}{figure.caption.32}\protected@file@percent }
paper/paper.aux:900:\newlabel{fig:hacking-composition}{{4}{10}{Hacking mode composition across reward conditions (proved samples). ISR reward converts H1 (conclusion embedding) into the more extreme H7 (conclusion duplication) without reducing total hacking prevalence. SFT exhibits near-zero hacking (92.9\% genuine)}{figure.caption.32}{}}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b701692e-e256-4930-8d5a-7dc933b4156d",
  "isSidechain": false,
  "promptId": "c33bf5b5-c338-4f2f-97b8-e3e6d5f92819",
  "type": "user",
  "uuid": "229bc8ad-1d47-4b58-843c-7e7c003b5495",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "paper/experiments.tex:104:\\caption{Hacking composition across reward conditions (proved samples). ISR converts H1 (conclusion embedding) into more extreme H7 (conclusion duplication) without reducing total hacking; SFT is near-zero hacking (92.9\\% genuine).}\npaper/experiments.tex:110:SFT remains the only condition with near-zero hacking (Figure~\\ref{fig:hacking-composition}), confirming hacking is RL-reward-specific.\npaper/abstract.tex:4:ISR exposes a collapse trajectory hidden from prove rate: over 100 to 1000 GRPO training steps (Qwen3-4B), ISR falls from 0.642 to 0.003---a 99.5\\% degradation---while prove rate rises from 32\\% to 96\\%. An SFT baseline achieves 92.9\\% genuine proofs with near-zero hacking, confirming the degeneration is RL-specific.\npaper/introduction.tex:18:A supervised fine-tuning (SFT) baseline achieves 92.9\\% genuine proofs with near-zero hacking, confirming that the structural collapse is a consequence of RL reward optimization, not model capacity or data limitations.\npaper/conclusion.tex:4:Applied to GRPO-trained models, ISR reveals a collapse trajectory hidden from prove rate, confirmed as RL-specific by an SFT baseline with near-zero hacking (\\S\\ref{sec:diagnostic}).\npaper/main.aux:511:\\@writefile{lof}{\\contentsline {figure}{\\numberline {3}{\\ignorespaces Hacking composition across reward conditions (proved samples). ISR converts H1 (conclusion embedding) into more extreme H7 (conclusion duplication) without reducing total hacking; SFT is near-zero hacking (92.9\\% genuine).}}{6}{figure.caption.10}\\protected@file@percent }\npaper/main.aux:512:\\newlabel{fig:hacking-composition}{{3}{6}{Hacking composition across reward conditions (proved samples). ISR converts H1 (conclusion embedding) into more extreme H7 (conclusion duplication) without reducing total hacking; SFT is near-zero hacking (92.9\\% genuine)}{figure.caption.10}{}}\npaper/paper.aux:899:\\@writefile{lof}{\\contentsline {figure}{\\numberline {4}{\\ignorespaces Hacking mode composition across reward conditions (proved samples). ISR reward converts H1 (conclusion embedding) into the more extreme H7 (conclusion duplication) without reducing total hacking prevalence. SFT exhibits near-zero hacking (92.9\\% genuine).}}{10}{figure.caption.32}\\protected@file@percent }\npaper/paper.aux:900:\\newlabel{fig:hacking-composition}{{4}{10}{Hacking mode composition across reward conditions (proved samples). ISR reward converts H1 (conclusion embedding) into the more extreme H7 (conclusion duplication) without reducing total hacking prevalence. SFT exhibits near-zero hacking (92.9\\% genuine)}{figure.caption.32}{}}",
    "numLines": 9
  },
  "sourceToolAssistantUUID": "b701692e-e256-4930-8d5a-7dc933b4156d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "24e67ff1-1ea3-4bcf-a9e3-703eaa6cb36e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 59 · 2026-05-14T21:46:54.152Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01TGjyUL2cqpxnqUpGgvZRbv`</summary>

```json
{
  "pattern": "additive vs.? convex|convex vs.? additive",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/",
  "output_mode": "content",
  "-i": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "229bc8ad-1d47-4b58-843c-7e7c003b5495",
  "isSidechain": false,
  "requestId": "req_011Cb3CBFaesFonfZR3a7nBq",
  "type": "assistant",
  "uuid": "a361ee05-1648-4b42-859b-5eb7264e76c9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "24e67ff1-1ea3-4bcf-a9e3-703eaa6cb36e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01Wi43F3k5PKAA5bmBgdoBg3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13930,
      "cache_read_input_tokens": 84732,
      "output_tokens": 9298,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13930,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 9298,
          "cache_read_input_tokens": 84732,
          "cache_creation_input_tokens": 13930,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13930
          },
          "type": "message"
        }
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

_source line 60 · 2026-05-14T21:46:54.176Z_

<details><summary>↩ Tool result · `toolu_01TGjyUL2cqpxnqUpGgvZRbv`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a361ee05-1648-4b42-859b-5eb7264e76c9",
  "isSidechain": false,
  "promptId": "c33bf5b5-c338-4f2f-97b8-e3e6d5f92819",
  "type": "user",
  "uuid": "0529287b-4812-4909-8d4a-8258ded12f42",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "",
    "numLines": 0
  },
  "sourceToolAssistantUUID": "a361ee05-1648-4b42-859b-5eb7264e76c9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "24e67ff1-1ea3-4bcf-a9e3-703eaa6cb36e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 61 · 2026-05-14T21:46:55.163Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01NaJZt7GNh83wvZLnPefacy`</summary>

```json
{
  "pattern": "3\\.2(x|×|\\\\times)",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0529287b-4812-4909-8d4a-8258ded12f42",
  "isSidechain": false,
  "requestId": "req_011Cb3CBFaesFonfZR3a7nBq",
  "type": "assistant",
  "uuid": "0bb277db-ff47-4a8a-98ca-f5603102ac4f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "24e67ff1-1ea3-4bcf-a9e3-703eaa6cb36e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01Wi43F3k5PKAA5bmBgdoBg3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13930,
      "cache_read_input_tokens": 84732,
      "output_tokens": 9298,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13930,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 9298,
          "cache_read_input_tokens": 84732,
          "cache_creation_input_tokens": 13930,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13930
          },
          "type": "message"
        }
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

_source line 62_

```json
{
  "type": "last-prompt",
  "leafUuid": "699b46ba-caaa-476b-bf42-672a879d4cda",
  "sessionId": "24e67ff1-1ea3-4bcf-a9e3-703eaa6cb36e"
}
```

---

### Runtime record

_source line 63_

```json
{
  "type": "ai-title",
  "aiTitle": "Audit paper figures against experiment registry",
  "sessionId": "24e67ff1-1ea3-4bcf-a9e3-703eaa6cb36e"
}
```

---

### Assistant

_source line 64 · 2026-05-14T21:47:01.461Z_

<details><summary>Logged reasoning block</summary>

```text

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "699b46ba-caaa-476b-bf42-672a879d4cda",
  "isSidechain": false,
  "requestId": "req_011Cb3CJGCoYsZ2vVQz4VqfY",
  "type": "assistant",
  "uuid": "d0a4835b-bbaf-4e20-b373-a121a103514d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "24e67ff1-1ea3-4bcf-a9e3-703eaa6cb36e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01NB3BKox8UbZx6VwKpzpv6T",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10542,
      "cache_read_input_tokens": 98662,
      "output_tokens": 819,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10542,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 819,
          "cache_read_input_tokens": 98662,
          "cache_creation_input_tokens": 10542,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10542
          },
          "type": "message"
        }
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

_source line 65 · 2026-05-14T21:47:02.809Z_

<details open><summary>🔧 Tool call — Grep · `toolu_016VFrvF3kTBpmkwzABL1dRi`</summary>

```json
{
  "pattern": "0\\.143",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d0a4835b-bbaf-4e20-b373-a121a103514d",
  "isSidechain": false,
  "requestId": "req_011Cb3CJGCoYsZ2vVQz4VqfY",
  "type": "assistant",
  "uuid": "59c891dc-7b99-42c8-9b76-e9699d648577",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "24e67ff1-1ea3-4bcf-a9e3-703eaa6cb36e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01NB3BKox8UbZx6VwKpzpv6T",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10542,
      "cache_read_input_tokens": 98662,
      "output_tokens": 819,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10542,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 819,
          "cache_read_input_tokens": 98662,
          "cache_creation_input_tokens": 10542,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10542
          },
          "type": "message"
        }
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

_source line 66 · 2026-05-14T21:47:02.822Z_

<details><summary>↩ Tool result · `toolu_016VFrvF3kTBpmkwzABL1dRi`</summary>

```text
paper/experiments.tex:64:ISR & 0.3 & 18 & 0.143 & --- & --- & --- \\
paper/appendix.tex:355:  & 42 & 500 & 0.18 & 0.143 & --- & --- & --- & Goodhart collapse \\
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "59c891dc-7b99-42c8-9b76-e9699d648577",
  "isSidechain": false,
  "promptId": "c33bf5b5-c338-4f2f-97b8-e3e6d5f92819",
  "type": "user",
  "uuid": "6fa58d24-5093-4a92-a9d3-075f3c946256",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "paper/experiments.tex:64:ISR & 0.3 & 18 & 0.143 & --- & --- & --- \\\\\npaper/appendix.tex:355:  & 42 & 500 & 0.18 & 0.143 & --- & --- & --- & Goodhart collapse \\\\",
    "numLines": 2
  },
  "sourceToolAssistantUUID": "59c891dc-7b99-42c8-9b76-e9699d648577",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "24e67ff1-1ea3-4bcf-a9e3-703eaa6cb36e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 67 · 2026-05-14T21:47:05.289Z_

<details><summary>↩ Tool result · `toolu_01MUu2iwoF3z8dyPAqf7ftri`</summary>

```text
paper/related_work.tex:2:\label{sec:related-work}
paper/related_work.tex:9:STA differs in diagnostic focus: ISR exposes that execution accuracy conflates faithful derivation with degenerate shortcuts, and our finding that 87\% of proved outputs under exec-only GRPO embed the conclusion in the premises (\S\ref{sec:diagnostic}) suggests prior prove-rate gains may overstate genuine reasoning improvement.
paper/related_work.tex:14:ISR is solver-grounded rather than learned (no reward-model noise), yet our \S\ref{sec:goodhart} result shows that even non-learned, deterministic process signals Goodhart when optimized---suggesting the problem is fundamental to process-level reward shaping, not specific to learned models.
paper/experiments.tex:2:\label{sec:experiments}
paper/experiments.tex:4:We evaluate STA along three axes: as a diagnostic for reward hacking (\S\ref{sec:diagnostic}); as a training reward exhibiting meta-level Goodhart's Law (\S\ref{sec:goodhart}); and as a cross-logic protocol (\S\ref{sec:crosslogic}). We synthesize results into a hacking taxonomy (\S\ref{sec:taxonomy}).
paper/experiments.tex:7:\label{sec:setup}
paper/experiments.tex:16:Full hyperparameters are in Appendix~\ref{app:setup}.
paper/experiments.tex:19:\label{sec:diagnostic}
paper/experiments.tex:25:\label{fig:isr-collapse}
paper/experiments.tex:29:Figure~\ref{fig:isr-collapse} traces ISR and PR over training for exec-only GRPO (seed~42).
paper/experiments.tex:38:The cross-seed PR $\sigma{=}\pm47$\,pp is itself a finding: aggregate metrics obscure qualitatively different failure modes (per-seed details in Table~\ref{tab:beta01-3seed}).
paper/experiments.tex:45:\label{sec:goodhart}
paper/experiments.tex:68:\caption{Goodhart landscape across reward conditions. 3-seed rows show mean$\pm$std (ISR/Random $\beta{=}0.1$); other rows are single seed. $^\dagger$Seed~42; see \S\ref{sec:diagnostic} for 3-seed divergence. $\ddagger$ISR$^*$ omitted: inflated by H7 gaming (Appendix Table~\ref{tab:beta01-3seed}). Best PR and Gen.\% bolded per group.}
paper/experiments.tex:69:\label{tab:goodhart-landscape}
paper/experiments.tex:73:Table~\ref{tab:goodhart-landscape} summarizes results.
paper/experiments.tex:76:Conclusion embedding (H1+H7) is GRPO-universal at 68--97\% across RL conditions: random produces only H1 (70.9--93.2\%), while ISR converts H1$\to$H7 without reducing the total (Figure~\ref{fig:hacking-composition}; per-seed: Appendix Table~\ref{tab:beta01-3seed}).
paper/experiments.tex:91:\label{sec:crosslogic}
paper/experiments.tex:93:We replicated both experiments using SWI-Prolog 8.4.2 (full results: Appendix Table~\ref{tab:prolog-crosslogic}).
paper/experiments.tex:99:\label{sec:taxonomy}
paper/experiments.tex:105:\label{fig:hacking-composition}
paper/experiments.tex:108:[Omitted long matching line]
paper/experiments.tex:110:SFT remains the only condition with near-zero hacking (Figure~\ref{fig:hacking-composition}), confirming hacking is RL-reward-specific.
paper/conclusion.tex:4:Applied to GRPO-trained models, ISR reveals a collapse trajectory hidden from prove rate, confirmed as RL-specific by an SFT baseline with near-zero hacking (\S\ref{sec:diagnostic}).
paper/conclusion.tex:5:When repurposed as a training signal, ISR induces meta-level Goodhart's Law: at low dose, the model games the diagnostic itself through conclusion duplication absent under matched controls; at high dose, prove rate collapses; the sole apparent ISR improvement reduces to noise after controlling for a premise-count confound (\S\ref{sec:goodhart}).
paper/conclusion.tex:6:Both diagnostic utility and Goodhart vulnerability transfer to Prolog/SWI-Prolog: ISR-as-reward yields universal gaming across all seeds with zero genuine proofs, each via a distinct mechanism (\S\ref{sec:crosslogic}).
paper/conclusion.tex:7:Across six reward conditions and two logic types, we catalog seven hacking modes, including query-as-fact gaming that bypasses text-match classifiers (\S\ref{sec:taxonomy}).
paper/conclusion.tex:21:ISR quantifies syntactic component necessity, not semantic faithfulness: a downstream NLI evaluation finds ISR and task accuracy uncorrelated (Spearman $\rho{=}{-}0.049$, $p{=}0.187$; Appendix~\ref{app:extended-discussion}).
paper/method.tex:2:\label{sec:method}
paper/method.tex:8:\label{fig:sta-overview}
paper/method.tex:12:\label{sec:task}
paper/method.tex:15:An external solver $S$ returns $S(F)\in\{\textit{proved},\textit{failed}\}$; we use Prover9 for FOL and SWI-Prolog for Prolog (\autoref{fig:sta-overview}a).
paper/method.tex:24:\label{sec:sta}
paper/method.tex:26:To diagnose structural quality, STA tests whether each component of a proved formalization is individually necessary for proof success (\autoref{fig:sta-overview}b).
paper/method.tex:35:  \label{eq:isr}
paper/method.tex:40:Pseudocode is in Appendix~\ref{app:algorithm}.
paper/method.tex:45:We control for this confound in our analysis (\S\ref{sec:goodhart}).
paper/method.tex:48:\label{sec:rewards}
paper/method.tex:50:We study six reward conditions (\autoref{fig:sta-overview}c).
paper/method.tex:58:Each RL condition is trained with seeds $\{42,43,44\}$ controlling initialization and stochasticity; all seeds share identical training data (\S\ref{sec:setup}).
paper/method.tex:61:\label{sec:taxonomy-method}
paper/method.tex:63:Across conditions, seeds, and logic types, we identify seven hacking modes (H1, H7, tautological collapse, repetition collapse, complexity-without-utility, contradiction explosion, query-as-fact gaming; full definitions in \S\ref{sec:taxonomy} and Appendix~\ref{app:hacking-modes}).
paper/appendix.tex:4:\label{app:setup}
paper/appendix.tex:6:Table~\ref{tab:hyperparams} lists all hyperparameters shared across experiments.
paper/appendix.tex:13:\label{tab:hyperparams}
paper/appendix.tex:58:\label{app:algorithm}
paper/appendix.tex:60:Algorithm~\ref{alg:sta} gives the full procedure for computing ISR over a proved formalization.
paper/appendix.tex:64:\label{alg:sta}
paper/appendix.tex:84:\label{app:extended-discussion}
paper/appendix.tex:94:Under exec-only training, low ISR in Prolog reflects redundant coding---repeated ground facts where removing any single copy does not affect the proof---rather than absence of reasoning (\S\ref{sec:crosslogic}).
paper/appendix.tex:95:Under ISR-as-reward, high ISR reflects metric gaming (\S\ref{sec:goodhart}).
paper/appendix.tex:101:This confound explains the sole apparent ISR-as-reward success (\S\ref{sec:goodhart}): ISR $\beta{=}0.1$ seed~42 produces shorter formalizations, mechanically inflating ISR.
paper/appendix.tex:102:Premise-count-matched comparison eliminates the difference ($1.06\times$; Table~\ref{tab:beta01-3seed}).
paper/appendix.tex:114:The three exec-only seeds diverge radically (PR $\sigma{=}\pm 47$ percentage points), each converging to a qualitatively different degeneration mode (\S\ref{sec:diagnostic}).
paper/appendix.tex:115:ISR $\beta{=}0.1$ seeds show similar divergence: 2/3 dominated by conclusion duplication (H7), 1/3 by premise minimization (\S\ref{sec:goodhart}).
paper/appendix.tex:120:\label{app:hacking-modes}
paper/appendix.tex:124:Table~\ref{tab:hacking-taxonomy-app} summarizes prevalence across FOL conditions.
paper/appendix.tex:143:\caption{Hacking taxonomy across FOL conditions (\% of proved samples). ISR/Rand columns: $\beta{=}0.1$ 3-seed means. Exec: H1${=}87$\% in s42; $\bullet$ marks seed- or step-specific modes (H7/Tautological in s44, Repetition in s43, Contradiction at 1000 steps). C-w/o-util.: complexity-without-utility (random-specific). Q-as-fact: Prolog STA only (Table~\ref{tab:prolog-crosslogic}).}
paper/appendix.tex:144:\label{tab:hacking-taxonomy-app}
paper/appendix.tex:313:\label{app:detailed-results}
paper/appendix.tex:315:Tables~\ref{tab:beta01-3seed} and \ref{tab:prolog-crosslogic} report full per-seed results.
paper/appendix.tex:321:\caption{Detailed per-seed results: FOL (Prover9). Includes the per-seed $\beta{=}0.1$ breakdown referenced from Table~\ref{tab:goodhart-landscape}. PR = prove rate, ISR$^*$ = proved-only ISR, H7/H1/Gen.\ = percentage among proved samples. ``---'' indicates data not available. $^\dagger$s43 uses sampling eval ($T{=}0.7$).}
paper/appendix.tex:322:\label{tab:fol-detailed}
paper/appendix.tex:323:\label{tab:beta01-3seed}
paper/appendix.tex:374:\label{tab:prolog-detailed}
paper/appendix.tex:375:\label{tab:prolog-crosslogic}
paper/appendix.tex:409:\label{fig:prolog-comparison}
paper/appendix.tex:413:Table~\ref{tab:fol-detailed} traces the ISR collapse over training:
paper/introduction.tex:2:\label{sec:introduction}
paper/introduction.tex:11:No existing method provides an annotation-free, solver-agnostic diagnostic for structural integrity in neurosymbolic outputs (see \S\ref{sec:related-work} for full context).
paper/introduction.tex:13:We address this gap with \emph{Solver Trace Ablation} (STA), a diagnostic protocol inspired by mutation testing~\cite{demillo1978} that applies component necessity testing---leave-one-out (LOO) ablation on solver inputs---to quantify structural integrity (\autoref{fig:sta-overview}).
paper/introduction.tex:21:At $\beta{=}0.1$, 64.5\% of proved samples exhibit ISR-specific conclusion duplication (H7) vs.\ 0\% under matched random reward, and the sole apparent improvement reduces to 1.06$\times$ after controlling for a premise-count confound (\S\ref{sec:goodhart}); at $\beta{=}0.3$ PR collapses to 18\% vs.\ 48\% for random control~\cite{gao-reward-overoptimization}.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c33b5bc3-af20-498b-a9d5-779ae4d76199",
  "isSidechain": false,
  "promptId": "c33bf5b5-c338-4f2f-97b8-e3e6d5f92819",
  "type": "user",
  "uuid": "a55984f6-a249-415b-918b-34cb725fd910",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "paper/related_work.tex:2:\\label{sec:related-work}\npaper/related_work.tex:9:STA differs in diagnostic focus: ISR exposes that execution accuracy conflates faithful derivation with degenerate shortcuts, and our finding that 87\\% of proved outputs under exec-only GRPO embed the conclusion in the premises (\\S\\ref{sec:diagnostic}) suggests prior prove-rate gains may overstate genuine reasoning improvement.\npaper/related_work.tex:14:ISR is solver-grounded rather than learned (no reward-model noise), yet our \\S\\ref{sec:goodhart} result shows that even non-learned, deterministic process signals Goodhart when optimized---suggesting the problem is fundamental to process-level reward shaping, not specific to learned models.\npaper/experiments.tex:2:\\label{sec:experiments}\npaper/experiments.tex:4:We evaluate STA along three axes: as a diagnostic for reward hacking (\\S\\ref{sec:diagnostic}); as a training reward exhibiting meta-level Goodhart's Law (\\S\\ref{sec:goodhart}); and as a cross-logic protocol (\\S\\ref{sec:crosslogic}). We synthesize results into a hacking taxonomy (\\S\\ref{sec:taxonomy}).\npaper/experiments.tex:7:\\label{sec:setup}\npaper/experiments.tex:16:Full hyperparameters are in Appendix~\\ref{app:setup}.\npaper/experiments.tex:19:\\label{sec:diagnostic}\npaper/experiments.tex:25:\\label{fig:isr-collapse}\npaper/experiments.tex:29:Figure~\\ref{fig:isr-collapse} traces ISR and PR over training for exec-only GRPO (seed~42).\npaper/experiments.tex:38:The cross-seed PR $\\sigma{=}\\pm47$\\,pp is itself a finding: aggregate metrics obscure qualitatively different failure modes (per-seed details in Table~\\ref{tab:beta01-3seed}).\npaper/experiments.tex:45:\\label{sec:goodhart}\npaper/experiments.tex:68:\\caption{Goodhart landscape across reward conditions. 3-seed rows show mean$\\pm$std (ISR/Random $\\beta{=}0.1$); other rows are single seed. $^\\dagger$Seed~42; see \\S\\ref{sec:diagnostic} for 3-seed divergence. $\\ddagger$ISR$^*$ omitted: inflated by H7 gaming (Appendix Table~\\ref{tab:beta01-3seed}). Best PR and Gen.\\% bolded per group.}\npaper/experiments.tex:69:\\label{tab:goodhart-landscape}\npaper/experiments.tex:73:Table~\\ref{tab:goodhart-landscape} summarizes results.\npaper/experiments.tex:76:Conclusion embedding (H1+H7) is GRPO-universal at 68--97\\% across RL conditions: random produces only H1 (70.9--93.2\\%), while ISR converts H1$\\to$H7 without reducing the total (Figure~\\ref{fig:hacking-composition}; per-seed: Appendix Table~\\ref{tab:beta01-3seed}).\npaper/experiments.tex:91:\\label{sec:crosslogic}\npaper/experiments.tex:93:We replicated both experiments using SWI-Prolog 8.4.2 (full results: Appendix Table~\\ref{tab:prolog-crosslogic}).\npaper/experiments.tex:99:\\label{sec:taxonomy}\npaper/experiments.tex:105:\\label{fig:hacking-composition}\npaper/experiments.tex:108:[Omitted long matching line]\npaper/experiments.tex:110:SFT remains the only condition with near-zero hacking (Figure~\\ref{fig:hacking-composition}), confirming hacking is RL-reward-specific.\npaper/conclusion.tex:4:Applied to GRPO-trained models, ISR reveals a collapse trajectory hidden from prove rate, confirmed as RL-specific by an SFT baseline with near-zero hacking (\\S\\ref{sec:diagnostic}).\npaper/conclusion.tex:5:When repurposed as a training signal, ISR induces meta-level Goodhart's Law: at low dose, the model games the diagnostic itself through conclusion duplication absent under matched controls; at high dose, prove rate collapses; the sole apparent ISR improvement reduces to noise after controlling for a premise-count confound (\\S\\ref{sec:goodhart}).\npaper/conclusion.tex:6:Both diagnostic utility and Goodhart vulnerability transfer to Prolog/SWI-Prolog: ISR-as-reward yields universal gaming across all seeds with zero genuine proofs, each via a distinct mechanism (\\S\\ref{sec:crosslogic}).\npaper/conclusion.tex:7:Across six reward conditions and two logic types, we catalog seven hacking modes, including query-as-fact gaming that bypasses text-match classifiers (\\S\\ref{sec:taxonomy}).\npaper/conclusion.tex:21:ISR quantifies syntactic component necessity, not semantic faithfulness: a downstream NLI evaluation finds ISR and task accuracy uncorrelated (Spearman $\\rho{=}{-}0.049$, $p{=}0.187$; Appendix~\\ref{app:extended-discussion}).\npaper/method.tex:2:\\label{sec:method}\npaper/method.tex:8:\\label{fig:sta-overview}\npaper/method.tex:12:\\label{sec:task}\npaper/method.tex:15:An external solver $S$ returns $S(F)\\in\\{\\textit{proved},\\textit{failed}\\}$; we use Prover9 for FOL and SWI-Prolog for Prolog (\\autoref{fig:sta-overview}a).\npaper/method.tex:24:\\label{sec:sta}\npaper/method.tex:26:To diagnose structural quality, STA tests whether each component of a proved formalization is individually necessary for proof success (\\autoref{fig:sta-overview}b).\npaper/method.tex:35:  \\label{eq:isr}\npaper/method.tex:40:Pseudocode is in Appendix~\\ref{app:algorithm}.\npaper/method.tex:45:We control for this confound in our analysis (\\S\\ref{sec:goodhart}).\npaper/method.tex:48:\\label{sec:rewards}\npaper/method.tex:50:We study six reward conditions (\\autoref{fig:sta-overview}c).\npaper/method.tex:58:Each RL condition is trained with seeds $\\{42,43,44\\}$ controlling initialization and stochasticity; all seeds share identical training data (\\S\\ref{sec:setup}).\npaper/method.tex:61:\\label{sec:taxonomy-method}\npaper/method.tex:63:Across conditions, seeds, and logic types, we identify seven hacking modes (H1, H7, tautological collapse, repetition collapse, complexity-without-utility, contradiction explosion, query-as-fact gaming; full definitions in \\S\\ref{sec:taxonomy} and Appendix~\\ref{app:hacking-modes}).\npaper/appendix.tex:4:\\label{app:setup}\npaper/appendix.tex:6:Table~\\ref{tab:hyperparams} lists all hyperparameters shared across experiments.\npaper/appendix.tex:13:\\label{tab:hyperparams}\npaper/appendix.tex:58:\\label{app:algorithm}\npaper/appendix.tex:60:Algorithm~\\ref{alg:sta} gives the full procedure for computing ISR over a proved formalization.\npaper/appendix.tex:64:\\label{alg:sta}\npaper/appendix.tex:84:\\label{app:extended-discussion}\npaper/appendix.tex:94:Under exec-only training, low ISR in Prolog reflects redundant coding---repeated ground facts where removing any single copy does not affect the proof---rather than absence of reasoning (\\S\\ref{sec:crosslogic}).\npaper/appendix.tex:95:Under ISR-as-reward, high ISR reflects metric gaming (\\S\\ref{sec:goodhart}).\npaper/appendix.tex:101:This confound explains the sole apparent ISR-as-reward success (\\S\\ref{sec:goodhart}): ISR $\\beta{=}0.1$ seed~42 produces shorter formalizations, mechanically inflating ISR.\npaper/appendix.tex:102:Premise-count-matched comparison eliminates the difference ($1.06\\times$; Table~\\ref{tab:beta01-3seed}).\npaper/appendix.tex:114:The three exec-only seeds diverge radically (PR $\\sigma{=}\\pm 47$ percentage points), each converging to a qualitatively different degeneration mode (\\S\\ref{sec:diagnostic}).\npaper/appendix.tex:115:ISR $\\beta{=}0.1$ seeds show similar divergence: 2/3 dominated by conclusion duplication (H7), 1/3 by premise minimization (\\S\\ref{sec:goodhart}).\npaper/appendix.tex:120:\\label{app:hacking-modes}\npaper/appendix.tex:124:Table~\\ref{tab:hacking-taxonomy-app} summarizes prevalence across FOL conditions.\npaper/appendix.tex:143:\\caption{Hacking taxonomy across FOL conditions (\\% of proved samples). ISR/Rand columns: $\\beta{=}0.1$ 3-seed means. Exec: H1${=}87$\\% in s42; $\\bullet$ marks seed- or step-specific modes (H7/Tautological in s44, Repetition in s43, Contradiction at 1000 steps). C-w/o-util.: complexity-without-utility (random-specific). Q-as-fact: Prolog STA only (Table~\\ref{tab:prolog-crosslogic}).}\npaper/appendix.tex:144:\\label{tab:hacking-taxonomy-app}\npaper/appendix.tex:313:\\label{app:detailed-results}\npaper/appendix.tex:315:Tables~\\ref{tab:beta01-3seed} and \\ref{tab:prolog-crosslogic} report full per-seed results.\npaper/appendix.tex:321:\\caption{Detailed per-seed results: FOL (Prover9). Includes the per-seed $\\beta{=}0.1$ breakdown referenced from Table~\\ref{tab:goodhart-landscape}. PR = prove rate, ISR$^*$ = proved-only ISR, H7/H1/Gen.\\ = percentage among proved samples. ``---'' indicates data not available. $^\\dagger$s43 uses sampling eval ($T{=}0.7$).}\npaper/appendix.tex:322:\\label{tab:fol-detailed}\npaper/appendix.tex:323:\\label{tab:beta01-3seed}\npaper/appendix.tex:374:\\label{tab:prolog-detailed}\npaper/appendix.tex:375:\\label{tab:prolog-crosslogic}\npaper/appendix.tex:409:\\label{fig:prolog-comparison}\npaper/appendix.tex:413:Table~\\ref{tab:fol-detailed} traces the ISR collapse over training:\npaper/introduction.tex:2:\\label{sec:introduction}\npaper/introduction.tex:11:No existing method provides an annotation-free, solver-agnostic diagnostic for structural integrity in neurosymbolic outputs (see \\S\\ref{sec:related-work} for full context).\npaper/introduction.tex:13:We address this gap with \\emph{Solver Trace Ablation} (STA), a diagnostic protocol inspired by mutation testing~\\cite{demillo1978} that applies component necessity testing---leave-one-out (LOO) ablation on solver inputs---to quantify structural integrity (\\autoref{fig:sta-overview}).\npaper/introduction.tex:21:At $\\beta{=}0.1$, 64.5\\% of proved samples exhibit ISR-specific conclusion duplication (H7) vs.\\ 0\\% under matched random reward, and the sole apparent improvement reduces to 1.06$\\times$ after controlling for a premise-count confound (\\S\\ref{sec:goodhart}); at $\\beta{=}0.3$ PR collapses to 18\\% vs.\\ 48\\% for random control~\\cite{gao-reward-overoptimization}.",
    "numLines": 71
  },
  "sourceToolAssistantUUID": "c33b5bc3-af20-498b-a9d5-779ae4d76199",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "24e67ff1-1ea3-4bcf-a9e3-703eaa6cb36e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 68 · 2026-05-14T21:47:04.153Z_

<details open><summary>🔧 Tool call — Grep · `toolu_016HcncpCjSwWxXoQrLF1U68`</summary>

```json
{
  "pattern": "seven|7 (modes|hacking)|seven (modes|hacking)",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/",
  "output_mode": "content",
  "-i": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6fa58d24-5093-4a92-a9d3-075f3c946256",
  "isSidechain": false,
  "requestId": "req_011Cb3CJGCoYsZ2vVQz4VqfY",
  "type": "assistant",
  "uuid": "20e023f0-0cf6-404a-bc6b-b9423ef4d78c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "24e67ff1-1ea3-4bcf-a9e3-703eaa6cb36e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01NB3BKox8UbZx6VwKpzpv6T",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10542,
      "cache_read_input_tokens": 98662,
      "output_tokens": 819,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10542,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 819,
          "cache_read_input_tokens": 98662,
          "cache_creation_input_tokens": 10542,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10542
          },
          "type": "message"
        }
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

_source line 69 · 2026-05-14T21:47:04.181Z_

<details><summary>↩ Tool result · `toolu_016HcncpCjSwWxXoQrLF1U68`</summary>

```text
paper/experiments.tex:108:[Omitted long matching line]
paper/conclusion.tex:7:Across six reward conditions and two logic types, we catalog seven hacking modes, including query-as-fact gaming that bypasses text-match classifiers (\S\ref{sec:taxonomy}).
paper/method.tex:63:Across conditions, seeds, and logic types, we identify seven hacking modes (H1, H7, tautological collapse, repetition collapse, complexity-without-utility, contradiction explosion, query-as-fact gaming; full definitions in \S\ref{sec:taxonomy} and Appendix~\ref{app:hacking-modes}).
paper/appendix.tex:122:We identify seven distinct reward hacking modes across all experiments.
paper/introduction.tex:30:\item We catalog 7 hacking modes including query-as-fact gaming that bypasses text-match classifiers, motivating functional cross-validation of diagnostics.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "20e023f0-0cf6-404a-bc6b-b9423ef4d78c",
  "isSidechain": false,
  "promptId": "c33bf5b5-c338-4f2f-97b8-e3e6d5f92819",
  "type": "user",
  "uuid": "68b1484f-2501-4c78-abcc-0dfa159bcbc5",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "paper/experiments.tex:108:[Omitted long matching line]\npaper/conclusion.tex:7:Across six reward conditions and two logic types, we catalog seven hacking modes, including query-as-fact gaming that bypasses text-match classifiers (\\S\\ref{sec:taxonomy}).\npaper/method.tex:63:Across conditions, seeds, and logic types, we identify seven hacking modes (H1, H7, tautological collapse, repetition collapse, complexity-without-utility, contradiction explosion, query-as-fact gaming; full definitions in \\S\\ref{sec:taxonomy} and Appendix~\\ref{app:hacking-modes}).\npaper/appendix.tex:122:We identify seven distinct reward hacking modes across all experiments.\npaper/introduction.tex:30:\\item We catalog 7 hacking modes including query-as-fact gaming that bypasses text-match classifiers, motivating functional cross-validation of diagnostics.",
    "numLines": 5
  },
  "sourceToolAssistantUUID": "20e023f0-0cf6-404a-bc6b-b9423ef4d78c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "24e67ff1-1ea3-4bcf-a9e3-703eaa6cb36e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 70 · 2026-05-14T21:47:05.258Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01MUu2iwoF3z8dyPAqf7ftri`</summary>

```json
{
  "pattern": "\\\\label\\{|\\\\ref\\{|\\\\autoref\\{",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/",
  "output_mode": "content",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "68b1484f-2501-4c78-abcc-0dfa159bcbc5",
  "isSidechain": false,
  "requestId": "req_011Cb3CJGCoYsZ2vVQz4VqfY",
  "type": "assistant",
  "uuid": "c33b5bc3-af20-498b-a9d5-779ae4d76199",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "24e67ff1-1ea3-4bcf-a9e3-703eaa6cb36e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01NB3BKox8UbZx6VwKpzpv6T",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10542,
      "cache_read_input_tokens": 98662,
      "output_tokens": 819,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10542,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 819,
          "cache_read_input_tokens": 98662,
          "cache_creation_input_tokens": 10542,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10542
          },
          "type": "message"
        }
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

_source line 71 · 2026-05-14T21:47:05.346Z_

```json
{
  "parentUuid": "a55984f6-a249-415b-918b-34cb725fd910",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [
      {
        "content": "Read all paper sections (conclusion, related_work, appendix)",
        "status": "in_progress",
        "activeForm": "Reading remaining paper sections"
      },
      {
        "content": "Cross-check ISR collapse trajectory numbers (0.642/0.132/0.003)",
        "status": "pending",
        "activeForm": "Cross-checking ISR collapse numbers"
      },
      {
        "content": "Cross-check 3-seed β=0.1 ISR/Random numbers in Table 1 and appendix",
        "status": "pending",
        "activeForm": "Cross-checking β=0.1 3-seed numbers"
      },
      {
        "content": "Cross-check SFT baseline numbers (PR=14%, ISR=0.571, 92.9%)",
        "status": "pending",
        "activeForm": "Cross-checking SFT baseline numbers"
      },
      {
        "content": "Cross-check Prolog numbers in experiments/appendix",
        "status": "pending",
        "activeForm": "Cross-checking Prolog numbers"
      },
      {
        "content": "Check hard constraints (no 2.4x, hacking taxonomy 7, etc.)",
        "status": "pending",
        "activeForm": "Checking hard constraints from paper_framing"
      },
      {
        "content": "Check internal consistency between abstract/intro/experiments/conclusion",
        "status": "pending",
        "activeForm": "Checking internal consistency"
      },
      {
        "content": "Write consistency report to artifacts/",
        "status": "pending",
        "activeForm": "Writing consistency report"
      }
    ],
    "itemCount": 8
  },
  "type": "attachment",
  "uuid": "90be3e29-0dfb-4816-8827-9207a46194f8",
  "timestamp": "2026-05-14T21:47:05.346Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "24e67ff1-1ea3-4bcf-a9e3-703eaa6cb36e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 72 · 2026-05-14T21:47:12.266Z_

<details open><summary>🔧 Tool call — TodoWrite · `toolu_01X9pVGTY9Xw6Jxttn2n2zM9`</summary>

```json
{
  "todos": [
    {
      "content": "Read all paper sections (conclusion, related_work, appendix)",
      "activeForm": "Reading remaining paper sections",
      "status": "completed"
    },
    {
      "content": "Cross-check ISR collapse trajectory numbers (0.642/0.132/0.003)",
      "activeForm": "Cross-checking ISR collapse numbers",
      "status": "completed"
    },
    {
      "content": "Cross-check 3-seed β=0.1 ISR/Random numbers in Table 1 and appendix",
      "activeForm": "Cross-checking β=0.1 3-seed numbers",
      "status": "completed"
    },
    {
      "content": "Cross-check SFT baseline numbers (PR=14%, ISR=0.571, 92.9%)",
      "activeForm": "Cross-checking SFT baseline numbers",
      "status": "completed"
    },
    {
      "content": "Cross-check Prolog numbers in experiments/appendix",
      "activeForm": "Cross-checking Prolog numbers",
      "status": "completed"
    },
    {
      "content": "Check hard constraints (no 2.4x, hacking taxonomy 7, etc.)",
      "activeForm": "Checking hard constraints from paper_framing",
      "status": "completed"
    },
    {
      "content": "Check internal consistency between abstract/intro/experiments/conclusion",
      "activeForm": "Checking internal consistency",
      "status": "completed"
    },
    {
      "content": "Write consistency report to artifacts/",
      "activeForm": "Writing consistency report",
      "status": "in_progress"
    }
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "90be3e29-0dfb-4816-8827-9207a46194f8",
  "isSidechain": false,
  "requestId": "req_011Cb3CK22nu7FXbSt9r5ECu",
  "type": "assistant",
  "uuid": "e0f68da4-1bbf-4843-b2b6-c5f3afd8fc3a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "24e67ff1-1ea3-4bcf-a9e3-703eaa6cb36e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01WBycHgnJLDvhdyknsa3M6P",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6061,
      "cache_read_input_tokens": 109204,
      "output_tokens": 569,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6061,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 569,
          "cache_read_input_tokens": 109204,
          "cache_creation_input_tokens": 6061,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6061
          },
          "type": "message"
        }
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

_source line 73 · 2026-05-14T21:47:12.271Z_

<details><summary>↩ Tool result · `toolu_01X9pVGTY9Xw6Jxttn2n2zM9`</summary>

```text
Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e0f68da4-1bbf-4843-b2b6-c5f3afd8fc3a",
  "isSidechain": false,
  "promptId": "c33bf5b5-c338-4f2f-97b8-e3e6d5f92819",
  "type": "user",
  "uuid": "698a4fca-d773-44fb-9488-2b483c219469",
  "toolUseResult": {
    "oldTodos": [
      {
        "content": "Read all paper sections (conclusion, related_work, appendix)",
        "status": "in_progress",
        "activeForm": "Reading remaining paper sections"
      },
      {
        "content": "Cross-check ISR collapse trajectory numbers (0.642/0.132/0.003)",
        "status": "pending",
        "activeForm": "Cross-checking ISR collapse numbers"
      },
      {
        "content": "Cross-check 3-seed β=0.1 ISR/Random numbers in Table 1 and appendix",
        "status": "pending",
        "activeForm": "Cross-checking β=0.1 3-seed numbers"
      },
      {
        "content": "Cross-check SFT baseline numbers (PR=14%, ISR=0.571, 92.9%)",
        "status": "pending",
        "activeForm": "Cross-checking SFT baseline numbers"
      },
      {
        "content": "Cross-check Prolog numbers in experiments/appendix",
        "status": "pending",
        "activeForm": "Cross-checking Prolog numbers"
      },
      {
        "content": "Check hard constraints (no 2.4x, hacking taxonomy 7, etc.)",
        "status": "pending",
        "activeForm": "Checking hard constraints from paper_framing"
      },
      {
        "content": "Check internal consistency between abstract/intro/experiments/conclusion",
        "status": "pending",
        "activeForm": "Checking internal consistency"
      },
      {
        "content": "Write consistency report to artifacts/",
        "status": "pending",
        "activeForm": "Writing consistency report"
      }
    ],
    "newTodos": [
      {
        "content": "Read all paper sections (conclusion, related_work, appendix)",
        "status": "completed",
        "activeForm": "Reading remaining paper sections"
      },
      {
        "content": "Cross-check ISR collapse trajectory numbers (0.642/0.132/0.003)",
        "status": "completed",
        "activeForm": "Cross-checking ISR collapse numbers"
      },
      {
        "content": "Cross-check 3-seed β=0.1 ISR/Random numbers in Table 1 and appendix",
        "status": "completed",
        "activeForm": "Cross-checking β=0.1 3-seed numbers"
      },
      {
        "content": "Cross-check SFT baseline numbers (PR=14%, ISR=0.571, 92.9%)",
        "status": "completed",
        "activeForm": "Cross-checking SFT baseline numbers"
      },
      {
        "content": "Cross-check Prolog numbers in experiments/appendix",
        "status": "completed",
        "activeForm": "Cross-checking Prolog numbers"
      },
      {
        "content": "Check hard constraints (no 2.4x, hacking taxonomy 7, etc.)",
        "status": "completed",
        "activeForm": "Checking hard constraints from paper_framing"
      },
      {
        "content": "Check internal consistency between abstract/intro/experiments/conclusion",
        "status": "completed",
        "activeForm": "Checking internal consistency"
      },
      {
        "content": "Write consistency report to artifacts/",
        "status": "in_progress",
        "activeForm": "Writing consistency report"
      }
    ],
    "verificationNudgeNeeded": false
  },
  "sourceToolAssistantUUID": "e0f68da4-1bbf-4843-b2b6-c5f3afd8fc3a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "24e67ff1-1ea3-4bcf-a9e3-703eaa6cb36e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 74_

```json
{
  "type": "last-prompt",
  "leafUuid": "698a4fca-d773-44fb-9488-2b483c219469",
  "sessionId": "24e67ff1-1ea3-4bcf-a9e3-703eaa6cb36e"
}
```

---

### Runtime record

_source line 75_

```json
{
  "type": "ai-title",
  "aiTitle": "Audit paper figures against experiment registry",
  "sessionId": "24e67ff1-1ea3-4bcf-a9e3-703eaa6cb36e"
}
```

---

### Assistant

_source line 76 · 2026-05-14T21:47:49.023Z_

<details><summary>Logged reasoning block</summary>

```text

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "698a4fca-d773-44fb-9488-2b483c219469",
  "isSidechain": false,
  "requestId": "req_011Cb3CKXExNtbiaiAmGzEXZ",
  "type": "assistant",
  "uuid": "4df5846f-0c52-4c6a-90e6-27421a89e90b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "24e67ff1-1ea3-4bcf-a9e3-703eaa6cb36e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01MSS2cTqXWzVxxeT6P4B3Su",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 627,
      "cache_read_input_tokens": 115265,
      "output_tokens": 3537,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 627,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3537,
          "cache_read_input_tokens": 115265,
          "cache_creation_input_tokens": 627,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 627
          },
          "type": "message"
        }
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

_source line 77 · 2026-05-14T21:47:49.814Z_

Now let me check the ISR β=0.1 H1 row in Table 1 carefully — paper says 17% but pooled would be 18.2%.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4df5846f-0c52-4c6a-90e6-27421a89e90b",
  "isSidechain": false,
  "requestId": "req_011Cb3CKXExNtbiaiAmGzEXZ",
  "type": "assistant",
  "uuid": "3b010b9a-5626-4d9b-b750-cb43199e35b7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "24e67ff1-1ea3-4bcf-a9e3-703eaa6cb36e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01MSS2cTqXWzVxxeT6P4B3Su",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 627,
      "cache_read_input_tokens": 115265,
      "output_tokens": 3537,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 627,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3537,
          "cache_read_input_tokens": 115265,
          "cache_creation_input_tokens": 627,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 627
          },
          "type": "message"
        }
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

_source line 78 · 2026-05-14T21:47:52.247Z_

<details open><summary>🔧 Tool call — Grep · `toolu_017HwZYXP9VvE2dq1oLcH2LA`</summary>

```json
{
  "pattern": "ISR & 0.1|Random & 0.1|0\\.582|0\\.5816",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3b010b9a-5626-4d9b-b750-cb43199e35b7",
  "isSidechain": false,
  "requestId": "req_011Cb3CKXExNtbiaiAmGzEXZ",
  "type": "assistant",
  "uuid": "92494406-8c26-4daf-a4a6-5731d54d1ef2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "24e67ff1-1ea3-4bcf-a9e3-703eaa6cb36e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01MSS2cTqXWzVxxeT6P4B3Su",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 627,
      "cache_read_input_tokens": 115265,
      "output_tokens": 3537,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 627,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3537,
          "cache_read_input_tokens": 115265,
          "cache_creation_input_tokens": 627,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 627
          },
          "type": "message"
        }
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

_source line 79 · 2026-05-14T21:47:53.616Z_

<details><summary>↩ Tool result · `toolu_01JG2Jxj45TwVV5cNGAWaD8i`</summary>

```text
paper/appendix.tex:333:Ground-truth FOL
paper/appendix.tex:334:  & --- & --- & 0.18 & 0.559 & --- & --- & --- & Human formalizations \\
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9f43ae12-a83e-4fb5-b610-d436640c2df2",
  "isSidechain": false,
  "promptId": "c33bf5b5-c338-4f2f-97b8-e3e6d5f92819",
  "type": "user",
  "uuid": "dc332dfc-8951-439e-9404-26cad0e389d8",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "paper/appendix.tex:333:Ground-truth FOL\npaper/appendix.tex:334:  & --- & --- & 0.18 & 0.559 & --- & --- & --- & Human formalizations \\\\",
    "numLines": 2
  },
  "sourceToolAssistantUUID": "9f43ae12-a83e-4fb5-b610-d436640c2df2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "24e67ff1-1ea3-4bcf-a9e3-703eaa6cb36e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 80 · 2026-05-14T21:47:52.349Z_

<details><summary>↩ Tool result · `toolu_017HwZYXP9VvE2dq1oLcH2LA`</summary>

```text
paper/experiments.tex:61:ISR & 0.1 & 77{\scriptsize$\pm$14} & $\ddagger$ & \textbf{65} & 17 & ${\sim}$16 \\
paper/experiments.tex:62:Random & 0.1 & \textbf{85}{\scriptsize$\pm$6} & 0.086{\scriptsize$\pm$.04} & 0 & 81 & 19 \\
paper/appendix.tex:343:  & 44 & 500 & 0.98 & 0.582 & 100 & 0 & 0 & Tautological collapse \\
paper/figures/gen_fig4.py:18:fol_isr = [0.132, 0.000, 0.582]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "92494406-8c26-4daf-a4a6-5731d54d1ef2",
  "isSidechain": false,
  "promptId": "c33bf5b5-c338-4f2f-97b8-e3e6d5f92819",
  "type": "user",
  "uuid": "a3e55b68-4b44-4b72-9632-475b6afd12f6",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "paper/experiments.tex:61:ISR & 0.1 & 77{\\scriptsize$\\pm$14} & $\\ddagger$ & \\textbf{65} & 17 & ${\\sim}$16 \\\\\npaper/experiments.tex:62:Random & 0.1 & \\textbf{85}{\\scriptsize$\\pm$6} & 0.086{\\scriptsize$\\pm$.04} & 0 & 81 & 19 \\\\\npaper/appendix.tex:343:  & 44 & 500 & 0.98 & 0.582 & 100 & 0 & 0 & Tautological collapse \\\\\npaper/figures/gen_fig4.py:18:fol_isr = [0.132, 0.000, 0.582]",
    "numLines": 4
  },
  "sourceToolAssistantUUID": "92494406-8c26-4daf-a4a6-5731d54d1ef2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "24e67ff1-1ea3-4bcf-a9e3-703eaa6cb36e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 81 · 2026-05-14T21:47:53.554Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01JG2Jxj45TwVV5cNGAWaD8i`</summary>

```json
{
  "pattern": "0\\.557|0\\.559|0\\.55|sta-gt|ground.truth FOL",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/",
  "output_mode": "content",
  "-i": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a3e55b68-4b44-4b72-9632-475b6afd12f6",
  "isSidechain": false,
  "requestId": "req_011Cb3CKXExNtbiaiAmGzEXZ",
  "type": "assistant",
  "uuid": "9f43ae12-a83e-4fb5-b610-d436640c2df2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "24e67ff1-1ea3-4bcf-a9e3-703eaa6cb36e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01MSS2cTqXWzVxxeT6P4B3Su",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 627,
      "cache_read_input_tokens": 115265,
      "output_tokens": 3537,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 627,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3537,
          "cache_read_input_tokens": 115265,
          "cache_creation_input_tokens": 627,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 627
          },
          "type": "message"
        }
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

_source line 82 · 2026-05-14T21:47:57.294Z_

<details><summary>Logged reasoning block</summary>

```text

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dc332dfc-8951-439e-9404-26cad0e389d8",
  "isSidechain": false,
  "requestId": "req_011Cb3CNa3xWbJ53kfgTeqBX",
  "type": "assistant",
  "uuid": "eed3e366-302e-4849-8ae6-fb274392a3a7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "24e67ff1-1ea3-4bcf-a9e3-703eaa6cb36e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_017PrYSVUDGgTsDZE2pWvQhx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3914,
      "cache_read_input_tokens": 115892,
      "output_tokens": 330,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3914,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 330,
          "cache_read_input_tokens": 115892,
          "cache_creation_input_tokens": 3914,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3914
          },
          "type": "message"
        }
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

_source line 83 · 2026-05-14T21:47:58.182Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01575erGUrZgVxwnJD78gha8`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/ 2>/dev/null | head -20",
  "description": "Check artifacts directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "eed3e366-302e-4849-8ae6-fb274392a3a7",
  "isSidechain": false,
  "requestId": "req_011Cb3CNa3xWbJ53kfgTeqBX",
  "type": "assistant",
  "uuid": "8f3762dc-e8c0-4c4a-945c-0a99f54d4458",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "24e67ff1-1ea3-4bcf-a9e3-703eaa6cb36e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_017PrYSVUDGgTsDZE2pWvQhx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3914,
      "cache_read_input_tokens": 115892,
      "output_tokens": 330,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3914,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 330,
          "cache_read_input_tokens": 115892,
          "cache_creation_input_tokens": 3914,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3914
          },
          "type": "message"
        }
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

_source line 84 · 2026-05-14T21:47:58.278Z_

<details><summary>↩ Tool result · `toolu_01575erGUrZgVxwnJD78gha8`</summary>

```text
_deprecated
_project
analysis_random_vs_isr_b01_interim.md
claim_coverage_audit.md
component_count_analysis.md
diagnose_phase1_r3.md
dream_reports
evidence_chain_status.md
evidence_tables_d051.md
figure_quality_report.md
genuine_isr_crosscheck.md
grpo_exec_only.yaml
grpo_exec_sta.yaml
hacking_characterization_report.md
hacking_taxonomy.md
hacking_taxonomy_comparison.md
launch_phase1.sh
literature_goodhart.md
literature_map.yaml
manifest.yaml
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8f3762dc-e8c0-4c4a-945c-0a99f54d4458",
  "isSidechain": false,
  "promptId": "c33bf5b5-c338-4f2f-97b8-e3e6d5f92819",
  "type": "user",
  "uuid": "a75763cf-d68f-4354-b777-1e526b97d66f",
  "toolUseResult": {
    "stdout": "_deprecated\n_project\nanalysis_random_vs_isr_b01_interim.md\nclaim_coverage_audit.md\ncomponent_count_analysis.md\ndiagnose_phase1_r3.md\ndream_reports\nevidence_chain_status.md\nevidence_tables_d051.md\nfigure_quality_report.md\ngenuine_isr_crosscheck.md\ngrpo_exec_only.yaml\ngrpo_exec_sta.yaml\nhacking_characterization_report.md\nhacking_taxonomy.md\nhacking_taxonomy_comparison.md\nlaunch_phase1.sh\nliterature_goodhart.md\nliterature_map.yaml\nmanifest.yaml",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "8f3762dc-e8c0-4c4a-945c-0a99f54d4458",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "24e67ff1-1ea3-4bcf-a9e3-703eaa6cb36e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 85 · 2026-05-14T21:49:21.083Z_

<details open><summary>🔧 Tool call — Write · `toolu_01HKFqS3eeJ9MVRfqrnhopbX`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/data_consistency_report.md",
  "content": "# 论文数据一致性审查报告\n\n生成日期: 2026-05-14\n审查范围: `paper/{abstract,introduction,method,experiments,conclusion,related_work,appendix}.tex`\n数据源: `registry.yaml`（success/DONE 实验）+ `paper_framing.md`\n\n总体结论: **PASS（无 critical 数据错误）**。所有引用数字均可追溯至 registry，且与 `paper_framing.md` 一致。仅发现 2 处 minor 方法学不一致和 1 处需注意的约定（proved-only ISR 而非 mean ISR）——均不影响 paper claim 的正确性。\n\n---\n\n## 1. 数字一致性核对\n\n### 1.1 ISR 崩塌轨迹（abstract / intro / experiments §3.2 / appendix tab:beta01-3seed）\n\n| Step | 论文值 | Registry 来源 | Registry 实际值 | 状态 |\n|------|--------|---------------|------------------|------|\n| 100  | PR=32%, ISR=0.642 | plan003-eval-exec-only-r5 | prove_rate=0.32, proved_only_isr=0.6423 | ✓ |\n| 500  | PR=93%, ISR=0.132 | plan001-exec-only-s42-r2 | eval_prove_rate=0.93, eval_proved_only_isr=0.1324 | ✓ |\n| 1000 | PR=96%, ISR=0.003, components=18.55, 94.8% ISR=0 | plan016-extended-1000-s42 | prove_rate=0.96, isr=0.003 (proved_only=0.0028), components=18.55, isr_zero=94.8% | ✓ |\n\n**99.5% degradation** (abstract): (0.642 − 0.003)/0.642 = 99.53% ✓\n**−79.4% / −99.6%** (appendix): (0.642 − 0.132)/0.642 = 79.4%; (0.642 − 0.003)/0.642 = 99.5%。Appendix 写 −99.6% 实际是 99.5%，**rounding off by 0.1 pp**（minor，不需修）。\n\n### 1.2 PR 轨迹\n\n论文: 32% → 93% → 96%。Registry: 0.32 → 0.93 → 0.96。 ✓\n\n### 1.3 ISR β=0.1 三 seed (tab:beta01-3seed)\n\n| Seed | 论文 PR | 论文 ISR* | 论文 H7% | 论文 H1% | 论文 Gen% | Registry plan | Registry 实际 | 状态 |\n|------|---------|-----------|----------|----------|-----------|---------------|---------------|------|\n| s42 | 0.81 | 0.415 | 16.0 | 51.9 | 30.9 | plan002-additive-b01-s42 | PR=0.81, ISR*=0.4154, h7=0.16, h1=0.519, genuine=0.309 | ✓ |\n| s43 | 0.61 | 0.830 | 96.7 | 0 | ~3 | plan002-additive-b01-s43 | PR=0.61, ISR*=0.8301, h7=0.967, h1=0 | ✓ |\n| s44 | 0.89 | 0.902 | 86.5 | 0 | ~13.5 | plan002-additive-b01-s44 | PR=0.89, mean_isr=0.803 → proved_only=0.803/0.89=0.902, h7=0.865 | ✓ |\n\n3-seed mean: PR=0.77±0.14, ISR*=0.716±0.26。重新计算：\n- PR mean=(0.81+0.61+0.89)/3=0.770; std≈0.144 ✓\n- ISR mean=(0.415+0.830+0.902)/3=0.716; std≈0.262 ✓\n\n### 1.4 Random β=0.1 三 seed (tab:beta01-3seed)\n\n| Seed | 论文 PR | 论文 ISR* | 论文 H7% | 论文 H1% | 论文 Gen% | Registry plan | Registry 实际 | 状态 |\n|------|---------|-----------|----------|----------|-----------|---------------|---------------|------|\n| s42 | 0.79 | 0.131 | 0 | 70.9 | 29.1 | plan018-additive-random-b01-s42 | PR=0.79, ISR*=0.1314 | ✓ |\n| s43 | 0.88 | 0.058 | 0 | 93.2 | 6.8 | plan018-additive-random-b01-s43-r2 | h1_rate=93.2, genuine_rate=6.8 (PR/ISR 在 framing 中确认) | ✓ |\n| s44 | 0.89 | 0.070 | 0 | 79.8 | 20.2 | plan018-additive-random-b01-s44 | PR=0.89, ISR*=0.0695 | ✓ |\n\n3-seed mean: PR=0.85±0.06, ISR*=0.086±0.039。重算：\n- PR mean=(0.79+0.88+0.89)/3=0.853; std≈0.055 ✓\n- ISR mean=(0.131+0.058+0.070)/3=0.0863; std≈0.039 ✓\n\n### 1.5 SFT Baseline\n\n| 指标 | 论文值 | Registry plan009-sft-baseline-s42-r4 | 状态 |\n|------|--------|--------------------------------------|------|\n| PR | 14% | 0.14 | ✓ |\n| ISR* | 0.571 | 0.571 | ✓ |\n| H7 | 0/14 (0%) | h7_count=0 | ✓ |\n| H1 | 1/14 (7.1%) | h1_count=1, h1_rate=0.071 | ✓ |\n| Genuine | 13/14 (92.9%) | genuine_count=13, genuine_rate=0.929 | ✓ |\n\n### 1.6 Prolog 数字 (tab:prolog-crosslogic / §3.3)\n\n**Exec-only:**\n| Seed | 论文 PR | 论文 ISR* | Registry | 状态 |\n|------|---------|-----------|----------|------|\n| s42 | 0.83 | 0.037 | plan006-prolog-exec-s42: PR=0.83, ISR*=0.037 | ✓ |\n| s43 | 0.56 | 0.015 | plan006-prolog-exec-s43-r3: PR=0.56, ISR*=0.015 | ✓ |\n| s44 | 0.21 | 0.387 | plan006-prolog-exec-s44: PR=0.21, ISR*=0.3866 | ✓ |\n\n3-seed mean: PR=0.53±0.31, ISR=0.146±0.21\n- (0.037+0.015+0.387)/3 = 0.146 ✓\n- std≈0.213 ✓\n\n**Exec+ISR (STA reward):**\n| Seed | 论文 PR | 论文 ISR* | 论文 H7% | 论文 H1% | Registry | 状态 |\n|------|---------|-----------|----------|----------|----------|------|\n| s42 | 0.50 | 1.000 | 100 | 0 | plan006-prolog-sta-s42: PR=0.5, ISR*=1, h7=1 | ✓ |\n| s43 | 0.38 | 0.185 | 0 (strict; functional 100%) | 97.4 | plan006-prolog-sta-s43: PR=0.38, ISR*=0.1853, h7=0, h1=37/38=97.4% | ✓ |\n| s44 | 0.97 | 0.912 | 0 (strict; functional 95/97) | 0 | plan006-prolog-sta-s44: PR=0.97, mean_isr=0.885 → proved_only=0.885/0.97=0.9124 | ✓ |\n\n3-seed mean: PR=0.62±0.31, ISR=0.699±0.45\n- (0.5+0.38+0.97)/3=0.617 ✓\n- (1.0+0.185+0.912)/3=0.699 ✓\n\n### 1.7 1000-step extended run (§3.2)\n\n论文: ISR=0.003, 94.8% ISR=0, mean components 18.55, H1=100%, Gen=0%。\nRegistry plan016-extended-1000-s42: isr=0.003, components=18.55, h1_rate=1, genuine_rate=0, n_necessary=0 ratio=94.8%。 ✓\n\n### 1.8 Exec-only 跨 seed (§3.2)\n\n| Seed | 论文 PR | 论文 ISR* | Registry | 状态 |\n|------|---------|-----------|----------|------|\n| s42 | 0.93, H1=87.1% | — | plan001-exec-only-s42-r2: PR=0.93, h1=0.871 | ✓ |\n| s43 | 0.14, ISR=0 | sampling T=0.7 | plan001-exec-only-s43-r4: sampling_PR=0.14, sampling_ISR=0 | ✓ |\n| s44 | 0.98, H7=100%, components=2.04 | — | plan001-exec-only-s44: PR=0.98, h7=1, components=2.04 | ✓ |\n\n3-seed PR σ=±47pp: std(0.93, 0.14, 0.98)=0.471 ✓\n\n### 1.9 其他基线 (appendix tab:beta01-3seed)\n\n| 行 | 论文值 | Registry | 状态 |\n|----|--------|----------|------|\n| Base model (no training) | PR=0.12, ISR=0.064 | sta-phase0-baseline: prove_rate=0.12, mean_isr=0.0641 | ✓ |\n| Ground-truth FOL | PR=0.18, ISR=0.559 | sta-gt-isr-baseline: prove_rate=0.18, mean_isr=0.5588 | ✓ |\n\n### 1.10 Random β=0.3 (Goodhart landscape)\n\n论文: PR=48, ISR=0.094, components=9.6。\nRegistry plan017-additive-random-s42: PR=0.48, ISR*=0.0943, components=9.6。 ✓\n\n### 1.11 ISR β=0.3 (无独立 eval registry 项)\n\n论文: PR=18, ISR*=0.143。\nRegistry plan002-additive-b03-s42 仅记录训练统计（无 eval_*），但与 framing 一致：framing 给出 mean_isr=0.026，而 0.143 × 0.18 = 0.0257 ≈ 0.026，所以 paper 的 0.143（proved-only）与 framing 的 0.026（mean）数学一致。 ✓\n\n### 1.12 Premise-count-matched (§3.2 / Limitations)\n\n论文: 1.06× (ISR-genuine ISR=0.258 n=11 vs random-genuine ISR=0.243 n=21)。\nFraming: ISR s42 genuine n_prem≥3: n=11, mean ISR=0.2578; Random s42 genuine n_prem≥3: n=21, mean ISR=0.2434。Ratio=1.06×。 ✓\n\n### 1.13 Component-count s42\n\n论文: ISR s42 mean=5.58 components, Random s42 mean=8.46 components。\nRegistry plan002-b01-s42: component_count_mean=5.58。plan018-random-s42: component_count_mean=8.46。 ✓\n\n### 1.14 NLI Limitation (Conclusion / Appendix)\n\n论文: Spearman ρ=−0.049, p=0.187。\nRegistry plan014-downstream-nli-s42: spearman_rho=-0.049, spearman_p=0.187。 ✓\n\n### 1.15 H7 pooled rate\n\n论文: 64.5% (149/231), Random 0% (0/256)。\n- ISR pooled: (13 + 59 + 77)/(81+61+89) = 149/231 = 64.50% ✓\n- Random pooled: (0+0+0)/(79+88+89) = 0/256 ✓\n\n---\n\n## 2. 硬约束检查\n\n| 约束 | 状态 | 证据 |\n|------|------|------|\n| D051: \"2.4x\" 已作废，不应出现 | ✅ PASS | grep `2\\.4(x|×|\\\\times)` 在 paper/*.tex 0 matches |\n| 旧的 \"3.2x\" 也已移除 | ✅ PASS | grep `3\\.2(x|×|\\\\times)` 0 matches |\n| Hacking taxonomy = 7 modes (非 6) | ✅ PASS | abstract/method/conclusion/appendix 均说 \"seven\" / \"7\"。`six modes` 0 matches |\n| ISR β=0.1 不应标 \"no hacking\" | ✅ PASS | \"near-zero hacking\" 仅用于 SFT (92.9% genuine)；ISR β=0.1 在论文中明确标注 H7 主导 |\n| s44 Prolog STA: query-as-fact gaming, 0% genuine | ✅ PASS | appendix tab:prolog-crosslogic 标 Gen=0%，footnote $^b$ 解释功能性 H7 (95/97) |\n| plan013 vs plan017 不简化为 \"additive vs convex\" | ✅ PASS | grep 0 matches |\n| C006: ISR 双语义区分（exec-only low ISR=冗余编码 vs ISR-reward high ISR=metric gaming） | ✅ PASS | conclusion §\"Interpreting ISR\" 和 appendix §\"What ISR measures\" 均明确区分 |\n\n---\n\n## 3. 内部一致性检查\n\n### 3.1 跨章节核心数字一致\n\n- 93% PR + 87% H1: abstract / intro / experiments §3.2 / appendix。一致 ✓\n- 64.5% H7 vs 0% random: abstract / intro / experiments §3.2 / appendix。一致 ✓\n- 1.06× premise-matched: abstract / intro §1 / experiments §3.2 / appendix。一致 ✓\n- 18% vs 48%（β=0.3 ISR vs Random）: abstract / intro / experiments §3.2 / appendix。一致 ✓\n- 92.9% genuine SFT: abstract / intro / experiments §3.1 / Table 1 / appendix。一致 ✓\n- 3/3 Prolog seeds gaming, 0% genuine: abstract / intro / experiments §3.3 / conclusion / appendix。一致 ✓\n- 7 hacking modes: method §2.4 / experiments §3.4 / conclusion / appendix §C。一致 ✓\n- 6 reward conditions: method §2.3 / experiments §3 setup / conclusion。一致 ✓ (Exec-only / ISR β=0.1 / ISR β=0.3 / Random β=0.1 / Random β=0.3 / SFT = 6)\n- ISR 崩塌 0.642→0.132→0.003: abstract / intro / experiments §3.2 / appendix §F。一致 ✓\n\n### 3.2 交叉引用\n\n所有 `\\ref{}` 标签均能在 paper/*.tex 找到对应定义：\n- sec:setup, sec:diagnostic, sec:goodhart, sec:crosslogic, sec:taxonomy, sec:taxonomy-method, sec:method, sec:task, sec:sta, sec:rewards, sec:experiments, sec:related-work ✓\n- fig:sta-overview, fig:isr-collapse, fig:hacking-composition, fig:prolog-comparison ✓\n- tab:goodhart-landscape, tab:hyperparams, tab:hacking-taxonomy-app, tab:fol-detailed / tab:beta01-3seed, tab:prolog-detailed / tab:prolog-crosslogic ✓\n- alg:sta ✓\n- eq:isr ✓\n- app:setup, app:algorithm, app:extended-discussion, app:hacking-modes, app:detailed-results ✓\n\n### 3.3 Minor 内部不一致\n\n#### 3.3.1 H1 mean 算法不一致（simple mean vs pooled）\n\n- **H7 ISR β=0.1 (论文 65%)**: pooled = 149/231 = 64.5% → 论文用 pooled\n- **H1 ISR β=0.1 (论文 17%)**: simple mean = (51.9+0+0)/3 = 17.3% vs pooled = 42/231 = 18.2% → 论文用 simple mean\n\n这与 framing 一致（framing 也是混用），但同一行同一指标用两种平均方法略不规范。**Impact: 0.8pp 差异，不影响 claim**。\n\n建议：在 caption 或正文 footnote 中说明 H7/H1 用 simple mean of seeds（而非 pooled）。\n\n#### 3.3.2 Appendix line 414 微小 rounding\n\n> \"ISR$^*=0.642$ at 100 steps $\\to$ $0.132$ at 500 steps ($-79.4$\\%) $\\to$ $0.003$ at 1000 steps ($-99.6$\\% from step 100).\"\n\n(0.642−0.003)/0.642 = 0.9953 = **99.5%**，paper 写 99.6%。Abstract 写 99.5%（正确）。\n\n**建议**：把 appendix 改为 99.5%，与 abstract 对齐。\n\n#### 3.3.3 Appendix tab:beta01-3seed exec-only s44 ISR* = 0.582\n\nRegistry 值 0.5816 — 四舍五入应为 0.582 ✓。但 framing 文本写 0.57（粗略），paper 用更精确的 0.582。无问题。\n\n#### 3.3.4 Proved-only vs mean ISR 表达约定\n\nPaper 全文使用 ISR* = proved-only。Registry 中部分 metrics 仅存 mean_isr（all samples，含 unproved=0）。当看到 paper 给的 0.902 (ISR s44) vs registry 0.803 (mean_isr) 时，需理解：proved_only = mean_isr / PR (∵ unproved=0)。\n\n- ISR β=0.1 s44: 0.803/0.89 = 0.902 ✓\n- Prolog STA s44: 0.885/0.97 = 0.912 ✓\n- ISR β=0.3 s42: 0.0257/0.18 = 0.143 ✓ (framing 写 0.026 = mean, paper 写 0.143 = proved-only)\n- Random β=0.3 s42: 0.0453/0.48 = 0.0944 ✓\n\n约定一致，无错误。但**建议在 §3.1 Setup 中明确 footnote**：「除非另有说明，所有 ISR 报告均为 proved-only ISR* ≡ mean of ISR over proved samples」。Setup 已在第 13 行说明「we report ... proved-only ISR (ISR*, over proved samples only)」，已 OK。\n\n---\n\n## 4. 总结与建议修改\n\n### 4.1 总体评价\n\n**论文数据层面 PASS**。所有定量 claim 均可追溯至 registry，跨章节一致，硬约束全部遵守。\n\n### 4.2 建议修改（均为 minor）\n\n1. **Appendix line 414**: `−99.6%` → `−99.5%` 以与 abstract 99.5% 对齐。\n2. **Table 1 caption 或 §3.2 footnote**: 添加一句说明 3-seed mean H7/H1 是 simple mean across seeds（非 pooled），以避免审稿人质疑 H7=65% 与 H1=17% 计算口径差异。\n3. **可选**: appendix line 388 Prolog STA s44 后 footnote $^b$ 提到「strict classifier reports Genuine=100%」，但表中已经写 Gen=0%（覆盖），建议在表内 Gen 列标注 `0$^b$` 或类似显眼标记，避免读者误读 ground-truth 标签。当前 footnote 在右下角，可能被忽略。\n\n### 4.3 无 critical 错误\n\n- 没有引用作废的 2.4× 优势\n- 没有混淆 binary _fast_fn 训练 ISR 与 full STA eval ISR\n- 没有把 s44 Prolog STA 误标为 genuine\n- 7-mode taxonomy 全文一致\n- C001 数据约束（train_500_seed42.jsonl）在 setup 和 appendix 均明确\n\n报告结束。\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a75763cf-d68f-4354-b777-1e526b97d66f",
  "isSidechain": false,
  "requestId": "req_011Cb3CNunNGEziD21dtooRu",
  "type": "assistant",
  "uuid": "1887bbef-f1f4-4e26-8856-69932f4f18ec",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "24e67ff1-1ea3-4bcf-a9e3-703eaa6cb36e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01GkiUs1jdXbNbm5qpFu7rhb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 564,
      "cache_read_input_tokens": 119806,
      "output_tokens": 7110,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 564,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 7110,
          "cache_read_input_tokens": 119806,
          "cache_creation_input_tokens": 564,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 564
          },
          "type": "message"
        }
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

_source line 86 · 2026-05-14T21:49:21.125Z_

<details><summary>↩ Tool result · `toolu_01HKFqS3eeJ9MVRfqrnhopbX`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/data_consistency_report.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1887bbef-f1f4-4e26-8856-69932f4f18ec",
  "isSidechain": false,
  "promptId": "c33bf5b5-c338-4f2f-97b8-e3e6d5f92819",
  "type": "user",
  "uuid": "88c03bc5-c631-41cb-b71c-bf1a6dec069c",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/data_consistency_report.md",
    "content": "# 论文数据一致性审查报告\n\n生成日期: 2026-05-14\n审查范围: `paper/{abstract,introduction,method,experiments,conclusion,related_work,appendix}.tex`\n数据源: `registry.yaml`（success/DONE 实验）+ `paper_framing.md`\n\n总体结论: **PASS（无 critical 数据错误）**。所有引用数字均可追溯至 registry，且与 `paper_framing.md` 一致。仅发现 2 处 minor 方法学不一致和 1 处需注意的约定（proved-only ISR 而非 mean ISR）——均不影响 paper claim 的正确性。\n\n---\n\n## 1. 数字一致性核对\n\n### 1.1 ISR 崩塌轨迹（abstract / intro / experiments §3.2 / appendix tab:beta01-3seed）\n\n| Step | 论文值 | Registry 来源 | Registry 实际值 | 状态 |\n|------|--------|---------------|------------------|------|\n| 100  | PR=32%, ISR=0.642 | plan003-eval-exec-only-r5 | prove_rate=0.32, proved_only_isr=0.6423 | ✓ |\n| 500  | PR=93%, ISR=0.132 | plan001-exec-only-s42-r2 | eval_prove_rate=0.93, eval_proved_only_isr=0.1324 | ✓ |\n| 1000 | PR=96%, ISR=0.003, components=18.55, 94.8% ISR=0 | plan016-extended-1000-s42 | prove_rate=0.96, isr=0.003 (proved_only=0.0028), components=18.55, isr_zero=94.8% | ✓ |\n\n**99.5% degradation** (abstract): (0.642 − 0.003)/0.642 = 99.53% ✓\n**−79.4% / −99.6%** (appendix): (0.642 − 0.132)/0.642 = 79.4%; (0.642 − 0.003)/0.642 = 99.5%。Appendix 写 −99.6% 实际是 99.5%，**rounding off by 0.1 pp**（minor，不需修）。\n\n### 1.2 PR 轨迹\n\n论文: 32% → 93% → 96%。Registry: 0.32 → 0.93 → 0.96。 ✓\n\n### 1.3 ISR β=0.1 三 seed (tab:beta01-3seed)\n\n| Seed | 论文 PR | 论文 ISR* | 论文 H7% | 论文 H1% | 论文 Gen% | Registry plan | Registry 实际 | 状态 |\n|------|---------|-----------|----------|----------|-----------|---------------|---------------|------|\n| s42 | 0.81 | 0.415 | 16.0 | 51.9 | 30.9 | plan002-additive-b01-s42 | PR=0.81, ISR*=0.4154, h7=0.16, h1=0.519, genuine=0.309 | ✓ |\n| s43 | 0.61 | 0.830 | 96.7 | 0 | ~3 | plan002-additive-b01-s43 | PR=0.61, ISR*=0.8301, h7=0.967, h1=0 | ✓ |\n| s44 | 0.89 | 0.902 | 86.5 | 0 | ~13.5 | plan002-additive-b01-s44 | PR=0.89, mean_isr=0.803 → proved_only=0.803/0.89=0.902, h7=0.865 | ✓ |\n\n3-seed mean: PR=0.77±0.14, ISR*=0.716±0.26。重新计算：\n- PR mean=(0.81+0.61+0.89)/3=0.770; std≈0.144 ✓\n- ISR mean=(0.415+0.830+0.902)/3=0.716; std≈0.262 ✓\n\n### 1.4 Random β=0.1 三 seed (tab:beta01-3seed)\n\n| Seed | 论文 PR | 论文 ISR* | 论文 H7% | 论文 H1% | 论文 Gen% | Registry plan | Registry 实际 | 状态 |\n|------|---------|-----------|----------|----------|-----------|---------------|---------------|------|\n| s42 | 0.79 | 0.131 | 0 | 70.9 | 29.1 | plan018-additive-random-b01-s42 | PR=0.79, ISR*=0.1314 | ✓ |\n| s43 | 0.88 | 0.058 | 0 | 93.2 | 6.8 | plan018-additive-random-b01-s43-r2 | h1_rate=93.2, genuine_rate=6.8 (PR/ISR 在 framing 中确认) | ✓ |\n| s44 | 0.89 | 0.070 | 0 | 79.8 | 20.2 | plan018-additive-random-b01-s44 | PR=0.89, ISR*=0.0695 | ✓ |\n\n3-seed mean: PR=0.85±0.06, ISR*=0.086±0.039。重算：\n- PR mean=(0.79+0.88+0.89)/3=0.853; std≈0.055 ✓\n- ISR mean=(0.131+0.058+0.070)/3=0.0863; std≈0.039 ✓\n\n### 1.5 SFT Baseline\n\n| 指标 | 论文值 | Registry plan009-sft-baseline-s42-r4 | 状态 |\n|------|--------|--------------------------------------|------|\n| PR | 14% | 0.14 | ✓ |\n| ISR* | 0.571 | 0.571 | ✓ |\n| H7 | 0/14 (0%) | h7_count=0 | ✓ |\n| H1 | 1/14 (7.1%) | h1_count=1, h1_rate=0.071 | ✓ |\n| Genuine | 13/14 (92.9%) | genuine_count=13, genuine_rate=0.929 | ✓ |\n\n### 1.6 Prolog 数字 (tab:prolog-crosslogic / §3.3)\n\n**Exec-only:**\n| Seed | 论文 PR | 论文 ISR* | Registry | 状态 |\n|------|---------|-----------|----------|------|\n| s42 | 0.83 | 0.037 | plan006-prolog-exec-s42: PR=0.83, ISR*=0.037 | ✓ |\n| s43 | 0.56 | 0.015 | plan006-prolog-exec-s43-r3: PR=0.56, ISR*=0.015 | ✓ |\n| s44 | 0.21 | 0.387 | plan006-prolog-exec-s44: PR=0.21, ISR*=0.3866 | ✓ |\n\n3-seed mean: PR=0.53±0.31, ISR=0.146±0.21\n- (0.037+0.015+0.387)/3 = 0.146 ✓\n- std≈0.213 ✓\n\n**Exec+ISR (STA reward):**\n| Seed | 论文 PR | 论文 ISR* | 论文 H7% | 论文 H1% | Registry | 状态 |\n|------|---------|-----------|----------|----------|----------|------|\n| s42 | 0.50 | 1.000 | 100 | 0 | plan006-prolog-sta-s42: PR=0.5, ISR*=1, h7=1 | ✓ |\n| s43 | 0.38 | 0.185 | 0 (strict; functional 100%) | 97.4 | plan006-prolog-sta-s43: PR=0.38, ISR*=0.1853, h7=0, h1=37/38=97.4% | ✓ |\n| s44 | 0.97 | 0.912 | 0 (strict; functional 95/97) | 0 | plan006-prolog-sta-s44: PR=0.97, mean_isr=0.885 → proved_only=0.885/0.97=0.9124 | ✓ |\n\n3-seed mean: PR=0.62±0.31, ISR=0.699±0.45\n- (0.5+0.38+0.97)/3=0.617 ✓\n- (1.0+0.185+0.912)/3=0.699 ✓\n\n### 1.7 1000-step extended run (§3.2)\n\n论文: ISR=0.003, 94.8% ISR=0, mean components 18.55, H1=100%, Gen=0%。\nRegistry plan016-extended-1000-s42: isr=0.003, components=18.55, h1_rate=1, genuine_rate=0, n_necessary=0 ratio=94.8%。 ✓\n\n### 1.8 Exec-only 跨 seed (§3.2)\n\n| Seed | 论文 PR | 论文 ISR* | Registry | 状态 |\n|------|---------|-----------|----------|------|\n| s42 | 0.93, H1=87.1% | — | plan001-exec-only-s42-r2: PR=0.93, h1=0.871 | ✓ |\n| s43 | 0.14, ISR=0 | sampling T=0.7 | plan001-exec-only-s43-r4: sampling_PR=0.14, sampling_ISR=0 | ✓ |\n| s44 | 0.98, H7=100%, components=2.04 | — | plan001-exec-only-s44: PR=0.98, h7=1, components=2.04 | ✓ |\n\n3-seed PR σ=±47pp: std(0.93, 0.14, 0.98)=0.471 ✓\n\n### 1.9 其他基线 (appendix tab:beta01-3seed)\n\n| 行 | 论文值 | Registry | 状态 |\n|----|--------|----------|------|\n| Base model (no training) | PR=0.12, ISR=0.064 | sta-phase0-baseline: prove_rate=0.12, mean_isr=0.0641 | ✓ |\n| Ground-truth FOL | PR=0.18, ISR=0.559 | sta-gt-isr-baseline: prove_rate=0.18, mean_isr=0.5588 | ✓ |\n\n### 1.10 Random β=0.3 (Goodhart landscape)\n\n论文: PR=48, ISR=0.094, components=9.6。\nRegistry plan017-additive-random-s42: PR=0.48, ISR*=0.0943, components=9.6。 ✓\n\n### 1.11 ISR β=0.3 (无独立 eval registry 项)\n\n论文: PR=18, ISR*=0.143。\nRegistry plan002-additive-b03-s42 仅记录训练统计（无 eval_*），但与 framing 一致：framing 给出 mean_isr=0.026，而 0.143 × 0.18 = 0.0257 ≈ 0.026，所以 paper 的 0.143（proved-only）与 framing 的 0.026（mean）数学一致。 ✓\n\n### 1.12 Premise-count-matched (§3.2 / Limitations)\n\n论文: 1.06× (ISR-genuine ISR=0.258 n=11 vs random-genuine ISR=0.243 n=21)。\nFraming: ISR s42 genuine n_prem≥3: n=11, mean ISR=0.2578; Random s42 genuine n_prem≥3: n=21, mean ISR=0.2434。Ratio=1.06×。 ✓\n\n### 1.13 Component-count s42\n\n论文: ISR s42 mean=5.58 components, Random s42 mean=8.46 components。\nRegistry plan002-b01-s42: component_count_mean=5.58。plan018-random-s42: component_count_mean=8.46。 ✓\n\n### 1.14 NLI Limitation (Conclusion / Appendix)\n\n论文: Spearman ρ=−0.049, p=0.187。\nRegistry plan014-downstream-nli-s42: spearman_rho=-0.049, spearman_p=0.187。 ✓\n\n### 1.15 H7 pooled rate\n\n论文: 64.5% (149/231), Random 0% (0/256)。\n- ISR pooled: (13 + 59 + 77)/(81+61+89) = 149/231 = 64.50% ✓\n- Random pooled: (0+0+0)/(79+88+89) = 0/256 ✓\n\n---\n\n## 2. 硬约束检查\n\n| 约束 | 状态 | 证据 |\n|------|------|------|\n| D051: \"2.4x\" 已作废，不应出现 | ✅ PASS | grep `2\\.4(x|×|\\\\times)` 在 paper/*.tex 0 matches |\n| 旧的 \"3.2x\" 也已移除 | ✅ PASS | grep `3\\.2(x|×|\\\\times)` 0 matches |\n| Hacking taxonomy = 7 modes (非 6) | ✅ PASS | abstract/method/conclusion/appendix 均说 \"seven\" / \"7\"。`six modes` 0 matches |\n| ISR β=0.1 不应标 \"no hacking\" | ✅ PASS | \"near-zero hacking\" 仅用于 SFT (92.9% genuine)；ISR β=0.1 在论文中明确标注 H7 主导 |\n| s44 Prolog STA: query-as-fact gaming, 0% genuine | ✅ PASS | appendix tab:prolog-crosslogic 标 Gen=0%，footnote $^b$ 解释功能性 H7 (95/97) |\n| plan013 vs plan017 不简化为 \"additive vs convex\" | ✅ PASS | grep 0 matches |\n| C006: ISR 双语义区分（exec-only low ISR=冗余编码 vs ISR-reward high ISR=metric gaming） | ✅ PASS | conclusion §\"Interpreting ISR\" 和 appendix §\"What ISR measures\" 均明确区分 |\n\n---\n\n## 3. 内部一致性检查\n\n### 3.1 跨章节核心数字一致\n\n- 93% PR + 87% H1: abstract / intro / experiments §3.2 / appendix。一致 ✓\n- 64.5% H7 vs 0% random: abstract / intro / experiments §3.2 / appendix。一致 ✓\n- 1.06× premise-matched: abstract / intro §1 / experiments §3.2 / appendix。一致 ✓\n- 18% vs 48%（β=0.3 ISR vs Random）: abstract / intro / experiments §3.2 / appendix。一致 ✓\n- 92.9% genuine SFT: abstract / intro / experiments §3.1 / Table 1 / appendix。一致 ✓\n- 3/3 Prolog seeds gaming, 0% genuine: abstract / intro / experiments §3.3 / conclusion / appendix。一致 ✓\n- 7 hacking modes: method §2.4 / experiments §3.4 / conclusion / appendix §C。一致 ✓\n- 6 reward conditions: method §2.3 / experiments §3 setup / conclusion。一致 ✓ (Exec-only / ISR β=0.1 / ISR β=0.3 / Random β=0.1 / Random β=0.3 / SFT = 6)\n- ISR 崩塌 0.642→0.132→0.003: abstract / intro / experiments §3.2 / appendix §F。一致 ✓\n\n### 3.2 交叉引用\n\n所有 `\\ref{}` 标签均能在 paper/*.tex 找到对应定义：\n- sec:setup, sec:diagnostic, sec:goodhart, sec:crosslogic, sec:taxonomy, sec:taxonomy-method, sec:method, sec:task, sec:sta, sec:rewards, sec:experiments, sec:related-work ✓\n- fig:sta-overview, fig:isr-collapse, fig:hacking-composition, fig:prolog-comparison ✓\n- tab:goodhart-landscape, tab:hyperparams, tab:hacking-taxonomy-app, tab:fol-detailed / tab:beta01-3seed, tab:prolog-detailed / tab:prolog-crosslogic ✓\n- alg:sta ✓\n- eq:isr ✓\n- app:setup, app:algorithm, app:extended-discussion, app:hacking-modes, app:detailed-results ✓\n\n### 3.3 Minor 内部不一致\n\n#### 3.3.1 H1 mean 算法不一致（simple mean vs pooled）\n\n- **H7 ISR β=0.1 (论文 65%)**: pooled = 149/231 = 64.5% → 论文用 pooled\n- **H1 ISR β=0.1 (论文 17%)**: simple mean = (51.9+0+0)/3 = 17.3% vs pooled = 42/231 = 18.2% → 论文用 simple mean\n\n这与 framing 一致（framing 也是混用），但同一行同一指标用两种平均方法略不规范。**Impact: 0.8pp 差异，不影响 claim**。\n\n建议：在 caption 或正文 footnote 中说明 H7/H1 用 simple mean of seeds（而非 pooled）。\n\n#### 3.3.2 Appendix line 414 微小 rounding\n\n> \"ISR$^*=0.642$ at 100 steps $\\to$ $0.132$ at 500 steps ($-79.4$\\%) $\\to$ $0.003$ at 1000 steps ($-99.6$\\% from step 100).\"\n\n(0.642−0.003)/0.642 = 0.9953 = **99.5%**，paper 写 99.6%。Abstract 写 99.5%（正确）。\n\n**建议**：把 appendix 改为 99.5%，与 abstract 对齐。\n\n#### 3.3.3 Appendix tab:beta01-3seed exec-only s44 ISR* = 0.582\n\nRegistry 值 0.5816 — 四舍五入应为 0.582 ✓。但 framing 文本写 0.57（粗略），paper 用更精确的 0.582。无问题。\n\n#### 3.3.4 Proved-only vs mean ISR 表达约定\n\nPaper 全文使用 ISR* = proved-only。Registry 中部分 metrics 仅存 mean_isr（all samples，含 unproved=0）。当看到 paper 给的 0.902 (ISR s44) vs registry 0.803 (mean_isr) 时，需理解：proved_only = mean_isr / PR (∵ unproved=0)。\n\n- ISR β=0.1 s44: 0.803/0.89 = 0.902 ✓\n- Prolog STA s44: 0.885/0.97 = 0.912 ✓\n- ISR β=0.3 s42: 0.0257/0.18 = 0.143 ✓ (framing 写 0.026 = mean, paper 写 0.143 = proved-only)\n- Random β=0.3 s42: 0.0453/0.48 = 0.0944 ✓\n\n约定一致，无错误。但**建议在 §3.1 Setup 中明确 footnote**：「除非另有说明，所有 ISR 报告均为 proved-only ISR* ≡ mean of ISR over proved samples」。Setup 已在第 13 行说明「we report ... proved-only ISR (ISR*, over proved samples only)」，已 OK。\n\n---\n\n## 4. 总结与建议修改\n\n### 4.1 总体评价\n\n**论文数据层面 PASS**。所有定量 claim 均可追溯至 registry，跨章节一致，硬约束全部遵守。\n\n### 4.2 建议修改（均为 minor）\n\n1. **Appendix line 414**: `−99.6%` → `−99.5%` 以与 abstract 99.5% 对齐。\n2. **Table 1 caption 或 §3.2 footnote**: 添加一句说明 3-seed mean H7/H1 是 simple mean across seeds（非 pooled），以避免审稿人质疑 H7=65% 与 H1=17% 计算口径差异。\n3. **可选**: appendix line 388 Prolog STA s44 后 footnote $^b$ 提到「strict classifier reports Genuine=100%」，但表中已经写 Gen=0%（覆盖），建议在表内 Gen 列标注 `0$^b$` 或类似显眼标记，避免读者误读 ground-truth 标签。当前 footnote 在右下角，可能被忽略。\n\n### 4.3 无 critical 错误\n\n- 没有引用作废的 2.4× 优势\n- 没有混淆 binary _fast_fn 训练 ISR 与 full STA eval ISR\n- 没有把 s44 Prolog STA 误标为 genuine\n- 7-mode taxonomy 全文一致\n- C001 数据约束（train_500_seed42.jsonl）在 setup 和 appendix 均明确\n\n报告结束。\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "1887bbef-f1f4-4e26-8856-69932f4f18ec",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "24e67ff1-1ea3-4bcf-a9e3-703eaa6cb36e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 87_

```json
{
  "type": "last-prompt",
  "leafUuid": "88c03bc5-c631-41cb-b71c-bf1a6dec069c",
  "sessionId": "24e67ff1-1ea3-4bcf-a9e3-703eaa6cb36e"
}
```

---

### Runtime record

_source line 88_

```json
{
  "type": "ai-title",
  "aiTitle": "Audit paper figures against experiment registry",
  "sessionId": "24e67ff1-1ea3-4bcf-a9e3-703eaa6cb36e"
}
```

---

### Tool call

_source line 89 · 2026-05-14T21:49:29.120Z_

<details open><summary>🔧 Tool call — TodoWrite · `toolu_01CoDRLAgJFsqimuJFXYwLoD`</summary>

```json
{
  "todos": [
    {
      "content": "Read all paper sections (conclusion, related_work, appendix)",
      "activeForm": "Reading remaining paper sections",
      "status": "completed"
    },
    {
      "content": "Cross-check ISR collapse trajectory numbers (0.642/0.132/0.003)",
      "activeForm": "Cross-checking ISR collapse numbers",
      "status": "completed"
    },
    {
      "content": "Cross-check 3-seed β=0.1 ISR/Random numbers in Table 1 and appendix",
      "activeForm": "Cross-checking β=0.1 3-seed numbers",
      "status": "completed"
    },
    {
      "content": "Cross-check SFT baseline numbers (PR=14%, ISR=0.571, 92.9%)",
      "activeForm": "Cross-checking SFT baseline numbers",
      "status": "completed"
    },
    {
      "content": "Cross-check Prolog numbers in experiments/appendix",
      "activeForm": "Cross-checking Prolog numbers",
      "status": "completed"
    },
    {
      "content": "Check hard constraints (no 2.4x, hacking taxonomy 7, etc.)",
      "activeForm": "Checking hard constraints from paper_framing",
      "status": "completed"
    },
    {
      "content": "Check internal consistency between abstract/intro/experiments/conclusion",
      "activeForm": "Checking internal consistency",
      "status": "completed"
    },
    {
      "content": "Write consistency report to artifacts/",
      "activeForm": "Writing consistency report",
      "status": "completed"
    }
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "88c03bc5-c631-41cb-b71c-bf1a6dec069c",
  "isSidechain": false,
  "requestId": "req_011Cb3CV25YjmYM1r3bwHRFn",
  "type": "assistant",
  "uuid": "a0e558b5-cd39-409c-a43a-4a35bdf331a9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "24e67ff1-1ea3-4bcf-a9e3-703eaa6cb36e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01J9nWHfEvKFBS4VwZUzEMoN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7185,
      "cache_read_input_tokens": 120370,
      "output_tokens": 567,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7185,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 567,
          "cache_read_input_tokens": 120370,
          "cache_creation_input_tokens": 7185,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7185
          },
          "type": "message"
        }
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

_source line 90 · 2026-05-14T21:49:29.122Z_

<details><summary>↩ Tool result · `toolu_01CoDRLAgJFsqimuJFXYwLoD`</summary>

```text
Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a0e558b5-cd39-409c-a43a-4a35bdf331a9",
  "isSidechain": false,
  "promptId": "c33bf5b5-c338-4f2f-97b8-e3e6d5f92819",
  "type": "user",
  "uuid": "ea8ad386-6a9f-4e68-a96a-091ed971a542",
  "toolUseResult": {
    "oldTodos": [
      {
        "content": "Read all paper sections (conclusion, related_work, appendix)",
        "status": "completed",
        "activeForm": "Reading remaining paper sections"
      },
      {
        "content": "Cross-check ISR collapse trajectory numbers (0.642/0.132/0.003)",
        "status": "completed",
        "activeForm": "Cross-checking ISR collapse numbers"
      },
      {
        "content": "Cross-check 3-seed β=0.1 ISR/Random numbers in Table 1 and appendix",
        "status": "completed",
        "activeForm": "Cross-checking β=0.1 3-seed numbers"
      },
      {
        "content": "Cross-check SFT baseline numbers (PR=14%, ISR=0.571, 92.9%)",
        "status": "completed",
        "activeForm": "Cross-checking SFT baseline numbers"
      },
      {
        "content": "Cross-check Prolog numbers in experiments/appendix",
        "status": "completed",
        "activeForm": "Cross-checking Prolog numbers"
      },
      {
        "content": "Check hard constraints (no 2.4x, hacking taxonomy 7, etc.)",
        "status": "completed",
        "activeForm": "Checking hard constraints from paper_framing"
      },
      {
        "content": "Check internal consistency between abstract/intro/experiments/conclusion",
        "status": "completed",
        "activeForm": "Checking internal consistency"
      },
      {
        "content": "Write consistency report to artifacts/",
        "status": "in_progress",
        "activeForm": "Writing consistency report"
      }
    ],
    "newTodos": [
      {
        "content": "Read all paper sections (conclusion, related_work, appendix)",
        "status": "completed",
        "activeForm": "Reading remaining paper sections"
      },
      {
        "content": "Cross-check ISR collapse trajectory numbers (0.642/0.132/0.003)",
        "status": "completed",
        "activeForm": "Cross-checking ISR collapse numbers"
      },
      {
        "content": "Cross-check 3-seed β=0.1 ISR/Random numbers in Table 1 and appendix",
        "status": "completed",
        "activeForm": "Cross-checking β=0.1 3-seed numbers"
      },
      {
        "content": "Cross-check SFT baseline numbers (PR=14%, ISR=0.571, 92.9%)",
        "status": "completed",
        "activeForm": "Cross-checking SFT baseline numbers"
      },
      {
        "content": "Cross-check Prolog numbers in experiments/appendix",
        "status": "completed",
        "activeForm": "Cross-checking Prolog numbers"
      },
      {
        "content": "Check hard constraints (no 2.4x, hacking taxonomy 7, etc.)",
        "status": "completed",
        "activeForm": "Checking hard constraints from paper_framing"
      },
      {
        "content": "Check internal consistency between abstract/intro/experiments/conclusion",
        "status": "completed",
        "activeForm": "Checking internal consistency"
      },
      {
        "content": "Write consistency report to artifacts/",
        "status": "completed",
        "activeForm": "Writing consistency report"
      }
    ],
    "verificationNudgeNeeded": false
  },
  "sourceToolAssistantUUID": "a0e558b5-cd39-409c-a43a-4a35bdf331a9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "24e67ff1-1ea3-4bcf-a9e3-703eaa6cb36e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 91 · 2026-05-14T21:49:38.588Z_

报告已写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/data_consistency_report.md`。

**核心结论：PASS（无 critical 错误）**

- 所有数字（ISR 崩塌轨迹 0.642→0.132→0.003、3-seed β=0.1 ISR/Random、SFT 92.9%、Prolog 3-seed、1000-step 18.55 components 等）均与 registry 一致
- 所有硬约束遵守：0 处 "2.4x"、0 处 "six modes"、s44 query-as-fact gaming 正确标 0% genuine、plan013 vs plan017 未简化为 additive/convex 对照、ISR β=0.1 未误标 "no hacking"
- "near-zero hacking" 仅用于 SFT（92.9% genuine），不用于 ISR β=0.1
- proved-only ISR* 约定全文一致（registry 中部分 mean_isr 数学换算后吻合）

**3 处 minor 建议修改：**
1. Appendix line 414 把 `−99.6%` 改为 `−99.5%`（与 abstract 对齐）
2. Table 1 caption 或 §3.2 footnote 说明 H7/H1 是 simple mean across seeds（H1=17% 用 simple mean，H7=65% 用 pooled，口径差异 ~0.8pp）
3. 可选：Prolog STA s44 的 Gen=0 在表内更显眼标注，避免读者忽略 footnote $^b$ 中的 strict classifier 100% genuine 误报

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ea8ad386-6a9f-4e68-a96a-091ed971a542",
  "isSidechain": false,
  "requestId": "req_011Cb3CVcuJZ5acm5DgWzyRC",
  "type": "assistant",
  "uuid": "641cac01-d9e3-4150-8acd-69340ffcf3c0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "24e67ff1-1ea3-4bcf-a9e3-703eaa6cb36e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_017Yu3pJ2DVvzmCnhQiqp8Tf",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 625,
      "cache_read_input_tokens": 127555,
      "output_tokens": 565,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 625,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 565,
          "cache_read_input_tokens": 127555,
          "cache_creation_input_tokens": 625,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 625
          },
          "type": "message"
        }
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
  "leafUuid": "641cac01-d9e3-4150-8acd-69340ffcf3c0",
  "sessionId": "24e67ff1-1ea3-4bcf-a9e3-703eaa6cb36e"
}
```

---

### Runtime record

_source line 93_

```json
{
  "type": "ai-title",
  "aiTitle": "Audit paper figures against experiment registry",
  "sessionId": "24e67ff1-1ea3-4bcf-a9e3-703eaa6cb36e"
}
```

---
