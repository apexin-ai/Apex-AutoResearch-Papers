# reviewer / loop_21.md

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_21.md`
- **Structured JSON:** [`51a8d233d8941d95c575.json`](../../sessions/51/51a8d233d8941d95c575.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 21
reason: max_wall_time
updated: '2026-05-23T20:17:01+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目 GPU 白名单未在 constraints.yaml 中明确，但当前实际分配：cuda:0/1/2/3 均在用。B=8 实验占 cuda:0 和 cuda:2，ablation 占 cuda:1 和 cuda:3（已完成）。
- 1.7B 实验全部使用 τ=0.8（非 0.6B 的 τ=0.7），两个 scale 的 τ 不同是设计选择，不要混淆。
- `generate_paper_figures.py` 中 `fig2_constraint_regime()` 仍硬编码 tau=0.8 旧数据——**禁止重新运行此脚本生成图**，当前 PDF 已被 worker v3 用正确 tau=0.7 数据覆盖。
- config.json 中 `contamination_ratio` 字段是元数据标签，实际 ρ 由 `--data_path` 决定。多个实验的 config 写了 0.2 但实际跑的是 0.4 数据——功能正确，元数据错误。

### 2. 🖥️ 基础设施快照
- 服务器：westd-41312(root)，代码根目录 `/root/provenance_weight_training`
- 数据盘：`/root/autodl-tmp/provenance_weight_training/`（模型输出、数据、eval 结果）
- Python：`/root/miniconda3/bin/python`（conda base 环境）
- 模型：`/root/autodl-tmp/provenance_weight_training/output/models/` 下所有实验
- 数据：`/root/provenance_weight_training/data/scored_data.jsonl`（371,499 条，ρ=0.4）
- 论文本地路径：`/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/`
- 活跃进程（截至 handoff）：bs8_nmin4_adaptive_seed456_r2 (cuda:0, ~76%), bs8_nmin4_uniform_seed456_r2 (cuda:2, ~78%)，预计 ~2h 完成

### 3. 📊 当前状态
**刚完成**：
- α_eff-only ablation (n_min=1) seed42+seed123 训练+eval 完成。Registry 已更新：seed42=17.750, seed123=17.733, mean=17.742±0.009。比 uniform (17.694) 差 +0.048，比双约束 (17.674) 差 +0.068。Finding 3 得到消融支持。
- 全文交叉验证完成（Part A/B/C/D），发送了 3 份报告给 Director：
  1. 1.7B 数据核实（降级为 warning，3 seed 完整，uniform PPL 四舍五入偏差）
  2. detector table vs tau table PPL 不一致（17.650 vs 17.683，疑 checkpoint-resumed 混入）
  3. α_eff-only eval 结果 + 2×2 消融矩阵分析

**仍在运行**：
- bs8_nmin4_adaptive_seed456_r2 和 bs8_nmin4_uniform_seed456_r2，约 2h 后完成
- n_min=1 seed456 待 B=8 完成后启动

**已确认修复的问题**：p=0.010 统一 ✓, intro "empirically observed" ✓, Spearman ≥0.86 ✓, discussion epoch qualifier ✓, 1.7B uniform 13.27 ✓

### 4. 📋 待办
- B=8 seed456 完成 → 核实 eval 结果，检查是否与 seed42/seed123 的 B=8 数据一致，确认 batch-size amplification 三 seed 完整
- n_min=1 seed456 启动通知 → 核实 config（n_min=1, tau=0.7, B=4, seed=456），确认 GPU 分配
- n_min=1 seed456 eval 完成 → 更新 2×2 消融矩阵为 3-seed，重新评估 Finding 3 显著性
- results.tex:120 更新通知 → 核实 PPL 从 17.789 改为 17.742（或 3-seed 均值），确认论文内部一致
- tab:detector 修复通知 → 核实 PPL 改为 from-scratch 值 17.683, Δ=-0.011

### 5. 🎯 战略上下文
**论文核心三发现**：(1) epoch confound >95% of D&R advantage; (2) detector needs both AUC + calibration; (3) minimum intervention (dual-constrained) outperforms maximization。

**评分预估**：3.0 (Findings)。结构性证据广度限制（单模型族、self-contamination、N=3 seeds）阻止升至 3.5。α_eff-only 消融加强 Finding 3 但不改变整体 scope。

**易错点**：
- memory.md 和 report.md 严重过时（仍显示 1.7B Δ=-0.23 单 seed、seed123 "准备中"），不要信这两个文件——以 registry 为准。
- 论文中有两处 τ 不同：0.6B 用 τ=0.7（主实验），1.7B 用 τ=0.8。不要假设全局统一。
- tab:detector 和 tab:tau 理应记录同一实验但 PPL 差 0.033——最可能是 tab:detector 混入了 checkpoint-resumed seed42。这个 Director 尚未确认是否修复。
- 2×2 消融矩阵中 ESS-only 仅 1 seed (17.691)，α_eff-only 仅 2 seed——数据不对称，claim 需谨慎措辞。
- "α_eff-binding majority (50.9%)" 是频率统计，但消融显示 ESS 的边际性能贡献 (-0.066) 远大于 α_eff (-0.003)——这个张力可能是 discussion point，也可能被审稿人攻击。


---
