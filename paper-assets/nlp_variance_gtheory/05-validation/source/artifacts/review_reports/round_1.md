---
round: 1
review_mode: fresh
overall_score: weak reject
timestamp: 2026-05-22T03:26:55.281114+00:00
reviewer_ids: [1, 2, 3]
cross_response_reviewer_ids: [1, 2, 3]
force_resubmit: False
---

# 审稿报告：Format-Conditional Variance Structure in LLM Evaluation: A Generalizability Theory Approach

**目标 Venue**: AAAI 2027 Main Technical Track
**审稿团队**: 3 名 Reviewer（R1: 方法/统计 6/10, R2: 新颖性/定位 5/10, R3: 写作/格式/复现 5/10）
**审稿模式**: Fresh（重新审稿） | **日期**: 2026-05-22
**交叉回应**: 全部完成，1 轮达成共识

---

## Summary

本文将心理测量学中的 Generalizability Theory (G-theory) 应用于 LLM 评测方差分解，通过 7-facet 全交叉设计（item, model, precision, prompt, seed, temperature, ordering）在 8 个 7-9B 模型和 5 个 benchmarks 上分析了 2.3M 评测记录。核心发现是方差结构具有 format-conditional 特性：multiple-choice benchmarks 中 item-related variance（item + model×item）集中（>65%），而 free-form benchmarks 中方差分散于多个来源（5-24% each）。论文还提出 D-study budget calculator，证明 multi-facet 设计比 single-condition 设计效率高约 10×（55 vs 552 items for G≥0.80）。

---

## Strengths

**S1. 实验规模和设计严谨性 [全员共识]**
7-facet 全交叉设计覆盖 8 模型 × 5 benchmarks × 2.3M records，在 LLM 评测方差分析文献中属 top-tier 规模。Table 1 的 design matrix 展示了对 factorial experiment 的深入理解。

**S2. Format-conditional 发现的描述性价值 [全员共识]**
Table 3 中 MC vs. FF benchmarks 的方差结构差异在描述性层面非常显著——即使形式化统计检验效力不足（见 W1），效应量本身（Cohen's d=1.73, 均值差 CI [11.44, 21.02] pp）仍有实际参考价值。

**S3. D-study budget 的实践导向 [全员共识]**
将 G-theory 分析转化为 D-study projection curves 和可操作的 item budget 建议（multi-facet 55 items vs. single-condition 552 items），填补了从"学术分析"到"实践工具"的桥梁。

**S4. Binary data 处理的方法论认真度 [R1, R2]**
Henderson Method I + 四项 robustness check（simulation ρ=0.732, GLMM complement ρ=1.0, accuracy-range stability r=-0.048, estimator guarantee）展示了对心理测量方法迁移的严肃处理。

**S5. Precision separability 的实用价值 [R1, R3]**
BF16/FP16 在 binary scoring 下可互换（<0.1% interaction）对评测实践者有直接指导价值。

---

## Weaknesses

### Must-Fix（影响接收决定）

**W1. [CRITICAL] "Format-conditional" 核心 claim 的统计支撑全面不足 [全员共识]**

论文标题和 Contribution 1 同时面临三重证据缺陷：

(a) **Permutation test 从设计上无法拒绝 H₀**：5 个 benchmarks 分为 3 MC + 2 FF，C(5,2)=10 种划分，p=0.10 是数学上可达到的最小 p 值。α=0.05 下永远不可能显著。Abstract 和 Conclusion 仍使用断言式语言。

(b) **MC/FF 二分法内部不一致**：R1 数据核查揭示，3 个 MC benchmarks 中仅 MMLU 呈现 clear item dominance（37.9% vs 30.2%），ARC 的 item 和 model×item 完全持平（均 33.7%），HellaSwag 则逆转（item 34.3% < model×item 36.0%）。"Item selection dominates in MC" 仅对 1/3 MC benchmarks 成立。

(c) **Cohen's d=1.73 在 n₁=3, n₂=2 下 CI 极宽**（约 [-0.5, 4.0]），包含零。

