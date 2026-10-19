---
round: 7
review_mode: fresh
overall_score: 3.5 - Borderline Conference
timestamp: 2026-05-23T00:05:07.609984+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Consolidated Review Report — Round 7

**论文**: "Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction"
**Venue**: EMNLP 2026 (ACL ARR, Long Paper)
**Reviewer 编排**: 2 人（R1: 方法严谨性, R2: 新颖性与完整性）
**轮次**: Round 1（1 轮收敛，无需第 2 轮）

---

## Summary

本文针对 K-class 非差异性错分类在 7 种经典 DAG 拓扑下的偏差传播进行系统性理论分析，推导 probability limit 表达式，建立 Annotation Sensitivity Values (ASV) 敏感性分析框架，并证明 FWL 不变性导致矩阵校正方法在 4 种拓扑下完全无效。论文通过 23 个真实 LLM 配置 × 7 拓扑 = 161 个场景的经验验证（MAPE 1.6%），确认理论预测。贡献扎实且问题 timely，但存在可修复的命名不当、声称过强和验证范围不足问题。

---

## Strengths

**S1. 系统性跨拓扑比较的原创价值** [R1-S1, R2-S1, 双方一致]
首次在统一线性 SEM 框架下推导全部 7 种拓扑的 bias 表达式，揭示同一混淆矩阵在不同拓扑下产生质量上不同的偏差（attenuating vs. amplifying vs. sign-reversing）。Teblunthuis (2024) 覆盖 4 种拓扑但限于 binary；Lee & Wood-Doughty (2024) 只分析 confounding。"首次跨 7 种拓扑系统比较"的声明在两位 Reviewer 的检索范围内成立。

**S2. FWL 不变性负结果有实用价值** [R1-S3, R2-S2, 双方一致]
证明 matrix-based correction 对 4 种 covariate 拓扑下完全无效（0% bias reduction）——基于 FWL 定理的代数性质，论证完整且优雅。对 practitioners 选择校正方法有直接指导意义。R1 仔细审查了 Appendix B.2 的推导，确认代数正确。

**S3. 透明的三级证明层级** [R1-S2, R2-S4, 双方一致]
明确区分 analytically proved（Proposition 1, Theorem 1）、numerically verified（Proposition 2, 100K+ matrices）和 conjectured（Conjecture 1, ε-approximate bounds）三个层次。这种方法论诚实度在投稿论文中不常见。

**S4. 实验验证层次丰富** [R1-S5, R2-S3, 双方一致]
23 LLM 配置 × 7 拓扑 = 161 scenarios，grand MAPE 1.6%。包含 cross-K robustness (K=5,7)、logistic DGP 验证、non-differential stress test、bootstrap ASV CI——不是单一实验而是多层验证体系。ClinicalBERT case study (Appendix B.3) 展示端到端应用。

**S5. 实际问题导向** [R2-S5]
Figure 3 (F1 vs bias) 有效说明"F1 不预测因果风险"：在 F1=0.614–0.690 窄区间内 bias 跨拓扑变化 10×。对 CSS 实践者有直接警示价值。

---

## Weaknesses

### Must-Fix（影响接收决定）

**MF-1. [CRITICAL] "Primary coefficient never reverses" 声明的 evidence 不足以支撑其 prominence**
[R2-N2 首发 CRITICAL, R1 完全 AGREE CRITICAL]

- **位置**: Abstract ("in all 23 empirical configurations tested, the primary treatment effect does not reverse"), Section 3.2 footnote 2, Introduction paragraph 2
- **问题**: 该声明在 abstract 和 introduction 中以近乎 structural property 的语气呈现，但：(a) 仅基于 23 个经验配置——样本量极小；(b) 解释仅为 footnote 2 的 heuristic（"magnitude dominance"）——无 formal sufficient condition；(c) 论文自身在 Section 3.2 已使用 "empirical regularity"，但 abstract 措辞未反映这一谨慎性；(d) 未讨论 breakdown regime（如多个 coefficient magnitude 接近时）
- **R1 补充证据**: Appendix B.1 binarization 分析暗示在某些 K≥3 结构下 primary reversal 可能发生
- **要求**: (a) Abstract 中明确标注 "empirical regularity"；(b) 提供 formal sufficient condition（如 diagonal dominance threshold + coefficient magnitude ratio）或讨论 breakdown regime；(c) 降低 claim prominence

