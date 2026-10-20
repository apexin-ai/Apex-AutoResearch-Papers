# Research conversation: <project_context> # 项目: simgate-modular-routing ## 运行环境 - 服务器名: westb-13313 - SSH 账户: root（调用 ssh_execute / submit_train

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 35
- **Recorded user turns:** 1
- **Tool calls:** 7
- **Original source:** `logs/chats/exported-trajectories/account-1/e7d68ec2-6069-4d98-9ec3-cf89b610a4f6.jsonl`
- **Structured JSON:** [`659fe76ceffd7ecaf745.json`](../../sessions/65/659fe76ceffd7ecaf745.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-14T02:06:46.103Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-14T02:06:46.103Z",
  "sessionId": "e7d68ec2-6069-4d98-9ec3-cf89b610a4f6",
  "content": "&lt;project_context>\n# 项目: simgate-modular-routing\n\n## 运行环境\n- 服务器名: westb-13313\n- SSH 账户: root（调用 ssh_execute / submit_training_job 时传入 account=\"root\"）\n- SSH 连接命令: ssh connect.westb.seetacloud.com  # 必须用此命令，~/.ssh/config 自动应用密钥和跳板机，禁止用裸 IP\n- 项目代码根目录: /root/autodl-tmp/simgate-modular-routing\n\n\n## 环境搭建\n连接服务器后先调 `detect_image` 检测是否为预置镜像。如果匹配，跳过基础环境搭建，只装项目特有依赖。已预装的包不要重复安装。\n\n## 输出风格\n回复简洁直接。只输出执行结果和必要信息，不要解释过程、不要客套、不要给未被要求的建议。\n&lt;/project_context>\n你是 ML 论文写作 Worker。任务：撰写 EMNLP 2026 短论文（4 页）的 Method 章节初稿。\n\n## 写作前必读\n\n先 Read 以下技能文件获取写作规范：\n- `/home/ubuntu/agent-ml-research/skills/global/latex-paper.skill.md`\n\n## 目标产出\n\n在本地路径写一个文件：\n`/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/_project/paper/method_draft.md`\n\n内容为纯 LaTeX（\\section{Method} 开头），约 1.0 页篇幅（~800-900 words）。\n\n## 章节结构要求（Director 指令）\n\n用 4 个 \\subsection 组织：\n\n### 3.1 Counterfactual Episode Collection\n- 对每个 task type，在相同 task instance（same seed）下运行两个完整 episode：\n  - **Pure-internal**：所有 step 使用 LLM internal reasoning（ReAct 范式）\n  - **Pure-deterministic**：所有 step 使用 deterministic external computation（environment simulator）\n- 产出：每个 episode 的 (score_internal, score_deterministic, death_internal, death_deterministic) 四元组\n- 关键设计决策：episode-level 而非 step-level，因为 per-step oracle 在 sparse-reward 下退化为 98% ties（Introduction 已论述）\n- LLM backbone: Qwen2.5-7B-Instruct（通过 vLLM 推理）\n- ScienceWorld 环境：30 个 task types，每 task 多 episodes（prescreening 5 ep + full collection 20 ep）\n- Max steps per episode: 30\n\n### 3.2 Death-Aware Labeling\n- Episode-level routing label 基于四元组分配，四种 signal 类型：\n  1. **death_asymmetry**：一方死亡另一方存活 → 存活方 preferred（最强 signal）\n  2. **tied_alive**：双方存活且分数差 ≤ 阈值 → no_preference\n  3. **both_dead**：双方均死亡 → no_preference（无有效 routing signal）\n  4. **score_comparison**：双方存活但分数差 > 阈值 → 高分方 preferred\n- Label distribution（30 tasks, 249 episodes）: det_preferred 41%, internal_preferred 0.5%, no_preference 59%\n- 关键观察：death_asymmetry 贡献了绝大多数 det_preferred labels\n\n### 3.3 Death Avoidance Factor (DAF)\n- DAF 定义：量化 death avoidance 在 routing signal 中的占比\n- 公式：DAF = 1 - (Δ_no_death / Δ_full)\n  - Δ_full = mean(score_det) - mean(score_int)（全部 episodes）\n  - Δ_no_death = mean(score_det | no_death) - mean(score_int | no_death)（仅非死亡 episodes）\n- DAF = 1 表示 routing signal 完全来自 death avoidance\n- DAF = 0 表示 routing signal 完全来自非死亡性能差异\n- 当前数据：DAF = 0.99（Δ_full = +37.9, Δ_no_death = +0.2）\n- Per-task DAF 变异：25/30 tasks DAF ≥ 95%，少数 tasks（如 measure-melting-point-unknown, DAF=0.594）显示 genuine non-death advantage\n- 统计验证：Pearson r = 0.989 (p < 0.0001) between per-task death rate differential and Δ(det-int)\n\n### 3.4 Rule-Based Baseline\n- 设计动机：测试简单 keyword heuristic 能否替代 learned routing\n- 三版 keyword list：\n  - v1（20 generic verbs incl. connect/move）→ 85.8% match rate ≈ always-deterministic（退化）\n  - v2（17 science-only: heat/boil/melt/freeze）→ 4.9% match rate ≈ always-internal（退化）\n  - v3（12 state-change verbs）→ 2.8% match rate ≈ always-internal（退化）\n- 结论：ScienceWorld actions 使用 generic interaction verbs（connect/move/pick up），非 science-specific keywords，任何 keyword list 都无法提供 meaningful routing signal\n- 定位：structural failure analysis，支持 learned/observation-based routing 的必要性\n\n## 核心数据（来自 registry，Truth Source）\n\n- plan-012-decomposition: Δ_full=37.9, Δ_no_death=0.2, DAF=0.99, r=0.989, p<0.0001, 30 tasks, 249 episodes, label_dist: det 41% / int 0.5% / no-pref 59%\n- plan-011-rule-based: v1 85.8%, v2 4.9%, v3 2.8%（均退化）\n\n注意：这些是中间分析数据。在最终数据可能微调的位置标注 [PLACEHOLDER]。\n\n## 已有章节（保持一致性）\n\nIntroduction (v2) 已完成，关键术语/notation 必须一致：\n- \"episode-level counterfactual analysis\"\n- \"death decomposition\"\n- Δ_full, Δ_no_death 符号\n- DAF (death avoidance fraction)\n- \"oracle degeneracy\"（Introduction 用词）\n- ReAct \\cite{react-2023} 作为 internal reasoning baseline\n\nRelated Work (v2) 已完成，引用 keys：\n- toolformer-2024, art-2023, chameleon-2024, retool-2026\n- cogrouter-2026, ares-2026, mixture-of-recursions-2025\n- itp-2026, dynathink-2025\n- react-2023\n\n## 写作红线\n\n1. **Claim-Evidence**: 每个定量声明必须有 registry 数据支撑\n2. **强度词限制**: 单 benchmark → 禁用 \"consistently outperforms\" / \"state-of-the-art\"\n3. **引用防幻觉**: 只使用上面列出的 cite keys + ScienceWorld 的引用 \\cite{scienceworld-2022}（如需要可标 [CITATION NEEDED]）\n4. **数字精度**: 与 registry 完全一致\n5. **PLACEHOLDER 标注**: 最终数据可能更新的数字用 [PLACEHOLDER: 当前值] 格式\n6. **不重复 Introduction 已有论述**: Introduction 已论述了 oracle degeneracy 的 motivation，Method 只需简要回指（\"as motivated in §1\"），不要重新论述\n\n## 风格\n\n- EMNLP 短论文风格：紧凑、精确\n- 用 \\cite{key} 格式引用\n- DAF 公式用 \\begin{equation} 编号\n- 不加章节编号（短论文惯例，但 subsection 用 \\subsection）\n- 算法伪代码不需要（篇幅限制），用文字描述流程"
}
```

---

### Runtime record

_source line 2 · 2026-05-14T02:06:46.107Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-14T02:06:46.107Z",
  "sessionId": "e7d68ec2-6069-4d98-9ec3-cf89b610a4f6"
}
```

---

## Round 1

33 recorded events

### User

_source line 3 · 2026-05-14T02:06:46.147Z_

&lt;project_context>
# 项目: simgate-modular-routing

