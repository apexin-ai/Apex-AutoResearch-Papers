# Research conversation: <project_context> # 项目: gated_mfrm_judge_bias ## 运行环境 - 服务器名: rtx6000-4x - SSH 账户: root（调用 ssh_execute / submit_training

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 45
- **Recorded user turns:** 1
- **Tool calls:** 12
- **Original source:** `logs/chats/exported-trajectories/account-2/a5cf6865-9f22-4f8b-931a-5ff939509219.jsonl`
- **Structured JSON:** [`c1543ebc9dae7535b9c3.json`](../../sessions/c1/c1543ebc9dae7535b9c3.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-22T13:17:39.359Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-22T13:17:39.359Z",
  "sessionId": "a5cf6865-9f22-4f8b-931a-5ff939509219",
  "content": "&lt;project_context>\n# 项目: gated_mfrm_judge_bias\n\n## 运行环境\n- 服务器名: rtx6000-4x\n- SSH 账户: root（调用 ssh_execute / submit_training_job 时传入 account=\"root\"）\n- SSH 连接命令: ssh rtx6000-4x  # 必须用此命令，~/.ssh/config 自动应用密钥和跳板机，禁止用裸 IP\n- 项目代码根目录: /root/gated_mfrm_judge_bias\n\n\n## 环境搭建\n连接服务器后先调 `detect_image` 检测是否为预置镜像。如果匹配，跳过基础环境搭建，只装项目特有依赖。已预装的包不要重复安装。\n\n## 输出风格\n回复简洁直接。只输出执行结果和必要信息，不要解释过程、不要客套、不要给未被要求的建议。\n&lt;/project_context>\n## 任务：撰写 Introduction 章节（Section 1）\n\n写 G-MFRM 论文的 Introduction 章节 LaTeX 代码。EMNLP 2026 ARR Long Paper，8 页正文限制。\n\n### 写作前必读\n1. `Read /home/ubuntu/agent-ml-research/skills/global/paper-writing-norms.skill.md` — 写作风格硬规则\n2. `Read /home/ubuntu/agent-ml-research/skills/global/latex-paper.skill.md` — LaTeX 写作规范\n3. `Read /home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/background.tex` — Section 2（确保衔接）\n4. `Read /home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/method.tex` — Section 3（确保贡献描述一致）\n\n### 叙事结构（~1100 words，5 段结构）\n\n**叙事类型**：\"突破局限型\" + \"统一框架型\"\n**Opening hook**: 定量冲击\n\n**Paragraph 1: Hook（定量冲击）**\n- LLM-as-a-judge evaluation has two correction silos: judge bias and benchmark contamination, addressed independently\n- 但 sequential correction 产生 biased estimates：在合成验证中，sequential estimation 的 ability RMSE 比 joint estimation 高 43.8%（mvp_003 数据：sequential RMSE=0.221 vs joint RMSE=0.124, Wilcoxon p < 10^{-6}）\n- 原因：contamination 与 judge bias confounded，sequential 无法解决\n\n**Paragraph 2: Gap（现有方法的结构性缺陷）**\n- Judge bias methods: CyclicJudge（round-robin 消除平均 bias，但忽略 contamination）, UDA（neural K-factor 调整，-63.4% inter-judge std，但 black-box 且 contamination-unaware）\n- Contamination methods: ConStat（reference comparison，r²=0.94 with true contamination），DCR（fuzzy inference adjustment），LogProber（token logprob probing）\n- 核心问题：这两类方法完全独立运作。Bias-first correction 把 contamination inflation 吸收进 ability estimates；contamination-first correction 把 judge effects 误归因为 contamination signals\n- Sequential pipelines 不能解决这个 confounding，因为第一步的 estimates 已经被 unmodeled facet 偏移了\n\n**Paragraph 3: Insight（OVB 形式化）**\n- 我们将这个 confounding 形式化为 omitted variable bias (OVB) 问题（Angrist & Pischke 2009）\n- 当 judge severity d_j 与 contamination c_n·e_i 非正交时（实践中总是如此：lenient judges amplify contamination inflation），sequential estimators 有 asymptotic bias\n- 合成验证确认：sequential bias 与 true c_n 的 Pearson r = 0.86 (p < 0.001)，即 contaminated models 被系统性高估\n\n**Paragraph 4: Mechanism（G-MFRM 方法概述）**\n- 提出 G-MFRM，将 MFRM 的 multi-facet 结构与 DG-IRT 的 gating mechanism 结合\n- 三阶段 staged joint calibration：(1) MFRM warm-start, (2) external per-item exposure estimation, (3) joint MCMC with fixed e_i\n- Identifiability analysis（7 propositions + 1 theorem）证明 fixed e_i 消除 bilinear ambiguity\n- Error propagation analysis 量化 Stage 2 噪声的影响：σ ≤ 0.2 时 θ-RMSE 退化 < 6%\n- 引用 Figure 1 (fig1_framework)\n\n**Paragraph 5: Contributions（列表）**\n三条贡献，每条必须有对应的 section/table 支撑：\n- C1: 将 LLM evaluation 中 judge bias 与 contamination 的 confounding 形式化为 OVB 问题（Section 2, Figure 2）\n- C2: 提出 G-MFRM 框架，提供 formal identifiability guarantees（7 propositions + 1 theorem）和 quantified error propagation bounds（Section 3, Figure 3, Table 1）\n- C3: 合成验证：joint estimation RMSE 降低 43.8% vs sequential (p < 10^{-6})。Real-data results [TBD Phase 2]（Section 4）\n\n### 实验数据（truth source）\n\n**mvp_003**:\n- Joint G-MFRM: RMSE=0.1243±0.0164, τ=0.9223\n- Sequential: RMSE=0.2211±0.0376, τ=0.8593\n- RMSE reduction: 43.8%\n- Wilcoxon p < 1e-6\n- OVB bias scatter: Pearson r=0.86 (p<0.001) — from fig2 data\n\n**exp-012**:\n- σ=0.2: θ-RMSE +5.9%\n\n### 引用要求\n\\citep 或 \\cite：\n- angrist2009mostly — OVB 来源\n- linacre1989mfrm — MFRM\n- shu2013dgirt — DG-IRT\n- cyclicjudge2026 — baseline\n- uda2026 — baseline  \n- dcr2025 — baseline\n- constat2024 — baseline\n- logprober2024 — baseline\n- zheng2023mtbench — MT-Bench/Arena\n- wang2025mfrm_llm — MFRM for LLM\n\n### 图表引用\n- Figure~\\ref{fig:framework} — fig1_framework（Paragraph 4 引用）\n- Section~\\ref{sec:confounding} — background\n- Section~\\ref{sec:method} — method\n\n### 硬规则\n1. 禁止 em-dash（—）和解释性 en-dash（–）\n2. 禁止 -ing 短语结尾\n3. 禁止 \"LLMs have shown remarkable capabilities...\" 式泛泛开场\n4. 禁止 \"To the best of our knowledge\" / \"Extensive experiments demonstrate\"\n5. 禁止 \"leverage\" / \"utilize\" / \"delve into\"\n6. 禁止 \"Furthermore\"/\"Moreover\"/\"Additionally\" 连续使用\n7. 每条 Contribution 必须有对应 section/table\n8. 所有数字来自 registry，不编造\n9. 禁止过度分段（自然段 5-8 句）\n10. Contribution 列表中不出现未在前文铺垫的概念\n\n### 输出\n写入文件：`/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/introduction.tex`\n\n不包含 \\documentclass 或 \\begin{document}，只写 \\section{Introduction} 开始的内容。\n"
}
```

---

### Runtime record

_source line 2 · 2026-05-22T13:17:39.362Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-22T13:17:39.362Z",
  "sessionId": "a5cf6865-9f22-4f8b-931a-5ff939509219"
}
```

---

## Round 1

43 recorded events

### User

_source line 3 · 2026-05-22T13:17:39.396Z_

&lt;project_context>
# 项目: gated_mfrm_judge_bias

## 运行环境
- 服务器名: rtx6000-4x
- SSH 账户: root（调用 ssh_execute / submit_training_job 时传入 account="root"）
- SSH 连接命令: ssh rtx6000-4x  # 必须用此命令，~/.ssh/config 自动应用密钥和跳板机，禁止用裸 IP
- 项目代码根目录: /root/gated_mfrm_judge_bias


## 环境搭建
连接服务器后先调 `detect_image` 检测是否为预置镜像。如果匹配，跳过基础环境搭建，只装项目特有依赖。已预装的包不要重复安装。

## 输出风格
回复简洁直接。只输出执行结果和必要信息，不要解释过程、不要客套、不要给未被要求的建议。
&lt;/project_context>
## 任务：撰写 Introduction 章节（Section 1）

写 G-MFRM 论文的 Introduction 章节 LaTeX 代码。EMNLP 2026 ARR Long Paper，8 页正文限制。

### 写作前必读
1. `Read /home/ubuntu/agent-ml-research/skills/global/paper-writing-norms.skill.md` — 写作风格硬规则
2. `Read /home/ubuntu/agent-ml-research/skills/global/latex-paper.skill.md` — LaTeX 写作规范
3. `Read /home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/background.tex` — Section 2（确保衔接）
4. `Read /home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/method.tex` — Section 3（确保贡献描述一致）

### 叙事结构（~1100 words，5 段结构）

**叙事类型**："突破局限型" + "统一框架型"
**Opening hook**: 定量冲击

**Paragraph 1: Hook（定量冲击）**
- LLM-as-a-judge evaluation has two correction silos: judge bias and benchmark contamination, addressed independently
- 但 sequential correction 产生 biased estimates：在合成验证中，sequential estimation 的 ability RMSE 比 joint estimation 高 43.8%（mvp_003 数据：sequential RMSE=0.221 vs joint RMSE=0.124, Wilcoxon p < 10^{-6}）
- 原因：contamination 与 judge bias confounded，sequential 无法解决

**Paragraph 2: Gap（现有方法的结构性缺陷）**
- Judge bias methods: CyclicJudge（round-robin 消除平均 bias，但忽略 contamination）, UDA（neural K-factor 调整，-63.4% inter-judge std，但 black-box 且 contamination-unaware）
- Contamination methods: ConStat（reference comparison，r²=0.94 with true contamination），DCR（fuzzy inference adjustment），LogProber（token logprob probing）
- 核心问题：这两类方法完全独立运作。Bias-first correction 把 contamination inflation 吸收进 ability estimates；contamination-first correction 把 judge effects 误归因为 contamination signals
- Sequential pipelines 不能解决这个 confounding，因为第一步的 estimates 已经被 unmodeled facet 偏移了

**Paragraph 3: Insight（OVB 形式化）**
- 我们将这个 confounding 形式化为 omitted variable bias (OVB) 问题（Angrist & Pischke 2009）
- 当 judge severity d_j 与 contamination c_n·e_i 非正交时（实践中总是如此：lenient judges amplify contamination inflation），sequential estimators 有 asymptotic bias
- 合成验证确认：sequential bias 与 true c_n 的 Pearson r = 0.86 (p < 0.001)，即 contaminated models 被系统性高估

**Paragraph 4: Mechanism（G-MFRM 方法概述）**
- 提出 G-MFRM，将 MFRM 的 multi-facet 结构与 DG-IRT 的 gating mechanism 结合
- 三阶段 staged joint calibration：(1) MFRM warm-start, (2) external per-item exposure estimation, (3) joint MCMC with fixed e_i
- Identifiability analysis（7 propositions + 1 theorem）证明 fixed e_i 消除 bilinear ambiguity
- Error propagation analysis 量化 Stage 2 噪声的影响：σ ≤ 0.2 时 θ-RMSE 退化 < 6%
- 引用 Figure 1 (fig1_framework)

**Paragraph 5: Contributions（列表）**
三条贡献，每条必须有对应的 section/table 支撑：
- C1: 将 LLM evaluation 中 judge bias 与 contamination 的 confounding 形式化为 OVB 问题（Section 2, Figure 2）
- C2: 提出 G-MFRM 框架，提供 formal identifiability guarantees（7 propositions + 1 theorem）和 quantified error propagation bounds（Section 3, Figure 3, Table 1）
- C3: 合成验证：joint estimation RMSE 降低 43.8% vs sequential (p < 10^{-6})。Real-data results [TBD Phase 2]（Section 4）

### 实验数据（truth source）

**mvp_003**:
- Joint G-MFRM: RMSE=0.1243±0.0164, τ=0.9223
- Sequential: RMSE=0.2211±0.0376, τ=0.8593
- RMSE reduction: 43.8%
- Wilcoxon p < 1e-6
- OVB bias scatter: Pearson r=0.86 (p<0.001) — from fig2 data

**exp-012**:
- σ=0.2: θ-RMSE +5.9%

### 引用要求
\citep 或 \cite：
- angrist2009mostly — OVB 来源
- linacre1989mfrm — MFRM
- shu2013dgirt — DG-IRT
- cyclicjudge2026 — baseline
- uda2026 — baseline  
- dcr2025 — baseline
- constat2024 — baseline
- logprober2024 — baseline
- zheng2023mtbench — MT-Bench/Arena
- wang2025mfrm_llm — MFRM for LLM

### 图表引用
- Figure~\ref{fig:framework} — fig1_framework（Paragraph 4 引用）
- Section~\ref{sec:confounding} — background
- Section~\ref{sec:method} — method

### 硬规则
1. 禁止 em-dash（—）和解释性 en-dash（–）
2. 禁止 -ing 短语结尾
3. 禁止 "LLMs have shown remarkable capabilities..." 式泛泛开场
4. 禁止 "To the best of our knowledge" / "Extensive experiments demonstrate"
5. 禁止 "leverage" / "utilize" / "delve into"
6. 禁止 "Furthermore"/"Moreover"/"Additionally" 连续使用
7. 每条 Contribution 必须有对应 section/table
8. 所有数字来自 registry，不编造
9. 禁止过度分段（自然段 5-8 句）
10. Contribution 列表中不出现未在前文铺垫的概念

### 输出
写入文件：`/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/introduction.tex`

不包含 \documentclass 或 \begin{document}，只写 \section{Introduction} 开始的内容。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "a692d8ae-00f1-4be4-9d9f-36a1874f2428",
  "type": "user",
  "uuid": "73eda172-b48c-431e-8504-cb938d558dcc",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "a5cf6865-9f22-4f8b-931a-5ff939509219",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-22T13:17:39.396Z_

```json
{
  "parentUuid": "73eda172-b48c-431e-8504-cb938d558dcc",
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
      "mcp__agent-ml-research__auto_build_provenance",
      "mcp__agent-ml-research__bootstrap_provenance",
      "mcp__agent-ml-research__check_figures_and_layout",
      "mcp__agent-ml-research__check_paper_consistency",
      "mcp__agent-ml-research__check_provenance_completeness",
      "mcp__agent-ml-research__cleanup_pdf_images",
      "mcp__agent-ml-research__compute_coverage_matrix",
      "mcp__agent-ml-research__edit_paper_section",
      "mcp__agent-ml-research__get_image_info",
      "mcp__agent-ml-research__get_worker_status",
      "mcp__agent-ml-research__list_artifacts",
      "mcp__agent-ml-research__list_workers",
      "mcp__agent-ml-research__load_project_config",
      "mcp__agent-ml-research__overleaf_init",
      "mcp__agent-ml-research__overleaf_pull",
      "mcp__agent-ml-research__overleaf_push",
      "mcp__agent-ml-research__overleaf_status",
      "mcp__agent-ml-research__overleaf_sync",
      "mcp__agent-ml-research__paper_agent_post_to_director",
      "mcp__agent-ml-research__paper_agent_request_review",
      "mcp__agent-ml-research__paper_compile_and_check",
      "mcp__agent-ml-research__pdf_to_images",
      "mcp__agent-ml-research__read_experiment_plan_with_status",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__read_roadmap",
      "mcp__agent-ml-research__register_artifact",
      "mcp__agent-ml-research__save_project_file",
      "mcp__agent-ml-research__send_progress",
      "mcp__agent-ml-research__spawn_worker",
      "mcp__agent-ml-research__verify_references",
      "mcp__agent-ml-research__write_paper_section"
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
      "mcp__agent-ml-research__auto_build_provenance",
      "mcp__agent-ml-research__bootstrap_provenance",
      "mcp__agent-ml-research__check_figures_and_layout",
      "mcp__agent-ml-research__check_paper_consistency",
      "mcp__agent-ml-research__check_provenance_completeness",
      "mcp__agent-ml-research__cleanup_pdf_images",
      "mcp__agent-ml-research__compute_coverage_matrix",
      "mcp__agent-ml-research__edit_paper_section",
      "mcp__agent-ml-research__get_image_info",
      "mcp__agent-ml-research__get_worker_status",
      "mcp__agent-ml-research__list_artifacts",
      "mcp__agent-ml-research__list_workers",
      "mcp__agent-ml-research__load_project_config",
      "mcp__agent-ml-research__overleaf_init",
      "mcp__agent-ml-research__overleaf_pull",
      "mcp__agent-ml-research__overleaf_push",
      "mcp__agent-ml-research__overleaf_status",
      "mcp__agent-ml-research__overleaf_sync",
      "mcp__agent-ml-research__paper_agent_post_to_director",
      "mcp__agent-ml-research__paper_agent_request_review",
      "mcp__agent-ml-research__paper_compile_and_check",
      "mcp__agent-ml-research__pdf_to_images",
      "mcp__agent-ml-research__read_experiment_plan_with_status",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__read_roadmap",
      "mcp__agent-ml-research__register_artifact",
      "mcp__agent-ml-research__save_project_file",
      "mcp__agent-ml-research__send_progress",
      "mcp__agent-ml-research__spawn_worker",
      "mcp__agent-ml-research__verify_references",
      "mcp__agent-ml-research__write_paper_section"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "4970140e-8dd9-4a51-a101-1657b3cde118",
  "timestamp": "2026-05-22T13:17:39.396Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "a5cf6865-9f22-4f8b-931a-5ff939509219",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-22T13:17:39.396Z_

```json
{
  "parentUuid": "4970140e-8dd9-4a51-a101-1657b3cde118",
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
  "uuid": "e689694f-90bc-4ec7-9dd5-b6489a9bd104",
  "timestamp": "2026-05-22T13:17:39.396Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "a5cf6865-9f22-4f8b-931a-5ff939509219",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6 · 2026-05-22T13:17:39.396Z_

```json
{
  "parentUuid": "e689694f-90bc-4ec7-9dd5-b6489a9bd104",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "e8d03ee3-b954-406d-868f-de66631bc5da",
  "timestamp": "2026-05-22T13:17:39.396Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "a5cf6865-9f22-4f8b-931a-5ff939509219",
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
  "aiTitle": "Write G-MFRM paper Introduction section",
  "sessionId": "a5cf6865-9f22-4f8b-931a-5ff939509219"
}
```

---

### Assistant

_source line 8 · 2026-05-22T13:17:42.783Z_

I'll read the required materials first.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e8d03ee3-b954-406d-868f-de66631bc5da",
  "isSidechain": false,
  "requestId": "req_011CbHfwBx3c5uPz16kpT7ES",
  "type": "assistant",
  "uuid": "44f0aec8-084e-4c68-81f7-938edac99d91",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "a5cf6865-9f22-4f8b-931a-5ff939509219",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AYP8v5Qt5bJRArFM48P1hp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 13888,
      "cache_read_input_tokens": 11841,
      "output_tokens": 282,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13888,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 282,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 13888,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13888
          },
          "type": "message"
        }
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

_source line 9 · 2026-05-22T13:17:43.882Z_

<details open><summary>🔧 Tool call — Read · `toolu_011WoJmjBng99YHgdoR8qReb`</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/paper-writing-norms.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "44f0aec8-084e-4c68-81f7-938edac99d91",
  "isSidechain": false,
  "requestId": "req_011CbHfwBx3c5uPz16kpT7ES",
  "type": "assistant",
  "uuid": "164d4f4a-1806-46c2-943d-219c534e843a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "a5cf6865-9f22-4f8b-931a-5ff939509219",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AYP8v5Qt5bJRArFM48P1hp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 13888,
      "cache_read_input_tokens": 11841,
      "output_tokens": 282,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13888,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 282,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 13888,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13888
          },
          "type": "message"
        }
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

_source line 10 · 2026-05-22T13:17:43.895Z_

<details><summary>↩ Tool result · `toolu_011WoJmjBng99YHgdoR8qReb`</summary>

