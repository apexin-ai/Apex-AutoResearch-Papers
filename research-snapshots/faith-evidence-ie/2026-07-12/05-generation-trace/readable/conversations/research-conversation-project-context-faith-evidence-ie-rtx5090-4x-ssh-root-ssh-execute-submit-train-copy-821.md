# Research conversation: <project_context> # 项目: faith-evidence-ie ## 运行环境 - 服务器名: rtx5090-4x - SSH 账户: root（调用 ssh_execute / submit_training_job

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 36
- **Recorded user turns:** 1
- **Tool calls:** 8
- **Original source:** `logs/chats/exported-trajectories/account-2/6a109daa-4474-48f0-ab6d-eef9007c0510.jsonl`
- **Structured JSON:** [`3cca448b9a3c23cdb6be.json`](../../sessions/3c/3cca448b9a3c23cdb6be.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-23T19:16:13.707Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-23T19:16:13.707Z",
  "sessionId": "6a109daa-4474-48f0-ab6d-eef9007c0510",
  "content": "&lt;project_context>\n# 项目: faith-evidence-ie\n\n## 运行环境\n- 服务器名: rtx5090-4x\n- SSH 账户: root（调用 ssh_execute / submit_training_job 时传入 account=\"root\"）\n- SSH 连接命令: ssh rtx5090-4x  # 必须用此命令，~/.ssh/config 自动应用密钥和跳板机，禁止用裸 IP\n- 项目代码根目录: /root/autodl-tmp/freige\n\n## ⚠️ 活跃约束（必须遵守）\n\n- **C001**: 提交 eval 前必须 nvidia-smi 确认目标 GPU 显存占用 < 2GB，否则不提交、换卡或等待（原因：本 session 已 5 次因 eval 提交到被占用 GPU 导致 OOM，修复 eval 也因此作废。eval 推理需要接近全部显存，与训练共享必然 OOM。） [来自 D064]\n- **C002**: 提交训练/评估任务时必须在命令前设置 CUDA_VISIBLE_DEVICES=X，禁止依赖 device_map=\"auto\" 自动分配 GPU（原因：plan_011 和 rsft_ced_s45_train_r3 两次因未设 CUDA_VISIBLE_DEVICES 导致 device_map=\"auto\" 跨 GPU 分布，造成 OOM 和资源冲突。已知 bug 重复发生。）\n- **C003**: 提交训练任务时必须在命令前设置 CUDA_VISIBLE_DEVICES=X，禁止依赖 device_map=\"auto\" 自动分配 GPU（原因：plan_011 和 rsft_ced_s45_train_r3 均因未设 CUDA_VISIBLE_DEVICES 导致模型跨 GPU 分布，造成 OOM 或显存冲突。已重复发生两次。）\n- **C004**: Registry 标记 killed 时必须同时 kill -9 PID 并 ps 验证进程已终止，否则 killed 状态不可信（原因：rsft_ced_s45_train_r2 (PID 276148) registry 标记 killed 但进程未实际终止，占用 cuda:2 31.6GB 导致 r3 OOM。plan_011 也有类似模式。Reviewer WARNING。）\n- **C005**: no-evidence 模型 eval 必须传 --no_evidence 参数，确保推理时使用 NO_EVIDENCE_SYSTEM_PROMPT 与训练一致（原因：plan_006 1.7B/8B no-evidence eval 漏传该参数，导致训练/推理提示词不匹配（模型被要求输出未训练过的 evidence 字段），结果全部无效。Reviewer critical #20。）\n\n\n## 环境搭建\n连接服务器后先调 `detect_image` 检测是否为预置镜像。如果匹配，跳过基础环境搭建，只装项目特有依赖。已预装的包不要重复安装。\n\n## 输出风格\n回复简洁直接。只输出执行结果和必要信息，不要解释过程、不要客套、不要给未被要求的建议。\n&lt;/project_context>\n**[P0] ARR 提交前最终数据审计 — Worker 1: Abstract + 正文数字交叉验证**\n\n论文 LaTeX 文件位于：`/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/`\n\n子文件包括：abstract.tex, introduction.tex, method.tex, experiments.tex, conclusion.tex, appendix.tex\n\n**任务**：\n\n1. **读取 abstract.tex**，提取所有数字/统计量（如 -5.63pp, +0.25±0.47pp, 2.58, 51.19, 0.09pp, 50.19, 3.23pp, 4.7×, ρ=1.0 等）\n\n2. 对每个数字，找到 experiments.tex 或 appendix.tex 中的对应来源表/段落，验证一致性\n\n3. **读取 introduction.tex**，提取所有数字（如 -5.63pp, +0.25±0.47pp, ρ=-0.79 等），与正文/表格交叉验证\n\n4. **读取 method.tex**，检查 EDCR 值（应为 0.6797 和 0.6487）是否与 Table 1 (tab:main) 中的值一致\n\n5. **读取 conclusion.tex**，检查重复引用的数字（1.7B, 8B, 4.7× 等）是否与正文一致\n\n6. **四舍五入一致性检查**：全篇扫描同一指标是否使用统一精度。例如 Ign-F1 是否一律两位小数，evidence tax 是否一律 pp 单位。\n\n**产出**：将审计结果写入 `/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/final_audit_w1_abstract.md`\n\n格式：\n```\n## ✅ 已核对一致\n[每个数字 + 来源文件:行号]\n\n## ⚠️ 发现不一致\n[具体问题 + 正确值 + 错误值]\n\n## ❌ 待确认疑点\n[无法确定的项]\n```"
}
````

---

### Runtime record

_source line 2 · 2026-05-23T19:16:13.710Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-23T19:16:13.710Z",
  "sessionId": "6a109daa-4474-48f0-ab6d-eef9007c0510"
}
```

---

## Round 1

34 recorded events

### User

_source line 3 · 2026-05-23T19:16:13.744Z_

&lt;project_context>
# 项目: faith-evidence-ie

## 运行环境
- 服务器名: rtx5090-4x
- SSH 账户: root（调用 ssh_execute / submit_training_job 时传入 account="root"）
- SSH 连接命令: ssh rtx5090-4x  # 必须用此命令，~/.ssh/config 自动应用密钥和跳板机，禁止用裸 IP
- 项目代码根目录: /root/autodl-tmp/freige

## ⚠️ 活跃约束（必须遵守）

- **C001**: 提交 eval 前必须 nvidia-smi 确认目标 GPU 显存占用 < 2GB，否则不提交、换卡或等待（原因：本 session 已 5 次因 eval 提交到被占用 GPU 导致 OOM，修复 eval 也因此作废。eval 推理需要接近全部显存，与训练共享必然 OOM。） [来自 D064]
- **C002**: 提交训练/评估任务时必须在命令前设置 CUDA_VISIBLE_DEVICES=X，禁止依赖 device_map="auto" 自动分配 GPU（原因：plan_011 和 rsft_ced_s45_train_r3 两次因未设 CUDA_VISIBLE_DEVICES 导致 device_map="auto" 跨 GPU 分布，造成 OOM 和资源冲突。已知 bug 重复发生。）
- **C003**: 提交训练任务时必须在命令前设置 CUDA_VISIBLE_DEVICES=X，禁止依赖 device_map="auto" 自动分配 GPU（原因：plan_011 和 rsft_ced_s45_train_r3 均因未设 CUDA_VISIBLE_DEVICES 导致模型跨 GPU 分布，造成 OOM 或显存冲突。已重复发生两次。）
- **C004**: Registry 标记 killed 时必须同时 kill -9 PID 并 ps 验证进程已终止，否则 killed 状态不可信（原因：rsft_ced_s45_train_r2 (PID 276148) registry 标记 killed 但进程未实际终止，占用 cuda:2 31.6GB 导致 r3 OOM。plan_011 也有类似模式。Reviewer WARNING。）
- **C005**: no-evidence 模型 eval 必须传 --no_evidence 参数，确保推理时使用 NO_EVIDENCE_SYSTEM_PROMPT 与训练一致（原因：plan_006 1.7B/8B no-evidence eval 漏传该参数，导致训练/推理提示词不匹配（模型被要求输出未训练过的 evidence 字段），结果全部无效。Reviewer critical #20。）


## 环境搭建
连接服务器后先调 `detect_image` 检测是否为预置镜像。如果匹配，跳过基础环境搭建，只装项目特有依赖。已预装的包不要重复安装。

## 输出风格
回复简洁直接。只输出执行结果和必要信息，不要解释过程、不要客套、不要给未被要求的建议。
&lt;/project_context>
**[P0] ARR 提交前最终数据审计 — Worker 1: Abstract + 正文数字交叉验证**

论文 LaTeX 文件位于：`/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/`

子文件包括：abstract.tex, introduction.tex, method.tex, experiments.tex, conclusion.tex, appendix.tex

**任务**：

1. **读取 abstract.tex**，提取所有数字/统计量（如 -5.63pp, +0.25±0.47pp, 2.58, 51.19, 0.09pp, 50.19, 3.23pp, 4.7×, ρ=1.0 等）

2. 对每个数字，找到 experiments.tex 或 appendix.tex 中的对应来源表/段落，验证一致性

3. **读取 introduction.tex**，提取所有数字（如 -5.63pp, +0.25±0.47pp, ρ=-0.79 等），与正文/表格交叉验证

4. **读取 method.tex**，检查 EDCR 值（应为 0.6797 和 0.6487）是否与 Table 1 (tab:main) 中的值一致

5. **读取 conclusion.tex**，检查重复引用的数字（1.7B, 8B, 4.7× 等）是否与正文一致

6. **四舍五入一致性检查**：全篇扫描同一指标是否使用统一精度。例如 Ign-F1 是否一律两位小数，evidence tax 是否一律 pp 单位。

**产出**：将审计结果写入 `/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/final_audit_w1_abstract.md`

格式：
```
## ✅ 已核对一致
[每个数字 + 来源文件:行号]

## ⚠️ 发现不一致
[具体问题 + 正确值 + 错误值]

## ❌ 待确认疑点
[无法确定的项]
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "659f4775-47ec-4bb9-8db5-86432609ca56",
  "type": "user",
  "uuid": "8c2999ed-af07-448b-84e8-2fbc9e887f6d",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "6a109daa-4474-48f0-ab6d-eef9007c0510",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-23T19:16:13.743Z_

```json
{
  "parentUuid": "8c2999ed-af07-448b-84e8-2fbc9e887f6d",
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
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__register_artifact",
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
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__register_artifact",
      "mcp__agent-ml-research__update_registry"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "bbea0948-2eb4-4496-8a37-be506cb4a3ee",
  "timestamp": "2026-05-23T19:16:13.743Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "6a109daa-4474-48f0-ab6d-eef9007c0510",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-23T19:16:13.744Z_

```json
{
  "parentUuid": "bbea0948-2eb4-4496-8a37-be506cb4a3ee",
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
  "uuid": "c1bf2978-f2a9-4a73-aac6-035c0eae6bad",
  "timestamp": "2026-05-23T19:16:13.744Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "6a109daa-4474-48f0-ab6d-eef9007c0510",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6 · 2026-05-23T19:16:13.744Z_

```json
{
  "parentUuid": "c1bf2978-f2a9-4a73-aac6-035c0eae6bad",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "a8b9ffbd-66fb-444c-ba60-f2acbdb0c3ba",
  "timestamp": "2026-05-23T19:16:13.744Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "6a109daa-4474-48f0-ab6d-eef9007c0510",
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
  "aiTitle": "Audit paper numbers across LaTeX sections",
  "sessionId": "6a109daa-4474-48f0-ab6d-eef9007c0510"
}
```

---

### Assistant

_source line 8 · 2026-05-23T19:16:22.367Z_

I'll start by reading all the relevant LaTeX files in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a8b9ffbd-66fb-444c-ba60-f2acbdb0c3ba",
  "isSidechain": false,
  "requestId": "req_011CbL36289gvUXAKzRzAYg9",
  "type": "assistant",
  "uuid": "06b5ca36-95a0-4b83-9739-2018b7c7567e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "6a109daa-4474-48f0-ab6d-eef9007c0510",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019khDA8yXxCp24kUd1s4EQH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12651,
      "cache_read_input_tokens": 11841,
      "output_tokens": 466,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12651,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 466,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12651,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12651
          },
          "type": "message"
        }
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

_source line 9 · 2026-05-23T19:16:22.855Z_

<details open><summary>🔧 Tool call — Read · `toolu_01SJtGjyF7v1rWJZZ491G6eF`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "06b5ca36-95a0-4b83-9739-2018b7c7567e",
  "isSidechain": false,
  "requestId": "req_011CbL36289gvUXAKzRzAYg9",
  "type": "assistant",
  "uuid": "c67b30a8-058d-47f6-ad2d-d712864425d9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "6a109daa-4474-48f0-ab6d-eef9007c0510",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019khDA8yXxCp24kUd1s4EQH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12651,
      "cache_read_input_tokens": 11841,
      "output_tokens": 466,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12651,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 466,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12651,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12651
          },
          "type": "message"
        }
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

_source line 10 · 2026-05-23T19:16:22.875Z_

<details><summary>↩ Tool result · `toolu_01SJtGjyF7v1rWJZZ491G6eF`</summary>

```text
1	\begin{abstract}
2	
3	LLM-based Document-level Relation Extraction (DocRE) now matches or exceeds encoder baselines in extraction accuracy, yet these methods output bare relation triplets without identifying supporting sentences. Encoder-based evidence methods (SAIS, DREEAM) provide supporting sentences but trail LLM approaches in accuracy, creating a gap between extraction performance and output verifiability.
4	
5	We formalize evidence-grounded DocRE as structured generation and compare GRPO, DPO, and RSFT across three fully evaluated scales (1.7B, 4B, 8B) with 14B validation, two model families, and two datasets. The evidence tax---extraction cost of generating evidence---is scale-dependent: beneficial at 1.7B ($-$5.63pp dev Ign-F1) but approximately neutral at $\geq$4B (+0.25$\pm$0.47pp at 4B; positive $=$ cost). Gradient-based optimization amplifies evidence-extraction competition (GRPO catastrophic, DPO gradual), while RSFT with NLI-based scoring avoids decoupling entirely through output filtering rather than gradient pressure.
6	
7	RSFT consistently reduces training seed variance (complete pairwise seed separation on LLaMA, Cohen's $d{=}2.58$; non-overlapping $\chi^2$ CIs at 1.7B). Our 1.7B RSFT model (51.19 Ign-F1, std 0.09pp) approaches 8B SFT performance (50.19, std 3.23pp) at 4.7$\times$ fewer parameters. Test-set evaluation preserves model ranking across all evaluated scales (Spearman $\rho{=}1.0$).
8	
9	\end{abstract}
10	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c67b30a8-058d-47f6-ad2d-d712864425d9",
  "isSidechain": false,
  "promptId": "659f4775-47ec-4bb9-8db5-86432609ca56",
  "type": "user",
  "uuid": "26d14ced-269b-47fa-a0e0-a0e227c589dc",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/abstract.tex",
      "content": "\\begin{abstract}\n\nLLM-based Document-level Relation Extraction (DocRE) now matches or exceeds encoder baselines in extraction accuracy, yet these methods output bare relation triplets without identifying supporting sentences. Encoder-based evidence methods (SAIS, DREEAM) provide supporting sentences but trail LLM approaches in accuracy, creating a gap between extraction performance and output verifiability.\n\nWe formalize evidence-grounded DocRE as structured generation and compare GRPO, DPO, and RSFT across three fully evaluated scales (1.7B, 4B, 8B) with 14B validation, two model families, and two datasets. The evidence tax---extraction cost of generating evidence---is scale-dependent: beneficial at 1.7B ($-$5.63pp dev Ign-F1) but approximately neutral at $\\geq$4B (+0.25$\\pm$0.47pp at 4B; positive $=$ cost). Gradient-based optimization amplifies evidence-extraction competition (GRPO catastrophic, DPO gradual), while RSFT with NLI-based scoring avoids decoupling entirely through output filtering rather than gradient pressure.\n\nRSFT consistently reduces training seed variance (complete pairwise seed separation on LLaMA, Cohen's $d{=}2.58$; non-overlapping $\\chi^2$ CIs at 1.7B). Our 1.7B RSFT model (51.19 Ign-F1, std 0.09pp) approaches 8B SFT performance (50.19, std 3.23pp) at 4.7$\\times$ fewer parameters. Test-set evaluation preserves model ranking across all evaluated scales (Spearman $\\rho{=}1.0$).\n\n\\end{abstract}\n",
      "numLines": 10,
      "startLine": 1,
      "totalLines": 10
    }
  },
  "sourceToolAssistantUUID": "c67b30a8-058d-47f6-ad2d-d712864425d9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "6a109daa-4474-48f0-ab6d-eef9007c0510",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-23T19:16:23.327Z_

<details open><summary>🔧 Tool call — Read · `toolu_0195dGVWgaRLkomtsymPkWkq`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "26d14ced-269b-47fa-a0e0-a0e227c589dc",
  "isSidechain": false,
  "requestId": "req_011CbL36289gvUXAKzRzAYg9",
  "type": "assistant",
  "uuid": "254cd821-df74-4e9c-90cb-2bfcb9b55c34",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "6a109daa-4474-48f0-ab6d-eef9007c0510",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019khDA8yXxCp24kUd1s4EQH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12651,
      "cache_read_input_tokens": 11841,
      "output_tokens": 466,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12651,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 466,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12651,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12651
          },
          "type": "message"
        }
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

_source line 12 · 2026-05-23T19:16:23.332Z_

<details><summary>↩ Tool result · `toolu_0195dGVWgaRLkomtsymPkWkq`</summary>

```text
1	\section{Introduction}
2	
3	Document-level relation extraction (DocRE) requires identifying semantic relations between entity pairs across multiple sentences, a task where encoder-based methods such as \citet{zhou2021atlop} long dominated.
4	Recent LLM-based approaches have closed this gap: \citet{autore2024} fine-tune LLMs with structured decomposition, \citet{xu2024lmrc} frame it as multi-choice reading comprehension, and \citet{chen2025docksrag} combine retrieval-augmented generation with structured knowledge.
5	These methods approach or surpass encoder baselines on DocRED \citep{yao2019docred} and Re-DocRED \citep{tan2022redocred} in extraction accuracy, yet every one outputs bare relation triplets $(e_h, r, e_t)$ without indicating \emph{which sentences} support each prediction.
6	In deployment contexts---clinical knowledge bases, legal due-diligence pipelines, financial compliance systems---users cannot verify a prediction without manually locating its textual basis across a multi-page document.
7	
8	Encoder-based methods have partially addressed this need: \citet{xiao2022sais} introduce sentence-level evidence supervision as an auxiliary signal, and \citet{ma2023dreeam} extend this with dynamic evidence retrieval through memory attention.
9	Both produce evidence and improve extraction, but encoder methods now trail LLM-based approaches in accuracy.
10	The community faces a gap: the most accurate extractors provide no evidence, while evidence-capable methods are no longer competitive.
11	
12	This gap reflects a structural difference.
13	In encoder methods, evidence retrieval is classification that regularizes the encoder at negligible cost; in LLM-based DocRE, evidence requires the model to \emph{generate} additional output tokens per triple, increasing output length and decoding complexity.
14	The na\"{i}ve expectation is that this generation cost always harms extraction accuracy.
15	Our experiments show this expectation is wrong.
16	The evidence tax is not a fixed penalty but a landscape shaped by model capacity, optimization paradigm, and training data quality.
17	Within the Qwen3 family, evidence generation \emph{benefits} extraction at 1.7B ($-$5.63pp Ign-F1, partly through halving output duplication) but is approximately neutral at $\geq$4B (+0.25$\pm$0.47pp at 4B).
18	Gradient-based optimization amplifies this competition---GRPO collapses extraction under constrained precision, DPO progressively trades extraction for evidence---while discrete sample selection (RSFT) avoids the trade-off entirely by filtering outputs rather than pushing gradients.
19	
20	We formalize evidence-grounded DocRE as a structured generation task and compare three post-training paradigms---GRPO \citep{shao2024deepseekmath}, DPO \citep{rafailov2023direct}, and RSFT (building on STaR; \citealt{zelikman2022star})---across three fully evaluated scales (1.7B, 4B, 8B) with 14B validation, two model families, and two datasets. Our contributions:
21	\begin{enumerate}
22	    \item \textbf{Evidence generation is not uniformly harmful.} We observe a scale-dependent evidence tax with a within-family capacity threshold: beneficial at 1.7B ($-$5.63pp) but approximately neutral at $\geq$4B (+0.25$\pm$0.47pp at 4B), challenging the assumption that evidence always costs extraction accuracy.
23	
24	    \item \textbf{Gradient pressure causes evidence-extraction decoupling.} We characterize a decoupling spectrum (GRPO catastrophic $\rightarrow$ DPO gradual $\rightarrow$ RSFT none) and introduce the Evidence-Decoupling Ratio (EDCR) as a diagnostic, validated at per-relation level ($\rho{=}{-}0.79$, $n{=}76$, $p{<}0.001$).
25	
26	    \item \textbf{RSFT consistently reduces training variance.} NLI-based sample selection improves mean Ign-F1 across tested scales (+1.2 to +6.6pp); our 1.7B RSFT model (51.19 Ign-F1, std 0.09pp) approaches 8B SFT performance (50.19, std 3.23pp) at 4.7$\times$ fewer parameters, enabling deployment-efficient evidence-grounded extraction.
27	\end{enumerate}
28	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "254cd821-df74-4e9c-90cb-2bfcb9b55c34",
  "isSidechain": false,
  "promptId": "659f4775-47ec-4bb9-8db5-86432609ca56",
  "type": "user",
  "uuid": "e342c07d-e0fb-4511-8118-b65beab46ac5",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/introduction.tex",
      "content": "\\section{Introduction}\n\nDocument-level relation extraction (DocRE) requires identifying semantic relations between entity pairs across multiple sentences, a task where encoder-based methods such as \\citet{zhou2021atlop} long dominated.\nRecent LLM-based approaches have closed this gap: \\citet{autore2024} fine-tune LLMs with structured decomposition, \\citet{xu2024lmrc} frame it as multi-choice reading comprehension, and \\citet{chen2025docksrag} combine retrieval-augmented generation with structured knowledge.\nThese methods approach or surpass encoder baselines on DocRED \\citep{yao2019docred} and Re-DocRED \\citep{tan2022redocred} in extraction accuracy, yet every one outputs bare relation triplets $(e_h, r, e_t)$ without indicating \\emph{which sentences} support each prediction.\nIn deployment contexts---clinical knowledge bases, legal due-diligence pipelines, financial compliance systems---users cannot verify a prediction without manually locating its textual basis across a multi-page document.\n\nEncoder-based methods have partially addressed this need: \\citet{xiao2022sais} introduce sentence-level evidence supervision as an auxiliary signal, and \\citet{ma2023dreeam} extend this with dynamic evidence retrieval through memory attention.\nBoth produce evidence and improve extraction, but encoder methods now trail LLM-based approaches in accuracy.\nThe community faces a gap: the most accurate extractors provide no evidence, while evidence-capable methods are no longer competitive.\n\nThis gap reflects a structural difference.\nIn encoder methods, evidence retrieval is classification that regularizes the encoder at negligible cost; in LLM-based DocRE, evidence requires the model to \\emph{generate} additional output tokens per triple, increasing output length and decoding complexity.\nThe na\\\"{i}ve expectation is that this generation cost always harms extraction accuracy.\nOur experiments show this expectation is wrong.\nThe evidence tax is not a fixed penalty but a landscape shaped by model capacity, optimization paradigm, and training data quality.\nWithin the Qwen3 family, evidence generation \\emph{benefits} extraction at 1.7B ($-$5.63pp Ign-F1, partly through halving output duplication) but is approximately neutral at $\\geq$4B (+0.25$\\pm$0.47pp at 4B).\nGradient-based optimization amplifies this competition---GRPO collapses extraction under constrained precision, DPO progressively trades extraction for evidence---while discrete sample selection (RSFT) avoids the trade-off entirely by filtering outputs rather than pushing gradients.\n\nWe formalize evidence-grounded DocRE as a structured generation task and compare three post-training paradigms---GRPO \\citep{shao2024deepseekmath}, DPO \\citep{rafailov2023direct}, and RSFT (building on STaR; \\citealt{zelikman2022star})---across three fully evaluated scales (1.7B, 4B, 8B) with 14B validation, two model families, and two datasets. Our contributions:\n\\begin{enumerate}\n    \\item \\textbf{Evidence generation is not uniformly harmful.} We observe a scale-dependent evidence tax with a within-family capacity threshold: beneficial at 1.7B ($-$5.63pp) but approximately neutral at $\\geq$4B (+0.25$\\pm$0.47pp at 4B), challenging the assumption that evidence always costs extraction accuracy.\n\n    \\item \\textbf{Gradient pressure causes evidence-extraction decoupling.} We characterize a decoupling spectrum (GRPO catastrophic $\\rightarrow$ DPO gradual $\\rightarrow$ RSFT none) and introduce the Evidence-Decoupling Ratio (EDCR) as a diagnostic, validated at per-relation level ($\\rho{=}{-}0.79$, $n{=}76$, $p{<}0.001$).\n\n    \\item \\textbf{RSFT consistently reduces training variance.} NLI-based sample selection improves mean Ign-F1 across tested scales (+1.2 to +6.6pp); our 1.7B RSFT model (51.19 Ign-F1, std 0.09pp) approaches 8B SFT performance (50.19, std 3.23pp) at 4.7$\\times$ fewer parameters, enabling deployment-efficient evidence-grounded extraction.\n\\end{enumerate}\n",
      "numLines": 28,
      "startLine": 1,
      "totalLines": 28
    }
  },
  "sourceToolAssistantUUID": "254cd821-df74-4e9c-90cb-2bfcb9b55c34",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "6a109daa-4474-48f0-ab6d-eef9007c0510",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-23T19:16:23.800Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Xz1k1kWtWdrK3nC2g7a2LB`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e342c07d-e0fb-4511-8118-b65beab46ac5",
  "isSidechain": false,
  "requestId": "req_011CbL36289gvUXAKzRzAYg9",
  "type": "assistant",
  "uuid": "0ad2ab38-dc48-40a1-ac6b-2ebf83a8dd18",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "6a109daa-4474-48f0-ab6d-eef9007c0510",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019khDA8yXxCp24kUd1s4EQH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12651,
      "cache_read_input_tokens": 11841,
      "output_tokens": 466,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12651,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 466,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12651,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12651
          },
          "type": "message"
        }
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

_source line 14 · 2026-05-23T19:16:23.806Z_

<details><summary>↩ Tool result · `toolu_01Xz1k1kWtWdrK3nC2g7a2LB`</summary>

```text
1	\section{Method}
2	\label{sec:method}
3	
4	\begin{figure*}[t]
5	\centering
6	\includegraphics[width=0.92\textwidth]{fig_overview.pdf}
7	\vspace{-2mm}
8	\caption{Overview of our approach. (Top) Standard DocRE outputs bare triples; evidence-grounded DocRE additionally generates supporting sentence indices for each prediction. (Bottom) RSFT pipeline: the SFT model samples $N$ candidate responses per document, scores them with CED/NLI, selects the top-$k$, and fine-tunes on the filtered set.}
9	\label{fig:overview}
10	\end{figure*}
11	
12	\subsection{Task: Evidence-Grounded Document-Level Relation Extraction}
13	\label{sec:task}
14	
15	Given a document $D = \{s_1, \ldots, s_n\}$ consisting of $n$ sentences and a set of entities $\mathcal{E}$ identified within $D$, the task of evidence-grounded document-level relation extraction (DocRE) requires predicting, for each entity pair $(e_h, e_t) \in \mathcal{E} \times \mathcal{E}$, a relation $r \in \mathcal{R} \cup \{\texttt{NA}\}$ together with a set of supporting evidence sentences $E \subseteq D$. Standard DocRE predicts only the triple $(e_h, r, e_t)$; the evidence-grounded formulation also requires $E$, which grounds each prediction in specific textual support (Figure~\ref{fig:overview}).
16	
17	In our LLM-based approach, the model generates structured outputs that jointly encode both components. For each predicted relation, the output follows the format \texttt{(head, relation, tail) | Evidence: [S$i$][S$j$]}, requiring the model to produce complete evidence references inline with each triple rather than as a separate retrieval step. This design contrasts with encoder-based evidence methods such as SAIS~\citep{xiao2022sais} and DREEAM~\citep{ma2023dreeam}, which frame evidence identification as sentence-level binary classification. Because classification over a fixed sentence set does not increase output length, these methods incur no generation overhead. Our LLM formulation requires additional tokens for each evidence reference, creating a generation burden that scales with the number of predicted triples and their evidence sentences. This scale-dependent cost is the central phenomenon we investigate.
18	
19	
20	\subsection{Supervised Fine-Tuning Baseline}
21	\label{sec:sft}
22	
23	We fine-tune all models with LoRA~\citep{hu2022lora} at rank $r{=}64$ and scaling factor $\alpha{=}128$, applied to all linear projections (attention and feed-forward). The training data consists of DocRED~\citep{yao2019docred} training documents converted to the structured output format described above, where each example maps a document and its entity set to the complete set of relation triples with evidence annotations. We also train a \emph{no-evidence} variant under identical configuration but with evidence references removed from the output format, producing only \texttt{(head, relation, tail)}. This variant serves as an upper bound on extraction performance by eliminating the generation cost of evidence, and allows direct measurement of the evidence tax at each model scale. Detailed hyperparameters (learning rate, batch size, number of epochs) are reported in the Appendix.
24	
25	
26	\subsection{Optimization Paradigms}
27	\label{sec:paradigms}
28	
29	We evaluate three post-SFT optimization paradigms that differ in how they incorporate quality signals from the CED scoring function (\S\ref{sec:ced}).
30	
31	\paragraph{GRPO.}
32	Group Relative Policy Optimization~\citep{shao2024deepseekmath} is an online RL method that eliminates the need for a separate value network by computing advantages within groups of sampled outputs. For each training document, the policy generates $G$ candidate responses, which are scored by CED. The advantage of each response is computed relative to the group mean, and the policy is updated to increase the probability of above-average outputs. We test two configurations: QLoRA with $G{=}4$ groups under 4-bit quantization, and bf16 full-precision LoRA with $G{=}8$. Because GRPO applies gradient updates that directly optimize the reward signal, evidence quality and extraction accuracy compete for gradient capacity. We analyze this multi-objective tension in Section~\ref{sec:spectrum}.
33	
34	\paragraph{DPO.}
35	Direct Preference Optimization~\citep{rafailov2023direct} reformulates RLHF as a classification problem over preference pairs, without explicit reward models. We construct preference data from the SFT model's sampled outputs: for each document, the response with the highest CED score is labeled as preferred and the lowest-scoring response as rejected. DPO then adjusts the policy to increase the log-probability ratio between preferred and rejected completions. We train for 1 and 3 epochs to observe the temporal dynamics of evidence-extraction trade-offs under implicit optimization.
36	
37	\paragraph{RSFT.}
38	Rejection Sampling Fine-Tuning is a single-round variant of iterative self-improvement methods such as STaR~\citep{zelikman2022star}. The procedure is straightforward: the SFT model generates $N{=}8$ candidate outputs per training document, each candidate is scored by CED, and only the top-$k{=}1$ response is retained as training data. We use $k{=}1$ (best-of-$N$) selection throughout all experiments, selecting the single highest-scoring candidate per document for RSFT training data construction. This yields approximately 3,000 training examples per model (one per document; exact counts vary slightly by model due to generation failures). Unlike GRPO and DPO, RSFT does not apply gradient-based optimization pressure toward a reward signal. Instead, it improves training data quality through filtering: the model trains on its own best outputs rather than all outputs. This distinction is critical because discrete selection over complete outputs cannot exploit the extraction-evidence trade-off that gradient methods find. The contribution of RSFT in our setting is not the framework itself, which is well-established, but its application to evidence-grounded DocRE with CED as a domain-specific quality filter.
39	
40	
41	\subsection{Contrastive Evidence Discrimination}
42	\label{sec:ced}
43	
44	CED is a scoring function that evaluates the faithfulness of predicted evidence sentences to their associated relation triples. It builds on Natural Language Inference (NLI) to measure whether evidence actually entails the predicted relation, rather than merely co-occurring with the relevant entities.
45	
46	For a predicted triple $(e_h, r, e_t)$ with evidence sentences $E$, CED constructs a positive NLI pair: the premise is the concatenation of sentences in $E$, and the hypothesis is a natural-language verbalization of the relation (e.g., ``$e_h$ has relation $r$ with $e_t$''). An NLI model (\texttt{cross-encoder/nli-deberta-v3-base}) produces an entailment probability $p^+$ for this pair. The contrastive component introduces hard negatives drawn from the same document. For each triple, we collect sentences that mention $e_h$ or $e_t$ but are not in the predicted evidence set. These entity-sharing distractors serve as negative premises, and the NLI model scores each to obtain $p^-_1, \ldots, p^-_m$. The CED score for a single triple is:
47	\begin{equation}
48	\text{CED}(e_h, r, e_t, E) = p^+ - \max_j \, p^-_j
49	\label{eq:ced}
50	\end{equation}
51	This formulation forces the scoring function to distinguish sentences that genuinely support the relation from sentences that merely mention the same entities. A high CED score indicates that the evidence provides relation-specific support beyond entity co-occurrence.
52	
53	The document-level CED score aggregates over all predicted triples, weighted by extraction correctness: triples that match ground-truth relations contribute their CED scores, while incorrect triples receive zero credit. This coupling ensures that CED rewards both faithful evidence and accurate extraction jointly.
54	
55	We also evaluate a \emph{flat-NLI} baseline that uses only the positive entailment score $p^+$ without the contrastive term. CED and flat-NLI produce comparable RSFT outcomes (mean Rel-F1 difference of 0.02pp across available seeds; Section~\ref{sec:analysis}), confirming that the contrastive formulation is not essential for data selection quality. We adopt CED as the default because its per-triple discrimination scores support interpretable error analysis.
56	
57	
58	\subsection{Evidence-Decoupling Ratio}
59	\label{sec:edcr}
60	
61	We introduce the Evidence-Decoupling Ratio (EDCR) as a diagnostic metric that quantifies the degree of misalignment between a model's extraction and evidence capabilities. EDCR is not a training component; it serves purely as an analytical tool for comparing optimization methods.
62	
63	EDCR is defined as:
64	\begin{equation}
65	\text{EDCR} = \frac{\text{Evi-Recall}_{\text{TP}}}{\text{Rel-Recall}}
66	\label{eq:edcr}
67	\end{equation}
68	where $\text{Evi-Recall}_{\text{TP}}$ is evidence sentence recall computed only over correctly predicted triples (true positives), and $\text{Rel-Recall}$ is overall relation extraction recall. The numerator captures evidence quality on the subset of triples the model gets right; the denominator captures how many triples the model identifies in total.
69	
70	The intuition is as follows. A model that correctly identifies a few triples and provides excellent evidence for them, but misses most triples entirely, will have high $\text{Evi-Recall}_{\text{TP}}$ and low $\text{Rel-Recall}$, yielding a high EDCR. This pattern signals that evidence quality has decoupled from extraction capability: the model produces faithful evidence only within a narrow comfort zone.
71	
72	EDCR operates at two diagnostic levels. At the method level, comparing EDCR across seven independent method configurations reveals a negative correlation with Rel-F1 (Spearman $\rho{=}{-}0.89$, $n{=}7$, $p{=}0.007$). Because EDCR shares Rel-Recall with Rel-F1 by construction, this correlation should be interpreted as a diagnostic pattern rather than an independent discovery; its primary value lies in per-relation analysis. We validate EDCR's diagnostic utility through per-relation analysis (\S\ref{sec:analysis}), which avoids the shared-component concern present in cross-method correlation. At the per-relation level, computing EDCR for individual relation types reveals a robust negative correlation with Rel-F1 ($\rho{=}{-}0.79$, $n{=}76$, $p{<}0.001$) that is independent of Evi-F1 ($\rho{=}{-}0.06$, $p{=}0.58$). This independence means EDCR captures relation-specific extraction-evidence misalignment that aggregate evidence metrics miss. The SFT baseline EDCR (0.6797, three-seed mean) reflects the inherent cost of evidence generation; EDCR values substantially exceeding this level (e.g., GRPO QLoRA at 0.9876) indicate RL-induced decoupling beyond what evidence production alone explains, while values below the baseline (e.g., RSFT at 0.6487) reflect improved co-optimization.
73	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0ad2ab38-dc48-40a1-ac6b-2ebf83a8dd18",
  "isSidechain": false,
  "promptId": "659f4775-47ec-4bb9-8db5-86432609ca56",
  "type": "user",
  "uuid": "0e9237a1-7b5e-4129-95fd-6a1eda885cde",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/method.tex",
      "content": "\\section{Method}\n\\label{sec:method}\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=0.92\\textwidth]{fig_overview.pdf}\n\\vspace{-2mm}\n\\caption{Overview of our approach. (Top) Standard DocRE outputs bare triples; evidence-grounded DocRE additionally generates supporting sentence indices for each prediction. (Bottom) RSFT pipeline: the SFT model samples $N$ candidate responses per document, scores them with CED/NLI, selects the top-$k$, and fine-tunes on the filtered set.}\n\\label{fig:overview}\n\\end{figure*}\n\n\\subsection{Task: Evidence-Grounded Document-Level Relation Extraction}\n\\label{sec:task}\n\nGiven a document $D = \\{s_1, \\ldots, s_n\\}$ consisting of $n$ sentences and a set of entities $\\mathcal{E}$ identified within $D$, the task of evidence-grounded document-level relation extraction (DocRE) requires predicting, for each entity pair $(e_h, e_t) \\in \\mathcal{E} \\times \\mathcal{E}$, a relation $r \\in \\mathcal{R} \\cup \\{\\texttt{NA}\\}$ together with a set of supporting evidence sentences $E \\subseteq D$. Standard DocRE predicts only the triple $(e_h, r, e_t)$; the evidence-grounded formulation also requires $E$, which grounds each prediction in specific textual support (Figure~\\ref{fig:overview}).\n\nIn our LLM-based approach, the model generates structured outputs that jointly encode both components. For each predicted relation, the output follows the format \\texttt{(head, relation, tail) | Evidence: [S$i$][S$j$]}, requiring the model to produce complete evidence references inline with each triple rather than as a separate retrieval step. This design contrasts with encoder-based evidence methods such as SAIS~\\citep{xiao2022sais} and DREEAM~\\citep{ma2023dreeam}, which frame evidence identification as sentence-level binary classification. Because classification over a fixed sentence set does not increase output length, these methods incur no generation overhead. Our LLM formulation requires additional tokens for each evidence reference, creating a generation burden that scales with the number of predicted triples and their evidence sentences. This scale-dependent cost is the central phenomenon we investigate.\n\n\n\\subsection{Supervised Fine-Tuning Baseline}\n\\label{sec:sft}\n\nWe fine-tune all models with LoRA~\\citep{hu2022lora} at rank $r{=}64$ and scaling factor $\\alpha{=}128$, applied to all linear projections (attention and feed-forward). The training data consists of DocRED~\\citep{yao2019docred} training documents converted to the structured output format described above, where each example maps a document and its entity set to the complete set of relation triples with evidence annotations. We also train a \\emph{no-evidence} variant under identical configuration but with evidence references removed from the output format, producing only \\texttt{(head, relation, tail)}. This variant serves as an upper bound on extraction performance by eliminating the generation cost of evidence, and allows direct measurement of the evidence tax at each model scale. Detailed hyperparameters (learning rate, batch size, number of epochs) are reported in the Appendix.\n\n\n\\subsection{Optimization Paradigms}\n\\label{sec:paradigms}\n\nWe evaluate three post-SFT optimization paradigms that differ in how they incorporate quality signals from the CED scoring function (\\S\\ref{sec:ced}).\n\n\\paragraph{GRPO.}\nGroup Relative Policy Optimization~\\citep{shao2024deepseekmath} is an online RL method that eliminates the need for a separate value network by computing advantages within groups of sampled outputs. For each training document, the policy generates $G$ candidate responses, which are scored by CED. The advantage of each response is computed relative to the group mean, and the policy is updated to increase the probability of above-average outputs. We test two configurations: QLoRA with $G{=}4$ groups under 4-bit quantization, and bf16 full-precision LoRA with $G{=}8$. Because GRPO applies gradient updates that directly optimize the reward signal, evidence quality and extraction accuracy compete for gradient capacity. We analyze this multi-objective tension in Section~\\ref{sec:spectrum}.\n\n\\paragraph{DPO.}\nDirect Preference Optimization~\\citep{rafailov2023direct} reformulates RLHF as a classification problem over preference pairs, without explicit reward models. We construct preference data from the SFT model's sampled outputs: for each document, the response with the highest CED score is labeled as preferred and the lowest-scoring response as rejected. DPO then adjusts the policy to increase the log-probability ratio between preferred and rejected completions. We train for 1 and 3 epochs to observe the temporal dynamics of evidence-extraction trade-offs under implicit optimization.\n\n\\paragraph{RSFT.}\nRejection Sampling Fine-Tuning is a single-round variant of iterative self-improvement methods such as STaR~\\citep{zelikman2022star}. The procedure is straightforward: the SFT model generates $N{=}8$ candidate outputs per training document, each candidate is scored by CED, and only the top-$k{=}1$ response is retained as training data. We use $k{=}1$ (best-of-$N$) selection throughout all experiments, selecting the single highest-scoring candidate per document for RSFT training data construction. This yields approximately 3,000 training examples per model (one per document; exact counts vary slightly by model due to generation failures). Unlike GRPO and DPO, RSFT does not apply gradient-based optimization pressure toward a reward signal. Instead, it improves training data quality through filtering: the model trains on its own best outputs rather than all outputs. This distinction is critical because discrete selection over complete outputs cannot exploit the extraction-evidence trade-off that gradient methods find. The contribution of RSFT in our setting is not the framework itself, which is well-established, but its application to evidence-grounded DocRE with CED as a domain-specific quality filter.\n\n\n\\subsection{Contrastive Evidence Discrimination}\n\\label{sec:ced}\n\nCED is a scoring function that evaluates the faithfulness of predicted evidence sentences to their associated relation triples. It builds on Natural Language Inference (NLI) to measure whether evidence actually entails the predicted relation, rather than merely co-occurring with the relevant entities.\n\nFor a predicted triple $(e_h, r, e_t)$ with evidence sentences $E$, CED constructs a positive NLI pair: the premise is the concatenation of sentences in $E$, and the hypothesis is a natural-language verbalization of the relation (e.g., ``$e_h$ has relation $r$ with $e_t$''). An NLI model (\\texttt{cross-encoder/nli-deberta-v3-base}) produces an entailment probability $p^+$ for this pair. The contrastive component introduces hard negatives drawn from the same document. For each triple, we collect sentences that mention $e_h$ or $e_t$ but are not in the predicted evidence set. These entity-sharing distractors serve as negative premises, and the NLI model scores each to obtain $p^-_1, \\ldots, p^-_m$. The CED score for a single triple is:\n\\begin{equation}\n\\text{CED}(e_h, r, e_t, E) = p^+ - \\max_j \\, p^-_j\n\\label{eq:ced}\n\\end{equation}\nThis formulation forces the scoring function to distinguish sentences that genuinely support the relation from sentences that merely mention the same entities. A high CED score indicates that the evidence provides relation-specific support beyond entity co-occurrence.\n\nThe document-level CED score aggregates over all predicted triples, weighted by extraction correctness: triples that match ground-truth relations contribute their CED scores, while incorrect triples receive zero credit. This coupling ensures that CED rewards both faithful evidence and accurate extraction jointly.\n\nWe also evaluate a \\emph{flat-NLI} baseline that uses only the positive entailment score $p^+$ without the contrastive term. CED and flat-NLI produce comparable RSFT outcomes (mean Rel-F1 difference of 0.02pp across available seeds; Section~\\ref{sec:analysis}), confirming that the contrastive formulation is not essential for data selection quality. We adopt CED as the default because its per-triple discrimination scores support interpretable error analysis.\n\n\n\\subsection{Evidence-Decoupling Ratio}\n\\label{sec:edcr}\n\nWe introduce the Evidence-Decoupling Ratio (EDCR) as a diagnostic metric that quantifies the degree of misalignment between a model's extraction and evidence capabilities. EDCR is not a training component; it serves purely as an analytical tool for comparing optimization methods.\n\nEDCR is defined as:\n\\begin{equation}\n\\text{EDCR} = \\frac{\\text{Evi-Recall}_{\\text{TP}}}{\\text{Rel-Recall}}\n\\label{eq:edcr}\n\\end{equation}\nwhere $\\text{Evi-Recall}_{\\text{TP}}$ is evidence sentence recall computed only over correctly predicted triples (true positives), and $\\text{Rel-Recall}$ is overall relation extraction recall. The numerator captures evidence quality on the subset of triples the model gets right; the denominator captures how many triples the model identifies in total.\n\nThe intuition is as follows. A model that correctly identifies a few triples and provides excellent evidence for them, but misses most triples entirely, will have high $\\text{Evi-Recall}_{\\text{TP}}$ and low $\\text{Rel-Recall}$, yielding a high EDCR. This pattern signals that evidence quality has decoupled from extraction capability: the model produces faithful evidence only within a narrow comfort zone.\n\nEDCR operates at two diagnostic levels. At the method level, comparing EDCR across seven independent method configurations reveals a negative correlation with Rel-F1 (Spearman $\\rho{=}{-}0.89$, $n{=}7$, $p{=}0.007$). Because EDCR shares Rel-Recall with Rel-F1 by construction, this correlation should be interpreted as a diagnostic pattern rather than an independent discovery; its primary value lies in per-relation analysis. We validate EDCR's diagnostic utility through per-relation analysis (\\S\\ref{sec:analysis}), which avoids the shared-component concern present in cross-method correlation. At the per-relation level, computing EDCR for individual relation types reveals a robust negative correlation with Rel-F1 ($\\rho{=}{-}0.79$, $n{=}76$, $p{<}0.001$) that is independent of Evi-F1 ($\\rho{=}{-}0.06$, $p{=}0.58$). This independence means EDCR captures relation-specific extraction-evidence misalignment that aggregate evidence metrics miss. The SFT baseline EDCR (0.6797, three-seed mean) reflects the inherent cost of evidence generation; EDCR values substantially exceeding this level (e.g., GRPO QLoRA at 0.9876) indicate RL-induced decoupling beyond what evidence production alone explains, while values below the baseline (e.g., RSFT at 0.6487) reflect improved co-optimization.\n",
      "numLines": 73,
      "startLine": 1,
      "totalLines": 73
    }
  },
  "sourceToolAssistantUUID": "0ad2ab38-dc48-40a1-ac6b-2ebf83a8dd18",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "6a109daa-4474-48f0-ab6d-eef9007c0510",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-23T19:16:24.275Z_