## 运行环境
- 服务器名: westb-13313
- SSH 账户: root（调用 ssh_execute / submit_training_job 时传入 account="root"）
- SSH 连接命令: ssh connect.westb.seetacloud.com  # 必须用此命令，~/.ssh/config 自动应用密钥和跳板机，禁止用裸 IP
- 项目代码根目录: /root/autodl-tmp/simgate-modular-routing


## 环境搭建
连接服务器后先调 `detect_image` 检测是否为预置镜像。如果匹配，跳过基础环境搭建，只装项目特有依赖。已预装的包不要重复安装。

## 输出风格
回复简洁直接。只输出执行结果和必要信息，不要解释过程、不要客套、不要给未被要求的建议。
&lt;/project_context>
你是 ML 论文写作 Worker。任务：撰写 EMNLP 2026 短论文（4 页）的 Method 章节初稿。

## 写作前必读

先 Read 以下技能文件获取写作规范：
- `/home/ubuntu/agent-ml-research/skills/global/latex-paper.skill.md`

## 目标产出

在本地路径写一个文件：
`/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/_project/paper/method_draft.md`

内容为纯 LaTeX（\section{Method} 开头），约 1.0 页篇幅（~800-900 words）。

## 章节结构要求（Director 指令）

用 4 个 \subsection 组织：

### 3.1 Counterfactual Episode Collection
- 对每个 task type，在相同 task instance（same seed）下运行两个完整 episode：
  - **Pure-internal**：所有 step 使用 LLM internal reasoning（ReAct 范式）
  - **Pure-deterministic**：所有 step 使用 deterministic external computation（environment simulator）
- 产出：每个 episode 的 (score_internal, score_deterministic, death_internal, death_deterministic) 四元组
- 关键设计决策：episode-level 而非 step-level，因为 per-step oracle 在 sparse-reward 下退化为 98% ties（Introduction 已论述）
- LLM backbone: Qwen2.5-7B-Instruct（通过 vLLM 推理）
- ScienceWorld 环境：30 个 task types，每 task 多 episodes（prescreening 5 ep + full collection 20 ep）
- Max steps per episode: 30

### 3.2 Death-Aware Labeling
- Episode-level routing label 基于四元组分配，四种 signal 类型：
  1. **death_asymmetry**：一方死亡另一方存活 → 存活方 preferred（最强 signal）
  2. **tied_alive**：双方存活且分数差 ≤ 阈值 → no_preference
  3. **both_dead**：双方均死亡 → no_preference（无有效 routing signal）
  4. **score_comparison**：双方存活但分数差 > 阈值 → 高分方 preferred
- Label distribution（30 tasks, 249 episodes）: det_preferred 41%, internal_preferred 0.5%, no_preference 59%
- 关键观察：death_asymmetry 贡献了绝大多数 det_preferred labels

### 3.3 Death Avoidance Factor (DAF)
- DAF 定义：量化 death avoidance 在 routing signal 中的占比
- 公式：DAF = 1 - (Δ_no_death / Δ_full)
  - Δ_full = mean(score_det) - mean(score_int)（全部 episodes）
  - Δ_no_death = mean(score_det | no_death) - mean(score_int | no_death)（仅非死亡 episodes）
- DAF = 1 表示 routing signal 完全来自 death avoidance
- DAF = 0 表示 routing signal 完全来自非死亡性能差异
- 当前数据：DAF = 0.99（Δ_full = +37.9, Δ_no_death = +0.2）
- Per-task DAF 变异：25/30 tasks DAF ≥ 95%，少数 tasks（如 measure-melting-point-unknown, DAF=0.594）显示 genuine non-death advantage
- 统计验证：Pearson r = 0.989 (p < 0.0001) between per-task death rate differential and Δ(det-int)

### 3.4 Rule-Based Baseline
- 设计动机：测试简单 keyword heuristic 能否替代 learned routing
- 三版 keyword list：
  - v1（20 generic verbs incl. connect/move）→ 85.8% match rate ≈ always-deterministic（退化）
  - v2（17 science-only: heat/boil/melt/freeze）→ 4.9% match rate ≈ always-internal（退化）
  - v3（12 state-change verbs）→ 2.8% match rate ≈ always-internal（退化）
- 结论：ScienceWorld actions 使用 generic interaction verbs（connect/move/pick up），非 science-specific keywords，任何 keyword list 都无法提供 meaningful routing signal
- 定位：structural failure analysis，支持 learned/observation-based routing 的必要性

## 核心数据（来自 registry，Truth Source）

- plan-012-decomposition: Δ_full=37.9, Δ_no_death=0.2, DAF=0.99, r=0.989, p<0.0001, 30 tasks, 249 episodes, label_dist: det 41% / int 0.5% / no-pref 59%
- plan-011-rule-based: v1 85.8%, v2 4.9%, v3 2.8%（均退化）

注意：这些是中间分析数据。在最终数据可能微调的位置标注 [PLACEHOLDER]。

## 已有章节（保持一致性）

Introduction (v2) 已完成，关键术语/notation 必须一致：
- "episode-level counterfactual analysis"
- "death decomposition"
- Δ_full, Δ_no_death 符号
- DAF (death avoidance fraction)
- "oracle degeneracy"（Introduction 用词）
- ReAct \cite{react-2023} 作为 internal reasoning baseline

Related Work (v2) 已完成，引用 keys：
- toolformer-2024, art-2023, chameleon-2024, retool-2026
- cogrouter-2026, ares-2026, mixture-of-recursions-2025
- itp-2026, dynathink-2025
- react-2023

## 写作红线

1. **Claim-Evidence**: 每个定量声明必须有 registry 数据支撑
2. **强度词限制**: 单 benchmark → 禁用 "consistently outperforms" / "state-of-the-art"
3. **引用防幻觉**: 只使用上面列出的 cite keys + ScienceWorld 的引用 \cite{scienceworld-2022}（如需要可标 [CITATION NEEDED]）
4. **数字精度**: 与 registry 完全一致
5. **PLACEHOLDER 标注**: 最终数据可能更新的数字用 [PLACEHOLDER: 当前值] 格式
6. **不重复 Introduction 已有论述**: Introduction 已论述了 oracle degeneracy 的 motivation，Method 只需简要回指（"as motivated in §1"），不要重新论述

## 风格

- EMNLP 短论文风格：紧凑、精确
- 用 \cite{key} 格式引用
- DAF 公式用 \begin{equation} 编号
- 不加章节编号（短论文惯例，但 subsection 用 \subsection）
- 算法伪代码不需要（篇幅限制），用文字描述流程

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "db5f24fc-919c-42ca-bee6-b8b77a4c500d",
  "type": "user",
  "uuid": "5d815c2c-d4fc-48fc-98bd-5b5a914e2688",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "e7d68ec2-6069-4d98-9ec3-cf89b610a4f6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-14T02:06:46.146Z_

```json
{
  "parentUuid": "5d815c2c-d4fc-48fc-98bd-5b5a914e2688",
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
  "uuid": "8187fe62-dab2-47f0-b774-7736707d1c6e",
  "timestamp": "2026-05-14T02:06:46.146Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "e7d68ec2-6069-4d98-9ec3-cf89b610a4f6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-14T02:06:46.146Z_

```json
{
  "parentUuid": "8187fe62-dab2-47f0-b774-7736707d1c6e",
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
  "uuid": "59c1a7a5-b7c4-4974-8457-7dc00201e739",
  "timestamp": "2026-05-14T02:06:46.146Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "e7d68ec2-6069-4d98-9ec3-cf89b610a4f6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6 · 2026-05-14T02:06:46.146Z_

```json
{
  "parentUuid": "59c1a7a5-b7c4-4974-8457-7dc00201e739",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "4ec39db2-d475-450c-81e8-32b3c556ff48",
  "timestamp": "2026-05-14T02:06:46.146Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "e7d68ec2-6069-4d98-9ec3-cf89b610a4f6",
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
  "aiTitle": "Write Method section for EMNLP short paper",
  "sessionId": "e7d68ec2-6069-4d98-9ec3-cf89b610a4f6"
}
```

---

### Assistant

_source line 8 · 2026-05-14T02:06:56.263Z_

I'll start by reading the latex-paper skill file and checking existing project files for context.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4ec39db2-d475-450c-81e8-32b3c556ff48",
  "isSidechain": false,
  "requestId": "req_011Cb1eJd2hpaFgnkuTtFBay",
  "type": "assistant",
  "uuid": "8c2f1f71-07b2-4983-837d-a6587e5915ea",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "e7d68ec2-6069-4d98-9ec3-cf89b610a4f6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TRs1NXxskThUd2XKZpr1kU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13200,
      "cache_read_input_tokens": 11841,
      "output_tokens": 172,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13200,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 172,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 13200,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13200
          },
          "type": "message"
        }
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

