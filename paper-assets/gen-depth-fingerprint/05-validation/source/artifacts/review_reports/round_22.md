---
round: 22
review_mode: fresh
overall_score: 3.0 (Findings)
timestamp: 2026-05-19T03:00:51.281885+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Round 22 审稿报告 — Depth Profiling: Classifying Recursive Generation Depth in Base LLM Text Chains

**Target Venue**: EMNLP 2026 (ARR Long Paper)
**Reviewers**: R1 (方法严谨性/实验/统计) + R2 (新颖性/framing/写作/格式)
**Review Mode**: Fresh (初审)
**Date**: 2026-05-19

---

## Summary

论文提出 generation depth classification 任务（gen-0/gen-1/gen-2+），使用 8 个 base model generator（5 families, 0.6B-8B）构建递归生成链，提取 7 个 handcrafted 特征，通过 XGBoost 分类器实现 LOGO binary F1=0.694。核心发现是 Differential Depth Response (DDR)：特征在递归生成下呈现三分结构（3 drifting / 1 intermediate / 3 near-stationary）。实验覆盖面广，包含 20+ 附录分析，诚实报告了 instruct 退化、温度敏感性、下游负面结果等局限。

---

## Strengths

**S1. 研究问题新颖**：递归生成深度分类（beyond binary real-vs-synthetic）是一个未被充分探索的方向，DDR 的 location/shape 分解提供了理解递归生成分布变化的有用 lens。

**S2. 实验体系极为全面**：8 generators × 5 families，LOGO + LOFO 评估，加上 20+ 附录涵盖长度控制、prompt type、温度敏感性、cross-domain、instruction tuning、error analysis、downstream utility、seed control、TOST equivalence 等。这种 thoroughness 在提交论文中不常见。

**S3. 统计方法严谨**：Bootstrap CI、McNemar tests、TOST equivalence testing、Bonferroni correction、Cohen's d + Spearman ρ + KS tests 的 multi-metric convergence——统计分析深度远超同类论文。

**S4. 负面结果的诚实报告**：downstream utility null result、instruction-tuning 灾难性退化、温度敏感性、DDR 是 "parameter-dependent phenomenon not intrinsic property"——这种透明度是该论文的重要优势。

**S5. 写作质量良好**：无明显 AI 写作痕迹（无 em-dash/en-dash 滥用、无 -ing 结尾堆积、无过度分段），术语定义基本完整，格式完全合规（≤8 页正文、行号开启、匿名化完整）。

**S6. 可复现性高**：详细的超参数、软件版本、GPU 配置（62 GPU-hours, 4×RTX 5090）、承诺发布代码和数据。

---

## Weaknesses

### Must-Fix（影响接收决定）

**C1. [Critical, R1+R2 共识] DDR 3/1/3 partition 的统计基础不足**

DDR 三分结构是论文的核心框架性贡献（Contribution 2），但多重证据表明其统计支撑弱于声称：

(a) **异方差下的 Cohen's d**：§4.2 承认 Levene tests reject equal-variance (p < 10^{-10})，但 DDR 阈值（d > 0.75 / d < 0.10）依赖 pooled Cohen's d。在方差显著不等时，Cohen's d 是有偏估计量。需补充 Glass's Δ 或 Cliff's delta 作为 sensitivity check。[R1 critical, R2 agree 但认为 multi-metric convergence 部分缓解]

(b) **数据驱动验证不支持 3-group**：k-means 最优 k=2 (silhouette=0.632)，k=3 仅 0.499（Appendix S）；holdout 4/4 split 产出 3/2/2 而非 3/1/3；tail decay 仅 4/8 generators 通过 TOST ε=0.20；entropy min 需要 domain-informed binary-task d 才能从 intermediate 归入 near-stationary。[R1+R2 strongest consensus]

(c) **建议**：将分区描述为 "primarily a 2-group structure (drifting vs non-drifting) with domain-informed refinement to 3/1/3" 而非数据驱动的三分发现。或在 held-out generator subset 上选阈值、另一 subset 上验证。

**C2. [Critical, R2 提出 + R1 完全同意] Framing 断裂：Introduction 实用动机 vs 实际发现**

Introduction §1 L5 声称 "downstream implications for model collapse theory and data provenance"，但论文实际发现与此不符：

- Discussion §5 L16 承认 "diagnostic rather than prescriptive role"
- §5 L7 明确 DDR 是 "parameter-dependent phenomenon, not an intrinsic property of recursive generation"
- 下游 TOST（Appendix M）证明 depth-aware curation 与 random subsampling 等价（虽然 n=3 效力不足，见 C4）
- Instruction-tuned 模型信号灾难性退化（OLMo LOGO F1: 0.763→0.338，Appendix K）

