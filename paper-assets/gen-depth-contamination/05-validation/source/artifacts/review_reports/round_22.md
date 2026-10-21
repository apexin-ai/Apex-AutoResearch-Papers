---
round: 22
review_mode: fresh
overall_score: 3.5 - Borderline Conference
timestamp: 2026-05-20T16:15:04.662659+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告：Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary

**Venue**: EMNLP 2026 (ARR May 2026)  |  **Deadline**: 2026-05-25  |  **Round**: 1 (Fresh Review)
**Reviewers**: R1 (方法论 + 实验严谨性), R2 (新颖性 + 完整性 + 写作)
**格式确认**: Long paper, 正文 8 页 ✓, ACL 2026 review 模板 ✓, Double-blind ✓

---

## Summary

本文提出 generational depth estimation 框架，定义 discrimination boundary K* 为统计分类器能可靠区分相邻生成深度的最大深度。使用 15 维 surprisal 统计特征配合 OBD-LightGBM 分类器，在 10 种模型配置（6 个架构家族，≤14B）、4 个域（C4, Wikipedia, arXiv, Code）上系统测量 K*。核心发现：web text 的 K*=2（θ=0.60），域排序 arXiv(3) > C4(2) = Code(2) > Wikipedia(1) 跨模型稳定，跨模型迁移在聚合层面保留 80-92% 但边界级别脆弱（4/6 off-diagonal 7B pairs fall below θ），fine-tuned DeBERTa 可将 K* 推高至 3-4（域依赖的 feature-set-dependent two-tier structure）。

---

## Strengths

**S1. 新颖且可操作的问题定义** [R1, R2 共识]
将 AI 生成文本检测从二元判别推向有序多类（generational depth），K* 作为离散边界指标具有直接的 data curation 操作价值。在 model collapse 文献（训练退化趋势）和 AI 文本检测（二元判别）之间开辟了新问题空间。

**S2. 实验规模与系统性** [R1, R2 共识]
10 种生成配置 × 6 架构家族 × 4 域 × 4 解码策略，配合 bootstrap 95% CI、置换检验、PELT changepoint 分析、LOFO 交叉验证、统计功效分析。20 页附录提供详尽的消融和 robustness check，远超同类工作的覆盖范围。

**S3. Cross-family scoring 控制** [R1]
识别并系统控制了 same-family scoring 导致的 K* 膨胀（如 Wikipedia 上 Qwen same-family K*=2 vs cross-family K*=1），消除了一个容易被忽视但对结果有重大影响的混淆变量。

**S4. 域排序发现的理论启发性** [R2]
arXiv(K*=3) > C4(K*=2) = Code(K*=2) > Wikipedia(K*=1) 的 θ-invariant 排序揭示了域结构复杂度与可区分深度的关系，对 data curation 有直接指导意义。

**S5. Marginal cases 的诚实报告** [R1]
明确报告 4/7 continuation-mode 配置 CI lower bound 距 θ 不足 1pp，boundary-level transfer 的脆弱性。透明度值得肯定。

**S6. Feature-set-dependent two-tier structure** [R1]
DeBERTa 在 arXiv 上 K*=3-4 表明 K* 本质上是 feature set 和 domain 的函数，这一发现对 K* 的正确解释具有重要意义。

---

## Weaknesses

### Must-Fix（影响接收决定，4 项）

**C1. DPI 理论论证与经验方法之间存在逻辑跳跃** [R1-W3 + R2-N1, 交叉共识 AGREE]
- **位置**: Section 3.1, Section 6
- DPI 保证的是完整分布上互信息的单调递减，但论文使用的是 15 维 surprisal 特征空间中的 pairwise AUC。从 DPI 到"特定特征空间中分类器性能单调递减"之间缺少形式化桥梁。Section 6 自己承认 "DPI guarantees existence but does not bound K*_neural"，但 Section 3.1 仍使用 "guarantee" 等强措辞。两位 Reviewer 独立指出此问题，交叉后维持 critical。
- **建议**: 将 DPI 明确定位为 motivation 而非 formal guarantee，调整 Section 3.1 措辞；补充讨论 surprisal 统计量作为互信息损失 proxy 的合理性。

