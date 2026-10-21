---
round: 5
review_mode: fresh
overall_score: 3.0
timestamp: 2026-05-21T01:54:58.181474+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 5 (Fresh Review)

**论文**: A Sharp Detection Onset in Iterative Model Collapse
**Venue**: EMNLP 2026 (ARR May cycle), Long Paper
**审稿模式**: Fresh (重新审稿)
**Reviewer 编排**: 2 人 — R1 方法严谨性, R2 新颖性/完整性
**轮次**: Round 1 (单轮收敛)

---

## Summary

本文研究迭代合成数据训练中 model collapse 的统计检测问题。使用 permutation Granger causality (PermG) 在 Pythia-410M 上覆盖 13 个污染水平（α=0.00-1.00），发现检测率在 α_c≈0.50 处从 0/8 跳跃至 6/8 FDR-significant pairs（"sharp detection onset"）。论文提出 cascade ordering theory（entropy 先于 diversity 下降，Theorem 1）、S×R interpretive lens 解释非单调 dose-response、method sensitivity analysis 揭示方法选择使 null-control FPR 从 0% 膨胀至 75%，以及 canary-triggered intervention 降低 peak perplexity 58%。跨架构验证覆盖 6 个模型族（345M-6.9B），11/15 条件确认检测。

---

## Strengths

**S1. 方法选择敏感性分析是对 model collapse 检测领域的真实贡献** [R1, R2 共识]
五种检测方法在同一数据上的 forward significance 率从 0% 到 75%，inter-method agreement κ=0.185（近 chance）。PermG 在 4 种加权方案下均排名第一且是唯一实现 0% null-control FPR + consistent detection 的方法（Appendix Q Table 22）。这一发现对整个领域有重要警示价值。

**S2. 统计实践规范** [R1, R2 共识]
Permutation testing (5,000 permutations)、BH-FDR 校正、first-differencing 控制 spurious regression、specification curve analysis (1,160 specs)、null-control calibration。该领域论文中罕见。

**S3. Cascade ordering 在 15/15 条件下一致确认** [R1]
Entropy onset at generation 1, distinct-n at generation 2, 不依赖 Granger 检验——change-point analysis 独立确认（Appendix G）。

**S4. 对自身局限性高度透明** [R1, R2 共识]
Limitations section 诚实报告 GPT-2 失败、seed 依赖、non-monotonic scale behavior、specification curve 的 subset analysis 性质。

**S5. 实验设计系统** [R2]
15 model-seed 条件 × 13 污染水平 × 5 检测方法，附录完整（23 页含 29 tables/figures），承诺开源。

**S6. 实用干预验证** [R2]
Canary-triggered cessation 降低 peak perplexity 58% (bootstrap 95% CI: 29-64%)，robust operating band [10%, 22%]。

---

## Weaknesses

### CRITICAL (影响接收决定)

**C1. S×R 框架是标准 z-test power formula 的重参数化，非独立方法论贡献** [R1-N3, R2-N2; 共识]
Power(α,T) = Φ(S·R·√T/σ) 就是标准 Wald 检验 power formula (Power = Φ(δ√n/σ))，其中 effect size δ 被分解为 S(α)×R(α)。论文自身写 "We apply standard statistical power scaling to PermG"（§4.1）。R(α) 的非单调性是框架最有趣的预测，但从未被直接测量——论文测量的是 S·R 的乘积（检测率），非 R 单独。σ 定义模糊。作为 Contribution 1 的一部分，与实际增量不匹配。

**C2. 核心方法是计量经济学标准技术的直接移植，新颖性定位不清晰** [R2-N1, R1 部分同意; 共识]
PermG = Granger (1969) + permutation test；first-differencing 是标准预处理；BH-FDR 是 Benjamini & Hochberg (1995)；specification curve 来自 Simonsohn et al. (2020)。Introduction "four design choices" 框架暗示方法论创新，但实际是已有工具的组合应用。论文未充分回答：NLP 极短时间序列的特殊性在哪里？组合策略的增量贡献是什么？

**C3. T=10 时间序列的统计效力根本性不足** [R1-N1, R2-W4; 共识]
全部核心分析建立在 T=10 (11 data points) 上。lag-1 VAR 有效 df=8。Appendix N power simulation 使用线性 AR(1) DGP，实际非线性动力学可能使 power 更低。论文未提供基于观测 effect size 的事后 power calculation。"Sharp onset" 可能反映 detection power 的阶跃（统计功效曲线的标准 sigmoid 形状），而非 collapse dynamics 新发现。T=20 实验（仅在 Appendix）是唯一能在较充足 power 下验证 claim 的数据。

