# Research conversation: <project_context> # 项目: contamcal-irt-calibration ## 运行环境 - 服务器名: cqa1-21977 - SSH 连接命令: ssh connect.cqa1.seetacloud.com

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 30
- **Recorded user turns:** 1
- **Tool calls:** 5
- **Original source:** `logs/chats/exported-trajectories/account-2/b4bb6832-311d-424b-8b19-57bd3d213f37.jsonl`
- **Structured JSON:** [`945f2df8ba56426f128c.json`](../../sessions/94/945f2df8ba56426f128c.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-18T07:07:25.287Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-18T07:07:25.287Z",
  "sessionId": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "content": "&lt;project_context>\n# 项目: contamcal-irt-calibration\n\n## 运行环境\n- 服务器名: cqa1-21977\n- SSH 连接命令: ssh connect.cqa1.seetacloud.com  # 必须用此命令，~/.ssh/config 自动应用密钥和跳板机，禁止用裸 IP\n- 项目代码根目录: /root/contamcal-irt-calibration\n\n## ⚠️ 活跃约束（必须遵守）\n\n- **C001**: 提交实验前必须检查目标 GPU 上是否已有同类进程（nvidia-smi 查 PID + 对比 output dir），有则不提交（原因：GPU 2 因重复提交导致 4 次进程冲突和数据污染。on_failed hook 触发的 worker 和手动提交都不做查重。）\n- **C002**: 提交 GPU 任务前必须用 nvidia-smi 确认目标 GPU 空闲，不得仅依赖 get_project_resource_usage 判断（原因：resource_usage 工具因 PID/tmux 不匹配严重误报（cuda:0/2/3 活跃但报 idle），已导致调度风险。Reviewer 2026-05-14 确认。）\n- **C003**: 标记实验为 failed 时必须同时 kill 所有关联 GPU 进程；submit 新任务到 GPU 前必须先 nvidia-smi + ps 确认该 GPU 无残留进程（原因：GPU 2 两次出现\"标 failed 不 kill 进程\"导致新旧进程冲突、数据腐败风险。v3 标 failed 但 2 个子进程存活，v4 提交时未检查，造成三进程竞争同一 output-dir。）\n- **C004**: 提交 GPU 实验时必须在命令中显式设置 CUDA_VISIBLE_DEVICES=N，不依赖默认行为（原因：已两次出现声明 cuda:3 实际跑在 cuda:0 的事故（PID 498153、PID 513900/513826），根因是 tmux/nohup 启动时未显式传递 CUDA_VISIBLE_DEVICES。）\n- **C005**: 禁止在 cuda:4 有 SFT 训练运行时提交 compute_signals 任务到 cuda:4；signals_3B 任务必须等目标 GPU 独占空闲后再提交（原因：cuda:4 三次出现未授权 compute_signals 进程与 d000_v3 SFT 抢显存（PID 590509, 605267, 607648）。来源疑为旧 session Worker 或 auto-loop 触发的 signals 批量任务。必须杜绝 signals 任务与 SFT 训练共享 GPU。）\n- **C006**: 禁止在 alpha=16 checkpoint 上启动任何任务（训练/eval/信号计算）。废弃目录黑名单：Qwen2.5-3B_d000_s42, Qwen2.5-3B_d000_v2_s42, Qwen2.5-3B_d005_s42, Qwen2.5-3B_d025_s42, Qwen2.5-3B_d100_s42（不含 _v3/_v2 等 alpha=32 重训版本）。启动前必须 cat adapter_config.json | grep lora_alpha 确认 =32。（原因：D055/D076 决定全部标准化到 alpha=32 + lr=5e-5。本 session 已 4 次发现 Worker 在废弃 alpha=16 checkpoint 上启动信号计算，每次 kill 后又重启新进程，累计浪费 10+ GPU-hours。根因是 Worker prompt 中缺少废弃 checkpoint 黑名单。） [来自 D055]\n- **C007**: GPU 释放后优先级：0.5B s123 signals > 1.5B s123 signals > d100_a32_s123 signals > 其他。0.5B/1.5B s123 全部完成前不分配 GPU 给低优先级信号任务。（原因：0.5B/1.5B s123 合计 +8 respondents 是达到 N≥16 IRT 门槛的最高 ROI 路径，d100 仅 +1。Reviewer 第三次确认优先级倒挂风险。）\n- **C008**: IRT 模型选择规则：2PL+γ 为默认（robust，N<16 可用）；4PL+γ 仅当 N≥16 且 benchmark 为 MCQ format 时使用。N<16 时 4PL 的 c/d 参数不可识别，会导致 PPP=0 和校准恶化。（原因：ARC N=5 使用 4PL+γ 导致 PPP=0.000、MAE 从 0.004 恶化到 0.068（过参数化）。Director 指令要求建立模型选择规则供后续所有 IRT fitting 使用。）\n\n\n## 环境搭建\n连接服务器后先调 `detect_image` 检测是否为预置镜像。如果匹配，跳过基础环境搭建，只装项目特有依赖。已预装的包不要重复安装。\n\n## 输出风格\n回复简洁直接。只输出执行结果和必要信息，不要解释过程、不要客套、不要给未被要求的建议。\n&lt;/project_context>\n## 任务：搜索 2025-2026 前沿开源 base models (7B-14B)\n\n### 背景\n我们的论文 \"Does SFT-Injected Benchmark Contamination Need Calibration?\" 需要 5 个 model families 做跨家族验证。当前选择包含 2024 年的旧模型（Llama 3.1, Mistral v0.3, Qwen 2.5），审稿人可能质疑模型过时。需要搜索 2025-2026 年最新发布的开源 base models 作为替代。\n\n### 约束\n- 参数范围: **7B-14B**（我们的 GPU 是 96GB，可以跑 bf16 LoRA）\n- 必须是 **base models**（不是 instruct/chat 版本），因为我们要做 controlled SFT contamination injection\n- 需要 HuggingFace 上可下载\n- 最好不是 gated model（避免 license 审批问题）\n- 需要 5 个不同 model families 做跨家族验证\n\n### 搜索关键词\n请用 WebSearch 搜索以下关键词（每个都搜）:\n1. \"best open source LLM 2025 2026 base model\"\n2. \"latest base models huggingface 2025\"\n3. \"Llama 4 base model release\"\n4. \"Qwen 3 base model\"\n5. \"Mistral latest base model 2025\"\n6. \"Gemma 3 base model\"\n7. \"new open source LLM families 2025 2026\"\n8. \"OLMo 2 base model\"\n9. \"DeepSeek V3 base model\"\n10. \"Phi-4 base model\"\n\n### 需要收集的信息（每个候选模型）\n- 模型全名 + HuggingFace repo ID\n- 参数量\n- 发布日期\n- 是否 gated (需要 license agreement)\n- 是否有 base (非-instruct) 版本\n- HuggingFace 下载链接\n- 训练数据量/token 数\n- 与同参数量前代模型的性能对比（如有）\n\n### 产出格式\n\n请产出一个 markdown 表格，包含所有候选模型，按推荐度排序。\n\n然后给出你的推荐：\n1. **5 个最佳候选组合**（替换当前矩阵中的模型），理由\n2. 哪些模型可以直接替换 Llama-3.1-8B（被取消的那个）\n3. 是否有 Qwen 3 发布（如果有，是否应替换 Qwen 2.5）\n\n### 时间约束\n30 分钟内完成搜索和推荐。"
}
```

---

### Runtime record

_source line 2 · 2026-05-18T07:07:25.292Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-18T07:07:25.292Z",
  "sessionId": "b4bb6832-311d-424b-8b19-57bd3d213f37"
}
```

---

## Round 1

28 recorded events

### User

_source line 3 · 2026-05-18T07:07:25.331Z_

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


## 环境搭建
连接服务器后先调 `detect_image` 检测是否为预置镜像。如果匹配，跳过基础环境搭建，只装项目特有依赖。已预装的包不要重复安装。

## 输出风格
回复简洁直接。只输出执行结果和必要信息，不要解释过程、不要客套、不要给未被要求的建议。
&lt;/project_context>
## 任务：搜索 2025-2026 前沿开源 base models (7B-14B)

### 背景
我们的论文 "Does SFT-Injected Benchmark Contamination Need Calibration?" 需要 5 个 model families 做跨家族验证。当前选择包含 2024 年的旧模型（Llama 3.1, Mistral v0.3, Qwen 2.5），审稿人可能质疑模型过时。需要搜索 2025-2026 年最新发布的开源 base models 作为替代。

### 约束
- 参数范围: **7B-14B**（我们的 GPU 是 96GB，可以跑 bf16 LoRA）
- 必须是 **base models**（不是 instruct/chat 版本），因为我们要做 controlled SFT contamination injection
- 需要 HuggingFace 上可下载
- 最好不是 gated model（避免 license 审批问题）
- 需要 5 个不同 model families 做跨家族验证

### 搜索关键词
请用 WebSearch 搜索以下关键词（每个都搜）:
1. "best open source LLM 2025 2026 base model"
2. "latest base models huggingface 2025"
3. "Llama 4 base model release"
4. "Qwen 3 base model"
5. "Mistral latest base model 2025"
6. "Gemma 3 base model"
7. "new open source LLM families 2025 2026"
8. "OLMo 2 base model"
9. "DeepSeek V3 base model"
10. "Phi-4 base model"

### 需要收集的信息（每个候选模型）
- 模型全名 + HuggingFace repo ID
- 参数量
- 发布日期
- 是否 gated (需要 license agreement)
- 是否有 base (非-instruct) 版本
- HuggingFace 下载链接
- 训练数据量/token 数
- 与同参数量前代模型的性能对比（如有）

### 产出格式

请产出一个 markdown 表格，包含所有候选模型，按推荐度排序。

然后给出你的推荐：
1. **5 个最佳候选组合**（替换当前矩阵中的模型），理由
2. 哪些模型可以直接替换 Llama-3.1-8B（被取消的那个）
3. 是否有 Qwen 3 发布（如果有，是否应替换 Qwen 2.5）

### 时间约束
30 分钟内完成搜索和推荐。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "04205c35-fa25-4f0b-9c44-5def633915cd",
  "type": "user",
  "uuid": "65163f35-bb08-44c6-8181-ed0dd1c30042",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-18T07:07:25.330Z_

```json
{
  "parentUuid": "65163f35-bb08-44c6-8181-ed0dd1c30042",
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
  "uuid": "16c579ac-b840-4e85-b31a-634c98629a60",
  "timestamp": "2026-05-18T07:07:25.330Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-18T07:07:25.330Z_

```json
{
  "parentUuid": "16c579ac-b840-4e85-b31a-634c98629a60",
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
  "uuid": "415ed3d4-500a-45f3-99c5-f1b0243ca46f",
  "timestamp": "2026-05-18T07:07:25.330Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6 · 2026-05-18T07:07:25.330Z_

```json
{
  "parentUuid": "415ed3d4-500a-45f3-99c5-f1b0243ca46f",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "2e02a123-ab8f-4f73-848f-e72b743e6229",
  "timestamp": "2026-05-18T07:07:25.330Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "b4bb6832-311d-424b-8b19-57bd3d213f37",
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
  "aiTitle": "Search 2025-2026 base models for cross-family validation",
  "sessionId": "b4bb6832-311d-424b-8b19-57bd3d213f37"
}
```

---

### Assistant

_source line 8 · 2026-05-18T07:07:29.695Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to search for the latest open-source base models (7B-14B) from 2025-2026 for their contamination calibration paper. They need 5 model families for cross-family validation. Let me launch parallel web searches to gather this information efficiently.

Let me first load the WebSearch tool, then launch multiple search agents in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2e02a123-ab8f-4f73-848f-e72b743e6229",
  "isSidechain": false,
  "requestId": "req_011Cb9cU2qj2VZZMr8VY8Eei",
  "type": "assistant",
  "uuid": "64425b0b-bed5-4d3d-ab4a-921515c4ce87",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U4EJjVYM9HbZTpmY5NrpAh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14117,
      "cache_read_input_tokens": 11841,
      "output_tokens": 171,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14117,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 171,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 14117,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14117
          },
          "type": "message"
        }
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

_source line 9 · 2026-05-18T07:07:29.999Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01SMhtys5MBoFBFVndtm2NYk`</summary>

```json
{
  "query": "select:WebSearch",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "64425b0b-bed5-4d3d-ab4a-921515c4ce87",
  "isSidechain": false,
  "requestId": "req_011Cb9cU2qj2VZZMr8VY8Eei",
  "type": "assistant",
  "uuid": "a2c19ded-8a6d-4d33-99b4-1de8c1356f92",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U4EJjVYM9HbZTpmY5NrpAh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14117,
      "cache_read_input_tokens": 11841,
      "output_tokens": 171,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14117,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 171,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 14117,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14117
          },
          "type": "message"
        }
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

_source line 10 · 2026-05-18T07:07:30.008Z_

<details><summary>↩ Tool result · `toolu_01SMhtys5MBoFBFVndtm2NYk`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "WebSearch"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a2c19ded-8a6d-4d33-99b4-1de8c1356f92",
  "isSidechain": false,
  "promptId": "04205c35-fa25-4f0b-9c44-5def633915cd",
  "type": "user",
  "uuid": "6faeecc4-926a-4726-81e8-3b2dff69c2e4",
  "toolUseResult": {
    "matches": [
      "WebSearch"
    ],
    "query": "select:WebSearch",
    "total_deferred_tools": 22
  },
  "sourceToolAssistantUUID": "a2c19ded-8a6d-4d33-99b4-1de8c1356f92",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 11 · 2026-05-18T07:07:33.061Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me launch parallel web searches for all the keywords the user specified. I'll use multiple agents to search in parallel for efficiency.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6faeecc4-926a-4726-81e8-3b2dff69c2e4",
  "isSidechain": false,
  "requestId": "req_011Cb9cUP87yAYaPYKNLYnYE",
  "type": "assistant",
  "uuid": "96161667-043a-4797-9b74-af40c9154c95",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R2JdnQVstyta5ag8imEWYL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 699,
      "cache_read_input_tokens": 25958,
      "output_tokens": 1180,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 699,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1180,
          "cache_read_input_tokens": 25958,
          "cache_creation_input_tokens": 699,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 699
          },
          "type": "message"
        }
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

_source line 12 · 2026-05-18T07:07:33.702Z_

开始并行搜索 10 个关键词。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "96161667-043a-4797-9b74-af40c9154c95",
  "isSidechain": false,
  "requestId": "req_011Cb9cUP87yAYaPYKNLYnYE",
  "type": "assistant",
  "uuid": "6c4eff74-8844-4251-b4ac-072737428fa3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R2JdnQVstyta5ag8imEWYL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 699,
      "cache_read_input_tokens": 25958,
      "output_tokens": 1180,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 699,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1180,
          "cache_read_input_tokens": 25958,
          "cache_creation_input_tokens": 699,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 699
          },
          "type": "message"
        }
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

_source line 13 · 2026-05-18T07:07:38.445Z_

<details open><summary>🔧 Tool call — Agent · `toolu_019GEYgwrqvsAqC9HcwLnZ7s`</summary>

```json
{
  "description": "Search batch 1: general + HF",
  "subagent_type": "general-purpose",
  "prompt": "You are researching the latest open-source base LLMs (7B-14B parameters) released in 2025-2026 for an academic paper. Run the following 3 web searches and compile ALL results with as much detail as possible. For each model found, note: full name, HuggingFace repo ID, parameter count, release date, whether it's gated, whether a base (non-instruct) version exists, training data size if mentioned, and benchmark performance if mentioned.\n\nSearch 1: \"best open source LLM 2025 2026 base model\"\nSearch 2: \"latest base models huggingface 2025\"\nSearch 3: \"new open source LLM families 2025 2026\"\n\nReturn ALL findings in a structured format. Be thorough - list every model you find in the 7B-14B range."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6c4eff74-8844-4251-b4ac-072737428fa3",
  "isSidechain": false,
  "requestId": "req_011Cb9cUP87yAYaPYKNLYnYE",
  "type": "assistant",
  "uuid": "45f9c1d2-c26b-4532-b966-e7ffa02a770c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R2JdnQVstyta5ag8imEWYL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 699,
      "cache_read_input_tokens": 25958,
      "output_tokens": 1180,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 699,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1180,
          "cache_read_input_tokens": 25958,
          "cache_creation_input_tokens": 699,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 699
          },
          "type": "message"
        }
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

_source line 14 · 2026-05-18T07:07:40.452Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01UUx3h1Z4EHFrb7q9YJpLgR`</summary>

```json
{
  "description": "Search batch 2: Llama + Qwen + Mistral",
  "subagent_type": "general-purpose",
  "prompt": "You are researching the latest open-source base LLMs (7B-14B parameters) released in 2025-2026 for an academic paper. Run the following 3 web searches and compile ALL results with as much detail as possible. For each model found, note: full name, HuggingFace repo ID, parameter count, release date, whether it's gated, whether a base (non-instruct) version exists, training data size if mentioned, and benchmark performance if mentioned.\n\nSearch 1: \"Llama 4 base model release\"\nSearch 2: \"Qwen 3 base model\"\nSearch 3: \"Mistral latest base model 2025\"\n\nReturn ALL findings in a structured format. Be thorough - list every model you find in the 7B-14B range."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "45f9c1d2-c26b-4532-b966-e7ffa02a770c",
  "isSidechain": false,
  "requestId": "req_011Cb9cUP87yAYaPYKNLYnYE",
  "type": "assistant",
  "uuid": "98f79d7d-3d0e-4989-bfea-4fbfe0109d7d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R2JdnQVstyta5ag8imEWYL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 699,
      "cache_read_input_tokens": 25958,
      "output_tokens": 1180,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 699,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1180,
          "cache_read_input_tokens": 25958,
          "cache_creation_input_tokens": 699,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 699
          },
          "type": "message"
        }
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

_source line 15 · 2026-05-18T07:07:42.910Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01BPp8oiLtg786D15Msvztwn`</summary>

```json
{
  "description": "Search batch 3: Gemma + OLMo",
  "subagent_type": "general-purpose",
  "prompt": "You are researching the latest open-source base LLMs (7B-14B parameters) released in 2025-2026 for an academic paper. Run the following 3 web searches and compile ALL results with as much detail as possible. For each model found, note: full name, HuggingFace repo ID, parameter count, release date, whether it's gated, whether a base (non-instruct) version exists, training data size if mentioned, and benchmark performance if mentioned.\n\nSearch 1: \"Gemma 3 base model\"\nSearch 2: \"OLMo 2 base model\"\nSearch 3: \"Gemma 3 pretrained model huggingface 2025\"\n\nReturn ALL findings in a structured format. Be thorough."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "98f79d7d-3d0e-4989-bfea-4fbfe0109d7d",
  "isSidechain": false,
  "requestId": "req_011Cb9cUP87yAYaPYKNLYnYE",
  "type": "assistant",
  "uuid": "f98bdbe4-4d54-45ec-8be5-1afad109d931",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R2JdnQVstyta5ag8imEWYL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 699,
      "cache_read_input_tokens": 25958,
      "output_tokens": 1180,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 699,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1180,
          "cache_read_input_tokens": 25958,
          "cache_creation_input_tokens": 699,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 699
          },
          "type": "message"
        }
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

_source line 16 · 2026-05-18T07:07:46.101Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01XSzbYG4aNMXhPUJ8DwFSt1`</summary>