**C2. θ=0.60 的 post-hoc 选择使 K*=2 核心结论脆弱** [R1-N1 + R2-W5, 交叉共识 AGREE]
- **位置**: Section 3.1, Figure 3, Section 4.1
- θ=0.60 是在观察 1v2 和 2v3 AUC 分布后选择的 post-hoc 阈值。4/7 continuation-mode 配置 CI lower bound 距 θ 不足 1pp（Qwen-cont 仅 0.2pp，OLMo-1B 仅 0.5pp），θ 上移 0.5pp 即可翻转多个 K* 判定。AUC=0.60 本身代表的分类能力很弱（仅略高于随机的 0.50）。R1 原评 critical，R2 原评 should-fix 后在交叉中同意升级。
- **建议**: 增加系统性 θ-sensitivity 表格（各配置在 θ∈{0.55, 0.575, 0.60, 0.625, 0.65} 下的 K*）；报告 Youden's J 选择的 θ_optimal 及对应 K*；Abstract/Conclusion 加入 "at θ=0.60" 的明确限定；讨论 AUC=0.60 对应的实际分类表现。

**C3. Prompt-chain 焦点与 model collapse 叙事之间的范围张力** [R2-N2, R1 AGREE with nuance]
- **位置**: Abstract, Section 1, Appendix D.1
- Introduction 以 model collapse 文献为动机，但实验几乎完全基于 prompt-chain。Retrain-chain 实验（Appendix D.1）仅覆盖 Qwen-1.5B 和 Pythia-1.4B，且 retrain-chain K*≈5-7 远高于 prompt-chain K*=2，表明两种场景退化动态本质不同。R1 建议以 web text curation 为独立动机。
- **建议**: Abstract/Introduction 明确 K*=2 是 prompt-chain 结论；减少对 model collapse 文献的叙事依赖，以 web text curation / one-wash detection 为自洽动机。

**C4. 模型规模覆盖偏向小模型，威胁 headline claim 可推广性** [R1-N3, R2 partially AGREE]
- **位置**: Table 1, Section 4.1, Limitations
- 10 种配置中 7 种 ≤2B 参数，≥7B 仅 3 种，14B 仅 1 种。K*=2 可能反映小模型容量限制而非文本可区分性的内在边界。DeBERTa K*=3-4 暗示更强检测器可延伸边界（R2 修正：DeBERTa 是 detector，K*=4 反映 detector capacity 而非 generator scale，但两者合力指向 K*=2 可能部分是 15D 特征空间 ceiling）。
- **建议**: Abstract/Conclusion 明确限定 "for models ≤14B"；Discussion 区分 K*_{15D} 和 K*_{intrinsic}。

### Reviewer 共识（Should-Fix，7 项）

**W1. 跨模型迁移的 boundary-level 失败需更充分讨论** [R1, R2 AGREE]
Section 4.2 报告 4/6 off-diagonal 7B pairs 在 boundary 级别失败，对生成模型未知的实际 curation 场景意味着 K* 估计不可靠。讨论仅限一句。建议 Section 6 增加段落分析实际影响及 multi-source pooling 缓解策略。

**W2. PELT changepoint 分析呈现具有误导性** [R1, R2 AGREE]
Exact agreement 仅 46%（K*∈{1,2,3} 量表上 ±1 chance level ~78%）。建议报告 Cohen's kappa，将 "validates" 降级为 "provides complementary evidence"。

**W3. Filtering 实验（Section 5）证据基础薄弱** [R1, R2 AGREE]
MMLU 改善约 0.76pp，仅覆盖 1-2 个下游任务。建议降级为 "preliminary case study"。Section 5 与前文缺过渡段。

**W4. K*=2 可能是 15D 特征空间的容量上限** [R1-Q3, R2-Q3 shared concern]
DeBERTa arXiv K*=4 vs LightGBM K*=2-3。建议 Discussion 明确区分 K*_{15D} 和 K*_{intrinsic}，承认两者可能不同。

