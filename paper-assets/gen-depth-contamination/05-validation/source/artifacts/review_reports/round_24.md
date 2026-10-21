---
round: 24
review_mode: fresh
overall_score: 3.0 (Findings)
timestamp: 2026-05-22T05:49:23.064499+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Consolidated Review Report — gen-depth-contamination
## Round 24 (Fresh Review, 2026-05-22)
## Venue: EMNLP 2026 (ARR May 2026) | Deadline: 2026-05-25

---

## Summary

本文提出 generational depth estimation，测量递归合成文本的可区分深度边界 K\*\_empirical——使用 15 个统计特征 + OBD-LightGBM 分类器，在 10 个模型配置（6 个架构族, 1B-8B）、3 个文本域、4 种解码策略上实验，发现 K\*\_empirical ∈ {1,2,3}，一般 web 文本以 K\*=2 为主导模式（6/10 配置），arXiv 学术文本 K\*=3。论文验证了跨模型迁移能力（80-100% 精度保持）和 K\*-aware 数据过滤的下游效用。

---

## Strengths

**S1. 新颖的问题形式化。** Generational depth estimation 填补了 binary detection（人 vs. 机器）与 model collapse 宏观动力学之间的真实空白。K\* 概念定义清晰、可操作（Eq.1: max{k ≥ 1 : AUC\_{k-1,k} > θ}），是对现有文献的有意义扩展。

**S2. 统计方法论严谨度高于同类工作。** Bootstrap 95% CI（1,000 resamples）、permutation test（p ≤ 0.002）、Cohen's h 效应量（h ≈ 0.20）、5-fold GroupKFold 交叉验证（按 seed document 分组防泄漏）——这套统计体系在 NLP 实证论文中不常见。

**S3. "One-wash laundering" 洞察有实践价值。** K\*=2 意味着一次生成就足以让 web 文本与更深层合成内容不可区分，对数据策展有直接指导意义：对 web text 而言，超越 binary 过滤的更精细深度策略是不必要的。

**S4. 跨模型迁移设计精巧。** Cross-scorer validation 和 scorer-invariant feature ranking（ρ > 0.90）共同提供了有部署价值的方法论贡献。Continuation-mode 分类器在 Pythia↔OLMo 间保持 90-92% 迁移准确率。

**S5. Limitations 诚实详尽。** 7 条主要局限 + Extended Appendix（retrain-chain, dose-response），主动暴露了 threshold sensitivity、feature-set dependence、marginal boundary cases。

**S6. 模型覆盖面在 ≤8B 范围内合理。** 6 个架构族、rewrite + continuation 两种模式、4 种解码策略、3 个文本域——消融设计系统全面。

---

## Weaknesses

### Critical — Must-Fix

**W1 [Critical, Consensus]** 附录至少 5-6 个数据表为空占位符

两位 Reviewer 独立发现至少 5 个附录表数据完全缺失：
- Table 21 / S12（跨域 pairwise AUC）：21 个数据单元格全为 em-dash
- Table 24（Three-way ANOVA: Generator × Scorer × Depth-Pair）：F/p/η²\_p 全部为 `---`，但标题声称 "non-significant Scorer main effect confirms scorer independence"
- Table S10（Pythia 解码消融）：30 个 AUC 值全空
- Table S11（长度消融）：15 个 AUC 值全空（仅 K\* 行有值）
- Table S13（Scorer sensitivity）：5/7 generator 的 cross-scorer K\* 为 `---`

这构成系统性投稿质量问题。ANOVA 空表尤其严重——scorer independence 是论文 cross-model transfer 核心支柱，表标题直接下了结论但无任何数据支撑。主文 Section 4.5 引用了具体数值（如 "Wikipedia yields K\*=2, AUC: 0.623"），但完整逐深度对数据缺失。

**W2 [Critical, Consensus]** Cross-scorer 验证部分证伪了 scorer independence claim

Qwen-continuation 自身打分 K\*=2（1v2 AUC = 0.611, CI lower = 0.602, 仅超过 θ 约 0.002），但 Pythia 打分 AUC = 0.5923 < θ，OLMo 打分 AUC = 0.5858 < θ，K\* 均降为 1（Table 22, Agreement=×）。Discussion 仍写 "Cross-scorer validation confirms K\*\_empirical is governed by the generation process rather than the scoring model"，用 feature ranking ρ 替代 K\* agreement 是 misleading——feature ranking 一致不等于 K\* 判定一致。仅 Qwen-rewrite（信号最强配置, 1v2 AUC = 0.696）在 cross-scorer 下保持 K\*=2。

