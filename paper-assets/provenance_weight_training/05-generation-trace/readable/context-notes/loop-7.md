# director / loop_7.md

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_7.md`
- **Structured JSON:** [`b2c13c9b12f40d888fe7.json`](../../sessions/b2/b2c13c9b12f40d888fe7.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 7
reason: max_messages
updated: '2026-05-15T12:36:59+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：westd-47453 cuda:0/1/2/3，不得用其他服务器或 GPU
- D026：seed456 b≥2.0 三组实验（grid_b2_0/b3_0/b5_0_seed456）已 INVALIDATED（checkpoint resume artifact），从所有统计中排除，论文只用 2 seeds
- 论文数值口径：ratio-of-means = 90.1%（从 per-seed Δ 计算），不是 mean-of-ratios 91.0%，不是 89.4%/89.9%
- τ 不是 temperature，是 α_eff 质量下界阈值。所有标注/注释/图表中用 "quality threshold"
- pretrain_weighted.py 中 n_min = max(2, batch_size//2) 会随 batch_size 联动变化，batch_size ablation 论文中必须说明

### 2. 🖥️ 基础设施快照
- 服务器：westd-47453 (connect.westd.seetacloud.com)，账号 root
- 工作目录：/root/provenance_weight_training
- Python：conda 环境（aml-train 镜像），/root/miniconda3/bin/python
- 4× RTX 6000 Pro 96GB，全部分配给本项目
- auto_eval_watcher：PID 99508（May14 启动），磁盘版本已修复（动态 GPU 选择 + glob * 扫描），重启后自动生效
- 已消耗 ~115 GPU·h / 剩余 ~65h，P0 实验预计还需 ~40h

### 3. 📊 当前状态
Registry 显示 4 个 RUNNING（ETA 早已过，可能实际已完成但无人处理）：
- ess_only_seed42 (cuda:1) — ESS-only max-intervention baseline，**关键实验**：决定 α_eff 独立价值
- golden_ratio_seed42 (cuda:0) — Golden Ratio oracle baseline
- nmin1_seed42 (cuda:2) — n_min=1 sensitivity
- tau_06_seed42 (cuda:3) — τ=0.6 sweep 第一组

**Dream dream_20260515T102146 已完成（11:19 UTC）但回调未送达我。** 报告在 `artifacts/dream_reports/dream_20260515T102146/`，尚未分析。上一轮 dream（dream_20260515T011902）全三档 Weak Reject，导致 D021-D023 三次 framing 重构。

待处理：τ sweep 后续 4 组（τ=0.5/0.7/0.9/0.95）脚本已就绪，GPU 释放即提交。

### 4. 📋 待办
- **第一优先**：读 dream_20260515T102146 报告 → 按 dream-report-action skill 分析，判断 D023 dual-constraint framing 是否有结构性缺陷
- 4 个 RUNNING 实验 ETA 已过 → 立即派 Agent 检查实际完成状态，处理结果
- ess_only_seed42 完成 → PPL 对比 adaptive_fix：若 ESS-only 更差 → dual-constraint framing 站住；若相近/更好 → α_eff 价值被削弱，需再次调整 framing
- GPU 释放 → 按顺序提交 τ sweep 后续：tau_05 → tau_07 → tau_09 → tau_095
- τ sweep 6 点全齐 → 生成 τ-PPL 曲线（analyze_tau_sweep.py），支撑 Claim 3
- 全部 P0 完成 → 评估是否启动 P1（ρ=0.6 contamination、Llama-3B、detect-and-remove baseline）

### 5. 🎯 战略上下文
- 投稿目标：EMNLP ARR May 25（剩 ~10 天）
- 核心 framing（D023）：dual-constrained adaptive b*（α_eff 质量下界 + ESS 稳定上界 → minimum intervention principle）。这是第三版 framing，前两版分别因 α_eff 单调性问题和 decorative 判断被推翻
- D023 的关键赌注：ESS-only baseline 实验。如果 ESS-only 训练效果与 dual-constraint 相当，α_eff 的独立贡献被质疑，需第四次 framing 调整
- τ 已从理论推导降级为 empirical HP with theoretical motivation（D025），τ sweep 证明宽泛范围内不敏感即可
- Llama-3B 已从 P0 降级 P1（D024，节省 ~25h）
- 易错点：不要把 dream 模拟的审稿意见当真实审稿处理——dream 是检查 plan 结构性缺陷的工具，不是逐条修论文的依据


---
