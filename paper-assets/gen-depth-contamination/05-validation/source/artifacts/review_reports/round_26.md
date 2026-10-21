---
round: 26
review_mode: fresh
overall_score: 3.0
timestamp: 2026-05-22T08:14:17.791626+00:00
reviewer_ids: ['1', '2']
cross_response_reviewer_ids: ['1', '2']
force_resubmit: False
---

# Round 26 审稿报告 — gen-depth-contamination

**论文**: Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary
**Venue**: EMNLP 2026 (ARR May 2026 cycle)
**审稿模式**: Fresh（重新审稿）
**Reviewer 编排**: 2 人（R1: 方法严谨性 + 实验设计 + 统计有效性; R2: 新颖性 + 完整性 + 相关工作 + 写作质量）
**交叉回应轮次**: 1 轮（Round 1 后即达成共识）

---

## Summary

本文提出 generational depth estimation 任务，定义 K\*\_empirical 为递归合成文本代际判别边界的操作性下界。使用 15 维统计特征 + OBD-LightGBM 分类器，在 10 个模型配置（6 架构族, 1B–8B）、3 个文本域、4 种解码策略上度量 K\*\_empirical。核心发现：通用 web 文本 K\*\_empirical ∈ {1, 2}（6/10 配置 K\*=2, 4/10 K\*=1），结构化学术文本（arXiv）K\*=3。作者将此称为"one-wash laundering"效应，并通过下游 filtering 实验验证 binary curation 是最优策略。

---

## Strengths

**S1. 问题定义清晰且填补真实研究空白。** 将 binary detection 扩展到 ordinal depth estimation 是自然推进。K\*\_empirical 作为操作性度量有明确定义（Eq.1），与 model collapse 文献的 information loss 概念形成桥接。[R1, R2 共识]

**S2. 实验设计系统性强。** 10 个模型配置覆盖 6 个架构族、3 个文本域（C4, Wikipedia, arXiv）、4 种解码策略，实验矩阵设计合理。Cross-model transfer（Section 4.2）、cross-scorer validation（Table 22）、decoding ablation（Table S2）提供多角度验证。[R1, R2 共识]

**S3. C4 主实验统计验证扎实。** Bootstrap 95% CI、10,000-iteration permutation test、Cohen's h effect size 的综合使用在该领域论文中少见。K\*\_empirical 的三重验证增强结论可信度。θ-free sensitivity surface（Figure 3）允许读者在任意阈值下读取 K\*。[R1 特别肯定]

**S4. "One-wash laundering" 有实际指导意义。** Binary filtering 捕获唯一可靠信号、graduated weighting 在 K\* 之后只增加噪声——这一 negative result 对 data curation practitioners 有直接操作性价值。[R1, R2 共识]

**S5. 附录详尽。** 12 页附录覆盖 extended ablation（D.1-D.9）、confusion matrices、token length analysis、seed robustness 等，展示扎实实验工作。Reproducibility 得分高（特征定义 Table 14、超参数 Table 15-16 完整公开）。[R2 特别肯定]

---

## Weaknesses

### Must-Fix（影响接收决定）

**[MF-1] arXiv K\*=3 缺乏 bootstrap CI 和 permutation p-value** [R1 critical, R2 agrees]
- 位置：Table 4 (Section 4.6), Abstract contribution (b)
- 问题：K\*=3 for arXiv 被列为独立贡献，但边界对（2v3 AUC = 0.6436 / 0.6545）无 CI 无 p-value。C4 主实验 Table 2 对所有边界对提供了完整统计验证，arXiv 作为单独贡献却缺乏同等标准。仅 2 个模型家族、n=2,200（低于 C4 的 5,000）。
- 影响：如果 2v3 CI 下界低于 θ=0.60，K\*=3 claim 不成立。无法被读者独立验证的 boundary claim 不应作为独立贡献。
- 建议：补充 arXiv 2v3 bootstrap 95% CI + permutation p-value；在 Abstract/Conclusion 添加覆盖受限 caveat。