<details open><summary>🔧 Tool call — Read · `toolu_01DRWATQzySa7GkJEtXKx1ZF`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0e9237a1-7b5e-4129-95fd-6a1eda885cde",
  "isSidechain": false,
  "requestId": "req_011CbL36289gvUXAKzRzAYg9",
  "type": "assistant",
  "uuid": "0ef7124a-c728-45c0-89b8-7058c133dff4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "6a109daa-4474-48f0-ab6d-eef9007c0510",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019khDA8yXxCp24kUd1s4EQH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12651,
      "cache_read_input_tokens": 11841,
      "output_tokens": 466,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12651,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 466,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12651,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12651
          },
          "type": "message"
        }
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

_source line 16 · 2026-05-23T19:16:24.284Z_

<details><summary>↩ Tool result · `toolu_01DRWATQzySa7GkJEtXKx1ZF`</summary>

```text
1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:setup}
6	
7	We evaluate on DocRED~\citep{yao2019docred} (3,053 training / 998 dev documents, 96 relation types) with Re-DocRED~\citep{tan2022redocred} for cross-dataset validation. Our primary model is Qwen3-4B; we also train Qwen3-1.7B, 8B, and 14B to study scale effects, with LLaMA-3.1-8B for cross-family validation. All models use LoRA~\citep{hu2022lora} ($r{=}64$, $\alpha{=}128$) with structured output jointly producing triples and evidence. RSFT selects the top-$k{=}1$ of $N{=}8$ samples by CED score (\S\ref{sec:ced}); GRPO uses group sizes $G{=}4$ (QLoRA) and $G{=}8$ (bf16); DPO constructs preference pairs from CED-ranked outputs. We report Ign-F1 (primary; ignores training-set triples), Rel-F1, Evi-F1 (TP-only and joint per DREEAM protocol~\citep{ma2023dreeam}), and EDCR (\S\ref{sec:edcr}). Detailed hyperparameters appear in the Appendix.
8	
9	
10	\subsection{Main Results}
11	\label{sec:main_results}
12	
13	Table~\ref{tab:main} presents the primary comparison on Qwen3-4B. The SFT baseline exhibits high seed sensitivity (mean Ign-F1 43.58, std 3.80pp, range 39.74--47.34). Removing evidence entirely (no-evidence SFT, s42) reaches 47.21 Ign-F1.
14	
15	RSFT CED achieves 44.82 Ign-F1 (+1.24 over SFT mean) with substantially lower variance (std 0.51pp), though these reflect different sources of variation (Section~\ref{sec:scaling}). Even the weakest RSFT seed (44.23) exceeds the SFT mean. Evidence quality improves (Evi-F1 80.96 vs.\ 79.61) and coupling tightens (EDCR 0.6487 vs.\ 0.6797). Per-seed results appear in Appendix~\ref{sec:ablation_full}.
16	
17	\begin{table}[t]
18	\centering
19	\caption{Main results on DocRED dev (Qwen3-4B). Ign-F1 shows mean $\pm$ std$^{(\text{seeds})}$; other metrics are same-seed means. Best \textbf{bold}; best evidence-generating \underline{underlined}. Per-seed: Appendix~\ref{tab:ablation_full}.}
20	\label{tab:main}
21	\small
22	\resizebox{\columnwidth}{!}{%
23	\begin{tabular}{lcccc}
24	\toprule
25	\textbf{Method} & \textbf{Ign-F1} & \textbf{Rel-F1} & \textbf{Evi-F1} & \textbf{EDCR} \\
26	\midrule
27	SFT baseline & 43.58{\scriptsize$\pm$3.80}$^{(3)}$ & 44.39 & 79.61 & 0.6797 \\
28	SFT no-evidence & \textbf{47.21} & \textbf{48.76} & -- & -- \\
29	RSFT CED & \underline{44.82{\scriptsize$\pm$0.51}$^{(3)}$} & \underline{45.80} & 80.96 & 0.6487 \\
30	\bottomrule
31	\end{tabular}%
32	}
33	\vspace{-2mm}
34	\end{table}
35	
36	
37	\subsection{Evidence-Extraction Decoupling Spectrum}
38	\label{sec:spectrum}
39	
40	Because evidence and extraction share gradient capacity, different optimization paradigms handle this competition in qualitatively different ways. We organize the outcomes along a \emph{decoupling spectrum} from catastrophic collapse to no decoupling (Figure~\ref{fig:spectrum}; full data in Table~\ref{tab:spectrum}, Appendix; training dynamics in Figure~\ref{fig:grpo_dynamics}, Appendix).
41	
42	\paragraph{GRPO.}
43	Under QLoRA 4-bit quantization ($G{=}4$), GRPO drives Rel-F1 to 1.38 while Evi-F1 rises to 85.04 (EDCR 0.9876): quantization-constrained precision limits the effective parameter space, so the reward signal preferentially optimizes the easier sub-task~\citep{gao2023scaling}, resembling the quantized-actor divergence of \citet{li2026qurl}. Full-precision bf16 ($G{=}8$) avoids catastrophe (Rel-F1 45.49, EDCR 0.6318), confirming quantization precision rather than group size as the primary factor.
44	
45	\paragraph{DPO and RSFT.}
46	DPO exhibits substantial extraction degradation: Rel-F1 drops from 33.37 (1 epoch) to 31.45 (3 epochs) while Evi-F1 rises (80.90$\to$84.84). EDCR is non-monotonic (0.8123$\to$0.7503): despite worsening extraction, evidence selectivity improves with continued training, partially reducing the decoupling. RSFT maintains both capabilities simultaneously (Rel-F1 45.80, Evi-F1 80.96, EDCR 0.6487) because discrete output selection cannot exploit the extraction-evidence trade-off.
47	
48	\begin{figure}[t]
49	\centering
50	\includegraphics[width=\columnwidth]{fig_spectrum.pdf}
51	\caption{Decoupling spectrum. Each method is plotted by Rel-F1 (x-axis) and Evi-F1 (y-axis). Arrows indicate training progression for DPO and GRPO bf16. Decoupled methods drift toward the upper-left.}
52	\label{fig:spectrum}
53	\end{figure}
54	
55	
56	\subsection{Scale-Dependent Evidence Tax}
57	\label{sec:scaling}
58	
59	The evidence tax, defined as Ign-F1(no-evidence) $-$ Ign-F1(with-evidence) on the development set, is scale-dependent. Under matched evaluation conditions (\texttt{max\_new\_tokens}$=$2048, format-compliant intersection; Appendix~\ref{sec:training_tax}), the training-time tax reveals a within-family capacity threshold: evidence generation benefits 1.7B ($-$5.63pp; Appendix~\ref{sec:training_tax}), where it also halves the output duplication rate (60.5\%$\to$33.0\%; Appendix~\ref{sec:error_analysis}), but is approximately neutral at $\geq$4B (+0.25$\pm$0.47pp at 4B, $n{=}3$; +0.04pp at 8B; +0.03pp at 14B). Table~\ref{tab:scaling} and Figure~\ref{fig:evidence_tax} present RSFT performance and inference-time evidence tax across five models (Figure~\ref{fig:scaling} in Appendix). Evidence training also affects SFT seed variance in a scale-dependent manner: at 4B and 8B, with-evidence models show lower cross-seed spread than no-evidence models (25$\times$ and 1.4$\times$ compression, respectively), but at 1.7B the pattern reverses---with-evidence variance exceeds no-evidence variance, likely amplified by extreme truncation rates at this scale (Appendix~\ref{sec:training_tax}).
60	
61	RSFT navigates this capacity landscape through quality-based data selection rather than gradient pressure. Mean Ign-F1 improves across tested scales: +6.55pp at 1.7B, +1.24pp at 4B, +4.14pp at 8B, and +3.79pp at 14B (Table~\ref{tab:scaling}). RSFT from an independent SFT base (s44, Method B) achieves 51.52 Ign-F1 at 4B (+4.18pp over that base). This result confirms that RSFT gains are not contingent on a specific SFT checkpoint.
62	
63	Beyond mean performance, RSFT consistently reduces training variance (sign test: 4/4 scales, $p{=}0.0625$; $\chi^2$ CI analysis confirms non-overlapping intervals at the 1.7B scale; Cohen's $d \geq 1.79$ for 3/4 scales; Appendix~\ref{sec:variance_ci}). Three RSFT seeds from a shared SFT checkpoint yield standard deviations of 0.09pp at 1.7B, 0.51pp at 4B, and 0.50pp at 8B ($n{=}3$ each), compared to SFT cross-seed variation of 2.79pp, 3.80pp, and 3.23pp respectively. While these measure different sources of variance (SFT reflects full training runs from different random seeds; RSFT reflects additional fine-tuning from a fixed base), the practical consequence is direct: across all Qwen3 scales with $\geq$3 seeds, variance compression is 31$\times$ at 1.7B, 7.5$\times$ at 4B, and 6.5$\times$ at 8B (point estimates from $N{=}3$ seeds; confidence intervals are wide, Appendix~\ref{sec:variance_ci}). The 1.7B RSFT model (51.19 Ign-F1, std 0.09pp) approaches 8B SFT performance (50.19, std 3.23pp) at 4.7$\times$ fewer parameters---comparable in mean yet 36$\times$ more predictable.
64	
65	Cross-family validation on LLaMA-3.1-8B confirms these patterns. All three RSFT seeds (55.87--57.14) exceed all three SFT seeds (48.02--53.84), yielding complete pairwise seed separation (Cohen's $d{=}2.58$) and 4.6$\times$ variance compression (std 2.92pp $\to$ 0.64pp). The SFT seed lottery is starkest at s44 (48.02 Ign-F1, 24.4\% truncation, elevated Evi-F1 85\%), a degenerate outcome that RSFT eliminates entirely (s44: 55.87). This robustness extends to inference-time format changes: LLaMA SFT models evaluated without evidence at 1024 tokens suffer 38--42\% truncation with Ign-F1 collapsing to ${\sim}$0.33 (s43/s44), while RSFT models truncate only 18--19\% with stable performance (55.41$\pm$0.13pp), indicating that CED filtering selects for compact output structure.
66	
67	For RSFT models, the inference-time evidence tax (same model evaluated with vs.\ without evidence output) preserves the benefit direction at 1.7B ($-$7.75pp, confirmed with 2048-token no-evidence evaluation that rules out truncation). At 4B, where the training-time tax is approximately neutral (+0.25$\pm$0.47pp; Appendix~\ref{sec:training_tax}), the RSFT inference-time tax is similarly small (+0.94pp). At 8B, the tax reverses to a benefit ($-$0.78pp), and at 14B the benefit is largest ($-$4.54pp). RSFT thus maintains or improves extraction quality with evidence across the Qwen3 family. LLaMA-3.1-8B RSFT shows a larger inference-time evidence benefit ($-$2.17$\pm$0.76pp, three-seed mean, vs.\ $-$0.78pp for Qwen3-8B), confirming that both performance gains and training reliability generalize across model families.
68	
69	The effect of RSFT on inference-time evidence dependence is heterogeneous. At 1.7B, RSFT maintains strong evidence benefit ($-$5.43pp\textsuperscript{$\ddagger$}), comparable to SFT ($-$4.86pp). At 4B, RSFT introduces a mild evidence cost (+1.65$\pm$0.29pp, three-seed mean), the Qwen3 scale with the largest positive RSFT test tax. Within the Qwen3 family at $\geq$8B, RSFT approaches evidence neutrality ($-$0.91$\pm$0.74pp at 8B, three-seed mean). Cross-architecture, LLaMA-3.1-8B shows partial compression: SFT tax of $-$4.94pp reduces to $-$1.46$\pm$0.40pp (two-seed mean) under RSFT, consistent with the cross-family variation observed in SFT evidence tax (Appendix~\ref{sec:training_tax}).
70	
71	\begin{table}[t]
72	\centering
73	\caption{RSFT performance and inference-time evidence tax across model scales (DocRED dev Ign-F1). LLaMA-3.1-8B included for cross-family validation. Mean $\pm$ std$^{(\text{seeds})}$.}
74	\label{tab:scaling}
75	\small
76	\resizebox{\columnwidth}{!}{%
77	\begin{tabular}{lcccc}
78	\toprule
79	\textbf{Model} & \textbf{SFT w/ evi} & \textbf{RSFT} & \textbf{RSFT Tax}$^\dagger$ & \textbf{RSFT Gain} \\
80	\midrule
81	Qwen3-1.7B & 44.64{\scriptsize$\pm$2.79}$^{(3)}$ & 51.19{\scriptsize$\pm$0.09}$^{(3)}$ & $-$7.75 & +6.55 \\
82	Qwen3-4B & 43.58{\scriptsize$\pm$3.80}$^{(3)}$ & 44.82{\scriptsize$\pm$0.51}$^{(3)}$ & +0.94 & +1.24 \\
83	Qwen3-8B & 50.19{\scriptsize$\pm$3.23}$^{(3)}$ & 54.33{\scriptsize$\pm$0.50}$^{(3)}$ & $-$0.78 & +4.14 \\
84	Qwen3-14B & 55.07 & 58.86 & $-$4.54 & +3.79 \\
85	LLaMA-3.1-8B & 51.09{\scriptsize$\pm$2.92}$^{(3)}$ & 56.54{\scriptsize$\pm$0.64}$^{(3)}$ & $-$2.17{\scriptsize$\pm$0.76}$^{(3)}$ & +5.45 \\
86	\bottomrule
87	\end{tabular}%
88	}
89	\vspace{-2mm}
90	{\raggedright\footnotesize $^\dagger$Inference-time: same RSFT model with vs.\ without evidence output. No-evi eval uses \texttt{max\_new\_tokens}$=$2048; with-evi eval uses 1024 (1.7B uses 2048 for both). Tax $=$ no-evi $-$ with-evi; positive $=$ cost. Seeds: 1.7B s42; 4B Method B s44; 8B, 14B: s42; LLaMA: three-seed mean. Training-time tax (matched@2048 fair evaluation) in Appendix~\ref{sec:training_tax}.\par}
91	\end{table}
92	
93	\begin{figure}[t]
94	\centering
95	\includegraphics[width=\columnwidth]{fig_evidence_tax.pdf}
96	\vspace{-2mm}
97	\caption{Inference-time evidence tax across model scales (RSFT models, Re-DocRED test). Negative values indicate evidence \emph{benefits} extraction. Error bars show $\pm$1 std where $\geq$2 seeds are available; 1.7B is a single seed ($n{=}1$).}
98	\label{fig:evidence_tax}
99	\end{figure}
100	
101	\subsection{Evidence Strategy Comparison}
102	\label{sec:evidence_strategy}
103	
104	We compare joint generation against post-hoc BM25 retrieval (entity-constrained, $k{=}2$), using Evi-F1 (joint) with the DREEAM-protocol denominator~\citep{ma2023dreeam}. Post-hoc retrieval achieves higher Rel-F1 (48.76) by avoiding the evidence tax but lower Evi-F1 (joint) of 34.7 (EDCR 0.766). RSFT CED reaches 36.1 (EDCR 0.654), a 1.4-point evidence advantage. CED reranking at inference (best-of-$N{=}8$ by CED score) achieves Rel-F1 48.64 and Evi-F1 81.88 (TP-only), approaching no-evidence extraction quality while preserving evidence.
105	
106	
107	\subsection{Generalization}
108	\label{sec:generalization}
109	
110	Cross-architecture validation on LLaMA-3.1-8B (Table~\ref{tab:scaling}) shows the largest RSFT gain (+5.45pp) with complete pairwise seed separation (\S\ref{sec:scaling}). The RSFT improvement transfers across datasets: on Re-DocRED~\citep{tan2022redocred}, RSFT achieves 41.45 Ign-F1 (+4.86pp over SFT 36.59), matching the DocRED gain (+5.08pp). Our best joint Evi-F1 (36.1, DREEAM-protocol) falls below supervised DREEAM (54.01\%~\citep{ma2023dreeam}), a gap driven by extraction performance rather than evidence quality (TP-only Evi-F1 exceeds 80\%). On the Re-DocRED test set, RSFT Ign-F1 drops approximately 20pp relative to dev across all evaluated scales (e.g., 14B: 58.9$\to$38.5), attributable to 2.82$\times$ higher annotation density in test (34.7 vs.\ 12.3 gold triples per document); model ranking is perfectly preserved (Spearman $\rho{=}1.0$; Table~\ref{tab:test_results} in Appendix). Full results appear in Appendix~\ref{sec:generalization_full}.
111	
112	
113	\subsection{Discussion}
114	\label{sec:analysis}
115	
116	EDCR (\S\ref{sec:edcr}) validates as a diagnostic at both cross-method ($\rho = -0.89$, $p = 0.007$) and per-relation levels ($\rho = -0.79$, $n = 76$, $p < 0.001$; Appendix~\ref{sec:edcr_per_relation}), the latter orthogonal to Evi-F1 ($\rho = -0.06$); partial correlations controlling for shared components are virtually unchanged ($\rho = -0.8541$ vs.\ $-0.8554$). CED and flat-NLI produce comparable RSFT results (Rel-F1 45.63 vs.\ 45.61); stricter selection ($k{=}1$) outperforms $k{=}3$ by 1.02 Ign-F1 despite fewer examples (Appendix~\ref{sec:ablation_full}). RSFT reduces truncation FN, hallucinated FP, and duplicates by 6--22\% across scales, but evidence quality is unchanged ($\Delta < 0.4$pp; Appendix~\ref{sec:error_analysis}): RSFT improves \emph{what} the model extracts but not \emph{how well} it grounds extractions.
117	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0ef7124a-c728-45c0-89b8-7058c133dff4",
  "isSidechain": false,
  "promptId": "659f4775-47ec-4bb9-8db5-86432609ca56",
  "type": "user",
  "uuid": "98517fc1-78d6-49a4-bef2-5f158afece2c",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/experiments.tex",
      "content": "\\section{Experiments}\n\\label{sec:experiments}\n\n\\subsection{Experimental Setup}\n\\label{sec:setup}\n\nWe evaluate on DocRED~\\citep{yao2019docred} (3,053 training / 998 dev documents, 96 relation types) with Re-DocRED~\\citep{tan2022redocred} for cross-dataset validation. Our primary model is Qwen3-4B; we also train Qwen3-1.7B, 8B, and 14B to study scale effects, with LLaMA-3.1-8B for cross-family validation. All models use LoRA~\\citep{hu2022lora} ($r{=}64$, $\\alpha{=}128$) with structured output jointly producing triples and evidence. RSFT selects the top-$k{=}1$ of $N{=}8$ samples by CED score (\\S\\ref{sec:ced}); GRPO uses group sizes $G{=}4$ (QLoRA) and $G{=}8$ (bf16); DPO constructs preference pairs from CED-ranked outputs. We report Ign-F1 (primary; ignores training-set triples), Rel-F1, Evi-F1 (TP-only and joint per DREEAM protocol~\\citep{ma2023dreeam}), and EDCR (\\S\\ref{sec:edcr}). Detailed hyperparameters appear in the Appendix.\n\n\n\\subsection{Main Results}\n\\label{sec:main_results}\n\nTable~\\ref{tab:main} presents the primary comparison on Qwen3-4B. The SFT baseline exhibits high seed sensitivity (mean Ign-F1 43.58, std 3.80pp, range 39.74--47.34). Removing evidence entirely (no-evidence SFT, s42) reaches 47.21 Ign-F1.\n\nRSFT CED achieves 44.82 Ign-F1 (+1.24 over SFT mean) with substantially lower variance (std 0.51pp), though these reflect different sources of variation (Section~\\ref{sec:scaling}). Even the weakest RSFT seed (44.23) exceeds the SFT mean. Evidence quality improves (Evi-F1 80.96 vs.\\ 79.61) and coupling tightens (EDCR 0.6487 vs.\\ 0.6797). Per-seed results appear in Appendix~\\ref{sec:ablation_full}.\n\n\\begin{table}[t]\n\\centering\n\\caption{Main results on DocRED dev (Qwen3-4B). Ign-F1 shows mean $\\pm$ std$^{(\\text{seeds})}$; other metrics are same-seed means. Best \\textbf{bold}; best evidence-generating \\underline{underlined}. Per-seed: Appendix~\\ref{tab:ablation_full}.}\n\\label{tab:main}\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Method} & \\textbf{Ign-F1} & \\textbf{Rel-F1} & \\textbf{Evi-F1} & \\textbf{EDCR} \\\\\n\\midrule\nSFT baseline & 43.58{\\scriptsize$\\pm$3.80}$^{(3)}$ & 44.39 & 79.61 & 0.6797 \\\\\nSFT no-evidence & \\textbf{47.21} & \\textbf{48.76} & -- & -- \\\\\nRSFT CED & \\underline{44.82{\\scriptsize$\\pm$0.51}$^{(3)}$} & \\underline{45.80} & 80.96 & 0.6487 \\\\\n\\bottomrule\n\\end{tabular}%\n}\n\\vspace{-2mm}\n\\end{table}\n\n\n\\subsection{Evidence-Extraction Decoupling Spectrum}\n\\label{sec:spectrum}\n\nBecause evidence and extraction share gradient capacity, different optimization paradigms handle this competition in qualitatively different ways. We organize the outcomes along a \\emph{decoupling spectrum} from catastrophic collapse to no decoupling (Figure~\\ref{fig:spectrum}; full data in Table~\\ref{tab:spectrum}, Appendix; training dynamics in Figure~\\ref{fig:grpo_dynamics}, Appendix).\n\n\\paragraph{GRPO.}\nUnder QLoRA 4-bit quantization ($G{=}4$), GRPO drives Rel-F1 to 1.38 while Evi-F1 rises to 85.04 (EDCR 0.9876): quantization-constrained precision limits the effective parameter space, so the reward signal preferentially optimizes the easier sub-task~\\citep{gao2023scaling}, resembling the quantized-actor divergence of \\citet{li2026qurl}. Full-precision bf16 ($G{=}8$) avoids catastrophe (Rel-F1 45.49, EDCR 0.6318), confirming quantization precision rather than group size as the primary factor.\n\n\\paragraph{DPO and RSFT.}\nDPO exhibits substantial extraction degradation: Rel-F1 drops from 33.37 (1 epoch) to 31.45 (3 epochs) while Evi-F1 rises (80.90$\\to$84.84). EDCR is non-monotonic (0.8123$\\to$0.7503): despite worsening extraction, evidence selectivity improves with continued training, partially reducing the decoupling. RSFT maintains both capabilities simultaneously (Rel-F1 45.80, Evi-F1 80.96, EDCR 0.6487) because discrete output selection cannot exploit the extraction-evidence trade-off.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig_spectrum.pdf}\n\\caption{Decoupling spectrum. Each method is plotted by Rel-F1 (x-axis) and Evi-F1 (y-axis). Arrows indicate training progression for DPO and GRPO bf16. Decoupled methods drift toward the upper-left.}\n\\label{fig:spectrum}\n\\end{figure}\n\n\n\\subsection{Scale-Dependent Evidence Tax}\n\\label{sec:scaling}\n\nThe evidence tax, defined as Ign-F1(no-evidence) $-$ Ign-F1(with-evidence) on the development set, is scale-dependent. Under matched evaluation conditions (\\texttt{max\\_new\\_tokens}$=$2048, format-compliant intersection; Appendix~\\ref{sec:training_tax}), the training-time tax reveals a within-family capacity threshold: evidence generation benefits 1.7B ($-$5.63pp; Appendix~\\ref{sec:training_tax}), where it also halves the output duplication rate (60.5\\%$\\to$33.0\\%; Appendix~\\ref{sec:error_analysis}), but is approximately neutral at $\\geq$4B (+0.25$\\pm$0.47pp at 4B, $n{=}3$; +0.04pp at 8B; +0.03pp at 14B). Table~\\ref{tab:scaling} and Figure~\\ref{fig:evidence_tax} present RSFT performance and inference-time evidence tax across five models (Figure~\\ref{fig:scaling} in Appendix). Evidence training also affects SFT seed variance in a scale-dependent manner: at 4B and 8B, with-evidence models show lower cross-seed spread than no-evidence models (25$\\times$ and 1.4$\\times$ compression, respectively), but at 1.7B the pattern reverses---with-evidence variance exceeds no-evidence variance, likely amplified by extreme truncation rates at this scale (Appendix~\\ref{sec:training_tax}).\n\nRSFT navigates this capacity landscape through quality-based data selection rather than gradient pressure. Mean Ign-F1 improves across tested scales: +6.55pp at 1.7B, +1.24pp at 4B, +4.14pp at 8B, and +3.79pp at 14B (Table~\\ref{tab:scaling}). RSFT from an independent SFT base (s44, Method B) achieves 51.52 Ign-F1 at 4B (+4.18pp over that base). This result confirms that RSFT gains are not contingent on a specific SFT checkpoint.\n\nBeyond mean performance, RSFT consistently reduces training variance (sign test: 4/4 scales, $p{=}0.0625$; $\\chi^2$ CI analysis confirms non-overlapping intervals at the 1.7B scale; Cohen's $d \\geq 1.79$ for 3/4 scales; Appendix~\\ref{sec:variance_ci}). Three RSFT seeds from a shared SFT checkpoint yield standard deviations of 0.09pp at 1.7B, 0.51pp at 4B, and 0.50pp at 8B ($n{=}3$ each), compared to SFT cross-seed variation of 2.79pp, 3.80pp, and 3.23pp respectively. While these measure different sources of variance (SFT reflects full training runs from different random seeds; RSFT reflects additional fine-tuning from a fixed base), the practical consequence is direct: across all Qwen3 scales with $\\geq$3 seeds, variance compression is 31$\\times$ at 1.7B, 7.5$\\times$ at 4B, and 6.5$\\times$ at 8B (point estimates from $N{=}3$ seeds; confidence intervals are wide, Appendix~\\ref{sec:variance_ci}). The 1.7B RSFT model (51.19 Ign-F1, std 0.09pp) approaches 8B SFT performance (50.19, std 3.23pp) at 4.7$\\times$ fewer parameters---comparable in mean yet 36$\\times$ more predictable.\n\nCross-family validation on LLaMA-3.1-8B confirms these patterns. All three RSFT seeds (55.87--57.14) exceed all three SFT seeds (48.02--53.84), yielding complete pairwise seed separation (Cohen's $d{=}2.58$) and 4.6$\\times$ variance compression (std 2.92pp $\\to$ 0.64pp). The SFT seed lottery is starkest at s44 (48.02 Ign-F1, 24.4\\% truncation, elevated Evi-F1 85\\%), a degenerate outcome that RSFT eliminates entirely (s44: 55.87). This robustness extends to inference-time format changes: LLaMA SFT models evaluated without evidence at 1024 tokens suffer 38--42\\% truncation with Ign-F1 collapsing to ${\\sim}$0.33 (s43/s44), while RSFT models truncate only 18--19\\% with stable performance (55.41$\\pm$0.13pp), indicating that CED filtering selects for compact output structure.\n\nFor RSFT models, the inference-time evidence tax (same model evaluated with vs.\\ without evidence output) preserves the benefit direction at 1.7B ($-$7.75pp, confirmed with 2048-token no-evidence evaluation that rules out truncation). At 4B, where the training-time tax is approximately neutral (+0.25$\\pm$0.47pp; Appendix~\\ref{sec:training_tax}), the RSFT inference-time tax is similarly small (+0.94pp). At 8B, the tax reverses to a benefit ($-$0.78pp), and at 14B the benefit is largest ($-$4.54pp). RSFT thus maintains or improves extraction quality with evidence across the Qwen3 family. LLaMA-3.1-8B RSFT shows a larger inference-time evidence benefit ($-$2.17$\\pm$0.76pp, three-seed mean, vs.\\ $-$0.78pp for Qwen3-8B), confirming that both performance gains and training reliability generalize across model families.\n\nThe effect of RSFT on inference-time evidence dependence is heterogeneous. At 1.7B, RSFT maintains strong evidence benefit ($-$5.43pp\\textsuperscript{$\\ddagger$}), comparable to SFT ($-$4.86pp). At 4B, RSFT introduces a mild evidence cost (+1.65$\\pm$0.29pp, three-seed mean), the Qwen3 scale with the largest positive RSFT test tax. Within the Qwen3 family at $\\geq$8B, RSFT approaches evidence neutrality ($-$0.91$\\pm$0.74pp at 8B, three-seed mean). Cross-architecture, LLaMA-3.1-8B shows partial compression: SFT tax of $-$4.94pp reduces to $-$1.46$\\pm$0.40pp (two-seed mean) under RSFT, consistent with the cross-family variation observed in SFT evidence tax (Appendix~\\ref{sec:training_tax}).\n\n\\begin{table}[t]\n\\centering\n\\caption{RSFT performance and inference-time evidence tax across model scales (DocRED dev Ign-F1). LLaMA-3.1-8B included for cross-family validation. Mean $\\pm$ std$^{(\\text{seeds})}$.}\n\\label{tab:scaling}\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Model} & \\textbf{SFT w/ evi} & \\textbf{RSFT} & \\textbf{RSFT Tax}$^\\dagger$ & \\textbf{RSFT Gain} \\\\\n\\midrule\nQwen3-1.7B & 44.64{\\scriptsize$\\pm$2.79}$^{(3)}$ & 51.19{\\scriptsize$\\pm$0.09}$^{(3)}$ & $-$7.75 & +6.55 \\\\\nQwen3-4B & 43.58{\\scriptsize$\\pm$3.80}$^{(3)}$ & 44.82{\\scriptsize$\\pm$0.51}$^{(3)}$ & +0.94 & +1.24 \\\\\nQwen3-8B & 50.19{\\scriptsize$\\pm$3.23}$^{(3)}$ & 54.33{\\scriptsize$\\pm$0.50}$^{(3)}$ & $-$0.78 & +4.14 \\\\\nQwen3-14B & 55.07 & 58.86 & $-$4.54 & +3.79 \\\\\nLLaMA-3.1-8B & 51.09{\\scriptsize$\\pm$2.92}$^{(3)}$ & 56.54{\\scriptsize$\\pm$0.64}$^{(3)}$ & $-$2.17{\\scriptsize$\\pm$0.76}$^{(3)}$ & +5.45 \\\\\n\\bottomrule\n\\end{tabular}%\n}\n\\vspace{-2mm}\n{\\raggedright\\footnotesize $^\\dagger$Inference-time: same RSFT model with vs.\\ without evidence output. No-evi eval uses \\texttt{max\\_new\\_tokens}$=$2048; with-evi eval uses 1024 (1.7B uses 2048 for both). Tax $=$ no-evi $-$ with-evi; positive $=$ cost. Seeds: 1.7B s42; 4B Method B s44; 8B, 14B: s42; LLaMA: three-seed mean. Training-time tax (matched@2048 fair evaluation) in Appendix~\\ref{sec:training_tax}.\\par}\n\\end{table}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig_evidence_tax.pdf}\n\\vspace{-2mm}\n\\caption{Inference-time evidence tax across model scales (RSFT models, Re-DocRED test). Negative values indicate evidence \\emph{benefits} extraction. Error bars show $\\pm$1 std where $\\geq$2 seeds are available; 1.7B is a single seed ($n{=}1$).}\n\\label{fig:evidence_tax}\n\\end{figure}\n\n\\subsection{Evidence Strategy Comparison}\n\\label{sec:evidence_strategy}\n\nWe compare joint generation against post-hoc BM25 retrieval (entity-constrained, $k{=}2$), using Evi-F1 (joint) with the DREEAM-protocol denominator~\\citep{ma2023dreeam}. Post-hoc retrieval achieves higher Rel-F1 (48.76) by avoiding the evidence tax but lower Evi-F1 (joint) of 34.7 (EDCR 0.766). RSFT CED reaches 36.1 (EDCR 0.654), a 1.4-point evidence advantage. CED reranking at inference (best-of-$N{=}8$ by CED score) achieves Rel-F1 48.64 and Evi-F1 81.88 (TP-only), approaching no-evidence extraction quality while preserving evidence.\n\n\n\\subsection{Generalization}\n\\label{sec:generalization}\n\nCross-architecture validation on LLaMA-3.1-8B (Table~\\ref{tab:scaling}) shows the largest RSFT gain (+5.45pp) with complete pairwise seed separation (\\S\\ref{sec:scaling}). The RSFT improvement transfers across datasets: on Re-DocRED~\\citep{tan2022redocred}, RSFT achieves 41.45 Ign-F1 (+4.86pp over SFT 36.59), matching the DocRED gain (+5.08pp). Our best joint Evi-F1 (36.1, DREEAM-protocol) falls below supervised DREEAM (54.01\\%~\\citep{ma2023dreeam}), a gap driven by extraction performance rather than evidence quality (TP-only Evi-F1 exceeds 80\\%). On the Re-DocRED test set, RSFT Ign-F1 drops approximately 20pp relative to dev across all evaluated scales (e.g., 14B: 58.9$\\to$38.5), attributable to 2.82$\\times$ higher annotation density in test (34.7 vs.\\ 12.3 gold triples per document); model ranking is perfectly preserved (Spearman $\\rho{=}1.0$; Table~\\ref{tab:test_results} in Appendix). Full results appear in Appendix~\\ref{sec:generalization_full}.\n\n\n\\subsection{Discussion}\n\\label{sec:analysis}\n\nEDCR (\\S\\ref{sec:edcr}) validates as a diagnostic at both cross-method ($\\rho = -0.89$, $p = 0.007$) and per-relation levels ($\\rho = -0.79$, $n = 76$, $p < 0.001$; Appendix~\\ref{sec:edcr_per_relation}), the latter orthogonal to Evi-F1 ($\\rho = -0.06$); partial correlations controlling for shared components are virtually unchanged ($\\rho = -0.8541$ vs.\\ $-0.8554$). CED and flat-NLI produce comparable RSFT results (Rel-F1 45.63 vs.\\ 45.61); stricter selection ($k{=}1$) outperforms $k{=}3$ by 1.02 Ign-F1 despite fewer examples (Appendix~\\ref{sec:ablation_full}). RSFT reduces truncation FN, hallucinated FP, and duplicates by 6--22\\% across scales, but evidence quality is unchanged ($\\Delta < 0.4$pp; Appendix~\\ref{sec:error_analysis}): RSFT improves \\emph{what} the model extracts but not \\emph{how well} it grounds extractions.\n",
      "numLines": 117,
      "startLine": 1,
      "totalLines": 117
    }
  },
  "sourceToolAssistantUUID": "0ef7124a-c728-45c0-89b8-7058c133dff4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "6a109daa-4474-48f0-ab6d-eef9007c0510",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-23T19:16:24.768Z_

<details open><summary>🔧 Tool call — Read · `toolu_014G82EspEZRtzNLuNhhiED2`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "98517fc1-78d6-49a4-bef2-5f158afece2c",
  "isSidechain": false,
  "requestId": "req_011CbL36289gvUXAKzRzAYg9",
  "type": "assistant",
  "uuid": "d11c4100-ec65-4541-8811-62860be4800d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "6a109daa-4474-48f0-ab6d-eef9007c0510",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019khDA8yXxCp24kUd1s4EQH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12651,
      "cache_read_input_tokens": 11841,
      "output_tokens": 466,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12651,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 466,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12651,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12651
          },
          "type": "message"
        }
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

_source line 18 · 2026-05-23T19:16:24.773Z_

<details><summary>↩ Tool result · `toolu_014G82EspEZRtzNLuNhhiED2`</summary>

```text
1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We formalize evidence-grounded document-level relation extraction as a structured generation task and compare three post-training paradigms across three fully evaluated scales (1.7B, 4B, 8B) with 14B validation, two model families, and two datasets. The evidence tax is not a fixed penalty but a landscape shaped by capacity, optimization paradigm, and data quality filtering.
5	RSFT improves mean extraction across all tested scales and reduces training variance at every evaluated configuration; a 1.7B RSFT model approaches 8B SFT performance at 4.7$\times$ fewer parameters.
6	Future work should investigate targeted evidence rewards and extend evaluation to non-Wikipedia domains.
7	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d11c4100-ec65-4541-8811-62860be4800d",
  "isSidechain": false,
  "promptId": "659f4775-47ec-4bb9-8db5-86432609ca56",
  "type": "user",
  "uuid": "3d76d62a-f13f-47bd-b620-f17febf7d010",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/conclusion.tex",
      "content": "\\section{Conclusion}\n\\label{sec:conclusion}\n\nWe formalize evidence-grounded document-level relation extraction as a structured generation task and compare three post-training paradigms across three fully evaluated scales (1.7B, 4B, 8B) with 14B validation, two model families, and two datasets. The evidence tax is not a fixed penalty but a landscape shaped by capacity, optimization paradigm, and data quality filtering.\nRSFT improves mean extraction across all tested scales and reduces training variance at every evaluated configuration; a 1.7B RSFT model approaches 8B SFT performance at 4.7$\\times$ fewer parameters.\nFuture work should investigate targeted evidence rewards and extend evaluation to non-Wikipedia domains.\n",
      "numLines": 7,
      "startLine": 1,
      "totalLines": 7
    }
  },
  "sourceToolAssistantUUID": "d11c4100-ec65-4541-8811-62860be4800d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "6a109daa-4474-48f0-ab6d-eef9007c0510",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-23T19:16:25.213Z_

