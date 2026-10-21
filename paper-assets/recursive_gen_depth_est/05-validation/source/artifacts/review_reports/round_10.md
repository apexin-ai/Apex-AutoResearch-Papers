---
round: 10
review_mode: fresh
overall_score: 3.0 (Findings)
timestamp: 2026-05-19T06:52:00.336403+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 13 (Fresh Review)

**论文**: How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints
**目标 Venue**: EMNLP 2026 (ARR May cycle)
**审稿模式**: Fresh (重新审稿)
**Reviewer 编排**: 2 人（R1: 方法严谨性+实验设计, R2: 新颖性+写作完整性+Related Work）
**轮次**: Round 1 独立审稿 → 交叉分享 → 收敛（1 轮完成）

---

## Summary

本文将递归生成深度估计（recursive generation depth estimation）形式化为序数分类任务，构建了 180K 样本的基准测试集（3 个模型族 × 3 种解码策略 × 4 个深度等级），使用基于 19 个统计特征的 Random Forest 进行分类，并提出 Effective Discriminable Depth (EDD) 指标量化相邻深度的可区分极限。论文在多个泛化轴（跨模型、跨策略、跨域、跨尺度）上进行了系统实验，核心发现是困惑度尾部特征族（p90_ppl、var_surprisal）在所有 9 个 model-strategy cell 中主导深度判别，EDD_{0.70}=4 for all three model families at 1-1.5B scale。

---

## Strengths

**S1: 任务形式化填补真实空白。** 在二元检测（human vs. machine）和模型坍塌理论（假定深度已知）之间，序数深度估计是一个未被研究的新维度。EDD 指标将 model collapse 理论的定性预测转化为可操作的定量指标。两位 Reviewer 一致认可这是论文最重要的贡献。

**S2: 基准设计系统且全面。** 3×3 grid（模型族 × 解码策略）覆盖了合理的变异来源，180K 样本规模充足，8 个泛化轴的测试体系（跨模型、跨策略、跨域、跨尺度、prompted generation、跨模型链、深度扩展、温度鲁棒性）在 empirical study 中罕见地系统。

**S3: 控制实验和报告诚信度高。** Domain bias analysis 中的 LOGO 评估（72.1% 匹配标准 CV 72.0%）和 seed-group negative control（10.2%, chance level）有效排除了 topic leakage。修正 bug 后如实报告修正前后数据体现研究诚信。Limitations 章节主动讨论了 full-replacement vs. accumulation、d0 inflation、cross-strategy boundary inversion、reference model dependency 等多个 limitation，透明度在提交稿中罕见。

**S4: 分类器收敛验证了特征为核心。** RF、XGBoost、LightGBM 在 0.4pp 内收敛（§5.1），CORAL/DivEye 在 0.6pp 内匹配（p>0.05），有力论证信号来自特征设计而非分类器架构。这本身是一个有价值的 empirical finding。

**S5: Related Work 覆盖全面。** 69 条引用，覆盖 model collapse theory、AI text detection、membership inference、ordinal classification、decoding strategy effects 等主要领域，2025-2026 最新工作均已纳入。

**S6: 跨模型递归链实验有说服力。** 异构链（Pythia→OLMo→GPT-2 XL, 84.75%）和反向链（GPT-2 XL→OLMo→Pythia, 85.75%）有效排除了架构指纹假说，为 process-level depth signal 提供了初步证据。

---

## Weaknesses

### Must-Fix（共识）

**W1 [Must-Fix, consensus]: Reference model circularity claim 与消融数据直接矛盾。**
- §3.4 声称 Pythia-1.4B 同时作为 generator 和 reference model "confers no systematic advantage"，论据是 Pythia 数据（78.7%）低于 GPT-2 XL 数据（85.9%）。
- 但这是跨 generator 的混淆比较。Appendix H（Table 8）的公平消融显示：在 Pythia 生成的数据上，self-reference（78.6%）> OLMo 参考（74.5%）> GPT-2 XL 参考（67.3%），self-reference 带来 4.1-11.3pp 优势。
- Limitations 也承认 "same-family references yield optimal performance"。
- 这使得 9 个 cell 的横向比较不公平：Pythia cell 可能因 self-reference 被高估，OLMo/GPT-2 XL cell 因 cross-reference 被低估。
- **修复**: 修正 §3.4 claim，承认 self-reference 带来可测量优势；Table 2 Pythia 行注明 self-reference。