**C4. First-differencing 后 canary→perplexity 消失无法区分 power loss 与 spurious regression** [R1-N2; R2 部分同意]
Perplexity channel 原始 |r|=0.462 vs diversity |r|=0.920+（Table 25）。T=9, df=7 下弱信号消失可能是 power loss 而非 spurious regression 证据。24/24 vs 0/24 的全/无差异定性上 suggestive（如仅是 power loss 预期至少有部分通过），但缺乏 Monte Carlo simulation 量化 differenced PermG 在 |r|≈0.4 条件下的 power。"Canary claim scoped to diversity metrics only"（§5.2）若为 power artifact 则论文核心发现之一被削弱。

**C5. Headline 数字 (73%) 掩盖系统性架构依赖** [R2-N3, R1-W3; 共识]
Abstract "detection in 11/15 conditions (73%)" 将 GPT-2-medium 0/8（完全失败, 2 seeds）、SmolLM3-3B 3/8（单 seed）、Pythia-1.4B seed 依赖（2/8 vs 6/8）简单平均。4/15 failures 被归因于 "architecture-specific factors"——但这些正是泛化所需覆盖的维度。Intervention 实验仅 n=2 models（同一 Pythia 家族）。

### MAJOR (影响评分)

**M1. 标题 "Sharp Detection Onset" 暗示 collapse 动力学发现** [R2-W1; R1 同意]
实际是 PermG power curve 跨越检测阈值——Φ 函数本身就是 sigmoid-shaped，power curves 的陡峭 onset 是标准性质。§5.2 自承 "power curve crossing" 但标题/abstract 未充分反映。

**M2. "Four design choices" 框架攻击 straw man** [R2-W2]
Shumailov et al. (2024)、Dohmatob et al. (2024/2025) 研究 collapse dynamics（机理/scaling laws），不是 monitoring tools。批评它们没用 Granger causality/FDR 不公平。论文现称 "four design choices absent from existing monitoring analyses"（§1），但引用的 works 主要贡献是描述 collapse 而非 monitoring。

**M3. α_c bootstrap CI [0.43, 0.56] 过宽** [R1-W1]
Sigmoid SE=0.006 来自单 seed 参数不确定性，未涵盖 cross-seed variability。Bootstrap CI 跨越有效范围 13%。主文应报告 CI 而非 SE；"critical contamination level" 精度声明需 temper。

**M4. 0/24 null-control FPR 有效独立观测量被高估** [R1-W2]
同一 seed 内 8 pairs 共享训练轨迹。ICC=0.34, cluster-adjusted CI [0%, 41%]。以 seed 为 cluster unit，effective n 远低于 24。需 cluster bootstrap 和 per-seed FPR 报告。

**M5. T=20 predictions 大多数 trivial** [R1-W4]
"Four of five predictions match" 中仅 α=0.45（0/8→5/8）为 non-trivial prediction。其余 4 个为已 saturated cases 的延续。

**M6. Intervention 15% threshold post-hoc** [R1-W5]
同一数据集选择 threshold 和评估性能，无 held-out 或 cross-validation。n=2 models, α=1.0 only。应标注 proof-of-concept 性质。

**M7. Theorem 1 数学深度有限** [R2-W3]
"Entropy 先于 diversity 下降"是直观观察，证明仅用 Jensen 不等式。被定位为 "Cascade ordering theory with formal proof"，与实际深度不匹配。

### MINOR

**m1.** Abstract 信息密度过高（13+ 数值）[R2-W5]
**m2.** "Granger-causes" vs "Granger-precedes" 术语残留不一致 [R2-W6]
**m3.** scheffer2012anticipating orphan bib entry [R1-M1, R2-M3]
**m4.** alemohammad2024mad, marcinkevics2022neural first author mismatch [R1-M2, R2]
**m5.** gerstgrasser2024model 和 dey2024breaking 疑似重复 bib entries [R1-M3]
**m6.** σ 在 S×R power formula 中定义不清 [R1, 延续自 Round 4]
**m7.** Figure 2 尺寸偏小，建议改为 figure* [视觉审查]

---

## Reviewer Consensus

两位 Reviewer 在以下关键问题上达成共识 [AGREE]：