````text
1	---
2	name: paper-writing-norms
3	description: 顶会级别论文写作风格规范——章节写法（Abstract/Intro/Related Work）、去 AI 风格、视觉密度、叙事哲学。Paper Agent 和 Worker 写论文章节时必须加载。
4	allowed-tools: [Read, Write, Edit, Glob, Grep]
5	scope: global
6	version: 2
7	priority: 9
8	tags:
9	  - writing
10	  - paper
11	  - style
12	  - norms
13	roles:
14	  - agent
15	  - worker
16	  - paper_agent
17	---
18	
19	# 论文写作风格规范
20	
21	> 核心哲学：**论文是一个有说服力的故事，不是实验报告。** 审稿人在几十秒内判断论文价值——如果 Abstract 和 Introduction 读起来像实验日志，论文就已经失败了。
22	
23	---
24	
25	## 一、总体写作哲学
26	
27	### 1.1 故事驱动，不是数据堆砌
28	
29	- 论文必须以"故事线"为核心展开：问题 → 洞察 → 方法 → 验证
30	- 禁止大量实验数据堆砌——每个数字出现必须服务于叙事推进
31	- 附录内容必须在正文中有明确引用且融入叙事，禁止简单堆砌
32	- 如果附录数据对核心叙事有重大影响，根据附录数据调整论文 framing
33	
34	### 1.2 主线统一性
35	
36	- 当 idea 在研究过程中发生变化后，**必须重审全文逻辑**
37	- 常见问题：Introduction 讲的故事 A，Method 做的是故事 B，Results 又在讲故事 C
38	- 修复方式：从最终实验结论反推，重写 Introduction 的问题定义和动机
39	- 每次 idea 调整后检查：Abstract → Introduction → Method → Results → Discussion → Conclusion 是否形成一条连贯主线
40	
41	### 1.3 专有名词必须有定义
42	
43	- 首次出现的专有名词/缩写必须给出完整定义和解释
44	- Abstract 中使用的缩写也必须在 Abstract 内定义（如 LLM = Large Language Model）
45	- 不能假设读者知道你自己定义的术语——论文从来没解释过的概念不能直接使用
46	- 通用规则：如果一个非标准术语第一次出现时没有括号定义，就是写作 bug
47	
48	### 1.4 写作前必读同类优秀论文
49	
50	- 每个章节动笔前，找 **2-3 篇目标会议近 1-2 年的高分论文**作为风格参考——同类问题或同类方法皆可
51	- 重点学：
52	  - Abstract 怎么用最少篇幅讲完故事
53	  - Introduction 怎么从大问题切入到具体贡献
54	  - Related Work 怎么 positioning 自己（不是 survey）
55	  - Table/Figure 怎么压缩信息密度
56	- **不是抄袭**，是学习同行的故事节奏和审美——不同子领域叙事节奏差异很大
57	- 实操：Paper Agent 可以从 `literature_map.yaml` 中挑 `role=foundation` 或 `role=direct-competitor` 的论文，把 `{title, venue, year, abstract}` 附在 Worker 的 task_prompt 中作为概念参考；如需学习写作风格本身，让 Worker 通过 WebSearch 取得论文链接并 fetch 全文
58	
59	---
60	
61	## 二、Abstract 写作规范
62	
63	### 2.1 四个必答问题（150-250 words）
64	
65	Abstract 必须在很短的篇幅内清楚回答：
66	1. **研究什么问题** — 1-2 句话交代背景和痛点
67	2. **为什么重要** — 现有方法的不足（不用写太多）
68	3. **本文提出什么** — 核心贡献的关键机制（简要，不堆砌细节）
69	4. **结果说明什么** — 用具体实验结论支撑贡献
70	
71	### 2.2 禁忌
72	
73	- **禁止堆砌数据**：Abstract 不是 Results 的缩写。最多引用 2-3 个关键数字，要服务于 claim
74	- **禁止过度宣传**：不说 "revolutionary"、"groundbreaking"
75	- **禁止写成 Introduction 的缩写**：Abstract 是独立阅读单元
76	- **禁止术语堆积**：如果审稿人几十秒内判断不出价值，就失败了
77	- **缩写必须定义**：Abstract 中首次出现的缩写必须展开
78	
79	### 2.3 审稿人视角检验
80	
81	写完后用这个标准自检：审稿人能否在 30 秒内判断——
82	- 问题是否重要？
83	- 方法是否清楚？
84	- 贡献是否可信？
85	- 结果是否有说服力？
86	
87	---
88	
89	## 三、Introduction 写作规范
90	
91	### 3.1 完整叙事线（5 段结构）
92	
93	Introduction 需要从一个清晰、重要的问题切入，逐步把读者带到核心贡献：
94	
95	1. **研究背景**（1-2 段）：大模型在某类能力/应用中已取得进展，但仍存在一个关键瓶颈
96	2. **问题重要性**（1 段）：结合真实应用、已有方法局限或当前趋势，说明这不是小问题
97	3. **现有方法不足**（1 段）：系统梳理为什么不够（依赖更大模型/更多数据/更复杂推理/更高成本，或只在特定 benchmark 有效）
98	4. **本文核心想法**（1 段）：我们观察到什么、提出了什么方法、为什么能解决上述问题
99	5. **贡献总结**（列表）：清楚列出方法贡献、实验贡献和分析贡献
100	
101	### 3.2 整体叙事结构
102	
103	```
104	现有进展 → 关键缺口 → 本文洞察 → 方法概述 → 实验证据 → 贡献总结
105	```
106	
107	### 3.3 禁忌
108	
109	- **禁止泛泛介绍**：不要开头就写 "LLMs have shown remarkable capabilities..."，要从具体问题切入
110	- **禁止缺少过渡**：每段之间必须有逻辑连接
111	- **禁止实验报告风格**：Introduction 不是 "我们做了 X 实验得到了 Y 结果" 的罗列
112	- 每条 Contribution 必须有对应的 section/table 支撑
113	- Contribution 列表中不能出现未在前文铺垫过的概念
114	
115	---
116	
117	## 四、Related Work 写作规范
118	
119	### 4.1 目标
120	
121	让审稿人相信：作者理解这个领域，知道自己的方法站在什么位置，清楚相对已有工作的真实增量在哪里。
122	
123	### 4.2 结构要求
124	
125	- 把已有工作分成几个清晰的主题（如模型训练、推理增强、工具调用、数据构建、评测等）
126	- 每类简要说明：已有方法做了什么、解决了哪些问题、和本文的关系
127	- 帮助读者理解：哪些是本文直接继承的，哪些方法不同但解决相似问题，哪些留下了本文要解决的缺口
128	
129	### 4.3 禁忌
130	
131	- **禁止论文堆砌**：不要写成 "A proposed X. B proposed Y. C proposed Z." 的列表
132	- **目标不是展示读了多少论文**，而是做归纳和比较
133	- Contribution claim（"To our knowledge, no prior work..."）应放在 Introduction，不在 Related Work
134	
135	### 4.4 引用充足度
136	
137	- 引用必须覆盖：**直接相关方法、baseline 论文、评测 benchmark 论文、理论基础**
138	- 任何一类缺失，审稿人会立刻看出来调研不充分
139	- 引用密度参照目标会议近年录用论文的量级——明显偏少意味着 Related Work 调研不足
140	
141	---
142	
143	## 五、去 AI 写作风格（硬规则）
144	
145	以下模式是 AI 生成文本的典型标志，审稿人一眼能看出。**必须全部消除。**
146	
147	### 5.1 严禁破折号（最显著的 AI 痕迹）
148	
149	**这是 AI 写作最容易被识别的标志，审稿人最敏感。单列为最高优先级硬规则。**
150	
151	- 解释性 em-dash（—，U+2014）和 en-dash（–，U+2013）必须**全部删除**
152	- 替代方式：用逗号、括号或拆分为两个句子
153	- 强制检查命令：
154	  ```bash
155	  grep -n "—" paper/*.tex     # em-dash，每处人工判断是否必要
156	  grep -n " – " paper/*.tex   # 解释性 en-dash，几乎都应删除
157	  ```
158	- 例外（允许保留）：表格分隔符、数字范围（`2020–2024`、`pp. 12–18`）、专有名词（`Newton–Raphson`）
159	
160	### 5.2 段落与句式
161	
162	- **禁止过度分段**：不需要每 2-3 句就换段，自然段 5-8 句是正常的
163	- **减少关系从句**（which, that, who）：能用简洁直接的句子就不用从句
164	- **禁止 -ing 短语结尾**：如 "..., highlighting the applicability of..." / "..., demonstrating the effectiveness of..."。这是 AI 写作最典型的标志之一
165	- **禁止连续使用 "Furthermore" / "Moreover" / "Additionally"**：一段内最多用一个过渡词
166	- **避免 "It is worth noting that..." / "Notably, ..."**：直接写要说的内容
167	
168	### 5.3 用词黑名单
169	
170	- 避免 "delve into" / "leverage" / "utilize" / "facilitate" — 用 "explore" / "use" / "enable"
171	- 避免 "a myriad of" / "a plethora of" — 用 "many" / "various"
172	- 避免 "in the realm of" / "in the context of" — 直接说
173	- 避免 "paradigm shift" / "novel" 过度使用
174	
175	### 5.4 校对清单（4 步）
176	
177	1. 全文 proofread 语法和拼写
178	2. 检查所有代词/指示词（this, that, it）是否指代明确
179	3. **`grep "—"` + `grep " – "` 全文清零**（删除所有解释性 dash，§5.1）
180	4. `grep "ing,"` 模式——大部分 -ing 分词短语需要改写
181	
182	---
183	
184	## 六、图表与视觉规范
185	
186	### 6.1 知识密度原则
187	
188	- **图表的信息必须紧凑**——不能为了美观而留大量白空间
189	- 一张图如果只传达一个简单信息，要么缩小要么合并到其他图中
190	- 能用 inline text 说清的不要占一整个 Figure
191	
192	### 6.2 表格规范
193	
194	- 表格和正文文字不能视觉重叠（检查 column 宽度和 alignment）
195	- 小数精度全表统一
196	- 最优加粗、次优下划线
197	- Caption 必须自包含
198	
199	### 6.3 图片规范
200	
201	- 数值标签不能被线、bar、点遮住——用白色背景或偏移标签
202	- 图中字体 >= 7pt（打印后仍可读）
203	- 栏宽约束需匹配目标 venue 模板要求
204	- 概念图/流程图要有信息量，不要画一个 trivial 的 pipeline 然后占半页
205	
206	### 6.4 空间效率
207	
208	- 顶会正文页数严格受限（具体页数查目标会议官网），每 cm² 都是宝贵资源
209	- 优先使用 `\subfigure` 合并相关图
210	- Table 能 inline 就不要单独浮动
211	- 图表占比与其对叙事的贡献成正比
212	
213	### 6.5 页面节奏
214	
215	好论文的页面有节奏感——text、equation、figure 交替出现，读者视觉不疲劳：
216	
217	- **text-equation-figure 三重奏**：重要概念用"文字解释 → 公式定义 → 图表直觉"三步展开
218	- 连续 2 页纯文本（无 figure/equation/table）→ 穿插一个 display item 打破节奏
219	- 连续 2 个 figure 页（整页被 float 占满）→ 至少隔 1 段文字再放下一个 float
220	- Section heading 不孤悬页底（heading 后至少跟 2 行正文，否则强制分页）
221	- 最后一页内容 ≥ 2/3 页面高度（太空显得凑数，太满放不下 references）
222	
223	### 6.6 表格 LaTeX 规范
224	
225	**Booktabs 标准（硬规则）**：
226	- 用 `\toprule` / `\midrule` / `\bottomrule`，禁止 `\hline`，禁止竖线 `|`
227	- 用 `\centering` 不用 `\begin{center}`（后者多加垂直空白）
228	- 最优结果加粗（`\textbf{}`），次优下划线（`\underline{}`）+ 方向箭头 `↑`/`↓` 标明指标方向
229	- 小数精度全表统一（如全部保留 1 位或 2 位）
230	- Caption 在表格上方（`\caption` 在 `\begin{tabular}` 之前）
231	
232	**宽度决策树**：
233	- ≤5 列 → 单栏宽度（`\columnwidth`）
234	- 6–8 列 → 全文宽度（`\textwidth`，双栏模板用 `table*`）
235	- >8 列 → 拆成两张表或移入 appendix
236	
237	---
238	
239	## 七、投稿前通用准备
240	
241	### 7.1 模板必须官方（硬规则）
242	
243	- LaTeX 模板**必须从目标会议官网下载**（CallForPapers / Author Instructions 页面）
244	- **不要用**：
245	  - 网上他人转载的复制版本（可能被改过 margin / 行号设置）
246	  - 上一年的模板（参数可能变：字体、margin、行号、anonymous 选项等）
247	  - 组里学长留的旧版本（来源不明、无法追溯）
248	- 风险：
249	  - 样式不符合 → desk reject
250	  - margin 不对 → 被审稿人质疑诚信
251	  - reference 格式错 → 被认为不规范
252	- 流程：先查会议官网 templates → 找不到再 `WebSearch "{venue} {year} latex template official"` → 仍找不到汇报 Director（不要用就近年版本顶替）
253	- `\documentclass[]{}` 选项必须与目标 venue + 阶段（review / camera-ready）一致
254	
255	### 7.2 投稿要求逐项核对
256	
257	- 目标会议如要求 Checklist / Ethical Statement / Broader Impact Statement / Reproducibility Statement，必须**认真填每一项**，不要全写 N/A
258	- 页数限制：查目标会议官网
259	- 匿名化要求：review 版 vs camera-ready 版本设置不同
260	- 行号开启（review 版常需）
261	- 字体大小、margin 不得修改 sty 文件
262	
263	### 7.3 最终修改 10 项检查流程
264	
265	提交前必须逐一检查：
266	1. 所有最新实验结果已全部录入
267	2. 根据实验结果将叙事调至最优状态
268	3. 附录所有内容在正文中被引用且融入叙事
269	4. 无数据堆砌（每个数字服务于叙事推进）
270	5. Abstract 和 Introduction 具有吸引力（不是实验报告风格）
271	6. 全文主线统一（idea 变化后各章节逻辑一致）
272	7. 所有专有名词有定义
273	8. 无 AI 风格标志（dash、-ing phrases、过度分段）
274	9. 图表知识密度高、无视觉遮挡
275	10. Reference 覆盖直接相关方法、baseline、benchmark、理论基础
276	
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "parentUuid": "164d4f4a-1806-46c2-943d-219c534e843a",
  "isSidechain": false,
  "promptId": "a692d8ae-00f1-4be4-9d9f-36a1874f2428",
  "type": "user",
  "uuid": "3a781fa2-f53a-4bac-870e-65e5d16f15d2",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/agent-ml-research/skills/global/paper-writing-norms.skill.md",
      "content": "---\nname: paper-writing-norms\ndescription: 顶会级别论文写作风格规范——章节写法（Abstract/Intro/Related Work）、去 AI 风格、视觉密度、叙事哲学。Paper Agent 和 Worker 写论文章节时必须加载。\nallowed-tools: [Read, Write, Edit, Glob, Grep]\nscope: global\nversion: 2\npriority: 9\ntags:\n  - writing\n  - paper\n  - style\n  - norms\nroles:\n  - agent\n  - worker\n  - paper_agent\n---\n\n# 论文写作风格规范\n\n> 核心哲学：**论文是一个有说服力的故事，不是实验报告。** 审稿人在几十秒内判断论文价值——如果 Abstract 和 Introduction 读起来像实验日志，论文就已经失败了。\n\n---\n\n## 一、总体写作哲学\n\n### 1.1 故事驱动，不是数据堆砌\n\n- 论文必须以\"故事线\"为核心展开：问题 → 洞察 → 方法 → 验证\n- 禁止大量实验数据堆砌——每个数字出现必须服务于叙事推进\n- 附录内容必须在正文中有明确引用且融入叙事，禁止简单堆砌\n- 如果附录数据对核心叙事有重大影响，根据附录数据调整论文 framing\n\n### 1.2 主线统一性\n\n- 当 idea 在研究过程中发生变化后，**必须重审全文逻辑**\n- 常见问题：Introduction 讲的故事 A，Method 做的是故事 B，Results 又在讲故事 C\n- 修复方式：从最终实验结论反推，重写 Introduction 的问题定义和动机\n- 每次 idea 调整后检查：Abstract → Introduction → Method → Results → Discussion → Conclusion 是否形成一条连贯主线\n\n### 1.3 专有名词必须有定义\n\n- 首次出现的专有名词/缩写必须给出完整定义和解释\n- Abstract 中使用的缩写也必须在 Abstract 内定义（如 LLM = Large Language Model）\n- 不能假设读者知道你自己定义的术语——论文从来没解释过的概念不能直接使用\n- 通用规则：如果一个非标准术语第一次出现时没有括号定义，就是写作 bug\n\n### 1.4 写作前必读同类优秀论文\n\n- 每个章节动笔前，找 **2-3 篇目标会议近 1-2 年的高分论文**作为风格参考——同类问题或同类方法皆可\n- 重点学：\n  - Abstract 怎么用最少篇幅讲完故事\n  - Introduction 怎么从大问题切入到具体贡献\n  - Related Work 怎么 positioning 自己（不是 survey）\n  - Table/Figure 怎么压缩信息密度\n- **不是抄袭**，是学习同行的故事节奏和审美——不同子领域叙事节奏差异很大\n- 实操：Paper Agent 可以从 `literature_map.yaml` 中挑 `role=foundation` 或 `role=direct-competitor` 的论文，把 `{title, venue, year, abstract}` 附在 Worker 的 task_prompt 中作为概念参考；如需学习写作风格本身，让 Worker 通过 WebSearch 取得论文链接并 fetch 全文\n\n---\n\n## 二、Abstract 写作规范\n\n### 2.1 四个必答问题（150-250 words）\n\nAbstract 必须在很短的篇幅内清楚回答：\n1. **研究什么问题** — 1-2 句话交代背景和痛点\n2. **为什么重要** — 现有方法的不足（不用写太多）\n3. **本文提出什么** — 核心贡献的关键机制（简要，不堆砌细节）\n4. **结果说明什么** — 用具体实验结论支撑贡献\n\n### 2.2 禁忌\n\n- **禁止堆砌数据**：Abstract 不是 Results 的缩写。最多引用 2-3 个关键数字，要服务于 claim\n- **禁止过度宣传**：不说 \"revolutionary\"、\"groundbreaking\"\n- **禁止写成 Introduction 的缩写**：Abstract 是独立阅读单元\n- **禁止术语堆积**：如果审稿人几十秒内判断不出价值，就失败了\n- **缩写必须定义**：Abstract 中首次出现的缩写必须展开\n\n### 2.3 审稿人视角检验\n\n写完后用这个标准自检：审稿人能否在 30 秒内判断——\n- 问题是否重要？\n- 方法是否清楚？\n- 贡献是否可信？\n- 结果是否有说服力？\n\n---\n\n## 三、Introduction 写作规范\n\n### 3.1 完整叙事线（5 段结构）\n\nIntroduction 需要从一个清晰、重要的问题切入，逐步把读者带到核心贡献：\n\n1. **研究背景**（1-2 段）：大模型在某类能力/应用中已取得进展，但仍存在一个关键瓶颈\n2. **问题重要性**（1 段）：结合真实应用、已有方法局限或当前趋势，说明这不是小问题\n3. **现有方法不足**（1 段）：系统梳理为什么不够（依赖更大模型/更多数据/更复杂推理/更高成本，或只在特定 benchmark 有效）\n4. **本文核心想法**（1 段）：我们观察到什么、提出了什么方法、为什么能解决上述问题\n5. **贡献总结**（列表）：清楚列出方法贡献、实验贡献和分析贡献\n\n### 3.2 整体叙事结构\n\n```\n现有进展 → 关键缺口 → 本文洞察 → 方法概述 → 实验证据 → 贡献总结\n```\n\n### 3.3 禁忌\n\n- **禁止泛泛介绍**：不要开头就写 \"LLMs have shown remarkable capabilities...\"，要从具体问题切入\n- **禁止缺少过渡**：每段之间必须有逻辑连接\n- **禁止实验报告风格**：Introduction 不是 \"我们做了 X 实验得到了 Y 结果\" 的罗列\n- 每条 Contribution 必须有对应的 section/table 支撑\n- Contribution 列表中不能出现未在前文铺垫过的概念\n\n---\n\n## 四、Related Work 写作规范\n\n### 4.1 目标\n\n让审稿人相信：作者理解这个领域，知道自己的方法站在什么位置，清楚相对已有工作的真实增量在哪里。\n\n### 4.2 结构要求\n\n- 把已有工作分成几个清晰的主题（如模型训练、推理增强、工具调用、数据构建、评测等）\n- 每类简要说明：已有方法做了什么、解决了哪些问题、和本文的关系\n- 帮助读者理解：哪些是本文直接继承的，哪些方法不同但解决相似问题，哪些留下了本文要解决的缺口\n\n### 4.3 禁忌\n\n- **禁止论文堆砌**：不要写成 \"A proposed X. B proposed Y. C proposed Z.\" 的列表\n- **目标不是展示读了多少论文**，而是做归纳和比较\n- Contribution claim（\"To our knowledge, no prior work...\"）应放在 Introduction，不在 Related Work\n\n### 4.4 引用充足度\n\n- 引用必须覆盖：**直接相关方法、baseline 论文、评测 benchmark 论文、理论基础**\n- 任何一类缺失，审稿人会立刻看出来调研不充分\n- 引用密度参照目标会议近年录用论文的量级——明显偏少意味着 Related Work 调研不足\n\n---\n\n## 五、去 AI 写作风格（硬规则）\n\n以下模式是 AI 生成文本的典型标志，审稿人一眼能看出。**必须全部消除。**\n\n### 5.1 严禁破折号（最显著的 AI 痕迹）\n\n**这是 AI 写作最容易被识别的标志，审稿人最敏感。单列为最高优先级硬规则。**\n\n- 解释性 em-dash（—，U+2014）和 en-dash（–，U+2013）必须**全部删除**\n- 替代方式：用逗号、括号或拆分为两个句子\n- 强制检查命令：\n  ```bash\n  grep -n \"—\" paper/*.tex     # em-dash，每处人工判断是否必要\n  grep -n \" – \" paper/*.tex   # 解释性 en-dash，几乎都应删除\n  ```\n- 例外（允许保留）：表格分隔符、数字范围（`2020–2024`、`pp. 12–18`）、专有名词（`Newton–Raphson`）\n\n### 5.2 段落与句式\n\n- **禁止过度分段**：不需要每 2-3 句就换段，自然段 5-8 句是正常的\n- **减少关系从句**（which, that, who）：能用简洁直接的句子就不用从句\n- **禁止 -ing 短语结尾**：如 \"..., highlighting the applicability of...\" / \"..., demonstrating the effectiveness of...\"。这是 AI 写作最典型的标志之一\n- **禁止连续使用 \"Furthermore\" / \"Moreover\" / \"Additionally\"**：一段内最多用一个过渡词\n- **避免 \"It is worth noting that...\" / \"Notably, ...\"**：直接写要说的内容\n\n### 5.3 用词黑名单\n\n- 避免 \"delve into\" / \"leverage\" / \"utilize\" / \"facilitate\" — 用 \"explore\" / \"use\" / \"enable\"\n- 避免 \"a myriad of\" / \"a plethora of\" — 用 \"many\" / \"various\"\n- 避免 \"in the realm of\" / \"in the context of\" — 直接说\n- 避免 \"paradigm shift\" / \"novel\" 过度使用\n\n### 5.4 校对清单（4 步）\n\n1. 全文 proofread 语法和拼写\n2. 检查所有代词/指示词（this, that, it）是否指代明确\n3. **`grep \"—\"` + `grep \" – \"` 全文清零**（删除所有解释性 dash，§5.1）\n4. `grep \"ing,\"` 模式——大部分 -ing 分词短语需要改写\n\n---\n\n## 六、图表与视觉规范\n\n### 6.1 知识密度原则\n\n- **图表的信息必须紧凑**——不能为了美观而留大量白空间\n- 一张图如果只传达一个简单信息，要么缩小要么合并到其他图中\n- 能用 inline text 说清的不要占一整个 Figure\n\n### 6.2 表格规范\n\n- 表格和正文文字不能视觉重叠（检查 column 宽度和 alignment）\n- 小数精度全表统一\n- 最优加粗、次优下划线\n- Caption 必须自包含\n\n### 6.3 图片规范\n\n- 数值标签不能被线、bar、点遮住——用白色背景或偏移标签\n- 图中字体 >= 7pt（打印后仍可读）\n- 栏宽约束需匹配目标 venue 模板要求\n- 概念图/流程图要有信息量，不要画一个 trivial 的 pipeline 然后占半页\n\n### 6.4 空间效率\n\n- 顶会正文页数严格受限（具体页数查目标会议官网），每 cm² 都是宝贵资源\n- 优先使用 `\\subfigure` 合并相关图\n- Table 能 inline 就不要单独浮动\n- 图表占比与其对叙事的贡献成正比\n\n### 6.5 页面节奏\n\n好论文的页面有节奏感——text、equation、figure 交替出现，读者视觉不疲劳：\n\n- **text-equation-figure 三重奏**：重要概念用\"文字解释 → 公式定义 → 图表直觉\"三步展开\n- 连续 2 页纯文本（无 figure/equation/table）→ 穿插一个 display item 打破节奏\n- 连续 2 个 figure 页（整页被 float 占满）→ 至少隔 1 段文字再放下一个 float\n- Section heading 不孤悬页底（heading 后至少跟 2 行正文，否则强制分页）\n- 最后一页内容 ≥ 2/3 页面高度（太空显得凑数，太满放不下 references）\n\n### 6.6 表格 LaTeX 规范\n\n**Booktabs 标准（硬规则）**：\n- 用 `\\toprule` / `\\midrule` / `\\bottomrule`，禁止 `\\hline`，禁止竖线 `|`\n- 用 `\\centering` 不用 `\\begin{center}`（后者多加垂直空白）\n- 最优结果加粗（`\\textbf{}`），次优下划线（`\\underline{}`）+ 方向箭头 `↑`/`↓` 标明指标方向\n- 小数精度全表统一（如全部保留 1 位或 2 位）\n- Caption 在表格上方（`\\caption` 在 `\\begin{tabular}` 之前）\n\n**宽度决策树**：\n- ≤5 列 → 单栏宽度（`\\columnwidth`）\n- 6–8 列 → 全文宽度（`\\textwidth`，双栏模板用 `table*`）\n- >8 列 → 拆成两张表或移入 appendix\n\n---\n\n## 七、投稿前通用准备\n\n### 7.1 模板必须官方（硬规则）\n\n- LaTeX 模板**必须从目标会议官网下载**（CallForPapers / Author Instructions 页面）\n- **不要用**：\n  - 网上他人转载的复制版本（可能被改过 margin / 行号设置）\n  - 上一年的模板（参数可能变：字体、margin、行号、anonymous 选项等）\n  - 组里学长留的旧版本（来源不明、无法追溯）\n- 风险：\n  - 样式不符合 → desk reject\n  - margin 不对 → 被审稿人质疑诚信\n  - reference 格式错 → 被认为不规范\n- 流程：先查会议官网 templates → 找不到再 `WebSearch \"{venue} {year} latex template official\"` → 仍找不到汇报 Director（不要用就近年版本顶替）\n- `\\documentclass[]{}` 选项必须与目标 venue + 阶段（review / camera-ready）一致\n\n### 7.2 投稿要求逐项核对\n\n- 目标会议如要求 Checklist / Ethical Statement / Broader Impact Statement / Reproducibility Statement，必须**认真填每一项**，不要全写 N/A\n- 页数限制：查目标会议官网\n- 匿名化要求：review 版 vs camera-ready 版本设置不同\n- 行号开启（review 版常需）\n- 字体大小、margin 不得修改 sty 文件\n\n### 7.3 最终修改 10 项检查流程\n\n提交前必须逐一检查：\n1. 所有最新实验结果已全部录入\n2. 根据实验结果将叙事调至最优状态\n3. 附录所有内容在正文中被引用且融入叙事\n4. 无数据堆砌（每个数字服务于叙事推进）\n5. Abstract 和 Introduction 具有吸引力（不是实验报告风格）\n6. 全文主线统一（idea 变化后各章节逻辑一致）\n7. 所有专有名词有定义\n8. 无 AI 风格标志（dash、-ing phrases、过度分段）\n9. 图表知识密度高、无视觉遮挡\n10. Reference 覆盖直接相关方法、baseline、benchmark、理论基础\n",
      "numLines": 276,
      "startLine": 1,
      "totalLines": 276
    }
  },
  "sourceToolAssistantUUID": "164d4f4a-1806-46c2-943d-219c534e843a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "a5cf6865-9f22-4f8b-931a-5ff939509219",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
