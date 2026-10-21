# acr-vla-conformal-refinement — Research Dashboard

> 最后更新: 2026-05-30 02:23 UTC | 更新原因: Camera-ready 三项修复完成（fig:teaser 引用 + Related Work 2026 近作 + Limitations 坦诚扩充），Reviewer 全项 PASS

> 详见 paper_framing.md（D170-D186）

## 核心方向
**ACR-VLA: Adaptive Conformal Refinement for Frozen Flow-Matching VLAs**。CoRL 2026 DDL 已过。投稿状态待用户确认。

## 当前状态：CAMERA-READY
- **14 轮 Paper Agent 指令全部完成**，Reviewer 逐项验证 PASS
- **竞争力 6.5/10 | Accept 概率 25-30%**
- **编译通过**：主文 8 页 + 附录，0 critical warnings
- **Rebuttal 预案**：5 条预案就绪

## 完成的全部改进（5→6.5+ 历程）
1. Abstract 重写（hook + headline numbers −14.8pp/+13.5pp/~170ms）
2. MC3 升级（preliminary→confirm，π₀.₅ n=3 完整，−17.5pp headline）
3. 统计论证三层：8/8 sign test p=0.004 + 7/8 gating p=0.035 + Cohen's d
4. π₀.₅ compact table 入主文（Figure 5 移 appendix）
5. Deployment Guidelines 5 条 + trigger rate diagnostic
6. Related Work 显式定位 + **2 篇 2026 近作**（SC-VLA, Tang et al.）
7. Intro 紧凑化 + root cause preview
8. Conclusion Future Work 3 方向
9. Section 2 标题呼应 title + fig:teaser 引用补全
10. SmolVLA Long n=5 full recovery（−0.3pp）
11. Per-suite t-test 7/8 significant + trigger rate SD ≤ 0.9pp
12. **Limitations 扩充至 ~198 words**：坦诚承认方法不 beat VLA-only，贡献定位 diagnostic + methodological

## Registry 数据挖掘结论（2026-05-30）
- 113 有效实验全量分析，确认现有 claims，无遗漏 pattern
- 6.5→7 barrier = Novelty×Impact（方法简单 + 仅 LIBERO），非写作/统计可解

## Pending（阻塞于用户决策 + GPU）
| 实验 | GPU-hours | 价值 |
|------|-----------|------|
| SmolVLA Long VLA-only+CRM s45/s46 | 5.0 | Long n=5 baseline+CRM 对齐 |

## 阻塞项
- **飞书 API 99991403**：月度配额耗尽，预计 6/1 恢复
- **用户决策**：投稿状态 / 是否补实验 / 后续计划
- **服务器全部释放**（2026-05-28 用户指令）

## GPU 预算
- 当前：**0/0**，全部释放

## 关键决策日志

| ID | 日期 | 摘要 | 关联实验 |
|----|------|------|----------|
| D186 | 2026-05-29 | D186: 论文达非 GPU 最大潜力 6.5/10，accept 概率 25-30%。进一步提分需 | — |
| D185 | 2026-05-29 | D185: Adaptive ε 离线分析 — NO-GO。二元 gating 已是最优，conti | — |
| D184 | 2026-05-28 | Title 锁定 + 20:00 数据锁定 + CoRL 提交确认。用户授权按核心 claim 定  | — |
| D183 | 2026-05-28 | D183: 移除 OpenVLA Contribution 4，保留 discussion 段 bo | — |
| D182 | 2026-05-28 | D182: Pi05 Table 2 Long 数据确认 — VLA-only 95.0%, CRM | pi05-crm-always-on-long-s42, pi05-vla-only-long-s42-4090-r3, pi05-vla-only-long-s43-4090, pi05-vla-only-long-s44-4090 |
| D181 | 2026-05-28 | D181: Table 2 确认 degradation-only 两列（VLA-only + CR | pi05-crm-always-on-object-s42, pi05-crm-always-on-goal-s42, pi05-object-adaptive-s42-cqa1 |
| D180 | 2026-05-28 | Table 2 叙事调整：Pi05 CRM always-on 跨模型一致有害（MC1 强化），但  | pi05-crm-always-on-object-s42, pi05-crm-always-on-spatial-s42, pi05-crm-always-on-goal-s42 |
| D179 | 2026-05-28 | Title 锁定 "Knowing When Not to Correct: Adaptive Te | crm-always-on-long-s42, pi05-crm-always-on-goal-s42 |
| D178 | 2026-05-27 | Long CRM always-on -14.7pp 是论文最有力证据。4/4 suites CRM | crm-always-on-long-s42, crm-always-on-long-s43, smolvla-tau025-object-s42-r3, smolvla-tau025-long-s42 |
| D177 | 2026-05-27 | Table 1 重构为 K-matched 3 列（VLA-only K=1 / K=2 CRM a | crm-always-on-object-s42, crm-always-on-object-s43, crm-always-on-object-s44, crm-always-on-spatial-s42, crm-always-on-spatial-s43, crm-always-on-spatial-s44, crm-always-on-goal-s42, crm-always-on-goal-s43, crm-always-on-goal-s44 |