_source line 9 · 2026-05-14T02:06:56.266Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Ux7FtgJKKxjR4JEbaTXhxn`</summary>

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
  "parentUuid": "8c2f1f71-07b2-4983-837d-a6587e5915ea",
  "isSidechain": false,
  "requestId": "req_011Cb1eJd2hpaFgnkuTtFBay",
  "type": "assistant",
  "uuid": "3b907220-164f-47c7-9353-f0ea4e590980",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "e7d68ec2-6069-4d98-9ec3-cf89b610a4f6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TRs1NXxskThUd2XKZpr1kU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13200,
      "cache_read_input_tokens": 11841,
      "output_tokens": 172,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13200,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 172,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 13200,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13200
          },
          "type": "message"
        }
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

_source line 10 · 2026-05-14T02:06:56.289Z_

<details><summary>↩ Tool result · `toolu_01Ux7FtgJKKxjR4JEbaTXhxn`</summary>

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
  "parentUuid": "3b907220-164f-47c7-9353-f0ea4e590980",
  "isSidechain": false,
  "promptId": "db5f24fc-919c-42ca-bee6-b8b77a4c500d",
  "type": "user",
  "uuid": "83ec4df1-bead-4bfe-adee-29ac4addada6",
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
  "sourceToolAssistantUUID": "3b907220-164f-47c7-9353-f0ea4e590980",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "e7d68ec2-6069-4d98-9ec3-cf89b610a4f6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
````

</details>

---

### Tool result

_source line 11 · 2026-05-14T02:06:56.595Z_

<details><summary>↩ Tool result · `toolu_019xkg9RA37k6gbAFvkXeNSg`</summary>

```text
experiment_tables.md
introduction_draft.md
introduction_draft_d860d5.md
related_work_draft.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "616a5135-b7ea-4d06-a891-0fbfc6a23c58",
  "isSidechain": false,
  "promptId": "db5f24fc-919c-42ca-bee6-b8b77a4c500d",
  "type": "user",
  "uuid": "e0f74644-8c1c-4608-89d6-44e43300472b",
  "toolUseResult": {
    "stdout": "experiment_tables.md\nintroduction_draft.md\nintroduction_draft_d860d5.md\nrelated_work_draft.md",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "616a5135-b7ea-4d06-a891-0fbfc6a23c58",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "e7d68ec2-6069-4d98-9ec3-cf89b610a4f6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-14T02:06:56.419Z_

<details open><summary>🔧 Tool call — Bash · `toolu_019xkg9RA37k6gbAFvkXeNSg`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/_project/paper/ 2>/dev/null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "83ec4df1-bead-4bfe-adee-29ac4addada6",
  "isSidechain": false,
  "requestId": "req_011Cb1eJd2hpaFgnkuTtFBay",
  "type": "assistant",
  "uuid": "616a5135-b7ea-4d06-a891-0fbfc6a23c58",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "e7d68ec2-6069-4d98-9ec3-cf89b610a4f6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TRs1NXxskThUd2XKZpr1kU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13200,
      "cache_read_input_tokens": 11841,
      "output_tokens": 172,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13200,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 172,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 13200,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13200
          },
          "type": "message"
        }
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

_source line 13_

```json
{
  "type": "last-prompt",
  "leafUuid": "e0f74644-8c1c-4608-89d6-44e43300472b",
  "sessionId": "e7d68ec2-6069-4d98-9ec3-cf89b610a4f6"
}
```

---

### Runtime record

_source line 14_

```json
{
  "type": "ai-title",
  "aiTitle": "Write Method section for EMNLP short paper",
  "sessionId": "e7d68ec2-6069-4d98-9ec3-cf89b610a4f6"
}
```

---

### Assistant

_source line 15 · 2026-05-14T02:06:59.977Z_

<details><summary>Logged reasoning block</summary>