<details open><summary>🔧 Tool call — Read · `toolu_015B4Dp9SzVVZZBcmiVBMTPn`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3d76d62a-f13f-47bd-b620-f17febf7d010",
  "isSidechain": false,
  "requestId": "req_011CbL36289gvUXAKzRzAYg9",
  "type": "assistant",
  "uuid": "7cddcce9-5c4a-43e0-937a-f24636f0993c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "6a109daa-4474-48f0-ab6d-eef9007c0510",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019khDA8yXxCp24kUd1s4EQH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12651,
      "cache_read_input_tokens": 11841,
      "output_tokens": 466,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12651,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 466,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12651,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12651
          },
          "type": "message"
        }
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

_source line 20_

```json
{
  "type": "last-prompt",
  "leafUuid": "7cddcce9-5c4a-43e0-937a-f24636f0993c",
  "sessionId": "6a109daa-4474-48f0-ab6d-eef9007c0510"
}
```

---

### Runtime record

_source line 21_

```json
{
  "type": "ai-title",
  "aiTitle": "Audit paper numbers across LaTeX sections",
  "sessionId": "6a109daa-4474-48f0-ab6d-eef9007c0510"
}
```

---

### Tool result

_source line 22 · 2026-05-23T19:16:25.491Z_

<details><summary>↩ Tool result · `toolu_015B4Dp9SzVVZZBcmiVBMTPn`</summary>

