# occsafe_vla — Research Dashboard

> 最后更新: 2026-05-30 00:37 UTC | 更新原因: D081 claim 最大化 7 项全部完成（interaction plot + TSR/per-task/instability 贡献升级 + rebuttal 4 项修正）

> 核心方向详见 paper_framing.md

## 核心方向
Auxiliary spatial supervision 不提升 VLA collision avoidance。两个 additive main effects：BN+gradient flow 有害（g=0.78）；LN 优势（g=0.88）。ANOVA 交互项零。

## 目标会议
- **SafeRL Workshop @ RSS 2025**: 已提交（May 28），进入审稿修复阶段

## 当前阶段：审稿修复
第 3 轮审稿报告：4/10 Weak Reject，17 个 issue。

**修复进度：12/17 resolved + 论文全面加固 + GPU 恢复脚本就绪**

| 状态 | Issue | 类型 | 说明 |
|------|-------|------|------|
| ✅ | R1-W15, RD2-N3, RD3-W4 | format | 8 页合规 + Limitations 移入正文 |
| ✅ | RD3-C1 | framing | 重构为 "two additive main effects" |
| ✅ | RD2-W1, RD2-W2 | method | Factorial 描述修正 + Hedges' g |
| ✅ | R1-W21, RD2-W3, RD2-W5 | writing | v1 caveat + 标题范围 + guidelines 限定 |
| ✅ | RD2-W6, RD3-W1, RD3-W2 | writing | 补引用 + permutation ANOVA + 机制区分 |
| 🔴 | RD2-N1 (critical) | experiment | 加 seeds 提升统计功效（n≥5/cell） |
| 🔴 | RD2-N2 (critical) | experiment | v2 Random OCC 验证 content irrelevance |
| 🔴 | RD2-W4 | experiment | BN eval mode 消融 |
| 🔴 | RD3-W3 | experiment | λ₀ sweep {0.001, 0.01, 0.1} |
| ⏳ | R1-C9 | experiment | v1/v2 mixing（关联 RD2-N2） |

## 统计加固（D080，全部完成）

| 分析 | 结果 | 论文位置 |
|------|------|---------|
| ✅ Bayesian ANOVA | BF₀₁=3.50 (moderate additivity) | appendix.tex + Table 2 caption |
| ✅ TSR factorial ANOVA | All p>0.27 (safety-specific) | appendix.tex |
| ✅ Leave-one-out | 14/14 方向一致 | appendix.tex |
| ✅ Levene + Welch | W=0.71, p=0.57 | appendix.tex |
| ✅ Per-task 放大效应 | Norm 4× on hard tasks | results.tex |
| ✅ discussion.tex 修复 | "highest TSR" → 正确措辞 | discussion.tex |

## 论文质量加固（全部完成）

**Phase 1（锐化+修复）：**
- ✅ 论文修复 6 项 + 锐化 5/7 项 + 一致性验证 PASS
- ✅ Figure 3 caption v1 annotation + labels 清理 + rebuttal 预算修正
- ✅ Introduction 重叠修复 + Discussion 精简 + 8 页合规

**Phase 2（D081 claim 最大化，Reviewer 驱动）：**
- ✅ Figure 2(b) 改为经典 interaction plot（平行线可视化无交互）
- ✅ Table 2 caption 加 BF₀₁=3.50
- ✅ C1 contribution 加 TSR invisibility 子发现 + per-task 4× amplification
- ✅ C3 guidelines 加 7× cross-seed variance instability warning
- ✅ Rebuttal: breadth-over-depth 解释 + RD2-N2 contingency 文本 + wall time 修正 + convergent evidence 总结句

编译通过，主体 8 页合规。

## GPU 恢复准备
- ✅ 14 个实验启动脚本就绪（art_20260530_d856df）
- 包含 checkpoint resume 检查逻辑 + nvidia-smi 验证

## 基础设施
- 2× AutoDL 服务器（westd-34685, westd-10894），各 4×RTX PRO 6000 98GB
- **当前状态：🔴 GPU 不可用** — 两台均 SSH 不可达（已通知用户 3+ 次，等待重启确认）
- 论文源码：`projects/occsafe_vla/docs/paper/`

## 近期任务
- [x] 写作类修复 12 个 issue
- [x] 统计加固 6 项 + 论文质量锐化
- [x] GPU 恢复脚本 14 个就绪
- [x] D081 claim 最大化 7 项（interaction plot + rebuttal 加强）
- [ ] **阻塞：等用户确认 AutoDL 服务器重启**
- [ ] GPU 上线后：nvidia-smi 验证 → 检查 r4/r5 checkpoints → 提交 P0 实验
- [ ] 实验完成后更新论文数据 + ANOVA 重算 + 提交第 4 轮审稿

## GPU 预算
- 本地 8 GPU（2×4 RTX PRO 6000 98GB），当前 0/8 可用
- 剩余实验 GPU 需求：~216 GPU·h（RD2-N1 ~104h + RD2-N2 ~39h + RD2-W4 ~15h + RD3-W3 ~36h + buffer）
- 8 卡并行预计 ~27h wall time

## 关键决策日志

| ID | 日期 | 摘要 | 关联实验 |
|----|------|------|----------|
| D081 | 2026-05-30 | D081: GPU 停机窗口论文质量最大化——采纳 Reviewer 7 项建议：interacti | — |
| D080 | 2026-05-29 | 采纳 Reviewer 统计脆弱性分析——追加 3 个零成本分析加固论文：Bayesian ANOV | — |
| D079 | 2026-05-28 | D079: Framing 重构——Cell 4 vs Vanilla (d=2.31, p=0.0 | — |
| D078 | 2026-05-28 | Cell 4 第4 seed 暂不并入论文，等 RD2-N1 种子扩充(n≥5)完成后一次性更新全部 | — |
| D077 | 2026-05-28 | 批准 4 组 post-submission 实验（15-16 runs, ~220 GPU·h）： | — |
| D076 | 2026-05-28 | D076: 强制 revert 论文到 paper-final-check 版本（n=3），撤销 P | detach_ln_v2_s2_eval |
| D075 | 2026-05-28 | 保持论文 Cell 4 n=3，不纳入第 4 seed (s2 CAR=0.784)。ANOVA 脚 | detach_ln_v2_s2_eval |
| D074 | 2026-05-27 | Framing shift: from "ordinal interaction" to "dual | — |
| D073 | 2026-05-27 | D073: 采纳 Reviewer 建议——提升 LN normalization 主效应为 sec | full_occ_retrain_s0, full_occ_ln_v2_s1c, detach_ln_v2_s1_35 |
| D072 | 2026-05-27 | 纯 v2 统计分析确认 BN-specific gradient flow harm：Full OC | full_occ_retrain_s0, full_occ_bn_v2_s1, mvp_occ_s3_v2, detach_bn_v2_s0, detach_bn_v2_s1, detach_bn_v2_s2, ablation_occ_detach_s3_v2 |