**MF-2. [MAJOR] ASV 框架与 E-value 的方法论差异需更清晰阐述**
[R2-N1 首发 CRITICAL, R1 AGREE with nuance 降为 MAJOR]

- **位置**: Section 3.3
- **问题**: 论文列举的三个 ASV vs E-value 差异偏表面：(1) ε-approximate monotonicity proof 是验证任务非方法创新；(2) three ASV types 本质是同一 idea 用不同 threshold；(3) FWL combination 是 routing 应用
- **R1 关键洞察**: 真正的方法论贡献被淹没——E-value 的 confounding 参数 Γ 的 monotonicity 是 trivially satisfied（Cinelli & Hazlett 2020 已证明），但 annotation error domain 中 monotonicity 非平凡（需 Theorem 1 + Conjecture 1），且拓扑依赖（confounding 递增, collider 递减）。这种 non-trivial topology-dependent monotonicity 是 E-value 框架中不存在的
- **R1 降级理由**: ASV 不是 E-value 的简单搬运——monotonicity 非平凡性本身就是方法论贡献，只是论文未凸显
- **要求**: 重构 ASV novelty 叙事——将 "monotonicity is non-trivial and topology-dependent" 作为核心方法论贡献阐述

### Should-Fix（影响评分但不一票否决）

**SF-1. [MAJOR] Proposition 2 命名与数值验证性质不匹配**
[R1-W1 首发 MAJOR, R2 AGREE]

- **位置**: Section 3.3 (page 5)
- **问题**: Proposition 2 的 "证明" 实质是 20,000 组随机矩阵的数值验证；在数学惯例中 "Proposition" 意味已证结果。Conjecture 1 正确使用 "Conjecture"，命名不一致更凸显问题
- **要求**: 改为 "Numerical Result 1" 或显式标注 "supported by numerical evidence; analytic proof remains open"

**SF-2. [MAJOR] Theorem 1 的 proportional effects 假设 (f=λg) 讨论不足**
[R1-W2 首发 MAJOR, R2 AGREE with nuance]

- **位置**: Theorem 1 (page 5), Appendix A.4 (page 13)
- **问题**: f=λg 在实际 NLP 场景（如政治立场 K=5）中不太可能严格成立。Appendix A.4 有 general case 数值验证（worst-case deviation < 0.005）但主文未充分引用
- **R2 补充**: Proposition 2 + Conjecture 1 为 general case 提供数值支撑；但 ε/η 在 weak effect 下可能放大误差
- **要求**: (a) 讨论 proportional effects 在 NLP 场景的合理性；(b) 主文引用 Appendix A.4 general case 数值验证

**SF-3. [MAJOR] 非差异性错分类压力测试覆盖不足**
[R1-W4 首发 MAJOR, R2 强烈 AGREE]

- **位置**: Appendix B.5 (Table 7)
- **问题**: 仅覆盖 r ∈ {0, 0.05, 0.1} 的 mild violations。实际场景（few-shot demonstrations 编码 outcome-treatment 关联, RLHF implicit correlations, RAG outcome signal）可能远超 r=0.1
- **R2 补充**: 当前 r 定义是均匀扰动所有 off-diagonal entries——实际 violation 可能是 structured
- **要求**: 扩展到 r ∈ {0.2, 0.3, 0.5}

**SF-4. [MAJOR] 线性 SEM 范围限制标注不够显著**
[R1-W7 首发 MINOR, R2-W1 首发 MAJOR, 交叉后共识 MAJOR]