```json
{
  "description": "Search batch 4: DeepSeek + Phi",
  "subagent_type": "general-purpose",
  "prompt": "You are researching the latest open-source base LLMs (7B-14B parameters) released in 2025-2026 for an academic paper. Run the following 3 web searches and compile ALL results with as much detail as possible. For each model found, note: full name, HuggingFace repo ID, parameter count, release date, whether it's gated, whether a base (non-instruct) version exists, training data size if mentioned, and benchmark performance if mentioned.\n\nSearch 1: \"DeepSeek V3 base model\"\nSearch 2: \"Phi-4 base model\"\nSearch 3: \"DeepSeek R2 base model 2025 2026\"\n\nReturn ALL findings in a structured format. Be thorough - list every model you find in the 7B-14B range. Also note if any of these models use MoE architecture (mixture of experts) and what the active parameter count is."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f98bdbe4-4d54-45ec-8be5-1afad109d931",
  "isSidechain": false,
  "requestId": "req_011Cb9cUP87yAYaPYKNLYnYE",
  "type": "assistant",
  "uuid": "faccd5e5-3705-46db-bae1-72dc2de8c36a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R2JdnQVstyta5ag8imEWYL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 699,
      "cache_read_input_tokens": 25958,
      "output_tokens": 1180,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 699,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1180,
          "cache_read_input_tokens": 25958,
          "cache_creation_input_tokens": 699,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 699
          },
          "type": "message"
        }
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
  "leafUuid": "faccd5e5-3705-46db-bae1-72dc2de8c36a",
  "sessionId": "b4bb6832-311d-424b-8b19-57bd3d213f37"
}
```

---

### Runtime record

_source line 18_

```json
{
  "type": "ai-title",
  "aiTitle": "Search 2025-2026 base models for cross-family validation",
  "sessionId": "b4bb6832-311d-424b-8b19-57bd3d213f37"
}
```

---

### Tool result

_source line 19 · 2026-05-18T07:09:24.475Z_

<details><summary>↩ Tool result · `toolu_01BPp8oiLtg786D15Msvztwn`</summary>

```text
Here are all findings compiled in structured format.

---

## Gemma 3 (Google DeepMind)

**Release date:** March 12, 2025 (added to HuggingFace Transformers); public release ~March 25, 2025

**License:** Gemma Terms of Use (custom Google license)

**Gated:** Yes. Requires agreeing to Google's usage license on HuggingFace before downloading.

**Base (pretrained) versions exist:** Yes. All sizes have a `-pt` (pretrained) variant.

| Size | HuggingFace Repo ID | Parameters | Modality | Context Window | Training Tokens | MMLU (base) | HellaSwag (base) |
|------|---------------------|------------|----------|----------------|-----------------|-------------|------------------|
| 1B | `google/gemma-3-1b-pt` | 1B | Text only | 32K | 2T | 38.8% | 62.3 |
| 4B | `google/gemma-3-4b-pt` | 4B | Text + Image | 128K | 4T | 58.1% | 77.2 |
| 12B | `google/gemma-3-12b-pt` | 12B | Text + Image | 128K | 12T | 71.9% | 84.2 |
| 27B | `google/gemma-3-27b-pt` | 27B | Text + Image | 128K | 14T | 76.9% | 85.6 |

**Instruction-tuned counterparts** use the `-it` suffix (e.g., `google/gemma-3-12b-it`).

**Additional notes:**
- 140+ language support
- Trained using knowledge distillation from larger Gemini models
- Trained on TPUv4p, TPUv5p, and TPUv5e hardware
- A 270M text-only variant also exists, trained on 6T tokens
- Gemma 3 4B-IT beats Gemma 2 27B-IT; Gemma 3 27B-IT is comparable to Gemini 1.5 Pro
- Technical report: [arxiv.org/abs/2503.19786](https://arxiv.org/abs/2503.19786)

---

## OLMo 2 (Allen Institute for AI / Ai2)

**License:** Apache 2.0 (fully open, including training data, code, and weights)

**Gated:** No. All models are openly available.

**Base (pretrained) versions exist:** Yes. The base repo IDs below are the pretrained models; instruct/SFT/DPO variants have corresponding suffixes.

| Size | HuggingFace Repo ID | Parameters | Release Date | Training Tokens | MMLU (base) |
|------|---------------------|------------|--------------|-----------------|-------------|
| 1B | `allenai/OLMo-2-0425-1B` | 1B | April 2025 | 4T (+ 50B mid-training) | Not reported in search results |
| 7B | `allenai/OLMo-2-1124-7B` | 7B | November 2024 (updated Dec 31, 2024) | ~4T (Stage 1: 3.9T OLMo-Mix-1124, Stage 2: 50B Dolmino-Mix-1124) | 63.7 |
| 13B | `allenai/OLMo-2-1124-13B` | 13B | November 2024 | Up to 5T | 67.5 |
| 32B | `allenai/OLMo-2-0325-32B` | 32B | March 2025 | Up to 6T | Not reported in search results |

**Instruct variants:**
- `allenai/OLMo-2-1124-7B-Instruct`
- `allenai/OLMo-2-1124-13B-Instruct`
- `allenai/OLMo-2-0325-32B-Instruct`
- `allenai/OLMo-2-0425-1B-Instruct`

**Additional OLMo 2 details:**
- Modality: Text only
- Training data: OLMo-Mix-1124 (Stage 1) + Dolmino-Mix-1124 (Stage 2, mid-training)
- 7B model: trained for ~1 epoch on 3.9T tokens, then 3 runs of 50B token mid-training merged via model souping
- 9-point MMLU increase over original OLMo 7B
- OLMo 2 7B outperforms Llama 3.1 8B on English academic benchmarks
- OLMo 2 13B surpasses Qwen 2.5 7B despite fewer training FLOPs
- OLMo 2 32B is described as "the first fully-open model to outperform GPT-3.5-Turbo and GPT-4o mini" on multi-skill academic benchmarks
- ARC scores: improved from 80.2 to 83.5 for 13B
- Data cutoff: December 2023
- Technical report: [arxiv.org/abs/2501.00656](https://arxiv.org/abs/2501.00656)
- Also note: Ai2 has released **OLMo 3** (`allenai/Olmo-3-1125-32B`) and **OLMo 3.1** (`allenai/Olmo-3.1-32B-Think`), though these are outside your 7B-14B scope

---

## Summary: Models in the 7B-14B Range

For the specific 7B-14B parameter range relevant to the paper:

| Model | Repo ID | Params | Gated | License | Training Data | MMLU |
|-------|---------|--------|-------|---------|---------------|------|
| Gemma 3 12B PT | `google/gemma-3-12b-pt` | 12B | Yes | Gemma ToU | 12T tokens | 71.9% |
| OLMo 2 7B | `allenai/OLMo-2-1124-7B` | 7B | No | Apache 2.0 | ~4T tokens | 63.7% |
| OLMo 2 13B | `allenai/OLMo-2-1124-13B` | 13B | No | Apache 2.0 | ~5T tokens | 67.5% |

OLMo 2 is the stronger choice for reproducibility research since it is fully open (Apache 2.0, open training data and code). Gemma 3 12B has stronger benchmark numbers but is gated and uses a custom license.

---

Sources:
- [Gemma 3 HuggingFace Docs](https://huggingface.co/docs/transformers/model_doc/gemma3)
- [Welcome Gemma 3 Blog Post](https://huggingface.co/blog/gemma3)
- [Gemma 3 Release Collection](https://huggingface.co/collections/google/gemma-3-release)
- [google/gemma-3-12b-pt](https://huggingface.co/google/gemma-3-12b-pt)
- [google/gemma-3-4b-pt](https://huggingface.co/google/gemma-3-4b-pt)
- [google/gemma-3-27b-pt](https://huggingface.co/google/gemma-3-27b-pt)
- [google/gemma-3-1b-pt](https://huggingface.co/google/gemma-3-1b-pt)
- [Gemma 3 Technical Report (arxiv)](https://arxiv.org/abs/2503.19786)
- [Gemma 3 Model Card (Google)](https://ai.google.dev/gemma/docs/core/model_card_3)
- [allenai/OLMo-2-1124-7B](https://huggingface.co/allenai/OLMo-2-1124-7B)
- [allenai/OLMo-2-1124-13B](https://huggingface.co/allenai/OLMo-2-1124-13B)
- [allenai/OLMo-2-0325-32B](https://huggingface.co/allenai/OLMo-2-0325-32B)
- [allenai/OLMo-2-0425-1B](https://huggingface.co/allenai/OLMo-2-0425-1B)
- [OLMo 2 Collection](https://huggingface.co/collections/allenai/olmo-2)
- [OLMo 2 Blog Post (Ai2)](https://allenai.org/blog/olmo2)
- [OLMo 2 Paper (arxiv)](https://arxiv.org/abs/2501.00656)
- [OLMo Release Notes](https://allenai.org/olmo/release-notes)
- [Google DeepMind Gemma 3](https://deepmind.google/models/gemma/gemma-3/)

agentId: a21ba8d3a3938265b (use SendMessage with to: 'a21ba8d3a3938265b' to continue this agent)
&lt;usage>total_tokens: 34598
tool_uses: 15
duration_ms: 101562&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f98bdbe4-4d54-45ec-8be5-1afad109d931",
  "isSidechain": false,
  "promptId": "04205c35-fa25-4f0b-9c44-5def633915cd",
  "type": "user",
  "uuid": "b9805f26-85f8-4bc5-b4b6-4090fada6a60",
  "toolUseResult": {
    "status": "completed",
    "prompt": "You are researching the latest open-source base LLMs (7B-14B parameters) released in 2025-2026 for an academic paper. Run the following 3 web searches and compile ALL results with as much detail as possible. For each model found, note: full name, HuggingFace repo ID, parameter count, release date, whether it's gated, whether a base (non-instruct) version exists, training data size if mentioned, and benchmark performance if mentioned.\n\nSearch 1: \"Gemma 3 base model\"\nSearch 2: \"OLMo 2 base model\"\nSearch 3: \"Gemma 3 pretrained model huggingface 2025\"\n\nReturn ALL findings in a structured format. Be thorough.",
    "agentId": "a21ba8d3a3938265b",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Here are all findings compiled in structured format.\n\n---\n\n## Gemma 3 (Google DeepMind)\n\n**Release date:** March 12, 2025 (added to HuggingFace Transformers); public release ~March 25, 2025\n\n**License:** Gemma Terms of Use (custom Google license)\n\n**Gated:** Yes. Requires agreeing to Google's usage license on HuggingFace before downloading.\n\n**Base (pretrained) versions exist:** Yes. All sizes have a `-pt` (pretrained) variant.\n\n| Size | HuggingFace Repo ID | Parameters | Modality | Context Window | Training Tokens | MMLU (base) | HellaSwag (base) |\n|------|---------------------|------------|----------|----------------|-----------------|-------------|------------------|\n| 1B | `google/gemma-3-1b-pt` | 1B | Text only | 32K | 2T | 38.8% | 62.3 |\n| 4B | `google/gemma-3-4b-pt` | 4B | Text + Image | 128K | 4T | 58.1% | 77.2 |\n| 12B | `google/gemma-3-12b-pt` | 12B | Text + Image | 128K | 12T | 71.9% | 84.2 |\n| 27B | `google/gemma-3-27b-pt` | 27B | Text + Image | 128K | 14T | 76.9% | 85.6 |\n\n**Instruction-tuned counterparts** use the `-it` suffix (e.g., `google/gemma-3-12b-it`).\n\n**Additional notes:**\n- 140+ language support\n- Trained using knowledge distillation from larger Gemini models\n- Trained on TPUv4p, TPUv5p, and TPUv5e hardware\n- A 270M text-only variant also exists, trained on 6T tokens\n- Gemma 3 4B-IT beats Gemma 2 27B-IT; Gemma 3 27B-IT is comparable to Gemini 1.5 Pro\n- Technical report: [arxiv.org/abs/2503.19786](https://arxiv.org/abs/2503.19786)\n\n---\n\n## OLMo 2 (Allen Institute for AI / Ai2)\n\n**License:** Apache 2.0 (fully open, including training data, code, and weights)\n\n**Gated:** No. All models are openly available.\n\n**Base (pretrained) versions exist:** Yes. The base repo IDs below are the pretrained models; instruct/SFT/DPO variants have corresponding suffixes.\n\n| Size | HuggingFace Repo ID | Parameters | Release Date | Training Tokens | MMLU (base) |\n|------|---------------------|------------|--------------|-----------------|-------------|\n| 1B | `allenai/OLMo-2-0425-1B` | 1B | April 2025 | 4T (+ 50B mid-training) | Not reported in search results |\n| 7B | `allenai/OLMo-2-1124-7B` | 7B | November 2024 (updated Dec 31, 2024) | ~4T (Stage 1: 3.9T OLMo-Mix-1124, Stage 2: 50B Dolmino-Mix-1124) | 63.7 |\n| 13B | `allenai/OLMo-2-1124-13B` | 13B | November 2024 | Up to 5T | 67.5 |\n| 32B | `allenai/OLMo-2-0325-32B` | 32B | March 2025 | Up to 6T | Not reported in search results |\n\n**Instruct variants:**\n- `allenai/OLMo-2-1124-7B-Instruct`\n- `allenai/OLMo-2-1124-13B-Instruct`\n- `allenai/OLMo-2-0325-32B-Instruct`\n- `allenai/OLMo-2-0425-1B-Instruct`\n\n**Additional OLMo 2 details:**\n- Modality: Text only\n- Training data: OLMo-Mix-1124 (Stage 1) + Dolmino-Mix-1124 (Stage 2, mid-training)\n- 7B model: trained for ~1 epoch on 3.9T tokens, then 3 runs of 50B token mid-training merged via model souping\n- 9-point MMLU increase over original OLMo 7B\n- OLMo 2 7B outperforms Llama 3.1 8B on English academic benchmarks\n- OLMo 2 13B surpasses Qwen 2.5 7B despite fewer training FLOPs\n- OLMo 2 32B is described as \"the first fully-open model to outperform GPT-3.5-Turbo and GPT-4o mini\" on multi-skill academic benchmarks\n- ARC scores: improved from 80.2 to 83.5 for 13B\n- Data cutoff: December 2023\n- Technical report: [arxiv.org/abs/2501.00656](https://arxiv.org/abs/2501.00656)\n- Also note: Ai2 has released **OLMo 3** (`allenai/Olmo-3-1125-32B`) and **OLMo 3.1** (`allenai/Olmo-3.1-32B-Think`), though these are outside your 7B-14B scope\n\n---\n\n## Summary: Models in the 7B-14B Range\n\nFor the specific 7B-14B parameter range relevant to the paper:\n\n| Model | Repo ID | Params | Gated | License | Training Data | MMLU |\n|-------|---------|--------|-------|---------|---------------|------|\n| Gemma 3 12B PT | `google/gemma-3-12b-pt` | 12B | Yes | Gemma ToU | 12T tokens | 71.9% |\n| OLMo 2 7B | `allenai/OLMo-2-1124-7B` | 7B | No | Apache 2.0 | ~4T tokens | 63.7% |\n| OLMo 2 13B | `allenai/OLMo-2-1124-13B` | 13B | No | Apache 2.0 | ~5T tokens | 67.5% |\n\nOLMo 2 is the stronger choice for reproducibility research since it is fully open (Apache 2.0, open training data and code). Gemma 3 12B has stronger benchmark numbers but is gated and uses a custom license.\n\n---\n\nSources:\n- [Gemma 3 HuggingFace Docs](https://huggingface.co/docs/transformers/model_doc/gemma3)\n- [Welcome Gemma 3 Blog Post](https://huggingface.co/blog/gemma3)\n- [Gemma 3 Release Collection](https://huggingface.co/collections/google/gemma-3-release)\n- [google/gemma-3-12b-pt](https://huggingface.co/google/gemma-3-12b-pt)\n- [google/gemma-3-4b-pt](https://huggingface.co/google/gemma-3-4b-pt)\n- [google/gemma-3-27b-pt](https://huggingface.co/google/gemma-3-27b-pt)\n- [google/gemma-3-1b-pt](https://huggingface.co/google/gemma-3-1b-pt)\n- [Gemma 3 Technical Report (arxiv)](https://arxiv.org/abs/2503.19786)\n- [Gemma 3 Model Card (Google)](https://ai.google.dev/gemma/docs/core/model_card_3)\n- [allenai/OLMo-2-1124-7B](https://huggingface.co/allenai/OLMo-2-1124-7B)\n- [allenai/OLMo-2-1124-13B](https://huggingface.co/allenai/OLMo-2-1124-13B)\n- [allenai/OLMo-2-0325-32B](https://huggingface.co/allenai/OLMo-2-0325-32B)\n- [allenai/OLMo-2-0425-1B](https://huggingface.co/allenai/OLMo-2-0425-1B)\n- [OLMo 2 Collection](https://huggingface.co/collections/allenai/olmo-2)\n- [OLMo 2 Blog Post (Ai2)](https://allenai.org/blog/olmo2)\n- [OLMo 2 Paper (arxiv)](https://arxiv.org/abs/2501.00656)\n- [OLMo Release Notes](https://allenai.org/olmo/release-notes)\n- [Google DeepMind Gemma 3](https://deepmind.google/models/gemma/gemma-3/)"
      }
    ],
    "totalDurationMs": 101562,
    "totalTokens": 34598,
    "totalToolUseCount": 15,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6181,
      "cache_read_input_tokens": 26051,
      "output_tokens": 2365,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6181
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2365,
          "cache_read_input_tokens": 26051,
          "cache_creation_input_tokens": 6181,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6181,
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
      "otherToolCount": 15
    }
  },
  "sourceToolAssistantUUID": "f98bdbe4-4d54-45ec-8be5-1afad109d931",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-18T07:09:40.865Z_

<details><summary>↩ Tool result · `toolu_01UUx3h1Z4EHFrb7q9YJpLgR`</summary>

```text
Here are the compiled findings from all three searches.

---

## SEARCH 1: Llama 4 Base Model Release

**Important caveat:** Llama 4 does NOT have any models in the 7B-14B parameter range. All Llama 4 models have 17B active parameters (MoE), with total parameter counts of 109B+ . There is no Llama 4 equivalent of the old Llama 3.1 8B.

### Llama 4 Scout

| Field | Detail |
|---|---|
| **Full name** | Llama 4 Scout 17B 16E |
| **HuggingFace repo (base)** | `meta-llama/Llama-4-Scout-17B-16E` |
| **HuggingFace repo (instruct)** | `meta-llama/Llama-4-Scout-17B-16E-Instruct` |
| **Parameter count** | 17B active, ~109B total (16 experts) |
| **Release date** | April 5, 2025 |
| **Gated?** | Yes -- requires accepting the Llama 4 Community License Agreement on HuggingFace |
| **Base (non-instruct) version?** | Yes (`meta-llama/Llama-4-Scout-17B-16E`) |
| **Training data size** | ~40 trillion tokens (multimodal), cutoff August 2024 |
| **Context window** | 10M tokens (pretrained at 256K) |
| **Architecture** | Mixture-of-Experts (MoE), auto-regressive, natively multimodal |
| **Benchmark** | Not individually broken out in public announcements for the base model |

### Llama 4 Maverick

| Field | Detail |
|---|---|
| **Full name** | Llama 4 Maverick 17B 128E |
| **HuggingFace repo (base)** | `meta-llama/Llama-4-Maverick-17B-128E` (also `meta-llama/Llama-4-Maverick-17B-128E-Original` for Meta format) |
| **HuggingFace repo (instruct)** | `meta-llama/Llama-4-Maverick-17B-128E-Instruct` |
| **Parameter count** | 17B active, ~400B total (128 experts) |
| **Release date** | April 5, 2025 |
| **Gated?** | Yes -- same Llama 4 Community License |
| **Base (non-instruct) version?** | Yes |
| **Training data size** | ~22 trillion tokens (multimodal), cutoff August 2024 |
| **Context window** | 1M tokens |
| **Architecture** | MoE, auto-regressive, natively multimodal |

### Llama 4 Behemoth (not released)

Announced but still in training at time of Scout/Maverick release. 288B active parameters, ~2T total, 16 experts.

**Bottom line for your paper:** Llama 4 has no dense 7B-14B model. If you need a Meta base model in that range, the closest is still **Llama 3.1 8B** or **Llama 3.2 (1B/3B)**.

