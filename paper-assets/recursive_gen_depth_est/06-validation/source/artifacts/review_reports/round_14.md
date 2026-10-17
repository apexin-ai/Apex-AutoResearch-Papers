---
round: 14
review_mode: fresh
overall_score: 3.0
timestamp: 2026-05-21T06:50:28.032521+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 17 (Fresh)

**论文**: How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints
**Venue**: EMNLP 2026 (ARR May cycle)
**截止日期**: 2026-05-25
**审稿模式**: Fresh (重新审稿)
**Reviewer 编排**: 2 名 Reviewer
- Reviewer 1: 方法严谨性 + 实验设计 + 统计有效性
- Reviewer 2: 新颖性 + 贡献充分性 + Related Work 覆盖 + 写作质量

---

## Summary

本文将递归生成深度估计（recursive generation depth estimation）形式化为序数分类问题，构建了覆盖 3 个模型族（Pythia-1.4B, OLMo-1B, GPT-2 XL）× 3 种解码策略（nucleus, temperature, top-k）× 4 个深度的 180K 样本基准数据集。从固定参考模型（Pythia-1.4B）的困惑度分布中提取 19 个统计特征，使用 Random Forest 分类器进行深度分类。提出 Effective Discriminable Depth (EDD) 指标量化可区分深度上限。分布内四分类准确率 68.9–85.9%（d1-d3 balanced: 58.9–81.5%），跨模型迁移 66.4%（d1-d3: 55.4%），跨策略迁移 59.1%（d1-d3: 45.9%），14B 模型 EDD=0。论文定位为 task formalization + systematic empirical characterization。

---

## Strengths

**S1. 问题提出新颖且及时** [R1, R2 共识]
从二元检测（human vs. AI）扩展到递归深度估计是一个自然但未被探索的方向。在 model collapse 日益受关注的背景下，"文本经历了多少轮递归生成"这个问题具有前瞻性。Introduction 从 model collapse → detection gap → depth estimation 建立了清晰的逻辑链。

**S2. 极其系统的实验设计** [R1, R2 共识]
3×3×4 grid + 180K 样本、8 个 generalization axis（跨模型/跨策略/跨规模/跨域/seed replication/accumulation/prompted generation/mixed-depth）、24 页附录覆盖近 30 个子实验。R1 评价："这是近期审稿中见过的最全面的 empirical study 之一。"

**S3. 诚实报告负面结果** [R1, R2 共识]
14B EDD=0、cross-strategy 45.9%、downstream curation PoC 不显著（p>0.4）、跨温度 inverted AUC 等负面结果均被坦诚报告。无 cherry-picking 或隐藏不利证据。

**S4. Perplexity tail statistics 发现有洞察力** [R1, R2 共识]
p90_ppl 在所有 9 cells 中排名 top-2，与 surprisal variance 共同占据 41% Gini importance。Mean perplexity 表现等同 chance (25.1%)，揭示深度信号集中在分布尾部而非均值——对后续工作有指导价值。Group-level ablation（perplexity alone 76.6% vs. full 78.4%）提供了不受共线性影响的验证。

**S5. 理论框架与实验发现的良好对应** [R1]
Tail erosion 理论（§3.5）预测 perplexity tail 特征应主导深度信号，group-level ablation 确认。Scale-dependent attenuation 的理论预测在 14B 实验中得到定性验证。

**S6. 控制实验设计精细** [R1]
Heterogeneous chain + reverse-chain control（Appendix B.15）排除 architecture confound、LOGO + negative control 消除 domain bias（Appendix B.10）、temperature robustness + memorization-prerequisite 发现（Appendix B.7）展示高水平实验工程。

**S7. EDD metric 有独立价值** [R1, R2 共识]
将"可区分深度"从模糊概念形式化为可操作度量，contiguous pairwise AUC 的最长前缀定义简洁，可被后续工作采用。

---

## Weaknesses

### Must-Fix 问题（影响接收决定）

**N1. Full-replacement 假设从根本上限制实用价值** [R1 critical, R2 升级为 critical]

