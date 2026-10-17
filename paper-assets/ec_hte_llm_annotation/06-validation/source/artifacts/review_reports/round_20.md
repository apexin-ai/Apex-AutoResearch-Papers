---
round: 20
review_mode: fresh
overall_score: 3.5 - Borderline Conference
timestamp: 2026-05-24T17:19:58.840317+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Round 20 审稿报告

> Venue: EMNLP 2026 via ARR | Reviewers: 2 | Rounds: 1 + 交叉分享 | 模式: Fresh

---

## Summary

本文研究 LLM 标注在异质处理效应 (HTE) 估计中的偏差问题。核心理论发现：当 LLM 分类器误差率在子群间存在异质性时，标准全局混淆矩阵校正可引入新偏差甚至反转 CATE 符号。论文推导了偏差恒等式 (Theorem 1: bias = δ_s · Δτ / (1-2π̄))，提出基于层级贝叶斯的逐子群校正方法 (EC-HTE)，并在合成（520 配置）、半合成（8 LLMs × 2 任务）和真实数据（hate speech）上验证。

---

## Strengths

1. **理论分解干净且可解释 [共识]**：Theorem 1 将 global correction 偏差分解为三个可独立估计的因子——δ_s（子群误差偏离）、Δτ（处理效应异质性）、1/(1-2π̄)（矩阵求逆放大）。R1 逐步验证了 Appendix B 的矩阵代数证明，M⁻¹_global · M_s 的 (1,1) 项和 (1,2) 项推导正确。

2. **Proposition 5 的 Δτ-free 诊断准则有实用价值 [共识]**：无需估计处理效应即可判断 global correction 是否有害，是可操作的前置检查工具。两位 Reviewer 均列为主要优势。

3. **实验验证异常充分 [共识]**：33 页中 25 页附录，覆盖：520 个合成配置（R²=0.994, K=2）、8 个 LLM 半合成实验、hate speech 真实案例、10+ 假设违反的 robustness 分析（outcome-dependent/treatment-dependent/confounded/asymmetric 等）、先验敏感性、bootstrap SE 校准、CausalForest oracle coverage。两位 Reviewer 均称"最充分的附录之一"。

4. **方法实用性好**：HB 估计 <5ms（经验贝叶斯优化），κ-guard 保障数值稳定性（实际 κ_max=1.485，远低于阈值 100），对实践者友好。

5. **与 PPI/DSL 框架的组合性**：Appendix K/U 验证了 EC-HTE 与 PPI 和 DSL 的互补组合（combined bias: 0.179→0.007），Table 11 有实证。

---

## Weaknesses

### Critical（影响接收决定）

**C1. [共识-Major] 对称误分类假设 (A2) 严重限制标题级 "Exact Identity" 声称**

Theorem 1 的精确性严格依赖 FPR=FNR（假设 A2），但真实 LLM 分类器几乎总是非对称的（Table 22: GPT-4o TweetEval FPR=0.249, FNR=0.157；GPT-4.1 Civil Comments FPR=0.098, FNR=0.042）。Appendix J 的非对称推广将精确恒等式退化为充分条件（max |B₁,₁| > max(FPR_s, FNR_s)），R² 从 >0.97 降至 ~0.73（48 个非对称配置）。当 FPR/FNR 比值极端（1:3 或 3:1）时 R² 进一步退化。

主文仅在 Remark 2 (p.5) 用一句话提及，而整个推导流程（Theorem 1 → Proposition 5 → Section 4）完全建立在对称假设上。论文标题和 Abstract 的核心卖点是 "exact bias identity"，但这个精确性在最常见的实际应用场景下不成立。

- R1 初审提出 (Must-Fix)，R2 交叉回应从 Minor 升级为 Major
- **修改要求**：(1) 主文给出 2×2 非对称情形的精确偏差 closed-form（R1 建议形式：bias = [(1−π̄)(FPR_s − FPR̄) − π̄(FNR_s − FNR̄)] / [(1−FPR̄−FNR̄)] · τ(1) + [...]·τ(0)），或 (2) 明确限定 "exact" 的适用条件，调整标题/Abstract 表述

