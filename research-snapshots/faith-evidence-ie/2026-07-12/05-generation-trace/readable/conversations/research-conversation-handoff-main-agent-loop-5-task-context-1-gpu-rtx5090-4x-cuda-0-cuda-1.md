# Research conversation: [HANDOFF] 你是 Main Agent，这是 Loop #5。 ## 上一轮交接 (task_context) ### 1. 🔴 硬约束 / 红线 - 本项目 GPU 白名单：rtx5090-4x 的 cuda:0, cuda:1,

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 8
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-1/16904510-f7d3-4b77-af37-09307a65997c.jsonl`
- **Structured JSON:** [`f5a2f95658248c711447.json`](../../sessions/f5/f5a2f95658248c711447.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-15T00:21:51.305Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-15T00:21:51.305Z",
  "sessionId": "16904510-f7d3-4b77-af37-09307a65997c",
  "content": "[HANDOFF] 你是 Main Agent，这是 Loop #5。\n\n## 上一轮交接 (task_context)\n\n### 1. 🔴 硬约束 / 红线\n- 本项目 GPU 白名单：rtx5090-4x 的 cuda:0, cuda:1, cuda:2, cuda:3（4 张全分配）\n- kl001_r4 系列（lr=5e-5）已判 FAIL(D027)，禁止再启动该方向新实验\n- PREPARING 队列中的 mvp2_grpo_ced_kl001_r2/r3 属 FAIL 方向，不要启动\n- P0 pass criteria: ckpt-20 rel_f1 > 0.30；P0+P1 额外要求 pred_count ≥ 9720\n- submit_on_allocated 命令必须自带环境激活（服务器用 conda：`source /root/miniconda3/bin/activate`）\n\n### 2. 🖥️ 基础设施快照\n- 服务器：rtx5090-4x（4× RTX 5090 32GB，2 个 SSH endpoint 同一台机器）\n- 工作目录：/root/autodl-tmp/（大文件）、代码在 /root/ 下的项目目录\n- Python：/root/miniconda3/bin/python（conda base 环境）\n- 模型：Qwen3-4B，SFT adapter 在 /root/autodl-tmp/sft_output\n- GRPO checkpoint 目录：/root/autodl-tmp/grpo_ced_lr5e6_r1/（P0）、/root/autodl-tmp/grpo_ced_lr5e6_rp_r2/（P0+P1）\n- 数据：/root/autodl-tmp/data/docred（dev: 985 条）\n- Eval 结果：/root/autodl-tmp/eval_results/\n- 活跃进程：\n  - mvp2_grpo_ced_lr5e6_r1: PID 90080, cuda:0, step ~25/200\n  - mvp2_grpo_ced_lr5e6_rp_r2: PID 94758, cuda:3, step ~8/200\n  - mvp2_eval_lr5e6_r1_ckpt20: PID 96500, cuda:1, ~6% done\n- Cron 监控上述 3 个实验\n\n### 3. 📊 当前状态\n刚收到 mvp2_eval_ced_kl001_r4_multi 的失败 cron 回调（\"process dead 5× with no sentinel/W&B\"）。这是预期退出——kl001_r4 已 FAIL，Director 之前指令 ckpt-30 后即停。\n\n已完成动作：\n- session-start 初始化（registry + reconcile + ROADMAP）\n- 派 Worker（worker_diagnose_mvp2_eval_ced_kl001_r4_multi_20260514T212003）读日志确认失败原因\n- 向 Director 汇报 cuda:2 空闲，请求决策下一步\n\n等待中：\n- Worker 诊断回调（读日志 + 更新 registry failure_reason）\n- Director 决策 cuda:2 分配（建议 P0 ckpt-30 eval，但 P0 目前 step 25，ckpt-30 即将生成）\n\n### 4. 📋 待办\n- 诊断 Worker 完成 → 确认 failure_reason 已更新，检查是否有可提取的 eval metrics\n- Director 回复 cuda:2 决策 → 按指令执行（大概率是 P0 ckpt-30 或 ckpt-40 eval）\n- P0 到达 step 30 → 在 cuda:2 启动 ckpt-30 eval（如 Director 批准）\n- mvp2_eval_lr5e6_r1_ckpt20 完成（cuda:1）→ 分析结果，rel_f1 > 0.30 = PASS → 立即启动 P0+P1 ckpt-20 eval\n- P0 ckpt-20 eval PASS → MVP-2 P0 通过，进入完整评估框架阶段\n- P0 ckpt-20 eval FAIL (rel_f1 ≤ 0.30) → 产出 Framing 调整提案，禁止默默跑下一个\n\n### 5. 🎯 战略上下文\n- 项目核心：FREIGE — 用 CED 奖励训练 LLM 做文档级关系抽取 + 可验证证据生成\n- MVP-1 已 PASS（CED margin 0.4827, acc 81.5%）\n- MVP-2 核心验证：lr=5e-6 GRPO 是否避免灾难性遗忘（lr=5e-5 全灭）\n- 关键决策链：D027 判定 lr=5e-5 FAIL → 转向 lr=5e-6 → P0（纯 lr 修复）vs P0+P1（lr + recall_penalty）并行验证\n- 易错点：P0 训练 200 steps，checkpoint 间隔看代码配置（可能 10 steps），不要假设 ckpt 编号 = step 数（需确认）\n- 易错点：eval 脚本用 `--quantize` 标志（QLoRA 4-bit），忘加会 OOM 或结果不对\n- cuda:2 空闲是当前唯一资源浪费点，但短期内确实没可跑的实验（P0 ckpt-30 几小时内会到）\n\n## 可查的历史\n前 33 轮 handoff 在 `task_context/history/agent/loop_*.md`，如有疑问可 Read 回查。\n完整聊天归档可用 `recall_session_history(\"关键词\")` 搜索。\n\n## 第一个动作要求\n1. 用 `read_registry` 确认当前 RUNNING/PREPARING 实验状态（防止幻觉记忆过时状态）\n2. 回复一句话确认你看到了上面的硬约束 + 当前活跃实验，再开始任何工具调用"
}
```

---

### Runtime record

_source line 2 · 2026-05-15T00:21:51.308Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-15T00:21:51.308Z",
  "sessionId": "16904510-f7d3-4b77-af37-09307a65997c"
}
```

