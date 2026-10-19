---
loop: 26
reason: max_wall_time
updated: '2026-05-29T05:39:36+00:00'
---

### 1. 🔴 硬约束 / 红线
- CoRL 2026 DDL **已过**（2026-05-28 20:00 BJ）。论文数据已锁定（D184），**不得修改 Table 1/Table 3 数据**，除非用户明确指示转投其他会议
- 3/4 服务器不可达（bjb1-32546, bjb2-28827, cqa1-32758），**不要反复重试连接**——AutoDL 端口可能已变，需用户去控制台查新端口
- Registry 中 SR 字段名不统一：`success_rate` / `overall_success_rate` / `SR` 三种都有。读 metrics 时必须三个都查，否则漏判数据覆盖

### 2. 🖥️ 基础设施快照
- **唯一可达服务器**：bjb1-18228（root），1× RTX 4090，空闲
- 工作目录：`/root/acr-vla-conformal-refinement`
- Python：`/root/miniconda3/bin/python`（conda base）
- 不可达：bjb1-32546 / bjb2-28827 / cqa1-32758（全部 connection refused）
- 活跃进程：无（全面停机，0 RUNNING 实验）
- 论文源码：本地 `docs/paper/`，`\graphicspath{{figures/}}`
- Registry：1423 实验，全部 DONE/killed/cancelled

### 3. 📊 当前状态
本轮审查了 6 个 Worker 产出：
- **fig_teaser + fig_method_bar**：数据与 Table 1 一致 ✓。method bar 中 "τ≈20%" 标注是 trigger rate 不是阈值——**尚未修复**（gen_method_bar.py L96）。两图配色不一致（teaser 旧色 #A93226，method bar 新色 #A63D40）——**尚未修复**
- **fig_tau_sweep**：SR 数据与 Appendix Table 5 一致 ✓。Object τ=0.10 trigger rate "52%" 在 appendix 中标 "---"——**尚未修复**。Goal τ=0.15 标注 33% 应为 34%
- **fig1_pipeline**：经历 3 轮 PaperBanana → 最终回退 matplotlib 版本。d₂ 下标已修复 ✓，但 trigger rate 范围回退为 "~4-20%"（应为 "~3-20%"）——**尚未修复**
- **supplementary_summary.md**：修复了 `overall_success_rate` 字段漏读 bug，数据覆盖显著改善 ✓
- **GPU check**：确认全面停机状态 ✓
- **ROADMAP 更新**：post-submission 等待态，数据与论文一致 ✓

无 RUNNING 实验、无待回调 Worker、无 Cron。等待用户确认提交状态。

### 4. 📋 待办
- 用户确认已提交 CoRL → 关闭项目，释放服务器
- 用户说转投其他会议 → 重新评估 DDL、恢复服务器、根据新 venue 要求调整论文
- 用户恢复服务器 → 重新验证端口并更新 SSH config，补齐 Appendix bonus seed 剩余缺口（goal/reconvla 差 1 seed、pi05 spatial CRM 差 2 seed）
- 任何新 Worker 修改 Table 1/Table 3 数据 → **CRITICAL 打回**（D184 数据锁定）

### 5. 🎯 战略上下文
- **核心结论**：CRM unconditional correction 在 SmolVLA 上 4/4 suites 有害（-1.3 到 -14.8pp），τ-gating 完全恢复（+2.8 到 +14.5pp）。cross-VLA 在 π0.5 上验证跨模型一致性。论文 framing = "knowing when NOT to correct"
- **决策链**：D170（4/4 harmful 叙事）→ D177（K-matched Table 1）→ D178（Long -14.8pp 最强证据）→ D184（数据锁定 + 提交）
- **易错点**：
  1. 不要把 Δ_gate（Adaptive - CRM）和 Δ_vs_VLA（Adaptive - VLA-only）搞混。论文 Table 1 报的是 Δ_gate，ROADMAP 同时展示两种
  2. Object/Long 的 Adaptive vs VLA-only 提升极小（+0.1 / -0.3pp），论文 framing 回避了"beat VLA-only"的 claim，聚焦于"recover from CRM degradation"
  3. Appendix Table 5 Spatial τ=0.25 SR=80.0 与 Table 1 的 80.8 有 0.8pp 差异（pre-existing，可能 seed 组合不同），这是已知问题不要重复 flag
  4. 图表有 4 个未修复的 warning 级问题（上述），如果 Paper Agent 再次触发图表生成，需跟进验证