**W5. Retrain-chain CI 方法与主实验不一致** [R1, R2 AGREE]
主实验 1,000-10,000 次 bootstrap vs retrain-chain 5 个 fold t-distribution。Retrain-chain 结论对 scope 界定至关重要，应改用 document-level bootstrap。

**W6. 与 Geng et al. (2026) 的技术区分不够清晰** [R2 原评 critical, R1 降级为 should-fix]
Section 3.1 的 Markov chain 形式化与 Geng et al. 高度相似。R1 认为 Markov chain 是通用框架不构成 novelty 冲突。建议明确归因并讨论 discrimination boundary vs convergence analysis 的区别。

**W7. Wang et al. (2025) attractor cycles 与 K* 概念联系值得深化** [R2, R1 partially AGREE]
Attractor entry depth 可能对应 K* boundary。论文已引用但未建立正式关联。

### Reviewer 分歧（2 项）

**D1. 多重比较校正** [R1: critical, R2: REBUT]
- R1：数十个同时检验缺 BH/Bonferroni 校正。
- R2 反驳：K* 由 CI-vs-θ 决定非 p-value，所有 p<0.001 经 Bonferroni(α=0.0005) 仍显著。
- **Director 评估**: R2 反驳有技术依据。定级 should-fix（补充 BH-adjusted p-values 增强严谨性，但非独立 critical）。

**D2. Soundness 评分** [R1: 3.0, R2: 3.5]
- R1 对 θ 选择和多重比较更严格；R2 认为实验设计整体达标。
- **Director 采纳 R1 的 3.0**: θ fragility 和模型规模偏向确实构成 soundness 层面的 concern。

---

## Questions for Authors

1. **Retrain-chain scope**: K*≈5-7 是否在 Qwen-1.5B/Pythia-1.4B 之外验证？如果普遍远高于 prompt-chain K*=2，prompt-chain 的 model collapse 动机是否需要重新定位？ [R2-Q1, R1 corroborated]
2. **θ robustness**: θ=0.60 如果用 leave-one-family-out CV 确定，K* 分布是否实质变化？ [R1-Q1, R2 AGREE]
3. **Marginal CI**: Qwen-cont CI lower bound 距 θ 仅 0.2pp，CI width 和 bootstrap variance 是多少？ [R1-Q2, R2 AGREE]
4. **Feature ceiling**: DeBERTa arXiv K*=4，如果换更丰富的 generator-independent 特征集（30D/50D），K* 是否提高？ [R1-Q3, R2-Q3]
5. **Instruct models**: 为什么不包含 7B+ instruction-tuned models？实际递归生成主要由 chat/instruct 模型产生。 [R1-Q4, R2 AGREE]
6. **Metric clarity**: Multi-source mixing 中 generator identity AUC=0.006，标准二分类 AUC 下界 0.5，请确认指标定义。 [R1-Q5, R2 AGREE]
7. **Wikipedia K*=1**: 1v2 不可区分与"生成文本随代际变化"的直觉关系？ [R2-Q3]
8. **Scalability**: Section 5 filtering 在 web-scale（数十亿文档、混合模型）下的可扩展性？ [R2-Q4]

---

## Missing References

R2 建议、R1 交叉评估相关性：

1. **"Can Generative AI Survive Data Contamination?"** (arXiv:2602.16065, 2026) — 递归训练污染理论保证，与 Markov chain 形式化交叉。[R1: 潜在高相关]
2. **"Beyond the Final Actor"** (arXiv:2604.04932, 2026) — fine-grained LLM text detection。[R1: 相关性待确认]
3. **"A Probabilistic Perspective on Model Collapse"** (Xu et al., 2025) — 概率论视角的 model collapse 分析，可能为 C1 的 DPI gap 提供理论补充。[R1: 潜在高相关]

---

## External Review (Stanford Agentic Reviewer)

**状态：未请求。** 项目未配置外部审稿。