### Major — Should-Fix

**W3 [Critical-Major, Divergence]** K\*\_empirical framing: "the discrimination boundary" vs "feature-specific lower bound"

- **R2 (Critical)**：Title/Abstract/Introduction 将 K\*\_empirical 定位为 "the discrimination boundary"，但 Limitation 5 承认它是 "feature-set-specific lower bound"，neural probe K\*\_neural∈{1,2,3} 随模型变化。正文与 Limitations 之间存在系统性 overclaiming。
- **R1 (Warning)**：Section 3.1 Eq.1 前已写 "We define the operational lower bound"，K\*\_empirical 同时是 empirical boundary 和 K\*\_theory 的 lower bound，两层含义不矛盾。是措辞精度问题，未达 systematic overclaiming。
- **共识方向**：至少 Abstract 和 Introduction 应引入 "lower bound" 限定语（如 "a lower bound on the discrimination boundary"）。

**W4 [Major, Consensus]** Filtering 在现实污染比例下实用价值消失

Appendix D.8 dose-response 分析：10% 污染所有策略无差异（Δ\_max = 0.03pp, p > 0.8）；30% 不显著（p > 0.3）；50% 不显著（p = 0.12）。仅 100%（非现实场景）下有显著效果（0.77pp 改善）。主文 Section 5 仅报告 100% 设定，将 filtering 作为 contribution 呈现。应重新定位为 consistency check，在正文中提及 dose-response convergence。

**W5 [Major, Consensus]** Qwen 家族过度代表

4/10 配置来自 Qwen（Qwen-rw, Qwen-cont, Qwen-base, Qwen-7B），全部 K\*=2。按家族去重：K\*=2 确认 3 个家族（Qwen, LLaMA, Pythia-1.4B），K\*=1 确认 3 个家族（OLMo, Mistral, Gemma），Pythia 分裂（1.4B=2, 6.9B=1）。"6/10 configurations yield K\*=2" 变为 "3/6 families (+1 split)"。应同时报告 per-family 和 per-configuration 统计。

**W6 [Major, Consensus]** 缺少 >8B 模型，scale trend 可能使结论失效

0v1 JSD 随模型规模降低（0.15-0.27 at ≤1.5B vs. 0.077 at 8B LLaMA-3.1）。论文推测 "models at 13B+ may increasingly yield K\*=1"。若属实，K\*=2 仅适用于中小模型，前沿模型可能都是 K\*=1，缩小实践相关性。应在 Abstract/Conclusion 明确标注 ≤8B 适用范围。

**W7 [Major, Divergence]** arXiv K\*=3 证据基础

- **R2 (Major)**：仅 2 个模型, n=2200，但作为平行贡献呈现。
- **R1 (Rebut)**：Table 4 full 实际覆盖 5 模型/4 家族（Qwen-1.5B, Qwen-7B, Pythia-1.4B, LLaMA-8B, Mistral-7B），R2 仅看到 Abstract 的 "two architectures"。
- **共识**：模型覆盖面超出 R2 初判，但 n=2,200 样本量较小，对应的完整 pairwise AUC 支撑表（Table S12/21）为空。

**W8 [Major, Consensus]** 缺少重要相关工作

- Wang, Li, Yan, Cheng, Zhang (ACL 2025) "Unveiling Attractor Cycles in LLMs" — prompt-chain attractor cycles 与 K\* 直接相关
- Fu, Wang, Chen, Tian, Tao (ICLR 2025) "A Theoretical Perspective: How to Prevent Model Collapse in Self-consuming Training Loops" — collapse 理论条件，K\* 存在的理论背景

### Warning

**W9 [Warning, Consensus]** DPI→AUC 理论桥接不完整。DPI 保证 I(X; Y\_k) 单调递减，但论文应用于 AUC\_{k-1,k}（相邻代际 pairwise 分类精度），两者不等价。应明确 DPI 是 heuristic motivation 而非 strict proof。

**W10 [Warning, Partial Consensus]** θ=0.60 阈值事后选择风险。Cohen's h = 0.20 提供先验理论基础（两位共识），但论文三条"独立"证据中第三条（distributional discontinuity）是 data-driven（R1 指出），应标为 post-hoc confirmatory。

**W11 [Warning, Consensus]** Filtering 仅在单一 generator（Qwen-1.5B continuation）上验证，应至少在 K\*=1 generator 上重复。

### Minor

**W12** [Minor, Consensus] Conclusion 过于简短（3-4 句），应扩展至 5-7 句，加实践建议和局限总结。