1. **S×R = power formula reparameterization**: 两位均独立识别 Power(α,T)=Φ(S·R·√T/σ) 为标准 z-test power 公式。
2. **T=10 power 根本性受限**: 两位均认为主体 claims 的统计基础不充分，T=20 应提升为主体结果。
3. **跨架构泛化不足**: 两位均认为 73% headline 掩盖系统性失败模式，应弱化 claim。
4. **方法论新颖性**: 两位均同意核心方法是计量经济学标准技术的迁移，但 R1 更强调方法敏感性分析是真实贡献。
5. **Framing 问题**: 两位均认为标题和 narrative 仍暗示 collapse dynamics 发现而非 statistical detection boundary。
6. **方法敏感性分析是主要贡献**: 两位均肯定 FPR 0%→75% 的发现对领域有重要价值。

## Reviewer Divergence

1. **First-differencing 解读**: R1 将其列为 CRITICAL（power loss 无法排除），R2 认为 24/24 vs 0/24 的全/无差异 "suggestive"。双方同意需要 simulation 验证。
2. **评分**: R1 给 3.5（Borderline Conference, 方法敏感性分析足够支撑）, R2 给 3.0（Findings, 新颖性不足是首要障碍）。分歧来自对 "标准方法的成功应用" 是否构成 Conference 级别贡献的判断。

---

## Questions

**Q1.** 在 T=10, lag=1 条件下，PermG 对 diversity channel (|r|≈0.92) 和 perplexity channel (|r|≈0.46) 的事后 statistical power 分别是多少？若 perplexity channel power < 80%，如何排除 first-differencing 后消失是 Type II error？

**Q2.** S(α) 和 R(α) 能否被独立估计？如果不能，S×R 框架相比直接报告 PermG effect size 有什么额外的 explanatory value？

**Q3.** GPT-2-medium 0/8 失败的根因？能否通过 ablation 确定是 tokenizer、架构还是训练目标的差异？

**Q4.** α_c(T) 是否存在 scaling law？对实际部署（monitoring window 选择）有直接影响。

**Q5.** T=20 predictions 是否在观察 T=20 数据之前锁定？如是，请提供时间戳或版本控制证据。

**Q6.** Intervention 15% threshold 是否在 intervention 数据收集之前确定？Operating band [10%, 22%] 是否使用了 intervention 后的数据？

**Q7.** 论文声称 "Granger precedence is not causation"（§6），但 §5.5 intervention 假设 entropy→diversity 因果关系。理论基础是什么？

---

## Missing References

1. **Donoho & Jin (2004)** "Higher criticism for detecting sparse heterogeneous mixtures," Annals of Statistics 32(3):962-994 — sparse signal detection boundary 与 detection onset 直接相关 [R2]
2. **Dickey & Fuller (1979)** / **Phillips & Perron (1988)** — 标准 unit root 检验，论文讨论 non-stationarity 但未引用 [R1]
3. **Zapata & Rambaldi (1997)** "Monte Carlo evidence on cointegration and causation" — 小样本 Granger causality size distortion，与 T=10 直接相关 [R1]
4. **scheffer2012anticipating** — orphan bib entry，正文未引用 [R1, R2]
5. **alemohammad2024mad, marcinkevics2022neural** — bib first author 与 OpenAlex 记录不匹配 [R1, R2]
6. **gerstgrasser2024model / dey2024breaking** — 疑似重复 bib entries [R1]

---

## External Review

**状态**: 未请求（项目未配置外部审稿）。

---

## Visual Layout Check（非评分项）

**状态**: done (耗时 4 分钟)

**Findings**:
- **[WARNING]** 连续 2 页无 figure/table（p.4-5, Method §4 + Experiments §5 开头）。建议加方法概览图或小表格打破文字墙。
- **[INFO]** 主文仅 4 个 display items（0.5/页），对实证论文偏低（通常 5-8 个）。附录 ~30 个 display items。建议将关键附录表格/图表提升到主文。
- **[INFO]** Figure 2（Metric traces）仅占右栏，信息密度高，考虑改为 figure*（全宽）。
- **[INFO]** Figure 1 质量好：bootstrap CI 阴影清晰，regime 分区标注直观。
- **[INFO]** Table 1, 2 格式规范（booktabs），caption 自包含。
- **[INFO]** Algorithm 1, Figure 3, Figure 4 格式规范。
- **[INFO]** References 无 [?] 未解析引用。附录组织有序。

---

## Overall Assessment

**Overall Score: 3.0 (Findings)**

**Soundness**: 3.0/5 — PermG 方法本身合理，但 T=10 效力根本性受限；first-differencing scoping 无法排除 power loss；0/24 FPR 有效 n 被高估。

**Excitement**: 2.75/5 — 方法敏感性分析（FPR 0%→75%）有真实贡献，cascade ordering 有价值，但 S×R 是 reparameterization，核心方法为标准技术迁移。

**Reproducibility**: 4.0/5 — 实验网格详尽，附录完整，承诺代码公开。