---

## Round 1

6 recorded events

### User

_source line 3 · 2026-05-15T00:21:51.357Z_

[HANDOFF] 你是 Main Agent，这是 Loop #5。

## 上一轮交接 (task_context)

### 1. 🔴 硬约束 / 红线
- 本项目 GPU 白名单：rtx5090-4x 的 cuda:0, cuda:1, cuda:2, cuda:3（4 张全分配）
- kl001_r4 系列（lr=5e-5）已判 FAIL(D027)，禁止再启动该方向新实验
- PREPARING 队列中的 mvp2_grpo_ced_kl001_r2/r3 属 FAIL 方向，不要启动
- P0 pass criteria: ckpt-20 rel_f1 > 0.30；P0+P1 额外要求 pred_count ≥ 9720
- submit_on_allocated 命令必须自带环境激活（服务器用 conda：`source /root/miniconda3/bin/activate`）

### 2. 🖥️ 基础设施快照
- 服务器：rtx5090-4x（4× RTX 5090 32GB，2 个 SSH endpoint 同一台机器）
- 工作目录：/root/autodl-tmp/（大文件）、代码在 /root/ 下的项目目录
- Python：/root/miniconda3/bin/python（conda base 环境）
- 模型：Qwen3-4B，SFT adapter 在 /root/autodl-tmp/sft_output
- GRPO checkpoint 目录：/root/autodl-tmp/grpo_ced_lr5e6_r1/（P0）、/root/autodl-tmp/grpo_ced_lr5e6_rp_r2/（P0+P1）
- 数据：/root/autodl-tmp/data/docred（dev: 985 条）
- Eval 结果：/root/autodl-tmp/eval_results/
- 活跃进程：
  - mvp2_grpo_ced_lr5e6_r1: PID 90080, cuda:0, step ~25/200
  - mvp2_grpo_ced_lr5e6_rp_r2: PID 94758, cuda:3, step ~8/200
  - mvp2_eval_lr5e6_r1_ckpt20: PID 96500, cuda:1, ~6% done
- Cron 监控上述 3 个实验

### 3. 📊 当前状态
刚收到 mvp2_eval_ced_kl001_r4_multi 的失败 cron 回调（"process dead 5× with no sentinel/W&B"）。这是预期退出——kl001_r4 已 FAIL，Director 之前指令 ckpt-30 后即停。

已完成动作：
- session-start 初始化（registry + reconcile + ROADMAP）
- 派 Worker（worker_diagnose_mvp2_eval_ced_kl001_r4_multi_20260514T212003）读日志确认失败原因
- 向 Director 汇报 cuda:2 空闲，请求决策下一步

