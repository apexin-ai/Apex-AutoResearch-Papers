---
round: 8
review_mode: fresh
overall_score: 3.0
timestamp: 2026-05-22T12:54:15.520581+00:00
reviewer_ids: ['1', '2']
cross_response_reviewer_ids: ['1', '2']
force_resubmit: False
---

# 审稿报告 — Round 8 (Fresh Review)

**论文**: Mapping the Detectability Landscape of Iterative Model Collapse
**Venue**: EMNLP 2026 (via ACL Rolling Review)
**审稿模式**: Fresh（独立重审，无上轮记忆）
**Reviewer 编排**: 2 名 Reviewer + 视觉审查 Agent
- Reviewer 1: 方法严谨性 + 统计分析 + 实验设计
- Reviewer 2: 新颖性/贡献定位 + 完整性 + 格式合规

---

## Summary

本文系统刻画迭代模型坍塌的可检测性，在 13 个污染水平（含 null control）和 5 个模型族（345M–6.9B）上比较五种统计检测方法，提出 permutation Granger causality (PermG) 作为最优方法，并拟合幂律检测边界 α_c(T) ∝ T^{−γ}。论文还建立了 entropy Granger-precedes diversity 的级联排序（Proposition 1-2），并展示了 canary-triggered cessation 的 proof-of-concept intervention。实验设计规模大（189 实验、25 页附录、1160 specifications 的稳健性检验），诚实报告负面结果，但核心统计声明和理论贡献在多处存在方法论漏洞。

---

## Strengths

**S1. 系统性的多方法比较框架。** 5 种检测方法 × 13 α 水平 × 多 T × 多 seed 的交叉比较，引入 MMCT 共识检验和 Shapley 贡献分析，在方法论上超越现有工作。（R1-S1, R2-S1）

**S2. 诚实报告失败案例。** 5/15 跨架构未 confirm、α=0.60 sync dip、intervention 仅为 PoC——负面结果的坦诚报告体现学术诚信。（R1-S2）

**S3. 极为丰富的稳健性检验。** Permutation count stability、FDR threshold sensitivity、specification curve (1160 specs)、DGP power simulation、non-stationarity robustness、Shapley value analysis。这种程度在 NLP 论文中罕见。（R1-S3, R2-S3）

**S4. Granger precedence vs. causation 区分贯穿全文。** 脚注 1、§6、Appendix L 多处明确声明 claim 范围。（R1-S4, R2-S6）

**S5. 可复现性高。** Appendix A 完整超参数、Algorithm 1 (MMCT) 伪代码清晰、Table 3 完整 metric drift 数据。（R1 Reproducibility 4.0, R2 Reproducibility 4.0）

**S6. Figure 1 信息密度高。** Detection phase diagram 直观传达核心发现，Caption 自包含。（R2-S5）

---

## Weaknesses

### CRITICAL

**C1. FPR=0% 声明不可靠（F3-J4）** [R1-W1, R2 强 AGREE]
主文 §4.1 和 Abstract 突出 "zero null-control FPR"，但仅有 3 seeds × 8 pairs = 24 null-control observations，ICC=0.34（种子内非独立），cluster-adjusted Clopper-Pearson 97.5% CI 为 **[0%, 41%]**。真实 FPR 可能高达 41%——此时 PermG 相对 Toda-Yamamoto (FPR≈17%) 的优势不再显著。FPR=0% 驱动了 MMCT 权重分配和 Shapley 优势分析，是论文核心卖点之一。主文必须报告 cluster-adjusted CI，而非将其埋在 Appendix Q 17 页之后。

**C2. Proposition 3 本质是 curve fitting，非理论推导（F2-W4b）** [R2-W1, R1 AGREE]
Sub-linear signal model S(α) = cα^β 的假设本身来自数据拟合（β=0.66, CI [0.24, 0.78]），非从 mode amplification 或训练动力学推导。推导链循环：拟合 → 解析形式 → "预测"拟合数据来源。Cross-T validation 只验证了曲线拟合质量而非理论预测力。β CI 兼容线性 (β≈1) 和强凹 (β≈0.25) 两种截然不同的动力学。

