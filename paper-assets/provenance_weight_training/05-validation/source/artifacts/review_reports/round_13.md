---
round: 13
review_mode: fresh
overall_score: 3.0 — Findings
timestamp: 2026-05-25T05:02:49.813508+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 13 (Fresh Review)

**论文**: When Does Detect-and-Reweight Work for Synthetic Contamination?
**Venue**: EMNLP 2026 (via ACL Rolling Review, May 2026 cycle)
**Reviewers**: R1（方法严谨性 + 实验设计）, R2（新颖性 + 论文完整性 + 格式合规）
**审稿模式**: Fresh（重新审稿，无上轮记忆）

---

## Summary

本文通过 Qwen3-0.6B 的 controlled continued pretraining 实验（132M FineWeb tokens, 40% self-contamination, 5 seeds），研究 detect-and-reweight (D&R) 方法的有效条件。核心发现三项：(1) 已发表 D&R 评估受 multi-epoch exposure 混淆，epoch-matched 后 >95% 优势消失；(2) detector 需同时具备 AUC≥0.9 和 ECE≤0.05；(3) minimum intervention 原则优于 unconstrained weight maximization。论文提出 dual-constrained adaptive b* 作为示例应用。

两位 Reviewer 独立给出完全一致的评分（Overall 3.0 / Soundness 3.5 / Excitement 2.5 / Reproducibility 4 / Confidence 4），交叉回应后高度收敛，仅在方法新颖性水平（R1: 中偏低 vs R2: 低）和 N2 严重度（R1: critical vs R2: should-fix）上存在 minor 分歧。

---

## Strengths

**S1** [共识] **Epoch confound 发现是最强贡献**。Table 2 和 Figure 1(a) 清晰展示 D&R 在 epoch-matched controls 下优势从 Δ≈-1.1 缩减至 Δ≈-0.017。实验设计简洁有效，对 data curation 社区有实际预警价值。

**S2** [共识] **实验方法论严谨**。5 seeds + Bonferroni-Holm correction；ablation hierarchy (Adaptive > Uniform > ESS-only > Random > Permuted) 逻辑清晰；控制组设计周全（Permuted 破坏信号保留非均匀性，Random 使用随机权重，ESS-only 最大化 b）。

**S3** [共识] **诚实的 framing**。论文将方法定位为 "an illustrative application"（Abstract），Limitations 对 scope 限定负责任。

**S4** [R2] **Constraint regime 分析**（Figure 7）有实践洞察价值：ρ=0.4 时 ~59% batches clean，~40% ESS-binding，介入范围可预测。R1 交叉回应补充认同。

**S5** [共识] **写作和视觉密度**。8 页正文含 7 figures + 5 tables，每个有明确目的。Propositions 1-2 数学正确，Algorithm 1 实现清晰。

---

## Weaknesses

### Must-Fix

**MF1** [共识, R1-N1 + R2-W2+W5] **核心效应无实际意义且不迁移至下游任务**

Adaptive b* 的 PPL 改善仅 0.13% relative（Δ=−0.023），5 个下游基准 Δ 全在标准误内（accuracy 均 0.5414）。然而论文在三处使用 practitioner 导向表述（§5.1 "For practitioners"、§6 Table 5 "Decision summary for practitioners"、§7 "For practitioners, reweighting is worthwhile"），Abstract 说 "improves over uniform training" 未限定 PPL-only。

R1 补充：Cohen's d=3.83 被 deterministic data ordering 人为放大（σ=0.006，5 个 seed 仅改变模型初始化，data order 固定）——如果 data shuffle seed 也随机化，paired SD 大概率升高，Cohen's d 大幅缩水。

**建议**：(a) Abstract/Conclusion 明确限定 "improves held-out PPL"；(b) 在 main text 讨论下游 null result（而非仅 Appendix I）；(c) 考虑重新定位为 analysis paper with negative practical result at current scales。

**MF2** [R2-W1, R1 AGREE] **标题通用性远超实验 scope**

标题 "When Does D&R Work?" 暗示一般性回答，但实验受限于 self-contamination / 0.6B 单一模型 / continued pretraining / 单一数据源。关键矛盾：最强贡献（epoch confound）在 from-scratch pretraining 下不适用（§6 自述 "invisible in Drayson et al. because from-scratch pretraining rarely completes even one epoch"）——即该发现对最常见的 pretraining 设定无意义，但标题未反映这一关键 scope 限定。

**建议**：标题应更具体反映 scope，如 "When Does Detect-and-Reweight Work? An Analysis under Self-Contamination in Continued Pretraining"。

### Should-Fix

**SF1** [R1-N2, R2 AGREE（降为 should-fix）] **α_eff proxy 与 Wang (2026) 理论保证之间的逻辑断裂**

