---
round: 12
review_mode: fresh
overall_score: 3.0
timestamp: 2026-05-23T20:34:21.139670+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: True
---

# 圆桌审稿报告（修订版）：Error-Corrected Heterogeneous Treatment Effects

**论文**: Error-Corrected Heterogeneous Treatment Effects: When LLM Annotation Debiasing Hurts
**Venue**: EMNLP 2026 (ARR Long Paper)
**审稿模式**: Fresh (Round 18)
**Reviewer 配置**: 2 人（R1: 方法严谨性 + 实验设计；R2: 新颖性 + 完整性 + 写作）
**交叉回应**: 已完成（R1↔R2 双向 [AGREE]/[REBUT]，含扩展交叉轮次）
**修订说明**: 本报告替代此前提交的 3.5 分版本。R1 额外审查了一份非投稿 PDF（dream report, 9页），R2 拒绝审查该 PDF 但在交叉中验证了部分发现在提交版本（31页 submitted.pdf）中同样成立。以下评估严格基于提交版本，仅纳入经 R2 在提交版本中验证的发现。

---

## Summary

本文研究 LLM 标注误差对因果推断中异质性处理效应（HTE）估计的影响。核心贡献：(1) 偏差分解恒等式（Theorem 1），证明全局混淆矩阵校正在子群误分类率异质时引入与 δ_s·Δτ 成正比的偏差，14.9% 配置中反转 CATE 符号；(2) EC-HTE 方法，使用分层贝叶斯混淆矩阵估计进行子群级校正，合成数据上实现 7.4× 偏差缩减；(3) 无需估计 Δτ 的先验诊断准则。

---

## Strengths

**S1. 理论贡献扎实且有实践意义** [两位 Reviewer 一致]
Theorem 1 的 δ_s·Δτ/(1−2π̄) 乘积结构优雅且新颖，超越经典测量误差的衰减偏差分析。K=2 时为精确恒等式（R²=0.994），K=1 退化为 F-L 标量衰减，理论连贯。K>2 的推广（K=4: R²=0.974, tightness max 1.089）涉及非平凡的近似选择，贡献度高于 "routine derivation"。

**S2. 问题动机清晰，CSS 社区实践相关**
LLM 标注中 5× 跨子群误差率变异（Ashwin 2025）是真实问题。"全局校正可能有害" 的 negative result 本身对 CSS 社区有重要警示价值。

**S3. 实验覆盖面广，负面结果坦诚报告**
11/11 计划实验执行完毕；100 次 MC 运行；覆盖 K∈{2,4,8}、DIM/CausalForest、多种鲁棒性检查。论文在 Appendix R (Table 15) 坦诚报告真实数据失败——"HB EC-HTE underperforms global at all budgets"——体现科学诚信。

**S4. 方法设计合理**
分层贝叶斯 CM 估计（Dirichlet-Multinomial + 经验贝叶斯）在理论上有据，部分池化在子群间借力。κ>100 奇异性守卫防止数值不稳定。

**S5. 偏差恒等式的多维实证验证**
520 配置 grid + 11 模型-数据集组合（R²=0.975）+ 8 个 LLM（含 4 个开源模型）的验证组合有力支持理论预测。

---

## Weaknesses

### Must-Fix（不修复将影响接收）

**W-MF1. 假设 (A5) 与核心贡献存在根本张力** [两位 Reviewer 一致]
(A5) 要求跨子群同质处理效应 τ(z)=τ₀，但论文的存在理由是纠正异质 CATE 估计。Remark 2 仅给出 O(Δτ²) 非正式论证，需升级为正式命题。

**W-MF2. 真实数据实验 EC-HTE 全面劣于 naive 和 global** [R1 发现，R2 在提交版本中验证]
Appendix R, Table 15 明确记录：hate speech 案例中 EC-HTE avg |Bias| > naive > global，且在所有 expert budget 下均不如 global。论文诚实报告了此结果（表标题直接写 "underperforms"），但被放置在附录 20+ 页之后，主文 Table 1 仅展示正面的合成/半合成结果。

这是一个核心问题：**论文唯一的端到端真实数据验证中，proposed method 是最差的。** 失败根因（FNR=53.5%, 接近随机分类）定义了方法的边界条件，但：
- 主文未提及此结果
- Singularity guard (κ>100) 未捕获此场景（κ≈14.3）
- 当前仅有一个真实数据测试点，且落在 operating window 之外

