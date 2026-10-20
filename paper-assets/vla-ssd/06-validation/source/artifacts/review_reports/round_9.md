---
round: 9
review_mode: continue
overall_score: 6/10 marginally above acceptance threshold
timestamp: 2026-05-19T06:09:13.944216+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: True
---

# Round 10 (Continue) 审稿报告

**论文**: Vision Encodes, Language Routes: Token-Level Functional Specialization in a Vision-Language-Action Model
**Venue**: CoRL 2026 (deadline 2026-05-29)
**模式**: Continue（基于 Round 9 意见的修订评估）
**日期**: 2026-05-19
**Reviewers**: R1, R2（2 轮：独立评审 + 交叉分享，共识充分）

---

## Summary

论文根据 Round 9 审稿意见进行了实质性修改。修订有效解决了大部分方法论和 framing 问题，包括 C1 降权、"causal" 术语修正、counterfactual 的 Jaccard 重构、N=10 hedging、新增 MSE ground-truth 分析、trajectory-level Cohen's d、expanded specificity controls 和 leave-one-out task sensitivity 分析。论文现在是一篇 claims well-calibrated 的分析工作。两个 critical scope 限制（单模型、无闭环验证）仍然存在，但已非修订周期内可解决的问题。

---

## Strengths

1. **修订响应性强**: 13 个 Round 9 issues 中，6 个 RESOLVED，3 个 PARTIALLY_RESOLVED，仅 2 个 STILL_OPEN（均为 scope 限制）
2. **MSE ground-truth 分析** (Appendix): 消融后 MSE 不变 (ΔMSE = -0.001, p = 0.52) 建立了 R² ↑ + trajectory change + MSE 不变 的三角关系，支持 "information-computation dissociation" 框架——这是一个新颖且有信息量的机制发现
3. **Counterfactual Jaccard 分析**: 从含糊的 "semantic distance" 到可量化的 "token novelty (1 - Jaccard) perfectly predicts ordering (ρ = 1.0)"，质的提升。VLA 对 token identity 比 semantics 更敏感的发现本身是有趣的 observation
4. **Claims 一致 well-calibrated**: "primarily"、"limited"、N=10 qualifier 等 hedging 全文一致化，reader 不会被 mislead
5. **C1 降权到位**: Abstract 末句 sanity check、Introduction 末位、Contribution (iii) framework 下，与其贡献度匹配
6. **Task-dependent routing with LOO**: 所有 leave-one-out p ≤ 0.083，无单一任务驱动效应——从 "all tasks show routing" 升级为 "routing matters more when instruction is needed"
7. **Per-token attention normalization**: 38.2× text-to-image ratio 有效回应 token-count imbalance
8. **Expanded specificity controls**: 四组 matched-size 比较（instruction > random > image-dominant > bottom-24）优于原两组

---

## Weaknesses

### Critical (unchanged scope limitations)

1. **[R9-N1] 单模型范围** (STILL_OPEN): 仅分析 OpenVLA-7B，无法判断 L1 routing 是该模型特性还是 VLA 通用机制。Discussion 对 π₀、RT-2、Octo 的三个预测仍为猜测，无新实验验证。共识降为 residual scope limitation。

2. **[R9-N2] 无闭环验证** (STILL_OPEN): 所有分析 open-loop，routing 发现对 robot learning practice 的价值仍为推测。缺少 layer-pruning task success 评估或 routing integrity vs success rate 相关性。共识降为 residual scope limitation。

### Warning (partially resolved)

3. **[R9-N4] Ablation R² paradox** (PARTIALLY_RESOLVED, severity critical→minor): MSE 证据 + information-computation dissociation 框架实质性缓解。但 random 24 heads 的 R² 增加大于 instruction-dominant 24 heads (+0.077 vs +0.042) 的机制未充分解释——"structured noise for the probe" 措辞与 "routing signal 是功能性的" 核心叙事存在语义张力。

4. **[R9-W1] CoRL scope fit** (PARTIALLY_RESOLVED): 新增 deployment monitoring 和 activation steering 讨论使 robotics 连接更具体，但仍为 speculative。从 "完全不相关" 升级为 "边界但有连接"。