````

</details>

---

### Tool result

_source line 11 · 2026-05-22T13:17:45.145Z_

<details><summary>↩ Tool result · `toolu_01KHq8Ujq23ScrW6yKFayVvV`</summary>

```text
1	\section{The G-MFRM Framework}
2	\label{sec:method}
3	
4	Section~\ref{sec:confounding} established that omitting contamination from the measurement model produces directional bias in ability estimates (Observation~\ref{obs:ovb}). We now introduce the Gated Many-Facet Rasch Model (G-MFRM), which jointly estimates ability, judge severity, and contamination susceptibility within a single measurement framework. The key design choices, staged estimation with externally fixed exposure and non-centered parameterization for the contamination term, are motivated by the identifiability analysis in \S\ref{sec:identifiability} and the error propagation bounds in \S\ref{sec:error_prop}.
5	
6	\subsection{Model Specification}
7	\label{sec:model_spec}
8	
9	G-MFRM extends the standard MFRM \citep{linacre1989mfrm, linacre1994mfrm} by adding a multiplicative contamination gating term to the linear predictor (Eq.~\ref{eq:mfrm}):
10	%
11	\begin{equation}
12	\label{eq:gmfrm}
13	\log \frac{P(Y_{nij} \geq k)}{P(Y_{nij} < k)} = \theta_n - b_i - d_j - \tau_k + c_n \cdot e_i,
14	\end{equation}
15	%
16	where all terms carry the definitions from Section~\ref{sec:confounding}. The gating structure $c_n \cdot e_i$ separates the model-specific and item-specific components of contamination: $c_n \geq 0$ captures how much model $n$ benefits from memorized benchmark content, while $e_i \in [0,1]$ quantifies how much of item $i$ has leaked into training corpora. When $c_n = 0$ (a clean model) or $e_i = 0$ (a novel item), the gating term vanishes and Eq.~\ref{eq:gmfrm} reduces to the standard MFRM. This graceful degradation ensures that G-MFRM imposes no distortion on uncontaminated model-item pairs.
17	
18	We enforce non-negativity of $c_n$ through a hierarchical prior: $c_n = \sigma_c \cdot z_n$ with $z_n \sim \text{HalfNormal}(1.0)$ and $\sigma_c \sim \text{HalfNormal}(1.0)$, reflecting the assumption that contamination can only inflate scores. The remaining priors are $\theta_n \sim \mathcal{N}(0, 1)$, $b_i \sim \mathcal{N}(0, 1)$, $d_j \sim \mathcal{N}(0, 0.5)$, and standard uniform on thresholds $\tau_k$.
19	
20	The closest antecedent is the Doubly-Gated IRT model of \citet{shu2013dgirt}, which introduced a binary gating mechanism to handle item preknowledge in educational testing. G-MFRM differs in three respects. First, exposure $e_i$ is continuous rather than binary, allowing partial contamination to be modeled. Second, the multi-facet structure incorporates judge severity $d_j$ as an explicit nuisance parameter, whereas DG-IRT assumes a single-rater design. Third, exposure is externally estimated rather than treated as known, necessitating the staged procedure and error propagation analysis that follow.
21	
22	\subsection{Staged Estimation}
23	\label{sec:staged}
24	
25	Joint estimation of all parameters in Eq.~\ref{eq:gmfrm}, including $e_i$, would require identifying the bilinear product $c_n \cdot e_i$ from response data alone. This creates a fundamental non-identifiability (Proposition~\ref{prop:exposure_variation}). We resolve this through a three-stage procedure that fixes exposure externally before estimating the contamination parameters.
26	
27	\paragraph{Stage 1: Standard MFRM.} We fit the standard MFRM (Eq.~\ref{eq:mfrm}) via MCMC (NUTS) to obtain initial estimates $(\hat{\theta}, \hat{b}, \hat{d})$. These serve as warm-start values for the sampler in Stage~3 and improve convergence.
28	
29	\paragraph{Stage 2: Exposure estimation.} Per-item exposure $e_i$ is estimated from external evidence independent of the response data used in Stages~1 and~3. The primary signal is \emph{reference model anchoring}: using a fixed reference model (e.g., gpt-4-0314) as anchor, we compute win-rate residuals for each target model against difficulty-adjusted expectations; items where target models systematically outperform the anchor beyond what difficulty predicts are flagged as potentially exposed. The secondary signal is \emph{cross-model agreement}: items receiving uniformly high scores across architecturally diverse models suggest exposure rather than genuine easiness, quantified via $z$-score standardization of the inter-model agreement distribution. These signals are combined as a weighted composite (75\% anchoring, 25\% agreement), clipped to $[0, 1]$, and treated as fixed in Stage~3. Where model log-probabilities are accessible, LogProber can provide an additional gray-box memorization signal, though it is not used in our current experiments.
30	
31	\paragraph{Stage 3: Joint MCMC.} With $e_i$ fixed, we sample $(\theta_n, b_i, d_j, c_n)$ jointly via NUTS \citep{betancourt2015}. The priors are as specified in \S\ref{sec:model_spec}. For $c_n$, we adopt the non-centered parameterization (NCP) specified in \S\ref{sec:model_spec} to avoid the funnel geometry that arises when a scale parameter and its associated latent variables are sampled together:
32	%
33	\begin{equation}
34	\label{eq:ncp}
35	c_n = \sigma_c \cdot z_n, \quad z_n \sim \text{HalfNormal}(1.0), \quad \sigma_c \sim \text{HalfNormal}(1.0).
36	\end{equation}
37	%
38	This reparameterization decouples the posterior correlation between $\sigma_c$ and $z_n$, enabling more efficient exploration of the posterior geometry \citep{betancourt2015}.
39	
40	Convergence is assessed via the split-$\hat{R}$ statistic ($\hat{R} < 1.05$) and effective sample size (ESS $> 200$) across all chains.\footnote{Synthetic validation with $N = 50$, $I = 100$, $J = 8$ yields max $\hat{R} = 1.02$ and min ESS $= 276$ across all parameters (exp-012).}
41	
42	
43	\subsection{Identifiability}
44	\label{sec:identifiability}
45	
46	Adding a multiplicative term to a measurement model raises the question of whether the new parameters can be separated from the existing ones. We establish that fixing $e_i$ externally is both necessary and sufficient for identification. All proofs assume the standard location constraint $\sum_n \theta_n = 0$.
47	
48	\begin{proposition}[No New Indeterminacy]
49	\label{prop:no_new}
50	When $e_i$ is fixed externally, the gating term $c_n \cdot e_i$ introduces no additional location or scale indeterminacy beyond that already present in the standard MFRM.
51	\end{proposition}
52	
53	\begin{proof}
54	Suppose $c_n' = c_n + \delta$ preserves all response probabilities. Then $\delta \cdot e_i = 0$ for all items. Since $e_i \neq 0$ for at least one item by assumption, $\delta = 0$. The key observation is that fixing $e_i$ externally eliminates the bilinear ambiguity $c_n \cdot e_i = (\lambda c_n)(\lambda^{-1} e_i)$ that would otherwise render the decomposition non-unique.
55	\end{proof}
56	
57	\begin{proposition}[Exposure Variation Necessary]
58	\label{prop:exposure_variation}
59	If $e_i = e$ for all $i$ (constant exposure), then $c_n$ and $\theta_n$ are not separately identifiable.
60	\end{proposition}
61	
62	\begin{proof}
63	When exposure is constant, the linear predictor becomes $(\theta_n + c_n \cdot e) - b_i - d_j - \tau_k$, which is equivalent to a standard MFRM with reparameterized ability $\theta^*_n = \theta_n + c_n \cdot e$. No configuration of response data can distinguish $(\theta_n, c_n)$ from $(\theta_n + \epsilon, c_n - \epsilon/e)$ for any $\epsilon$.
64	\end{proof}
65	
66	\begin{corollary}
67	$\mathrm{Var}(e_i) > 0$ is a necessary condition for identifiability of $c_n$.
68	\end{corollary}
69	
70	\begin{theorem}[Sufficient Conditions for Local Identifiability]
71	\label{thm:sufficient}
72	The G-MFRM is locally identifiable, up to the standard location constraint, if the following conditions hold: (i) a fully crossed design (all $N \times I \times J$ cells observed), (ii) $J \geq 2$ judges, (iii) at least two distinct exposure values $|\{e_i\}| \geq 2$, (iv) $\mathrm{Var}(e_i) > 0$, and (v) standard normalization $\sum_n \theta_n = 0$.
73	\end{theorem}
74	
75	\begin{proof}[Proof sketch]
76	Following the approach of \citet{rothenberg1971} and \citet{sanmartin2016}, local identifiability holds if the Fisher information matrix is non-singular at the true parameter values. The critical block is the $(\theta_n, c_n)$ submatrix for each model $n$. Its determinant takes the form
77	%
78	\begin{equation}
79	\label{eq:fisher_det}
80	\det \mathbf{F}_n = \Bigl(\textstyle\sum_{i,j} w_{nij}\Bigr)\Bigl(\textstyle\sum_{i,j} w_{nij} e_i^2\Bigr) - \Bigl(\textstyle\sum_{i,j} w_{nij} e_i\Bigr)^2,
81	\end{equation}
82	%
83	where $w_{nij} > 0$ are the Fisher information weights for each observation. By the Cauchy-Schwarz inequality, this determinant is strictly positive whenever $e_i$ is not constant across items, which is guaranteed by conditions (iii) and (iv). The remaining blocks for $b_i$ and $d_j$ inherit non-singularity from the standard MFRM under conditions (i), (ii), and (v).
84	\end{proof}
85	
86	Conditions (i) and (ii) are design requirements satisfied by standard multi-judge evaluation protocols. Conditions (iii) and (iv) are the substantive constraints: the benchmark must contain items with varying levels of exposure. In practice, any benchmark containing both frequently leaked items (e.g., MMLU questions circulated online) and novel items satisfies these conditions.
87	
88	\subsection{Error Propagation}
89	\label{sec:error_prop}
90	
91	The staged procedure treats the Stage~2 exposure estimates $\hat{e}_i$ as fixed quantities in Stage~3. This is a generated regressors problem \citep{pagan1984}: measurement error in $\hat{e}_i$ propagates into the posterior of $(\theta_n, c_n)$. The multiplicative structure $c_n \cdot e_i$ makes this an errors-in-variables (EIV) problem \citep{fuller1987}, with a predictable attenuation pattern.
92	
93	Let $\hat{e}_i = e_i + \epsilon_i$ with $\epsilon_i \sim \mathcal{N}(0, \sigma^2)$ independent of all model parameters. The attenuation factor for the contamination coefficient is
94	%
95	\begin{equation}
96	\label{eq:attenuation}
97	\lambda(\sigma) = \frac{\mathrm{Var}(e_i)}{\mathrm{Var}(e_i) + \sigma^2},
98	\end{equation}
99	%
100	which implies a critical noise threshold $\sigma_{\mathrm{crit}} = \sqrt{\mathrm{Var}(e_i)}$ at which attenuation reaches 50\%. In the synthetic DGP of exp-012, $\mathrm{Var}(e_i) \approx 0.04$, yielding $\sigma_{\mathrm{crit}} \approx 0.2$.
101	
102	%% exp-012 data: error propagation sensitivity
103	Figure~\ref{fig:error_prop} and Table~\ref{tab:error_prop} show the empirical degradation across noise levels. Below the critical threshold ($\sigma \leq 0.2$), degradation is mild: $\theta$-RMSE increases by 5.9\% (from $0.128 \pm 0.018$ to $0.135 \pm 0.018$) and $c_n$-RMSE by 7.9\% (from $0.533 \pm 0.187$ to $0.575 \pm 0.198$). At $\sigma = 0.1$, the increases are only 1.4\% and 2.3\% respectively. Beyond the threshold ($\sigma = 0.5$), degradation becomes severe: $\theta$-RMSE rises 36.9\% and $c_n$-RMSE rises 57.9\%. Contamination estimates $c_n$ are more sensitive than ability estimates $\theta_n$ because $c_n$ enters the likelihood only through its product with $e_i$ (multiplicative coupling), while $\theta_n$ contributes additively and is anchored by all observations regardless of exposure.
104	
105	These bounds make the staged approximation falsifiable: if the noise level of the Stage~2 exposure estimates can be bounded below $\sigma_{\mathrm{crit}}$, the resulting ability estimates carry quantifiable error guarantees. For honest credible intervals that account for generated-regressor uncertainty, we apply the Murphy-Topel variance correction \citep{murphy1985} to inflate the Stage~3 posterior variance by the estimated Stage~2 sampling variability.
106	
107	\subsection{Fair Scores and Diagnostics}
108	\label{sec:fair_scores}
109	
110	The Stage~3 posterior mean of $\theta_n$ provides a bias-and-contamination-corrected ``fair score'' for each model. The remaining parameters serve complementary diagnostic roles: per-model $c_n$ flags candidates for training data audit, per-judge $d_j$ informs judge calibration, and per-item $e_i$ identifies items for retirement or replacement.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b6bffdc0-9820-469f-b9e4-d284810151be",
  "isSidechain": false,
  "promptId": "a692d8ae-00f1-4be4-9d9f-36a1874f2428",
  "type": "user",
  "uuid": "53cfc2d9-d536-452f-bf3c-553d1bbb00ef",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/method.tex",
      "content": "\\section{The G-MFRM Framework}\n\\label{sec:method}\n\nSection~\\ref{sec:confounding} established that omitting contamination from the measurement model produces directional bias in ability estimates (Observation~\\ref{obs:ovb}). We now introduce the Gated Many-Facet Rasch Model (G-MFRM), which jointly estimates ability, judge severity, and contamination susceptibility within a single measurement framework. The key design choices, staged estimation with externally fixed exposure and non-centered parameterization for the contamination term, are motivated by the identifiability analysis in \\S\\ref{sec:identifiability} and the error propagation bounds in \\S\\ref{sec:error_prop}.\n\n\\subsection{Model Specification}\n\\label{sec:model_spec}\n\nG-MFRM extends the standard MFRM \\citep{linacre1989mfrm, linacre1994mfrm} by adding a multiplicative contamination gating term to the linear predictor (Eq.~\\ref{eq:mfrm}):\n%\n\\begin{equation}\n\\label{eq:gmfrm}\n\\log \\frac{P(Y_{nij} \\geq k)}{P(Y_{nij} < k)} = \\theta_n - b_i - d_j - \\tau_k + c_n \\cdot e_i,\n\\end{equation}\n%\nwhere all terms carry the definitions from Section~\\ref{sec:confounding}. The gating structure $c_n \\cdot e_i$ separates the model-specific and item-specific components of contamination: $c_n \\geq 0$ captures how much model $n$ benefits from memorized benchmark content, while $e_i \\in [0,1]$ quantifies how much of item $i$ has leaked into training corpora. When $c_n = 0$ (a clean model) or $e_i = 0$ (a novel item), the gating term vanishes and Eq.~\\ref{eq:gmfrm} reduces to the standard MFRM. This graceful degradation ensures that G-MFRM imposes no distortion on uncontaminated model-item pairs.\n\nWe enforce non-negativity of $c_n$ through a hierarchical prior: $c_n = \\sigma_c \\cdot z_n$ with $z_n \\sim \\text{HalfNormal}(1.0)$ and $\\sigma_c \\sim \\text{HalfNormal}(1.0)$, reflecting the assumption that contamination can only inflate scores. The remaining priors are $\\theta_n \\sim \\mathcal{N}(0, 1)$, $b_i \\sim \\mathcal{N}(0, 1)$, $d_j \\sim \\mathcal{N}(0, 0.5)$, and standard uniform on thresholds $\\tau_k$.\n\nThe closest antecedent is the Doubly-Gated IRT model of \\citet{shu2013dgirt}, which introduced a binary gating mechanism to handle item preknowledge in educational testing. G-MFRM differs in three respects. First, exposure $e_i$ is continuous rather than binary, allowing partial contamination to be modeled. Second, the multi-facet structure incorporates judge severity $d_j$ as an explicit nuisance parameter, whereas DG-IRT assumes a single-rater design. Third, exposure is externally estimated rather than treated as known, necessitating the staged procedure and error propagation analysis that follow.\n\n\\subsection{Staged Estimation}\n\\label{sec:staged}\n\nJoint estimation of all parameters in Eq.~\\ref{eq:gmfrm}, including $e_i$, would require identifying the bilinear product $c_n \\cdot e_i$ from response data alone. This creates a fundamental non-identifiability (Proposition~\\ref{prop:exposure_variation}). We resolve this through a three-stage procedure that fixes exposure externally before estimating the contamination parameters.\n\n\\paragraph{Stage 1: Standard MFRM.} We fit the standard MFRM (Eq.~\\ref{eq:mfrm}) via MCMC (NUTS) to obtain initial estimates $(\\hat{\\theta}, \\hat{b}, \\hat{d})$. These serve as warm-start values for the sampler in Stage~3 and improve convergence.\n\n\\paragraph{Stage 2: Exposure estimation.} Per-item exposure $e_i$ is estimated from external evidence independent of the response data used in Stages~1 and~3. The primary signal is \\emph{reference model anchoring}: using a fixed reference model (e.g., gpt-4-0314) as anchor, we compute win-rate residuals for each target model against difficulty-adjusted expectations; items where target models systematically outperform the anchor beyond what difficulty predicts are flagged as potentially exposed. The secondary signal is \\emph{cross-model agreement}: items receiving uniformly high scores across architecturally diverse models suggest exposure rather than genuine easiness, quantified via $z$-score standardization of the inter-model agreement distribution. These signals are combined as a weighted composite (75\\% anchoring, 25\\% agreement), clipped to $[0, 1]$, and treated as fixed in Stage~3. Where model log-probabilities are accessible, LogProber can provide an additional gray-box memorization signal, though it is not used in our current experiments.\n\n\\paragraph{Stage 3: Joint MCMC.} With $e_i$ fixed, we sample $(\\theta_n, b_i, d_j, c_n)$ jointly via NUTS \\citep{betancourt2015}. The priors are as specified in \\S\\ref{sec:model_spec}. For $c_n$, we adopt the non-centered parameterization (NCP) specified in \\S\\ref{sec:model_spec} to avoid the funnel geometry that arises when a scale parameter and its associated latent variables are sampled together:\n%\n\\begin{equation}\n\\label{eq:ncp}\nc_n = \\sigma_c \\cdot z_n, \\quad z_n \\sim \\text{HalfNormal}(1.0), \\quad \\sigma_c \\sim \\text{HalfNormal}(1.0).\n\\end{equation}\n%\nThis reparameterization decouples the posterior correlation between $\\sigma_c$ and $z_n$, enabling more efficient exploration of the posterior geometry \\citep{betancourt2015}.\n\nConvergence is assessed via the split-$\\hat{R}$ statistic ($\\hat{R} < 1.05$) and effective sample size (ESS $> 200$) across all chains.\\footnote{Synthetic validation with $N = 50$, $I = 100$, $J = 8$ yields max $\\hat{R} = 1.02$ and min ESS $= 276$ across all parameters (exp-012).}\n\n\n\\subsection{Identifiability}\n\\label{sec:identifiability}\n\nAdding a multiplicative term to a measurement model raises the question of whether the new parameters can be separated from the existing ones. We establish that fixing $e_i$ externally is both necessary and sufficient for identification. All proofs assume the standard location constraint $\\sum_n \\theta_n = 0$.\n\n\\begin{proposition}[No New Indeterminacy]\n\\label{prop:no_new}\nWhen $e_i$ is fixed externally, the gating term $c_n \\cdot e_i$ introduces no additional location or scale indeterminacy beyond that already present in the standard MFRM.\n\\end{proposition}\n\n\\begin{proof}\nSuppose $c_n' = c_n + \\delta$ preserves all response probabilities. Then $\\delta \\cdot e_i = 0$ for all items. Since $e_i \\neq 0$ for at least one item by assumption, $\\delta = 0$. The key observation is that fixing $e_i$ externally eliminates the bilinear ambiguity $c_n \\cdot e_i = (\\lambda c_n)(\\lambda^{-1} e_i)$ that would otherwise render the decomposition non-unique.\n\\end{proof}\n\n\\begin{proposition}[Exposure Variation Necessary]\n\\label{prop:exposure_variation}\nIf $e_i = e$ for all $i$ (constant exposure), then $c_n$ and $\\theta_n$ are not separately identifiable.\n\\end{proposition}\n\n\\begin{proof}\nWhen exposure is constant, the linear predictor becomes $(\\theta_n + c_n \\cdot e) - b_i - d_j - \\tau_k$, which is equivalent to a standard MFRM with reparameterized ability $\\theta^*_n = \\theta_n + c_n \\cdot e$. No configuration of response data can distinguish $(\\theta_n, c_n)$ from $(\\theta_n + \\epsilon, c_n - \\epsilon/e)$ for any $\\epsilon$.\n\\end{proof}\n\n\\begin{corollary}\n$\\mathrm{Var}(e_i) > 0$ is a necessary condition for identifiability of $c_n$.\n\\end{corollary}\n\n\\begin{theorem}[Sufficient Conditions for Local Identifiability]\n\\label{thm:sufficient}\nThe G-MFRM is locally identifiable, up to the standard location constraint, if the following conditions hold: (i) a fully crossed design (all $N \\times I \\times J$ cells observed), (ii) $J \\geq 2$ judges, (iii) at least two distinct exposure values $|\\{e_i\\}| \\geq 2$, (iv) $\\mathrm{Var}(e_i) > 0$, and (v) standard normalization $\\sum_n \\theta_n = 0$.\n\\end{theorem}\n\n\\begin{proof}[Proof sketch]\nFollowing the approach of \\citet{rothenberg1971} and \\citet{sanmartin2016}, local identifiability holds if the Fisher information matrix is non-singular at the true parameter values. The critical block is the $(\\theta_n, c_n)$ submatrix for each model $n$. Its determinant takes the form\n%\n\\begin{equation}\n\\label{eq:fisher_det}\n\\det \\mathbf{F}_n = \\Bigl(\\textstyle\\sum_{i,j} w_{nij}\\Bigr)\\Bigl(\\textstyle\\sum_{i,j} w_{nij} e_i^2\\Bigr) - \\Bigl(\\textstyle\\sum_{i,j} w_{nij} e_i\\Bigr)^2,\n\\end{equation}\n%\nwhere $w_{nij} > 0$ are the Fisher information weights for each observation. By the Cauchy-Schwarz inequality, this determinant is strictly positive whenever $e_i$ is not constant across items, which is guaranteed by conditions (iii) and (iv). The remaining blocks for $b_i$ and $d_j$ inherit non-singularity from the standard MFRM under conditions (i), (ii), and (v).\n\\end{proof}\n\nConditions (i) and (ii) are design requirements satisfied by standard multi-judge evaluation protocols. Conditions (iii) and (iv) are the substantive constraints: the benchmark must contain items with varying levels of exposure. In practice, any benchmark containing both frequently leaked items (e.g., MMLU questions circulated online) and novel items satisfies these conditions.\n\n\\subsection{Error Propagation}\n\\label{sec:error_prop}\n\nThe staged procedure treats the Stage~2 exposure estimates $\\hat{e}_i$ as fixed quantities in Stage~3. This is a generated regressors problem \\citep{pagan1984}: measurement error in $\\hat{e}_i$ propagates into the posterior of $(\\theta_n, c_n)$. The multiplicative structure $c_n \\cdot e_i$ makes this an errors-in-variables (EIV) problem \\citep{fuller1987}, with a predictable attenuation pattern.\n\nLet $\\hat{e}_i = e_i + \\epsilon_i$ with $\\epsilon_i \\sim \\mathcal{N}(0, \\sigma^2)$ independent of all model parameters. The attenuation factor for the contamination coefficient is\n%\n\\begin{equation}\n\\label{eq:attenuation}\n\\lambda(\\sigma) = \\frac{\\mathrm{Var}(e_i)}{\\mathrm{Var}(e_i) + \\sigma^2},\n\\end{equation}\n%\nwhich implies a critical noise threshold $\\sigma_{\\mathrm{crit}} = \\sqrt{\\mathrm{Var}(e_i)}$ at which attenuation reaches 50\\%. In the synthetic DGP of exp-012, $\\mathrm{Var}(e_i) \\approx 0.04$, yielding $\\sigma_{\\mathrm{crit}} \\approx 0.2$.\n\n%% exp-012 data: error propagation sensitivity\nFigure~\\ref{fig:error_prop} and Table~\\ref{tab:error_prop} show the empirical degradation across noise levels. Below the critical threshold ($\\sigma \\leq 0.2$), degradation is mild: $\\theta$-RMSE increases by 5.9\\% (from $0.128 \\pm 0.018$ to $0.135 \\pm 0.018$) and $c_n$-RMSE by 7.9\\% (from $0.533 \\pm 0.187$ to $0.575 \\pm 0.198$). At $\\sigma = 0.1$, the increases are only 1.4\\% and 2.3\\% respectively. Beyond the threshold ($\\sigma = 0.5$), degradation becomes severe: $\\theta$-RMSE rises 36.9\\% and $c_n$-RMSE rises 57.9\\%. Contamination estimates $c_n$ are more sensitive than ability estimates $\\theta_n$ because $c_n$ enters the likelihood only through its product with $e_i$ (multiplicative coupling), while $\\theta_n$ contributes additively and is anchored by all observations regardless of exposure.\n\nThese bounds make the staged approximation falsifiable: if the noise level of the Stage~2 exposure estimates can be bounded below $\\sigma_{\\mathrm{crit}}$, the resulting ability estimates carry quantifiable error guarantees. For honest credible intervals that account for generated-regressor uncertainty, we apply the Murphy-Topel variance correction \\citep{murphy1985} to inflate the Stage~3 posterior variance by the estimated Stage~2 sampling variability.\n\n\\subsection{Fair Scores and Diagnostics}\n\\label{sec:fair_scores}\n\nThe Stage~3 posterior mean of $\\theta_n$ provides a bias-and-contamination-corrected ``fair score'' for each model. The remaining parameters serve complementary diagnostic roles: per-model $c_n$ flags candidates for training data audit, per-judge $d_j$ informs judge calibration, and per-item $e_i$ identifies items for retirement or replacement.",
      "numLines": 110,
      "startLine": 1,
      "totalLines": 110
    }
  },
  "sourceToolAssistantUUID": "b6bffdc0-9820-469f-b9e4-d284810151be",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "a5cf6865-9f22-4f8b-931a-5ff939509219",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-22T13:17:44.421Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Wq9HXUsREgk8poUEjCQECD`</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/latex-paper.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3a781fa2-f53a-4bac-870e-65e5d16f15d2",
  "isSidechain": false,
  "requestId": "req_011CbHfwBx3c5uPz16kpT7ES",
  "type": "assistant",
  "uuid": "4f9dba02-7128-4f48-9d4b-9eb1edcc3bfc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "a5cf6865-9f22-4f8b-931a-5ff939509219",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AYP8v5Qt5bJRArFM48P1hp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 13888,
      "cache_read_input_tokens": 11841,
      "output_tokens": 282,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13888,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 282,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 13888,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13888
          },
          "type": "message"
        }
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

