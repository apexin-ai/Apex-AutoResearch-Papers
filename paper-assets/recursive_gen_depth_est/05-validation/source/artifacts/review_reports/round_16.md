---
round: 16
review_mode: fresh
overall_score: 3.0 (Findings)
timestamp: 2026-05-22T23:20:33.759888+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 19

**论文**: "How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints"
**Venue**: EMNLP 2026 (ARR May cycle, deadline 2026-05-25)
**Reviewer 编排**: 2 人（R1: 方法严谨性+实验设计, R2: 新颖性+完整性+写作）
**流程**: Round 1 独立审稿 → 交叉分享 → 收敛（1 轮完成）

---

## Summary

本文定义了"递归生成深度估计"任务，将其形式化为序数分类。构建了 180K 实例的基准数据集（3 模型族 × 3 解码策略 × 4 深度），提出 19 个统计特征 + Random Forest 的轻量管线，引入 Effective Discriminable Depth (EDD) 指标。主要发现：深度信号集中在困惑度分布尾部，解码策略比模型架构更影响迁移，信号随规模衰减（14B EDD₇₀=0）。论文实证工作系统全面，但方法论创新有限、泛化能力不足、且部分关键声明与证据不匹配。

---

## Strengths

1. **任务形式化具有真正的新颖性** [R1 AGREE, R2 AGREE]：将递归生成深度从二分类推广到序数估计是自然且有价值的形式化。与 model collapse 和 AI text detection 文献的区分在 Section 2 清晰。EDD 指标提供了有操作价值的可区分深度摘要。

2. **系统性实证分析深度出色** [R1 AGREE, R2 AGREE]：180K 实例、3×3 网格、30+ 消融实验（Appendix B.1–B.34）的密度在 EMNLP 投稿中少见。Depth Degradation Atlas 提供了直观的退化全景图。

3. **特征一致性发现有理论价值** [R1 AGREE, R2 AGREE]：p90_ppl 和 var_surprisal 在 9/9 cells 稳居 top-2（Table 3），跨模型特征排名 Spearman ρ=0.868。Gini/SHAP/CPI 三种方法交叉验证特征排名（Kendall's W=0.90）。

4. **诚实报告负面结果** [R1 AGREE, R2 AGREE]：跨策略迁移失败（45.9%）、14B 衰减（EDD=0）、curation PoC 不显著（p>0.4）均有透明报告。

5. **可复现性良好** [R1: 4/5, R2: 4/5]：超参数、数据规模、训练细节在正文和附录中详细记录。

---

## Weaknesses

### Must-Fix (Critical)

**C1. 泛化性 claim 与证据系统性失配** [R1 AGREE, R2 N2 Critical]
- 跨策略迁移：d1–d3 仅 45.9%（Section 5.3），接近随机
- 14B self-reference：EDD₇₀=0，4-class 仅 50.8%（Section 5.4）
- 标题 "Statistical Fingerprints" 暗示可迁移信号，但实证表明信号高度依赖已知模型族和解码策略
- Abstract "consistent in direction but scale-dependent in magnitude" 将方向一致性包装为正面结论，但 45.9% 的分类器在部署场景中几乎不可用
- Two-stage pipeline 恢复到 70.5%（Section 5.3）是重要发现但仍远低于 within-cell 水平
- **共识**：需在 Abstract 和 Introduction 明确限定 claim scope 为 "within known model-strategy configurations"

**C2. 14B 规模衰减是根本性瓶颈** [R1 AGREE, R2 N3 Critical]
- Self-reference 50.8%（2× chance）但 EDD₇₀=0 意味着序数结构已坍塌
- 当前主流 LLM 70B–405B，1.4B 成功更多是 proof-of-concept
- Introduction/Discussion 叙事以积极语气讨论前景，未充分传达这是当前方法的根本瓶颈
- R2 REBUT R1-W4（14B confound）：self-ref 数据已足够分离 scale vs ref-model（50.8% vs 44.1% = ~7pp gap 远小于 30+pp 与 1.4B 的差距）——scale 是主要驱动因素
- **共识**：Contribution list 需显式声明规模限制

**C3. 参考模型依赖限制部署可行性** [R1 N1 Critical, R2 W3 Warning → AGREE]
- 19 特征中 12 个依赖 Pythia-1.4B log-probabilities
- Cross-architecture 下降 4–11pp（Appendix B.17 Table 18）
- Generator-unknown 场景下无参考模型选择策略
- 正文仅笼统提及，未系统讨论部署含义
- **分歧**：R1 列为 Critical（pipeline 根本瓶颈），R2 认为 proof-of-concept 阶段可接受 Should-Fix。Director 判定：由于 12/19 特征绑定且缺乏选择策略讨论，维持 Critical。

---

### Should-Fix (Warning)

