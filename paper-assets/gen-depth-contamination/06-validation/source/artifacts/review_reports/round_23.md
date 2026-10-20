---
round: 23
review_mode: fresh
overall_score: 3.5 - Borderline Conference
timestamp: 2026-05-21T01:39:06.054648+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — gen-depth-contamination (Round 23, Fresh Review)

**目标 Venue**: EMNLP 2026 (ARR May 2026 cycle)
**Deadline**: 2026-05-25 (AoE)
**审稿模式**: Fresh (重新审稿)
**Reviewer 编排**: 2 人（R1: 方法严谨性+实验设计; R2: 新颖性+完整性+Related Work+写作质量）
**流程**: Round 1 独立审稿 → 交叉分享（逐条 AGREE/REBUT）→ 1 轮收敛

---

## Summary

本文形式化了 K*（递归合成文本中分类器能可靠区分相邻代际的最大生成深度），使用 15 个统计特征和 OBD-LightGBM 分类器，在 10 个模型配置（6 个架构族，1B-14B）上测量得出 prompt-chain 模式下 K*≤2（θ=0.60）。论文报告了特征集不变的域排序（arXiv>C4=Code>Wikipedia）、跨模型迁移结果（80-92% 准确率保留但边界处脆弱）、以及 K*-一致过滤的下游评估。DeBERTa fine-tuning 验证了域排序的 feature-set invariance，在 C4/Code 上匹配 15D 边界（K*=2），在 arXiv/Wikipedia 上推高 K*，确立 15D 为保守下界。

---

## Strengths

**S1. 新颖且有用的形式化框架** [R1, R2 共识]
K* 概念填补了 binary detection 和 population-level model collapse 分析之间的空白，提供 per-text 可操作深度估计，直接连接数据筛选需求。研究问题定义清晰，实际意义明确。

**S2. 系统性实验设计** [R1, R2 共识]
10 配置 × 4 域 × 4 解码策略的覆盖面在同类工作中属前列。域排序通过 changepoint 分析（PELT）、margin stratification、LOFO cross-validation 三重验证。

**S3. 统计方法论严谨** [R1, R2 共识]
Bootstrap CI（1,000/10,000 resamples）、置换检验（p≤10⁻⁴）、BH 校正（q_max=0.003）、GroupKFold、Youden's J 分析。统计方法论的主体框架正确且在 NLP 论文中少见。

**S4. 极其坦诚的 Limitations** [R1, R2 共识]
9 项详尽的 Limitations 覆盖 scope、protocol、threshold、marginal boundary、feature set、segment length、curation applicability、family balance、transfer coverage，体现良好学术诚信。

**S5. 域排序 invariance 发现** [R1, R2 共识]
arXiv(K*=3) > C4(K*=2) = Code(K*=2) > Wikipedia(K*=1) 在两种特征体系（15D 和 DeBERTa）下均成立，是有价值的新经验知识。

**S6. Retrain-chain 对比** [R1]
Appendix 中 retrain-chain K*=7（vs prompt-chain K*=2）有效区分了 text-intrinsic 信息损失和累积模型适应伪影。Figure 4 JSD 衰减曲线提供很好的互补证据。

---

## Weaknesses

### Must-Fix（影响接收决定）

**C1. θ=0.60 的选择存在循环论证风险** [R1 Critical, R2 Agree(降为 Major)]
θ 从观测到的 AUC 分布中得出（1v2 聚集于 0.61-0.70，2v3 聚集于 0.55-0.59），然后用 Youden's J 在同一数据上"验证"。LOFO（θ̂∈[0.5725,0.6004]，8/9 K* 匹配）提供了部分 held-out 验证，但不足以完全消解循环性。多个配置 CI lower 距 θ 不足 1pp（Qwen-cont 0.2pp，OLMo 0.5pp，LLaMA-8B 0.3pp）。
- **Action**: 补充 held-out validation（non-Qwen 推导 + Qwen 验证或反向）；报告 θ∈[0.55,0.65] 每 0.01 步长的 K* 赋值表；明确标注 marginal cases。

**C2. Prompt-chain 焦点与 model collapse 叙事范围存在张力** [R2 Critical, R1 Agree(降级)]
Introduction 以 retrain-chain model collapse 为核心动机（引用 Shumailov 2024, Dohmatob 2024），但全部主实验在 prompt-chain 下进行。论文在 Introduction 第一段已区分两者（"we study prompt-chains"），但区分的位置和力度不够。Retrain-chain K*=7 仅在 Appendix 出现。
- **Action**: Introduction 末尾提及 retrain-chain K*=7，形成 K*∈[2,7] 完整图景；更明确说明 prompt-chain 对 web-scale curation 的实践相关性。

