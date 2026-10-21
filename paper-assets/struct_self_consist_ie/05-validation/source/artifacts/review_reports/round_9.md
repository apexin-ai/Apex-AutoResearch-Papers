---
round: 9
overall_score: borderline
timestamp: 2026-05-15T15:19:33.133813+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Round 8 Consolidated Review Report

**Paper**: "Strong Predictors, Weak Selectors: Confidence Signals Predict but Do Not Select in 8B-Scale Information Extraction"
**Venue**: EMNLP 2026 Findings (ARR May cycle, deadline 2026-05-25)
**Reviewers**: R1 (方法+实验), R2 (新颖性+写作+格式)
**Protocol**: 独立初审 → 交叉分享 → 收敛（1轮达成共识，无需第2轮）

---

## Summary

本文系统评估了五种置信度信号（VC、SJ、FK、EM、LP）在 LLM 结构化信息抽取中的质量估计、二元判别和样本选择三个维度上的表现。核心发现为"correlation-selection gap"——所有信号在质量估计上表现良好（ρ 最高 0.38，AUROC 最高 0.75），但在样本选择上均未能显著优于 greedy baseline，尽管存在 12-18pp 的 oracle headroom。论文提出两层解释：(1) 四个信号为 instance-level 聚合，定义上无法排序候选；(2) LP 分数严重压缩（60% 实例有效并列）。实验覆盖 2 个模型族（Qwen3-8B, LLaMA-3.1-8B）、3 个数据集（SciERC, CoNLL-2003, WNUT-17）、N=8/16 两个采样规模。

---

## Strengths

**S1. 系统性实验设计（两位 Reviewer 共识）**
5 信号 × 3 维度 × 3 数据集 × 2 模型的全因子设计，覆盖面在同类工作中罕见。bootstrapped CI、paired permutation test、3-seed 稳定性分析等统计方法规范。

**S2. 核心发现具有实用价值**
Correlation-selection gap 的发现对 self-consistency 方法的实际部署有直接指导意义——警示从业者不能仅凭 rank correlation 选择信号。

**S3. 多层次诊断分析**
从定义层（instance-level 信号无法排序候选）到机制层（LP 压缩、MBR 效用-质量错位）的分层解释，提供了比单纯报告现象更深的理解。

**S4. 透明的局限性讨论**
Limitations 部分涵盖 RE 单基准、模型规模限制、温度未测试、enable_thinking 不一致等，展现了诚实的自我评估。

**S5. Ablation 设计有价值**
Free-form ablation 排除了 constrained decoding 作为 LP 压缩的唯一来源，non-tied LP 子集的显著性分析（+2.9pp, p=0.01）为机制解释提供了关键证据。

---

## Weaknesses

### Critical（必须修复）

**C1. 页数严重超限 [R1+R2 共识]**
正文（Abstract 至 Conclusion）估计为 10-11 页，超出 ARR/EMNLP 8 页限制 2-3 页。这是格式硬性要求，desk reject 风险极高。
- R1: 需要大幅压缩 experiments 和 discussion
- R2: 必须砍到 8 页，建议将 free-form ablation 详情、N-scaling 细节、部分表格移入 appendix

**C2. ε=0.05 "effectively tied" 阈值循环论证 [R1 提出, R2 同意]**
LP 压缩的核心量化依赖 ε=0.05 阈值，但该阈值缺乏独立于数据的 justification。论文未提供 ε sensitivity analysis（不同 ε 下 tied fraction 如何变化），使"60% tied"这一关键数字的可信度受损。R1 建议补充 ε sweep 图表。

**C3. LP 温度 T=0.7 数据缺失 [R1 提出, R2 同意]**
温度比较实验（T=0.7 vs T=1.0）中 LP 被排除（因缺少 T=0.7 LP 数据）。这恰好是 LP 压缩与温度交互效应的关键缺失——practitioners 通常在 T<1.0 部署，LP 在低温下的表现直接影响论文结论的实用性。Limitations 已提及但仅作为"unknown"处理，不足以弥补。

