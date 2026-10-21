# agent / loop_13.md

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_13.md`
- **Structured JSON:** [`609aa26a471768e4306c.json`](../../sessions/60/609aa26a471768e4306c.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 13
reason: idle_timeout
updated: '2026-05-16T12:51:10+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：westd-47453 的 cuda:0/1/2/3，不可用其他设备
- grid_b0_1_seed42 结果直接决定 Claim 2 走向——PPL 回升=U形确认 b=0.3 grid-best；PPL 继续降=需要 reframe Claim 2。**不要在 Worker 回调前自行判定结论**
- τ 系列实验（threshold_q03/q07）用 WANDB_MODE=disabled，完成后需从日志人工取指标，不能依赖 W&B
- submit_on_allocated 命令必须自带 `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`，不要假设 .venv
- 投稿 deadline: EMNLP 2026 ARR May 25（还剩 9 天）

### 2. 🖥️ 基础设施快照
- 服务器：westd-47453，工作目录 /root/provenance_weight_training
- Python：/root/miniconda3/bin/python（conda base 环境）
- 模型：Qwen/Qwen3-0.6B（HF 下载到本地）
- 数据：/root/provenance_weight_training/data/scored_data.jsonl（371499 条，ρ=0.4）
- 日志目录：~/runs/provenance_weight_training/
- 脚本目录：/root/provenance_weight_training/scripts/
- 活跃进程：
  - threshold_q03_seed42: PID 299248, cuda:3
  - threshold_q07_seed42: PID 302159, cuda:0
  - random_reweight_seed42: PID 310180, cuda:2
- cuda:1 空闲（grid_b0_1 刚完成释放）

### 3. 📊 当前状态
- 刚收到 grid_b0_1_seed42 完成回调（ANALYZING），已派 Worker `worker_analyze_grid_b0_1_seed42_20260516T084409` 去 SSH 读日志取指标
- **等待该 Worker 回调**——拿到 PPL 后才能判定 Claim 2 走向
- 3 个实验 RUNNING（threshold_q03/q07 + random_reweight），各自有 cron 监控
- 2 个 PREPARING：batchsize16_nmin8_seed42、grid_b0_2_seed42
- report.md 显示 cuda:1 空闲——Worker 回调后应立即安排 grid_b0_2_seed42 上 cuda:1

### 4. 📋 待办
- Worker analyze 回调到 → 根据 PPL 判定：
  - PPL > 17.640 (b=0.3) → U形确认，conclusion=success，Claim 2 "b=0.3 grid-best, adaptive within noise" 成立
  - PPL < 17.640 → grid-best 移至 b=0.1，conclusion=negative 或需 reframe Claim 2 为 "eliminates grid at minimal gap"
  - 无论哪种：update_registry(status=DONE) + 刷 report.md + 汇报 Director
- cuda:1 释放 → 立即提交 grid_b0_2_seed42（b=0.2，补完曲线）
- threshold_q03/q07 完成 → 对比 detect_remove (PPL 17.29)，验证 "filtering needs precise threshold calibration"
- random_reweight 完成 → 若 PPL > adaptive，证明 detector signal load-bearing；若 PPL ≈ adaptive，Claim 需调整
- 所有 baseline 实验完成后 → 更新 paper_framing.md Claim 2 数据表 + 通知论文 Worker 更新 Results

### 5. 🎯 战略上下文
- 核心 story：dual-constrained adaptive b*（α_eff 下界 + ESS 上界）→ 自动选 b，免 grid search
- Claim 1 ✅ (dual > ESS-only)，Claim 3 ~90% (proportion-free)，**Claim 2 是当前最大风险点**
- D051 发现 detect_remove PPL=17.29 大幅优于 adaptive(17.653)——这不是 bug，因为 detect_remove 丢弃数据导致 holdout 集有效样本变少/分布偏移，需在论文中解释而非视为 adaptive 劣势。threshold_q03/q07 实验就是为此设计的对照
- 易错点：b-PPL 曲线不是单调的——b=0.5 给 17.706，b=0.3 给 17.640，b=0.1 如果回升则 U 形。不要假设 b 越小越好
- D054 已确认论文定位为 "focused empirical study"，不追求 theoretical contribution
- GPU 预算紧张（剩余 ~10-12h），每个 slot 完成后必须立即填入下一个实验


---