Wang (2026) 要求 true real fraction ≥ τ，但论文用 α_eff 替代（R²≈0.63）。~37% 未解释方差意味着部分 α_eff ≥ τ 的 batch 真实 real fraction 可能 < τ，理论保证不成立。§3 中 "guarantees a convergence-rate lower bound" 措辞在技术上不准确。n_min 缓冲是 heuristic 而非 principled correction。

R2 建议降为 should-fix：论文核心贡献是 empirical findings 不是理论保证，修改 "guarantees" 措辞即可消除误导。圆桌采纳此判断。

**建议**：将 "guarantees" 改为 "targets/approximates"；量化 α_eff ≥ τ 但 true fraction < τ 的 batch 比例。

**SF2** [R1-W1, R2 AGREE] **Grid-best b=0.3 vs adaptive b*≈0.9 偏差未解释**

Grid search 最优 b=0.3 而 adaptive 产生 b*≈0.9，差异 3×。因果链：α_eff 负偏差（Table 12, bias≈−0.03）→ quality floor 过早绑定 → b_τ 被推高 → adaptive b* 远高于 post-hoc 最优。方法实际行为偏离 "minimum intervention" 设计意图。与 SF1 构成闭环。

**建议**：补充 per-batch b* 分布（median, percentiles）；分析 debiased α_eff 的效果。

**SF3** [R1-W2, R2 AGREE] **缺少 "uniform + multi-epoch" 基线**

Epoch confound 分析缺少关键对照：对全部数据做 multi-epoch uniform training（~3.2 epochs，等量 compute），以区分纯重复 vs 选择性重复的效果。计算成本低但对分析完整性至关重要。

**SF4** [R2-W3, R1 partial REBUT] **方法新颖性有限**

w=(1−q)^b 完全来自 Drayson et al.，dual constraint + bisection 是标准方法组合。R1 认为组合在此问题上是新的且分析贡献不依赖算法新颖性（评 "中偏低"）；R2 认为方法新颖性低。圆桌结论：中偏低，论文应在 Introduction 早期更明确 analysis paper 定位。

**SF5** [R2-W4 + R1 AGREE] **Detector 覆盖面极窄**

仅 3 个 detector（TF-IDF+LR, GPT-2 perplexity, N-gram），缺少 neural detectors。3 个数据点不足以得出 AUC/ECE threshold 通用规律。

**建议**：扩展至少 1 个 neural detector，或将 threshold 标注为 "observed in our 3 detectors"。

**SF6** [R1-W3 + R2-Q5] **1.7B 规模效应递减 43% 未正式讨论**

0.6B→1.7B Δ 从 −0.023 缩至 −0.013（43% 递减），OOD 方向不一致。如果 trend 成立，方法在 practitioner 关注的 7B+ 规模可能完全失效。

**建议**：正式讨论 scaling trend，在 Table 5 或 Conclusion 加 scale caveat。

**SF7** [R1-W5 + R2-W6] **Self-contamination 生态效度有限**

Self-contamination 对 detector 最有利。Cross-model 结果（Llama-3.2-3B）仅单 seed 无 PPL，反而暴露 generalization 困难。

**SF8** [R1-W4, R2 AGREE（较低严重度）] **B=4 是最弱设置却用于主实验**

B=4 时 MAE=0.114，advantage 最小（1.0×）。B=16 时 advantage 放大 3.0×。R2 认为 conservative reporting 有合理性，但应至少在 B=16 下重复核心对比并报告下游。

### Minor

- **m1** [R2-W7] ρ≥0.4 实用门槛偏高，适用场景极窄
- **m2** [R2-W8, R1 AGREE] PPL-capability 关系未讨论
- **m3** [R1-M1] Permuted q-scores 仅 1 seed
- **m4** [R1-M2] ρ=0.6 p_BH=0.064 措辞需明确标为 "not significant after correction"
- **m5** [R1-M3] Table 5 "Generator ≠ trainee" 应考虑标为必要条件
- **m6** [R1-M4 + R2] Cohen's d=3.83 解读需注意 deterministic ordering 对 paired SD 的影响
- **m7** [R2] §6 Discussion 第一段与 §5.1 epoch confound 内容重复

---

## Questions

**Q1** [共识]: 下游任务零改善下，方法推荐用于什么实际场景？
**Q2** [共识]: GPT-4/Claude 级 synthetic data 下 detector 性能如何？AUC/ECE guidance 在更广 detector sweep 下是否稳健？
**Q3** [R1]: α_eff 负偏差是否导致 b* 系统偏高？Debiased α_eff 效果如何？
**Q4** [共识]: 为何选 B=4 而非 B=8/16 作主实验配置？
**Q5** [R2]: τ=0.7 是否有 principled 选择方法？Per-batch bisection 的 b* variance 对 gradient noise 的影响？
**Q6** [R2]: 1.7B 规模 benefit 缩减至 Δ≈−0.013，方法在 7B+ 是否完全失效？

---

## Missing References