**C3. T=10 power≈37%，sharp onset 可能是 power artifact（F5-N2）** [R1-W3, R2 AGREE with nuance]
Appendix N 显示 T=10、β=3 下 PermG power 仅约 37%。0/8→6/8 的 "sharp detection onset" 可解释为低 power 下 power curve 从 ~0% 跳到 ~37% 的表象。R2 指出跨种子一致性和 α≈0.50 的物理意义（合成数据占 majority 的临界点）提供部分反驳——onset 存在性可能真实，但 sharpness degree 可能被低 power 放大。Proposition 3 可能是对统计伪影的过度解读。

**C4. "Detectability landscape" framing 承诺超过交付（F2-W2b）** [R2-W2, R1 AGREE]
"Landscape" 暗示多维空间的系统映射，但实际交付的是 (α, T) → detectable/not-detectable 的二元边界，主要来自 Pythia-410M 单一架构。跨架构验证 5/15 条件不 confirm（涵盖 precision, bidirectional confounding, seed dependence, architecture-specific decoupling 四种不同机制）。更准确的定位是 "detection boundary characterization" 或 "statistical power mapping"。

### MAJOR

**M1. fp32/bf16 precision sensitivity（F2-W1）** [R1-W2 (方向错误被 R2 纠正), R2 partial AGREE]
注：R1 声称 "fp32 0/8, bf16 8/8"——**方向错误**，论文原文 §5.5: bf16 0/8, fp32 6/8。但 underlying concern 有效：低精度训练（工业界默认 bf16/fp16）下 PermG 可能完全失效。论文讨论不够充分（仅 §5.5 一句 + Limitations 一句）。

**M2. 5/15 跨架构失败削弱泛化性（F2-W10）** [R1-W5, R2-W3, 双方 AGREE]
失败涵盖 4 种机制：precision sensitivity (GPT-2 bf16 0/8 vs fp32 6/8)、bidirectional confounding (GPT-2 s43)、seed dependence (Pythia-1.4B s42 2/8 vs s43 6/8)、architecture-specific decoupling (SmolLM3-3B 3/8, entropy 0/4)。SmolLM3-3B entropy 完全失效尤其严重——entropy 是 Proposition 1 的核心 canary metric，如果 >1B 模型不满足 mode amplification 假设，理论框架的适用范围被根本性限制。§5.5 仅两段讨论不足。

**M3. Entropy → distinct-n 机械耦合未排除（F2-W5）** [R1-W6, R2 强 AGREE]
R2 称此为"R1 最有洞察力的一条"。Token entropy 和 distinct-n 均从 token frequency distribution 计算，lead-lag 可能仅是度量灵敏度差异——entropy 对分布变化一阶敏感，distinct-n（counting measure）需要更大偏移才触发。缺少用非 token-distribution-based 度量（如 embedding-space 覆盖度、下游 task accuracy）替代 distinct-n 的验证。

**M4. Intervention 实验过于初步（F2-W7）** [R1-W7, R2 AGREE]
四重局限：(1) 15% entropy drop 阈值 post-hoc 选择无 hold-out validation；(2) 仅 2 个模型；(3) 仅 α=1.0（最极端场景）；(4) 95% CI 29-64% 极宽。不足以支撑 Abstract 中的 intervention 声明。

**M5. Proposition 1 over-framed（F5-N1/F5-W1）** [R2-W5, R1 partial REBUT]
核心步骤是 Jensen 不等式的直接应用。R1 认为 formalization 本身有价值（为 canary metric 选择提供 principled basis），但同意 Assumption 4 (Mode Amplification) 的适用边界未讨论——SmolLM3-3B 恰好是 Assumption 4 失效的实证。共识：应定位为 "formalized observation" 而非 "theoretical contribution"，并在正文讨论 Assumption 4 何时成立/不成立。

**M6. Discussion 过于简短（F8-C2）** [R2-W4, R1 AGREE]
§6 约 100 词。缺少：(a) 跨架构 failure 的 root cause 分析；(b) 与 Schaeffer et al. (2025) 8 种 collapse 定义的映射；(c) α 未知时的实际部署讨论；(d) Appendix L 的 domain-dependent directionality 发现（WikiText PermG reverse=0/8 全条件 forward，C4 reverse 7/8——这一重要限制被埋在 Appendix 中）。建议扩展至 300+ 词。