```text
Let me read the existing Introduction and Related Work drafts to ensure consistency in terminology and notation.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e0f74644-8c1c-4608-89d6-44e43300472b",
  "isSidechain": false,
  "requestId": "req_011Cb1eKQB5FLC9FmKeN7avM",
  "type": "assistant",
  "uuid": "88a68bda-acaa-48c3-989b-646c13cff874",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "e7d68ec2-6069-4d98-9ec3-cf89b610a4f6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VuNVdSQEsYWz9aUUzSaYVY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5692,
      "cache_read_input_tokens": 25041,
      "output_tokens": 220,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5692,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 220,
          "cache_read_input_tokens": 25041,
          "cache_creation_input_tokens": 5692,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5692
          },
          "type": "message"
        }
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

_source line 16 · 2026-05-14T02:07:00.440Z_

Let me read the existing Introduction and Related Work drafts for consistency.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "88a68bda-acaa-48c3-989b-646c13cff874",
  "isSidechain": false,
  "requestId": "req_011Cb1eKQB5FLC9FmKeN7avM",
  "type": "assistant",
  "uuid": "54fdf271-78a0-4883-8d0f-6a26127d42b8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "e7d68ec2-6069-4d98-9ec3-cf89b610a4f6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VuNVdSQEsYWz9aUUzSaYVY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5692,
      "cache_read_input_tokens": 25041,
      "output_tokens": 220,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5692,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 220,
          "cache_read_input_tokens": 25041,
          "cache_creation_input_tokens": 5692,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5692
          },
          "type": "message"
        }
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

_source line 17 · 2026-05-14T02:07:02.766Z_

<details open><summary>🔧 Tool call — Read · `toolu_01YQr1SGpknH1jpqsmfPTM9t`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/_project/paper/introduction_draft.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "54fdf271-78a0-4883-8d0f-6a26127d42b8",
  "isSidechain": false,
  "requestId": "req_011Cb1eKQB5FLC9FmKeN7avM",
  "type": "assistant",
  "uuid": "65088e8f-4643-4887-8c2a-4ddd18269a5d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "e7d68ec2-6069-4d98-9ec3-cf89b610a4f6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VuNVdSQEsYWz9aUUzSaYVY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5692,
      "cache_read_input_tokens": 25041,
      "output_tokens": 220,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5692,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 220,
          "cache_read_input_tokens": 25041,
          "cache_creation_input_tokens": 5692,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5692
          },
          "type": "message"
        }
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

_source line 18 · 2026-05-14T02:07:02.950Z_

<details><summary>↩ Tool result · `toolu_01Smop8fF9qvhdkk5o5vFGu7`</summary>

```text
1	# Related Work — Draft v1
2	
3	\section{Related Work}
4	
5	\paragraph{Tool-Use Learning.}
6	A line of work teaches LLMs when and how to invoke external tools.
7	Toolformer \cite{toolformer-2024} inserts API calls via self-supervised filtering, while ART \cite{art-2023} uses LLM reasoning chains to select tools automatically, and Chameleon \cite{chameleon-2024} composes diverse tool modules under LLM-as-planner orchestration.
8	More recently, ReTool \cite{retool-2026} applies reinforcement learning to learn implicit code-interpreter invocation strategies for mathematical reasoning.
9	Our work differs along three axes: (1) we generate routing labels via \emph{episode-level counterfactual analysis}---running complete trajectories under competing strategies---rather than self-supervised or RL-based signals; (2) we frame routing as \emph{catastrophic failure prevention} rather than general tool selection; and (3) we train an explicit lightweight router decoupled from the backbone LLM, enabling diagnostic analysis of what the routing signal encodes.
10	
11	\paragraph{Adaptive Computation.}
12	Several recent methods adapt reasoning effort per step.
13	CogRouter \cite{cogrouter-2026} achieves 82.3\% on ScienceWorld by routing among cognitive depth levels (instinct to strategic planning) via Cooperative Policy Optimization, while ARES \cite{ares-2026} trains a lightweight router to select per-step reasoning effort (low/medium/high), reducing token cost by 52.7\%.
14	Mixture-of-Recursions \cite{mixture-of-recursions-2025} applies adaptive depth at the architecture level via per-token recursive routing.
15	These methods route \emph{how much} to reason; we route \emph{which modality} to use (internal LLM reasoning vs.\ deterministic computation) and contribute the empirical finding that death avoidance accounts for ${\sim}99\%$ of the learned routing signal.
16	
17	\paragraph{World Model Routing.}
18	ITP \cite{itp-2026} augments agents with LLM-based world model lookahead, adaptively adjusting the simulation horizon based on task progress.
19	Dyna-Think \cite{dynathink-2025} integrates world model simulation into the reasoning loop, matching 685B-parameter performance with a 32B model at half the token cost.
20	Both route to \emph{approximate} world models that inherit LLM hallucination failures.
21	Our deterministic computation modality provides \emph{exact} state transitions, and our counterfactual analysis reveals that this exactness matters almost exclusively for death avoidance---non-death performance is near-equivalent between modalities.
22	
23	\paragraph{Agent Frameworks.}
24	ReAct \cite{react-2023} interleaves reasoning and acting in a single LLM call and serves as a foundational framework for interactive agents including our internal-reasoning baseline.
25	Our work complements ReAct by analyzing \emph{when} reasoning should yield to deterministic computation and finding that the answer is concentrated in catastrophic failure scenarios.
26	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "58f55167-52f5-4359-be8f-14e9cccdabb5",
  "isSidechain": false,
  "promptId": "db5f24fc-919c-42ca-bee6-b8b77a4c500d",
  "type": "user",
  "uuid": "6e28093f-c783-4c54-a6f1-70809d4d679b",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/_project/paper/related_work_draft.md",
      "content": "# Related Work — Draft v1\n\n\\section{Related Work}\n\n\\paragraph{Tool-Use Learning.}\nA line of work teaches LLMs when and how to invoke external tools.\nToolformer \\cite{toolformer-2024} inserts API calls via self-supervised filtering, while ART \\cite{art-2023} uses LLM reasoning chains to select tools automatically, and Chameleon \\cite{chameleon-2024} composes diverse tool modules under LLM-as-planner orchestration.\nMore recently, ReTool \\cite{retool-2026} applies reinforcement learning to learn implicit code-interpreter invocation strategies for mathematical reasoning.\nOur work differs along three axes: (1) we generate routing labels via \\emph{episode-level counterfactual analysis}---running complete trajectories under competing strategies---rather than self-supervised or RL-based signals; (2) we frame routing as \\emph{catastrophic failure prevention} rather than general tool selection; and (3) we train an explicit lightweight router decoupled from the backbone LLM, enabling diagnostic analysis of what the routing signal encodes.\n\n\\paragraph{Adaptive Computation.}\nSeveral recent methods adapt reasoning effort per step.\nCogRouter \\cite{cogrouter-2026} achieves 82.3\\% on ScienceWorld by routing among cognitive depth levels (instinct to strategic planning) via Cooperative Policy Optimization, while ARES \\cite{ares-2026} trains a lightweight router to select per-step reasoning effort (low/medium/high), reducing token cost by 52.7\\%.\nMixture-of-Recursions \\cite{mixture-of-recursions-2025} applies adaptive depth at the architecture level via per-token recursive routing.\nThese methods route \\emph{how much} to reason; we route \\emph{which modality} to use (internal LLM reasoning vs.\\ deterministic computation) and contribute the empirical finding that death avoidance accounts for ${\\sim}99\\%$ of the learned routing signal.\n\n\\paragraph{World Model Routing.}\nITP \\cite{itp-2026} augments agents with LLM-based world model lookahead, adaptively adjusting the simulation horizon based on task progress.\nDyna-Think \\cite{dynathink-2025} integrates world model simulation into the reasoning loop, matching 685B-parameter performance with a 32B model at half the token cost.\nBoth route to \\emph{approximate} world models that inherit LLM hallucination failures.\nOur deterministic computation modality provides \\emph{exact} state transitions, and our counterfactual analysis reveals that this exactness matters almost exclusively for death avoidance---non-death performance is near-equivalent between modalities.\n\n\\paragraph{Agent Frameworks.}\nReAct \\cite{react-2023} interleaves reasoning and acting in a single LLM call and serves as a foundational framework for interactive agents including our internal-reasoning baseline.\nOur work complements ReAct by analyzing \\emph{when} reasoning should yield to deterministic computation and finding that the answer is concentrated in catastrophic failure scenarios.\n",
      "numLines": 26,
      "startLine": 1,
      "totalLines": 26
    }
  },
  "sourceToolAssistantUUID": "58f55167-52f5-4359-be8f-14e9cccdabb5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "e7d68ec2-6069-4d98-9ec3-cf89b610a4f6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-14T02:07:02.772Z_

<details><summary>↩ Tool result · `toolu_01YQr1SGpknH1jpqsmfPTM9t`</summary>