```text
1	\section{Training Hyperparameters}
2	\label{sec:hyperparams}
3	
4	Table~\ref{tab:hyperparams} lists the hyperparameters for all training configurations. All methods use LoRA with rank $r{=}64$ and $\alpha{=}128$ applied to all linear projections (attention and feed-forward). SFT and RSFT share the same optimizer settings; RSFT differs only in data construction (top-1 CED-selected outputs from $N{=}8$ candidates). GRPO and DPO use lower learning rates to stabilize post-SFT optimization.
5	
6	\begin{table*}[t]
7	\centering
8	\caption{Training hyperparameters for all optimization paradigms. All experiments use Qwen3-4B as the base model with LoRA adaptation. A dash indicates that the parameter is not applicable to the given method.}
9	\label{tab:hyperparams}
10	\small
11	\begin{tabular}{lccccc}
12	\toprule
13	\textbf{Parameter} & \textbf{SFT} & \textbf{RSFT} & \textbf{GRPO QLoRA} & \textbf{GRPO bf16} & \textbf{DPO} \\
14	\midrule
15	Base model & Qwen3-4B & Qwen3-4B & Qwen3-4B & Qwen3-4B & Qwen3-4B \\
16	LoRA rank $r$ & 64 & 64 & 64 & 64 & 64 \\
17	LoRA $\alpha$ & 128 & 128 & 128 & 128 & 128 \\
18	Learning rate & 2e-5 & 2e-5 & 5e-6 & 5e-6 & 5e-7 \\
19	Batch size (effective) & 16 & 16 & 4 & 8 & 4 \\
20	Epochs & 3 & 3 & -- & -- & 1, 3\textsuperscript{$\star$} \\
21	Max steps & -- & -- & 100 & 100 & -- \\
22	Gradient accumulation & 4 & 4 & 16 & 4 & 4 \\
23	Max new tokens & 1024 & 1024 & 1024 & 1024 & 1024 \\
24	Quantization & -- & -- & NF4 4-bit & bf16 & bf16 \\
25	Group size $G$ & -- & -- & 4 & 8 & -- \\
26	KL coefficient & -- & -- & 0.01 & 0.01 & -- \\
27	$\beta$ (DPO) & -- & -- & -- & -- & 0.1 \\
28	Candidates $N$ & -- & 8 & -- & -- & 8 \\
29	Top-$k$ selection & -- & 1 & -- & -- & -- \\
30	Training samples & 3,053 & 2,718 & 3,053 & 3,053 & 3,053 \\
31	Scoring function & -- & CED & CED & CED & CED \\
32	\bottomrule
33	\end{tabular}
34	\vspace{1mm}
35	{\raggedright\footnotesize \textsuperscript{$\star$}DPO is trained for both 1 and 3 epochs to observe temporal dynamics of the evidence-extraction trade-off (Section~\ref{sec:spectrum}).\par}
36	\end{table*}
37	
38	
39	\section{Full Ablation Results}
40	\label{sec:ablation_full}
41	
42	Table~\ref{tab:ablation_full} reports the complete RSFT ablation across scoring functions, top-$k$ values, and random seeds. RSFT CED $k{=}1$ achieves a four-seed mean Ign-F1 of 44.66 (standard deviation 0.49), confirming robust improvement over the SFT s42 baseline (39.74). The three-seed mean reported in Table~\ref{tab:main} (44.82, seeds 42/43/44) is slightly higher because it excludes the lowest seed (s45: 44.16). Random selection RSFT $k{=}1$ (41.14 Ign-F1), which samples from the same candidate pool without CED scoring, improves only +1.40pp over SFT s42 versus +4.92pp for CED RSFT, confirming that CED scoring precision drives the majority of the RSFT gain. Increasing $k$ to 3 slightly degrades performance (43.64 Ign-F1), consistent with the intuition that stricter selection yields higher-quality training data. The flat-NLI scoring variant produces comparable Rel-F1 (mean 45.61 vs.\ 45.63 for CED, a difference of 0.02pp). Both CED and flat-NLI improve substantially over the SFT baseline while maintaining or improving Evi-F1, confirming that the RSFT gains are driven by quality-based data selection rather than by the specific contrastive formulation.
43	
44	\paragraph{NLI scoring comparison.} Across all available seeds, CED RSFT achieves mean Rel-F1 of 45.63 (seeds 42, 43, 44, 45: range 45.14--46.21), and flat-NLI RSFT achieves mean Rel-F1 of 45.61 (seeds 42, 43: range 45.35--45.86). The 0.02pp difference suggests comparable performance: CED's contrastive design does not substantially outperform simpler NLI scoring for RSFT data selection. We adopt CED as the default because its contrastive formulation produces per-triple discrimination scores that support interpretable error analysis.
45	
46	\paragraph{Top-$k$ selection.} Best-of-8 ($k{=}1$) yields mean Ign-F1 44.66 and Rel-F1 45.63, while top-3-of-8 ($k{=}3$) produces 43.64 and 44.54. The selected training data confirms the quality gap: $k{=}1$ data has mean extraction F1 of 61.57 and mean CED of 0.6683, versus 57.61 and 0.6205 for $k{=}3$. Despite $k{=}3$ providing 2.96$\times$ more training examples, the additional lower-ranked samples introduce noise that degrades final performance.
47	
48	\paragraph{NLI scorer capacity.} CED filtering is robust to NLI model capacity: replacing the default scorer (DeBERTa-v3-base, 86M parameters) with DeBERTa-v3-large (304M) yields only +1.10pp Ign-F1 (45.33 vs.\ 44.23, s42), a difference within the v3-base seed noise of 0.88pp (s42: 44.23, s44: 45.11). Other metrics confirm the pattern: Rel-F1 improves by +1.19pp (46.36 vs.\ 45.17), Evi-F1 by +0.20pp (81.94 vs.\ 81.74), while EDCR shifts by $-$0.39pp (0.6530 vs.\ 0.6569)---the inconsistent direction across metrics rules out systematic improvement from a larger scorer. This insensitivity supports v3-base as a cost-effective default, as a 3.5$\times$ larger scorer does not materially improve CED-based data selection.
49	
50	\begin{table}[t]
51	\centering
52	\caption{Full RSFT ablation on DocRED dev set (Qwen3-4B). CED and flat-NLI denote the scoring function used for candidate selection. Best Ign-F1 among evidence-generating methods in \textbf{bold}.}
53	\label{tab:ablation_full}
54	\small
55	\resizebox{\columnwidth}{!}{%
56	\begin{tabular}{lcccc}
57	\toprule
58	\textbf{Configuration} & \textbf{Ign-F1} & \textbf{Rel-F1} & \textbf{Evi-F1} & \textbf{EDCR} \\
59	\midrule
60	SFT baseline (s42) & 39.74 & 40.49 & 79.86 & 0.6982 \\
61	SFT no-evidence & \textbf{47.21} & 48.76 & -- & -- \\
62	\midrule
63	RSFT random $k{=}1$ & 41.14 & 41.98 & 79.64 & 0.6971 \\
64	\midrule
65	RSFT CED $k{=}1$ (s42) & 44.23 & 45.17 & 81.74 & 0.6569 \\
66	RSFT CED $k{=}1$ (s43) & 45.12 & 46.01 & 80.63 & 0.6542 \\
67	RSFT CED $k{=}1$ (s44) & 45.11 & 46.21 & 80.50 & 0.6350 \\
68	RSFT CED $k{=}1$ (s45) & 44.16 & 45.14 & 81.74 & 0.6550 \\
69	RSFT CED $k{=}1$ (mean) & 44.66 & 45.63 & 81.15 & 0.6503 \\
70	\midrule
71	RSFT CED $k{=}3$ & 43.64 & 44.54 & 80.88 & 0.6635 \\
72	\midrule
73	RSFT flat-NLI (s42) & -- & 45.35 & 80.43 & 0.6431 \\
74	RSFT flat-NLI (s43) & -- & 45.86 & 81.58 & 0.6505 \\
75	RSFT flat-NLI (mean) & -- & 45.61 & 81.01 & 0.6468 \\
76	\midrule
77	RSFT CED $k{=}1$ v3-large (s42) & 45.33 & 46.36 & 81.94 & 0.6530 \\
78	\bottomrule
79	\end{tabular}%
80	}
81	\end{table}
82	
83	
84	\section{Scaling Details}
85	\label{sec:scaling_details}
86	
87	Table~\ref{tab:cross_detail} supplements Table~\ref{tab:scaling} in the main text with per-scale Rel-F1 and Evi-F1 breakdowns. At 1.7B, RSFT improves Rel-F1 from 45.86 to 52.81 (+6.95, multi-seed mean) while achieving Evi-F1 82.63 and EDCR 0.6217. The 4B model shows the same pattern: Rel-F1 increases from 44.39 to 45.80 (+1.41, three-seed mean). For 8B, RSFT brings Rel-F1 from 51.87 to 56.07 (three-seed mean) with Evi-F1 of 81.26 and EDCR 0.6235, confirming tight coupling between extraction and evidence at this scale. At 14B, the SFT baseline already achieves strong Rel-F1 (56.11) and Evi-F1 (82.92).
88	
89	\begin{table}[t]
90	\centering
91	\caption{Detailed Rel-F1 and Evi-F1 across model scales on DocRED dev set. SFT and RSFT columns show multi-seed means where available (Qwen3 1.7B/4B/8B: 3-seed; 14B: single seed; LLaMA SFT Rel-F1/Evi-F1: s42 only; LLaMA RSFT: 3-seed).}
92	\label{tab:cross_detail}
93	\small
94	\resizebox{\columnwidth}{!}{%
95	\begin{tabular}{lccccc}
96	\toprule
97	\textbf{Model} & \textbf{SFT Rel-F1} & \textbf{SFT Evi-F1} & \textbf{RSFT Rel-F1} & \textbf{RSFT Evi-F1} & \textbf{RSFT EDCR} \\
98	\midrule
99	Qwen3-1.7B & 45.86 & 82.85 & 52.81 & 82.63 & 0.6217 \\
100	Qwen3-4B & 44.39 & 79.61 & 45.80 & 80.96 & 0.6487 \\
101	Qwen3-8B & 51.87 & 82.94 & 56.07 & 81.26 & 0.6235 \\
102	Qwen3-14B & 56.11 & 82.92 & -- & -- & -- \\
103	LLaMA-3.1-8B & 55.14 & 81.51 & 57.75 & 82.84 & 0.5804 \\
104	\bottomrule
105	\end{tabular}%
106	}
107	\end{table}
108	
109	\begin{figure}[t]
110	\centering
111	\includegraphics[width=\columnwidth]{fig_scaling.pdf}
112	\caption{Evidence tax across model scales. Bar heights show Ign-F1 for each training configuration. The gap between no-evidence and SFT bars reverses direction between 1.7B and 4B, revealing the scale-dependent nature of the evidence tax. RSFT consistently narrows the gap toward the no-evidence upper bound.}
113	\label{fig:scaling}
114	\end{figure}
115	
116	
117	\section{Variance Compression Confidence Intervals}
118	\label{sec:variance_ci}
119	
120	Table~\ref{tab:variance_ci} reports 95\% confidence intervals for SFT and RSFT standard deviations using the $\chi^2$ distribution ($N{=}3$ seeds per configuration). At 1.7B, the confidence intervals are fully non-overlapping (SFT lower bound 1.45pp $>$ RSFT upper bound 0.54pp), providing the strongest evidence for variance compression. At the remaining three scales, intervals overlap but point estimates are consistently in the same direction (SFT std $>$ RSFT std at all four scales; sign test $p = 0.0625$, one-sided binomial, $n = 4$, underpowered). Cohen's $d$ ranges from 0.46 (4B) to 3.31 (1.7B), with 1.7B and LLaMA-8B showing large effect sizes ($d > 2.5$).
121	
122	\begin{table}[t]
123	\centering
124	\caption{95\% confidence intervals for training variance ($\chi^2$ method, $N{=}3$ seeds). Compression is the ratio of SFT to RSFT point estimates (unrounded).}
125	\label{tab:variance_ci}
126	\small
127	\resizebox{\columnwidth}{!}{%
128	\begin{tabular}{lcccccc}
129	\toprule
130	\textbf{Scale} & \textbf{SFT std} & \textbf{SFT 95\% CI} & \textbf{RSFT std} & \textbf{RSFT 95\% CI} & \textbf{Compr.} & \textbf{Cohen's $d$} \\
131	\midrule
132	Qwen3-1.7B & 2.79 & [1.45, 17.55] & 0.09 & [0.04, 0.54] & 32.6$\times$ & 3.31 \\
133	Qwen3-4B & 3.80 & [1.98, 23.89] & 0.51 & [0.27, 3.21] & 7.5$\times$ & 0.46 \\
134	Qwen3-8B & 3.23 & [1.68, 20.31] & 0.50 & [0.26, 3.15] & 6.5$\times$ & 1.79 \\
135	LLaMA-3.1-8B & 2.92 & [1.52, 18.37] & 0.64 & [0.33, 4.01] & 4.6$\times$ & 2.58 \\
136	\bottomrule
137	\end{tabular}%
138	}
139	\vspace{-2mm}
140	{\raggedright\footnotesize Sign test: $p = 0.0625$ (one-sided binomial, $n = 4$; underpowered). The consistent direction (4/4 SFT $>$ RSFT), non-overlapping CIs at 1.7B, and large Cohen's $d$ at 1.7B and LLaMA provide practical evidence for variance compression despite limited statistical power from $N{=}3$ seeds.\par}
141	\end{table}
142	
143	
144	\section{Controlled Evaluation Subset}
145	\label{sec:fair_subset}
146	
147	The 1.7B evidence tax comparison (\S\ref{sec:scaling}) is confounded by differential truncation rates. At \texttt{max\_new\_tokens}$=$1024, the no-evidence model truncates 50.9\% of outputs (501/985 documents) versus 31.9\% (314/985) for the evidence model. To address this, we adopt a matched@2048 fair evaluation: both configurations are evaluated at \texttt{max\_new\_tokens}$=$2048, and the tax is computed on the intersection of documents where both produce format-compliant output. This yields 971/985 fair-subset documents, with a tax of $-$5.63pp (s42), confirming a genuine 1.7B evidence benefit. As additional validation, a stricter controlled subset at @1024 (excluding truncated or repetitive outputs; 442/985 documents) yields $-$6.2pp, with the stronger benefit attributable to the more aggressive filtering.
148	
149	Table~\ref{tab:mechanistic} provides a mechanistic breakdown across three scales (evaluated at @1024). Output duplication rate (fraction of documents containing $\geq$3 repeated triples or unique/total $< 0.5$) declines monotonically with scale for both training configurations, but the gap between no-evidence and with-evidence models narrows from 27.5pp at 1.7B to 3.7pp at 8B. This pattern supports the implicit regularization hypothesis: evidence generation forces smaller models to attend to supporting context, reducing degenerate repetition. At 4B, duplication is already moderate (31.1\% with evidence), so the regularization benefit diminishes; under matched@2048 evaluation, the 4B training-time tax is approximately neutral (+0.25$\pm$0.47pp, three-seed mean). The truncation asymmetry reverses across scales: at 1.7B the no-evidence model truncates 19pp more often; at 8B the evidence model truncates 9pp more often due to the longer output format.
150	
151	\begin{table}[t]
152	\centering
153	\caption{Mechanistic breakdown of output quality across scales. Duplication rate: fraction of documents with degenerate outputs. Truncation $\Delta$: no-evidence rate minus with-evidence rate (positive means no-evidence truncates more).}
154	\label{tab:mechanistic}
155	\small
156	\begin{tabular}{lccccc}
157	\toprule
158	& \multicolumn{3}{c}{\textbf{Duplication Rate}} & \multicolumn{2}{c}{\textbf{Truncation}} \\
159	\cmidrule(lr){2-4} \cmidrule(lr){5-6}
160	\textbf{Scale} & \textbf{w/ evi} & \textbf{no-evi} & \textbf{Gap} & \textbf{$\Delta$} & \textbf{Pattern} \\
161	\midrule
162	1.7B & 33.0 & 60.5 & 27.5 & +19 & no-evi worse \\
163	4B & 31.1 & 43.2 & 12.1 & +2 & neutral \\
164	8B & 29.2 & 32.9 & 3.7 & $-$9 & evi worse \\
165	\bottomrule
166	\end{tabular}
167	\end{table}
168	
169	
170	\section{Training-Time Evidence Tax}
171	\label{sec:training_tax}
172	
173	The evidence tax can be measured in two ways. The \emph{training-time} tax compares separately trained models (SFT with evidence vs.\ SFT without evidence in the training output format). The \emph{inference-time} tax (reported in Table~\ref{tab:scaling}) evaluates the same RSFT model with and without evidence at inference time.
174	
175	Na\"ive comparisons at \texttt{max\_new\_tokens}$=$1024 are confounded by differential truncation rates (e.g., 50.9\% vs.\ 31.9\% at 1.7B). To control for this, we adopt a \emph{matched@2048 fair evaluation}: both configurations are evaluated at \texttt{max\_new\_tokens}$=$2048, and the tax is computed on the intersection of documents where both models produce format-compliant output. Table~\ref{tab:training_tax} reports the matched@2048 training-time tax across Qwen3 scales.
176	
177	The tax reveals a within-family capacity threshold: evidence generation benefits 1.7B ($-$5.63pp on 971/985 fair-subset documents) but is approximately neutral at $\geq$4B (+0.25$\pm$0.47pp at 4B across three seeds, +0.04pp at 8B, +0.03pp at 14B). At 1.7B, s42 is the strongest SFT seed (47.86 Ign-F1, +3.22pp above the three-seed mean of 44.64), so the benefit may be amplified relative to the population mean. LLaMA-3.1-8B SFT training-time tax is consistently negative but with high magnitude variance ($-$1.53 to $-$11.20pp, mean $-$5.19$\pm$5.25pp under matched@2048) and omitted from the table due to the s43 outlier (16.3\% no-evidence format failure inflates its tax); cross-architecture patterns are addressed in \S\ref{sec:generalization_full}.
178	
179	\begin{table}[t]
180	\centering
181	\caption{Training-time evidence tax under matched@2048 fair evaluation (DocRED dev Ign-F1). Both configurations evaluated at \texttt{max\_new\_tokens}$=$2048; tax computed on format-compliant intersection. Tax $=$ no-evidence $-$ with-evidence; positive $=$ cost.}
182	\label{tab:training_tax}
183	\small
184	\begin{tabular}{lcccc}
185	\toprule
186	\textbf{Model} & \textbf{Fair w/ evi} & \textbf{Fair no-evi} & \textbf{Evi Tax} & \textbf{Subset} \\
187	\midrule
188	Qwen3-1.7B & 48.38 & 42.75 & $-$5.63 & 971 \\
189	Qwen3-4B & -- & -- & +0.25{\scriptsize$\pm$0.47}$^{(3)}$ & $\geq$982 \\
190	Qwen3-8B & 50.15 & 50.19 & +0.04 & 984 \\
191	Qwen3-14B & 55.07 & 55.10 & +0.03 & 985$^\dagger$ \\
192	\bottomrule
193	\end{tabular}
194	\vspace{-2mm}
195	{\raggedright\footnotesize 1.7B and 8B are s42; 4B reports three-seed mean $\pm$ std (per-seed range: $-$0.19 to +0.73pp); 14B evaluated at @1024 with 0\% truncation for both configurations ($^\dagger$fair subset equals full dev set). Subset: documents in format-compliant intersection out of 985.\par}
196	\end{table}
197	
198	\paragraph{Evidence training and SFT seed variance.}
199	Evidence training's effect on SFT seed variance is also scale-dependent. At 4B, with-evidence SFT models show near-identical cross-seed spread (0.02pp) compared to no-evidence models (0.50pp), yielding 25$\times$ variance compression. At 8B, the compression is more modest (0.35pp vs.\ 0.48pp, 1.4$\times$). However, at 1.7B the pattern reverses: with-evidence seed spread (0.63pp) exceeds no-evidence spread (0.20pp). This reversal likely reflects the extreme truncation rates at 1.7B (75.6\% with-evidence, 94.4\% no-evidence at \texttt{max\_new\_tokens}$=$1024): truncated outputs produce noisy extraction results whose variance depends on which triples appear before the cutoff point. The RSFT variance compression reported in \S\ref{sec:scaling} is measured relative to SFT with-evidence baselines and holds at all scales regardless of this SFT-internal pattern.
200	
201	
202	\section{Why RSFT Avoids Decoupling}
203	\label{sec:rsft_theory}
204	
205	The structural difference between selection and optimization explains why RSFT does not exhibit the decoupling observed in gradient-based methods. GRPO and DPO update model parameters through gradients that optimize a reward signal. When two sub-tasks (extraction and evidence) compete for gradient capacity, the optimizer can discover and exploit the trade-off between them, improving one at the expense of the other. RSFT operates differently: it selects complete outputs and trains on them with standard supervised loss. Because the selection is discrete (accept or reject a full response), there is no gradient pathway through which the model can learn to sacrifice extraction for evidence quality. Only outputs where both extraction and evidence are jointly strong survive the CED filter. This property is not specific to RSFT's design but is a structural consequence of discrete selection over complete outputs: any selection-based method that filters on a joint quality criterion will inherit the same coupling guarantee. The implication for practitioners is direct: when optimizing for multiple coupled generation objectives, selection-based methods preserve inter-objective balance that gradient-based methods disrupt.
206	
207	
208	\section{Full Generalization Results}
209	\label{sec:generalization_full}
210	
211	\paragraph{Cross-family transfer.}
212	LLaMA-3.1-8B confirms the scaling patterns observed with Qwen3. Its SFT baseline achieves a three-seed mean of 51.09 Ign-F1 (std 2.92pp; s42: 53.84, s43: 51.42, s44: 48.02). Under matched@2048 fair evaluation, the training-time tax is consistently negative across all three seeds (s42: $-$1.53, s43: $-$11.20, s44: $-$2.83; mean $-$5.19$\pm$5.25pp), indicating that evidence generation consistently benefits LLaMA-3.1-8B. This contrasts with Qwen3-8B's approximately neutral tax (+0.04pp), suggesting that the evidence tax may be architecture-dependent at the 8B scale; however, the high magnitude variance (driven by s43, whose no-evidence configuration has a 16.3\% format failure rate that inflates the tax estimate) precludes precise quantification. RSFT CED improves LLaMA to a three-seed mean of 56.54 Ign-F1 (std 0.64pp; s42: 57.14, s43: 56.62, s44: 55.87), a +5.45 point gain over SFT mean (51.09), with 4.6$\times$ variance compression (2.92pp $\to$ 0.64pp), consistent with the pattern at the 8B scale (Qwen3-8B: +4.14, 6.5$\times$ compression).
213	
214	\paragraph{Cross-dataset robustness.}
215	On Re-DocRED~\citep{tan2022redocred}, the SFT baseline achieves 36.59 Ign-F1 (Evi-F1 81.70, EDCR 0.6674). RSFT CED improves this to 41.45 Ign-F1 (Evi-F1 81.82, EDCR 0.6210), a +4.86pp gain that closely matches the +5.08pp improvement on DocRED (RSFT three-seed mean minus SFT s42). This consistency across datasets with different annotation protocols confirms that RSFT's benefit generalizes beyond training-set-specific artifacts. Evidence quality remains stable across datasets (Evi-F1 81.82 vs.\ 81.15 on DocRED), and the EDCR reduction ($-0.046$) mirrors the DocRED pattern, further supporting the robustness of CED-based selection.
216	
217	\paragraph{Re-DocRED test set evaluation.}
218	Table~\ref{tab:test_results} reports SFT and RSFT performance on the Re-DocRED test set. We observe a consistent performance gap between dev and test sets, with test Ign-F1 approximately 20 percentage points lower (RSFT: 1.7B 51.2$\to$29.3, 4B 44.8$\to$25.0, 8B 54.3$\to$33.5, 14B 58.9$\to$38.5, LLaMA-8B 56.5$\to$35.5; SFT 1.7B: 44.6$\to$25.8). This gap is attributable to annotation density: the test set contains 34.7 gold triples per document versus 12.3 in the dev set (a 2.82$\times$ ratio), imposing a harder recall requirement. The gap magnitude is stable across scales and architectures (range: 18.9--21.9pp), and model ranking is perfectly preserved (Spearman $\rho{=}1.0$), indicating that the absolute drop reflects the test annotation scheme rather than a model-specific deficiency. At 14B, the RSFT advantage observed on dev (+3.79pp) reverses on test ($\Delta{=}{-}0.37$pp); we note that the SFT model's 50.6\% truncation rate implies longer outputs that generate more candidate triples to match the test set's dense annotation scheme.
219	
220	\begin{table}[t]
221	\centering
222	\caption{SFT and RSFT performance on Re-DocRED test set (Ign-F1 \%). Dev Ign-F1 (RSFT) from Table~\ref{tab:scaling}. All test results use s42.}
223	\label{tab:test_results}
224	\small
225	\resizebox{\columnwidth}{!}{%
226	\begin{tabular}{lccccccc}
227	\toprule
228	\textbf{Model} & \textbf{Dev} & \textbf{SFT} & \textbf{RSFT} & \textbf{$\Delta$} & \textbf{Tr. SFT} & \textbf{Tr. RSFT} & \textbf{Evi-F1} \\
229	\midrule
230	Qwen3-1.7B & 51.19 & 25.79 & 29.33 & +3.54 & 81.8 & 73.8 & 23.20 \\
231	Qwen3-4B & 44.82$^\dagger$ & 22.32 & 25.01 & +2.69 & 64.6 & 42.8 & 18.38 \\
232	Qwen3-8B & 54.33 & 31.06 & 33.53 & +2.47 & 82.0 & 1.8 & 25.26 \\
233	Qwen3-14B & 58.86 & 38.86 & 38.49 & $-$0.37 & 50.6 & 13.4 & 26.88 \\
234	LLaMA-3.1-8B & 56.54 & 34.20 & 35.54 & +1.34 & 65.4 & 56.6 & 25.09 \\
235	\bottomrule
236	\end{tabular}%
237	}
238	\vspace{-2mm}
239	{\raggedright\footnotesize $^\dagger$4B dev Ign-F1 is three-seed mean from original checkpoint; test results use retrained checkpoint (original unavailable for reproduction; retrained v2 achieves comparable dev performance, 43.88 vs.\ 44.23). $\Delta$: RSFT $-$ SFT. Evi-F1: RSFT joint (DREEAM protocol). Tr.: truncation rate (\%). Dev is RSFT three-seed mean from Table~\ref{tab:scaling}.\par}
240	\end{table}
241	
242	\paragraph{Test-set evidence tax.}
243	Table~\ref{tab:test_tax} reports the evidence tax on the Re-DocRED test set, comparing SFT models trained with and without evidence in the output format. Test-set evaluation confirms the directional pattern observed on development data across all five model configurations: the tax is negative (beneficial) at 1.7B ($-$4.86pp) and LLaMA-8B ($-$4.94pp), and near-neutral at mid-scales ($-$0.13pp at 4B, $-$0.32pp at 14B). The 8B test tax ($-$1.71pp) shows slight variation from its near-neutral dev counterpart (+0.04pp), though both remain modest relative to the 1.7B and LLaMA benefits.
244	
245	\begin{table}[t]
246	\centering
247	\caption{Evidence tax on Re-DocRED test set (Ign-F1 \%). Tax $=$ no-evi $-$ with-evi; negative $=$ benefit. All results use s42. Dev tax from Table~\ref{tab:training_tax}.}
248	\label{tab:test_tax}
249	\small
250	\resizebox{\columnwidth}{!}{%
251	\begin{tabular}{lcccc}
252	\toprule
253	\textbf{Model} & \textbf{With-evi} & \textbf{No-evi} & \textbf{Test Tax} & \textbf{Dev Tax} \\
254	\midrule
255	Qwen3-1.7B & 25.79 & 20.93 & $-$4.86 & $-$5.63 \\
256	Qwen3-4B & 22.32 & 22.19 & $-$0.13 & +0.25 \\
257	Qwen3-8B & 31.06 & 29.35 & $-$1.71 & +0.04 \\
258	Qwen3-14B & 38.86 & 38.54 & $-$0.32 & +0.03 \\
259	LLaMA-3.1-8B & 34.20 & 29.26 & $-$4.94 & $-$5.19 \\
260	\bottomrule
261	\end{tabular}%
262	}
263	\end{table}
264	
265	\paragraph{RSFT test-set evidence tax.}
266	Table~\ref{tab:rsft_test_tax} reports the inference-time evidence tax for RSFT models on the Re-DocRED test set (same RSFT model evaluated with vs.\ without evidence output; per-seed s42 values). Figure~\ref{fig:evidence_tax} presents multi-seed means with error bars where $\geq$2 seeds are available. At 1.7B, RSFT preserves a strong evidence benefit ($-$5.43pp), comparable to the SFT tax ($-$4.86pp). At 4B, the tax is mildly positive (+1.65$\pm$0.29pp, three-seed mean; s42: +1.51pp), the Qwen3 scale with the largest positive RSFT test tax; this contrasts with the near-neutral SFT tax at 4B ($-$0.13pp). At 8B, RSFT compresses the tax magnitude relative to SFT ($-$0.91$\pm$0.74pp, three-seed mean, vs.\ SFT $-$1.71pp). At 14B, the two-seed mean tax is +0.43$\pm$0.49pp (s42: +0.77pp, s43: +0.08pp), reversing sign relative to dev ($-$4.54pp); the small test magnitude and high inter-seed variance may reflect noise or evaluation protocol differences given the 2.82$\times$ annotation density gap between dev and test. LLaMA-3.1-8B shows partial compression from SFT ($-$4.94pp $\to$ $-$1.46$\pm$0.40pp, two-seed mean).
267	
268	\begin{table}[t]
269	\centering
270	\caption{RSFT inference-time evidence tax on Re-DocRED test set (Ign-F1 \%). Tax $=$ no-evi $-$ with-evi; positive $=$ cost. All results use s42.}
271	\label{tab:rsft_test_tax}
272	\small
273	\resizebox{\columnwidth}{!}{%
274	\begin{tabular}{lccc}
275	\toprule
276	\textbf{Model} & \textbf{RSFT w/ evi} & \textbf{RSFT no-evi} & \textbf{RSFT Tax} \\
277	\midrule
278	Qwen3-1.7B & 29.33 & 23.90 & $-$5.43$^\ddagger$ \\
279	Qwen3-4B & 25.01 & 26.52 & +1.51 \\
280	Qwen3-8B & 33.53 & 33.19 & $-$0.34 \\
281	Qwen3-14B & 38.49 & 39.26 & +0.77$^\dagger$ \\
282	LLaMA-3.1-8B & 35.54 & 33.80 & $-$1.74 \\
283	\bottomrule
284	\end{tabular}%
285	}
286	\vspace{-2mm}
287	{\raggedright\footnotesize $^\ddagger$1.7B no-evi truncation rate is 94.8\% (vs.\ 73.8\% with-evi), which may amplify the tax magnitude. $^\dagger$14B shows a dev-test reversal (dev tax $= -$4.54pp); the two-seed test mean (+0.43$\pm$0.49pp) is small relative to inter-seed variance (CI crosses zero), suggesting the direction signal is noise-dominated at this magnitude. All other scales preserve dev-test direction consistency.\par}
288	\end{table}
289	
290	\paragraph{Comparison to supervised methods.}
291	Table~\ref{tab:encoder_comparison} directly compares encoder-based methods with our LLM-based approach. Encoder methods achieve substantially higher extraction performance (Rel-F1 63--65 vs.\ our 45--56), reflecting decades of architecture-specific optimization for the classification formulation. However, their evidence identification operates as binary sentence classification, producing Evi-F1 of 52--56 under a joint evaluation protocol. Our TP-only Evi-F1 exceeds 80\%, indicating that when the model correctly identifies a triple, it produces higher-quality evidence than encoder methods. The joint Evi-F1 gap (36.1 vs.\ 54.15) is driven primarily by extraction performance rather than evidence quality: false-positive and false-negative triples dilute the denominator. The substantial extraction gap (16--18pp Ign-F1) reflects the current limitation of generative LLM approaches relative to specialized encoder models. Closing this gap requires improving extraction capability of LLM-based methods, an orthogonal direction to the evidence faithfulness problem we address.
292	
293	\begin{table}[t]
294	\centering
295	\caption{Comparison with encoder-based methods on DocRED dev set. Encoder methods use RoBERTa-large; LLM methods use Qwen3. Evi-F1 for encoder methods uses joint evaluation (all triples in denominator); our joint Evi-F1 follows the same protocol for fair comparison. TP-only Evi-F1 conditions on correctly predicted triples. Rel-F1 is reported in percentage for all methods.}
296	\label{tab:encoder_comparison}
297	\small
298	\resizebox{\columnwidth}{!}{%
299	\begin{tabular}{llcccc}
300	\toprule
301	\textbf{Method} & \textbf{Type} & \textbf{Ign-F1} & \textbf{Rel-F1} & \textbf{Evi-F1 (joint)} & \textbf{Evi-F1 (TP)} \\
302	\midrule
303	ATLOP & Encoder & 61.32 & 63.18 & -- & -- \\
304	EIDER & Encoder & 62.34 & 64.27 & 52.54 & -- \\
305	SAIS & Encoder & 62.23 & 65.17 & 55.84 & -- \\
306	DREEAM & Encoder & 61.71 & 63.49 & 54.15 & -- \\
307	\midrule
308	Ours (4B RSFT) & LLM & 44.82 & 45.80 & 36.1 & 80.96 \\
309	Ours (8B RSFT) & LLM & 54.33 & 56.07 & -- & 81.26 \\
310	Ours (14B RSFT) & LLM & 58.86 & 60.09 & 48.59 & 83.92 \\
311	\bottomrule
312	\end{tabular}%
313	}
314	\end{table}
315	
316	
317	\section{Decoupling Spectrum Data}
318	\label{sec:spectrum_data}
319	
320	\begin{table}[t]
321	\centering
322	\caption{Evidence-extraction decoupling across RL paradigms (Qwen3-4B). Severity indicates the degree of extraction collapse relative to evidence improvement.}
323	\label{tab:spectrum}
324	\small
325	\resizebox{\columnwidth}{!}{%
326	\begin{tabular}{llcccc}
327	\toprule
328	\textbf{Paradigm} & \textbf{Config} & \textbf{Rel-F1} & \textbf{Evi-F1} & \textbf{EDCR} & \textbf{Severity} \\
329	\midrule
330	GRPO & QLoRA $G{=}4$ & 1.38 & 85.04 & 0.9876 & Catastrophic \\
331	GRPO & bf16 $G{=}8$ & 45.49 & 80.86 & 0.6318 & Mild \\
332	DPO & bf16 1ep & 33.37 & 80.90 & 0.8123 & Gradual \\
333	DPO & bf16 3ep & 31.45 & 84.84 & 0.7503 & Gradual \\
334	\midrule
335	SFT & baseline$^\ddagger$ & 44.39 & 79.61 & 0.6797 & None \\
336	RSFT & CED$^\ddagger$ & 45.80 & 80.96 & 0.6487 & None \\
337	\bottomrule
338	\end{tabular}%
339	}
340	\vspace{-2mm}
341	{\raggedright\footnotesize $^\ddagger$Three-seed mean. DPO rows evaluated at \texttt{max\_new\_tokens}$=$2048 (matched protocol); all other rows at 1024. Severity reflects training trajectory stability (propensity for extraction collapse during optimization), not the final-checkpoint EDCR value.\par}
342	\end{table}
343	
344	
345	\section{GRPO Training Dynamics}
346	\label{sec:grpo_dynamics}
347	
348	\begin{figure*}[t]
349	\centering
350	\includegraphics[width=\linewidth]{fig_grpo_dynamics.pdf}
351	\caption{Training dynamics of GRPO under different configurations. (a)~Relation F1 across checkpoints: G=4 QLoRA suffers catastrophic collapse at step~10, while G=8 bf16 remains stable. (b)~Evidence F1 stays intact for G=8 bf16, confirming the generation mechanism itself does not fail. (c)~Evidence-Decoupling Ratio (EDCR) reveals near-total decoupling in G=4 QLoRA (extraction collapses to Rel-F1 1.4), while G=8 bf16 maintains healthy ratios.}
352	\label{fig:grpo_dynamics}
353	\end{figure*}
354	
355	
356	\section{Error Analysis: SFT vs.\ RSFT}
357	\label{sec:error_analysis}
358	
359	Table~\ref{tab:error_analysis} decomposes the extraction improvements from RSFT into error categories across three scales. Three mechanisms drive the gains consistently:
360	
361	\paragraph{Truncation false negatives.} SFT models frequently hit the generation length limit, producing incomplete outputs that miss triples. RSFT training on compact, high-quality outputs reduces this truncation rate. The effect is strongest at 1.7B ($-841$ truncation FN, $-22$\%), where the SFT model's output length is least controlled.
362	
363	\paragraph{Hallucinated false positives.} CED-based filtering removes training examples with unfaithful predictions, reducing the rate of hallucinated triples at inference. LLaMA benefits most ($-593$ hallucinated FP, $-11.8$\%), suggesting cross-architecture variation in hallucination susceptibility.
364	
365	\paragraph{Duplicate predictions.} RSFT training data, selected for quality, contains fewer repetitive patterns. This propagates to inference, reducing duplicate triples by $11$--$20$\% across scales, with 1.7B showing the largest reduction ($-20.2$\%).
366	
367	\paragraph{Evidence quality unchanged.} Despite substantial extraction improvements, evidence exact-match F1 changes by less than 0.4pp at every scale. RSFT selects for joint extraction-evidence quality, but the evidence signal in CED scoring does not translate into measurable evidence improvement. This suggests that evidence grounding requires targeted optimization (e.g., evidence-specific rewards in RL) rather than data selection alone.
368	
369	\paragraph{Residual difficulty.} The proportion of ``other'' false negatives (triples missed for reasons beyond truncation or formatting) increases by 13--15\% in relative terms after RSFT. As easy errors (truncation, duplication) are eliminated, the remaining error distribution shifts toward harder cases: cross-sentence reasoning, implicit relations, and long-tail entity pairs. The relation types with the largest RSFT gains (participant, conflict, league, screenwriter, operator, contains\_administrative\_territory) involve cross-sentence reasoning or long-tail entities, consistent with RSFT's selection pressure toward diverse, high-quality outputs.
370	
371	\begin{table}[t]
372	\centering
373	\caption{Error pattern changes from SFT to RSFT across scales. $\Delta$\% shows relative change. Truncation FN, hallucinated FP, and duplicates all decrease; evidence quality and residual FN difficulty are unchanged.}
374	\label{tab:error_analysis}
375	\small
376	\resizebox{\columnwidth}{!}{%
377	\begin{tabular}{llccc}
378	\toprule
379	\textbf{Error Category} & \textbf{Direction} & \textbf{1.7B} & \textbf{4B} & \textbf{8B / LLaMA} \\
380	\midrule
381	Truncation FN & $\downarrow$ & $-$22\% & $-$16\% & $-$18\% \\
382	Hallucinated FP & $\downarrow$ & $-$8\% & $-$6\% & $-$12\% \\
383	Duplicates & $\downarrow$ & $-$20\% & $-$11\% & $-$14\% \\
384	Evidence (exact) & $\approx$ & $<$0.4pp & $<$0.4pp & $<$0.4pp \\
385	FN: other & $\uparrow$ & +13\% & +15\% & +14\% \\
386	\bottomrule
387	\end{tabular}%
388	}
389	\end{table}
390	
391	
392	\section{Per-Relation EDCR Distribution}
393	\label{sec:edcr_per_relation}
394	
395	Computing EDCR for each of the 76 relation types with $\geq$5 evaluation samples (from the RSFT CED s42 model) reveals that per-relation EDCR correlates strongly with per-relation Rel-F1 ($\rho = -0.79$, $n = 76$, $p < 0.001$), confirming its utility as a difficulty indicator. Filtering to types with $\geq$5 predictions strengthens the correlation ($\rho = -0.85$, $n = 74$, $p < 0.001$). Per-relation EDCR is statistically independent of Evi-F1 ($\rho = -0.06$, $p = 0.58$), and Evi-F1 itself shows no association with Rel-F1 ($\rho = -0.01$, $p = 0.91$). These null correlations establish that evidence quality and extraction ability are fully decoupled across relation types. Extreme cases illustrate the diagnostic power: \texttt{date\_of\_birth} has EDCR $= 0.118$ (highly faithful, with extraction and evidence tightly coupled), while \texttt{head\_of\_government} reaches $0.956$ (highly decoupled). This per-relation analysis avoids the shared-component concern present in cross-method EDCR-vs-Rel-F1 correlation, providing independent validation of EDCR's diagnostic utility. A permutation test (10,000 iterations) on the per-relation correlation yields $p < 0.0001$, confirming that the association is not an artifact of the shared TP component.
396	
397	\paragraph{Partial correlations controlling for TP.}
398	Because EDCR shares TP (true positives) in both numerator and denominator with Rel-F1, we report partial correlations controlling for Evi-Recall$_\text{TP}$. At the cross-method level ($n = 17$ seed-specific configurations), the partial Spearman $\rho = -0.8541$ ($p = 0.000025$), virtually unchanged from the raw $\rho = -0.8554$ (0.15\% reduction). Removing the GRPO QLoRA outlier yields partial $\rho = -0.8681$ ($n = 16$, $p = 0.000027$). Aggregating to $n = 7$ unique methods: raw $\rho = -0.9643$, partial $\rho = -0.9617$. These results confirm that the EDCR--Rel-F1 association is not driven by the shared TP component. Note that seed-level configurations ($n = 17$) are not fully independent; the $n = 7$ unique-method analysis provides a conservative estimate.
399	
400	\paragraph{Similar-TP, different-EDCR pairs.}
401	To further validate that EDCR captures information beyond what TP alone provides, we identify configuration pairs with similar Evi-Recall$_\text{TP}$ ($|\Delta| < 5$pp) but substantially different EDCR ($|\Delta| > 5$pp). Forty-eight such pairs exist across all configurations. The most illustrative: DPO-CED 1-epoch (Evi-Recall$_\text{TP} = 0.833$) vs.\ RSFT CED LLaMA s43 (Evi-Recall$_\text{TP} = 0.829$) differ by only 2.4pp in TP-conditioned evidence recall but 13.6pp in EDCR, reflecting the substantial extraction gap between these methods. This pattern demonstrates that EDCR captures extraction-evidence alignment that aggregate TP metrics miss.
402	
403	\begin{figure}[t]
404	\centering
405	\includegraphics[width=\linewidth]{fig_edcr_relations.pdf}
406	\caption{Per-relation EDCR distribution across all 93 relation types observed in the development set (of 96 defined in DocRED). The correlation analysis in the text uses the 76 types with $\geq$5 samples for statistical reliability. Red bars indicate EDCR $\geq$ 0.70 (severe decoupling), green bars indicate EDCR $<$ 0.30 (healthy evidence grounding). Seven types exhibit EDCR = 1.0.}
407	\label{fig:edcr_relations}
408	\end{figure}
409	
410	
411	\section{Qualitative Analysis}
412	\label{sec:qualitative}
413	
414	We present representative examples illustrating three phenomena: evidence quality differences between SFT and RSFT, GRPO format gaming under catastrophic collapse, and per-relation EDCR diagnostics.
415	
416	\paragraph{Case 1: Evidence quality.}
417	Table~\ref{tab:case_evidence} compares evidence citations from SFT and RSFT on three documents. SFT tends to cite many sentences indiscriminately, including distractors unrelated to the target triple, while RSFT selects precisely the gold evidence sentences. For \emph{America's Sweetheart}, SFT cites 6 sentences (precision 0.17) whereas RSFT cites only the single correct sentence (precision 1.00). The pattern is consistent: SFT achieves evidence precision of 0.00--0.20 across these examples, while RSFT achieves 1.00 in all three cases.
418	
419	\begin{table}[t]
420	\centering
421	\caption{Evidence citation comparison between SFT and RSFT. Precision measures the fraction of cited sentences that match gold evidence.}
422	\label{tab:case_evidence}
423	\small
424	\resizebox{\columnwidth}{!}{%
425	\begin{tabular}{llccc}
426	\toprule
427	\textbf{Document} & \textbf{Triple} & \textbf{SFT Prec.} & \textbf{RSFT Prec.} & \textbf{SFT \#Cited} \\
428	\midrule
429	Oleg Tinkov & (Oleg Tinkov, country of citizenship, Russia) & 0.00 & 1.00 & 3 \\
430	America's Sweetheart & (record label, country, United States) & 0.17 & 1.00 & 6 \\
431	Jade (Mortal Kombat) & (Jade, present in work, Mortal Kombat) & 0.20 & 1.00 & 5 \\
432	\bottomrule
433	\end{tabular}%
434	}
435	\end{table}
436	
437	\paragraph{Case 2: GRPO format gaming.}
438	Under catastrophic collapse (GRPO QLoRA $G{=}4$), the model abandons the DocRED 96-type relation ontology and generates free-text relation labels. On the document \emph{Something to Believe In}, the model produces 35 predicted triples with relations such as ``is a'', ``honor'', and ``location'', none of which belong to the target ontology. All 35 predictions are incorrect. Similarly, for \emph{J\'{o}zef Pi\l{}sudski Monument}, 28 predictions use non-standard relations with 0 correct matches. The model retains the structural format of triple-with-evidence output but fills it with fabricated relation types. The model produces well-formed evidence for these non-existent relations.
439	
440	\paragraph{Case 3: EDCR diagnostics.}
441	Per-relation EDCR identifies specific relation types where extraction and evidence are misaligned. For \texttt{date\_of\_birth} (EDCR $= 0.118$), the model's evidence consistently matches gold annotations: both extraction and evidence point to the same biographical sentence. In contrast, \texttt{notable\_work} (EDCR $= 0.941$) exhibits severe decoupling: the model cites sentence [0] (a general introduction) instead of the gold evidence sentence [3] (which contains the actual work attribution). High-EDCR relations tend to involve indirect or multi-hop reasoning where surface-level context misleads the evidence generator.
442	
443	
444	\section{Use of AI Assistants}
445	\label{app:ai-assistants}
446	
447	We used Claude (Anthropic) as an AI coding and writing assistant
448	throughout this work. Specifically:
449	\begin{itemize}
450	    \item \textbf{Code:} drafting experiment scripts, data-processing
451	    pipelines, and analysis utilities; debugging and refactoring.
452	    \item \textbf{Writing:} drafting and revising paper sections,
453	    polishing prose, and reformatting LaTeX.
454	    \item \textbf{Literature:} summarizing related papers to inform
455	    the related-work section.
456	\end{itemize}
457	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7cddcce9-5c4a-43e0-937a-f24636f0993c",
  "isSidechain": false,
  "promptId": "659f4775-47ec-4bb9-8db5-86432609ca56",
  "type": "user",
  "uuid": "95b55ac0-b8f4-41c7-855a-ddd005bac453",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/appendix.tex",
      "content": "\\section{Training Hyperparameters}\n\\label{sec:hyperparams}\n\nTable~\\ref{tab:hyperparams} lists the hyperparameters for all training configurations. All methods use LoRA with rank $r{=}64$ and $\\alpha{=}128$ applied to all linear projections (attention and feed-forward). SFT and RSFT share the same optimizer settings; RSFT differs only in data construction (top-1 CED-selected outputs from $N{=}8$ candidates). GRPO and DPO use lower learning rates to stabilize post-SFT optimization.\n\n\\begin{table*}[t]\n\\centering\n\\caption{Training hyperparameters for all optimization paradigms. All experiments use Qwen3-4B as the base model with LoRA adaptation. A dash indicates that the parameter is not applicable to the given method.}\n\\label{tab:hyperparams}\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{Parameter} & \\textbf{SFT} & \\textbf{RSFT} & \\textbf{GRPO QLoRA} & \\textbf{GRPO bf16} & \\textbf{DPO} \\\\\n\\midrule\nBase model & Qwen3-4B & Qwen3-4B & Qwen3-4B & Qwen3-4B & Qwen3-4B \\\\\nLoRA rank $r$ & 64 & 64 & 64 & 64 & 64 \\\\\nLoRA $\\alpha$ & 128 & 128 & 128 & 128 & 128 \\\\\nLearning rate & 2e-5 & 2e-5 & 5e-6 & 5e-6 & 5e-7 \\\\\nBatch size (effective) & 16 & 16 & 4 & 8 & 4 \\\\\nEpochs & 3 & 3 & -- & -- & 1, 3\\textsuperscript{$\\star$} \\\\\nMax steps & -- & -- & 100 & 100 & -- \\\\\nGradient accumulation & 4 & 4 & 16 & 4 & 4 \\\\\nMax new tokens & 1024 & 1024 & 1024 & 1024 & 1024 \\\\\nQuantization & -- & -- & NF4 4-bit & bf16 & bf16 \\\\\nGroup size $G$ & -- & -- & 4 & 8 & -- \\\\\nKL coefficient & -- & -- & 0.01 & 0.01 & -- \\\\\n$\\beta$ (DPO) & -- & -- & -- & -- & 0.1 \\\\\nCandidates $N$ & -- & 8 & -- & -- & 8 \\\\\nTop-$k$ selection & -- & 1 & -- & -- & -- \\\\\nTraining samples & 3,053 & 2,718 & 3,053 & 3,053 & 3,053 \\\\\nScoring function & -- & CED & CED & CED & CED \\\\\n\\bottomrule\n\\end{tabular}\n\\vspace{1mm}\n{\\raggedright\\footnotesize \\textsuperscript{$\\star$}DPO is trained for both 1 and 3 epochs to observe temporal dynamics of the evidence-extraction trade-off (Section~\\ref{sec:spectrum}).\\par}\n\\end{table*}\n\n\n\\section{Full Ablation Results}\n\\label{sec:ablation_full}\n\nTable~\\ref{tab:ablation_full} reports the complete RSFT ablation across scoring functions, top-$k$ values, and random seeds. RSFT CED $k{=}1$ achieves a four-seed mean Ign-F1 of 44.66 (standard deviation 0.49), confirming robust improvement over the SFT s42 baseline (39.74). The three-seed mean reported in Table~\\ref{tab:main} (44.82, seeds 42/43/44) is slightly higher because it excludes the lowest seed (s45: 44.16). Random selection RSFT $k{=}1$ (41.14 Ign-F1), which samples from the same candidate pool without CED scoring, improves only +1.40pp over SFT s42 versus +4.92pp for CED RSFT, confirming that CED scoring precision drives the majority of the RSFT gain. Increasing $k$ to 3 slightly degrades performance (43.64 Ign-F1), consistent with the intuition that stricter selection yields higher-quality training data. The flat-NLI scoring variant produces comparable Rel-F1 (mean 45.61 vs.\\ 45.63 for CED, a difference of 0.02pp). Both CED and flat-NLI improve substantially over the SFT baseline while maintaining or improving Evi-F1, confirming that the RSFT gains are driven by quality-based data selection rather than by the specific contrastive formulation.\n\n\\paragraph{NLI scoring comparison.} Across all available seeds, CED RSFT achieves mean Rel-F1 of 45.63 (seeds 42, 43, 44, 45: range 45.14--46.21), and flat-NLI RSFT achieves mean Rel-F1 of 45.61 (seeds 42, 43: range 45.35--45.86). The 0.02pp difference suggests comparable performance: CED's contrastive design does not substantially outperform simpler NLI scoring for RSFT data selection. We adopt CED as the default because its contrastive formulation produces per-triple discrimination scores that support interpretable error analysis.\n\n\\paragraph{Top-$k$ selection.} Best-of-8 ($k{=}1$) yields mean Ign-F1 44.66 and Rel-F1 45.63, while top-3-of-8 ($k{=}3$) produces 43.64 and 44.54. The selected training data confirms the quality gap: $k{=}1$ data has mean extraction F1 of 61.57 and mean CED of 0.6683, versus 57.61 and 0.6205 for $k{=}3$. Despite $k{=}3$ providing 2.96$\\times$ more training examples, the additional lower-ranked samples introduce noise that degrades final performance.\n\n\\paragraph{NLI scorer capacity.} CED filtering is robust to NLI model capacity: replacing the default scorer (DeBERTa-v3-base, 86M parameters) with DeBERTa-v3-large (304M) yields only +1.10pp Ign-F1 (45.33 vs.\\ 44.23, s42), a difference within the v3-base seed noise of 0.88pp (s42: 44.23, s44: 45.11). Other metrics confirm the pattern: Rel-F1 improves by +1.19pp (46.36 vs.\\ 45.17), Evi-F1 by +0.20pp (81.94 vs.\\ 81.74), while EDCR shifts by $-$0.39pp (0.6530 vs.\\ 0.6569)---the inconsistent direction across metrics rules out systematic improvement from a larger scorer. This insensitivity supports v3-base as a cost-effective default, as a 3.5$\\times$ larger scorer does not materially improve CED-based data selection.\n\n\\begin{table}[t]\n\\centering\n\\caption{Full RSFT ablation on DocRED dev set (Qwen3-4B). CED and flat-NLI denote the scoring function used for candidate selection. Best Ign-F1 among evidence-generating methods in \\textbf{bold}.}\n\\label{tab:ablation_full}\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Configuration} & \\textbf{Ign-F1} & \\textbf{Rel-F1} & \\textbf{Evi-F1} & \\textbf{EDCR} \\\\\n\\midrule\nSFT baseline (s42) & 39.74 & 40.49 & 79.86 & 0.6982 \\\\\nSFT no-evidence & \\textbf{47.21} & 48.76 & -- & -- \\\\\n\\midrule\nRSFT random $k{=}1$ & 41.14 & 41.98 & 79.64 & 0.6971 \\\\\n\\midrule\nRSFT CED $k{=}1$ (s42) & 44.23 & 45.17 & 81.74 & 0.6569 \\\\\nRSFT CED $k{=}1$ (s43) & 45.12 & 46.01 & 80.63 & 0.6542 \\\\\nRSFT CED $k{=}1$ (s44) & 45.11 & 46.21 & 80.50 & 0.6350 \\\\\nRSFT CED $k{=}1$ (s45) & 44.16 & 45.14 & 81.74 & 0.6550 \\\\\nRSFT CED $k{=}1$ (mean) & 44.66 & 45.63 & 81.15 & 0.6503 \\\\\n\\midrule\nRSFT CED $k{=}3$ & 43.64 & 44.54 & 80.88 & 0.6635 \\\\\n\\midrule\nRSFT flat-NLI (s42) & -- & 45.35 & 80.43 & 0.6431 \\\\\nRSFT flat-NLI (s43) & -- & 45.86 & 81.58 & 0.6505 \\\\\nRSFT flat-NLI (mean) & -- & 45.61 & 81.01 & 0.6468 \\\\\n\\midrule\nRSFT CED $k{=}1$ v3-large (s42) & 45.33 & 46.36 & 81.94 & 0.6530 \\\\\n\\bottomrule\n\\end{tabular}%\n}\n\\end{table}\n\n\n\\section{Scaling Details}\n\\label{sec:scaling_details}\n\nTable~\\ref{tab:cross_detail} supplements Table~\\ref{tab:scaling} in the main text with per-scale Rel-F1 and Evi-F1 breakdowns. At 1.7B, RSFT improves Rel-F1 from 45.86 to 52.81 (+6.95, multi-seed mean) while achieving Evi-F1 82.63 and EDCR 0.6217. The 4B model shows the same pattern: Rel-F1 increases from 44.39 to 45.80 (+1.41, three-seed mean). For 8B, RSFT brings Rel-F1 from 51.87 to 56.07 (three-seed mean) with Evi-F1 of 81.26 and EDCR 0.6235, confirming tight coupling between extraction and evidence at this scale. At 14B, the SFT baseline already achieves strong Rel-F1 (56.11) and Evi-F1 (82.92).\n\n\\begin{table}[t]\n\\centering\n\\caption{Detailed Rel-F1 and Evi-F1 across model scales on DocRED dev set. SFT and RSFT columns show multi-seed means where available (Qwen3 1.7B/4B/8B: 3-seed; 14B: single seed; LLaMA SFT Rel-F1/Evi-F1: s42 only; LLaMA RSFT: 3-seed).}\n\\label{tab:cross_detail}\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{Model} & \\textbf{SFT Rel-F1} & \\textbf{SFT Evi-F1} & \\textbf{RSFT Rel-F1} & \\textbf{RSFT Evi-F1} & \\textbf{RSFT EDCR} \\\\\n\\midrule\nQwen3-1.7B & 45.86 & 82.85 & 52.81 & 82.63 & 0.6217 \\\\\nQwen3-4B & 44.39 & 79.61 & 45.80 & 80.96 & 0.6487 \\\\\nQwen3-8B & 51.87 & 82.94 & 56.07 & 81.26 & 0.6235 \\\\\nQwen3-14B & 56.11 & 82.92 & -- & -- & -- \\\\\nLLaMA-3.1-8B & 55.14 & 81.51 & 57.75 & 82.84 & 0.5804 \\\\\n\\bottomrule\n\\end{tabular}%\n}\n\\end{table}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig_scaling.pdf}\n\\caption{Evidence tax across model scales. Bar heights show Ign-F1 for each training configuration. The gap between no-evidence and SFT bars reverses direction between 1.7B and 4B, revealing the scale-dependent nature of the evidence tax. RSFT consistently narrows the gap toward the no-evidence upper bound.}\n\\label{fig:scaling}\n\\end{figure}\n\n\n\\section{Variance Compression Confidence Intervals}\n\\label{sec:variance_ci}\n\nTable~\\ref{tab:variance_ci} reports 95\\% confidence intervals for SFT and RSFT standard deviations using the $\\chi^2$ distribution ($N{=}3$ seeds per configuration). At 1.7B, the confidence intervals are fully non-overlapping (SFT lower bound 1.45pp $>$ RSFT upper bound 0.54pp), providing the strongest evidence for variance compression. At the remaining three scales, intervals overlap but point estimates are consistently in the same direction (SFT std $>$ RSFT std at all four scales; sign test $p = 0.0625$, one-sided binomial, $n = 4$, underpowered). Cohen's $d$ ranges from 0.46 (4B) to 3.31 (1.7B), with 1.7B and LLaMA-8B showing large effect sizes ($d > 2.5$).\n\n\\begin{table}[t]\n\\centering\n\\caption{95\\% confidence intervals for training variance ($\\chi^2$ method, $N{=}3$ seeds). Compression is the ratio of SFT to RSFT point estimates (unrounded).}\n\\label{tab:variance_ci}\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcccccc}\n\\toprule\n\\textbf{Scale} & \\textbf{SFT std} & \\textbf{SFT 95\\% CI} & \\textbf{RSFT std} & \\textbf{RSFT 95\\% CI} & \\textbf{Compr.} & \\textbf{Cohen's $d$} \\\\\n\\midrule\nQwen3-1.7B & 2.79 & [1.45, 17.55] & 0.09 & [0.04, 0.54] & 32.6$\\times$ & 3.31 \\\\\nQwen3-4B & 3.80 & [1.98, 23.89] & 0.51 & [0.27, 3.21] & 7.5$\\times$ & 0.46 \\\\\nQwen3-8B & 3.23 & [1.68, 20.31] & 0.50 & [0.26, 3.15] & 6.5$\\times$ & 1.79 \\\\\nLLaMA-3.1-8B & 2.92 & [1.52, 18.37] & 0.64 & [0.33, 4.01] & 4.6$\\times$ & 2.58 \\\\\n\\bottomrule\n\\end{tabular}%\n}\n\\vspace{-2mm}\n{\\raggedright\\footnotesize Sign test: $p = 0.0625$ (one-sided binomial, $n = 4$; underpowered). The consistent direction (4/4 SFT $>$ RSFT), non-overlapping CIs at 1.7B, and large Cohen's $d$ at 1.7B and LLaMA provide practical evidence for variance compression despite limited statistical power from $N{=}3$ seeds.\\par}\n\\end{table}\n\n\n\\section{Controlled Evaluation Subset}\n\\label{sec:fair_subset}\n\nThe 1.7B evidence tax comparison (\\S\\ref{sec:scaling}) is confounded by differential truncation rates. At \\texttt{max\\_new\\_tokens}$=$1024, the no-evidence model truncates 50.9\\% of outputs (501/985 documents) versus 31.9\\% (314/985) for the evidence model. To address this, we adopt a matched@2048 fair evaluation: both configurations are evaluated at \\texttt{max\\_new\\_tokens}$=$2048, and the tax is computed on the intersection of documents where both produce format-compliant output. This yields 971/985 fair-subset documents, with a tax of $-$5.63pp (s42), confirming a genuine 1.7B evidence benefit. As additional validation, a stricter controlled subset at @1024 (excluding truncated or repetitive outputs; 442/985 documents) yields $-$6.2pp, with the stronger benefit attributable to the more aggressive filtering.\n\nTable~\\ref{tab:mechanistic} provides a mechanistic breakdown across three scales (evaluated at @1024). Output duplication rate (fraction of documents containing $\\geq$3 repeated triples or unique/total $< 0.5$) declines monotonically with scale for both training configurations, but the gap between no-evidence and with-evidence models narrows from 27.5pp at 1.7B to 3.7pp at 8B. This pattern supports the implicit regularization hypothesis: evidence generation forces smaller models to attend to supporting context, reducing degenerate repetition. At 4B, duplication is already moderate (31.1\\% with evidence), so the regularization benefit diminishes; under matched@2048 evaluation, the 4B training-time tax is approximately neutral (+0.25$\\pm$0.47pp, three-seed mean). The truncation asymmetry reverses across scales: at 1.7B the no-evidence model truncates 19pp more often; at 8B the evidence model truncates 9pp more often due to the longer output format.\n\n\\begin{table}[t]\n\\centering\n\\caption{Mechanistic breakdown of output quality across scales. Duplication rate: fraction of documents with degenerate outputs. Truncation $\\Delta$: no-evidence rate minus with-evidence rate (positive means no-evidence truncates more).}\n\\label{tab:mechanistic}\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\n& \\multicolumn{3}{c}{\\textbf{Duplication Rate}} & \\multicolumn{2}{c}{\\textbf{Truncation}} \\\\\n\\cmidrule(lr){2-4} \\cmidrule(lr){5-6}\n\\textbf{Scale} & \\textbf{w/ evi} & \\textbf{no-evi} & \\textbf{Gap} & \\textbf{$\\Delta$} & \\textbf{Pattern} \\\\\n\\midrule\n1.7B & 33.0 & 60.5 & 27.5 & +19 & no-evi worse \\\\\n4B & 31.1 & 43.2 & 12.1 & +2 & neutral \\\\\n8B & 29.2 & 32.9 & 3.7 & $-$9 & evi worse \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n\\section{Training-Time Evidence Tax}\n\\label{sec:training_tax}\n\nThe evidence tax can be measured in two ways. The \\emph{training-time} tax compares separately trained models (SFT with evidence vs.\\ SFT without evidence in the training output format). The \\emph{inference-time} tax (reported in Table~\\ref{tab:scaling}) evaluates the same RSFT model with and without evidence at inference time.\n\nNa\\\"ive comparisons at \\texttt{max\\_new\\_tokens}$=$1024 are confounded by differential truncation rates (e.g., 50.9\\% vs.\\ 31.9\\% at 1.7B). To control for this, we adopt a \\emph{matched@2048 fair evaluation}: both configurations are evaluated at \\texttt{max\\_new\\_tokens}$=$2048, and the tax is computed on the intersection of documents where both models produce format-compliant output. Table~\\ref{tab:training_tax} reports the matched@2048 training-time tax across Qwen3 scales.\n\nThe tax reveals a within-family capacity threshold: evidence generation benefits 1.7B ($-$5.63pp on 971/985 fair-subset documents) but is approximately neutral at $\\geq$4B (+0.25$\\pm$0.47pp at 4B across three seeds, +0.04pp at 8B, +0.03pp at 14B). At 1.7B, s42 is the strongest SFT seed (47.86 Ign-F1, +3.22pp above the three-seed mean of 44.64), so the benefit may be amplified relative to the population mean. LLaMA-3.1-8B SFT training-time tax is consistently negative but with high magnitude variance ($-$1.53 to $-$11.20pp, mean $-$5.19$\\pm$5.25pp under matched@2048) and omitted from the table due to the s43 outlier (16.3\\% no-evidence format failure inflates its tax); cross-architecture patterns are addressed in \\S\\ref{sec:generalization_full}.\n\n\\begin{table}[t]\n\\centering\n\\caption{Training-time evidence tax under matched@2048 fair evaluation (DocRED dev Ign-F1). Both configurations evaluated at \\texttt{max\\_new\\_tokens}$=$2048; tax computed on format-compliant intersection. Tax $=$ no-evidence $-$ with-evidence; positive $=$ cost.}\n\\label{tab:training_tax}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Model} & \\textbf{Fair w/ evi} & \\textbf{Fair no-evi} & \\textbf{Evi Tax} & \\textbf{Subset} \\\\\n\\midrule\nQwen3-1.7B & 48.38 & 42.75 & $-$5.63 & 971 \\\\\nQwen3-4B & -- & -- & +0.25{\\scriptsize$\\pm$0.47}$^{(3)}$ & $\\geq$982 \\\\\nQwen3-8B & 50.15 & 50.19 & +0.04 & 984 \\\\\nQwen3-14B & 55.07 & 55.10 & +0.03 & 985$^\\dagger$ \\\\\n\\bottomrule\n\\end{tabular}\n\\vspace{-2mm}\n{\\raggedright\\footnotesize 1.7B and 8B are s42; 4B reports three-seed mean $\\pm$ std (per-seed range: $-$0.19 to +0.73pp); 14B evaluated at @1024 with 0\\% truncation for both configurations ($^\\dagger$fair subset equals full dev set). Subset: documents in format-compliant intersection out of 985.\\par}\n\\end{table}\n\n\\paragraph{Evidence training and SFT seed variance.}\nEvidence training's effect on SFT seed variance is also scale-dependent. At 4B, with-evidence SFT models show near-identical cross-seed spread (0.02pp) compared to no-evidence models (0.50pp), yielding 25$\\times$ variance compression. At 8B, the compression is more modest (0.35pp vs.\\ 0.48pp, 1.4$\\times$). However, at 1.7B the pattern reverses: with-evidence seed spread (0.63pp) exceeds no-evidence spread (0.20pp). This reversal likely reflects the extreme truncation rates at 1.7B (75.6\\% with-evidence, 94.4\\% no-evidence at \\texttt{max\\_new\\_tokens}$=$1024): truncated outputs produce noisy extraction results whose variance depends on which triples appear before the cutoff point. The RSFT variance compression reported in \\S\\ref{sec:scaling} is measured relative to SFT with-evidence baselines and holds at all scales regardless of this SFT-internal pattern.\n\n\n\\section{Why RSFT Avoids Decoupling}\n\\label{sec:rsft_theory}\n\nThe structural difference between selection and optimization explains why RSFT does not exhibit the decoupling observed in gradient-based methods. GRPO and DPO update model parameters through gradients that optimize a reward signal. When two sub-tasks (extraction and evidence) compete for gradient capacity, the optimizer can discover and exploit the trade-off between them, improving one at the expense of the other. RSFT operates differently: it selects complete outputs and trains on them with standard supervised loss. Because the selection is discrete (accept or reject a full response), there is no gradient pathway through which the model can learn to sacrifice extraction for evidence quality. Only outputs where both extraction and evidence are jointly strong survive the CED filter. This property is not specific to RSFT's design but is a structural consequence of discrete selection over complete outputs: any selection-based method that filters on a joint quality criterion will inherit the same coupling guarantee. The implication for practitioners is direct: when optimizing for multiple coupled generation objectives, selection-based methods preserve inter-objective balance that gradient-based methods disrupt.\n\n\n\\section{Full Generalization Results}\n\\label{sec:generalization_full}\n\n\\paragraph{Cross-family transfer.}\nLLaMA-3.1-8B confirms the scaling patterns observed with Qwen3. Its SFT baseline achieves a three-seed mean of 51.09 Ign-F1 (std 2.92pp; s42: 53.84, s43: 51.42, s44: 48.02). Under matched@2048 fair evaluation, the training-time tax is consistently negative across all three seeds (s42: $-$1.53, s43: $-$11.20, s44: $-$2.83; mean $-$5.19$\\pm$5.25pp), indicating that evidence generation consistently benefits LLaMA-3.1-8B. This contrasts with Qwen3-8B's approximately neutral tax (+0.04pp), suggesting that the evidence tax may be architecture-dependent at the 8B scale; however, the high magnitude variance (driven by s43, whose no-evidence configuration has a 16.3\\% format failure rate that inflates the tax estimate) precludes precise quantification. RSFT CED improves LLaMA to a three-seed mean of 56.54 Ign-F1 (std 0.64pp; s42: 57.14, s43: 56.62, s44: 55.87), a +5.45 point gain over SFT mean (51.09), with 4.6$\\times$ variance compression (2.92pp $\\to$ 0.64pp), consistent with the pattern at the 8B scale (Qwen3-8B: +4.14, 6.5$\\times$ compression).\n\n\\paragraph{Cross-dataset robustness.}\nOn Re-DocRED~\\citep{tan2022redocred}, the SFT baseline achieves 36.59 Ign-F1 (Evi-F1 81.70, EDCR 0.6674). RSFT CED improves this to 41.45 Ign-F1 (Evi-F1 81.82, EDCR 0.6210), a +4.86pp gain that closely matches the +5.08pp improvement on DocRED (RSFT three-seed mean minus SFT s42). This consistency across datasets with different annotation protocols confirms that RSFT's benefit generalizes beyond training-set-specific artifacts. Evidence quality remains stable across datasets (Evi-F1 81.82 vs.\\ 81.15 on DocRED), and the EDCR reduction ($-0.046$) mirrors the DocRED pattern, further supporting the robustness of CED-based selection.\n\n\\paragraph{Re-DocRED test set evaluation.}\nTable~\\ref{tab:test_results} reports SFT and RSFT performance on the Re-DocRED test set. We observe a consistent performance gap between dev and test sets, with test Ign-F1 approximately 20 percentage points lower (RSFT: 1.7B 51.2$\\to$29.3, 4B 44.8$\\to$25.0, 8B 54.3$\\to$33.5, 14B 58.9$\\to$38.5, LLaMA-8B 56.5$\\to$35.5; SFT 1.7B: 44.6$\\to$25.8). This gap is attributable to annotation density: the test set contains 34.7 gold triples per document versus 12.3 in the dev set (a 2.82$\\times$ ratio), imposing a harder recall requirement. The gap magnitude is stable across scales and architectures (range: 18.9--21.9pp), and model ranking is perfectly preserved (Spearman $\\rho{=}1.0$), indicating that the absolute drop reflects the test annotation scheme rather than a model-specific deficiency. At 14B, the RSFT advantage observed on dev (+3.79pp) reverses on test ($\\Delta{=}{-}0.37$pp); we note that the SFT model's 50.6\\% truncation rate implies longer outputs that generate more candidate triples to match the test set's dense annotation scheme.\n\n\\begin{table}[t]\n\\centering\n\\caption{SFT and RSFT performance on Re-DocRED test set (Ign-F1 \\%). Dev Ign-F1 (RSFT) from Table~\\ref{tab:scaling}. All test results use s42.}\n\\label{tab:test_results}\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lccccccc}\n\\toprule\n\\textbf{Model} & \\textbf{Dev} & \\textbf{SFT} & \\textbf{RSFT} & \\textbf{$\\Delta$} & \\textbf{Tr. SFT} & \\textbf{Tr. RSFT} & \\textbf{Evi-F1} \\\\\n\\midrule\nQwen3-1.7B & 51.19 & 25.79 & 29.33 & +3.54 & 81.8 & 73.8 & 23.20 \\\\\nQwen3-4B & 44.82$^\\dagger$ & 22.32 & 25.01 & +2.69 & 64.6 & 42.8 & 18.38 \\\\\nQwen3-8B & 54.33 & 31.06 & 33.53 & +2.47 & 82.0 & 1.8 & 25.26 \\\\\nQwen3-14B & 58.86 & 38.86 & 38.49 & $-$0.37 & 50.6 & 13.4 & 26.88 \\\\\nLLaMA-3.1-8B & 56.54 & 34.20 & 35.54 & +1.34 & 65.4 & 56.6 & 25.09 \\\\\n\\bottomrule\n\\end{tabular}%\n}\n\\vspace{-2mm}\n{\\raggedright\\footnotesize $^\\dagger$4B dev Ign-F1 is three-seed mean from original checkpoint; test results use retrained checkpoint (original unavailable for reproduction; retrained v2 achieves comparable dev performance, 43.88 vs.\\ 44.23). $\\Delta$: RSFT $-$ SFT. Evi-F1: RSFT joint (DREEAM protocol). Tr.: truncation rate (\\%). Dev is RSFT three-seed mean from Table~\\ref{tab:scaling}.\\par}\n\\end{table}\n\n\\paragraph{Test-set evidence tax.}\nTable~\\ref{tab:test_tax} reports the evidence tax on the Re-DocRED test set, comparing SFT models trained with and without evidence in the output format. Test-set evaluation confirms the directional pattern observed on development data across all five model configurations: the tax is negative (beneficial) at 1.7B ($-$4.86pp) and LLaMA-8B ($-$4.94pp), and near-neutral at mid-scales ($-$0.13pp at 4B, $-$0.32pp at 14B). The 8B test tax ($-$1.71pp) shows slight variation from its near-neutral dev counterpart (+0.04pp), though both remain modest relative to the 1.7B and LLaMA benefits.\n\n\\begin{table}[t]\n\\centering\n\\caption{Evidence tax on Re-DocRED test set (Ign-F1 \\%). Tax $=$ no-evi $-$ with-evi; negative $=$ benefit. All results use s42. Dev tax from Table~\\ref{tab:training_tax}.}\n\\label{tab:test_tax}\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Model} & \\textbf{With-evi} & \\textbf{No-evi} & \\textbf{Test Tax} & \\textbf{Dev Tax} \\\\\n\\midrule\nQwen3-1.7B & 25.79 & 20.93 & $-$4.86 & $-$5.63 \\\\\nQwen3-4B & 22.32 & 22.19 & $-$0.13 & +0.25 \\\\\nQwen3-8B & 31.06 & 29.35 & $-$1.71 & +0.04 \\\\\nQwen3-14B & 38.86 & 38.54 & $-$0.32 & +0.03 \\\\\nLLaMA-3.1-8B & 34.20 & 29.26 & $-$4.94 & $-$5.19 \\\\\n\\bottomrule\n\\end{tabular}%\n}\n\\end{table}\n\n\\paragraph{RSFT test-set evidence tax.}\nTable~\\ref{tab:rsft_test_tax} reports the inference-time evidence tax for RSFT models on the Re-DocRED test set (same RSFT model evaluated with vs.\\ without evidence output; per-seed s42 values). Figure~\\ref{fig:evidence_tax} presents multi-seed means with error bars where $\\geq$2 seeds are available. At 1.7B, RSFT preserves a strong evidence benefit ($-$5.43pp), comparable to the SFT tax ($-$4.86pp). At 4B, the tax is mildly positive (+1.65$\\pm$0.29pp, three-seed mean; s42: +1.51pp), the Qwen3 scale with the largest positive RSFT test tax; this contrasts with the near-neutral SFT tax at 4B ($-$0.13pp). At 8B, RSFT compresses the tax magnitude relative to SFT ($-$0.91$\\pm$0.74pp, three-seed mean, vs.\\ SFT $-$1.71pp). At 14B, the two-seed mean tax is +0.43$\\pm$0.49pp (s42: +0.77pp, s43: +0.08pp), reversing sign relative to dev ($-$4.54pp); the small test magnitude and high inter-seed variance may reflect noise or evaluation protocol differences given the 2.82$\\times$ annotation density gap between dev and test. LLaMA-3.1-8B shows partial compression from SFT ($-$4.94pp $\\to$ $-$1.46$\\pm$0.40pp, two-seed mean).\n\n\\begin{table}[t]\n\\centering\n\\caption{RSFT inference-time evidence tax on Re-DocRED test set (Ign-F1 \\%). Tax $=$ no-evi $-$ with-evi; positive $=$ cost. All results use s42.}\n\\label{tab:rsft_test_tax}\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Model} & \\textbf{RSFT w/ evi} & \\textbf{RSFT no-evi} & \\textbf{RSFT Tax} \\\\\n\\midrule\nQwen3-1.7B & 29.33 & 23.90 & $-$5.43$^\\ddagger$ \\\\\nQwen3-4B & 25.01 & 26.52 & +1.51 \\\\\nQwen3-8B & 33.53 & 33.19 & $-$0.34 \\\\\nQwen3-14B & 38.49 & 39.26 & +0.77$^\\dagger$ \\\\\nLLaMA-3.1-8B & 35.54 & 33.80 & $-$1.74 \\\\\n\\bottomrule\n\\end{tabular}%\n}\n\\vspace{-2mm}\n{\\raggedright\\footnotesize $^\\ddagger$1.7B no-evi truncation rate is 94.8\\% (vs.\\ 73.8\\% with-evi), which may amplify the tax magnitude. $^\\dagger$14B shows a dev-test reversal (dev tax $= -$4.54pp); the two-seed test mean (+0.43$\\pm$0.49pp) is small relative to inter-seed variance (CI crosses zero), suggesting the direction signal is noise-dominated at this magnitude. All other scales preserve dev-test direction consistency.\\par}\n\\end{table}\n\n\\paragraph{Comparison to supervised methods.}\nTable~\\ref{tab:encoder_comparison} directly compares encoder-based methods with our LLM-based approach. Encoder methods achieve substantially higher extraction performance (Rel-F1 63--65 vs.\\ our 45--56), reflecting decades of architecture-specific optimization for the classification formulation. However, their evidence identification operates as binary sentence classification, producing Evi-F1 of 52--56 under a joint evaluation protocol. Our TP-only Evi-F1 exceeds 80\\%, indicating that when the model correctly identifies a triple, it produces higher-quality evidence than encoder methods. The joint Evi-F1 gap (36.1 vs.\\ 54.15) is driven primarily by extraction performance rather than evidence quality: false-positive and false-negative triples dilute the denominator. The substantial extraction gap (16--18pp Ign-F1) reflects the current limitation of generative LLM approaches relative to specialized encoder models. Closing this gap requires improving extraction capability of LLM-based methods, an orthogonal direction to the evidence faithfulness problem we address.\n\n\\begin{table}[t]\n\\centering\n\\caption{Comparison with encoder-based methods on DocRED dev set. Encoder methods use RoBERTa-large; LLM methods use Qwen3. Evi-F1 for encoder methods uses joint evaluation (all triples in denominator); our joint Evi-F1 follows the same protocol for fair comparison. TP-only Evi-F1 conditions on correctly predicted triples. Rel-F1 is reported in percentage for all methods.}\n\\label{tab:encoder_comparison}\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{Method} & \\textbf{Type} & \\textbf{Ign-F1} & \\textbf{Rel-F1} & \\textbf{Evi-F1 (joint)} & \\textbf{Evi-F1 (TP)} \\\\\n\\midrule\nATLOP & Encoder & 61.32 & 63.18 & -- & -- \\\\\nEIDER & Encoder & 62.34 & 64.27 & 52.54 & -- \\\\\nSAIS & Encoder & 62.23 & 65.17 & 55.84 & -- \\\\\nDREEAM & Encoder & 61.71 & 63.49 & 54.15 & -- \\\\\n\\midrule\nOurs (4B RSFT) & LLM & 44.82 & 45.80 & 36.1 & 80.96 \\\\\nOurs (8B RSFT) & LLM & 54.33 & 56.07 & -- & 81.26 \\\\\nOurs (14B RSFT) & LLM & 58.86 & 60.09 & 48.59 & 83.92 \\\\\n\\bottomrule\n\\end{tabular}%\n}\n\\end{table}\n\n\n\\section{Decoupling Spectrum Data}\n\\label{sec:spectrum_data}\n\n\\begin{table}[t]\n\\centering\n\\caption{Evidence-extraction decoupling across RL paradigms (Qwen3-4B). Severity indicates the degree of extraction collapse relative to evidence improvement.}\n\\label{tab:spectrum}\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{Paradigm} & \\textbf{Config} & \\textbf{Rel-F1} & \\textbf{Evi-F1} & \\textbf{EDCR} & \\textbf{Severity} \\\\\n\\midrule\nGRPO & QLoRA $G{=}4$ & 1.38 & 85.04 & 0.9876 & Catastrophic \\\\\nGRPO & bf16 $G{=}8$ & 45.49 & 80.86 & 0.6318 & Mild \\\\\nDPO & bf16 1ep & 33.37 & 80.90 & 0.8123 & Gradual \\\\\nDPO & bf16 3ep & 31.45 & 84.84 & 0.7503 & Gradual \\\\\n\\midrule\nSFT & baseline$^\\ddagger$ & 44.39 & 79.61 & 0.6797 & None \\\\\nRSFT & CED$^\\ddagger$ & 45.80 & 80.96 & 0.6487 & None \\\\\n\\bottomrule\n\\end{tabular}%\n}\n\\vspace{-2mm}\n{\\raggedright\\footnotesize $^\\ddagger$Three-seed mean. DPO rows evaluated at \\texttt{max\\_new\\_tokens}$=$2048 (matched protocol); all other rows at 1024. Severity reflects training trajectory stability (propensity for extraction collapse during optimization), not the final-checkpoint EDCR value.\\par}\n\\end{table}\n\n\n\\section{GRPO Training Dynamics}\n\\label{sec:grpo_dynamics}\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\linewidth]{fig_grpo_dynamics.pdf}\n\\caption{Training dynamics of GRPO under different configurations. (a)~Relation F1 across checkpoints: G=4 QLoRA suffers catastrophic collapse at step~10, while G=8 bf16 remains stable. (b)~Evidence F1 stays intact for G=8 bf16, confirming the generation mechanism itself does not fail. (c)~Evidence-Decoupling Ratio (EDCR) reveals near-total decoupling in G=4 QLoRA (extraction collapses to Rel-F1 1.4), while G=8 bf16 maintains healthy ratios.}\n\\label{fig:grpo_dynamics}\n\\end{figure*}\n\n\n\\section{Error Analysis: SFT vs.\\ RSFT}\n\\label{sec:error_analysis}\n\nTable~\\ref{tab:error_analysis} decomposes the extraction improvements from RSFT into error categories across three scales. Three mechanisms drive the gains consistently:\n\n\\paragraph{Truncation false negatives.} SFT models frequently hit the generation length limit, producing incomplete outputs that miss triples. RSFT training on compact, high-quality outputs reduces this truncation rate. The effect is strongest at 1.7B ($-841$ truncation FN, $-22$\\%), where the SFT model's output length is least controlled.\n\n\\paragraph{Hallucinated false positives.} CED-based filtering removes training examples with unfaithful predictions, reducing the rate of hallucinated triples at inference. LLaMA benefits most ($-593$ hallucinated FP, $-11.8$\\%), suggesting cross-architecture variation in hallucination susceptibility.\n\n\\paragraph{Duplicate predictions.} RSFT training data, selected for quality, contains fewer repetitive patterns. This propagates to inference, reducing duplicate triples by $11$--$20$\\% across scales, with 1.7B showing the largest reduction ($-20.2$\\%).\n\n\\paragraph{Evidence quality unchanged.} Despite substantial extraction improvements, evidence exact-match F1 changes by less than 0.4pp at every scale. RSFT selects for joint extraction-evidence quality, but the evidence signal in CED scoring does not translate into measurable evidence improvement. This suggests that evidence grounding requires targeted optimization (e.g., evidence-specific rewards in RL) rather than data selection alone.\n\n\\paragraph{Residual difficulty.} The proportion of ``other'' false negatives (triples missed for reasons beyond truncation or formatting) increases by 13--15\\% in relative terms after RSFT. As easy errors (truncation, duplication) are eliminated, the remaining error distribution shifts toward harder cases: cross-sentence reasoning, implicit relations, and long-tail entity pairs. The relation types with the largest RSFT gains (participant, conflict, league, screenwriter, operator, contains\\_administrative\\_territory) involve cross-sentence reasoning or long-tail entities, consistent with RSFT's selection pressure toward diverse, high-quality outputs.\n\n\\begin{table}[t]\n\\centering\n\\caption{Error pattern changes from SFT to RSFT across scales. $\\Delta$\\% shows relative change. Truncation FN, hallucinated FP, and duplicates all decrease; evidence quality and residual FN difficulty are unchanged.}\n\\label{tab:error_analysis}\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llccc}\n\\toprule\n\\textbf{Error Category} & \\textbf{Direction} & \\textbf{1.7B} & \\textbf{4B} & \\textbf{8B / LLaMA} \\\\\n\\midrule\nTruncation FN & $\\downarrow$ & $-$22\\% & $-$16\\% & $-$18\\% \\\\\nHallucinated FP & $\\downarrow$ & $-$8\\% & $-$6\\% & $-$12\\% \\\\\nDuplicates & $\\downarrow$ & $-$20\\% & $-$11\\% & $-$14\\% \\\\\nEvidence (exact) & $\\approx$ & $<$0.4pp & $<$0.4pp & $<$0.4pp \\\\\nFN: other & $\\uparrow$ & +13\\% & +15\\% & +14\\% \\\\\n\\bottomrule\n\\end{tabular}%\n}\n\\end{table}\n\n\n\\section{Per-Relation EDCR Distribution}\n\\label{sec:edcr_per_relation}\n\nComputing EDCR for each of the 76 relation types with $\\geq$5 evaluation samples (from the RSFT CED s42 model) reveals that per-relation EDCR correlates strongly with per-relation Rel-F1 ($\\rho = -0.79$, $n = 76$, $p < 0.001$), confirming its utility as a difficulty indicator. Filtering to types with $\\geq$5 predictions strengthens the correlation ($\\rho = -0.85$, $n = 74$, $p < 0.001$). Per-relation EDCR is statistically independent of Evi-F1 ($\\rho = -0.06$, $p = 0.58$), and Evi-F1 itself shows no association with Rel-F1 ($\\rho = -0.01$, $p = 0.91$). These null correlations establish that evidence quality and extraction ability are fully decoupled across relation types. Extreme cases illustrate the diagnostic power: \\texttt{date\\_of\\_birth} has EDCR $= 0.118$ (highly faithful, with extraction and evidence tightly coupled), while \\texttt{head\\_of\\_government} reaches $0.956$ (highly decoupled). This per-relation analysis avoids the shared-component concern present in cross-method EDCR-vs-Rel-F1 correlation, providing independent validation of EDCR's diagnostic utility. A permutation test (10,000 iterations) on the per-relation correlation yields $p < 0.0001$, confirming that the association is not an artifact of the shared TP component.\n\n\\paragraph{Partial correlations controlling for TP.}\nBecause EDCR shares TP (true positives) in both numerator and denominator with Rel-F1, we report partial correlations controlling for Evi-Recall$_\\text{TP}$. At the cross-method level ($n = 17$ seed-specific configurations), the partial Spearman $\\rho = -0.8541$ ($p = 0.000025$), virtually unchanged from the raw $\\rho = -0.8554$ (0.15\\% reduction). Removing the GRPO QLoRA outlier yields partial $\\rho = -0.8681$ ($n = 16$, $p = 0.000027$). Aggregating to $n = 7$ unique methods: raw $\\rho = -0.9643$, partial $\\rho = -0.9617$. These results confirm that the EDCR--Rel-F1 association is not driven by the shared TP component. Note that seed-level configurations ($n = 17$) are not fully independent; the $n = 7$ unique-method analysis provides a conservative estimate.\n\n\\paragraph{Similar-TP, different-EDCR pairs.}\nTo further validate that EDCR captures information beyond what TP alone provides, we identify configuration pairs with similar Evi-Recall$_\\text{TP}$ ($|\\Delta| < 5$pp) but substantially different EDCR ($|\\Delta| > 5$pp). Forty-eight such pairs exist across all configurations. The most illustrative: DPO-CED 1-epoch (Evi-Recall$_\\text{TP} = 0.833$) vs.\\ RSFT CED LLaMA s43 (Evi-Recall$_\\text{TP} = 0.829$) differ by only 2.4pp in TP-conditioned evidence recall but 13.6pp in EDCR, reflecting the substantial extraction gap between these methods. This pattern demonstrates that EDCR captures extraction-evidence alignment that aggregate TP metrics miss.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\linewidth]{fig_edcr_relations.pdf}\n\\caption{Per-relation EDCR distribution across all 93 relation types observed in the development set (of 96 defined in DocRED). The correlation analysis in the text uses the 76 types with $\\geq$5 samples for statistical reliability. Red bars indicate EDCR $\\geq$ 0.70 (severe decoupling), green bars indicate EDCR $<$ 0.30 (healthy evidence grounding). Seven types exhibit EDCR = 1.0.}\n\\label{fig:edcr_relations}\n\\end{figure}\n\n\n\\section{Qualitative Analysis}\n\\label{sec:qualitative}\n\nWe present representative examples illustrating three phenomena: evidence quality differences between SFT and RSFT, GRPO format gaming under catastrophic collapse, and per-relation EDCR diagnostics.\n\n\\paragraph{Case 1: Evidence quality.}\nTable~\\ref{tab:case_evidence} compares evidence citations from SFT and RSFT on three documents. SFT tends to cite many sentences indiscriminately, including distractors unrelated to the target triple, while RSFT selects precisely the gold evidence sentences. For \\emph{America's Sweetheart}, SFT cites 6 sentences (precision 0.17) whereas RSFT cites only the single correct sentence (precision 1.00). The pattern is consistent: SFT achieves evidence precision of 0.00--0.20 across these examples, while RSFT achieves 1.00 in all three cases.\n\n\\begin{table}[t]\n\\centering\n\\caption{Evidence citation comparison between SFT and RSFT. Precision measures the fraction of cited sentences that match gold evidence.}\n\\label{tab:case_evidence}\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llccc}\n\\toprule\n\\textbf{Document} & \\textbf{Triple} & \\textbf{SFT Prec.} & \\textbf{RSFT Prec.} & \\textbf{SFT \\#Cited} \\\\\n\\midrule\nOleg Tinkov & (Oleg Tinkov, country of citizenship, Russia) & 0.00 & 1.00 & 3 \\\\\nAmerica's Sweetheart & (record label, country, United States) & 0.17 & 1.00 & 6 \\\\\nJade (Mortal Kombat) & (Jade, present in work, Mortal Kombat) & 0.20 & 1.00 & 5 \\\\\n\\bottomrule\n\\end{tabular}%\n}\n\\end{table}\n\n\\paragraph{Case 2: GRPO format gaming.}\nUnder catastrophic collapse (GRPO QLoRA $G{=}4$), the model abandons the DocRED 96-type relation ontology and generates free-text relation labels. On the document \\emph{Something to Believe In}, the model produces 35 predicted triples with relations such as ``is a'', ``honor'', and ``location'', none of which belong to the target ontology. All 35 predictions are incorrect. Similarly, for \\emph{J\\'{o}zef Pi\\l{}sudski Monument}, 28 predictions use non-standard relations with 0 correct matches. The model retains the structural format of triple-with-evidence output but fills it with fabricated relation types. The model produces well-formed evidence for these non-existent relations.\n\n\\paragraph{Case 3: EDCR diagnostics.}\nPer-relation EDCR identifies specific relation types where extraction and evidence are misaligned. For \\texttt{date\\_of\\_birth} (EDCR $= 0.118$), the model's evidence consistently matches gold annotations: both extraction and evidence point to the same biographical sentence. In contrast, \\texttt{notable\\_work} (EDCR $= 0.941$) exhibits severe decoupling: the model cites sentence [0] (a general introduction) instead of the gold evidence sentence [3] (which contains the actual work attribution). High-EDCR relations tend to involve indirect or multi-hop reasoning where surface-level context misleads the evidence generator.\n\n\n\\section{Use of AI Assistants}\n\\label{app:ai-assistants}\n\nWe used Claude (Anthropic) as an AI coding and writing assistant\nthroughout this work. Specifically:\n\\begin{itemize}\n    \\item \\textbf{Code:} drafting experiment scripts, data-processing\n    pipelines, and analysis utilities; debugging and refactoring.\n    \\item \\textbf{Writing:} drafting and revising paper sections,\n    polishing prose, and reformatting LaTeX.\n    \\item \\textbf{Literature:} summarizing related papers to inform\n    the related-work section.\n\\end{itemize}\n",
      "numLines": 457,
      "startLine": 1,
      "totalLines": 457
    }
  },
  "sourceToolAssistantUUID": "7cddcce9-5c4a-43e0-937a-f24636f0993c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "6a109daa-4474-48f0-ab6d-eef9007c0510",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 23_

```json
{
  "type": "last-prompt",
  "leafUuid": "95b55ac0-b8f4-41c7-855a-ddd005bac453",
  "sessionId": "6a109daa-4474-48f0-ab6d-eef9007c0510"
}
```

---

### Runtime record

_source line 24_

```json
{
  "type": "ai-title",
  "aiTitle": "Audit paper numbers across LaTeX sections",
  "sessionId": "6a109daa-4474-48f0-ab6d-eef9007c0510"
}
```

---

### Assistant

_source line 25 · 2026-05-23T19:21:51.875Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the files. Let me systematically extract and cross-verify every number.

## Abstract numbers to verify:

1. **-5.63pp dev Ign-F1** (1.7B evidence tax)
2. **+0.25±0.47pp at 4B** (evidence tax at 4B)
3. **Cohen's d=2.58** (LLaMA pairwise seed separation)
4. **51.19 Ign-F1** (1.7B RSFT model)
5. **std 0.09pp** (1.7B RSFT std)


6. **50.19** (8B SFT performance)
7. **std 3.23pp** (8B SFT std)
8. **4.7× fewer parameters** (1.7B vs 8B)
9. **Spearman ρ=1.0** (test-set model ranking)
10. **1.7B, 4B, 8B** (three fully evaluated scales)
11. **14B validation** 
12. **two model families**
13. **two datasets**

## Introduction numbers to verify:

1. **-5.63pp Ign-F1** at 1.7B (

line 17, 22)
2. **+0.25±0.47pp at 4B** (line 17, 22)
3. **ρ=-0.79, n=76, p<0.001** (line 24) — EDCR per-relation
4. **+1.2 to +6.6pp** RSFT improvement range (line 26)
5. **51.19 Ign-F1, std 0.09pp** (line 26) — 1.7B RSFT
6. **50.19, std 3.23pp** (line 26) — 8B SFT
7. **4.7× fewer parameters** (line 26)
8. **Cohen's d=2.58** (line 24) — LLaMA
9. **EDCR 0.6797 and 0.6487** (line 24) — SFT and RSFT

I need to clarify where these EDCR values appear. The introduction mentions the metric is validated at the per-relation level with that strong correlation, but the actual values 0.6797 and 0.6487 are reported in the methods section. Let me verify which specific lines these come from to make sure I'm tracking the right numbers.

Now I'm going through the method section to confirm the EDCR baseline for SFT at 0.6797 and RSFT at 0.6487, along with the other key metrics like the GRPO QLoRA performance at 0.9876 and the various correlation coefficients across different validation levels. I also need to check the conclusion section for the model scales tested and the parameter efficiency claim.

I'm verifying the -5.63pp evidence tax at 1.7B by cross-referencing the abstract, introduction, and appendix table calculations where the difference between fair with evidence (48.38) and fair without evidence (42.75) confirms the penalty. Now checking the +0.25±0.47pp improvement at 4B across the same sections. Continuing to verify the 1.7B RSFT metrics—the 51.19 Ign-F1 score and 0.09pp standard deviation appear consistently across the abstract, introduction, experiments section, and the scaling table. Now checking the 8B SFT baseline performance of 50.19, which should also be referenced across multiple sections. Verifying the parameter ratio: 8B divided by 1.7B gives approximately 4.71, so the 4.7× claim is accurate across all mentions. Now checking the Spearman correlation coefficient for the test-set ranking preservation. Ranking by test results shows the same order, confirming the Spearman correlation of 1.0. Now checking the EDCR values in the method section—the SFT baseline is listed at 0.6797 and RSFT at 0.6487, both matching the main results table.

GRPO QLoRA shows 0.9876 across all document sections. The per-relation EDCR correlation of ρ=-0.79 with n=76 and p<0.001 is consistently cited in the introduction, methods, experiments, and appendix.

Now checking the cross-method EDCR correlation where ρ=-0.89, n=7, p=0.007 appears in the method and experiments sections. The independence check shows ρ=-0.06, p=0.58 between EDCR and evidence F1 scores, verified across multiple locations. Finally, I'm looking at the RSFT improvement range of +1.2 to +6.6 percentage points mentioned in the introduction and the scaling table. The table values round consistently to the introduction's summary—6.55 becomes 6.6 and 1.24 becomes 1.2 when expressed to one decimal place. This is just a difference in precision between the detailed experiments section and the broader introduction summary, so there's no actual inconsistency here.

Now I'm checking the SFT baseline numbers across different tables and seeds. The main table shows 43.58±3.80, but I need to verify this against the ablation and scaling tables to understand the full range of seed variation, particularly that 39.74 value mentioned in the ablation section. Now I'm verifying the RSFT CED results by checking the three individual seed values from the ablation data and confirming they average to 44.82 with a standard deviation of 0.51.

Looking at the RSFT Evi-F1 metric, it shows 80.96 compared to the SFT baseline of 79.61, which I can cross-reference across the main table and experimental results. The EDCR metric shows RSFT at 0.6487 versus SFT's 0.6797, and I'm verifying these values appear consistently in both the main results table and the method documentation.

For RSFT's Rel-F1 score of 45.80, this appears in the main table and is mentioned in the experiments section as part of the simultaneous capability maintenance. Moving to GRPO with QLoRA, the results show Rel-F1 dropping to 1.38 while Evi-F1 rises to 85.04 with EDCR at 0.9876, all confirmed in the spectrum appendix. The bf16 variant shows Rel-F1 at 45.49 and EDCR at 0.6318 with Evi-F1 at 80.86.

For DPO, I'm tracking the metric transitions where Rel-F1 decreases from 33.37 to 31.45, Evi-F1 increases from 80.90 to 84.84, and EDCR shifts from 0.8123 to 0.7503.

Now I'm verifying the duplication rate improvement where the evidence-based approach reduces output duplication from 60.5% down to 33.0%, which is confirmed in the mechanistic analysis section. Looking at the variance compression ratios next, which show a 31× improvement at the 1.7B scale. The appendix table caption clarifies that compression ratios are calculated from unrounded standard deviation values, not the rounded ones displayed. So while the shown values of 2.79 and 0.09 divide to 31.0, the actual unrounded figures must be slightly different—something like 2.7934 and 0.0857—which would yield the 32.6× shown in the compression column.

This reveals a genuine inconsistency: the experiments text reports 31× compression for the 1.7B model using the rounded values, while the appendix table shows 32.6× using unrounded values. Now checking the 36× claim in experiments—that's calculated as 3.23/0.09, which only gives 35.9, so there's a rounding discrepancy there too.

For LLaMA, the 4.6× variance compression checks out: 2.92/0.64 = 4.56, which rounds to 4.6×, and this matches across both the experiments text and appendix. Now I need to verify the RSFT seed ranges for LLaMA that are mentioned in line 65. I'm verifying the RSFT improvements across model sizes by checking the calculations against the scaling table—each gain matches up correctly. Now I'm moving on to validate the Method B results, which show a 4.18 percentage point improvement at 4B scale.

Looking at the duplication rates across different model sizes, I can see that evidence-based inference substantially reduces output repetition, with the gap narrowing as models get larger. The claim about halving the duplication rate at 1.7B is approximately correct—60.5% down to 33.0% is close to a 50% reduction.

Now checking the CED versus flat-NLI comparison, which shows a negligible 0.02 percentage point difference between the two methods. Moving on to verify the RSFT CED performance claim of 44.82 Ign-F1, which is indeed 1.24 points above the SFT baseline of 43.58.

For the weakest RSFT seed claim, I'm looking at the ablation table data. There are actually four seeds reported (s42, s43, s44, s45), but the main results use only three seeds for the mean calculation. Among those three seeds used for reporting (s42=44.23, s43=45.12, s44=45.11), s42 at 44.23 is the weakest, which matches what the text states—though s45=44.16 would technically be lower if included.

Now checking the k=1 vs k=3 comparison: the ablation shows k=1 achieves 44.66 and k=3 achieves 43.64, giving exactly the 1.02 Ign-F1 difference cited in the experiments section. For Re-DocRED, the RSFT result of 41.45 with a 4.86 percentage point improvement over the SFT baseline of 36.59 also checks out against the appendix.

On the DocRED side, I need to verify the +5.08pp gain claim. The ablation data shows RSFT CED at 44.66 and SFT at 39.74, which would give 4.92—but using the 3-seed mean of 44.82 instead yields exactly 5.08, matching what's stated in the experiments section.

Now I'm checking the evidence strategy comparison numbers. The post-hoc retrieval achieves 48.76 Rel-F1, which corresponds to the no-evidence SFT model in the main table. For the evidence strategy metrics, I'm seeing RSFT CED reaches 36.1 with an EDCR of 0.654, but there's a discrepancy—the table shows RSFT EDCR as 0.6487, not 0.654. There's a discrepancy between the two EDCR values—0.654 in the experiments section versus 0.6487 in the table—and since EDCR is computed the same way regardless of whether we're looking at joint or TP-only Evi-F1, these should match. Let me dig into whether there's a different computation method or rounding issue at play here.

Looking at the per-seed breakdown for RSFT CED, I can see the individual values across seeds s42 through s45, and when I average just the first three seeds (0.6569 + 0.6542 + 0.6350) / 3, I get exactly 0.6487—which matches the table value. So the table is using a 3-seed average while the experiments section might be reporting something different.

The 0.654 figure doesn't align with either the 3-seed mean of 0.6487 or the 4-seed mean of 0.6503, so it's likely computed using a different methodology—possibly the DREEAM-protocol joint denominator rather than the standard TP-only calculation. Looking more carefully at line 104 in experiments.tex, I see the EDCR values are tied to specific Evi-F1 scores—0.766 for post-hoc retrieval and 0.654 for RSFT CED. So the 0.654 isn't a standalone metric but corresponds to RSFT CED's particular Evi-F1 result, which explains why it doesn't match the table values I was comparing it against.

Now checking the DREEAM numbers: experiments.tex says 54.01% but the encoder comparison table shows 54.15 for the same metric. That's a discrepancy I need to flag. this discrepancy about the DREEAM numbers. Now I'm checking the RSFT results across different model scales on the Re-DocRED test set—there's a consistent drop of roughly 20 percentage points in Ign-F1 from dev to test, which matches what the experiments section claims, though the exact numbers vary slightly by model size.

Looking at the annotation density claim next: 34.7 versus 12.3 gold triples per document gives a ratio of about 2.82×, which checks out mathematically.

Now I'm verifying the Spearman correlation claim for test ranking.

Moving on to the partial correlations in the discussion—the values ρ = -0.8541 versus -0.8554 are confirmed across both the main text and appendix, with the appendix noting this represents only a 0.15% reduction when controlling for shared components.

Finally, checking the CED versus flat-NLI comparison showing Rel-F1 scores of 45.63 and 45.61 respectively... Evidence quality stays below 0.4 percentage points across all scales. Now I'm verifying the conclusion claims—three fully evaluated model scales, validation on 14B, two model families and datasets, plus the key result that the 1.7B RSFT model matches 8B SFT performance with 4.7× fewer parameters. Moving into a precision consistency check on the Ign-F1 metrics across tables. Now I'm checking the EDCR precision across different sections — most values use 4 decimal places, but I notice the experiments section at line 104 drops to 3 decimal places, which breaks the consistency pattern. 81.26, 82.84 — all consistently 2 decimal places except for 36.1 in the encoder_comparison table, which drops to 1 decimal place. That's the only outlier in the Evi-F1 values. Rel-F1 stays consistent at 2 decimals throughout. Now checking the abstract against the table footnotes — both define positive values as indicating cost, with the scaling table specifying that the tax calculation is no-evidence minus with-evidence.

The evidence tax of +0.25pp at 4B aligns with this definition. Looking at the variance confidence intervals, the SFT and RSFT ranges at 1.7B don't overlap as claimed — SFT's lower bound of 1.45 exceeds RSFT's upper bound of 0.54. Finally, verifying the training-time tax figures: 8B shows +0.04pp and 14B shows +0.03pp, which matches the appendix calculations exactly.

Now checking the RSFT performance gains — at 1.7B the improvement is 6.55 points (51.19 minus 44.64), and at 4B with Method B the model reaches 51.52 for a +4.18pp boost over the independent SFT baseline. I can't verify this last value against the tables directly, so I'm noting that as uncertain. There's also something about a footnote on the 4B dev Ign-F1 that got cut off.

The footnote explains that the 4B test results use a retrained checkpoint since the original wasn't available, with the retrained v2 achieving 43.88 dev performance compared to the original's 44.23 — that's documented and checks out. For the 14B RSFT Rel-F1 value of 60.09, I found it in the encoder comparison table, but the cross-detail table shows dashes for 14B RSFT entries, so I'm still tracking down where that 60.09 comes from exactly.

Now looking at the 14B RSFT evidence and joint F1 scores — the encoder comparison table shows 83.92 for TP-only and 48.59 for joint, but there's no other table to cross-reference these values against. And I'm noticing a discrepancy with DREEAM: the experiments text cites 54.01% but the encoder comparison table lists 54.15 for the same metric. So there's definitely a discrepancy with the DREEAM numbers—54.01 cited directly from the paper versus 54.15 in the encoder comparison table, both labeled as joint Evi-F1. I'll flag that as an inconsistency. Now checking the RSFT LLaMA calculation: 56.54 minus 51.09 gives exactly 5.45, so that checks out. For the SFT seed range of 39.74 to 47.34 at 4B, if the mean across three seeds is 43.58 with a standard deviation of 3.80, and I know one seed is 39.74, the third seed would work out to around 43.43.

66. Verifying the standard deviation with those three values—39.74, 43.66, and 47.34—gives a variance of about 14.44 and a standard deviation of 3.80, which matches perfectly. Now I'm looking at the evidence strategy comparison and the EDCR values reported in the experiments section, where post-hoc BM25 shows 0.766 and RSFT CED shows 0.654.

There's a discrepancy though—the RSFT EDCR of 0.654 doesn't align with what's in the main table at 0.6487. I'm wondering if the evidence strategy section might be using a different calculation method, perhaps involving joint evidence recall rather than just true positives, or maybe it's computed from a single seed rather than the three-seed average. Let me check the individual seed values to see if one of them matches that 0.654 figure.

Looking at the breakdown, s42 gives 0.6569, s43 gives 0.6542, and s44 gives 0.6350. The s43 value of 0.6542 rounds to 0.654 when expressed to three decimal places, which could explain the discrepancy if that particular seed was used for the evidence strategy comparison instead of the standard s42 seed used elsewhere.

However, checking other possibilities—like whether 0.654 could be a two-seed average of s42 and s43—yields 0.6556, which rounds to 0.656, not 0.654. So that doesn't work either. Given that other values in the evidence strategy section also use three decimal place precision, it seems plausible they're rounding s43's result, though this remains an unexplained inconsistency worth noting.

Actually, I'm now wondering if the evidence strategy section is evaluating a different model configuration entirely—"Post-hoc BM25 retrieval (entity-constrained, k=2)" versus the main RSFT results. But the text explicitly states "RSFT CED reaches 36.1 (EDCR 0.654)", which should be the same RSFT model. The formula EDCR = Evi-Recall_TP / Rel-Recall shouldn't depend on how Evi-F1 is computed, so the EDCR value should remain consistent. Unless the evidence strategy section is computing EDCR differently—perhaps using joint Evi-Recall (all predicted triples rather than just true positives) in the numerator, which would explain the discrepancy.

That would constitute a different metric than what's defined in the paper, so I'm flagging this as a potential inconsistency.

Now I'm doing a final precision check across the abstract and introduction to ensure all reported values maintain consistent decimal places—verifying that percentages, correlation coefficients, and multipliers all follow the same formatting standards throughout.

I'm also checking the methods and experiments sections for any deviations, particularly noting that the EDCR values in the evidence strategy section use three decimal places while other sections use four, and I need to verify the variance compression ratios reported in the experiments section. I'm noticing a discrepancy in the 1.7B variance compression figures—the main text reports 31× while the appendix table shows 32.6×. The difference comes down to rounding: the text uses rounded standard deviation values (2.79 and 0.09) which divide to 31.0, but the appendix table uses full-precision values that yield 32.6× when computed. I'm checking whether the 8B and LLaMA results are combined in that column header, which seems like an unusual but acceptable approach for a summary table. Let me also verify the LLaMA-specific metrics: the RSFT gain of +5.45pp checks out from the scaling table, and the 4.6× variance compression (2.92/0.64 = 4.56) matches both the variance table and what appears in the main text around line 65. Now I'm ready to write up the audit report.

Before I do, I want to cross-check a few more claims from the methods section. The EDCR values cited—0.9876 for GRPO QLoRA and 0.6487 for RSFT—both match their corresponding table entries. And the negative correlation between EDCR and Rel-F1 across the seven method configurations (Spearman ρ=-0.89, n=7, p=0.007) is what I'm verifying now.

Now I'm checking the seed separation claim about LLaMA. The abstract mentions complete pairwise seed separation with Cohen's d=2.58, and I need to confirm that every RSFT seed actually exceeds every SFT seed—looking at the values, RSFT ranges from 55.87 to 57.14 while SFT ranges from 48.02 to 53.84, so that checks out.

For the Method B case, I'm tracing through the calculation: if RSFT from the independent SFT base achieves 51.52 Ign-F1 with a +4.18pp improvement, that means the Method B SFT base itself scored 47.34, which interestingly matches the strongest standard SFT seed mentioned in the main text.

Now I'm moving on to compile the final audit document, but first let me verify a few more details from the experiments section. The CED reranking results show 48.64 Rel-F1, which aligns well with the 48.76 no-evidence baseline. I'm also confirming the abstract's claims about the three fully evaluated scales and the two model families and datasets being tested.

One more thing to check: the 1.7B tax value of -5.63pp actually indicates that evidence generation is beneficial at that scale, since the negative tax means the no-evidence model performs worse. The abstract correctly frames this as "beneficial" with the negative cost notation. I've verified the sign conventions are consistent throughout—negative tax means a benefit, and the abstract correctly labels the 1.7B results as beneficial since the negative value indicates evidence helps. The units all check out as percentage points. Now I'm ready to write up the report.

Looking at the discrepancies more carefully, I found three genuine inconsistencies: the variance compression ratio differs between the main text (31×) and appendix (32.6×), the DREEAM Evi-F1 value is reported as 54.01% in one place but 54.15 in the table, and the RSFT EDCR in the evidence strategy section shows 0.654 but the main table has 0.6487 with no individual seed matching exactly. There are also a few minor precision inconsistencies where some values use different decimal places than others, and a couple of entries I couldn't fully verify against the tables.

Now I'm ready to write up the report.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "95b55ac0-b8f4-41c7-855a-ddd005bac453",
  "isSidechain": false,
  "requestId": "req_011CbL36tjS9ifeyxZzDNjUU",
  "type": "assistant",
  "uuid": "d844bd36-92fb-44f6-9c9c-e70f3eb969d1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "6a109daa-4474-48f0-ab6d-eef9007c0510",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Wm1ZLCsSywHUdfkdwrZcwq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 25984,
      "cache_read_input_tokens": 24492,
      "output_tokens": 17175,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 25984,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 17175,
          "cache_read_input_tokens": 24492,
          "cache_creation_input_tokens": 25984,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 25984
          },
          "type": "message"
        }
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

_source line 26 · 2026-05-23T19:21:51.878Z_

All files loaded. Now I'll systematically cross-verify every number. Let me compute some values and write the audit report.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d844bd36-92fb-44f6-9c9c-e70f3eb969d1",
  "isSidechain": false,
  "requestId": "req_011CbL36tjS9ifeyxZzDNjUU",
  "type": "assistant",
  "uuid": "9362f47e-03b2-4a09-80e0-5684d1294ffc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "6a109daa-4474-48f0-ab6d-eef9007c0510",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Wm1ZLCsSywHUdfkdwrZcwq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 25984,
      "cache_read_input_tokens": 24492,
      "output_tokens": 17175,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 25984,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 17175,
          "cache_read_input_tokens": 24492,
          "cache_creation_input_tokens": 25984,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 25984
          },
          "type": "message"
        }
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

_source line 27 · 2026-05-23T19:21:52.140Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01Bf31r9Zggb7JFzKMngQNKM`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/",
  "description": "List artifacts directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9362f47e-03b2-4a09-80e0-5684d1294ffc",
  "isSidechain": false,
  "requestId": "req_011CbL36tjS9ifeyxZzDNjUU",
  "type": "assistant",
  "uuid": "7dcdf1bc-e0fc-4c39-a066-9d1fe7e90353",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "6a109daa-4474-48f0-ab6d-eef9007c0510",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Wm1ZLCsSywHUdfkdwrZcwq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 25984,
      "cache_read_input_tokens": 24492,
      "output_tokens": 17175,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 25984,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 17175,
          "cache_read_input_tokens": 24492,
          "cache_creation_input_tokens": 25984,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 25984
          },
          "type": "message"
        }
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