**R1 建设性建议**：所有 MC benchmarks 的 item+model×item 合计 >65%（MMLU 68.1%, ARC 67.4%, HellaSwag 70.3%），而 FF <45%。建议将叙事从 "item dominates in MC" 重构为 "item-related variance (item + model×item) concentrates differently across formats"。

**W2. [CRITICAL] "Hidden second-largest source" 的 novelty overclaim [全员共识]**

Model×item interaction 在 IRT 文献中已被广泛讨论和量化（Pezeshkpour & Hruschka 2024, Zhou et al. AAAI 2026 Oral, Maia Polo et al. 2024）。称已知现象为 "hidden" 缺乏文献支撑。G-theory 的增量在于将此 interaction 置于 7-facet 同时分解框架中量化其相对占比，而非首次"发现"它。建议改为 "the second-largest component in our multi-facet variance decomposition, consistent with prior IRT findings on differential item functioning"。

**W3. [CRITICAL] 可复现性三重缺陷 [全员共识]**

(a) **8 个模型名称和版本未列出**：仅提及 Llama-3.1-8B-Instruct，其余 7 个未知。模型选择直接影响所有 variance component 估计——如果模型同质性高，model facet 和 model×item 可能被系统低估。R1 强调这使得 quasi-random facet 假设无法评估。

(b) **6 个 prompt template 内容未公开**：prompt 是 7 个 facet 之一，其设计空间直接影响 prompt variance 和 prompt×item interaction 估计。

(c) **缺少 AAAI 强制要求的 Reproducibility Checklist**：AAAI-26 明确要求，2027 预计延续。对于以 "reproducibility budgets" 为核心贡献的论文，自身未达到 venue 的可复现性标准构成根本矛盾。

**W4. [CRITICAL] Model facet scope 与标题泛化不匹配 [全员共识]**

8 个 7-9B 参数的 open-weight instruction-tuned 模型不能代表 "LLM Evaluation" 的一般情况。不含 base models、API models（GPT-4, Claude）、小模型（<7B）或大模型（70B+）。如果方差结构随模型规模变化，核心结论的适用范围需大幅限缩。Title/Abstract 应限定 scope。

**W5. [CRITICAL] "10.0× fewer items" 核心实用 claim 缺少置信区间 [全员共识]**

55 vs 552 items 是点估计。Henderson Method I 的方差分量估计在小 facet levels（n_model=8）下偏差不可忽略，D-study projection 是这些估计的函数，uncertainty 会被 propagated。无 CI 的 "10×" claim 在统计上 misleading。论文应通过 bootstrap 计算 D-study projection 的 CI。

**W6. [CRITICAL] 遗漏直接相关文献 Madaan et al. (2024) [R1, R2 共识; R3 部分同意]**

Madaan et al. (2024, arXiv:2406.10229) "Quantifying Variance in Evaluation Benchmarks" 覆盖 13 benchmarks 和 280+ models，与本文研究问题高度重叠。R3 指出两者方法可能不同（sensitivity analysis vs. G-theory），因此不一定是"直接竞争"，但遗漏如此相关的高影响力文献是重大学术缺失。

### Should-Fix（影响评分）

**W7. IRT 对比不公平 [全员共识]**
Section 6 将 IRT-selected 116 items（G=0.457）与 G-theory multi-facet design（55 items）对比，但 IRT 优化 item discrimination，G-theory 优化跨 facet generalizability——目标函数不同。用 G coefficient 评估 IRT 对 IRT 天然不利。应明确为 illustrative comparison。

**W8. Bootstrap resampling unit 未说明 [全员共识]**
"1,000 bootstrap resamples" 未指明 resampling unit（item-level / observation-level / block-level）。在 crossed factorial design 中，resampling strategy 直接影响 CI 有效性。

**W9. Appendix robustness analyses 不可验证 [全员共识]**
5 项 robustness check 各仅 1-2 句话，无方法描述、无统计细节、无结果表。Page 9 附录仅填充约 25% 页面，75% 空白——极不专业。建议大幅扩展或移入 supplementary material。

