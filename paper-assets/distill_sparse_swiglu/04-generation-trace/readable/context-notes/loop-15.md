# agent / loop_15.md

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_15.md`
- **Structured JSON:** [`caa9107b69b726436cd2.json`](../../sessions/ca/caa9107b69b726436cd2.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 15
reason: idle_timeout
updated: '2026-05-23T00:03:58+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：westd-41718 cuda:0,1 + westd-34887 cuda:0,1（共 4× RTX PRO 6000）
- westd-41718 无外网，所有 HF 下载必须先 `source /etc/network_turbo` + 设 SSL 证书环境变量，或从 westd-34887 同步缓存
- submit_training_job 命令必须自带 `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`，不要假设 .venv 存在
- 论文 DDL：2026-05-25（EMNLP 2026 ARR May cycle），Round 19 审稿已提交等用户审批
- RevKL BoolQ 数据是 Table 4 唯一缺失格，填完前不要声称表格完整

### 2. 🖥️ 基础设施快照
- **westd-41718**：工作目录 `/root/distill_sparse_swiglu`，Python `/root/miniconda3/bin/python`（conda base），HF_HOME `/root/autodl-tmp/.hf_cache`，模型 `/root/autodl-tmp/models/llama-3.1-8b`，磁盘 765G/879G 可用（9%已用）
- **westd-34887**：同结构，有 super_glue 数据集缓存，磁盘 817G/879G 可用（3%已用）
- **活跃进程**：perlayer_kl_50_s42（PID 359439，tmux，westd-41718 cuda:0）— reconcile_crons 确认仍在跑
- **Cron**：perlayer_kl_50_s42 监控中（1 active cron）
- W&B 项目：distill_sparse_swiglu

### 3. 📊 当前状态
- **刚做完**：诊断 revkl_30_s42_boolq_uniform 失败（super_glue 数据集缓存缺失 + 无外网），已更新 registry failure_reason，已派 Worker `worker_fix_revkl_30_s42_boolq_uniform_20260522T032151` 去修复（启用代理下载数据集 + 用 submit_training_job 重跑）
- **RUNNING**：perlayer_kl_50_s42（westd-41718 cuda:0）— per-layer KL 50% uniform 训练，填 Table 4 高 sparsity 行
- **PREPARING**：revkl_30_s42_boolq_uniform（等 Worker 修复重跑）、perlayer_kl_s123_downstream_v2（PENDING 等人工审批）、另有 ~37 项历史 PREPARING 残留
- **等待中的回调**：Worker `worker_fix_revkl_30_s42_boolq_uniform_20260522T032151` 完成回调；perlayer_kl_50_s42 cron 完成回调

### 4. 📋 待办
- Worker fix 回调到达 → 确认 revkl_30_s42_boolq_uniform 已重新提交并 RUNNING，更新 registry
- revkl_30_s42_boolq_uniform 完成 → 提取 BoolQ acc，填入 ROADMAP 表 RevKL 行（当前为 —），更新 report.md，汇报 Director
- perlayer_kl_50_s42 完成 → eval PPL（应在 E2E KL 50% 11.84 和 MSE 18.52 之间），验证 2D decomposition claim 在 50% sparsity 成立，更新 Table 4
- Round 19 审稿用户审批通过 → 按 review-report-action skill 处理审稿反馈
- perlayer_kl_s123_downstream_v2 审批通过 → 确认 westd-34887 环境就绪（之前因 super_glue 缓存问题排除了 BoolQ）

### 5. 🎯 战略上下文
- **核心结论**：KL distillation 在 PPL 上全面碾压 MSE/BCE/TEAL，2D decomposition（signal type × coupling scope）是论文核心 claim——signal type 占 PPL gap 97.5%，coupling scope 主导 downstream
- **论文已接近完稿**，Round 19 fresh review 已提交。当前跑的实验是填充 Table 4 空行（RevKL BoolQ、per-layer KL 50%），不是探索新方向
- **易错点**：westd-41718 的 HF_DATASETS_OFFLINE=1 在数据集未缓存时会直接报错而非优雅降级——每次在 41718 跑新 task/benchmark 前必须确认缓存存在
- **D091**：Table 4 allocation 统一规则——30% 列用 uniform，50% 列用 global。提交评估实验时必须匹配
- **MSE 50% 已放弃**（D092）：seed sensitivity 导致 sparsity collapse（5.1%），不再重跑


---