- **位置**: Section 3.1, Section 4.5
- **问题**: Section 3.1 仅一句话提到 "linear structural equations"；FWL invariance 严格依赖线性假设但标注不突出
- **R1 纠正 R2 事实错误**: Appendix B.6 实际测试了全部 7 种拓扑（非仅 exposure）。但 R2 核心论点成立：sign-flip rate stability ≠ FWL invariance preservation
- **要求**: Section 3 开头和 Section 4.5 显著标注 linear scope

**SF-5. [MAJOR] ASV 对 C₀ 选择的敏感性未充分分析**
[R1-W3 首发 MAJOR, R2 AGREE]

- **位置**: Section 3.3, Appendix B.7
- **问题**: Bootstrap CI 回答了 sampling uncertainty，未回答不同 C₀ 估计方法的系统性差异。IV 的 95% CI [0.44, 1.29] 跨越 δ=1——point estimate 不可靠
- **要求**: 增加 C₀ 扰动分析或讨论 ranking robustness 条件

**SF-6. [MAJOR] 83.4% sign reversal 在 Section 4.2/Figure 2 中的呈现顺序有误导性**
[R2-W3 首发 MAJOR, R1 AGREE partially]

- **位置**: Section 4.2 paragraph 2, Figure 2 caption
- **问题**: Dirichlet(1,1,1) prior 对角元素期望仅 1/K≈0.33，对 realistic classifiers 不合理
- **R1 纠正**: Abstract 实际首先使用 realistic number (2.1%)；83.4% 主要出现在 Section 4.2 和 Figure 2
- **要求**: Section 4.2 重排呈现顺序——先 realistic rate (2.1%)，再 Dirichlet 分析作为理论极端

**SF-7. [MINOR] Method section 关键拓扑推导过于简略**
[R2-W2 首发 MAJOR, R1 REBUT partially 降为 MINOR]

- **问题**: Main text 仅给出 confounding/exposure/mediation 的公式，collider/M-bias/front-door/IV 仅有文字描述
- **R1 论证**: 8 页限制下合理权衡，完整推导在 Appendix A.3-A.8（共 10 页证明）
- **要求**: 添加一句声明指向 appendix

**SF-8. [MINOR] "154×" binarization bias 倍数来源不透明**
[R1-W6 首发 MINOR, R2 AGREE]

- **位置**: Introduction Contribution 1
- **要求**: 在 Appendix B.1 或正文中给出 154× 的具体计算基础

**SF-9. [MINOR] 缺少商业 LLM 实验配置**
[R2-W4 首发 MINOR→MAJOR, R1 REBUT partially 维持 MINOR]

- **问题**: 4 个 LLM 全部开源。R1 论证：理论贡献不依赖具体 LLM，API 成本和 reproducibility 是合理理由
- **要求**: Limitations 中讨论即可

**SF-10. [MINOR] 引用格式不统一**
[R2-W5 首发 MINOR, R1 AGREE]

- **问题**: Pangakis et al. (2023), Cheng et al. (2024), Cadei et al. (2025) 标为 arXiv preprint 但正文未标注状态
- **要求**: 统一标注 preprint 状态，检查是否已正式发表

---

## Reviewer Consensus [AGREE]

1. **Primary coefficient claim 过强** (MF-1)：两位 Reviewer 均评为 CRITICAL——本轮最需修改的声称
2. **ASV novelty 需更好阐述** (MF-2)：聚焦 monotonicity 非平凡性和拓扑依赖性
3. **Proposition 2 命名不当** (SF-1)：应反映数值验证性质
4. **Stress test 范围过窄** (SF-3)：r≤0.1 不足，需扩展到 r≥0.3
5. **Linear scope 标注不足** (SF-4)：对 NLP/CSS 受众需更显著标注
6. **核心理论贡献扎实**：7 拓扑 taxonomy、FWL invariance、三级证明体系均获双方肯定

## Reviewer Divergence [REBUT]