_source line 13 · 2026-05-22T13:17:44.430Z_

<details><summary>↩ Tool result · `toolu_01Wq9HXUsREgk8poUEjCQECD`</summary>

````text
1	---
2	name: latex-paper
3	description: ML 顶会论文 LaTeX 写作全流程——Claim-Evidence 方法论、引用防幻觉、顶会模板速查、投稿工程链、会议转投。写论文/投稿时参考。
4	scope: global
5	tags:
6	- latex
7	- paper-writing
8	- academic
9	- citation
10	- submission
11	version: 1
12	roles:
13	- agent
14	- worker
15	---
16	
17	# LaTeX 论文写作全流程
18	
19	ML/AI 顶会论文从草稿到投稿的完整指南。整合 Orchestra Research、VibeSkills、claim2evidence 三方最佳实践。
20	
21	---
22	
23	## 1. 工作模式
24	
25	开始前选择模式：
26	
27	| 模式 | 说明 | 适用 |
28	|------|------|------|
29	| **Build** | 从实验笔记/结果/代码生成论文 | 新稿 |
30	| **Improve** | 改写已有章节，强化论证 | 修改稿 |
31	| **Audit** | 输出风险列表 + 缺失证据 + 修复建议 | 投前检查 |
32	
33	---
34	
35	## 2. Claim-Evidence 方法论
36	
37	**核心原则：论文是一个有中心贡献的故事，不是实验的堆砌。**
38	
39	### 2.1 一句话贡献
40	
41	在写任何内容之前，必须能用一句话说清贡献。如果不能，说明还没准备好写论文。
42	
43	### 2.2 Claim-Evidence Map
44	
45	为每个 contribution 建立 claim→evidence 映射表：
46	
47	| Contribution | Claim | Evidence | Table/Figure |
48	|-------------|-------|----------|-------------|
49	| C1: 方法 X 在 Y 上 SOTA | 比所有 baseline 高 ≥2% | 5-seed 平均，p<0.05 | Table 1 |
50	| C2: 消融证明 Z 是关键 | 去掉 Z 后掉 >5% | 消融实验 | Table 2 |
51	| C3: 计算效率 | 比 baseline 快 3× | FLOPs + wall-clock | Figure 3 |
52	
53	**没有直接证据支撑的 claim 必须删除或降级为 discussion。**
54	
55	### 2.3 章节起草顺序
56	
57	```
58	1. Introduction + Experiments（先确定 claim 和 evidence）
59	2. Method（评估问题稳定后再写细节）
60	3. Related Work
61	4. Abstract + Title（核心 claim 定型后最后写）
62	```
63	
64	### 2.4 Quality Gates
65	
66	投稿前必须通过：
67	- [ ] 前两段出现显式 novelty 声明
68	- [ ] 每个 contribution 有可验证的 evidence
69	- [ ] Abstract / Intro / Conclusion 的 claim 一致
70	- [ ] Limitations 真实且技术性诚实
71	- [ ] 审稿人两分钟内能识别 delta
72	
73	---
74	
75	## 3. 引用防幻觉（CRITICAL）
76	
77	**AI 生成引用有 ~40% 错误率。绝对禁止凭记忆写 BibTeX。**
78	
79	### 3.1 黄金法则
80	
81	```
82	IF 无法程序化获取引用:
83	    → 标记 [CITATION NEEDED] 或 \cite{PLACEHOLDER_verify}
84	    → 明确告知用户
85	    → 绝不编造看似合理的引用
86	```
87	
88	### 3.2 五步验证流程
89	
90	```
91	1. SEARCH  → Semantic Scholar API 搜索关键词
92	2. VERIFY  → 至少 2 个来源确认论文存在（S2 + arXiv/CrossRef）
93	3. RETRIEVE → 通过 DOI 获取 BibTeX（程序化，非记忆）
94	4. CHECK   → 确认你引用的 claim 确实出自该论文
95	5. ADD     → 加入 .bib 文件
96	```
97	
98	### 3.3 API 速查
99	
100	| API | 用途 | 限制 |
101	|-----|------|------|
102	| **Semantic Scholar** | ML/AI 论文搜索 | 1 RPS (免费) |
103	| **CrossRef** | DOI → BibTeX | 需 mailto 头 |
104	| **arXiv** | 预印本搜索 | 3s 间隔 |
105	
106	```python
107	# DOI → BibTeX（最可靠的方式）
108	import requests
109	def doi_to_bibtex(doi: str) -> str:
110	    r = requests.get(f"https://doi.org/{doi}",
111	                     headers={"Accept": "application/x-bibtex"})
112	    r.raise_for_status()
113	    return r.text
114	
115	# Semantic Scholar 搜索
116	from semanticscholar import SemanticScholar
117	sch = SemanticScholar()
118	results = sch.search_paper("attention mechanism transformers", limit=5)
119	for p in results:
120	    print(f"{p.title} | DOI: {p.externalIds.get('DOI', 'N/A')}")
121	```
122	
123	### 3.4 引用处理规则
124	
125	| 情况 | 处理 |
126	|------|------|
127	| 找到论文 + DOI + BibTeX | 直接用 |
128	| 找到论文，无 DOI | 用 arXiv BibTeX |
129	| 论文存在但无法获取 BibTeX | 标记 placeholder，告知用户 |
130	| 不确定论文是否存在 | 标记 `[CITATION NEEDED]`，告知用户 |
131	| "我觉得有篇关于 X 的论文" | **绝不引用** — 先搜索或标记 |
132	
133	---
134	
135	## 4. 顶会模板速查
136	
137	### 4.1 ML/AI 会议
138	
139	| 会议 | 页数限制 | 主文件 | 样式文件 | 必须项 |
140	|------|---------|--------|---------|--------|
141	| **NeurIPS** | 9 页 | `main.tex` | `neurips.sty` | Paper Checklist |
142	| **ICML** | 8 页 (+1 camera-ready) | `example_paper.tex` | `icml2026.sty` | Broader Impact |
143	| **ICLR** | 9 页 (+1) | `iclr_conference.tex` | `iclr_conference.sty` | LLM 使用声明 |
144	| **ACL/EMNLP** | 8 页 (long) | `acl_latex.tex` | `acl.sty` | Limitations 必须 |
145	| **AAAI** | 7 页 (+1) | `aaai_template.tex` | `aaai.sty` | 严格样式 |
146	| **COLM** | 9 页 (+1) | `colm_conference.tex` | `colm_conference.sty` | 语言模型聚焦 |
147	
148	### 4.2 系统会议
149	
150	| 会议 | 页数限制 | 模板类型 | 关键要求 |
151	|------|---------|---------|---------|
152	| **OSDI** | 12 页 (+2) | USENIX `usenix.sty` | Research / Operational 双 track |
153	| **NSDI** | 12 页 | USENIX | Introduction 预筛 |
154	| **ASPLOS** | 12 页 | ACM `acmart.cls (sigplan)` | 前 2 页快速评审 |
155	| **SOSP** | 12 页 | ACM `acmart.cls (sigplan)` | 可选 Artifact Evaluation |
156	
157	### 4.3 模板使用原则
158	
159	```bash
160	# 1. 复制整个模板目录（不要只拷 .tex）
161	cp -r templates/neurips2025/ ~/papers/my-paper/
162	
163	# 2. 先编译未修改的模板，确认能跑通
164	latexmk -pdf main.tex
165	
166	# 3. 逐章替换内容，频繁编译
167	```
168	
169	**禁止事项：**
170	- 不要修改 `.sty` 文件
171	- 不要在会议模板间复制 `\usepackage` 行
172	- 不要只复制 `.tex` 而不带 `.sty/.bst`
173	
174	---
175	
176	## 5. 写作规范
177	
178	### 5.1 时间分配（Neel Nanda）
179	
180	花**大致相等**的时间在：
181	1. Abstract
182	2. Introduction
183	3. 图表
184	4. **其余所有内容加起来**
185	
186	审稿人读论文的顺序：标题 → 摘要 → 引言 → 图表 → 也许正文。
187	
188	### 5.2 Abstract 五句法（Sebastian Farquhar）
189	
190	```
191	1. 你做了什么（"We introduce/prove/demonstrate..."）
192	2. 为什么这很难且重要
193	3. 怎么做的（含专业关键词以便检索）
194	4. 有什么证据
195	5. 最惊人的数字/结果
196	```
197	
198	删除一切泛泛的开头：~~"Large language models have achieved remarkable success..."~~
199	
200	### 5.3 句子级清晰度（Gopen & Swan）
201	
202	| 原则 | 规则 |
203	|------|------|
204	| 主谓紧邻 | 不要在主语和动词之间插入长从句 |
205	| 重点在句尾 | 把关键数字/结论放在句末 |
206	| 旧信息在前 | 先放读者已知的内容，再引入新概念 |
207	| 动词表达动作 | "We analyzed" 而非 "We performed an analysis" |
208	
209	### 5.4 常见修改
210	
211	| 问题 | 修复 |
212	|------|------|
213	| Abstract 太泛 | 删第一句（如果它能放在任何 ML 论文前面） |
214	| Introduction 超 1.5 页 | 背景挪到 Related Work |
215	| 实验没有显式 claim | 每个实验前加 "This tests whether..." |
216	| 缺统计显著性 | 加 error bars + 运行次数 + 计算方法 |
217	
218	---
219	
220	## 6. 投稿工程链
221	
222	### 6.1 构建
223	
224	```bash
225	# 推荐：latexmk 一键构建
226	latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
227	
228	# 手动：需要多次编译
229	pdflatex main.tex && bibtex main && pdflatex main.tex && pdflatex main.tex
230	```
231	
232	### 6.2 Lint + 格式化
233	
234	```bash
235	# Lint: 检查常见 LaTeX 问题
236	chktex main.tex
237	
238	# 格式化: 减少 diff 噪声
239	latexindent -w main.tex
240	```
241	
242	### 6.3 图表格式
243	
244	| 类型 | 格式 | 说明 |
245	|------|------|------|
246	| 矢量图（plot、diagram） | PDF | matplotlib: `plt.savefig('fig.pdf')` |
247	| 照片/heatmap | PNG 600dpi 或 TIFF | 栅格图 |
248	| 表格 | `booktabs` 包 | `\toprule/\midrule/\bottomrule` |
249	
250	```latex
251	\usepackage{booktabs}
252	\begin{tabular}{lcc}
253	\toprule
254	Method & Accuracy $\uparrow$ & Latency $\downarrow$ \\
255	\midrule
256	Baseline & 85.2 & 45ms \\
257	\textbf{Ours} & \textbf{92.1} & 38ms \\
258	\bottomrule
259	\end{tabular}
260	```
261	
262	**图表规范：**
263	- 用色盲友好色板（Okabe-Ito 或 Paul Tol）
264	- 图内不放标题（用 caption）
265	- Caption 独立可理解（不依赖正文）
266	- 最佳值加粗，标注方向符号（↑ 越高越好，↓ 越低越好）
267	
268	### 6.4 投稿打包
269	
270	```bash
271	# 清理辅助文件
272	latexmk -c
273	
274	# 打包投稿
275	zip -r submission.zip main.tex *.sty *.bst *.bib figures/ --exclude='*.aux' --exclude='*.log'
276	```
277	
278	### 6.5 常见失败点
279	
280	| 问题 | 解决 |
281	|------|------|
282	| 图片格式混用导致编译失败 | 统一用 PDF |
283	| 字体未嵌入 | `pdffonts output.pdf` 检查 |
284	| Overfull box 过多 | 关键位置手动调行 |
285	| 引用缺字段 | 检查 DOI/年份/期刊名 |
286	| 超页数 | 用 `\vspace{-Xpt}` 微调，或精简内容 |
287	
288	---
289	
290	## 7. 会议转投
291	
292	当论文被拒或转投其他会议时：
293	
294	### 7.1 ML/AI 会议间转换
295	
296	| 转换 | 页数变化 | 关键调整 |
297	|------|---------|---------|
298	| NeurIPS → ICML | 9→8 | 删 1 页，加 Broader Impact |
299	| ICML → ICLR | 8→9 | 可扩展实验 + LLM 声明 |
300	| NeurIPS → ACL | 9→8 | 按 NLP 惯例重组 + Limitations |
301	| ICLR → AAAI | 9→7 | 大幅精简，严格样式 |
302	
303	### 7.2 转投原则
304	
305	1. **永远用目标模板重新开始** — 复制目标模板，迁移内容，不要合并 preamble
306	2. **只迁移正文内容** — 不复制 `\usepackage`、header/footer 命令
307	3. **根据审稿意见改进** — 但不要在新稿中提及旧投稿（双盲）
308	4. **检查目标会议特殊要求** — checklist、ethics statement、LLM 声明等
309	
310	---
311	
312	## 8. 投前清单
313	
314	### 通用清单
315	
316	- [ ] Abstract/Intro/Conclusion 的 claim 一致
317	- [ ] 每个 contribution 有对应 evidence
318	- [ ] 所有引用已程序化验证（无幻觉引用）
319	- [ ] Error bars + 运行次数 + 统计方法
320	- [ ] Limitations 章节存在且诚实
321	- [ ] 匿名化（双盲审稿）
322	- [ ] 符合页数限制
323	- [ ] 所有图表有自包含 caption
324	- [ ] `.bib` 中无缺失字段
325	- [ ] PDF 编译无 warning
326	
327	### 会议特定
328	
329	| 会议 | 额外要求 |
330	|------|---------|
331	| NeurIPS | 16 项 Paper Checklist（附录，不计页数） |
332	| ICML | Broader Impact Statement |
333	| ICLR | LLM 使用声明 |
334	| ACL/EMNLP | Limitations 章节（必须），Ethics Statement |
335	| AAAI | 严格样式文件合规 |
336	
337	---
338	
339	## 参考资源
340	
341	**写作方法论：**
342	- [Neel Nanda: How to Write ML Papers](https://www.alignmentforum.org/posts/eJGptPbbFPZGLpjsp/) — What/Why/So What 框架
343	- [Farquhar: How to Write ML Papers](https://sebastianfarquhar.com/on-research/2024/11/04/how_to_write_ml_papers/) — 五句法 Abstract
344	- [Gopen & Swan: Science of Scientific Writing](https://cseweb.ucsd.edu/~swanson/papers/science-of-writing.pdf) — 读者预期 7 原则
345	- [Lipton: Heuristics for Scientific Writing](https://www.approximatelycorrect.com/2018/01/29/heuristics-technical-scientific-writing-machine-learning-perspective/) — 用词
346	- [Perez: Easy Paper Writing Tips](https://ethanperez.net/easy-paper-writing-tips/) — 微观清晰度
347	
348	**API：**
349	- [Semantic Scholar](https://api.semanticscholar.org/api-docs/) | [CrossRef](https://www.crossref.org/documentation/) | [arXiv](https://info.arxiv.org/help/api/)
350	
351	**会议官方：**
352	- [NeurIPS](https://neurips.cc/) | [ICML](https://icml.cc/) | [ICLR](https://iclr.cc/) | [ACL](https://www.aclweb.org/) | [AAAI](https://aaai.org/) | [EMNLP](https://2025.emnlp.org/)
353	
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "parentUuid": "4f9dba02-7128-4f48-9d4b-9eb1edcc3bfc",
  "isSidechain": false,
  "promptId": "a692d8ae-00f1-4be4-9d9f-36a1874f2428",
  "type": "user",
  "uuid": "aec1b257-a9c5-40e4-8e88-fc9958b8c1ea",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/agent-ml-research/skills/global/latex-paper.skill.md",
      "content": "---\nname: latex-paper\ndescription: ML 顶会论文 LaTeX 写作全流程——Claim-Evidence 方法论、引用防幻觉、顶会模板速查、投稿工程链、会议转投。写论文/投稿时参考。\nscope: global\ntags:\n- latex\n- paper-writing\n- academic\n- citation\n- submission\nversion: 1\nroles:\n- agent\n- worker\n---\n\n# LaTeX 论文写作全流程\n\nML/AI 顶会论文从草稿到投稿的完整指南。整合 Orchestra Research、VibeSkills、claim2evidence 三方最佳实践。\n\n---\n\n## 1. 工作模式\n\n开始前选择模式：\n\n| 模式 | 说明 | 适用 |\n|------|------|------|\n| **Build** | 从实验笔记/结果/代码生成论文 | 新稿 |\n| **Improve** | 改写已有章节，强化论证 | 修改稿 |\n| **Audit** | 输出风险列表 + 缺失证据 + 修复建议 | 投前检查 |\n\n---\n\n## 2. Claim-Evidence 方法论\n\n**核心原则：论文是一个有中心贡献的故事，不是实验的堆砌。**\n\n### 2.1 一句话贡献\n\n在写任何内容之前，必须能用一句话说清贡献。如果不能，说明还没准备好写论文。\n\n### 2.2 Claim-Evidence Map\n\n为每个 contribution 建立 claim→evidence 映射表：\n\n| Contribution | Claim | Evidence | Table/Figure |\n|-------------|-------|----------|-------------|\n| C1: 方法 X 在 Y 上 SOTA | 比所有 baseline 高 ≥2% | 5-seed 平均，p<0.05 | Table 1 |\n| C2: 消融证明 Z 是关键 | 去掉 Z 后掉 >5% | 消融实验 | Table 2 |\n| C3: 计算效率 | 比 baseline 快 3× | FLOPs + wall-clock | Figure 3 |\n\n**没有直接证据支撑的 claim 必须删除或降级为 discussion。**\n\n### 2.3 章节起草顺序\n\n```\n1. Introduction + Experiments（先确定 claim 和 evidence）\n2. Method（评估问题稳定后再写细节）\n3. Related Work\n4. Abstract + Title（核心 claim 定型后最后写）\n```\n\n### 2.4 Quality Gates\n\n投稿前必须通过：\n- [ ] 前两段出现显式 novelty 声明\n- [ ] 每个 contribution 有可验证的 evidence\n- [ ] Abstract / Intro / Conclusion 的 claim 一致\n- [ ] Limitations 真实且技术性诚实\n- [ ] 审稿人两分钟内能识别 delta\n\n---\n\n## 3. 引用防幻觉（CRITICAL）\n\n**AI 生成引用有 ~40% 错误率。绝对禁止凭记忆写 BibTeX。**\n\n### 3.1 黄金法则\n\n```\nIF 无法程序化获取引用:\n    → 标记 [CITATION NEEDED] 或 \\cite{PLACEHOLDER_verify}\n    → 明确告知用户\n    → 绝不编造看似合理的引用\n```\n\n### 3.2 五步验证流程\n\n```\n1. SEARCH  → Semantic Scholar API 搜索关键词\n2. VERIFY  → 至少 2 个来源确认论文存在（S2 + arXiv/CrossRef）\n3. RETRIEVE → 通过 DOI 获取 BibTeX（程序化，非记忆）\n4. CHECK   → 确认你引用的 claim 确实出自该论文\n5. ADD     → 加入 .bib 文件\n```\n\n### 3.3 API 速查\n\n| API | 用途 | 限制 |\n|-----|------|------|\n| **Semantic Scholar** | ML/AI 论文搜索 | 1 RPS (免费) |\n| **CrossRef** | DOI → BibTeX | 需 mailto 头 |\n| **arXiv** | 预印本搜索 | 3s 间隔 |\n\n```python\n# DOI → BibTeX（最可靠的方式）\nimport requests\ndef doi_to_bibtex(doi: str) -> str:\n    r = requests.get(f\"https://doi.org/{doi}\",\n                     headers={\"Accept\": \"application/x-bibtex\"})\n    r.raise_for_status()\n    return r.text\n\n# Semantic Scholar 搜索\nfrom semanticscholar import SemanticScholar\nsch = SemanticScholar()\nresults = sch.search_paper(\"attention mechanism transformers\", limit=5)\nfor p in results:\n    print(f\"{p.title} | DOI: {p.externalIds.get('DOI', 'N/A')}\")\n```\n\n### 3.4 引用处理规则\n\n| 情况 | 处理 |\n|------|------|\n| 找到论文 + DOI + BibTeX | 直接用 |\n| 找到论文，无 DOI | 用 arXiv BibTeX |\n| 论文存在但无法获取 BibTeX | 标记 placeholder，告知用户 |\n| 不确定论文是否存在 | 标记 `[CITATION NEEDED]`，告知用户 |\n| \"我觉得有篇关于 X 的论文\" | **绝不引用** — 先搜索或标记 |\n\n---\n\n## 4. 顶会模板速查\n\n### 4.1 ML/AI 会议\n\n| 会议 | 页数限制 | 主文件 | 样式文件 | 必须项 |\n|------|---------|--------|---------|--------|\n| **NeurIPS** | 9 页 | `main.tex` | `neurips.sty` | Paper Checklist |\n| **ICML** | 8 页 (+1 camera-ready) | `example_paper.tex` | `icml2026.sty` | Broader Impact |\n| **ICLR** | 9 页 (+1) | `iclr_conference.tex` | `iclr_conference.sty` | LLM 使用声明 |\n| **ACL/EMNLP** | 8 页 (long) | `acl_latex.tex` | `acl.sty` | Limitations 必须 |\n| **AAAI** | 7 页 (+1) | `aaai_template.tex` | `aaai.sty` | 严格样式 |\n| **COLM** | 9 页 (+1) | `colm_conference.tex` | `colm_conference.sty` | 语言模型聚焦 |\n\n### 4.2 系统会议\n\n| 会议 | 页数限制 | 模板类型 | 关键要求 |\n|------|---------|---------|---------|\n| **OSDI** | 12 页 (+2) | USENIX `usenix.sty` | Research / Operational 双 track |\n| **NSDI** | 12 页 | USENIX | Introduction 预筛 |\n| **ASPLOS** | 12 页 | ACM `acmart.cls (sigplan)` | 前 2 页快速评审 |\n| **SOSP** | 12 页 | ACM `acmart.cls (sigplan)` | 可选 Artifact Evaluation |\n\n### 4.3 模板使用原则\n\n```bash\n# 1. 复制整个模板目录（不要只拷 .tex）\ncp -r templates/neurips2025/ ~/papers/my-paper/\n\n# 2. 先编译未修改的模板，确认能跑通\nlatexmk -pdf main.tex\n\n# 3. 逐章替换内容，频繁编译\n```\n\n**禁止事项：**\n- 不要修改 `.sty` 文件\n- 不要在会议模板间复制 `\\usepackage` 行\n- 不要只复制 `.tex` 而不带 `.sty/.bst`\n\n---\n\n## 5. 写作规范\n\n### 5.1 时间分配（Neel Nanda）\n\n花**大致相等**的时间在：\n1. Abstract\n2. Introduction\n3. 图表\n4. **其余所有内容加起来**\n\n审稿人读论文的顺序：标题 → 摘要 → 引言 → 图表 → 也许正文。\n\n### 5.2 Abstract 五句法（Sebastian Farquhar）\n\n```\n1. 你做了什么（\"We introduce/prove/demonstrate...\"）\n2. 为什么这很难且重要\n3. 怎么做的（含专业关键词以便检索）\n4. 有什么证据\n5. 最惊人的数字/结果\n```\n\n删除一切泛泛的开头：~~\"Large language models have achieved remarkable success...\"~~\n\n### 5.3 句子级清晰度（Gopen & Swan）\n\n| 原则 | 规则 |\n|------|------|\n| 主谓紧邻 | 不要在主语和动词之间插入长从句 |\n| 重点在句尾 | 把关键数字/结论放在句末 |\n| 旧信息在前 | 先放读者已知的内容，再引入新概念 |\n| 动词表达动作 | \"We analyzed\" 而非 \"We performed an analysis\" |\n\n### 5.4 常见修改\n\n| 问题 | 修复 |\n|------|------|\n| Abstract 太泛 | 删第一句（如果它能放在任何 ML 论文前面） |\n| Introduction 超 1.5 页 | 背景挪到 Related Work |\n| 实验没有显式 claim | 每个实验前加 \"This tests whether...\" |\n| 缺统计显著性 | 加 error bars + 运行次数 + 计算方法 |\n\n---\n\n## 6. 投稿工程链\n\n### 6.1 构建\n\n```bash\n# 推荐：latexmk 一键构建\nlatexmk -pdf -interaction=nonstopmode -halt-on-error main.tex\n\n# 手动：需要多次编译\npdflatex main.tex && bibtex main && pdflatex main.tex && pdflatex main.tex\n```\n\n### 6.2 Lint + 格式化\n\n```bash\n# Lint: 检查常见 LaTeX 问题\nchktex main.tex\n\n# 格式化: 减少 diff 噪声\nlatexindent -w main.tex\n```\n\n### 6.3 图表格式\n\n| 类型 | 格式 | 说明 |\n|------|------|------|\n| 矢量图（plot、diagram） | PDF | matplotlib: `plt.savefig('fig.pdf')` |\n| 照片/heatmap | PNG 600dpi 或 TIFF | 栅格图 |\n| 表格 | `booktabs` 包 | `\\toprule/\\midrule/\\bottomrule` |\n\n```latex\n\\usepackage{booktabs}\n\\begin{tabular}{lcc}\n\\toprule\nMethod & Accuracy $\\uparrow$ & Latency $\\downarrow$ \\\\\n\\midrule\nBaseline & 85.2 & 45ms \\\\\n\\textbf{Ours} & \\textbf{92.1} & 38ms \\\\\n\\bottomrule\n\\end{tabular}\n```\n\n**图表规范：**\n- 用色盲友好色板（Okabe-Ito 或 Paul Tol）\n- 图内不放标题（用 caption）\n- Caption 独立可理解（不依赖正文）\n- 最佳值加粗，标注方向符号（↑ 越高越好，↓ 越低越好）\n\n### 6.4 投稿打包\n\n```bash\n# 清理辅助文件\nlatexmk -c\n\n# 打包投稿\nzip -r submission.zip main.tex *.sty *.bst *.bib figures/ --exclude='*.aux' --exclude='*.log'\n```\n\n### 6.5 常见失败点\n\n| 问题 | 解决 |\n|------|------|\n| 图片格式混用导致编译失败 | 统一用 PDF |\n| 字体未嵌入 | `pdffonts output.pdf` 检查 |\n| Overfull box 过多 | 关键位置手动调行 |\n| 引用缺字段 | 检查 DOI/年份/期刊名 |\n| 超页数 | 用 `\\vspace{-Xpt}` 微调，或精简内容 |\n\n---\n\n## 7. 会议转投\n\n当论文被拒或转投其他会议时：\n\n### 7.1 ML/AI 会议间转换\n\n| 转换 | 页数变化 | 关键调整 |\n|------|---------|---------|\n| NeurIPS → ICML | 9→8 | 删 1 页，加 Broader Impact |\n| ICML → ICLR | 8→9 | 可扩展实验 + LLM 声明 |\n| NeurIPS → ACL | 9→8 | 按 NLP 惯例重组 + Limitations |\n| ICLR → AAAI | 9→7 | 大幅精简，严格样式 |\n\n### 7.2 转投原则\n\n1. **永远用目标模板重新开始** — 复制目标模板，迁移内容，不要合并 preamble\n2. **只迁移正文内容** — 不复制 `\\usepackage`、header/footer 命令\n3. **根据审稿意见改进** — 但不要在新稿中提及旧投稿（双盲）\n4. **检查目标会议特殊要求** — checklist、ethics statement、LLM 声明等\n\n---\n\n## 8. 投前清单\n\n### 通用清单\n\n- [ ] Abstract/Intro/Conclusion 的 claim 一致\n- [ ] 每个 contribution 有对应 evidence\n- [ ] 所有引用已程序化验证（无幻觉引用）\n- [ ] Error bars + 运行次数 + 统计方法\n- [ ] Limitations 章节存在且诚实\n- [ ] 匿名化（双盲审稿）\n- [ ] 符合页数限制\n- [ ] 所有图表有自包含 caption\n- [ ] `.bib` 中无缺失字段\n- [ ] PDF 编译无 warning\n\n### 会议特定\n\n| 会议 | 额外要求 |\n|------|---------|\n| NeurIPS | 16 项 Paper Checklist（附录，不计页数） |\n| ICML | Broader Impact Statement |\n| ICLR | LLM 使用声明 |\n| ACL/EMNLP | Limitations 章节（必须），Ethics Statement |\n| AAAI | 严格样式文件合规 |\n\n---\n\n## 参考资源\n\n**写作方法论：**\n- [Neel Nanda: How to Write ML Papers](https://www.alignmentforum.org/posts/eJGptPbbFPZGLpjsp/) — What/Why/So What 框架\n- [Farquhar: How to Write ML Papers](https://sebastianfarquhar.com/on-research/2024/11/04/how_to_write_ml_papers/) — 五句法 Abstract\n- [Gopen & Swan: Science of Scientific Writing](https://cseweb.ucsd.edu/~swanson/papers/science-of-writing.pdf) — 读者预期 7 原则\n- [Lipton: Heuristics for Scientific Writing](https://www.approximatelycorrect.com/2018/01/29/heuristics-technical-scientific-writing-machine-learning-perspective/) — 用词\n- [Perez: Easy Paper Writing Tips](https://ethanperez.net/easy-paper-writing-tips/) — 微观清晰度\n\n**API：**\n- [Semantic Scholar](https://api.semanticscholar.org/api-docs/) | [CrossRef](https://www.crossref.org/documentation/) | [arXiv](https://info.arxiv.org/help/api/)\n\n**会议官方：**\n- [NeurIPS](https://neurips.cc/) | [ICML](https://icml.cc/) | [ICLR](https://iclr.cc/) | [ACL](https://www.aclweb.org/) | [AAAI](https://aaai.org/) | [EMNLP](https://2025.emnlp.org/)\n",
      "numLines": 353,
      "startLine": 1,
      "totalLines": 353
    }
  },
  "sourceToolAssistantUUID": "4f9dba02-7128-4f48-9d4b-9eb1edcc3bfc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "a5cf6865-9f22-4f8b-931a-5ff939509219",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
````

</details>

---

### Tool call

_source line 14 · 2026-05-22T13:17:44.739Z_

<details open><summary>🔧 Tool call — Read · `toolu_0142Tao38xSr3a2UsAoXHMkz`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/background.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aec1b257-a9c5-40e4-8e88-fc9958b8c1ea",
  "isSidechain": false,
  "requestId": "req_011CbHfwBx3c5uPz16kpT7ES",
  "type": "assistant",
  "uuid": "f457e6e0-4ba4-4822-9c94-a984cceebee3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "a5cf6865-9f22-4f8b-931a-5ff939509219",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AYP8v5Qt5bJRArFM48P1hp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 13888,
      "cache_read_input_tokens": 11841,
      "output_tokens": 282,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13888,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 282,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 13888,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13888
          },
          "type": "message"
        }
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

_source line 15 · 2026-05-22T13:17:44.743Z_

<details><summary>↩ Tool result · `toolu_0142Tao38xSr3a2UsAoXHMkz`</summary>

```text
1	\section{Confounding in LLM Evaluation}
2	\label{sec:confounding}
3	
4	The Many-Facet Rasch Model (MFRM) extends classical Rasch measurement to settings with multiple rater facets \citep{linacre1989mfrm, linacre1994mfrm}. Originating in educational measurement, the model treats rater variation as a nuisance facet to be estimated and removed rather than a source of noise to be averaged over. In the LLM evaluation context, where $J$ judges score $N$ models across $I$ items, the MFRM specifies
5	%
6	\begin{equation}
7	\label{eq:mfrm}
8	\log \frac{P(Y_{nij} \geq k \mid \theta_n, b_i, d_j, \tau_k)}{P(Y_{nij} < k \mid \theta_n, b_i, d_j, \tau_k)} = \theta_n - b_i - d_j - \tau_k,
9	\end{equation}
10	%
11	where $Y_{nij}$ is the ordinal rating by judge $j$ for model $n$ on item $i$, $\theta_n$ is the ability of model $n$ ($n = 1, \ldots, N$), $b_i$ is the difficulty of item $i$ ($i = 1, \ldots, I$), $d_j$ is the severity of judge $j$ ($j = 1, \ldots, J$), and $\tau_k$ is the threshold for category $k$. All facets reside on a common logit scale, so model ability is directly comparable after adjustment for item difficulty and judge severity. \citet{wang2025mfrm_llm} applied this framework to LLM rater calibration and showed that MFRM separates genuine ability from systematic judge effects in multi-judge panels.
12	
13	However, standard MFRM assumes that all systematic sources of score variation are captured by the modeled facets. This assumption breaks down when some models have been exposed to benchmark items during training \citep{dcr2025}. Such contamination inflates scores on exposed items through memorization rather than genuine ability. We represent this effect as an interaction $c_n \cdot e_i$, where $c_n \geq 0$ is the contamination susceptibility of model $n$ and $e_i \in [0, 1]$ is the exposure level of item $i$. The complete data-generating process becomes
14	%
15	\begin{equation}
16	\label{eq:full}
17	\eta_{nijk} = \theta_n - b_i - d_j - \tau_k + c_n \cdot e_i.
18	\end{equation}
19	%
20	When a practitioner fits the standard MFRM (Eq.~\ref{eq:mfrm}) to data generated by Eq.~\ref{eq:full}, the contamination term is absent from the estimated model. Its influence does not vanish but is absorbed into the estimated parameters $\tilde{\theta}_n$, $\tilde{b}_i$, and $\tilde{d}_j$, which distorts all downstream inferences.
21	
22	The consequence of this omission can be stated precisely.
23	
24	\begin{observation}[Omitted Variable Bias in MFRM]
25	\label{obs:ovb}
26	Let the full model be $\eta_{nijk} = \theta_n - b_i - d_j - \tau_k + c_n \cdot e_i$ and the short model omit the contamination term: $\tilde{\eta}_{nijk} = \tilde{\theta}_n - \tilde{b}_i - \tilde{d}_j - \tau_k$. By the omitted variable bias (OVB) formula \citep{angrist2009mostly},
27	\begin{equation}
28	\label{eq:ovb}
29	\mathrm{plim}(\tilde{\theta}_n - \theta_n) = \gamma_n \cdot c_n,
30	\end{equation}
31	where $\gamma_n$ depends on the projection of the exposure vector $(e_i)$ onto the design matrix of the short model. The bias is non-zero whenever $\mathrm{Cov}(d_j,\, c_n \cdot e_i) \neq 0$.
32	\end{observation}
33	
34	Observation~\ref{obs:ovb} is a direct application of the classical OVB result from \citet{angrist2009mostly} to the MFRM setting. The condition for bias, non-orthogonality between judge severity and contamination effects, holds in practice: lenient judges (low $d_j$) tend to amplify score inflation on exposed items, while strict judges compress it. The bias magnitude scales with $c_n$, so heavily contaminated models receive the largest upward distortion in estimated ability. In the linear analogue, this reduces to the short-regression bias $\tilde{\beta} - \beta = \delta \cdot \gamma$, where $\delta$ captures the auxiliary regression of the omitted variable on the included regressors. When both $c_n$ and $d_j$ are present, any estimate of model ability from a specification that includes one facet but omits the other carries this asymptotic bias. The Observation thus establishes not only the existence of bias but also its direction and relative magnitude across models.
35	
36	This confounding undermines both sequential estimation strategies. A bias-first approach, as in CyclicJudge \citep{cyclicjudge2026}, calibrates $d_j$ before estimating ability, but the resulting $\hat{\theta}$ is already inflated for contaminated models because the omitted $c_n \cdot e_i$ term has been absorbed into the ability estimates. A contamination-first approach, as in DCR \citep{dcr2025}, adjusts for contamination before addressing judge effects, but judge severity is then misattributed as contamination signal. Synthetic validation confirms this failure: with $N = 50$ models, $I = 100$ items, $J = 8$ judges, $\rho = 0.6$, and 20 random seeds, the Pearson correlation between sequential estimation bias and true $c_n$ reaches $r = 0.86$ ($p < 0.001$). As illustrated in Figure~\ref{fig:ovb_bias}, the bias is not random but directional: contaminated models are systematically overestimated under both sequential orderings.
37	
38	\begin{figure}[t]
39	\centering
40	\includegraphics[width=\columnwidth]{fig2_ovb_bias}
41	\caption{Sequential estimation bias ($\hat{\theta}_{\mathrm{seq}} - \theta_{\mathrm{true}}$) versus true contamination susceptibility $c_n$. Pearson $r = 0.86$ ($p < 0.001$) confirms systematic overestimation of contaminated models. Synthetic data ($N = 50$, $I = 100$, $J = 8$, 20 seeds).}
42	\label{fig:ovb_bias}
43	\end{figure}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f457e6e0-4ba4-4822-9c94-a984cceebee3",
  "isSidechain": false,
  "promptId": "a692d8ae-00f1-4be4-9d9f-36a1874f2428",
  "type": "user",
  "uuid": "d837671b-3611-4bcc-8704-d0e0c7ef8f4b",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/background.tex",
      "content": "\\section{Confounding in LLM Evaluation}\n\\label{sec:confounding}\n\nThe Many-Facet Rasch Model (MFRM) extends classical Rasch measurement to settings with multiple rater facets \\citep{linacre1989mfrm, linacre1994mfrm}. Originating in educational measurement, the model treats rater variation as a nuisance facet to be estimated and removed rather than a source of noise to be averaged over. In the LLM evaluation context, where $J$ judges score $N$ models across $I$ items, the MFRM specifies\n%\n\\begin{equation}\n\\label{eq:mfrm}\n\\log \\frac{P(Y_{nij} \\geq k \\mid \\theta_n, b_i, d_j, \\tau_k)}{P(Y_{nij} < k \\mid \\theta_n, b_i, d_j, \\tau_k)} = \\theta_n - b_i - d_j - \\tau_k,\n\\end{equation}\n%\nwhere $Y_{nij}$ is the ordinal rating by judge $j$ for model $n$ on item $i$, $\\theta_n$ is the ability of model $n$ ($n = 1, \\ldots, N$), $b_i$ is the difficulty of item $i$ ($i = 1, \\ldots, I$), $d_j$ is the severity of judge $j$ ($j = 1, \\ldots, J$), and $\\tau_k$ is the threshold for category $k$. All facets reside on a common logit scale, so model ability is directly comparable after adjustment for item difficulty and judge severity. \\citet{wang2025mfrm_llm} applied this framework to LLM rater calibration and showed that MFRM separates genuine ability from systematic judge effects in multi-judge panels.\n\nHowever, standard MFRM assumes that all systematic sources of score variation are captured by the modeled facets. This assumption breaks down when some models have been exposed to benchmark items during training \\citep{dcr2025}. Such contamination inflates scores on exposed items through memorization rather than genuine ability. We represent this effect as an interaction $c_n \\cdot e_i$, where $c_n \\geq 0$ is the contamination susceptibility of model $n$ and $e_i \\in [0, 1]$ is the exposure level of item $i$. The complete data-generating process becomes\n%\n\\begin{equation}\n\\label{eq:full}\n\\eta_{nijk} = \\theta_n - b_i - d_j - \\tau_k + c_n \\cdot e_i.\n\\end{equation}\n%\nWhen a practitioner fits the standard MFRM (Eq.~\\ref{eq:mfrm}) to data generated by Eq.~\\ref{eq:full}, the contamination term is absent from the estimated model. Its influence does not vanish but is absorbed into the estimated parameters $\\tilde{\\theta}_n$, $\\tilde{b}_i$, and $\\tilde{d}_j$, which distorts all downstream inferences.\n\nThe consequence of this omission can be stated precisely.\n\n\\begin{observation}[Omitted Variable Bias in MFRM]\n\\label{obs:ovb}\nLet the full model be $\\eta_{nijk} = \\theta_n - b_i - d_j - \\tau_k + c_n \\cdot e_i$ and the short model omit the contamination term: $\\tilde{\\eta}_{nijk} = \\tilde{\\theta}_n - \\tilde{b}_i - \\tilde{d}_j - \\tau_k$. By the omitted variable bias (OVB) formula \\citep{angrist2009mostly},\n\\begin{equation}\n\\label{eq:ovb}\n\\mathrm{plim}(\\tilde{\\theta}_n - \\theta_n) = \\gamma_n \\cdot c_n,\n\\end{equation}\nwhere $\\gamma_n$ depends on the projection of the exposure vector $(e_i)$ onto the design matrix of the short model. The bias is non-zero whenever $\\mathrm{Cov}(d_j,\\, c_n \\cdot e_i) \\neq 0$.\n\\end{observation}\n\nObservation~\\ref{obs:ovb} is a direct application of the classical OVB result from \\citet{angrist2009mostly} to the MFRM setting. The condition for bias, non-orthogonality between judge severity and contamination effects, holds in practice: lenient judges (low $d_j$) tend to amplify score inflation on exposed items, while strict judges compress it. The bias magnitude scales with $c_n$, so heavily contaminated models receive the largest upward distortion in estimated ability. In the linear analogue, this reduces to the short-regression bias $\\tilde{\\beta} - \\beta = \\delta \\cdot \\gamma$, where $\\delta$ captures the auxiliary regression of the omitted variable on the included regressors. When both $c_n$ and $d_j$ are present, any estimate of model ability from a specification that includes one facet but omits the other carries this asymptotic bias. The Observation thus establishes not only the existence of bias but also its direction and relative magnitude across models.\n\nThis confounding undermines both sequential estimation strategies. A bias-first approach, as in CyclicJudge \\citep{cyclicjudge2026}, calibrates $d_j$ before estimating ability, but the resulting $\\hat{\\theta}$ is already inflated for contaminated models because the omitted $c_n \\cdot e_i$ term has been absorbed into the ability estimates. A contamination-first approach, as in DCR \\citep{dcr2025}, adjusts for contamination before addressing judge effects, but judge severity is then misattributed as contamination signal. Synthetic validation confirms this failure: with $N = 50$ models, $I = 100$ items, $J = 8$ judges, $\\rho = 0.6$, and 20 random seeds, the Pearson correlation between sequential estimation bias and true $c_n$ reaches $r = 0.86$ ($p < 0.001$). As illustrated in Figure~\\ref{fig:ovb_bias}, the bias is not random but directional: contaminated models are systematically overestimated under both sequential orderings.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig2_ovb_bias}\n\\caption{Sequential estimation bias ($\\hat{\\theta}_{\\mathrm{seq}} - \\theta_{\\mathrm{true}}$) versus true contamination susceptibility $c_n$. Pearson $r = 0.86$ ($p < 0.001$) confirms systematic overestimation of contaminated models. Synthetic data ($N = 50$, $I = 100$, $J = 8$, 20 seeds).}\n\\label{fig:ovb_bias}\n\\end{figure}",
      "numLines": 43,
      "startLine": 1,
      "totalLines": 43
    }
  },
  "sourceToolAssistantUUID": "f457e6e0-4ba4-4822-9c94-a984cceebee3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "a5cf6865-9f22-4f8b-931a-5ff939509219",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-22T13:17:45.140Z_

<details open><summary>🔧 Tool call — Read · `toolu_01KHq8Ujq23ScrW6yKFayVvV`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d837671b-3611-4bcc-8704-d0e0c7ef8f4b",
  "isSidechain": false,
  "requestId": "req_011CbHfwBx3c5uPz16kpT7ES",
  "type": "assistant",
  "uuid": "b6bffdc0-9820-469f-b9e4-d284810151be",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "a5cf6865-9f22-4f8b-931a-5ff939509219",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AYP8v5Qt5bJRArFM48P1hp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 13888,
      "cache_read_input_tokens": 11841,
      "output_tokens": 282,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13888,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 282,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 13888,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13888
          },
          "type": "message"
        }
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
  "leafUuid": "53cfc2d9-d536-452f-bf3c-553d1bbb00ef",
  "sessionId": "a5cf6865-9f22-4f8b-931a-5ff939509219"
}
```

---

### Runtime record

_source line 18_

```json
{
  "type": "ai-title",
  "aiTitle": "Write G-MFRM paper Introduction section",
  "sessionId": "a5cf6865-9f22-4f8b-931a-5ff939509219"
}
```

---

### Assistant

_source line 19 · 2026-05-22T13:17:49.281Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the materials needed. Let me also check if there's an existing introduction.tex file and what the bib file looks like to confirm the citation keys.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "53cfc2d9-d536-452f-bf3c-553d1bbb00ef",
  "isSidechain": false,
  "requestId": "req_011CbHfwcccembwF33uydyKn",
  "type": "assistant",
  "uuid": "91ae835a-6c0f-4eb5-82ee-738c8764b613",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "a5cf6865-9f22-4f8b-931a-5ff939509219",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AxxU8Ddut9hCAkdja1Wuvr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17015,
      "cache_read_input_tokens": 25729,
      "output_tokens": 250,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 17015,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 250,
          "cache_read_input_tokens": 25729,
          "cache_creation_input_tokens": 17015,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 17015
          },
          "type": "message"
        }
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

_source line 20 · 2026-05-22T13:17:50.172Z_

Let me check existing files for citation keys and any existing introduction.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "91ae835a-6c0f-4eb5-82ee-738c8764b613",
  "isSidechain": false,
  "requestId": "req_011CbHfwcccembwF33uydyKn",
  "type": "assistant",
  "uuid": "ac3463f6-2613-46f8-903d-27770c6ea2bf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "a5cf6865-9f22-4f8b-931a-5ff939509219",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AxxU8Ddut9hCAkdja1Wuvr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17015,
      "cache_read_input_tokens": 25729,
      "output_tokens": 250,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 17015,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 250,
          "cache_read_input_tokens": 25729,
          "cache_creation_input_tokens": 17015,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 17015
          },
          "type": "message"
        }
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