**C2. [共识-Major] 相对经典测量误差理论的理论增量未界定**

Theorem 1 可视为 Frazis-Loewenstein (2003) 经典衰减公式（β̂ = β·(1−2π)）在子群层面的推广，数学难度有限。论文未在主文中讨论与 F-L 的关系，也未界定自身的理论增量边界。

R1 交叉回应 AGREE with nuance，补充了两个独立增量点：(a) 三因子分解的可解释性是新的——F-L 讨论回归系数衰减，不涉及子群异质性修正；(b) Proposition 5 的诊断准则在 F-L 框架中不存在。共识：这是 framing 问题而非 soundness 问题。

- **修改要求**：Section 2 或 3 开头用 1-2 句明确声明与 F-L (2003) 的关系（"our identity can be viewed as a subgroup-stratified generalization of the classical F-L attenuation"），同时强调分解形式和诊断准则的独立贡献

**C3. [共识-Major] 缺失噪声标签学习核心文献**

Related Work 未讨论噪声标签学习文献，特别是：
- Natarajan et al. (2013) "Learning with Noisy Labels" — 混淆矩阵校正在分类器训练中的经典应用，使用完全相同的 M⁻¹ 结构
- Patrini et al. (2017) "Making Deep Neural Networks Robust to Label Noise" — forward/backward loss correction

R1 交叉完全同意，并补充了 instance-dependent noise 方向（Xia et al. 2019; Cheng et al. 2022），其中误分类率因样本而异——与本文 subgroup-specific misclassification 密切相关。虽然目标不同（分类器训练 vs 因果推断），但核心数学工具一致。不讨论这些工作是面向 NLP/ML 会议的明显遗漏。

- **修改要求**：Related Work 增加噪声标签学习段落，讨论与 transition matrix estimation 文献的联系和区别

### Should-Fix（影响评分）

**W1. [分歧: R1 Must-Fix / R2 strong Should-Fix] MC=100 不足以支撑 coverage 声称**

100 次 MC 运行下，95% coverage 估计的标准误 ≈ 2.2pp，95% CI 为 [90.7%, 99.3%]。Table 1 中 EC-HTE coverage 0.96 vs nominal 0.95 的差异完全在统计噪声范围内。

R2 指出跨 520 配置的一致性部分弥补了单配置 MC 数不足（如果绝大多数配置 ≥0.93，这一模式提供超越单次 MC 的证据强度）。共识：至少在 Table 1 报告 MC 标准误作为最低成本有效修复。

- **修改要求**：Table 1 添加 MC 标准误列（±2.2pp at B=100 MC runs）；或将关键配置增加至 ≥500 MC runs

**W2. [共识] 方法论技术新颖性偏浅**

EC-HTE pipeline 三个组件（Dirichlet-Multinomial HB、逐子群 M⁻¹ 校正、variance-adjusted SE 传播）均为教科书级成熟技术。R1 补充：经验贝叶斯（marginal likelihood maximization）在此规模问题上完全够用（<5ms），说明方法层面无新技术挑战。

共识：核心贡献应定位为理论洞察而非方法。贡献分配 theory (60%) + empirical (20%) + method (20%)，方法新颖性不高不致命，前提是 theory 和 empirical 足够强。

- **建议**：论文应更明确将贡献定位调整，降低方法新颖性期望

**W3. [共识] Corollary 7（子群异质处理效应推广）应进入主文**

假设 (A5) 要求 τ(z,s) = τ(z)，即处理效应跨子群同质——意味着所有观测到的 HTE 异质性是误分类伪影。但 Corollary 7 (Appendix Z.1, p.28) 推广到 Δτ_s 因子群而异的情形（bias ∝ δ_s · Δτ_s），这是一个实质性推广，却被埋在附录第 28 页。