**C4. RE 结论基于单基准+单 seed（部分场景）[R1+R2 共识]**
RE 仅在 SciERC 上评估（且 40% 实例 F1=0），free-form ablation RE 选择方向逆转基于单 seed。论文在多处声称 RE 为 "preliminary"，但标注不一致——abstract 和部分正文中未标注。所有 RE claim 必须统一标注 preliminary。

### Major（强烈建议修复）

**M1. 标题 "Do Not Select" 过度断言 [R2 提出, R1 部分同意]**
标题断言信号"不能选择"，但 non-tied LP 子集确实能选择（+2.9pp, p=0.01），且论文仅测试了 unsupervised 信号。R1 认为当前标题可接受但可改进为更精确的表述。R2 认为标题与论文自己的证据矛盾。建议修改为反映条件性失败的表述。

**M2. Abstract 信息过载 [R1+R2 共识]**
10 行 abstract 塞入 5 个信号名、3 个数据集、2 个模型、4 个指标的具体数值，first-pass 可读性差。建议精简到核心 narrative：gap 存在 → 诊断原因 → 实用影响。

**M3. Framing 问题：贡献 C1 的性质 [R1、R2 分歧，见下]**
R2 认为 C1（instance-level 信号无法排序候选）是定义推导而非实证贡献，将其列为"贡献"存在 framing 误导；R1 认为 definition-level 诊断本身有价值但同意措辞可改进。论文需要更清晰地区分 definitional vs empirical 贡献。

**M4. Eikema & Aziz (2022) MBR 讨论位置不当 [R1+R2 共识]**
MBR decoding 连接出现在 Discussion 而非 Related Work，使读者在 §5 才发现这一重要理论关联。建议在 Related Work 中增加 MBR/utility-based selection 子节。

**M5. 缺少代码/数据发布声明 [R2 提出, R1 同意]**
论文未包含代码或数据发布声明。ARR review form 明确询问 reproducibility resources。即使匿名期无法提供链接，也应声明提交时或录用后会发布。

### Minor

**W1. enable_thinking 对 LP 的潜在影响**
Qwen3-8B SciERC checkpoint 训练时有空 `<think></think>` 块，可能影响 first-token 概率分布。虽然 Limitations 中已讨论，但未定量评估影响大小。

**W2. Free-form ablation 范围窄**
仅在 SciERC + Qwen3-8B 上进行，泛化性未验证。

**W3. FK t-test 统计功效不足**
SciERC RE 的 FK t-test 可能样本量不足，p 值接近临界值时可信度受限。

**W4. TOST δ 锚定**
等价性检验的 δ 选择缺乏先验 justification。

**W5. SJ 的 Hungarian 算法匹配**
SJ 使用 Hungarian 算法做 token-level IoU 匹配，计算复杂度 O(n³)，论文未讨论 scalability。

---

## Reviewer Consensus（共识区）

以下问题两位 Reviewer 完全一致：
1. **页数超限是 desk reject 级问题**，必须在提交前解决
2. **ε=0.05 需要 sensitivity analysis** 或独立于数据的 justification
3. **LP T=0.7 缺失**是对实用性的重大限制
4. **RE preliminary 标注必须全文一致**
5. **Abstract 需精简**，减少具体数值堆砌
6. **Eikema MBR 讨论应前移到 Related Work**
7. **需要代码发布声明**
8. **核心实验设计和统计方法扎实**

---

## Reviewer Divergence（分歧区）

**D1. Framing 严重程度**
- R2 (2.5/5): 认为 framing 存在根本性问题——将定义推导包装为实证贡献，标题与证据矛盾，整体叙事需要重构
- R1 (3.5/5): 认为是表述改进问题而非根本缺陷，核心发现的价值不受 framing 影响