_source line 21 · 2026-05-22T13:17:51.859Z_

<details open><summary>🔧 Tool call — Glob · `toolu_0131k29A77E2CeWpTuJihnSY`</summary>

```json
{
  "pattern": "**/*.bib",
  "path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ac3463f6-2613-46f8-903d-27770c6ea2bf",
  "isSidechain": false,
  "requestId": "req_011CbHfwcccembwF33uydyKn",
  "type": "assistant",
  "uuid": "a888ee73-24f1-4ff6-95cc-27dd9955a336",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "a5cf6865-9f22-4f8b-931a-5ff939509219",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AxxU8Ddut9hCAkdja1Wuvr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17015,
      "cache_read_input_tokens": 25729,
      "output_tokens": 250,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 17015,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 250,
          "cache_read_input_tokens": 25729,
          "cache_creation_input_tokens": 17015,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 17015
          },
          "type": "message"
        }
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

_source line 22 · 2026-05-22T13:17:52.507Z_

<details><summary>↩ Tool result · `toolu_01JFxWDpp3rMnhghccaSJE99`</summary>

```text
No files found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9485ff5d-e91f-4a1d-a2eb-bd7ccefc0f39",
  "isSidechain": false,
  "promptId": "a692d8ae-00f1-4be4-9d9f-36a1874f2428",
  "type": "user",
  "uuid": "13b370b2-bebb-4794-91de-8e7714837102",
  "toolUseResult": {
    "filenames": [],
    "durationMs": 6,
    "numFiles": 0,
    "truncated": false
  },
  "sourceToolAssistantUUID": "9485ff5d-e91f-4a1d-a2eb-bd7ccefc0f39",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "a5cf6865-9f22-4f8b-931a-5ff939509219",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-22T13:17:51.878Z_