- **修改要求**：Section 3 Theorem 1 之后用 2-3 行提及 Corollary 7 结论并指向附录。不需要额外公式空间。

**W4. [分歧: R1 Must-Fix / R2 Should-Fix] 假设 (A1) 灵敏度分析形式单一**

仅用单一参数 logistic link（γ ∈ [0, 0.20]）。R2 认为横向覆盖面充分（8 种假设违反类型），参数化是领域标准做法，但纵向深度不足。

- **建议**：增加一种基于文本特征的 confounding 形式（如文本长度/复杂度同时影响 LLM 标注准确率和处理效应），比抽象非参数违反更贴合 NLP 场景

**W5. [共识] 仅用 CausalForestDML 作为下游估计器**

Appendix S 测试了 R-learner（结果一致），但 R-learner 和 CausalForest 都属于基于损失的估计器。X-learner（imputation-based）和 BART（贝叶斯树）未经验证。论文声称 EC-HTE 的校正是 estimator-agnostic 的，但实证覆盖不足。

- **建议**：附录增加至少一个替代估计器（X-learner 或 BART），或在 Limitations 中明确讨论

**W6. [共识] Bootstrap B=100 偏小**

B=1000 是更标准选择。Appendix Y 表明 plug-in SE 已 well-calibrated，full bootstrap 仅微调至 exactly 95.0%。

- **建议**：说明 B=100 足够的理由（plug-in SE 已校准，bootstrap 仅作微调），或改用 B≥500

### Minor

- p.1 Abstract: "per-model range 0.26-0.09" 应为 "0.09-0.26"（从小到大排序）
- p.4 Theorem 1: "effect-modifier level z" 对 NLP 读者不友好，建议首次出现时用例子说明
- p.7 Figure 2: "ε-guard" 标注字号偏小
- p.8 Table 1: 建议标注 MC 标准误（±2.2pp at 100 MC runs）
- p.33 Algorithm 1: Step 8 的 κ̃ 阈值应与 Appendix A.1 的分析（κ=100）一致标注

---

## Reviewer Consensus

| 主题 | R1 | R2 | 结论 |
|------|-----|-----|------|
| Overall Assessment | 3.5 | 3.5 | **3.5 Borderline Conference** |
| Soundness | 4/5 | 4/5 | 4/5 |
| A2 对称假设是核心弱点 | N1 Must-Fix | ↑升级为 Major | **Critical** |
| 实验验证充分 | S3 | S3 | 最突出优点 |
| 噪声标签文献缺失 | 交叉 AGREE | W3 Major | **Critical** |
| 理论增量需界定 | 交叉 AGREE w/ nuance | W1 Major | **Critical** (framing) |
| Corollary 7 应进主文 | W1 | AGREE | **Should-Fix** |
| 需更多下游估计器 | W4 | AGREE | **Should-Fix** |
| 方法新颖性有限 | AGREE | W2 Major | **Should-Fix** |
| Bootstrap B=100 偏小 | W3 | AGREE | **Should-Fix** |

---

## Reviewer Divergence

| 主题 | R1 | R2 | 分歧性质 |
|------|-----|-----|----------|
| Excitement | 3.5/5 | 3/5 | R2 更严格：认为理论增量更有限（经典测量误差理论的直接推广） |
| MC runs 严重程度 | Must-Fix | strong Should-Fix | R2 认为跨 520 配置一致性部分弥补单配置 MC 数不足 |
| A1 灵敏度分析 | Must-Fix | Should-Fix | R2 认为参数化灵敏度分析是领域标准做法 |
| Expert labels 成本 | Should-Fix | REBUT | R2 论证：expert labels 用于校准 CM（每群 50 个），非直接 HTE 估计；200 labels 校准后用 N=5000 LLM 标注做 HTE 远优于用 200 labels 直接做 HTE。Appendix I Figure 5 已回答此问题。**Director 判定：R2 的 REBUT 有理，此项不纳入修改要求** |
| 升级至 4.0 条件 | 2 条 | 4 条 | R1 要求非对称公式 + MC≥500；R2 额外要求 F-L 增量界定 + 噪声标签文献。R2 门槛更高 |

