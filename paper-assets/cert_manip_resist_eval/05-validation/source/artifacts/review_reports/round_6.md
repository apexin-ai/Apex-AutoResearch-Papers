---
round: 6
review_mode: fresh
overall_score: 3.0 (Findings)
timestamp: 2026-05-25T06:15:23.895230+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Round 6 审稿报告

**论文**: "The Shifting Predictor: Panel-Size-Dependent Vulnerability Patterns in LLM Judge Panels"
**Venue**: EMNLP 2026 via ACL Rolling Review
**Reviewers**: R1（方法/实验严谨性）3.5 Borderline Conference · R2（新颖性与完整性）3.0 Findings
**交叉回应收敛度**: 高（R1 对 R2 的 6 条 weakness 同意 5 条，R2 对 R1 的 6 条同意 5 条）

---

## Summary

本文将 LLM 评审面板的攻击成功率（ASR）分解为最弱链路易感性（θ_base）和有效独立通道数（K_eff），在 15 个模型、6 种攻击、2 个多选基准上系统展示了 "predictor shift"：小面板（K=3）中个体鲁棒性主导，大面板（K≥5）中多样性（K_eff）主导。实验规模大（455–6,435 面板组合），统计方法论在 NLP 领域中属高标准（四种校正方法 + Cinelli-Hazlett 敏感度分析），但核心发现在严格推断框架下不稳健，K_eff 作为独立贡献的理论和实证基础均受到严重质疑。

---

## Strengths

**S1. 大规模系统性实验设计。** 455–6,435 面板组合，覆盖 6 模型家族、3 能力层级、6 攻击类型。组合式穷举方法论优于抽样式研究。[R1, R2 共识]

**S2. 统计推断标准高于 NLP 领域平均。** 四种独立校正方法（OLS、clustered SE、mixed effects、wild cluster bootstrap）同时报告，Cinelli-Hazlett 敏感度分析量化未观测混杂因素强度阈值。[R1, R2 共识]

**S3. 诚实报告局限性。** 主动承认 diversity-capability confound（r=0.70–0.81）、Bayesian R²=0.09、K_eff 某些条件 0/12 显著。Table 3 同时展示 4 种推断方法的不同结果，避免 p-hacking 嫌疑。[R1, R2 共识]

**S4. 实践价值。** "小面板筛选个体鲁棒性，大面板优化多样性" 的设计指南对 LLM-as-Judge 实践有直接参考意义。[R2]

**S5. 攻击类型覆盖全面。** 6 种攻击类型涵盖已知主要操纵策略，Table 2 系统报告所有条件下回归结果。[R1, R2]

**S6. 形式化基础。** Theorem 1（Weakest-Link Monotonicity）和 K_eff 信息论定义为实证分析提供理论锚点。[R2]

---

## Weaknesses

### Critical（影响接收决定）

**C1. [R1-W1 + R2-W1 共识] Predictor shift 在严格推断下不稳健，且与经典 ensemble theory 增量区分不足。**

这是两位 Reviewer 交叉审稿后达成的首要共识。问题有两层：

(a) **统计不稳健**：Crossed random effects 下，K=3 条件 θ_base 和 K_eff 显著性降至 0/12，K=7 同样降至 0/12，仅 K=5 保持显著。Shift 叙事（"K=3 个体主导 → K≥5 多样性主导"）在保守推断下碎片化为"仅 K=5 在部分方法下显著"。同时，K=3→K=7 样本量从 455 增至 6,435（14 倍），显著性上升可部分归因于统计功效机械增长。Appendix H 的 random subsample 分析基于 mean significance rate 而非对每次 subsample 的 shift pattern 进行系统检验，说服力有限。

(b) **Novelty 不足**：Predictor shift（个体质量在小 ensemble 更重要、多样性在大 ensemble 更重要）是 ensemble learning 的经典结论（Krogh & Vaidya 1995, Brown et al. 2005）。论文引用了这些工作但未明确阐述超越经典框架的维度。如果 shift 本身是 artifact，贡献进一步退化为经典理论的 LLM 场景重新验证。Section 5.3 的 random-vs-adversarial 区分是潜在增量点，但仅一段文字处理，未被提升为核心贡献。