<details><summary>↩ Tool result · `toolu_0131k29A77E2CeWpTuJihnSY`</summary>

```text
docs/paper/references.bib
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a888ee73-24f1-4ff6-95cc-27dd9955a336",
  "isSidechain": false,
  "promptId": "a692d8ae-00f1-4be4-9d9f-36a1874f2428",
  "type": "user",
  "uuid": "d1cf35cf-07f0-4de7-8532-5a13bb0fe882",
  "toolUseResult": {
    "filenames": [
      "docs/paper/references.bib"
    ],
    "durationMs": 10,
    "numFiles": 1,
    "truncated": false
  },
  "sourceToolAssistantUUID": "a888ee73-24f1-4ff6-95cc-27dd9955a336",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "a5cf6865-9f22-4f8b-931a-5ff939509219",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-22T13:17:52.498Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01JFxWDpp3rMnhghccaSJE99`</summary>

```json
{
  "pattern": "**/introduction.tex",
  "path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d1cf35cf-07f0-4de7-8532-5a13bb0fe882",
  "isSidechain": false,
  "requestId": "req_011CbHfwcccembwF33uydyKn",
  "type": "assistant",
  "uuid": "9485ff5d-e91f-4a1d-a2eb-bd7ccefc0f39",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "a5cf6865-9f22-4f8b-931a-5ff939509219",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AxxU8Ddut9hCAkdja1Wuvr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17015,
      "cache_read_input_tokens": 25729,
      "output_tokens": 250,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 17015,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 250,
          "cache_read_input_tokens": 25729,
          "cache_creation_input_tokens": 17015,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 17015
          },
          "type": "message"
        }
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

_source line 25 · 2026-05-22T13:17:54.864Z_

<details open><summary>🔧 Tool call — Read · `toolu_01EbCoscnBrCmPxbJbkjYW6y`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "13b370b2-bebb-4794-91de-8e7714837102",
  "isSidechain": false,
  "requestId": "req_011CbHfxA3UNpcfXCL9PaRG3",
  "type": "assistant",
  "uuid": "ea733791-7f0f-412d-a1c6-e80ded491220",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "a5cf6865-9f22-4f8b-931a-5ff939509219",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ENeVwgJmwZ6x3X3H5UtS16",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 322,
      "cache_read_input_tokens": 42744,
      "output_tokens": 87,
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
          "output_tokens": 87,
          "cache_read_input_tokens": 42744,
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

_source line 26 · 2026-05-22T13:17:54.868Z_

<details><summary>↩ Tool result · `toolu_01EbCoscnBrCmPxbJbkjYW6y`</summary>

```text
&lt;system-reminder>Warning: the file exists but is shorter than the provided offset (1). The file has 1 lines.&lt;/system-reminder>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ea733791-7f0f-412d-a1c6-e80ded491220",
  "isSidechain": false,
  "promptId": "a692d8ae-00f1-4be4-9d9f-36a1874f2428",
  "type": "user",
  "uuid": "634dbac4-92d7-4760-8c3c-2ebcf798806d",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/references.bib",
      "content": "",
      "numLines": 1,
      "startLine": 1,
      "totalLines": 1
    }
  },
  "sourceToolAssistantUUID": "ea733791-7f0f-412d-a1c6-e80ded491220",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "a5cf6865-9f22-4f8b-931a-5ff939509219",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-22T13:18:02.630Z_

<details open><summary>🔧 Tool call — Read · `toolu_01DmfrX59FvmnCbGKymbheKG`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/references.bib",
  "offset": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "634dbac4-92d7-4760-8c3c-2ebcf798806d",
  "isSidechain": false,
  "requestId": "req_011CbHfxLK7G8yK4KsUMN4xN",
  "type": "assistant",
  "uuid": "a7f44605-8e41-450a-997b-feadd103d411",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "a5cf6865-9f22-4f8b-931a-5ff939509219",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0186M7TN2qyFY8LgcB346Bff",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 129,
      "cache_read_input_tokens": 43066,
      "output_tokens": 104,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 129,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 104,
          "cache_read_input_tokens": 43066,
          "cache_creation_input_tokens": 129,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 129
          },
          "type": "message"
        }
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

_source line 28 · 2026-05-22T13:18:02.637Z_

<details><summary>↩ Tool result · `toolu_01DmfrX59FvmnCbGKymbheKG`</summary>

```text
&lt;system-reminder>Warning: the file exists but is shorter than the provided offset (0). The file has 1 lines.&lt;/system-reminder>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a7f44605-8e41-450a-997b-feadd103d411",
  "isSidechain": false,
  "promptId": "a692d8ae-00f1-4be4-9d9f-36a1874f2428",
  "type": "user",
  "uuid": "5bf1a897-bb6a-4154-8245-385d51baf305",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/references.bib",
      "content": "",
      "numLines": 1,
      "startLine": 0,
      "totalLines": 1
    }
  },
  "sourceToolAssistantUUID": "a7f44605-8e41-450a-997b-feadd103d411",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "a5cf6865-9f22-4f8b-931a-5ff939509219",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 29 · 2026-05-22T13:18:02.641Z_

```json
{
  "parentUuid": "5bf1a897-bb6a-4154-8245-385d51baf305",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "e42585c7-a781-44c1-9569-11a9eafbd28b",
  "timestamp": "2026-05-22T13:18:02.641Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "a5cf6865-9f22-4f8b-931a-5ff939509219",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 30 · 2026-05-22T13:18:07.166Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01UHM3VoE97j2nunK6SjYYe1`</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/references.bib",
  "description": "Check bib file contents"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e42585c7-a781-44c1-9569-11a9eafbd28b",
  "isSidechain": false,
  "requestId": "req_011CbHfxuD2kRZcTJUeyEMFs",
  "type": "assistant",
  "uuid": "fd212744-5dfa-4b13-aa78-75a018c9d2bd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "a5cf6865-9f22-4f8b-931a-5ff939509219",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DHmsmuwyjscNfGK7K72Ffn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 250,
      "cache_read_input_tokens": 43195,
      "output_tokens": 108,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 250,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 108,
          "cache_read_input_tokens": 43195,
          "cache_creation_input_tokens": 250,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 250
          },
          "type": "message"
        }
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

_source line 31 · 2026-05-22T13:18:07.326Z_

<details><summary>↩ Tool result · `toolu_01UHM3VoE97j2nunK6SjYYe1`</summary>

```text
(Bash completed with no output)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fd212744-5dfa-4b13-aa78-75a018c9d2bd",
  "isSidechain": false,
  "promptId": "a692d8ae-00f1-4be4-9d9f-36a1874f2428",
  "type": "user",
  "uuid": "010ac30b-c4b4-4e04-9f35-18722507db09",
  "toolUseResult": {
    "stdout": "",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "fd212744-5dfa-4b13-aa78-75a018c9d2bd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "a5cf6865-9f22-4f8b-931a-5ff939509219",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 32 · 2026-05-22T13:18:12.049Z_

<details><summary>Logged reasoning block</summary>

```text
The bib file is empty. Let me also check the main.tex to understand the document structure and how sections are included.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "010ac30b-c4b4-4e04-9f35-18722507db09",
  "isSidechain": false,
  "requestId": "req_011CbHfyFCZJjBiFXxvFZhoS",
  "type": "assistant",
  "uuid": "f6a0adee-ce42-4bde-a5f2-d9f7804bb486",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "a5cf6865-9f22-4f8b-931a-5ff939509219",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JWRpGXHJPhCHT8VSC5r7iK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 126,
      "cache_read_input_tokens": 43445,
      "output_tokens": 141,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 126,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 141,
          "cache_read_input_tokens": 43445,
          "cache_creation_input_tokens": 126,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 126
          },
          "type": "message"
        }
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

_source line 33 · 2026-05-22T13:18:12.262Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01FGcC7y84dxryxjE4entwKn`</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f6a0adee-ce42-4bde-a5f2-d9f7804bb486",
  "isSidechain": false,
  "requestId": "req_011CbHfyFCZJjBiFXxvFZhoS",
  "type": "assistant",
  "uuid": "20877940-81bb-44b7-ab87-ce39b63bdfdb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "a5cf6865-9f22-4f8b-931a-5ff939509219",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JWRpGXHJPhCHT8VSC5r7iK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 126,
      "cache_read_input_tokens": 43445,
      "output_tokens": 141,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 126,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 141,
          "cache_read_input_tokens": 43445,
          "cache_creation_input_tokens": 126,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 126
          },
          "type": "message"
        }
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

_source line 34 · 2026-05-22T13:18:12.271Z_

<details><summary>↩ Tool result · `toolu_01FGcC7y84dxryxjE4entwKn`</summary>

```text
docs/paper/background.tex
docs/paper/main.tex
docs/paper/method.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "20877940-81bb-44b7-ab87-ce39b63bdfdb",
  "isSidechain": false,
  "promptId": "a692d8ae-00f1-4be4-9d9f-36a1874f2428",
  "type": "user",
  "uuid": "c66d9e7c-b676-4cdc-a0bb-679c2e5cfc58",
  "toolUseResult": {
    "filenames": [
      "docs/paper/background.tex",
      "docs/paper/main.tex",
      "docs/paper/method.tex"
    ],
    "durationMs": 6,
    "numFiles": 3,
    "truncated": false
  },
  "sourceToolAssistantUUID": "20877940-81bb-44b7-ab87-ce39b63bdfdb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "a5cf6865-9f22-4f8b-931a-5ff939509219",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-22T13:18:15.546Z_

<details open><summary>🔧 Tool call — Read · `toolu_01RXKhdcspxrjzrHikyTxR1x`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c66d9e7c-b676-4cdc-a0bb-679c2e5cfc58",
  "isSidechain": false,
  "requestId": "req_011CbHfycg8tzZjrtinsQzxZ",
  "type": "assistant",
  "uuid": "d1c30836-7572-4bbf-b4d1-35b4ee685d41",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "a5cf6865-9f22-4f8b-931a-5ff939509219",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017P15PzmpRp6Yftfhhecwjr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 176,
      "cache_read_input_tokens": 43571,
      "output_tokens": 86,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 176,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 86,
          "cache_read_input_tokens": 43571,
          "cache_creation_input_tokens": 176,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 176
          },
          "type": "message"
        }
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

_source line 36 · 2026-05-22T13:18:15.550Z_

<details><summary>↩ Tool result · `toolu_01RXKhdcspxrjzrHikyTxR1x`</summary>

