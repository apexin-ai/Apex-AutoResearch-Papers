# Research conversation: [HANDOFF] 你是 Main Agent，这是 Loop #11。 ## 上一轮交接 (task_context) ### 1. 🔴 硬约束 / 红线 - GPU 白名单：仅 `autodl-simgate:cuda:0` 和 `au

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 7
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-1/09fd7d0d-546a-44c4-83c4-190ff2fc3404.jsonl`
- **Structured JSON:** [`8c74a618762180765a6f.json`](../../sessions/8c/8c74a618762180765a6f.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-15T00:20:22.266Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-15T00:20:22.266Z",
  "sessionId": "09fd7d0d-546a-44c4-83c4-190ff2fc3404",
  "content": "[HANDOFF] 你是 Main Agent，这是 Loop #11。\n\n## 上一轮交接 (task_context)\n\n### 1. 🔴 硬约束 / 红线\n- GPU 白名单：仅 `autodl-simgate:cuda:0` 和 `autodl-simgate:cuda:1`（westb-13313），禁止使用其他 GPU\n- 论文 Table 1 数字必须来自 `eval_end_to_end.py`，不可用 `eval_implicit_router.py` 的数字（-12.84 已废弃，正确值 -10.70）\n- 唯一可用训练数据文件：`data/plan-004-implicit/implicit_sft.jsonl`（MD5: c9b59e04de78, 2040 samples）。`results/plan_c_test_labels/implicit_sft.jsonl` 标签损坏（D026），绝对不可使用\n- Qwen3 推理必须 `enable_thinking=False` + `re.sub` 兜底清理 `&lt;think>` tags，否则 eval 结果不可靠\n- Checkpoint 路径：`checkpoints/plan-004-implicit/final_adapter` = ablation-b（成功的 router）。`checkpoints/plan-002-generative-v1/final_adapter` = gen-v1（失败），两者 eval metrics 相似易混淆\n\n### 2. 🖥️ 基础设施快照\n- 服务器：westb-13313，账号 root，工作目录 `/root/autodl-tmp/simgate-modular-routing`\n- Python 环境：conda base（aml-train 镜像），`/root/miniconda3/bin/python`。不要创建 venv\n- GPU：2× RTX 5090 32GB（cuda:0, cuda:1），当前均空闲\n- 活跃进程：无。0 tmux session，0 cron 任务\n- Worker 池：0（report.md 注\"后端无可用账号\"）\n- AutoDL 注意：pip/git 前 `source /etc/network_turbo`；HF 下载设 `HF_HOME=/root/autodl-tmp/.hf_cache` + `HF_HUB_DISABLE_XET=1`\n\n### 3. 📊 当前状态\n**论文阶段**：R3 审稿已提交（D049, Weak Accept - Findings 3.25/5），等待 R3 结果。R2 的 3 个 Blockers 全部修复完成（标题 scope / train-test split / penalty sensitivity）。本地编译通过：7 页（正文 4p + 非计入 3p），0 warnings，22 bib entries。\n\n**实验全部终态**：58 experiments — 22 success / 13 negative / 10 failed / 13 killed，0 RUNNING / 0 PREPARING。所有 plan 级实验要么 DONE 要么 planned（未启动的 P1/P2 优先级：plan-002 router SFT, plan-005 routing pattern analysis, plan-006/008/009/010 均 planned 但非 critical path）。\n\n**上一轮完成项**：\n- alfworld-counterfactual-full 完成（det 27.4% vs int 3.0%），结果写入 Limitations + Conclusion\n- 修复 2 处断引用 + 全文数字一致性验证通过\n- R2→R3 所有修复（B1-B3, S1-S8）已完成并提交\n\n**等待中**：无 Worker / Cron 回调。等待 R3 审稿结果返回。\n\n### 4. 📋 待办（条件触发式）\n- R3 审稿结果返回 → 读 review 内容，分叉：Accept → camera-ready 准备；Revision requested → 按 action matrix 逐条修复\n- Director 要求远程同步 → spawn Worker rsync 本地→westb-13313 + 远程 pdflatex 编译验证\n- Director 要求最终 PDF 视觉检查 → spawn Worker 用 paper-visual-review skill\n- 5/23 到达 → 终稿锁定 + ARR 提交流程（需 Director 确认）\n- Director 要求补充实验（如 plan-005 routing pattern analysis）→ 两张 GPU 空闲可立即启动\n- 收到 `[WRITE HANDOFF]` → 立即写 handoff，不做其他事\n\n### 5. 🎯 战略上下文\n**核心结论链**：D013（pivot to analysis paper）→ D033（Option B: 方法论贡献 framing）→ D046（撤销 method paper pivot，回归 analysis paper）→ D049（R3 camera-ready）。论文贡献 = counterfactual 分析方法论 + death avoidance empirical finding（DAF=90.41%, r=0.9698）。Router 本身 balanced_acc=58.1±0.8%（仅比随机高 8pp）IS the finding，不要描述为\"成功的 router\"。\n\n**易错点**：\n1. 不要把 router 的 near-random performance 描述为失败——这正是 C1 的核心证据（death avoidance 主导，router 几乎无非死亡信号可学）\n2. plan-004 v5（implicit routing）conclusion=negative，logit 级 balanced_acc=79% 但 generation 级退化到 41%——根因是 ga=1 导致 effective batch=4 过拟合。ablation-b 用 ga=8（effective batch=32）无此问题\n3. Oracle routing 仅比 always-det 好 2.89 分（-6.58 vs -9.47），96.2% episode 也选 det——这直接支撑 C1\n4. 文献新颖性已确认（12 篇扫描无 direct competitor），但论文必须有 dedicated Related Work section 对标 Toolformer/ART/Chameleon/CogRouter\n5. MATH track（plan-009）和 ALFWorld 均为 exploratory，MATH 反转信号（D045）否定了统一 router 前提，只作 Discussion 素材\n\n## 可查的历史\n前 72 轮 handoff 在 `task_context/history/agent/loop_*.md`，如有疑问可 Read 回查。\n完整聊天归档可用 `recall_session_history(\"关键词\")` 搜索。\n\n## 第一个动作要求\n1. 用 `read_registry` 确认当前 RUNNING/PREPARING 实验状态（防止幻觉记忆过时状态）\n2. 回复一句话确认你看到了上面的硬约束 + 当前活跃实验，再开始任何工具调用"
}
```

---

### Runtime record

_source line 2 · 2026-05-15T00:20:22.273Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-15T00:20:22.273Z",
  "sessionId": "09fd7d0d-546a-44c4-83c4-190ff2fc3404"
}
```