等待中：
- Worker 诊断回调（读日志 + 更新 registry failure_reason）
- Director 决策 cuda:2 分配（建议 P0 ckpt-30 eval，但 P0 目前 step 25，ckpt-30 即将生成）

### 4. 📋 待办
- 诊断 Worker 完成 → 确认 failure_reason 已更新，检查是否有可提取的 eval metrics
- Director 回复 cuda:2 决策 → 按指令执行（大概率是 P0 ckpt-30 或 ckpt-40 eval）
- P0 到达 step 30 → 在 cuda:2 启动 ckpt-30 eval（如 Director 批准）
- mvp2_eval_lr5e6_r1_ckpt20 完成（cuda:1）→ 分析结果，rel_f1 > 0.30 = PASS → 立即启动 P0+P1 ckpt-20 eval
- P0 ckpt-20 eval PASS → MVP-2 P0 通过，进入完整评估框架阶段
- P0 ckpt-20 eval FAIL (rel_f1 ≤ 0.30) → 产出 Framing 调整提案，禁止默默跑下一个

### 5. 🎯 战略上下文
- 项目核心：FREIGE — 用 CED 奖励训练 LLM 做文档级关系抽取 + 可验证证据生成
- MVP-1 已 PASS（CED margin 0.4827, acc 81.5%）
- MVP-2 核心验证：lr=5e-6 GRPO 是否避免灾难性遗忘（lr=5e-5 全灭）
- 关键决策链：D027 判定 lr=5e-5 FAIL → 转向 lr=5e-6 → P0（纯 lr 修复）vs P0+P1（lr + recall_penalty）并行验证
- 易错点：P0 训练 200 steps，checkpoint 间隔看代码配置（可能 10 steps），不要假设 ckpt 编号 = step 数（需确认）
- 易错点：eval 脚本用 `--quantize` 标志（QLoRA 4-bit），忘加会 OOM 或结果不对
- cuda:2 空闲是当前唯一资源浪费点，但短期内确实没可跑的实验（P0 ckpt-30 几小时内会到）

## 可查的历史
前 33 轮 handoff 在 `task_context/history/agent/loop_*.md`，如有疑问可 Read 回查。
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
  "promptId": "0c0a6f6d-d78b-4b03-8680-398f20c1fe93",
  "type": "user",
  "uuid": "b29cb7cb-5021-483e-9762-2c9d81c2eb1b",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/agent_13c7b466",
  "sessionId": "16904510-f7d3-4b77-af37-09307a65997c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-15T00:21:51.355Z_

```json
{
  "parentUuid": "b29cb7cb-5021-483e-9762-2c9d81c2eb1b",
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
  "uuid": "677446ea-9bf7-4cc1-b969-ad67d09fd8ee",
  "timestamp": "2026-05-15T00:21:51.355Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/agent_13c7b466",
  "sessionId": "16904510-f7d3-4b77-af37-09307a65997c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-15T00:21:51.356Z_

```json
{
  "parentUuid": "677446ea-9bf7-4cc1-b969-ad67d09fd8ee",
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
  "uuid": "2829ed4f-5569-4bf9-aff9-6669fa9c12c6",
  "timestamp": "2026-05-15T00:21:51.356Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/agent_13c7b466",
  "sessionId": "16904510-f7d3-4b77-af37-09307a65997c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6 · 2026-05-15T00:21:51.356Z_

```json
{
  "parentUuid": "2829ed4f-5569-4bf9-aff9-6669fa9c12c6",
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
  "uuid": "777aa9a6-cac0-4cbf-a14c-32c74f3d2af0",
  "timestamp": "2026-05-15T00:21:51.356Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/agent_13c7b466",
  "sessionId": "16904510-f7d3-4b77-af37-09307a65997c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 7 · 2026-05-15T00:21:51.356Z_

```json
{
  "parentUuid": "777aa9a6-cac0-4cbf-a14c-32c74f3d2af0",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "6402d958-b019-4c3d-8c56-054cde4b35f4",
  "timestamp": "2026-05-15T00:21:51.356Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/agent_13c7b466",
  "sessionId": "16904510-f7d3-4b77-af37-09307a65997c",
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
  "aiTitle": "Diagnose kl001_r4 failure and manage GPU allocation",
  "sessionId": "16904510-f7d3-4b77-af37-09307a65997c"
}
```

---