```text
1	\documentclass[11pt]{article}
2	
3	\usepackage[review]{acl}
4	
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	\usepackage{inconsolata}
11	\usepackage{graphicx}
12	\usepackage{amsmath}
13	\usepackage{amssymb}
14	\usepackage{amsthm}
15	\usepackage{booktabs}
16	\usepackage{xcolor}
17	\usepackage{subcaption}
18	
19	\newtheorem{observation}{Observation}
20	\newtheorem{proposition}{Proposition}
21	\newtheorem{theorem}{Theorem}
22	\newtheorem{corollary}{Corollary}
23	
24	\graphicspath{{../../figures/paper/}}
25	
26	\title{Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model\\for Disentangling Judge Bias and Contamination in LLM Evaluation}
27	
28	\author{Anonymous}
29	
30	\begin{document}
31	\maketitle
32	
33	\input{abstract}
34	\input{introduction}
35	\input{background}
36	\input{method}
37	\input{experiments}
38	\input{related_work}
39	\input{conclusion}
40	
41	\section*{Limitations}
42	\input{limitations}
43	
44	\bibliography{references}
45	\bibliographystyle{acl_natbib}
46	
47	\end{document}
48	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d1c30836-7572-4bbf-b4d1-35b4ee685d41",
  "isSidechain": false,
  "promptId": "a692d8ae-00f1-4be4-9d9f-36a1874f2428",
  "type": "user",
  "uuid": "d6c675f3-bdc5-4e12-83ba-d8d47939aafe",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/main.tex",
      "content": "\\documentclass[11pt]{article}\n\n\\usepackage[review]{acl}\n\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage[T1]{fontenc}\n\\usepackage[utf8]{inputenc}\n\\usepackage{microtype}\n\\usepackage{inconsolata}\n\\usepackage{graphicx}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{amsthm}\n\\usepackage{booktabs}\n\\usepackage{xcolor}\n\\usepackage{subcaption}\n\n\\newtheorem{observation}{Observation}\n\\newtheorem{proposition}{Proposition}\n\\newtheorem{theorem}{Theorem}\n\\newtheorem{corollary}{Corollary}\n\n\\graphicspath{{../../figures/paper/}}\n\n\\title{Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model\\\\for Disentangling Judge Bias and Contamination in LLM Evaluation}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n\\input{abstract}\n\\input{introduction}\n\\input{background}\n\\input{method}\n\\input{experiments}\n\\input{related_work}\n\\input{conclusion}\n\n\\section*{Limitations}\n\\input{limitations}\n\n\\bibliography{references}\n\\bibliographystyle{acl_natbib}\n\n\\end{document}\n",
      "numLines": 48,
      "startLine": 1,
      "totalLines": 48
    }
  },
  "sourceToolAssistantUUID": "d1c30836-7572-4bbf-b4d1-35b4ee685d41",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "a5cf6865-9f22-4f8b-931a-5ff939509219",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 37 · 2026-05-22T13:23:18.110Z_

<details><summary>Logged reasoning block</summary>

```text
Good. Now I have all the context I need. Let me write the introduction.tex file.

Key things to check:
- The paper title mentions "G-MFRM" and "Gated Many-Facet Rasch Model"
- background.tex is Section 2 titled "Confounding in LLM Evaluation" with label `sec:confounding`
- method.tex is Section 3 titled "The G-MFRM Framework" with label `sec:method`
- Figure labels in background.tex: `fig:ovb_bias` (Figure 2)


- Figure labels in method.tex: `fig:error_prop` and `tab:error_prop`
- Figure 1 is `fig:framework`

Now I'm looking at the experimental results. The mvp_003 results show a substantial improvement with joint RMSE of 0.1243 compared to sequential RMSE of 0.2211, representing a 43.8% reduction with strong statistical significance. The OVB bias analysis shows a Pearson correlation of 0.86, indicating good agreement between the model predictions and observed bias patterns.

I need to track down several citations including work on causal inference, measurement frameworks, and recent LLM evaluation benchmarks. The key references to integrate are the framework figure, the confounding section, and the method section. I should avoid em-dashes, -ing phrase endings, and generic capability statements when writing this up.

Now I'm structuring the introduction around a quantitative finding: when correcting for judge bias and benchmark contamination separately, the estimates are biased because these two issues are confounded. The joint correction yields an RMSE of 0.124 compared to 0.221 from sequential correction—a 43.8% difference with strong statistical significance. This motivates the need for a structural approach that handles both sources of error simultaneously rather than treating them in isolation. I'm thinking through the prose flow for the introduction—it should establish the dual problem of judge bias and contamination at a conceptual level before the background section gets into the mathematical details. I'm drafting the opening to explain how these two distortion sources affect LLM evaluation, then noting that existing methods address them separately, which sets up why a unified approach is needed.

The synthetic experiment results are striking: sequential correction yields RMSE of 0.221 versus 0.124 for joint estimation, a substantial gap driven by structural confounding rather than noise. This empirical motivation justifies moving beyond isolated corrections and frames the contribution clearly. I'm working through the acronym definitions for the introduction—LLM should be defined on first use even though it's common in NLP, and I need to make sure MFRM, G-MFRM, DG-IRT, OVB, and RMSE all get their full forms when they first appear.

Now I'm drafting the introduction section, starting with how LLM-as-a-judge evaluation works and the two main distortions—judge bias and benchmark contamination—that affect these evaluations, then explaining how current correction methods treat them separately, which creates problems when practitioners try to apply both sequentially.

I'm showing the empirical evidence from synthetic experiments: when correcting sequentially across 50 models, 100 items, and 8 judges, the ability estimation error jumps to 0.221 RMSE compared to 0.124 for joint estimation—a substantial 43.8% increase that's statistically significant. The key insight is that this gap stems from structural confounding between the two distortions rather than just estimation noise, meaning sequential correction fundamentally can't resolve how they interact.

Now I'm reconsidering the structure to make the opening more impactful, thinking about how to frame this as a quantitative shock that hooks the reader immediately with the core problem.

Looking at the existing methods, I see they operate in separate silos: judge bias correction techniques like CyclicJudge use round-robin designs to average out bias but ignore contamination entirely, while neural approaches like UDA reduce inter-judge variance by 63.4% but remain black-box and unaware of contamination. On the contamination side, methods like ConStat focus on reference-based detection but don't account for judge bias.

The fundamental issue is that these approaches create a confounding problem—correcting for bias first absorbs contamination inflation into ability estimates, while correcting for contamination first misattributes judge effects as contamination signals. Sequential pipelines can't resolve this because the first step's estimates are already shifted by unmeasured factors.

I'm formalizing this confounding as an omitted variable bias problem, where judge severity and contamination are correlated, creating bias in downstream estimates.

Now I'm introducing G-MFRM, which combines the multi-facet structure with a gating mechanism, using a three-stage calibration process that starts with warm initialization, then incorporates external exposure estimates, and finally performs joint inference.

I'm proving that fixing the exposure parameters eliminates the bilinear ambiguity through identifiability analysis, and I'm quantifying how noise from the exposure estimation stage affects the final estimates—showing that with reasonable noise levels, the degradation in accuracy stays below 6%.

For the contributions, I need to formalize how judge bias and contamination confound each other as an omitted variable bias problem, and present the G-MFRM framework with its identifiability guarantees. I'm checking the proposition and theorem count against what's actually in the method section. I see Proposition 1, Proposition 2, Theorem 1, and Corollary 1 so far, but the task specifies 7 propositions plus 1 theorem, so I'll trust that specification since there may be additional results in the appendix or still being written. Now I'm drafting the introduction section, starting with how LLM-as-a-judge evaluation works and the two main sources of distortion: judge bias and response order effects.

I'm explaining that while the research community has developed separate correction methods for each problem, practitioners need both corrections applied jointly rather than sequentially. I'm presenting empirical evidence from synthetic experiments showing that sequential correction yields much higher error rates compared to joint estimation, demonstrating a significant performance gap that reflects structural confounding between the two sources of distortion. I'm also beginning to describe existing judge bias correction approaches like CyclicJudge.

Now I'm surveying the landscape of existing methods—judge bias corrections like CyclicJudge and UDA that reduce inter-judge variance, alongside contamination detection approaches like ConStat, DCR, and LogProber that operate independently. The key insight is that these two families of methods work in isolation, so applying them sequentially creates a dilemma: correcting bias first leaves contamination-induced inflation in the ability estimates, while correcting contamination first leaves uncorrected bias effects.

I'm formalizing this as an omitted variable bias problem within the Many-Facet Rasch Model framework—when you fit a model that includes judge severity but omits the contamination interaction (or vice versa), you get asymptotically biased estimates whenever these two facets correlate. And they do correlate in practice: lenient judges amplify score inflation on exposed items while strict judges compress it, creating systematic non-orthogonality between the facets.

Synthetic validation bears this out with a strong correlation of 0.86 between sequential estimation bias and true contamination susceptibility, confirming that sequential correction systematically overestimates contaminated models. To address this, I'm proposing the Gated Many-Facet Rasch Model, which integrates the multi-facet structure of MFRM with a gating mechanism from Doubly-Gated IRT to jointly estimate ability, judge severity, and contamination susceptibility in a single framework using a three-stage calibration procedure.

The key innovation is fixing exposure values externally in the final MCMC stage, which resolves the fundamental non-identifiability problem in the product of contamination and exposure. I've proven this through an identifiability analysis with seven propositions and a theorem establishing necessary and sufficient conditions for parameter separation, and an error propagation analysis shows that when exposure measurement error stays below 0.2, the resulting ability estimation degradation remains under 6%.

Now I'm laying out the main contributions: formalizing the confounding between judge bias and benchmark contamination as an omitted variable bias problem, proposing the G-MFRM framework with formal identifiability guarantees and error propagation bounds, and demonstrating through synthetic validation that joint estimation substantially outperforms sequential estimation with a 43.8% reduction in ability RMSE and notably higher rank correlation.

I'm checking the word count on the introduction paragraphs and finding they're running short of the target, so I need to expand several sections to add more context and detail about why LLM-as-a-judge evaluation matters, the structural problems at play, the omitted variable bias mechanism, and the methodological approach. Judge bias correction methods like CyclicJudge and UDA reduce inter-judge variation but ignore contamination entirely, while contamination detection approaches like ConStat, DCR, and LogProber work independently without accounting for judge bias. The core problem is that applying these corrections sequentially doesn't resolve the underlying interaction between bias and contamination—when bias correction runs first, contamination-induced inflation gets baked into ability estimates because the correction process treats it as genuine signal.

I'm now formalizing this as an omitted variable bias problem within the Many-Facet Rasch Model framework, where fitting a model that includes judge severity but omits contamination effects (or vice versa) produces asymptotically biased estimates whenever these two facets correlate with each other.

In practice, lenient judges amplify score inflation on exposed items while strict judges compress it, creating systematic correlation between judge and contamination effects. The bias scales with each model's contamination susceptibility, so the most contaminated models get the largest upward distortion. Synthetic validation confirms this: the correlation between sequential estimation bias and true contamination susceptibility reaches 0.86 (p < 0.001), confirming that contaminated models are systematically overestimated under sequential correction.

To address this, I'm proposing the Gated Many-Facet Rasch Model, which merges the multi-facet structure of MFRM with a gating mechanism from Doubly-Gated IRT to jointly estimate model ability, judge severity, and contamination susceptibility in one framework. The model adds a multiplicative contamination term to the standard MFRM predictor, where the contamination susceptibility parameter captures model-specific vulnerability and an exposure parameter quantifies item-level exposure. Since this product term isn't identifiable from response data alone, I need to incorporate additional constraints...

The solution is a three-stage calibration approach: first, I run standard MFRM to get initial estimates, then I estimate item exposure externally using data independent of the responses, and finally I use MCMC sampling with those exposure values fixed. This external constraint resolves the identifiability problem, and I've established through formal analysis that this approach is both necessary and sufficient for separating the parameters. I've also analyzed how measurement error from the exposure estimation propagates downstream—when exposure error stays below 0.2, the ability estimates degrade by less than 6%. The key contribution is formalizing how judge bias and benchmark contamination confound each other in LLM evaluation. I'm expanding the substance of each paragraph to meet academic standards, particularly beefing up the discussion of the OVB mechanism and what distinguishes G-MFRM from simpler approaches. I should also watch for sentences that end with -ing phrases, which need to be restructured. ated scores on items encountered during training. Both problems have received sustained attention from the research community, and each has produced a substantial toolkit of correction methods. These toolkits, however, treat the two problems as independent and address them in separate pipelines. A practitioner who needs both corrections must apply them sequentially: first correct one source of distortion, then correct the other. This sequential approach produces unreliable ability estimates. In synthetic experiments with 50 models, 100 items, and 8 judges, sequential estimation yields ability root mean squared error (RMSE) of 0.221, while joint estimation achieves 0.124, representing a 43.8\% RMSE reduction (Wilcoxon $p < 10^{-6}$). The gap does not arise from estimation noise but from structural confounding between judge bias and contamination that no sequential pipeline can resolve.

P2 (expanded):

Existing judge bias correction methods remove systematic differences across judges without modeling contamination. CyclicJudge uses round-robin pairing to balance judge exposure across model pairs, but treats all remaining score variation as genuine signal. UDA learns a neural adjustment that reduces inter-judge variance by 63.4%, though it operates as a black-box without accounting for contamination effects. On the contamination side, ConStat compares target models against reference models to estimate item-level contamination with high accuracy, DCR applies fuzzy inference to adjust scores on suspected leaked items, and LogProber detects memorization by probing token-level probabilities. These separate families of methods don't interact when combined sequentially, and applying bias correction first creates downstream problems that contamination correction alone cannot fix.

A bias-first pipeline absorbs contamination-induced score inflation into ability estimates because the bias model attributes all residual systematic variation to genuine ability differences. A contamination-first pipeline misattributes judge severity differences as contamination signals because score elevation from a lenient judge is indistinguishable from score elevation due to memorization without a joint model. In either ordering, the first correction stage produces estimates already distorted by the unmodeled facet, and the second stage inherits this distortion with no mechanism for self-correction.

P3 (expanded):

We formalize this confounding as an omitted variable bias problem in the econometric sense. Within the Many-Facet Rasch Model framework, fitting a specification that includes judge severity but omits the contamination interaction produces asymptotically biased parameter estimates whenever the two facets are non-orthogonal. This condition holds in practice: lenient judges amplify score inflation on exposed items, while strict judges compress it, creating a systematic dependence between judge effects and contamination effects. The omitted variable bias framework predicts that sequential estimation will produce biased ability estimates, and this prediction is borne out in our experiments.

The core insight is that judge bias and contamination are not independent sources of distortion—they interact in ways that sequential correction cannot disentangle. A joint model that estimates both facets simultaneously is necessary to recover unbiased ability estimates.

The sequential approach fails because it treats two interdependent problems as if they were independent. When judge bias is corrected first, contamination effects get absorbed into ability estimates. When contamination is corrected first, judge severity differences get misattributed as contamination signals. Either way, the first correction stage distorts the estimates, and the second stage inherits and propagates that distortion. Formalizing this as an omitted variable bias problem shows that judge effects and contamination effects are non-orthogonal in practice—lenient judges amplify score inflation on exposed items while strict judges compress it—so sequential estimation produces asymptotically biased parameters. Only a joint model that estimates both facets simultaneously can recover unbiased ability estimates. ional to contamination levels, and the G-MFRM framework with formal identifiability guarantees and error propagation bounds successfully reduces ability estimation error by 43.8% compared to sequential methods, achieving a Kendall rank correlation of 0.922 versus 0.859 in synthetic validation.

Now I'm reconsidering the word distribution across the paragraphs. I need about 1100 words total, so I should aim for roughly 220 words in the first paragraph, 280 in the second, 200 in the third, 260 in the fourth, and 140 in the list. Let me expand the opening paragraphs with more substantive content about the practical implications and technical details. The synthetic experiments show a dramatic improvement: joint estimation reduces ability RMSE to 0.124 compared to 0.221 with sequential correction, a 43.8% reduction that's statistically significant. This gap isn't just noise or implementation artifacts—it stems from structural confounding where contamination inflates scores in patterns that correlate with judge leniency, so correcting one distortion while ignoring the other leaves systematic bias that sequential refinement can't fix. I'm verifying the LaTeX reference labels across the document — `fig:framework` for the framework diagram, `fig:ovb_bias` for the bias figure, and the section references like `sec:confounding` and `sec:method` all check out. I should confirm the experiments section uses `sec:experiments` as its label.

Now I'm finalizing the contribution descriptions, focusing on the synthetic validation results with the joint estimation showing a 43.8% RMSE reduction compared to sequential estimation. I'll report the Kendall tau correlation values rounded to three decimal places: 0.922 for joint and 0.859 for sequential, and I'm skipping the "Real-data results [TBD Phase 2]" note since that's just a task reminder, not content for the paper itself. confirms that the 43.8% figure represents the reduction in RMSE when using joint estimation compared to sequential, not a direct percentage comparison between the two values.

Now I'm drafting the introduction section, which sets up the problem of LLM-as-a-judge evaluation and identifies two key sources of distortion: judge bias and benchmark contamination. The section explains how these issues have been addressed separately through different toolkits.

The next part establishes the core contribution: when practitioners need both corrections, applying them sequentially produces worse results than a joint approach. I'm noting the empirical evidence from synthetic experiments showing that sequential estimation has significantly higher error (RMSE of 0.221) compared to joint estimation (0.124), representing a 43.8% improvement. This gap isn't just noise—it reveals fundamental structural confounding between the two distortion sources that sequential methods can't resolve.

Then I'm transitioning into existing work, starting with how current judge bias correction methods operate independently of contamination considerations, using CyclicJudge as an example of one approach.

Now I'm examining the broader landscape of existing methods across both domains. The key insight I'm developing is that these two families of methods operate in isolation, creating a fundamental problem: whichever correction you apply first distorts the estimates in ways the second correction can't fix. A bias-first approach absorbs contamination effects into ability estimates, while a contamination-first approach misattributes judge severity as contamination signals. Either way, the first stage produces already-distorted estimates that the second stage can't properly disentangle.

I'm formalizing this as an omitted variable bias problem within the Many-Facet Rasch framework. When you fit a model that includes judge severity but omits the contamination interaction, you get asymptotically biased estimates whenever these two facets aren't orthogonal—which they aren't in practice. Lenient judges amplify score inflation on exposed items while strict judges compress it, creating systematic dependence between judge effects and contamination. The theory predicts that the most contaminated models receive the largest upward distortion in their ability estimates, scaled by their contamination susceptibility.

My synthetic validation confirms this: the correlation between estimation bias and true contamination susceptibility reaches 0.86 with strong significance, showing that contaminated models are systematically overestimated regardless of the sequential ordering. To address this, I'm proposing the Gated Many-Facet Rasch Model, which combines the multi-facet structure with a gating mechanism to jointly estimate model ability, judge severity, and contamination susceptibility in one framework. The key innovation is extending the linear predictor with a multiplicative contamination gating term that captures model-specific susceptibility.

Since the bilinear product can't be uniquely decomposed from response data alone, I'm using a three-stage calibration: first a standard warm-start to initialize parameters, then external per-item exposure estimation from independent evidence, and finally joint sampling with exposure fixed. I've worked through a complete identifiability analysis proving that fixing exposure externally is both necessary and sufficient for parameter separation, and an error propagation analysis showing that when exposure estimation error stays below 0.2, ability degradation remains under 6%.

Now I'm laying out the key contributions: formalizing the confounding between judge bias and benchmark contamination as an omitted variable bias problem with directional bias proportional to contamination levels, proposing the G-MFRM framework with formal identifiability guarantees and error bounds for the staged procedure, and showing through synthetic validation that joint estimation reduces ability RMSE by 43.8% compared to sequential estimation with substantially better rank correlation.

I'm checking the word counts across the paragraphs and finding I'm still under the 1100-word target, so I need to expand a few sections—adding context about why the two-silo paradigm persists across different research communities and what's at stake, elaborating on the symmetric nature of the OVB and its implications, and discussing the non-centered parameterization approach. I'm formalizing the confounding as an omitted variable bias problem within the Many-Facet Rasch Model framework. When fitting a model that includes one source of distortion but omits the other, the parameters become asymptotically biased whenever the two facets correlate—which they do in practice, since lenient judges amplify contamination on exposed items while strict judges suppress it. The bias magnitude scales with each model's contamination susceptibility, meaning the most vulnerable models get the largest upward distortion in their ability estimates.

The bias works symmetrically: omitting contamination inflates ability estimates in a judge-aware model, while omitting judge severity distorts contamination estimates in a contamination-aware model. Synthetic validation confirms this pattern with a strong correlation of 0.86 between the sequential estimation bias and true contamination levels, showing that contaminated models are systematically overestimated regardless of which facet is estimated first.

Now I'm introducing the Gated Many-Facet Rasch Model, which merges the multi-facet structure with a gating mechanism to jointly estimate both sources of distortion. ability, judge severity, and contamination susceptibility in a single measurement framework. G-MFRM extends the MFRM linear predictor with a multiplicative contamination gating term $c_n \cdot e_i$, where $c_n \geq 0$ captures model-specific contamination susceptibility and $e_i \in [0,1]$ quantifies per-item exposure. When $c_n = 0$ or $e_i = 0$, the gating term vanishes and the model reduces to standard MFRM, so uncontaminated model-item pairs incur no distortion. Because the bilinear product $c_n \cdot e_i$ cannot be uniquely decomposed from response data alone, G-MFRM employs a three-stage calibration procedure: (1) standard MFRM warm-start to obtain initial parameter estimates, (2) external per-item exposure estimation from evidence independent of the response data, and (3) joint MCMC sampling with $e_i$ fixed from Stage 2.

I've developed a complete identifiability analysis showing that fixing exposure externally is both necessary and sufficient for separating parameters under standard multi-judge designs, along with an error propagation analysis demonstrating that when exposure estimation error stays below 0.2 standard deviations, ability estimates degrade by less than 6%—a threshold that aligns with the natural variability in true exposure values. I need to finalize the LaTeX label reference and add a key sentence about why accurate ability estimates matter, then insert it strategically in the paragraph before the practitioner example.

The next thinking shows the continuation where I'm demonstrating the problem: when practitioners apply corrections sequentially rather than jointly, they get much worse results. I'm presenting empirical evidence from synthetic experiments showing a 43.8% error reduction with joint estimation, and explaining that this gap reflects structural confounding that sequential approaches can't resolve.

I should compress this to 1-3 sentences that capture the core finding without repeating what's already established about the two distortion sources.

Yet sequential correction of these distortions produces unreliable estimates, as shown in synthetic experiments where joint estimation of judge bias and contamination achieves 43.8% lower ability error than applying corrections sequentially—a gap reflecting structural confounding that no pipeline can resolve. I'm refining that sentence about practical benchmark evaluation to be more insightful—emphasizing how contamination correction specifically prevents the systematic overestimation that occurs when a model's training data overlaps with the benchmark. Let me verify the -ing endings one more time across all paragraphs to make sure none of them end that way, and I'm also checking for em-dashes and other stylistic elements. I'm going through the draft systematically to verify there are no en-dashes or em-dashes, checking each special character carefully. The mathematical notation uses proper minus signs and plus-minus symbols, not dashes, and all the hyphenated compound words like "self-correction," "warm-start," and "non-orthogonal" are regular hyphens as they should be. Everything checks out.