论文的 Abstract 和 Introduction 仍保留了实用性暗示，但 Discussion 和实验结论指向纯科学发现的定位。建议重写 Introduction 动机，将论文定位为 "理解 base-model 递归生成的分布结构" 的科学发现，将 data provenance/model collapse 从核心动机降级为远期联系。

**C3. [Critical, R2 提出 + R1 部分同意] 新颖性受并行工作和增量性质削弱**

三篇独立工作（Broken Telephone, Markovian Chains, 本文）收敛于 ~3 个可区分深度类别（论文自己在 §2.2 L31 承认）。DDR 被自认为 "empirical descriptive framework, not a claimed universal law"（§5 L6）。Binary → 3-class 是自然演进。

R1 认为 DDR 分解本身（what converges vs what stays stable）有独立增量价值，但前提是 DDR 的统计基础可靠（回到 C1）。共识：novelty 声称应从 "No existing method addresses this task"（§1 L9）调整为聚焦 DDR 分解的独特角度。

**C4. [Critical, R1+R2 共识] 下游 TOST n=3 统计效力严重不足**

下游实验（Appendix M）仅用 3 random seeds，df=4。Cohen's d=86.0/119.7 由 cross-seed std < 0.001 造成 artifact。Margin sensitivity analysis 显示 ±1% margin 全部 fail。论文自认 "preliminary observation rather than definitive null result"（Appendix M L73），但 Discussion §5 L16 将此结果用于支撑 "diagnostic rather than prescriptive role" 的核心定位——推广超出 n=3 的支撑范围。

建议：增加 seeds 至 10-20 个；或在 Discussion 中明确限定此结论的初步性质，不作为核心论点的支撑。

**C5. [Critical, R2 提出 + R1 部分同意] Base-model-only scope 限制影响力**

OLMo-Instruct LOGO F1 从 0.763 降至 0.338，entropy-mean ρ 符号反转（base: -0.60 → instruct: +0.48）。Qwen length-matched 后 binary F1≈0.5（Limitations §7）。实际 web 文本几乎全由 instruct/RLHF 模型生成。

R1 认为严重性取决于 framing：如果按 C2 建议调整为科学发现论文，base-model-only 是合理研究边界而非致命缺陷；如果坚持实用 framing，则确实致命。论文标题已含 "Base" 限定，Abstract 也有声明——但 Introduction 的实用动机暗示与此不匹配。

---

### Should-Fix（影响评分但不一票否决）

**W1. 温度敏感性限制实用范围**：t=0.9 时所有 4 个测试 generators 退化 9.3-26.0pp（Appendix H, Table 10），Pythia-2.8B 降至 0.480 接近随机。可靠工作范围仅 t∈[0.5, 0.7]。Cross-temperature transfer（Appendix O）显示 train@0.7/test@1.0 对 Pythia F1 从 0.848 降至 0.713。建议将温度限制提升为 Limitations 首要条目。[R1+R2 共识]

**W2. Generator 规模局限（≤8B）**：Table 1 显示明确 scale effect（Mistral-7B binary F1=0.633 最低，Qwen3-8B 0.692 也低于小模型），暗示 DDR 在 frontier models 上可能消失。Limitations 应更明确讨论规模外推风险。[R1+R2 共识]

**W3. Binary F1=0.694 性能上限偏低**：4-detector+surface ensemble (0.708) 与 7-feature set (0.705) 接近（Table 2），QLoRA 远超（0.905）。7-feature DDR 的独特价值区间窄——向上 QLoRA 远超，向下 detection baselines 接近。[R1+R2 共识]

**W4. Table 1 呈现可能误导**：3-class F1 (0.762) 作为首列但含 gen-0 seed sharing inflation，binary F1 (0.694) 才是 leak-free 指标。建议交换列顺序或加更醒目 footnote。[R1+R2 共识]

**W5. 多个 generator subsets 使结果难以交叉对比**：QLoRA 用 6-gen，baselines Table 2 用 6-gen，main Table 1 用 8-gen，cross-model 用 5-gen。Appendix U 已有 subset summary 但信息密度可更高。[R2 提出, R1 同意]

**W6. Contribution 3 叙事过于笼统**：覆盖 ~15 个 appendix 的 catch-all。建议拆分为具体发现（如 instruct degradation sign reversal、temperature sensitivity threshold、downstream null result）。[R2 提出, R1 同意]

