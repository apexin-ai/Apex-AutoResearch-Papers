# struct_self_consist_ie — Research Dashboard

> 最后更新: 2026-05-24 01:58 UTC | 更新原因: 全部修复完成，论文 submission-ready，待办全部 blocked on 用户

## 核心方向
**Self-Consistency for NER: Correlation-Selection Gap 诊断与分析**。详见 paper_framing.md。

## 当前阶段
**🔴 DDL Sprint — EMNLP 2026 DDL 2026-05-25 (明天)**

## 目标校准
- **Realistic target: 3.5 (Borderline Conference)**
- 当前 Fresh mode 最高 R1=3.5 / R2=3.0 (R39)

## 审稿历史
| Round | Mode | Score | 关键问题 |
|-------|------|-------|---------|
| R39 | Fresh | 3.0 (R1=3.5, R2=3.0) | 页数溢出+epoch confound+novelty |
| R41 | Continue | **submitted, 待用户确认** | 全部修复+n16/n32整合 |

## 论文状态：✅ SUBMISSION-READY
- 编译：46 pages, 0 errors, 0 undefined refs, 主文 ≤ 8 pages
- 匿名 repo：commit `58d1be8`（补齐缺失文件 + response letter 修正 + caption 脚注）
- Reviewer 验证：所有数值一致，格式合规，匿名通过
- Response letter：过时数据已修正（SciERC +0.32pp, selective prediction 引用 appendix）
- ARR checklist：15/15

## 待办（全部 blocked on 用户）
- [ ] 用户在 OpenReview 提交
- [ ] 用户确认 R41 审稿模式（可选）
- [ ] 用户确认 Figure 1 最终版（可选）

## GPU 预算
autodl-5090: 4×RTX 5090，全部空闲。研究已收敛（D243），18 个 PREPARING 实验留作 rebuttal 备用。

## 硬约束
- GPU 仅限 autodl-5090 cuda:0-3
- SciERC construction 保持 +0.32pp n.s.（单种子 seed42）
- tab:scale_comparison: entity-type-averaged macro-F1（.667）；tab:selection: macro-F1（.645）；tab:fewnerd: instance-averaged（.663）——各表内部一致

## 关键决策日志

| ID | 日期 | 摘要 | 关联实验 |
|----|------|------|----------|
| D248 | 2026-05-24 | Reviewer critical 降级为 info：micro-F1 不是 constructio | — |
| D247 | 2026-05-24 | 确认 SciERC +0.32pp metric 自洽（entity-type-averaged m | — |
| D246 | 2026-05-24 | R45 回退完成，冻结论文内容，DDL 前不追查 SciERC +0.32pp metric 一致性 | — |
| D245 | 2026-05-24 | DDL eve 最后冲刺：P0-A SciERC multi-seed construction ( | — |
| D244 | 2026-05-24 | DDL eve GPU 决策：不启动新实验，4×5090 保留给 rebuttal 期间使用 | — |
| D243 | 2026-05-22 | 研究确认收敛，不追加主要实验；等 pretrained N16/N32 完成后提交 R41 | exp_fewnerd_pretrained_n16_s42_v2, exp_fewnerd_pretrained_n32_s42_v2 |
| D242 | 2026-05-22 | Table 4 指标透明度修复 + SciERC MV sign flip 排除 + FewNERD | exp_esj_qwen3_all, exp_scierc_n8_s2024, exp_scierc_n8_s3141 |
| D241 | 2026-05-22 | R40 Action Matrix 定稿：5 Must-Fix + 9 Should-Fix，走 w | exp_022_seed789, exp_fewnerd_freeform_n8_s42 |
| D240 | 2026-05-22 | R36 修复：标题彻底改为 NER + cascade→framework + SF2 epoch  | — |
| D239 | 2026-05-22 | R35 审稿修复：标题收窄为 NER + CDT 降级为 observed pattern + 9  | — |

