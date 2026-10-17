---
round: 9
review_mode: fresh
overall_score: 3.5
timestamp: 2026-05-23T06:31:47.766641+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Round 12 审稿报告：Error-Corrected Heterogeneous Treatment Effects

**目标 Venue**: EMNLP 2026 (ARR May cycle)
**审稿人**: Reviewer 1, Reviewer 2
**交叉回应**: Reviewer 1 ↔ Reviewer 2 完成
**Overall Score**: 3.5 (Borderline Conference)

---

## Summary

本文研究 LLM 标注用于因果推断（HTE 估计）时，全局混淆矩阵校正在子组间引入系统性偏差的问题。主要贡献：(1) 推导精确偏差恒等式（Theorem 1），表明全局校正偏差与 δ_s·Δτ 成正比；(2) 提出 EC-HTE，基于分层贝叶斯估计子组混淆矩阵进行分组校正；(3) 给出无需估计处理效应的诊断准则（Proposition 3）。实验覆盖合成、半合成（TweetEval）及多个鲁棒性验证，展示 EC-HTE 在极端异质性条件下将偏差从 0.059 降至 0.010。

论文技术扎实，理论推导严谨，实验设计全面。主要不足在于：(1) 诊断工具在真实 LLM 混淆矩阵上 AUC 降至 0.63，但摘要仅报告 0.86；(2) 方法论新颖性有限——EC-HTE 本质上是识别问题后的自然修复；(3) 缺乏真实因果数据集验证；(4) 主体正文视觉密度偏低，大量关键结果被推入 Appendix。

---

## Strengths

1. **理论贡献清晰且可验证**：偏差恒等式（Theorem 1）提供了精确的解析形式，R²≥0.974 的经验验证令人信服。这一理论结果本身具有独立价值——即使不采用 EC-HTE，从业者也可据此判断全局校正何时有害。

2. **实验覆盖面极广**：100 次 MC 重复、K∈{2,4,8}、对称/非对称混淆矩阵、6 个 OpenAI 模型 + 开源 LLM、hate speech 案例、子组误指定、A1 敏感性分析、混杂处理、R-learner 兼容性等——超过 20 个 Appendix 章节覆盖了几乎所有可预见的质疑。

3. **方法论位置清晰**：准确定位 EC-HTE 与 PPI/DSL/PPCI 的关系——全局校正等价于 pooled DSL，EC-HTE 添加分层部分池化——避免了过度声称新颖性。

4. **写作质量高**：主体正文在 8 页内呈现了完整的理论-方法-实验叙事，Introduction 的 Figure 1 三面板设计有效传达核心直觉。

5. **实用性**：诊断准则（尽管有局限）和预算指南（Appendix 的 crossover curves）为从业者提供了可操作的工具。

---

## Weaknesses

### Must-Fix（不修复则影响接收）

**[W-MF1] 摘要诊断 AUC 选择性报告** [R1 AGREE, R2 AGREE — 共识]
摘要称 "AUC = 0.86" 但仅限合成对称误差条件；在 16 个真实 LLM 模型-数据集组合上 AUC 降至 0.63（Appendix D.9）。对于 K=2，诊断甚至 anti-predict（§4.4 承认）。摘要应同时报告两个数字，或使用更保守的表述（如 "AUC up to 0.86 under symmetric errors; 0.63 on real LLM confusion matrices"）。这是诚实报告的问题，不修复会被审稿人标记为 misleading。

**[W-MF2] 主结果表缺乏代表性** [R1 AGREE, R2 AGREE — 共识]
Table 1 仅展示 extreme heterogeneity 配置，但 §4.3 承认 "moderate heterogeneity 下方法趋同"、"TweetEval 半合成实验中 EC-HTE RMSE 高于 Global"。主表应至少包含一个非极端配置（moderate 或 TweetEval），否则读者对方法的适用范围产生过于乐观的印象。当前 Table~\ref{tab:main_supp} 在 Appendix 中，但这些是读者最需要在主体看到的结果。

### Should-Fix（建议修复，不修复会扣分但不致命）

**[W-SF1] Algorithm 1 描述歧义** [R1 AGREE, R2 AGREE — 共识]
Algorithm 1 Step 2 "corrected labels" 与 Step 3 的操作存在歧义——EC-HTE 校正的是 moments（期望值）而非逐条标签。建议明确使用 "corrected outcome moments" 或等价表述，避免与逐条标签校正方法（如 PPCI）混淆。

**[W-SF2] K=8 可扩展性边界应在主体提及** [R1 AGREE, R2 AGREE — 共识]
K=8 时 EC-HTE RMSE 超过 Global（Appendix D.16），这是方法的重要边界条件。当前仅在 Limitations 一笔带过。建议在 §4.3 加一句明确提及此边界，或在 Table 1 增加 K=8 行。