---

## Questions（需作者在 Rebuttal 中回答）

1. **[核心]** 2×2 非对称情形（FPR_s ≠ FNR_s）的精确偏差 closed-form 公式是什么？其可解释性相对对称情形的三因子分解如何？
2. Corollary 7（子群异质处理效应推广）为何未在主文中呈现——是证明依赖额外假设，还是纯粹篇幅考虑？
3. 诊断准则（仅需混淆矩阵估计，无需 expert labels）相对于直接运行 EC-HTE（需 expert labels，<5ms）的使用场景差异是什么？如果 expert labels 已收集，诊断准则是否冗余？
4. 层次贝叶斯可交换性假设在文本特征根本不同的子群间（如 Reddit 评论 vs Twitter 推文）是否成立？Appendix P 的 Robustness to Subgroup Misspecification 是否充分回答了这个问题？
5. 能否给出 minimum expert budget 的理论下界（如基于混淆矩阵估计的 Fisher information），而非仅依赖 Appendix I 的经验 crossover curves？

---

## Missing References

**必须补充：**
- Natarajan et al. (2013) "Learning with Noisy Labels" — 混淆矩阵校正在分类器训练中的经典应用
- Patrini et al. (2017) "Making Deep Neural Networks Robust to Label Noise" — forward/backward loss correction

**建议补充：**
- Xia et al. (2019), Cheng et al. (2022) — instance-dependent noise methods（与 subgroup-specific misclassification 密切相关）
- Frazis & Loewenstein (2003) — 如已引用，应在主文中更显著讨论
- Zhang et al. (2024, NeurIPS) "Causal inference with LLM annotations"（如果与本文问题设置重叠，需确认真实性）

---

## External Review (Stanford Agentic Reviewer)

**状态：未请求。** 本轮未启用外部审稿。

---

## Visual Layout Check（非评分项）

视觉审查已完成（耗时 ~4 分钟）。**0 critical / 3 warning / 10 info。**

**Warnings:**
1. **前 2 页纯文本密集**：Title/Abstract/Intro/Contributions/Related Work 开头无任何 display item，第一个视觉锚点 Figure 1 出现在第 3 页顶部——在 3 页阈值内但审稿人第一印象偏重
2. **正文 display items 过少**：8 页正文仅含 3 个 display items（Figure 1 p3、Figure 2 p7、Table 1 p8），几乎所有定量实验证据推至附录（~38 张表 + 6 张图）。审稿人在正文中只能看到 1 张结果表。建议将 1-2 张关键附录表（如诊断 ROC 曲线 Figure 4 或 expert budget crossover Figure 5）提升至正文
3. **Pages 4-6 理论推导连续 3 页无图表**：Section 3（Bias Decomposition）和 Section 4 开头均为纯理论推导，对理论密集内容可豁免，但跨度达 3 整页

**Positive highlights:**
- Figure 1 三面板颜色区分度良好，caption 自包含，能独立传达核心 message（全局校正导致 sign reversal）
- Figure 2 pipeline 图使用 colorblind-safe 配色（蓝/红），清晰可读
- Table 1 booktabs 三线表格式专业，最优结果加粗，数值精度一致
- Limitations 段落长度适中（约半栏，3-4 点），符合 EMNLP 要求
- 参考文献格式统一，无 [?] 未解析引用
- Algorithm 1 放在附录最后一页较隐蔽（如对方法理解重要可前移）

---

## Overall Assessment

**Overall Score: 3.5 — Borderline Conference**

