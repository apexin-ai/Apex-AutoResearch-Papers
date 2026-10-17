---
round: 7
review_mode: fresh
overall_score: 3.0 Findings
timestamp: 2026-05-22T04:44:12.686143+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Round 7 审稿报告：Per-Example Predictive Multiplicity in Hybrid Recurrent Architectures

**Target Venue**: EMNLP 2026 (ARR May 2026 cycle)
**Reviewers**: R1 (方法严谨性) + R2 (新颖性/完整性)
**交叉分享**: 完成，关键问题达成共识

---

## Summary

本文使用 Wang et al. (2025) 的 controlled model zoo（GatedDeltaNet / RetNet / HGRN2 × 5 attention ratios × 2 scales），系统分析了 hybrid recurrent 架构中 attention 对 per-example 行为的影响。三个核心发现：(1) per-example predictive multiplicity 呈 task-dependent variation（α = 0.14–0.30），跨架构 Jaccard 一致低（≤ 0.10）；(2) aggregate convergence 仅 LAMBADA 显著（ρ = −1.0, Bonferroni-adjusted p = .100）；(3) aggregate convergence 与 per-example divergence decoupled。

---

## Strengths

1. **受控实验设计**：利用同训练数据/tokenizer/超参数的 model zoo 隔离架构变量，在同类研究中少见。(R1-S, R2-S2)
2. **统计透明度高**：坦诚报告 Bonferroni p=.100 不达标、BCa 退化、GDN confound 等限制。(R1-S, R2-S3)
3. **充分的 robustness 分析**：GDN exclusion sensitivity、normalized Jaccard ES、subsample sensitivity、cross-scale validation、confirmatory/exploratory pre-specification。(R1-S, R2-S3)
4. **Decoupling 发现有信息量**：aggregate σ 持续下降而 Jaccard 在 4% attention 即饱和，对 practitioners 有实用参考价值。(R2-S4)
5. **Confidence margin 机制性 insight**：attention 系统性拯救 near-miss 错误、翻转弱正确答案，提供可解释的 per-example 预测信号。(R1-S)
6. **Reproducibility 好**：公开 model zoo + 标准 benchmark (lm-eval-harness) + 详尽统计流程。(R1, R2)

---

## Weaknesses

### Critical (Must-Fix，影响接收决定)

**C1. Convergence claim 统计 fragility 与措辞不匹配** [R1-N1 + R2-W4, 共识]
- LAMBADA convergence (ρ = −1.0) 经 Bonferroni 校正后 p = .100，未达 α = 0.05。n=5 检验效力上限使即使完美单调也只能达到 p = .0167。
- Abstract "monotonic variance reduction (79%)" 和 "BCa 95% CI excludes zero" 给读者过于确定的印象。
- GDN exclusion 后 ρ 降至 −0.7, p = .233（§4.4）。
- **共识要求**：Abstract/Introduction 中 convergence 需用 "suggestive" / "preliminary" 修饰，并注明 adjusted p 和 GDN dependency。

**C2. 无 seed baseline，架构效应 vs 初始化效应不可分离** [R1-N2 + R2-W5, 共识]
- 每个 (architecture, attention ratio, scale) 仅一个 training run。
- Within-arch Jaccard ~0.33 vs cross-arch ~0.10 的 3× gap 是间接证据，但 within-arch 比较混淆了 attention dose 变化与 seed 变化。
- McCoy (2020) / D'Amour (2022) 已展示同架构 seed variation 产生类似量级的 per-example divergence。
- **共识要求**：至少一个架构补 2-3 seed runs 以量化相对贡献；若不可行则系统性降级 claim 为 "associated with" 而非 "produces"。

**C3. "Decoupling" 缺乏形式化定义和统计检验** [R1-N3 + R2 AGREE, 共识]
- 仅有操作性描述（σ 下降 + Jaccard 饱和），无数学定义、null hypothesis 或 formal test。
- σ（百分比）与 Jaccard（集合相似度 [0,1]）scale 不同，直接比较 trajectory 需归一化。
- Jaccard floor effect：observed ~0.10 vs null ~0.05，range 极窄，微小趋同变化可能被掩盖。
- **共识要求**：(a) 形式化定义（如 ρ(σ, J) rank correlation 不显著为负）；(b) 讨论 Jaccard floor effect 和灵敏度限制。

**C4. 方法论新颖性不足** [R2-N1 + R1 AGREE, 共识]
- Section 3 全部分析工具（α, Jaccard, Spearman, confidence margin, BCa bootstrap）均为已有方法直接套用。
- "First systematic per-example analysis" 但 per-example decomposition (helped/hurt/unchanged + pairwise overlap) 是标准做法。
- 不同架构产生比同架构更大的 divergence 是合理预期而非反直觉发现，surprise factor 有限。
- **共识结论**：empirical contribution 路线在 NLP 中可接受，但 excitement 上限受限于无方法论创新。适合 Findings 但不足 main conference。

