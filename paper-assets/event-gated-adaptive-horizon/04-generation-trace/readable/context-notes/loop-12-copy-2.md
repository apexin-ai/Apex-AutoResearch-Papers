# agent / loop_12.md

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_12.md`
- **Structured JSON:** [`78ce13516999fde3ca5c.json`](../../sessions/78/78ce13516999fde3ca5c.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 12
reason: max_messages
updated: '2026-05-15T16:38:12+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：只能用 cuda:0 和 cuda:1（gpu_ids 配置）。服务器 bjb1-45299 上 2×RTX PRO 6000
- 训练命令必须带 `LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=osmesa`（不是 egl！009d 三次失败可能与用了 egl 有关）
- submit_training_job 设 CUDA_VISIBLE_DEVICES 隔离，脚本内只能 `--device cuda:0`
- conda 环境激活：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`，不要假设 .venv 存在
- 源码在 `/root/autodl-tmp/event-gated-adaptive-horizon/`，不在 `/root/runs/`

### 2. 🖥️ 基础设施快照
- 服务器：bjb1-45299，account: root
- 工作目录：/root/autodl-tmp/event-gated-adaptive-horizon
- Python：/root/miniconda3/bin/python（conda base 环境）
- conda activate.d 已配置 mujoco_env.sh（LD_PRELOAD + MUJOCO_GL=osmesa 自动生效）
- logdir：/root/autodl-tmp/event-gated-adaptive-horizon/logdir/
- 活跃进程：exp_015b_frozen_dt_emb 应在 cuda:1 上 RUNNING（未确认存活，需检查）
- 009d 的 tmux session 状态未知（Worker 正在诊断中）

### 3. 📊 当前状态
**刚做完**：session-start 初始化（registry + reconcile + report.md + ROADMAP）。收到 009d 第三次失败回调（EXIT_CODE=129 = SIGHUP），已派诊断 Worker。

**RUNNING 实验**：
- exp_015b_frozen_dt_emb (cuda:1) — 2×2 消融矩阵：frozen dt_emb + subsample ON + H=8 seed 1。验证 dt_emb training 是否为 CIVO 必要条件
- exp_009d_baseline_walker_s0 (cuda:0) — Walker baseline seed 0，第三次失败待诊断。retry_count=2

**等待中**：
- Worker `worker_diagnose_exp_009d_baseline_walker_s0_20260515T123241` 正在 SSH 诊断 009d 失败原因（检查 tmux、系统日志、MUJOCO_GL 配置冲突）
- 排队实验：exp_017 (subsample OFF + trained dt_emb)、exp_010a (Cheetah baseline s1)、exp_009f (008f multi-seed)

### 4. 📋 待办
- 诊断 Worker 回调 → 读 root_cause，更新 registry(notes/conclusion/status)，如果 can_auto_fix=true 且是 MUJOCO_GL=egl→osmesa 问题则修复后第四次提交（但 retry≥3 需谨慎，考虑报 Director）；否则报 Director 决策
- 015b cron 回调（预计 ~105K steps 完成）→ 按 on-experiment-done 分析，关键看 frozen dt_emb 是否崩溃。如果不崩 → 确认 dt_emb training 是 CIVO 根因，立即提交 plan_017 到 cuda:1
- 009d 修复成功重启后 → ~19h 完成（500K steps）→ baseline seed 0 数据入 Table
- 2×2 矩阵全部闭合（015B + 017 完成）→ log decision → 推进 Cheetah 跨环境验证

### 5. 🎯 战略上下文
- **目标**：CoRL 2026，DDL 2026-05-29（剩 14 天）
- **核心因果链**：trained dt_embedding → CIVO（Critic Imagination Value Overestimation）→ stochastic collapse
- **C2 confirmed**：2/3 trained dt_emb seeds collapse（008d/009e collapse, 009b self-correct）。正确统计是 1/2 独立 seed collapse（008d 和 009e 是同一 seed=1）
- **C6 PARTIALLY FALSIFIED**：dt=1 imagination 不阻止 collapse（008e_v3_s2 崩溃），只延迟 onset ~70K steps。根因是 trained dt_embedding 存在 + replay buffer 中 dt>1 transitions
- **2×2 消融矩阵**是当前关键：隔离 dt_emb training vs subsample 的因果效应。015B（frozen dt_emb）和 017（subsample OFF）两个缺失格
- **易错点**：
  - 008d 和 009e 是同一 seed=1，不要重复计数为两个独立 collapse
  - MUJOCO_GL 必须用 osmesa 不是 egl——activate.d 脚本设了 osmesa，但 009d 命令行显式传了 egl，可能覆盖了环境变量
  - 009d 已失败 3 次，如果诊断后仍无法修复，cuda:0 空着是浪费——应考虑先跑其他排队实验（010a Cheetah baseline）同时调查
  - artifacts/figures 改动必须在本地做，不要只改服务器（Reviewer 检查本地文件）


---