### Should-Fix（修复将显著提升论文质量）

**W-SF1. Theorem 1 "exact identity" 声称需限定为 K=2**
K=2 时 R²=0.994（精确），K=4 时 R²=0.974（tightness max 1.089, ~9% 松弛）。K>2 时恒等式变为 first-order approximation，论文应明确区分。

**W-SF2. 诊断准则 AUC 在真实 LLM 上退化至 0.63**
主文 Section 5.4 呈现的 AUC=0.86 是合成数据结果；真实 LLM CM 上降至 0.63。"restricting to τ_s > 0 recovers AUC=1.0" 是循环论证。应在主文中更突出呈现 0.63。

**W-SF3. CausalForest RMSE tradeoff 讨论不足** [R1 发现，R2 验证]
EC-HTE 降低 bias 但增加 variance，净效果在部分配置下 RMSE 更高。论文未提供 bias-RMSE Pareto frontier 分析帮助实践者决策。Theorem 1 → CausalForest 的理论桥梁也缺失。

**W-SF4. PPCI 组合边际贡献有限** [R1 发现]
DGP C 中 PPCI alone bias=0.004 vs EC-HTE+PPCI=0.005——EC-HTE 的 marginal contribution 接近零。PPCI 所有配置 Coverage=1.0 暗示过度保守 CI（未报告 CI 宽度）。PPCI 组合缺乏理论支撑（顺序选择、coverage 保证、error 传播均未分析）。

**W-SF5. 方法 operating window 极窄且分散表述**
EC-HTE 有效需同时满足：extreme heterogeneity (Δπ>0.15) + 充足 expert budget (n≥250) + well-conditioned CM (FNR<~50%) + K≤4。在 K=2/moderate heterogeneity 下 "EC-HTE NEVER outperforms global"（§4.3 原文）。这些条件分散在 §4.3、Appendix R、Limitations 中，读者难以形成统一判断。

**W-SF6. 插件 SE 不足以作为默认推荐**
CausalForest 插件 SE 覆盖率 93.8%（低于名义 95%），不足覆盖集中在高误差子群。应推荐 bootstrap SE 为默认并报告计算成本。

**W-SF7. 半合成实验仅测试 Δπ=0.20 (extreme)** [R1 发现，R2 验证]
Table 14 显示真实 LLM 的 Δπ≈0.08-0.14，半合成用的 Δπ=0.20 是真实值的 1.4-2.5×。选择偏向展示 EC-HTE 优势的参数。

### Minor

**W-M1.** 结论（4 行）过于简短，未讨论更广泛影响或未来方向。

**W-M2.** Abstract "AUC=1.0" 未限定条件（仅 non-zero Δτ subgroups）。

**W-M3.** "14.9% of configurations" 的 configuration 定义在首次出现时未说明。

**W-M4.** Limitations 章节偏长（35行，约10个限制点），可适当压缩。

**W-M5.** K>2 时 Theorem 1 为近似而非精确恒等式，应在 Theorem 陈述旁注明。

**W-M6.** HB coverage 在部分 subgroup-regime 组合下低于 0.95（0.87-0.93），与 "calibrated inference" 声称存在张力。

**W-M7.** Dirichlet 超参数 (a₀, b₀) 的默认值和 empirical Bayes 实现细节未给出；hyperprior sensitivity ~4-5% RMSE variation 属 non-trivial。

**W-M8.** CausalForest 超参数（min_n, n_trees, max_depth, honesty）和 PPCI 超参数未报告。

---

## Reviewer Consensus（交叉后一致意见）

1. **(A5) 假设是最关键的理论问题**：需正式处理 τ 异质下的偏差恒等式精度
2. **论文的核心价值在于问题识别（"global correction can hurt"）而非方法贡献（EC-HTE）**：作为 "awareness paper" 对 CSS 社区有教育价值
3. **真实数据失败（Table 15）应在主文中提及**：当前放置位置构成信息不对称
4. **诊断 AUC 在真实场景下退化严重**：需在主文透明呈现
5. **实验覆盖面和负面结果的坦诚报告是论文的强项**
6. **Operating window 过窄但分散表述**：应集中讨论适用条件
7. **K>2 时 "exact identity" 变为近似**：需限定声称
8. **PPCI 组合边际贡献有限，Coverage=1.0 是过度保守信号**