**M7. Schaeffer et al. 关系不清（F8-C3）** [R2-W6, R1 AGREE]
§2 仅一句引用。论文检测框架最接近 Schaeffer 分类中的 "distributional shift" (D4-D6)，而非 "performance collapse" 或 "mode collapse"。应明确映射以界定 "detectability landscape" 的 scope。

**M8. Detection boundary 零自由度拟合（F2-W6）** [R1-W4, R2 AGREE]
α_c(T) = A·T^{-γ} 有 2 参数，主要训练 T∈{10, 20}——零自由度。LOO-CV 测试集也仅 2 个 T 值。T 范围 [5, 20] 无法区分 power law 与其他单调递减函数。Appendix Z 的 V1/V2 predict-then-verify 存在 post-hoc adjustment 嫌疑（V1 git-committed 用 raw p-values, V2 not committed 改用 BH-FDR）。

**M9. BH-FDR 在强依赖下适用性（F8-N1）** [R1-W8, R2 partial AGREE]
R2 指出 R1 可能混淆时间序列自相关（由 Granger 检验 lag 结构处理）与跨 metric pair 相关（影响 BH-FDR 有效性）两个层面。但论文确实应报告跨 pair correlation 结构并讨论 PRDS 假设适用性。

### MINOR

**m1.** 未讨论选择经典 permutation Granger 而非 neural GC 的理由（R2-W7, R1 降级 MINOR）——T≤20 极短序列是合理理由但应显式说明。

**m2.** "13 contamination levels" 未集中列出全部 α 值（R2-W8）。

**m3.** Figure 1/2 子图内文字偏小，Figure 2 灰度打印下线色难区分（R2-W9, Visual Check consistent）。

**m4.** Appendix 关键验证（T=20 predict-then-verify, power analysis）应摘要纳入正文（R2-W10, R1 AGREE）。

**m5.** Granger "precedence" vs "causality" 术语不一致（R1-W10, R2 AGREE）。

**m6.** Naive cross-correlation 的纳入——R1 认为有 straw-man 嫌疑，R2 反驳认为是标准做法有教育价值。

---

## Reviewer Consensus [AGREE]

以下问题两位 Reviewer 达成明确共识：

1. **FPR CI 必须入主文**：主文 §4.1 和 Abstract 必须报告 cluster-adjusted CI [0%, 41%]，不能仅报告点估计 0%。
2. **Proposition 3 降级**：应定位为 "empirical scaling observation" 而非理论推导。β 缺乏独立于数据的理论 justification。
3. **跨架构失败需深入分析**：5/15 失败涵盖 4 种不同机制，当前讨论不足。SmolLM3-3B entropy 0/4 威胁 Proposition 1 核心 claim。
4. **Discussion 需扩展**：覆盖 failure analysis、Schaeffer 定义映射、部署讨论、domain-dependent directionality。
5. **机械耦合是关键问题**：entropy → distinct-n 的 lead-lag 可能是度量灵敏度差异，需用非 token-distribution-based 度量验证。
6. **Intervention 降级为 PoC**：当前证据不足以支撑更强声明。
7. **Framing 需调整**："detectability landscape" 承诺超过交付，应更精确定位。

---

## Reviewer Divergence

1. **fp32/bf16 方向**：R1 引用方向错误（fp32 0/8, bf16 8/8），被 R2 纠正为 bf16 0/8, fp32 6/8。R1 的 underlying concern（precision sensitivity）有效，但事实错误需注意。
2. **Proposition 1 的价值**：R1 认为 formalization 有独立价值（partial REBUT R2-W5），R2 认为仅是 Jensen 不等式。共识：有价值但应降级。
3. **Naive XCor straw-man**：R1 认为有嫌疑，R2 反驳为标准做法。分歧未影响整体评分。
4. **Sharp onset 的性质**：R2 部分反驳 R1 的 "完全是 power artifact" 强结论，指出跨种子一致性和 α≈0.50 物理意义。共识：存在性可能真实，但 sharpness 可能被放大。
5. **BH-FDR 层面混淆**：R2 指出 R1 可能混淆两个层面的相关性。但双方同意论文应报告跨 pair correlation 结构。

