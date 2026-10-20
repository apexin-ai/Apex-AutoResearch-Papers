# Research conversation: [HANDOFF] 你是 Main Agent，这是 Loop #15。 ## 上一轮交接 (task_context) ### 1. 🔴 硬约束 / 红线 - GPU 白名单：**westd-22162 cuda:0~3** 仅此 4 张

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 72
- **Recorded user turns:** 1
- **Tool calls:** 19
- **Original source:** `logs/chats/exported-trajectories/account-3/ffa9d23f-27b7-4443-aea1-c7cdeeb2bf53.jsonl`
- **Structured JSON:** [`23c0457797911914f272.json`](../../sessions/23/23c0457797911914f272.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-16T02:45:51.630Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-16T02:45:51.630Z",
  "sessionId": "ffa9d23f-27b7-4443-aea1-c7cdeeb2bf53",
  "content": "[HANDOFF] 你是 Main Agent，这是 Loop #15。\n\n## 上一轮交接 (task_context)\n\n### 1. 🔴 硬约束 / 红线\n- GPU 白名单：**westd-22162 cuda:0~3** 仅此 4 张，不可用其他 GPU\n- c8_llama_n250 正在占满 4 GPU（4 并行推理），完成前不可提交新 GPU 实验\n- EMNLP 2026 ARR **截稿 2026-05-25**（距今 9 天），Round 10 Weak Reject (2.25/5) 修订中，Findings track\n- Paper 修订必须先读 red-section skill，MUSTAFAR 引用已标记删除（R10-C1 fake citation）\n- DS accuracy 数据**已降为定性观察**（D086），QW 是 accuracy dose-response 主证据\n- G× 值已下修为 21-64×（D082），不要引用旧值 58-241×\n\n### 2. 🖥️ 基础设施快照\n- 服务器：**westd-22162**，工作目录 `/root/autodl-tmp/pacs`\n- Python：conda base（`/root/miniconda3/bin/python`），不是 venv\n- 模型：DeepSeek-R1-Distill-Qwen-7B, Qwen2.5-7B-Instruct, DeepSeek-R1-Distill-Llama-8B（均在服务器本地）\n- 活跃进程：**c8_llama_n250** RUNNING（4 GPU 并行，cron 监控中，command=`bash run_c8_llama_n250.sh`，log=/tmp/c8_llama_n250.log）\n- 活跃 Worker：3 个 running — `worker_analysis_c5_per_phase_gini_20260516T024150`（per-phase Gini）、`worker_analysis_c9_gsm8k_power_20260516T024207`（GSM8K power analysis）、`worker_analysis_c10_lang_switching_20260516T024225`（language switching check）\n- 活跃 Cron：c8_llama_n250（interval 300s，刚 reconcile 过）\n\n### 3. 📊 当前状态\n前一轮完成 Round 10 审稿回溯，拆解 Action Matrix（5 Critical + 6 Warning → 2 SYSTEMIC_ISSUE），已派发全部修订任务：\n- **c8_llama_n250** RUNNING — LLaMA n=250 跨架构验证（8 conditions: imp/rand × 4 sparsity），GPU 密集，预估 5-6h，回应 R10-C3 underpowered\n- **c5_per_phase_gini** PREPARING — Worker 正在跑 per-phase Gini decomposition（CPU，从 c4_entropy 数据），回应 R10-C5\n- **c4_think_validation_math500** PREPARING — Worker 尚未开始（可能等 c5 Worker 先做完或被排队），验证 `&lt;think>` token 与 PPL phase segmentation 一致性，回应 R10-C4\n- **c9_gsm8k_power_analysis** PREPARING — Worker 正在跑 GSM8K post-hoc power analysis（CPU），回应 R10-W5\n- **c10_lang_switching** PREPARING — Worker 正在检查 DS language switching rate（CPU），回应写作质疑\n- Paper Agent 修订任务（bib 审计、Abstract/Intro rewrite、§4-7 corrections、Appendix fixes）**尚未派发**\n\n等待中：3 个 Worker 回调 + c8_llama_n250 cron 回调 + Paper Agent 任务待派\n\n### 4. 📋 待办（条件触发式）\n- c5_per_phase_gini Worker 回调 → 更新 registry metrics + report.md，汇报 Director\n- c9_gsm8k_power Worker 回调 → 更新 registry + 汇报 Director（power analysis 结果决定是否需要扩大 GSM8K 样本量）\n- c10_lang_switching Worker 回调 → 更新 registry + 汇报（结果入论文 Appendix）\n- c4_think_validation_math500 若还没有 Worker 在跑 → 需 spawn worker 执行\n- c8_llama_n250 cron 回调 (DONE) → on-experiment-done 全流程：分析 8 condition 结果，imp_vs_rand d_z 是否 ≥0.5 → 成功则更新 C8 evidence 并写入论文；n=250 仍 NS → Framing 调整提案（LLaMA 降为 \"qualitative consistency\"）\n- 4 个 CPU Worker 回调后 → 立即 spawn Paper Agent（bib 审计 + Abstract/Intro + §4-7 + Appendix）并行修订\n- 全部修订完成 → Round 11 审稿提交\n\n### 5. 🎯 战略上下文\n- **核心发现**：importance-based eviction 的 compound interaction severity 随 sparsity 单调递增，DS/QW 双模型 n=500 confirm（Spearman ρ=1.0, all Bonferroni sig）。Random masking 无 phase gradient（DS s015-s020 NS）。\n- **最大风险**：C8 LLaMA cross-arch 目前 n=49 只有 s030 一个点 significant。n=250 是 make-or-break：成功 → 三模型 generalization claim 站住；失败 → LLaMA 降为 qualitative + discussion。**不要等 LLaMA 结果再动 paper**——先写其他部分（DS/QW 部分已稳固）。\n- **易错点 1**：QW random s030 GSM8K gradient (2.89) > importance gradient (2.09) — 已知反转，paper_framing 注明仅在原始 II_low 值上。不要把这个当 negative。\n- **易错点 2**：C4 entropy collapse 是 model-dependent（QW s025 反转），Gini/CV 才是跨模型一致的证据。论文里 entropy 只能写 DS confirmed + QW model-dependent。\n- **易错点 3**：DS accuracy dose curve 只有 4 点（无 s030），且 s020+ truncation 驱动。不要当作 II 的直接映射。\n- **决策链**：D091 接受 Findings track → D090 dual dose curve 完成 → D089 双 regime 结构发现 → 当前 Round 10 修订\n\n## 可查的历史\n前 235 轮 handoff 在 `task_context/history/agent/loop_*.md`，如有疑问可 Read 回查。\n完整聊天归档可用 `recall_session_history(\"关键词\")` 搜索。\n\n## 第一个动作要求\n1. 用 `read_registry` 确认当前 RUNNING/PREPARING 实验状态（防止幻觉记忆过时状态）\n2. 回复一句话确认你看到了上面的硬约束 + 当前活跃实验，再开始任何工具调用"
}
```

---

### Runtime record

_source line 2 · 2026-05-16T02:45:51.634Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-16T02:45:51.634Z",
  "sessionId": "ffa9d23f-27b7-4443-aea1-c7cdeeb2bf53"
}
```

---

## Round 1

70 recorded events

### User

_source line 3 · 2026-05-16T02:45:51.673Z_

[HANDOFF] 你是 Main Agent，这是 Loop #15。

## 上一轮交接 (task_context)

### 1. 🔴 硬约束 / 红线
- GPU 白名单：**westd-22162 cuda:0~3** 仅此 4 张，不可用其他 GPU
- c8_llama_n250 正在占满 4 GPU（4 并行推理），完成前不可提交新 GPU 实验
- EMNLP 2026 ARR **截稿 2026-05-25**（距今 9 天），Round 10 Weak Reject (2.25/5) 修订中，Findings track
- Paper 修订必须先读 red-section skill，MUSTAFAR 引用已标记删除（R10-C1 fake citation）
- DS accuracy 数据**已降为定性观察**（D086），QW 是 accuracy dose-response 主证据
- G× 值已下修为 21-64×（D082），不要引用旧值 58-241×

### 2. 🖥️ 基础设施快照
- 服务器：**westd-22162**，工作目录 `/root/autodl-tmp/pacs`
- Python：conda base（`/root/miniconda3/bin/python`），不是 venv
- 模型：DeepSeek-R1-Distill-Qwen-7B, Qwen2.5-7B-Instruct, DeepSeek-R1-Distill-Llama-8B（均在服务器本地）
- 活跃进程：**c8_llama_n250** RUNNING（4 GPU 并行，cron 监控中，command=`bash run_c8_llama_n250.sh`，log=/tmp/c8_llama_n250.log）
- 活跃 Worker：3 个 running — `worker_analysis_c5_per_phase_gini_20260516T024150`（per-phase Gini）、`worker_analysis_c9_gsm8k_power_20260516T024207`（GSM8K power analysis）、`worker_analysis_c10_lang_switching_20260516T024225`（language switching check）
- 活跃 Cron：c8_llama_n250（interval 300s，刚 reconcile 过）

### 3. 📊 当前状态
前一轮完成 Round 10 审稿回溯，拆解 Action Matrix（5 Critical + 6 Warning → 2 SYSTEMIC_ISSUE），已派发全部修订任务：
- **c8_llama_n250** RUNNING — LLaMA n=250 跨架构验证（8 conditions: imp/rand × 4 sparsity），GPU 密集，预估 5-6h，回应 R10-C3 underpowered
- **c5_per_phase_gini** PREPARING — Worker 正在跑 per-phase Gini decomposition（CPU，从 c4_entropy 数据），回应 R10-C5
- **c4_think_validation_math500** PREPARING — Worker 尚未开始（可能等 c5 Worker 先做完或被排队），验证 `&lt;think>` token 与 PPL phase segmentation 一致性，回应 R10-C4
- **c9_gsm8k_power_analysis** PREPARING — Worker 正在跑 GSM8K post-hoc power analysis（CPU），回应 R10-W5
- **c10_lang_switching** PREPARING — Worker 正在检查 DS language switching rate（CPU），回应写作质疑
- Paper Agent 修订任务（bib 审计、Abstract/Intro rewrite、§4-7 corrections、Appendix fixes）**尚未派发**

等待中：3 个 Worker 回调 + c8_llama_n250 cron 回调 + Paper Agent 任务待派

### 4. 📋 待办（条件触发式）
- c5_per_phase_gini Worker 回调 → 更新 registry metrics + report.md，汇报 Director
- c9_gsm8k_power Worker 回调 → 更新 registry + 汇报 Director（power analysis 结果决定是否需要扩大 GSM8K 样本量）
- c10_lang_switching Worker 回调 → 更新 registry + 汇报（结果入论文 Appendix）
- c4_think_validation_math500 若还没有 Worker 在跑 → 需 spawn worker 执行
- c8_llama_n250 cron 回调 (DONE) → on-experiment-done 全流程：分析 8 condition 结果，imp_vs_rand d_z 是否 ≥0.5 → 成功则更新 C8 evidence 并写入论文；n=250 仍 NS → Framing 调整提案（LLaMA 降为 "qualitative consistency"）
- 4 个 CPU Worker 回调后 → 立即 spawn Paper Agent（bib 审计 + Abstract/Intro + §4-7 + Appendix）并行修订
- 全部修订完成 → Round 11 审稿提交

### 5. 🎯 战略上下文
- **核心发现**：importance-based eviction 的 compound interaction severity 随 sparsity 单调递增，DS/QW 双模型 n=500 confirm（Spearman ρ=1.0, all Bonferroni sig）。Random masking 无 phase gradient（DS s015-s020 NS）。
- **最大风险**：C8 LLaMA cross-arch 目前 n=49 只有 s030 一个点 significant。n=250 是 make-or-break：成功 → 三模型 generalization claim 站住；失败 → LLaMA 降为 qualitative + discussion。**不要等 LLaMA 结果再动 paper**——先写其他部分（DS/QW 部分已稳固）。
- **易错点 1**：QW random s030 GSM8K gradient (2.89) > importance gradient (2.09) — 已知反转，paper_framing 注明仅在原始 II_low 值上。不要把这个当 negative。
- **易错点 2**：C4 entropy collapse 是 model-dependent（QW s025 反转），Gini/CV 才是跨模型一致的证据。论文里 entropy 只能写 DS confirmed + QW model-dependent。
- **易错点 3**：DS accuracy dose curve 只有 4 点（无 s030），且 s020+ truncation 驱动。不要当作 II 的直接映射。
- **决策链**：D091 接受 Findings track → D090 dual dose curve 完成 → D089 双 regime 结构发现 → 当前 Round 10 修订

## 可查的历史
前 235 轮 handoff 在 `task_context/history/agent/loop_*.md`，如有疑问可 Read 回查。
完整聊天归档可用 `recall_session_history("关键词")` 搜索。

## 第一个动作要求
1. 用 `read_registry` 确认当前 RUNNING/PREPARING 实验状态（防止幻觉记忆过时状态）
2. 回复一句话确认你看到了上面的硬约束 + 当前活跃实验，再开始任何工具调用

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "d6a043a1-3c08-4fe7-9e57-50e76a38ea26",
  "type": "user",
  "uuid": "b2027776-1bbe-4ab4-9c23-6dc32e8d16b7",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/.claude/sessions/agent_9c1243df",
  "sessionId": "ffa9d23f-27b7-4443-aea1-c7cdeeb2bf53",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-16T02:45:51.673Z_

```json
{
  "parentUuid": "b2027776-1bbe-4ab4-9c23-6dc32e8d16b7",
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
      "mcp__agent-ml-research__allocate_and_submit",
      "mcp__agent-ml-research__append_idea",
      "mcp__agent-ml-research__approve_worker",
      "mcp__agent-ml-research__auto_build_provenance",
      "mcp__agent-ml-research__backup_project_to_s3",
      "mcp__agent-ml-research__cancel_worker",
      "mcp__agent-ml-research__check_job_status",
      "mcp__agent-ml-research__check_paper_consistency",
      "mcp__agent-ml-research__check_provenance_completeness",
      "mcp__agent-ml-research__cleanup_pdf_images",
      "mcp__agent-ml-research__compute_coverage_matrix",
      "mcp__agent-ml-research__detect_image",
      "mcp__agent-ml-research__edit_paper_section",
      "mcp__agent-ml-research__feishu_read_tum_pending_key",
      "mcp__agent-ml-research__feishu_send_alert",
      "mcp__agent-ml-research__feishu_send_approval_card",
      "mcp__agent-ml-research__feishu_send_result_card",
      "mcp__agent-ml-research__feishu_send_tum_key_request_card",
      "mcp__agent-ml-research__fetch_wandb_metrics",
      "mcp__agent-ml-research__get_baseline_metrics",
      "mcp__agent-ml-research__get_gpu_health",
      "mcp__agent-ml-research__get_image_info",
      "mcp__agent-ml-research__get_matrix_value",
      "mcp__agent-ml-research__get_project_resource_usage",
      "mcp__agent-ml-research__get_tum_config",
      "mcp__agent-ml-research__get_worker_status",
      "mcp__agent-ml-research__impact_analysis",
      "mcp__agent-ml-research__kill_job",
      "mcp__agent-ml-research__list_artifacts",
      "mcp__agent-ml-research__list_available_gpus",
      "mcp__agent-ml-research__list_constraints",
      "mcp__agent-ml-research__list_s3_backups",
      "mcp__agent-ml-research__list_workers",
      "mcp__agent-ml-research__load_project_config",
      "mcp__agent-ml-research__main_agent_post_to_director",
      "mcp__agent-ml-research__matrix_gap_analysis",
      "mcp__agent-ml-research__pdf_to_images",
      "mcp__agent-ml-research__poll_cron",
      "mcp__agent-ml-research__poll_secret_request",
      "mcp__agent-ml-research__read_experiment_plan_with_status",
      "mcp__agent-ml-research__read_matrix",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__read_roadmap",
      "mcp__agent-ml-research__reconcile_crons",
      "mcp__agent-ml-research__register_artifact",
      "mcp__agent-ml-research__register_cron",
      "mcp__agent-ml-research__request_secret",
      "mcp__agent-ml-research__save_project_file",
      "mcp__agent-ml-research__send_progress",
      "mcp__agent-ml-research__spawn_worker",
      "mcp__agent-ml-research__submit_on_allocated",
      "mcp__agent-ml-research__submit_training_job",
      "mcp__agent-ml-research__sync_matrix_status",
      "mcp__agent-ml-research__tail_training_logs",
      "mcp__agent-ml-research__update_baseline",
      "mcp__agent-ml-research__update_matrix",
      "mcp__agent-ml-research__update_registry",
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
      "mcp__agent-ml-research__allocate_and_submit",
      "mcp__agent-ml-research__append_idea",
      "mcp__agent-ml-research__approve_worker",
      "mcp__agent-ml-research__auto_build_provenance",
      "mcp__agent-ml-research__backup_project_to_s3",
      "mcp__agent-ml-research__cancel_worker",
      "mcp__agent-ml-research__check_job_status",
      "mcp__agent-ml-research__check_paper_consistency",
      "mcp__agent-ml-research__check_provenance_completeness",
      "mcp__agent-ml-research__cleanup_pdf_images",
      "mcp__agent-ml-research__compute_coverage_matrix",
      "mcp__agent-ml-research__detect_image",
      "mcp__agent-ml-research__edit_paper_section",
      "mcp__agent-ml-research__feishu_read_tum_pending_key",
      "mcp__agent-ml-research__feishu_send_alert",
      "mcp__agent-ml-research__feishu_send_approval_card",
      "mcp__agent-ml-research__feishu_send_result_card",
      "mcp__agent-ml-research__feishu_send_tum_key_request_card",
      "mcp__agent-ml-research__fetch_wandb_metrics",
      "mcp__agent-ml-research__get_baseline_metrics",
      "mcp__agent-ml-research__get_gpu_health",
      "mcp__agent-ml-research__get_image_info",
      "mcp__agent-ml-research__get_matrix_value",
      "mcp__agent-ml-research__get_project_resource_usage",
      "mcp__agent-ml-research__get_tum_config",
      "mcp__agent-ml-research__get_worker_status",
      "mcp__agent-ml-research__impact_analysis",
      "mcp__agent-ml-research__kill_job",
      "mcp__agent-ml-research__list_artifacts",
      "mcp__agent-ml-research__list_available_gpus",
      "mcp__agent-ml-research__list_constraints",
      "mcp__agent-ml-research__list_s3_backups",
      "mcp__agent-ml-research__list_workers",
      "mcp__agent-ml-research__load_project_config",
      "mcp__agent-ml-research__main_agent_post_to_director",
      "mcp__agent-ml-research__matrix_gap_analysis",
      "mcp__agent-ml-research__pdf_to_images",
      "mcp__agent-ml-research__poll_cron",
      "mcp__agent-ml-research__poll_secret_request",
      "mcp__agent-ml-research__read_experiment_plan_with_status",
      "mcp__agent-ml-research__read_matrix",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__read_roadmap",
      "mcp__agent-ml-research__reconcile_crons",
      "mcp__agent-ml-research__register_artifact",
      "mcp__agent-ml-research__register_cron",
      "mcp__agent-ml-research__request_secret",
      "mcp__agent-ml-research__save_project_file",
      "mcp__agent-ml-research__send_progress",
      "mcp__agent-ml-research__spawn_worker",
      "mcp__agent-ml-research__submit_on_allocated",
      "mcp__agent-ml-research__submit_training_job",
      "mcp__agent-ml-research__sync_matrix_status",
      "mcp__agent-ml-research__tail_training_logs",
      "mcp__agent-ml-research__update_baseline",
      "mcp__agent-ml-research__update_matrix",
      "mcp__agent-ml-research__update_registry",
      "mcp__agent-ml-research__verify_references",
      "mcp__agent-ml-research__write_paper_section"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "76da25f3-0b74-47c3-b34c-8f84fedd7974",
  "timestamp": "2026-05-16T02:45:51.673Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/.claude/sessions/agent_9c1243df",
  "sessionId": "ffa9d23f-27b7-4443-aea1-c7cdeeb2bf53",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-16T02:45:51.673Z_

```json
{
  "parentUuid": "76da25f3-0b74-47c3-b34c-8f84fedd7974",
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
  "uuid": "e4ea57c6-fac6-4462-8fa8-fda9f133d7de",
  "timestamp": "2026-05-16T02:45:51.673Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/.claude/sessions/agent_9c1243df",
  "sessionId": "ffa9d23f-27b7-4443-aea1-c7cdeeb2bf53",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6 · 2026-05-16T02:45:51.673Z_

```json
{
  "parentUuid": "e4ea57c6-fac6-4462-8fa8-fda9f133d7de",
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
  "uuid": "039de2ac-0e9e-4dad-931c-733f7ce13f11",
  "timestamp": "2026-05-16T02:45:51.673Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/.claude/sessions/agent_9c1243df",
  "sessionId": "ffa9d23f-27b7-4443-aea1-c7cdeeb2bf53",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 7 · 2026-05-16T02:45:51.673Z_

```json
{
  "parentUuid": "039de2ac-0e9e-4dad-931c-733f7ce13f11",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "27c2eaa0-3fd9-4e70-bc3a-5c5dc6a24b7f",
  "timestamp": "2026-05-16T02:45:51.673Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/.claude/sessions/agent_9c1243df",
  "sessionId": "ffa9d23f-27b7-4443-aea1-c7cdeeb2bf53",
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
  "aiTitle": "Verify active experiments and paper revisions for EMNLP 2026",
  "sessionId": "ffa9d23f-27b7-4443-aea1-c7cdeeb2bf53"
}
```

---

### Assistant

_source line 9 · 2026-05-16T02:45:56.060Z_

<details><summary>Logged reasoning block</summary>

```text
新 session 启动，按 session-start 规范执行初始化。先确认硬约束，然后并行读取 registry、reconcile crons、读 report.md 和 ROADMAP.md。
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "27c2eaa0-3fd9-4e70-bc3a-5c5dc6a24b7f",
  "isSidechain": false,
  "requestId": "req_011Cb5UuMQSBYMwLYSUzhvX9",
  "type": "assistant",
  "uuid": "e55cb6dd-e2e1-49d4-a47a-017619542137",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/.claude/sessions/agent_9c1243df",
  "sessionId": "ffa9d23f-27b7-4443-aea1-c7cdeeb2bf53",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FkhRB7ccaLJnpZCPcawr4M",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 25331,
      "cache_read_input_tokens": 11447,
      "output_tokens": 320,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 25331,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 320,
          "cache_read_input_tokens": 11447,
          "cache_creation_input_tokens": 25331,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 25331
          },
          "type": "message"
        }
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

_source line 10 · 2026-05-16T02:45:57.648Z_

确认：4 GPU 白名单 westd-22162 cuda:0~3，c8_llama_n250 占满 4 卡，EMNLP ARR 截稿 5/25（剩 9 天），3 个 CPU Worker 在跑。开始 session-start 初始化。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e55cb6dd-e2e1-49d4-a47a-017619542137",
  "isSidechain": false,
  "requestId": "req_011Cb5UuMQSBYMwLYSUzhvX9",
  "type": "assistant",
  "uuid": "cb31f15c-9462-43f9-a4f5-3c9f4f1ba9ea",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/.claude/sessions/agent_9c1243df",
  "sessionId": "ffa9d23f-27b7-4443-aea1-c7cdeeb2bf53",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FkhRB7ccaLJnpZCPcawr4M",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 25331,
      "cache_read_input_tokens": 11447,
      "output_tokens": 320,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 25331,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 320,
          "cache_read_input_tokens": 11447,
          "cache_creation_input_tokens": 25331,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 25331
          },
          "type": "message"
        }
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

_source line 11 · 2026-05-16T02:45:59.611Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01YF3YmnUgvrX6XbgtDAXEfn`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__reconcile_crons,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__read_roadmap,mcp__agent-ml-research__main_agent_post_to_director,mcp__agent-ml-research__list_workers",
  "max_results": 6
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cb31f15c-9462-43f9-a4f5-3c9f4f1ba9ea",
  "isSidechain": false,
  "requestId": "req_011Cb5UuMQSBYMwLYSUzhvX9",
  "type": "assistant",
  "uuid": "5cda8789-195b-4d63-982d-05454375d308",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/.claude/sessions/agent_9c1243df",
  "sessionId": "ffa9d23f-27b7-4443-aea1-c7cdeeb2bf53",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FkhRB7ccaLJnpZCPcawr4M",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 25331,
      "cache_read_input_tokens": 11447,
      "output_tokens": 320,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 25331,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 320,
          "cache_read_input_tokens": 11447,
          "cache_creation_input_tokens": 25331,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 25331
          },
          "type": "message"
        }
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

_source line 12 · 2026-05-16T02:45:59.621Z_

<details><summary>↩ Tool result · `toolu_01YF3YmnUgvrX6XbgtDAXEfn`</summary>

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
  "tool_name": "mcp__agent-ml-research__reconcile_crons"
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
  "tool_name": "mcp__agent-ml-research__read_roadmap"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__main_agent_post_to_director"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__list_workers"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5cda8789-195b-4d63-982d-05454375d308",
  "isSidechain": false,
  "promptId": "d6a043a1-3c08-4fe7-9e57-50e76a38ea26",
  "type": "user",
  "uuid": "4b8ae34c-80a6-4142-b7e7-948e8730749a",
  "toolUseResult": {
    "matches": [
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__reconcile_crons",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__read_roadmap",
      "mcp__agent-ml-research__main_agent_post_to_director",
      "mcp__agent-ml-research__list_workers"
    ],
    "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__reconcile_crons,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__read_roadmap,mcp__agent-ml-research__main_agent_post_to_director,mcp__agent-ml-research__list_workers",
    "total_deferred_tools": 79
  },
  "sourceToolAssistantUUID": "5cda8789-195b-4d63-982d-05454375d308",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/.claude/sessions/agent_9c1243df",
  "sessionId": "ffa9d23f-27b7-4443-aea1-c7cdeeb2bf53",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-16T02:46:02.732Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01WSdeo65wXau1sDf9Vwn3Sg`</summary>

```json
{
  "project": "phase-gated-compound-sparse",
  "limit": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4b8ae34c-80a6-4142-b7e7-948e8730749a",
  "isSidechain": false,
  "requestId": "req_011Cb5UuwN6gHEciLdxbQscj",
  "type": "assistant",
  "uuid": "894da37e-35e8-457e-82ab-0a7ae63a39f2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/.claude/sessions/agent_9c1243df",
  "sessionId": "ffa9d23f-27b7-4443-aea1-c7cdeeb2bf53",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UADVgkN4zKVRvZ67BUf752",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1658,
      "cache_read_input_tokens": 36778,
      "output_tokens": 312,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1658,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 312,
          "cache_read_input_tokens": 36778,
          "cache_creation_input_tokens": 1658,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1658
          },
          "type": "message"
        }
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

_source line 14 · 2026-05-16T02:46:03.089Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__reconcile_crons · `toolu_01EYAyJGB1st1q3WHkTPC52G`</summary>

```json
{}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "894da37e-35e8-457e-82ab-0a7ae63a39f2",
  "isSidechain": false,
  "requestId": "req_011Cb5UuwN6gHEciLdxbQscj",
  "type": "assistant",
  "uuid": "4af5a121-263e-4780-ba60-9bf86b3f9ecd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/.claude/sessions/agent_9c1243df",
  "sessionId": "ffa9d23f-27b7-4443-aea1-c7cdeeb2bf53",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UADVgkN4zKVRvZ67BUf752",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1658,
      "cache_read_input_tokens": 36778,
      "output_tokens": 312,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1658,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 312,
          "cache_read_input_tokens": 36778,
          "cache_creation_input_tokens": 1658,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1658
          },
          "type": "message"
        }
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

_source line 15 · 2026-05-16T02:46:03.531Z_

<details><summary>↩ Tool result · `toolu_01WSdeo65wXau1sDf9Vwn3Sg`</summary>

```text
Error: result (94,593 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-phase-gated-compound-sparse--claude-sessions-agent-9c1243df/ffa9d23f-27b7-4443-aea1-c7cdeeb2bf53/tool-results/mcp-agent-ml-research-read_registry-1778899563513.txt.
Format: JSON with schema: {result: string}
- For targeted queries (find a value, filter by field): use jq on the file directly.
- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-phase-gated-compound-sparse--claude-sessions-agent-9c1243df/ffa9d23f-27b7-4443-aea1-c7cdeeb2bf53/tool-results/mcp-agent-ml-research-read_registry-1778899563513.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.
- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-phase-gated-compound-sparse--claude-sessions-agent-9c1243df/ffa9d23f-27b7-4443-aea1-c7cdeeb2bf53/tool-results/mcp-agent-ml-research-read_registry-1778899563513.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim." A vague "summarize this" may lose detail.

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "894da37e-35e8-457e-82ab-0a7ae63a39f2",
  "isSidechain": false,
  "promptId": "d6a043a1-3c08-4fe7-9e57-50e76a38ea26",
  "type": "user",
  "uuid": "2949a970-7d32-4cd9-80b0-10d153fcc8fe",
  "toolUseResult": "Error: result (94,593 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-phase-gated-compound-sparse--claude-sessions-agent-9c1243df/ffa9d23f-27b7-4443-aea1-c7cdeeb2bf53/tool-results/mcp-agent-ml-research-read_registry-1778899563513.txt.\nFormat: JSON with schema: {result: string}\n- For targeted queries (find a value, filter by field): use jq on the file directly.\n- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-phase-gated-compound-sparse--claude-sessions-agent-9c1243df/ffa9d23f-27b7-4443-aea1-c7cdeeb2bf53/tool-results/mcp-agent-ml-research-read_registry-1778899563513.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.\n- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. \"/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-phase-gated-compound-sparse--claude-sessions-agent-9c1243df/ffa9d23f-27b7-4443-aea1-c7cdeeb2bf53/tool-results/mcp-agent-ml-research-read_registry-1778899563513.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim.\" A vague \"summarize this\" may lose detail.\n",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"c10_lang_switching\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-16T02:41:23.965Z\", \"updated_at\": \"2026-05-16T02:41:23.965Z\"}, \"c9_gsm8k_power_analysis\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-16T02:41:22.330Z\", \"updated_at\": \"2026-05-16T02:41:22.330Z\"}, \"c8_llama_n250\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-16T02:32:37.721Z\", \"updated_at\": \"2026-05-16T02:37:11.623Z\"}, \"c5_per_phase_gini\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-16T02:32:42.922Z\", \"updated_at\": \"2026-05-16T02:32:42.922Z\"}, \"c4_think_validation_math500\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-16T02:32:40.564Z\", \"updated_at\": \"2026-05-16T02:32:40.564Z\"}, \"acc_ds_s030_8k_v2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T21:35:02.560Z\", \"updated_at\": \"2026-05-16T01:41:37.520Z\", \"hypothesis\": \"DS s030 accuracy eval with max_new_tokens=8192，补全 5-point dose curve。\", \"metrics\": {\"accuracy\": 0.04, \"correct\": 2, \"total\": 50, \"truncation_rate\": 0.76, \"truncated_count\": 38, \"extraction_failures\": 3, \"non_truncated_accuracy\": 0.167, \"non_truncated_correct\": 2, \"non_truncated_total\": 12, \"max_new_tokens\": 8192, \"avg_tokens\": 6566.3, \"total_time_seconds\": 7095.1}, \"conclusion\": \"success\"}, \"acc_qw_s030_b1_8k\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T00:55:21.056Z\", \"updated_at\": \"2026-05-16T01:32:35.412Z\", \"hypothesis\": \"重跑 QW importance_s030 batch1 (problems 1-50) with max_new_tokens=8192，修复原 batch1 使用 2048 的 token 预算不匹配问题。\", \"metrics\": {\"accuracy\": 0.14, \"correct\": 7, \"total\": 50, \"truncation_rate\": 0.04, \"truncated_count\": 2, \"extraction_failures\": 8, \"max_new_tokens\": 8192, \"total_time_seconds\": 886.7, \"batch\": \"b1_v2 (problems 1-50, 8k tokens)\", \"old_batch1_acc\": 0.14, \"old_batch1_correct\": 7, \"batch2_acc\": 0.24, \"batch2_correct\": 12, \"new_combined_n100_acc\": 0.19, \"new_combined_n100_correct\": 19}, \"conclusion\": \"negative\"}, \"acc_qw_s025_b1_8k\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T00:55:20.024Z\", \"updated_at\": \"2026-05-16T01:32:32.193Z\", \"hypothesis\": \"重跑 QW importance_s025 batch1 (problems 1-50) with max_new_tokens=8192，修复原 batch1 使用 2048 的 token 预算不匹配问题。\", \"metrics\": {\"accuracy\": 0.32, \"correct\": 16, \"n_problems\": 50, \"truncation_rate\": 0.04, \"truncated_count\": 2, \"extraction_failures\": 6, \"avg_tokens\": 797.3, \"total_time_seconds\": 831.6}, \"conclusion\": \"negative\"}, \"acc_qw_s015_b1_8k\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T00:55:17.275Z\", \"updated_at\": \"2026-05-16T01:31:00.641Z\", \"hypothesis\": \"重跑 QW importance_s015 batch1 (problems 1-50) with max_new_tokens=8192，修复原 batch1 使用 2048 的 token 预算不匹配问题。\", \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 0.46, \"correct\": 23, \"total\": 50, \"truncation_rate_8k\": 0.02, \"gen_over_2k\": 3, \"gen_over_2k_all_wrong\": true, \"max_gen_length\": 8192, \"mean_gen_length\": 776}}, \"acc_ds_s020_8k_v2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T21:34:59.657Z\", \"updated_at\": \"2026-05-16T01:30:53.536Z\", \"hypothesis\": \"DS s020 accuracy eval with max_new_tokens=8192，补全 5-point dose curve。4096 版截断率 64%，8k 目标 <20%。\", \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 0.3, \"correct\": 15, \"total\": 50, \"truncated_count\": 28, \"truncated_rate\": 0.56, \"extraction_failures\": 1, \"non_truncated_accuracy\": 0.682, \"non_truncated_correct\": 15, \"non_truncated_total\": 22, \"total_time_seconds\": 5549, \"max_new_tokens\": 8192}}, \"acc_qw_s020_b1_8k\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T00:55:18.700Z\", \"updated_at\": \"2026-05-16T01:11:21.524Z\", \"hypothesis\": \"重跑 QW importance_s020 batch1 (problems 1-50) with max_new_tokens=8192，修复原 batch1 使用 2048 的 token 预算不匹配问题。\", \"metrics\": {\"accuracy\": 0.26, \"correct\": 13, \"n_problems\": 50, \"truncation_rate\": 0.02, \"truncated_count\": 1, \"avg_tokens\": 722.1, \"max_tokens_generated\": 8192, \"max_new_tokens\": 8192, \"total_time_seconds\": 729.1, \"null_count\": 0, \"batch\": \"b1_v2 (problems 1-50, 8k tokens)\", \"old_batch1_acc\": 0.26, \"old_batch1_correct\": 13, \"new_combined_n100_acc\": 0.36, \"new_combined_n100_correct\": 36, \"batch2_acc\": 0.46, \"batch2_correct\": 23}, \"conclusion\": \"success\"}, \"acc_qw_dense_b1_8k\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T00:55:16.337Z\", \"updated_at\": \"2026-05-16T01:11:19.181Z\", \"hypothesis\": \"重跑 QW dense batch1 (problems 1-50) with max_new_tokens=8192，修复原 batch1 使用 2048 的 token 预算不匹配问题。\", \"metrics\": {\"accuracy\": 0.44, \"correct\": 22, \"n_problems\": 50, \"truncation_rate\": 0.02, \"truncated_count\": 1, \"avg_tokens\": 759.7, \"max_tokens_generated\": 8192, \"max_new_tokens\": 8192, \"total_time_seconds\": 681.8, \"null_count\": 0, \"batch\": \"b1_v2 (problems 1-50, 8k tokens)\", \"old_batch1_acc\": 0.32, \"old_batch1_correct\": 16, \"new_combined_n100_acc\": 0.46, \"new_combined_n100_correct\": 46, \"batch2_acc\": 0.48, \"batch2_correct\": 24}, \"conclusion\": \"success\"}, \"acc_ds_s015_8k_v2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T21:34:57.489Z\", \"updated_at\": \"2026-05-16T00:32:31.715Z\", \"hypothesis\": \"DS s015 accuracy eval with max_new_tokens=8192，验证 dense→s015 是否存在断崖式下降（v1 暗示 0.74→~0.36）。\", \"metrics\": {\"accuracy\": 0.48, \"correct\": 24, \"total\": 50, \"truncation_rate\": 0.32, \"truncated_count\": 16, \"non_truncated_accuracy\": 0.706, \"non_truncated_correct\": 24, \"non_truncated_total\": 34, \"wall_time_s\": 3967, \"max_new_tokens\": 8192}, \"conclusion\": \"success\"}, \"r9c2-spike-v3\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T20:35:35.819Z\", \"updated_at\": \"2026-05-16T00:28:46.195Z\", \"conclusion\": \"killed\", \"notes\": \"abandoned — spike investigation 已终止，非 critical path\"}, \"r9c2-spike-v2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T20:35:10.902Z\", \"updated_at\": \"2026-05-16T00:28:44.920Z\", \"conclusion\": \"killed\", \"notes\": \"abandoned — spike investigation 已终止，非 critical path\"}, \"r9c2-spike\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T20:34:26.906Z\", \"updated_at\": \"2026-05-16T00:28:43.177Z\", \"conclusion\": \"killed\", \"notes\": \"abandoned — spike investigation 已终止，非 critical path\"}, \"acc_ds_s025_8k_v2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T21:35:01.085Z\", \"updated_at\": \"2026-05-16T00:20:39.536Z\", \"hypothesis\": \"DS s025 accuracy eval with max_new_tokens=8192，补全 5-point dose curve。4096 版截断率 76%，8k 目标 <20%。\", \"conclusion\": \"negative\", \"metrics\": {\"accuracy\": 0.08, \"correct\": 4, \"total\": 50, \"truncated_count\": 38, \"truncated_rate\": 0.76, \"avg_tokens\": 6343.8, \"max_new_tokens\": 8192, \"total_time_seconds\": 6827.8, \"null_count\": 36}}, \"gsm8k_qw_rand_s025_v2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T22:30:14.407Z\", \"updated_at\": \"2026-05-15T23:44:43.451Z\", \"hypothesis\": \"C10 重跑：QW random masking s=0.25 GSM8K compound interaction（修复 bootstrap bug 后）\", \"parent\": \"gsm8k_qw_rand_s025\", \"conclusion\": \"success\", \"metrics\": {\"verdict\": \"PASS\", \"n_problems\": 50, \"n_bootstrap\": 1000, \"seed\": 42, \"high_sparsity\": {\"n_segments\": 216, \"n_tokens\": 9326, \"ppl_dense\": 1.0695, \"ppl_attn\": 5.9362, \"ppl_kv\": 3.4316, \"ppl_both\": 15.7484, \"ii_mean\": 6.5954, \"ii_ci\": [1.1114, 11.3791], \"ii_median\": 0.7176, \"ii_median_ci\": [0.5959, 0.9347], \"winsorized_mean\": 6.5046, \"skewness\": -4.6807, \"outlier_count\": 3}, \"low_sparsity\": {\"n_segments\": 252, \"n_tokens\": 29224, \"ppl_dense\": 1.1972, \"ppl_attn\": 11.5347, \"ppl_kv\": 5.6038, \"ppl_both\": 21.6874, \"ii_mean\": 2.3883, \"ii_ci\": [-8.4602, 11.029], \"ii_median\": 1.4587, \"ii_median_ci\": [1.1121, 2.0451], \"winsorized_mean\": 5.8911, \"skewness\": -7.6074, \"outlier_count\": 4}, \"mid_sparsity\": {\"n_segments\": 51, \"n_tokens\": 5954, \"ppl_dense\": 1.2601, \"ppl_attn\": 13.4132, \"ppl_kv\": 6.4841, \"ppl_both\": 20.8714, \"ii_mean\": 4.5407, \"ii_ci\": [-4.8854, 12.4605], \"ii_median\": 1.1272, \"ii_median_ci\": [0.637, 3.3729], \"winsorized_mean\": 6.3284, \"skewness\": -3.4048, \"outlier_count\": 1}}}, \"gsm8k_qw_rand_s030_v2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T22:30:15.959Z\", \"updated_at\": \"2026-05-15T23:28:35.411Z\", \"hypothesis\": \"C10 重跑：QW random masking s=0.30 GSM8K compound interaction（修复 bootstrap bug 后）\", \"parent\": \"gsm8k_qw_rand_s030\", \"conclusion\": \"success\", \"metrics\": {\"verdict\": \"PASS\", \"n_problems\": 50, \"n_bootstrap\": 1000, \"seed\": 42, \"high_sparsity\": {\"n_segments\": 216, \"n_tokens\": 9326, \"null_ratio\": \"2/50\", \"ppl_dense\": 1.0695, \"ppl_attn\": 6.5613, \"ppl_kv\": 4.481, \"ppl_both\": 23.7486, \"ii_mean\": 11.83, \"ii_median\": 2.31, \"ii_ci\": [6.17, 17.04], \"ii_median_ci\": [1.64, 2.81], \"winsorized_mean\": 10.55, \"skewness\": -2.29, \"outlier_count\": 7}, \"low_sparsity\": {\"n_segments\": 252, \"n_tokens\": 29224, \"null_ratio\": \"5/50\", \"ppl_dense\": 1.1972, \"ppl_attn\": 6.3283, \"ppl_kv\": 8.5374, \"ppl_both\": 56.2304, \"ii_mean\": 31.26, \"ii_median\": 5.2, \"ii_ci\": [17.84, 47.86], \"ii_median_ci\": [3.95, 7.24], \"winsorized_mean\": 16.35, \"skewness\": 7.57, \"outlier_count\": 4}, \"mid_sparsity\": {\"n_segments\": 51, \"n_tokens\": 5954, \"null_ratio\": \"17/50\", \"ppl_dense\": 1.2601, \"ppl_attn\": 18.6162, \"ppl_kv\": 11.6625, \"ppl_both\": 47.9019, \"ii_mean\": 18.02, \"ii_median\": 2.7, \"ii_ci\": [0.09, 36.69], \"ii_median_ci\": [1.46, 8.77], \"winsorized_mean\": 18.22, \"skewness\": 0.43, \"outlier_count\": 2}}}, \"acc_qw_s025_n100_b2_fix\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T22:22:57.057Z\", \"updated_at\": \"2026-05-15T23:28:18.012Z\", \"hypothesis\": \"重跑 QW s025 batch2 (problems 51-100) with max_new_tokens=8192，修复原 batch2 使用 2048 的不一致问题。\", \"parent\": \"acc_qw_s025_n100\", \"metrics\": {\"accuracy\": 0.34, \"correct\": 17, \"n_problems\": 50, \"truncation_rate\": 0.06, \"truncated_count\": 3, \"avg_tokens\": 1044, \"max_new_tokens\": 8192, \"total_time_seconds\": 1099, \"batch\": \"b2 (problems 51-100)\", \"merged_n100_accuracy\": 0.33, \"merged_n100_correct\": 33, \"merged_n100_note\": \"batch1 used max_new_tokens=2048, batch2_fix used 8192 — mismatch\"}, \"conclusion\": \"success\"}, \"acc_ds_dense_8k_v2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T22:27:00.640Z\", \"updated_at\": \"2026-05-15T23:28:12.650Z\", \"hypothesis\": \"DS dense 8k 重跑：原 acc_ds_dense_8k 进程被 kill 后输出丢失，需重跑获取完整 dense baseline accuracy (max_new_tokens=8192)。\", \"metrics\": {\"accuracy\": 0.74, \"correct\": 37, \"n_problems\": 50, \"truncation_rate\": 0.16, \"truncated_count\": 8, \"avg_tokens\": 3126, \"max_new_tokens\": 8192, \"total_time_seconds\": 2882}, \"conclusion\": \"success\"}, \"acc_qw_s020_n100_b2_fix\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T22:22:55.755Z\", \"updated_at\": \"2026-05-15T22:48:39.196Z\", \"hypothesis\": \"重跑 QW s020 batch2 (problems 51-100) with max_new_tokens=8192，修复原 batch2 使用 2048 的不一致问题。\", \"parent\": \"acc_qw_s020_n100\", \"conclusion\": \"success\", \"metrics\": {\"batch2_correct\": 23, \"batch2_total\": 50, \"batch2_acc\": 0.46, \"batch1_correct_v2\": 13, \"batch1_total\": 50, \"batch1_acc_v2\": 0.26, \"combined_correct\": 36, \"combined_total\": 100, \"combined_acc\": 0.36, \"null_count\": 2, \"truncated_count\": 1, \"total_time_seconds\": 884.3, \"max_new_tokens\": 8192, \"original_batch2_correct\": 22, \"original_batch2_acc\": 0.44, \"delta_vs_original\": \"+1 correct (+0.02 acc)\"}}, \"gsm8k_qw_rand_s025\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T21:37:36.627Z\", \"updated_at\": \"2026-05-15T22:27:18.969Z\", \"hypothesis\": \"C10: QW random masking s=0.25 在 GSM8K 上的 compound interaction，作为 importance masking 的对照组。参照 gsm8k_profiling_qw 设置。\", \"parent\": \"gsm8k_profiling_qw\", \"conclusion\": \"failed\"}, \"gsm8k_qw_rand_s030\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T21:37:39.530Z\", \"updated_at\": \"2026-05-15T22:23:52.155Z\", \"hypothesis\": \"C10: QW random masking s=0.30 在 GSM8K 上的 compound interaction，作为 importance masking 的对照组。gsm8k_profiling_qw 中此条件结果 INVALID，需重跑。\", \"parent\": \"gsm8k_profiling_qw\", \"conclusion\": \"failed\"}, \"acc_qw_s030_n100\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T21:34:40.948Z\", \"updated_at\": \"2026-05-15T22:21:11.181Z\", \"hypothesis\": \"补跑 QW importance_s030 problems 51-100，扩展到 n=100 以降低噪声\", \"conclusion\": \"success\", \"metrics\": {\"batch1_correct\": 7, \"batch1_total\": 50, \"batch1_acc\": 0.14, \"batch1_source\": \"acc_qw_s030_b1_8k (v2, 8k tokens)\", \"batch2_correct\": 12, \"batch2_total\": 50, \"batch2_acc\": 0.24, \"combined_correct\": 19, \"combined_total\": 100, \"combined_acc\": 0.19}}, \"acc_qw_dense_n100\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T21:34:35.557Z\", \"updated_at\": \"2026-05-15T21:54:45.453Z\", \"hypothesis\": \"补跑 QW dense problems 51-100，扩展到 n=100 以降低噪声\", \"metrics\": {\"batch1_correct\": 22, \"batch1_total\": 50, \"batch1_acc\": 0.44, \"batch1_source\": \"acc_qw_dense_b1_8k (v2, 8k tokens)\", \"batch2_correct\": 24, \"batch2_total\": 50, \"batch2_acc\": 0.48, \"combined_correct\": 46, \"combined_total\": 100, \"combined_acc\": 0.46}, \"conclusion\": \"success\"}, \"acc_qw_s015_n100\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T21:34:38.959Z\", \"updated_at\": \"2026-05-15T21:50:13.043Z\", \"hypothesis\": \"补跑 QW importance_s015 problems 51-100，扩展到 n=100 以降低噪声\", \"metrics\": {\"batch1_acc\": 0.46, \"batch1_correct\": 23, \"batch1_total\": 50, \"batch1_source\": \"acc_qw_s015_b1_8k (v2, 8k tokens)\", \"batch2_acc\": 0.38, \"batch2_correct\": 19, \"batch2_total\": 50, \"combined_acc\": 0.42, \"combined_correct\": 42, \"combined_total\": 100}, \"conclusion\": \"success\"}, \"acc_qw_s025_n100\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T21:09:36.278Z\", \"updated_at\": \"2026-05-15T21:34:48.072Z\", \"conclusion\": \"success\", \"metrics\": {\"batch1_acc\": 0.32, \"batch1_correct\": 16, \"batch1_total\": 50, \"batch1_source\": \"acc_qw_s025_b1_8k (v2, 8k tokens)\", \"batch2_acc\": 0.34, \"batch2_correct\": 17, \"batch2_total\": 50, \"combined_acc\": 0.33, \"combined_correct\": 33, \"combined_total\": 100}}, \"acc_qw_s020_n100\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T21:09:34.155Z\", \"updated_at\": \"2026-05-15T21:34:46.864Z\", \"conclusion\": \"success\", \"metrics\": {\"batch1_acc\": 0.26, \"batch1_correct\": 13, \"batch1_total\": 50, \"batch1_source\": \"acc_qw_s020_b1_8k (v2, 8k tokens)\", \"batch2_acc\": 0.46, \"batch2_correct\": 23, \"batch2_total\": 50, \"combined_acc\": 0.36, \"combined_correct\": 36, \"combined_total\": 100, \"note\": \"batch effect: batch1=26% vs batch2=46%, Δ=20pp\"}}, \"acc_ds_s030_8k\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T21:22:53.748Z\", \"updated_at\": \"2026-05-15T21:29:19.105Z\", \"hypothesis\": \"8192 token budget 下 DS s030 截断率应从高截断率降至 <20%，accuracy 应高于 4096 版本的 0.10\", \"conclusion\": \"killed\"}, \"acc_ds_s025_8k\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T21:22:52.297Z\", \"updated_at\": \"2026-05-15T21:29:17.817Z\", \"hypothesis\": \"8192 token budget 下 DS s025 截断率应从 76% 降至 <20%，accuracy 应高于 4096 版本的 0.08\", \"conclusion\": \"killed\"}, \"acc_ds_s020_8k\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T21:22:51.129Z\", \"updated_at\": \"2026-05-15T21:29:16.495Z\", \"hypothesis\": \"8192 token budget 下 DS s020 截断率应从 64% 降至 <20%，accuracy 应高于 4096 版本的 0.26\", \"conclusion\": \"killed\"}, \"acc_ds_dense_8k\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T21:22:44.546Z\", \"updated_at\": \"2026-05-15T21:28:57.693Z\", \"hypothesis\": \"8192 token budget 下 DS dense baseline 截断率应降至 <20%，accuracy 应高于 4096 版本的 0.52\", \"conclusion\": \"killed\"}, \"acc_ds_s015_8k\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T21:22:48.736Z\", \"updated_at\": \"2026-05-15T21:28:48.029Z\", \"hypothesis\": \"8192 token budget 下 DS s015 截断率应降至 <20%，accuracy 应高于 4096 版本的 0.36\", \"conclusion\": \"killed\"}, \"acc_ds_s025\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T20:49:25.437Z\", \"updated_at\": \"2026-05-15T21:23:19.024Z\", \"metrics\": {\"accuracy\": 0.08, \"correct\": 4, \"total\": 50, \"null_count\": 37, \"null_rate\": 0.74, \"output_truncated_count\": 38, \"output_truncated_rate\": 0.76, \"wrong_count\": 9, \"wrong_rate\": 0.18, \"extraction_failure_count\": 1, \"extraction_failure_rate\": 0.02, \"total_time_s\": 1670.5, \"heads_pruned\": 196, \"delta_vs_dense\": -0.44}, \"conclusion\": \"negative\"}, \"acc_ds_s020\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T20:49:21.186Z\", \"updated_at\": \"2026-05-15T21:20:03.642Z\", \"conclusion\": \"negative\", \"metrics\": {\"ds_s020_acc\": 0.26, \"ds_s020_acc_v2\": 0.26, \"ds_s020_correct\": 13, \"ds_s020_total\": 50, \"ds_s020_delta_vs_dense\": -0.26, \"output_truncated_count\": 32, \"output_truncated_rate\": 0.64, \"extraction_failure_count\": 31, \"extraction_failure_rate\": 0.62, \"total_time_s\": 1560, \"note\": \"v2 rescored with fixed radical+degree matcher; 0 changes. Dense baseline=0.52\"}}, \"c2_accuracy_eval\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T20:44:33.644Z\", \"updated_at\": \"2026-05-15T21:17:27.151Z\", \"conclusion\": \"success\", \"metrics\": {\"n_problems\": 50, \"ds_dense_acc\": 0.52, \"ds_s015_acc\": 0.36, \"ds_s015_delta\": -0.16, \"ds_s030_acc\": 0.1, \"ds_s030_delta\": -0.42, \"qw_dense_acc\": 0.32, \"qw_s015_acc\": 0.34, \"qw_s015_delta\": 0.02, \"qw_s030_acc\": 0.14, \"qw_s030_delta\": -0.18, \"ds_s030_chinese_reasoning_rate\": 0.4, \"ds_dense_truncation_rate\": 0.56, \"note\": \"v2 rescored with fixed radical+degree matcher. DS s015 34→36, QW s015 32→34\"}}, \"acc_qw_s025\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T20:49:29.416Z\", \"updated_at\": \"2026-05-15T21:17:24.568Z\", \"metrics\": {\"qw_s025_acc\": 0.32, \"qw_s025_correct\": 16, \"qw_s025_total\": 50, \"qw_s025_delta_vs_dense\": 0, \"null_count\": 8, \"null_rate\": 0.16, \"output_truncated_count\": 2, \"output_truncated_rate\": 0.04, \"extraction_failure_count\": 6, \"extraction_failure_rate\": 0.12, \"wrong_count\": 26, \"wrong_rate\": 0.52, \"heads_pruned\": 196, \"total_time_s\": 559, \"note\": \"v2 rescored with fixed radical+degree matcher; 3 problems flipped (sqrt+degree)\"}, \"conclusion\": \"negative\"}, \"acc_qw_s020\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T20:49:27.167Z\", \"updated_at\": \"2026-05-15T21:17:22.146Z\", \"metrics\": {\"qw_s020_acc\": 0.26, \"qw_s020_correct\": 13, \"qw_s020_total\": 50, \"qw_s020_delta_vs_dense\": -0.06, \"null_count\": 2, \"null_rate\": 0.04, \"output_truncated_count\": 2, \"output_truncated_rate\": 0.04, \"extraction_failure_count\": 0, \"extraction_failure_rate\": 0, \"wrong_count\": 35, \"wrong_rate\": 0.7, \"heads_pruned\": 140, \"total_time_s\": 598, \"note\": \"v2 rescored with fixed radical+degree matcher\"}, \"conclusion\": \"negative\"}, \"think_phase_validation\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T19:35:06.395Z\", \"updated_at\": \"2026-05-15T19:35:45.955Z\", \"conclusion\": \"success\", \"metrics\": {\"effective_n\": 48, \"skipped_problems\": 2, \"median_kappa\": 0.887, \"thinking_in_low_sparsity_phase\": 0.578, \"answer_in_high_sparsity_phase\": 0.627, \"note\": \"Phase segmentation based on dense model — 4 sparsity conditions share identical phase boundaries, effective sample n=48 not n=192\"}}, \"gsm8k_profiling_qw\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T14:09:43.081Z\", \"updated_at\": \"2026-05-15T18:33:54.305Z\", \"hypothesis\": \"GSM8K profiling 验证 compound sparsity severity 的可迁移性：Qwen 在 GSM8K n=50 上是否复现 MATH-500 的 phase-gated II pattern（importance > random, 单调递增）\", \"conclusion\": \"success\", \"notes\": \"All QW outputs truncated at max_new_tokens=2047 (50/50 problems). Does not affect directional conclusions. rand_s030 per-sparsity data missing, merged data has aggregation bug.\", \"metrics\": {\"version\": \"v3_median\", \"n_problems\": 50, \"method\": \"median + Wilcoxon + bootstrap_median(B=10000)\", \"importance\": {\"s015\": {\"median_gradient\": 0.039}, \"s020\": {\"median_gradient\": 0.158}, \"s025\": {\"median_gradient\": 1.1}, \"s030\": {\"median_gradient\": 2.092}}, \"qw_rand_s030\": \"INVALID\"}}, \"gsm8k_profiling_ds\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T14:09:41.908Z\", \"updated_at\": \"2026-05-15T18:33:52.432Z\", \"hypothesis\": \"GSM8K profiling 验证 compound sparsity severity 的可迁移性：DeepSeek 在 GSM8K n=50 上是否复现 MATH-500 的 phase-gated II pattern（importance > random, 单调递增）\", \"conclusion\": \"success\", \"metrics\": {\"version\": \"v3_median\", \"n_problems\": 50, \"method\": \"median + Wilcoxon + bootstrap_median(B=10000)\", \"importance\": {\"s015\": {\"median_gradient\": 0.241, \"ci_low\": 0.077, \"ci_high\": 0.478, \"wilcoxon_p\": 0.0003}, \"s020\": {\"median_gradient\": 0.74, \"ci_low\": 0.314, \"ci_high\": 1.119, \"wilcoxon_p\": 0.0001}, \"s025\": {\"median_gradient\": 1.992, \"ci_low\": 0.933, \"ci_high\": 2.82, \"wilcoxon_p\": 0.0001}, \"s030\": {\"median_gradient\": 4.682, \"ci_low\": 2.121, \"ci_high\": 10.557, \"wilcoxon_p\": 0.0001}}, \"imp_rand_ratio\": {\"s015\": 2.3, \"s020\": 2.5, \"s025\": 3.8, \"s030\": 2.8}, \"dose_response_monotonic\": true}}, \"sf5_asymmetric_spot\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T10:59:35.784Z\", \"updated_at\": \"2026-05-15T18:20:37.200Z\", \"conclusion\": \"success\", \"metrics\": {\"config_a_h02_kv03\": {\"II_low\": 19.51, \"II_mid\": 6.05, \"II_high\": 0.38, \"D\": 19.13}, \"config_b_h03_kv02\": {\"II_low\": 18.77, \"II_mid\": 3.97, \"II_high\": 0.52, \"D\": 18.25}, \"pre_registered_criterion_passed\": true, \"gradient_direction\": \"II_low >> II_mid >> II_high (consistent with symmetric baseline)\"}}, \"c2_qw_n500_r3\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T19:26:53.700Z\", \"updated_at\": \"2026-05-15T08:40:33.785Z\", \"hypothesis\": \"C2 Qwen n=500 continuation (cron false positive on c2_qw_n500). s015 完成, s020-s030 remaining. 与 DeepSeek 对称验证 compound sparsity severity.\", \"parent\": \"c2_qw_n500\", \"notes\": \"[2026-05-15] n=475 (low+high valid). [D066] Bonferroni revised: k=4 family-wise (was k=48). QW rand s025/s030 remain *** under k=4. BH-FDR also applied (48 tests). All imp conditions *** unchanged. Results in n500_unified_final.{csv,json}, n500_full_statistics.md.\", \"metrics\": {\"n_problems\": 500, \"effective_n\": 475, \"filter\": \"low+high valid only (mid-null allowed)\", \"mid_null_rate\": 0.452, \"imp_s015_median_ii\": 0.0659, \"imp_s015_ci\": [0.0492, 0.0925], \"imp_s015_wilcoxon_p\": 8.66e-15, \"imp_s015_bonf_p\": 3.46e-14, \"imp_s020_median_ii\": 0.3073, \"imp_s020_ci\": [0.2612, 0.3564], \"imp_s020_wilcoxon_p\": 6.84e-42, \"imp_s020_bonf_p\": 2.74e-41, \"imp_s025_median_ii\": 1.0745, \"imp_s025_ci\": [0.9766, 1.1787], \"imp_s025_wilcoxon_p\": 1.06e-68, \"imp_s025_bonf_p\": 4.25e-68, \"imp_s030_median_ii\": 3.155, \"imp_s030_ci\": [2.7834, 3.5582], \"imp_s030_wilcoxon_p\": 9.21e-74, \"imp_s030_bonf_p\": 3.69e-73, \"rand_s015_median_ii\": -0.0111, \"rand_s015_wilcoxon_p\": 0.172, \"rand_s015_bonf_p\": 0.687, \"rand_s020_median_ii\": 0.0153, \"rand_s020_wilcoxon_p\": 0.2, \"rand_s020_bonf_p\": 0.8, \"rand_s025_median_ii\": 0.3931, \"rand_s025_wilcoxon_p\": 1.59e-11, \"rand_s025_bonf_p\": 6.37e-11, \"rand_s025_fdr_p\": 2.63e-11, \"rand_s030_median_ii\": 0.9127, \"rand_s030_wilcoxon_p\": 2.92e-15, \"rand_s030_bonf_p\": 1.17e-14, \"rand_s030_fdr_p\": 5.61e-15, \"dz_s015_s020\": -0.629, \"dz_s020_s025\": -0.865, \"dz_s025_s030\": -0.767, \"dz_s015_s030\": -0.923, \"all_dz_reliable\": true, \"dose_response_monotonic\": true, \"dose_response_spearman_rho\": 1, \"dose_response_perm_p\": 0.0417, \"imp_rand_ratio_range\": \"2.7-20.1x\", \"bonferroni_k\": 4, \"bonferroni_note\": \"Bonferroni k=4 family-wise (D066 revision)\"}, \"conclusion\": \"success\"}, \"c2_n500_deepseek\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T13:33:50.628Z\", \"updated_at\": \"2026-05-15T08:40:22.196Z\", \"hypothesis\": \"C2 statistical power boost: 将 DeepSeek 8 conditions (imp/rand × 4 sparsity) 从 n=50 扩到 n=500，提升统计功效。预注册：若 QW s015 在 n=500 后 CI 仍跨零，论文叙事改为 \\\"compound effect emerges above a threshold sparsity level (~s020)\\\"\", \"notes\": \"[2026-05-15] ALL 8 CONDITIONS DONE (500/500). [D066] Bonferroni revised: k=4 family-wise (was k=48). DS rand s025 bonf_p=0.0058 (**), s030 bonf_p=0.0059 (**) — both restored to significant. BH-FDR also applied (48 tests): rand s025/s030 fdr_p=0.0019. Results in n500_unified_final.{csv,json}.\", \"metrics\": {\"n_problems\": 500, \"effective_n\": 496, \"mid_null_rate\": 0.102, \"imp_s015_median_ii\": 0.3907, \"imp_s015_ci\": [0.3496, 0.4431], \"imp_s015_wilcoxon_p\": 1.27e-70, \"imp_s020_median_ii\": 1.2149, \"imp_s020_ci\": [1.1072, 1.3365], \"imp_s020_wilcoxon_p\": 3.98e-75, \"imp_s025_median_ii\": 3.9857, \"imp_s025_ci\": [3.5272, 4.3588], \"imp_s025_wilcoxon_p\": 1.99e-78, \"imp_s030_median_ii\": 8.4813, \"imp_s030_ci\": [7.7543, 9.6919], \"imp_s030_wilcoxon_p\": 1.09e-79, \"rand_s015_median_ii\": 0.0139, \"rand_s015_wilcoxon_p\": 0.863, \"rand_s020_median_ii\": 0.0315, \"rand_s020_wilcoxon_p\": 0.28, \"rand_s025_median_ii\": 0.2574, \"rand_s025_bonf_p\": 0.005839, \"rand_s025_fdr_p\": 0.001914, \"rand_s030_median_ii\": 0.5096, \"rand_s030_bonf_p\": 0.005903, \"rand_s030_fdr_p\": 0.001914, \"dz_s015_s020\": -0.925, \"dz_s020_s025\": -0.824, \"dz_s025_s030\": -0.773, \"dz_s015_s030\": -0.944, \"all_dz_reliable\": true, \"dose_response_monotonic\": true, \"dose_response_spearman_rho\": 1, \"dose_response_perm_p\": 0.0417, \"imp_rand_ratio_range\": \"15.5-38.6x\", \"bonferroni_k\": 4, \"bonferroni_note\": \"Bonferroni k=4 family-wise (D066 revision)\"}, \"conclusion\": \"success\"}, \"c2_qw_n500\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T13:34:05.213Z\", \"updated_at\": \"2026-05-14T19:26:11.742Z\", \"hypothesis\": \"C2: Qwen n=500 统计功效提升。将 Qwen 8 conditions (imp/rand × 4 sparsity) 从 n=50 扩到 n=500，与 DeepSeek 对称验证。\", \"notes\": \"2026-05-15T03:30: Cron false positive corrected. Process alive on GPU 2+3. s015 COMPLETE (500/500 both conditions, results in profiling_results.json). s020 RUNNING: qw_imp_s020 PID159269 cuda:2, qw_rand_s020 PID159794 cuda:3. Screen session auto-advances through sparsity levels. n=500 s015 analysis: both DeepSeek and Qwen paired gradient now significant (Bonferroni p<0.0001), resolving D058.\", \"conclusion\": \"failed\"}, \"c5b_pilot\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T14:51:04.044Z\", \"updated_at\": \"2026-05-14T19:10:56.005Z\", \"hypothesis\": \"C5b mitigation pilot: oracle (真实 phase labels) + heuristic (token position ratio) phase-aware sparsity allocation 能否恢复 compound interaction severity。Gate: oracle recovery >30% at s025 or s030。\", \"notes\": \"s025 30/30 完成（GPU3 run）。Gate FAIL: oracle recovery +18.0% < 30% threshold。Heuristic recovery +31.7%。s030 未完成（SSH 断连 kill）。Cron 误判为 failed（无 sentinel/W&B），实际 s025 结果完整。结果路径: profiling_output_c5b_all_s025/mitigation_pilot_results.json。Framing 提案: C5b → §8 Future Work open question。\", \"conclusion\": \"negative\", \"metrics\": {\"s025_uniform_median_ii\": 1.0435, \"s025_oracle_median_ii\": 0.856, \"s025_oracle_recovery_pct\": 18, \"s025_oracle_recovery_ci\": [-39, 45.8], \"s025_oracle_wilcoxon_p\": 0.0021, \"s025_heuristic_median_ii\": 0.7127, \"s025_heuristic_recovery_pct\": 31.7, \"s025_heuristic_recovery_ci\": [-22.8, 66], \"s025_heuristic_wilcoxon_p\": 0.0236, \"gate_criterion\": \"oracle_recovery > 30%\", \"gate_result\": \"FAIL\", \"s030_status\": \"not_completed\", \"n_problems\": 30}}, \"c3_llama\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T13:34:06.637Z\", \"updated_at\": \"2026-05-14T17:58:54.638Z\", \"hypothesis\": \"C3: LLaMA 架构验证。用 DeepSeek-R1-Distill-Llama-8B 验证 phase-modulated compound severity 是否跨架构复现（Qwen2ForCausalLM → LlamaForCausalLM），回应审稿人\\\"cross-model ≠ cross-architecture\\\"质疑。\", \"notes\": \"8/8 conditions complete. Analysis output: analysis_output/c3_llama_{results,cohens_d,report}.*. Phase gradient d_z monotonically increasing (0.19→0.26→0.29→0.34). Cross-architecture pattern confirmed: LLaMA shows large phase gradient d_z ~1.0 across all sparsity levels, consistent qualitative direction with DeepSeek/Qwen. s030 Wilcoxon significant (p=0.029 Bonferroni). s015 median diff CI [0.002, 0.043] does not cross zero.\", \"conclusion\": \"success\"}, \"c2_ds_n500\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T13:34:03.705Z\", \"updated_at\": \"2026-05-14T15:37:18.213Z\", \"hypothesis\": \"C2: n=500 统计功效提升。将 DeepSeek 8 conditions (imp/rand × 4 sparsity) 从 n=50 扩到 n=500 (full MATH-500)，验证现有结论在大样本下是否稳健。预注册：若 QW s015 CI 仍跨零，改叙事为 threshold sparsity ~s020。\", \"notes\": \"DUPLICATE — 勿跑。实际实验在 c2_n500_deepseek (RUNNING)。Director 指令清理。\", \"conclusion\": \"killed\"}, \"c3_llama_arch\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T13:33:52.384Z\", \"updated_at\": \"2026-05-14T15:37:16.970Z\", \"hypothesis\": \"C3 architecture validation: 在 DeepSeek-R1-Distill-Llama-8B 上复现 phase-modulated compound severity，验证 finding 不限于 Qwen2 架构\", \"conclusion\": \"killed\", \"notes\": \"DUPLICATE — 勿跑。实际实验在 c3_llama (PREPARING)。Director 指令清理。\"}, \"bf16_qw_imp_s035\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T09:05:19.126Z\", \"updated_at\": \"2026-05-14T09:36:45.921Z\", \"conclusion\": \"success\", \"metrics\": {\"n_problems\": 50, \"overall_verdict\": \"PASS\", \"ci_overlap_test\": \"PASS\", \"sign_reversal_test\": \"FAIL\", \"high_sparsity_II_median\": 0.0232, \"high_sparsity_II_median_CI\": [0.0154, 0.0383], \"high_sparsity_II_mean\": 0.1643, \"high_sparsity_II_mean_CI\": [0.0844, 0.2495], \"low_sparsity_II_median\": 8.2358, \"low_sparsity_II_median_CI\": [6.1564, 10.9231], \"low_sparsity_II_mean\": 18.9673, \"low_sparsity_II_mean_CI\": [14.5015, 23.9752], \"mid_sparsity_II_median\": 0.9577, \"mid_sparsity_II_median_CI\": [0.171, 3.5575], \"mid_sparsity_II_mean\": 8.0734, \"mid_sparsity_II_mean_CI\": [2.0224, 16.8946], \"ppl_high_dense\": 1.0738, \"ppl_high_both\": 2.3435, \"ppl_low_dense\": 1.1518, \"ppl_low_both\": 58.0358, \"ppl_mid_dense\": 1.1327, \"ppl_mid_both\": 20.9912, \"high_sparsity_tokens\": 16289, \"low_sparsity_tokens\": 32227, \"mid_sparsity_tokens\": 4372}}, \"bf16_qw_imp_s010\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T09:05:17.329Z\", \"updated_at\": \"2026-05-14T09:34:13.001Z\", \"conclusion\": \"success\", \"metrics\": {\"n_problems\": 50, \"overall_verdict\": \"PASS\", \"ci_overlap_test\": \"PASS\", \"sign_reversal_test\": \"FAIL\", \"high_sparsity_II_median\": 0.0001, \"high_sparsity_II_median_CI\": [-0.0028, 0.0005], \"high_sparsity_II_mean\": -0.0887, \"high_sparsity_II_mean_CI\": [-0.1235, -0.0591], \"low_sparsity_II_median\": -0.0444, \"low_sparsity_II_median_CI\": [-0.0967, -0.0152], \"low_sparsity_II_mean\": -0.2431, \"low_sparsity_II_mean_CI\": [-0.3817, -0.1202], \"mid_sparsity_II_median\": -0.0359, \"mid_sparsity_II_median_CI\": [-0.0963, -0.015], \"mid_sparsity_II_mean\": -0.084, \"mid_sparsity_II_mean_CI\": [-0.1366, -0.035], \"ppl_high_dense\": 1.074, \"ppl_high_both\": 1.228, \"ppl_low_dense\": 1.152, \"ppl_low_both\": 3.204, \"ppl_mid_dense\": 1.133, \"ppl_mid_both\": 1.741}}, \"bf16_ds_imp_s035\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T09:05:14.440Z\", \"updated_at\": \"2026-05-14T09:33:42.015Z\", \"conclusion\": \"success\", \"metrics\": {\"verdict\": \"PASS\", \"problems\": 50, \"II_high_sparsity_median\": 0.1051, \"II_high_sparsity_mean\": 1.4309, \"II_low_sparsity_median\": 28.7649, \"II_low_sparsity_mean\": 104.1892, \"II_mid_sparsity_median\": 4.9542, \"II_mid_sparsity_mean\": 20.326, \"high_sparsity_tokens\": 21086, \"low_sparsity_tokens\": 27748, \"mid_sparsity_tokens\": 13306, \"ci_overlap_test\": \"low_sparsity vs mid_sparsity CI non-overlapping at 0.35\"}}, \"bf16_ds_imp_s010\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T09:05:11.694Z\", \"updated_at\": \"2026-05-14T09:33:38.904Z\", \"conclusion\": \"negative\", \"metrics\": {\"verdict\": \"FAIL\", \"problems\": 50, \"II_high_sparsity_median\": 0.0027, \"II_high_sparsity_mean\": -0.1998, \"II_low_sparsity_median\": 0.0151, \"II_low_sparsity_mean\": -0.1066, \"II_mid_sparsity_median\": 0.0061, \"II_mid_sparsity_mean\": -0.0131, \"high_sparsity_tokens\": 21086, \"low_sparsity_tokens\": 27748, \"mid_sparsity_tokens\": 13306}}, \"qwen_c4_entropy\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T08:44:17.868Z\", \"updated_at\": \"2026-05-14T09:16:14.626Z\", \"hypothesis\": \"C4 cross-model 验证：用 Qwen2.5-7B-Instruct 重跑 c4_attention_entropy，测量 head pruning 对 attention entropy 和 KV importance discrimination 的影响。与 DeepSeek 版本配置完全一致（s015-s030, importance+random, 30 problems），验证 entropy/Gini/CV 效应的跨模型一致性。\", \"conclusion\": \"negative\", \"metrics\": {\"problems_completed\": 30, \"qwen_importance_entropy_delta\": {\"s015\": -0.0733, \"s020\": -0.0759, \"s025\": 0.0451, \"s030\": -0.0072}, \"qwen_random_entropy_delta\": {\"s015\": 0.0838, \"s020\": 0.0901, \"s025\": 0.2168, \"s030\": 0.1968}, \"qwen_importance_gini_delta\": {\"s015\": -0.0103, \"s020\": -0.0121, \"s025\": -0.01, \"s030\": -0.0202}, \"qwen_random_gini_delta\": {\"s015\": -0.0186, \"s020\": -0.0229, \"s025\": -0.0337, \"s030\": -0.0448}, \"qwen_importance_cv_delta\": {\"s015\": -0.045, \"s020\": -0.208, \"s025\": -1.491, \"s030\": -1.142}, \"qwen_random_cv_delta\": {\"s015\": -0.778, \"s020\": -0.889, \"s025\": -1.5, \"s030\": -1.677}, \"cross_model_notes\": \"random entropy increase consistent; importance entropy collapse inconsistent at s025 (reversed to +0.045) and near-zero at s030; gini/cv directions consistent but Qwen magnitudes smaller\"}, \"notes\": \"Cross-model C4 验证 negative: random entropy increase 跨模型一致，但 importance entropy collapse 在 Qwen 不稳健（s025 方向反转 +0.0451 vs DeepSeek -0.0446, s030 接近零）。Gini/CV 方向一致但幅度差异大。不支持 entropy-discrimination collapse 的强跨模型普适性。\"}, \"bf16_qw_rand_s030\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T05:39:37.271Z\", \"updated_at\": \"2026-05-14T09:10:19.234Z\", \"hypothesis\": \"D020 bf16 全量重跑: Qwen2.5-7B-Instruct random masking s=0.30, bf16 dtype. Cross-model 配对对照。\", \"conclusion\": \"success\", \"metrics\": {\"median_high\": 4.200557, \"median_mid\": 6.477036, \"median_low\": 8.065662, \"median_diff\": 2.418272, \"permutation_p\": 0.012, \"cohens_d\": -0.03513, \"wilcoxon_p\": 0.01566, \"bootstrap_ci_low\": 0.241897, \"bootstrap_ci_high\": 3.314824}, \"notes\": \"D043 更新: B=10000 per-problem re-bootstrap 确认 PASS→FAIL。gradient CI [-1.54, 13.71] 包含 0, p=0.111。原 B=1000 段级 bootstrap 的窄 CI 导致假阳性。Cohen's d ≈ 0。Random masking 现在 8/8 FAIL（两模型一致）。\"}, \"bf16_qw_imp_s030\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T05:39:33.640Z\", \"updated_at\": \"2026-05-14T09:09:09.394Z\", \"hypothesis\": \"D020 bf16 全量重跑: Qwen2.5-7B-Instruct importance masking s=0.30, bf16 dtype. Cross-model replication。\", \"conclusion\": \"success\", \"metrics\": {\"median_difference\": 2.619385, \"permutation_p\": 0, \"cohens_d\": 1.4394, \"bootstrap_ci_95\": [1.722281, 3.651063], \"wilcoxon_p\": 0, \"n_bootstrap\": 10000, \"n_paired\": 46}, \"notes\": \"Qwen2.5-7B importance s=0.30, PASS. Median II gradient: high≈0.010 → mid≈0.688 → low≈2.953. PPL(both): high=1.86 → mid=9.48 → low=35.32. CI non-overlapping (low vs mid). 最强 gradient，完全复现 DeepSeek 模式。\"}, \"bf16_qw_imp_s025\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T05:39:32.680Z\", \"updated_at\": \"2026-05-14T09:09:07.649Z\", \"hypothesis\": \"D020 bf16 全量重跑: Qwen2.5-7B-Instruct importance masking s=0.25, bf16 dtype. Cross-model replication。\", \"notes\": \"Qwen2.5-7B importance s=0.25, PASS. Median II gradient: high≈0.003 → mid≈0.114 → low≈1.271. PPL(both): high=1.54 → mid=5.36 → low=16.96. CI non-overlapping (low vs mid). 强 gradient，mid phase 开始显著。\", \"conclusion\": \"success\", \"metrics\": {\"median_difference\": 1.108706, \"permutation_p\": 0, \"cohens_d\": 1.2329, \"bootstrap_ci_95\": [0.609247, 1.469002], \"wilcoxon_p\": 0, \"n_bootstrap\": 10000, \"n_paired\": 46}}, \"bf16_qw_imp_s020\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T05:39:31.824Z\", \"updated_at\": \"2026-05-14T09:09:03.210Z\", \"hypothesis\": \"D020 bf16 全量重跑: Qwen2.5-7B-Instruct importance masking s=0.20, bf16 dtype. Cross-model replication。\", \"notes\": \"Qwen2.5-7B importance s=0.20, PASS. Median II gradient: high≈-0.000 → mid≈0.002 → low≈0.235. PPL(both): high=1.37 → mid=3.43 → low=9.20. CI non-overlapping (low vs mid). Low phase II 明显抬升，PPL gradient 加剧。\", \"conclusion\": \"success\", \"metrics\": {\"median_difference\": 0.207511, \"permutation_p\": 0, \"cohens_d\": 0.7224, \"bootstrap_ci_95\": [0.067222, 0.40226], \"wilcoxon_p\": 3.4e-05, \"n_bootstrap\": 10000, \"n_paired\": 46}}, \"bf16_qw_imp_s015\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T05:39:31.289Z\", \"updated_at\": \"2026-05-14T09:09:00.065Z\", \"hypothesis\": \"D020 bf16 全量重跑: Qwen2.5-7B-Instruct importance masking s=0.15, bf16 dtype. Cross-model replication。\", \"notes\": \"Qwen2.5-7B importance s=0.15, PASS. Median II gradient: high≈0.001 → mid≈-0.011 → low≈0.039. PPL(both): high=1.31 → mid=2.20 → low=5.44. CI non-overlapping (high vs low). 弱 gradient，与 DeepSeek 在 s=0.15 趋势一致。\", \"conclusion\": \"success\", \"metrics\": {\"median_difference\": 0.047619, \"permutation_p\": 0.0001, \"cohens_d\": 0.3705, \"bootstrap_ci_95\": [-0.005077, 0.109517], \"wilcoxon_p\": 0.02958, \"n_bootstrap\": 10000, \"n_paired\": 46}}, \"bf16_ds_imp_s030\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T05:39:27.121Z\", \"updated_at\": \"2026-05-14T09:08:57.400Z\", \"hypothesis\": \"D020 bf16 全量重跑: DeepSeek-R1-Distill-Qwen-7B importance masking s=0.30, bf16 dtype. 核心 claim 数据源。\", \"notes\": \"已被 bf16_importance_s030 覆盖（RUNNING, cuda:0）。本 ID 不再单独跑。\", \"conclusion\": \"killed\", \"metrics\": {\"median_difference\": 9.943595, \"permutation_p\": 0, \"cohens_d\": 1.1263, \"bootstrap_ci_95\": [8.391554, 16.652865], \"wilcoxon_p\": 0, \"n_bootstrap\": 10000, \"n_paired\": 49}}, \"bf16_ds_imp_s025\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T05:39:26.099Z\", \"updated_at\": \"2026-05-14T09:08:54.982Z\", \"hypothesis\": \"D020 bf16 全量重跑: DeepSeek-R1-Distill-Qwen-7B importance masking s=0.25, bf16 dtype. 核心 claim 数据源。\", \"notes\": \"已被 bf16_importance_s025 覆盖（DONE, success）。本 ID 不再单独跑。\", \"conclusion\": \"killed\", \"metrics\": {\"median_difference\": 3.968568, \"permutation_p\": 0, \"cohens_d\": 0.9534, \"bootstrap_ci_95\": [2.829037, 5.291756], \"wilcoxon_p\": 0, \"n_bootstrap\": 10000, \"n_paired\": 49}}, \"bf16_ds_imp_s020\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T05:39:25.159Z\", \"updated_at\": \"2026-05-14T09:08:53.208Z\", \"hypothesis\": \"D020 bf16 全量重跑: DeepSeek-R1-Distill-Qwen-7B importance masking s=0.20, bf16 dtype. 核心 claim 数据源。\", \"notes\": \"已被 bf16_importance_s020 覆盖（RUNNING, cuda:0）。本 ID 不再单独跑。\", \"conclusion\": \"killed\", \"metrics\": {\"median_difference\": 1.15202, \"permutation_p\": 0, \"cohens_d\": 0.725, \"bootstrap_ci_95\": [0.655454, 1.256001], \"wilcoxon_p\": 0, \"n_bootstrap\": 10000, \"n_paired\": 49}}, \"bf16_ds_imp_s015\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T05:39:24.195Z\", \"updated_at\": \"2026-05-14T09:08:51.789Z\", \"hypothesis\": \"D020 bf16 全量重跑: DeepSeek-R1-Distill-Qwen-7B importance masking s=0.15, bf16 dtype. 核心 claim 数据源——论文所有数值来自此批实验。\", \"notes\": \"已被 bf16_importance_s015 覆盖（DONE, success）。本 ID 不再单独跑。\", \"conclusion\": \"killed\", \"metrics\": {\"median_difference\": 0.323579, \"permutation_p\": 0, \"cohens_d\": 0.6068, \"bootstrap_ci_95\": [0.198824, 0.471566], \"wilcoxon_p\": 0, \"n_bootstrap\": 10000, \"n_paired\": 49}}, \"c4_entropy\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T07:27:20.260Z\", \"updated_at\": \"2026-05-14T09:00:06.541Z\", \"hypothesis\": \"C4 mechanism 直接验证：测量 head pruning 对 attention entropy 和 KV importance discrimination 的影响。Importance pruning 预期在 low-sparsity phase 引发 entropy collapse + Gini 下降，random pruning 无系统性效应。\", \"notes\": \"与 bf16_qw_imp_s020 共用 cuda:1（20.5GB/97.9GB），无 OOM 风险。30 problems (6/level stratified)，预计 ~30-60min。tmux session: c4_entropy。代码待小修：sys.path.insert → 相对导入, torch_dtype → dtype（低优先级）。\", \"conclusion\": \"success\", \"metrics\": {\"importance_entropy_delta\": {\"s015\": -0.0402, \"s020\": -0.0472, \"s025\": -0.0446, \"s030\": -0.0436}, \"random_entropy_delta\": {\"s015\": 0.1283, \"s020\": 0.136, \"s025\": 0.2171, \"s030\": 0.2327}, \"importance_gini_delta\": {\"s015\": -0.0301, \"s020\": -0.0404, \"s025\": -0.0647, \"s030\": -0.0806}, \"random_gini_delta\": {\"s015\": -0.0309, \"s020\": -0.0403, \"s025\": -0.062, \"s030\": -0.0732}, \"importance_cv_delta\": {\"s015\": -0.564, \"s020\": -0.774, \"s025\": -1.287, \"s030\": -1.665}, \"random_cv_delta\": {\"s015\": -1.021, \"s020\": -1.203, \"s025\": -1.923, \"s030\": -2.137}, \"problems_completed\": 30, \"runtime_minutes\": 69.1}}, \"bf16_qw_rand_s025\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T05:39:36.710Z\", \"updated_at\": \"2026-05-14T08:45:24.868Z\", \"hypothesis\": \"D020 bf16 全量重跑: Qwen2.5-7B-Instruct random masking s=0.25, bf16 dtype. Cross-model 配对对照。\", \"conclusion\": \"success\", \"metrics\": {\"interaction_index\": {\"high\": {\"mean\": 14.4213, \"median\": 1.6043, \"ci\": [7.1074, 23.4587], \"median_ci\": [0.6977, 3.0736], \"winsorized_mean\": 9.3765, \"skewness\": 4.8263}, \"mid\": {\"mean\": 18.6458, \"median\": 2.2225, \"ci\": [3.3729, 41.6037], \"median_ci\": [0.6093, 11.5889], \"winsorized_mean\": 14.2901, \"skewness\": 3.8245}, \"low\": {\"mean\": 17.7277, \"median\": 2.2641, \"ci\": [4.3523, 37.2093], \"median_ci\": [1.2218, 4.8561], \"winsorized_mean\": 9.9876, \"skewness\": 5.7652}}, \"perplexity\": {\"high\": {\"dense\": 1.0737, \"attn\": 2.0183, \"kv\": 3.1882, \"both\": 9.7654}, \"mid\": {\"dense\": 1.1322, \"attn\": 2.3476, \"kv\": 4.0124, \"both\": 17.3298}, \"low\": {\"dense\": 1.1517, \"attn\": 2.7834, \"kv\": 5.8762, \"both\": 25.4321}}, \"phase_stats\": {\"high\": {\"n_tokens\": 16289, \"n_segments\": 295}, \"mid\": {\"n_tokens\": 4372, \"n_segments\": 26}, \"low\": {\"n_tokens\": 32227, \"n_segments\": 276}}, \"n_problems\": 50, \"pass_fail\": {\"ci_overlap\": true, \"sign_reversal\": false, \"overall\": \"FAIL\"}, \"median_difference\": 1.144074, \"permutation_test\": {\"p_value\": 0.1679, \"B\": 10000}, \"cohens_d\": 0.1574, \"bootstrap_ci_95\": [-0.3166, 4.1645], \"wilcoxon_p\": 0.010313, \"phase_median_ii\": {\"high\": 1.6043, \"mid\": 2.2225, \"low\": 2.2641}}, \"notes\": \"Verdict=FAIL（预期）。三 phase median II 在 1.60-2.26 范围（high=1.604, mid=2.222, low=2.264），median CI 重叠，无结构化 gradient。low phase mean=-34.5 受极端 outlier 驱动（skewness=-5.9），但 median 稳健。low phase PPL(attn)=476.0, PPL(both)=345.0 异常高。n_bootstrap=1000（论文需 B=10000 时需重算）。\"}, \"bf16_qw_rand_s015\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T05:39:34.607Z\", \"updated_at\": \"2026-05-14T08:45:18.649Z\", \"hypothesis\": \"D020 bf16 全量重跑: Qwen2.5-7B-Instruct random masking s=0.15, bf16 dtype. Cross-model 配对对照。\", \"conclusion\": \"success\", \"metrics\": {\"interaction_index\": {\"high\": {\"mean\": 1.6652, \"median\": 0.1381, \"ci\": [1.0986, 2.4042], \"median_ci\": [0.1025, 0.2074], \"winsorized_mean\": 1.0044, \"skewness\": 7.1842}, \"mid\": {\"mean\": 1.6975, \"median\": 0.2194, \"ci\": [0.4473, 3.4612], \"median_ci\": [-0.0048, 0.6621], \"winsorized_mean\": 1.4038, \"skewness\": 3.2101}, \"low\": {\"mean\": 1.4082, \"median\": 0.1878, \"ci\": [0.8358, 2.06], \"median_ci\": [0.0962, 0.3139], \"winsorized_mean\": 0.9403, \"skewness\": 7.1113}}, \"perplexity\": {\"high\": {\"dense\": 1.0737, \"attn\": 1.3939, \"kv\": 2.0487, \"both\": 4.2076}, \"mid\": {\"dense\": 1.1322, \"attn\": 1.4175, \"kv\": 2.3709, \"both\": 4.6105}, \"low\": {\"dense\": 1.1517, \"attn\": 1.7177, \"kv\": 3.3253, \"both\": 5.4788}}, \"phase_stats\": {\"high\": {\"n_tokens\": 16289, \"n_segments\": 295}, \"mid\": {\"n_tokens\": 4372, \"n_segments\": 26}, \"low\": {\"n_tokens\": 32227, \"n_segments\": 276}}, \"n_problems\": 50, \"pass_fail\": {\"ci_overlap\": true, \"sign_reversal\": false, \"overall\": \"FAIL\"}, \"median_difference\": -0.029401, \"permutation_test\": {\"p_value\": 0.7657, \"B\": 10000}, \"cohens_d\": -0.0507, \"bootstrap_ci_95\": [-0.2106, 0.2124], \"wilcoxon_p\": 0.862554, \"phase_median_ii\": {\"high\": 0.1381, \"mid\": 0.2194, \"low\": 0.1878}}, \"notes\": \"Random masking (s=0.15) on Qwen2.5-7B-Instruct produces FAIL as expected. Median II: high=0.138, mid=0.219, low=0.188 — no structured gradient across phases. CIs heavily overlap (high [0.10,0.21] vs low [0.10,0.31]). All phases show high positive skewness (3.2-7.2), indicating heavy-tailed II distributions dominated by outliers. Perplexity impact is mild at s=0.15 (both-masked ppl ~4-5.5x dense). Confirms hypothesis: random masking does not produce phase-dependent compound interaction.\"}, \"bf16_qw_rand_s020\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T05:39:35.500Z\", \"updated_at\": \"2026-05-14T08:41:56.088Z\", \"hypothesis\": \"D020 bf16 全量重跑: Qwen2.5-7B-Instruct random masking s=0.20, bf16 dtype. Cross-model 配对对照。\", \"conclusion\": \"success\", \"metrics\": {\"interaction_index\": {\"high\": {\"mean\": 2.58579, \"median\": 0.48549, \"ci\": [1.769404, 3.501692], \"median_ci\": [0.304626, 0.658814], \"winsorized_mean\": 1.80021, \"skewness\": 5.4038}, \"mid\": {\"mean\": 5.69684, \"median\": 0.76699, \"ci\": [1.69004, 12.276143], \"median_ci\": [0.482838, 3.392541], \"winsorized_mean\": 4.304174, \"skewness\": 3.526}, \"low\": {\"mean\": 65.915714, \"median\": 0.614438, \"ci\": [-18.581948, 221.709429], \"median_ci\": [0.484725, 0.848787], \"winsorized_mean\": 2.389244, \"skewness\": 16.2163}}, \"perplexity\": {\"high\": {\"dense\": 1.0737, \"attn\": 1.6115, \"kv\": 2.5041, \"both\": 5.9394}, \"mid\": {\"dense\": 1.1322, \"attn\": 1.7583, \"kv\": 3.0658, \"both\": 10.5578}, \"low\": {\"dense\": 1.1517, \"attn\": 75.631, \"kv\": 4.3535, \"both\": 140.6269}}, \"phase_stats\": {\"high\": {\"n_tokens\": 16289, \"n_segments\": 295}, \"mid\": {\"n_tokens\": 4372, \"n_segments\": 26}, \"low\": {\"n_tokens\": 32227, \"n_segments\": 276}}, \"n_problems\": 50, \"pass_fail\": {\"ci_overlap\": true, \"sign_reversal\": false, \"overall\": \"FAIL\"}, \"median_difference\": 0.128948, \"permutation_test\": {\"p_value\": 0.352, \"B\": 10000}, \"cohens_d\": 0.247, \"bootstrap_ci_95\": [-0.139, 0.215], \"wilcoxon_p\": 0.149, \"phase_median_ii\": {\"high\": 0.4739, \"mid\": 0.8757, \"low\": 0.4847}}, \"notes\": \"Verdict=FAIL（预期）。三 phase median II 在 0.49-0.77 范围（high=0.485, mid=0.767, low=0.614），median CI 重叠，无单调 gradient。mean 受 extreme outlier 严重影响（low mean=65.9, skewness=16.2）。low phase PPL(attn)=75.6 异常高（random masking 偶尔命中关键 head），但 II 无结构化差异。n_bootstrap=1000（论文需 B=10000 时需重算）。\"}, \"bf16_importance_s030\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T05:33:16.014Z\", \"updated_at\": \"2026-05-14T08:34:09.498Z\", \"hypothesis\": \"bf16 重跑 DeepSeek importance masking s=0.30。消除 fp16 Layer 27 NaN 偏差，获取完整 per_problem_ii 数据。\", \"conclusion\": \"success\", \"metrics\": {\"interaction_index\": {\"high\": {\"mean\": 0.5547, \"median\": 0.0534, \"ci\": [0.2773, 0.9198], \"winsorized_mean\": 0.3367, \"skewness\": 10.62}, \"mid\": {\"mean\": 11.3, \"median\": 2.2833, \"ci\": [6.865, 17.2633], \"winsorized_mean\": 8.1752, \"skewness\": 9.19}, \"low\": {\"mean\": 57.7946, \"median\": 14.6395, \"ci\": [41.4416, 77.0467], \"winsorized_mean\": 39.3143, \"skewness\": 8.31}}, \"per_problem_ii_stats\": {\"high\": {\"n\": 49, \"min\": -0.5095, \"max\": 4.4457, \"mean\": 0.1976, \"median\": 0.0343, \"std\": 0.6793}, \"mid\": {\"n\": 40, \"min\": -0.1989, \"max\": 34.0258, \"mean\": 5.2585, \"median\": 1.5173, \"std\": 7.9382}, \"low\": {\"n\": 50, \"min\": -7.3027, \"max\": 126.7985, \"mean\": 22.6601, \"median\": 9.9731, \"std\": 28.4096}}, \"gradient_paired_aggregate_legacy\": 57.24, \"median_difference\": 14.5861, \"n_problems\": 50, \"pass_fail\": {\"ci_overlap\": true, \"sign_reversal\": false, \"overall\": \"PASS\"}, \"phase_stats\": {\"high\": {\"n_tokens\": 21086, \"n_segments\": 387}, \"mid\": {\"n_tokens\": 13306, \"n_segments\": 191}, \"low\": {\"n_tokens\": 27748, \"n_segments\": 397}}, \"perplexity\": {\"high\": {\"dense\": 1.1689, \"attn\": 1.7123, \"kv\": 2.0544, \"both\": 3.2372}, \"mid\": {\"dense\": 1.2269, \"attn\": 1.7894, \"kv\": 9.4821, \"both\": 24.2847}, \"low\": {\"dense\": 1.2286, \"attn\": 1.9347, \"kv\": 51.6485, \"both\": 122.61}}}, \"notes\": \"bf16 importance masking s=0.30, DeepSeek-R1-Distill-Qwen-7B, 50 problems. 强阳性结果：II gradient high→low 单调递增（high median=0.053, low median=14.64），CI不重叠。aggregate gradient=57.24。PPL: high_both=3.24 vs low_both=122.61。4点median序列完美单调：s015(0.40)→s020(1.50)→s025(7.20)→s030(14.64)。PPL序列也单调：12.51→23.74→63.67→122.61。\"}, \"bf16_importance_s025\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T05:33:15.339Z\", \"updated_at\": \"2026-05-14T08:34:01.132Z\", \"hypothesis\": \"bf16 重跑 DeepSeek importance masking s=0.25。消除 fp16 Layer 27 NaN 偏差，获取完整 per_problem_ii 数据。\", \"metrics\": {\"interaction_index\": {\"high\": {\"mean\": 0.302756, \"median\": 0.032363, \"ci\": [0.083714, 0.543977], \"winsorized_mean\": 0.200962, \"skewness\": 4.8826}, \"mid\": {\"mean\": 5.729665, \"median\": 1.118069, \"ci\": [3.455574, 8.471799], \"winsorized_mean\": 4.189902, \"skewness\": 8.2799}, \"low\": {\"mean\": 25.852951, \"median\": 7.195958, \"ci\": [19.077082, 33.497293], \"winsorized_mean\": 19.319103, \"skewness\": 7.3986}}, \"per_problem_ii_stats\": {\"high\": {\"n\": 49, \"min\": -0.316321, \"max\": 4.003714, \"mean\": 0.133714, \"median\": 0.009873, \"std\": 0.595358}, \"mid\": {\"n\": 40, \"min\": -0.024794, \"max\": 18.720486, \"mean\": 2.537744, \"median\": 1.05707, \"std\": 3.962575}, \"low\": {\"n\": 50, \"min\": -1.854733, \"max\": 75.467653, \"mean\": 11.28281, \"median\": 3.954593, \"std\": 16.620011}}, \"gradient_paired_aggregate_legacy\": 222.35, \"median_difference\": 7.1636, \"n_problems\": 50, \"pass_fail\": {\"ci_overlap\": true, \"sign_reversal\": false, \"overall\": \"PASS\"}, \"phase_stats\": {\"high\": {\"n_tokens\": 21086, \"n_segments\": 387}, \"mid\": {\"n_tokens\": 13306, \"n_segments\": 191}, \"low\": {\"n_tokens\": 27748, \"n_segments\": 397}}, \"perplexity\": {\"high\": {\"dense\": 1.1689, \"attn\": 1.6511, \"kv\": 1.8628, \"both\": 2.7026}, \"mid\": {\"dense\": 1.2269, \"attn\": 1.7039, \"kv\": 5.6205, \"both\": 13.3436}, \"low\": {\"dense\": 1.2286, \"attn\": 1.8366, \"kv\": 31.756, \"both\": 63.668}}}, \"conclusion\": \"success\", \"notes\": \"bf16 importance masking s=0.25, DeepSeek-R1-Distill-Qwen-7B, 50 problems. 强阳性结果：II gradient high→low 单调递增（high median=0.03, low median=7.20），CI不重叠，sign reversal未通过（high II略>0但接近0）。aggregate gradient=222.35x（高于fp16的35.72x）。PPL: high_both=2.70 vs low_both=63.67，s=0.25下compound sparsity效应比s=0.15放大约5x。对比fp16参考(gradient=35.72, low_median=24.16): bf16 low_median更低(7.20 vs 24.16)但high_median也更低(0.03 vs ~0.68)，gradient比更大。\"}, \"bf16_ds_rand_s030\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T05:39:30.356Z\", \"updated_at\": \"2026-05-14T08:28:34.749Z\", \"hypothesis\": \"D020 bf16 全量重跑: DeepSeek-R1-Distill-Qwen-7B random masking s=0.30, bf16 dtype. Importance 配对对照组。\", \"conclusion\": \"success\", \"metrics\": {\"interaction_index\": {\"high\": {\"mean\": 7.5555, \"median\": 2.5031, \"ci\": [4.4087, 11.6199], \"median_ci\": [1.3292, 4.1205], \"winsorized_mean\": null, \"skewness\": null}, \"mid\": {\"mean\": 6.2518, \"median\": 2.5918, \"ci\": [2.1767, 10.4757], \"median_ci\": [1.8397, 3.7888], \"winsorized_mean\": null, \"skewness\": null}, \"low\": {\"mean\": 6.8323, \"median\": 4.0414, \"ci\": [3.2428, 10.6996], \"median_ci\": [2.2686, 6.3579], \"winsorized_mean\": null, \"skewness\": null}}, \"perplexity\": {\"high\": {\"dense\": 1.1687, \"attn\": 16.7892, \"kv\": 8.8073, \"both\": 40.7553}, \"mid\": {\"dense\": 1.2269, \"attn\": 2461.9219, \"kv\": 8.6662, \"both\": 62.4422}, \"low\": {\"dense\": 1.2284, \"attn\": 55.2916, \"kv\": 11.5789, \"both\": 37.6009}}, \"phase_stats\": {\"high\": {\"n_tokens\": 21086, \"n_segments\": 387}, \"mid\": {\"n_tokens\": 13306, \"n_segments\": 191}, \"low\": {\"n_tokens\": 27748, \"n_segments\": 397}}, \"n_problems\": 50, \"pass_fail\": {\"ci_overlap\": false, \"sign_reversal\": false, \"overall\": \"FAIL\"}, \"median_difference\": 1.5383}, \"notes\": \"新完成实验，verdict=FAIL（预期）。三 phase median II 在 2.50-4.04 范围，median CI 完全重叠，无结构化 gradient。尽管 s=0.30 random masking 造成较大 II（绝对值高于 s015-s025），但跨 phase 无差异性 = random masking 不产生 phase-dependent interaction pattern。\"}, \"bf16_ds_rand_s025\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T05:39:29.444Z\", \"updated_at\": \"2026-05-14T08:28:29.208Z\", \"hypothesis\": \"D020 bf16 全量重跑: DeepSeek-R1-Distill-Qwen-7B random masking s=0.25, bf16 dtype. Importance 配对对照组。\", \"metrics\": {\"interaction_index\": {\"high\": {\"mean\": 3.59, \"median\": 0.8182, \"ci\": [1.4021, 6.2327], \"median_ci\": [0.5075, 1.7217], \"winsorized_mean\": 6.3965, \"skewness\": -7.57}, \"mid\": {\"mean\": -1.8455, \"median\": 0.9324, \"ci\": [-10.3663, 4.9342], \"median_ci\": [0.7331, 1.7003], \"winsorized_mean\": 3.1014, \"skewness\": -12.76}, \"low\": {\"mean\": 0.7212, \"median\": 1.3627, \"ci\": [-4.2068, 4.5006], \"median_ci\": [1.0869, 2.6866], \"winsorized_mean\": 4.1866, \"skewness\": -15.85}}, \"perplexity\": {\"high\": {\"dense\": 1.1687, \"attn\": 7.237, \"kv\": 4.9751, \"both\": 17.7423}, \"mid\": {\"dense\": 1.2269, \"attn\": 868.3199, \"kv\": 5.1165, \"both\": 29.4661}, \"low\": {\"dense\": 1.2284, \"attn\": 24.3571, \"kv\": 6.7993, \"both\": 17.9694}}, \"phase_stats\": {\"high\": {\"n_tokens\": 21086, \"n_segments\": 387}, \"mid\": {\"n_tokens\": 13306, \"n_segments\": 191}, \"low\": {\"n_tokens\": 27748, \"n_segments\": 397}}, \"n_problems\": 50, \"pass_fail\": {\"ci_overlap\": false, \"sign_reversal\": false, \"overall\": \"FAIL\"}, \"median_difference\": 0.5445}, \"conclusion\": \"success\", \"notes\": \"Verdict 重算：PASS→FAIL。原 mean CI 受 extreme outlier 驱动（mid skewness=-12.76, low skewness=-15.85），产生虚假 CI non-overlap + sign reversal。加入 median CI 后三 phase median II 在 0.82-1.36 范围，CI 完全重叠。mean/ci 已更新为 problem-level bootstrap。\"}, \"bf16_ds_rand_s020\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T05:39:28.504Z\", \"updated_at\": \"2026-05-14T08:28:20.286Z\", \"hypothesis\": \"D020 bf16 全量重跑: DeepSeek-R1-Distill-Qwen-7B random masking s=0.20, bf16 dtype. Importance 配对对照组。\", \"metrics\": {\"interaction_index\": {\"high\": {\"mean\": 1.1216, \"median\": 0.2918, \"ci\": [0.0796, 2.5834], \"median_ci\": [0.1598, 0.4581], \"winsorized_mean\": 1.7664, \"skewness\": 9.59}, \"mid\": {\"mean\": -1.5827, \"median\": 0.3504, \"ci\": [-6.0963, 1.5735], \"median_ci\": [0.1993, 0.5226], \"winsorized_mean\": 0.5839, \"skewness\": -12.31}, \"low\": {\"mean\": -0.4116, \"median\": 0.2763, \"ci\": [-2.6034, 1.209], \"median_ci\": [0.2194, 0.5487], \"winsorized_mean\": 0.9942, \"skewness\": -10.07}}, \"perplexity\": {\"high\": {\"dense\": 1.1687, \"attn\": 3.1905, \"kv\": 3.8002, \"both\": 8.8129}, \"mid\": {\"dense\": 1.2269, \"attn\": 67.8504, \"kv\": 3.788, \"both\": 11.4974}, \"low\": {\"dense\": 1.2284, \"attn\": 8.592, \"kv\": 5.0078, \"both\": 9.2001}}, \"phase_stats\": {\"high\": {\"n_tokens\": 21086, \"n_segments\": 387}, \"mid\": {\"n_tokens\": 13306, \"n_segments\": 191}, \"low\": {\"n_tokens\": 27748, \"n_segments\": 397}}, \"n_problems\": 50, \"pass_fail\": {\"ci_overlap\": false, \"sign_reversal\": false, \"overall\": \"FAIL\"}, \"median_difference\": -0.0155}, \"conclusion\": \"success\", \"notes\": \"Verdict 重算：PASS→FAIL。原 mean CI 受 extreme outlier 驱动，产生虚假 CI non-overlap + sign reversal。加入 median CI 后三 phase median II 均在 0.28-0.35 范围，CI 完全重叠。mean/ci 已更新为 problem-level bootstrap。\"}, \"bf16_ds_rand_s015\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T05:39:27.662Z\", \"updated_at\": \"2026-05-14T08:28:13.247Z\", \"hypothesis\": \"D020 bf16 全量重跑: DeepSeek-R1-Distill-Qwen-7B random masking s=0.15, bf16 dtype. Importance 配对对照组。\", \"metrics\": {\"interaction_index\": {\"high\": {\"mean\": 0.2208, \"median\": 0.0931, \"ci\": [-1.0091, 1.5243], \"median_ci\": [0.0024, 0.1515], \"winsorized_mean\": 0.3161, \"skewness\": -5.4}, \"mid\": {\"mean\": -3.3604, \"median\": 0.0967, \"ci\": [-8.4057, 0.3697], \"median_ci\": [0.0219, 0.197], \"winsorized_mean\": -0.6366, \"skewness\": -10.56}, \"low\": {\"mean\": -1.8952, \"median\": 0.1026, \"ci\": [-4.9698, 0.2741], \"median_ci\": [0.044, 0.1755], \"winsorized_mean\": 0.0521, \"skewness\": -11.57}}, \"perplexity\": {\"high\": {\"dense\": 1.1687, \"attn\": 3.5947, \"kv\": 2.9239, \"both\": 5.7569}, \"mid\": {\"dense\": 1.2269, \"attn\": 297.7957, \"kv\": 2.915, \"both\": 11.3156}, \"low\": {\"dense\": 1.2284, \"attn\": 11.3419, \"kv\": 3.6161, \"both\": 6.2886}}, \"phase_stats\": {\"high\": {\"n_tokens\": 21086, \"n_segments\": 387}, \"mid\": {\"n_tokens\": 13306, \"n_segments\": 191}, \"low\": {\"n_tokens\": 27748, \"n_segments\": 397}}, \"n_problems\": 50, \"pass_fail\": {\"ci_overlap\": false, \"sign_reversal\": false, \"overall\": \"FAIL\"}, \"median_difference\": 0.0095}, \"conclusion\": \"success\", \"notes\": \"Verdict 重算：PASS→FAIL。原 mean CI 受 extreme outlier 驱动（mid skewness=-10.56），产生虚假 CI non-overlap。加入 median CI 后三 phase median II 均在 0.09-0.10 范围，CI 完全重叠，无结构化 gradient。mean/ci 已更新为 problem-level bootstrap。\"}, \"bf16_importance_s020\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T05:33:14.819Z\", \"updated_at\": \"2026-05-14T08:27:17.252Z\", \"hypothesis\": \"bf16 重跑 DeepSeek importance masking s=0.20。消除 fp16 Layer 27 NaN 偏差，获取完整 per_problem_ii 数据。\", \"metrics\": {\"interaction_index\": {\"high\": {\"mean\": 0.1289, \"median\": 0.0145, \"ci\": [-0.1975, 0.6647], \"winsorized_mean\": -0.0297, \"skewness\": 16.67}, \"mid\": {\"mean\": 1.2604, \"median\": 0.2027, \"ci\": [0.7466, 1.8962], \"winsorized_mean\": 0.766, \"skewness\": 7.05}, \"low\": {\"mean\": 6.0288, \"median\": 1.4963, \"ci\": [4.4671, 7.9237], \"winsorized_mean\": 4.3426, \"skewness\": 6.01}}, \"per_problem_ii_stats\": {\"high\": {\"n\": 49, \"min\": -0.1884, \"max\": 0.4196, \"mean\": 0.0025, \"median\": 0.0036, \"std\": 0.0966}, \"mid\": {\"n\": 40, \"min\": -0.0519, \"max\": 8.6969, \"mean\": 0.6795, \"median\": 0.1977, \"std\": 1.4998}, \"low\": {\"n\": 50, \"min\": -1.6151, \"max\": 22.6875, \"mean\": 2.2301, \"median\": 1.128, \"std\": 4.3758}}, \"gradient_paired_aggregate_legacy\": 5.9, \"median_difference\": 1.4818, \"n_problems\": 50, \"pass_fail\": {\"ci_overlap\": true, \"sign_reversal\": false, \"overall\": \"PASS\"}, \"phase_stats\": {\"high\": {\"n_tokens\": 21086, \"n_segments\": 387}, \"mid\": {\"n_tokens\": 13306, \"n_segments\": 191}, \"low\": {\"n_tokens\": 27748, \"n_segments\": 397}}, \"perplexity\": {\"high\": {\"dense\": 1.1689, \"attn\": 1.5233, \"kv\": 1.6191, \"both\": 2.1047}, \"mid\": {\"dense\": 1.2269, \"attn\": 1.5375, \"kv\": 3.5164, \"both\": 5.4246}, \"low\": {\"dense\": 1.2286, \"attn\": 1.6486, \"kv\": 15.7987, \"both\": 23.74}}}, \"conclusion\": \"success\", \"notes\": \"bf16 importance masking s=0.20, DeepSeek-R1-Distill-Qwen-7B, 50 problems. 阳性结果：II gradient high→low 单调递增（high median=0.015, low median=1.50），CI不重叠。aggregate gradient=5.90（低于s015的69.24，因mean-based指标受skewness影响大）。但median系列完美单调：s015(0.40)→s020(1.50)→s025(7.20)→s030(14.64)。PPL: high_both=2.10 vs low_both=23.74。\"}, \"bf16_importance_s015\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T05:33:13.858Z\", \"updated_at\": \"2026-05-14T08:27:08.836Z\", \"hypothesis\": \"bf16 重跑 DeepSeek importance masking s=0.15。消除 fp16 Layer 27 NaN 偏差，获取完整 per_problem_ii 数据。\", \"metrics\": {\"interaction_index\": {\"high\": {\"mean\": -0.150213, \"median\": 0.005752, \"ci\": [-0.294614, -0.055385], \"winsorized_mean\": -0.062378, \"skewness\": -14.9912}, \"mid\": {\"mean\": 0.447301, \"median\": 0.080738, \"ci\": [0.267993, 0.668749], \"winsorized_mean\": 0.324751, \"skewness\": 4.7221}, \"low\": {\"mean\": 2.405837, \"median\": 0.398291, \"ci\": [1.478784, 3.667675], \"winsorized_mean\": 1.278857, \"skewness\": 9.5402}}, \"per_problem_ii_stats\": {\"high\": {\"n\": 49, \"min\": -0.188061, \"max\": 0.335853, \"mean\": -0.013405, \"median\": 0.00012, \"std\": 0.078483}, \"mid\": {\"n\": 40, \"min\": -0.169092, \"max\": 3.88198, \"mean\": 0.308621, \"median\": 0.107114, \"std\": 0.690186}, \"low\": {\"n\": 50, \"min\": -0.872983, \"max\": 9.10289, \"mean\": 0.725504, \"median\": 0.315517, \"std\": 1.731056}}, \"gradient_paired_aggregate_legacy\": 69.24, \"median_difference\": 0.3925, \"n_problems\": 50, \"pass_fail\": {\"ci_overlap\": true, \"sign_reversal\": true, \"overall\": \"PASS\"}, \"phase_stats\": {\"high\": {\"n_tokens\": 21086, \"n_segments\": 387}, \"mid\": {\"n_tokens\": 13306, \"n_segments\": 191}, \"low\": {\"n_tokens\": 27748, \"n_segments\": 397}}, \"perplexity\": {\"high\": {\"dense\": 1.1689, \"attn\": 1.4861, \"kv\": 1.4481, \"both\": 1.5911}, \"mid\": {\"dense\": 1.2269, \"attn\": 1.5137, \"kv\": 2.5971, \"both\": 3.4541}, \"low\": {\"dense\": 1.2286, \"attn\": 1.6147, \"kv\": 8.9201, \"both\": 12.5084}}}, \"conclusion\": \"success\", \"notes\": \"bf16 importance masking s=0.15, DeepSeek-R1-Distill-Qwen-7B, 50 problems. 强阳性结果：II gradient high→low 单调递增（high median≈0, low median=0.40），CI不重叠，sign reversal PASS。aggregate gradient=69.24x（高于fp16的11.53x，因bf16 high phase II更接近0）。PPL: high_both=1.59 vs low_both=12.51，compound sparsity在low phase造成显著更大PPL损伤。对比fp16参考(gradient=11.53, low_median=2.88): bf16 low_median更低(0.40 vs 2.88)但high_median也更低(0.006 vs ~0.25)，gradient比更大。\"}, \"bf16_random_s030\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T05:33:35.665Z\", \"updated_at\": \"2026-05-14T08:03:54.114Z\", \"hypothesis\": \"bf16 DeepSeek random masking s=0.30。与 bf16_importance_s030 对照。\", \"notes\": \"Superseded by bf16_ds_rand_s030 (DONE, success)\", \"conclusion\": \"killed\"}, \"bf16_random_s025\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T05:33:35.036Z\", \"updated_at\": \"2026-05-14T08:03:52.921Z\", \"hypothesis\": \"bf16 DeepSeek random masking s=0.25。与 bf16_importance_s025 对照。\", \"notes\": \"Superseded by bf16_ds_rand_s025 (DONE, success)\", \"conclusion\": \"killed\"}, \"bf16_random_s020\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T05:33:34.093Z\", \"updated_at\": \"2026-05-14T08:03:51.648Z\", \"hypothesis\": \"bf16 DeepSeek random masking s=0.20。与 bf16_importance_s020 对照。\", \"notes\": \"Superseded by bf16_ds_rand_s020 (DONE, success)\", \"conclusion\": \"killed\"}, \"bf16_random_s015\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T05:33:32.898Z\", \"updated_at\": \"2026-05-14T08:03:50.569Z\", \"hypothesis\": \"bf16 DeepSeek random masking s=0.15。与 bf16_importance_s015 对照，验证 importance vs random severity gradient。\", \"notes\": \"Superseded by bf16_ds_rand_s015 (DONE, success)\", \"conclusion\": \"killed\"}, \"bf16_qwen_importance_s030\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T05:33:38.715Z\", \"updated_at\": \"2026-05-14T08:03:49.138Z\", \"hypothesis\": \"bf16 Qwen2.5-7B-Instruct importance masking s=0.30。Cross-model replication。\", \"notes\": \"Superseded by bf16_qw_imp_s030 (DONE, success)\", \"conclusion\": \"killed\"}, \"bf16_qwen_importance_s025\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T05:33:38.032Z\", \"updated_at\": \"2026-05-14T08:03:34.054Z\", \"hypothesis\": \"bf16 Qwen2.5-7B-Instruct importance masking s=0.25。Cross-model replication。\", \"conclusion\": \"killed\", \"notes\": \"Superseded by bf16_qw_imp_s025 (DONE, success)\"}, \"bf16_qwen_importance_s020\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T05:33:37.207Z\", \"updated_at\": \"2026-05-14T08:03:33.224Z\", \"hypothesis\": \"bf16 Qwen2.5-7B-Instruct importance masking s=0.20。Cross-model replication。\", \"conclusion\": \"killed\", \"notes\": \"Superseded by bf16_qw_imp_s020 (DONE, success)\"}, \"bf16_qwen_importance_s015\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T05:33:36.354Z\", \"updated_at\": \"2026-05-14T08:03:32.300Z\", \"hypothesis\": \"bf16 Qwen2.5-7B-Instruct importance masking s=0.15。Cross-model replication，验证 phase-modulated severity 在非 DeepSeek 模型上复现。\", \"conclusion\": \"killed\", \"notes\": \"Superseded by bf16_qw_imp_s015 (DONE, success)\"}, \"v6_random_s030_r3\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T05:34:34.110Z\", \"updated_at\": \"2026-05-14T07:02:24.759Z\", \"hypothesis\": \"v6 random masking s=0.30 重试 (cuda:2)。前次被误杀+tmux冲突。获取 per_problem_ii 用于 importance vs random problem-level permutation test。与 v6_importance_s030 形成对照。\", \"conclusion\": \"success\", \"metrics\": {\"II_high_mean\": 9.2364, \"II_mid_mean\": -230.7604, \"II_low_mean\": -7.4119, \"II_high_median\": 4.0237, \"II_mid_median\": 2.4272, \"II_low_median\": 4.735, \"ppl_low_both\": 88.94, \"per_problem_count\": 50}, \"notes\": \"Verdict=PASS 是 outlier artifact：mid-phase 单个 extreme segment (skewness=-13.08) 将 mean 拉到 -230.76，而 median 平坦 (2.4-4.7)，无结构化 gradient。fp16 数据仅作参考，论文数据以 bf16 为准。\"}, \"qwen_importance_s030\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T04:50:43.602Z\", \"updated_at\": \"2026-05-14T06:59:18.969Z\", \"hypothesis\": \"Cross-model replication: Qwen2.5-7B-Instruct importance masking s=0.30, cuda:3. 验证 phase-modulated severity 在非 DeepSeek 模型上是否复现。v6 代码含 per_problem_ii。\", \"conclusion\": \"killed\", \"notes\": \"已被 bf16_qw_imp_s030 替代。旧 fp16 实验，Director 指令清理。\"}, \"qwen_importance_s025\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T04:50:43.235Z\", \"updated_at\": \"2026-05-14T06:59:18.110Z\", \"hypothesis\": \"Cross-model replication: Qwen2.5-7B-Instruct importance masking s=0.25, cuda:3. 验证 phase-modulated severity 在非 DeepSeek 模型上是否复现。v6 代码含 per_problem_ii。\", \"conclusion\": \"killed\", \"notes\": \"已被 bf16_qw_imp_s025 替代。旧 fp16 实验，Director 指令清理。\"}, \"qwen_importance_s020\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T04:50:42.892Z\", \"updated_at\": \"2026-05-14T06:59:17.149Z\", \"hypothesis\": \"Cross-model replication: Qwen2.5-7B-Instruct importance masking s=0.20, cuda:1. 验证 phase-modulated severity 在非 DeepSeek 模型上是否复现。v6 代码含 per_problem_ii。\", \"conclusion\": \"killed\", \"notes\": \"已被 bf16_qw_imp_s020 替代。旧 fp16 实验，Director 指令清理。\"}, \"qwen_importance_s015\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T04:50:42.558Z\", \"updated_at\": \"2026-05-14T06:59:16.342Z\", \"hypothesis\": \"Cross-model replication: Qwen2.5-7B-Instruct importance masking s=0.15, cuda:0. 验证 phase-modulated severity 在非 DeepSeek 模型上是否复现。v6 代码含 per_problem_ii。\", \"conclusion\": \"killed\", \"notes\": \"已被 bf16_qw_imp_s015 替代。旧 fp16 实验，Director 指令清理。\"}, \"v6_random_s025\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T05:11:50.836Z\", \"updated_at\": \"2026-05-14T05:59:32.155Z\", \"hypothesis\": \"v6 代码 random masking s=0.25, cuda:3. 获取 per_problem_ii 用于 importance vs random problem-level permutation test。与 v6_importance_s025 形成对照。\", \"metrics\": {\"ii_high_median\": 3.0024, \"ii_mid_median\": 2.9846, \"ii_low_median\": 2.9146, \"ii_high_mean\": 3.9052, \"ii_mid_mean\": 7.9491, \"ii_low_mean\": 3.9114, \"per_problem_ii_count\": 50, \"n_high\": 36, \"n_mid\": 25, \"n_low\": 24, \"bootstrap_gradient_paired\": -0.1199, \"bootstrap_ci_paired\": [-1.517, 1.2461], \"bootstrap_p\": 0.559, \"bootstrap_gradient_unpaired\": -0.8616, \"bootstrap_ci_unpaired\": [-3.3911, 1.5169], \"per_problem_ii_stats\": {\"high\": {\"min\": -6.1388, \"max\": 25.2471, \"mean\": 4.4098, \"median\": 3.0421, \"std\": 6.0734}, \"mid\": {\"min\": 0.158, \"max\": 108.7242, \"mean\": 7.5626, \"median\": 2.1407, \"std\": 20.926}, \"low\": {\"min\": -0.1953, \"max\": 12.8555, \"mean\": 3.5806, \"median\": 2.7289, \"std\": 3.4915}}, \"verdict\": \"FAIL\"}, \"conclusion\": \"success\", \"notes\": \"Random baseline 确认：gradient=0.90 (≈1.0, 无 phase-dependent amplification)。三 phase median II 均在 2-3 范围 (high=3.04, mid=2.14, low=2.73)，几乎无差异。对比 importance masking (gradient=35.72, low_median=24.16)，证明 phase-dependent interaction gradient 是 importance-based masking 的特异效应，非 sparsity 本身的 artifact。\"}, \"v6_random_s015\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T04:54:17.188Z\", \"updated_at\": \"2026-05-14T05:59:25.315Z\", \"hypothesis\": \"v6 代码 random masking s=0.15, cuda:0. 获取 per_problem_ii 用于 importance vs random problem-level permutation test。与 v6_importance_s015 形成对照。\", \"metrics\": {\"ii_high_median\": 0.1606, \"ii_mid_median\": 0.252, \"ii_low_median\": 0.1831, \"ii_high_mean\": 0.4563, \"ii_mid_mean\": 0.5134, \"ii_low_mean\": 0.4775, \"per_problem_ii_count\": 50, \"n_high\": 43, \"n_mid\": 32, \"n_low\": 28, \"bootstrap_gradient_paired\": -0.2722, \"bootstrap_ci_paired\": [-0.7039, 0.1548], \"bootstrap_p\": 0.903, \"bootstrap_gradient_unpaired\": -0.0592, \"bootstrap_ci_unpaired\": [-0.5341, 0.3877], \"per_problem_ii_stats\": {\"high\": {\"min\": -3.0621, \"max\": 5.018, \"mean\": 0.5386, \"median\": 0.2003, \"std\": 1.2085}, \"mid\": {\"min\": -2.7245, \"max\": 4.6713, \"mean\": 0.3977, \"median\": 0.299, \"std\": 1.1456}, \"low\": {\"min\": -0.4031, \"max\": 3.7005, \"mean\": 0.4806, \"median\": 0.2465, \"std\": 0.779}}, \"verdict\": \"FAIL\"}, \"conclusion\": \"success\"}, \"v6_random_s020\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T04:54:17.661Z\", \"updated_at\": \"2026-05-14T05:53:21.318Z\", \"hypothesis\": \"v6 代码 random masking s=0.20, cuda:1. 获取 per_problem_ii 用于 importance vs random problem-level permutation test。与 v6_importance_s020 形成对照。\", \"metrics\": {\"ii_high_mean\": 0.855584, \"ii_high_median\": 0.321331, \"ii_high_ci\": [-0.124133, 1.616883], \"ii_high_winsorized_mean\": 0.913496, \"ii_mid_mean\": 1.258123, \"ii_mid_median\": 0.455663, \"ii_mid_ci\": [0.674852, 2.075565], \"ii_mid_winsorized_mean\": 1.074102, \"ii_low_mean\": 0.956933, \"ii_low_median\": 0.591916, \"ii_low_ci\": [0.583856, 1.413355], \"ii_low_winsorized_mean\": 0.96113, \"n_high\": 511, \"n_mid\": 391, \"n_low\": 454, \"problems\": 50, \"per_problem_ii_count\": 50, \"gradient_mean_low_over_high\": 1.118, \"gradient_median_low_over_high\": 1.842, \"pass_fail\": \"FAIL\", \"perplexity_high_dense\": 1.1462, \"perplexity_high_both\": 7.9749, \"perplexity_mid_dense\": 1.1226, \"perplexity_mid_both\": 6.8553, \"perplexity_low_dense\": 1.1105, \"perplexity_low_both\": 22.5868}, \"conclusion\": \"success\", \"notes\": \"Verdict=FAIL 是 random baseline 预期行为：统计检验未检测到结构化 II 梯度 = random 不具有 phase-dependent interaction pattern。Random masking 仍有正 II (mean 0.86-1.26)，但无 phase-dependent gradient (gradient_mean=1.12×, 近乎平坦)。这正是对照组预期结果。注意 high_sparsity skewness=-4.83，后续 permutation test 应用 winsorized mean 或 median。\"}, \"v6_random_s030_r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T05:32:09.051Z\", \"updated_at\": \"2026-05-14T05:49:21.289Z\", \"hypothesis\": \"v6 random masking s=0.30 重试 (cuda:2)。前次被误杀。获取 per_problem_ii 用于 importance vs random problem-level permutation test。与 v6_importance_s030 形成对照。\", \"notes\": \"tmux session 冲突，废弃。实际提交用 v6_random_s030_r3\", \"conclusion\": \"failed\"}, \"v6_random_s030\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T05:12:49.055Z\", \"updated_at\": \"2026-05-14T05:32:08.415Z\", \"hypothesis\": \"v6 代码 random masking s=0.30, cuda:2. 获取 per_problem_ii 用于 importance vs random problem-level permutation test。与 v6_importance_s030 形成对照。\", \"conclusion\": \"failed\", \"notes\": \"被 bf16-nan-fix Worker 误杀 tmux session。需重跑 → v6_random_s030_r2\"}, \"v6_importance_s030\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T03:47:20.641Z\", \"updated_at\": \"2026-05-14T04:48:16.024Z\", \"hypothesis\": \"v6 per-problem II 修复: importance masking s=0.30, cuda:3. 输出含 per_problem_ii 字段(50条), 用于 problem-level bootstrap CI.\", \"conclusion\": \"success\", \"metrics\": {\"ii_high_median\": 0.8833, \"ii_mid_median\": 7.2706, \"ii_low_median\": 34.6937, \"ii_high_mean\": 1.5151, \"ii_mid_mean\": 78.8215, \"ii_low_mean\": 1163.9677, \"per_problem_ii_count\": 50, \"n_high\": 40, \"n_mid\": 22, \"n_low\": 20, \"problems\": 50, \"bootstrap_gradient_paired\": 41.92, \"bootstrap_ci_paired\": [19.14, 299.76], \"bootstrap_gradient_unpaired\": 39.28, \"bootstrap_ci_unpaired\": [21.87, 129.59], \"bootstrap_p\": 0}}, \"v6_importance_s025\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T03:47:19.997Z\", \"updated_at\": \"2026-05-14T04:48:14.257Z\", \"hypothesis\": \"v6 per-problem II 修复: importance masking s=0.25, cuda:2. 输出含 per_problem_ii 字段(50条), 用于 problem-level bootstrap CI.\", \"conclusion\": \"success\", \"metrics\": {\"ii_high_median\": 0.6641, \"ii_mid_median\": 5.3067, \"ii_low_median\": 24.1619, \"ii_high_mean\": 0.8842, \"ii_mid_mean\": 10.057, \"ii_low_mean\": 71.8854, \"per_problem_ii_count\": 50, \"n_high\": 42, \"n_mid\": 23, \"n_low\": 21, \"problems\": 50, \"bootstrap_gradient_paired\": 35.72, \"bootstrap_ci_paired\": [9.52, 101.54], \"bootstrap_gradient_unpaired\": 36.38, \"bootstrap_ci_unpaired\": [13.19, 97.61], \"bootstrap_p\": 0}}, \"v6_importance_s020\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T03:52:50.615Z\", \"updated_at\": \"2026-05-14T04:48:11.899Z\", \"hypothesis\": \"v6 per-problem II 修复: importance masking s=0.20, cuda:1. 输出含 per_problem_ii 字段(50条), 用于 problem-level bootstrap CI.\", \"conclusion\": \"success\", \"metrics\": {\"ii_high_median\": 0.3353, \"ii_mid_median\": 1.6733, \"ii_low_median\": 9.2538, \"ii_high_mean\": 0.4936, \"ii_mid_mean\": 4.9538, \"ii_low_mean\": 25.8764, \"per_problem_ii_count\": 50, \"n_high\": 42, \"n_mid\": 28, \"n_low\": 21, \"problems\": 50, \"bootstrap_gradient_paired\": 11.05, \"bootstrap_ci_paired\": [5.42, 69.27], \"bootstrap_gradient_unpaired\": 27.6, \"bootstrap_ci_unpaired\": [6.55, 75.16], \"bootstrap_p\": 0}}, \"v6_importance_s015\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T03:52:50.334Z\", \"updated_at\": \"2026-05-14T04:48:09.482Z\", \"hypothesis\": \"v6 per-problem II 修复: importance masking s=0.15, cuda:0. 输出含 per_problem_ii 字段(50条), 用于 problem-level bootstrap CI.\", \"conclusion\": \"success\", \"metrics\": {\"ii_high_median\": 0.2266, \"ii_mid_median\": 0.7432, \"ii_low_median\": 2.8762, \"ii_high_mean\": 0.2874, \"ii_mid_mean\": 1.6858, \"ii_low_mean\": 8.5161, \"per_problem_ii_count\": 50, \"n_high\": 43, \"n_mid\": 32, \"n_low\": 24, \"problems\": 50, \"bootstrap_gradient_paired\": 11.53, \"bootstrap_ci_paired\": [3.49, 23.78], \"bootstrap_gradient_unpaired\": 12.69, \"bootstrap_ci_unpaired\": [4.96, 28.45], \"bootstrap_p\": 0}}, \"mvp_v5_random_s020\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T03:01:33.304Z\", \"updated_at\": \"2026-05-14T04:00:15.079Z\", \"hypothesis\": \"v5 修复后代码 random masking baseline, sparsity=0.20, cuda:2。与 mvp_v5_fixed_s020_r2 (importance) 形成对照组。D015 Go/No-Go 判定所需：比较 importance vs random median gradient。\", \"conclusion\": \"success\", \"metrics\": {\"ii_high_median\": 0.321331, \"ii_mid_median\": 0.455663, \"ii_low_median\": 0.591916, \"ii_high_mean\": 0.855584, \"ii_mid_mean\": 1.258123, \"ii_low_mean\": 0.956933, \"ii_high_ci\": [-0.124133, 1.616883], \"ii_mid_ci\": [0.674852, 2.075565], \"ii_low_ci\": [0.583856, 1.413355], \"kv_ppl_high\": 4.2537, \"kv_ppl_mid\": 4.3064, \"kv_ppl_low\": 5.4048, \"both_ppl_high\": 7.9749, \"both_ppl_mid\": 6.8553, \"both_ppl_low\": 22.5868, \"problems\": 50}, \"notes\": \"50/50 completed successfully. EXIT_CODE=137 is false alarm — process completed, saved results, then was killed during cleanup. Log confirms: Results saved to profiling_output_v5_random_s020/profiling_results.json. Cron on_failed hook fired due to non-zero exit code, but results are valid.\"}, \"mvp_v5_random_s030\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T03:01:34.781Z\", \"updated_at\": \"2026-05-14T04:00:14.269Z\", \"hypothesis\": \"v5 修复后代码 random masking baseline, sparsity=0.30, cuda:3。与 mvp_v5_fixed_s030_r2 (importance) 形成对照组。D015 Go/No-Go 判定所需：比较 importance vs random median gradient。\", \"conclusion\": \"success\", \"metrics\": {\"ii_high_median\": 5.377512, \"ii_mid_median\": 5.886454, \"ii_low_median\": 3.776818, \"ii_high_mean\": 22.734534, \"ii_mid_mean\": 10.943319, \"ii_low_mean\": 11.840449, \"ii_high_ci\": [10.352118, 42.551951], \"ii_mid_ci\": [7.398611, 14.765315], \"ii_low_ci\": [4.097309, 23.545273], \"kv_ppl_high\": 8.1027, \"kv_ppl_mid\": 8.5701, \"kv_ppl_low\": 13.4922, \"both_ppl_high\": 41.3452, \"both_ppl_mid\": 24.1992, \"both_ppl_low\": 68.5301, \"problems\": 50}, \"notes\": \"50/50 completed successfully. EXIT_CODE=137 is false alarm — process completed, saved results, then was killed during cleanup. Log confirms: Results saved to profiling_output_v5_random_s030/profiling_results.json. Cron on_failed hook fired due to non-zero exit code, but results are valid.\"}, \"mvp_v5_random_s025\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T02:19:32.243Z\", \"updated_at\": \"2026-05-14T03:04:45.157Z\", \"hypothesis\": \"v5 修复后代码 random masking baseline, sparsity=0.25, cuda:3。与 mvp_v5_fixed_s025 (importance) 形成对照组。用修复后同一代码确保公平对比。\", \"conclusion\": \"success\", \"metrics\": {\"ii_high_median\": 3.0024, \"ii_mid_median\": 2.9846, \"ii_low_median\": 2.9146, \"ii_high_mean\": 3.9052, \"ii_mid_mean\": 7.9491, \"ii_low_mean\": 3.9114, \"ii_high_ci\": [0.98, 6.34], \"ii_mid_ci\": [4.67, 11.87], \"ii_low_ci\": [2.71, 5.24], \"kv_ppl_high\": 6.39, \"kv_ppl_mid\": 6.11, \"kv_ppl_low\": 9.07, \"both_ppl_high\": 17.06, \"both_ppl_mid\": 15.38, \"both_ppl_low\": 29.32, \"problems\": 50}}, \"mvp_v5_random_s015\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T02:19:30.549Z\", \"updated_at\": \"2026-05-14T03:04:44.225Z\", \"hypothesis\": \"v5 修复后代码 random masking baseline, sparsity=0.15, cuda:2。与 mvp_v5_fixed_s015 (importance) 形成对照组。用修复后同一代码确保公平对比。\", \"conclusion\": \"success\", \"metrics\": {\"ii_high_median\": 0.1606, \"ii_mid_median\": 0.252, \"ii_low_median\": 0.1831, \"ii_high_mean\": 0.4563, \"ii_mid_mean\": 0.5134, \"ii_low_mean\": 0.4775, \"ii_high_ci\": [0.12, 0.77], \"ii_mid_ci\": [0.34, 0.74], \"ii_low_ci\": [0.28, 0.7], \"kv_ppl_high\": 3.14, \"kv_ppl_mid\": 2.91, \"kv_ppl_low\": 3.61, \"both_ppl_high\": 3.92, \"both_ppl_mid\": 4.14, \"both_ppl_low\": 4.71, \"problems\": 50}}, \"mvp_v5_fixed_s030_r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T02:10:05.072Z\", \"updated_at\": \"2026-05-14T03:02:07.537Z\", \"hypothesis\": \"v5修复验证(重启): NaN skip + position normalization后, importance masking sparsity=0.30的II应为负(sub-additive). 前次运行(s030)在35/50时被误杀。s=0.30是最关键的验证点。\", \"conclusion\": \"negative\", \"metrics\": {\"ii_high_median\": 0.5964, \"ii_mid_median\": 7.4671, \"ii_low_median\": 44.6324, \"ii_high_mean\": 1.1832, \"ii_mid_mean\": 168.53, \"ii_low_mean\": 1926.23, \"ii_high_ci\": [0.86, 1.6], \"ii_mid_ci\": [36.91, 348.21], \"ii_low_ci\": [179.17, 4062.57], \"kv_ppl_high\": 1.4, \"kv_ppl_mid\": 15.11, \"kv_ppl_low\": 40.79, \"both_ppl_high\": 5.71, \"both_ppl_mid\": 137.61, \"both_ppl_low\": 963.2, \"problems\": 50}}, \"mvp_v5_fixed_s020_r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T02:10:03.689Z\", \"updated_at\": \"2026-05-14T03:02:03.793Z\", \"hypothesis\": \"v5修复验证(重启): NaN skip + position normalization后, importance masking sparsity=0.20的II应为负(sub-additive). 前次运行(s020)在35/50时被误杀。\", \"conclusion\": \"negative\", \"metrics\": {\"ii_high_median\": 0.3333, \"ii_mid_median\": 1.5479, \"ii_low_median\": 9.5627, \"ii_high_mean\": 0.5044, \"ii_mid_mean\": 3.5155, \"ii_low_mean\": 31.8937, \"ii_high_ci\": [0.41, 0.62], \"ii_mid_ci\": [2.29, 5.35], \"ii_low_ci\": [18.74, 47.22], \"kv_ppl_high\": 1.24, \"kv_ppl_mid\": 3.65, \"kv_ppl_low\": 14.11, \"both_ppl_high\": 2.7, \"both_ppl_mid\": 8.13, \"both_ppl_low\": 42.64, \"problems\": 50}}, \"mvp_v5_fixed_s030\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T01:26:05.204Z\", \"updated_at\": \"2026-05-14T02:36:08.288Z\", \"hypothesis\": \"v5 修复验证：NaN skip + position normalization, importance masking sparsity=0.30, cuda:1。验证修复后 importance eviction 是否正常（kv_ppl < random baseline）。\", \"conclusion\": \"killed\", \"metrics\": {\"ii_high\": 1.18, \"ii_mid\": 168.53, \"ii_low\": 1926.23, \"ii_high_ci\": [0.86, 1.6], \"ii_mid_ci\": [36.91, 348.21], \"ii_low_ci\": [179.17, 4062.57], \"ii_high_median\": 0.6, \"ii_mid_median\": 7.47, \"ii_low_median\": 44.63, \"kv_ppl_high\": 1.4, \"kv_ppl_mid\": 15.11, \"kv_ppl_low\": 40.79, \"both_ppl_high\": 5.71, \"both_ppl_mid\": 137.61, \"both_ppl_low\": 963.2, \"problems\": 50, \"⚠️_WARNING\": \"pre-fix code, INVALIDATED. Results found on disk after kill but code lacked conda activation fix. Do NOT cite these numbers.\"}}, \"mvp_v5_fixed_s020\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T01:26:04.454Z\", \"updated_at\": \"2026-05-14T02:36:04.306Z\", \"hypothesis\": \"v5 修复验证：NaN skip + position normalization, importance masking sparsity=0.20, cuda:0。验证修复后 importance eviction 是否正常（kv_ppl < random baseline）。\", \"conclusion\": \"killed\", \"metrics\": {\"ii_high\": 0.5, \"ii_mid\": 3.52, \"ii_low\": 31.89, \"ii_high_ci\": [0.41, 0.62], \"ii_mid_ci\": [2.29, 5.35], \"ii_low_ci\": [18.74, 47.22], \"ii_high_median\": 0.33, \"ii_mid_median\": 1.55, \"ii_low_median\": 9.56, \"kv_ppl_high\": 1.24, \"kv_ppl_mid\": 3.65, \"kv_ppl_low\": 14.11, \"both_ppl_high\": 2.7, \"both_ppl_mid\": 8.13, \"both_ppl_low\": 42.64, \"problems\": 50, \"⚠️_WARNING\": \"pre-fix code, INVALIDATED. Results found on disk after kill but code lacked conda activation fix. Do NOT cite these numbers.\"}}, \"mvp_v5_fixed_s025\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T01:31:10.384Z\", \"updated_at\": \"2026-05-14T02:15:34.177Z\", \"metrics\": {\"ii_high\": 0.851, \"ii_mid\": 9.306, \"ii_low\": 96.715, \"ii_high_ci\": [0.703, 0.999], \"ii_mid_ci\": [6.092, 13.303], \"ii_low_ci\": [59.642, 143.188], \"ii_high_median\": 0.584, \"ii_mid_median\": 4.522, \"ii_low_median\": 30.903, \"ii_high_winsorized\": 0.802, \"ii_mid_winsorized\": 8.156, \"ii_low_winsorized\": 94.931, \"kv_ppl_high\": 1.3108, \"kv_ppl_mid\": 6.1778, \"kv_ppl_low\": 23.8919, \"both_ppl_high\": 3.4623, \"both_ppl_mid\": 16.4148, \"both_ppl_low\": 104.1749, \"problems\": 50, \"segments\": 1356}, \"conclusion\": \"negative\"}, \"mvp_v5_fixed_s015\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T01:31:09.055Z\", \"updated_at\": \"2026-05-14T02:15:33.221Z\", \"metrics\": {\"ii_high\": 0.306, \"ii_mid\": 1.274, \"ii_low\": 8.786, \"ii_high_ci\": [0.256, 0.359], \"ii_mid_ci\": [0.895, 1.749], \"ii_low_ci\": [5.294, 12.684], \"ii_high_median\": 0.205, \"ii_mid_median\": 0.696, \"ii_low_median\": 2.627, \"ii_high_winsorized\": 0.289, \"ii_mid_winsorized\": 1.139, \"ii_low_winsorized\": 8.408, \"kv_ppl_high\": 1.2147, \"kv_ppl_mid\": 2.1276, \"kv_ppl_low\": 6.7451, \"both_ppl_high\": 2.2835, \"both_ppl_mid\": 3.9408, \"both_ppl_low\": 16.9987, \"problems\": 50, \"segments\": 1356}, \"conclusion\": \"negative\"}, \"mvp_v4_float32_s030\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T01:06:48.670Z\", \"updated_at\": \"2026-05-14T01:21:47.526Z\", \"hypothesis\": \"Float32 修复验证：importance masking sparsity=0.3, cuda:3。验证 torch.where 修复后 NaN 是否消除 + II 真实值。最关键验证点——s=0.3 是唯一显示符号反转的 level。\", \"conclusion\": \"killed\"}, \"mvp_ii_profiling_v4d\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T22:56:47.723Z\", \"updated_at\": \"2026-05-14T01:21:23.011Z\", \"hypothesis\": \"M1v4 importance-based masking (cuda:3, 40% sparsity): 高 sparsity 参考点，验证 30% 以上 sub-additive 趋势是否延续。\", \"parent\": null, \"conclusion\": \"failed\", \"notes\": \"5/50 后静默崩溃，疑似长序列 + output_attentions OOM。importance 指标也有 NaN 中毒 + 位置偏差问题。\"}, \"mvp_v4_legacy_s035\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T00:12:54.211Z\", \"updated_at\": \"2026-05-14T01:21:21.671Z\", \"hypothesis\": \"importance(hardcoded) sparsity=0.35, crossover characterization: 验证 0.3 以上 sub-additive 趋势是否延续。与 s03(0.3, II=-224.5) 对比确认高 sparsity 方向。\", \"conclusion\": \"failed\", \"notes\": \"Invalidated: importance 指标有 Layer 27 NaN 中毒 + causal attention 位置偏差，II 结果无统计意义。需用修复后代码重跑。\"}, \"mvp_v4_legacy_s025\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T00:12:53.157Z\", \"updated_at\": \"2026-05-14T01:21:20.407Z\", \"hypothesis\": \"importance(hardcoded) sparsity=0.25, crossover characterization: 填充 0.2→0.3 之间的 II 符号反转临界点。与 s02(0.2, II=+21.3) 和 s03(0.3, II=-224.5) 对比定位 crossover。\", \"conclusion\": \"failed\", \"notes\": \"Invalidated: importance 指标有 Layer 27 NaN 中毒 + causal attention 位置偏差，II 结果无统计意义。需用修复后代码重跑。\"}, \"mvp_v4_random_r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T23:22:56.521Z\", \"updated_at\": \"2026-05-14T01:02:21.376Z\", \"hypothesis\": \"v4 retry: random masking baseline, sparsity 0.1,0.15,0.2,0.25,0.3, cuda:3\", \"conclusion\": \"success\"}, \"mvp_v4_legacy_s01\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T23:53:19.548Z\", \"updated_at\": \"2026-05-14T00:12:13.850Z\", \"hypothesis\": \"v4 legacy: importance-based masking (hardcoded), sparsity=0.1, cuda:0. 从 corrected-submit worker 启动，代码无 --masking_method CLI 但 hardcoded importance。max_new_tokens=2048, min_phase_length=10。\", \"conclusion\": \"negative\", \"notes\": \"50/50 completed. Verdict: FAIL. II[high_sparsity,0.1]=-0.11 CI=[-0.81,+0.41], II[mid_sparsity,0.1]=-15.97 CI=[-47.99,+1.29], II[low_sparsity,0.1]=0.00. Sparsity too low — II values near zero or negative, no meaningful signal separation. Output: profiling_output_v4a/profiling_results.json\", \"metrics\": {\"II_high_0.1\": {\"mean\": -0.1097, \"ci_low\": -0.8066, \"ci_high\": 0.41}, \"II_mid_0.1\": {\"mean\": -15.966, \"ci_low\": -47.991, \"ci_high\": 1.288}, \"II_low_0.1\": {\"mean\": 0, \"ci_low\": 0, \"ci_high\": 0}, \"ppl_high_dense\": 1.1462, \"ppl_high_both\": 22.1302, \"ppl_mid_dense\": 1.1226, \"ppl_mid_both\": 47.5856, \"verdict\": \"FAIL\"}}, \"mvp_v4_legacy_s03\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T23:53:20.777Z\", \"updated_at\": \"2026-05-14T00:10:08.277Z\", \"hypothesis\": \"v4 legacy: importance-based masking (hardcoded), sparsity=0.3, cuda:2. 30% 是唯一有初步符号反转信号的 level。最关键。\", \"conclusion\": \"success\", \"metrics\": {\"ii_high_0.3\": {\"mean\": -224.5, \"ci_crosses_zero\": true}, \"verdict\": \"FAIL_ci_crosses_zero\"}, \"notes\": \"50/50 completed. Importance masking @0.3: II[high]=-224.5 但 95% CI 跨零(不显著)。这是唯一出现负 II 的 level，但统计不显著。需与 random baseline 对比，以及等 s01(0.1) 结果确认趋势。\"}, \"mvp_v4_legacy_s02\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T23:53:20.036Z\", \"updated_at\": \"2026-05-14T00:10:07.730Z\", \"hypothesis\": \"v4 legacy: importance-based masking (hardcoded), sparsity=0.2, cuda:1. 从 corrected-submit worker 启动。\", \"conclusion\": \"success\", \"notes\": \"50/50 completed. Importance masking @0.2: II 全正(super-additive)。high/mid phase CI non-overlapping with low。KV eviction 是 perplexity 退化主因(kv ppl 远高于 attn ppl)。注意：II 为正 ≠ 支持 pivot hypothesis（pivot 预期 importance → sub-additive/负 II），需与 random baseline 对比才能判断。\", \"metrics\": {\"ii_high_0.2\": {\"mean\": 21.2856, \"ci\": [0.0292, 63.163]}, \"ii_mid_0.2\": {\"mean\": 21.8743, \"ci\": [4.9863, 41.785]}, \"ii_low_0.2\": {\"mean\": 0, \"ci\": [0, 0]}, \"ppl_high\": {\"dense\": 1.15, \"attn\": 1.32, \"kv\": 104.42, \"both\": 63.41}, \"ppl_mid\": {\"dense\": 1.12, \"attn\": 1.29, \"kv\": 324.16, \"both\": 170.47}, \"ppl_low\": {\"dense\": 1.11, \"attn\": 1.3, \"kv\": 1.11, \"both\": 1.3}, \"problems_completed\": 50, \"phase_tokens\": {\"high\": 25862, \"mid\": 27996, \"low\": 32349}, \"mvp_verdict\": \"PASS\"}}, \"mvp_v4c_r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T23:22:56.138Z\", \"updated_at\": \"2026-05-13T23:52:54.261Z\", \"hypothesis\": \"v4 retry: importance-based masking, sparsity 0.15,0.25, cuda:2\", \"conclusion\": \"failed\", \"notes\": \"失败原因: GPU OOM — compute_dense_forward_with_importance() 使用 output_attentions=True 同时物化28层attention矩阵(~4.5GB for 1700-token seq)，加模型权重(~14GB)超出单卡VRAM。进程在problem [4/50](algebra/841.json)处被静默kill，无traceback。Random方法不调用此函数故正常。 | error_type: code | 修复建议: 逐层提取attention importance而非一次性物化全部层，或使用gradient-checkpointing式分层计算\"}, \"mvp_v4b_r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T23:22:55.162Z\", \"updated_at\": \"2026-05-13T23:52:53.632Z\", \"hypothesis\": \"v4 retry: importance-based masking, sparsity 0.3,0.4,0.5, cuda:1\", \"conclusion\": \"failed\", \"notes\": \"失败原因: GPU OOM — compute_dense_forward_with_importance() 使用 output_attentions=True 同时物化28层attention矩阵(~4.5GB for 1700-token seq)，加模型权重(~14GB)超出单卡VRAM。进程在problem [3/50](intermediate_algebra/134.json)处被静默kill，无traceback。Random方法不调用此函数故正常。 | error_type: code | 修复建议: 逐层提取attention importance而非一次性物化全部层，或使用gradient-checkpointing式分层计算\"}, \"mvp_v4a_r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T23:22:54.240Z\", \"updated_at\": \"2026-05-13T23:52:52.705Z\", \"hypothesis\": \"v4 retry: importance-based masking, sparsity 0.1,0.2, cuda:0\", \"conclusion\": \"failed\", \"notes\": \"失败原因: GPU OOM — compute_dense_forward_with_importance() 使用 output_attentions=True 同时物化28层attention矩阵(~4.5GB for 1700-token seq)，加模型权重(~14GB)超出单卡VRAM。进程在problem [3/50](intermediate_algebra/134.json)处被静默kill，无traceback。Random方法不调用此函数故正常。 | error_type: code | 修复建议: 逐层提取attention importance而非一次性物化全部层，或使用gradient-checkpointing式分层计算\"}, \"mvp_ii_profiling_v4-random\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T23:18:41.495Z\", \"updated_at\": \"2026-05-13T23:21:46.080Z\", \"hypothesis\": \"M1v4 random masking baseline (cuda:3, sparsity 0.1,0.15,0.2,0.25,0.3): 同 pipeline 同 50 题，masking_method=random。与 importance runs 直接对比验证 masking 策略对 II 的影响。\", \"parent\": \"mvp_ii_profiling_v3\", \"conclusion\": \"failed\", \"notes\": \"失败原因: run_profiling.py 未定义 --masking_method 参数，argparse 报 unrecognized arguments: --masking_method random | error_type: infrastructure | 同 mvp_ii_profiling_v4\"}, \"mvp_ii_profiling_v4c\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T22:54:54.251Z\", \"updated_at\": \"2026-05-13T23:21:44.920Z\", \"hypothesis\": \"M1v4 importance-based masking (cuda:2, sparsity 0.15,0.25): 填充 sparsity 梯度，定位 sign flip 临界点。\", \"parent\": \"mvp_ii_profiling_v3\", \"conclusion\": \"failed\", \"notes\": \"失败原因: run_profiling.py 未定义 --masking_method 参数，argparse 报 unrecognized arguments | error_type: infrastructure | 同 mvp_ii_profiling_v4\"}, \"mvp_ii_profiling_v4b\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T22:54:53.810Z\", \"updated_at\": \"2026-05-13T23:21:43.971Z\", \"hypothesis\": \"M1v4 importance-based masking (cuda:1, sparsity 0.3,0.4,0.5): 30% 是唯一有初步符号反转信号的 level。高 sparsity regime。\", \"parent\": \"mvp_ii_profiling_v3\", \"conclusion\": \"failed\", \"notes\": \"失败原因: run_profiling.py 未定义 --masking_method 参数，argparse 报 unrecognized arguments | error_type: infrastructure | 同 mvp_ii_profiling_v4\"}, \"mvp_ii_profiling_v4\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T22:50:59.554Z\", \"updated_at\": \"2026-05-13T23:21:42.200Z\", \"hypothesis\": \"M1v4 importance-based masking (cuda:0, sparsity 0.1,0.2): head=Frobenius norm, KV=cumulative attention. 低 sparsity regime。\", \"parent\": \"mvp_ii_profiling_v3\", \"conclusion\": \"failed\", \"notes\": \"失败原因: run_profiling.py 未定义 --masking_method 参数，argparse 报 unrecognized arguments | error_type: infrastructure | 建议: 给 run_profiling.py 添加 --masking_method 参数后重跑\"}, \"mvp_ii_profiling_v3\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T21:28:01.393Z\", \"updated_at\": \"2026-05-13T22:42:34.790Z\", \"hypothesis\": \"M1v3诊断: 降低sparsity至10%/20%(v2的30%/50%导致Inf退化) + quantile segmentation替代KDE(v2 90%样本fallback) + NaN guard。测试compound sparsity交互强度是否在sparsity regime间有显著差异。\", \"parent\": \"mvp_ii_profiling_v2\", \"conclusion\": \"negative\", \"metrics\": {\"mvp_verdict\": \"FAIL\", \"ci_nonoverlap\": false, \"sign_reversal\": false, \"phase_distribution_balanced\": true, \"ii_high_0.1\": {\"mean\": 0.2317, \"ci\": [0.1338, 0.3418]}, \"ii_low_0.1\": {\"mean\": 0.1711, \"ci\": [0.0782, 0.2768]}, \"ii_mid_0.1\": {\"mean\": 0.1607, \"ci\": [0.0886, 0.2489]}, \"ii_high_0.2\": {\"mean\": 2.1574, \"ci\": [1.0605, 3.5491]}, \"ii_low_0.2\": {\"mean\": 1.1294, \"ci\": [0.4368, 1.9593]}, \"ii_mid_0.2\": {\"mean\": 0.3049, \"ci\": [-1.0635, 1.3044]}, \"total_tokens\": 86207, \"no_nan_inf\": true, \"segments\": {\"high\": 511, \"low\": 454, \"mid\": 391}}}, \"mvp_ii_profiling_v2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T20:41:50.875Z\", \"updated_at\": \"2026-05-13T22:42:24.179Z\", \"hypothesis\": \"P0修复后重跑: Phase-dependent interaction direction reversal — compound sparsity exhibits qualitatively different interaction patterns across reasoning phases. KV eviction mask已修复为1D共享(原P0 bug导致指数级token丢失). 同时启用P1诊断dump验证phase segmentation.\", \"parent\": \"mvp_interaction_index_profiling\", \"conclusion\": \"negative\", \"metrics\": {\"mvp_verdict\": \"PASS_technical_but_negative_hypothesis\", \"ci_nonoverlap\": true, \"sign_reversal\": false, \"ii_reasoning_0.3\": 17.79, \"ii_reasoning_0.3_ci\": [4.09, 38.76], \"ii_transition_0.3\": 3.06, \"ii_transition_0.3_ci\": [0.01, 5.6], \"ii_reasoning_0.5\": 468.9, \"ii_transition_0.5\": 850.07, \"ii_execution_0.3\": \"Inf\", \"phase_distribution\": {\"execution\": \"1.2%_25seg\", \"reasoning\": \"8.1%_96seg\", \"transition\": \"90.7%_192seg\"}, \"total_tokens\": 86207, \"all_ii_superadditive\": true, \"amplitude_ratio_reas_vs_trans_0.3\": 5.81, \"gmm_best_k\": 5, \"gmm_means\": [0.438, 0.597, 0.719, 0.816, 0.892], \"gmm_weights\": [0.062, 0.14, 0.208, 0.282, 0.309], \"sparsity_global\": {\"mean\": 0.7653, \"std\": 0.1364, \"median\": 0.8004}, \"quantile_boundaries\": [0.7337, 0.8482]}}, \"mvp_interaction_index_profiling\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T19:19:05.209Z\", \"updated_at\": \"2026-05-13T20:41:42.206Z\", \"hypothesis\": \"Phase-dependent interaction direction reversal: compound sparsity (attention head pruning + KV cache eviction) exhibits qualitatively different interaction patterns (super- vs sub-additive) across reasoning phases (execution/reasoning/transition), as measured by Interaction Index on DeepSeek-R1-Distill-Qwen-7B MATH-500 traces.\", \"conclusion\": \"failed\"}}, \"count\": 126, \"total\": 126, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.5047}}"
    }
  },
  "sourceToolAssistantUUID": "894da37e-35e8-457e-82ab-0a7ae63a39f2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/.claude/sessions/agent_9c1243df",
  "sessionId": "ffa9d23f-27b7-4443-aea1-c7cdeeb2bf53",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-16T02:46:03.553Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_019FNMMzZZbkBnBUJwoFqaJS`</summary>

```json
{
  "project": "phase-gated-compound-sparse",
  "file": "report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2949a970-7d32-4cd9-80b0-10d153fcc8fe",
  "isSidechain": false,
  "requestId": "req_011Cb5UuwN6gHEciLdxbQscj",
  "type": "assistant",
  "uuid": "68266e14-b272-4f77-bce8-da489f0654c2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/.claude/sessions/agent_9c1243df",
  "sessionId": "ffa9d23f-27b7-4443-aea1-c7cdeeb2bf53",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UADVgkN4zKVRvZ67BUf752",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1658,
      "cache_read_input_tokens": 36778,
      "output_tokens": 312,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1658,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 312,
          "cache_read_input_tokens": 36778,
          "cache_creation_input_tokens": 1658,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1658
          },
          "type": "message"
        }
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

_source line 17 · 2026-05-16T02:46:04.125Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_roadmap · `toolu_01A9jiHREmQbDFfCBCvzCS9a`</summary>

```json
{
  "project": "phase-gated-compound-sparse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "68266e14-b272-4f77-bce8-da489f0654c2",
  "isSidechain": false,
  "requestId": "req_011Cb5UuwN6gHEciLdxbQscj",
  "type": "assistant",
  "uuid": "034bf14c-4a7d-4b4e-84b5-45b1c1576d86",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/.claude/sessions/agent_9c1243df",
  "sessionId": "ffa9d23f-27b7-4443-aea1-c7cdeeb2bf53",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UADVgkN4zKVRvZ67BUf752",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1658,
      "cache_read_input_tokens": 36778,
      "output_tokens": 312,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1658,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 312,
          "cache_read_input_tokens": 36778,
          "cache_creation_input_tokens": 1658,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1658
          },
          "type": "message"
        }
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

_source line 18 · 2026-05-16T02:46:04.221Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__list_workers · `toolu_01XgS4w3xzw3U4CjXhJErNRL`</summary>

```json
{
  "project": "phase-gated-compound-sparse",
  "status": "running"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "034bf14c-4a7d-4b4e-84b5-45b1c1576d86",
  "isSidechain": false,
  "requestId": "req_011Cb5UuwN6gHEciLdxbQscj",
  "type": "assistant",
  "uuid": "bd6f2067-c4c7-4a21-8a59-04cfe91c7bb7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/.claude/sessions/agent_9c1243df",
  "sessionId": "ffa9d23f-27b7-4443-aea1-c7cdeeb2bf53",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UADVgkN4zKVRvZ67BUf752",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1658,
      "cache_read_input_tokens": 36778,
      "output_tokens": 312,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1658,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 312,
          "cache_read_input_tokens": 36778,
          "cache_creation_input_tokens": 1658,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1658
          },
          "type": "message"
        }
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

_source line 19_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[HANDOFF] 你是 Main Agent，这是 Loop #15。  ## 上一轮交接 (task_context)  ### 1. 🔴 硬约束 / 红线 - GPU 白名单：**westd-22162 cuda:0~3** 仅此 4 张，不可用其他 GPU - c8_llama_n250 正在占满 4 GPU（4 并行推理），完成前不可提交新 GPU 实验 - EMNLP 2026 AR…",
  "leafUuid": "bd6f2067-c4c7-4a21-8a59-04cfe91c7bb7",
  "sessionId": "ffa9d23f-27b7-4443-aea1-c7cdeeb2bf53"
}
```

---

### Runtime record

_source line 20_

```json
{
  "type": "ai-title",
  "aiTitle": "Verify active experiments and paper revisions for EMNLP 2026",
  "sessionId": "ffa9d23f-27b7-4443-aea1-c7cdeeb2bf53"
}
```

---

### Tool result

_source line 21 · 2026-05-16T02:46:06.653Z_

<details><summary>↩ Tool result · `toolu_01EYAyJGB1st1q3WHkTPC52G`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"reconciled\": 1, \"results\": [{\"exp_id\": \"c8_llama_n250\", \"success\": true, \"actions\": [\"Job still running (pid=301187)\"]}]}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4af5a121-263e-4780-ba60-9bf86b3f9ecd",
  "isSidechain": false,
  "promptId": "d6a043a1-3c08-4fe7-9e57-50e76a38ea26",
  "type": "user",
  "uuid": "4f7713dc-82c8-4fa9-87fa-35173063b481",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"reconciled\\\": 1, \\\"results\\\": [{\\\"exp_id\\\": \\\"c8_llama_n250\\\", \\\"success\\\": true, \\\"actions\\\": [\\\"Job still running (pid=301187)\\\"]}]}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"reconciled\": 1, \"results\": [{\"exp_id\": \"c8_llama_n250\", \"success\": true, \"actions\": [\"Job still running (pid=301187)\"]}]}, \"error\": null, \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "4af5a121-263e-4780-ba60-9bf86b3f9ecd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/.claude/sessions/agent_9c1243df",
  "sessionId": "ffa9d23f-27b7-4443-aea1-c7cdeeb2bf53",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-16T02:46:06.668Z_

<details><summary>↩ Tool result · `toolu_019FNMMzZZbkBnBUJwoFqaJS`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/report.md\", \"content\": \"# Handover — 2026-05-16\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\\n|--------|------|------|---------|-----|\\n| c8_llama_n250 | — | — | — | — |\\n\\n## 待处理\\n- c10_lang_switching（准备中）\\n- c9_gsm8k_power_analysis（准备中）\\n- c5_per_phase_gini（准备中）\\n- c4_think_validation_math500（准备中）\\n\\n## 近期结论\\n- **acc_ds_s030_8k_v2** (success): DS s030 accuracy eval with max_new_tokens=8192，补全 5-point dose curve。\\n- **acc_qw_s030_b1_8k** (negative): 重跑 QW importance_s030 batch1 (problems 1-50) with max_new_tokens=8192，修复原 batch1 使用 2048 的 token 预算不匹配问题。\\n- **acc_qw_s025_b1_8k** (negative): 重跑 QW importance_s025 batch1 (problems 1-50) with max_new_tokens=8192，修复原 batch1 使用 2048 的 token 预算不匹配问题。\\n\\n## 趋势\\n成功 59 / 负向 17 / 失败 16 / 共 121\\naccuracy: 0.04 ↓（近 3 次 success）\\ncorrect: 2 ↓（近 3 次 success）\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\nwestd-22162: 无 GPU 信息\\n\\n## 告警\\n- mvp_interaction_index_profiling: 训练失败 — unknown\\n- mvp_ii_profiling_v4: 训练失败 — unknown\\n- mvp_ii_profiling_v4b: 训练失败 — unknown\\n- mvp_ii_profiling_v4c: 训练失败 — unknown\\n- mvp_ii_profiling_v4d: 训练失败 — unknown\\n- mvp_ii_profiling_v4-random: 训练失败 — unknown\\n- mvp_v4a_r2: 训练失败 — unknown\\n- mvp_v4b_r2: 训练失败 — unknown\\n- mvp_v4c_r2: 训练失败 — unknown\\n- mvp_v4_legacy_s025: 训练失败 — unknown\\n- mvp_v4_legacy_s035: 训练失败 — unknown\\n- mvp_v4_float32_s030: 已被终止 — unknown\\n- mvp_v5_fixed_s020: 已被终止 — unknown\\n- mvp_v5_fixed_s030: 已被终止 — unknown\\n- qwen_importance_s015: 已被终止 — unknown\\n- qwen_importance_s020: 已被终止 — unknown\\n- qwen_importance_s025: 已被终止 — unknown\\n- qwen_importance_s030: 已被终止 — unknown\\n- v6_random_s030: 训练失败 — unknown\\n- v6_random_s030_r2: 训练失败 — unknown\\n- bf16_random_s015: 已被终止 — unknown\\n- bf16_random_s020: 已被终止 — unknown\\n- bf16_random_s025: 已被终止 — unknown\\n- bf16_random_s030: 已被终止 — unknown\\n- bf16_qwen_importance_s015: 已被终止 — unknown\\n- bf16_qwen_importance_s020: 已被终止 — unknown\\n- bf16_qwen_importance_s025: 已被终止 — unknown\\n- bf16_qwen_importance_s030: 已被终止 — unknown\\n- bf16_ds_imp_s015: 已被终止 — unknown\\n- bf16_ds_imp_s020: 已被终止 — unknown\\n- bf16_ds_imp_s025: 已被终止 — unknown\\n- bf16_ds_imp_s030: 已被终止 — unknown\\n- c3_llama_arch: 已被终止 — unknown\\n- c2_ds_n500: 已被终止 — unknown\\n- c2_qw_n500: 训练失败 — unknown\\n- r9c2-spike: 已被终止 — unknown\\n- r9c2-spike-v2: 已被终止 — unknown\\n- r9c2-spike-v3: 已被终止 — unknown\\n- acc_ds_dense_8k: 已被终止 — unknown\\n- acc_ds_s015_8k: 已被终止 — unknown\\n- acc_ds_s020_8k: 已被终止 — unknown\\n- acc_ds_s025_8k: 已被终止 — unknown\\n- acc_ds_s030_8k: 已被终止 — unknown\\n- gsm8k_qw_rand_s025: 训练失败 — unknown\\n- gsm8k_qw_rand_s030: 训练失败 — unknown\\n\", \"total_chars\": 2495, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "68266e14-b272-4f77-bce8-da489f0654c2",
  "isSidechain": false,
  "promptId": "d6a043a1-3c08-4fe7-9e57-50e76a38ea26",
  "type": "user",
  "uuid": "1988b69e-52ce-4a1f-8ceb-968625b89f52",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/report.md\\\", \\\"content\\\": \\\"# Handover — 2026-05-16\\\\n\\\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\\\n\\\\n## 运行中\\\\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\\\\n|--------|------|------|---------|-----|\\\\n| c8_llama_n250 | — | — | — | — |\\\\n\\\\n## 待处理\\\\n- c10_lang_switching（准备中）\\\\n- c9_gsm8k_power_analysis（准备中）\\\\n- c5_per_phase_gini（准备中）\\\\n- c4_think_validation_math500（准备中）\\\\n\\\\n## 近期结论\\\\n- **acc_ds_s030_8k_v2** (success): DS s030 accuracy eval with max_new_tokens=8192，补全 5-point dose curve。\\\\n- **acc_qw_s030_b1_8k** (negative): 重跑 QW importance_s030 batch1 (problems 1-50) with max_new_tokens=8192，修复原 batch1 使用 2048 的 token 预算不匹配问题。\\\\n- **acc_qw_s025_b1_8k** (negative): 重跑 QW importance_s025 batch1 (problems 1-50) with max_new_tokens=8192，修复原 batch1 使用 2048 的 token 预算不匹配问题。\\\\n\\\\n## 趋势\\\\n成功 59 / 负向 17 / 失败 16 / 共 121\\\\naccuracy: 0.04 ↓（近 3 次 success）\\\\ncorrect: 2 ↓（近 3 次 success）\\\\n\\\\n## 下一步\\\\n（无活跃 idea，请通过 ideas.md 添加）\\\\n\\\\n## 资源状态\\\\nwestd-22162: 无 GPU 信息\\\\n\\\\n## 告警\\\\n- mvp_interaction_index_profiling: 训练失败 — unknown\\\\n- mvp_ii_profiling_v4: 训练失败 — unknown\\\\n- mvp_ii_profiling_v4b: 训练失败 — unknown\\\\n- mvp_ii_profiling_v4c: 训练失败 — unknown\\\\n- mvp_ii_profiling_v4d: 训练失败 — unknown\\\\n- mvp_ii_profiling_v4-random: 训练失败 — unknown\\\\n- mvp_v4a_r2: 训练失败 — unknown\\\\n- mvp_v4b_r2: 训练失败 — unknown\\\\n- mvp_v4c_r2: 训练失败 — unknown\\\\n- mvp_v4_legacy_s025: 训练失败 — unknown\\\\n- mvp_v4_legacy_s035: 训练失败 — unknown\\\\n- mvp_v4_float32_s030: 已被终止 — unknown\\\\n- mvp_v5_fixed_s020: 已被终止 — unknown\\\\n- mvp_v5_fixed_s030: 已被终止 — unknown\\\\n- qwen_importance_s015: 已被终止 — unknown\\\\n- qwen_importance_s020: 已被终止 — unknown\\\\n- qwen_importance_s025: 已被终止 — unknown\\\\n- qwen_importance_s030: 已被终止 — unknown\\\\n- v6_random_s030: 训练失败 — unknown\\\\n- v6_random_s030_r2: 训练失败 — unknown\\\\n- bf16_random_s015: 已被终止 — unknown\\\\n- bf16_random_s020: 已被终止 — unknown\\\\n- bf16_random_s025: 已被终止 — unknown\\\\n- bf16_random_s030: 已被终止 — unknown\\\\n- bf16_qwen_importance_s015: 已被终止 — unknown\\\\n- bf16_qwen_importance_s020: 已被终止 — unknown\\\\n- bf16_qwen_importance_s025: 已被终止 — unknown\\\\n- bf16_qwen_importance_s030: 已被终止 — unknown\\\\n- bf16_ds_imp_s015: 已被终止 — unknown\\\\n- bf16_ds_imp_s020: 已被终止 — unknown\\\\n- bf16_ds_imp_s025: 已被终止 — unknown\\\\n- bf16_ds_imp_s030: 已被终止 — unknown\\\\n- c3_llama_arch: 已被终止 — unknown\\\\n- c2_ds_n500: 已被终止 — unknown\\\\n- c2_qw_n500: 训练失败 — unknown\\\\n- r9c2-spike: 已被终止 — unknown\\\\n- r9c2-spike-v2: 已被终止 — unknown\\\\n- r9c2-spike-v3: 已被终止 — unknown\\\\n- acc_ds_dense_8k: 已被终止 — unknown\\\\n- acc_ds_s015_8k: 已被终止 — unknown\\\\n- acc_ds_s020_8k: 已被终止 — unknown\\\\n- acc_ds_s025_8k: 已被终止 — unknown\\\\n- acc_ds_s030_8k: 已被终止 — unknown\\\\n- gsm8k_qw_rand_s025: 训练失败 — unknown\\\\n- gsm8k_qw_rand_s030: 训练失败 — unknown\\\\n\\\", \\\"total_chars\\\": 2495, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/report.md\", \"content\": \"# Handover — 2026-05-16\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\\n|--------|------|------|---------|-----|\\n| c8_llama_n250 | — | — | — | — |\\n\\n## 待处理\\n- c10_lang_switching（准备中）\\n- c9_gsm8k_power_analysis（准备中）\\n- c5_per_phase_gini（准备中）\\n- c4_think_validation_math500（准备中）\\n\\n## 近期结论\\n- **acc_ds_s030_8k_v2** (success): DS s030 accuracy eval with max_new_tokens=8192，补全 5-point dose curve。\\n- **acc_qw_s030_b1_8k** (negative): 重跑 QW importance_s030 batch1 (problems 1-50) with max_new_tokens=8192，修复原 batch1 使用 2048 的 token 预算不匹配问题。\\n- **acc_qw_s025_b1_8k** (negative): 重跑 QW importance_s025 batch1 (problems 1-50) with max_new_tokens=8192，修复原 batch1 使用 2048 的 token 预算不匹配问题。\\n\\n## 趋势\\n成功 59 / 负向 17 / 失败 16 / 共 121\\naccuracy: 0.04 ↓（近 3 次 success）\\ncorrect: 2 ↓（近 3 次 success）\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\nwestd-22162: 无 GPU 信息\\n\\n## 告警\\n- mvp_interaction_index_profiling: 训练失败 — unknown\\n- mvp_ii_profiling_v4: 训练失败 — unknown\\n- mvp_ii_profiling_v4b: 训练失败 — unknown\\n- mvp_ii_profiling_v4c: 训练失败 — unknown\\n- mvp_ii_profiling_v4d: 训练失败 — unknown\\n- mvp_ii_profiling_v4-random: 训练失败 — unknown\\n- mvp_v4a_r2: 训练失败 — unknown\\n- mvp_v4b_r2: 训练失败 — unknown\\n- mvp_v4c_r2: 训练失败 — unknown\\n- mvp_v4_legacy_s025: 训练失败 — unknown\\n- mvp_v4_legacy_s035: 训练失败 — unknown\\n- mvp_v4_float32_s030: 已被终止 — unknown\\n- mvp_v5_fixed_s020: 已被终止 — unknown\\n- mvp_v5_fixed_s030: 已被终止 — unknown\\n- qwen_importance_s015: 已被终止 — unknown\\n- qwen_importance_s020: 已被终止 — unknown\\n- qwen_importance_s025: 已被终止 — unknown\\n- qwen_importance_s030: 已被终止 — unknown\\n- v6_random_s030: 训练失败 — unknown\\n- v6_random_s030_r2: 训练失败 — unknown\\n- bf16_random_s015: 已被终止 — unknown\\n- bf16_random_s020: 已被终止 — unknown\\n- bf16_random_s025: 已被终止 — unknown\\n- bf16_random_s030: 已被终止 — unknown\\n- bf16_qwen_importance_s015: 已被终止 — unknown\\n- bf16_qwen_importance_s020: 已被终止 — unknown\\n- bf16_qwen_importance_s025: 已被终止 — unknown\\n- bf16_qwen_importance_s030: 已被终止 — unknown\\n- bf16_ds_imp_s015: 已被终止 — unknown\\n- bf16_ds_imp_s020: 已被终止 — unknown\\n- bf16_ds_imp_s025: 已被终止 — unknown\\n- bf16_ds_imp_s030: 已被终止 — unknown\\n- c3_llama_arch: 已被终止 — unknown\\n- c2_ds_n500: 已被终止 — unknown\\n- c2_qw_n500: 训练失败 — unknown\\n- r9c2-spike: 已被终止 — unknown\\n- r9c2-spike-v2: 已被终止 — unknown\\n- r9c2-spike-v3: 已被终止 — unknown\\n- acc_ds_dense_8k: 已被终止 — unknown\\n- acc_ds_s015_8k: 已被终止 — unknown\\n- acc_ds_s020_8k: 已被终止 — unknown\\n- acc_ds_s025_8k: 已被终止 — unknown\\n- acc_ds_s030_8k: 已被终止 — unknown\\n- gsm8k_qw_rand_s025: 训练失败 — unknown\\n- gsm8k_qw_rand_s030: 训练失败 — unknown\\n\", \"total_chars\": 2495, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "68266e14-b272-4f77-bce8-da489f0654c2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/.claude/sessions/agent_9c1243df",
  "sessionId": "ffa9d23f-27b7-4443-aea1-c7cdeeb2bf53",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-16T02:46:06.692Z_

<details><summary>↩ Tool result · `toolu_01A9jiHREmQbDFfCBCvzCS9a`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/ROADMAP.md\", \"content\": \"# phase-gated-compound-sparse — Research Dashboard\\n\\n> 最后更新: 2026-05-16 02:35 UTC | 更新原因: Round 10 审稿回溯：加入系统性问题 Holistic Pass + 更新近期任务为 Action Matrix 派发项\\n\\n> 核心文档链: paper_framing.md → experiment_plan.yaml → 本 ROADMAP\\n\\n## 核心方向\\n**Phase-modulated compound sparsity severity**：importance-based eviction 的 compound interaction severity 随 sparsity 单调递增（n=500 confirmed）。详见 paper_framing.md。\\n\\n## 目标会议\\nEMNLP 2026 ARR — **截稿 2026-05-25（距今 9 天）** — Findings track\\n\\n## 当前进展\\n- 阶段：**Round 10 审稿完成 (weak reject 2.25/5) → 修订中**\\n- 121 实验完成（58 success / 18 negative / 16 failed），38 plan experiments 全部 done（coverage 92.1%）\\n- Round 10 审稿：5 Critical + 6 Warning，已拆解 Action Matrix 并派发\\n- 关键修订：LLaMA n=250 扩展（P1 GPU）、&lt;think> phase validation（P1）、per-phase Gini（P1 CPU）、写作全面修正\\n\\n## 审稿回溯·系统性问题（Round 10 Holistic Pass）\\n\\n### SYSTEMIC_ISSUE #1: 写作可信度（6 issues → 根因：初稿质量控制不足）\\nR10-C1 (MUSTAFAR fake citation), R10-W1 (overclaiming), R10-W3 (H2O confound), R10-W4 (GPU deanon), R10-W5 (statistical gaps), R10-W6 (clarity)\\n**根因处理**：Paper Agent 执行全面写作修正，含 bib 全量审计 + 贡献词降级 + 统计报告补全 + 匿名化 + H2O limitations\\n\\n### SYSTEMIC_ISSUE #2: 实验证据厚度（4 issues → 根因：cross-arch 和机制验证不足）\\nR10-C3 (LLaMA n=49 underpowered), R10-C4 (&lt;think> validation), R10-C5 (per-phase Gini), R10-W5 (pilot CI)\\n**根因处理**：Agent 并行 4 任务——LLaMA n=250（GPU 5-6h）、&lt;think> token validation、per-phase Gini decomposition、GSM8K power analysis\\n\\n### 非系统性但 Critical: 定位调整\\nR10-C2 (novelty for main conf) → 接受 Findings track，reframe contributions 为 empirical insights\\n\\n**结论**：无 SYSTEMIC_ISSUE 指向 core method design，现有实验矩阵在新理解下仍有效，不需要 experiment-matrix 回溯。\\n\\n## 近期任务（Round 10 修订）\\n- [ ] **P1-GPU** Agent: LLaMA n=250 扩展（4 sparsity × 2 strategy × MATH-500，4 GPU 并行，~5-6h）\\n- [ ] **P1-CPU** Agent: MATH-500 &lt;think> token position validation（DS+QW × 50 problems）\\n- [ ] **P1-CPU** Agent: Per-phase Gini decomposition（从 c4_entropy 数据，~30min）\\n- [ ] **P2-CPU** Agent: GSM8K random subset power analysis（n=50 bootstrap → 需多少 n）\\n- [ ] **P2-CPU** Agent: MATH-500 language switching check（DS 中文/符号切换影响）\\n- [ ] **P1** Paper Agent: MUSTAFAR 删除 + bib 全量审计\\n- [ ] **P1** Paper Agent: Abstract/Intro rewrite（Findings framing + Δ headline）\\n- [ ] **P1** Paper Agent: §4-7 corrections（贡献词、因果语言、footnote、GPU匿名、Bonferroni、CoT citations）\\n- [ ] **P1** Paper Agent: Appendix fixes（NT samples、pilot CI、G metric downgrade）\\n- [ ] 等待用户确认 Findings track 决策\\n- [ ] Round 11 审稿提交\\n\\n## GPU 预算\\n- RTX 6000 Pro ×4: westd-22162 cuda:0~3\\n- 当前：LLaMA n=250 即将占满 4 GPU（~5-6h）\\n- 已用: ~36h / ~250h 预算\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D091 | 2026-05-16 | R10 审稿 Weak Reject (2.25/5)：接受 Findings track，启动 5 | c3_llama, think_phase_validation, c4_entropy |\\n| D090 | 2026-05-16 | Round 10 dual dose curve 完成：DS 5-point (0.74→0.04) | acc_ds_dense_8k_v2, acc_ds_s015_8k_v2, acc_ds_s020_8k_v2, acc_ds_s025_8k_v2, acc_ds_s030_8k_v2, acc_qw_s030_b1_8k, acc_qw_s025_b1_8k |\\n| D089 | 2026-05-16 | DS 8k v2 揭示双 regime 结构：s≤0.20 截断驱动（非截断 acc ~71% 稳定 | acc_ds_dense_8k_v2, acc_ds_s015_8k_v2, acc_ds_s020_8k_v2, acc_ds_s025_8k_v2, acc_ds_s030_8k_v2 |\\n| D088 | 2026-05-15 | D086 补充：DS 8k token budget 验证性重跑，确认截断效应与定性观察边界 | acc_ds_dense_8k_v2, acc_ds_s020_8k_v2, acc_ds_s015_8k_v2, acc_ds_s025_8k_v2, acc_ds_s030_8k_v2 |\\n| D087 | 2026-05-15 | QW n=100 accuracy eval 完成（s020≈34%, s025≈30%）；DS 8 | acc_qw_s020_n100, acc_qw_s025_n100, acc_ds_dense_8k, acc_ds_s015_8k, acc_ds_s020_8k, acc_ds_s025_8k, acc_ds_s030_8k |\\n| D086 | 2026-05-15 | DS accuracy 数据降为定性观察，QW 作为 accuracy dose-response  | acc_ds_s020, acc_ds_s025, acc_qw_s020_n100, acc_qw_s025_n100 |\\n| D085 | 2026-05-15 | R9 C1+C2 均 PASS，维持 EMNLP main conference 目标；补 s020 | think_phase_validation, c2_accuracy_eval |\\n| D084 | 2026-05-15 | Round 9 Action Matrix: 并行实验 C1(`&lt;think>` validatio | gsm8k_profiling_ds, gsm8k_profiling_qw |\\n| D083 | 2026-05-15 | GSM8K 聚合统计量从 nanmean 改为 nanmedian + Wilcoxon（Revie | gsm8k_profiling_ds, gsm8k_profiling_qw |\\n| D082 | 2026-05-15 | G× 数值下修：58-241× → 21-64×（per-problem precise 计算），论 | appendix_b_precise_gx |\\n\\n\\n\\n\", \"lines\": 69}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "034bf14c-4a7d-4b4e-84b5-45b1c1576d86",
  "isSidechain": false,
  "promptId": "d6a043a1-3c08-4fe7-9e57-50e76a38ea26",
  "type": "user",
  "uuid": "536fe8b6-f4b6-46b9-a45a-e53a7f1bb9ac",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/ROADMAP.md\\\", \\\"content\\\": \\\"# phase-gated-compound-sparse — Research Dashboard\\\\n\\\\n> 最后更新: 2026-05-16 02:35 UTC | 更新原因: Round 10 审稿回溯：加入系统性问题 Holistic Pass + 更新近期任务为 Action Matrix 派发项\\\\n\\\\n> 核心文档链: paper_framing.md → experiment_plan.yaml → 本 ROADMAP\\\\n\\\\n## 核心方向\\\\n**Phase-modulated compound sparsity severity**：importance-based eviction 的 compound interaction severity 随 sparsity 单调递增（n=500 confirmed）。详见 paper_framing.md。\\\\n\\\\n## 目标会议\\\\nEMNLP 2026 ARR — **截稿 2026-05-25（距今 9 天）** — Findings track\\\\n\\\\n## 当前进展\\\\n- 阶段：**Round 10 审稿完成 (weak reject 2.25/5) → 修订中**\\\\n- 121 实验完成（58 success / 18 negative / 16 failed），38 plan experiments 全部 done（coverage 92.1%）\\\\n- Round 10 审稿：5 Critical + 6 Warning，已拆解 Action Matrix 并派发\\\\n- 关键修订：LLaMA n=250 扩展（P1 GPU）、&lt;think> phase validation（P1）、per-phase Gini（P1 CPU）、写作全面修正\\\\n\\\\n## 审稿回溯·系统性问题（Round 10 Holistic Pass）\\\\n\\\\n### SYSTEMIC_ISSUE #1: 写作可信度（6 issues → 根因：初稿质量控制不足）\\\\nR10-C1 (MUSTAFAR fake citation), R10-W1 (overclaiming), R10-W3 (H2O confound), R10-W4 (GPU deanon), R10-W5 (statistical gaps), R10-W6 (clarity)\\\\n**根因处理**：Paper Agent 执行全面写作修正，含 bib 全量审计 + 贡献词降级 + 统计报告补全 + 匿名化 + H2O limitations\\\\n\\\\n### SYSTEMIC_ISSUE #2: 实验证据厚度（4 issues → 根因：cross-arch 和机制验证不足）\\\\nR10-C3 (LLaMA n=49 underpowered), R10-C4 (&lt;think> validation), R10-C5 (per-phase Gini), R10-W5 (pilot CI)\\\\n**根因处理**：Agent 并行 4 任务——LLaMA n=250（GPU 5-6h）、&lt;think> token validation、per-phase Gini decomposition、GSM8K power analysis\\\\n\\\\n### 非系统性但 Critical: 定位调整\\\\nR10-C2 (novelty for main conf) → 接受 Findings track，reframe contributions 为 empirical insights\\\\n\\\\n**结论**：无 SYSTEMIC_ISSUE 指向 core method design，现有实验矩阵在新理解下仍有效，不需要 experiment-matrix 回溯。\\\\n\\\\n## 近期任务（Round 10 修订）\\\\n- [ ] **P1-GPU** Agent: LLaMA n=250 扩展（4 sparsity × 2 strategy × MATH-500，4 GPU 并行，~5-6h）\\\\n- [ ] **P1-CPU** Agent: MATH-500 &lt;think> token position validation（DS+QW × 50 problems）\\\\n- [ ] **P1-CPU** Agent: Per-phase Gini decomposition（从 c4_entropy 数据，~30min）\\\\n- [ ] **P2-CPU** Agent: GSM8K random subset power analysis（n=50 bootstrap → 需多少 n）\\\\n- [ ] **P2-CPU** Agent: MATH-500 language switching check（DS 中文/符号切换影响）\\\\n- [ ] **P1** Paper Agent: MUSTAFAR 删除 + bib 全量审计\\\\n- [ ] **P1** Paper Agent: Abstract/Intro rewrite（Findings framing + Δ headline）\\\\n- [ ] **P1** Paper Agent: §4-7 corrections（贡献词、因果语言、footnote、GPU匿名、Bonferroni、CoT citations）\\\\n- [ ] **P1** Paper Agent: Appendix fixes（NT samples、pilot CI、G metric downgrade）\\\\n- [ ] 等待用户确认 Findings track 决策\\\\n- [ ] Round 11 审稿提交\\\\n\\\\n## GPU 预算\\\\n- RTX 6000 Pro ×4: westd-22162 cuda:0~3\\\\n- 当前：LLaMA n=250 即将占满 4 GPU（~5-6h）\\\\n- 已用: ~36h / ~250h 预算\\\\n\\\\n## 关键决策日志\\\\n\\\\n| ID | 日期 | 摘要 | 关联实验 |\\\\n|----|------|------|----------|\\\\n| D091 | 2026-05-16 | R10 审稿 Weak Reject (2.25/5)：接受 Findings track，启动 5 | c3_llama, think_phase_validation, c4_entropy |\\\\n| D090 | 2026-05-16 | Round 10 dual dose curve 完成：DS 5-point (0.74→0.04) | acc_ds_dense_8k_v2, acc_ds_s015_8k_v2, acc_ds_s020_8k_v2, acc_ds_s025_8k_v2, acc_ds_s030_8k_v2, acc_qw_s030_b1_8k, acc_qw_s025_b1_8k |\\\\n| D089 | 2026-05-16 | DS 8k v2 揭示双 regime 结构：s≤0.20 截断驱动（非截断 acc ~71% 稳定 | acc_ds_dense_8k_v2, acc_ds_s015_8k_v2, acc_ds_s020_8k_v2, acc_ds_s025_8k_v2, acc_ds_s030_8k_v2 |\\\\n| D088 | 2026-05-15 | D086 补充：DS 8k token budget 验证性重跑，确认截断效应与定性观察边界 | acc_ds_dense_8k_v2, acc_ds_s020_8k_v2, acc_ds_s015_8k_v2, acc_ds_s025_8k_v2, acc_ds_s030_8k_v2 |\\\\n| D087 | 2026-05-15 | QW n=100 accuracy eval 完成（s020≈34%, s025≈30%）；DS 8 | acc_qw_s020_n100, acc_qw_s025_n100, acc_ds_dense_8k, acc_ds_s015_8k, acc_ds_s020_8k, acc_ds_s025_8k, acc_ds_s030_8k |\\\\n| D086 | 2026-05-15 | DS accuracy 数据降为定性观察，QW 作为 accuracy dose-response  | acc_ds_s020, acc_ds_s025, acc_qw_s020_n100, acc_qw_s025_n100 |\\\\n| D085 | 2026-05-15 | R9 C1+C2 均 PASS，维持 EMNLP main conference 目标；补 s020 | think_phase_validation, c2_accuracy_eval |\\\\n| D084 | 2026-05-15 | Round 9 Action Matrix: 并行实验 C1(`&lt;think>` validatio | gsm8k_profiling_ds, gsm8k_profiling_qw |\\\\n| D083 | 2026-05-15 | GSM8K 聚合统计量从 nanmean 改为 nanmedian + Wilcoxon（Revie | gsm8k_profiling_ds, gsm8k_profiling_qw |\\\\n| D082 | 2026-05-15 | G× 数值下修：58-241× → 21-64×（per-problem precise 计算），论 | appendix_b_precise_gx |\\\\n\\\\n\\\\n\\\\n\\\", \\\"lines\\\": 69}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/ROADMAP.md\", \"content\": \"# phase-gated-compound-sparse — Research Dashboard\\n\\n> 最后更新: 2026-05-16 02:35 UTC | 更新原因: Round 10 审稿回溯：加入系统性问题 Holistic Pass + 更新近期任务为 Action Matrix 派发项\\n\\n> 核心文档链: paper_framing.md → experiment_plan.yaml → 本 ROADMAP\\n\\n## 核心方向\\n**Phase-modulated compound sparsity severity**：importance-based eviction 的 compound interaction severity 随 sparsity 单调递增（n=500 confirmed）。详见 paper_framing.md。\\n\\n## 目标会议\\nEMNLP 2026 ARR — **截稿 2026-05-25（距今 9 天）** — Findings track\\n\\n## 当前进展\\n- 阶段：**Round 10 审稿完成 (weak reject 2.25/5) → 修订中**\\n- 121 实验完成（58 success / 18 negative / 16 failed），38 plan experiments 全部 done（coverage 92.1%）\\n- Round 10 审稿：5 Critical + 6 Warning，已拆解 Action Matrix 并派发\\n- 关键修订：LLaMA n=250 扩展（P1 GPU）、&lt;think> phase validation（P1）、per-phase Gini（P1 CPU）、写作全面修正\\n\\n## 审稿回溯·系统性问题（Round 10 Holistic Pass）\\n\\n### SYSTEMIC_ISSUE #1: 写作可信度（6 issues → 根因：初稿质量控制不足）\\nR10-C1 (MUSTAFAR fake citation), R10-W1 (overclaiming), R10-W3 (H2O confound), R10-W4 (GPU deanon), R10-W5 (statistical gaps), R10-W6 (clarity)\\n**根因处理**：Paper Agent 执行全面写作修正，含 bib 全量审计 + 贡献词降级 + 统计报告补全 + 匿名化 + H2O limitations\\n\\n### SYSTEMIC_ISSUE #2: 实验证据厚度（4 issues → 根因：cross-arch 和机制验证不足）\\nR10-C3 (LLaMA n=49 underpowered), R10-C4 (&lt;think> validation), R10-C5 (per-phase Gini), R10-W5 (pilot CI)\\n**根因处理**：Agent 并行 4 任务——LLaMA n=250（GPU 5-6h）、&lt;think> token validation、per-phase Gini decomposition、GSM8K power analysis\\n\\n### 非系统性但 Critical: 定位调整\\nR10-C2 (novelty for main conf) → 接受 Findings track，reframe contributions 为 empirical insights\\n\\n**结论**：无 SYSTEMIC_ISSUE 指向 core method design，现有实验矩阵在新理解下仍有效，不需要 experiment-matrix 回溯。\\n\\n## 近期任务（Round 10 修订）\\n- [ ] **P1-GPU** Agent: LLaMA n=250 扩展（4 sparsity × 2 strategy × MATH-500，4 GPU 并行，~5-6h）\\n- [ ] **P1-CPU** Agent: MATH-500 &lt;think> token position validation（DS+QW × 50 problems）\\n- [ ] **P1-CPU** Agent: Per-phase Gini decomposition（从 c4_entropy 数据，~30min）\\n- [ ] **P2-CPU** Agent: GSM8K random subset power analysis（n=50 bootstrap → 需多少 n）\\n- [ ] **P2-CPU** Agent: MATH-500 language switching check（DS 中文/符号切换影响）\\n- [ ] **P1** Paper Agent: MUSTAFAR 删除 + bib 全量审计\\n- [ ] **P1** Paper Agent: Abstract/Intro rewrite（Findings framing + Δ headline）\\n- [ ] **P1** Paper Agent: §4-7 corrections（贡献词、因果语言、footnote、GPU匿名、Bonferroni、CoT citations）\\n- [ ] **P1** Paper Agent: Appendix fixes（NT samples、pilot CI、G metric downgrade）\\n- [ ] 等待用户确认 Findings track 决策\\n- [ ] Round 11 审稿提交\\n\\n## GPU 预算\\n- RTX 6000 Pro ×4: westd-22162 cuda:0~3\\n- 当前：LLaMA n=250 即将占满 4 GPU（~5-6h）\\n- 已用: ~36h / ~250h 预算\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D091 | 2026-05-16 | R10 审稿 Weak Reject (2.25/5)：接受 Findings track，启动 5 | c3_llama, think_phase_validation, c4_entropy |\\n| D090 | 2026-05-16 | Round 10 dual dose curve 完成：DS 5-point (0.74→0.04) | acc_ds_dense_8k_v2, acc_ds_s015_8k_v2, acc_ds_s020_8k_v2, acc_ds_s025_8k_v2, acc_ds_s030_8k_v2, acc_qw_s030_b1_8k, acc_qw_s025_b1_8k |\\n| D089 | 2026-05-16 | DS 8k v2 揭示双 regime 结构：s≤0.20 截断驱动（非截断 acc ~71% 稳定 | acc_ds_dense_8k_v2, acc_ds_s015_8k_v2, acc_ds_s020_8k_v2, acc_ds_s025_8k_v2, acc_ds_s030_8k_v2 |\\n| D088 | 2026-05-15 | D086 补充：DS 8k token budget 验证性重跑，确认截断效应与定性观察边界 | acc_ds_dense_8k_v2, acc_ds_s020_8k_v2, acc_ds_s015_8k_v2, acc_ds_s025_8k_v2, acc_ds_s030_8k_v2 |\\n| D087 | 2026-05-15 | QW n=100 accuracy eval 完成（s020≈34%, s025≈30%）；DS 8 | acc_qw_s020_n100, acc_qw_s025_n100, acc_ds_dense_8k, acc_ds_s015_8k, acc_ds_s020_8k, acc_ds_s025_8k, acc_ds_s030_8k |\\n| D086 | 2026-05-15 | DS accuracy 数据降为定性观察，QW 作为 accuracy dose-response  | acc_ds_s020, acc_ds_s025, acc_qw_s020_n100, acc_qw_s025_n100 |\\n| D085 | 2026-05-15 | R9 C1+C2 均 PASS，维持 EMNLP main conference 目标；补 s020 | think_phase_validation, c2_accuracy_eval |\\n| D084 | 2026-05-15 | Round 9 Action Matrix: 并行实验 C1(`&lt;think>` validatio | gsm8k_profiling_ds, gsm8k_profiling_qw |\\n| D083 | 2026-05-15 | GSM8K 聚合统计量从 nanmean 改为 nanmedian + Wilcoxon（Revie | gsm8k_profiling_ds, gsm8k_profiling_qw |\\n| D082 | 2026-05-15 | G× 数值下修：58-241× → 21-64×（per-problem precise 计算），论 | appendix_b_precise_gx |\\n\\n\\n\\n\", \"lines\": 69}, \"error\": null, \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "034bf14c-4a7d-4b4e-84b5-45b1c1576d86",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/.claude/sessions/agent_9c1243df",
  "sessionId": "ffa9d23f-27b7-4443-aea1-c7cdeeb2bf53",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-16T02:46:06.787Z_

<details><summary>↩ Tool result · `toolu_01XgS4w3xzw3U4CjXhJErNRL`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"workers\": [{\"worker_id\": \"worker_analysis_c5_per_phase_gini_20260516T024150\", \"task_type\": \"analysis:c5_per_phase_gini\", \"project\": \"phase-gated-compound-sparse\", \"status\": \"running\", \"started_at\": \"2026-05-16T02:41:50.985321+00:00\", \"ended_at\": null}, {\"worker_id\": \"worker_analysis_c9_gsm8k_power_20260516T024207\", \"task_type\": \"analysis:c9_gsm8k_power\", \"project\": \"phase-gated-compound-sparse\", \"status\": \"running\", \"started_at\": \"2026-05-16T02:42:07.277018+00:00\", \"ended_at\": null}, {\"worker_id\": \"worker_analysis_c10_lang_switching_20260516T024225\", \"task_type\": \"analysis:c10_lang_switching\", \"project\": \"phase-gated-compound-sparse\", \"status\": \"running\", \"started_at\": \"2026-05-16T02:42:25.449564+00:00\", \"ended_at\": null}], \"count\": 3}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bd6f2067-c4c7-4a21-8a59-04cfe91c7bb7",
  "isSidechain": false,
  "promptId": "d6a043a1-3c08-4fe7-9e57-50e76a38ea26",
  "type": "user",
  "uuid": "ac3e45e2-cb90-4dd9-b027-139a69ab7b45",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"workers\\\": [{\\\"worker_id\\\": \\\"worker_analysis_c5_per_phase_gini_20260516T024150\\\", \\\"task_type\\\": \\\"analysis:c5_per_phase_gini\\\", \\\"project\\\": \\\"phase-gated-compound-sparse\\\", \\\"status\\\": \\\"running\\\", \\\"started_at\\\": \\\"2026-05-16T02:41:50.985321+00:00\\\", \\\"ended_at\\\": null}, {\\\"worker_id\\\": \\\"worker_analysis_c9_gsm8k_power_20260516T024207\\\", \\\"task_type\\\": \\\"analysis:c9_gsm8k_power\\\", \\\"project\\\": \\\"phase-gated-compound-sparse\\\", \\\"status\\\": \\\"running\\\", \\\"started_at\\\": \\\"2026-05-16T02:42:07.277018+00:00\\\", \\\"ended_at\\\": null}, {\\\"worker_id\\\": \\\"worker_analysis_c10_lang_switching_20260516T024225\\\", \\\"task_type\\\": \\\"analysis:c10_lang_switching\\\", \\\"project\\\": \\\"phase-gated-compound-sparse\\\", \\\"status\\\": \\\"running\\\", \\\"started_at\\\": \\\"2026-05-16T02:42:25.449564+00:00\\\", \\\"ended_at\\\": null}], \\\"count\\\": 3}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"workers\": [{\"worker_id\": \"worker_analysis_c5_per_phase_gini_20260516T024150\", \"task_type\": \"analysis:c5_per_phase_gini\", \"project\": \"phase-gated-compound-sparse\", \"status\": \"running\", \"started_at\": \"2026-05-16T02:41:50.985321+00:00\", \"ended_at\": null}, {\"worker_id\": \"worker_analysis_c9_gsm8k_power_20260516T024207\", \"task_type\": \"analysis:c9_gsm8k_power\", \"project\": \"phase-gated-compound-sparse\", \"status\": \"running\", \"started_at\": \"2026-05-16T02:42:07.277018+00:00\", \"ended_at\": null}, {\"worker_id\": \"worker_analysis_c10_lang_switching_20260516T024225\", \"task_type\": \"analysis:c10_lang_switching\", \"project\": \"phase-gated-compound-sparse\", \"status\": \"running\", \"started_at\": \"2026-05-16T02:42:25.449564+00:00\", \"ended_at\": null}], \"count\": 3}, \"error\": null, \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "bd6f2067-c4c7-4a21-8a59-04cfe91c7bb7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/.claude/sessions/agent_9c1243df",
  "sessionId": "ffa9d23f-27b7-4443-aea1-c7cdeeb2bf53",
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
  "lastPrompt": "[HANDOFF] 你是 Main Agent，这是 Loop #15。  ## 上一轮交接 (task_context)  ### 1. 🔴 硬约束 / 红线 - GPU 白名单：**westd-22162 cuda:0~3** 仅此 4 张，不可用其他 GPU - c8_llama_n250 正在占满 4 GPU（4 并行推理），完成前不可提交新 GPU 实验 - EMNLP 2026 AR…",
  "leafUuid": "ac3e45e2-cb90-4dd9-b027-139a69ab7b45",
  "sessionId": "ffa9d23f-27b7-4443-aea1-c7cdeeb2bf53"
}
```

---

### Runtime record

_source line 26_

```json
{
  "type": "ai-title",
  "aiTitle": "Verify active experiments and paper revisions for EMNLP 2026",
  "sessionId": "ffa9d23f-27b7-4443-aea1-c7cdeeb2bf53"
}
```

---

### Assistant

_source line 27 · 2026-05-16T02:46:16.226Z_

<details><summary>Logged reasoning block</summary>

```text
Let me parse the results:

1. **Registry**: Too large, saved to file. I need to query it with jq for RUNNING/PREPARING experiments.
2. **Reconcile crons**: c8_llama_n250 still running (pid=301187).
3. **Report.md**: Shows c8_llama_n250 running, c10/c9/c5/c4 as pending.
4. **ROADMAP**: Confirms Round 10 修订中, deadline 5/25, action items listed.


5. **Workers**: Three experiments are actively running - c5_per_phase_gini, c9_gsm8k_power, and c10_lang_switching. I notice c4_think_validation_math500 is marked as PREPARING in the handoff but has no corresponding worker process, so I'm querying the registry with jq to get a clearer picture of what's actually active.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ac3e45e2-cb90-4dd9-b027-139a69ab7b45",
  "isSidechain": false,
  "requestId": "req_011Cb5UvTwNRFHLh6SiFFmEG",
  "type": "assistant",
  "uuid": "c7a41b40-e3c1-4dfc-b61e-d937282c0aec",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/.claude/sessions/agent_9c1243df",
  "sessionId": "ffa9d23f-27b7-4443-aea1-c7cdeeb2bf53",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016ez19JU6xyrEzSWGsMob2u",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5414,
      "cache_read_input_tokens": 38436,
      "output_tokens": 802,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5414,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 802,
          "cache_read_input_tokens": 38436,
          "cache_creation_input_tokens": 5414,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5414
          },
          "type": "message"
        }
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

_source line 28 · 2026-05-16T02:46:16.229Z_

Registry 太大，用 jq 提取活跃实验状态。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c7a41b40-e3c1-4dfc-b61e-d937282c0aec",
  "isSidechain": false,
  "requestId": "req_011Cb5UvTwNRFHLh6SiFFmEG",
  "type": "assistant",
  "uuid": "c76389bc-a39e-4d24-9e93-d9c53e419a86",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/.claude/sessions/agent_9c1243df",
  "sessionId": "ffa9d23f-27b7-4443-aea1-c7cdeeb2bf53",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016ez19JU6xyrEzSWGsMob2u",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5414,
      "cache_read_input_tokens": 38436,
      "output_tokens": 802,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5414,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 802,
          "cache_read_input_tokens": 38436,
          "cache_creation_input_tokens": 5414,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5414
          },
          "type": "message"
        }
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

_source line 29 · 2026-05-16T02:46:23.495Z_

<details open><summary>🔧 Tool call — Bash · `toolu_016S8KoipyUKrMirffwyU1im`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-phase-gated-compound-sparse--claude-sessions-agent-9c1243df/ffa9d23f-27b7-4443-aea1-c7cdeeb2bf53/tool-results/mcp-agent-ml-research-read_registry-1778899563513.txt | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\nexperiments = json.loads(data['result'])['data']['experiments']\n# Filter for non-terminal statuses or recent experiments\nactive = [e for e in experiments if e.get('status') in ('RUNNING', 'PREPARING', 'PENDING', 'QUEUED', 'ALLOCATED', 'ANALYZING')]\nprint(f'Total experiments: {len(experiments)}')\nprint(f'Active (non-terminal): {len(active)}')\nfor e in active:\n    print(f\\\"  {e['exp_id']}: status={e['status']}, conclusion={e.get('conclusion','—')}\\\")\nprint()\n# Also check c4_think_validation_math500 specifically\nc4 = [e for e in experiments if 'c4_think' in e.get('exp_id','')]\nfor e in c4:\n    print(f\\\"c4 found: {e['exp_id']}: status={e['status']}\\\")\n# Check c5, c9, c10\nfor prefix in ['c5_per_phase', 'c9_gsm8k', 'c10_lang']:\n    matches = [e for e in experiments if prefix in e.get('exp_id','')]\n    for e in matches:\n        print(f\\\"{e['exp_id']}: status={e['status']}, conclusion={e.get('conclusion','—')}\\\")\n\"\n",
  "description": "Extract active experiments from registry JSON"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c76389bc-a39e-4d24-9e93-d9c53e419a86",
  "isSidechain": false,
  "requestId": "req_011Cb5UvTwNRFHLh6SiFFmEG",
  "type": "assistant",
  "uuid": "2896c495-75e6-4328-b220-a1335f832b1a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/.claude/sessions/agent_9c1243df",
  "sessionId": "ffa9d23f-27b7-4443-aea1-c7cdeeb2bf53",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016ez19JU6xyrEzSWGsMob2u",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5414,
      "cache_read_input_tokens": 38436,
      "output_tokens": 802,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5414,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 802,
          "cache_read_input_tokens": 38436,
          "cache_creation_input_tokens": 5414,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5414
          },
          "type": "message"
        }
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

_source line 30 · 2026-05-16T02:46:23.875Z_

<details><summary>↩ Tool result · reported error · `toolu_016S8KoipyUKrMirffwyU1im`</summary>

```text
Exit code 1
Traceback (most recent call last):
  File "&lt;string>", line 6, in &lt;module>
    active = [e for e in experiments if e.get('status') in ('RUNNING', 'PREPARING', 'PENDING', 'QUEUED', 'ALLOCATED', 'ANALYZING')]
                                        ^^^^^
AttributeError: 'str' object has no attribute 'get'
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2896c495-75e6-4328-b220-a1335f832b1a",
  "isSidechain": false,
  "promptId": "d6a043a1-3c08-4fe7-9e57-50e76a38ea26",
  "type": "user",
  "uuid": "83ddcb5e-ade2-417f-a2b9-ea3d056bf131",
  "toolUseResult": "Error: Exit code 1\nTraceback (most recent call last):\n  File \"&lt;string>\", line 6, in &lt;module>\n    active = [e for e in experiments if e.get('status') in ('RUNNING', 'PREPARING', 'PENDING', 'QUEUED', 'ALLOCATED', 'ANALYZING')]\n                                        ^^^^^\nAttributeError: 'str' object has no attribute 'get'",
  "sourceToolAssistantUUID": "2896c495-75e6-4328-b220-a1335f832b1a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/.claude/sessions/agent_9c1243df",
  "sessionId": "ffa9d23f-27b7-4443-aea1-c7cdeeb2bf53",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-16T02:46:32.468Z_

<details open><summary>🔧 Tool call — Bash · `toolu_015Fn5yQxqRF9ga47DXxY399`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-phase-gated-compound-sparse--claude-sessions-agent-9c1243df/ffa9d23f-27b7-4443-aea1-c7cdeeb2bf53/tool-results/mcp-agent-ml-research-read_registry-1778899563513.txt | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\nresult = json.loads(data['result'])\nexperiments = result['data']['experiments']\n# Check type of first element\nif experiments:\n    first = experiments[0]\n    if isinstance(first, str):\n        # It's a list of exp_id strings; need to get the full data\n        print('Registry returned list of strings, not dicts')\n        print(f'Total: {len(experiments)}')\n        print(f'Sample: {experiments[:5]}')\n    else:\n        print(type(first))\n        print(first.keys() if hasattr(first, 'keys') else first)\n\"\n",
  "description": "Probe registry data structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "83ddcb5e-ade2-417f-a2b9-ea3d056bf131",
  "isSidechain": false,
  "requestId": "req_011Cb5Uwj5j28HpmgCJRyoDD",
  "type": "assistant",
  "uuid": "8575338a-4cbb-4df0-9fbc-088529ec0d87",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/.claude/sessions/agent_9c1243df",
  "sessionId": "ffa9d23f-27b7-4443-aea1-c7cdeeb2bf53",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TAto8qhDeqfnhxrCwGALrG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 922,
      "cache_read_input_tokens": 43850,
      "output_tokens": 347,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 922,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 347,
          "cache_read_input_tokens": 43850,
          "cache_creation_input_tokens": 922,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 922
          },
          "type": "message"
        }
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

_source line 32 · 2026-05-16T02:46:32.746Z_

<details><summary>↩ Tool result · reported error · `toolu_015Fn5yQxqRF9ga47DXxY399`</summary>

```text
Exit code 1
Traceback (most recent call last):
  File "&lt;string>", line 8, in &lt;module>
    first = experiments[0]
            ~~~~~~~~~~~^^^
KeyError: 0
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8575338a-4cbb-4df0-9fbc-088529ec0d87",
  "isSidechain": false,
  "promptId": "d6a043a1-3c08-4fe7-9e57-50e76a38ea26",
  "type": "user",
  "uuid": "68e00098-61b3-47d9-8bb6-8b923955561d",
  "toolUseResult": "Error: Exit code 1\nTraceback (most recent call last):\n  File \"&lt;string>\", line 8, in &lt;module>\n    first = experiments[0]\n            ~~~~~~~~~~~^^^\nKeyError: 0",
  "sourceToolAssistantUUID": "8575338a-4cbb-4df0-9fbc-088529ec0d87",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/.claude/sessions/agent_9c1243df",
  "sessionId": "ffa9d23f-27b7-4443-aea1-c7cdeeb2bf53",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 33 · 2026-05-16T02:46:32.753Z_

```json
{
  "parentUuid": "68e00098-61b3-47d9-8bb6-8b923955561d",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "9f8568fe-b80e-4ee9-b0d2-735453c24348",
  "timestamp": "2026-05-16T02:46:32.753Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/.claude/sessions/agent_9c1243df",
  "sessionId": "ffa9d23f-27b7-4443-aea1-c7cdeeb2bf53",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 34 · 2026-05-16T02:46:40.498Z_

<details open><summary>🔧 Tool call — Bash · `toolu_013kHaCow3FwgnbyMZjTR6tb`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-phase-gated-compound-sparse--claude-sessions-agent-9c1243df/ffa9d23f-27b7-4443-aea1-c7cdeeb2bf53/tool-results/mcp-agent-ml-research-read_registry-1778899563513.txt | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\nresult = json.loads(data['result'])\nexperiments = result['data']['experiments']\nprint(type(experiments))\nif isinstance(experiments, dict):\n    # Dict keyed by exp_id\n    active = {k: v for k, v in experiments.items() if v.get('status') in ('RUNNING', 'PREPARING', 'PENDING', 'QUEUED', 'ALLOCATED', 'ANALYZING')}\n    print(f'Total: {len(experiments)}, Active: {len(active)}')\n    for k, v in active.items():\n        print(f'  {k}: status={v.get(\\\"status\\\")}, conclusion={v.get(\\\"conclusion\\\",\\\"—\\\")}')\n    # Check specific experiments\n    for key in ['c4_think_validation_math500', 'c5_per_phase_gini', 'c9_gsm8k_power_analysis', 'c10_lang_switching', 'c8_llama_n250']:\n        if key in experiments:\n            e = experiments[key]\n            print(f'  >> {key}: status={e.get(\\\"status\\\")}, conclusion={e.get(\\\"conclusion\\\",\\\"—\\\")}')\n        else:\n            print(f'  >> {key}: NOT IN REGISTRY')\nelif isinstance(experiments, list):\n    print(f'List of {len(experiments)} items, first type: {type(experiments[0]) if experiments else \\\"empty\\\"}')\n\"\n",
  "description": "Parse registry dict structure for active experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9f8568fe-b80e-4ee9-b0d2-735453c24348",
  "isSidechain": false,
  "requestId": "req_011Cb5UxP1Fs172sBxY1Z7ti",
  "type": "assistant",
  "uuid": "55edb407-d041-4550-8fca-3f9fbac8fbda",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/.claude/sessions/agent_9c1243df",
  "sessionId": "ffa9d23f-27b7-4443-aea1-c7cdeeb2bf53",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YW2EAdtTNMhHFXXYCaiBLD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 519,
      "cache_read_input_tokens": 44772,
      "output_tokens": 558,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 519,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 558,
          "cache_read_input_tokens": 44772,
          "cache_creation_input_tokens": 519,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 519
          },
          "type": "message"
        }
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

_source line 35 · 2026-05-16T02:46:40.594Z_

<details><summary>↩ Tool result · `toolu_013kHaCow3FwgnbyMZjTR6tb`</summary>

```text
&lt;class 'dict'>
Total: 126, Active: 5
  c10_lang_switching: status=PREPARING, conclusion=—
  c9_gsm8k_power_analysis: status=PREPARING, conclusion=—
  c8_llama_n250: status=RUNNING, conclusion=—
  c5_per_phase_gini: status=PREPARING, conclusion=—
  c4_think_validation_math500: status=PREPARING, conclusion=—
  >> c4_think_validation_math500: status=PREPARING, conclusion=—
  >> c5_per_phase_gini: status=PREPARING, conclusion=—
  >> c9_gsm8k_power_analysis: status=PREPARING, conclusion=—
  >> c10_lang_switching: status=PREPARING, conclusion=—
  >> c8_llama_n250: status=RUNNING, conclusion=—
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "55edb407-d041-4550-8fca-3f9fbac8fbda",
  "isSidechain": false,
  "promptId": "d6a043a1-3c08-4fe7-9e57-50e76a38ea26",
  "type": "user",
  "uuid": "42c1719f-072a-4191-8793-fc4e8bb3f440",
  "toolUseResult": {
    "stdout": "&lt;class 'dict'>\nTotal: 126, Active: 5\n  c10_lang_switching: status=PREPARING, conclusion=—\n  c9_gsm8k_power_analysis: status=PREPARING, conclusion=—\n  c8_llama_n250: status=RUNNING, conclusion=—\n  c5_per_phase_gini: status=PREPARING, conclusion=—\n  c4_think_validation_math500: status=PREPARING, conclusion=—\n  >> c4_think_validation_math500: status=PREPARING, conclusion=—\n  >> c5_per_phase_gini: status=PREPARING, conclusion=—\n  >> c9_gsm8k_power_analysis: status=PREPARING, conclusion=—\n  >> c10_lang_switching: status=PREPARING, conclusion=—\n  >> c8_llama_n250: status=RUNNING, conclusion=—",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "55edb407-d041-4550-8fca-3f9fbac8fbda",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/.claude/sessions/agent_9c1243df",
  "sessionId": "ffa9d23f-27b7-4443-aea1-c7cdeeb2bf53",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 36 · 2026-05-16T02:47:06.103Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a clear picture:

**Active experiments:**
- c8_llama_n250: RUNNING (GPU, 4 cards, cron monitoring, pid=301187 still alive)
- c5_per_phase_gini: PREPARING (Worker running)
- c9_gsm8k_power_analysis: PREPARING (Worker running)
- c10_lang_switching: PREPARING (Worker running)
- c4_think_validation_math500: PREPARING (NO Worker running!)


I notice c4 is stuck in PREPARING without a Worker assigned, while the other three experiments each have one running. I need to spawn a Worker for c4 to get it moving. The Paper Agent tasks are waiting for CPU Worker callbacks, so they'll start once these are underway.

Looking at the paper tasks more carefully though, some of them don't actually depend on the CPU Worker results — the bibliography audit and Abstract/Intro rewrite can start now since the core findings are already locked in. The sections that need c5's per-phase Gini results will have to wait, but I could get the independent writing work started in parallel.

The handoff is explicit about waiting for all 4 CPU Workers to finish before spawning the Paper Agent, so I should respect that constraint even if it's not perfectly efficient. Though I should definitely spawn the c4 Worker immediately since that's a clear gap. With the EMNLP 2026 deadline looming, I need to think about whether this sequential approach actually leaves enough time. With the 9-day deadline, I need to prioritize parallelism—spawning the c4 validation worker immediately while also checking the resource-saturation skill to understand capacity constraints before reporting to the Director. Given the time pressure, I'll start the c4 worker first, then review the skill requirements and consider whether to launch independent paper tasks concurrently.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "42c1719f-072a-4191-8793-fc4e8bb3f440",
  "isSidechain": false,
  "requestId": "req_011Cb5UxxVeNFR1xocLkt1xy",
  "type": "assistant",
  "uuid": "1245c296-5dfc-464f-b01d-f2e705fc223f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/.claude/sessions/agent_9c1243df",
  "sessionId": "ffa9d23f-27b7-4443-aea1-c7cdeeb2bf53",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014SVGse3Eo2o5XyypfzTBw8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 786,
      "cache_read_input_tokens": 45291,
      "output_tokens": 1321,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 786,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1321,
          "cache_read_input_tokens": 45291,
          "cache_creation_input_tokens": 786,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 786
          },
          "type": "message"
        }
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

_source line 37 · 2026-05-16T02:47:06.298Z_

状态确认完毕。关键发现：**c4_think_validation_math500 处于 PREPARING 但无 Worker 在跑** — 这是一个缺口，需要立即补派。

加载 spawn_worker 和 resource-saturation skill。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1245c296-5dfc-464f-b01d-f2e705fc223f",
  "isSidechain": false,
  "requestId": "req_011Cb5UxxVeNFR1xocLkt1xy",
  "type": "assistant",
  "uuid": "172a7d57-99e6-4bab-aa12-92f228504f39",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/.claude/sessions/agent_9c1243df",
  "sessionId": "ffa9d23f-27b7-4443-aea1-c7cdeeb2bf53",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014SVGse3Eo2o5XyypfzTBw8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 786,
      "cache_read_input_tokens": 45291,
      "output_tokens": 1321,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 786,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1321,
          "cache_read_input_tokens": 45291,
          "cache_creation_input_tokens": 786,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 786
          },
          "type": "message"
        }
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

_source line 38 · 2026-05-16T02:47:07.776Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01NCpzyFbd8QD8PUd1VJHmFj`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__spawn_worker,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__send_progress",
  "max_results": 4
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "172a7d57-99e6-4bab-aa12-92f228504f39",
  "isSidechain": false,
  "requestId": "req_011Cb5UxxVeNFR1xocLkt1xy",
  "type": "assistant",
  "uuid": "b71846ed-0342-4e21-be14-693f989e94d5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/.claude/sessions/agent_9c1243df",
  "sessionId": "ffa9d23f-27b7-4443-aea1-c7cdeeb2bf53",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014SVGse3Eo2o5XyypfzTBw8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 786,
      "cache_read_input_tokens": 45291,
      "output_tokens": 1321,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 786,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1321,
          "cache_read_input_tokens": 45291,
          "cache_creation_input_tokens": 786,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 786
          },
          "type": "message"
        }
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

_source line 39 · 2026-05-16T02:47:08.257Z_

<details><summary>↩ Tool result · reported error · `toolu_01VgAPoxXkNY6QwBxuFyTnUb`</summary>

```text
File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/.claude/sessions/agent_9c1243df.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a87f5133-1baf-4300-8e16-08fbc38dcd22",
  "isSidechain": false,
  "promptId": "d6a043a1-3c08-4fe7-9e57-50e76a38ea26",
  "type": "user",
  "uuid": "43cf5f5f-1eb2-489a-bb4e-431ade1098a5",
  "toolUseResult": "Error: File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/.claude/sessions/agent_9c1243df.",
  "sourceToolAssistantUUID": "a87f5133-1baf-4300-8e16-08fbc38dcd22",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/.claude/sessions/agent_9c1243df",
  "sessionId": "ffa9d23f-27b7-4443-aea1-c7cdeeb2bf53",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-16T02:47:07.784Z_

<details><summary>↩ Tool result · `toolu_01NCpzyFbd8QD8PUd1VJHmFj`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__spawn_worker"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__update_registry"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__save_project_file"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__send_progress"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b71846ed-0342-4e21-be14-693f989e94d5",
  "isSidechain": false,
  "promptId": "d6a043a1-3c08-4fe7-9e57-50e76a38ea26",
  "type": "user",
  "uuid": "45dbb6d4-6d5a-4d4e-9f7c-7afa5c7c2de3",
  "toolUseResult": {
    "matches": [
      "mcp__agent-ml-research__spawn_worker",
      "mcp__agent-ml-research__update_registry",
      "mcp__agent-ml-research__save_project_file",
      "mcp__agent-ml-research__send_progress"
    ],
    "query": "select:mcp__agent-ml-research__spawn_worker,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__send_progress",
    "total_deferred_tools": 79
  },
  "sourceToolAssistantUUID": "b71846ed-0342-4e21-be14-693f989e94d5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/.claude/sessions/agent_9c1243df",
  "sessionId": "ffa9d23f-27b7-4443-aea1-c7cdeeb2bf53",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-16T02:47:08.248Z_

<details open><summary>🔧 Tool call — Read · `toolu_01VgAPoxXkNY6QwBxuFyTnUb`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/.claude/skills/resource-saturation.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "45dbb6d4-6d5a-4d4e-9f7c-7afa5c7c2de3",
  "isSidechain": false,
  "requestId": "req_011Cb5UxxVeNFR1xocLkt1xy",
  "type": "assistant",
  "uuid": "a87f5133-1baf-4300-8e16-08fbc38dcd22",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/.claude/sessions/agent_9c1243df",
  "sessionId": "ffa9d23f-27b7-4443-aea1-c7cdeeb2bf53",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014SVGse3Eo2o5XyypfzTBw8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 786,
      "cache_read_input_tokens": 45291,
      "output_tokens": 1321,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 786,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1321,
          "cache_read_input_tokens": 45291,
          "cache_creation_input_tokens": 786,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 786
          },
          "type": "message"
        }
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

_source line 42 · 2026-05-16T02:47:11.700Z_

<details><summary>Logged reasoning block</summary>

```text
The resource-saturation skill file wasn't found at that path. Let me find it.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "43cf5f5f-1eb2-489a-bb4e-431ade1098a5",
  "isSidechain": false,
  "requestId": "req_011Cb5V111WT1NPtsbRH5ymy",
  "type": "assistant",
  "uuid": "5ab2f19a-61b4-472d-966a-39314c27bdb8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/.claude/sessions/agent_9c1243df",
  "sessionId": "ffa9d23f-27b7-4443-aea1-c7cdeeb2bf53",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VMSsyGdfwRKF3ButzYU8Nf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3424,
      "cache_read_input_tokens": 46077,
      "output_tokens": 131,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3424,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 131,
          "cache_read_input_tokens": 46077,
          "cache_creation_input_tokens": 3424,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3424
          },
          "type": "message"
        }
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

_source line 43 · 2026-05-16T02:47:11.895Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01Vy7eYGnmfjJvZCgmH4nR2p`</summary>

```json
{
  "pattern": "**/resource-saturation.skill.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5ab2f19a-61b4-472d-966a-39314c27bdb8",
  "isSidechain": false,
  "requestId": "req_011Cb5V111WT1NPtsbRH5ymy",
  "type": "assistant",
  "uuid": "0dc7a9c6-c672-4673-8a29-01c5f9521d69",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/.claude/sessions/agent_9c1243df",
  "sessionId": "ffa9d23f-27b7-4443-aea1-c7cdeeb2bf53",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VMSsyGdfwRKF3ButzYU8Nf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3424,
      "cache_read_input_tokens": 46077,
      "output_tokens": 131,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3424,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 131,
          "cache_read_input_tokens": 46077,
          "cache_creation_input_tokens": 3424,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3424
          },
          "type": "message"
        }
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

_source line 44 · 2026-05-16T02:47:11.922Z_

<details><summary>↩ Tool result · `toolu_01Vy7eYGnmfjJvZCgmH4nR2p`</summary>

```text
No files found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0dc7a9c6-c672-4673-8a29-01c5f9521d69",
  "isSidechain": false,
  "promptId": "d6a043a1-3c08-4fe7-9e57-50e76a38ea26",
  "type": "user",
  "uuid": "8d0380c1-0c90-455b-8bf9-04e689aa0b2d",
  "toolUseResult": {
    "filenames": [],
    "durationMs": 21,
    "numFiles": 0,
    "truncated": false
  },
  "sourceToolAssistantUUID": "0dc7a9c6-c672-4673-8a29-01c5f9521d69",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/.claude/sessions/agent_9c1243df",
  "sessionId": "ffa9d23f-27b7-4443-aea1-c7cdeeb2bf53",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 45_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[HANDOFF] 你是 Main Agent，这是 Loop #15。  ## 上一轮交接 (task_context)  ### 1. 🔴 硬约束 / 红线 - GPU 白名单：**westd-22162 cuda:0~3** 仅此 4 张，不可用其他 GPU - c8_llama_n250 正在占满 4 GPU（4 并行推理），完成前不可提交新 GPU 实验 - EMNLP 2026 AR…",
  "leafUuid": "8d0380c1-0c90-455b-8bf9-04e689aa0b2d",
  "sessionId": "ffa9d23f-27b7-4443-aea1-c7cdeeb2bf53"
}
```

---

### Runtime record

_source line 46_

```json
{
  "type": "ai-title",
  "aiTitle": "Verify active experiments and paper revisions for EMNLP 2026",
  "sessionId": "ffa9d23f-27b7-4443-aea1-c7cdeeb2bf53"
}
```

---

### Tool call

_source line 47 · 2026-05-16T02:47:14.428Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01E3b4iUdaabMrkXztHN3UtJ`</summary>

```json
{
  "pattern": "**/resource-saturation*",
  "path": "/home/ubuntu/agent-ml-research"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8d0380c1-0c90-455b-8bf9-04e689aa0b2d",
  "isSidechain": false,
  "requestId": "req_011Cb5V1GYeqkyfaj1nTxLdy",
  "type": "assistant",
  "uuid": "c68d6e94-669a-472a-991d-5fa09ac24262",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/.claude/sessions/agent_9c1243df",
  "sessionId": "ffa9d23f-27b7-4443-aea1-c7cdeeb2bf53",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016QhDp4VHVaWL8ghba4ZL8N",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 147,
      "cache_read_input_tokens": 49501,
      "output_tokens": 84,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 147,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 84,
          "cache_read_input_tokens": 49501,
          "cache_creation_input_tokens": 147,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 147
          },
          "type": "message"
        }
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

_source line 48 · 2026-05-16T02:47:14.583Z_

<details><summary>↩ Tool result · `toolu_01E3b4iUdaabMrkXztHN3UtJ`</summary>

```text
/home/ubuntu/agent-ml-research/skills/global/resource-saturation.skill.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c68d6e94-669a-472a-991d-5fa09ac24262",
  "isSidechain": false,
  "promptId": "d6a043a1-3c08-4fe7-9e57-50e76a38ea26",
  "type": "user",
  "uuid": "9f947e03-ebe3-43f5-b1dd-1b114b8c975f",
  "toolUseResult": {
    "filenames": [
      "/home/ubuntu/agent-ml-research/skills/global/resource-saturation.skill.md"
    ],
    "durationMs": 152,
    "numFiles": 1,
    "truncated": false
  },
  "sourceToolAssistantUUID": "c68d6e94-669a-472a-991d-5fa09ac24262",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/.claude/sessions/agent_9c1243df",
  "sessionId": "ffa9d23f-27b7-4443-aea1-c7cdeeb2bf53",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-16T02:47:17.201Z_

<details open><summary>🔧 Tool call — Read · `toolu_017G2viM9DWEBAdaUPqp2X6o`</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/resource-saturation.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9f947e03-ebe3-43f5-b1dd-1b114b8c975f",
  "isSidechain": false,
  "requestId": "req_011Cb5V1TpZX41Cw2QqpTSxn",
  "type": "assistant",
  "uuid": "89735e1b-1ba3-4dc6-b846-16ce2a4a7aa4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/.claude/sessions/agent_9c1243df",
  "sessionId": "ffa9d23f-27b7-4443-aea1-c7cdeeb2bf53",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TE8c8rNzDRPPdTpTdBGUXX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 118,
      "cache_read_input_tokens": 49648,
      "output_tokens": 75,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 118,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 75,
          "cache_read_input_tokens": 49648,
          "cache_creation_input_tokens": 118,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 118
          },
          "type": "message"
        }
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

_source line 50 · 2026-05-16T02:47:17.212Z_

<details><summary>↩ Tool result · `toolu_017G2viM9DWEBAdaUPqp2X6o`</summary>

```text
1	---
2	name: resource-saturation
3	description: "当你准备向 Director 汇报前、收到 cron/worker 回调、审批通过准备开跑、怀疑 Worker 池不够饱和时,立即使用本 skill。四部分:A) GPU 分配率(分配了没跑=失职) B) GPU 效率 C) 非 GPU 任务并行(Worker 池<2=失职) D) 汇报必须带 [资源] 行。"
4	always: false
5	roles:
6	  - director
7	  - agent
8	---
9	
10	# 资源饱和度自检（硬约束）
11	
12	## A. GPU 分配率检查
13	
14	调 `get_project_resource_usage(project)` 看:
15	- 已分配给本项目的 GPU 总数和具体卡号
16	- 实际在跑任务的 GPU 数和具体卡号（交叉 registry RUNNING + nvidia-smi 进程）
17	- 分配了但没跑的 GPU 清单 ⚠️
18	
19	任何"分配了但没跑"的 GPU = 失职。必须立即:
20	- 派 Worker 铺 dry-run / 下一批实验代码准备
21	- 铺 ablation（从 experiment-matrix 空白格子里挑）
22	- 确实无实验可铺 → 向 Director 汇报"暂无可铺实验"+ 建议下一步方向(扩 ablation 维度 / 加 baseline / 加 benchmark)。**不要建议归还 GPU**——项目级 GPU 归还只在归档时由 `archive_project` 自动触发, 不是 Director 中途的动作
23	
24	**单实验不占多卡**: 分配 4 卡但实验只用 1 卡 → 另 3 卡必须并行跑其他实验,不能空占。
25	
26	## B. GPU 效率检查
27	
28	调 `get_gpu_health(server)`:
29	- 空闲 GPU（util < 10% 持续 > 5 min）→ 立即铺任务
30	- 低利用率（util < 50% 持续 > 15 min）→ spawn_worker 诊断（batch / IO / 同步）
31	- OOM 风险（显存 > 90% 持续 10 min）→ 主动降 batch / 调优
32	
33	## C. 非 GPU 任务并行
34	
35	GPU 在跑 ≠ 你空闲。以下 CPU / 网络任务**必须**派独立 Worker 并行:
36	- 下一批实验的数据集下载 / 预处理 / fingerprint
37	- 下一批实验的代码准备 / dry-run / 环境配置
38	- 论文文献调研 / related work 检索
39	- 已完成实验的 log 深度分析 / metric 聚合
40	- 论文章节起草
41	- 代码 review / refactor
42	
43	**硬约束**: 任一时刻 Worker 池 < 2 个 = 失职（除非真的全部下游阻塞在等 GPU,这时应当向 Director 申请扩 GPU）。
44	
45	## D. 汇报格式
46	
47	向 Director 汇报时开头必须带资源声明行:
48	
49	    [资源] GPU 分配 N / 实际在跑 M | Worker 池 K (其中 GPU 任务 A / CPU 任务 B)
50	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "89735e1b-1ba3-4dc6-b846-16ce2a4a7aa4",
  "isSidechain": false,
  "promptId": "d6a043a1-3c08-4fe7-9e57-50e76a38ea26",
  "type": "user",
  "uuid": "9968be3e-2d11-400c-8cf6-4b0adec375e3",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/agent-ml-research/skills/global/resource-saturation.skill.md",
      "content": "---\nname: resource-saturation\ndescription: \"当你准备向 Director 汇报前、收到 cron/worker 回调、审批通过准备开跑、怀疑 Worker 池不够饱和时,立即使用本 skill。四部分:A) GPU 分配率(分配了没跑=失职) B) GPU 效率 C) 非 GPU 任务并行(Worker 池<2=失职) D) 汇报必须带 [资源] 行。\"\nalways: false\nroles:\n  - director\n  - agent\n---\n\n# 资源饱和度自检（硬约束）\n\n## A. GPU 分配率检查\n\n调 `get_project_resource_usage(project)` 看:\n- 已分配给本项目的 GPU 总数和具体卡号\n- 实际在跑任务的 GPU 数和具体卡号（交叉 registry RUNNING + nvidia-smi 进程）\n- 分配了但没跑的 GPU 清单 ⚠️\n\n任何\"分配了但没跑\"的 GPU = 失职。必须立即:\n- 派 Worker 铺 dry-run / 下一批实验代码准备\n- 铺 ablation（从 experiment-matrix 空白格子里挑）\n- 确实无实验可铺 → 向 Director 汇报\"暂无可铺实验\"+ 建议下一步方向(扩 ablation 维度 / 加 baseline / 加 benchmark)。**不要建议归还 GPU**——项目级 GPU 归还只在归档时由 `archive_project` 自动触发, 不是 Director 中途的动作\n\n**单实验不占多卡**: 分配 4 卡但实验只用 1 卡 → 另 3 卡必须并行跑其他实验,不能空占。\n\n## B. GPU 效率检查\n\n调 `get_gpu_health(server)`:\n- 空闲 GPU（util < 10% 持续 > 5 min）→ 立即铺任务\n- 低利用率（util < 50% 持续 > 15 min）→ spawn_worker 诊断（batch / IO / 同步）\n- OOM 风险（显存 > 90% 持续 10 min）→ 主动降 batch / 调优\n\n## C. 非 GPU 任务并行\n\nGPU 在跑 ≠ 你空闲。以下 CPU / 网络任务**必须**派独立 Worker 并行:\n- 下一批实验的数据集下载 / 预处理 / fingerprint\n- 下一批实验的代码准备 / dry-run / 环境配置\n- 论文文献调研 / related work 检索\n- 已完成实验的 log 深度分析 / metric 聚合\n- 论文章节起草\n- 代码 review / refactor\n\n**硬约束**: 任一时刻 Worker 池 < 2 个 = 失职（除非真的全部下游阻塞在等 GPU,这时应当向 Director 申请扩 GPU）。\n\n## D. 汇报格式\n\n向 Director 汇报时开头必须带资源声明行:\n\n    [资源] GPU 分配 N / 实际在跑 M | Worker 池 K (其中 GPU 任务 A / CPU 任务 B)\n",
      "numLines": 50,
      "startLine": 1,
      "totalLines": 50
    }
  },
  "sourceToolAssistantUUID": "89735e1b-1ba3-4dc6-b846-16ce2a4a7aa4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/.claude/sessions/agent_9c1243df",
  "sessionId": "ffa9d23f-27b7-4443-aea1-c7cdeeb2bf53",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 51 · 2026-05-16T02:47:44.917Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a clear picture. Let me do the resource saturation check:

**A. GPU 分配率**: 4 GPU (cuda:0~3), c8_llama_n250 occupying all 4 → 4/4 in use. OK.

**B. GPU 效率**: c8_llama_n250 is running 4 parallel inference processes. Cron confirms pid=301187 still alive. OK.

**C. 非 GPU 任务并行**: 
- 3 Workers running: c5_per_phase_gini, c9_gsm8k_power, c10_lang_switching


- c4_think_validation_math500 is missing a Worker, so I need to spawn one immediately. After that, the pool goes from 3 to 4 Workers, with GPU taking 1 and CPU handling the remaining 3.

**D. 汇报格式**: [资源] GPU 分配 4 / 实际在跑 4 | Worker 池 3→4 (GPU 1 / CPU 3→4)

For the paper tasks, the handoff says to wait for CPU Worker callbacks, but some of them like the bibliography audit and abstract are independent enough that I could start spawning them now without blocking on other dependencies.

Looking at what's truly independent versus what needs experimental results: the editorial fixes like removing the fake MUSTAFAR citation, anonymizing GPU references, adjusting contribution language, and fixing causal phrasing can all happen immediately. The sections that actually depend on experimental evidence—like the Intro rewrite, sections 4-7 corrections, and appendix fixes tied to c9 and c5—those are the ones that need to wait. Given the 9-day deadline and the principle of aggressive parallelization, I should spawn the independent paper tasks now while respecting the handoff's intent to prioritize the CPU Worker callbacks.

The real tension is whether to spawn paper Workers piecemeal or wait for a coherent pass. The bibliography audit is genuinely independent—it's just removing MUSTAFAR and validating the rest—so that's safe to start immediately. But I need to be careful not to fragment the revision process too much. Let me spawn the validation work on the math500 thinking and the bibliography audit, since those are both clearly independent and high-priority.

For the c4 validation, I'm checking what the experiment actually requires. From the handoff, it's validating that the `&lt;think>` token positions align with the PPL-based phase segmentation across the DS and QW models. That's a straightforward analysis task on existing data, not a training run.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9968be3e-2d11-400c-8cf6-4b0adec375e3",
  "isSidechain": false,
  "requestId": "req_011Cb5V1fFu6FTaZ6qzUnsqD",
  "type": "assistant",
  "uuid": "09a80426-9706-4bd5-86af-b395ce3ae4f0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/.claude/sessions/agent_9c1243df",
  "sessionId": "ffa9d23f-27b7-4443-aea1-c7cdeeb2bf53",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015a1oHwiAVLEY1fYJ5p2kJm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1147,
      "cache_read_input_tokens": 49766,
      "output_tokens": 1140,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1147,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1140,
          "cache_read_input_tokens": 49766,
          "cache_creation_input_tokens": 1147,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1147
          },
          "type": "message"
        }
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

_source line 52 · 2026-05-16T02:47:44.952Z_

需要读实验计划获取 c4 的详细规格，同时检查 c4 相关背景。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "09a80426-9706-4bd5-86af-b395ce3ae4f0",
  "isSidechain": false,
  "requestId": "req_011Cb5V1fFu6FTaZ6qzUnsqD",
  "type": "assistant",
  "uuid": "1ee94807-c1c9-46c4-936e-b34f61bf0c48",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/.claude/sessions/agent_9c1243df",
  "sessionId": "ffa9d23f-27b7-4443-aea1-c7cdeeb2bf53",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015a1oHwiAVLEY1fYJ5p2kJm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1147,
      "cache_read_input_tokens": 49766,
      "output_tokens": 1140,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1147,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1140,
          "cache_read_input_tokens": 49766,
          "cache_creation_input_tokens": 1147,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1147
          },
          "type": "message"
        }
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

_source line 53 · 2026-05-16T02:47:45.377Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_0154hcstij9j12QEEETfm2QM`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_experiment_plan_with_status",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1ee94807-c1c9-46c4-936e-b34f61bf0c48",
  "isSidechain": false,
  "requestId": "req_011Cb5V1fFu6FTaZ6qzUnsqD",
  "type": "assistant",
  "uuid": "883c46e8-8df1-4bf4-8eda-204a48a5e9c0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/.claude/sessions/agent_9c1243df",
  "sessionId": "ffa9d23f-27b7-4443-aea1-c7cdeeb2bf53",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015a1oHwiAVLEY1fYJ5p2kJm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1147,
      "cache_read_input_tokens": 49766,
      "output_tokens": 1140,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1147,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1140,
          "cache_read_input_tokens": 49766,
          "cache_creation_input_tokens": 1147,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1147
          },
          "type": "message"
        }
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

_source line 54 · 2026-05-16T02:47:45.385Z_

<details><summary>↩ Tool result · `toolu_0154hcstij9j12QEEETfm2QM`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__read_experiment_plan_with_status"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "883c46e8-8df1-4bf4-8eda-204a48a5e9c0",
  "isSidechain": false,
  "promptId": "d6a043a1-3c08-4fe7-9e57-50e76a38ea26",
  "type": "user",
  "uuid": "c5596446-b62c-4074-b28e-1649ba5b0ab3",
  "toolUseResult": {
    "matches": [
      "mcp__agent-ml-research__read_experiment_plan_with_status"
    ],
    "query": "select:mcp__agent-ml-research__read_experiment_plan_with_status",
    "total_deferred_tools": 79
  },
  "sourceToolAssistantUUID": "883c46e8-8df1-4bf4-8eda-204a48a5e9c0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/.claude/sessions/agent_9c1243df",
  "sessionId": "ffa9d23f-27b7-4443-aea1-c7cdeeb2bf53",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-16T02:47:47.692Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_experiment_plan_with_status · `toolu_01Uxf8BXk7oDPLbTAcg6m6fW`</summary>

```json
{
  "project": "phase-gated-compound-sparse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c5596446-b62c-4074-b28e-1649ba5b0ab3",
  "isSidechain": false,
  "requestId": "req_011Cb5V3jjLDNPWzUWrbAomM",
  "type": "assistant",
  "uuid": "1c869f6a-2638-4ba9-832e-ecdb9d44f06d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/.claude/sessions/agent_9c1243df",
  "sessionId": "ffa9d23f-27b7-4443-aea1-c7cdeeb2bf53",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018D7NKUGu7SacDuPmLvUQVm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1366,
      "cache_read_input_tokens": 50913,
      "output_tokens": 76,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1366,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 76,
          "cache_read_input_tokens": 50913,
          "cache_creation_input_tokens": 1366,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1366
          },
          "type": "message"
        }
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

_source line 56 · 2026-05-16T02:47:48.132Z_

<details><summary>↩ Tool result · `toolu_01Uxf8BXk7oDPLbTAcg6m6fW`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": [{\"id\": \"c1_bf16_importance_s025\", \"claim\": \"C1\", \"description\": \"II median: high=0.032, mid=1.118, low=7.196; importance masking shows strong phase gradient\", \"registry_id\": \"bf16_importance_s025\", \"role\": \"primary\", \"priority\": \"high\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"interaction_index\": {\"high\": {\"mean\": 0.302756, \"median\": 0.032363, \"ci\": [0.083714, 0.543977], \"winsorized_mean\": 0.200962, \"skewness\": 4.8826}, \"mid\": {\"mean\": 5.729665, \"median\": 1.118069, \"ci\": [3.455574, 8.471799], \"winsorized_mean\": 4.189902, \"skewness\": 8.2799}, \"low\": {\"mean\": 25.852951, \"median\": 7.195958, \"ci\": [19.077082, 33.497293], \"winsorized_mean\": 19.319103, \"skewness\": 7.3986}}, \"per_problem_ii_stats\": {\"high\": {\"n\": 49, \"min\": -0.316321, \"max\": 4.003714, \"mean\": 0.133714, \"median\": 0.009873, \"std\": 0.595358}, \"mid\": {\"n\": 40, \"min\": -0.024794, \"max\": 18.720486, \"mean\": 2.537744, \"median\": 1.05707, \"std\": 3.962575}, \"low\": {\"n\": 50, \"min\": -1.854733, \"max\": 75.467653, \"mean\": 11.28281, \"median\": 3.954593, \"std\": 16.620011}}, \"gradient_paired_aggregate_legacy\": 222.35, \"median_difference\": 7.1636, \"n_problems\": 50, \"pass_fail\": {\"ci_overlap\": true, \"sign_reversal\": false, \"overall\": \"PASS\"}, \"phase_stats\": {\"high\": {\"n_tokens\": 21086, \"n_segments\": 387}, \"mid\": {\"n_tokens\": 13306, \"n_segments\": 191}, \"low\": {\"n_tokens\": 27748, \"n_segments\": 397}}, \"perplexity\": {\"high\": {\"dense\": 1.1689, \"attn\": 1.6511, \"kv\": 1.8628, \"both\": 2.7026}, \"mid\": {\"dense\": 1.2269, \"attn\": 1.7039, \"kv\": 5.6205, \"both\": 13.3436}, \"low\": {\"dense\": 1.2286, \"attn\": 1.8366, \"kv\": 31.756, \"both\": 63.668}}}}, {\"id\": \"c1_bf16_ds_rand_s025\", \"claim\": \"C1\", \"description\": \"Random II median: high=0.818, mid=0.932, low=1.363; flat gradient vs importance\", \"registry_id\": \"bf16_ds_rand_s025\", \"role\": \"primary\", \"priority\": \"high\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"interaction_index\": {\"high\": {\"mean\": 3.59, \"median\": 0.8182, \"ci\": [1.4021, 6.2327], \"median_ci\": [0.5075, 1.7217], \"winsorized_mean\": 6.3965, \"skewness\": -7.57}, \"mid\": {\"mean\": -1.8455, \"median\": 0.9324, \"ci\": [-10.3663, 4.9342], \"median_ci\": [0.7331, 1.7003], \"winsorized_mean\": 3.1014, \"skewness\": -12.76}, \"low\": {\"mean\": 0.7212, \"median\": 1.3627, \"ci\": [-4.2068, 4.5006], \"median_ci\": [1.0869, 2.6866], \"winsorized_mean\": 4.1866, \"skewness\": -15.85}}, \"perplexity\": {\"high\": {\"dense\": 1.1687, \"attn\": 7.237, \"kv\": 4.9751, \"both\": 17.7423}, \"mid\": {\"dense\": 1.2269, \"attn\": 868.3199, \"kv\": 5.1165, \"both\": 29.4661}, \"low\": {\"dense\": 1.2284, \"attn\": 24.3571, \"kv\": 6.7993, \"both\": 17.9694}}, \"phase_stats\": {\"high\": {\"n_tokens\": 21086, \"n_segments\": 387}, \"mid\": {\"n_tokens\": 13306, \"n_segments\": 191}, \"low\": {\"n_tokens\": 27748, \"n_segments\": 397}}, \"n_problems\": 50, \"pass_fail\": {\"ci_overlap\": false, \"sign_reversal\": false, \"overall\": \"FAIL\"}, \"median_difference\": 0.5445}}, {\"id\": \"c1_bf16_qw_imp_s025\", \"claim\": \"C1\", \"description\": \"Qwen cross-model: median_diff=1.109, Cohen's d=1.233, p<1e-5\", \"registry_id\": \"bf16_qw_imp_s025\", \"role\": \"supporting\", \"priority\": \"medium\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"median_difference\": 1.108706, \"permutation_p\": 0, \"cohens_d\": 1.2329, \"bootstrap_ci_95\": [0.609247, 1.469002], \"wilcoxon_p\": 0, \"n_bootstrap\": 10000, \"n_paired\": 46}}, {\"id\": \"c1_sf5_asymmetric_spot\", \"claim\": \"C1\", \"description\": \"Asymmetric configs: h02_kv03 D=19.13, h03_kv02 D=18.25; gradient consistent\", \"registry_id\": \"sf5_asymmetric_spot\", \"role\": \"ablation\", \"priority\": \"medium\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"config_a_h02_kv03\": {\"II_low\": 19.51, \"II_mid\": 6.05, \"II_high\": 0.38, \"D\": 19.13}, \"config_b_h03_kv02\": {\"II_low\": 18.77, \"II_mid\": 3.97, \"II_high\": 0.52, \"D\": 18.25}, \"pre_registered_criterion_passed\": true, \"gradient_direction\": \"II_low >> II_mid >> II_high (consistent with symmetric baseline)\"}}, {\"id\": \"c1_c2_accuracy_eval\", \"claim\": \"C1\", \"description\": \"DS dense->s030 acc: 0.52->0.10 (-0.42); QW dense->s030: 0.32->0.14 (-0.18)\", \"registry_id\": \"c2_accuracy_eval\", \"role\": \"supporting\", \"priority\": \"medium\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"n_problems\": 50, \"ds_dense_acc\": 0.52, \"ds_s015_acc\": 0.36, \"ds_s015_delta\": -0.16, \"ds_s030_acc\": 0.1, \"ds_s030_delta\": -0.42, \"qw_dense_acc\": 0.32, \"qw_s015_acc\": 0.34, \"qw_s015_delta\": 0.02, \"qw_s030_acc\": 0.14, \"qw_s030_delta\": -0.18, \"ds_s030_chinese_reasoning_rate\": 0.4, \"ds_dense_truncation_rate\": 0.56, \"note\": \"v2 rescored with fixed radical+degree matcher. DS s015 34→36, QW s015 32→34\"}}, {\"id\": \"c2_bf16_importance_s030\", \"claim\": \"C2\", \"description\": \"Phase gradient: II low=14.64 >> mid=2.28 >> high=0.053 (median); low/high ratio ~276x\", \"registry_id\": \"bf16_importance_s030\", \"role\": \"primary\", \"priority\": \"high\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"interaction_index\": {\"high\": {\"mean\": 0.5547, \"median\": 0.0534, \"ci\": [0.2773, 0.9198], \"winsorized_mean\": 0.3367, \"skewness\": 10.62}, \"mid\": {\"mean\": 11.3, \"median\": 2.2833, \"ci\": [6.865, 17.2633], \"winsorized_mean\": 8.1752, \"skewness\": 9.19}, \"low\": {\"mean\": 57.7946, \"median\": 14.6395, \"ci\": [41.4416, 77.0467], \"winsorized_mean\": 39.3143, \"skewness\": 8.31}}, \"per_problem_ii_stats\": {\"high\": {\"n\": 49, \"min\": -0.5095, \"max\": 4.4457, \"mean\": 0.1976, \"median\": 0.0343, \"std\": 0.6793}, \"mid\": {\"n\": 40, \"min\": -0.1989, \"max\": 34.0258, \"mean\": 5.2585, \"median\": 1.5173, \"std\": 7.9382}, \"low\": {\"n\": 50, \"min\": -7.3027, \"max\": 126.7985, \"mean\": 22.6601, \"median\": 9.9731, \"std\": 28.4096}}, \"gradient_paired_aggregate_legacy\": 57.24, \"median_difference\": 14.5861, \"n_problems\": 50, \"pass_fail\": {\"ci_overlap\": true, \"sign_reversal\": false, \"overall\": \"PASS\"}, \"phase_stats\": {\"high\": {\"n_tokens\": 21086, \"n_segments\": 387}, \"mid\": {\"n_tokens\": 13306, \"n_segments\": 191}, \"low\": {\"n_tokens\": 27748, \"n_segments\": 397}}, \"perplexity\": {\"high\": {\"dense\": 1.1689, \"attn\": 1.7123, \"kv\": 2.0544, \"both\": 3.2372}, \"mid\": {\"dense\": 1.2269, \"attn\": 1.7894, \"kv\": 9.4821, \"both\": 24.2847}, \"low\": {\"dense\": 1.2286, \"attn\": 1.9347, \"kv\": 51.6485, \"both\": 122.61}}}}, {\"id\": \"c2_v6_importance_s030\", \"claim\": \"C2\", \"description\": \"II low_median=34.69, mid_median=7.27, high_median=0.88; bootstrap_gradient=41.92, CI=[19.14,299.76]\", \"registry_id\": \"v6_importance_s030\", \"role\": \"primary\", \"priority\": \"high\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"ii_high_median\": 0.8833, \"ii_mid_median\": 7.2706, \"ii_low_median\": 34.6937, \"ii_high_mean\": 1.5151, \"ii_mid_mean\": 78.8215, \"ii_low_mean\": 1163.9677, \"per_problem_ii_count\": 50, \"n_high\": 40, \"n_mid\": 22, \"n_low\": 20, \"problems\": 50, \"bootstrap_gradient_paired\": 41.92, \"bootstrap_ci_paired\": [19.14, 299.76], \"bootstrap_gradient_unpaired\": 39.28, \"bootstrap_ci_unpaired\": [21.87, 129.59], \"bootstrap_p\": 0}}, {\"id\": \"c2_think_phase_validation\", \"claim\": \"C2\", \"description\": \"Phase segmentation kappa=0.887; thinking=57.8% low-sparsity, answer=62.7% high-sparsity\", \"registry_id\": \"think_phase_validation\", \"role\": \"supporting\", \"priority\": \"medium\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"effective_n\": 48, \"skipped_problems\": 2, \"median_kappa\": 0.887, \"thinking_in_low_sparsity_phase\": 0.578, \"answer_in_high_sparsity_phase\": 0.627, \"note\": \"Phase segmentation based on dense model — 4 sparsity conditions share identical phase boundaries, effective sample n=48 not n=192\"}}, {\"id\": \"c2_acc_qw_s030_n100\", \"claim\": \"C2\", \"description\": \"QW importance s030 accuracy=0.19 (n=100); dose-response monotonic decline from dense=0.40\", \"registry_id\": \"acc_qw_s030_n100\", \"role\": \"supporting\", \"priority\": \"medium\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"batch1_correct\": 7, \"batch1_total\": 50, \"batch1_acc\": 0.14, \"batch1_source\": \"acc_qw_s030_b1_8k (v2, 8k tokens)\", \"batch2_correct\": 12, \"batch2_total\": 50, \"batch2_acc\": 0.24, \"combined_correct\": 19, \"combined_total\": 100, \"combined_acc\": 0.19}}, {\"id\": \"c2_acc_ds_s015_8k_v2\", \"claim\": \"C2\", \"description\": \"DS s015 accuracy=0.48 vs dense=0.74; early onset of compound degradation\", \"registry_id\": \"acc_ds_s015_8k_v2\", \"role\": \"supporting\", \"priority\": \"medium\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 0.48, \"correct\": 24, \"total\": 50, \"truncation_rate\": 0.32, \"truncated_count\": 16, \"non_truncated_accuracy\": 0.706, \"non_truncated_correct\": 24, \"non_truncated_total\": 34, \"wall_time_s\": 3967, \"max_new_tokens\": 8192}}, {\"id\": \"c3_v6_importance_s025\", \"claim\": \"C3\", \"description\": \"Importance: II low_median=24.16 >> high_median=0.66; strong phase gradient (36x ratio)\", \"registry_id\": \"v6_importance_s025\", \"role\": \"primary\", \"priority\": \"high\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"ii_high_median\": 0.6641, \"ii_mid_median\": 5.3067, \"ii_low_median\": 24.1619, \"ii_high_mean\": 0.8842, \"ii_mid_mean\": 10.057, \"ii_low_mean\": 71.8854, \"per_problem_ii_count\": 50, \"n_high\": 42, \"n_mid\": 23, \"n_low\": 21, \"problems\": 50, \"bootstrap_gradient_paired\": 35.72, \"bootstrap_ci_paired\": [9.52, 101.54], \"bootstrap_gradient_unpaired\": 36.38, \"bootstrap_ci_unpaired\": [13.19, 97.61], \"bootstrap_p\": 0}}, {\"id\": \"c3_v6_random_s025\", \"claim\": \"C3\", \"description\": \"Random: II low_median=2.91 ~ high_median=3.00; flat phase gradient (bootstrap_p=0.559)\", \"registry_id\": \"v6_random_s025\", \"role\": \"primary\", \"priority\": \"high\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"ii_high_median\": 3.0024, \"ii_mid_median\": 2.9846, \"ii_low_median\": 2.9146, \"ii_high_mean\": 3.9052, \"ii_mid_mean\": 7.9491, \"ii_low_mean\": 3.9114, \"per_problem_ii_count\": 50, \"n_high\": 36, \"n_mid\": 25, \"n_low\": 24, \"bootstrap_gradient_paired\": -0.1199, \"bootstrap_ci_paired\": [-1.517, 1.2461], \"bootstrap_p\": 0.559, \"bootstrap_gradient_unpaired\": -0.8616, \"bootstrap_ci_unpaired\": [-3.3911, 1.5169], \"per_problem_ii_stats\": {\"high\": {\"min\": -6.1388, \"max\": 25.2471, \"mean\": 4.4098, \"median\": 3.0421, \"std\": 6.0734}, \"mid\": {\"min\": 0.158, \"max\": 108.7242, \"mean\": 7.5626, \"median\": 2.1407, \"std\": 20.926}, \"low\": {\"min\": -0.1953, \"max\": 12.8555, \"mean\": 3.5806, \"median\": 2.7289, \"std\": 3.4915}}, \"verdict\": \"FAIL\"}}, {\"id\": \"c3_bf16_importance_s020\", \"claim\": \"C3\", \"description\": \"Importance: II low=1.50, mid=0.20, high=0.015 (median); clear phase separation\", \"registry_id\": \"bf16_importance_s020\", \"role\": \"supporting\", \"priority\": \"medium\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"interaction_index\": {\"high\": {\"mean\": 0.1289, \"median\": 0.0145, \"ci\": [-0.1975, 0.6647], \"winsorized_mean\": -0.0297, \"skewness\": 16.67}, \"mid\": {\"mean\": 1.2604, \"median\": 0.2027, \"ci\": [0.7466, 1.8962], \"winsorized_mean\": 0.766, \"skewness\": 7.05}, \"low\": {\"mean\": 6.0288, \"median\": 1.4963, \"ci\": [4.4671, 7.9237], \"winsorized_mean\": 4.3426, \"skewness\": 6.01}}, \"per_problem_ii_stats\": {\"high\": {\"n\": 49, \"min\": -0.1884, \"max\": 0.4196, \"mean\": 0.0025, \"median\": 0.0036, \"std\": 0.0966}, \"mid\": {\"n\": 40, \"min\": -0.0519, \"max\": 8.6969, \"mean\": 0.6795, \"median\": 0.1977, \"std\": 1.4998}, \"low\": {\"n\": 50, \"min\": -1.6151, \"max\": 22.6875, \"mean\": 2.2301, \"median\": 1.128, \"std\": 4.3758}}, \"gradient_paired_aggregate_legacy\": 5.9, \"median_difference\": 1.4818, \"n_problems\": 50, \"pass_fail\": {\"ci_overlap\": true, \"sign_reversal\": false, \"overall\": \"PASS\"}, \"phase_stats\": {\"high\": {\"n_tokens\": 21086, \"n_segments\": 387}, \"mid\": {\"n_tokens\": 13306, \"n_segments\": 191}, \"low\": {\"n_tokens\": 27748, \"n_segments\": 397}}, \"perplexity\": {\"high\": {\"dense\": 1.1689, \"attn\": 1.5233, \"kv\": 1.6191, \"both\": 2.1047}, \"mid\": {\"dense\": 1.2269, \"attn\": 1.5375, \"kv\": 3.5164, \"both\": 5.4246}, \"low\": {\"dense\": 1.2286, \"attn\": 1.6486, \"kv\": 15.7987, \"both\": 23.74}}}}, {\"id\": \"c3_bf16_ds_rand_s020\", \"claim\": \"C3\", \"description\": \"Random: II high=0.292, mid=0.350, low=0.276 (median); no phase separation\", \"registry_id\": \"bf16_ds_rand_s020\", \"role\": \"supporting\", \"priority\": \"medium\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"interaction_index\": {\"high\": {\"mean\": 1.1216, \"median\": 0.2918, \"ci\": [0.0796, 2.5834], \"median_ci\": [0.1598, 0.4581], \"winsorized_mean\": 1.7664, \"skewness\": 9.59}, \"mid\": {\"mean\": -1.5827, \"median\": 0.3504, \"ci\": [-6.0963, 1.5735], \"median_ci\": [0.1993, 0.5226], \"winsorized_mean\": 0.5839, \"skewness\": -12.31}, \"low\": {\"mean\": -0.4116, \"median\": 0.2763, \"ci\": [-2.6034, 1.209], \"median_ci\": [0.2194, 0.5487], \"winsorized_mean\": 0.9942, \"skewness\": -10.07}}, \"perplexity\": {\"high\": {\"dense\": 1.1687, \"attn\": 3.1905, \"kv\": 3.8002, \"both\": 8.8129}, \"mid\": {\"dense\": 1.2269, \"attn\": 67.8504, \"kv\": 3.788, \"both\": 11.4974}, \"low\": {\"dense\": 1.2284, \"attn\": 8.592, \"kv\": 5.0078, \"both\": 9.2001}}, \"phase_stats\": {\"high\": {\"n_tokens\": 21086, \"n_segments\": 387}, \"mid\": {\"n_tokens\": 13306, \"n_segments\": 191}, \"low\": {\"n_tokens\": 27748, \"n_segments\": 397}}, \"n_problems\": 50, \"pass_fail\": {\"ci_overlap\": false, \"sign_reversal\": false, \"overall\": \"FAIL\"}, \"median_difference\": -0.0155}}, {\"id\": \"c4_c4_entropy\", \"claim\": \"C4\", \"description\": \"DS importance entropy_delta: -0.04 to -0.05 (collapse); random: +0.13 to +0.23 (redistribution). Gini_delta: -0.03 to -0.08\", \"registry_id\": \"c4_entropy\", \"role\": \"primary\", \"priority\": \"high\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"importance_entropy_delta\": {\"s015\": -0.0402, \"s020\": -0.0472, \"s025\": -0.0446, \"s030\": -0.0436}, \"random_entropy_delta\": {\"s015\": 0.1283, \"s020\": 0.136, \"s025\": 0.2171, \"s030\": 0.2327}, \"importance_gini_delta\": {\"s015\": -0.0301, \"s020\": -0.0404, \"s025\": -0.0647, \"s030\": -0.0806}, \"random_gini_delta\": {\"s015\": -0.0309, \"s020\": -0.0403, \"s025\": -0.062, \"s030\": -0.0732}, \"importance_cv_delta\": {\"s015\": -0.564, \"s020\": -0.774, \"s025\": -1.287, \"s030\": -1.665}, \"random_cv_delta\": {\"s015\": -1.021, \"s020\": -1.203, \"s025\": -1.923, \"s030\": -2.137}, \"problems_completed\": 30, \"runtime_minutes\": 69.1}}, {\"id\": \"c4_qwen_c4_entropy\", \"claim\": \"C4\", \"description\": \"QW importance entropy_delta mixed: s015=-0.073, s025=+0.045; Gini weaker (-0.01 to -0.02). Model-dependent pattern\", \"registry_id\": \"qwen_c4_entropy\", \"role\": \"primary\", \"priority\": \"high\", \"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"problems_completed\": 30, \"qwen_importance_entropy_delta\": {\"s015\": -0.0733, \"s020\": -0.0759, \"s025\": 0.0451, \"s030\": -0.0072}, \"qwen_random_entropy_delta\": {\"s015\": 0.0838, \"s020\": 0.0901, \"s025\": 0.2168, \"s030\": 0.1968}, \"qwen_importance_gini_delta\": {\"s015\": -0.0103, \"s020\": -0.0121, \"s025\": -0.01, \"s030\": -0.0202}, \"qwen_random_gini_delta\": {\"s015\": -0.0186, \"s020\": -0.0229, \"s025\": -0.0337, \"s030\": -0.0448}, \"qwen_importance_cv_delta\": {\"s015\": -0.045, \"s020\": -0.208, \"s025\": -1.491, \"s030\": -1.142}, \"qwen_random_cv_delta\": {\"s015\": -0.778, \"s020\": -0.889, \"s025\": -1.5, \"s030\": -1.677}, \"cross_model_notes\": \"random entropy increase consistent; importance entropy collapse inconsistent at s025 (reversed to +0.045) and near-zero at s030; gini/cv directions consistent but Qwen magnitudes smaller\"}}, {\"id\": \"c5_bf16_qw_imp_s030\", \"claim\": \"C5\", \"description\": \"Qwen: median_diff=2.619, Cohen's d=1.439, p<1e-5; replicates DeepSeek pattern\", \"registry_id\": \"bf16_qw_imp_s030\", \"role\": \"primary\", \"priority\": \"high\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"median_difference\": 2.619385, \"permutation_p\": 0, \"cohens_d\": 1.4394, \"bootstrap_ci_95\": [1.722281, 3.651063], \"wilcoxon_p\": 0, \"n_bootstrap\": 10000, \"n_paired\": 46}}, {\"id\": \"c5_bf16_importance_s030\", \"claim\": \"C5\", \"description\": \"DeepSeek: II low_median=14.64, high_median=0.053; strong phase gradient\", \"registry_id\": \"bf16_importance_s030\", \"role\": \"primary\", \"priority\": \"high\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"interaction_index\": {\"high\": {\"mean\": 0.5547, \"median\": 0.0534, \"ci\": [0.2773, 0.9198], \"winsorized_mean\": 0.3367, \"skewness\": 10.62}, \"mid\": {\"mean\": 11.3, \"median\": 2.2833, \"ci\": [6.865, 17.2633], \"winsorized_mean\": 8.1752, \"skewness\": 9.19}, \"low\": {\"mean\": 57.7946, \"median\": 14.6395, \"ci\": [41.4416, 77.0467], \"winsorized_mean\": 39.3143, \"skewness\": 8.31}}, \"per_problem_ii_stats\": {\"high\": {\"n\": 49, \"min\": -0.5095, \"max\": 4.4457, \"mean\": 0.1976, \"median\": 0.0343, \"std\": 0.6793}, \"mid\": {\"n\": 40, \"min\": -0.1989, \"max\": 34.0258, \"mean\": 5.2585, \"median\": 1.5173, \"std\": 7.9382}, \"low\": {\"n\": 50, \"min\": -7.3027, \"max\": 126.7985, \"mean\": 22.6601, \"median\": 9.9731, \"std\": 28.4096}}, \"gradient_paired_aggregate_legacy\": 57.24, \"median_difference\": 14.5861, \"n_problems\": 50, \"pass_fail\": {\"ci_overlap\": true, \"sign_reversal\": false, \"overall\": \"PASS\"}, \"phase_stats\": {\"high\": {\"n_tokens\": 21086, \"n_segments\": 387}, \"mid\": {\"n_tokens\": 13306, \"n_segments\": 191}, \"low\": {\"n_tokens\": 27748, \"n_segments\": 397}}, \"perplexity\": {\"high\": {\"dense\": 1.1689, \"attn\": 1.7123, \"kv\": 2.0544, \"both\": 3.2372}, \"mid\": {\"dense\": 1.2269, \"attn\": 1.7894, \"kv\": 9.4821, \"both\": 24.2847}, \"low\": {\"dense\": 1.2286, \"attn\": 1.9347, \"kv\": 51.6485, \"both\": 122.61}}}}, {\"id\": \"c5_c2_n500_deepseek\", \"claim\": \"C5\", \"description\": \"DS n=500: imp_s030 median_II=8.48, CI=[7.46,9.56], p=1.3e-78; robust at scale\", \"registry_id\": \"c2_n500_deepseek\", \"role\": \"supporting\", \"priority\": \"medium\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"n_problems\": 500, \"effective_n\": 496, \"mid_null_rate\": 0.102, \"imp_s015_median_ii\": 0.3907, \"imp_s015_ci\": [0.3496, 0.4431], \"imp_s015_wilcoxon_p\": 1.27e-70, \"imp_s020_median_ii\": 1.2149, \"imp_s020_ci\": [1.1072, 1.3365], \"imp_s020_wilcoxon_p\": 3.98e-75, \"imp_s025_median_ii\": 3.9857, \"imp_s025_ci\": [3.5272, 4.3588], \"imp_s025_wilcoxon_p\": 1.99e-78, \"imp_s030_median_ii\": 8.4813, \"imp_s030_ci\": [7.7543, 9.6919], \"imp_s030_wilcoxon_p\": 1.09e-79, \"rand_s015_median_ii\": 0.0139, \"rand_s015_wilcoxon_p\": 0.863, \"rand_s020_median_ii\": 0.0315, \"rand_s020_wilcoxon_p\": 0.28, \"rand_s025_median_ii\": 0.2574, \"rand_s025_bonf_p\": 0.005839, \"rand_s025_fdr_p\": 0.001914, \"rand_s030_median_ii\": 0.5096, \"rand_s030_bonf_p\": 0.005903, \"rand_s030_fdr_p\": 0.001914, \"dz_s015_s020\": -0.925, \"dz_s020_s025\": -0.824, \"dz_s025_s030\": -0.773, \"dz_s015_s030\": -0.944, \"all_dz_reliable\": true, \"dose_response_monotonic\": true, \"dose_response_spearman_rho\": 1, \"dose_response_perm_p\": 0.0417, \"imp_rand_ratio_range\": \"15.5-38.6x\", \"bonferroni_k\": 4, \"bonferroni_note\": \"Bonferroni k=4 family-wise (D066 revision)\"}}, {\"id\": \"c5_c2_qw_n500_r3\", \"claim\": \"C5\", \"description\": \"QW n=500: imp_s030 median_II=4.33, p<1e-40; cross-model replication at high power\", \"registry_id\": \"c2_qw_n500_r3\", \"role\": \"supporting\", \"priority\": \"medium\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"n_problems\": 500, \"effective_n\": 475, \"filter\": \"low+high valid only (mid-null allowed)\", \"mid_null_rate\": 0.452, \"imp_s015_median_ii\": 0.0659, \"imp_s015_ci\": [0.0492, 0.0925], \"imp_s015_wilcoxon_p\": 8.66e-15, \"imp_s015_bonf_p\": 3.46e-14, \"imp_s020_median_ii\": 0.3073, \"imp_s020_ci\": [0.2612, 0.3564], \"imp_s020_wilcoxon_p\": 6.84e-42, \"imp_s020_bonf_p\": 2.74e-41, \"imp_s025_median_ii\": 1.0745, \"imp_s025_ci\": [0.9766, 1.1787], \"imp_s025_wilcoxon_p\": 1.06e-68, \"imp_s025_bonf_p\": 4.25e-68, \"imp_s030_median_ii\": 3.155, \"imp_s030_ci\": [2.7834, 3.5582], \"imp_s030_wilcoxon_p\": 9.21e-74, \"imp_s030_bonf_p\": 3.69e-73, \"rand_s015_median_ii\": -0.0111, \"rand_s015_wilcoxon_p\": 0.172, \"rand_s015_bonf_p\": 0.687, \"rand_s020_median_ii\": 0.0153, \"rand_s020_wilcoxon_p\": 0.2, \"rand_s020_bonf_p\": 0.8, \"rand_s025_median_ii\": 0.3931, \"rand_s025_wilcoxon_p\": 1.59e-11, \"rand_s025_bonf_p\": 6.37e-11, \"rand_s025_fdr_p\": 2.63e-11, \"rand_s030_median_ii\": 0.9127, \"rand_s030_wilcoxon_p\": 2.92e-15, \"rand_s030_bonf_p\": 1.17e-14, \"rand_s030_fdr_p\": 5.61e-15, \"dz_s015_s020\": -0.629, \"dz_s020_s025\": -0.865, \"dz_s025_s030\": -0.767, \"dz_s015_s030\": -0.923, \"all_dz_reliable\": true, \"dose_response_monotonic\": true, \"dose_response_spearman_rho\": 1, \"dose_response_perm_p\": 0.0417, \"imp_rand_ratio_range\": \"2.7-20.1x\", \"bonferroni_k\": 4, \"bonferroni_note\": \"Bonferroni k=4 family-wise (D066 revision)\"}}, {\"id\": \"c5b_c5b_pilot\", \"claim\": \"C5b\", \"description\": \"Oracle recovery=18% (gate: >30% FAIL); heuristic recovery=31.7% but CI crosses zero. s030 incomplete\", \"registry_id\": \"c5b_pilot\", \"role\": \"primary\", \"priority\": \"high\", \"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"s025_uniform_median_ii\": 1.0435, \"s025_oracle_median_ii\": 0.856, \"s025_oracle_recovery_pct\": 18, \"s025_oracle_recovery_ci\": [-39, 45.8], \"s025_oracle_wilcoxon_p\": 0.0021, \"s025_heuristic_median_ii\": 0.7127, \"s025_heuristic_recovery_pct\": 31.7, \"s025_heuristic_recovery_ci\": [-22.8, 66], \"s025_heuristic_wilcoxon_p\": 0.0236, \"gate_criterion\": \"oracle_recovery > 30%\", \"gate_result\": \"FAIL\", \"s030_status\": \"not_completed\", \"n_problems\": 30}}, {\"id\": \"c6_bf16_importance_s015\", \"claim\": \"C6\", \"description\": \"II low_median=0.398 at s=0.15\", \"registry_id\": \"bf16_importance_s015\", \"role\": \"primary\", \"priority\": \"high\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"interaction_index\": {\"high\": {\"mean\": -0.150213, \"median\": 0.005752, \"ci\": [-0.294614, -0.055385], \"winsorized_mean\": -0.062378, \"skewness\": -14.9912}, \"mid\": {\"mean\": 0.447301, \"median\": 0.080738, \"ci\": [0.267993, 0.668749], \"winsorized_mean\": 0.324751, \"skewness\": 4.7221}, \"low\": {\"mean\": 2.405837, \"median\": 0.398291, \"ci\": [1.478784, 3.667675], \"winsorized_mean\": 1.278857, \"skewness\": 9.5402}}, \"per_problem_ii_stats\": {\"high\": {\"n\": 49, \"min\": -0.188061, \"max\": 0.335853, \"mean\": -0.013405, \"median\": 0.00012, \"std\": 0.078483}, \"mid\": {\"n\": 40, \"min\": -0.169092, \"max\": 3.88198, \"mean\": 0.308621, \"median\": 0.107114, \"std\": 0.690186}, \"low\": {\"n\": 50, \"min\": -0.872983, \"max\": 9.10289, \"mean\": 0.725504, \"median\": 0.315517, \"std\": 1.731056}}, \"gradient_paired_aggregate_legacy\": 69.24, \"median_difference\": 0.3925, \"n_problems\": 50, \"pass_fail\": {\"ci_overlap\": true, \"sign_reversal\": true, \"overall\": \"PASS\"}, \"phase_stats\": {\"high\": {\"n_tokens\": 21086, \"n_segments\": 387}, \"mid\": {\"n_tokens\": 13306, \"n_segments\": 191}, \"low\": {\"n_tokens\": 27748, \"n_segments\": 397}}, \"perplexity\": {\"high\": {\"dense\": 1.1689, \"attn\": 1.4861, \"kv\": 1.4481, \"both\": 1.5911}, \"mid\": {\"dense\": 1.2269, \"attn\": 1.5137, \"kv\": 2.5971, \"both\": 3.4541}, \"low\": {\"dense\": 1.2286, \"attn\": 1.6147, \"kv\": 8.9201, \"both\": 12.5084}}}}, {\"id\": \"c6_bf16_importance_s020\", \"claim\": \"C6\", \"description\": \"II low_median=1.496 at s=0.20\", \"registry_id\": \"bf16_importance_s020\", \"role\": \"supporting\", \"priority\": \"medium\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"interaction_index\": {\"high\": {\"mean\": 0.1289, \"median\": 0.0145, \"ci\": [-0.1975, 0.6647], \"winsorized_mean\": -0.0297, \"skewness\": 16.67}, \"mid\": {\"mean\": 1.2604, \"median\": 0.2027, \"ci\": [0.7466, 1.8962], \"winsorized_mean\": 0.766, \"skewness\": 7.05}, \"low\": {\"mean\": 6.0288, \"median\": 1.4963, \"ci\": [4.4671, 7.9237], \"winsorized_mean\": 4.3426, \"skewness\": 6.01}}, \"per_problem_ii_stats\": {\"high\": {\"n\": 49, \"min\": -0.1884, \"max\": 0.4196, \"mean\": 0.0025, \"median\": 0.0036, \"std\": 0.0966}, \"mid\": {\"n\": 40, \"min\": -0.0519, \"max\": 8.6969, \"mean\": 0.6795, \"median\": 0.1977, \"std\": 1.4998}, \"low\": {\"n\": 50, \"min\": -1.6151, \"max\": 22.6875, \"mean\": 2.2301, \"median\": 1.128, \"std\": 4.3758}}, \"gradient_paired_aggregate_legacy\": 5.9, \"median_difference\": 1.4818, \"n_problems\": 50, \"pass_fail\": {\"ci_overlap\": true, \"sign_reversal\": false, \"overall\": \"PASS\"}, \"phase_stats\": {\"high\": {\"n_tokens\": 21086, \"n_segments\": 387}, \"mid\": {\"n_tokens\": 13306, \"n_segments\": 191}, \"low\": {\"n_tokens\": 27748, \"n_segments\": 397}}, \"perplexity\": {\"high\": {\"dense\": 1.1689, \"attn\": 1.5233, \"kv\": 1.6191, \"both\": 2.1047}, \"mid\": {\"dense\": 1.2269, \"attn\": 1.5375, \"kv\": 3.5164, \"both\": 5.4246}, \"low\": {\"dense\": 1.2286, \"attn\": 1.6486, \"kv\": 15.7987, \"both\": 23.74}}}}, {\"id\": \"c6_bf16_importance_s025\", \"claim\": \"C6\", \"description\": \"II low_median=7.196 at s=0.25\", \"registry_id\": \"bf16_importance_s025\", \"role\": \"supporting\", \"priority\": \"medium\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"interaction_index\": {\"high\": {\"mean\": 0.302756, \"median\": 0.032363, \"ci\": [0.083714, 0.543977], \"winsorized_mean\": 0.200962, \"skewness\": 4.8826}, \"mid\": {\"mean\": 5.729665, \"median\": 1.118069, \"ci\": [3.455574, 8.471799], \"winsorized_mean\": 4.189902, \"skewness\": 8.2799}, \"low\": {\"mean\": 25.852951, \"median\": 7.195958, \"ci\": [19.077082, 33.497293], \"winsorized_mean\": 19.319103, \"skewness\": 7.3986}}, \"per_problem_ii_stats\": {\"high\": {\"n\": 49, \"min\": -0.316321, \"max\": 4.003714, \"mean\": 0.133714, \"median\": 0.009873, \"std\": 0.595358}, \"mid\": {\"n\": 40, \"min\": -0.024794, \"max\": 18.720486, \"mean\": 2.537744, \"median\": 1.05707, \"std\": 3.962575}, \"low\": {\"n\": 50, \"min\": -1.854733, \"max\": 75.467653, \"mean\": 11.28281, \"median\": 3.954593, \"std\": 16.620011}}, \"gradient_paired_aggregate_legacy\": 222.35, \"median_difference\": 7.1636, \"n_problems\": 50, \"pass_fail\": {\"ci_overlap\": true, \"sign_reversal\": false, \"overall\": \"PASS\"}, \"phase_stats\": {\"high\": {\"n_tokens\": 21086, \"n_segments\": 387}, \"mid\": {\"n_tokens\": 13306, \"n_segments\": 191}, \"low\": {\"n_tokens\": 27748, \"n_segments\": 397}}, \"perplexity\": {\"high\": {\"dense\": 1.1689, \"attn\": 1.6511, \"kv\": 1.8628, \"both\": 2.7026}, \"mid\": {\"dense\": 1.2269, \"attn\": 1.7039, \"kv\": 5.6205, \"both\": 13.3436}, \"low\": {\"dense\": 1.2286, \"attn\": 1.8366, \"kv\": 31.756, \"both\": 63.668}}}}, {\"id\": \"c6_bf16_importance_s030\", \"claim\": \"C6\", \"description\": \"II low_median=14.64 at s=0.30; growth 0.40->1.50->7.20->14.64 is sub-exponential\", \"registry_id\": \"bf16_importance_s030\", \"role\": \"supporting\", \"priority\": \"medium\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"interaction_index\": {\"high\": {\"mean\": 0.5547, \"median\": 0.0534, \"ci\": [0.2773, 0.9198], \"winsorized_mean\": 0.3367, \"skewness\": 10.62}, \"mid\": {\"mean\": 11.3, \"median\": 2.2833, \"ci\": [6.865, 17.2633], \"winsorized_mean\": 8.1752, \"skewness\": 9.19}, \"low\": {\"mean\": 57.7946, \"median\": 14.6395, \"ci\": [41.4416, 77.0467], \"winsorized_mean\": 39.3143, \"skewness\": 8.31}}, \"per_problem_ii_stats\": {\"high\": {\"n\": 49, \"min\": -0.5095, \"max\": 4.4457, \"mean\": 0.1976, \"median\": 0.0343, \"std\": 0.6793}, \"mid\": {\"n\": 40, \"min\": -0.1989, \"max\": 34.0258, \"mean\": 5.2585, \"median\": 1.5173, \"std\": 7.9382}, \"low\": {\"n\": 50, \"min\": -7.3027, \"max\": 126.7985, \"mean\": 22.6601, \"median\": 9.9731, \"std\": 28.4096}}, \"gradient_paired_aggregate_legacy\": 57.24, \"median_difference\": 14.5861, \"n_problems\": 50, \"pass_fail\": {\"ci_overlap\": true, \"sign_reversal\": false, \"overall\": \"PASS\"}, \"phase_stats\": {\"high\": {\"n_tokens\": 21086, \"n_segments\": 387}, \"mid\": {\"n_tokens\": 13306, \"n_segments\": 191}, \"low\": {\"n_tokens\": 27748, \"n_segments\": 397}}, \"perplexity\": {\"high\": {\"dense\": 1.1689, \"attn\": 1.7123, \"kv\": 2.0544, \"both\": 3.2372}, \"mid\": {\"dense\": 1.2269, \"attn\": 1.7894, \"kv\": 9.4821, \"both\": 24.2847}, \"low\": {\"dense\": 1.2286, \"attn\": 1.9347, \"kv\": 51.6485, \"both\": 122.61}}}}, {\"id\": \"c7_c2_n500_deepseek\", \"claim\": \"C7\", \"description\": \"DS n=500: all 4 sparsities significant (p<1e-70); CIs non-overlapping across dose levels\", \"registry_id\": \"c2_n500_deepseek\", \"role\": \"primary\", \"priority\": \"high\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"n_problems\": 500, \"effective_n\": 496, \"mid_null_rate\": 0.102, \"imp_s015_median_ii\": 0.3907, \"imp_s015_ci\": [0.3496, 0.4431], \"imp_s015_wilcoxon_p\": 1.27e-70, \"imp_s020_median_ii\": 1.2149, \"imp_s020_ci\": [1.1072, 1.3365], \"imp_s020_wilcoxon_p\": 3.98e-75, \"imp_s025_median_ii\": 3.9857, \"imp_s025_ci\": [3.5272, 4.3588], \"imp_s025_wilcoxon_p\": 1.99e-78, \"imp_s030_median_ii\": 8.4813, \"imp_s030_ci\": [7.7543, 9.6919], \"imp_s030_wilcoxon_p\": 1.09e-79, \"rand_s015_median_ii\": 0.0139, \"rand_s015_wilcoxon_p\": 0.863, \"rand_s020_median_ii\": 0.0315, \"rand_s020_wilcoxon_p\": 0.28, \"rand_s025_median_ii\": 0.2574, \"rand_s025_bonf_p\": 0.005839, \"rand_s025_fdr_p\": 0.001914, \"rand_s030_median_ii\": 0.5096, \"rand_s030_bonf_p\": 0.005903, \"rand_s030_fdr_p\": 0.001914, \"dz_s015_s020\": -0.925, \"dz_s020_s025\": -0.824, \"dz_s025_s030\": -0.773, \"dz_s015_s030\": -0.944, \"all_dz_reliable\": true, \"dose_response_monotonic\": true, \"dose_response_spearman_rho\": 1, \"dose_response_perm_p\": 0.0417, \"imp_rand_ratio_range\": \"15.5-38.6x\", \"bonferroni_k\": 4, \"bonferroni_note\": \"Bonferroni k=4 family-wise (D066 revision)\"}}, {\"id\": \"c7_c2_qw_n500_r3\", \"claim\": \"C7\", \"description\": \"QW n=500: all 4 sparsities significant (p<1e-14 Bonferroni-corrected); mid_null_rate=45.2%\", \"registry_id\": \"c2_qw_n500_r3\", \"role\": \"primary\", \"priority\": \"high\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"n_problems\": 500, \"effective_n\": 475, \"filter\": \"low+high valid only (mid-null allowed)\", \"mid_null_rate\": 0.452, \"imp_s015_median_ii\": 0.0659, \"imp_s015_ci\": [0.0492, 0.0925], \"imp_s015_wilcoxon_p\": 8.66e-15, \"imp_s015_bonf_p\": 3.46e-14, \"imp_s020_median_ii\": 0.3073, \"imp_s020_ci\": [0.2612, 0.3564], \"imp_s020_wilcoxon_p\": 6.84e-42, \"imp_s020_bonf_p\": 2.74e-41, \"imp_s025_median_ii\": 1.0745, \"imp_s025_ci\": [0.9766, 1.1787], \"imp_s025_wilcoxon_p\": 1.06e-68, \"imp_s025_bonf_p\": 4.25e-68, \"imp_s030_median_ii\": 3.155, \"imp_s030_ci\": [2.7834, 3.5582], \"imp_s030_wilcoxon_p\": 9.21e-74, \"imp_s030_bonf_p\": 3.69e-73, \"rand_s015_median_ii\": -0.0111, \"rand_s015_wilcoxon_p\": 0.172, \"rand_s015_bonf_p\": 0.687, \"rand_s020_median_ii\": 0.0153, \"rand_s020_wilcoxon_p\": 0.2, \"rand_s020_bonf_p\": 0.8, \"rand_s025_median_ii\": 0.3931, \"rand_s025_wilcoxon_p\": 1.59e-11, \"rand_s025_bonf_p\": 6.37e-11, \"rand_s025_fdr_p\": 2.63e-11, \"rand_s030_median_ii\": 0.9127, \"rand_s030_wilcoxon_p\": 2.92e-15, \"rand_s030_bonf_p\": 1.17e-14, \"rand_s030_fdr_p\": 5.61e-15, \"dz_s015_s020\": -0.629, \"dz_s020_s025\": -0.865, \"dz_s025_s030\": -0.767, \"dz_s015_s030\": -0.923, \"all_dz_reliable\": true, \"dose_response_monotonic\": true, \"dose_response_spearman_rho\": 1, \"dose_response_perm_p\": 0.0417, \"imp_rand_ratio_range\": \"2.7-20.1x\", \"bonferroni_k\": 4, \"bonferroni_note\": \"Bonferroni k=4 family-wise (D066 revision)\"}}, {\"id\": \"c8_c3_llama\", \"claim\": \"C8\", \"description\": \"LLaMA-8B (LlamaForCausalLM) replicates phase-modulated compound severity from Qwen2ForCausalLM\", \"registry_id\": \"c3_llama\", \"role\": \"primary\", \"priority\": \"high\", \"status\": \"DONE\", \"conclusion\": \"success\"}, {\"id\": \"c10_gsm8k_profiling_ds\", \"claim\": \"C10\", \"description\": \"DS GSM8K importance gradient: s015=0.241, s020=0.740, s025=1.992, s030=4.636 (monotonic)\", \"registry_id\": \"gsm8k_profiling_ds\", \"role\": \"primary\", \"priority\": \"high\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"version\": \"v3_median\", \"n_problems\": 50, \"method\": \"median + Wilcoxon + bootstrap_median(B=10000)\", \"importance\": {\"s015\": {\"median_gradient\": 0.241, \"ci_low\": 0.077, \"ci_high\": 0.478, \"wilcoxon_p\": 0.0003}, \"s020\": {\"median_gradient\": 0.74, \"ci_low\": 0.314, \"ci_high\": 1.119, \"wilcoxon_p\": 0.0001}, \"s025\": {\"median_gradient\": 1.992, \"ci_low\": 0.933, \"ci_high\": 2.82, \"wilcoxon_p\": 0.0001}, \"s030\": {\"median_gradient\": 4.682, \"ci_low\": 2.121, \"ci_high\": 10.557, \"wilcoxon_p\": 0.0001}}, \"imp_rand_ratio\": {\"s015\": 2.3, \"s020\": 2.5, \"s025\": 3.8, \"s030\": 2.8}, \"dose_response_monotonic\": true}}, {\"id\": \"c10_gsm8k_profiling_qw\", \"claim\": \"C10\", \"description\": \"QW GSM8K importance gradient: s015=0.039, s020=0.158, s025=1.100, s030=2.092 (monotonic)\", \"registry_id\": \"gsm8k_profiling_qw\", \"role\": \"primary\", \"priority\": \"high\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"version\": \"v3_median\", \"n_problems\": 50, \"method\": \"median + Wilcoxon + bootstrap_median(B=10000)\", \"importance\": {\"s015\": {\"median_gradient\": 0.039}, \"s020\": {\"median_gradient\": 0.158}, \"s025\": {\"median_gradient\": 1.1}, \"s030\": {\"median_gradient\": 2.092}}, \"qw_rand_s030\": \"INVALID\"}}, {\"id\": \"c10_gsm8k_qw_rand_s025_v2\", \"claim\": \"C10\", \"description\": \"QW random s025 GSM8K: II median_high=0.72, low=1.48; phase gradient weaker than importance\", \"registry_id\": \"gsm8k_qw_rand_s025_v2\", \"role\": \"supporting\", \"priority\": \"medium\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"verdict\": \"PASS\", \"n_problems\": 50, \"n_bootstrap\": 1000, \"seed\": 42, \"high_sparsity\": {\"n_segments\": 216, \"n_tokens\": 9326, \"ppl_dense\": 1.0695, \"ppl_attn\": 5.9362, \"ppl_kv\": 3.4316, \"ppl_both\": 15.7484, \"ii_mean\": 6.5954, \"ii_ci\": [1.1114, 11.3791], \"ii_median\": 0.7176, \"ii_median_ci\": [0.5959, 0.9347], \"winsorized_mean\": 6.5046, \"skewness\": -4.6807, \"outlier_count\": 3}, \"low_sparsity\": {\"n_segments\": 252, \"n_tokens\": 29224, \"ppl_dense\": 1.1972, \"ppl_attn\": 11.5347, \"ppl_kv\": 5.6038, \"ppl_both\": 21.6874, \"ii_mean\": 2.3883, \"ii_ci\": [-8.4602, 11.029], \"ii_median\": 1.4587, \"ii_median_ci\": [1.1121, 2.0451], \"winsorized_mean\": 5.8911, \"skewness\": -7.6074, \"outlier_count\": 4}, \"mid_sparsity\": {\"n_segments\": 51, \"n_tokens\": 5954, \"ppl_dense\": 1.2601, \"ppl_attn\": 13.4132, \"ppl_kv\": 6.4841, \"ppl_both\": 20.8714, \"ii_mean\": 4.5407, \"ii_ci\": [-4.8854, 12.4605], \"ii_median\": 1.1272, \"ii_median_ci\": [0.637, 3.3729], \"winsorized_mean\": 6.3284, \"skewness\": -3.4048, \"outlier_count\": 1}}}, {\"id\": \"c10_gsm8k_qw_rand_s030_v2\", \"claim\": \"C10\", \"description\": \"QW random s030 GSM8K: II median_high=2.31, low=5.87; compound effect on GSM8K confirmed\", \"registry_id\": \"gsm8k_qw_rand_s030_v2\", \"role\": \"supporting\", \"priority\": \"medium\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"verdict\": \"PASS\", \"n_problems\": 50, \"n_bootstrap\": 1000, \"seed\": 42, \"high_sparsity\": {\"n_segments\": 216, \"n_tokens\": 9326, \"null_ratio\": \"2/50\", \"ppl_dense\": 1.0695, \"ppl_attn\": 6.5613, \"ppl_kv\": 4.481, \"ppl_both\": 23.7486, \"ii_mean\": 11.83, \"ii_median\": 2.31, \"ii_ci\": [6.17, 17.04], \"ii_median_ci\": [1.64, 2.81], \"winsorized_mean\": 10.55, \"skewness\": -2.29, \"outlier_count\": 7}, \"low_sparsity\": {\"n_segments\": 252, \"n_tokens\": 29224, \"null_ratio\": \"5/50\", \"ppl_dense\": 1.1972, \"ppl_attn\": 6.3283, \"ppl_kv\": 8.5374, \"ppl_both\": 56.2304, \"ii_mean\": 31.26, \"ii_median\": 5.2, \"ii_ci\": [17.84, 47.86], \"ii_median_ci\": [3.95, 7.24], \"winsorized_mean\": 16.35, \"skewness\": 7.57, \"outlier_count\": 4}, \"mid_sparsity\": {\"n_segments\": 51, \"n_tokens\": 5954, \"null_ratio\": \"17/50\", \"ppl_dense\": 1.2601, \"ppl_attn\": 18.6162, \"ppl_kv\": 11.6625, \"ppl_both\": 47.9019, \"ii_mean\": 18.02, \"ii_median\": 2.7, \"ii_ci\": [0.09, 36.69], \"ii_median_ci\": [1.46, 8.77], \"winsorized_mean\": 18.22, \"skewness\": 0.43, \"outlier_count\": 2}}}, {\"id\": \"s3_c_bf16_ds_imp_s010\", \"claim\": \"S3->C\", \"description\": \"DS s=0.10: II_high_median=0.003, verdict=FAIL; below onset threshold for DeepSeek\", \"registry_id\": \"bf16_ds_imp_s010\", \"role\": \"primary\", \"priority\": \"high\", \"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"verdict\": \"FAIL\", \"problems\": 50, \"II_high_sparsity_median\": 0.0027, \"II_high_sparsity_mean\": -0.1998, \"II_low_sparsity_median\": 0.0151, \"II_low_sparsity_mean\": -0.1066, \"II_mid_sparsity_median\": 0.0061, \"II_mid_sparsity_mean\": -0.0131, \"high_sparsity_tokens\": 21086, \"low_sparsity_tokens\": 27748, \"mid_sparsity_tokens\": 13306}}, {\"id\": \"s3_c_bf16_qw_imp_s010\", \"claim\": \"S3->C\", \"description\": \"QW s=0.10: overall_verdict=PASS, CI_overlap_test=PASS; Qwen onset earlier than DeepSeek\", \"registry_id\": \"bf16_qw_imp_s010\", \"role\": \"primary\", \"priority\": \"high\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"n_problems\": 50, \"overall_verdict\": \"PASS\", \"ci_overlap_test\": \"PASS\", \"sign_reversal_test\": \"FAIL\", \"high_sparsity_II_median\": 0.0001, \"high_sparsity_II_median_CI\": [-0.0028, 0.0005], \"high_sparsity_II_mean\": -0.0887, \"high_sparsity_II_mean_CI\": [-0.1235, -0.0591], \"low_sparsity_II_median\": -0.0444, \"low_sparsity_II_median_CI\": [-0.0967, -0.0152], \"low_sparsity_II_mean\": -0.2431, \"low_sparsity_II_mean_CI\": [-0.3817, -0.1202], \"mid_sparsity_II_median\": -0.0359, \"mid_sparsity_II_median_CI\": [-0.0963, -0.015], \"mid_sparsity_II_mean\": -0.084, \"mid_sparsity_II_mean_CI\": [-0.1366, -0.035], \"ppl_high_dense\": 1.074, \"ppl_high_both\": 1.228, \"ppl_low_dense\": 1.152, \"ppl_low_both\": 3.204, \"ppl_mid_dense\": 1.133, \"ppl_mid_both\": 1.741}}, {\"id\": \"s3_c_bf16_qw_imp_s015\", \"claim\": \"S3->C\", \"description\": \"QW s=0.15: median_diff=0.048, permutation_p=0.0001; confirmed above threshold\", \"registry_id\": \"bf16_qw_imp_s015\", \"role\": \"supporting\", \"priority\": \"medium\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"median_difference\": 0.047619, \"permutation_p\": 0.0001, \"cohens_d\": 0.3705, \"bootstrap_ci_95\": [-0.005077, 0.109517], \"wilcoxon_p\": 0.02958, \"n_bootstrap\": 10000, \"n_paired\": 46}}, {\"id\": \"s7_c_c2_n500_deepseek\", \"claim\": \"S7->C\", \"description\": \"DS n=500 monotonic: imp median II 0.39->1.21->3.99->8.48 across s015-s030 (Spearman rho=1.0)\", \"registry_id\": \"c2_n500_deepseek\", \"role\": \"primary\", \"priority\": \"high\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"n_problems\": 500, \"effective_n\": 496, \"mid_null_rate\": 0.102, \"imp_s015_median_ii\": 0.3907, \"imp_s015_ci\": [0.3496, 0.4431], \"imp_s015_wilcoxon_p\": 1.27e-70, \"imp_s020_median_ii\": 1.2149, \"imp_s020_ci\": [1.1072, 1.3365], \"imp_s020_wilcoxon_p\": 3.98e-75, \"imp_s025_median_ii\": 3.9857, \"imp_s025_ci\": [3.5272, 4.3588], \"imp_s025_wilcoxon_p\": 1.99e-78, \"imp_s030_median_ii\": 8.4813, \"imp_s030_ci\": [7.7543, 9.6919], \"imp_s030_wilcoxon_p\": 1.09e-79, \"rand_s015_median_ii\": 0.0139, \"rand_s015_wilcoxon_p\": 0.863, \"rand_s020_median_ii\": 0.0315, \"rand_s020_wilcoxon_p\": 0.28, \"rand_s025_median_ii\": 0.2574, \"rand_s025_bonf_p\": 0.005839, \"rand_s025_fdr_p\": 0.001914, \"rand_s030_median_ii\": 0.5096, \"rand_s030_bonf_p\": 0.005903, \"rand_s030_fdr_p\": 0.001914, \"dz_s015_s020\": -0.925, \"dz_s020_s025\": -0.824, \"dz_s025_s030\": -0.773, \"dz_s015_s030\": -0.944, \"all_dz_reliable\": true, \"dose_response_monotonic\": true, \"dose_response_spearman_rho\": 1, \"dose_response_perm_p\": 0.0417, \"imp_rand_ratio_range\": \"15.5-38.6x\", \"bonferroni_k\": 4, \"bonferroni_note\": \"Bonferroni k=4 family-wise (D066 revision)\"}}, {\"id\": \"s7_c_c2_qw_n500_r3\", \"claim\": \"S7->C\", \"description\": \"QW n=500 monotonic: imp median II 0.066->0.307->1.075->4.33 across s015-s030 (Spearman rho=1.0)\", \"registry_id\": \"c2_qw_n500_r3\", \"role\": \"primary\", \"priority\": \"high\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"n_problems\": 500, \"effective_n\": 475, \"filter\": \"low+high valid only (mid-null allowed)\", \"mid_null_rate\": 0.452, \"imp_s015_median_ii\": 0.0659, \"imp_s015_ci\": [0.0492, 0.0925], \"imp_s015_wilcoxon_p\": 8.66e-15, \"imp_s015_bonf_p\": 3.46e-14, \"imp_s020_median_ii\": 0.3073, \"imp_s020_ci\": [0.2612, 0.3564], \"imp_s020_wilcoxon_p\": 6.84e-42, \"imp_s020_bonf_p\": 2.74e-41, \"imp_s025_median_ii\": 1.0745, \"imp_s025_ci\": [0.9766, 1.1787], \"imp_s025_wilcoxon_p\": 1.06e-68, \"imp_s025_bonf_p\": 4.25e-68, \"imp_s030_median_ii\": 3.155, \"imp_s030_ci\": [2.7834, 3.5582], \"imp_s030_wilcoxon_p\": 9.21e-74, \"imp_s030_bonf_p\": 3.69e-73, \"rand_s015_median_ii\": -0.0111, \"rand_s015_wilcoxon_p\": 0.172, \"rand_s015_bonf_p\": 0.687, \"rand_s020_median_ii\": 0.0153, \"rand_s020_wilcoxon_p\": 0.2, \"rand_s020_bonf_p\": 0.8, \"rand_s025_median_ii\": 0.3931, \"rand_s025_wilcoxon_p\": 1.59e-11, \"rand_s025_bonf_p\": 6.37e-11, \"rand_s025_fdr_p\": 2.63e-11, \"rand_s030_median_ii\": 0.9127, \"rand_s030_wilcoxon_p\": 2.92e-15, \"rand_s030_bonf_p\": 1.17e-14, \"rand_s030_fdr_p\": 5.61e-15, \"dz_s015_s020\": -0.629, \"dz_s020_s025\": -0.865, \"dz_s025_s030\": -0.767, \"dz_s015_s030\": -0.923, \"all_dz_reliable\": true, \"dose_response_monotonic\": true, \"dose_response_spearman_rho\": 1, \"dose_response_perm_p\": 0.0417, \"imp_rand_ratio_range\": \"2.7-20.1x\", \"bonferroni_k\": 4, \"bonferroni_note\": \"Bonferroni k=4 family-wise (D066 revision)\"}}, {\"id\": \"s7_c_bf16_qw_imp_s035\", \"claim\": \"S7->C\", \"description\": \"QW s=0.35: low_II_median=8.24; extends dose-response beyond s030\", \"registry_id\": \"bf16_qw_imp_s035\", \"role\": \"supporting\", \"priority\": \"medium\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"n_problems\": 50, \"overall_verdict\": \"PASS\", \"ci_overlap_test\": \"PASS\", \"sign_reversal_test\": \"FAIL\", \"high_sparsity_II_median\": 0.0232, \"high_sparsity_II_median_CI\": [0.0154, 0.0383], \"high_sparsity_II_mean\": 0.1643, \"high_sparsity_II_mean_CI\": [0.0844, 0.2495], \"low_sparsity_II_median\": 8.2358, \"low_sparsity_II_median_CI\": [6.1564, 10.9231], \"low_sparsity_II_mean\": 18.9673, \"low_sparsity_II_mean_CI\": [14.5015, 23.9752], \"mid_sparsity_II_median\": 0.9577, \"mid_sparsity_II_median_CI\": [0.171, 3.5575], \"mid_sparsity_II_mean\": 8.0734, \"mid_sparsity_II_mean_CI\": [2.0224, 16.8946], \"ppl_high_dense\": 1.0738, \"ppl_high_both\": 2.3435, \"ppl_low_dense\": 1.1518, \"ppl_low_both\": 58.0358, \"ppl_mid_dense\": 1.1327, \"ppl_mid_both\": 20.9912, \"high_sparsity_tokens\": 16289, \"low_sparsity_tokens\": 32227, \"mid_sparsity_tokens\": 4372}}], \"total\": 38}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1c869f6a-2638-4ba9-832e-ecdb9d44f06d",
  "isSidechain": false,
  "promptId": "d6a043a1-3c08-4fe7-9e57-50e76a38ea26",
  "type": "user",
  "uuid": "634a406a-9c64-415a-b06a-b890b55966ef",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": [{\\\"id\\\": \\\"c1_bf16_importance_s025\\\", \\\"claim\\\": \\\"C1\\\", \\\"description\\\": \\\"II median: high=0.032, mid=1.118, low=7.196; importance masking shows strong phase gradient\\\", \\\"registry_id\\\": \\\"bf16_importance_s025\\\", \\\"role\\\": \\\"primary\\\", \\\"priority\\\": \\\"high\\\", \\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"interaction_index\\\": {\\\"high\\\": {\\\"mean\\\": 0.302756, \\\"median\\\": 0.032363, \\\"ci\\\": [0.083714, 0.543977], \\\"winsorized_mean\\\": 0.200962, \\\"skewness\\\": 4.8826}, \\\"mid\\\": {\\\"mean\\\": 5.729665, \\\"median\\\": 1.118069, \\\"ci\\\": [3.455574, 8.471799], \\\"winsorized_mean\\\": 4.189902, \\\"skewness\\\": 8.2799}, \\\"low\\\": {\\\"mean\\\": 25.852951, \\\"median\\\": 7.195958, \\\"ci\\\": [19.077082, 33.497293], \\\"winsorized_mean\\\": 19.319103, \\\"skewness\\\": 7.3986}}, \\\"per_problem_ii_stats\\\": {\\\"high\\\": {\\\"n\\\": 49, \\\"min\\\": -0.316321, \\\"max\\\": 4.003714, \\\"mean\\\": 0.133714, \\\"median\\\": 0.009873, \\\"std\\\": 0.595358}, \\\"mid\\\": {\\\"n\\\": 40, \\\"min\\\": -0.024794, \\\"max\\\": 18.720486, \\\"mean\\\": 2.537744, \\\"median\\\": 1.05707, \\\"std\\\": 3.962575}, \\\"low\\\": {\\\"n\\\": 50, \\\"min\\\": -1.854733, \\\"max\\\": 75.467653, \\\"mean\\\": 11.28281, \\\"median\\\": 3.954593, \\\"std\\\": 16.620011}}, \\\"gradient_paired_aggregate_legacy\\\": 222.35, \\\"median_difference\\\": 7.1636, \\\"n_problems\\\": 50, \\\"pass_fail\\\": {\\\"ci_overlap\\\": true, \\\"sign_reversal\\\": false, \\\"overall\\\": \\\"PASS\\\"}, \\\"phase_stats\\\": {\\\"high\\\": {\\\"n_tokens\\\": 21086, \\\"n_segments\\\": 387}, \\\"mid\\\": {\\\"n_tokens\\\": 13306, \\\"n_segments\\\": 191}, \\\"low\\\": {\\\"n_tokens\\\": 27748, \\\"n_segments\\\": 397}}, \\\"perplexity\\\": {\\\"high\\\": {\\\"dense\\\": 1.1689, \\\"attn\\\": 1.6511, \\\"kv\\\": 1.8628, \\\"both\\\": 2.7026}, \\\"mid\\\": {\\\"dense\\\": 1.2269, \\\"attn\\\": 1.7039, \\\"kv\\\": 5.6205, \\\"both\\\": 13.3436}, \\\"low\\\": {\\\"dense\\\": 1.2286, \\\"attn\\\": 1.8366, \\\"kv\\\": 31.756, \\\"both\\\": 63.668}}}}, {\\\"id\\\": \\\"c1_bf16_ds_rand_s025\\\", \\\"claim\\\": \\\"C1\\\", \\\"description\\\": \\\"Random II median: high=0.818, mid=0.932, low=1.363; flat gradient vs importance\\\", \\\"registry_id\\\": \\\"bf16_ds_rand_s025\\\", \\\"role\\\": \\\"primary\\\", \\\"priority\\\": \\\"high\\\", \\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"interaction_index\\\": {\\\"high\\\": {\\\"mean\\\": 3.59, \\\"median\\\": 0.8182, \\\"ci\\\": [1.4021, 6.2327], \\\"median_ci\\\": [0.5075, 1.7217], \\\"winsorized_mean\\\": 6.3965, \\\"skewness\\\": -7.57}, \\\"mid\\\": {\\\"mean\\\": -1.8455, \\\"median\\\": 0.9324, \\\"ci\\\": [-10.3663, 4.9342], \\\"median_ci\\\": [0.7331, 1.7003], \\\"winsorized_mean\\\": 3.1014, \\\"skewness\\\": -12.76}, \\\"low\\\": {\\\"mean\\\": 0.7212, \\\"median\\\": 1.3627, \\\"ci\\\": [-4.2068, 4.5006], \\\"median_ci\\\": [1.0869, 2.6866], \\\"winsorized_mean\\\": 4.1866, \\\"skewness\\\": -15.85}}, \\\"perplexity\\\": {\\\"high\\\": {\\\"dense\\\": 1.1687, \\\"attn\\\": 7.237, \\\"kv\\\": 4.9751, \\\"both\\\": 17.7423}, \\\"mid\\\": {\\\"dense\\\": 1.2269, \\\"attn\\\": 868.3199, \\\"kv\\\": 5.1165, \\\"both\\\": 29.4661}, \\\"low\\\": {\\\"dense\\\": 1.2284, \\\"attn\\\": 24.3571, \\\"kv\\\": 6.7993, \\\"both\\\": 17.9694}}, \\\"phase_stats\\\": {\\\"high\\\": {\\\"n_tokens\\\": 21086, \\\"n_segments\\\": 387}, \\\"mid\\\": {\\\"n_tokens\\\": 13306, \\\"n_segments\\\": 191}, \\\"low\\\": {\\\"n_tokens\\\": 27748, \\\"n_segments\\\": 397}}, \\\"n_problems\\\": 50, \\\"pass_fail\\\": {\\\"ci_overlap\\\": false, \\\"sign_reversal\\\": false, \\\"overall\\\": \\\"FAIL\\\"}, \\\"median_difference\\\": 0.5445}}, {\\\"id\\\": \\\"c1_bf16_qw_imp_s025\\\", \\\"claim\\\": \\\"C1\\\", \\\"description\\\": \\\"Qwen cross-model: median_diff=1.109, Cohen's d=1.233, p<1e-5\\\", \\\"registry_id\\\": \\\"bf16_qw_imp_s025\\\", \\\"role\\\": \\\"supporting\\\", \\\"priority\\\": \\\"medium\\\", \\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"median_difference\\\": 1.108706, \\\"permutation_p\\\": 0, \\\"cohens_d\\\": 1.2329, \\\"bootstrap_ci_95\\\": [0.609247, 1.469002], \\\"wilcoxon_p\\\": 0, \\\"n_bootstrap\\\": 10000, \\\"n_paired\\\": 46}}, {\\\"id\\\": \\\"c1_sf5_asymmetric_spot\\\", \\\"claim\\\": \\\"C1\\\", \\\"description\\\": \\\"Asymmetric configs: h02_kv03 D=19.13, h03_kv02 D=18.25; gradient consistent\\\", \\\"registry_id\\\": \\\"sf5_asymmetric_spot\\\", \\\"role\\\": \\\"ablation\\\", \\\"priority\\\": \\\"medium\\\", \\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"config_a_h02_kv03\\\": {\\\"II_low\\\": 19.51, \\\"II_mid\\\": 6.05, \\\"II_high\\\": 0.38, \\\"D\\\": 19.13}, \\\"config_b_h03_kv02\\\": {\\\"II_low\\\": 18.77, \\\"II_mid\\\": 3.97, \\\"II_high\\\": 0.52, \\\"D\\\": 18.25}, \\\"pre_registered_criterion_passed\\\": true, \\\"gradient_direction\\\": \\\"II_low >> II_mid >> II_high (consistent with symmetric baseline)\\\"}}, {\\\"id\\\": \\\"c1_c2_accuracy_eval\\\", \\\"claim\\\": \\\"C1\\\", \\\"description\\\": \\\"DS dense->s030 acc: 0.52->0.10 (-0.42); QW dense->s030: 0.32->0.14 (-0.18)\\\", \\\"registry_id\\\": \\\"c2_accuracy_eval\\\", \\\"role\\\": \\\"supporting\\\", \\\"priority\\\": \\\"medium\\\", \\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"n_problems\\\": 50, \\\"ds_dense_acc\\\": 0.52, \\\"ds_s015_acc\\\": 0.36, \\\"ds_s015_delta\\\": -0.16, \\\"ds_s030_acc\\\": 0.1, \\\"ds_s030_delta\\\": -0.42, \\\"qw_dense_acc\\\": 0.32, \\\"qw_s015_acc\\\": 0.34, \\\"qw_s015_delta\\\": 0.02, \\\"qw_s030_acc\\\": 0.14, \\\"qw_s030_delta\\\": -0.18, \\\"ds_s030_chinese_reasoning_rate\\\": 0.4, \\\"ds_dense_truncation_rate\\\": 0.56, \\\"note\\\": \\\"v2 rescored with fixed radical+degree matcher. DS s015 34→36, QW s015 32→34\\\"}}, {\\\"id\\\": \\\"c2_bf16_importance_s030\\\", \\\"claim\\\": \\\"C2\\\", \\\"description\\\": \\\"Phase gradient: II low=14.64 >> mid=2.28 >> high=0.053 (median); low/high ratio ~276x\\\", \\\"registry_id\\\": \\\"bf16_importance_s030\\\", \\\"role\\\": \\\"primary\\\", \\\"priority\\\": \\\"high\\\", \\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"interaction_index\\\": {\\\"high\\\": {\\\"mean\\\": 0.5547, \\\"median\\\": 0.0534, \\\"ci\\\": [0.2773, 0.9198], \\\"winsorized_mean\\\": 0.3367, \\\"skewness\\\": 10.62}, \\\"mid\\\": {\\\"mean\\\": 11.3, \\\"median\\\": 2.2833, \\\"ci\\\": [6.865, 17.2633], \\\"winsorized_mean\\\": 8.1752, \\\"skewness\\\": 9.19}, \\\"low\\\": {\\\"mean\\\": 57.7946, \\\"median\\\": 14.6395, \\\"ci\\\": [41.4416, 77.0467], \\\"winsorized_mean\\\": 39.3143, \\\"skewness\\\": 8.31}}, \\\"per_problem_ii_stats\\\": {\\\"high\\\": {\\\"n\\\": 49, \\\"min\\\": -0.5095, \\\"max\\\": 4.4457, \\\"mean\\\": 0.1976, \\\"median\\\": 0.0343, \\\"std\\\": 0.6793}, \\\"mid\\\": {\\\"n\\\": 40, \\\"min\\\": -0.1989, \\\"max\\\": 34.0258, \\\"mean\\\": 5.2585, \\\"median\\\": 1.5173, \\\"std\\\": 7.9382}, \\\"low\\\": {\\\"n\\\": 50, \\\"min\\\": -7.3027, \\\"max\\\": 126.7985, \\\"mean\\\": 22.6601, \\\"median\\\": 9.9731, \\\"std\\\": 28.4096}}, \\\"gradient_paired_aggregate_legacy\\\": 57.24, \\\"median_difference\\\": 14.5861, \\\"n_problems\\\": 50, \\\"pass_fail\\\": {\\\"ci_overlap\\\": true, \\\"sign_reversal\\\": false, \\\"overall\\\": \\\"PASS\\\"}, \\\"phase_stats\\\": {\\\"high\\\": {\\\"n_tokens\\\": 21086, \\\"n_segments\\\": 387}, \\\"mid\\\": {\\\"n_tokens\\\": 13306, \\\"n_segments\\\": 191}, \\\"low\\\": {\\\"n_tokens\\\": 27748, \\\"n_segments\\\": 397}}, \\\"perplexity\\\": {\\\"high\\\": {\\\"dense\\\": 1.1689, \\\"attn\\\": 1.7123, \\\"kv\\\": 2.0544, \\\"both\\\": 3.2372}, \\\"mid\\\": {\\\"dense\\\": 1.2269, \\\"attn\\\": 1.7894, \\\"kv\\\": 9.4821, \\\"both\\\": 24.2847}, \\\"low\\\": {\\\"dense\\\": 1.2286, \\\"attn\\\": 1.9347, \\\"kv\\\": 51.6485, \\\"both\\\": 122.61}}}}, {\\\"id\\\": \\\"c2_v6_importance_s030\\\", \\\"claim\\\": \\\"C2\\\", \\\"description\\\": \\\"II low_median=34.69, mid_median=7.27, high_median=0.88; bootstrap_gradient=41.92, CI=[19.14,299.76]\\\", \\\"registry_id\\\": \\\"v6_importance_s030\\\", \\\"role\\\": \\\"primary\\\", \\\"priority\\\": \\\"high\\\", \\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"ii_high_median\\\": 0.8833, \\\"ii_mid_median\\\": 7.2706, \\\"ii_low_median\\\": 34.6937, \\\"ii_high_mean\\\": 1.5151, \\\"ii_mid_mean\\\": 78.8215, \\\"ii_low_mean\\\": 1163.9677, \\\"per_problem_ii_count\\\": 50, \\\"n_high\\\": 40, \\\"n_mid\\\": 22, \\\"n_low\\\": 20, \\\"problems\\\": 50, \\\"bootstrap_gradient_paired\\\": 41.92, \\\"bootstrap_ci_paired\\\": [19.14, 299.76], \\\"bootstrap_gradient_unpaired\\\": 39.28, \\\"bootstrap_ci_unpaired\\\": [21.87, 129.59], \\\"bootstrap_p\\\": 0}}, {\\\"id\\\": \\\"c2_think_phase_validation\\\", \\\"claim\\\": \\\"C2\\\", \\\"description\\\": \\\"Phase segmentation kappa=0.887; thinking=57.8% low-sparsity, answer=62.7% high-sparsity\\\", \\\"registry_id\\\": \\\"think_phase_validation\\\", \\\"role\\\": \\\"supporting\\\", \\\"priority\\\": \\\"medium\\\", \\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"effective_n\\\": 48, \\\"skipped_problems\\\": 2, \\\"median_kappa\\\": 0.887, \\\"thinking_in_low_sparsity_phase\\\": 0.578, \\\"answer_in_high_sparsity_phase\\\": 0.627, \\\"note\\\": \\\"Phase segmentation based on dense model — 4 sparsity conditions share identical phase boundaries, effective sample n=48 not n=192\\\"}}, {\\\"id\\\": \\\"c2_acc_qw_s030_n100\\\", \\\"claim\\\": \\\"C2\\\", \\\"description\\\": \\\"QW importance s030 accuracy=0.19 (n=100); dose-response monotonic decline from dense=0.40\\\", \\\"registry_id\\\": \\\"acc_qw_s030_n100\\\", \\\"role\\\": \\\"supporting\\\", \\\"priority\\\": \\\"medium\\\", \\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"batch1_correct\\\": 7, \\\"batch1_total\\\": 50, \\\"batch1_acc\\\": 0.14, \\\"batch1_source\\\": \\\"acc_qw_s030_b1_8k (v2, 8k tokens)\\\", \\\"batch2_correct\\\": 12, \\\"batch2_total\\\": 50, \\\"batch2_acc\\\": 0.24, \\\"combined_correct\\\": 19, \\\"combined_total\\\": 100, \\\"combined_acc\\\": 0.19}}, {\\\"id\\\": \\\"c2_acc_ds_s015_8k_v2\\\", \\\"claim\\\": \\\"C2\\\", \\\"description\\\": \\\"DS s015 accuracy=0.48 vs dense=0.74; early onset of compound degradation\\\", \\\"registry_id\\\": \\\"acc_ds_s015_8k_v2\\\", \\\"role\\\": \\\"supporting\\\", \\\"priority\\\": \\\"medium\\\", \\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"accuracy\\\": 0.48, \\\"correct\\\": 24, \\\"total\\\": 50, \\\"truncation_rate\\\": 0.32, \\\"truncated_count\\\": 16, \\\"non_truncated_accuracy\\\": 0.706, \\\"non_truncated_correct\\\": 24, \\\"non_truncated_total\\\": 34, \\\"wall_time_s\\\": 3967, \\\"max_new_tokens\\\": 8192}}, {\\\"id\\\": \\\"c3_v6_importance_s025\\\", \\\"claim\\\": \\\"C3\\\", \\\"description\\\": \\\"Importance: II low_median=24.16 >> high_median=0.66; strong phase gradient (36x ratio)\\\", \\\"registry_id\\\": \\\"v6_importance_s025\\\", \\\"role\\\": \\\"primary\\\", \\\"priority\\\": \\\"high\\\", \\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"ii_high_median\\\": 0.6641, \\\"ii_mid_median\\\": 5.3067, \\\"ii_low_median\\\": 24.1619, \\\"ii_high_mean\\\": 0.8842, \\\"ii_mid_mean\\\": 10.057, \\\"ii_low_mean\\\": 71.8854, \\\"per_problem_ii_count\\\": 50, \\\"n_high\\\": 42, \\\"n_mid\\\": 23, \\\"n_low\\\": 21, \\\"problems\\\": 50, \\\"bootstrap_gradient_paired\\\": 35.72, \\\"bootstrap_ci_paired\\\": [9.52, 101.54], \\\"bootstrap_gradient_unpaired\\\": 36.38, \\\"bootstrap_ci_unpaired\\\": [13.19, 97.61], \\\"bootstrap_p\\\": 0}}, {\\\"id\\\": \\\"c3_v6_random_s025\\\", \\\"claim\\\": \\\"C3\\\", \\\"description\\\": \\\"Random: II low_median=2.91 ~ high_median=3.00; flat phase gradient (bootstrap_p=0.559)\\\", \\\"registry_id\\\": \\\"v6_random_s025\\\", \\\"role\\\": \\\"primary\\\", \\\"priority\\\": \\\"high\\\", \\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"ii_high_median\\\": 3.0024, \\\"ii_mid_median\\\": 2.9846, \\\"ii_low_median\\\": 2.9146, \\\"ii_high_mean\\\": 3.9052, \\\"ii_mid_mean\\\": 7.9491, \\\"ii_low_mean\\\": 3.9114, \\\"per_problem_ii_count\\\": 50, \\\"n_high\\\": 36, \\\"n_mid\\\": 25, \\\"n_low\\\": 24, \\\"bootstrap_gradient_paired\\\": -0.1199, \\\"bootstrap_ci_paired\\\": [-1.517, 1.2461], \\\"bootstrap_p\\\": 0.559, \\\"bootstrap_gradient_unpaired\\\": -0.8616, \\\"bootstrap_ci_unpaired\\\": [-3.3911, 1.5169], \\\"per_problem_ii_stats\\\": {\\\"high\\\": {\\\"min\\\": -6.1388, \\\"max\\\": 25.2471, \\\"mean\\\": 4.4098, \\\"median\\\": 3.0421, \\\"std\\\": 6.0734}, \\\"mid\\\": {\\\"min\\\": 0.158, \\\"max\\\": 108.7242, \\\"mean\\\": 7.5626, \\\"median\\\": 2.1407, \\\"std\\\": 20.926}, \\\"low\\\": {\\\"min\\\": -0.1953, \\\"max\\\": 12.8555, \\\"mean\\\": 3.5806, \\\"median\\\": 2.7289, \\\"std\\\": 3.4915}}, \\\"verdict\\\": \\\"FAIL\\\"}}, {\\\"id\\\": \\\"c3_bf16_importance_s020\\\", \\\"claim\\\": \\\"C3\\\", \\\"description\\\": \\\"Importance: II low=1.50, mid=0.20, high=0.015 (median); clear phase separation\\\", \\\"registry_id\\\": \\\"bf16_importance_s020\\\", \\\"role\\\": \\\"supporting\\\", \\\"priority\\\": \\\"medium\\\", \\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"interaction_index\\\": {\\\"high\\\": {\\\"mean\\\": 0.1289, \\\"median\\\": 0.0145, \\\"ci\\\": [-0.1975, 0.6647], \\\"winsorized_mean\\\": -0.0297, \\\"skewness\\\": 16.67}, \\\"mid\\\": {\\\"mean\\\": 1.2604, \\\"median\\\": 0.2027, \\\"ci\\\": [0.7466, 1.8962], \\\"winsorized_mean\\\": 0.766, \\\"skewness\\\": 7.05}, \\\"low\\\": {\\\"mean\\\": 6.0288, \\\"median\\\": 1.4963, \\\"ci\\\": [4.4671, 7.9237], \\\"winsorized_mean\\\": 4.3426, \\\"skewness\\\": 6.01}}, \\\"per_problem_ii_stats\\\": {\\\"high\\\": {\\\"n\\\": 49, \\\"min\\\": -0.1884, \\\"max\\\": 0.4196, \\\"mean\\\": 0.0025, \\\"median\\\": 0.0036, \\\"std\\\": 0.0966}, \\\"mid\\\": {\\\"n\\\": 40, \\\"min\\\": -0.0519, \\\"max\\\": 8.6969, \\\"mean\\\": 0.6795, \\\"median\\\": 0.1977, \\\"std\\\": 1.4998}, \\\"low\\\": {\\\"n\\\": 50, \\\"min\\\": -1.6151, \\\"max\\\": 22.6875, \\\"mean\\\": 2.2301, \\\"median\\\": 1.128, \\\"std\\\": 4.3758}}, \\\"gradient_paired_aggregate_legacy\\\": 5.9, \\\"median_difference\\\": 1.4818, \\\"n_problems\\\": 50, \\\"pass_fail\\\": {\\\"ci_overlap\\\": true, \\\"sign_reversal\\\": false, \\\"overall\\\": \\\"PASS\\\"}, \\\"phase_stats\\\": {\\\"high\\\": {\\\"n_tokens\\\": 21086, \\\"n_segments\\\": 387}, \\\"mid\\\": {\\\"n_tokens\\\": 13306, \\\"n_segments\\\": 191}, \\\"low\\\": {\\\"n_tokens\\\": 27748, \\\"n_segments\\\": 397}}, \\\"perplexity\\\": {\\\"high\\\": {\\\"dense\\\": 1.1689, \\\"attn\\\": 1.5233, \\\"kv\\\": 1.6191, \\\"both\\\": 2.1047}, \\\"mid\\\": {\\\"dense\\\": 1.2269, \\\"attn\\\": 1.5375, \\\"kv\\\": 3.5164, \\\"both\\\": 5.4246}, \\\"low\\\": {\\\"dense\\\": 1.2286, \\\"attn\\\": 1.6486, \\\"kv\\\": 15.7987, \\\"both\\\": 23.74}}}}, {\\\"id\\\": \\\"c3_bf16_ds_rand_s020\\\", \\\"claim\\\": \\\"C3\\\", \\\"description\\\": \\\"Random: II high=0.292, mid=0.350, low=0.276 (median); no phase separation\\\", \\\"registry_id\\\": \\\"bf16_ds_rand_s020\\\", \\\"role\\\": \\\"supporting\\\", \\\"priority\\\": \\\"medium\\\", \\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"interaction_index\\\": {\\\"high\\\": {\\\"mean\\\": 1.1216, \\\"median\\\": 0.2918, \\\"ci\\\": [0.0796, 2.5834], \\\"median_ci\\\": [0.1598, 0.4581], \\\"winsorized_mean\\\": 1.7664, \\\"skewness\\\": 9.59}, \\\"mid\\\": {\\\"mean\\\": -1.5827, \\\"median\\\": 0.3504, \\\"ci\\\": [-6.0963, 1.5735], \\\"median_ci\\\": [0.1993, 0.5226], \\\"winsorized_mean\\\": 0.5839, \\\"skewness\\\": -12.31}, \\\"low\\\": {\\\"mean\\\": -0.4116, \\\"median\\\": 0.2763, \\\"ci\\\": [-2.6034, 1.209], \\\"median_ci\\\": [0.2194, 0.5487], \\\"winsorized_mean\\\": 0.9942, \\\"skewness\\\": -10.07}}, \\\"perplexity\\\": {\\\"high\\\": {\\\"dense\\\": 1.1687, \\\"attn\\\": 3.1905, \\\"kv\\\": 3.8002, \\\"both\\\": 8.8129}, \\\"mid\\\": {\\\"dense\\\": 1.2269, \\\"attn\\\": 67.8504, \\\"kv\\\": 3.788, \\\"both\\\": 11.4974}, \\\"low\\\": {\\\"dense\\\": 1.2284, \\\"attn\\\": 8.592, \\\"kv\\\": 5.0078, \\\"both\\\": 9.2001}}, \\\"phase_stats\\\": {\\\"high\\\": {\\\"n_tokens\\\": 21086, \\\"n_segments\\\": 387}, \\\"mid\\\": {\\\"n_tokens\\\": 13306, \\\"n_segments\\\": 191}, \\\"low\\\": {\\\"n_tokens\\\": 27748, \\\"n_segments\\\": 397}}, \\\"n_problems\\\": 50, \\\"pass_fail\\\": {\\\"ci_overlap\\\": false, \\\"sign_reversal\\\": false, \\\"overall\\\": \\\"FAIL\\\"}, \\\"median_difference\\\": -0.0155}}, {\\\"id\\\": \\\"c4_c4_entropy\\\", \\\"claim\\\": \\\"C4\\\", \\\"description\\\": \\\"DS importance entropy_delta: -0.04 to -0.05 (collapse); random: +0.13 to +0.23 (redistribution). Gini_delta: -0.03 to -0.08\\\", \\\"registry_id\\\": \\\"c4_entropy\\\", \\\"role\\\": \\\"primary\\\", \\\"priority\\\": \\\"high\\\", \\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"importance_entropy_delta\\\": {\\\"s015\\\": -0.0402, \\\"s020\\\": -0.0472, \\\"s025\\\": -0.0446, \\\"s030\\\": -0.0436}, \\\"random_entropy_delta\\\": {\\\"s015\\\": 0.1283, \\\"s020\\\": 0.136, \\\"s025\\\": 0.2171, \\\"s030\\\": 0.2327}, \\\"importance_gini_delta\\\": {\\\"s015\\\": -0.0301, \\\"s020\\\": -0.0404, \\\"s025\\\": -0.0647, \\\"s030\\\": -0.0806}, \\\"random_gini_delta\\\": {\\\"s015\\\": -0.0309, \\\"s020\\\": -0.0403, \\\"s025\\\": -0.062, \\\"s030\\\": -0.0732}, \\\"importance_cv_delta\\\": {\\\"s015\\\": -0.564, \\\"s020\\\": -0.774, \\\"s025\\\": -1.287, \\\"s030\\\": -1.665}, \\\"random_cv_delta\\\": {\\\"s015\\\": -1.021, \\\"s020\\\": -1.203, \\\"s025\\\": -1.923, \\\"s030\\\": -2.137}, \\\"problems_completed\\\": 30, \\\"runtime_minutes\\\": 69.1}}, {\\\"id\\\": \\\"c4_qwen_c4_entropy\\\", \\\"claim\\\": \\\"C4\\\", \\\"description\\\": \\\"QW importance entropy_delta mixed: s015=-0.073, s025=+0.045; Gini weaker (-0.01 to -0.02). Model-dependent pattern\\\", \\\"registry_id\\\": \\\"qwen_c4_entropy\\\", \\\"role\\\": \\\"primary\\\", \\\"priority\\\": \\\"high\\\", \\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\", \\\"metrics\\\": {\\\"problems_completed\\\": 30, \\\"qwen_importance_entropy_delta\\\": {\\\"s015\\\": -0.0733, \\\"s020\\\": -0.0759, \\\"s025\\\": 0.0451, \\\"s030\\\": -0.0072}, \\\"qwen_random_entropy_delta\\\": {\\\"s015\\\": 0.0838, \\\"s020\\\": 0.0901, \\\"s025\\\": 0.2168, \\\"s030\\\": 0.1968}, \\\"qwen_importance_gini_delta\\\": {\\\"s015\\\": -0.0103, \\\"s020\\\": -0.0121, \\\"s025\\\": -0.01, \\\"s030\\\": -0.0202}, \\\"qwen_random_gini_delta\\\": {\\\"s015\\\": -0.0186, \\\"s020\\\": -0.0229, \\\"s025\\\": -0.0337, \\\"s030\\\": -0.0448}, \\\"qwen_importance_cv_delta\\\": {\\\"s015\\\": -0.045, \\\"s020\\\": -0.208, \\\"s025\\\": -1.491, \\\"s030\\\": -1.142}, \\\"qwen_random_cv_delta\\\": {\\\"s015\\\": -0.778, \\\"s020\\\": -0.889, \\\"s025\\\": -1.5, \\\"s030\\\": -1.677}, \\\"cross_model_notes\\\": \\\"random entropy increase consistent; importance entropy collapse inconsistent at s025 (reversed to +0.045) and near-zero at s030; gini/cv directions consistent but Qwen magnitudes smaller\\\"}}, {\\\"id\\\": \\\"c5_bf16_qw_imp_s030\\\", \\\"claim\\\": \\\"C5\\\", \\\"description\\\": \\\"Qwen: median_diff=2.619, Cohen's d=1.439, p<1e-5; replicates DeepSeek pattern\\\", \\\"registry_id\\\": \\\"bf16_qw_imp_s030\\\", \\\"role\\\": \\\"primary\\\", \\\"priority\\\": \\\"high\\\", \\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"median_difference\\\": 2.619385, \\\"permutation_p\\\": 0, \\\"cohens_d\\\": 1.4394, \\\"bootstrap_ci_95\\\": [1.722281, 3.651063], \\\"wilcoxon_p\\\": 0, \\\"n_bootstrap\\\": 10000, \\\"n_paired\\\": 46}}, {\\\"id\\\": \\\"c5_bf16_importance_s030\\\", \\\"claim\\\": \\\"C5\\\", \\\"description\\\": \\\"DeepSeek: II low_median=14.64, high_median=0.053; strong phase gradient\\\", \\\"registry_id\\\": \\\"bf16_importance_s030\\\", \\\"role\\\": \\\"primary\\\", \\\"priority\\\": \\\"high\\\", \\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"interaction_index\\\": {\\\"high\\\": {\\\"mean\\\": 0.5547, \\\"median\\\": 0.0534, \\\"ci\\\": [0.2773, 0.9198], \\\"winsorized_mean\\\": 0.3367, \\\"skewness\\\": 10.62}, \\\"mid\\\": {\\\"mean\\\": 11.3, \\\"median\\\": 2.2833, \\\"ci\\\": [6.865, 17.2633], \\\"winsorized_mean\\\": 8.1752, \\\"skewness\\\": 9.19}, \\\"low\\\": {\\\"mean\\\": 57.7946, \\\"median\\\": 14.6395, \\\"ci\\\": [41.4416, 77.0467], \\\"winsorized_mean\\\": 39.3143, \\\"skewness\\\": 8.31}}, \\\"per_problem_ii_stats\\\": {\\\"high\\\": {\\\"n\\\": 49, \\\"min\\\": -0.5095, \\\"max\\\": 4.4457, \\\"mean\\\": 0.1976, \\\"median\\\": 0.0343, \\\"std\\\": 0.6793}, \\\"mid\\\": {\\\"n\\\": 40, \\\"min\\\": -0.1989, \\\"max\\\": 34.0258, \\\"mean\\\": 5.2585, \\\"median\\\": 1.5173, \\\"std\\\": 7.9382}, \\\"low\\\": {\\\"n\\\": 50, \\\"min\\\": -7.3027, \\\"max\\\": 126.7985, \\\"mean\\\": 22.6601, \\\"median\\\": 9.9731, \\\"std\\\": 28.4096}}, \\\"gradient_paired_aggregate_legacy\\\": 57.24, \\\"median_difference\\\": 14.5861, \\\"n_problems\\\": 50, \\\"pass_fail\\\": {\\\"ci_overlap\\\": true, \\\"sign_reversal\\\": false, \\\"overall\\\": \\\"PASS\\\"}, \\\"phase_stats\\\": {\\\"high\\\": {\\\"n_tokens\\\": 21086, \\\"n_segments\\\": 387}, \\\"mid\\\": {\\\"n_tokens\\\": 13306, \\\"n_segments\\\": 191}, \\\"low\\\": {\\\"n_tokens\\\": 27748, \\\"n_segments\\\": 397}}, \\\"perplexity\\\": {\\\"high\\\": {\\\"dense\\\": 1.1689, \\\"attn\\\": 1.7123, \\\"kv\\\": 2.0544, \\\"both\\\": 3.2372}, \\\"mid\\\": {\\\"dense\\\": 1.2269, \\\"attn\\\": 1.7894, \\\"kv\\\": 9.4821, \\\"both\\\": 24.2847}, \\\"low\\\": {\\\"dense\\\": 1.2286, \\\"attn\\\": 1.9347, \\\"kv\\\": 51.6485, \\\"both\\\": 122.61}}}}, {\\\"id\\\": \\\"c5_c2_n500_deepseek\\\", \\\"claim\\\": \\\"C5\\\", \\\"description\\\": \\\"DS n=500: imp_s030 median_II=8.48, CI=[7.46,9.56], p=1.3e-78; robust at scale\\\", \\\"registry_id\\\": \\\"c2_n500_deepseek\\\", \\\"role\\\": \\\"supporting\\\", \\\"priority\\\": \\\"medium\\\", \\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"n_problems\\\": 500, \\\"effective_n\\\": 496, \\\"mid_null_rate\\\": 0.102, \\\"imp_s015_median_ii\\\": 0.3907, \\\"imp_s015_ci\\\": [0.3496, 0.4431], \\\"imp_s015_wilcoxon_p\\\": 1.27e-70, \\\"imp_s020_median_ii\\\": 1.2149, \\\"imp_s020_ci\\\": [1.1072, 1.3365], \\\"imp_s020_wilcoxon_p\\\": 3.98e-75, \\\"imp_s025_median_ii\\\": 3.9857, \\\"imp_s025_ci\\\": [3.5272, 4.3588], \\\"imp_s025_wilcoxon_p\\\": 1.99e-78, \\\"imp_s030_median_ii\\\": 8.4813, \\\"imp_s030_ci\\\": [7.7543, 9.6919], \\\"imp_s030_wilcoxon_p\\\": 1.09e-79, \\\"rand_s015_median_ii\\\": 0.0139, \\\"rand_s015_wilcoxon_p\\\": 0.863, \\\"rand_s020_median_ii\\\": 0.0315, \\\"rand_s020_wilcoxon_p\\\": 0.28, \\\"rand_s025_median_ii\\\": 0.2574, \\\"rand_s025_bonf_p\\\": 0.005839, \\\"rand_s025_fdr_p\\\": 0.001914, \\\"rand_s030_median_ii\\\": 0.5096, \\\"rand_s030_bonf_p\\\": 0.005903, \\\"rand_s030_fdr_p\\\": 0.001914, \\\"dz_s015_s020\\\": -0.925, \\\"dz_s020_s025\\\": -0.824, \\\"dz_s025_s030\\\": -0.773, \\\"dz_s015_s030\\\": -0.944, \\\"all_dz_reliable\\\": true, \\\"dose_response_monotonic\\\": true, \\\"dose_response_spearman_rho\\\": 1, \\\"dose_response_perm_p\\\": 0.0417, \\\"imp_rand_ratio_range\\\": \\\"15.5-38.6x\\\", \\\"bonferroni_k\\\": 4, \\\"bonferroni_note\\\": \\\"Bonferroni k=4 family-wise (D066 revision)\\\"}}, {\\\"id\\\": \\\"c5_c2_qw_n500_r3\\\", \\\"claim\\\": \\\"C5\\\", \\\"description\\\": \\\"QW n=500: imp_s030 median_II=4.33, p<1e-40; cross-model replication at high power\\\", \\\"registry_id\\\": \\\"c2_qw_n500_r3\\\", \\\"role\\\": \\\"supporting\\\", \\\"priority\\\": \\\"medium\\\", \\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"n_problems\\\": 500, \\\"effective_n\\\": 475, \\\"filter\\\": \\\"low+high valid only (mid-null allowed)\\\", \\\"mid_null_rate\\\": 0.452, \\\"imp_s015_median_ii\\\": 0.0659, \\\"imp_s015_ci\\\": [0.0492, 0.0925], \\\"imp_s015_wilcoxon_p\\\": 8.66e-15, \\\"imp_s015_bonf_p\\\": 3.46e-14, \\\"imp_s020_median_ii\\\": 0.3073, \\\"imp_s020_ci\\\": [0.2612, 0.3564], \\\"imp_s020_wilcoxon_p\\\": 6.84e-42, \\\"imp_s020_bonf_p\\\": 2.74e-41, \\\"imp_s025_median_ii\\\": 1.0745, \\\"imp_s025_ci\\\": [0.9766, 1.1787], \\\"imp_s025_wilcoxon_p\\\": 1.06e-68, \\\"imp_s025_bonf_p\\\": 4.25e-68, \\\"imp_s030_median_ii\\\": 3.155, \\\"imp_s030_ci\\\": [2.7834, 3.5582], \\\"imp_s030_wilcoxon_p\\\": 9.21e-74, \\\"imp_s030_bonf_p\\\": 3.69e-73, \\\"rand_s015_median_ii\\\": -0.0111, \\\"rand_s015_wilcoxon_p\\\": 0.172, \\\"rand_s015_bonf_p\\\": 0.687, \\\"rand_s020_median_ii\\\": 0.0153, \\\"rand_s020_wilcoxon_p\\\": 0.2, \\\"rand_s020_bonf_p\\\": 0.8, \\\"rand_s025_median_ii\\\": 0.3931, \\\"rand_s025_wilcoxon_p\\\": 1.59e-11, \\\"rand_s025_bonf_p\\\": 6.37e-11, \\\"rand_s025_fdr_p\\\": 2.63e-11, \\\"rand_s030_median_ii\\\": 0.9127, \\\"rand_s030_wilcoxon_p\\\": 2.92e-15, \\\"rand_s030_bonf_p\\\": 1.17e-14, \\\"rand_s030_fdr_p\\\": 5.61e-15, \\\"dz_s015_s020\\\": -0.629, \\\"dz_s020_s025\\\": -0.865, \\\"dz_s025_s030\\\": -0.767, \\\"dz_s015_s030\\\": -0.923, \\\"all_dz_reliable\\\": true, \\\"dose_response_monotonic\\\": true, \\\"dose_response_spearman_rho\\\": 1, \\\"dose_response_perm_p\\\": 0.0417, \\\"imp_rand_ratio_range\\\": \\\"2.7-20.1x\\\", \\\"bonferroni_k\\\": 4, \\\"bonferroni_note\\\": \\\"Bonferroni k=4 family-wise (D066 revision)\\\"}}, {\\\"id\\\": \\\"c5b_c5b_pilot\\\", \\\"claim\\\": \\\"C5b\\\", \\\"description\\\": \\\"Oracle recovery=18% (gate: >30% FAIL); heuristic recovery=31.7% but CI crosses zero. s030 incomplete\\\", \\\"registry_id\\\": \\\"c5b_pilot\\\", \\\"role\\\": \\\"primary\\\", \\\"priority\\\": \\\"high\\\", \\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\", \\\"metrics\\\": {\\\"s025_uniform_median_ii\\\": 1.0435, \\\"s025_oracle_median_ii\\\": 0.856, \\\"s025_oracle_recovery_pct\\\": 18, \\\"s025_oracle_recovery_ci\\\": [-39, 45.8], \\\"s025_oracle_wilcoxon_p\\\": 0.0021, \\\"s025_heuristic_median_ii\\\": 0.7127, \\\"s025_heuristic_recovery_pct\\\": 31.7, \\\"s025_heuristic_recovery_ci\\\": [-22.8, 66], \\\"s025_heuristic_wilcoxon_p\\\": 0.0236, \\\"gate_criterion\\\": \\\"oracle_recovery > 30%\\\", \\\"gate_result\\\": \\\"FAIL\\\", \\\"s030_status\\\": \\\"not_completed\\\", \\\"n_problems\\\": 30}}, {\\\"id\\\": \\\"c6_bf16_importance_s015\\\", \\\"claim\\\": \\\"C6\\\", \\\"description\\\": \\\"II low_median=0.398 at s=0.15\\\", \\\"registry_id\\\": \\\"bf16_importance_s015\\\", \\\"role\\\": \\\"primary\\\", \\\"priority\\\": \\\"high\\\", \\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"interaction_index\\\": {\\\"high\\\": {\\\"mean\\\": -0.150213, \\\"median\\\": 0.005752, \\\"ci\\\": [-0.294614, -0.055385], \\\"winsorized_mean\\\": -0.062378, \\\"skewness\\\": -14.9912}, \\\"mid\\\": {\\\"mean\\\": 0.447301, \\\"median\\\": 0.080738, \\\"ci\\\": [0.267993, 0.668749], \\\"winsorized_mean\\\": 0.324751, \\\"skewness\\\": 4.7221}, \\\"low\\\": {\\\"mean\\\": 2.405837, \\\"median\\\": 0.398291, \\\"ci\\\": [1.478784, 3.667675], \\\"winsorized_mean\\\": 1.278857, \\\"skewness\\\": 9.5402}}, \\\"per_problem_ii_stats\\\": {\\\"high\\\": {\\\"n\\\": 49, \\\"min\\\": -0.188061, \\\"max\\\": 0.335853, \\\"mean\\\": -0.013405, \\\"median\\\": 0.00012, \\\"std\\\": 0.078483}, \\\"mid\\\": {\\\"n\\\": 40, \\\"min\\\": -0.169092, \\\"max\\\": 3.88198, \\\"mean\\\": 0.308621, \\\"median\\\": 0.107114, \\\"std\\\": 0.690186}, \\\"low\\\": {\\\"n\\\": 50, \\\"min\\\": -0.872983, \\\"max\\\": 9.10289, \\\"mean\\\": 0.725504, \\\"median\\\": 0.315517, \\\"std\\\": 1.731056}}, \\\"gradient_paired_aggregate_legacy\\\": 69.24, \\\"median_difference\\\": 0.3925, \\\"n_problems\\\": 50, \\\"pass_fail\\\": {\\\"ci_overlap\\\": true, \\\"sign_reversal\\\": true, \\\"overall\\\": \\\"PASS\\\"}, \\\"phase_stats\\\": {\\\"high\\\": {\\\"n_tokens\\\": 21086, \\\"n_segments\\\": 387}, \\\"mid\\\": {\\\"n_tokens\\\": 13306, \\\"n_segments\\\": 191}, \\\"low\\\": {\\\"n_tokens\\\": 27748, \\\"n_segments\\\": 397}}, \\\"perplexity\\\": {\\\"high\\\": {\\\"dense\\\": 1.1689, \\\"attn\\\": 1.4861, \\\"kv\\\": 1.4481, \\\"both\\\": 1.5911}, \\\"mid\\\": {\\\"dense\\\": 1.2269, \\\"attn\\\": 1.5137, \\\"kv\\\": 2.5971, \\\"both\\\": 3.4541}, \\\"low\\\": {\\\"dense\\\": 1.2286, \\\"attn\\\": 1.6147, \\\"kv\\\": 8.9201, \\\"both\\\": 12.5084}}}}, {\\\"id\\\": \\\"c6_bf16_importance_s020\\\", \\\"claim\\\": \\\"C6\\\", \\\"description\\\": \\\"II low_median=1.496 at s=0.20\\\", \\\"registry_id\\\": \\\"bf16_importance_s020\\\", \\\"role\\\": \\\"supporting\\\", \\\"priority\\\": \\\"medium\\\", \\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"interaction_index\\\": {\\\"high\\\": {\\\"mean\\\": 0.1289, \\\"median\\\": 0.0145, \\\"ci\\\": [-0.1975, 0.6647], \\\"winsorized_mean\\\": -0.0297, \\\"skewness\\\": 16.67}, \\\"mid\\\": {\\\"mean\\\": 1.2604, \\\"median\\\": 0.2027, \\\"ci\\\": [0.7466, 1.8962], \\\"winsorized_mean\\\": 0.766, \\\"skewness\\\": 7.05}, \\\"low\\\": {\\\"mean\\\": 6.0288, \\\"median\\\": 1.4963, \\\"ci\\\": [4.4671, 7.9237], \\\"winsorized_mean\\\": 4.3426, \\\"skewness\\\": 6.01}}, \\\"per_problem_ii_stats\\\": {\\\"high\\\": {\\\"n\\\": 49, \\\"min\\\": -0.1884, \\\"max\\\": 0.4196, \\\"mean\\\": 0.0025, \\\"median\\\": 0.0036, \\\"std\\\": 0.0966}, \\\"mid\\\": {\\\"n\\\": 40, \\\"min\\\": -0.0519, \\\"max\\\": 8.6969, \\\"mean\\\": 0.6795, \\\"median\\\": 0.1977, \\\"std\\\": 1.4998}, \\\"low\\\": {\\\"n\\\": 50, \\\"min\\\": -1.6151, \\\"max\\\": 22.6875, \\\"mean\\\": 2.2301, \\\"median\\\": 1.128, \\\"std\\\": 4.3758}}, \\\"gradient_paired_aggregate_legacy\\\": 5.9, \\\"median_difference\\\": 1.4818, \\\"n_problems\\\": 50, \\\"pass_fail\\\": {\\\"ci_overlap\\\": true, \\\"sign_reversal\\\": false, \\\"overall\\\": \\\"PASS\\\"}, \\\"phase_stats\\\": {\\\"high\\\": {\\\"n_tokens\\\": 21086, \\\"n_segments\\\": 387}, \\\"mid\\\": {\\\"n_tokens\\\": 13306, \\\"n_segments\\\": 191}, \\\"low\\\": {\\\"n_tokens\\\": 27748, \\\"n_segments\\\": 397}}, \\\"perplexity\\\": {\\\"high\\\": {\\\"dense\\\": 1.1689, \\\"attn\\\": 1.5233, \\\"kv\\\": 1.6191, \\\"both\\\": 2.1047}, \\\"mid\\\": {\\\"dense\\\": 1.2269, \\\"attn\\\": 1.5375, \\\"kv\\\": 3.5164, \\\"both\\\": 5.4246}, \\\"low\\\": {\\\"dense\\\": 1.2286, \\\"attn\\\": 1.6486, \\\"kv\\\": 15.7987, \\\"both\\\": 23.74}}}}, {\\\"id\\\": \\\"c6_bf16_importance_s025\\\", \\\"claim\\\": \\\"C6\\\", \\\"description\\\": \\\"II low_median=7.196 at s=0.25\\\", \\\"registry_id\\\": \\\"bf16_importance_s025\\\", \\\"role\\\": \\\"supporting\\\", \\\"priority\\\": \\\"medium\\\", \\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"interaction_index\\\": {\\\"high\\\": {\\\"mean\\\": 0.302756, \\\"median\\\": 0.032363, \\\"ci\\\": [0.083714, 0.543977], \\\"winsorized_mean\\\": 0.200962, \\\"skewness\\\": 4.8826}, \\\"mid\\\": {\\\"mean\\\": 5.729665, \\\"median\\\": 1.118069, \\\"ci\\\": [3.455574, 8.471799], \\\"winsorized_mean\\\": 4.189902, \\\"skewness\\\": 8.2799}, \\\"low\\\": {\\\"mean\\\": 25.852951, \\\"median\\\": 7.195958, \\\"ci\\\": [19.077082, 33.497293], \\\"winsorized_mean\\\": 19.319103, \\\"skewness\\\": 7.3986}}, \\\"per_problem_ii_stats\\\": {\\\"high\\\": {\\\"n\\\": 49, \\\"min\\\": -0.316321, \\\"max\\\": 4.003714, \\\"mean\\\": 0.133714, \\\"median\\\": 0.009873, \\\"std\\\": 0.595358}, \\\"mid\\\": {\\\"n\\\": 40, \\\"min\\\": -0.024794, \\\"max\\\": 18.720486, \\\"mean\\\": 2.537744, \\\"median\\\": 1.05707, \\\"std\\\": 3.962575}, \\\"low\\\": {\\\"n\\\": 50, \\\"min\\\": -1.854733, \\\"max\\\": 75.467653, \\\"mean\\\": 11.28281, \\\"median\\\": 3.954593, \\\"std\\\": 16.620011}}, \\\"gradient_paired_aggregate_legacy\\\": 222.35, \\\"median_difference\\\": 7.1636, \\\"n_problems\\\": 50, \\\"pass_fail\\\": {\\\"ci_overlap\\\": true, \\\"sign_reversal\\\": false, \\\"overall\\\": \\\"PASS\\\"}, \\\"phase_stats\\\": {\\\"high\\\": {\\\"n_tokens\\\": 21086, \\\"n_segments\\\": 387}, \\\"mid\\\": {\\\"n_tokens\\\": 13306, \\\"n_segments\\\": 191}, \\\"low\\\": {\\\"n_tokens\\\": 27748, \\\"n_segments\\\": 397}}, \\\"perplexity\\\": {\\\"high\\\": {\\\"dense\\\": 1.1689, \\\"attn\\\": 1.6511, \\\"kv\\\": 1.8628, \\\"both\\\": 2.7026}, \\\"mid\\\": {\\\"dense\\\": 1.2269, \\\"attn\\\": 1.7039, \\\"kv\\\": 5.6205, \\\"both\\\": 13.3436}, \\\"low\\\": {\\\"dense\\\": 1.2286, \\\"attn\\\": 1.8366, \\\"kv\\\": 31.756, \\\"both\\\": 63.668}}}}, {\\\"id\\\": \\\"c6_bf16_importance_s030\\\", \\\"claim\\\": \\\"C6\\\", \\\"description\\\": \\\"II low_median=14.64 at s=0.30; growth 0.40->1.50->7.20->14.64 is sub-exponential\\\", \\\"registry_id\\\": \\\"bf16_importance_s030\\\", \\\"role\\\": \\\"supporting\\\", \\\"priority\\\": \\\"medium\\\", \\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"interaction_index\\\": {\\\"high\\\": {\\\"mean\\\": 0.5547, \\\"median\\\": 0.0534, \\\"ci\\\": [0.2773, 0.9198], \\\"winsorized_mean\\\": 0.3367, \\\"skewness\\\": 10.62}, \\\"mid\\\": {\\\"mean\\\": 11.3, \\\"median\\\": 2.2833, \\\"ci\\\": [6.865, 17.2633], \\\"winsorized_mean\\\": 8.1752, \\\"skewness\\\": 9.19}, \\\"low\\\": {\\\"mean\\\": 57.7946, \\\"median\\\": 14.6395, \\\"ci\\\": [41.4416, 77.0467], \\\"winsorized_mean\\\": 39.3143, \\\"skewness\\\": 8.31}}, \\\"per_problem_ii_stats\\\": {\\\"high\\\": {\\\"n\\\": 49, \\\"min\\\": -0.5095, \\\"max\\\": 4.4457, \\\"mean\\\": 0.1976, \\\"median\\\": 0.0343, \\\"std\\\": 0.6793}, \\\"mid\\\": {\\\"n\\\": 40, \\\"min\\\": -0.1989, \\\"max\\\": 34.0258, \\\"mean\\\": 5.2585, \\\"median\\\": 1.5173, \\\"std\\\": 7.9382}, \\\"low\\\": {\\\"n\\\": 50, \\\"min\\\": -7.3027, \\\"max\\\": 126.7985, \\\"mean\\\": 22.6601, \\\"median\\\": 9.9731, \\\"std\\\": 28.4096}}, \\\"gradient_paired_aggregate_legacy\\\": 57.24, \\\"median_difference\\\": 14.5861, \\\"n_problems\\\": 50, \\\"pass_fail\\\": {\\\"ci_overlap\\\": true, \\\"sign_reversal\\\": false, \\\"overall\\\": \\\"PASS\\\"}, \\\"phase_stats\\\": {\\\"high\\\": {\\\"n_tokens\\\": 21086, \\\"n_segments\\\": 387}, \\\"mid\\\": {\\\"n_tokens\\\": 13306, \\\"n_segments\\\": 191}, \\\"low\\\": {\\\"n_tokens\\\": 27748, \\\"n_segments\\\": 397}}, \\\"perplexity\\\": {\\\"high\\\": {\\\"dense\\\": 1.1689, \\\"attn\\\": 1.7123, \\\"kv\\\": 2.0544, \\\"both\\\": 3.2372}, \\\"mid\\\": {\\\"dense\\\": 1.2269, \\\"attn\\\": 1.7894, \\\"kv\\\": 9.4821, \\\"both\\\": 24.2847}, \\\"low\\\": {\\\"dense\\\": 1.2286, \\\"attn\\\": 1.9347, \\\"kv\\\": 51.6485, \\\"both\\\": 122.61}}}}, {\\\"id\\\": \\\"c7_c2_n500_deepseek\\\", \\\"claim\\\": \\\"C7\\\", \\\"description\\\": \\\"DS n=500: all 4 sparsities significant (p<1e-70); CIs non-overlapping across dose levels\\\", \\\"registry_id\\\": \\\"c2_n500_deepseek\\\", \\\"role\\\": \\\"primary\\\", \\\"priority\\\": \\\"high\\\", \\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"n_problems\\\": 500, \\\"effective_n\\\": 496, \\\"mid_null_rate\\\": 0.102, \\\"imp_s015_median_ii\\\": 0.3907, \\\"imp_s015_ci\\\": [0.3496, 0.4431], \\\"imp_s015_wilcoxon_p\\\": 1.27e-70, \\\"imp_s020_median_ii\\\": 1.2149, \\\"imp_s020_ci\\\": [1.1072, 1.3365], \\\"imp_s020_wilcoxon_p\\\": 3.98e-75, \\\"imp_s025_median_ii\\\": 3.9857, \\\"imp_s025_ci\\\": [3.5272, 4.3588], \\\"imp_s025_wilcoxon_p\\\": 1.99e-78, \\\"imp_s030_median_ii\\\": 8.4813, \\\"imp_s030_ci\\\": [7.7543, 9.6919], \\\"imp_s030_wilcoxon_p\\\": 1.09e-79, \\\"rand_s015_median_ii\\\": 0.0139, \\\"rand_s015_wilcoxon_p\\\": 0.863, \\\"rand_s020_median_ii\\\": 0.0315, \\\"rand_s020_wilcoxon_p\\\": 0.28, \\\"rand_s025_median_ii\\\": 0.2574, \\\"rand_s025_bonf_p\\\": 0.005839, \\\"rand_s025_fdr_p\\\": 0.001914, \\\"rand_s030_median_ii\\\": 0.5096, \\\"rand_s030_bonf_p\\\": 0.005903, \\\"rand_s030_fdr_p\\\": 0.001914, \\\"dz_s015_s020\\\": -0.925, \\\"dz_s020_s025\\\": -0.824, \\\"dz_s025_s030\\\": -0.773, \\\"dz_s015_s030\\\": -0.944, \\\"all_dz_reliable\\\": true, \\\"dose_response_monotonic\\\": true, \\\"dose_response_spearman_rho\\\": 1, \\\"dose_response_perm_p\\\": 0.0417, \\\"imp_rand_ratio_range\\\": \\\"15.5-38.6x\\\", \\\"bonferroni_k\\\": 4, \\\"bonferroni_note\\\": \\\"Bonferroni k=4 family-wise (D066 revision)\\\"}}, {\\\"id\\\": \\\"c7_c2_qw_n500_r3\\\", \\\"claim\\\": \\\"C7\\\", \\\"description\\\": \\\"QW n=500: all 4 sparsities significant (p<1e-14 Bonferroni-corrected); mid_null_rate=45.2%\\\", \\\"registry_id\\\": \\\"c2_qw_n500_r3\\\", \\\"role\\\": \\\"primary\\\", \\\"priority\\\": \\\"high\\\", \\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"n_problems\\\": 500, \\\"effective_n\\\": 475, \\\"filter\\\": \\\"low+high valid only (mid-null allowed)\\\", \\\"mid_null_rate\\\": 0.452, \\\"imp_s015_median_ii\\\": 0.0659, \\\"imp_s015_ci\\\": [0.0492, 0.0925], \\\"imp_s015_wilcoxon_p\\\": 8.66e-15, \\\"imp_s015_bonf_p\\\": 3.46e-14, \\\"imp_s020_median_ii\\\": 0.3073, \\\"imp_s020_ci\\\": [0.2612, 0.3564], \\\"imp_s020_wilcoxon_p\\\": 6.84e-42, \\\"imp_s020_bonf_p\\\": 2.74e-41, \\\"imp_s025_median_ii\\\": 1.0745, \\\"imp_s025_ci\\\": [0.9766, 1.1787], \\\"imp_s025_wilcoxon_p\\\": 1.06e-68, \\\"imp_s025_bonf_p\\\": 4.25e-68, \\\"imp_s030_median_ii\\\": 3.155, \\\"imp_s030_ci\\\": [2.7834, 3.5582], \\\"imp_s030_wilcoxon_p\\\": 9.21e-74, \\\"imp_s030_bonf_p\\\": 3.69e-73, \\\"rand_s015_median_ii\\\": -0.0111, \\\"rand_s015_wilcoxon_p\\\": 0.172, \\\"rand_s015_bonf_p\\\": 0.687, \\\"rand_s020_median_ii\\\": 0.0153, \\\"rand_s020_wilcoxon_p\\\": 0.2, \\\"rand_s020_bonf_p\\\": 0.8, \\\"rand_s025_median_ii\\\": 0.3931, \\\"rand_s025_wilcoxon_p\\\": 1.59e-11, \\\"rand_s025_bonf_p\\\": 6.37e-11, \\\"rand_s025_fdr_p\\\": 2.63e-11, \\\"rand_s030_median_ii\\\": 0.9127, \\\"rand_s030_wilcoxon_p\\\": 2.92e-15, \\\"rand_s030_bonf_p\\\": 1.17e-14, \\\"rand_s030_fdr_p\\\": 5.61e-15, \\\"dz_s015_s020\\\": -0.629, \\\"dz_s020_s025\\\": -0.865, \\\"dz_s025_s030\\\": -0.767, \\\"dz_s015_s030\\\": -0.923, \\\"all_dz_reliable\\\": true, \\\"dose_response_monotonic\\\": true, \\\"dose_response_spearman_rho\\\": 1, \\\"dose_response_perm_p\\\": 0.0417, \\\"imp_rand_ratio_range\\\": \\\"2.7-20.1x\\\", \\\"bonferroni_k\\\": 4, \\\"bonferroni_note\\\": \\\"Bonferroni k=4 family-wise (D066 revision)\\\"}}, {\\\"id\\\": \\\"c8_c3_llama\\\", \\\"claim\\\": \\\"C8\\\", \\\"description\\\": \\\"LLaMA-8B (LlamaForCausalLM) replicates phase-modulated compound severity from Qwen2ForCausalLM\\\", \\\"registry_id\\\": \\\"c3_llama\\\", \\\"role\\\": \\\"primary\\\", \\\"priority\\\": \\\"high\\\", \\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, {\\\"id\\\": \\\"c10_gsm8k_profiling_ds\\\", \\\"claim\\\": \\\"C10\\\", \\\"description\\\": \\\"DS GSM8K importance gradient: s015=0.241, s020=0.740, s025=1.992, s030=4.636 (monotonic)\\\", \\\"registry_id\\\": \\\"gsm8k_profiling_ds\\\", \\\"role\\\": \\\"primary\\\", \\\"priority\\\": \\\"high\\\", \\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"version\\\": \\\"v3_median\\\", \\\"n_problems\\\": 50, \\\"method\\\": \\\"median + Wilcoxon + bootstrap_median(B=10000)\\\", \\\"importance\\\": {\\\"s015\\\": {\\\"median_gradient\\\": 0.241, \\\"ci_low\\\": 0.077, \\\"ci_high\\\": 0.478, \\\"wilcoxon_p\\\": 0.0003}, \\\"s020\\\": {\\\"median_gradient\\\": 0.74, \\\"ci_low\\\": 0.314, \\\"ci_high\\\": 1.119, \\\"wilcoxon_p\\\": 0.0001}, \\\"s025\\\": {\\\"median_gradient\\\": 1.992, \\\"ci_low\\\": 0.933, \\\"ci_high\\\": 2.82, \\\"wilcoxon_p\\\": 0.0001}, \\\"s030\\\": {\\\"median_gradient\\\": 4.682, \\\"ci_low\\\": 2.121, \\\"ci_high\\\": 10.557, \\\"wilcoxon_p\\\": 0.0001}}, \\\"imp_rand_ratio\\\": {\\\"s015\\\": 2.3, \\\"s020\\\": 2.5, \\\"s025\\\": 3.8, \\\"s030\\\": 2.8}, \\\"dose_response_monotonic\\\": true}}, {\\\"id\\\": \\\"c10_gsm8k_profiling_qw\\\", \\\"claim\\\": \\\"C10\\\", \\\"description\\\": \\\"QW GSM8K importance gradient: s015=0.039, s020=0.158, s025=1.100, s030=2.092 (monotonic)\\\", \\\"registry_id\\\": \\\"gsm8k_profiling_qw\\\", \\\"role\\\": \\\"primary\\\", \\\"priority\\\": \\\"high\\\", \\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"version\\\": \\\"v3_median\\\", \\\"n_problems\\\": 50, \\\"method\\\": \\\"median + Wilcoxon + bootstrap_median(B=10000)\\\", \\\"importance\\\": {\\\"s015\\\": {\\\"median_gradient\\\": 0.039}, \\\"s020\\\": {\\\"median_gradient\\\": 0.158}, \\\"s025\\\": {\\\"median_gradient\\\": 1.1}, \\\"s030\\\": {\\\"median_gradient\\\": 2.092}}, \\\"qw_rand_s030\\\": \\\"INVALID\\\"}}, {\\\"id\\\": \\\"c10_gsm8k_qw_rand_s025_v2\\\", \\\"claim\\\": \\\"C10\\\", \\\"description\\\": \\\"QW random s025 GSM8K: II median_high=0.72, low=1.48; phase gradient weaker than importance\\\", \\\"registry_id\\\": \\\"gsm8k_qw_rand_s025_v2\\\", \\\"role\\\": \\\"supporting\\\", \\\"priority\\\": \\\"medium\\\", \\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"verdict\\\": \\\"PASS\\\", \\\"n_problems\\\": 50, \\\"n_bootstrap\\\": 1000, \\\"seed\\\": 42, \\\"high_sparsity\\\": {\\\"n_segments\\\": 216, \\\"n_tokens\\\": 9326, \\\"ppl_dense\\\": 1.0695, \\\"ppl_attn\\\": 5.9362, \\\"ppl_kv\\\": 3.4316, \\\"ppl_both\\\": 15.7484, \\\"ii_mean\\\": 6.5954, \\\"ii_ci\\\": [1.1114, 11.3791], \\\"ii_median\\\": 0.7176, \\\"ii_median_ci\\\": [0.5959, 0.9347], \\\"winsorized_mean\\\": 6.5046, \\\"skewness\\\": -4.6807, \\\"outlier_count\\\": 3}, \\\"low_sparsity\\\": {\\\"n_segments\\\": 252, \\\"n_tokens\\\": 29224, \\\"ppl_dense\\\": 1.1972, \\\"ppl_attn\\\": 11.5347, \\\"ppl_kv\\\": 5.6038, \\\"ppl_both\\\": 21.6874, \\\"ii_mean\\\": 2.3883, \\\"ii_ci\\\": [-8.4602, 11.029], \\\"ii_median\\\": 1.4587, \\\"ii_median_ci\\\": [1.1121, 2.0451], \\\"winsorized_mean\\\": 5.8911, \\\"skewness\\\": -7.6074, \\\"outlier_count\\\": 4}, \\\"mid_sparsity\\\": {\\\"n_segments\\\": 51, \\\"n_tokens\\\": 5954, \\\"ppl_dense\\\": 1.2601, \\\"ppl_attn\\\": 13.4132, \\\"ppl_kv\\\": 6.4841, \\\"ppl_both\\\": 20.8714, \\\"ii_mean\\\": 4.5407, \\\"ii_ci\\\": [-4.8854, 12.4605], \\\"ii_median\\\": 1.1272, \\\"ii_median_ci\\\": [0.637, 3.3729], \\\"winsorized_mean\\\": 6.3284, \\\"skewness\\\": -3.4048, \\\"outlier_count\\\": 1}}}, {\\\"id\\\": \\\"c10_gsm8k_qw_rand_s030_v2\\\", \\\"claim\\\": \\\"C10\\\", \\\"description\\\": \\\"QW random s030 GSM8K: II median_high=2.31, low=5.87; compound effect on GSM8K confirmed\\\", \\\"registry_id\\\": \\\"gsm8k_qw_rand_s030_v2\\\", \\\"role\\\": \\\"supporting\\\", \\\"priority\\\": \\\"medium\\\", \\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"verdict\\\": \\\"PASS\\\", \\\"n_problems\\\": 50, \\\"n_bootstrap\\\": 1000, \\\"seed\\\": 42, \\\"high_sparsity\\\": {\\\"n_segments\\\": 216, \\\"n_tokens\\\": 9326, \\\"null_ratio\\\": \\\"2/50\\\", \\\"ppl_dense\\\": 1.0695, \\\"ppl_attn\\\": 6.5613, \\\"ppl_kv\\\": 4.481, \\\"ppl_both\\\": 23.7486, \\\"ii_mean\\\": 11.83, \\\"ii_median\\\": 2.31, \\\"ii_ci\\\": [6.17, 17.04], \\\"ii_median_ci\\\": [1.64, 2.81], \\\"winsorized_mean\\\": 10.55, \\\"skewness\\\": -2.29, \\\"outlier_count\\\": 7}, \\\"low_sparsity\\\": {\\\"n_segments\\\": 252, \\\"n_tokens\\\": 29224, \\\"null_ratio\\\": \\\"5/50\\\", \\\"ppl_dense\\\": 1.1972, \\\"ppl_attn\\\": 6.3283, \\\"ppl_kv\\\": 8.5374, \\\"ppl_both\\\": 56.2304, \\\"ii_mean\\\": 31.26, \\\"ii_median\\\": 5.2, \\\"ii_ci\\\": [17.84, 47.86], \\\"ii_median_ci\\\": [3.95, 7.24], \\\"winsorized_mean\\\": 16.35, \\\"skewness\\\": 7.57, \\\"outlier_count\\\": 4}, \\\"mid_sparsity\\\": {\\\"n_segments\\\": 51, \\\"n_tokens\\\": 5954, \\\"null_ratio\\\": \\\"17/50\\\", \\\"ppl_dense\\\": 1.2601, \\\"ppl_attn\\\": 18.6162, \\\"ppl_kv\\\": 11.6625, \\\"ppl_both\\\": 47.9019, \\\"ii_mean\\\": 18.02, \\\"ii_median\\\": 2.7, \\\"ii_ci\\\": [0.09, 36.69], \\\"ii_median_ci\\\": [1.46, 8.77], \\\"winsorized_mean\\\": 18.22, \\\"skewness\\\": 0.43, \\\"outlier_count\\\": 2}}}, {\\\"id\\\": \\\"s3_c_bf16_ds_imp_s010\\\", \\\"claim\\\": \\\"S3->C\\\", \\\"description\\\": \\\"DS s=0.10: II_high_median=0.003, verdict=FAIL; below onset threshold for DeepSeek\\\", \\\"registry_id\\\": \\\"bf16_ds_imp_s010\\\", \\\"role\\\": \\\"primary\\\", \\\"priority\\\": \\\"high\\\", \\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\", \\\"metrics\\\": {\\\"verdict\\\": \\\"FAIL\\\", \\\"problems\\\": 50, \\\"II_high_sparsity_median\\\": 0.0027, \\\"II_high_sparsity_mean\\\": -0.1998, \\\"II_low_sparsity_median\\\": 0.0151, \\\"II_low_sparsity_mean\\\": -0.1066, \\\"II_mid_sparsity_median\\\": 0.0061, \\\"II_mid_sparsity_mean\\\": -0.0131, \\\"high_sparsity_tokens\\\": 21086, \\\"low_sparsity_tokens\\\": 27748, \\\"mid_sparsity_tokens\\\": 13306}}, {\\\"id\\\": \\\"s3_c_bf16_qw_imp_s010\\\", \\\"claim\\\": \\\"S3->C\\\", \\\"description\\\": \\\"QW s=0.10: overall_verdict=PASS, CI_overlap_test=PASS; Qwen onset earlier than DeepSeek\\\", \\\"registry_id\\\": \\\"bf16_qw_imp_s010\\\", \\\"role\\\": \\\"primary\\\", \\\"priority\\\": \\\"high\\\", \\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"n_problems\\\": 50, \\\"overall_verdict\\\": \\\"PASS\\\", \\\"ci_overlap_test\\\": \\\"PASS\\\", \\\"sign_reversal_test\\\": \\\"FAIL\\\", \\\"high_sparsity_II_median\\\": 0.0001, \\\"high_sparsity_II_median_CI\\\": [-0.0028, 0.0005], \\\"high_sparsity_II_mean\\\": -0.0887, \\\"high_sparsity_II_mean_CI\\\": [-0.1235, -0.0591], \\\"low_sparsity_II_median\\\": -0.0444, \\\"low_sparsity_II_median_CI\\\": [-0.0967, -0.0152], \\\"low_sparsity_II_mean\\\": -0.2431, \\\"low_sparsity_II_mean_CI\\\": [-0.3817, -0.1202], \\\"mid_sparsity_II_median\\\": -0.0359, \\\"mid_sparsity_II_median_CI\\\": [-0.0963, -0.015], \\\"mid_sparsity_II_mean\\\": -0.084, \\\"mid_sparsity_II_mean_CI\\\": [-0.1366, -0.035], \\\"ppl_high_dense\\\": 1.074, \\\"ppl_high_both\\\": 1.228, \\\"ppl_low_dense\\\": 1.152, \\\"ppl_low_both\\\": 3.204, \\\"ppl_mid_dense\\\": 1.133, \\\"ppl_mid_both\\\": 1.741}}, {\\\"id\\\": \\\"s3_c_bf16_qw_imp_s015\\\", \\\"claim\\\": \\\"S3->C\\\", \\\"description\\\": \\\"QW s=0.15: median_diff=0.048, permutation_p=0.0001; confirmed above threshold\\\", \\\"registry_id\\\": \\\"bf16_qw_imp_s015\\\", \\\"role\\\": \\\"supporting\\\", \\\"priority\\\": \\\"medium\\\", \\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"median_difference\\\": 0.047619, \\\"permutation_p\\\": 0.0001, \\\"cohens_d\\\": 0.3705, \\\"bootstrap_ci_95\\\": [-0.005077, 0.109517], \\\"wilcoxon_p\\\": 0.02958, \\\"n_bootstrap\\\": 10000, \\\"n_paired\\\": 46}}, {\\\"id\\\": \\\"s7_c_c2_n500_deepseek\\\", \\\"claim\\\": \\\"S7->C\\\", \\\"description\\\": \\\"DS n=500 monotonic: imp median II 0.39->1.21->3.99->8.48 across s015-s030 (Spearman rho=1.0)\\\", \\\"registry_id\\\": \\\"c2_n500_deepseek\\\", \\\"role\\\": \\\"primary\\\", \\\"priority\\\": \\\"high\\\", \\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"n_problems\\\": 500, \\\"effective_n\\\": 496, \\\"mid_null_rate\\\": 0.102, \\\"imp_s015_median_ii\\\": 0.3907, \\\"imp_s015_ci\\\": [0.3496, 0.4431], \\\"imp_s015_wilcoxon_p\\\": 1.27e-70, \\\"imp_s020_median_ii\\\": 1.2149, \\\"imp_s020_ci\\\": [1.1072, 1.3365], \\\"imp_s020_wilcoxon_p\\\": 3.98e-75, \\\"imp_s025_median_ii\\\": 3.9857, \\\"imp_s025_ci\\\": [3.5272, 4.3588], \\\"imp_s025_wilcoxon_p\\\": 1.99e-78, \\\"imp_s030_median_ii\\\": 8.4813, \\\"imp_s030_ci\\\": [7.7543, 9.6919], \\\"imp_s030_wilcoxon_p\\\": 1.09e-79, \\\"rand_s015_median_ii\\\": 0.0139, \\\"rand_s015_wilcoxon_p\\\": 0.863, \\\"rand_s020_median_ii\\\": 0.0315, \\\"rand_s020_wilcoxon_p\\\": 0.28, \\\"rand_s025_median_ii\\\": 0.2574, \\\"rand_s025_bonf_p\\\": 0.005839, \\\"rand_s025_fdr_p\\\": 0.001914, \\\"rand_s030_median_ii\\\": 0.5096, \\\"rand_s030_bonf_p\\\": 0.005903, \\\"rand_s030_fdr_p\\\": 0.001914, \\\"dz_s015_s020\\\": -0.925, \\\"dz_s020_s025\\\": -0.824, \\\"dz_s025_s030\\\": -0.773, \\\"dz_s015_s030\\\": -0.944, \\\"all_dz_reliable\\\": true, \\\"dose_response_monotonic\\\": true, \\\"dose_response_spearman_rho\\\": 1, \\\"dose_response_perm_p\\\": 0.0417, \\\"imp_rand_ratio_range\\\": \\\"15.5-38.6x\\\", \\\"bonferroni_k\\\": 4, \\\"bonferroni_note\\\": \\\"Bonferroni k=4 family-wise (D066 revision)\\\"}}, {\\\"id\\\": \\\"s7_c_c2_qw_n500_r3\\\", \\\"claim\\\": \\\"S7->C\\\", \\\"description\\\": \\\"QW n=500 monotonic: imp median II 0.066->0.307->1.075->4.33 across s015-s030 (Spearman rho=1.0)\\\", \\\"registry_id\\\": \\\"c2_qw_n500_r3\\\", \\\"role\\\": \\\"primary\\\", \\\"priority\\\": \\\"high\\\", \\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"n_problems\\\": 500, \\\"effective_n\\\": 475, \\\"filter\\\": \\\"low+high valid only (mid-null allowed)\\\", \\\"mid_null_rate\\\": 0.452, \\\"imp_s015_median_ii\\\": 0.0659, \\\"imp_s015_ci\\\": [0.0492, 0.0925], \\\"imp_s015_wilcoxon_p\\\": 8.66e-15, \\\"imp_s015_bonf_p\\\": 3.46e-14, \\\"imp_s020_median_ii\\\": 0.3073, \\\"imp_s020_ci\\\": [0.2612, 0.3564], \\\"imp_s020_wilcoxon_p\\\": 6.84e-42, \\\"imp_s020_bonf_p\\\": 2.74e-41, \\\"imp_s025_median_ii\\\": 1.0745, \\\"imp_s025_ci\\\": [0.9766, 1.1787], \\\"imp_s025_wilcoxon_p\\\": 1.06e-68, \\\"imp_s025_bonf_p\\\": 4.25e-68, \\\"imp_s030_median_ii\\\": 3.155, \\\"imp_s030_ci\\\": [2.7834, 3.5582], \\\"imp_s030_wilcoxon_p\\\": 9.21e-74, \\\"imp_s030_bonf_p\\\": 3.69e-73, \\\"rand_s015_median_ii\\\": -0.0111, \\\"rand_s015_wilcoxon_p\\\": 0.172, \\\"rand_s015_bonf_p\\\": 0.687, \\\"rand_s020_median_ii\\\": 0.0153, \\\"rand_s020_wilcoxon_p\\\": 0.2, \\\"rand_s020_bonf_p\\\": 0.8, \\\"rand_s025_median_ii\\\": 0.3931, \\\"rand_s025_wilcoxon_p\\\": 1.59e-11, \\\"rand_s025_bonf_p\\\": 6.37e-11, \\\"rand_s025_fdr_p\\\": 2.63e-11, \\\"rand_s030_median_ii\\\": 0.9127, \\\"rand_s030_wilcoxon_p\\\": 2.92e-15, \\\"rand_s030_bonf_p\\\": 1.17e-14, \\\"rand_s030_fdr_p\\\": 5.61e-15, \\\"dz_s015_s020\\\": -0.629, \\\"dz_s020_s025\\\": -0.865, \\\"dz_s025_s030\\\": -0.767, \\\"dz_s015_s030\\\": -0.923, \\\"all_dz_reliable\\\": true, \\\"dose_response_monotonic\\\": true, \\\"dose_response_spearman_rho\\\": 1, \\\"dose_response_perm_p\\\": 0.0417, \\\"imp_rand_ratio_range\\\": \\\"2.7-20.1x\\\", \\\"bonferroni_k\\\": 4, \\\"bonferroni_note\\\": \\\"Bonferroni k=4 family-wise (D066 revision)\\\"}}, {\\\"id\\\": \\\"s7_c_bf16_qw_imp_s035\\\", \\\"claim\\\": \\\"S7->C\\\", \\\"description\\\": \\\"QW s=0.35: low_II_median=8.24; extends dose-response beyond s030\\\", \\\"registry_id\\\": \\\"bf16_qw_imp_s035\\\", \\\"role\\\": \\\"supporting\\\", \\\"priority\\\": \\\"medium\\\", \\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"n_problems\\\": 50, \\\"overall_verdict\\\": \\\"PASS\\\", \\\"ci_overlap_test\\\": \\\"PASS\\\", \\\"sign_reversal_test\\\": \\\"FAIL\\\", \\\"high_sparsity_II_median\\\": 0.0232, \\\"high_sparsity_II_median_CI\\\": [0.0154, 0.0383], \\\"high_sparsity_II_mean\\\": 0.1643, \\\"high_sparsity_II_mean_CI\\\": [0.0844, 0.2495], \\\"low_sparsity_II_median\\\": 8.2358, \\\"low_sparsity_II_median_CI\\\": [6.1564, 10.9231], \\\"low_sparsity_II_mean\\\": 18.9673, \\\"low_sparsity_II_mean_CI\\\": [14.5015, 23.9752], \\\"mid_sparsity_II_median\\\": 0.9577, \\\"mid_sparsity_II_median_CI\\\": [0.171, 3.5575], \\\"mid_sparsity_II_mean\\\": 8.0734, \\\"mid_sparsity_II_mean_CI\\\": [2.0224, 16.8946], \\\"ppl_high_dense\\\": 1.0738, \\\"ppl_high_both\\\": 2.3435, \\\"ppl_low_dense\\\": 1.1518, \\\"ppl_low_both\\\": 58.0358, \\\"ppl_mid_dense\\\": 1.1327, \\\"ppl_mid_both\\\": 20.9912, \\\"high_sparsity_tokens\\\": 16289, \\\"low_sparsity_tokens\\\": 32227, \\\"mid_sparsity_tokens\\\": 4372}}], \\\"total\\\": 38}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": [{\"id\": \"c1_bf16_importance_s025\", \"claim\": \"C1\", \"description\": \"II median: high=0.032, mid=1.118, low=7.196; importance masking shows strong phase gradient\", \"registry_id\": \"bf16_importance_s025\", \"role\": \"primary\", \"priority\": \"high\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"interaction_index\": {\"high\": {\"mean\": 0.302756, \"median\": 0.032363, \"ci\": [0.083714, 0.543977], \"winsorized_mean\": 0.200962, \"skewness\": 4.8826}, \"mid\": {\"mean\": 5.729665, \"median\": 1.118069, \"ci\": [3.455574, 8.471799], \"winsorized_mean\": 4.189902, \"skewness\": 8.2799}, \"low\": {\"mean\": 25.852951, \"median\": 7.195958, \"ci\": [19.077082, 33.497293], \"winsorized_mean\": 19.319103, \"skewness\": 7.3986}}, \"per_problem_ii_stats\": {\"high\": {\"n\": 49, \"min\": -0.316321, \"max\": 4.003714, \"mean\": 0.133714, \"median\": 0.009873, \"std\": 0.595358}, \"mid\": {\"n\": 40, \"min\": -0.024794, \"max\": 18.720486, \"mean\": 2.537744, \"median\": 1.05707, \"std\": 3.962575}, \"low\": {\"n\": 50, \"min\": -1.854733, \"max\": 75.467653, \"mean\": 11.28281, \"median\": 3.954593, \"std\": 16.620011}}, \"gradient_paired_aggregate_legacy\": 222.35, \"median_difference\": 7.1636, \"n_problems\": 50, \"pass_fail\": {\"ci_overlap\": true, \"sign_reversal\": false, \"overall\": \"PASS\"}, \"phase_stats\": {\"high\": {\"n_tokens\": 21086, \"n_segments\": 387}, \"mid\": {\"n_tokens\": 13306, \"n_segments\": 191}, \"low\": {\"n_tokens\": 27748, \"n_segments\": 397}}, \"perplexity\": {\"high\": {\"dense\": 1.1689, \"attn\": 1.6511, \"kv\": 1.8628, \"both\": 2.7026}, \"mid\": {\"dense\": 1.2269, \"attn\": 1.7039, \"kv\": 5.6205, \"both\": 13.3436}, \"low\": {\"dense\": 1.2286, \"attn\": 1.8366, \"kv\": 31.756, \"both\": 63.668}}}}, {\"id\": \"c1_bf16_ds_rand_s025\", \"claim\": \"C1\", \"description\": \"Random II median: high=0.818, mid=0.932, low=1.363; flat gradient vs importance\", \"registry_id\": \"bf16_ds_rand_s025\", \"role\": \"primary\", \"priority\": \"high\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"interaction_index\": {\"high\": {\"mean\": 3.59, \"median\": 0.8182, \"ci\": [1.4021, 6.2327], \"median_ci\": [0.5075, 1.7217], \"winsorized_mean\": 6.3965, \"skewness\": -7.57}, \"mid\": {\"mean\": -1.8455, \"median\": 0.9324, \"ci\": [-10.3663, 4.9342], \"median_ci\": [0.7331, 1.7003], \"winsorized_mean\": 3.1014, \"skewness\": -12.76}, \"low\": {\"mean\": 0.7212, \"median\": 1.3627, \"ci\": [-4.2068, 4.5006], \"median_ci\": [1.0869, 2.6866], \"winsorized_mean\": 4.1866, \"skewness\": -15.85}}, \"perplexity\": {\"high\": {\"dense\": 1.1687, \"attn\": 7.237, \"kv\": 4.9751, \"both\": 17.7423}, \"mid\": {\"dense\": 1.2269, \"attn\": 868.3199, \"kv\": 5.1165, \"both\": 29.4661}, \"low\": {\"dense\": 1.2284, \"attn\": 24.3571, \"kv\": 6.7993, \"both\": 17.9694}}, \"phase_stats\": {\"high\": {\"n_tokens\": 21086, \"n_segments\": 387}, \"mid\": {\"n_tokens\": 13306, \"n_segments\": 191}, \"low\": {\"n_tokens\": 27748, \"n_segments\": 397}}, \"n_problems\": 50, \"pass_fail\": {\"ci_overlap\": false, \"sign_reversal\": false, \"overall\": \"FAIL\"}, \"median_difference\": 0.5445}}, {\"id\": \"c1_bf16_qw_imp_s025\", \"claim\": \"C1\", \"description\": \"Qwen cross-model: median_diff=1.109, Cohen's d=1.233, p<1e-5\", \"registry_id\": \"bf16_qw_imp_s025\", \"role\": \"supporting\", \"priority\": \"medium\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"median_difference\": 1.108706, \"permutation_p\": 0, \"cohens_d\": 1.2329, \"bootstrap_ci_95\": [0.609247, 1.469002], \"wilcoxon_p\": 0, \"n_bootstrap\": 10000, \"n_paired\": 46}}, {\"id\": \"c1_sf5_asymmetric_spot\", \"claim\": \"C1\", \"description\": \"Asymmetric configs: h02_kv03 D=19.13, h03_kv02 D=18.25; gradient consistent\", \"registry_id\": \"sf5_asymmetric_spot\", \"role\": \"ablation\", \"priority\": \"medium\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"config_a_h02_kv03\": {\"II_low\": 19.51, \"II_mid\": 6.05, \"II_high\": 0.38, \"D\": 19.13}, \"config_b_h03_kv02\": {\"II_low\": 18.77, \"II_mid\": 3.97, \"II_high\": 0.52, \"D\": 18.25}, \"pre_registered_criterion_passed\": true, \"gradient_direction\": \"II_low >> II_mid >> II_high (consistent with symmetric baseline)\"}}, {\"id\": \"c1_c2_accuracy_eval\", \"claim\": \"C1\", \"description\": \"DS dense->s030 acc: 0.52->0.10 (-0.42); QW dense->s030: 0.32->0.14 (-0.18)\", \"registry_id\": \"c2_accuracy_eval\", \"role\": \"supporting\", \"priority\": \"medium\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"n_problems\": 50, \"ds_dense_acc\": 0.52, \"ds_s015_acc\": 0.36, \"ds_s015_delta\": -0.16, \"ds_s030_acc\": 0.1, \"ds_s030_delta\": -0.42, \"qw_dense_acc\": 0.32, \"qw_s015_acc\": 0.34, \"qw_s015_delta\": 0.02, \"qw_s030_acc\": 0.14, \"qw_s030_delta\": -0.18, \"ds_s030_chinese_reasoning_rate\": 0.4, \"ds_dense_truncation_rate\": 0.56, \"note\": \"v2 rescored with fixed radical+degree matcher. DS s015 34→36, QW s015 32→34\"}}, {\"id\": \"c2_bf16_importance_s030\", \"claim\": \"C2\", \"description\": \"Phase gradient: II low=14.64 >> mid=2.28 >> high=0.053 (median); low/high ratio ~276x\", \"registry_id\": \"bf16_importance_s030\", \"role\": \"primary\", \"priority\": \"high\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"interaction_index\": {\"high\": {\"mean\": 0.5547, \"median\": 0.0534, \"ci\": [0.2773, 0.9198], \"winsorized_mean\": 0.3367, \"skewness\": 10.62}, \"mid\": {\"mean\": 11.3, \"median\": 2.2833, \"ci\": [6.865, 17.2633], \"winsorized_mean\": 8.1752, \"skewness\": 9.19}, \"low\": {\"mean\": 57.7946, \"median\": 14.6395, \"ci\": [41.4416, 77.0467], \"winsorized_mean\": 39.3143, \"skewness\": 8.31}}, \"per_problem_ii_stats\": {\"high\": {\"n\": 49, \"min\": -0.5095, \"max\": 4.4457, \"mean\": 0.1976, \"median\": 0.0343, \"std\": 0.6793}, \"mid\": {\"n\": 40, \"min\": -0.1989, \"max\": 34.0258, \"mean\": 5.2585, \"median\": 1.5173, \"std\": 7.9382}, \"low\": {\"n\": 50, \"min\": -7.3027, \"max\": 126.7985, \"mean\": 22.6601, \"median\": 9.9731, \"std\": 28.4096}}, \"gradient_paired_aggregate_legacy\": 57.24, \"median_difference\": 14.5861, \"n_problems\": 50, \"pass_fail\": {\"ci_overlap\": true, \"sign_reversal\": false, \"overall\": \"PASS\"}, \"phase_stats\": {\"high\": {\"n_tokens\": 21086, \"n_segments\": 387}, \"mid\": {\"n_tokens\": 13306, \"n_segments\": 191}, \"low\": {\"n_tokens\": 27748, \"n_segments\": 397}}, \"perplexity\": {\"high\": {\"dense\": 1.1689, \"attn\": 1.7123, \"kv\": 2.0544, \"both\": 3.2372}, \"mid\": {\"dense\": 1.2269, \"attn\": 1.7894, \"kv\": 9.4821, \"both\": 24.2847}, \"low\": {\"dense\": 1.2286, \"attn\": 1.9347, \"kv\": 51.6485, \"both\": 122.61}}}}, {\"id\": \"c2_v6_importance_s030\", \"claim\": \"C2\", \"description\": \"II low_median=34.69, mid_median=7.27, high_median=0.88; bootstrap_gradient=41.92, CI=[19.14,299.76]\", \"registry_id\": \"v6_importance_s030\", \"role\": \"primary\", \"priority\": \"high\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"ii_high_median\": 0.8833, \"ii_mid_median\": 7.2706, \"ii_low_median\": 34.6937, \"ii_high_mean\": 1.5151, \"ii_mid_mean\": 78.8215, \"ii_low_mean\": 1163.9677, \"per_problem_ii_count\": 50, \"n_high\": 40, \"n_mid\": 22, \"n_low\": 20, \"problems\": 50, \"bootstrap_gradient_paired\": 41.92, \"bootstrap_ci_paired\": [19.14, 299.76], \"bootstrap_gradient_unpaired\": 39.28, \"bootstrap_ci_unpaired\": [21.87, 129.59], \"bootstrap_p\": 0}}, {\"id\": \"c2_think_phase_validation\", \"claim\": \"C2\", \"description\": \"Phase segmentation kappa=0.887; thinking=57.8% low-sparsity, answer=62.7% high-sparsity\", \"registry_id\": \"think_phase_validation\", \"role\": \"supporting\", \"priority\": \"medium\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"effective_n\": 48, \"skipped_problems\": 2, \"median_kappa\": 0.887, \"thinking_in_low_sparsity_phase\": 0.578, \"answer_in_high_sparsity_phase\": 0.627, \"note\": \"Phase segmentation based on dense model — 4 sparsity conditions share identical phase boundaries, effective sample n=48 not n=192\"}}, {\"id\": \"c2_acc_qw_s030_n100\", \"claim\": \"C2\", \"description\": \"QW importance s030 accuracy=0.19 (n=100); dose-response monotonic decline from dense=0.40\", \"registry_id\": \"acc_qw_s030_n100\", \"role\": \"supporting\", \"priority\": \"medium\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"batch1_correct\": 7, \"batch1_total\": 50, \"batch1_acc\": 0.14, \"batch1_source\": \"acc_qw_s030_b1_8k (v2, 8k tokens)\", \"batch2_correct\": 12, \"batch2_total\": 50, \"batch2_acc\": 0.24, \"combined_correct\": 19, \"combined_total\": 100, \"combined_acc\": 0.19}}, {\"id\": \"c2_acc_ds_s015_8k_v2\", \"claim\": \"C2\", \"description\": \"DS s015 accuracy=0.48 vs dense=0.74; early onset of compound degradation\", \"registry_id\": \"acc_ds_s015_8k_v2\", \"role\": \"supporting\", \"priority\": \"medium\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 0.48, \"correct\": 24, \"total\": 50, \"truncation_rate\": 0.32, \"truncated_count\": 16, \"non_truncated_accuracy\": 0.706, \"non_truncated_correct\": 24, \"non_truncated_total\": 34, \"wall_time_s\": 3967, \"max_new_tokens\": 8192}}, {\"id\": \"c3_v6_importance_s025\", \"claim\": \"C3\", \"description\": \"Importance: II low_median=24.16 >> high_median=0.66; strong phase gradient (36x ratio)\", \"registry_id\": \"v6_importance_s025\", \"role\": \"primary\", \"priority\": \"high\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"ii_high_median\": 0.6641, \"ii_mid_median\": 5.3067, \"ii_low_median\": 24.1619, \"ii_high_mean\": 0.8842, \"ii_mid_mean\": 10.057, \"ii_low_mean\": 71.8854, \"per_problem_ii_count\": 50, \"n_high\": 42, \"n_mid\": 23, \"n_low\": 21, \"problems\": 50, \"bootstrap_gradient_paired\": 35.72, \"bootstrap_ci_paired\": [9.52, 101.54], \"bootstrap_gradient_unpaired\": 36.38, \"bootstrap_ci_unpaired\": [13.19, 97.61], \"bootstrap_p\": 0}}, {\"id\": \"c3_v6_random_s025\", \"claim\": \"C3\", \"description\": \"Random: II low_median=2.91 ~ high_median=3.00; flat phase gradient (bootstrap_p=0.559)\", \"registry_id\": \"v6_random_s025\", \"role\": \"primary\", \"priority\": \"high\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"ii_high_median\": 3.0024, \"ii_mid_median\": 2.9846, \"ii_low_median\": 2.9146, \"ii_high_mean\": 3.9052, \"ii_mid_mean\": 7.9491, \"ii_low_mean\": 3.9114, \"per_problem_ii_count\": 50, \"n_high\": 36, \"n_mid\": 25, \"n_low\": 24, \"bootstrap_gradient_paired\": -0.1199, \"bootstrap_ci_paired\": [-1.517, 1.2461], \"bootstrap_p\": 0.559, \"bootstrap_gradient_unpaired\": -0.8616, \"bootstrap_ci_unpaired\": [-3.3911, 1.5169], \"per_problem_ii_stats\": {\"high\": {\"min\": -6.1388, \"max\": 25.2471, \"mean\": 4.4098, \"median\": 3.0421, \"std\": 6.0734}, \"mid\": {\"min\": 0.158, \"max\": 108.7242, \"mean\": 7.5626, \"median\": 2.1407, \"std\": 20.926}, \"low\": {\"min\": -0.1953, \"max\": 12.8555, \"mean\": 3.5806, \"median\": 2.7289, \"std\": 3.4915}}, \"verdict\": \"FAIL\"}}, {\"id\": \"c3_bf16_importance_s020\", \"claim\": \"C3\", \"description\": \"Importance: II low=1.50, mid=0.20, high=0.015 (median); clear phase separation\", \"registry_id\": \"bf16_importance_s020\", \"role\": \"supporting\", \"priority\": \"medium\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"interaction_index\": {\"high\": {\"mean\": 0.1289, \"median\": 0.0145, \"ci\": [-0.1975, 0.6647], \"winsorized_mean\": -0.0297, \"skewness\": 16.67}, \"mid\": {\"mean\": 1.2604, \"median\": 0.2027, \"ci\": [0.7466, 1.8962], \"winsorized_mean\": 0.766, \"skewness\": 7.05}, \"low\": {\"mean\": 6.0288, \"median\": 1.4963, \"ci\": [4.4671, 7.9237], \"winsorized_mean\": 4.3426, \"skewness\": 6.01}}, \"per_problem_ii_stats\": {\"high\": {\"n\": 49, \"min\": -0.1884, \"max\": 0.4196, \"mean\": 0.0025, \"median\": 0.0036, \"std\": 0.0966}, \"mid\": {\"n\": 40, \"min\": -0.0519, \"max\": 8.6969, \"mean\": 0.6795, \"median\": 0.1977, \"std\": 1.4998}, \"low\": {\"n\": 50, \"min\": -1.6151, \"max\": 22.6875, \"mean\": 2.2301, \"median\": 1.128, \"std\": 4.3758}}, \"gradient_paired_aggregate_legacy\": 5.9, \"median_difference\": 1.4818, \"n_problems\": 50, \"pass_fail\": {\"ci_overlap\": true, \"sign_reversal\": false, \"overall\": \"PASS\"}, \"phase_stats\": {\"high\": {\"n_tokens\": 21086, \"n_segments\": 387}, \"mid\": {\"n_tokens\": 13306, \"n_segments\": 191}, \"low\": {\"n_tokens\": 27748, \"n_segments\": 397}}, \"perplexity\": {\"high\": {\"dense\": 1.1689, \"attn\": 1.5233, \"kv\": 1.6191, \"both\": 2.1047}, \"mid\": {\"dense\": 1.2269, \"attn\": 1.5375, \"kv\": 3.5164, \"both\": 5.4246}, \"low\": {\"dense\": 1.2286, \"attn\": 1.6486, \"kv\": 15.7987, \"both\": 23.74}}}}, {\"id\": \"c3_bf16_ds_rand_s020\", \"claim\": \"C3\", \"description\": \"Random: II high=0.292, mid=0.350, low=0.276 (median); no phase separation\", \"registry_id\": \"bf16_ds_rand_s020\", \"role\": \"supporting\", \"priority\": \"medium\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"interaction_index\": {\"high\": {\"mean\": 1.1216, \"median\": 0.2918, \"ci\": [0.0796, 2.5834], \"median_ci\": [0.1598, 0.4581], \"winsorized_mean\": 1.7664, \"skewness\": 9.59}, \"mid\": {\"mean\": -1.5827, \"median\": 0.3504, \"ci\": [-6.0963, 1.5735], \"median_ci\": [0.1993, 0.5226], \"winsorized_mean\": 0.5839, \"skewness\": -12.31}, \"low\": {\"mean\": -0.4116, \"median\": 0.2763, \"ci\": [-2.6034, 1.209], \"median_ci\": [0.2194, 0.5487], \"winsorized_mean\": 0.9942, \"skewness\": -10.07}}, \"perplexity\": {\"high\": {\"dense\": 1.1687, \"attn\": 3.1905, \"kv\": 3.8002, \"both\": 8.8129}, \"mid\": {\"dense\": 1.2269, \"attn\": 67.8504, \"kv\": 3.788, \"both\": 11.4974}, \"low\": {\"dense\": 1.2284, \"attn\": 8.592, \"kv\": 5.0078, \"both\": 9.2001}}, \"phase_stats\": {\"high\": {\"n_tokens\": 21086, \"n_segments\": 387}, \"mid\": {\"n_tokens\": 13306, \"n_segments\": 191}, \"low\": {\"n_tokens\": 27748, \"n_segments\": 397}}, \"n_problems\": 50, \"pass_fail\": {\"ci_overlap\": false, \"sign_reversal\": false, \"overall\": \"FAIL\"}, \"median_difference\": -0.0155}}, {\"id\": \"c4_c4_entropy\", \"claim\": \"C4\", \"description\": \"DS importance entropy_delta: -0.04 to -0.05 (collapse); random: +0.13 to +0.23 (redistribution). Gini_delta: -0.03 to -0.08\", \"registry_id\": \"c4_entropy\", \"role\": \"primary\", \"priority\": \"high\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"importance_entropy_delta\": {\"s015\": -0.0402, \"s020\": -0.0472, \"s025\": -0.0446, \"s030\": -0.0436}, \"random_entropy_delta\": {\"s015\": 0.1283, \"s020\": 0.136, \"s025\": 0.2171, \"s030\": 0.2327}, \"importance_gini_delta\": {\"s015\": -0.0301, \"s020\": -0.0404, \"s025\": -0.0647, \"s030\": -0.0806}, \"random_gini_delta\": {\"s015\": -0.0309, \"s020\": -0.0403, \"s025\": -0.062, \"s030\": -0.0732}, \"importance_cv_delta\": {\"s015\": -0.564, \"s020\": -0.774, \"s025\": -1.287, \"s030\": -1.665}, \"random_cv_delta\": {\"s015\": -1.021, \"s020\": -1.203, \"s025\": -1.923, \"s030\": -2.137}, \"problems_completed\": 30, \"runtime_minutes\": 69.1}}, {\"id\": \"c4_qwen_c4_entropy\", \"claim\": \"C4\", \"description\": \"QW importance entropy_delta mixed: s015=-0.073, s025=+0.045; Gini weaker (-0.01 to -0.02). Model-dependent pattern\", \"registry_id\": \"qwen_c4_entropy\", \"role\": \"primary\", \"priority\": \"high\", \"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"problems_completed\": 30, \"qwen_importance_entropy_delta\": {\"s015\": -0.0733, \"s020\": -0.0759, \"s025\": 0.0451, \"s030\": -0.0072}, \"qwen_random_entropy_delta\": {\"s015\": 0.0838, \"s020\": 0.0901, \"s025\": 0.2168, \"s030\": 0.1968}, \"qwen_importance_gini_delta\": {\"s015\": -0.0103, \"s020\": -0.0121, \"s025\": -0.01, \"s030\": -0.0202}, \"qwen_random_gini_delta\": {\"s015\": -0.0186, \"s020\": -0.0229, \"s025\": -0.0337, \"s030\": -0.0448}, \"qwen_importance_cv_delta\": {\"s015\": -0.045, \"s020\": -0.208, \"s025\": -1.491, \"s030\": -1.142}, \"qwen_random_cv_delta\": {\"s015\": -0.778, \"s020\": -0.889, \"s025\": -1.5, \"s030\": -1.677}, \"cross_model_notes\": \"random entropy increase consistent; importance entropy collapse inconsistent at s025 (reversed to +0.045) and near-zero at s030; gini/cv directions consistent but Qwen magnitudes smaller\"}}, {\"id\": \"c5_bf16_qw_imp_s030\", \"claim\": \"C5\", \"description\": \"Qwen: median_diff=2.619, Cohen's d=1.439, p<1e-5; replicates DeepSeek pattern\", \"registry_id\": \"bf16_qw_imp_s030\", \"role\": \"primary\", \"priority\": \"high\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"median_difference\": 2.619385, \"permutation_p\": 0, \"cohens_d\": 1.4394, \"bootstrap_ci_95\": [1.722281, 3.651063], \"wilcoxon_p\": 0, \"n_bootstrap\": 10000, \"n_paired\": 46}}, {\"id\": \"c5_bf16_importance_s030\", \"claim\": \"C5\", \"description\": \"DeepSeek: II low_median=14.64, high_median=0.053; strong phase gradient\", \"registry_id\": \"bf16_importance_s030\", \"role\": \"primary\", \"priority\": \"high\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"interaction_index\": {\"high\": {\"mean\": 0.5547, \"median\": 0.0534, \"ci\": [0.2773, 0.9198], \"winsorized_mean\": 0.3367, \"skewness\": 10.62}, \"mid\": {\"mean\": 11.3, \"median\": 2.2833, \"ci\": [6.865, 17.2633], \"winsorized_mean\": 8.1752, \"skewness\": 9.19}, \"low\": {\"mean\": 57.7946, \"median\": 14.6395, \"ci\": [41.4416, 77.0467], \"winsorized_mean\": 39.3143, \"skewness\": 8.31}}, \"per_problem_ii_stats\": {\"high\": {\"n\": 49, \"min\": -0.5095, \"max\": 4.4457, \"mean\": 0.1976, \"median\": 0.0343, \"std\": 0.6793}, \"mid\": {\"n\": 40, \"min\": -0.1989, \"max\": 34.0258, \"mean\": 5.2585, \"median\": 1.5173, \"std\": 7.9382}, \"low\": {\"n\": 50, \"min\": -7.3027, \"max\": 126.7985, \"mean\": 22.6601, \"median\": 9.9731, \"std\": 28.4096}}, \"gradient_paired_aggregate_legacy\": 57.24, \"median_difference\": 14.5861, \"n_problems\": 50, \"pass_fail\": {\"ci_overlap\": true, \"sign_reversal\": false, \"overall\": \"PASS\"}, \"phase_stats\": {\"high\": {\"n_tokens\": 21086, \"n_segments\": 387}, \"mid\": {\"n_tokens\": 13306, \"n_segments\": 191}, \"low\": {\"n_tokens\": 27748, \"n_segments\": 397}}, \"perplexity\": {\"high\": {\"dense\": 1.1689, \"attn\": 1.7123, \"kv\": 2.0544, \"both\": 3.2372}, \"mid\": {\"dense\": 1.2269, \"attn\": 1.7894, \"kv\": 9.4821, \"both\": 24.2847}, \"low\": {\"dense\": 1.2286, \"attn\": 1.9347, \"kv\": 51.6485, \"both\": 122.61}}}}, {\"id\": \"c5_c2_n500_deepseek\", \"claim\": \"C5\", \"description\": \"DS n=500: imp_s030 median_II=8.48, CI=[7.46,9.56], p=1.3e-78; robust at scale\", \"registry_id\": \"c2_n500_deepseek\", \"role\": \"supporting\", \"priority\": \"medium\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"n_problems\": 500, \"effective_n\": 496, \"mid_null_rate\": 0.102, \"imp_s015_median_ii\": 0.3907, \"imp_s015_ci\": [0.3496, 0.4431], \"imp_s015_wilcoxon_p\": 1.27e-70, \"imp_s020_median_ii\": 1.2149, \"imp_s020_ci\": [1.1072, 1.3365], \"imp_s020_wilcoxon_p\": 3.98e-75, \"imp_s025_median_ii\": 3.9857, \"imp_s025_ci\": [3.5272, 4.3588], \"imp_s025_wilcoxon_p\": 1.99e-78, \"imp_s030_median_ii\": 8.4813, \"imp_s030_ci\": [7.7543, 9.6919], \"imp_s030_wilcoxon_p\": 1.09e-79, \"rand_s015_median_ii\": 0.0139, \"rand_s015_wilcoxon_p\": 0.863, \"rand_s020_median_ii\": 0.0315, \"rand_s020_wilcoxon_p\": 0.28, \"rand_s025_median_ii\": 0.2574, \"rand_s025_bonf_p\": 0.005839, \"rand_s025_fdr_p\": 0.001914, \"rand_s030_median_ii\": 0.5096, \"rand_s030_bonf_p\": 0.005903, \"rand_s030_fdr_p\": 0.001914, \"dz_s015_s020\": -0.925, \"dz_s020_s025\": -0.824, \"dz_s025_s030\": -0.773, \"dz_s015_s030\": -0.944, \"all_dz_reliable\": true, \"dose_response_monotonic\": true, \"dose_response_spearman_rho\": 1, \"dose_response_perm_p\": 0.0417, \"imp_rand_ratio_range\": \"15.5-38.6x\", \"bonferroni_k\": 4, \"bonferroni_note\": \"Bonferroni k=4 family-wise (D066 revision)\"}}, {\"id\": \"c5_c2_qw_n500_r3\", \"claim\": \"C5\", \"description\": \"QW n=500: imp_s030 median_II=4.33, p<1e-40; cross-model replication at high power\", \"registry_id\": \"c2_qw_n500_r3\", \"role\": \"supporting\", \"priority\": \"medium\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"n_problems\": 500, \"effective_n\": 475, \"filter\": \"low+high valid only (mid-null allowed)\", \"mid_null_rate\": 0.452, \"imp_s015_median_ii\": 0.0659, \"imp_s015_ci\": [0.0492, 0.0925], \"imp_s015_wilcoxon_p\": 8.66e-15, \"imp_s015_bonf_p\": 3.46e-14, \"imp_s020_median_ii\": 0.3073, \"imp_s020_ci\": [0.2612, 0.3564], \"imp_s020_wilcoxon_p\": 6.84e-42, \"imp_s020_bonf_p\": 2.74e-41, \"imp_s025_median_ii\": 1.0745, \"imp_s025_ci\": [0.9766, 1.1787], \"imp_s025_wilcoxon_p\": 1.06e-68, \"imp_s025_bonf_p\": 4.25e-68, \"imp_s030_median_ii\": 3.155, \"imp_s030_ci\": [2.7834, 3.5582], \"imp_s030_wilcoxon_p\": 9.21e-74, \"imp_s030_bonf_p\": 3.69e-73, \"rand_s015_median_ii\": -0.0111, \"rand_s015_wilcoxon_p\": 0.172, \"rand_s015_bonf_p\": 0.687, \"rand_s020_median_ii\": 0.0153, \"rand_s020_wilcoxon_p\": 0.2, \"rand_s020_bonf_p\": 0.8, \"rand_s025_median_ii\": 0.3931, \"rand_s025_wilcoxon_p\": 1.59e-11, \"rand_s025_bonf_p\": 6.37e-11, \"rand_s025_fdr_p\": 2.63e-11, \"rand_s030_median_ii\": 0.9127, \"rand_s030_wilcoxon_p\": 2.92e-15, \"rand_s030_bonf_p\": 1.17e-14, \"rand_s030_fdr_p\": 5.61e-15, \"dz_s015_s020\": -0.629, \"dz_s020_s025\": -0.865, \"dz_s025_s030\": -0.767, \"dz_s015_s030\": -0.923, \"all_dz_reliable\": true, \"dose_response_monotonic\": true, \"dose_response_spearman_rho\": 1, \"dose_response_perm_p\": 0.0417, \"imp_rand_ratio_range\": \"2.7-20.1x\", \"bonferroni_k\": 4, \"bonferroni_note\": \"Bonferroni k=4 family-wise (D066 revision)\"}}, {\"id\": \"c5b_c5b_pilot\", \"claim\": \"C5b\", \"description\": \"Oracle recovery=18% (gate: >30% FAIL); heuristic recovery=31.7% but CI crosses zero. s030 incomplete\", \"registry_id\": \"c5b_pilot\", \"role\": \"primary\", \"priority\": \"high\", \"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"s025_uniform_median_ii\": 1.0435, \"s025_oracle_median_ii\": 0.856, \"s025_oracle_recovery_pct\": 18, \"s025_oracle_recovery_ci\": [-39, 45.8], \"s025_oracle_wilcoxon_p\": 0.0021, \"s025_heuristic_median_ii\": 0.7127, \"s025_heuristic_recovery_pct\": 31.7, \"s025_heuristic_recovery_ci\": [-22.8, 66], \"s025_heuristic_wilcoxon_p\": 0.0236, \"gate_criterion\": \"oracle_recovery > 30%\", \"gate_result\": \"FAIL\", \"s030_status\": \"not_completed\", \"n_problems\": 30}}, {\"id\": \"c6_bf16_importance_s015\", \"claim\": \"C6\", \"description\": \"II low_median=0.398 at s=0.15\", \"registry_id\": \"bf16_importance_s015\", \"role\": \"primary\", \"priority\": \"high\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"interaction_index\": {\"high\": {\"mean\": -0.150213, \"median\": 0.005752, \"ci\": [-0.294614, -0.055385], \"winsorized_mean\": -0.062378, \"skewness\": -14.9912}, \"mid\": {\"mean\": 0.447301, \"median\": 0.080738, \"ci\": [0.267993, 0.668749], \"winsorized_mean\": 0.324751, \"skewness\": 4.7221}, \"low\": {\"mean\": 2.405837, \"median\": 0.398291, \"ci\": [1.478784, 3.667675], \"winsorized_mean\": 1.278857, \"skewness\": 9.5402}}, \"per_problem_ii_stats\": {\"high\": {\"n\": 49, \"min\": -0.188061, \"max\": 0.335853, \"mean\": -0.013405, \"median\": 0.00012, \"std\": 0.078483}, \"mid\": {\"n\": 40, \"min\": -0.169092, \"max\": 3.88198, \"mean\": 0.308621, \"median\": 0.107114, \"std\": 0.690186}, \"low\": {\"n\": 50, \"min\": -0.872983, \"max\": 9.10289, \"mean\": 0.725504, \"median\": 0.315517, \"std\": 1.731056}}, \"gradient_paired_aggregate_legacy\": 69.24, \"median_difference\": 0.3925, \"n_problems\": 50, \"pass_fail\": {\"ci_overlap\": true, \"sign_reversal\": true, \"overall\": \"PASS\"}, \"phase_stats\": {\"high\": {\"n_tokens\": 21086, \"n_segments\": 387}, \"mid\": {\"n_tokens\": 13306, \"n_segments\": 191}, \"low\": {\"n_tokens\": 27748, \"n_segments\": 397}}, \"perplexity\": {\"high\": {\"dense\": 1.1689, \"attn\": 1.4861, \"kv\": 1.4481, \"both\": 1.5911}, \"mid\": {\"dense\": 1.2269, \"attn\": 1.5137, \"kv\": 2.5971, \"both\": 3.4541}, \"low\": {\"dense\": 1.2286, \"attn\": 1.6147, \"kv\": 8.9201, \"both\": 12.5084}}}}, {\"id\": \"c6_bf16_importance_s020\", \"claim\": \"C6\", \"description\": \"II low_median=1.496 at s=0.20\", \"registry_id\": \"bf16_importance_s020\", \"role\": \"supporting\", \"priority\": \"medium\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"interaction_index\": {\"high\": {\"mean\": 0.1289, \"median\": 0.0145, \"ci\": [-0.1975, 0.6647], \"winsorized_mean\": -0.0297, \"skewness\": 16.67}, \"mid\": {\"mean\": 1.2604, \"median\": 0.2027, \"ci\": [0.7466, 1.8962], \"winsorized_mean\": 0.766, \"skewness\": 7.05}, \"low\": {\"mean\": 6.0288, \"median\": 1.4963, \"ci\": [4.4671, 7.9237], \"winsorized_mean\": 4.3426, \"skewness\": 6.01}}, \"per_problem_ii_stats\": {\"high\": {\"n\": 49, \"min\": -0.1884, \"max\": 0.4196, \"mean\": 0.0025, \"median\": 0.0036, \"std\": 0.0966}, \"mid\": {\"n\": 40, \"min\": -0.0519, \"max\": 8.6969, \"mean\": 0.6795, \"median\": 0.1977, \"std\": 1.4998}, \"low\": {\"n\": 50, \"min\": -1.6151, \"max\": 22.6875, \"mean\": 2.2301, \"median\": 1.128, \"std\": 4.3758}}, \"gradient_paired_aggregate_legacy\": 5.9, \"median_difference\": 1.4818, \"n_problems\": 50, \"pass_fail\": {\"ci_overlap\": true, \"sign_reversal\": false, \"overall\": \"PASS\"}, \"phase_stats\": {\"high\": {\"n_tokens\": 21086, \"n_segments\": 387}, \"mid\": {\"n_tokens\": 13306, \"n_segments\": 191}, \"low\": {\"n_tokens\": 27748, \"n_segments\": 397}}, \"perplexity\": {\"high\": {\"dense\": 1.1689, \"attn\": 1.5233, \"kv\": 1.6191, \"both\": 2.1047}, \"mid\": {\"dense\": 1.2269, \"attn\": 1.5375, \"kv\": 3.5164, \"both\": 5.4246}, \"low\": {\"dense\": 1.2286, \"attn\": 1.6486, \"kv\": 15.7987, \"both\": 23.74}}}}, {\"id\": \"c6_bf16_importance_s025\", \"claim\": \"C6\", \"description\": \"II low_median=7.196 at s=0.25\", \"registry_id\": \"bf16_importance_s025\", \"role\": \"supporting\", \"priority\": \"medium\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"interaction_index\": {\"high\": {\"mean\": 0.302756, \"median\": 0.032363, \"ci\": [0.083714, 0.543977], \"winsorized_mean\": 0.200962, \"skewness\": 4.8826}, \"mid\": {\"mean\": 5.729665, \"median\": 1.118069, \"ci\": [3.455574, 8.471799], \"winsorized_mean\": 4.189902, \"skewness\": 8.2799}, \"low\": {\"mean\": 25.852951, \"median\": 7.195958, \"ci\": [19.077082, 33.497293], \"winsorized_mean\": 19.319103, \"skewness\": 7.3986}}, \"per_problem_ii_stats\": {\"high\": {\"n\": 49, \"min\": -0.316321, \"max\": 4.003714, \"mean\": 0.133714, \"median\": 0.009873, \"std\": 0.595358}, \"mid\": {\"n\": 40, \"min\": -0.024794, \"max\": 18.720486, \"mean\": 2.537744, \"median\": 1.05707, \"std\": 3.962575}, \"low\": {\"n\": 50, \"min\": -1.854733, \"max\": 75.467653, \"mean\": 11.28281, \"median\": 3.954593, \"std\": 16.620011}}, \"gradient_paired_aggregate_legacy\": 222.35, \"median_difference\": 7.1636, \"n_problems\": 50, \"pass_fail\": {\"ci_overlap\": true, \"sign_reversal\": false, \"overall\": \"PASS\"}, \"phase_stats\": {\"high\": {\"n_tokens\": 21086, \"n_segments\": 387}, \"mid\": {\"n_tokens\": 13306, \"n_segments\": 191}, \"low\": {\"n_tokens\": 27748, \"n_segments\": 397}}, \"perplexity\": {\"high\": {\"dense\": 1.1689, \"attn\": 1.6511, \"kv\": 1.8628, \"both\": 2.7026}, \"mid\": {\"dense\": 1.2269, \"attn\": 1.7039, \"kv\": 5.6205, \"both\": 13.3436}, \"low\": {\"dense\": 1.2286, \"attn\": 1.8366, \"kv\": 31.756, \"both\": 63.668}}}}, {\"id\": \"c6_bf16_importance_s030\", \"claim\": \"C6\", \"description\": \"II low_median=14.64 at s=0.30; growth 0.40->1.50->7.20->14.64 is sub-exponential\", \"registry_id\": \"bf16_importance_s030\", \"role\": \"supporting\", \"priority\": \"medium\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"interaction_index\": {\"high\": {\"mean\": 0.5547, \"median\": 0.0534, \"ci\": [0.2773, 0.9198], \"winsorized_mean\": 0.3367, \"skewness\": 10.62}, \"mid\": {\"mean\": 11.3, \"median\": 2.2833, \"ci\": [6.865, 17.2633], \"winsorized_mean\": 8.1752, \"skewness\": 9.19}, \"low\": {\"mean\": 57.7946, \"median\": 14.6395, \"ci\": [41.4416, 77.0467], \"winsorized_mean\": 39.3143, \"skewness\": 8.31}}, \"per_problem_ii_stats\": {\"high\": {\"n\": 49, \"min\": -0.5095, \"max\": 4.4457, \"mean\": 0.1976, \"median\": 0.0343, \"std\": 0.6793}, \"mid\": {\"n\": 40, \"min\": -0.1989, \"max\": 34.0258, \"mean\": 5.2585, \"median\": 1.5173, \"std\": 7.9382}, \"low\": {\"n\": 50, \"min\": -7.3027, \"max\": 126.7985, \"mean\": 22.6601, \"median\": 9.9731, \"std\": 28.4096}}, \"gradient_paired_aggregate_legacy\": 57.24, \"median_difference\": 14.5861, \"n_problems\": 50, \"pass_fail\": {\"ci_overlap\": true, \"sign_reversal\": false, \"overall\": \"PASS\"}, \"phase_stats\": {\"high\": {\"n_tokens\": 21086, \"n_segments\": 387}, \"mid\": {\"n_tokens\": 13306, \"n_segments\": 191}, \"low\": {\"n_tokens\": 27748, \"n_segments\": 397}}, \"perplexity\": {\"high\": {\"dense\": 1.1689, \"attn\": 1.7123, \"kv\": 2.0544, \"both\": 3.2372}, \"mid\": {\"dense\": 1.2269, \"attn\": 1.7894, \"kv\": 9.4821, \"both\": 24.2847}, \"low\": {\"dense\": 1.2286, \"attn\": 1.9347, \"kv\": 51.6485, \"both\": 122.61}}}}, {\"id\": \"c7_c2_n500_deepseek\", \"claim\": \"C7\", \"description\": \"DS n=500: all 4 sparsities significant (p<1e-70); CIs non-overlapping across dose levels\", \"registry_id\": \"c2_n500_deepseek\", \"role\": \"primary\", \"priority\": \"high\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"n_problems\": 500, \"effective_n\": 496, \"mid_null_rate\": 0.102, \"imp_s015_median_ii\": 0.3907, \"imp_s015_ci\": [0.3496, 0.4431], \"imp_s015_wilcoxon_p\": 1.27e-70, \"imp_s020_median_ii\": 1.2149, \"imp_s020_ci\": [1.1072, 1.3365], \"imp_s020_wilcoxon_p\": 3.98e-75, \"imp_s025_median_ii\": 3.9857, \"imp_s025_ci\": [3.5272, 4.3588], \"imp_s025_wilcoxon_p\": 1.99e-78, \"imp_s030_median_ii\": 8.4813, \"imp_s030_ci\": [7.7543, 9.6919], \"imp_s030_wilcoxon_p\": 1.09e-79, \"rand_s015_median_ii\": 0.0139, \"rand_s015_wilcoxon_p\": 0.863, \"rand_s020_median_ii\": 0.0315, \"rand_s020_wilcoxon_p\": 0.28, \"rand_s025_median_ii\": 0.2574, \"rand_s025_bonf_p\": 0.005839, \"rand_s025_fdr_p\": 0.001914, \"rand_s030_median_ii\": 0.5096, \"rand_s030_bonf_p\": 0.005903, \"rand_s030_fdr_p\": 0.001914, \"dz_s015_s020\": -0.925, \"dz_s020_s025\": -0.824, \"dz_s025_s030\": -0.773, \"dz_s015_s030\": -0.944, \"all_dz_reliable\": true, \"dose_response_monotonic\": true, \"dose_response_spearman_rho\": 1, \"dose_response_perm_p\": 0.0417, \"imp_rand_ratio_range\": \"15.5-38.6x\", \"bonferroni_k\": 4, \"bonferroni_note\": \"Bonferroni k=4 family-wise (D066 revision)\"}}, {\"id\": \"c7_c2_qw_n500_r3\", \"claim\": \"C7\", \"description\": \"QW n=500: all 4 sparsities significant (p<1e-14 Bonferroni-corrected); mid_null_rate=45.2%\", \"registry_id\": \"c2_qw_n500_r3\", \"role\": \"primary\", \"priority\": \"high\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"n_problems\": 500, \"effective_n\": 475, \"filter\": \"low+high valid only (mid-null allowed)\", \"mid_null_rate\": 0.452, \"imp_s015_median_ii\": 0.0659, \"imp_s015_ci\": [0.0492, 0.0925], \"imp_s015_wilcoxon_p\": 8.66e-15, \"imp_s015_bonf_p\": 3.46e-14, \"imp_s020_median_ii\": 0.3073, \"imp_s020_ci\": [0.2612, 0.3564], \"imp_s020_wilcoxon_p\": 6.84e-42, \"imp_s020_bonf_p\": 2.74e-41, \"imp_s025_median_ii\": 1.0745, \"imp_s025_ci\": [0.9766, 1.1787], \"imp_s025_wilcoxon_p\": 1.06e-68, \"imp_s025_bonf_p\": 4.25e-68, \"imp_s030_median_ii\": 3.155, \"imp_s030_ci\": [2.7834, 3.5582], \"imp_s030_wilcoxon_p\": 9.21e-74, \"imp_s030_bonf_p\": 3.69e-73, \"rand_s015_median_ii\": -0.0111, \"rand_s015_wilcoxon_p\": 0.172, \"rand_s015_bonf_p\": 0.687, \"rand_s020_median_ii\": 0.0153, \"rand_s020_wilcoxon_p\": 0.2, \"rand_s020_bonf_p\": 0.8, \"rand_s025_median_ii\": 0.3931, \"rand_s025_wilcoxon_p\": 1.59e-11, \"rand_s025_bonf_p\": 6.37e-11, \"rand_s025_fdr_p\": 2.63e-11, \"rand_s030_median_ii\": 0.9127, \"rand_s030_wilcoxon_p\": 2.92e-15, \"rand_s030_bonf_p\": 1.17e-14, \"rand_s030_fdr_p\": 5.61e-15, \"dz_s015_s020\": -0.629, \"dz_s020_s025\": -0.865, \"dz_s025_s030\": -0.767, \"dz_s015_s030\": -0.923, \"all_dz_reliable\": true, \"dose_response_monotonic\": true, \"dose_response_spearman_rho\": 1, \"dose_response_perm_p\": 0.0417, \"imp_rand_ratio_range\": \"2.7-20.1x\", \"bonferroni_k\": 4, \"bonferroni_note\": \"Bonferroni k=4 family-wise (D066 revision)\"}}, {\"id\": \"c8_c3_llama\", \"claim\": \"C8\", \"description\": \"LLaMA-8B (LlamaForCausalLM) replicates phase-modulated compound severity from Qwen2ForCausalLM\", \"registry_id\": \"c3_llama\", \"role\": \"primary\", \"priority\": \"high\", \"status\": \"DONE\", \"conclusion\": \"success\"}, {\"id\": \"c10_gsm8k_profiling_ds\", \"claim\": \"C10\", \"description\": \"DS GSM8K importance gradient: s015=0.241, s020=0.740, s025=1.992, s030=4.636 (monotonic)\", \"registry_id\": \"gsm8k_profiling_ds\", \"role\": \"primary\", \"priority\": \"high\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"version\": \"v3_median\", \"n_problems\": 50, \"method\": \"median + Wilcoxon + bootstrap_median(B=10000)\", \"importance\": {\"s015\": {\"median_gradient\": 0.241, \"ci_low\": 0.077, \"ci_high\": 0.478, \"wilcoxon_p\": 0.0003}, \"s020\": {\"median_gradient\": 0.74, \"ci_low\": 0.314, \"ci_high\": 1.119, \"wilcoxon_p\": 0.0001}, \"s025\": {\"median_gradient\": 1.992, \"ci_low\": 0.933, \"ci_high\": 2.82, \"wilcoxon_p\": 0.0001}, \"s030\": {\"median_gradient\": 4.682, \"ci_low\": 2.121, \"ci_high\": 10.557, \"wilcoxon_p\": 0.0001}}, \"imp_rand_ratio\": {\"s015\": 2.3, \"s020\": 2.5, \"s025\": 3.8, \"s030\": 2.8}, \"dose_response_monotonic\": true}}, {\"id\": \"c10_gsm8k_profiling_qw\", \"claim\": \"C10\", \"description\": \"QW GSM8K importance gradient: s015=0.039, s020=0.158, s025=1.100, s030=2.092 (monotonic)\", \"registry_id\": \"gsm8k_profiling_qw\", \"role\": \"primary\", \"priority\": \"high\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"version\": \"v3_median\", \"n_problems\": 50, \"method\": \"median + Wilcoxon + bootstrap_median(B=10000)\", \"importance\": {\"s015\": {\"median_gradient\": 0.039}, \"s020\": {\"median_gradient\": 0.158}, \"s025\": {\"median_gradient\": 1.1}, \"s030\": {\"median_gradient\": 2.092}}, \"qw_rand_s030\": \"INVALID\"}}, {\"id\": \"c10_gsm8k_qw_rand_s025_v2\", \"claim\": \"C10\", \"description\": \"QW random s025 GSM8K: II median_high=0.72, low=1.48; phase gradient weaker than importance\", \"registry_id\": \"gsm8k_qw_rand_s025_v2\", \"role\": \"supporting\", \"priority\": \"medium\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"verdict\": \"PASS\", \"n_problems\": 50, \"n_bootstrap\": 1000, \"seed\": 42, \"high_sparsity\": {\"n_segments\": 216, \"n_tokens\": 9326, \"ppl_dense\": 1.0695, \"ppl_attn\": 5.9362, \"ppl_kv\": 3.4316, \"ppl_both\": 15.7484, \"ii_mean\": 6.5954, \"ii_ci\": [1.1114, 11.3791], \"ii_median\": 0.7176, \"ii_median_ci\": [0.5959, 0.9347], \"winsorized_mean\": 6.5046, \"skewness\": -4.6807, \"outlier_count\": 3}, \"low_sparsity\": {\"n_segments\": 252, \"n_tokens\": 29224, \"ppl_dense\": 1.1972, \"ppl_attn\": 11.5347, \"ppl_kv\": 5.6038, \"ppl_both\": 21.6874, \"ii_mean\": 2.3883, \"ii_ci\": [-8.4602, 11.029], \"ii_median\": 1.4587, \"ii_median_ci\": [1.1121, 2.0451], \"winsorized_mean\": 5.8911, \"skewness\": -7.6074, \"outlier_count\": 4}, \"mid_sparsity\": {\"n_segments\": 51, \"n_tokens\": 5954, \"ppl_dense\": 1.2601, \"ppl_attn\": 13.4132, \"ppl_kv\": 6.4841, \"ppl_both\": 20.8714, \"ii_mean\": 4.5407, \"ii_ci\": [-4.8854, 12.4605], \"ii_median\": 1.1272, \"ii_median_ci\": [0.637, 3.3729], \"winsorized_mean\": 6.3284, \"skewness\": -3.4048, \"outlier_count\": 1}}}, {\"id\": \"c10_gsm8k_qw_rand_s030_v2\", \"claim\": \"C10\", \"description\": \"QW random s030 GSM8K: II median_high=2.31, low=5.87; compound effect on GSM8K confirmed\", \"registry_id\": \"gsm8k_qw_rand_s030_v2\", \"role\": \"supporting\", \"priority\": \"medium\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"verdict\": \"PASS\", \"n_problems\": 50, \"n_bootstrap\": 1000, \"seed\": 42, \"high_sparsity\": {\"n_segments\": 216, \"n_tokens\": 9326, \"null_ratio\": \"2/50\", \"ppl_dense\": 1.0695, \"ppl_attn\": 6.5613, \"ppl_kv\": 4.481, \"ppl_both\": 23.7486, \"ii_mean\": 11.83, \"ii_median\": 2.31, \"ii_ci\": [6.17, 17.04], \"ii_median_ci\": [1.64, 2.81], \"winsorized_mean\": 10.55, \"skewness\": -2.29, \"outlier_count\": 7}, \"low_sparsity\": {\"n_segments\": 252, \"n_tokens\": 29224, \"null_ratio\": \"5/50\", \"ppl_dense\": 1.1972, \"ppl_attn\": 6.3283, \"ppl_kv\": 8.5374, \"ppl_both\": 56.2304, \"ii_mean\": 31.26, \"ii_median\": 5.2, \"ii_ci\": [17.84, 47.86], \"ii_median_ci\": [3.95, 7.24], \"winsorized_mean\": 16.35, \"skewness\": 7.57, \"outlier_count\": 4}, \"mid_sparsity\": {\"n_segments\": 51, \"n_tokens\": 5954, \"null_ratio\": \"17/50\", \"ppl_dense\": 1.2601, \"ppl_attn\": 18.6162, \"ppl_kv\": 11.6625, \"ppl_both\": 47.9019, \"ii_mean\": 18.02, \"ii_median\": 2.7, \"ii_ci\": [0.09, 36.69], \"ii_median_ci\": [1.46, 8.77], \"winsorized_mean\": 18.22, \"skewness\": 0.43, \"outlier_count\": 2}}}, {\"id\": \"s3_c_bf16_ds_imp_s010\", \"claim\": \"S3->C\", \"description\": \"DS s=0.10: II_high_median=0.003, verdict=FAIL; below onset threshold for DeepSeek\", \"registry_id\": \"bf16_ds_imp_s010\", \"role\": \"primary\", \"priority\": \"high\", \"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"verdict\": \"FAIL\", \"problems\": 50, \"II_high_sparsity_median\": 0.0027, \"II_high_sparsity_mean\": -0.1998, \"II_low_sparsity_median\": 0.0151, \"II_low_sparsity_mean\": -0.1066, \"II_mid_sparsity_median\": 0.0061, \"II_mid_sparsity_mean\": -0.0131, \"high_sparsity_tokens\": 21086, \"low_sparsity_tokens\": 27748, \"mid_sparsity_tokens\": 13306}}, {\"id\": \"s3_c_bf16_qw_imp_s010\", \"claim\": \"S3->C\", \"description\": \"QW s=0.10: overall_verdict=PASS, CI_overlap_test=PASS; Qwen onset earlier than DeepSeek\", \"registry_id\": \"bf16_qw_imp_s010\", \"role\": \"primary\", \"priority\": \"high\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"n_problems\": 50, \"overall_verdict\": \"PASS\", \"ci_overlap_test\": \"PASS\", \"sign_reversal_test\": \"FAIL\", \"high_sparsity_II_median\": 0.0001, \"high_sparsity_II_median_CI\": [-0.0028, 0.0005], \"high_sparsity_II_mean\": -0.0887, \"high_sparsity_II_mean_CI\": [-0.1235, -0.0591], \"low_sparsity_II_median\": -0.0444, \"low_sparsity_II_median_CI\": [-0.0967, -0.0152], \"low_sparsity_II_mean\": -0.2431, \"low_sparsity_II_mean_CI\": [-0.3817, -0.1202], \"mid_sparsity_II_median\": -0.0359, \"mid_sparsity_II_median_CI\": [-0.0963, -0.015], \"mid_sparsity_II_mean\": -0.084, \"mid_sparsity_II_mean_CI\": [-0.1366, -0.035], \"ppl_high_dense\": 1.074, \"ppl_high_both\": 1.228, \"ppl_low_dense\": 1.152, \"ppl_low_both\": 3.204, \"ppl_mid_dense\": 1.133, \"ppl_mid_both\": 1.741}}, {\"id\": \"s3_c_bf16_qw_imp_s015\", \"claim\": \"S3->C\", \"description\": \"QW s=0.15: median_diff=0.048, permutation_p=0.0001; confirmed above threshold\", \"registry_id\": \"bf16_qw_imp_s015\", \"role\": \"supporting\", \"priority\": \"medium\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"median_difference\": 0.047619, \"permutation_p\": 0.0001, \"cohens_d\": 0.3705, \"bootstrap_ci_95\": [-0.005077, 0.109517], \"wilcoxon_p\": 0.02958, \"n_bootstrap\": 10000, \"n_paired\": 46}}, {\"id\": \"s7_c_c2_n500_deepseek\", \"claim\": \"S7->C\", \"description\": \"DS n=500 monotonic: imp median II 0.39->1.21->3.99->8.48 across s015-s030 (Spearman rho=1.0)\", \"registry_id\": \"c2_n500_deepseek\", \"role\": \"primary\", \"priority\": \"high\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"n_problems\": 500, \"effective_n\": 496, \"mid_null_rate\": 0.102, \"imp_s015_median_ii\": 0.3907, \"imp_s015_ci\": [0.3496, 0.4431], \"imp_s015_wilcoxon_p\": 1.27e-70, \"imp_s020_median_ii\": 1.2149, \"imp_s020_ci\": [1.1072, 1.3365], \"imp_s020_wilcoxon_p\": 3.98e-75, \"imp_s025_median_ii\": 3.9857, \"imp_s025_ci\": [3.5272, 4.3588], \"imp_s025_wilcoxon_p\": 1.99e-78, \"imp_s030_median_ii\": 8.4813, \"imp_s030_ci\": [7.7543, 9.6919], \"imp_s030_wilcoxon_p\": 1.09e-79, \"rand_s015_median_ii\": 0.0139, \"rand_s015_wilcoxon_p\": 0.863, \"rand_s020_median_ii\": 0.0315, \"rand_s020_wilcoxon_p\": 0.28, \"rand_s025_median_ii\": 0.2574, \"rand_s025_bonf_p\": 0.005839, \"rand_s025_fdr_p\": 0.001914, \"rand_s030_median_ii\": 0.5096, \"rand_s030_bonf_p\": 0.005903, \"rand_s030_fdr_p\": 0.001914, \"dz_s015_s020\": -0.925, \"dz_s020_s025\": -0.824, \"dz_s025_s030\": -0.773, \"dz_s015_s030\": -0.944, \"all_dz_reliable\": true, \"dose_response_monotonic\": true, \"dose_response_spearman_rho\": 1, \"dose_response_perm_p\": 0.0417, \"imp_rand_ratio_range\": \"15.5-38.6x\", \"bonferroni_k\": 4, \"bonferroni_note\": \"Bonferroni k=4 family-wise (D066 revision)\"}}, {\"id\": \"s7_c_c2_qw_n500_r3\", \"claim\": \"S7->C\", \"description\": \"QW n=500 monotonic: imp median II 0.066->0.307->1.075->4.33 across s015-s030 (Spearman rho=1.0)\", \"registry_id\": \"c2_qw_n500_r3\", \"role\": \"primary\", \"priority\": \"high\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"n_problems\": 500, \"effective_n\": 475, \"filter\": \"low+high valid only (mid-null allowed)\", \"mid_null_rate\": 0.452, \"imp_s015_median_ii\": 0.0659, \"imp_s015_ci\": [0.0492, 0.0925], \"imp_s015_wilcoxon_p\": 8.66e-15, \"imp_s015_bonf_p\": 3.46e-14, \"imp_s020_median_ii\": 0.3073, \"imp_s020_ci\": [0.2612, 0.3564], \"imp_s020_wilcoxon_p\": 6.84e-42, \"imp_s020_bonf_p\": 2.74e-41, \"imp_s025_median_ii\": 1.0745, \"imp_s025_ci\": [0.9766, 1.1787], \"imp_s025_wilcoxon_p\": 1.06e-68, \"imp_s025_bonf_p\": 4.25e-68, \"imp_s030_median_ii\": 3.155, \"imp_s030_ci\": [2.7834, 3.5582], \"imp_s030_wilcoxon_p\": 9.21e-74, \"imp_s030_bonf_p\": 3.69e-73, \"rand_s015_median_ii\": -0.0111, \"rand_s015_wilcoxon_p\": 0.172, \"rand_s015_bonf_p\": 0.687, \"rand_s020_median_ii\": 0.0153, \"rand_s020_wilcoxon_p\": 0.2, \"rand_s020_bonf_p\": 0.8, \"rand_s025_median_ii\": 0.3931, \"rand_s025_wilcoxon_p\": 1.59e-11, \"rand_s025_bonf_p\": 6.37e-11, \"rand_s025_fdr_p\": 2.63e-11, \"rand_s030_median_ii\": 0.9127, \"rand_s030_wilcoxon_p\": 2.92e-15, \"rand_s030_bonf_p\": 1.17e-14, \"rand_s030_fdr_p\": 5.61e-15, \"dz_s015_s020\": -0.629, \"dz_s020_s025\": -0.865, \"dz_s025_s030\": -0.767, \"dz_s015_s030\": -0.923, \"all_dz_reliable\": true, \"dose_response_monotonic\": true, \"dose_response_spearman_rho\": 1, \"dose_response_perm_p\": 0.0417, \"imp_rand_ratio_range\": \"2.7-20.1x\", \"bonferroni_k\": 4, \"bonferroni_note\": \"Bonferroni k=4 family-wise (D066 revision)\"}}, {\"id\": \"s7_c_bf16_qw_imp_s035\", \"claim\": \"S7->C\", \"description\": \"QW s=0.35: low_II_median=8.24; extends dose-response beyond s030\", \"registry_id\": \"bf16_qw_imp_s035\", \"role\": \"supporting\", \"priority\": \"medium\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"n_problems\": 50, \"overall_verdict\": \"PASS\", \"ci_overlap_test\": \"PASS\", \"sign_reversal_test\": \"FAIL\", \"high_sparsity_II_median\": 0.0232, \"high_sparsity_II_median_CI\": [0.0154, 0.0383], \"high_sparsity_II_mean\": 0.1643, \"high_sparsity_II_mean_CI\": [0.0844, 0.2495], \"low_sparsity_II_median\": 8.2358, \"low_sparsity_II_median_CI\": [6.1564, 10.9231], \"low_sparsity_II_mean\": 18.9673, \"low_sparsity_II_mean_CI\": [14.5015, 23.9752], \"mid_sparsity_II_median\": 0.9577, \"mid_sparsity_II_median_CI\": [0.171, 3.5575], \"mid_sparsity_II_mean\": 8.0734, \"mid_sparsity_II_mean_CI\": [2.0224, 16.8946], \"ppl_high_dense\": 1.0738, \"ppl_high_both\": 2.3435, \"ppl_low_dense\": 1.1518, \"ppl_low_both\": 58.0358, \"ppl_mid_dense\": 1.1327, \"ppl_mid_both\": 20.9912, \"high_sparsity_tokens\": 16289, \"low_sparsity_tokens\": 32227, \"mid_sparsity_tokens\": 4372}}], \"total\": 38}, \"error\": null, \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "1c869f6a-2638-4ba9-832e-ecdb9d44f06d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/.claude/sessions/agent_9c1243df",
  "sessionId": "ffa9d23f-27b7-4443-aea1-c7cdeeb2bf53",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 57 · 2026-05-16T02:47:48.140Z_

```json
{
  "parentUuid": "634a406a-9c64-415a-b06a-b890b55966ef",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "22dbdb58-901a-45ec-84b2-4e57191a3981",
  "timestamp": "2026-05-16T02:47:48.140Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/.claude/sessions/agent_9c1243df",
  "sessionId": "ffa9d23f-27b7-4443-aea1-c7cdeeb2bf53",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 58_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[HANDOFF] 你是 Main Agent，这是 Loop #15。  ## 上一轮交接 (task_context)  ### 1. 🔴 硬约束 / 红线 - GPU 白名单：**westd-22162 cuda:0~3** 仅此 4 张，不可用其他 GPU - c8_llama_n250 正在占满 4 GPU（4 并行推理），完成前不可提交新 GPU 实验 - EMNLP 2026 AR…",
  "leafUuid": "22dbdb58-901a-45ec-84b2-4e57191a3981",
  "sessionId": "ffa9d23f-27b7-4443-aea1-c7cdeeb2bf53"
}
```

---

### Runtime record

_source line 59_

```json
{
  "type": "ai-title",
  "aiTitle": "Verify active experiments and paper revisions for EMNLP 2026",
  "sessionId": "ffa9d23f-27b7-4443-aea1-c7cdeeb2bf53"
}
```

---

### Assistant

_source line 60 · 2026-05-16T02:48:30.058Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have the full picture. Let me summarize:

**Active experiments:**
- c8_llama_n250: RUNNING (4 GPU, pid=301187 alive, cron monitoring)
- c5_per_phase_gini: PREPARING, Worker running
- c9_gsm8k_power_analysis: PREPARING, Worker running
- c10_lang_switching: PREPARING, Worker running
- c4_think_validation_math500: PREPARING, **NO Worker** → GAP

**Immediate actions needed:**
1. Spawn Worker for c4_think_validation_math500 (CPU task)


2. Report to Director with [资源] line

Looking at the experiment lineage, c2_think_phase_validation already validated think token positions against PPL phase segmentation and achieved kappa=0.887 on the dataset. The c4_think_validation_math500 experiment extends this validation to MATH-500 problems, testing both datasets.

From the roadmap, c4 is specifically validating that think token boundaries align with PPL-derived phase boundaries across 50 MATH problems for both DS and QW. This addresses R10-C4's concern about whether the PPL-based phase segmentation actually captures meaningful chain-of-thought phases. The worker hasn't started yet, possibly waiting for dependencies or queue availability.

Now I need to spawn the c4 Worker with the right configuration — westd-22162 server, the pacs working directory, and access to the already-completed c4_entropy data. After that spawns, I'll have 4 active workers, but once c5/c9/c10 finish, the pool drops to just 1, which means I should queue up the paper-related workers then to maintain saturation before the 9-day deadline.

The bib audit task is tempting to spawn now since it's independent and critical (that fake citation issue needs fixing), but I should stick with the handoff plan — wait for at least one CPU worker callback with fresh results before launching the paper tasks. The workers have been running since around 2:42 UTC, so I need to check the current time to estimate when they'll finish.

Let me write the c4 worker prompt. I'm trying to understand what distinguishes this task — the existing think_phase_validation already achieved kappa=0.887 on a smaller sample, so what's the actual difference with extending to MATH-500?

Looking at the registry, the original validation was DS-only with an effective n of 48 across 4 sparsity conditions. The c4 task appears to be adding QW and scaling up the sample size, making it more rigorous than the pilot.

I'm gathering what the Worker needs: SSH access to the data store, read permissions for the c4_entropy dataset, understanding of the validation methodology, and registry write access for results. I should also check if there's existing code from the original think_phase_validation that can be reused or built upon. Let me set up the Worker with all the necessary context and spawn it now.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "22dbdb58-901a-45ec-84b2-4e57191a3981",
  "isSidechain": false,
  "requestId": "req_011Cb5V3wH7LXsDUcPAqdV1m",
  "type": "assistant",
  "uuid": "7bf123af-8309-4545-ada2-8bd96295cd95",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/.claude/sessions/agent_9c1243df",
  "sessionId": "ffa9d23f-27b7-4443-aea1-c7cdeeb2bf53",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012TLyP5aKsiuaMXaaXa7Fxi",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 21343,
      "cache_read_input_tokens": 52279,
      "output_tokens": 1871,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 21343,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1871,
          "cache_read_input_tokens": 52279,
          "cache_creation_input_tokens": 21343,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 21343
          },
          "type": "message"
        }
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

_source line 61 · 2026-05-16T02:48:30.127Z_

c4_think_validation_math500 无 Worker 在跑——立即补派。同时检查是否有现成代码可复用。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7bf123af-8309-4545-ada2-8bd96295cd95",
  "isSidechain": false,
  "requestId": "req_011Cb5V3wH7LXsDUcPAqdV1m",
  "type": "assistant",
  "uuid": "f38ce9fa-0899-4454-a3b9-ebb292bd5625",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/.claude/sessions/agent_9c1243df",
  "sessionId": "ffa9d23f-27b7-4443-aea1-c7cdeeb2bf53",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012TLyP5aKsiuaMXaaXa7Fxi",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 21343,
      "cache_read_input_tokens": 52279,
      "output_tokens": 1871,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 21343,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1871,
          "cache_read_input_tokens": 52279,
          "cache_creation_input_tokens": 21343,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 21343
          },
          "type": "message"
        }
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

_source line 62 · 2026-05-16T02:48:35.264Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01HQaBU5H7j4aREfGCfdiEjN`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-phase-gated-compound-sparse--claude-sessions-agent-9c1243df/ffa9d23f-27b7-4443-aea1-c7cdeeb2bf53/tool-results/mcp-agent-ml-research-read_registry-1778899563513.txt | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\nresult = json.loads(data['result'])\nexperiments = result['data']['experiments']\n# Get think_phase_validation details\nfor key in ['think_phase_validation', 'c4_think_validation_math500']:\n    if key in experiments:\n        e = experiments[key]\n        print(f'=== {key} ===')\n        print(json.dumps(e, indent=2, default=str)[:3000])\n        print()\n\"\n",
  "description": "Get think_phase_validation and c4 experiment details"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f38ce9fa-0899-4454-a3b9-ebb292bd5625",
  "isSidechain": false,
  "requestId": "req_011Cb5V3wH7LXsDUcPAqdV1m",
  "type": "assistant",
  "uuid": "259b8a88-8a19-41a9-8f95-d33eac6da43e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/.claude/sessions/agent_9c1243df",
  "sessionId": "ffa9d23f-27b7-4443-aea1-c7cdeeb2bf53",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012TLyP5aKsiuaMXaaXa7Fxi",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 21343,
      "cache_read_input_tokens": 52279,
      "output_tokens": 1871,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 21343,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1871,
          "cache_read_input_tokens": 52279,
          "cache_creation_input_tokens": 21343,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 21343
          },
          "type": "message"
        }
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

_source line 63 · 2026-05-16T02:48:35.441Z_

<details><summary>↩ Tool result · `toolu_01HQaBU5H7j4aREfGCfdiEjN`</summary>

```text
=== think_phase_validation ===
{
  "status": "DONE",
  "created_at": "2026-05-15T19:35:06.395Z",
  "updated_at": "2026-05-15T19:35:45.955Z",
  "conclusion": "success",
  "metrics": {
    "effective_n": 48,
    "skipped_problems": 2,
    "median_kappa": 0.887,
    "thinking_in_low_sparsity_phase": 0.578,
    "answer_in_high_sparsity_phase": 0.627,
    "note": "Phase segmentation based on dense model \u2014 4 sparsity conditions share identical phase boundaries, effective sample n=48 not n=192"
  }
}

=== c4_think_validation_math500 ===
{
  "status": "PREPARING",
  "created_at": "2026-05-16T02:32:40.564Z",
  "updated_at": "2026-05-16T02:32:40.564Z"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "259b8a88-8a19-41a9-8f95-d33eac6da43e",
  "isSidechain": false,
  "promptId": "d6a043a1-3c08-4fe7-9e57-50e76a38ea26",
  "type": "user",
  "uuid": "1901d661-bc60-46c6-8695-f143b7a0673a",
  "toolUseResult": {
    "stdout": "=== think_phase_validation ===\n{\n  \"status\": \"DONE\",\n  \"created_at\": \"2026-05-15T19:35:06.395Z\",\n  \"updated_at\": \"2026-05-15T19:35:45.955Z\",\n  \"conclusion\": \"success\",\n  \"metrics\": {\n    \"effective_n\": 48,\n    \"skipped_problems\": 2,\n    \"median_kappa\": 0.887,\n    \"thinking_in_low_sparsity_phase\": 0.578,\n    \"answer_in_high_sparsity_phase\": 0.627,\n    \"note\": \"Phase segmentation based on dense model \\u2014 4 sparsity conditions share identical phase boundaries, effective sample n=48 not n=192\"\n  }\n}\n\n=== c4_think_validation_math500 ===\n{\n  \"status\": \"PREPARING\",\n  \"created_at\": \"2026-05-16T02:32:40.564Z\",\n  \"updated_at\": \"2026-05-16T02:32:40.564Z\"\n}",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "259b8a88-8a19-41a9-8f95-d33eac6da43e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/.claude/sessions/agent_9c1243df",
  "sessionId": "ffa9d23f-27b7-4443-aea1-c7cdeeb2bf53",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 64 · 2026-05-16T02:48:45.368Z_

<details><summary>Logged reasoning block</summary>

```text
Now I need to spawn the c4 Worker. Let me construct a detailed prompt. The task is:

1. Validate `&lt;think>` token positions against PPL phase segmentation
2. For both DS and QW models
3. On 50 MATH-500 problems
4. This extends the existing think_phase_validation (DS only, n=48, kappa=0.887)

I need to check what code exists for think_phase_validation on the server. The Worker should:
1. SSH to westd-22162
2. Find the existing think_phase_validation code
3. Extend it to QW model


4. Run on 50 MATH-500 problems and compute kappa agreement plus phase-token alignment stats
5. Update the registry with results

I should also factor in the R10-C4 reviewer concern from the ROADMAP about whether PPL-based phase segmentation actually aligns with meaningful CoT phases. The validation needs to demonstrate that `&lt;think>` tokens map to the low-sparsity-sensitive phase while answer tokens align appropriately. Let me spawn the Worker with SSH, registry, and knowledge tool groups to handle this.

Now I'm crafting the prompt to show that Cohen's kappa is high between the PPL-based phases and the `&lt;think>` token phases.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1901d661-bc60-46c6-8695-f143b7a0673a",
  "isSidechain": false,
  "requestId": "req_011Cb5V7RaJ95fVybardt1VG",
  "type": "assistant",
  "uuid": "59a8883f-1b5b-436c-88eb-47ef6029ef13",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/.claude/sessions/agent_9c1243df",
  "sessionId": "ffa9d23f-27b7-4443-aea1-c7cdeeb2bf53",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PEz5mEBKo35sRD52ptXZn2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2156,
      "cache_read_input_tokens": 73622,
      "output_tokens": 1683,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2156,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1683,
          "cache_read_input_tokens": 73622,
          "cache_creation_input_tokens": 2156,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2156
          },
          "type": "message"
        }
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

_source line 65 · 2026-05-16T02:49:05.345Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__spawn_worker · `toolu_01RHMz9q45HvV8VyxvnPDzD8`</summary>

```json
{
  "task_type": "analysis:c4_think_validation_math500",
  "project": "phase-gated-compound-sparse",
  "task_prompt": "## 任务：`&lt;think>` Token 与 PPL Phase Segmentation 一致性验证\n\n### 背景\nRound 10 审稿 R10-C4 质疑 PPL-based phase segmentation 是否真正对应有意义的 CoT 阶段。已有 pilot 验证（think_phase_validation, DS only, n=48, kappa=0.887）。本任务需扩展到 **DS + QW 双模型**，用更系统的方式验证。\n\n### 目标\n在 westd-22162 服务器上，对 50 个 MATH-500 问题，分别用 DS 和 QW 模型：\n1. 提取每个 problem 的 `&lt;think>...&lt;/think>` token 边界\n2. 与 PPL-based phase segmentation（来自 c4_entropy 实验数据）对比\n3. 计算 Cohen's kappa、thinking tokens 在 low-sparsity phase 的比例、answer tokens 在 high-sparsity phase 的比例\n\n### 环境\n- 服务器：westd-22162\n- 工作目录：`/root/autodl-tmp/pacs`\n- Python 环境：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`\n- 模型路径：DeepSeek-R1-Distill-Qwen-7B 和 Qwen2.5-7B-Instruct 在服务器本地（先 `ls /root/autodl-tmp/` 确认路径）\n- 已有代码：查找 `think_phase_validation` 或 `think_valid` 相关脚本（可能在 /root/autodl-tmp/pacs/ 下）\n- c4_entropy 数据：查找 c4_entropy 相关输出文件（perplexity + phase segmentation 数据）\n\n### 执行步骤\n1. SSH 到 westd-22162，探测环境和已有代码/数据\n2. 找到 think_phase_validation 的已有脚本，理解其方法\n3. 扩展或新写脚本，覆盖 DS + QW 双模型\n4. 运行验证（CPU 任务，不需要 GPU——只需要读取已生成的 perplexity 数据和 token 序列）\n5. 产出：每个模型的 kappa、thinking_in_low_ratio、answer_in_high_ratio\n\n### 输出要求\n- 更新 registry `c4_think_validation_math500` 的 metrics，包含：\n  - ds_kappa, ds_thinking_in_low, ds_answer_in_high, ds_effective_n\n  - qw_kappa, qw_thinking_in_low, qw_answer_in_high, qw_effective_n\n  - combined_kappa (if applicable)\n- 结论判断：kappa ≥ 0.8 且 thinking_in_low ≥ 0.5 且 answer_in_high ≥ 0.5 → success\n\n### 注意\n- 这是 CPU 分析任务，不需要 submit_training_job\n- 如果找不到已有的 perplexity/phase 数据，查找 c4_entropy 实验的输出目录\n- QW 模型（Qwen2.5-7B-Instruct）不使用 `&lt;think>` token——它用不同的 CoT 格式。需要先确认 QW 的 CoT 分隔方式（可能是直接文本段落，而非 `&lt;think>` 标记）。如果 QW 没有显式 `&lt;think>` 标记，报告这一发现并只做 DS 验证。\n- DeepSeek-R1 系列使用 `&lt;think>...&lt;/think>` 标记\n",
  "tool_groups": [
    "ssh",
    "registry",
    "knowledge"
  ],
  "context": "Round 10 审稿修订中，EMNLP 2026 ARR 截稿 2026-05-25。R10-C4 质疑 PPL phase segmentation 与 CoT phase 的对应关系。已有 pilot: DS kappa=0.887, thinking_in_low=0.578, answer_in_high=0.627 (n=48)。本任务需更系统地验证并覆盖 QW 模型。服务器 westd-22162，conda base 环境。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "59a8883f-1b5b-436c-88eb-47ef6029ef13",
  "isSidechain": false,
  "requestId": "req_011Cb5V7RaJ95fVybardt1VG",
  "type": "assistant",
  "uuid": "ddd41f2b-ba9b-410e-8394-19e7052914fb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/.claude/sessions/agent_9c1243df",
  "sessionId": "ffa9d23f-27b7-4443-aea1-c7cdeeb2bf53",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PEz5mEBKo35sRD52ptXZn2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2156,
      "cache_read_input_tokens": 73622,
      "output_tokens": 1683,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2156,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1683,
          "cache_read_input_tokens": 73622,
          "cache_creation_input_tokens": 2156,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2156
          },
          "type": "message"
        }
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

_source line 66 · 2026-05-16T02:49:08.441Z_

<details><summary>↩ Tool result · `toolu_01RHMz9q45HvV8VyxvnPDzD8`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"worker_id\": \"worker_analysis_c4_think_validation_math500_20260516T024906\", \"status\": \"running\", \"log_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/logs/workers/worker_analysis_c4_think_validation_math500_20260516T024906.log\", \"setup_data\": {}, \"message\": \"Worker worker_analysis_c4_think_validation_math500_20260516T024906 started. Use get_worker_status('worker_analysis_c4_think_validation_math500_20260516T024906') to check progress.\"}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ddd41f2b-ba9b-410e-8394-19e7052914fb",
  "isSidechain": false,
  "promptId": "d6a043a1-3c08-4fe7-9e57-50e76a38ea26",
  "type": "user",
  "uuid": "da52b034-6e55-43db-a0a4-c52b4037f262",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"worker_id\\\": \\\"worker_analysis_c4_think_validation_math500_20260516T024906\\\", \\\"status\\\": \\\"running\\\", \\\"log_path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/logs/workers/worker_analysis_c4_think_validation_math500_20260516T024906.log\\\", \\\"setup_data\\\": {}, \\\"message\\\": \\\"Worker worker_analysis_c4_think_validation_math500_20260516T024906 started. Use get_worker_status('worker_analysis_c4_think_validation_math500_20260516T024906') to check progress.\\\"}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"worker_id\": \"worker_analysis_c4_think_validation_math500_20260516T024906\", \"status\": \"running\", \"log_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/logs/workers/worker_analysis_c4_think_validation_math500_20260516T024906.log\", \"setup_data\": {}, \"message\": \"Worker worker_analysis_c4_think_validation_math500_20260516T024906 started. Use get_worker_status('worker_analysis_c4_think_validation_math500_20260516T024906') to check progress.\"}, \"error\": null, \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "ddd41f2b-ba9b-410e-8394-19e7052914fb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/.claude/sessions/agent_9c1243df",
  "sessionId": "ffa9d23f-27b7-4443-aea1-c7cdeeb2bf53",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 67 · 2026-05-16T02:49:22.247Z_

<details><summary>Logged reasoning block</summary>

```text
c4 Worker spawned. Now let me do the resource saturation check and report to Director.

Current state:
- **GPU**: 4/4 allocated, 4/4 in use (c8_llama_n250)
- **Worker pool**: 4 running (c5_per_phase_gini, c9_gsm8k_power, c10_lang_switching, c4_think_validation_math500) — all CPU tasks
- **GPU task**: 1 (c8_llama_n250)
- **CPU tasks**: 4

Resource line: [资源] GPU 分配 4 / 实际在跑 4 | Worker 池 4 (GPU 1 / CPU 4)


Everything's running well with 4 Workers exceeding the minimum threshold and GPU fully utilized. I need to update the Director with the current status: Session 15 is live, c8_llama_n250 is still executing with active process monitoring, and I have four CPU Workers handling different validation tasks including the newly spawned c4. The Paper Agent is standing by until these Workers finish their callbacks, then I'll kick off the writing revisions.

The Workers started around 02:41-02:42 UTC, so they should be wrapping up soon — I'll monitor for their completion signals before moving forward.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "da52b034-6e55-43db-a0a4-c52b4037f262",
  "isSidechain": false,
  "requestId": "req_011Cb5V9rcjw9WASd6dhEg5t",
  "type": "assistant",
  "uuid": "4d533ac5-0ffd-4d73-988b-6ce040e3d695",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/.claude/sessions/agent_9c1243df",
  "sessionId": "ffa9d23f-27b7-4443-aea1-c7cdeeb2bf53",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XTN4KU4pZeYDGGdDXZCrUp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1896,
      "cache_read_input_tokens": 75778,
      "output_tokens": 905,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1896,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 905,
          "cache_read_input_tokens": 75778,
          "cache_creation_input_tokens": 1896,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1896
          },
          "type": "message"
        }
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

_source line 68 · 2026-05-16T02:49:22.248Z_

c4 Worker 已启动。当前 Worker 池 = 4（全部 CPU 任务），GPU 4/4 被 c8_llama_n250 占用。向 Director 汇报。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4d533ac5-0ffd-4d73-988b-6ce040e3d695",
  "isSidechain": false,
  "requestId": "req_011Cb5V9rcjw9WASd6dhEg5t",
  "type": "assistant",
  "uuid": "4ad1c315-b892-4374-9471-bda870157030",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/.claude/sessions/agent_9c1243df",
  "sessionId": "ffa9d23f-27b7-4443-aea1-c7cdeeb2bf53",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XTN4KU4pZeYDGGdDXZCrUp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1896,
      "cache_read_input_tokens": 75778,
      "output_tokens": 905,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1896,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 905,
          "cache_read_input_tokens": 75778,
          "cache_creation_input_tokens": 1896,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1896
          },
          "type": "message"
        }
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

_source line 69 · 2026-05-16T02:49:28.394Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__main_agent_post_to_director · `toolu_01WcrFgR3y1yuMJTZjoUBwMD`</summary>

```json
{
  "text": "[资源] GPU 分配 4 / 实际在跑 4 (c8_llama_n250) | Worker 池 4 (GPU 0 / CPU 4)\n\n**Session 15 初始化完成，状态同步：**\n\n1. **c8_llama_n250** RUNNING — LLaMA n=250 跨架构验证（8 conditions），pid=301187 存活，cron 300s 监控中。预估完成时间待 cron 下次回调确认进度。\n\n2. **4 个 CPU Worker 并行中**（均 PREPARING → Worker 已在执行）：\n   - c5_per_phase_gini — per-phase Gini decomposition（从 c4_entropy 数据）\n   - c9_gsm8k_power_analysis — GSM8K post-hoc power analysis\n   - c10_lang_switching — DS language switching rate 检查\n   - c4_think_validation_math500 — `&lt;think>` token vs PPL phase 一致性验证（**刚补派，之前遗漏无 Worker**）\n\n3. **待办序列**：CPU Worker 回调 → spawn Paper Agent（bib 审计 + Abstract/Intro + §4-7 + Appendix 并行修订）→ c8 回调 → LLaMA 结果写入论文 → Round 11 提交\n\n无阻塞，全速推进中。",
  "project": "phase-gated-compound-sparse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4ad1c315-b892-4374-9471-bda870157030",
  "isSidechain": false,
  "requestId": "req_011Cb5V9rcjw9WASd6dhEg5t",
  "type": "assistant",
  "uuid": "cd3b8604-9f41-4128-b72e-f1f2ee5f0f23",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/.claude/sessions/agent_9c1243df",
  "sessionId": "ffa9d23f-27b7-4443-aea1-c7cdeeb2bf53",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XTN4KU4pZeYDGGdDXZCrUp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1896,
      "cache_read_input_tokens": 75778,
      "output_tokens": 905,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1896,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 905,
          "cache_read_input_tokens": 75778,
          "cache_creation_input_tokens": 1896,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1896
          },
          "type": "message"
        }
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

_source line 70_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[HANDOFF] 你是 Main Agent，这是 Loop #15。  ## 上一轮交接 (task_context)  ### 1. 🔴 硬约束 / 红线 - GPU 白名单：**westd-22162 cuda:0~3** 仅此 4 张，不可用其他 GPU - c8_llama_n250 正在占满 4 GPU（4 并行推理），完成前不可提交新 GPU 实验 - EMNLP 2026 AR…",
  "leafUuid": "cd3b8604-9f41-4128-b72e-f1f2ee5f0f23",
  "sessionId": "ffa9d23f-27b7-4443-aea1-c7cdeeb2bf53"
}
```

---

### Runtime record

_source line 71_

```json
{
  "type": "ai-title",
  "aiTitle": "Verify active experiments and paper revisions for EMNLP 2026",
  "sessionId": "ffa9d23f-27b7-4443-aea1-c7cdeeb2bf53"
}
```

---

### Tool result

_source line 72 · 2026-05-16T02:49:32.943Z_

<details><summary>↩ Tool result · `toolu_01WcrFgR3y1yuMJTZjoUBwMD`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"director_session\": \"feishu:group:oc_fdc656be1c7fe17c11ab639cdbce3710:director\"}, \"error\": \"\"}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cd3b8604-9f41-4128-b72e-f1f2ee5f0f23",
  "isSidechain": false,
  "promptId": "d6a043a1-3c08-4fe7-9e57-50e76a38ea26",
  "type": "user",
  "uuid": "6c3c4a7a-e4f7-4594-9e74-4d82a47a5cce",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"director_session\\\": \\\"feishu:group:oc_fdc656be1c7fe17c11ab639cdbce3710:director\\\"}, \\\"error\\\": \\\"\\\"}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"director_session\": \"feishu:group:oc_fdc656be1c7fe17c11ab639cdbce3710:director\"}, \"error\": \"\"}"
    }
  },
  "sourceToolAssistantUUID": "cd3b8604-9f41-4128-b72e-f1f2ee5f0f23",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/.claude/sessions/agent_9c1243df",
  "sessionId": "ffa9d23f-27b7-4443-aea1-c7cdeeb2bf53",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---
