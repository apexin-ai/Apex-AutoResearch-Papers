# Research conversation: <project_context> # 项目: contamcal-irt-calibration ## 运行环境 - 服务器名: cqa1-21977 - SSH 连接命令: ssh connect.cqa1.seetacloud.com

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 63
- **Recorded user turns:** 1
- **Tool calls:** 16
- **Original source:** `logs/chats/exported-trajectories/account-2/a95a1f6e-644c-4d12-abb6-01351d2cbf40.jsonl`
- **Structured JSON:** [`a9a31e75a2ae5a53fc33.json`](../../sessions/a9/a9a31e75a2ae5a53fc33.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-21T11:06:45.131Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-21T11:06:45.131Z",
  "sessionId": "a95a1f6e-644c-4d12-abb6-01351d2cbf40",
  "content": "&lt;project_context>\n# 项目: contamcal-irt-calibration\n\n## 运行环境\n- 服务器名: cqa1-21977\n- SSH 连接命令: ssh connect.cqa1.seetacloud.com  # 必须用此命令，~/.ssh/config 自动应用密钥和跳板机，禁止用裸 IP\n- 项目代码根目录: /root/contamcal-irt-calibration\n\n## ⚠️ 活跃约束（必须遵守）\n\n- **C001**: 提交实验前必须检查目标 GPU 上是否已有同类进程（nvidia-smi 查 PID + 对比 output dir），有则不提交（原因：GPU 2 因重复提交导致 4 次进程冲突和数据污染。on_failed hook 触发的 worker 和手动提交都不做查重。）\n- **C002**: 提交 GPU 任务前必须用 nvidia-smi 确认目标 GPU 空闲，不得仅依赖 get_project_resource_usage 判断（原因：resource_usage 工具因 PID/tmux 不匹配严重误报（cuda:0/2/3 活跃但报 idle），已导致调度风险。Reviewer 2026-05-14 确认。）\n- **C003**: 标记实验为 failed 时必须同时 kill 所有关联 GPU 进程；submit 新任务到 GPU 前必须先 nvidia-smi + ps 确认该 GPU 无残留进程（原因：GPU 2 两次出现\"标 failed 不 kill 进程\"导致新旧进程冲突、数据腐败风险。v3 标 failed 但 2 个子进程存活，v4 提交时未检查，造成三进程竞争同一 output-dir。）\n- **C004**: 提交 GPU 实验时必须在命令中显式设置 CUDA_VISIBLE_DEVICES=N，不依赖默认行为（原因：已两次出现声明 cuda:3 实际跑在 cuda:0 的事故（PID 498153、PID 513900/513826），根因是 tmux/nohup 启动时未显式传递 CUDA_VISIBLE_DEVICES。）\n- **C005**: 禁止在 cuda:4 有 SFT 训练运行时提交 compute_signals 任务到 cuda:4；signals_3B 任务必须等目标 GPU 独占空闲后再提交（原因：cuda:4 三次出现未授权 compute_signals 进程与 d000_v3 SFT 抢显存（PID 590509, 605267, 607648）。来源疑为旧 session Worker 或 auto-loop 触发的 signals 批量任务。必须杜绝 signals 任务与 SFT 训练共享 GPU。）\n- **C006**: 禁止在 alpha=16 checkpoint 上启动任何任务（训练/eval/信号计算）。废弃目录黑名单：Qwen2.5-3B_d000_s42, Qwen2.5-3B_d000_v2_s42, Qwen2.5-3B_d005_s42, Qwen2.5-3B_d025_s42, Qwen2.5-3B_d100_s42（不含 _v3/_v2 等 alpha=32 重训版本）。启动前必须 cat adapter_config.json | grep lora_alpha 确认 =32。（原因：D055/D076 决定全部标准化到 alpha=32 + lr=5e-5。本 session 已 4 次发现 Worker 在废弃 alpha=16 checkpoint 上启动信号计算，每次 kill 后又重启新进程，累计浪费 10+ GPU-hours。根因是 Worker prompt 中缺少废弃 checkpoint 黑名单。） [来自 D055]\n- **C007**: GPU 释放后优先级：0.5B s123 signals > 1.5B s123 signals > d100_a32_s123 signals > 其他。0.5B/1.5B s123 全部完成前不分配 GPU 给低优先级信号任务。（原因：0.5B/1.5B s123 合计 +8 respondents 是达到 N≥16 IRT 门槛的最高 ROI 路径，d100 仅 +1。Reviewer 第三次确认优先级倒挂风险。）\n- **C008**: IRT 模型选择规则：2PL+γ 为默认（robust，N<16 可用）；4PL+γ 仅当 N≥16 且 benchmark 为 MCQ format 时使用。N<16 时 4PL 的 c/d 参数不可识别，会导致 PPP=0 和校准恶化。（原因：ARC N=5 使用 4PL+γ 导致 PPP=0.000、MAE 从 0.004 恶化到 0.068（过参数化）。Director 指令要求建立模型选择规则供后续所有 IRT fitting 使用。）\n- **C009**: 启动 eval 前必须 md5sum evaluate.py 并确认与 reference hash（westd 37591 bytes 版本）一致；跨服务器 eval 前必须先 SCP 同步脚本（原因：M022/M025: evaluate.py 版本漂移已第三次导致无效 eval 结果。mc_suffix 位置差异（user turn vs assistant turn）产生 3.63pp 系统性偏移，浪费数小时 GPU 时间。） [来自 D159]\n- **C010**: C009 扩展：分析脚本读取的 eval 数据必须全部来自同一版本 evaluate.py。同一 benchmark 不同 dosage 的数据禁止混用不同版本产出。分析前验证所有输入文件的 evaluate.py 版本一致。（原因：M022/M025 再现：analyze_gsm8k.py 在 westd 读旧版 d000 数据(71.04%)，cqa1 新版产出 d000=70.58%，0.46pp 偏移。混用会导致 contamination effect 估算偏差。）\n\n\n## 环境搭建\n连接服务器后先调 `detect_image` 检测是否为预置镜像。如果匹配，跳过基础环境搭建，只装项目特有依赖。已预装的包不要重复安装。\n\n## 输出风格\n回复简洁直接。只输出执行结果和必要信息，不要解释过程、不要客套、不要给未被要求的建议。\n&lt;/project_context>\n## 任务：GSM8K Appendix 数据完整性检查 + LLaMA-3 论文段落准备\n\n### 背景\nEMNLP 2026 ARR deadline May 25（D+4）。论文有一个 GSM8K Cross-Benchmark Transfer Appendix。\n\n### 步骤\n\n1. **GSM8K Appendix 数据完整性**：\n   用 `read_registry` 搜索所有包含 \"gsm8k\" 的 DONE 实验，列出每个家族的 GSM8K 数据覆盖情况。\n   \n   已知：\n   - Qwen-14B: 完整 5-dose (d000=74.98, d005=71.19, d025=79.30, d050=?, d100=82.41)\n   - Qwen-7B: 完整 5-dose (d000=73.31, d100=81.20)\n   - Phi-4: d000=84.46, d100=?\n   - OLMo-2: 已排除（D204: evaluate.py 版本不一致）\n   - Gemma-2: catastrophic forgetting (17.82), 不做\n   \n   确认 Phi-4 d100 GSM8K 是否已有数据。如果没有，记录为 gap。\n\n2. **读 paper_framing.md 和 ROADMAP.md**，确认 LLaMA-3 验证结果需要写入哪些论文章节。\n\n3. **产出**：\n   - GSM8K appendix 数据完整性表格（每个家族 × 每个 dosage 的数据状态）\n   - Phi-4 d100 GSM8K 状态确认\n   - LLaMA-3 结果预计写入的论文章节列表"
}
```

---

### Runtime record

_source line 2 · 2026-05-21T11:06:45.135Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-21T11:06:45.135Z",
  "sessionId": "a95a1f6e-644c-4d12-abb6-01351d2cbf40"
}
```

---

## Round 1

61 recorded events

### User

_source line 3 · 2026-05-21T11:06:45.168Z_

&lt;project_context>
# 项目: contamcal-irt-calibration

## 运行环境
- 服务器名: cqa1-21977
- SSH 连接命令: ssh connect.cqa1.seetacloud.com  # 必须用此命令，~/.ssh/config 自动应用密钥和跳板机，禁止用裸 IP
- 项目代码根目录: /root/contamcal-irt-calibration

## ⚠️ 活跃约束（必须遵守）

- **C001**: 提交实验前必须检查目标 GPU 上是否已有同类进程（nvidia-smi 查 PID + 对比 output dir），有则不提交（原因：GPU 2 因重复提交导致 4 次进程冲突和数据污染。on_failed hook 触发的 worker 和手动提交都不做查重。）
- **C002**: 提交 GPU 任务前必须用 nvidia-smi 确认目标 GPU 空闲，不得仅依赖 get_project_resource_usage 判断（原因：resource_usage 工具因 PID/tmux 不匹配严重误报（cuda:0/2/3 活跃但报 idle），已导致调度风险。Reviewer 2026-05-14 确认。）
- **C003**: 标记实验为 failed 时必须同时 kill 所有关联 GPU 进程；submit 新任务到 GPU 前必须先 nvidia-smi + ps 确认该 GPU 无残留进程（原因：GPU 2 两次出现"标 failed 不 kill 进程"导致新旧进程冲突、数据腐败风险。v3 标 failed 但 2 个子进程存活，v4 提交时未检查，造成三进程竞争同一 output-dir。）
- **C004**: 提交 GPU 实验时必须在命令中显式设置 CUDA_VISIBLE_DEVICES=N，不依赖默认行为（原因：已两次出现声明 cuda:3 实际跑在 cuda:0 的事故（PID 498153、PID 513900/513826），根因是 tmux/nohup 启动时未显式传递 CUDA_VISIBLE_DEVICES。）
- **C005**: 禁止在 cuda:4 有 SFT 训练运行时提交 compute_signals 任务到 cuda:4；signals_3B 任务必须等目标 GPU 独占空闲后再提交（原因：cuda:4 三次出现未授权 compute_signals 进程与 d000_v3 SFT 抢显存（PID 590509, 605267, 607648）。来源疑为旧 session Worker 或 auto-loop 触发的 signals 批量任务。必须杜绝 signals 任务与 SFT 训练共享 GPU。）
- **C006**: 禁止在 alpha=16 checkpoint 上启动任何任务（训练/eval/信号计算）。废弃目录黑名单：Qwen2.5-3B_d000_s42, Qwen2.5-3B_d000_v2_s42, Qwen2.5-3B_d005_s42, Qwen2.5-3B_d025_s42, Qwen2.5-3B_d100_s42（不含 _v3/_v2 等 alpha=32 重训版本）。启动前必须 cat adapter_config.json | grep lora_alpha 确认 =32。（原因：D055/D076 决定全部标准化到 alpha=32 + lr=5e-5。本 session 已 4 次发现 Worker 在废弃 alpha=16 checkpoint 上启动信号计算，每次 kill 后又重启新进程，累计浪费 10+ GPU-hours。根因是 Worker prompt 中缺少废弃 checkpoint 黑名单。） [来自 D055]
- **C007**: GPU 释放后优先级：0.5B s123 signals > 1.5B s123 signals > d100_a32_s123 signals > 其他。0.5B/1.5B s123 全部完成前不分配 GPU 给低优先级信号任务。（原因：0.5B/1.5B s123 合计 +8 respondents 是达到 N≥16 IRT 门槛的最高 ROI 路径，d100 仅 +1。Reviewer 第三次确认优先级倒挂风险。）
- **C008**: IRT 模型选择规则：2PL+γ 为默认（robust，N<16 可用）；4PL+γ 仅当 N≥16 且 benchmark 为 MCQ format 时使用。N<16 时 4PL 的 c/d 参数不可识别，会导致 PPP=0 和校准恶化。（原因：ARC N=5 使用 4PL+γ 导致 PPP=0.000、MAE 从 0.004 恶化到 0.068（过参数化）。Director 指令要求建立模型选择规则供后续所有 IRT fitting 使用。）
- **C009**: 启动 eval 前必须 md5sum evaluate.py 并确认与 reference hash（westd 37591 bytes 版本）一致；跨服务器 eval 前必须先 SCP 同步脚本（原因：M022/M025: evaluate.py 版本漂移已第三次导致无效 eval 结果。mc_suffix 位置差异（user turn vs assistant turn）产生 3.63pp 系统性偏移，浪费数小时 GPU 时间。） [来自 D159]
- **C010**: C009 扩展：分析脚本读取的 eval 数据必须全部来自同一版本 evaluate.py。同一 benchmark 不同 dosage 的数据禁止混用不同版本产出。分析前验证所有输入文件的 evaluate.py 版本一致。（原因：M022/M025 再现：analyze_gsm8k.py 在 westd 读旧版 d000 数据(71.04%)，cqa1 新版产出 d000=70.58%，0.46pp 偏移。混用会导致 contamination effect 估算偏差。）


## 环境搭建
连接服务器后先调 `detect_image` 检测是否为预置镜像。如果匹配，跳过基础环境搭建，只装项目特有依赖。已预装的包不要重复安装。

## 输出风格
回复简洁直接。只输出执行结果和必要信息，不要解释过程、不要客套、不要给未被要求的建议。
&lt;/project_context>
## 任务：GSM8K Appendix 数据完整性检查 + LLaMA-3 论文段落准备

### 背景
EMNLP 2026 ARR deadline May 25（D+4）。论文有一个 GSM8K Cross-Benchmark Transfer Appendix。

### 步骤

1. **GSM8K Appendix 数据完整性**：
   用 `read_registry` 搜索所有包含 "gsm8k" 的 DONE 实验，列出每个家族的 GSM8K 数据覆盖情况。
   
   已知：
   - Qwen-14B: 完整 5-dose (d000=74.98, d005=71.19, d025=79.30, d050=?, d100=82.41)
   - Qwen-7B: 完整 5-dose (d000=73.31, d100=81.20)
   - Phi-4: d000=84.46, d100=?
   - OLMo-2: 已排除（D204: evaluate.py 版本不一致）
   - Gemma-2: catastrophic forgetting (17.82), 不做
   
   确认 Phi-4 d100 GSM8K 是否已有数据。如果没有，记录为 gap。

2. **读 paper_framing.md 和 ROADMAP.md**，确认 LLaMA-3 验证结果需要写入哪些论文章节。

3. **产出**：
   - GSM8K appendix 数据完整性表格（每个家族 × 每个 dosage 的数据状态）
   - Phi-4 d100 GSM8K 状态确认
   - LLaMA-3 结果预计写入的论文章节列表

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "ff132cc0-9ef7-4a70-8848-7ec535292349",
  "type": "user",
  "uuid": "0fb208db-4e80-456c-896e-9a8210999c63",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "a95a1f6e-644c-4d12-abb6-01351d2cbf40",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-21T11:06:45.168Z_

```json
{
  "parentUuid": "0fb208db-4e80-456c-896e-9a8210999c63",
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
  "uuid": "d76a6fe0-9647-4ad5-85b9-4491f22e2bfe",
  "timestamp": "2026-05-21T11:06:45.168Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "a95a1f6e-644c-4d12-abb6-01351d2cbf40",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-21T11:06:45.168Z_

```json
{
  "parentUuid": "d76a6fe0-9647-4ad5-85b9-4491f22e2bfe",
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
  "uuid": "2239ae87-de20-4434-bb38-af29c9ae6956",
  "timestamp": "2026-05-21T11:06:45.168Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "a95a1f6e-644c-4d12-abb6-01351d2cbf40",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6 · 2026-05-21T11:06:45.168Z_

```json
{
  "parentUuid": "2239ae87-de20-4434-bb38-af29c9ae6956",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "d334ce50-2f1d-4bc2-9d73-78701e0135c2",
  "timestamp": "2026-05-21T11:06:45.168Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "a95a1f6e-644c-4d12-abb6-01351d2cbf40",
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
  "aiTitle": "Verify GSM8K appendix data and prepare LLaMA-3 paper sections",
  "sessionId": "a95a1f6e-644c-4d12-abb6-01351d2cbf40"
}
```

---

### Assistant

_source line 8 · 2026-05-21T11:06:48.372Z_

I'll start by gathering data from the registry and reading the project files in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d334ce50-2f1d-4bc2-9d73-78701e0135c2",
  "isSidechain": false,
  "requestId": "req_011CbFc9JVZEyowoMSVjMqp2",
  "type": "assistant",
  "uuid": "102abc76-56fe-4b19-8f9a-de055823f6c3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "a95a1f6e-644c-4d12-abb6-01351d2cbf40",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VhhhvKcRYjaUWUFoDbpQEf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13457,
      "cache_read_input_tokens": 11841,
      "output_tokens": 119,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13457,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 119,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 13457,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13457
          },
          "type": "message"
        }
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

_source line 9 · 2026-05-21T11:06:49.670Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_017D2QiEptdtsQ6FPjEVXqT3`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__read_project_file",
  "max_results": 2
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "102abc76-56fe-4b19-8f9a-de055823f6c3",
  "isSidechain": false,
  "requestId": "req_011CbFc9JVZEyowoMSVjMqp2",
  "type": "assistant",
  "uuid": "252f9416-17ad-4725-b71a-fce1f50d32b7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "a95a1f6e-644c-4d12-abb6-01351d2cbf40",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VhhhvKcRYjaUWUFoDbpQEf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13457,
      "cache_read_input_tokens": 11841,
      "output_tokens": 119,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13457,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 119,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 13457,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13457
          },
          "type": "message"
        }
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

_source line 10 · 2026-05-21T11:06:49.692Z_

<details><summary>↩ Tool result · `toolu_017D2QiEptdtsQ6FPjEVXqT3`</summary>

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
  "parentUuid": "252f9416-17ad-4725-b71a-fce1f50d32b7",
  "isSidechain": false,
  "promptId": "ff132cc0-9ef7-4a70-8848-7ec535292349",
  "type": "user",
  "uuid": "0fb2f5f1-51ea-40fa-aaeb-62578addaa0f",
  "toolUseResult": {
    "matches": [
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__read_project_file"
    ],
    "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__read_project_file",
    "total_deferred_tools": 25
  },
  "sourceToolAssistantUUID": "252f9416-17ad-4725-b71a-fce1f50d32b7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "a95a1f6e-644c-4d12-abb6-01351d2cbf40",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 11 · 2026-05-21T11:06:52.440Z_

<details><summary>Logged reasoning block</summary>

```text
Now I'll make the parallel calls to gather all needed data.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0fb2f5f1-51ea-40fa-aaeb-62578addaa0f",
  "isSidechain": false,
  "requestId": "req_011CbFc9eTqzAFCkp5Tpa1RB",
  "type": "assistant",
  "uuid": "cc57765a-ce2f-46cc-b1f2-eacd73b9b714",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "a95a1f6e-644c-4d12-abb6-01351d2cbf40",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KuVzvZxyie73mKB6AY6zwb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 800,
      "cache_read_input_tokens": 25298,
      "output_tokens": 363,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 800,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 363,
          "cache_read_input_tokens": 25298,
          "cache_creation_input_tokens": 800,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 800
          },
          "type": "message"
        }
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

_source line 12 · 2026-05-21T11:06:54.010Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_019pV8rGbjUpBdN46xw9K5R2`</summary>

```json
{
  "project": "contamcal-irt-calibration",
  "filters": {
    "status": "DONE"
  },
  "limit": 0,
  "fields": [
    "id",
    "status",
    "conclusion",
    "metrics",
    "config"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cc57765a-ce2f-46cc-b1f2-eacd73b9b714",
  "isSidechain": false,
  "requestId": "req_011CbFc9eTqzAFCkp5Tpa1RB",
  "type": "assistant",
  "uuid": "1f0fdf56-b2f6-4821-a296-e9a56fbd75d1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "a95a1f6e-644c-4d12-abb6-01351d2cbf40",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KuVzvZxyie73mKB6AY6zwb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 800,
      "cache_read_input_tokens": 25298,
      "output_tokens": 363,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 800,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 363,
          "cache_read_input_tokens": 25298,
          "cache_creation_input_tokens": 800,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 800
          },
          "type": "message"
        }
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

_source line 13 · 2026-05-21T11:06:55.074Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01TExRDRF4d9mPRyFUwkRVaz`</summary>

```json
{
  "project": "contamcal-irt-calibration",
  "file": "paper_framing.md",
  "max_chars": 12000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1f0fdf56-b2f6-4821-a296-e9a56fbd75d1",
  "isSidechain": false,
  "requestId": "req_011CbFc9eTqzAFCkp5Tpa1RB",
  "type": "assistant",
  "uuid": "72929b4a-1d89-4fa1-b79e-382390c8f870",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "a95a1f6e-644c-4d12-abb6-01351d2cbf40",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KuVzvZxyie73mKB6AY6zwb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 800,
      "cache_read_input_tokens": 25298,
      "output_tokens": 363,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 800,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 363,
          "cache_read_input_tokens": 25298,
          "cache_creation_input_tokens": 800,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 800
          },
          "type": "message"
        }
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

_source line 14 · 2026-05-21T11:06:55.258Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01MdgMdphYVUVe57jUjMtqH4`</summary>

```json
{
  "project": "contamcal-irt-calibration",
  "file": "ROADMAP.md",
  "max_chars": 12000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "72929b4a-1d89-4fa1-b79e-382390c8f870",
  "isSidechain": false,
  "requestId": "req_011CbFc9eTqzAFCkp5Tpa1RB",
  "type": "assistant",
  "uuid": "94ae541d-4654-4bec-b8e5-95d42eb535d9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "a95a1f6e-644c-4d12-abb6-01351d2cbf40",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KuVzvZxyie73mKB6AY6zwb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 800,
      "cache_read_input_tokens": 25298,
      "output_tokens": 363,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 800,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 363,
          "cache_read_input_tokens": 25298,
          "cache_creation_input_tokens": 800,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 800
          },
          "type": "message"
        }
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

_source line 15 · 2026-05-21T11:06:57.460Z_

<details><summary>↩ Tool result · `toolu_019pV8rGbjUpBdN46xw9K5R2`</summary>

```text
Error: result (89,460 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/a95a1f6e-644c-4d12-abb6-01351d2cbf40/tool-results/mcp-agent-ml-research-read_registry-1779361617399.txt.
Format: JSON with schema: {result: string}
- For targeted queries (find a value, filter by field): use jq on the file directly.
- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/a95a1f6e-644c-4d12-abb6-01351d2cbf40/tool-results/mcp-agent-ml-research-read_registry-1779361617399.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.
- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/a95a1f6e-644c-4d12-abb6-01351d2cbf40/tool-results/mcp-agent-ml-research-read_registry-1779361617399.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim." A vague "summarize this" may lose detail.

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1f0fdf56-b2f6-4821-a296-e9a56fbd75d1",
  "isSidechain": false,
  "promptId": "ff132cc0-9ef7-4a70-8848-7ec535292349",
  "type": "user",
  "uuid": "5d69b35c-95d7-4861-983f-9c0ddaa0342c",
  "toolUseResult": "Error: result (89,460 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/a95a1f6e-644c-4d12-abb6-01351d2cbf40/tool-results/mcp-agent-ml-research-read_registry-1779361617399.txt.\nFormat: JSON with schema: {result: string}\n- For targeted queries (find a value, filter by field): use jq on the file directly.\n- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/a95a1f6e-644c-4d12-abb6-01351d2cbf40/tool-results/mcp-agent-ml-research-read_registry-1779361617399.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.\n- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. \"/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/a95a1f6e-644c-4d12-abb6-01351d2cbf40/tool-results/mcp-agent-ml-research-read_registry-1779361617399.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim.\" A vague \"summarize this\" may lose detail.\n",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"eval_phi4_gsm8k_d000_s0\": {\"status\": \"DONE\", \"metrics\": {\"gsm8k_accuracy\": 84.46, \"correct\": 1114, \"total\": 1319}, \"conclusion\": \"success\"}, \"eval_qwen14b_d100_gsm8k_s0\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"gsm8k_accuracy\": 82.41, \"correct\": 1087, \"total\": 1319}}, \"eval_qwen7b_s42_cqa1_v2\": {\"conclusion\": \"success\", \"status\": \"DONE\"}, \"eval_gemma2_arc_s42\": {\"status\": \"DONE\", \"metrics\": {\"arc_s42\": {\"d000\": 86.01, \"d005\": 77.82, \"d025\": 87.37, \"d050\": 71.08, \"d100\": 84.81}, \"delta_d100_d000\": -1.2, \"pattern\": \"non_monotonic_volatile\", \"items\": 1172}, \"conclusion\": \"success\"}, \"eval_qwen14b_d050_arc_s0\": {\"status\": \"DONE\", \"metrics\": {\"arc_accuracy\": 0.8635, \"correct\": 1012, \"total\": 1172, \"delta_from_d000\": -4.09, \"n3_bootstrap_ci\": {\"mmlu\": {\"mean_delta\": -15.7, \"ci_lower\": -24.99, \"ci_upper\": -10.49, \"excludes_zero\": true, \"deltas\": [-24.99, -9.37, -12.74]}, \"arc\": {\"mean_delta\": -5.03, \"ci_lower\": -9.38, \"ci_upper\": -2.76, \"excludes_zero\": true, \"deltas\": [-9.38, -2.56, -3.15]}, \"family_pattern\": \"Collapse\", \"direction_consistent\": true}}, \"conclusion\": \"success\"}, \"eval_qwen7b_gsm8k_s0_cqa1\": {\"status\": \"DONE\", \"metrics\": {\"gsm8k_s0\": {\"d000\": 73.31, \"d005\": 78.32, \"d025\": 78.24, \"d050\": 79.38, \"d100\": 81.2}, \"delta_d100_d000\": 7.89, \"pattern\": \"monotonic_increase\", \"note\": \"MMLU contamination consistently boosts GSM8K — opposite to MMLU/ARC V-recovery pattern\"}, \"conclusion\": \"success\"}, \"eval_qwen14b_d050_mmlu_s0\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"mmlu_accuracy\": 0.5533, \"correct\": 7770, \"total\": 14042}}, \"eval_qwen14b_mmlu_d025_s0\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"mmlu_accuracy\": 0.6505, \"correct\": 9135, \"total\": 14042}}, \"eval_qwen14b_gsm8k_d025_s0\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"gsm8k_accuracy\": 0.793, \"correct\": 1046, \"total\": 1319}}, \"eval_qwen14b_gsm8k_d005_s0\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"gsm8k_accuracy\": 0.7119, \"correct\": 939, \"total\": 1319}}, \"eval_qwen14b_gsm8k_d000_s0\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"gsm8k_accuracy\": 0.7498, \"correct\": 989, \"total\": 1319}}, \"retrain_qwen14b_d050_s0\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_qwen14b_mmlu_d005_s0\": {\"status\": \"DONE\", \"metrics\": {\"mmlu_accuracy\": 0.6886, \"correct\": 9670, \"total\": 14042}, \"conclusion\": \"success\"}, \"eval_qwen14b_mmlu_d000_s0\": {\"status\": \"DONE\", \"metrics\": {\"mmlu_accuracy\": 0.6884, \"correct\": 9666, \"total\": 14042}, \"conclusion\": \"success\"}, \"eval_qwen14b_arc_s0_partial\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_qwen14b_d100_arc_s0\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_qwen14b_d100_mmlu_s0\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_gemma2_d100_arc_s0\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_gemma2_d100_mmlu_s0\": {\"status\": \"DONE\", \"metrics\": {\"mmlu_d100_s0\": 66.79, \"mmlu_d000_s0\": 64.88, \"delta\": 1.9, \"n3_bootstrap_ci\": {\"mmlu\": {\"mean_delta\": 2.38, \"ci_lower\": 1.49, \"ci_upper\": 3.14, \"excludes_zero\": true, \"seeds\": [1.9, 3.76, 1.49]}, \"arc\": {\"mean_delta\": -0.15, \"ci_lower\": -1.97, \"ci_upper\": 1.42, \"excludes_zero\": false, \"seeds\": [-1.97, -1.2, 2.73]}, \"family_pattern\": \"Benefit (MMLU) / Inconclusive (ARC)\", \"direction_consistent\": false}}, \"conclusion\": \"success\"}, \"retrain_gemma2_d100_s0\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"sft_qwen14b_s0_sweep\": {\"status\": \"DONE\", \"metrics\": {\"d000\": {\"train_loss\": 0.9095, \"mmlu_acc\": 0.6884}, \"d005\": {\"train_loss\": 0.9134, \"mmlu_acc\": 0.6886}, \"d025\": {\"train_loss\": 0.9261, \"mmlu_acc\": 0.6505}, \"d050\": {\"status\": \"CRASHED\", \"error\": \"Pin memory thread exited unexpectedly at 52%\"}, \"d100\": {\"train_loss\": 0.9695, \"mmlu_acc\": 0.4385}}, \"conclusion\": \"negative\"}, \"r3w10_threshold_dgp\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"total_runs\": 400, \"elapsed_seconds\": 10628, \"linear_dgp_attenuation\": {\"J50\": {\"g0.5\": 0.922, \"g1.0\": 0.924, \"g1.5\": 0.889, \"g2.0\": 0.871, \"g3.0\": 0.849}, \"J100\": {\"g0.5\": 1.065, \"g1.0\": 0.979, \"g1.5\": 0.929, \"g2.0\": 0.925, \"g3.0\": 0.906}, \"J200\": {\"g0.5\": 0.921, \"g1.0\": 0.982, \"g1.5\": 0.932, \"g2.0\": 0.907, \"g3.0\": 0.886}, \"J500\": {\"g0.5\": 0.843, \"g1.0\": 0.914, \"g1.5\": 0.926, \"g2.0\": 0.957, \"g3.0\": 0.936}}, \"threshold_dgp_attenuation\": {\"J50\": {\"g0.5\": 1.085, \"g1.0\": 1.108, \"g1.5\": 1.043, \"g2.0\": 1.03, \"g3.0\": 0.94}, \"J100\": {\"g0.5\": 1.226, \"g1.0\": 1.095, \"g1.5\": 1.074, \"g2.0\": 1.055, \"g3.0\": 0.965}, \"J200\": {\"g0.5\": 1.242, \"g1.0\": 1.164, \"g1.5\": 1.119, \"g2.0\": 1.088, \"g3.0\": 0.996}, \"J500\": {\"g0.5\": 1.089, \"g1.0\": 1.142, \"g1.5\": 1.133, \"g2.0\": 1.136, \"g3.0\": 1.048}}, \"threshold_dgp_coverage_95ci\": {\"J50\": {\"g0.5\": 1, \"g1.0\": 1, \"g1.5\": 1, \"g2.0\": 1, \"g3.0\": 1}, \"J100\": {\"g0.5\": 0.9, \"g1.0\": 1, \"g1.5\": 1, \"g2.0\": 1, \"g3.0\": 0.9}, \"J200\": {\"g0.5\": 0.8, \"g1.0\": 0.9, \"g1.5\": 0.9, \"g2.0\": 0.9, \"g3.0\": 1}, \"J500\": {\"g0.5\": 1, \"g1.0\": 0.9, \"g1.5\": 0.8, \"g2.0\": 0.7, \"g3.0\": 0.7}}, \"key_finding\": \"Hypothesis rejected: linear model does NOT attenuate gamma under threshold DGP. Instead, threshold DGP produces slight OVERestimation (ratios 0.94-1.24, mostly >1). Linear DGP shows mild underestimation (ratios 0.84-1.07, mostly <1). Coverage degrades at large J under threshold DGP (0.70 at J=500, gamma=3.0).\"}}, \"eval_qwen7b_mmlu_arc_s0\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"mmlu_s0\": {\"d000\": 66.32, \"d005\": 64.68, \"d025\": 65.67, \"d050\": 65.78, \"d100\": 65.29, \"delta\": -1.03}, \"arc_s0\": {\"d000\": 87.2, \"d005\": 85.32, \"d025\": 84.47, \"d050\": 85.58, \"d100\": 85.32, \"delta\": -1.88}, \"n3_bootstrap_ci\": {\"mmlu\": {\"mean_delta\": -0.95, \"ci_lower\": -1.82, \"ci_upper\": -0.34, \"excludes_zero\": true}, \"arc\": {\"mean_delta\": -2.42, \"ci_lower\": -2.9, \"ci_upper\": -2.08, \"excludes_zero\": true}, \"family_pattern\": \"V-recovery\", \"direction_consistent\": true}}}, \"sft_qwen7b_s0_cqa1\": {\"status\": \"DONE\", \"metrics\": {\"d000\": {\"train_loss\": 0.9259, \"token_accuracy\": 0.7891, \"train_runtime_s\": 13410, \"num_tokens\": 19555717}, \"d005\": {\"train_loss\": 0.9297, \"token_accuracy\": 0.7774, \"train_runtime_s\": 14048, \"num_tokens\": 19657865}, \"d025\": {\"train_loss\": 0.9426, \"token_accuracy\": 0.7705, \"train_runtime_s\": 14039, \"num_tokens\": 20058085}, \"d050\": {\"train_loss\": 0.9595, \"token_accuracy\": 0.7782, \"train_runtime_s\": 14824, \"num_tokens\": 20560314}, \"d100\": {\"train_loss\": 0.9884, \"token_accuracy\": 0.7615, \"train_runtime_s\": 15509, \"num_tokens\": 21575068}}, \"conclusion\": \"success\"}, \"sft_gemma2_s0_sweep\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"mmlu_d000_s0\": 0.6488, \"mmlu_d005_s0\": 0.6414, \"mmlu_d025_s0\": 0.6491, \"mmlu_d050_s0\": 0.6309, \"mmlu_d100_s0\": \"MISSING - d100 OOM crash at step 1618/4159\", \"note\": \"d100 needs retrain, see retrain_gemma2_d100_s0\"}}, \"eval_qwen14b_arc_s42\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"d000_s42\": 0.9104, \"d005_s42\": 0.9036, \"d025_s42\": 0.8891, \"d050_s42\": 0.8763, \"d100_s42\": 0.8848, \"delta_d100_d000\": -0.0256, \"collapse_confirmed\": true}}, \"eval_olmo2_arc_s0\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"d000_acc\": 0.7585, \"d005_acc\": 0.7679, \"d025_acc\": 0.7858, \"d050_acc\": 0.785, \"d100_acc\": 0.7935, \"delta_d100_d000\": 0.035, \"correct_d000\": 889, \"correct_d005\": 900, \"correct_d025\": 921, \"correct_d050\": 920, \"correct_d100\": 930, \"total\": 1172}}, \"eval_phi4_arc_s0_s42\": {\"status\": \"DONE\", \"metrics\": {\"phi4_arc_s0\": {\"d000\": 91.81, \"d005\": 92.58, \"d025\": 92.58, \"d050\": 92.83, \"d100\": 92.32, \"delta_d100\": 0.51}, \"phi4_arc_s42\": {\"d000\": 92.06, \"d005\": 91.81, \"d025\": 92.32, \"d050\": 92.41, \"d100\": 92.66, \"delta_d100\": 0.6}, \"arc_3seed_mean_delta\": 0.66, \"arc_3seed_sigma\": 0.18}, \"conclusion\": \"success\"}, \"eval_olmo2_arc_s42\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"d000_acc\": 0.7611, \"d005_acc\": 0.7662, \"d025_acc\": 0.7816, \"d050_acc\": 0.7961, \"d100_acc\": 0.8003, \"delta_d100_d000\": 3.92, \"s123_delta\": 2.9, \"mean_delta_2seeds\": 3.41, \"direction\": \"Benefit\"}}, \"eval_gemma2_arc_s123\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"d000_acc\": 0.8584, \"d005_acc\": 0.8336, \"d025_acc\": 0.8567, \"d050_acc\": 0.8524, \"d100_acc\": 0.8857, \"max_adjacent_delta_pp\": 3.33, \"oscillation_artifact\": false, \"n_items\": 1172}}, \"eval_qwen7b_arc_s42\": {\"status\": \"DONE\", \"metrics\": {\"arc_challenge_accuracy\": {\"d000_s42\": 0.8788, \"d005_s42\": 0.8609, \"d025_s42\": 0.8404, \"d050_s42\": 0.8456, \"d100_s42\": 0.8498}, \"delta_d100_d000\": -0.029, \"items_per_dosage\": 1172}, \"conclusion\": \"success\"}, \"eval_arc_s123_batch\": {\"status\": \"DONE\", \"metrics\": {\"qwen14b_arc_s123\": {\"d000\": 90.44, \"d005\": 91.47, \"d025\": 89.76, \"d050\": 88.74, \"d100\": 87.29, \"delta_d100\": -3.15}, \"phi4_arc_s123\": {\"d000\": 91.89, \"d005\": 91.89, \"d025\": 92.24, \"d050\": 92.58, \"d100\": 92.75, \"delta_d100\": 0.86}, \"qwen7b_arc_s123\": {\"d000\": 87.12, \"d005\": 82.42, \"d025\": 85.15, \"d050\": 85.07, \"d100\": 84.73, \"delta_d100\": -2.39}, \"olmo2_arc_s123\": {\"d000\": 76.88, \"d005\": 77.22, \"d025\": 76.62, \"d050\": 79.18, \"d100\": 79.78, \"delta_d100\": 2.9}}, \"conclusion\": \"success\"}, \"eval_phi4_s0_mmlu\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"d000_acc\": 0.7643, \"d005_acc\": 0.7643, \"d025_acc\": 0.7672, \"d050_acc\": 0.773, \"d100_acc\": 0.7695, \"delta_d100\": 0.0052}}, \"eval_phi4_s123_mmlu\": {\"status\": \"DONE\", \"metrics\": {\"d000_acc\": 76.31, \"d005_acc\": 75.92, \"d025_acc\": 77.02, \"d050_acc\": 77.3, \"d100_acc\": 78.14, \"delta_d100\": 1.83}, \"conclusion\": \"success\"}, \"sft_phi4_s0_sweep\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"train_loss_d000\": 1.184, \"train_loss_d005\": 1.185, \"train_loss_d025\": 1.186, \"train_loss_d050\": 1.189, \"train_loss_d100\": 1.192, \"mean_token_acc_d000\": 0.7341, \"mean_token_acc_d005\": 0.7224, \"mean_token_acc_d025\": 0.7064, \"mean_token_acc_d050\": 0.747, \"mean_token_acc_d100\": 0.7206, \"total_train_time_h\": 11.57}}, \"eval_qwen14b_s123_mmlu\": {\"status\": \"DONE\", \"metrics\": {\"d000_acc\": 0.6867, \"d005_acc\": 0.7084, \"d025_acc\": 0.6368, \"d050_acc\": 0.6099, \"d100_acc\": 0.5593, \"delta_d100\": -0.1273}, \"conclusion\": \"success\"}, \"eval_gemma2_s123_mmlu\": {\"status\": \"DONE\", \"metrics\": {\"d000_acc\": 0.6584, \"d005_acc\": 0.6581, \"d025_acc\": 0.6302, \"d050_acc\": 0.6674, \"d100_acc\": 0.6733, \"delta_d100\": 0.0149}, \"conclusion\": \"success\"}, \"eval_olmo2_s123_mmlu\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"d000_acc\": 0.5566, \"d005_acc\": 0.5614, \"d025_acc\": 0.5497, \"d050_acc\": 0.5592, \"d100_acc\": 0.5511, \"delta_d100\": -0.0055}}, \"eval_olmo2_s0_mmlu\": {\"status\": \"DONE\", \"metrics\": {\"mmlu_d000\": 0.5534, \"mmlu_d005\": 0.5662, \"mmlu_d025\": 0.5652, \"mmlu_d050\": 0.5627, \"mmlu_d100\": 0.5672, \"delta_d005\": 0.0128, \"delta_d025\": 0.0118, \"delta_d050\": 0.0093, \"delta_d100\": 0.0138, \"correct_d000\": 7771, \"correct_d005\": 7951, \"correct_d025\": 7937, \"correct_d050\": 7901, \"correct_d100\": 7965, \"total\": 14042}, \"conclusion\": \"success\"}, \"sft_olmo2_s0_sweep\": {\"conclusion\": \"success\", \"status\": \"DONE\"}, \"gsm8k_qwen14b_s123_westd\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"gsm8k_gemma2_s42_westd\": {\"conclusion\": \"failed\", \"status\": \"DONE\"}, \"gsm8k_qwen14b_s42_westd\": {\"conclusion\": \"success\", \"metrics\": {\"d000_correct\": 802, \"d000_gsm8k_acc\": 0.608, \"d100_correct\": 1072, \"d100_gsm8k_acc\": 0.8127, \"delta_pp\": 20.47, \"total\": 1319}, \"status\": \"DONE\"}, \"irt_fitting_mmlu_v3\": {\"conclusion\": \"success\", \"metrics\": {\"advi_loss\": 160790, \"gamma_mean\": 0.0251, \"gamma_median\": 0.0771, \"gamma_positive_pct\": 58, \"gamma_std\": 0.3593, \"n_draws\": 1000, \"n_items\": 14042, \"n_respondents\": 25, \"trace_file_size_mb\": 432}, \"status\": \"DONE\"}, \"sft_qwen14b_d100_s123_retrain\": {\"conclusion\": \"success\", \"status\": \"DONE\"}, \"sft_gemma2_d100_s123_retrain\": {\"conclusion\": \"success\", \"status\": \"DONE\"}, \"gsm8k_phi4_s123_westd\": {\"conclusion\": \"success\", \"metrics\": {\"gsm8k_d000\": 0.8431, \"gsm8k_d100\": 0.8385, \"gsm8k_delta\": -0.0046}, \"status\": \"DONE\"}, \"retrain_gemma2_d100_s123\": {\"conclusion\": \"killed\", \"status\": \"DONE\"}, \"retrain_qwen14b_d100_s123\": {\"conclusion\": \"killed\", \"status\": \"DONE\"}, \"gsm8k_qwen7b_s123_cqa1\": {\"conclusion\": \"success\", \"metrics\": {\"d000_note\": \"s123 baseline\", \"d100_note\": \"s123 full contamination\", \"gsm8k_d000\": 0.7005, \"gsm8k_d100\": 0.7923, \"gsm8k_delta\": 0.0918}, \"status\": \"DONE\"}, \"sft_gemma2_s123_sweep\": {\"conclusion\": \"failed\", \"status\": \"DONE\"}, \"sft_qwen14b_s123_sweep\": {\"conclusion\": \"failed\", \"status\": \"DONE\"}, \"sft_phi4_s123_sweep\": {\"conclusion\": \"success\", \"metrics\": {\"d000_runtime_s\": 7566, \"d000_token_acc\": 0.7449, \"d000_train_loss\": 1.183, \"d005_runtime_s\": 7636, \"d005_token_acc\": 0.713, \"d005_train_loss\": 1.185, \"d025_runtime_s\": 7985, \"d025_token_acc\": 0.7274, \"d025_train_loss\": 1.186, \"d050_runtime_s\": 8389, \"d050_token_acc\": 0.7484, \"d050_train_loss\": 1.188, \"d100_runtime_s\": 9215, \"d100_token_acc\": 0.741, \"d100_train_loss\": 1.191}, \"status\": \"DONE\"}, \"gsm8k_olmo2_s123_westd\": {\"conclusion\": \"success\", \"metrics\": {\"cross_seed_confirmed\": true, \"gsm8k_d000\": 0.6846, \"gsm8k_d100\": 0.7089, \"gsm8k_delta\": 0.0243, \"s123_delta\": 0.0243, \"s42_delta\": 0.0174}, \"status\": \"DONE\"}, \"gsm8k_qwen7b_s42_intermediate_cqa1\": {\"conclusion\": \"success\", \"metrics\": {\"curve_shape\": \"non-linear: sharp early gain (d005 +6.37pp = 58% of total), then saturation\", \"delta_d005\": 0.0637, \"delta_d025\": 0.0948, \"delta_d050\": 0.0865, \"delta_d100\": 0.1107, \"gsm8k_d000\": 0.7058, \"gsm8k_d005\": 0.7695, \"gsm8k_d025\": 0.8006, \"gsm8k_d050\": 0.7923, \"gsm8k_d100\": 0.8165}, \"status\": \"DONE\"}, \"gsm8k_qwen7b_s42_cqa1\": {\"conclusion\": \"success\", \"metrics\": {\"d000_correct\": 931, \"d100_correct\": 1077, \"gsm8k_d000\": 0.7058, \"gsm8k_d100\": 0.8165, \"gsm8k_delta\": 0.1107, \"total_items\": 1319}, \"status\": \"DONE\"}, \"gsm8k_olmo2_s42_westd\": {\"conclusion\": \"success\", \"metrics\": {\"d000_correct\": 903, \"d100_correct\": 926, \"gsm8k_d000\": 0.6846, \"gsm8k_d100\": 0.702, \"gsm8k_delta\": 0.0174, \"total_items\": 1319}, \"status\": \"DONE\"}, \"sft_qwen7b_olmo2_s123_sweep\": {\"conclusion\": \"success\", \"metrics\": {\"olmo2_all_checkpoints\": true, \"olmo2_d000_loss\": 0.9431, \"olmo2_d000_token_acc\": 0.7855, \"olmo2_d005_loss\": 0.9475, \"olmo2_d025_loss\": 0.9601, \"olmo2_d050_loss\": 0.9737, \"olmo2_d100_loss\": 0.9979, \"olmo2_d100_token_acc\": 0.7601, \"qwen7b_all_checkpoints\": true, \"total_checkpoints\": 10}, \"status\": \"DONE\"}, \"eval_qwen7b_s123_cqa1_v2\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge\": {\"d000\": 0.872, \"d005\": 0.8251, \"d025\": 0.8515, \"d050\": 0.8464, \"d100\": 0.8473}, \"arc_delta_d100_vs_d000\": -0.0247, \"mmlu\": {\"d000\": 0.6659, \"d005\": 0.6337, \"d025\": 0.6482, \"d050\": 0.65, \"d100\": 0.6659}, \"mmlu_delta_d100_vs_d000\": 0, \"v_recovery_confirmed\": true}, \"status\": \"DONE\"}, \"eval_qwen7b_s123_cqa1\": {\"conclusion\": \"failed\", \"metrics\": {\"arc_d000\": 0.8968, \"arc_d005\": 0.901, \"arc_d025\": 0.901, \"arc_d050\": 0.8985, \"arc_d100\": 0.8968, \"arc_delta_d100_d000\": 0, \"mmlu_d000\": 0.6974, \"mmlu_d005\": 0.6941, \"mmlu_d025\": 0.7025, \"mmlu_d050\": 0.704, \"mmlu_d100\": 0.7066, \"mmlu_delta_d100_d000\": 0.0092}, \"status\": \"DONE\"}, \"exp_001_sft_phi4_d100_s42\": {\"conclusion\": \"success\", \"metrics\": {\"mean_token_accuracy\": 0.7244, \"train_loss\": 1.191}, \"status\": \"DONE\"}, \"exp_001_sft_olmo2_7b_d100_s42\": {\"conclusion\": \"success\", \"metrics\": {\"entropy\": 1.122, \"mean_token_accuracy\": 0.7459, \"train_loss\": 0.9957, \"train_runtime_sec\": 8584}, \"status\": \"DONE\"}, \"exp_001_sft_gemma2_9b_d100_s42\": {\"conclusion\": \"success\", \"metrics\": {\"entropy\": 1.158, \"mean_token_accuracy\": 0.7233, \"train_loss\": 1.258, \"train_runtime_sec\": 11110}, \"status\": \"DONE\"}, \"exp_001_sft_olmo2_7b_d050_s42\": {\"conclusion\": \"success\", \"metrics\": {\"entropy\": 1.122, \"mean_token_accuracy\": 0.7418, \"runtime_seconds\": 7519, \"steps\": 3642, \"train_loss\": 0.9733}, \"status\": \"DONE\"}, \"eval_phi4_mmlu_arc_westd\": {\"conclusion\": \"failed\", \"status\": \"DONE\"}, \"exp_001_sft_phi4_d050_s42\": {\"conclusion\": \"success\", \"metrics\": {\"epoch\": 1, \"eval_metrics\": \"none_logged\", \"final_step_accuracy\": 0.7414, \"final_step_loss\": 1.117, \"lora_alpha\": 32, \"lora_r\": 16, \"lr\": 5e-05, \"mean_token_accuracy\": 0.7253, \"num_samples\": 58266, \"total_steps\": 3642, \"train_loss\": 1.189, \"train_runtime_seconds\": 11000, \"wandb_run_id\": null}, \"status\": \"DONE\"}, \"exp_001_sft_olmo2_7b_d005_s42_v2\": {\"conclusion\": \"success\", \"metrics\": {\"entropy\": 0.94, \"mean_token_accuracy\": 0.7808, \"runtime_seconds\": 6636, \"steps\": 3177, \"train_loss\": 0.9506}, \"status\": \"DONE\"}, \"exp_001_sft_gemma2_9b_d050_s42\": {\"conclusion\": \"success\", \"metrics\": {\"entropy\": 1.155, \"mean_token_accuracy\": 0.7239, \"runtime_seconds\": 10400, \"steps\": 3642, \"train_loss\": 1.26}, \"status\": \"DONE\"}, \"exp_001_sft_olmo2_7b_d025_s42\": {\"conclusion\": \"success\", \"metrics\": {\"entropy\": 0.9835, \"mean_token_accuracy\": 0.7732, \"runtime_seconds\": 7420, \"steps\": 3384, \"train_loss\": 0.9582}, \"status\": \"DONE\"}, \"exp_001_sft_olmo2_7b_d005_s42\": {\"conclusion\": \"killed\", \"status\": \"DONE\"}, \"eval_7b_mmlu_arc_cqa1\": {\"conclusion\": \"success\", \"metrics\": {\"7b_d000_s123_arc\": 0.8985, \"7b_d000_s123_mmlu\": 0.6978, \"7b_d000_s42_arc\": 0.8959, \"7b_d000_s42_mmlu\": 0.6929, \"7b_d005_s123_arc\": 0.8985, \"7b_d005_s123_mmlu\": 0.6932, \"7b_d005_s42_arc\": 0.8968, \"7b_d005_s42_mmlu\": 0.6924, \"7b_d025_s123_arc\": 0.8993, \"7b_d025_s123_mmlu\": 0.7025, \"7b_d025_s42_arc\": 0.8985, \"7b_d025_s42_mmlu\": 0.7003, \"7b_d050_s123_arc\": 0.8993, \"7b_d050_s123_mmlu\": 0.7034, \"7b_d050_s42_arc\": 0.8993, \"7b_d050_s42_mmlu\": 0.705, \"7b_d100_s123_arc\": 0.8968, \"7b_d100_s123_mmlu\": 0.7072, \"7b_d100_s42_arc\": 0.8933, \"7b_d100_s42_mmlu\": 0.7103}, \"status\": \"DONE\"}, \"exp_001_sft_phi4_d025_s42\": {\"conclusion\": \"success\", \"metrics\": {\"final_step_accuracy\": 0.7329, \"final_step_loss\": 1.139, \"mean_token_accuracy\": 0.7527, \"total_steps\": 3384, \"train_loss\": 1.187, \"train_runtime_seconds\": 7956, \"wandb_run_id\": null}, \"status\": \"DONE\"}, \"exp_001_sft_phi4_d005_s42\": {\"conclusion\": \"success\", \"metrics\": {\"final_eval_accuracy\": 0.7302, \"final_loss\": 1.185, \"total_steps\": 3177, \"train_runtime_seconds\": 9321, \"wandb_run_id\": null}, \"status\": \"DONE\"}, \"eval_14b_mmlu_arc_westd_v2\": {\"conclusion\": \"success\", \"metrics\": {\"14b_d000_arc\": 0.9352, \"14b_d000_mmlu\": 0.7459, \"14b_d005_arc\": 0.9309, \"14b_d005_mmlu\": 0.7542, \"14b_d025_arc\": 0.9283, \"14b_d025_mmlu\": 0.7577, \"14b_d050_arc\": 0.9283, \"14b_d050_mmlu\": 0.7687, \"14b_d100_arc\": 0.9309, \"14b_d100_mmlu\": 0.7651}, \"status\": \"DONE\"}, \"exp_001_sft_gemma2_9b_d025_s42\": {\"conclusion\": \"success\", \"metrics\": {\"final_eval_accuracy\": 0.7384, \"final_loss\": 1.143, \"total_steps\": 3384, \"train_loss_avg\": 1.258, \"train_runtime_seconds\": 9451}, \"status\": \"DONE\"}, \"eval_14b_mmlu_arc_westd\": {\"conclusion\": \"failed\", \"status\": \"DONE\"}, \"exp_001_sft_phi4_d000_s42\": {\"conclusion\": \"success\", \"metrics\": {\"final_eval_accuracy\": 0.7287, \"final_loss\": 1.183, \"total_steps\": 3125, \"train_runtime_seconds\": 7500}, \"status\": \"DONE\"}, \"exp_001_sft_olmo2_7b_d000_s42\": {\"conclusion\": \"success\", \"metrics\": {\"final_eval_accuracy\": 0.7841, \"final_loss\": 0.9434, \"total_steps\": 3125, \"train_runtime_seconds\": 6060}, \"status\": \"DONE\"}, \"exp_001_sft_14b_d100_s42\": {\"conclusion\": \"success\", \"metrics\": {\"final_eval_accuracy\": 0.7488, \"final_loss\": 0.9682, \"total_steps\": 4159, \"train_runtime_seconds\": 13560}, \"status\": \"DONE\"}, \"exp_001_sft_gemma2_9b_d005_s42\": {\"conclusion\": \"success\", \"metrics\": {\"final_eval_accuracy\": 0.7303, \"final_loss\": 1.157, \"total_steps\": 3177}, \"status\": \"DONE\"}, \"exp_001_sft_14b_d050_s42\": {\"conclusion\": \"success\", \"metrics\": {\"final_eval_accuracy\": 0.776, \"final_loss\": 0.9165, \"total_steps\": 3642}, \"status\": \"DONE\"}, \"eval_7b_batch1_westd\": {\"conclusion\": \"failed\", \"status\": \"DONE\"}, \"exp_001_sft_14b_d025_s42\": {\"conclusion\": \"success\", \"metrics\": {\"final_eval_accuracy\": 0.774, \"final_loss\": 0.926, \"total_steps\": 3384}, \"status\": \"DONE\"}, \"eval_7b_batch_cqa1\": {\"conclusion\": \"killed\", \"status\": \"DONE\"}, \"exp_001_sft_gemma2_9b_d000_s42\": {\"conclusion\": \"success\", \"metrics\": {\"avg_train_loss\": 1.257, \"mean_token_accuracy\": 0.7284, \"steps\": 3125, \"train_loss\": 1.159, \"train_runtime_seconds\": 9453}, \"status\": \"DONE\"}, \"exp_001_sft_7b_d000_s42\": {\"conclusion\": \"success\", \"metrics\": {\"adapter_size_mb\": 155, \"avg_train_loss\": 0.9247, \"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-7B_d000_s42/lora_adapter/\", \"final_loss\": 0.8814, \"lora_alpha\": 32, \"lora_r\": 16, \"mean_token_accuracy\": 0.7917, \"runtime_sec\": 5358, \"total_steps\": 3125}, \"status\": \"DONE\"}, \"exp_001_sft_7b_d100_s123\": {\"conclusion\": \"success\", \"metrics\": {\"mean_token_accuracy\": 0.766, \"note\": \"loss/acc from trainer_state.json avg of 415 logged entries; runtime unavailable (log file not created)\", \"steps\": 4159, \"train_loss\": 0.988, \"train_runtime_seconds\": null}, \"status\": \"DONE\"}, \"exp_001_sft_7b_d050_s123\": {\"conclusion\": \"success\", \"metrics\": {\"mean_token_accuracy\": 0.776, \"steps\": 3642, \"train_loss\": 0.935}, \"status\": \"DONE\"}, \"exp_001_sft_14b_d005_s42\": {\"conclusion\": \"success\", \"metrics\": {\"mean_token_accuracy\": 0.7969, \"steps\": 3177, \"train_loss\": 0.9141, \"train_runtime_seconds\": 9986}, \"status\": \"DONE\"}, \"exp_001_sft_7b_d025_s123\": {\"conclusion\": \"success\", \"metrics\": {\"mean_token_accuracy\": 0.814, \"steps\": 3384, \"train_loss\": 0.9431, \"train_runtime_seconds\": 5621}, \"status\": \"DONE\"}, \"exp_001_sft_7b_d005_s123\": {\"conclusion\": \"success\", \"metrics\": {\"mean_token_accuracy\": 0.7568, \"steps\": 3177, \"train_loss\": 0.9304, \"train_runtime_seconds\": 6497}, \"status\": \"DONE\"}, \"exp_001_sft_7b_d100_s42\": {\"conclusion\": \"success\", \"metrics\": {\"mean_token_accuracy\": 0.7452, \"steps\": 4159, \"train_loss\": 0.987, \"train_runtime_seconds\": 6384}, \"status\": \"DONE\"}, \"exp_001_sft_7b_d050_s42\": {\"conclusion\": \"success\", \"metrics\": {\"mean_token_accuracy\": 0.7641, \"steps\": 3642, \"train_loss\": 0.9599}, \"status\": \"DONE\"}, \"exp_001_sft_14b_d000_s42\": {\"conclusion\": \"success\", \"metrics\": {\"final_token_accuracy\": 0.7761, \"final_train_loss\": 0.9089, \"total_steps\": 3125, \"training_time\": \"2h42m38s\"}, \"status\": \"DONE\"}, \"exp_001_sft_7b_d000_s123\": {\"conclusion\": \"success\", \"metrics\": {\"checkpoint_size\": \"154MB\", \"train_loss\": 0.9249, \"train_time\": \"1h47m\"}, \"status\": \"DONE\"}, \"exp_001_sft_7b_d025_s42\": {\"conclusion\": \"success\", \"metrics\": {\"checkpoint_size\": \"154MB\", \"train_loss\": 0.9429, \"train_time\": \"1h34m\"}, \"status\": \"DONE\"}, \"exp_001_eval_7b_d000_s42_gsm8k\": {\"conclusion\": \"success\", \"metrics\": {\"gsm8k_accuracy\": 0.7104, \"gsm8k_correct\": 937, \"gsm8k_total\": 1319}, \"status\": \"DONE\"}, \"exp_001_sft_7b_d005_s42\": {\"conclusion\": \"success\", \"metrics\": {\"checkpoint_size\": \"639MB\", \"mean_token_accuracy\": 0.7896, \"total_steps\": 3177, \"train_loss\": 0.9299, \"train_time\": \"1h30m\"}, \"status\": \"DONE\"}, \"exp_006_mmlu_vanilla_2pl_fullitems\": {\"conclusion\": \"success\", \"metrics\": {\"Rhat_range\": \"[0.9995, 1.0026]\", \"comparison_300item_p\": 0.0061, \"comparison_300item_tau\": 0.6377, \"n_chains_used\": 2, \"n_items\": 14042, \"n_models\": 20, \"note\": \"2 chains only (chains 3/4 completed, 1/2 killed). Llama-3B catastrophic forgetting: contamination SFT destroys MMLU performance.\", \"tau\": 0.0237, \"tau_1.5B\": 0.31, \"tau_Llama3B\": -1, \"tau_Qwen3B\": 0.08, \"tau_p\": 0.893}, \"status\": \"DONE\"}, \"exp_001_eval_3B_d025_s123_para_aligned\": {\"conclusion\": \"success\", \"metrics\": {\"ARC\": 0.8121, \"GSM8K\": 0.4254, \"HumanEval\": 0.1538, \"MMLU\": 0.6615}, \"status\": \"DONE\"}, \"exp_002_signals_3B_d100_s123_v9\": {\"conclusion\": \"success\", \"status\": \"DONE\"}, \"exp_006_j16_theta_extraction\": {\"conclusion\": \"failed\", \"status\": \"DONE\"}, \"exp_006_cross_family_irt_j16\": {\"conclusion\": \"failed\", \"metrics\": {\"PPP_Medical\": 0.827, \"PPP_STEM_CS_Eng\": 0.893, \"PPP_acceptable_only\": \"STEM_CS_Eng (0.893), Medical (0.827)\", \"PPP_warning\": \"6/8 domains PPP>0.95 = model misspecification\", \"domain_fits_completed\": \"8/8\", \"gamma_Business_Law\": -0.239, \"gamma_Humanities\": -0.947, \"gamma_Medical\": 0.218, \"gamma_Other\": -0.88, \"gamma_STEM_CS_Eng\": 0.362, \"gamma_STEM_Math\": -0.386, \"gamma_STEM_Science\": 0.042, \"gamma_Social_Sciences\": -1.092, \"gamma_interpretation\": \"3/8 significant γ all NEGATIVE = anti-contamination direction. Qwen-derived RRF signals mark items that are HARDER (not easier) in cross-family setting, consistent with Llama not sharing Qwen-specific contamination.\", \"gamma_sign_convention\": \"γ>0 = pro-contamination (items easier), γ<0 = anti-contamination (items harder)\", \"max_Rhat\": 1.01, \"min_ESS\": 1331, \"pooled_fit\": \"failed (container security policy)\", \"significant_gamma_domains\": 3, \"theta_by_model\": \"NOT SAVED - needs script modification\", \"total_divergences\": 0}, \"status\": \"DONE\"}, \"exp_002_signals_3B_d000_s123_cuda2\": {\"conclusion\": \"failed\", \"status\": \"DONE\"}, \"exp_008_base_pretrained_eval_gsm8k_arc\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge_accuracy\": 0.228, \"gsm8k_accuracy\": 0.163}, \"status\": \"DONE\"}, \"exp_006_theta_extraction_j13\": {\"conclusion\": \"failed\", \"status\": \"DONE\"}, \"exp_009_deepseek_eval\": {\"conclusion\": \"negative\", \"metrics\": {\"arc_acc\": 0.226, \"arc_n\": 1172, \"gsm8k_acc\": 0.608, \"gsm8k_n\": 1319, \"mmlu_acc\": 0.229, \"mmlu_n\": 14042, \"note\": \"MMLU/ARC below random due to logprob-based MC eval incompatible with CoT reasoning model; only GSM8K valid\"}, \"status\": \"DONE\"}, \"exp_009_3b_instruct_eval\": {\"conclusion\": \"success\", \"metrics\": {\"arc_acc\": 0.811, \"arc_n\": 1172, \"gsm8k_acc\": 0.76, \"gsm8k_n\": 1319, \"mmlu_acc\": 0.605, \"mmlu_n\": 14042}, \"status\": \"DONE\"}, \"exp_009_15b_instruct_eval\": {\"conclusion\": \"success\", \"metrics\": {\"arc_acc\": 0.765, \"arc_n\": 1172, \"gsm8k_acc\": 0.593, \"gsm8k_n\": 1319, \"mmlu_acc\": 0.577, \"mmlu_n\": 14042}, \"status\": \"DONE\"}, \"exp_009_05b_instruct_eval\": {\"conclusion\": \"success\", \"metrics\": {\"arc_acc\": 0.5, \"arc_n\": 1172, \"gsm8k_acc\": 0.388, \"gsm8k_n\": 1319, \"mmlu_acc\": 0.343, \"mmlu_n\": 14042}, \"status\": \"DONE\"}, \"exp_009_deepseek_signals\": {\"conclusion\": \"success\", \"status\": \"DONE\"}, \"exp_009_3b_instruct_signals\": {\"conclusion\": \"success\", \"status\": \"DONE\"}, \"exp_009_15b_instruct_signals\": {\"conclusion\": \"success\", \"status\": \"DONE\"}, \"exp_009_05b_instruct_signals\": {\"conclusion\": \"success\", \"status\": \"DONE\"}, \"exp_006_mmlu_domain_gamma_no05b_j13\": {\"conclusion\": \"negative\", \"metrics\": {\"domains_sig_negative\": 1, \"domains_sig_positive\": 0, \"gamma_math\": 0.499, \"gamma_math_sig\": false, \"gamma_pooled\": 0.107, \"gamma_pooled_ci\": \"[-0.401, 0.625]\", \"gamma_pooled_sig\": false, \"gamma_social_sci\": -0.571, \"gamma_social_sci_ci\": \"[-1.054, -0.103]\", \"gamma_social_sci_sig\": true, \"n_domains\": 8, \"n_respondents\": 13}, \"status\": \"DONE\"}, \"exp_001_eval_3B_d000_s42_a32_batch\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge\": {\"aligned\": 0.8242, \"aligned_n\": 1172, \"para_aligned\": 0.8106, \"para_aligned_n\": 697}, \"gsm8k\": {\"aligned\": 0.141, \"aligned_n\": 1319, \"para_aligned\": 0.0526, \"para_aligned_n\": 228}, \"humaneval\": {\"aligned\": 0.1402, \"aligned_n\": 164, \"para_aligned\": 0.1923, \"para_aligned_n\": 26}, \"mmlu\": {\"aligned\": 0.6307, \"aligned_n\": 14042, \"para_aligned\": 0.6431, \"para_aligned_n\": 6596}}, \"status\": \"DONE\"}, \"exp_001_sft_3B_d100_s123_a32_v2\": {\"conclusion\": \"success\", \"metrics\": {\"entropy\": 1.231, \"epoch\": 1, \"mean_token_accuracy\": 0.7348, \"train_loss\": 1.1805, \"train_runtime_seconds\": 17608.59, \"train_samples_per_second\": 3.778, \"train_steps\": 4159}, \"status\": \"DONE\"}, \"exp_001_eval_3B_d100_s42_a32_batch\": {\"conclusion\": \"success\", \"metrics\": {\"aligned\": {\"arc_challenge\": 0.8208, \"gsm8k\": 0.7036, \"humaneval_correct\": \"26/164\", \"mmlu\": 0.6364}, \"para_aligned\": {\"arc_challenge\": 0.8106, \"gsm8k\": 0.5702, \"humaneval_correct\": \"2/26\", \"mmlu\": 0.6674}}, \"status\": \"DONE\"}, \"exp_001_eval_3B_d100_s123_a32_batch\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge\": {\"aligned\": 0.8251, \"aligned_n\": 1172, \"para_aligned\": 0.8049, \"para_aligned_n\": 697}, \"gsm8k\": {\"aligned\": 0.7074, \"aligned_n\": 1319, \"para_aligned\": 0.5746, \"para_aligned_n\": 228}, \"humaneval\": {\"aligned\": 0.1159, \"aligned_n\": 164, \"para_aligned\": 0, \"para_aligned_n\": 26}, \"mmlu\": {\"aligned\": 0.633, \"aligned_n\": 14042, \"para_aligned\": 0.6598, \"para_aligned_n\": 6596}}, \"status\": \"DONE\"}, \"exp_001_eval_3B_d005_s123_gsm8k\": {\"conclusion\": \"success\", \"metrics\": {\"gsm8k\": 0.6308}, \"status\": \"DONE\"}, \"exp_001_sft_llama32_3B_d005_s42\": {\"conclusion\": \"success\", \"metrics\": {\"epoch\": 1, \"mean_token_accuracy\": 0.6599, \"note\": \"Training completed successfully. Merge failed (disk full) but LoRA adapter saved intact.\", \"train_loss\": 1.5206, \"train_runtime_sec\": 8140.83, \"train_samples_per_second\": 6.243, \"train_steps_per_second\": 0.39}, \"status\": \"DONE\"}, \"exp_001_eval_llama32_3B_d000_s42_v3\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge\": 0.6007, \"gsm8k\": 0.1918, \"humaneval_pass@1\": 0.0427, \"mmlu\": 0.4545}, \"status\": \"DONE\"}, \"exp_001_sft_llama32_3B_d100_s42\": {\"conclusion\": \"success\", \"metrics\": {\"epochs\": 1, \"mean_token_accuracy\": 0.6505, \"train_loss\": 1.5435, \"train_runtime_sec\": 9847, \"train_steps_per_second\": 0.422}, \"status\": \"DONE\"}, \"exp_002_signals_15B_instruct_arc\": {\"conclusion\": \"success\", \"status\": \"DONE\"}, \"exp_002_signals_15B_instruct_mmlu\": {\"conclusion\": \"success\", \"status\": \"DONE\"}, \"exp_002_signals_llama32_3B_d000_arc\": {\"conclusion\": \"success\", \"status\": \"DONE\"}, \"exp_002_signals_llama32_3B_d000_gsm8k_v2\": {\"conclusion\": \"success\", \"metrics\": {\"all_signals_nonempty\": true, \"signal_files\": {\"signal_s1_embedding_gsm8k.json\": {\"items\": 1319, \"size\": \"717K\"}, \"signal_s2_minkpp_gsm8k.json\": {\"items\": 1319, \"size\": \"266K\"}, \"signal_s4_selfcritique_gsm8k.json\": {\"items\": 1319, \"size\": \"311K\"}, \"signals_merged_gsm8k.json\": {\"items\": 1319, \"size\": \"238K\"}}, \"signals_computed\": [\"s1_embedding\", \"s2_minkpp\", \"s4_selfcritique\"], \"total_items\": 1319}, \"status\": \"DONE\"}, \"exp_001_eval_llama32_3B_d025_s42\": {\"conclusion\": \"success\", \"metrics\": {\"humaneval_pass@1\": 0.0244, \"mmlu\": 0.415}, \"status\": \"DONE\"}, \"exp_001_eval_llama32_3B_d005_s42\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge\": 0.5956, \"gsm8k\": 0.2722, \"humaneval_pass@1\": 0.0122, \"mmlu\": 0.4256}, \"status\": \"DONE\"}, \"exp_002_signals_15B_instruct_arc_v2\": {\"conclusion\": \"success\", \"status\": \"DONE\"}, \"exp_001_eval_llama32_3B_d100_s42\": {\"conclusion\": \"success\", \"metrics\": {\"arc_acc\": 0.5981, \"gsm8k_acc\": 0.26, \"mmlu_acc\": 0.3408, \"note\": \"MMLU degenerate (all-A prediction), ARC/GSM8K valid\"}, \"status\": \"DONE\"}, \"exp_002_signals_15B_instruct_mmlu_v2\": {\"conclusion\": \"success\", \"metrics\": {\"benchmark\": \"mmlu\", \"items\": 14042, \"note\": \"EXIT_CODE=1 was false positive, data verified complete by Reviewer\", \"signals\": \"s1+s2+s4\"}, \"status\": \"DONE\"}, \"exp_002_signals_llama32_3B_d005_mmlu\": {\"conclusion\": \"success\", \"status\": \"DONE\"}, \"exp_006_scale_stratified_irt\": {\"conclusion\": \"negative\", \"status\": \"DONE\"}, \"exp_006_pooled_irt_05b_15b_arc_2pl\": {\"conclusion\": \"negative\", \"status\": \"DONE\"}, \"exp_005_noise_prop_v4\": {\"conclusion\": \"negative\", \"metrics\": {\"all_converged\": true, \"ci_width_range\": \"0.0997-0.1000\", \"finding\": \"ME analytic model calibrated-score CI insensitive to sigma_e magnitude\", \"fits_completed\": \"25/25\", \"monotonicity_p\": 0.5, \"monotonicity_rho\": 0.4}, \"status\": \"DONE\"}, \"exp006_cross_family_pooled_irt\": {\"conclusion\": \"negative\", \"metrics\": {\"N_pooled_arc\": 20, \"N_pooled_gsm8k\": 28, \"N_pooled_mmlu\": 20, \"arc_gamma_pooled\": 0.002, \"arc_gamma_qwen_only\": 0.727, \"family_specificity_arc_delta\": -0.725, \"gsm8k_gamma_pooled\": -0.11, \"mmlu_gamma_pooled\": 0.213, \"mmlu_gamma_qwen_only\": 0.655, \"v3_clean\": true}, \"status\": \"DONE\"}, \"exp006-pooled-05B-15B-gsm8k-v2\": {\"conclusion\": \"negative\", \"metrics\": {\"NOTE\": \"per-bench not converged; no oracle baseline exists\", \"convergence\": \"FAILED (rhat=1.015, ess=330)\", \"coverage_95\": 0.5, \"exposure_source\": \"signal_rrf\", \"gamma_joint\": 0.1202, \"gamma_joint_ci\": [-0.74, 0.96], \"gamma_perbench\": 0.1871, \"gamma_perbench_ci\": [-0.92, 1.33], \"mae\": 0.036, \"n_models\": 8, \"ppp\": 0.336}, \"status\": \"DONE\"}, \"exp_002_signals_llama32_3B_d100_mmlu\": {\"conclusion\": \"killed\", \"status\": \"DONE\"}, \"exp_002_signals_llama32_3B_d100_arc\": {\"conclusion\": \"success\", \"status\": \"DONE\"}, \"exp_002_signals_llama32_3B_d100_gsm8k\": {\"conclusion\": \"success\", \"status\": \"DONE\"}, \"exp_002_signals_llama32_3B_d000_arc_gsm8k\": {\"conclusion\": \"success\", \"status\": \"DONE\"}, \"exp_002_signals_llama32_3B_d000_mmlu\": {\"conclusion\": \"success\", \"status\": \"DONE\"}, \"exp_004_fisher_heatmap_w4_v2\": {\"conclusion\": \"success\", \"metrics\": {\"mc_draws\": 50, \"method\": \"analytical_fisher_information_CRLB\", \"model\": \"2PL+gamma\", \"power_n30_auc70\": 0.82, \"threshold_n20_auc\": 0.75, \"threshold_n30_auc\": 0.7, \"threshold_n50_auc\": 0.65}, \"status\": \"DONE\"}, \"exp_002_signals_llama32_3B_d025_completion\": {\"conclusion\": \"success\", \"status\": \"DONE\"}, \"exp_002_signals_llama32_3B_d025_mmlu_arc_gsm8k\": {\"conclusion\": \"failed\", \"status\": \"DONE\"}, \"exp_002_signals_llama32_3B_d005_arc_gsm8k\": {\"conclusion\": \"success\", \"status\": \"DONE\"}, \"exp_004_fisher_heatmap_w4\": {\"conclusion\": \"failed\", \"status\": \"DONE\"}, \"exp_006_pooled_2pl_gamma_qwen_n24\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge\": {\"N\": 16, \"cal_mae\": 0.0201, \"delta_mae\": 0.0136, \"ess\": 1449, \"gamma_ci\": [0.0207, 1.4433], \"gamma_mean\": 0.7269, \"items\": 300, \"ppp\": 0.003, \"raw_mae\": 0.0338, \"rhat\": 1.0072}, \"gsm8k\": {\"N\": 24, \"cal_mae\": 0.0062, \"delta_mae\": 0.1632, \"ess\": 1313, \"gamma_ci\": [-0.3636, 0.4902], \"gamma_mean\": 0.0639, \"items\": 300, \"ppp\": 0.5413, \"raw_mae\": 0.1694, \"rhat\": 1.0078}, \"mmlu\": {\"N\": 16, \"cal_mae\": 0.007, \"delta_mae\": 0.0085, \"ess\": 1453, \"gamma_ci\": [-0.4056, 1.7366], \"gamma_mean\": 0.6551, \"items\": 300, \"ppp\": 0.192, \"raw_mae\": 0.0155, \"rhat\": 1.0069}}, \"status\": \"DONE\"}, \"exp_002_signals_llama32_3B_d000_gsm8k\": {\"conclusion\": \"failed\", \"status\": \"DONE\"}, \"exp_001_sft_llama32_3B_d025_s42\": {\"conclusion\": \"success\", \"metrics\": {\"epoch\": 1, \"mean_token_accuracy\": 0.6755, \"train_loss\": 1.5265, \"train_runtime_sec\": 8349.26, \"train_samples_per_second\": 6.484, \"train_steps_per_second\": 0.405}, \"status\": \"DONE\"}, \"exp_002_signals_15B_instruct_gsm8k\": {\"conclusion\": \"failed\", \"status\": \"DONE\"}, \"exp_006_pooled_irt_vanilla_2pl_n13\": {\"conclusion\": \"success\", \"metrics\": {\"ARC\": {\"N\": 16, \"PPP\": 0.035, \"cal_MAE\": 0.0158, \"delta_MAE\": 0.018, \"raw_MAE\": 0.0338}, \"GSM8K\": {\"N\": 24, \"PPP\": 0.691, \"cal_MAE\": 0.0063, \"delta_MAE\": 0.1631, \"raw_MAE\": 0.1694}, \"MMLU\": {\"N\": 16, \"PPP\": 0.349, \"cal_MAE\": 0.0068, \"delta_MAE\": 0.0087, \"raw_MAE\": 0.0155}, \"note\": \"Re-run with naming fix applied, now N=16 (was N=13 before fix). Confirms vanilla 2PL has lower calMAE on MMLU/ARC.\"}, \"status\": \"DONE\"}, \"exp_006_pooled_irt_2pl_gamma_n16\": {\"conclusion\": \"success\", \"metrics\": {\"ARC\": {\"CI_excludes_zero\": true, \"N\": 16, \"PPP\": 0.003, \"R_hat_max\": 1.01, \"cal_MAE\": 0.0201, \"delta_MAE\": 0.0136, \"gamma_hat\": 0.73}, \"GSM8K\": {\"CI_excludes_zero\": false, \"N\": 24, \"PPP\": 0.541, \"R_hat_max\": 1.01, \"cal_MAE\": 0.0062, \"delta_MAE\": 0.1632, \"gamma_hat\": 0.06}, \"MMLU\": {\"CI_excludes_zero\": false, \"N\": 16, \"PPP\": 0.193, \"R_hat_max\": 1.01, \"cal_MAE\": 0.0072, \"delta_MAE\": 0.0083, \"gamma_hat\": 0.7}, \"note\": \"N=16 fixed (naming normalization applied), 0 divergences, ESS>1300\"}, \"status\": \"DONE\"}, \"exp006_pooled_irt_n16_fixed\": {\"conclusion\": \"success\", \"status\": \"DONE\"}, \"exp_001_eval_05B_instruct\": {\"conclusion\": \"success\", \"status\": \"DONE\"}, \"exp_001_eval_llama32_3B_d000_s42\": {\"conclusion\": \"killed\", \"metrics\": {\"MMLU\": 0.4545}, \"status\": \"DONE\"}, \"exp_001_eval_15B_instruct\": {\"conclusion\": \"success\", \"metrics\": {\"ARC\": 0.7654, \"GSM8K\": 0.5929, \"MMLU\": 0.5775}, \"status\": \"DONE\"}, \"exp_006_mmlu_domain_gamma_n24_v4\": {\"conclusion\": \"success\", \"metrics\": {\"Business_Law_gamma\": \"not_significant\", \"CS_Eng_gamma\": \"not_significant\", \"Humanities_gamma\": \"negative_significant\", \"Medical_gamma\": \"negative_significant\", \"STEM_Math_gamma\": \"positive_significant\", \"STEM_Science_gamma\": \"positive_significant\", \"Social_Sciences_gamma\": \"negative_significant\", \"domains\": 7, \"note\": \"CmdStan crashed after results saved. Humanities rhat=1.014 not converged.\"}, \"status\": \"DONE\"}, \"exp_006_pooled_irt_rrf_n25_v2\": {\"conclusion\": \"success\", \"metrics\": {\"arc_N8_4PLgamma\": \"over_parameterized_cal_worsens\", \"gsm8k_N16_delta_mae\": 0.118, \"gsm8k_calibration\": \"effective\", \"mmlu_N8_4PLgamma\": \"over_parameterized_cal_worsens\", \"note\": \"GSM8K N=16 works. MMLU/ARC N=8 with 4PL+gamma over-parameterized, PPP=0.006/0.000, cal_mae > raw_mae. Need 2PL+gamma or N>=16.\"}, \"status\": \"DONE\"}, \"exp_003_rrf_full_n25_latest\": {\"conclusion\": \"success\", \"status\": \"DONE\"}, \"signals_05B_s123_v2\": {\"conclusion\": \"success\", \"status\": \"DONE\"}, \"exp_006_pooled_irt_n25\": {\"conclusion\": \"success\", \"status\": \"DONE\"}, \"exp_001_eval_3B_instruct_v2\": {\"conclusion\": \"success\", \"metrics\": {\"GSM8K\": 0.76, \"HumanEval\": 0.5, \"MMLU\": 0.605}, \"status\": \"DONE\"}, \"exp_006_mmlu_domain_gamma_n24_v3\": {\"conclusion\": \"failed\", \"metrics\": {\"Humanities\": {\"CI\": [-0.776, -0.041], \"N\": 21, \"PPP\": 1, \"converged\": \"borderline_rhat_1.014\", \"excludes_zero\": true, \"gamma_mean\": -0.407}, \"Medical\": {\"CI\": [-0.338, -0.06], \"N\": 24, \"PPP\": 1, \"converged\": true, \"excludes_zero\": true, \"gamma_mean\": -0.199}, \"STEM_CS_Eng\": {\"CI\": [-0.448, 0.835], \"N\": 23, \"PPP\": 0.892, \"converged\": true, \"excludes_zero\": false, \"gamma_mean\": 0.197}, \"STEM_Math\": {\"CI\": [0.527, 1.43], \"N\": 23, \"PPP\": 0.438, \"converged\": true, \"excludes_zero\": true, \"gamma_mean\": 0.969}, \"STEM_Science\": {\"CI\": [0.385, 1.274], \"N\": 23, \"PPP\": 0.807, \"converged\": true, \"excludes_zero\": true, \"gamma_mean\": 0.838}, \"completed_domains\": 5, \"crashed\": \"Social_Sciences (CmdStan retcode=[1,0,0,1])\", \"not_run\": [\"Business_Law\", \"Other\"], \"total_domains\": 8}, \"status\": \"DONE\"}, \"exp_002_signals_15B_d100_s123_cuda2\": {\"conclusion\": \"success\", \"status\": \"DONE\"}, \"exp_002_signals_15B_s123_batch\": {\"conclusion\": \"success\", \"status\": \"DONE\"}, \"exp_006_mmlu_domain_gamma_n24\": {\"conclusion\": \"success\", \"metrics\": {\"STEM_CS_Eng\": {\"N_items\": 557, \"N_models\": 23, \"PPP\": 0.892, \"fit_time_s\": 153, \"gamma_excludes_zero\": false, \"gamma_mean\": 0.197}, \"STEM_Math\": {\"N_items\": 1190, \"N_models\": 23, \"PPP\": 0.438, \"fit_time_s\": 527, \"gamma_excludes_zero\": true, \"gamma_mean\": 0.969}, \"STEM_Science\": {\"N_items\": 1397, \"N_models\": 23, \"PPP\": 0.807, \"fit_time_s\": 618, \"gamma_excludes_zero\": true, \"gamma_mean\": 0.838}, \"domains_completed\": 3, \"domains_total\": 8, \"note\": \"3/8 domains complete. Process stopped after 3 — remaining 5 need restart.\"}, \"status\": \"DONE\"}, \"exp_006_mmlu_domain_gamma_n24_v2\": {\"conclusion\": \"failed\", \"status\": \"DONE\"}, \"exp_001_sft_llama32_3B_d000_s42\": {\"conclusion\": \"success\", \"metrics\": {\"epoch\": 1, \"mean_token_accuracy\": 0.6685, \"train_loss\": 1.5165, \"train_runtime_sec\": 8170}, \"status\": \"DONE\"}, \"exp_002_signals_05B_s123_v2\": {\"conclusion\": \"success\", \"status\": \"DONE\"}, \"exp_001_sft_3B_d100_s123_a32\": {\"conclusion\": \"success\", \"status\": \"DONE\"}, \"exp_002_signals_3B_d100_a32_s42\": {\"conclusion\": \"success\", \"metrics\": {\"benchmarks_completed\": [\"mmlu\", \"gsm8k\", \"arc_challenge\"], \"signals_generated\": [\"s1_embedding\", \"s2_minkpp\", \"s4_selfcritique\"], \"status_note\": \"Signals validated via pooled IRT (exp_006_pooled_irt_all_scales, N=23 success). Analysis worker completed 2026-05-16T10:50:52 but callback not processed due to session reset.\"}, \"status\": \"DONE\"}, \"exp_006_pooled_irt_all_scales\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge\": {\"cal_mae\": 0.0153, \"delta_mae\": 0.0183, \"divergences\": 0, \"ess\": 1670, \"gamma_ci95\": [-0.2552, 1.2529], \"gamma_mean\": 0.4859, \"n_items\": 300, \"n_models\": 13, \"ppp\": 0.027, \"raw_mae\": 0.0335, \"rhat\": 1.0065}, \"exposure\": \"rrf_signal\", \"gsm8k\": {\"cal_mae\": 0.0078, \"delta_mae\": 0.1552, \"divergences\": 0, \"ess\": 1388, \"gamma_ci95\": [-0.2889, 0.637], \"gamma_mean\": 0.1721, \"n_items\": 300, \"n_models\": 20, \"ppp\": 0.3425, \"raw_mae\": 0.163, \"rhat\": 1.0071}, \"mmlu\": {\"cal_mae\": 0.0059, \"delta_mae\": 0.0098, \"divergences\": 0, \"ess\": 1402, \"gamma_ci95\": [-0.5501, 1.5974], \"gamma_mean\": 0.5172, \"n_items\": 300, \"n_models\": 15, \"ppp\": 0.2335, \"raw_mae\": 0.0157, \"rhat\": 1.0067}, \"model_type\": \"2pl_gamma\", \"rrf_respondents\": 23, \"scales\": [\"0.5B\", \"1.5B\", \"3B\"]}, \"status\": \"DONE\"}, \"exp_001_eval_3B_instruct_aligned_para\": {\"conclusion\": \"failed\", \"status\": \"DONE\"}, \"exp_002_signals_3B_d000_a32_s42\": {\"conclusion\": \"success\", \"metrics\": {\"benchmarks\": {\"arc_challenge\": {\"n_items\": 1172, \"signals\": [\"s1_embedding\", \"s2_minkpp\", \"s4_selfcritique\"]}, \"gsm8k\": {\"n_items\": 1319, \"signals\": [\"s1_embedding\", \"s2_minkpp\", \"s4_selfcritique\"]}, \"mmlu\": {\"n_items\": 14042, \"signals\": [\"s1_embedding\", \"s2_minkpp\", \"s4_selfcritique\"]}}, \"output_files\": {\"signal_s1_embedding_arc_challenge.json\": \"650K\", \"signal_s1_embedding_gsm8k.json\": \"717K\", \"signal_s1_embedding_mmlu.json\": \"7.6M\", \"signal_s2_minkpp_arc_challenge.json\": \"245K\", \"signal_s2_minkpp_gsm8k.json\": \"266K\", \"signal_s2_minkpp_mmlu.json\": \"2.8M\", \"signal_s4_selfcritique_arc_challenge.json\": \"284K\", \"signal_s4_selfcritique_gsm8k.json\": \"310K\", \"signal_s4_selfcritique_mmlu.json\": \"3.2M\"}, \"runtime_minutes\": 189, \"signals_completed\": 9, \"signals_failed\": 0}, \"status\": \"DONE\"}, \"exp_002_signals_3B_d005_a32_s42\": {\"conclusion\": \"success\", \"status\": \"DONE\"}, \"exp_006_pooled_irt_05b_15b\": {\"conclusion\": \"success\", \"metrics\": {\"arc_cal_mae\": 0.0682, \"arc_ci95\": \"[-0.271, 2.857]\", \"arc_delta_mae\": -0.064, \"arc_ess\": 1480, \"arc_gamma\": 1.2259, \"arc_n_models\": 5, \"arc_ppp\": 0, \"arc_raw_mae\": 0.0042, \"arc_rhat\": 1.0072, \"gsm8k_cal_mae\": 0.0373, \"gsm8k_ci95\": \"[-0.990, 1.019]\", \"gsm8k_delta_mae\": 0.1128, \"gsm8k_ess\": 1300, \"gsm8k_gamma\": 0.0128, \"gsm8k_n_models\": 11, \"gsm8k_ppp\": 0.663, \"gsm8k_raw_mae\": 0.1501, \"gsm8k_rhat\": 1.0072, \"n_items_subsampled\": 300}, \"status\": \"DONE\"}, \"exp006_pooled_rrf_irt_05b_15b\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge\": {\"cal_mae\": 0.0682, \"delta_mae\": -0.064, \"divergences\": 0, \"ess\": 1480, \"gamma_ci95\": [-0.2711, 2.8571], \"gamma_mean\": 1.2259, \"n_items\": 300, \"n_models\": 5, \"ppp\": 0, \"raw_mae\": 0.0042, \"rhat\": 1.0072}, \"gsm8k\": {\"cal_mae\": 0.0373, \"delta_mae\": 0.1128, \"divergences\": 0, \"ess\": 1300, \"gamma_ci95\": [-0.99, 1.0187], \"gamma_mean\": 0.0128, \"n_items\": 300, \"n_models\": 11, \"ppp\": 0.663, \"raw_mae\": 0.1501, \"rhat\": 1.0072}}, \"status\": \"DONE\"}, \"exp_006_mmlu_domain_gamma\": {\"conclusion\": \"success\", \"metrics\": {\"Business_Law_gamma\": 0.61, \"Humanities_gamma\": 0.47, \"Medical_gamma\": 0.27, \"Other_gamma\": 1.34, \"STEM_CS_Eng_gamma\": 0.29, \"STEM_Math_gamma\": -0.55, \"STEM_Science_gamma\": 0.36, \"Social_Sciences_gamma\": 0.28, \"all_rhat_max\": 1.008, \"divergent_transitions\": 0, \"n_domains\": 8, \"n_models\": 16}, \"status\": \"DONE\"}, \"exp_001_eval_3B_d005_s42_para_aligned\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge_acc\": 0.8164, \"arc_challenge_n\": 697, \"gsm8k_acc\": 0.3421, \"gsm8k_n\": 228, \"humaneval_n\": 26, \"humaneval_pass1\": 0.0769, \"mmlu_acc\": 0.6471, \"mmlu_n\": 6596}, \"status\": \"DONE\"}, \"exp_001_eval_3B_d000_s42_a32_para_aligned\": {\"conclusion\": \"success\", \"metrics\": {\"arc_para\": 0.8106, \"gsm8k_para\": 0.0526, \"humaneval_para\": 0.1923, \"mmlu_para\": 0.6431}, \"status\": \"DONE\"}, \"exp_001_eval_3B_d005_s42_a32_batch\": {\"conclusion\": \"success\", \"metrics\": {\"arc\": 0.8251, \"arc_para\": 0.8164, \"gsm8k\": 0.4147, \"gsm8k_para\": 0.3421, \"humaneval\": 0.1341, \"humaneval_para\": 0.0769, \"mmlu\": 0.6308, \"mmlu_para\": 0.6471}, \"status\": \"DONE\"}, \"exp_008_instruct_rl_proxy\": {\"conclusion\": \"failed\", \"metrics\": {\"base_pretrained_signals\": \"computing_PID_701898_GPU5\", \"comparison\": {\"arc\": {\"d000_sft_s2\": 1.7079, \"d000_sft_s4\": -0.9538, \"instruct_s2\": 1.6737, \"instruct_s4\": -0.9227, \"s4_delta_instruct_vs_sft\": 0.0311}, \"gsm8k\": {\"d000_sft_s2\": 1.6532, \"d000_sft_s4\": -0.9408, \"instruct_s2\": 1.7073, \"instruct_s4\": -0.9632, \"s4_delta_instruct_vs_sft\": -0.0224}, \"mmlu\": {\"base_s2\": 1.7009, \"base_s4\": \"computing\", \"d000_sft_s2\": 1.6976, \"d000_sft_s4\": -0.9557, \"instruct_s2\": 1.6952, \"instruct_s4\": -0.8782, \"s4_delta_instruct_vs_sft\": 0.0775}}, \"d000_sft_signals_complete\": true, \"instruct_signals_complete\": true, \"key_finding\": \"S4 differentiates regimes (MMLU +0.078, ARC +0.031 Instruct vs SFT); S2 does not (<0.01 difference). RL increases S4 entropy on knowledge benchmarks.\", \"signal_paths\": {\"base_pretrained\": \"/root/autodl-tmp/exp008/signals/base_pretrained/\", \"d000_sft\": \"/root/autodl-tmp/exp002/signals/Qwen2.5-0.5B_d000_s42/\", \"instruct\": \"/root/autodl-tmp/exp008/signals/rl_aligned/\"}}, \"status\": \"DONE\"}, \"exp_003_mmlu_item_aligned_gap\": {\"conclusion\": \"success\", \"metrics\": {\"aggregate\": {\"max_abs_gap_pp\": 3.73, \"mean_gap_pp\": -2.243, \"median_gap_pp\": -2.259, \"std_gap_pp\": 0.671}, \"alignment_correction\": {\"conclusion\": \"Proper item-ID alignment changes result by <0.3pp vs naive positional comparison\", \"misaligned_vs_aligned_diff_pp\": \"<0.3 (confirmed from prior 2-pair check)\"}, \"by_contamination\": {\"d000\": {\"mean_pp\": -2.292, \"n\": 5}, \"d005\": {\"mean_pp\": -2.181, \"n\": 6}, \"d025\": {\"mean_pp\": -1.913, \"n\": 5}, \"d100\": {\"mean_pp\": -2.687, \"n\": 4}}, \"by_size\": {\"0.5B\": {\"mean_pp\": -2.259, \"n\": 4, \"std_pp\": 1.238}, \"1.5B\": {\"mean_pp\": -2.452, \"n\": 8, \"std_pp\": 0.31}, \"3B\": {\"mean_pp\": -2.026, \"n\": 8, \"std_pp\": 0.415}}, \"n_common_items\": 6596, \"n_pairs\": 20, \"per_item\": {\"mean_disagree_rate_pct\": 15.5, \"n_flagged_items\": 426, \"pct_aligned_easier\": 6.6, \"pct_high_disagree_gt50\": 6.5, \"pct_neutral_lt03pp\": 84.8, \"pct_para_easier\": 8.6}, \"prior_2pair_check\": {\"15B_d100\": {\"aligned_gap_pp\": -2.9, \"qc_selection_bias_pp\": 0.56}, \"3B_d100\": {\"aligned_gap_pp\": -3.5, \"qc_selection_bias_pp\": -0.08}}}, \"status\": \"DONE\"}, \"exp_001_eval_3B_d025_s42_a32_para\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge_para\": 0.8106, \"gsm8k_para\": \"completed\", \"humaneval_para\": 0, \"mmlu_para\": \"completed_6596_items\", \"output_dir\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d025_v3_s42_para_aligned\", \"sentinel\": \".done exists\"}, \"status\": \"DONE\"}, \"exp_002_signals_3B_d025_v3_s42\": {\"conclusion\": \"success\", \"status\": \"DONE\"}, \"exp_002_signals_3B_v9\": {\"conclusion\": \"failed\", \"status\": \"DONE\"}, \"exp_001_sft_3B_d025_s42_a32_v3\": {\"conclusion\": \"killed\", \"status\": \"DONE\"}, \"exp_001_eval_3B_d025_v3_s42_batch\": {\"conclusion\": \"killed\", \"status\": \"DONE\"}, \"exp_002_signals_05B_s123_batch\": {\"conclusion\": \"failed\", \"status\": \"DONE\"}, \"exp_002_signals_3B_v7\": {\"conclusion\": \"success\", \"metrics\": {\"benchmarks\": [\"mmlu\", \"gsm8k\", \"arc_challenge\"], \"merged_files\": 3, \"output_dir\": \"/root/autodl-tmp/exp002/signals/Qwen2.5-3B_d005_s123/\", \"signal_files\": 9, \"signals\": [\"s1_embedding\", \"s2_minkpp\", \"s4_selfcritique\"]}, \"status\": \"DONE\"}, \"exp_001_sft_3B_d100_s42_a32_v3\": {\"conclusion\": \"success\", \"metrics\": {\"entropy\": 1.296, \"final_epoch\": 1, \"mean_token_accuracy\": 0.7186, \"total_steps\": 4159, \"train_loss\": 1.1795, \"train_runtime_sec\": 17645, \"train_samples_per_second\": 3.771, \"train_steps_per_second\": 0.236}, \"status\": \"DONE\"}, \"exp_001_sft_3B_d005_s42_a32\": {\"conclusion\": \"success\", \"metrics\": {\"epoch\": 1, \"final_loss\": 1.0822, \"mean_token_accuracy\": 0.7511, \"steps\": 3177, \"train_runtime_sec\": 14913.5}, \"status\": \"DONE\"}, \"exp_002_signals_3B_v8_recovery\": {\"conclusion\": \"failed\", \"status\": \"DONE\"}, \"exp_004_sim_sweep_v7\": {\"conclusion\": \"success\", \"metrics\": {\"ci95_coverage_range\": \"[0.8, 1.0]\", \"conditions_failed\": \"auc0.65_n20/n50/n100 (CmdStan TMPDIR race)\", \"conditions_ok\": 9, \"conditions_total\": 12, \"gamma_bias_range\": \"[-0.025, +0.056]\", \"gamma_rmse_range\": \"[0.005, 0.085]\", \"note\": \"9/12 sufficient for Claim 1 identifiability\", \"theta_corr_range\": \"[0.947, 0.972]\"}, \"status\": \"DONE\"}, \"exp_001_sft_3B_d000_s42_a32\": {\"conclusion\": \"success\", \"metrics\": {\"epoch\": 1, \"final_loss\": 1.1324, \"steps\": 3125}, \"status\": \"DONE\"}, \"exp_002_signals_3B_v8\": {\"conclusion\": \"failed\", \"status\": \"DONE\"}, \"exp_002_signals_3B_v5\": {\"conclusion\": \"failed\", \"status\": \"DONE\"}, \"exp_001_sft_3B_d025_s42_a32_v2\": {\"conclusion\": \"failed\", \"status\": \"DONE\"}, \"exp_001_eval_15B_s123_para_aligned_batch\": {\"conclusion\": \"success\", \"metrics\": {\"d000_s123_para_aligned\": {\"arc_challenge\": 0.7547, \"gsm8k\": 0.5921, \"humaneval\": 0.1538, \"mmlu\": 0.6111}, \"d005_s123_para_aligned\": {\"arc_challenge\": 0.7475, \"gsm8k\": 0.5439, \"humaneval\": 0.0769, \"mmlu\": 0.614}, \"d025_s123_para_aligned\": {\"arc_challenge\": 0.7504, \"gsm8k\": 0.5482, \"humaneval\": 0.1923, \"mmlu\": 0.6145}, \"d100_s123_para_aligned\": {\"arc_challenge\": 0.7834, \"gsm8k\": 0.5307, \"humaneval\": 0.2308, \"mmlu\": 0.629}}, \"status\": \"DONE\"}, \"exp_001_sft_3B_d100_s42_a32_v2\": {\"conclusion\": \"failed\", \"status\": \"DONE\"}, \"exp_001_sft_3B_d025_s42_a32\": {\"conclusion\": \"killed\", \"status\": \"DONE\"}, \"exp_001_sft_3B_d100_s42_a32\": {\"conclusion\": \"killed\", \"status\": \"DONE\"}, \"exp_001_sft_d025_3B_v3\": {\"conclusion\": \"success\", \"metrics\": {\"entropy\": 1.1807, \"epoch\": 1, \"mean_token_accuracy\": 0.734, \"total_steps\": 3384, \"train_loss\": 1.1464, \"train_runtime_s\": 14584}, \"status\": \"DONE\"}, \"exp_002_signals_3B_v6\": {\"conclusion\": \"failed\", \"status\": \"DONE\"}, \"exp_001_sft_d005_3B\": {\"conclusion\": \"success\", \"metrics\": {\"epochs\": 1, \"final_loss\": 1.11, \"total_steps\": 3177, \"training_hours\": 3.76}, \"status\": \"DONE\"}, \"exp_002_signals_3B_v4\": {\"conclusion\": \"failed\", \"status\": \"DONE\"}, \"exp_004_sim_sweep_extreme_gamma\": {\"conclusion\": \"success\", \"metrics\": {\"conditions\": 8, \"gamma2_avg_bias\": 0.017, \"gamma2_avg_rmse\": 0.101, \"gamma2_ci95_coverage\": 1, \"gamma4_avg_bias\": -0.106, \"gamma4_avg_rmse\": 0.226, \"gamma4_ci95_coverage\": 0.925, \"seeds_per_condition\": 10, \"theta_corr_range\": [0.914, 0.969], \"total_time_hours\": 11.1}, \"status\": \"DONE\"}, \"exp_001_eval_3B_d100_s123_para_aligned_v2\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge\": {\"accuracy\": 0.8164, \"correct\": 569, \"total\": 697}, \"gsm8k\": {\"accuracy\": 0.5877, \"correct\": 134, \"total\": 228}, \"humaneval\": {\"correct\": 2, \"pass@1\": 0.0769, \"total\": 26}, \"mmlu\": {\"accuracy\": 0.6565, \"correct\": 4330, \"total\": 6596}}, \"status\": \"DONE\"}, \"exp_001_eval_3B_d100_s123_para_aligned\": {\"conclusion\": \"failed\", \"status\": \"DONE\"}, \"exp_001_sft_3B_d000_v3\": {\"conclusion\": \"failed\", \"status\": \"DONE\"}, \"exp_004_sim_sweep_v6\": {\"conclusion\": \"killed\", \"status\": \"DONE\"}, \"exp_002_signals_3B_v3\": {\"conclusion\": \"killed\", \"status\": \"DONE\"}, \"exp_001_eval_3B_d005_s123_aligned\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge_accuracy\": 0.8242, \"gsm8k_exact_match\": 0.6308, \"humaneval_pass1\": 0.1037, \"mmlu_accuracy\": 0.6324}, \"status\": \"DONE\"}, \"exp_001_eval_3B_d025_s123_aligned\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge\": 0.8336, \"gsm8k\": 0.5254, \"humaneval\": 0.1585, \"mmlu\": 0.6367}, \"status\": \"DONE\"}, \"exp_002_signals_3B_v2\": {\"conclusion\": \"killed\", \"status\": \"DONE\"}, \"exp_001_eval_3B_d005_s123_para_aligned\": {\"conclusion\": \"success\", \"metrics\": {\"ARC\": 0.8192, \"GSM8K\": 0.5, \"HumanEval\": 0.0769, \"MMLU\": 0.6461}, \"status\": \"DONE\"}, \"exp_001_eval_15B_d005_s123\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge\": {\"accuracy\": 0.7568, \"correct\": 887, \"total\": 1172}, \"gsm8k\": {\"correct\": 855, \"exact_match\": 0.6482, \"total\": 1319}, \"humaneval\": {\"correct\": 41, \"pass@1\": 0.25, \"total\": 164}, \"mmlu\": {\"accuracy\": 0.5869, \"correct\": 8241, \"total\": 14042}}, \"status\": \"DONE\"}, \"exp_001_eval_15B_d005_s123_v2\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge\": {\"accuracy\": 0.7568, \"correct\": 887, \"total\": 1172}, \"gsm8k\": {\"correct\": 855, \"exact_match\": 0.6482, \"total\": 1319}, \"humaneval\": {\"correct\": 41, \"pass@1\": 0.25, \"total\": 164}, \"mmlu\": {\"accuracy\": 0.5869, \"correct\": 8241, \"total\": 14042}}, \"status\": \"DONE\"}, \"exp_001_eval_15B_d025_s123\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge\": {\"accuracy\": 0.7577, \"correct\": 888, \"total\": 1172}, \"gsm8k\": {\"correct\": 864, \"exact_match\": 0.655, \"total\": 1319}, \"humaneval\": {\"correct\": 41, \"pass@1\": 0.25, \"total\": 164}, \"mmlu\": {\"accuracy\": 0.5881, \"correct\": 8258, \"total\": 14042}}, \"status\": \"DONE\"}, \"exp_001_eval_15B_d025_s123_v2\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge\": {\"accuracy\": 0.7577, \"correct\": 888, \"total\": 1172}, \"gsm8k\": {\"correct\": 864, \"exact_match\": 0.655, \"total\": 1319}, \"humaneval\": {\"correct\": 41, \"pass@1\": 0.25, \"total\": 164}, \"mmlu\": {\"accuracy\": 0.5881, \"correct\": 8258, \"total\": 14042}}, \"status\": \"DONE\"}, \"exp_001_sft_d025_3B_v2\": {\"conclusion\": \"success\", \"metrics\": {\"epochs\": 1, \"mean_token_accuracy\": 0.7342, \"runtime_seconds\": 14499, \"steps\": 3384, \"train_loss\": 1.1501}, \"status\": \"DONE\"}, \"exp_001_sft_d100_3B_v2\": {\"conclusion\": \"success\", \"metrics\": {\"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d100_s42/lora_adapter\", \"d020_params\": \"lr=5e-5, alpha=16, r=16\", \"status\": \"training_complete\", \"steps\": \"4159/4159\"}, \"status\": \"DONE\"}, \"exp_001_sft_3B_d000_v2\": {\"conclusion\": \"success\", \"metrics\": {\"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_v2_s42/lora_adapter\", \"completed_at\": \"2026-05-15T03:45Z\", \"status\": \"training_complete\"}, \"status\": \"DONE\"}, \"exp_002_signals_3B\": {\"conclusion\": \"failed\", \"status\": \"DONE\"}, \"exp_001_eval_3B_d000_s42_para_aligned\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge\": {\"accuracy\": 0.8235, \"correct\": 574, \"total\": 697}, \"gsm8k\": {\"accuracy\": 0.0482, \"correct\": 11, \"total\": 228}, \"humaneval\": {\"correct\": 3, \"pass@1\": 0.1154, \"total\": 26}, \"mmlu\": {\"accuracy\": 0.6474, \"correct\": 4270, \"total\": 6596}}, \"status\": \"DONE\"}, \"exp_001_eval_3B_d100_s42_para_aligned\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge\": {\"accuracy\": 0.8092, \"correct\": 564, \"total\": 697}, \"gsm8k\": {\"accuracy\": 0.5833, \"correct\": 133, \"total\": 228}, \"humaneval\": {\"correct\": 3, \"pass@1\": 0.1154, \"total\": 26}, \"mmlu\": {\"accuracy\": 0.659, \"correct\": 4347, \"total\": 6596}}, \"status\": \"DONE\"}, \"exp_001_sft_3B_d005_s123\": {\"conclusion\": \"success\", \"metrics\": {\"final_loss\": 1.1349, \"final_token_accuracy\": 0.7069, \"total_steps\": 3177}, \"status\": \"DONE\"}, \"exp_001_sft_3B_d025_s123\": {\"conclusion\": \"success\", \"metrics\": {\"final_loss\": 1.1401, \"final_token_accuracy\": 0.734, \"total_steps\": 3384}, \"status\": \"DONE\"}, \"exp_001_eval_3B_d000_s123_aligned\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge\": 0.8328, \"gsm8k\": 0.1812, \"humaneval\": 0.0854, \"mmlu\": 0.6332}, \"status\": \"DONE\"}, \"exp_001_eval_3B_d005_s42_aligned\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge\": 0.8294, \"gsm8k\": 0.2077, \"humaneval\": 0.1463, \"mmlu\": 0.6345}, \"status\": \"DONE\"}, \"exp_008_base_pretrained_eval_v2\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge\": 0.2278, \"gsm8k\": 0.163, \"humaneval\": 0, \"mmlu\": 0.2294}, \"status\": \"DONE\"}, \"exp_001_sft_15B_d025_s123_v2\": {\"conclusion\": \"success\", \"metrics\": {\"mean_token_accuracy\": 0.7466, \"train_loss\": 1.2723}, \"status\": \"DONE\"}, \"exp_001_sft_15B_d005_s123_v2\": {\"conclusion\": \"success\", \"metrics\": {\"mean_token_accuracy\": 0.6855, \"train_loss\": 1.2639}, \"status\": \"DONE\"}, \"exp_008_base_pretrained_15B_eval_v2\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge\": 0.2304, \"arc_correct\": 270, \"arc_total\": 1172, \"gsm8k\": 0.0053, \"gsm8k_correct\": 7, \"gsm8k_total\": 1319, \"humaneval_correct\": 38, \"humaneval_pass1\": 0.2317, \"humaneval_total\": 164, \"mmlu\": 0.2303, \"mmlu_correct\": 3234, \"mmlu_total\": 14042}, \"status\": \"DONE\"}, \"exp_008_base_pretrained_15B_eval\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge_accuracy\": 0.2304, \"arc_correct\": 270, \"arc_total\": 1172, \"gsm8k_accuracy\": 0.0053, \"gsm8k_correct\": 7, \"gsm8k_total\": 1319, \"humaneval_correct\": 38, \"humaneval_pass@1\": 0.2317, \"humaneval_total\": 164, \"mmlu_accuracy\": 0.2303, \"mmlu_correct\": 3234, \"mmlu_total\": 14042}, \"status\": \"DONE\"}, \"exp_008_base_pretrained_eval\": {\"conclusion\": \"failed\", \"status\": \"DONE\"}, \"exp_001_eval_15B_d000_s123_aligned\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge_accuracy\": 0.7577, \"gsm8k_accuracy\": 0.6535, \"humaneval_pass@1\": 0.1707, \"mmlu_accuracy\": 0.5855}, \"status\": \"DONE\"}, \"exp_001_eval_15B_d100_s123_aligned\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge_accuracy\": 0.7816, \"gsm8k_accuracy\": 0.6444, \"humaneval_pass@1\": 0.2805, \"mmlu_accuracy\": 0.5956}, \"status\": \"DONE\"}, \"exp_001_eval_05B_d000_s123_aligned\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge\": 0.4974, \"gsm8k\": 0.3412, \"humaneval\": 0.1037, \"mmlu\": 0.4216}, \"status\": \"DONE\"}, \"exp_001_eval_3B_d000_s42_v3\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge\": 0.8276, \"gsm8k\": 0.1198, \"humaneval\": 0.1159, \"mmlu\": 0.634}, \"status\": \"DONE\"}, \"exp006-s1only-gsm8k-2pl\": {\"conclusion\": \"success\", \"metrics\": {\"ci_excludes_zero\": false, \"divergent_count\": 0, \"gamma_ci95\": [-0.306, 0.591], \"gamma_mean\": 0.1389, \"gamma_sd\": 0.2274, \"max_rhat\": 1.0024, \"min_ess\": 3604.4, \"obs_mean_acc\": 0.5086, \"ppp\": 0.2835, \"pred_mean_acc\": 0.5011, \"residual_mae\": 0.0083}, \"status\": \"DONE\"}, \"exp_001_eval_3B_d000_v2_s123_aligned\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge\": 0.8259, \"gsm8k\": 0.2676, \"humaneval\": 0.061, \"mmlu\": 0.6314}, \"status\": \"DONE\"}, \"exp_001_eval_3B_d025_v2_aligned\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge\": 0.8276, \"gsm8k\": 0.6793, \"humaneval\": 0.0976, \"mmlu\": 0.5998}, \"status\": \"DONE\"}, \"exp_001_eval_3B_d100_v2_s123_aligned\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge\": 0.8311, \"gsm8k\": 0.7324, \"humaneval\": 0.1829, \"mmlu\": 0.6319}, \"status\": \"DONE\"}, \"exp_001_sft_15B_d005_s123\": {\"conclusion\": \"failed\", \"status\": \"DONE\"}, \"exp_001_eval_05B_d025_s123_aligned\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge\": {\"accuracy\": 0.4061, \"correct\": 476, \"total\": 1172}, \"gsm8k\": {\"accuracy\": 0.3533, \"correct\": 466, \"total\": 1319}, \"humaneval\": {\"correct\": 14, \"pass@1\": 0.0854, \"total\": 164}, \"mmlu\": {\"accuracy\": 0.3473, \"correct\": 4877, \"total\": 14042}}, \"status\": \"DONE\"}, \"exp_001_sft_05B_d025_s123_v2\": {\"conclusion\": \"success\", \"metrics\": {\"accuracy\": 0.697, \"epoch\": 1, \"global_steps\": 3384, \"runtime_seconds\": 5930, \"train_loss\": 1.548}, \"status\": \"DONE\"}, \"exp_001_eval_05B_d000_s42_v7\": {\"conclusion\": \"failed\", \"status\": \"DONE\"}, \"exp_004_sim_sweep_v5\": {\"conclusion\": \"failed\", \"metrics\": {\"conditions_all_failed\": [\"auc0.65_n20 (0/10)\", \"auc0.65_n50 (0/7)\"], \"conditions_complete\": 4, \"conditions_fully_ok\": [\"auc0.55_n20 (10/10)\", \"auc0.55_n50 (10/10)\", \"auc0.8_n20 (10/10)\", \"auc0.8_n50 (10/10)\"], \"conditions_missing\": 3, \"conditions_never_started\": [\"auc0.65_n100\", \"auc0.9_n50\", \"auc0.9_n100\"], \"conditions_partial\": 5, \"conditions_partial_ok\": [\"auc0.55_n100 (7/10)\", \"auc0.8_n100 (6/10)\", \"auc0.9_n20 (6/10)\"], \"failure_cause\": \"Disk quota exceeded ([Errno 122]) - root partition /tmp filled by CmdStan temp files\", \"seeds_attempted\": 97, \"seeds_ok\": 59, \"seeds_total\": 120}, \"status\": \"DONE\"}, \"exp006-oracle-arc-4pl-pooled\": {\"conclusion\": \"failed\", \"status\": \"DONE\"}, \"exp_008_instruct_05B_eval\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge_accuracy\": 0.2816, \"gsm8k_accuracy\": 0.3882, \"humaneval_pass@1\": 0, \"mmlu_accuracy\": 0.2462}, \"status\": \"DONE\"}, \"exp_001_eval_3B_d100_v2_aligned_v2\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge_accuracy\": 0.8242, \"gsm8k_accuracy\": 0.7415, \"humaneval_pass@1\": 0.1707, \"mmlu_accuracy\": 0.632}, \"status\": \"DONE\"}, \"exp_001_eval_3B_d025_v2_para_aligned\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge_para_accuracy\": 0.8106, \"gsm8k_para_accuracy\": 0.5482, \"humaneval_para_pass@1\": 0.1154, \"mmlu_para_accuracy\": 0.621}, \"status\": \"DONE\"}, \"exp_001_sft_3B_d100_s123\": {\"conclusion\": \"success\", \"metrics\": {\"epochs\": 1, \"mean_token_accuracy\": 0.7343, \"runtime_seconds\": 18252, \"steps\": 4159, \"train_loss\": 1.1846}, \"status\": \"DONE\"}, \"exp006-oracle-arc-2pl\": {\"conclusion\": \"success\", \"metrics\": {\"C95_coverage\": 0.1818, \"ESS\": 1512, \"MAE\": 0.0759, \"gamma\": -0.618, \"gamma_ci\": [-1.04, -0.2], \"rhat\": 1.006}, \"status\": \"DONE\"}, \"exp_001_eval_3B_d000_v2_s123_para_aligned\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge_para_accuracy\": 0.8121, \"gsm8k_para_accuracy\": 0.1491, \"humaneval_para_pass@1\": 0.0385, \"mmlu_para_accuracy\": 0.6512}, \"status\": \"DONE\"}, \"exp006-pooled-s1only-gsm8k-v2\": {\"conclusion\": \"success\", \"metrics\": {\"diagnostics_ok\": false, \"divergent_pct\": 0, \"ess_min\": 330.2, \"fit_time_sec\": 336.9, \"gamma\": 0.1871, \"gamma_ci_excludes_zero\": false, \"gamma_ci_lower\": -0.9172, \"gamma_ci_upper\": 1.3294, \"gamma_sd\": 0.5687, \"n_items\": 1319, \"n_models\": 8, \"note\": \"No evaluation/baselines files generated; only IRT fit available. rhat and ESS did not pass thresholds.\", \"ppp\": 0.336, \"residual_mae\": 0.0367, \"rhat_max\": 1.0148}, \"status\": \"DONE\"}, \"exp006-pooled-s1only-arc\": {\"conclusion\": \"success\", \"metrics\": {\"baselines\": {\"B0_raw_mae\": 0.0588, \"B1_remove_rescore_mae\": 0.0588, \"B2_2pl_gamma_mae\": 0.064, \"B3_vanilla_4pl_mae\": 0.0706, \"B4_linear_regression_mae\": 0.0562, \"B5_emperor_mae\": 0.0588, \"B6_dcr_fuzzy_mae\": 0.2454}, \"brier\": 0.0018, \"coverage_50\": 0, \"coverage_80\": 0.25, \"coverage_95\": 0.625, \"divergent_pct\": 0, \"ece\": 0.0319, \"ess_min\": 769.6, \"fit_time_sec\": 317.7, \"gamma\": -1.4637, \"gamma_ci_excludes_zero\": true, \"gamma_ci_lower\": -2.51, \"gamma_ci_upper\": -0.4051, \"gamma_sd\": 0.5276, \"kendall_tau\": 0.7559, \"mae\": 0.0347, \"n_items\": 1172, \"n_models\": 8, \"ppp\": 0.9677, \"rhat_max\": 1.0098, \"sharpness_95\": 0.0684}, \"status\": \"DONE\"}, \"exp006-oracle-gsm8k-extended-v2\": {\"conclusion\": \"success\", \"metrics\": {\"baselines\": {\"B0_raw_mae\": 0.005, \"B4_linear_regression_mae\": 0.008, \"B5_emperor_mae\": 0.005, \"B6_dcr_fuzzy_mae\": 0.138}, \"coverage_50\": 0.25, \"coverage_80\": 0.25, \"coverage_95\": 0.31, \"divergent_pct\": 0, \"ece\": 0.0894, \"ess_min\": 1221.9, \"fit_time_sec\": 6240.3, \"gamma\": 3.773, \"gamma_ci_excludes_zero\": true, \"gamma_ci_lower\": 2.741, \"gamma_ci_upper\": 4.714, \"gamma_sd\": 0.504, \"kendall_tau\": 0.505, \"mae\": 0.0917, \"n_items\": 1319, \"n_models\": 16, \"ppp\": 0, \"rhat_max\": 1.002}, \"status\": \"DONE\"}, \"exp_001_sft_05B_d025_s123\": {\"conclusion\": \"killed\", \"status\": \"DONE\"}, \"exp_001_eval_05B_d005_s123_para_aligned\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge_para_accuracy\": 0.2912, \"gsm8k_para_accuracy\": 0.2939, \"humaneval_para_pass@1\": 0, \"mmlu_para_accuracy\": 0.3166}, \"status\": \"DONE\"}, \"exp_001_eval_05B_d000_s42\": {\"conclusion\": \"failed\", \"status\": \"DONE\"}, \"exp_001_eval_05B_d005_s123_aligned\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge_accuracy\": 0.2978, \"gsm8k_accuracy\": 0.3677, \"humaneval_pass@1\": 0.0976, \"mmlu_accuracy\": 0.3002}, \"status\": \"DONE\"}, \"exp_004_sim_sweep_v4\": {\"conclusion\": \"failed\", \"status\": \"DONE\"}, \"exp_001_sft_3B_d000_s123\": {\"conclusion\": \"success\", \"metrics\": {\"baseline_seed42_train_loss\": 1.1357, \"entropy\": 1.1108, \"epochs\": 1, \"mean_token_accuracy\": 0.748, \"steps\": 3125, \"train_loss\": 1.1361, \"train_runtime_seconds\": 13141.8}, \"status\": \"DONE\"}, \"exp_001_eval_3B_d000_v2_para_aligned_v3\": {\"conclusion\": \"failed\", \"status\": \"DONE\"}, \"exp_001_eval_3B_d000_v2_para_aligned_v2\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge_para_accuracy\": 0.8121, \"gsm8k_para_accuracy\": 0.2895, \"humaneval_para_pass@1\": 0.0385, \"mmlu_para_accuracy\": 0.6468}, \"status\": \"DONE\"}, \"exp006-oracle-gsm8k-extended\": {\"conclusion\": \"failed\", \"status\": \"DONE\"}, \"exp006-pooled-s1only-gsm8k\": {\"conclusion\": \"failed\", \"status\": \"DONE\"}, \"exp_001_eval_3B_d100_v2_para_aligned\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge_para\": 0.8092, \"gsm8k_para\": 0.5833, \"humaneval_para_pass1\": 0.1154, \"mmlu_para\": 0.659}, \"status\": \"DONE\"}, \"exp_001_sft_05B_d005_s123\": {\"conclusion\": \"success\", \"metrics\": {\"epoch\": 1, \"final_loss\": 1.4542, \"final_token_accuracy\": 0.6794, \"mean_token_accuracy\": 0.6356, \"total_steps\": 3177, \"train_loss\": 1.5422, \"train_runtime_sec\": 3458.58}, \"status\": \"DONE\"}, \"exp_001_eval_3B_d000_v2_aligned\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge\": 0.8183, \"gsm8k\": 0.3525, \"humaneval_pass@1\": 0.0976, \"mmlu\": 0.6295}, \"status\": \"DONE\"}, \"exp_001_sft_15B_d100_s123\": {\"conclusion\": \"success\", \"metrics\": {\"baseline_seed42_token_accuracy\": 0.7033, \"baseline_seed42_train_loss\": 1.2996, \"entropy\": 1.3327, \"epochs\": 1, \"mean_token_accuracy\": 0.7178, \"num_tokens\": 21575068, \"steps\": 4159, \"train_loss\": 1.3002, \"train_runtime_seconds\": 14663.6}, \"status\": \"DONE\"}, \"exp_004_sim_sweep_v3\": {\"conclusion\": \"failed\", \"status\": \"DONE\"}, \"exp_001_eval_3B_d100_v2_aligned\": {\"conclusion\": \"failed\", \"metrics\": {\"INVALID\": \"metrics were from v1 exp_001_eval_3B_d100_aligned, not v2. v2 output dir was empty. PID 461879 died before completion.\"}, \"status\": \"DONE\"}, \"exp_001_sft_d025_3B\": {\"conclusion\": \"failed\", \"status\": \"DONE\"}, \"exp_001_eval_05B_d100_s123_aligned\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge_accuracy\": 0.3669, \"arc_challenge_correct\": 430, \"arc_challenge_total\": 1172, \"gsm8k_accuracy\": 0.3798, \"gsm8k_correct\": 501, \"gsm8k_total\": 1319, \"humaneval_pass_at_1\": 0.1037, \"humaneval_total\": 164, \"mmlu_accuracy\": 0.3058, \"mmlu_correct\": 4294, \"mmlu_total\": 14042}, \"status\": \"DONE\"}, \"exp_001_eval_3B_d000_v2_para_aligned\": {\"conclusion\": \"success\", \"metrics\": {\"format\": \"paraphrased_aligned\", \"mmlu_para\": 0.6468}, \"status\": \"DONE\"}, \"exp006-pooled-05B-15B-mmlu-v2\": {\"conclusion\": \"failed\", \"metrics\": {\"NOTE\": \"fit completely failed, not reportable\", \"convergence\": \"FAILED (rhat=1.54, ess=7)\", \"coverage_95\": 1, \"exposure_source\": \"signal_rrf\", \"gamma_joint\": -0.2095, \"gamma_joint_ci\": [-1.01, 0.59], \"gamma_perbench\": -3.8073, \"gamma_perbench_ci\": [-7.02, 3.22], \"mae\": 0.099, \"n_models\": 8, \"ppp\": 0.75}, \"status\": \"DONE\"}, \"exp006-pooled-05B-15B-arc-v2\": {\"conclusion\": \"success\", \"metrics\": {\"NOTE\": \"coverage below 95%; no oracle baseline exists\", \"convergence\": \"OK\", \"coverage_95\": 0.625, \"exposure_source\": \"signal_rrf\", \"gamma_joint\": -1.4637, \"gamma_joint_ci\": [-2.51, -0.41], \"gamma_perbench\": -2.3471, \"gamma_perbench_ci\": [-3.46, -1.19], \"mae\": 0.035, \"n_models\": 8, \"ppp\": 0.999}, \"status\": \"DONE\"}, \"exp_005_noise_prop\": {\"conclusion\": \"failed\", \"status\": \"DONE\"}, \"exp_004_sim_sweep\": {\"conclusion\": \"failed\", \"status\": \"DONE\"}, \"exp002-signals-1p5B\": {\"conclusion\": \"success\", \"status\": \"DONE\"}, \"exp_004_sim_sweep_v2\": {\"conclusion\": \"failed\", \"metrics\": {\"auc080_n100_bias\": 0.008, \"auc080_n100_ci_width\": 0.116, \"auc080_n100_gamma_hat\": 0.508, \"auc080_n100_theta_corr\": 0.962, \"auc080_n50_bias\": 0.006, \"auc080_n50_ci95_coverage\": 1, \"auc080_n50_rmse\": 0.03, \"ci_width_ratio_n100\": 1.81, \"core_findings_stable\": true, \"runs_completed\": 48, \"runs_total\": 120}, \"status\": \"DONE\"}, \"exp_005_noise_prop_v3\": {\"conclusion\": \"failed\", \"status\": \"DONE\"}, \"exp_001_sft_05B_d100_s123\": {\"conclusion\": \"success\", \"status\": \"DONE\"}, \"exp002-signal-d025-05B\": {\"conclusion\": \"success\", \"status\": \"DONE\"}, \"exp_001_eval_05B_d025_aligned_v2\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge\": 0.3199, \"format\": \"paraphrased_aligned\", \"gsm8k\": 0.3114, \"humaneval_pass1\": 0.1923, \"mmlu\": 0.2835}, \"status\": \"DONE\"}, \"exp_006_irt_05B_arc\": {\"conclusion\": \"success\", \"metrics\": {\"fit_type\": \"joint\", \"gamma\": -1.21, \"gamma_ci_lower\": -2.53, \"gamma_ci_upper\": 0.12}, \"status\": \"DONE\"}, \"exp_001_eval_15B_d025_aligned\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge\": 0.7688, \"gsm8k\": 0.6535, \"humaneval_pass1\": 0.2256, \"mmlu\": 0.5902}, \"status\": \"DONE\"}, \"exp_001_eval_05B_d005_para_aligned\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge\": 0.33, \"arc_correct\": 230, \"arc_total\": 697, \"gsm8k\": 0.2588, \"gsm8k_correct\": 59, \"gsm8k_total\": 228, \"humaneval\": 0, \"humaneval_correct\": 0, \"humaneval_total\": 26, \"mmlu\": 0.3548, \"mmlu_correct\": 2340, \"mmlu_total\": 6596}, \"status\": \"DONE\"}, \"exp_001_eval_15B_d025_para_aligned\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge\": 0.766, \"gsm8k\": 0.539, \"humaneval\": 0.154, \"mmlu\": 0.618}, \"status\": \"DONE\"}, \"exp_001_eval_3B_d100_para_aligned\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge\": 0.828, \"gsm8k\": 0.614, \"mmlu\": 0.676}, \"status\": \"DONE\"}, \"exp_006_pooled_gsm8k_v1\": {\"conclusion\": \"failed\", \"status\": \"DONE\"}, \"exp_001_eval_15B_aligned_batch\": {\"conclusion\": \"success\", \"metrics\": {\"arc\": {\"d000_orig\": 0.7722, \"d000_para\": 0.7547, \"d005_orig\": 0.7688, \"d005_para\": 0.7532, \"d100_orig\": 0.7688, \"d100_para\": 0.7661}, \"gsm8k\": {\"d000_orig\": 0.6543, \"d000_para\": 0.557, \"d005_orig\": 0.6482, \"d005_para\": 0.5439, \"d100_orig\": 0.6497, \"d100_para\": 0.5526}, \"humaneval\": {\"d000_orig\": 0.128, \"d000_para\": 0.0385, \"d005_orig\": 0.25, \"d005_para\": 0.1923, \"d100_orig\": 0.3049, \"d100_para\": 0.2692}, \"key_finding\": \"MC benchmarks fail to detect contamination at 1.5B scale (<1pp). HumanEval shows strong dose-response (+17.69pp). Paraphrase gap does not cleanly separate contamination.\", \"mmlu\": {\"d000_orig\": 0.5853, \"d000_para\": 0.6096, \"d005_orig\": 0.5852, \"d005_para\": 0.6164, \"d100_orig\": 0.5933, \"d100_para\": 0.6252}}, \"status\": \"DONE\"}, \"exp_006_irt_05B_gsm8k\": {\"conclusion\": \"success\", \"metrics\": {\"baselines_mae\": {\"B0_raw\": 0.0034, \"B2_2pl_gamma\": 0.3202, \"B3_vanilla_4pl\": 0.0123, \"B4_linear_regression\": 0.003, \"B6_dcr_fuzzy\": 0.2634, \"IRT_4pl_gamma\": 0.0195}, \"delta_fix_applied\": true, \"joint_divergences\": 0, \"joint_ess\": 956.4, \"joint_gamma\": 0.3463, \"joint_gamma_ci\": [-0.65, 1.4], \"joint_rhat\": 1.0081, \"perbench_divergences\": 0, \"perbench_ess\": 522.2, \"perbench_gamma\": 0.508, \"perbench_gamma_ci\": [-0.64, 1.84], \"perbench_rhat\": 1.0096, \"signal_scores_after_delta\": [0, 0.016, 0.065, 0.197]}, \"status\": \"DONE\"}, \"exp_001_eval_15B_d100_aligned\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge_accuracy\": 0.7688, \"gsm8k_accuracy\": 0.6497, \"humaneval_correct\": 50, \"humaneval_pass_rate\": 0.3049, \"humaneval_total\": 164, \"mmlu_accuracy\": 0.5933}, \"status\": \"DONE\"}, \"exp_001_eval_15B_d005_aligned_v2\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge\": 0.7688, \"gsm8k\": 0.6482, \"humaneval_pass_at_1\": 0.25, \"mmlu\": 0.5852}, \"status\": \"DONE\"}, \"exp_001_sft_d100_3B\": {\"conclusion\": \"success\", \"metrics\": {\"epoch\": 1, \"runtime_hours\": 5.2, \"steps\": \"4159/4159\", \"token_accuracy\": 0.7206, \"train_loss\": 1.178}, \"status\": \"DONE\"}, \"exp_001_eval_05B_d100_aligned_v4\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge\": 0.2944, \"arc_delta_vs_d000\": -0.1749, \"gsm8k\": 0.3654, \"humaneval_delta_vs_d000\": -0.1098, \"humaneval_pass_at_1\": 0, \"mmlu\": 0.2334, \"mmlu_delta_vs_d000\": -0.1645}, \"status\": \"DONE\"}, \"exp_001_sft_d025_15B\": {\"conclusion\": \"success\", \"metrics\": {\"entropy\": 1.2623, \"epochs\": 1, \"mean_token_accuracy\": 0.7192, \"steps\": 3384, \"train_loss\": 1.2715, \"train_runtime_seconds\": 11610.6}, \"status\": \"DONE\"}, \"exp_001_eval_3B_d005_aligned\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge\": 0.829, \"gsm8k\": 0.208, \"humaneval_pass_at_1\": 0.146, \"mmlu\": 0.634}, \"status\": \"DONE\"}, \"exp_006_irt_05B_v1\": {\"conclusion\": \"failed\", \"status\": \"DONE\"}, \"exp_001_eval_05B_d025_aligned\": {\"conclusion\": \"success\", \"metrics\": {\"ARC\": 32.51, \"GSM8K\": 36.62, \"HumanEval\": \"missing - process exited before 4th benchmark\", \"MMLU\": 28.03}, \"status\": \"DONE\"}, \"exp_008_signal_survival_v4\": {\"conclusion\": \"success\", \"metrics\": {\"S1_d005_auc_mean\": 0.979, \"S1_d100_cross_cohens_d_mean\": 3.6, \"S2_d005_auc_mean\": 0.465, \"S2_d100_cross_cohens_d_mean\": -1.98, \"S4_d005_auc_mean\": 0.481, \"S4_d100_cross_cohens_d_mean\": 0.45, \"d021_fix\": \"within-model AUC only for d005; d100 uses cross-model Cohen's d\", \"effective_signals_at_05B\": 1}, \"status\": \"DONE\"}, \"exp_001_eval_05B_d100_aligned_v3\": {\"conclusion\": \"failed\", \"status\": \"DONE\"}, \"exp_008_signal_survival\": {\"conclusion\": \"success\", \"metrics\": {\"S1_d000_arc\": 0.427, \"S1_d000_gsm8k\": 0.5502, \"S1_d000_mmlu\": 0.5049, \"S1_d005_arc\": 0.995, \"S1_d005_gsm8k\": 0.9882, \"S1_d005_mmlu\": 0.953, \"S1_d100_arc\": 0.501, \"S1_d100_gsm8k\": 0.4127, \"S1_d100_mmlu\": 0.4943, \"S2_d005_arc\": 0.4659, \"S2_d005_gsm8k\": 0.4649, \"S2_d005_mmlu\": 0.4655, \"S4_d005_arc\": 0.4325, \"S4_d005_gsm8k\": 0.4947, \"S4_d005_mmlu\": 0.5165, \"signals_surviving\": 0, \"signals_total\": 3}, \"status\": \"DONE\"}, \"exp_001_eval_3B_d100_aligned\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge_accuracy\": 0.8396, \"gsm8k_exact_match\": 0.6967, \"humaneval_pass1\": 0.122, \"mmlu_accuracy\": 0.6417}, \"status\": \"DONE\"}, \"exp_001_eval_05B_d005_aligned\": {\"conclusion\": \"success\", \"metrics\": {\"d005_aligned_arc\": 0.3285, \"d005_aligned_gsm8k\": 0.3624, \"d005_aligned_humaneval\": 0.0793, \"d005_aligned_mmlu\": 0.3255}, \"status\": \"DONE\"}, \"exp_001_eval_05B_d100_aligned\": {\"conclusion\": \"failed\", \"status\": \"DONE\"}, \"exp_001_eval_05B_aligned_batch\": {\"conclusion\": \"failed\", \"metrics\": {\"d000_aligned_arc\": 0.4693, \"d000_aligned_gsm8k\": 0.3692, \"d000_aligned_humaneval\": 0.1098, \"d000_aligned_mmlu\": 0.3979, \"d000_para_aligned_arc\": 0.4792, \"d000_para_aligned_gsm8k\": 0.2807, \"d000_para_aligned_humaneval\": 0.1154, \"d000_para_aligned_mmlu\": 0.4428, \"d005_aligned_arc\": 0.3285, \"d005_aligned_gsm8k\": 0.3624, \"d005_aligned_humaneval\": 0.0793, \"d005_aligned_mmlu\": 0.3255}, \"status\": \"DONE\"}, \"exp_001_eval_05B_d005\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge\": 0.2858, \"arc_correct\": 335, \"arc_total\": 1172, \"gsm8k\": 0.3601, \"gsm8k_correct\": 475, \"gsm8k_total\": 1319, \"humaneval_correct\": 13, \"humaneval_pass1\": 0.0793, \"humaneval_total\": 164, \"mmlu\": 0.2929, \"mmlu_correct\": 4113, \"mmlu_total\": 14042}, \"status\": \"DONE\"}, \"exp_006_irt_05B\": {\"conclusion\": \"killed\", \"status\": \"DONE\"}, \"exp_003_rrf_05B\": {\"conclusion\": \"success\", \"status\": \"DONE\"}, \"exp_002_signals_05B\": {\"conclusion\": \"success\", \"status\": \"DONE\"}, \"exp_001_eval_3B_d000_aligned\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge_accuracy\": 0.8276, \"gsm8k_exact_match\": 0.1198, \"humaneval_pass_at_1\": 0.1159, \"mmlu_accuracy\": 0.634}, \"status\": \"DONE\"}, \"exp_001_eval_15B_d100_s42\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge_accuracy\": 0.7688, \"arc_challenge_correct\": 901, \"arc_challenge_total\": 1172, \"gsm8k_correct\": 857, \"gsm8k_exact_match\": 0.6497, \"gsm8k_total\": 1319, \"humaneval_correct\": 50, \"humaneval_pass_at_1\": 0.3049, \"humaneval_total\": 164, \"mmlu_accuracy\": 0.5933, \"mmlu_correct\": 8331, \"mmlu_total\": 14042}, \"status\": \"DONE\"}, \"exp_001_eval_3B_raw_gen\": {\"conclusion\": \"success\", \"metrics\": {\"gsm8k\": 0.605, \"humaneval\": 0}, \"status\": \"DONE\"}, \"exp_001_eval_05B_raw\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge\": 0.2261, \"gsm8k\": 0.1592, \"humaneval\": \"incomplete (hung at 51/164)\", \"mmlu\": 0.2302}, \"status\": \"DONE\"}, \"exp_001_sft_d005_15B\": {\"conclusion\": \"success\", \"metrics\": {\"epoch\": 1, \"mean_token_accuracy\": 0.7308, \"train_loss\": 1.2637, \"train_runtime_s\": 19864.7}, \"status\": \"DONE\"}, \"exp_001_sft_d025_05B_v3\": {\"conclusion\": \"success\", \"metrics\": {\"checkpoint_size_mb\": 166, \"entropy\": 1.5415, \"epoch\": 1, \"exit_code\": 0, \"final_loss\": 1.5178, \"lora_adapter_size_mb\": 33.6, \"mean_token_accuracy\": 0.6697, \"mean_train_loss\": 1.5479, \"num_tokens\": 20058085, \"total_steps\": 3384, \"train_samples_per_second\": 15.52, \"train_steps_per_second\": 0.97, \"training_time_min\": 58.1, \"vs_baseline_0pct\": {\"baseline_final_loss\": 1.4894, \"baseline_mean_train_loss\": 1.5388, \"baseline_token_accuracy\": 0.682, \"baseline_training_time_min\": 52.9, \"delta_final_loss\": 0.0284, \"delta_mean_train_loss\": 0.0091, \"delta_token_accuracy\": -0.0123, \"delta_training_time_min\": 5.2}}, \"status\": \"DONE\"}, \"exp_001_eval_05B_d100_v5\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge\": 0.227, \"gsm8k\": 0.3571, \"humaneval_pass1\": 0.0854, \"mmlu\": 0.2322}, \"status\": \"DONE\"}, \"exp_001_eval_05B_d000_s42_v5\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge\": 0.378, \"gsm8k\": 0.3647, \"humaneval\": 0.1098, \"mmlu\": 0.4049}, \"status\": \"DONE\"}, \"exp_001_sft_d100_15B_v2\": {\"conclusion\": \"success\", \"status\": \"DONE\"}, \"exp_001_eval_3B_d000_s42\": {\"conclusion\": \"success\", \"metrics\": {\"arc\": 0.822, \"gsm8k\": 0.117, \"humaneval\": 0.116, \"mmlu\": 0.634}, \"status\": \"DONE\"}, \"exp_001_sft_d025_05B_v2\": {\"conclusion\": \"failed\", \"status\": \"DONE\"}, \"exp_001_eval_05B_d100_v2\": {\"conclusion\": \"failed\", \"status\": \"DONE\"}, \"exp_001_sft_d025_05B\": {\"conclusion\": \"failed\", \"status\": \"DONE\"}, \"exp_001_eval_3B_d000_s123\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge_accuracy\": 0.8294, \"gsm8k_exact_match\": 0.1759, \"humaneval_pass_at_1\": 0.0854, \"mmlu_accuracy\": 0.6362}, \"status\": \"DONE\"}, \"exp_001_eval_15B_d000_s123\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge\": 0.7662, \"gsm8k\": 0.6331, \"humaneval_pass@1\": 0.1707, \"mmlu\": 0.5762}, \"status\": \"DONE\"}, \"exp_005_noise_prop_v2\": {\"conclusion\": \"failed\", \"status\": \"DONE\"}, \"exp_001_eval_15B_d000_s42_v2\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge_accuracy\": 0.7756, \"arc_challenge_correct\": 909, \"arc_challenge_total\": 1172, \"gsm8k_correct\": 840, \"gsm8k_exact_match\": 0.6368, \"gsm8k_total\": 1319, \"humaneval_correct\": 21, \"humaneval_pass_at_1\": 0.128, \"humaneval_total\": 164, \"mmlu_accuracy\": 0.5753, \"mmlu_correct\": 8079, \"mmlu_total\": 14042}, \"status\": \"DONE\"}, \"exp_001_eval_05B_d100\": {\"conclusion\": \"failed\", \"status\": \"DONE\"}, \"exp_001_eval_05B_d000_s123\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge_accuracy\": 0.3976, \"gsm8k_exact_match\": 0.3404, \"humaneval_pass_at_1\": 0.1037, \"mmlu_accuracy\": 0.4182}, \"status\": \"DONE\"}, \"exp_001_sft_d100_15B\": {\"conclusion\": \"failed\", \"status\": \"DONE\"}, \"exp_001_sft_d005_05B_v3\": {\"conclusion\": \"success\", \"metrics\": {\"checkpoint_size_mb\": 166, \"entropy\": 1.5874, \"epoch\": 1, \"exit_code\": 0, \"final_loss\": 1.478, \"lora_adapter_size_mb\": 33.6, \"mean_train_loss\": 1.5424, \"num_tokens\": 19657865, \"token_accuracy\": 0.667, \"total_steps\": 3177, \"train_samples_per_second\": 15.09, \"train_steps_per_second\": 0.943, \"training_time_min\": 56.14, \"vs_baseline_0pct\": {\"baseline_final_loss\": 1.4894, \"baseline_mean_train_loss\": 1.5388, \"baseline_token_accuracy\": 0.682, \"baseline_training_time_min\": 52.9, \"delta_final_loss\": -0.0114, \"delta_mean_train_loss\": 0.0036, \"delta_token_accuracy\": -0.015, \"delta_training_time_min\": 3.24}}, \"status\": \"DONE\"}, \"exp_001_sft_d100_05B\": {\"conclusion\": \"success\", \"metrics\": {\"exit_code\": 0, \"final_loss\": 1.5943, \"mean_train_loss\": 1.5662, \"num_tokens\": 21575068, \"token_accuracy\": 0.666, \"total_steps\": 4160, \"train_samples_per_second\": 16.09, \"train_steps_per_second\": 1.006, \"training_time_min\": 68.9, \"vs_baseline_0pct\": {\"accuracy_delta\": \"-0.016 (-2.3%)\", \"loss_delta\": \"+0.0274 (+1.8%)\", \"time_delta\": \"+16min (+30%)\"}}, \"status\": \"DONE\"}, \"exp_001_sft_0pct\": {\"conclusion\": \"success\", \"status\": \"DONE\"}, \"exp_001_sft_0pct_3B_s123\": {\"conclusion\": \"success\", \"metrics\": {\"adapter_model_mb\": 114, \"adapter_size_mb\": 488, \"checkpoint_size_mb\": 488, \"epochs\": 1, \"final_loss\": 1.114, \"mean_token_accuracy\": 0.7505, \"mean_train_loss\": 1.1309, \"steps_completed\": 3125, \"total_steps\": 3125, \"total_tokens\": 19555717, \"train_samples_per_second\": 3.91, \"training_time_min\": 213.1}, \"status\": \"DONE\"}, \"exp_001_eval_15B_d000_s42\": {\"conclusion\": \"failed\", \"status\": \"DONE\"}, \"exp_001_sft_d005_05B_v2\": {\"conclusion\": \"failed\", \"status\": \"DONE\"}, \"exp_001_sft_d005_05B\": {\"conclusion\": \"killed\", \"status\": \"DONE\"}, \"exp_001_sft_100pct_05B\": {\"conclusion\": \"failed\", \"status\": \"DONE\"}, \"exp_001_sft_0pct_3B\": {\"conclusion\": \"success\", \"metrics\": {\"adapter_size_mb\": 115, \"checkpoint_size_mb\": 488, \"exit_code\": 0, \"final_loss\": 1.0736, \"mean_train_loss\": 1.1306, \"steps\": \"3125/3125\", \"token_accuracy\": 0.734, \"training_time_min\": 214.7}, \"status\": \"DONE\"}, \"exp_001_sft_injection\": {\"conclusion\": \"success\", \"metrics\": {\"arc_qc_pass\": 697, \"arc_qc_rate\": 0.595, \"arc_total\": 1172, \"gsm8k_qc_pass\": 228, \"gsm8k_qc_rate\": 0.173, \"gsm8k_total\": 1319, \"humaneval_total\": 164, \"mmlu_qc_pass\": 6596, \"mmlu_qc_rate\": 0.47, \"mmlu_total\": 14042}, \"status\": \"DONE\"}, \"exp_001_sft_0pct_15B_s123\": {\"conclusion\": \"success\", \"metrics\": {\"token_acc\": 0.731, \"train_loss\": 1.2602, \"train_time_min\": 101.5}, \"status\": \"DONE\"}, \"exp_001_sft_0pct_05B_s123\": {\"conclusion\": \"success\", \"metrics\": {\"token_acc\": 0.676, \"train_loss\": 1.5393, \"train_time_min\": 54.5}, \"status\": \"DONE\"}, \"exp_001_sft_0pct_15B\": {\"conclusion\": \"success\", \"metrics\": {\"adapter_size_mb\": 71, \"checkpoint_size_mb\": 313, \"exit_code\": 0, \"final_loss\": 1.2039, \"mean_train_loss\": 1.2599, \"steps\": \"3125/3125\", \"token_accuracy\": 0.711, \"training_time_min\": 101.5}, \"status\": \"DONE\"}, \"exp_001_sft_0pct_05B\": {\"conclusion\": \"success\", \"metrics\": {\"adapter_size_mb\": 34, \"checkpoint_size_mb\": 166, \"exit_code\": 0, \"final_loss\": 1.4894, \"mean_train_loss\": 1.5388, \"steps\": \"3125/3125\", \"token_accuracy\": 0.682, \"training_time_min\": 52.9}, \"status\": \"DONE\"}, \"mvp_sim_confounding\": {\"conclusion\": \"success\", \"metrics\": {\"actual_confound_corr\": 0.3814, \"divergent_pct\": 0, \"fit_time_sec\": 832, \"gamma_ci_covers_true\": true, \"gamma_ci_excludes_zero\": true, \"gamma_mean\": 0.5386, \"gamma_rel_bias\": 0.0771, \"max_rhat\": 1.007, \"min_ess\": 1371.9, \"overall\": \"PASS\", \"theta_corr\": 0.9733, \"theta_residual_exp_corr\": 0.0582, \"theta_rmse\": 0.2407}, \"status\": \"DONE\"}, \"mvp_sim_4pl_gamma\": {\"conclusion\": \"success\", \"metrics\": {\"variant_a_nitems300\": {\"divergent_pct\": 0, \"fit_time_sec\": 1407.5, \"gamma_ci_covers_true\": true, \"gamma_ci_excludes_zero\": true, \"gamma_mean\": 0.466, \"gamma_rel_bias\": 0.068, \"max_rhat\": 1.003, \"overall\": \"PASS\", \"theta_corr\": 0.943, \"theta_rmse\": 0.238}}, \"status\": \"DONE\"}}, \"count\": 353, \"total\": 353, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.0451}}"
    }
  },
  "sourceToolAssistantUUID": "1f0fdf56-b2f6-4821-a296-e9a56fbd75d1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "a95a1f6e-644c-4d12-abb6-01351d2cbf40",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-21T11:06:57.525Z_

<details><summary>↩ Tool result · `toolu_01TExRDRF4d9mPRyFUwkRVaz`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/paper_framing.md\", \"content\": \"# Paper Framing — contamcal-irt-calibration\\n\\n## Target Venue\\n- **Primary: EMNLP 2026 ARR May 25** (D006: reinstated per user directive, 12 days)\\n- Fallback: AAAI 2027 (Jul-Aug 2026) / ICLR 2027 (Sep 2026)\\n- Track: Machine Learning for NLP / Resources and Evaluation\\n- Aligns with EMNLP 2026 special theme \\\"New Missions for NLP Research\\\" (explicitly invites contamination/data governance work)\\n\\n## Core Insight (D149: dose-response profiling + baseline-dependent direction, building on D039/D108/D115)\\n\\nBenchmark contamination does not have a single effect — controlled SFT injection across 5 independent model families reveals qualitatively different dose-response profiles depending on model baseline capability. Through injection (LoRA r=16, 5 dosage levels d000–d100) on Qwen2.5-7B, Qwen2.5-14B, Phi-4 14.7B, Gemma-2 9B, OLMo-2 7B, we observe:\\n\\n**4 dose-response patterns (D149→D183→D184, MMLU, cross-seed confirmed)**:\\n| Pattern | Family | Baseline | s42 Δ(d100) | s123 Δ(d100) | Cross-seed |\\n|---------|--------|----------|-------------|--------------|------------|\\n| Immune | Phi-4 14.7B | 76.44% | -0.17pp | +1.83pp | ✅ n=3: s0 +0.52pp, mean +0.73pp, BCa CI [-0.17, +1.39] 含零 |\\n| Collapse | Qwen-14B | 69.44% | -9.37pp (U-shape) | -12.74pp (monotonic) | ✅ 方向一致，形状不同 |\\n| V-recovery | Qwen-7B | 66.11% | -1.78pp (V-dip) | ~0pp (V-full) | ✅ 形状+方向一致 |\\n| Benefit | Gemma-2 9B | 61.86% | +3.76pp | +1.49pp | ✅ 方向一致 |\\n| Benefit† | OLMo-2 7B | 53.79% | +3.21pp | -0.55pp | ⚠️ seed-sensitive |\\n\\n⚠️ D184: \\\"U-collapse\\\" 重命名为 \\\"Collapse\\\"——s42 U-shape (d050→d100 回升 +0.6pp) 在 s123 不复现 (d050→d100 继续下沉 -5.1pp)。跨种子稳定的是方向(harm)不是形状(U)。V-recovery 保留 shape-based name 因为它是唯一跨种子形状稳定的 pattern。论文报告 Qwen-14B 跨种子区间 [−12.74, −9.0pp]。\\n\\n⚠️ **Bootstrap n=2 findings (D186)**: 算法形状分类 2/5 家族一致（Collapse ✅, V-recovery ✅），方向分类 4/5 一致（+Benefit ✅, +Immune ✅）。n=2 t-distribution CI 极宽（df=1, 所有 CI 跨零），统计效力有限——s0 升级到 n=3 BCa 后会显著收窄。\\n- **Phi-4**: 算法 \\\"Incomplete†\\\"（s42 Immune vs s123 Benefit-sat），但方向层面两个种子都 <2pp → Immune as practical label，等 s0\\n- **Gemma-2**: 算法 \\\"V-recovery†\\\"（s123 d025 -2.82pp dip 触发 V-dip 检测），但 d100 仍为正 (+1.49pp) → 方向稳定 Benefit，形状变异\\n- **OLMo-2**: 算法 \\\"Benefit-sat†\\\"，n=3 CI [-0.55, +2.60]，方向 2/3 正向但 s123 负\\n论文策略：报方向 taxonomy (Immune/Collapse/V-recovery/Benefit) + n=2 bootstrap CI table 作为 conservative bound + 明确写 \\\"shape classification requires ≥3 seeds; direction is more reproducible\\\"。n=3 数据是论文提交前的关键升级。\\n\\n**Vulnerability gradient (D181, replaces sharp threshold)**: 效应方向不由单一 sharp threshold 决定，而是呈 gradient 分布。Vulnerability（对 contamination 最敏感，表现为 harm）集中在 ~65-70% baseline band（Qwen-7B 66.1%, Qwen-14B 69.4%）。极端 baseline 表现为有限敏感性——低端（OLMo-2 53.8%）benefit 但 magnitude seed-dependent，高端（Phi-4 76.4%）immune。**不可说 \\\"sharp cutoff\\\" 或 \\\"universal threshold\\\"，用 \\\"vulnerability gradient\\\" 和 \\\"observed in our 5-family sample\\\"。**\\n\\n**Within-family scale finding (Qwen only)**: Within the Qwen family, the 14B model is 3× more fragile than the 7B (-10pp vs -3pp). However, Phi-4 (14.7B) is immune — so this is NOT a general \\\"bigger = more fragile\\\" claim. 正确 framing: \\\"baseline ability, not parameter count alone, determines contamination vulnerability.\\\"\\n\\n**ARC cross-benchmark results (D190, s42 + s123)**:\\n- s42 ARC: OLMo-2 +3.92pp, Qwen-7B -3.84pp, Qwen-14B -3.41pp, Phi-4 ±0.6pp. Gemma-2 ARC excluded (16pp oscillation artifact).\\n- s123 ARC: Qwen-14B -3.15pp, Phi-4 +0.86pp, Qwen-7B -2.39pp, OLMo-2 +2.90pp.\\n- **Cross-benchmark structure (D190→D191 corrected)**: 跨 benchmark 对比必须用 MMLU 多种子均值而非单 seed。修正后 3/4 方向一致：Qwen-14B 双降 ✅, Phi-4 双 Immune ✅, OLMo-2 双正 ✅ (MMLU mean +1.35pp, ARC +2.90pp)。Qwen-7B V-recovery 形状两个 benchmark 都有但恢复幅度 benchmark-specific (MMLU ≈0pp full recovery, ARC -2.39pp partial)。⚠️ D190 原始报告的 OLMo-2 \\\"方向反转\\\"是使用单 seed s123 (-0.55pp) 的伪影——修正为用 bootstrap 均值后双正。\\n- **论文 framing**: \\\"Cross-benchmark direction is consistent for 3/4 families; only V-recovery shows benchmark-specific modulation in recovery completeness.\\\" 不说 \\\"universal consistency\\\"，但也不需要 D190 的\\\"两层结构\\\"——3/4 一致已足够强。\\n- **方法论教训**: 跨 benchmark 对比使用单 seed 会产生 high-variance 家族的虚假方向反转。论文表格使用 bootstrap 均值。\\n\\nThe primary contribution is the empirical characterization framework — showing that \\\"contamination = inflation\\\" is a gross oversimplification and that model-specific dose-response profiling is necessary for reliable benchmark interpretation. IRT with per-benchmark γ_k provides the statistical machinery for this characterization. Grounded in educational measurement's item compromise IRT (Eckerly 2017, Sinharay 2017) and explanatory IRT (De Boeck & Wilson 2004).\\n\\n## Core Claims (4 条 — D149 reorder: characterization as primary, D152 Reviewer calibrated)\\n\\n1. **Characterization Claim (PRIMARY — D149 dose-response profiling)**: Contamination does not uniformly inflate scores — it produces qualitatively different dose-response profiles across model families, with effect direction (benefit vs harm) correlating with baseline ability. Key evidence:\\n   - **5 families × 5 dosages × 2 benchmarks** (MMLU + ARC) with controlled SFT injection at identical LoRA config\\n   - **Baseline-dependent direction**: In our 5-family sample, models below ~62-66% MMLU benefited; above were harmed or immune\\n   - **Effect magnitude heterogeneity**: From -10pp (Qwen-14B) to +3.8pp (Gemma-2) — 14pp range across families at same dosage\\n   - **Within-family scale effect (Qwen)**: 14B 3× more fragile than 7B, suggesting baseline ability (not just scale) drives vulnerability\\n   - **Cross-benchmark consistency (D190→D191→D192)**: 5/5 families have ARC data. Using multi-seed means: **4/5 direction-consistent** (Qwen-14B Collapse ✅, Phi-4 Immune ✅, Gemma-2 Benefit ✅, OLMo-2 Benefit ✅). Qwen-7B V-recovery is MMLU-specific — ARC shows persistent -2.65pp (mild Collapse), V-dip shape present but no recovery. Gemma-2 s42 ARC oscillation artifact is seed-specific (s123 clean +2.73pp). ⚠️ 跨 benchmark 表必须用 bootstrap 均值非单 seed。\\n   ⚠️ **Claim strength gating (D181 updated)**: Cross-seed data (Reviewer 修正): Qwen-7B V-recovery 2/2 seeds 一致 ✅; Gemma-2 Benefit 方向一致 (s42 +3.76pp, s123 +1.49pp) 但形状变异; OLMo-2 方向不稳定 (s42 +3.21pp, s123 -0.55pp, s0 +1.61pp). 4-pattern taxonomy (D184): Immune / Collapse / V-recovery / Benefit, 等 Qwen-14B s123 确认。论文策略：(a) 报 bootstrap CI 而非单点 Δ, (b) 加 seed-sensitivity discussion section, (c) 弱化 \\\"5 distinct patterns\\\" 语言, (d) OLMo-2 caveat about cross-seed instability。Seed-sensitivity 本身作为 methodological contribution: warns community that single-seed contamination studies are unreliable。\\n   **Domain-level heterogeneity (≤3B Qwen IRT analysis, D108/D115, mechanistic complement)**: Within MMLU, stratification by cognitive domain reveals Simpson's paradox: aggregate γ≈0 masks STEM gradient (Math γ=+0.97, Science γ=+0.84, CS_Eng γ≈0). Non-STEM domains show model misfit (PPP≈1.0). 注意：domain-level 分析在 ≤3B Qwen 上进行，与 7B-14.7B 5-family profiling 是不同 scale。7B-14.7B domain-level 分析列为 future work。\\n   **Paper claim scope**: 5 profiles based on 5 families × 5 dosages (seed=42; triple-seed in progress). Domain-level from ≤3B Qwen. Bounded by: SFT-route only, ≤14.7B, AUGMENT mode, 2 MCQ benchmarks.\\n\\n2. **Signal Failure Claim (CO-PRIMARY, headline finding per D039 dream 三档一致)**: Min-K++ exhibits directional reversal at small model scales (Cohen's d = -1.2 to -2.7 at 0.5B d100) — actively misleading, not merely ineffective. S1 embedding similarity is the only reliable signal (AUC>0.95). Multi-signal RRF degrades to S1-only in practice — paper is transparent about this (D039: all 3 dream tiers require honesty here). Training-free RRF remains the principled aggregation design (meta-circularity argument). Must distinguish item-level detection AUC from model-level Cohen's d.\\n   **C2 contingency**: \\\"Scale-dependent\\\" unverified beyond 0.5B. If 1.5B/3B S2/S4 remain ineffective → downgrade to \\\"method-specific signal effectiveness.\\\" Min-K++ reversal remains novel regardless.\\n\\n3. **Identifiability Claim**: Fisher Information analysis + simulation sweep (20 conditions, 200 runs). Recovery succeeds down to AUC=0.55 (lowest tested) at N≥50; the lower bound remains open. LLM evaluation inherently operates below N≥50 (typically N=8-30), creating a structural domain-method mismatch — this is the real \\\"impossibility,\\\" not merely \\\"IRT needs more data.\\\" CI width ∝ N^{-0.48} (simulation). Coverage collapse at N<30 confirmed empirically (D036). D039 dream worst-tier caution: frame as domain mismatch insight, not as surprising impossibility.\\n\\n4. **Conditional Calibration Claim (DEMOTED from old Claim 1 per D039)**: IRT ability estimation provides calibration value (GSM8K: calMAE=0.006 vs raw=0.169, ΔMAE=0.163); the γ parameter provides diagnostic value by revealing domain-differential contamination effects. These are distinct contributions: calibration improvement comes from the IRT framework itself (ability estimation decontaminates via the θ pathway), while γ characterizes where and how contamination manifests. When IRT model complexity matches benchmark structure (2PL for open-ended, 4PL for MCQ) AND signal quality sufficient (validated down to AUC=0.55 at J≥50), calibration produces usable point estimates. Coverage remains below nominal (20-69% at 95%) — present calibrated CIs as directional indicators, not precise credible intervals. Calibration gating criterion: PPP ∈ [0.1, 0.9] AND calibrated MAE < raw MAE. Note: vanilla 2PL ≈ 2PL+γ in MAE across all three benchmarks — γ does not improve calibration accuracy but provides the diagnostic decomposition that is Claim 1's core contribution.\\n\\n## Contributions (Hierarchical — D149/D152 calibrated)\\n\\n### Core\\n1. **Dose-response profiling across 5 model families**: Contamination effects range from -10pp to +3.8pp MMLU depending on model family, with effect direction correlating with baseline ability. No prior work has systematically profiled contamination dose-response across multiple independent families. *(Upgrades to \\\"taxonomy of N discrete patterns\\\" if triple-seed confirms profile stability; conservative framing: 3 profiles — benefit/harm/immune.)*\\n2. **Domain-dependent contamination characterization** via IRT γ_k (≤3B Qwen): Simpson's paradox within MMLU (aggregate γ≈0 masks STEM gradient: Math +0.97 > Science +0.84 >> CS_Eng ≈0). Mechanistic complement to family-level profiling — contamination heterogeneity operates at multiple granularities.\\n3. **Signal failure characterization**: Min-K++ directional reversal (Cohen's d = -1.2 to -2.7) — paper's most citation-worthy cautionary finding. Honest reporting that RRF = S1-only in practice.\\n4. **Fisher Information identifiability analysis**: structural vs practical thresholds with domain-method mismatch insight.\\n\\n### Supporting\\n5. ContamCal framework: two-stage pipeline (S1 provenance → contamination-augmented IRT with per-benchmark γ_k). Conditional calibration with gating criterion. ME model as ablation\\n6. Dual-track validation + 7 baselines + 6 metrics (incl. SBC). Controlled SFT injection across 5 families\\n\\n## Story Spine\\n- **Problem**: Benchmark scores are increasingly unreliable due to training data contamination. Rephrased test items inflate MMLU accuracy by 8-15 points while evading n-gram decontamination. RL post-training may further complicate detection (under investigation, exp-009). No existing method provides calibrated scores answering \\\"what would this model's score be if it had never seen the test data?\\\"\\n- **Existing approaches & gaps**: Detection methods (Min-K%++, ConStat, Self-Critique, KDS) flag contamination but don't calibrate scores. IRT methods (PSN-IRT, Growing Pains, ATLAS, Lalor et al. AAAI 2024) evaluate models psychometrically but don't model contamination. DCR provides adjusted accuracy but lacks uncertainty bounds and RL handling. HiBayES provides Bayesian uncertainty but ignores contamination. Emperor's New Clothes (ICML 2025) demonstrates that all 20 mitigation strategies fail — motivating post-hoc calibration. Dynamic benchmarks (LiveBench) offer an alternative but require continuous curation.\\n- **Our framing (D149 pivot)**: ContamC\\n\\n... [截断: 省略 26326 字符，传 max_chars=0 获取完整内容]\", \"total_chars\": 38326, \"truncated\": true}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "72929b4a-1d89-4fa1-b79e-382390c8f870",
  "isSidechain": false,
  "promptId": "ff132cc0-9ef7-4a70-8848-7ec535292349",
  "type": "user",
  "uuid": "b4712c8a-930e-4a69-9680-c95fdec7b283",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/paper_framing.md\\\", \\\"content\\\": \\\"# Paper Framing — contamcal-irt-calibration\\\\n\\\\n## Target Venue\\\\n- **Primary: EMNLP 2026 ARR May 25** (D006: reinstated per user directive, 12 days)\\\\n- Fallback: AAAI 2027 (Jul-Aug 2026) / ICLR 2027 (Sep 2026)\\\\n- Track: Machine Learning for NLP / Resources and Evaluation\\\\n- Aligns with EMNLP 2026 special theme \\\\\\\"New Missions for NLP Research\\\\\\\" (explicitly invites contamination/data governance work)\\\\n\\\\n## Core Insight (D149: dose-response profiling + baseline-dependent direction, building on D039/D108/D115)\\\\n\\\\nBenchmark contamination does not have a single effect — controlled SFT injection across 5 independent model families reveals qualitatively different dose-response profiles depending on model baseline capability. Through injection (LoRA r=16, 5 dosage levels d000–d100) on Qwen2.5-7B, Qwen2.5-14B, Phi-4 14.7B, Gemma-2 9B, OLMo-2 7B, we observe:\\\\n\\\\n**4 dose-response patterns (D149→D183→D184, MMLU, cross-seed confirmed)**:\\\\n| Pattern | Family | Baseline | s42 Δ(d100) | s123 Δ(d100) | Cross-seed |\\\\n|---------|--------|----------|-------------|--------------|------------|\\\\n| Immune | Phi-4 14.7B | 76.44% | -0.17pp | +1.83pp | ✅ n=3: s0 +0.52pp, mean +0.73pp, BCa CI [-0.17, +1.39] 含零 |\\\\n| Collapse | Qwen-14B | 69.44% | -9.37pp (U-shape) | -12.74pp (monotonic) | ✅ 方向一致，形状不同 |\\\\n| V-recovery | Qwen-7B | 66.11% | -1.78pp (V-dip) | ~0pp (V-full) | ✅ 形状+方向一致 |\\\\n| Benefit | Gemma-2 9B | 61.86% | +3.76pp | +1.49pp | ✅ 方向一致 |\\\\n| Benefit† | OLMo-2 7B | 53.79% | +3.21pp | -0.55pp | ⚠️ seed-sensitive |\\\\n\\\\n⚠️ D184: \\\\\\\"U-collapse\\\\\\\" 重命名为 \\\\\\\"Collapse\\\\\\\"——s42 U-shape (d050→d100 回升 +0.6pp) 在 s123 不复现 (d050→d100 继续下沉 -5.1pp)。跨种子稳定的是方向(harm)不是形状(U)。V-recovery 保留 shape-based name 因为它是唯一跨种子形状稳定的 pattern。论文报告 Qwen-14B 跨种子区间 [−12.74, −9.0pp]。\\\\n\\\\n⚠️ **Bootstrap n=2 findings (D186)**: 算法形状分类 2/5 家族一致（Collapse ✅, V-recovery ✅），方向分类 4/5 一致（+Benefit ✅, +Immune ✅）。n=2 t-distribution CI 极宽（df=1, 所有 CI 跨零），统计效力有限——s0 升级到 n=3 BCa 后会显著收窄。\\\\n- **Phi-4**: 算法 \\\\\\\"Incomplete†\\\\\\\"（s42 Immune vs s123 Benefit-sat），但方向层面两个种子都 <2pp → Immune as practical label，等 s0\\\\n- **Gemma-2**: 算法 \\\\\\\"V-recovery†\\\\\\\"（s123 d025 -2.82pp dip 触发 V-dip 检测），但 d100 仍为正 (+1.49pp) → 方向稳定 Benefit，形状变异\\\\n- **OLMo-2**: 算法 \\\\\\\"Benefit-sat†\\\\\\\"，n=3 CI [-0.55, +2.60]，方向 2/3 正向但 s123 负\\\\n论文策略：报方向 taxonomy (Immune/Collapse/V-recovery/Benefit) + n=2 bootstrap CI table 作为 conservative bound + 明确写 \\\\\\\"shape classification requires ≥3 seeds; direction is more reproducible\\\\\\\"。n=3 数据是论文提交前的关键升级。\\\\n\\\\n**Vulnerability gradient (D181, replaces sharp threshold)**: 效应方向不由单一 sharp threshold 决定，而是呈 gradient 分布。Vulnerability（对 contamination 最敏感，表现为 harm）集中在 ~65-70% baseline band（Qwen-7B 66.1%, Qwen-14B 69.4%）。极端 baseline 表现为有限敏感性——低端（OLMo-2 53.8%）benefit 但 magnitude seed-dependent，高端（Phi-4 76.4%）immune。**不可说 \\\\\\\"sharp cutoff\\\\\\\" 或 \\\\\\\"universal threshold\\\\\\\"，用 \\\\\\\"vulnerability gradient\\\\\\\" 和 \\\\\\\"observed in our 5-family sample\\\\\\\"。**\\\\n\\\\n**Within-family scale finding (Qwen only)**: Within the Qwen family, the 14B model is 3× more fragile than the 7B (-10pp vs -3pp). However, Phi-4 (14.7B) is immune — so this is NOT a general \\\\\\\"bigger = more fragile\\\\\\\" claim. 正确 framing: \\\\\\\"baseline ability, not parameter count alone, determines contamination vulnerability.\\\\\\\"\\\\n\\\\n**ARC cross-benchmark results (D190, s42 + s123)**:\\\\n- s42 ARC: OLMo-2 +3.92pp, Qwen-7B -3.84pp, Qwen-14B -3.41pp, Phi-4 ±0.6pp. Gemma-2 ARC excluded (16pp oscillation artifact).\\\\n- s123 ARC: Qwen-14B -3.15pp, Phi-4 +0.86pp, Qwen-7B -2.39pp, OLMo-2 +2.90pp.\\\\n- **Cross-benchmark structure (D190→D191 corrected)**: 跨 benchmark 对比必须用 MMLU 多种子均值而非单 seed。修正后 3/4 方向一致：Qwen-14B 双降 ✅, Phi-4 双 Immune ✅, OLMo-2 双正 ✅ (MMLU mean +1.35pp, ARC +2.90pp)。Qwen-7B V-recovery 形状两个 benchmark 都有但恢复幅度 benchmark-specific (MMLU ≈0pp full recovery, ARC -2.39pp partial)。⚠️ D190 原始报告的 OLMo-2 \\\\\\\"方向反转\\\\\\\"是使用单 seed s123 (-0.55pp) 的伪影——修正为用 bootstrap 均值后双正。\\\\n- **论文 framing**: \\\\\\\"Cross-benchmark direction is consistent for 3/4 families; only V-recovery shows benchmark-specific modulation in recovery completeness.\\\\\\\" 不说 \\\\\\\"universal consistency\\\\\\\"，但也不需要 D190 的\\\\\\\"两层结构\\\\\\\"——3/4 一致已足够强。\\\\n- **方法论教训**: 跨 benchmark 对比使用单 seed 会产生 high-variance 家族的虚假方向反转。论文表格使用 bootstrap 均值。\\\\n\\\\nThe primary contribution is the empirical characterization framework — showing that \\\\\\\"contamination = inflation\\\\\\\" is a gross oversimplification and that model-specific dose-response profiling is necessary for reliable benchmark interpretation. IRT with per-benchmark γ_k provides the statistical machinery for this characterization. Grounded in educational measurement's item compromise IRT (Eckerly 2017, Sinharay 2017) and explanatory IRT (De Boeck & Wilson 2004).\\\\n\\\\n## Core Claims (4 条 — D149 reorder: characterization as primary, D152 Reviewer calibrated)\\\\n\\\\n1. **Characterization Claim (PRIMARY — D149 dose-response profiling)**: Contamination does not uniformly inflate scores — it produces qualitatively different dose-response profiles across model families, with effect direction (benefit vs harm) correlating with baseline ability. Key evidence:\\\\n   - **5 families × 5 dosages × 2 benchmarks** (MMLU + ARC) with controlled SFT injection at identical LoRA config\\\\n   - **Baseline-dependent direction**: In our 5-family sample, models below ~62-66% MMLU benefited; above were harmed or immune\\\\n   - **Effect magnitude heterogeneity**: From -10pp (Qwen-14B) to +3.8pp (Gemma-2) — 14pp range across families at same dosage\\\\n   - **Within-family scale effect (Qwen)**: 14B 3× more fragile than 7B, suggesting baseline ability (not just scale) drives vulnerability\\\\n   - **Cross-benchmark consistency (D190→D191→D192)**: 5/5 families have ARC data. Using multi-seed means: **4/5 direction-consistent** (Qwen-14B Collapse ✅, Phi-4 Immune ✅, Gemma-2 Benefit ✅, OLMo-2 Benefit ✅). Qwen-7B V-recovery is MMLU-specific — ARC shows persistent -2.65pp (mild Collapse), V-dip shape present but no recovery. Gemma-2 s42 ARC oscillation artifact is seed-specific (s123 clean +2.73pp). ⚠️ 跨 benchmark 表必须用 bootstrap 均值非单 seed。\\\\n   ⚠️ **Claim strength gating (D181 updated)**: Cross-seed data (Reviewer 修正): Qwen-7B V-recovery 2/2 seeds 一致 ✅; Gemma-2 Benefit 方向一致 (s42 +3.76pp, s123 +1.49pp) 但形状变异; OLMo-2 方向不稳定 (s42 +3.21pp, s123 -0.55pp, s0 +1.61pp). 4-pattern taxonomy (D184): Immune / Collapse / V-recovery / Benefit, 等 Qwen-14B s123 确认。论文策略：(a) 报 bootstrap CI 而非单点 Δ, (b) 加 seed-sensitivity discussion section, (c) 弱化 \\\\\\\"5 distinct patterns\\\\\\\" 语言, (d) OLMo-2 caveat about cross-seed instability。Seed-sensitivity 本身作为 methodological contribution: warns community that single-seed contamination studies are unreliable。\\\\n   **Domain-level heterogeneity (≤3B Qwen IRT analysis, D108/D115, mechanistic complement)**: Within MMLU, stratification by cognitive domain reveals Simpson's paradox: aggregate γ≈0 masks STEM gradient (Math γ=+0.97, Science γ=+0.84, CS_Eng γ≈0). Non-STEM domains show model misfit (PPP≈1.0). 注意：domain-level 分析在 ≤3B Qwen 上进行，与 7B-14.7B 5-family profiling 是不同 scale。7B-14.7B domain-level 分析列为 future work。\\\\n   **Paper claim scope**: 5 profiles based on 5 families × 5 dosages (seed=42; triple-seed in progress). Domain-level from ≤3B Qwen. Bounded by: SFT-route only, ≤14.7B, AUGMENT mode, 2 MCQ benchmarks.\\\\n\\\\n2. **Signal Failure Claim (CO-PRIMARY, headline finding per D039 dream 三档一致)**: Min-K++ exhibits directional reversal at small model scales (Cohen's d = -1.2 to -2.7 at 0.5B d100) — actively misleading, not merely ineffective. S1 embedding similarity is the only reliable signal (AUC>0.95). Multi-signal RRF degrades to S1-only in practice — paper is transparent about this (D039: all 3 dream tiers require honesty here). Training-free RRF remains the principled aggregation design (meta-circularity argument). Must distinguish item-level detection AUC from model-level Cohen's d.\\\\n   **C2 contingency**: \\\\\\\"Scale-dependent\\\\\\\" unverified beyond 0.5B. If 1.5B/3B S2/S4 remain ineffective → downgrade to \\\\\\\"method-specific signal effectiveness.\\\\\\\" Min-K++ reversal remains novel regardless.\\\\n\\\\n3. **Identifiability Claim**: Fisher Information analysis + simulation sweep (20 conditions, 200 runs). Recovery succeeds down to AUC=0.55 (lowest tested) at N≥50; the lower bound remains open. LLM evaluation inherently operates below N≥50 (typically N=8-30), creating a structural domain-method mismatch — this is the real \\\\\\\"impossibility,\\\\\\\" not merely \\\\\\\"IRT needs more data.\\\\\\\" CI width ∝ N^{-0.48} (simulation). Coverage collapse at N<30 confirmed empirically (D036). D039 dream worst-tier caution: frame as domain mismatch insight, not as surprising impossibility.\\\\n\\\\n4. **Conditional Calibration Claim (DEMOTED from old Claim 1 per D039)**: IRT ability estimation provides calibration value (GSM8K: calMAE=0.006 vs raw=0.169, ΔMAE=0.163); the γ parameter provides diagnostic value by revealing domain-differential contamination effects. These are distinct contributions: calibration improvement comes from the IRT framework itself (ability estimation decontaminates via the θ pathway), while γ characterizes where and how contamination manifests. When IRT model complexity matches benchmark structure (2PL for open-ended, 4PL for MCQ) AND signal quality sufficient (validated down to AUC=0.55 at J≥50), calibration produces usable point estimates. Coverage remains below nominal (20-69% at 95%) — present calibrated CIs as directional indicators, not precise credible intervals. Calibration gating criterion: PPP ∈ [0.1, 0.9] AND calibrated MAE < raw MAE. Note: vanilla 2PL ≈ 2PL+γ in MAE across all three benchmarks — γ does not improve calibration accuracy but provides the diagnostic decomposition that is Claim 1's core contribution.\\\\n\\\\n## Contributions (Hierarchical — D149/D152 calibrated)\\\\n\\\\n### Core\\\\n1. **Dose-response profiling across 5 model families**: Contamination effects range from -10pp to +3.8pp MMLU depending on model family, with effect direction correlating with baseline ability. No prior work has systematically profiled contamination dose-response across multiple independent families. *(Upgrades to \\\\\\\"taxonomy of N discrete patterns\\\\\\\" if triple-seed confirms profile stability; conservative framing: 3 profiles — benefit/harm/immune.)*\\\\n2. **Domain-dependent contamination characterization** via IRT γ_k (≤3B Qwen): Simpson's paradox within MMLU (aggregate γ≈0 masks STEM gradient: Math +0.97 > Science +0.84 >> CS_Eng ≈0). Mechanistic complement to family-level profiling — contamination heterogeneity operates at multiple granularities.\\\\n3. **Signal failure characterization**: Min-K++ directional reversal (Cohen's d = -1.2 to -2.7) — paper's most citation-worthy cautionary finding. Honest reporting that RRF = S1-only in practice.\\\\n4. **Fisher Information identifiability analysis**: structural vs practical thresholds with domain-method mismatch insight.\\\\n\\\\n### Supporting\\\\n5. ContamCal framework: two-stage pipeline (S1 provenance → contamination-augmented IRT with per-benchmark γ_k). Conditional calibration with gating criterion. ME model as ablation\\\\n6. Dual-track validation + 7 baselines + 6 metrics (incl. SBC). Controlled SFT injection across 5 families\\\\n\\\\n## Story Spine\\\\n- **Problem**: Benchmark scores are increasingly unreliable due to training data contamination. Rephrased test items inflate MMLU accuracy by 8-15 points while evading n-gram decontamination. RL post-training may further complicate detection (under investigation, exp-009). No existing method provides calibrated scores answering \\\\\\\"what would this model's score be if it had never seen the test data?\\\\\\\"\\\\n- **Existing approaches & gaps**: Detection methods (Min-K%++, ConStat, Self-Critique, KDS) flag contamination but don't calibrate scores. IRT methods (PSN-IRT, Growing Pains, ATLAS, Lalor et al. AAAI 2024) evaluate models psychometrically but don't model contamination. DCR provides adjusted accuracy but lacks uncertainty bounds and RL handling. HiBayES provides Bayesian uncertainty but ignores contamination. Emperor's New Clothes (ICML 2025) demonstrates that all 20 mitigation strategies fail — motivating post-hoc calibration. Dynamic benchmarks (LiveBench) offer an alternative but require continuous curation.\\\\n- **Our framing (D149 pivot)**: ContamC\\\\n\\\\n... [截断: 省略 26326 字符，传 max_chars=0 获取完整内容]\\\", \\\"total_chars\\\": 38326, \\\"truncated\\\": true}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/paper_framing.md\", \"content\": \"# Paper Framing — contamcal-irt-calibration\\n\\n## Target Venue\\n- **Primary: EMNLP 2026 ARR May 25** (D006: reinstated per user directive, 12 days)\\n- Fallback: AAAI 2027 (Jul-Aug 2026) / ICLR 2027 (Sep 2026)\\n- Track: Machine Learning for NLP / Resources and Evaluation\\n- Aligns with EMNLP 2026 special theme \\\"New Missions for NLP Research\\\" (explicitly invites contamination/data governance work)\\n\\n## Core Insight (D149: dose-response profiling + baseline-dependent direction, building on D039/D108/D115)\\n\\nBenchmark contamination does not have a single effect — controlled SFT injection across 5 independent model families reveals qualitatively different dose-response profiles depending on model baseline capability. Through injection (LoRA r=16, 5 dosage levels d000–d100) on Qwen2.5-7B, Qwen2.5-14B, Phi-4 14.7B, Gemma-2 9B, OLMo-2 7B, we observe:\\n\\n**4 dose-response patterns (D149→D183→D184, MMLU, cross-seed confirmed)**:\\n| Pattern | Family | Baseline | s42 Δ(d100) | s123 Δ(d100) | Cross-seed |\\n|---------|--------|----------|-------------|--------------|------------|\\n| Immune | Phi-4 14.7B | 76.44% | -0.17pp | +1.83pp | ✅ n=3: s0 +0.52pp, mean +0.73pp, BCa CI [-0.17, +1.39] 含零 |\\n| Collapse | Qwen-14B | 69.44% | -9.37pp (U-shape) | -12.74pp (monotonic) | ✅ 方向一致，形状不同 |\\n| V-recovery | Qwen-7B | 66.11% | -1.78pp (V-dip) | ~0pp (V-full) | ✅ 形状+方向一致 |\\n| Benefit | Gemma-2 9B | 61.86% | +3.76pp | +1.49pp | ✅ 方向一致 |\\n| Benefit† | OLMo-2 7B | 53.79% | +3.21pp | -0.55pp | ⚠️ seed-sensitive |\\n\\n⚠️ D184: \\\"U-collapse\\\" 重命名为 \\\"Collapse\\\"——s42 U-shape (d050→d100 回升 +0.6pp) 在 s123 不复现 (d050→d100 继续下沉 -5.1pp)。跨种子稳定的是方向(harm)不是形状(U)。V-recovery 保留 shape-based name 因为它是唯一跨种子形状稳定的 pattern。论文报告 Qwen-14B 跨种子区间 [−12.74, −9.0pp]。\\n\\n⚠️ **Bootstrap n=2 findings (D186)**: 算法形状分类 2/5 家族一致（Collapse ✅, V-recovery ✅），方向分类 4/5 一致（+Benefit ✅, +Immune ✅）。n=2 t-distribution CI 极宽（df=1, 所有 CI 跨零），统计效力有限——s0 升级到 n=3 BCa 后会显著收窄。\\n- **Phi-4**: 算法 \\\"Incomplete†\\\"（s42 Immune vs s123 Benefit-sat），但方向层面两个种子都 <2pp → Immune as practical label，等 s0\\n- **Gemma-2**: 算法 \\\"V-recovery†\\\"（s123 d025 -2.82pp dip 触发 V-dip 检测），但 d100 仍为正 (+1.49pp) → 方向稳定 Benefit，形状变异\\n- **OLMo-2**: 算法 \\\"Benefit-sat†\\\"，n=3 CI [-0.55, +2.60]，方向 2/3 正向但 s123 负\\n论文策略：报方向 taxonomy (Immune/Collapse/V-recovery/Benefit) + n=2 bootstrap CI table 作为 conservative bound + 明确写 \\\"shape classification requires ≥3 seeds; direction is more reproducible\\\"。n=3 数据是论文提交前的关键升级。\\n\\n**Vulnerability gradient (D181, replaces sharp threshold)**: 效应方向不由单一 sharp threshold 决定，而是呈 gradient 分布。Vulnerability（对 contamination 最敏感，表现为 harm）集中在 ~65-70% baseline band（Qwen-7B 66.1%, Qwen-14B 69.4%）。极端 baseline 表现为有限敏感性——低端（OLMo-2 53.8%）benefit 但 magnitude seed-dependent，高端（Phi-4 76.4%）immune。**不可说 \\\"sharp cutoff\\\" 或 \\\"universal threshold\\\"，用 \\\"vulnerability gradient\\\" 和 \\\"observed in our 5-family sample\\\"。**\\n\\n**Within-family scale finding (Qwen only)**: Within the Qwen family, the 14B model is 3× more fragile than the 7B (-10pp vs -3pp). However, Phi-4 (14.7B) is immune — so this is NOT a general \\\"bigger = more fragile\\\" claim. 正确 framing: \\\"baseline ability, not parameter count alone, determines contamination vulnerability.\\\"\\n\\n**ARC cross-benchmark results (D190, s42 + s123)**:\\n- s42 ARC: OLMo-2 +3.92pp, Qwen-7B -3.84pp, Qwen-14B -3.41pp, Phi-4 ±0.6pp. Gemma-2 ARC excluded (16pp oscillation artifact).\\n- s123 ARC: Qwen-14B -3.15pp, Phi-4 +0.86pp, Qwen-7B -2.39pp, OLMo-2 +2.90pp.\\n- **Cross-benchmark structure (D190→D191 corrected)**: 跨 benchmark 对比必须用 MMLU 多种子均值而非单 seed。修正后 3/4 方向一致：Qwen-14B 双降 ✅, Phi-4 双 Immune ✅, OLMo-2 双正 ✅ (MMLU mean +1.35pp, ARC +2.90pp)。Qwen-7B V-recovery 形状两个 benchmark 都有但恢复幅度 benchmark-specific (MMLU ≈0pp full recovery, ARC -2.39pp partial)。⚠️ D190 原始报告的 OLMo-2 \\\"方向反转\\\"是使用单 seed s123 (-0.55pp) 的伪影——修正为用 bootstrap 均值后双正。\\n- **论文 framing**: \\\"Cross-benchmark direction is consistent for 3/4 families; only V-recovery shows benchmark-specific modulation in recovery completeness.\\\" 不说 \\\"universal consistency\\\"，但也不需要 D190 的\\\"两层结构\\\"——3/4 一致已足够强。\\n- **方法论教训**: 跨 benchmark 对比使用单 seed 会产生 high-variance 家族的虚假方向反转。论文表格使用 bootstrap 均值。\\n\\nThe primary contribution is the empirical characterization framework — showing that \\\"contamination = inflation\\\" is a gross oversimplification and that model-specific dose-response profiling is necessary for reliable benchmark interpretation. IRT with per-benchmark γ_k provides the statistical machinery for this characterization. Grounded in educational measurement's item compromise IRT (Eckerly 2017, Sinharay 2017) and explanatory IRT (De Boeck & Wilson 2004).\\n\\n## Core Claims (4 条 — D149 reorder: characterization as primary, D152 Reviewer calibrated)\\n\\n1. **Characterization Claim (PRIMARY — D149 dose-response profiling)**: Contamination does not uniformly inflate scores — it produces qualitatively different dose-response profiles across model families, with effect direction (benefit vs harm) correlating with baseline ability. Key evidence:\\n   - **5 families × 5 dosages × 2 benchmarks** (MMLU + ARC) with controlled SFT injection at identical LoRA config\\n   - **Baseline-dependent direction**: In our 5-family sample, models below ~62-66% MMLU benefited; above were harmed or immune\\n   - **Effect magnitude heterogeneity**: From -10pp (Qwen-14B) to +3.8pp (Gemma-2) — 14pp range across families at same dosage\\n   - **Within-family scale effect (Qwen)**: 14B 3× more fragile than 7B, suggesting baseline ability (not just scale) drives vulnerability\\n   - **Cross-benchmark consistency (D190→D191→D192)**: 5/5 families have ARC data. Using multi-seed means: **4/5 direction-consistent** (Qwen-14B Collapse ✅, Phi-4 Immune ✅, Gemma-2 Benefit ✅, OLMo-2 Benefit ✅). Qwen-7B V-recovery is MMLU-specific — ARC shows persistent -2.65pp (mild Collapse), V-dip shape present but no recovery. Gemma-2 s42 ARC oscillation artifact is seed-specific (s123 clean +2.73pp). ⚠️ 跨 benchmark 表必须用 bootstrap 均值非单 seed。\\n   ⚠️ **Claim strength gating (D181 updated)**: Cross-seed data (Reviewer 修正): Qwen-7B V-recovery 2/2 seeds 一致 ✅; Gemma-2 Benefit 方向一致 (s42 +3.76pp, s123 +1.49pp) 但形状变异; OLMo-2 方向不稳定 (s42 +3.21pp, s123 -0.55pp, s0 +1.61pp). 4-pattern taxonomy (D184): Immune / Collapse / V-recovery / Benefit, 等 Qwen-14B s123 确认。论文策略：(a) 报 bootstrap CI 而非单点 Δ, (b) 加 seed-sensitivity discussion section, (c) 弱化 \\\"5 distinct patterns\\\" 语言, (d) OLMo-2 caveat about cross-seed instability。Seed-sensitivity 本身作为 methodological contribution: warns community that single-seed contamination studies are unreliable。\\n   **Domain-level heterogeneity (≤3B Qwen IRT analysis, D108/D115, mechanistic complement)**: Within MMLU, stratification by cognitive domain reveals Simpson's paradox: aggregate γ≈0 masks STEM gradient (Math γ=+0.97, Science γ=+0.84, CS_Eng γ≈0). Non-STEM domains show model misfit (PPP≈1.0). 注意：domain-level 分析在 ≤3B Qwen 上进行，与 7B-14.7B 5-family profiling 是不同 scale。7B-14.7B domain-level 分析列为 future work。\\n   **Paper claim scope**: 5 profiles based on 5 families × 5 dosages (seed=42; triple-seed in progress). Domain-level from ≤3B Qwen. Bounded by: SFT-route only, ≤14.7B, AUGMENT mode, 2 MCQ benchmarks.\\n\\n2. **Signal Failure Claim (CO-PRIMARY, headline finding per D039 dream 三档一致)**: Min-K++ exhibits directional reversal at small model scales (Cohen's d = -1.2 to -2.7 at 0.5B d100) — actively misleading, not merely ineffective. S1 embedding similarity is the only reliable signal (AUC>0.95). Multi-signal RRF degrades to S1-only in practice — paper is transparent about this (D039: all 3 dream tiers require honesty here). Training-free RRF remains the principled aggregation design (meta-circularity argument). Must distinguish item-level detection AUC from model-level Cohen's d.\\n   **C2 contingency**: \\\"Scale-dependent\\\" unverified beyond 0.5B. If 1.5B/3B S2/S4 remain ineffective → downgrade to \\\"method-specific signal effectiveness.\\\" Min-K++ reversal remains novel regardless.\\n\\n3. **Identifiability Claim**: Fisher Information analysis + simulation sweep (20 conditions, 200 runs). Recovery succeeds down to AUC=0.55 (lowest tested) at N≥50; the lower bound remains open. LLM evaluation inherently operates below N≥50 (typically N=8-30), creating a structural domain-method mismatch — this is the real \\\"impossibility,\\\" not merely \\\"IRT needs more data.\\\" CI width ∝ N^{-0.48} (simulation). Coverage collapse at N<30 confirmed empirically (D036). D039 dream worst-tier caution: frame as domain mismatch insight, not as surprising impossibility.\\n\\n4. **Conditional Calibration Claim (DEMOTED from old Claim 1 per D039)**: IRT ability estimation provides calibration value (GSM8K: calMAE=0.006 vs raw=0.169, ΔMAE=0.163); the γ parameter provides diagnostic value by revealing domain-differential contamination effects. These are distinct contributions: calibration improvement comes from the IRT framework itself (ability estimation decontaminates via the θ pathway), while γ characterizes where and how contamination manifests. When IRT model complexity matches benchmark structure (2PL for open-ended, 4PL for MCQ) AND signal quality sufficient (validated down to AUC=0.55 at J≥50), calibration produces usable point estimates. Coverage remains below nominal (20-69% at 95%) — present calibrated CIs as directional indicators, not precise credible intervals. Calibration gating criterion: PPP ∈ [0.1, 0.9] AND calibrated MAE < raw MAE. Note: vanilla 2PL ≈ 2PL+γ in MAE across all three benchmarks — γ does not improve calibration accuracy but provides the diagnostic decomposition that is Claim 1's core contribution.\\n\\n## Contributions (Hierarchical — D149/D152 calibrated)\\n\\n### Core\\n1. **Dose-response profiling across 5 model families**: Contamination effects range from -10pp to +3.8pp MMLU depending on model family, with effect direction correlating with baseline ability. No prior work has systematically profiled contamination dose-response across multiple independent families. *(Upgrades to \\\"taxonomy of N discrete patterns\\\" if triple-seed confirms profile stability; conservative framing: 3 profiles — benefit/harm/immune.)*\\n2. **Domain-dependent contamination characterization** via IRT γ_k (≤3B Qwen): Simpson's paradox within MMLU (aggregate γ≈0 masks STEM gradient: Math +0.97 > Science +0.84 >> CS_Eng ≈0). Mechanistic complement to family-level profiling — contamination heterogeneity operates at multiple granularities.\\n3. **Signal failure characterization**: Min-K++ directional reversal (Cohen's d = -1.2 to -2.7) — paper's most citation-worthy cautionary finding. Honest reporting that RRF = S1-only in practice.\\n4. **Fisher Information identifiability analysis**: structural vs practical thresholds with domain-method mismatch insight.\\n\\n### Supporting\\n5. ContamCal framework: two-stage pipeline (S1 provenance → contamination-augmented IRT with per-benchmark γ_k). Conditional calibration with gating criterion. ME model as ablation\\n6. Dual-track validation + 7 baselines + 6 metrics (incl. SBC). Controlled SFT injection across 5 families\\n\\n## Story Spine\\n- **Problem**: Benchmark scores are increasingly unreliable due to training data contamination. Rephrased test items inflate MMLU accuracy by 8-15 points while evading n-gram decontamination. RL post-training may further complicate detection (under investigation, exp-009). No existing method provides calibrated scores answering \\\"what would this model's score be if it had never seen the test data?\\\"\\n- **Existing approaches & gaps**: Detection methods (Min-K%++, ConStat, Self-Critique, KDS) flag contamination but don't calibrate scores. IRT methods (PSN-IRT, Growing Pains, ATLAS, Lalor et al. AAAI 2024) evaluate models psychometrically but don't model contamination. DCR provides adjusted accuracy but lacks uncertainty bounds and RL handling. HiBayES provides Bayesian uncertainty but ignores contamination. Emperor's New Clothes (ICML 2025) demonstrates that all 20 mitigation strategies fail — motivating post-hoc calibration. Dynamic benchmarks (LiveBench) offer an alternative but require continuous curation.\\n- **Our framing (D149 pivot)**: ContamC\\n\\n... [截断: 省略 26326 字符，传 max_chars=0 获取完整内容]\", \"total_chars\": 38326, \"truncated\": true}, \"error\": null, \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "72929b4a-1d89-4fa1-b79e-382390c8f870",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "a95a1f6e-644c-4d12-abb6-01351d2cbf40",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-21T11:06:57.568Z_

<details><summary>↩ Tool result · `toolu_01MdgMdphYVUVe57jUjMtqH4`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/ROADMAP.md\", \"content\": \"# contamcal-irt-calibration — Research Dashboard\\n\\n> 最后更新: 2026-05-21 09:02 UTC | 更新原因: Action matrix 大部分完成: W1-W2-W4-W5-W6-W7 done, W9 100% stable, C1-C3 全完成, LLaMA-3 改 Base 下载中\\n\\n> 目标: EMNLP 2026 ARR May 25 | **D+3, 剩余 3 天**\\n\\n## 核心方向\\nSFT-route benchmark contamination 产生 family-dependent dose-response profiles。**4-pattern taxonomy**: Immune / Collapse / V-recovery / Benefit。详见 paper_framing.md。\\n\\n## 当前状态\\n- **Round 8 审稿**: 3.0 (Findings) → 冲 3.5+\\n- **Paper 修改**: Batch 2 + DiD power + RRF ablation appendix 全部完成。W9 heatmap 写入中\\n- **实验**: LLaMA-3.1-8B Base 下载中 + GSM8K appendix evals 运行中\\n- **计算任务**: 5/5 全部完成 ✅\\n\\n## Round 8 Action Matrix\\n\\n### Critical\\n| ID | 问题 | 状态 |\\n|----|------|------|\\n| W1 | n=3 claims 弱化 | ✅ Paper done |\\n| W2 | DiD power + claim 弱化 | ✅ MDES computed + paper done |\\n| W3 | N=4 泛化性 | 🟡 LLaMA-3 Base 下载中 (d000+d100 先行) |\\n| W4 | Han et al. 对比 | ✅ Paper done |\\n\\n### Should-Fix\\n| ID | 问题 | 状态 |\\n|----|------|------|\\n| W5 | 页数超限 | ✅ ≤8 pages |\\n| W6 | 术语统一 | ✅ Paper done |\\n| W7 | RRF ablation | ✅ D203: item-level valid, appendix written |\\n| W8 | Skewed exposure sim | ⏳ 最低优先级 |\\n| W9 | τ×σ heatmap | ✅ 100% stable → Paper Agent 写入中 |\\n\\n### Minor + Refs\\n✅ M1-M6 全部修复 + 3 refs verified\\n\\n### 计算任务\\n| 任务 | 状态 |\\n|------|------|\\n| DiD MDES (d025) | ✅ MMLU 1.2-2.0pp / ARC 2.3-5.6pp |\\n| DiD d050 补充 | ✅ 改善仅 7%, item variance 是约束 |\\n| C1+C2 RRF ablation | ✅ S4>S1>S2, model-level ρ≈0 |\\n| C3 τ×σ heatmap | ✅ 30/30 → 100% stable |\\n| Bootstrap Qwen-7B | ✅ CI=[-1.82,-0.35] 验证链闭合 |\\n\\n## LLaMA-3 验证 (W3)\\n- 模型: meta-llama/Llama-3.1-8B (**Base**, 非 Instruct — M044 教训)\\n- 策略: d000+d100 先行快速验证 → 时间允许补 d005/d025/d050\\n- 下载: ModelScope 加速方案执行中\\n- GPU: westd 待空闲卡\\n\\n## GSM8K Cross-Benchmark Transfer (Appendix)\\n| Family | d000 | d100 | Δ | 状态 |\\n|--------|------|------|---|------|\\n| Qwen-14B | 74.98 | 82.41 | +7.43 | ✅ 完整 5-dose |\\n| Qwen-7B | 73.31 | 81.20 | +7.89 | ✅ 完整 5-dose |\\n| Phi-4 | 84.46 | running | — | 🟡 |\\n| OLMo-2 | running | — | — | 🟡 |\\n| Gemma-2 | 17.82⚠️ | — | — | CoT 崩塌 |\\n\\n## 时间线\\n- **May 21 (今天)**: ✅ Paper Batch 2 + 计算任务完成; 🟡 LLaMA-3 下载 + GSM8K evals\\n- **May 22**: LLaMA-3 SFT + eval; GSM8K 完成; Paper Agent 合入最终数据\\n- **May 23**: 全文一致性检查 + 重新提交审稿 (continue mode)\\n- **May 24-25**: 终稿提交 (ARR DDL)\\n\\n## GPU 预算\\n- westd: 4× RTX PRO 6000 Blackwell (98GB) — 4/4 active\\n- cqa1: 1× RTX 4090 D (24GB) — 空闲\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D206 | 2026-05-21 | GSM8K appendix 全部统一 s0 数据（37775版本）+ 强 caveat，不做跨家族 | gsm8k_appendix |\\n| D205 | 2026-05-21 | GSM8K appendix 保留现有数据不重跑——s0 用 37775 版 evaluate.py | eval_olmo2_gsm8k_d000_s0, sft_llama3_d000_s0 |\\n| D204 | 2026-05-21 | OLMo-2 GSM8K s0 数据排除（evaluate.py 版本不一致），appendix 改 | eval_olmo2_gsm8k_d000_s0, eval_olmo2_gsm8k_d100_s0 |\\n| D203 | 2026-05-21 | W7 RRF 消融：model-level dosage correlation≈0, S2有害—— | rrf_signal_correlation, rrf_leave_one_out |\\n| D202 | 2026-05-21 | D202: Round 8 审稿 3.0 (Findings) — 识别 2 个系统性问题 + 构建 | round8_review |\\n| D201 | 2026-05-21 | D201: Qwen-7B n=3 数据确认成立 + CI 方法论风险识别——BCa bootstr | bootstrap_qwen7b_n3, eval_qwen7b_s42_cqa1_v2 |\\n| D200 | 2026-05-21 | 5/5 n=3 BCa bootstrap CI 全部完成，四种 dose-response pat | bootstrap_qwen14b_n3, eval_qwen7b_gsm8k_s0_cqa1 |\\n| D199 | 2026-05-21 | Cross-benchmark consistency 4/5→3/5: Gemma-2 bench | bootstrap_gemma2_n3, eval_gemma2_d100_arc_s0, eval_gemma2_d100_arc_s123 |\\n| D198 | 2026-05-21 | D198: Gemma-2 n=3 MMLU Benefit 确认（mean +2.38pp, 3/ | retrain_gemma2_d100_s0, sft_gemma2_s0_sweep |\\n| D197 | 2026-05-21 | D197: Qwen-14B position bias 确认为 Qwen 家族共有特征——更新 L | sft_qwen14b_s0_sweep |\\n\\n\", \"total_chars\": 3537, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "94ae541d-4654-4bec-b8e5-95d42eb535d9",
  "isSidechain": false,
  "promptId": "ff132cc0-9ef7-4a70-8848-7ec535292349",
  "type": "user",
  "uuid": "41d10ede-9365-418b-a930-1cbc51302d65",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/ROADMAP.md\\\", \\\"content\\\": \\\"# contamcal-irt-calibration — Research Dashboard\\\\n\\\\n> 最后更新: 2026-05-21 09:02 UTC | 更新原因: Action matrix 大部分完成: W1-W2-W4-W5-W6-W7 done, W9 100% stable, C1-C3 全完成, LLaMA-3 改 Base 下载中\\\\n\\\\n> 目标: EMNLP 2026 ARR May 25 | **D+3, 剩余 3 天**\\\\n\\\\n## 核心方向\\\\nSFT-route benchmark contamination 产生 family-dependent dose-response profiles。**4-pattern taxonomy**: Immune / Collapse / V-recovery / Benefit。详见 paper_framing.md。\\\\n\\\\n## 当前状态\\\\n- **Round 8 审稿**: 3.0 (Findings) → 冲 3.5+\\\\n- **Paper 修改**: Batch 2 + DiD power + RRF ablation appendix 全部完成。W9 heatmap 写入中\\\\n- **实验**: LLaMA-3.1-8B Base 下载中 + GSM8K appendix evals 运行中\\\\n- **计算任务**: 5/5 全部完成 ✅\\\\n\\\\n## Round 8 Action Matrix\\\\n\\\\n### Critical\\\\n| ID | 问题 | 状态 |\\\\n|----|------|------|\\\\n| W1 | n=3 claims 弱化 | ✅ Paper done |\\\\n| W2 | DiD power + claim 弱化 | ✅ MDES computed + paper done |\\\\n| W3 | N=4 泛化性 | 🟡 LLaMA-3 Base 下载中 (d000+d100 先行) |\\\\n| W4 | Han et al. 对比 | ✅ Paper done |\\\\n\\\\n### Should-Fix\\\\n| ID | 问题 | 状态 |\\\\n|----|------|------|\\\\n| W5 | 页数超限 | ✅ ≤8 pages |\\\\n| W6 | 术语统一 | ✅ Paper done |\\\\n| W7 | RRF ablation | ✅ D203: item-level valid, appendix written |\\\\n| W8 | Skewed exposure sim | ⏳ 最低优先级 |\\\\n| W9 | τ×σ heatmap | ✅ 100% stable → Paper Agent 写入中 |\\\\n\\\\n### Minor + Refs\\\\n✅ M1-M6 全部修复 + 3 refs verified\\\\n\\\\n### 计算任务\\\\n| 任务 | 状态 |\\\\n|------|------|\\\\n| DiD MDES (d025) | ✅ MMLU 1.2-2.0pp / ARC 2.3-5.6pp |\\\\n| DiD d050 补充 | ✅ 改善仅 7%, item variance 是约束 |\\\\n| C1+C2 RRF ablation | ✅ S4>S1>S2, model-level ρ≈0 |\\\\n| C3 τ×σ heatmap | ✅ 30/30 → 100% stable |\\\\n| Bootstrap Qwen-7B | ✅ CI=[-1.82,-0.35] 验证链闭合 |\\\\n\\\\n## LLaMA-3 验证 (W3)\\\\n- 模型: meta-llama/Llama-3.1-8B (**Base**, 非 Instruct — M044 教训)\\\\n- 策略: d000+d100 先行快速验证 → 时间允许补 d005/d025/d050\\\\n- 下载: ModelScope 加速方案执行中\\\\n- GPU: westd 待空闲卡\\\\n\\\\n## GSM8K Cross-Benchmark Transfer (Appendix)\\\\n| Family | d000 | d100 | Δ | 状态 |\\\\n|--------|------|------|---|------|\\\\n| Qwen-14B | 74.98 | 82.41 | +7.43 | ✅ 完整 5-dose |\\\\n| Qwen-7B | 73.31 | 81.20 | +7.89 | ✅ 完整 5-dose |\\\\n| Phi-4 | 84.46 | running | — | 🟡 |\\\\n| OLMo-2 | running | — | — | 🟡 |\\\\n| Gemma-2 | 17.82⚠️ | — | — | CoT 崩塌 |\\\\n\\\\n## 时间线\\\\n- **May 21 (今天)**: ✅ Paper Batch 2 + 计算任务完成; 🟡 LLaMA-3 下载 + GSM8K evals\\\\n- **May 22**: LLaMA-3 SFT + eval; GSM8K 完成; Paper Agent 合入最终数据\\\\n- **May 23**: 全文一致性检查 + 重新提交审稿 (continue mode)\\\\n- **May 24-25**: 终稿提交 (ARR DDL)\\\\n\\\\n## GPU 预算\\\\n- westd: 4× RTX PRO 6000 Blackwell (98GB) — 4/4 active\\\\n- cqa1: 1× RTX 4090 D (24GB) — 空闲\\\\n\\\\n## 关键决策日志\\\\n\\\\n| ID | 日期 | 摘要 | 关联实验 |\\\\n|----|------|------|----------|\\\\n| D206 | 2026-05-21 | GSM8K appendix 全部统一 s0 数据（37775版本）+ 强 caveat，不做跨家族 | gsm8k_appendix |\\\\n| D205 | 2026-05-21 | GSM8K appendix 保留现有数据不重跑——s0 用 37775 版 evaluate.py | eval_olmo2_gsm8k_d000_s0, sft_llama3_d000_s0 |\\\\n| D204 | 2026-05-21 | OLMo-2 GSM8K s0 数据排除（evaluate.py 版本不一致），appendix 改 | eval_olmo2_gsm8k_d000_s0, eval_olmo2_gsm8k_d100_s0 |\\\\n| D203 | 2026-05-21 | W7 RRF 消融：model-level dosage correlation≈0, S2有害—— | rrf_signal_correlation, rrf_leave_one_out |\\\\n| D202 | 2026-05-21 | D202: Round 8 审稿 3.0 (Findings) — 识别 2 个系统性问题 + 构建 | round8_review |\\\\n| D201 | 2026-05-21 | D201: Qwen-7B n=3 数据确认成立 + CI 方法论风险识别——BCa bootstr | bootstrap_qwen7b_n3, eval_qwen7b_s42_cqa1_v2 |\\\\n| D200 | 2026-05-21 | 5/5 n=3 BCa bootstrap CI 全部完成，四种 dose-response pat | bootstrap_qwen14b_n3, eval_qwen7b_gsm8k_s0_cqa1 |\\\\n| D199 | 2026-05-21 | Cross-benchmark consistency 4/5→3/5: Gemma-2 bench | bootstrap_gemma2_n3, eval_gemma2_d100_arc_s0, eval_gemma2_d100_arc_s123 |\\\\n| D198 | 2026-05-21 | D198: Gemma-2 n=3 MMLU Benefit 确认（mean +2.38pp, 3/ | retrain_gemma2_d100_s0, sft_gemma2_s0_sweep |\\\\n| D197 | 2026-05-21 | D197: Qwen-14B position bias 确认为 Qwen 家族共有特征——更新 L | sft_qwen14b_s0_sweep |\\\\n\\\\n\\\", \\\"total_chars\\\": 3537, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/ROADMAP.md\", \"content\": \"# contamcal-irt-calibration — Research Dashboard\\n\\n> 最后更新: 2026-05-21 09:02 UTC | 更新原因: Action matrix 大部分完成: W1-W2-W4-W5-W6-W7 done, W9 100% stable, C1-C3 全完成, LLaMA-3 改 Base 下载中\\n\\n> 目标: EMNLP 2026 ARR May 25 | **D+3, 剩余 3 天**\\n\\n## 核心方向\\nSFT-route benchmark contamination 产生 family-dependent dose-response profiles。**4-pattern taxonomy**: Immune / Collapse / V-recovery / Benefit。详见 paper_framing.md。\\n\\n## 当前状态\\n- **Round 8 审稿**: 3.0 (Findings) → 冲 3.5+\\n- **Paper 修改**: Batch 2 + DiD power + RRF ablation appendix 全部完成。W9 heatmap 写入中\\n- **实验**: LLaMA-3.1-8B Base 下载中 + GSM8K appendix evals 运行中\\n- **计算任务**: 5/5 全部完成 ✅\\n\\n## Round 8 Action Matrix\\n\\n### Critical\\n| ID | 问题 | 状态 |\\n|----|------|------|\\n| W1 | n=3 claims 弱化 | ✅ Paper done |\\n| W2 | DiD power + claim 弱化 | ✅ MDES computed + paper done |\\n| W3 | N=4 泛化性 | 🟡 LLaMA-3 Base 下载中 (d000+d100 先行) |\\n| W4 | Han et al. 对比 | ✅ Paper done |\\n\\n### Should-Fix\\n| ID | 问题 | 状态 |\\n|----|------|------|\\n| W5 | 页数超限 | ✅ ≤8 pages |\\n| W6 | 术语统一 | ✅ Paper done |\\n| W7 | RRF ablation | ✅ D203: item-level valid, appendix written |\\n| W8 | Skewed exposure sim | ⏳ 最低优先级 |\\n| W9 | τ×σ heatmap | ✅ 100% stable → Paper Agent 写入中 |\\n\\n### Minor + Refs\\n✅ M1-M6 全部修复 + 3 refs verified\\n\\n### 计算任务\\n| 任务 | 状态 |\\n|------|------|\\n| DiD MDES (d025) | ✅ MMLU 1.2-2.0pp / ARC 2.3-5.6pp |\\n| DiD d050 补充 | ✅ 改善仅 7%, item variance 是约束 |\\n| C1+C2 RRF ablation | ✅ S4>S1>S2, model-level ρ≈0 |\\n| C3 τ×σ heatmap | ✅ 30/30 → 100% stable |\\n| Bootstrap Qwen-7B | ✅ CI=[-1.82,-0.35] 验证链闭合 |\\n\\n## LLaMA-3 验证 (W3)\\n- 模型: meta-llama/Llama-3.1-8B (**Base**, 非 Instruct — M044 教训)\\n- 策略: d000+d100 先行快速验证 → 时间允许补 d005/d025/d050\\n- 下载: ModelScope 加速方案执行中\\n- GPU: westd 待空闲卡\\n\\n## GSM8K Cross-Benchmark Transfer (Appendix)\\n| Family | d000 | d100 | Δ | 状态 |\\n|--------|------|------|---|------|\\n| Qwen-14B | 74.98 | 82.41 | +7.43 | ✅ 完整 5-dose |\\n| Qwen-7B | 73.31 | 81.20 | +7.89 | ✅ 完整 5-dose |\\n| Phi-4 | 84.46 | running | — | 🟡 |\\n| OLMo-2 | running | — | — | 🟡 |\\n| Gemma-2 | 17.82⚠️ | — | — | CoT 崩塌 |\\n\\n## 时间线\\n- **May 21 (今天)**: ✅ Paper Batch 2 + 计算任务完成; 🟡 LLaMA-3 下载 + GSM8K evals\\n- **May 22**: LLaMA-3 SFT + eval; GSM8K 完成; Paper Agent 合入最终数据\\n- **May 23**: 全文一致性检查 + 重新提交审稿 (continue mode)\\n- **May 24-25**: 终稿提交 (ARR DDL)\\n\\n## GPU 预算\\n- westd: 4× RTX PRO 6000 Blackwell (98GB) — 4/4 active\\n- cqa1: 1× RTX 4090 D (24GB) — 空闲\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D206 | 2026-05-21 | GSM8K appendix 全部统一 s0 数据（37775版本）+ 强 caveat，不做跨家族 | gsm8k_appendix |\\n| D205 | 2026-05-21 | GSM8K appendix 保留现有数据不重跑——s0 用 37775 版 evaluate.py | eval_olmo2_gsm8k_d000_s0, sft_llama3_d000_s0 |\\n| D204 | 2026-05-21 | OLMo-2 GSM8K s0 数据排除（evaluate.py 版本不一致），appendix 改 | eval_olmo2_gsm8k_d000_s0, eval_olmo2_gsm8k_d100_s0 |\\n| D203 | 2026-05-21 | W7 RRF 消融：model-level dosage correlation≈0, S2有害—— | rrf_signal_correlation, rrf_leave_one_out |\\n| D202 | 2026-05-21 | D202: Round 8 审稿 3.0 (Findings) — 识别 2 个系统性问题 + 构建 | round8_review |\\n| D201 | 2026-05-21 | D201: Qwen-7B n=3 数据确认成立 + CI 方法论风险识别——BCa bootstr | bootstrap_qwen7b_n3, eval_qwen7b_s42_cqa1_v2 |\\n| D200 | 2026-05-21 | 5/5 n=3 BCa bootstrap CI 全部完成，四种 dose-response pat | bootstrap_qwen14b_n3, eval_qwen7b_gsm8k_s0_cqa1 |\\n| D199 | 2026-05-21 | Cross-benchmark consistency 4/5→3/5: Gemma-2 bench | bootstrap_gemma2_n3, eval_gemma2_d100_arc_s0, eval_gemma2_d100_arc_s123 |\\n| D198 | 2026-05-21 | D198: Gemma-2 n=3 MMLU Benefit 确认（mean +2.38pp, 3/ | retrain_gemma2_d100_s0, sft_gemma2_s0_sweep |\\n| D197 | 2026-05-21 | D197: Qwen-14B position bias 确认为 Qwen 家族共有特征——更新 L | sft_qwen14b_s0_sweep |\\n\\n\", \"total_chars\": 3537, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "94ae541d-4654-4bec-b8e5-95d42eb535d9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "a95a1f6e-644c-4d12-abb6-01351d2cbf40",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 18_

```json
{
  "type": "last-prompt",
  "leafUuid": "41d10ede-9365-418b-a930-1cbc51302d65",
  "sessionId": "a95a1f6e-644c-4d12-abb6-01351d2cbf40"
}
```

---

### Runtime record

_source line 19_

```json
{
  "type": "ai-title",
  "aiTitle": "Verify GSM8K appendix data and prepare LLaMA-3 paper sections",
  "sessionId": "a95a1f6e-644c-4d12-abb6-01351d2cbf40"
}
```

---

### Assistant

_source line 20 · 2026-05-21T11:07:13.304Z_

<details><summary>Logged reasoning block</summary>

```text
The registry output was too large and was saved to a file. Let me use an agent to extract GSM8K-related experiments from it. I also need to check Phi-4 d100 GSM8K status.

From what I've already gathered:

**paper_framing.md** mentions:
- GSM8K is mentioned as a cross-benchmark transfer validation
- LLaMA-3 is for W3 (N=4 generalizability)
- Sections where LLaMA-3 results would go: primarily the characterization claim (Claim 1), which is about dose-response profiling across model families


- **ROADMAP.md** shows the GSM8K cross-benchmark transfer table status: Qwen-14B and Qwen-7B are complete with full 5-dose runs, Phi-4 has d000 done but d100 is still running, OLMo-2 is in progress though D204 was excluded due to an evaluate.py version issue, and Gemma-2 shows a concerning CoT collapse at 17.82

.

Now I'm checking on LLaMA-3 verification using the base 8B model—planning to run d000 and d100 first, then fill in the middle dosages if there's time. The model download is underway through ModelScope. I should pull the exact GSM8K data points from the registry to confirm Phi-4's d100 status and clarify which paper sections LLaMA-3 belongs in.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "41d10ede-9365-418b-a930-1cbc51302d65",
  "isSidechain": false,
  "requestId": "req_011CbFcADgrfwnFF6emyCeAf",
  "type": "assistant",
  "uuid": "f5182f3f-857a-4f8d-a282-b5677212a29e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "a95a1f6e-644c-4d12-abb6-01351d2cbf40",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P3yYEthrcXgDtezDPZtnBe",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8052,
      "cache_read_input_tokens": 26098,
      "output_tokens": 880,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8052,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 880,
          "cache_read_input_tokens": 26098,
          "cache_creation_input_tokens": 8052,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8052
          },
          "type": "message"
        }
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

_source line 21 · 2026-05-21T11:07:13.304Z_

Registry output too large — let me extract the GSM8K-relevant entries.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f5182f3f-857a-4f8d-a282-b5677212a29e",
  "isSidechain": false,
  "requestId": "req_011CbFcADgrfwnFF6emyCeAf",
  "type": "assistant",
  "uuid": "779624b2-7bb3-48fb-be13-8a2bf312d557",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "a95a1f6e-644c-4d12-abb6-01351d2cbf40",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P3yYEthrcXgDtezDPZtnBe",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8052,
      "cache_read_input_tokens": 26098,
      "output_tokens": 880,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8052,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 880,
          "cache_read_input_tokens": 26098,
          "cache_creation_input_tokens": 8052,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8052
          },
          "type": "message"
        }
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

_source line 22 · 2026-05-21T11:07:20.596Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01SQgaHTDmFmzdjKDyCtq6cr`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/a95a1f6e-644c-4d12-abb6-01351d2cbf40/tool-results/mcp-agent-ml-research-read_registry-1779361617399.txt | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\nexperiments = json.loads(data['result'])\n# Filter for gsm8k-related experiments\ngsm = [e for e in experiments if 'gsm8k' in json.dumps(e).lower()]\nfor e in gsm:\n    print(f\\\"ID: {e.get('id','?')}  Status: {e.get('status','?')}\\\")\n    print(f\\\"  Conclusion: {e.get('conclusion','')[:200]}\\\")\n    if e.get('metrics'):\n        print(f\\\"  Metrics: {json.dumps(e['metrics'])[:300]}\\\")\n    if e.get('config'):\n        print(f\\\"  Config: {json.dumps(e['config'])[:300]}\\\")\n    print()\n\"",
  "description": "Extract GSM8K experiments from registry dump"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "779624b2-7bb3-48fb-be13-8a2bf312d557",
  "isSidechain": false,
  "requestId": "req_011CbFcADgrfwnFF6emyCeAf",
  "type": "assistant",
  "uuid": "f551132a-29f6-4812-82d9-9dc136d39f1d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "a95a1f6e-644c-4d12-abb6-01351d2cbf40",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P3yYEthrcXgDtezDPZtnBe",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8052,
      "cache_read_input_tokens": 26098,
      "output_tokens": 880,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8052,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 880,
          "cache_read_input_tokens": 26098,
          "cache_creation_input_tokens": 8052,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8052
          },
          "type": "message"
        }
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

_source line 23 · 2026-05-21T11:07:20.822Z_

<details><summary>↩ Tool result · `toolu_01SQgaHTDmFmzdjKDyCtq6cr`</summary>

```text
(Bash completed with no output)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f551132a-29f6-4812-82d9-9dc136d39f1d",
  "isSidechain": false,
  "promptId": "ff132cc0-9ef7-4a70-8848-7ec535292349",
  "type": "user",
  "uuid": "180a1670-c45e-472c-8465-c22495dcf0da",
  "toolUseResult": {
    "stdout": "",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "f551132a-29f6-4812-82d9-9dc136d39f1d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "a95a1f6e-644c-4d12-abb6-01351d2cbf40",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 24 · 2026-05-21T11:07:25.465Z_

<details><summary>Logged reasoning block</summary>

```text
No output — the structure might be different. Let me probe it.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "180a1670-c45e-472c-8465-c22495dcf0da",
  "isSidechain": false,
  "requestId": "req_011CbFcBw3JY9JxMsBK7RtfZ",
  "type": "assistant",
  "uuid": "f9493ec9-02a7-4fad-80df-2a198c0518f5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "a95a1f6e-644c-4d12-abb6-01351d2cbf40",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011aHhgwyNY5XCC2uAtAzBfC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 895,
      "cache_read_input_tokens": 34150,
      "output_tokens": 343,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 895,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 343,
          "cache_read_input_tokens": 34150,
          "cache_creation_input_tokens": 895,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 895
          },
          "type": "message"
        }
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

_source line 25 · 2026-05-21T11:07:28.303Z_

<details open><summary>🔧 Tool call — Bash · `toolu_019qtXX51q9u2QzW4CXkHp6B`</summary>

```json
{
  "command": "python3 -c \"\nimport json\nwith open('/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/a95a1f6e-644c-4d12-abb6-01351d2cbf40/tool-results/mcp-agent-ml-research-read_registry-1779361617399.txt') as f:\n    data = json.load(f)\nresult = data['result']\n# Check type\nif isinstance(result, str):\n    parsed = json.loads(result)\nelse:\n    parsed = result\nprint(type(parsed), len(parsed) if isinstance(parsed, list) else 'not list')\nif isinstance(parsed, list) and len(parsed) > 0:\n    print(json.dumps(parsed[0], indent=2)[:500])\nelif isinstance(parsed, dict):\n    print(list(parsed.keys())[:10])\n\"\n",
  "description": "Probe registry data structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f9493ec9-02a7-4fad-80df-2a198c0518f5",
  "isSidechain": false,
  "requestId": "req_011CbFcBw3JY9JxMsBK7RtfZ",
  "type": "assistant",
  "uuid": "77e9f9e1-22d4-4f35-94e8-9d781f587851",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "a95a1f6e-644c-4d12-abb6-01351d2cbf40",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011aHhgwyNY5XCC2uAtAzBfC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 895,
      "cache_read_input_tokens": 34150,
      "output_tokens": 343,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 895,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 343,
          "cache_read_input_tokens": 34150,
          "cache_creation_input_tokens": 895,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 895
          },
          "type": "message"
        }
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

_source line 26 · 2026-05-21T11:07:28.404Z_

<details><summary>↩ Tool result · `toolu_019qtXX51q9u2QzW4CXkHp6B`</summary>

```text
&lt;class 'dict'> not list
['success', 'data', 'error', 'metadata']
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "77e9f9e1-22d4-4f35-94e8-9d781f587851",
  "isSidechain": false,
  "promptId": "ff132cc0-9ef7-4a70-8848-7ec535292349",
  "type": "user",
  "uuid": "80f23c4a-903e-4036-93c6-bf30f58ea369",
  "toolUseResult": {
    "stdout": "&lt;class 'dict'> not list\n['success', 'data', 'error', 'metadata']",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "77e9f9e1-22d4-4f35-94e8-9d781f587851",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "a95a1f6e-644c-4d12-abb6-01351d2cbf40",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-21T11:07:35.273Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01CJqKCidKktG48bJs1FZfUD`</summary>

```json
{
  "command": "python3 -c \"\nimport json\nwith open('/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/a95a1f6e-644c-4d12-abb6-01351d2cbf40/tool-results/mcp-agent-ml-research-read_registry-1779361617399.txt') as f:\n    data = json.load(f)\nparsed = json.loads(data['result'])\nexperiments = parsed['data']\nprint(f'Total experiments: {len(experiments)}')\n# Filter for gsm8k\ngsm = [e for e in experiments if 'gsm8k' in json.dumps(e).lower()]\nprint(f'GSM8K-related: {len(gsm)}')\nfor e in gsm:\n    eid = e.get('id','?')\n    status = e.get('status','?')\n    conclusion = str(e.get('conclusion',''))[:200]\n    metrics = json.dumps(e.get('metrics',{}))[:300] if e.get('metrics') else 'none'\n    config = json.dumps(e.get('config',{}))[:300] if e.get('config') else 'none'\n    print(f'\\\\nID: {eid}  Status: {status}')\n    print(f'  Conclusion: {conclusion}')\n    print(f'  Metrics: {metrics}')\n    print(f'  Config: {config}')\n\"\n",
  "description": "Extract GSM8K experiments from registry"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "80f23c4a-903e-4036-93c6-bf30f58ea369",
  "isSidechain": false,
  "requestId": "req_011CbFcCVK1pzR7miATnFji8",
  "type": "assistant",
  "uuid": "94e8a75c-90d9-4e10-86ed-82d9ed70559a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "a95a1f6e-644c-4d12-abb6-01351d2cbf40",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BU4ZDbKscGeohTh1pPsw7L",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 379,
      "cache_read_input_tokens": 35045,
      "output_tokens": 457,
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
          "output_tokens": 457,
          "cache_read_input_tokens": 35045,
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

_source line 28 · 2026-05-21T11:07:35.387Z_

<details><summary>↩ Tool result · `toolu_01CJqKCidKktG48bJs1FZfUD`</summary>

```text
Total experiments: 4
GSM8K-related: 0
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "94e8a75c-90d9-4e10-86ed-82d9ed70559a",
  "isSidechain": false,
  "promptId": "ff132cc0-9ef7-4a70-8848-7ec535292349",
  "type": "user",
  "uuid": "c53cabee-623f-452e-82fe-b96ca11a4661",
  "toolUseResult": {
    "stdout": "Total experiments: 4\nGSM8K-related: 0",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "94e8a75c-90d9-4e10-86ed-82d9ed70559a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "a95a1f6e-644c-4d12-abb6-01351d2cbf40",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 29 · 2026-05-21T11:07:38.473Z_

<details><summary>Logged reasoning block</summary>

```text
Only 4 experiments with DONE status and none related to GSM8K. The filter was for DONE status. Let me try without the filter, or search with different criteria.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c53cabee-623f-452e-82fe-b96ca11a4661",
  "isSidechain": false,
  "requestId": "req_011CbFcD1BcnUm1AEJHt2rev",
  "type": "assistant",
  "uuid": "8215e107-b248-458a-ba5c-e128360ccdc1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "a95a1f6e-644c-4d12-abb6-01351d2cbf40",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XP1gmgvNqSb41NY5qMjohe",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 484,
      "cache_read_input_tokens": 35424,
      "output_tokens": 192,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 484,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 192,
          "cache_read_input_tokens": 35424,
          "cache_creation_input_tokens": 484,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 484
          },
          "type": "message"
        }
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

_source line 30 · 2026-05-21T11:07:39.433Z_

Only 4 DONE experiments returned, none GSM8K. Let me search without status filter.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8215e107-b248-458a-ba5c-e128360ccdc1",
  "isSidechain": false,
  "requestId": "req_011CbFcD1BcnUm1AEJHt2rev",
  "type": "assistant",
  "uuid": "b3162d30-72b1-4cd0-b3a2-1c77e9667edf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "a95a1f6e-644c-4d12-abb6-01351d2cbf40",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XP1gmgvNqSb41NY5qMjohe",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 484,
      "cache_read_input_tokens": 35424,
      "output_tokens": 192,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 484,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 192,
          "cache_read_input_tokens": 35424,
          "cache_creation_input_tokens": 484,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 484
          },
          "type": "message"
        }
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

_source line 31 · 2026-05-21T11:07:40.503Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_0118Md8pnxw1pZphJPvJ5xw5`</summary>

```json
{
  "project": "contamcal-irt-calibration",
  "limit": 0,
  "fields": [
    "id",
    "status",
    "conclusion",
    "metrics"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b3162d30-72b1-4cd0-b3a2-1c77e9667edf",
  "isSidechain": false,
  "requestId": "req_011CbFcD1BcnUm1AEJHt2rev",
  "type": "assistant",
  "uuid": "8ef60cf5-4df8-4ce0-b634-457bc5014096",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "a95a1f6e-644c-4d12-abb6-01351d2cbf40",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XP1gmgvNqSb41NY5qMjohe",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 484,
      "cache_read_input_tokens": 35424,
      "output_tokens": 192,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 484,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 192,
          "cache_read_input_tokens": 35424,
          "cache_creation_input_tokens": 484,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 484
          },
          "type": "message"
        }
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

_source line 32 · 2026-05-21T11:07:41.871Z_

<details><summary>↩ Tool result · `toolu_0118Md8pnxw1pZphJPvJ5xw5`</summary>

```text
Error: result (92,905 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/a95a1f6e-644c-4d12-abb6-01351d2cbf40/tool-results/mcp-agent-ml-research-read_registry-1779361661868.txt.
Format: JSON with schema: {result: string}
- For targeted queries (find a value, filter by field): use jq on the file directly.
- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/a95a1f6e-644c-4d12-abb6-01351d2cbf40/tool-results/mcp-agent-ml-research-read_registry-1779361661868.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.
- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/a95a1f6e-644c-4d12-abb6-01351d2cbf40/tool-results/mcp-agent-ml-research-read_registry-1779361661868.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim." A vague "summarize this" may lose detail.

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8ef60cf5-4df8-4ce0-b634-457bc5014096",
  "isSidechain": false,
  "promptId": "ff132cc0-9ef7-4a70-8848-7ec535292349",
  "type": "user",
  "uuid": "1a33dbc3-94f6-46a8-8f01-219c5d8b94b3",
  "toolUseResult": "Error: result (92,905 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/a95a1f6e-644c-4d12-abb6-01351d2cbf40/tool-results/mcp-agent-ml-research-read_registry-1779361661868.txt.\nFormat: JSON with schema: {result: string}\n- For targeted queries (find a value, filter by field): use jq on the file directly.\n- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/a95a1f6e-644c-4d12-abb6-01351d2cbf40/tool-results/mcp-agent-ml-research-read_registry-1779361661868.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.\n- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. \"/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/a95a1f6e-644c-4d12-abb6-01351d2cbf40/tool-results/mcp-agent-ml-research-read_registry-1779361661868.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim.\" A vague \"summarize this\" may lose detail.\n",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"sft_llama3_d100_s0\": {\"status\": \"RUNNING\"}, \"sft_llama3_d025_s0\": {\"status\": \"RUNNING\"}, \"sft_llama3_d000_s0\": {\"status\": \"RUNNING\"}, \"sft_llama3_8b_s0_validation\": {\"status\": \"PREPARING\"}, \"eval_phi4_gsm8k_d000_s0\": {\"status\": \"DONE\", \"metrics\": {\"gsm8k_accuracy\": 84.46, \"correct\": 1114, \"total\": 1319}, \"conclusion\": \"success\"}, \"eval_qwen14b_d100_gsm8k_s0\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"gsm8k_accuracy\": 82.41, \"correct\": 1087, \"total\": 1319}}, \"eval_qwen7b_s42_cqa1_v2\": {\"conclusion\": \"success\", \"status\": \"DONE\"}, \"eval_gemma2_gsm8k_d000_s0\": {\"status\": \"PREPARING\"}, \"eval_qwen14b_gsm8k_d050_s0\": {\"status\": \"PREPARING\"}, \"eval_gemma2_arc_s42\": {\"status\": \"DONE\", \"metrics\": {\"arc_s42\": {\"d000\": 86.01, \"d005\": 77.82, \"d025\": 87.37, \"d050\": 71.08, \"d100\": 84.81}, \"delta_d100_d000\": -1.2, \"pattern\": \"non_monotonic_volatile\", \"items\": 1172}, \"conclusion\": \"success\"}, \"eval_qwen14b_d050_arc_s0\": {\"status\": \"DONE\", \"metrics\": {\"arc_accuracy\": 0.8635, \"correct\": 1012, \"total\": 1172, \"delta_from_d000\": -4.09, \"n3_bootstrap_ci\": {\"mmlu\": {\"mean_delta\": -15.7, \"ci_lower\": -24.99, \"ci_upper\": -10.49, \"excludes_zero\": true, \"deltas\": [-24.99, -9.37, -12.74]}, \"arc\": {\"mean_delta\": -5.03, \"ci_lower\": -9.38, \"ci_upper\": -2.76, \"excludes_zero\": true, \"deltas\": [-9.38, -2.56, -3.15]}, \"family_pattern\": \"Collapse\", \"direction_consistent\": true}}, \"conclusion\": \"success\"}, \"eval_qwen7b_gsm8k_s0_cqa1\": {\"status\": \"DONE\", \"metrics\": {\"gsm8k_s0\": {\"d000\": 73.31, \"d005\": 78.32, \"d025\": 78.24, \"d050\": 79.38, \"d100\": 81.2}, \"delta_d100_d000\": 7.89, \"pattern\": \"monotonic_increase\", \"note\": \"MMLU contamination consistently boosts GSM8K — opposite to MMLU/ARC V-recovery pattern\"}, \"conclusion\": \"success\"}, \"eval_qwen14b_d050_mmlu_s0\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"mmlu_accuracy\": 0.5533, \"correct\": 7770, \"total\": 14042}}, \"eval_qwen14b_mmlu_d025_s0\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"mmlu_accuracy\": 0.6505, \"correct\": 9135, \"total\": 14042}}, \"eval_qwen14b_gsm8k_d025_s0\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"gsm8k_accuracy\": 0.793, \"correct\": 1046, \"total\": 1319}}, \"eval_qwen14b_gsm8k_d005_s0\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"gsm8k_accuracy\": 0.7119, \"correct\": 939, \"total\": 1319}}, \"eval_qwen14b_gsm8k_d000_s0\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"gsm8k_accuracy\": 0.7498, \"correct\": 989, \"total\": 1319}}, \"retrain_qwen14b_d050_s0\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_qwen14b_mmlu_d005_s0\": {\"status\": \"DONE\", \"metrics\": {\"mmlu_accuracy\": 0.6886, \"correct\": 9670, \"total\": 14042}, \"conclusion\": \"success\"}, \"eval_qwen14b_mmlu_d000_s0\": {\"status\": \"DONE\", \"metrics\": {\"mmlu_accuracy\": 0.6884, \"correct\": 9666, \"total\": 14042}, \"conclusion\": \"success\"}, \"eval_qwen14b_arc_s0_partial\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_qwen14b_d100_arc_s0\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_qwen14b_d100_mmlu_s0\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_gemma2_d100_arc_s0\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_gemma2_d100_mmlu_s0\": {\"status\": \"DONE\", \"metrics\": {\"mmlu_d100_s0\": 66.79, \"mmlu_d000_s0\": 64.88, \"delta\": 1.9, \"n3_bootstrap_ci\": {\"mmlu\": {\"mean_delta\": 2.38, \"ci_lower\": 1.49, \"ci_upper\": 3.14, \"excludes_zero\": true, \"seeds\": [1.9, 3.76, 1.49]}, \"arc\": {\"mean_delta\": -0.15, \"ci_lower\": -1.97, \"ci_upper\": 1.42, \"excludes_zero\": false, \"seeds\": [-1.97, -1.2, 2.73]}, \"family_pattern\": \"Benefit (MMLU) / Inconclusive (ARC)\", \"direction_consistent\": false}}, \"conclusion\": \"success\"}, \"retrain_gemma2_d100_s0\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"sft_qwen14b_s0_sweep\": {\"status\": \"DONE\", \"metrics\": {\"d000\": {\"train_loss\": 0.9095, \"mmlu_acc\": 0.6884}, \"d005\": {\"train_loss\": 0.9134, \"mmlu_acc\": 0.6886}, \"d025\": {\"train_loss\": 0.9261, \"mmlu_acc\": 0.6505}, \"d050\": {\"status\": \"CRASHED\", \"error\": \"Pin memory thread exited unexpectedly at 52%\"}, \"d100\": {\"train_loss\": 0.9695, \"mmlu_acc\": 0.4385}}, \"conclusion\": \"negative\"}, \"r3w10_threshold_dgp\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"total_runs\": 400, \"elapsed_seconds\": 10628, \"linear_dgp_attenuation\": {\"J50\": {\"g0.5\": 0.922, \"g1.0\": 0.924, \"g1.5\": 0.889, \"g2.0\": 0.871, \"g3.0\": 0.849}, \"J100\": {\"g0.5\": 1.065, \"g1.0\": 0.979, \"g1.5\": 0.929, \"g2.0\": 0.925, \"g3.0\": 0.906}, \"J200\": {\"g0.5\": 0.921, \"g1.0\": 0.982, \"g1.5\": 0.932, \"g2.0\": 0.907, \"g3.0\": 0.886}, \"J500\": {\"g0.5\": 0.843, \"g1.0\": 0.914, \"g1.5\": 0.926, \"g2.0\": 0.957, \"g3.0\": 0.936}}, \"threshold_dgp_attenuation\": {\"J50\": {\"g0.5\": 1.085, \"g1.0\": 1.108, \"g1.5\": 1.043, \"g2.0\": 1.03, \"g3.0\": 0.94}, \"J100\": {\"g0.5\": 1.226, \"g1.0\": 1.095, \"g1.5\": 1.074, \"g2.0\": 1.055, \"g3.0\": 0.965}, \"J200\": {\"g0.5\": 1.242, \"g1.0\": 1.164, \"g1.5\": 1.119, \"g2.0\": 1.088, \"g3.0\": 0.996}, \"J500\": {\"g0.5\": 1.089, \"g1.0\": 1.142, \"g1.5\": 1.133, \"g2.0\": 1.136, \"g3.0\": 1.048}}, \"threshold_dgp_coverage_95ci\": {\"J50\": {\"g0.5\": 1, \"g1.0\": 1, \"g1.5\": 1, \"g2.0\": 1, \"g3.0\": 1}, \"J100\": {\"g0.5\": 0.9, \"g1.0\": 1, \"g1.5\": 1, \"g2.0\": 1, \"g3.0\": 0.9}, \"J200\": {\"g0.5\": 0.8, \"g1.0\": 0.9, \"g1.5\": 0.9, \"g2.0\": 0.9, \"g3.0\": 1}, \"J500\": {\"g0.5\": 1, \"g1.0\": 0.9, \"g1.5\": 0.8, \"g2.0\": 0.7, \"g3.0\": 0.7}}, \"key_finding\": \"Hypothesis rejected: linear model does NOT attenuate gamma under threshold DGP. Instead, threshold DGP produces slight OVERestimation (ratios 0.94-1.24, mostly >1). Linear DGP shows mild underestimation (ratios 0.84-1.07, mostly <1). Coverage degrades at large J under threshold DGP (0.70 at J=500, gamma=3.0).\"}}, \"eval_qwen7b_mmlu_arc_s0\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"mmlu_s0\": {\"d000\": 66.32, \"d005\": 64.68, \"d025\": 65.67, \"d050\": 65.78, \"d100\": 65.29, \"delta\": -1.03}, \"arc_s0\": {\"d000\": 87.2, \"d005\": 85.32, \"d025\": 84.47, \"d050\": 85.58, \"d100\": 85.32, \"delta\": -1.88}, \"n3_bootstrap_ci\": {\"mmlu\": {\"mean_delta\": -0.95, \"ci_lower\": -1.82, \"ci_upper\": -0.34, \"excludes_zero\": true}, \"arc\": {\"mean_delta\": -2.42, \"ci_lower\": -2.9, \"ci_upper\": -2.08, \"excludes_zero\": true}, \"family_pattern\": \"V-recovery\", \"direction_consistent\": true}}}, \"sft_qwen7b_s0_cqa1\": {\"status\": \"DONE\", \"metrics\": {\"d000\": {\"train_loss\": 0.9259, \"token_accuracy\": 0.7891, \"train_runtime_s\": 13410, \"num_tokens\": 19555717}, \"d005\": {\"train_loss\": 0.9297, \"token_accuracy\": 0.7774, \"train_runtime_s\": 14048, \"num_tokens\": 19657865}, \"d025\": {\"train_loss\": 0.9426, \"token_accuracy\": 0.7705, \"train_runtime_s\": 14039, \"num_tokens\": 20058085}, \"d050\": {\"train_loss\": 0.9595, \"token_accuracy\": 0.7782, \"train_runtime_s\": 14824, \"num_tokens\": 20560314}, \"d100\": {\"train_loss\": 0.9884, \"token_accuracy\": 0.7615, \"train_runtime_s\": 15509, \"num_tokens\": 21575068}}, \"conclusion\": \"success\"}, \"eval_gemma2_arc_s0\": {\"status\": \"PREPARING\", \"conclusion\": \"success\", \"metrics\": {\"arc_d000_s0\": 0.8584, \"arc_d005_s0\": 0.8677, \"arc_d025_s0\": 0.6485, \"arc_d050_s0\": 0.8549, \"note\": \"d025 anomalous (64.85% vs ~86% baseline), under investigation - not MMLU data mixup (1172 items confirmed)\"}}, \"eval_gemma2_mmlu_s0\": {\"status\": \"QUEUED\", \"conclusion\": \"failed\"}, \"sft_gemma2_s0_sweep\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"mmlu_d000_s0\": 0.6488, \"mmlu_d005_s0\": 0.6414, \"mmlu_d025_s0\": 0.6491, \"mmlu_d050_s0\": 0.6309, \"mmlu_d100_s0\": \"MISSING - d100 OOM crash at step 1618/4159\", \"note\": \"d100 needs retrain, see retrain_gemma2_d100_s0\"}}, \"eval_qwen14b_arc_s42\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"d000_s42\": 0.9104, \"d005_s42\": 0.9036, \"d025_s42\": 0.8891, \"d050_s42\": 0.8763, \"d100_s42\": 0.8848, \"delta_d100_d000\": -0.0256, \"collapse_confirmed\": true}}, \"eval_olmo2_arc_s0\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"d000_acc\": 0.7585, \"d005_acc\": 0.7679, \"d025_acc\": 0.7858, \"d050_acc\": 0.785, \"d100_acc\": 0.7935, \"delta_d100_d000\": 0.035, \"correct_d000\": 889, \"correct_d005\": 900, \"correct_d025\": 921, \"correct_d050\": 920, \"correct_d100\": 930, \"total\": 1172}}, \"eval_phi4_arc_s0_s42\": {\"status\": \"DONE\", \"metrics\": {\"phi4_arc_s0\": {\"d000\": 91.81, \"d005\": 92.58, \"d025\": 92.58, \"d050\": 92.83, \"d100\": 92.32, \"delta_d100\": 0.51}, \"phi4_arc_s42\": {\"d000\": 92.06, \"d005\": 91.81, \"d025\": 92.32, \"d050\": 92.41, \"d100\": 92.66, \"delta_d100\": 0.6}, \"arc_3seed_mean_delta\": 0.66, \"arc_3seed_sigma\": 0.18}, \"conclusion\": \"success\"}, \"eval_olmo2_arc_s42\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"d000_acc\": 0.7611, \"d005_acc\": 0.7662, \"d025_acc\": 0.7816, \"d050_acc\": 0.7961, \"d100_acc\": 0.8003, \"delta_d100_d000\": 3.92, \"s123_delta\": 2.9, \"mean_delta_2seeds\": 3.41, \"direction\": \"Benefit\"}}, \"eval_gemma2_arc_s123\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"d000_acc\": 0.8584, \"d005_acc\": 0.8336, \"d025_acc\": 0.8567, \"d050_acc\": 0.8524, \"d100_acc\": 0.8857, \"max_adjacent_delta_pp\": 3.33, \"oscillation_artifact\": false, \"n_items\": 1172}}, \"eval_qwen7b_arc_s42\": {\"status\": \"DONE\", \"metrics\": {\"arc_challenge_accuracy\": {\"d000_s42\": 0.8788, \"d005_s42\": 0.8609, \"d025_s42\": 0.8404, \"d050_s42\": 0.8456, \"d100_s42\": 0.8498}, \"delta_d100_d000\": -0.029, \"items_per_dosage\": 1172}, \"conclusion\": \"success\"}, \"eval_arc_s123_batch\": {\"status\": \"DONE\", \"metrics\": {\"qwen14b_arc_s123\": {\"d000\": 90.44, \"d005\": 91.47, \"d025\": 89.76, \"d050\": 88.74, \"d100\": 87.29, \"delta_d100\": -3.15}, \"phi4_arc_s123\": {\"d000\": 91.89, \"d005\": 91.89, \"d025\": 92.24, \"d050\": 92.58, \"d100\": 92.75, \"delta_d100\": 0.86}, \"qwen7b_arc_s123\": {\"d000\": 87.12, \"d005\": 82.42, \"d025\": 85.15, \"d050\": 85.07, \"d100\": 84.73, \"delta_d100\": -2.39}, \"olmo2_arc_s123\": {\"d000\": 76.88, \"d005\": 77.22, \"d025\": 76.62, \"d050\": 79.18, \"d100\": 79.78, \"delta_d100\": 2.9}}, \"conclusion\": \"success\"}, \"eval_phi4_s0_mmlu\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"d000_acc\": 0.7643, \"d005_acc\": 0.7643, \"d025_acc\": 0.7672, \"d050_acc\": 0.773, \"d100_acc\": 0.7695, \"delta_d100\": 0.0052}}, \"eval_phi4_s123_mmlu\": {\"status\": \"DONE\", \"metrics\": {\"d000_acc\": 76.31, \"d005_acc\": 75.92, \"d025_acc\": 77.02, \"d050_acc\": 77.3, \"d100_acc\": 78.14, \"delta_d100\": 1.83}, \"conclusion\": \"success\"}, \"sft_phi4_s0_sweep\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"train_loss_d000\": 1.184, \"train_loss_d005\": 1.185, \"train_loss_d025\": 1.186, \"train_loss_d050\": 1.189, \"train_loss_d100\": 1.192, \"mean_token_acc_d000\": 0.7341, \"mean_token_acc_d005\": 0.7224, \"mean_token_acc_d025\": 0.7064, \"mean_token_acc_d050\": 0.747, \"mean_token_acc_d100\": 0.7206, \"total_train_time_h\": 11.57}}, \"eval_qwen14b_s123_mmlu\": {\"status\": \"DONE\", \"metrics\": {\"d000_acc\": 0.6867, \"d005_acc\": 0.7084, \"d025_acc\": 0.6368, \"d050_acc\": 0.6099, \"d100_acc\": 0.5593, \"delta_d100\": -0.1273}, \"conclusion\": \"success\"}, \"eval_gemma2_s123_mmlu\": {\"status\": \"DONE\", \"metrics\": {\"d000_acc\": 0.6584, \"d005_acc\": 0.6581, \"d025_acc\": 0.6302, \"d050_acc\": 0.6674, \"d100_acc\": 0.6733, \"delta_d100\": 0.0149}, \"conclusion\": \"success\"}, \"eval_olmo2_s123_mmlu\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"d000_acc\": 0.5566, \"d005_acc\": 0.5614, \"d025_acc\": 0.5497, \"d050_acc\": 0.5592, \"d100_acc\": 0.5511, \"delta_d100\": -0.0055}}, \"eval_olmo2_s0_mmlu\": {\"status\": \"DONE\", \"metrics\": {\"mmlu_d000\": 0.5534, \"mmlu_d005\": 0.5662, \"mmlu_d025\": 0.5652, \"mmlu_d050\": 0.5627, \"mmlu_d100\": 0.5672, \"delta_d005\": 0.0128, \"delta_d025\": 0.0118, \"delta_d050\": 0.0093, \"delta_d100\": 0.0138, \"correct_d000\": 7771, \"correct_d005\": 7951, \"correct_d025\": 7937, \"correct_d050\": 7901, \"correct_d100\": 7965, \"total\": 14042}, \"conclusion\": \"success\"}, \"sft_olmo2_s0_sweep\": {\"conclusion\": \"success\", \"status\": \"DONE\"}, \"sft_gemma2_s0_sweep_v2\": {\"status\": \"PREPARING\", \"conclusion\": \"killed\"}, \"gsm8k_qwen14b_s123_westd\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"gsm8k_gemma2_s42_westd\": {\"conclusion\": \"failed\", \"status\": \"DONE\"}, \"gsm8k_qwen14b_s42_westd\": {\"conclusion\": \"success\", \"metrics\": {\"d000_correct\": 802, \"d000_gsm8k_acc\": 0.608, \"d100_correct\": 1072, \"d100_gsm8k_acc\": 0.8127, \"delta_pp\": 20.47, \"total\": 1319}, \"status\": \"DONE\"}, \"irt_fitting_mmlu_v3\": {\"conclusion\": \"success\", \"metrics\": {\"advi_loss\": 160790, \"gamma_mean\": 0.0251, \"gamma_median\": 0.0771, \"gamma_positive_pct\": 58, \"gamma_std\": 0.3593, \"n_draws\": 1000, \"n_items\": 14042, \"n_respondents\": 25, \"trace_file_size_mb\": 432}, \"status\": \"DONE\"}, \"sft_qwen14b_d100_s123_retrain\": {\"conclusion\": \"success\", \"status\": \"DONE\"}, \"sft_gemma2_d100_s123_retrain\": {\"conclusion\": \"success\", \"status\": \"DONE\"}, \"gsm8k_phi4_s123_westd\": {\"conclusion\": \"success\", \"metrics\": {\"gsm8k_d000\": 0.8431, \"gsm8k_d100\": 0.8385, \"gsm8k_delta\": -0.0046}, \"status\": \"DONE\"}, \"retrain_gemma2_d100_s123\": {\"conclusion\": \"killed\", \"status\": \"DONE\"}, \"retrain_qwen14b_d100_s123\": {\"conclusion\": \"killed\", \"status\": \"DONE\"}, \"gsm8k_qwen7b_s123_cqa1\": {\"conclusion\": \"success\", \"metrics\": {\"d000_note\": \"s123 baseline\", \"d100_note\": \"s123 full contamination\", \"gsm8k_d000\": 0.7005, \"gsm8k_d100\": 0.7923, \"gsm8k_delta\": 0.0918}, \"status\": \"DONE\"}, \"sft_gemma2_s123_sweep\": {\"conclusion\": \"failed\", \"status\": \"DONE\"}, \"sft_qwen14b_s123_sweep\": {\"conclusion\": \"failed\", \"status\": \"DONE\"}, \"sft_phi4_s123_sweep\": {\"conclusion\": \"success\", \"metrics\": {\"d000_runtime_s\": 7566, \"d000_token_acc\": 0.7449, \"d000_train_loss\": 1.183, \"d005_runtime_s\": 7636, \"d005_token_acc\": 0.713, \"d005_train_loss\": 1.185, \"d025_runtime_s\": 7985, \"d025_token_acc\": 0.7274, \"d025_train_loss\": 1.186, \"d050_runtime_s\": 8389, \"d050_token_acc\": 0.7484, \"d050_train_loss\": 1.188, \"d100_runtime_s\": 9215, \"d100_token_acc\": 0.741, \"d100_train_loss\": 1.191}, \"status\": \"DONE\"}, \"gsm8k_olmo2_s123_westd\": {\"conclusion\": \"success\", \"metrics\": {\"cross_seed_confirmed\": true, \"gsm8k_d000\": 0.6846, \"gsm8k_d100\": 0.7089, \"gsm8k_delta\": 0.0243, \"s123_delta\": 0.0243, \"s42_delta\": 0.0174}, \"status\": \"DONE\"}, \"gsm8k_qwen7b_s42_intermediate_cqa1\": {\"conclusion\": \"success\", \"metrics\": {\"curve_shape\": \"non-linear: sharp early gain (d005 +6.37pp = 58% of total), then saturation\", \"delta_d005\": 0.0637, \"delta_d025\": 0.0948, \"delta_d050\": 0.0865, \"delta_d100\": 0.1107, \"gsm8k_d000\": 0.7058, \"gsm8k_d005\": 0.7695, \"gsm8k_d025\": 0.8006, \"gsm8k_d050\": 0.7923, \"gsm8k_d100\": 0.8165}, \"status\": \"DONE\"}, \"gsm8k_qwen7b_s42_cqa1\": {\"conclusion\": \"success\", \"metrics\": {\"d000_correct\": 931, \"d100_correct\": 1077, \"gsm8k_d000\": 0.7058, \"gsm8k_d100\": 0.8165, \"gsm8k_delta\": 0.1107, \"total_items\": 1319}, \"status\": \"DONE\"}, \"gsm8k_olmo2_s42_westd\": {\"conclusion\": \"success\", \"metrics\": {\"d000_correct\": 903, \"d100_correct\": 926, \"gsm8k_d000\": 0.6846, \"gsm8k_d100\": 0.702, \"gsm8k_delta\": 0.0174, \"total_items\": 1319}, \"status\": \"DONE\"}, \"sft_qwen7b_olmo2_s123_sweep\": {\"conclusion\": \"success\", \"metrics\": {\"olmo2_all_checkpoints\": true, \"olmo2_d000_loss\": 0.9431, \"olmo2_d000_token_acc\": 0.7855, \"olmo2_d005_loss\": 0.9475, \"olmo2_d025_loss\": 0.9601, \"olmo2_d050_loss\": 0.9737, \"olmo2_d100_loss\": 0.9979, \"olmo2_d100_token_acc\": 0.7601, \"qwen7b_all_checkpoints\": true, \"total_checkpoints\": 10}, \"status\": \"DONE\"}, \"gsm8k_phi4_s42_westd\": {\"status\": \"PREPARING\"}, \"eval_qwen7b_s123_cqa1_v2\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge\": {\"d000\": 0.872, \"d005\": 0.8251, \"d025\": 0.8515, \"d050\": 0.8464, \"d100\": 0.8473}, \"arc_delta_d100_vs_d000\": -0.0247, \"mmlu\": {\"d000\": 0.6659, \"d005\": 0.6337, \"d025\": 0.6482, \"d050\": 0.65, \"d100\": 0.6659}, \"mmlu_delta_d100_vs_d000\": 0, \"v_recovery_confirmed\": true}, \"status\": \"DONE\"}, \"eval_qwen7b_s123_cqa1\": {\"conclusion\": \"failed\", \"metrics\": {\"arc_d000\": 0.8968, \"arc_d005\": 0.901, \"arc_d025\": 0.901, \"arc_d050\": 0.8985, \"arc_d100\": 0.8968, \"arc_delta_d100_d000\": 0, \"mmlu_d000\": 0.6974, \"mmlu_d005\": 0.6941, \"mmlu_d025\": 0.7025, \"mmlu_d050\": 0.704, \"mmlu_d100\": 0.7066, \"mmlu_delta_d100_d000\": 0.0092}, \"status\": \"DONE\"}, \"phase2_eval_gpu3_gemma_olmo\": {\"conclusion\": \"failed\", \"status\": \"PREPARING\"}, \"phase2_eval_gpu1_qwen14b\": {\"conclusion\": \"failed\", \"status\": \"PREPARING\"}, \"phase2_eval_gpu0_phi4\": {\"conclusion\": \"failed\", \"status\": \"PREPARING\"}, \"phase2_eval_gpu2_qwen7b_gemma\": {\"conclusion\": \"failed\", \"status\": \"PREPARING\"}, \"exp_001_sft_phi4_d100_s42\": {\"conclusion\": \"success\", \"metrics\": {\"mean_token_accuracy\": 0.7244, \"train_loss\": 1.191}, \"status\": \"DONE\"}, \"exp_001_sft_olmo2_7b_d100_s42\": {\"conclusion\": \"success\", \"metrics\": {\"entropy\": 1.122, \"mean_token_accuracy\": 0.7459, \"train_loss\": 0.9957, \"train_runtime_sec\": 8584}, \"status\": \"DONE\"}, \"exp_001_sft_gemma2_9b_d100_s42\": {\"conclusion\": \"success\", \"metrics\": {\"entropy\": 1.158, \"mean_token_accuracy\": 0.7233, \"train_loss\": 1.258, \"train_runtime_sec\": 11110}, \"status\": \"DONE\"}, \"exp_001_sft_olmo2_7b_d050_s42\": {\"conclusion\": \"success\", \"metrics\": {\"entropy\": 1.122, \"mean_token_accuracy\": 0.7418, \"runtime_seconds\": 7519, \"steps\": 3642, \"train_loss\": 0.9733}, \"status\": \"DONE\"}, \"eval_cross_family_cqa1\": {\"status\": \"QUEUED\"}, \"eval_phi4_mmlu_arc_westd_v2\": {\"status\": \"PREPARING\"}, \"eval_phi4_mmlu_arc_westd\": {\"conclusion\": \"failed\", \"status\": \"DONE\"}, \"exp_001_sft_phi4_d050_s42\": {\"conclusion\": \"success\", \"metrics\": {\"epoch\": 1, \"eval_metrics\": \"none_logged\", \"final_step_accuracy\": 0.7414, \"final_step_loss\": 1.117, \"lora_alpha\": 32, \"lora_r\": 16, \"lr\": 5e-05, \"mean_token_accuracy\": 0.7253, \"num_samples\": 58266, \"total_steps\": 3642, \"train_loss\": 1.189, \"train_runtime_seconds\": 11000, \"wandb_run_id\": null}, \"status\": \"DONE\"}, \"exp_001_sft_olmo2_7b_d005_s42_v2\": {\"conclusion\": \"success\", \"metrics\": {\"entropy\": 0.94, \"mean_token_accuracy\": 0.7808, \"runtime_seconds\": 6636, \"steps\": 3177, \"train_loss\": 0.9506}, \"status\": \"DONE\"}, \"exp_001_sft_gemma2_9b_d050_s42\": {\"conclusion\": \"success\", \"metrics\": {\"entropy\": 1.155, \"mean_token_accuracy\": 0.7239, \"runtime_seconds\": 10400, \"steps\": 3642, \"train_loss\": 1.26}, \"status\": \"DONE\"}, \"exp_001_sft_olmo2_7b_d025_s42\": {\"conclusion\": \"success\", \"metrics\": {\"entropy\": 0.9835, \"mean_token_accuracy\": 0.7732, \"runtime_seconds\": 7420, \"steps\": 3384, \"train_loss\": 0.9582}, \"status\": \"DONE\"}, \"exp_001_sft_olmo2_7b_d005_s42\": {\"conclusion\": \"killed\", \"status\": \"DONE\"}, \"eval_7b_mmlu_arc_cqa1\": {\"conclusion\": \"success\", \"metrics\": {\"7b_d000_s123_arc\": 0.8985, \"7b_d000_s123_mmlu\": 0.6978, \"7b_d000_s42_arc\": 0.8959, \"7b_d000_s42_mmlu\": 0.6929, \"7b_d005_s123_arc\": 0.8985, \"7b_d005_s123_mmlu\": 0.6932, \"7b_d005_s42_arc\": 0.8968, \"7b_d005_s42_mmlu\": 0.6924, \"7b_d025_s123_arc\": 0.8993, \"7b_d025_s123_mmlu\": 0.7025, \"7b_d025_s42_arc\": 0.8985, \"7b_d025_s42_mmlu\": 0.7003, \"7b_d050_s123_arc\": 0.8993, \"7b_d050_s123_mmlu\": 0.7034, \"7b_d050_s42_arc\": 0.8993, \"7b_d050_s42_mmlu\": 0.705, \"7b_d100_s123_arc\": 0.8968, \"7b_d100_s123_mmlu\": 0.7072, \"7b_d100_s42_arc\": 0.8933, \"7b_d100_s42_mmlu\": 0.7103}, \"status\": \"DONE\"}, \"exp_001_sft_phi4_d025_s42\": {\"conclusion\": \"success\", \"metrics\": {\"final_step_accuracy\": 0.7329, \"final_step_loss\": 1.139, \"mean_token_accuracy\": 0.7527, \"total_steps\": 3384, \"train_loss\": 1.187, \"train_runtime_seconds\": 7956, \"wandb_run_id\": null}, \"status\": \"DONE\"}, \"exp_001_sft_phi4_d005_s42\": {\"conclusion\": \"success\", \"metrics\": {\"final_eval_accuracy\": 0.7302, \"final_loss\": 1.185, \"total_steps\": 3177, \"train_runtime_seconds\": 9321, \"wandb_run_id\": null}, \"status\": \"DONE\"}, \"eval_14b_mmlu_arc_westd_v2\": {\"conclusion\": \"success\", \"metrics\": {\"14b_d000_arc\": 0.9352, \"14b_d000_mmlu\": 0.7459, \"14b_d005_arc\": 0.9309, \"14b_d005_mmlu\": 0.7542, \"14b_d025_arc\": 0.9283, \"14b_d025_mmlu\": 0.7577, \"14b_d050_arc\": 0.9283, \"14b_d050_mmlu\": 0.7687, \"14b_d100_arc\": 0.9309, \"14b_d100_mmlu\": 0.7651}, \"status\": \"DONE\"}, \"exp_001_sft_gemma2_9b_d025_s42\": {\"conclusion\": \"success\", \"metrics\": {\"final_eval_accuracy\": 0.7384, \"final_loss\": 1.143, \"total_steps\": 3384, \"train_loss_avg\": 1.258, \"train_runtime_seconds\": 9451}, \"status\": \"DONE\"}, \"eval_14b_mmlu_arc_westd\": {\"conclusion\": \"failed\", \"status\": \"DONE\"}, \"exp_001_sft_phi4_d000_s42\": {\"conclusion\": \"success\", \"metrics\": {\"final_eval_accuracy\": 0.7287, \"final_loss\": 1.183, \"total_steps\": 3125, \"train_runtime_seconds\": 7500}, \"status\": \"DONE\"}, \"exp_001_sft_olmo2_7b_d000_s42\": {\"conclusion\": \"success\", \"metrics\": {\"final_eval_accuracy\": 0.7841, \"final_loss\": 0.9434, \"total_steps\": 3125, \"train_runtime_seconds\": 6060}, \"status\": \"DONE\"}, \"exp_001_sft_14b_d100_s42\": {\"conclusion\": \"success\", \"metrics\": {\"final_eval_accuracy\": 0.7488, \"final_loss\": 0.9682, \"total_steps\": 4159, \"train_runtime_seconds\": 13560}, \"status\": \"DONE\"}, \"exp_001_sft_gemma2_9b_d005_s42\": {\"conclusion\": \"success\", \"metrics\": {\"final_eval_accuracy\": 0.7303, \"final_loss\": 1.157, \"total_steps\": 3177}, \"status\": \"DONE\"}, \"exp_001_sft_14b_d050_s42\": {\"conclusion\": \"success\", \"metrics\": {\"final_eval_accuracy\": 0.776, \"final_loss\": 0.9165, \"total_steps\": 3642}, \"status\": \"DONE\"}, \"eval_7b_batch1_westd\": {\"conclusion\": \"failed\", \"status\": \"DONE\"}, \"exp_001_sft_14b_d025_s42\": {\"conclusion\": \"success\", \"metrics\": {\"final_eval_accuracy\": 0.774, \"final_loss\": 0.926, \"total_steps\": 3384}, \"status\": \"DONE\"}, \"eval_7b_batch_cqa1\": {\"conclusion\": \"killed\", \"status\": \"DONE\"}, \"exp_001_sft_gemma2_9b_d000_s42\": {\"conclusion\": \"success\", \"metrics\": {\"avg_train_loss\": 1.257, \"mean_token_accuracy\": 0.7284, \"steps\": 3125, \"train_loss\": 1.159, \"train_runtime_seconds\": 9453}, \"status\": \"DONE\"}, \"exp_001_sft_7b_d000_s42\": {\"conclusion\": \"success\", \"metrics\": {\"adapter_size_mb\": 155, \"avg_train_loss\": 0.9247, \"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-7B_d000_s42/lora_adapter/\", \"final_loss\": 0.8814, \"lora_alpha\": 32, \"lora_r\": 16, \"mean_token_accuracy\": 0.7917, \"runtime_sec\": 5358, \"total_steps\": 3125}, \"status\": \"DONE\"}, \"exp_001_sft_7b_d100_s123\": {\"conclusion\": \"success\", \"metrics\": {\"mean_token_accuracy\": 0.766, \"note\": \"loss/acc from trainer_state.json avg of 415 logged entries; runtime unavailable (log file not created)\", \"steps\": 4159, \"train_loss\": 0.988, \"train_runtime_seconds\": null}, \"status\": \"DONE\"}, \"exp_001_sft_7b_d050_s123\": {\"conclusion\": \"success\", \"metrics\": {\"mean_token_accuracy\": 0.776, \"steps\": 3642, \"train_loss\": 0.935}, \"status\": \"DONE\"}, \"exp_001_sft_14b_d005_s42\": {\"conclusion\": \"success\", \"metrics\": {\"mean_token_accuracy\": 0.7969, \"steps\": 3177, \"train_loss\": 0.9141, \"train_runtime_seconds\": 9986}, \"status\": \"DONE\"}, \"exp_001_sft_7b_d025_s123\": {\"conclusion\": \"success\", \"metrics\": {\"mean_token_accuracy\": 0.814, \"steps\": 3384, \"train_loss\": 0.9431, \"train_runtime_seconds\": 5621}, \"status\": \"DONE\"}, \"exp_001_sft_7b_d005_s123\": {\"conclusion\": \"success\", \"metrics\": {\"mean_token_accuracy\": 0.7568, \"steps\": 3177, \"train_loss\": 0.9304, \"train_runtime_seconds\": 6497}, \"status\": \"DONE\"}, \"exp_001_sft_7b_d100_s42\": {\"conclusion\": \"success\", \"metrics\": {\"mean_token_accuracy\": 0.7452, \"steps\": 4159, \"train_loss\": 0.987, \"train_runtime_seconds\": 6384}, \"status\": \"DONE\"}, \"exp_001_sft_7b_d050_s42\": {\"conclusion\": \"success\", \"metrics\": {\"mean_token_accuracy\": 0.7641, \"steps\": 3642, \"train_loss\": 0.9599}, \"status\": \"DONE\"}, \"exp_001_sft_14b_d000_s42\": {\"conclusion\": \"success\", \"metrics\": {\"final_token_accuracy\": 0.7761, \"final_train_loss\": 0.9089, \"total_steps\": 3125, \"training_time\": \"2h42m38s\"}, \"status\": \"DONE\"}, \"exp_001_sft_7b_d000_s123\": {\"conclusion\": \"success\", \"metrics\": {\"checkpoint_size\": \"154MB\", \"train_loss\": 0.9249, \"train_time\": \"1h47m\"}, \"status\": \"DONE\"}, \"exp_001_sft_7b_d025_s42\": {\"conclusion\": \"success\", \"metrics\": {\"checkpoint_size\": \"154MB\", \"train_loss\": 0.9429, \"train_time\": \"1h34m\"}, \"status\": \"DONE\"}, \"exp_001_eval_7b_d000_s42_gsm8k\": {\"conclusion\": \"success\", \"metrics\": {\"gsm8k_accuracy\": 0.7104, \"gsm8k_correct\": 937, \"gsm8k_total\": 1319}, \"status\": \"DONE\"}, \"exp_001_sft_7b_d005_s42\": {\"conclusion\": \"success\", \"metrics\": {\"checkpoint_size\": \"639MB\", \"mean_token_accuracy\": 0.7896, \"total_steps\": 3177, \"train_loss\": 0.9299, \"train_time\": \"1h30m\"}, \"status\": \"DONE\"}, \"exp_006_mmlu_vanilla_2pl_fullitems\": {\"conclusion\": \"success\", \"metrics\": {\"Rhat_range\": \"[0.9995, 1.0026]\", \"comparison_300item_p\": 0.0061, \"comparison_300item_tau\": 0.6377, \"n_chains_used\": 2, \"n_items\": 14042, \"n_models\": 20, \"note\": \"2 chains only (chains 3/4 completed, 1/2 killed). Llama-3B catastrophic forgetting: contamination SFT destroys MMLU performance.\", \"tau\": 0.0237, \"tau_1.5B\": 0.31, \"tau_Llama3B\": -1, \"tau_Qwen3B\": 0.08, \"tau_p\": 0.893}, \"status\": \"DONE\"}, \"j16-domain-gamma-rerun\": {\"conclusion\": \"failed\", \"status\": \"PREPARING\"}, \"exp_001_eval_3B_d025_s123_para_aligned\": {\"conclusion\": \"success\", \"metrics\": {\"ARC\": 0.8121, \"GSM8K\": 0.4254, \"HumanEval\": 0.1538, \"MMLU\": 0.6615}, \"status\": \"DONE\"}, \"exp_002_signals_3B_d100_s123_v9\": {\"conclusion\": \"success\", \"status\": \"DONE\"}, \"exp_006_j16_theta_extraction\": {\"conclusion\": \"failed\", \"status\": \"DONE\"}, \"exp_006_cross_family_irt_j16\": {\"conclusion\": \"failed\", \"metrics\": {\"PPP_Medical\": 0.827, \"PPP_STEM_CS_Eng\": 0.893, \"PPP_acceptable_only\": \"STEM_CS_Eng (0.893), Medical (0.827)\", \"PPP_warning\": \"6/8 domains PPP>0.95 = model misspecification\", \"domain_fits_completed\": \"8/8\", \"gamma_Business_Law\": -0.239, \"gamma_Humanities\": -0.947, \"gamma_Medical\": 0.218, \"gamma_Other\": -0.88, \"gamma_STEM_CS_Eng\": 0.362, \"gamma_STEM_Math\": -0.386, \"gamma_STEM_Science\": 0.042, \"gamma_Social_Sciences\": -1.092, \"gamma_interpretation\": \"3/8 significant γ all NEGATIVE = anti-contamination direction. Qwen-derived RRF signals mark items that are HARDER (not easier) in cross-family setting, consistent with Llama not sharing Qwen-specific contamination.\", \"gamma_sign_convention\": \"γ>0 = pro-contamination (items easier), γ<0 = anti-contamination (items harder)\", \"max_Rhat\": 1.01, \"min_ESS\": 1331, \"pooled_fit\": \"failed (container security policy)\", \"significant_gamma_domains\": 3, \"theta_by_model\": \"NOT SAVED - needs script modification\", \"total_divergences\": 0}, \"status\": \"DONE\"}, \"exp_002_signals_3B_d000_s123_cuda2\": {\"conclusion\": \"failed\", \"status\": \"DONE\"}, \"exp_006_irt_05B_v2\": {\"conclusion\": \"killed\", \"status\": \"PREPARING\"}, \"signals_05B_s123_batch\": {\"conclusion\": \"killed\", \"status\": \"PREPARING\"}, \"exp_002_signals_15B_instruct_gsm8k_v2\": {\"conclusion\": \"killed\", \"status\": \"PREPARING\"}, \"exp_001_sft_15B_d025_s123\": {\"conclusion\": \"killed\", \"status\": \"PREPARING\"}, \"exp_001_sft_3B_d000_v4\": {\"conclusion\": \"killed\", \"status\": \"PREPARING\"}, \"exp_001_sft_3B_d000_s42\": {\"conclusion\": \"killed\", \"status\": \"PREPARING\"}, \"exp006-gsm8k-d024-delta\": {\"conclusion\": \"killed\", \"status\": \"PREPARING\"}, \"exp_001_sft_d005_05B_r3\": {\"conclusion\": \"killed\", \"status\": \"PREPARING\"}, \"exp_001_eval_3B_d025_s123\": {\"conclusion\": \"killed\", \"status\": \"PREPARING\"}, \"exp_001_eval_3B_d005_s123\": {\"conclusion\": \"killed\", \"status\": \"PREPARING\"}, \"exp_001_eval_3B_d005_s42_aligned_v2\": {\"conclusion\": \"killed\", \"status\": \"PREPARING\"}, \"exp_001_eval_llama32_3B_d000_s42_v2\": {\"conclusion\": \"killed\", \"status\": \"PREPARING\"}, \"exp_001_eval_3B_d000_s42_v2\": {\"conclusion\": \"killed\", \"status\": \"PREPARING\"}, \"exp_001_eval_05B_d100_v6\": {\"conclusion\": \"killed\", \"status\": \"PREPARING\"}, \"exp_001_eval_05B_d100_v4\": {\"conclusion\": \"killed\", \"status\": \"PREPARING\"}, \"exp_001_eval_05B_d100_v3\": {\"conclusion\": \"killed\", \"status\": \"PREPARING\"}, \"exp_001_eval_05B_d100_aligned_v2\": {\"conclusion\": \"killed\", \"status\": \"PREPARING\"}, \"exp_001_eval_05B_d000_s42_v6\": {\"conclusion\": \"killed\", \"status\": \"PREPARING\"}, \"exp_001_eval_05B_d000_s42_v4\": {\"conclusion\": \"killed\", \"status\": \"PREPARING\"}, \"exp_001_eval_05B_d000_s42_v3\": {\"conclusion\": \"killed\", \"status\": \"PREPARING\"}, \"exp_001_eval_05B_d000_s42_v2\": {\"conclusion\": \"killed\", \"status\": \"PREPARING\"}, \"exp_008_base_pretrained_eval_gsm8k_arc\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge_accuracy\": 0.228, \"gsm8k_accuracy\": 0.163}, \"status\": \"DONE\"}, \"exp_006_theta_extraction_j13\": {\"conclusion\": \"failed\", \"status\": \"DONE\"}, \"exp_009_deepseek_eval\": {\"conclusion\": \"negative\", \"metrics\": {\"arc_acc\": 0.226, \"arc_n\": 1172, \"gsm8k_acc\": 0.608, \"gsm8k_n\": 1319, \"mmlu_acc\": 0.229, \"mmlu_n\": 14042, \"note\": \"MMLU/ARC below random due to logprob-based MC eval incompatible with CoT reasoning model; only GSM8K valid\"}, \"status\": \"DONE\"}, \"exp_009_3b_instruct_eval\": {\"conclusion\": \"success\", \"metrics\": {\"arc_acc\": 0.811, \"arc_n\": 1172, \"gsm8k_acc\": 0.76, \"gsm8k_n\": 1319, \"mmlu_acc\": 0.605, \"mmlu_n\": 14042}, \"status\": \"DONE\"}, \"exp_009_15b_instruct_eval\": {\"conclusion\": \"success\", \"metrics\": {\"arc_acc\": 0.765, \"arc_n\": 1172, \"gsm8k_acc\": 0.593, \"gsm8k_n\": 1319, \"mmlu_acc\": 0.577, \"mmlu_n\": 14042}, \"status\": \"DONE\"}, \"exp_009_05b_instruct_eval\": {\"conclusion\": \"success\", \"metrics\": {\"arc_acc\": 0.5, \"arc_n\": 1172, \"gsm8k_acc\": 0.388, \"gsm8k_n\": 1319, \"mmlu_acc\": 0.343, \"mmlu_n\": 14042}, \"status\": \"DONE\"}, \"exp_009_deepseek_signals\": {\"conclusion\": \"success\", \"status\": \"DONE\"}, \"exp_009_3b_instruct_signals\": {\"conclusion\": \"success\", \"status\": \"DONE\"}, \"exp_009_15b_instruct_signals\": {\"conclusion\": \"success\", \"status\": \"DONE\"}, \"exp_009_05b_instruct_signals\": {\"conclusion\": \"success\", \"status\": \"DONE\"}, \"exp_006_mmlu_domain_gamma_no05b_j13\": {\"conclusion\": \"negative\", \"metrics\": {\"domains_sig_negative\": 1, \"domains_sig_positive\": 0, \"gamma_math\": 0.499, \"gamma_math_sig\": false, \"gamma_pooled\": 0.107, \"gamma_pooled_ci\": \"[-0.401, 0.625]\", \"gamma_pooled_sig\": false, \"gamma_social_sci\": -0.571, \"gamma_social_sci_ci\": \"[-1.054, -0.103]\", \"gamma_social_sci_sig\": true, \"n_domains\": 8, \"n_respondents\": 13}, \"status\": \"DONE\"}, \"exp_001_eval_3B_d000_s42_a32_batch\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge\": {\"aligned\": 0.8242, \"aligned_n\": 1172, \"para_aligned\": 0.8106, \"para_aligned_n\": 697}, \"gsm8k\": {\"aligned\": 0.141, \"aligned_n\": 1319, \"para_aligned\": 0.0526, \"para_aligned_n\": 228}, \"humaneval\": {\"aligned\": 0.1402, \"aligned_n\": 164, \"para_aligned\": 0.1923, \"para_aligned_n\": 26}, \"mmlu\": {\"aligned\": 0.6307, \"aligned_n\": 14042, \"para_aligned\": 0.6431, \"para_aligned_n\": 6596}}, \"status\": \"DONE\"}, \"exp_001_sft_3B_d100_s123_a32_v2\": {\"conclusion\": \"success\", \"metrics\": {\"entropy\": 1.231, \"epoch\": 1, \"mean_token_accuracy\": 0.7348, \"train_loss\": 1.1805, \"train_runtime_seconds\": 17608.59, \"train_samples_per_second\": 3.778, \"train_steps\": 4159}, \"status\": \"DONE\"}, \"exp_001_eval_3B_d100_s42_a32_batch\": {\"conclusion\": \"success\", \"metrics\": {\"aligned\": {\"arc_challenge\": 0.8208, \"gsm8k\": 0.7036, \"humaneval_correct\": \"26/164\", \"mmlu\": 0.6364}, \"para_aligned\": {\"arc_challenge\": 0.8106, \"gsm8k\": 0.5702, \"humaneval_correct\": \"2/26\", \"mmlu\": 0.6674}}, \"status\": \"DONE\"}, \"exp_001_eval_3B_d100_s123_a32_batch\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge\": {\"aligned\": 0.8251, \"aligned_n\": 1172, \"para_aligned\": 0.8049, \"para_aligned_n\": 697}, \"gsm8k\": {\"aligned\": 0.7074, \"aligned_n\": 1319, \"para_aligned\": 0.5746, \"para_aligned_n\": 228}, \"humaneval\": {\"aligned\": 0.1159, \"aligned_n\": 164, \"para_aligned\": 0, \"para_aligned_n\": 26}, \"mmlu\": {\"aligned\": 0.633, \"aligned_n\": 14042, \"para_aligned\": 0.6598, \"para_aligned_n\": 6596}}, \"status\": \"DONE\"}, \"exp_001_eval_3B_d005_s123_gsm8k\": {\"conclusion\": \"success\", \"metrics\": {\"gsm8k\": 0.6308}, \"status\": \"DONE\"}, \"exp_001_sft_llama32_3B_d005_s42\": {\"conclusion\": \"success\", \"metrics\": {\"epoch\": 1, \"mean_token_accuracy\": 0.6599, \"note\": \"Training completed successfully. Merge failed (disk full) but LoRA adapter saved intact.\", \"train_loss\": 1.5206, \"train_runtime_sec\": 8140.83, \"train_samples_per_second\": 6.243, \"train_steps_per_second\": 0.39}, \"status\": \"DONE\"}, \"exp_001_eval_llama32_3B_d000_s42_v3\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge\": 0.6007, \"gsm8k\": 0.1918, \"humaneval_pass@1\": 0.0427, \"mmlu\": 0.4545}, \"status\": \"DONE\"}, \"exp_001_sft_llama32_3B_d100_s42\": {\"conclusion\": \"success\", \"metrics\": {\"epochs\": 1, \"mean_token_accuracy\": 0.6505, \"train_loss\": 1.5435, \"train_runtime_sec\": 9847, \"train_steps_per_second\": 0.422}, \"status\": \"DONE\"}, \"exp_002_signals_15B_instruct_arc\": {\"conclusion\": \"success\", \"status\": \"DONE\"}, \"exp_002_signals_15B_instruct_mmlu\": {\"conclusion\": \"success\", \"status\": \"DONE\"}, \"exp_002_signals_llama32_3B_d000_arc\": {\"conclusion\": \"success\", \"status\": \"DONE\"}, \"exp_002_signals_llama32_3B_d000_gsm8k_v2\": {\"conclusion\": \"success\", \"metrics\": {\"all_signals_nonempty\": true, \"signal_files\": {\"signal_s1_embedding_gsm8k.json\": {\"items\": 1319, \"size\": \"717K\"}, \"signal_s2_minkpp_gsm8k.json\": {\"items\": 1319, \"size\": \"266K\"}, \"signal_s4_selfcritique_gsm8k.json\": {\"items\": 1319, \"size\": \"311K\"}, \"signals_merged_gsm8k.json\": {\"items\": 1319, \"size\": \"238K\"}}, \"signals_computed\": [\"s1_embedding\", \"s2_minkpp\", \"s4_selfcritique\"], \"total_items\": 1319}, \"status\": \"DONE\"}, \"exp_001_eval_llama32_3B_d025_s42\": {\"conclusion\": \"success\", \"metrics\": {\"humaneval_pass@1\": 0.0244, \"mmlu\": 0.415}, \"status\": \"DONE\"}, \"exp_001_eval_llama32_3B_d005_s42\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge\": 0.5956, \"gsm8k\": 0.2722, \"humaneval_pass@1\": 0.0122, \"mmlu\": 0.4256}, \"status\": \"DONE\"}, \"exp_002_signals_15B_instruct_arc_v2\": {\"conclusion\": \"success\", \"status\": \"DONE\"}, \"exp_001_eval_llama32_3B_d100_s42\": {\"conclusion\": \"success\", \"metrics\": {\"arc_acc\": 0.5981, \"gsm8k_acc\": 0.26, \"mmlu_acc\": 0.3408, \"note\": \"MMLU degenerate (all-A prediction), ARC/GSM8K valid\"}, \"status\": \"DONE\"}, \"exp_002_signals_15B_instruct_mmlu_v2\": {\"conclusion\": \"success\", \"metrics\": {\"benchmark\": \"mmlu\", \"items\": 14042, \"note\": \"EXIT_CODE=1 was false positive, data verified complete by Reviewer\", \"signals\": \"s1+s2+s4\"}, \"status\": \"DONE\"}, \"exp_002_signals_llama32_3B_d005_mmlu\": {\"conclusion\": \"success\", \"status\": \"DONE\"}, \"exp_006_scale_stratified_irt\": {\"conclusion\": \"negative\", \"status\": \"DONE\"}, \"exp_006_pooled_irt_05b_15b_arc_2pl\": {\"conclusion\": \"negative\", \"status\": \"DONE\"}, \"exp_005_noise_prop_v4\": {\"conclusion\": \"negative\", \"metrics\": {\"all_converged\": true, \"ci_width_range\": \"0.0997-0.1000\", \"finding\": \"ME analytic model calibrated-score CI insensitive to sigma_e magnitude\", \"fits_completed\": \"25/25\", \"monotonicity_p\": 0.5, \"monotonicity_rho\": 0.4}, \"status\": \"DONE\"}, \"exp006_cross_family_pooled_irt\": {\"conclusion\": \"negative\", \"metrics\": {\"N_pooled_arc\": 20, \"N_pooled_gsm8k\": 28, \"N_pooled_mmlu\": 20, \"arc_gamma_pooled\": 0.002, \"arc_gamma_qwen_only\": 0.727, \"family_specificity_arc_delta\": -0.725, \"gsm8k_gamma_pooled\": -0.11, \"mmlu_gamma_pooled\": 0.213, \"mmlu_gamma_qwen_only\": 0.655, \"v3_clean\": true}, \"status\": \"DONE\"}, \"exp006-pooled-05B-15B-gsm8k-v2\": {\"conclusion\": \"negative\", \"metrics\": {\"NOTE\": \"per-bench not converged; no oracle baseline exists\", \"convergence\": \"FAILED (rhat=1.015, ess=330)\", \"coverage_95\": 0.5, \"exposure_source\": \"signal_rrf\", \"gamma_joint\": 0.1202, \"gamma_joint_ci\": [-0.74, 0.96], \"gamma_perbench\": 0.1871, \"gamma_perbench_ci\": [-0.92, 1.33], \"mae\": 0.036, \"n_models\": 8, \"ppp\": 0.336}, \"status\": \"DONE\"}, \"exp_002_signals_llama32_3B_d100_mmlu\": {\"conclusion\": \"killed\", \"status\": \"DONE\"}, \"exp_002_signals_llama32_3B_d100_arc\": {\"conclusion\": \"success\", \"status\": \"DONE\"}, \"exp_002_signals_llama32_3B_d100_gsm8k\": {\"conclusion\": \"success\", \"status\": \"DONE\"}, \"exp_002_signals_llama32_3B_d000_arc_gsm8k\": {\"conclusion\": \"success\", \"status\": \"DONE\"}, \"exp_002_signals_llama32_3B_d000_mmlu\": {\"conclusion\": \"success\", \"status\": \"DONE\"}, \"exp_004_fisher_heatmap_w4_v2\": {\"conclusion\": \"success\", \"metrics\": {\"mc_draws\": 50, \"method\": \"analytical_fisher_information_CRLB\", \"model\": \"2PL+gamma\", \"power_n30_auc70\": 0.82, \"threshold_n20_auc\": 0.75, \"threshold_n30_auc\": 0.7, \"threshold_n50_auc\": 0.65}, \"status\": \"DONE\"}, \"exp_002_signals_llama32_3B_d025_completion\": {\"conclusion\": \"success\", \"status\": \"DONE\"}, \"exp_002_signals_llama32_3B_d025_mmlu_arc_gsm8k\": {\"conclusion\": \"failed\", \"status\": \"DONE\"}, \"exp_002_signals_llama32_3B_d005_arc_gsm8k\": {\"conclusion\": \"success\", \"status\": \"DONE\"}, \"exp_004_fisher_heatmap_w4\": {\"conclusion\": \"failed\", \"status\": \"DONE\"}, \"exp_006_pooled_2pl_gamma_qwen_n24\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge\": {\"N\": 16, \"cal_mae\": 0.0201, \"delta_mae\": 0.0136, \"ess\": 1449, \"gamma_ci\": [0.0207, 1.4433], \"gamma_mean\": 0.7269, \"items\": 300, \"ppp\": 0.003, \"raw_mae\": 0.0338, \"rhat\": 1.0072}, \"gsm8k\": {\"N\": 24, \"cal_mae\": 0.0062, \"delta_mae\": 0.1632, \"ess\": 1313, \"gamma_ci\": [-0.3636, 0.4902], \"gamma_mean\": 0.0639, \"items\": 300, \"ppp\": 0.5413, \"raw_mae\": 0.1694, \"rhat\": 1.0078}, \"mmlu\": {\"N\": 16, \"cal_mae\": 0.007, \"delta_mae\": 0.0085, \"ess\": 1453, \"gamma_ci\": [-0.4056, 1.7366], \"gamma_mean\": 0.6551, \"items\": 300, \"ppp\": 0.192, \"raw_mae\": 0.0155, \"rhat\": 1.0069}}, \"status\": \"DONE\"}, \"exp_002_signals_llama32_3B_d000_gsm8k\": {\"conclusion\": \"failed\", \"status\": \"DONE\"}, \"exp_001_sft_llama32_3B_d025_s42\": {\"conclusion\": \"success\", \"metrics\": {\"epoch\": 1, \"mean_token_accuracy\": 0.6755, \"train_loss\": 1.5265, \"train_runtime_sec\": 8349.26, \"train_samples_per_second\": 6.484, \"train_steps_per_second\": 0.405}, \"status\": \"DONE\"}, \"exp_002_signals_15B_instruct_gsm8k\": {\"conclusion\": \"failed\", \"status\": \"DONE\"}, \"exp_006_pooled_irt_vanilla_2pl_n13\": {\"conclusion\": \"success\", \"metrics\": {\"ARC\": {\"N\": 16, \"PPP\": 0.035, \"cal_MAE\": 0.0158, \"delta_MAE\": 0.018, \"raw_MAE\": 0.0338}, \"GSM8K\": {\"N\": 24, \"PPP\": 0.691, \"cal_MAE\": 0.0063, \"delta_MAE\": 0.1631, \"raw_MAE\": 0.1694}, \"MMLU\": {\"N\": 16, \"PPP\": 0.349, \"cal_MAE\": 0.0068, \"delta_MAE\": 0.0087, \"raw_MAE\": 0.0155}, \"note\": \"Re-run with naming fix applied, now N=16 (was N=13 before fix). Confirms vanilla 2PL has lower calMAE on MMLU/ARC.\"}, \"status\": \"DONE\"}, \"exp_006_pooled_irt_2pl_gamma_n16\": {\"conclusion\": \"success\", \"metrics\": {\"ARC\": {\"CI_excludes_zero\": true, \"N\": 16, \"PPP\": 0.003, \"R_hat_max\": 1.01, \"cal_MAE\": 0.0201, \"delta_MAE\": 0.0136, \"gamma_hat\": 0.73}, \"GSM8K\": {\"CI_excludes_zero\": false, \"N\": 24, \"PPP\": 0.541, \"R_hat_max\": 1.01, \"cal_MAE\": 0.0062, \"delta_MAE\": 0.1632, \"gamma_hat\": 0.06}, \"MMLU\": {\"CI_excludes_zero\": false, \"N\": 16, \"PPP\": 0.193, \"R_hat_max\": 1.01, \"cal_MAE\": 0.0072, \"delta_MAE\": 0.0083, \"gamma_hat\": 0.7}, \"note\": \"N=16 fixed (naming normalization applied), 0 divergences, ESS>1300\"}, \"status\": \"DONE\"}, \"exp006_pooled_irt_n16_fixed\": {\"conclusion\": \"success\", \"status\": \"DONE\"}, \"exp_001_eval_05B_instruct\": {\"conclusion\": \"success\", \"status\": \"DONE\"}, \"exp_001_eval_llama32_3B_d000_s42\": {\"conclusion\": \"killed\", \"metrics\": {\"MMLU\": 0.4545}, \"status\": \"DONE\"}, \"exp_001_eval_15B_instruct\": {\"conclusion\": \"success\", \"metrics\": {\"ARC\": 0.7654, \"GSM8K\": 0.5929, \"MMLU\": 0.5775}, \"status\": \"DONE\"}, \"exp_006_mmlu_domain_gamma_n24_v4\": {\"conclusion\": \"success\", \"metrics\": {\"Business_Law_gamma\": \"not_significant\", \"CS_Eng_gamma\": \"not_significant\", \"Humanities_gamma\": \"negative_significant\", \"Medical_gamma\": \"negative_significant\", \"STEM_Math_gamma\": \"positive_significant\", \"STEM_Science_gamma\": \"positive_significant\", \"Social_Sciences_gamma\": \"negative_significant\", \"domains\": 7, \"note\": \"CmdStan crashed after results saved. Humanities rhat=1.014 not converged.\"}, \"status\": \"DONE\"}, \"exp_006_pooled_irt_rrf_n25_v2\": {\"conclusion\": \"success\", \"metrics\": {\"arc_N8_4PLgamma\": \"over_parameterized_cal_worsens\", \"gsm8k_N16_delta_mae\": 0.118, \"gsm8k_calibration\": \"effective\", \"mmlu_N8_4PLgamma\": \"over_parameterized_cal_worsens\", \"note\": \"GSM8K N=16 works. MMLU/ARC N=8 with 4PL+gamma over-parameterized, PPP=0.006/0.000, cal_mae > raw_mae. Need 2PL+gamma or N>=16.\"}, \"status\": \"DONE\"}, \"exp_003_rrf_full_n25_latest\": {\"conclusion\": \"success\", \"status\": \"DONE\"}, \"signals_05B_s123_v2\": {\"conclusion\": \"success\", \"status\": \"DONE\"}, \"exp_006_pooled_irt_n25\": {\"conclusion\": \"success\", \"status\": \"DONE\"}, \"exp_001_eval_3B_instruct_v2\": {\"conclusion\": \"success\", \"metrics\": {\"GSM8K\": 0.76, \"HumanEval\": 0.5, \"MMLU\": 0.605}, \"status\": \"DONE\"}, \"exp_006_mmlu_domain_gamma_n24_v3\": {\"conclusion\": \"failed\", \"metrics\": {\"Humanities\": {\"CI\": [-0.776, -0.041], \"N\": 21, \"PPP\": 1, \"converged\": \"borderline_rhat_1.014\", \"excludes_zero\": true, \"gamma_mean\": -0.407}, \"Medical\": {\"CI\": [-0.338, -0.06], \"N\": 24, \"PPP\": 1, \"converged\": true, \"excludes_zero\": true, \"gamma_mean\": -0.199}, \"STEM_CS_Eng\": {\"CI\": [-0.448, 0.835], \"N\": 23, \"PPP\": 0.892, \"converged\": true, \"excludes_zero\": false, \"gamma_mean\": 0.197}, \"STEM_Math\": {\"CI\": [0.527, 1.43], \"N\": 23, \"PPP\": 0.438, \"converged\": true, \"excludes_zero\": true, \"gamma_mean\": 0.969}, \"STEM_Science\": {\"CI\": [0.385, 1.274], \"N\": 23, \"PPP\": 0.807, \"converged\": true, \"excludes_zero\": true, \"gamma_mean\": 0.838}, \"completed_domains\": 5, \"crashed\": \"Social_Sciences (CmdStan retcode=[1,0,0,1])\", \"not_run\": [\"Business_Law\", \"Other\"], \"total_domains\": 8}, \"status\": \"DONE\"}, \"exp_002_signals_15B_d100_s123_cuda2\": {\"conclusion\": \"success\", \"status\": \"DONE\"}, \"exp_002_signals_15B_s123_batch\": {\"conclusion\": \"success\", \"status\": \"DONE\"}, \"exp_006_mmlu_domain_gamma_n24\": {\"conclusion\": \"success\", \"metrics\": {\"STEM_CS_Eng\": {\"N_items\": 557, \"N_models\": 23, \"PPP\": 0.892, \"fit_time_s\": 153, \"gamma_excludes_zero\": false, \"gamma_mean\": 0.197}, \"STEM_Math\": {\"N_items\": 1190, \"N_models\": 23, \"PPP\": 0.438, \"fit_time_s\": 527, \"gamma_excludes_zero\": true, \"gamma_mean\": 0.969}, \"STEM_Science\": {\"N_items\": 1397, \"N_models\": 23, \"PPP\": 0.807, \"fit_time_s\": 618, \"gamma_excludes_zero\": true, \"gamma_mean\": 0.838}, \"domains_completed\": 3, \"domains_total\": 8, \"note\": \"3/8 domains complete. Process stopped after 3 — remaining 5 need restart.\"}, \"status\": \"DONE\"}, \"exp_006_mmlu_domain_gamma_n24_v2\": {\"conclusion\": \"failed\", \"status\": \"DONE\"}, \"exp_001_sft_llama32_3B_d000_s42\": {\"conclusion\": \"success\", \"metrics\": {\"epoch\": 1, \"mean_token_accuracy\": 0.6685, \"train_loss\": 1.5165, \"train_runtime_sec\": 8170}, \"status\": \"DONE\"}, \"exp_002_signals_05B_s123_v2\": {\"conclusion\": \"success\", \"status\": \"DONE\"}, \"exp_001_sft_3B_d100_s123_a32\": {\"conclusion\": \"success\", \"status\": \"DONE\"}, \"exp_002_signals_3B_d100_a32_s42\": {\"conclusion\": \"success\", \"metrics\": {\"benchmarks_completed\": [\"mmlu\", \"gsm8k\", \"arc_challenge\"], \"signals_generated\": [\"s1_embedding\", \"s2_minkpp\", \"s4_selfcritique\"], \"status_note\": \"Signals validated via pooled IRT (exp_006_pooled_irt_all_scales, N=23 success). Analysis worker completed 2026-05-16T10:50:52 but callback not processed due to session reset.\"}, \"status\": \"DONE\"}, \"exp_006_pooled_irt_all_scales\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge\": {\"cal_mae\": 0.0153, \"delta_mae\": 0.0183, \"divergences\": 0, \"ess\": 1670, \"gamma_ci95\": [-0.2552, 1.2529], \"gamma_mean\": 0.4859, \"n_items\": 300, \"n_models\": 13, \"ppp\": 0.027, \"raw_mae\": 0.0335, \"rhat\": 1.0065}, \"exposure\": \"rrf_signal\", \"gsm8k\": {\"cal_mae\": 0.0078, \"delta_mae\": 0.1552, \"divergences\": 0, \"ess\": 1388, \"gamma_ci95\": [-0.2889, 0.637], \"gamma_mean\": 0.1721, \"n_items\": 300, \"n_models\": 20, \"ppp\": 0.3425, \"raw_mae\": 0.163, \"rhat\": 1.0071}, \"mmlu\": {\"cal_mae\": 0.0059, \"delta_mae\": 0.0098, \"divergences\": 0, \"ess\": 1402, \"gamma_ci95\": [-0.5501, 1.5974], \"gamma_mean\": 0.5172, \"n_items\": 300, \"n_models\": 15, \"ppp\": 0.2335, \"raw_mae\": 0.0157, \"rhat\": 1.0067}, \"model_type\": \"2pl_gamma\", \"rrf_respondents\": 23, \"scales\": [\"0.5B\", \"1.5B\", \"3B\"]}, \"status\": \"DONE\"}, \"exp_001_eval_3B_instruct_aligned_para\": {\"conclusion\": \"failed\", \"status\": \"DONE\"}, \"exp_002_signals_3B_d000_a32_s42\": {\"conclusion\": \"success\", \"metrics\": {\"benchmarks\": {\"arc_challenge\": {\"n_items\": 1172, \"signals\": [\"s1_embedding\", \"s2_minkpp\", \"s4_selfcritique\"]}, \"gsm8k\": {\"n_items\": 1319, \"signals\": [\"s1_embedding\", \"s2_minkpp\", \"s4_selfcritique\"]}, \"mmlu\": {\"n_items\": 14042, \"signals\": [\"s1_embedding\", \"s2_minkpp\", \"s4_selfcritique\"]}}, \"output_files\": {\"signal_s1_embedding_arc_challenge.json\": \"650K\", \"signal_s1_embedding_gsm8k.json\": \"717K\", \"signal_s1_embedding_mmlu.json\": \"7.6M\", \"signal_s2_minkpp_arc_challenge.json\": \"245K\", \"signal_s2_minkpp_gsm8k.json\": \"266K\", \"signal_s2_minkpp_mmlu.json\": \"2.8M\", \"signal_s4_selfcritique_arc_challenge.json\": \"284K\", \"signal_s4_selfcritique_gsm8k.json\": \"310K\", \"signal_s4_selfcritique_mmlu.json\": \"3.2M\"}, \"runtime_minutes\": 189, \"signals_completed\": 9, \"signals_failed\": 0}, \"status\": \"DONE\"}, \"exp_002_signals_3B_d005_a32_s42\": {\"conclusion\": \"success\", \"status\": \"DONE\"}, \"exp_006_pooled_irt_05b_15b\": {\"conclusion\": \"success\", \"metrics\": {\"arc_cal_mae\": 0.0682, \"arc_ci95\": \"[-0.271, 2.857]\", \"arc_delta_mae\": -0.064, \"arc_ess\": 1480, \"arc_gamma\": 1.2259, \"arc_n_models\": 5, \"arc_ppp\": 0, \"arc_raw_mae\": 0.0042, \"arc_rhat\": 1.0072, \"gsm8k_cal_mae\": 0.0373, \"gsm8k_ci95\": \"[-0.990, 1.019]\", \"gsm8k_delta_mae\": 0.1128, \"gsm8k_ess\": 1300, \"gsm8k_gamma\": 0.0128, \"gsm8k_n_models\": 11, \"gsm8k_ppp\": 0.663, \"gsm8k_raw_mae\": 0.1501, \"gsm8k_rhat\": 1.0072, \"n_items_subsampled\": 300}, \"status\": \"DONE\"}, \"exp006_pooled_rrf_irt_05b_15b\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge\": {\"cal_mae\": 0.0682, \"delta_mae\": -0.064, \"divergences\": 0, \"ess\": 1480, \"gamma_ci95\": [-0.2711, 2.8571], \"gamma_mean\": 1.2259, \"n_items\": 300, \"n_models\": 5, \"ppp\": 0, \"raw_mae\": 0.0042, \"rhat\": 1.0072}, \"gsm8k\": {\"cal_mae\": 0.0373, \"delta_mae\": 0.1128, \"divergences\": 0, \"ess\": 1300, \"gamma_ci95\": [-0.99, 1.0187], \"gamma_mean\": 0.0128, \"n_items\": 300, \"n_models\": 11, \"ppp\": 0.663, \"raw_mae\": 0.1501, \"rhat\": 1.0072}}, \"status\": \"DONE\"}, \"exp006_pooled_rrf_irt_05b_15b_v2\": {\"status\": \"PREPARING\"}, \"exp_006_mmlu_domain_gamma\": {\"conclusion\": \"success\", \"metrics\": {\"Business_Law_gamma\": 0.61, \"Humanities_gamma\": 0.47, \"Medical_gamma\": 0.27, \"Other_gamma\": 1.34, \"STEM_CS_Eng_gamma\": 0.29, \"STEM_Math_gamma\": -0.55, \"STEM_Science_gamma\": 0.36, \"Social_Sciences_gamma\": 0.28, \"all_rhat_max\": 1.008, \"divergent_transitions\": 0, \"n_domains\": 8, \"n_models\": 16}, \"status\": \"DONE\"}, \"exp_001_eval_3B_d005_s42_para_aligned\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge_acc\": 0.8164, \"arc_challenge_n\": 697, \"gsm8k_acc\": 0.3421, \"gsm8k_n\": 228, \"humaneval_n\": 26, \"humaneval_pass1\": 0.0769, \"mmlu_acc\": 0.6471, \"mmlu_n\": 6596}, \"status\": \"DONE\"}, \"exp_001_eval_3B_d000_s42_a32_para_aligned\": {\"conclusion\": \"success\", \"metrics\": {\"arc_para\": 0.8106, \"gsm8k_para\": 0.0526, \"humaneval_para\": 0.1923, \"mmlu_para\": 0.6431}, \"status\": \"DONE\"}, \"exp_001_eval_3B_d005_s42_a32_batch\": {\"conclusion\": \"success\", \"metrics\": {\"arc\": 0.8251, \"arc_para\": 0.8164, \"gsm8k\": 0.4147, \"gsm8k_para\": 0.3421, \"humaneval\": 0.1341, \"humaneval_para\": 0.0769, \"mmlu\": 0.6308, \"mmlu_para\": 0.6471}, \"status\": \"DONE\"}, \"exp_008_instruct_rl_proxy\": {\"conclusion\": \"failed\", \"metrics\": {\"base_pretrained_signals\": \"computing_PID_701898_GPU5\", \"comparison\": {\"arc\": {\"d000_sft_s2\": 1.7079, \"d000_sft_s4\": -0.9538, \"instruct_s2\": 1.6737, \"instruct_s4\": -0.9227, \"s4_delta_instruct_vs_sft\": 0.0311}, \"gsm8k\": {\"d000_sft_s2\": 1.6532, \"d000_sft_s4\": -0.9408, \"instruct_s2\": 1.7073, \"instruct_s4\": -0.9632, \"s4_delta_instruct_vs_sft\": -0.0224}, \"mmlu\": {\"base_s2\": 1.7009, \"base_s4\": \"computing\", \"d000_sft_s2\": 1.6976, \"d000_sft_s4\": -0.9557, \"instruct_s2\": 1.6952, \"instruct_s4\": -0.8782, \"s4_delta_instruct_vs_sft\": 0.0775}}, \"d000_sft_signals_complete\": true, \"instruct_signals_complete\": true, \"key_finding\": \"S4 differentiates regimes (MMLU +0.078, ARC +0.031 Instruct vs SFT); S2 does not (<0.01 difference). RL increases S4 entropy on knowledge benchmarks.\", \"signal_paths\": {\"base_pretrained\": \"/root/autodl-tmp/exp008/signals/base_pretrained/\", \"d000_sft\": \"/root/autodl-tmp/exp002/signals/Qwen2.5-0.5B_d000_s42/\", \"instruct\": \"/root/autodl-tmp/exp008/signals/rl_aligned/\"}}, \"status\": \"DONE\"}, \"exp_003_mmlu_item_aligned_gap\": {\"conclusion\": \"success\", \"metrics\": {\"aggregate\": {\"max_abs_gap_pp\": 3.73, \"mean_gap_pp\": -2.243, \"median_gap_pp\": -2.259, \"std_gap_pp\": 0.671}, \"alignment_correction\": {\"conclusion\": \"Proper item-ID alignment changes result by <0.3pp vs naive positional comparison\", \"misaligned_vs_aligned_diff_pp\": \"<0.3 (confirmed from prior 2-pair check)\"}, \"by_contamination\": {\"d000\": {\"mean_pp\": -2.292, \"n\": 5}, \"d005\": {\"mean_pp\": -2.181, \"n\": 6}, \"d025\": {\"mean_pp\": -1.913, \"n\": 5}, \"d100\": {\"mean_pp\": -2.687, \"n\": 4}}, \"by_size\": {\"0.5B\": {\"mean_pp\": -2.259, \"n\": 4, \"std_pp\": 1.238}, \"1.5B\": {\"mean_pp\": -2.452, \"n\": 8, \"std_pp\": 0.31}, \"3B\": {\"mean_pp\": -2.026, \"n\": 8, \"std_pp\": 0.415}}, \"n_common_items\": 6596, \"n_pairs\": 20, \"per_item\": {\"mean_disagree_rate_pct\": 15.5, \"n_flagged_items\": 426, \"pct_aligned_easier\": 6.6, \"pct_high_disagree_gt50\": 6.5, \"pct_neutral_lt03pp\": 84.8, \"pct_para_easier\": 8.6}, \"prior_2pair_check\": {\"15B_d100\": {\"aligned_gap_pp\": -2.9, \"qc_selection_bias_pp\": 0.56}, \"3B_d100\": {\"aligned_gap_pp\": -3.5, \"qc_selection_bias_pp\": -0.08}}}, \"status\": \"DONE\"}, \"exp_001_eval_3B_d025_s42_a32_para\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge_para\": 0.8106, \"gsm8k_para\": \"completed\", \"humaneval_para\": 0, \"mmlu_para\": \"completed_6596_items\", \"output_dir\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d025_v3_s42_para_aligned\", \"sentinel\": \".done exists\"}, \"status\": \"DONE\"}, \"exp_002_signals_3B_d025_v3_s42\": {\"conclusion\": \"success\", \"status\": \"DONE\"}, \"exp_002_signals_3B_v9\": {\"conclusion\": \"failed\", \"status\": \"DONE\"}, \"exp_001_sft_3B_d025_s42_a32_v3\": {\"conclusion\": \"killed\", \"status\": \"DONE\"}, \"exp_001_eval_3B_d025_v3_s42_batch\": {\"conclusion\": \"killed\", \"status\": \"DONE\"}, \"exp_002_signals_05B_s123_batch\": {\"conclusion\": \"failed\", \"status\": \"DONE\"}, \"exp_002_signals_3B_v7\": {\"conclusion\": \"success\", \"metrics\": {\"benchmarks\": [\"mmlu\", \"gsm8k\", \"arc_challenge\"], \"merged_files\": 3, \"output_dir\": \"/root/autodl-tmp/exp002/signals/Qwen2.5-3B_d005_s123/\", \"signal_files\": 9, \"signals\": [\"s1_embedding\", \"s2_minkpp\", \"s4_selfcritique\"]}, \"status\": \"DONE\"}, \"exp_001_sft_3B_d100_s42_a32_v3\": {\"conclusion\": \"success\", \"metrics\": {\"entropy\": 1.296, \"final_epoch\": 1, \"mean_token_accuracy\": 0.7186, \"total_steps\": 4159, \"train_loss\": 1.1795, \"train_runtime_sec\": 17645, \"train_samples_per_second\": 3.771, \"train_steps_per_second\": 0.236}, \"status\": \"DONE\"}, \"exp_001_sft_3B_d005_s42_a32\": {\"conclusion\": \"success\", \"metrics\": {\"epoch\": 1, \"final_loss\": 1.0822, \"mean_token_accuracy\": 0.7511, \"steps\": 3177, \"train_runtime_sec\": 14913.5}, \"status\": \"DONE\"}, \"exp_002_signals_3B_v8_recovery\": {\"conclusion\": \"failed\", \"status\": \"DONE\"}, \"exp_004_sim_sweep_v7\": {\"conclusion\": \"success\", \"metrics\": {\"ci95_coverage_range\": \"[0.8, 1.0]\", \"conditions_failed\": \"auc0.65_n20/n50/n100 (CmdStan TMPDIR race)\", \"conditions_ok\": 9, \"conditions_total\": 12, \"gamma_bias_range\": \"[-0.025, +0.056]\", \"gamma_rmse_range\": \"[0.005, 0.085]\", \"note\": \"9/12 sufficient for Claim 1 identifiability\", \"theta_corr_range\": \"[0.947, 0.972]\"}, \"status\": \"DONE\"}, \"exp_001_eval_3B_d000_s42_a32_aligned\": {\"status\": \"PREPARING\"}, \"exp_001_sft_3B_d000_s42_a32\": {\"conclusion\": \"success\", \"metrics\": {\"epoch\": 1, \"final_loss\": 1.1324, \"steps\": 3125}, \"status\": \"DONE\"}, \"exp_002_signals_3B_v8\": {\"conclusion\": \"failed\", \"status\": \"DONE\"}, \"exp_002_signals_3B_v5\": {\"conclusion\": \"failed\", \"status\": \"DONE\"}, \"exp_001_sft_3B_d025_s42_a32_v2\": {\"conclusion\": \"failed\", \"status\": \"DONE\"}, \"exp_001_eval_15B_s123_para_aligned_batch\": {\"conclusion\": \"success\", \"metrics\": {\"d000_s123_para_aligned\": {\"arc_challenge\": 0.7547, \"gsm8k\": 0.5921, \"humaneval\": 0.1538, \"mmlu\": 0.6111}, \"d005_s123_para_aligned\": {\"arc_challenge\": 0.7475, \"gsm8k\": 0.5439, \"humaneval\": 0.0769, \"mmlu\": 0.614}, \"d025_s123_para_aligned\": {\"arc_challenge\": 0.7504, \"gsm8k\": 0.5482, \"humaneval\": 0.1923, \"mmlu\": 0.6145}, \"d100_s123_para_aligned\": {\"arc_challenge\": 0.7834, \"gsm8k\": 0.5307, \"humaneval\": 0.2308, \"mmlu\": 0.629}}, \"status\": \"DONE\"}, \"exp_001_sft_3B_d100_s42_a32_v2\": {\"conclusion\": \"failed\", \"status\": \"DONE\"}, \"exp_001_sft_3B_d025_s42_a32\": {\"conclusion\": \"killed\", \"status\": \"DONE\"}, \"exp_001_sft_3B_d100_s42_a32\": {\"conclusion\": \"killed\", \"status\": \"DONE\"}, \"exp_001_sft_d025_3B_v3\": {\"conclusion\": \"success\", \"metrics\": {\"entropy\": 1.1807, \"epoch\": 1, \"mean_token_accuracy\": 0.734, \"total_steps\": 3384, \"train_loss\": 1.1464, \"train_runtime_s\": 14584}, \"status\": \"DONE\"}, \"exp_002_signals_3B_v6\": {\"conclusion\": \"failed\", \"status\": \"DONE\"}, \"exp_001_sft_d005_3B\": {\"conclusion\": \"success\", \"metrics\": {\"epochs\": 1, \"final_loss\": 1.11, \"total_steps\": 3177, \"training_hours\": 3.76}, \"status\": \"DONE\"}, \"exp_002_signals_3B_v4\": {\"conclusion\": \"failed\", \"status\": \"DONE\"}, \"exp_004_sim_sweep_extreme_gamma\": {\"conclusion\": \"success\", \"metrics\": {\"conditions\": 8, \"gamma2_avg_bias\": 0.017, \"gamma2_avg_rmse\": 0.101, \"gamma2_ci95_coverage\": 1, \"gamma4_avg_bias\": -0.106, \"gamma4_avg_rmse\": 0.226, \"gamma4_ci95_coverage\": 0.925, \"seeds_per_condition\": 10, \"theta_corr_range\": [0.914, 0.969], \"total_time_hours\": 11.1}, \"status\": \"DONE\"}, \"exp_001_eval_3B_d100_s123_para_aligned_v2\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge\": {\"accuracy\": 0.8164, \"correct\": 569, \"total\": 697}, \"gsm8k\": {\"accuracy\": 0.5877, \"correct\": 134, \"total\": 228}, \"humaneval\": {\"correct\": 2, \"pass@1\": 0.0769, \"total\": 26}, \"mmlu\": {\"accuracy\": 0.6565, \"correct\": 4330, \"total\": 6596}}, \"status\": \"DONE\"}, \"exp_001_eval_3B_d100_s123_para_aligned\": {\"conclusion\": \"failed\", \"status\": \"DONE\"}, \"exp_001_sft_3B_d000_v3\": {\"conclusion\": \"failed\", \"status\": \"DONE\"}, \"exp_004_sim_sweep_v6\": {\"conclusion\": \"killed\", \"status\": \"DONE\"}, \"exp_002_signals_3B_v3\": {\"conclusion\": \"killed\", \"status\": \"DONE\"}, \"exp_001_eval_3B_d005_s123_aligned\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge_accuracy\": 0.8242, \"gsm8k_exact_match\": 0.6308, \"humaneval_pass1\": 0.1037, \"mmlu_accuracy\": 0.6324}, \"status\": \"DONE\"}, \"exp_001_eval_3B_d025_s123_aligned\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge\": 0.8336, \"gsm8k\": 0.5254, \"humaneval\": 0.1585, \"mmlu\": 0.6367}, \"status\": \"DONE\"}, \"exp_002_signals_3B_v2\": {\"conclusion\": \"killed\", \"status\": \"DONE\"}, \"exp_001_eval_3B_d005_s123_para_aligned\": {\"conclusion\": \"success\", \"metrics\": {\"ARC\": 0.8192, \"GSM8K\": 0.5, \"HumanEval\": 0.0769, \"MMLU\": 0.6461}, \"status\": \"DONE\"}, \"exp_001_eval_15B_d005_s123\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge\": {\"accuracy\": 0.7568, \"correct\": 887, \"total\": 1172}, \"gsm8k\": {\"correct\": 855, \"exact_match\": 0.6482, \"total\": 1319}, \"humaneval\": {\"correct\": 41, \"pass@1\": 0.25, \"total\": 164}, \"mmlu\": {\"accuracy\": 0.5869, \"correct\": 8241, \"total\": 14042}}, \"status\": \"DONE\"}, \"exp_001_eval_15B_d005_s123_v2\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge\": {\"accuracy\": 0.7568, \"correct\": 887, \"total\": 1172}, \"gsm8k\": {\"correct\": 855, \"exact_match\": 0.6482, \"total\": 1319}, \"humaneval\": {\"correct\": 41, \"pass@1\": 0.25, \"total\": 164}, \"mmlu\": {\"accuracy\": 0.5869, \"correct\": 8241, \"total\": 14042}}, \"status\": \"DONE\"}, \"exp_001_eval_15B_d025_s123\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge\": {\"accuracy\": 0.7577, \"correct\": 888, \"total\": 1172}, \"gsm8k\": {\"correct\": 864, \"exact_match\": 0.655, \"total\": 1319}, \"humaneval\": {\"correct\": 41, \"pass@1\": 0.25, \"total\": 164}, \"mmlu\": {\"accuracy\": 0.5881, \"correct\": 8258, \"total\": 14042}}, \"status\": \"DONE\"}, \"exp_001_eval_15B_d025_s123_v2\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge\": {\"accuracy\": 0.7577, \"correct\": 888, \"total\": 1172}, \"gsm8k\": {\"correct\": 864, \"exact_match\": 0.655, \"total\": 1319}, \"humaneval\": {\"correct\": 41, \"pass@1\": 0.25, \"total\": 164}, \"mmlu\": {\"accuracy\": 0.5881, \"correct\": 8258, \"total\": 14042}}, \"status\": \"DONE\"}, \"exp_001_sft_d025_3B_v2\": {\"conclusion\": \"success\", \"metrics\": {\"epochs\": 1, \"mean_token_accuracy\": 0.7342, \"runtime_seconds\": 14499, \"steps\": 3384, \"train_loss\": 1.1501}, \"status\": \"DONE\"}, \"exp_001_sft_d100_3B_v2\": {\"conclusion\": \"success\", \"metrics\": {\"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d100_s42/lora_adapter\", \"d020_params\": \"lr=5e-5, alpha=16, r=16\", \"status\": \"training_complete\", \"steps\": \"4159/4159\"}, \"status\": \"DONE\"}, \"exp_001_sft_3B_d000_v2\": {\"conclusion\": \"success\", \"metrics\": {\"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_v2_s42/lora_adapter\", \"completed_at\": \"2026-05-15T03:45Z\", \"status\": \"training_complete\"}, \"status\": \"DONE\"}, \"exp_002_signals_3B\": {\"conclusion\": \"failed\", \"status\": \"DONE\"}, \"exp_001_eval_3B_d000_s42_para_aligned\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge\": {\"accuracy\": 0.8235, \"correct\": 574, \"total\": 697}, \"gsm8k\": {\"accuracy\": 0.0482, \"correct\": 11, \"total\": 228}, \"humaneval\": {\"correct\": 3, \"pass@1\": 0.1154, \"total\": 26}, \"mmlu\": {\"accuracy\": 0.6474, \"correct\": 4270, \"total\": 6596}}, \"status\": \"DONE\"}, \"exp_001_eval_3B_d100_s42_para_aligned\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge\": {\"accuracy\": 0.8092, \"correct\": 564, \"total\": 697}, \"gsm8k\": {\"accuracy\": 0.5833, \"correct\": 133, \"total\": 228}, \"humaneval\": {\"correct\": 3, \"pass@1\": 0.1154, \"total\": 26}, \"mmlu\": {\"accuracy\": 0.659, \"correct\": 4347, \"total\": 6596}}, \"status\": \"DONE\"}, \"exp_001_sft_3B_d005_s123\": {\"conclusion\": \"success\", \"metrics\": {\"final_loss\": 1.1349, \"final_token_accuracy\": 0.7069, \"total_steps\": 3177}, \"status\": \"DONE\"}, \"exp_001_sft_3B_d025_s123\": {\"conclusion\": \"success\", \"metrics\": {\"final_loss\": 1.1401, \"final_token_accuracy\": 0.734, \"total_steps\": 3384}, \"status\": \"DONE\"}, \"exp_001_eval_3B_d000_s123_aligned\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge\": 0.8328, \"gsm8k\": 0.1812, \"humaneval\": 0.0854, \"mmlu\": 0.6332}, \"status\": \"DONE\"}, \"exp_001_eval_3B_d005_s42_aligned\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge\": 0.8294, \"gsm8k\": 0.2077, \"humaneval\": 0.1463, \"mmlu\": 0.6345}, \"status\": \"DONE\"}, \"exp_008_base_pretrained_eval_v2\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge\": 0.2278, \"gsm8k\": 0.163, \"humaneval\": 0, \"mmlu\": 0.2294}, \"status\": \"DONE\"}, \"exp_001_sft_15B_d025_s123_v2\": {\"conclusion\": \"success\", \"metrics\": {\"mean_token_accuracy\": 0.7466, \"train_loss\": 1.2723}, \"status\": \"DONE\"}, \"exp_001_sft_15B_d005_s123_v2\": {\"conclusion\": \"success\", \"metrics\": {\"mean_token_accuracy\": 0.6855, \"train_loss\": 1.2639}, \"status\": \"DONE\"}, \"exp_008_base_pretrained_15B_eval_v2\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge\": 0.2304, \"arc_correct\": 270, \"arc_total\": 1172, \"gsm8k\": 0.0053, \"gsm8k_correct\": 7, \"gsm8k_total\": 1319, \"humaneval_correct\": 38, \"humaneval_pass1\": 0.2317, \"humaneval_total\": 164, \"mmlu\": 0.2303, \"mmlu_correct\": 3234, \"mmlu_total\": 14042}, \"status\": \"DONE\"}, \"exp_008_base_pretrained_15B_eval\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge_accuracy\": 0.2304, \"arc_correct\": 270, \"arc_total\": 1172, \"gsm8k_accuracy\": 0.0053, \"gsm8k_correct\": 7, \"gsm8k_total\": 1319, \"humaneval_correct\": 38, \"humaneval_pass@1\": 0.2317, \"humaneval_total\": 164, \"mmlu_accuracy\": 0.2303, \"mmlu_correct\": 3234, \"mmlu_total\": 14042}, \"status\": \"DONE\"}, \"exp_008_base_pretrained_eval\": {\"conclusion\": \"failed\", \"status\": \"DONE\"}, \"exp_001_eval_15B_d000_s123_aligned\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge_accuracy\": 0.7577, \"gsm8k_accuracy\": 0.6535, \"humaneval_pass@1\": 0.1707, \"mmlu_accuracy\": 0.5855}, \"status\": \"DONE\"}, \"exp_001_eval_15B_d100_s123_aligned\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge_accuracy\": 0.7816, \"gsm8k_accuracy\": 0.6444, \"humaneval_pass@1\": 0.2805, \"mmlu_accuracy\": 0.5956}, \"status\": \"DONE\"}, \"exp_001_eval_05B_d000_s123_aligned\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge\": 0.4974, \"gsm8k\": 0.3412, \"humaneval\": 0.1037, \"mmlu\": 0.4216}, \"status\": \"DONE\"}, \"exp_001_eval_3B_d000_s42_v3\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge\": 0.8276, \"gsm8k\": 0.1198, \"humaneval\": 0.1159, \"mmlu\": 0.634}, \"status\": \"DONE\"}, \"exp006-s1only-gsm8k-2pl\": {\"conclusion\": \"success\", \"metrics\": {\"ci_excludes_zero\": false, \"divergent_count\": 0, \"gamma_ci95\": [-0.306, 0.591], \"gamma_mean\": 0.1389, \"gamma_sd\": 0.2274, \"max_rhat\": 1.0024, \"min_ess\": 3604.4, \"obs_mean_acc\": 0.5086, \"ppp\": 0.2835, \"pred_mean_acc\": 0.5011, \"residual_mae\": 0.0083}, \"status\": \"DONE\"}, \"exp_001_eval_3B_d000_v2_s123_aligned\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge\": 0.8259, \"gsm8k\": 0.2676, \"humaneval\": 0.061, \"mmlu\": 0.6314}, \"status\": \"DONE\"}, \"exp_001_eval_3B_d025_v2_aligned\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge\": 0.8276, \"gsm8k\": 0.6793, \"humaneval\": 0.0976, \"mmlu\": 0.5998}, \"status\": \"DONE\"}, \"exp_001_eval_3B_d100_v2_s123_aligned\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge\": 0.8311, \"gsm8k\": 0.7324, \"humaneval\": 0.1829, \"mmlu\": 0.6319}, \"status\": \"DONE\"}, \"exp_001_sft_15B_d005_s123\": {\"conclusion\": \"failed\", \"status\": \"DONE\"}, \"exp_001_eval_05B_d025_s123_aligned\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge\": {\"accuracy\": 0.4061, \"correct\": 476, \"total\": 1172}, \"gsm8k\": {\"accuracy\": 0.3533, \"correct\": 466, \"total\": 1319}, \"humaneval\": {\"correct\": 14, \"pass@1\": 0.0854, \"total\": 164}, \"mmlu\": {\"accuracy\": 0.3473, \"correct\": 4877, \"total\": 14042}}, \"status\": \"DONE\"}, \"exp_001_sft_05B_d025_s123_v2\": {\"conclusion\": \"success\", \"metrics\": {\"accuracy\": 0.697, \"epoch\": 1, \"global_steps\": 3384, \"runtime_seconds\": 5930, \"train_loss\": 1.548}, \"status\": \"DONE\"}, \"exp_001_eval_05B_d000_s42_v7\": {\"conclusion\": \"failed\", \"status\": \"DONE\"}, \"exp_004_sim_sweep_v5\": {\"conclusion\": \"failed\", \"metrics\": {\"conditions_all_failed\": [\"auc0.65_n20 (0/10)\", \"auc0.65_n50 (0/7)\"], \"conditions_complete\": 4, \"conditions_fully_ok\": [\"auc0.55_n20 (10/10)\", \"auc0.55_n50 (10/10)\", \"auc0.8_n20 (10/10)\", \"auc0.8_n50 (10/10)\"], \"conditions_missing\": 3, \"conditions_never_started\": [\"auc0.65_n100\", \"auc0.9_n50\", \"auc0.9_n100\"], \"conditions_partial\": 5, \"conditions_partial_ok\": [\"auc0.55_n100 (7/10)\", \"auc0.8_n100 (6/10)\", \"auc0.9_n20 (6/10)\"], \"failure_cause\": \"Disk quota exceeded ([Errno 122]) - root partition /tmp filled by CmdStan temp files\", \"seeds_attempted\": 97, \"seeds_ok\": 59, \"seeds_total\": 120}, \"status\": \"DONE\"}, \"exp006-oracle-arc-4pl-pooled\": {\"conclusion\": \"failed\", \"status\": \"DONE\"}, \"exp_008_instruct_05B_eval\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge_accuracy\": 0.2816, \"gsm8k_accuracy\": 0.3882, \"humaneval_pass@1\": 0, \"mmlu_accuracy\": 0.2462}, \"status\": \"DONE\"}, \"exp_001_eval_3B_d100_v2_aligned_v2\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge_accuracy\": 0.8242, \"gsm8k_accuracy\": 0.7415, \"humaneval_pass@1\": 0.1707, \"mmlu_accuracy\": 0.632}, \"status\": \"DONE\"}, \"exp_001_eval_3B_d025_v2_para_aligned\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge_para_accuracy\": 0.8106, \"gsm8k_para_accuracy\": 0.5482, \"humaneval_para_pass@1\": 0.1154, \"mmlu_para_accuracy\": 0.621}, \"status\": \"DONE\"}, \"exp_001_sft_3B_d100_s123\": {\"conclusion\": \"success\", \"metrics\": {\"epochs\": 1, \"mean_token_accuracy\": 0.7343, \"runtime_seconds\": 18252, \"steps\": 4159, \"train_loss\": 1.1846}, \"status\": \"DONE\"}, \"exp006-oracle-arc-2pl\": {\"conclusion\": \"success\", \"metrics\": {\"C95_coverage\": 0.1818, \"ESS\": 1512, \"MAE\": 0.0759, \"gamma\": -0.618, \"gamma_ci\": [-1.04, -0.2], \"rhat\": 1.006}, \"status\": \"DONE\"}, \"exp_001_eval_3B_d000_v2_s123_para_aligned\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge_para_accuracy\": 0.8121, \"gsm8k_para_accuracy\": 0.1491, \"humaneval_para_pass@1\": 0.0385, \"mmlu_para_accuracy\": 0.6512}, \"status\": \"DONE\"}, \"exp006-pooled-s1only-gsm8k-v2\": {\"conclusion\": \"success\", \"metrics\": {\"diagnostics_ok\": false, \"divergent_pct\": 0, \"ess_min\": 330.2, \"fit_time_sec\": 336.9, \"gamma\": 0.1871, \"gamma_ci_excludes_zero\": false, \"gamma_ci_lower\": -0.9172, \"gamma_ci_upper\": 1.3294, \"gamma_sd\": 0.5687, \"n_items\": 1319, \"n_models\": 8, \"note\": \"No evaluation/baselines files generated; only IRT fit available. rhat and ESS did not pass thresholds.\", \"ppp\": 0.336, \"residual_mae\": 0.0367, \"rhat_max\": 1.0148}, \"status\": \"DONE\"}, \"exp006-pooled-s1only-arc\": {\"conclusion\": \"success\", \"metrics\": {\"baselines\": {\"B0_raw_mae\": 0.0588, \"B1_remove_rescore_mae\": 0.0588, \"B2_2pl_gamma_mae\": 0.064, \"B3_vanilla_4pl_mae\": 0.0706, \"B4_linear_regression_mae\": 0.0562, \"B5_emperor_mae\": 0.0588, \"B6_dcr_fuzzy_mae\": 0.2454}, \"brier\": 0.0018, \"coverage_50\": 0, \"coverage_80\": 0.25, \"coverage_95\": 0.625, \"divergent_pct\": 0, \"ece\": 0.0319, \"ess_min\": 769.6, \"fit_time_sec\": 317.7, \"gamma\": -1.4637, \"gamma_ci_excludes_zero\": true, \"gamma_ci_lower\": -2.51, \"gamma_ci_upper\": -0.4051, \"gamma_sd\": 0.5276, \"kendall_tau\": 0.7559, \"mae\": 0.0347, \"n_items\": 1172, \"n_models\": 8, \"ppp\": 0.9677, \"rhat_max\": 1.0098, \"sharpness_95\": 0.0684}, \"status\": \"DONE\"}, \"exp006-oracle-gsm8k-extended-v2\": {\"conclusion\": \"success\", \"metrics\": {\"baselines\": {\"B0_raw_mae\": 0.005, \"B4_linear_regression_mae\": 0.008, \"B5_emperor_mae\": 0.005, \"B6_dcr_fuzzy_mae\": 0.138}, \"coverage_50\": 0.25, \"coverage_80\": 0.25, \"coverage_95\": 0.31, \"divergent_pct\": 0, \"ece\": 0.0894, \"ess_min\": 1221.9, \"fit_time_sec\": 6240.3, \"gamma\": 3.773, \"gamma_ci_excludes_zero\": true, \"gamma_ci_lower\": 2.741, \"gamma_ci_upper\": 4.714, \"gamma_sd\": 0.504, \"kendall_tau\": 0.505, \"mae\": 0.0917, \"n_items\": 1319, \"n_models\": 16, \"ppp\": 0, \"rhat_max\": 1.002}, \"status\": \"DONE\"}, \"exp_001_sft_05B_d025_s123\": {\"conclusion\": \"killed\", \"status\": \"DONE\"}, \"exp_001_eval_05B_d005_s123_para_aligned\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge_para_accuracy\": 0.2912, \"gsm8k_para_accuracy\": 0.2939, \"humaneval_para_pass@1\": 0, \"mmlu_para_accuracy\": 0.3166}, \"status\": \"DONE\"}, \"exp_001_eval_05B_d000_s42\": {\"conclusion\": \"failed\", \"status\": \"DONE\"}, \"exp_001_eval_05B_d005_s123_aligned\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge_accuracy\": 0.2978, \"gsm8k_accuracy\": 0.3677, \"humaneval_pass@1\": 0.0976, \"mmlu_accuracy\": 0.3002}, \"status\": \"DONE\"}, \"exp_004_sim_sweep_v4\": {\"conclusion\": \"failed\", \"status\": \"DONE\"}, \"exp_001_sft_3B_d000_s123\": {\"conclusion\": \"success\", \"metrics\": {\"baseline_seed42_train_loss\": 1.1357, \"entropy\": 1.1108, \"epochs\": 1, \"mean_token_accuracy\": 0.748, \"steps\": 3125, \"train_loss\": 1.1361, \"train_runtime_seconds\": 13141.8}, \"status\": \"DONE\"}, \"exp_001_eval_3B_d000_v2_para_aligned_v3\": {\"conclusion\": \"failed\", \"status\": \"DONE\"}, \"exp_001_eval_3B_d000_v2_para_aligned_v2\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge_para_accuracy\": 0.8121, \"gsm8k_para_accuracy\": 0.2895, \"humaneval_para_pass@1\": 0.0385, \"mmlu_para_accuracy\": 0.6468}, \"status\": \"DONE\"}, \"exp006-oracle-gsm8k-extended\": {\"conclusion\": \"failed\", \"status\": \"DONE\"}, \"exp006-pooled-s1only-gsm8k\": {\"conclusion\": \"failed\", \"status\": \"DONE\"}, \"exp_001_eval_3B_d100_v2_para_aligned\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge_para\": 0.8092, \"gsm8k_para\": 0.5833, \"humaneval_para_pass1\": 0.1154, \"mmlu_para\": 0.659}, \"status\": \"DONE\"}, \"exp_001_sft_05B_d005_s123\": {\"conclusion\": \"success\", \"metrics\": {\"epoch\": 1, \"final_loss\": 1.4542, \"final_token_accuracy\": 0.6794, \"mean_token_accuracy\": 0.6356, \"total_steps\": 3177, \"train_loss\": 1.5422, \"train_runtime_sec\": 3458.58}, \"status\": \"DONE\"}, \"exp_001_eval_3B_d000_v2_aligned\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge\": 0.8183, \"gsm8k\": 0.3525, \"humaneval_pass@1\": 0.0976, \"mmlu\": 0.6295}, \"status\": \"DONE\"}, \"exp_001_sft_15B_d100_s123\": {\"conclusion\": \"success\", \"metrics\": {\"baseline_seed42_token_accuracy\": 0.7033, \"baseline_seed42_train_loss\": 1.2996, \"entropy\": 1.3327, \"epochs\": 1, \"mean_token_accuracy\": 0.7178, \"num_tokens\": 21575068, \"steps\": 4159, \"train_loss\": 1.3002, \"train_runtime_seconds\": 14663.6}, \"status\": \"DONE\"}, \"exp_004_sim_sweep_v3\": {\"conclusion\": \"failed\", \"status\": \"DONE\"}, \"exp_001_eval_3B_d100_v2_aligned\": {\"conclusion\": \"failed\", \"metrics\": {\"INVALID\": \"metrics were from v1 exp_001_eval_3B_d100_aligned, not v2. v2 output dir was empty. PID 461879 died before completion.\"}, \"status\": \"DONE\"}, \"exp_001_sft_d025_3B\": {\"conclusion\": \"failed\", \"status\": \"DONE\"}, \"exp_001_eval_05B_d100_s123_aligned\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge_accuracy\": 0.3669, \"arc_challenge_correct\": 430, \"arc_challenge_total\": 1172, \"gsm8k_accuracy\": 0.3798, \"gsm8k_correct\": 501, \"gsm8k_total\": 1319, \"humaneval_pass_at_1\": 0.1037, \"humaneval_total\": 164, \"mmlu_accuracy\": 0.3058, \"mmlu_correct\": 4294, \"mmlu_total\": 14042}, \"status\": \"DONE\"}, \"exp_001_eval_3B_d000_v2_para_aligned\": {\"conclusion\": \"success\", \"metrics\": {\"format\": \"paraphrased_aligned\", \"mmlu_para\": 0.6468}, \"status\": \"DONE\"}, \"exp006-pooled-05B-15B-mmlu-v2\": {\"conclusion\": \"failed\", \"metrics\": {\"NOTE\": \"fit completely failed, not reportable\", \"convergence\": \"FAILED (rhat=1.54, ess=7)\", \"coverage_95\": 1, \"exposure_source\": \"signal_rrf\", \"gamma_joint\": -0.2095, \"gamma_joint_ci\": [-1.01, 0.59], \"gamma_perbench\": -3.8073, \"gamma_perbench_ci\": [-7.02, 3.22], \"mae\": 0.099, \"n_models\": 8, \"ppp\": 0.75}, \"status\": \"DONE\"}, \"exp006-pooled-05B-15B-arc-v2\": {\"conclusion\": \"success\", \"metrics\": {\"NOTE\": \"coverage below 95%; no oracle baseline exists\", \"convergence\": \"OK\", \"coverage_95\": 0.625, \"exposure_source\": \"signal_rrf\", \"gamma_joint\": -1.4637, \"gamma_joint_ci\": [-2.51, -0.41], \"gamma_perbench\": -2.3471, \"gamma_perbench_ci\": [-3.46, -1.19], \"mae\": 0.035, \"n_models\": 8, \"ppp\": 0.999}, \"status\": \"DONE\"}, \"exp_005_noise_prop\": {\"conclusion\": \"failed\", \"status\": \"DONE\"}, \"exp_004_sim_sweep\": {\"conclusion\": \"failed\", \"status\": \"DONE\"}, \"exp002-signals-1p5B\": {\"conclusion\": \"success\", \"status\": \"DONE\"}, \"exp_004_sim_sweep_v2\": {\"conclusion\": \"failed\", \"metrics\": {\"auc080_n100_bias\": 0.008, \"auc080_n100_ci_width\": 0.116, \"auc080_n100_gamma_hat\": 0.508, \"auc080_n100_theta_corr\": 0.962, \"auc080_n50_bias\": 0.006, \"auc080_n50_ci95_coverage\": 1, \"auc080_n50_rmse\": 0.03, \"ci_width_ratio_n100\": 1.81, \"core_findings_stable\": true, \"runs_completed\": 48, \"runs_total\": 120}, \"status\": \"DONE\"}, \"exp_005_noise_prop_v3\": {\"conclusion\": \"failed\", \"status\": \"DONE\"}, \"exp_001_sft_05B_d100_s123\": {\"conclusion\": \"success\", \"status\": \"DONE\"}, \"exp002-signal-d025-05B\": {\"conclusion\": \"success\", \"status\": \"DONE\"}, \"exp_001_eval_05B_d025_aligned_v2\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge\": 0.3199, \"format\": \"paraphrased_aligned\", \"gsm8k\": 0.3114, \"humaneval_pass1\": 0.1923, \"mmlu\": 0.2835}, \"status\": \"DONE\"}, \"exp_006_irt_05B_arc\": {\"conclusion\": \"success\", \"metrics\": {\"fit_type\": \"joint\", \"gamma\": -1.21, \"gamma_ci_lower\": -2.53, \"gamma_ci_upper\": 0.12}, \"status\": \"DONE\"}, \"exp_001_eval_15B_d025_aligned\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge\": 0.7688, \"gsm8k\": 0.6535, \"humaneval_pass1\": 0.2256, \"mmlu\": 0.5902}, \"status\": \"DONE\"}, \"exp_001_eval_05B_d005_para_aligned\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge\": 0.33, \"arc_correct\": 230, \"arc_total\": 697, \"gsm8k\": 0.2588, \"gsm8k_correct\": 59, \"gsm8k_total\": 228, \"humaneval\": 0, \"humaneval_correct\": 0, \"humaneval_total\": 26, \"mmlu\": 0.3548, \"mmlu_correct\": 2340, \"mmlu_total\": 6596}, \"status\": \"DONE\"}, \"exp_001_eval_15B_d025_para_aligned\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge\": 0.766, \"gsm8k\": 0.539, \"humaneval\": 0.154, \"mmlu\": 0.618}, \"status\": \"DONE\"}, \"exp_001_eval_3B_d100_para_aligned\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge\": 0.828, \"gsm8k\": 0.614, \"mmlu\": 0.676}, \"status\": \"DONE\"}, \"exp_006_pooled_gsm8k_v1\": {\"conclusion\": \"failed\", \"status\": \"DONE\"}, \"exp_001_eval_15B_aligned_batch\": {\"conclusion\": \"success\", \"metrics\": {\"arc\": {\"d000_orig\": 0.7722, \"d000_para\": 0.7547, \"d005_orig\": 0.7688, \"d005_para\": 0.7532, \"d100_orig\": 0.7688, \"d100_para\": 0.7661}, \"gsm8k\": {\"d000_orig\": 0.6543, \"d000_para\": 0.557, \"d005_orig\": 0.6482, \"d005_para\": 0.5439, \"d100_orig\": 0.6497, \"d100_para\": 0.5526}, \"humaneval\": {\"d000_orig\": 0.128, \"d000_para\": 0.0385, \"d005_orig\": 0.25, \"d005_para\": 0.1923, \"d100_orig\": 0.3049, \"d100_para\": 0.2692}, \"key_finding\": \"MC benchmarks fail to detect contamination at 1.5B scale (<1pp). HumanEval shows strong dose-response (+17.69pp). Paraphrase gap does not cleanly separate contamination.\", \"mmlu\": {\"d000_orig\": 0.5853, \"d000_para\": 0.6096, \"d005_orig\": 0.5852, \"d005_para\": 0.6164, \"d100_orig\": 0.5933, \"d100_para\": 0.6252}}, \"status\": \"DONE\"}, \"exp_006_irt_05B_gsm8k\": {\"conclusion\": \"success\", \"metrics\": {\"baselines_mae\": {\"B0_raw\": 0.0034, \"B2_2pl_gamma\": 0.3202, \"B3_vanilla_4pl\": 0.0123, \"B4_linear_regression\": 0.003, \"B6_dcr_fuzzy\": 0.2634, \"IRT_4pl_gamma\": 0.0195}, \"delta_fix_applied\": true, \"joint_divergences\": 0, \"joint_ess\": 956.4, \"joint_gamma\": 0.3463, \"joint_gamma_ci\": [-0.65, 1.4], \"joint_rhat\": 1.0081, \"perbench_divergences\": 0, \"perbench_ess\": 522.2, \"perbench_gamma\": 0.508, \"perbench_gamma_ci\": [-0.64, 1.84], \"perbench_rhat\": 1.0096, \"signal_scores_after_delta\": [0, 0.016, 0.065, 0.197]}, \"status\": \"DONE\"}, \"exp_001_eval_15B_d100_aligned\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge_accuracy\": 0.7688, \"gsm8k_accuracy\": 0.6497, \"humaneval_correct\": 50, \"humaneval_pass_rate\": 0.3049, \"humaneval_total\": 164, \"mmlu_accuracy\": 0.5933}, \"status\": \"DONE\"}, \"exp_001_eval_15B_d005_aligned_v2\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge\": 0.7688, \"gsm8k\": 0.6482, \"humaneval_pass_at_1\": 0.25, \"mmlu\": 0.5852}, \"status\": \"DONE\"}, \"exp_001_sft_d100_3B\": {\"conclusion\": \"success\", \"metrics\": {\"epoch\": 1, \"runtime_hours\": 5.2, \"steps\": \"4159/4159\", \"token_accuracy\": 0.7206, \"train_loss\": 1.178}, \"status\": \"DONE\"}, \"exp_001_eval_05B_d100_aligned_v4\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge\": 0.2944, \"arc_delta_vs_d000\": -0.1749, \"gsm8k\": 0.3654, \"humaneval_delta_vs_d000\": -0.1098, \"humaneval_pass_at_1\": 0, \"mmlu\": 0.2334, \"mmlu_delta_vs_d000\": -0.1645}, \"status\": \"DONE\"}, \"exp_001_sft_d025_15B\": {\"conclusion\": \"success\", \"metrics\": {\"entropy\": 1.2623, \"epochs\": 1, \"mean_token_accuracy\": 0.7192, \"steps\": 3384, \"train_loss\": 1.2715, \"train_runtime_seconds\": 11610.6}, \"status\": \"DONE\"}, \"exp_001_eval_3B_d005_aligned\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge\": 0.829, \"gsm8k\": 0.208, \"humaneval_pass_at_1\": 0.146, \"mmlu\": 0.634}, \"status\": \"DONE\"}, \"exp_006_irt_05B_v1\": {\"conclusion\": \"failed\", \"status\": \"DONE\"}, \"exp_001_eval_05B_d025_aligned\": {\"conclusion\": \"success\", \"metrics\": {\"ARC\": 32.51, \"GSM8K\": 36.62, \"HumanEval\": \"missing - process exited before 4th benchmark\", \"MMLU\": 28.03}, \"status\": \"DONE\"}, \"exp_008_signal_survival_v4\": {\"conclusion\": \"success\", \"metrics\": {\"S1_d005_auc_mean\": 0.979, \"S1_d100_cross_cohens_d_mean\": 3.6, \"S2_d005_auc_mean\": 0.465, \"S2_d100_cross_cohens_d_mean\": -1.98, \"S4_d005_auc_mean\": 0.481, \"S4_d100_cross_cohens_d_mean\": 0.45, \"d021_fix\": \"within-model AUC only for d005; d100 uses cross-model Cohen's d\", \"effective_signals_at_05B\": 1}, \"status\": \"DONE\"}, \"exp_001_eval_05B_d100_aligned_v3\": {\"conclusion\": \"failed\", \"status\": \"DONE\"}, \"exp_008_signal_survival\": {\"conclusion\": \"success\", \"metrics\": {\"S1_d000_arc\": 0.427, \"S1_d000_gsm8k\": 0.5502, \"S1_d000_mmlu\": 0.5049, \"S1_d005_arc\": 0.995, \"S1_d005_gsm8k\": 0.9882, \"S1_d005_mmlu\": 0.953, \"S1_d100_arc\": 0.501, \"S1_d100_gsm8k\": 0.4127, \"S1_d100_mmlu\": 0.4943, \"S2_d005_arc\": 0.4659, \"S2_d005_gsm8k\": 0.4649, \"S2_d005_mmlu\": 0.4655, \"S4_d005_arc\": 0.4325, \"S4_d005_gsm8k\": 0.4947, \"S4_d005_mmlu\": 0.5165, \"signals_surviving\": 0, \"signals_total\": 3}, \"status\": \"DONE\"}, \"exp_001_eval_3B_d100_aligned\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge_accuracy\": 0.8396, \"gsm8k_exact_match\": 0.6967, \"humaneval_pass1\": 0.122, \"mmlu_accuracy\": 0.6417}, \"status\": \"DONE\"}, \"exp_001_eval_05B_d005_aligned\": {\"conclusion\": \"success\", \"metrics\": {\"d005_aligned_arc\": 0.3285, \"d005_aligned_gsm8k\": 0.3624, \"d005_aligned_humaneval\": 0.0793, \"d005_aligned_mmlu\": 0.3255}, \"status\": \"DONE\"}, \"exp_001_eval_05B_d100_aligned\": {\"conclusion\": \"failed\", \"status\": \"DONE\"}, \"exp_001_eval_05B_aligned_batch\": {\"conclusion\": \"failed\", \"metrics\": {\"d000_aligned_arc\": 0.4693, \"d000_aligned_gsm8k\": 0.3692, \"d000_aligned_humaneval\": 0.1098, \"d000_aligned_mmlu\": 0.3979, \"d000_para_aligned_arc\": 0.4792, \"d000_para_aligned_gsm8k\": 0.2807, \"d000_para_aligned_humaneval\": 0.1154, \"d000_para_aligned_mmlu\": 0.4428, \"d005_aligned_arc\": 0.3285, \"d005_aligned_gsm8k\": 0.3624, \"d005_aligned_humaneval\": 0.0793, \"d005_aligned_mmlu\": 0.3255}, \"status\": \"DONE\"}, \"exp_001_eval_05B_d005\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge\": 0.2858, \"arc_correct\": 335, \"arc_total\": 1172, \"gsm8k\": 0.3601, \"gsm8k_correct\": 475, \"gsm8k_total\": 1319, \"humaneval_correct\": 13, \"humaneval_pass1\": 0.0793, \"humaneval_total\": 164, \"mmlu\": 0.2929, \"mmlu_correct\": 4113, \"mmlu_total\": 14042}, \"status\": \"DONE\"}, \"exp_006_irt_05B\": {\"conclusion\": \"killed\", \"status\": \"DONE\"}, \"exp_003_rrf_05B\": {\"conclusion\": \"success\", \"status\": \"DONE\"}, \"exp_002_signals_05B\": {\"conclusion\": \"success\", \"status\": \"DONE\"}, \"exp_001_eval_3B_d000_aligned\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge_accuracy\": 0.8276, \"gsm8k_exact_match\": 0.1198, \"humaneval_pass_at_1\": 0.1159, \"mmlu_accuracy\": 0.634}, \"status\": \"DONE\"}, \"exp_001_eval_15B_d100_s42\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge_accuracy\": 0.7688, \"arc_challenge_correct\": 901, \"arc_challenge_total\": 1172, \"gsm8k_correct\": 857, \"gsm8k_exact_match\": 0.6497, \"gsm8k_total\": 1319, \"humaneval_correct\": 50, \"humaneval_pass_at_1\": 0.3049, \"humaneval_total\": 164, \"mmlu_accuracy\": 0.5933, \"mmlu_correct\": 8331, \"mmlu_total\": 14042}, \"status\": \"DONE\"}, \"exp_001_eval_3B_raw_gen\": {\"conclusion\": \"success\", \"metrics\": {\"gsm8k\": 0.605, \"humaneval\": 0}, \"status\": \"DONE\"}, \"exp_001_eval_05B_raw\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge\": 0.2261, \"gsm8k\": 0.1592, \"humaneval\": \"incomplete (hung at 51/164)\", \"mmlu\": 0.2302}, \"status\": \"DONE\"}, \"exp_001_sft_d005_15B\": {\"conclusion\": \"success\", \"metrics\": {\"epoch\": 1, \"mean_token_accuracy\": 0.7308, \"train_loss\": 1.2637, \"train_runtime_s\": 19864.7}, \"status\": \"DONE\"}, \"exp_001_sft_d025_05B_v3\": {\"conclusion\": \"success\", \"metrics\": {\"checkpoint_size_mb\": 166, \"entropy\": 1.5415, \"epoch\": 1, \"exit_code\": 0, \"final_loss\": 1.5178, \"lora_adapter_size_mb\": 33.6, \"mean_token_accuracy\": 0.6697, \"mean_train_loss\": 1.5479, \"num_tokens\": 20058085, \"total_steps\": 3384, \"train_samples_per_second\": 15.52, \"train_steps_per_second\": 0.97, \"training_time_min\": 58.1, \"vs_baseline_0pct\": {\"baseline_final_loss\": 1.4894, \"baseline_mean_train_loss\": 1.5388, \"baseline_token_accuracy\": 0.682, \"baseline_training_time_min\": 52.9, \"delta_final_loss\": 0.0284, \"delta_mean_train_loss\": 0.0091, \"delta_token_accuracy\": -0.0123, \"delta_training_time_min\": 5.2}}, \"status\": \"DONE\"}, \"exp_001_eval_05B_d100_v5\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge\": 0.227, \"gsm8k\": 0.3571, \"humaneval_pass1\": 0.0854, \"mmlu\": 0.2322}, \"status\": \"DONE\"}, \"exp_001_eval_05B_d000_s42_v5\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge\": 0.378, \"gsm8k\": 0.3647, \"humaneval\": 0.1098, \"mmlu\": 0.4049}, \"status\": \"DONE\"}, \"exp_001_sft_d100_15B_v2\": {\"conclusion\": \"success\", \"status\": \"DONE\"}, \"exp_001_eval_3B_d000_s42\": {\"conclusion\": \"success\", \"metrics\": {\"arc\": 0.822, \"gsm8k\": 0.117, \"humaneval\": 0.116, \"mmlu\": 0.634}, \"status\": \"DONE\"}, \"exp_001_sft_d025_05B_v2\": {\"conclusion\": \"failed\", \"status\": \"DONE\"}, \"exp_001_eval_05B_d100_v2\": {\"conclusion\": \"failed\", \"status\": \"DONE\"}, \"exp_001_sft_d025_05B\": {\"conclusion\": \"failed\", \"status\": \"DONE\"}, \"exp_001_eval_3B_d000_s123\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge_accuracy\": 0.8294, \"gsm8k_exact_match\": 0.1759, \"humaneval_pass_at_1\": 0.0854, \"mmlu_accuracy\": 0.6362}, \"status\": \"DONE\"}, \"exp_001_eval_15B_d000_s123\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge\": 0.7662, \"gsm8k\": 0.6331, \"humaneval_pass@1\": 0.1707, \"mmlu\": 0.5762}, \"status\": \"DONE\"}, \"exp_005_noise_prop_v2\": {\"conclusion\": \"failed\", \"status\": \"DONE\"}, \"exp_001_eval_15B_d000_s42_v2\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge_accuracy\": 0.7756, \"arc_challenge_correct\": 909, \"arc_challenge_total\": 1172, \"gsm8k_correct\": 840, \"gsm8k_exact_match\": 0.6368, \"gsm8k_total\": 1319, \"humaneval_correct\": 21, \"humaneval_pass_at_1\": 0.128, \"humaneval_total\": 164, \"mmlu_accuracy\": 0.5753, \"mmlu_correct\": 8079, \"mmlu_total\": 14042}, \"status\": \"DONE\"}, \"exp_001_eval_05B_d100\": {\"conclusion\": \"failed\", \"status\": \"DONE\"}, \"exp_001_eval_05B_d000_s123\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge_accuracy\": 0.3976, \"gsm8k_exact_match\": 0.3404, \"humaneval_pass_at_1\": 0.1037, \"mmlu_accuracy\": 0.4182}, \"status\": \"DONE\"}, \"exp_001_sft_d100_15B\": {\"conclusion\": \"failed\", \"status\": \"DONE\"}, \"exp_001_sft_d005_05B_v3\": {\"conclusion\": \"success\", \"metrics\": {\"checkpoint_size_mb\": 166, \"entropy\": 1.5874, \"epoch\": 1, \"exit_code\": 0, \"final_loss\": 1.478, \"lora_adapter_size_mb\": 33.6, \"mean_train_loss\": 1.5424, \"num_tokens\": 19657865, \"token_accuracy\": 0.667, \"total_steps\": 3177, \"train_samples_per_second\": 15.09, \"train_steps_per_second\": 0.943, \"training_time_min\": 56.14, \"vs_baseline_0pct\": {\"baseline_final_loss\": 1.4894, \"baseline_mean_train_loss\": 1.5388, \"baseline_token_accuracy\": 0.682, \"baseline_training_time_min\": 52.9, \"delta_final_loss\": -0.0114, \"delta_mean_train_loss\": 0.0036, \"delta_token_accuracy\": -0.015, \"delta_training_time_min\": 3.24}}, \"status\": \"DONE\"}, \"exp_001_sft_d100_05B\": {\"conclusion\": \"success\", \"metrics\": {\"exit_code\": 0, \"final_loss\": 1.5943, \"mean_train_loss\": 1.5662, \"num_tokens\": 21575068, \"token_accuracy\": 0.666, \"total_steps\": 4160, \"train_samples_per_second\": 16.09, \"train_steps_per_second\": 1.006, \"training_time_min\": 68.9, \"vs_baseline_0pct\": {\"accuracy_delta\": \"-0.016 (-2.3%)\", \"loss_delta\": \"+0.0274 (+1.8%)\", \"time_delta\": \"+16min (+30%)\"}}, \"status\": \"DONE\"}, \"exp_001_sft_0pct\": {\"conclusion\": \"success\", \"status\": \"DONE\"}, \"exp_001_sft_0pct_3B_s123\": {\"conclusion\": \"success\", \"metrics\": {\"adapter_model_mb\": 114, \"adapter_size_mb\": 488, \"checkpoint_size_mb\": 488, \"epochs\": 1, \"final_loss\": 1.114, \"mean_token_accuracy\": 0.7505, \"mean_train_loss\": 1.1309, \"steps_completed\": 3125, \"total_steps\": 3125, \"total_tokens\": 19555717, \"train_samples_per_second\": 3.91, \"training_time_min\": 213.1}, \"status\": \"DONE\"}, \"exp_001_eval_15B_d000_s42\": {\"conclusion\": \"failed\", \"status\": \"DONE\"}, \"exp_001_sft_d005_05B_v2\": {\"conclusion\": \"failed\", \"status\": \"DONE\"}, \"exp_001_sft_d005_05B\": {\"conclusion\": \"killed\", \"status\": \"DONE\"}, \"exp_001_sft_100pct_05B\": {\"conclusion\": \"failed\", \"status\": \"DONE\"}, \"exp_001_sft_0pct_3B\": {\"conclusion\": \"success\", \"metrics\": {\"adapter_size_mb\": 115, \"checkpoint_size_mb\": 488, \"exit_code\": 0, \"final_loss\": 1.0736, \"mean_train_loss\": 1.1306, \"steps\": \"3125/3125\", \"token_accuracy\": 0.734, \"training_time_min\": 214.7}, \"status\": \"DONE\"}, \"exp_001_sft_injection\": {\"conclusion\": \"success\", \"metrics\": {\"arc_qc_pass\": 697, \"arc_qc_rate\": 0.595, \"arc_total\": 1172, \"gsm8k_qc_pass\": 228, \"gsm8k_qc_rate\": 0.173, \"gsm8k_total\": 1319, \"humaneval_total\": 164, \"mmlu_qc_pass\": 6596, \"mmlu_qc_rate\": 0.47, \"mmlu_total\": 14042}, \"status\": \"DONE\"}, \"exp_001_sft_0pct_15B_s123\": {\"conclusion\": \"success\", \"metrics\": {\"token_acc\": 0.731, \"train_loss\": 1.2602, \"train_time_min\": 101.5}, \"status\": \"DONE\"}, \"exp_001_sft_0pct_05B_s123\": {\"conclusion\": \"success\", \"metrics\": {\"token_acc\": 0.676, \"train_loss\": 1.5393, \"train_time_min\": 54.5}, \"status\": \"DONE\"}, \"exp_001_sft_0pct_15B\": {\"conclusion\": \"success\", \"metrics\": {\"adapter_size_mb\": 71, \"checkpoint_size_mb\": 313, \"exit_code\": 0, \"final_loss\": 1.2039, \"mean_train_loss\": 1.2599, \"steps\": \"3125/3125\", \"token_accuracy\": 0.711, \"training_time_min\": 101.5}, \"status\": \"DONE\"}, \"exp_001_sft_0pct_05B\": {\"conclusion\": \"success\", \"metrics\": {\"adapter_size_mb\": 34, \"checkpoint_size_mb\": 166, \"exit_code\": 0, \"final_loss\": 1.4894, \"mean_train_loss\": 1.5388, \"steps\": \"3125/3125\", \"token_accuracy\": 0.682, \"training_time_min\": 52.9}, \"status\": \"DONE\"}, \"mvp_sim_confounding\": {\"conclusion\": \"success\", \"metrics\": {\"actual_confound_corr\": 0.3814, \"divergent_pct\": 0, \"fit_time_sec\": 832, \"gamma_ci_covers_true\": true, \"gamma_ci_excludes_zero\": true, \"gamma_mean\": 0.5386, \"gamma_rel_bias\": 0.0771, \"max_rhat\": 1.007, \"min_ess\": 1371.9, \"overall\": \"PASS\", \"theta_corr\": 0.9733, \"theta_residual_exp_corr\": 0.0582, \"theta_rmse\": 0.2407}, \"status\": \"DONE\"}, \"mvp_sim_4pl_gamma\": {\"conclusion\": \"success\", \"metrics\": {\"variant_a_nitems300\": {\"divergent_pct\": 0, \"fit_time_sec\": 1407.5, \"gamma_ci_covers_true\": true, \"gamma_ci_excludes_zero\": true, \"gamma_mean\": 0.466, \"gamma_rel_bias\": 0.068, \"max_rhat\": 1.003, \"overall\": \"PASS\", \"theta_corr\": 0.943, \"theta_rmse\": 0.238}}, \"status\": \"DONE\"}}, \"count\": 393, \"total\": 393, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.0404}}"
    }
  },
  "sourceToolAssistantUUID": "8ef60cf5-4df8-4ce0-b634-457bc5014096",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "a95a1f6e-644c-4d12-abb6-01351d2cbf40",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 33 · 2026-05-21T11:07:41.875Z_

```json
{
  "parentUuid": "1a33dbc3-94f6-46a8-8f01-219c5d8b94b3",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "99172156-1cc4-4d85-a4b6-20e83b8ab73c",
  "timestamp": "2026-05-21T11:07:41.875Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "a95a1f6e-644c-4d12-abb6-01351d2cbf40",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 34_

```json
{
  "type": "last-prompt",
  "leafUuid": "99172156-1cc4-4d85-a4b6-20e83b8ab73c",
  "sessionId": "a95a1f6e-644c-4d12-abb6-01351d2cbf40"
}
```

---

### Runtime record

_source line 35_

```json
{
  "type": "ai-title",
  "aiTitle": "Verify GSM8K appendix data and prepare LLaMA-3 paper sections",
  "sessionId": "a95a1f6e-644c-4d12-abb6-01351d2cbf40"
}
```

---

### Tool call

_source line 36 · 2026-05-21T11:07:47.539Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01TP8DruwtW79HPYF3JdaWxa`</summary>

```json
{
  "command": "python3 -c \"\nimport json\nwith open('/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/a95a1f6e-644c-4d12-abb6-01351d2cbf40/tool-results/mcp-agent-ml-research-read_registry-1779361661868.txt') as f:\n    data = json.load(f)\nparsed = json.loads(data['result'])\nexperiments = parsed['data']\nprint(f'Total experiments: {len(experiments)}')\n# Filter for gsm8k\ngsm = [e for e in experiments if 'gsm8k' in json.dumps(e).lower()]\nprint(f'GSM8K-related: {len(gsm)}')\nfor e in gsm:\n    eid = e.get('id','?')\n    status = e.get('status','?')\n    conclusion = str(e.get('conclusion',''))[:250]\n    metrics = json.dumps(e.get('metrics',{}))[:400] if e.get('metrics') else 'none'\n    print(f'\\\\nID: {eid}  Status: {status}')\n    print(f'  Conclusion: {conclusion}')\n    print(f'  Metrics: {metrics}')\n\" 2>&1",
  "description": "Extract all GSM8K experiments from full registry"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "99172156-1cc4-4d85-a4b6-20e83b8ab73c",
  "isSidechain": false,
  "requestId": "req_011CbFcDUrG2U6cujHZZLbiN",
  "type": "assistant",
  "uuid": "2344b46d-aac1-40ee-81c3-b5b377471d8e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "a95a1f6e-644c-4d12-abb6-01351d2cbf40",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q14JTDRXbLvwHuz2DjUDYJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 817,
      "cache_read_input_tokens": 35908,
      "output_tokens": 418,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 817,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 418,
          "cache_read_input_tokens": 35908,
          "cache_creation_input_tokens": 817,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 817
          },
          "type": "message"
        }
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

_source line 37 · 2026-05-21T11:07:47.656Z_

<details><summary>↩ Tool result · `toolu_01TP8DruwtW79HPYF3JdaWxa`</summary>

```text
Total experiments: 4
GSM8K-related: 0
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2344b46d-aac1-40ee-81c3-b5b377471d8e",
  "isSidechain": false,
  "promptId": "ff132cc0-9ef7-4a70-8848-7ec535292349",
  "type": "user",
  "uuid": "85de2ef4-dbfb-44de-8a91-e148c4060bfc",
  "toolUseResult": {
    "stdout": "Total experiments: 4\nGSM8K-related: 0",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "2344b46d-aac1-40ee-81c3-b5b377471d8e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "a95a1f6e-644c-4d12-abb6-01351d2cbf40",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 38 · 2026-05-21T11:07:51.660Z_

<details><summary>Logged reasoning block</summary>

```text
Hmm, still only 4 experiments. The registry only has 4 experiments total? That seems unlikely for a project with so many experiments. Let me check the full structure more carefully - maybe the data is nested differently or the experiments are in a different part of the registry.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "85de2ef4-dbfb-44de-8a91-e148c4060bfc",
  "isSidechain": false,
  "requestId": "req_011CbFcDufGEPQiAX8yubA6D",
  "type": "assistant",
  "uuid": "7e2a5cae-c8dd-4a3b-80e9-0cc9c8c0fb9b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "a95a1f6e-644c-4d12-abb6-01351d2cbf40",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U2ajgMjh2Qoxr7Udq1ZUXf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 445,
      "cache_read_input_tokens": 36725,
      "output_tokens": 437,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 445,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 437,
          "cache_read_input_tokens": 36725,
          "cache_creation_input_tokens": 445,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 445
          },
          "type": "message"
        }
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

_source line 39 · 2026-05-21T11:07:55.859Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01Cp5sSGrVLpapcHcPqsp8vf`</summary>

```json
{
  "command": "python3 -c \"\nimport json\nwith open('/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/a95a1f6e-644c-4d12-abb6-01351d2cbf40/tool-results/mcp-agent-ml-research-read_registry-1779361661868.txt') as f:\n    data = json.load(f)\nparsed = json.loads(data['result'])\nexps = parsed['data']\nprint(f'Total: {len(exps)}')\nfor e in exps:\n    print(f\\\"  {e.get('id')} -> {e.get('status')}: {str(e.get('conclusion',''))[:120]}\\\")\nprint()\n# Check full text size\nfull_text = json.dumps(parsed)\nprint(f'Full JSON size: {len(full_text)} chars')\n# Check if there are nested experiments\nfor k in parsed:\n    if k != 'data':\n        print(f'Other key: {k} = {str(parsed[k])[:200]}')\n\" 2>&1",
  "description": "Inspect full registry structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7e2a5cae-c8dd-4a3b-80e9-0cc9c8c0fb9b",
  "isSidechain": false,
  "requestId": "req_011CbFcDufGEPQiAX8yubA6D",
  "type": "assistant",
  "uuid": "08d75b1d-5358-4bf5-8975-80f6729441fc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "a95a1f6e-644c-4d12-abb6-01351d2cbf40",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U2ajgMjh2Qoxr7Udq1ZUXf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 445,
      "cache_read_input_tokens": 36725,
      "output_tokens": 437,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 445,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 437,
          "cache_read_input_tokens": 36725,
          "cache_creation_input_tokens": 445,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 445
          },
          "type": "message"
        }
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

_source line 40 · 2026-05-21T11:07:56.071Z_

<details><summary>↩ Tool result · reported error · `toolu_01Cp5sSGrVLpapcHcPqsp8vf`</summary>

```text
Exit code 1
Traceback (most recent call last):
  File "&lt;string>", line 9, in &lt;module>
    print(f"  {e.get('id')} -> {e.get('status')}: {str(e.get('conclusion',''))[:120]}")
               ^^^^^
AttributeError: 'str' object has no attribute 'get'
Total: 4
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "08d75b1d-5358-4bf5-8975-80f6729441fc",
  "isSidechain": false,
  "promptId": "ff132cc0-9ef7-4a70-8848-7ec535292349",
  "type": "user",
  "uuid": "b44b4425-e8c6-4d0b-b035-097b6f47ee0f",
  "toolUseResult": "Error: Exit code 1\nTraceback (most recent call last):\n  File \"&lt;string>\", line 9, in &lt;module>\n    print(f\"  {e.get('id')} -> {e.get('status')}: {str(e.get('conclusion',''))[:120]}\")\n               ^^^^^\nAttributeError: 'str' object has no attribute 'get'\nTotal: 4",
  "sourceToolAssistantUUID": "08d75b1d-5358-4bf5-8975-80f6729441fc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "a95a1f6e-644c-4d12-abb6-01351d2cbf40",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-21T11:08:01.906Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01DEvLh98cUXBF38jZFWd6tD`</summary>

```json
{
  "command": "python3 -c \"\nimport json\nwith open('/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/a95a1f6e-644c-4d12-abb6-01351d2cbf40/tool-results/mcp-agent-ml-research-read_registry-1779361661868.txt') as f:\n    data = json.load(f)\nparsed = json.loads(data['result'])\nexps = parsed['data']\nfor i, e in enumerate(exps):\n    print(f'Item {i}: type={type(e).__name__}, preview={str(e)[:300]}')\n    print()\n\" 2>&1",
  "description": "Check item types in registry data"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b44b4425-e8c6-4d0b-b035-097b6f47ee0f",
  "isSidechain": false,
  "requestId": "req_011CbFcEXfi1qkgbPkbfEBvZ",
  "type": "assistant",
  "uuid": "5d11ae3b-25a0-4246-b51f-a3fe9c27c700",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "a95a1f6e-644c-4d12-abb6-01351d2cbf40",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NmxsCcUZb1SgRiKufttNfw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 550,
      "cache_read_input_tokens": 37170,
      "output_tokens": 263,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 550,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 263,
          "cache_read_input_tokens": 37170,
          "cache_creation_input_tokens": 550,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 550
          },
          "type": "message"
        }
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

_source line 42 · 2026-05-21T11:08:01.994Z_

<details><summary>↩ Tool result · `toolu_01DEvLh98cUXBF38jZFWd6tD`</summary>

```text
Item 0: type=str, preview=experiments

Item 1: type=str, preview=count

Item 2: type=str, preview=total

Item 3: type=str, preview=baseline
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5d11ae3b-25a0-4246-b51f-a3fe9c27c700",
  "isSidechain": false,
  "promptId": "ff132cc0-9ef7-4a70-8848-7ec535292349",
  "type": "user",
  "uuid": "7c3c2681-0778-4fca-8a40-1a0a9b80bc8b",
  "toolUseResult": {
    "stdout": "Item 0: type=str, preview=experiments\n\nItem 1: type=str, preview=count\n\nItem 2: type=str, preview=total\n\nItem 3: type=str, preview=baseline",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "5d11ae3b-25a0-4246-b51f-a3fe9c27c700",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "a95a1f6e-644c-4d12-abb6-01351d2cbf40",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 43 · 2026-05-21T11:08:04.632Z_

<details><summary>Logged reasoning block</summary>

```text
The data is a dict with keys 'experiments', 'count', 'total', 'baseline'. Let me access the experiments key.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7c3c2681-0778-4fca-8a40-1a0a9b80bc8b",
  "isSidechain": false,
  "requestId": "req_011CbFcExuVz5z1NK2JfUirY",
  "type": "assistant",
  "uuid": "5960317e-491c-4794-92b4-05b8602a7922",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "a95a1f6e-644c-4d12-abb6-01351d2cbf40",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SbWoENrScv8HHqkRrkNAe4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 322,
      "cache_read_input_tokens": 37720,
      "output_tokens": 505,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 322,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 505,
          "cache_read_input_tokens": 37720,
          "cache_creation_input_tokens": 322,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 322
          },
          "type": "message"
        }
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

_source line 44 · 2026-05-21T11:08:09.045Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01S6MpotHJbSLp7NjrnHpLbk`</summary>

```json
{
  "command": "python3 -c \"\nimport json\nwith open('/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/a95a1f6e-644c-4d12-abb6-01351d2cbf40/tool-results/mcp-agent-ml-research-read_registry-1779361661868.txt') as f:\n    data = json.load(f)\nparsed = json.loads(data['result'])\nregistry = parsed['data']\nprint(f'Keys: {list(registry.keys())}')\nexps = registry['experiments']\nprint(f'Experiments count: {len(exps)}')\nprint(f'Total: {registry.get(\\\"total\\\")}')\n\n# Filter for gsm8k\ngsm = [e for e in exps if 'gsm8k' in json.dumps(e).lower()]\nprint(f'\\\\nGSM8K-related: {len(gsm)}')\nfor e in gsm:\n    eid = e.get('id','?')\n    status = e.get('status','?')\n    conclusion = str(e.get('conclusion',''))[:250]\n    metrics = json.dumps(e.get('metrics',{}))[:400] if e.get('metrics') else 'none'\n    print(f'\\\\nID: {eid}  Status: {status}')\n    print(f'  Conclusion: {conclusion}')\n    print(f'  Metrics: {metrics}')\n\" 2>&1",
  "description": "Access experiments from registry dict"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5960317e-491c-4794-92b4-05b8602a7922",
  "isSidechain": false,
  "requestId": "req_011CbFcExuVz5z1NK2JfUirY",
  "type": "assistant",
  "uuid": "5fd5a0cc-5a2d-41ea-a20a-bbb7acd16e35",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "a95a1f6e-644c-4d12-abb6-01351d2cbf40",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SbWoENrScv8HHqkRrkNAe4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 322,
      "cache_read_input_tokens": 37720,
      "output_tokens": 505,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 322,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 505,
          "cache_read_input_tokens": 37720,
          "cache_creation_input_tokens": 322,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 322
          },
          "type": "message"
        }
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

_source line 45 · 2026-05-21T11:08:09.246Z_

<details><summary>↩ Tool result · reported error · `toolu_01S6MpotHJbSLp7NjrnHpLbk`</summary>

```text
Exit code 1
Traceback (most recent call last):
  File "&lt;string>", line 16, in &lt;module>
    eid = e.get('id','?')
          ^^^^^
AttributeError: 'str' object has no attribute 'get'
Keys: ['experiments', 'count', 'total', 'baseline']
Experiments count: 393
Total: 393

GSM8K-related: 38
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5fd5a0cc-5a2d-41ea-a20a-bbb7acd16e35",
  "isSidechain": false,
  "promptId": "ff132cc0-9ef7-4a70-8848-7ec535292349",
  "type": "user",
  "uuid": "02ffc719-6930-424a-b6d1-51db6a088183",
  "toolUseResult": "Error: Exit code 1\nTraceback (most recent call last):\n  File \"&lt;string>\", line 16, in &lt;module>\n    eid = e.get('id','?')\n          ^^^^^\nAttributeError: 'str' object has no attribute 'get'\nKeys: ['experiments', 'count', 'total', 'baseline']\nExperiments count: 393\nTotal: 393\n\nGSM8K-related: 38",
  "sourceToolAssistantUUID": "5fd5a0cc-5a2d-41ea-a20a-bbb7acd16e35",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "a95a1f6e-644c-4d12-abb6-01351d2cbf40",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 46 · 2026-05-21T11:08:14.088Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01X5q5o9EsKPvP4wRs8YadwU`</summary>

```json
{
  "command": "python3 -c \"\nimport json\nwith open('/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/a95a1f6e-644c-4d12-abb6-01351d2cbf40/tool-results/mcp-agent-ml-research-read_registry-1779361661868.txt') as f:\n    data = json.load(f)\nparsed = json.loads(data['result'])\nregistry = parsed['data']\nexps = registry['experiments']\n# Check type of first experiment\nprint(f'Type of exp: {type(exps[0]).__name__}')\nprint(f'First exp preview: {str(exps[0])[:500]}')\n\" 2>&1",
  "description": "Check experiment item type"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "02ffc719-6930-424a-b6d1-51db6a088183",
  "isSidechain": false,
  "requestId": "req_011CbFcFVuKU2SmrdGR9qcVg",
  "type": "assistant",
  "uuid": "0f88afbe-ef2a-4106-9bf2-68e5f63b2e80",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "a95a1f6e-644c-4d12-abb6-01351d2cbf40",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RVgVQfCmNhXVzwBbgsEcQ2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 628,
      "cache_read_input_tokens": 38042,
      "output_tokens": 274,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 628,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 274,
          "cache_read_input_tokens": 38042,
          "cache_creation_input_tokens": 628,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 628
          },
          "type": "message"
        }
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

_source line 47 · 2026-05-21T11:08:14.289Z_

<details><summary>↩ Tool result · reported error · `toolu_01X5q5o9EsKPvP4wRs8YadwU`</summary>

```text
Exit code 1
Traceback (most recent call last):
  File "&lt;string>", line 9, in &lt;module>
    print(f'Type of exp: {type(exps[0]).__name__}')
                               ~~~~^^^
KeyError: 0
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0f88afbe-ef2a-4106-9bf2-68e5f63b2e80",
  "isSidechain": false,
  "promptId": "ff132cc0-9ef7-4a70-8848-7ec535292349",
  "type": "user",
  "uuid": "7d78235c-7e6f-42a6-83c1-e731b7275cbc",
  "toolUseResult": "Error: Exit code 1\nTraceback (most recent call last):\n  File \"&lt;string>\", line 9, in &lt;module>\n    print(f'Type of exp: {type(exps[0]).__name__}')\n                               ~~~~^^^\nKeyError: 0",
  "sourceToolAssistantUUID": "0f88afbe-ef2a-4106-9bf2-68e5f63b2e80",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "a95a1f6e-644c-4d12-abb6-01351d2cbf40",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 48 · 2026-05-21T11:08:21.660Z_

<details open><summary>🔧 Tool call — Bash · `toolu_013opSDHwRen2envYtywE3Vj`</summary>

```json
{
  "command": "python3 -c \"\nimport json\nwith open('/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/a95a1f6e-644c-4d12-abb6-01351d2cbf40/tool-results/mcp-agent-ml-research-read_registry-1779361661868.txt') as f:\n    data = json.load(f)\nparsed = json.loads(data['result'])\nexps = parsed['data']['experiments']\n# It's a dict keyed by experiment ID\nprint(f'Type: {type(exps).__name__}')\nkeys = list(exps.keys())\nprint(f'First 5 keys: {keys[:5]}')\n# Filter for gsm8k\ngsm = {k: v for k, v in exps.items() if 'gsm8k' in k.lower() or 'gsm8k' in json.dumps(v).lower()}\nprint(f'\\\\nGSM8K experiments: {len(gsm)}')\nfor k, v in gsm.items():\n    status = v.get('status','?') if isinstance(v, dict) else '?'\n    conclusion = str(v.get('conclusion',''))[:200] if isinstance(v, dict) else str(v)[:200]\n    metrics_str = json.dumps(v.get('metrics',{}))[:300] if isinstance(v, dict) and v.get('metrics') else ''\n    print(f'\\\\n{k}  [{status}]')\n    print(f'  {conclusion}')\n    if metrics_str:\n        print(f'  Metrics: {metrics_str}')\n\" 2>&1",
  "description": "Extract GSM8K experiments from dict-keyed registry"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7d78235c-7e6f-42a6-83c1-e731b7275cbc",
  "isSidechain": false,
  "requestId": "req_011CbFcFsUrCrjqhch1hKtDQ",
  "type": "assistant",
  "uuid": "565e42fb-6765-465b-953d-8b0bf1ab55e2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "a95a1f6e-644c-4d12-abb6-01351d2cbf40",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HVpvjwzyd72RwnjLpm5nkb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 358,
      "cache_read_input_tokens": 38670,
      "output_tokens": 512,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 358,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 512,
          "cache_read_input_tokens": 38670,
          "cache_creation_input_tokens": 358,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 358
          },
          "type": "message"
        }
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

_source line 49 · 2026-05-21T11:08:21.743Z_

<details><summary>↩ Tool result · `toolu_013opSDHwRen2envYtywE3Vj`</summary>

```text
Type: dict
First 5 keys: ['sft_llama3_d100_s0', 'sft_llama3_d025_s0', 'sft_llama3_d000_s0', 'sft_llama3_8b_s0_validation', 'eval_phi4_gsm8k_d000_s0']

GSM8K experiments: 129

eval_phi4_gsm8k_d000_s0  [DONE]
  success
  Metrics: {"gsm8k_accuracy": 84.46, "correct": 1114, "total": 1319}

eval_qwen14b_d100_gsm8k_s0  [DONE]
  success
  Metrics: {"gsm8k_accuracy": 82.41, "correct": 1087, "total": 1319}

eval_gemma2_gsm8k_d000_s0  [PREPARING]
  

eval_qwen14b_gsm8k_d050_s0  [PREPARING]
  

eval_qwen7b_gsm8k_s0_cqa1  [DONE]
  success
  Metrics: {"gsm8k_s0": {"d000": 73.31, "d005": 78.32, "d025": 78.24, "d050": 79.38, "d100": 81.2}, "delta_d100_d000": 7.89, "pattern": "monotonic_increase", "note": "MMLU contamination consistently boosts GSM8K \u2014 opposite to MMLU/ARC V-recovery pattern"}

eval_qwen14b_gsm8k_d025_s0  [DONE]
  success
  Metrics: {"gsm8k_accuracy": 0.793, "correct": 1046, "total": 1319}

eval_qwen14b_gsm8k_d005_s0  [DONE]
  success
  Metrics: {"gsm8k_accuracy": 0.7119, "correct": 939, "total": 1319}

eval_qwen14b_gsm8k_d000_s0  [DONE]
  success
  Metrics: {"gsm8k_accuracy": 0.7498, "correct": 989, "total": 1319}

gsm8k_qwen14b_s123_westd  [DONE]
  success

gsm8k_gemma2_s42_westd  [DONE]
  failed

gsm8k_qwen14b_s42_westd  [DONE]
  success
  Metrics: {"d000_correct": 802, "d000_gsm8k_acc": 0.608, "d100_correct": 1072, "d100_gsm8k_acc": 0.8127, "delta_pp": 20.47, "total": 1319}

gsm8k_phi4_s123_westd  [DONE]
  success
  Metrics: {"gsm8k_d000": 0.8431, "gsm8k_d100": 0.8385, "gsm8k_delta": -0.0046}

gsm8k_qwen7b_s123_cqa1  [DONE]
  success
  Metrics: {"d000_note": "s123 baseline", "d100_note": "s123 full contamination", "gsm8k_d000": 0.7005, "gsm8k_d100": 0.7923, "gsm8k_delta": 0.0918}

gsm8k_olmo2_s123_westd  [DONE]
  success
  Metrics: {"cross_seed_confirmed": true, "gsm8k_d000": 0.6846, "gsm8k_d100": 0.7089, "gsm8k_delta": 0.0243, "s123_delta": 0.0243, "s42_delta": 0.0174}

gsm8k_qwen7b_s42_intermediate_cqa1  [DONE]
  success
  Metrics: {"curve_shape": "non-linear: sharp early gain (d005 +6.37pp = 58% of total), then saturation", "delta_d005": 0.0637, "delta_d025": 0.0948, "delta_d050": 0.0865, "delta_d100": 0.1107, "gsm8k_d000": 0.7058, "gsm8k_d005": 0.7695, "gsm8k_d025": 0.8006, "gsm8k_d050": 0.7923, "gsm8k_d100": 0.8165}

gsm8k_qwen7b_s42_cqa1  [DONE]
  success
  Metrics: {"d000_correct": 931, "d100_correct": 1077, "gsm8k_d000": 0.7058, "gsm8k_d100": 0.8165, "gsm8k_delta": 0.1107, "total_items": 1319}

gsm8k_olmo2_s42_westd  [DONE]
  success
  Metrics: {"d000_correct": 903, "d100_correct": 926, "gsm8k_d000": 0.6846, "gsm8k_d100": 0.702, "gsm8k_delta": 0.0174, "total_items": 1319}

gsm8k_phi4_s42_westd  [PREPARING]
  

exp_001_eval_7b_d000_s42_gsm8k  [DONE]
  success
  Metrics: {"gsm8k_accuracy": 0.7104, "gsm8k_correct": 937, "gsm8k_total": 1319}

exp_001_eval_3B_d025_s123_para_aligned  [DONE]
  success
  Metrics: {"ARC": 0.8121, "GSM8K": 0.4254, "HumanEval": 0.1538, "MMLU": 0.6615}

exp_002_signals_15B_instruct_gsm8k_v2  [PREPARING]
  killed

exp006-gsm8k-d024-delta  [PREPARING]
  killed

exp_008_base_pretrained_eval_gsm8k_arc  [DONE]
  success
  Metrics: {"arc_challenge_accuracy": 0.228, "gsm8k_accuracy": 0.163}

exp_009_deepseek_eval  [DONE]
  negative
  Metrics: {"arc_acc": 0.226, "arc_n": 1172, "gsm8k_acc": 0.608, "gsm8k_n": 1319, "mmlu_acc": 0.229, "mmlu_n": 14042, "note": "MMLU/ARC below random due to logprob-based MC eval incompatible with CoT reasoning model; only GSM8K valid"}

exp_009_3b_instruct_eval  [DONE]
  success
  Metrics: {"arc_acc": 0.811, "arc_n": 1172, "gsm8k_acc": 0.76, "gsm8k_n": 1319, "mmlu_acc": 0.605, "mmlu_n": 14042}

exp_009_15b_instruct_eval  [DONE]
  success
  Metrics: {"arc_acc": 0.765, "arc_n": 1172, "gsm8k_acc": 0.593, "gsm8k_n": 1319, "mmlu_acc": 0.577, "mmlu_n": 14042}

exp_009_05b_instruct_eval  [DONE]
  success
  Metrics: {"arc_acc": 0.5, "arc_n": 1172, "gsm8k_acc": 0.388, "gsm8k_n": 1319, "mmlu_acc": 0.343, "mmlu_n": 14042}

exp_001_eval_3B_d000_s42_a32_batch  [DONE]
  success
  Metrics: {"arc_challenge": {"aligned": 0.8242, "aligned_n": 1172, "para_aligned": 0.8106, "para_aligned_n": 697}, "gsm8k": {"aligned": 0.141, "aligned_n": 1319, "para_aligned": 0.0526, "para_aligned_n": 228}, "humaneval": {"aligned": 0.1402, "aligned_n": 164, "para_aligned": 0.1923, "para_aligned_n": 26}, "m

exp_001_eval_3B_d100_s42_a32_batch  [DONE]
  success
  Metrics: {"aligned": {"arc_challenge": 0.8208, "gsm8k": 0.7036, "humaneval_correct": "26/164", "mmlu": 0.6364}, "para_aligned": {"arc_challenge": 0.8106, "gsm8k": 0.5702, "humaneval_correct": "2/26", "mmlu": 0.6674}}

exp_001_eval_3B_d100_s123_a32_batch  [DONE]
  success
  Metrics: {"arc_challenge": {"aligned": 0.8251, "aligned_n": 1172, "para_aligned": 0.8049, "para_aligned_n": 697}, "gsm8k": {"aligned": 0.7074, "aligned_n": 1319, "para_aligned": 0.5746, "para_aligned_n": 228}, "humaneval": {"aligned": 0.1159, "aligned_n": 164, "para_aligned": 0, "para_aligned_n": 26}, "mmlu"

exp_001_eval_3B_d005_s123_gsm8k  [DONE]
  success
  Metrics: {"gsm8k": 0.6308}

exp_001_eval_llama32_3B_d000_s42_v3  [DONE]
  success
  Metrics: {"arc_challenge": 0.6007, "gsm8k": 0.1918, "humaneval_pass@1": 0.0427, "mmlu": 0.4545}

exp_002_signals_llama32_3B_d000_gsm8k_v2  [DONE]
  success
  Metrics: {"all_signals_nonempty": true, "signal_files": {"signal_s1_embedding_gsm8k.json": {"items": 1319, "size": "717K"}, "signal_s2_minkpp_gsm8k.json": {"items": 1319, "size": "266K"}, "signal_s4_selfcritique_gsm8k.json": {"items": 1319, "size": "311K"}, "signals_merged_gsm8k.json": {"items": 1319, "size"

exp_001_eval_llama32_3B_d005_s42  [DONE]
  success
  Metrics: {"arc_challenge": 0.5956, "gsm8k": 0.2722, "humaneval_pass@1": 0.0122, "mmlu": 0.4256}

exp_001_eval_llama32_3B_d100_s42  [DONE]
  success
  Metrics: {"arc_acc": 0.5981, "gsm8k_acc": 0.26, "mmlu_acc": 0.3408, "note": "MMLU degenerate (all-A prediction), ARC/GSM8K valid"}

exp006_cross_family_pooled_irt  [DONE]
  negative
  Metrics: {"N_pooled_arc": 20, "N_pooled_gsm8k": 28, "N_pooled_mmlu": 20, "arc_gamma_pooled": 0.002, "arc_gamma_qwen_only": 0.727, "family_specificity_arc_delta": -0.725, "gsm8k_gamma_pooled": -0.11, "mmlu_gamma_pooled": 0.213, "mmlu_gamma_qwen_only": 0.655, "v3_clean": true}

exp006-pooled-05B-15B-gsm8k-v2  [DONE]
  negative
  Metrics: {"NOTE": "per-bench not converged; no oracle baseline exists", "convergence": "FAILED (rhat=1.015, ess=330)", "coverage_95": 0.5, "exposure_source": "signal_rrf", "gamma_joint": 0.1202, "gamma_joint_ci": [-0.74, 0.96], "gamma_perbench": 0.1871, "gamma_perbench_ci": [-0.92, 1.33], "mae": 0.036, "n_mo

exp_002_signals_llama32_3B_d100_gsm8k  [DONE]
  success

exp_002_signals_llama32_3B_d000_arc_gsm8k  [DONE]
  success

exp_002_signals_llama32_3B_d025_mmlu_arc_gsm8k  [DONE]
  failed

exp_002_signals_llama32_3B_d005_arc_gsm8k  [DONE]
  success

exp_006_pooled_2pl_gamma_qwen_n24  [DONE]
  success
  Metrics: {"arc_challenge": {"N": 16, "cal_mae": 0.0201, "delta_mae": 0.0136, "ess": 1449, "gamma_ci": [0.0207, 1.4433], "gamma_mean": 0.7269, "items": 300, "ppp": 0.003, "raw_mae": 0.0338, "rhat": 1.0072}, "gsm8k": {"N": 24, "cal_mae": 0.0062, "delta_mae": 0.1632, "ess": 1313, "gamma_ci": [-0.3636, 0.4902], 

exp_002_signals_llama32_3B_d000_gsm8k  [DONE]
  failed

exp_002_signals_15B_instruct_gsm8k  [DONE]
  failed

exp_006_pooled_irt_vanilla_2pl_n13  [DONE]
  success
  Metrics: {"ARC": {"N": 16, "PPP": 0.035, "cal_MAE": 0.0158, "delta_MAE": 0.018, "raw_MAE": 0.0338}, "GSM8K": {"N": 24, "PPP": 0.691, "cal_MAE": 0.0063, "delta_MAE": 0.1631, "raw_MAE": 0.1694}, "MMLU": {"N": 16, "PPP": 0.349, "cal_MAE": 0.0068, "delta_MAE": 0.0087, "raw_MAE": 0.0155}, "note": "Re-run with nam

exp_006_pooled_irt_2pl_gamma_n16  [DONE]
  success
  Metrics: {"ARC": {"CI_excludes_zero": true, "N": 16, "PPP": 0.003, "R_hat_max": 1.01, "cal_MAE": 0.0201, "delta_MAE": 0.0136, "gamma_hat": 0.73}, "GSM8K": {"CI_excludes_zero": false, "N": 24, "PPP": 0.541, "R_hat_max": 1.01, "cal_MAE": 0.0062, "delta_MAE": 0.1632, "gamma_hat": 0.06}, "MMLU": {"CI_excludes_ze

exp_001_eval_15B_instruct  [DONE]
  success
  Metrics: {"ARC": 0.7654, "GSM8K": 0.5929, "MMLU": 0.5775}

exp_006_pooled_irt_rrf_n25_v2  [DONE]
  success
  Metrics: {"arc_N8_4PLgamma": "over_parameterized_cal_worsens", "gsm8k_N16_delta_mae": 0.118, "gsm8k_calibration": "effective", "mmlu_N8_4PLgamma": "over_parameterized_cal_worsens", "note": "GSM8K N=16 works. MMLU/ARC N=8 with 4PL+gamma over-parameterized, PPP=0.006/0.000, cal_mae > raw_mae. Need 2PL+gamma or

exp_001_eval_3B_instruct_v2  [DONE]
  success
  Metrics: {"GSM8K": 0.76, "HumanEval": 0.5, "MMLU": 0.605}

exp_002_signals_3B_d100_a32_s42  [DONE]
  success
  Metrics: {"benchmarks_completed": ["mmlu", "gsm8k", "arc_challenge"], "signals_generated": ["s1_embedding", "s2_minkpp", "s4_selfcritique"], "status_note": "Signals validated via pooled IRT (exp_006_pooled_irt_all_scales, N=23 success). Analysis worker completed 2026-05-16T10:50:52 but callback not processed

exp_006_pooled_irt_all_scales  [DONE]
  success
  Metrics: {"arc_challenge": {"cal_mae": 0.0153, "delta_mae": 0.0183, "divergences": 0, "ess": 1670, "gamma_ci95": [-0.2552, 1.2529], "gamma_mean": 0.4859, "n_items": 300, "n_models": 13, "ppp": 0.027, "raw_mae": 0.0335, "rhat": 1.0065}, "exposure": "rrf_signal", "gsm8k": {"cal_mae": 0.0078, "delta_mae": 0.155

exp_002_signals_3B_d000_a32_s42  [DONE]
  success
  Metrics: {"benchmarks": {"arc_challenge": {"n_items": 1172, "signals": ["s1_embedding", "s2_minkpp", "s4_selfcritique"]}, "gsm8k": {"n_items": 1319, "signals": ["s1_embedding", "s2_minkpp", "s4_selfcritique"]}, "mmlu": {"n_items": 14042, "signals": ["s1_embedding", "s2_minkpp", "s4_selfcritique"]}}, "output_

exp_006_pooled_irt_05b_15b  [DONE]
  success
  Metrics: {"arc_cal_mae": 0.0682, "arc_ci95": "[-0.271, 2.857]", "arc_delta_mae": -0.064, "arc_ess": 1480, "arc_gamma": 1.2259, "arc_n_models": 5, "arc_ppp": 0, "arc_raw_mae": 0.0042, "arc_rhat": 1.0072, "gsm8k_cal_mae": 0.0373, "gsm8k_ci95": "[-0.990, 1.019]", "gsm8k_delta_mae": 0.1128, "gsm8k_ess": 1300, "g

exp006_pooled_rrf_irt_05b_15b  [DONE]
  success
  Metrics: {"arc_challenge": {"cal_mae": 0.0682, "delta_mae": -0.064, "divergences": 0, "ess": 1480, "gamma_ci95": [-0.2711, 2.8571], "gamma_mean": 1.2259, "n_items": 300, "n_models": 5, "ppp": 0, "raw_mae": 0.0042, "rhat": 1.0072}, "gsm8k": {"cal_mae": 0.0373, "delta_mae": 0.1128, "divergences": 0, "ess": 130

exp_001_eval_3B_d005_s42_para_aligned  [DONE]
  success
  Metrics: {"arc_challenge_acc": 0.8164, "arc_challenge_n": 697, "gsm8k_acc": 0.3421, "gsm8k_n": 228, "humaneval_n": 26, "humaneval_pass1": 0.0769, "mmlu_acc": 0.6471, "mmlu_n": 6596}

exp_001_eval_3B_d000_s42_a32_para_aligned  [DONE]
  success
  Metrics: {"arc_para": 0.8106, "gsm8k_para": 0.0526, "humaneval_para": 0.1923, "mmlu_para": 0.6431}

exp_001_eval_3B_d005_s42_a32_batch  [DONE]
  success
  Metrics: {"arc": 0.8251, "arc_para": 0.8164, "gsm8k": 0.4147, "gsm8k_para": 0.3421, "humaneval": 0.1341, "humaneval_para": 0.0769, "mmlu": 0.6308, "mmlu_para": 0.6471}

exp_008_instruct_rl_proxy  [DONE]
  failed
  Metrics: {"base_pretrained_signals": "computing_PID_701898_GPU5", "comparison": {"arc": {"d000_sft_s2": 1.7079, "d000_sft_s4": -0.9538, "instruct_s2": 1.6737, "instruct_s4": -0.9227, "s4_delta_instruct_vs_sft": 0.0311}, "gsm8k": {"d000_sft_s2": 1.6532, "d000_sft_s4": -0.9408, "instruct_s2": 1.7073, "instruct

exp_001_eval_3B_d025_s42_a32_para  [DONE]
  success
  Metrics: {"arc_challenge_para": 0.8106, "gsm8k_para": "completed", "humaneval_para": 0, "mmlu_para": "completed_6596_items", "output_dir": "/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d025_v3_s42_para_aligned", "sentinel": ".done exists"}

exp_002_signals_3B_v7  [DONE]
  success
  Metrics: {"benchmarks": ["mmlu", "gsm8k", "arc_challenge"], "merged_files": 3, "output_dir": "/root/autodl-tmp/exp002/signals/Qwen2.5-3B_d005_s123/", "signal_files": 9, "signals": ["s1_embedding", "s2_minkpp", "s4_selfcritique"]}

exp_001_eval_15B_s123_para_aligned_batch  [DONE]
  success
  Metrics: {"d000_s123_para_aligned": {"arc_challenge": 0.7547, "gsm8k": 0.5921, "humaneval": 0.1538, "mmlu": 0.6111}, "d005_s123_para_aligned": {"arc_challenge": 0.7475, "gsm8k": 0.5439, "humaneval": 0.0769, "mmlu": 0.614}, "d025_s123_para_aligned": {"arc_challenge": 0.7504, "gsm8k": 0.5482, "humaneval": 0.19

exp_001_eval_3B_d100_s123_para_aligned_v2  [DONE]
  success
  Metrics: {"arc_challenge": {"accuracy": 0.8164, "correct": 569, "total": 697}, "gsm8k": {"accuracy": 0.5877, "correct": 134, "total": 228}, "humaneval": {"correct": 2, "pass@1": 0.0769, "total": 26}, "mmlu": {"accuracy": 0.6565, "correct": 4330, "total": 6596}}

exp_001_eval_3B_d005_s123_aligned  [DONE]
  success
  Metrics: {"arc_challenge_accuracy": 0.8242, "gsm8k_exact_match": 0.6308, "humaneval_pass1": 0.1037, "mmlu_accuracy": 0.6324}

exp_001_eval_3B_d025_s123_aligned  [DONE]
  success
  Metrics: {"arc_challenge": 0.8336, "gsm8k": 0.5254, "humaneval": 0.1585, "mmlu": 0.6367}

exp_001_eval_3B_d005_s123_para_aligned  [DONE]
  success
  Metrics: {"ARC": 0.8192, "GSM8K": 0.5, "HumanEval": 0.0769, "MMLU": 0.6461}

exp_001_eval_15B_d005_s123  [DONE]
  success
  Metrics: {"arc_challenge": {"accuracy": 0.7568, "correct": 887, "total": 1172}, "gsm8k": {"correct": 855, "exact_match": 0.6482, "total": 1319}, "humaneval": {"correct": 41, "pass@1": 0.25, "total": 164}, "mmlu": {"accuracy": 0.5869, "correct": 8241, "total": 14042}}

exp_001_eval_15B_d005_s123_v2  [DONE]
  success
  Metrics: {"arc_challenge": {"accuracy": 0.7568, "correct": 887, "total": 1172}, "gsm8k": {"correct": 855, "exact_match": 0.6482, "total": 1319}, "humaneval": {"correct": 41, "pass@1": 0.25, "total": 164}, "mmlu": {"accuracy": 0.5869, "correct": 8241, "total": 14042}}

exp_001_eval_15B_d025_s123  [DONE]
  success
  Metrics: {"arc_challenge": {"accuracy": 0.7577, "correct": 888, "total": 1172}, "gsm8k": {"correct": 864, "exact_match": 0.655, "total": 1319}, "humaneval": {"correct": 41, "pass@1": 0.25, "total": 164}, "mmlu": {"accuracy": 0.5881, "correct": 8258, "total": 14042}}

exp_001_eval_15B_d025_s123_v2  [DONE]
  success
  Metrics: {"arc_challenge": {"accuracy": 0.7577, "correct": 888, "total": 1172}, "gsm8k": {"correct": 864, "exact_match": 0.655, "total": 1319}, "humaneval": {"correct": 41, "pass@1": 0.25, "total": 164}, "mmlu": {"accuracy": 0.5881, "correct": 8258, "total": 14042}}

exp_001_eval_3B_d000_s42_para_aligned  [DONE]
  success
  Metrics: {"arc_challenge": {"accuracy": 0.8235, "correct": 574, "total": 697}, "gsm8k": {"accuracy": 0.0482, "correct": 11, "total": 228}, "humaneval": {"correct": 3, "pass@1": 0.1154, "total": 26}, "mmlu": {"accuracy": 0.6474, "correct": 4270, "total": 6596}}

exp_001_eval_3B_d100_s42_para_aligned  [DONE]
  success
  Metrics: {"arc_challenge": {"accuracy": 0.8092, "correct": 564, "total": 697}, "gsm8k": {"accuracy": 0.5833, "correct": 133, "total": 228}, "humaneval": {"correct": 3, "pass@1": 0.1154, "total": 26}, "mmlu": {"accuracy": 0.659, "correct": 4347, "total": 6596}}

exp_001_eval_3B_d000_s123_aligned  [DONE]
  success
  Metrics: {"arc_challenge": 0.8328, "gsm8k": 0.1812, "humaneval": 0.0854, "mmlu": 0.6332}

exp_001_eval_3B_d005_s42_aligned  [DONE]
  success
  Metrics: {"arc_challenge": 0.8294, "gsm8k": 0.2077, "humaneval": 0.1463, "mmlu": 0.6345}

exp_008_base_pretrained_eval_v2  [DONE]
  success
  Metrics: {"arc_challenge": 0.2278, "gsm8k": 0.163, "humaneval": 0, "mmlu": 0.2294}

exp_008_base_pretrained_15B_eval_v2  [DONE]
  success
  Metrics: {"arc_challenge": 0.2304, "arc_correct": 270, "arc_total": 1172, "gsm8k": 0.0053, "gsm8k_correct": 7, "gsm8k_total": 1319, "humaneval_correct": 38, "humaneval_pass1": 0.2317, "humaneval_total": 164, "mmlu": 0.2303, "mmlu_correct": 3234, "mmlu_total": 14042}

exp_008_base_pretrained_15B_eval  [DONE]
  success
  Metrics: {"arc_challenge_accuracy": 0.2304, "arc_correct": 270, "arc_total": 1172, "gsm8k_accuracy": 0.0053, "gsm8k_correct": 7, "gsm8k_total": 1319, "humaneval_correct": 38, "humaneval_pass@1": 0.2317, "humaneval_total": 164, "mmlu_accuracy": 0.2303, "mmlu_correct": 3234, "mmlu_total": 14042}

exp_001_eval_15B_d000_s123_aligned  [DONE]
  success
  Metrics: {"arc_challenge_accuracy": 0.7577, "gsm8k_accuracy": 0.6535, "humaneval_pass@1": 0.1707, "mmlu_accuracy": 0.5855}

exp_001_eval_15B_d100_s123_aligned  [DONE]
  success
  Metrics: {"arc_challenge_accuracy": 0.7816, "gsm8k_accuracy": 0.6444, "humaneval_pass@1": 0.2805, "mmlu_accuracy": 0.5956}

exp_001_eval_05B_d000_s123_aligned  [DONE]
  success
  Metrics: {"arc_challenge": 0.4974, "gsm8k": 0.3412, "humaneval": 0.1037, "mmlu": 0.4216}

exp_001_eval_3B_d000_s42_v3  [DONE]
  success
  Metrics: {"arc_challenge": 0.8276, "gsm8k": 0.1198, "humaneval": 0.1159, "mmlu": 0.634}

exp006-s1only-gsm8k-2pl  [DONE]
  success
  Metrics: {"ci_excludes_zero": false, "divergent_count": 0, "gamma_ci95": [-0.306, 0.591], "gamma_mean": 0.1389, "gamma_sd": 0.2274, "max_rhat": 1.0024, "min_ess": 3604.4, "obs_mean_acc": 0.5086, "ppp": 0.2835, "pred_mean_acc": 0.5011, "residual_mae": 0.0083}

exp_001_eval_3B_d000_v2_s123_aligned  [DONE]
  success
  Metrics: {"arc_challenge": 0.8259, "gsm8k": 0.2676, "humaneval": 0.061, "mmlu": 0.6314}

exp_001_eval_3B_d025_v2_aligned  [DONE]
  success
  Metrics: {"arc_challenge": 0.8276, "gsm8k": 0.6793, "humaneval": 0.0976, "mmlu": 0.5998}

exp_001_eval_3B_d100_v2_s123_aligned  [DONE]
  success
  Metrics: {"arc_challenge": 0.8311, "gsm8k": 0.7324, "humaneval": 0.1829, "mmlu": 0.6319}

exp_001_eval_05B_d025_s123_aligned  [DONE]
  success
  Metrics: {"arc_challenge": {"accuracy": 0.4061, "correct": 476, "total": 1172}, "gsm8k": {"accuracy": 0.3533, "correct": 466, "total": 1319}, "humaneval": {"correct": 14, "pass@1": 0.0854, "total": 164}, "mmlu": {"accuracy": 0.3473, "correct": 4877, "total": 14042}}

exp_008_instruct_05B_eval  [DONE]
  success
  Metrics: {"arc_challenge_accuracy": 0.2816, "gsm8k_accuracy": 0.3882, "humaneval_pass@1": 0, "mmlu_accuracy": 0.2462}

exp_001_eval_3B_d100_v2_aligned_v2  [DONE]
  success
  Metrics: {"arc_challenge_accuracy": 0.8242, "gsm8k_accuracy": 0.7415, "humaneval_pass@1": 0.1707, "mmlu_accuracy": 0.632}

exp_001_eval_3B_d025_v2_para_aligned  [DONE]
  success
  Metrics: {"arc_challenge_para_accuracy": 0.8106, "gsm8k_para_accuracy": 0.5482, "humaneval_para_pass@1": 0.1154, "mmlu_para_accuracy": 0.621}

exp_001_eval_3B_d000_v2_s123_para_aligned  [DONE]
  success
  Metrics: {"arc_challenge_para_accuracy": 0.8121, "gsm8k_para_accuracy": 0.1491, "humaneval_para_pass@1": 0.0385, "mmlu_para_accuracy": 0.6512}

exp006-pooled-s1only-gsm8k-v2  [DONE]
  success
  Metrics: {"diagnostics_ok": false, "divergent_pct": 0, "ess_min": 330.2, "fit_time_sec": 336.9, "gamma": 0.1871, "gamma_ci_excludes_zero": false, "gamma_ci_lower": -0.9172, "gamma_ci_upper": 1.3294, "gamma_sd": 0.5687, "n_items": 1319, "n_models": 8, "note": "No evaluation/baselines files generated; only IRT

exp006-oracle-gsm8k-extended-v2  [DONE]
  success
  Metrics: {"baselines": {"B0_raw_mae": 0.005, "B4_linear_regression_mae": 0.008, "B5_emperor_mae": 0.005, "B6_dcr_fuzzy_mae": 0.138}, "coverage_50": 0.25, "coverage_80": 0.25, "coverage_95": 0.31, "divergent_pct": 0, "ece": 0.0894, "ess_min": 1221.9, "fit_time_sec": 6240.3, "gamma": 3.773, "gamma_ci_excludes_

exp_001_eval_05B_d005_s123_para_aligned  [DONE]
  success
  Metrics: {"arc_challenge_para_accuracy": 0.2912, "gsm8k_para_accuracy": 0.2939, "humaneval_para_pass@1": 0, "mmlu_para_accuracy": 0.3166}

exp_001_eval_05B_d005_s123_aligned  [DONE]
  success
  Metrics: {"arc_challenge_accuracy": 0.2978, "gsm8k_accuracy": 0.3677, "humaneval_pass@1": 0.0976, "mmlu_accuracy": 0.3002}

exp_001_eval_3B_d000_v2_para_aligned_v2  [DONE]
  success
  Metrics: {"arc_challenge_para_accuracy": 0.8121, "gsm8k_para_accuracy": 0.2895, "humaneval_para_pass@1": 0.0385, "mmlu_para_accuracy": 0.6468}

exp006-oracle-gsm8k-extended  [DONE]
  failed

exp006-pooled-s1only-gsm8k  [DONE]
  failed

exp_001_eval_3B_d100_v2_para_aligned  [DONE]
  success
  Metrics: {"arc_challenge_para": 0.8092, "gsm8k_para": 0.5833, "humaneval_para_pass1": 0.1154, "mmlu_para": 0.659}

exp_001_eval_3B_d000_v2_aligned  [DONE]
  success
  Metrics: {"arc_challenge": 0.8183, "gsm8k": 0.3525, "humaneval_pass@1": 0.0976, "mmlu": 0.6295}

exp_001_eval_05B_d100_s123_aligned  [DONE]
  success
  Metrics: {"arc_challenge_accuracy": 0.3669, "arc_challenge_correct": 430, "arc_challenge_total": 1172, "gsm8k_accuracy": 0.3798, "gsm8k_correct": 501, "gsm8k_total": 1319, "humaneval_pass_at_1": 0.1037, "humaneval_total": 164, "mmlu_accuracy": 0.3058, "mmlu_correct": 4294, "mmlu_total": 14042}

exp_001_eval_05B_d025_aligned_v2  [DONE]
  success
  Metrics: {"arc_challenge": 0.3199, "format": "paraphrased_aligned", "gsm8k": 0.3114, "humaneval_pass1": 0.1923, "mmlu": 0.2835}

exp_001_eval_15B_d025_aligned  [DONE]
  success
  Metrics: {"arc_challenge": 0.7688, "gsm8k": 0.6535, "humaneval_pass1": 0.2256, "mmlu": 0.5902}

exp_001_eval_05B_d005_para_aligned  [DONE]
  success
  Metrics: {"arc_challenge": 0.33, "arc_correct": 230, "arc_total": 697, "gsm8k": 0.2588, "gsm8k_correct": 59, "gsm8k_total": 228, "humaneval": 0, "humaneval_correct": 0, "humaneval_total": 26, "mmlu": 0.3548, "mmlu_correct": 2340, "mmlu_total": 6596}

exp_001_eval_15B_d025_para_aligned  [DONE]
  success
  Metrics: {"arc_challenge": 0.766, "gsm8k": 0.539, "humaneval": 0.154, "mmlu": 0.618}

exp_001_eval_3B_d100_para_aligned  [DONE]
  success
  Metrics: {"arc_challenge": 0.828, "gsm8k": 0.614, "mmlu": 0.676}

exp_006_pooled_gsm8k_v1  [DONE]
  failed

exp_001_eval_15B_aligned_batch  [DONE]
  success
  Metrics: {"arc": {"d000_orig": 0.7722, "d000_para": 0.7547, "d005_orig": 0.7688, "d005_para": 0.7532, "d100_orig": 0.7688, "d100_para": 0.7661}, "gsm8k": {"d000_orig": 0.6543, "d000_para": 0.557, "d005_orig": 0.6482, "d005_para": 0.5439, "d100_orig": 0.6497, "d100_para": 0.5526}, "humaneval": {"d000_orig": 0

exp_006_irt_05B_gsm8k  [DONE]
  success
  Metrics: {"baselines_mae": {"B0_raw": 0.0034, "B2_2pl_gamma": 0.3202, "B3_vanilla_4pl": 0.0123, "B4_linear_regression": 0.003, "B6_dcr_fuzzy": 0.2634, "IRT_4pl_gamma": 0.0195}, "delta_fix_applied": true, "joint_divergences": 0, "joint_ess": 956.4, "joint_gamma": 0.3463, "joint_gamma_ci": [-0.65, 1.4], "joint

exp_001_eval_15B_d100_aligned  [DONE]
  success
  Metrics: {"arc_challenge_accuracy": 0.7688, "gsm8k_accuracy": 0.6497, "humaneval_correct": 50, "humaneval_pass_rate": 0.3049, "humaneval_total": 164, "mmlu_accuracy": 0.5933}

exp_001_eval_15B_d005_aligned_v2  [DONE]
  success
  Metrics: {"arc_challenge": 0.7688, "gsm8k": 0.6482, "humaneval_pass_at_1": 0.25, "mmlu": 0.5852}

exp_001_eval_05B_d100_aligned_v4  [DONE]
  success
  Metrics: {"arc_challenge": 0.2944, "arc_delta_vs_d000": -0.1749, "gsm8k": 0.3654, "humaneval_delta_vs_d000": -0.1098, "humaneval_pass_at_1": 0, "mmlu": 0.2334, "mmlu_delta_vs_d000": -0.1645}

exp_001_eval_3B_d005_aligned  [DONE]
  success
  Metrics: {"arc_challenge": 0.829, "gsm8k": 0.208, "humaneval_pass_at_1": 0.146, "mmlu": 0.634}

exp_001_eval_05B_d025_aligned  [DONE]
  success
  Metrics: {"ARC": 32.51, "GSM8K": 36.62, "HumanEval": "missing - process exited before 4th benchmark", "MMLU": 28.03}

exp_008_signal_survival  [DONE]
  success
  Metrics: {"S1_d000_arc": 0.427, "S1_d000_gsm8k": 0.5502, "S1_d000_mmlu": 0.5049, "S1_d005_arc": 0.995, "S1_d005_gsm8k": 0.9882, "S1_d005_mmlu": 0.953, "S1_d100_arc": 0.501, "S1_d100_gsm8k": 0.4127, "S1_d100_mmlu": 0.4943, "S2_d005_arc": 0.4659, "S2_d005_gsm8k": 0.4649, "S2_d005_mmlu": 0.4655, "S4_d005_arc": 

exp_001_eval_3B_d100_aligned  [DONE]
  success
  Metrics: {"arc_challenge_accuracy": 0.8396, "gsm8k_exact_match": 0.6967, "humaneval_pass1": 0.122, "mmlu_accuracy": 0.6417}

exp_001_eval_05B_d005_aligned  [DONE]
  success
  Metrics: {"d005_aligned_arc": 0.3285, "d005_aligned_gsm8k": 0.3624, "d005_aligned_humaneval": 0.0793, "d005_aligned_mmlu": 0.3255}

exp_001_eval_05B_aligned_batch  [DONE]
  failed
  Metrics: {"d000_aligned_arc": 0.4693, "d000_aligned_gsm8k": 0.3692, "d000_aligned_humaneval": 0.1098, "d000_aligned_mmlu": 0.3979, "d000_para_aligned_arc": 0.4792, "d000_para_aligned_gsm8k": 0.2807, "d000_para_aligned_humaneval": 0.1154, "d000_para_aligned_mmlu": 0.4428, "d005_aligned_arc": 0.3285, "d005_ali

exp_001_eval_05B_d005  [DONE]
  success
  Metrics: {"arc_challenge": 0.2858, "arc_correct": 335, "arc_total": 1172, "gsm8k": 0.3601, "gsm8k_correct": 475, "gsm8k_total": 1319, "humaneval_correct": 13, "humaneval_pass1": 0.0793, "humaneval_total": 164, "mmlu": 0.2929, "mmlu_correct": 4113, "mmlu_total": 14042}

exp_001_eval_3B_d000_aligned  [DONE]
  success
  Metrics: {"arc_challenge_accuracy": 0.8276, "gsm8k_exact_match": 0.1198, "humaneval_pass_at_1": 0.1159, "mmlu_accuracy": 0.634}

exp_001_eval_15B_d100_s42  [DONE]
  success
  Metrics: {"arc_challenge_accuracy": 0.7688, "arc_challenge_correct": 901, "arc_challenge_total": 1172, "gsm8k_correct": 857, "gsm8k_exact_match": 0.6497, "gsm8k_total": 1319, "humaneval_correct": 50, "humaneval_pass_at_1": 0.3049, "humaneval_total": 164, "mmlu_accuracy": 0.5933, "mmlu_correct": 8331, "mmlu_t

exp_001_eval_3B_raw_gen  [DONE]
  success
  Metrics: {"gsm8k": 0.605, "humaneval": 0}

exp_001_eval_05B_raw  [DONE]
  success
  Metrics: {"arc_challenge": 0.2261, "gsm8k": 0.1592, "humaneval": "incomplete (hung at 51/164)", "mmlu": 0.2302}

exp_001_eval_05B_d100_v5  [DONE]
  success
  Metrics: {"arc_challenge": 0.227, "gsm8k": 0.3571, "humaneval_pass1": 0.0854, "mmlu": 0.2322}

exp_001_eval_05B_d000_s42_v5  [DONE]
  success
  Metrics: {"arc_challenge": 0.378, "gsm8k": 0.3647, "humaneval": 0.1098, "mmlu": 0.4049}

exp_001_eval_3B_d000_s42  [DONE]
  success
  Metrics: {"arc": 0.822, "gsm8k": 0.117, "humaneval": 0.116, "mmlu": 0.634}

exp_001_eval_3B_d000_s123  [DONE]
  success
  Metrics: {"arc_challenge_accuracy": 0.8294, "gsm8k_exact_match": 0.1759, "humaneval_pass_at_1": 0.0854, "mmlu_accuracy": 0.6362}

exp_001_eval_15B_d000_s123  [DONE]
  success
  Metrics: {"arc_challenge": 0.7662, "gsm8k": 0.6331, "humaneval_pass@1": 0.1707, "mmlu": 0.5762}

exp_001_eval_15B_d000_s42_v2  [DONE]
  success
  Metrics: {"arc_challenge_accuracy": 0.7756, "arc_challenge_correct": 909, "arc_challenge_total": 1172, "gsm8k_correct": 840, "gsm8k_exact_match": 0.6368, "gsm8k_total": 1319, "humaneval_correct": 21, "humaneval_pass_at_1": 0.128, "humaneval_total": 164, "mmlu_accuracy": 0.5753, "mmlu_correct": 8079, "mmlu_to

exp_001_eval_05B_d000_s123  [DONE]
  success
  Metrics: {"arc_challenge_accuracy": 0.3976, "gsm8k_exact_match": 0.3404, "humaneval_pass_at_1": 0.1037, "mmlu_accuracy": 0.4182}

exp_001_sft_injection  [DONE]
  success
  Metrics: {"arc_qc_pass": 697, "arc_qc_rate": 0.595, "arc_total": 1172, "gsm8k_qc_pass": 228, "gsm8k_qc_rate": 0.173, "gsm8k_total": 1319, "humaneval_total": 164, "mmlu_qc_pass": 6596, "mmlu_qc_rate": 0.47, "mmlu_total": 14042}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "565e42fb-6765-465b-953d-8b0bf1ab55e2",
  "isSidechain": false,
  "promptId": "ff132cc0-9ef7-4a70-8848-7ec535292349",
  "type": "user",
  "uuid": "4d160ac0-125f-47ee-bb71-aa3944fb09f3",
  "toolUseResult": {
    "stdout": "Type: dict\nFirst 5 keys: ['sft_llama3_d100_s0', 'sft_llama3_d025_s0', 'sft_llama3_d000_s0', 'sft_llama3_8b_s0_validation', 'eval_phi4_gsm8k_d000_s0']\n\nGSM8K experiments: 129\n\neval_phi4_gsm8k_d000_s0  [DONE]\n  success\n  Metrics: {\"gsm8k_accuracy\": 84.46, \"correct\": 1114, \"total\": 1319}\n\neval_qwen14b_d100_gsm8k_s0  [DONE]\n  success\n  Metrics: {\"gsm8k_accuracy\": 82.41, \"correct\": 1087, \"total\": 1319}\n\neval_gemma2_gsm8k_d000_s0  [PREPARING]\n  \n\neval_qwen14b_gsm8k_d050_s0  [PREPARING]\n  \n\neval_qwen7b_gsm8k_s0_cqa1  [DONE]\n  success\n  Metrics: {\"gsm8k_s0\": {\"d000\": 73.31, \"d005\": 78.32, \"d025\": 78.24, \"d050\": 79.38, \"d100\": 81.2}, \"delta_d100_d000\": 7.89, \"pattern\": \"monotonic_increase\", \"note\": \"MMLU contamination consistently boosts GSM8K \\u2014 opposite to MMLU/ARC V-recovery pattern\"}\n\neval_qwen14b_gsm8k_d025_s0  [DONE]\n  success\n  Metrics: {\"gsm8k_accuracy\": 0.793, \"correct\": 1046, \"total\": 1319}\n\neval_qwen14b_gsm8k_d005_s0  [DONE]\n  success\n  Metrics: {\"gsm8k_accuracy\": 0.7119, \"correct\": 939, \"total\": 1319}\n\neval_qwen14b_gsm8k_d000_s0  [DONE]\n  success\n  Metrics: {\"gsm8k_accuracy\": 0.7498, \"correct\": 989, \"total\": 1319}\n\ngsm8k_qwen14b_s123_westd  [DONE]\n  success\n\ngsm8k_gemma2_s42_westd  [DONE]\n  failed\n\ngsm8k_qwen14b_s42_westd  [DONE]\n  success\n  Metrics: {\"d000_correct\": 802, \"d000_gsm8k_acc\": 0.608, \"d100_correct\": 1072, \"d100_gsm8k_acc\": 0.8127, \"delta_pp\": 20.47, \"total\": 1319}\n\ngsm8k_phi4_s123_westd  [DONE]\n  success\n  Metrics: {\"gsm8k_d000\": 0.8431, \"gsm8k_d100\": 0.8385, \"gsm8k_delta\": -0.0046}\n\ngsm8k_qwen7b_s123_cqa1  [DONE]\n  success\n  Metrics: {\"d000_note\": \"s123 baseline\", \"d100_note\": \"s123 full contamination\", \"gsm8k_d000\": 0.7005, \"gsm8k_d100\": 0.7923, \"gsm8k_delta\": 0.0918}\n\ngsm8k_olmo2_s123_westd  [DONE]\n  success\n  Metrics: {\"cross_seed_confirmed\": true, \"gsm8k_d000\": 0.6846, \"gsm8k_d100\": 0.7089, \"gsm8k_delta\": 0.0243, \"s123_delta\": 0.0243, \"s42_delta\": 0.0174}\n\ngsm8k_qwen7b_s42_intermediate_cqa1  [DONE]\n  success\n  Metrics: {\"curve_shape\": \"non-linear: sharp early gain (d005 +6.37pp = 58% of total), then saturation\", \"delta_d005\": 0.0637, \"delta_d025\": 0.0948, \"delta_d050\": 0.0865, \"delta_d100\": 0.1107, \"gsm8k_d000\": 0.7058, \"gsm8k_d005\": 0.7695, \"gsm8k_d025\": 0.8006, \"gsm8k_d050\": 0.7923, \"gsm8k_d100\": 0.8165}\n\ngsm8k_qwen7b_s42_cqa1  [DONE]\n  success\n  Metrics: {\"d000_correct\": 931, \"d100_correct\": 1077, \"gsm8k_d000\": 0.7058, \"gsm8k_d100\": 0.8165, \"gsm8k_delta\": 0.1107, \"total_items\": 1319}\n\ngsm8k_olmo2_s42_westd  [DONE]\n  success\n  Metrics: {\"d000_correct\": 903, \"d100_correct\": 926, \"gsm8k_d000\": 0.6846, \"gsm8k_d100\": 0.702, \"gsm8k_delta\": 0.0174, \"total_items\": 1319}\n\ngsm8k_phi4_s42_westd  [PREPARING]\n  \n\nexp_001_eval_7b_d000_s42_gsm8k  [DONE]\n  success\n  Metrics: {\"gsm8k_accuracy\": 0.7104, \"gsm8k_correct\": 937, \"gsm8k_total\": 1319}\n\nexp_001_eval_3B_d025_s123_para_aligned  [DONE]\n  success\n  Metrics: {\"ARC\": 0.8121, \"GSM8K\": 0.4254, \"HumanEval\": 0.1538, \"MMLU\": 0.6615}\n\nexp_002_signals_15B_instruct_gsm8k_v2  [PREPARING]\n  killed\n\nexp006-gsm8k-d024-delta  [PREPARING]\n  killed\n\nexp_008_base_pretrained_eval_gsm8k_arc  [DONE]\n  success\n  Metrics: {\"arc_challenge_accuracy\": 0.228, \"gsm8k_accuracy\": 0.163}\n\nexp_009_deepseek_eval  [DONE]\n  negative\n  Metrics: {\"arc_acc\": 0.226, \"arc_n\": 1172, \"gsm8k_acc\": 0.608, \"gsm8k_n\": 1319, \"mmlu_acc\": 0.229, \"mmlu_n\": 14042, \"note\": \"MMLU/ARC below random due to logprob-based MC eval incompatible with CoT reasoning model; only GSM8K valid\"}\n\nexp_009_3b_instruct_eval  [DONE]\n  success\n  Metrics: {\"arc_acc\": 0.811, \"arc_n\": 1172, \"gsm8k_acc\": 0.76, \"gsm8k_n\": 1319, \"mmlu_acc\": 0.605, \"mmlu_n\": 14042}\n\nexp_009_15b_instruct_eval  [DONE]\n  success\n  Metrics: {\"arc_acc\": 0.765, \"arc_n\": 1172, \"gsm8k_acc\": 0.593, \"gsm8k_n\": 1319, \"mmlu_acc\": 0.577, \"mmlu_n\": 14042}\n\nexp_009_05b_instruct_eval  [DONE]\n  success\n  Metrics: {\"arc_acc\": 0.5, \"arc_n\": 1172, \"gsm8k_acc\": 0.388, \"gsm8k_n\": 1319, \"mmlu_acc\": 0.343, \"mmlu_n\": 14042}\n\nexp_001_eval_3B_d000_s42_a32_batch  [DONE]\n  success\n  Metrics: {\"arc_challenge\": {\"aligned\": 0.8242, \"aligned_n\": 1172, \"para_aligned\": 0.8106, \"para_aligned_n\": 697}, \"gsm8k\": {\"aligned\": 0.141, \"aligned_n\": 1319, \"para_aligned\": 0.0526, \"para_aligned_n\": 228}, \"humaneval\": {\"aligned\": 0.1402, \"aligned_n\": 164, \"para_aligned\": 0.1923, \"para_aligned_n\": 26}, \"m\n\nexp_001_eval_3B_d100_s42_a32_batch  [DONE]\n  success\n  Metrics: {\"aligned\": {\"arc_challenge\": 0.8208, \"gsm8k\": 0.7036, \"humaneval_correct\": \"26/164\", \"mmlu\": 0.6364}, \"para_aligned\": {\"arc_challenge\": 0.8106, \"gsm8k\": 0.5702, \"humaneval_correct\": \"2/26\", \"mmlu\": 0.6674}}\n\nexp_001_eval_3B_d100_s123_a32_batch  [DONE]\n  success\n  Metrics: {\"arc_challenge\": {\"aligned\": 0.8251, \"aligned_n\": 1172, \"para_aligned\": 0.8049, \"para_aligned_n\": 697}, \"gsm8k\": {\"aligned\": 0.7074, \"aligned_n\": 1319, \"para_aligned\": 0.5746, \"para_aligned_n\": 228}, \"humaneval\": {\"aligned\": 0.1159, \"aligned_n\": 164, \"para_aligned\": 0, \"para_aligned_n\": 26}, \"mmlu\"\n\nexp_001_eval_3B_d005_s123_gsm8k  [DONE]\n  success\n  Metrics: {\"gsm8k\": 0.6308}\n\nexp_001_eval_llama32_3B_d000_s42_v3  [DONE]\n  success\n  Metrics: {\"arc_challenge\": 0.6007, \"gsm8k\": 0.1918, \"humaneval_pass@1\": 0.0427, \"mmlu\": 0.4545}\n\nexp_002_signals_llama32_3B_d000_gsm8k_v2  [DONE]\n  success\n  Metrics: {\"all_signals_nonempty\": true, \"signal_files\": {\"signal_s1_embedding_gsm8k.json\": {\"items\": 1319, \"size\": \"717K\"}, \"signal_s2_minkpp_gsm8k.json\": {\"items\": 1319, \"size\": \"266K\"}, \"signal_s4_selfcritique_gsm8k.json\": {\"items\": 1319, \"size\": \"311K\"}, \"signals_merged_gsm8k.json\": {\"items\": 1319, \"size\"\n\nexp_001_eval_llama32_3B_d005_s42  [DONE]\n  success\n  Metrics: {\"arc_challenge\": 0.5956, \"gsm8k\": 0.2722, \"humaneval_pass@1\": 0.0122, \"mmlu\": 0.4256}\n\nexp_001_eval_llama32_3B_d100_s42  [DONE]\n  success\n  Metrics: {\"arc_acc\": 0.5981, \"gsm8k_acc\": 0.26, \"mmlu_acc\": 0.3408, \"note\": \"MMLU degenerate (all-A prediction), ARC/GSM8K valid\"}\n\nexp006_cross_family_pooled_irt  [DONE]\n  negative\n  Metrics: {\"N_pooled_arc\": 20, \"N_pooled_gsm8k\": 28, \"N_pooled_mmlu\": 20, \"arc_gamma_pooled\": 0.002, \"arc_gamma_qwen_only\": 0.727, \"family_specificity_arc_delta\": -0.725, \"gsm8k_gamma_pooled\": -0.11, \"mmlu_gamma_pooled\": 0.213, \"mmlu_gamma_qwen_only\": 0.655, \"v3_clean\": true}\n\nexp006-pooled-05B-15B-gsm8k-v2  [DONE]\n  negative\n  Metrics: {\"NOTE\": \"per-bench not converged; no oracle baseline exists\", \"convergence\": \"FAILED (rhat=1.015, ess=330)\", \"coverage_95\": 0.5, \"exposure_source\": \"signal_rrf\", \"gamma_joint\": 0.1202, \"gamma_joint_ci\": [-0.74, 0.96], \"gamma_perbench\": 0.1871, \"gamma_perbench_ci\": [-0.92, 1.33], \"mae\": 0.036, \"n_mo\n\nexp_002_signals_llama32_3B_d100_gsm8k  [DONE]\n  success\n\nexp_002_signals_llama32_3B_d000_arc_gsm8k  [DONE]\n  success\n\nexp_002_signals_llama32_3B_d025_mmlu_arc_gsm8k  [DONE]\n  failed\n\nexp_002_signals_llama32_3B_d005_arc_gsm8k  [DONE]\n  success\n\nexp_006_pooled_2pl_gamma_qwen_n24  [DONE]\n  success\n  Metrics: {\"arc_challenge\": {\"N\": 16, \"cal_mae\": 0.0201, \"delta_mae\": 0.0136, \"ess\": 1449, \"gamma_ci\": [0.0207, 1.4433], \"gamma_mean\": 0.7269, \"items\": 300, \"ppp\": 0.003, \"raw_mae\": 0.0338, \"rhat\": 1.0072}, \"gsm8k\": {\"N\": 24, \"cal_mae\": 0.0062, \"delta_mae\": 0.1632, \"ess\": 1313, \"gamma_ci\": [-0.3636, 0.4902], \n\nexp_002_signals_llama32_3B_d000_gsm8k  [DONE]\n  failed\n\nexp_002_signals_15B_instruct_gsm8k  [DONE]\n  failed\n\nexp_006_pooled_irt_vanilla_2pl_n13  [DONE]\n  success\n  Metrics: {\"ARC\": {\"N\": 16, \"PPP\": 0.035, \"cal_MAE\": 0.0158, \"delta_MAE\": 0.018, \"raw_MAE\": 0.0338}, \"GSM8K\": {\"N\": 24, \"PPP\": 0.691, \"cal_MAE\": 0.0063, \"delta_MAE\": 0.1631, \"raw_MAE\": 0.1694}, \"MMLU\": {\"N\": 16, \"PPP\": 0.349, \"cal_MAE\": 0.0068, \"delta_MAE\": 0.0087, \"raw_MAE\": 0.0155}, \"note\": \"Re-run with nam\n\nexp_006_pooled_irt_2pl_gamma_n16  [DONE]\n  success\n  Metrics: {\"ARC\": {\"CI_excludes_zero\": true, \"N\": 16, \"PPP\": 0.003, \"R_hat_max\": 1.01, \"cal_MAE\": 0.0201, \"delta_MAE\": 0.0136, \"gamma_hat\": 0.73}, \"GSM8K\": {\"CI_excludes_zero\": false, \"N\": 24, \"PPP\": 0.541, \"R_hat_max\": 1.01, \"cal_MAE\": 0.0062, \"delta_MAE\": 0.1632, \"gamma_hat\": 0.06}, \"MMLU\": {\"CI_excludes_ze\n\nexp_001_eval_15B_instruct  [DONE]\n  success\n  Metrics: {\"ARC\": 0.7654, \"GSM8K\": 0.5929, \"MMLU\": 0.5775}\n\nexp_006_pooled_irt_rrf_n25_v2  [DONE]\n  success\n  Metrics: {\"arc_N8_4PLgamma\": \"over_parameterized_cal_worsens\", \"gsm8k_N16_delta_mae\": 0.118, \"gsm8k_calibration\": \"effective\", \"mmlu_N8_4PLgamma\": \"over_parameterized_cal_worsens\", \"note\": \"GSM8K N=16 works. MMLU/ARC N=8 with 4PL+gamma over-parameterized, PPP=0.006/0.000, cal_mae > raw_mae. Need 2PL+gamma or\n\nexp_001_eval_3B_instruct_v2  [DONE]\n  success\n  Metrics: {\"GSM8K\": 0.76, \"HumanEval\": 0.5, \"MMLU\": 0.605}\n\nexp_002_signals_3B_d100_a32_s42  [DONE]\n  success\n  Metrics: {\"benchmarks_completed\": [\"mmlu\", \"gsm8k\", \"arc_challenge\"], \"signals_generated\": [\"s1_embedding\", \"s2_minkpp\", \"s4_selfcritique\"], \"status_note\": \"Signals validated via pooled IRT (exp_006_pooled_irt_all_scales, N=23 success). Analysis worker completed 2026-05-16T10:50:52 but callback not processed\n\nexp_006_pooled_irt_all_scales  [DONE]\n  success\n  Metrics: {\"arc_challenge\": {\"cal_mae\": 0.0153, \"delta_mae\": 0.0183, \"divergences\": 0, \"ess\": 1670, \"gamma_ci95\": [-0.2552, 1.2529], \"gamma_mean\": 0.4859, \"n_items\": 300, \"n_models\": 13, \"ppp\": 0.027, \"raw_mae\": 0.0335, \"rhat\": 1.0065}, \"exposure\": \"rrf_signal\", \"gsm8k\": {\"cal_mae\": 0.0078, \"delta_mae\": 0.155\n\nexp_002_signals_3B_d000_a32_s42  [DONE]\n  success\n  Metrics: {\"benchmarks\": {\"arc_challenge\": {\"n_items\": 1172, \"signals\": [\"s1_embedding\", \"s2_minkpp\", \"s4_selfcritique\"]}, \"gsm8k\": {\"n_items\": 1319, \"signals\": [\"s1_embedding\", \"s2_minkpp\", \"s4_selfcritique\"]}, \"mmlu\": {\"n_items\": 14042, \"signals\": [\"s1_embedding\", \"s2_minkpp\", \"s4_selfcritique\"]}}, \"output_\n\nexp_006_pooled_irt_05b_15b  [DONE]\n  success\n  Metrics: {\"arc_cal_mae\": 0.0682, \"arc_ci95\": \"[-0.271, 2.857]\", \"arc_delta_mae\": -0.064, \"arc_ess\": 1480, \"arc_gamma\": 1.2259, \"arc_n_models\": 5, \"arc_ppp\": 0, \"arc_raw_mae\": 0.0042, \"arc_rhat\": 1.0072, \"gsm8k_cal_mae\": 0.0373, \"gsm8k_ci95\": \"[-0.990, 1.019]\", \"gsm8k_delta_mae\": 0.1128, \"gsm8k_ess\": 1300, \"g\n\nexp006_pooled_rrf_irt_05b_15b  [DONE]\n  success\n  Metrics: {\"arc_challenge\": {\"cal_mae\": 0.0682, \"delta_mae\": -0.064, \"divergences\": 0, \"ess\": 1480, \"gamma_ci95\": [-0.2711, 2.8571], \"gamma_mean\": 1.2259, \"n_items\": 300, \"n_models\": 5, \"ppp\": 0, \"raw_mae\": 0.0042, \"rhat\": 1.0072}, \"gsm8k\": {\"cal_mae\": 0.0373, \"delta_mae\": 0.1128, \"divergences\": 0, \"ess\": 130\n\nexp_001_eval_3B_d005_s42_para_aligned  [DONE]\n  success\n  Metrics: {\"arc_challenge_acc\": 0.8164, \"arc_challenge_n\": 697, \"gsm8k_acc\": 0.3421, \"gsm8k_n\": 228, \"humaneval_n\": 26, \"humaneval_pass1\": 0.0769, \"mmlu_acc\": 0.6471, \"mmlu_n\": 6596}\n\nexp_001_eval_3B_d000_s42_a32_para_aligned  [DONE]\n  success\n  Metrics: {\"arc_para\": 0.8106, \"gsm8k_para\": 0.0526, \"humaneval_para\": 0.1923, \"mmlu_para\": 0.6431}\n\nexp_001_eval_3B_d005_s42_a32_batch  [DONE]\n  success\n  Metrics: {\"arc\": 0.8251, \"arc_para\": 0.8164, \"gsm8k\": 0.4147, \"gsm8k_para\": 0.3421, \"humaneval\": 0.1341, \"humaneval_para\": 0.0769, \"mmlu\": 0.6308, \"mmlu_para\": 0.6471}\n\nexp_008_instruct_rl_proxy  [DONE]\n  failed\n  Metrics: {\"base_pretrained_signals\": \"computing_PID_701898_GPU5\", \"comparison\": {\"arc\": {\"d000_sft_s2\": 1.7079, \"d000_sft_s4\": -0.9538, \"instruct_s2\": 1.6737, \"instruct_s4\": -0.9227, \"s4_delta_instruct_vs_sft\": 0.0311}, \"gsm8k\": {\"d000_sft_s2\": 1.6532, \"d000_sft_s4\": -0.9408, \"instruct_s2\": 1.7073, \"instruct\n\nexp_001_eval_3B_d025_s42_a32_para  [DONE]\n  success\n  Metrics: {\"arc_challenge_para\": 0.8106, \"gsm8k_para\": \"completed\", \"humaneval_para\": 0, \"mmlu_para\": \"completed_6596_items\", \"output_dir\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d025_v3_s42_para_aligned\", \"sentinel\": \".done exists\"}\n\nexp_002_signals_3B_v7  [DONE]\n  success\n  Metrics: {\"benchmarks\": [\"mmlu\", \"gsm8k\", \"arc_challenge\"], \"merged_files\": 3, \"output_dir\": \"/root/autodl-tmp/exp002/signals/Qwen2.5-3B_d005_s123/\", \"signal_files\": 9, \"signals\": [\"s1_embedding\", \"s2_minkpp\", \"s4_selfcritique\"]}\n\nexp_001_eval_15B_s123_para_aligned_batch  [DONE]\n  success\n  Metrics: {\"d000_s123_para_aligned\": {\"arc_challenge\": 0.7547, \"gsm8k\": 0.5921, \"humaneval\": 0.1538, \"mmlu\": 0.6111}, \"d005_s123_para_aligned\": {\"arc_challenge\": 0.7475, \"gsm8k\": 0.5439, \"humaneval\": 0.0769, \"mmlu\": 0.614}, \"d025_s123_para_aligned\": {\"arc_challenge\": 0.7504, \"gsm8k\": 0.5482, \"humaneval\": 0.19\n\nexp_001_eval_3B_d100_s123_para_aligned_v2  [DONE]\n  success\n  Metrics: {\"arc_challenge\": {\"accuracy\": 0.8164, \"correct\": 569, \"total\": 697}, \"gsm8k\": {\"accuracy\": 0.5877, \"correct\": 134, \"total\": 228}, \"humaneval\": {\"correct\": 2, \"pass@1\": 0.0769, \"total\": 26}, \"mmlu\": {\"accuracy\": 0.6565, \"correct\": 4330, \"total\": 6596}}\n\nexp_001_eval_3B_d005_s123_aligned  [DONE]\n  success\n  Metrics: {\"arc_challenge_accuracy\": 0.8242, \"gsm8k_exact_match\": 0.6308, \"humaneval_pass1\": 0.1037, \"mmlu_accuracy\": 0.6324}\n\nexp_001_eval_3B_d025_s123_aligned  [DONE]\n  success\n  Metrics: {\"arc_challenge\": 0.8336, \"gsm8k\": 0.5254, \"humaneval\": 0.1585, \"mmlu\": 0.6367}\n\nexp_001_eval_3B_d005_s123_para_aligned  [DONE]\n  success\n  Metrics: {\"ARC\": 0.8192, \"GSM8K\": 0.5, \"HumanEval\": 0.0769, \"MMLU\": 0.6461}\n\nexp_001_eval_15B_d005_s123  [DONE]\n  success\n  Metrics: {\"arc_challenge\": {\"accuracy\": 0.7568, \"correct\": 887, \"total\": 1172}, \"gsm8k\": {\"correct\": 855, \"exact_match\": 0.6482, \"total\": 1319}, \"humaneval\": {\"correct\": 41, \"pass@1\": 0.25, \"total\": 164}, \"mmlu\": {\"accuracy\": 0.5869, \"correct\": 8241, \"total\": 14042}}\n\nexp_001_eval_15B_d005_s123_v2  [DONE]\n  success\n  Metrics: {\"arc_challenge\": {\"accuracy\": 0.7568, \"correct\": 887, \"total\": 1172}, \"gsm8k\": {\"correct\": 855, \"exact_match\": 0.6482, \"total\": 1319}, \"humaneval\": {\"correct\": 41, \"pass@1\": 0.25, \"total\": 164}, \"mmlu\": {\"accuracy\": 0.5869, \"correct\": 8241, \"total\": 14042}}\n\nexp_001_eval_15B_d025_s123  [DONE]\n  success\n  Metrics: {\"arc_challenge\": {\"accuracy\": 0.7577, \"correct\": 888, \"total\": 1172}, \"gsm8k\": {\"correct\": 864, \"exact_match\": 0.655, \"total\": 1319}, \"humaneval\": {\"correct\": 41, \"pass@1\": 0.25, \"total\": 164}, \"mmlu\": {\"accuracy\": 0.5881, \"correct\": 8258, \"total\": 14042}}\n\nexp_001_eval_15B_d025_s123_v2  [DONE]\n  success\n  Metrics: {\"arc_challenge\": {\"accuracy\": 0.7577, \"correct\": 888, \"total\": 1172}, \"gsm8k\": {\"correct\": 864, \"exact_match\": 0.655, \"total\": 1319}, \"humaneval\": {\"correct\": 41, \"pass@1\": 0.25, \"total\": 164}, \"mmlu\": {\"accuracy\": 0.5881, \"correct\": 8258, \"total\": 14042}}\n\nexp_001_eval_3B_d000_s42_para_aligned  [DONE]\n  success\n  Metrics: {\"arc_challenge\": {\"accuracy\": 0.8235, \"correct\": 574, \"total\": 697}, \"gsm8k\": {\"accuracy\": 0.0482, \"correct\": 11, \"total\": 228}, \"humaneval\": {\"correct\": 3, \"pass@1\": 0.1154, \"total\": 26}, \"mmlu\": {\"accuracy\": 0.6474, \"correct\": 4270, \"total\": 6596}}\n\nexp_001_eval_3B_d100_s42_para_aligned  [DONE]\n  success\n  Metrics: {\"arc_challenge\": {\"accuracy\": 0.8092, \"correct\": 564, \"total\": 697}, \"gsm8k\": {\"accuracy\": 0.5833, \"correct\": 133, \"total\": 228}, \"humaneval\": {\"correct\": 3, \"pass@1\": 0.1154, \"total\": 26}, \"mmlu\": {\"accuracy\": 0.659, \"correct\": 4347, \"total\": 6596}}\n\nexp_001_eval_3B_d000_s123_aligned  [DONE]\n  success\n  Metrics: {\"arc_challenge\": 0.8328, \"gsm8k\": 0.1812, \"humaneval\": 0.0854, \"mmlu\": 0.6332}\n\nexp_001_eval_3B_d005_s42_aligned  [DONE]\n  success\n  Metrics: {\"arc_challenge\": 0.8294, \"gsm8k\": 0.2077, \"humaneval\": 0.1463, \"mmlu\": 0.6345}\n\nexp_008_base_pretrained_eval_v2  [DONE]\n  success\n  Metrics: {\"arc_challenge\": 0.2278, \"gsm8k\": 0.163, \"humaneval\": 0, \"mmlu\": 0.2294}\n\nexp_008_base_pretrained_15B_eval_v2  [DONE]\n  success\n  Metrics: {\"arc_challenge\": 0.2304, \"arc_correct\": 270, \"arc_total\": 1172, \"gsm8k\": 0.0053, \"gsm8k_correct\": 7, \"gsm8k_total\": 1319, \"humaneval_correct\": 38, \"humaneval_pass1\": 0.2317, \"humaneval_total\": 164, \"mmlu\": 0.2303, \"mmlu_correct\": 3234, \"mmlu_total\": 14042}\n\nexp_008_base_pretrained_15B_eval  [DONE]\n  success\n  Metrics: {\"arc_challenge_accuracy\": 0.2304, \"arc_correct\": 270, \"arc_total\": 1172, \"gsm8k_accuracy\": 0.0053, \"gsm8k_correct\": 7, \"gsm8k_total\": 1319, \"humaneval_correct\": 38, \"humaneval_pass@1\": 0.2317, \"humaneval_total\": 164, \"mmlu_accuracy\": 0.2303, \"mmlu_correct\": 3234, \"mmlu_total\": 14042}\n\nexp_001_eval_15B_d000_s123_aligned  [DONE]\n  success\n  Metrics: {\"arc_challenge_accuracy\": 0.7577, \"gsm8k_accuracy\": 0.6535, \"humaneval_pass@1\": 0.1707, \"mmlu_accuracy\": 0.5855}\n\nexp_001_eval_15B_d100_s123_aligned  [DONE]\n  success\n  Metrics: {\"arc_challenge_accuracy\": 0.7816, \"gsm8k_accuracy\": 0.6444, \"humaneval_pass@1\": 0.2805, \"mmlu_accuracy\": 0.5956}\n\nexp_001_eval_05B_d000_s123_aligned  [DONE]\n  success\n  Metrics: {\"arc_challenge\": 0.4974, \"gsm8k\": 0.3412, \"humaneval\": 0.1037, \"mmlu\": 0.4216}\n\nexp_001_eval_3B_d000_s42_v3  [DONE]\n  success\n  Metrics: {\"arc_challenge\": 0.8276, \"gsm8k\": 0.1198, \"humaneval\": 0.1159, \"mmlu\": 0.634}\n\nexp006-s1only-gsm8k-2pl  [DONE]\n  success\n  Metrics: {\"ci_excludes_zero\": false, \"divergent_count\": 0, \"gamma_ci95\": [-0.306, 0.591], \"gamma_mean\": 0.1389, \"gamma_sd\": 0.2274, \"max_rhat\": 1.0024, \"min_ess\": 3604.4, \"obs_mean_acc\": 0.5086, \"ppp\": 0.2835, \"pred_mean_acc\": 0.5011, \"residual_mae\": 0.0083}\n\nexp_001_eval_3B_d000_v2_s123_aligned  [DONE]\n  success\n  Metrics: {\"arc_challenge\": 0.8259, \"gsm8k\": 0.2676, \"humaneval\": 0.061, \"mmlu\": 0.6314}\n\nexp_001_eval_3B_d025_v2_aligned  [DONE]\n  success\n  Metrics: {\"arc_challenge\": 0.8276, \"gsm8k\": 0.6793, \"humaneval\": 0.0976, \"mmlu\": 0.5998}\n\nexp_001_eval_3B_d100_v2_s123_aligned  [DONE]\n  success\n  Metrics: {\"arc_challenge\": 0.8311, \"gsm8k\": 0.7324, \"humaneval\": 0.1829, \"mmlu\": 0.6319}\n\nexp_001_eval_05B_d025_s123_aligned  [DONE]\n  success\n  Metrics: {\"arc_challenge\": {\"accuracy\": 0.4061, \"correct\": 476, \"total\": 1172}, \"gsm8k\": {\"accuracy\": 0.3533, \"correct\": 466, \"total\": 1319}, \"humaneval\": {\"correct\": 14, \"pass@1\": 0.0854, \"total\": 164}, \"mmlu\": {\"accuracy\": 0.3473, \"correct\": 4877, \"total\": 14042}}\n\nexp_008_instruct_05B_eval  [DONE]\n  success\n  Metrics: {\"arc_challenge_accuracy\": 0.2816, \"gsm8k_accuracy\": 0.3882, \"humaneval_pass@1\": 0, \"mmlu_accuracy\": 0.2462}\n\nexp_001_eval_3B_d100_v2_aligned_v2  [DONE]\n  success\n  Metrics: {\"arc_challenge_accuracy\": 0.8242, \"gsm8k_accuracy\": 0.7415, \"humaneval_pass@1\": 0.1707, \"mmlu_accuracy\": 0.632}\n\nexp_001_eval_3B_d025_v2_para_aligned  [DONE]\n  success\n  Metrics: {\"arc_challenge_para_accuracy\": 0.8106, \"gsm8k_para_accuracy\": 0.5482, \"humaneval_para_pass@1\": 0.1154, \"mmlu_para_accuracy\": 0.621}\n\nexp_001_eval_3B_d000_v2_s123_para_aligned  [DONE]\n  success\n  Metrics: {\"arc_challenge_para_accuracy\": 0.8121, \"gsm8k_para_accuracy\": 0.1491, \"humaneval_para_pass@1\": 0.0385, \"mmlu_para_accuracy\": 0.6512}\n\nexp006-pooled-s1only-gsm8k-v2  [DONE]\n  success\n  Metrics: {\"diagnostics_ok\": false, \"divergent_pct\": 0, \"ess_min\": 330.2, \"fit_time_sec\": 336.9, \"gamma\": 0.1871, \"gamma_ci_excludes_zero\": false, \"gamma_ci_lower\": -0.9172, \"gamma_ci_upper\": 1.3294, \"gamma_sd\": 0.5687, \"n_items\": 1319, \"n_models\": 8, \"note\": \"No evaluation/baselines files generated; only IRT\n\nexp006-oracle-gsm8k-extended-v2  [DONE]\n  success\n  Metrics: {\"baselines\": {\"B0_raw_mae\": 0.005, \"B4_linear_regression_mae\": 0.008, \"B5_emperor_mae\": 0.005, \"B6_dcr_fuzzy_mae\": 0.138}, \"coverage_50\": 0.25, \"coverage_80\": 0.25, \"coverage_95\": 0.31, \"divergent_pct\": 0, \"ece\": 0.0894, \"ess_min\": 1221.9, \"fit_time_sec\": 6240.3, \"gamma\": 3.773, \"gamma_ci_excludes_\n\nexp_001_eval_05B_d005_s123_para_aligned  [DONE]\n  success\n  Metrics: {\"arc_challenge_para_accuracy\": 0.2912, \"gsm8k_para_accuracy\": 0.2939, \"humaneval_para_pass@1\": 0, \"mmlu_para_accuracy\": 0.3166}\n\nexp_001_eval_05B_d005_s123_aligned  [DONE]\n  success\n  Metrics: {\"arc_challenge_accuracy\": 0.2978, \"gsm8k_accuracy\": 0.3677, \"humaneval_pass@1\": 0.0976, \"mmlu_accuracy\": 0.3002}\n\nexp_001_eval_3B_d000_v2_para_aligned_v2  [DONE]\n  success\n  Metrics: {\"arc_challenge_para_accuracy\": 0.8121, \"gsm8k_para_accuracy\": 0.2895, \"humaneval_para_pass@1\": 0.0385, \"mmlu_para_accuracy\": 0.6468}\n\nexp006-oracle-gsm8k-extended  [DONE]\n  failed\n\nexp006-pooled-s1only-gsm8k  [DONE]\n  failed\n\nexp_001_eval_3B_d100_v2_para_aligned  [DONE]\n  success\n  Metrics: {\"arc_challenge_para\": 0.8092, \"gsm8k_para\": 0.5833, \"humaneval_para_pass1\": 0.1154, \"mmlu_para\": 0.659}\n\nexp_001_eval_3B_d000_v2_aligned  [DONE]\n  success\n  Metrics: {\"arc_challenge\": 0.8183, \"gsm8k\": 0.3525, \"humaneval_pass@1\": 0.0976, \"mmlu\": 0.6295}\n\nexp_001_eval_05B_d100_s123_aligned  [DONE]\n  success\n  Metrics: {\"arc_challenge_accuracy\": 0.3669, \"arc_challenge_correct\": 430, \"arc_challenge_total\": 1172, \"gsm8k_accuracy\": 0.3798, \"gsm8k_correct\": 501, \"gsm8k_total\": 1319, \"humaneval_pass_at_1\": 0.1037, \"humaneval_total\": 164, \"mmlu_accuracy\": 0.3058, \"mmlu_correct\": 4294, \"mmlu_total\": 14042}\n\nexp_001_eval_05B_d025_aligned_v2  [DONE]\n  success\n  Metrics: {\"arc_challenge\": 0.3199, \"format\": \"paraphrased_aligned\", \"gsm8k\": 0.3114, \"humaneval_pass1\": 0.1923, \"mmlu\": 0.2835}\n\nexp_001_eval_15B_d025_aligned  [DONE]\n  success\n  Metrics: {\"arc_challenge\": 0.7688, \"gsm8k\": 0.6535, \"humaneval_pass1\": 0.2256, \"mmlu\": 0.5902}\n\nexp_001_eval_05B_d005_para_aligned  [DONE]\n  success\n  Metrics: {\"arc_challenge\": 0.33, \"arc_correct\": 230, \"arc_total\": 697, \"gsm8k\": 0.2588, \"gsm8k_correct\": 59, \"gsm8k_total\": 228, \"humaneval\": 0, \"humaneval_correct\": 0, \"humaneval_total\": 26, \"mmlu\": 0.3548, \"mmlu_correct\": 2340, \"mmlu_total\": 6596}\n\nexp_001_eval_15B_d025_para_aligned  [DONE]\n  success\n  Metrics: {\"arc_challenge\": 0.766, \"gsm8k\": 0.539, \"humaneval\": 0.154, \"mmlu\": 0.618}\n\nexp_001_eval_3B_d100_para_aligned  [DONE]\n  success\n  Metrics: {\"arc_challenge\": 0.828, \"gsm8k\": 0.614, \"mmlu\": 0.676}\n\nexp_006_pooled_gsm8k_v1  [DONE]\n  failed\n\nexp_001_eval_15B_aligned_batch  [DONE]\n  success\n  Metrics: {\"arc\": {\"d000_orig\": 0.7722, \"d000_para\": 0.7547, \"d005_orig\": 0.7688, \"d005_para\": 0.7532, \"d100_orig\": 0.7688, \"d100_para\": 0.7661}, \"gsm8k\": {\"d000_orig\": 0.6543, \"d000_para\": 0.557, \"d005_orig\": 0.6482, \"d005_para\": 0.5439, \"d100_orig\": 0.6497, \"d100_para\": 0.5526}, \"humaneval\": {\"d000_orig\": 0\n\nexp_006_irt_05B_gsm8k  [DONE]\n  success\n  Metrics: {\"baselines_mae\": {\"B0_raw\": 0.0034, \"B2_2pl_gamma\": 0.3202, \"B3_vanilla_4pl\": 0.0123, \"B4_linear_regression\": 0.003, \"B6_dcr_fuzzy\": 0.2634, \"IRT_4pl_gamma\": 0.0195}, \"delta_fix_applied\": true, \"joint_divergences\": 0, \"joint_ess\": 956.4, \"joint_gamma\": 0.3463, \"joint_gamma_ci\": [-0.65, 1.4], \"joint\n\nexp_001_eval_15B_d100_aligned  [DONE]\n  success\n  Metrics: {\"arc_challenge_accuracy\": 0.7688, \"gsm8k_accuracy\": 0.6497, \"humaneval_correct\": 50, \"humaneval_pass_rate\": 0.3049, \"humaneval_total\": 164, \"mmlu_accuracy\": 0.5933}\n\nexp_001_eval_15B_d005_aligned_v2  [DONE]\n  success\n  Metrics: {\"arc_challenge\": 0.7688, \"gsm8k\": 0.6482, \"humaneval_pass_at_1\": 0.25, \"mmlu\": 0.5852}\n\nexp_001_eval_05B_d100_aligned_v4  [DONE]\n  success\n  Metrics: {\"arc_challenge\": 0.2944, \"arc_delta_vs_d000\": -0.1749, \"gsm8k\": 0.3654, \"humaneval_delta_vs_d000\": -0.1098, \"humaneval_pass_at_1\": 0, \"mmlu\": 0.2334, \"mmlu_delta_vs_d000\": -0.1645}\n\nexp_001_eval_3B_d005_aligned  [DONE]\n  success\n  Metrics: {\"arc_challenge\": 0.829, \"gsm8k\": 0.208, \"humaneval_pass_at_1\": 0.146, \"mmlu\": 0.634}\n\nexp_001_eval_05B_d025_aligned  [DONE]\n  success\n  Metrics: {\"ARC\": 32.51, \"GSM8K\": 36.62, \"HumanEval\": \"missing - process exited before 4th benchmark\", \"MMLU\": 28.03}\n\nexp_008_signal_survival  [DONE]\n  success\n  Metrics: {\"S1_d000_arc\": 0.427, \"S1_d000_gsm8k\": 0.5502, \"S1_d000_mmlu\": 0.5049, \"S1_d005_arc\": 0.995, \"S1_d005_gsm8k\": 0.9882, \"S1_d005_mmlu\": 0.953, \"S1_d100_arc\": 0.501, \"S1_d100_gsm8k\": 0.4127, \"S1_d100_mmlu\": 0.4943, \"S2_d005_arc\": 0.4659, \"S2_d005_gsm8k\": 0.4649, \"S2_d005_mmlu\": 0.4655, \"S4_d005_arc\": \n\nexp_001_eval_3B_d100_aligned  [DONE]\n  success\n  Metrics: {\"arc_challenge_accuracy\": 0.8396, \"gsm8k_exact_match\": 0.6967, \"humaneval_pass1\": 0.122, \"mmlu_accuracy\": 0.6417}\n\nexp_001_eval_05B_d005_aligned  [DONE]\n  success\n  Metrics: {\"d005_aligned_arc\": 0.3285, \"d005_aligned_gsm8k\": 0.3624, \"d005_aligned_humaneval\": 0.0793, \"d005_aligned_mmlu\": 0.3255}\n\nexp_001_eval_05B_aligned_batch  [DONE]\n  failed\n  Metrics: {\"d000_aligned_arc\": 0.4693, \"d000_aligned_gsm8k\": 0.3692, \"d000_aligned_humaneval\": 0.1098, \"d000_aligned_mmlu\": 0.3979, \"d000_para_aligned_arc\": 0.4792, \"d000_para_aligned_gsm8k\": 0.2807, \"d000_para_aligned_humaneval\": 0.1154, \"d000_para_aligned_mmlu\": 0.4428, \"d005_aligned_arc\": 0.3285, \"d005_ali\n\nexp_001_eval_05B_d005  [DONE]\n  success\n  Metrics: {\"arc_challenge\": 0.2858, \"arc_correct\": 335, \"arc_total\": 1172, \"gsm8k\": 0.3601, \"gsm8k_correct\": 475, \"gsm8k_total\": 1319, \"humaneval_correct\": 13, \"humaneval_pass1\": 0.0793, \"humaneval_total\": 164, \"mmlu\": 0.2929, \"mmlu_correct\": 4113, \"mmlu_total\": 14042}\n\nexp_001_eval_3B_d000_aligned  [DONE]\n  success\n  Metrics: {\"arc_challenge_accuracy\": 0.8276, \"gsm8k_exact_match\": 0.1198, \"humaneval_pass_at_1\": 0.1159, \"mmlu_accuracy\": 0.634}\n\nexp_001_eval_15B_d100_s42  [DONE]\n  success\n  Metrics: {\"arc_challenge_accuracy\": 0.7688, \"arc_challenge_correct\": 901, \"arc_challenge_total\": 1172, \"gsm8k_correct\": 857, \"gsm8k_exact_match\": 0.6497, \"gsm8k_total\": 1319, \"humaneval_correct\": 50, \"humaneval_pass_at_1\": 0.3049, \"humaneval_total\": 164, \"mmlu_accuracy\": 0.5933, \"mmlu_correct\": 8331, \"mmlu_t\n\nexp_001_eval_3B_raw_gen  [DONE]\n  success\n  Metrics: {\"gsm8k\": 0.605, \"humaneval\": 0}\n\nexp_001_eval_05B_raw  [DONE]\n  success\n  Metrics: {\"arc_challenge\": 0.2261, \"gsm8k\": 0.1592, \"humaneval\": \"incomplete (hung at 51/164)\", \"mmlu\": 0.2302}\n\nexp_001_eval_05B_d100_v5  [DONE]\n  success\n  Metrics: {\"arc_challenge\": 0.227, \"gsm8k\": 0.3571, \"humaneval_pass1\": 0.0854, \"mmlu\": 0.2322}\n\nexp_001_eval_05B_d000_s42_v5  [DONE]\n  success\n  Metrics: {\"arc_challenge\": 0.378, \"gsm8k\": 0.3647, \"humaneval\": 0.1098, \"mmlu\": 0.4049}\n\nexp_001_eval_3B_d000_s42  [DONE]\n  success\n  Metrics: {\"arc\": 0.822, \"gsm8k\": 0.117, \"humaneval\": 0.116, \"mmlu\": 0.634}\n\nexp_001_eval_3B_d000_s123  [DONE]\n  success\n  Metrics: {\"arc_challenge_accuracy\": 0.8294, \"gsm8k_exact_match\": 0.1759, \"humaneval_pass_at_1\": 0.0854, \"mmlu_accuracy\": 0.6362}\n\nexp_001_eval_15B_d000_s123  [DONE]\n  success\n  Metrics: {\"arc_challenge\": 0.7662, \"gsm8k\": 0.6331, \"humaneval_pass@1\": 0.1707, \"mmlu\": 0.5762}\n\nexp_001_eval_15B_d000_s42_v2  [DONE]\n  success\n  Metrics: {\"arc_challenge_accuracy\": 0.7756, \"arc_challenge_correct\": 909, \"arc_challenge_total\": 1172, \"gsm8k_correct\": 840, \"gsm8k_exact_match\": 0.6368, \"gsm8k_total\": 1319, \"humaneval_correct\": 21, \"humaneval_pass_at_1\": 0.128, \"humaneval_total\": 164, \"mmlu_accuracy\": 0.5753, \"mmlu_correct\": 8079, \"mmlu_to\n\nexp_001_eval_05B_d000_s123  [DONE]\n  success\n  Metrics: {\"arc_challenge_accuracy\": 0.3976, \"gsm8k_exact_match\": 0.3404, \"humaneval_pass_at_1\": 0.1037, \"mmlu_accuracy\": 0.4182}\n\nexp_001_sft_injection  [DONE]\n  success\n  Metrics: {\"arc_qc_pass\": 697, \"arc_qc_rate\": 0.595, \"arc_total\": 1172, \"gsm8k_qc_pass\": 228, \"gsm8k_qc_rate\": 0.173, \"gsm8k_total\": 1319, \"humaneval_total\": 164, \"mmlu_qc_pass\": 6596, \"mmlu_qc_rate\": 0.47, \"mmlu_total\": 14042}",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "565e42fb-6765-465b-953d-8b0bf1ab55e2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "a95a1f6e-644c-4d12-abb6-01351d2cbf40",
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
  "leafUuid": "4d160ac0-125f-47ee-bb71-aa3944fb09f3",
  "sessionId": "a95a1f6e-644c-4d12-abb6-01351d2cbf40"
}
```

---

### Runtime record

_source line 51_

```json
{
  "type": "ai-title",
  "aiTitle": "Verify GSM8K appendix data and prepare LLaMA-3 paper sections",
  "sessionId": "a95a1f6e-644c-4d12-abb6-01351d2cbf40"
}
```

---

### Assistant

_source line 52 · 2026-05-21T11:09:37.221Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a comprehensive view. Let me extract the key GSM8K data points for the 7B+ model families that are relevant to the appendix. Let me also look for Phi-4 d100 GSM8K specifically.

From the registry data, the relevant GSM8K experiments for the appendix families are:

**Phi-4 GSM8K:**
- `eval_phi4_gsm8k_d000_s0`: DONE, accuracy=84.46%
- `gsm8k_phi4_s123_westd`: DONE, d000=84.31%, d100=83.85%, delta=-0.46pp


- `gsm8k_phi4_s42_westd`: PREPARING (not done)

So Phi-4 d100 GSM8K data exists from s123 (83.85%), but not from s0 or s42. The ROADMAP says "d100=running" which seems to be about s0/s42.

Wait, the ROADMAP says the appendix uses specific seeds. Let me check D206 which says "GSM8K appendix 全部统一 s0 数据". So the appendix uses s0 data.

For Phi-4:
- d000 s0: 84.46% ✅ 

For d100 s0, I don't have the data yet—the only d100 result I can find is from s123 at 83.85%, while the s42 experiment is still preparing. The appendix specifically needs s0 data, so this is a gap I need to fill.

Now I'm checking the other model families for their GSM8K appendix data. Qwen-14B has most of the d000 through d025 results in s0, but I'm still looking for d050 and d100 entries. Looking at the OLMo-2 and Gemma-2 results, I see OLMo-2 has multiple seed variants completed but Gemma-2 shows a failed run with catastrophic forgetting and only a preparing d000 experiment. For the appendix, D206 specifies using unified s0 data across all models with version 37775, so I need to identify which seed convention applies to each model's experiments.

Generating completeness table... I'm noticing some inconsistencies in the data—OLMo-2 shows as running in the roadmap but was excluded in D204, and for Phi-4 I need to verify whether the d100 results are from the s0 seed as required or from s123 instead.

Looking at the GSM8K results, I found Phi-4 d100 with s123 seeds showing 83.85%, but there's no completed s0 experiment in the registry yet. D206 specifies using s0 data, so if that's a hard requirement, then Phi-4 d100 GSM8K is still a gap—though I should clarify whether "s0" in the directive means seed 0 specifically or refers to the base uncontaminated version.

Actually, checking the experiment names more carefully, eval_phi4_gsm8k_d000_s0 does exist and shows 84.46% accuracy, and Qwen-7B's s0 experiment has the full dose curve, so s0 appears to be a designated seed for this appendix. Now I'm compiling the GSM8K appendix status table with the s0 seed results across different model families and contamination levels.

Let me verify whether Qwen-14B actually has d050 data, since the task description marked it as uncertain.  Looking at the registry, I see `eval_qwen14b_gsm8k_d050_s0` is still in PREPARING status, so it hasn't completed yet. The ROADMAP claims Qwen-14B has a complete 5-dose set, but I'm seeing conflicting information—the actual d050 experiment appears to still be running, and the other seed experiments I'm checking show different metrics than what I'd expect. The user marked d050 with a question mark because they don't actually know that value, not because it's missing. Looking at the Qwen-14B experiments I can confirm, I have three of the five doses documented: d000 at 74.98%, d005 at 71.19%, and d025 at 79.30%, but d050 is still unaccounted for despite the roadmap claiming the full 5-dose set is complete. - eval_qwen14b_gsm8k_d050_s0: PREPARING (not done)
- eval_qwen14b_d100_gsm8k_s0: 82.41% ✅

So d050 for Qwen-14B is actually a gap! But the ROADMAP says "complete 5-dose." This is contradictory. Let me check if d050 data might be embedded in another experiment.

Hmm, maybe the ROADMAP was ahead of itself, or d050 is running but listed as PREPARING in the registry. Either way, based on the registry data, Qwen-14B d050 GSM8K s0 is not done, and I'm not finding a completed Phi-4 d100 GSM8K experiment either.

Now looking at the LLaMA-3 paper sections from paper_framing.md, it's designated for W3 to expand the generalizability from 5 to 6 model families. The results would fit into the characterization claim and the main results table, plus the cross-seed analysis sections. I'm mapping out where the LLaMA-3 results fit into the paper structure—the main characterization table showing dose-response patterns, the pattern taxonomy discussion, the vulnerability gradient positioning, and potentially a cross-benchmark appendix if GSM8K evaluation is included.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4d160ac0-125f-47ee-bb71-aa3944fb09f3",
  "isSidechain": false,
  "requestId": "req_011CbFcGRPUwuEYWvrssAxUz",
  "type": "assistant",
  "uuid": "4ec8caa4-78a7-4413-bb83-ab8fa31c41e2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "a95a1f6e-644c-4d12-abb6-01351d2cbf40",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BfbDfVwfpJqrm19Ey1tK3o",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13713,
      "cache_read_input_tokens": 39028,
      "output_tokens": 4571,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13713,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4571,
          "cache_read_input_tokens": 39028,
          "cache_creation_input_tokens": 13713,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13713
          },
          "type": "message"
        }
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

_source line 53 · 2026-05-21T11:09:37.258Z_

Now let me check the Qwen-14B d050 and Phi-4 d100 GSM8K status more carefully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4ec8caa4-78a7-4413-bb83-ab8fa31c41e2",
  "isSidechain": false,
  "requestId": "req_011CbFcGRPUwuEYWvrssAxUz",
  "type": "assistant",
  "uuid": "03afcb06-e535-4391-8043-468b77c877ca",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "a95a1f6e-644c-4d12-abb6-01351d2cbf40",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BfbDfVwfpJqrm19Ey1tK3o",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13713,
      "cache_read_input_tokens": 39028,
      "output_tokens": 4571,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13713,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4571,
          "cache_read_input_tokens": 39028,
          "cache_creation_input_tokens": 13713,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13713
          },
          "type": "message"
        }
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

_source line 54 · 2026-05-21T11:09:47.171Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01AwYN79Mnuu9imQmT6U7AEg`</summary>

```json
{
  "command": "python3 -c \"\nimport json\nwith open('/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/a95a1f6e-644c-4d12-abb6-01351d2cbf40/tool-results/mcp-agent-ml-research-read_registry-1779361661868.txt') as f:\n    data = json.load(f)\nparsed = json.loads(data['result'])\nexps = parsed['data']['experiments']\n\n# Search for phi4 d100 and qwen14b d050 specifically\ntargets = ['phi4_d100', 'phi4_gsm8k_d100', 'qwen14b_d050', 'qwen14b_gsm8k_d050']\nfor k, v in exps.items():\n    for t in targets:\n        if t in k.lower():\n            status = v.get('status','?') if isinstance(v, dict) else '?'\n            metrics = json.dumps(v.get('metrics',{}))[:300] if isinstance(v, dict) and v.get('metrics') else ''\n            print(f'{k}  [{status}]')\n            if metrics:\n                print(f'  Metrics: {metrics}')\n            print()\n\n# Also search for any phi4 eval with d100\nprint('--- All phi4 eval experiments ---')\nfor k, v in exps.items():\n    if 'phi4' in k.lower() and ('eval' in k.lower() or 'gsm8k' in k.lower()):\n        status = v.get('status','?') if isinstance(v, dict) else '?'\n        conclusion = str(v.get('conclusion',''))[:100] if isinstance(v, dict) else ''\n        metrics_str = json.dumps(v.get('metrics',{}))[:200] if isinstance(v, dict) and v.get('metrics') else ''\n        print(f'{k}  [{status}] {conclusion}')\n        if metrics_str:\n            print(f'  {metrics_str}')\n\" 2>&1",
  "description": "Search for Phi-4 d100 and Qwen-14B d050 GSM8K experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "03afcb06-e535-4391-8043-468b77c877ca",
  "isSidechain": false,
  "requestId": "req_011CbFcGRPUwuEYWvrssAxUz",
  "type": "assistant",
  "uuid": "b9a70572-b3b0-42cf-a65f-e3fe69ccef25",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "a95a1f6e-644c-4d12-abb6-01351d2cbf40",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BfbDfVwfpJqrm19Ey1tK3o",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13713,
      "cache_read_input_tokens": 39028,
      "output_tokens": 4571,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13713,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4571,
          "cache_read_input_tokens": 39028,
          "cache_creation_input_tokens": 13713,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13713
          },
          "type": "message"
        }
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

_source line 55 · 2026-05-21T11:09:47.268Z_

<details><summary>↩ Tool result · `toolu_01AwYN79Mnuu9imQmT6U7AEg`</summary>

```text
eval_qwen14b_gsm8k_d050_s0  [PREPARING]

eval_qwen14b_d050_arc_s0  [DONE]
  Metrics: {"arc_accuracy": 0.8635, "correct": 1012, "total": 1172, "delta_from_d000": -4.09, "n3_bootstrap_ci": {"mmlu": {"mean_delta": -15.7, "ci_lower": -24.99, "ci_upper": -10.49, "excludes_zero": true, "deltas": [-24.99, -9.37, -12.74]}, "arc": {"mean_delta": -5.03, "ci_lower": -9.38, "ci_upper": -2.76, "

eval_qwen14b_d050_mmlu_s0  [DONE]
  Metrics: {"mmlu_accuracy": 0.5533, "correct": 7770, "total": 14042}

retrain_qwen14b_d050_s0  [DONE]

exp_001_sft_phi4_d100_s42  [DONE]
  Metrics: {"mean_token_accuracy": 0.7244, "train_loss": 1.191}

--- All phi4 eval experiments ---
eval_phi4_gsm8k_d000_s0  [DONE] success
  {"gsm8k_accuracy": 84.46, "correct": 1114, "total": 1319}
eval_phi4_arc_s0_s42  [DONE] success
  {"phi4_arc_s0": {"d000": 91.81, "d005": 92.58, "d025": 92.58, "d050": 92.83, "d100": 92.32, "delta_d100": 0.51}, "phi4_arc_s42": {"d000": 92.06, "d005": 91.81, "d025": 92.32, "d050": 92.41, "d100": 92
eval_phi4_s0_mmlu  [DONE] success
  {"d000_acc": 0.7643, "d005_acc": 0.7643, "d025_acc": 0.7672, "d050_acc": 0.773, "d100_acc": 0.7695, "delta_d100": 0.0052}
eval_phi4_s123_mmlu  [DONE] success
  {"d000_acc": 76.31, "d005_acc": 75.92, "d025_acc": 77.02, "d050_acc": 77.3, "d100_acc": 78.14, "delta_d100": 1.83}
gsm8k_phi4_s123_westd  [DONE] success
  {"gsm8k_d000": 0.8431, "gsm8k_d100": 0.8385, "gsm8k_delta": -0.0046}
gsm8k_phi4_s42_westd  [PREPARING] 
phase2_eval_gpu0_phi4  [PREPARING] failed
eval_phi4_mmlu_arc_westd_v2  [PREPARING] 
eval_phi4_mmlu_arc_westd  [DONE] failed
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b9a70572-b3b0-42cf-a65f-e3fe69ccef25",
  "isSidechain": false,
  "promptId": "ff132cc0-9ef7-4a70-8848-7ec535292349",
  "type": "user",
  "uuid": "ad2d9155-ec9b-47ba-9062-5a60738316a4",
  "toolUseResult": {
    "stdout": "eval_qwen14b_gsm8k_d050_s0  [PREPARING]\n\neval_qwen14b_d050_arc_s0  [DONE]\n  Metrics: {\"arc_accuracy\": 0.8635, \"correct\": 1012, \"total\": 1172, \"delta_from_d000\": -4.09, \"n3_bootstrap_ci\": {\"mmlu\": {\"mean_delta\": -15.7, \"ci_lower\": -24.99, \"ci_upper\": -10.49, \"excludes_zero\": true, \"deltas\": [-24.99, -9.37, -12.74]}, \"arc\": {\"mean_delta\": -5.03, \"ci_lower\": -9.38, \"ci_upper\": -2.76, \"\n\neval_qwen14b_d050_mmlu_s0  [DONE]\n  Metrics: {\"mmlu_accuracy\": 0.5533, \"correct\": 7770, \"total\": 14042}\n\nretrain_qwen14b_d050_s0  [DONE]\n\nexp_001_sft_phi4_d100_s42  [DONE]\n  Metrics: {\"mean_token_accuracy\": 0.7244, \"train_loss\": 1.191}\n\n--- All phi4 eval experiments ---\neval_phi4_gsm8k_d000_s0  [DONE] success\n  {\"gsm8k_accuracy\": 84.46, \"correct\": 1114, \"total\": 1319}\neval_phi4_arc_s0_s42  [DONE] success\n  {\"phi4_arc_s0\": {\"d000\": 91.81, \"d005\": 92.58, \"d025\": 92.58, \"d050\": 92.83, \"d100\": 92.32, \"delta_d100\": 0.51}, \"phi4_arc_s42\": {\"d000\": 92.06, \"d005\": 91.81, \"d025\": 92.32, \"d050\": 92.41, \"d100\": 92\neval_phi4_s0_mmlu  [DONE] success\n  {\"d000_acc\": 0.7643, \"d005_acc\": 0.7643, \"d025_acc\": 0.7672, \"d050_acc\": 0.773, \"d100_acc\": 0.7695, \"delta_d100\": 0.0052}\neval_phi4_s123_mmlu  [DONE] success\n  {\"d000_acc\": 76.31, \"d005_acc\": 75.92, \"d025_acc\": 77.02, \"d050_acc\": 77.3, \"d100_acc\": 78.14, \"delta_d100\": 1.83}\ngsm8k_phi4_s123_westd  [DONE] success\n  {\"gsm8k_d000\": 0.8431, \"gsm8k_d100\": 0.8385, \"gsm8k_delta\": -0.0046}\ngsm8k_phi4_s42_westd  [PREPARING] \nphase2_eval_gpu0_phi4  [PREPARING] failed\neval_phi4_mmlu_arc_westd_v2  [PREPARING] \neval_phi4_mmlu_arc_westd  [DONE] failed",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "b9a70572-b3b0-42cf-a65f-e3fe69ccef25",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "a95a1f6e-644c-4d12-abb6-01351d2cbf40",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 56 · 2026-05-21T11:10:16.381Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a clear picture. Let me also check if there's a Phi-4 d100 GSM8K s0 experiment somewhere. Looking at the results:

- eval_phi4_gsm8k_d000_s0: DONE, 84.46% (s0 seed)
- gsm8k_phi4_s123_westd: DONE, d000=84.31%, d100=83.85% (s123 seed)
- gsm8k_phi4_s42_westd: PREPARING (s42 seed, not done)


- No eval_phi4_gsm8k_d100_s0 exists

So Phi-4 d100 GSM8K s0 is a gap — only the s123 variant has d100 data at 83.85%. For Qwen-14B d050 GSM8K s0, it's still preparing, which is another gap. The roadmap claims Qwen-14B is complete with 5 doses, but the table only shows d000 and d100 values, not the full set, so there's an inconsistency between what the roadmap says and what's actually documented. Looking at the registry data more carefully, I see we actually have results for d000, d005, d025, and d100, but d050 is stuck in PREPARING status—so that's only 4 out of 5 dosage levels completed despite the roadmap claiming "complete 5-dose." Since the d050 model training finished, the evaluation must be what's holding things up, so I should flag this as incomplete pending that eval result.

For the LLaMA-3 analysis, adding it as a sixth model family directly strengthens the generalization claim against the concern about limited model diversity, and the d000 and d100 results should help validate whether the dosage effects hold across different architectures. would add a row to the main dose-response table.

2. **Table in the paper** showing the 4-pattern taxonomy (Immune / Collapse / V-recovery / Benefit) — LLaMA-3 would be classified into one of these.

3. **Vulnerability gradient discussion** — where LLaMA-3.1-8B Base falls on the baseline ability spectrum.

4. **W3 response in the paper** — directly addressing reviewer concern about limited family count.

5. **GSM8K Cross-Benchmark Transfer Appendix** — if GSM8K eval is also completed for LLaMA-3.

The ROADMAP mentions LLaMA-3 SFT experiments with three variants at different data scales, all marked as recent in the registry. I should verify where these stand in terms of completion.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ad2d9155-ec9b-47ba-9062-5a60738316a4",
  "isSidechain": false,
  "requestId": "req_011CbFcNjFC4T1m9bmCfYCUX",
  "type": "assistant",
  "uuid": "c1bd290b-5cd6-42eb-9ad1-622e567058be",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "a95a1f6e-644c-4d12-abb6-01351d2cbf40",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MdcF4JRAK6Aru9zeDkv42V",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5398,
      "cache_read_input_tokens": 52741,
      "output_tokens": 1576,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5398,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1576,
          "cache_read_input_tokens": 52741,
          "cache_creation_input_tokens": 5398,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5398
          },
          "type": "message"
        }
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

_source line 57 · 2026-05-21T11:10:21.721Z_

<details open><summary>🔧 Tool call — Bash · `toolu_018RF4n8D6hsGvmA6bKYHxge`</summary>

```json
{
  "command": "python3 -c \"\nimport json\nwith open('/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/a95a1f6e-644c-4d12-abb6-01351d2cbf40/tool-results/mcp-agent-ml-research-read_registry-1779361661868.txt') as f:\n    data = json.load(f)\nparsed = json.loads(data['result'])\nexps = parsed['data']['experiments']\n\n# LLaMA-3 experiments\nprint('=== LLaMA-3 experiments ===')\nfor k, v in exps.items():\n    if 'llama3' in k.lower() and 'llama32' not in k.lower():\n        status = v.get('status','?') if isinstance(v, dict) else '?'\n        conclusion = str(v.get('conclusion',''))[:150] if isinstance(v, dict) else ''\n        metrics = json.dumps(v.get('metrics',{}))[:300] if isinstance(v, dict) and v.get('metrics') else ''\n        print(f'{k}  [{status}] {conclusion}')\n        if metrics:\n            print(f'  {metrics}')\n        print()\n\" 2>&1",
  "description": "Check LLaMA-3 experiment status"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c1bd290b-5cd6-42eb-9ad1-622e567058be",
  "isSidechain": false,
  "requestId": "req_011CbFcNjFC4T1m9bmCfYCUX",
  "type": "assistant",
  "uuid": "bcc6ee98-f8bb-4917-8eaa-ab87fab30f10",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "a95a1f6e-644c-4d12-abb6-01351d2cbf40",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MdcF4JRAK6Aru9zeDkv42V",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5398,
      "cache_read_input_tokens": 52741,
      "output_tokens": 1576,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5398,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1576,
          "cache_read_input_tokens": 52741,
          "cache_creation_input_tokens": 5398,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5398
          },
          "type": "message"
        }
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

_source line 58 · 2026-05-21T11:10:21.809Z_

<details><summary>↩ Tool result · `toolu_018RF4n8D6hsGvmA6bKYHxge`</summary>

```text
=== LLaMA-3 experiments ===
sft_llama3_d100_s0  [RUNNING] 

sft_llama3_d025_s0  [RUNNING] 

sft_llama3_d000_s0  [RUNNING] 

sft_llama3_8b_s0_validation  [PREPARING]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bcc6ee98-f8bb-4917-8eaa-ab87fab30f10",
  "isSidechain": false,
  "promptId": "ff132cc0-9ef7-4a70-8848-7ec535292349",
  "type": "user",
  "uuid": "89a6ace8-5a90-4dbb-948a-f9243023e519",
  "toolUseResult": {
    "stdout": "=== LLaMA-3 experiments ===\nsft_llama3_d100_s0  [RUNNING] \n\nsft_llama3_d025_s0  [RUNNING] \n\nsft_llama3_d000_s0  [RUNNING] \n\nsft_llama3_8b_s0_validation  [PREPARING]",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "bcc6ee98-f8bb-4917-8eaa-ab87fab30f10",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "a95a1f6e-644c-4d12-abb6-01351d2cbf40",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 59_

```json
{
  "type": "last-prompt",
  "leafUuid": "89a6ace8-5a90-4dbb-948a-f9243023e519",
  "sessionId": "a95a1f6e-644c-4d12-abb6-01351d2cbf40"
}
```

---

### Runtime record

_source line 60_

```json
{
  "type": "ai-title",
  "aiTitle": "Verify GSM8K appendix data and prepare LLaMA-3 paper sections",
  "sessionId": "a95a1f6e-644c-4d12-abb6-01351d2cbf40"
}
```

---

### Assistant

_source line 61 · 2026-05-21T11:10:49.565Z_

Now I have the full picture. Here's the output:

---

## 1. GSM8K Appendix 数据完整性表（s0 seed, 37775 evaluate.py — D206）

| Family | d000 | d005 | d025 | d050 | d100 | 状态 |
|--------|------|------|------|------|------|------|
| **Qwen-7B** | 73.31% ✅ | 78.32% ✅ | 78.24% ✅ | 79.38% ✅ | 81.20% ✅ | **完整 5-dose** |
| **Qwen-14B** | 74.98% ✅ | 71.19% ✅ | 79.30% ✅ | **GAP** (PREPARING) | 82.41% ✅ | **4/5** |
| **Phi-4** | 84.46% ✅ | — | — | — | **GAP** | **1/5** |
| OLMo-2 | ❌ 排除 (D204: evaluate.py 版本不一致) | — | — | — | — | **排除** |
| Gemma-2 | 17.82% ⚠️ CoT 崩塌 | — | — | — | — | **排除** |

**Gaps:**
- **Qwen-14B d050 GSM8K s0**: 模型存在（retrain_qwen14b_d050_s0 DONE），MMLU/ARC eval 已完成，但 GSM8K eval 仍 PREPARING
- **Phi-4 d100 GSM8K s0**: 无 s0 数据。s123 数据存在（83.85%, gsm8k_phi4_s123_westd），s42 仍 PREPARING

注：ROADMAP 标 Qwen-14B "✅ 完整 5-dose" 与 registry 矛盾（d050 PREPARING）。需确认 d050 是否已完成但未注册。

## 2. Phi-4 d100 GSM8K 状态确认

**s0: 无数据（GAP）。s123: 83.85%（Δ = -0.46pp vs d000=84.31%）。s42: PREPARING。**

如果 appendix 统一用 s0（D206），Phi-4 d100 是必须补的 gap。但 s123 数据显示 Phi-4 GSM8K 基本 immune（-0.46pp），与 MMLU pattern 一致。

## 3. LLaMA-3 结果预计写入的论文章节

LLaMA-3.1-8B Base 当前状态：SFT 训练中（sft_llama3_d000_s0 / d025 / d100 均 RUNNING），eval 尚未开始。

预计写入章节：

| 章节 | 内容 | 优先级 |
|------|------|--------|
| **§4 Results / Claim 1 Characterization** | 主表添加第 6 行（LLaMA-3 dose-response pattern 分类）| 核心——直接回应 W3 |
| **§4 Vulnerability gradient 讨论** | LLaMA-3.1-8B Base 的 baseline MMLU 决定它在 gradient 上的位置 | 核心 |
| **Table 1（主结果表）** | 5→6 families，添加 d000/d100 Δ | 核心 |
| **§5 Discussion / Generalizability** | "6 independent families" 替代 "5 families"，增强泛化论证 | 重要 |
| **Appendix: GSM8K Cross-Benchmark** | 如果时间允许跑 LLaMA-3 GSM8K eval | 可选 |
| **Limitations** | family count 从 5→6 可弱化 "limited families" caveat | 次要 |

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "89a6ace8-5a90-4dbb-948a-f9243023e519",
  "isSidechain": false,
  "requestId": "req_011CbFcRHK4WxKhN24PkjYSz",
  "type": "assistant",
  "uuid": "6aa84f3e-272f-4550-bd61-dffaaf080739",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "a95a1f6e-644c-4d12-abb6-01351d2cbf40",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B1YYe5NPkSzbvXXV7afb7d",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1675,
      "cache_read_input_tokens": 58139,
      "output_tokens": 1087,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1675,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1087,
          "cache_read_input_tokens": 58139,
          "cache_creation_input_tokens": 1675,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1675
          },
          "type": "message"
        }
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
  "leafUuid": "6aa84f3e-272f-4550-bd61-dffaaf080739",
  "sessionId": "a95a1f6e-644c-4d12-abb6-01351d2cbf40"
}
```

---

### Runtime record

_source line 63_

```json
{
  "type": "ai-title",
  "aiTitle": "Verify GSM8K appendix data and prepare LLaMA-3 paper sections",
  "sessionId": "a95a1f6e-644c-4d12-abb6-01351d2cbf40"
}
```

---