**C2. [R1-W3 + R2-W2 共识] K_eff 作为独立贡献的理论和实证基础双重瓦解。**

两位 Reviewer 从不同方向对 K_eff 形成"上下夹击"：

(a) **理论端（R1）**：K_eff = K·exp(−2·MI) 的推导假设 Gaussian copula 依赖结构，但 Appendix T 的 Cramér-von Mises GoF 检验在 97–100% 的面板中拒绝了 Gaussian copula（p<0.001）。"有效独立通道数"的物理解读失去理论锚点。

(b) **实证端（R2）**：K_eff 与 κ-diversity 的 Spearman ρ=0.978（Table 16），实证层面几乎无增量信息。但两者显著性模式定性相反（K_eff 随 K 增大上升 4→9，κ-diversity 下降 8→6，Shannon MI 持平 4→4→0）——三个本质相似的 diversity 指标产生三种不同 shift 模式，说明 predictor shift 更可能是 K_eff 特定数学形式（exp(−2·MI) 非线性变换 + log-log 回归）的 artifact，而非稳健现象。

(c) **交叉互证**：理论假设被拒 → 无法用 "K_eff 捕捉了 κ-diversity 遗漏的结构" 解释分歧 → 分歧更可能源于数学变换 artifact。如果用 κ-diversity 替代 K_eff，predictor shift 消失。

**C3. [R1-W2 共识] Diversity-capability confound 未被有效控制——"underpowered de-confounding" 结构性困境。**

- Diversity 与 capability 相关性 r=0.70–0.81
- Cinelli-Hazlett 分析：25/36 条件下 K_eff 效应可被已知混杂因素解释
- Capability-matched subsampling（Pool A）功效仅 30.1%（84 panels at K=3 vs full 455）
- 唯一能控制混杂的方法恰好丧失了检测效应的统计功效——这是当前 15 个模型池的结构性限制，非论文写作可解决

R2 补充：Appendix K 跨基准预测的成功可能仅反映混杂变量（capability tier）在两个基准上的稳定性，而非 K_eff 本身的泛化能力。

**C4. [R1-W2 + R2-M3] INT4 量化混淆未解决——API-only 中 predictor shift 不复现。**

API-only 子集中 K_eff 显著性仅 2–3/12，shift 不复现。AWQ INT4 量化对脆弱性分布的影响在论文 tier 分类中被隐含承认但未显式讨论。VIF=4.4 不解释方向性消失。FP16 baseline 实验仍在运行中。

### Should-Fix（影响评分但不一票否决）

**S1. [R1-N2 + R2-W4 共识] 因果语言超出相关性分析支撑范围。**
Figure 1 caption "determines vulnerability"、Abstract "dominant vulnerability pathway"、Section 1 "mechanism"——核心分析是 OLS 回归（相关性），在 r=0.70–0.81 confound 下任何因果语言都超出支撑。这是自 Round 3 以来的反复问题（第 4 次被标记）。

**S2. [R2-W5, R1 部分同意] Theorem 1 深度有限。**
"用更脆弱评审替换面板成员只能增加 ASR"——直觉的形式化，缺乏定量 bound（ASR 增量与脆弱性差距的函数关系），也未刻画 shift point。R1 认为方向性保证仍有价值，建议降级为 supporting result。

**S3. [R2-W6 + R1 同意] K_eff 正系数的直觉解释不充分。**
更高 K_eff → 更高 ASR，与 BFT/Condorcet 定理（独立性保护容错）矛盾。Section 5.3 的 random-vs-adversarial 对比方向正确但仅约一段处理，未形式化区分。

**S4. [R1-W4] 显著性计数方法论问题。**
"X/12 conditions significant" 作为核心论据：12 条件非独立（2 benchmarks × 6 attacks × 共享模型池），不能简单计数；缺少跨条件 pooled effect size + heterogeneity statistics（I²、Q-test）；仅报告显著性二值化丢失效应量和方向信息。

**S5. [R1-W5 + R2 同意] Bayesian R²=0.09 的含义被低估。**
换聚合规则即让核心预测因子失效（R²=0.09），暗示因子可能仅在特定聚合条件下碰巧有统计关联。Random vs adversarial R² 对比（0.73–0.81 vs 0.27–0.43）缺乏置信区间或统计检验。