**W2 [Must-Fix, consensus]: Cross-scale 实验的 5 个混淆因素使结论不可靠，Abstract 表述过度乐观。**
- 7-14B 实验受 5 个混淆因素限制（QLoRA 4-bit 量化 / 500 vs 5000 samples / 仅 nucleus 策略 / 词表不匹配 / 14B self-reference）。
- 仅 2 个 7-8B 模型给出方向相反的 AUC 轨迹（Llama-3.1 单调 vs Qwen2.5 U型），无法判断哪种是主流模式。
- 14B 的 EDD=0（d0v1 AUC=0.643）可能是 self-reference + quantization 的产物。
- Abstract "depth signal persists at larger scales" 对 14B 不成立。
- **修复**: Abstract 中 14B 标记为 boundary condition；限制 "existence proof" claim 为 7-8B。

### Should-Fix（共识或 Director 裁定）

**W3 [Should-Fix, R1 Must-Fix / R2 Should-Fix, Director 裁定 Should-Fix]: d0 recall >97% 膨胀 headline metrics。**
- Abstract 和 Contribution 列表仍以四类准确率为主导叙事。Cross-model transfer 66.4% headline → 55.4% d1-d3；Cross-strategy 59.1% → 45.9% d1-d3。Pythia holdout d2 recall 仅 26.8%。
- 论文已在每个 table 旁系统性并列 d1-d3 balanced accuracy（相比 Round 12 有改善），但 Abstract 仍以四类准确率领头。
- **修复**: Abstract 和 Contribution 列表以 d1-d3 balanced accuracy 为主指标。

**W4 [Should-Fix, R2 Must-Fix / R1 Should-Fix, Director 裁定 Should-Fix]: Abstract 数字堆砌。**
- Abstract 9 句话包含 20+ 个数值，读起来像 results summary 而非叙事。信息完整但缺乏吸引力。Round 12 已提出但未修复。
- **修复**: 减少到 8-10 个关键数字，叙事主线放在困惑度尾部统计洞察上。

**W5 [Should-Fix, R2 Must-Fix / R1 Should-Fix, Director 裁定 Should-Fix]: Discussion 过薄。**
- 从 Round 12 的 ~80 词扩展到 ~250 词（3 段），有改善但仍不足以承载 9 cell + 8 泛化轴的 empirical study insight。Appendix N 的 provenance toolkit 讨论和 cross-strategy conditional decomposition 是有价值的材料但被放逐到附录。
- **修复**: 将 provenance toolkit 讨论提升到正文；新增 cross-strategy barrier 作为 empirical contribution 的分析和 depth-as-process vs depth-estimation 的概念区分。

**W6 [Should-Fix, consensus]: Full-replacement only 缺乏 accumulation 实验。**
- 所有实验使用 full-replacement chains。Discussion 声称这是 accumulation 的 "ceiling estimate"，但缺乏理论或实验支持。Accumulation 设置下特征行为可能完全不同。Round 12 至今未补充任何 accumulation 实验。
- **修复**: 至少做一个 toy-scale accumulation 实验验证 upper bound 假设。

**W7 [Should-Fix, consensus]: Curation PoC 统计分析有误。**
- 核心比较（RF-filtered vs unfiltered）全部不显著（p>0.4）。RF vs random 的 Bonferroni 校正后，Appendix N 声称 "2 of 3 surviving" 不准确（rf_moderate vs random_moderate p=0.020 > α=0.017）。
- **修复**: 修正 Bonferroni 表述；将 curation 描述为 negative/inconclusive result。

**W8 [Should-Fix, consensus]: VIF>10 下 feature importance 解释过度。**
- 14-16/19 features VIF>10，脚注承认 multicollinearity caveat，但 Table 3 仍展示逐特征精确 importance 值。Group-level claim（Kendall's W=0.90）可靠，但 individual feature rankings 不稳定。
- **修复**: 将脚注 caveat 提升为正文段落；Table 3 caption 明确注明 individual rankings unstable。

**W9 [Should-Fix, consensus]: EDD contiguous prefix 在非单调场景下过于保守。**
- EDD 要求所有 pairwise AUC 从 (0,1) 到 (d*,d*+1) 均超过 T。非单调 AUC（Qwen2.5-7B U型, cross-strategy d1v2 AUC 低至 0.129）下 EDD 大幅低估真实可区分范围。Limitations 承认但无替代方案。
- **修复**: 提供补充指标（如 Maximum Discriminable Depth）；§3.5 明确适用条件。

