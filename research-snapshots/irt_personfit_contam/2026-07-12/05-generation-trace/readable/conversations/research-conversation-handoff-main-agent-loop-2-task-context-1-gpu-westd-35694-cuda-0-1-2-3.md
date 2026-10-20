# Research conversation: [HANDOFF] 你是 Main Agent，这是 Loop #2。 ## 上一轮交接 (task_context) ### 1. 🔴 硬约束 / 红线 - GPU 白名单: westd-35694 的 cuda:0/1/2/3，不可用其

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination? (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 43
- **Recorded user turns:** 1
- **Tool calls:** 10
- **Original source:** `logs/chats/exported-trajectories/account-3/465c36a7-990a-4437-ba2f-9fd3ebf0f8ef.jsonl`
- **Structured JSON:** [`422961a760a1b6b4a45b.json`](../../sessions/42/422961a760a1b6b4a45b.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-21T13:06:44.556Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-21T13:06:44.556Z",
  "sessionId": "465c36a7-990a-4437-ba2f-9fd3ebf0f8ef",
  "content": "[HANDOFF] 你是 Main Agent，这是 Loop #2。\n\n## 上一轮交接 (task_context)\n\n### 1. 🔴 硬约束 / 红线\n- GPU 白名单: westd-35694 的 cuda:0/1/2/3，不可用其他设备\n- Llama 模型路径来自 ModelScope (`LLM-Research/Meta-Llama-3.1-8B-Instruct`)，不是 HuggingFace 直接下载\n- ctrl-contam-llama 的 clean baseline 只有 1 个 seed（不像 Qwen pilot 有 3 seeds），Cohen's d 计算需要不同分母策略（或复用 Qwen clean variance）\n- WANDB_MODE=disabled（所有 Llama 实验），指标只在本地 log 里，不要去 W&B 查\n- PSN-IRT 4PL 参数文件在 `/root/autodl-tmp/ctrl_contam_pilot/` 下（Qwen pilot 目录），Llama 实验也用同一套 item params\n\n### 2. 🖥️ 基础设施快照\n- 服务器: westd-35694, account: root, 4× RTX PRO 6000 Blackwell 96GB\n- Python: `/root/miniconda3/bin/python`，激活: `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`\n- Qwen pilot 目录: `/root/autodl-tmp/ctrl_contam_pilot/`（checkpoints/, results/, data/）\n- Llama 实验目录: `/root/autodl-tmp/ctrl_contam_llama/`（train.py, data/, logs/, checkpoints/）\n- Cron 日志目录: `/root/runs/irt_personfit_contam/`\n- 磁盘: 根分区 879GB (97% free), /autodl-pub 7.3T (73% free)\n- HF_HOME 应设为 `/root/autodl-tmp/.hf_cache`\n- 活跃进程: exp-ctrl-contam-llama-clean 在 registry 标记为 RUNNING (cuda:0)，但 resource-usage 显示 0 GPU 实际在跑——**下一个你需要先 SSH 确认 clean 是否还活着**\n\n### 3. 📊 当前状态\n**刚做完**: Session 初始化 + 收到 contam15 CRON 回调。已 spawn Worker (`worker_analysis_ctrl-contam-llama-results_20260520T210404`) 去 SSH 读取 contam15 + contam50 的训练日志和 eval 结果。\n\n**等待中的回调**:\n- Worker `analysis:ctrl-contam-llama-results` — 正在分析 contam15 + contam50 结果，完成后会回调\n- contam50 也有 on_complete hook 但 CRON 消息可能已被本 session 的 contam15 回调覆盖\n\n**Registry 状态**:\n- `exp-ctrl-contam-llama-clean`: RUNNING (cuda:0) — 可能已完成但未更新\n- `exp-ctrl-contam-llama-contam15`: PREPARING → 实际已完成，等 Worker 分析后转 DONE\n- `exp-ctrl-contam-llama-contam50`: PREPARING → 实际已完成，等 Worker 分析后转 DONE\n- `exp-ctrl-contam-llama`: PREPARING — 伞实验，3 个子条件跑完后需要汇总\n- 其余 DONE 实验 21 个（15 success, 6 negative）\n\n**未回复的 Director 指令**: 无。上次 Director 决策 D016 已执行（启动 Llama 跨家族实验）。\n\n### 4. 📋 待办（条件触发式）\n- Worker `analysis:ctrl-contam-llama-results` 回调 → 读取结果 → update_registry(contam15, contam50) 设 metrics + conclusion + checkpoint_path + log_path → 刷新 report.md\n- clean 实验确认完成 → 同样 spawn Worker 分析 → 有了 Llama clean baseline 才能计算 Llama 自身的 Cohen's d\n- 三个条件全部 DONE → 汇总 Llama vs Qwen 对比，update exp-ctrl-contam-llama 伞实验 → 向 Director 汇报跨模型泛化结论\n- 如果 Llama Δlz* 效应与 Qwen comparable（|d| > 1.0）→ hypothesis confirmed，REV-ADD-2 已回答，评分预期 +0.25\n- 如果 Llama 效应显著弱于 Qwen → negative，需要推导原因（模型架构差异? tokenizer 差异?）\n- ARR DDL 仍未确认（5/25 vs 6/15）→ 全局阻塞写作节奏，Director 在等用户回复\n- Figure 2 修正（PCHIP → 真实 power function）仍未完成，M005 CRITICAL\n\n### 5. 🎯 战略上下文\n**核心 story**: lz* 作为 LLM benchmark contamination 的最小信息检测方法。4PL IRT 的 d 参数是关键（3PL 检测力减半）。已有 Qwen pilot 强结果（|d|=3.58），Llama 实验是跨模型泛化的最后一块拼图。\n\n**决策链关键节点**:\n- D016: 启动 Llama 跨家族实验\n- D015: ctrl-contam-pilot 为 partial（H1✓H2✓H3✗H4✗），θ-shift 是方法论贡献，θ-fixed 恢复单调性\n- D014: Claim 结构重组，universal misfit 从 Claim 1 → Claim 3\n- D010: Leaderboard audit 降级为描述性（Path D IRT refit 失败）\n\n**易错点**:\n- contam15/contam50 在 registry 里 status=PREPARING（不是 ANALYZING），因为 cron 系统标记了 finished_at 但可能没转 status——Worker 分析完后需要手动 update_registry status→DONE\n- Qwen pilot 的 θ-shift 现象：contam_50 的 lz_free 反而比 contam_15 更接近 clean（因为 θ 漂移），必须用 θ_fixed 分析才能看到单调剂量-反应。Llama 可能有同样现象\n- exp-ctrl-contam-llama 是伞实验（PREPARING），三个子条件（clean/contam15/contam50）是独立 registry 条目\n- 写 paper 前 Figure 2 PCHIP 问题必须先修（M005 CRITICAL），不能发初稿带着这个问题\n\n## 项目硬约束 (memory.md 节选)\n\n## GPU 审计 (2026-05-21 15:47 UTC)\n\n### GPU 占用总览\n| GPU | PID | Process | VRAM | Status |\n|-----|------|---------|------|--------|\n| 0 | 98622 | eval_lz.py --condition clean_s5 --gpu 0 | 8,628 MiB | **ZOMBIE** — s5 results 已存在 |\n| 0 | 99214 | train.py --condition clean_s7 --gpu 3 | 37,694 MiB | 运行中, 56/939 steps (~6%) |\n| 1 | 96745 | train.py --condition clean_s6 --gpu 0 | 23,102 MiB | **ZOMBIE** — 训练已完成，模型已保存 |\n| 2 | 97791 | train_grpo.py | 8,062 MiB | 运行中, 134/14042 steps (~1%), ETA ~20h |\n| 3 | 99807 | train.py --condition clean_s8 --gpu 0 | 27,470 MiB | 运行中 (无日志) |\n\n### 进程状态\n- **PID 97791 (GRPO)**: 存活, step 134/14042, epoch 0.0078, ~5.1s/step, reward 0.3-0.78 波动, ETA ~19h\n- **PID 96745 (s6 train)**: 存活但已完成 — 3 epoch 训练结束, model saved to checkpoints/clean_s6, 仍占 GPU 1 23GB\n- **PID 99214 (s7 train)**: 存活, 56/939 steps (~6%), ~2s/step\n- **PID 99807 (s8 train)**: 存活, 无日志输出\n- **PID 98622 (s5 eval)**: 存活但 s5 results 已存在 — zombie\n- **PID 98896, 98897**: 已死亡\n\n### Eval 结果\n| Condition | Accuracy | θ_MLE | lz* |\n|-----------|----------|-------|-----|\n| clean_s3 | 0.6783 | -0.1068 | 9.5293 |\n| clean_s4 | 0.6786 | -0.1092 | 8.9673 |\n| clean_s5 | 0.6787 | -0.0875 | 8.5322 |\n| clean_s6 | — | — | — (训练刚完成, eval 未开始) |\n\n### HT post-RL 结果\n| Stage | Accuracy | θ_MLE | lz* | acc_seen | acc_unseen | lz*_seen | lz*_unseen |\n|-------|----------|-------|-----|----------|------------|----------|------------|\n| SFT | 0.7339 | +0.2281 | 2.914 | 0.8310 | 0.7167 | -0.395 | 3.278 |\n\nbase_results.json 也存在。\n\n### 建议操作\n1. **Kill PID 98622** — s5 eval zombie, 浪费 GPU 0 上 8.6GB\n2. **Kill PID 96745** — s6 训练已完成, 浪费 GPU 1 上 23.1GB → 释放后可启动 s6 eval\n3. s7 (GPU 0) 和 s8 (GPU 3) 正常运行中, 不动\n4. GRPO (GPU 2) 正常运行中, 不动\n5. GPU 1 清理后启动 clean_s6 eval\n\n## 可查的历史\n前 1 轮 handoff 在 `task_context/history/agent/loop_*.md`，如有疑问可 Read 回查。\n完整聊天归档可用 `recall_session_history(\"关键词\")` 搜索。\n\n## 第一个动作要求\n1. 用 `read_registry` 确认当前 RUNNING/PREPARING 实验状态（防止幻觉记忆过时状态）\n2. 回复一句话确认你看到了上面的硬约束 + 当前活跃实验，再开始任何工具调用"
}
```

---

### Runtime record

_source line 2 · 2026-05-21T13:06:44.560Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-21T13:06:44.560Z",
  "sessionId": "465c36a7-990a-4437-ba2f-9fd3ebf0f8ef"
}
```

---

## Round 1

41 recorded events

### User

_source line 3 · 2026-05-21T13:06:44.595Z_

[HANDOFF] 你是 Main Agent，这是 Loop #2。

## 上一轮交接 (task_context)

### 1. 🔴 硬约束 / 红线
- GPU 白名单: westd-35694 的 cuda:0/1/2/3，不可用其他设备
- Llama 模型路径来自 ModelScope (`LLM-Research/Meta-Llama-3.1-8B-Instruct`)，不是 HuggingFace 直接下载
- ctrl-contam-llama 的 clean baseline 只有 1 个 seed（不像 Qwen pilot 有 3 seeds），Cohen's d 计算需要不同分母策略（或复用 Qwen clean variance）
- WANDB_MODE=disabled（所有 Llama 实验），指标只在本地 log 里，不要去 W&B 查
- PSN-IRT 4PL 参数文件在 `/root/autodl-tmp/ctrl_contam_pilot/` 下（Qwen pilot 目录），Llama 实验也用同一套 item params

### 2. 🖥️ 基础设施快照
- 服务器: westd-35694, account: root, 4× RTX PRO 6000 Blackwell 96GB
- Python: `/root/miniconda3/bin/python`，激活: `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- Qwen pilot 目录: `/root/autodl-tmp/ctrl_contam_pilot/`（checkpoints/, results/, data/）
- Llama 实验目录: `/root/autodl-tmp/ctrl_contam_llama/`（train.py, data/, logs/, checkpoints/）
- Cron 日志目录: `/root/runs/irt_personfit_contam/`
- 磁盘: 根分区 879GB (97% free), /autodl-pub 7.3T (73% free)
- HF_HOME 应设为 `/root/autodl-tmp/.hf_cache`
- 活跃进程: exp-ctrl-contam-llama-clean 在 registry 标记为 RUNNING (cuda:0)，但 resource-usage 显示 0 GPU 实际在跑——**下一个你需要先 SSH 确认 clean 是否还活着**

### 3. 📊 当前状态
**刚做完**: Session 初始化 + 收到 contam15 CRON 回调。已 spawn Worker (`worker_analysis_ctrl-contam-llama-results_20260520T210404`) 去 SSH 读取 contam15 + contam50 的训练日志和 eval 结果。

**等待中的回调**:
- Worker `analysis:ctrl-contam-llama-results` — 正在分析 contam15 + contam50 结果，完成后会回调
- contam50 也有 on_complete hook 但 CRON 消息可能已被本 session 的 contam15 回调覆盖

**Registry 状态**:
- `exp-ctrl-contam-llama-clean`: RUNNING (cuda:0) — 可能已完成但未更新
- `exp-ctrl-contam-llama-contam15`: PREPARING → 实际已完成，等 Worker 分析后转 DONE
- `exp-ctrl-contam-llama-contam50`: PREPARING → 实际已完成，等 Worker 分析后转 DONE
- `exp-ctrl-contam-llama`: PREPARING — 伞实验，3 个子条件跑完后需要汇总
- 其余 DONE 实验 21 个（15 success, 6 negative）

**未回复的 Director 指令**: 无。上次 Director 决策 D016 已执行（启动 Llama 跨家族实验）。

### 4. 📋 待办（条件触发式）
- Worker `analysis:ctrl-contam-llama-results` 回调 → 读取结果 → update_registry(contam15, contam50) 设 metrics + conclusion + checkpoint_path + log_path → 刷新 report.md
- clean 实验确认完成 → 同样 spawn Worker 分析 → 有了 Llama clean baseline 才能计算 Llama 自身的 Cohen's d
- 三个条件全部 DONE → 汇总 Llama vs Qwen 对比，update exp-ctrl-contam-llama 伞实验 → 向 Director 汇报跨模型泛化结论
- 如果 Llama Δlz* 效应与 Qwen comparable（|d| > 1.0）→ hypothesis confirmed，REV-ADD-2 已回答，评分预期 +0.25
- 如果 Llama 效应显著弱于 Qwen → negative，需要推导原因（模型架构差异? tokenizer 差异?）
- ARR DDL 仍未确认（5/25 vs 6/15）→ 全局阻塞写作节奏，Director 在等用户回复
- Figure 2 修正（PCHIP → 真实 power function）仍未完成，M005 CRITICAL

### 5. 🎯 战略上下文
**核心 story**: lz* 作为 LLM benchmark contamination 的最小信息检测方法。4PL IRT 的 d 参数是关键（3PL 检测力减半）。已有 Qwen pilot 强结果（|d|=3.58），Llama 实验是跨模型泛化的最后一块拼图。

**决策链关键节点**:
- D016: 启动 Llama 跨家族实验
- D015: ctrl-contam-pilot 为 partial（H1✓H2✓H3✗H4✗），θ-shift 是方法论贡献，θ-fixed 恢复单调性
- D014: Claim 结构重组，universal misfit 从 Claim 1 → Claim 3
- D010: Leaderboard audit 降级为描述性（Path D IRT refit 失败）

**易错点**:
- contam15/contam50 在 registry 里 status=PREPARING（不是 ANALYZING），因为 cron 系统标记了 finished_at 但可能没转 status——Worker 分析完后需要手动 update_registry status→DONE
- Qwen pilot 的 θ-shift 现象：contam_50 的 lz_free 反而比 contam_15 更接近 clean（因为 θ 漂移），必须用 θ_fixed 分析才能看到单调剂量-反应。Llama 可能有同样现象
- exp-ctrl-contam-llama 是伞实验（PREPARING），三个子条件（clean/contam15/contam50）是独立 registry 条目
- 写 paper 前 Figure 2 PCHIP 问题必须先修（M005 CRITICAL），不能发初稿带着这个问题

## 项目硬约束 (memory.md 节选)

## GPU 审计 (2026-05-21 15:47 UTC)

### GPU 占用总览
| GPU | PID | Process | VRAM | Status |
|-----|------|---------|------|--------|
| 0 | 98622 | eval_lz.py --condition clean_s5 --gpu 0 | 8,628 MiB | **ZOMBIE** — s5 results 已存在 |
| 0 | 99214 | train.py --condition clean_s7 --gpu 3 | 37,694 MiB | 运行中, 56/939 steps (~6%) |
| 1 | 96745 | train.py --condition clean_s6 --gpu 0 | 23,102 MiB | **ZOMBIE** — 训练已完成，模型已保存 |
| 2 | 97791 | train_grpo.py | 8,062 MiB | 运行中, 134/14042 steps (~1%), ETA ~20h |
| 3 | 99807 | train.py --condition clean_s8 --gpu 0 | 27,470 MiB | 运行中 (无日志) |

### 进程状态
- **PID 97791 (GRPO)**: 存活, step 134/14042, epoch 0.0078, ~5.1s/step, reward 0.3-0.78 波动, ETA ~19h
- **PID 96745 (s6 train)**: 存活但已完成 — 3 epoch 训练结束, model saved to checkpoints/clean_s6, 仍占 GPU 1 23GB
- **PID 99214 (s7 train)**: 存活, 56/939 steps (~6%), ~2s/step
- **PID 99807 (s8 train)**: 存活, 无日志输出
- **PID 98622 (s5 eval)**: 存活但 s5 results 已存在 — zombie
- **PID 98896, 98897**: 已死亡

### Eval 结果
| Condition | Accuracy | θ_MLE | lz* |
|-----------|----------|-------|-----|
| clean_s3 | 0.6783 | -0.1068 | 9.5293 |
| clean_s4 | 0.6786 | -0.1092 | 8.9673 |
| clean_s5 | 0.6787 | -0.0875 | 8.5322 |
| clean_s6 | — | — | — (训练刚完成, eval 未开始) |

### HT post-RL 结果
| Stage | Accuracy | θ_MLE | lz* | acc_seen | acc_unseen | lz*_seen | lz*_unseen |
|-------|----------|-------|-----|----------|------------|----------|------------|
| SFT | 0.7339 | +0.2281 | 2.914 | 0.8310 | 0.7167 | -0.395 | 3.278 |

base_results.json 也存在。

### 建议操作
1. **Kill PID 98622** — s5 eval zombie, 浪费 GPU 0 上 8.6GB
2. **Kill PID 96745** — s6 训练已完成, 浪费 GPU 1 上 23.1GB → 释放后可启动 s6 eval
3. s7 (GPU 0) 和 s8 (GPU 3) 正常运行中, 不动
4. GRPO (GPU 2) 正常运行中, 不动
5. GPU 1 清理后启动 clean_s6 eval

## 可查的历史
前 1 轮 handoff 在 `task_context/history/agent/loop_*.md`，如有疑问可 Read 回查。
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
  "promptId": "26661264-62cc-4d8c-933c-ac64167cc12e",
  "type": "user",
  "uuid": "ec53258a-3ccb-45f6-bca5-063319c17feb",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/.claude/sessions/agent_272f846c",
  "sessionId": "465c36a7-990a-4437-ba2f-9fd3ebf0f8ef",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-21T13:06:44.595Z_

```json
{
  "parentUuid": "ec53258a-3ccb-45f6-bca5-063319c17feb",
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
      "mcp__agent-ml-research__distill_papers",
      "mcp__agent-ml-research__edit_paper_section",
      "mcp__agent-ml-research__feishu_read_tum_pending_key",
      "mcp__agent-ml-research__feishu_send_alert",
      "mcp__agent-ml-research__feishu_send_approval_card",
      "mcp__agent-ml-research__feishu_send_result_card",
      "mcp__agent-ml-research__feishu_send_tum_key_request_card",
      "mcp__agent-ml-research__fetch_wandb_metrics",
      "mcp__agent-ml-research__get_baseline_metrics",
      "mcp__agent-ml-research__get_distill_status",
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
      "mcp__agent-ml-research__read_mistakes",
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
      "mcp__agent-ml-research__distill_papers",
      "mcp__agent-ml-research__edit_paper_section",
      "mcp__agent-ml-research__feishu_read_tum_pending_key",
      "mcp__agent-ml-research__feishu_send_alert",
      "mcp__agent-ml-research__feishu_send_approval_card",
      "mcp__agent-ml-research__feishu_send_result_card",
      "mcp__agent-ml-research__feishu_send_tum_key_request_card",
      "mcp__agent-ml-research__fetch_wandb_metrics",
      "mcp__agent-ml-research__get_baseline_metrics",
      "mcp__agent-ml-research__get_distill_status",
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
      "mcp__agent-ml-research__read_mistakes",
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
  "uuid": "3f1c9c7d-da02-46df-baf6-03ff53559a31",
  "timestamp": "2026-05-21T13:06:44.595Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/.claude/sessions/agent_272f846c",
  "sessionId": "465c36a7-990a-4437-ba2f-9fd3ebf0f8ef",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-21T13:06:44.595Z_

```json
{
  "parentUuid": "3f1c9c7d-da02-46df-baf6-03ff53559a31",
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
  "uuid": "f35d1c2b-e900-400d-9e86-0c13a5a23f14",
  "timestamp": "2026-05-21T13:06:44.595Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/.claude/sessions/agent_272f846c",
  "sessionId": "465c36a7-990a-4437-ba2f-9fd3ebf0f8ef",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6 · 2026-05-21T13:06:44.595Z_

```json
{
  "parentUuid": "f35d1c2b-e900-400d-9e86-0c13a5a23f14",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "81767060-a54c-4274-af8a-816f9393ceac",
  "timestamp": "2026-05-21T13:06:44.595Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/.claude/sessions/agent_272f846c",
  "sessionId": "465c36a7-990a-4437-ba2f-9fd3ebf0f8ef",
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
  "aiTitle": "Confirm Llama clean status and analyze contam results",
  "sessionId": "465c36a7-990a-4437-ba2f-9fd3ebf0f8ef"
}
```

---

### Assistant

_source line 8 · 2026-05-21T13:06:54.704Z_

<details><summary>Logged reasoning block</summary>

```text
Let me start by understanding the handoff context. I'm the Main Agent in Loop #2. I need to:

1. First, run session-start: read_registry, reconcile_crons, read report.md, read ROADMAP.md
2. Confirm I've read the handoff constraints
3. Figure out what needs to be done next

Key things from handoff:
- Server: westd-35694, 4× RTX PRO 6000 Blackwell 96GB
- Llama experiments: clean (possibly done), contam15 (done), contam50 (done)
- Worker analyzing contam15+contam50 results


- GPU audit shows zombie processes on GPU 0 and GPU 1, with GRPO running on GPU 2, s7 on GPU 0, and s8 on GPU 3
- Clean seeds s3-s8 are running for the multi-seed clean baseline

Now I'll run the session-start protocol to read the registry, reconcile any cron jobs, and check the report and roadmap files.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "81767060-a54c-4274-af8a-816f9393ceac",
  "isSidechain": false,
  "requestId": "req_011CbFmJ1KVBFzcnuczeQUG4",
  "type": "assistant",
  "uuid": "efab152c-e8b9-4cec-8916-8a5feb54972b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/.claude/sessions/agent_272f846c",
  "sessionId": "465c36a7-990a-4437-ba2f-9fd3ebf0f8ef",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0174hrxWMZfLoPD9q3KFBYuD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 28451,
      "cache_read_input_tokens": 11841,
      "output_tokens": 525,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 28451,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 525,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 28451,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 28451
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

_source line 9 · 2026-05-21T13:06:57.885Z_

确认收到 handoff。硬约束已读：GPU 白名单 westd-35694 cuda:0-3，Llama 用 ModelScope 路径，WANDB_MODE=disabled，PSN-IRT 4PL 参数复用 Qwen pilot 目录。当前活跃：clean 可能已完成待确认，contam15/contam50 等 Worker 分析回调，GRPO 在 GPU 2 跑着。

执行 session-start 初始化。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "efab152c-e8b9-4cec-8916-8a5feb54972b",
  "isSidechain": false,
  "requestId": "req_011CbFmJ1KVBFzcnuczeQUG4",
  "type": "assistant",
  "uuid": "a6ffa323-407f-41b0-8753-e67add8c02e8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/.claude/sessions/agent_272f846c",
  "sessionId": "465c36a7-990a-4437-ba2f-9fd3ebf0f8ef",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0174hrxWMZfLoPD9q3KFBYuD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 28451,
      "cache_read_input_tokens": 11841,
      "output_tokens": 525,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 28451,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 525,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 28451,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 28451
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

_source line 10 · 2026-05-21T13:06:59.382Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01EmyaU4QexYpkghWJoGerve`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__reconcile_crons,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__read_roadmap",
  "max_results": 4
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a6ffa323-407f-41b0-8753-e67add8c02e8",
  "isSidechain": false,
  "requestId": "req_011CbFmJ1KVBFzcnuczeQUG4",
  "type": "assistant",
  "uuid": "00902671-07a3-4d4f-835e-55bdb6412f5a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/.claude/sessions/agent_272f846c",
  "sessionId": "465c36a7-990a-4437-ba2f-9fd3ebf0f8ef",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0174hrxWMZfLoPD9q3KFBYuD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 28451,
      "cache_read_input_tokens": 11841,
      "output_tokens": 525,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 28451,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 525,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 28451,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 28451
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

_source line 11 · 2026-05-21T13:06:59.389Z_

<details><summary>↩ Tool result · `toolu_01EmyaU4QexYpkghWJoGerve`</summary>

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
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "00902671-07a3-4d4f-835e-55bdb6412f5a",
  "isSidechain": false,
  "promptId": "26661264-62cc-4d8c-933c-ac64167cc12e",
  "type": "user",
  "uuid": "9d73a546-1169-416c-b01c-072b91c74a24",
  "toolUseResult": {
    "matches": [
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__reconcile_crons",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__read_roadmap"
    ],
    "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__reconcile_crons,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__read_roadmap",
    "total_deferred_tools": 82
  },
  "sourceToolAssistantUUID": "00902671-07a3-4d4f-835e-55bdb6412f5a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/.claude/sessions/agent_272f846c",
  "sessionId": "465c36a7-990a-4437-ba2f-9fd3ebf0f8ef",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 12_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[HANDOFF] 你是 Main Agent，这是 Loop #2。  ## 上一轮交接 (task_context)  ### 1. 🔴 硬约束 / 红线 - GPU 白名单: westd-35694 的 cuda:0/1/2/3，不可用其他设备 - Llama 模型路径来自 ModelScope (`LLM-Research/Meta-Llama-3.1-8B-Instruct`)，不是…",
  "leafUuid": "9d73a546-1169-416c-b01c-072b91c74a24",
  "sessionId": "465c36a7-990a-4437-ba2f-9fd3ebf0f8ef"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Confirm Llama clean status and analyze contam results",
  "sessionId": "465c36a7-990a-4437-ba2f-9fd3ebf0f8ef"
}
```

---

### Tool call

_source line 14 · 2026-05-21T13:07:02.347Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01LE6CMrod3WtnhbFTQ3V4fB`</summary>

```json
{
  "project": "irt_personfit_contam",
  "limit": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9d73a546-1169-416c-b01c-072b91c74a24",
  "isSidechain": false,
  "requestId": "req_011CbFmK6YHvNMn4Xe3YdHmT",
  "type": "assistant",
  "uuid": "19525180-0ca9-476c-84ae-28beb29fd7e3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/.claude/sessions/agent_272f846c",
  "sessionId": "465c36a7-990a-4437-ba2f-9fd3ebf0f8ef",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XHzM1ZgmhqqMqwV3T3N1tD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1403,
      "cache_read_input_tokens": 40292,
      "output_tokens": 243,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1403,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 243,
          "cache_read_input_tokens": 40292,
          "cache_creation_input_tokens": 1403,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1403
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

_source line 15 · 2026-05-21T13:07:02.371Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__reconcile_crons · `toolu_01P171D6i6EMt1fS6w3mPsyL`</summary>

```json
{}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "19525180-0ca9-476c-84ae-28beb29fd7e3",
  "isSidechain": false,
  "requestId": "req_011CbFmK6YHvNMn4Xe3YdHmT",
  "type": "assistant",
  "uuid": "78acfe90-aca1-483b-abe5-abc0d9b3da69",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/.claude/sessions/agent_272f846c",
  "sessionId": "465c36a7-990a-4437-ba2f-9fd3ebf0f8ef",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XHzM1ZgmhqqMqwV3T3N1tD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1403,
      "cache_read_input_tokens": 40292,
      "output_tokens": 243,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1403,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 243,
          "cache_read_input_tokens": 40292,
          "cache_creation_input_tokens": 1403,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1403
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

_source line 16 · 2026-05-21T13:07:02.626Z_

<details><summary>↩ Tool result · `toolu_01LE6CMrod3WtnhbFTQ3V4fB`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {\"exp-arcc-clean-s10\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T12:48:49.366Z\", \"updated_at\": \"2026-05-21T13:05:54.577Z\", \"hypothesis\": \"ARC-Challenge clean baseline (seed=307) for cross-benchmark Cohen's d — expanding clean lz* distribution\", \"parent\": \"exp-arcc-benchmark\", \"conclusion\": \"success\", \"metrics\": {\"theta_mle\": 0.8111, \"lz_star\": -5.0733, \"accuracy\": 0.9051, \"n_items\": 295}}, \"exp-arcc-clean-s9\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T12:48:48.480Z\", \"updated_at\": \"2026-05-21T13:05:53.688Z\", \"hypothesis\": \"ARC-Challenge clean baseline (seed=306) for cross-benchmark Cohen's d — expanding clean lz* distribution\", \"parent\": \"exp-arcc-benchmark\", \"conclusion\": \"success\", \"metrics\": {\"theta_mle\": 0.8868, \"lz_star\": -5.5359, \"accuracy\": 0.9017, \"n_items\": 295}}, \"exp-arcc-clean-s8\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T12:48:47.531Z\", \"updated_at\": \"2026-05-21T13:05:52.824Z\", \"hypothesis\": \"ARC-Challenge clean baseline (seed=305) for cross-benchmark Cohen's d — expanding clean lz* distribution\", \"parent\": \"exp-arcc-benchmark\", \"conclusion\": \"success\", \"metrics\": {\"theta_mle\": 0.8511, \"lz_star\": -5.4001, \"accuracy\": 0.9051, \"n_items\": 295}}, \"exp-arcc-clean-s7\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T12:48:46.522Z\", \"updated_at\": \"2026-05-21T13:05:51.824Z\", \"hypothesis\": \"ARC-Challenge clean baseline (seed=304) for cross-benchmark Cohen's d — expanding clean lz* distribution\", \"parent\": \"exp-arcc-benchmark\", \"conclusion\": \"success\", \"metrics\": {\"theta_mle\": 0.7058, \"lz_star\": -5.5852, \"accuracy\": 0.8915, \"n_items\": 295}}, \"exp-ctrl-contam-llama-clean-s10\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-21T13:03:57.523Z\", \"updated_at\": \"2026-05-21T13:04:26.843Z\", \"hypothesis\": \"Independent clean Llama-3.1-8B-Instruct baseline (seed=307) for n=10 Cohen's d variance estimation\", \"parent\": \"exp-ctrl-contam-llama-contam15\"}, \"exp-ctrl-contam-llama-clean-s9\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-21T13:03:56.214Z\", \"updated_at\": \"2026-05-21T13:04:25.842Z\", \"hypothesis\": \"Independent clean Llama-3.1-8B-Instruct baseline (seed=306) for n=10 Cohen's d variance estimation\", \"parent\": \"exp-ctrl-contam-llama-contam15\"}, \"exp-ctrl-contam-llama-clean-s8\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-21T13:03:54.282Z\", \"updated_at\": \"2026-05-21T13:04:24.947Z\", \"hypothesis\": \"Independent clean Llama-3.1-8B-Instruct baseline (seed=305) for n=10 Cohen's d variance estimation\", \"parent\": \"exp-ctrl-contam-llama-contam15\"}, \"eval-mistral-clean-s3\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T12:59:20.651Z\", \"updated_at\": \"2026-05-21T13:00:42.054Z\", \"hypothesis\": \"Mistral clean_s3 (seed 3) LoRA adapter trained on clean MMLU data will show lz* near zero, consistent with no contamination signal in the IRT person-fit framework.\", \"metrics\": {\"theta_mle\": -0.9733, \"lz_star\": 3.2792, \"accuracy_overall\": 0.5413, \"n_items\": 14042}, \"conclusion\": \"success\"}, \"eval-mistral-clean-s2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T12:59:19.645Z\", \"updated_at\": \"2026-05-21T13:00:41.390Z\", \"hypothesis\": \"Mistral clean_s2 (seed 2) LoRA adapter trained on clean MMLU data will show lz* near zero, consistent with no contamination signal in the IRT person-fit framework.\", \"metrics\": {\"theta_mle\": -0.9627, \"lz_star\": -1.0456, \"accuracy_overall\": 0.5428, \"n_items\": 14042}, \"conclusion\": \"success\"}, \"exp-post-rl-v3\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-21T12:45:42.860Z\", \"updated_at\": \"2026-05-21T12:47:34.274Z\", \"hypothesis\": \"GRPO with num_generations=16 + temperature=1.2 produces measurable parameter update while preserving lz* contamination signal (R7 post-RL robustness)\", \"parent\": \"exp-post-rl\"}, \"exp-post-rl\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T03:55:49.080Z\", \"updated_at\": \"2026-05-21T12:47:18.550Z\", \"hypothesis\": \"Post-RL (GRPO) training does not wash out contamination signal detectable by lz*: SFT-contaminated model retains negative Δlz* after GRPO alignment, demonstrating that IRT-based detection is robust to RL post-training — addressing reviewer concern R7 about SFT-only scope\", \"notes\": \"GRPO v1/v2 reward saturation (frac_reward_zero_std=1.0), zero gradient, model ≈ SFT. Restarting as exp-post-rl-v3 with fixed params (num_generations=16, temperature=1.2, max_steps=3000, save_steps=500).\", \"conclusion\": \"negative\"}, \"exp-ctrl-contam-llama-clean-s7\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T12:42:50.324Z\", \"updated_at\": \"2026-05-21T12:44:14.678Z\", \"hypothesis\": \"Clean SFT (seed 7) on Llama-3.1-8B should produce lz* near zero, indicating no person-fit anomaly without contamination.\", \"conclusion\": \"success\", \"metrics\": {\"theta_mle\": -0.6356, \"lz_star\": -0.4007, \"accuracy_overall\": 0.5929, \"n_items\": 14042}}, \"exp-ctrl-contam-llama-clean-s6\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T12:42:49.542Z\", \"updated_at\": \"2026-05-21T12:44:13.998Z\", \"hypothesis\": \"Clean SFT (seed 6) on Llama-3.1-8B should produce lz* near zero, indicating no person-fit anomaly without contamination.\", \"conclusion\": \"success\", \"metrics\": {\"theta_mle\": -0.6027, \"lz_star\": 2.8466, \"accuracy_overall\": 0.601, \"n_items\": 14042}}, \"exp-ctrl-contam-llama-clean-s5\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T12:42:48.174Z\", \"updated_at\": \"2026-05-21T12:44:13.366Z\", \"hypothesis\": \"Clean SFT (seed 5) on Llama-3.1-8B should produce lz* near zero, indicating no person-fit anomaly without contamination.\", \"conclusion\": \"success\", \"metrics\": {\"theta_mle\": -0.63, \"lz_star\": 1.7323, \"accuracy_overall\": 0.5965, \"n_items\": 14042}}, \"exp-ctrl-contam-llama-clean-s4\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T12:24:43.970Z\", \"updated_at\": \"2026-05-21T12:44:12.382Z\", \"hypothesis\": \"Clean SFT (seed 4) on Llama-3.1-8B should produce lz* near zero, indicating no person-fit anomaly without contamination.\", \"conclusion\": \"success\", \"metrics\": {\"theta_mle\": -0.6435, \"lz_star\": 0.0206, \"accuracy_overall\": 0.5923, \"n_items\": 14042}}, \"arcc-clean-s10\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-21T12:08:37.841Z\", \"updated_at\": \"2026-05-21T12:10:04.708Z\"}, \"arcc-clean-s9\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-21T12:08:35.737Z\", \"updated_at\": \"2026-05-21T12:10:03.378Z\"}, \"arcc-clean-s8\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-21T12:08:33.697Z\", \"updated_at\": \"2026-05-21T12:10:01.469Z\"}, \"arcc-clean-s7\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-21T12:08:32.282Z\", \"updated_at\": \"2026-05-21T12:10:00.031Z\"}, \"exp-ctrl-contam-pilot\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T13:54:01.818Z\", \"updated_at\": \"2026-05-21T11:44:22.927Z\", \"hypothesis\": \"Controlled contamination via QLoRA fine-tuning on MMLU items produces measurable Δlz* signal: (1) clean-vs-clean Δlz* ≈ 0 (seed1 vs seed2), confirming the noise floor; (2) 15% contamination produces significant negative Δlz* with Cohen's d > 1.0; (3) 50% contamination produces even stronger signal; (4) contamination signal concentrates on seen items (memorization fraction > 0.5)\", \"conclusion\": \"success\", \"metrics\": {\"cohens_d_contam15\": 6.575, \"cohens_d_contam15_ci\": [4.514, 15.199], \"cohens_d_contam50\": 1.897, \"cohens_d_contam50_ci\": [1.041, 4.923], \"clean_n10_mean_lz\": 8.684, \"clean_n10_sd_lz\": 0.735, \"contam15_lz\": 3.849, \"contam50_lz\": 7.289, \"n_clean_seeds\": 10, \"n_items\": 14042}, \"notes\": \"partial: H1✓ H2✓ H3✗(θ-shift, fixed analysis restores monotonicity) H4✗(memorization<0.5). θ-fixed=-0.0965 (n=3 mean). Snijders lz* corrected: dose-response ratio=3.12 (unchanged from Drasgow). Δlz*_fixed: contam_15=+3.169, contam_50=+9.893. All values use Snijders (2001) lz*.\"}, \"exp-arcc-benchmark\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-21T08:07:05.912Z\", \"updated_at\": \"2026-05-21T11:20:59.126Z\", \"hypothesis\": \"ℓz* contamination detection generalizes beyond MMLU to ARC-Challenge, a second benchmark with PSN-IRT 4PL calibration — demonstrating cross-benchmark applicability and addressing reviewer concern about single-benchmark evaluation.\", \"notes\": \"代码就绪: /root/autodl-tmp/ctrl_contam_arcc/ (prepare_arcc_data.py + train.py + eval_lz.py + arc_c_params.csv)。ARC-C: 295 items with 4PL params (294×4-choice + 1×3-choice), 15% contam=44 items, 50% contam=147 items。预期检测力有限 (sim_001 12.9% power) 但 cross-benchmark generalization 价值明确。数据已生成。等 GPU 可用后启动。\", \"metrics\": {\"19912_clean_s1_acc\": 0.902, \"19912_clean_s1_lz\": -5.448, \"19912_clean_s2_acc\": 0.895, \"19912_clean_s2_lz\": -5.433, \"19912_contam15_acc\": 0.909, \"19912_contam15_lz\": -4.917, \"19912_contam15_lz_seen\": 0.568, \"19912_contam50_acc\": 0.942, \"19912_contam50_lz\": -4.573, \"19912_contam50_lz_seen\": -0.331, \"35694_clean_s1_acc\": 0.895, \"35694_clean_s1_lz\": -5.511, \"35694_clean_s2_acc\": 0.898, \"35694_clean_s2_lz\": -5.493, \"35694_contam15_acc\": 0.909, \"35694_contam15_lz\": -5.032, \"35694_contam15_lz_seen\": 0.186, \"35694_contam50_acc\": 0.946, \"35694_contam50_lz\": -4.185, \"35694_contam50_lz_seen\": -0.475}}, \"exp-ctrl-contam-qwen-clean-s10\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-21T09:12:35.740Z\", \"updated_at\": \"2026-05-21T11:20:55.470Z\", \"hypothesis\": \"Tenth independent clean Qwen2.5-7B-Instruct baseline (seed=307) for n=10 Cohen's d variance estimation\", \"parent\": \"exp-ctrl-contam-pilot\", \"metrics\": {\"accuracy\": 0.676, \"lz_star\": 8.149, \"theta_mle\": -0.116, \"n_items\": 14042}}, \"exp-ctrl-contam-llama-contam50\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T20:57:09.849Z\", \"updated_at\": \"2026-05-21T11:15:59.751Z\", \"hypothesis\": \"50% MMLU contamination on Llama-3.1-8B-Instruct produces measurable Δlz* signal, with expected θ-shift effects comparable to Qwen pilot\", \"conclusion\": \"success\", \"metrics\": {\"lz_star\": -3.3313, \"acc\": 0.6983, \"theta_mle\": -0.149, \"acc_seen\": 0.735, \"acc_unseen\": 0.661, \"delta_lz_star\": -3.1906, \"cohens_d_ddof1\": -3.31, \"method\": \"Snijders (2001) lz*\"}}, \"exp-ctrl-contam-llama-contam15\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T20:57:08.665Z\", \"updated_at\": \"2026-05-21T11:15:59.136Z\", \"hypothesis\": \"15% MMLU contamination on Llama-3.1-8B-Instruct produces comparable Δlz* signal to Qwen2.5-7B (pilot d=-3.58), confirming cross-model generalizability\", \"conclusion\": \"success\", \"metrics\": {\"lz_star\": -2.9922, \"acc\": 0.6654, \"theta_mle\": -0.276, \"acc_seen\": 0.742, \"acc_unseen\": 0.652, \"delta_lz_star\": -2.8515, \"cohens_d_ddof1\": -2.95, \"method\": \"Snijders (2001) lz*\"}}, \"exp-constat-comparison\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-21T08:07:04.296Z\", \"updated_at\": \"2026-05-21T10:57:28.101Z\", \"hypothesis\": \"ConStat (NeurIPS 2024) requires multi-benchmark performance scores for contamination detection, making it inapplicable or underpowered in single-benchmark scenarios. ℓz* operates on binary response patterns from a single benchmark, demonstrating superior minimal-information detection capability.\", \"notes\": \"Bugfix 完成: (1) Snijders 方差校正已加 (2) 阈值方向修正为 abs(lz)>1.96 (3) RNG 隔离。修正后 clean lz* mean=-0.058≈0。仿真结果: 绝对 lz* power≈FAR 在所有 contam 级别（θ-shift 完全吸收信号），进一步证实 Δlz* 对比设计的必要性。ConStat 真实模型对比不可行（缺 reference benchmark + ≥5 reference models）。\"}, \"exp-arcc-clean-s1\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-21T09:12:36.602Z\", \"updated_at\": \"2026-05-21T10:57:23.992Z\", \"hypothesis\": \"ARC-Challenge clean baseline (seed=42) for cross-benchmark ℓz* detection — establishing clean lz* distribution on a second benchmark with PSN-IRT 4PL calibration\", \"parent\": \"exp-arcc-benchmark\", \"metrics\": {\"accuracy\": 0.8949, \"theta_mle\": 0.6872, \"lz_star\": -5.5107, \"n_items\": 295}}, \"exp-mia-mink-comparison\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-21T08:07:05.266Z\", \"updated_at\": \"2026-05-21T10:57:22.586Z\", \"hypothesis\": \"MIA methods (Min-K%/Min-K%++) fail to detect contamination in post-RL (GRPO) models because RL fine-tuning disrupts token-level log-prob distributions, while ℓz* remains effective because it operates on response-pattern-level statistics that survive RL post-training — demonstrating robustness advantage over MIA approaches.\", \"notes\": \"代码就绪: eval_mia.py (Loss/Min-K%/Min-K%++ K=10-50, AUC-ROC) + compare_mia_lz.py。路径: /root/autodl-tmp/post_rl_contam/。需 GPU ~1-2h/stage，等 GRPO 完成后执行。\", \"metrics\": {\"base_auc_loss\": 0.486, \"base_auc_mink10\": 0.493, \"base_auc_minkpp10\": 0.488, \"sft_auc_loss\": 0.592, \"sft_auc_mink10\": 0.611, \"sft_auc_minkpp10\": 0.569}}, \"exp-arcc-clean-s2\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-21T10:17:15.804Z\", \"updated_at\": \"2026-05-21T10:17:15.804Z\"}, \"exp-ctrl-contam-qwen-clean-s9\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T08:25:55.311Z\", \"updated_at\": \"2026-05-21T09:13:10.810Z\", \"hypothesis\": \"Ninth independent clean Qwen2.5-7B-Instruct baseline (seed=306) for n=10 Cohen's d variance estimation\", \"parent\": \"exp-ctrl-contam-pilot\", \"metrics\": {\"accuracy\": 0.6743, \"lz_star\": 9.013, \"theta_mle\": -0.1242, \"n_items\": 14042}, \"conclusion\": \"success\"}, \"exp-ctrl-contam-qwen-clean-s7\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T07:42:16.770Z\", \"updated_at\": \"2026-05-21T09:13:10.213Z\", \"hypothesis\": \"Seventh independent clean Qwen2.5-7B-Instruct baseline (seed=304) for n=10 Cohen's d\", \"parent\": \"exp-ctrl-contam-pilot\", \"metrics\": {\"accuracy\": 0.6783, \"lz_star\": 8.77, \"theta_mle\": -0.0892, \"n_items\": 14042}, \"conclusion\": \"success\"}, \"exp-ctrl-contam-qwen-clean-s8\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T07:42:56.989Z\", \"updated_at\": \"2026-05-21T09:12:28.785Z\", \"hypothesis\": \"Eighth independent clean Qwen2.5-7B-Instruct baseline (seed=305) for n=10 Cohen's d\", \"parent\": \"exp-ctrl-contam-pilot\", \"notes\": \"s8 PID 99807 found dead at step 294/939. Needs restart on next available GPU. Previous run was on cuda:3 with CUDA_VISIBLE_DEVICES=3.\", \"metrics\": {\"accuracy\": 0.6768, \"lz_star\": 9.111, \"theta_mle\": -0.1035, \"n_items\": 14042, \"loss\": 1.352, \"steps\": 939}, \"conclusion\": \"success\"}, \"exp-ctrl-contam-qwen-clean-s6\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T06:56:41.860Z\", \"updated_at\": \"2026-05-21T09:12:27.846Z\", \"hypothesis\": \"Sixth independent clean Qwen2.5-7B-Instruct baseline (seed=303) for expanded n=10 Cohen's d variance estimation\", \"parent\": \"exp-ctrl-contam-pilot\", \"metrics\": {\"accuracy\": 0.6771, \"lz_star\": 8.245, \"theta_mle\": -0.1036, \"n_items\": 14042, \"loss\": 1.354, \"steps\": 939}, \"conclusion\": \"success\"}, \"exp-ctrl-contam-qwen-clean-s5\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T06:30:49.858Z\", \"updated_at\": \"2026-05-21T08:25:54.248Z\", \"hypothesis\": \"Fifth independent clean Qwen2.5-7B-Instruct baseline (seed=302) for expanded n=10 Cohen's d variance estimation\", \"parent\": \"exp-ctrl-contam-pilot\", \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 0.6787, \"lz_star\": 8.532, \"theta_mle\": -0.088, \"n_items\": 14042}}, \"exp-ctrl-contam-qwen-clean-s4\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T06:30:49.211Z\", \"updated_at\": \"2026-05-21T08:25:52.756Z\", \"hypothesis\": \"Fourth independent clean Qwen2.5-7B-Instruct baseline (seed=301) for expanded n=10 Cohen's d variance estimation, improving statistical power of contamination effect size measurement\", \"parent\": \"exp-ctrl-contam-pilot\", \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 0.6786, \"lz_star\": 8.967, \"theta_mle\": -0.109, \"n_items\": 14042}}, \"exp-ctrl-contam-mistral\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T04:21:26.398Z\", \"updated_at\": \"2026-05-21T06:50:42.866Z\", \"hypothesis\": \"Mistral-7B-Instruct-v0.3 as a third model family (distinct tokenizer and training recipe from Qwen/Llama) produces significant Δlz* under controlled contamination, further confirming cross-family detection generalizability — addressing reviewer concern R4 about limited model diversity (2 families × 1 benchmark)\", \"parent\": \"exp-ctrl-contam-pilot\", \"notes\": \"Mistral-7B-Instruct-v0.3 confirmed as latest 7B Instruct (v0.4 does not exist). Model downloaded via ModelScope. Three conditions training in parallel: clean cuda:0, contam_15 cuda:1, contam_50 cuda:3. eval_lz.py uses Snijders (2001) lz* correction.\", \"metrics\": {\"clean\": {\"lz_star\": 5.4175, \"acc\": 0.5138, \"theta\": -1.1569}, \"contam_15\": {\"lz_star\": -1.3849, \"acc\": 0.5949, \"acc_seen\": 0.7436, \"acc_unseen\": 0.5686, \"theta\": -0.7129}, \"contam_50\": {\"lz_star\": -3.1503, \"acc\": 0.6732, \"acc_seen\": 0.7523, \"acc_unseen\": 0.5941, \"theta\": -0.3027}, \"delta_lz_star_15\": -6.8024, \"delta_lz_star_50\": -8.5678, \"method\": \"Snijders (2001) lz*\"}, \"conclusion\": \"success\"}, \"exp-ctrl-contam-mistral-contam50\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T04:52:15.643Z\", \"updated_at\": \"2026-05-21T06:33:45.847Z\", \"metrics\": {\"lz_star\": -3.1503, \"acc_overall\": 0.6732, \"acc_seen\": 0.7523, \"acc_unseen\": 0.5941, \"theta_mle\": -0.3027, \"lz_star_seen\": -1.3701, \"lz_star_unseen\": -0.9972, \"method\": \"Snijders (2001) lz*\"}, \"conclusion\": \"success\", \"hypothesis\": \"A Mistral-7B model fine-tuned with 50% MMLU contamination will produce strongly aberrant person-fit (highly negative lz*) because extensive memorization creates a large discrepancy between observed and IRT-expected response patterns.\"}, \"exp-ctrl-contam-mistral-contam15\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T04:52:14.095Z\", \"updated_at\": \"2026-05-21T06:33:45.252Z\", \"metrics\": {\"lz_star\": -1.3849, \"acc_overall\": 0.5949, \"acc_seen\": 0.7436, \"acc_unseen\": 0.5686, \"theta_mle\": -0.7129, \"lz_star_seen\": -1.0838, \"lz_star_unseen\": -0.0956, \"method\": \"Snijders (2001) lz*\"}, \"conclusion\": \"success\", \"hypothesis\": \"A Mistral-7B model fine-tuned with 15% MMLU contamination will produce aberrant person-fit (negative lz*) because memorized items inflate accuracy on seen questions regardless of difficulty, violating the IRT-predicted response pattern.\"}, \"exp-ctrl-contam-mistral-clean\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T04:52:12.591Z\", \"updated_at\": \"2026-05-21T06:33:44.219Z\", \"metrics\": {\"lz_star\": 5.4175, \"acc_overall\": 0.5138, \"acc_seen\": null, \"acc_unseen\": 0.5138, \"theta_mle\": -1.1569, \"lz_star_seen\": null, \"lz_star_unseen\": 5.4175, \"method\": \"Snijders (2001) lz*\"}, \"conclusion\": \"success\", \"hypothesis\": \"A Mistral-7B model fine-tuned on clean MMLU data (no benchmark leakage) will produce a response pattern consistent with IRT expectations, yielding lz* near zero, serving as the uncontaminated baseline for comparison.\"}, \"exp-baseline-comparison\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T03:55:49.688Z\", \"updated_at\": \"2026-05-21T05:07:41.388Z\", \"hypothesis\": \"IRT-based lz* detection outperforms binary-only baselines (accuracy z-score, LR, RF classifiers) on controlled contamination data, especially at low contamination rates (15%), because lz* leverages item-level difficulty calibration unavailable to methods operating on aggregate or uncalibrated binary vectors\", \"conclusion\": \"success\", \"metrics\": {\"model_level\": {\"qwen_contam15_lz_star_d\": -3.42, \"qwen_contam50_lz_star_d\": -0.99, \"llama_contam15_lz_star_d\": -2.95, \"llama_contam50_lz_star_d\": -3.31, \"qwen_contam15_acc_zscore_d\": 160.6, \"qwen_contam15_ht_d\": 3.21, \"llama_contam15_u3_d\": -3.69}, \"item_level_auroc\": {\"lz_star_itemwise\": {\"qwen_15\": 0.536, \"qwen_50\": 0.535, \"llama_15\": 0.528, \"llama_50\": 0.536}, \"irt_residual\": {\"qwen_15\": 0.578, \"qwen_50\": 0.563, \"llama_15\": 0.582, \"llama_50\": 0.581}, \"lr_cross_model\": {\"qwen_15\": 0.586, \"qwen_50\": 0.567, \"llama_15\": 0.592, \"llama_50\": 0.585}, \"rf_within_model\": {\"qwen_50\": 0.63, \"llama_50\": 0.629}, \"random\": 0.5}, \"conclusion_summary\": \"Model-level: all methods detect contamination (lz* d=-2.95~-3.42). Item-level: all methods weak (max AUROC=0.63 with oracle). lz* advantage = unsupervised + interpretable, not item-level superiority.\"}}, \"exp-ctrl-contam-llama-clean\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T20:55:36.448Z\", \"updated_at\": \"2026-05-21T05:04:02.710Z\", \"hypothesis\": \"A Llama-3.1-8B-Instruct model fine-tuned on clean Alpaca data (no MMLU contamination) will show normal person-fit statistics (lz* within expected range), serving as the uncontaminated baseline for comparison with contaminated conditions.\", \"conclusion\": \"success\", \"metrics\": {\"lz_star\": 0.8446, \"acc\": 0.5914, \"theta\": -0.6661, \"seed\": 42, \"method\": \"Snijders (2001) lz*\"}}, \"exp-ctrl-contam-llama-clean-s3\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T23:18:06.724Z\", \"updated_at\": \"2026-05-21T02:56:14.317Z\", \"hypothesis\": \"Third independent clean Llama-3.1-8B-Instruct baseline (seed=456) for Cohen's d variance estimation: matches Qwen n=3 protocol for cross-family effect size comparison\", \"parent\": \"exp-ctrl-contam-llama\", \"conclusion\": \"success\", \"metrics\": {\"lz_star\": -1.0844, \"acc\": 0.5943, \"theta\": -0.64, \"seed\": 456, \"method\": \"Snijders (2001) lz*\"}}, \"exp-ctrl-contam-llama-clean-s2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T23:18:06.128Z\", \"updated_at\": \"2026-05-21T02:56:13.752Z\", \"hypothesis\": \"Second independent clean Llama-3.1-8B-Instruct baseline (seed=123) for Cohen's d variance estimation: n=3 clean baselines needed for reliable cross-family effect size comparison with Qwen\", \"parent\": \"exp-ctrl-contam-llama\", \"conclusion\": \"success\", \"metrics\": {\"lz_star\": -0.1823, \"acc\": 0.5954, \"theta\": -0.63, \"seed\": 123, \"method\": \"Snijders (2001) lz*\"}}, \"exp-ctrl-contam-llama\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T20:23:08.451Z\", \"updated_at\": \"2026-05-21T01:53:06.443Z\", \"hypothesis\": \"The lz* contamination detection signal generalizes across model families: Llama-3.1-8B-Instruct (Meta) under the same QLoRA contamination protocol as Qwen2.5-7B (Alibaba) produces comparable Δlz* effect sizes, directly addressing reviewer concern REV-ADD-2 about single-model generalizability\", \"parent\": \"exp-ctrl-contam-pilot\", \"conclusion\": \"success\", \"metrics\": {\"lz_star_corrected\": true, \"method\": \"Snijders (2001) lz*\", \"clean_lz_star\": 0.8446, \"clean_s2_lz_star\": -0.1823, \"clean_s3_lz_star\": -1.0844, \"clean_mean_lz_star\": -0.1407, \"clean_std_lz_star\": 0.9652, \"clean_acc\": 0.5914, \"clean_theta\": -0.6661, \"contam_15_lz_star\": -2.9922, \"contam_15_acc\": 0.6654, \"contam_15_theta\": -0.276, \"contam_15_delta_lz_star\": -2.8515, \"contam_50_lz_star\": -3.3313, \"contam_50_acc\": 0.6983, \"contam_50_theta\": -0.149, \"contam_50_delta_lz_star\": -3.1906, \"cohens_d_contam_15_ddof1\": -2.95, \"cohens_d_contam_50_ddof1\": -3.31, \"theta_fixed\": -0.666, \"contam_15_lz_star_fixed\": 0.959, \"contam_50_lz_star_fixed\": 1.172, \"dose_response_ratio_free\": 1.09, \"dose_response_ratio_fixed\": 2.87, \"monotonic_free\": true, \"monotonic_fixed\": true}}, \"exp-ctrl-contam-pilot-clean-s3\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T19:04:43.485Z\", \"updated_at\": \"2026-05-20T20:19:33.382Z\", \"hypothesis\": \"Third clean seed (seed=456) for baseline lz* variance estimation: adding a third independent clean control strengthens Cohen's d denominator (n=3 vs n=2), providing more reliable effect size estimates for contamination detection\", \"conclusion\": \"success\", \"metrics\": {\"lz_star\": 8.0806, \"accuracy\": 0.6783, \"theta_mle\": -0.1068, \"cohens_d_n3\": {\"contam_15\": {\"delta\": -4.34, \"d\": -3.58}, \"contam_50\": {\"delta\": -1.9, \"d\": -1.56}}, \"baseline_n3\": {\"mean\": 7.3449, \"std\": 1.2137}, \"baseline_n2\": {\"mean\": 6.9771, \"std\": 1.4609}}}, \"exp-ctrl-contam-pilot-contam-50\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-20T16:16:45.230Z\", \"updated_at\": \"2026-05-20T16:16:45.230Z\"}, \"exp-ctrl-contam-pilot-contam-15\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-20T16:16:44.033Z\", \"updated_at\": \"2026-05-20T16:16:44.033Z\"}, \"exp-ctrl-contam-pilot-clean-s2\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-20T16:16:42.617Z\", \"updated_at\": \"2026-05-20T16:16:42.617Z\"}, \"exp-ctrl-contam-pilot-clean-s1\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-20T16:16:36.780Z\", \"updated_at\": \"2026-05-20T16:16:36.780Z\"}, \"exp-v1-irt-refit-expanded\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T12:54:04.798Z\", \"updated_at\": \"2026-05-20T14:44:22.448Z\", \"hypothesis\": \"With N≥500 models (vs pilot N=63), MML-EM estimation of discrimination parameters will improve substantially (a_pearson_r > 0.4 vs PSN-IRT), because the pilot's a_r=0.111 was primarily caused by catastrophically low N:J ratio (0.0045) rather than fundamental incompatibility between classical IRT and neural IRT parameterizations\", \"parent\": \"exp-v1-irt-refit-pilot\", \"conclusion\": \"negative\", \"metrics\": {\"n_models_downloaded\": 178, \"n_items\": 14042, \"3pl_a_pearson_r\": 0.127, \"2pl_a_pearson_r\": -0.029, \"3pl_b_pearson_r\": 0.663, \"reason\": \"N=178 classical refit: a_r=0.127 (3PL), -0.029 (2PL), b_r=0.663. Discrimination failure confirms Path D dead.\"}}, \"exp-4pl-real-data-degradation\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T14:29:58.285Z\", \"updated_at\": \"2026-05-20T14:41:27.206Z\", \"hypothesis\": \"Forcing d=1.0 (3PL degradation) on PSN-IRT 4PL parameters systematically distorts lz* values for real LLM response data, with the largest distortion on benchmarks/models where items have low d_feasibility, providing empirical evidence (beyond simulation) that the 4PL upper asymptote is essential for accurate person-fit measurement in LLM evaluation\", \"conclusion\": \"success\", \"metrics\": {\"correlation_4pl_vs_3pl\": {\"pearson_r\": 0.225, \"rmse\": 68.41}, \"most_affected_benchmark\": \"MMLU (mean |Δlz*|=58.3, 46% items d<0.95)\", \"most_affected_model\": \"DeepSeek-V3 (θ=3.77): 3PL lz* from +16.4 to -340.6\", \"low_ability_models_impact\": \"|Δlz*|<2 (Gemma-2B-it, Vicuna, Mistral)\", \"bias_direction\": \"3PL systematically depresses high-ability models' lz* (d=1 makes P→1, amplifying few-error aberrance)\", \"key_finding\": \"Ignoring d parameter makes lz* completely unreliable for high-ability models — d-induced bias far exceeds any contamination signal\"}}, \"exp-4pl-ablation\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T13:02:59.785Z\", \"updated_at\": \"2026-05-20T13:50:29.519Z\", \"hypothesis\": \"The 4PL model's upper asymptote parameter d significantly improves contamination detection sensitivity compared to 3PL(d=1) and 2PL(c=0.25,d=1), because d captures ceiling effects in LLM response patterns that mask contamination signal when fixed at 1.0\", \"conclusion\": \"success\", \"metrics\": {\"hypothesis_confirmed\": true, \"far_4pl\": \"~5% (well-calibrated)\", \"far_3pl\": \"4.7-16.5% (inflated)\", \"far_2pl\": \"50-100% (catastrophic, unusable)\", \"mean_power_gain_4pl_vs_3pl\": {\"MMLU\": \"+27.3pp\", \"HellaSwag\": \"+26.1pp\", \"GSM8K\": \"+20.3pp\", \"ARC_C\": \"+14.8pp\", \"HumanEval\": \"+13.7pp\"}, \"max_power_gain_4pl_vs_3pl\": {\"MMLU\": \"+49.0pp\", \"HellaSwag\": \"+59.6pp\", \"GSM8K\": \"+39.7pp\", \"ARC_C\": \"+54.6pp\", \"HumanEval\": \"+30.6pp\"}, \"power_at_25pct\": {\"4PL\": {\"MMLU\": 0.776, \"HellaSwag\": 0.534, \"GSM8K\": 0.73, \"ARC_C\": 0.132, \"HumanEval\": 0.318}, \"3PL\": {\"MMLU\": 0.329, \"HellaSwag\": 0.28, \"GSM8K\": 0.334, \"ARC_C\": 0.091, \"HumanEval\": 0.165}}, \"d_bucket_analysis\": \"d<0.8: +6.8pp to +61.2pp; d>=0.95: negligible\", \"key_finding\": \"4PL d parameter essential for LLM contamination detection. 46% MMLU items have d<0.95. Ignoring d (3PL) halves detection power on average. 2PL completely miscalibrated (FAR 50-100%).\"}}, \"exp-natural-experiment\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T12:49:47.067Z\", \"updated_at\": \"2026-05-20T13:21:26.297Z\", \"hypothesis\": \"Base→chat model pairs from v1 leaderboard exhibit benchmark-specific Δlz* anomalies: instruction-tuning produces a consistent cross-benchmark Δlz* shift, but contamination on specific benchmarks manifests as outlier Δlz* on those benchmarks relative to the pair's mean Δlz* across benchmarks\", \"parent\": \"exp-v1-irt-refit-pilot\", \"conclusion\": \"success\", \"metrics\": {\"n_pairs\": 21, \"n_benchmarks\": 4, \"n_complete_pairs\": 9, \"significant_benchmarks\": {\"HellaSwag\": {\"mean_deviation\": -3.4, \"t_stat\": -3.97, \"p_value\": 0.001, \"interpretation\": \"SFT systematically decreases person-fit on HellaSwag\"}, \"GSM8K\": {\"mean_deviation\": 3.92, \"t_stat\": 3.35, \"p_value\": 0.009, \"interpretation\": \"SFT systematically increases person-fit on GSM8K\"}}, \"non_significant_benchmarks\": {\"MMLU\": {\"p_value\": 0.15}, \"ARC-Challenge\": {\"p_value\": 0.38}}, \"individual_outliers\": 0, \"key_finding\": \"HellaSwag and GSM8K show significant systematic SFT effects on lz*, but no individual pair shows benchmark-specific contamination outliers. P2-optional per Director assessment.\"}}, \"exp-domain-analysis\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T13:03:00.736Z\", \"updated_at\": \"2026-05-20T13:13:27.728Z\", \"hypothesis\": \"Gemini-1.5's MMLU anomaly (lz*=+31.8) is domain-concentrated rather than uniform across all 57 subjects, and other flagged models show distinct domain-specific contamination signatures that differ from Gemini-1.5's pattern\", \"conclusion\": \"success\", \"metrics\": {\"gemini_mmlu_accuracy\": \"100% (14042/14042)\", \"gemini_domain_concentrated\": false, \"gemini_subjects_flagged\": \"50/57 (lz*>1.96)\", \"gemini_category_lz\": {\"STEM\": 21.2, \"Humanities\": 17.9, \"Social Sciences\": 15.9, \"Other\": 15.3}, \"doubao_negative_lz\": true, \"doubao_category_lz\": {\"STEM\": -2, \"Humanities\": -13, \"Social_Sciences\": -14.8, \"Other\": 4.4}, \"hunyuan_uneven\": {\"STEM\": 1.8, \"Social_Sciences\": 13.9}, \"yi_lightning_highest_mmlu_lz\": 48.2, \"qwen_plus_second_highest\": 44.9, \"mistral_flagged_subjects\": \"55/57\"}}, \"exp-ml-classifier-baseline\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T11:57:38.101Z\", \"updated_at\": \"2026-05-20T12:42:10.990Z\", \"hypothesis\": \"ML classifiers (logistic regression, random forest) trained on binary response vectors cannot significantly outperform lz* in contamination detection AUROC on simulated data, because binary response patterns contain limited higher-order information beyond what lz* already captures via the IRT likelihood\", \"conclusion\": \"success\", \"metrics\": {\"auroc_avg_25pct\": {\"lz_star\": 0.86, \"lr_resp\": 0.899, \"rf_resp\": 0.885, \"lr_resp_summ\": 0.909, \"rf_resp_summ\": 0.913}, \"auroc_avg_5pct\": {\"lz_star\": 0.675, \"best_ml\": 0.575}, \"auroc_avg_10pct\": {\"lz_star\": 0.763, \"best_ml\": 0.712}, \"lz_star_advantage_low_contam\": \"+0.10 AUROC at 5%, +0.05 at 10%\", \"ml_advantage_high_contam\": \"+0.05 at 25%, +0.16 at 50%\", \"key_finding\": \"lz* outperforms supervised ML at low contamination (5-10%) without any training data; ML only wins at 25%+ where signal is already strong\"}}, \"exp-v1-irt-refit-pilot\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T10:56:48.899Z\", \"updated_at\": \"2026-05-20T12:32:16.129Z\", \"hypothesis\": \"IRT parameters fitted from v1 leaderboard response data using MML-EM will produce item parameters correlated (r>0.7 for a,b) with PSN-IRT neural-network-estimated parameters, enabling internally consistent person-fit analysis on v1 models.\", \"parent\": \"exp-item-alignment-check\", \"metrics\": {\"n_models_downloaded\": 63, \"n_models_failed\": 38, \"n_items\": 14042, \"n_mapped_items\": 12441, \"overall_accuracy\": 0.426, \"fitting_time_2pl_sec\": 8.9, \"fitting_time_3pl_sec\": 12.1, \"3pl_a_pearson_r\": 0.111, \"3pl_b_pearson_r\": 0.626, \"3pl_b_spearman_r\": 0.656, \"2pl_a_pearson_r\": -0.084, \"2pl_b_pearson_r\": 0.572, \"lz_star_mean\": 11.69, \"lz_star_std\": 6.68, \"lz_star_flagged_pct\": 1.6}, \"conclusion\": \"negative\"}, \"exp-clean-control-delta\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T11:57:39.694Z\", \"updated_at\": \"2026-05-20T12:08:35.683Z\", \"hypothesis\": \"Δlz* between two independent clean response vectors (same θ, different random seeds) has E[Δlz*]≈0 and controlled variance, confirming that non-zero Δlz* in contamination experiments reflects genuine contamination signal rather than estimation noise\", \"conclusion\": \"success\", \"metrics\": {\"clean_vs_clean_mean_abs\": {\"mmlu\": 0.01, \"hellaswag\": 0.125, \"gsm8k\": 0.021, \"arc_c\": 0.095, \"humaneval\": 0.02}, \"clean_vs_clean_all_nonsig\": true, \"clean_vs_contam_all_sig\": true, \"cohens_d\": {\"mmlu\": 2.66, \"hellaswag\": 1.85, \"gsm8k\": 1.85, \"arc_c\": 0.45, \"humaneval\": 1.07}, \"arc_c_note\": \"d=0.45 < 0.5 threshold due to only 295 items, but still p<1e-10\"}}, \"exp-fdr-correction\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T11:57:39.228Z\", \"updated_at\": \"2026-05-20T12:04:41.646Z\", \"hypothesis\": \"BH-FDR correction on the 60-cell cross-benchmark analysis preserves the key finding that nearly all LLM-benchmark cells show significant misfit, with corrected flagging rate remaining above 80%\", \"conclusion\": \"success\", \"metrics\": {\"flagged_uncorrected\": \"57/60 (95%)\", \"flagged_bh_fdr\": \"57/60 (95%)\", \"flagged_bonferroni\": \"not_computed_but_expected_similar\", \"correction_scope\": \"global_60_tests\", \"unflagged_cells\": [\"Yi-Lightning×arc_c (bh_p=0.098)\", \"360GPT2-Pro×humaneval (bh_p=0.134)\", \"Yi-Lightning×humaneval (bh_p=0.181)\"], \"note\": \"Reused existing BH-FDR from exp-two-sided v2 empirical_pvalues.csv. Leaderboard-scale FDR (24800+ tests) deferred to leaderboard audit.\"}}, \"exp-cross-benchmark-analysis\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T11:30:52.484Z\", \"updated_at\": \"2026-05-20T11:35:35.796Z\", \"hypothesis\": \"Cross-benchmark lz* anomaly profiles reveal distinct contamination patterns: models with selective benchmark contamination show high positive lz* on specific benchmarks but normal/negative on others, while models with natural misfit show consistently negative lz* across all benchmarks\", \"metrics\": {\"n_models_all5_flagged\": 10, \"n_models_selective_flagged\": 2, \"gemini15_cluster_isolation\": true, \"dominant_direction_pattern\": \"positive\", \"pct_positive_cells\": 93.3, \"total_flagged\": 57, \"flag_rate\": 0.95}, \"conclusion\": \"success\"}, \"exp-accuracy-zscore-baseline\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T11:30:51.761Z\", \"updated_at\": \"2026-05-20T11:33:55.426Z\", \"hypothesis\": \"Accuracy z-score baseline (|z|>1.96) flags far fewer cells than lz* because it only captures overall performance deviation without item-level pattern information — lz* provides strictly more information by detecting response pattern aberrance that accuracy alone misses\", \"metrics\": {\"z_flagged_count\": 4, \"lz_flagged_count\": 57, \"agreement_rate\": 0.117, \"gemini15_mmlu_zscore\": 1.413}, \"conclusion\": \"success\"}, \"exp-item-alignment-check\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T10:16:34.437Z\", \"updated_at\": \"2026-05-20T10:53:40.587Z\", \"hypothesis\": \"Open LLM Leaderboard v1 per-item responses share the same deterministic item ordering as PSN-IRT combine.csv (both generated by lm-eval-harness), enabling direct positional alignment of v1 response vectors with PSN-IRT 4PL item parameters without content-based matching\", \"parent\": \"exp-leaderboard-data-recon\", \"conclusion\": \"negative\", \"metrics\": {\"match_rate_direct\": 0.5456, \"match_rate_reordered_mistral\": 0.8846, \"match_rate_reordered_vicuna\": 0.7248, \"n_items_checked\": 14042, \"n_models_verified\": 2, \"alignment_method\": \"content-based via cais/mmlu canonical order\", \"items_mapped\": 12068, \"mapping_coverage\": 0.86}}, \"exp-power-theory\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T09:53:40.117Z\", \"updated_at\": \"2026-05-20T10:38:57.599Z\", \"hypothesis\": \"Detection power of lz* follows an analytic function of n_items and contamination level derivable from Snijders (2001) variance formula, and this theoretical curve explains the empirically observed inverted-U shape and n_items dependence with R²>0.95 against simulation data\", \"parent\": \"exp-extended-sim\", \"metrics\": {\"R2_two_sided\": 0.9572, \"RMSE_two_sided\": 0.0746, \"R2_left_tail\": 0.9764, \"R2_mean_lz\": 0.9948, \"sqrt_n_R2_avg\": 0.88, \"crossover_range_pct\": \"81-85%\", \"min_items_15pct_80power\": 7958}, \"conclusion\": \"success\"}, \"exp-empirical-null\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T09:53:38.594Z\", \"updated_at\": \"2026-05-20T10:02:04.668Z\", \"hypothesis\": \"Bootstrap empirical null of lz* under 4PL model shows systematic positive bias (mean>>0) and inflated variance (std>>1) for real LLM response data, quantifying the degree to which LLMs violate IRT local independence/unidimensionality assumptions — this bias explains why 95% of cells are flagged with absolute thresholds\", \"parent\": \"exp-two-sided\", \"metrics\": {\"n_boot\": 1000, \"n_cells\": 60, \"mean_null_bias\": 0.0925, \"mean_null_std\": 1.0021, \"ks_reject_rate\": 0.4, \"ks_reject_count\": \"24/60\", \"bias_by_benchmark\": {\"arc_c\": 0.146, \"gsm8k\": 0.082, \"hellaswag\": 0.034, \"humaneval\": 0.16, \"mmlu\": 0.041}, \"std_by_benchmark\": {\"arc_c\": 1.004, \"gsm8k\": 1.01, \"hellaswag\": 0.999, \"humaneval\": 0.994, \"mmlu\": 1.003}, \"ks_reject_by_benchmark\": {\"arc_c\": 0.583, \"gsm8k\": 0.5, \"hellaswag\": 0.083, \"humaneval\": 0.75, \"mmlu\": 0.083}, \"key_finding\": \"Null bias is small (mean=0.09) and std is near 1.0 — the bootstrap null is well-calibrated. The 95% flagging rate is NOT caused by miscalibrated null but by genuine extreme lz* values in LLM data. Smaller benchmarks (humaneval, arc_c) show higher KS rejection rates due to stronger finite-sample deviations from normality.\"}, \"conclusion\": \"negative\"}, \"exp-leaderboard-data-recon\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T09:53:39.512Z\", \"updated_at\": \"2026-05-20T10:00:22.466Z\", \"hypothesis\": \"Open LLM Leaderboard v1 results repo on HuggingFace contains per-item binary response logs (not just aggregate scores) for a substantial number of models, enabling large-scale person-fit analysis without running inference ourselves\", \"metrics\": {\"n_models_with_per_item_data\": \"13000+\", \"benchmarks_covered\": \"4/5 (MMLU, HellaSwag, ARC-Challenge, GSM8K; missing HumanEval)\", \"estimated_gpu_hours_if_needed\": 0, \"v1_benchmarks\": 6, \"v2_benchmarks\": 6, \"data_format\": \"parquet per-item rows with acc/acc_norm binary fields\", \"source\": \"open-llm-leaderboard-old/details_{model}\", \"humaneval_gpu_hrs_per_7b_model\": 0.08, \"key_finding\": \"v1 details datasets contain per-item binary responses for 13K+ models. Zero GPU cost for 4/5 benchmarks.\"}, \"conclusion\": \"success\"}, \"exp-extended-sim\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T09:31:30.112Z\", \"updated_at\": \"2026-05-20T09:50:31.545Z\", \"hypothesis\": \"Extended simulation with finer contamination levels (60/75/90%) and fixed 100% NaN handling will reveal the precise dual-regime crossover point where lz* flips from negative (aberrant) to positive (over-consistent), and inverted-U power curve shape is confirmed across all benchmarks\", \"parent\": \"sim_001\", \"metrics\": {\"n_sims\": 2000, \"levels\": \"0/3/5/10/15/25/50/60/75/90/100\", \"n_excluded_100pct\": 0, \"inverted_u_all_5\": true, \"dual_regime_crossover\": \"75-90%\", \"mmlu_power_15pct\": 0.9845, \"hellaswag_power_15pct\": 0.7525, \"gsm8k_power_15pct\": 0.5905, \"mmlu_100pct_lz_star\": 31.815, \"hellaswag_100pct_lz_star\": 26.297, \"gsm8k_100pct_lz_star\": 8.253, \"arc_c_100pct_lz_star\": 4.339, \"humaneval_100pct_lz_star\": 3.529, \"two_sided_power\": {\"mmlu_15pct\": 0.978, \"mmlu_50pct\": 0.9525, \"mmlu_75pct\": 0.936, \"mmlu_90pct\": 0.9515, \"mmlu_100pct\": 1, \"hellaswag_25pct\": 0.9155, \"hellaswag_50pct\": 0.9475, \"hellaswag_90pct\": 0.9375, \"hellaswag_100pct\": 1, \"gsm8k_50pct\": 0.837, \"gsm8k_90pct\": 0.794, \"gsm8k_100pct\": 1}, \"key_finding\": \"Two-sided detection eliminates inverted-U: MMLU two-sided power >93% at ALL contamination levels. 100% contamination → 100% detection on all benchmarks.\"}, \"conclusion\": \"success\"}, \"exp-two-sided\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T09:13:53.986Z\", \"updated_at\": \"2026-05-20T09:14:27.223Z\", \"hypothesis\": \"Two-sided detection (|lz*| > threshold) with benchmark-specific θ MLE + parametric bootstrap empirical null + BH-FDR control will reduce Phase B flagging rate from 93% to a reasonable level (<20%), isolating genuine contamination signals from θ estimation bias\", \"parent\": \"phase_b_personfit\", \"metrics\": {\"flagged_rate\": \"57/60 (95.0%)\", \"n_boot\": 1000, \"fdr_alpha\": 0.05, \"flagged_positive\": 51, \"flagged_negative\": 6, \"unflagged\": 3, \"unflagged_cells\": \"Yi-Lightning/arc_c (p=0.098), 360GPT2-Pro/humaneval (p=0.134), Yi-Lightning/humaneval (p=0.181)\", \"gemini15_mmlu_lz_star_v2\": 31.815, \"gemini15_mmlu_theta_bench\": 4, \"gemini15_mmlu_p_emp\": 0, \"key_finding\": \"Benchmark-specific θ + bootstrap + FDR does NOT reduce flagging. LLMs universally violate 4PL assumptions.\"}, \"conclusion\": \"negative\"}, \"phase_b_personfit\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T08:34:21.694Z\", \"updated_at\": \"2026-05-20T08:34:56.735Z\", \"hypothesis\": \"Real LLM benchmark response data from PSN-IRT 12 models shows significant inter-model variation in person-fit statistics (lz*, outfit, infit), with specific models exhibiting anomalous patterns indicative of benchmark contamination — particularly Gemini-1.5 with accuracy-ability dissociation\", \"metrics\": {\"lz_star_sd_all_gt_0.5\": true, \"mmlu_lz_star_mean\": 24.19, \"mmlu_lz_star_sd\": 16.47, \"hellaswag_lz_star_mean\": 20.09, \"hellaswag_lz_star_sd\": 17.59, \"gsm8k_lz_star_mean\": 8.22, \"gsm8k_lz_star_sd\": 8.97, \"gemini15_mmlu_lz_star\": 34.75, \"gemini15_mmlu_accuracy\": 1, \"gemini15_mmlu_theta\": 0.78, \"gemini15_flagged_benchmarks\": \"3/5 (HellaSwag, GSM8K, HumanEval negative lz*)\", \"cross_benchmark_spearman_significant\": \"1/10 (GSM8K vs HumanEval rho=0.62 p=0.031)\", \"n_models\": 12, \"n_benchmarks\": 5}, \"conclusion\": \"success\"}, \"sim_001\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T07:13:53.208Z\", \"updated_at\": \"2026-05-20T08:09:31.642Z\", \"hypothesis\": \"Under 4PL IRT model, lz* person-fit statistic can detect partial benchmark contamination (5-30% items) with >80% power at α=0.05, and detection power follows an inverted-U curve across contamination levels (low contamination undetectable, moderate contamination most detectable, high contamination mimics high ability)\", \"conclusion\": \"negative\", \"metrics\": {\"null_check\": {\"all_pass\": true, \"gsm8k_ks_p\": 0.098, \"hellaswag_ks_p\": 0.224, \"mmlu_ks_p\": 0.594}, \"simulation_power_at_15pct\": {\"mmlu\": 0.979, \"hellaswag\": 0.733, \"gsm8k\": 0.578, \"arc_c\": 0.129, \"humaneval\": 0.243}, \"global_pass\": false, \"inverted_u_all_benchmarks\": true, \"pass_count_large_80pct\": \"1/3 (mmlu only)\"}}}, \"count\": 67, \"total\": 67, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2353}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "19525180-0ca9-476c-84ae-28beb29fd7e3",
  "isSidechain": false,
  "promptId": "26661264-62cc-4d8c-933c-ac64167cc12e",
  "type": "user",
  "uuid": "dc5d2d2a-9e0d-41ab-9982-e1b40ec299c9",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {\\\"exp-arcc-clean-s10\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-21T12:48:49.366Z\\\", \\\"updated_at\\\": \\\"2026-05-21T13:05:54.577Z\\\", \\\"hypothesis\\\": \\\"ARC-Challenge clean baseline (seed=307) for cross-benchmark Cohen's d — expanding clean lz* distribution\\\", \\\"parent\\\": \\\"exp-arcc-benchmark\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"theta_mle\\\": 0.8111, \\\"lz_star\\\": -5.0733, \\\"accuracy\\\": 0.9051, \\\"n_items\\\": 295}}, \\\"exp-arcc-clean-s9\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-21T12:48:48.480Z\\\", \\\"updated_at\\\": \\\"2026-05-21T13:05:53.688Z\\\", \\\"hypothesis\\\": \\\"ARC-Challenge clean baseline (seed=306) for cross-benchmark Cohen's d — expanding clean lz* distribution\\\", \\\"parent\\\": \\\"exp-arcc-benchmark\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"theta_mle\\\": 0.8868, \\\"lz_star\\\": -5.5359, \\\"accuracy\\\": 0.9017, \\\"n_items\\\": 295}}, \\\"exp-arcc-clean-s8\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-21T12:48:47.531Z\\\", \\\"updated_at\\\": \\\"2026-05-21T13:05:52.824Z\\\", \\\"hypothesis\\\": \\\"ARC-Challenge clean baseline (seed=305) for cross-benchmark Cohen's d — expanding clean lz* distribution\\\", \\\"parent\\\": \\\"exp-arcc-benchmark\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"theta_mle\\\": 0.8511, \\\"lz_star\\\": -5.4001, \\\"accuracy\\\": 0.9051, \\\"n_items\\\": 295}}, \\\"exp-arcc-clean-s7\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-21T12:48:46.522Z\\\", \\\"updated_at\\\": \\\"2026-05-21T13:05:51.824Z\\\", \\\"hypothesis\\\": \\\"ARC-Challenge clean baseline (seed=304) for cross-benchmark Cohen's d — expanding clean lz* distribution\\\", \\\"parent\\\": \\\"exp-arcc-benchmark\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"theta_mle\\\": 0.7058, \\\"lz_star\\\": -5.5852, \\\"accuracy\\\": 0.8915, \\\"n_items\\\": 295}}, \\\"exp-ctrl-contam-llama-clean-s10\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"created_at\\\": \\\"2026-05-21T13:03:57.523Z\\\", \\\"updated_at\\\": \\\"2026-05-21T13:04:26.843Z\\\", \\\"hypothesis\\\": \\\"Independent clean Llama-3.1-8B-Instruct baseline (seed=307) for n=10 Cohen's d variance estimation\\\", \\\"parent\\\": \\\"exp-ctrl-contam-llama-contam15\\\"}, \\\"exp-ctrl-contam-llama-clean-s9\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"created_at\\\": \\\"2026-05-21T13:03:56.214Z\\\", \\\"updated_at\\\": \\\"2026-05-21T13:04:25.842Z\\\", \\\"hypothesis\\\": \\\"Independent clean Llama-3.1-8B-Instruct baseline (seed=306) for n=10 Cohen's d variance estimation\\\", \\\"parent\\\": \\\"exp-ctrl-contam-llama-contam15\\\"}, \\\"exp-ctrl-contam-llama-clean-s8\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"created_at\\\": \\\"2026-05-21T13:03:54.282Z\\\", \\\"updated_at\\\": \\\"2026-05-21T13:04:24.947Z\\\", \\\"hypothesis\\\": \\\"Independent clean Llama-3.1-8B-Instruct baseline (seed=305) for n=10 Cohen's d variance estimation\\\", \\\"parent\\\": \\\"exp-ctrl-contam-llama-contam15\\\"}, \\\"eval-mistral-clean-s3\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-21T12:59:20.651Z\\\", \\\"updated_at\\\": \\\"2026-05-21T13:00:42.054Z\\\", \\\"hypothesis\\\": \\\"Mistral clean_s3 (seed 3) LoRA adapter trained on clean MMLU data will show lz* near zero, consistent with no contamination signal in the IRT person-fit framework.\\\", \\\"metrics\\\": {\\\"theta_mle\\\": -0.9733, \\\"lz_star\\\": 3.2792, \\\"accuracy_overall\\\": 0.5413, \\\"n_items\\\": 14042}, \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-mistral-clean-s2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-21T12:59:19.645Z\\\", \\\"updated_at\\\": \\\"2026-05-21T13:00:41.390Z\\\", \\\"hypothesis\\\": \\\"Mistral clean_s2 (seed 2) LoRA adapter trained on clean MMLU data will show lz* near zero, consistent with no contamination signal in the IRT person-fit framework.\\\", \\\"metrics\\\": {\\\"theta_mle\\\": -0.9627, \\\"lz_star\\\": -1.0456, \\\"accuracy_overall\\\": 0.5428, \\\"n_items\\\": 14042}, \\\"conclusion\\\": \\\"success\\\"}, \\\"exp-post-rl-v3\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"created_at\\\": \\\"2026-05-21T12:45:42.860Z\\\", \\\"updated_at\\\": \\\"2026-05-21T12:47:34.274Z\\\", \\\"hypothesis\\\": \\\"GRPO with num_generations=16 + temperature=1.2 produces measurable parameter update while preserving lz* contamination signal (R7 post-RL robustness)\\\", \\\"parent\\\": \\\"exp-post-rl\\\"}, \\\"exp-post-rl\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-21T03:55:49.080Z\\\", \\\"updated_at\\\": \\\"2026-05-21T12:47:18.550Z\\\", \\\"hypothesis\\\": \\\"Post-RL (GRPO) training does not wash out contamination signal detectable by lz*: SFT-contaminated model retains negative Δlz* after GRPO alignment, demonstrating that IRT-based detection is robust to RL post-training — addressing reviewer concern R7 about SFT-only scope\\\", \\\"notes\\\": \\\"GRPO v1/v2 reward saturation (frac_reward_zero_std=1.0), zero gradient, model ≈ SFT. Restarting as exp-post-rl-v3 with fixed params (num_generations=16, temperature=1.2, max_steps=3000, save_steps=500).\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"exp-ctrl-contam-llama-clean-s7\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-21T12:42:50.324Z\\\", \\\"updated_at\\\": \\\"2026-05-21T12:44:14.678Z\\\", \\\"hypothesis\\\": \\\"Clean SFT (seed 7) on Llama-3.1-8B should produce lz* near zero, indicating no person-fit anomaly without contamination.\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"theta_mle\\\": -0.6356, \\\"lz_star\\\": -0.4007, \\\"accuracy_overall\\\": 0.5929, \\\"n_items\\\": 14042}}, \\\"exp-ctrl-contam-llama-clean-s6\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-21T12:42:49.542Z\\\", \\\"updated_at\\\": \\\"2026-05-21T12:44:13.998Z\\\", \\\"hypothesis\\\": \\\"Clean SFT (seed 6) on Llama-3.1-8B should produce lz* near zero, indicating no person-fit anomaly without contamination.\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"theta_mle\\\": -0.6027, \\\"lz_star\\\": 2.8466, \\\"accuracy_overall\\\": 0.601, \\\"n_items\\\": 14042}}, \\\"exp-ctrl-contam-llama-clean-s5\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-21T12:42:48.174Z\\\", \\\"updated_at\\\": \\\"2026-05-21T12:44:13.366Z\\\", \\\"hypothesis\\\": \\\"Clean SFT (seed 5) on Llama-3.1-8B should produce lz* near zero, indicating no person-fit anomaly without contamination.\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"theta_mle\\\": -0.63, \\\"lz_star\\\": 1.7323, \\\"accuracy_overall\\\": 0.5965, \\\"n_items\\\": 14042}}, \\\"exp-ctrl-contam-llama-clean-s4\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-21T12:24:43.970Z\\\", \\\"updated_at\\\": \\\"2026-05-21T12:44:12.382Z\\\", \\\"hypothesis\\\": \\\"Clean SFT (seed 4) on Llama-3.1-8B should produce lz* near zero, indicating no person-fit anomaly without contamination.\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"theta_mle\\\": -0.6435, \\\"lz_star\\\": 0.0206, \\\"accuracy_overall\\\": 0.5923, \\\"n_items\\\": 14042}}, \\\"arcc-clean-s10\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"created_at\\\": \\\"2026-05-21T12:08:37.841Z\\\", \\\"updated_at\\\": \\\"2026-05-21T12:10:04.708Z\\\"}, \\\"arcc-clean-s9\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"created_at\\\": \\\"2026-05-21T12:08:35.737Z\\\", \\\"updated_at\\\": \\\"2026-05-21T12:10:03.378Z\\\"}, \\\"arcc-clean-s8\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"created_at\\\": \\\"2026-05-21T12:08:33.697Z\\\", \\\"updated_at\\\": \\\"2026-05-21T12:10:01.469Z\\\"}, \\\"arcc-clean-s7\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"created_at\\\": \\\"2026-05-21T12:08:32.282Z\\\", \\\"updated_at\\\": \\\"2026-05-21T12:10:00.031Z\\\"}, \\\"exp-ctrl-contam-pilot\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-20T13:54:01.818Z\\\", \\\"updated_at\\\": \\\"2026-05-21T11:44:22.927Z\\\", \\\"hypothesis\\\": \\\"Controlled contamination via QLoRA fine-tuning on MMLU items produces measurable Δlz* signal: (1) clean-vs-clean Δlz* ≈ 0 (seed1 vs seed2), confirming the noise floor; (2) 15% contamination produces significant negative Δlz* with Cohen's d > 1.0; (3) 50% contamination produces even stronger signal; (4) contamination signal concentrates on seen items (memorization fraction > 0.5)\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"cohens_d_contam15\\\": 6.575, \\\"cohens_d_contam15_ci\\\": [4.514, 15.199], \\\"cohens_d_contam50\\\": 1.897, \\\"cohens_d_contam50_ci\\\": [1.041, 4.923], \\\"clean_n10_mean_lz\\\": 8.684, \\\"clean_n10_sd_lz\\\": 0.735, \\\"contam15_lz\\\": 3.849, \\\"contam50_lz\\\": 7.289, \\\"n_clean_seeds\\\": 10, \\\"n_items\\\": 14042}, \\\"notes\\\": \\\"partial: H1✓ H2✓ H3✗(θ-shift, fixed analysis restores monotonicity) H4✗(memorization<0.5). θ-fixed=-0.0965 (n=3 mean). Snijders lz* corrected: dose-response ratio=3.12 (unchanged from Drasgow). Δlz*_fixed: contam_15=+3.169, contam_50=+9.893. All values use Snijders (2001) lz*.\\\"}, \\\"exp-arcc-benchmark\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"created_at\\\": \\\"2026-05-21T08:07:05.912Z\\\", \\\"updated_at\\\": \\\"2026-05-21T11:20:59.126Z\\\", \\\"hypothesis\\\": \\\"ℓz* contamination detection generalizes beyond MMLU to ARC-Challenge, a second benchmark with PSN-IRT 4PL calibration — demonstrating cross-benchmark applicability and addressing reviewer concern about single-benchmark evaluation.\\\", \\\"notes\\\": \\\"代码就绪: /root/autodl-tmp/ctrl_contam_arcc/ (prepare_arcc_data.py + train.py + eval_lz.py + arc_c_params.csv)。ARC-C: 295 items with 4PL params (294×4-choice + 1×3-choice), 15% contam=44 items, 50% contam=147 items。预期检测力有限 (sim_001 12.9% power) 但 cross-benchmark generalization 价值明确。数据已生成。等 GPU 可用后启动。\\\", \\\"metrics\\\": {\\\"19912_clean_s1_acc\\\": 0.902, \\\"19912_clean_s1_lz\\\": -5.448, \\\"19912_clean_s2_acc\\\": 0.895, \\\"19912_clean_s2_lz\\\": -5.433, \\\"19912_contam15_acc\\\": 0.909, \\\"19912_contam15_lz\\\": -4.917, \\\"19912_contam15_lz_seen\\\": 0.568, \\\"19912_contam50_acc\\\": 0.942, \\\"19912_contam50_lz\\\": -4.573, \\\"19912_contam50_lz_seen\\\": -0.331, \\\"35694_clean_s1_acc\\\": 0.895, \\\"35694_clean_s1_lz\\\": -5.511, \\\"35694_clean_s2_acc\\\": 0.898, \\\"35694_clean_s2_lz\\\": -5.493, \\\"35694_contam15_acc\\\": 0.909, \\\"35694_contam15_lz\\\": -5.032, \\\"35694_contam15_lz_seen\\\": 0.186, \\\"35694_contam50_acc\\\": 0.946, \\\"35694_contam50_lz\\\": -4.185, \\\"35694_contam50_lz_seen\\\": -0.475}}, \\\"exp-ctrl-contam-qwen-clean-s10\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"created_at\\\": \\\"2026-05-21T09:12:35.740Z\\\", \\\"updated_at\\\": \\\"2026-05-21T11:20:55.470Z\\\", \\\"hypothesis\\\": \\\"Tenth independent clean Qwen2.5-7B-Instruct baseline (seed=307) for n=10 Cohen's d variance estimation\\\", \\\"parent\\\": \\\"exp-ctrl-contam-pilot\\\", \\\"metrics\\\": {\\\"accuracy\\\": 0.676, \\\"lz_star\\\": 8.149, \\\"theta_mle\\\": -0.116, \\\"n_items\\\": 14042}}, \\\"exp-ctrl-contam-llama-contam50\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-20T20:57:09.849Z\\\", \\\"updated_at\\\": \\\"2026-05-21T11:15:59.751Z\\\", \\\"hypothesis\\\": \\\"50% MMLU contamination on Llama-3.1-8B-Instruct produces measurable Δlz* signal, with expected θ-shift effects comparable to Qwen pilot\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"lz_star\\\": -3.3313, \\\"acc\\\": 0.6983, \\\"theta_mle\\\": -0.149, \\\"acc_seen\\\": 0.735, \\\"acc_unseen\\\": 0.661, \\\"delta_lz_star\\\": -3.1906, \\\"cohens_d_ddof1\\\": -3.31, \\\"method\\\": \\\"Snijders (2001) lz*\\\"}}, \\\"exp-ctrl-contam-llama-contam15\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-20T20:57:08.665Z\\\", \\\"updated_at\\\": \\\"2026-05-21T11:15:59.136Z\\\", \\\"hypothesis\\\": \\\"15% MMLU contamination on Llama-3.1-8B-Instruct produces comparable Δlz* signal to Qwen2.5-7B (pilot d=-3.58), confirming cross-model generalizability\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"lz_star\\\": -2.9922, \\\"acc\\\": 0.6654, \\\"theta_mle\\\": -0.276, \\\"acc_seen\\\": 0.742, \\\"acc_unseen\\\": 0.652, \\\"delta_lz_star\\\": -2.8515, \\\"cohens_d_ddof1\\\": -2.95, \\\"method\\\": \\\"Snijders (2001) lz*\\\"}}, \\\"exp-constat-comparison\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"created_at\\\": \\\"2026-05-21T08:07:04.296Z\\\", \\\"updated_at\\\": \\\"2026-05-21T10:57:28.101Z\\\", \\\"hypothesis\\\": \\\"ConStat (NeurIPS 2024) requires multi-benchmark performance scores for contamination detection, making it inapplicable or underpowered in single-benchmark scenarios. ℓz* operates on binary response patterns from a single benchmark, demonstrating superior minimal-information detection capability.\\\", \\\"notes\\\": \\\"Bugfix 完成: (1) Snijders 方差校正已加 (2) 阈值方向修正为 abs(lz)>1.96 (3) RNG 隔离。修正后 clean lz* mean=-0.058≈0。仿真结果: 绝对 lz* power≈FAR 在所有 contam 级别（θ-shift 完全吸收信号），进一步证实 Δlz* 对比设计的必要性。ConStat 真实模型对比不可行（缺 reference benchmark + ≥5 reference models）。\\\"}, \\\"exp-arcc-clean-s1\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"created_at\\\": \\\"2026-05-21T09:12:36.602Z\\\", \\\"updated_at\\\": \\\"2026-05-21T10:57:23.992Z\\\", \\\"hypothesis\\\": \\\"ARC-Challenge clean baseline (seed=42) for cross-benchmark ℓz* detection — establishing clean lz* distribution on a second benchmark with PSN-IRT 4PL calibration\\\", \\\"parent\\\": \\\"exp-arcc-benchmark\\\", \\\"metrics\\\": {\\\"accuracy\\\": 0.8949, \\\"theta_mle\\\": 0.6872, \\\"lz_star\\\": -5.5107, \\\"n_items\\\": 295}}, \\\"exp-mia-mink-comparison\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"created_at\\\": \\\"2026-05-21T08:07:05.266Z\\\", \\\"updated_at\\\": \\\"2026-05-21T10:57:22.586Z\\\", \\\"hypothesis\\\": \\\"MIA methods (Min-K%/Min-K%++) fail to detect contamination in post-RL (GRPO) models because RL fine-tuning disrupts token-level log-prob distributions, while ℓz* remains effective because it operates on response-pattern-level statistics that survive RL post-training — demonstrating robustness advantage over MIA approaches.\\\", \\\"notes\\\": \\\"代码就绪: eval_mia.py (Loss/Min-K%/Min-K%++ K=10-50, AUC-ROC) + compare_mia_lz.py。路径: /root/autodl-tmp/post_rl_contam/。需 GPU ~1-2h/stage，等 GRPO 完成后执行。\\\", \\\"metrics\\\": {\\\"base_auc_loss\\\": 0.486, \\\"base_auc_mink10\\\": 0.493, \\\"base_auc_minkpp10\\\": 0.488, \\\"sft_auc_loss\\\": 0.592, \\\"sft_auc_mink10\\\": 0.611, \\\"sft_auc_minkpp10\\\": 0.569}}, \\\"exp-arcc-clean-s2\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"created_at\\\": \\\"2026-05-21T10:17:15.804Z\\\", \\\"updated_at\\\": \\\"2026-05-21T10:17:15.804Z\\\"}, \\\"exp-ctrl-contam-qwen-clean-s9\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-21T08:25:55.311Z\\\", \\\"updated_at\\\": \\\"2026-05-21T09:13:10.810Z\\\", \\\"hypothesis\\\": \\\"Ninth independent clean Qwen2.5-7B-Instruct baseline (seed=306) for n=10 Cohen's d variance estimation\\\", \\\"parent\\\": \\\"exp-ctrl-contam-pilot\\\", \\\"metrics\\\": {\\\"accuracy\\\": 0.6743, \\\"lz_star\\\": 9.013, \\\"theta_mle\\\": -0.1242, \\\"n_items\\\": 14042}, \\\"conclusion\\\": \\\"success\\\"}, \\\"exp-ctrl-contam-qwen-clean-s7\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-21T07:42:16.770Z\\\", \\\"updated_at\\\": \\\"2026-05-21T09:13:10.213Z\\\", \\\"hypothesis\\\": \\\"Seventh independent clean Qwen2.5-7B-Instruct baseline (seed=304) for n=10 Cohen's d\\\", \\\"parent\\\": \\\"exp-ctrl-contam-pilot\\\", \\\"metrics\\\": {\\\"accuracy\\\": 0.6783, \\\"lz_star\\\": 8.77, \\\"theta_mle\\\": -0.0892, \\\"n_items\\\": 14042}, \\\"conclusion\\\": \\\"success\\\"}, \\\"exp-ctrl-contam-qwen-clean-s8\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-21T07:42:56.989Z\\\", \\\"updated_at\\\": \\\"2026-05-21T09:12:28.785Z\\\", \\\"hypothesis\\\": \\\"Eighth independent clean Qwen2.5-7B-Instruct baseline (seed=305) for n=10 Cohen's d\\\", \\\"parent\\\": \\\"exp-ctrl-contam-pilot\\\", \\\"notes\\\": \\\"s8 PID 99807 found dead at step 294/939. Needs restart on next available GPU. Previous run was on cuda:3 with CUDA_VISIBLE_DEVICES=3.\\\", \\\"metrics\\\": {\\\"accuracy\\\": 0.6768, \\\"lz_star\\\": 9.111, \\\"theta_mle\\\": -0.1035, \\\"n_items\\\": 14042, \\\"loss\\\": 1.352, \\\"steps\\\": 939}, \\\"conclusion\\\": \\\"success\\\"}, \\\"exp-ctrl-contam-qwen-clean-s6\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-21T06:56:41.860Z\\\", \\\"updated_at\\\": \\\"2026-05-21T09:12:27.846Z\\\", \\\"hypothesis\\\": \\\"Sixth independent clean Qwen2.5-7B-Instruct baseline (seed=303) for expanded n=10 Cohen's d variance estimation\\\", \\\"parent\\\": \\\"exp-ctrl-contam-pilot\\\", \\\"metrics\\\": {\\\"accuracy\\\": 0.6771, \\\"lz_star\\\": 8.245, \\\"theta_mle\\\": -0.1036, \\\"n_items\\\": 14042, \\\"loss\\\": 1.354, \\\"steps\\\": 939}, \\\"conclusion\\\": \\\"success\\\"}, \\\"exp-ctrl-contam-qwen-clean-s5\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-21T06:30:49.858Z\\\", \\\"updated_at\\\": \\\"2026-05-21T08:25:54.248Z\\\", \\\"hypothesis\\\": \\\"Fifth independent clean Qwen2.5-7B-Instruct baseline (seed=302) for expanded n=10 Cohen's d variance estimation\\\", \\\"parent\\\": \\\"exp-ctrl-contam-pilot\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"accuracy\\\": 0.6787, \\\"lz_star\\\": 8.532, \\\"theta_mle\\\": -0.088, \\\"n_items\\\": 14042}}, \\\"exp-ctrl-contam-qwen-clean-s4\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-21T06:30:49.211Z\\\", \\\"updated_at\\\": \\\"2026-05-21T08:25:52.756Z\\\", \\\"hypothesis\\\": \\\"Fourth independent clean Qwen2.5-7B-Instruct baseline (seed=301) for expanded n=10 Cohen's d variance estimation, improving statistical power of contamination effect size measurement\\\", \\\"parent\\\": \\\"exp-ctrl-contam-pilot\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"accuracy\\\": 0.6786, \\\"lz_star\\\": 8.967, \\\"theta_mle\\\": -0.109, \\\"n_items\\\": 14042}}, \\\"exp-ctrl-contam-mistral\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-21T04:21:26.398Z\\\", \\\"updated_at\\\": \\\"2026-05-21T06:50:42.866Z\\\", \\\"hypothesis\\\": \\\"Mistral-7B-Instruct-v0.3 as a third model family (distinct tokenizer and training recipe from Qwen/Llama) produces significant Δlz* under controlled contamination, further confirming cross-family detection generalizability — addressing reviewer concern R4 about limited model diversity (2 families × 1 benchmark)\\\", \\\"parent\\\": \\\"exp-ctrl-contam-pilot\\\", \\\"notes\\\": \\\"Mistral-7B-Instruct-v0.3 confirmed as latest 7B Instruct (v0.4 does not exist). Model downloaded via ModelScope. Three conditions training in parallel: clean cuda:0, contam_15 cuda:1, contam_50 cuda:3. eval_lz.py uses Snijders (2001) lz* correction.\\\", \\\"metrics\\\": {\\\"clean\\\": {\\\"lz_star\\\": 5.4175, \\\"acc\\\": 0.5138, \\\"theta\\\": -1.1569}, \\\"contam_15\\\": {\\\"lz_star\\\": -1.3849, \\\"acc\\\": 0.5949, \\\"acc_seen\\\": 0.7436, \\\"acc_unseen\\\": 0.5686, \\\"theta\\\": -0.7129}, \\\"contam_50\\\": {\\\"lz_star\\\": -3.1503, \\\"acc\\\": 0.6732, \\\"acc_seen\\\": 0.7523, \\\"acc_unseen\\\": 0.5941, \\\"theta\\\": -0.3027}, \\\"delta_lz_star_15\\\": -6.8024, \\\"delta_lz_star_50\\\": -8.5678, \\\"method\\\": \\\"Snijders (2001) lz*\\\"}, \\\"conclusion\\\": \\\"success\\\"}, \\\"exp-ctrl-contam-mistral-contam50\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-21T04:52:15.643Z\\\", \\\"updated_at\\\": \\\"2026-05-21T06:33:45.847Z\\\", \\\"metrics\\\": {\\\"lz_star\\\": -3.1503, \\\"acc_overall\\\": 0.6732, \\\"acc_seen\\\": 0.7523, \\\"acc_unseen\\\": 0.5941, \\\"theta_mle\\\": -0.3027, \\\"lz_star_seen\\\": -1.3701, \\\"lz_star_unseen\\\": -0.9972, \\\"method\\\": \\\"Snijders (2001) lz*\\\"}, \\\"conclusion\\\": \\\"success\\\", \\\"hypothesis\\\": \\\"A Mistral-7B model fine-tuned with 50% MMLU contamination will produce strongly aberrant person-fit (highly negative lz*) because extensive memorization creates a large discrepancy between observed and IRT-expected response patterns.\\\"}, \\\"exp-ctrl-contam-mistral-contam15\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-21T04:52:14.095Z\\\", \\\"updated_at\\\": \\\"2026-05-21T06:33:45.252Z\\\", \\\"metrics\\\": {\\\"lz_star\\\": -1.3849, \\\"acc_overall\\\": 0.5949, \\\"acc_seen\\\": 0.7436, \\\"acc_unseen\\\": 0.5686, \\\"theta_mle\\\": -0.7129, \\\"lz_star_seen\\\": -1.0838, \\\"lz_star_unseen\\\": -0.0956, \\\"method\\\": \\\"Snijders (2001) lz*\\\"}, \\\"conclusion\\\": \\\"success\\\", \\\"hypothesis\\\": \\\"A Mistral-7B model fine-tuned with 15% MMLU contamination will produce aberrant person-fit (negative lz*) because memorized items inflate accuracy on seen questions regardless of difficulty, violating the IRT-predicted response pattern.\\\"}, \\\"exp-ctrl-contam-mistral-clean\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-21T04:52:12.591Z\\\", \\\"updated_at\\\": \\\"2026-05-21T06:33:44.219Z\\\", \\\"metrics\\\": {\\\"lz_star\\\": 5.4175, \\\"acc_overall\\\": 0.5138, \\\"acc_seen\\\": null, \\\"acc_unseen\\\": 0.5138, \\\"theta_mle\\\": -1.1569, \\\"lz_star_seen\\\": null, \\\"lz_star_unseen\\\": 5.4175, \\\"method\\\": \\\"Snijders (2001) lz*\\\"}, \\\"conclusion\\\": \\\"success\\\", \\\"hypothesis\\\": \\\"A Mistral-7B model fine-tuned on clean MMLU data (no benchmark leakage) will produce a response pattern consistent with IRT expectations, yielding lz* near zero, serving as the uncontaminated baseline for comparison.\\\"}, \\\"exp-baseline-comparison\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-21T03:55:49.688Z\\\", \\\"updated_at\\\": \\\"2026-05-21T05:07:41.388Z\\\", \\\"hypothesis\\\": \\\"IRT-based lz* detection outperforms binary-only baselines (accuracy z-score, LR, RF classifiers) on controlled contamination data, especially at low contamination rates (15%), because lz* leverages item-level difficulty calibration unavailable to methods operating on aggregate or uncalibrated binary vectors\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"model_level\\\": {\\\"qwen_contam15_lz_star_d\\\": -3.42, \\\"qwen_contam50_lz_star_d\\\": -0.99, \\\"llama_contam15_lz_star_d\\\": -2.95, \\\"llama_contam50_lz_star_d\\\": -3.31, \\\"qwen_contam15_acc_zscore_d\\\": 160.6, \\\"qwen_contam15_ht_d\\\": 3.21, \\\"llama_contam15_u3_d\\\": -3.69}, \\\"item_level_auroc\\\": {\\\"lz_star_itemwise\\\": {\\\"qwen_15\\\": 0.536, \\\"qwen_50\\\": 0.535, \\\"llama_15\\\": 0.528, \\\"llama_50\\\": 0.536}, \\\"irt_residual\\\": {\\\"qwen_15\\\": 0.578, \\\"qwen_50\\\": 0.563, \\\"llama_15\\\": 0.582, \\\"llama_50\\\": 0.581}, \\\"lr_cross_model\\\": {\\\"qwen_15\\\": 0.586, \\\"qwen_50\\\": 0.567, \\\"llama_15\\\": 0.592, \\\"llama_50\\\": 0.585}, \\\"rf_within_model\\\": {\\\"qwen_50\\\": 0.63, \\\"llama_50\\\": 0.629}, \\\"random\\\": 0.5}, \\\"conclusion_summary\\\": \\\"Model-level: all methods detect contamination (lz* d=-2.95~-3.42). Item-level: all methods weak (max AUROC=0.63 with oracle). lz* advantage = unsupervised + interpretable, not item-level superiority.\\\"}}, \\\"exp-ctrl-contam-llama-clean\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-20T20:55:36.448Z\\\", \\\"updated_at\\\": \\\"2026-05-21T05:04:02.710Z\\\", \\\"hypothesis\\\": \\\"A Llama-3.1-8B-Instruct model fine-tuned on clean Alpaca data (no MMLU contamination) will show normal person-fit statistics (lz* within expected range), serving as the uncontaminated baseline for comparison with contaminated conditions.\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"lz_star\\\": 0.8446, \\\"acc\\\": 0.5914, \\\"theta\\\": -0.6661, \\\"seed\\\": 42, \\\"method\\\": \\\"Snijders (2001) lz*\\\"}}, \\\"exp-ctrl-contam-llama-clean-s3\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-20T23:18:06.724Z\\\", \\\"updated_at\\\": \\\"2026-05-21T02:56:14.317Z\\\", \\\"hypothesis\\\": \\\"Third independent clean Llama-3.1-8B-Instruct baseline (seed=456) for Cohen's d variance estimation: matches Qwen n=3 protocol for cross-family effect size comparison\\\", \\\"parent\\\": \\\"exp-ctrl-contam-llama\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"lz_star\\\": -1.0844, \\\"acc\\\": 0.5943, \\\"theta\\\": -0.64, \\\"seed\\\": 456, \\\"method\\\": \\\"Snijders (2001) lz*\\\"}}, \\\"exp-ctrl-contam-llama-clean-s2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-20T23:18:06.128Z\\\", \\\"updated_at\\\": \\\"2026-05-21T02:56:13.752Z\\\", \\\"hypothesis\\\": \\\"Second independent clean Llama-3.1-8B-Instruct baseline (seed=123) for Cohen's d variance estimation: n=3 clean baselines needed for reliable cross-family effect size comparison with Qwen\\\", \\\"parent\\\": \\\"exp-ctrl-contam-llama\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"lz_star\\\": -0.1823, \\\"acc\\\": 0.5954, \\\"theta\\\": -0.63, \\\"seed\\\": 123, \\\"method\\\": \\\"Snijders (2001) lz*\\\"}}, \\\"exp-ctrl-contam-llama\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-20T20:23:08.451Z\\\", \\\"updated_at\\\": \\\"2026-05-21T01:53:06.443Z\\\", \\\"hypothesis\\\": \\\"The lz* contamination detection signal generalizes across model families: Llama-3.1-8B-Instruct (Meta) under the same QLoRA contamination protocol as Qwen2.5-7B (Alibaba) produces comparable Δlz* effect sizes, directly addressing reviewer concern REV-ADD-2 about single-model generalizability\\\", \\\"parent\\\": \\\"exp-ctrl-contam-pilot\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"lz_star_corrected\\\": true, \\\"method\\\": \\\"Snijders (2001) lz*\\\", \\\"clean_lz_star\\\": 0.8446, \\\"clean_s2_lz_star\\\": -0.1823, \\\"clean_s3_lz_star\\\": -1.0844, \\\"clean_mean_lz_star\\\": -0.1407, \\\"clean_std_lz_star\\\": 0.9652, \\\"clean_acc\\\": 0.5914, \\\"clean_theta\\\": -0.6661, \\\"contam_15_lz_star\\\": -2.9922, \\\"contam_15_acc\\\": 0.6654, \\\"contam_15_theta\\\": -0.276, \\\"contam_15_delta_lz_star\\\": -2.8515, \\\"contam_50_lz_star\\\": -3.3313, \\\"contam_50_acc\\\": 0.6983, \\\"contam_50_theta\\\": -0.149, \\\"contam_50_delta_lz_star\\\": -3.1906, \\\"cohens_d_contam_15_ddof1\\\": -2.95, \\\"cohens_d_contam_50_ddof1\\\": -3.31, \\\"theta_fixed\\\": -0.666, \\\"contam_15_lz_star_fixed\\\": 0.959, \\\"contam_50_lz_star_fixed\\\": 1.172, \\\"dose_response_ratio_free\\\": 1.09, \\\"dose_response_ratio_fixed\\\": 2.87, \\\"monotonic_free\\\": true, \\\"monotonic_fixed\\\": true}}, \\\"exp-ctrl-contam-pilot-clean-s3\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-20T19:04:43.485Z\\\", \\\"updated_at\\\": \\\"2026-05-20T20:19:33.382Z\\\", \\\"hypothesis\\\": \\\"Third clean seed (seed=456) for baseline lz* variance estimation: adding a third independent clean control strengthens Cohen's d denominator (n=3 vs n=2), providing more reliable effect size estimates for contamination detection\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"lz_star\\\": 8.0806, \\\"accuracy\\\": 0.6783, \\\"theta_mle\\\": -0.1068, \\\"cohens_d_n3\\\": {\\\"contam_15\\\": {\\\"delta\\\": -4.34, \\\"d\\\": -3.58}, \\\"contam_50\\\": {\\\"delta\\\": -1.9, \\\"d\\\": -1.56}}, \\\"baseline_n3\\\": {\\\"mean\\\": 7.3449, \\\"std\\\": 1.2137}, \\\"baseline_n2\\\": {\\\"mean\\\": 6.9771, \\\"std\\\": 1.4609}}}, \\\"exp-ctrl-contam-pilot-contam-50\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"created_at\\\": \\\"2026-05-20T16:16:45.230Z\\\", \\\"updated_at\\\": \\\"2026-05-20T16:16:45.230Z\\\"}, \\\"exp-ctrl-contam-pilot-contam-15\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"created_at\\\": \\\"2026-05-20T16:16:44.033Z\\\", \\\"updated_at\\\": \\\"2026-05-20T16:16:44.033Z\\\"}, \\\"exp-ctrl-contam-pilot-clean-s2\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"created_at\\\": \\\"2026-05-20T16:16:42.617Z\\\", \\\"updated_at\\\": \\\"2026-05-20T16:16:42.617Z\\\"}, \\\"exp-ctrl-contam-pilot-clean-s1\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"created_at\\\": \\\"2026-05-20T16:16:36.780Z\\\", \\\"updated_at\\\": \\\"2026-05-20T16:16:36.780Z\\\"}, \\\"exp-v1-irt-refit-expanded\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-20T12:54:04.798Z\\\", \\\"updated_at\\\": \\\"2026-05-20T14:44:22.448Z\\\", \\\"hypothesis\\\": \\\"With N≥500 models (vs pilot N=63), MML-EM estimation of discrimination parameters will improve substantially (a_pearson_r > 0.4 vs PSN-IRT), because the pilot's a_r=0.111 was primarily caused by catastrophically low N:J ratio (0.0045) rather than fundamental incompatibility between classical IRT and neural IRT parameterizations\\\", \\\"parent\\\": \\\"exp-v1-irt-refit-pilot\\\", \\\"conclusion\\\": \\\"negative\\\", \\\"metrics\\\": {\\\"n_models_downloaded\\\": 178, \\\"n_items\\\": 14042, \\\"3pl_a_pearson_r\\\": 0.127, \\\"2pl_a_pearson_r\\\": -0.029, \\\"3pl_b_pearson_r\\\": 0.663, \\\"reason\\\": \\\"N=178 classical refit: a_r=0.127 (3PL), -0.029 (2PL), b_r=0.663. Discrimination failure confirms Path D dead.\\\"}}, \\\"exp-4pl-real-data-degradation\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-20T14:29:58.285Z\\\", \\\"updated_at\\\": \\\"2026-05-20T14:41:27.206Z\\\", \\\"hypothesis\\\": \\\"Forcing d=1.0 (3PL degradation) on PSN-IRT 4PL parameters systematically distorts lz* values for real LLM response data, with the largest distortion on benchmarks/models where items have low d_feasibility, providing empirical evidence (beyond simulation) that the 4PL upper asymptote is essential for accurate person-fit measurement in LLM evaluation\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"correlation_4pl_vs_3pl\\\": {\\\"pearson_r\\\": 0.225, \\\"rmse\\\": 68.41}, \\\"most_affected_benchmark\\\": \\\"MMLU (mean |Δlz*|=58.3, 46% items d<0.95)\\\", \\\"most_affected_model\\\": \\\"DeepSeek-V3 (θ=3.77): 3PL lz* from +16.4 to -340.6\\\", \\\"low_ability_models_impact\\\": \\\"|Δlz*|<2 (Gemma-2B-it, Vicuna, Mistral)\\\", \\\"bias_direction\\\": \\\"3PL systematically depresses high-ability models' lz* (d=1 makes P→1, amplifying few-error aberrance)\\\", \\\"key_finding\\\": \\\"Ignoring d parameter makes lz* completely unreliable for high-ability models — d-induced bias far exceeds any contamination signal\\\"}}, \\\"exp-4pl-ablation\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-20T13:02:59.785Z\\\", \\\"updated_at\\\": \\\"2026-05-20T13:50:29.519Z\\\", \\\"hypothesis\\\": \\\"The 4PL model's upper asymptote parameter d significantly improves contamination detection sensitivity compared to 3PL(d=1) and 2PL(c=0.25,d=1), because d captures ceiling effects in LLM response patterns that mask contamination signal when fixed at 1.0\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"hypothesis_confirmed\\\": true, \\\"far_4pl\\\": \\\"~5% (well-calibrated)\\\", \\\"far_3pl\\\": \\\"4.7-16.5% (inflated)\\\", \\\"far_2pl\\\": \\\"50-100% (catastrophic, unusable)\\\", \\\"mean_power_gain_4pl_vs_3pl\\\": {\\\"MMLU\\\": \\\"+27.3pp\\\", \\\"HellaSwag\\\": \\\"+26.1pp\\\", \\\"GSM8K\\\": \\\"+20.3pp\\\", \\\"ARC_C\\\": \\\"+14.8pp\\\", \\\"HumanEval\\\": \\\"+13.7pp\\\"}, \\\"max_power_gain_4pl_vs_3pl\\\": {\\\"MMLU\\\": \\\"+49.0pp\\\", \\\"HellaSwag\\\": \\\"+59.6pp\\\", \\\"GSM8K\\\": \\\"+39.7pp\\\", \\\"ARC_C\\\": \\\"+54.6pp\\\", \\\"HumanEval\\\": \\\"+30.6pp\\\"}, \\\"power_at_25pct\\\": {\\\"4PL\\\": {\\\"MMLU\\\": 0.776, \\\"HellaSwag\\\": 0.534, \\\"GSM8K\\\": 0.73, \\\"ARC_C\\\": 0.132, \\\"HumanEval\\\": 0.318}, \\\"3PL\\\": {\\\"MMLU\\\": 0.329, \\\"HellaSwag\\\": 0.28, \\\"GSM8K\\\": 0.334, \\\"ARC_C\\\": 0.091, \\\"HumanEval\\\": 0.165}}, \\\"d_bucket_analysis\\\": \\\"d<0.8: +6.8pp to +61.2pp; d>=0.95: negligible\\\", \\\"key_finding\\\": \\\"4PL d parameter essential for LLM contamination detection. 46% MMLU items have d<0.95. Ignoring d (3PL) halves detection power on average. 2PL completely miscalibrated (FAR 50-100%).\\\"}}, \\\"exp-natural-experiment\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-20T12:49:47.067Z\\\", \\\"updated_at\\\": \\\"2026-05-20T13:21:26.297Z\\\", \\\"hypothesis\\\": \\\"Base→chat model pairs from v1 leaderboard exhibit benchmark-specific Δlz* anomalies: instruction-tuning produces a consistent cross-benchmark Δlz* shift, but contamination on specific benchmarks manifests as outlier Δlz* on those benchmarks relative to the pair's mean Δlz* across benchmarks\\\", \\\"parent\\\": \\\"exp-v1-irt-refit-pilot\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"n_pairs\\\": 21, \\\"n_benchmarks\\\": 4, \\\"n_complete_pairs\\\": 9, \\\"significant_benchmarks\\\": {\\\"HellaSwag\\\": {\\\"mean_deviation\\\": -3.4, \\\"t_stat\\\": -3.97, \\\"p_value\\\": 0.001, \\\"interpretation\\\": \\\"SFT systematically decreases person-fit on HellaSwag\\\"}, \\\"GSM8K\\\": {\\\"mean_deviation\\\": 3.92, \\\"t_stat\\\": 3.35, \\\"p_value\\\": 0.009, \\\"interpretation\\\": \\\"SFT systematically increases person-fit on GSM8K\\\"}}, \\\"non_significant_benchmarks\\\": {\\\"MMLU\\\": {\\\"p_value\\\": 0.15}, \\\"ARC-Challenge\\\": {\\\"p_value\\\": 0.38}}, \\\"individual_outliers\\\": 0, \\\"key_finding\\\": \\\"HellaSwag and GSM8K show significant systematic SFT effects on lz*, but no individual pair shows benchmark-specific contamination outliers. P2-optional per Director assessment.\\\"}}, \\\"exp-domain-analysis\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-20T13:03:00.736Z\\\", \\\"updated_at\\\": \\\"2026-05-20T13:13:27.728Z\\\", \\\"hypothesis\\\": \\\"Gemini-1.5's MMLU anomaly (lz*=+31.8) is domain-concentrated rather than uniform across all 57 subjects, and other flagged models show distinct domain-specific contamination signatures that differ from Gemini-1.5's pattern\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"gemini_mmlu_accuracy\\\": \\\"100% (14042/14042)\\\", \\\"gemini_domain_concentrated\\\": false, \\\"gemini_subjects_flagged\\\": \\\"50/57 (lz*>1.96)\\\", \\\"gemini_category_lz\\\": {\\\"STEM\\\": 21.2, \\\"Humanities\\\": 17.9, \\\"Social Sciences\\\": 15.9, \\\"Other\\\": 15.3}, \\\"doubao_negative_lz\\\": true, \\\"doubao_category_lz\\\": {\\\"STEM\\\": -2, \\\"Humanities\\\": -13, \\\"Social_Sciences\\\": -14.8, \\\"Other\\\": 4.4}, \\\"hunyuan_uneven\\\": {\\\"STEM\\\": 1.8, \\\"Social_Sciences\\\": 13.9}, \\\"yi_lightning_highest_mmlu_lz\\\": 48.2, \\\"qwen_plus_second_highest\\\": 44.9, \\\"mistral_flagged_subjects\\\": \\\"55/57\\\"}}, \\\"exp-ml-classifier-baseline\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-20T11:57:38.101Z\\\", \\\"updated_at\\\": \\\"2026-05-20T12:42:10.990Z\\\", \\\"hypothesis\\\": \\\"ML classifiers (logistic regression, random forest) trained on binary response vectors cannot significantly outperform lz* in contamination detection AUROC on simulated data, because binary response patterns contain limited higher-order information beyond what lz* already captures via the IRT likelihood\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"auroc_avg_25pct\\\": {\\\"lz_star\\\": 0.86, \\\"lr_resp\\\": 0.899, \\\"rf_resp\\\": 0.885, \\\"lr_resp_summ\\\": 0.909, \\\"rf_resp_summ\\\": 0.913}, \\\"auroc_avg_5pct\\\": {\\\"lz_star\\\": 0.675, \\\"best_ml\\\": 0.575}, \\\"auroc_avg_10pct\\\": {\\\"lz_star\\\": 0.763, \\\"best_ml\\\": 0.712}, \\\"lz_star_advantage_low_contam\\\": \\\"+0.10 AUROC at 5%, +0.05 at 10%\\\", \\\"ml_advantage_high_contam\\\": \\\"+0.05 at 25%, +0.16 at 50%\\\", \\\"key_finding\\\": \\\"lz* outperforms supervised ML at low contamination (5-10%) without any training data; ML only wins at 25%+ where signal is already strong\\\"}}, \\\"exp-v1-irt-refit-pilot\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-20T10:56:48.899Z\\\", \\\"updated_at\\\": \\\"2026-05-20T12:32:16.129Z\\\", \\\"hypothesis\\\": \\\"IRT parameters fitted from v1 leaderboard response data using MML-EM will produce item parameters correlated (r>0.7 for a,b) with PSN-IRT neural-network-estimated parameters, enabling internally consistent person-fit analysis on v1 models.\\\", \\\"parent\\\": \\\"exp-item-alignment-check\\\", \\\"metrics\\\": {\\\"n_models_downloaded\\\": 63, \\\"n_models_failed\\\": 38, \\\"n_items\\\": 14042, \\\"n_mapped_items\\\": 12441, \\\"overall_accuracy\\\": 0.426, \\\"fitting_time_2pl_sec\\\": 8.9, \\\"fitting_time_3pl_sec\\\": 12.1, \\\"3pl_a_pearson_r\\\": 0.111, \\\"3pl_b_pearson_r\\\": 0.626, \\\"3pl_b_spearman_r\\\": 0.656, \\\"2pl_a_pearson_r\\\": -0.084, \\\"2pl_b_pearson_r\\\": 0.572, \\\"lz_star_mean\\\": 11.69, \\\"lz_star_std\\\": 6.68, \\\"lz_star_flagged_pct\\\": 1.6}, \\\"conclusion\\\": \\\"negative\\\"}, \\\"exp-clean-control-delta\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-20T11:57:39.694Z\\\", \\\"updated_at\\\": \\\"2026-05-20T12:08:35.683Z\\\", \\\"hypothesis\\\": \\\"Δlz* between two independent clean response vectors (same θ, different random seeds) has E[Δlz*]≈0 and controlled variance, confirming that non-zero Δlz* in contamination experiments reflects genuine contamination signal rather than estimation noise\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"clean_vs_clean_mean_abs\\\": {\\\"mmlu\\\": 0.01, \\\"hellaswag\\\": 0.125, \\\"gsm8k\\\": 0.021, \\\"arc_c\\\": 0.095, \\\"humaneval\\\": 0.02}, \\\"clean_vs_clean_all_nonsig\\\": true, \\\"clean_vs_contam_all_sig\\\": true, \\\"cohens_d\\\": {\\\"mmlu\\\": 2.66, \\\"hellaswag\\\": 1.85, \\\"gsm8k\\\": 1.85, \\\"arc_c\\\": 0.45, \\\"humaneval\\\": 1.07}, \\\"arc_c_note\\\": \\\"d=0.45 < 0.5 threshold due to only 295 items, but still p<1e-10\\\"}}, \\\"exp-fdr-correction\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-20T11:57:39.228Z\\\", \\\"updated_at\\\": \\\"2026-05-20T12:04:41.646Z\\\", \\\"hypothesis\\\": \\\"BH-FDR correction on the 60-cell cross-benchmark analysis preserves the key finding that nearly all LLM-benchmark cells show significant misfit, with corrected flagging rate remaining above 80%\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"flagged_uncorrected\\\": \\\"57/60 (95%)\\\", \\\"flagged_bh_fdr\\\": \\\"57/60 (95%)\\\", \\\"flagged_bonferroni\\\": \\\"not_computed_but_expected_similar\\\", \\\"correction_scope\\\": \\\"global_60_tests\\\", \\\"unflagged_cells\\\": [\\\"Yi-Lightning×arc_c (bh_p=0.098)\\\", \\\"360GPT2-Pro×humaneval (bh_p=0.134)\\\", \\\"Yi-Lightning×humaneval (bh_p=0.181)\\\"], \\\"note\\\": \\\"Reused existing BH-FDR from exp-two-sided v2 empirical_pvalues.csv. Leaderboard-scale FDR (24800+ tests) deferred to leaderboard audit.\\\"}}, \\\"exp-cross-benchmark-analysis\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-20T11:30:52.484Z\\\", \\\"updated_at\\\": \\\"2026-05-20T11:35:35.796Z\\\", \\\"hypothesis\\\": \\\"Cross-benchmark lz* anomaly profiles reveal distinct contamination patterns: models with selective benchmark contamination show high positive lz* on specific benchmarks but normal/negative on others, while models with natural misfit show consistently negative lz* across all benchmarks\\\", \\\"metrics\\\": {\\\"n_models_all5_flagged\\\": 10, \\\"n_models_selective_flagged\\\": 2, \\\"gemini15_cluster_isolation\\\": true, \\\"dominant_direction_pattern\\\": \\\"positive\\\", \\\"pct_positive_cells\\\": 93.3, \\\"total_flagged\\\": 57, \\\"flag_rate\\\": 0.95}, \\\"conclusion\\\": \\\"success\\\"}, \\\"exp-accuracy-zscore-baseline\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-20T11:30:51.761Z\\\", \\\"updated_at\\\": \\\"2026-05-20T11:33:55.426Z\\\", \\\"hypothesis\\\": \\\"Accuracy z-score baseline (|z|>1.96) flags far fewer cells than lz* because it only captures overall performance deviation without item-level pattern information — lz* provides strictly more information by detecting response pattern aberrance that accuracy alone misses\\\", \\\"metrics\\\": {\\\"z_flagged_count\\\": 4, \\\"lz_flagged_count\\\": 57, \\\"agreement_rate\\\": 0.117, \\\"gemini15_mmlu_zscore\\\": 1.413}, \\\"conclusion\\\": \\\"success\\\"}, \\\"exp-item-alignment-check\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-20T10:16:34.437Z\\\", \\\"updated_at\\\": \\\"2026-05-20T10:53:40.587Z\\\", \\\"hypothesis\\\": \\\"Open LLM Leaderboard v1 per-item responses share the same deterministic item ordering as PSN-IRT combine.csv (both generated by lm-eval-harness), enabling direct positional alignment of v1 response vectors with PSN-IRT 4PL item parameters without content-based matching\\\", \\\"parent\\\": \\\"exp-leaderboard-data-recon\\\", \\\"conclusion\\\": \\\"negative\\\", \\\"metrics\\\": {\\\"match_rate_direct\\\": 0.5456, \\\"match_rate_reordered_mistral\\\": 0.8846, \\\"match_rate_reordered_vicuna\\\": 0.7248, \\\"n_items_checked\\\": 14042, \\\"n_models_verified\\\": 2, \\\"alignment_method\\\": \\\"content-based via cais/mmlu canonical order\\\", \\\"items_mapped\\\": 12068, \\\"mapping_coverage\\\": 0.86}}, \\\"exp-power-theory\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-20T09:53:40.117Z\\\", \\\"updated_at\\\": \\\"2026-05-20T10:38:57.599Z\\\", \\\"hypothesis\\\": \\\"Detection power of lz* follows an analytic function of n_items and contamination level derivable from Snijders (2001) variance formula, and this theoretical curve explains the empirically observed inverted-U shape and n_items dependence with R²>0.95 against simulation data\\\", \\\"parent\\\": \\\"exp-extended-sim\\\", \\\"metrics\\\": {\\\"R2_two_sided\\\": 0.9572, \\\"RMSE_two_sided\\\": 0.0746, \\\"R2_left_tail\\\": 0.9764, \\\"R2_mean_lz\\\": 0.9948, \\\"sqrt_n_R2_avg\\\": 0.88, \\\"crossover_range_pct\\\": \\\"81-85%\\\", \\\"min_items_15pct_80power\\\": 7958}, \\\"conclusion\\\": \\\"success\\\"}, \\\"exp-empirical-null\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-20T09:53:38.594Z\\\", \\\"updated_at\\\": \\\"2026-05-20T10:02:04.668Z\\\", \\\"hypothesis\\\": \\\"Bootstrap empirical null of lz* under 4PL model shows systematic positive bias (mean>>0) and inflated variance (std>>1) for real LLM response data, quantifying the degree to which LLMs violate IRT local independence/unidimensionality assumptions — this bias explains why 95% of cells are flagged with absolute thresholds\\\", \\\"parent\\\": \\\"exp-two-sided\\\", \\\"metrics\\\": {\\\"n_boot\\\": 1000, \\\"n_cells\\\": 60, \\\"mean_null_bias\\\": 0.0925, \\\"mean_null_std\\\": 1.0021, \\\"ks_reject_rate\\\": 0.4, \\\"ks_reject_count\\\": \\\"24/60\\\", \\\"bias_by_benchmark\\\": {\\\"arc_c\\\": 0.146, \\\"gsm8k\\\": 0.082, \\\"hellaswag\\\": 0.034, \\\"humaneval\\\": 0.16, \\\"mmlu\\\": 0.041}, \\\"std_by_benchmark\\\": {\\\"arc_c\\\": 1.004, \\\"gsm8k\\\": 1.01, \\\"hellaswag\\\": 0.999, \\\"humaneval\\\": 0.994, \\\"mmlu\\\": 1.003}, \\\"ks_reject_by_benchmark\\\": {\\\"arc_c\\\": 0.583, \\\"gsm8k\\\": 0.5, \\\"hellaswag\\\": 0.083, \\\"humaneval\\\": 0.75, \\\"mmlu\\\": 0.083}, \\\"key_finding\\\": \\\"Null bias is small (mean=0.09) and std is near 1.0 — the bootstrap null is well-calibrated. The 95% flagging rate is NOT caused by miscalibrated null but by genuine extreme lz* values in LLM data. Smaller benchmarks (humaneval, arc_c) show higher KS rejection rates due to stronger finite-sample deviations from normality.\\\"}, \\\"conclusion\\\": \\\"negative\\\"}, \\\"exp-leaderboard-data-recon\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-20T09:53:39.512Z\\\", \\\"updated_at\\\": \\\"2026-05-20T10:00:22.466Z\\\", \\\"hypothesis\\\": \\\"Open LLM Leaderboard v1 results repo on HuggingFace contains per-item binary response logs (not just aggregate scores) for a substantial number of models, enabling large-scale person-fit analysis without running inference ourselves\\\", \\\"metrics\\\": {\\\"n_models_with_per_item_data\\\": \\\"13000+\\\", \\\"benchmarks_covered\\\": \\\"4/5 (MMLU, HellaSwag, ARC-Challenge, GSM8K; missing HumanEval)\\\", \\\"estimated_gpu_hours_if_needed\\\": 0, \\\"v1_benchmarks\\\": 6, \\\"v2_benchmarks\\\": 6, \\\"data_format\\\": \\\"parquet per-item rows with acc/acc_norm binary fields\\\", \\\"source\\\": \\\"open-llm-leaderboard-old/details_{model}\\\", \\\"humaneval_gpu_hrs_per_7b_model\\\": 0.08, \\\"key_finding\\\": \\\"v1 details datasets contain per-item binary responses for 13K+ models. Zero GPU cost for 4/5 benchmarks.\\\"}, \\\"conclusion\\\": \\\"success\\\"}, \\\"exp-extended-sim\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-20T09:31:30.112Z\\\", \\\"updated_at\\\": \\\"2026-05-20T09:50:31.545Z\\\", \\\"hypothesis\\\": \\\"Extended simulation with finer contamination levels (60/75/90%) and fixed 100% NaN handling will reveal the precise dual-regime crossover point where lz* flips from negative (aberrant) to positive (over-consistent), and inverted-U power curve shape is confirmed across all benchmarks\\\", \\\"parent\\\": \\\"sim_001\\\", \\\"metrics\\\": {\\\"n_sims\\\": 2000, \\\"levels\\\": \\\"0/3/5/10/15/25/50/60/75/90/100\\\", \\\"n_excluded_100pct\\\": 0, \\\"inverted_u_all_5\\\": true, \\\"dual_regime_crossover\\\": \\\"75-90%\\\", \\\"mmlu_power_15pct\\\": 0.9845, \\\"hellaswag_power_15pct\\\": 0.7525, \\\"gsm8k_power_15pct\\\": 0.5905, \\\"mmlu_100pct_lz_star\\\": 31.815, \\\"hellaswag_100pct_lz_star\\\": 26.297, \\\"gsm8k_100pct_lz_star\\\": 8.253, \\\"arc_c_100pct_lz_star\\\": 4.339, \\\"humaneval_100pct_lz_star\\\": 3.529, \\\"two_sided_power\\\": {\\\"mmlu_15pct\\\": 0.978, \\\"mmlu_50pct\\\": 0.9525, \\\"mmlu_75pct\\\": 0.936, \\\"mmlu_90pct\\\": 0.9515, \\\"mmlu_100pct\\\": 1, \\\"hellaswag_25pct\\\": 0.9155, \\\"hellaswag_50pct\\\": 0.9475, \\\"hellaswag_90pct\\\": 0.9375, \\\"hellaswag_100pct\\\": 1, \\\"gsm8k_50pct\\\": 0.837, \\\"gsm8k_90pct\\\": 0.794, \\\"gsm8k_100pct\\\": 1}, \\\"key_finding\\\": \\\"Two-sided detection eliminates inverted-U: MMLU two-sided power >93% at ALL contamination levels. 100% contamination → 100% detection on all benchmarks.\\\"}, \\\"conclusion\\\": \\\"success\\\"}, \\\"exp-two-sided\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-20T09:13:53.986Z\\\", \\\"updated_at\\\": \\\"2026-05-20T09:14:27.223Z\\\", \\\"hypothesis\\\": \\\"Two-sided detection (|lz*| > threshold) with benchmark-specific θ MLE + parametric bootstrap empirical null + BH-FDR control will reduce Phase B flagging rate from 93% to a reasonable level (<20%), isolating genuine contamination signals from θ estimation bias\\\", \\\"parent\\\": \\\"phase_b_personfit\\\", \\\"metrics\\\": {\\\"flagged_rate\\\": \\\"57/60 (95.0%)\\\", \\\"n_boot\\\": 1000, \\\"fdr_alpha\\\": 0.05, \\\"flagged_positive\\\": 51, \\\"flagged_negative\\\": 6, \\\"unflagged\\\": 3, \\\"unflagged_cells\\\": \\\"Yi-Lightning/arc_c (p=0.098), 360GPT2-Pro/humaneval (p=0.134), Yi-Lightning/humaneval (p=0.181)\\\", \\\"gemini15_mmlu_lz_star_v2\\\": 31.815, \\\"gemini15_mmlu_theta_bench\\\": 4, \\\"gemini15_mmlu_p_emp\\\": 0, \\\"key_finding\\\": \\\"Benchmark-specific θ + bootstrap + FDR does NOT reduce flagging. LLMs universally violate 4PL assumptions.\\\"}, \\\"conclusion\\\": \\\"negative\\\"}, \\\"phase_b_personfit\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-20T08:34:21.694Z\\\", \\\"updated_at\\\": \\\"2026-05-20T08:34:56.735Z\\\", \\\"hypothesis\\\": \\\"Real LLM benchmark response data from PSN-IRT 12 models shows significant inter-model variation in person-fit statistics (lz*, outfit, infit), with specific models exhibiting anomalous patterns indicative of benchmark contamination — particularly Gemini-1.5 with accuracy-ability dissociation\\\", \\\"metrics\\\": {\\\"lz_star_sd_all_gt_0.5\\\": true, \\\"mmlu_lz_star_mean\\\": 24.19, \\\"mmlu_lz_star_sd\\\": 16.47, \\\"hellaswag_lz_star_mean\\\": 20.09, \\\"hellaswag_lz_star_sd\\\": 17.59, \\\"gsm8k_lz_star_mean\\\": 8.22, \\\"gsm8k_lz_star_sd\\\": 8.97, \\\"gemini15_mmlu_lz_star\\\": 34.75, \\\"gemini15_mmlu_accuracy\\\": 1, \\\"gemini15_mmlu_theta\\\": 0.78, \\\"gemini15_flagged_benchmarks\\\": \\\"3/5 (HellaSwag, GSM8K, HumanEval negative lz*)\\\", \\\"cross_benchmark_spearman_significant\\\": \\\"1/10 (GSM8K vs HumanEval rho=0.62 p=0.031)\\\", \\\"n_models\\\": 12, \\\"n_benchmarks\\\": 5}, \\\"conclusion\\\": \\\"success\\\"}, \\\"sim_001\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-20T07:13:53.208Z\\\", \\\"updated_at\\\": \\\"2026-05-20T08:09:31.642Z\\\", \\\"hypothesis\\\": \\\"Under 4PL IRT model, lz* person-fit statistic can detect partial benchmark contamination (5-30% items) with >80% power at α=0.05, and detection power follows an inverted-U curve across contamination levels (low contamination undetectable, moderate contamination most detectable, high contamination mimics high ability)\\\", \\\"conclusion\\\": \\\"negative\\\", \\\"metrics\\\": {\\\"null_check\\\": {\\\"all_pass\\\": true, \\\"gsm8k_ks_p\\\": 0.098, \\\"hellaswag_ks_p\\\": 0.224, \\\"mmlu_ks_p\\\": 0.594}, \\\"simulation_power_at_15pct\\\": {\\\"mmlu\\\": 0.979, \\\"hellaswag\\\": 0.733, \\\"gsm8k\\\": 0.578, \\\"arc_c\\\": 0.129, \\\"humaneval\\\": 0.243}, \\\"global_pass\\\": false, \\\"inverted_u_all_benchmarks\\\": true, \\\"pass_count_large_80pct\\\": \\\"1/3 (mmlu only)\\\"}}}, \\\"count\\\": 67, \\\"total\\\": 67, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.2353}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"exp-arcc-clean-s10\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T12:48:49.366Z\", \"updated_at\": \"2026-05-21T13:05:54.577Z\", \"hypothesis\": \"ARC-Challenge clean baseline (seed=307) for cross-benchmark Cohen's d — expanding clean lz* distribution\", \"parent\": \"exp-arcc-benchmark\", \"conclusion\": \"success\", \"metrics\": {\"theta_mle\": 0.8111, \"lz_star\": -5.0733, \"accuracy\": 0.9051, \"n_items\": 295}}, \"exp-arcc-clean-s9\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T12:48:48.480Z\", \"updated_at\": \"2026-05-21T13:05:53.688Z\", \"hypothesis\": \"ARC-Challenge clean baseline (seed=306) for cross-benchmark Cohen's d — expanding clean lz* distribution\", \"parent\": \"exp-arcc-benchmark\", \"conclusion\": \"success\", \"metrics\": {\"theta_mle\": 0.8868, \"lz_star\": -5.5359, \"accuracy\": 0.9017, \"n_items\": 295}}, \"exp-arcc-clean-s8\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T12:48:47.531Z\", \"updated_at\": \"2026-05-21T13:05:52.824Z\", \"hypothesis\": \"ARC-Challenge clean baseline (seed=305) for cross-benchmark Cohen's d — expanding clean lz* distribution\", \"parent\": \"exp-arcc-benchmark\", \"conclusion\": \"success\", \"metrics\": {\"theta_mle\": 0.8511, \"lz_star\": -5.4001, \"accuracy\": 0.9051, \"n_items\": 295}}, \"exp-arcc-clean-s7\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T12:48:46.522Z\", \"updated_at\": \"2026-05-21T13:05:51.824Z\", \"hypothesis\": \"ARC-Challenge clean baseline (seed=304) for cross-benchmark Cohen's d — expanding clean lz* distribution\", \"parent\": \"exp-arcc-benchmark\", \"conclusion\": \"success\", \"metrics\": {\"theta_mle\": 0.7058, \"lz_star\": -5.5852, \"accuracy\": 0.8915, \"n_items\": 295}}, \"exp-ctrl-contam-llama-clean-s10\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-21T13:03:57.523Z\", \"updated_at\": \"2026-05-21T13:04:26.843Z\", \"hypothesis\": \"Independent clean Llama-3.1-8B-Instruct baseline (seed=307) for n=10 Cohen's d variance estimation\", \"parent\": \"exp-ctrl-contam-llama-contam15\"}, \"exp-ctrl-contam-llama-clean-s9\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-21T13:03:56.214Z\", \"updated_at\": \"2026-05-21T13:04:25.842Z\", \"hypothesis\": \"Independent clean Llama-3.1-8B-Instruct baseline (seed=306) for n=10 Cohen's d variance estimation\", \"parent\": \"exp-ctrl-contam-llama-contam15\"}, \"exp-ctrl-contam-llama-clean-s8\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-21T13:03:54.282Z\", \"updated_at\": \"2026-05-21T13:04:24.947Z\", \"hypothesis\": \"Independent clean Llama-3.1-8B-Instruct baseline (seed=305) for n=10 Cohen's d variance estimation\", \"parent\": \"exp-ctrl-contam-llama-contam15\"}, \"eval-mistral-clean-s3\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T12:59:20.651Z\", \"updated_at\": \"2026-05-21T13:00:42.054Z\", \"hypothesis\": \"Mistral clean_s3 (seed 3) LoRA adapter trained on clean MMLU data will show lz* near zero, consistent with no contamination signal in the IRT person-fit framework.\", \"metrics\": {\"theta_mle\": -0.9733, \"lz_star\": 3.2792, \"accuracy_overall\": 0.5413, \"n_items\": 14042}, \"conclusion\": \"success\"}, \"eval-mistral-clean-s2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T12:59:19.645Z\", \"updated_at\": \"2026-05-21T13:00:41.390Z\", \"hypothesis\": \"Mistral clean_s2 (seed 2) LoRA adapter trained on clean MMLU data will show lz* near zero, consistent with no contamination signal in the IRT person-fit framework.\", \"metrics\": {\"theta_mle\": -0.9627, \"lz_star\": -1.0456, \"accuracy_overall\": 0.5428, \"n_items\": 14042}, \"conclusion\": \"success\"}, \"exp-post-rl-v3\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-21T12:45:42.860Z\", \"updated_at\": \"2026-05-21T12:47:34.274Z\", \"hypothesis\": \"GRPO with num_generations=16 + temperature=1.2 produces measurable parameter update while preserving lz* contamination signal (R7 post-RL robustness)\", \"parent\": \"exp-post-rl\"}, \"exp-post-rl\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T03:55:49.080Z\", \"updated_at\": \"2026-05-21T12:47:18.550Z\", \"hypothesis\": \"Post-RL (GRPO) training does not wash out contamination signal detectable by lz*: SFT-contaminated model retains negative Δlz* after GRPO alignment, demonstrating that IRT-based detection is robust to RL post-training — addressing reviewer concern R7 about SFT-only scope\", \"notes\": \"GRPO v1/v2 reward saturation (frac_reward_zero_std=1.0), zero gradient, model ≈ SFT. Restarting as exp-post-rl-v3 with fixed params (num_generations=16, temperature=1.2, max_steps=3000, save_steps=500).\", \"conclusion\": \"negative\"}, \"exp-ctrl-contam-llama-clean-s7\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T12:42:50.324Z\", \"updated_at\": \"2026-05-21T12:44:14.678Z\", \"hypothesis\": \"Clean SFT (seed 7) on Llama-3.1-8B should produce lz* near zero, indicating no person-fit anomaly without contamination.\", \"conclusion\": \"success\", \"metrics\": {\"theta_mle\": -0.6356, \"lz_star\": -0.4007, \"accuracy_overall\": 0.5929, \"n_items\": 14042}}, \"exp-ctrl-contam-llama-clean-s6\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T12:42:49.542Z\", \"updated_at\": \"2026-05-21T12:44:13.998Z\", \"hypothesis\": \"Clean SFT (seed 6) on Llama-3.1-8B should produce lz* near zero, indicating no person-fit anomaly without contamination.\", \"conclusion\": \"success\", \"metrics\": {\"theta_mle\": -0.6027, \"lz_star\": 2.8466, \"accuracy_overall\": 0.601, \"n_items\": 14042}}, \"exp-ctrl-contam-llama-clean-s5\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T12:42:48.174Z\", \"updated_at\": \"2026-05-21T12:44:13.366Z\", \"hypothesis\": \"Clean SFT (seed 5) on Llama-3.1-8B should produce lz* near zero, indicating no person-fit anomaly without contamination.\", \"conclusion\": \"success\", \"metrics\": {\"theta_mle\": -0.63, \"lz_star\": 1.7323, \"accuracy_overall\": 0.5965, \"n_items\": 14042}}, \"exp-ctrl-contam-llama-clean-s4\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T12:24:43.970Z\", \"updated_at\": \"2026-05-21T12:44:12.382Z\", \"hypothesis\": \"Clean SFT (seed 4) on Llama-3.1-8B should produce lz* near zero, indicating no person-fit anomaly without contamination.\", \"conclusion\": \"success\", \"metrics\": {\"theta_mle\": -0.6435, \"lz_star\": 0.0206, \"accuracy_overall\": 0.5923, \"n_items\": 14042}}, \"arcc-clean-s10\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-21T12:08:37.841Z\", \"updated_at\": \"2026-05-21T12:10:04.708Z\"}, \"arcc-clean-s9\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-21T12:08:35.737Z\", \"updated_at\": \"2026-05-21T12:10:03.378Z\"}, \"arcc-clean-s8\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-21T12:08:33.697Z\", \"updated_at\": \"2026-05-21T12:10:01.469Z\"}, \"arcc-clean-s7\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-21T12:08:32.282Z\", \"updated_at\": \"2026-05-21T12:10:00.031Z\"}, \"exp-ctrl-contam-pilot\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T13:54:01.818Z\", \"updated_at\": \"2026-05-21T11:44:22.927Z\", \"hypothesis\": \"Controlled contamination via QLoRA fine-tuning on MMLU items produces measurable Δlz* signal: (1) clean-vs-clean Δlz* ≈ 0 (seed1 vs seed2), confirming the noise floor; (2) 15% contamination produces significant negative Δlz* with Cohen's d > 1.0; (3) 50% contamination produces even stronger signal; (4) contamination signal concentrates on seen items (memorization fraction > 0.5)\", \"conclusion\": \"success\", \"metrics\": {\"cohens_d_contam15\": 6.575, \"cohens_d_contam15_ci\": [4.514, 15.199], \"cohens_d_contam50\": 1.897, \"cohens_d_contam50_ci\": [1.041, 4.923], \"clean_n10_mean_lz\": 8.684, \"clean_n10_sd_lz\": 0.735, \"contam15_lz\": 3.849, \"contam50_lz\": 7.289, \"n_clean_seeds\": 10, \"n_items\": 14042}, \"notes\": \"partial: H1✓ H2✓ H3✗(θ-shift, fixed analysis restores monotonicity) H4✗(memorization<0.5). θ-fixed=-0.0965 (n=3 mean). Snijders lz* corrected: dose-response ratio=3.12 (unchanged from Drasgow). Δlz*_fixed: contam_15=+3.169, contam_50=+9.893. All values use Snijders (2001) lz*.\"}, \"exp-arcc-benchmark\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-21T08:07:05.912Z\", \"updated_at\": \"2026-05-21T11:20:59.126Z\", \"hypothesis\": \"ℓz* contamination detection generalizes beyond MMLU to ARC-Challenge, a second benchmark with PSN-IRT 4PL calibration — demonstrating cross-benchmark applicability and addressing reviewer concern about single-benchmark evaluation.\", \"notes\": \"代码就绪: /root/autodl-tmp/ctrl_contam_arcc/ (prepare_arcc_data.py + train.py + eval_lz.py + arc_c_params.csv)。ARC-C: 295 items with 4PL params (294×4-choice + 1×3-choice), 15% contam=44 items, 50% contam=147 items。预期检测力有限 (sim_001 12.9% power) 但 cross-benchmark generalization 价值明确。数据已生成。等 GPU 可用后启动。\", \"metrics\": {\"19912_clean_s1_acc\": 0.902, \"19912_clean_s1_lz\": -5.448, \"19912_clean_s2_acc\": 0.895, \"19912_clean_s2_lz\": -5.433, \"19912_contam15_acc\": 0.909, \"19912_contam15_lz\": -4.917, \"19912_contam15_lz_seen\": 0.568, \"19912_contam50_acc\": 0.942, \"19912_contam50_lz\": -4.573, \"19912_contam50_lz_seen\": -0.331, \"35694_clean_s1_acc\": 0.895, \"35694_clean_s1_lz\": -5.511, \"35694_clean_s2_acc\": 0.898, \"35694_clean_s2_lz\": -5.493, \"35694_contam15_acc\": 0.909, \"35694_contam15_lz\": -5.032, \"35694_contam15_lz_seen\": 0.186, \"35694_contam50_acc\": 0.946, \"35694_contam50_lz\": -4.185, \"35694_contam50_lz_seen\": -0.475}}, \"exp-ctrl-contam-qwen-clean-s10\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-21T09:12:35.740Z\", \"updated_at\": \"2026-05-21T11:20:55.470Z\", \"hypothesis\": \"Tenth independent clean Qwen2.5-7B-Instruct baseline (seed=307) for n=10 Cohen's d variance estimation\", \"parent\": \"exp-ctrl-contam-pilot\", \"metrics\": {\"accuracy\": 0.676, \"lz_star\": 8.149, \"theta_mle\": -0.116, \"n_items\": 14042}}, \"exp-ctrl-contam-llama-contam50\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T20:57:09.849Z\", \"updated_at\": \"2026-05-21T11:15:59.751Z\", \"hypothesis\": \"50% MMLU contamination on Llama-3.1-8B-Instruct produces measurable Δlz* signal, with expected θ-shift effects comparable to Qwen pilot\", \"conclusion\": \"success\", \"metrics\": {\"lz_star\": -3.3313, \"acc\": 0.6983, \"theta_mle\": -0.149, \"acc_seen\": 0.735, \"acc_unseen\": 0.661, \"delta_lz_star\": -3.1906, \"cohens_d_ddof1\": -3.31, \"method\": \"Snijders (2001) lz*\"}}, \"exp-ctrl-contam-llama-contam15\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T20:57:08.665Z\", \"updated_at\": \"2026-05-21T11:15:59.136Z\", \"hypothesis\": \"15% MMLU contamination on Llama-3.1-8B-Instruct produces comparable Δlz* signal to Qwen2.5-7B (pilot d=-3.58), confirming cross-model generalizability\", \"conclusion\": \"success\", \"metrics\": {\"lz_star\": -2.9922, \"acc\": 0.6654, \"theta_mle\": -0.276, \"acc_seen\": 0.742, \"acc_unseen\": 0.652, \"delta_lz_star\": -2.8515, \"cohens_d_ddof1\": -2.95, \"method\": \"Snijders (2001) lz*\"}}, \"exp-constat-comparison\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-21T08:07:04.296Z\", \"updated_at\": \"2026-05-21T10:57:28.101Z\", \"hypothesis\": \"ConStat (NeurIPS 2024) requires multi-benchmark performance scores for contamination detection, making it inapplicable or underpowered in single-benchmark scenarios. ℓz* operates on binary response patterns from a single benchmark, demonstrating superior minimal-information detection capability.\", \"notes\": \"Bugfix 完成: (1) Snijders 方差校正已加 (2) 阈值方向修正为 abs(lz)>1.96 (3) RNG 隔离。修正后 clean lz* mean=-0.058≈0。仿真结果: 绝对 lz* power≈FAR 在所有 contam 级别（θ-shift 完全吸收信号），进一步证实 Δlz* 对比设计的必要性。ConStat 真实模型对比不可行（缺 reference benchmark + ≥5 reference models）。\"}, \"exp-arcc-clean-s1\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-21T09:12:36.602Z\", \"updated_at\": \"2026-05-21T10:57:23.992Z\", \"hypothesis\": \"ARC-Challenge clean baseline (seed=42) for cross-benchmark ℓz* detection — establishing clean lz* distribution on a second benchmark with PSN-IRT 4PL calibration\", \"parent\": \"exp-arcc-benchmark\", \"metrics\": {\"accuracy\": 0.8949, \"theta_mle\": 0.6872, \"lz_star\": -5.5107, \"n_items\": 295}}, \"exp-mia-mink-comparison\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-21T08:07:05.266Z\", \"updated_at\": \"2026-05-21T10:57:22.586Z\", \"hypothesis\": \"MIA methods (Min-K%/Min-K%++) fail to detect contamination in post-RL (GRPO) models because RL fine-tuning disrupts token-level log-prob distributions, while ℓz* remains effective because it operates on response-pattern-level statistics that survive RL post-training — demonstrating robustness advantage over MIA approaches.\", \"notes\": \"代码就绪: eval_mia.py (Loss/Min-K%/Min-K%++ K=10-50, AUC-ROC) + compare_mia_lz.py。路径: /root/autodl-tmp/post_rl_contam/。需 GPU ~1-2h/stage，等 GRPO 完成后执行。\", \"metrics\": {\"base_auc_loss\": 0.486, \"base_auc_mink10\": 0.493, \"base_auc_minkpp10\": 0.488, \"sft_auc_loss\": 0.592, \"sft_auc_mink10\": 0.611, \"sft_auc_minkpp10\": 0.569}}, \"exp-arcc-clean-s2\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-21T10:17:15.804Z\", \"updated_at\": \"2026-05-21T10:17:15.804Z\"}, \"exp-ctrl-contam-qwen-clean-s9\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T08:25:55.311Z\", \"updated_at\": \"2026-05-21T09:13:10.810Z\", \"hypothesis\": \"Ninth independent clean Qwen2.5-7B-Instruct baseline (seed=306) for n=10 Cohen's d variance estimation\", \"parent\": \"exp-ctrl-contam-pilot\", \"metrics\": {\"accuracy\": 0.6743, \"lz_star\": 9.013, \"theta_mle\": -0.1242, \"n_items\": 14042}, \"conclusion\": \"success\"}, \"exp-ctrl-contam-qwen-clean-s7\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T07:42:16.770Z\", \"updated_at\": \"2026-05-21T09:13:10.213Z\", \"hypothesis\": \"Seventh independent clean Qwen2.5-7B-Instruct baseline (seed=304) for n=10 Cohen's d\", \"parent\": \"exp-ctrl-contam-pilot\", \"metrics\": {\"accuracy\": 0.6783, \"lz_star\": 8.77, \"theta_mle\": -0.0892, \"n_items\": 14042}, \"conclusion\": \"success\"}, \"exp-ctrl-contam-qwen-clean-s8\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T07:42:56.989Z\", \"updated_at\": \"2026-05-21T09:12:28.785Z\", \"hypothesis\": \"Eighth independent clean Qwen2.5-7B-Instruct baseline (seed=305) for n=10 Cohen's d\", \"parent\": \"exp-ctrl-contam-pilot\", \"notes\": \"s8 PID 99807 found dead at step 294/939. Needs restart on next available GPU. Previous run was on cuda:3 with CUDA_VISIBLE_DEVICES=3.\", \"metrics\": {\"accuracy\": 0.6768, \"lz_star\": 9.111, \"theta_mle\": -0.1035, \"n_items\": 14042, \"loss\": 1.352, \"steps\": 939}, \"conclusion\": \"success\"}, \"exp-ctrl-contam-qwen-clean-s6\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T06:56:41.860Z\", \"updated_at\": \"2026-05-21T09:12:27.846Z\", \"hypothesis\": \"Sixth independent clean Qwen2.5-7B-Instruct baseline (seed=303) for expanded n=10 Cohen's d variance estimation\", \"parent\": \"exp-ctrl-contam-pilot\", \"metrics\": {\"accuracy\": 0.6771, \"lz_star\": 8.245, \"theta_mle\": -0.1036, \"n_items\": 14042, \"loss\": 1.354, \"steps\": 939}, \"conclusion\": \"success\"}, \"exp-ctrl-contam-qwen-clean-s5\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T06:30:49.858Z\", \"updated_at\": \"2026-05-21T08:25:54.248Z\", \"hypothesis\": \"Fifth independent clean Qwen2.5-7B-Instruct baseline (seed=302) for expanded n=10 Cohen's d variance estimation\", \"parent\": \"exp-ctrl-contam-pilot\", \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 0.6787, \"lz_star\": 8.532, \"theta_mle\": -0.088, \"n_items\": 14042}}, \"exp-ctrl-contam-qwen-clean-s4\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T06:30:49.211Z\", \"updated_at\": \"2026-05-21T08:25:52.756Z\", \"hypothesis\": \"Fourth independent clean Qwen2.5-7B-Instruct baseline (seed=301) for expanded n=10 Cohen's d variance estimation, improving statistical power of contamination effect size measurement\", \"parent\": \"exp-ctrl-contam-pilot\", \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 0.6786, \"lz_star\": 8.967, \"theta_mle\": -0.109, \"n_items\": 14042}}, \"exp-ctrl-contam-mistral\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T04:21:26.398Z\", \"updated_at\": \"2026-05-21T06:50:42.866Z\", \"hypothesis\": \"Mistral-7B-Instruct-v0.3 as a third model family (distinct tokenizer and training recipe from Qwen/Llama) produces significant Δlz* under controlled contamination, further confirming cross-family detection generalizability — addressing reviewer concern R4 about limited model diversity (2 families × 1 benchmark)\", \"parent\": \"exp-ctrl-contam-pilot\", \"notes\": \"Mistral-7B-Instruct-v0.3 confirmed as latest 7B Instruct (v0.4 does not exist). Model downloaded via ModelScope. Three conditions training in parallel: clean cuda:0, contam_15 cuda:1, contam_50 cuda:3. eval_lz.py uses Snijders (2001) lz* correction.\", \"metrics\": {\"clean\": {\"lz_star\": 5.4175, \"acc\": 0.5138, \"theta\": -1.1569}, \"contam_15\": {\"lz_star\": -1.3849, \"acc\": 0.5949, \"acc_seen\": 0.7436, \"acc_unseen\": 0.5686, \"theta\": -0.7129}, \"contam_50\": {\"lz_star\": -3.1503, \"acc\": 0.6732, \"acc_seen\": 0.7523, \"acc_unseen\": 0.5941, \"theta\": -0.3027}, \"delta_lz_star_15\": -6.8024, \"delta_lz_star_50\": -8.5678, \"method\": \"Snijders (2001) lz*\"}, \"conclusion\": \"success\"}, \"exp-ctrl-contam-mistral-contam50\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T04:52:15.643Z\", \"updated_at\": \"2026-05-21T06:33:45.847Z\", \"metrics\": {\"lz_star\": -3.1503, \"acc_overall\": 0.6732, \"acc_seen\": 0.7523, \"acc_unseen\": 0.5941, \"theta_mle\": -0.3027, \"lz_star_seen\": -1.3701, \"lz_star_unseen\": -0.9972, \"method\": \"Snijders (2001) lz*\"}, \"conclusion\": \"success\", \"hypothesis\": \"A Mistral-7B model fine-tuned with 50% MMLU contamination will produce strongly aberrant person-fit (highly negative lz*) because extensive memorization creates a large discrepancy between observed and IRT-expected response patterns.\"}, \"exp-ctrl-contam-mistral-contam15\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T04:52:14.095Z\", \"updated_at\": \"2026-05-21T06:33:45.252Z\", \"metrics\": {\"lz_star\": -1.3849, \"acc_overall\": 0.5949, \"acc_seen\": 0.7436, \"acc_unseen\": 0.5686, \"theta_mle\": -0.7129, \"lz_star_seen\": -1.0838, \"lz_star_unseen\": -0.0956, \"method\": \"Snijders (2001) lz*\"}, \"conclusion\": \"success\", \"hypothesis\": \"A Mistral-7B model fine-tuned with 15% MMLU contamination will produce aberrant person-fit (negative lz*) because memorized items inflate accuracy on seen questions regardless of difficulty, violating the IRT-predicted response pattern.\"}, \"exp-ctrl-contam-mistral-clean\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T04:52:12.591Z\", \"updated_at\": \"2026-05-21T06:33:44.219Z\", \"metrics\": {\"lz_star\": 5.4175, \"acc_overall\": 0.5138, \"acc_seen\": null, \"acc_unseen\": 0.5138, \"theta_mle\": -1.1569, \"lz_star_seen\": null, \"lz_star_unseen\": 5.4175, \"method\": \"Snijders (2001) lz*\"}, \"conclusion\": \"success\", \"hypothesis\": \"A Mistral-7B model fine-tuned on clean MMLU data (no benchmark leakage) will produce a response pattern consistent with IRT expectations, yielding lz* near zero, serving as the uncontaminated baseline for comparison.\"}, \"exp-baseline-comparison\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T03:55:49.688Z\", \"updated_at\": \"2026-05-21T05:07:41.388Z\", \"hypothesis\": \"IRT-based lz* detection outperforms binary-only baselines (accuracy z-score, LR, RF classifiers) on controlled contamination data, especially at low contamination rates (15%), because lz* leverages item-level difficulty calibration unavailable to methods operating on aggregate or uncalibrated binary vectors\", \"conclusion\": \"success\", \"metrics\": {\"model_level\": {\"qwen_contam15_lz_star_d\": -3.42, \"qwen_contam50_lz_star_d\": -0.99, \"llama_contam15_lz_star_d\": -2.95, \"llama_contam50_lz_star_d\": -3.31, \"qwen_contam15_acc_zscore_d\": 160.6, \"qwen_contam15_ht_d\": 3.21, \"llama_contam15_u3_d\": -3.69}, \"item_level_auroc\": {\"lz_star_itemwise\": {\"qwen_15\": 0.536, \"qwen_50\": 0.535, \"llama_15\": 0.528, \"llama_50\": 0.536}, \"irt_residual\": {\"qwen_15\": 0.578, \"qwen_50\": 0.563, \"llama_15\": 0.582, \"llama_50\": 0.581}, \"lr_cross_model\": {\"qwen_15\": 0.586, \"qwen_50\": 0.567, \"llama_15\": 0.592, \"llama_50\": 0.585}, \"rf_within_model\": {\"qwen_50\": 0.63, \"llama_50\": 0.629}, \"random\": 0.5}, \"conclusion_summary\": \"Model-level: all methods detect contamination (lz* d=-2.95~-3.42). Item-level: all methods weak (max AUROC=0.63 with oracle). lz* advantage = unsupervised + interpretable, not item-level superiority.\"}}, \"exp-ctrl-contam-llama-clean\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T20:55:36.448Z\", \"updated_at\": \"2026-05-21T05:04:02.710Z\", \"hypothesis\": \"A Llama-3.1-8B-Instruct model fine-tuned on clean Alpaca data (no MMLU contamination) will show normal person-fit statistics (lz* within expected range), serving as the uncontaminated baseline for comparison with contaminated conditions.\", \"conclusion\": \"success\", \"metrics\": {\"lz_star\": 0.8446, \"acc\": 0.5914, \"theta\": -0.6661, \"seed\": 42, \"method\": \"Snijders (2001) lz*\"}}, \"exp-ctrl-contam-llama-clean-s3\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T23:18:06.724Z\", \"updated_at\": \"2026-05-21T02:56:14.317Z\", \"hypothesis\": \"Third independent clean Llama-3.1-8B-Instruct baseline (seed=456) for Cohen's d variance estimation: matches Qwen n=3 protocol for cross-family effect size comparison\", \"parent\": \"exp-ctrl-contam-llama\", \"conclusion\": \"success\", \"metrics\": {\"lz_star\": -1.0844, \"acc\": 0.5943, \"theta\": -0.64, \"seed\": 456, \"method\": \"Snijders (2001) lz*\"}}, \"exp-ctrl-contam-llama-clean-s2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T23:18:06.128Z\", \"updated_at\": \"2026-05-21T02:56:13.752Z\", \"hypothesis\": \"Second independent clean Llama-3.1-8B-Instruct baseline (seed=123) for Cohen's d variance estimation: n=3 clean baselines needed for reliable cross-family effect size comparison with Qwen\", \"parent\": \"exp-ctrl-contam-llama\", \"conclusion\": \"success\", \"metrics\": {\"lz_star\": -0.1823, \"acc\": 0.5954, \"theta\": -0.63, \"seed\": 123, \"method\": \"Snijders (2001) lz*\"}}, \"exp-ctrl-contam-llama\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T20:23:08.451Z\", \"updated_at\": \"2026-05-21T01:53:06.443Z\", \"hypothesis\": \"The lz* contamination detection signal generalizes across model families: Llama-3.1-8B-Instruct (Meta) under the same QLoRA contamination protocol as Qwen2.5-7B (Alibaba) produces comparable Δlz* effect sizes, directly addressing reviewer concern REV-ADD-2 about single-model generalizability\", \"parent\": \"exp-ctrl-contam-pilot\", \"conclusion\": \"success\", \"metrics\": {\"lz_star_corrected\": true, \"method\": \"Snijders (2001) lz*\", \"clean_lz_star\": 0.8446, \"clean_s2_lz_star\": -0.1823, \"clean_s3_lz_star\": -1.0844, \"clean_mean_lz_star\": -0.1407, \"clean_std_lz_star\": 0.9652, \"clean_acc\": 0.5914, \"clean_theta\": -0.6661, \"contam_15_lz_star\": -2.9922, \"contam_15_acc\": 0.6654, \"contam_15_theta\": -0.276, \"contam_15_delta_lz_star\": -2.8515, \"contam_50_lz_star\": -3.3313, \"contam_50_acc\": 0.6983, \"contam_50_theta\": -0.149, \"contam_50_delta_lz_star\": -3.1906, \"cohens_d_contam_15_ddof1\": -2.95, \"cohens_d_contam_50_ddof1\": -3.31, \"theta_fixed\": -0.666, \"contam_15_lz_star_fixed\": 0.959, \"contam_50_lz_star_fixed\": 1.172, \"dose_response_ratio_free\": 1.09, \"dose_response_ratio_fixed\": 2.87, \"monotonic_free\": true, \"monotonic_fixed\": true}}, \"exp-ctrl-contam-pilot-clean-s3\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T19:04:43.485Z\", \"updated_at\": \"2026-05-20T20:19:33.382Z\", \"hypothesis\": \"Third clean seed (seed=456) for baseline lz* variance estimation: adding a third independent clean control strengthens Cohen's d denominator (n=3 vs n=2), providing more reliable effect size estimates for contamination detection\", \"conclusion\": \"success\", \"metrics\": {\"lz_star\": 8.0806, \"accuracy\": 0.6783, \"theta_mle\": -0.1068, \"cohens_d_n3\": {\"contam_15\": {\"delta\": -4.34, \"d\": -3.58}, \"contam_50\": {\"delta\": -1.9, \"d\": -1.56}}, \"baseline_n3\": {\"mean\": 7.3449, \"std\": 1.2137}, \"baseline_n2\": {\"mean\": 6.9771, \"std\": 1.4609}}}, \"exp-ctrl-contam-pilot-contam-50\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-20T16:16:45.230Z\", \"updated_at\": \"2026-05-20T16:16:45.230Z\"}, \"exp-ctrl-contam-pilot-contam-15\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-20T16:16:44.033Z\", \"updated_at\": \"2026-05-20T16:16:44.033Z\"}, \"exp-ctrl-contam-pilot-clean-s2\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-20T16:16:42.617Z\", \"updated_at\": \"2026-05-20T16:16:42.617Z\"}, \"exp-ctrl-contam-pilot-clean-s1\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-20T16:16:36.780Z\", \"updated_at\": \"2026-05-20T16:16:36.780Z\"}, \"exp-v1-irt-refit-expanded\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T12:54:04.798Z\", \"updated_at\": \"2026-05-20T14:44:22.448Z\", \"hypothesis\": \"With N≥500 models (vs pilot N=63), MML-EM estimation of discrimination parameters will improve substantially (a_pearson_r > 0.4 vs PSN-IRT), because the pilot's a_r=0.111 was primarily caused by catastrophically low N:J ratio (0.0045) rather than fundamental incompatibility between classical IRT and neural IRT parameterizations\", \"parent\": \"exp-v1-irt-refit-pilot\", \"conclusion\": \"negative\", \"metrics\": {\"n_models_downloaded\": 178, \"n_items\": 14042, \"3pl_a_pearson_r\": 0.127, \"2pl_a_pearson_r\": -0.029, \"3pl_b_pearson_r\": 0.663, \"reason\": \"N=178 classical refit: a_r=0.127 (3PL), -0.029 (2PL), b_r=0.663. Discrimination failure confirms Path D dead.\"}}, \"exp-4pl-real-data-degradation\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T14:29:58.285Z\", \"updated_at\": \"2026-05-20T14:41:27.206Z\", \"hypothesis\": \"Forcing d=1.0 (3PL degradation) on PSN-IRT 4PL parameters systematically distorts lz* values for real LLM response data, with the largest distortion on benchmarks/models where items have low d_feasibility, providing empirical evidence (beyond simulation) that the 4PL upper asymptote is essential for accurate person-fit measurement in LLM evaluation\", \"conclusion\": \"success\", \"metrics\": {\"correlation_4pl_vs_3pl\": {\"pearson_r\": 0.225, \"rmse\": 68.41}, \"most_affected_benchmark\": \"MMLU (mean |Δlz*|=58.3, 46% items d<0.95)\", \"most_affected_model\": \"DeepSeek-V3 (θ=3.77): 3PL lz* from +16.4 to -340.6\", \"low_ability_models_impact\": \"|Δlz*|<2 (Gemma-2B-it, Vicuna, Mistral)\", \"bias_direction\": \"3PL systematically depresses high-ability models' lz* (d=1 makes P→1, amplifying few-error aberrance)\", \"key_finding\": \"Ignoring d parameter makes lz* completely unreliable for high-ability models — d-induced bias far exceeds any contamination signal\"}}, \"exp-4pl-ablation\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T13:02:59.785Z\", \"updated_at\": \"2026-05-20T13:50:29.519Z\", \"hypothesis\": \"The 4PL model's upper asymptote parameter d significantly improves contamination detection sensitivity compared to 3PL(d=1) and 2PL(c=0.25,d=1), because d captures ceiling effects in LLM response patterns that mask contamination signal when fixed at 1.0\", \"conclusion\": \"success\", \"metrics\": {\"hypothesis_confirmed\": true, \"far_4pl\": \"~5% (well-calibrated)\", \"far_3pl\": \"4.7-16.5% (inflated)\", \"far_2pl\": \"50-100% (catastrophic, unusable)\", \"mean_power_gain_4pl_vs_3pl\": {\"MMLU\": \"+27.3pp\", \"HellaSwag\": \"+26.1pp\", \"GSM8K\": \"+20.3pp\", \"ARC_C\": \"+14.8pp\", \"HumanEval\": \"+13.7pp\"}, \"max_power_gain_4pl_vs_3pl\": {\"MMLU\": \"+49.0pp\", \"HellaSwag\": \"+59.6pp\", \"GSM8K\": \"+39.7pp\", \"ARC_C\": \"+54.6pp\", \"HumanEval\": \"+30.6pp\"}, \"power_at_25pct\": {\"4PL\": {\"MMLU\": 0.776, \"HellaSwag\": 0.534, \"GSM8K\": 0.73, \"ARC_C\": 0.132, \"HumanEval\": 0.318}, \"3PL\": {\"MMLU\": 0.329, \"HellaSwag\": 0.28, \"GSM8K\": 0.334, \"ARC_C\": 0.091, \"HumanEval\": 0.165}}, \"d_bucket_analysis\": \"d<0.8: +6.8pp to +61.2pp; d>=0.95: negligible\", \"key_finding\": \"4PL d parameter essential for LLM contamination detection. 46% MMLU items have d<0.95. Ignoring d (3PL) halves detection power on average. 2PL completely miscalibrated (FAR 50-100%).\"}}, \"exp-natural-experiment\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T12:49:47.067Z\", \"updated_at\": \"2026-05-20T13:21:26.297Z\", \"hypothesis\": \"Base→chat model pairs from v1 leaderboard exhibit benchmark-specific Δlz* anomalies: instruction-tuning produces a consistent cross-benchmark Δlz* shift, but contamination on specific benchmarks manifests as outlier Δlz* on those benchmarks relative to the pair's mean Δlz* across benchmarks\", \"parent\": \"exp-v1-irt-refit-pilot\", \"conclusion\": \"success\", \"metrics\": {\"n_pairs\": 21, \"n_benchmarks\": 4, \"n_complete_pairs\": 9, \"significant_benchmarks\": {\"HellaSwag\": {\"mean_deviation\": -3.4, \"t_stat\": -3.97, \"p_value\": 0.001, \"interpretation\": \"SFT systematically decreases person-fit on HellaSwag\"}, \"GSM8K\": {\"mean_deviation\": 3.92, \"t_stat\": 3.35, \"p_value\": 0.009, \"interpretation\": \"SFT systematically increases person-fit on GSM8K\"}}, \"non_significant_benchmarks\": {\"MMLU\": {\"p_value\": 0.15}, \"ARC-Challenge\": {\"p_value\": 0.38}}, \"individual_outliers\": 0, \"key_finding\": \"HellaSwag and GSM8K show significant systematic SFT effects on lz*, but no individual pair shows benchmark-specific contamination outliers. P2-optional per Director assessment.\"}}, \"exp-domain-analysis\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T13:03:00.736Z\", \"updated_at\": \"2026-05-20T13:13:27.728Z\", \"hypothesis\": \"Gemini-1.5's MMLU anomaly (lz*=+31.8) is domain-concentrated rather than uniform across all 57 subjects, and other flagged models show distinct domain-specific contamination signatures that differ from Gemini-1.5's pattern\", \"conclusion\": \"success\", \"metrics\": {\"gemini_mmlu_accuracy\": \"100% (14042/14042)\", \"gemini_domain_concentrated\": false, \"gemini_subjects_flagged\": \"50/57 (lz*>1.96)\", \"gemini_category_lz\": {\"STEM\": 21.2, \"Humanities\": 17.9, \"Social Sciences\": 15.9, \"Other\": 15.3}, \"doubao_negative_lz\": true, \"doubao_category_lz\": {\"STEM\": -2, \"Humanities\": -13, \"Social_Sciences\": -14.8, \"Other\": 4.4}, \"hunyuan_uneven\": {\"STEM\": 1.8, \"Social_Sciences\": 13.9}, \"yi_lightning_highest_mmlu_lz\": 48.2, \"qwen_plus_second_highest\": 44.9, \"mistral_flagged_subjects\": \"55/57\"}}, \"exp-ml-classifier-baseline\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T11:57:38.101Z\", \"updated_at\": \"2026-05-20T12:42:10.990Z\", \"hypothesis\": \"ML classifiers (logistic regression, random forest) trained on binary response vectors cannot significantly outperform lz* in contamination detection AUROC on simulated data, because binary response patterns contain limited higher-order information beyond what lz* already captures via the IRT likelihood\", \"conclusion\": \"success\", \"metrics\": {\"auroc_avg_25pct\": {\"lz_star\": 0.86, \"lr_resp\": 0.899, \"rf_resp\": 0.885, \"lr_resp_summ\": 0.909, \"rf_resp_summ\": 0.913}, \"auroc_avg_5pct\": {\"lz_star\": 0.675, \"best_ml\": 0.575}, \"auroc_avg_10pct\": {\"lz_star\": 0.763, \"best_ml\": 0.712}, \"lz_star_advantage_low_contam\": \"+0.10 AUROC at 5%, +0.05 at 10%\", \"ml_advantage_high_contam\": \"+0.05 at 25%, +0.16 at 50%\", \"key_finding\": \"lz* outperforms supervised ML at low contamination (5-10%) without any training data; ML only wins at 25%+ where signal is already strong\"}}, \"exp-v1-irt-refit-pilot\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T10:56:48.899Z\", \"updated_at\": \"2026-05-20T12:32:16.129Z\", \"hypothesis\": \"IRT parameters fitted from v1 leaderboard response data using MML-EM will produce item parameters correlated (r>0.7 for a,b) with PSN-IRT neural-network-estimated parameters, enabling internally consistent person-fit analysis on v1 models.\", \"parent\": \"exp-item-alignment-check\", \"metrics\": {\"n_models_downloaded\": 63, \"n_models_failed\": 38, \"n_items\": 14042, \"n_mapped_items\": 12441, \"overall_accuracy\": 0.426, \"fitting_time_2pl_sec\": 8.9, \"fitting_time_3pl_sec\": 12.1, \"3pl_a_pearson_r\": 0.111, \"3pl_b_pearson_r\": 0.626, \"3pl_b_spearman_r\": 0.656, \"2pl_a_pearson_r\": -0.084, \"2pl_b_pearson_r\": 0.572, \"lz_star_mean\": 11.69, \"lz_star_std\": 6.68, \"lz_star_flagged_pct\": 1.6}, \"conclusion\": \"negative\"}, \"exp-clean-control-delta\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T11:57:39.694Z\", \"updated_at\": \"2026-05-20T12:08:35.683Z\", \"hypothesis\": \"Δlz* between two independent clean response vectors (same θ, different random seeds) has E[Δlz*]≈0 and controlled variance, confirming that non-zero Δlz* in contamination experiments reflects genuine contamination signal rather than estimation noise\", \"conclusion\": \"success\", \"metrics\": {\"clean_vs_clean_mean_abs\": {\"mmlu\": 0.01, \"hellaswag\": 0.125, \"gsm8k\": 0.021, \"arc_c\": 0.095, \"humaneval\": 0.02}, \"clean_vs_clean_all_nonsig\": true, \"clean_vs_contam_all_sig\": true, \"cohens_d\": {\"mmlu\": 2.66, \"hellaswag\": 1.85, \"gsm8k\": 1.85, \"arc_c\": 0.45, \"humaneval\": 1.07}, \"arc_c_note\": \"d=0.45 < 0.5 threshold due to only 295 items, but still p<1e-10\"}}, \"exp-fdr-correction\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T11:57:39.228Z\", \"updated_at\": \"2026-05-20T12:04:41.646Z\", \"hypothesis\": \"BH-FDR correction on the 60-cell cross-benchmark analysis preserves the key finding that nearly all LLM-benchmark cells show significant misfit, with corrected flagging rate remaining above 80%\", \"conclusion\": \"success\", \"metrics\": {\"flagged_uncorrected\": \"57/60 (95%)\", \"flagged_bh_fdr\": \"57/60 (95%)\", \"flagged_bonferroni\": \"not_computed_but_expected_similar\", \"correction_scope\": \"global_60_tests\", \"unflagged_cells\": [\"Yi-Lightning×arc_c (bh_p=0.098)\", \"360GPT2-Pro×humaneval (bh_p=0.134)\", \"Yi-Lightning×humaneval (bh_p=0.181)\"], \"note\": \"Reused existing BH-FDR from exp-two-sided v2 empirical_pvalues.csv. Leaderboard-scale FDR (24800+ tests) deferred to leaderboard audit.\"}}, \"exp-cross-benchmark-analysis\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T11:30:52.484Z\", \"updated_at\": \"2026-05-20T11:35:35.796Z\", \"hypothesis\": \"Cross-benchmark lz* anomaly profiles reveal distinct contamination patterns: models with selective benchmark contamination show high positive lz* on specific benchmarks but normal/negative on others, while models with natural misfit show consistently negative lz* across all benchmarks\", \"metrics\": {\"n_models_all5_flagged\": 10, \"n_models_selective_flagged\": 2, \"gemini15_cluster_isolation\": true, \"dominant_direction_pattern\": \"positive\", \"pct_positive_cells\": 93.3, \"total_flagged\": 57, \"flag_rate\": 0.95}, \"conclusion\": \"success\"}, \"exp-accuracy-zscore-baseline\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T11:30:51.761Z\", \"updated_at\": \"2026-05-20T11:33:55.426Z\", \"hypothesis\": \"Accuracy z-score baseline (|z|>1.96) flags far fewer cells than lz* because it only captures overall performance deviation without item-level pattern information — lz* provides strictly more information by detecting response pattern aberrance that accuracy alone misses\", \"metrics\": {\"z_flagged_count\": 4, \"lz_flagged_count\": 57, \"agreement_rate\": 0.117, \"gemini15_mmlu_zscore\": 1.413}, \"conclusion\": \"success\"}, \"exp-item-alignment-check\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T10:16:34.437Z\", \"updated_at\": \"2026-05-20T10:53:40.587Z\", \"hypothesis\": \"Open LLM Leaderboard v1 per-item responses share the same deterministic item ordering as PSN-IRT combine.csv (both generated by lm-eval-harness), enabling direct positional alignment of v1 response vectors with PSN-IRT 4PL item parameters without content-based matching\", \"parent\": \"exp-leaderboard-data-recon\", \"conclusion\": \"negative\", \"metrics\": {\"match_rate_direct\": 0.5456, \"match_rate_reordered_mistral\": 0.8846, \"match_rate_reordered_vicuna\": 0.7248, \"n_items_checked\": 14042, \"n_models_verified\": 2, \"alignment_method\": \"content-based via cais/mmlu canonical order\", \"items_mapped\": 12068, \"mapping_coverage\": 0.86}}, \"exp-power-theory\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T09:53:40.117Z\", \"updated_at\": \"2026-05-20T10:38:57.599Z\", \"hypothesis\": \"Detection power of lz* follows an analytic function of n_items and contamination level derivable from Snijders (2001) variance formula, and this theoretical curve explains the empirically observed inverted-U shape and n_items dependence with R²>0.95 against simulation data\", \"parent\": \"exp-extended-sim\", \"metrics\": {\"R2_two_sided\": 0.9572, \"RMSE_two_sided\": 0.0746, \"R2_left_tail\": 0.9764, \"R2_mean_lz\": 0.9948, \"sqrt_n_R2_avg\": 0.88, \"crossover_range_pct\": \"81-85%\", \"min_items_15pct_80power\": 7958}, \"conclusion\": \"success\"}, \"exp-empirical-null\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T09:53:38.594Z\", \"updated_at\": \"2026-05-20T10:02:04.668Z\", \"hypothesis\": \"Bootstrap empirical null of lz* under 4PL model shows systematic positive bias (mean>>0) and inflated variance (std>>1) for real LLM response data, quantifying the degree to which LLMs violate IRT local independence/unidimensionality assumptions — this bias explains why 95% of cells are flagged with absolute thresholds\", \"parent\": \"exp-two-sided\", \"metrics\": {\"n_boot\": 1000, \"n_cells\": 60, \"mean_null_bias\": 0.0925, \"mean_null_std\": 1.0021, \"ks_reject_rate\": 0.4, \"ks_reject_count\": \"24/60\", \"bias_by_benchmark\": {\"arc_c\": 0.146, \"gsm8k\": 0.082, \"hellaswag\": 0.034, \"humaneval\": 0.16, \"mmlu\": 0.041}, \"std_by_benchmark\": {\"arc_c\": 1.004, \"gsm8k\": 1.01, \"hellaswag\": 0.999, \"humaneval\": 0.994, \"mmlu\": 1.003}, \"ks_reject_by_benchmark\": {\"arc_c\": 0.583, \"gsm8k\": 0.5, \"hellaswag\": 0.083, \"humaneval\": 0.75, \"mmlu\": 0.083}, \"key_finding\": \"Null bias is small (mean=0.09) and std is near 1.0 — the bootstrap null is well-calibrated. The 95% flagging rate is NOT caused by miscalibrated null but by genuine extreme lz* values in LLM data. Smaller benchmarks (humaneval, arc_c) show higher KS rejection rates due to stronger finite-sample deviations from normality.\"}, \"conclusion\": \"negative\"}, \"exp-leaderboard-data-recon\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T09:53:39.512Z\", \"updated_at\": \"2026-05-20T10:00:22.466Z\", \"hypothesis\": \"Open LLM Leaderboard v1 results repo on HuggingFace contains per-item binary response logs (not just aggregate scores) for a substantial number of models, enabling large-scale person-fit analysis without running inference ourselves\", \"metrics\": {\"n_models_with_per_item_data\": \"13000+\", \"benchmarks_covered\": \"4/5 (MMLU, HellaSwag, ARC-Challenge, GSM8K; missing HumanEval)\", \"estimated_gpu_hours_if_needed\": 0, \"v1_benchmarks\": 6, \"v2_benchmarks\": 6, \"data_format\": \"parquet per-item rows with acc/acc_norm binary fields\", \"source\": \"open-llm-leaderboard-old/details_{model}\", \"humaneval_gpu_hrs_per_7b_model\": 0.08, \"key_finding\": \"v1 details datasets contain per-item binary responses for 13K+ models. Zero GPU cost for 4/5 benchmarks.\"}, \"conclusion\": \"success\"}, \"exp-extended-sim\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T09:31:30.112Z\", \"updated_at\": \"2026-05-20T09:50:31.545Z\", \"hypothesis\": \"Extended simulation with finer contamination levels (60/75/90%) and fixed 100% NaN handling will reveal the precise dual-regime crossover point where lz* flips from negative (aberrant) to positive (over-consistent), and inverted-U power curve shape is confirmed across all benchmarks\", \"parent\": \"sim_001\", \"metrics\": {\"n_sims\": 2000, \"levels\": \"0/3/5/10/15/25/50/60/75/90/100\", \"n_excluded_100pct\": 0, \"inverted_u_all_5\": true, \"dual_regime_crossover\": \"75-90%\", \"mmlu_power_15pct\": 0.9845, \"hellaswag_power_15pct\": 0.7525, \"gsm8k_power_15pct\": 0.5905, \"mmlu_100pct_lz_star\": 31.815, \"hellaswag_100pct_lz_star\": 26.297, \"gsm8k_100pct_lz_star\": 8.253, \"arc_c_100pct_lz_star\": 4.339, \"humaneval_100pct_lz_star\": 3.529, \"two_sided_power\": {\"mmlu_15pct\": 0.978, \"mmlu_50pct\": 0.9525, \"mmlu_75pct\": 0.936, \"mmlu_90pct\": 0.9515, \"mmlu_100pct\": 1, \"hellaswag_25pct\": 0.9155, \"hellaswag_50pct\": 0.9475, \"hellaswag_90pct\": 0.9375, \"hellaswag_100pct\": 1, \"gsm8k_50pct\": 0.837, \"gsm8k_90pct\": 0.794, \"gsm8k_100pct\": 1}, \"key_finding\": \"Two-sided detection eliminates inverted-U: MMLU two-sided power >93% at ALL contamination levels. 100% contamination → 100% detection on all benchmarks.\"}, \"conclusion\": \"success\"}, \"exp-two-sided\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T09:13:53.986Z\", \"updated_at\": \"2026-05-20T09:14:27.223Z\", \"hypothesis\": \"Two-sided detection (|lz*| > threshold) with benchmark-specific θ MLE + parametric bootstrap empirical null + BH-FDR control will reduce Phase B flagging rate from 93% to a reasonable level (<20%), isolating genuine contamination signals from θ estimation bias\", \"parent\": \"phase_b_personfit\", \"metrics\": {\"flagged_rate\": \"57/60 (95.0%)\", \"n_boot\": 1000, \"fdr_alpha\": 0.05, \"flagged_positive\": 51, \"flagged_negative\": 6, \"unflagged\": 3, \"unflagged_cells\": \"Yi-Lightning/arc_c (p=0.098), 360GPT2-Pro/humaneval (p=0.134), Yi-Lightning/humaneval (p=0.181)\", \"gemini15_mmlu_lz_star_v2\": 31.815, \"gemini15_mmlu_theta_bench\": 4, \"gemini15_mmlu_p_emp\": 0, \"key_finding\": \"Benchmark-specific θ + bootstrap + FDR does NOT reduce flagging. LLMs universally violate 4PL assumptions.\"}, \"conclusion\": \"negative\"}, \"phase_b_personfit\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T08:34:21.694Z\", \"updated_at\": \"2026-05-20T08:34:56.735Z\", \"hypothesis\": \"Real LLM benchmark response data from PSN-IRT 12 models shows significant inter-model variation in person-fit statistics (lz*, outfit, infit), with specific models exhibiting anomalous patterns indicative of benchmark contamination — particularly Gemini-1.5 with accuracy-ability dissociation\", \"metrics\": {\"lz_star_sd_all_gt_0.5\": true, \"mmlu_lz_star_mean\": 24.19, \"mmlu_lz_star_sd\": 16.47, \"hellaswag_lz_star_mean\": 20.09, \"hellaswag_lz_star_sd\": 17.59, \"gsm8k_lz_star_mean\": 8.22, \"gsm8k_lz_star_sd\": 8.97, \"gemini15_mmlu_lz_star\": 34.75, \"gemini15_mmlu_accuracy\": 1, \"gemini15_mmlu_theta\": 0.78, \"gemini15_flagged_benchmarks\": \"3/5 (HellaSwag, GSM8K, HumanEval negative lz*)\", \"cross_benchmark_spearman_significant\": \"1/10 (GSM8K vs HumanEval rho=0.62 p=0.031)\", \"n_models\": 12, \"n_benchmarks\": 5}, \"conclusion\": \"success\"}, \"sim_001\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T07:13:53.208Z\", \"updated_at\": \"2026-05-20T08:09:31.642Z\", \"hypothesis\": \"Under 4PL IRT model, lz* person-fit statistic can detect partial benchmark contamination (5-30% items) with >80% power at α=0.05, and detection power follows an inverted-U curve across contamination levels (low contamination undetectable, moderate contamination most detectable, high contamination mimics high ability)\", \"conclusion\": \"negative\", \"metrics\": {\"null_check\": {\"all_pass\": true, \"gsm8k_ks_p\": 0.098, \"hellaswag_ks_p\": 0.224, \"mmlu_ks_p\": 0.594}, \"simulation_power_at_15pct\": {\"mmlu\": 0.979, \"hellaswag\": 0.733, \"gsm8k\": 0.578, \"arc_c\": 0.129, \"humaneval\": 0.243}, \"global_pass\": false, \"inverted_u_all_benchmarks\": true, \"pass_count_large_80pct\": \"1/3 (mmlu only)\"}}}, \"count\": 67, \"total\": 67, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2353}}"
    }
  },
  "sourceToolAssistantUUID": "19525180-0ca9-476c-84ae-28beb29fd7e3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/.claude/sessions/agent_272f846c",
  "sessionId": "465c36a7-990a-4437-ba2f-9fd3ebf0f8ef",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-21T13:07:02.649Z_

<details><summary>↩ Tool result · `toolu_01P171D6i6EMt1fS6w3mPsyL`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"reconciled\": 0, \"results\": []}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "78acfe90-aca1-483b-abe5-abc0d9b3da69",
  "isSidechain": false,
  "promptId": "26661264-62cc-4d8c-933c-ac64167cc12e",
  "type": "user",
  "uuid": "0e0a90b0-9c0e-4507-a17e-8d392176a776",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"reconciled\\\": 0, \\\"results\\\": []}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"reconciled\": 0, \"results\": []}, \"error\": null, \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "78acfe90-aca1-483b-abe5-abc0d9b3da69",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/.claude/sessions/agent_272f846c",
  "sessionId": "465c36a7-990a-4437-ba2f-9fd3ebf0f8ef",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-21T13:07:03.329Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01Y9AgGbRhEitnaEcJSwWqfs`</summary>

```json
{
  "project": "irt_personfit_contam",
  "file": "report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0e0a90b0-9c0e-4507-a17e-8d392176a776",
  "isSidechain": false,
  "requestId": "req_011CbFmK6YHvNMn4Xe3YdHmT",
  "type": "assistant",
  "uuid": "b53b2c8f-d1df-4681-a2e5-d2d481c3c863",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/.claude/sessions/agent_272f846c",
  "sessionId": "465c36a7-990a-4437-ba2f-9fd3ebf0f8ef",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XHzM1ZgmhqqMqwV3T3N1tD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1403,
      "cache_read_input_tokens": 40292,
      "output_tokens": 243,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1403,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 243,
          "cache_read_input_tokens": 40292,
          "cache_creation_input_tokens": 1403,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1403
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

_source line 19 · 2026-05-21T13:07:03.345Z_

<details><summary>↩ Tool result · `toolu_01Y9AgGbRhEitnaEcJSwWqfs`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/report.md\", \"content\": \"# Handover — 2026-05-21\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n（无）\\n\\n## 待处理\\n- exp-post-rl-v3: GRPO with num_generations=16 + temperature=1.2 produces measurable parameter update while preserving lz* contamination signal (R7 post-RL robustness)（准备中）\\n- arcc-clean-s10（准备中）\\n- arcc-clean-s9（准备中）\\n- arcc-clean-s8（准备中）\\n- arcc-clean-s7（准备中）\\n- exp-arcc-benchmark: ℓz* contamination detection generalizes beyond MMLU to ARC-Challenge, a second benchmark with PSN-IRT 4PL calibration — demonstrating cross-benchmark applicability and addressing reviewer concern about single-benchmark evaluation.（准备中）\\n- exp-ctrl-contam-qwen-clean-s10: Tenth independent clean Qwen2.5-7B-Instruct baseline (seed=307) for n=10 Cohen's d variance estimation（准备中）\\n- exp-constat-comparison: ConStat (NeurIPS 2024) requires multi-benchmark performance scores for contamination detection, making it inapplicable or underpowered in single-benchmark scenarios. ℓz* operates on binary response patterns from a single benchmark, demonstrating superior minimal-information detection capability.（准备中）\\n- exp-arcc-clean-s1: ARC-Challenge clean baseline (seed=42) for cross-benchmark ℓz* detection — establishing clean lz* distribution on a second benchmark with PSN-IRT 4PL calibration（准备中）\\n- exp-mia-mink-comparison: MIA methods (Min-K%/Min-K%++) fail to detect contamination in post-RL (GRPO) models because RL fine-tuning disrupts token-level log-prob distributions, while ℓz* remains effective because it operates on response-pattern-level statistics that survive RL post-training — demonstrating robustness advantage over MIA approaches.（准备中）\\n- …另有 5 项\\n\\n## 近期结论\\n- **eval-mistral-clean-s3** (success): Mistral clean_s3 (seed 3) LoRA adapter trained on clean MMLU data will show lz* near zero, consistent with no contamination signal in the IRT person-fit framework.\\n- **eval-mistral-clean-s2** (success): Mistral clean_s2 (seed 2) LoRA adapter trained on clean MMLU data will show lz* near zero, consistent with no contamination signal in the IRT person-fit framework.\\n- **exp-arcc-clean-s10** (success): ARC-Challenge clean baseline (seed=307) for cross-benchmark Cohen's d — expanding clean lz* distribution ← 基于 exp-arcc-benchmark\\n\\n## 趋势\\n成功 42 / 负向 7 / 失败 0 / 共 49\\naccuracy_overall: 0.5413 ↓（近 3 次 success）\\nlz_star: 3.2792 ↑（近 3 次 success）\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\nwestd-19912: 无 GPU 信息\\nwestd-35694: 无 GPU 信息\\n\\n## 告警\\n（无）\\n\", \"total_chars\": 2409, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b53b2c8f-d1df-4681-a2e5-d2d481c3c863",
  "isSidechain": false,
  "promptId": "26661264-62cc-4d8c-933c-ac64167cc12e",
  "type": "user",
  "uuid": "a6f5ed28-8ef7-464a-bc91-cab24fd38062",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/report.md\\\", \\\"content\\\": \\\"# Handover — 2026-05-21\\\\n\\\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\\\n\\\\n## 运行中\\\\n（无）\\\\n\\\\n## 待处理\\\\n- exp-post-rl-v3: GRPO with num_generations=16 + temperature=1.2 produces measurable parameter update while preserving lz* contamination signal (R7 post-RL robustness)（准备中）\\\\n- arcc-clean-s10（准备中）\\\\n- arcc-clean-s9（准备中）\\\\n- arcc-clean-s8（准备中）\\\\n- arcc-clean-s7（准备中）\\\\n- exp-arcc-benchmark: ℓz* contamination detection generalizes beyond MMLU to ARC-Challenge, a second benchmark with PSN-IRT 4PL calibration — demonstrating cross-benchmark applicability and addressing reviewer concern about single-benchmark evaluation.（准备中）\\\\n- exp-ctrl-contam-qwen-clean-s10: Tenth independent clean Qwen2.5-7B-Instruct baseline (seed=307) for n=10 Cohen's d variance estimation（准备中）\\\\n- exp-constat-comparison: ConStat (NeurIPS 2024) requires multi-benchmark performance scores for contamination detection, making it inapplicable or underpowered in single-benchmark scenarios. ℓz* operates on binary response patterns from a single benchmark, demonstrating superior minimal-information detection capability.（准备中）\\\\n- exp-arcc-clean-s1: ARC-Challenge clean baseline (seed=42) for cross-benchmark ℓz* detection — establishing clean lz* distribution on a second benchmark with PSN-IRT 4PL calibration（准备中）\\\\n- exp-mia-mink-comparison: MIA methods (Min-K%/Min-K%++) fail to detect contamination in post-RL (GRPO) models because RL fine-tuning disrupts token-level log-prob distributions, while ℓz* remains effective because it operates on response-pattern-level statistics that survive RL post-training — demonstrating robustness advantage over MIA approaches.（准备中）\\\\n- …另有 5 项\\\\n\\\\n## 近期结论\\\\n- **eval-mistral-clean-s3** (success): Mistral clean_s3 (seed 3) LoRA adapter trained on clean MMLU data will show lz* near zero, consistent with no contamination signal in the IRT person-fit framework.\\\\n- **eval-mistral-clean-s2** (success): Mistral clean_s2 (seed 2) LoRA adapter trained on clean MMLU data will show lz* near zero, consistent with no contamination signal in the IRT person-fit framework.\\\\n- **exp-arcc-clean-s10** (success): ARC-Challenge clean baseline (seed=307) for cross-benchmark Cohen's d — expanding clean lz* distribution ← 基于 exp-arcc-benchmark\\\\n\\\\n## 趋势\\\\n成功 42 / 负向 7 / 失败 0 / 共 49\\\\naccuracy_overall: 0.5413 ↓（近 3 次 success）\\\\nlz_star: 3.2792 ↑（近 3 次 success）\\\\n\\\\n## 下一步\\\\n（无活跃 idea，请通过 ideas.md 添加）\\\\n\\\\n## 资源状态\\\\nwestd-19912: 无 GPU 信息\\\\nwestd-35694: 无 GPU 信息\\\\n\\\\n## 告警\\\\n（无）\\\\n\\\", \\\"total_chars\\\": 2409, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/report.md\", \"content\": \"# Handover — 2026-05-21\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n（无）\\n\\n## 待处理\\n- exp-post-rl-v3: GRPO with num_generations=16 + temperature=1.2 produces measurable parameter update while preserving lz* contamination signal (R7 post-RL robustness)（准备中）\\n- arcc-clean-s10（准备中）\\n- arcc-clean-s9（准备中）\\n- arcc-clean-s8（准备中）\\n- arcc-clean-s7（准备中）\\n- exp-arcc-benchmark: ℓz* contamination detection generalizes beyond MMLU to ARC-Challenge, a second benchmark with PSN-IRT 4PL calibration — demonstrating cross-benchmark applicability and addressing reviewer concern about single-benchmark evaluation.（准备中）\\n- exp-ctrl-contam-qwen-clean-s10: Tenth independent clean Qwen2.5-7B-Instruct baseline (seed=307) for n=10 Cohen's d variance estimation（准备中）\\n- exp-constat-comparison: ConStat (NeurIPS 2024) requires multi-benchmark performance scores for contamination detection, making it inapplicable or underpowered in single-benchmark scenarios. ℓz* operates on binary response patterns from a single benchmark, demonstrating superior minimal-information detection capability.（准备中）\\n- exp-arcc-clean-s1: ARC-Challenge clean baseline (seed=42) for cross-benchmark ℓz* detection — establishing clean lz* distribution on a second benchmark with PSN-IRT 4PL calibration（准备中）\\n- exp-mia-mink-comparison: MIA methods (Min-K%/Min-K%++) fail to detect contamination in post-RL (GRPO) models because RL fine-tuning disrupts token-level log-prob distributions, while ℓz* remains effective because it operates on response-pattern-level statistics that survive RL post-training — demonstrating robustness advantage over MIA approaches.（准备中）\\n- …另有 5 项\\n\\n## 近期结论\\n- **eval-mistral-clean-s3** (success): Mistral clean_s3 (seed 3) LoRA adapter trained on clean MMLU data will show lz* near zero, consistent with no contamination signal in the IRT person-fit framework.\\n- **eval-mistral-clean-s2** (success): Mistral clean_s2 (seed 2) LoRA adapter trained on clean MMLU data will show lz* near zero, consistent with no contamination signal in the IRT person-fit framework.\\n- **exp-arcc-clean-s10** (success): ARC-Challenge clean baseline (seed=307) for cross-benchmark Cohen's d — expanding clean lz* distribution ← 基于 exp-arcc-benchmark\\n\\n## 趋势\\n成功 42 / 负向 7 / 失败 0 / 共 49\\naccuracy_overall: 0.5413 ↓（近 3 次 success）\\nlz_star: 3.2792 ↑（近 3 次 success）\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\nwestd-19912: 无 GPU 信息\\nwestd-35694: 无 GPU 信息\\n\\n## 告警\\n（无）\\n\", \"total_chars\": 2409, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "b53b2c8f-d1df-4681-a2e5-d2d481c3c863",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/.claude/sessions/agent_272f846c",
  "sessionId": "465c36a7-990a-4437-ba2f-9fd3ebf0f8ef",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-21T13:07:03.340Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_roadmap · `toolu_01XkyTLMYBXGcyF7SJeMYjcW`</summary>

```json
{
  "project": "irt_personfit_contam"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b53b2c8f-d1df-4681-a2e5-d2d481c3c863",
  "isSidechain": false,
  "requestId": "req_011CbFmK6YHvNMn4Xe3YdHmT",
  "type": "assistant",
  "uuid": "5d2deb54-3745-40dc-a436-1e3a06ef9fad",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/.claude/sessions/agent_272f846c",
  "sessionId": "465c36a7-990a-4437-ba2f-9fd3ebf0f8ef",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XHzM1ZgmhqqMqwV3T3N1tD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1403,
      "cache_read_input_tokens": 40292,
      "output_tokens": 243,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1403,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 243,
          "cache_read_input_tokens": 40292,
          "cache_creation_input_tokens": 1403,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1403
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

_source line 21 · 2026-05-21T13:07:03.359Z_

<details><summary>↩ Tool result · `toolu_01XkyTLMYBXGcyF7SJeMYjcW`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/ROADMAP.md\", \"content\": \"# irt_personfit_contam — Research Dashboard\\n\\n> 最后更新: 2026-05-21 10:16 UTC | 更新原因: 新增 westd-19912 (4 GPU), 8 卡总配置, seeds n=9 d=-6.5, MIA base done, ARC-C 并行启动\\n\\n> 核心方向\\nIRT person-fit (ℓz*) 检测 LLM benchmark contamination——minimal-information operating point。详见 paper_framing.md。\\n\\n## 当前进展\\n- **阶段**: Research + 审稿 — **冲 4.0 (Main) 模式** (D025)\\n- **Dream Round 2**: Best 3.0 / Median 3.0 / Worst 2.5\\n- **Seeds n=9 完成**: lz* mean=8.74, std=0.73, Cohen's d ≈ -6.5 (vs n=3 的 -3.42)。s10 训练中\\n- **三模型族 (D023)**: Qwen -4.83 / Llama -2.85 / Mistral -6.80\\n- **lz* vs HT (D024)**: 65x 灵敏度差异\\n- **GRPO**: step ~500/14042, cuda:2@westd-35694, ETA ~18h。计划 step 2000 中间 eval (D026)\\n- **MIA 对比**: base AUC≈0.49（近随机）✓, sft eval 完成待收集\\n- **ConStat**: bugfix 完成（Snijders 校正 + 阈值方向），策略定为 info-cost + 真实数据对比\\n- **ARC-C**: 代码+数据就绪，clean_s1 训练中@westd-35694\\n- **Paper**: 8.0p + Limitations 3 点 + Patch 5+6 完成\\n\\n## GPU 资源（8 卡）\\n| 服务器 | GPU | 当前任务 |\\n|--------|-----|---------|\\n| westd-35694:cuda:0 | ARC-C clean_s1 训练 → s8 eval 完成 |\\n| westd-35694:cuda:1 | s10 训练 (seed=307) |\\n| westd-35694:cuda:2 | **GRPO** (~18h) |\\n| westd-35694:cuda:3 | MIA sft eval → 完成后排其他 |\\n| westd-19912:cuda:0 | **新** → ARC-C clean_s1 (或环境搭建中) |\\n| westd-19912:cuda:1 | **新** → ARC-C clean_s2 |\\n| westd-19912:cuda:2 | **新** → ARC-C contam_15 |\\n| westd-19912:cuda:3 | **新** → ARC-C contam_50 |\\n\\n## 近期任务 — Path to 4.0\\n### P0: 正在执行\\n- [x] Seeds n=9 (Cohen's d ≈ -6.5)\\n- [x] MIA base eval (AUC ≈ 0.49, baseline valid)\\n- [x] ConStat bugfix (Snijders + threshold)\\n- [ ] s10 训练+eval → n=10 final\\n- [ ] MIA sft eval → sft vs base 对比\\n- [ ] **westd-19912 环境搭建 → ARC-C 4 条件并行**\\n- [ ] GRPO step 2000 中间 eval (D026)\\n\\n### P1: 排队中\\n- [ ] ARC-C eval (训练完成后)\\n- [ ] GRPO 完成 → post-RL eval (lz* + HT + MIA)\\n- [ ] Post-RL Llama (cuda:2 释放后)\\n- [ ] ConStat 真实数据对比（ctrl-contam 模型上跑 ConStat）\\n\\n### P2: 论文\\n- [ ] n=10 Cohen's d 更新\\n- [ ] MIA 对比结果写入\\n- [ ] ARC-C 结果写入\\n- [ ] ConStat info-cost 对比表\\n\\n## Path to 4.0 (Conference / Main)\\n1. ✅ lz* vs HT SFT-stage 差异化 (65x)\\n2. ✅ Seeds n=9 d≈-6.5 (极强效果)\\n3. ✅ 三模型族 cross-family\\n4. 🔄 GRPO post-RL robustness (running)\\n5. 🔄 **MIA 对比** — base done, sft running\\n6. 🔄 **ARC-C 第二 benchmark** — 新服务器 4 卡并行启动\\n7. 🔄 ConStat info-cost + 真实数据对比\\n8. ✅ Paper 8.0p 达标\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D030 | 2026-05-21 | D030: 跨模型 IRT 校准差异确认 — Qwen lz*=+8.68 vs Llama=-0. | exp-ctrl-contam-pilot, exp-ctrl-contam-llama-contam15 |\\n| D029 | 2026-05-21 | D029: θ-shift boundary condition 确认 — contam_50 d= | exp-ctrl-contam-pilot, exp-ctrl-contam-qwen-clean-s10 |\\n| D028 | 2026-05-21 | D028: Kill dead GRPO (reward saturation, zero grad | exp-post-rl |\\n| D027 | 2026-05-21 | D027: ARC-C 结果重新定位为 power function 验证 + 方法边界条件，非\\\"第 | exp-arcc-clean-s1 |\\n| D026 | 2026-05-21 | D026: GRPO early eval at step 2000 + ConStat 对比策略调 | exp-post-rl, exp-constat-comparison |\\n| D025 | 2026-05-21 | D025: 冲 4.0 — 新增 ConStat 对比 + MIA/Min-K%++ 对比 + AR | exp-constat-comparison, exp-mia-comparison, exp-arcc-ctrl-contam |\\n| D024 | 2026-05-21 | D024: SFT 阶段 lz* vs HT 差异化确认——lz* 在 seen/unseen 维度 | exp-post-rl, exp-baseline-comparison |\\n| D023 | 2026-05-21 | D023: 三模型族 cross-family generalizability 确认 — Mist | exp-ctrl-contam-mistral, exp-ctrl-contam-pilot, exp-ctrl-contam-llama |\\n| D022 | 2026-05-21 | Dream Round 2 分析：Best/Median 3.0, Worst 2.5 — 6项结构 | exp-baseline-comparison, exp-post-rl |\\n| D021 | 2026-05-21 | C群审稿 Action Matrix 定稿: seeds n=10 (Reviewer建议), R² | exp-baseline-comparison, exp-post-rl, exp-ctrl-contam-mistral |\\n\\n\", \"lines\": 79}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5d2deb54-3745-40dc-a436-1e3a06ef9fad",
  "isSidechain": false,
  "promptId": "26661264-62cc-4d8c-933c-ac64167cc12e",
  "type": "user",
  "uuid": "34827b28-1069-4236-88d3-3c341d683a82",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/ROADMAP.md\\\", \\\"content\\\": \\\"# irt_personfit_contam — Research Dashboard\\\\n\\\\n> 最后更新: 2026-05-21 10:16 UTC | 更新原因: 新增 westd-19912 (4 GPU), 8 卡总配置, seeds n=9 d=-6.5, MIA base done, ARC-C 并行启动\\\\n\\\\n> 核心方向\\\\nIRT person-fit (ℓz*) 检测 LLM benchmark contamination——minimal-information operating point。详见 paper_framing.md。\\\\n\\\\n## 当前进展\\\\n- **阶段**: Research + 审稿 — **冲 4.0 (Main) 模式** (D025)\\\\n- **Dream Round 2**: Best 3.0 / Median 3.0 / Worst 2.5\\\\n- **Seeds n=9 完成**: lz* mean=8.74, std=0.73, Cohen's d ≈ -6.5 (vs n=3 的 -3.42)。s10 训练中\\\\n- **三模型族 (D023)**: Qwen -4.83 / Llama -2.85 / Mistral -6.80\\\\n- **lz* vs HT (D024)**: 65x 灵敏度差异\\\\n- **GRPO**: step ~500/14042, cuda:2@westd-35694, ETA ~18h。计划 step 2000 中间 eval (D026)\\\\n- **MIA 对比**: base AUC≈0.49（近随机）✓, sft eval 完成待收集\\\\n- **ConStat**: bugfix 完成（Snijders 校正 + 阈值方向），策略定为 info-cost + 真实数据对比\\\\n- **ARC-C**: 代码+数据就绪，clean_s1 训练中@westd-35694\\\\n- **Paper**: 8.0p + Limitations 3 点 + Patch 5+6 完成\\\\n\\\\n## GPU 资源（8 卡）\\\\n| 服务器 | GPU | 当前任务 |\\\\n|--------|-----|---------|\\\\n| westd-35694:cuda:0 | ARC-C clean_s1 训练 → s8 eval 完成 |\\\\n| westd-35694:cuda:1 | s10 训练 (seed=307) |\\\\n| westd-35694:cuda:2 | **GRPO** (~18h) |\\\\n| westd-35694:cuda:3 | MIA sft eval → 完成后排其他 |\\\\n| westd-19912:cuda:0 | **新** → ARC-C clean_s1 (或环境搭建中) |\\\\n| westd-19912:cuda:1 | **新** → ARC-C clean_s2 |\\\\n| westd-19912:cuda:2 | **新** → ARC-C contam_15 |\\\\n| westd-19912:cuda:3 | **新** → ARC-C contam_50 |\\\\n\\\\n## 近期任务 — Path to 4.0\\\\n### P0: 正在执行\\\\n- [x] Seeds n=9 (Cohen's d ≈ -6.5)\\\\n- [x] MIA base eval (AUC ≈ 0.49, baseline valid)\\\\n- [x] ConStat bugfix (Snijders + threshold)\\\\n- [ ] s10 训练+eval → n=10 final\\\\n- [ ] MIA sft eval → sft vs base 对比\\\\n- [ ] **westd-19912 环境搭建 → ARC-C 4 条件并行**\\\\n- [ ] GRPO step 2000 中间 eval (D026)\\\\n\\\\n### P1: 排队中\\\\n- [ ] ARC-C eval (训练完成后)\\\\n- [ ] GRPO 完成 → post-RL eval (lz* + HT + MIA)\\\\n- [ ] Post-RL Llama (cuda:2 释放后)\\\\n- [ ] ConStat 真实数据对比（ctrl-contam 模型上跑 ConStat）\\\\n\\\\n### P2: 论文\\\\n- [ ] n=10 Cohen's d 更新\\\\n- [ ] MIA 对比结果写入\\\\n- [ ] ARC-C 结果写入\\\\n- [ ] ConStat info-cost 对比表\\\\n\\\\n## Path to 4.0 (Conference / Main)\\\\n1. ✅ lz* vs HT SFT-stage 差异化 (65x)\\\\n2. ✅ Seeds n=9 d≈-6.5 (极强效果)\\\\n3. ✅ 三模型族 cross-family\\\\n4. 🔄 GRPO post-RL robustness (running)\\\\n5. 🔄 **MIA 对比** — base done, sft running\\\\n6. 🔄 **ARC-C 第二 benchmark** — 新服务器 4 卡并行启动\\\\n7. 🔄 ConStat info-cost + 真实数据对比\\\\n8. ✅ Paper 8.0p 达标\\\\n\\\\n## 关键决策日志\\\\n\\\\n| ID | 日期 | 摘要 | 关联实验 |\\\\n|----|------|------|----------|\\\\n| D030 | 2026-05-21 | D030: 跨模型 IRT 校准差异确认 — Qwen lz*=+8.68 vs Llama=-0. | exp-ctrl-contam-pilot, exp-ctrl-contam-llama-contam15 |\\\\n| D029 | 2026-05-21 | D029: θ-shift boundary condition 确认 — contam_50 d= | exp-ctrl-contam-pilot, exp-ctrl-contam-qwen-clean-s10 |\\\\n| D028 | 2026-05-21 | D028: Kill dead GRPO (reward saturation, zero grad | exp-post-rl |\\\\n| D027 | 2026-05-21 | D027: ARC-C 结果重新定位为 power function 验证 + 方法边界条件，非\\\\\\\"第 | exp-arcc-clean-s1 |\\\\n| D026 | 2026-05-21 | D026: GRPO early eval at step 2000 + ConStat 对比策略调 | exp-post-rl, exp-constat-comparison |\\\\n| D025 | 2026-05-21 | D025: 冲 4.0 — 新增 ConStat 对比 + MIA/Min-K%++ 对比 + AR | exp-constat-comparison, exp-mia-comparison, exp-arcc-ctrl-contam |\\\\n| D024 | 2026-05-21 | D024: SFT 阶段 lz* vs HT 差异化确认——lz* 在 seen/unseen 维度 | exp-post-rl, exp-baseline-comparison |\\\\n| D023 | 2026-05-21 | D023: 三模型族 cross-family generalizability 确认 — Mist | exp-ctrl-contam-mistral, exp-ctrl-contam-pilot, exp-ctrl-contam-llama |\\\\n| D022 | 2026-05-21 | Dream Round 2 分析：Best/Median 3.0, Worst 2.5 — 6项结构 | exp-baseline-comparison, exp-post-rl |\\\\n| D021 | 2026-05-21 | C群审稿 Action Matrix 定稿: seeds n=10 (Reviewer建议), R² | exp-baseline-comparison, exp-post-rl, exp-ctrl-contam-mistral |\\\\n\\\\n\\\", \\\"lines\\\": 79}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/ROADMAP.md\", \"content\": \"# irt_personfit_contam — Research Dashboard\\n\\n> 最后更新: 2026-05-21 10:16 UTC | 更新原因: 新增 westd-19912 (4 GPU), 8 卡总配置, seeds n=9 d=-6.5, MIA base done, ARC-C 并行启动\\n\\n> 核心方向\\nIRT person-fit (ℓz*) 检测 LLM benchmark contamination——minimal-information operating point。详见 paper_framing.md。\\n\\n## 当前进展\\n- **阶段**: Research + 审稿 — **冲 4.0 (Main) 模式** (D025)\\n- **Dream Round 2**: Best 3.0 / Median 3.0 / Worst 2.5\\n- **Seeds n=9 完成**: lz* mean=8.74, std=0.73, Cohen's d ≈ -6.5 (vs n=3 的 -3.42)。s10 训练中\\n- **三模型族 (D023)**: Qwen -4.83 / Llama -2.85 / Mistral -6.80\\n- **lz* vs HT (D024)**: 65x 灵敏度差异\\n- **GRPO**: step ~500/14042, cuda:2@westd-35694, ETA ~18h。计划 step 2000 中间 eval (D026)\\n- **MIA 对比**: base AUC≈0.49（近随机）✓, sft eval 完成待收集\\n- **ConStat**: bugfix 完成（Snijders 校正 + 阈值方向），策略定为 info-cost + 真实数据对比\\n- **ARC-C**: 代码+数据就绪，clean_s1 训练中@westd-35694\\n- **Paper**: 8.0p + Limitations 3 点 + Patch 5+6 完成\\n\\n## GPU 资源（8 卡）\\n| 服务器 | GPU | 当前任务 |\\n|--------|-----|---------|\\n| westd-35694:cuda:0 | ARC-C clean_s1 训练 → s8 eval 完成 |\\n| westd-35694:cuda:1 | s10 训练 (seed=307) |\\n| westd-35694:cuda:2 | **GRPO** (~18h) |\\n| westd-35694:cuda:3 | MIA sft eval → 完成后排其他 |\\n| westd-19912:cuda:0 | **新** → ARC-C clean_s1 (或环境搭建中) |\\n| westd-19912:cuda:1 | **新** → ARC-C clean_s2 |\\n| westd-19912:cuda:2 | **新** → ARC-C contam_15 |\\n| westd-19912:cuda:3 | **新** → ARC-C contam_50 |\\n\\n## 近期任务 — Path to 4.0\\n### P0: 正在执行\\n- [x] Seeds n=9 (Cohen's d ≈ -6.5)\\n- [x] MIA base eval (AUC ≈ 0.49, baseline valid)\\n- [x] ConStat bugfix (Snijders + threshold)\\n- [ ] s10 训练+eval → n=10 final\\n- [ ] MIA sft eval → sft vs base 对比\\n- [ ] **westd-19912 环境搭建 → ARC-C 4 条件并行**\\n- [ ] GRPO step 2000 中间 eval (D026)\\n\\n### P1: 排队中\\n- [ ] ARC-C eval (训练完成后)\\n- [ ] GRPO 完成 → post-RL eval (lz* + HT + MIA)\\n- [ ] Post-RL Llama (cuda:2 释放后)\\n- [ ] ConStat 真实数据对比（ctrl-contam 模型上跑 ConStat）\\n\\n### P2: 论文\\n- [ ] n=10 Cohen's d 更新\\n- [ ] MIA 对比结果写入\\n- [ ] ARC-C 结果写入\\n- [ ] ConStat info-cost 对比表\\n\\n## Path to 4.0 (Conference / Main)\\n1. ✅ lz* vs HT SFT-stage 差异化 (65x)\\n2. ✅ Seeds n=9 d≈-6.5 (极强效果)\\n3. ✅ 三模型族 cross-family\\n4. 🔄 GRPO post-RL robustness (running)\\n5. 🔄 **MIA 对比** — base done, sft running\\n6. 🔄 **ARC-C 第二 benchmark** — 新服务器 4 卡并行启动\\n7. 🔄 ConStat info-cost + 真实数据对比\\n8. ✅ Paper 8.0p 达标\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D030 | 2026-05-21 | D030: 跨模型 IRT 校准差异确认 — Qwen lz*=+8.68 vs Llama=-0. | exp-ctrl-contam-pilot, exp-ctrl-contam-llama-contam15 |\\n| D029 | 2026-05-21 | D029: θ-shift boundary condition 确认 — contam_50 d= | exp-ctrl-contam-pilot, exp-ctrl-contam-qwen-clean-s10 |\\n| D028 | 2026-05-21 | D028: Kill dead GRPO (reward saturation, zero grad | exp-post-rl |\\n| D027 | 2026-05-21 | D027: ARC-C 结果重新定位为 power function 验证 + 方法边界条件，非\\\"第 | exp-arcc-clean-s1 |\\n| D026 | 2026-05-21 | D026: GRPO early eval at step 2000 + ConStat 对比策略调 | exp-post-rl, exp-constat-comparison |\\n| D025 | 2026-05-21 | D025: 冲 4.0 — 新增 ConStat 对比 + MIA/Min-K%++ 对比 + AR | exp-constat-comparison, exp-mia-comparison, exp-arcc-ctrl-contam |\\n| D024 | 2026-05-21 | D024: SFT 阶段 lz* vs HT 差异化确认——lz* 在 seen/unseen 维度 | exp-post-rl, exp-baseline-comparison |\\n| D023 | 2026-05-21 | D023: 三模型族 cross-family generalizability 确认 — Mist | exp-ctrl-contam-mistral, exp-ctrl-contam-pilot, exp-ctrl-contam-llama |\\n| D022 | 2026-05-21 | Dream Round 2 分析：Best/Median 3.0, Worst 2.5 — 6项结构 | exp-baseline-comparison, exp-post-rl |\\n| D021 | 2026-05-21 | C群审稿 Action Matrix 定稿: seeds n=10 (Reviewer建议), R² | exp-baseline-comparison, exp-post-rl, exp-ctrl-contam-mistral |\\n\\n\", \"lines\": 79}, \"error\": null, \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "5d2deb54-3745-40dc-a436-1e3a06ef9fad",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/.claude/sessions/agent_272f846c",
  "sessionId": "465c36a7-990a-4437-ba2f-9fd3ebf0f8ef",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 22_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[HANDOFF] 你是 Main Agent，这是 Loop #2。  ## 上一轮交接 (task_context)  ### 1. 🔴 硬约束 / 红线 - GPU 白名单: westd-35694 的 cuda:0/1/2/3，不可用其他设备 - Llama 模型路径来自 ModelScope (`LLM-Research/Meta-Llama-3.1-8B-Instruct`)，不是…",
  "leafUuid": "34827b28-1069-4236-88d3-3c341d683a82",
  "sessionId": "465c36a7-990a-4437-ba2f-9fd3ebf0f8ef"
}
```

---

### Runtime record

_source line 23_

```json
{
  "type": "ai-title",
  "aiTitle": "Confirm Llama clean status and analyze contam results",
  "sessionId": "465c36a7-990a-4437-ba2f-9fd3ebf0f8ef"
}
```

---

### Assistant

_source line 24 · 2026-05-21T13:08:14.286Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze the current state from the registry and handoff:

## Registry Status Summary

**RUNNING**: None showing as RUNNING in registry
**PREPARING** (still active):
- exp-ctrl-contam-llama-clean-s8, s9, s10 (Llama multi-seed clean baselines)
- exp-post-rl-v3 (GRPO v3)
- arcc-clean-s7, s8, s9, s10 (ARC-C experiments)
- exp-arcc-benchmark (umbrella)


- exp-ctrl-contam-qwen-clean-s10, exp-constat-comparison, exp-arcc-clean-s1, s2, exp-mia-mink-comparison, and several older pilot sub-experiments still queued

**DONE (Recent Key)**:
- exp-ctrl-contam-llama-contam15: DONE, success, lz*=-2.9922, Cohen's d=-2.95
- exp-ctrl-contam-llama-contam50: DONE, success, lz*=-3.3

313, Cohen's d=-3.31
- exp-ctrl-contam-llama: DONE, success (umbrella with all 3 conditions complete)
- exp-ctrl-contam-llama-clean-s3 through s7: DONE, success (multi-seed clean baselines)
- exp-ctrl-contam-mistral: DONE, success (3rd model family)
- eval-mistral-clean-s2, s3: DONE, success
- exp-arcc-clean-s7 through s10: DONE, success

The Llama contamination experiments wrapped up with strong effect sizes, the umbrella experiment is complete with full metrics, and the clean baselines across multiple seeds are done. Mistral results are in, and the Mistral eval runs finished successfully too.

Now looking at the GPU status from the handoff—there's a mismatch between what the audit showed running and what the registry reports. The audit flagged zombie processes on GPUs 0 and 1 that need to be killed, and I need to verify whether the clean training runs for s7 and s8 are still active or if they've stalled. Looking at the registry entries more carefully, I see s7 is marked DONE with its metrics already recorded, but the GPU audit shows a process still training s7—either it finished between sessions or the Worker hasn't processed it yet. The key issue is that s8-s10 for the Llama clean experiments are stuck in PREPARING state, while s4-s7 are complete, so I need to figure out why those three aren't progressing and check what the GPU audit says about their processes. was training clean_s8 — s8 is still PREPARING in registry.

The handoff was from a few hours ago, so things may have changed. The key question is: what's currently running on the GPUs?

Let me think about what I need to do:

1. **Check GPU status** — spawn a Worker to SSH check what's currently running on westd-35694
2. **Check Llama clean s8-s10 status** — are they still training? Did any finish?
3. **Check GRPO status** — is it still running?
4. **Check if there's a pending Worker callback** — the handoff mentioned Worker `analysis:ctrl-contam-llama-results` was analyzing

Looking at the registry more carefully, the Llama experiments have progressed significantly since the handoff. The clean s4 through s7 runs all finished around 12:42-12:44 UTC, and the contamination experiments completed earlier at 11:15. The umbrella experiment finished even before that. So the Worker analysis has already been processed and the Llama pipeline is further along than expected. What's still pending are the clean s8-s10 runs, which remain in PREPARING status. I should spawn a Worker to check GPU status and process details. Re-reading the handoff, I see that exp-ctrl-contam-llama-clean was marked RUNNING but showed zero actual GPU usage — now it's DONE in the registry. Looking at the GPU audit, the timestamps suggest s7 finished recently, which aligns with it now showing DONE, though there are still zombie processes on GPUs 0 and 1 that need cleanup. The registry entry probably got updated to DONE after s7 finished, though there might be a lingering zombie process. Right now I need to check what's currently running and which GPUs are available. Looking at the roadmap for "Path to 4.0," most experiments are either done or in progress, but I'm still waiting on s10 with Qwen to complete the n=10 Cohen's d calculation.

Checking the Qwen s10 status, it shows PREPARING but already has metrics (accuracy=0.676, lz*=8.149), which is strange—the training and eval might be finished but the status wasn't updated. I need to spawn a Worker to SSH into westd-35694 and check the GPU status, then figure out what to do next based on what I find. I'm noticing a discrepancy between the handoff documentation, which lists only westd-35694's GPUs as available, and the ROADMAP that mentions westd-19912 as well—the ROADMAP might be outdated. I should check the project config directly to clarify the actual GPU allocation, then spawn a worker to check westd-35694's current status while I read through memory.md for additional context.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "34827b28-1069-4236-88d3-3c341d683a82",
  "isSidechain": false,
  "requestId": "req_011CbFmKPX11Th1c2smgZmhh",
  "type": "assistant",
  "uuid": "e8f620f8-c4d5-43a1-998c-ba8f1d12e00e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/.claude/sessions/agent_272f846c",
  "sessionId": "465c36a7-990a-4437-ba2f-9fd3ebf0f8ef",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QTnyFE9onwdVEMUpbhLYbg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 21671,
      "cache_read_input_tokens": 41695,
      "output_tokens": 3551,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 21671,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3551,
          "cache_read_input_tokens": 41695,
          "cache_creation_input_tokens": 21671,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 21671
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

_source line 25 · 2026-05-21T13:08:16.525Z_

Session 初始化完成。Registry 显示：
- **0 个 RUNNING** 实验（与 handoff 预期不符）
- **15 个 PREPARING**（含 Llama clean s8-s10、GRPO v3、ARC-C 系列、MIA 对比等）
- Llama contam15/contam50/clean 以及多个子条件已转 DONE
- Cron 0 条活跃

需要立即 SSH 确认 westd-35694 GPU 实际占用——registry 无 RUNNING 但 handoff 显示 GRPO 和多个训练进程可能仍在跑。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e8f620f8-c4d5-43a1-998c-ba8f1d12e00e",
  "isSidechain": false,
  "requestId": "req_011CbFmKPX11Th1c2smgZmhh",
  "type": "assistant",
  "uuid": "cca666a7-9347-42ee-9131-c6f9ee6406f2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/.claude/sessions/agent_272f846c",
  "sessionId": "465c36a7-990a-4437-ba2f-9fd3ebf0f8ef",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QTnyFE9onwdVEMUpbhLYbg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 21671,
      "cache_read_input_tokens": 41695,
      "output_tokens": 3551,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 21671,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3551,
          "cache_read_input_tokens": 41695,
          "cache_creation_input_tokens": 21671,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 21671
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

_source line 26 · 2026-05-21T13:08:19.001Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01HE1XKRod9uKvvLLKe5nmwC`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__spawn_worker,mcp__agent-ml-research__load_project_config,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__main_agent_post_to_director,mcp__agent-ml-research__list_workers",
  "max_results": 5
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cca666a7-9347-42ee-9131-c6f9ee6406f2",
  "isSidechain": false,
  "requestId": "req_011CbFmKPX11Th1c2smgZmhh",
  "type": "assistant",
  "uuid": "ca4abbe5-0c3f-45df-9a59-1660696002e5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/.claude/sessions/agent_272f846c",
  "sessionId": "465c36a7-990a-4437-ba2f-9fd3ebf0f8ef",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QTnyFE9onwdVEMUpbhLYbg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 21671,
      "cache_read_input_tokens": 41695,
      "output_tokens": 3551,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 21671,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3551,
          "cache_read_input_tokens": 41695,
          "cache_creation_input_tokens": 21671,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 21671
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

_source line 27 · 2026-05-21T13:08:19.018Z_

<details><summary>↩ Tool result · `toolu_01HE1XKRod9uKvvLLKe5nmwC`</summary>

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
  "tool_name": "mcp__agent-ml-research__load_project_config"
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
  "parentUuid": "ca4abbe5-0c3f-45df-9a59-1660696002e5",
  "isSidechain": false,
  "promptId": "26661264-62cc-4d8c-933c-ac64167cc12e",
  "type": "user",
  "uuid": "58b671d4-ac99-4ada-85a1-8867978cf73e",
  "toolUseResult": {
    "matches": [
      "mcp__agent-ml-research__spawn_worker",
      "mcp__agent-ml-research__load_project_config",
      "mcp__agent-ml-research__update_registry",
      "mcp__agent-ml-research__main_agent_post_to_director",
      "mcp__agent-ml-research__list_workers"
    ],
    "query": "select:mcp__agent-ml-research__spawn_worker,mcp__agent-ml-research__load_project_config,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__main_agent_post_to_director,mcp__agent-ml-research__list_workers",
    "total_deferred_tools": 82
  },
  "sourceToolAssistantUUID": "ca4abbe5-0c3f-45df-9a59-1660696002e5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/.claude/sessions/agent_272f846c",
  "sessionId": "465c36a7-990a-4437-ba2f-9fd3ebf0f8ef",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-21T13:08:19.805Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_0168qNwTVBDooZwZ5vn4RaT1`</summary>

```json
{
  "project": "irt_personfit_contam",
  "file": "memory.md",
  "max_chars": 12000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "58b671d4-ac99-4ada-85a1-8867978cf73e",
  "isSidechain": false,
  "requestId": "req_011CbFmKPX11Th1c2smgZmhh",
  "type": "assistant",
  "uuid": "095ce946-209e-4bf9-adba-26c9987fa48b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/.claude/sessions/agent_272f846c",
  "sessionId": "465c36a7-990a-4437-ba2f-9fd3ebf0f8ef",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QTnyFE9onwdVEMUpbhLYbg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 21671,
      "cache_read_input_tokens": 41695,
      "output_tokens": 3551,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 21671,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3551,
          "cache_read_input_tokens": 41695,
          "cache_creation_input_tokens": 21671,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 21671
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

_source line 29 · 2026-05-21T13:08:19.820Z_

<details><summary>↩ Tool result · `toolu_0168qNwTVBDooZwZ5vn4RaT1`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/memory.md\", \"content\": \"# Memory — irt_personfit_contam\\n\\n## OOM 教训 (2026-05-20)\\n- 7.6GB RAM 机器上，N_SIM×n_items float64 矩阵不能一次性分配。MMLU 10K×14042×8B ≈ 1.07GB 单个矩阵，compute_lz_star 内部创建 ~7 个同尺寸中间数组 → OOM\\n- 解决方案：BATCH_SIZE=500 分批计算 + N_SIM 降至 2000（统计效力足够）\\n- generate_response 和 compute_lz_star 都需要分批\\n\\n## Worker context exhaustion 教训 (2026-05-20)\\n- exp-v1-irt-refit-expanded Worker 跑 1.5 小时后崩溃，无输出。任务是从 HuggingFace 下载 500+ 模型的 per-item 数据并拟合 IRT。\\n- **根因**: 大量 HF API 调用 + 数据处理的累积输出耗尽 Worker context window。\\n- **教训**: 涉及大规模数据下载（100+ datasets）的任务必须分批 + checkpoint 中间结果，或拆成多个 Worker 串行执行。单个 Worker 不适合做 1.5hr+ 的重型数据工程。\\n- **补充 (同日)**: ssh_read_only 读取大 JSON 文件（8MB+ 单行）也会撑爆 context。Worker 操作远程大文件必须用 python 脚本提取摘要，不要 cat/head。\\n- **补充 (同日)**: Worker 无法在进程内长时间等待（~2 min 就退出）。涉及 GPU 训练 + eval 的任务应分阶段处理：训练完成后由 cron 回调触发 eval Worker，或由主 Agent 定时派 Worker 检查。\\n\\n## sim_001 关键发现 (2026-05-20)\\n- **Null check 全通过**：PSN-IRT 神经网络估计的 4PL 参数与经典 IRT 兼容，lz* ≈ N(0,1)\\n  - 大 benchmark（GSM8K/HellaSwag/MMLU）KS p 全部 > 0.01\\n  - 小 benchmark（HumanEval/ARC-C）KS p < 0.01，但属预期（items 太少，CLT 近似弱）\\n- **检测力与 n_items 强正相关**：MMLU(14042)=97.9% >> HellaSwag(10042)=73.3% >> GSM8K(1319)=57.8% >> ARC-C(295)=12.9%\\n- **Inverted-U 所有 benchmark 可观测**：power 在 25-50% contamination 达峰，100% 全部 NaN（全答对 → MLE 不收敛）\\n\\n## PSN-IRT 12 模型身份 (2026-05-20)\\n\\n**来源**：arXiv:2505.15055 (AAAI 2026 Oral)，GitHub repo `Joe-Hall-Lee/PSN-IRT`\\n\\n| student_id | θ | 正确率 | 模型名称 | 类型 |\\n|---|---|---|---|---|\\n| 0 | 1.46 | 80.6% | 360GPT2-Pro | API |\\n| 1 | 3.77 | 85.7% | DeepSeek-V3 | API |\\n| 2 | 1.14 | 78.9% | Doubao-pro | API |\\n| 3 | 0.78 | 84.5% | Gemini-1.5 | API |\\n| 4 | -3.38 | 23.1% | Gemma-2B-it | 开源 2B |\\n| 5 | 1.73 | 82.1% | Hunyuan-Turbo | API |\\n| 6 | -1.37 | 40.0% | Mistral-7B-Instruct-v0.1 | 开源 7B |\\n| 7 | 0.93 | 77.0% | Moonshot-v1 | API |\\n| 8 | 0.96 | 76.3% | Qwen-Plus | API |\\n| 9 | -0.13 | 60.4% | Qwen2.5-3B-Instruct | 开源 3B |\\n| 10 | -1.89 | 31.6% | Vicuna-7B-v1.3 | 开源 7B |\\n| 11 | 0.77 | 75.2% | Yi-Lightning | API |\\n\\n## Gemini-1.5 × 100% contamination 精确匹配 (2026-05-20)\\n\\nGemini-1.5 MMLU lz*(benchmark-specific θ) = +31.815 = 100% contamination simulation lz* = +31.815（完全一致）。机制：100% accuracy → θ_bench=4.0 → lz* deterministic。其他 benchmark Gemini-1.5 lz* 为负（非 100% acc），说明异常是 benchmark-specific 的。\\n\\n## exp-extended-sim 关键发现 (2026-05-20)\\n\\n- Dual-regime crossover 75-90%：所有 5 benchmark 在此区间 lz* 从负翻正\\n- 100% contamination lz* deterministic (std=0.0)\\n- Inverted-U 全 5 benchmark 确认\\n\\n## exp-two-sided 关键教训 (2026-05-20)\\n\\n95% flagging 即使用 benchmark-specific θ + bootstrap + FDR 也无法降低。LLM 系统性违反 4PL 假设（单维+局部独立）。绝对阈值对 real data 无意义，需 controlled calibration (Δlz*)。\\n\\n## exp-empirical-null 关键发现 (2026-05-20)\\n\\nBootstrap null 校准良好（mean bias=0.09, std=1.002）。95% flagging 不是 null miscalibration，而是 LLM response pattern 产生极端 lz*。大 benchmark KS reject 仅 8.3%，小 benchmark 58-75%（有限样本效应）。\\n\\n## exp-power-theory 关键发现 (2026-05-20)\\n\\nR²(two-sided)=0.957, R²(left-tail)=0.976, R²(mean lz*)=0.995。δ ∝ √n confirmed。Inverted-U 拐点理论值 π*≈81-85%。最小 n_items (80% power): 15% contam→~8K, 25%→~3K, 50%→~1K。\\n\\n## exp-item-alignment-check 关键发现 (2026-05-20)\\n\\n**PSN-IRT 与 v1 Leaderboard item ordering 不对齐。** 直接位置匹配率 54.56%（≈随机）。Content-based 重排后 Mistral 88.46%, Vicuna 72.48%。\\n\\n**根因**: PSN-IRT 保持 raw MMLU 原始顺序，v1 leaderboard 在 subject 内部 shuffle。且 PSN-IRT 是独立评测（不同 prompt/few-shot），即使对齐后仍有 ~12% response 差异。\\n\\n**结论**: **不可混用 v1 responses + PSN-IRT parameters**。~12% 噪声对 item-level person-fit 统计量影响严重。\\n\\n**已生成 item_mapping.csv**: 12068/14042 items 的 v1→PSN-IRT 位置映射，可用于未来 content-based 对齐需求。\\n\\n## Open LLM Leaderboard v1 per-item data (2026-05-20)\\n\\n**来源**: `open-llm-leaderboard-old/details_{org}__{model}` HuggingFace datasets\\n**格式**: Parquet, `acc`/`acc_norm` 二值字段\\n**覆盖**: MMLU ✅, HellaSwag ✅, ARC-C ✅, GSM8K ✅ | HumanEval ❌\\n**模型数**: 13,000+\\n**⚠️ 不可直接用 PSN-IRT parameters** — 见 item-alignment-check 发现\\n\\n## exp-fdr-correction 关键发现 (2026-05-20)\\n\\nexp-two-sided v2 的 `empirical_pvalues.csv` 已包含 global BH-FDR 校正（60 cells 一起做 BH）。校正前后 flagging 均为 57/60 (95%)——因大多数 cells empirical p=0.000，BH 校正无实质影响。Leaderboard-scale FDR (24800+ tests) 需在 leaderboard audit 中单独处理。\\n\\n## exp-clean-control-delta 关键发现 (2026-05-20)\\n\\nClean-vs-clean Δlz* 均值全部接近 0（|mean| < 0.13），无一显著，确认 estimation noise floor ~ N(0, 1.4)。\\nClean-vs-contaminated (25%) Δlz* 均高度显著（p<1e-10），Cohen's d: MMLU=2.66, HellaSwag=1.85, GSM8K=1.85, HumanEval=1.07, ARC-C=0.45。\\nARC-C d=0.45 略低 0.5 阈值（仅 295 items），与 power theory 一致。\\n论文中标注为 \\\"theoretical noise floor\\\"，真实 SFT clean-vs-clean 在 ctrl-contam-pilot 中实现。\\n\\n## exp-ml-classifier-baseline 关键发现 (2026-05-20)\\n\\n**lz* 在低污染率 (5-10%) 优于有监督 ML 分类器**：5% contam lz* AUROC 0.675 vs best ML 0.575 (+0.10); 10% contam 0.763 vs 0.712 (+0.05)。ML 仅在 25%+ 污染时略胜 (+0.05)，但需 oracle contamination labels（实际不可用）。\\nRF feature importance 在 items 间高度弥散（top item <1%），与 lz* 全局 likelihood 方法一致。\\n论文限定为 simulation 场景下的对比，不推广为\\\"所有 binary-only ML 方法都不如 IRT\\\"。\\n\\n## exp-domain-analysis 关键发现 (2026-05-20)\\n\\n**Gemini-1.5 MMLU 100% accuracy 覆盖全部 57 个 subject**——不是 domain-concentrated 泄漏，是完全数据集泄漏。50/57 subjects flagged (lz*>1.96)，未 flagged 的 7 个 subject 的 lz* 也很高但 item 数太少。\\n\\n**模型 contamination 指纹多样**：\\n- Doubao-pro: 反向 pattern，Humanities/Social Sciences lz* 极负（-13~-15），STEM 接近 0，Other 正向——可能是训练数据偏科\\n- Hunyuan-Turbo: STEM lz*=1.8 vs Social Sciences lz*=13.9——Social Sciences 方向过度拟合\\n- Yi-Lightning 和 Qwen-Plus: 全 domain 高 lz*（16~28），领先所有其他模型\\n\\n**论文价值**: domain decomposition 为 12-model case study 增加定性分析深度，但 non-essential（P2 级别）。\\n\\n**virology lz*=-8.21 诊断**：双重根因——(1) global θ=0.78 vs MMLU θ_MLE=4.0 错配；(2) virology 全部 166 items d<1.0 (mean=0.71)，即使 θ=4.0 仍有 58/166 items P<0.5。是 PSN-IRT calibration artifact，不影响 overall lz*=34.75。per-subject 分析需加 caveat。\\n\\n## exp-natural-experiment 关键发现 (2026-05-20)\\n\\n21 对 base→chat 模型 × 4 benchmarks（MMLU/HellaSwag/ARC-C/GSM8K）。\\n\\n**两个 benchmark 有显著系统性 SFT 效应**：\\n- HellaSwag: Δlz* 偏差 mean=-3.40, t=-3.97, p=0.001（SFT 系统性降低 person-fit）\\n- GSM8K: Δlz* 偏差 mean=+3.92, t=3.35, p=0.009（SFT 系统性提高 person-fit）\\n- MMLU/ARC-C 无显著效应\\n\\n**无个体 pair outlier**——未能检测到单个模型的 benchmark-specific contamination。\\n**Director 评估价值极低（P2-optional）**，不作为核心 evidence 使用。\\n\\n## exp-4pl-ablation 关键发现 (2026-05-20)\\n\\n**4PL d 参数对检测力的影响是决定性的，不是锦上添花。**\\n\\n核心数据（4PL vs 3PL(d=1)，平均 power gain across contamination levels）：\\n- MMLU: +27.3pp (max +49.0pp)\\n- HellaSwag: +26.1pp (max +59.6pp)\\n- GSM8K: +20.3pp (max +39.7pp)\\n- ARC_C: +14.8pp (max +54.6pp)\\n- HumanEval: +13.7pp (max +30.6pp)\\n\\nFAR 校准：4PL ≈ 5%（正确），3PL 4.7-16.5%（偏高），2PL 50-100%（完全不可用——固定 c=0.25 灾难性错误）。\\n\\n**d-bucket 机制确认**：d<0.8 的 items 上 4PL 优势最大（MMLU +61pp），d≥0.95 时差异可忽略。这证实 d 参数捕捉 ceiling effect 是检测力提升的关键来源。\\n\\n**论文价值**：回应 Reviewer R8 concern（为什么用 4PL 而非 3PL）。46% MMLU items d<0.95，忽略 d 约将检测力减半。这是 Method 部分的核心 justification。\\n\\n## exp-4pl-real-data-degradation 关键发现 (2026-05-20)\\n\\n**实数据验证：d 参数的影响对高能力模型是毁灭性的。**\\n\\n在 12 个 PSN-IRT 模型的真实响应数据上，4PL vs 3PL(d=1) 的 lz* 仅有 r=0.225, RMSE=68.41——几乎无关联。\\n\\n**不对称影响机制**：d=1 使 P(θ)→1（高能力模型预期全部答对），导致少量错误被 lz* 放大为极端异常值。低能力模型的 P(θ) 本身就远离 1.0，d=1 vs d<1 差异小，因此几乎不受影响。\\n\\n- DeepSeek-V3 (θ=3.77): MMLU lz* 从 +16.4 暴跌至 -340.6\\n- Gemma-2B-it / Vicuna / Mistral (低 θ): |Δlz*|<2\\n- MMLU 最严重（46% items d<0.95），mean |Δlz*|=58.3\\n\\n**与 exp-4pl-ablation 的互补**：ablation 在模拟数据上证明 power 损失，本实验在实数据上证明 lz* 值本身被完全摧毁。二者形成 R8 的双重证据链——4PL d 参数不可或缺。\\n\\n**论文写作注意**：这个结果特别适合做 case study 可视化（选 DeepSeek-V3 on MMLU 作为 extreme case），放在 ablation study 或 appendix 中。\\n\\n## exp-ctrl-contam-pilot 关键发现 (2026-05-20)\\n\\n**首次真实 LLM controlled contamination 实验。** Qwen2.5-7B-Instruct QLoRA SFT，4+1 条件。\\n\\n**核心结果（n=3 clean seeds, ddof=1）**：\\n| Condition | Accuracy | θ_MLE | lz* |\\n|-----------|----------|-------|-----|\\n| clean_s1 (seed=42) | 0.6787 | -0.0987 | 8.0101 |\\n| clean_s2 (seed=123) | 0.6789 | -0.0842 | 5.9440 |\\n| clean_s3 (seed=456) | 0.6783 | -0.1068 | 8.0806 |\\n| contam_15 | 0.7310 | +0.1971 | 3.0046 |\\n| contam_50 | 0.7644 | +0.3703 | 5.4480 |\\n\\n**Baseline（n=3）**: mean=7.3449, std=1.2137\\n**Cohen's d（n=3, ddof=1）**: contam_15 d=-3.58, contam_50 d=-1.56\\n**注意**：之前汇报的 d=-3.85 / d=-1.48 使用了 ddof=0。论文统一用 ddof=1。\\n\\n**H1 ✓ H2 ✓ H3 ✗(θ-free) H4 ✗**\\n\\n**θ-shift 是 dose-response 倒置的确切原因**：\\n- contamination 抬高 θ_MLE（clean -0.09 → contam_50 +0.37），MLE 将 contamination 信号解释为 \\\"能力提升\\\"\\n- θ-fixed（固定为 clean θ 均值 -0.0914）下，dose-response 恢复单调：\\n  - |Δlz*_fixed_15| = 2.96, |Δlz*_fixed_50| = 8.67, ratio = 2.93 ✅\\n- θ-shift 分别吸收了 contam_15 的 6.93 和 contam_50 的 10.20 lz* 单位信号\\n\\n**clean seed 变异性**：s1 和 s3 的 lz* 接近（8.01, 8.08），s2 明显低（5.94）。n=3 baseline std=1.21 vs n=2 的 1.46，加入 s3 压缩了方差，使 Cohen's d 更极端。\\n\\n**Memorization fraction 低于预期**（0.38/0.29 vs 假设的 >0.5）——QLoRA 3 epochs 不足以产生强 memorization，但足以产生可检测的 lz* 偏移。\\n\\n**论文叙事价值**：\\n1. θ-shift = \\\"ability inflation\\\" 是 contamination 逃避 person-fit 检测的核心机制\\n2. 与 simulation inverted-U 发现形成呼应——real-world 版本的同一现象\\n3. θ-fixed 分析作为 supplementary evidence 证明底层信号单调递增\\n4. 支撑 Discussion 中 \\\"θ estimation as confound\\\" 段落\\n\\n## GPU 审计 (2026-05-21 15:47 UTC)\\n\\n### GPU 占用总览\\n| GPU | PID | Process | VRAM | Status |\\n|-----|------|---------|------|--------|\\n| 0 | 98622 | eval_lz.py --condition clean_s5 --gpu 0 | 8,628 MiB | **ZOMBIE** — s5 results 已存在 |\\n| 0 | 99214 | train.py --condition clean_s7 --gpu 3 | 37,694 MiB | 运行中, 56/939 steps (~6%) |\\n| 1 | 96745 | train.py --condition clean_s6 --gpu 0 | 23,102 MiB | **ZOMBIE** — 训练已完成，模型已保存 |\\n| 2 | 97791 | train_grpo.py | 8,062 MiB | 运行中, 134/14042 steps (~1%), ETA ~20h |\\n| 3 | 99807 | train.py --condition clean_s8 --gpu 0 | 27,470 MiB | 运行中 (无日志) |\\n\\n### 进程状态\\n- **PID 97791 (GRPO)**: 存活, step 134/14042, epoch 0.0078, ~5.1s/step, reward 0.3-0.78 波动, ETA ~19h\\n- **PID 96745 (s6 train)**: 存活但已完成 — 3 epoch 训练结束, model saved to checkpoints/clean_s6, 仍占 GPU 1 23GB\\n- **PID 99214 (s7 train)**: 存活, 56/939 steps (~6%), ~2s/step\\n- **PID 99807 (s8 train)**: 存活, 无日志输出\\n- **PID 98622 (s5 eval)**: 存活但 s5 results 已存在 — zombie\\n- **PID 98896, 98897**: 已死亡\\n\\n### Eval 结果\\n| Condition | Accuracy | θ_MLE | lz* |\\n|-----------|----------|-------|-----|\\n| clean_s3 | 0.6783 | -0.1068 | 9.5293 |\\n| clean_s4 | 0.6786 | -0.1092 | 8.9673 |\\n| clean_s5 | 0.6787 | -0.0875 | 8.5322 |\\n| clean_s6 | — | — | — (训练刚完成, eval 未开始) |\\n\\n### HT post-RL 结果\\n| Stage | Accuracy | θ_MLE | lz* | acc_seen | acc_unseen | lz*_seen | lz*_unseen |\\n|-------|----------|-------|-----|----------|------------|----------|------------|\\n| SFT | 0.7339 | +0.2281 | 2.914 | 0.8310 | 0.7167 | -0.395 | 3.278 |\\n\\nbase_results.json 也存在。\\n\\n### 建议操作\\n1. **Kill PID 98622** — s5 eval zombie, 浪费 GPU 0 上 8.6GB\\n2. **Kill PID 96745** — s6 训练已完成, 浪费 GPU 1 上 23.1GB → 释放后可启动 s6 eval\\n3. s7 (GPU 0) 和 s8 (GPU 3) 正常运行中, 不动\\n4. GRPO (GPU 2) 正常运行中, 不动\\n5. GPU 1 清理后启动 clean_s6 eval\\n\\n## MIA 对比准备 (2026-05-21)\\n\\n**目标**：用 MIA (Min-K%/Min-K%++) 作为 baseline，与 lz* 对比在 post-RL 模型上的检测能力。Wang et al. (2025) 证明 MIA 在 post-RL 模型上失效，我们要展示 lz* 在 GRPO 后仍有效。\\n\\n**脚本就绪**：\\n- `/root/autodl-tmp/post_rl_contam/eval_mia.py` — MIA 评估脚本（Min-K% + Min-K%++），支持 `--stage base|sft|grpo --gpu N`\\n- `/root/autodl-tmp/post_rl_contam/compare_mia_lz.py` — 对比表生成（加载 MIA + lz* 结果，输出对比 AUC-ROC）\\n- 依赖 scikit-learn 已安装\\n\\n**算法实现**：\\n- Min-K%: token log-prob 最小 K% 的均值（K=10,20,30,40,50）\\n- Min-K%++: 标准化 log-prob (z = (log_p - μ_vocab) / σ_vocab) 最小 K% 的均值\\n- 同时计算 Loss baseline（平均 log-prob）\\n- 输出 per-item scores + AUC-ROC\\n\\n**运行方式**：`python eval_mia.py --stage base --gpu 0`（需 GPU，14042 items，预估 1-2h/stage）\\n\\n**参考文献**：\\n- Min-K%++: Zhang et al. (2024), ICLR 2025 Spotlight, [github.com/zjysteven/mink-plus-plus](https://github.com/zjysteven/mink-plus-plus)\\n- Min-K%: Shi et al. (2024) \\\"Detecting Pretraining Data from Large Language Models\\\"\\n\\n## ConStat 对比分析 (2026-05-21, updated)\\n\\n**论文**: Dekoninck et al., \\\"ConStat: Performance-Based Contamination Detection in Large Language Models\\\", NeurIPS 2024.\\n**代码**: [github.com/eth-sri/ConStat](https://github.com/eth-sri/ConStat), 已 clone 到 `/root/autodl-tmp/ConStat/`, pip install -e . 完成。\\n\\n### ConStat 方法核心\\n\\nConStat 是 **dual-benchmark + multi-model** 方法：通过比较 target model 在 primary benchmark vs reference benchmark 上的性能增量，判断 primary 是否被污染。核心逻辑——如果 model 在 primary 上的表现显著高于 spline(reference_perf) 的预测，则 primary 被污染。\\n\\n### 输入要求对比\\n\\n| 维度 | ConStat | lz* (ours) |\\n|------|---------|------------|\\n| Benchmarks | 2 (primary + reference) | 1 |\\n| Ref\\n\\n... [截断: 省略 3010 字符，传 max_chars=0 获取完整内容]\", \"total_chars\": 15010, \"truncated\": true}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "095ce946-209e-4bf9-adba-26c9987fa48b",
  "isSidechain": false,
  "promptId": "26661264-62cc-4d8c-933c-ac64167cc12e",
  "type": "user",
  "uuid": "fb38ef3c-1262-4a3e-a872-1d65aac13f39",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/memory.md\\\", \\\"content\\\": \\\"# Memory — irt_personfit_contam\\\\n\\\\n## OOM 教训 (2026-05-20)\\\\n- 7.6GB RAM 机器上，N_SIM×n_items float64 矩阵不能一次性分配。MMLU 10K×14042×8B ≈ 1.07GB 单个矩阵，compute_lz_star 内部创建 ~7 个同尺寸中间数组 → OOM\\\\n- 解决方案：BATCH_SIZE=500 分批计算 + N_SIM 降至 2000（统计效力足够）\\\\n- generate_response 和 compute_lz_star 都需要分批\\\\n\\\\n## Worker context exhaustion 教训 (2026-05-20)\\\\n- exp-v1-irt-refit-expanded Worker 跑 1.5 小时后崩溃，无输出。任务是从 HuggingFace 下载 500+ 模型的 per-item 数据并拟合 IRT。\\\\n- **根因**: 大量 HF API 调用 + 数据处理的累积输出耗尽 Worker context window。\\\\n- **教训**: 涉及大规模数据下载（100+ datasets）的任务必须分批 + checkpoint 中间结果，或拆成多个 Worker 串行执行。单个 Worker 不适合做 1.5hr+ 的重型数据工程。\\\\n- **补充 (同日)**: ssh_read_only 读取大 JSON 文件（8MB+ 单行）也会撑爆 context。Worker 操作远程大文件必须用 python 脚本提取摘要，不要 cat/head。\\\\n- **补充 (同日)**: Worker 无法在进程内长时间等待（~2 min 就退出）。涉及 GPU 训练 + eval 的任务应分阶段处理：训练完成后由 cron 回调触发 eval Worker，或由主 Agent 定时派 Worker 检查。\\\\n\\\\n## sim_001 关键发现 (2026-05-20)\\\\n- **Null check 全通过**：PSN-IRT 神经网络估计的 4PL 参数与经典 IRT 兼容，lz* ≈ N(0,1)\\\\n  - 大 benchmark（GSM8K/HellaSwag/MMLU）KS p 全部 > 0.01\\\\n  - 小 benchmark（HumanEval/ARC-C）KS p < 0.01，但属预期（items 太少，CLT 近似弱）\\\\n- **检测力与 n_items 强正相关**：MMLU(14042)=97.9% >> HellaSwag(10042)=73.3% >> GSM8K(1319)=57.8% >> ARC-C(295)=12.9%\\\\n- **Inverted-U 所有 benchmark 可观测**：power 在 25-50% contamination 达峰，100% 全部 NaN（全答对 → MLE 不收敛）\\\\n\\\\n## PSN-IRT 12 模型身份 (2026-05-20)\\\\n\\\\n**来源**：arXiv:2505.15055 (AAAI 2026 Oral)，GitHub repo `Joe-Hall-Lee/PSN-IRT`\\\\n\\\\n| student_id | θ | 正确率 | 模型名称 | 类型 |\\\\n|---|---|---|---|---|\\\\n| 0 | 1.46 | 80.6% | 360GPT2-Pro | API |\\\\n| 1 | 3.77 | 85.7% | DeepSeek-V3 | API |\\\\n| 2 | 1.14 | 78.9% | Doubao-pro | API |\\\\n| 3 | 0.78 | 84.5% | Gemini-1.5 | API |\\\\n| 4 | -3.38 | 23.1% | Gemma-2B-it | 开源 2B |\\\\n| 5 | 1.73 | 82.1% | Hunyuan-Turbo | API |\\\\n| 6 | -1.37 | 40.0% | Mistral-7B-Instruct-v0.1 | 开源 7B |\\\\n| 7 | 0.93 | 77.0% | Moonshot-v1 | API |\\\\n| 8 | 0.96 | 76.3% | Qwen-Plus | API |\\\\n| 9 | -0.13 | 60.4% | Qwen2.5-3B-Instruct | 开源 3B |\\\\n| 10 | -1.89 | 31.6% | Vicuna-7B-v1.3 | 开源 7B |\\\\n| 11 | 0.77 | 75.2% | Yi-Lightning | API |\\\\n\\\\n## Gemini-1.5 × 100% contamination 精确匹配 (2026-05-20)\\\\n\\\\nGemini-1.5 MMLU lz*(benchmark-specific θ) = +31.815 = 100% contamination simulation lz* = +31.815（完全一致）。机制：100% accuracy → θ_bench=4.0 → lz* deterministic。其他 benchmark Gemini-1.5 lz* 为负（非 100% acc），说明异常是 benchmark-specific 的。\\\\n\\\\n## exp-extended-sim 关键发现 (2026-05-20)\\\\n\\\\n- Dual-regime crossover 75-90%：所有 5 benchmark 在此区间 lz* 从负翻正\\\\n- 100% contamination lz* deterministic (std=0.0)\\\\n- Inverted-U 全 5 benchmark 确认\\\\n\\\\n## exp-two-sided 关键教训 (2026-05-20)\\\\n\\\\n95% flagging 即使用 benchmark-specific θ + bootstrap + FDR 也无法降低。LLM 系统性违反 4PL 假设（单维+局部独立）。绝对阈值对 real data 无意义，需 controlled calibration (Δlz*)。\\\\n\\\\n## exp-empirical-null 关键发现 (2026-05-20)\\\\n\\\\nBootstrap null 校准良好（mean bias=0.09, std=1.002）。95% flagging 不是 null miscalibration，而是 LLM response pattern 产生极端 lz*。大 benchmark KS reject 仅 8.3%，小 benchmark 58-75%（有限样本效应）。\\\\n\\\\n## exp-power-theory 关键发现 (2026-05-20)\\\\n\\\\nR²(two-sided)=0.957, R²(left-tail)=0.976, R²(mean lz*)=0.995。δ ∝ √n confirmed。Inverted-U 拐点理论值 π*≈81-85%。最小 n_items (80% power): 15% contam→~8K, 25%→~3K, 50%→~1K。\\\\n\\\\n## exp-item-alignment-check 关键发现 (2026-05-20)\\\\n\\\\n**PSN-IRT 与 v1 Leaderboard item ordering 不对齐。** 直接位置匹配率 54.56%（≈随机）。Content-based 重排后 Mistral 88.46%, Vicuna 72.48%。\\\\n\\\\n**根因**: PSN-IRT 保持 raw MMLU 原始顺序，v1 leaderboard 在 subject 内部 shuffle。且 PSN-IRT 是独立评测（不同 prompt/few-shot），即使对齐后仍有 ~12% response 差异。\\\\n\\\\n**结论**: **不可混用 v1 responses + PSN-IRT parameters**。~12% 噪声对 item-level person-fit 统计量影响严重。\\\\n\\\\n**已生成 item_mapping.csv**: 12068/14042 items 的 v1→PSN-IRT 位置映射，可用于未来 content-based 对齐需求。\\\\n\\\\n## Open LLM Leaderboard v1 per-item data (2026-05-20)\\\\n\\\\n**来源**: `open-llm-leaderboard-old/details_{org}__{model}` HuggingFace datasets\\\\n**格式**: Parquet, `acc`/`acc_norm` 二值字段\\\\n**覆盖**: MMLU ✅, HellaSwag ✅, ARC-C ✅, GSM8K ✅ | HumanEval ❌\\\\n**模型数**: 13,000+\\\\n**⚠️ 不可直接用 PSN-IRT parameters** — 见 item-alignment-check 发现\\\\n\\\\n## exp-fdr-correction 关键发现 (2026-05-20)\\\\n\\\\nexp-two-sided v2 的 `empirical_pvalues.csv` 已包含 global BH-FDR 校正（60 cells 一起做 BH）。校正前后 flagging 均为 57/60 (95%)——因大多数 cells empirical p=0.000，BH 校正无实质影响。Leaderboard-scale FDR (24800+ tests) 需在 leaderboard audit 中单独处理。\\\\n\\\\n## exp-clean-control-delta 关键发现 (2026-05-20)\\\\n\\\\nClean-vs-clean Δlz* 均值全部接近 0（|mean| < 0.13），无一显著，确认 estimation noise floor ~ N(0, 1.4)。\\\\nClean-vs-contaminated (25%) Δlz* 均高度显著（p<1e-10），Cohen's d: MMLU=2.66, HellaSwag=1.85, GSM8K=1.85, HumanEval=1.07, ARC-C=0.45。\\\\nARC-C d=0.45 略低 0.5 阈值（仅 295 items），与 power theory 一致。\\\\n论文中标注为 \\\\\\\"theoretical noise floor\\\\\\\"，真实 SFT clean-vs-clean 在 ctrl-contam-pilot 中实现。\\\\n\\\\n## exp-ml-classifier-baseline 关键发现 (2026-05-20)\\\\n\\\\n**lz* 在低污染率 (5-10%) 优于有监督 ML 分类器**：5% contam lz* AUROC 0.675 vs best ML 0.575 (+0.10); 10% contam 0.763 vs 0.712 (+0.05)。ML 仅在 25%+ 污染时略胜 (+0.05)，但需 oracle contamination labels（实际不可用）。\\\\nRF feature importance 在 items 间高度弥散（top item <1%），与 lz* 全局 likelihood 方法一致。\\\\n论文限定为 simulation 场景下的对比，不推广为\\\\\\\"所有 binary-only ML 方法都不如 IRT\\\\\\\"。\\\\n\\\\n## exp-domain-analysis 关键发现 (2026-05-20)\\\\n\\\\n**Gemini-1.5 MMLU 100% accuracy 覆盖全部 57 个 subject**——不是 domain-concentrated 泄漏，是完全数据集泄漏。50/57 subjects flagged (lz*>1.96)，未 flagged 的 7 个 subject 的 lz* 也很高但 item 数太少。\\\\n\\\\n**模型 contamination 指纹多样**：\\\\n- Doubao-pro: 反向 pattern，Humanities/Social Sciences lz* 极负（-13~-15），STEM 接近 0，Other 正向——可能是训练数据偏科\\\\n- Hunyuan-Turbo: STEM lz*=1.8 vs Social Sciences lz*=13.9——Social Sciences 方向过度拟合\\\\n- Yi-Lightning 和 Qwen-Plus: 全 domain 高 lz*（16~28），领先所有其他模型\\\\n\\\\n**论文价值**: domain decomposition 为 12-model case study 增加定性分析深度，但 non-essential（P2 级别）。\\\\n\\\\n**virology lz*=-8.21 诊断**：双重根因——(1) global θ=0.78 vs MMLU θ_MLE=4.0 错配；(2) virology 全部 166 items d<1.0 (mean=0.71)，即使 θ=4.0 仍有 58/166 items P<0.5。是 PSN-IRT calibration artifact，不影响 overall lz*=34.75。per-subject 分析需加 caveat。\\\\n\\\\n## exp-natural-experiment 关键发现 (2026-05-20)\\\\n\\\\n21 对 base→chat 模型 × 4 benchmarks（MMLU/HellaSwag/ARC-C/GSM8K）。\\\\n\\\\n**两个 benchmark 有显著系统性 SFT 效应**：\\\\n- HellaSwag: Δlz* 偏差 mean=-3.40, t=-3.97, p=0.001（SFT 系统性降低 person-fit）\\\\n- GSM8K: Δlz* 偏差 mean=+3.92, t=3.35, p=0.009（SFT 系统性提高 person-fit）\\\\n- MMLU/ARC-C 无显著效应\\\\n\\\\n**无个体 pair outlier**——未能检测到单个模型的 benchmark-specific contamination。\\\\n**Director 评估价值极低（P2-optional）**，不作为核心 evidence 使用。\\\\n\\\\n## exp-4pl-ablation 关键发现 (2026-05-20)\\\\n\\\\n**4PL d 参数对检测力的影响是决定性的，不是锦上添花。**\\\\n\\\\n核心数据（4PL vs 3PL(d=1)，平均 power gain across contamination levels）：\\\\n- MMLU: +27.3pp (max +49.0pp)\\\\n- HellaSwag: +26.1pp (max +59.6pp)\\\\n- GSM8K: +20.3pp (max +39.7pp)\\\\n- ARC_C: +14.8pp (max +54.6pp)\\\\n- HumanEval: +13.7pp (max +30.6pp)\\\\n\\\\nFAR 校准：4PL ≈ 5%（正确），3PL 4.7-16.5%（偏高），2PL 50-100%（完全不可用——固定 c=0.25 灾难性错误）。\\\\n\\\\n**d-bucket 机制确认**：d<0.8 的 items 上 4PL 优势最大（MMLU +61pp），d≥0.95 时差异可忽略。这证实 d 参数捕捉 ceiling effect 是检测力提升的关键来源。\\\\n\\\\n**论文价值**：回应 Reviewer R8 concern（为什么用 4PL 而非 3PL）。46% MMLU items d<0.95，忽略 d 约将检测力减半。这是 Method 部分的核心 justification。\\\\n\\\\n## exp-4pl-real-data-degradation 关键发现 (2026-05-20)\\\\n\\\\n**实数据验证：d 参数的影响对高能力模型是毁灭性的。**\\\\n\\\\n在 12 个 PSN-IRT 模型的真实响应数据上，4PL vs 3PL(d=1) 的 lz* 仅有 r=0.225, RMSE=68.41——几乎无关联。\\\\n\\\\n**不对称影响机制**：d=1 使 P(θ)→1（高能力模型预期全部答对），导致少量错误被 lz* 放大为极端异常值。低能力模型的 P(θ) 本身就远离 1.0，d=1 vs d<1 差异小，因此几乎不受影响。\\\\n\\\\n- DeepSeek-V3 (θ=3.77): MMLU lz* 从 +16.4 暴跌至 -340.6\\\\n- Gemma-2B-it / Vicuna / Mistral (低 θ): |Δlz*|<2\\\\n- MMLU 最严重（46% items d<0.95），mean |Δlz*|=58.3\\\\n\\\\n**与 exp-4pl-ablation 的互补**：ablation 在模拟数据上证明 power 损失，本实验在实数据上证明 lz* 值本身被完全摧毁。二者形成 R8 的双重证据链——4PL d 参数不可或缺。\\\\n\\\\n**论文写作注意**：这个结果特别适合做 case study 可视化（选 DeepSeek-V3 on MMLU 作为 extreme case），放在 ablation study 或 appendix 中。\\\\n\\\\n## exp-ctrl-contam-pilot 关键发现 (2026-05-20)\\\\n\\\\n**首次真实 LLM controlled contamination 实验。** Qwen2.5-7B-Instruct QLoRA SFT，4+1 条件。\\\\n\\\\n**核心结果（n=3 clean seeds, ddof=1）**：\\\\n| Condition | Accuracy | θ_MLE | lz* |\\\\n|-----------|----------|-------|-----|\\\\n| clean_s1 (seed=42) | 0.6787 | -0.0987 | 8.0101 |\\\\n| clean_s2 (seed=123) | 0.6789 | -0.0842 | 5.9440 |\\\\n| clean_s3 (seed=456) | 0.6783 | -0.1068 | 8.0806 |\\\\n| contam_15 | 0.7310 | +0.1971 | 3.0046 |\\\\n| contam_50 | 0.7644 | +0.3703 | 5.4480 |\\\\n\\\\n**Baseline（n=3）**: mean=7.3449, std=1.2137\\\\n**Cohen's d（n=3, ddof=1）**: contam_15 d=-3.58, contam_50 d=-1.56\\\\n**注意**：之前汇报的 d=-3.85 / d=-1.48 使用了 ddof=0。论文统一用 ddof=1。\\\\n\\\\n**H1 ✓ H2 ✓ H3 ✗(θ-free) H4 ✗**\\\\n\\\\n**θ-shift 是 dose-response 倒置的确切原因**：\\\\n- contamination 抬高 θ_MLE（clean -0.09 → contam_50 +0.37），MLE 将 contamination 信号解释为 \\\\\\\"能力提升\\\\\\\"\\\\n- θ-fixed（固定为 clean θ 均值 -0.0914）下，dose-response 恢复单调：\\\\n  - |Δlz*_fixed_15| = 2.96, |Δlz*_fixed_50| = 8.67, ratio = 2.93 ✅\\\\n- θ-shift 分别吸收了 contam_15 的 6.93 和 contam_50 的 10.20 lz* 单位信号\\\\n\\\\n**clean seed 变异性**：s1 和 s3 的 lz* 接近（8.01, 8.08），s2 明显低（5.94）。n=3 baseline std=1.21 vs n=2 的 1.46，加入 s3 压缩了方差，使 Cohen's d 更极端。\\\\n\\\\n**Memorization fraction 低于预期**（0.38/0.29 vs 假设的 >0.5）——QLoRA 3 epochs 不足以产生强 memorization，但足以产生可检测的 lz* 偏移。\\\\n\\\\n**论文叙事价值**：\\\\n1. θ-shift = \\\\\\\"ability inflation\\\\\\\" 是 contamination 逃避 person-fit 检测的核心机制\\\\n2. 与 simulation inverted-U 发现形成呼应——real-world 版本的同一现象\\\\n3. θ-fixed 分析作为 supplementary evidence 证明底层信号单调递增\\\\n4. 支撑 Discussion 中 \\\\\\\"θ estimation as confound\\\\\\\" 段落\\\\n\\\\n## GPU 审计 (2026-05-21 15:47 UTC)\\\\n\\\\n### GPU 占用总览\\\\n| GPU | PID | Process | VRAM | Status |\\\\n|-----|------|---------|------|--------|\\\\n| 0 | 98622 | eval_lz.py --condition clean_s5 --gpu 0 | 8,628 MiB | **ZOMBIE** — s5 results 已存在 |\\\\n| 0 | 99214 | train.py --condition clean_s7 --gpu 3 | 37,694 MiB | 运行中, 56/939 steps (~6%) |\\\\n| 1 | 96745 | train.py --condition clean_s6 --gpu 0 | 23,102 MiB | **ZOMBIE** — 训练已完成，模型已保存 |\\\\n| 2 | 97791 | train_grpo.py | 8,062 MiB | 运行中, 134/14042 steps (~1%), ETA ~20h |\\\\n| 3 | 99807 | train.py --condition clean_s8 --gpu 0 | 27,470 MiB | 运行中 (无日志) |\\\\n\\\\n### 进程状态\\\\n- **PID 97791 (GRPO)**: 存活, step 134/14042, epoch 0.0078, ~5.1s/step, reward 0.3-0.78 波动, ETA ~19h\\\\n- **PID 96745 (s6 train)**: 存活但已完成 — 3 epoch 训练结束, model saved to checkpoints/clean_s6, 仍占 GPU 1 23GB\\\\n- **PID 99214 (s7 train)**: 存活, 56/939 steps (~6%), ~2s/step\\\\n- **PID 99807 (s8 train)**: 存活, 无日志输出\\\\n- **PID 98622 (s5 eval)**: 存活但 s5 results 已存在 — zombie\\\\n- **PID 98896, 98897**: 已死亡\\\\n\\\\n### Eval 结果\\\\n| Condition | Accuracy | θ_MLE | lz* |\\\\n|-----------|----------|-------|-----|\\\\n| clean_s3 | 0.6783 | -0.1068 | 9.5293 |\\\\n| clean_s4 | 0.6786 | -0.1092 | 8.9673 |\\\\n| clean_s5 | 0.6787 | -0.0875 | 8.5322 |\\\\n| clean_s6 | — | — | — (训练刚完成, eval 未开始) |\\\\n\\\\n### HT post-RL 结果\\\\n| Stage | Accuracy | θ_MLE | lz* | acc_seen | acc_unseen | lz*_seen | lz*_unseen |\\\\n|-------|----------|-------|-----|----------|------------|----------|------------|\\\\n| SFT | 0.7339 | +0.2281 | 2.914 | 0.8310 | 0.7167 | -0.395 | 3.278 |\\\\n\\\\nbase_results.json 也存在。\\\\n\\\\n### 建议操作\\\\n1. **Kill PID 98622** — s5 eval zombie, 浪费 GPU 0 上 8.6GB\\\\n2. **Kill PID 96745** — s6 训练已完成, 浪费 GPU 1 上 23.1GB → 释放后可启动 s6 eval\\\\n3. s7 (GPU 0) 和 s8 (GPU 3) 正常运行中, 不动\\\\n4. GRPO (GPU 2) 正常运行中, 不动\\\\n5. GPU 1 清理后启动 clean_s6 eval\\\\n\\\\n## MIA 对比准备 (2026-05-21)\\\\n\\\\n**目标**：用 MIA (Min-K%/Min-K%++) 作为 baseline，与 lz* 对比在 post-RL 模型上的检测能力。Wang et al. (2025) 证明 MIA 在 post-RL 模型上失效，我们要展示 lz* 在 GRPO 后仍有效。\\\\n\\\\n**脚本就绪**：\\\\n- `/root/autodl-tmp/post_rl_contam/eval_mia.py` — MIA 评估脚本（Min-K% + Min-K%++），支持 `--stage base|sft|grpo --gpu N`\\\\n- `/root/autodl-tmp/post_rl_contam/compare_mia_lz.py` — 对比表生成（加载 MIA + lz* 结果，输出对比 AUC-ROC）\\\\n- 依赖 scikit-learn 已安装\\\\n\\\\n**算法实现**：\\\\n- Min-K%: token log-prob 最小 K% 的均值（K=10,20,30,40,50）\\\\n- Min-K%++: 标准化 log-prob (z = (log_p - μ_vocab) / σ_vocab) 最小 K% 的均值\\\\n- 同时计算 Loss baseline（平均 log-prob）\\\\n- 输出 per-item scores + AUC-ROC\\\\n\\\\n**运行方式**：`python eval_mia.py --stage base --gpu 0`（需 GPU，14042 items，预估 1-2h/stage）\\\\n\\\\n**参考文献**：\\\\n- Min-K%++: Zhang et al. (2024), ICLR 2025 Spotlight, [github.com/zjysteven/mink-plus-plus](https://github.com/zjysteven/mink-plus-plus)\\\\n- Min-K%: Shi et al. (2024) \\\\\\\"Detecting Pretraining Data from Large Language Models\\\\\\\"\\\\n\\\\n## ConStat 对比分析 (2026-05-21, updated)\\\\n\\\\n**论文**: Dekoninck et al., \\\\\\\"ConStat: Performance-Based Contamination Detection in Large Language Models\\\\\\\", NeurIPS 2024.\\\\n**代码**: [github.com/eth-sri/ConStat](https://github.com/eth-sri/ConStat), 已 clone 到 `/root/autodl-tmp/ConStat/`, pip install -e . 完成。\\\\n\\\\n### ConStat 方法核心\\\\n\\\\nConStat 是 **dual-benchmark + multi-model** 方法：通过比较 target model 在 primary benchmark vs reference benchmark 上的性能增量，判断 primary 是否被污染。核心逻辑——如果 model 在 primary 上的表现显著高于 spline(reference_perf) 的预测，则 primary 被污染。\\\\n\\\\n### 输入要求对比\\\\n\\\\n| 维度 | ConStat | lz* (ours) |\\\\n|------|---------|------------|\\\\n| Benchmarks | 2 (primary + reference) | 1 |\\\\n| Ref\\\\n\\\\n... [截断: 省略 3010 字符，传 max_chars=0 获取完整内容]\\\", \\\"total_chars\\\": 15010, \\\"truncated\\\": true}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/memory.md\", \"content\": \"# Memory — irt_personfit_contam\\n\\n## OOM 教训 (2026-05-20)\\n- 7.6GB RAM 机器上，N_SIM×n_items float64 矩阵不能一次性分配。MMLU 10K×14042×8B ≈ 1.07GB 单个矩阵，compute_lz_star 内部创建 ~7 个同尺寸中间数组 → OOM\\n- 解决方案：BATCH_SIZE=500 分批计算 + N_SIM 降至 2000（统计效力足够）\\n- generate_response 和 compute_lz_star 都需要分批\\n\\n## Worker context exhaustion 教训 (2026-05-20)\\n- exp-v1-irt-refit-expanded Worker 跑 1.5 小时后崩溃，无输出。任务是从 HuggingFace 下载 500+ 模型的 per-item 数据并拟合 IRT。\\n- **根因**: 大量 HF API 调用 + 数据处理的累积输出耗尽 Worker context window。\\n- **教训**: 涉及大规模数据下载（100+ datasets）的任务必须分批 + checkpoint 中间结果，或拆成多个 Worker 串行执行。单个 Worker 不适合做 1.5hr+ 的重型数据工程。\\n- **补充 (同日)**: ssh_read_only 读取大 JSON 文件（8MB+ 单行）也会撑爆 context。Worker 操作远程大文件必须用 python 脚本提取摘要，不要 cat/head。\\n- **补充 (同日)**: Worker 无法在进程内长时间等待（~2 min 就退出）。涉及 GPU 训练 + eval 的任务应分阶段处理：训练完成后由 cron 回调触发 eval Worker，或由主 Agent 定时派 Worker 检查。\\n\\n## sim_001 关键发现 (2026-05-20)\\n- **Null check 全通过**：PSN-IRT 神经网络估计的 4PL 参数与经典 IRT 兼容，lz* ≈ N(0,1)\\n  - 大 benchmark（GSM8K/HellaSwag/MMLU）KS p 全部 > 0.01\\n  - 小 benchmark（HumanEval/ARC-C）KS p < 0.01，但属预期（items 太少，CLT 近似弱）\\n- **检测力与 n_items 强正相关**：MMLU(14042)=97.9% >> HellaSwag(10042)=73.3% >> GSM8K(1319)=57.8% >> ARC-C(295)=12.9%\\n- **Inverted-U 所有 benchmark 可观测**：power 在 25-50% contamination 达峰，100% 全部 NaN（全答对 → MLE 不收敛）\\n\\n## PSN-IRT 12 模型身份 (2026-05-20)\\n\\n**来源**：arXiv:2505.15055 (AAAI 2026 Oral)，GitHub repo `Joe-Hall-Lee/PSN-IRT`\\n\\n| student_id | θ | 正确率 | 模型名称 | 类型 |\\n|---|---|---|---|---|\\n| 0 | 1.46 | 80.6% | 360GPT2-Pro | API |\\n| 1 | 3.77 | 85.7% | DeepSeek-V3 | API |\\n| 2 | 1.14 | 78.9% | Doubao-pro | API |\\n| 3 | 0.78 | 84.5% | Gemini-1.5 | API |\\n| 4 | -3.38 | 23.1% | Gemma-2B-it | 开源 2B |\\n| 5 | 1.73 | 82.1% | Hunyuan-Turbo | API |\\n| 6 | -1.37 | 40.0% | Mistral-7B-Instruct-v0.1 | 开源 7B |\\n| 7 | 0.93 | 77.0% | Moonshot-v1 | API |\\n| 8 | 0.96 | 76.3% | Qwen-Plus | API |\\n| 9 | -0.13 | 60.4% | Qwen2.5-3B-Instruct | 开源 3B |\\n| 10 | -1.89 | 31.6% | Vicuna-7B-v1.3 | 开源 7B |\\n| 11 | 0.77 | 75.2% | Yi-Lightning | API |\\n\\n## Gemini-1.5 × 100% contamination 精确匹配 (2026-05-20)\\n\\nGemini-1.5 MMLU lz*(benchmark-specific θ) = +31.815 = 100% contamination simulation lz* = +31.815（完全一致）。机制：100% accuracy → θ_bench=4.0 → lz* deterministic。其他 benchmark Gemini-1.5 lz* 为负（非 100% acc），说明异常是 benchmark-specific 的。\\n\\n## exp-extended-sim 关键发现 (2026-05-20)\\n\\n- Dual-regime crossover 75-90%：所有 5 benchmark 在此区间 lz* 从负翻正\\n- 100% contamination lz* deterministic (std=0.0)\\n- Inverted-U 全 5 benchmark 确认\\n\\n## exp-two-sided 关键教训 (2026-05-20)\\n\\n95% flagging 即使用 benchmark-specific θ + bootstrap + FDR 也无法降低。LLM 系统性违反 4PL 假设（单维+局部独立）。绝对阈值对 real data 无意义，需 controlled calibration (Δlz*)。\\n\\n## exp-empirical-null 关键发现 (2026-05-20)\\n\\nBootstrap null 校准良好（mean bias=0.09, std=1.002）。95% flagging 不是 null miscalibration，而是 LLM response pattern 产生极端 lz*。大 benchmark KS reject 仅 8.3%，小 benchmark 58-75%（有限样本效应）。\\n\\n## exp-power-theory 关键发现 (2026-05-20)\\n\\nR²(two-sided)=0.957, R²(left-tail)=0.976, R²(mean lz*)=0.995。δ ∝ √n confirmed。Inverted-U 拐点理论值 π*≈81-85%。最小 n_items (80% power): 15% contam→~8K, 25%→~3K, 50%→~1K。\\n\\n## exp-item-alignment-check 关键发现 (2026-05-20)\\n\\n**PSN-IRT 与 v1 Leaderboard item ordering 不对齐。** 直接位置匹配率 54.56%（≈随机）。Content-based 重排后 Mistral 88.46%, Vicuna 72.48%。\\n\\n**根因**: PSN-IRT 保持 raw MMLU 原始顺序，v1 leaderboard 在 subject 内部 shuffle。且 PSN-IRT 是独立评测（不同 prompt/few-shot），即使对齐后仍有 ~12% response 差异。\\n\\n**结论**: **不可混用 v1 responses + PSN-IRT parameters**。~12% 噪声对 item-level person-fit 统计量影响严重。\\n\\n**已生成 item_mapping.csv**: 12068/14042 items 的 v1→PSN-IRT 位置映射，可用于未来 content-based 对齐需求。\\n\\n## Open LLM Leaderboard v1 per-item data (2026-05-20)\\n\\n**来源**: `open-llm-leaderboard-old/details_{org}__{model}` HuggingFace datasets\\n**格式**: Parquet, `acc`/`acc_norm` 二值字段\\n**覆盖**: MMLU ✅, HellaSwag ✅, ARC-C ✅, GSM8K ✅ | HumanEval ❌\\n**模型数**: 13,000+\\n**⚠️ 不可直接用 PSN-IRT parameters** — 见 item-alignment-check 发现\\n\\n## exp-fdr-correction 关键发现 (2026-05-20)\\n\\nexp-two-sided v2 的 `empirical_pvalues.csv` 已包含 global BH-FDR 校正（60 cells 一起做 BH）。校正前后 flagging 均为 57/60 (95%)——因大多数 cells empirical p=0.000，BH 校正无实质影响。Leaderboard-scale FDR (24800+ tests) 需在 leaderboard audit 中单独处理。\\n\\n## exp-clean-control-delta 关键发现 (2026-05-20)\\n\\nClean-vs-clean Δlz* 均值全部接近 0（|mean| < 0.13），无一显著，确认 estimation noise floor ~ N(0, 1.4)。\\nClean-vs-contaminated (25%) Δlz* 均高度显著（p<1e-10），Cohen's d: MMLU=2.66, HellaSwag=1.85, GSM8K=1.85, HumanEval=1.07, ARC-C=0.45。\\nARC-C d=0.45 略低 0.5 阈值（仅 295 items），与 power theory 一致。\\n论文中标注为 \\\"theoretical noise floor\\\"，真实 SFT clean-vs-clean 在 ctrl-contam-pilot 中实现。\\n\\n## exp-ml-classifier-baseline 关键发现 (2026-05-20)\\n\\n**lz* 在低污染率 (5-10%) 优于有监督 ML 分类器**：5% contam lz* AUROC 0.675 vs best ML 0.575 (+0.10); 10% contam 0.763 vs 0.712 (+0.05)。ML 仅在 25%+ 污染时略胜 (+0.05)，但需 oracle contamination labels（实际不可用）。\\nRF feature importance 在 items 间高度弥散（top item <1%），与 lz* 全局 likelihood 方法一致。\\n论文限定为 simulation 场景下的对比，不推广为\\\"所有 binary-only ML 方法都不如 IRT\\\"。\\n\\n## exp-domain-analysis 关键发现 (2026-05-20)\\n\\n**Gemini-1.5 MMLU 100% accuracy 覆盖全部 57 个 subject**——不是 domain-concentrated 泄漏，是完全数据集泄漏。50/57 subjects flagged (lz*>1.96)，未 flagged 的 7 个 subject 的 lz* 也很高但 item 数太少。\\n\\n**模型 contamination 指纹多样**：\\n- Doubao-pro: 反向 pattern，Humanities/Social Sciences lz* 极负（-13~-15），STEM 接近 0，Other 正向——可能是训练数据偏科\\n- Hunyuan-Turbo: STEM lz*=1.8 vs Social Sciences lz*=13.9——Social Sciences 方向过度拟合\\n- Yi-Lightning 和 Qwen-Plus: 全 domain 高 lz*（16~28），领先所有其他模型\\n\\n**论文价值**: domain decomposition 为 12-model case study 增加定性分析深度，但 non-essential（P2 级别）。\\n\\n**virology lz*=-8.21 诊断**：双重根因——(1) global θ=0.78 vs MMLU θ_MLE=4.0 错配；(2) virology 全部 166 items d<1.0 (mean=0.71)，即使 θ=4.0 仍有 58/166 items P<0.5。是 PSN-IRT calibration artifact，不影响 overall lz*=34.75。per-subject 分析需加 caveat。\\n\\n## exp-natural-experiment 关键发现 (2026-05-20)\\n\\n21 对 base→chat 模型 × 4 benchmarks（MMLU/HellaSwag/ARC-C/GSM8K）。\\n\\n**两个 benchmark 有显著系统性 SFT 效应**：\\n- HellaSwag: Δlz* 偏差 mean=-3.40, t=-3.97, p=0.001（SFT 系统性降低 person-fit）\\n- GSM8K: Δlz* 偏差 mean=+3.92, t=3.35, p=0.009（SFT 系统性提高 person-fit）\\n- MMLU/ARC-C 无显著效应\\n\\n**无个体 pair outlier**——未能检测到单个模型的 benchmark-specific contamination。\\n**Director 评估价值极低（P2-optional）**，不作为核心 evidence 使用。\\n\\n## exp-4pl-ablation 关键发现 (2026-05-20)\\n\\n**4PL d 参数对检测力的影响是决定性的，不是锦上添花。**\\n\\n核心数据（4PL vs 3PL(d=1)，平均 power gain across contamination levels）：\\n- MMLU: +27.3pp (max +49.0pp)\\n- HellaSwag: +26.1pp (max +59.6pp)\\n- GSM8K: +20.3pp (max +39.7pp)\\n- ARC_C: +14.8pp (max +54.6pp)\\n- HumanEval: +13.7pp (max +30.6pp)\\n\\nFAR 校准：4PL ≈ 5%（正确），3PL 4.7-16.5%（偏高），2PL 50-100%（完全不可用——固定 c=0.25 灾难性错误）。\\n\\n**d-bucket 机制确认**：d<0.8 的 items 上 4PL 优势最大（MMLU +61pp），d≥0.95 时差异可忽略。这证实 d 参数捕捉 ceiling effect 是检测力提升的关键来源。\\n\\n**论文价值**：回应 Reviewer R8 concern（为什么用 4PL 而非 3PL）。46% MMLU items d<0.95，忽略 d 约将检测力减半。这是 Method 部分的核心 justification。\\n\\n## exp-4pl-real-data-degradation 关键发现 (2026-05-20)\\n\\n**实数据验证：d 参数的影响对高能力模型是毁灭性的。**\\n\\n在 12 个 PSN-IRT 模型的真实响应数据上，4PL vs 3PL(d=1) 的 lz* 仅有 r=0.225, RMSE=68.41——几乎无关联。\\n\\n**不对称影响机制**：d=1 使 P(θ)→1（高能力模型预期全部答对），导致少量错误被 lz* 放大为极端异常值。低能力模型的 P(θ) 本身就远离 1.0，d=1 vs d<1 差异小，因此几乎不受影响。\\n\\n- DeepSeek-V3 (θ=3.77): MMLU lz* 从 +16.4 暴跌至 -340.6\\n- Gemma-2B-it / Vicuna / Mistral (低 θ): |Δlz*|<2\\n- MMLU 最严重（46% items d<0.95），mean |Δlz*|=58.3\\n\\n**与 exp-4pl-ablation 的互补**：ablation 在模拟数据上证明 power 损失，本实验在实数据上证明 lz* 值本身被完全摧毁。二者形成 R8 的双重证据链——4PL d 参数不可或缺。\\n\\n**论文写作注意**：这个结果特别适合做 case study 可视化（选 DeepSeek-V3 on MMLU 作为 extreme case），放在 ablation study 或 appendix 中。\\n\\n## exp-ctrl-contam-pilot 关键发现 (2026-05-20)\\n\\n**首次真实 LLM controlled contamination 实验。** Qwen2.5-7B-Instruct QLoRA SFT，4+1 条件。\\n\\n**核心结果（n=3 clean seeds, ddof=1）**：\\n| Condition | Accuracy | θ_MLE | lz* |\\n|-----------|----------|-------|-----|\\n| clean_s1 (seed=42) | 0.6787 | -0.0987 | 8.0101 |\\n| clean_s2 (seed=123) | 0.6789 | -0.0842 | 5.9440 |\\n| clean_s3 (seed=456) | 0.6783 | -0.1068 | 8.0806 |\\n| contam_15 | 0.7310 | +0.1971 | 3.0046 |\\n| contam_50 | 0.7644 | +0.3703 | 5.4480 |\\n\\n**Baseline（n=3）**: mean=7.3449, std=1.2137\\n**Cohen's d（n=3, ddof=1）**: contam_15 d=-3.58, contam_50 d=-1.56\\n**注意**：之前汇报的 d=-3.85 / d=-1.48 使用了 ddof=0。论文统一用 ddof=1。\\n\\n**H1 ✓ H2 ✓ H3 ✗(θ-free) H4 ✗**\\n\\n**θ-shift 是 dose-response 倒置的确切原因**：\\n- contamination 抬高 θ_MLE（clean -0.09 → contam_50 +0.37），MLE 将 contamination 信号解释为 \\\"能力提升\\\"\\n- θ-fixed（固定为 clean θ 均值 -0.0914）下，dose-response 恢复单调：\\n  - |Δlz*_fixed_15| = 2.96, |Δlz*_fixed_50| = 8.67, ratio = 2.93 ✅\\n- θ-shift 分别吸收了 contam_15 的 6.93 和 contam_50 的 10.20 lz* 单位信号\\n\\n**clean seed 变异性**：s1 和 s3 的 lz* 接近（8.01, 8.08），s2 明显低（5.94）。n=3 baseline std=1.21 vs n=2 的 1.46，加入 s3 压缩了方差，使 Cohen's d 更极端。\\n\\n**Memorization fraction 低于预期**（0.38/0.29 vs 假设的 >0.5）——QLoRA 3 epochs 不足以产生强 memorization，但足以产生可检测的 lz* 偏移。\\n\\n**论文叙事价值**：\\n1. θ-shift = \\\"ability inflation\\\" 是 contamination 逃避 person-fit 检测的核心机制\\n2. 与 simulation inverted-U 发现形成呼应——real-world 版本的同一现象\\n3. θ-fixed 分析作为 supplementary evidence 证明底层信号单调递增\\n4. 支撑 Discussion 中 \\\"θ estimation as confound\\\" 段落\\n\\n## GPU 审计 (2026-05-21 15:47 UTC)\\n\\n### GPU 占用总览\\n| GPU | PID | Process | VRAM | Status |\\n|-----|------|---------|------|--------|\\n| 0 | 98622 | eval_lz.py --condition clean_s5 --gpu 0 | 8,628 MiB | **ZOMBIE** — s5 results 已存在 |\\n| 0 | 99214 | train.py --condition clean_s7 --gpu 3 | 37,694 MiB | 运行中, 56/939 steps (~6%) |\\n| 1 | 96745 | train.py --condition clean_s6 --gpu 0 | 23,102 MiB | **ZOMBIE** — 训练已完成，模型已保存 |\\n| 2 | 97791 | train_grpo.py | 8,062 MiB | 运行中, 134/14042 steps (~1%), ETA ~20h |\\n| 3 | 99807 | train.py --condition clean_s8 --gpu 0 | 27,470 MiB | 运行中 (无日志) |\\n\\n### 进程状态\\n- **PID 97791 (GRPO)**: 存活, step 134/14042, epoch 0.0078, ~5.1s/step, reward 0.3-0.78 波动, ETA ~19h\\n- **PID 96745 (s6 train)**: 存活但已完成 — 3 epoch 训练结束, model saved to checkpoints/clean_s6, 仍占 GPU 1 23GB\\n- **PID 99214 (s7 train)**: 存活, 56/939 steps (~6%), ~2s/step\\n- **PID 99807 (s8 train)**: 存活, 无日志输出\\n- **PID 98622 (s5 eval)**: 存活但 s5 results 已存在 — zombie\\n- **PID 98896, 98897**: 已死亡\\n\\n### Eval 结果\\n| Condition | Accuracy | θ_MLE | lz* |\\n|-----------|----------|-------|-----|\\n| clean_s3 | 0.6783 | -0.1068 | 9.5293 |\\n| clean_s4 | 0.6786 | -0.1092 | 8.9673 |\\n| clean_s5 | 0.6787 | -0.0875 | 8.5322 |\\n| clean_s6 | — | — | — (训练刚完成, eval 未开始) |\\n\\n### HT post-RL 结果\\n| Stage | Accuracy | θ_MLE | lz* | acc_seen | acc_unseen | lz*_seen | lz*_unseen |\\n|-------|----------|-------|-----|----------|------------|----------|------------|\\n| SFT | 0.7339 | +0.2281 | 2.914 | 0.8310 | 0.7167 | -0.395 | 3.278 |\\n\\nbase_results.json 也存在。\\n\\n### 建议操作\\n1. **Kill PID 98622** — s5 eval zombie, 浪费 GPU 0 上 8.6GB\\n2. **Kill PID 96745** — s6 训练已完成, 浪费 GPU 1 上 23.1GB → 释放后可启动 s6 eval\\n3. s7 (GPU 0) 和 s8 (GPU 3) 正常运行中, 不动\\n4. GRPO (GPU 2) 正常运行中, 不动\\n5. GPU 1 清理后启动 clean_s6 eval\\n\\n## MIA 对比准备 (2026-05-21)\\n\\n**目标**：用 MIA (Min-K%/Min-K%++) 作为 baseline，与 lz* 对比在 post-RL 模型上的检测能力。Wang et al. (2025) 证明 MIA 在 post-RL 模型上失效，我们要展示 lz* 在 GRPO 后仍有效。\\n\\n**脚本就绪**：\\n- `/root/autodl-tmp/post_rl_contam/eval_mia.py` — MIA 评估脚本（Min-K% + Min-K%++），支持 `--stage base|sft|grpo --gpu N`\\n- `/root/autodl-tmp/post_rl_contam/compare_mia_lz.py` — 对比表生成（加载 MIA + lz* 结果，输出对比 AUC-ROC）\\n- 依赖 scikit-learn 已安装\\n\\n**算法实现**：\\n- Min-K%: token log-prob 最小 K% 的均值（K=10,20,30,40,50）\\n- Min-K%++: 标准化 log-prob (z = (log_p - μ_vocab) / σ_vocab) 最小 K% 的均值\\n- 同时计算 Loss baseline（平均 log-prob）\\n- 输出 per-item scores + AUC-ROC\\n\\n**运行方式**：`python eval_mia.py --stage base --gpu 0`（需 GPU，14042 items，预估 1-2h/stage）\\n\\n**参考文献**：\\n- Min-K%++: Zhang et al. (2024), ICLR 2025 Spotlight, [github.com/zjysteven/mink-plus-plus](https://github.com/zjysteven/mink-plus-plus)\\n- Min-K%: Shi et al. (2024) \\\"Detecting Pretraining Data from Large Language Models\\\"\\n\\n## ConStat 对比分析 (2026-05-21, updated)\\n\\n**论文**: Dekoninck et al., \\\"ConStat: Performance-Based Contamination Detection in Large Language Models\\\", NeurIPS 2024.\\n**代码**: [github.com/eth-sri/ConStat](https://github.com/eth-sri/ConStat), 已 clone 到 `/root/autodl-tmp/ConStat/`, pip install -e . 完成。\\n\\n### ConStat 方法核心\\n\\nConStat 是 **dual-benchmark + multi-model** 方法：通过比较 target model 在 primary benchmark vs reference benchmark 上的性能增量，判断 primary 是否被污染。核心逻辑——如果 model 在 primary 上的表现显著高于 spline(reference_perf) 的预测，则 primary 被污染。\\n\\n### 输入要求对比\\n\\n| 维度 | ConStat | lz* (ours) |\\n|------|---------|------------|\\n| Benchmarks | 2 (primary + reference) | 1 |\\n| Ref\\n\\n... [截断: 省略 3010 字符，传 max_chars=0 获取完整内容]\", \"total_chars\": 15010, \"truncated\": true}, \"error\": null, \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "095ce946-209e-4bf9-adba-26c9987fa48b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/.claude/sessions/agent_272f846c",
  "sessionId": "465c36a7-990a-4437-ba2f-9fd3ebf0f8ef",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 30_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[HANDOFF] 你是 Main Agent，这是 Loop #2。  ## 上一轮交接 (task_context)  ### 1. 🔴 硬约束 / 红线 - GPU 白名单: westd-35694 的 cuda:0/1/2/3，不可用其他设备 - Llama 模型路径来自 ModelScope (`LLM-Research/Meta-Llama-3.1-8B-Instruct`)，不是…",
  "leafUuid": "fb38ef3c-1262-4a3e-a872-1d65aac13f39",
  "sessionId": "465c36a7-990a-4437-ba2f-9fd3ebf0f8ef"
}
```

---

### Runtime record

_source line 31_

```json
{
  "type": "ai-title",
  "aiTitle": "Confirm Llama clean status and analyze contam results",
  "sessionId": "465c36a7-990a-4437-ba2f-9fd3ebf0f8ef"
}
```

---

### Assistant

_source line 32 · 2026-05-21T13:08:34.378Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze the current state:

1. **Registry**: No RUNNING experiments. Many PREPARING experiments that may have actual processes running on the GPU.
2. **GPU audit from memory.md** (timestamped 15:47 UTC on 2026-05-21): Shows processes running but some are zombies
3. **Key completed experiments**: Llama contam15/contam50 done, Mistral done, many clean seeds done
4. **Still PREPARING**: Llama clean s8-s10, GRPO v3, ARC-C experiments, MIA comparison, Qwen s10


5. **Next steps**: I need to check the current GPU status on westd-35694 to see what's actually running versus zombie processes, verify the GPU whitelist in the project config, and check if any workers are still active.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fb38ef3c-1262-4a3e-a872-1d65aac13f39",
  "isSidechain": false,
  "requestId": "req_011CbFmR2U96Q2k2zvq4gDed",
  "type": "assistant",
  "uuid": "39b8de67-e475-4d19-9c06-f955751b6f36",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/.claude/sessions/agent_272f846c",
  "sessionId": "465c36a7-990a-4437-ba2f-9fd3ebf0f8ef",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0166RfKQrR2FaPGxC3kmwnUw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13692,
      "cache_read_input_tokens": 63366,
      "output_tokens": 483,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13692,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 483,
          "cache_read_input_tokens": 63366,
          "cache_creation_input_tokens": 13692,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13692
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

_source line 33 · 2026-05-21T13:08:34.387Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__list_workers · `toolu_01Rez8qqY9dX1uZ56Qfgi5Hz`</summary>

```json
{
  "project": "irt_personfit_contam",
  "status": "running",
  "limit": 10
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "39b8de67-e475-4d19-9c06-f955751b6f36",
  "isSidechain": false,
  "requestId": "req_011CbFmR2U96Q2k2zvq4gDed",
  "type": "assistant",
  "uuid": "4836ff6f-7620-4bc8-be71-e50e4ee61bfd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/.claude/sessions/agent_272f846c",
  "sessionId": "465c36a7-990a-4437-ba2f-9fd3ebf0f8ef",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0166RfKQrR2FaPGxC3kmwnUw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13692,
      "cache_read_input_tokens": 63366,
      "output_tokens": 483,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13692,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 483,
          "cache_read_input_tokens": 63366,
          "cache_creation_input_tokens": 13692,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13692
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

_source line 34 · 2026-05-21T13:08:34.413Z_

<details><summary>↩ Tool result · `toolu_01Rez8qqY9dX1uZ56Qfgi5Hz`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"workers\": [{\"worker_id\": \"worker_code_19912-arcc-eval-then-llama_20260521T124530\", \"task_type\": \"code:19912-arcc-eval-then-llama\", \"project\": \"irt_personfit_contam\", \"status\": \"running\", \"started_at\": \"2026-05-21T12:45:30.527515+00:00\", \"ended_at\": null}, {\"worker_id\": \"worker_code_check-19912-fill_20260521T130313\", \"task_type\": \"code:check-19912-fill\", \"project\": \"irt_personfit_contam\", \"status\": \"running\", \"started_at\": \"2026-05-21T13:03:14.083851+00:00\", \"ended_at\": null}], \"count\": 2}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4836ff6f-7620-4bc8-be71-e50e4ee61bfd",
  "isSidechain": false,
  "promptId": "26661264-62cc-4d8c-933c-ac64167cc12e",
  "type": "user",
  "uuid": "82ecadb2-6a83-4eb2-936e-307217e3868b",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"workers\\\": [{\\\"worker_id\\\": \\\"worker_code_19912-arcc-eval-then-llama_20260521T124530\\\", \\\"task_type\\\": \\\"code:19912-arcc-eval-then-llama\\\", \\\"project\\\": \\\"irt_personfit_contam\\\", \\\"status\\\": \\\"running\\\", \\\"started_at\\\": \\\"2026-05-21T12:45:30.527515+00:00\\\", \\\"ended_at\\\": null}, {\\\"worker_id\\\": \\\"worker_code_check-19912-fill_20260521T130313\\\", \\\"task_type\\\": \\\"code:check-19912-fill\\\", \\\"project\\\": \\\"irt_personfit_contam\\\", \\\"status\\\": \\\"running\\\", \\\"started_at\\\": \\\"2026-05-21T13:03:14.083851+00:00\\\", \\\"ended_at\\\": null}], \\\"count\\\": 2}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"workers\": [{\"worker_id\": \"worker_code_19912-arcc-eval-then-llama_20260521T124530\", \"task_type\": \"code:19912-arcc-eval-then-llama\", \"project\": \"irt_personfit_contam\", \"status\": \"running\", \"started_at\": \"2026-05-21T12:45:30.527515+00:00\", \"ended_at\": null}, {\"worker_id\": \"worker_code_check-19912-fill_20260521T130313\", \"task_type\": \"code:check-19912-fill\", \"project\": \"irt_personfit_contam\", \"status\": \"running\", \"started_at\": \"2026-05-21T13:03:14.083851+00:00\", \"ended_at\": null}], \"count\": 2}, \"error\": null, \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "4836ff6f-7620-4bc8-be71-e50e4ee61bfd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/.claude/sessions/agent_272f846c",
  "sessionId": "465c36a7-990a-4437-ba2f-9fd3ebf0f8ef",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-21T13:08:34.547Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__load_project_config · `toolu_019vHtgk8hSSnwJ8Jd1HEYHD`</summary>

```json
{
  "project_name": "irt_personfit_contam",
  "section": "execution"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "82ecadb2-6a83-4eb2-936e-307217e3868b",
  "isSidechain": false,
  "requestId": "req_011CbFmR2U96Q2k2zvq4gDed",
  "type": "assistant",
  "uuid": "5647e26c-dc68-49cc-82a1-f79be31e3c86",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/.claude/sessions/agent_272f846c",
  "sessionId": "465c36a7-990a-4437-ba2f-9fd3ebf0f8ef",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0166RfKQrR2FaPGxC3kmwnUw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13692,
      "cache_read_input_tokens": 63366,
      "output_tokens": 483,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13692,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 483,
          "cache_read_input_tokens": 63366,
          "cache_creation_input_tokens": 13692,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13692
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

_source line 36 · 2026-05-21T13:08:34.557Z_

<details><summary>↩ Tool result · `toolu_019vHtgk8hSSnwJ8Jd1HEYHD`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"project\": \"irt_personfit_contam\", \"section\": \"execution\", \"config\": {\"execution\": {\"gpu_ids\": [\"cuda:0\", \"cuda:1\", \"cuda:2\", \"cuda:3\"], \"servers\": [{\"account\": \"root\", \"server\": \"westd-35694\"}, {\"account\": \"root\", \"server\": \"westd-19912\"}]}}}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5647e26c-dc68-49cc-82a1-f79be31e3c86",
  "isSidechain": false,
  "promptId": "26661264-62cc-4d8c-933c-ac64167cc12e",
  "type": "user",
  "uuid": "008e08ab-036b-4a66-9fcd-00155d7d7f01",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"project\\\": \\\"irt_personfit_contam\\\", \\\"section\\\": \\\"execution\\\", \\\"config\\\": {\\\"execution\\\": {\\\"gpu_ids\\\": [\\\"cuda:0\\\", \\\"cuda:1\\\", \\\"cuda:2\\\", \\\"cuda:3\\\"], \\\"servers\\\": [{\\\"account\\\": \\\"root\\\", \\\"server\\\": \\\"westd-35694\\\"}, {\\\"account\\\": \\\"root\\\", \\\"server\\\": \\\"westd-19912\\\"}]}}}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"project\": \"irt_personfit_contam\", \"section\": \"execution\", \"config\": {\"execution\": {\"gpu_ids\": [\"cuda:0\", \"cuda:1\", \"cuda:2\", \"cuda:3\"], \"servers\": [{\"account\": \"root\", \"server\": \"westd-35694\"}, {\"account\": \"root\", \"server\": \"westd-19912\"}]}}}, \"error\": null, \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "5647e26c-dc68-49cc-82a1-f79be31e3c86",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/.claude/sessions/agent_272f846c",
  "sessionId": "465c36a7-990a-4437-ba2f-9fd3ebf0f8ef",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 37 · 2026-05-21T13:08:34.630Z_

```json
{
  "parentUuid": "008e08ab-036b-4a66-9fcd-00155d7d7f01",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "1cb9cc5b-2d1c-49bb-80ff-e57f1c1c8237",
  "timestamp": "2026-05-21T13:08:34.630Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/.claude/sessions/agent_272f846c",
  "sessionId": "465c36a7-990a-4437-ba2f-9fd3ebf0f8ef",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 38 · 2026-05-21T13:09:32.881Z_

<details><summary>Logged reasoning block</summary>

```text
Important findings:

1. **GPU allocation**: Both westd-35694 AND westd-19912 are in the project config. The handoff's "GPU whitelist: westd-35694 cuda:0/1/2/3" was wrong or outdated — both servers are authorized.

2. **Running workers**: Two workers still running:
   - `worker_code_19912-arcc-eval-then-llama_20260521T124530` — started 12:45 UTC (about 17+ minutes ago based on current time)
   - `worker_code_check-19912-fill_20260521T130313` — started 13:03 UTC (about 1-2 minutes ago)

Both are working on westd-19912 tasks (ARC-C eval and Llama experiments), likely doing SSH work on that server.

3. **Servers**: westd-35694 and westd-19912 both allocated.

I should check westd-35694's GPU status to see what's actually running there, but I'll hold off interfering with the workers since they're already in progress and will callback when done.

I need a fresh GPU status check on westd-35694 since the audit from memory.md is outdated. Let me spawn a worker to SSH in and see what's currently running, then assess which experiments need attention. Several tasks are stuck in PREPARING state — the Llama clean s8-s10 and GRPO v3 might be training on one of the servers, while Qwen s10 already has metrics but may just need a status update to DONE. The ARC-C experiments are actively running with the worker on westd-19912.

Looking at the Qwen clean s10 experiment, it has valid eval metrics (accuracy=0.676, lz_star=8.149, theta_mle=-0.116, n_items=14042), so I should mark it as DONE. I'm also noticing what looks like duplicate ARC-C entries — some prefixed with "exp-" that are already DONE with metrics, and others without the prefix that are still PREPARING. I need to clarify whether these are actually separate experiments or if there's been some naming inconsistency.

I'm also spotting a few other experiments with metrics that are stuck in PREPARING status: exp-ctrl-contam-qwen-clean-s10, exp-arcc-clean-s1, and exp-arcc-benchmark. These should probably be updated to DONE unless there's a specific reason they're being held back, like waiting for additional conditions to complete.

The arcc-clean-s7 through s10 entries without the exp- prefix look like stale duplicates since the properly named exp-arcc-clean-s7 through s10 are already marked DONE. I should focus on updating the ones with complete metrics first, then clean up any obvious duplicates.

Looking at the entries with full eval results, I notice they're stuck in PREPARING status even though they have valid metrics. The issue is that transitioning to DONE requires both checkpoint_path and log_path to be set, which I don't see in the current registry entries. I need to check whether those paths were actually recorded during the experiment runs before I can mark them as complete.

Let me spawn a Worker to SSH into the GPU node and check the current state—what's running on the GPUs, whether GRPO is still active, if any of the training jobs are still in progress, and whether there are any zombie processes I need to clean up. In parallel, I'll attempt to update the registry for the experiments that clearly finished but are stuck in PREPARING, and see if the checkpoint and log paths are actually stored but just not visible in the summary view. I'm calculating Cohen's d values to compare the clean Llama baseline against contamination conditions — with seven seeds, the effect sizes are strong but slightly different from the three-seed estimates, so getting s8-s10 will help refine these numbers further. Let me stop the math and focus on actually checking the GPU status.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1cb9cc5b-2d1c-49bb-80ff-e57f1c1c8237",
  "isSidechain": false,
  "requestId": "req_011CbFmS7YmNS6QNcALvQNLk",
  "type": "assistant",
  "uuid": "b4677a17-d4e2-44e8-bd39-51d531526430",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/.claude/sessions/agent_272f846c",
  "sessionId": "465c36a7-990a-4437-ba2f-9fd3ebf0f8ef",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Tt3K44bQJvydq44wMNSVfH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1068,
      "cache_read_input_tokens": 77058,
      "output_tokens": 4008,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1068,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4008,
          "cache_read_input_tokens": 77058,
          "cache_creation_input_tokens": 1068,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1068
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

_source line 39 · 2026-05-21T13:09:32.912Z_

两个 Worker 仍在运行（westd-19912 的 ARC-C eval 和 Llama 任务）。项目配置确认两台服务器都在白名单内（westd-35694 + westd-19912）。

现在 spawn Worker 检查 westd-35694 当前 GPU 状态和进程，同时更新明显已完成但卡在 PREPARING 的实验。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b4677a17-d4e2-44e8-bd39-51d531526430",
  "isSidechain": false,
  "requestId": "req_011CbFmS7YmNS6QNcALvQNLk",
  "type": "assistant",
  "uuid": "87368d4e-6d48-43ed-8792-16b2ba667912",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/.claude/sessions/agent_272f846c",
  "sessionId": "465c36a7-990a-4437-ba2f-9fd3ebf0f8ef",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Tt3K44bQJvydq44wMNSVfH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1068,
      "cache_read_input_tokens": 77058,
      "output_tokens": 4008,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1068,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4008,
          "cache_read_input_tokens": 77058,
          "cache_creation_input_tokens": 1068,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1068
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

_source line 40 · 2026-05-21T13:09:53.809Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__spawn_worker · `toolu_016u3mNhWnEQFbSm7M38D6Ry`</summary>

````json
{
  "task_type": "ssh:gpu-audit-35694",
  "project": "irt_personfit_contam",
  "task_prompt": "## 任务：westd-35694 GPU 状态审计\n\nSSH 到 westd-35694 (account: root)，执行以下检查：\n\n### 1. GPU 占用\n```bash\nnvidia-smi --query-gpu=index,memory.used,memory.total,utilization.gpu --format=csv,noheader\nnvidia-smi --query-compute-apps=pid,gpu_uuid,used_memory,name --format=csv,noheader\n```\n\n### 2. 关键进程状态\n检查以下进程是否存活：\n- GRPO (train_grpo.py) — 上次在 GPU 2, PID 97791\n- Llama clean s8 train — 上次在 GPU 3, PID 99807\n- Llama clean s7 train — 上次在 GPU 0, PID 99214（可能已完成）\n- s5 eval zombie — PID 98622\n- s6 train zombie — PID 96745\n\n对每个存活进程：\n```bash\nps -p &lt;PID> -o pid=,cmd= 2>/dev/null && echo \"ALIVE\" || echo \"DEAD\"\n```\n\n### 3. GRPO 进度\n如果 GRPO 仍在运行：\n```bash\n# 检查 GRPO log\nls -la /root/autodl-tmp/post_rl_contam/logs/\ntail -20 /root/autodl-tmp/post_rl_contam/logs/grpo_*.log 2>/dev/null || tail -20 /root/runs/irt_personfit_contam/*/output.log 2>/dev/null | grep -i \"step\\|loss\\|reward\"\n```\n\n### 4. Llama clean 训练状态\n```bash\n# 检查 s7, s8, s9, s10 的训练日志和 checkpoint\nls /root/autodl-tmp/ctrl_contam_llama/checkpoints/clean_s*/\nls /root/autodl-tmp/ctrl_contam_llama/logs/clean_s*.log 2>/dev/null\nfor s in s7 s8 s9 s10; do\n  echo \"=== $s ===\"\n  if [ -f \"/root/autodl-tmp/ctrl_contam_llama/logs/clean_${s}.log\" ]; then\n    tail -5 /root/autodl-tmp/ctrl_contam_llama/logs/clean_${s}.log\n  fi\n  ls /root/autodl-tmp/ctrl_contam_llama/checkpoints/clean_${s}/ 2>/dev/null | head -3\ndone\n```\n\n### 5. Eval 结果检查\n```bash\n# 检查哪些 clean seeds 已有 eval 结果\nls /root/autodl-tmp/ctrl_contam_llama/results/clean_s*_results.json 2>/dev/null\nfor f in /root/autodl-tmp/ctrl_contam_llama/results/clean_s*_results.json; do\n  echo \"=== $(basename $f) ===\"\n  python3 -c \"import json; d=json.load(open('$f')); print(f'acc={d.get(\\\"accuracy_overall\\\",\\\"?\\\")}, lz*={d.get(\\\"lz_star\\\",\\\"?\\\")}, theta={d.get(\\\"theta_mle\\\",\\\"?\\\")}')\" 2>/dev/null\ndone\n```\n\n### 6. Qwen s10 状态\n```bash\n# 检查 Qwen clean s10 训练和 eval\nls /root/autodl-tmp/ctrl_contam_pilot/checkpoints/clean_s10/ 2>/dev/null | head -3\nls /root/autodl-tmp/ctrl_contam_pilot/results/clean_s10_results.json 2>/dev/null\nif [ -f \"/root/autodl-tmp/ctrl_contam_pilot/results/clean_s10_results.json\" ]; then\n  python3 -c \"import json; d=json.load(open('/root/autodl-tmp/ctrl_contam_pilot/results/clean_s10_results.json')); print(f'acc={d.get(\\\"accuracy\\\",d.get(\\\"accuracy_overall\\\",\\\"?\\\"))}, lz*={d.get(\\\"lz_star\\\",\\\"?\\\")}, theta={d.get(\\\"theta_mle\\\",\\\"?\\\")}')\"\nfi\n```\n\n### 7. 磁盘\n```bash\ndf -h / /root/autodl-tmp 2>/dev/null | tail -2\n```\n\n**产出要求**：\n1. 每个 GPU 当前占用情况表（GPU ID, PID, 进程名, VRAM, 状态）\n2. 每个关键进程的存活/死亡状态\n3. GRPO 当前 step 和 ETA\n4. 哪些 Llama clean seeds 训练完成、eval 完成\n5. Qwen s10 是否完成\n6. 空闲 GPU 列表\n7. 建议 kill 的 zombie 进程列表\n\n用 save_project_file 将审计结果写入 `gpu_audit_35694.md`。\n",
  "tool_groups": [
    "ssh",
    "knowledge"
  ]
}
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "87368d4e-6d48-43ed-8792-16b2ba667912",
  "isSidechain": false,
  "requestId": "req_011CbFmS7YmNS6QNcALvQNLk",
  "type": "assistant",
  "uuid": "75247e66-8ded-4e88-ba4b-0d8257da27a9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/.claude/sessions/agent_272f846c",
  "sessionId": "465c36a7-990a-4437-ba2f-9fd3ebf0f8ef",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Tt3K44bQJvydq44wMNSVfH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1068,
      "cache_read_input_tokens": 77058,
      "output_tokens": 4008,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1068,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4008,
          "cache_read_input_tokens": 77058,
          "cache_creation_input_tokens": 1068,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1068
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

_source line 41_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[HANDOFF] 你是 Main Agent，这是 Loop #2。  ## 上一轮交接 (task_context)  ### 1. 🔴 硬约束 / 红线 - GPU 白名单: westd-35694 的 cuda:0/1/2/3，不可用其他设备 - Llama 模型路径来自 ModelScope (`LLM-Research/Meta-Llama-3.1-8B-Instruct`)，不是…",
  "leafUuid": "75247e66-8ded-4e88-ba4b-0d8257da27a9",
  "sessionId": "465c36a7-990a-4437-ba2f-9fd3ebf0f8ef"
}
```

---

### Runtime record

_source line 42_

```json
{
  "type": "ai-title",
  "aiTitle": "Confirm Llama clean status and analyze contam results",
  "sessionId": "465c36a7-990a-4437-ba2f-9fd3ebf0f8ef"
}
```

---

### Tool result

_source line 43 · 2026-05-21T13:09:56.453Z_

<details><summary>↩ Tool result · `toolu_016u3mNhWnEQFbSm7M38D6Ry`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"worker_id\": \"worker_ssh_gpu-audit-35694_20260521T130954\", \"status\": \"running\", \"log_path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/logs/workers/worker_ssh_gpu-audit-35694_20260521T130954.log\", \"setup_data\": {}, \"message\": \"Worker worker_ssh_gpu-audit-35694_20260521T130954 started. Use get_worker_status('worker_ssh_gpu-audit-35694_20260521T130954') to check progress.\"}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "75247e66-8ded-4e88-ba4b-0d8257da27a9",
  "isSidechain": false,
  "promptId": "26661264-62cc-4d8c-933c-ac64167cc12e",
  "type": "user",
  "uuid": "ce53539b-7b86-4294-bbae-8ddd97058382",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"worker_id\\\": \\\"worker_ssh_gpu-audit-35694_20260521T130954\\\", \\\"status\\\": \\\"running\\\", \\\"log_path\\\": \\\"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/logs/workers/worker_ssh_gpu-audit-35694_20260521T130954.log\\\", \\\"setup_data\\\": {}, \\\"message\\\": \\\"Worker worker_ssh_gpu-audit-35694_20260521T130954 started. Use get_worker_status('worker_ssh_gpu-audit-35694_20260521T130954') to check progress.\\\"}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"worker_id\": \"worker_ssh_gpu-audit-35694_20260521T130954\", \"status\": \"running\", \"log_path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/logs/workers/worker_ssh_gpu-audit-35694_20260521T130954.log\", \"setup_data\": {}, \"message\": \"Worker worker_ssh_gpu-audit-35694_20260521T130954 started. Use get_worker_status('worker_ssh_gpu-audit-35694_20260521T130954') to check progress.\"}, \"error\": null, \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "75247e66-8ded-4e88-ba4b-0d8257da27a9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/.claude/sessions/agent_272f846c",
  "sessionId": "465c36a7-990a-4437-ba2f-9fd3ebf0f8ef",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---