_source line 28 · 2026-05-23T19:21:52.295Z_

<details><summary>↩ Tool result · `toolu_01Bf31r9Zggb7JFzKMngQNKM`</summary>

```text
14b_rsft_status.md
1_7b_repetition_fair_eval.md
_project
anon_cleanup_report.md
anon_repo_diff.md
ced_eval_commands.md
ced_stabilizer_literature_survey.md
comprehensive_results.md
cuda3_diagnostic.md
d024_literature_survey.md
d076_eval_audit.py
d076_final_audit.py
d076_seed_status.md
d102_next_batch
d112
d112_pipeline_plan.md
d112_rsft_no_evidence_eval_r3_analysis.md
d112_rsft_no_evidence_eval_r3_prep.md
d112_rsft_s44_train_prep.md
d140_4b_sft_s42_no_evi_2048_diagnosis.md
d140_progress_check.md
dev_test_gap_paragraph.md
diag_mvp2_grpo_flatnli_r3.md
diag_plan019_1_7b_rsft_s43.md
diag_redocred_rsft_r2.md
diagnose_8b_timeout.md
diagnose_eval_llama_rsft_s42_with_evidence_2048.md
diagnose_eval_llama_sft_s42_no_evidence_std.md
diagnose_plan_001.md
diversity_probe.py
diversity_probe_results.md
dpo_rebuilt_3ep_eval
dream_reports
dreeam_evif1_alignment_report.md
edcr_analysis.md
edcr_analysis_r2b.md
edcr_diagnostic_table.md
eval_plan_014_no_evidence_r2_analysis.md
eval_progress_20260516.md
eval_progress_check_0515.md
eval_rsft_ced_s43
eval_rsft_ced_s45
eval_script_audit.md
eval_status_check.md
evidence_cost_literature_scan.md
evidence_tax_annotation_notes.md
experiment_summary_table.md
fig_edcr_relations.pdf
fig_edcr_relations.png
fig_evidence_tax.pdf
fig_evidence_tax.png
fig_grpo_dynamics.pdf
fig_grpo_dynamics.png
fig_spectrum.pdf
fig_spectrum.png
freige
gap_analysis_w3.md
grpo_forgetting_dynamics.pdf
grpo_forgetting_dynamics.png
kl_analysis_report.md
literature_quantization_rl.md
literature_survey_evidence_overhead.md
manifest.yaml
metrics_summary.csv
metrics_summary_table.md
mvp2_eval_rsft_r2b_maxtok1536_r2
negative_review.md
next_batch_plan.md
no_evi_test_commands.md
paired_ttest_analysis.py
paper
paper_evidence_table.md
paper_main_tables_draft.md
paper_metrics_table.md
paper_status_audit.md
paper_table1_data.md
plan019_8b_sft_s43_eval_analysis.md
plan_001_flat_nli_seed45
plan_003
plan_003_edcr_cross_method_table.md
plan_003_edcr_diagnostic
plan_003_edcr_diagnostic.md
plan_006_qwen3_1_7b_no_evidence_eval_v3_results.json
plan_007_redocred_rsft_eval_r2
plan_009
plan_009_dynamics_data.json
plan_009_dynamics_figure
plan_009_forgetting_data.csv
plan_009_forgetting_data_v5.csv
plan_009_forgetting_figure
plan_009_grpo_forgetting
plan_012_dpo_ced
plan_012_dpo_ced_1ep_analysis.md
process_check_report.md
reeval_ced_s42
reeval_ced_s44
reeval_commands.md
reeval_flat_nli_s42
reeval_flat_nli_s43_r2
reeval_sft_baseline_d076
related_work_gap_analysis.md
related_work_survey
review_issues.yaml
review_reports
review_round_2
rsft_gen_progress_check.md
rsft_pipeline_commands.md
server_state_20260522.md
status_check_loop4.md
test_eval_14b_rsft_s43
test_eval_14b_rsft_s43_no_evi
test_eval_14b_rsft_s43_pair
test_eval_4b_rsft_s44_no_evi_r2
test_eval_8b_rsft_s42
test_eval_commands.md
test_eval_llama_rsft_s42_no_evi_v2
test_eval_llama_rsft_s42_with_evi_v3
test_table_compilation.md
test_table_draft.md
topk_ablation_lit_review.md
training_health_check.md
training_trajectory_loop4.md
trl_grpo_stability_research.md
worker_check_status.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7dcdf1bc-e0fc-4c39-a066-9d1fe7e90353",
  "isSidechain": false,
  "promptId": "659f4775-47ec-4bb9-8db5-86432609ca56",
  "type": "user",
  "uuid": "6639f9f7-6511-4944-9ef4-a337ea5aba04",
  "toolUseResult": {
    "stdout": "14b_rsft_status.md\n1_7b_repetition_fair_eval.md\n_project\nanon_cleanup_report.md\nanon_repo_diff.md\nced_eval_commands.md\nced_stabilizer_literature_survey.md\ncomprehensive_results.md\ncuda3_diagnostic.md\nd024_literature_survey.md\nd076_eval_audit.py\nd076_final_audit.py\nd076_seed_status.md\nd102_next_batch\nd112\nd112_pipeline_plan.md\nd112_rsft_no_evidence_eval_r3_analysis.md\nd112_rsft_no_evidence_eval_r3_prep.md\nd112_rsft_s44_train_prep.md\nd140_4b_sft_s42_no_evi_2048_diagnosis.md\nd140_progress_check.md\ndev_test_gap_paragraph.md\ndiag_mvp2_grpo_flatnli_r3.md\ndiag_plan019_1_7b_rsft_s43.md\ndiag_redocred_rsft_r2.md\ndiagnose_8b_timeout.md\ndiagnose_eval_llama_rsft_s42_with_evidence_2048.md\ndiagnose_eval_llama_sft_s42_no_evidence_std.md\ndiagnose_plan_001.md\ndiversity_probe.py\ndiversity_probe_results.md\ndpo_rebuilt_3ep_eval\ndream_reports\ndreeam_evif1_alignment_report.md\nedcr_analysis.md\nedcr_analysis_r2b.md\nedcr_diagnostic_table.md\neval_plan_014_no_evidence_r2_analysis.md\neval_progress_20260516.md\neval_progress_check_0515.md\neval_rsft_ced_s43\neval_rsft_ced_s45\neval_script_audit.md\neval_status_check.md\nevidence_cost_literature_scan.md\nevidence_tax_annotation_notes.md\nexperiment_summary_table.md\nfig_edcr_relations.pdf\nfig_edcr_relations.png\nfig_evidence_tax.pdf\nfig_evidence_tax.png\nfig_grpo_dynamics.pdf\nfig_grpo_dynamics.png\nfig_spectrum.pdf\nfig_spectrum.png\nfreige\ngap_analysis_w3.md\ngrpo_forgetting_dynamics.pdf\ngrpo_forgetting_dynamics.png\nkl_analysis_report.md\nliterature_quantization_rl.md\nliterature_survey_evidence_overhead.md\nmanifest.yaml\nmetrics_summary.csv\nmetrics_summary_table.md\nmvp2_eval_rsft_r2b_maxtok1536_r2\nnegative_review.md\nnext_batch_plan.md\nno_evi_test_commands.md\npaired_ttest_analysis.py\npaper\npaper_evidence_table.md\npaper_main_tables_draft.md\npaper_metrics_table.md\npaper_status_audit.md\npaper_table1_data.md\nplan019_8b_sft_s43_eval_analysis.md\nplan_001_flat_nli_seed45\nplan_003\nplan_003_edcr_cross_method_table.md\nplan_003_edcr_diagnostic\nplan_003_edcr_diagnostic.md\nplan_006_qwen3_1_7b_no_evidence_eval_v3_results.json\nplan_007_redocred_rsft_eval_r2\nplan_009\nplan_009_dynamics_data.json\nplan_009_dynamics_figure\nplan_009_forgetting_data.csv\nplan_009_forgetting_data_v5.csv\nplan_009_forgetting_figure\nplan_009_grpo_forgetting\nplan_012_dpo_ced\nplan_012_dpo_ced_1ep_analysis.md\nprocess_check_report.md\nreeval_ced_s42\nreeval_ced_s44\nreeval_commands.md\nreeval_flat_nli_s42\nreeval_flat_nli_s43_r2\nreeval_sft_baseline_d076\nrelated_work_gap_analysis.md\nrelated_work_survey\nreview_issues.yaml\nreview_reports\nreview_round_2\nrsft_gen_progress_check.md\nrsft_pipeline_commands.md\nserver_state_20260522.md\nstatus_check_loop4.md\ntest_eval_14b_rsft_s43\ntest_eval_14b_rsft_s43_no_evi\ntest_eval_14b_rsft_s43_pair\ntest_eval_4b_rsft_s44_no_evi_r2\ntest_eval_8b_rsft_s42\ntest_eval_commands.md\ntest_eval_llama_rsft_s42_no_evi_v2\ntest_eval_llama_rsft_s42_with_evi_v3\ntest_table_compilation.md\ntest_table_draft.md\ntopk_ablation_lit_review.md\ntraining_health_check.md\ntraining_trajectory_loop4.md\ntrl_grpo_stability_research.md\nworker_check_status.md",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "7dcdf1bc-e0fc-4c39-a066-9d1fe7e90353",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "6a109daa-4474-48f0-ab6d-eef9007c0510",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 29_

```json
{
  "type": "last-prompt",
  "leafUuid": "6639f9f7-6511-4944-9ef4-a337ea5aba04",
  "sessionId": "6a109daa-4474-48f0-ab6d-eef9007c0510"
}
```

---

### Runtime record

_source line 30_

```json
{
  "type": "ai-title",
  "aiTitle": "Audit paper numbers across LaTeX sections",
  "sessionId": "6a109daa-4474-48f0-ab6d-eef9007c0510"
}
```

---

### Tool call

_source line 31 · 2026-05-23T19:23:34.042Z_

<details open><summary>🔧 Tool call — Write · `toolu_018qWDnZVXr2TZMqDUCm3fsH`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/final_audit_w1_abstract.md",
  "content": "# Final Audit W1: Abstract + 正文数字交叉验证\n\n审计日期: 2026-05-23\n\n---\n\n## ✅ 已核对一致\n\n### Abstract 数字\n\n| 数字 | 来源 | 验证 |\n|------|------|------|\n| -5.63pp (1.7B evidence tax) | abstract.tex:5, introduction.tex:17,22, experiments.tex:59, appendix.tex:188 (tab:training_tax: 42.75-48.38=-5.63) | ✅ 全部一致 |\n| +0.25±0.47pp (4B tax) | abstract.tex:5, introduction.tex:17,22, experiments.tex:59, appendix.tex:189 | ✅ 全部一致 |\n| Cohen's d=2.58 (LLaMA) | abstract.tex:7, experiments.tex:65, appendix.tex:135 (tab:variance_ci) | ✅ 全部一致 |\n| 51.19 Ign-F1 (1.7B RSFT) | abstract.tex:7, introduction.tex:26, experiments.tex:81 (tab:scaling) | ✅ 全部一致 |\n| std 0.09pp (1.7B RSFT) | abstract.tex:7, introduction.tex:26, experiments.tex:63,81, appendix.tex:132 | ✅ 全部一致 |\n| 50.19 (8B SFT) | abstract.tex:7, introduction.tex:26, experiments.tex:83 (tab:scaling) | ✅ 全部一致 |\n| std 3.23pp (8B SFT) | abstract.tex:7, introduction.tex:26, experiments.tex:63,83, appendix.tex:134 | ✅ 全部一致 |\n| 4.7× fewer params | abstract.tex:7, introduction.tex:26, conclusion.tex:5, experiments.tex:63 — 8/1.7=4.706≈4.7 | ✅ 全部一致 |\n| ρ=1.0 (test ranking) | abstract.tex:7, experiments.tex:110, appendix.tex:218 — 手动验证 tab:test_results 排名: 14B>LLaMA>8B>1.7B>4B dev/test 相同 | ✅ 全部一致 |\n| non-overlapping χ² CIs at 1.7B | abstract.tex:7, appendix.tex:132 (SFT CI [1.45,17.55], RSFT CI [0.04,0.54], 1.45>0.54) | ✅ 不重叠确认 |\n\n### Introduction 数字\n\n| 数字 | 来源 | 验证 |\n|------|------|------|\n| -5.63pp (1.7B) | introduction.tex:17,22 → 与 abstract、experiments、appendix 一致 | ✅ |\n| +0.25±0.47pp (4B) | introduction.tex:17,22 → 同上 | ✅ |\n| ρ=-0.79, n=76, p<0.001 (per-relation EDCR) | introduction.tex:24, method.tex:72, experiments.tex:116, appendix.tex:394 | ✅ 四处一致 |\n| +1.2 to +6.6pp (RSFT range) | introduction.tex:26 → tab:scaling gains: +1.24, +1.24→1.2(1dp); +6.55→6.6(1dp) | ✅ 四舍五入正确 |\n| 51.19, std 0.09pp | introduction.tex:26 → 同 abstract 验证 | ✅ |\n| 50.19, std 3.23pp | introduction.tex:26 → 同 abstract 验证 | ✅ |\n| 4.7× | introduction.tex:26 → 同 abstract 验证 | ✅ |\n| Cohen's d=2.58 | introduction.tex:24 → 同 abstract 验证 | ✅ |\n\n### Method 数字\n\n| 数字 | 来源 | 验证 |\n|------|------|------|\n| EDCR 0.6797 (SFT baseline) | method.tex:72 → tab:main (experiments.tex:27): 0.6797 | ✅ |\n| EDCR 0.6487 (RSFT) | method.tex:72 → tab:main (experiments.tex:29): 0.6487; 手动验证 (0.6569+0.6542+0.6350)/3=0.6487 | ✅ |\n| EDCR 0.9876 (GRPO QLoRA) | method.tex:72 → tab:spectrum (appendix.tex:330): 0.9876 | ✅ |\n| ρ=-0.89, n=7, p=0.007 (cross-method) | method.tex:72, experiments.tex:116 | ✅ |\n| ρ=-0.06, p=0.58 (EDCR vs Evi-F1) | method.tex:72, experiments.tex:116, appendix.tex:394 | ✅ |\n\n### Experiments 数字 (除不一致项外)\n\n| 数字 | 来源 | 验证 |\n|------|------|------|\n| SFT mean 43.58±3.80, range 39.74--47.34 | experiments.tex:13, tab:main:27; 手动验证: seeds 39.74/43.66/47.34, mean=43.58, std=3.80 | ✅ |\n| SFT no-evidence 47.21 | tab:main:28, tab:ablation_full:61 | ✅ |\n| RSFT CED 44.82±0.51 (3-seed) | tab:main:29; 手动验证 (44.23+45.12+45.11)/3=44.82, std=0.511≈0.51 | ✅ |\n| Evi-F1 80.96 vs 79.61 | experiments.tex:15, tab:main:27,29 | ✅ |\n| RSFT Rel-F1 45.80 | tab:main:29, experiments.tex:46, appendix.tex:100 | ✅ |\n| GRPO QLoRA: Rel-F1 1.38, Evi-F1 85.04, EDCR 0.9876 | experiments.tex:43, tab:spectrum:330 | ✅ |\n| GRPO bf16: Rel-F1 45.49, EDCR 0.6318 | experiments.tex:43, tab:spectrum:331 | ✅ |\n| DPO 1ep→3ep: Rel-F1 33.37→31.45, Evi-F1 80.90→84.84, EDCR 0.8123→0.7503 | experiments.tex:46, tab:spectrum:332-333 | ✅ |\n| Duplication 60.5%→33.0% | experiments.tex:59, tab:mechanistic:162 | ✅ |\n| Training-time tax: +0.04pp (8B), +0.03pp (14B) | experiments.tex:59, tab:training_tax:190-191; 验证: 50.19-50.15=0.04, 55.10-55.07=0.03 | ✅ |\n| RSFT gains: +6.55/+1.24/+4.14/+3.79 | experiments.tex:61, tab:scaling; 验证: 51.19-44.64/44.82-43.58/54.33-50.19/58.86-55.07 | ✅ |\n| LLaMA RSFT gain +5.45 | tab:scaling:85; 56.54-51.09=5.45 | ✅ |\n| LLaMA seeds RSFT 55.87--57.14, SFT 48.02--53.84 | experiments.tex:65, appendix.tex:212 | ✅ |\n| Variance compression 7.5× (4B), 6.5× (8B), 4.6× (LLaMA) | experiments.tex:63,65, tab:variance_ci:133-135 | ✅ |\n| SFT seed stds: 2.79/3.80/3.23 (1.7B/4B/8B), RSFT: 0.09/0.51/0.50 | experiments.tex:63, tab:scaling, tab:variance_ci | ✅ |\n| 36× more predictable (3.23/0.09) | experiments.tex:63; 3.23/0.09=35.89≈36 | ✅ |\n| Re-DocRED: RSFT 41.45 (+4.86pp over SFT 36.59) | experiments.tex:110, appendix.tex:215; 41.45-36.59=4.86 | ✅ |\n| DocRED RSFT gain +5.08pp | experiments.tex:110, appendix.tex:215; 44.82-39.74=5.08 (3-seed mean minus SFT s42) | ✅ |\n| Test Ign-F1 drops ~20pp | tab:test_results: range 19.81--21.86pp across all models | ✅ |\n| Annotation density 34.7 vs 12.3, 2.82× | experiments.tex:110; 34.7/12.3=2.821 | ✅ |\n| Partial correlations ρ=-0.8541 vs -0.8554 | experiments.tex:116, appendix.tex:397-398 | ✅ |\n| CED vs flat-NLI: Rel-F1 45.63 vs 45.61 (diff 0.02pp) | experiments.tex:116, method.tex:55, appendix.tex:44 | ✅ |\n| k=1 vs k=3: +1.02 Ign-F1 | experiments.tex:116; 44.66-43.64=1.02 | ✅ |\n| Error reduction 6--22% | experiments.tex:116, tab:error_analysis: trunc FN -16~-22%, halluc FP -6~-12%, dup -11~-20% | ✅ |\n| Evidence unchanged <0.4pp | experiments.tex:116, tab:error_analysis | ✅ |\n| SFT evidence variance compression 25× (4B), 1.4× (8B) | experiments.tex:59, appendix.tex:199; 0.50/0.02=25, 0.48/0.35=1.37≈1.4 | ✅ |\n\n### Conclusion 数字\n\n| 数字 | 来源 | 验证 |\n|------|------|------|\n| 1.7B, 4B, 8B + 14B validation | conclusion.tex:4 → 与 abstract/intro 一致 | ✅ |\n| two model families, two datasets | conclusion.tex:4 → Qwen3+LLaMA, DocRED+Re-DocRED | ✅ |\n| 4.7× fewer params | conclusion.tex:5 → 与 abstract/intro/experiments 一致 | ✅ |\n\n---\n\n## ⚠️ 发现不一致\n\n### 1. 1.7B 方差压缩倍数: 31× vs 32.6×\n\n- **experiments.tex:63**: \"variance compression is 31× at 1.7B\"\n- **appendix.tex tab:variance_ci (line 132)**: Compression = 32.6×\n- **原因**: experiments 用 rounded std 计算 (2.79/0.09=31.0)；appendix 表声明 \"ratio of SFT to RSFT point estimates (unrounded)\"，用未四舍五入的 std 得到 32.6×\n- **建议**: 统一为 32.6×（使用精确值）或两处都写 31×（使用 rounded 值），不应两处不同\n\n### 2. DREEAM joint Evi-F1: 54.01% vs 54.15\n\n- **experiments.tex:110**: \"supervised DREEAM (54.01\\%~\\citep{ma2023dreeam})\"\n- **appendix.tex tab:encoder_comparison (line 306)**: DREEAM Evi-F1 (joint) = 54.15\n- **差异**: 0.14pp\n- **建议**: 核对 DREEAM 原论文的 exact value，统一两处\n\n### 3. Evidence Strategy 段 EDCR 0.654 vs Table 1 EDCR 0.6487\n\n- **experiments.tex:104 (§5.5)**: \"RSFT CED reaches 36.1 (EDCR 0.654)\"\n- **experiments.tex tab:main (line 29)**: RSFT CED EDCR = 0.6487\n- **个别 seed EDCR**: s42=0.6569, s43=0.6542, s44=0.6350, s45=0.6550 — 均不等于 0.654\n- **3-seed mean**: (0.6569+0.6542+0.6350)/3 = 0.6487; **4-seed mean**: 0.6503\n- **最接近**: s43=0.6542 四舍五入到 3dp 为 0.654，但其他 EDCR 均用 4dp\n- **建议**: 统一为 0.6487（3-seed mean）或明确标注哪个 seed/计算方式\n\n---\n\n## ❌ 待确认疑点\n\n### 1. RSFT Method B: 51.52 Ign-F1 at 4B (+4.18pp)\n\n- **experiments.tex:61**: \"RSFT from an independent SFT base (s44, Method B) achieves 51.52 Ign-F1 at 4B (+4.18pp over that base)\"\n- 推算 base = 51.52 - 4.18 = 47.34 (即 SFT 4B 最强 seed s44)\n- 内部逻辑自洽，但 **51.52 未出现在任何表格中**，无法从已有表格交叉验证\n\n### 2. CED reranking: Rel-F1 48.64, Evi-F1 81.88\n\n- **experiments.tex:104**: \"CED reranking at inference (best-of-N=8 by CED score) achieves Rel-F1 48.64 and Evi-F1 81.88 (TP-only)\"\n- **未出现在任何表格中**，无法交叉验证\n\n### 3. Post-hoc BM25: Evi-F1 (joint) 34.7, EDCR 0.766\n\n- **experiments.tex:104**: \"Post-hoc retrieval achieves higher Rel-F1 (48.76) ... lower Evi-F1 (joint) of 34.7 (EDCR 0.766)\"\n- Rel-F1 48.76 与 SFT no-evidence 的 Rel-F1 匹配（tab:main:28），✅\n- 但 **Evi-F1 34.7 和 EDCR 0.766 未出现在任何表格中**\n\n### 4. Evidence Strategy 段精度不统一\n\n- §5.5 使用 3dp EDCR (0.766, 0.654)，全文其他位置均用 4dp\n- §5.5 Evi-F1 36.1 用 1dp，tab:encoder_comparison 也用 36.1（一致但与其他 Evi-F1 的 2dp 不同）\n- 不影响正确性，但 reviewer 可能注意到\n\n---\n\n## 四舍五入一致性检查\n\n| 指标 | 精度 | 状态 |\n|------|------|------|\n| Ign-F1 | 2dp (43.58, 44.82, 51.19 等) | ✅ 全篇一致 |\n| Ign-F1 增量 | 2dp 正文 (e.g., +6.55, +1.24)；1dp 用于 intro 范围摘要 (+1.2 to +6.6) | ✅ 可接受 |\n| Rel-F1 | 2dp | ✅ 全篇一致 |\n| Evi-F1 | 2dp（除 §5.5 的 36.1 和 34.7 为 1dp） | ⚠️ 轻微不统一 |\n| EDCR | 4dp（除 §5.5 为 3dp） | ⚠️ 轻微不统一 |\n| Std | 2dp (0.09, 0.51, 3.80 等) | ✅ 全篇一致 |\n| 方差压缩倍数 | 1dp (4.7×, 4.6×, 7.5× 等) | ✅ 一致（但 32.6× 在 appendix 表中） |\n| Evidence tax | pp 单位，2dp | ✅ 全篇一致 |\n| 相关系数 ρ | 2dp (0.79, 0.89, 0.06) | ✅ 一致 |\n| p 值 | 3dp 或不等式 (0.007, <0.001) | ✅ 一致 |\n| Cohen's d | 2dp | ✅ 一致 |\n\n---\n\n## 总结\n\n- **已验证一致**: 50+ 个数字/统计量\n- **发现 3 个不一致**（需修正）:\n  1. 方差压缩 31× vs 32.6×\n  2. DREEAM Evi-F1 54.01% vs 54.15\n  3. EDCR 0.654 vs 0.6487\n- **4 个待确认疑点**（数字无对应表格，无法交叉验证）\n- **精度基本统一**，仅 §5.5 (Evidence Strategy Comparison) 存在轻微精度不统一\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6639f9f7-6511-4944-9ef4-a337ea5aba04",
  "isSidechain": false,
  "requestId": "req_011CbL3WyRsd6JpyhaYEoJdg",
  "type": "assistant",
  "uuid": "29e207ba-ce13-4ea3-8050-e1863b546587",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "6a109daa-4474-48f0-ab6d-eef9007c0510",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015SJtpPGMQoqobhX2qeSAxJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18461,
      "cache_read_input_tokens": 50476,
      "output_tokens": 5028,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 18461,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5028,
          "cache_read_input_tokens": 50476,
          "cache_creation_input_tokens": 18461,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 18461
          },
          "type": "message"
        }
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

_source line 32 · 2026-05-23T19:23:34.093Z_

<details><summary>↩ Tool result · `toolu_018qWDnZVXr2TZMqDUCm3fsH`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/final_audit_w1_abstract.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "29e207ba-ce13-4ea3-8050-e1863b546587",
  "isSidechain": false,
  "promptId": "659f4775-47ec-4bb9-8db5-86432609ca56",
  "type": "user",
  "uuid": "c7aeed08-cac1-49e0-bfc9-7fd3b28a878b",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/final_audit_w1_abstract.md",
    "content": "# Final Audit W1: Abstract + 正文数字交叉验证\n\n审计日期: 2026-05-23\n\n---\n\n## ✅ 已核对一致\n\n### Abstract 数字\n\n| 数字 | 来源 | 验证 |\n|------|------|------|\n| -5.63pp (1.7B evidence tax) | abstract.tex:5, introduction.tex:17,22, experiments.tex:59, appendix.tex:188 (tab:training_tax: 42.75-48.38=-5.63) | ✅ 全部一致 |\n| +0.25±0.47pp (4B tax) | abstract.tex:5, introduction.tex:17,22, experiments.tex:59, appendix.tex:189 | ✅ 全部一致 |\n| Cohen's d=2.58 (LLaMA) | abstract.tex:7, experiments.tex:65, appendix.tex:135 (tab:variance_ci) | ✅ 全部一致 |\n| 51.19 Ign-F1 (1.7B RSFT) | abstract.tex:7, introduction.tex:26, experiments.tex:81 (tab:scaling) | ✅ 全部一致 |\n| std 0.09pp (1.7B RSFT) | abstract.tex:7, introduction.tex:26, experiments.tex:63,81, appendix.tex:132 | ✅ 全部一致 |\n| 50.19 (8B SFT) | abstract.tex:7, introduction.tex:26, experiments.tex:83 (tab:scaling) | ✅ 全部一致 |\n| std 3.23pp (8B SFT) | abstract.tex:7, introduction.tex:26, experiments.tex:63,83, appendix.tex:134 | ✅ 全部一致 |\n| 4.7× fewer params | abstract.tex:7, introduction.tex:26, conclusion.tex:5, experiments.tex:63 — 8/1.7=4.706≈4.7 | ✅ 全部一致 |\n| ρ=1.0 (test ranking) | abstract.tex:7, experiments.tex:110, appendix.tex:218 — 手动验证 tab:test_results 排名: 14B>LLaMA>8B>1.7B>4B dev/test 相同 | ✅ 全部一致 |\n| non-overlapping χ² CIs at 1.7B | abstract.tex:7, appendix.tex:132 (SFT CI [1.45,17.55], RSFT CI [0.04,0.54], 1.45>0.54) | ✅ 不重叠确认 |\n\n### Introduction 数字\n\n| 数字 | 来源 | 验证 |\n|------|------|------|\n| -5.63pp (1.7B) | introduction.tex:17,22 → 与 abstract、experiments、appendix 一致 | ✅ |\n| +0.25±0.47pp (4B) | introduction.tex:17,22 → 同上 | ✅ |\n| ρ=-0.79, n=76, p<0.001 (per-relation EDCR) | introduction.tex:24, method.tex:72, experiments.tex:116, appendix.tex:394 | ✅ 四处一致 |\n| +1.2 to +6.6pp (RSFT range) | introduction.tex:26 → tab:scaling gains: +1.24, +1.24→1.2(1dp); +6.55→6.6(1dp) | ✅ 四舍五入正确 |\n| 51.19, std 0.09pp | introduction.tex:26 → 同 abstract 验证 | ✅ |\n| 50.19, std 3.23pp | introduction.tex:26 → 同 abstract 验证 | ✅ |\n| 4.7× | introduction.tex:26 → 同 abstract 验证 | ✅ |\n| Cohen's d=2.58 | introduction.tex:24 → 同 abstract 验证 | ✅ |\n\n### Method 数字\n\n| 数字 | 来源 | 验证 |\n|------|------|------|\n| EDCR 0.6797 (SFT baseline) | method.tex:72 → tab:main (experiments.tex:27): 0.6797 | ✅ |\n| EDCR 0.6487 (RSFT) | method.tex:72 → tab:main (experiments.tex:29): 0.6487; 手动验证 (0.6569+0.6542+0.6350)/3=0.6487 | ✅ |\n| EDCR 0.9876 (GRPO QLoRA) | method.tex:72 → tab:spectrum (appendix.tex:330): 0.9876 | ✅ |\n| ρ=-0.89, n=7, p=0.007 (cross-method) | method.tex:72, experiments.tex:116 | ✅ |\n| ρ=-0.06, p=0.58 (EDCR vs Evi-F1) | method.tex:72, experiments.tex:116, appendix.tex:394 | ✅ |\n\n### Experiments 数字 (除不一致项外)\n\n| 数字 | 来源 | 验证 |\n|------|------|------|\n| SFT mean 43.58±3.80, range 39.74--47.34 | experiments.tex:13, tab:main:27; 手动验证: seeds 39.74/43.66/47.34, mean=43.58, std=3.80 | ✅ |\n| SFT no-evidence 47.21 | tab:main:28, tab:ablation_full:61 | ✅ |\n| RSFT CED 44.82±0.51 (3-seed) | tab:main:29; 手动验证 (44.23+45.12+45.11)/3=44.82, std=0.511≈0.51 | ✅ |\n| Evi-F1 80.96 vs 79.61 | experiments.tex:15, tab:main:27,29 | ✅ |\n| RSFT Rel-F1 45.80 | tab:main:29, experiments.tex:46, appendix.tex:100 | ✅ |\n| GRPO QLoRA: Rel-F1 1.38, Evi-F1 85.04, EDCR 0.9876 | experiments.tex:43, tab:spectrum:330 | ✅ |\n| GRPO bf16: Rel-F1 45.49, EDCR 0.6318 | experiments.tex:43, tab:spectrum:331 | ✅ |\n| DPO 1ep→3ep: Rel-F1 33.37→31.45, Evi-F1 80.90→84.84, EDCR 0.8123→0.7503 | experiments.tex:46, tab:spectrum:332-333 | ✅ |\n| Duplication 60.5%→33.0% | experiments.tex:59, tab:mechanistic:162 | ✅ |\n| Training-time tax: +0.04pp (8B), +0.03pp (14B) | experiments.tex:59, tab:training_tax:190-191; 验证: 50.19-50.15=0.04, 55.10-55.07=0.03 | ✅ |\n| RSFT gains: +6.55/+1.24/+4.14/+3.79 | experiments.tex:61, tab:scaling; 验证: 51.19-44.64/44.82-43.58/54.33-50.19/58.86-55.07 | ✅ |\n| LLaMA RSFT gain +5.45 | tab:scaling:85; 56.54-51.09=5.45 | ✅ |\n| LLaMA seeds RSFT 55.87--57.14, SFT 48.02--53.84 | experiments.tex:65, appendix.tex:212 | ✅ |\n| Variance compression 7.5× (4B), 6.5× (8B), 4.6× (LLaMA) | experiments.tex:63,65, tab:variance_ci:133-135 | ✅ |\n| SFT seed stds: 2.79/3.80/3.23 (1.7B/4B/8B), RSFT: 0.09/0.51/0.50 | experiments.tex:63, tab:scaling, tab:variance_ci | ✅ |\n| 36× more predictable (3.23/0.09) | experiments.tex:63; 3.23/0.09=35.89≈36 | ✅ |\n| Re-DocRED: RSFT 41.45 (+4.86pp over SFT 36.59) | experiments.tex:110, appendix.tex:215; 41.45-36.59=4.86 | ✅ |\n| DocRED RSFT gain +5.08pp | experiments.tex:110, appendix.tex:215; 44.82-39.74=5.08 (3-seed mean minus SFT s42) | ✅ |\n| Test Ign-F1 drops ~20pp | tab:test_results: range 19.81--21.86pp across all models | ✅ |\n| Annotation density 34.7 vs 12.3, 2.82× | experiments.tex:110; 34.7/12.3=2.821 | ✅ |\n| Partial correlations ρ=-0.8541 vs -0.8554 | experiments.tex:116, appendix.tex:397-398 | ✅ |\n| CED vs flat-NLI: Rel-F1 45.63 vs 45.61 (diff 0.02pp) | experiments.tex:116, method.tex:55, appendix.tex:44 | ✅ |\n| k=1 vs k=3: +1.02 Ign-F1 | experiments.tex:116; 44.66-43.64=1.02 | ✅ |\n| Error reduction 6--22% | experiments.tex:116, tab:error_analysis: trunc FN -16~-22%, halluc FP -6~-12%, dup -11~-20% | ✅ |\n| Evidence unchanged <0.4pp | experiments.tex:116, tab:error_analysis | ✅ |\n| SFT evidence variance compression 25× (4B), 1.4× (8B) | experiments.tex:59, appendix.tex:199; 0.50/0.02=25, 0.48/0.35=1.37≈1.4 | ✅ |\n\n### Conclusion 数字\n\n| 数字 | 来源 | 验证 |\n|------|------|------|\n| 1.7B, 4B, 8B + 14B validation | conclusion.tex:4 → 与 abstract/intro 一致 | ✅ |\n| two model families, two datasets | conclusion.tex:4 → Qwen3+LLaMA, DocRED+Re-DocRED | ✅ |\n| 4.7× fewer params | conclusion.tex:5 → 与 abstract/intro/experiments 一致 | ✅ |\n\n---\n\n## ⚠️ 发现不一致\n\n### 1. 1.7B 方差压缩倍数: 31× vs 32.6×\n\n- **experiments.tex:63**: \"variance compression is 31× at 1.7B\"\n- **appendix.tex tab:variance_ci (line 132)**: Compression = 32.6×\n- **原因**: experiments 用 rounded std 计算 (2.79/0.09=31.0)；appendix 表声明 \"ratio of SFT to RSFT point estimates (unrounded)\"，用未四舍五入的 std 得到 32.6×\n- **建议**: 统一为 32.6×（使用精确值）或两处都写 31×（使用 rounded 值），不应两处不同\n\n### 2. DREEAM joint Evi-F1: 54.01% vs 54.15\n\n- **experiments.tex:110**: \"supervised DREEAM (54.01\\%~\\citep{ma2023dreeam})\"\n- **appendix.tex tab:encoder_comparison (line 306)**: DREEAM Evi-F1 (joint) = 54.15\n- **差异**: 0.14pp\n- **建议**: 核对 DREEAM 原论文的 exact value，统一两处\n\n### 3. Evidence Strategy 段 EDCR 0.654 vs Table 1 EDCR 0.6487\n\n- **experiments.tex:104 (§5.5)**: \"RSFT CED reaches 36.1 (EDCR 0.654)\"\n- **experiments.tex tab:main (line 29)**: RSFT CED EDCR = 0.6487\n- **个别 seed EDCR**: s42=0.6569, s43=0.6542, s44=0.6350, s45=0.6550 — 均不等于 0.654\n- **3-seed mean**: (0.6569+0.6542+0.6350)/3 = 0.6487; **4-seed mean**: 0.6503\n- **最接近**: s43=0.6542 四舍五入到 3dp 为 0.654，但其他 EDCR 均用 4dp\n- **建议**: 统一为 0.6487（3-seed mean）或明确标注哪个 seed/计算方式\n\n---\n\n## ❌ 待确认疑点\n\n### 1. RSFT Method B: 51.52 Ign-F1 at 4B (+4.18pp)\n\n- **experiments.tex:61**: \"RSFT from an independent SFT base (s44, Method B) achieves 51.52 Ign-F1 at 4B (+4.18pp over that base)\"\n- 推算 base = 51.52 - 4.18 = 47.34 (即 SFT 4B 最强 seed s44)\n- 内部逻辑自洽，但 **51.52 未出现在任何表格中**，无法从已有表格交叉验证\n\n### 2. CED reranking: Rel-F1 48.64, Evi-F1 81.88\n\n- **experiments.tex:104**: \"CED reranking at inference (best-of-N=8 by CED score) achieves Rel-F1 48.64 and Evi-F1 81.88 (TP-only)\"\n- **未出现在任何表格中**，无法交叉验证\n\n### 3. Post-hoc BM25: Evi-F1 (joint) 34.7, EDCR 0.766\n\n- **experiments.tex:104**: \"Post-hoc retrieval achieves higher Rel-F1 (48.76) ... lower Evi-F1 (joint) of 34.7 (EDCR 0.766)\"\n- Rel-F1 48.76 与 SFT no-evidence 的 Rel-F1 匹配（tab:main:28），✅\n- 但 **Evi-F1 34.7 和 EDCR 0.766 未出现在任何表格中**\n\n### 4. Evidence Strategy 段精度不统一\n\n- §5.5 使用 3dp EDCR (0.766, 0.654)，全文其他位置均用 4dp\n- §5.5 Evi-F1 36.1 用 1dp，tab:encoder_comparison 也用 36.1（一致但与其他 Evi-F1 的 2dp 不同）\n- 不影响正确性，但 reviewer 可能注意到\n\n---\n\n## 四舍五入一致性检查\n\n| 指标 | 精度 | 状态 |\n|------|------|------|\n| Ign-F1 | 2dp (43.58, 44.82, 51.19 等) | ✅ 全篇一致 |\n| Ign-F1 增量 | 2dp 正文 (e.g., +6.55, +1.24)；1dp 用于 intro 范围摘要 (+1.2 to +6.6) | ✅ 可接受 |\n| Rel-F1 | 2dp | ✅ 全篇一致 |\n| Evi-F1 | 2dp（除 §5.5 的 36.1 和 34.7 为 1dp） | ⚠️ 轻微不统一 |\n| EDCR | 4dp（除 §5.5 为 3dp） | ⚠️ 轻微不统一 |\n| Std | 2dp (0.09, 0.51, 3.80 等) | ✅ 全篇一致 |\n| 方差压缩倍数 | 1dp (4.7×, 4.6×, 7.5× 等) | ✅ 一致（但 32.6× 在 appendix 表中） |\n| Evidence tax | pp 单位，2dp | ✅ 全篇一致 |\n| 相关系数 ρ | 2dp (0.79, 0.89, 0.06) | ✅ 一致 |\n| p 值 | 3dp 或不等式 (0.007, <0.001) | ✅ 一致 |\n| Cohen's d | 2dp | ✅ 一致 |\n\n---\n\n## 总结\n\n- **已验证一致**: 50+ 个数字/统计量\n- **发现 3 个不一致**（需修正）:\n  1. 方差压缩 31× vs 32.6×\n  2. DREEAM Evi-F1 54.01% vs 54.15\n  3. EDCR 0.654 vs 0.6487\n- **4 个待确认疑点**（数字无对应表格，无法交叉验证）\n- **精度基本统一**，仅 §5.5 (Evidence Strategy Comparison) 存在轻微精度不统一\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "29e207ba-ce13-4ea3-8050-e1863b546587",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "6a109daa-4474-48f0-ab6d-eef9007c0510",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 33 · 2026-05-23T19:23:34.099Z_

```json
{
  "parentUuid": "c7aeed08-cac1-49e0-bfc9-7fd3b28a878b",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "e08bff41-2690-4942-8a56-6dd1b7e08112",
  "timestamp": "2026-05-23T19:23:34.099Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "6a109daa-4474-48f0-ab6d-eef9007c0510",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 34 · 2026-05-23T19:23:44.120Z_

审计完成。报告已写入 `artifacts/final_audit_w1_abstract.md`。

**核心发现**：

**3 个不一致需修正**：
1. 1.7B 方差压缩倍数 — experiments 写 31×，appendix 表写 32.6×（rounded vs unrounded std 计算差异）
2. DREEAM Evi-F1 — experiments 文中写 54.01%，encoder_comparison 表写 54.15（差 0.14pp）
3. §5.5 EDCR — 文中写 0.654，Table 1 写 0.6487，且无任何单 seed 精确匹配 0.654

**4 个数字缺少表格支撑**（无法交叉验证）：Method B 51.52、CED reranking 48.64/81.88、post-hoc BM25 34.7/0.766。

其余 50+ 个数字全部验证一致，精度统一（仅 §5.5 存在轻微 dp 不统一）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e08bff41-2690-4942-8a56-6dd1b7e08112",
  "isSidechain": false,
  "requestId": "req_011CbL3eUfifUk228uiesYfM",
  "type": "assistant",
  "uuid": "a6f81e6b-006e-4f2e-a1cd-fa37335542c0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "6a109daa-4474-48f0-ab6d-eef9007c0510",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016qqmNWGvKsuFEuKXreScYK",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5188,
      "cache_read_input_tokens": 68937,
      "output_tokens": 299,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5188,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 299,
          "cache_read_input_tokens": 68937,
          "cache_creation_input_tokens": 5188,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5188
          },
          "type": "message"
        }
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

_source line 35_

```json
{
  "type": "last-prompt",
  "leafUuid": "a6f81e6b-006e-4f2e-a1cd-fa37335542c0",
  "sessionId": "6a109daa-4474-48f0-ab6d-eef9007c0510"
}
```

---

### Runtime record

_source line 36_

```json
{
  "type": "ai-title",
  "aiTitle": "Audit paper numbers across LaTeX sections",
  "sessionId": "6a109daa-4474-48f0-ab6d-eef9007c0510"
}
```

---