**D2. 贡献 C1 的性质**
- R2: 属于方法论层面的定义问题，不应列为论文贡献
- R1: Definitional 诊断本身具有实证价值（因为社区此前未明确意识到这一点）

**D3. SJ Hungarian matching 的新颖性**
- R2: 技术新颖性有限，且 scalability 未讨论
- R1: 论文未将其声称为贡献，不应作为弱点评判

---

## Questions for Authors

Q1. ε=0.05 的选择依据是什么？能否提供 ε ∈ {0.01, 0.02, 0.05, 0.10, 0.20} 下 tied fraction 和 LP selection Δ 的 sensitivity curve？

Q2. LP 在 T=0.7 下的压缩行为是否可从现有数据推断？是否有技术障碍阻止收集 T=0.7 LP 数据？

Q3. Non-tied LP 子集（40%, n=210）的 instance 特征是什么？它们是否对应特定难度区间或 schema 复杂度？

Q4. 如果 C1 是 definitional（如论文 Introduction L23 所述），为何将其列为论文的第一个 contribution 而非 background/preliminary？

Q5. Free-form ablation 中 RE LP selection 方向逆转（-0.68→+1.69pp）的机制解释是什么？这是否暗示 constrained decoding 而非 LP 本身是 RE selection 失败的原因？

Q6. 论文是否计划发布代码、模型 checkpoint 或实验数据？

---

## Missing References

两位 Reviewer 均未发现关键缺失引用。引用列表（62 条）经核查真实完整。

建议补充（非必须）：
- MBR decoding 在 NLP 中的更多近期工作（如 Bertsch et al. 2023 等）
- Conformal prediction for NLP（论文 Conclusion 中提到但未引用具体工作）

---

## External Review

本轮未获得外部审稿结果（用户跳过）。

---

## Overall Assessment

**综合评分: Borderline（边界线）**

**R1 评分: 3.5/5** — 方法扎实、发现有价值，但 ε 循环论证和 LP 温度缺失削弱了核心 claim 的可信度
**R2 评分: 2.5/5** — 实验设计严谨但页数超限+framing 问题构成提交障碍；R2 表示若页数+framing+标题修复可升至 3.0/5

**录用建议: Borderline Reject → Borderline Accept（取决于修改质量）**

论文的核心发现（correlation-selection gap）具有实际价值，实验设计系统严谨，统计方法规范。但当前版本存在以下提交障碍：

1. **Blocking**: 页数超限 2-3 页（desk reject 风险）
2. **Blocking**: ε=0.05 缺乏独立 justification（核心量化可信度）
3. **High priority**: 标题过度断言、RE preliminary 标注不一致、abstract 可读性

如果作者能在 deadline 前（2026-05-25）完成：压缩至 8 页、补充 ε sensitivity analysis、统一 RE preliminary 标注、修改标题、精简 abstract，论文有望达到 EMNLP Findings 的录用标准。否则建议推迟至下一 cycle。

---

## Detailed Comments

### 页数压缩建议（优先级排序）
1. Discussion §5 的 free-form ablation 详情（¶4）→ 移入 Appendix，正文仅保留一句结论
2. Table 2 的 N=16 行 → 移入 Appendix，正文讨论 N=8 为主
3. Experiments 中 WNUT-17 的详细讨论 → 压缩为 1 段，作为 capability boundary 验证
4. Figure 3 → 考虑是否可与 Figure 2 合并或移入 Appendix

### RE 处理建议
- 所有 RE 相关 claim 统一添加 "(preliminary; single benchmark)" 标注
- Abstract 中 RE 相关数值可删除或移入括号注释
- 考虑将 RE 定位为 "exploratory analysis" 而非与 NER 并列的主要结果

### Framing 调整建议
- C1 重新措辞：从 "contribution" 改为 "observation/finding"，或明确区分 "definitional analysis" 与 "empirical contribution"
- 标题选项："Confidence Signals Predict but Struggle to Select" 或 "The Correlation-Selection Gap in ..."