**W1. 方法论创新不足** [R1 部分 REBUT, R2 W1 Warning]
- 19 特征均为标准 NLP 特征（GLTR/DetectGPT/Ghostbuster 均有先例），RF 为 off-the-shelf
- 本质是"已有特征应用于新任务"
- R1 认为 EMNLP 接收系统性实证研究；R2 认为这限制了 Conference excitement
- **未深入分析统计特征优于 PLM 表征 20pp 的根本原因**——这个 "why" 本身有价值

**W2. Full-replacement benchmark 与真实 accumulation 场景 gap** [R1 N3 Critical → R2 认为 Should-Fix]
- 真实场景涉及 accumulation + unknown mixing ratios + 异构模型
- Appendix B.8 仅覆盖 6 组合，GPT-2 XL 50% mixing 出现 boundary failure（AUC=0.695）
- **共识**：证据不足，但首篇论文从受控设定起步合理

**W3. Neural baseline 比较信息不对等** [R1 W1 Warning, R2 AGREE]
- RF 使用参考模型 oracle（token-level perplexity），DeBERTa/RoBERTa 仅获得原文
- 当前对比更像 "PLM 不能从原文推断困惑度分布"（不意外）

**W4. 多重比较未统一校正** [R1 N2 Critical → R2 认为非 Critical]
- Section 5.1 将 Binoculars p>0.05 解读为 "statistical equivalence"，但非显著性 ≠ 等价性（需 TOST）
- Section 4.3 已做部分 Bonferroni 但未统一应用
- Director 判定：核心结论不依赖这些 p 值，降为 Warning，但 Binoculars 等价性声明必须修正

**W5. BOS seeding artifact** [R1 W5, R2 AGREE]
- BOS seeding vs prompted generation 差 13.8pp（Appendix B.16）
- 深度信号可能部分来自无条件生成的特异性 artifact
- 正文应更显著地讨论此差距的含义

**W6. 序数分类框架与实际方法脱节** [R1 AGREE, R2 W2]
- 强调 ordinal classification 但主管线用标准 RF 不利用序数结构
- CORAL 仅有边际改善（Appendix B.25）但未在正文讨论原因

**W7. 单 LoRA seed 统计功效** [R1 W6, R2 AGREE 程度较轻]
- 主实验单 seed，2-seed replication 方向一致但不足以估计方差分布

---

## Reviewer Consensus [AGREE]

1. 任务定义的新颖性和价值 ✓
2. 实证分析的系统性和深度 ✓
3. 泛化 claim 超出证据支撑范围 ✓
4. 14B 规模衰减是根本性挑战 ✓
5. 参考模型依赖需更充分讨论 ✓
6. Neural baseline 比较信息不对等 ✓
7. BOS seeding artifact 值得讨论 ✓
8. 序数框架与方法脱节 ✓

## Reviewer Divergence

| 问题 | R1 | R2 | 分歧实质 |
|------|-----|-----|---------|
| Excitement | 3.5/5 | 2.5/5 | R1 更重任务新颖性；R2 更重方法创新和部署前景 |
| 参考模型依赖严重程度 | Critical | Warning | R1: pipeline 根本瓶颈；R2: proof-of-concept 可接受 |
| 多重比较严重程度 | Critical | Minor→Warning | R1: 统计论文需统计严谨；R2: 核心结论不依赖 p 值 |
| Full-replacement gap 严重程度 | Critical | Warning | R1: 生态效度不足；R2: 首篇论文合理起步 |
| 方法论创新 | 不阻拦 | 限制 Conference | R1: EMNLP 接收实证研究；R2: 零创新限制 excitement |
| 14B confound 分离 | W4 Warning | REBUT | R2: self-ref 50.8% 已足够分离 scale vs ref-model |

---

## Questions（需作者回答）

1. Generator-unknown 部署场景下的参考模型选择策略？是否考虑 multi-reference ensemble？
2. 为什么主管线不使用序数分类器？CORAL 在此任务中边际改善的原因分析？
3. BOS seeding vs prompted generation 的 13.8pp gap——深度信号中有多大比例来自 BOS seeding artifact？
4. 14B 以上规模的理论预期？是否存在 U 型曲线？
5. 统计特征优于 PLM 表征 20pp 的根本原因？这对 NLP 表征学习有何启示？
6. 10% mixing ratio 下 pipeline 是否仍能工作？
7. QWK=0.89 对应的具体 ordinal misclassification pattern？

---

## Missing References

**两位 Reviewer 共同推荐**：
- Lakens (2017) equivalence testing 方法论（TOST）
- Gutiérrez et al. (2016) ordinal regression 综述

**R2 推荐**（R1 认为间接关联，nice-to-have）：
- FineWeb (Penedo et al., 2024) — 数据策展管线
- DCLM (Li et al., 2024) — 大规模数据策展
- Sachdeva et al. (2024) Training on the Test Task

**交叉纠正**：R1 推荐的 Alemohammad et al. (2024) 已在 Section 2 第1段引用（R2 确认）。

---

## External Review (Stanford Agentic Reviewer)

未请求（项目配置未启用）。

---

## Visual Layout Check（非评分项）