**[W-SF3] 子组定义指导缺失** [R1 AGREE, R2 AGREE — 共识]
论文使用 hashtag presence 和 text length 定义子组，但未讨论从业者如何选择子组变量。当子组定义本身与 LLM 误差模式相关（如按文本长度分组，而 LLM 在短文本上系统性更差），子组选择就不是中性的。需要至少一段讨论。

**[W-SF4] 专家标注成本-收益分析不足** [R1 AGREE, R2 AGREE — 共识]
EC-HTE 需要按子组分配专家标注（每子组 ≥25），但论文未讨论相比全局方法，额外的子组级标注成本是否值得。预算 crossover curves 在 Appendix 但应在主体简要总结。

**[W-SF5] Theorem 1 "exact identity" 措辞** [R1 REBUT → R2 ACCEPT downgrade]
经交叉讨论，R1 的反驳成立——Theorem 1 推导出的是 finite-sample exact identity（非渐近近似），且与 Firth-Liang 方法的区分是实质性的。但建议在 proof sketch 中更明确说明 "exact" 的含义（有限样本精确 vs. 渐近），避免歧义。降级为 should-fix。

**[W-SF6] 缺乏真实因果数据集验证** [R1 AGREE, R2 AGREE — 共识]
所有 CATE 均为合成注入（即使在 "semi-synthetic" 中，文本特征真实但效应人工注入）。论文在 Limitations 中承认这一点，并指出 "suitable public benchmarks" 不存在。审稿人理解这是结构性限制，但建议讨论是否可使用 LaLonde/IHDP 等经典因果数据集（即使非 NLP 领域）作为补充验证。

### Minor

**[W-M1] 摘要信息密度过高** [R1 AGREE, R2 AGREE — 共识]
摘要包含 δ_s·Δτ 公式、R²≥0.97、AUC=0.86、5.9× 改善等密集技术细节，对非因果推断背景的 NLP 读者不够友好。建议简化数学表述，保留核心叙事。

**[W-M2] 方法新颖性有限** [R1 AGREE, R2 AGREE — 共识]
EC-HTE 的核心操作（分层贝叶斯混淆矩阵估计 + 矩校正）是识别问题后的自然修复步骤。主要贡献在于问题识别（偏差恒等式）而非解决方案本身。论文对此定位准确，但应进一步强调理论贡献的独立价值。

**[W-M3] Figure 2 轴标签字号偏小**
Heatmap 的轴标签和 colorbar 刻度约为正文字号的 60-65%，打印时可能不够清晰。

**[W-M4] A2 对称假设的影响范围应澄清**
经交叉讨论确认：A2（对称误分类）仅影响诊断准则（Proposition 3），不影响 EC-HTE 方法本身。建议在 Assumptions 列表中明确标注 A2 的适用范围（"used only for the diagnostic"）。

**[W-M5] 主体 display item 密度偏低**
8 页正文仅含 3 个 display items（Figure 1, Table 1, Figure 2），pages 3-6 为纯文本。建议考虑将 Appendix 中的 budget crossover figure 或 cross-model consistency 关键结果移入主体。

---

## Reviewer Consensus

以下问题两位审稿人达成完全共识：

1. **诊断 AUC 报告问题是最关键的修复项**——摘要的选择性报告构成 misleading risk
2. **Table 1 的代表性不足**——仅展示 extreme 配置给读者错误印象
3. **理论贡献 > 方法贡献**——偏差恒等式是核心贡献，EC-HTE 是自然延伸
4. **实验全面性是论文最大优势**——Appendix 的深度覆盖令人印象深刻
5. **论文适合 EMNLP**——NLP+因果推断的交叉主题、LLM 标注校正的实用性

## Reviewer Divergence

以下问题经交叉讨论后解决，无残留分歧：

1. **Theorem 1 "exact identity" 措辞**：R2 初审认为措辞有误导，R1 反驳 F-L 区分是实质性的。R2 接受降级为 should-fix，建议澄清 "exact" 的含义。
2. **A2 对称假设**：R1 初审认为 A2 限制了方法通用性，R2 指出 EC-HTE 本身不依赖 A2。达成共识：仅诊断受影响，方法不受限。
3. **SE plug-in 校准**：R1 标记 1.2pp 覆盖率缺口为 should-fix，R2 认为在 MC 误差范围内且提供了 bootstrap 替代方案。达成共识：minor issue。

---

## Questions for Authors