---

## SEARCH 2: Qwen 3 Base Model

Qwen3 was released on **April 29, 2025** by Alibaba Cloud's Qwen team. Dense base models in the 7B-14B range:

### Qwen3-8B-Base

| Field | Detail |
|---|---|
| **Full name** | Qwen3-8B-Base |
| **HuggingFace repo** | `Qwen/Qwen3-8B-Base` |
| **Parameter count** | 8.2B total, 6.95B non-embedding |
| **Architecture** | Dense causal transformer, 36 layers, 32 Q-heads / 8 KV-heads (GQA), SwiGLU, RMSNorm |
| **Release date** | April 29, 2025 |
| **Gated?** | No -- open weights under Apache 2.0 |
| **Base (non-instruct) version?** | Yes (this IS the base version; instruct = `Qwen/Qwen3-8B`) |
| **Training data size** | 36 trillion tokens, 119 languages |
| **Context length** | 32,768 native; up to 131,072 with YaRN |
| **Benchmarks (base)** | MMLU: 79.66, GSM8K: 90.22, EvalPlus: 60.70 |
| **Notable** | Outperforms Qwen2.5-14B-Base on many benchmarks |

### Qwen3-14B-Base

| Field | Detail |
|---|---|
| **Full name** | Qwen3-14B-Base |
| **HuggingFace repo** | `Qwen/Qwen3-14B-Base` |
| **Parameter count** | 14.8B total, 13.2B non-embedding |
| **Architecture** | Dense causal transformer, 40 layers, 40 Q-heads / 8 KV-heads (GQA), SwiGLU, RMSNorm |
| **Release date** | April 29, 2025 |
| **Gated?** | No -- open weights under Apache 2.0 |
| **Base (non-instruct) version?** | Yes (instruct = `Qwen/Qwen3-14B`) |
| **Training data size** | 36 trillion tokens, 119 languages |
| **Context length** | 32,768 native |
| **Benchmarks (base)** | MMLU: 81.05, GSM8K: 92.49, EvalPlus: 72.23 |
| **Notable** | Competitive with Qwen2.5-32B-Base; significant cost advantage |

### Other Qwen3 dense base models (outside 7B-14B but for reference)

- `Qwen/Qwen3-0.6B-Base` (0.6B)
- `Qwen/Qwen3-1.7B-Base` (1.7B)
- `Qwen/Qwen3-4B-Base` (4B) -- MMLU: 74.16, GSM8K: 85.36
- `Qwen/Qwen3-32B-Base` (32B)