**W7. TTR-hapax r=0.97 与 "effective dimensionality ~5" 论述不充分**：LOFO 显示 hapax Δ=-1.5pp 但 TTR Δ=-0.65pp，若 r=0.97 为何影响差异大？需 per-depth 相关性分析或 PCA 支持。[R1 提出, R2 agree with nuance]

**W8. 特征选择缺乏系统性**：7 特征来自先验知识（two perspectives），未探索句法复杂度、语义连贯性等替代特征。§3.3 L61 坦诚 "no larger candidate set was explored"，但应至少讨论排除理由。[R1 提出, R2 partial rebut: DDR 价值在于 interpretable features]

**W9. Cross-domain 实验存在温度混淆**：Academic domain t=0.7 binary F1 仅 0.628。论文自标注 cross-domain 原始数据用 t=1.0（在可靠范围外），虽补充了 t=0.7 数据但 domain effect 与 temperature effect 仍被混淆。[R1+R2 共识]

---

### Minor Issues

1. Abstract 中 "LLM" 未展开（ARR 要求 Abstract 内定义缩写）
2. Orphan bib entry: `self_refine` (Madaan et al., 2023) 未被引用
3. Table 2 baseline 的 ms/text 列标 N/A 未解释原因
4. Figure 1 axis labels 约 6-7pt，接近 ACL 可读性下限
5. "Effective dimensionality ~5" 需更正式支持（如 PCA explained variance）
6. Cross-model chains (§4.1) 使用 5-fold CV 而非 LOGO，评估协议不统一

---

## Reviewer Consensus

两位 Reviewer 在以下关键问题上达成共识 [AGREE]：

1. **DDR 3/1/3 分区统计支撑不足**（C1）：k-means 最优 k=2，holdout 产出 3/2/2，multiple boundary cases 需 post-hoc adjustment——两位 Reviewer 独立得出相同结论，是本轮最强共识
2. **Framing 断裂**（C2）：Introduction 实用动机与 Discussion 诊断定位不匹配
3. **TOST n=3 效力不足**（C4）：下游等价性结论被推广到 Discussion 核心论点，超出实验支撑
4. **Binary F1 应为 primary metric**（W4）：3-class F1 含 gen-0 inflation
5. **温度敏感性和规模局限**（W1, W2）：限制实用范围和泛化能力

## Reviewer Divergence

**QLoRA 是否削弱 DDR 框架贡献**：

- **R1 (Critical)**：QLoRA F1=0.905 vs XGBoost 0.762 (+14.3pp) 表明手工特征是 lossy compression，DDR 三分法可能不反映深度信号的真实结构。7-feature DDR 的价值区间窄（向上 QLoRA 远超，向下 detection baselines 接近）。
- **R2 (Rebut)**：DDR 和 QLoRA 回答不同问题（理解递归生成结构 vs 最大化分类精度）。QLoRA 的存在反而验证了 depth signal 的真实性，DDR 提供 QLoRA 无法提供的可解释分解。DDR 仅需 410M reference model (905 MB)，在 corpus-level audit 场景中有独立的效率优势。

**Director 判断**：R2 的论点更有说服力——DDR 和 QLoRA 的功能定位不同，QLoRA 不直接削弱 DDR 的解释性贡献。但论文应在 Discussion 中更清楚地阐述这一互补关系，并提供 QLoRA 的 cross-generator/cross-temperature 泛化对比以加强论证。记为 Should-Fix（W3）而非 Must-Fix。

---

## Questions for Authors

1. 使用 Glass's Δ 或 Cliff's delta 替代 Cohen's d 后，DDR 三分区边界是否改变？entropy std 是否仍为 "intermediate"？
2. 如果将 DDR 描述从 "3/1/3 data-driven partition" 调整为 "2-group primary structure with domain-informed 3/1/3 refinement"，是否影响 Contribution 2 的核心声称？
3. 为什么 Qwen 家族对温度变化不敏感而 Pythia/OLMo 显著受影响？这是否暗示 DDR 特征在测量 model-family-specific 属性而非 universal depth signal？
4. QLoRA 在 cross-generator/cross-temperature 泛化上是否也受同等影响？如果 QLoRA 更鲁棒，7-feature DDR 的解释性优势能否弥补泛化劣势？
5. 下游实验中 cross-seed std < 0.001 是否表明 seed-based variability 分析在此场景下无意义？
6. 5-class F1≈0.50 且 gen-2/3/4 不可区分——"depth profiling" 的概念是否本质上只有 2-3 个有意义层级？