所有实验使用 full-replacement 递归链（每个深度完全替换前一代训练语料），但论文声称的应用场景（§6 "depth-scored data curation"）面对的是 accumulation 场景（合成和人类数据以未知比例共存）。Pilot accumulation 实验仅在 §6 中以一句话报告 "-14 到 -15pp"，无独立 Table、无 per-cell 分解、无 EDD 变化、无统计检验。-14 到 -15pp 相当于 full-replacement baseline 的 ~18% 相对衰减，可能使 OLMo nucleus (65.6%) 等 cell 的 d1-d3 准确率降至 ~50%，接近功能不可用。

R2 的关键洞察：model collapse 文献使用 full-replacement 展示 worst-case 现象是合理的，但本文声称的目标是 data curation 工具——两个目标的实验设计要求根本不同。

**N2. 14B EDD=0 被 self-reference confound 污染** [R1 critical, R2 critical + 承认自身疏漏]

Qwen2.5-14B 使用 self-reference（14B 模型自身计算特征），而主表（Table 2）所有 1-1.5B 实验使用 Pythia-1.4B 作为固定参考模型。这意味着观察到的 EDD=0 可能来自：(a) 纯规模效应，(b) 参考模型从 cross-reference 切换到 self-reference 导致特征语义改变，或 (c) 两者混合。论文在 Appendix B.14 承认此 confound 但未做任何控制实验来分离两个因素。

R1 指出至少需要两个对照：(i) 14B + Pythia-1.4B reference（测纯规模效应），(ii) 1.4B + self-reference（测 reference 切换效应）。R2 承认这是本轮审稿中最有价值的方法论发现，修正了自己 N2 中将 EDD=0 直接归因于规模效应的分析。

补充：7-8B 实验（Llama-3.1-8B 70.2% EDD=4, Qwen2.5-7B 60.1% EDD>5）表明框架在 7-8B 仍有信号，并非 ">7B 完全失效"——更准确的表述是"14B 出现断崖式衰减，且该衰减的归因被 confound 污染"。

**N3. 跨策略迁移 d1-d3 仅 45.9%，策略未知时方法基本失效** [R1 critical, R2 critical]

Cross-strategy transfer 将 d1-d3 balanced accuracy 降至 45.9%（四分类: 59.1%），仅 1.4× chance。d0 recall ≥89% 膨胀了 headline accuracy。在真实部署中解码策略通常未知，这与论文的 data provenance 应用场景根本矛盾。

R1 补充了更严峻的证据：Appendix B.7 跨温度实验 leave-one-τ-out mean d1v2 AUC 仅 0.319，τ=0.5 holdout 时出现 inverted AUC (0.176)——不是"性能下降"而是"特征语义在不同策略下反转"。Two-stage pipeline（策略识别 + per-strategy 分类）恢复 11.5pp 但 presupposes 策略可被识别——循环依赖。

**N4. 严重共线性（VIF>10, 14-16/19 features）下个体特征排名不可靠** [R1 critical, R2 agree with nuance]

19 个特征中 14-16 个 VIF>10，有效独立维度仅 ~4-5。论文引用 Strobl et al. (2008) 和 Hooker et al. (2021) 讨论共线性影响，但并未使用 conditional permutation importance——引用方法论批评但不采纳其建议的"自我矛盾"。Kendall's W=0.90 across 3 methods 不能排除系统性偏差。

R2 的 nuanced 回应：family-level 分析（group-level ablation: perplexity 76.6% vs. full 78.4%）不受共线性影响，支持 perplexity tail 家族主导的结论。但 individual feature ranking（"p90_ppl ranks top-2 in all 9 cells"）在如此共线性下不应如此自信地声称。

**两位 Reviewer 共识**：family-level 结论可靠，individual feature ranking 结论需弱化。

**N5. 方法层面 novelty 不足以支撑 Conference-level long paper** [R2 critical, R1 partial REBUT]

19 个特征全部是标准统计量（perplexity percentiles, surprisal moments, n-gram repetition），分类器是标准 Random Forest，EDD 本质上是 contiguous pairwise AUC 的最长前缀。整个方法管道无 algorithmic novelty。

R1 的 partial REBUT：(1) tail vs. mean 的特征选择并非 trivial（mean perplexity = chance, p90_ppl = 58.3%），(2) EDD 的 formalization 有独立价值（类比 BLEU），(3) "零创新"过于绝对。但 R1 同意就 Conference 标准而言 novelty 偏弱。

**两位 Reviewer 共识**：novelty 不构成 "零"，但不足以支撑 Conference 录用。更适合 Findings 定位。