---

## Questions（需要作者澄清）

**Q1.** 更大规模 null simulation（10+ seeds 或 bootstrap）下 PermG FPR 点估计是否仍为 0%？

**Q2.** α=0.60 sync dip 位置是否随训练超参（lr, batch size, warmup）变化？实际部署中如何避免恰好处于 sync dip？

**Q3.** 在 T≥25 上 onset sharpness 是否增加？如果 sharp onset 是真实效应，更高 power 下应看到更陡 sigmoid。

**Q4.** 推荐的最低部署要求是 T≥ 多少才能达到 power≥80%？

**Q5.** SmolLM3-3B entropy 0/4 是否意味着 >1B 模型的 entropy 不再是有效 canary metric？Assumption 4 的适用边界是什么？

**Q6.** 用非 token-distribution-based 度量（如 embedding-space 覆盖度、下游 task accuracy）替代 distinct-n，Granger precedence 是否仍成立？

**Q7.** Proposition 3 的 β 参数有无独立于 Pythia-410M 数据的理论 justification？新架构/新 domain 是否需要重新拟合？

**Q8.** Appendix Z 的 V1→V2 修改（raw p-values → BH-FDR）是否构成 pre-registration 后的 protocol deviation？

**Q9.** 请集中列出全部 13 个 contamination level 的 α 值。

---

## Missing References

1. **Online/continual learning 下 model collapse 检测**：实际部署通常是 continual learning，与论文 iterative from-scratch 设定差异大。（R1, R2 双方 AGREE）
2. **Gerstgrasser et al. (2024)** data accumulation vs iterative replacement 的关系讨论不足。（R2）
3. **Dohmatob et al. (2024)** scaling law 视角：两种 scaling law 的异同未充分对比。（R2）
4. **Masur & Scharkow (2020)** multiverse analysis 方法论改进——与 Appendix E specification curve 相关。（R2）

---

## External Review (Stanford Agentic Reviewer)

**状态：未启用。** 项目配置未开启外部审稿（`external_review.paperreview_ai.enabled` 未配置）。

---

## Visual Layout Check（非评分项）

**状态：已完成。** 0 critical / 3 warning / 13 info。

主要发现：
- **Warning 1**: 前 2 页纯文本（Abstract + Introduction + Related Work 开头），无 display item。第一个视觉锚点（Figure 1）直到第 3 页才出现。建议将 Figure 1 提前或在 Introduction 加入概念示意图。
- **Warning 2**: 第 4-5 页（Method 章节）连续纯文本，无 figure/table。公式提供部分视觉变化但对非理论背景审稿人仍显单调。
- **Warning 3**: 末页（p.25）严重空白——Table 30 仅占约 1/4 页面，下方 ~75% 空白。建议合并或填充。
- **Info**: 主文 8 页共 4 个 display items（Figure 1-2, Table 1-2），密度 0.5/页，偏低端。Figure 1 热力图内数字字号偏小（约正文 60%）。Figure 2 灰度打印下线色可能难区分。主体 8 页合规，匿名化正确，引用格式正常。

---

## Overall Assessment

### ARR 官方维度打分（综合两位 Reviewer）

| 维度 | R1 | R2 | 综合 | 理由 |
|------|----|----|------|------|
| **Soundness** | 2.5/5 | 3.5/5 | **3.0/5** | 实验设计扎实但核心统计声明有漏洞：FPR CI 过宽（C1），power 不足致 onset 可能是 artifact（C3），boundary 拟合零 DF（M8），机械耦合未排除（M3） |
| **Excitement** | 3.0/5 | 3.0/5 | **3.0/5** | "Detectability landscape" 概念有价值，系统性实验设计少见。但核心方法是现有工具直接应用，framing 承诺超过交付（C4） |
| **Reproducibility** | 4.0/5 | 4.0/5 | **4.0/5** | 超参数完整、算法伪代码清晰、metric drift 数据齐全。未提供代码但信息足够复现 |