Now I'm noticing the task mentions seven propositions and one theorem, but the method section only shows two propositions and one theorem so far—though that's fine since there could be more in the appendix or sections still being written. I'm also cross-referencing how background.tex and method.tex label their sections and equations to make sure I'm being consistent with the naming conventions already established.

I should double-check that my intro properly defines all the key acronyms on first use: MFRM gets introduced in paragraph 3, DG-IRT in paragraph 4, and I need to make sure MCMC includes its full form rather than just the abbreviation. I'm debating whether to define MCMC in the introduction since it's standard in NLP, but the paper guidelines require defining acronyms on first use, so I'll include the full expansion. Looking at the method section, I see it mentions NUTS sampling, which partially covers this, but I should still define it upfront in the intro.

Now I'm reconsidering the level of detail in P4—the parameterization choices and convergence diagnostics feel too technical for an introduction. Instead, I should focus on what the method produces: bias-corrected ability scores, contamination susceptibility estimates per model, and calibration diagnostics for judges. This better frames the contribution without getting into implementation minutiae.

I'm checking the task outline against what I've written, and it specifies error propagation analysis and noise impact quantification for P4, which I have covered. The outline doesn't mention non-centered parameterization, so I'll keep the intro simpler and move those technical details to the methods section where they belong.

Now I'm drafting the introduction, starting with how LLM-as-a-judge evaluation works and the two main distortion sources—judge bias and benchmark contamination—that are typically treated separately despite needing joint correction. I'm setting up the empirical motivation by contrasting sequential versus joint estimation approaches, showing that joint estimation cuts RMSE nearly in half compared to applying corrections sequentially.

The core issue is structural confounding: judge bias and contamination are entangled in ways that sequential pipelines cannot disentangle. I'm then surveying existing methods—CyclicJudge and UDA for judge bias, ConStat and DCR for contamination—to show that each toolkit operates independently without accounting for the other distortion source.

Now I'm formalizing this as an omitted variable bias problem within the Many-Facet Rasch Model framework, where applying bias correction first absorbs contamination-induced inflation into ability estimates, while contamination-first approaches misattribute judge severity as memorization signals. Either ordering leaves the second stage inheriting distortions from the unmodeled facet with no recovery mechanism.

The key insight is that judge severity and contamination effects are non-orthogonal in practice—lenient judges amplify score inflation on exposed items while strict judges compress it—so fitting a model that includes one facet but omits the other produces asymptotically biased parameter estimates. This means the bias magnitude scales with how contaminated each model is, so the models with the most training data overlap with the benchmark get the largest upward distortion in ability estimates, which is exactly what contamination correction should prevent.

Synthetic validation confirms this pattern with a strong correlation ($r = 0.86$, $p < 0.001$) between estimation bias and true contamination susceptibility across both sequential orderings. To address this, I'm proposing the Gated Many-Facet Rasch Model, which combines the multi-facet structure of MFRM with a gating mechanism from Doubly-Gated IRT to jointly estimate model ability, judge severity, and contamination susceptibility in a single framework, extending the MFRM predictor with a multiplicative contamination gating term.

The gating term uses a product of model-specific contamination susceptibility and per-item exposure that can be zeroed out when either component is absent, reducing to standard MFRM for uncontaminated pairs. Since this bilinear product can't be uniquely identified from response data alone, I'm using a three-stage calibration: initial MFRM estimates as a warm-start, external per-item exposure estimation from independent evidence, and then joint MCMC sampling with exposure values fixed from the second stage, along with a complete identifiability analysis.

The identifiability proof shows that fixing exposure externally is necessary and sufficient for parameter separation under standard multi-judge designs, and an error propagation analysis demonstrates that when exposure estimation error stays below 0.2 standard deviation, ability RMSE degradation remains under 6%. I'm formalizing the confounding between judge bias and benchmark contamination as an omitted variable bias problem, showing that sequential correction produces directional bias proportional to contamination levels, and proposing the G-MFRM framework to address this. I'm running through a final checklist on the paper structure—verifying there are no em-dashes, checking that -ing phrases don't end sentences, confirming each contribution points to its corresponding section and table, and making sure all the numbers come from the experimental registry. I also need to track down that missing citation key for constat2024 since the others are accounted for. I've verified all the citations and cross-references are in place. Now I'm reconsidering a couple of claims in the prose—whether the separation between judge bias and contamination really stems from different research communities rather than principled reasons, and whether "safety evaluation" is the right framing when contaminated models might get selected for safety-critical applications despite inflated performance metrics.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d6c675f3-bdc5-4e12-83ba-d8d47939aafe",
  "isSidechain": false,
  "requestId": "req_011CbHfyrsfJFxxjQSjN9dvA",
  "type": "assistant",
  "uuid": "cdba01f1-cb8a-4769-82f6-d4d5f500b1ac",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "a5cf6865-9f22-4f8b-931a-5ff939509219",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F7hmzxhsJHw6wt9qzx3u9P",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 566,
      "cache_read_input_tokens": 43747,
      "output_tokens": 20105,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 566,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 20105,
          "cache_read_input_tokens": 43747,
          "cache_creation_input_tokens": 566,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 566
          },
          "type": "message"
        }
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

_source line 38 · 2026-05-22T13:23:18.113Z_

Now I have all the context. Writing the introduction.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cdba01f1-cb8a-4769-82f6-d4d5f500b1ac",
  "isSidechain": false,
  "requestId": "req_011CbHfyrsfJFxxjQSjN9dvA",
  "type": "assistant",
  "uuid": "0e8d4561-bf16-4805-8ac1-32ea9d531062",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "a5cf6865-9f22-4f8b-931a-5ff939509219",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F7hmzxhsJHw6wt9qzx3u9P",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 566,
      "cache_read_input_tokens": 43747,
      "output_tokens": 20105,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 566,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 20105,
          "cache_read_input_tokens": 43747,
          "cache_creation_input_tokens": 566,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 566
          },
          "type": "message"
        }
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

_source line 39 · 2026-05-22T13:23:31.638Z_

<details open><summary>🔧 Tool call — Write · `toolu_01KAYLZRDNtp4KJgFKsboiJq`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/introduction.tex",
  "content": "\\section{Introduction}\n\\label{sec:introduction}\n\nLarge Language Model (LLM) evaluation increasingly relies on LLM-as-a-judge protocols, where one or more LLM judges score model responses on structured benchmarks \\citep{zheng2023mtbench}. Two well-documented sources of distortion affect these evaluations: \\emph{judge bias}, where different judges assign systematically different scores to the same response, and \\emph{benchmark contamination}, where models achieve inflated scores on items encountered during training. Both problems have received sustained research attention, producing separate toolkits for bias calibration and contamination detection. These toolkits treat the two distortions as independent phenomena, a separation that reflects their origins in different research communities rather than any principled argument for independence. Accurate ability ranking is essential for model selection, safety evaluation, and benchmark design; systematic distortion in estimated abilities undermines all three. Yet a practitioner who needs both corrections must apply them sequentially: first correct one source of distortion, then the other. This sequential approach produces unreliable ability estimates. In synthetic experiments with 50 models, 100 items, and 8 judges, sequential estimation yields ability root mean squared error (RMSE) of $0.221 \\pm 0.038$, while joint estimation achieves $0.124 \\pm 0.016$, a 43.8\\% reduction (Wilcoxon $p < 10^{-6}$). The gap does not arise from estimation noise or algorithmic limitations of individual methods; it reflects structural confounding between judge bias and contamination that no sequential pipeline can resolve.\n\nExisting judge bias correction methods remove systematic differences across judges without modeling contamination. CyclicJudge \\citep{cyclicjudge2026} uses round-robin pairing to cancel average bias through balanced exposure of model pairs to all judges, but treats all residual score variation as genuine ability signal. UDA \\citep{uda2026} learns a neural K-factor adjustment that reduces inter-judge standard deviation by 63.4\\%, yet operates as a black-box transformation with no mechanism for contamination effects. On the contamination side, ConStat \\citep{constat2024} compares target model performance against a reference model to estimate item-level contamination ($r^2 = 0.94$ with true contamination levels in controlled settings), DCR \\citep{dcr2025} applies fuzzy inference to adjust scores on suspected leaked items, and LogProber \\citep{logprober2024} probes token-level log-probabilities to detect memorization signatures. These two families of methods operate in separate silos. A bias-first pipeline absorbs contamination-induced score inflation into the ability estimates, because the bias model attributes all residual systematic variation to genuine ability differences. A contamination-first pipeline misattributes judge severity differences as contamination signals, because score elevation from a lenient judge is indistinguishable from score elevation due to memorization without a joint model. In either ordering, the first correction stage produces estimates already distorted by the unmodeled facet, and the second stage inherits this distortion with no mechanism for self-correction.\n\nWe formalize this confounding as an omitted variable bias (OVB) problem \\citep{angrist2009mostly}. Within the Many-Facet Rasch Model (MFRM) framework \\citep{linacre1989mfrm}, the complete data-generating process includes both judge severity $d_j$ and a contamination interaction $c_n \\cdot e_i$. Fitting a specification that includes one facet but omits the other produces asymptotically biased parameter estimates whenever the two facets are non-orthogonal. This non-orthogonality holds in practice: lenient judges (low severity $d_j$) amplify score inflation on exposed items, while strict judges compress it, creating systematic dependence between judge effects and contamination effects. The OVB framework predicts that the bias magnitude scales with the contamination susceptibility $c_n$ of each model, so the most contaminated models receive the largest upward distortion in estimated ability. For practical benchmark evaluations, this means that the more a model's training data overlaps with the benchmark, the more its ability is overestimated, precisely the failure mode that contamination correction is designed to prevent. Synthetic validation confirms the predicted pattern: the Pearson correlation between sequential estimation bias and true $c_n$ reaches $r = 0.86$ ($p < 0.001$), which shows that contaminated models are systematically overestimated under both sequential orderings (Section~\\ref{sec:confounding}).\n\nWe propose the Gated Many-Facet Rasch Model (G-MFRM), which combines the multi-facet structure of MFRM \\citep{linacre1989mfrm, wang2025mfrm_llm} with the gating mechanism of Doubly-Gated Item Response Theory (DG-IRT) \\citep{shu2013dgirt} to jointly estimate model ability, judge severity, and contamination susceptibility in a single measurement framework. G-MFRM extends the MFRM linear predictor with a multiplicative contamination gating term $c_n \\cdot e_i$, where $c_n \\geq 0$ captures model-specific contamination susceptibility and $e_i \\in [0,1]$ quantifies per-item exposure. When $c_n = 0$ or $e_i = 0$, the gating term vanishes and the model reduces to standard MFRM, so uncontaminated model-item pairs incur no distortion. Because the bilinear product $c_n \\cdot e_i$ cannot be uniquely decomposed from response data alone, G-MFRM employs a three-stage calibration procedure: (1) standard MFRM warm-start to obtain initial parameter estimates, (2) external per-item exposure estimation from evidence independent of the response data, and (3) joint Markov chain Monte Carlo (MCMC) sampling with $e_i$ fixed from Stage~2. We provide a complete identifiability analysis (seven propositions and one theorem) that proves fixing $e_i$ externally is both necessary and sufficient for parameter separation under standard multi-judge designs (Section~\\ref{sec:method}). A complementary error propagation analysis bounds the impact of Stage~2 measurement noise: when exposure estimation error satisfies $\\sigma \\leq 0.2$, ability RMSE degradation remains below 6\\%. Figure~\\ref{fig:framework} provides an overview of the complete framework.\n\nOur contributions are as follows:\n\\begin{enumerate}\n    \\item We formalize the confounding between judge bias and benchmark contamination in LLM evaluation as an omitted variable bias problem, and show that sequential correction produces directional bias proportional to model contamination levels (Section~\\ref{sec:confounding}, Figure~\\ref{fig:ovb_bias}).\n    \\item We propose the G-MFRM framework with formal identifiability guarantees (seven propositions and one theorem) and quantified error propagation bounds for the staged estimation procedure (Section~\\ref{sec:method}, Figure~\\ref{fig:error_prop}, Table~\\ref{tab:error_prop}).\n    \\item Synthetic validation confirms that joint estimation reduces ability RMSE by 43.8\\% relative to sequential estimation ($p < 10^{-6}$), with Kendall rank correlation $\\tau = 0.922$ versus $\\tau = 0.859$ (Section~\\ref{sec:experiments}).\n\\end{enumerate}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0e8d4561-bf16-4805-8ac1-32ea9d531062",
  "isSidechain": false,
  "requestId": "req_011CbHfyrsfJFxxjQSjN9dvA",
  "type": "assistant",
  "uuid": "0109a7dd-5a4f-47b0-a563-7052e32b6606",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "a5cf6865-9f22-4f8b-931a-5ff939509219",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F7hmzxhsJHw6wt9qzx3u9P",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 566,
      "cache_read_input_tokens": 43747,
      "output_tokens": 20105,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 566,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 20105,
          "cache_read_input_tokens": 43747,
          "cache_creation_input_tokens": 566,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 566
          },
          "type": "message"
        }
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

_source line 40 · 2026-05-22T13:23:31.660Z_

<details><summary>↩ Tool result · `toolu_01KAYLZRDNtp4KJgFKsboiJq`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/introduction.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0109a7dd-5a4f-47b0-a563-7052e32b6606",
  "isSidechain": false,
  "promptId": "a692d8ae-00f1-4be4-9d9f-36a1874f2428",
  "type": "user",
  "uuid": "7afb5c44-255b-4ccc-8c85-dace01955f6d",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/introduction.tex",
    "content": "\\section{Introduction}\n\\label{sec:introduction}\n\nLarge Language Model (LLM) evaluation increasingly relies on LLM-as-a-judge protocols, where one or more LLM judges score model responses on structured benchmarks \\citep{zheng2023mtbench}. Two well-documented sources of distortion affect these evaluations: \\emph{judge bias}, where different judges assign systematically different scores to the same response, and \\emph{benchmark contamination}, where models achieve inflated scores on items encountered during training. Both problems have received sustained research attention, producing separate toolkits for bias calibration and contamination detection. These toolkits treat the two distortions as independent phenomena, a separation that reflects their origins in different research communities rather than any principled argument for independence. Accurate ability ranking is essential for model selection, safety evaluation, and benchmark design; systematic distortion in estimated abilities undermines all three. Yet a practitioner who needs both corrections must apply them sequentially: first correct one source of distortion, then the other. This sequential approach produces unreliable ability estimates. In synthetic experiments with 50 models, 100 items, and 8 judges, sequential estimation yields ability root mean squared error (RMSE) of $0.221 \\pm 0.038$, while joint estimation achieves $0.124 \\pm 0.016$, a 43.8\\% reduction (Wilcoxon $p < 10^{-6}$). The gap does not arise from estimation noise or algorithmic limitations of individual methods; it reflects structural confounding between judge bias and contamination that no sequential pipeline can resolve.\n\nExisting judge bias correction methods remove systematic differences across judges without modeling contamination. CyclicJudge \\citep{cyclicjudge2026} uses round-robin pairing to cancel average bias through balanced exposure of model pairs to all judges, but treats all residual score variation as genuine ability signal. UDA \\citep{uda2026} learns a neural K-factor adjustment that reduces inter-judge standard deviation by 63.4\\%, yet operates as a black-box transformation with no mechanism for contamination effects. On the contamination side, ConStat \\citep{constat2024} compares target model performance against a reference model to estimate item-level contamination ($r^2 = 0.94$ with true contamination levels in controlled settings), DCR \\citep{dcr2025} applies fuzzy inference to adjust scores on suspected leaked items, and LogProber \\citep{logprober2024} probes token-level log-probabilities to detect memorization signatures. These two families of methods operate in separate silos. A bias-first pipeline absorbs contamination-induced score inflation into the ability estimates, because the bias model attributes all residual systematic variation to genuine ability differences. A contamination-first pipeline misattributes judge severity differences as contamination signals, because score elevation from a lenient judge is indistinguishable from score elevation due to memorization without a joint model. In either ordering, the first correction stage produces estimates already distorted by the unmodeled facet, and the second stage inherits this distortion with no mechanism for self-correction.\n\nWe formalize this confounding as an omitted variable bias (OVB) problem \\citep{angrist2009mostly}. Within the Many-Facet Rasch Model (MFRM) framework \\citep{linacre1989mfrm}, the complete data-generating process includes both judge severity $d_j$ and a contamination interaction $c_n \\cdot e_i$. Fitting a specification that includes one facet but omits the other produces asymptotically biased parameter estimates whenever the two facets are non-orthogonal. This non-orthogonality holds in practice: lenient judges (low severity $d_j$) amplify score inflation on exposed items, while strict judges compress it, creating systematic dependence between judge effects and contamination effects. The OVB framework predicts that the bias magnitude scales with the contamination susceptibility $c_n$ of each model, so the most contaminated models receive the largest upward distortion in estimated ability. For practical benchmark evaluations, this means that the more a model's training data overlaps with the benchmark, the more its ability is overestimated, precisely the failure mode that contamination correction is designed to prevent. Synthetic validation confirms the predicted pattern: the Pearson correlation between sequential estimation bias and true $c_n$ reaches $r = 0.86$ ($p < 0.001$), which shows that contaminated models are systematically overestimated under both sequential orderings (Section~\\ref{sec:confounding}).\n\nWe propose the Gated Many-Facet Rasch Model (G-MFRM), which combines the multi-facet structure of MFRM \\citep{linacre1989mfrm, wang2025mfrm_llm} with the gating mechanism of Doubly-Gated Item Response Theory (DG-IRT) \\citep{shu2013dgirt} to jointly estimate model ability, judge severity, and contamination susceptibility in a single measurement framework. G-MFRM extends the MFRM linear predictor with a multiplicative contamination gating term $c_n \\cdot e_i$, where $c_n \\geq 0$ captures model-specific contamination susceptibility and $e_i \\in [0,1]$ quantifies per-item exposure. When $c_n = 0$ or $e_i = 0$, the gating term vanishes and the model reduces to standard MFRM, so uncontaminated model-item pairs incur no distortion. Because the bilinear product $c_n \\cdot e_i$ cannot be uniquely decomposed from response data alone, G-MFRM employs a three-stage calibration procedure: (1) standard MFRM warm-start to obtain initial parameter estimates, (2) external per-item exposure estimation from evidence independent of the response data, and (3) joint Markov chain Monte Carlo (MCMC) sampling with $e_i$ fixed from Stage~2. We provide a complete identifiability analysis (seven propositions and one theorem) that proves fixing $e_i$ externally is both necessary and sufficient for parameter separation under standard multi-judge designs (Section~\\ref{sec:method}). A complementary error propagation analysis bounds the impact of Stage~2 measurement noise: when exposure estimation error satisfies $\\sigma \\leq 0.2$, ability RMSE degradation remains below 6\\%. Figure~\\ref{fig:framework} provides an overview of the complete framework.\n\nOur contributions are as follows:\n\\begin{enumerate}\n    \\item We formalize the confounding between judge bias and benchmark contamination in LLM evaluation as an omitted variable bias problem, and show that sequential correction produces directional bias proportional to model contamination levels (Section~\\ref{sec:confounding}, Figure~\\ref{fig:ovb_bias}).\n    \\item We propose the G-MFRM framework with formal identifiability guarantees (seven propositions and one theorem) and quantified error propagation bounds for the staged estimation procedure (Section~\\ref{sec:method}, Figure~\\ref{fig:error_prop}, Table~\\ref{tab:error_prop}).\n    \\item Synthetic validation confirms that joint estimation reduces ability RMSE by 43.8\\% relative to sequential estimation ($p < 10^{-6}$), with Kendall rank correlation $\\tau = 0.922$ versus $\\tau = 0.859$ (Section~\\ref{sec:experiments}).\n\\end{enumerate}\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "0109a7dd-5a4f-47b0-a563-7052e32b6606",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "a5cf6865-9f22-4f8b-931a-5ff939509219",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 41_

```json
{
  "type": "last-prompt",
  "leafUuid": "7afb5c44-255b-4ccc-8c85-dace01955f6d",
  "sessionId": "a5cf6865-9f22-4f8b-931a-5ff939509219"
}
```

---

### Runtime record

_source line 42_

```json
{
  "type": "ai-title",
  "aiTitle": "Write G-MFRM paper Introduction section",
  "sessionId": "a5cf6865-9f22-4f8b-931a-5ff939509219"
}
```

---

### Assistant

_source line 43 · 2026-05-22T13:23:46.101Z_

文件已写入。5 段结构，约 1060 词：

- **P1 Hook**: 两个矫正孤岛 → sequential RMSE 比 joint 高 43.8% 的定量冲击
- **P2 Gap**: CyclicJudge/UDA/ConStat/DCR/LogProber 各自局限 → bias-first 和 contamination-first 都失败的结构性原因
- **P3 Insight**: OVB 形式化，非正交条件，r=0.86 合成验证
- **P4 Mechanism**: G-MFRM = MFRM + DG-IRT gating，三阶段校准，identifiability (7 propositions + 1 theorem)，error propagation (σ≤0.2 → <6%)，引用 Figure 1
- **P5 Contributions**: 3 条，每条有 Section/Figure/Table 支撑

所有 10 个 citation key 已使用，无 em-dash/en-dash，无 -ing 短语结尾，无黑名单词汇。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7afb5c44-255b-4ccc-8c85-dace01955f6d",
  "isSidechain": false,
  "requestId": "req_011CbHgP9sztbWSPdf2e1ekF",
  "type": "assistant",
  "uuid": "74ccb09d-e581-46d8-bd76-ad2eb7180229",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "a5cf6865-9f22-4f8b-931a-5ff939509219",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CSwi6D3DxiSHePc6hpBLf4",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 20129,
      "cache_read_input_tokens": 44313,
      "output_tokens": 298,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 20129,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 298,
          "cache_read_input_tokens": 44313,
          "cache_creation_input_tokens": 20129,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 20129
          },
          "type": "message"
        }
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

_source line 44_

```json
{
  "type": "last-prompt",
  "leafUuid": "74ccb09d-e581-46d8-bd76-ad2eb7180229",
  "sessionId": "a5cf6865-9f22-4f8b-931a-5ff939509219"
}
```

---

### Runtime record

_source line 45_

```json
{
  "type": "ai-title",
  "aiTitle": "Write G-MFRM paper Introduction section",
  "sessionId": "a5cf6865-9f22-4f8b-931a-5ff939509219"
}
```

---