---

### Should-Fix 问题（影响评分但不一票否决）

**W1. LoRA seed 仅 2 个** [R1, R2 AGREE]
OLMo +3.17pp（CI 不重叠）说明 LoRA 初始化对绝对准确率有非平凡影响。2 个 seed 不足以建立 stability claim。至少需要 5 个 seed。

**W2. 多重比较校正缺失** [R1, R2 AGREE]
脚注声明 p-values 为 exploratory，但 Abstract 和 §6 使用确定性语言。Appendix B.12 Curation PoC 的显著性检验涉及多重比较但未校正。要么全面校正，要么全面弱化结论语气。

**W3. Neural end-to-end baselines 仅测试 ≤125M backbone** [R1, R2 AGREE]
DeBERTa-v3-base (86M) 和 RoBERTa-base (125M) 比 RF 低 20pp，但更大 backbone 可能缩小差距。R2 认为瓶颈更可能是表示空间（PLM 无法线性恢复 perplexity tail statistics）而非参数量，但需更大 backbone 验证。

**W4. BOS-seeded generation 生态效度** [R1, R2 partial REBUT]
主实验使用 BOS-seeded generation。Prompted generation 实验（-13.8pp, Appendix B.27）和 instruction-tuned model 实验（Appendix B.21）部分缓解但未完全解决——instruction-following 场景（实际中最相关）未被测试。R2 指出 §B.21 instruction-tuning 改变 AUC 衰减模式证明 gap non-trivial。

**W5. Binoculars 达到统计等价性能** [R1, R2 AGREE]
Binoculars 11-feat RF: 78.1% vs. 本文 19-feat: 78.4%（p>0.05）。额外 8 个 non-Binoculars 特征边际贡献不显著。削弱了 "19-feature comprehensive pipeline" 的独特价值叙事。论文应更精确地定位贡献为 formulation/benchmark 而非 pipeline 性能优势。

**W6. Wild-data FPR 高达 22.4%，thresholding recall 代价未量化** [R1, R2 AGREE]
GPT-2 XL on C4 FPR 22.4%。Confidence thresholding 降至 2.8% 但 recall/coverage 代价未报告。需 FPR-coverage tradeoff curve。

**W7. §6 Discussion 过于压缩** [R2, R1 AGREE]
3 段 ~250 词，缺少：跨策略失败根因分析、EDD ceiling 突破路径、provenance 工具互补关系、scale-up 路线图。需考虑 8 页限制约束。

**W8. Downstream curation PoC 不显著但 Introduction 暗示应用** [R1, R2 AGREE]
RF-vs-unfiltered p>0.4。RF-vs-random 的 p<0.02 涉及多重比较未校正。Introduction 和 §6 的 "depth-scored data curation" 叙事缺乏实验支撑。

---

## Reviewer Consensus

以下为两位 Reviewer 达成共识的关键判断：

- [AGREE] **评分**: 均给出 3.0 (Findings)，置信度均为 4/5
- [AGREE] **问题重要性**: 递归生成深度估计是有价值的新问题
- [AGREE] **实验质量**: 系统性和诚实度均属上乘
- [AGREE] **Full-replacement 限制** (N1): critical，需要系统性 accumulation 实验
- [AGREE] **14B confound** (N2): critical，需要控制实验分离 scale vs. reference-model 效应
- [AGREE] **跨策略迁移** (N3): critical，需限定 claim scope
- [AGREE] **共线性** (N4): family-level 结论可靠，individual ranking 需弱化
- [AGREE] **Findings 定位**: novelty 不足以支撑 Conference，但 empirical 贡献适合 Findings

## Reviewer Divergence

- [R1 REBUT] **R2-N1 "零创新"**: R1 认为 tail vs. mean 的特征选择和 EDD formalization 有非平凡价值，"零创新"是 overstatement。R2 承认 N1 与自己优势评价第 4 点存在内部张力。最终共识：不是"零"，但不足以支撑 Conference。
- [R1 REBUT] **R2-W1 "Atlas 过度包装"**: R1 认为 atlas 准确描述了系统性制图的实验组织。未解决。
- [R1 REBUT] **R2-W4 "Abstract 信息过载"**: R1 认为信息密度在 *ACL empirical study 中属正常。未解决。
- [R2 partial REBUT] **R1-W4 "BOS-seeded 生态效度"**: R2 认为 prompted/instruction-tuned 补充实验部分缓解。部分解决。