**W10. Messing (2026) 可验证性存疑 [全员共识]**
论文多次引用 Messing (2026) 作为 G-theory 在 LLM 评测中的先驱工作，但 R2 在 arXiv/Google Scholar/Semantic Scholar 多平台搜索未找到。如不可验证，positioning narrative 需完全重构。需在 rebuttal 中提供完整引用信息和访问链接。

**W11. G-theory 术语对 AAAI 读者可访问性不足 [全员共识]**
Facet, universe of admissible observations, Henderson Method I, D-study 等术语对 AAAI 的 broader AI 读者群需更多直觉解释。建议增加 "G-theory for ML practitioners" 桥接段落。

**W12. 200 items 的 10 个 MMLU subject 选择标准不完整 [R1, R3]**
MMLU 有 57 个 subjects，选了 10 个但未说明标准。如偏向某类则 item variance 估计可能被偏置。

**W13. Exp-002 reduced crossing 可能引入 confounding [R1, R2]**
Exp-002 简化为 BF16 only × 2 temperatures，precision×temperature interaction 被吸收进残差。需提供 exp-001 BF16-only subset 的方差分解对比证明合理性。

**W14. 缺少 tetrachoric-based G-theory 对比 [R1, R2]**
心理测量处理 binary data 的标准方法是 tetrachoric correlation。选择 Henderson Method I 应提供方法论 justification 和 sensitivity comparison。

**W15. Item resampling 仅 3 个样本 [全员共识]**
3 个 resampled datasets 不足以刻画 variance components 的 sampling distribution。建议增至 ≥30 次。

**W16. 贡献排列和 weight 分配不恰当 [全员共识]**
Precision separability 是 confirmatory negative finding，不应与 format-conditional structure 和 D-study budgets 并列为同级贡献。建议重组为 2-3 核心贡献 + 辅助发现/工具。

**W17. 更多遗漏的相关工作 [R2, R3]**
除 Madaan et al. 外，还遗漏 arXiv:2601.02370 (Variance-Aware LLM Annotation), arXiv:2602.15532 (Construct Validity), arXiv:2505.08245 (LLM Psychometrics systematic review)。另 Hua et al. (EMNLP 2025) 已被引用但 Related Work 中未讨论其方法论含义（prompt sensitivity 可能是 evaluation artifact）。

---

## Reviewer Consensus [AGREE]

以下问题获得全部 3 位 Reviewer 的明确共识（交叉回应中全部 AGREE）：

1. **Permutation test p=0.10 是理论最小值**——format-conditional claim 缺乏形式化统计支撑
2. **MC/FF 二分法内部不一致**——HellaSwag anomaly + ARC 持平 = 3 个 MC 中仅 1 个呈 clear item dominance
3. **Model facet scope 过窄**——8 个 7-9B models 不能支撑 "LLM Evaluation" 的泛化表述
4. **"10×" claim 缺 CI**——核心实用贡献需要 uncertainty quantification
5. **"Hidden" model×item 是 overclaim**——IRT 文献早已讨论，G-theory 增量是量化框架
6. **可复现性三重缺陷**——模型名、prompt 内容、reproducibility checklist 全部缺失
7. **修辞强度与证据强度不匹配**——Abstract/Conclusion 断言式语言与弱统计证据不一致
8. **Appendix 不可验证**——5 项 robustness 各一句话
9. **Bootstrap resampling unit 未说明**——关键方法细节缺失
10. **IRT 对比不公平**——不同优化目标，应标注为 illustrative

---

## Reviewer Divergence

1. **AAAI venue 适配度**：R2 认为更适合 ACL/EMNLP（缺算法创新）；R1 和 R3 反驳（AAAI 2026 已接收 Zhou et al. IRT paper 为 Oral，跨学科方法论适合 AAAI）。**多数意见：venue 适配度可接受。**

2. **Results 数字密度**：R3 认为过高；R1 和 R2 认为方差分解论文可接受，建议补充 visualization 而非删数字。**多数意见：可接受，补视觉摘要。**