**C3. 模型配置空间偏重 Qwen 家族** [R1 Major, R2 Agree]
10 配置中 Qwen 占 5 个（continuation-mode 4/9），≥7B 仅 3 个模型，14B 仅 Qwen-2.5-14B。Cross-domain 实验中 Gemma-2-2B 和 OLMo-1B 多个 domain 缺失。当 K*≤2 结论主要由 Qwen 变体驱动时，跨架构可推广性声称被削弱。
- **Action**: 补充至少 1 个非 Qwen 规模变体（如 Pythia-6.9B、LLaMA-3-1B），或显著弱化可推广性声称。

### Should-Fix（影响评分但不一票否决）

**W1. K* 部分依赖分类器能力，非文本固有属性** [R1 Major, R2 Agree]
DeBERTa 将 arXiv K* 从 2-3 扩展到 3-4，Wikipedia 从 1 到 2。C4/Code 上 K*_DeBERTa=K*_15D=2 构成 representation-independent boundary，但其他域不然。论文的叙事（Title "Measuring the Discrimination Boundary"）暗示 K* 是文本内在属性。
- **Action**: 更系统使用 K*_15D 和 K*_DeBERTa 符号；Discussion 增加 Practical Recommendations 段落。

**W2. Filtering 实验效果量不足** [R1 Major, R2 Major, 强共识]
GSM8K +1.92pp, TruthfulQA +1.52pp, WinoGrande -0.79pp（负面！），效果量在 benchmark noise floor 内且方向不一致。Pythia 上 graduated=no-filter。仅 30K docs + 5 seeds，统计 power 可能不足。
- **Action**: 将 Section 5 明确定位为 consistency check 而非独立贡献；讨论 WinoGrande 负面结果和 Pythia graduated failure；补充 power analysis 或 Limitations 声明。

**W3. Abstract 信息密度过高** [R2 Major, R1 Agree]
Abstract 在未定义 K* 的前提下使用 OBD-LightGBM、θ=0.60、margin stratification 等术语，并引用 Section 4.1（在 ACL 论文中不常见）。
- **Action**: 前半部分加一句 K* 直觉定义，移除 Section 引用，精简实现细节。

**W4. Conclusion 过于简短** [R2 Major, R1 Agree]
Section 7 仅约 5 行，对一篇有 21 页附录的论文来说过于单薄。缺 broader implications 和 actionable takeaways。
- **Action**: 扩展至 8-12 行，包括 K*=2 对 web-scale curation 的指导、prompt-chain vs retrain-chain 的 broader implications、未来方向。

**W5. K* 符号系统过度增殖** [R2 Minor-Major, R1 部分同意]
K*, K*_empirical, K*_theory, K*_neural, K*_binary, K*_15D, K*_intrinsic 等变体过多。部分可能是隐含变体而非显式定义，但仍增加认知负担。
- **Action**: 主文统一为 K*（默认 15D+OBD），仅对比时引入带下标变体；确认 notation table 覆盖完整。

### Minor

**M1. 遗漏 Fu et al. (2025) 引用** [R2, R1 Agree]
"A Theoretical Perspective: How to Prevent Model Collapse in Self-consuming Training Loops" (ICLR 2025) 与 K* 有限边界概念直接相关。

**M2. 3 个 orphan bib entries** [R2, R1 Agree]
hao2025rewrite, tang2024science, wu2023survey 未被引用。levin2017markov 年份需确认版本。

**M3. ANOVA 交互 vs generator-independent 措辞** [R1 Q3, R2 rebut 效应量极小]
η²=0.03 统计显著但效应量可忽略。建议将 "generator-independent" 调整为 "largely generator-invariant"。

**M4. Retrain-chain CI 方法与主实验不一致** [R1, R2 Agree]
主实验用 bootstrap CI，retrain-chain 用 t-distribution CI（K=5）。应说明选择理由。

---

## Reviewer Consensus [AGREE]

以下问题两位 Reviewer 达成完全共识：