**W10 [Should-Fix, consensus]: Cross-seed replication 仅 3/9 cells，seed=43 系统性偏高。**
- seed=43 在所有 3 cell 中均优于 seed=42（+0.14 到 +3.17pp），2/3 统计显著。Table 2 中多个跨 cell 差异可能在 seed noise 范围内（~1-3pp）。

### Minor

**W11 [Minor, divergence]: 方法层面无算法贡献。** R2 列为 Should-Fix，R1 REBUT（ARR guidelines H2 保护 empirical contribution）。论文已在 Introduction 明确声明 empirical contribution 定位，classifier convergence 本身是有价值的 empirical finding。Director 裁定：这是论文 excitement 的主要限制因素，但不构成 soundness 问题。

**W12 [Minor, consensus]: AI 写作痕迹。** -ing 短语（confirming/demonstrating/suggesting...）正文+附录共 20 次。不影响技术内容但为审稿人可见的 AI 写作标志。

**W13 [Minor]: 3 条孤儿引用（llama3, qwen2.5, sugiyama2007_importance_weighting）在 bib 中但未被 cite。**

**W14 [Minor]: 单一 LoRA 超参配置，缺乏 rank/lr 敏感性分析。**

**W15 [Minor]: Prompted generation 验证仅 1/9 cell（GPT-2 XL nucleus），-13.8pp 下降幅度下 top-k 配置可能逼近 chance。**

---

## Reviewer Consensus

**完全一致 [AGREE] 的问题:**
1. Reference model circularity claim 需修正（R1-W1 / R2 AGREE）
2. Cross-scale 14B 结论不可靠，Abstract 表述需校准（R1-W2 / R2-W7 / 双方 AGREE）
3. Full-replacement scope 是核心限制，缺乏 accumulation 实验（R1-W8 / R2-W4 / 双方 AGREE）
4. Curation PoC 统计分析需修正（R1-W4 / R2-W9 / 双方 AGREE）
5. VIF>10 下 feature importance 解释过度（R1-W5 / R2 AGREE）
6. EDD contiguous prefix 在非单调下过于保守（R1-W6 / R2 AGREE）
7. Cross-seed replication 不足（R1-W7 / R2 AGREE）
8. 孤儿引用需清理（R2-W8 / R1 AGREE）
9. Curation PoC 需 multiple comparison correction（R2-W9 / R1-W4 AGREE）
10. 任务形式化是真正的新贡献（S1 双方一致）
11. 实验设计系统全面（S2 双方一致）

## Reviewer Divergence

**R1 Must-Fix / R2 Should-Fix:**
- d0 inflation: R1 认为 Abstract 应以 d1-d3 为主指标（Must-Fix），R2 认为论文已通过并列 d1-d3 balanced accuracy 充分处理（Should-Fix）。**Director 裁定 Should-Fix**：transparency 已改善，但 Abstract 叙事仍需调整。

**R2 Must-Fix / R1 Should-Fix:**
- Abstract 数字堆砌: R2 列为 Must-Fix，R1 AGREE 但降为 Should-Fix（信息完整性无问题）。**Director 裁定 Should-Fix**。
- Discussion 过薄: R2 列为 Must-Fix，R1 AGREE 但降为 Should-Fix（影响 excitement 而非 soundness）。**Director 裁定 Should-Fix**。

**R2 Should-Fix / R1 REBUT:**
- 方法无算法贡献: R2 认为 RF + 已知特征不足以支撑 Conference（Should-Fix），R1 引用 ARR guidelines H2 和 empirical contribution 先例 REBUT。**Director 裁定**：合理的审美分歧，记录但不作为降分依据。
- EDD 创新有限: R2 认为本质是 pairwise AUC + threshold，R1 REBUT（operationalization 有独立价值，类比 BLEU/ROUGE）。**Director 裁定**：R1 论据更有说服力。

---

## Questions（需要作者在 Rebuttal 中回答）

**Q1 [R1]:** Table 8 self-reference 带来 4-11pp 优势，§3.4 如何与 "no systematic advantage" 调和？

**Q2 [R1]:** Full-replacement "upper bound" 假设有何实验或理论依据？是否存在 accumulation 反而增强某些深度信号的可能？

