---
round: 34
review_mode: continue
overall_score: 3.5 — Borderline Conference
timestamp: 2026-05-20T17:35:58.130616+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Round 34 审稿报告（继续审稿）

**论文**: Depth Fingerprinting: Detecting Recursive Generation Depth in LLM Text Chains
**目标 Venue**: EMNLP 2026 (ARR Long Paper)
**审稿模式**: Continue（基于 Round 33 的修订验证）
**Reviewer**: R1（方法严谨性 + 统计验证）、R2（新颖性 + 完整性 + 写作）

---

## Summary

本轮为修订验证审稿，基于 Round 33 提出的 11 个 in_progress issue 逐条检查论文修改情况。论文在 framing 层面做了实质性改进：DDR partition 从"经验发现"重新定位为"数据驱动聚类 (k=2, silhouette=0.632)"；分类器从"主要贡献"降级为"proof-of-concept"；entropy_min 和 tail_decay 被诚实标注为"boundary feature"；基线比较增加了公平性说明；novelty framing 从"DDR 本身"转向"what converges vs what is preserved"的分析视角。这些修改有效回应了 Round 33 的核心批评。

**11 个 issue 验证结果**: 10 RESOLVED, 1 STILL_OPEN (minor)

---

## Strengths

1. **Framing 改进到位**: 将 DDR partition 锚定在 k=2 聚类 (silhouette=0.632) 上，3/1/3 细分明确标注为 domain-informed refinement，解决了 post-hoc 质疑。
2. **诚实的 proof-of-concept 定位**: Introduction L14 "As a proof of concept"、Discussion L11 "~30% error rate" 不再过度宣称分类性能。
3. **Boundary feature 透明处理**: entropy_min (|ρ|=0.40 pooled but d=0.016 gen-1/gen-2+) 和 tail_decay (4/8 TOST) 的边界性质被充分披露。
4. **Novelty 重新定位**: "what converges vs what is preserved" 的分析框架与 broken_telephone、markovian_chains 形成互补而非重复。
5. **基线比较公平性**: 承认 4-det+surface (0.708) > 7-feature (0.705)，不再隐藏对自身不利的结果。
6. **Limitations 全面**: base-model scope、scale boundary、temperature sensitivity、prompt-type dependency 均有充分讨论。

---

## Weaknesses

### 仍然存在的结构性限制（非修改可解决）

1. **[Major] Base-model-only scope 限制泛化价值**: instruct model F1 降至 0.338-0.667，而实际 web text 主要由 instruct/RLHF 模型生成。论文已在 Limitations 中充分讨论，但这仍是制约会议级接收的核心短板。Reviewer 共识：这是 scope limitation 而非 fatal flaw，论文对此的诚实讨论是加分项。

2. **[Major] 分类性能天花板**: Binary F1=0.694 (LOGO) 在检测任务中偏低。proof-of-concept 定位缓解了期望落差，但限制了方法的实际影响力。

3. **[Minor] QLoRA gap 未充分解释**: end-to-end F1=0.905 (+11.6pp) 说明 7 个手工特征丢失了大量信号，但论文未深入分析这些信号是什么，错失了 insight 机会。

### 未修复的遗留问题

4. **[Minor] Wang et al. (ACL 2025) 引用缺失**: "Unveiling Attractor Cycles in LLMs" (ACL Anthology: 2025.acl-long.624) 应加入 §2.2 Related Work，与 markovian_chains 的 attractor dynamics 讨论直接相关。（R29-W6，跨 3 轮未修复）

---

## Questions

1. 是否考虑过将 entropy_min 从 near-stationary 组移至独立的 "boundary" 类别，使 DDR 成为 4-way partition？当前 3/1/3 中 entropy_min 归入 near-stationary 但 pooled |ρ|=0.40 明显偏高。
2. QLoRA +11.6pp 的增益来源是否可通过 attention pattern 或 feature importance 分析进一步拆解？

---

## Missing References

- **Wang et al. (ACL 2025)**: "Unveiling Attractor Cycles in LLMs" — 直接相关于 §2.2 attractor dynamics 讨论。(2025.acl-long.624, arXiv: 2502.15208)