```text
1	# Introduction — Draft v1
2	
3	\section{Introduction}
4	
5	When LLM agents interact with rule-governed environments---manipulating temperatures, mixing chemicals, navigating physical constraints---they face a failure mode qualitatively distinct from suboptimality: \emph{catastrophic death}. A single hallucinated state transition can trigger an irreversible termination penalty, collapsing the episode score to $-100$. Deterministic external computation---environment simulators or code interpreters---eliminates such hallucinations by providing exact state transitions. But what does a router actually learn when trained to select between internal LLM reasoning and deterministic computation? Recent work on tool-use learning \cite{toolformer-2024,art-2023,chameleon-2024,retool-2026} and adaptive computation \cite{cogrouter-2026,ares-2026,mixture-of-recursions-2025} has developed methods for deciding when and how to invoke external modules, yet these approaches frame routing as a general capability or efficiency question---selecting the right tool, calibrating reasoning depth---without examining whether \emph{failure avoidance} constitutes a distinct and potentially dominant routing signal.
6	
7	We address this question by analyzing routing between internal reasoning, following the ReAct interleaved reasoning-and-acting paradigm \cite{react-2023}, and deterministic computation on ScienceWorld, an interactive science environment with sparse rewards and catastrophic failure penalties. A natural first approach is per-step oracle comparison: at each decision point, run both modalities and prefer the one yielding higher immediate reward. However, in sparse-reward environments where non-zero reward arrives only at episode termination, this strategy degenerates. On ScienceWorld, per-step oracle labeling produces \textbf{[PLACEHOLDER: 98\%]} ties---neither modality shows a per-step advantage on the vast majority of steps---rendering the resulting labels uninformative for router training. This \emph{oracle degeneracy} motivates a shift from step-level to episode-level analysis.
8	
9	We introduce \emph{episode-level counterfactual analysis}: for each task instance, we run complete episodes under pure-internal and pure-deterministic strategies, then compare episode-level outcomes to generate routing labels. Across [PLACEHOLDER: 30] ScienceWorld task types ([PLACEHOLDER: 249] episodes), this methodology reveals a striking concentration of routing signal. The full performance gap between deterministic and internal-reasoning strategies is [PLACEHOLDER: $\Delta_{\text{full}} = +37.9$] points. When we exclude episodes where either strategy results in agent death and recompute the gap, it collapses to [PLACEHOLDER: $\Delta_{\text{no\_death}} = +0.2$]---effectively zero. Death avoidance accounts for [PLACEHOLDER: 99\%] of the routing signal (death avoidance fraction [PLACEHOLDER: 98.75\%]). The per-task correlation between death rate differential and performance gap is $r =$ [PLACEHOLDER: 0.989] ($p < 0.0001$). Episode-level label distribution confirms this asymmetry: [PLACEHOLDER: 41\%] of episodes prefer deterministic computation, only [PLACEHOLDER: 0.5\%] prefer internal reasoning, and [PLACEHOLDER: 59\%] show no preference. When agents do not die, both reasoning modalities perform approximately equally.
10	
11	Our contributions are:
12	\begin{itemize}
13	    \item We propose \textbf{episode-level counterfactual analysis} for routing label generation, overcoming the degeneracy of per-step oracle labeling in sparse-reward interactive environments (per-step tie rate of [PLACEHOLDER: 98\%] on ScienceWorld).
14	    \item We introduce a \textbf{death decomposition framework} that separates routing signal into death-avoidance and non-death components, quantifying how much routing value derives from catastrophic failure prevention versus positive task guidance.
15	    \item We provide \textbf{empirical evidence} across [PLACEHOLDER: 30] ScienceWorld task types that death avoidance accounts for [PLACEHOLDER: 99\%] of routing signal between internal LLM reasoning and deterministic computation, with non-death performance near-equivalent between modalities ([PLACEHOLDER: $\Delta_{\text{no\_death}} = +0.2$]).
16	\end{itemize}
17	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "65088e8f-4643-4887-8c2a-4ddd18269a5d",
  "isSidechain": false,
  "promptId": "db5f24fc-919c-42ca-bee6-b8b77a4c500d",
  "type": "user",
  "uuid": "78ec324e-abf7-4f30-aaef-4ef58eb86904",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/_project/paper/introduction_draft.md",
      "content": "# Introduction — Draft v1\n\n\\section{Introduction}\n\nWhen LLM agents interact with rule-governed environments---manipulating temperatures, mixing chemicals, navigating physical constraints---they face a failure mode qualitatively distinct from suboptimality: \\emph{catastrophic death}. A single hallucinated state transition can trigger an irreversible termination penalty, collapsing the episode score to $-100$. Deterministic external computation---environment simulators or code interpreters---eliminates such hallucinations by providing exact state transitions. But what does a router actually learn when trained to select between internal LLM reasoning and deterministic computation? Recent work on tool-use learning \\cite{toolformer-2024,art-2023,chameleon-2024,retool-2026} and adaptive computation \\cite{cogrouter-2026,ares-2026,mixture-of-recursions-2025} has developed methods for deciding when and how to invoke external modules, yet these approaches frame routing as a general capability or efficiency question---selecting the right tool, calibrating reasoning depth---without examining whether \\emph{failure avoidance} constitutes a distinct and potentially dominant routing signal.\n\nWe address this question by analyzing routing between internal reasoning, following the ReAct interleaved reasoning-and-acting paradigm \\cite{react-2023}, and deterministic computation on ScienceWorld, an interactive science environment with sparse rewards and catastrophic failure penalties. A natural first approach is per-step oracle comparison: at each decision point, run both modalities and prefer the one yielding higher immediate reward. However, in sparse-reward environments where non-zero reward arrives only at episode termination, this strategy degenerates. On ScienceWorld, per-step oracle labeling produces \\textbf{[PLACEHOLDER: 98\\%]} ties---neither modality shows a per-step advantage on the vast majority of steps---rendering the resulting labels uninformative for router training. This \\emph{oracle degeneracy} motivates a shift from step-level to episode-level analysis.\n\nWe introduce \\emph{episode-level counterfactual analysis}: for each task instance, we run complete episodes under pure-internal and pure-deterministic strategies, then compare episode-level outcomes to generate routing labels. Across [PLACEHOLDER: 30] ScienceWorld task types ([PLACEHOLDER: 249] episodes), this methodology reveals a striking concentration of routing signal. The full performance gap between deterministic and internal-reasoning strategies is [PLACEHOLDER: $\\Delta_{\\text{full}} = +37.9$] points. When we exclude episodes where either strategy results in agent death and recompute the gap, it collapses to [PLACEHOLDER: $\\Delta_{\\text{no\\_death}} = +0.2$]---effectively zero. Death avoidance accounts for [PLACEHOLDER: 99\\%] of the routing signal (death avoidance fraction [PLACEHOLDER: 98.75\\%]). The per-task correlation between death rate differential and performance gap is $r =$ [PLACEHOLDER: 0.989] ($p < 0.0001$). Episode-level label distribution confirms this asymmetry: [PLACEHOLDER: 41\\%] of episodes prefer deterministic computation, only [PLACEHOLDER: 0.5\\%] prefer internal reasoning, and [PLACEHOLDER: 59\\%] show no preference. When agents do not die, both reasoning modalities perform approximately equally.\n\nOur contributions are:\n\\begin{itemize}\n    \\item We propose \\textbf{episode-level counterfactual analysis} for routing label generation, overcoming the degeneracy of per-step oracle labeling in sparse-reward interactive environments (per-step tie rate of [PLACEHOLDER: 98\\%] on ScienceWorld).\n    \\item We introduce a \\textbf{death decomposition framework} that separates routing signal into death-avoidance and non-death components, quantifying how much routing value derives from catastrophic failure prevention versus positive task guidance.\n    \\item We provide \\textbf{empirical evidence} across [PLACEHOLDER: 30] ScienceWorld task types that death avoidance accounts for [PLACEHOLDER: 99\\%] of routing signal between internal LLM reasoning and deterministic computation, with non-death performance near-equivalent between modalities ([PLACEHOLDER: $\\Delta_{\\text{no\\_death}} = +0.2$]).\n\\end{itemize}\n",
      "numLines": 17,
      "startLine": 1,
      "totalLines": 17
    }
  },
  "sourceToolAssistantUUID": "65088e8f-4643-4887-8c2a-4ddd18269a5d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "e7d68ec2-6069-4d98-9ec3-cf89b610a4f6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-14T02:07:02.938Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Smop8fF9qvhdkk5o5vFGu7`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/_project/paper/related_work_draft.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "78ec324e-abf7-4f30-aaef-4ef58eb86904",
  "isSidechain": false,
  "requestId": "req_011Cb1eKQB5FLC9FmKeN7avM",
  "type": "assistant",
  "uuid": "58f55167-52f5-4359-be8f-14e9cccdabb5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "e7d68ec2-6069-4d98-9ec3-cf89b610a4f6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VuNVdSQEsYWz9aUUzSaYVY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5692,
      "cache_read_input_tokens": 25041,
      "output_tokens": 220,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5692,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 220,
          "cache_read_input_tokens": 25041,
          "cache_creation_input_tokens": 5692,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5692
          },
          "type": "message"
        }
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

_source line 21 · 2026-05-14T02:07:15.687Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a clear picture of the existing sections and their terminology. Let me also check the registry data for exact numbers.

Let me now write the Method section draft. I need to:
1. Use consistent terminology with Introduction and Related Work
2. Follow the 4 subsection structure specified
3. Use the exact numbers from the registry data
4. Mark placeholders where appropriate
5. Keep it around 800-900 words (~1 page)
6. Use EMNLP short paper style (compact, precise)

Key terms to maintain consistency:
- "episode-level counterfactual analysis"
- "death decomposition"


- Δ_full, Δ_no_death metrics
- DAF (death avoidance fraction)
- "oracle degeneracy"
- ReAct and ScienceWorld as baseline references
- Pure-internal and pure-deterministic strategy types

Now I'm drafting the Method section with these technical definitions and citations integrated throughout.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6e28093f-c783-4c54-a6f1-70809d4d679b",
  "isSidechain": false,
  "requestId": "req_011Cb1eKs55wVACuYbvhzpXy",
  "type": "assistant",
  "uuid": "51c0edce-3671-4374-a810-0e394480b184",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "e7d68ec2-6069-4d98-9ec3-cf89b610a4f6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NB6oQdHcNJGe4ZoDLQS3JA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2086,
      "cache_read_input_tokens": 30733,
      "output_tokens": 2135,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2086,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2135,
          "cache_read_input_tokens": 30733,
          "cache_creation_input_tokens": 2086,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2086
          },
          "type": "message"
        }
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

_source line 22 · 2026-05-14T02:07:15.698Z_

Now I have all the context needed. Let me write the Method section.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "51c0edce-3671-4374-a810-0e394480b184",
  "isSidechain": false,
  "requestId": "req_011Cb1eKs55wVACuYbvhzpXy",
  "type": "assistant",
  "uuid": "451a473c-4927-4c85-a2e0-6b9872ff01c6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "e7d68ec2-6069-4d98-9ec3-cf89b610a4f6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NB6oQdHcNJGe4ZoDLQS3JA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2086,
      "cache_read_input_tokens": 30733,
      "output_tokens": 2135,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2086,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2135,
          "cache_read_input_tokens": 30733,
          "cache_creation_input_tokens": 2086,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2086
          },
          "type": "message"
        }
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

_source line 23 · 2026-05-14T02:07:50.151Z_