**Q3 [R1]:** seed=43 系统性偏高的原因？d3 outlier 比例 0.56% vs 12.8% 但 seed=43 准确率更高——clipping 机制是否为完整解释？

**Q4 [R1]:** Cross-strategy transfer d1-d3: 45.9% 是否足以支持 "data auditing" 实用 claim？

**Q5 [R2]:** Cross-strategy d1/d2 inversion 是否意味着 depth 作为统计量的 strategy-invariance 不成立？depth-as-process 和 depth-as-estimable-quantity 的边界在哪里？

**Q6 [R2]:** GPT-2 XL 始终最高准确率：是 architecture effect 还是 reference model 分布差异效应？

**Q7 [R2]:** EDD=4 跨三个 family 一致性有无超出经验观察的理论基础？

---

## Missing References

两位 Reviewer 均未发现重大引用遗漏。Related Work 覆盖全面（69 引用），model collapse theory、AI text detection、membership inference、ordinal classification、decoding strategy effects 主要工作均已纳入。

建议关注：
- Synthetic data contamination in the wild 的实证研究（2025-2026 新工作）
- LoRA 微调与模型坍塌交互的工作

3 条孤儿引用需删除或添加 cite（llama3, qwen2.5, sugiyama2007_importance_weighting）。

---

## External Review (Stanford Agentic Reviewer)

外部审稿：未配置。

---

## Overall Assessment

**Overall: 3.0 (Findings)**
**Confidence: 4/5**

**评分区间**: R1 给 3.5 (Borderline Conference), R2 给 3.0 (Findings)。

**Director 裁定 3.0 (Findings) 的理由:**

论文的核心贡献——将递归生成深度估计形式化为序数分类并构建系统性基准——是有意义且及时的。在 1-1.5B full-replacement 范围内的实验设计审慎，控制实验（LOGO、negative control、reverse chain）是亮点，reporting 诚信度高。

但以下问题的组合将论文限制在 Findings 水平：

1. **Claim 校准问题**（W1, W2）：reference model circularity 的误导性 claim 和 cross-scale 的过度乐观表述是方法严谨性缺陷，需要实质性修正。

2. **生态效度不足**（W6）：full-replacement only 且无任何 accumulation 实验，"upper bound" 假设未经验证。这限制了论文从实验室到部署的路径说服力。

3. **写作深度不足**（W4, W5）：Abstract 数字堆砌缺乏叙事吸引力，Discussion ~250 词无法承载 empirical study 的 insight 深度。这些是 impression management 问题，但在审稿人快速判断价值时影响显著。

4. **方法层面无算法贡献**（W11）：虽然 ARR guidelines 保护 empirical contribution，标准 RF + 标准特征的组合在 excitement 维度上是限制因素。classifier convergence 证明了特征为瓶颈，但也意味着当前 pipeline 已触及 ceiling。

**从 3.0 提升到 3.5 的路径：**
- 修复 W1（reference model claim）和 W2（cross-scale claim 校准）→ 消除 soundness concerns
- 充实 Discussion（W5）+ 重写 Abstract（W4）→ 提升 excitement/impression
- 补充 accumulation pilot（W6）→ 提升生态效度

这些修改在 rebuttal + revision cycle 内是可行的。

---

## Detailed Comments（按 Section）

### Abstract
- 20+ 数字堆砌，缺乏叙事吸引力（W4）。应以 d1-d3 balanced accuracy 为主指标（W3）。
- "depth signal persists at larger scales" 对 14B（EDD=0）不准确（W2）。
- "Preliminary cross-scale experiments (7-14B, 54-70%)" 应将 14B 明确标记为 boundary condition。
- "a single-cell prompted-generation test 69.5%" 的 qualifier 是诚实的，保持。

### §1 Introduction
- Full-replacement scope 说明在第 2 段出现，位置合理但可更前置。
- Contribution 列表中 "EDD_{0.70}=4 for all three families" 需注明这是 1-1.5B 结果。
- Empirical contribution 定位声明是恰当的。

### §2 Related Work
- 覆盖全面，69 引用，结构清晰（6 个 paragraph 按主题分组）。
- 与 Mohamed et al. (2025) "Broken Telephone" 的区分清晰但可补充为何其 degradation characterization 不能直接用于深度分类。