视觉审查已完成（0 critical, 3 warnings, 15 info）：

**Warnings**:
1. **pp.1-2 无 display item**：连续 2 页纯文本（Abstract + Introduction + Related Work），审稿人前 2 页无视觉锚点。建议将 Figure 1 提升到 page 2。
2. **p.7 Figure 2/3 字号偏小**：heatmap cell 内数值约 6pt，Figure 3 三面板 axis labels 约正文 60%。建议 Figure 2 改为 figure*（全宽）。
3. **p.8 极度拥挤**：Table 4 + Table 5 + Section 5（4 子节）+ Section 6 全压缩在一页，审稿人可能认为 Generalization 和 Discussion 匆忙收尾。

**正面确认**：主文 8 页 ✓；所有表格 booktabs 统一、最优结果加粗一致；无 margin overflow、无 LaTeX 渲染错误、无 [?] 未解析引用；Limitations 覆盖 3 点 ✓；Ethics Statement 存在 ✓；Appendix 15 页详尽。

---

## Overall Assessment

**评分：3.0 (Findings)**
**置信度：4/5**

**R1: 3.5 (Borderline Conference) | R2: 3.0 (Findings)**

本文的核心价值在于任务形式化——将递归生成深度估计定义为序数分类，引入 EDD 指标，构建系统性 180K 基准。这是 genuinely novel 的问题定义，且实证工作的深度和诚实度达到顶会水准。

但以下因素将评分限制在 Findings：

1. **方法论贡献有限**：管线完全由已有组件组成（标准统计特征 + 标准 RF），无方法创新。四种分类器在 0.8pp 内收敛（Appendix B.25）表明准确率上限由特征决定，但特征本身也非本文提出。

2. **泛化性是结构性瓶颈**：跨策略 45.9%、14B EDD₇₀=0 表明方法仅在已知模型-策略配置下有效。标题 "Statistical Fingerprints" 暗示的可迁移性与实证结果存在系统性张力。

3. **规模衰减是根本性的**：当前主流 LLM 70B–405B，1.4B 规模的成功定位为 proof-of-concept 更合适。

4. **参考模型硬依赖**：12/19 特征绑定单一参考模型，跨架构下降 4–11pp，无选择策略讨论。

**升分路径**：如果 rebuttal 能 (a) 明确限定 claim scope 到 within-configuration 并调整标题/Abstract 措辞, (b) 补充 TOST/Bonferroni 校正关键统计声明, (c) 在 Discussion 中深入分析统计特征优于 PLM 的原因, 则可重新评估至 3.5 (Borderline Conference)。

---

## Detailed Comments

**Abstract**: 信息密度过高。最后长括号内混合了准确率、EDD、因素分解三个维度的数字，建议拆分。Director 核查：R2 报告的 "≈19%" 不一致问题为误读——当前 abstract.tex 实际写 "~44%"，与 Section 5.4 一致。但 cross-reference EDD₇₀=2 与 self-reference EDD₇₀=0 的混用仍需明确标注条件。

**Introduction (Section 1)**: 动机合理，贡献列表结构清晰。但 "consistent in direction" 需弱化——方向一致性不等于跨条件可用性。建议在贡献列表增加显式规模限制声明。

**Related Work (Section 2)**: 覆盖全面（model collapse、AI detection、membership inference、ordinal classification、decoding effects），定位清晰。建议补充 Lakens (2017) equivalence testing 方法论。

**Method (Section 3)**: Benchmark 构建设计合理。EDD 定义形式化清晰。建议更早提及 VIF>10 共线性（当前 Section 4.2 才出现）。"depth estimation" vs "ordinal classification" 术语声明已存在（Section 3.1），但后续使用仍偶有混用。

**Atlas (Section 4)**: 最强章节。特征重要性分析透彻，策略依赖轨迹发现有理论意义。Figure 2/3 字号需增大。

**Generalization (Section 5)**: 内容密度过高，5 子节不到 2 页。Two-stage pipeline 恢复到 70.5% 是重要发现但仅一句话带过。Table 4/5 的 cross-model/cross-strategy 结果应给更多讨论空间。

**Discussion (Section 6)**: 过于压缩。5 个加粗主题每个仅 2-3 句。"Why neural methods underperform" 是核心洞察值得展开——统计特征优于 PLM 表征 20pp 的原因分析有独立的学术价值。建议考虑将 Conclusion 独立成节。

**Limitations**: 覆盖关键局限，但 BOS seeding artifact（-13.8pp）的讨论应更显著。

**Appendix**: 内容极为详尽（15 页，B.1–B.34），远超同类投稿。**注意：Section B.20 (Qwen2.5-7B Self-Reference) 有 PLACEHOLDER 注释未填充——提交前必须补全或删除。**

**格式合规**: 主文 8 页 ✓；double-blind 匿名 ✓（作者标注 "Anonymous"）；Limitations ✓；Ethics Statement ✓；ACL 模板 ✓；引用格式统一 ✓。