**Technical report:** [arxiv.org/abs/2505.09388](https://arxiv.org/abs/2505.09388) (May 15, 2025)

---

## SEARCH 3: Mistral Latest Base Model 2025

The Mistral 3 family launched on **December 2, 2025**, including the Ministral 3 edge/local models with base variants.

### Ministral-3-8B-Base-2512

| Field | Detail |
|---|---|
| **Full name** | Ministral 3 8B Base 2512 |
| **HuggingFace repo** | `mistralai/Ministral-3-8B-Base-2512` |
| **Parameter count** | 8.4B total |
| **Architecture** | Dense vision-language model, 34 layers, 4096 hidden size, 32 attention heads, 8 KV groups (GQA) |
| **Release date** | December 2 (or 4), 2025 |
| **Gated?** | No -- Apache 2.0 license |
| **Base (non-instruct) version?** | Yes (instruct = `mistralai/Ministral-3-8B-Instruct-2512`; reasoning = `mistralai/Ministral-3-8B-Reasoning-2512`) |
| **Training data size** | Not publicly disclosed |
| **Context length** | Up to 256K tokens (YaRN RoPE scaling) |
| **Benchmarks (base)** | Specific MMLU score for the 8B base not found in search results |
| **Notable** | Natively multimodal (vision baked into core training); trained on 40+ languages (strong European language support); fits on single H200 GPU |

### Ministral-3-14B-Base-2512

| Field | Detail |
|---|---|
| **Full name** | Ministral 3 14B Base 2512 |
| **HuggingFace repo** | `mistralai/Ministral-3-14B-Base-2512` |
| **Parameter count** | ~14B total |
| **Architecture** | Dense vision-language model, 40 layers, 5120 hidden size, 32 attention heads, 8 KV groups (GQA) |
| **Release date** | December 2 (or 4), 2025 |
| **Gated?** | No -- Apache 2.0 license |
| **Base (non-instruct) version?** | Yes (instruct = `mistralai/Ministral-3-14B-Instruct-2512`; reasoning = `mistralai/Ministral-3-14B-Reasoning-2512`) |
| **Training data size** | Not publicly disclosed |
| **Context length** | Up to 256K tokens |
| **Benchmarks (base)** | MMLU: 79.4%, MMLU-Redux: 82.0% |
| **Notable** | Performance comparable to Mistral Small 3.2 24B; recommended 2xH200 for full 256K context |

### Ministral-3-3B-Base-2512 (outside 7B-14B but for reference)

- HuggingFace repo: `mistralai/Ministral-3-3B-Base-2512`
- 3.4B params, 26 layers, Apache 2.0, 256K context

### Mistral Small 4 (March 2026, for context)

- MoE model: 119B total, 6B active per token
- Not a base model in the traditional sense; instruction/reasoning focused
- Not in the 7B-14B dense range

**Technical report:** [arxiv.org/abs/2601.08584](https://arxiv.org/abs/2601.08584)

---

## Summary: All Base Models in the 7B-14B Range (2025-2026)

| Model | Repo ID | Params | Released | License | Gated? | Training Data | Context | MMLU (base) |
|---|---|---|---|---|---|---|---|---|
| **Qwen3-8B-Base** | `Qwen/Qwen3-8B-Base` | 8.2B | 2025-04-29 | Apache 2.0 | No | 36T tokens | 32K (131K w/ YaRN) | 79.66 |
| **Qwen3-14B-Base** | `Qwen/Qwen3-14B-Base` | 14.8B | 2025-04-29 | Apache 2.0 | No | 36T tokens | 32K | 81.05 |
| **Ministral-3-8B-Base** | `mistralai/Ministral-3-8B-Base-2512` | 8.4B | 2025-12-02 | Apache 2.0 | No | Undisclosed | 256K | -- |
| **Ministral-3-14B-Base** | `mistralai/Ministral-3-14B-Base-2512` | ~14B | 2025-12-02 | Apache 2.0 | No | Undisclosed | 256K | 79.4 |
| **Llama 4 Scout (MoE)** | `meta-llama/Llama-4-Scout-17B-16E` | 17B active / 109B total | 2025-04-05 | Llama 4 CLA | Yes | 40T tokens | 10M | -- |

Llama 4 Scout/Maverick are included for completeness but are MoE models with 17B active params (outside the strict 7B-14B dense range). There is **no Llama 4 dense model in the 7B-14B range**.

Sources:
- [Meta Llama 4 blog](https://ai.meta.com/blog/llama-4-multimodal-intelligence/)
- [meta-llama/Llama-4-Scout-17B-16E](https://huggingface.co/meta-llama/Llama-4-Scout-17B-16E)
- [meta-llama/Llama-4-Maverick-17B-128E](https://huggingface.co/meta-llama/Llama-4-Maverick-17B-128E)
- [HuggingFace Llama 4 release blog](https://huggingface.co/blog/llama4-release)
- [Qwen3 blog](https://qwenlm.github.io/blog/qwen3/)
- [Qwen/Qwen3-8B-Base](https://huggingface.co/Qwen/Qwen3-8B-Base)
- [Qwen/Qwen3-14B-Base](https://huggingface.co/Qwen/Qwen3-14B-Base)
- [Qwen3 Technical Report (arXiv 2505.09388)](https://arxiv.org/pdf/2505.09388)
- [Introducing Mistral 3](https://mistral.ai/news/mistral-3)
- [mistralai/Ministral-3-8B-Base-2512](https://huggingface.co/mistralai/Ministral-3-8B-Base-2512)
- [mistralai/Ministral-3-14B-Base-2512](https://huggingface.co/mistralai/Ministral-3-14B-Base-2512)
- [Ministral 3 Technical Report (arXiv 2601.08584)](https://arxiv.org/pdf/2601.08584)
- [Mistral 3 guide (Shawn Kanungo)](https://shawnkanungo.com/blog/what-is-mistral-3-ai-open-source-models-guide-2026)
- [Mistral AI Models 2026 guide (Serenities AI)](https://serenitiesai.com/articles/mistral-ai-models-2026-complete-guide)

agentId: ac855f59be58ea3ac (use SendMessage with to: 'ac855f59be58ea3ac' to continue this agent)
&lt;usage>total_tokens: 35454
tool_uses: 16
duration_ms: 120410&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "98f79d7d-3d0e-4989-bfea-4fbfe0109d7d",
  "isSidechain": false,
  "promptId": "04205c35-fa25-4f0b-9c44-5def633915cd",
  "type": "user",
  "uuid": "4096d60c-2402-47e3-a46f-328f56e71514",
  "toolUseResult": {
    "status": "completed",
    "prompt": "You are researching the latest open-source base LLMs (7B-14B parameters) released in 2025-2026 for an academic paper. Run the following 3 web searches and compile ALL results with as much detail as possible. For each model found, note: full name, HuggingFace repo ID, parameter count, release date, whether it's gated, whether a base (non-instruct) version exists, training data size if mentioned, and benchmark performance if mentioned.\n\nSearch 1: \"Llama 4 base model release\"\nSearch 2: \"Qwen 3 base model\"\nSearch 3: \"Mistral latest base model 2025\"\n\nReturn ALL findings in a structured format. Be thorough - list every model you find in the 7B-14B range.",
    "agentId": "ac855f59be58ea3ac",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Here are the compiled findings from all three searches.\n\n---\n\n## SEARCH 1: Llama 4 Base Model Release\n\n**Important caveat:** Llama 4 does NOT have any models in the 7B-14B parameter range. All Llama 4 models have 17B active parameters (MoE), with total parameter counts of 109B+ . There is no Llama 4 equivalent of the old Llama 3.1 8B.\n\n### Llama 4 Scout\n\n| Field | Detail |\n|---|---|\n| **Full name** | Llama 4 Scout 17B 16E |\n| **HuggingFace repo (base)** | `meta-llama/Llama-4-Scout-17B-16E` |\n| **HuggingFace repo (instruct)** | `meta-llama/Llama-4-Scout-17B-16E-Instruct` |\n| **Parameter count** | 17B active, ~109B total (16 experts) |\n| **Release date** | April 5, 2025 |\n| **Gated?** | Yes -- requires accepting the Llama 4 Community License Agreement on HuggingFace |\n| **Base (non-instruct) version?** | Yes (`meta-llama/Llama-4-Scout-17B-16E`) |\n| **Training data size** | ~40 trillion tokens (multimodal), cutoff August 2024 |\n| **Context window** | 10M tokens (pretrained at 256K) |\n| **Architecture** | Mixture-of-Experts (MoE), auto-regressive, natively multimodal |\n| **Benchmark** | Not individually broken out in public announcements for the base model |\n\n### Llama 4 Maverick\n\n| Field | Detail |\n|---|---|\n| **Full name** | Llama 4 Maverick 17B 128E |\n| **HuggingFace repo (base)** | `meta-llama/Llama-4-Maverick-17B-128E` (also `meta-llama/Llama-4-Maverick-17B-128E-Original` for Meta format) |\n| **HuggingFace repo (instruct)** | `meta-llama/Llama-4-Maverick-17B-128E-Instruct` |\n| **Parameter count** | 17B active, ~400B total (128 experts) |\n| **Release date** | April 5, 2025 |\n| **Gated?** | Yes -- same Llama 4 Community License |\n| **Base (non-instruct) version?** | Yes |\n| **Training data size** | ~22 trillion tokens (multimodal), cutoff August 2024 |\n| **Context window** | 1M tokens |\n| **Architecture** | MoE, auto-regressive, natively multimodal |\n\n### Llama 4 Behemoth (not released)\n\nAnnounced but still in training at time of Scout/Maverick release. 288B active parameters, ~2T total, 16 experts.\n\n**Bottom line for your paper:** Llama 4 has no dense 7B-14B model. If you need a Meta base model in that range, the closest is still **Llama 3.1 8B** or **Llama 3.2 (1B/3B)**.\n\n---\n\n## SEARCH 2: Qwen 3 Base Model\n\nQwen3 was released on **April 29, 2025** by Alibaba Cloud's Qwen team. Dense base models in the 7B-14B range:\n\n### Qwen3-8B-Base\n\n| Field | Detail |\n|---|---|\n| **Full name** | Qwen3-8B-Base |\n| **HuggingFace repo** | `Qwen/Qwen3-8B-Base` |\n| **Parameter count** | 8.2B total, 6.95B non-embedding |\n| **Architecture** | Dense causal transformer, 36 layers, 32 Q-heads / 8 KV-heads (GQA), SwiGLU, RMSNorm |\n| **Release date** | April 29, 2025 |\n| **Gated?** | No -- open weights under Apache 2.0 |\n| **Base (non-instruct) version?** | Yes (this IS the base version; instruct = `Qwen/Qwen3-8B`) |\n| **Training data size** | 36 trillion tokens, 119 languages |\n| **Context length** | 32,768 native; up to 131,072 with YaRN |\n| **Benchmarks (base)** | MMLU: 79.66, GSM8K: 90.22, EvalPlus: 60.70 |\n| **Notable** | Outperforms Qwen2.5-14B-Base on many benchmarks |\n\n### Qwen3-14B-Base\n\n| Field | Detail |\n|---|---|\n| **Full name** | Qwen3-14B-Base |\n| **HuggingFace repo** | `Qwen/Qwen3-14B-Base` |\n| **Parameter count** | 14.8B total, 13.2B non-embedding |\n| **Architecture** | Dense causal transformer, 40 layers, 40 Q-heads / 8 KV-heads (GQA), SwiGLU, RMSNorm |\n| **Release date** | April 29, 2025 |\n| **Gated?** | No -- open weights under Apache 2.0 |\n| **Base (non-instruct) version?** | Yes (instruct = `Qwen/Qwen3-14B`) |\n| **Training data size** | 36 trillion tokens, 119 languages |\n| **Context length** | 32,768 native |\n| **Benchmarks (base)** | MMLU: 81.05, GSM8K: 92.49, EvalPlus: 72.23 |\n| **Notable** | Competitive with Qwen2.5-32B-Base; significant cost advantage |\n\n### Other Qwen3 dense base models (outside 7B-14B but for reference)\n\n- `Qwen/Qwen3-0.6B-Base` (0.6B)\n- `Qwen/Qwen3-1.7B-Base` (1.7B)\n- `Qwen/Qwen3-4B-Base` (4B) -- MMLU: 74.16, GSM8K: 85.36\n- `Qwen/Qwen3-32B-Base` (32B)\n\n**Technical report:** [arxiv.org/abs/2505.09388](https://arxiv.org/abs/2505.09388) (May 15, 2025)\n\n---\n\n## SEARCH 3: Mistral Latest Base Model 2025\n\nThe Mistral 3 family launched on **December 2, 2025**, including the Ministral 3 edge/local models with base variants.\n\n### Ministral-3-8B-Base-2512\n\n| Field | Detail |\n|---|---|\n| **Full name** | Ministral 3 8B Base 2512 |\n| **HuggingFace repo** | `mistralai/Ministral-3-8B-Base-2512` |\n| **Parameter count** | 8.4B total |\n| **Architecture** | Dense vision-language model, 34 layers, 4096 hidden size, 32 attention heads, 8 KV groups (GQA) |\n| **Release date** | December 2 (or 4), 2025 |\n| **Gated?** | No -- Apache 2.0 license |\n| **Base (non-instruct) version?** | Yes (instruct = `mistralai/Ministral-3-8B-Instruct-2512`; reasoning = `mistralai/Ministral-3-8B-Reasoning-2512`) |\n| **Training data size** | Not publicly disclosed |\n| **Context length** | Up to 256K tokens (YaRN RoPE scaling) |\n| **Benchmarks (base)** | Specific MMLU score for the 8B base not found in search results |\n| **Notable** | Natively multimodal (vision baked into core training); trained on 40+ languages (strong European language support); fits on single H200 GPU |\n\n### Ministral-3-14B-Base-2512\n\n| Field | Detail |\n|---|---|\n| **Full name** | Ministral 3 14B Base 2512 |\n| **HuggingFace repo** | `mistralai/Ministral-3-14B-Base-2512` |\n| **Parameter count** | ~14B total |\n| **Architecture** | Dense vision-language model, 40 layers, 5120 hidden size, 32 attention heads, 8 KV groups (GQA) |\n| **Release date** | December 2 (or 4), 2025 |\n| **Gated?** | No -- Apache 2.0 license |\n| **Base (non-instruct) version?** | Yes (instruct = `mistralai/Ministral-3-14B-Instruct-2512`; reasoning = `mistralai/Ministral-3-14B-Reasoning-2512`) |\n| **Training data size** | Not publicly disclosed |\n| **Context length** | Up to 256K tokens |\n| **Benchmarks (base)** | MMLU: 79.4%, MMLU-Redux: 82.0% |\n| **Notable** | Performance comparable to Mistral Small 3.2 24B; recommended 2xH200 for full 256K context |\n\n### Ministral-3-3B-Base-2512 (outside 7B-14B but for reference)\n\n- HuggingFace repo: `mistralai/Ministral-3-3B-Base-2512`\n- 3.4B params, 26 layers, Apache 2.0, 256K context\n\n### Mistral Small 4 (March 2026, for context)\n\n- MoE model: 119B total, 6B active per token\n- Not a base model in the traditional sense; instruction/reasoning focused\n- Not in the 7B-14B dense range\n\n**Technical report:** [arxiv.org/abs/2601.08584](https://arxiv.org/abs/2601.08584)\n\n---\n\n## Summary: All Base Models in the 7B-14B Range (2025-2026)\n\n| Model | Repo ID | Params | Released | License | Gated? | Training Data | Context | MMLU (base) |\n|---|---|---|---|---|---|---|---|---|\n| **Qwen3-8B-Base** | `Qwen/Qwen3-8B-Base` | 8.2B | 2025-04-29 | Apache 2.0 | No | 36T tokens | 32K (131K w/ YaRN) | 79.66 |\n| **Qwen3-14B-Base** | `Qwen/Qwen3-14B-Base` | 14.8B | 2025-04-29 | Apache 2.0 | No | 36T tokens | 32K | 81.05 |\n| **Ministral-3-8B-Base** | `mistralai/Ministral-3-8B-Base-2512` | 8.4B | 2025-12-02 | Apache 2.0 | No | Undisclosed | 256K | -- |\n| **Ministral-3-14B-Base** | `mistralai/Ministral-3-14B-Base-2512` | ~14B | 2025-12-02 | Apache 2.0 | No | Undisclosed | 256K | 79.4 |\n| **Llama 4 Scout (MoE)** | `meta-llama/Llama-4-Scout-17B-16E` | 17B active / 109B total | 2025-04-05 | Llama 4 CLA | Yes | 40T tokens | 10M | -- |\n\nLlama 4 Scout/Maverick are included for completeness but are MoE models with 17B active params (outside the strict 7B-14B dense range). There is **no Llama 4 dense model in the 7B-14B range**.\n\nSources:\n- [Meta Llama 4 blog](https://ai.meta.com/blog/llama-4-multimodal-intelligence/)\n- [meta-llama/Llama-4-Scout-17B-16E](https://huggingface.co/meta-llama/Llama-4-Scout-17B-16E)\n- [meta-llama/Llama-4-Maverick-17B-128E](https://huggingface.co/meta-llama/Llama-4-Maverick-17B-128E)\n- [HuggingFace Llama 4 release blog](https://huggingface.co/blog/llama4-release)\n- [Qwen3 blog](https://qwenlm.github.io/blog/qwen3/)\n- [Qwen/Qwen3-8B-Base](https://huggingface.co/Qwen/Qwen3-8B-Base)\n- [Qwen/Qwen3-14B-Base](https://huggingface.co/Qwen/Qwen3-14B-Base)\n- [Qwen3 Technical Report (arXiv 2505.09388)](https://arxiv.org/pdf/2505.09388)\n- [Introducing Mistral 3](https://mistral.ai/news/mistral-3)\n- [mistralai/Ministral-3-8B-Base-2512](https://huggingface.co/mistralai/Ministral-3-8B-Base-2512)\n- [mistralai/Ministral-3-14B-Base-2512](https://huggingface.co/mistralai/Ministral-3-14B-Base-2512)\n- [Ministral 3 Technical Report (arXiv 2601.08584)](https://arxiv.org/pdf/2601.08584)\n- [Mistral 3 guide (Shawn Kanungo)](https://shawnkanungo.com/blog/what-is-mistral-3-ai-open-source-models-guide-2026)\n- [Mistral AI Models 2026 guide (Serenities AI)](https://serenitiesai.com/articles/mistral-ai-models-2026-complete-guide)"
      }
    ],
    "totalDurationMs": 120410,
    "totalTokens": 35454,
    "totalToolUseCount": 16,
    "usage": {
      "input_tokens": 904,
      "cache_creation_input_tokens": 1267,
      "cache_read_input_tokens": 29599,
      "output_tokens": 3684,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1267
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 904,
          "output_tokens": 3684,
          "cache_read_input_tokens": 29599,
          "cache_creation_input_tokens": 1267,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1267,
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
      "otherToolCount": 16
    }
  },
  "sourceToolAssistantUUID": "98f79d7d-3d0e-4989-bfea-4fbfe0109d7d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 21_

```json
{
  "type": "last-prompt",
  "leafUuid": "4096d60c-2402-47e3-a46f-328f56e71514",
  "sessionId": "b4bb6832-311d-424b-8b19-57bd3d213f37"
}
```

---

### Runtime record

_source line 22_

```json
{
  "type": "ai-title",
  "aiTitle": "Search 2025-2026 base models for cross-family validation",
  "sessionId": "b4bb6832-311d-424b-8b19-57bd3d213f37"
}
```

---

### Tool result

_source line 23 · 2026-05-18T07:11:04.389Z_

<details><summary>↩ Tool result · `toolu_01XSzbYG4aNMXhPUJ8DwFSt1`</summary>

```text
Here is the compiled structured report of all findings.

---

## Search 1: DeepSeek V3 Base Model

DeepSeek-V3 is **not** in the 7B-14B range. It is a large MoE model. However, the DeepSeek ecosystem includes several models that do fall in the target range.

### DeepSeek-V3 (for reference, out of range)
- **Full name:** DeepSeek-V3
- **HuggingFace repo:** `deepseek-ai/DeepSeek-V3-Base`
- **Total parameters:** 671B (+14B MTP module = 685B total weights)
- **Active parameters:** 37B per token
- **Architecture:** MoE (256 experts)
- **Release date:** December 2024 (V3-0324 update March 2025; V3.1 and V3.2 followed)
- **Gated:** No (MIT license)
- **Base version exists:** Yes (`deepseek-ai/DeepSeek-V3-Base`)
- **Training data:** ~14.8T tokens
- **NOT in 7B-14B range**

### DeepSeek-V2-Lite (in range)
- **Full name:** DeepSeek-V2-Lite
- **HuggingFace repo:** `deepseek-ai/DeepSeek-V2-Lite`
- **Total parameters:** 15.7B
- **Active parameters:** 2.4B per token
- **Architecture:** MoE (2 shared experts + 64 routed experts, 6 activated per token)
- **Release date:** May 7, 2024
- **Gated:** No (MIT license)
- **Base version exists:** Yes (this IS the base version; chat version at `deepseek-ai/DeepSeek-V2-Lite-Chat`)
- **Training data:** 5.7T tokens (same pre-training corpus as DeepSeek-V2)
- **Benchmarks:** Outperforms 7B dense and 16B MoE models on many English/Chinese benchmarks (specific MMLU not retrieved)

### DeepSeek-Coder-V2-Lite-Base (in range)
- **Full name:** DeepSeek-Coder-V2-Lite-Base
- **HuggingFace repo:** `deepseek-ai/DeepSeek-Coder-V2-Lite-Base`
- **Total parameters:** 15.7B (sometimes cited as 16B)
- **Active parameters:** 2.4B per token
- **Architecture:** MoE (2 shared experts + 64 routed experts, 6 activated per token)
- **Release date:** June 2024
- **Gated:** No
- **Base version exists:** Yes (this IS the base; instruct variant at `deepseek-ai/DeepSeek-Coder-V2-Lite-Instruct`)
- **Training data:** Not separately disclosed; code-focused extension of V2 data
- **Benchmarks:** Strong on code intelligence tasks; competes with closed-source models on coding benchmarks

### DeepSeek-R1-Distill-Qwen-14B (in range)
- **Full name:** DeepSeek-R1-Distill-Qwen-14B
- **HuggingFace repo:** `deepseek-ai/DeepSeek-R1-Distill-Qwen-14B`
- **Parameters:** 14B (dense)
- **Architecture:** Dense transformer (based on Qwen2.5-14B)
- **Release date:** January 20, 2025
- **Gated:** No (MIT license for DeepSeek distillation; underlying Qwen2.5 is Apache 2.0)
- **Base version exists:** No -- this is a distilled/fine-tuned model (SFT on 800K reasoning samples from DeepSeek-R1), not a base pretrained model
- **Training data:** Fine-tuned with 800K samples curated from DeepSeek-R1 outputs
- **Benchmarks:** AIME 2024: 69.7%, MATH-500: 93.9% (pass@1 with temperature=0.6, top-p=0.95, 64 samples)

### DeepSeek-R1-Distill-Qwen-7B (in range)
- **Full name:** DeepSeek-R1-Distill-Qwen-7B
- **HuggingFace repo:** `deepseek-ai/DeepSeek-R1-Distill-Qwen-7B`
- **Parameters:** 7B (dense)
- **Architecture:** Dense transformer (based on Qwen2.5-7B)
- **Release date:** January 20, 2025
- **Gated:** No
- **Base version exists:** No -- distilled model, not base pretrained
- **Training data:** Fine-tuned with 800K samples from DeepSeek-R1

---

## Search 2: Phi-4 Base Model

### Phi-4 (14B base)
- **Full name:** Phi-4
- **HuggingFace repo:** `microsoft/phi-4`
- **Parameters:** 14.7B (dense)
- **Architecture:** Dense decoder-only transformer
- **Release date:** December 2024 (initially on Azure; open-sourced on HuggingFace January 2025)
- **Gated:** No (MIT license, fully open access)
- **Base version exists:** Yes -- `microsoft/phi-4` IS the base pretrained model
- **Training data:** 9.8T tokens; mix of synthetic data (generated by GPT-4o), high-quality web content, educational data, code, academic books, Q&A datasets
- **Context length:** 16K tokens
- **Benchmarks:** MMLU: 84.8%, MATH: 80.4%, HumanEval: 82.6%

### Phi-4-reasoning (14B, fine-tuned)
- **Full name:** Phi-4-reasoning
- **HuggingFace repo:** `microsoft/Phi-4-reasoning`
- **Parameters:** 14B (dense)
- **Release date:** April 30, 2025
- **Gated:** No (MIT license)
- **Base version exists:** Not a base model; fine-tuned from Phi-4 for reasoning
- **Benchmarks:** AIME 2024: 75.3%

### Phi-4-reasoning-plus (14B, fine-tuned)
- **Full name:** Phi-4-reasoning-plus
- **HuggingFace repo:** `microsoft/Phi-4-reasoning-plus`
- **Parameters:** 14B (dense)
- **Release date:** April 30, 2025
- **Gated:** No (MIT license)
- **Base version exists:** Not a base model
- **Benchmarks:** AIME 2024: 81.3%

### Phi-4-mini-instruct (3.8B, NOT in 7B-14B range)
- **Full name:** Phi-4-mini-instruct
- **HuggingFace repo:** `microsoft/Phi-4-mini-instruct`
- **Parameters:** 3.8B (dense)
- **Release date:** March 19, 2026
- **Training data:** 5T tokens
- **Context length:** 128K tokens
- **Benchmarks:** MMLU: ~73% (matches Llama 3.1 8B)
- **NOT in 7B-14B range**

---

## Search 3: DeepSeek R2

**DeepSeek R2 has NOT been released as of May 2026.** Key findings:

- DeepSeek R2 was widely anticipated as the second-generation reasoning model.
- It was reportedly slated for release in H1 2025 but was delayed.
- The delay was caused by failed training runs on Huawei Ascend AI chips (stability problems, slow interconnect, immature software tooling).
- As of April 2026, DeepSeek instead released DeepSeek-V4-Pro (1.6T parameters) and DeepSeek-V4-Flash (284B parameters) with 1M token context windows.
- R2 is NOT listed in the official DeepSeek API model list as of May 2026.
- No HuggingFace repository exists for DeepSeek R2.

---

## Additional Models Found in the 7B-14B Range (2025-2026)

### Qwen3-14B-Base
- **HuggingFace repo:** `Qwen/Qwen3-14B-Base`
- **Parameters:** 14B (dense)
- **Architecture:** Dense transformer
- **Release date:** April 29, 2025
- **Gated:** No (Apache 2.0)
- **Base version exists:** Yes (this IS the base)
- **Training data:** ~36T tokens covering 119 languages (3-stage pretraining: S1 >30T tokens at 4K context, S2 +5T tokens STEM-heavy, S3 long-context extension to 32K)
- **Benchmarks:** MMLU: 81.05 (base model). Performance matches Qwen2.5-32B-Base.

### Qwen3-8B-Base
- **HuggingFace repo:** `Qwen/Qwen3-8B-Base`
- **Parameters:** 8B (dense)
- **Architecture:** Dense transformer
- **Release date:** April 29, 2025
- **Gated:** No (Apache 2.0)
- **Base version exists:** Yes
- **Training data:** ~36T tokens (same corpus as all Qwen3 models)
- **Benchmarks:** Performance matches Qwen2.5-14B-Base

### Gemma 3 12B (pretrained base)
- **Full name:** Gemma 3 12B PT
- **HuggingFace repo:** `google/gemma-3-12b-pt`
- **Parameters:** 12B (dense)
- **Architecture:** Dense transformer, multimodal (text+image input, text output)
- **Release date:** March 12, 2025
- **Gated:** Yes (requires agreeing to Google's usage license on HuggingFace)
- **Base version exists:** Yes (`google/gemma-3-12b-pt` is the pretrained base)
- **Training data:** 12T tokens
- **Context length:** 128K tokens
- **Benchmarks:** Specific MMLU for 12B not retrieved; 27B version: MMLU-Pro 67.5

### Ministral-3-14B-Base-2512
- **Full name:** Ministral 3 14B Base
- **HuggingFace repo:** `mistralai/Ministral-3-14B-Base-2512`
- **Parameters:** 14B (dense)
- **Architecture:** Dense transformer with vision capabilities
- **Release date:** December 1, 2025
- **Gated:** No (Apache 2.0)
- **Base version exists:** Yes (this IS the base)
- **Training data:** Not publicly disclosed. Trained via cascade distillation from Mistral Small 3.1 (24B parent)
- **Vocab size:** 131K tokens
- **Benchmarks:** Multilingual MMLU: 74.2%. Reasoning variant achieves 85% on AIME 2025.

### Ministral-3-8B-Base-2512
- **Full name:** Ministral 3 8B Base
- **HuggingFace repo:** `mistralai/Ministral-3-8B-Base-2512`
- **Parameters:** 8B (dense)
- **Architecture:** Dense transformer with vision capabilities
- **Release date:** December 1, 2025
- **Gated:** No (Apache 2.0)
- **Base version exists:** Yes
- **Training data:** Not disclosed. Cascade distillation from Ministral 3 14B.
- **Benchmarks:** Multilingual MMLU: 70.6%. Outperforms Gemma 3 12B on most evaluations except TriviaQA.

### Llama 4 Scout (out of strict 7B-14B range but noteworthy for active params)
- **Full name:** Llama 4 Scout 17B-16E
- **HuggingFace repo:** `meta-llama/Llama-4-Scout-17B-16E`
- **Total parameters:** ~109B
- **Active parameters:** 17B per token
- **Architecture:** MoE (16 experts)
- **Release date:** April 2025
- **Gated:** Yes (Meta Community License, 700M MAU clause)
- **Base version exists:** Yes (base and instruct variants both available)
- **Training data:** ~40T tokens (multimodal)
- **Context length:** 256K (pretrained), 10M (instruct)
- **Note:** While total params are 109B, active params (17B) are close to the 14B range. This is an MoE model.

---

## Summary Table: Models with Base Versions in the 7B-14B Dense Parameter Range

| Model | HF Repo ID | Params | Architecture | Release | License | Gated | Training Data | Base Exists | MMLU |
|---|---|---|---|---|---|---|---|---|---|
| **Phi-4** | `microsoft/phi-4` | 14.7B dense | Dense | Dec 2024 / Jan 2025 | MIT | No | 9.8T tokens | Yes | 84.8% |
| **Qwen3-14B** | `Qwen/Qwen3-14B-Base` | 14B dense | Dense | Apr 29, 2025 | Apache 2.0 | No | ~36T tokens | Yes | 81.05% |
| **Qwen3-8B** | `Qwen/Qwen3-8B-Base` | 8B dense | Dense | Apr 29, 2025 | Apache 2.0 | No | ~36T tokens | Yes | -- |
| **Gemma 3 12B** | `google/gemma-3-12b-pt` | 12B dense | Dense | Mar 12, 2025 | Gemma license | Yes | 12T tokens | Yes | -- |
| **Ministral 3 14B** | `mistralai/Ministral-3-14B-Base-2512` | 14B dense | Dense | Dec 1, 2025 | Apache 2.0 | No | Undisclosed | Yes | 74.2% (multilingual) |
| **Ministral 3 8B** | `mistralai/Ministral-3-8B-Base-2512` | 8B dense | Dense | Dec 1, 2025 | Apache 2.0 | No | Undisclosed | Yes | 70.6% (multilingual) |
| **DeepSeek-V2-Lite** | `deepseek-ai/DeepSeek-V2-Lite` | 15.7B total / **2.4B active** | **MoE** | May 7, 2024 | MIT | No | 5.7T tokens | Yes | -- |
| **DeepSeek-Coder-V2-Lite** | `deepseek-ai/DeepSeek-Coder-V2-Lite-Base` | 15.7B total / **2.4B active** | **MoE** | Jun 2024 | MIT | No | Undisclosed | Yes | -- |

## MoE Models Near the Range (for reference)

| Model | Total Params | Active Params | Experts | Notes |
|---|---|---|---|---|
| DeepSeek-V2-Lite | 15.7B | 2.4B | 64 routed + 2 shared, 6 active | Smallest DeepSeek MoE |
| DeepSeek-Coder-V2-Lite | 15.7B | 2.4B | Same as above | Code-focused variant |
| Llama 4 Scout | ~109B | 17B | 16 experts | Active params close to range |
| Gemma 4 26B-A4B | 25.2B | 3.8B | MoE | Out of range but notable |
| DeepSeek-V3 | 671B | 37B | 256 experts | Far out of range |

## Key Takeaway for Your Paper

For an academic paper needing open-source base (non-instruct) LLMs in the 7B-14B dense parameter range released in 2025-2026, the strongest candidates are:

1. **Phi-4** (`microsoft/phi-4`) -- 14.7B, MIT, not gated, highest MMLU at 84.8%
2. **Qwen3-14B-Base** (`Qwen/Qwen3-14B-Base`) -- 14B, Apache 2.0, not gated, MMLU 81.05%, largest training corpus (36T tokens)
3. **Qwen3-8B-Base** (`Qwen/Qwen3-8B-Base`) -- 8B, Apache 2.0, not gated
4. **Gemma 3 12B PT** (`google/gemma-3-12b-pt`) -- 12B, gated (license agreement required)
5. **Ministral 3 14B Base** (`mistralai/Ministral-3-14B-Base-2512`) -- 14B, Apache 2.0, Dec 2025
6. **Ministral 3 8B Base** (`mistralai/Ministral-3-8B-Base-2512`) -- 8B, Apache 2.0, Dec 2025

DeepSeek R2 does not exist yet. DeepSeek V3 is far too large (671B). The DeepSeek-R1-Distill models (7B/14B) exist but are fine-tuned reasoning models, not base pretrained models.

agentId: a72b4b1ce170203bc (use SendMessage with to: 'a72b4b1ce170203bc' to continue this agent)
&lt;usage>total_tokens: 46413
tool_uses: 24
duration_ms: 198282&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "faccd5e5-3705-46db-bae1-72dc2de8c36a",
  "isSidechain": false,
  "promptId": "04205c35-fa25-4f0b-9c44-5def633915cd",
  "type": "user",
  "uuid": "b3b8c1b4-7f9c-41d4-ad56-68c6a45a7422",
  "toolUseResult": {
    "status": "completed",
    "prompt": "You are researching the latest open-source base LLMs (7B-14B parameters) released in 2025-2026 for an academic paper. Run the following 3 web searches and compile ALL results with as much detail as possible. For each model found, note: full name, HuggingFace repo ID, parameter count, release date, whether it's gated, whether a base (non-instruct) version exists, training data size if mentioned, and benchmark performance if mentioned.\n\nSearch 1: \"DeepSeek V3 base model\"\nSearch 2: \"Phi-4 base model\"\nSearch 3: \"DeepSeek R2 base model 2025 2026\"\n\nReturn ALL findings in a structured format. Be thorough - list every model you find in the 7B-14B range. Also note if any of these models use MoE architecture (mixture of experts) and what the active parameter count is.",
    "agentId": "a72b4b1ce170203bc",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Here is the compiled structured report of all findings.\n\n---\n\n## Search 1: DeepSeek V3 Base Model\n\nDeepSeek-V3 is **not** in the 7B-14B range. It is a large MoE model. However, the DeepSeek ecosystem includes several models that do fall in the target range.\n\n### DeepSeek-V3 (for reference, out of range)\n- **Full name:** DeepSeek-V3\n- **HuggingFace repo:** `deepseek-ai/DeepSeek-V3-Base`\n- **Total parameters:** 671B (+14B MTP module = 685B total weights)\n- **Active parameters:** 37B per token\n- **Architecture:** MoE (256 experts)\n- **Release date:** December 2024 (V3-0324 update March 2025; V3.1 and V3.2 followed)\n- **Gated:** No (MIT license)\n- **Base version exists:** Yes (`deepseek-ai/DeepSeek-V3-Base`)\n- **Training data:** ~14.8T tokens\n- **NOT in 7B-14B range**\n\n### DeepSeek-V2-Lite (in range)\n- **Full name:** DeepSeek-V2-Lite\n- **HuggingFace repo:** `deepseek-ai/DeepSeek-V2-Lite`\n- **Total parameters:** 15.7B\n- **Active parameters:** 2.4B per token\n- **Architecture:** MoE (2 shared experts + 64 routed experts, 6 activated per token)\n- **Release date:** May 7, 2024\n- **Gated:** No (MIT license)\n- **Base version exists:** Yes (this IS the base version; chat version at `deepseek-ai/DeepSeek-V2-Lite-Chat`)\n- **Training data:** 5.7T tokens (same pre-training corpus as DeepSeek-V2)\n- **Benchmarks:** Outperforms 7B dense and 16B MoE models on many English/Chinese benchmarks (specific MMLU not retrieved)\n\n### DeepSeek-Coder-V2-Lite-Base (in range)\n- **Full name:** DeepSeek-Coder-V2-Lite-Base\n- **HuggingFace repo:** `deepseek-ai/DeepSeek-Coder-V2-Lite-Base`\n- **Total parameters:** 15.7B (sometimes cited as 16B)\n- **Active parameters:** 2.4B per token\n- **Architecture:** MoE (2 shared experts + 64 routed experts, 6 activated per token)\n- **Release date:** June 2024\n- **Gated:** No\n- **Base version exists:** Yes (this IS the base; instruct variant at `deepseek-ai/DeepSeek-Coder-V2-Lite-Instruct`)\n- **Training data:** Not separately disclosed; code-focused extension of V2 data\n- **Benchmarks:** Strong on code intelligence tasks; competes with closed-source models on coding benchmarks\n\n### DeepSeek-R1-Distill-Qwen-14B (in range)\n- **Full name:** DeepSeek-R1-Distill-Qwen-14B\n- **HuggingFace repo:** `deepseek-ai/DeepSeek-R1-Distill-Qwen-14B`\n- **Parameters:** 14B (dense)\n- **Architecture:** Dense transformer (based on Qwen2.5-14B)\n- **Release date:** January 20, 2025\n- **Gated:** No (MIT license for DeepSeek distillation; underlying Qwen2.5 is Apache 2.0)\n- **Base version exists:** No -- this is a distilled/fine-tuned model (SFT on 800K reasoning samples from DeepSeek-R1), not a base pretrained model\n- **Training data:** Fine-tuned with 800K samples curated from DeepSeek-R1 outputs\n- **Benchmarks:** AIME 2024: 69.7%, MATH-500: 93.9% (pass@1 with temperature=0.6, top-p=0.95, 64 samples)\n\n### DeepSeek-R1-Distill-Qwen-7B (in range)\n- **Full name:** DeepSeek-R1-Distill-Qwen-7B\n- **HuggingFace repo:** `deepseek-ai/DeepSeek-R1-Distill-Qwen-7B`\n- **Parameters:** 7B (dense)\n- **Architecture:** Dense transformer (based on Qwen2.5-7B)\n- **Release date:** January 20, 2025\n- **Gated:** No\n- **Base version exists:** No -- distilled model, not base pretrained\n- **Training data:** Fine-tuned with 800K samples from DeepSeek-R1\n\n---\n\n## Search 2: Phi-4 Base Model\n\n### Phi-4 (14B base)\n- **Full name:** Phi-4\n- **HuggingFace repo:** `microsoft/phi-4`\n- **Parameters:** 14.7B (dense)\n- **Architecture:** Dense decoder-only transformer\n- **Release date:** December 2024 (initially on Azure; open-sourced on HuggingFace January 2025)\n- **Gated:** No (MIT license, fully open access)\n- **Base version exists:** Yes -- `microsoft/phi-4` IS the base pretrained model\n- **Training data:** 9.8T tokens; mix of synthetic data (generated by GPT-4o), high-quality web content, educational data, code, academic books, Q&A datasets\n- **Context length:** 16K tokens\n- **Benchmarks:** MMLU: 84.8%, MATH: 80.4%, HumanEval: 82.6%\n\n### Phi-4-reasoning (14B, fine-tuned)\n- **Full name:** Phi-4-reasoning\n- **HuggingFace repo:** `microsoft/Phi-4-reasoning`\n- **Parameters:** 14B (dense)\n- **Release date:** April 30, 2025\n- **Gated:** No (MIT license)\n- **Base version exists:** Not a base model; fine-tuned from Phi-4 for reasoning\n- **Benchmarks:** AIME 2024: 75.3%\n\n### Phi-4-reasoning-plus (14B, fine-tuned)\n- **Full name:** Phi-4-reasoning-plus\n- **HuggingFace repo:** `microsoft/Phi-4-reasoning-plus`\n- **Parameters:** 14B (dense)\n- **Release date:** April 30, 2025\n- **Gated:** No (MIT license)\n- **Base version exists:** Not a base model\n- **Benchmarks:** AIME 2024: 81.3%\n\n### Phi-4-mini-instruct (3.8B, NOT in 7B-14B range)\n- **Full name:** Phi-4-mini-instruct\n- **HuggingFace repo:** `microsoft/Phi-4-mini-instruct`\n- **Parameters:** 3.8B (dense)\n- **Release date:** March 19, 2026\n- **Training data:** 5T tokens\n- **Context length:** 128K tokens\n- **Benchmarks:** MMLU: ~73% (matches Llama 3.1 8B)\n- **NOT in 7B-14B range**\n\n---\n\n## Search 3: DeepSeek R2\n\n**DeepSeek R2 has NOT been released as of May 2026.** Key findings:\n\n- DeepSeek R2 was widely anticipated as the second-generation reasoning model.\n- It was reportedly slated for release in H1 2025 but was delayed.\n- The delay was caused by failed training runs on Huawei Ascend AI chips (stability problems, slow interconnect, immature software tooling).\n- As of April 2026, DeepSeek instead released DeepSeek-V4-Pro (1.6T parameters) and DeepSeek-V4-Flash (284B parameters) with 1M token context windows.\n- R2 is NOT listed in the official DeepSeek API model list as of May 2026.\n- No HuggingFace repository exists for DeepSeek R2.\n\n---\n\n## Additional Models Found in the 7B-14B Range (2025-2026)\n\n### Qwen3-14B-Base\n- **HuggingFace repo:** `Qwen/Qwen3-14B-Base`\n- **Parameters:** 14B (dense)\n- **Architecture:** Dense transformer\n- **Release date:** April 29, 2025\n- **Gated:** No (Apache 2.0)\n- **Base version exists:** Yes (this IS the base)\n- **Training data:** ~36T tokens covering 119 languages (3-stage pretraining: S1 >30T tokens at 4K context, S2 +5T tokens STEM-heavy, S3 long-context extension to 32K)\n- **Benchmarks:** MMLU: 81.05 (base model). Performance matches Qwen2.5-32B-Base.\n\n### Qwen3-8B-Base\n- **HuggingFace repo:** `Qwen/Qwen3-8B-Base`\n- **Parameters:** 8B (dense)\n- **Architecture:** Dense transformer\n- **Release date:** April 29, 2025\n- **Gated:** No (Apache 2.0)\n- **Base version exists:** Yes\n- **Training data:** ~36T tokens (same corpus as all Qwen3 models)\n- **Benchmarks:** Performance matches Qwen2.5-14B-Base\n\n### Gemma 3 12B (pretrained base)\n- **Full name:** Gemma 3 12B PT\n- **HuggingFace repo:** `google/gemma-3-12b-pt`\n- **Parameters:** 12B (dense)\n- **Architecture:** Dense transformer, multimodal (text+image input, text output)\n- **Release date:** March 12, 2025\n- **Gated:** Yes (requires agreeing to Google's usage license on HuggingFace)\n- **Base version exists:** Yes (`google/gemma-3-12b-pt` is the pretrained base)\n- **Training data:** 12T tokens\n- **Context length:** 128K tokens\n- **Benchmarks:** Specific MMLU for 12B not retrieved; 27B version: MMLU-Pro 67.5\n\n### Ministral-3-14B-Base-2512\n- **Full name:** Ministral 3 14B Base\n- **HuggingFace repo:** `mistralai/Ministral-3-14B-Base-2512`\n- **Parameters:** 14B (dense)\n- **Architecture:** Dense transformer with vision capabilities\n- **Release date:** December 1, 2025\n- **Gated:** No (Apache 2.0)\n- **Base version exists:** Yes (this IS the base)\n- **Training data:** Not publicly disclosed. Trained via cascade distillation from Mistral Small 3.1 (24B parent)\n- **Vocab size:** 131K tokens\n- **Benchmarks:** Multilingual MMLU: 74.2%. Reasoning variant achieves 85% on AIME 2025.\n\n### Ministral-3-8B-Base-2512\n- **Full name:** Ministral 3 8B Base\n- **HuggingFace repo:** `mistralai/Ministral-3-8B-Base-2512`\n- **Parameters:** 8B (dense)\n- **Architecture:** Dense transformer with vision capabilities\n- **Release date:** December 1, 2025\n- **Gated:** No (Apache 2.0)\n- **Base version exists:** Yes\n- **Training data:** Not disclosed. Cascade distillation from Ministral 3 14B.\n- **Benchmarks:** Multilingual MMLU: 70.6%. Outperforms Gemma 3 12B on most evaluations except TriviaQA.\n\n### Llama 4 Scout (out of strict 7B-14B range but noteworthy for active params)\n- **Full name:** Llama 4 Scout 17B-16E\n- **HuggingFace repo:** `meta-llama/Llama-4-Scout-17B-16E`\n- **Total parameters:** ~109B\n- **Active parameters:** 17B per token\n- **Architecture:** MoE (16 experts)\n- **Release date:** April 2025\n- **Gated:** Yes (Meta Community License, 700M MAU clause)\n- **Base version exists:** Yes (base and instruct variants both available)\n- **Training data:** ~40T tokens (multimodal)\n- **Context length:** 256K (pretrained), 10M (instruct)\n- **Note:** While total params are 109B, active params (17B) are close to the 14B range. This is an MoE model.\n\n---\n\n## Summary Table: Models with Base Versions in the 7B-14B Dense Parameter Range\n\n| Model | HF Repo ID | Params | Architecture | Release | License | Gated | Training Data | Base Exists | MMLU |\n|---|---|---|---|---|---|---|---|---|---|\n| **Phi-4** | `microsoft/phi-4` | 14.7B dense | Dense | Dec 2024 / Jan 2025 | MIT | No | 9.8T tokens | Yes | 84.8% |\n| **Qwen3-14B** | `Qwen/Qwen3-14B-Base` | 14B dense | Dense | Apr 29, 2025 | Apache 2.0 | No | ~36T tokens | Yes | 81.05% |\n| **Qwen3-8B** | `Qwen/Qwen3-8B-Base` | 8B dense | Dense | Apr 29, 2025 | Apache 2.0 | No | ~36T tokens | Yes | -- |\n| **Gemma 3 12B** | `google/gemma-3-12b-pt` | 12B dense | Dense | Mar 12, 2025 | Gemma license | Yes | 12T tokens | Yes | -- |\n| **Ministral 3 14B** | `mistralai/Ministral-3-14B-Base-2512` | 14B dense | Dense | Dec 1, 2025 | Apache 2.0 | No | Undisclosed | Yes | 74.2% (multilingual) |\n| **Ministral 3 8B** | `mistralai/Ministral-3-8B-Base-2512` | 8B dense | Dense | Dec 1, 2025 | Apache 2.0 | No | Undisclosed | Yes | 70.6% (multilingual) |\n| **DeepSeek-V2-Lite** | `deepseek-ai/DeepSeek-V2-Lite` | 15.7B total / **2.4B active** | **MoE** | May 7, 2024 | MIT | No | 5.7T tokens | Yes | -- |\n| **DeepSeek-Coder-V2-Lite** | `deepseek-ai/DeepSeek-Coder-V2-Lite-Base` | 15.7B total / **2.4B active** | **MoE** | Jun 2024 | MIT | No | Undisclosed | Yes | -- |\n\n## MoE Models Near the Range (for reference)\n\n| Model | Total Params | Active Params | Experts | Notes |\n|---|---|---|---|---|\n| DeepSeek-V2-Lite | 15.7B | 2.4B | 64 routed + 2 shared, 6 active | Smallest DeepSeek MoE |\n| DeepSeek-Coder-V2-Lite | 15.7B | 2.4B | Same as above | Code-focused variant |\n| Llama 4 Scout | ~109B | 17B | 16 experts | Active params close to range |\n| Gemma 4 26B-A4B | 25.2B | 3.8B | MoE | Out of range but notable |\n| DeepSeek-V3 | 671B | 37B | 256 experts | Far out of range |\n\n## Key Takeaway for Your Paper\n\nFor an academic paper needing open-source base (non-instruct) LLMs in the 7B-14B dense parameter range released in 2025-2026, the strongest candidates are:\n\n1. **Phi-4** (`microsoft/phi-4`) -- 14.7B, MIT, not gated, highest MMLU at 84.8%\n2. **Qwen3-14B-Base** (`Qwen/Qwen3-14B-Base`) -- 14B, Apache 2.0, not gated, MMLU 81.05%, largest training corpus (36T tokens)\n3. **Qwen3-8B-Base** (`Qwen/Qwen3-8B-Base`) -- 8B, Apache 2.0, not gated\n4. **Gemma 3 12B PT** (`google/gemma-3-12b-pt`) -- 12B, gated (license agreement required)\n5. **Ministral 3 14B Base** (`mistralai/Ministral-3-14B-Base-2512`) -- 14B, Apache 2.0, Dec 2025\n6. **Ministral 3 8B Base** (`mistralai/Ministral-3-8B-Base-2512`) -- 8B, Apache 2.0, Dec 2025\n\nDeepSeek R2 does not exist yet. DeepSeek V3 is far too large (671B). The DeepSeek-R1-Distill models (7B/14B) exist but are fine-tuned reasoning models, not base pretrained models."
      }
    ],
    "totalDurationMs": 198282,
    "totalTokens": 46413,
    "totalToolUseCount": 24,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3858,
      "cache_read_input_tokens": 38062,
      "output_tokens": 4492,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3858
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4492,
          "cache_read_input_tokens": 38062,
          "cache_creation_input_tokens": 3858,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3858,
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
      "otherToolCount": 24
    }
  },
  "sourceToolAssistantUUID": "faccd5e5-3705-46db-bae1-72dc2de8c36a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-18T07:11:31.980Z_

<details><summary>↩ Tool result · `toolu_019GEYgwrqvsAqC9HcwLnZ7s`</summary>

```text
Now I have comprehensive data. Here is the structured compilation of all findings.

---

## Open-Source Base LLMs (7B-14B Parameters) Released 2024-2026

### 1. Qwen3-8B-Base (Alibaba)

| Field | Detail |
|---|---|
| **Full Name** | Qwen3-8B-Base |
| **HuggingFace Repo** | `Qwen/Qwen3-8B-Base` |
| **Parameters** | 8B (7.6B non-embedding) |
| **Release Date** | May 2025 |
| **Gated** | No (Apache 2.0) |
| **Base Version Exists** | Yes |
| **Training Data** | 36T tokens, 119 languages |
| **Benchmarks** | MMLU ~74.7; performs on par with Qwen2.5-14B-Base. Top HumanEval (76.0) under 8B. Strong CJK multilingual. |

### 2. Qwen3-14B-Base (Alibaba)

| Field | Detail |
|---|---|
| **Full Name** | Qwen3-14B-Base |
| **HuggingFace Repo** | `Qwen/Qwen3-14B-Base` |
| **Parameters** | 14.8B (13.2B non-embedding), 40 layers, GQA (40 Q heads / 8 KV heads) |
| **Release Date** | May 2025 |
| **Gated** | No (Apache 2.0) |
| **Base Version Exists** | Yes |
| **Training Data** | 36T tokens, 119 languages |
| **Benchmarks** | Performs on par with Qwen2.5-32B-Base; outperforms larger Qwen2.5 in STEM, coding, reasoning. Context 32K. |

### 3. Qwen2.5-7B (Alibaba)

| Field | Detail |
|---|---|
| **Full Name** | Qwen2.5-7B |
| **HuggingFace Repo** | `Qwen/Qwen2.5-7B` |
| **Parameters** | 7B |
| **Release Date** | September 2024 |
| **Gated** | No (Apache 2.0) |
| **Base Version Exists** | Yes |
| **Training Data** | 18T tokens |
| **Benchmarks** | MMLU 74.2, MATH 49.8, HumanEval 57.9. Context 128K, generates up to 8K tokens. |

### 4. Qwen2.5-14B (Alibaba)

| Field | Detail |
|---|---|
| **Full Name** | Qwen2.5-14B |
| **HuggingFace Repo** | `Qwen/Qwen2.5-14B` |
| **Parameters** | 14B |
| **Release Date** | September 2024 |
| **Gated** | No (Apache 2.0) |
| **Base Version Exists** | Yes |
| **Training Data** | Up to 18T tokens |
| **Benchmarks** | MMLU 79.7. Context 128K. |

### 5. Qwen2.5-Coder-7B (Alibaba)

| Field | Detail |
|---|---|
| **Full Name** | Qwen2.5-Coder-7B |
| **HuggingFace Repo** | `Qwen/Qwen2.5-Coder-7B` |
| **Parameters** | 7B |
| **Release Date** | Late 2024 |
| **Gated** | No (Apache 2.0) |
| **Base Version Exists** | Yes |
| **Training Data** | 5.5T tokens (source code, text-code grounding, synthetic data) |
| **Benchmarks** | Outperforms general-purpose models 2x its size on code generation. Fits 8GB VRAM. |

### 6. Qwen2.5-Coder-14B (Alibaba)

| Field | Detail |
|---|---|
| **Full Name** | Qwen2.5-Coder-14B |
| **HuggingFace Repo** | `Qwen/Qwen2.5-Coder-14B` |
| **Parameters** | 14B |
| **Release Date** | Late 2024 |
| **Gated** | No (Apache 2.0) |
| **Base Version Exists** | Yes |
| **Training Data** | 5.5T tokens |
| **Benchmarks** | Sweet spot for 16GB VRAM; stronger multi-file reasoning and algorithm implementation vs 7B. |

### 7. Gemma 3 12B (Google)

| Field | Detail |
|---|---|
| **Full Name** | Gemma 3 12B |
| **HuggingFace Repo** | `google/gemma-3-12b-pt` (pretrained) / `google/gemma-3-12b-it` (instruct) |
| **Parameters** | 12B |
| **Release Date** | March 12, 2025 |
| **Gated** | Yes (requires Google usage license agreement) |
| **Base Version Exists** | Yes (`gemma-3-12b-pt`) |
| **Training Data** | 12T tokens |
| **Benchmarks** | Global-MMLU-Lite 69.4 (base); MMLU-Pro 59.5 (IT). Native vision support, 128K context, 140+ languages. |

### 8. Gemma 2 9B (Google)

| Field | Detail |
|---|---|
| **Full Name** | Gemma 2 9B |
| **HuggingFace Repo** | `google/gemma-2-9b` |
| **Parameters** | 9B |
| **Release Date** | July 2024 |
| **Gated** | Yes (Google usage license) |
| **Base Version Exists** | Yes |
| **Training Data** | 8T tokens; trained with knowledge distillation |
| **Benchmarks** | OpenLLM v1 average 73.23 (IT). Interleaved local/global attention, GQA. Competitive with 2x-size models. |

### 9. Phi-4 14B (Microsoft)

| Field | Detail |
|---|---|
| **Full Name** | Phi-4 |
| **HuggingFace Repo** | `microsoft/phi-4` |
| **Parameters** | 14.7B |
| **Release Date** | December 2024 |
| **Gated** | No (MIT license) |
| **Base Version Exists** | Yes (the `microsoft/phi-4` model is the base) |
| **Training Data** | Extension of Phi-3 data: filtered web docs, educational data, synthetic "textbook-like" data for math/coding/reasoning, academic books, Q&A datasets. ~8% multilingual. |
| **Benchmarks** | MMLU 84.8 (surpasses Llama-3.3-70B). Q5_K_M variant reaches 76.2 MMLU. Strong in reasoning and math. |

### 10. Llama 3.1 8B (Meta)

| Field | Detail |
|---|---|
| **Full Name** | Llama 3.1 8B |
| **HuggingFace Repo** | `meta-llama/Llama-3.1-8B` |
| **Parameters** | 8B |
| **Release Date** | July 23, 2024 |
| **Gated** | Yes (Llama 3.1 Community License) |
| **Base Version Exists** | Yes |
| **Training Data** | ~15T multilingual tokens |
| **Benchmarks** | MMLU 65.6 (5-shot, base). 128K context window. |

### 11. Llama 3 8B (Meta)

| Field | Detail |
|---|---|
| **Full Name** | Meta-Llama-3-8B |
| **HuggingFace Repo** | `meta-llama/Meta-Llama-3-8B` |
| **Parameters** | 8B |
| **Release Date** | April 18, 2024 |
| **Gated** | Yes (Llama 3 Community License) |
| **Base Version Exists** | Yes |
| **Training Data** | ~15T tokens |
| **Benchmarks** | Predecessor to 3.1; widely used baseline. |

### 12. DeepSeek-R1-Distill-Qwen-7B (DeepSeek)

| Field | Detail |
|---|---|
| **Full Name** | DeepSeek-R1-Distill-Qwen-7B |
| **HuggingFace Repo** | `deepseek-ai/DeepSeek-R1-Distill-Qwen-7B` |
| **Parameters** | 7B |
| **Release Date** | January 2025 |
| **Gated** | No (Apache 2.0, inherited from Qwen2.5) |
| **Base Version Exists** | This is a distilled/fine-tuned model (from Qwen2.5 base), not a pretrained-from-scratch base |
| **Training Data** | Distilled from DeepSeek-R1 with 800K curated reasoning samples |
| **Benchmarks** | Strong chain-of-thought reasoning; inherits R1's reasoning capabilities at 7B scale. |

### 13. DeepSeek-R1-Distill-Qwen-14B (DeepSeek)

| Field | Detail |
|---|---|
| **Full Name** | DeepSeek-R1-Distill-Qwen-14B |
| **HuggingFace Repo** | `deepseek-ai/DeepSeek-R1-Distill-Qwen-14B` |
| **Parameters** | 14B |
| **Release Date** | January 2025 |
| **Gated** | No (Apache 2.0, inherited from Qwen2.5) |
| **Base Version Exists** | Distilled model, not pretrained base |
| **Training Data** | 800K curated samples from DeepSeek-R1 |
| **Benchmarks** | Strongest distilled reasoning model at 14B scale. |

### 14. DeepSeek-R1-Distill-Llama-8B (DeepSeek)

| Field | Detail |
|---|---|
| **Full Name** | DeepSeek-R1-Distill-Llama-8B |
| **HuggingFace Repo** | `deepseek-ai/DeepSeek-R1-Distill-Llama-8B` |
| **Parameters** | 8B |
| **Release Date** | January 2025 |
| **Gated** | Llama 3.1 license (inherited from Llama3.1-8B-Base) |
| **Base Version Exists** | Distilled model built on Llama 3.1 8B base |
| **Training Data** | 800K curated samples from DeepSeek-R1 |
| **Benchmarks** | Reasoning-enhanced Llama variant. |

### 15. Falcon 3 7B (TII)

| Field | Detail |
|---|---|
| **Full Name** | Falcon3-7B-Base |
| **HuggingFace Repo** | `tiiuae/Falcon3-7B-Base` |
| **Parameters** | 7B |
| **Release Date** | December 2024 |
| **Gated** | No (TII Falcon License 2.0; compatible with Llama architecture) |
| **Base Version Exists** | Yes |
| **Training Data** | 14T tokens (web, code, STEM, multilingual: EN/FR/ES/PT) |
| **Benchmarks** | MMLU 67.4, MMLU-PRO 39.2. On par with Qwen2.5-7B among sub-9B models. |

### 16. Falcon 3 10B (TII)

| Field | Detail |
|---|---|
| **Full Name** | Falcon3-10B-Base |
| **HuggingFace Repo** | `tiiuae/Falcon3-10B-Base` |
| **Parameters** | 10B |
| **Release Date** | December 2024 |
| **Gated** | No |
| **Base Version Exists** | Yes |
| **Training Data** | Upscaled from 7B + 2T additional tokens (web, code, STEM) |
| **Benchmarks** | MMLU 73.1, MMLU-PRO 42.5. SOTA zero-shot and few-shot for sub-13B models. |

### 17. Falcon-H1-7B (TII)

| Field | Detail |
|---|---|
| **Full Name** | Falcon-H1-7B-Base |
| **HuggingFace Repo** | `tiiuae/Falcon-H1-7B-Base` |
| **Parameters** | 7B |
| **Release Date** | 2025 |
| **Gated** | No |
| **Base Version Exists** | Yes |
| **Training Data** | Not specified in search results |
| **Benchmarks** | Hybrid Transformer + SSM (Mamba) architecture. 256K context. 18 native languages. Adjustable attention/SSM ratio for efficiency. |

### 18. OLMo 2 7B (Allen AI)

| Field | Detail |
|---|---|
| **Full Name** | OLMo-2-1124-7B |
| **HuggingFace Repo** | `allenai/OLMo-2-1124-7B` |
| **Parameters** | 7B |
| **Release Date** | November 2024 |
| **Gated** | No (fully open: data, code, weights, training logs) |
| **Base Version Exists** | Yes |
| **Training Data** | ~5T tokens (OLMo-Mix-1124: DCLM, Dolma, Starcoder, Proof Pile II) |
| **Benchmarks** | MMLU 63.7. Outperforms Llama-3.1-8B. Staged training approach. |

### 19. OLMo 2 13B (Allen AI)

| Field | Detail |
|---|---|
| **Full Name** | OLMo-2-1124-13B |
| **HuggingFace Repo** | `allenai/OLMo-2-1124-13B` |
| **Parameters** | 13B |
| **Release Date** | November 2024 |
| **Gated** | No (fully open) |
| **Base Version Exists** | Yes |
| **Training Data** | ~5T tokens (1.2 epochs) |
| **Benchmarks** | MMLU 67.5. Outperforms Qwen2.5-7B despite lower training FLOPs. |

### 20. OLMo 3 7B (Allen AI)

| Field | Detail |
|---|---|
| **Full Name** | Olmo-3-1025-7B |
| **HuggingFace Repo** | `allenai/Olmo-3-1025-7B` |
| **Parameters** | 7B |
| **Release Date** | October 2025 |
| **Gated** | No (Apache 2.0; fully open) |
| **Base Version Exists** | Yes |
| **Training Data** | ~5.93T tokens (dolma3_6T-mix-1025). Mix: 20% code, 28% web, 19% math, 14% QA, 8% thinking, 6% instruction, 5% PDFs. |
| **Benchmarks** | Successor to OLMo 2; details in paper at allenai.org/papers/olmo3. |

### 21. Mistral Nemo 12B (Mistral AI / NVIDIA)

| Field | Detail |
|---|---|
| **Full Name** | Mistral-NeMo-12B-Base |
| **HuggingFace Repo** | `mistralai/Mistral-Nemo-Base-2407` (also `nvidia/Mistral-NeMo-12B-Base`) |
| **Parameters** | 12B |
| **Release Date** | July 2024 |
| **Gated** | No (Apache 2.0) |
| **Base Version Exists** | Yes |
| **Training Data** | Trained May-June 2024; 80+ programming languages, multilingual (EN/FR/DE/ES/IT/PT/ZH/JA/KO/AR/HI) |
| **Benchmarks** | MMLU 68.0 (5-shot), HellaSwag 83.5, Winogrande 76.8, TriviaQA 73.8. Outperforms Gemma 2 9B and Llama 3 8B. |

### 22. InternLM3 8B (Shanghai AI Lab)

| Field | Detail |
|---|---|
| **Full Name** | InternLM3-8B |
| **HuggingFace Repo** | `internlm/internlm3-8b-instruct` (instruct version released; base checkpoint may be in the `internlm` collection) |
| **Parameters** | 8B |
| **Release Date** | January 15, 2025 |
| **Gated** | No |
| **Base Version Exists** | Instruct version publicly available; base checkpoint availability unclear from search results |
| **Training Data** | 4T tokens (claimed 75% training cost savings vs comparable models) |
| **Benchmarks** | Surpasses Llama3.1-8B and Qwen2.5-7B on reasoning/knowledge tasks. Supports deep thinking (long CoT) mode. |

### 23. Yi-1.5-9B (01.AI)

| Field | Detail |
|---|---|
| **Full Name** | Yi-1.5-9B |
| **HuggingFace Repo** | `01-ai/Yi-1.5-9B` |
| **Parameters** | 9B |
| **Release Date** | May 13, 2024 |
| **Gated** | No (Apache 2.0) |
| **Base Version Exists** | Yes |
| **Training Data** | Bilingual (EN/ZH); 34B variant trained on 3.1T tokens (9B likely similar or subset) |
| **Benchmarks** | MMLU 76.3, BBH 54.3, C-Eval 81.4. Top performer among similarly sized open-source models. GQA + SwiGLU architecture. |

### 24. MAP-Neo 7B (MAP)

| Field | Detail |
|---|---|
| **Full Name** | MAP-Neo 7B |
| **HuggingFace Repo** | `m-a-p/neo_7b` |
| **Parameters** | 7B |
| **Release Date** | Mid 2024 |
| **Gated** | No (commercial use permitted) |
| **Base Version Exists** | Yes |
| **Training Data** | 4.5T tokens (English + Chinese). Fully open: data pipeline, cleaning code, all checkpoints, tokenizer. |
| **Benchmarks** | Comparable to LLaMA 2 7B. Strong in reasoning, math, coding. Fully reproducible (all artifacts released). |

### 25. StarCoder2-7B (BigCode)

| Field | Detail |
|---|---|
| **Full Name** | StarCoder2-7B |
| **HuggingFace Repo** | `bigcode/starcoder2-7b` |
| **Parameters** | 7B |
| **Release Date** | February 28, 2024 |
| **Gated** | No (BigCode OpenRAIL-M v1) |
| **Base Version Exists** | Yes (code-only base model) |
| **Training Data** | 3.5T+ tokens, 17 programming languages (The Stack v2) |
| **Benchmarks** | Code generation specialist. GQA, 16K context, sliding window attention 4K. Fill-in-the-Middle objective. |

### 26. StarCoder2-15B (BigCode)

| Field | Detail |
|---|---|
| **Full Name** | StarCoder2-15B |
| **HuggingFace Repo** | `bigcode/starcoder2-15b` |
| **Parameters** | 15B (slightly above 14B range, included for completeness) |
| **Release Date** | February 28, 2024 |
| **Gated** | No (BigCode OpenRAIL-M v1) |
| **Base Version Exists** | Yes (code-only base model) |
| **Training Data** | 4T+ tokens, 600+ programming languages (The Stack v2) |
| **Benchmarks** | Strongest code model in its size class at release. 16K context. |

### 27. Mistral Small 3 24B (Mistral AI) [NOTE: Not 7B]

| Field | Detail |
|---|---|
| **Full Name** | Mistral-Small-24B-Base-2501 |
| **HuggingFace Repo** | `mistralai/Mistral-Small-24B-Base-2501` (also Instruct: `mistralai/Mistral-Small-3.1-24B-Instruct-2503`) |
| **Parameters** | 24B (outside 7B-14B range) |
| **Release Date** | January 2025 |
| **Gated** | No |
| **Base Version Exists** | Yes |
| **Note** | Included because some sources incorrectly describe it as "7B." Actual parameter count is 24B. MMLU >81%, ~150 tokens/s, MT-Bench 8.0. |

---

## Summary: Models Strictly in 7B-14B Range with Base Versions Available

| Model | Params | Release | License | Training Data | MMLU (base) | HF Repo |
|---|---|---|---|---|---|---|
| Qwen3-8B-Base | 8B | May 2025 | Apache 2.0 | 36T tokens | ~74.7 | `Qwen/Qwen3-8B-Base` |
| Qwen3-14B-Base | 14.8B | May 2025 | Apache 2.0 | 36T tokens | ~Qwen2.5-32B level | `Qwen/Qwen3-14B-Base` |
| Qwen2.5-7B | 7B | Sep 2024 | Apache 2.0 | 18T tokens | 74.2 | `Qwen/Qwen2.5-7B` |
| Qwen2.5-14B | 14B | Sep 2024 | Apache 2.0 | 18T tokens | 79.7 | `Qwen/Qwen2.5-14B` |
| Qwen2.5-Coder-7B | 7B | Late 2024 | Apache 2.0 | 5.5T tokens | Code specialist | `Qwen/Qwen2.5-Coder-7B` |
| Qwen2.5-Coder-14B | 14B | Late 2024 | Apache 2.0 | 5.5T tokens | Code specialist | `Qwen/Qwen2.5-Coder-14B` |
| Phi-4 | 14.7B | Dec 2024 | MIT | Synthetic+web+academic | 84.8 | `microsoft/phi-4` |
| Gemma 3 12B | 12B | Mar 2025 | Google license (gated) | 12T tokens | GMMLU 69.4 | `google/gemma-3-12b-pt` |
| Gemma 2 9B | 9B | Jul 2024 | Google license (gated) | 8T tokens | ~68-70 est. | `google/gemma-2-9b` |
| Llama 3.1 8B | 8B | Jul 2024 | Llama license (gated) | 15T tokens | 65.6 | `meta-llama/Llama-3.1-8B` |
| Mistral Nemo 12B | 12B | Jul 2024 | Apache 2.0 | Multilingual | 68.0 | `mistralai/Mistral-Nemo-Base-2407` |
| Falcon3-7B | 7B | Dec 2024 | Falcon License 2.0 | 14T tokens | 67.4 | `tiiuae/Falcon3-7B-Base` |
| Falcon3-10B | 10B | Dec 2024 | Falcon License 2.0 | 7B+2T upscale | 73.1 | `tiiuae/Falcon3-10B-Base` |
| Falcon-H1-7B | 7B | 2025 | Open | Not specified | Hybrid SSM+Attn | `tiiuae/Falcon-H1-7B-Base` |
| OLMo 2 7B | 7B | Nov 2024 | Apache 2.0 (fully open) | 5T tokens | 63.7 | `allenai/OLMo-2-1124-7B` |
| OLMo 2 13B | 13B | Nov 2024 | Apache 2.0 (fully open) | 5T tokens | 67.5 | `allenai/OLMo-2-1124-13B` |
| OLMo 3 7B | 7B | Oct 2025 | Apache 2.0 (fully open) | 5.93T tokens | Improved over OLMo 2 | `allenai/Olmo-3-1025-7B` |
| InternLM3 8B | 8B | Jan 2025 | Open | 4T tokens | Beats Llama3.1-8B | `internlm/internlm3-8b-instruct` |
| Yi-1.5-9B | 9B | May 2024 | Apache 2.0 | ~3T tokens | 76.3 | `01-ai/Yi-1.5-9B` |
| MAP-Neo 7B | 7B | Mid 2024 | Open (commercial OK) | 4.5T tokens | ~LLaMA2-7B level | `m-a-p/neo_7b` |
| StarCoder2-7B | 7B | Feb 2024 | OpenRAIL-M | 3.5T tokens | Code specialist | `bigcode/starcoder2-7b` |
| DeepSeek-R1-Distill-Qwen-7B | 7B | Jan 2025 | Apache 2.0 | 800K reasoning samples | Reasoning specialist | `deepseek-ai/DeepSeek-R1-Distill-Qwen-7B` |
| DeepSeek-R1-Distill-Qwen-14B | 14B | Jan 2025 | Apache 2.0 | 800K reasoning samples | Reasoning specialist | `deepseek-ai/DeepSeek-R1-Distill-Qwen-14B` |
| DeepSeek-R1-Distill-Llama-8B | 8B | Jan 2025 | Llama 3.1 license | 800K reasoning samples | Reasoning specialist | `deepseek-ai/DeepSeek-R1-Distill-Llama-8B` |

---

## Key Observations for Academic Paper Use

1. **Strongest base models by MMLU in range**: Phi-4 (84.8) > Qwen2.5-14B (79.7) > Yi-1.5-9B (76.3) > Qwen3-8B (~74.7) > Qwen2.5-7B (74.2) > Falcon3-10B (73.1)

2. **Fully open models** (data + code + weights): OLMo 2/3 (Allen AI) and MAP-Neo are the only models with complete reproducibility artifacts (training data, pipeline code, all checkpoints).

3. **2025-2026 releases**: Qwen3-8B-Base, Qwen3-14B-Base, Gemma 3 12B, InternLM3-8B, OLMo 3 7B, Falcon-H1-7B, DeepSeek-R1 distilled variants.

4. **Llama 4 does NOT have a dense 7B-14B base model**. Llama 4 uses MoE: Scout (109B total, 17B active) and Maverick (400B total, 17B active). The last dense Llama base in this range is Llama 3.1 8B.

5. **Gated models** requiring license agreement: All Gemma models (Google), all Llama models (Meta). Non-gated: Qwen, Phi-4, Falcon, OLMo, Mistral Nemo, Yi, MAP-Neo, StarCoder2.

6. **Gemma 4** was released April 2, 2026 but its sizes are E2B, E4B, 26B-A4B, and 31B (none in the 7B-14B dense range).

Sources:
- [Qwen3-8B-Base on HuggingFace](https://huggingface.co/Qwen/Qwen3-8B-Base)
- [Qwen3 Blog Post](https://qwenlm.github.io/blog/qwen3/)
- [Qwen3-14B-Base on HuggingFace](https://huggingface.co/Qwen/Qwen3-14B-Base)
- [Qwen2.5-7B on HuggingFace](https://huggingface.co/Qwen/Qwen2.5-7B)
- [Qwen2.5-14B on HuggingFace](https://huggingface.co/Qwen/Qwen2.5-14B)
- [Qwen2.5 Technical Report](https://arxiv.org/pdf/2412.15115)
- [Phi-4 on HuggingFace](https://huggingface.co/microsoft/phi-4)
- [Phi-4 Technical Report](https://arxiv.org/html/2412.08905v1)
- [Gemma 3 12B Pretrained](https://huggingface.co/google/gemma-3-12b-pt)
- [Gemma 3 Blog](https://huggingface.co/blog/gemma3)
- [Gemma 2 9B](https://huggingface.co/google/gemma-2-9b)
- [Llama 3.1 8B](https://huggingface.co/meta-llama/Llama-3.1-8B)
- [Mistral Nemo Base](https://huggingface.co/mistralai/Mistral-Nemo-Base-2407)
- [Falcon3-7B-Base](https://huggingface.co/tiiuae/Falcon3-7B-Base)
- [Falcon3-10B-Base](https://huggingface.co/tiiuae/Falcon3-10B-Base)
- [Falcon3 Blog](https://huggingface.co/blog/falcon3)
- [Falcon-H1 Blog](https://falcon-lm.github.io/blog/falcon-h1/)
- [OLMo 2 Collection](https://huggingface.co/collections/allenai/olmo-2)
- [OLMo 2 Blog](https://allenai.org/blog/olmo2)
- [OLMo 3 7B](https://huggingface.co/allenai/Olmo-3-1025-7B)
- [InternLM3-8B](https://huggingface.co/internlm/internlm3-8b-instruct)
- [Yi-1.5-9B](https://huggingface.co/01-ai/Yi-1.5-9B)
- [MAP-Neo 7B](https://huggingface.co/m-a-p/neo_7b)
- [StarCoder2-7B](https://huggingface.co/bigcode/starcoder2-7b)
- [DeepSeek-R1-Distill-Qwen-7B](https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-7B)
- [DeepSeek-R1-Distill-Qwen-14B](https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-14B)
- [Open-Source LLM Landscape 2026](https://presenc.ai/research/open-source-llm-landscape-2026)
- [Featherless Best Open-Source LLMs 2026](https://featherless.ai/blog/best-open-source-llms-2026)
- [HuggingFace State of Open Source Spring 2026](https://huggingface.co/blog/huggingface/state-of-os-hf-spring-2026)
- [Gemma 4 Overview](https://ai.google.dev/gemma/docs/core)

agentId: a07b72467ddf2db7b (use SendMessage with to: 'a07b72467ddf2db7b' to continue this agent)
&lt;usage>total_tokens: 57338
tool_uses: 33
duration_ms: 233530&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "45f9c1d2-c26b-4532-b966-e7ffa02a770c",
  "isSidechain": false,
  "promptId": "04205c35-fa25-4f0b-9c44-5def633915cd",
  "type": "user",
  "uuid": "c96b92d4-ef3e-48e4-b0ed-2ca63b335621",
  "toolUseResult": {
    "status": "completed",
    "prompt": "You are researching the latest open-source base LLMs (7B-14B parameters) released in 2025-2026 for an academic paper. Run the following 3 web searches and compile ALL results with as much detail as possible. For each model found, note: full name, HuggingFace repo ID, parameter count, release date, whether it's gated, whether a base (non-instruct) version exists, training data size if mentioned, and benchmark performance if mentioned.\n\nSearch 1: \"best open source LLM 2025 2026 base model\"\nSearch 2: \"latest base models huggingface 2025\"\nSearch 3: \"new open source LLM families 2025 2026\"\n\nReturn ALL findings in a structured format. Be thorough - list every model you find in the 7B-14B range.",
    "agentId": "a07b72467ddf2db7b",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Now I have comprehensive data. Here is the structured compilation of all findings.\n\n---\n\n## Open-Source Base LLMs (7B-14B Parameters) Released 2024-2026\n\n### 1. Qwen3-8B-Base (Alibaba)\n\n| Field | Detail |\n|---|---|\n| **Full Name** | Qwen3-8B-Base |\n| **HuggingFace Repo** | `Qwen/Qwen3-8B-Base` |\n| **Parameters** | 8B (7.6B non-embedding) |\n| **Release Date** | May 2025 |\n| **Gated** | No (Apache 2.0) |\n| **Base Version Exists** | Yes |\n| **Training Data** | 36T tokens, 119 languages |\n| **Benchmarks** | MMLU ~74.7; performs on par with Qwen2.5-14B-Base. Top HumanEval (76.0) under 8B. Strong CJK multilingual. |\n\n### 2. Qwen3-14B-Base (Alibaba)\n\n| Field | Detail |\n|---|---|\n| **Full Name** | Qwen3-14B-Base |\n| **HuggingFace Repo** | `Qwen/Qwen3-14B-Base` |\n| **Parameters** | 14.8B (13.2B non-embedding), 40 layers, GQA (40 Q heads / 8 KV heads) |\n| **Release Date** | May 2025 |\n| **Gated** | No (Apache 2.0) |\n| **Base Version Exists** | Yes |\n| **Training Data** | 36T tokens, 119 languages |\n| **Benchmarks** | Performs on par with Qwen2.5-32B-Base; outperforms larger Qwen2.5 in STEM, coding, reasoning. Context 32K. |\n\n### 3. Qwen2.5-7B (Alibaba)\n\n| Field | Detail |\n|---|---|\n| **Full Name** | Qwen2.5-7B |\n| **HuggingFace Repo** | `Qwen/Qwen2.5-7B` |\n| **Parameters** | 7B |\n| **Release Date** | September 2024 |\n| **Gated** | No (Apache 2.0) |\n| **Base Version Exists** | Yes |\n| **Training Data** | 18T tokens |\n| **Benchmarks** | MMLU 74.2, MATH 49.8, HumanEval 57.9. Context 128K, generates up to 8K tokens. |\n\n### 4. Qwen2.5-14B (Alibaba)\n\n| Field | Detail |\n|---|---|\n| **Full Name** | Qwen2.5-14B |\n| **HuggingFace Repo** | `Qwen/Qwen2.5-14B` |\n| **Parameters** | 14B |\n| **Release Date** | September 2024 |\n| **Gated** | No (Apache 2.0) |\n| **Base Version Exists** | Yes |\n| **Training Data** | Up to 18T tokens |\n| **Benchmarks** | MMLU 79.7. Context 128K. |\n\n### 5. Qwen2.5-Coder-7B (Alibaba)\n\n| Field | Detail |\n|---|---|\n| **Full Name** | Qwen2.5-Coder-7B |\n| **HuggingFace Repo** | `Qwen/Qwen2.5-Coder-7B` |\n| **Parameters** | 7B |\n| **Release Date** | Late 2024 |\n| **Gated** | No (Apache 2.0) |\n| **Base Version Exists** | Yes |\n| **Training Data** | 5.5T tokens (source code, text-code grounding, synthetic data) |\n| **Benchmarks** | Outperforms general-purpose models 2x its size on code generation. Fits 8GB VRAM. |\n\n### 6. Qwen2.5-Coder-14B (Alibaba)\n\n| Field | Detail |\n|---|---|\n| **Full Name** | Qwen2.5-Coder-14B |\n| **HuggingFace Repo** | `Qwen/Qwen2.5-Coder-14B` |\n| **Parameters** | 14B |\n| **Release Date** | Late 2024 |\n| **Gated** | No (Apache 2.0) |\n| **Base Version Exists** | Yes |\n| **Training Data** | 5.5T tokens |\n| **Benchmarks** | Sweet spot for 16GB VRAM; stronger multi-file reasoning and algorithm implementation vs 7B. |\n\n### 7. Gemma 3 12B (Google)\n\n| Field | Detail |\n|---|---|\n| **Full Name** | Gemma 3 12B |\n| **HuggingFace Repo** | `google/gemma-3-12b-pt` (pretrained) / `google/gemma-3-12b-it` (instruct) |\n| **Parameters** | 12B |\n| **Release Date** | March 12, 2025 |\n| **Gated** | Yes (requires Google usage license agreement) |\n| **Base Version Exists** | Yes (`gemma-3-12b-pt`) |\n| **Training Data** | 12T tokens |\n| **Benchmarks** | Global-MMLU-Lite 69.4 (base); MMLU-Pro 59.5 (IT). Native vision support, 128K context, 140+ languages. |\n\n### 8. Gemma 2 9B (Google)\n\n| Field | Detail |\n|---|---|\n| **Full Name** | Gemma 2 9B |\n| **HuggingFace Repo** | `google/gemma-2-9b` |\n| **Parameters** | 9B |\n| **Release Date** | July 2024 |\n| **Gated** | Yes (Google usage license) |\n| **Base Version Exists** | Yes |\n| **Training Data** | 8T tokens; trained with knowledge distillation |\n| **Benchmarks** | OpenLLM v1 average 73.23 (IT). Interleaved local/global attention, GQA. Competitive with 2x-size models. |\n\n### 9. Phi-4 14B (Microsoft)\n\n| Field | Detail |\n|---|---|\n| **Full Name** | Phi-4 |\n| **HuggingFace Repo** | `microsoft/phi-4` |\n| **Parameters** | 14.7B |\n| **Release Date** | December 2024 |\n| **Gated** | No (MIT license) |\n| **Base Version Exists** | Yes (the `microsoft/phi-4` model is the base) |\n| **Training Data** | Extension of Phi-3 data: filtered web docs, educational data, synthetic \"textbook-like\" data for math/coding/reasoning, academic books, Q&A datasets. ~8% multilingual. |\n| **Benchmarks** | MMLU 84.8 (surpasses Llama-3.3-70B). Q5_K_M variant reaches 76.2 MMLU. Strong in reasoning and math. |\n\n### 10. Llama 3.1 8B (Meta)\n\n| Field | Detail |\n|---|---|\n| **Full Name** | Llama 3.1 8B |\n| **HuggingFace Repo** | `meta-llama/Llama-3.1-8B` |\n| **Parameters** | 8B |\n| **Release Date** | July 23, 2024 |\n| **Gated** | Yes (Llama 3.1 Community License) |\n| **Base Version Exists** | Yes |\n| **Training Data** | ~15T multilingual tokens |\n| **Benchmarks** | MMLU 65.6 (5-shot, base). 128K context window. |\n\n### 11. Llama 3 8B (Meta)\n\n| Field | Detail |\n|---|---|\n| **Full Name** | Meta-Llama-3-8B |\n| **HuggingFace Repo** | `meta-llama/Meta-Llama-3-8B` |\n| **Parameters** | 8B |\n| **Release Date** | April 18, 2024 |\n| **Gated** | Yes (Llama 3 Community License) |\n| **Base Version Exists** | Yes |\n| **Training Data** | ~15T tokens |\n| **Benchmarks** | Predecessor to 3.1; widely used baseline. |\n\n### 12. DeepSeek-R1-Distill-Qwen-7B (DeepSeek)\n\n| Field | Detail |\n|---|---|\n| **Full Name** | DeepSeek-R1-Distill-Qwen-7B |\n| **HuggingFace Repo** | `deepseek-ai/DeepSeek-R1-Distill-Qwen-7B` |\n| **Parameters** | 7B |\n| **Release Date** | January 2025 |\n| **Gated** | No (Apache 2.0, inherited from Qwen2.5) |\n| **Base Version Exists** | This is a distilled/fine-tuned model (from Qwen2.5 base), not a pretrained-from-scratch base |\n| **Training Data** | Distilled from DeepSeek-R1 with 800K curated reasoning samples |\n| **Benchmarks** | Strong chain-of-thought reasoning; inherits R1's reasoning capabilities at 7B scale. |\n\n### 13. DeepSeek-R1-Distill-Qwen-14B (DeepSeek)\n\n| Field | Detail |\n|---|---|\n| **Full Name** | DeepSeek-R1-Distill-Qwen-14B |\n| **HuggingFace Repo** | `deepseek-ai/DeepSeek-R1-Distill-Qwen-14B` |\n| **Parameters** | 14B |\n| **Release Date** | January 2025 |\n| **Gated** | No (Apache 2.0, inherited from Qwen2.5) |\n| **Base Version Exists** | Distilled model, not pretrained base |\n| **Training Data** | 800K curated samples from DeepSeek-R1 |\n| **Benchmarks** | Strongest distilled reasoning model at 14B scale. |\n\n### 14. DeepSeek-R1-Distill-Llama-8B (DeepSeek)\n\n| Field | Detail |\n|---|---|\n| **Full Name** | DeepSeek-R1-Distill-Llama-8B |\n| **HuggingFace Repo** | `deepseek-ai/DeepSeek-R1-Distill-Llama-8B` |\n| **Parameters** | 8B |\n| **Release Date** | January 2025 |\n| **Gated** | Llama 3.1 license (inherited from Llama3.1-8B-Base) |\n| **Base Version Exists** | Distilled model built on Llama 3.1 8B base |\n| **Training Data** | 800K curated samples from DeepSeek-R1 |\n| **Benchmarks** | Reasoning-enhanced Llama variant. |\n\n### 15. Falcon 3 7B (TII)\n\n| Field | Detail |\n|---|---|\n| **Full Name** | Falcon3-7B-Base |\n| **HuggingFace Repo** | `tiiuae/Falcon3-7B-Base` |\n| **Parameters** | 7B |\n| **Release Date** | December 2024 |\n| **Gated** | No (TII Falcon License 2.0; compatible with Llama architecture) |\n| **Base Version Exists** | Yes |\n| **Training Data** | 14T tokens (web, code, STEM, multilingual: EN/FR/ES/PT) |\n| **Benchmarks** | MMLU 67.4, MMLU-PRO 39.2. On par with Qwen2.5-7B among sub-9B models. |\n\n### 16. Falcon 3 10B (TII)\n\n| Field | Detail |\n|---|---|\n| **Full Name** | Falcon3-10B-Base |\n| **HuggingFace Repo** | `tiiuae/Falcon3-10B-Base` |\n| **Parameters** | 10B |\n| **Release Date** | December 2024 |\n| **Gated** | No |\n| **Base Version Exists** | Yes |\n| **Training Data** | Upscaled from 7B + 2T additional tokens (web, code, STEM) |\n| **Benchmarks** | MMLU 73.1, MMLU-PRO 42.5. SOTA zero-shot and few-shot for sub-13B models. |\n\n### 17. Falcon-H1-7B (TII)\n\n| Field | Detail |\n|---|---|\n| **Full Name** | Falcon-H1-7B-Base |\n| **HuggingFace Repo** | `tiiuae/Falcon-H1-7B-Base` |\n| **Parameters** | 7B |\n| **Release Date** | 2025 |\n| **Gated** | No |\n| **Base Version Exists** | Yes |\n| **Training Data** | Not specified in search results |\n| **Benchmarks** | Hybrid Transformer + SSM (Mamba) architecture. 256K context. 18 native languages. Adjustable attention/SSM ratio for efficiency. |\n\n### 18. OLMo 2 7B (Allen AI)\n\n| Field | Detail |\n|---|---|\n| **Full Name** | OLMo-2-1124-7B |\n| **HuggingFace Repo** | `allenai/OLMo-2-1124-7B` |\n| **Parameters** | 7B |\n| **Release Date** | November 2024 |\n| **Gated** | No (fully open: data, code, weights, training logs) |\n| **Base Version Exists** | Yes |\n| **Training Data** | ~5T tokens (OLMo-Mix-1124: DCLM, Dolma, Starcoder, Proof Pile II) |\n| **Benchmarks** | MMLU 63.7. Outperforms Llama-3.1-8B. Staged training approach. |\n\n### 19. OLMo 2 13B (Allen AI)\n\n| Field | Detail |\n|---|---|\n| **Full Name** | OLMo-2-1124-13B |\n| **HuggingFace Repo** | `allenai/OLMo-2-1124-13B` |\n| **Parameters** | 13B |\n| **Release Date** | November 2024 |\n| **Gated** | No (fully open) |\n| **Base Version Exists** | Yes |\n| **Training Data** | ~5T tokens (1.2 epochs) |\n| **Benchmarks** | MMLU 67.5. Outperforms Qwen2.5-7B despite lower training FLOPs. |\n\n### 20. OLMo 3 7B (Allen AI)\n\n| Field | Detail |\n|---|---|\n| **Full Name** | Olmo-3-1025-7B |\n| **HuggingFace Repo** | `allenai/Olmo-3-1025-7B` |\n| **Parameters** | 7B |\n| **Release Date** | October 2025 |\n| **Gated** | No (Apache 2.0; fully open) |\n| **Base Version Exists** | Yes |\n| **Training Data** | ~5.93T tokens (dolma3_6T-mix-1025). Mix: 20% code, 28% web, 19% math, 14% QA, 8% thinking, 6% instruction, 5% PDFs. |\n| **Benchmarks** | Successor to OLMo 2; details in paper at allenai.org/papers/olmo3. |\n\n### 21. Mistral Nemo 12B (Mistral AI / NVIDIA)\n\n| Field | Detail |\n|---|---|\n| **Full Name** | Mistral-NeMo-12B-Base |\n| **HuggingFace Repo** | `mistralai/Mistral-Nemo-Base-2407` (also `nvidia/Mistral-NeMo-12B-Base`) |\n| **Parameters** | 12B |\n| **Release Date** | July 2024 |\n| **Gated** | No (Apache 2.0) |\n| **Base Version Exists** | Yes |\n| **Training Data** | Trained May-June 2024; 80+ programming languages, multilingual (EN/FR/DE/ES/IT/PT/ZH/JA/KO/AR/HI) |\n| **Benchmarks** | MMLU 68.0 (5-shot), HellaSwag 83.5, Winogrande 76.8, TriviaQA 73.8. Outperforms Gemma 2 9B and Llama 3 8B. |\n\n### 22. InternLM3 8B (Shanghai AI Lab)\n\n| Field | Detail |\n|---|---|\n| **Full Name** | InternLM3-8B |\n| **HuggingFace Repo** | `internlm/internlm3-8b-instruct` (instruct version released; base checkpoint may be in the `internlm` collection) |\n| **Parameters** | 8B |\n| **Release Date** | January 15, 2025 |\n| **Gated** | No |\n| **Base Version Exists** | Instruct version publicly available; base checkpoint availability unclear from search results |\n| **Training Data** | 4T tokens (claimed 75% training cost savings vs comparable models) |\n| **Benchmarks** | Surpasses Llama3.1-8B and Qwen2.5-7B on reasoning/knowledge tasks. Supports deep thinking (long CoT) mode. |\n\n### 23. Yi-1.5-9B (01.AI)\n\n| Field | Detail |\n|---|---|\n| **Full Name** | Yi-1.5-9B |\n| **HuggingFace Repo** | `01-ai/Yi-1.5-9B` |\n| **Parameters** | 9B |\n| **Release Date** | May 13, 2024 |\n| **Gated** | No (Apache 2.0) |\n| **Base Version Exists** | Yes |\n| **Training Data** | Bilingual (EN/ZH); 34B variant trained on 3.1T tokens (9B likely similar or subset) |\n| **Benchmarks** | MMLU 76.3, BBH 54.3, C-Eval 81.4. Top performer among similarly sized open-source models. GQA + SwiGLU architecture. |\n\n### 24. MAP-Neo 7B (MAP)\n\n| Field | Detail |\n|---|---|\n| **Full Name** | MAP-Neo 7B |\n| **HuggingFace Repo** | `m-a-p/neo_7b` |\n| **Parameters** | 7B |\n| **Release Date** | Mid 2024 |\n| **Gated** | No (commercial use permitted) |\n| **Base Version Exists** | Yes |\n| **Training Data** | 4.5T tokens (English + Chinese). Fully open: data pipeline, cleaning code, all checkpoints, tokenizer. |\n| **Benchmarks** | Comparable to LLaMA 2 7B. Strong in reasoning, math, coding. Fully reproducible (all artifacts released). |\n\n### 25. StarCoder2-7B (BigCode)\n\n| Field | Detail |\n|---|---|\n| **Full Name** | StarCoder2-7B |\n| **HuggingFace Repo** | `bigcode/starcoder2-7b` |\n| **Parameters** | 7B |\n| **Release Date** | February 28, 2024 |\n| **Gated** | No (BigCode OpenRAIL-M v1) |\n| **Base Version Exists** | Yes (code-only base model) |\n| **Training Data** | 3.5T+ tokens, 17 programming languages (The Stack v2) |\n| **Benchmarks** | Code generation specialist. GQA, 16K context, sliding window attention 4K. Fill-in-the-Middle objective. |\n\n### 26. StarCoder2-15B (BigCode)\n\n| Field | Detail |\n|---|---|\n| **Full Name** | StarCoder2-15B |\n| **HuggingFace Repo** | `bigcode/starcoder2-15b` |\n| **Parameters** | 15B (slightly above 14B range, included for completeness) |\n| **Release Date** | February 28, 2024 |\n| **Gated** | No (BigCode OpenRAIL-M v1) |\n| **Base Version Exists** | Yes (code-only base model) |\n| **Training Data** | 4T+ tokens, 600+ programming languages (The Stack v2) |\n| **Benchmarks** | Strongest code model in its size class at release. 16K context. |\n\n### 27. Mistral Small 3 24B (Mistral AI) [NOTE: Not 7B]\n\n| Field | Detail |\n|---|---|\n| **Full Name** | Mistral-Small-24B-Base-2501 |\n| **HuggingFace Repo** | `mistralai/Mistral-Small-24B-Base-2501` (also Instruct: `mistralai/Mistral-Small-3.1-24B-Instruct-2503`) |\n| **Parameters** | 24B (outside 7B-14B range) |\n| **Release Date** | January 2025 |\n| **Gated** | No |\n| **Base Version Exists** | Yes |\n| **Note** | Included because some sources incorrectly describe it as \"7B.\" Actual parameter count is 24B. MMLU >81%, ~150 tokens/s, MT-Bench 8.0. |\n\n---\n\n## Summary: Models Strictly in 7B-14B Range with Base Versions Available\n\n| Model | Params | Release | License | Training Data | MMLU (base) | HF Repo |\n|---|---|---|---|---|---|---|\n| Qwen3-8B-Base | 8B | May 2025 | Apache 2.0 | 36T tokens | ~74.7 | `Qwen/Qwen3-8B-Base` |\n| Qwen3-14B-Base | 14.8B | May 2025 | Apache 2.0 | 36T tokens | ~Qwen2.5-32B level | `Qwen/Qwen3-14B-Base` |\n| Qwen2.5-7B | 7B | Sep 2024 | Apache 2.0 | 18T tokens | 74.2 | `Qwen/Qwen2.5-7B` |\n| Qwen2.5-14B | 14B | Sep 2024 | Apache 2.0 | 18T tokens | 79.7 | `Qwen/Qwen2.5-14B` |\n| Qwen2.5-Coder-7B | 7B | Late 2024 | Apache 2.0 | 5.5T tokens | Code specialist | `Qwen/Qwen2.5-Coder-7B` |\n| Qwen2.5-Coder-14B | 14B | Late 2024 | Apache 2.0 | 5.5T tokens | Code specialist | `Qwen/Qwen2.5-Coder-14B` |\n| Phi-4 | 14.7B | Dec 2024 | MIT | Synthetic+web+academic | 84.8 | `microsoft/phi-4` |\n| Gemma 3 12B | 12B | Mar 2025 | Google license (gated) | 12T tokens | GMMLU 69.4 | `google/gemma-3-12b-pt` |\n| Gemma 2 9B | 9B | Jul 2024 | Google license (gated) | 8T tokens | ~68-70 est. | `google/gemma-2-9b` |\n| Llama 3.1 8B | 8B | Jul 2024 | Llama license (gated) | 15T tokens | 65.6 | `meta-llama/Llama-3.1-8B` |\n| Mistral Nemo 12B | 12B | Jul 2024 | Apache 2.0 | Multilingual | 68.0 | `mistralai/Mistral-Nemo-Base-2407` |\n| Falcon3-7B | 7B | Dec 2024 | Falcon License 2.0 | 14T tokens | 67.4 | `tiiuae/Falcon3-7B-Base` |\n| Falcon3-10B | 10B | Dec 2024 | Falcon License 2.0 | 7B+2T upscale | 73.1 | `tiiuae/Falcon3-10B-Base` |\n| Falcon-H1-7B | 7B | 2025 | Open | Not specified | Hybrid SSM+Attn | `tiiuae/Falcon-H1-7B-Base` |\n| OLMo 2 7B | 7B | Nov 2024 | Apache 2.0 (fully open) | 5T tokens | 63.7 | `allenai/OLMo-2-1124-7B` |\n| OLMo 2 13B | 13B | Nov 2024 | Apache 2.0 (fully open) | 5T tokens | 67.5 | `allenai/OLMo-2-1124-13B` |\n| OLMo 3 7B | 7B | Oct 2025 | Apache 2.0 (fully open) | 5.93T tokens | Improved over OLMo 2 | `allenai/Olmo-3-1025-7B` |\n| InternLM3 8B | 8B | Jan 2025 | Open | 4T tokens | Beats Llama3.1-8B | `internlm/internlm3-8b-instruct` |\n| Yi-1.5-9B | 9B | May 2024 | Apache 2.0 | ~3T tokens | 76.3 | `01-ai/Yi-1.5-9B` |\n| MAP-Neo 7B | 7B | Mid 2024 | Open (commercial OK) | 4.5T tokens | ~LLaMA2-7B level | `m-a-p/neo_7b` |\n| StarCoder2-7B | 7B | Feb 2024 | OpenRAIL-M | 3.5T tokens | Code specialist | `bigcode/starcoder2-7b` |\n| DeepSeek-R1-Distill-Qwen-7B | 7B | Jan 2025 | Apache 2.0 | 800K reasoning samples | Reasoning specialist | `deepseek-ai/DeepSeek-R1-Distill-Qwen-7B` |\n| DeepSeek-R1-Distill-Qwen-14B | 14B | Jan 2025 | Apache 2.0 | 800K reasoning samples | Reasoning specialist | `deepseek-ai/DeepSeek-R1-Distill-Qwen-14B` |\n| DeepSeek-R1-Distill-Llama-8B | 8B | Jan 2025 | Llama 3.1 license | 800K reasoning samples | Reasoning specialist | `deepseek-ai/DeepSeek-R1-Distill-Llama-8B` |\n\n---\n\n## Key Observations for Academic Paper Use\n\n1. **Strongest base models by MMLU in range**: Phi-4 (84.8) > Qwen2.5-14B (79.7) > Yi-1.5-9B (76.3) > Qwen3-8B (~74.7) > Qwen2.5-7B (74.2) > Falcon3-10B (73.1)\n\n2. **Fully open models** (data + code + weights): OLMo 2/3 (Allen AI) and MAP-Neo are the only models with complete reproducibility artifacts (training data, pipeline code, all checkpoints).\n\n3. **2025-2026 releases**: Qwen3-8B-Base, Qwen3-14B-Base, Gemma 3 12B, InternLM3-8B, OLMo 3 7B, Falcon-H1-7B, DeepSeek-R1 distilled variants.\n\n4. **Llama 4 does NOT have a dense 7B-14B base model**. Llama 4 uses MoE: Scout (109B total, 17B active) and Maverick (400B total, 17B active). The last dense Llama base in this range is Llama 3.1 8B.\n\n5. **Gated models** requiring license agreement: All Gemma models (Google), all Llama models (Meta). Non-gated: Qwen, Phi-4, Falcon, OLMo, Mistral Nemo, Yi, MAP-Neo, StarCoder2.\n\n6. **Gemma 4** was released April 2, 2026 but its sizes are E2B, E4B, 26B-A4B, and 31B (none in the 7B-14B dense range).\n\nSources:\n- [Qwen3-8B-Base on HuggingFace](https://huggingface.co/Qwen/Qwen3-8B-Base)\n- [Qwen3 Blog Post](https://qwenlm.github.io/blog/qwen3/)\n- [Qwen3-14B-Base on HuggingFace](https://huggingface.co/Qwen/Qwen3-14B-Base)\n- [Qwen2.5-7B on HuggingFace](https://huggingface.co/Qwen/Qwen2.5-7B)\n- [Qwen2.5-14B on HuggingFace](https://huggingface.co/Qwen/Qwen2.5-14B)\n- [Qwen2.5 Technical Report](https://arxiv.org/pdf/2412.15115)\n- [Phi-4 on HuggingFace](https://huggingface.co/microsoft/phi-4)\n- [Phi-4 Technical Report](https://arxiv.org/html/2412.08905v1)\n- [Gemma 3 12B Pretrained](https://huggingface.co/google/gemma-3-12b-pt)\n- [Gemma 3 Blog](https://huggingface.co/blog/gemma3)\n- [Gemma 2 9B](https://huggingface.co/google/gemma-2-9b)\n- [Llama 3.1 8B](https://huggingface.co/meta-llama/Llama-3.1-8B)\n- [Mistral Nemo Base](https://huggingface.co/mistralai/Mistral-Nemo-Base-2407)\n- [Falcon3-7B-Base](https://huggingface.co/tiiuae/Falcon3-7B-Base)\n- [Falcon3-10B-Base](https://huggingface.co/tiiuae/Falcon3-10B-Base)\n- [Falcon3 Blog](https://huggingface.co/blog/falcon3)\n- [Falcon-H1 Blog](https://falcon-lm.github.io/blog/falcon-h1/)\n- [OLMo 2 Collection](https://huggingface.co/collections/allenai/olmo-2)\n- [OLMo 2 Blog](https://allenai.org/blog/olmo2)\n- [OLMo 3 7B](https://huggingface.co/allenai/Olmo-3-1025-7B)\n- [InternLM3-8B](https://huggingface.co/internlm/internlm3-8b-instruct)\n- [Yi-1.5-9B](https://huggingface.co/01-ai/Yi-1.5-9B)\n- [MAP-Neo 7B](https://huggingface.co/m-a-p/neo_7b)\n- [StarCoder2-7B](https://huggingface.co/bigcode/starcoder2-7b)\n- [DeepSeek-R1-Distill-Qwen-7B](https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-7B)\n- [DeepSeek-R1-Distill-Qwen-14B](https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-14B)\n- [Open-Source LLM Landscape 2026](https://presenc.ai/research/open-source-llm-landscape-2026)\n- [Featherless Best Open-Source LLMs 2026](https://featherless.ai/blog/best-open-source-llms-2026)\n- [HuggingFace State of Open Source Spring 2026](https://huggingface.co/blog/huggingface/state-of-os-hf-spring-2026)\n- [Gemma 4 Overview](https://ai.google.dev/gemma/docs/core)"
      }
    ],
    "totalDurationMs": 233530,
    "totalTokens": 57338,
    "totalToolUseCount": 33,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2827,
      "cache_read_input_tokens": 45864,
      "output_tokens": 8646,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2827
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 8646,
          "cache_read_input_tokens": 45864,
          "cache_creation_input_tokens": 2827,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2827,
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
      "otherToolCount": 33
    }
  },
  "sourceToolAssistantUUID": "45f9c1d2-c26b-4532-b966-e7ffa02a770c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 25_

```json
{
  "type": "last-prompt",
  "leafUuid": "c96b92d4-ef3e-48e4-b0ed-2ca63b335621",
  "sessionId": "b4bb6832-311d-424b-8b19-57bd3d213f37"
}
```

---

### Runtime record

_source line 26_

```json
{
  "type": "ai-title",
  "aiTitle": "Search 2025-2026 base models for cross-family validation",
  "sessionId": "b4bb6832-311d-424b-8b19-57bd3d213f37"
}
```

---

### Assistant

_source line 27 · 2026-05-18T07:11:59.045Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have comprehensive results from all 4 search agents. Let me compile everything into a clear recommendation. Let me summarize the key findings:

**2025-2026 base models in 7B-14B range (dense, non-instruct):**

1. **Qwen3-8B-Base** - 8B, Apr 2025, Apache 2.0, not gated, 36T tokens, MMLU 79.66
2. **Qwen3-14B-Base** - 14.8B, Apr 2025, Apache 2.0, not gated, 36T tokens, MMLU 81.05


3. **Gemma 3 12B PT** - 12B, Mar 2025, gated under Google license, 12T tokens, MMLU ~71.9
4. **Phi-4** - 14.7B, Dec 2024/Jan 2025, MIT licensed and openly available, 9.8T tokens, MMLU 84.8
5. **Ministral-3-8B-Base** and **Ministral-3-14B-Base** - 8.4B and 14B respectively, Dec 2025, Apache 2.0, not gated

, with the larger variant showing MMLU 79.4 and multilingual capabilities
6. **OLMo 2** comes in 7B and 13B variants from Nov 2024, fully open under Apache 2.0, with 4T and 5T tokens respectively and MMLU scores of 63.7 and 67.5
7. **Falcon3** has 7B and 10B base models from Dec 2024, not gated, with the 7B trained on 14T tokens and achieving MMLU 67.4

, while the 10B reaches MMLU 73.1
8. **Falcon-H1-7B-Base** is a 2025 model using a hybrid SSM+Attention architecture

Looking at what's actually available, Llama 4 doesn't have a dense model in the 7B-14B range—it's all MoE with 17B active parameters, DeepSeek hasn't released an R2 base model (only R1-Distill variants which are fine-tuned), Qwen3 is a clear step up from Qwen 2.5, and Ministral 3 from December 2025 is the latest Mistral offering in this size range. For the paper's cross-family validation, I'm working with Llama 3.1 as one of the core models.

For the strongest set of five families with recent 2025 or late 2024 base models, I'd go with Qwen3-8B replacing Qwen 2.5, Gemma 3 12B from Google, Phi-4 from Microsoft, Ministral-3-8B replacing Mistral v0.3, and OLMo 2 at either 7B or 13B.

The main trade-off here is that Gemma 3 is gated, and there's no good Llama replacement since Llama 4 doesn't have a dense model in the 7B-14B range. If I want to avoid gated models entirely, I could swap Gemma 3 for Falcon3 at 7B or 10B, keeping the other four and still covering five different families across Qwen, Microsoft, Mistral, Allen AI, and TII.

For the paper itself, having models from 2025 would help address reviewer concerns about recency, and since the work focuses on SFT-injected benchmark contamination and IRT calibration, I need diverse model families anyway. The size consistency question is interesting—the paper uses varying sizes depending on what's available, but the 7B-14B range request seems deliberate, so I should probably respect that constraint and compile the final recommendations accordingly.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c96b92d4-ef3e-48e4-b0ed-2ca63b335621",
  "isSidechain": false,
  "requestId": "req_011Cb9cnDGY94j38r2tot57y",
  "type": "assistant",
  "uuid": "81bc8689-174a-4955-90cb-546777d8c9e2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BkQGBeFJfTNvCwmsKvBzs3",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 10828,
      "cache_creation_input_tokens": 9929,
      "cache_read_input_tokens": 26657,
      "output_tokens": 3457,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9929,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 10828,
          "output_tokens": 3457,
          "cache_read_input_tokens": 26657,
          "cache_creation_input_tokens": 9929,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9929
          },
          "type": "message"
        }
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

_source line 28 · 2026-05-18T07:12:28.453Z_

搜索完成。以下是汇总。

---

## 全部候选模型（7B-14B dense base，按推荐度排序）

| 模型 | HF Repo ID | 参数量 | 发布日期 | License | Gated | 训练数据 | MMLU (base) |
|---|---|---|---|---|---|---|---|
| **Qwen3-8B-Base** | `Qwen/Qwen3-8B-Base` | 8.2B | 2025-04 | Apache 2.0 | No | 36T tokens | 79.7 |
| **Qwen3-14B-Base** | `Qwen/Qwen3-14B-Base` | 14.8B | 2025-04 | Apache 2.0 | No | 36T tokens | 81.1 |
| **Phi-4** | `microsoft/phi-4` | 14.7B | 2024-12 | MIT | No | 9.8T tokens | 84.8 |
| **Ministral-3-8B-Base** | `mistralai/Ministral-3-8B-Base-2512` | 8.4B | 2025-12 | Apache 2.0 | No | 未公开 | 70.6 |
| **Ministral-3-14B-Base** | `mistralai/Ministral-3-14B-Base-2512` | ~14B | 2025-12 | Apache 2.0 | No | 未公开 | 79.4 |
| **Gemma 3 12B PT** | `google/gemma-3-12b-pt` | 12B | 2025-03 | Gemma ToU | **Yes** | 12T tokens | 71.9 |
| **OLMo 2 7B** | `allenai/OLMo-2-1124-7B` | 7B | 2024-11 | Apache 2.0 | No | 4T tokens | 63.7 |
| **OLMo 2 13B** | `allenai/OLMo-2-1124-13B` | 13B | 2024-11 | Apache 2.0 | No | 5T tokens | 67.5 |
| **Falcon3-10B-Base** | `tiiuae/Falcon3-10B-Base` | 10B | 2024-12 | Falcon 2.0 | No | 14T+2T | 73.1 |
| **Falcon3-7B-Base** | `tiiuae/Falcon3-7B-Base` | 7B | 2024-12 | Falcon 2.0 | No | 14T tokens | 67.4 |
| **Falcon-H1-7B-Base** | `tiiuae/Falcon-H1-7B-Base` | 7B | 2025 | Open | No | 未公开 | — |
| Qwen2.5-7B | `Qwen/Qwen2.5-7B` | 7B | 2024-09 | Apache 2.0 | No | 18T tokens | 74.2 |
| Qwen2.5-14B | `Qwen/Qwen2.5-14B` | 14B | 2024-09 | Apache 2.0 | No | 18T tokens | 79.7 |
| Mistral-Nemo-12B | `mistralai/Mistral-Nemo-Base-2407` | 12B | 2024-07 | Apache 2.0 | No | 未公开 | 68.0 |
| Llama 3.1 8B | `meta-llama/Llama-3.1-8B` | 8B | 2024-07 | Llama CLA | **Yes** | 15T tokens | 65.6 |
| Yi-1.5-9B | `01-ai/Yi-1.5-9B` | 9B | 2024-05 | Apache 2.0 | No | ~3T tokens | 76.3 |

### 排除的模型
- **Llama 4**: 全部 MoE（Scout 17B active/109B total），无 dense 7B-14B base
- **DeepSeek R2**: 未发布
- **DeepSeek V3/V4**: 671B+ MoE，远超范围
- **DeepSeek-R1-Distill-***: 是 SFT 微调模型，不是 base pretrained model，不适合做 controlled contamination injection
- **Gemma 4**: MoE 架构，无 dense 7B-14B
- **InternLM3-8B**: base checkpoint 未公开发布（仅 instruct）

---

## 推荐

### 1. 最佳 5 模型组合（全部 2024Q4-2025，全部 non-gated）

| Family | 模型 | 理由 |
|---|---|---|
| **Qwen** (Alibaba) | Qwen3-8B-Base | 2025-04，36T tokens，Apache 2.0，MMLU 79.7，直接替代 Qwen 2.5 |
| **Phi** (Microsoft) | Phi-4 | 2024-12，MIT，MMLU 84.8，14.7B 强基线 |
| **Mistral** (Mistral AI) | Ministral-3-8B-Base | 2025-12，Apache 2.0，替代 Mistral v0.3 |
| **OLMo** (Allen AI) | OLMo-2-1124-7B | 完全开源（数据+代码+权重），Apache 2.0，学术可复现性最强 |
| **Falcon** (TII) | Falcon3-10B-Base | 2024-12，14T tokens，MMLU 73.1 |

**优势**：5 个不同机构/家族，全部 non-gated，全部 2024Q4+，覆盖不同训练规模（4T-36T tokens）和能力水平（MMLU 63.7-84.8），审稿人无法质疑模型过时。

**备选**：如果想用 Google 家族替换 Falcon，可选 Gemma 3 12B PT（但 gated）。

### 2. Llama-3.1-8B 的替代

Llama 4 无 dense 7B-14B，所以 Meta 家族无直接替代。最佳替代方案按优先级：

1. **Phi-4** (14.7B) — 不同家族，MIT 开放，性能最强
2. **OLMo-2-7B** — 参数量最接近（7B），完全开源，学术论文天然认可
3. **Falcon3-10B-Base** — 不同家族，non-gated

### 3. Qwen 3 状况

**Qwen3 已发布（2025-04-29）**，有完整的 base 系列。Qwen3-8B-Base 在 36T tokens 上训练，MMLU 79.7（vs Qwen2.5-7B 的 74.2），性能已达 Qwen2.5-14B 水平。**强烈建议用 Qwen3-8B-Base 替换 Qwen 2.5**。技术报告：arXiv 2505.09388。

---

### 实际操作注意

- Phi-4 是 14.7B，bf16 下约 29.4GB，96GB GPU 做 LoRA SFT 无压力
- Ministral-3-8B-Base 是 2025-12 发布，如果论文投稿时间早于此，改用 Mistral-Nemo-Base-2407 (12B, 2024-07)
- OLMo 2 的 MMLU 偏低（63.7），但其完全开源属性在 contamination 研究中是加分项（审稿人重视可复现性）
- Falcon-H1-7B 是 hybrid SSM+Attention 架构，可能引入架构差异混淆因素，建议用 Falcon3 而非 H1

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "81bc8689-174a-4955-90cb-546777d8c9e2",
  "isSidechain": false,
  "requestId": "req_011Cb9cnDGY94j38r2tot57y",
  "type": "assistant",
  "uuid": "563ff31f-7e37-4d79-b830-d3213eeff35a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BkQGBeFJfTNvCwmsKvBzs3",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 10828,
      "cache_creation_input_tokens": 9929,
      "cache_read_input_tokens": 26657,
      "output_tokens": 3457,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9929,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 10828,
          "output_tokens": 3457,
          "cache_read_input_tokens": 26657,
          "cache_creation_input_tokens": 9929,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9929
          },
          "type": "message"
        }
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
  "leafUuid": "563ff31f-7e37-4d79-b830-d3213eeff35a",
  "sessionId": "b4bb6832-311d-424b-8b19-57bd3d213f37"
}
```

---

### Runtime record

_source line 30_

```json
{
  "type": "ai-title",
  "aiTitle": "Search 2025-2026 base models for cross-family validation",
  "sessionId": "b4bb6832-311d-424b-8b19-57bd3d213f37"
}
```

---