### Overall Score

**Overall: 3.0 — Findings**

**Confidence: 4/5**（两位 Reviewer 独立给出一致评分，交叉回应后共识进一步巩固）

### 评分理由

论文是一项实验设计出色、稳健性验证充分的 empirical study。189 个实验、25 页附录、1160 specifications 的工作量值得肯定。将 model collapse 检测从方法论上系统化（多方法比较、FPR 校准、specification curve）是有价值的贡献方向。

但四个 CRITICAL 问题阻止了 Conference 接收：
1. **核心统计声明的支撑不足**：FPR=0% 的 cluster-adjusted CI [0%, 41%] 使得 PermG 的优势声明不可靠；
2. **理论贡献被 over-framed**：Proposition 3 是 curve fitting 而非理论推导，Proposition 1 仅是 Jensen 不等式的 formalization；
3. **泛化性未建立**：5/15 跨架构条件未 confirm，SmolLM3-3B entropy 完全失效；
4. **Framing 落差**："detectability landscape" 的承诺与 "detection boundary on single architecture" 的交付之间存在显著差距。

### 升至 3.5 (Borderline Conference) 的条件

1. 主文报告 FPR cluster-adjusted CI，并在 FPR=10% 假设下做 MMCT sensitivity analysis
2. Proposition 3 降级为 empirical scaling observation，Proposition 1 降级为 formalized observation
3. 扩展 Discussion 至 300+ 词，含 Schaeffer 定义映射、跨架构 failure analysis、Assumption 4 适用边界
4. 调整 framing：标题/Abstract 更精确地反映实际交付（detection boundary characterization）
5. 将 T=20 predict-then-verify 和 power analysis 关键结果纳入正文

### 降至 2.5 (Borderline Findings) 的风险

如果机械耦合问题（M3）被进一步证实（即用非 token-distribution-based 度量后 Granger precedence 消失），论文的核心 claim（entropy leads diversity）将从因果关系降级为灵敏度差异描述，贡献将大幅缩水。

---

## Detailed Comments

### §1 Introduction
- "13 contamination levels" 应集中列出全部 α 值（m2）
- "any nonzero contamination produces signal" 的表述需注意——这依赖于 α_∞≈0 的外推，而 power law 模型本身是 empirical fit（C2）

### §3 Cascade Ordering
- Proposition 1: 将 "Entropy leads diversity" 改为 "Entropy responds before diversity under mode amplification"——后者更精确且避免因果含义
- 需在正文讨论 Assumption 4 (Mode Amplification) 的适用边界，特别是 SmolLM3-3B entropy 0/4 作为反例

### §4.1 Method Sensitivity Analysis
- "PermG 0% [0, 0]" 必须改为 "PermG 0% [0, 41%] (cluster-adjusted)"
- 增加 1-2 句解释为何选择经典 permutation Granger 而非 neural GC（T≤20 极短序列）

### §4.2 Detection Boundary
- Proposition 3 标题改为 "Empirical detection boundary scaling" 或类似
- 报告 β 的 bootstrap CI 和模型比较（power law vs exponential vs logarithmic）

### §5.2 Sharp Detection Onset
- 需明确讨论 power≈37% 对 onset sharpness 的量化影响
- 报告 power curve 作为 α 的函数（而非仅在固定 β 处）

### §5.5 Cross-Architecture Validation
- SmolLM3-3B entropy 0/4 需要单独分析段落
- 对每个 failure mode 至少一段 root cause 分析

### §5.6 Intervention
- 开头明确标注 "proof-of-concept under favorable conditions"
- 讨论 threshold 的 hold-out validation 和多 α 测试作为 future work

### §6 Discussion
- 当前约 100 词，需扩展至 300-400 词
- 必须覆盖：Schaeffer 定义映射、5/15 failure analysis、α 未知时的部署讨论、domain-dependent directionality（从 Appendix L 提入）

### Limitations
- 当前覆盖充分（3 个核心点），长度适中，符合 EMNLP 要求

### References
- 确认 du2026geometric 引用 arXiv ID/标题/研究对象是否已修正
- 补充 online/continual learning 相关引用