---

## External Review

未启用外部审稿。

---

## Visual Layout Check

**状态**: 已完成

关键发现：
- **[Critical]** Pages 1-4（Introduction 至 Method 前半）无任何 display item（图/表），纯文字密度过高，建议前移 Figure 1 或增加早期可视化
- **[Warning]** 6 项排版警告（含图表位置、空白分布等）
- **[Info]** 9 项信息提示

视觉审查为非评分项，仅供参考。

---

## Overall Assessment

**评分: 3.5 — Borderline Conference**

**评分依据**:

Round 33 → Round 34 提升 0.5 分的理由：
- DDR partition 从 post-hoc 标签升级为 data-driven clustering (k=2)，方法论严谨性显著改善
- proof-of-concept 定位消除了性能过度宣称的问题
- boundary feature 透明标注体现了科学诚实
- novelty framing ("what converges vs what is preserved") 与相关工作形成清晰区分

未达 4.0 (Conference) 的理由：
- base-model-only scope 严重限制实际应用价值，web text 场景无法直接使用
- Binary F1=0.694 作为 proof-of-concept 可接受，但缺乏通向 deployable system 的路径
- DDR 作为分析框架的 novelty 中等——location drift 在 model collapse 文献中已有充分记录，shape preservation 是新贡献但效果有限
- QLoRA gap 暗示手工特征设计的上限较低，削弱了特征工程贡献的价值

**Reviewer 共识**: 两位 Reviewer 均从 Round 33 的 3.0 上调至 3.5，认可修改的实质性但维持对 scope 和性能的保留意见。交叉讨论中两个分歧点（TOST power analysis 必要性、QLoRA gap 严重程度）已达成共识。

**建议**: Borderline Conference / Strong Findings。论文作为 empirical analysis 贡献了有价值的分析视角，但 scope 限制和性能天花板制约了主会议接收。若能在 camera-ready 前补充 instruct model 的初步分析路径或 QLoRA 信号分解，将增强 Conference 接收的论据。

---

## Detailed Comments

### Issue Tracker 验证结果（11 项）

| Issue ID | 问题 | 状态 | 说明 |
|----------|------|------|------|
| R33-W1 | Base-model scope framing | ✅ RESOLVED | Limitations 充分讨论，abstract/intro 加入 scope qualifier |
| R33-W2 | DDR novelty vs diversity loss | ✅ RESOLVED | "what converges vs preserved" 框架与 concurrent work 区分 |
| R33-W3 | 3/1/3 partition post-hoc | ✅ RESOLVED | k=2 (silhouette=0.632) 为 primary，3/1/3 为 refinement |
| R33-W4 | entropy_min 分类矛盾 | ✅ RESOLVED | 标注为 "boundary feature"，|ρ|=0.40 但 d=0.016 |
| R33-W5 | tail_decay TOST borderline | ✅ RESOLVED | 4/8 pass rate 明确报告 |
| R33-W6 | F1=0.694 proof-of-concept | ✅ RESOLVED | "proof of concept" + "~30% error rate" 定位 |
| R33-W7 | Downstream null result | ✅ RESOLVED | 降级处理，不作为主要贡献 |
| R33-W8 | QLoRA gap 解释 | ✅ RESOLVED | 承认 gap 存在，框架为 "richer representations" |
| R33-W9 | Baseline unfairness | ✅ RESOLVED | 承认 4-det+surface > 7-feature |
| R33-W10 | TOST power analysis | ✅ RESOLVED | Reviewer 共识：sensitivity analysis 足够 |
| R29-W6 | Wang et al. reference | ❌ STILL_OPEN | 跨 3 轮未添加，minor |

### 跨轮趋势

- Round 29-32: 初始投稿，多轮修改建立基本框架
- Round 33: 全面重审，识别 5 Critical + 7 Major + 9 Minor，评分 3.0
- Round 34: 修订验证，10/11 resolved，评分 3.5（+0.5）

论文在 framing 和诚实度上持续改善，但 scope (base-model-only) 和 performance (F1=0.694) 的结构性限制非短期修改可解决。