**W13** [Minor, Consensus] K\* 符号变体过多（K\*\_empirical, K\*\_theory, K\*\_neural），K\*\_theory 仅作占位符。

**W14** [Minor, Divergence] Abstract 信息密度（R2 认为过高，R1 认为正常）。

**W15** [Minor, Consensus] Table 1 仅列 6 配置但声称 10，应添加脚注或列出全部。

**W16** [Minor] "one-wash laundering" 术语可能混淆（K\*=2 ≠ one-wash 直觉），建议首次使用加说明。

**W17** [Minor] Figure 3/5 x 轴标签可读性差；Table 4 脚注过密。

**W18** [Minor] 引用格式不一致（39 条中 8 条缺 URL）。

**W19** [Minor, Consensus] K\*\_empirical 定义中 max 算子隐含 AUC 单调递减假设，应明确该假设或改用 "连续满足条件的最大 k"。

---

## Reviewer Consensus

两位 Reviewer 达成共识的关键问题：
1. **[AGREE]** 附录 5-6 个空表构成系统性投稿质量问题（Critical）
2. **[AGREE]** Cross-scorer 验证部分证伪 scorer independence claim（Critical-Major）
3. **[AGREE]** Filtering 在 <50% 污染下无显著效果，应重新定位为 consistency check（Major）
4. **[AGREE]** Qwen 过度代表导致 "6/10" 统计夸大（Major）
5. **[AGREE]** 缺少 >8B 模型限制实践相关性（Major）
6. **[AGREE]** DPI→AUC 理论桥接不完整（Warning）
7. **[AGREE]** 缺少 Wang et al. (ACL 2025) 和 Fu et al. (ICLR 2025) 引用（Major）

## Reviewer Divergence

1. **K\*\_empirical overclaiming** (W3)：R1 认为措辞精度问题（Warning），R2 认为系统性 overclaiming（Critical）。共识方向：至少 Abstract/Introduction 需加 "lower bound" 限定。
2. **arXiv 证据基础** (W7)：R1 指出实际 5 模型/4 家族（非 R2 认为的 2 模型），但 n=2,200 样本量和空支撑表关注仍成立。
3. **Abstract 信息密度** (W14)：R1 认为正常，R2 认为过高。
4. **Kirchenbauer watermarking 引用**：R1 建议添加，R2 rebut 认为不同问题域（不纳入 Missing References）。

---

## Questions

**Q1.** 附录 5-6 个空表（Tables S10/S11/S12/S13, Table 21, Table 24）是排版遗漏还是实验未完成？如果数据存在，请提供完整数值。

**Q2.** Qwen-continuation 的 K\*=2 在 cross-scorer 下降为 1（Table 22），如何调和 "K\* is governed by the generation process" 的声明？能否扩展 Table 22 覆盖更多 generator-scorer 组合？

**Q3.** 现实 web-scale 合成内容比例估计为多少？在 10-30% 污染下，K\*-aware curation 的实际增益是什么？

**Q4.** 13B+ 模型若 K\*=1，K\*=2 核心发现是否仅限于正在被淘汰的模型规模窗口？

**Q5.** K\*\_empirical 定义中 max 算子是否隐含 AUC 单调递减假设？是否应改为 "连续满足条件的最大 k"？

**Q6.** Prompt-chain K\*=2 vs retrain-chain K\*≥4：是否测量了本质不同的现象？如何调和？

---

## Missing References

1. **Wang, Li, Yan, Cheng, Zhang (ACL 2025)**: "Unveiling Attractor Cycles in Large Language Models: A Dynamical Systems View of Successive Paraphrasing" — prompt-chain attractor cycles 与 K\* 收敛机制直接相关。[Consensus]
2. **Fu, Wang, Chen, Tian, Tao (ICLR 2025)**: "A Theoretical Perspective: How to Prevent Model Collapse in Self-consuming Training Loops" — 自消费循环中 collapse 的理论条件，K\* 存在的理论背景。[Consensus]

---

## External Review (Stanford Agentic Reviewer)

未配置，不适用。

---

## Visual Layout Check（非评分项）

视觉审查已完成（耗时约 4 分钟）。主要发现：