<details open><summary>🔧 Tool call — Write · `toolu_01UQhLR4NyXKw89WCJUxQVgQ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/_project/paper/method_draft.md",
  "content": "# Method — Draft v1\n\n\\section{Method}\n\nWe describe our methodology in four parts: counterfactual episode collection (\\S\\ref{sec:collection}), death-aware labeling (\\S\\ref{sec:labeling}), the death avoidance factor (\\S\\ref{sec:daf}), and a rule-based baseline analysis (\\S\\ref{sec:rule}).\n\n\\subsection{Counterfactual Episode Collection}\n\\label{sec:collection}\n\nAs motivated in \\S1, per-step oracle labeling degenerates under sparse rewards. We instead adopt \\emph{episode-level counterfactual analysis}: for each task instance, we run two complete episodes under identical initial conditions (same random seed):\n\n\\begin{itemize}\n    \\item \\textbf{Pure-internal}: all steps use the LLM's internal reasoning following the ReAct paradigm \\cite{react-2023}, where the agent interleaves chain-of-thought reasoning with environment actions.\n    \\item \\textbf{Pure-deterministic}: all steps use deterministic external computation via the environment simulator, providing exact state transitions.\n\\end{itemize}\n\nEach episode produces a tuple $(s^{\\text{int}}, s^{\\text{det}}, d^{\\text{int}}, d^{\\text{det}})$, where $s$ denotes episode score and $d \\in \\{0, 1\\}$ indicates whether the agent died. Episodes are capped at [PLACEHOLDER: 30] steps. We use Qwen2.5-7B-Instruct as the LLM backbone, served via vLLM.\n\nWe evaluate on ScienceWorld \\cite{scienceworld-2022}, which provides [PLACEHOLDER: 30] task types spanning physical and chemical reasoning. For each task type, we first run a prescreening phase (5 episodes) to identify tasks where both strategies can be meaningfully compared, then collect the full dataset of [PLACEHOLDER: 20] episodes per task. The final dataset comprises [PLACEHOLDER: 249] episodes across all [PLACEHOLDER: 30] task types.\n\n\\subsection{Death-Aware Labeling}\n\\label{sec:labeling}\n\nWe assign an episode-level routing label to each counterfactual pair based on the four-tuple $(s^{\\text{int}}, s^{\\text{det}}, d^{\\text{int}}, d^{\\text{det}})$, distinguishing four signal types ordered by priority:\n\n\\begin{enumerate}\n    \\item \\textbf{Death asymmetry}: one strategy results in agent death while the other survives ($d^{\\text{int}} \\neq d^{\\text{det}}$). The surviving strategy is labeled as preferred. This constitutes the strongest routing signal, as it reflects a catastrophic outcome difference rather than a marginal score gap.\n    \\item \\textbf{Tied alive}: both strategies survive and their scores differ by at most a threshold $\\tau$ ($|s^{\\text{int}} - s^{\\text{det}}| \\leq \\tau$, $d^{\\text{int}} = d^{\\text{det}} = 0$). Label: \\texttt{no\\_preference}.\n    \\item \\textbf{Both dead}: both strategies result in death ($d^{\\text{int}} = d^{\\text{det}} = 1$). Label: \\texttt{no\\_preference}, as neither strategy provides a viable routing signal.\n    \\item \\textbf{Score comparison}: both survive but scores differ beyond $\\tau$ ($|s^{\\text{int}} - s^{\\text{det}}| > \\tau$, $d^{\\text{int}} = d^{\\text{det}} = 0$). The higher-scoring strategy is preferred.\n\\end{enumerate}\n\nThe resulting label distribution across [PLACEHOLDER: 249] episodes is: [PLACEHOLDER: 41\\%] \\texttt{det\\_preferred}, [PLACEHOLDER: 0.5\\%] \\texttt{internal\\_preferred}, and [PLACEHOLDER: 59\\%] \\texttt{no\\_preference}. The near-absence of \\texttt{internal\\_preferred} labels and the dominance of \\texttt{det\\_preferred} labels---driven overwhelmingly by death asymmetry---indicate that deterministic computation's primary advantage lies in avoiding catastrophic failures rather than achieving higher task scores.\n\n\\subsection{Death Avoidance Factor}\n\\label{sec:daf}\n\nTo quantify the contribution of death avoidance to routing signal, we define the \\emph{Death Avoidance Factor} (DAF). Let $\\Delta_{\\text{full}}$ be the mean score gap between deterministic and internal strategies across all episodes, and $\\Delta_{\\text{no\\_death}}$ be the same gap computed only over episodes where neither strategy results in death:\n\\begin{equation}\n    \\text{DAF} = 1 - \\frac{\\Delta_{\\text{no\\_death}}}{\\Delta_{\\text{full}}}\n\\end{equation}\nDAF $= 1$ indicates that the routing signal is entirely attributable to death avoidance; DAF $= 0$ indicates it derives entirely from non-death performance differences.\n\nAcross the full dataset, [PLACEHOLDER: $\\Delta_{\\text{full}} = +37.9$] and [PLACEHOLDER: $\\Delta_{\\text{no\\_death}} = +0.2$], yielding [PLACEHOLDER: DAF $= 0.99$]. Death avoidance accounts for virtually all of the observed routing advantage. Per-task analysis further confirms this: [PLACEHOLDER: 25] of [PLACEHOLDER: 30] tasks exhibit DAF $\\geq 0.95$, while a small number of tasks show genuine non-death advantages (e.g., \\texttt{measure-melting-point-unknown} with DAF $= 0.594$). The Pearson correlation between per-task death rate differential and score gap is [PLACEHOLDER: $r = 0.989$] ([PLACEHOLDER: $p < 0.0001$]), demonstrating that knowing how much more frequently the internal strategy dies is nearly sufficient to predict the full performance gap.\n\n\\subsection{Rule-Based Baseline}\n\\label{sec:rule}\n\nA natural question is whether simple heuristics can approximate learned routing. We test keyword-based rules that route to deterministic computation when the current action contains science-related verbs, under the hypothesis that actions involving physical or chemical state changes benefit most from exact computation.\n\nWe evaluate three keyword lists of decreasing breadth:\n\\begin{itemize}\n    \\item \\textbf{v1} (20 generic verbs including \\texttt{connect}, \\texttt{move}): matches [PLACEHOLDER: 85.8\\%] of actions, degenerating to an always-deterministic policy.\n    \\item \\textbf{v2} (17 science-specific: \\texttt{heat}, \\texttt{boil}, \\texttt{melt}, \\texttt{freeze}): matches [PLACEHOLDER: 4.9\\%], degenerating to always-internal.\n    \\item \\textbf{v3} (12 state-change verbs): matches [PLACEHOLDER: 2.8\\%], similarly degenerating.\n\\end{itemize}\n\nThe structural cause is that ScienceWorld actions use generic interaction verbs (\\texttt{pick up}, \\texttt{move}, \\texttt{connect}) rather than science-specific terms, making keyword overlap with the underlying task semantics either near-total or negligible. No keyword granularity provides meaningful routing discrimination, motivating observation-based or learned routing approaches.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "451a473c-4927-4c85-a2e0-6b9872ff01c6",
  "isSidechain": false,
  "requestId": "req_011Cb1eKs55wVACuYbvhzpXy",
  "type": "assistant",
  "uuid": "777961ab-30ac-4ddb-948e-664de6b562c1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "e7d68ec2-6069-4d98-9ec3-cf89b610a4f6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NB6oQdHcNJGe4ZoDLQS3JA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2086,
      "cache_read_input_tokens": 30733,
      "output_tokens": 2135,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2086,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2135,
          "cache_read_input_tokens": 30733,
          "cache_creation_input_tokens": 2086,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2086
          },
          "type": "message"
        }
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

_source line 24 · 2026-05-14T02:07:50.179Z_

<details><summary>↩ Tool result · `toolu_01UQhLR4NyXKw89WCJUxQVgQ`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/_project/paper/method_draft.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "777961ab-30ac-4ddb-948e-664de6b562c1",
  "isSidechain": false,
  "promptId": "db5f24fc-919c-42ca-bee6-b8b77a4c500d",
  "type": "user",
  "uuid": "2f064943-b35b-480b-8d5a-08a4edbeb99f",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/_project/paper/method_draft.md",
    "content": "# Method — Draft v1\n\n\\section{Method}\n\nWe describe our methodology in four parts: counterfactual episode collection (\\S\\ref{sec:collection}), death-aware labeling (\\S\\ref{sec:labeling}), the death avoidance factor (\\S\\ref{sec:daf}), and a rule-based baseline analysis (\\S\\ref{sec:rule}).\n\n\\subsection{Counterfactual Episode Collection}\n\\label{sec:collection}\n\nAs motivated in \\S1, per-step oracle labeling degenerates under sparse rewards. We instead adopt \\emph{episode-level counterfactual analysis}: for each task instance, we run two complete episodes under identical initial conditions (same random seed):\n\n\\begin{itemize}\n    \\item \\textbf{Pure-internal}: all steps use the LLM's internal reasoning following the ReAct paradigm \\cite{react-2023}, where the agent interleaves chain-of-thought reasoning with environment actions.\n    \\item \\textbf{Pure-deterministic}: all steps use deterministic external computation via the environment simulator, providing exact state transitions.\n\\end{itemize}\n\nEach episode produces a tuple $(s^{\\text{int}}, s^{\\text{det}}, d^{\\text{int}}, d^{\\text{det}})$, where $s$ denotes episode score and $d \\in \\{0, 1\\}$ indicates whether the agent died. Episodes are capped at [PLACEHOLDER: 30] steps. We use Qwen2.5-7B-Instruct as the LLM backbone, served via vLLM.\n\nWe evaluate on ScienceWorld \\cite{scienceworld-2022}, which provides [PLACEHOLDER: 30] task types spanning physical and chemical reasoning. For each task type, we first run a prescreening phase (5 episodes) to identify tasks where both strategies can be meaningfully compared, then collect the full dataset of [PLACEHOLDER: 20] episodes per task. The final dataset comprises [PLACEHOLDER: 249] episodes across all [PLACEHOLDER: 30] task types.\n\n\\subsection{Death-Aware Labeling}\n\\label{sec:labeling}\n\nWe assign an episode-level routing label to each counterfactual pair based on the four-tuple $(s^{\\text{int}}, s^{\\text{det}}, d^{\\text{int}}, d^{\\text{det}})$, distinguishing four signal types ordered by priority:\n\n\\begin{enumerate}\n    \\item \\textbf{Death asymmetry}: one strategy results in agent death while the other survives ($d^{\\text{int}} \\neq d^{\\text{det}}$). The surviving strategy is labeled as preferred. This constitutes the strongest routing signal, as it reflects a catastrophic outcome difference rather than a marginal score gap.\n    \\item \\textbf{Tied alive}: both strategies survive and their scores differ by at most a threshold $\\tau$ ($|s^{\\text{int}} - s^{\\text{det}}| \\leq \\tau$, $d^{\\text{int}} = d^{\\text{det}} = 0$). Label: \\texttt{no\\_preference}.\n    \\item \\textbf{Both dead}: both strategies result in death ($d^{\\text{int}} = d^{\\text{det}} = 1$). Label: \\texttt{no\\_preference}, as neither strategy provides a viable routing signal.\n    \\item \\textbf{Score comparison}: both survive but scores differ beyond $\\tau$ ($|s^{\\text{int}} - s^{\\text{det}}| > \\tau$, $d^{\\text{int}} = d^{\\text{det}} = 0$). The higher-scoring strategy is preferred.\n\\end{enumerate}\n\nThe resulting label distribution across [PLACEHOLDER: 249] episodes is: [PLACEHOLDER: 41\\%] \\texttt{det\\_preferred}, [PLACEHOLDER: 0.5\\%] \\texttt{internal\\_preferred}, and [PLACEHOLDER: 59\\%] \\texttt{no\\_preference}. The near-absence of \\texttt{internal\\_preferred} labels and the dominance of \\texttt{det\\_preferred} labels---driven overwhelmingly by death asymmetry---indicate that deterministic computation's primary advantage lies in avoiding catastrophic failures rather than achieving higher task scores.\n\n\\subsection{Death Avoidance Factor}\n\\label{sec:daf}\n\nTo quantify the contribution of death avoidance to routing signal, we define the \\emph{Death Avoidance Factor} (DAF). Let $\\Delta_{\\text{full}}$ be the mean score gap between deterministic and internal strategies across all episodes, and $\\Delta_{\\text{no\\_death}}$ be the same gap computed only over episodes where neither strategy results in death:\n\\begin{equation}\n    \\text{DAF} = 1 - \\frac{\\Delta_{\\text{no\\_death}}}{\\Delta_{\\text{full}}}\n\\end{equation}\nDAF $= 1$ indicates that the routing signal is entirely attributable to death avoidance; DAF $= 0$ indicates it derives entirely from non-death performance differences.\n\nAcross the full dataset, [PLACEHOLDER: $\\Delta_{\\text{full}} = +37.9$] and [PLACEHOLDER: $\\Delta_{\\text{no\\_death}} = +0.2$], yielding [PLACEHOLDER: DAF $= 0.99$]. Death avoidance accounts for virtually all of the observed routing advantage. Per-task analysis further confirms this: [PLACEHOLDER: 25] of [PLACEHOLDER: 30] tasks exhibit DAF $\\geq 0.95$, while a small number of tasks show genuine non-death advantages (e.g., \\texttt{measure-melting-point-unknown} with DAF $= 0.594$). The Pearson correlation between per-task death rate differential and score gap is [PLACEHOLDER: $r = 0.989$] ([PLACEHOLDER: $p < 0.0001$]), demonstrating that knowing how much more frequently the internal strategy dies is nearly sufficient to predict the full performance gap.\n\n\\subsection{Rule-Based Baseline}\n\\label{sec:rule}\n\nA natural question is whether simple heuristics can approximate learned routing. We test keyword-based rules that route to deterministic computation when the current action contains science-related verbs, under the hypothesis that actions involving physical or chemical state changes benefit most from exact computation.\n\nWe evaluate three keyword lists of decreasing breadth:\n\\begin{itemize}\n    \\item \\textbf{v1} (20 generic verbs including \\texttt{connect}, \\texttt{move}): matches [PLACEHOLDER: 85.8\\%] of actions, degenerating to an always-deterministic policy.\n    \\item \\textbf{v2} (17 science-specific: \\texttt{heat}, \\texttt{boil}, \\texttt{melt}, \\texttt{freeze}): matches [PLACEHOLDER: 4.9\\%], degenerating to always-internal.\n    \\item \\textbf{v3} (12 state-change verbs): matches [PLACEHOLDER: 2.8\\%], similarly degenerating.\n\\end{itemize}\n\nThe structural cause is that ScienceWorld actions use generic interaction verbs (\\texttt{pick up}, \\texttt{move}, \\texttt{connect}) rather than science-specific terms, making keyword overlap with the underlying task semantics either near-total or negligible. No keyword granularity provides meaningful routing discrimination, motivating observation-based or learned routing approaches.\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "777961ab-30ac-4ddb-948e-664de6b562c1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "e7d68ec2-6069-4d98-9ec3-cf89b610a4f6",
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
  "leafUuid": "2f064943-b35b-480b-8d5a-08a4edbeb99f",
  "sessionId": "e7d68ec2-6069-4d98-9ec3-cf89b610a4f6"
}
```