---

## Reviewer Divergence（交叉后仍存在分歧）

| 编号 | 议题 | R1 立场 | R2 立场 | Director 裁定 |
|------|------|---------|---------|---------------|
| D1 | 真实数据失败的严重程度 | "Total failure"——方法在所有真实数据上可能都会失败 | "边界条件失败"——FNR=53.5% 接近随机，不代表所有真实数据 | **Should-fix**：失败是边界条件导致，但唯一真实数据点落在边界外这一事实本身是严重的。需要更多真实数据验证或至少在主文中讨论 |
| D2 | Theorem 1 novelty | Routine derivation in Fuller/Carroll framework | K>2 扩展涉及非平凡近似选择，贡献度高于 routine | **Moderate novelty**：K=2 为已知框架特化，K>2 有独立贡献但需诚实限定 |
| D3 | LLM Δπ 下降趋势的影响 | 问题正在 diminish（GPT-3.5 Δπ=0.198 → GPT-4.1 Δπ=0.117） | 特定领域（low-resource, adversarial）的 Δπ 可能持续高位 | **Valid concern but not decisive**：趋势存在但 long-tail 场景保持方法的相关性 |
| D4 | Soundness 评分 | 3.0（经验 R² ≠ 数学证明） | 3.5（完整证明在附录中，R² 验证充分） | **3.5**：提交版本有完整证明（Appendix B/C/D），R1 的"证明缺失"批评基于 dream 版本，不适用于提交版本 |
| D5 | Venue fit | Borderline：技术核心属计量经济学 | Acceptable：CSS+NLP 交叉论文，EMNLP 有先例 | **Borderline acceptable**：NLP-specific 贡献有限但问题与社区高度相关 |

---

## Questions for Authors

**Q1.** Theorem 1 在 τ(z) 异质时的精确余项是什么？Remark 2 的 O(Δτ²) 能否形式化为带显式常数的界？

**Q2.** Table 15 显示 EC-HTE 在 hate speech 数据上全 budget 劣于 global。是否有至少一个真实数据场景 EC-HTE 表现优于 global？如果没有，如何说服实践者在真实场景中使用该方法？

**Q3.** Singularity guard 阈值 κ>100 未能捕获 FNR=53.5% 的场景（κ≈14.3 但放大因子 1/(1-2×0.535)≈14.3×）。是否应降低阈值（如 κ>15）？这会对合成实验结果产生什么影响？

**Q4.** PPCI 所有配置 Coverage=1.0——CI 宽度是多少？与 EC-HTE 的 CI 宽度比是多少？如果 PPCI CI 宽度是 EC-HTE 的 5-10×，Coverage=1.0 不是优势而是缺陷。

**Q5.** DGP C 中 PPCI alone bias=0.004 vs EC-HTE+PPCI=0.005——EC-HTE 在组合中的 marginal 贡献是什么？在哪些 DGP 下 EC-HTE 的独立贡献显著？

---

## Missing References（建议补充）

1. **Zhang & Ding (2024)** — 高维 HTE 推断中的标准误校正，与 EC-HTE 的 SE 传播讨论相关
2. **Semenova & Chernozhukov (2021)** — Debiased ML of CATE：可在方法兼容性讨论中更明确引用

---

## External Review

❌ 未配置外部审稿。

---

## Visual Layout Check（非评分项）

⚠️ 视觉审查 Agent 超时（300s 内未完成）。未产生有效排版检查结果。

---

## Overall Assessment

**评分：3.0 — Findings**

**评分变化说明**：从初版报告的 3.5 (Borderline Conference) 下调至 3.0 (Findings)。调整基于扩展交叉轮次中 R2 在提交版本中验证的三个关键发现：