5. **[R9-W6] Specificity control** (PARTIALLY_RESOLVED): d ratio 降至 1.08×（更诚实），四组对照梯度方向正确，但 gap 很小。论文 "distributed, attention-graded routing" framing 与数据一致，但不能声称 strong specificity。

### Minor disagreement

6. **[R9-N6] N=10 power limitation 表述**: R1 认为主文需一句明确 power limitation 声明；R2 认为当前 hedging + LIBERO-Spatial 对冲已足够。不影响评分。

### Info

7. **[R9-I2] Häon et al. 互补关系** (PARTIALLY_RESOLVED): 两类机制（L1 attention routing vs sparse semantic directions）的关系未分析。1-2 句连接分析即可。

---

## Questions for Rebuttal

1. 消融后 MSE 不变是否存在 task-level cancellation？可否提供 per-task MSE breakdown？
2. Specificity d ratio 1.08× 意味着 any 24 heads at L1 产生类似效果——instruction-attention fraction 作为 predictor 的增量 value 是什么？
3. Random-subset ablation R² 增加 > instruction-dominant ablation (+0.077 vs +0.042)——如何解释 structured routing signal 对 probe 干扰更小？

---

## Missing References

无新缺失引用。Round 9 提出的 Octo 已补。

---

## Overall Assessment

| Reviewer | R9 Score | R10 Score | Change |
|----------|----------|-----------|--------|
| R1       | 5/10     | 6/10      | +1     |
| R2       | 5/10     | 6/10      | +1     |
| **Consensus** | **5/10** | **6/10** | **+1** |

### 6/10 — Marginally above acceptance threshold

修订有效回应了大部分 Round 9 issues（6 RESOLVED, 3 PARTIALLY_RESOLVED），论文的方法论严谨性和叙事连贯性显著提升。新增的 MSE 证据、trajectory-level d、Jaccard 分析和 expanded controls 是实质性改进。Claims 现在 well-calibrated。

阻止更高评分的根本原因是两个 unchanged scope limitations：(1) 单模型范围使结论通用性不可评估；(2) 无闭环验证使 robotics impact 为推测。对 CoRL 社区，这两点限制了论文的 significance 和 relevance。

Borderline accept/reject 的决定性因素：AC 对 "pure analysis paper at CoRL" 的容忍度，以及 rebuttal 能否提供额外实验证据。如果 rebuttal 能提供以下任一项，两位 Reviewer 均表示愿意向 7 移动：
- RT-2 或其他 VLA 的 attention profile 对比（验证 L1 routing 通用性）
- Layer-pruning + LIBERO success rate（建立 routing → task performance 连接）
- Routing integrity vs task success 相关性

**Confidence: 4/5** (两位 Reviewer 评分和判断完全一致)

---

## Issue Resolution Summary

| Issue | Severity | R10 Status |
|-------|----------|------------|
| R9-N1 单模型 | critical | STILL_OPEN (residual) |
| R9-N2 无闭环 | critical | STILL_OPEN (residual) |
| R9-N3 Causal术语 | warning | RESOLVED |
| R9-N4 Ablation R² | warning | PARTIAL (minor) |
| R9-N5 Counterfactual | warning | RESOLVED |
| R9-N6 N=10 hedging | warning | RESOLVED* |
| R9-W1 CoRL scope | warning | PARTIAL |
| R9-W2 C1 占比 | warning | RESOLVED |
| R9-W3 Vision framing | warning | RESOLVED |
| R9-W4 Cohen's d | warning | RESOLVED |
| R9-W5 Llama-2 bias | warning | RESOLVED |
| R9-W6 Specificity | warning | PARTIAL |
| R9-W7 N=63,228 | warning | RESOLVED |
| R9-I1 Octo引用 | info | RESOLVED |
| R9-I2 Häon关系 | info | PARTIAL |
| R9-I3 小问题 | info | PARTIAL |

*R1 认为 PARTIALLY_RESOLVED，R2 认为 RESOLVED，minor disagreement