---

## Round 1

5 recorded events

### User

_source line 3 · 2026-05-15T00:20:22.323Z_

[HANDOFF] 你是 Main Agent，这是 Loop #11。

## 上一轮交接 (task_context)

### 1. 🔴 硬约束 / 红线
- GPU 白名单：仅 `autodl-simgate:cuda:0` 和 `autodl-simgate:cuda:1`（westb-13313），禁止使用其他 GPU
- 论文 Table 1 数字必须来自 `eval_end_to_end.py`，不可用 `eval_implicit_router.py` 的数字（-12.84 已废弃，正确值 -10.70）
- 唯一可用训练数据文件：`data/plan-004-implicit/implicit_sft.jsonl`（MD5: c9b59e04de78, 2040 samples）。`results/plan_c_test_labels/implicit_sft.jsonl` 标签损坏（D026），绝对不可使用
- Qwen3 推理必须 `enable_thinking=False` + `re.sub` 兜底清理 `&lt;think>` tags，否则 eval 结果不可靠
- Checkpoint 路径：`checkpoints/plan-004-implicit/final_adapter` = ablation-b（成功的 router）。`checkpoints/plan-002-generative-v1/final_adapter` = gen-v1（失败），两者 eval metrics 相似易混淆

### 2. 🖥️ 基础设施快照
- 服务器：westb-13313，账号 root，工作目录 `/root/autodl-tmp/simgate-modular-routing`
- Python 环境：conda base（aml-train 镜像），`/root/miniconda3/bin/python`。不要创建 venv
- GPU：2× RTX 5090 32GB（cuda:0, cuda:1），当前均空闲
- 活跃进程：无。0 tmux session，0 cron 任务
- Worker 池：0（report.md 注"后端无可用账号"）
- AutoDL 注意：pip/git 前 `source /etc/network_turbo`；HF 下载设 `HF_HOME=/root/autodl-tmp/.hf_cache` + `HF_HUB_DISABLE_XET=1`

### 3. 📊 当前状态
**论文阶段**：R3 审稿已提交（D049, Weak Accept - Findings 3.25/5），等待 R3 结果。R2 的 3 个 Blockers 全部修复完成（标题 scope / train-test split / penalty sensitivity）。本地编译通过：7 页（正文 4p + 非计入 3p），0 warnings，22 bib entries。

