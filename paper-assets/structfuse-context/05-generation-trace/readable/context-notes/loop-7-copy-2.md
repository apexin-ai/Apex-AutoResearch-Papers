# agent / loop_7.md

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_7.md`
- **Structured JSON:** [`3f205bfe7ca9853e4ac6.json`](../../sessions/3f/3f205bfe7ca9853e4ac6.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 7
reason: idle_timeout
updated: '2026-05-14T21:12:11+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：**只能用 bjb1-42106 的 cuda:0 和 cuda:1**。曾两次 GPU 越界被 CRITICAL（D005, m2_early_pilot_v3 用了 cuda:0 on cqa1）
- m1_reextract_v2 数据**不重跑 M2**（Director Session 8 决策）：ARR May 25 DDL 不允许再加 4-5 天重训，新数据只做 1-seed pilot 对比 + 论文讨论点
- BM25 Phase 2 由 tmux watcher 自动触发，watcher 启动的训练**不经过 submit_training_job**——链完成回调时必须补注册 cron
- Claim 2 已降级为 "exploratory observation"（D035），不可在论文中按 core claim 强度陈述
- Registry 状态只能前进，长链中途误标时创建 `_resumed/_continued` 新 entry，不可回退

### 2. 🖥️ 基础设施快照
- **服务器**：bjb1-42106，2× RTX PRO 6000 96GB
- **工作目录**：`/root/structfuse`
- **Python**：`/root/miniconda3/bin/python`（conda base 环境，不是 venv）
- **激活命令**：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- **模型缓存**：`/root/autodl-tmp/` 下（Qwen2.5-Coder-3B, StarCoder2-3B）
- **训练数据**：`/root/autodl-tmp/structfuse/full_m2_training_data/`（11,308 train/seed）
- **M1 原始数据**：`/root/autodl-tmp/structfuse/full_m1_data/`
- **BM25 数据已就绪**：`/root/autodl-tmp/structfuse/full_m2_training_data/{train,val}_bm25_s{42,43,44}.jsonl`
- **活跃进程**：
  - PID 337267 (cuda:0, tmux) — m2_full_qwen_continued 链：random_s44 running → embedding×3 → dataflow×3
  - PID 519791 (cuda:1, tmux) — m2_full_starcoder_resumed 链：random_s43 running → s44 → embedding×3 → dataflow×3
  - m1_reextract_v2 (CPU, 4 workers) — ~80% done
  - tmux `bm25_qwen_watcher` / `bm25_starcoder_watcher` — 每 5min 检查链 PID，退出后自动启动 BM25 训练
- **Cron**：3 个活跃（m1_reextract_v2, m2_full_starcoder_resumed, m2_full_qwen_continued）

### 3. 📊 当前状态
**刚完成**：session-start 初始化，reconcile crons 确认 3 个实验仍在运行。

**RUNNING 实验**：
- `m2_full_qwen_continued`：random_s44 step 650/2816，eval@500 R@1=0.6009。2/10 runs done。速度 ~428 steps/h，ETA 全链 ~50h（~May 17）
- `m2_full_starcoder_resumed`：random_s43 step 500/2810。1/9 runs done。速度 ~195 steps/h，ETA ~96h（~May 18-19）
- `m1_reextract_v2`：80.8% done (22,842/28,276)，0 ERROR，~560/hr。预计 May 15 ~15:00 CST 完成

**PREPARING**：`plan_005_stratified` — 分层分析脚本已就绪（5 patches done），等 M2 checkpoint 出后执行真实评估

**QUEUED**：`plan_018_bm25` Phase 2（watcher 自动触发）、`plan_015_dynamic`（排队等 GPU）

**Worker 池**：0 running — 当前无 CPU 任务需要执行，GPU 满载

**无待处理回调**，无 pending Director 决策。

### 4. 📋 待办（条件触发式）
- m1_reextract_v2 cron 完成回调 → spawn worker 合并 .json 到 all.jsonl，统计总量，更新 registry，汇报 Director
- m2_full_qwen_continued 链完成 → bm25_qwen_watcher 自动触发 BM25 训练 → **补注册 cron 监控 BM25 进程** → 同时启动 plan_003 SWE-bench eval（另一卡）
- m2_full_starcoder_resumed 链完成 → bm25_starcoder_watcher 自动触发 → 补注册 cron
- 两卡 M2 全部完成 → 立即跑统计检验（3 策略 × 3 seeds × 2 encoders paired test）→ 更新 paper claims
- plan_005 真实评估 → M2 best checkpoint 出后 spawn worker 用 analyze_stratified.py 跑真实 R@1（0 GPU，可在 M2 跑完后立即执行）
- Post-M2 GPU 空出 → P0: plan_003 SWE-bench (40h) + plan_018 Phase 2 (15h) 并行两卡；P1: plan_004 + plan_019 + plan_005

### 5. 🎯 战略上下文
**核心结论链**：embedding distance negatives consistently improve contrastive code retrieval (+1.6–2.0pp R@1, pilot confirmed on both Qwen and StarCoder)。Dataflow benefit is encoder-dependent（Qwen +0.8pp, StarCoder -0.5pp），故 D035 将 Claim 2 降级为 exploratory。BM25 baseline 是审稿最大结构性缺陷（Dream 三档一致），Phase 2 结果决定 narrative（harm→correction / neutral→systematic comparison）。

**时间线**：M2 ~May 17 → post-M2 实验 ~May 19 → 写作 ~May 20-24 → **ARR May 25**

**易错点**：
- StarCoder 比 Qwen 慢一倍（~195 vs ~428 steps/h），链完成时间不同步，BM25 watcher 独立触发
- random_s44 的 eval@500 R@1=0.6009 异常高于 s42(0.5527)/s43(0.5554)——可能是 early eval noise，不要过早下结论
- plan_005 的 confound 分析 v1 数据**全部无效**（D039：dry-run mock predictions），只有分布结构（cross_tabulation.csv）可信
- re-dream gate 未通过但 Director 决定继续（D034）：median=WR 由不可修复因素驱动，目标最大化 Best case
- Bash 预读陷阱：运行中的 bash 链脚本已预读到内存，磁盘修改无效


---