**[MF-2] Qwen 过度代表膨胀 "6/10" headline 统计** [R1 critical, R2 critical]
- 位置：Abstract, Section 4.1, Conclusion
- 问题：K\*≥2 的 6/10 配置中 4 个是 Qwen 变体。Per-family：仅 2/6 族一致 K\*=2（Qwen, LLaMA），3/6 族 K\*=1（OLMo, Mistral, Gemma），Pythia 分裂。Abstract 虽含 "(2 of 6 families unanimously)" 但 "6/10" 在前、"2/6" 在括号中，叙事权重偏向前者。
- 影响：读者按 family 计数时，核心发现从"多数配置 K\*=2"变为"仅 2 个族一致 K\*=2"，结论普适性大幅减弱。
- 建议：将 per-family 统计提至与 "6/10" 同等突出的位置（如 "2/6 model families consistently yield K\*≥2, spanning 6/10 individual configurations including within-family variants"）；正文增加 family-level 分析段落。

### Should-Fix（影响评分但不一票否决）

**[SF-1] 核心贡献的叙事张力未充分解决** [R2 critical → R1 should-fix, 共识: should-fix]
- 问题：论文叙事"提出 ordinal framework → 发现 binary suffices"造成内在张力。R2 认为是 fundamental paradox（critical），R1 认为 ordinal framework 作为科学工具建立 negative result 是有效贡献模式（should-fix）。
- 共识：需更明确地 frame ordinal estimation 为"测量工具"——它证明了 binary 为何足够（非假设），揭示了 domain-dependent variation（C4 K\*=2 vs arXiv K\*=3），量化了 boundary sensitivity（Qwen-cont CI = 0.002 above θ）。但当前叙事让读者误以为 ordinal estimation 本身有直接应用价值。
- 建议：Introduction/Discussion 明确区分"验证 binary boundary 的存在"（已知）与"精确量化 boundary 的位置和特性"（新贡献）。

**[SF-2] 遗漏高度相关近期工作** [R2 critical → R1 should-fix, 共识: should-fix]
- (1) **Geng et al. (March 2026)**, "Markovian Generation Chains in LLMs" (arXiv:2603.11228)：研究 LLM 迭代生成链收敛行为，Markov chain 理论框架与本文 Section 3.1 高度重叠。
- (2) **Shahriar et al. (Dec 2025)**, "The Erosion of LLM Signatures" (arXiv:2512.05311)：量化迭代 paraphrasing 后 detection 衰减 ~25.4%，与 one-wash laundering 直接相关。
- 两篇均经 web search 验证真实存在。R1 认为互补但不 subsume 本文（降为 should-fix）。
- 建议：Section 2 添加讨论，明确本文与 Geng et al. 的区别（discrimination boundary 量化 vs. convergence behavior），与 Shahriar et al. 的互补性。

**[SF-3] 边界 CI 决策缺乏多重比较校正** [R1 should-fix, R2 strongly agrees]
- 10 个配置同时检验 CI lower bound > θ，未用 Bonferroni/FDR 校正。Qwen-cont CI 下界仅超 θ 0.002，校正后 99.5% CI 极可能跌破→K\*=2 count 从 6/10 降为 5/10。
- 建议：报告 Bonferroni-corrected CIs，或至少在 Discussion 承认 Qwen-cont 在校正后可能降级。

**[SF-4] DPI conjecture 混淆两个独立论点** [R1 should-fix, R2 agrees]
- K\*\_empirical ≤ K\*\_theory 从特征子集关系可直接推出（15D 是最优特征的子集，AUC 不可能低于子集），不需要 DPI 也不需要 "conjecture"。DPI 仅用于 motivate 经验观察到的 AUC 单调衰减。当前表述将两个论点混为一谈。
- 建议：Lower bound 作为 direct consequence of feature subset 直接声明；DPI 仅用于 motivate 单调衰减。