**评分明细：R1 = 3.5 (Soundness 4, Excitement 3.5, Reproducibility 4.5, Confidence 4) | R2 = 3.5 (Soundness 4, Excitement 3)**

**Director 判定：3.5（建议 Findings 接收，Rebuttal 后有望提升至 Conference）**

**核心判断：**

本文在 LLM 标注的因果推断中做出了干净的理论贡献（Theorem 1 偏差恒等式）和极其全面的实验验证。问题定位精准——effect modifier misclassification 是 PPI/DSL/PPCI 均未覆盖的盲区，在 LLM-as-annotator 快速增长的背景下具有实际意义。

然而，两位 Reviewer 从不同角度（R1 侧重方法严谨性，R2 侧重新颖性定位）指出了同等级别的不足：
1. **"Exact" 声称的诚实性**：标题级贡献在最常见的非对称误分类场景下只是近似（R² ~0.73），主文对此讨论严重不足
2. **理论增量边界模糊**：与 Frazis-Loewenstein (2003) 经典文献的关系未界定，与噪声标签学习文献（Natarajan 2013, Patrini 2017）的联系完全缺失
3. **方法层面无技术创新**：EC-HTE 是成熟组件的组合，贡献定位应更明确偏向理论洞察

**Rebuttal 升级路径（→ 4.0 Conference）：**
- **[必须]** 给出 2×2 非对称精确偏差 closed-form 或调整 "exact" 声称范围
- **[必须]** 补充 Natarajan et al. (2013) / Patrini et al. (2017) 的讨论
- **[必须]** 在主文中界定相对 F-L (2003) 的增量贡献
- **[强烈建议]** Table 1 报告 MC 标准误
- **[建议]** 主文提及 Corollary 7

前 3 项为两位 Reviewer 共同要求。R1 明确表示满足非对称公式 + MC 改进后愿上调至 4.0；R2 需要额外满足增量界定 + 噪声标签文献。综合两方条件，以上 5 项全部满足是 4.0 的充分条件。

---

## Detailed Comments

### Section 1 (Introduction)
- 问题定位（global correction can hurt when error rates vary across subgroups）清晰有力，motivating example 有说服力
- 未提及与 F-L (2003) 的关系——应在 Intro 中定位理论增量

### Section 2 (Related Work)
- 覆盖了 PPI (Angelopoulos et al. 2023)、DSL (Egami et al. 2023)、PPCI 等核心方向，50+ 引用
- **关键遗漏**：噪声标签学习文献（Natarajan 2013, Patrini 2017）使用相同的 M⁻¹ 校正结构，目标不同（分类器训练 vs 因果推断），应讨论联系和区别

### Section 3 (Bias Decomposition)
- Theorem 1 代数正确（R1 逐步验证），三因子分解可解释
- A2 (symmetric misclassification) 的地位需重新处理：当前标注为 "expository simplification"，但标题级 "exact" 依赖于此。建议给出非对称 closed-form 或明确限定
- Corollary 7 推广到 Δτ_s 因子群而异的情形，应在 Theorem 1 后提及

### Section 4 (EC-HTE Method)
- HB 估计使用经验贝叶斯（marginal likelihood maximization），计算高效但无新技术贡献
- κ-guard 数值稳定性设计务实（实际 κ_max=1.485）
- Eq. 7 不确定性传播缺消融实验（vs 点估计校正）

### Section 5 (Experiments)
- 合成实验覆盖面极其全面（520 配置），但 MC=100 的 coverage 精度有限
- Table 1 仅展示 4 配置 × 2K 值，正文定量证据偏少——大量结果在附录
- 下游估计器仅 CausalForest + R-learner（均基于损失），缺 imputation-based（X-learner）和贝叶斯树（BART）

### Section 6 (Conclusion)
- 已改进（从 2 句扩展到 3 句），含 adoption guideline 和 relaxed screening
- 可进一步加强：简要提及非对称推广的现状和未来方向