1. **ASV novelty severity**：R2 评 CRITICAL，R1 降为 MAJOR（R1 认为 monotonicity 非平凡性本身就是方法论贡献，只是论文未凸显）→ 最终采纳 **MAJOR**
2. **Method section brevity** (SF-7)：R2 评 MAJOR，R1 REBUT 为 MINOR（8 页限制下合理权衡）→ 最终采纳 **MINOR**
3. **83.4% framing** (SF-6)：R2 评 MAJOR，R1 partially AGREE 但纠正 Abstract 实际首先使用 realistic number → 最终维持 **MAJOR**（Section 4.2/Figure 2 仍需改进）
4. **Commercial LLM** (SF-9)：R2 升为 MAJOR，R1 REBUT 维持 MINOR → 最终采纳 **MINOR**
5. **矩阵覆盖充分性** (R1-W5)：R2 REBUT——20,000 对存在性验证目标 adequate（confidence > 99.99% for p=0.001 violation rate）→ 最终不列为 weakness

---

## Questions（需作者澄清）

**Q1.** Proposition 1(a) 的 sufficient condition (sign(τ)=sign(τ+B_OV)) 需要知道 B_OV 方向——实践者如何在不知道 B_OV 的情况下判断 sign preservation？ASV 框架能否间接回答此问题？ [R2-Q1, R1 AGREE]

**Q2.** Table 9 (Appendix B.10) 显示 ASV ranking 依赖 β 配置。"Vulnerability spectrum from IV to M-bias" 是否仅端点（IV 最脆弱, M-bias 最稳健）稳定而中间排名可变？ [R2-Q2, R1 AGREE — 端点稳定，中间排名可变]

**Q3.** Theorem 1 的 (C₀)_jj ≥ 1/2 条件在 K=10 (HumAID) 时是否对所有 j 成立？论文应报告 HumAID confusion matrices 的 per-class diagonal 分布。 [R1-Q1, R2 AGREE]

**Q4.** Non-differential stress test 仅测试到 r=0.1。在 few-shot prompting 下 differential 程度可能远超——是否有更大 r 下的结果？ [R2-Q3, R1-W4 共同提出]

**Q5.** IV 的 bootstrap ASV CI [0.44, 1.29] 跨越 δ=1 boundary。对 IV 拓扑，ASV point estimate 是否不可靠？论文应在 main text 提及此限制。 [R2-Q4, R1 AGREE]

**Q6.** Conjecture 1 的 ε/η 精度：η 小时 ε/η 可以很大。R1 REBUT 认为 bootstrapping 缓解此问题（practical worst-case deviation 远小于 ε bound），但建议论文添加解释。 [R2-Q5, R1 REBUT with suggested addition]

**Q7.** Algorithm 1 (p.26) 的 risk threshold 0.1 选择依据？不同 application domain 是否应使用不同 threshold？ [R2-Q6, R1 AGREE]

---

## Missing References

**R2 建议（R1 AGREE partially）:**
1. Wei, He, Li & Geng (2025) "Multiply robust causal inference in the presence of an error-prone treatment" — Statistical Methods in Medical Research. 直接处理 error-prone treatment 因果推断
2. Demirel et al. (2024) "Prediction-powered Generalization of Causal Inferences" (ICML 2024) — PPI 在 causal setting 的 generalization
3. Cheng et al. (2024) → 检查 2025 年 2 月更新版本是否已正式发表

**R1 可选补充:**
4. Fong, Hazlett, and Imai (2018) "Covariate Balancing Propensity Score for a Continuous Treatment" — 与 ASV 方法论有对话空间（非必需）

---

## External Review (Stanford Agentic Reviewer)

未请求（项目未配置外部审稿）。

---

## Visual Layout Check（非评分项）

**状态: error**
视觉审查 Agent 因 API 限额耗尽退出（"You've hit your limit · resets 4pm (UTC)"）。无排版审查结果可用。用户可在限额重置后重新触发。

---

## Overall Assessment

**Overall Score: 3.5 / 5 — Borderline Conference**

| 维度 | R1 | R2 | 综合 |
|------|-----|-----|------|
| Soundness | 4.0 | 3.5 | 3.75 |
| Excitement | 3.5 | 3.0 | 3.25 |
| Reproducibility | 4.0 | 4.0 | 4.0 |