- **[Critical]** Table 21（p.18）数据全部为 em-dash，与两位 Reviewer 发现一致
- **[Warning]** p.1-2 连续纯文本无 display item，Figure 1 直到 p.3 才出现——在容忍范围内但影响第一印象
- **[Warning]** p.4 单页 3 个 figure（Figure 2/3/4），视觉密度过高，Figure 3/4 尺寸被压缩
- **[Warning]** Figure 4 热图使用红绿配色，对红绿色盲不友好，建议改用 Blue-Orange 或 viridis
- **[Warning]** p.12-13, p.15 大面积空白（Table 10/11/13 布局松散）
- **[Info]** 正文 8 页含 4 figures + 4-5 tables = 8-9 个 display items，密度适中
- **[Info]** Figure 5 x 轴标签 150 DPI 下勉强可读
- **[Info]** 参考文献格式统一，无 [?] 未解析引用

---

## Overall Assessment

**Overall: 3.0 (Findings)**
**Confidence: 4/5**

| 维度 | R1 | R2 | 综合 |
|------|----|----|------|
| Soundness | 3/5 | 3.5/5 | 3/5 |
| Excitement | 3.5/5 | 3/5 | 3/5 |
| Reproducibility | 2/5 | 4/5 | 3/5 |
| Overall | 3.0 | 3.5 | **3.0** |

本文提出了新颖且有意义的 generational depth estimation 概念，K\* 作为递归合成文本可区分深度的操作性度量填补了 binary detection 与 model collapse macro dynamics 之间的真实空白。统计方法论严谨，"one-wash laundering" 发现有实践价值。

当前版本未达 Conference 标准的核心原因：

1. **投稿完整性红线**：至少 5-6 个附录表为空占位符，包括支撑 scorer independence 核心声明的 ANOVA 表。空表格 + 已有结论 = 不可验证的声明。
2. **核心声明被自身数据部分证伪**：唯一完成 cross-scoring 的 continuation 配置（Qwen-cont）显示 K\*=2 是 scorer-dependent 的（Table 22 Agreement=×），与 "K\* governed by generation process" 矛盾。
3. **实用价值存疑**：K\*-aware filtering 仅在 100% 合成（非现实场景）下有显著效果；dose-response 在 <50% 污染下所有策略收敛（p > 0.12）。
4. **统计表述夸大**："6/10 configurations yield K\*=2" 按家族去重后变为 "3/6 families (+1 split)"；K\*\_empirical 被 frame 为 "the discrimination boundary" 而非 feature-specific lower bound。

**修复路径**：填充附录数据（如确为排版遗漏则容易修复）→ 修正 scorer independence 叙事（区分 robust vs marginal K\*=2）→ 校准 filtering utility 定位（consistency check, 非独立贡献）→ 同时报告 per-family 和 per-configuration K\* 统计 → 补充 Wang/Fu 引用。完成后论文有望达到 3.5（Borderline Conference）。

---

## Detailed Comments

### Section 1 (Introduction)
- Model collapse 作为动机但实验几乎全是 prompt-chain，应更早更明确区分两者
- Contribution list 的 filtering validation 应降级为 consistency check
- 应提及 retrain-chain K\*≥4 形成完整图景

### Section 2 (Related Work)
- 缺 Wang et al. (ACL 2025) attractor cycles 和 Fu et al. (ICLR 2025) collapse theory
- 与 Geng et al. Markov convergence 的 K\* 增量贡献区分仍可更清晰

### Section 3 (Method)
- DPI→AUC 桥接不完整，应明确为 heuristic motivation
- K\*\_empirical Eq.1 中 max 算子隐含单调假设，应明确或修改定义
- θ=0.60 三条证据中第三条应标为 post-hoc confirmatory

### Section 4 (Experiments)
- Table 1 应列出全部 10 配置
- Cross-scorer 结果（Table 22）直接削弱 scorer independence 声明，Discussion 措辞需修正
- 按家族去重后 K\*=2 比例显著降低，应双重报告

### Section 5 (Filtering)
- 应重新定位为 consistency check
- 正文需至少一句 dose-response summary（<50% 污染下策略收敛）
- 仅在 Qwen-1.5B continuation 验证，缺 generator 多样性

### Section 6 (Discussion)
- Scorer independence 段落使用 feature ranking ρ 替代 K\* agreement，应修正
- "one-wash laundering" 术语需首次使用说明或改名
- 缺少对 per-family K\* 分布的讨论

### Section 7 (Conclusion)
- 过于简短（3-4 句），应扩展加入实践建议和主要局限

### Abstract
- 至少加 "lower bound" 限定语
- 考虑精简部分定量细节

### Limitations
- 内容诚实详尽，是论文优点

### Appendix
- 5-6 个空表为最严重的投稿质量问题
- Figure 4 配色应改为色盲友好
- p.12-15 布局可优化（减少空白）