**S6. [R2-W3 + R1 同意] 实验范围仅限两个 MC 基准。**
MMLU 和 ARC 均为多选题。LLM-as-Judge 主要应用（开放式生成评估、复杂推理、安全性评估）的脆弱性模式可能完全不同。与 confound 问题正交叠加：内部效度（confound 未解耦）+ 外部效度（仅 MC）同时受损。

**S7. [R2-W7, R1 部分反驳] Conclusion 过于单薄。**
R2 认为缺少前瞻性讨论。R1 认为 8 页限制下篇幅取舍合理，但同意"模型能力提升后 shift 是否持续"值得加入。

### Minor

**M1.** Abstract 数字密度过高（0/12、12/12、r=0.70–0.81），部分可改用定性描述。[R2]

**M2.** Figure 1 文字标签在打印尺寸下偏小。[R2]

**M3.** 缺少匿名审稿代码链接（当前声称接收后发布）。[R2]

**M4.** Appendix 部分表格出现在 References 之后，与 ACL 模板标准排版顺序不完全一致。[R2]

---

## Reviewer Consensus

以下关键问题两位 Reviewer 达成共识 [AGREE]：

1. **Predictor shift 不稳健** — crossed RE 0/12（K=3, K=7）+ 功效膨胀 + 指标选择敏感 [R1-W1 ↔ R2-W1]
2. **K_eff 双重瓦解** — 理论假设被拒（97-100%）+ 实证与 κ-diversity ρ=0.978 无增量 + 三指标三模式 = artifact [R1-W3 ↔ R2-W2]
3. **Confound 结构性困境** — 25/36 被混杂解释 + Pool A 功效 30.1% = underpowered de-confounding [R1-W2]
4. **因果语言 overclaim** — 连续 4 轮被标记 [R1-N2 ↔ R2-W4]
5. **Novelty 受限** — 经典 ensemble theory 已预测类似模式 [R2-W1 ↔ R1 同意]

## Reviewer Divergence

1. **R2-W7 Conclusion 单薄**: R1 [REBUT]——8 页限制下篇幅取舍合理，不属于核心问题。R2 认为前瞻性讨论不可省略。
   → **判定**：minor 级别分歧，不影响整体评估。

2. **R1-W6 模型家族 vs 个体模型混杂**: R2 [REBUT]——mixed effects random intercepts 已部分处理，面板层级回归自然平滑家族内变异。R1 认为未检验家族内变异是否恰当处理。
   → **判定**：R2 的 rebut 有理，维持 minor 级别。

3. **评分分歧 3.5 vs 3.0**: R1 侧重方法论贡献（统计框架本身有价值），认为重新定位后可达 Conference。R2 侧重 novelty 和效应可靠性，认为即使重新定位核心效应仍不稳健。
   → **判定**：R2 的论证链更完整（shift artifact + confound + K_eff 双重问题三位一体），采纳 3.0 Findings 作为综合评分，但记录 R1 的 3.5 作为上界。

---

## Questions（需作者澄清）

**Q1.** K_eff 与 κ-diversity 的分歧机制——ρ=0.978 但显著性趋势定性相反，请提供形式化解释或合成数据实验。[R2-Q1, 两位 Reviewer 共识为最关键问题]

**Q2.** Crossed RE 下 K=3 的 0/12 和 K=7 的 0/12——是否测试过 crossed RE 的统计功效？是否对大 K 下采样至 455 面板后检验 shift 稳健性？[R1-Q1, R2 补充]

**Q3.** K_eff 正系数在 adaptive adversary 模型下能否被形式化证明？与 Condorcet jury theorem 的预测方向矛盾需明确解释。[R2-Q3]

**Q4.** 是否测试过任何非多选基准？MC 判断结构（离散选项、固定答案空间）与开放式连续评分的脆弱性模式差异是否被评估过？[R2-Q4]

**Q5.** Diversity-capability confound 是否考虑过工具变量法或其他因果推断方法？当前 Pool A 的 30.1% 功效下，"不显著"的结论无法区分"效应不存在"和"功效不足"。[R2-Q5]

**Q6.** Bayesian 聚合 R²=0.09 意味着什么？如果核心预测因子在不同聚合规则下失效，它们是否真正驱动面板脆弱性？[R1-W5]