**置信度**: 4/5（两位 Reviewer 均有相关领域经验，仔细审查了推导和实验）

**判断依据**:
- 论文解决了一个 timely 且重要的问题（LLM annotation error × causal inference），跨 7 种 DAG 拓扑的系统比较是 genuinely novel 的综合贡献
- 理论核心（FWL invariance、sign preservation proofs for confounding/collider）扎实
- 实验验证多层次且 MAPE 1.6% 的 theory-MC agreement 令人信服
- 但存在两类可修复问题阻碍达到 Conference 水准：
  - (1) **声称与证据的匹配性**：primary coefficient claim 过强、ASV novelty 阐述不足
  - (2) **验证范围的完整性**：stress test r 范围过窄、C₀ sensitivity 未分析、proportional effects 讨论不足

**从 3.5 到 4.0 的路径**（两位 Reviewer 共识）:
1. **MF-1**: 将 "primary coefficient never reverses" 降级为 empirical regularity，提供 sufficient condition 或讨论 breakdown regime
2. **MF-2**: 重构 ASV novelty 叙事——聚焦 monotonicity 非平凡性和拓扑依赖性作为核心贡献
3. **SF-1**: Proposition 2 命名反映数值验证性质
4. **SF-3**: 扩展 non-differential stress test 到 r ≥ 0.3
5. **SF-4**: 在 Section 3 开头和 Section 4.5 显著标注 linear scope

如果 MF-1 和 MF-2 能 adequately address，加上 SF-1/SF-3/SF-4 的修改，论文可达到 **4.0 (Conference)** 水准。

---

## Detailed Comments（逐节）

### Abstract
- 信息密度仍偏高（至少 8 个 specific 数字），但整体可读
- "the primary treatment effect does not reverse" → 需降级为 empirical regularity (MF-1)
- 数值（2.1% sign reversal under realistic accuracy）与 Section 4.2 一致

### Introduction
- Paragraph 1 的叙事逻辑清晰：LLM annotation 普及 → multi-class 是主流 → error propagation 依赖 structure 和 topology
- Contribution 2 (ASV) 的 novelty 需加强阐述 (MF-2)
- "154×" binarization claim 来源不透明 (SF-8)

### Related Work
- 覆盖面广泛且组织合理（measurement error / LLM annotation / sensitivity analysis 三条线）
- 与 prior work 的差异化表述清晰
- R1 确认引用覆盖充分；R2 建议补充 2-3 篇新引用

### Method (Section 3)
- Definition 1 (non-differential misclassification) 清晰严格
- Confounding (Eq.1), Exposure (Eq.2), Mediation (Eq.3) 推导正确
- Collider/M-bias/Front-door/IV 在 main text 仅有文字描述——8 页限制下可接受但应明确指向 appendix (SF-7)
- Proposition 1(a)(b)(c) 证明正确；(a) 的 sufficient condition 需实践指导 (Q1)
- Theorem 1 证明完整但 proportional effects 限制需讨论 (SF-2)
- Proposition 2 命名需修正 (SF-1)
- ASV 三种类型定义严格，但 ε threshold 选择缺乏讨论

### Experiments (Section 4)
- Theory-MC agreement MAPE 1.6% 令人信服
- Figure 3 (F1 vs bias) 是论文中最 effective 的可视化
- Table 1 格式清晰但 "Violation"/"Amplif." 列需在 caption 中定义
- Correction guidance (Section 4.5) "no single method dominates" 有实用价值
- Section 4.2 呈现顺序应改进 (SF-6)

### Conclusion & Limitations
- Limitations 覆盖了主要 scope restrictions
- 应补充商业 LLM 限制说明 (SF-9)

### Appendix
- 附录质量高，推导完整（Appendix A 共 10 页 proofs）
- Appendix B.5 stress test r 范围过窄 (SF-3)
- Appendix B.7 bootstrap CI 结果对 IV 的 implication 应在 main text 提及 (Q5)
- Appendix B.10 ASV stability 显示中间拓扑排名可变——值得在 main text 提及 (Q2)