3. **Madaan et al. 定性**：R2 称"直接竞争者"；R3 部分反驳（方法不同，是"相关但互补"）。R1 同意 R2。**多数意见：应引用，具体定性由作者在 Related Work 中阐明。**

---

## Questions to Authors

1. 能否提供全部 8 个模型完整名称、版本号和参数量？
2. 能否公开 6 个 prompt template 完整文本？
3. Bootstrap CI 的 resampling unit 是什么？
4. Messing (2026) 的 arXiv ID 或 DOI？
5. D-study "55 items for G≥0.80" 的 CI？若 variance components ±10%，所需 items 范围？
6. Cohen's d CI 报告为 [11.44, 21.02]——这是 mean difference CI 还是 d 的 CI？
7. 200 items 来自 MMLU 哪 10 个 subjects？选择标准？
8. 扩展 model facet 到 70B+，预期方差结构如何变化？
9. LOMO 8 个子集中方差结构变化最大的是移除哪个模型时？
10. Hua et al. (EMNLP 2025) 的发现（prompt sensitivity 可能是 artifact）如何影响本文 prompt variance 的解读？

---

## Missing References

1. **Madaan et al. (2024). "Quantifying Variance in Evaluation Benchmarks." arXiv:2406.10229** [全员共识应引用]
2. **arXiv:2601.02370 (2026). "Variance-Aware LLM Annotation"** — G-theory 在 LLM 领域另一应用 [R2]
3. **arXiv:2602.15532 (2026). "Quantifying Construct Validity in LLM Evaluations"** — 互补 psychometric 视角 [R2]
4. **arXiv:2505.08245 (2025). "Large Language Model Psychometrics: A Systematic Review"** — 系统综述 [R2]

注：Hua et al. (EMNLP 2025) 和 BrittleBench (2026) 已被引用，但前者在 Related Work 中未充分讨论其方法论含义。

---

## External Review (Stanford Agentic Reviewer)

**状态**：未请求（项目未配置外部审稿）

---

## Visual Layout Check（非评分项）

视觉审查已完成（耗时 ~2.5 分钟）。1 critical + 3 warning + 5 info：

| 严重性 | 位置 | 发现 |
|--------|------|------|
| ⛔ critical | Page 9 | Appendix 仅填充约 25% 页面，底部 75% 空白。投稿论文出现大面积空白极不专业。建议扩充内容或整合入 supplementary material。 |
| ⚠️ warning | Page 1-2 | 前 2 页连续纯文本，第一个视觉锚点（Table 1）第 3 页才出现。建议将 Figure 1 前移至第 2 页。 |
| ⚠️ warning | Page 6 | 单页 3 个 display items（Table 3 + Figure 2 + Table 4），视觉拥挤。建议将 Table 4 移至第 7 页。 |
| ⚠️ warning | Page 1-7 | 主文恰好 7 页（符合 AAAI 限制），无额外页面预算。注：视觉审查误判为未用完预算，实为 AAAI 7 页限制而非 EMNLP 8 页。 |
| ℹ️ info | Page 6 | Figure 2 legend/axis 字号偏小（约正文 60-65%），打印可读性有风险。 |
| ℹ️ info | Page 4 | Figure 1 部分浅色与白色背景对比度低，建议检查灰度打印。 |
| ℹ️ info | Page 5-6 | Table 2, 3 booktabs 格式规范，粗体标注 dominant component，质量良好。 |
| ℹ️ info | Page 7 | Figure 3 D-study curves 清晰可读，阈值标注明确。 |
| ℹ️ info | Page 8 | References 排版正常，无未解析引用。 |

---

## Overall Assessment

**评分：Weak Reject**
**置信度：High（三位 Reviewer 均 confident，交叉回应达成广泛共识）**
**评分分布**：R1 6/10 (Weak Accept), R2 5/10 (Borderline Reject), R3 5/10 (Below Threshold)