---

## Questions to Authors

1. 能否提供累积（accumulation）场景下的完整结果（至少覆盖部分 cells），包括 accuracy、EDD、per-class recall？pilot 中 -14 到 -15pp 的衰减是在哪个 cell 上测的？
2. 14B 实验中，是否有技术原因无法使用 Pythia-1.4B 作为 cross-reference？如果用 Pythia-1.4B 对 Qwen2.5-14B 文本做特征提取，预期结果如何？
3. 跨策略迁移中，是否尝试过 normalization-based domain adaptation（如 per-strategy z-score normalization）？
4. 对于 Binoculars 近平局的结果，作者如何定位本文的独特贡献——是 formulation/benchmark，还是 method 本身？
5. 14B EDD=0 的根因分析：是 14B 模型 perplexity 分布方差更小，还是 fine-tuning 在大模型上更"gentle"？是否有 per-feature 的 scale-dependent 分析？
6. 深度 >5 时是否存在 saturation？是否有更深的初步数据？
7. 是否考虑过将 depth estimation 与 model attribution 结合（cf. Bevendorff et al. 2025 two-paradigm framework）？

---

## Missing References

**R1 建议**:
- Liang et al. (2023), "GPT Detectors Are Biased Against Non-Native English Writers" — detection bias 与 depth estimation 的公平性直接相关
- Sadasivan et al. (2023) 的 impossibility result 对 ordinal 设定的含义（论文已引用但未讨论）

**R2 建议**:
- "Unveiling Attractor Cycles in Large Language Models: A Dynamical Systems View of Successive Paraphrasing" (2025, arXiv:2502.15208) — iterative paraphrasing 的 attractor dynamics，与递归生成链高度相关
- "The Canary's Echo: Auditing Privacy Risks of LLM-Generated Synthetic Text" (2025, arXiv:2502.14921) — data auditing 角度
- "Data Provenance Auditing of Fine-Tuned Large Language Models" (2025, arXiv:2510.09655) — 数据来源审计

**引用验证**: R2 验证 76 条 bib entries，无幻觉引用。1 条 orphan bib (penedo2024_fineweb)。

---

## External Review

**外部审稿**: 未配置（项目未启用 paperreview.ai）

---

## Visual Layout Check（非评分项）

**状态**: done（耗时 ~3 分钟）

**Warnings (3)**:
1. **Pages 1-3 无视觉锚点**: 连续 3 页纯文本，第一个 display item（Table 1）直到第 4 页才出现。建议将 Figure 1（Atlas 热力图）或 Figure 2（AUC 衰减曲线）前移，或添加 pipeline 示意图。
2. **Page 8 display items 堆叠**: 单页内 4 个 display items（Table 4 + Table 5 + Table 6 + Figure 3），视觉极度拥挤，与前面纯文本形成强烈失衡。
3. **Figure 3 尺寸过小**: 两个混淆矩阵挤在半栏宽度内，数字和 axis label 在正常阅读距离下难以辨认。建议改为 figure*（全宽）或移至 Appendix。

**Info (9)**: 模板合规、booktabs 格式规范、Figure 2 质量最高、无 LaTeX 渲染错误或 margin overflow。

---

## Overall Assessment

**Overall Score**: 3.0 / 5 — Findings（可被 Findings 接收）

**置信度**: 4 / 5（两位 Reviewer 均为 4/5）

**维度打分汇总**:

| 维度 | R1 | R2 | 合并 |
|------|-----|-----|------|
| Soundness | 3.0 | 3.5 | 3.0 |
| Excitement | 3.0 | 2.0 | 2.5 |
| Reproducibility | 4.0 | 4.0 | 4.0 |

**判断理由**:

本文在一个新颖且有前景的问题（递归生成深度估计）上进行了极为系统的实证研究，实验覆盖面和诚实度在该领域罕见。Perplexity tail statistics 主导深度信号的发现有洞察力，EDD metric 有独立贡献价值。

但五个核心限制共同构成 Findings 而非 Conference 的判断：