---

## Visual Layout Check（非评分项）

**状态：已完成** (4 warning, 18 info, 0 critical)

**Warning:**
1. Figure 2/3 axis labels 字号偏小（正文 60-65%），建议提升至 70%+
2. Appendix page 15 极度拥挤（4 个 display items 挤在单页）
3. Appendix page 19 四张表格密集，表间留白极少
4. Appendix page 20 约 10 张小表极度密集堆叠

**亮点:** 主正文严格 8 页 ✓；display items 密度优秀（5 figures + 4 tables in 4 pages）；全文 booktabs 一致 ✓；无 margin 溢出/引用错误 ✓；首页无视觉锚点（Figure 1 在第 2 页），建议考虑上移。

---

## Overall Assessment

**Overall Score: 3.5 (Borderline Conference)**

| 维度 | R1 | R2 | 综合 |
|------|----|----|------|
| Soundness | 3.0 | 3.5 | 3.0 |
| Excitement | 3.5 | 3.5 | 3.5 |
| Reproducibility | 4.0 | 4.0 | 4.0 |
| Confidence | 4/5 | 4/5 | 4/5 |

**EMNLP 2026 ARR 标准**: 3.5 = Borderline Conference，介于 Findings 接收(3.0)和主会议接收(4.0)之间。

**核心判断**: 论文提出了一个新颖且有实用价值的问题定义（generational depth estimation + K* boundary），实验规模和系统性达到顶会水准。但四个 critical 问题共同限制了当前版本的接收可能性：(1) DPI 理论框架停留在 motivation 层面却以 "guarantee" 包装；(2) K*=2 核心结论对 post-hoc θ 选择高度敏感，多个配置在统计余量极薄处勉强通过；(3) prompt-chain 焦点与 model collapse 叙事存在未解决的范围张力；(4) 模型规模覆盖偏向 ≤2B，headline claim 的可推广性不足。

**Rebuttal 潜力**: 如果作者能 (a) 将 DPI 明确重新定位为 motivation（措辞调整，非实验变更）；(b) 提供 θ-sensitivity 完整表格和 Youden's J 数据；(c) 在 Abstract/Introduction 明确限定 prompt-chain scope 和模型规模范围；(d) 补充 BH-adjusted p-values，论文有潜力达到 Conference 接收水准。(a)(c)(d) 为措辞/分析调整不需新实验，(b) 需补充计算但数据已有。

---

## Detailed Comments

**Section 3.1 (Method):** K* 定义中 ∀f∈S 的 S 在此处未明确（直到 Section 3.2 才具体化）。DPI 段落需将 "guarantees" 改为 "motivates/suggests"。

**Section 4.1 (Results):** Margin stratification 分层报告有价值，建议 Table 2 补充每个配置的 margin-to-θ 值。Domain ordering claim 应仅基于 confident 配置。

**Section 4.2 (Transfer):** 聚合层面 80-92% 与 boundary-level 4/6 失败之间的张力需更深入分析。讨论 multi-source pooling 是否缓解 boundary-level failure。

**Section 4.4 (DeBERTa):** 建议正式引入 K*_{15D} vs K*_{intrinsic} 区分。

**Section 5 (Filtering):** 缺乏与 Section 4 的过渡。MMLU 改善 0.76pp 效应量小，建议降级 framing 为 "consistency check" 或 "preliminary case study"。

**Section 6 (Discussion):** Scale trends 基于 3 个数据点不宜外推。增加段落讨论 K* 与 attractor entry depth 的关系。

**Appendix D.1 (Retrain-chain):** CI 方法应改为 document-level bootstrap。

**Appendix D.21 (F1@0.50):** 主文提及但未给汇总数值，至少给出汇总 F1。

**Appendix D.24 (PELT):** 报告 Cohen's kappa，降低 "validation" framing。

**格式细节:** Table 4 跨两页影响可读性；Figure 2/3 字号偏小；generator identity AUC=0.006 指标待澄清；levin2017markov bib 年份核实版本。