**[SF-5] θ=0.60 阈值定位需更明确** [R2 should-fix, R1 agrees]
- "Small effect size" (Cohen's h=0.20) 本身主观——为何不用 medium (h=0.50, AUC≈0.67)？Figure 3 提供了 θ-free 连续度量但未在正文充分讨论。
- 建议：将 θ=0.60 定位为"参考操作点"而非唯一正确阈值；正文增加一段总结 Figure 3 的 sensitivity range。

**[SF-6] Filtering 在现实污染比例下失去统计显著性** [R1 should-fix, R2 agrees]
- 100% synthetic 实验显示 binary-ours 优势，但 dose-response（Appendix D.8）：50% 污染 p=0.12，10% 污染 Δ\_max=0.03pp。实际指导价值在现实条件下缺乏 evidence。关键 dose-response 结果放在 Appendix 有 cherry-picking 嫌疑。
- 建议：Section 5 正文增加 dose-response 结果引用，或将 Table 25 移入正文。

**[SF-7] 模型规模覆盖偏向小模型（≤8B）** [R2 should-fix, R1 agrees]
- 实际 web-scale 合成文本来自 100B+ 模型。Discussion 推测"13B+ may yield K\*=1"未验证。
- 建议：Conclusion 更显式限定适用范围；如可能补充 >8B 数据点。

**[SF-8] 文档长度（256 tokens）代表性不足** [R2 should-fix, R1 agrees]
- 512 tokens 时 1v2 CI lower = 0.5979 < θ=0.60。真实 web 文档通常数千 tokens。
- 建议：扩展到 1024+ tokens 实验，或在 Limitations 更显式讨论长度敏感性的实际含义。

### Minor（不影响接收）

- **[m1]** 正文 Table 2 仅展示 5/10 配置，其余在 Appendix Table S2b。建议至少在正文提供 10 配置汇总表或更完整覆盖。[R1-M2, R2-M3]
- **[m2]** OLMo sub-threshold AUC 存在非单调性（2v3=0.497 < 3v4=0.502），应显式标注。[R1-M1, R2 agrees]
- **[m3]** Neural probe "self-familiarity artifacts" 归因为推测而非实验验证，缺少 cross-family probe 对照实验。[R1-M3, R2 agrees]
- **[m4]** ANOVA 使用 GroupKFold 非独立观测值，p-value 可能偏乐观。ANOVA 用于 feature importance 而非核心 K\* 结论，影响有限。[R1-W4 → R2 rebut to minor]
- **[m5]** Abstract 信息密度偏高，单段落含过多技术细节。[R2-M1]
- **[m6]** 标题 "Recursive Synthetic Text" 范围略宽于 prompt-chain 实际覆盖。正文 Section 3.1 已明确协议，影响有限。[R2-W4 → R1 rebut to minor]
- **[m7]** 未明确承诺 code/data release。[R2-M10]
- **[m8]** arXiv preprint 参考文献格式不完全统一（部分有 venue 部分没有）。[R2-M8]

---

## Reviewer Consensus

以下问题两位 Reviewer 达成一致：

1. **[AGREE]** arXiv K\*=3 必须补充 CI（MF-1）——作为独立贡献需同等统计验证
2. **[AGREE]** "6/10" headline 被 Qwen 膨胀（MF-2）——per-family 统计应更突出
3. **[AGREE]** DPI conjecture 混淆（SF-4）——lower bound 从特征子集直接推出
4. **[AGREE]** 多重比较校正缺失（SF-3）——Qwen-cont 边界脆弱
5. **[AGREE]** Filtering 在现实条件下无显著收益（SF-6）——dose-response 应在正文讨论
6. **[AGREE]** θ=0.60 应定位为参考操作点（SF-5）
7. **[AGREE]** 模型规模限制（SF-7）和文档长度限制（SF-8）需更显式讨论
8. **[AGREE]** 正文 Table 覆盖不足（m1）、OLMo 非单调性（m2）、neural probe 归因（m3）

---

## Reviewer Divergence

| 问题 | R1 | R2 | 最终判定 |
|------|----|----|----------|
| 贡献悖论（SF-1） | Should-Fix: ordinal framework 建立 negative result 是有效贡献模式 | Critical: ordinal→binary 构成 fundamental paradox | **Should-Fix**（R1 论证更有说服力——negative result 需要工具来建立） |
| 遗漏引用（SF-2） | Should-Fix: 互补但不 subsume | Critical: Geng et al. 理论框架高度重叠 | **Should-Fix**（两篇研究不同问题，补引用+讨论即可） |
| Section 4.1 标题误导（R2-N2） | REBUT: R2 误读 ≤ 为 ≥，标题"K\*\_empirical ≤ 2"准确 | Critical: 标题暗示所有配置 K\*≥2 | **撤回**（R2 事实性误读，实际标题 ≤ 2 表示上界，无误导） |
| ANOVA 非独立性 | Should-Fix | Minor: ANOVA 非核心结论基础 | **Minor**（R2 论证合理） |
| 标题范围过广 | Minor | Should-Fix | **Minor**（正文已明确协议） |
| Limitations 篇幅 | Minor（接近边界） | 无问题 | **无问题** |
| Overall 评分 | 3.5 (Borderline Conference) | 3.0 (Findings) | 见下方 Overall Assessment |

---

## Questions for Authors

**Q1** [R1, 高优先级]: 能否提供 arXiv 2v3 边界对的 bootstrap 95% CI 和 permutation p-value？这直接关系到 K\*=3 claim 的稳健性。

**Q2** [R2]: 如果在 70B+ 模型上 K\*\_empirical=1，K\*\_empirical 框架在最重要的实际场景下是否退化为 binary detection？你们如何看待框架的长期价值？

**Q3** [R2]: 与 Geng et al. (2026) "Markovian Generation Chains in LLMs" 的理论框架有什么关系？他们的收敛/recurrence 分析能否解释 K\*\_empirical 为何总是很小？

**Q4** [R1]: Eq. 1 的 ∀j 约束被描述为因经验单调性而"naturally satisfied"。在初步实验中是否观察到过 above-θ 的非单调情况？

**Q5** [R1]: 对 K\*=1 的生成器（如 OLMo），filtering 分析会怎样？binary filtering 是否也会失效？

**Q6** [R2]: Table 5 中 Binary K\* filtering 的 MMLU 改善（+0.74pp）的 error bar 是否 overlapping？在 Bonferroni 校正后是否仍显著？

**Q7** [R1]: Prompt-chain 和 retrain-chain 的 K\* 在实际 web-scale 污染（两种机制共存）中如何交互？

---

## Missing References

1. **Geng, Mingmeng, et al. "Markovian Generation Chains in Large Language Models." arXiv:2603.11228, March 2026.** [R2 提出, R1 验证并同意] — 研究 LLM 迭代生成链收敛行为，Markov chain 理论框架与本文 Section 3.1 高度重叠。

2. **Shahriar, Sadat, Navid Ayoobi, and Arjun Mukherjee. "The Erosion of LLM Signatures: Can We Still Distinguish Human and LLM-Generated Scientific Ideas After Iterative Paraphrasing?" arXiv:2512.05311, December 2025.** [R2 提出, R1 验证并同意] — 量化迭代 paraphrasing 后 detection 性能衰减，与 one-wash laundering 直接相关。

3. **Ordinal regression 方法文献** [R2 建议]: 如 Gutiérrez et al. (2016) "Ordinal Regression Methods: Survey and Experimental Study" 或更新的深度学习 ordinal regression 工作，以论证 OBD 为合理 baseline 选择。

---

## External Review (Stanford Agentic Reviewer)

**状态：未请求。** 项目未配置外部审稿（external\_review.paperreview\_ai.enabled 未启用）。

---

## Visual Layout Check（非评分项）

**状态：已完成** (2026-05-22 07:56–08:00, 约 4 分钟)

### 发现

| 严重性 | 位置 | 问题 |
|--------|------|------|
| **Critical** | Page 8 | 主正文最后一页仅约 15 行结论（~20% 页面），~75% 为空白。8 页限制实际使用约 7.2 页。审稿人可能认为内容不够充实。建议将部分 Appendix 核心内容提升至正文。 |
| Warning | Pages 1-2 | 连续两页纯文本（Abstract + Intro + Related Work），无 display item。Figure 1 延迟到第 3 页。建议将 Figure 1 提前。 |
| Warning | Pages 7-8 | Discussion + Conclusion 跨两页纯文本，与第 8 页大面积空白形成反差。建议在 Discussion 加入汇总性 figure/table。 |
| Warning | Pages 13-14 | 附录 Table 10/11 上方大面积空白，建议合并或调整 float。 |
| Warning | Page 11 | Figure 5 bar chart 部分柱颜色饱和度低，灰度打印可能难辨。建议添加 hatch pattern。 |

### 正面发现
- Pages 3-6 视觉节奏良好，text-figure-table 交替出现
- 所有表格统一 booktabs 风格，最优值加粗，小数位一致
- 主正文 9 个 display items / 8 页，密度适中
- 无 margin 溢出、公式渲染错误、[?] 未解析引用
- Figure/Table 编号连续，参考文献格式统一

---

## Overall Assessment

**Overall Score: 3.0 (Findings)**
**Confidence: 4/5**
**评分区间: R1=3.5 (Borderline Conference), R2=3.0 (Findings)**

### 判定理由

本文填补了一个真实的研究空白（无方法估计递归合成文本的代际深度），K\*\_empirical 指标定义清晰，C4 主实验统计验证扎实，"one-wash laundering"发现对 data curation 有实际指导意义。

阻碍 Conference 推荐的核心问题：

1. **arXiv K\*=3 统计验证不完整**（MF-1）：作为独立贡献缺乏 CI，无法判断稳健性
2. **Headline 统计被 Qwen 膨胀**（MF-2）：per-family 视角下跨族证据薄弱（2/6 unanimous）
3. **贡献叙事张力**（SF-1）：ordinal framework → binary conclusion 的增量贡献论证不够清晰
4. **Filtering 实用性受限**（SF-6）：现实污染比例下无统计显著收益
5. **模型规模/文档长度限制**（SF-7, SF-8）：1B–8B、256 tokens 的结论难以直接迁移到实际场景

### 提升路径

- **3.0 → 3.5 (Borderline Conference)**：补充 arXiv CI（若支持 K\*=3）+ 修正 headline framing + 补充 missing references + 正文讨论 dose-response
- **3.5 → 4.0 (Conference)**：需增加 non-Qwen 家族的 K\*=2 证据（如更多 7B+ 模型）、解决多重比较校正后 Qwen-cont 边界问题、扩展 filtering 到多模型/多任务

### ARR 维度评分汇总

| 维度 | R1 | R2 | 共识 |
|------|----|----|------|
| Soundness | 3.5 | 3.5 | 3.5 |
| Excitement | 3.0 | 2.5 | 2.75 |
| Reproducibility | 4.0 | 3.5 | 3.75 |

---

## Detailed Comments（逐节）

### Abstract
- 信息密度偏高（m5），一个段落含过多技术细节
- "6/10 configurations (2 of 6 families unanimously)" 叙事权重偏向前者（MF-2）
- "a conventional small-effect-size threshold" 比原 Cohen's h 表述更好，但仍可能让读者困惑 θ=0.60 的具体含义

### Section 1 (Introduction)
- Contribution (a) 的 K\*\_empirical 度量需更明确强调其作为"测量工具"的方法论价值（SF-1）
- Contribution (b) 的 arXiv K\*=3 需 caveat（MF-1）
- 最后一段的 filtering consistency check 表述恰当（"as a consistency check"）

### Section 2 (Related Work)
- 覆盖 binary detection、model collapse、data selection 的主要工作
- 遗漏 Geng et al. (2026) 和 Shahriar et al. (2025)（SF-2）
- OBD 方法选择缺少 ordinal regression 方法论文献支撑（Missing Ref #3）

### Section 3 (Method)
- DPI conjecture 混淆 lower bound 和 monotonicity 两个独立论点（SF-4）
- θ justification 三重验证结构好，但应更明确定位为"参考操作点"（SF-5）
- Eq.1 定义（∀j≤k 连续满足）比原 max 定义更严谨
- 特征定义完整（Table 14），OBD 描述清晰

### Section 4 (Experiments)
- C4 主实验统计验证扎实（bootstrap CI + permutation test）
- Table 2 仅展示 5/10 配置（m1）
- arXiv Table 4 缺 CI（MF-1）
- Cross-scorer validation（Table 22）三层分析有价值，但 ANOVA 独立性假设有瑕疵（m4）
- Neural probe self-familiarity 归因为推测（m3）

### Section 5 (Filtering)
- "Consistency Check" 定位恰当
- 100% synthetic 上限实验 + dose-response 分析框架合理
- Dose-response 关键结果（≤50% 无显著差异）应在正文展示（SF-6）
- 单一模型/数据集验证范围不足

### Section 6 (Discussion)
- "One-wash laundering" 解释清晰
- "What K\*\_empirical reveals" 四点 epistemological contribution 部分回应了贡献悖论（SF-1），但需更突出
- "13B+ may yield K\*=1" 推测应在 Conclusion 更显式限定
- Boundary cases 分析详细

### Section 7 (Conclusion)
- 适当长度，覆盖主要发现和 future work
- 需加强 scope limitation（1B–8B, prompt-chain）的显式度

### Limitations
- 覆盖 7 个限制点，内容充实。EMNLP 规则下不计入页数，篇幅可接受
- 建议增加 generation prompt template 多样性的讨论

### Ethics Statement
- 讨论了正面用途和双用风险，内容充分

### Format Compliance
- ✅ 正文 ≤ 8 页（实际约 7.2 页，第 8 页大面积空白——视觉审查标记为 critical）
- ✅ ACL 模板 `\usepackage[review]{acl}`
- ✅ 双盲 `\author{Anonymous}`
- ✅ Limitations 和 Ethics Statement 存在且不计入页数
- ✅ 无匿名违规
- ⚠️ 未承诺 code/data release