1. 在 K=4 TweetEval 半合成实验中，EC-HTE 的 RMSE (0.225) 显著高于 Global (0.124)。能否提供子组级别的分解，说明 RMSE 增加主要来自哪些子组？是否存在子组级别 EC-HTE 优于 Global 的情况？

2. 诊断准则在 K=2 时 anti-predict 的根本原因是 |δ₀|=|δ₁| 的代数约束。是否有修改诊断公式使其在 K=2 也可靠的理论路径？

3. 分层贝叶斯的 Gamma(3,1) 超先验选择依据是什么？是否进行了先验敏感性分析？

4. 子组变量选择（hashtag presence, text length）是否存在事后选择偏差？如果从业者尝试多个子组定义并选择"最好"的结果，如何控制多重比较问题？

---

## Missing References

未发现明显遗漏的关键引用。论文对 PPI、DSL、PPCI 等核心竞争方法的引用完整。建议考虑引用：
- Zrnic & Candès (2024) 关于 cross-prediction 的后续工作（如已发表）
- 因果推断中测量误差校正的经典统计文献（如 Carroll et al., Measurement Error in Nonlinear Models）中与混淆矩阵反演直接相关的章节

---

## External Review

未启用外部审稿。

---

## Visual Layout Check（非评分项）

**状态**: ✅ 完成
**结果**: 0 critical / 2 warning / 9 info

**Warnings**:
1. Pages 3-6 从 Figure 1 (p2) 到 Table 1 (p7) 跨越 5 页纯文本，视觉单调（text desert）。理论推导的 display equations 有一定缓解作用，但对实证+理论混合型论文而言偏长。
2. 主体 8 页仅含 3 个 display items（Figure 1, Table 1, Figure 2），密度偏低。建议将 1-2 个关键 Appendix 表格/图提入主体。

**Info（正面）**:
- Figure 1 位置得当（p2），三面板设计清晰
- Table 1 booktabs 格式规范，精度一致
- Figure 2 heatmap hatching 区分有效
- 数学公式渲染正确，无 LaTeX 错误
- 参考文献格式统一，无未解析引用
- 无 margin 溢出，符合 ACL 模板规范

---

## Overall Assessment

**评分: 3.5 — Borderline Conference**

**理由**：

论文在理论层面做出了有价值的贡献——偏差恒等式（Theorem 1）揭示了一个此前未被形式化的问题（全局混淆矩阵校正在子组间引入系统偏差），经验验证充分（R²≥0.97）。实验设计全面，鲁棒性验证覆盖面远超同类论文。

阻碍更高评分的主要因素：
1. **方法新颖性有限**：EC-HTE 是识别问题后的直接修复，贡献主要在问题发现而非解决方案
2. **诊断工具实用性存疑**：核心卖点之一的诊断准则在真实 LLM 数据上 AUC 仅 0.63，K=2 时 anti-predict
3. **摘要选择性报告**：AUC=0.86 的报告方式有 misleading risk，需立即修复
4. **缺乏真实因果验证**：所有效应为合成注入，尽管是结构性限制但削弱了对实际场景有效性的信心
5. **主表代表性不足**：仅展示 extreme 配置，隐藏了方法在中等异质性下的局限

论文整体质量适合 Findings 接收（3.0），但理论贡献的清晰度和实验的全面性使其有机会进入主会议（borderline）。修复 W-MF1（AUC 报告）和 W-MF2（Table 1 代表性）后，论文竞争力将显著提升。

---

## Detailed Comments

### 给作者的具体修改建议（按优先级排序）

1. **摘要 AUC 报告**（Must-Fix）：将 "AUC = 0.86" 改为 "AUC = 0.86 under synthetic symmetric errors (0.63 on real LLM confusion matrices)" 或类似表述。

2. **Table 1 扩展**（Must-Fix）：增加 moderate heterogeneity 行和/或 TweetEval 半合成行。如空间不够，可将 extreme+moderate 合并为单表，用子表头区分。

3. **Algorithm 1 措辞**（Should-Fix）：Step 2 "Compute corrected labels" → "Compute corrected outcome moments" 或 "Apply moment correction"。

4. **K=8 边界**（Should-Fix）：在 §4.3 末尾加一句："At K=8 with n_expert=250, EC-HTE maintains nominal coverage but RMSE exceeds global correction (Appendix X), establishing a practical scalability boundary."

5. **子组选择讨论**（Should-Fix）：在 §3 或 Limitations 中增加一段讨论子组变量选择的指导原则和潜在陷阱。

6. **A2 适用范围标注**（Minor）：在 Assumption (A2) 后括注 "(used for diagnostic only; EC-HTE correction does not require symmetric errors)"。

7. **Figure 2 字号**（Minor）：增大轴标签和 colorbar 刻度字号至正文字号的 80% 以上。