1. **θ 验证需加强**：LOFO 提供部分 held-out，但更严格的 family-split validation 更优（R1-W1, R2 agree）
2. **K* 是 classifier-conditional 的**：需更清晰的 K*_15D vs K*_DeBERTa framing（R1-W3, R2 agree）
3. **Qwen 过度代表**：可推广性声称需弱化或补充实验（R1-W4, R2-W4 均标记）
4. **Filtering 应定位为 consistency check**：效果量不足以支撑独立贡献（R1-W5, R2-W2 强共识）
5. **Abstract 需精简**：加 K* 直觉定义，去 Section 引用（R2-W1, R1 agree）
6. **Conclusion 需扩展**：增 broader implications（R2-W3, R1 agree）
7. **Missing reference**: Fu et al. (2025) ICLR（R2-W5, R1 agree）
8. **Orphan bib entries**: 3 个需清理（R2-W6, R1 agree）
9. **统计方法一致性**: retrain-chain CI 需说明理由（R1-W7, R2 agree）
10. **评分一致**: 均 3.5 Borderline Conference

## Reviewer Divergence [REBUT]

**唯一显著分歧：DPI/novelty 的 framing 问题**

两位 Reviewer 从不同角度标记了同一问题，但互相 rebut 了对方的版本：

- **R1-W2（DPI→K* 逻辑缺口）**: R1 标记为 Critical。R2 **[REBUT]**: 论文已明确声明 "DPI motivates but does not formally guarantee or bound K*"（Section 3.1），且将 adjacent-pair convergence 归因于 Markov chain stationary distribution approach（cite Levin & Peres 2017）。R2 认为论文当前措辞基本到位，建议降至 Minor。

- **R2-N2（K* vs Geng/Wang 增量贡献）**: R2 标记为 Critical。R1 **[REBUT]**: K* 是 classifier-operational 指标（per-text 可操作深度估计），与 Geng 的 distributional convergence 和 Wang 的 dynamical systems 描述是不同层面的问题。要求 formalize K* 与 mixing time 的关系需要非平凡的数学证明，超出实证论文合理范围。R1 建议降至 Minor-to-Moderate。

**Director 评估**: 两个 REBUT 的方向一致——都认为对方标记的问题在论文中已有部分处理，不构成 Critical。但合并来看，DPI 的定位和 K* 相对于 convergence 概念的区分确实需要进一步强化。建议将两者合并为一个 Should-Fix：在 Section 3.1 和 Related Work 中更显著地强调 K* 的 per-text operational 独特性，同时确认 DPI 措辞无残留的 "guarantee/implies"。

---

## Questions（需作者澄清）

**Q1** [R1]: θ 的 held-out validation 是否可行？non-Qwen 推导 + Qwen 验证？
**Q2** [R1, R2]: 实践者应使用 K*_15D=2 还是 K*_DeBERTa=3-4？论文缺明确指导。
**Q3** [R2]: Mistral-7B 在 C4 上 K*=1 但 arXiv 上 K*=3，是否暗示 K* 更多反映 domain-model interaction 而非纯 domain structural complexity？（R1 同意但指出 ordering invariance 未被违反，更准确描述是"domain 决定 ordering，model 决定 absolute level"。）
**Q4** [R1]: 30K 文档 + 5 seeds 是否足以检测 ~2pp 的 filtering 效果量？能否提供 power analysis？
**Q5** [R1, R2]: 混合 prompt-chain + retrain-chain 设置下 K* 如何估计？K*∈[2,7] 区间对实践者过宽。
**Q6** [R2]: 是否考虑过更大 encoder（DeBERTa-large/xl）验证 K*=2 upper bound？

---

## Missing References

1. **Fu et al. (2025)** "A Theoretical Perspective: How to Prevent Model Collapse in Self-consuming Training Loops" (ICLR 2025, arXiv:2502.18865) — recursive stability 概念与 K* 有限边界相关 [R2 提出, R1 agree]
2. **PAN@CLEF 2025 Generated Plagiarism Detection Task** — iterative LLM generation 检测 shared task [R2 提出]

引用库验证：66 条中 58 条在线验证通过，4 条因较新未找到（均为真实论文），4 条轻微不匹配（年份/拼写），3 条 orphan，无伪造引用。

---

## External Review (Stanford Agentic Reviewer)

外部审稿：未启用（项目配置 `external_review.paperreview_ai.enabled = false`）。

---

## Visual Layout Check（非评分项）

**状态**: ✅ 已完成（耗时约 4 分钟）

**Findings**:
- **0 Critical, 1 Warning, 12 Info**
- ⚠️ Warning: Appendix page 20 单页包含 8 个小表格（Tables 25-32），视觉极度拥挤。建议合并或分页。
- ℹ️ 主文布局合理：Figure 1（page 2）作为首个 display item 效果良好，pipeline 图清晰传达核心流程。
- ℹ️ Table 2 脚注字号偏小（~6-7pt），Figure 2 子图 axis labels 接近可读下限，Figure 3 heatmap 数字字号偏小但配合颜色可辨识。
- ℹ️ Page 7 包含 Table 4 + Table 5（cross-domain + filtering），table-heavy 但内容不同，布局合理。
- ℹ️ Appendix 末页约 80% 填充，可接受。