---

### Runtime record

_source line 26_

```json
{
  "type": "ai-title",
  "aiTitle": "Write Method section for EMNLP short paper",
  "sessionId": "e7d68ec2-6069-4d98-9ec3-cf89b610a4f6"
}
```

---

### Assistant

_source line 27 · 2026-05-14T02:07:54.417Z_

Now let me register the artifact.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2f064943-b35b-480b-8d5a-08a4edbeb99f",
  "isSidechain": false,
  "requestId": "req_011Cb1ePLkJmLpAYfqzBpAWf",
  "type": "assistant",
  "uuid": "3d19e062-6ef7-405b-81c1-618c87f4aa2d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "e7d68ec2-6069-4d98-9ec3-cf89b610a4f6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015B8LPuS8Sztd73FaGEdg4g",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2191,
      "cache_read_input_tokens": 32819,
      "output_tokens": 93,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2191,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 93,
          "cache_read_input_tokens": 32819,
          "cache_creation_input_tokens": 2191,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2191
          },
          "type": "message"
        }
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

_source line 28 · 2026-05-14T02:07:54.977Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01Eix2imycpkbfHiioFNjwsi`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__register_artifact",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3d19e062-6ef7-405b-81c1-618c87f4aa2d",
  "isSidechain": false,
  "requestId": "req_011Cb1ePLkJmLpAYfqzBpAWf",
  "type": "assistant",
  "uuid": "364b4628-2248-4a48-a8a0-aeb60c2e62ab",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "e7d68ec2-6069-4d98-9ec3-cf89b610a4f6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015B8LPuS8Sztd73FaGEdg4g",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2191,
      "cache_read_input_tokens": 32819,
      "output_tokens": 93,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2191,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 93,
          "cache_read_input_tokens": 32819,
          "cache_creation_input_tokens": 2191,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2191
          },
          "type": "message"
        }
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

_source line 29 · 2026-05-14T02:07:54.981Z_

<details><summary>↩ Tool result · `toolu_01Eix2imycpkbfHiioFNjwsi`</summary>

````text
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
  "parentUuid": "364b4628-2248-4a48-a8a0-aeb60c2e62ab",
  "isSidechain": false,
  "promptId": "db5f24fc-919c-42ca-bee6-b8b77a4c500d",
  "type": "user",
  "uuid": "7a042160-9249-4f77-a06e-ab7e6409b643",
  "toolUseResult": {
    "matches": [
      "mcp__agent-ml-research__register_artifact"
    ],
    "query": "select:mcp__agent-ml-research__register_artifact",
    "total_deferred_tools": 50
  },
  "sourceToolAssistantUUID": "364b4628-2248-4a48-a8a0-aeb60c2e62ab",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "e7d68ec2-6069-4d98-9ec3-cf89b610a4f6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 30 · 2026-05-14T02:07:55.047Z_

```json
{
  "parentUuid": "7a042160-9249-4f77-a06e-ab7e6409b643",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "a4b74211-d1ab-4c24-ad42-3a7c0451ed4a",
  "timestamp": "2026-05-14T02:07:55.047Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "e7d68ec2-6069-4d98-9ec3-cf89b610a4f6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 31 · 2026-05-14T02:08:01.440Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact · `toolu_0163t8VPuYNayzRpWVRsTdcf`</summary>

```json
{
  "name": "method_draft",
  "type": "paper",
  "description": "Method section draft v1 for EMNLP 2026 short paper — 4 subsections: Counterfactual Episode Collection, Death-Aware Labeling, Death Avoidance Factor (DAF), Rule-Based Baseline. ~850 words, LaTeX format with PLACEHOLDER annotations.",
  "project": "simgate-modular-routing",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/_project/paper/method_draft.md",
  "tags": [
    "paper",
    "method",
    "draft-v1",
    "emnlp2026"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a4b74211-d1ab-4c24-ad42-3a7c0451ed4a",
  "isSidechain": false,
  "requestId": "req_011Cb1ePhYi2MWh5a7DnJe1m",
  "type": "assistant",
  "uuid": "3ca03502-71c3-42e3-9a82-e6c35bb33d3a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "e7d68ec2-6069-4d98-9ec3-cf89b610a4f6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SYj1dpYWD46hpvAmyVAvLM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 822,
      "cache_read_input_tokens": 35010,
      "output_tokens": 285,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 822,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 285,
          "cache_read_input_tokens": 35010,
          "cache_creation_input_tokens": 822,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 822
          },
          "type": "message"
        }
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

_source line 32 · 2026-05-14T02:08:01.483Z_

<details><summary>↩ Tool result · `toolu_0163t8VPuYNayzRpWVRsTdcf`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260514_e328fe\", \"name\": \"method_draft\", \"type\": \"paper\", \"description\": \"Method section draft v1 for EMNLP 2026 short paper — 4 subsections: Counterfactual Episode Collection, Death-Aware Labeling, Death Avoidance Factor (DAF), Rule-Based Baseline. ~850 words, LaTeX format with PLACEHOLDER annotations.\", \"path\": \"projects/simgate-modular-routing/artifacts/_project/paper/method_draft_e328fe.md\", \"url\": null, \"project\": \"simgate-modular-routing\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-14T02:08:01.449321+00:00\", \"tags\": [\"paper\", \"method\", \"draft-v1\", \"emnlp2026\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3ca03502-71c3-42e3-9a82-e6c35bb33d3a",
  "isSidechain": false,
  "promptId": "db5f24fc-919c-42ca-bee6-b8b77a4c500d",
  "type": "user",
  "uuid": "461a864d-086c-4521-8eb4-6a12cbca7928",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"artifact\\\": {\\\"id\\\": \\\"art_20260514_e328fe\\\", \\\"name\\\": \\\"method_draft\\\", \\\"type\\\": \\\"paper\\\", \\\"description\\\": \\\"Method section draft v1 for EMNLP 2026 short paper — 4 subsections: Counterfactual Episode Collection, Death-Aware Labeling, Death Avoidance Factor (DAF), Rule-Based Baseline. ~850 words, LaTeX format with PLACEHOLDER annotations.\\\", \\\"path\\\": \\\"projects/simgate-modular-routing/artifacts/_project/paper/method_draft_e328fe.md\\\", \\\"url\\\": null, \\\"project\\\": \\\"simgate-modular-routing\\\", \\\"exp_id\\\": null, \\\"skill\\\": \\\"\\\", \\\"created_at\\\": \\\"2026-05-14T02:08:01.449321+00:00\\\", \\\"tags\\\": [\\\"paper\\\", \\\"method\\\", \\\"draft-v1\\\", \\\"emnlp2026\\\"]}, \\\"manifest\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/manifest.yaml\\\"}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260514_e328fe\", \"name\": \"method_draft\", \"type\": \"paper\", \"description\": \"Method section draft v1 for EMNLP 2026 short paper — 4 subsections: Counterfactual Episode Collection, Death-Aware Labeling, Death Avoidance Factor (DAF), Rule-Based Baseline. ~850 words, LaTeX format with PLACEHOLDER annotations.\", \"path\": \"projects/simgate-modular-routing/artifacts/_project/paper/method_draft_e328fe.md\", \"url\": null, \"project\": \"simgate-modular-routing\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-14T02:08:01.449321+00:00\", \"tags\": [\"paper\", \"method\", \"draft-v1\", \"emnlp2026\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "3ca03502-71c3-42e3-9a82-e6c35bb33d3a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "e7d68ec2-6069-4d98-9ec3-cf89b610a4f6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 33 · 2026-05-14T02:08:13.212Z_

Method draft v1 已写入 `artifacts/_project/paper/method_draft.md` 并注册 (`art_20260514_e328fe`)。

**结构**：4 个 subsection，约 850 words，符合 ~1 页篇幅：
- §3.1 Counterfactual Episode Collection — pure-internal vs pure-deterministic 对比设计，seed-matched episodes
- §3.2 Death-Aware Labeling — 四元组 → 四类 signal 的优先级规则，label 分布
- §3.3 Death Avoidance Factor — DAF 公式（编号 equation），全局 DAF=0.99，per-task 分析，Pearson r=0.989
- §3.4 Rule-Based Baseline — 三版 keyword list 均退化，结构性原因分析

**一致性**：术语、符号（$\Delta_{\text{full}}$, $\Delta_{\text{no\_death}}$, DAF）、引用 keys 均与 Introduction/Related Work 对齐。所有可能更新的数字标注了 `[PLACEHOLDER]`。Introduction 已论述的 oracle degeneracy 仅用 "as motivated in §1" 回指，未重复。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "461a864d-086c-4521-8eb4-6a12cbca7928",
  "isSidechain": false,
  "requestId": "req_011Cb1eQBBNNumfCd5byaJrc",
  "type": "assistant",
  "uuid": "4f10d65f-96bb-49ed-bab5-dcdc80cc2185",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "e7d68ec2-6069-4d98-9ec3-cf89b610a4f6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TZ6HPwwZPfEucK1DyMs7Lw",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 608,
      "cache_read_input_tokens": 35832,
      "output_tokens": 334,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 608,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 334,
          "cache_read_input_tokens": 35832,
          "cache_creation_input_tokens": 608,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 608
          },
          "type": "message"
        }
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

_source line 34_

```json
{
  "type": "last-prompt",
  "leafUuid": "4f10d65f-96bb-49ed-bab5-dcdc80cc2185",
  "sessionId": "e7d68ec2-6069-4d98-9ec3-cf89b610a4f6"
}
```

---

### Runtime record

_source line 35_

```json
{
  "type": "ai-title",
  "aiTitle": "Write Method section for EMNLP short paper",
  "sessionId": "e7d68ec2-6069-4d98-9ec3-cf89b610a4f6"
}
```

---