### §3 Method
- §3.4: "confers no systematic advantage" 必须修正（W1）。建议改为 "confers a measurable advantage on same-family data (4-11pp; Appendix H) but does not drive the cross-generator accuracy ranking"。
- §3.5 EDD: Definition 1 的适用条件（monotonic AUC decay）应在定义正文而非脚注中明确（W9）。
- §3.6 Theoretical Grounding: 简洁有效，strategy-dependent convergence 的论述有理论支持。

### §4 Atlas
- §4.1: Table 2 建议增加 d1-d3 balanced accuracy 列。Pythia 行应标注 self-reference。
- §4.2: Footnote 3 的 multicollinearity caveat 应提升为正文段落（W8）。Table 3 caption 应注明 individual rankings unstable under VIF>10。
- §4.3: Monotonicity analysis 简洁有效。
- §4.4: EDD analysis 是论文亮点。AUC decay curves (Figure 2) 信息密度高。

### §5 Generalization
- §5.1: "within 0.4pp" 收敛 claim 是否经过等价性检验（如 TOST）？
- §5.3: Cross-strategy transfer 的 boundary inversion 分析是有价值的 empirical finding，但 Discussion 中应更深入地讨论 depth-as-process vs depth-estimation 的概念区分。
- §5.4: "existence proof" 措辞合适，但需限制为 7-8B。14B 应明确标记为 boundary condition。

### §6 Discussion
- ~250 词 3 段，有改善但仍不足。建议提升 Appendix N 内容到正文，新增 cross-strategy barrier 分析和 feature adaptation 讨论。

### Limitations
- 质量很高，主动覆盖了 9 个 limitation。Reference model circularity 的更诚实表述应从 Limitations 前移到 §3.4。

### Ethics Statement
- 简洁充分，覆盖了公开模型/数据使用、无人类受试者、潜在误用风险。

### Appendix
- 全面且有价值（16 个 subsection）。Appendix K（Curation PoC）的 Bonferroni 校正需修正（W7）。建议 Appendix N（Extended Discussion）中最重要的内容移回正文。

### 格式合规
- 模板: ACL style (review mode) ✓
- 匿名: "Anonymous" author ✓，未发现作者信息泄露
- Limitations: 存在且实质性 ✓
- Ethics Statement: 存在 ✓
- 引用格式: natbib, 基本一致 ✓
- 3 条孤儿引用需清理（W13）

---

## 与 Round 12 问题对照

| Round 12 Issue | R13 状态 | 备注 |
|---|---|---|
| R12-W1 生态效度/scope | 部分改善 | 添加了 scope 声明和 Discussion 段落，但仍缺 accumulation 实验 |
| R12-W2 Cross-strategy 45.9% | 改善 | 重定位为 key empirical finding，措辞修改 |
| R12-W3 d0 inflation | 改善 | d1-d3 balanced acc 系统性并列，但 Abstract 仍以四类为主 |
| R12-W4 Cross-scale confounds | 部分改善 | 标题改为 Preliminary，但 Abstract 表述仍过度乐观 |
| R12-W5 Curation PoC | 部分改善 | 标记 inconclusive 但 Bonferroni 表述仍有误 |
| R12-W6 Abstract 数字堆砌 | 未修复 | 仍 20+ 数字 |
| R12-W7 Discussion 过薄 | 部分改善 | 从 ~80 词扩展到 ~250 词，但仍不足 |
| R12-W8 Feature importance 共线性 | 部分改善 | 添加脚注 caveat 但 Table 3 仍展示个体 importance |
| R12-W9 算法贡献不足 | 改善 | Introduction 明确 empirical contribution 定位 |
| R12-M1 EDD threshold | 可能已修复 | 添加 T 敏感性分析 |
| R12-M2 RF ordinal claim | 可能已修复 | 弱化为 ordinally consistent predictions |
| R12-M3 Reference model 重叠 | 恶化 | 新增误导性 "no systematic advantage" claim，与 Table 8 矛盾 |
| R12-M4 Prompted gen 1/9 | 部分改善 | 添加 single-cell qualifier |
| R12-M6 孤儿 bib | 复发 | c2pa2024 删除但新增 3 条孤儿 |
| R12-M7 GPU claim | 可能已修复 | 修正为 CPU ~50 min |
| R12-M8 遗漏引用 | 可能已修复 | muennighoff + ilyas 已入 bib |