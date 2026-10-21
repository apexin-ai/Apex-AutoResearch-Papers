# gated_mfrm_judge_bias — Research Dashboard

> 最后更新: 2026-05-25 16:39 UTC | 更新原因: Patch 1&2 完成，Reframe 已派 Paper Agent，更新任务状态

## 核心方向
G-MFRM diagnostic framework for joint calibration of judge bias + benchmark contamination。OVB 理论 + diagnostic-first framing（D051: 从 ranking improvement 转为 diagnostic framework）。详见 paper_framing.md。

## 当前进展
- **阶段**: DDL 明天 (May 26)，论文 Reframe 进行中
- **Framing 切换 (D051)**: v4-v7 四种方法改进全部 negative → 锁定 diagnostic framework framing
- **关键证据链**: v2(-0.044) → v3(-0.015) → v7(0.000) 单调覆盖-降级关系
- **论文**: 17 页（~7.3 正文 + Limitations + Appendix/Refs）
- **Paper Agent**: 正在处理 Reframe（Abstract/Intro/Results/Conclusion）+ 详细补充指令已排队

## 近期任务
- [x] v3-v7 方法改进实验（全部 negative，支撑 D051）
- [x] Limitations 压缩 (80 词, 3 点)
- [x] Figure 5 视觉修复（panel b 标签重叠消除）
- [x] 正文扩充：fig4_bias_vs_rho 从附录迁入 §3
- [ ] **论文 Reframe**（Paper Agent 处理中）— Abstract/Intro/Results/Conclusion 对齐 D051 diagnostic framing
- [ ] **Table 2 TBD 填充** — 需 exp-020 N=17 MCMC 数据
- [ ] **orphan citation 清理** — `fuller1987` bib 条目残留
- [ ] **Round 5 审稿提交**

## GPU 预算
- **rtx6000-4x**: 4 张全空闲，方法改进实验已全部完成
- **autodl-8gpu**: 状态待确认
- 当前无 GPU 密集型任务待执行

## 论文贡献结构 (D051 锁定)
1. **OVB Theory**: confounding 存在 + bias 量化 (exp-009: joint bias 1/3 of sequential)
2. **G-MFRM Framework**: diagnostic tool 提供 c_n/d_j/θ 联合估计
3. **Diagnostic Finding**: coverage-degradation 单调关系 + synthetic-real gap 归因于 exposure quality

## 关键决策日志

| ID | 日期 | 摘要 | 关联实验 |
|----|------|------|----------|
| D052 | 2026-05-25 | 审计修复：统一数据归属（N=8标注+N=17补充）+ RMSE/τ统一到w7-ablation | exp-003b, exp-020, exp-w7-ablation |
| D051 | 2026-05-25 | Method→Diagnostic 贡献切换：v4-v7 全部 negative，转向 G-MFRM | exp-020, exp-018, exp-009 |
| D050 | 2026-05-25 | v3 Δτ=-0.015 仍为负；诊断 MFRM severity correction 是主因；启 | exp-020, exp-018 |
| D049 | 2026-05-25 | N=17 degradation root cause confirmed: 53.8% expos | exp-020, exp-020-diag-A, exp-020-diag-B, exp-020-N16 |
| D048 | 2026-05-25 | N=17 G-MFRM ranking degradation: launch 5-point di | exp-020 |
| D047 | 2026-05-25 | Kill exp-020 joint_gmfrm, diagnose and fix N=17 MC | exp-020, exp-003b |
| D046 | 2026-05-25 | D046: N=17 baseline 结果确认——所有独立方法 τ≤0.8382，无一超越 raw | exp-004, exp-020 |
| D045 | 2026-05-24 | N=17 J=6 conditional strategy: wait for MCMC Δτ be | exp-020, exp-006, exp-004 |
| D044 | 2026-05-24 | 修正：恢复 mistral-large-2407 参与 τ 计算（有验证 ELO 1250），EXC | exp-020 |
| D043 | 2026-05-24 | Option C: 保持 6 judges 全部运行，MCMC 硬启动 cutoff 为 Sonne | exp-020 |