**实验全部终态**：58 experiments — 22 success / 13 negative / 10 failed / 13 killed，0 RUNNING / 0 PREPARING。所有 plan 级实验要么 DONE 要么 planned（未启动的 P1/P2 优先级：plan-002 router SFT, plan-005 routing pattern analysis, plan-006/008/009/010 均 planned 但非 critical path）。

**上一轮完成项**：
- alfworld-counterfactual-full 完成（det 27.4% vs int 3.0%），结果写入 Limitations + Conclusion
- 修复 2 处断引用 + 全文数字一致性验证通过
- R2→R3 所有修复（B1-B3, S1-S8）已完成并提交

**等待中**：无 Worker / Cron 回调。等待 R3 审稿结果返回。

### 4. 📋 待办（条件触发式）
- R3 审稿结果返回 → 读 review 内容，分叉：Accept → camera-ready 准备；Revision requested → 按 action matrix 逐条修复
- Director 要求远程同步 → spawn Worker rsync 本地→westb-13313 + 远程 pdflatex 编译验证
- Director 要求最终 PDF 视觉检查 → spawn Worker 用 paper-visual-review skill
- 5/23 到达 → 终稿锁定 + ARR 提交流程（需 Director 确认）
- Director 要求补充实验（如 plan-005 routing pattern analysis）→ 两张 GPU 空闲可立即启动
- 收到 `[WRITE HANDOFF]` → 立即写 handoff，不做其他事

### 5. 🎯 战略上下文
**核心结论链**：D013（pivot to analysis paper）→ D033（Option B: 方法论贡献 framing）→ D046（撤销 method paper pivot，回归 analysis paper）→ D049（R3 camera-ready）。论文贡献 = counterfactual 分析方法论 + death avoidance empirical finding（DAF=90.41%, r=0.9698）。Router 本身 balanced_acc=58.1±0.8%（仅比随机高 8pp）IS the finding，不要描述为"成功的 router"。

**易错点**：
1. 不要把 router 的 near-random performance 描述为失败——这正是 C1 的核心证据（death avoidance 主导，router 几乎无非死亡信号可学）
2. plan-004 v5（implicit routing）conclusion=negative，logit 级 balanced_acc=79% 但 generation 级退化到 41%——根因是 ga=1 导致 effective batch=4 过拟合。ablation-b 用 ga=8（effective batch=32）无此问题
3. Oracle routing 仅比 always-det 好 2.89 分（-6.58 vs -9.47），96.2% episode 也选 det——这直接支撑 C1
4. 文献新颖性已确认（12 篇扫描无 direct competitor），但论文必须有 dedicated Related Work section 对标 Toolformer/ART/Chameleon/CogRouter
5. MATH track（plan-009）和 ALFWorld 均为 exploratory，MATH 反转信号（D045）否定了统一 router 前提，只作 Discussion 素材

## 可查的历史
前 72 轮 handoff 在 `task_context/history/agent/loop_*.md`，如有疑问可 Read 回查。
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
  "promptId": "7d4ca4a4-678c-46a8-9502-ac6b00ee9ac0",
  "type": "user",
  "uuid": "7f71f462-3ddd-481a-a29c-e435978719e4",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/agent_182dcd53",
  "sessionId": "09fd7d0d-546a-44c4-83c4-190ff2fc3404",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-15T00:20:22.321Z_

```json
{
  "parentUuid": "7f71f462-3ddd-481a-a29c-e435978719e4",
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
  "uuid": "9afcf13c-97e8-443b-8a3b-95cc36e9cbfb",
  "timestamp": "2026-05-15T00:20:22.321Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/agent_182dcd53",
  "sessionId": "09fd7d0d-546a-44c4-83c4-190ff2fc3404",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-15T00:20:22.322Z_

```json
{
  "parentUuid": "9afcf13c-97e8-443b-8a3b-95cc36e9cbfb",
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
  "uuid": "a3370074-19bc-471b-b072-1e6f140c9069",
  "timestamp": "2026-05-15T00:20:22.322Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/agent_182dcd53",
  "sessionId": "09fd7d0d-546a-44c4-83c4-190ff2fc3404",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6 · 2026-05-15T00:20:22.322Z_

```json
{
  "parentUuid": "a3370074-19bc-471b-b072-1e6f140c9069",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "e1c5af76-51df-4d7f-bbd5-c4ad38a68356",
  "timestamp": "2026-05-15T00:20:22.322Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/agent_182dcd53",
  "sessionId": "09fd7d0d-546a-44c4-83c4-190ff2fc3404",
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
  "aiTitle": "Await R3 review results and manage paper revisions",
  "sessionId": "09fd7d0d-546a-44c4-83c4-190ff2fc3404"
}
```

---