**C5. 缺乏 actionable insights** [R2-N3 + R1 AGREE, 共识]
- 全部贡献停在诊断层面——multiplicity 存在、task-dependent、与 convergence decoupled。
- Conclusion 推迟 ensemble 验证（"requires empirical validation beyond this observational study"）。
- 论文已有 30 配置 × 5153 LAMBADA 样本的完整预测数据，majority vote ensemble POC 计算成本极低，不做为显著的完整性缺陷。
- **共识要求**：至少一个 proof-of-concept（跨架构 majority vote / fairness 影响量化 / practitioner decision framework）。

### Should-Fix (影响评分但不一票否决)

**W1. BCa bootstrap CI (n=3) 覆盖率不可靠** [R1-W1 + R2 AGREE]
- 仅 27 unique resamples, 11.25% degenerate. §3.5 标注 "heuristic" 但 Abstract/Intro 引用 CI 时无 caveat。
- 建议：所有引用 CI 处附加 "(with limited coverage guarantees; §3.5)"。

**W2. "Task-dependent spectrum" 基于有限数据点** [R1-W2, R2 部分 REBUT]
- 4 main benchmarks 中 PIQA/HellaSwag CI 重叠。R2 指出加上 appendix BoolQ/WinoGrande 覆盖 0.14-0.45 范围。
- 折中：改称 "task-dependent variation" 而非 "spectrum"；正文引用 supplementary benchmarks 拓宽 evidence base。

**W3. GDN head confound 在正文中不够显著** [R1-W3 + R2 AGREE]
- GDN h3-1 用 16 heads（其他 32），Table 1 无脚注，§4.1 无提及。
- 建议：Table 1 加脚注 + §4.1 正文一句话提及 confound 及 robustness 影响。

**W4. 架构覆盖面窄，claim generality 不匹配** [R1-W5 + R2-W3, 共识]
- 仅 3 种 gated linear recurrence 架构，未含 Mamba/Griffin/SSM-MoE。
- Title "Hybrid Recurrent Architectures" 暗示更广范围。
- 建议：Title/Abstract 限定为 "linear recurrent architectures"；Limitations 讨论其他 hybrid family 泛化。

**W5. 遗漏重要相关工作** [R2-N2 + R2-W1 + R2-W2, R1 部分 AGREE]
- Swayamdipta et al. (2020) Dataset Cartography：per-example 分析先驱，必须补引并 differentiate。
- Fu et al. (2023) H3：首个系统性 SSM-attention hybrid，应补引。
- Cooper et al. (2024)：multiplicity 的 fairness 影响，建议补引。
- R1 对 Cartography 严重性有分歧（认为操作定义不同，应补引但非 "critical missing"），折中为 should-fix。

**W6. Contributions 列表仅 2 项偏少** [R2-W6 + R1 AGREE]
- 8 页 paper 仅 2 个 empirical contributions。Decoupling（§4.3 完整小节）未列为独立 contribution。
- 建议：提升 decoupling 为第 3 个 contribution。

**W7. Binary decomposition 信息损失** [R1-W4, R2 部分 REBUT]
- Jaccard 完全基于 binary 分类，confidence 0.51→0.49 与 0.99→0.01 的 hurt 不可区分。
- 论文在 Appendix N 有 continuous confidence margin 分析（d = 0.73-0.92），但直接 log-probability shift 的连续版本分析更优。
- 折中：现有分析 reasonable，直接 continuous 分析为 enhancement。

---

## Reviewer Consensus

以下问题两位 Reviewer 明确达成 [AGREE] 共识：
1. Convergence claim 措辞需系统性弱化（Abstract/Intro）
2. 无 seed baseline 是根本性实验盲点
3. Decoupling 需形式化定义 + Jaccard floor effect 讨论
4. 方法论新颖性有限，适合 Findings 不足 main conference
5. 缺少 actionable proof-of-concept
6. 架构覆盖面窄，claim generality 应降级
7. GDN confound 需在正文更显著讨论
8. BCa CI caveat 需在正文引用处标注

## Reviewer Divergence

| 问题 | R1 | R2 | 解决 |
|------|----|----|------|
| Dataset Cartography 遗漏严重性 | should-cite，操作定义不同 | critical missing，概念直接对应 | 折中：must-cite 但非 critical gap |
| "Spectrum" vs 二元观察 | 4 点中 2 点 CI 重叠→二元 | 6 benchmarks 覆盖 0.14-0.45→非二元 | 折中：改称 "variation" |
| Binary decomposition 严重性 | should-fix | nice-to-have（appendix 已有 continuous） | 折中：enhancement |

---

## Questions for Authors