1. **实用性断裂**: full-replacement 假设与 accumulation 实际场景的差距缺乏系统验证（N1）
2. **规模不可信**: 14B 的 EDD=0 被 self-reference confound 污染，无法可靠归因（N2）
3. **迁移性不足**: 跨策略 d1-d3 仅 45.9%，策略未知时方法基本失效（N3）
4. **统计可信度**: 共线性下个体特征排名不可靠（N4）
5. **Novelty 不足**: 标准特征 + 标准分类器，缺乏方法论创新（N5）

作为 Findings 论文，其系统性实验设计、诚实的负面结果报告、以及对 perplexity tail erosion 作为 depth marker 的实证确认有一定贡献价值。

**提升路径**: 如果作者能在 revision 中 (1) 补充 accumulation 场景的系统实验，(2) 提供 14B cross-reference 控制实验，(3) 补充 conditional permutation importance 或 bootstrap rank stability，(4) 调整 claim scope 为 within-strategy/known-strategy——论文有潜力在下一个 cycle 冲击 3.5–4.0（Borderline Conference 至 Conference）。

---

## Detailed Comments

### §1 Introduction
- 第 5 段 "our contribution centers on task formalization and systematic empirical characterization rather than algorithmic novelty" 的自我定位是诚实的，但可能过于前置——reviewer 在第一页就看到了"无新算法"的声明，影响后续阅读的期望值。建议将此定位移至贡献列表之后。
- 贡献 3 的 "structural barrier in cross-strategy transfer (d1–d3: 45.9%)" 以积极发现的语气呈现了一个本质上的负面结果。建议明确标注为 limitation/boundary condition。

### §3 Method
- §3.2: BOS-seeded generation 的 caveat ("BOS-seeded generation may amplify depth signal") 应更显著——目前只是括号内一句话。
- §3.3: "effective dimensionality ≈4–5" 是重要发现但在特征设计节轻描淡写，应提升到更显著位置并讨论其对 pipeline 简化的含义。
- §3.4: EDD 定义清晰但 T=0.70 的阈值选择依赖 Hosmer (2000) 的一般性 ROC 指南，未针对 depth estimation 场景做 task-specific 论证。

### §4 Depth Degradation Atlas
- §4.1: d0 recall >97% 的 "free points" 效应应在报告 headline accuracy 时明确讨论，而非只在 Table 2 caption 中提及。
- §4.2: "p90_ppl ranks top-2 by Gini importance in all 9 cells" 在 VIF>10 条件下不应如此自信地声称。建议改为 "the perplexity tail feature family consistently dominates across all 9 cells, with group-level ablation confirming..."
- §4.5: strategy effect (9.3pp) > model effect (7.2pp) 是重要发现，但在主文中仅占一段——考虑到这对部署的重大含义，值得更深入讨论。

### §5 Generalization
- §5.1: Binoculars 近平局（78.1% vs 78.4%, p>0.05）应更透明地讨论其对本文独特价值的含义。
- §5.3: "a two-stage pipeline recovers 11.5pp" 但 presupposes 策略可识别——应明确标注为条件性（conditional）结果。
- §5.4: 14B 结果应在主文中明确标注 self-reference confound，而非仅在 Appendix 中讨论。

### §6 Discussion
- 三段过于压缩。建议拆分 Discussion 和 Conclusion。
- "From ceiling to floor" 段的 deployment scenario（depth-scored data curation）缺乏实验支撑（Appendix B.12 PoC 不显著）。
- "Scale dependence and outlook" 段应讨论 self-reference confound 对 scale 叙事的影响。

### Appendix
- 15 页 29 个子节缺乏层级组织，建议按主题分组（Feature Analysis / Generalization / Ablation / Baselines）。
- B.10 Domain Bias Analysis 中 buggy pipeline 数字增加阅读负担，建议移至脚注。
- B.12 Curation PoC 和 B.22 Downstream Fine-Tuning 的 inconclusive 结果应在标题中明确标注（如已标注 "Inconclusive"——这是好的实践）。

### 格式合规性
- ✅ 主文 8 页（pp.1-8），Limitations 从第 9 页开始，合规
- ✅ Double-blind 匿名完整，无作者身份泄露
- ✅ ACL review 模板（acl.sty），booktabs 格式规范
- ⚠️ 1 条 orphan bib entry (penedo2024_fineweb)
- ⚠️ 术语残余不一致（depth estimation vs. depth classification）