**核心判断**：论文在实验规模（2.3M records, 7-facet fully crossed design）和方法论严谨性（Henderson Method I + robustness checks）上展示了高水平的工程和分析投入。D-study budget 工具有明确的实践价值。然而，当前版本存在系统性问题导致不满足 AAAI 接收标准：

1. **核心 claim 的证据链断裂**："Format-conditional variance structure" 是论文标题和 Contribution 1，但支撑它的统计检验先天无法拒绝 H₀（permutation p=0.10 = minimum achievable），MC 内部 pattern 不一致（仅 1/3 呈 clear item dominance），且效应量 CI 包含零。

2. **Novelty framing 过度**："Hidden" model×item interaction 在 IRT 文献中不 hidden；G-theory 的增量是量化框架，论文应重新定位贡献为分析工具而非发现。

3. **可复现性严重不足**：8 个模型名称和 6 个 prompt template 未公开，缺 reproducibility checklist——对于以 "reproducibility budgets" 为卖点的论文，这是根本矛盾。

4. **统计论证系统性偏弱**：D-study "10×" 无 CI，bootstrap 细节缺失，robustness appendix 不可验证，item resampling 仅 3 次。

**修改路径**：
- 大多数问题可通过 targeted revision 解决（模型列表、prompt 公开、checklist 补充、CI 计算、claim 措辞调整）
- 核心叙事需从 "format-conditional dichotomy" 重构为 "item-related variance concentration gradient across benchmarks"——R1 指出所有 MC 的 item+model×item >65% vs FF <45%，这一 pattern 更稳健
- 考虑增加 2-3 个不同规模模型验证 scale-invariance，或明确限定 scope
- Messing (2026) 可验证性需立即确认

**底线**：论文有真正的方法论贡献（multi-facet G-theory framework + D-study budget），但需显著修改后才能达到 AAAI 接收标准。如解决 W1-W6 中的 critical issues，评分可提升至 borderline accept 到 weak accept 区间。

---

## Detailed Comments

### Abstract
- "The variance structure is format-conditional" → hedged: "Our results suggest a format-associated pattern in variance structure"
- "Model×item interaction (up to 36%) is the hidden second-largest component" → 删除 "hidden"
- "10.0× fewer items" → 附 CI 或用 approximate 表述（"approximately an order of magnitude"）

### Introduction
- 第 2 段与 Related Work 存在内容重叠（Bouthillier, IRT, Mesting 均两处详细讨论），建议简化 Intro 中文献讨论
- "Three gaps remain" 铺垫有效，但 gap (b) 的 operationalization（MC/FF 二分法）应在引入时承认 format taxonomy 粗糙性

### Method (Section 3)
- Section 3.1 需增加 "G-theory for ML practitioners" 桥接段落
- Section 3.2 应列出全部 8 模型名称/版本（Table 1 或新表）
- 应说明 200 items 的 10 个 subject 选择标准
- 6 个 prompt template 需在正文或附录公开
- Bootstrap resampling unit 需明确

### Experiments (Section 5)
- Section 5.1 小效应（<1%）分组概括，精确值放入表格
- Section 5.2 "item difficulty dominates" 对 ARC（33.7% vs 33.7%）不准确——改为 "item and model×item are comparable"
- Section 5.3 permutation test 应明确 p=0.10 = minimum achievable 并讨论含义
- Table 3 caption 应注明 HellaSwag completion-style MC 与 knowledge-style MC 的 item construction 差异
- Section 5.4 IRT 对比应标注为 illustrative comparison（不同优化目标）

### Conclusion
- "the central finding is that variance structure is format-conditional" → 降级措辞
- Precision interchangeability 应限定为 "under binary scoring on single-GPU for 7-9B open-weight models"

### Limitations
- 缺少对统计检验效力限制的讨论（permutation test, n=5）
- 建议增加 format taxonomy 粗糙性和更精细分类（knowledge-MC / completion-MC / FF）的需求

### Appendix
- 5 项 robustness 需大幅扩展：每项含方法描述、关键数值（含 CI）、结果表格
- 当前半页空白极不专业
- 补充 AAAI Reproducibility Checklist