---

## Missing References

1. **Breiman (2001)** "Random Forests" — ensemble diversity 与性能的奠基性工作 [R2]
2. **Dietterich (2000)** "Ensemble Methods in Machine Learning" — diversity 对 ensemble 改进的经典综述 [R2]
3. **Zhou, Wu & Tang (2002)** "Ensembling Neural Networks: Many Could Be Better Than All" — 何时增加 ensemble 成员有助 vs 有害，与 predictor shift 高度平行 [R2]
4. **Blanchard, Mhamdi, Guerraoui & Julien (2017)** "Machine Learning with Adversaries: Byzantine Tolerant Gradient Descent" — ML 中的 BFT，比 Lamport 1982 更切题 [R2]
5. **JudgeBench (Tan et al. 2024), Auto-J (Li et al. 2024)** — LLM judge 基准评估 [R2]
6. **Li et al. 2024, Zhu et al. 2020 DVERGE, Cameron & Miller 2015** — Round 5 已提出，待确认是否已加入 [R5-W3]

---

## External Review (Stanford Agentic Reviewer)

**状态**: 未请求。本轮未启用外部审稿。

---

## Visual Layout Check（非评分项）

**状态**: 已完成（2026-05-25 05:56–06:01，耗时约 5 分钟）

**统计**: 0 critical / 3 warning / 19 info

**Warnings**:
1. **Figure 编号不连续**（p.10-13）: Figure 编号从 Figure 6（p.8）跳至 Figure 8（p.10），缺 Figure 7。若正文或附录引用了 "Figure 7" 会导致审稿人困惑。
2. **Figure 9 子图字号偏小**（p.13）: Cinelli-Hazlett sensitivity contour plot（2×3 grid）轴标签和等值线数字估计 <6pt，屏幕阅读时难以辨认。
3. **附录连续纯文本**（p.14-16）: 连续 3 页无 display item（Sections M-X），审稿人翻阅时视觉疲劳。

**正面发现**:
- 主文 8 页符合 EMNLP 2026 long paper 限制 ✓
- Display items 密度 1.25/页（6 Figures + 4 Tables = 10 个），对实证论文充足
- 所有表格 booktabs 风格 ✓，小数位统一 ✓
- 无 margin 溢出、公式渲染错误、section heading 孤悬页底
- 未发现 [?] 未解析引用
- 注意：页眉标注 "Anonymous ACL submission"，确认 ARR 模板 header 是否需调整

---

## Overall Assessment

### 综合评分: **3.0 (Findings)**

| 维度 | R1 | R2 | 综合 |
|------|----|----|------|
| Soundness | 3.5 | 3.0 | **3.0** |
| Excitement / Novelty | — | 2.5 | **2.5** |
| Reproducibility | — | 4.0 | **4.0** |
| Overall | 3.5 | 3.0 | **3.0** |

**置信度**: 3.5/5（两位 Reviewer 分别在统计方法论和 ensemble/diversity 理论方面有专长，对 MI-based K_eff 和 Cinelli-Hazlett 框架的技术细节非完全确信）

### 一段话总评

这是一篇在实验规模和统计方法论方面达到高标准的实证研究——15 个模型、6 种攻击、四种校正方法同时报告、Cinelli-Hazlett 敏感度分析在 NLP 论文中罕见。论文诚实报告了大量负面和模糊结果，这在该领域值得肯定。

然而，核心发现 "predictor shift" 面临三重挑战：(1) **统计不稳健**——crossed random effects 下 K=3 和 K=7 均降至 0/12 显著，shift 仅在 K=5 + OLS/bootstrap 下成立；(2) **指标 artifact**——K_eff 与 κ-diversity ρ=0.978 但产生定性相反的 shift 模式（K_eff 上升、κ-diversity 下降、Shannon MI 持平），K_eff 的理论基础（Gaussian copula）被 97-100% 面板拒绝，shift 更可能是数学变换的副产品而非真实现象；(3) **novelty 不足**——经典 ensemble diversity theory（Krogh & Vaidya 1995, Brown et al. 2005）已预测 diversity 在大 ensemble 中更重要，本文未在严格推断框架下证明 LLM 评审面板存在超越经典预测的现象。