1. **真实数据完全失败**（Table 15）：EC-HTE 在唯一的端到端真实数据验证中全 budget 劣于 global——这是最严重的降分因素。论文诚实报告了此结果但放在附录深处，主文仅展示正面结果。
2. **PPCI 组合边际贡献近零**：DGP C 中 EC-HTE 在 PPCI 基础上几乎不提供额外改善，且 Coverage=1.0 暗示过度保守。
3. **Operating window 比初版报告评估的更窄**：综合真实数据失败 + K=2/moderate 永不优于 global + CausalForest RMSE tradeoff，方法的实际适用场景极为有限。

**核心判断**：论文的主要价值在于**问题识别**（"global correction can hurt under heterogeneous error"）和**定量刻画**（Theorem 1 的乘积结构），而非方法论贡献（EC-HTE）。作为一篇 Findings 论文，它对 CSS 社区有教育和警示价值。但方法在唯一真实数据上的失败、极窄的 operating window、以及诊断工具在真实场景下的 AUC 退化，阻止其进入主会议 consideration。

**提升路径（3.0 → 3.5 Borderline Conference）**：
1. [必须] 在主文中提及 Table 15 的真实数据结果（至少一句话 + 指向附录）
2. [必须] 正式处理 (A5) 松弛，将 Remark 2 升级为命题
3. [必须] 提供至少一个 EC-HTE 表现优于 global 的真实数据实验
4. [建议] 集中讨论 operating conditions，提供决策流程图
5. [建议] 限定 Theorem 1 "exact identity" 为 K=2，K>2 为 first-order approximation
6. [建议] 报告 PPCI CI 宽度，讨论 coverage vs power tradeoff

---

## Detailed Comments（按章节）

### Abstract
- "AUC=1.0" 需加限定条件（"on subgroups with non-zero Δτ"）
- 196 words，符合 200-word 限制
- 建议提及方法的适用条件限制

### Introduction
- Figure 1 有效传达核心信息
- "14.9% of configurations" 首次出现时需简要定义 configuration space
- 建议增加一句话提及真实数据验证的结果（包括正面和负面）

### Theory (Section 3)
- Theorem 1 推导清晰，符号一致
- (A5) 需在主文中更好地处理松弛情况
- K>2 时 identity 变为近似，应在 Theorem 陈述旁注明
- Proposition 3 推导正确但实用性受限

### Method (Section 4)
- 分层贝叶斯设计清晰
- κ>100 阈值可能过高（FNR=53.5% 场景未被捕获）
- PPCI 组合仅 4 句话，缺乏理论支撑
- Dirichlet 超参数实现细节不足

### Experiments (Section 5)
- Table 1 信息密度高
- R² 验证令人信服
- 主文仅展示正面结果，真实数据失败放在附录——构成信息不对称
- 半合成 Δπ=0.20 偏向 extreme regime，与真实 LLM Δπ≈0.08-0.14 不匹配
- Section 5.4 诊断部分需调整 AUC 呈现顺序

### Related Work
- 三段式结构清晰，引用覆盖充分
- 与 F-L 的区分到位
- K>2 novelty 可更明确讨论

### Limitations
- 内容翔实但偏长（35 行），建议压缩
- 应将 operating conditions 集中讨论

### Conclusion
- 过于简短（4 行），建议扩展

### Format Compliance
- ✅ ACL 模板，双盲，Anonymous author
- ✅ 8 页主文限制
- ✅ Limitations 章节存在
- ✅ 引用格式一致

---

## 版本混淆说明

审稿过程中 R1 额外审查了一份非投稿 PDF（dream_reports/.../review_input_e90a5c14.pdf, 9页，标题 "When Debiasing Backfires"）。该 PDF 与提交版本（submitted.pdf, 31页）存在显著差异：缺少主文 Figure、仅含 OpenAI 模型、不同的 AUC 数字（0.83/0.49 vs 1.0/0.86/0.63）、证明缺失。R2 正确识别了版本差异并拒绝审查该 PDF。

本报告严格基于提交版本（submitted.pdf）。仅纳入 R2 在提交版本附录中独立验证的发现（Table 15 真实数据失败、PPCI coverage=1.0、CausalForest RMSE tradeoff）。R1 基于 dream 版本的评分（2.5）不直接适用于提交版本。

最终评分基于：
- R1 对提交版本的初审：3.5 → 交叉后隐含 3.0-3.5
- R2 对提交版本的初审：3.5 → 交叉后更新至 3.0
- Director 综合：3.0 (Findings)