- **RAID benchmark** (Dugan et al., 2024): AI text detection benchmark，覆盖多种 generator/domain [R2 提出, R1 AGREE]
- **M4 shared task** (Wang et al., 2024): 多语言多生成器检测 benchmark [R2 提出, R1 AGREE]

---

## External Review

**状态**：未请求。

---

## Visual Layout Check（非评分项）

**状态**：完成（0 critical, 1 warning, 10 info）

- **[warning]** Page 6 含 4 个 display items（Figure 4 + Tables 2, 3, 4），视觉密度极高。建议将 Table 4 移至 appendix。
- **[info]** Figure 1 legend 字号偏小，建议增大。
- **[info]** Figure 2 绿色半透明区域灰度打印下可能不够显眼，建议加阴影线。
- **[info]** Figure 9 axis label/legend 字号约正文 60-65%，接近可读性下限。
- **[info]** 格式合规：Abstract ~155 words（≤200 ✓），正文 8 页内（≤8 ✓），Limitations 段 3 点简短（✓），References 格式统一无 [?]（✓）。

---

## Overall Assessment

**Overall: 3.0 — Findings**

| 维度 | R1 | R2 | 合并 |
|------|----|----|------|
| Soundness | 3.5 | 3.5 | **3.5** |
| Excitement | 2.5 | 2.5 | **2.5** |
| Reproducibility | 4.0 | 4.0 | **4.0** |
| Confidence | 4.0 | 4.0 | **4.0** |
| **Overall** | **3.0** | **3.0** | **3.0** |

**核心判断**：论文实验方法论严谨，epoch confound 发现（F1）对社区有预警价值，写作诚实且 self-aware。但以下问题限制其影响力：

1. **效果量极小且零下游改善**（MF1）：0.13% PPL 改善不传导至任何下游任务，practitioner 导向 framing 缺乏支撑
2. **标题与 scope 严重不匹配**（MF2）：最强贡献 F1 在 from-scratch pretraining 下不适用，但标题暗示通用性
3. **α_eff proxy 理论断裂**（SF1）：与 Wang (2026) 理论保证不直接对应，导致 b* 系统偏高（SF2）
4. **方法新颖性有限**（SF4）：建立在 Drayson et al. 基础上的标准优化应用
5. **实验范围窄**：仅 self-contamination + 0.6B + continued pretraining + 3 detectors，规模递减趋势不利

**达到 Conference 水平需要**：
(a) 扩展 detector 覆盖（含 neural detectors）
(b) 在至少一个下游任务或更大 batch size 下展示改善，或明确重新定位为 negative result
(c) 补充 uniform+multi-epoch baseline 完善 epoch confound 分析
(d) 修改标题反映 scope 限定

论文作为 focused empirical analysis 适合 Findings 接收。

---

## Detailed Comments

### 交叉回应共识总结

| 问题 | R1→R2 | R2→R1 | 共识 |
|------|-------|-------|------|
| 核心效应小+零下游 | AGREE | AGREE | ✅ Must-fix |
| 标题 scope 不匹配 | AGREE（更精准） | — | ✅ Must-fix |
| α_eff 理论断裂 | — | AGREE（降为 SF） | ✅ Should-fix |
| Grid-best vs b* 偏差 | — | AGREE | ✅ Should-fix |
| 缺 multi-epoch baseline | — | AGREE | ✅ Should-fix |
| 方法新颖性 | REBUT（中 vs 低） | — | ⚠️ Minor 分歧 |
| Detector 覆盖窄 | AGREE | AGREE | ✅ Should-fix |
| Self-contamination 生态效度 | AGREE | AGREE | ✅ Should-fix |
| 规模递减 | AGREE | AGREE | ✅ Should-fix |
| B=4 最弱设置 | — | AGREE（较低严重度） | ✅ Should-fix |
| ρ≥0.4 门槛偏高 | AGREE | — | ✅ Minor |
| PPL-capability 关系 | AGREE | — | ✅ Minor |
| τ 选择 principled? | — | REBUT（已有 sweep） | ✅ 已回应 |

### Issue Tracker 跨轮次状态

本轮独立发现的问题与 Round 11-12 高度重叠，确认以下为结构性问题（4 轮连续被指出）：
- R11-C1: 统计检验力（已 in_progress，补 seed 中）
- R11-C2: α_eff proxy 可靠性（本轮从 critical 降为 should-fix）
- R11-C3: 下游零改善 + practitioner framing 矛盾
- R11-C4: 实验范围过窄 / 标题通用性

新增问题（Round 13 首次提出）：
- R13-W2: Grid-best b=0.3 vs adaptive b*≈0.9 偏差
- R13-W3: 1.7B 规模效应递减 43% 未正式讨论
- R13-W4: ρ≥0.4 门槛偏高
- R13-m2: Cohen's d 被 deterministic data ordering 放大
- R13-m3: PPL-capability 关系未讨论
