---
round: 10
review_mode: continue
overall_score: 6/10 marginally above acceptance threshold
timestamp: 2026-05-19T06:31:56.007476+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Round 11 (Continue) 审稿报告

**论文**: Vision Encodes, Language Routes: Token-Level Functional Specialization in a Vision-Language-Action Model
**Venue**: CoRL 2026 (deadline 2026-05-29)
**模式**: Continue（基于 Round 10 报告中 5 个 in_progress issues 的增量评估）
**日期**: 2026-05-19
**Reviewers**: R1（增量评估执行）、R2（Round 10 评估结论沿用，本轮变更过小无需独立重审）

---

## Summary

论文根据 Round 10 报告中 5 个 in_progress issues 进行了针对性的句子级修改。变更范围极小（5-6 句话），仅安排 R1 进行增量评估。R1 逐条评估后判定全部 5 个 issues RESOLVED，无 regression，无新问题引入。R2 的 Round 10 评估（6/10）作为基线沿用，本轮修改不涉及 R2 此前标记为 RESOLVED 的任何 issue，故无需独立重审。

至此，Round 9 提出的 13 个原始 issues + 1 个 Round 10 新增 issue 中：
- **11 个 RESOLVED**（含本轮新增 5 个：R9-N4、R9-N6、R9-W1、R9-I2、R10-Q1）
- **2 个 wont_fix**（R9-N1 单模型、R9-N2 无闭环——residual scope limitations，需 rebuttal 应对）
- **0 个 open/in_progress**

论文在其 scope 内（单模型 representational analysis）已无未解决的方法论或 framing 问题。

---

## 本轮修改评估（R1 执行）

| Issue | 修改内容 | R1 评估 |
|-------|---------|---------|
| R9-N4 Random R² > instruction R² | Discussion: "unstructured perturbation releases probe capacity without disrupting organized computation" | **RESOLVED** — information-computation dissociation 闭环完成 |
| R9-N6 Power limitation 声明 | §4.4: "N=10 limits statistical power; n.s. should not be interpreted as evidence of absence" | **RESOLVED** — 标准统计学表述，位置恰当 |
| R9-W1 Deployment implication | Discussion: "L1 attention entropy could monitor under-attention to instructions at runtime" | **RESOLVED** — 具体 actionable implication，hedging 恰当 |
| R9-I2 Häon et al. 互补 | Discussion: "Our routing (where) complements Häon et al.'s (what is encoded)" | **RESOLVED** — where/what 正交互补，嵌入 Limitations 段落长度恰当 |
| R10-Q1 Per-task MSE | Appendix: "all |ΔMSE| < 3%, all p > 0.27; uniformly small, not cancellation" | **RESOLVED** — 排除 cancellation，定量证据充分 |

**R2 沿用**: R2 在 Round 10 评估中对上述 issues 的 PARTIALLY_RESOLVED / in_progress 判断与 R1 一致。本轮修改精确回应了两位 Reviewer 共识指出的残留问题。

---

## Remaining Issues (wont_fix, rebuttal 应对)

1. **[R9-N1] 单模型范围**: OpenVLA-7B only。建议 rebuttal 强调：causal mask 架构约束的普遍性 + Discussion 中三个可测试预测 + LIBERO-Goal/Spatial 双 benchmark 验证。
2. **[R9-N2] 无闭环验证**: Open-loop only。建议 rebuttal 强调：open-loop 三角验证（MSE + d + Jaccard）的独立方法论价值 + 分析论文的 CoRL 先例。

---

## Overall Assessment

| Reviewer | R9 | R10 | R11 | Change |
|----------|-----|------|------|--------|
| R1       | 5   | 6    | 6    | 维持   |
| R2       | 5   | 6    | 6*   | 沿用   |
| **Consensus** | **5** | **6** | **6** | **维持** |

*R2 未执行独立 Round 11 评估；基于变更范围判断其 Round 10 评分不受影响。

### 6/10 — Marginally above acceptance threshold

本轮微调将所有 warning/info 级残留问题清零，论文在方法严谨性维度达到完备状态。评分不变的原因是两个 scope limitations 无法通过文字修改解决。

论文当前状态：
- **方法论**: Sound。统计报告 honest，controls 充分，claims well-calibrated，所有方法论 issues 已闭环
- **叙事**: 连贯。C1→C2→C3 层次分明，hedging 全文一致
- **Scope**: 有限。单模型 + open-loop 限制通用性和 robotics impact
- **CoRL fit**: Borderline。取决于 AC 对 pure analysis papers 的接受度

两位 Reviewer 在 Round 10 均表示：如果 rebuttal 能提供 RT-2 attention profile 对比、layer-pruning success rate、或 routing integrity vs task success 相关性中的任一项，愿意向 7 移动。

**Confidence: 4/5**