1. 如果有每个配置 2-3 个 seed 的模型，你们预期 seed-driven Jaccard 与 architecture-driven Jaccard 的差距有多大？
2. Attention weights 在 GDN/RetNet 间几乎相同 (cos 0.995) 但 per-example effects 不同——是否意味着 multiplicity 根源完全在 recurrent layers？"attention effects" 的 framing 是否需调整？
3. 简单 majority vote across 3 architectures 在 LAMBADA 上能带来多大 accuracy gain？
4. 为何未包含 Mamba-based hybrid？是 model zoo 限制还是其他原因？
5. ρ(σ, Jaccard) 的 rank correlation 是否显著为负？如果不显著，decoupling claim 如何成立？

---

## Missing References

| 引用 | 优先级 | 理由 |
|------|--------|------|
| Swayamdipta et al. (2020) Dataset Cartography, EMNLP | Must-cite | Per-example 分析先驱，需 differentiate |
| Fu et al. (2023) H3, ICLR | Should-cite | 首个系统性 SSM-attention hybrid |
| Cooper et al. (2024) Arbitrariness, AAAI | Should-cite | Multiplicity → fairness 影响 |
| Fisher et al. (2019) Rashomon set, JMLR | Nice-to-have | Rashomon set 理论基础 |

---

## External Review

**状态**：未请求（项目未配置外部审稿）

---

## Visual Layout Check（非评分项）

视觉审查已完成（4 warning, 6 info, 0 critical）。主要发现：

1. **[warning] Pages 3-4 视觉单调**：连续 2 页纯文本（Related Work 尾部 + Method 全部），无 display item 穿插。建议在 Method 中加实验设计概览图或 display math。
2. **[warning] Display items 偏少**：主正文 8 页仅 4 个 display items（2 figures + 2 tables），对实证为主的论文偏少（典型 5-8 个）。大量结果在 appendix，审稿人需频繁翻页。建议提升 1-2 个关键 appendix 表格到主正文。
3. **[warning] Figure 1 标签字号偏小**：axis labels/tick labels ~6-7pt，打印时可读性受限。建议 ≥8pt。
4. **[warning] Figure 2 尺寸偏小**：scatter points 密集重叠，部分 benchmark 标签难辨。建议增大图幅或 faceted layout。
5. **[info]** Table 1/2 布局规范（booktabs + bold），Limitations 篇幅适当，References 格式一致，Appendix 组织清晰。

---

## Overall Assessment

**评分：3.0 — Findings**

**置信度：4/5**（两位 Reviewer 独立给出相同评分，交叉分享后共识强化）

**理由**：
- 研究问题有实际意义（hybrid 架构选型中 per-example 行为的盲点），实验设计受控严谨，统计局限性报告透明
- 但存在 5 个 critical 问题的组合限制：(1) convergence claim 统计 fragile + 措辞过强，(2) 无 seed baseline 为根本性实验盲点，(3) decoupling 核心概念缺乏形式化，(4) 方法论无创新（已有指标直接套用），(5) 缺乏 actionable insights（连 trivial POC 都未做）
- 优势（受控设计、统计透明、robustness checks）使其达到 Findings 门槛
- 不足 main conference 标准：novelty limited + key claims statistically fragile + no actionable contribution

**如果修改到位（C1-C5 全部 addressed），可提升至 3.5 (Borderline Conference)**。关键升级路径：(a) 补 seed baseline 或彻底降级 claim；(b) decoupling 形式化；(c) majority vote ensemble POC；(d) 补 Dataset Cartography/H3 引用并 differentiate。

---

## Detailed Comments

### Abstract
- "monotonic variance reduction (79%)" → 加 "suggestive" 或注明 "Bonferroni-adjusted p = .100"
- "BCa 95% CI excludes zero" → 加 "(heuristic; n = 3 architectures)"
- 考虑将 "hybrid recurrent architectures" 限定为 "linear recurrent architectures"

### Introduction
- Paragraph 4 "only LAMBADA exhibits monotonic convergence" → 加 "though this does not survive strict Bonferroni correction"
- "the first systematic per-example analysis" → "the first systematic per-example analysis of architectural multiplicity in hybrid linear recurrent models"

### Section 3 (Method)
- §3.5 BCa "heuristic indicators" 的 caveat 需在正文每次引用 CI 时传递

### Section 4.1 (Task-Specific Convergence)
- 正文需提及 GDN head confound 及其对 convergence 结论的影响
- Table 1 加脚注标注 GDN h3-1 使用 16 heads

### Section 4.2 (Per-Example Divergence)
- "task-dependent spectrum" → "task-dependent variation"
- "all p < .01" 需指明检验类型

### Section 4.3 (Decoupling)
- 需要形式化数学定义
- 需讨论 Jaccard floor effect 作为 alternative explanation
- 需补充 ρ(σ, J) 或类似 formal test

### Section 5 (Conclusion)
- Ensemble 推测标注 "speculative"
- 补充 practitioner-facing protocol 或 at least majority vote POC 结果

### Related Work
- 补 Swayamdipta et al. (2020), Fu et al. (2023), Cooper et al. (2024)

### Figures
- Figure 1: 字号 ≥8pt
- Figure 2: 增大或 faceted layout
- 考虑在 Method section 增加实验设计概览图