此外，diversity-capability confound（r=0.70-0.81, 25/36 条件可被混杂解释, Pool A 功效 30.1%）和仅限两个 MC 基准的实验范围使内部效度与外部效度同时存疑。

**推荐**: 适合 Findings 接收。论文在方法论展示（如何严谨地分析 LLM 评审面板安全性）和负面结果报告（diversity-capability 不可分离本身是重要发现）方面有 Findings 级别价值。但 predictor shift 的统计脆弱性、K_eff 的理论/实证双重问题、以及与经典理论的增量区分不足使 main conference 接收不太合适。若作者能 (a) 用 copula-free diversity 度量重做核心分析验证 shift 持存性、(b) 提供 crossed RE 功效分析和下采样稳健性检验、(c) 明确论证相对经典 ensemble theory 的增量——有望在修订后达到 Borderline Conference。

### 评分区间与条件

- **当前**: 3.0 Findings（R1: 3.5, R2: 3.0）
- **上界**: 3.5 Borderline Conference（若 shift 在 copula-free 度量下持存 + crossed RE 功效分析支持 + 重新定位贡献）
- **风险下界**: 2.5 Borderline Findings（若 K_eff 替换为 κ-diversity 后 shift 完全消失，确认为 artifact）

---

## Detailed Comments

### Section 1 (Introduction)
- "the mechanism behind observed ASR reductions remains unclear" → "mechanism" 暗示因果通路，应改为 "the statistical pattern" 或 "the dominant predictor"
- Contribution 1 仍需重构：从 "predictor shift 是新发现" 改为 "我们记录了在特定推断方法和 diversity 度量下观测到的 predictor shift 模式"

### Section 2 (Related Work)
- 缺少经典 ensemble learning 文献（Breiman 2001, Dietterich 2000, Zhou et al. 2002）的实质性讨论——不仅是引用，需明确论证 LLM 评审面板的独特性（对抗性操纵 vs 随机噪声、异质模型 vs 同质弱分类器）
- Blanchard et al. (2017) 的 ML BFT 比 Lamport (1982) 的经典分布式系统 BFT 更切题

### Section 3 (Threat Model & K_eff)
- K_eff 定义：Gaussian copula 被拒后，"effective independent channels" 语言需要条件化（"under the Gaussian copula approximation, whose GoF is rejected in 97-100% of panels"）
- 建议考虑 copula-free 替代方案：pairwise MI 均值、κ-diversity 直接使用、排列检验
- Theorem 1 考虑降级为 supporting lemma 或补充定量 bound

### Section 4 (Experiments)
- Table 1: AWQ INT4 量化对脆弱性分布的影响需显式讨论
- 显著性计数方法需升级：补充 pooled effect size + I²/Q-test

### Section 5 (Results)
- Table 2/3: 主文叙事应以 β_std 效应量模式为主线，显著性计数为辅
- Section 5.1: K_eff 正方向 + BFT/Condorcet 矛盾需明确展开（random vs adversarial 独立性作用差异）
- Section 5.3: Random-vs-adversarial 对比应扩展，可能提升为核心贡献维度；R² 对比需置信区间
- Bayesian aggregation R²=0.09 的深层含义需充分讨论

### Section 6 (Analysis)
- Cinelli-Hazlett 25/36: 跨基准预测成功可能反映混杂变量稳定性而非 K_eff 泛化
- Pool A 功效分析：明确声明 30.1% 功效下无法区分 "效应不存在" 和 "功效不足"

### Section 7 (Conclusion)
- 增加 2-3 句前瞻性讨论：模型能力持续提升后 predictor shift 是否持续

### Figure 1
- Caption: "determines" → "predicts" / "is associated with"
- 打印尺寸下文字标签偏小

### Appendix
- Figure 编号不连续（缺 Figure 7）
- Figure 9 子图字号 <6pt
- p.14-16 连续纯文本可考虑以小表格呈现部分分析
- Tables 10-19 出现在 References 后，检查 ACL 模板排版顺序

### 格式
- 页眉 "Anonymous ACL submission"——确认 ARR 模板 header 是否需调整
- 匿名审稿代码链接缺失（建议提供 anonymous GitHub）