---

## Missing References

1. **mdok of KInIT (SemEval/Voight-Kampff 2025)**：Multi-class AI text detection 竞赛第一名。需核实是否涉及 depth classification 还是 source attribution——如果是后者则与本文正交，无需引用。[R2 提出, R1 partial agree]
2. Orphan bib entry `self_refine` 应删除或引用。

---

## External Review (Stanford Agentic Reviewer)

外部审稿：未配置。

---

## Overall Assessment

**Overall Score: 3.0 (Findings)**

**评分理由**：

两位 Reviewer 独立评分均为 3.0 (Findings)，交叉分享后维持一致。

论文的核心价值在于（1）提出 generation depth classification 这一有意义的新任务，（2）DDR location/shape 分解提供了理解递归生成的结构化视角，（3）实验方法论极为严谨且负面结果诚实报告。

但在 EMNLP 2026 标准下，五个关键弱点制约其达到 Conference 级别：

1. **DDR 3/1/3 的统计基础**弱于 2-group 结构（k-means、holdout、boundary cases 均指向 2-group）
2. **Framing 断裂**：Introduction 的实用动机与 Discussion 的诊断定位不匹配
3. **新颖性受限**：三篇并行工作收敛于 ~3 classes，DDR 增量贡献收窄
4. **TOST n=3 效力不足**：下游结论不可靠但被用于核心论点
5. **Base-model-only + 温度敏感性**：实际适用范围极窄

**升级路径**：如果（a）补充 robust effect size 验证 DDR 分区稳定性，（b）重写 Introduction framing 为科学发现定位，（c）增加下游 seeds 或限定结论，论文有潜力达到 3.5 (Borderline Conference)。当前版本适合 Findings。

**Confidence**: 4/5 (High)——两位 Reviewer 在关键问题上高度一致，唯一实质分歧（QLoRA 对 DDR 的冲击）已充分讨论。

---

## Detailed Comments

### Abstract
- "LLM" 首次出现未展开，ARR 要求 Abstract 内定义缩写
- Binary F1=0.694 已作为主要数字报告（做得好），但 "three classes" 的强调可能让读者先期待 0.762

### Introduction (§1)
- L5 "downstream implications for model collapse theory and data provenance" 与 Discussion 不匹配——建议降级为 "connections to" 或 "relevance for understanding"
- L9 "No existing method addresses this task" 在三篇并行工作存在的情况下过于强烈——建议改为 "No existing method provides a feature-level decomposition of depth signal"
- Contribution 3 过于笼统（catch-all），建议拆分为 2-3 个具体发现

### Related Work (§2)
- §2.2 与 Broken Telephone/Markovian Chains 的三点区分合理且充分
- 引用总量 67 条，覆盖 detection/collapse/stylometry/provenance 四条主线，密度合理
- 核实 mdok of KInIT (Voight-Kampff 2025) 是否需要引用

### Method (§3)
- §3.1 ordinal classification framing 与 nominal XGBoost 的关系：Appendix H 已证明 ordinal classifiers 无优势，但应在正文简述理由
- §3.3 L61 "no larger candidate set was explored" 的诚实声明好，但应补充为什么不探索（interpretability constraint）
- §3.3 TTR-hapax r=0.97 的处理：应讨论 per-depth 相关性和 5-feature subset 的等效性

### Results (§4)
- Table 1 列顺序：binary F1 应在 3-class F1 之前
- §4.2 DDR 分区：建议明确 "2-group primary structure with 3/1/3 refinement" 的层次
- §4.2 应补充 Glass's Δ 或 Cliff's delta 作为 Cohen's d 的 robustness check

### Discussion (§5)
- L16 "diagnostic rather than prescriptive role" 的支撑（TOST n=3）不充分，应限定为 "preliminary evidence suggests"
- QLoRA vs DDR 的互补关系可以更清楚地阐述
- 建议增加对 performance ceiling (binary F1=0.694) 实际含义的讨论

### Limitations
- 温度限制应提升为首要条目
- Scale degradation 趋势应更明确讨论外推风险
- Instruct 退化应强调为 "fundamental limitation of current method" 而非可延伸的初步结果

### Format
- 正文 ≤8 页 ✓，行号 ✓，匿名化 ✓，Limitations/Ethics sections ✓
- Orphan bib: `self_refine` 应删除
- Table 2 baseline ms/text 标 N/A 需注明原因
- Figure 1 字体接近下限，建议增大