**Confidence**: 4/5 — 两位 Reviewer 均熟悉 Granger causality、permutation testing、model collapse 文献。

**评分理由**:

论文在 model collapse 检测领域做了系统性的实证工作，方法敏感性分析是对该领域的真实贡献，cascade ordering 在 15/15 条件下的一致性令人印象深刻。然而，三个核心问题阻止主会议接收：

(1) **新颖性不足**: 核心方法是计量经济学标准技术的组合应用，S×R 框架是 power formula 的 trivial reparameterization，Theorem 1 数学深度有限。论文的主要价值在于 empirical characterization 而非 methodological innovation。

(2) **统计基础受限**: T=10 时间序列使所有 Granger 分析在效力边界运行；first-differencing scoping（论文核心发现之一）无法排除 power loss；null-control FPR 验证因非独立性被高估。

(3) **泛化证据薄弱**: 73% 跨架构确认率掩盖系统性失败模式（GPT-2 0/8, SmolLM3 3/8, Pythia-1.4B seed 依赖），intervention 仅 n=2 同一家族。

**推荐**: Findings 接收。论文的 empirical contributions（method sensitivity analysis, cascade ordering, regime characterization）对从业者有价值，但方法论新颖性和统计严谨性未达到主会议标准。

**修改建议优先级**:
1. [P0] 将 S×R 从 "theoretical framework" 降级为 "interpretive lens"
2. [P0] 提供基于观测 effect size 的事后 power analysis; 将 T=20 提升为主体结果
3. [P0] 弱化 cross-architecture generalization claim; 在 abstract 中明确呈现失败模式
4. [P1] Monte Carlo simulation 验证 first-differencing 后 perplexity 消失是否为 power artifact
5. [P1] 重新定位 contribution: empirical characterization + method sensitivity meta-contribution
6. [P1] 标题和 abstract 明确标注 "statistical detection boundary" 性质
7. [P2] Cluster bootstrap for null-control FPR; report per-seed FPR
8. [P2] Intervention threshold 标注 post-hoc; leave-one-seed-out CV
9. [P2] Abstract 精简数值; 引用修复; orphan bib 清理

---

## Detailed Comments

### §1 Introduction
- 叙事结构清晰，从 model collapse → early detection → Granger causality，逻辑链完整。
- 脚注 1 正确区分 Granger precedence 和 true causation，值得肯定。
- **问题**: "Four design choices absent from existing monitoring analyses" 中引用的 works 主要研究 collapse dynamics 而非 monitoring，构成 straw man。建议改为 "prior work focused on characterizing collapse; we develop a monitoring framework" 或将 design choices 限定于 monitoring 子领域。

### §2 Related Work
- 覆盖面广，分为四个子领域，组织合理。
- Truong & Truong (2026) 已引用但讨论不深——collapse 是一阶相变→CSD 类比在理论上无基础，需明确区分。
- 缺少 small-sample Granger causality 文献——这是本文方法核心限制。

### §3 Cascade Ordering Theory
- Theorem 1 和 Proposition 2 陈述清晰。
- 但数学深度有限（Jensen 不等式），被定位为 "theory with formal proof" 不匹配。
- Mode amplification 假设（Assumption 3）适用范围需讨论。

### §4 Method
- 五种检测方法并行评估是亮点。
- PermG 实现细节充分。
- **问题**: S×R lens 定位不清；σ 未在 equation 附近定义；Method sensitivity analysis 段过于简略（是论文最重要贡献之一，建议扩展）。

### §5 Experiments
- §5.1 Setup: 合理但 5,000 samples/generation 选择未给理由。
- §5.2 Sharp Detection Onset: 核心结果清晰。建议主文报告 bootstrap CI [0.43, 0.56] 而非 SE=0.006。
- §5.3 Dose-Response: S×R 叙述直觉有吸引力但数学上是 reparameterization。
- §5.4 Cross-Architecture: 4/15 failures 逐一分析是好做法，但 "architecture-specific factors" 解释本质 post-hoc。
- §5.5 Intervention: proof-of-concept 性质，n=2 models 过少。缺少 random stopping baseline。

### §6 Discussion
- "Granger precedence is not causation" 讨论必要。
- α_c vs CMR 讨论未深入——可能是错过的 contribution opportunity。

### Limitations
- 透明全面。特别肯定对 non-monotonic scale behavior 的承认。

### Appendix
- 内容丰富（15 页），建议将 Appendix N power analysis 核心结果和 Appendix E specification curve summary 纳入主文。
- 主文仅 4 个 display items 对实证论文偏低。