# agent / loop_13.md

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_13.md`
- **Structured JSON:** [`8d35168581585524fee4.json`](../../sessions/8d/8d35168581585524fee4.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 13
reason: idle_timeout
updated: '2026-05-16T19:21:30+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目只能用 westd-11235 的 cuda:0 和 cuda:1（`get_project_resource_usage` 白名单）
- westd-11235 用 conda 环境（`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`），**不存在 .venv**
- DeepSeek 系列 eval 时 max_length 必须匹配训练值 2048，用 16384 会 OOD 崩溃（28.5%）——Qwen 不受影响
- 模型/数据/checkpoint 必须放 `/root/autodl-tmp/`，根分区只有 ~30GB
- HF_HOME 必须设 `/root/autodl-tmp/.hf_cache`
- ARR May 25 提交，距今 9 天
- CodeLlama-7B 系列已被 Director kill（"user approved 13B not 7B"），不要再提交 7B

### 2. 🖥️ 基础设施快照
- **服务器**: westd-11235，工作目录 `/root/trace-verdict-study`
- **Python**: `/root/miniconda3/bin/python`（conda base env）
- **模型路径**: `/root/autodl-tmp/models/Qwen2.5-Coder-7B-Instruct`、`Qwen2.5-Coder-1.5B-Instruct`、`DeepSeek-Coder-6.7B-Instruct`、`CodeLlama-13b-Instruct-hf`
- **Checkpoint**: `/root/autodl-tmp/trace-verdict-study-checkpoints/{exp_id}/final/`
- **W&B project**: `trace-verdict-study`
- **代码 commit**: `e404237ccc765768e267d4d6fd3c89549dcf41a4`
- **GPU**: 2× ~98GB（H800/A100-80G 级别）
- **活跃进程**:
  - `codellama13b_vota_seed42`: PID 279473, tmux=codellama13b_vota_seed42, cuda:1, cron 监控中, 24%完成(108/444 steps), ~2h40m剩余

### 3. 📊 当前状态
Session-start 完成。发现 `exception_only_nomarker_seed42` 在 cuda:0 上 OOM 崩溃（PID 282597 已死，GPU 0 曾用 46.93GB）。已派 Worker 清理 GPU 0，等回调后用 `submit_training_job` 重新提交。

**RUNNING (1)**:
- `codellama13b_vota_seed42`（cuda:1）— CodeLlama-13B VOTA 训练+eval，24%

**Workers (3)**:
- `worker_ops_fix_gpu0_resubmit_nomarker_20260516T151841` — 清理 GPU 0（检查残留进程、杀旧 tmux、清 partial checkpoint）
- `worker_paper_pending_edits_round5_20260516T151855` — 论文 Round 5 修改（5 项 ⏳ 编辑）
- `worker_ops_check_vota_and_nomarker_20260516T151603` — 旧 worker，已出报告应即将结束

**关键近期完成**（已入 registry）:
- `codellama13b_exception_only_seed42`: 99.83% ← 跨家族验证成功！
- `codellama13b_no_trace_seed42`: 76.5%
- `loop_only_seed123/456`: 85.88%/86.64%（mean 86.05% ± 0.43）
- `qwen15b_full_trace_seed42`: 77.06%

### 4. 📋 待办（条件触发式）
- GPU 清理 Worker 回调（确认 cuda:0 clean）→ `submit_training_job` 重新提交 `exception_only_nomarker_seed42` 到 cuda:0（命令已在 registry spec 中，注意改 wandb_run_name 加 `_v2` 避免冲突）
- Paper Worker 回调 → 确认 5 项修改完成 → register_artifact
- `codellama13b_vota_seed42` cron 回调 → spawn worker 读 eval 结果 → 更新 registry → cuda:1 空出后提交 `exception_only_nomarker_seed123`
- 两卡空出后优先级：nomarker_seed123/456 → 其他 QUEUED
- 所有 nomarker 实验完成 → 汇总 format marker ablation 结论 → 更新 paper

### 5. 🎯 战略上下文
- **核心发现**: Exception events = most effective trace component. exception_only = 99.83% 跨 Qwen-7B/1.5B/CodeLlama-13B 完全一致（scale-invariant + family-invariant）
- **Paper framing v3.0**: 3 claims FINALIZED（exception dominance / cross-model / cross-task）
- **决策链 D044→D053**: regex baseline 93.61% 证 SFT 必要性；DebugBench 跨任务 100%；prediction overlap 确认 universal ceiling；signal-limited claim 升级
- **QUEUED 中 7 个是 killed/废弃的**（codellama_7b × 3 + qwen1.5b × 4），只有 nomarker × 3 是真正待跑的
- **OOM 踩坑**：`exception_only_nomarker_seed42` 首次提交 OOM，可能是残留进程占 GPU 0。清理后重试应该成功（Qwen-7B 正常只需 ~30GB，GPU 有 98GB）
- **论文压缩 13→8 页**（Discussion 移 appendix）尚未执行，是投稿前关键任务
- **Cron 有误判历史**——收到 failed 回调时必须 SSH 实际验证


---