---

## Overall Assessment

**Overall Score: 3.5 — Borderline Conference**

**ACL ARR 维度评分（Reviewer 均值）**:

| 维度 | R1 | R2 | 均值 |
|------|----|----|------|
| Soundness | 3.0 | 3.5 | 3.25 |
| Excitement | 3.0 | 3.0 | 3.0 |
| Reproducibility | 3.0 | 4.0 | 3.5 |
| Clarity | — | 3.5 | 3.5 |
| Confidence | 4.0 | 4.0 | 4.0 |

**判决理由**:

K* 框架新颖且填补了文献真实空白（per-text 可操作深度估计），实验覆盖面广（10 配置 × 4 域 × 4 解码策略），域排序 invariance 是有价值的新发现，Limitations 极其坦诚。

主要削弱因素：(1) θ=0.60 的选择虽有多重验证（Youden's J、BH 校正、LOFO、灵敏度分析）但缺真正独立的 held-out validation；(2) prompt-chain 焦点与 model collapse 动机的张力需更好弥合；(3) Qwen 占配置空间 50%；(4) filtering 效果量在 noise floor 内。核心问题不在实验执行质量（优秀），而在 claims 相对于证据偏强。

**如果以下 Must-Fix 解决，有潜力提升至 4.0（Conference）**:
1. θ 的 held-out validation（non-Qwen 推导 + Qwen 验证）
2. Introduction framing 调整（prompt-chain 独立动机 + retrain-chain K*=7 对比）
3. 弱化可推广性声称（限定 ≤14B，承认 Qwen 偏重）

---

## Detailed Comments

### Section 1 (Introduction)
- 开篇 model collapse 动机与 prompt-chain 实验的张力是两位 Reviewer 共同关注的最显著 framing 问题。建议在第一段即明确：(a) prompt-chain 和 retrain-chain 的降退机制不同（文本统计特征衰减 vs 权重累积偏移）；(b) prompt-chain 对 web-scale curation 更实际相关；(c) retrain-chain K*=7 提供 upper bound。
- Contribution (c) 中 "80-92% accuracy retention" 已含 "but boundary-level K* assignments fail" caveat，framing 已改善。

### Section 3 (Method)
- Section 3.1 DPI 讨论：当前措辞（"motivates but does not formally guarantee"）方向正确，但检查是否有残留的 "implies" 或 "guarantees"。
- θ=0.60：Youden's J（J=1.0 at config level, J=0.88 at fold level, θ*=0.605）和 BH 校正已有改善。建议补充 held-out family-split validation 和细粒度灵敏度表。

### Section 4 (Experiments)
- Table 2 中 marginal configurations 应有更显著的标注（如 bold/italic CI lower bounds within 1pp of θ）。
- Cross-domain Table 4 中 Gemma/OLMo 的 "---" 需统一说明 convention。
- Mistral-7B 的域间 K* 差异（C4=1, arXiv=3）值得在 Discussion 中更深入讨论 domain-model interaction vs pure domain complexity。

### Section 5 (Filtering)
- 当前标题 "K*-Consistent Filtering" 暗示独立贡献。建议改为 "Consistency Validation: K*-Guided Filtering" 或类似表述。
- WinoGrande -0.79pp 和 Pythia graduated failure 需诚实讨论。

### Section 6 (Discussion)
- "Feature-space ceiling" 段落方向正确但需更明确的实践指导：C4/Code 用 K*_15D=K*_DeBERTa=2；arXiv/Wikipedia 用 K*_DeBERTa 更优但需 fine-tuned encoder。
- "Transfer implications" 段落需更深入讨论 boundary failure 对实际 curation 的影响。

### Section 7 (Conclusion)
- 当前仅 5 行。建议扩展至 8-12 行。

### References
- 增加 Fu et al. (2025) ICLR；删除 3 个 orphan entries；确认 Levin & Peres 版本。

### Format Compliance
- ✅ Double-blind 匿名完整
- ✅ 主文 8 页（Section 1-7），Limitations 从 page 8 中部开始（不计入页数限制）
- ✅ Limitations section 存在且详尽（9 项）
- ✅ Ethics Statement 存在且合理
- ✅ ACL style with [review] option
- ✅ 正文无破折号违规
- ⚠️ 3 个 orphan bib entries 需清理